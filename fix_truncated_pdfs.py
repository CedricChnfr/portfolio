#!/usr/bin/env python3
"""
Script pour remplacer les PDFs tronqués sur le serveur distant
par les originaux complets depuis le répertoire local INSA.

UTILISATION:
    cd /chemin/vers/INSA
    python3 fix_truncated_pdfs.py

Le script:
  1. Lit TRUNCATED_PDFS.txt pour connaitre les fichiers tronqués
  2. Cherche le fichier local correspondant (gère les _ vs espaces)
  3. L'envoie sur le serveur via scp pour remplacer le tronqué
"""

import sys
import subprocess
import re
from pathlib import Path

# ============ CONFIGURATION ============
REMOTE_USER = "user"
REMOTE_HOST = "192.168.2.45"
REMOTE_PORTFOLIO = "/home/user/cedric/portfolio"
TRUNCATED_FILE = "TRUNCATED_PDFS.txt"
# =======================================

# Couleurs terminal
class C:
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    END = "\033[0m"


def parse_truncated_file(filepath: str) -> dict[str, list[str]]:
    """Parse TRUNCATED_PDFS.txt et retourne les chemins par section."""
    sections: dict[str, list[str]] = {}
    current_section = None

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or (line.startswith("#") and not line.startswith("## ")):
                continue

            # Détection des headers de section: ## cours-pdf/ ... ou ## file/reports/ ...
            if line.startswith("## "):
                # Extraire le prefix de chemin distant
                # Ex: "## cours-pdf/ (157 fichiers)" -> "cours-pdf"
                # Ex: "## file/reports/ (fichiers tronqués)" -> "file/reports"
                match = re.match(r"## ([\w/\-]+)/", line)
                if match:
                    current_section = match.group(1)
                    sections[current_section] = []
                else:
                    current_section = None
                continue

            if current_section is None:
                continue

            # Lignes de données: "1048576\tchemin/du/fichier.pdf"
            parts = line.split("\t")
            if len(parts) == 2 and parts[1].endswith(".pdf"):
                remote_path = parts[1].strip()
                # Ignorer les entrées "(1).pdf" sans chemin complet
                if remote_path.startswith("("):
                    continue
                sections[current_section].append(remote_path)

    return sections


def find_local_file(remote_path: str, section: str, local_base: Path) -> Path | None:
    """
    Trouve le fichier local correspondant au chemin distant.

    Le serveur utilise des underscores dans les noms, le local peut avoir
    des espaces. On essaie plusieurs variantes.

    Pour cours-pdf: le chemin distant est "cours-pdf/S1/Anglais/file.pdf"
                    le local est "./S1/Anglais/file.pdf" (depuis INSA/)
    Pour file/reports: le chemin distant est "file/reports/S5/rapport.pdf"
                       le local est "./reports/S5/rapport.pdf" ou "./file/reports/S5/rapport.pdf"
    """
    # Retirer le préfixe de la section du chemin distant
    if remote_path.startswith(section + "/"):
        rel_path = remote_path[len(section) + 1:]
    else:
        rel_path = remote_path

    # Construire les variantes de chemin local à tester
    candidates = []

    # Mapping des préfixes de section vers les répertoires locaux possibles
    if section == "cours-pdf":
        local_prefixes = [Path(".")]
    elif section == "file/reports":
        local_prefixes = [Path("reports"), Path("file/reports"), Path(".")]
    else:
        local_prefixes = [Path(section), Path(".")]

    for prefix in local_prefixes:
        # Variante 1: tel quel (avec underscores)
        candidates.append(local_base / prefix / rel_path)

        # Variante 2: underscores remplacés par des espaces dans le nom de fichier
        parts = Path(rel_path).parts
        space_parts = []
        for part in parts:
            space_parts.append(part.replace("_", " "))
        candidates.append(local_base / prefix / Path(*space_parts))

        # Variante 3: underscores -> espaces seulement dans le nom du fichier
        if len(parts) > 1:
            dir_parts = list(parts[:-1])
            filename = parts[-1].replace("_", " ")
            candidates.append(local_base / prefix / Path(*dir_parts, filename))

        # Variante 4: espaces dans les dossiers mais underscores dans le fichier
        if len(parts) > 1:
            dir_parts = [p.replace("_", " ") for p in parts[:-1]]
            filename = parts[-1]
            candidates.append(local_base / prefix / Path(*dir_parts, filename))

    # Tester chaque candidat
    for candidate in candidates:
        if candidate.is_file():
            return candidate

    return None


def fuzzy_find_local(remote_path: str, section: str, local_base: Path) -> Path | None:
    """
    Recherche floue: parcourt le dossier pour trouver un fichier
    dont le nom correspond (en ignorant espaces/underscores).
    """
    if remote_path.startswith(section + "/"):
        rel_path = remote_path[len(section) + 1:]
    else:
        rel_path = remote_path

    parts = Path(rel_path).parts
    if not parts:
        return None

    target_filename = parts[-1].replace("_", "").replace(" ", "").lower()

    # Déterminer dans quel sous-dossier chercher (ex: S1/Anglais)
    if section == "cours-pdf":
        search_root = local_base
    elif section == "file/reports":
        for d in [local_base / "reports", local_base / "file" / "reports", local_base]:
            if d.is_dir():
                search_root = d
                break
        else:
            search_root = local_base
    else:
        search_root = local_base

    # Si on a des sous-dossiers dans le chemin, essayer de naviguer
    if len(parts) > 1:
        sub_dirs = parts[:-1]
        # Essayer avec les noms exacts puis avec espaces/underscores
        for variation in [sub_dirs, tuple(p.replace("_", " ") for p in sub_dirs)]:
            candidate_dir = search_root
            for sd in variation:
                candidate_dir = candidate_dir / sd
            if candidate_dir.is_dir():
                # Chercher le fichier dans ce dossier
                for f in candidate_dir.iterdir():
                    if f.is_file() and f.suffix.lower() == ".pdf":
                        normalized = f.name.replace("_", "").replace(" ", "").lower()
                        if normalized == target_filename:
                            return f

    # Recherche récursive en dernier recours
    for f in search_root.rglob("*.pdf"):
        normalized = f.name.replace("_", "").replace(" ", "").lower()
        if normalized == target_filename:
            return f

    return None


def scp_upload(local_file: Path, remote_path: str) -> bool:
    """Upload un fichier via scp vers le serveur distant."""
    remote_full = f"{REMOTE_USER}@{REMOTE_HOST}:{REMOTE_PORTFOLIO}/{remote_path}"
    try:
        result = subprocess.run(
            ["scp", "-o", "StrictHostKeyChecking=no", str(local_file), remote_full],
            capture_output=True,
            text=True,
            timeout=120,
        )
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        return False


def verify_remote_file(remote_path: str, local_size: int) -> bool:
    """Vérifie que le fichier distant a bien la bonne taille après upload."""
    cmd = f"stat -c%s '{REMOTE_PORTFOLIO}/{remote_path}'"
    try:
        result = subprocess.run(
            ["ssh", f"{REMOTE_USER}@{REMOTE_HOST}", cmd],
            capture_output=True,
            text=True,
            timeout=30,
        )
        if result.returncode == 0:
            remote_size = int(result.stdout.strip())
            return remote_size == local_size
    except (subprocess.TimeoutExpired, ValueError):
        pass
    return False


def main():
    local_base = Path.cwd()

    # Vérifier que TRUNCATED_PDFS.txt est accessible
    truncated_file = local_base / TRUNCATED_FILE
    if not truncated_file.exists():
        # Essayer dans le dossier parent ou le télécharger du serveur
        print(f"{C.YELLOW}TRUNCATED_PDFS.txt non trouvé localement.{C.END}")
        print(f"Téléchargement depuis le serveur...")
        result = subprocess.run(
            ["scp", f"{REMOTE_USER}@{REMOTE_HOST}:{REMOTE_PORTFOLIO}/{TRUNCATED_FILE}", str(truncated_file)],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            print(f"{C.RED}Impossible de récupérer {TRUNCATED_FILE}{C.END}")
            sys.exit(1)
        print(f"{C.GREEN}Fichier récupéré.{C.END}\n")

    # Parser le fichier
    sections = parse_truncated_file(str(truncated_file))
    total_files = sum(len(files) for files in sections.values())
    print(f"{C.BOLD}{'='*60}{C.END}")
    print(f"{C.BOLD}  Remplacement des PDFs tronqués sur {REMOTE_HOST}{C.END}")
    print(f"{C.BOLD}  Répertoire local : {local_base}{C.END}")
    print(f"{C.BOLD}  Fichiers à traiter: {total_files}{C.END}")
    print(f"{C.BOLD}{'='*60}{C.END}\n")

    # Tester la connexion SSH
    print("Test de connexion SSH...", end=" ", flush=True)
    ssh_test = subprocess.run(
        ["ssh", "-o", "ConnectTimeout=5", f"{REMOTE_USER}@{REMOTE_HOST}", "echo ok"],
        capture_output=True,
        text=True,
    )
    if ssh_test.returncode != 0:
        print(f"{C.RED}ECHEC{C.END}")
        print(f"Impossible de se connecter à {REMOTE_USER}@{REMOTE_HOST}")
        print(f"Vérifie ta connexion SSH et tes clés.")
        sys.exit(1)
    print(f"{C.GREEN}OK{C.END}\n")

    stats = {"ok": 0, "missing": 0, "failed": 0, "skipped": 0}
    missing_files = []

    for section, files in sections.items():
        if not files:
            continue

        print(f"{C.CYAN}--- {section}/ ({len(files)} fichiers) ---{C.END}\n")

        for remote_path in files:
            # Chercher le fichier local
            local_file = find_local_file(remote_path, section, local_base)

            if local_file is None:
                local_file = fuzzy_find_local(remote_path, section, local_base)

            if local_file is None:
                print(f"  {C.RED}[ABSENT]{C.END} {remote_path}")
                print(f"           Fichier local introuvable")
                stats["missing"] += 1
                missing_files.append(remote_path)
                continue

            local_size = local_file.stat().st_size

            # Upload
            print(f"  Envoi: {local_file.name} ({local_size:,} bytes) -> {remote_path}")
            if scp_upload(local_file, remote_path):
                # Vérification
                if verify_remote_file(remote_path, local_size):
                    print(f"  {C.GREEN}[OK]{C.END}     Remplacé avec succès")
                    stats["ok"] += 1
                else:
                    print(f"  {C.YELLOW}[WARN]{C.END}   Uploadé mais taille non vérifiée")
                    stats["ok"] += 1
            else:
                print(f"  {C.RED}[FAIL]{C.END}   Echec de l'upload")
                stats["failed"] += 1

        print()

    # Résumé
    print(f"{C.BOLD}{'='*60}{C.END}")
    print(f"{C.BOLD}  Résumé{C.END}")
    print(f"{C.BOLD}{'='*60}{C.END}")
    print(f"  {C.GREEN}Remplacés : {stats['ok']}{C.END}")
    print(f"  {C.YELLOW}Skippés   : {stats['skipped']}{C.END}")
    print(f"  {C.RED}Absents   : {stats['missing']}{C.END}")
    print(f"  {C.RED}Echoués   : {stats['failed']}{C.END}")
    print()

    if missing_files:
        print(f"{C.YELLOW}Fichiers locaux introuvables:{C.END}")
        for f in missing_files:
            print(f"  - {f}")
        print()
        print(f"Vérifiez que vous lancez bien le script depuis le bon répertoire INSA")
        print(f"et que ces fichiers existent localement.\n")

    if stats["ok"] > 0:
        print(f"{C.GREEN}Relancez 'jekyll serve' sur le serveur pour vérifier.{C.END}")


if __name__ == "__main__":
    main()

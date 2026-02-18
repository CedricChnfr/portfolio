#!/bin/bash
# Script pour remplacer les PDFs tronqués par les originaux
#
# UTILISATION:
# 1. Depuis ton PC local, uploade le dossier cours-pdf complet vers le serveur:
#    scp -r cours-pdf/ user@<serveur>:/home/user/cedric/portfolio/uploaded_pdfs/
#    scp -r file/reports/ user@<serveur>:/home/user/cedric/portfolio/uploaded_reports/
#
# 2. Puis lance ce script sur le serveur:
#    bash fix_pdfs.sh
#

PORTFOLIO_DIR="/home/user/cedric/portfolio"
UPLOAD_DIR="$PORTFOLIO_DIR/uploaded_pdfs"
UPLOAD_REPORTS_DIR="$PORTFOLIO_DIR/uploaded_reports"

# Couleurs
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo "============================================"
echo "  Correction des PDFs tronqués"
echo "============================================"
echo ""

# Fonction pour vérifier si un PDF est tronqué (taille exacte en puissance de 2)
is_truncated() {
    local size=$(stat -c%s "$1" 2>/dev/null)
    case $size in
        262144|524288|786432|1048576|1310720) return 0 ;;
        *) return 1 ;;
    esac
}

# Fonction pour vérifier si un PDF est valide (se termine par %%EOF)
is_valid_pdf() {
    local tail_bytes=$(tail -c 20 "$1" 2>/dev/null)
    if echo "$tail_bytes" | grep -q "%%EOF"; then
        return 0
    else
        return 1
    fi
}

# Fonction pour renommer espaces en underscores
sanitize_name() {
    echo "$1" | sed 's/ /_/g'
}

replaced=0
skipped=0
missing=0
errors=0

# Traiter les PDFs de cours
if [ -d "$UPLOAD_DIR" ]; then
    echo "Traitement des PDFs de cours..."
    echo ""

    # Trouver tous les PDFs dans le dossier uploadé
    find "$UPLOAD_DIR" -name "*.pdf" -type f | while read -r src_file; do
        # Extraire le chemin relatif
        rel_path="${src_file#$UPLOAD_DIR/}"

        # Créer le nom avec underscores
        sanitized_path=$(echo "$rel_path" | sed 's/ /_/g')

        dest_file="$PORTFOLIO_DIR/cours-pdf/$sanitized_path"
        dest_dir=$(dirname "$dest_file")

        # Vérifier si le fichier source est valide
        if ! is_valid_pdf "$src_file"; then
            echo -e "  ${YELLOW}[SKIP]${NC} Source invalide: $rel_path"
            continue
        fi

        # Créer le répertoire destination si nécessaire
        mkdir -p "$dest_dir"

        # Copier le fichier
        cp "$src_file" "$dest_file"

        if is_valid_pdf "$dest_file"; then
            echo -e "  ${GREEN}[OK]${NC} $sanitized_path"
        else
            echo -e "  ${RED}[ERR]${NC} Copie échouée: $sanitized_path"
        fi
    done

    echo ""
    echo "PDFs de cours traités."
else
    echo -e "${YELLOW}Dossier uploaded_pdfs/ non trouvé.${NC}"
    echo "Uploade tes PDFs avec:"
    echo "  scp -r cours-pdf/ user@<serveur>:$PORTFOLIO_DIR/uploaded_pdfs/"
fi

echo ""

# Traiter les rapports
if [ -d "$UPLOAD_REPORTS_DIR" ]; then
    echo "Traitement des rapports..."
    echo ""

    find "$UPLOAD_REPORTS_DIR" -name "*.pdf" -type f | while read -r src_file; do
        rel_path="${src_file#$UPLOAD_REPORTS_DIR/}"
        sanitized_path=$(echo "$rel_path" | sed 's/ /_/g')
        dest_file="$PORTFOLIO_DIR/file/reports/$sanitized_path"
        dest_dir=$(dirname "$dest_file")

        if ! is_valid_pdf "$src_file"; then
            echo -e "  ${YELLOW}[SKIP]${NC} Source invalide: $rel_path"
            continue
        fi

        mkdir -p "$dest_dir"
        cp "$src_file" "$dest_file"

        if is_valid_pdf "$dest_file"; then
            echo -e "  ${GREEN}[OK]${NC} $sanitized_path"
        else
            echo -e "  ${RED}[ERR]${NC} Copie échouée: $sanitized_path"
        fi
    done

    echo ""
    echo "Rapports traités."
else
    echo -e "${YELLOW}Dossier uploaded_reports/ non trouvé.${NC}"
    echo "Uploade tes rapports avec:"
    echo "  scp -r file/reports/ user@<serveur>:$PORTFOLIO_DIR/uploaded_reports/"
fi

echo ""
echo "============================================"
echo "  Vérification finale"
echo "============================================"
echo ""

# Compter les fichiers encore tronqués
trunc_cours=$(find "$PORTFOLIO_DIR/cours-pdf" -name "*.pdf" \( -size 262144c -o -size 524288c -o -size 786432c -o -size 1048576c -o -size 1310720c \) | wc -l)
total_cours=$(find "$PORTFOLIO_DIR/cours-pdf" -name "*.pdf" | wc -l)
trunc_reports=$(find "$PORTFOLIO_DIR/file/reports" -name "*.pdf" \( -size 262144c -o -size 524288c -o -size 786432c -o -size 1048576c -o -size 1310720c \) | wc -l)
total_reports=$(find "$PORTFOLIO_DIR/file/reports" -name "*.pdf" | wc -l)

echo "Cours PDFs:   $trunc_cours/$total_cours encore tronqués"
echo "Rapports:     $trunc_reports/$total_reports encore tronqués"
echo ""

if [ "$trunc_cours" -eq 0 ] && [ "$trunc_reports" -eq 0 ]; then
    echo -e "${GREEN}Tous les PDFs sont OK !${NC}"
    echo ""
    echo "Prochaine étape: relancer 'jekyll serve' pour tester."
else
    echo -e "${YELLOW}Il reste des PDFs tronqués.${NC}"
    echo "Vérifie que tous les originaux ont bien été uploadés."
fi

echo ""
echo "Tu peux supprimer les dossiers temporaires après vérification:"
echo "  rm -rf $UPLOAD_DIR $UPLOAD_REPORTS_DIR"

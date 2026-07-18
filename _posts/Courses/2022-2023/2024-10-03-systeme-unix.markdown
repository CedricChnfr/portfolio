---
layout: default
title: "Système Unix - S5"
date: 2024-10-02 10:56:03 +0200
---

<style>
.back-nav {
  margin-bottom: 20px;
}
.back-nav a {
  text-decoration: none;
  color: #2a7ae2;
  font-weight: 600;
}
.back-nav a:hover {
  text-decoration: underline;
}
.section-title {
  color: #2a7ae2;
  border-bottom: 2px solid #2a7ae2;
  padding-bottom: 10px;
  margin-top: 30px;
  margin-bottom: 20px;
}
table {
    border-collapse: collapse;
    width: 100%;
    margin: 20px 0;
}
th, td {
    border: 1px solid #ddd;
    padding: 12px;
    text-align: left;
}
th {
    background-color: #2a7ae2;
    color: white;
}
tr:nth-child(even) {
    background-color: #f9f9f9;
}
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f9;
    color: #333;
    line-height: 1.6;
}
h2, h3, h4, h5 {
    color: #2a7ae2;
}
p {
    text-align: justify;
}
code {
    background-color: #f5f5f5;
    padding: 2px 6px;
    border-radius: 3px;
    font-family: 'Courier New', monospace;
}
pre {
    background-color: #f5f5f5;
    padding: 15px;
    border-radius: 5px;
    overflow-x: auto;
}
.pdf-container {
    margin: 40px 0;
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 8px;
}
.pdf-viewer {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    margin-top: 20px;
}
.pdf-item {
    flex: 1;
    min-width: 400px;
    background: white;
    padding: 15px;
    border-radius: 5px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
.pdf-item h4 {
    margin-top: 0;
    color: #2a7ae2;
    border-bottom: 2px solid #2a7ae2;
    padding-bottom: 10px;
}
</style>

<div class="back-nav">
  <a href="./my-courses-2022-2023.html" data-i18n-html="back-courses-2022-2023">&larr; Retour aux Cours 2022-2023</a>
</div>

<!-- ===================== FRENCH VERSION ===================== -->
<div class="lang-fr">

<h1>Systeme Unix - S5</h1>

<p><strong>Annee</strong> : 2022-2023 (Semestre 5)<br/>
<strong>Credits</strong> : 3 ECTS<br/>
<strong>Type</strong> : Systemes d'Exploitation</p>

<hr/>

<h2>PART A : PRESENTATION GENERALE</h2>

<h3 class="section-title">Objectifs du cours</h3>

<p>Ce cours introduit les systemes d'exploitation Unix/Linux en se concentrant sur l'utilisation pratique de la ligne de commande, la programmation shell, et l'administration systeme de base. L'accent est mis sur la maitrise des outils essentiels pour le developpement et l'exploitation de systemes embarques.</p>

<h3 class="section-title">Competences visees</h3>

<ul>
  <li>Maitriser la ligne de commande Unix/Linux</li>
  <li>Programmer des scripts shell pour l'automatisation</li>
  <li>Gerer les fichiers, processus et permissions</li>
  <li>Utiliser les outils de traitement de texte (grep, sed, awk)</li>
  <li>Comprendre l'architecture du systeme de fichiers</li>
  <li>Effectuer des taches d'administration systeme basiques</li>
  <li>Combiner les commandes avec pipes et redirections</li>
  <li>Resoudre des problemes pratiques avec les outils Unix</li>
</ul>

<h3 class="section-title">Organisation</h3>

<ul>
  <li><strong>Volume horaire</strong> : Cours, TD et videos pedagogiques</li>
  <li><strong>Evaluation</strong> : Examen ecrit + exercices pratiques</li>
  <li><strong>Semestre</strong> : 5 (2022-2023)</li>
  <li><strong>Prerequis</strong> : Notions d'informatique de base</li>
</ul>

<hr/>

<h2>PART B : EXPERIENCE, CONTEXTE ET FONCTION</h2>

<h3 class="section-title">Contenu pedagogique</h3>

<p>Le cours couvre les fondamentaux d'Unix a travers une approche pratique.</p>

<h4>1. Fondamentaux Unix</h4>

<p><strong>Philosophie Unix</strong> :</p>

<p>Principes de conception :</p>
<ul>
  <li>Tout est fichier (peripheriques, sockets, processus)</li>
  <li>Programmes simples faisant une seule chose bien</li>
  <li>Combinaison d'outils avec pipes</li>
  <li>Interfaces textuelles pour faciliter l'automatisation</li>
  <li>Systeme multi-utilisateurs et multi-taches</li>
</ul>

<p><strong>Architecture systeme</strong> :</p>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S5/unix/architecture-unix.svg" alt="Architecture Unix/Linux" style="max-width: 500px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Architecture en couches d'un systeme Unix/Linux</p>
</div>

<table>
  <tr><th>Composant</th><th>Fonction</th></tr>
  <tr><td>Noyau (kernel)</td><td>Gestion materielle, processus, memoire</td></tr>
  <tr><td>Shell</td><td>Interpreteur de commandes</td></tr>
  <tr><td>Programmes systeme</td><td>Utilitaires de base</td></tr>
  <tr><td>Applications</td><td>Logiciels utilisateur</td></tr>
</table>

<p><strong>Shells disponibles</strong> :</p>
<ul>
  <li><strong>bash</strong> (Bourne Again Shell) : le plus repandu</li>
  <li>sh (Bourne Shell) : shell historique</li>
  <li>zsh (Z Shell) : shell avance avec auto-completion</li>
  <li>csh/tcsh (C Shell) : syntaxe proche du C</li>
</ul>

<h4>2. Systeme de fichiers</h4>

<p><strong>Arborescence standard</strong> :</p>

<p>Structure hierarchique partant de la racine (/).</p>

<table>
  <tr><th>Repertoire</th><th>Contenu</th></tr>
  <tr><td>/bin</td><td>Commandes essentielles (ls, cp, mv)</td></tr>
  <tr><td>/etc</td><td>Fichiers de configuration</td></tr>
  <tr><td>/home</td><td>Repertoires personnels des utilisateurs</td></tr>
  <tr><td>/usr</td><td>Applications et utilitaires</td></tr>
  <tr><td>/var</td><td>Donnees variables (logs, caches)</td></tr>
  <tr><td>/tmp</td><td>Fichiers temporaires</td></tr>
  <tr><td>/dev</td><td>Fichiers de peripheriques</td></tr>
  <tr><td>/proc</td><td>Informations du systeme et processus</td></tr>
</table>

<p><strong>Types de fichiers</strong> :</p>
<ul>
  <li><strong>Fichier regulier</strong> (-) : fichier normal</li>
  <li><strong>Repertoire</strong> (d) : dossier</li>
  <li><strong>Lien symbolique</strong> (l) : raccourci vers un autre fichier</li>
  <li><strong>Peripherique bloc</strong> (b) : disque dur, USB</li>
  <li><strong>Peripherique caractere</strong> (c) : terminal, imprimante</li>
  <li><strong>Socket</strong> (s) : communication inter-processus</li>
  <li><strong>Pipe nomme</strong> (p) : canal de communication</li>
</ul>

<p><strong>Commandes de navigation</strong> :</p>

<pre><code class="language-bash">pwd                    # Afficher repertoire courant
cd /chemin/vers/dir    # Changer de repertoire
cd ..                  # Remonter d'un niveau
cd ~                   # Aller au home
cd -                   # Revenir au repertoire precedent
ls                     # Lister fichiers
ls -l                  # Liste detaillee
ls -a                  # Afficher fichiers caches
ls -lh                 # Tailles lisibles (KB, MB)</code></pre>

<p><strong>Manipulation de fichiers</strong> :</p>

<pre><code class="language-bash"># Creation
touch fichier.txt      # Creer fichier vide
mkdir dossier          # Creer repertoire
mkdir -p a/b/c         # Creer arborescence

# Copie et deplacement
cp source dest         # Copier fichier
cp -r dir1 dir2        # Copier repertoire recursivement
mv ancien nouveau      # Renommer/deplacer

# Suppression
rm fichier             # Supprimer fichier
rm -r dossier          # Supprimer repertoire recursivement
rm -f fichier          # Forcer suppression
rmdir dossier          # Supprimer repertoire vide</code></pre>

<p><strong>Visualisation de fichiers</strong> :</p>

<pre><code class="language-bash">cat fichier            # Afficher contenu complet
more fichier           # Afficher page par page
less fichier           # Naviguer dans le fichier
head fichier           # Afficher premieres lignes
head -n 20 fichier     # Afficher 20 premieres lignes
tail fichier           # Afficher dernieres lignes
tail -f fichier        # Suivre ajouts en temps reel (logs)</code></pre>

<h4>3. Permissions et droits d'acces</h4>

<p><strong>Systeme de permissions</strong> :</p>

<p>Format : <code>drwxrwxrwx</code></p>
<ul>
  <li>Premier caractere : type de fichier</li>
  <li>3 caracteres suivants : droits du proprietaire (user)</li>
  <li>3 suivants : droits du groupe (group)</li>
  <li>3 derniers : droits des autres (others)</li>
</ul>

<p><strong>Types de permissions</strong> :</p>

<table>
  <tr><th>Permission</th><th>Fichier</th><th>Repertoire</th></tr>
  <tr><td>r (read)</td><td>Lire le contenu</td><td>Lister le contenu</td></tr>
  <tr><td>w (write)</td><td>Modifier le fichier</td><td>Creer/supprimer fichiers</td></tr>
  <tr><td>x (execute)</td><td>Executer le fichier</td><td>Acceder au repertoire</td></tr>
</table>

<p><strong>Representation numerique</strong> :</p>

<p>Chaque permission a une valeur :</p>
<ul>
  <li>r = 4</li>
  <li>w = 2</li>
  <li>x = 1</li>
</ul>

<p>Exemples :</p>
<ul>
  <li>755 = rwxr-xr-x (proprietaire : tout, autres : lecture+execution)</li>
  <li>644 = rw-r--r-- (proprietaire : lecture+ecriture, autres : lecture seule)</li>
  <li>700 = rwx------ (proprietaire seul a tous les droits)</li>
  <li>777 = rwxrwxrwx (tous les droits pour tout le monde)</li>
</ul>

<p><strong>Commandes de gestion</strong> :</p>

<pre><code class="language-bash"># Modifier permissions
chmod 755 fichier              # Mode numerique
chmod u+x fichier              # Ajouter execution pour user
chmod g-w fichier              # Retirer ecriture pour group
chmod o+r fichier              # Ajouter lecture pour others
chmod a+x fichier              # Ajouter execution pour all

# Modifier proprietaire
chown utilisateur fichier      # Changer proprietaire
chown user:group fichier       # Changer user et group
chgrp groupe fichier           # Changer groupe uniquement</code></pre>

<p><strong>Permissions speciales</strong> :</p>

<p><strong>SUID (Set User ID)</strong> : 4xxx ou u+s</p>
<ul>
  <li>Le fichier s'execute avec les droits du proprietaire</li>
  <li>Exemple : /usr/bin/passwd (permet aux users de changer leur mot de passe)</li>
</ul>

<p><strong>SGID (Set Group ID)</strong> : 2xxx ou g+s</p>
<ul>
  <li>Le fichier s'execute avec les droits du groupe</li>
  <li>Sur un repertoire : fichiers crees heritent du groupe</li>
</ul>

<p><strong>Sticky bit</strong> : 1xxx ou +t</p>
<ul>
  <li>Sur repertoire : seul le proprietaire peut supprimer ses fichiers</li>
  <li>Exemple : /tmp (repertoire partage mais fichiers proteges)</li>
</ul>

<p>Exemple de l'examen :</p>
<pre><code class="language-bash">chmod 1777 /tmp/test3    # Sticky bit + tous droits
chmod 750 /tmp/test1     # rwxr-x---
chmod 640 fichier        # rw-r-----</code></pre>

<h4>4. Gestion des processus</h4>

<p><strong>Concept de processus</strong> :</p>

<p>Un processus est un programme en cours d'execution.</p>

<p>Attributs principaux :</p>
<ul>
  <li><strong>PID</strong> (Process ID) : identifiant unique</li>
  <li><strong>PPID</strong> (Parent Process ID) : processus parent</li>
  <li><strong>UID</strong> : utilisateur proprietaire</li>
  <li>Etat : running, sleeping, stopped, zombie</li>
  <li>Priorite : nice value</li>
</ul>

<p><strong>Commandes de gestion</strong> :</p>

<pre><code class="language-bash"># Afficher processus
ps                    # Processus de l'utilisateur courant
ps aux                # Tous les processus detailles
ps -ef                # Format long
top                   # Monitoring en temps reel
htop                  # Version amelioree de top

# Controle des processus
kill PID              # Envoyer signal TERM (terminaison propre)
kill -9 PID           # Signal KILL (terminaison forcee)
killall nom           # Tuer par nom de programme
pkill motif           # Tuer selon motif

# Arriere-plan
commande &amp;            # Lancer en arriere-plan
jobs                  # Lister jobs
fg %1                 # Ramener job 1 au premier plan
bg %1                 # Continuer job 1 en arriere-plan
Ctrl+Z                # Suspendre processus courant</code></pre>

<p><strong>Analyse de l'exemple de l'examen</strong> :</p>

<p>Commande : <code>ps -ef | awk '{print $3}' | sort | uniq -c | awk '{print $2,$1}' | grep -v PPID</code></p>

<p>Decomposition :</p>
<ol>
  <li><code>ps -ef</code> : liste tous les processus</li>
  <li><code>awk '{print $3}'</code> : extrait colonne PPID (parent)</li>
  <li><code>sort</code> : trie les PPID</li>
  <li><code>uniq -c</code> : compte occurrences de chaque PPID</li>
  <li><code>awk '{print $2,$1}'</code> : inverse colonnes (PPID puis count)</li>
  <li><code>grep -v PPID</code> : exclut l'en-tete</li>
</ol>

<p>Resultat : liste des processus avec leur nombre d'enfants.</p>

<h4>5. Programmation Shell (Bash)</h4>

<p><strong>Structure de base d'un script</strong> :</p>

<pre><code class="language-bash">#!/bin/bash
# Shebang : indique l'interpreteur a utiliser

# Ceci est un commentaire

echo "Premier script shell"</code></pre>

<p>Execution :</p>
<pre><code class="language-bash">chmod +x script.sh     # Rendre executable
./script.sh            # Executer</code></pre>

<p><strong>Variables</strong> :</p>

<pre><code class="language-bash"># Declaration (pas d'espace autour du =)
nom="Cedric"
age=25
i=3

# Utilisation
echo "Je m'appelle $nom"
echo "J'ai ${age} ans"

# Variables d'environnement
echo $HOME             # Repertoire personnel
echo $PATH             # Chemins de recherche des commandes
echo $USER             # Nom utilisateur</code></pre>

<p><strong>Lecture d'entree</strong> :</p>

<pre><code class="language-bash">echo "Entrez un nombre:"
read nombre
echo "Vous avez saisi: $nombre"

# Lecture dans variable specifique
read -p "Nom: " nom</code></pre>

<p><strong>Structures conditionnelles</strong> :</p>

<pre><code class="language-bash"># if-then-else
if test $i -eq 3
then
  echo "i vaut 3"
else
  echo "i ne vaut pas 3"
fi

# Forme alternative avec crochets
if [ $i -eq 3 ]
then
  echo "i vaut 3"
fi

# Operateurs de comparaison numerique
# -eq (egal), -ne (different), -lt (inferieur)
# -le (inferieur ou egal), -gt (superieur), -ge (superieur ou egal)

# Comparaisons de chaines
if [ "$str1" = "$str2" ]
then
  echo "Chaines identiques"
fi

# Tests de fichiers
if [ -f fichier ]      # Fichier existe
if [ -d dossier ]      # Repertoire existe
if [ -r fichier ]      # Fichier lisible
if [ -w fichier ]      # Fichier modifiable
if [ -x fichier ]      # Fichier executable

# Case
case $var in
  1) echo "Un" ;;
  2) echo "Deux" ;;
  *) echo "Autre" ;;
esac</code></pre>

<p><strong>Boucles</strong> :</p>

<pre><code class="language-bash"># Boucle for avec sequence
for i in $(seq 1 100)
do
  echo $i
done

# Boucle for sur fichiers
for fichier in *.txt
do
  echo "Traitement de $fichier"
done

# Boucle for sur resultat de commande
for fichier in $(ls *)
do
  echo $fichier
done

# Boucle while
compteur=1
while [ $compteur -le 10 ]
do
  echo $compteur
  compteur=$((compteur + 1))
done

# Boucle while avec lecture de fichier
while read ligne
do
  echo "Ligne: $ligne"
done &lt; fichier.txt

# Until (inverse de while)
until [ $compteur -gt 10 ]
do
  echo $compteur
  compteur=$((compteur + 1))
done</code></pre>

<p><strong>Tableaux</strong> :</p>

<pre><code class="language-bash"># Declaration
tab[0]="premier"
tab[1]="deuxieme"

# Ou
declare -a tab
tab=("un" "deux" "trois")

# Remplissage en boucle
n=4
for i in $(seq 1 $n)
do
  tab[$i]="element$i"
done

# Acces
echo ${tab[0]}         # Premier element
echo ${tab[*]}         # Tous les elements
echo ${#tab[*]}        # Nombre d'elements</code></pre>

<p><strong>Fonctions</strong> :</p>

<pre><code class="language-bash"># Definition
ma_fonction() {
  echo "Bonjour $1"    # $1 = premier argument
  return 0             # Code de retour
}

# Appel
ma_fonction "Cedric"</code></pre>

<p><strong>Erreurs courantes a eviter</strong> :</p>

<p>D'apres l'examen :</p>
<ol>
  <li>Oublier le <code>!</code> dans le shebang : <code>#!/bin/bash</code></li>
  <li>Espaces autour du <code>=</code> : utiliser <code>i=3</code> pas <code>i = 3</code></li>
  <li>Mauvaise syntaxe de boucle : <code>for i in $(seq 1 100)</code> pas <code>for i in 1..100</code></li>
  <li>Mauvais test : <code>if [ $i -eq 3 ]</code> pas <code>if test $i == 3 then</code></li>
  <li>Fermer avec <code>fi</code> pas <code>end</code></li>
  <li>Utiliser <code>$i</code> pour lire la variable, pas <code>$REPLY</code></li>
  <li>Acces tableau : <code>${tab[*]}</code> pas <code>${tab}</code></li>
  <li>Substitution de commande : <code>$(commande)</code> ou <code>`commande`</code></li>
</ol>

<h4>6. Traitement de texte</h4>

<p><strong>grep (recherche de motifs)</strong> :</p>

<pre><code class="language-bash">grep "motif" fichier              # Rechercher motif
grep -i "motif" fichier           # Insensible a la casse
grep -v "motif" fichier           # Inverser (lignes sans motif)
grep -r "motif" repertoire/       # Recursif dans repertoire
grep -n "motif" fichier           # Afficher numeros de lignes
grep -c "motif" fichier           # Compter occurrences
grep -E "regex" fichier           # Expressions regulieres etendues</code></pre>

<p><strong>sed (editeur de flux)</strong> :</p>

<pre><code class="language-bash"># Substitution
sed 's/ancien/nouveau/' fichier         # Premiere occurrence par ligne
sed 's/ancien/nouveau/g' fichier        # Toutes occurrences
sed -i 's/ancien/nouveau/g' fichier     # Modifier fichier en place

# Suppression
sed '/motif/d' fichier                  # Supprimer lignes contenant motif
sed '1d' fichier                        # Supprimer premiere ligne
sed '1,5d' fichier                      # Supprimer lignes 1 a 5</code></pre>

<p><strong>awk (langage de traitement)</strong> :</p>

<pre><code class="language-bash"># Afficher colonnes
awk '{print $1}' fichier               # Premiere colonne
awk '{print $1, $3}' fichier           # Colonnes 1 et 3
awk '{print $NF}' fichier              # Derniere colonne

# Avec conditions
awk '$3 &gt; 100 {print $1}' fichier      # Si colonne 3 &gt; 100

# Exemple de l'examen
ps -ef | awk '{print $3}'              # Extraire PPID
echo "$ligne" | awk '{print $1}'       # Extraire premier champ</code></pre>

<p><strong>Autres outils</strong> :</p>

<pre><code class="language-bash">sort fichier                 # Trier lignes
sort -n fichier              # Tri numerique
sort -r fichier              # Tri inverse
uniq fichier                 # Supprimer doublons consecutifs
uniq -c fichier              # Compter occurrences
wc fichier                   # Compter lignes, mots, caracteres
wc -l fichier                # Compter lignes seulement
cut -d':' -f1 fichier        # Extraire premier champ (delimiteur :)</code></pre>

<h4>7. Redirections et pipes</h4>

<p><strong>Flux standard</strong> :</p>
<ul>
  <li><strong>stdin</strong> (0) : entree standard (clavier)</li>
  <li><strong>stdout</strong> (1) : sortie standard (ecran)</li>
  <li><strong>stderr</strong> (2) : sortie d'erreur (ecran)</li>
</ul>

<p><strong>Redirections</strong> :</p>

<pre><code class="language-bash"># Redirection de sortie
commande &gt; fichier           # Ecraser fichier
commande &gt;&gt; fichier          # Ajouter a fichier
commande 2&gt; erreurs.txt      # Rediriger erreurs
commande 2&gt;&amp;1                # Erreurs vers sortie standard
commande &amp;&gt; fichier          # Sortie et erreurs vers fichier

# Redirection d'entree
commande &lt; fichier           # Lire depuis fichier
while read ligne
do
  echo $ligne
done &lt; fichier.txt

# Pipe (sortie d'une commande = entree de la suivante)
commande1 | commande2
ps aux | grep firefox
cat fichier | sort | uniq</code></pre>

<p><strong>Exemple complexe de l'examen</strong> :</p>

<pre><code class="language-bash">ps -ef | awk '{print $3}' | sort | uniq -c | awk '{print $2,$1}' | grep -v PPID &gt; /tmp/f</code></pre>

<p>Chaine de traitement avec 5 pipes combinant plusieurs outils.</p>

<h4>8. Administration systeme de base</h4>

<p><strong>Informations systeme</strong> :</p>

<pre><code class="language-bash">uname -a                # Info complete systeme
hostname                # Nom de la machine
whoami                  # Utilisateur courant
who                     # Utilisateurs connectes
w                       # Utilisateurs et activite
uptime                  # Temps de fonctionnement et charge
date                    # Date et heure</code></pre>

<p><strong>Gestion des disques</strong> :</p>

<pre><code class="language-bash">df -h                   # Espace disque (human-readable)
du -sh dossier          # Taille d'un repertoire
du -sh *                # Taille de tous elements</code></pre>

<p><strong>Gestion des utilisateurs</strong> :</p>

<pre><code class="language-bash">passwd                  # Changer son mot de passe
sudo commande           # Executer avec droits root
su                      # Devenir root
su - utilisateur        # Changer d'utilisateur</code></pre>

<p><strong>Recherche de fichiers</strong> :</p>

<pre><code class="language-bash">find /chemin -name "*.txt"           # Par nom
find /chemin -type f                 # Fichiers reguliers
find /chemin -type d                 # Repertoires
find /chemin -mtime -7               # Modifies depuis 7 jours
find /chemin -size +100M             # Taille &gt; 100 Mo
locate fichier                       # Recherche rapide (base de donnees)
which commande                       # Localiser executable</code></pre>

<p><strong>Archivage et compression</strong> :</p>

<pre><code class="language-bash"># tar (tape archive)
tar -cvf archive.tar fichiers/      # Creer archive
tar -xvf archive.tar                # Extraire archive
tar -tvf archive.tar                # Lister contenu

# Avec compression
tar -czvf archive.tar.gz fichiers/  # Creer + gzip
tar -xzvf archive.tar.gz            # Extraire gzip
tar -cjvf archive.tar.bz2 fichiers/ # Creer + bzip2

# zip/unzip
zip -r archive.zip dossier/
unzip archive.zip</code></pre>

<p><strong>Liens</strong> :</p>

<pre><code class="language-bash"># Lien symbolique (raccourci)
ln -s /chemin/cible lien            # Creer lien symbolique

# Lien dur (meme inode)
ln fichier_original lien_dur        # Creer lien dur</code></pre>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S5/unix/reseau-config1.png" alt="Configuration reseau Unix" style="max-width: 600px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Exemple de configuration reseau sous Unix/Linux - TP pratique</p>
</div>

<hr/>

<h2>PART C : ASPECTS TECHNIQUES</h2>

<h3 class="section-title">Exercices pratiques des examens</h3>

<p><strong>Exercice 1 : Creation d'arborescence avec permissions</strong></p>

<p>Objectif : reproduire exactement une structure de fichiers avec les bonnes permissions.</p>

<pre><code class="language-bash"># Creation de l'arborescence
mkdir -p /tmp/test/test1 /tmp/test/test2 /tmp/test/test3

# Creation des fichiers
touch /tmp/test/test1/f1
touch /tmp/test/test2/f2
touch /tmp/test/test3/f3

# Attribution des permissions aux repertoires
chmod 750 /tmp/test/test1    # rwxr-x---
chmod 754 /tmp/test/test2    # rwxr-xr--
chmod 1777 /tmp/test/test3   # rwxrwxrwt (avec sticky bit)

# Attribution des permissions aux fichiers
chmod 640 /tmp/test/test1/f1 # rw-r-----
chmod 444 /tmp/test/test2/f2 # r--r--r--
chmod 700 /tmp/test/test3/f3 # rwx------</code></pre>

<p><strong>Explications permissions speciales</strong> :</p>

<p><code>chmod 1777</code> : le <code>1</code> devant correspond au sticky bit.</p>
<ul>
  <li>Permet a chacun de creer des fichiers dans le repertoire</li>
  <li>Mais seul le proprietaire peut supprimer ses propres fichiers</li>
  <li>Typique pour /tmp</li>
</ul>

<p><strong>Exercice 2 : Correction de script shell</strong></p>

<p>Script avec erreurs :</p>
<pre><code class="language-bash">#/bin/bash                          # ERREUR: manque !

for i in 1..100                     # ERREUR: syntaxe incorrecte
do
 echo $i
done

for i in ls *                       # ERREUR: manque $()
do
  echo $i
done

i = 3                               # ERREUR: espaces autour de =

if test $i == 3 then                # ERREUR: -eq au lieu de ==, then mal place
  echo yes
else
  echo no
end                                 # ERREUR: doit etre fi

echo "un entier stp"
read i
echo entier saisi : $REPLY          # ERREUR: doit etre $i

n=4
for i in `seq 1 $n`
do
  tab[i]="toto"
done
echo ${tab}                         # ERREUR: doit etre ${tab[*]}</code></pre>

<p>Version corrigee :</p>
<pre><code class="language-bash">#!/bin/bash

for i in $(seq 1 100)
do
 echo $i
done

for i in $(ls *)
# ou plus simple: for i in *
do
  echo $i
done

i=3

if [ $i -eq 3 ]
then
  echo yes
else
  echo no
fi

echo "un entier stp"
read i
echo entier saisi : $i

n=4
for i in $(seq 1 $n)
do
  tab[$i]="toto"
done
echo ${tab[*]}</code></pre>

<p><strong>Exercice 3 : Analyse de pipeline complexe</strong></p>

<p>Script d'analyse des processus parents :</p>

<pre><code class="language-bash">#!/bin/bash

# Pipeline complexe
ps -ef | awk '{print $3}' | sort | uniq -c | awk '{print $2,$1}' | grep -v PPID &gt; /tmp/f

# Boucle de traitement
while read v
do
  a=$(echo $v | awk '{print $1}')   # PID
  b=$(echo $v | awk '{print $2}')   # Nombre d'enfants
  echo le processus $a a $b enfants
done &lt; /tmp/f</code></pre>

<p><strong>Explication detaillee du pipeline</strong> :</p>
<ol>
  <li><code>ps -ef</code> : affiche tous les processus avec PID, PPID, etc.</li>
  <li><code>awk '{print $3}'</code> : extrait la 3e colonne (PPID)</li>
  <li><code>sort</code> : trie les PPID numeriquement</li>
  <li><code>uniq -c</code> : compte les occurrences de chaque PPID unique</li>
  <li><code>awk '{print $2,$1}'</code> : inverse l'ordre (PPID puis compteur)</li>
  <li><code>grep -v PPID</code> : exclut la ligne d'en-tete</li>
  <li><code>&gt; /tmp/f</code> : sauvegarde dans fichier temporaire</li>
</ol>

<p>Resultat dans /tmp/f : chaque ligne contient un PID et le nombre de fois qu'il apparait comme parent (nombre d'enfants).</p>

<p><strong>La boucle while</strong> :</p>

<p>Lit chaque ligne du fichier /tmp/f et extrait :</p>
<ul>
  <li>Variable <code>a</code> : le PID du processus</li>
  <li>Variable <code>b</code> : le nombre d'enfants de ce processus</li>
</ul>

<p>Affiche : "le processus XXX a YYY enfants"</p>

<p><strong>Exercice 4 : Permissions et securite</strong></p>

<p>Analyse des permissions d'un jeu :</p>

<pre><code class="language-bash">drwxr-xr-x 2 etudiant etudiants 4096 jeu/
-r-sr-xr-x 1 etudiant etudiants 133792 le_binaire_du_jeu
-rw------- 1 etudiant etudiants 39 le_fichier_des_scores</code></pre>

<p><strong>Analyse</strong> :</p>

<p><strong>Le binaire (r-sr-xr-x)</strong> :</p>
<ul>
  <li>Bit SUID active (s a la place de x pour user)</li>
  <li>Tous peuvent l'executer (r-x pour group et others)</li>
  <li>Le jeu s'execute avec les droits de <code>etudiant</code></li>
  <li>Permet d'acceder au fichier des scores</li>
</ul>

<p><strong>Le fichier des scores (rw-------)</strong> :</p>
<ul>
  <li>Accessible en lecture/ecriture uniquement par <code>etudiant</code></li>
  <li>Autres utilisateurs ne peuvent ni lire ni ecrire</li>
  <li>Protection des scores contre la triche</li>
</ul>

<p><strong>Logique</strong> :</p>
<ul>
  <li>Les joueurs executent le binaire avec SUID</li>
  <li>Le programme s'execute comme <code>etudiant</code></li>
  <li>Il peut donc modifier le fichier des scores</li>
  <li>Mais les joueurs ne peuvent pas modifier directement les scores</li>
  <li>Empeche la triche tout en permettant le jeu</li>
</ul>

<h3 class="section-title">Commandes essentielles a maitriser</h3>

<p><strong>Navigation et fichiers</strong> :</p>
<pre><code class="language-bash">pwd, cd, ls, mkdir, rmdir, touch, cp, mv, rm, cat, more, less, head, tail</code></pre>

<p><strong>Permissions</strong> :</p>
<pre><code class="language-bash">chmod, chown, chgrp, umask</code></pre>

<p><strong>Processus</strong> :</p>
<pre><code class="language-bash">ps, top, kill, killall, bg, fg, jobs</code></pre>

<p><strong>Recherche</strong> :</p>
<pre><code class="language-bash">find, locate, which, whereis, grep</code></pre>

<p><strong>Traitement texte</strong> :</p>
<pre><code class="language-bash">grep, sed, awk, sort, uniq, wc, cut, tr</code></pre>

<p><strong>Systeme</strong> :</p>
<pre><code class="language-bash">uname, hostname, whoami, who, w, df, du, free, date</code></pre>

<p><strong>Archivage</strong> :</p>
<pre><code class="language-bash">tar, gzip, gunzip, zip, unzip</code></pre>

<hr/>

<h2>PART D : ANALYSE ET REFLEXION</h2>

<h3 class="section-title">Competences acquises</h3>

<p><strong>Ligne de commande</strong> :</p>
<ul>
  <li>Maitrise des commandes essentielles Unix</li>
  <li>Navigation efficace dans le systeme de fichiers</li>
  <li>Gestion des fichiers et repertoires</li>
  <li>Utilisation de la documentation (man)</li>
</ul>

<p><strong>Scripting</strong> :</p>
<ul>
  <li>Automatisation de taches repetitives</li>
  <li>Programmation shell avec bash</li>
  <li>Structures de controle (boucles, conditions)</li>
  <li>Manipulation de variables et tableaux</li>
  <li>Traitement de fichiers texte</li>
</ul>

<p><strong>Administration systeme</strong> :</p>
<ul>
  <li>Gestion des permissions et securite</li>
  <li>Gestion des processus</li>
  <li>Surveillance du systeme</li>
  <li>Archivage et sauvegarde</li>
</ul>

<p><strong>Outils avances</strong> :</p>
<ul>
  <li>Pipes et redirections pour combiner commandes</li>
  <li>Expressions regulieres pour recherche</li>
  <li>Traitement de flux avec awk et sed</li>
  <li>Analyse de logs et fichiers</li>
</ul>

<h3 class="section-title">Applications pratiques</h3>

<p>Unix/Linux est omnipresent dans l'informatique moderne :</p>

<p><strong>Developpement logiciel</strong> :</p>
<ul>
  <li>Environnement de developpement</li>
  <li>Compilation et build</li>
  <li>Gestion de versions (Git)</li>
  <li>Tests automatises</li>
</ul>

<p><strong>Systemes embarques</strong> :</p>
<ul>
  <li>Linux embarque sur Raspberry Pi, BeagleBone</li>
  <li>Systemes IoT</li>
  <li>Routeurs et equipements reseau</li>
  <li>Android (base sur Linux)</li>
</ul>

<p><strong>Serveurs et Cloud</strong> :</p>
<ul>
  <li>Serveurs web (Apache, Nginx)</li>
  <li>Bases de donnees (MySQL, PostgreSQL)</li>
  <li>Services cloud (AWS, Azure, GCP)</li>
  <li>Conteneurs (Docker, Kubernetes)</li>
</ul>

<p><strong>Administration systeme</strong> :</p>
<ul>
  <li>Gestion de serveurs</li>
  <li>Automatisation (scripts, cron)</li>
  <li>Monitoring et logs</li>
  <li>Sauvegardes</li>
</ul>

<p><strong>DevOps</strong> :</p>
<ul>
  <li>Deploiement continu (CI/CD)</li>
  <li>Automatisation d'infrastructure</li>
  <li>Configuration management (Ansible, Puppet)</li>
  <li>Orchestration de conteneurs</li>
</ul>

<h3 class="section-title">Liens avec autres cours</h3>

<table>
  <tr><th>Cours</th><th>Lien</th></tr>
  <tr><td>Langage C (S5)</td><td>Programmation systeme, appels systeme</td></tr>
  <tr><td>Systemes d'exploitation (S5)</td><td>Concepts de processus, memoire</td></tr>
  <tr><td>Reseau (S5)</td><td>Commandes reseau, sockets</td></tr>
  <tr><td>Architecture Materielle (S5)</td><td>Gestion peripheriques, drivers</td></tr>
  <tr><td>Temps Reel (S8)</td><td>Linux temps reel, ordonnancement</td></tr>
  <tr><td>Cloud Computing (S9)</td><td>Serveurs Linux, administration</td></tr>
</table>

<h3 class="section-title">Methodologie de travail</h3>

<p><strong>Apprentissage par la pratique</strong> :</p>

<p>La meilleure facon d'apprendre Unix est de pratiquer quotidiennement :</p>
<ul>
  <li>Utiliser le terminal au lieu de l'interface graphique</li>
  <li>Ecrire des scripts pour automatiser ses taches</li>
  <li>Lire le man des commandes</li>
  <li>Experimenter dans une VM pour eviter les erreurs</li>
</ul>

<p><strong>Ressources utiles</strong> :</p>
<ul>
  <li><code>man commande</code> : documentation integree</li>
  <li><code>commande --help</code> : aide rapide</li>
  <li><code>/usr/share/doc</code> : documentation detaillee</li>
  <li>StackOverflow et forums Linux</li>
  <li>Livres : "The Linux Command Line", "Unix and Linux System Administration Handbook"</li>
</ul>

<p><strong>Bonnes pratiques</strong> :</p>

<p>Scripts :</p>
<ul>
  <li>Toujours inclure le shebang</li>
  <li>Commenter son code</li>
  <li>Gerer les erreurs</li>
  <li>Tester avant deploiement</li>
</ul>

<p>Securite :</p>
<ul>
  <li>Principe du moindre privilege</li>
  <li>Eviter d'executer en root</li>
  <li>Verifier les permissions</li>
  <li>Sauvegarder avant modifications importantes</li>
</ul>

<h3 class="section-title">Mon opinion</h3>

<p>Ce cours est fondamental pour tout ingenieur informatique ou electronique.</p>

<p><strong>Points forts</strong> :</p>
<ul>
  <li>Competences immediatement applicables</li>
  <li>Universalite (Unix/Linux partout)</li>
  <li>Efficacite de la ligne de commande</li>
  <li>Automatisation puissante avec scripts</li>
</ul>

<p><strong>Importance professionnelle</strong> :</p>

<p>Unix/Linux est incontournable pour :</p>
<ul>
  <li>Developpement sur systemes embarques</li>
  <li>Administration de serveurs</li>
  <li>DevOps et Cloud</li>
  <li>IoT et objets connectes</li>
  <li>Intelligence artificielle (environnements de calcul)</li>
</ul>

<p><strong>Productivite</strong> :</p>

<p>Maitriser la ligne de commande permet :</p>
<ul>
  <li>Automatiser taches repetitives (gain de temps)</li>
  <li>Traiter volumes importants de donnees</li>
  <li>Travailler sur systemes distants (SSH)</li>
  <li>Scripter solutions sur mesure</li>
  <li>Diagnostiquer problemes efficacement</li>
</ul>

<p><strong>Complementarite avec autres competences</strong> :</p>

<p>Unix s'integre parfaitement avec :</p>
<ul>
  <li>Programmation C/C++ (compilation, debugging)</li>
  <li>Developpement web (serveurs, deploiement)</li>
  <li>Data science (traitement de donnees)</li>
  <li>Cybersecurite (analyse de logs, forensics)</li>
</ul>

<h3 class="section-title">Perspectives d'evolution</h3>

<p><strong>Technologies emergentes</strong> :</p>

<p><strong>Conteneurs</strong> : Docker et Kubernetes utilisent intensivement Unix.</p>
<p><strong>Edge Computing</strong> : Linux sur dispositifs embarques.</p>
<p><strong>Automatisation</strong> : Infrastructure as Code (Terraform, Ansible).</p>
<p><strong>Cloud natif</strong> : Microservices sur Linux.</p>

<h3 class="section-title">Conseils pratiques</h3>

<p><strong>Pour progresser</strong> :</p>
<ol>
  <li>Utiliser Linux comme systeme principal (dual-boot ou VM)</li>
  <li>Personnaliser son environnement (bashrc, aliases)</li>
  <li>Contribuer a des projets open-source</li>
  <li>Installer un serveur personnel (web, NAS)</li>
  <li>Automatiser ses taches quotidiennes avec scripts</li>
</ol>

<p><strong>Erreurs a eviter</strong> :</p>
<ul>
  <li>Ne jamais executer <code>rm -rf /</code> meme par curiosite</li>
  <li>Toujours verifier avant <code>rm -rf</code></li>
  <li>Sauvegarder avant modifications systeme</li>
  <li>Tester scripts dans un environnement de test</li>
  <li>Lire la documentation avant utilisation</li>
</ul>

<hr/>

<p><strong>Bilan personnel</strong> : Ce cours a fourni les bases essentielles pour travailler efficacement en environnement Unix/Linux. La maitrise de la ligne de commande et des scripts shell est une competence transversale precieuse pour toute carriere en informatique ou electronique. Ces connaissances sont quotidiennement utiles, que ce soit pour le developpement, l'administration systeme, ou le deploiement d'applications. La philosophie Unix (outils simples et combinables) reste d'actualite et influence de nombreux systemes modernes.</p>

<hr/>

<h2>Documents de Cours</h2>

<p>Voici les supports de cours en PDF pour approfondir le systeme Unix :</p>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Cours Unix Complet</h4>
      <p>Guide complet du systeme Unix, commandes shell, scripts Bash, gestion de processus et administration systeme.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S5/Unix/unix-cours.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S5/Unix/unix-cours.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Telecharger le PDF
        </a>
      </p>
    </div>
    <div class="pdf-item">
      <h4>Memo Commandes Unix</h4>
      <p>Aide-memoire pratique des commandes Unix/Linux les plus utilisees pour la ligne de commande et les scripts.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S5/Unix/memo.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S5/Unix/memo.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Telecharger le PDF
        </a>
      </p>
    </div>
  </div>
</div>

</div>

<!-- ===================== ENGLISH VERSION ===================== -->
<div class="lang-en">

<h1>Unix Systems - S5</h1>

<p><strong>Year</strong>: 2022-2023 (Semester 5)<br/>
<strong>Credits</strong>: 3 ECTS<br/>
<strong>Type</strong>: Operating Systems</p>

<hr/>

<h2>PART A: GENERAL OVERVIEW</h2>

<h3 class="section-title">Course Objectives</h3>

<p>This course introduces Unix/Linux operating systems with a focus on practical use of the command line, shell programming, and basic system administration. The emphasis is on mastering essential tools for development and operation of embedded systems.</p>

<h3 class="section-title">Target Skills</h3>

<ul>
  <li>Master the Unix/Linux command line</li>
  <li>Write shell scripts for automation</li>
  <li>Manage files, processes and permissions</li>
  <li>Use text processing tools (grep, sed, awk)</li>
  <li>Understand the file system architecture</li>
  <li>Perform basic system administration tasks</li>
  <li>Combine commands with pipes and redirections</li>
  <li>Solve practical problems with Unix tools</li>
</ul>

<h3 class="section-title">Organization</h3>

<ul>
  <li><strong>Teaching hours</strong>: Lectures, tutorials and educational videos</li>
  <li><strong>Assessment</strong>: Written exam + practical exercises</li>
  <li><strong>Semester</strong>: 5 (2022-2023)</li>
  <li><strong>Prerequisites</strong>: Basic computer science knowledge</li>
</ul>

<hr/>

<h2>PART B: EXPERIENCE, CONTEXT AND FUNCTION</h2>

<h3 class="section-title">Course Content</h3>

<p>The course covers Unix fundamentals through a practical approach.</p>

<h4>1. Unix Fundamentals</h4>

<p><strong>Unix Philosophy</strong>:</p>

<p>Design principles:</p>
<ul>
  <li>Everything is a file (devices, sockets, processes)</li>
  <li>Simple programs that do one thing well</li>
  <li>Tool combination with pipes</li>
  <li>Text interfaces to facilitate automation</li>
  <li>Multi-user and multi-tasking system</li>
</ul>

<p><strong>System Architecture</strong>:</p>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S5/unix/architecture-unix.svg" alt="Unix/Linux Architecture" style="max-width: 500px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Layered architecture of a Unix/Linux system</p>
</div>

<table>
  <tr><th>Component</th><th>Function</th></tr>
  <tr><td>Kernel</td><td>Hardware management, processes, memory</td></tr>
  <tr><td>Shell</td><td>Command interpreter</td></tr>
  <tr><td>System programs</td><td>Basic utilities</td></tr>
  <tr><td>Applications</td><td>User software</td></tr>
</table>

<p><strong>Available shells</strong>:</p>
<ul>
  <li><strong>bash</strong> (Bourne Again Shell): most widespread</li>
  <li>sh (Bourne Shell): historical shell</li>
  <li>zsh (Z Shell): advanced shell with auto-completion</li>
  <li>csh/tcsh (C Shell): C-like syntax</li>
</ul>

<h4>2. File System</h4>

<p><strong>Standard directory tree</strong>:</p>

<p>Hierarchical structure starting from root (/).</p>

<table>
  <tr><th>Directory</th><th>Contents</th></tr>
  <tr><td>/bin</td><td>Essential commands (ls, cp, mv)</td></tr>
  <tr><td>/etc</td><td>Configuration files</td></tr>
  <tr><td>/home</td><td>User home directories</td></tr>
  <tr><td>/usr</td><td>Applications and utilities</td></tr>
  <tr><td>/var</td><td>Variable data (logs, caches)</td></tr>
  <tr><td>/tmp</td><td>Temporary files</td></tr>
  <tr><td>/dev</td><td>Device files</td></tr>
  <tr><td>/proc</td><td>System and process information</td></tr>
</table>

<p><strong>File types</strong>:</p>
<ul>
  <li><strong>Regular file</strong> (-): normal file</li>
  <li><strong>Directory</strong> (d): folder</li>
  <li><strong>Symbolic link</strong> (l): shortcut to another file</li>
  <li><strong>Block device</strong> (b): hard drive, USB</li>
  <li><strong>Character device</strong> (c): terminal, printer</li>
  <li><strong>Socket</strong> (s): inter-process communication</li>
  <li><strong>Named pipe</strong> (p): communication channel</li>
</ul>

<p><strong>Navigation commands</strong>:</p>

<pre><code class="language-bash">pwd                    # Display current directory
cd /path/to/dir        # Change directory
cd ..                  # Go up one level
cd ~                   # Go to home
cd -                   # Return to previous directory
ls                     # List files
ls -l                  # Detailed listing
ls -a                  # Show hidden files
ls -lh                 # Human-readable sizes (KB, MB)</code></pre>

<p><strong>File manipulation</strong>:</p>

<pre><code class="language-bash"># Creation
touch file.txt         # Create empty file
mkdir folder           # Create directory
mkdir -p a/b/c         # Create directory tree

# Copy and move
cp source dest         # Copy file
cp -r dir1 dir2        # Copy directory recursively
mv old new             # Rename/move

# Deletion
rm file                # Delete file
rm -r folder           # Delete directory recursively
rm -f file             # Force deletion
rmdir folder           # Delete empty directory</code></pre>

<p><strong>File viewing</strong>:</p>

<pre><code class="language-bash">cat file               # Display full content
more file              # Display page by page
less file              # Navigate through file
head file              # Display first lines
head -n 20 file        # Display first 20 lines
tail file              # Display last lines
tail -f file           # Follow additions in real time (logs)</code></pre>

<h4>3. Permissions and Access Rights</h4>

<p><strong>Permission system</strong>:</p>

<p>Format: <code>drwxrwxrwx</code></p>
<ul>
  <li>First character: file type</li>
  <li>Next 3 characters: owner (user) rights</li>
  <li>Next 3: group rights</li>
  <li>Last 3: others rights</li>
</ul>

<p><strong>Permission types</strong>:</p>

<table>
  <tr><th>Permission</th><th>File</th><th>Directory</th></tr>
  <tr><td>r (read)</td><td>Read content</td><td>List content</td></tr>
  <tr><td>w (write)</td><td>Modify file</td><td>Create/delete files</td></tr>
  <tr><td>x (execute)</td><td>Execute file</td><td>Access directory</td></tr>
</table>

<p><strong>Numeric representation</strong>:</p>

<p>Each permission has a value:</p>
<ul>
  <li>r = 4</li>
  <li>w = 2</li>
  <li>x = 1</li>
</ul>

<p>Examples:</p>
<ul>
  <li>755 = rwxr-xr-x (owner: all, others: read+execute)</li>
  <li>644 = rw-r--r-- (owner: read+write, others: read only)</li>
  <li>700 = rwx------ (owner only has all rights)</li>
  <li>777 = rwxrwxrwx (all rights for everyone)</li>
</ul>

<p><strong>Management commands</strong>:</p>

<pre><code class="language-bash"># Modify permissions
chmod 755 file                 # Numeric mode
chmod u+x file                 # Add execute for user
chmod g-w file                 # Remove write for group
chmod o+r file                 # Add read for others
chmod a+x file                 # Add execute for all

# Modify owner
chown user file                # Change owner
chown user:group file          # Change user and group
chgrp group file               # Change group only</code></pre>

<p><strong>Special permissions</strong>:</p>

<p><strong>SUID (Set User ID)</strong>: 4xxx or u+s</p>
<ul>
  <li>The file executes with the owner's rights</li>
  <li>Example: /usr/bin/passwd (allows users to change their password)</li>
</ul>

<p><strong>SGID (Set Group ID)</strong>: 2xxx or g+s</p>
<ul>
  <li>The file executes with the group's rights</li>
  <li>On a directory: created files inherit the group</li>
</ul>

<p><strong>Sticky bit</strong>: 1xxx or +t</p>
<ul>
  <li>On directory: only the owner can delete their files</li>
  <li>Example: /tmp (shared directory but protected files)</li>
</ul>

<p>Exam example:</p>
<pre><code class="language-bash">chmod 1777 /tmp/test3    # Sticky bit + all rights
chmod 750 /tmp/test1     # rwxr-x---
chmod 640 file           # rw-r-----</code></pre>

<h4>4. Process Management</h4>

<p><strong>Process concept</strong>:</p>

<p>A process is a running program.</p>

<p>Main attributes:</p>
<ul>
  <li><strong>PID</strong> (Process ID): unique identifier</li>
  <li><strong>PPID</strong> (Parent Process ID): parent process</li>
  <li><strong>UID</strong>: owner user</li>
  <li>State: running, sleeping, stopped, zombie</li>
  <li>Priority: nice value</li>
</ul>

<p><strong>Management commands</strong>:</p>

<pre><code class="language-bash"># Display processes
ps                    # Current user's processes
ps aux                # All processes detailed
ps -ef                # Long format
top                   # Real-time monitoring
htop                  # Improved version of top

# Process control
kill PID              # Send TERM signal (graceful termination)
kill -9 PID           # KILL signal (forced termination)
killall name          # Kill by program name
pkill pattern         # Kill by pattern

# Background
command &amp;             # Launch in background
jobs                  # List jobs
fg %1                 # Bring job 1 to foreground
bg %1                 # Continue job 1 in background
Ctrl+Z                # Suspend current process</code></pre>

<p><strong>Exam example analysis</strong>:</p>

<p>Command: <code>ps -ef | awk '{print $3}' | sort | uniq -c | awk '{print $2,$1}' | grep -v PPID</code></p>

<p>Breakdown:</p>
<ol>
  <li><code>ps -ef</code>: list all processes</li>
  <li><code>awk '{print $3}'</code>: extract PPID column (parent)</li>
  <li><code>sort</code>: sort PPIDs</li>
  <li><code>uniq -c</code>: count occurrences of each PPID</li>
  <li><code>awk '{print $2,$1}'</code>: swap columns (PPID then count)</li>
  <li><code>grep -v PPID</code>: exclude the header</li>
</ol>

<p>Result: list of processes with their number of children.</p>

<h4>5. Shell Programming (Bash)</h4>

<p><strong>Basic script structure</strong>:</p>

<pre><code class="language-bash">#!/bin/bash
# Shebang: specifies the interpreter to use

# This is a comment

echo "First shell script"</code></pre>

<p>Execution:</p>
<pre><code class="language-bash">chmod +x script.sh     # Make executable
./script.sh            # Execute</code></pre>

<p><strong>Variables</strong>:</p>

<pre><code class="language-bash"># Declaration (no spaces around =)
name="Cedric"
age=25
i=3

# Usage
echo "My name is $name"
echo "I am ${age} years old"

# Environment variables
echo $HOME             # Home directory
echo $PATH             # Command search paths
echo $USER             # Username</code></pre>

<p><strong>Reading input</strong>:</p>

<pre><code class="language-bash">echo "Enter a number:"
read number
echo "You entered: $number"

# Read into specific variable
read -p "Name: " name</code></pre>

<p><strong>Conditional structures</strong>:</p>

<pre><code class="language-bash"># if-then-else
if test $i -eq 3
then
  echo "i equals 3"
else
  echo "i does not equal 3"
fi

# Alternative form with brackets
if [ $i -eq 3 ]
then
  echo "i equals 3"
fi

# Numeric comparison operators
# -eq (equal), -ne (not equal), -lt (less than)
# -le (less or equal), -gt (greater than), -ge (greater or equal)

# String comparisons
if [ "$str1" = "$str2" ]
then
  echo "Strings are identical"
fi

# File tests
if [ -f file ]         # File exists
if [ -d folder ]       # Directory exists
if [ -r file ]         # File is readable
if [ -w file ]         # File is writable
if [ -x file ]         # File is executable

# Case
case $var in
  1) echo "One" ;;
  2) echo "Two" ;;
  *) echo "Other" ;;
esac</code></pre>

<p><strong>Loops</strong>:</p>

<pre><code class="language-bash"># For loop with sequence
for i in $(seq 1 100)
do
  echo $i
done

# For loop on files
for file in *.txt
do
  echo "Processing $file"
done

# For loop on command output
for file in $(ls *)
do
  echo $file
done

# While loop
counter=1
while [ $counter -le 10 ]
do
  echo $counter
  counter=$((counter + 1))
done

# While loop with file reading
while read line
do
  echo "Line: $line"
done &lt; file.txt

# Until (opposite of while)
until [ $counter -gt 10 ]
do
  echo $counter
  counter=$((counter + 1))
done</code></pre>

<p><strong>Arrays</strong>:</p>

<pre><code class="language-bash"># Declaration
tab[0]="first"
tab[1]="second"

# Or
declare -a tab
tab=("one" "two" "three")

# Filling in a loop
n=4
for i in $(seq 1 $n)
do
  tab[$i]="element$i"
done

# Access
echo ${tab[0]}         # First element
echo ${tab[*]}         # All elements
echo ${#tab[*]}        # Number of elements</code></pre>

<p><strong>Functions</strong>:</p>

<pre><code class="language-bash"># Definition
my_function() {
  echo "Hello $1"      # $1 = first argument
  return 0             # Return code
}

# Call
my_function "Cedric"</code></pre>

<p><strong>Common mistakes to avoid</strong>:</p>

<p>From the exam:</p>
<ol>
  <li>Forgetting the <code>!</code> in the shebang: <code>#!/bin/bash</code></li>
  <li>Spaces around <code>=</code>: use <code>i=3</code> not <code>i = 3</code></li>
  <li>Wrong loop syntax: <code>for i in $(seq 1 100)</code> not <code>for i in 1..100</code></li>
  <li>Wrong test: <code>if [ $i -eq 3 ]</code> not <code>if test $i == 3 then</code></li>
  <li>Close with <code>fi</code> not <code>end</code></li>
  <li>Use <code>$i</code> to read the variable, not <code>$REPLY</code></li>
  <li>Array access: <code>${tab[*]}</code> not <code>${tab}</code></li>
  <li>Command substitution: <code>$(command)</code> or <code>`command`</code></li>
</ol>

<h4>6. Text Processing</h4>

<p><strong>grep (pattern search)</strong>:</p>

<pre><code class="language-bash">grep "pattern" file              # Search for pattern
grep -i "pattern" file           # Case insensitive
grep -v "pattern" file           # Invert (lines without pattern)
grep -r "pattern" directory/     # Recursive in directory
grep -n "pattern" file           # Show line numbers
grep -c "pattern" file           # Count occurrences
grep -E "regex" file             # Extended regular expressions</code></pre>

<p><strong>sed (stream editor)</strong>:</p>

<pre><code class="language-bash"># Substitution
sed 's/old/new/' file                  # First occurrence per line
sed 's/old/new/g' file                 # All occurrences
sed -i 's/old/new/g' file             # Modify file in place

# Deletion
sed '/pattern/d' file                  # Delete lines containing pattern
sed '1d' file                          # Delete first line
sed '1,5d' file                        # Delete lines 1 to 5</code></pre>

<p><strong>awk (processing language)</strong>:</p>

<pre><code class="language-bash"># Display columns
awk '{print $1}' file                  # First column
awk '{print $1, $3}' file             # Columns 1 and 3
awk '{print $NF}' file                # Last column

# With conditions
awk '$3 &gt; 100 {print $1}' file        # If column 3 &gt; 100

# Exam example
ps -ef | awk '{print $3}'             # Extract PPID
echo "$line" | awk '{print $1}'       # Extract first field</code></pre>

<p><strong>Other tools</strong>:</p>

<pre><code class="language-bash">sort file                    # Sort lines
sort -n file                 # Numeric sort
sort -r file                 # Reverse sort
uniq file                    # Remove consecutive duplicates
uniq -c file                 # Count occurrences
wc file                      # Count lines, words, characters
wc -l file                   # Count lines only
cut -d':' -f1 file           # Extract first field (delimiter :)</code></pre>

<h4>7. Redirections and Pipes</h4>

<p><strong>Standard streams</strong>:</p>
<ul>
  <li><strong>stdin</strong> (0): standard input (keyboard)</li>
  <li><strong>stdout</strong> (1): standard output (screen)</li>
  <li><strong>stderr</strong> (2): error output (screen)</li>
</ul>

<p><strong>Redirections</strong>:</p>

<pre><code class="language-bash"># Output redirection
command &gt; file               # Overwrite file
command &gt;&gt; file              # Append to file
command 2&gt; errors.txt        # Redirect errors
command 2&gt;&amp;1                 # Errors to standard output
command &amp;&gt; file              # Output and errors to file

# Input redirection
command &lt; file               # Read from file
while read line
do
  echo $line
done &lt; file.txt

# Pipe (output of one command = input of next)
command1 | command2
ps aux | grep firefox
cat file | sort | uniq</code></pre>

<p><strong>Complex exam example</strong>:</p>

<pre><code class="language-bash">ps -ef | awk '{print $3}' | sort | uniq -c | awk '{print $2,$1}' | grep -v PPID &gt; /tmp/f</code></pre>

<p>Processing chain with 5 pipes combining several tools.</p>

<h4>8. Basic System Administration</h4>

<p><strong>System information</strong>:</p>

<pre><code class="language-bash">uname -a                # Full system info
hostname                # Machine name
whoami                  # Current user
who                     # Connected users
w                       # Users and activity
uptime                  # Uptime and load
date                    # Date and time</code></pre>

<p><strong>Disk management</strong>:</p>

<pre><code class="language-bash">df -h                   # Disk space (human-readable)
du -sh folder           # Directory size
du -sh *                # Size of all items</code></pre>

<p><strong>User management</strong>:</p>

<pre><code class="language-bash">passwd                  # Change password
sudo command            # Execute with root rights
su                      # Become root
su - user               # Switch user</code></pre>

<p><strong>File search</strong>:</p>

<pre><code class="language-bash">find /path -name "*.txt"             # By name
find /path -type f                   # Regular files
find /path -type d                   # Directories
find /path -mtime -7                 # Modified within 7 days
find /path -size +100M               # Size &gt; 100 MB
locate file                          # Fast search (database)
which command                        # Locate executable</code></pre>

<p><strong>Archiving and compression</strong>:</p>

<pre><code class="language-bash"># tar (tape archive)
tar -cvf archive.tar files/         # Create archive
tar -xvf archive.tar                # Extract archive
tar -tvf archive.tar                # List contents

# With compression
tar -czvf archive.tar.gz files/     # Create + gzip
tar -xzvf archive.tar.gz            # Extract gzip
tar -cjvf archive.tar.bz2 files/    # Create + bzip2

# zip/unzip
zip -r archive.zip folder/
unzip archive.zip</code></pre>

<p><strong>Links</strong>:</p>

<pre><code class="language-bash"># Symbolic link (shortcut)
ln -s /path/target link              # Create symbolic link

# Hard link (same inode)
ln original_file hard_link           # Create hard link</code></pre>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S5/unix/reseau-config1.png" alt="Unix Network Configuration" style="max-width: 600px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Example of network configuration under Unix/Linux - Practical lab</p>
</div>

<hr/>

<h2>PART C: TECHNICAL ASPECTS</h2>

<h3 class="section-title">Practical Exam Exercises</h3>

<p><strong>Exercise 1: Creating a directory tree with permissions</strong></p>

<p>Objective: reproduce a file structure exactly with the correct permissions.</p>

<pre><code class="language-bash"># Create the directory tree
mkdir -p /tmp/test/test1 /tmp/test/test2 /tmp/test/test3

# Create files
touch /tmp/test/test1/f1
touch /tmp/test/test2/f2
touch /tmp/test/test3/f3

# Set directory permissions
chmod 750 /tmp/test/test1    # rwxr-x---
chmod 754 /tmp/test/test2    # rwxr-xr--
chmod 1777 /tmp/test/test3   # rwxrwxrwt (with sticky bit)

# Set file permissions
chmod 640 /tmp/test/test1/f1 # rw-r-----
chmod 444 /tmp/test/test2/f2 # r--r--r--
chmod 700 /tmp/test/test3/f3 # rwx------</code></pre>

<p><strong>Special permissions explanation</strong>:</p>

<p><code>chmod 1777</code>: the leading <code>1</code> corresponds to the sticky bit.</p>
<ul>
  <li>Allows everyone to create files in the directory</li>
  <li>But only the owner can delete their own files</li>
  <li>Typical for /tmp</li>
</ul>

<p><strong>Exercise 2: Shell script correction</strong></p>

<p>Script with errors:</p>
<pre><code class="language-bash">#/bin/bash                          # ERROR: missing !

for i in 1..100                     # ERROR: incorrect syntax
do
 echo $i
done

for i in ls *                       # ERROR: missing $()
do
  echo $i
done

i = 3                               # ERROR: spaces around =

if test $i == 3 then                # ERROR: -eq instead of ==, then misplaced
  echo yes
else
  echo no
end                                 # ERROR: should be fi

echo "an integer please"
read i
echo integer entered: $REPLY        # ERROR: should be $i

n=4
for i in `seq 1 $n`
do
  tab[i]="toto"
done
echo ${tab}                         # ERROR: should be ${tab[*]}</code></pre>

<p>Corrected version:</p>
<pre><code class="language-bash">#!/bin/bash

for i in $(seq 1 100)
do
 echo $i
done

for i in $(ls *)
# or simpler: for i in *
do
  echo $i
done

i=3

if [ $i -eq 3 ]
then
  echo yes
else
  echo no
fi

echo "an integer please"
read i
echo integer entered: $i

n=4
for i in $(seq 1 $n)
do
  tab[$i]="toto"
done
echo ${tab[*]}</code></pre>

<p><strong>Exercise 3: Complex pipeline analysis</strong></p>

<p>Parent process analysis script:</p>

<pre><code class="language-bash">#!/bin/bash

# Complex pipeline
ps -ef | awk '{print $3}' | sort | uniq -c | awk '{print $2,$1}' | grep -v PPID &gt; /tmp/f

# Processing loop
while read v
do
  a=$(echo $v | awk '{print $1}')   # PID
  b=$(echo $v | awk '{print $2}')   # Number of children
  echo process $a has $b children
done &lt; /tmp/f</code></pre>

<p><strong>Detailed pipeline explanation</strong>:</p>
<ol>
  <li><code>ps -ef</code>: displays all processes with PID, PPID, etc.</li>
  <li><code>awk '{print $3}'</code>: extracts the 3rd column (PPID)</li>
  <li><code>sort</code>: sorts PPIDs numerically</li>
  <li><code>uniq -c</code>: counts occurrences of each unique PPID</li>
  <li><code>awk '{print $2,$1}'</code>: reverses order (PPID then counter)</li>
  <li><code>grep -v PPID</code>: excludes the header line</li>
  <li><code>&gt; /tmp/f</code>: saves to a temporary file</li>
</ol>

<p>Result in /tmp/f: each line contains a PID and the number of times it appears as a parent (number of children).</p>

<p><strong>The while loop</strong>:</p>

<p>Reads each line from /tmp/f and extracts:</p>
<ul>
  <li>Variable <code>a</code>: the process PID</li>
  <li>Variable <code>b</code>: the number of children of this process</li>
</ul>

<p>Outputs: "process XXX has YYY children"</p>

<p><strong>Exercise 4: Permissions and security</strong></p>

<p>Analysis of a game's permissions:</p>

<pre><code class="language-bash">drwxr-xr-x 2 student students 4096 game/
-r-sr-xr-x 1 student students 133792 the_game_binary
-rw------- 1 student students 39 the_scores_file</code></pre>

<p><strong>Analysis</strong>:</p>

<p><strong>The binary (r-sr-xr-x)</strong>:</p>
<ul>
  <li>SUID bit enabled (s instead of x for user)</li>
  <li>Everyone can execute it (r-x for group and others)</li>
  <li>The game runs with <code>student</code>'s rights</li>
  <li>Allows access to the scores file</li>
</ul>

<p><strong>The scores file (rw-------)</strong>:</p>
<ul>
  <li>Readable/writable only by <code>student</code></li>
  <li>Other users cannot read or write</li>
  <li>Protection of scores against cheating</li>
</ul>

<p><strong>Logic</strong>:</p>
<ul>
  <li>Players execute the binary with SUID</li>
  <li>The program runs as <code>student</code></li>
  <li>It can therefore modify the scores file</li>
  <li>But players cannot modify scores directly</li>
  <li>Prevents cheating while allowing the game to be played</li>
</ul>

<h3 class="section-title">Essential Commands to Master</h3>

<p><strong>Navigation and files</strong>:</p>
<pre><code class="language-bash">pwd, cd, ls, mkdir, rmdir, touch, cp, mv, rm, cat, more, less, head, tail</code></pre>

<p><strong>Permissions</strong>:</p>
<pre><code class="language-bash">chmod, chown, chgrp, umask</code></pre>

<p><strong>Processes</strong>:</p>
<pre><code class="language-bash">ps, top, kill, killall, bg, fg, jobs</code></pre>

<p><strong>Search</strong>:</p>
<pre><code class="language-bash">find, locate, which, whereis, grep</code></pre>

<p><strong>Text processing</strong>:</p>
<pre><code class="language-bash">grep, sed, awk, sort, uniq, wc, cut, tr</code></pre>

<p><strong>System</strong>:</p>
<pre><code class="language-bash">uname, hostname, whoami, who, w, df, du, free, date</code></pre>

<p><strong>Archiving</strong>:</p>
<pre><code class="language-bash">tar, gzip, gunzip, zip, unzip</code></pre>

<hr/>

<h2>PART D: ANALYSIS AND REFLECTION</h2>

<h3 class="section-title">Skills Acquired</h3>

<p><strong>Command line</strong>:</p>
<ul>
  <li>Mastery of essential Unix commands</li>
  <li>Efficient navigation in the file system</li>
  <li>File and directory management</li>
  <li>Using documentation (man)</li>
</ul>

<p><strong>Scripting</strong>:</p>
<ul>
  <li>Automation of repetitive tasks</li>
  <li>Shell programming with bash</li>
  <li>Control structures (loops, conditions)</li>
  <li>Variable and array manipulation</li>
  <li>Text file processing</li>
</ul>

<p><strong>System administration</strong>:</p>
<ul>
  <li>Permission management and security</li>
  <li>Process management</li>
  <li>System monitoring</li>
  <li>Archiving and backup</li>
</ul>

<p><strong>Advanced tools</strong>:</p>
<ul>
  <li>Pipes and redirections to combine commands</li>
  <li>Regular expressions for searching</li>
  <li>Stream processing with awk and sed</li>
  <li>Log and file analysis</li>
</ul>

<h3 class="section-title">Practical Applications</h3>

<p>Unix/Linux is ubiquitous in modern computing:</p>

<p><strong>Software development</strong>:</p>
<ul>
  <li>Development environment</li>
  <li>Compilation and build</li>
  <li>Version control (Git)</li>
  <li>Automated testing</li>
</ul>

<p><strong>Embedded systems</strong>:</p>
<ul>
  <li>Embedded Linux on Raspberry Pi, BeagleBone</li>
  <li>IoT systems</li>
  <li>Routers and network equipment</li>
  <li>Android (based on Linux)</li>
</ul>

<p><strong>Servers and Cloud</strong>:</p>
<ul>
  <li>Web servers (Apache, Nginx)</li>
  <li>Databases (MySQL, PostgreSQL)</li>
  <li>Cloud services (AWS, Azure, GCP)</li>
  <li>Containers (Docker, Kubernetes)</li>
</ul>

<p><strong>System administration</strong>:</p>
<ul>
  <li>Server management</li>
  <li>Automation (scripts, cron)</li>
  <li>Monitoring and logs</li>
  <li>Backups</li>
</ul>

<p><strong>DevOps</strong>:</p>
<ul>
  <li>Continuous deployment (CI/CD)</li>
  <li>Infrastructure automation</li>
  <li>Configuration management (Ansible, Puppet)</li>
  <li>Container orchestration</li>
</ul>

<h3 class="section-title">Links with Other Courses</h3>

<table>
  <tr><th>Course</th><th>Connection</th></tr>
  <tr><td>C Language (S5)</td><td>System programming, system calls</td></tr>
  <tr><td>Operating Systems (S5)</td><td>Process concepts, memory</td></tr>
  <tr><td>Networking (S5)</td><td>Network commands, sockets</td></tr>
  <tr><td>Hardware Architecture (S5)</td><td>Device management, drivers</td></tr>
  <tr><td>Real-Time Systems (S8)</td><td>Real-time Linux, scheduling</td></tr>
  <tr><td>Cloud Computing (S9)</td><td>Linux servers, administration</td></tr>
</table>

<h3 class="section-title">Working Methodology</h3>

<p><strong>Learning by practice</strong>:</p>

<p>The best way to learn Unix is to practice daily:</p>
<ul>
  <li>Use the terminal instead of the graphical interface</li>
  <li>Write scripts to automate your tasks</li>
  <li>Read the man pages of commands</li>
  <li>Experiment in a VM to avoid mistakes</li>
</ul>

<p><strong>Useful resources</strong>:</p>
<ul>
  <li><code>man command</code>: built-in documentation</li>
  <li><code>command --help</code>: quick help</li>
  <li><code>/usr/share/doc</code>: detailed documentation</li>
  <li>StackOverflow and Linux forums</li>
  <li>Books: "The Linux Command Line", "Unix and Linux System Administration Handbook"</li>
</ul>

<p><strong>Best practices</strong>:</p>

<p>Scripts:</p>
<ul>
  <li>Always include the shebang</li>
  <li>Comment your code</li>
  <li>Handle errors</li>
  <li>Test before deployment</li>
</ul>

<p>Security:</p>
<ul>
  <li>Principle of least privilege</li>
  <li>Avoid running as root</li>
  <li>Check permissions</li>
  <li>Back up before major changes</li>
</ul>

<h3 class="section-title">My Opinion</h3>

<p>This course is fundamental for any computer science or electronics engineer.</p>

<p><strong>Strengths</strong>:</p>
<ul>
  <li>Immediately applicable skills</li>
  <li>Universality (Unix/Linux everywhere)</li>
  <li>Command line efficiency</li>
  <li>Powerful automation with scripts</li>
</ul>

<p><strong>Professional importance</strong>:</p>

<p>Unix/Linux is essential for:</p>
<ul>
  <li>Embedded systems development</li>
  <li>Server administration</li>
  <li>DevOps and Cloud</li>
  <li>IoT and connected objects</li>
  <li>Artificial intelligence (computing environments)</li>
</ul>

<p><strong>Productivity</strong>:</p>

<p>Mastering the command line allows you to:</p>
<ul>
  <li>Automate repetitive tasks (time savings)</li>
  <li>Process large volumes of data</li>
  <li>Work on remote systems (SSH)</li>
  <li>Script custom solutions</li>
  <li>Diagnose problems efficiently</li>
</ul>

<p><strong>Complementarity with other skills</strong>:</p>

<p>Unix integrates perfectly with:</p>
<ul>
  <li>C/C++ programming (compilation, debugging)</li>
  <li>Web development (servers, deployment)</li>
  <li>Data science (data processing)</li>
  <li>Cybersecurity (log analysis, forensics)</li>
</ul>

<h3 class="section-title">Future Perspectives</h3>

<p><strong>Emerging technologies</strong>:</p>

<p><strong>Containers</strong>: Docker and Kubernetes make intensive use of Unix.</p>
<p><strong>Edge Computing</strong>: Linux on embedded devices.</p>
<p><strong>Automation</strong>: Infrastructure as Code (Terraform, Ansible).</p>
<p><strong>Cloud native</strong>: Microservices on Linux.</p>

<h3 class="section-title">Practical Tips</h3>

<p><strong>To improve</strong>:</p>
<ol>
  <li>Use Linux as your main system (dual-boot or VM)</li>
  <li>Customize your environment (bashrc, aliases)</li>
  <li>Contribute to open-source projects</li>
  <li>Set up a personal server (web, NAS)</li>
  <li>Automate your daily tasks with scripts</li>
</ol>

<p><strong>Mistakes to avoid</strong>:</p>
<ul>
  <li>Never run <code>rm -rf /</code> even out of curiosity</li>
  <li>Always verify before <code>rm -rf</code></li>
  <li>Back up before system changes</li>
  <li>Test scripts in a test environment</li>
  <li>Read the documentation before use</li>
</ul>

<hr/>

<p><strong>Personal assessment</strong>: This course provided the essential foundations for working effectively in a Unix/Linux environment. Mastery of the command line and shell scripts is a valuable cross-cutting skill for any career in computer science or electronics. This knowledge is useful daily, whether for development, system administration, or application deployment. The Unix philosophy (simple and combinable tools) remains relevant and influences many modern systems.</p>

<hr/>

<h2>Course Documents</h2>

<p>Here are the course materials in PDF to deepen your understanding of Unix systems:</p>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Complete Unix Course</h4>
      <p>Comprehensive guide to Unix systems, shell commands, Bash scripts, process management and system administration.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S5/Unix/unix-cours.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S5/Unix/unix-cours.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Download PDF
        </a>
      </p>
    </div>
    <div class="pdf-item">
      <h4>Unix Command Cheat Sheet</h4>
      <p>Practical cheat sheet of the most commonly used Unix/Linux commands for the command line and scripts.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S5/Unix/memo.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S5/Unix/memo.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Download PDF
        </a>
      </p>
    </div>
  </div>
</div>

</div>

<div class="back-nav">
  <a href="./my-courses-2022-2023.html" data-i18n-html="back-courses-2022-2023">&larr; Retour aux Cours 2022-2023</a>
</div>

<em class="lang-fr">Redige par Cedric Chanfreau</em><em class="lang-en">Written by Cedric Chanfreau</em>

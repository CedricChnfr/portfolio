---
layout: default
title: "Programmation - S1"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
---

<style>
.back-nav { margin-bottom: 20px; }
.back-nav a { text-decoration: none; color: #2a7ae2; font-weight: 600; }
.back-nav a:hover { text-decoration: underline; }
.section-title { color: #2a7ae2; border-bottom: 2px solid #2a7ae2; padding-bottom: 10px; margin-top: 30px; margin-bottom: 20px; }
</style>

<div class="back-nav">
  <a href="./my-courses-2020-2021.html" data-i18n-html="back-courses-2020-2021">&larr; Retour a Mes Cours 2020-2021</a>
</div>

<div class="lang-fr">

<h1>Programmation - Semestre 1</h1>

<h2>PART A - Presentation Generale du Cours</h2>

<h3>Contexte de la formation</h3>

<p>La programmation est une competence fondamentale pour tout technicien ou ingenieur en GEII. Elle permet de controler des systemes embarques, automatiser des taches, traiter des donnees et developper des applications. Ce premier module de programmation, dispense en C++, pose les bases de la pensee algorithmique et de la programmation structuree, competences essentielles pour les projets futurs et la vie professionnelle.</p>

<h3>Positionnement dans le cursus</h3>
<ul>
<li><strong>Semestre</strong> : S1 (1ere annee DUT GEII)</li>
<li><strong>Volume horaire</strong> : 60h (20h CM + 25h TD + 15h TP)</li>
<li><strong>Credits ECTS</strong> : 5</li>
<li><strong>Prerequis</strong> : Aucun prerequis en programmation (debutants acceptes)</li>
<li><strong>Continuite</strong> : Programmation S2 (C/C++ avance), puis S3-S4 (embarque, Python)</li>
</ul>

<h3>Public vise</h3>
<p>Etudiants de premiere annee DUT GEII, debutants ou ayant quelques notions en programmation. Le cours s'adresse a tous les profils, avec une pedagogie progressive permettant a chacun de reussir.</p>

<hr/>

<h2>PART B: EXPERIENCE, CONTEXTE ET FONCTION</h2>

<h3>Objectifs pedagogiques</h3>

<p><strong>Competences algorithmiques :</strong></p>
<ul>
<li>Analyser un probleme et le decomposer en etapes</li>
<li>Concevoir des algorithmes structures et efficaces</li>
<li>Evaluer la complexite d'un algorithme</li>
<li>Deboguer et tester son code</li>
</ul>

<p><strong>Competences techniques C++ :</strong></p>
<ul>
<li>Maitriser la syntaxe de base du C++</li>
<li>Utiliser les structures de controle (conditions, boucles)</li>
<li>Manipuler les tableaux et les chaines de caracteres</li>
<li>Creer et utiliser des fonctions</li>
<li>Comprendre et utiliser les pointeurs (introduction)</li>
</ul>

<p><strong>Competences methodologiques :</strong></p>
<ul>
<li>Utiliser un environnement de developpement (IDE)</li>
<li>Compiler et executer un programme</li>
<li>Deboguer avec des outils appropries</li>
<li>Documenter son code</li>
<li>Travailler en mode projet</li>
</ul>

<h3>Programme detaille</h3>

<h4>1. Introduction a la programmation (5h)</h4>

<p><strong>Concepts fondamentaux :</strong></p>
<ul>
<li>Qu'est-ce qu'un programme ? Un algorithme ?</li>
<li>Langages de programmation (compiles vs interpretes)</li>
<li>Processus de compilation (source &rarr; compilation &rarr; executable)</li>
<li>Structure d'un programme C++</li>
</ul>

<p><strong>Premier programme "Hello World" :</strong></p>
<div class="code-block">
<pre><code>#include &lt;iostream&gt;
using namespace std;

int main() {
    cout &lt;&lt; "Hello, World!" &lt;&lt; endl;
    return 0;
}</code></pre>
</div>

<p><strong>Elements de syntaxe :</strong></p>
<ul>
<li>Directives du preprocesseur (#include)</li>
<li>Fonction main()</li>
<li>Instructions et point-virgule</li>
<li>Entrees/sorties (cin, cout)</li>
<li>Commentaires (// et /* */)</li>
</ul>

<h4>2. Variables et types de donnees (8h)</h4>

<p><strong>Types de base (primitifs) :</strong></p>
<div class="code-block">
<pre><code>int age = 20;              // Entier signe (4 octets)
unsigned int count = 100;  // Entier non signe
float temperature = 25.5;  // Flottant simple precision
double pi = 3.14159265359; // Flottant double precision
char letter = 'A';         // Caractere (1 octet)
bool isValid = true;       // Booleen (true/false)</code></pre>
</div>

<p><strong>Declaration et initialisation :</strong></p>
<ul>
<li>Declaration : <code>int x;</code></li>
<li>Initialisation : <code>int x = 10;</code></li>
<li>Affectation : <code>x = 20;</code></li>
<li>Constantes : <code>const double PI = 3.14159;</code></li>
</ul>

<p><strong>Operateurs :</strong></p>
<ul>
<li><strong>Arithmetiques</strong> : +, -, *, /, % (modulo)</li>
<li><strong>Comparaison</strong> : ==, !=, &lt;, &gt;, &lt;=, &gt;=</li>
<li><strong>Logiques</strong> : &amp;&amp; (AND), || (OR), ! (NOT)</li>
<li><strong>Incrementation</strong> : ++, --</li>
<li><strong>Affectation composee</strong> : +=, -=, *=, /=</li>
</ul>

<p><strong>Conversions de types (cast) :</strong></p>
<div class="code-block">
<pre><code>int a = 10;
float b = 3.7;
int result = a + (int)b;  // Cast explicite
float average = (float)a / 3;  // Division flottante</code></pre>
</div>

<p><strong>Entrees/sorties utilisateur :</strong></p>
<div class="code-block">
<pre><code>int age;
cout &lt;&lt; "Entrez votre age : ";
cin &gt;&gt; age;
cout &lt;&lt; "Vous avez " &lt;&lt; age &lt;&lt; " ans" &lt;&lt; endl;</code></pre>
</div>

<h4>3. Structures de controle (10h)</h4>

<p><strong>Instructions conditionnelles :</strong></p>

<p><strong>if / else if / else :</strong></p>
<div class="code-block">
<pre><code>if (temperature &gt; 30) {
    cout &lt;&lt; "Il fait chaud" &lt;&lt; endl;
}
else if (temperature &gt; 20) {
    cout &lt;&lt; "Il fait bon" &lt;&lt; endl;
}
else {
    cout &lt;&lt; "Il fait froid" &lt;&lt; endl;
}</code></pre>
</div>

<p><strong>Operateur ternaire :</strong></p>
<div class="code-block">
<pre><code>int max = (a &gt; b) ? a : b;  // Si a&gt;b alors max=a sinon max=b</code></pre>
</div>

<p><strong>Switch / case :</strong></p>
<div class="code-block">
<pre><code>int choice;
cin &gt;&gt; choice;

switch (choice) {
    case 1:
        cout &lt;&lt; "Option 1" &lt;&lt; endl;
        break;
    case 2:
        cout &lt;&lt; "Option 2" &lt;&lt; endl;
        break;
    default:
        cout &lt;&lt; "Option invalide" &lt;&lt; endl;
}</code></pre>
</div>

<p><strong>Boucles :</strong></p>

<p><strong>Boucle for (nombre d'iterations connu) :</strong></p>
<div class="code-block">
<pre><code>// Afficher les nombres de 1 a 10
for (int i = 1; i &lt;= 10; i++) {
    cout &lt;&lt; i &lt;&lt; " ";
}</code></pre>
</div>

<p><strong>Boucle while (condition en entree) :</strong></p>
<div class="code-block">
<pre><code>int i = 1;
while (i &lt;= 10) {
    cout &lt;&lt; i &lt;&lt; " ";
    i++;
}</code></pre>
</div>

<p><strong>Boucle do-while (condition en sortie, au moins 1 iteration) :</strong></p>
<div class="code-block">
<pre><code>int number;
do {
    cout &lt;&lt; "Entrez un nombre positif : ";
    cin &gt;&gt; number;
} while (number &lt;= 0);</code></pre>
</div>

<p><strong>break et continue :</strong></p>
<div class="code-block">
<pre><code>for (int i = 0; i &lt; 10; i++) {
    if (i == 5) continue;  // Passer a l'iteration suivante
    if (i == 8) break;     // Sortir de la boucle
    cout &lt;&lt; i &lt;&lt; " ";
}
// Affiche : 0 1 2 3 4 6 7</code></pre>
</div>

<h4>4. Tableaux et chaines de caracteres (10h)</h4>

<p><strong>Tableaux statiques (arrays) :</strong></p>
<div class="code-block">
<pre><code>// Declaration et initialisation
int notes[5] = {12, 15, 10, 18, 14};

// Acces aux elements (index commence a 0)
cout &lt;&lt; "Premiere note : " &lt;&lt; notes[0] &lt;&lt; endl;
notes[2] = 16;  // Modification

// Parcours avec boucle
float somme = 0;
for (int i = 0; i &lt; 5; i++) {
    somme += notes[i];
}
float moyenne = somme / 5;</code></pre>
</div>

<p><strong>Tableaux multidimensionnels :</strong></p>
<div class="code-block">
<pre><code>int matrice[3][4] = {
    {1, 2, 3, 4},
    {5, 6, 7, 8},
    {9, 10, 11, 12}
};

// Parcours avec boucles imbriquees
for (int i = 0; i &lt; 3; i++) {
    for (int j = 0; j &lt; 4; j++) {
        cout &lt;&lt; matrice[i][j] &lt;&lt; " ";
    }
    cout &lt;&lt; endl;
}</code></pre>
</div>

<p><strong>Chaines de caracteres (C-style strings) :</strong></p>
<div class="code-block">
<pre><code>char nom[50];
cout &lt;&lt; "Entrez votre nom : ";
cin &gt;&gt; nom;

// Fonctions de &lt;cstring&gt;
#include &lt;cstring&gt;
strlen(nom);        // Longueur
strcpy(dest, src);  // Copie
strcat(s1, s2);     // Concatenation
strcmp(s1, s2);      // Comparaison (0 si egales)</code></pre>
</div>

<p><strong>Chaines C++ (std::string) :</strong></p>
<div class="code-block">
<pre><code>#include &lt;string&gt;

string prenom = "Jean";
string nom = "Dupont";
string complet = prenom + " " + nom;  // Concatenation

cout &lt;&lt; complet.length() &lt;&lt; endl;  // Longueur
cout &lt;&lt; complet[0] &lt;&lt; endl;        // Premier caractere
complet += " Jr.";                 // Ajout a la fin</code></pre>
</div>

<h4>5. Fonctions (12h)</h4>

<p><strong>Declaration et definition :</strong></p>
<div class="code-block">
<pre><code>// Declaration (prototype)
int addition(int a, int b);

// Definition
int addition(int a, int b) {
    return a + b;
}

// Utilisation
int main() {
    int resultat = addition(5, 3);
    cout &lt;&lt; "5 + 3 = " &lt;&lt; resultat &lt;&lt; endl;
    return 0;
}</code></pre>
</div>

<p><strong>Passage de parametres :</strong></p>

<p><strong>Par valeur (copie) :</strong></p>
<div class="code-block">
<pre><code>void incrementer(int x) {
    x++;  // Modification locale, pas d'effet sur l'original
}

int main() {
    int a = 5;
    incrementer(a);
    cout &lt;&lt; a &lt;&lt; endl;  // Affiche 5 (inchange)
}</code></pre>
</div>

<p><strong>Par reference (modification de l'original) :</strong></p>
<div class="code-block">
<pre><code>void incrementer(int&amp; x) {  // Notez le &amp;
    x++;  // Modifie l'original
}

int main() {
    int a = 5;
    incrementer(a);
    cout &lt;&lt; a &lt;&lt; endl;  // Affiche 6
}</code></pre>
</div>

<p><strong>Fonctions void (sans retour) :</strong></p>
<div class="code-block">
<pre><code>void afficherMessage() {
    cout &lt;&lt; "Bonjour !" &lt;&lt; endl;
    // Pas de return (ou return; sans valeur)
}</code></pre>
</div>

<p><strong>Surcharge de fonctions (overloading) :</strong></p>
<div class="code-block">
<pre><code>int addition(int a, int b) {
    return a + b;
}

double addition(double a, double b) {
    return a + b;
}

// Le compilateur choisit selon les types des arguments</code></pre>
</div>

<p><strong>Valeurs par defaut :</strong></p>
<div class="code-block">
<pre><code>void afficher(string texte, int repetitions = 1) {
    for (int i = 0; i &lt; repetitions; i++) {
        cout &lt;&lt; texte &lt;&lt; endl;
    }
}

afficher("Bonjour");      // Utilise 1 par defaut
afficher("Bonjour", 3);   // Affiche 3 fois</code></pre>
</div>

<h4>6. Structures (struct) (8h)</h4>

<p><strong>Definition et utilisation :</strong></p>
<div class="code-block">
<pre><code>struct Point {
    double x;
    double y;
};

int main() {
    Point p1;
    p1.x = 10.5;
    p1.y = 20.3;

    Point p2 = {5.0, 7.0};  // Initialisation

    cout &lt;&lt; "Point 1 : (" &lt;&lt; p1.x &lt;&lt; ", " &lt;&lt; p1.y &lt;&lt; ")" &lt;&lt; endl;
}</code></pre>
</div>

<p><strong>Structures imbriquees :</strong></p>
<div class="code-block">
<pre><code>struct Adresse {
    string rue;
    int codePostal;
    string ville;
};

struct Personne {
    string nom;
    int age;
    Adresse adresse;
};

Personne p;
p.nom = "Dupont";
p.adresse.ville = "Toulouse";</code></pre>
</div>

<p><strong>Tableaux de structures :</strong></p>
<div class="code-block">
<pre><code>struct Etudiant {
    string nom;
    float moyenne;
};

Etudiant classe[30];
classe[0].nom = "Alice";
classe[0].moyenne = 15.5;</code></pre>
</div>

<h4>7. Introduction aux pointeurs (7h)</h4>

<p><strong>Concept de pointeur :</strong></p>
<div class="code-block">
<pre><code>int x = 10;
int* ptr = &amp;x;  // ptr contient l'adresse de x

cout &lt;&lt; "Valeur de x : " &lt;&lt; x &lt;&lt; endl;
cout &lt;&lt; "Adresse de x : " &lt;&lt; &amp;x &lt;&lt; endl;
cout &lt;&lt; "Valeur de ptr : " &lt;&lt; ptr &lt;&lt; endl;
cout &lt;&lt; "Valeur pointee : " &lt;&lt; *ptr &lt;&lt; endl;  // Dereferencement</code></pre>
</div>

<p><strong>Modification via pointeur :</strong></p>
<div class="code-block">
<pre><code>int a = 5;
int* p = &amp;a;
*p = 10;  // a vaut maintenant 10</code></pre>
</div>

<p><strong>Pointeurs et tableaux :</strong></p>
<div class="code-block">
<pre><code>int tab[5] = {10, 20, 30, 40, 50};
int* p = tab;  // Pointeur sur le premier element

for (int i = 0; i &lt; 5; i++) {
    cout &lt;&lt; *(p + i) &lt;&lt; " ";  // Acces par arithmetique de pointeurs
}</code></pre>
</div>

<p><strong>Pointeurs et fonctions :</strong></p>
<div class="code-block">
<pre><code>void echanger(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int x = 5, y = 10;
    echanger(&amp;x, &amp;y);
    cout &lt;&lt; "x = " &lt;&lt; x &lt;&lt; ", y = " &lt;&lt; y &lt;&lt; endl;  // x=10, y=5
}</code></pre>
</div>

<h3>Semaine intensive de programmation</h3>

<p><strong>Projet integratif (40h sur 1 semaine) :</strong></p>

<p>Realisation d'un projet complet mobilisant toutes les competences :</p>
<ul>
<li>Analyse et decomposition du probleme</li>
<li>Conception de l'algorithme (organigramme ou pseudo-code)</li>
<li>Implementation en C++</li>
<li>Tests et debogage</li>
<li>Documentation et presentation</li>
</ul>

<p><strong>Exemples de projets :</strong></p>
<ol>
<li><strong>Jeu du pendu</strong> : Gestion de chaines, structures de controle</li>
<li><strong>Gestion de contacts</strong> : Tableaux de structures, fichiers</li>
<li><strong>Calculatrice scientifique</strong> : Fonctions mathematiques, switch/case</li>
<li><strong>Jeu de la vie (Conway)</strong> : Tableaux 2D, algorithmique</li>
<li><strong>Gestionnaire de notes</strong> : Calculs statistiques, tri</li>
</ol>

<p><strong>Organisation :</strong></p>
<ul>
<li>Travail en binome</li>
<li>Suivi quotidien par les enseignants</li>
<li>Presentation finale (demo + code)</li>
<li>Rapport technique</li>
</ul>

<hr/>

<h2>PART C: ASPECTS TECHNIQUES</h2>

<h3>Environnements de developpement (IDE)</h3>

<h4>Code::Blocks (recommande pour debutants)</h4>

<p><strong>Installation :</strong></p>
<ul>
<li>Telecharger sur codeblocks.org</li>
<li>Version avec MinGW (compilateur GCC inclus)</li>
<li>Configuration automatique</li>
</ul>

<p><strong>Fonctionnalites :</strong></p>
<ul>
<li>Coloration syntaxique</li>
<li>Auto-completion</li>
<li>Compilation en un clic (F9)</li>
<li>Debogueur integre</li>
<li>Gestion de projets</li>
</ul>

<p><strong>Creation d'un projet :</strong></p>
<ol>
<li>File &rarr; New &rarr; Project &rarr; Console Application</li>
<li>Choisir C++</li>
<li>Nommer le projet et choisir l'emplacement</li>
<li>Code genere automatiquement</li>
</ol>

<h4>Visual Studio (Windows)</h4>

<p><strong>Avantages :</strong></p>
<ul>
<li>IDE professionnel puissant</li>
<li>Excellent debogueur</li>
<li>IntelliSense (auto-completion avancee)</li>
<li>Outils de profilage</li>
</ul>

<p><strong>Creation d'un projet :</strong></p>
<ul>
<li>File &rarr; New &rarr; Project &rarr; Empty Project (C++)</li>
<li>Ajouter un fichier .cpp</li>
<li>Build &rarr; Build Solution (Ctrl+Shift+B)</li>
<li>Debug &rarr; Start Debugging (F5)</li>
</ul>

<h4>VS Code (multiplateforme)</h4>

<p><strong>Configuration pour C++ :</strong></p>
<ol>
<li>Installer VS Code</li>
<li>Installer extension "C/C++"</li>
<li>Installer MinGW (Windows) ou GCC (Linux/Mac)</li>
<li>Configurer tasks.json pour compilation</li>
</ol>

<p><strong>Avantages :</strong></p>
<ul>
<li>Leger et rapide</li>
<li>Tres personnalisable</li>
<li>Extensions nombreuses</li>
<li>Integration Git native</li>
</ul>

<h3>Compilation et debogage</h3>

<h4>Processus de compilation</h4>

<p><strong>Etapes :</strong></p>
<div class="code-block">
<pre><code>Code source (.cpp) &rarr; Preprocesseur &rarr; Compilateur &rarr;
Assembleur &rarr; Linker &rarr; Executable (.exe ou binaire)</code></pre>
</div>

<p><strong>Compilation en ligne de commande :</strong></p>
<div class="code-block">
<pre><code># Compilation simple
g++ programme.cpp -o programme

# Avec warnings et optimisation
g++ -Wall -Wextra -O2 programme.cpp -o programme

# Avec informations de debug
g++ -g programme.cpp -o programme

# Execution
./programme  # Linux/Mac
programme.exe  # Windows</code></pre>
</div>

<h4>Debogage avec GDB</h4>

<p><strong>Commandes de base :</strong></p>
<div class="code-block">
<pre><code>gdb ./programme

(gdb) break main       # Point d'arret sur main
(gdb) run             # Lancer le programme
(gdb) next            # Ligne suivante (sans entrer dans fonctions)
(gdb) step            # Ligne suivante (en entrant dans fonctions)
(gdb) print variable  # Afficher valeur d'une variable
(gdb) continue        # Continuer jusqu'au prochain breakpoint
(gdb) quit            # Quitter GDB</code></pre>
</div>

<p><strong>Debogage dans IDE :</strong></p>
<ul>
<li>Placer des breakpoints (clic marge gauche)</li>
<li>F5 : Lancer en mode debug</li>
<li>F10 : Passer a la ligne suivante</li>
<li>F11 : Entrer dans une fonction</li>
<li>Inspecter les variables dans la fenetre "Watch"</li>
</ul>

<h3>Bonnes pratiques de programmation</h3>

<h4>Style et conventions</h4>

<p><strong>Nommage :</strong></p>
<div class="code-block">
<pre><code>// Variables : camelCase ou snake_case
int nombreEtudiants;  // camelCase
int nombre_etudiants;  // snake_case

// Constantes : MAJUSCULES
const int MAX_SIZE = 100;

// Fonctions : verbes d'action
void calculerMoyenne();
bool estPair(int n);

// Noms explicites (pas de x, y, z sauf cas mathematiques)
int age;  // Bien
int a;    // A eviter (sauf contexte clair)</code></pre>
</div>

<p><strong>Indentation et lisibilite :</strong></p>
<div class="code-block">
<pre><code>// Mauvais
if(a&gt;b){cout&lt;&lt;a;}else{cout&lt;&lt;b;}

// Bon
if (a &gt; b) {
    cout &lt;&lt; a &lt;&lt; endl;
} else {
    cout &lt;&lt; b &lt;&lt; endl;
}</code></pre>
</div>

<p><strong>Commentaires :</strong></p>
<div class="code-block">
<pre><code>// Commentaire ligne simple

/*
 * Commentaire
 * multi-lignes
 */

/**
 * Documentation fonction (style Doxygen)
 * @param rayon : rayon du cercle
 * @return surface du cercle
 */
double surfaceCercle(double rayon) {
    return 3.14159 * rayon * rayon;
}</code></pre>
</div>

<h4>Gestion des erreurs</h4>

<p><strong>Validation des entrees :</strong></p>
<div class="code-block">
<pre><code>int age;
cout &lt;&lt; "Entrez votre age : ";
cin &gt;&gt; age;

if (cin.fail()) {
    cout &lt;&lt; "Erreur : entree invalide" &lt;&lt; endl;
    cin.clear();  // Reinitialiser le flux
    cin.ignore(1000, '\n');  // Vider le buffer
}

if (age &lt; 0 || age &gt; 150) {
    cout &lt;&lt; "Erreur : age non valide" &lt;&lt; endl;
}</code></pre>
</div>

<p><strong>Tests et assertions :</strong></p>
<div class="code-block">
<pre><code>#include &lt;cassert&gt;

assert(diviseur != 0);  // Arrete le programme si faux (mode debug)</code></pre>
</div>

<hr/>

<h2>PART D: ANALYSE ET REFLEXION</h2>

<h3>Evaluation des competences</h3>

<h4>Modalites d'evaluation</h4>

<p><strong>Controle continu (40%) :</strong></p>
<ul>
<li>QCM theoriques (2 dans le semestre) - 10%</li>
<li>Tests pratiques sur machine (2x1h) - 30%</li>
</ul>

<p><strong>Travaux pratiques (30%) :</strong></p>
<ul>
<li>8 TP notes</li>
<li>Evaluation : code fonctionnel, methodologie, documentation</li>
<li>Presence obligatoire</li>
</ul>

<p><strong>Projet semaine intensive (20%) :</strong></p>
<ul>
<li>Code source commente</li>
<li>Fonctionnalites implementees</li>
<li>Presentation et demo</li>
<li>Rapport technique</li>
</ul>

<p><strong>Examen terminal (10%) :</strong></p>
<ul>
<li>Epreuve theorique (1h)</li>
<li>Questions de cours, analyse de code, algorithmique</li>
</ul>

<h4>Grille d'evaluation TP (exemple)</h4>

<table>
<thead>
<tr><th>Critere</th><th>Detail</th><th>Points</th></tr>
</thead>
<tbody>
<tr><td><strong>Fonctionnalites</strong></td><td>Programme compile et s'execute</td><td>/4</td></tr>
<tr><td><strong>Correction</strong></td><td>Resultats conformes aux attendus</td><td>/6</td></tr>
<tr><td><strong>Algorithmique</strong></td><td>Logique et efficacite de l'algorithme</td><td>/4</td></tr>
<tr><td><strong>Style</strong></td><td>Lisibilite, nommage, commentaires</td><td>/3</td></tr>
<tr><td><strong>Tests</strong></td><td>Cas limites testes</td><td>/2</td></tr>
<tr><td><strong>Documentation</strong></td><td>Explications claires</td><td>/1</td></tr>
<tr><td><strong>Total</strong></td><td></td><td><strong>/20</strong></td></tr>
</tbody>
</table>

<h3>Competences acquises</h3>

<h4>Savoirs theoriques</h4>
<ul>
<li>Comprendre les concepts de la programmation structuree</li>
<li>Connaitre la syntaxe et les structures du langage C++</li>
<li>Maitriser l'algorithmique de base</li>
<li>Comprendre la notion de complexite algorithmique</li>
</ul>

<h4>Savoir-faire techniques</h4>
<ul>
<li>Ecrire, compiler et executer un programme C++</li>
<li>Utiliser un IDE et des outils de debogage</li>
<li>Concevoir des algorithmes structures</li>
<li>Manipuler tableaux, fonctions, structures</li>
<li>Deboguer et tester son code</li>
<li>Documenter son travail</li>
</ul>

<h4>Savoir-etre</h4>
<ul>
<li>Rigueur et methode dans la resolution de problemes</li>
<li>Autonomie dans l'apprentissage</li>
<li>Perseverance face aux bugs</li>
<li>Travail en equipe sur des projets</li>
<li>Curiosite et veille technologique</li>
</ul>

<h3>Progression et liens avec le cursus</h3>

<h4>Suite du parcours Programmation</h4>

<table>
<thead>
<tr><th>Semestre</th><th>Module</th><th>Langage</th><th>Contenu</th></tr>
</thead>
<tbody>
<tr><td><strong>S1</strong></td><td>Programmation 1</td><td>C++</td><td>Bases, structures, fonctions</td></tr>
<tr><td><strong>S2</strong></td><td>Programmation 2</td><td>C/C++</td><td>Pointeurs avances, allocation dynamique, POO</td></tr>
<tr><td><strong>S3</strong></td><td>Informatique Embarquee</td><td>C</td><td>Programmation microcontroleurs (Arduino, STM32)</td></tr>
<tr><td><strong>S4</strong></td><td>Python / Outils logiciels</td><td>Python</td><td>Scripts, traitement donnees, automatisation</td></tr>
</tbody>
</table>

<h4>Liens avec les autres matieres</h4>

<table>
<thead>
<tr><th>Matiere</th><th>Utilisation de la programmation</th></tr>
</thead>
<tbody>
<tr><td><strong>Systemes Numeriques (SIN)</strong></td><td>Simulations VHDL, scripts de test</td></tr>
<tr><td><strong>Informatique Embarquee</strong></td><td>Programmation microcontroleurs en C</td></tr>
<tr><td><strong>Automatique</strong></td><td>Implementation regulateurs, simulations</td></tr>
<tr><td><strong>Traitement du Signal</strong></td><td>Algorithmes de filtrage numerique</td></tr>
<tr><td><strong>Mathematiques</strong></td><td>Calculs numeriques, resolution d'equations</td></tr>
<tr><td><strong>Projets</strong></td><td>Developpement logiciel des prototypes</td></tr>
</tbody>
</table>

<h3>Indicateurs de reussite</h3>

<h4>Statistiques</h4>
<p><strong>Taux de reussite :</strong> 90% (moyenne &ge; 10/20)<br/>
<strong>Moyenne generale :</strong> 13/20</p>

<p><strong>Profils d'etudiants :</strong></p>
<ul>
<li>Debutants complets : 60%</li>
<li>Ayant fait de la programmation au lycee (NSI, ISN) : 30%</li>
<li>Ayant programme en autonomie : 10%</li>
</ul>

<h4>Difficultes frequentes</h4>

<p><strong>Problemes courants :</strong></p>
<ul>
<li>Confusion entre = (affectation) et == (comparaison)</li>
<li>Oublier les accolades {} ou points-virgules ;</li>
<li>Boucles infinies (condition mal formulee)</li>
<li>Depassement d'indices de tableaux</li>
<li>Oubli du &amp; dans passage par reference</li>
<li>Confusion pointeurs/valeurs</li>
</ul>

<p><strong>Solutions et conseils :</strong></p>
<ul>
<li>Compiler frequemment (eviter d'accumuler les erreurs)</li>
<li>Utiliser le debogueur au lieu de cout partout</li>
<li>Dessiner les structures de donnees sur papier</li>
<li>Tester avec des cas simples d'abord</li>
<li>Commenter son code au fur et a mesure</li>
<li>Refaire les TP chez soi</li>
</ul>

<h3>Debouches et applications</h3>

<h4>Applications professionnelles</h4>

<p><strong>Metiers utilisant le C/C++ :</strong></p>
<ul>
<li>Developpeur embarque (IoT, automobile, aeronautique)</li>
<li>Programmeur de microcontroleurs</li>
<li>Developpeur systemes temps reel</li>
<li>Automaticien (interfaces, supervision)</li>
<li>Developpeur logiciel industriel</li>
</ul>

<p><strong>Industries :</strong></p>
<ul>
<li>Electronique grand public</li>
<li>Automobile (systemes embarques)</li>
<li>Aeronautique et spatial</li>
<li>Robotique</li>
<li>Automatisation industrielle</li>
<li>Telecommunications</li>
</ul>

<hr/>

<h2>Ressources complementaires</h2>

<h3>Ouvrages de reference</h3>

<p><strong>Pour debutants :</strong></p>
<ol>
<li><em>Programmer en langage C++</em> - Claude Delannoy (Eyrolles) - <strong>LE classique francais</strong></li>
<li><em>C++ pour les Nuls</em> - Stephen Randy Davis (First)</li>
<li><em>Apprendre la programmation</em> - Sebastien Rohaut (Eyrolles)</li>
</ol>

<p><strong>Pour approfondir :</strong></p>
<ul>
<li><em>The C++ Programming Language</em> - Bjarne Stroustrup (createur du C++)</li>
<li><em>Effective C++</em> - Scott Meyers (bonnes pratiques)</li>
</ul>

<h3>Sites web et tutoriels</h3>

<p><strong>Cours en ligne (gratuits) :</strong></p>
<ul>
<li><strong>OpenClassrooms</strong> : Cours C++ tres complet en francais</li>
<li><strong>Codecademy</strong> : Exercices interactifs</li>
<li><strong>SoloLearn</strong> : Application mobile ludique</li>
<li><strong>cplusplus.com</strong> : Documentation complete + tutoriels</li>
</ul>

<p><strong>References C++ :</strong></p>
<ul>
<li><strong>cppreference.com</strong> : Documentation officielle</li>
<li><strong>Stack Overflow</strong> : Forum Q&amp;A (chercher avant de poster)</li>
</ul>

<p><strong>Exercices en ligne :</strong></p>
<ul>
<li><strong>France-IOI</strong> : Exercices progressifs d'algorithmique</li>
<li><strong>CodinGame</strong> : Apprendre en jouant</li>
<li><strong>HackerRank</strong> / <strong>LeetCode</strong> : Defis algorithmiques</li>
<li><strong>Project Euler</strong> : Problemes mathematiques a resoudre par programmation</li>
</ul>

<h3>Outils en ligne</h3>

<p><strong>Compilateurs en ligne (pour tester rapidement) :</strong></p>
<ul>
<li><strong>OnlineGDB</strong> (onlinegdb.com) : IDE complet dans le navigateur</li>
<li><strong>Compiler Explorer</strong> (godbolt.org) : Voir le code assembleur genere</li>
<li><strong>Repl.it</strong> : Environnement collaboratif</li>
</ul>

<p><strong>Visualisation d'algorithmes :</strong></p>
<ul>
<li><strong>PythonTutor</strong> (pythontutor.com) : Visualiser l'execution pas a pas</li>
<li><strong>VisuAlgo</strong> : Animations d'algorithmes (tri, recherche, graphes)</li>
</ul>

<hr/>

<h2>Conseils methodologiques</h2>

<h3>Pour reussir en programmation</h3>

<p><strong>Pendant les cours/TD :</strong></p>
<ul>
<li>Taper le code soi-meme (ne pas juste regarder)</li>
<li>Experimenter : modifier le code pour voir ce qui se passe</li>
<li>Poser des questions immediatement</li>
<li>Noter les erreurs frequentes et comment les corriger</li>
</ul>

<p><strong>En TP :</strong></p>
<ul>
<li>Lire entierement le sujet avant de commencer</li>
<li>Decomposer le probleme en petites etapes</li>
<li>Tester chaque fonction individuellement</li>
<li>Compiler souvent (toutes les 5-10 lignes)</li>
<li>Demander de l'aide si bloque &gt;15 min</li>
</ul>

<p><strong>Travail personnel (3-4h/semaine recommandees) :</strong></p>
<ul>
<li>Refaire les exercices de TD sans regarder la correction</li>
<li>Creer ses propres petits programmes</li>
<li>Lire des codes d'autres personnes (GitHub, forums)</li>
<li>Participer a des defis (CodinGame, HackerRank)</li>
</ul>

<h3>Methodologie de resolution de problemes</h3>

<p><strong>Etapes systematiques :</strong></p>
<ol>
<li><strong>Comprendre</strong> : Lire et reformuler le probleme</li>
<li><strong>Decomposer</strong> : Identifier les sous-problemes</li>
<li><strong>Algorithme</strong> : Ecrire en pseudo-code ou organigramme</li>
<li><strong>Coder</strong> : Traduire en C++</li>
<li><strong>Tester</strong> : Cas normaux, limites, erreurs</li>
<li><strong>Deboguer</strong> : Si ca ne marche pas, identifier l'erreur</li>
<li><strong>Optimiser</strong> : Ameliorer si necessaire</li>
</ol>

<p><strong>Exemple : Calculer la moyenne d'un tableau</strong></p>
<div class="code-block">
<pre><code>1. Comprendre : Somme des elements / nombre d'elements
2. Decomposer :
   - Parcourir le tableau
   - Additionner les valeurs
   - Diviser par la taille
3. Pseudo-code :
   somme = 0
   POUR chaque element du tableau
       somme = somme + element
   moyenne = somme / taille
4. Coder en C++
5. Tester avec {10, 15, 20} -> moyenne = 15</code></pre>
</div>

<hr/>

<p><strong>Bienvenue dans le monde de la programmation !</strong></p>

<blockquote><p>"Everybody should learn to program a computer, because it teaches you how to think." - Steve Jobs</p></blockquote>

<p>N'ayez pas peur de faire des erreurs : les bugs font partie de l'apprentissage. Chaque erreur corrigee est une lecon apprise !</p>

<h2>Ressources complementaires</h2>
<ul>
<li>Documentation C++ standard</li>
<li>Exercices en ligne (France-IOI, CodinGame)</li>
<li>Livres de reference sur le C++</li>
</ul>

</div>

<div class="lang-en">

<h1>Programming - Semester 1</h1>

<h2>PART A - General Course Overview</h2>

<h3>Training context</h3>

<p>Programming is a fundamental skill for any technician or engineer in GEII (Electrical Engineering and Industrial Computing). It enables the control of embedded systems, task automation, data processing, and application development. This first programming module, taught in C++, lays the foundations of algorithmic thinking and structured programming -- essential skills for future projects and professional life.</p>

<h3>Position in the curriculum</h3>
<ul>
<li><strong>Semester</strong>: S1 (1st year DUT GEII)</li>
<li><strong>Course hours</strong>: 60h (20h lectures + 25h tutorials + 15h practical work)</li>
<li><strong>ECTS credits</strong>: 5</li>
<li><strong>Prerequisites</strong>: No prior programming experience required (beginners welcome)</li>
<li><strong>Continuation</strong>: Programming S2 (advanced C/C++), then S3-S4 (embedded, Python)</li>
</ul>

<h3>Target audience</h3>
<p>First-year DUT GEII students, beginners or with some programming knowledge. The course is designed for all profiles, with a progressive pedagogy enabling everyone to succeed.</p>

<hr/>

<h2>PART B: EXPERIENCE, CONTEXT AND FUNCTION</h2>

<h3>Learning objectives</h3>

<p><strong>Algorithmic skills:</strong></p>
<ul>
<li>Analyze a problem and break it down into steps</li>
<li>Design structured and efficient algorithms</li>
<li>Evaluate algorithm complexity</li>
<li>Debug and test code</li>
</ul>

<p><strong>C++ technical skills:</strong></p>
<ul>
<li>Master the basic syntax of C++</li>
<li>Use control structures (conditions, loops)</li>
<li>Handle arrays and character strings</li>
<li>Create and use functions</li>
<li>Understand and use pointers (introduction)</li>
</ul>

<p><strong>Methodological skills:</strong></p>
<ul>
<li>Use a development environment (IDE)</li>
<li>Compile and run a program</li>
<li>Debug with appropriate tools</li>
<li>Document code</li>
<li>Work in project mode</li>
</ul>

<h3>Detailed program</h3>

<h4>1. Introduction to programming (5h)</h4>

<p><strong>Fundamental concepts:</strong></p>
<ul>
<li>What is a program? An algorithm?</li>
<li>Programming languages (compiled vs interpreted)</li>
<li>Compilation process (source &rarr; compilation &rarr; executable)</li>
<li>Structure of a C++ program</li>
</ul>

<p><strong>First "Hello World" program:</strong></p>
<div class="code-block">
<pre><code>#include &lt;iostream&gt;
using namespace std;

int main() {
    cout &lt;&lt; "Hello, World!" &lt;&lt; endl;
    return 0;
}</code></pre>
</div>

<p><strong>Syntax elements:</strong></p>
<ul>
<li>Preprocessor directives (#include)</li>
<li>The main() function</li>
<li>Statements and semicolons</li>
<li>Input/output (cin, cout)</li>
<li>Comments (// and /* */)</li>
</ul>

<h4>2. Variables and data types (8h)</h4>

<p><strong>Basic (primitive) types:</strong></p>
<div class="code-block">
<pre><code>int age = 20;              // Signed integer (4 bytes)
unsigned int count = 100;  // Unsigned integer
float temperature = 25.5;  // Single precision float
double pi = 3.14159265359; // Double precision float
char letter = 'A';         // Character (1 byte)
bool isValid = true;       // Boolean (true/false)</code></pre>
</div>

<p><strong>Declaration and initialization:</strong></p>
<ul>
<li>Declaration: <code>int x;</code></li>
<li>Initialization: <code>int x = 10;</code></li>
<li>Assignment: <code>x = 20;</code></li>
<li>Constants: <code>const double PI = 3.14159;</code></li>
</ul>

<p><strong>Operators:</strong></p>
<ul>
<li><strong>Arithmetic</strong>: +, -, *, /, % (modulo)</li>
<li><strong>Comparison</strong>: ==, !=, &lt;, &gt;, &lt;=, &gt;=</li>
<li><strong>Logical</strong>: &amp;&amp; (AND), || (OR), ! (NOT)</li>
<li><strong>Increment</strong>: ++, --</li>
<li><strong>Compound assignment</strong>: +=, -=, *=, /=</li>
</ul>

<p><strong>Type conversions (cast):</strong></p>
<div class="code-block">
<pre><code>int a = 10;
float b = 3.7;
int result = a + (int)b;  // Explicit cast
float average = (float)a / 3;  // Floating-point division</code></pre>
</div>

<p><strong>User input/output:</strong></p>
<div class="code-block">
<pre><code>int age;
cout &lt;&lt; "Enter your age: ";
cin &gt;&gt; age;
cout &lt;&lt; "You are " &lt;&lt; age &lt;&lt; " years old" &lt;&lt; endl;</code></pre>
</div>

<h4>3. Control structures (10h)</h4>

<p><strong>Conditional statements:</strong></p>

<p><strong>if / else if / else:</strong></p>
<div class="code-block">
<pre><code>if (temperature &gt; 30) {
    cout &lt;&lt; "It's hot" &lt;&lt; endl;
}
else if (temperature &gt; 20) {
    cout &lt;&lt; "It's nice" &lt;&lt; endl;
}
else {
    cout &lt;&lt; "It's cold" &lt;&lt; endl;
}</code></pre>
</div>

<p><strong>Ternary operator:</strong></p>
<div class="code-block">
<pre><code>int max = (a &gt; b) ? a : b;  // If a&gt;b then max=a else max=b</code></pre>
</div>

<p><strong>Switch / case:</strong></p>
<div class="code-block">
<pre><code>int choice;
cin &gt;&gt; choice;

switch (choice) {
    case 1:
        cout &lt;&lt; "Option 1" &lt;&lt; endl;
        break;
    case 2:
        cout &lt;&lt; "Option 2" &lt;&lt; endl;
        break;
    default:
        cout &lt;&lt; "Invalid option" &lt;&lt; endl;
}</code></pre>
</div>

<p><strong>Loops:</strong></p>

<p><strong>for loop (known number of iterations):</strong></p>
<div class="code-block">
<pre><code>// Display numbers from 1 to 10
for (int i = 1; i &lt;= 10; i++) {
    cout &lt;&lt; i &lt;&lt; " ";
}</code></pre>
</div>

<p><strong>while loop (entry condition):</strong></p>
<div class="code-block">
<pre><code>int i = 1;
while (i &lt;= 10) {
    cout &lt;&lt; i &lt;&lt; " ";
    i++;
}</code></pre>
</div>

<p><strong>do-while loop (exit condition, at least 1 iteration):</strong></p>
<div class="code-block">
<pre><code>int number;
do {
    cout &lt;&lt; "Enter a positive number: ";
    cin &gt;&gt; number;
} while (number &lt;= 0);</code></pre>
</div>

<p><strong>break and continue:</strong></p>
<div class="code-block">
<pre><code>for (int i = 0; i &lt; 10; i++) {
    if (i == 5) continue;  // Skip to next iteration
    if (i == 8) break;     // Exit the loop
    cout &lt;&lt; i &lt;&lt; " ";
}
// Prints: 0 1 2 3 4 6 7</code></pre>
</div>

<h4>4. Arrays and character strings (10h)</h4>

<p><strong>Static arrays:</strong></p>
<div class="code-block">
<pre><code>// Declaration and initialization
int grades[5] = {12, 15, 10, 18, 14};

// Accessing elements (index starts at 0)
cout &lt;&lt; "First grade: " &lt;&lt; grades[0] &lt;&lt; endl;
grades[2] = 16;  // Modification

// Traversal with loop
float sum = 0;
for (int i = 0; i &lt; 5; i++) {
    sum += grades[i];
}
float average = sum / 5;</code></pre>
</div>

<p><strong>Multidimensional arrays:</strong></p>
<div class="code-block">
<pre><code>int matrix[3][4] = {
    {1, 2, 3, 4},
    {5, 6, 7, 8},
    {9, 10, 11, 12}
};

// Traversal with nested loops
for (int i = 0; i &lt; 3; i++) {
    for (int j = 0; j &lt; 4; j++) {
        cout &lt;&lt; matrix[i][j] &lt;&lt; " ";
    }
    cout &lt;&lt; endl;
}</code></pre>
</div>

<p><strong>Character strings (C-style strings):</strong></p>
<div class="code-block">
<pre><code>char name[50];
cout &lt;&lt; "Enter your name: ";
cin &gt;&gt; name;

// Functions from &lt;cstring&gt;
#include &lt;cstring&gt;
strlen(name);       // Length
strcpy(dest, src);  // Copy
strcat(s1, s2);     // Concatenation
strcmp(s1, s2);      // Comparison (0 if equal)</code></pre>
</div>

<p><strong>C++ strings (std::string):</strong></p>
<div class="code-block">
<pre><code>#include &lt;string&gt;

string firstName = "Jean";
string lastName = "Dupont";
string fullName = firstName + " " + lastName;  // Concatenation

cout &lt;&lt; fullName.length() &lt;&lt; endl;  // Length
cout &lt;&lt; fullName[0] &lt;&lt; endl;        // First character
fullName += " Jr.";                  // Append</code></pre>
</div>

<h4>5. Functions (12h)</h4>

<p><strong>Declaration and definition:</strong></p>
<div class="code-block">
<pre><code>// Declaration (prototype)
int addition(int a, int b);

// Definition
int addition(int a, int b) {
    return a + b;
}

// Usage
int main() {
    int result = addition(5, 3);
    cout &lt;&lt; "5 + 3 = " &lt;&lt; result &lt;&lt; endl;
    return 0;
}</code></pre>
</div>

<p><strong>Parameter passing:</strong></p>

<p><strong>By value (copy):</strong></p>
<div class="code-block">
<pre><code>void increment(int x) {
    x++;  // Local modification, no effect on original
}

int main() {
    int a = 5;
    increment(a);
    cout &lt;&lt; a &lt;&lt; endl;  // Prints 5 (unchanged)
}</code></pre>
</div>

<p><strong>By reference (modifies original):</strong></p>
<div class="code-block">
<pre><code>void increment(int&amp; x) {  // Note the &amp;
    x++;  // Modifies the original
}

int main() {
    int a = 5;
    increment(a);
    cout &lt;&lt; a &lt;&lt; endl;  // Prints 6
}</code></pre>
</div>

<p><strong>Void functions (no return value):</strong></p>
<div class="code-block">
<pre><code>void displayMessage() {
    cout &lt;&lt; "Hello!" &lt;&lt; endl;
    // No return (or return; without value)
}</code></pre>
</div>

<p><strong>Function overloading:</strong></p>
<div class="code-block">
<pre><code>int addition(int a, int b) {
    return a + b;
}

double addition(double a, double b) {
    return a + b;
}

// The compiler chooses based on argument types</code></pre>
</div>

<p><strong>Default values:</strong></p>
<div class="code-block">
<pre><code>void display(string text, int repetitions = 1) {
    for (int i = 0; i &lt; repetitions; i++) {
        cout &lt;&lt; text &lt;&lt; endl;
    }
}

display("Hello");       // Uses default value of 1
display("Hello", 3);    // Prints 3 times</code></pre>
</div>

<h4>6. Structures (struct) (8h)</h4>

<p><strong>Definition and usage:</strong></p>
<div class="code-block">
<pre><code>struct Point {
    double x;
    double y;
};

int main() {
    Point p1;
    p1.x = 10.5;
    p1.y = 20.3;

    Point p2 = {5.0, 7.0};  // Initialization

    cout &lt;&lt; "Point 1: (" &lt;&lt; p1.x &lt;&lt; ", " &lt;&lt; p1.y &lt;&lt; ")" &lt;&lt; endl;
}</code></pre>
</div>

<p><strong>Nested structures:</strong></p>
<div class="code-block">
<pre><code>struct Address {
    string street;
    int zipCode;
    string city;
};

struct Person {
    string name;
    int age;
    Address address;
};

Person p;
p.name = "Dupont";
p.address.city = "Toulouse";</code></pre>
</div>

<p><strong>Arrays of structures:</strong></p>
<div class="code-block">
<pre><code>struct Student {
    string name;
    float average;
};

Student classroom[30];
classroom[0].name = "Alice";
classroom[0].average = 15.5;</code></pre>
</div>

<h4>7. Introduction to pointers (7h)</h4>

<p><strong>Pointer concept:</strong></p>
<div class="code-block">
<pre><code>int x = 10;
int* ptr = &amp;x;  // ptr holds the address of x

cout &lt;&lt; "Value of x: " &lt;&lt; x &lt;&lt; endl;
cout &lt;&lt; "Address of x: " &lt;&lt; &amp;x &lt;&lt; endl;
cout &lt;&lt; "Value of ptr: " &lt;&lt; ptr &lt;&lt; endl;
cout &lt;&lt; "Pointed value: " &lt;&lt; *ptr &lt;&lt; endl;  // Dereferencing</code></pre>
</div>

<p><strong>Modification via pointer:</strong></p>
<div class="code-block">
<pre><code>int a = 5;
int* p = &amp;a;
*p = 10;  // a is now 10</code></pre>
</div>

<p><strong>Pointers and arrays:</strong></p>
<div class="code-block">
<pre><code>int tab[5] = {10, 20, 30, 40, 50};
int* p = tab;  // Pointer to the first element

for (int i = 0; i &lt; 5; i++) {
    cout &lt;&lt; *(p + i) &lt;&lt; " ";  // Access via pointer arithmetic
}</code></pre>
</div>

<p><strong>Pointers and functions:</strong></p>
<div class="code-block">
<pre><code>void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int x = 5, y = 10;
    swap(&amp;x, &amp;y);
    cout &lt;&lt; "x = " &lt;&lt; x &lt;&lt; ", y = " &lt;&lt; y &lt;&lt; endl;  // x=10, y=5
}</code></pre>
</div>

<h3>Intensive programming week</h3>

<p><strong>Integrative project (40h over 1 week):</strong></p>

<p>Completion of a full project using all acquired skills:</p>
<ul>
<li>Problem analysis and decomposition</li>
<li>Algorithm design (flowchart or pseudo-code)</li>
<li>Implementation in C++</li>
<li>Testing and debugging</li>
<li>Documentation and presentation</li>
</ul>

<p><strong>Project examples:</strong></p>
<ol>
<li><strong>Hangman game</strong>: String handling, control structures</li>
<li><strong>Contact manager</strong>: Arrays of structures, files</li>
<li><strong>Scientific calculator</strong>: Mathematical functions, switch/case</li>
<li><strong>Game of Life (Conway)</strong>: 2D arrays, algorithms</li>
<li><strong>Grade manager</strong>: Statistical calculations, sorting</li>
</ol>

<p><strong>Organization:</strong></p>
<ul>
<li>Work in pairs</li>
<li>Daily follow-up by instructors</li>
<li>Final presentation (demo + code)</li>
<li>Technical report</li>
</ul>

<hr/>

<h2>PART C: TECHNICAL ASPECTS</h2>

<h3>Development environments (IDE)</h3>

<h4>Code::Blocks (recommended for beginners)</h4>

<p><strong>Installation:</strong></p>
<ul>
<li>Download from codeblocks.org</li>
<li>Version with MinGW (GCC compiler included)</li>
<li>Automatic configuration</li>
</ul>

<p><strong>Features:</strong></p>
<ul>
<li>Syntax highlighting</li>
<li>Auto-completion</li>
<li>One-click compilation (F9)</li>
<li>Integrated debugger</li>
<li>Project management</li>
</ul>

<p><strong>Creating a project:</strong></p>
<ol>
<li>File &rarr; New &rarr; Project &rarr; Console Application</li>
<li>Choose C++</li>
<li>Name the project and choose location</li>
<li>Code generated automatically</li>
</ol>

<h4>Visual Studio (Windows)</h4>

<p><strong>Advantages:</strong></p>
<ul>
<li>Powerful professional IDE</li>
<li>Excellent debugger</li>
<li>IntelliSense (advanced auto-completion)</li>
<li>Profiling tools</li>
</ul>

<p><strong>Creating a project:</strong></p>
<ul>
<li>File &rarr; New &rarr; Project &rarr; Empty Project (C++)</li>
<li>Add a .cpp file</li>
<li>Build &rarr; Build Solution (Ctrl+Shift+B)</li>
<li>Debug &rarr; Start Debugging (F5)</li>
</ul>

<h4>VS Code (cross-platform)</h4>

<p><strong>Configuration for C++:</strong></p>
<ol>
<li>Install VS Code</li>
<li>Install "C/C++" extension</li>
<li>Install MinGW (Windows) or GCC (Linux/Mac)</li>
<li>Configure tasks.json for compilation</li>
</ol>

<p><strong>Advantages:</strong></p>
<ul>
<li>Lightweight and fast</li>
<li>Highly customizable</li>
<li>Numerous extensions</li>
<li>Native Git integration</li>
</ul>

<h3>Compilation and debugging</h3>

<h4>Compilation process</h4>

<p><strong>Steps:</strong></p>
<div class="code-block">
<pre><code>Source code (.cpp) &rarr; Preprocessor &rarr; Compiler &rarr;
Assembler &rarr; Linker &rarr; Executable (.exe or binary)</code></pre>
</div>

<p><strong>Command-line compilation:</strong></p>
<div class="code-block">
<pre><code># Simple compilation
g++ program.cpp -o program

# With warnings and optimization
g++ -Wall -Wextra -O2 program.cpp -o program

# With debug information
g++ -g program.cpp -o program

# Execution
./program    # Linux/Mac
program.exe  # Windows</code></pre>
</div>

<h4>Debugging with GDB</h4>

<p><strong>Basic commands:</strong></p>
<div class="code-block">
<pre><code>gdb ./program

(gdb) break main       # Breakpoint on main
(gdb) run             # Run the program
(gdb) next            # Next line (without entering functions)
(gdb) step            # Next line (entering functions)
(gdb) print variable  # Display variable value
(gdb) continue        # Continue to next breakpoint
(gdb) quit            # Quit GDB</code></pre>
</div>

<p><strong>Debugging in IDE:</strong></p>
<ul>
<li>Place breakpoints (click left margin)</li>
<li>F5: Launch in debug mode</li>
<li>F10: Step over to next line</li>
<li>F11: Step into a function</li>
<li>Inspect variables in the "Watch" window</li>
</ul>

<h3>Programming best practices</h3>

<h4>Style and conventions</h4>

<p><strong>Naming:</strong></p>
<div class="code-block">
<pre><code>// Variables: camelCase or snake_case
int studentCount;      // camelCase
int student_count;     // snake_case

// Constants: UPPERCASE
const int MAX_SIZE = 100;

// Functions: action verbs
void calculateAverage();
bool isEven(int n);

// Explicit names (avoid x, y, z except for mathematical context)
int age;  // Good
int a;    // Avoid (unless context is clear)</code></pre>
</div>

<p><strong>Indentation and readability:</strong></p>
<div class="code-block">
<pre><code>// Bad
if(a&gt;b){cout&lt;&lt;a;}else{cout&lt;&lt;b;}

// Good
if (a &gt; b) {
    cout &lt;&lt; a &lt;&lt; endl;
} else {
    cout &lt;&lt; b &lt;&lt; endl;
}</code></pre>
</div>

<p><strong>Comments:</strong></p>
<div class="code-block">
<pre><code>// Single-line comment

/*
 * Multi-line
 * comment
 */

/**
 * Function documentation (Doxygen style)
 * @param radius: radius of the circle
 * @return area of the circle
 */
double circleArea(double radius) {
    return 3.14159 * radius * radius;
}</code></pre>
</div>

<h4>Error handling</h4>

<p><strong>Input validation:</strong></p>
<div class="code-block">
<pre><code>int age;
cout &lt;&lt; "Enter your age: ";
cin &gt;&gt; age;

if (cin.fail()) {
    cout &lt;&lt; "Error: invalid input" &lt;&lt; endl;
    cin.clear();  // Reset the stream
    cin.ignore(1000, '\n');  // Clear the buffer
}

if (age &lt; 0 || age &gt; 150) {
    cout &lt;&lt; "Error: invalid age" &lt;&lt; endl;
}</code></pre>
</div>

<p><strong>Tests and assertions:</strong></p>
<div class="code-block">
<pre><code>#include &lt;cassert&gt;

assert(divisor != 0);  // Stops the program if false (debug mode)</code></pre>
</div>

<hr/>

<h2>PART D: ANALYSIS AND REFLECTION</h2>

<h3>Skills assessment</h3>

<h4>Assessment methods</h4>

<p><strong>Continuous assessment (40%):</strong></p>
<ul>
<li>Theoretical quizzes (2 per semester) - 10%</li>
<li>Practical computer tests (2x1h) - 30%</li>
</ul>

<p><strong>Practical work (30%):</strong></p>
<ul>
<li>8 graded lab sessions</li>
<li>Evaluation: working code, methodology, documentation</li>
<li>Mandatory attendance</li>
</ul>

<p><strong>Intensive week project (20%):</strong></p>
<ul>
<li>Commented source code</li>
<li>Implemented features</li>
<li>Presentation and demo</li>
<li>Technical report</li>
</ul>

<p><strong>Final exam (10%):</strong></p>
<ul>
<li>Theoretical test (1h)</li>
<li>Course questions, code analysis, algorithms</li>
</ul>

<h4>Lab grading rubric (example)</h4>

<table>
<thead>
<tr><th>Criterion</th><th>Detail</th><th>Points</th></tr>
</thead>
<tbody>
<tr><td><strong>Features</strong></td><td>Program compiles and runs</td><td>/4</td></tr>
<tr><td><strong>Correctness</strong></td><td>Results match expectations</td><td>/6</td></tr>
<tr><td><strong>Algorithms</strong></td><td>Logic and efficiency of algorithm</td><td>/4</td></tr>
<tr><td><strong>Style</strong></td><td>Readability, naming, comments</td><td>/3</td></tr>
<tr><td><strong>Testing</strong></td><td>Edge cases tested</td><td>/2</td></tr>
<tr><td><strong>Documentation</strong></td><td>Clear explanations</td><td>/1</td></tr>
<tr><td><strong>Total</strong></td><td></td><td><strong>/20</strong></td></tr>
</tbody>
</table>

<h3>Skills acquired</h3>

<h4>Theoretical knowledge</h4>
<ul>
<li>Understand structured programming concepts</li>
<li>Know the syntax and structures of the C++ language</li>
<li>Master basic algorithms</li>
<li>Understand the notion of algorithmic complexity</li>
</ul>

<h4>Technical know-how</h4>
<ul>
<li>Write, compile and run a C++ program</li>
<li>Use an IDE and debugging tools</li>
<li>Design structured algorithms</li>
<li>Handle arrays, functions, structures</li>
<li>Debug and test code</li>
<li>Document work</li>
</ul>

<h4>Soft skills</h4>
<ul>
<li>Rigor and method in problem solving</li>
<li>Self-directed learning</li>
<li>Perseverance when facing bugs</li>
<li>Teamwork on projects</li>
<li>Curiosity and technology watch</li>
</ul>

<h3>Progression and links with the curriculum</h3>

<h4>Programming pathway</h4>

<table>
<thead>
<tr><th>Semester</th><th>Module</th><th>Language</th><th>Content</th></tr>
</thead>
<tbody>
<tr><td><strong>S1</strong></td><td>Programming 1</td><td>C++</td><td>Basics, structures, functions</td></tr>
<tr><td><strong>S2</strong></td><td>Programming 2</td><td>C/C++</td><td>Advanced pointers, dynamic allocation, OOP</td></tr>
<tr><td><strong>S3</strong></td><td>Embedded Computing</td><td>C</td><td>Microcontroller programming (Arduino, STM32)</td></tr>
<tr><td><strong>S4</strong></td><td>Python / Software Tools</td><td>Python</td><td>Scripts, data processing, automation</td></tr>
</tbody>
</table>

<h4>Links with other subjects</h4>

<table>
<thead>
<tr><th>Subject</th><th>Use of programming</th></tr>
</thead>
<tbody>
<tr><td><strong>Digital Systems (SIN)</strong></td><td>VHDL simulations, test scripts</td></tr>
<tr><td><strong>Embedded Computing</strong></td><td>Microcontroller programming in C</td></tr>
<tr><td><strong>Control Systems</strong></td><td>Controller implementation, simulations</td></tr>
<tr><td><strong>Signal Processing</strong></td><td>Digital filtering algorithms</td></tr>
<tr><td><strong>Mathematics</strong></td><td>Numerical calculations, equation solving</td></tr>
<tr><td><strong>Projects</strong></td><td>Prototype software development</td></tr>
</tbody>
</table>

<h3>Success indicators</h3>

<h4>Statistics</h4>
<p><strong>Pass rate:</strong> 90% (average &ge; 10/20)<br/>
<strong>Overall average:</strong> 13/20</p>

<p><strong>Student profiles:</strong></p>
<ul>
<li>Complete beginners: 60%</li>
<li>With high school programming experience (NSI, ISN): 30%</li>
<li>Self-taught programmers: 10%</li>
</ul>

<h4>Common difficulties</h4>

<p><strong>Frequent issues:</strong></p>
<ul>
<li>Confusion between = (assignment) and == (comparison)</li>
<li>Forgetting braces {} or semicolons ;</li>
<li>Infinite loops (poorly formulated condition)</li>
<li>Array index out of bounds</li>
<li>Forgetting the &amp; in pass by reference</li>
<li>Pointer/value confusion</li>
</ul>

<p><strong>Solutions and tips:</strong></p>
<ul>
<li>Compile frequently (avoid accumulating errors)</li>
<li>Use the debugger instead of cout everywhere</li>
<li>Draw data structures on paper</li>
<li>Test with simple cases first</li>
<li>Comment code as you go</li>
<li>Redo lab exercises at home</li>
</ul>

<h3>Career opportunities and applications</h3>

<h4>Professional applications</h4>

<p><strong>Careers using C/C++:</strong></p>
<ul>
<li>Embedded developer (IoT, automotive, aerospace)</li>
<li>Microcontroller programmer</li>
<li>Real-time systems developer</li>
<li>Automation engineer (interfaces, supervision)</li>
<li>Industrial software developer</li>
</ul>

<p><strong>Industries:</strong></p>
<ul>
<li>Consumer electronics</li>
<li>Automotive (embedded systems)</li>
<li>Aerospace and space</li>
<li>Robotics</li>
<li>Industrial automation</li>
<li>Telecommunications</li>
</ul>

<hr/>

<h2>Additional resources</h2>

<h3>Reference books</h3>

<p><strong>For beginners:</strong></p>
<ol>
<li><em>Programmer en langage C++</em> - Claude Delannoy (Eyrolles) - <strong>THE French classic</strong></li>
<li><em>C++ for Dummies</em> - Stephen Randy Davis (First)</li>
<li><em>Apprendre la programmation</em> - Sebastien Rohaut (Eyrolles)</li>
</ol>

<p><strong>For deeper study:</strong></p>
<ul>
<li><em>The C++ Programming Language</em> - Bjarne Stroustrup (creator of C++)</li>
<li><em>Effective C++</em> - Scott Meyers (best practices)</li>
</ul>

<h3>Websites and tutorials</h3>

<p><strong>Online courses (free):</strong></p>
<ul>
<li><strong>OpenClassrooms</strong>: Comprehensive C++ course in French</li>
<li><strong>Codecademy</strong>: Interactive exercises</li>
<li><strong>SoloLearn</strong>: Fun mobile application</li>
<li><strong>cplusplus.com</strong>: Complete documentation + tutorials</li>
</ul>

<p><strong>C++ references:</strong></p>
<ul>
<li><strong>cppreference.com</strong>: Official documentation</li>
<li><strong>Stack Overflow</strong>: Q&amp;A forum (search before posting)</li>
</ul>

<p><strong>Online exercises:</strong></p>
<ul>
<li><strong>France-IOI</strong>: Progressive algorithm exercises</li>
<li><strong>CodinGame</strong>: Learn by playing</li>
<li><strong>HackerRank</strong> / <strong>LeetCode</strong>: Algorithm challenges</li>
<li><strong>Project Euler</strong>: Mathematical problems to solve through programming</li>
</ul>

<h3>Online tools</h3>

<p><strong>Online compilers (for quick testing):</strong></p>
<ul>
<li><strong>OnlineGDB</strong> (onlinegdb.com): Full IDE in the browser</li>
<li><strong>Compiler Explorer</strong> (godbolt.org): View generated assembly code</li>
<li><strong>Repl.it</strong>: Collaborative environment</li>
</ul>

<p><strong>Algorithm visualization:</strong></p>
<ul>
<li><strong>PythonTutor</strong> (pythontutor.com): Visualize step-by-step execution</li>
<li><strong>VisuAlgo</strong>: Algorithm animations (sorting, searching, graphs)</li>
</ul>

<hr/>

<h2>Methodological tips</h2>

<h3>How to succeed in programming</h3>

<p><strong>During lectures/tutorials:</strong></p>
<ul>
<li>Type the code yourself (don't just watch)</li>
<li>Experiment: modify the code to see what happens</li>
<li>Ask questions immediately</li>
<li>Note frequent errors and how to fix them</li>
</ul>

<p><strong>During lab sessions:</strong></p>
<ul>
<li>Read the entire assignment before starting</li>
<li>Break the problem into small steps</li>
<li>Test each function individually</li>
<li>Compile often (every 5-10 lines)</li>
<li>Ask for help if stuck for &gt;15 min</li>
</ul>

<p><strong>Personal work (3-4h/week recommended):</strong></p>
<ul>
<li>Redo tutorial exercises without looking at the solution</li>
<li>Create your own small programs</li>
<li>Read other people's code (GitHub, forums)</li>
<li>Participate in challenges (CodinGame, HackerRank)</li>
</ul>

<h3>Problem-solving methodology</h3>

<p><strong>Systematic steps:</strong></p>
<ol>
<li><strong>Understand</strong>: Read and rephrase the problem</li>
<li><strong>Decompose</strong>: Identify sub-problems</li>
<li><strong>Algorithm</strong>: Write in pseudo-code or flowchart</li>
<li><strong>Code</strong>: Translate to C++</li>
<li><strong>Test</strong>: Normal cases, edge cases, errors</li>
<li><strong>Debug</strong>: If it doesn't work, identify the error</li>
<li><strong>Optimize</strong>: Improve if necessary</li>
</ol>

<p><strong>Example: Calculate the average of an array</strong></p>
<div class="code-block">
<pre><code>1. Understand: Sum of elements / number of elements
2. Decompose:
   - Traverse the array
   - Add the values
   - Divide by the size
3. Pseudo-code:
   sum = 0
   FOR each element of the array
       sum = sum + element
   average = sum / size
4. Code in C++
5. Test with {10, 15, 20} -> average = 15</code></pre>
</div>

<hr/>

<p><strong>Welcome to the world of programming!</strong></p>

<blockquote><p>"Everybody should learn to program a computer, because it teaches you how to think." - Steve Jobs</p></blockquote>

<p>Don't be afraid of making mistakes: bugs are part of learning. Every fixed error is a lesson learned!</p>

<h2>Additional resources</h2>
<ul>
<li>Standard C++ documentation</li>
<li>Online exercises (France-IOI, CodinGame)</li>
<li>C++ reference books</li>
</ul>

</div>

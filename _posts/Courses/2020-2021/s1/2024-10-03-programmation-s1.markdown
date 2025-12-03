---
layout: default
title: "Programmation - S1"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
---

# Programmation - Semestre 1

## PART A - Présentation Générale du Cours

### Contexte de la formation
La programmation est une compétence fondamentale pour tout technicien ou ingénieur en GEII. Elle permet de contrôler des systèmes embarqués, automatiser des tâches, traiter des données et développer des applications. Ce premier module de programmation, dispensé en C++, pose les bases de la pensée algorithmique et de la programmation structurée, compétences essentielles pour les projets futurs et la vie professionnelle.

### Positionnement dans le cursus
- **Semestre** : S1 (1ère année DUT GEII)
- **Volume horaire** : 60h (20h CM + 25h TD + 15h TP)
- **Crédits ECTS** : 5
- **Prérequis** : Aucun prérequis en programmation (débutants acceptés)
- **Continuité** : Programmation S2 (C/C++ avancé), puis S3-S4 (embarqué, Python)

### Public visé
Étudiants de première année DUT GEII, débutants ou ayant quelques notions en programmation. Le cours s'adresse à tous les profils, avec une pédagogie progressive permettant à chacun de réussir.

---

## PART B: EXPÉRIENCE, CONTEXTE ET FONCTION

### Objectifs pédagogiques

**Compétences algorithmiques :**
- Analyser un problème et le décomposer en étapes
- Concevoir des algorithmes structurés et efficaces
- Évaluer la complexité d'un algorithme
- Déboguer et tester son code

**Compétences techniques C++ :**
- Maîtriser la syntaxe de base du C++
- Utiliser les structures de contrôle (conditions, boucles)
- Manipuler les tableaux et les chaînes de caractères
- Créer et utiliser des fonctions
- Comprendre et utiliser les pointeurs (introduction)

**Compétences méthodologiques :**
- Utiliser un environnement de développement (IDE)
- Compiler et exécuter un programme
- Déboguer avec des outils appropriés
- Documenter son code
- Travailler en mode projet

### Programme détaillé

#### 1. Introduction à la programmation (5h)

**Concepts fondamentaux :**
- Qu'est-ce qu'un programme ? Un algorithme ?
- Langages de programmation (compilés vs interprétés)
- Processus de compilation (source → compilation → exécutable)
- Structure d'un programme C++

**Premier programme "Hello World" :**
```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    return 0;
}
```

**Éléments de syntaxe :**
- Directives du préprocesseur (#include)
- Fonction main()
- Instructions et point-virgule
- Entrées/sorties (cin, cout)
- Commentaires (// et /* */)

#### 2. Variables et types de données (8h)

**Types de base (primitifs) :**
```cpp
int age = 20;              // Entier signé (4 octets)
unsigned int count = 100;  // Entier non signé
float temperature = 25.5;  // Flottant simple précision
double pi = 3.14159265359; // Flottant double précision
char letter = 'A';         // Caractère (1 octet)
bool isValid = true;       // Booléen (true/false)
```

**Déclaration et initialisation :**
- Déclaration : `int x;`
- Initialisation : `int x = 10;`
- Affectation : `x = 20;`
- Constantes : `const double PI = 3.14159;`

**Opérateurs :**
- **Arithmétiques** : +, -, *, /, % (modulo)
- **Comparaison** : ==, !=, <, >, <=, >=
- **Logiques** : && (AND), || (OR), ! (NOT)
- **Incrémentation** : ++, --
- **Affectation composée** : +=, -=, *=, /=

**Conversions de types (cast) :**
```cpp
int a = 10;
float b = 3.7;
int result = a + (int)b;  // Cast explicite
float average = (float)a / 3;  // Division flottante
```

**Entrées/sorties utilisateur :**
```cpp
int age;
cout << "Entrez votre âge : ";
cin >> age;
cout << "Vous avez " << age << " ans" << endl;
```

#### 3. Structures de contrôle (10h)

**Instructions conditionnelles :**

**if / else if / else :**
```cpp
if (temperature > 30) {
    cout << "Il fait chaud" << endl;
}
else if (temperature > 20) {
    cout << "Il fait bon" << endl;
}
else {
    cout << "Il fait froid" << endl;
}
```

**Opérateur ternaire :**
```cpp
int max = (a > b) ? a : b;  // Si a>b alors max=a sinon max=b
```

**Switch / case :**
```cpp
int choice;
cin >> choice;

switch (choice) {
    case 1:
        cout << "Option 1" << endl;
        break;
    case 2:
        cout << "Option 2" << endl;
        break;
    default:
        cout << "Option invalide" << endl;
}
```

**Boucles :**

**Boucle for (nombre d'itérations connu) :**
```cpp
// Afficher les nombres de 1 à 10
for (int i = 1; i <= 10; i++) {
    cout << i << " ";
}
```

**Boucle while (condition en entrée) :**
```cpp
int i = 1;
while (i <= 10) {
    cout << i << " ";
    i++;
}
```

**Boucle do-while (condition en sortie, au moins 1 itération) :**
```cpp
int number;
do {
    cout << "Entrez un nombre positif : ";
    cin >> number;
} while (number <= 0);
```

**break et continue :**
```cpp
for (int i = 0; i < 10; i++) {
    if (i == 5) continue;  // Passer à l'itération suivante
    if (i == 8) break;     // Sortir de la boucle
    cout << i << " ";
}
// Affiche : 0 1 2 3 4 6 7
```

#### 4. Tableaux et chaînes de caractères (10h)

**Tableaux statiques (arrays) :**
```cpp
// Déclaration et initialisation
int notes[5] = {12, 15, 10, 18, 14};

// Accès aux éléments (index commence à 0)
cout << "Première note : " << notes[0] << endl;
notes[2] = 16;  // Modification

// Parcours avec boucle
float somme = 0;
for (int i = 0; i < 5; i++) {
    somme += notes[i];
}
float moyenne = somme / 5;
```

**Tableaux multidimensionnels :**
```cpp
int matrice[3][4] = {
    {1, 2, 3, 4},
    {5, 6, 7, 8},
    {9, 10, 11, 12}
};

// Parcours avec boucles imbriquées
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 4; j++) {
        cout << matrice[i][j] << " ";
    }
    cout << endl;
}
```

**Chaînes de caractères (C-style strings) :**
```cpp
char nom[50];
cout << "Entrez votre nom : ";
cin >> nom;

// Fonctions de <cstring>
#include <cstring>
strlen(nom);        // Longueur
strcpy(dest, src);  // Copie
strcat(s1, s2);     // Concaténation
strcmp(s1, s2);     // Comparaison (0 si égales)
```

**Chaînes C++ (std::string) :**
```cpp
#include <string>

string prenom = "Jean";
string nom = "Dupont";
string complet = prenom + " " + nom;  // Concaténation

cout << complet.length() << endl;  // Longueur
cout << complet[0] << endl;        // Premier caractère
complet += " Jr.";                 // Ajout à la fin
```

#### 5. Fonctions (12h)

**Déclaration et définition :**
```cpp
// Déclaration (prototype)
int addition(int a, int b);

// Définition
int addition(int a, int b) {
    return a + b;
}

// Utilisation
int main() {
    int resultat = addition(5, 3);
    cout << "5 + 3 = " << resultat << endl;
    return 0;
}
```

**Passage de paramètres :**

**Par valeur (copie) :**
```cpp
void incrementer(int x) {
    x++;  // Modification locale, pas d'effet sur l'original
}

int main() {
    int a = 5;
    incrementer(a);
    cout << a << endl;  // Affiche 5 (inchangé)
}
```

**Par référence (modification de l'original) :**
```cpp
void incrementer(int& x) {  // Notez le &
    x++;  // Modifie l'original
}

int main() {
    int a = 5;
    incrementer(a);
    cout << a << endl;  // Affiche 6
}
```

**Fonctions void (sans retour) :**
```cpp
void afficherMessage() {
    cout << "Bonjour !" << endl;
    // Pas de return (ou return; sans valeur)
}
```

**Surcharge de fonctions (overloading) :**
```cpp
int addition(int a, int b) {
    return a + b;
}

double addition(double a, double b) {
    return a + b;
}

// Le compilateur choisit selon les types des arguments
```

**Valeurs par défaut :**
```cpp
void afficher(string texte, int repetitions = 1) {
    for (int i = 0; i < repetitions; i++) {
        cout << texte << endl;
    }
}

afficher("Bonjour");      // Utilise 1 par défaut
afficher("Bonjour", 3);   // Affiche 3 fois
```

#### 6. Structures (struct) (8h)

**Définition et utilisation :**
```cpp
struct Point {
    double x;
    double y;
};

int main() {
    Point p1;
    p1.x = 10.5;
    p1.y = 20.3;
    
    Point p2 = {5.0, 7.0};  // Initialisation
    
    cout << "Point 1 : (" << p1.x << ", " << p1.y << ")" << endl;
}
```

**Structures imbriquées :**
```cpp
struct Adresse {
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
p.adresse.ville = "Toulouse";
```

**Tableaux de structures :**
```cpp
struct Etudiant {
    string nom;
    float moyenne;
};

Etudiant classe[30];
classe[0].nom = "Alice";
classe[0].moyenne = 15.5;
```

#### 7. Introduction aux pointeurs (7h)

**Concept de pointeur :**
```cpp
int x = 10;
int* ptr = &x;  // ptr contient l'adresse de x

cout << "Valeur de x : " << x << endl;
cout << "Adresse de x : " << &x << endl;
cout << "Valeur de ptr : " << ptr << endl;
cout << "Valeur pointée : " << *ptr << endl;  // Déréférencement
```

**Modification via pointeur :**
```cpp
int a = 5;
int* p = &a;
*p = 10;  // a vaut maintenant 10
```

**Pointeurs et tableaux :**
```cpp
int tab[5] = {10, 20, 30, 40, 50};
int* p = tab;  // Pointeur sur le premier élément

for (int i = 0; i < 5; i++) {
    cout << *(p + i) << " ";  // Accès par arithmétique de pointeurs
}
```

**Pointeurs et fonctions :**
```cpp
void echanger(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int x = 5, y = 10;
    echanger(&x, &y);
    cout << "x = " << x << ", y = " << y << endl;  // x=10, y=5
}
```

### Semaine intensive de programmation

**Projet intégratif (40h sur 1 semaine) :**

Réalisation d'un projet complet mobilisant toutes les compétences :
- Analyse et décomposition du problème
- Conception de l'algorithme (organigramme ou pseudo-code)
- Implémentation en C++
- Tests et débogage
- Documentation et présentation

**Exemples de projets :**
1. **Jeu du pendu** : Gestion de chaînes, structures de contrôle
2. **Gestion de contacts** : Tableaux de structures, fichiers
3. **Calculatrice scientifique** : Fonctions mathématiques, switch/case
4. **Jeu de la vie (Conway)** : Tableaux 2D, algorithmique
5. **Gestionnaire de notes** : Calculs statistiques, tri

**Organisation :**
- Travail en binôme
- Suivi quotidien par les enseignants
- Présentation finale (démo + code)
- Rapport technique

---

## PART C: ASPECTS TECHNIQUES

### Environnements de développement (IDE)

#### Code::Blocks (recommandé pour débutants)

**Installation :**
- Télécharger sur codeblocks.org
- Version avec MinGW (compilateur GCC inclus)
- Configuration automatique

**Fonctionnalités :**
- Coloration syntaxique
- Auto-complétion
- Compilation en un clic (F9)
- Débogueur intégré
- Gestion de projets

**Création d'un projet :**
1. File → New → Project → Console Application
2. Choisir C++
3. Nommer le projet et choisir l'emplacement
4. Code généré automatiquement

#### Visual Studio (Windows)

**Avantages :**
- IDE professionnel puissant
- Excellent débogueur
- IntelliSense (auto-complétion avancée)
- Outils de profilage

**Création d'un projet :**
- File → New → Project → Empty Project (C++)
- Ajouter un fichier .cpp
- Build → Build Solution (Ctrl+Shift+B)
- Debug → Start Debugging (F5)

#### VS Code (multiplateforme)

**Configuration pour C++ :**
1. Installer VS Code
2. Installer extension "C/C++"
3. Installer MinGW (Windows) ou GCC (Linux/Mac)
4. Configurer tasks.json pour compilation

**Avantages :**
- Léger et rapide
- Très personnalisable
- Extensions nombreuses
- Intégration Git native

### Compilation et débogage

#### Processus de compilation

**Étapes :**
```
Code source (.cpp) → Préprocesseur → Compilateur → 
Assembleur → Linker → Exécutable (.exe ou binaire)
```

**Compilation en ligne de commande :**
```bash
# Compilation simple
g++ programme.cpp -o programme

# Avec warnings et optimisation
g++ -Wall -Wextra -O2 programme.cpp -o programme

# Avec informations de debug
g++ -g programme.cpp -o programme

# Exécution
./programme  # Linux/Mac
programme.exe  # Windows
```

#### Débogage avec GDB

**Commandes de base :**
```bash
gdb ./programme

(gdb) break main       # Point d'arrêt sur main
(gdb) run             # Lancer le programme
(gdb) next            # Ligne suivante (sans entrer dans fonctions)
(gdb) step            # Ligne suivante (en entrant dans fonctions)
(gdb) print variable  # Afficher valeur d'une variable
(gdb) continue        # Continuer jusqu'au prochain breakpoint
(gdb) quit            # Quitter GDB
```

**Débogage dans IDE :**
- Placer des breakpoints (clic marge gauche)
- F5 : Lancer en mode debug
- F10 : Passer à la ligne suivante
- F11 : Entrer dans une fonction
- Inspecter les variables dans la fenêtre "Watch"

### Bonnes pratiques de programmation

#### Style et conventions

**Nommage :**
```cpp
// Variables : camelCase ou snake_case
int nombreEtudiants;  // camelCase
int nombre_etudiants;  // snake_case

// Constantes : MAJUSCULES
const int MAX_SIZE = 100;

// Fonctions : verbes d'action
void calculerMoyenne();
bool estPair(int n);

// Noms explicites (pas de x, y, z sauf cas mathématiques)
int age;  // Bien
int a;    // À éviter (sauf contexte clair)
```

**Indentation et lisibilité :**
```cpp
// Mauvais
if(a>b){cout<<a;}else{cout<<b;}

// Bon
if (a > b) {
    cout << a << endl;
} else {
    cout << b << endl;
}
```

**Commentaires :**
```cpp
// Commentaire ligne simple

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
}
```

#### Gestion des erreurs

**Validation des entrées :**
```cpp
int age;
cout << "Entrez votre âge : ";
cin >> age;

if (cin.fail()) {
    cout << "Erreur : entrée invalide" << endl;
    cin.clear();  // Réinitialiser le flux
    cin.ignore(1000, '\n');  // Vider le buffer
}

if (age < 0 || age > 150) {
    cout << "Erreur : âge non valide" << endl;
}
```

**Tests et assertions :**
```cpp
#include <cassert>

assert(diviseur != 0);  // Arrête le programme si faux (mode debug)
```

---

## PART D: ANALYSE ET RÉFLEXION

### Évaluation des compétences

#### Modalités d'évaluation

**Contrôle continu (40%) :**
- QCM théoriques (2 dans le semestre) - 10%
- Tests pratiques sur machine (2×1h) - 30%

**Travaux pratiques (30%) :**
- 8 TP notés
- Évaluation : code fonctionnel, méthodologie, documentation
- Présence obligatoire

**Projet semaine intensive (20%) :**
- Code source commenté
- Fonctionnalités implémentées
- Présentation et démo
- Rapport technique

**Examen terminal (10%) :**
- Épreuve théorique (1h)
- Questions de cours, analyse de code, algorithmique

#### Grille d'évaluation TP (exemple)

| Critère | Détail | Points |
|---------|--------|--------|
| **Fonctionnalités** | Programme compile et s'exécute | /4 |
| **Correction** | Résultats conformes aux attendus | /6 |
| **Algorithmique** | Logique et efficacité de l'algorithme | /4 |
| **Style** | Lisibilité, nommage, commentaires | /3 |
| **Tests** | Cas limites testés | /2 |
| **Documentation** | Explications claires | /1 |
| **Total** | | **/20** |

### Compétences acquises

#### Savoirs théoriques

✓ Comprendre les concepts de la programmation structurée
✓ Connaître la syntaxe et les structures du langage C++
✓ Maîtriser l'algorithmique de base
✓ Comprendre la notion de complexité algorithmique

#### Savoir-faire techniques

✓ Écrire, compiler et exécuter un programme C++
✓ Utiliser un IDE et des outils de débogage
✓ Concevoir des algorithmes structurés
✓ Manipuler tableaux, fonctions, structures
✓ Déboguer et tester son code
✓ Documenter son travail

#### Savoir-être

✓ Rigueur et méthode dans la résolution de problèmes
✓ Autonomie dans l'apprentissage
✓ Persévérance face aux bugs
✓ Travail en équipe sur des projets
✓ Curiosité et veille technologique

### Progression et liens avec le cursus

#### Suite du parcours Programmation

| Semestre | Module | Langage | Contenu |
|----------|--------|---------|---------|
| **S1** | Programmation 1 | C++ | Bases, structures, fonctions |
| **S2** | Programmation 2 | C/C++ | Pointeurs avancés, allocation dynamique, POO |
| **S3** | Informatique Embarquée | C | Programmation microcontrôleurs (Arduino, STM32) |
| **S4** | Python / Outils logiciels | Python | Scripts, traitement données, automatisation |

#### Liens avec les autres matières

| Matière | Utilisation de la programmation |
|---------|--------------------------------|
| **Systèmes Numériques (SIN)** | Simulations VHDL, scripts de test |
| **Informatique Embarquée** | Programmation microcontrôleurs en C |
| **Automatique** | Implémentation régulateurs, simulations |
| **Traitement du Signal** | Algorithmes de filtrage numérique |
| **Mathématiques** | Calculs numériques, résolution d'équations |
| **Projets** | Développement logiciel des prototypes |

### Indicateurs de réussite

#### Statistiques

**Taux de réussite :** 90% (moyenne ≥ 10/20)
**Moyenne générale :** 13/20

**Profils d'étudiants :**
- Débutants complets : 60%
- Ayant fait de la programmation au lycée (NSI, ISN) : 30%
- Ayant programmé en autonomie : 10%

#### Difficultés fréquentes

**Problèmes courants :**
❌ Confusion entre = (affectation) et == (comparaison)
❌ Oublier les accolades {} ou points-virgules ;
❌ Boucles infinies (condition mal formulée)
❌ Dépassement d'indices de tableaux
❌ Oubli du & dans passage par référence
❌ Confusion pointeurs/valeurs

**Solutions et conseils :**
✅ Compiler fréquemment (éviter d'accumuler les erreurs)
✅ Utiliser le débogueur au lieu de cout partout
✅ Dessiner les structures de données sur papier
✅ Tester avec des cas simples d'abord
✅ Commenter son code au fur et à mesure
✅ Refaire les TP chez soi

### Débouchés et applications

#### Applications professionnelles

**Métiers utilisant le C/C++ :**
- Développeur embarqué (IoT, automobile, aéronautique)
- Programmeur de microcontrôleurs
- Développeur systèmes temps réel
- Automaticien (interfaces, supervision)
- Développeur logiciel industriel

**Industries :**
- Électronique grand public
- Automobile (systèmes embarqués)
- Aéronautique et spatial
- Robotique
- Automatisation industrielle
- Télécommunications

---

## 📚 Ressources complémentaires

### Ouvrages de référence

**Pour débutants :**
1. *Programmer en langage C++* - Claude Delannoy (Eyrolles) - **LE classique français**
2. *C++ pour les Nuls* - Stephen Randy Davis (First)
3. *Apprendre la programmation* - Sébastien Rohaut (Eyrolles)

**Pour approfondir :**
- *The C++ Programming Language* - Bjarne Stroustrup (créateur du C++)
- *Effective C++* - Scott Meyers (bonnes pratiques)

### Sites web et tutoriels

**Cours en ligne (gratuits) :**
- **OpenClassrooms** : Cours C++ très complet en français
- **Codecademy** : Exercices interactifs
- **SoloLearn** : Application mobile ludique
- **cplusplus.com** : Documentation complète + tutoriels

**Références C++ :**
- **cppreference.com** : Documentation officielle
- **Stack Overflow** : Forum Q&A (chercher avant de poster)

**Exercices en ligne :**
- **France-IOI** : Exercices progressifs d'algorithmique
- **CodinGame** : Apprendre en jouant
- **HackerRank** / **LeetCode** : Défis algorithmiques
- **Project Euler** : Problèmes mathématiques à résoudre par programmation

### Outils en ligne

**Compilateurs en ligne (pour tester rapidement) :**
- **OnlineGDB** (onlinegdb.com) : IDE complet dans le navigateur
- **Compiler Explorer** (godbolt.org) : Voir le code assembleur généré
- **Repl.it** : Environnement collaboratif

**Visualisation d'algorithmes :**
- **PythonTutor** (pythontutor.com) : Visualiser l'exécution pas à pas
- **VisuAlgo** : Animations d'algorithmes (tri, recherche, graphes)

---

## 🎯 Conseils méthodologiques

### Pour réussir en programmation

**Pendant les cours/TD :**
- Taper le code soi-même (ne pas juste regarder)
- Expérimenter : modifier le code pour voir ce qui se passe
- Poser des questions immédiatement
- Noter les erreurs fréquentes et comment les corriger

**En TP :**
- Lire entièrement le sujet avant de commencer
- Décomposer le problème en petites étapes
- Tester chaque fonction individuellement
- Compiler souvent (toutes les 5-10 lignes)
- Demander de l'aide si bloqué >15 min

**Travail personnel (3-4h/semaine recommandées) :**
- Refaire les exercices de TD sans regarder la correction
- Créer ses propres petits programmes
- Lire des codes d'autres personnes (GitHub, forums)
- Participer à des défis (CodinGame, HackerRank)

### Méthodologie de résolution de problèmes

**Étapes systématiques :**

1. **Comprendre** : Lire et reformuler le problème
2. **Décomposer** : Identifier les sous-problèmes
3. **Algorithme** : Écrire en pseudo-code ou organigramme
4. **Coder** : Traduire en C++
5. **Tester** : Cas normaux, limites, erreurs
6. **Déboguer** : Si ça ne marche pas, identifier l'erreur
7. **Optimiser** : Améliorer si nécessaire

**Exemple : Calculer la moyenne d'un tableau**
```
1. Comprendre : Somme des éléments / nombre d'éléments
2. Décomposer : 
   - Parcourir le tableau
   - Additionner les valeurs
   - Diviser par la taille
3. Pseudo-code :
   somme = 0
   POUR chaque élément du tableau
       somme = somme + élément
   moyenne = somme / taille
4. Coder en C++
5. Tester avec {10, 15, 20} → moyenne = 15 ✓
```

---

**Bienvenue dans le monde de la programmation ! 💻🚀**

> "Everybody should learn to program a computer, because it teaches you how to think." - Steve Jobs

N'ayez pas peur de faire des erreurs : les bugs font partie de l'apprentissage. Chaque erreur corrigée est une leçon apprise !

## 📖 Ressources complémentaires

- Documentation C++ standard
- Exercices en ligne (France-IOI, CodinGame)
- Livres de référence sur le C++

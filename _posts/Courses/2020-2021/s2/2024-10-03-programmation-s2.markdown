---
layout: default
title: "Programmation - S2"
date: 2024-10-02 10:56:03 +0200
---

<style>
.back-nav { margin-bottom: 20px; }
.back-nav a { text-decoration: none; color: #2a7ae2; font-weight: 600; }
.back-nav a:hover { text-decoration: underline; }
.section-title { color: #2a7ae2; border-bottom: 2px solid #2a7ae2; padding-bottom: 10px; margin-top: 30px; margin-bottom: 20px; }
</style>

<div class="back-nav">
  <a href="./my-courses-2020-2021.html">← Retour a Mes Cours 2020-2021</a>
</div>

# Programmation - S2

**Annee**: 2020-2021 | **Semestre**: 2 | **Type**: Informatique

---

## PART A : PRESENTATION GENERALE

### Contexte et objectifs

Approfondissement de la programmation en C/C++ avec introduction aux concepts avances et aux structures de donnees complexes. Ce cours consolide les bases acquises au S1 et prepare aux applications plus elaborees, notamment le projet tuteure de programmation (simulation de fourmis fourrageuses).

**Objectifs pedagogiques :**
- Maitriser les structures de donnees avancees (listes chainees, piles, files, arbres)
- Comprendre la gestion dynamique de la memoire (allocation, pointeurs)
- Developper des algorithmes complexes (tri, recherche, recursivite)
- Utiliser les fichiers pour la persistance des donnees
- Structurer des programmes de grande taille (programmation modulaire)

### Organisation

Le cours alterne entre cours magistraux, travaux pratiques sur machine et un projet de programmation collaboratif (projet tuteure). L'evaluation porte sur les TP notes, les QCM et le projet de programmation.

### Competences visees (BUT GEII)

Ce module contribue directement au bloc de competences "Informatique et Programmation" du BUT GEII :
- Ecrire des programmes structuraux et modulaires en C/C++
- Implementer des structures de donnees adaptees au probleme
- Gerer la memoire de maniere efficace et sans fuites
- Travailler en equipe sur un projet logiciel de taille moyenne

---

## PART B : EXPERIENCE ET CONTEXTE

### Environnement pedagogique

L'enseignement de programmation S2 est realise sur les postes informatiques de l'IUT avec l'environnement Code::Blocks et le compilateur GCC/G++. Le projet tuteure constitue une part importante du semestre, avec un travail en binome sur un projet de simulation.

### Projet tuteure : Fourmis Fourrageuses (GIBERT_CHANFREAU_FOURMIS)

Le projet phare du semestre a ete la realisation d'une **simulation de fourmis fourrageuses** en C/C++ :
- Simulation en mode console avec une grille de 20 lignes par 40 colonnes
- Affichage avec couleurs dans la console Windows (utilisation de l'API Windows pour les couleurs)
- Modelisation du comportement de fourmis : recherche de nourriture, suivi de pheromones, retour au nid
- Utilisation de matrices de caracteres, de structures, et de machines a etats pour gerer le comportement des fourmis
- Travail en binome sur une semaine de projet intensif (du 11 au 18 janvier 2021)
- Utilisation de Code::Blocks comme IDE

### Architecture du projet

Le projet etait organise en plusieurs fichiers :
- `main.cpp` : Point d'entree, boucle de simulation principale
- Fonctions d'affichage : gestion de la grille console avec couleurs
- Fonctions de logique : comportement des fourmis, gestion des pheromones
- Structures de donnees : matrices d'ecran, tableaux de sauvegarde des fourmis

### Outils utilises

- **IDE** : Code::Blocks
- **Compilateur** : GCC/G++
- **Debogueur** : GDB, debugger integre Code::Blocks
- **API** : Windows Console API (SetConsoleTextAttribute pour les couleurs)
- **Gestion de versions** : Organisation en fichiers source et en-tete

### Liens avec d'autres cours

- **Programmation S1** : Consolidation des bases du C
- **Informatique Embarquee (IE)** : Programmation C pour microcontroleurs
- **CEC** : Projet tuteure de programmation (rapport et presentation)
- **Mathematiques** : Algorithmes numeriques

---

## PART C : ASPECTS TECHNIQUES

### 1. Gestion dynamique de la memoire

La gestion dynamique de la memoire est un concept fondamental en C/C++. Elle permet d'allouer de la memoire pendant l'execution du programme, offrant une flexibilite que les allocations statiques ne permettent pas.

#### Allocation dynamique en C avec malloc/free

```c
#include <stdio.h>
#include <stdlib.h>

// Allocation dynamique d'un tableau d'entiers
int* creerTableau(int taille) {
    int* tab = (int*)malloc(taille * sizeof(int));
    if (tab == NULL) {
        printf("Erreur d'allocation memoire\n");
        exit(EXIT_FAILURE);
    }
    // Initialisation a zero
    for (int i = 0; i < taille; i++) {
        tab[i] = 0;
    }
    return tab;
}

// Redimensionnement d'un tableau
int* redimensionnerTableau(int* tab, int nouvelleTaille) {
    int* nouveauTab = (int*)realloc(tab, nouvelleTaille * sizeof(int));
    if (nouveauTab == NULL) {
        printf("Erreur de reallocation\n");
        free(tab);
        exit(EXIT_FAILURE);
    }
    return nouveauTab;
}

// Allocation d'une matrice 2D
int** creerMatrice(int lignes, int colonnes) {
    int** matrice = (int**)malloc(lignes * sizeof(int*));
    if (matrice == NULL) {
        exit(EXIT_FAILURE);
    }
    for (int i = 0; i < lignes; i++) {
        matrice[i] = (int*)malloc(colonnes * sizeof(int));
        if (matrice[i] == NULL) {
            // Liberation de la memoire deja allouee
            for (int j = 0; j < i; j++) {
                free(matrice[j]);
            }
            free(matrice);
            exit(EXIT_FAILURE);
        }
    }
    return matrice;
}

// Liberation d'une matrice 2D
void libererMatrice(int** matrice, int lignes) {
    for (int i = 0; i < lignes; i++) {
        free(matrice[i]);
    }
    free(matrice);
}

int main() {
    // Utilisation d'un tableau dynamique
    int n = 10;
    int* tableau = creerTableau(n);
    for (int i = 0; i < n; i++) {
        tableau[i] = i * i;
    }
    // Redimensionnement
    tableau = redimensionnerTableau(tableau, 20);
    free(tableau);

    // Utilisation d'une matrice dynamique
    int** mat = creerMatrice(5, 5);
    mat[2][3] = 42;
    libererMatrice(mat, 5);

    return 0;
}
```

#### Allocation dynamique en C++ avec new/delete

```cpp
#include <iostream>
using namespace std;

// Allocation d'un tableau avec new
int* creerTableauCpp(int taille) {
    int* tab = new int[taille];
    for (int i = 0; i < taille; i++) {
        tab[i] = 0;
    }
    return tab;
}

// Allocation d'une matrice avec new
int** creerMatriceCpp(int lignes, int colonnes) {
    int** matrice = new int*[lignes];
    for (int i = 0; i < lignes; i++) {
        matrice[i] = new int[colonnes];
        for (int j = 0; j < colonnes; j++) {
            matrice[i][j] = 0;
        }
    }
    return matrice;
}

// Liberation avec delete
void libererMatriceCpp(int** matrice, int lignes) {
    for (int i = 0; i < lignes; i++) {
        delete[] matrice[i];
    }
    delete[] matrice;
}

int main() {
    int* tab = creerTableauCpp(10);
    delete[] tab;

    int** mat = creerMatriceCpp(3, 4);
    mat[1][2] = 99;
    libererMatriceCpp(mat, 3);

    return 0;
}
```

### 2. Listes chainees en C

Les listes chainees sont des structures de donnees fondamentales qui permettent une gestion flexible des collections d'elements, avec des insertions et suppressions en temps constant.

#### Implementation d'une liste simplement chainee

```c
#include <stdio.h>
#include <stdlib.h>

// Definition de la structure de noeud
typedef struct Noeud {
    int donnee;
    struct Noeud* suivant;
} Noeud;

// Definition de la liste
typedef struct {
    Noeud* tete;
    int taille;
} Liste;

// Initialisation de la liste
void initialiserListe(Liste* liste) {
    liste->tete = NULL;
    liste->taille = 0;
}

// Insertion en tete
void insererEnTete(Liste* liste, int valeur) {
    Noeud* nouveau = (Noeud*)malloc(sizeof(Noeud));
    if (nouveau == NULL) {
        printf("Erreur d'allocation\n");
        return;
    }
    nouveau->donnee = valeur;
    nouveau->suivant = liste->tete;
    liste->tete = nouveau;
    liste->taille++;
}

// Insertion en fin
void insererEnFin(Liste* liste, int valeur) {
    Noeud* nouveau = (Noeud*)malloc(sizeof(Noeud));
    if (nouveau == NULL) return;
    nouveau->donnee = valeur;
    nouveau->suivant = NULL;

    if (liste->tete == NULL) {
        liste->tete = nouveau;
    } else {
        Noeud* courant = liste->tete;
        while (courant->suivant != NULL) {
            courant = courant->suivant;
        }
        courant->suivant = nouveau;
    }
    liste->taille++;
}

// Insertion a une position donnee
void insererAPosition(Liste* liste, int valeur, int position) {
    if (position < 0 || position > liste->taille) {
        printf("Position invalide\n");
        return;
    }
    if (position == 0) {
        insererEnTete(liste, valeur);
        return;
    }
    Noeud* nouveau = (Noeud*)malloc(sizeof(Noeud));
    if (nouveau == NULL) return;
    nouveau->donnee = valeur;

    Noeud* courant = liste->tete;
    for (int i = 0; i < position - 1; i++) {
        courant = courant->suivant;
    }
    nouveau->suivant = courant->suivant;
    courant->suivant = nouveau;
    liste->taille++;
}

// Suppression en tete
int supprimerEnTete(Liste* liste) {
    if (liste->tete == NULL) {
        printf("Liste vide\n");
        return -1;
    }
    Noeud* temp = liste->tete;
    int valeur = temp->donnee;
    liste->tete = temp->suivant;
    free(temp);
    liste->taille--;
    return valeur;
}

// Recherche d'un element
Noeud* rechercher(Liste* liste, int valeur) {
    Noeud* courant = liste->tete;
    while (courant != NULL) {
        if (courant->donnee == valeur) {
            return courant;
        }
        courant = courant->suivant;
    }
    return NULL;
}

// Affichage de la liste
void afficherListe(Liste* liste) {
    Noeud* courant = liste->tete;
    printf("Liste [%d elements] : ", liste->taille);
    while (courant != NULL) {
        printf("%d -> ", courant->donnee);
        courant = courant->suivant;
    }
    printf("NULL\n");
}

// Liberation de toute la liste
void libererListe(Liste* liste) {
    Noeud* courant = liste->tete;
    while (courant != NULL) {
        Noeud* temp = courant;
        courant = courant->suivant;
        free(temp);
    }
    liste->tete = NULL;
    liste->taille = 0;
}

int main() {
    Liste maListe;
    initialiserListe(&maListe);

    insererEnFin(&maListe, 10);
    insererEnFin(&maListe, 20);
    insererEnFin(&maListe, 30);
    insererEnTete(&maListe, 5);
    insererAPosition(&maListe, 15, 2);

    afficherListe(&maListe);
    // Resultat : Liste [5 elements] : 5 -> 10 -> 15 -> 20 -> 30 -> NULL

    Noeud* trouve = rechercher(&maListe, 20);
    if (trouve) printf("Element 20 trouve\n");

    supprimerEnTete(&maListe);
    afficherListe(&maListe);

    libererListe(&maListe);
    return 0;
}
```

### 3. Arbres binaires de recherche

Les arbres binaires de recherche (ABR) sont des structures de donnees hierarchiques qui permettent des operations de recherche, insertion et suppression en O(log n) en moyenne.

#### Implementation d'un ABR avec parcours

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct NoeudArbre {
    int valeur;
    struct NoeudArbre* gauche;
    struct NoeudArbre* droite;
} NoeudArbre;

// Creation d'un nouveau noeud
NoeudArbre* creerNoeud(int valeur) {
    NoeudArbre* noeud = (NoeudArbre*)malloc(sizeof(NoeudArbre));
    if (noeud == NULL) {
        printf("Erreur d'allocation\n");
        exit(EXIT_FAILURE);
    }
    noeud->valeur = valeur;
    noeud->gauche = NULL;
    noeud->droite = NULL;
    return noeud;
}

// Insertion dans l'ABR
NoeudArbre* inserer(NoeudArbre* racine, int valeur) {
    if (racine == NULL) {
        return creerNoeud(valeur);
    }
    if (valeur < racine->valeur) {
        racine->gauche = inserer(racine->gauche, valeur);
    } else if (valeur > racine->valeur) {
        racine->droite = inserer(racine->droite, valeur);
    }
    // Si egal, on ne fait rien (pas de doublons)
    return racine;
}

// Recherche dans l'ABR
NoeudArbre* rechercher(NoeudArbre* racine, int valeur) {
    if (racine == NULL || racine->valeur == valeur) {
        return racine;
    }
    if (valeur < racine->valeur) {
        return rechercher(racine->gauche, valeur);
    }
    return rechercher(racine->droite, valeur);
}

// Trouver le minimum dans un sous-arbre
NoeudArbre* trouverMin(NoeudArbre* noeud) {
    while (noeud->gauche != NULL) {
        noeud = noeud->gauche;
    }
    return noeud;
}

// Parcours prefixe (Pre-order) : Racine - Gauche - Droite
void parcoursPrefix(NoeudArbre* racine) {
    if (racine != NULL) {
        printf("%d ", racine->valeur);
        parcoursPrefix(racine->gauche);
        parcoursPrefix(racine->droite);
    }
}

// Parcours infixe (In-order) : Gauche - Racine - Droite
// Produit les elements dans l'ordre croissant pour un ABR
void parcoursInfixe(NoeudArbre* racine) {
    if (racine != NULL) {
        parcoursInfixe(racine->gauche);
        printf("%d ", racine->valeur);
        parcoursInfixe(racine->droite);
    }
}

// Parcours postfixe (Post-order) : Gauche - Droite - Racine
void parcoursPostfixe(NoeudArbre* racine) {
    if (racine != NULL) {
        parcoursPostfixe(racine->gauche);
        parcoursPostfixe(racine->droite);
        printf("%d ", racine->valeur);
    }
}

// Calcul de la hauteur de l'arbre
int hauteur(NoeudArbre* racine) {
    if (racine == NULL) return -1;
    int hGauche = hauteur(racine->gauche);
    int hDroite = hauteur(racine->droite);
    return 1 + (hGauche > hDroite ? hGauche : hDroite);
}

// Comptage du nombre de noeuds
int compterNoeuds(NoeudArbre* racine) {
    if (racine == NULL) return 0;
    return 1 + compterNoeuds(racine->gauche) + compterNoeuds(racine->droite);
}

// Liberation de l'arbre (parcours postfixe)
void libererArbre(NoeudArbre* racine) {
    if (racine != NULL) {
        libererArbre(racine->gauche);
        libererArbre(racine->droite);
        free(racine);
    }
}

int main() {
    NoeudArbre* racine = NULL;

    // Insertion de valeurs
    racine = inserer(racine, 50);
    inserer(racine, 30);
    inserer(racine, 70);
    inserer(racine, 20);
    inserer(racine, 40);
    inserer(racine, 60);
    inserer(racine, 80);

    //        50
    //       /  \
    //      30    70
    //     / \   / \
    //    20  40 60  80

    printf("Parcours infixe (croissant) : ");
    parcoursInfixe(racine);
    printf("\n");
    // Resultat : 20 30 40 50 60 70 80

    printf("Parcours prefixe : ");
    parcoursPrefix(racine);
    printf("\n");
    // Resultat : 50 30 20 40 70 60 80

    printf("Parcours postfixe : ");
    parcoursPostfixe(racine);
    printf("\n");
    // Resultat : 20 40 30 60 80 70 50

    printf("Hauteur : %d\n", hauteur(racine));
    printf("Nombre de noeuds : %d\n", compterNoeuds(racine));

    NoeudArbre* trouve = rechercher(racine, 40);
    if (trouve) printf("Element 40 trouve dans l'arbre\n");

    libererArbre(racine);
    return 0;
}
```

### 4. Projet Fourmis Fourrageuses : Structure et Code

Le projet de simulation de fourmis fourrageuses est le projet tuteure du semestre S2. Il modelise le comportement de fourmis qui cherchent de la nourriture, deposent des pheromones et retournent au nid. L'affichage se fait en mode console avec des couleurs via l'API Windows.

#### Constantes et types de donnees du projet

```cpp
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <windows.h>
#include <ctime>
using namespace std;

// Dimensions de la grille de simulation
const int LIG_MAX = 20;
const int COL_MAX = 40;

// Caracteres d'affichage
const char CARAC_FM = '8';   // Caractere representant une fourmi
const char CARAC_MUR = '#';  // Caractere representant un mur
const char CARAC_VIDE = '.'; // Caractere representant une case vide
const char CARAC_NID = 'N';  // Caractere representant le nid
const char CARAC_FOOD = 'F'; // Caractere representant la nourriture

// Limites de fourmis
const int NB_FOURMIS_MAX = 20;

// Types de donnees pour la grille et les fourmis
typedef char matriceEcran[LIG_MAX][COL_MAX];
typedef int fourmisSave[NB_FOURMIS_MAX][3]; // colonnes: X, Y, etat
```

#### Fonction de couleur console Windows

```cpp
// Gestion des couleurs dans la console Windows
// couleurTexte : 0=noir, 1=bleu, 2=vert, 3=cyan, 4=rouge, ...
// couleurFond  : meme correspondance de couleurs
void Color(int couleurTexte, int couleurFond) {
    HANDLE H = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleTextAttribute(H, couleurFond * 16 + couleurTexte);
}

// Exemple d'utilisation :
// Color(4, 0);  -> texte rouge sur fond noir
// Color(2, 0);  -> texte vert sur fond noir
// Color(14, 0); -> texte jaune sur fond noir
// Color(7, 0);  -> retour a la couleur par defaut (gris)
```

#### Initialisation de la grille

```cpp
// Initialisation de la matrice d'ecran avec les murs, le nid et la nourriture
void initialiserGrille(matriceEcran grille, int posNidX, int posNidY,
                       int posFoodX, int posFoodY) {
    for (int i = 0; i < LIG_MAX; i++) {
        for (int j = 0; j < COL_MAX; j++) {
            // Bordures = murs
            if (i == 0 || i == LIG_MAX - 1 || j == 0 || j == COL_MAX - 1) {
                grille[i][j] = CARAC_MUR;
            } else {
                grille[i][j] = CARAC_VIDE;
            }
        }
    }
    // Placement du nid et de la nourriture
    grille[posNidY][posNidX] = CARAC_NID;
    grille[posFoodY][posFoodX] = CARAC_FOOD;
}
```

#### Affichage de la grille avec couleurs

```cpp
// Affichage de la grille dans la console avec gestion des couleurs
void afficherGrille(matriceEcran grille) {
    // Repositionner le curseur en haut a gauche (evite le clignotement)
    COORD coord;
    coord.X = 0;
    coord.Y = 0;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);

    for (int i = 0; i < LIG_MAX; i++) {
        for (int j = 0; j < COL_MAX; j++) {
            switch (grille[i][j]) {
                case CARAC_MUR:
                    Color(8, 0);   // Gris fonce
                    cout << CARAC_MUR;
                    break;
                case CARAC_NID:
                    Color(14, 0);  // Jaune
                    cout << CARAC_NID;
                    break;
                case CARAC_FOOD:
                    Color(2, 0);   // Vert
                    cout << CARAC_FOOD;
                    break;
                case CARAC_FM:
                    Color(4, 0);   // Rouge
                    cout << CARAC_FM;
                    break;
                default:
                    Color(7, 0);   // Gris par defaut
                    cout << grille[i][j];
                    break;
            }
        }
        cout << endl;
    }
    Color(7, 0); // Reset couleur
}
```

#### Machine a etats pour le comportement des fourmis

```cpp
// Etats possibles d'une fourmi
enum EtatFourmi {
    CHERCHER_NOURRITURE = 0,  // La fourmi explore aleatoirement
    SUIVRE_PHEROMONE = 1,     // La fourmi suit une piste de pheromones
    RETOUR_NID = 2,           // La fourmi retourne au nid avec de la nourriture
    AU_NID = 3                // La fourmi est au nid
};

// Structure representant une fourmi
struct Fourmi {
    int posX;
    int posY;
    EtatFourmi etat;
    int nourriturePortee;     // 0 ou 1
    int direction;            // Direction actuelle (0-7 pour 8 directions)
};

// Deplacement aleatoire de la fourmi (exploration)
void deplacerAleatoire(Fourmi* fourmi, matriceEcran grille) {
    int dx, dy;
    int tentatives = 0;

    do {
        dx = (rand() % 3) - 1; // -1, 0, ou 1
        dy = (rand() % 3) - 1;
        tentatives++;
    } while ((dx == 0 && dy == 0) && tentatives < 10);

    int nouvX = fourmi->posX + dx;
    int nouvY = fourmi->posY + dy;

    // Verification des limites et des obstacles
    if (nouvX > 0 && nouvX < COL_MAX - 1 &&
        nouvY > 0 && nouvY < LIG_MAX - 1 &&
        grille[nouvY][nouvX] != CARAC_MUR) {
        fourmi->posX = nouvX;
        fourmi->posY = nouvY;
    }
}

// Mise a jour de l'etat de la fourmi (machine a etats)
void mettreAJourEtat(Fourmi* fourmi, matriceEcran grille,
                     int nidX, int nidY) {
    switch (fourmi->etat) {
        case CHERCHER_NOURRITURE:
            deplacerAleatoire(fourmi, grille);
            // Si la fourmi trouve de la nourriture
            if (grille[fourmi->posY][fourmi->posX] == CARAC_FOOD) {
                fourmi->nourriturePortee = 1;
                fourmi->etat = RETOUR_NID;
            }
            break;

        case RETOUR_NID:
            // Se diriger vers le nid
            if (fourmi->posX < nidX) fourmi->posX++;
            else if (fourmi->posX > nidX) fourmi->posX--;
            if (fourmi->posY < nidY) fourmi->posY++;
            else if (fourmi->posY > nidY) fourmi->posY--;
            // Si la fourmi est au nid
            if (fourmi->posX == nidX && fourmi->posY == nidY) {
                fourmi->nourriturePortee = 0;
                fourmi->etat = CHERCHER_NOURRITURE;
            }
            break;

        default:
            break;
    }
}
```

#### Boucle principale de simulation

```cpp
int main() {
    srand((unsigned int)time(NULL));

    matriceEcran grille;
    int nidX = 5, nidY = 10;
    int foodX = 35, foodY = 10;

    initialiserGrille(grille, nidX, nidY, foodX, foodY);

    // Initialisation des fourmis au nid
    const int NB_FOURMIS = 10;
    Fourmi fourmis[NB_FOURMIS];
    for (int i = 0; i < NB_FOURMIS; i++) {
        fourmis[i].posX = nidX;
        fourmis[i].posY = nidY;
        fourmis[i].etat = CHERCHER_NOURRITURE;
        fourmis[i].nourriturePortee = 0;
        fourmis[i].direction = rand() % 8;
    }

    // Boucle de simulation
    int iteration = 0;
    while (iteration < 1000) {
        // Nettoyer les anciennes positions des fourmis
        for (int i = 0; i < NB_FOURMIS; i++) {
            if (grille[fourmis[i].posY][fourmis[i].posX] == CARAC_FM) {
                grille[fourmis[i].posY][fourmis[i].posX] = CARAC_VIDE;
            }
        }

        // Mettre a jour chaque fourmi
        for (int i = 0; i < NB_FOURMIS; i++) {
            mettreAJourEtat(&fourmis[i], grille, nidX, nidY);
        }

        // Placer les fourmis sur la grille
        for (int i = 0; i < NB_FOURMIS; i++) {
            grille[fourmis[i].posY][fourmis[i].posX] = CARAC_FM;
        }

        // Remettre le nid et la nourriture
        grille[nidY][nidX] = CARAC_NID;
        grille[foodY][foodX] = CARAC_FOOD;

        afficherGrille(grille);
        Sleep(100); // Pause de 100ms entre chaque iteration
        iteration++;
    }

    return 0;
}
```

### 5. Algorithmes de tri

#### Tri rapide (Quicksort)

```c
#include <stdio.h>

void echanger(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int tab[], int debut, int fin) {
    int pivot = tab[fin];
    int i = debut - 1;
    for (int j = debut; j < fin; j++) {
        if (tab[j] <= pivot) {
            i++;
            echanger(&tab[i], &tab[j]);
        }
    }
    echanger(&tab[i + 1], &tab[fin]);
    return i + 1;
}

void quicksort(int tab[], int debut, int fin) {
    if (debut < fin) {
        int pi = partition(tab, debut, fin);
        quicksort(tab, debut, pi - 1);
        quicksort(tab, pi + 1, fin);
    }
}

int main() {
    int tab[] = {64, 25, 12, 22, 11, 90, 45};
    int n = sizeof(tab) / sizeof(tab[0]);

    quicksort(tab, 0, n - 1);

    printf("Tableau trie : ");
    for (int i = 0; i < n; i++) {
        printf("%d ", tab[i]);
    }
    printf("\n");
    // Resultat : 11 12 22 25 45 64 90
    return 0;
}
```

### 6. Gestion de fichiers

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char nom[50];
    int age;
    float note;
} Etudiant;

// Ecriture dans un fichier texte
void ecrireFichierTexte(const char* nomFichier, Etudiant* etudiants, int nb) {
    FILE* f = fopen(nomFichier, "w");
    if (f == NULL) {
        printf("Erreur d'ouverture du fichier\n");
        return;
    }
    for (int i = 0; i < nb; i++) {
        fprintf(f, "%s %d %.2f\n",
                etudiants[i].nom, etudiants[i].age, etudiants[i].note);
    }
    fclose(f);
}

// Lecture depuis un fichier texte
int lireFichierTexte(const char* nomFichier, Etudiant* etudiants, int maxEtu) {
    FILE* f = fopen(nomFichier, "r");
    if (f == NULL) {
        printf("Erreur d'ouverture du fichier\n");
        return 0;
    }
    int nb = 0;
    while (nb < maxEtu &&
           fscanf(f, "%s %d %f",
                  etudiants[nb].nom, &etudiants[nb].age,
                  &etudiants[nb].note) == 3) {
        nb++;
    }
    fclose(f);
    return nb;
}

// Ecriture en mode binaire
void ecrireFichierBinaire(const char* nomFichier, Etudiant* etudiants, int nb) {
    FILE* f = fopen(nomFichier, "wb");
    if (f == NULL) return;
    fwrite(&nb, sizeof(int), 1, f);
    fwrite(etudiants, sizeof(Etudiant), nb, f);
    fclose(f);
}

int main() {
    Etudiant etudiants[3] = {
        {"Alice", 20, 15.5},
        {"Bob", 21, 12.0},
        {"Charlie", 19, 17.8}
    };
    ecrireFichierTexte("etudiants.txt", etudiants, 3);
    ecrireFichierBinaire("etudiants.bin", etudiants, 3);

    Etudiant lecture[10];
    int nbLu = lireFichierTexte("etudiants.txt", lecture, 10);
    printf("Nombre d'etudiants lus : %d\n", nbLu);

    return 0;
}
```

### 7. Programmation modulaire

Le projet fourmis illustre le principe de la programmation modulaire, ou le code est decoupe en fichiers logiques :

```
Projet_Fourmis/
  |-- main.cpp           // Point d'entree et boucle principale
  |-- affichage.h        // Prototypes des fonctions d'affichage
  |-- affichage.cpp      // Implementation de l'affichage console
  |-- fourmis.h          // Prototypes des fonctions de gestion des fourmis
  |-- fourmis.cpp        // Implementation du comportement des fourmis
  |-- grille.h           // Prototypes des fonctions de gestion de la grille
  |-- grille.cpp         // Implementation de la grille (init, mise a jour)
  |-- types.h            // Definitions de types, constantes, structures
```

Chaque fichier `.h` contient les prototypes et les gardes d'inclusion :

```cpp
// types.h
#ifndef TYPES_H
#define TYPES_H

const int LIG_MAX = 20;
const int COL_MAX = 40;
const int NB_FOURMIS_MAX = 20;

typedef char matriceEcran[LIG_MAX][COL_MAX];

enum EtatFourmi { CHERCHER, SUIVRE, RETOUR, AU_NID };

struct Fourmi {
    int posX, posY;
    EtatFourmi etat;
    int nourriture;
};

#endif // TYPES_H
```

---

## PART D : ANALYSE ET REFLEXION

### Competences acquises

- Conception d'algorithmes efficaces avec analyse de complexite
- Gestion de la memoire dynamique sans fuites
- Programmation modulaire et structuree
- Debogage avance (pas a pas, inspection de variables, pile d'appels)
- Travail en binome sur un projet de taille moyenne
- Optimisation de code et bonnes pratiques

### Retour sur le projet Fourmis Fourrageuses

Le projet de simulation de fourmis fourrageuses a ete l'experience la plus formatrice du semestre. Il a permis de mettre en pratique l'ensemble des concepts vus en cours dans un contexte concret et motivant :

- **Structures de donnees** : utilisation de matrices pour la grille, de structures pour les fourmis, de tableaux pour la sauvegarde des etats
- **Machines a etats** : chaque fourmi suit un automate a etats finis (chercher, suivre, retourner, nid) qui determine son comportement a chaque iteration
- **API systeme** : interaction avec la console Windows pour l'affichage en couleurs, le positionnement du curseur et le controle du rafraichissement
- **Programmation modulaire** : decomposition du projet en fichiers logiques avec separation des responsabilites

Le travail en binome sur une semaine intensive (11-18 janvier 2021) a ete un exercice de gestion du temps et de repartition des taches. La communication et la planification ont ete essentielles pour livrer un projet fonctionnel dans les delais.

### Auto-evaluation

Ce semestre a marque une progression significative en programmation. Les concepts de listes chainees, d'arbres binaires et de gestion memoire sont desormais maitrises et constituent des fondations solides pour les semestres suivants. Le projet fourmis a demontre la capacite a gerer un projet complet, de la conception a la livraison.

### Bonnes pratiques developpees

- Nommage clair des variables et fonctions
- Commentaires pertinents du code
- Indentation et formatage coherents
- Toujours liberer la memoire allouee dynamiquement
- Tester au fur et a mesure du developpement
- Valider les entrees utilisateur
- Utiliser des gardes d'inclusion dans les fichiers d'en-tete
- Decouper le code en fonctions de taille raisonnable

### Connexions interdisciplinaires

La programmation S2 fournit les competences necessaires pour le cours d'Informatique Embarquee (programmation C pour microcontroleurs), l'Etude et Realisation (programmation de microcontroleurs en ER), et le projet tuteure CEC (developpement collaboratif avec rapport et soutenance).

---

## Documents de Cours

### Rapport de Projet Tuteure : Simulation de Fourmis Fourrageuses

Ce rapport presente le travail realise dans le cadre du projet tuteure de programmation du semestre 2. Il detaille la conception, l'implementation et les resultats de la simulation de fourmis fourrageuses en C/C++, realisee en binome (GIBERT et CHANFREAU) du 11 au 18 janvier 2021.

<div class="pdf-item">
  <h4>Rapport PTUT Programmation - Simulation de Fourmis Fourrageuses</h4>
  <p>Rapport complet du projet tuteure de programmation : conception de la simulation, architecture du code, resultats obtenus et ameliorations possibles.</p>
  <embed src="/file/reports/RAPPORT_PTUT_PROG_FINALLL.pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/file/reports/RAPPORT_PTUT_PROG_FINALLL.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
  </p>
</div>

### Presentation du Projet (Soutenance CEC)

<div class="pdf-item">
  <h4>Presentation PTUT Programmation S1 - GIBERT CHANFREAU</h4>
  <p>Support de presentation utilise lors de la soutenance du projet tuteure de programmation.</p>
  <embed src="/cours-pdf/S2/CEC/PRESENTATION_GIBERT_CHANFREAU_PTUT_PROGRAMMATION_S1.pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/cours-pdf/S2/CEC/PRESENTATION_GIBERT_CHANFREAU_PTUT_PROGRAMMATION_S1.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
  </p>
</div>

---

<style>body{font-family:Arial,sans-serif;background-color:#f4f4f9;color:#333;line-height:1.6}h2,h3,h4,h5{color:#2a7ae2}p{text-align:justify}code{background-color:#f5f5f5;padding:2px 6px;border-radius:3px;font-family:'Courier New',monospace}pre{background-color:#f5f5f5;padding:15px;border-radius:5px;overflow-x:auto}</style>

<div class="back-nav">
  <a href="./my-courses-2020-2021.html">← Retour a Mes Cours 2020-2021</a>
</div>

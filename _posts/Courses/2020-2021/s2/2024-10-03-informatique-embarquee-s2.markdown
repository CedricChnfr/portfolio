---
layout: default
title: "Informatique Embarquee (IE) - S2"
date: 2024-10-02 10:56:03 +0200
---

<style>
.back-nav { margin-bottom: 20px; }
.back-nav a { text-decoration: none; color: #2a7ae2; font-weight: 600; }
.back-nav a:hover { text-decoration: underline; }
.section-title { color: #2a7ae2; border-bottom: 2px solid #2a7ae2; padding-bottom: 10px; margin-top: 30px; margin-bottom: 20px; }
</style>

<div class="back-nav">
  <a href="./my-courses-2020-2021.html">&larr; Retour a Mes Cours 2020-2021</a>
</div>

# Informatique Embarquee (IE) - S2

**Annee**: 2020-2021 | **Semestre**: 2 | **Type**: Informatique Industrielle

---

## PART A : PRESENTATION GENERALE

### Contexte et objectifs

Le cours d'Informatique Embarquee au semestre 2 du DUT GEII constitue une introduction approfondie a la programmation de microcontroleurs et aux systemes embarques. Le cours s'appuie sur le microcontroleur **Siemens/Infineon C167**, un processeur 16 bits industriel programme en langage C via l'environnement de developpement **Keil uVision**. Ce cours couvre l'ensemble de la chaine, de la representation binaire des donnees jusqu'a la gestion des interruptions, en passant par les entrees/sorties numeriques, les timers et les conversions analogique-numerique.

**Objectifs pedagogiques :**
- Comprendre la representation des nombres en binaire (entiers signes/non signes, virgule fixe, virgule flottante)
- Maitriser l'architecture memoire et le fonctionnement interne d'un microcontroleur 16 bits
- Programmer en C embarque avec acces direct aux registres materiels
- Gerer les peripheriques de base : GPIO, timers, CNA/CAN
- Comprendre et implementer les interruptions materielles
- Developper des applications embarquees completes (chenillard, generateur de frequence, acquisition de donnees)

### Organisation

Le cours est structure en 9 chapitres progressifs (CHAP0 a CHAP9), chacun accompagne de travaux pratiques sur la plateforme C167. L'enseignement alterne entre cours magistraux theoriques et seances de TP en salle de microcontroleurs. L'evaluation porte sur les comptes-rendus de TP et les examens ecrits.

---

## PART B : EXPERIENCE ET CONTEXTE

### Environnement pedagogique

L'enseignement d'Informatique Embarquee est realise sur des cartes de developpement equipees du microcontroleur **Infineon C167**. Ce processeur 16 bits, issu de la famille Siemens C166, est un microcontroleur industriel qui offre une architecture riche avec de nombreux peripheriques integres (timers, CAN, CNA, ports serie, ports GPIO). Contrairement a des plateformes grand public comme Arduino, le C167 impose de travailler directement avec les registres du processeur, ce qui oblige a une comprehension fine de l'architecture materielle.

L'IDE utilise est **Keil uVision**, un environnement de developpement professionnel pour microcontroleurs ARM et C166/C167. Keil fournit un compilateur C optimise, un debugger integre et un simulateur qui permet de tester le code avant de le deployer sur la cible.

### Plateforme C167

Le microcontroleur C167 possede les caracteristiques suivantes :
- CPU 16 bits a 25 MHz
- 128 Ko de memoire Flash interne
- 4 Ko de RAM interne
- 16 canaux ADC 10 bits
- 5 timers 16 bits (T0 a T6 avec T1 et T5 reserves)
- 2 ports serie (USART)
- Ports GPIO configurables (P0 a P8)
- Systeme d'interruptions avec 16 niveaux de priorite

### Outils de developpement

- **Keil uVision IDE** : edition, compilation, debogage
- **Compilateur C166** : compilateur C specifique a la famille C166/C167
- **Debugger JTAG** : debogage en temps reel sur la cible
- **Bibliotheque IUT_C167_2019** : bibliotheque maison fournissant des fonctions utilitaires (initialisation serie, temporisations, etc.)
- **Terminal serie** : communication avec le PC via RS232

### Liens avec d'autres cours

- **Programmation S1/S2** : les bases du langage C (variables, boucles, fonctions, pointeurs) sont le prerequis indispensable
- **ER S2 (Microcontroleur)** : meme plateforme C167, mais avec un focus sur l'interface avec le materiel (capteurs, actionneurs)
- **ER S2 (FPGA)** : complementarite entre logiciel embarque et logique programmable
- **Systemes Electroniques** : comprehension des signaux et des circuits d'interface

<img src="/assets/images/courses/S2/IE/Correction organigramme TP3.png" alt="Organigramme TP3 - Chenillard" style="max-width: 100%; height: auto; margin: 20px 0; border: 1px solid #ddd; border-radius: 5px; padding: 10px;">

---

## PART C : ASPECTS TECHNIQUES

### Chapitre 0-1 : Representation des nombres en binaire

#### Entiers non signes

Un nombre entier non signe sur N bits peut representer les valeurs de 0 a 2^N - 1. Sur le C167 (processeur 16 bits), les types principaux sont :

```
unsigned char   : 8 bits  -> 0 a 255
unsigned int    : 16 bits -> 0 a 65535
unsigned long   : 32 bits -> 0 a 4 294 967 295
```

La conversion binaire-decimal s'effectue par decomposition en puissances de 2 :

```
Exemple : 0b10110011 = 1*128 + 0*64 + 1*32 + 1*16 + 0*8 + 0*4 + 1*2 + 1*1 = 179
```

#### Entiers signes (complement a deux)

Pour representer des nombres negatifs, on utilise le complement a deux. Le bit de poids fort (MSB) indique le signe : 0 pour positif, 1 pour negatif. La plage de representation sur N bits est de -2^(N-1) a 2^(N-1) - 1.

```
signed char : 8 bits  -> -128 a +127
signed int  : 16 bits -> -32768 a +32767
```

Pour obtenir l'oppose d'un nombre en complement a deux :
1. Inverser tous les bits (complement a un)
2. Ajouter 1

```
Exemple : +5 = 0b00000101
          ~5 = 0b11111010  (complement a un)
          -5 = 0b11111011  (complement a deux = complement a un + 1)
```

#### Representation hexadecimale

L'hexadecimal est couramment utilise pour les adresses memoire et les valeurs de registres :

```
0xFF = 0b11111111 = 255
0x0A = 0b00001010 = 10
0x1F = 0b00011111 = 31
```

#### Operations bit a bit

Les operations bit a bit sont fondamentales en programmation embarquee pour manipuler les registres :

```c
/* OU logique : mettre des bits a 1 */
registre |= 0x08;    /* Met le bit 3 a 1 sans toucher les autres */

/* ET logique : mettre des bits a 0 */
registre &= ~0x08;   /* Met le bit 3 a 0 sans toucher les autres */

/* OU EXCLUSIF : inverser des bits */
registre ^= 0x08;    /* Inverse le bit 3 */

/* Decalage a gauche : multiplication par 2^n */
valeur = 1 << 3;     /* Resultat : 0b00001000 = 8 */

/* Decalage a droite : division par 2^n */
valeur = 0x80 >> 3;  /* Resultat : 0b00010000 = 16 */
```

### Chapitre 2-3-4 : Memoire, architecture et rappels C

#### Architecture memoire du C167

Le C167 utilise une architecture Von Neumann segmentee avec un espace d'adressage de 16 Mo (bus d'adresses 24 bits). La memoire est organisee en segments de 64 Ko :

```
Adresse 0x000000 - 0x00FFFF : Segment 0 (memoire interne)
  - 0x000000 - 0x001FFF : SFR (Special Function Registers)
  - 0x00F600 - 0x00FDFF : RAM interne (2 Ko)
  - 0x00FE00 - 0x00FFFF : SFR supplementaires

Adresse 0x010000 - ...      : Memoire externe (Flash, RAM externe)
```

Les **SFR (Special Function Registers)** sont les registres de controle des peripheriques. Chaque peripherique (timer, port, ADC, etc.) est controle via un ou plusieurs SFR situes a des adresses fixes dans l'espace memoire.

#### Registres de direction des ports

Chaque port GPIO du C167 possede un registre de direction (DPx) et un registre de donnees (Px) :

```c
/* DP = Direction Port : 0 = entree, 1 = sortie */
DP7 = 0x00;   /* Configure tout le port 7 en entree */
DP8 = 0xFF;   /* Configure tout le port 8 en sortie */

/* Lecture/ecriture des ports */
valeur = P7;  /* Lit l'etat du port 7 */
P8 = 0xAA;    /* Ecrit 0xAA sur le port 8 */
```

#### Rappels de C pour l'embarque

Le C embarque differe du C standard sur plusieurs points :
- Acces direct aux adresses memoire via des pointeurs ou des macros
- Utilisation intensive des operations bit a bit
- Absence de systeme d'exploitation (pas de `printf` classique, pas de gestion automatique de la memoire)
- Boucle infinie dans le `main()` (le programme ne s'arrete jamais)
- Inclusion d'un fichier d'en-tete specifique au processeur (`reg167.h`)

```c
#include <reg167.h>       /* Definitions des SFR du C167 */
#include "IUT_C167_2019.h" /* Bibliotheque IUT */

void main(void) {
    init_serie();          /* Initialise la liaison serie */
    /* ... initialisation des peripheriques ... */

    do {
        /* Boucle principale infinie */
    } while(1);
}
```

### Chapitre 5 : Langage C applique au C167

#### Types de donnees et taille memoire

Sur le C167, la taille des types est importante pour l'optimisation :

```c
char           : 1 octet  (8 bits)
int            : 2 octets (16 bits) - type natif du processeur
long           : 4 octets (32 bits)
float          : 4 octets (32 bits, IEEE 754)
double         : 8 octets (64 bits)
```

Le type `int` est le type naturel du C167 (16 bits). Les operations sur `int` sont les plus rapides. Les operations sur `long` et `float` sont plus lentes car elles necessitent plusieurs instructions machine.

#### Structures et unions pour les registres

Les structures et unions permettent d'acceder aux bits individuels d'un registre :

```c
/* Acces par masque de bits */
if (P7 & 0x01) {     /* Teste le bit 0 du port 7 */
    P8 |= 0x80;      /* Met le bit 7 du port 8 a 1 */
}

/* Equivalent avec des constantes nommees */
#define SW1   0x01    /* Interrupteur 1 sur bit 0 */
#define LED8  0x80    /* LED 8 sur bit 7 */

if (P7 & SW1) {
    P8 |= LED8;
}
```

#### Fonctions de temporisation

La bibliotheque IUT fournit des fonctions de temporisation calibrees :

```c
tempo_ms(200);   /* Temporisation de 200 millisecondes */
tempo_us(100);   /* Temporisation de 100 microsecondes */
```

### Chapitre 6 : Entrees/sorties numeriques (GPIO)

#### Configuration des ports

Le C167 dispose de 9 ports (P0 a P8). La configuration se fait via les registres de direction :

```c
void initPorts(void) {
    DP7 = 0x00;   /* Port 7 en entree (interrupteurs) */
    DP8 = 0xFF;   /* Port 8 en sortie (LEDs) */
}
```

Certains ports ont des fonctions alternatives (timer output, serial I/O, ADC input). Le registre de direction permet de choisir entre la fonction GPIO et la fonction alternative.

#### Exemple complet : Chenillard LED (TP3)

Le chenillard est un programme classique qui fait defiler un motif lumineux sur un ensemble de LEDs. Voici l'implementation realisee en TP :

```c
#include <reg167.h>
#include "IUT_C167_2019.h"

void initPorts(void) {
    DP7 = 0x00;   /* Port 7 en entree */
    DP8 = 0xFF;   /* Port 8 en sortie */
}

void main(void) {
    unsigned char chenillard;
    init_serie();
    initPorts();
    chenillard = (unsigned char)P7;
    do {
        P8 = chenillard;
        tempo_ms(200);
        chenillard = chenillard << 1;
        if (chenillard == 0) chenillard = 1;
    } while(1);
}
```

**Analyse du code :**
1. Le port 7 est configure en entree pour lire la valeur initiale depuis les interrupteurs
2. Le port 8 est configure en sortie pour commander les LEDs
3. La valeur initiale du chenillard est lue sur le port 7
4. A chaque iteration, le motif est decale d'un bit vers la gauche
5. Quand le motif sort du registre (valeur 0 apres 8 decalages), il est reinitialise a 1
6. La temporisation de 200 ms determine la vitesse de defilement

#### Lecture de boutons avec anti-rebond

En pratique, les boutons mecaniques generent des rebonds lors de l'appui. Une technique simple d'anti-rebond logiciel :

```c
unsigned char lire_bouton(void) {
    unsigned char etat1, etat2;
    etat1 = P7 & 0x01;       /* Premiere lecture */
    tempo_ms(20);             /* Attente anti-rebond */
    etat2 = P7 & 0x01;       /* Deuxieme lecture */
    if (etat1 == etat2) {
        return etat1;         /* Lecture valide */
    }
    return 0xFF;              /* Lecture invalide */
}
```

### Chapitre 7 : Timers et generation de frequence

#### Architecture des timers du C167

Le C167 dispose de plusieurs timers 16 bits. Les plus couramment utilises sont :
- **T0** : timer general
- **T2** : timer avec fonction de rechargement
- **T3** : timer avec sortie toggle (generation de frequence)
- **T4** : timer general
- **T6** : timer avec capture

Chaque timer possede un registre de controle (TxCON) qui permet de configurer :
- La source d'horloge (horloge interne avec prediviseur ou horloge externe)
- Le mode de comptage (compteur/decompteur)
- L'activation de la sortie

#### Registre de controle T3CON

Le registre T3CON (Timer 3 Control) a la structure suivante :

```
Bit 15    : T3R  - Run (1 = timer actif)
Bit 14    : T3UD - Up/Down (0 = compteur, 1 = decompteur)
Bit 13    : T3UDE - Up/Down external
Bit 12-11 : T3M  - Mode
Bit 10    : T3OE - Output Enable (active la sortie toggle)
Bit 9     : T3OTL - Output Toggle Latch
Bits 2-0  : T3I  - Input selection (prescaler)
```

Le prescaler divise l'horloge systeme :
- T3I = 000 : pas de comptage (timer arrete)
- T3I = 001 : fCPU / 4
- T3I = 010 : fCPU / 8
- T3I = 011 : fCPU / 16
- T3I = 100 : fCPU / 32
- T3I = 101 : fCPU / 64
- T3I = 110 : fCPU / 128
- T3I = 111 : fCPU / 256

#### Generation de frequence avec Timer 3 et Timer 2 (TP5)

Le principe consiste a utiliser T3 en decompteur avec sortie toggle : a chaque passage par 0, la sortie P3.3 change d'etat (toggle). Le Timer 2 recharge automatiquement T3 a chaque debordement.

```c
void init_gene_freq(unsigned int prediv_T3I, unsigned int nb_impul_freq) {
    DP3 |= 0x0008;          /* P3.3 en sortie (bit 3 du port 3) */
    T3CON = (prediv_T3I & 0x07);  /* Configure le prescaler de T3 */
    T3OTL = 0;              /* Initialise le toggle latch */
    T3OE = 1;               /* Active la sortie toggle sur P3.3 */
    T3UD = 1;               /* Mode decompteur */
    T2CON = 0x0027;         /* T2 en mode rechargement de T3 */
    T3 = nb_impul_freq - 1; /* Valeur initiale du compteur */
    T2 = nb_impul_freq - 1; /* Valeur de rechargement */
}
```

**Calcul de la frequence generee** :

La frequence de sortie depend du prescaler et de la valeur de rechargement :

```
f_toggle = f_CPU / (prescaler * nb_impul_freq)
f_signal = f_toggle / 2   (car un toggle = demi-periode)

Exemple : f_CPU = 20 MHz, prescaler = 8 (T3I = 010), nb_impul_freq = 250
f_toggle = 20 000 000 / (8 * 250) = 10 000 Hz
f_signal = 10 000 / 2 = 5 000 Hz = 5 kHz
```

#### Generation de PWM

La modulation de largeur d'impulsion (PWM) permet de controler la puissance delivree a un actionneur. Le principe :

```c
/* PWM simple avec timer et comparaison */
void pwm_simple(unsigned char rapport) {
    /* rapport : 0 a 255 (0% a 100%) */
    do {
        P8 = 0xFF;              /* Sortie haute */
        tempo_us(rapport);      /* Duree du niveau haut */
        P8 = 0x00;              /* Sortie basse */
        tempo_us(255 - rapport); /* Duree du niveau bas */
    } while(1);
}
```

### Chapitre 8 : Convertisseurs CNA et CAN

#### Convertisseur Numerique-Analogique (CNA / DAC)

Le CNA convertit une valeur numerique en une tension analogique proportionnelle. Sur le C167, la conversion peut etre realisee par un CNA externe ou par PWM + filtre passe-bas.

Pour un CNA de N bits avec une tension de reference Vref :

```
Resolution = Vref / (2^N - 1)
V_sortie = (valeur_numerique / (2^N - 1)) * Vref

Exemple : CNA 8 bits, Vref = 5V
Resolution = 5 / 255 = 19.6 mV
Valeur 128 -> V = (128 / 255) * 5 = 2.51 V
```

#### Convertisseur Analogique-Numerique (CAN / ADC)

Le C167 integre un ADC 10 bits avec 16 canaux multiplexes. La configuration se fait via les registres ADCON (ADC Control) :

```c
void init_adc(void) {
    ADCON = 0x0000;   /* Configuration de base */
    /* Bits 3-0 : selection du canal (0 a 15) */
    /* Bit 4    : mode de conversion */
    /* Bit 8    : ADST (start conversion) */
    /* Bit 11   : ADBSY (busy flag) */
}

unsigned int lire_adc(unsigned char canal) {
    ADCON = canal & 0x0F;     /* Selectionne le canal */
    ADCON |= 0x0100;          /* Lance la conversion (ADST = 1) */
    while (ADCON & 0x0800);   /* Attend la fin de conversion (ADBSY) */
    return ADDAT;             /* Lit le resultat (10 bits) */
}
```

**Calcul de la tension mesuree** :

```
V_entree = (valeur_ADC / 1023) * Vref

Exemple : ADC 10 bits, Vref = 5V, valeur lue = 512
V = (512 / 1023) * 5 = 2.50 V
```

#### Temps de conversion et echantillonnage

Le temps de conversion de l'ADC du C167 depend de la frequence d'horloge et du nombre de cycles necessaires :

```
T_conversion = (nombre_de_cycles) / f_ADC_clock
f_echantillonnage_max = 1 / T_conversion
```

Le theoreme de Shannon impose : `f_echantillonnage >= 2 * f_max_signal` pour eviter le repliement spectral (aliasing).

### Chapitre 9 : Interruptions

#### Principe des interruptions

Une interruption est un mecanisme materiel qui permet au processeur de suspendre l'execution du programme principal pour traiter un evenement urgent (timer overflow, reception de donnees, front sur une broche). Contrairement au polling (scrutation), les interruptions permettent au processeur de realiser d'autres taches entre deux evenements.

Le mecanisme d'interruption suit ces etapes :
1. Un evenement declencheur se produit (flag d'interruption leve)
2. Le processeur termine l'instruction en cours
3. Le contexte est sauvegarde (registres, compteur programme)
4. Le processeur saute a l'adresse du vecteur d'interruption
5. La routine d'interruption (ISR) est executee
6. Le contexte est restaure et le programme principal reprend

#### Configuration sur le C167

Le C167 possede un systeme d'interruption avec 16 niveaux de priorite. Chaque source d'interruption possede un registre de controle d'interruption (xxIC) :

```
Bits 3-0  : ILVL (Interrupt Level, 0-15, 0 = desactive)
Bits 5-4  : GLVL (Group Level, sous-priorite)
Bit 6     : IE (Interrupt Enable)
Bit 7     : IR (Interrupt Request flag)
```

#### Exemple : interruption timer

```c
#include <reg167.h>
#include "IUT_C167_2019.h"

/* Variable globale modifiee dans l'ISR */
volatile unsigned int compteur = 0;

/* Routine d'interruption du Timer 3 */
void timer3_isr(void) interrupt T3INT = 0x23 {
    compteur++;
    if (compteur >= 500) {
        P8 ^= 0x01;    /* Toggle LED 1 toutes les 500 interruptions */
        compteur = 0;
    }
}

void init_timer3_interrupt(void) {
    T3CON = 0x0002;    /* Prescaler /8 */
    T3 = 0;
    T3IC = 0x0044;     /* Priorite 4, interruption activee */
    T3R = 1;           /* Demarre le timer */
}

void main(void) {
    init_serie();
    DP8 = 0xFF;        /* Port 8 en sortie */
    P8 = 0x00;

    init_timer3_interrupt();
    IEN = 1;           /* Active les interruptions globales */

    do {
        /* Le programme principal peut faire autre chose */
        /* L'ISR gere le clignotement en arriere-plan */
    } while(1);
}
```

**Points importants** :
- Le mot-cle `volatile` est obligatoire pour les variables partagees entre le programme principal et une ISR
- Le mot-cle `interrupt` suivi du numero de vecteur declare une fonction comme ISR
- L'ISR doit etre la plus courte possible pour ne pas bloquer les autres interruptions
- `IEN = 1` active le systeme d'interruptions global du C167

#### Priorites et imbrication

Le C167 supporte l'imbrication des interruptions : une interruption de priorite superieure peut interrompre une ISR de priorite inferieure. La priorite est determinee par ILVL (niveau) et GLVL (groupe, sous-priorite au sein du meme niveau).

```
Priorite globale = ILVL * 4 + GLVL
Plus le nombre est eleve, plus la priorite est haute.
```

### Communication serie (UART)

Le C167 dispose de deux ports serie (ASC0 et ASC1). La communication serie permet d'echanger des donnees avec un PC via RS232 :

```c
/* La bibliotheque IUT_C167_2019 fournit : */
init_serie();              /* Configure ASC0 a 9600 bauds, 8N1 */
putchar('A');              /* Envoie un caractere */
char c = getchar();        /* Recoit un caractere (bloquant) */
printf("Valeur = %d\n", v); /* Affichage formate */
```

Le protocole RS232 utilise un format asynchrone :
- 1 bit de start (niveau bas)
- 8 bits de donnees (LSB en premier)
- 0 ou 1 bit de parite
- 1 ou 2 bits de stop (niveau haut)

La vitesse de communication (baud rate) est configuree via le registre S0BG :

```
Baud rate = f_CPU / (32 * (S0BG + 1))
Pour 9600 bauds avec f_CPU = 20 MHz :
S0BG = 20 000 000 / (32 * 9600) - 1 = 64
```

---

## PART D : ANALYSE ET REFLEXION

### Competences acquises

Ce cours d'Informatique Embarquee a ete fondateur pour ma comprehension des systemes numeriques et de la programmation bas niveau :

- **Programmation de registres** : la manipulation directe des SFR du C167 m'a appris a travailler au plus pres du materiel. Contrairement aux couches d'abstraction des frameworks modernes (HAL, Arduino), cette approche oblige a comprendre chaque bit de configuration, ce qui donne une comprehension profonde du fonctionnement du microcontroleur.

- **Gestion du temps reel** : la programmation des timers et des interruptions m'a initie aux contraintes temps reel. La notion de latence d'interruption, de jitter et de priorite est essentielle pour les systemes embarques critiques.

- **Conversion de donnees** : la maitrise des CNA/CAN est fondamentale pour l'interface entre le monde numerique (processeur) et le monde analogique (capteurs, actionneurs).

- **Debogage embarque** : l'utilisation du debugger Keil (points d'arret, lecture de registres, execution pas a pas) est une competence professionnelle directement transferable a tout projet embarque.

### Auto-evaluation

Les premiers chapitres sur la representation binaire etaient relativement accessibles grace aux bases acquises en S1. La partie GPIO (chenillard) a ete motivante car les resultats sont immediatement visibles (LEDs qui clignotent). Les timers ont represente un saut de complexite, notamment pour le calcul des frequences generees et la comprehension du mecanisme de rechargement T2->T3. Les interruptions ont ete le chapitre le plus difficile, car elles introduisent la notion de concurrence (programme principal + ISR) et les problemes associes (variables volatiles, sections critiques).

Le C167, bien que moins moderne que les processeurs ARM actuels, offre un excellent support pedagogique car son architecture est suffisamment simple pour etre entierement comprise, tout en etant representatif des microcontroleurs industriels.

### Connexions et perspectives

Les competences acquises dans ce cours sont directement reutilisees dans :
- **ER S2 (Microcontroleur)** : meme plateforme C167 avec des projets plus complexes
- **Cours de S3-S4** : les microcontroleurs ARM (STM32) utilisent les memes concepts (GPIO, timers, interruptions) avec une architecture plus evoluee
- **Informatique industrielle** : la programmation embarquee est au coeur des systemes de controle-commande
- **IoT** : les objets connectes reposent sur des microcontroleurs avec des contraintes similaires (consommation, temps reel, peripheriques)

Ce cours a constitue le point de depart de ma specialisation en systemes embarques et IoT, domaine que j'ai approfondi tout au long de mon cursus jusqu'au Master REOC.

---

## Documents de Cours

<div class="pdf-item">
  <h4>Chapitre 0-1 : Representation des nombres binaires</h4>
  <p>Entiers signes et non signes, complement a deux, representation hexadecimale, virgule fixe et flottante (IEEE 754).</p>
  <embed src="/cours-pdf/S2/Informatique-embarque/CHAP0_1_representation_nombres_binaires_2020_2021.pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/cours-pdf/S2/Informatique-embarque/CHAP0_1_representation_nombres_binaires_2020_2021.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
  </p>
</div>

<div class="pdf-item">
  <h4>Chapitre 2-3-4 : Memoire, architecture et rappels C</h4>
  <p>Organisation memoire du C167, architecture du processeur, rappels de programmation C pour l'embarque.</p>
  <embed src="/cours-pdf/S2/Informatique-embarque/CHAP2-3-4_memoire_architecture_rappel1_C_2020_2021.pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/cours-pdf/S2/Informatique-embarque/CHAP2-3-4_memoire_architecture_rappel1_C_2020_2021.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
  </p>
</div>

<div class="pdf-item">
  <h4>Chapitre 5 : Langage C applique au C167</h4>
  <p>Types de donnees, operateurs, structures de controle, fonctions, pointeurs et manipulation de registres en C embarque.</p>
  <embed src="/cours-pdf/S2/Informatique-embarque/CHAP5_Langage_C_2020_2021.pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/cours-pdf/S2/Informatique-embarque/CHAP5_Langage_C_2020_2021.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
  </p>
</div>

<div class="pdf-item">
  <h4>Chapitre 5 (suite) : Langage C - Approfondissement</h4>
  <p>Complement sur les tableaux, les chaines de caracteres, les structures, les unions et les pointeurs de fonctions.</p>
  <embed src="/cours-pdf/S2/Informatique-embarque/CHAP5_Langage_C_2020_2021_suite.pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/cours-pdf/S2/Informatique-embarque/CHAP5_Langage_C_2020_2021_suite.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
  </p>
</div>

<div class="pdf-item">
  <h4>Chapitre 6 : Entrees/sorties numeriques</h4>
  <p>Configuration des ports GPIO du C167, registres de direction, lecture d'entrees, commande de sorties.</p>
  <embed src="/cours-pdf/S2/Informatique-embarque/CHAP6_entree_sortie_numérique_2020_2021.pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/cours-pdf/S2/Informatique-embarque/CHAP6_entree_sortie_numérique_2020_2021.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
  </p>
</div>

<div class="pdf-item">
  <h4>Chapitre 7 : Timers</h4>
  <p>Architecture des timers du C167, prescaler, modes compteur/decompteur, sortie toggle, generation de frequence, PWM.</p>
  <embed src="/cours-pdf/S2/Informatique-embarque/CHAP7_Tmers.pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/cours-pdf/S2/Informatique-embarque/CHAP7_Tmers.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
  </p>
</div>

<div class="pdf-item">
  <h4>Chapitre 8 : CNA et CAN</h4>
  <p>Convertisseurs numerique-analogique et analogique-numerique, resolution, temps de conversion, ADC 10 bits du C167.</p>
  <embed src="/cours-pdf/S2/Informatique-embarque/CHAP8_CNA-CAN_2020_2021.pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/cours-pdf/S2/Informatique-embarque/CHAP8_CNA-CAN_2020_2021.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
  </p>
</div>

<div class="pdf-item">
  <h4>Chapitre 9 : Interruptions</h4>
  <p>Mecanisme d'interruption, vecteurs, priorites, registres de controle, routines d'interruption (ISR), imbrication.</p>
  <embed src="/cours-pdf/S2/Informatique-embarque/CHAP9_Interruptions_2020_2021.pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/cours-pdf/S2/Informatique-embarque/CHAP9_Interruptions_2020_2021.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
  </p>
</div>

---

<style>body{font-family:Arial,sans-serif;background-color:#f4f4f9;color:#333;line-height:1.6}h2,h3,h4,h5{color:#2a7ae2}p{text-align:justify}code{background-color:#f5f5f5;padding:2px 6px;border-radius:3px;font-family:'Courier New',monospace}pre{background-color:#f5f5f5;padding:15px;border-radius:5px;overflow-x:auto}</style>

<div class="back-nav">
  <a href="./my-courses-2020-2021.html">&larr; Retour a Mes Cours 2020-2021</a>
</div>

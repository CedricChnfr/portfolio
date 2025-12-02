---
layout: default
title: "Langage d'Assemblage ARM CORTEX - S6"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
---

<style>
.back-nav {
    background: #f4f4f4;
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 20px;
}

.section-title {
    color: #2a7ae2;
    border-bottom: 2px solid #2a7ae2;
    padding-bottom: 5px;
    margin-top: 30px;
}

table {
    border-collapse: collapse;
    width: 100%;
    margin: 20px 0;
}

th {
    background-color: #2a7ae2;
    color: white;
    padding: 10px;
    text-align: left;
}

td {
    border: 1px solid #ddd;
    padding: 10px;
}

tr:nth-child(even) {
    background-color: #f9f9f9;
}

.code-block {
    background: #f4f4f4;
    border-left: 4px solid #2a7ae2;
    padding: 15px;
    margin: 15px 0;
    font-family: 'Courier New', monospace;
}
</style>

<div class="back-nav">
    <a href="./my-courses-2022-2023.html">← Retour aux Cours 2022-2023</a>
</div>

# ⚙️ Langage d'Assemblage ARM CORTEX - Semestre 6

**Année Universitaire** : 2022-2023  
**Semestre** : 6  
**Crédits** : 2 ECTS  
**Spécialité** : Systèmes Embarqués et Programmation Bas Niveau

---

## PART A - Présentation Générale du Cours

<h3 class="section-title">Vue d'ensemble</h3>

Ce cours enseigne la programmation en langage assembleur pour les microcontrôleurs ARM Cortex-M (architecture 32 bits). Il couvre l'architecture du processeur, le jeu d'instructions Thumb-2, et la programmation bas niveau pour systèmes embarqués. Les travaux pratiques utilisent des STM32F103 (Cortex-M3) avec l'environnement Keil µVision.

**Objectifs pédagogiques** :
- Comprendre l'architecture ARM Cortex-M (registres, pipeline, mémoire)
- Maîtriser le jeu d'instructions Thumb-2
- Programmer en assembleur (boucles, fonctions, accès périphériques)
- Interfacer avec du matériel (GPIO, UART, timers)
- Optimiser le code pour performances et taille

<h3 class="section-title">Position dans le cursus</h3>

Ce cours complète et approfondit :
- **Architecture Informatique Matérielle (S5)** : bases de l'architecture processeur
- **Architecture Matérielle (S6)** : ARM vs x86, pipeline, caches
- **Microcontrôleur (S6)** : périphériques et programmation en C

Il prépare aux applications :
- **Systèmes embarqués temps réel** : code critique et optimisé
- **Développement de drivers** : accès direct au matériel
- **Bootloaders et firmware** : code de bas niveau

---

## PART B - Expérience Personnelle et Contexte d'Apprentissage

<h3 class="section-title">Organisation et ressources</h3>

Le module était structuré en 4 séquences progressives :

**1. Séquence 1 : Architecture ARM Cortex-M**
- Organisation mémoire et registres
- Pipeline et modes d'exécution
- Conventions d'appel AAPCS

**2. Séquence 2 : Jeu d'instructions de base**
- Instructions arithmétiques et logiques
- Déplacements et chargements mémoire
- Branchements et boucles

**3. Séquence 3 : Sous-programmes et pile**
- Appels de fonctions (BL, BX)
- Gestion de la pile (PUSH, POP)
- Passage de paramètres

**4. Séquence 4 : Accès périphériques**
- Registres memory-mapped
- Contrôle GPIO
- Communication UART
- Interruptions

**Environnement de développement** :
- **IDE** : Keil µVision 5
- **Cible** : STM32F103RB (Cortex-M3, 128 KB Flash, 20 KB RAM)
- **Simulateur** : simulation cycle-accurate sans carte physique
- **Débuggage** : breakpoints, registres, mémoire, désassemblage

<h3 class="section-title">Déroulement des TDs et TPs</h3>

**TD2 : Conversion et affichage**

Objectif : lire 4 chiffres au clavier, les convertir en entier, et afficher le résultat.

**Fonctions à implémenter** :

```asm
; Lecture de 4 caractères via UART
BL GetKey_Echo      ; Lit un caractère et l'affiche
STRB R0,[R7]        ; Stocke dans la mémoire RAM

; Conversion ASCII → nombre
LDRB R3,[R7],#1     ; Charge caractère
SUB R3,#'0'         ; Convertit '0'-'9' en 0-9
MOV R4,#10
MUL R3,R3,R4        ; Décalage décimal

; Affichage d'une chaîne
Affichaine PROC
    LDRB R0,[R3],#1  ; Charge caractère
    CBZ R0,Fin       ; Si 0, fin de chaîne
    BL SendChar      ; Envoie via UART
    B Car_suivant    ; Boucle
Fin_Chaine
    POP {R0,PC}      ; Retour
    ENDP
```

**Concepts clés** :
- Adressage indirect avec post-incrément : `[R7],#1`
- Convention d'appel : paramètres dans R0-R3
- Sauvegarde contexte : PUSH/POP avec LR

**TD3 : Manipulation de tableaux**

Travail sur tableaux d'entiers : tri, recherche, calculs statistiques.

**Exemple : recherche du maximum**

```asm
; R0 = adresse du tableau
; R1 = taille du tableau
; Retour : R2 = valeur maximale

Recherche_Max PROC
    PUSH {R3,R4,LR}
    LDR R2,[R0],#4   ; Premier élément = max initial
    SUBS R1,#1       ; Compteur -1
    
Boucle
    LDR R3,[R0],#4   ; Élément suivant
    CMP R3,R2
    BLE Suivant      ; Si <= max, passe au suivant
    MOV R2,R3        ; Nouveau max
Suivant
    SUBS R1,#1       ; Décrément compteur
    BNE Boucle       ; Tant que != 0
    
    POP {R3,R4,PC}
    ENDP
```

**TD4 : Fonctions mathématiques**

Implémentation d'opérations complexes (division, racine carrée par approximations successives).

**TP : Projet "Roue Magique"**

Projet fil rouge en plusieurs étapes pour créer un jeu de lumières avec LEDs.

**Étape 1 : Contrôle d'une LED**

```asm
; Allumer une LED sur PC10
Allume_LED PROC
    LDR R0,=0x40010C10  ; Adresse GPIOC_BSRR (Bit Set Reset Register)
    MOV R1,#(0x01 << 10) ; Bit 10 pour PC10
    STR R1,[R0]          ; Écriture → LED allumée
    BX LR                ; Retour
    ENDP

; Éteindre la LED
Eteint_LED PROC
    LDR R2,=0x40010C14  ; Adresse GPIOC_BRR (Bit Reset Register)
    MOV R3,#(0x01 << 10)
    STR R3,[R2]
    BX LR
    ENDP
```

**Étape 2 : Lecture d'un bouton**

```asm
; Lire l'état d'un bouton sur PB8
Capteur PROC
    LDR R4,=0x40010808   ; Adresse GPIOB_IDR (Input Data Register)
    LDRH R5,[R4]         ; Lecture 16 bits
    AND R5,R5,#0x0100    ; Masque bit 8
    CMP R5,#0
    BEQ Bouton_Presse    ; Si 0, bouton appuyé
    BX LR
    ENDP
```

**Étape 3 : Séquence de LEDs**

Faire clignoter plusieurs LEDs en séquence (chenillard).

**Étape 4 : Interruptions et timers**

Utiliser un timer pour créer des délais précis sans attente active.

<h3 class="section-title">Difficultés rencontrées</h3>

**Gestion de la pile** :
Oublier de faire POP après PUSH provoque des erreurs de retour de fonction. Le LR (Link Register) doit être sauvegardé si la fonction appelle d'autres fonctions.

**Adressage mémoire** :
Confusion entre adresse et valeur. LDR R0,=0x2000 charge l'adresse, LDR R0,[R1] charge la valeur à l'adresse contenue dans R1.

**Flags de condition** :
Les instructions avec 'S' (ADDS, SUBS) modifient les flags NZCV. Nécessaire avant CMP pour les branchements conditionnels.

**Registres de périphériques** :
Adresses spécifiques à mémoriser ou utiliser des fichiers include. Documentation du STM32 indispensable.

---

## PART C - Aspects Techniques Détaillés

<h3 class="section-title">1. Architecture ARM Cortex-M3</h3>

**Banc de registres** :

Le Cortex-M3 dispose de 16 registres 32 bits :

| Registre | Nom | Usage |
|----------|-----|-------|
| R0-R12 | Registres généraux | Calculs, données temporaires |
| R13 (SP) | Stack Pointer | Pointeur de pile |
| R14 (LR) | Link Register | Adresse de retour de fonction |
| R15 (PC) | Program Counter | Adresse de l'instruction en cours |

**Registres spéciaux** :
- **PSR** (Program Status Register) : flags N, Z, C, V, mode, exceptions
- **PRIMASK** : masque global d'interruptions
- **CONTROL** : sélection de pile, niveau de privilège

**Organisation mémoire** :

| Région | Adresses | Usage |
|--------|----------|-------|
| Code | 0x00000000 - 0x1FFFFFFF | Flash, instructions |
| SRAM | 0x20000000 - 0x3FFFFFFF | RAM, données |
| Périphériques | 0x40000000 - 0x5FFFFFFF | Registres memory-mapped |
| Système | 0xE0000000 - 0xFFFFFFFF | NVIC, SysTick, debug |

**Pipeline 3 étages** :
1. Fetch : lecture instruction
2. Decode : décodage
3. Execute : exécution

Conséquence : le PC pointe toujours 2 instructions en avance (PC+4 en Thumb-2).

<h3 class="section-title">2. Jeu d'Instructions Thumb-2</h3>

**Instructions arithmétiques** :

| Instruction | Syntaxe | Description |
|-------------|---------|-------------|
| ADD | ADD Rd, Rn, Rm | Rd = Rn + Rm |
| SUB | SUB Rd, Rn, Rm | Rd = Rn - Rm |
| MUL | MUL Rd, Rn, Rm | Rd = Rn × Rm |
| SDIV | SDIV Rd, Rn, Rm | Rd = Rn / Rm (signé) |
| UDIV | UDIV Rd, Rn, Rm | Rd = Rn / Rm (non signé) |

Variantes avec flags : ADDS, SUBS (modifient NZCV).

**Instructions logiques** :

| Instruction | Description |
|-------------|-------------|
| AND Rd, Rn, Rm | ET logique |
| ORR Rd, Rn, Rm | OU logique |
| EOR Rd, Rn, Rm | OU exclusif (XOR) |
| BIC Rd, Rn, Rm | Bit Clear (Rd = Rn AND NOT Rm) |
| MVN Rd, Rm | NOT (inversion) |

**Décalages** :

| Instruction | Description |
|-------------|-------------|
| LSL Rd, Rn, #n | Logical Shift Left (décalage gauche) |
| LSR Rd, Rn, #n | Logical Shift Right (décalage droite, complète avec 0) |
| ASR Rd, Rn, #n | Arithmetic Shift Right (conserve le signe) |
| ROR Rd, Rn, #n | Rotate Right (rotation) |

**Déplacements de données** :

```asm
MOV R0,#42          ; R0 = 42 (immédiat)
MOV R1,R2           ; R1 = R2 (copie)
MOVW R0,#0x1234     ; Charge 16 bits bas
MOVT R0,#0x5678     ; Charge 16 bits haut → R0 = 0x56781234
```

<h3 class="section-title">3. Accès Mémoire</h3>

**Instructions de chargement** :

| Instruction | Taille | Description |
|-------------|--------|-------------|
| LDR Rd,[Rn] | 32 bits | Charge mot |
| LDRH Rd,[Rn] | 16 bits | Charge demi-mot (halfword) |
| LDRB Rd,[Rn] | 8 bits | Charge octet (byte) |
| LDRSB Rd,[Rn] | 8 bits signé | Charge octet avec extension de signe |
| LDRSH Rd,[Rn] | 16 bits signé | Charge demi-mot avec extension de signe |

**Instructions de stockage** :

| Instruction | Taille | Description |
|-------------|--------|-------------|
| STR Rd,[Rn] | 32 bits | Stocke mot |
| STRH Rd,[Rn] | 16 bits | Stocke demi-mot |
| STRB Rd,[Rn] | 8 bits | Stocke octet |

**Modes d'adressage** :

```asm
; Direct
LDR R0,[R1]         ; R0 = mem[R1]

; Offset
LDR R0,[R1,#8]      ; R0 = mem[R1+8]

; Pré-incrémenté
LDR R0,[R1,#8]!     ; R1 = R1+8, puis R0 = mem[R1]

; Post-incrémenté
LDR R0,[R1],#8      ; R0 = mem[R1], puis R1 = R1+8

; Indexé par registre
LDR R0,[R1,R2]      ; R0 = mem[R1+R2]

; PC-relatif (litteral pool)
LDR R0,=0x20000000  ; Charge adresse via pool constant
```

<h3 class="section-title">4. Contrôle de Flux</h3>

**Branchements inconditionnels** :

```asm
B etiquette         ; Branchement simple
BL fonction         ; Branchement avec Link (LR = PC+4)
BX Rm               ; Branchement vers adresse dans Rm
BLX Rm              ; Branchement avec Link vers Rm
```

**Branchements conditionnels** :

Basés sur les flags NZCV (Negative, Zero, Carry, oVerflow).

| Suffixe | Condition | Flags |
|---------|-----------|-------|
| EQ | Égal | Z=1 |
| NE | Non égal | Z=0 |
| GT | Supérieur (signé) | Z=0 ET N=V |
| LT | Inférieur (signé) | N≠V |
| GE | Supérieur ou égal (signé) | N=V |
| LE | Inférieur ou égal (signé) | Z=1 OU N≠V |
| HI | Supérieur (non signé) | C=1 ET Z=0 |
| LS | Inférieur ou égal (non signé) | C=0 OU Z=1 |

**Comparaisons** :

```asm
CMP R0,R1           ; Compare R0 et R1 (calcule R0-R1, met à jour flags)
CMN R0,R1           ; Compare negative (calcule R0+R1)
TST R0,R1           ; Test bits (AND, met à jour flags sans stocker)
TEQ R0,R1           ; Test equal (XOR, met à jour flags)
```

**Exemple de boucle** :

```asm
    MOV R0,#10      ; Compteur
Boucle
    ; ... code ...
    SUBS R0,#1      ; Décrément et mise à jour flags
    BNE Boucle      ; Tant que R0 != 0
```

<h3 class="section-title">5. Sous-programmes et Pile</h3>

**Convention d'appel AAPCS** (ARM Architecture Procedure Call Standard) :

| Registre | Usage | Sauvegarde |
|----------|-------|------------|
| R0-R3 | Paramètres et retour | Caller-saved |
| R4-R11 | Variables locales | Callee-saved |
| R12 | Temporaire | Caller-saved |
| R13 (SP) | Pile | - |
| R14 (LR) | Adresse retour | - |

**Appel de fonction** :

```asm
; Appelant (caller)
    MOV R0,#5       ; Premier paramètre
    MOV R1,#10      ; Deuxième paramètre
    BL MaFonction   ; Appel (LR = adresse retour)
    ; R0 contient le résultat

; Fonction (callee)
MaFonction PROC
    PUSH {R4,LR}    ; Sauvegarde registres utilisés
    
    ; Calculs utilisant R0, R1, R4
    ADD R4,R0,R1
    MOV R0,R4       ; Résultat dans R0
    
    POP {R4,PC}     ; Restaure et retourne
    ENDP
```

**Gestion de la pile** :

La pile croît vers les adresses décroissantes (full descending).

```asm
PUSH {R0-R3,LR}     ; Sauvegarde multiple
; SP = SP - 20 (5 registres × 4 octets)

POP {R0-R3,PC}      ; Restauration et retour
; SP = SP + 20
```

**Équivalent** :
- PUSH {Rx} = STMDB SP!, {Rx} (Store Multiple Decrement Before)
- POP {Rx} = LDMIA SP!, {Rx} (Load Multiple Increment After)

<h3 class="section-title">6. Accès aux Périphériques</h3>

**Memory-mapped I/O** :

Les périphériques sont accessibles via des adresses mémoire spécifiques.

**Exemple : GPIO (General Purpose Input/Output)**

Registres du GPIOC (Port C) pour STM32F103 :

| Registre | Adresse | Usage |
|----------|---------|-------|
| CRL | 0x40011000 | Configuration broches 0-7 |
| CRH | 0x40011004 | Configuration broches 8-15 |
| IDR | 0x40011008 | Input Data Register (lecture) |
| ODR | 0x4001100C | Output Data Register (écriture) |
| BSRR | 0x40011010 | Bit Set/Reset Register |
| BRR | 0x40011014 | Bit Reset Register |

**Configuration d'une broche en sortie** :

```asm
; Configurer PC10 en sortie push-pull, 50 MHz
    LDR R0,=0x40011004  ; GPIOC_CRH
    LDR R1,[R0]
    BIC R1,#(0xF << 8)  ; Clear bits pour PC10
    ORR R1,#(0x3 << 8)  ; MODE=11 (50MHz), CNF=00 (push-pull)
    STR R1,[R0]
```

**Manipulation de bits** :

```asm
; Mise à 1 d'un bit (set)
LDR R0,=0x40011010  ; GPIOC_BSRR
MOV R1,#(1 << 10)   ; Bit 10
STR R1,[R0]         ; PC10 = 1

; Mise à 0 d'un bit (reset)
LDR R0,=0x40011014  ; GPIOC_BRR
MOV R1,#(1 << 10)
STR R1,[R0]         ; PC10 = 0

; Lecture d'un bit
LDR R0,=0x40011008  ; GPIOC_IDR
LDR R1,[R0]
TST R1,#(1 << 8)    ; Test bit 8
BEQ Bit_A_Zero      ; Branch if zero
```

<h3 class="section-title">7. Directives Assembleur</h3>

**Organisation du code** :

```asm
    AREA MonCode, CODE, READONLY, ALIGN=2
    ; Sections de code
    
    AREA MesDonnees, DATA, READWRITE
    ; Sections de données
```

**Définition de données** :

```asm
; Constantes
Valeur  EQU 42          ; Équivalent #define

; Données initialisées
Tableau DCD 1,2,3,4,5   ; Define Constant Data (32 bits)
Chaine  DCB "Hello",0   ; Define Constant Byte (8 bits)
Mot     DCW 0x1234      ; Define Constant Word (16 bits)

; Données non initialisées
Buffer  SPACE 100       ; Réserve 100 octets
```

**Déclarations** :

```asm
    EXPORT main         ; Rend le symbole visible à l'extérieur
    IMPORT fonction     ; Importe un symbole externe
    
    PROC                ; Début de procédure
    ENDP                ; Fin de procédure
    
    END                 ; Fin du fichier source
```

<h3 class="section-title">8. Optimisations</h3>

**Taille de code** :

Instructions Thumb-2 sont 16 ou 32 bits. Préférer les instructions 16 bits quand possible.

```asm
; 16 bits
ADDS R0,R1,R2       ; Si R0-R7 et résultat modifie flags

; 32 bits
ADD.W R0,R1,R2      ; Force 32 bits
```

**Boucles efficaces** :

```asm
; Inefficace (compare à 0 à chaque itération)
    MOV R0,#0
Boucle
    ; ...
    ADD R0,#1
    CMP R0,#100
    BLT Boucle

; Efficace (décrémente et teste zéro implicitement)
    MOV R0,#100
Boucle
    ; ...
    SUBS R0,#1
    BNE Boucle
```

**Éviter les branchements** :

Utiliser les instructions conditionnelles quand possible.

```asm
; Avec branchement
    CMP R0,R1
    BLE Suivant
    MOV R2,R0
Suivant
    ; ...

; Sans branchement (IT = If-Then)
    CMP R0,R1
    IT GT
    MOVGT R2,R0     ; Exécuté si GT
```

---

## PART D - Analyse Réflexive et Perspectives

<h3 class="section-title">Compétences acquises</h3>

**Compréhension bas niveau** :
La programmation en assembleur force à comprendre exactement ce qui se passe au niveau processeur : chaque instruction, chaque accès mémoire, chaque modification de flag. Cette compréhension aide à débugger et optimiser le code C.

**Contrôle total du matériel** :
Accès direct aux registres de périphériques, manipulation bit à bit, timing précis. Essentiel pour développer des drivers ou du code temps réel critique.

**Optimisation** :
Conscience du coût de chaque instruction. Savoir où optimiser (boucles critiques) et quand laisser le compilateur faire le travail.

<h3 class="section-title">Points clés à retenir</h3>

**1. La pile est votre amie (et votre ennemie)** :
PUSH/POP doivent toujours être équilibrés. Oublier un POP ou faire POP du mauvais registre provoque des bugs difficiles à tracer.

**2. LR doit être sauvegardé** :
Si une fonction appelle d'autres fonctions, LR doit être sauvegardé (PUSH {LR}) et restauré (POP {PC}) pour retourner correctement.

**3. Flags de condition** :
Les instructions avec 'S' (ADDS, SUBS) modifient les flags. Nécessaire pour les branchements conditionnels. Attention à ne pas écraser les flags entre CMP et Bxx.

**4. Adressage mémoire** :
Bien distinguer adresse et valeur. LDR R0,=etiquette charge l'adresse, LDR R0,[R1] charge la valeur à l'adresse contenue dans R1.

**5. Documentation indispensable** :
Avoir toujours sous la main :
- ARM Architecture Reference Manual (jeu d'instructions)
- STM32 Reference Manual (adresses périphériques)
- Cortex-M3 Technical Reference Manual (architecture)

<h3 class="section-title">Applications pratiques</h3>

**Systèmes embarqués critiques** :
Bootloaders, routines d'initialisation, handlers d'interruption critiques. Code assembleur pour timing précis ou optimisation extrême.

**Drivers de périphériques** :
Accès direct aux registres matériels pour performances maximales. Utile quand les HAL (Hardware Abstraction Layer) sont trop lourds.

**Reverse engineering** :
Comprendre l'assembleur permet d'analyser du code compilé, débugger des problèmes obscurs, ou étudier des malwares.

**Inline assembly en C** :
Intégrer quelques instructions assembleur dans du code C pour optimisations locales.

```c
// Exemple inline assembly GCC
__asm volatile (
    "MOV R0, #42\n"
    "ADD R1, R0, R0\n"
    : "=r" (resultat)
    : "r" (entree)
    : "r0", "r1"
);
```

<h3 class="section-title">Assembleur vs C</h3>

**Quand utiliser l'assembleur** :
- Code critique en temps (ISR ultra-rapides)
- Optimisation extrême (boucles intensives)
- Accès à des fonctionnalités spéciales (instructions SIMD)
- Bootloaders et code d'initialisation
- Taille de code très contrainte

**Quand préférer le C** :
- Développement rapide et maintenabilité
- Portabilité entre architectures
- Code métier complexe
- 95% des cas !

Les compilateurs modernes optimisent très bien. L'assembleur manuel n'est souvent nécessaire que pour quelques pourcents du code.

<h3 class="section-title">Retour d'expérience sur le projet TP</h3>

Le projet "Roue Magique" a permis d'appliquer tous les concepts :
- Étape 1 : contrôle GPIO, découverte des registres
- Étape 2 : lecture d'entrées, logique conditionnelle
- Étape 3 : boucles et séquences
- Étape 4 : timers et interruptions

**Progression pédagogique** :
Chaque étape ajoute de la complexité. On construit progressivement un système complet. Sentiment d'accomplissement en voyant les LEDs s'allumer selon notre code.

**Difficultés** :
Débugger en assembleur est plus difficile qu'en C. Pas de printf facile. Utilisation intensive du debugger et de l'observation des registres.

<h3 class="section-title">Limites et ouvertures</h3>

**Limites du cours** :
- Peu sur les interruptions avancées (NVIC complet)
- Pas de DMA ou timers complexes
- Peu de code optimisé (SIMD, DSP)
- Pas de systèmes d'exploitation temps réel (RTOS)

**Ouvertures vers** :
- **Embedded C avancé** : inline assembly, optimisations
- **RTOS** : FreeRTOS, tâches, synchronisation
- **Compilation et linking** : fichiers objets, éditeur de liens
- **Architectures avancées** : Cortex-M4 DSP, Cortex-M7 cache
- **Sécurité** : TrustZone, secure boot

<h3 class="section-title">Évolution technologique</h3>

**Tendances actuelles** :
- **Cortex-M33** : TrustZone pour sécurité
- **Cortex-M55** : extensions Helium pour machine learning
- **RISC-V** : alternative open-source à ARM
- **Compilation Just-In-Time** : pour microcontrôleurs puissants

**Outils modernes** :
- CMSIS (Cortex Microcontroller Software Interface Standard)
- HAL (Hardware Abstraction Layer) générées automatiquement
- IDE graphiques (STM32CubeIDE, Mbed Studio)
- Débogage avancé (Segger J-Link, Ozone)

<h3 class="section-title">Conclusion</h3>

La programmation en assembleur ARM est un passage obligé pour comprendre en profondeur le fonctionnement des microcontrôleurs. Même si 95% du code moderne est écrit en C/C++, connaître l'assembleur permet :
- De mieux comprendre ce que fait le compilateur
- D'optimiser le code critique
- De débugger des problèmes complexes
- De développer des drivers efficaces
- D'apprécier la puissance des langages de haut niveau

L'architecture ARM Cortex-M est omniprésente dans les systèmes embarqués modernes (IoT, wearables, drones, automobile). La maîtriser est un atout majeur pour tout ingénieur en systèmes embarqués.

**Recommandations** :
- Pratiquer régulièrement (petits programmes, défis)
- Lire du code assembleur généré par le compilateur (option -S de GCC)
- Participer à des CTF (Capture The Flag) de reverse engineering
- Expérimenter avec différentes architectures (ARM, RISC-V, x86)

**Liens avec les autres cours** :
- [Architecture Matérielle - S6](./architecture-materielle.html) : pipeline, cache
- [Microcontrôleur - S6](./microcontroleur.html) : périphériques, C embarqué
- [Électronique Fonctions Numériques - S6](./electronique-fonctions-numeriques.html) : bus I2C/SPI
- [Temps Réel - S8](./temps-reel.html) : contraintes temporelles

---

*Cours enseigné en 2022-2023 à l'INSA Toulouse, Département Génie Électrique et Informatique.*

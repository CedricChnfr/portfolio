---
layout: default
title: "Langage d'Assemblage ARM CORTEX - S6"
date: 2024-10-02 10:56:03 +0200
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

.pdf-container {
    margin: 40px 0;
    padding: 20px;
    background: #f9f9f9;
    border-radius: 8px;
}
.pdf-viewer {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
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
    color: #2a7ae2;
    margin-top: 0;
}
</style>

<div class="back-nav">
    <a href="./my-courses-2022-2023.html" data-i18n-html="back-courses-2022-2023">← Retour aux Cours 2022-2023</a>
</div>

<!-- ==================== FRENCH VERSION ==================== -->
<div class="lang-fr">

<h1>⚙️ Langage d'Assemblage ARM CORTEX - Semestre 6</h1>

<p><strong>Année Universitaire</strong> : 2022-2023<br/>
<strong>Semestre</strong> : 6<br/>
<strong>Crédits</strong> : 2 ECTS<br/>
<strong>Spécialité</strong> : Systèmes Embarqués et Programmation Bas Niveau</p>

<hr/>

<h2>PART A - Présentation Générale du Cours</h2>

<h3 class="section-title">Vue d'ensemble</h3>

<p>Ce cours enseigne la programmation en langage assembleur pour les microcontrôleurs ARM Cortex-M (architecture 32 bits). Il couvre l'architecture du processeur, le jeu d'instructions Thumb-2, et la programmation bas niveau pour systèmes embarqués. Les travaux pratiques utilisent des STM32F103 (Cortex-M3) avec l'environnement Keil µVision.</p>

<p><strong>Objectifs pédagogiques</strong> :</p>
<ul>
<li>Comprendre l'architecture ARM Cortex-M (registres, pipeline, mémoire)</li>
<li>Maîtriser le jeu d'instructions Thumb-2</li>
<li>Programmer en assembleur (boucles, fonctions, accès périphériques)</li>
<li>Interfacer avec du matériel (GPIO, UART, timers)</li>
<li>Optimiser le code pour performances et taille</li>
</ul>

<h3 class="section-title">Position dans le cursus</h3>

<p>Ce cours complète et approfondit :</p>
<ul>
<li><strong>Architecture Informatique Matérielle (S5)</strong> : bases de l'architecture processeur</li>
<li><strong>Architecture Matérielle (S6)</strong> : ARM vs x86, pipeline, caches</li>
<li><strong>Microcontrôleur (S6)</strong> : périphériques et programmation en C</li>
</ul>

<p>Il prépare aux applications :</p>
<ul>
<li><strong>Systèmes embarqués temps réel</strong> : code critique et optimisé</li>
<li><strong>Développement de drivers</strong> : accès direct au matériel</li>
<li><strong>Bootloaders et firmware</strong> : code de bas niveau</li>
</ul>

<hr/>

<h2>PART B - Expérience Personnelle et Contexte d'Apprentissage</h2>

<h3 class="section-title">Organisation et ressources</h3>

<p>Le module était structuré en 4 séquences progressives :</p>

<p><strong>1. Séquence 1 : Architecture ARM Cortex-M</strong></p>
<ul>
<li>Organisation mémoire et registres</li>
<li>Pipeline et modes d'exécution</li>
<li>Conventions d'appel AAPCS</li>
</ul>

<p><strong>2. Séquence 2 : Jeu d'instructions de base</strong></p>
<ul>
<li>Instructions arithmétiques et logiques</li>
<li>Déplacements et chargements mémoire</li>
<li>Branchements et boucles</li>
</ul>

<p><strong>3. Séquence 3 : Sous-programmes et pile</strong></p>
<ul>
<li>Appels de fonctions (BL, BX)</li>
<li>Gestion de la pile (PUSH, POP)</li>
<li>Passage de paramètres</li>
</ul>

<p><strong>4. Séquence 4 : Accès périphériques</strong></p>
<ul>
<li>Registres memory-mapped</li>
<li>Contrôle GPIO</li>
<li>Communication UART</li>
<li>Interruptions</li>
</ul>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S6/arm-cortex/registres-arm.svg" alt="Registres ARM Cortex-M" style="max-width: 550px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Organisation des registres ARM Cortex-M - R0-R15, SP, LR, PC et PSR</p>
</div>

<p><strong>Environnement de développement</strong> :</p>
<ul>
<li><strong>IDE</strong> : Keil µVision 5</li>
<li><strong>Cible</strong> : STM32F103RB (Cortex-M3, 128 KB Flash, 20 KB RAM)</li>
<li><strong>Simulateur</strong> : simulation cycle-accurate sans carte physique</li>
<li><strong>Débuggage</strong> : breakpoints, registres, mémoire, désassemblage</li>
</ul>

<h3 class="section-title">Déroulement des TDs et TPs</h3>

<p><strong>TD2 : Conversion et affichage</strong></p>

<p>Objectif : lire 4 chiffres au clavier, les convertir en entier, et afficher le résultat.</p>

<p><strong>Fonctions à implémenter</strong> :</p>

<pre><code class="language-asm">; Lecture de 4 caractères via UART
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
</code></pre>

<p><strong>Concepts clés</strong> :</p>
<ul>
<li>Adressage indirect avec post-incrément : <code>[R7],#1</code></li>
<li>Convention d'appel : paramètres dans R0-R3</li>
<li>Sauvegarde contexte : PUSH/POP avec LR</li>
</ul>

<p><strong>TD3 : Manipulation de tableaux</strong></p>

<p>Travail sur tableaux d'entiers : tri, recherche, calculs statistiques.</p>

<p><strong>Exemple : recherche du maximum</strong></p>

<pre><code class="language-asm">; R0 = adresse du tableau
; R1 = taille du tableau
; Retour : R2 = valeur maximale

Recherche_Max PROC
    PUSH {R3,R4,LR}
    LDR R2,[R0],#4   ; Premier élément = max initial
    SUBS R1,#1       ; Compteur -1

Boucle
    LDR R3,[R0],#4   ; Élément suivant
    CMP R3,R2
    BLE Suivant      ; Si &lt;= max, passe au suivant
    MOV R2,R3        ; Nouveau max
Suivant
    SUBS R1,#1       ; Décrément compteur
    BNE Boucle       ; Tant que != 0

    POP {R3,R4,PC}
    ENDP
</code></pre>

<p><strong>TD4 : Fonctions mathématiques</strong></p>

<p>Implémentation d'opérations complexes (division, racine carrée par approximations successives).</p>

<p><strong>TP : Projet "Roue Magique"</strong></p>

<p>Projet fil rouge en plusieurs étapes pour créer un jeu de lumières avec LEDs.</p>

<p><strong>Étape 1 : Contrôle d'une LED</strong></p>

<pre><code class="language-asm">; Allumer une LED sur PC10
Allume_LED PROC
    LDR R0,=0x40010C10  ; Adresse GPIOC_BSRR (Bit Set Reset Register)
    MOV R1,#(0x01 &lt;&lt; 10) ; Bit 10 pour PC10
    STR R1,[R0]          ; Écriture → LED allumée
    BX LR                ; Retour
    ENDP

; Éteindre la LED
Eteint_LED PROC
    LDR R2,=0x40010C14  ; Adresse GPIOC_BRR (Bit Reset Register)
    MOV R3,#(0x01 &lt;&lt; 10)
    STR R3,[R2]
    BX LR
    ENDP
</code></pre>

<p><strong>Étape 2 : Lecture d'un bouton</strong></p>

<pre><code class="language-asm">; Lire l'état d'un bouton sur PB8
Capteur PROC
    LDR R4,=0x40010808   ; Adresse GPIOB_IDR (Input Data Register)
    LDRH R5,[R4]         ; Lecture 16 bits
    AND R5,R5,#0x0100    ; Masque bit 8
    CMP R5,#0
    BEQ Bouton_Presse    ; Si 0, bouton appuyé
    BX LR
    ENDP
</code></pre>

<p><strong>Étape 3 : Séquence de LEDs</strong></p>

<p>Faire clignoter plusieurs LEDs en séquence (chenillard).</p>

<p><strong>Étape 4 : Interruptions et timers</strong></p>

<p>Utiliser un timer pour créer des délais précis sans attente active.</p>

<h3 class="section-title">Difficultés rencontrées</h3>

<p><strong>Gestion de la pile</strong> :
Oublier de faire POP après PUSH provoque des erreurs de retour de fonction. Le LR (Link Register) doit être sauvegardé si la fonction appelle d'autres fonctions.</p>

<p><strong>Adressage mémoire</strong> :
Confusion entre adresse et valeur. LDR R0,=0x2000 charge l'adresse, LDR R0,[R1] charge la valeur à l'adresse contenue dans R1.</p>

<p><strong>Flags de condition</strong> :
Les instructions avec 'S' (ADDS, SUBS) modifient les flags NZCV. Nécessaire avant CMP pour les branchements conditionnels.</p>

<p><strong>Registres de périphériques</strong> :
Adresses spécifiques à mémoriser ou utiliser des fichiers include. Documentation du STM32 indispensable.</p>

<hr/>

<h2>PART C - Aspects Techniques Détaillés</h2>

<h3 class="section-title">1. Architecture ARM Cortex-M3</h3>

<p><strong>Banc de registres</strong> :</p>

<p>Le Cortex-M3 dispose de 16 registres 32 bits :</p>

<table>
<tr><th>Registre</th><th>Nom</th><th>Usage</th></tr>
<tr><td>R0-R12</td><td>Registres généraux</td><td>Calculs, données temporaires</td></tr>
<tr><td>R13 (SP)</td><td>Stack Pointer</td><td>Pointeur de pile</td></tr>
<tr><td>R14 (LR)</td><td>Link Register</td><td>Adresse de retour de fonction</td></tr>
<tr><td>R15 (PC)</td><td>Program Counter</td><td>Adresse de l'instruction en cours</td></tr>
</table>

<p><strong>Registres spéciaux</strong> :</p>
<ul>
<li><strong>PSR</strong> (Program Status Register) : flags N, Z, C, V, mode, exceptions</li>
<li><strong>PRIMASK</strong> : masque global d'interruptions</li>
<li><strong>CONTROL</strong> : sélection de pile, niveau de privilège</li>
</ul>

<p><strong>Organisation mémoire</strong> :</p>

<table>
<tr><th>Région</th><th>Adresses</th><th>Usage</th></tr>
<tr><td>Code</td><td>0x00000000 - 0x1FFFFFFF</td><td>Flash, instructions</td></tr>
<tr><td>SRAM</td><td>0x20000000 - 0x3FFFFFFF</td><td>RAM, données</td></tr>
<tr><td>Périphériques</td><td>0x40000000 - 0x5FFFFFFF</td><td>Registres memory-mapped</td></tr>
<tr><td>Système</td><td>0xE0000000 - 0xFFFFFFFF</td><td>NVIC, SysTick, debug</td></tr>
</table>

<p><strong>Pipeline 3 étages</strong> :</p>
<ol>
<li>Fetch : lecture instruction</li>
<li>Decode : décodage</li>
<li>Execute : exécution</li>
</ol>

<p>Conséquence : le PC pointe toujours 2 instructions en avance (PC+4 en Thumb-2).</p>

<h3 class="section-title">2. Jeu d'Instructions Thumb-2</h3>

<p><strong>Instructions arithmétiques</strong> :</p>

<table>
<tr><th>Instruction</th><th>Syntaxe</th><th>Description</th></tr>
<tr><td>ADD</td><td>ADD Rd, Rn, Rm</td><td>Rd = Rn + Rm</td></tr>
<tr><td>SUB</td><td>SUB Rd, Rn, Rm</td><td>Rd = Rn - Rm</td></tr>
<tr><td>MUL</td><td>MUL Rd, Rn, Rm</td><td>Rd = Rn × Rm</td></tr>
<tr><td>SDIV</td><td>SDIV Rd, Rn, Rm</td><td>Rd = Rn / Rm (signé)</td></tr>
<tr><td>UDIV</td><td>UDIV Rd, Rn, Rm</td><td>Rd = Rn / Rm (non signé)</td></tr>
</table>

<p>Variantes avec flags : ADDS, SUBS (modifient NZCV).</p>

<p><strong>Instructions logiques</strong> :</p>

<table>
<tr><th>Instruction</th><th>Description</th></tr>
<tr><td>AND Rd, Rn, Rm</td><td>ET logique</td></tr>
<tr><td>ORR Rd, Rn, Rm</td><td>OU logique</td></tr>
<tr><td>EOR Rd, Rn, Rm</td><td>OU exclusif (XOR)</td></tr>
<tr><td>BIC Rd, Rn, Rm</td><td>Bit Clear (Rd = Rn AND NOT Rm)</td></tr>
<tr><td>MVN Rd, Rm</td><td>NOT (inversion)</td></tr>
</table>

<p><strong>Décalages</strong> :</p>

<table>
<tr><th>Instruction</th><th>Description</th></tr>
<tr><td>LSL Rd, Rn, #n</td><td>Logical Shift Left (décalage gauche)</td></tr>
<tr><td>LSR Rd, Rn, #n</td><td>Logical Shift Right (décalage droite, complète avec 0)</td></tr>
<tr><td>ASR Rd, Rn, #n</td><td>Arithmetic Shift Right (conserve le signe)</td></tr>
<tr><td>ROR Rd, Rn, #n</td><td>Rotate Right (rotation)</td></tr>
</table>

<p><strong>Déplacements de données</strong> :</p>

<pre><code class="language-asm">MOV R0,#42          ; R0 = 42 (immédiat)
MOV R1,R2           ; R1 = R2 (copie)
MOVW R0,#0x1234     ; Charge 16 bits bas
MOVT R0,#0x5678     ; Charge 16 bits haut → R0 = 0x56781234
</code></pre>

<h3 class="section-title">3. Accès Mémoire</h3>

<p><strong>Instructions de chargement</strong> :</p>

<table>
<tr><th>Instruction</th><th>Taille</th><th>Description</th></tr>
<tr><td>LDR Rd,[Rn]</td><td>32 bits</td><td>Charge mot</td></tr>
<tr><td>LDRH Rd,[Rn]</td><td>16 bits</td><td>Charge demi-mot (halfword)</td></tr>
<tr><td>LDRB Rd,[Rn]</td><td>8 bits</td><td>Charge octet (byte)</td></tr>
<tr><td>LDRSB Rd,[Rn]</td><td>8 bits signé</td><td>Charge octet avec extension de signe</td></tr>
<tr><td>LDRSH Rd,[Rn]</td><td>16 bits signé</td><td>Charge demi-mot avec extension de signe</td></tr>
</table>

<p><strong>Instructions de stockage</strong> :</p>

<table>
<tr><th>Instruction</th><th>Taille</th><th>Description</th></tr>
<tr><td>STR Rd,[Rn]</td><td>32 bits</td><td>Stocke mot</td></tr>
<tr><td>STRH Rd,[Rn]</td><td>16 bits</td><td>Stocke demi-mot</td></tr>
<tr><td>STRB Rd,[Rn]</td><td>8 bits</td><td>Stocke octet</td></tr>
</table>

<p><strong>Modes d'adressage</strong> :</p>

<pre><code class="language-asm">; Direct
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
</code></pre>

<h3 class="section-title">4. Contrôle de Flux</h3>

<p><strong>Branchements inconditionnels</strong> :</p>

<pre><code class="language-asm">B etiquette         ; Branchement simple
BL fonction         ; Branchement avec Link (LR = PC+4)
BX Rm               ; Branchement vers adresse dans Rm
BLX Rm              ; Branchement avec Link vers Rm
</code></pre>

<p><strong>Branchements conditionnels</strong> :</p>

<p>Basés sur les flags NZCV (Negative, Zero, Carry, oVerflow).</p>

<table>
<tr><th>Suffixe</th><th>Condition</th><th>Flags</th></tr>
<tr><td>EQ</td><td>Égal</td><td>Z=1</td></tr>
<tr><td>NE</td><td>Non égal</td><td>Z=0</td></tr>
<tr><td>GT</td><td>Supérieur (signé)</td><td>Z=0 ET N=V</td></tr>
<tr><td>LT</td><td>Inférieur (signé)</td><td>N≠V</td></tr>
<tr><td>GE</td><td>Supérieur ou égal (signé)</td><td>N=V</td></tr>
<tr><td>LE</td><td>Inférieur ou égal (signé)</td><td>Z=1 OU N≠V</td></tr>
<tr><td>HI</td><td>Supérieur (non signé)</td><td>C=1 ET Z=0</td></tr>
<tr><td>LS</td><td>Inférieur ou égal (non signé)</td><td>C=0 OU Z=1</td></tr>
</table>

<p><strong>Comparaisons</strong> :</p>

<pre><code class="language-asm">CMP R0,R1           ; Compare R0 et R1 (calcule R0-R1, met à jour flags)
CMN R0,R1           ; Compare negative (calcule R0+R1)
TST R0,R1           ; Test bits (AND, met à jour flags sans stocker)
TEQ R0,R1           ; Test equal (XOR, met à jour flags)
</code></pre>

<p><strong>Exemple de boucle</strong> :</p>

<pre><code class="language-asm">    MOV R0,#10      ; Compteur
Boucle
    ; ... code ...
    SUBS R0,#1      ; Décrément et mise à jour flags
    BNE Boucle      ; Tant que R0 != 0
</code></pre>

<h3 class="section-title">5. Sous-programmes et Pile</h3>

<p><strong>Convention d'appel AAPCS</strong> (ARM Architecture Procedure Call Standard) :</p>

<table>
<tr><th>Registre</th><th>Usage</th><th>Sauvegarde</th></tr>
<tr><td>R0-R3</td><td>Paramètres et retour</td><td>Caller-saved</td></tr>
<tr><td>R4-R11</td><td>Variables locales</td><td>Callee-saved</td></tr>
<tr><td>R12</td><td>Temporaire</td><td>Caller-saved</td></tr>
<tr><td>R13 (SP)</td><td>Pile</td><td>-</td></tr>
<tr><td>R14 (LR)</td><td>Adresse retour</td><td>-</td></tr>
</table>

<p><strong>Appel de fonction</strong> :</p>

<pre><code class="language-asm">; Appelant (caller)
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
</code></pre>

<p><strong>Gestion de la pile</strong> :</p>

<p>La pile croît vers les adresses décroissantes (full descending).</p>

<pre><code class="language-asm">PUSH {R0-R3,LR}     ; Sauvegarde multiple
; SP = SP - 20 (5 registres × 4 octets)

POP {R0-R3,PC}      ; Restauration et retour
; SP = SP + 20
</code></pre>

<p><strong>Équivalent</strong> :</p>
<ul>
<li>PUSH {Rx} = STMDB SP!, {Rx} (Store Multiple Decrement Before)</li>
<li>POP {Rx} = LDMIA SP!, {Rx} (Load Multiple Increment After)</li>
</ul>

<h3 class="section-title">6. Accès aux Périphériques</h3>

<p><strong>Memory-mapped I/O</strong> :</p>

<p>Les périphériques sont accessibles via des adresses mémoire spécifiques.</p>

<p><strong>Exemple : GPIO (General Purpose Input/Output)</strong></p>

<p>Registres du GPIOC (Port C) pour STM32F103 :</p>

<table>
<tr><th>Registre</th><th>Adresse</th><th>Usage</th></tr>
<tr><td>CRL</td><td>0x40011000</td><td>Configuration broches 0-7</td></tr>
<tr><td>CRH</td><td>0x40011004</td><td>Configuration broches 8-15</td></tr>
<tr><td>IDR</td><td>0x40011008</td><td>Input Data Register (lecture)</td></tr>
<tr><td>ODR</td><td>0x4001100C</td><td>Output Data Register (écriture)</td></tr>
<tr><td>BSRR</td><td>0x40011010</td><td>Bit Set/Reset Register</td></tr>
<tr><td>BRR</td><td>0x40011014</td><td>Bit Reset Register</td></tr>
</table>

<p><strong>Configuration d'une broche en sortie</strong> :</p>

<pre><code class="language-asm">; Configurer PC10 en sortie push-pull, 50 MHz
    LDR R0,=0x40011004  ; GPIOC_CRH
    LDR R1,[R0]
    BIC R1,#(0xF &lt;&lt; 8)  ; Clear bits pour PC10
    ORR R1,#(0x3 &lt;&lt; 8)  ; MODE=11 (50MHz), CNF=00 (push-pull)
    STR R1,[R0]
</code></pre>

<p><strong>Manipulation de bits</strong> :</p>

<pre><code class="language-asm">; Mise à 1 d'un bit (set)
LDR R0,=0x40011010  ; GPIOC_BSRR
MOV R1,#(1 &lt;&lt; 10)   ; Bit 10
STR R1,[R0]         ; PC10 = 1

; Mise à 0 d'un bit (reset)
LDR R0,=0x40011014  ; GPIOC_BRR
MOV R1,#(1 &lt;&lt; 10)
STR R1,[R0]         ; PC10 = 0

; Lecture d'un bit
LDR R0,=0x40011008  ; GPIOC_IDR
LDR R1,[R0]
TST R1,#(1 &lt;&lt; 8)    ; Test bit 8
BEQ Bit_A_Zero      ; Branch if zero
</code></pre>

<h3 class="section-title">7. Directives Assembleur</h3>

<p><strong>Organisation du code</strong> :</p>

<pre><code class="language-asm">    AREA MonCode, CODE, READONLY, ALIGN=2
    ; Sections de code

    AREA MesDonnees, DATA, READWRITE
    ; Sections de données
</code></pre>

<p><strong>Définition de données</strong> :</p>

<pre><code class="language-asm">; Constantes
Valeur  EQU 42          ; Équivalent #define

; Données initialisées
Tableau DCD 1,2,3,4,5   ; Define Constant Data (32 bits)
Chaine  DCB "Hello",0   ; Define Constant Byte (8 bits)
Mot     DCW 0x1234      ; Define Constant Word (16 bits)

; Données non initialisées
Buffer  SPACE 100       ; Réserve 100 octets
</code></pre>

<p><strong>Déclarations</strong> :</p>

<pre><code class="language-asm">    EXPORT main         ; Rend le symbole visible à l'extérieur
    IMPORT fonction     ; Importe un symbole externe

    PROC                ; Début de procédure
    ENDP                ; Fin de procédure

    END                 ; Fin du fichier source
</code></pre>

<h3 class="section-title">8. Optimisations</h3>

<p><strong>Taille de code</strong> :</p>

<p>Instructions Thumb-2 sont 16 ou 32 bits. Préférer les instructions 16 bits quand possible.</p>

<pre><code class="language-asm">; 16 bits
ADDS R0,R1,R2       ; Si R0-R7 et résultat modifie flags

; 32 bits
ADD.W R0,R1,R2      ; Force 32 bits
</code></pre>

<p><strong>Boucles efficaces</strong> :</p>

<pre><code class="language-asm">; Inefficace (compare à 0 à chaque itération)
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
</code></pre>

<p><strong>Éviter les branchements</strong> :</p>

<p>Utiliser les instructions conditionnelles quand possible.</p>

<pre><code class="language-asm">; Avec branchement
    CMP R0,R1
    BLE Suivant
    MOV R2,R0
Suivant
    ; ...

; Sans branchement (IT = If-Then)
    CMP R0,R1
    IT GT
    MOVGT R2,R0     ; Exécuté si GT
</code></pre>

<hr/>

<h2>PART D - Analyse Réflexive et Perspectives</h2>

<h3 class="section-title">Compétences acquises</h3>

<p><strong>Compréhension bas niveau</strong> :
La programmation en assembleur force à comprendre exactement ce qui se passe au niveau processeur : chaque instruction, chaque accès mémoire, chaque modification de flag. Cette compréhension aide à débugger et optimiser le code C.</p>

<p><strong>Contrôle total du matériel</strong> :
Accès direct aux registres de périphériques, manipulation bit à bit, timing précis. Essentiel pour développer des drivers ou du code temps réel critique.</p>

<p><strong>Optimisation</strong> :
Conscience du coût de chaque instruction. Savoir où optimiser (boucles critiques) et quand laisser le compilateur faire le travail.</p>

<h3 class="section-title">Points clés à retenir</h3>

<p><strong>1. La pile est votre amie (et votre ennemie)</strong> :
PUSH/POP doivent toujours être équilibrés. Oublier un POP ou faire POP du mauvais registre provoque des bugs difficiles à tracer.</p>

<p><strong>2. LR doit être sauvegardé</strong> :
Si une fonction appelle d'autres fonctions, LR doit être sauvegardé (PUSH {LR}) et restauré (POP {PC}) pour retourner correctement.</p>

<p><strong>3. Flags de condition</strong> :
Les instructions avec 'S' (ADDS, SUBS) modifient les flags. Nécessaire pour les branchements conditionnels. Attention à ne pas écraser les flags entre CMP et Bxx.</p>

<p><strong>4. Adressage mémoire</strong> :
Bien distinguer adresse et valeur. LDR R0,=etiquette charge l'adresse, LDR R0,[R1] charge la valeur à l'adresse contenue dans R1.</p>

<p><strong>5. Documentation indispensable</strong> :
Avoir toujours sous la main :</p>
<ul>
<li>ARM Architecture Reference Manual (jeu d'instructions)</li>
<li>STM32 Reference Manual (adresses périphériques)</li>
<li>Cortex-M3 Technical Reference Manual (architecture)</li>
</ul>

<h3 class="section-title">Applications pratiques</h3>

<p><strong>Systèmes embarqués critiques</strong> :
Bootloaders, routines d'initialisation, handlers d'interruption critiques. Code assembleur pour timing précis ou optimisation extrême.</p>

<p><strong>Drivers de périphériques</strong> :
Accès direct aux registres matériels pour performances maximales. Utile quand les HAL (Hardware Abstraction Layer) sont trop lourds.</p>

<p><strong>Reverse engineering</strong> :
Comprendre l'assembleur permet d'analyser du code compilé, débugger des problèmes obscurs, ou étudier des malwares.</p>

<p><strong>Inline assembly en C</strong> :
Intégrer quelques instructions assembleur dans du code C pour optimisations locales.</p>

<pre><code class="language-c">// Exemple inline assembly GCC
__asm volatile (
    "MOV R0, #42\n"
    "ADD R1, R0, R0\n"
    : "=r" (resultat)
    : "r" (entree)
    : "r0", "r1"
);
</code></pre>

<h3 class="section-title">Assembleur vs C</h3>

<p><strong>Quand utiliser l'assembleur</strong> :</p>
<ul>
<li>Code critique en temps (ISR ultra-rapides)</li>
<li>Optimisation extrême (boucles intensives)</li>
<li>Accès à des fonctionnalités spéciales (instructions SIMD)</li>
<li>Bootloaders et code d'initialisation</li>
<li>Taille de code très contrainte</li>
</ul>

<p><strong>Quand préférer le C</strong> :</p>
<ul>
<li>Développement rapide et maintenabilité</li>
<li>Portabilité entre architectures</li>
<li>Code métier complexe</li>
<li>95% des cas !</li>
</ul>

<p>Les compilateurs modernes optimisent très bien. L'assembleur manuel n'est souvent nécessaire que pour quelques pourcents du code.</p>

<h3 class="section-title">Retour d'expérience sur le projet TP</h3>

<p>Le projet "Roue Magique" a permis d'appliquer tous les concepts :</p>
<ul>
<li>Étape 1 : contrôle GPIO, découverte des registres</li>
<li>Étape 2 : lecture d'entrées, logique conditionnelle</li>
<li>Étape 3 : boucles et séquences</li>
<li>Étape 4 : timers et interruptions</li>
</ul>

<p><strong>Progression pédagogique</strong> :
Chaque étape ajoute de la complexité. On construit progressivement un système complet. Sentiment d'accomplissement en voyant les LEDs s'allumer selon notre code.</p>

<p><strong>Difficultés</strong> :
Débugger en assembleur est plus difficile qu'en C. Pas de printf facile. Utilisation intensive du debugger et de l'observation des registres.</p>

<h3 class="section-title">Limites et ouvertures</h3>

<p><strong>Limites du cours</strong> :</p>
<ul>
<li>Peu sur les interruptions avancées (NVIC complet)</li>
<li>Pas de DMA ou timers complexes</li>
<li>Peu de code optimisé (SIMD, DSP)</li>
<li>Pas de systèmes d'exploitation temps réel (RTOS)</li>
</ul>

<p><strong>Ouvertures vers</strong> :</p>
<ul>
<li><strong>Embedded C avancé</strong> : inline assembly, optimisations</li>
<li><strong>RTOS</strong> : FreeRTOS, tâches, synchronisation</li>
<li><strong>Compilation et linking</strong> : fichiers objets, éditeur de liens</li>
<li><strong>Architectures avancées</strong> : Cortex-M4 DSP, Cortex-M7 cache</li>
<li><strong>Sécurité</strong> : TrustZone, secure boot</li>
</ul>

<h3 class="section-title">Évolution technologique</h3>

<p><strong>Tendances actuelles</strong> :</p>
<ul>
<li><strong>Cortex-M33</strong> : TrustZone pour sécurité</li>
<li><strong>Cortex-M55</strong> : extensions Helium pour machine learning</li>
<li><strong>RISC-V</strong> : alternative open-source à ARM</li>
<li><strong>Compilation Just-In-Time</strong> : pour microcontrôleurs puissants</li>
</ul>

<p><strong>Outils modernes</strong> :</p>
<ul>
<li>CMSIS (Cortex Microcontroller Software Interface Standard)</li>
<li>HAL (Hardware Abstraction Layer) générées automatiquement</li>
<li>IDE graphiques (STM32CubeIDE, Mbed Studio)</li>
<li>Débogage avancé (Segger J-Link, Ozone)</li>
</ul>

<h3 class="section-title">Conclusion</h3>

<p>La programmation en assembleur ARM est un passage obligé pour comprendre en profondeur le fonctionnement des microcontrôleurs. Même si 95% du code moderne est écrit en C/C++, connaître l'assembleur permet :</p>
<ul>
<li>De mieux comprendre ce que fait le compilateur</li>
<li>D'optimiser le code critique</li>
<li>De débugger des problèmes complexes</li>
<li>De développer des drivers efficaces</li>
<li>D'apprécier la puissance des langages de haut niveau</li>
</ul>

<p>L'architecture ARM Cortex-M est omniprésente dans les systèmes embarqués modernes (IoT, wearables, drones, automobile). La maîtriser est un atout majeur pour tout ingénieur en systèmes embarqués.</p>

<p><strong>Recommandations</strong> :</p>
<ul>
<li>Pratiquer régulièrement (petits programmes, défis)</li>
<li>Lire du code assembleur généré par le compilateur (option -S de GCC)</li>
<li>Participer à des CTF (Capture The Flag) de reverse engineering</li>
<li>Expérimenter avec différentes architectures (ARM, RISC-V, x86)</li>
</ul>

<p><strong>Liens avec les autres cours</strong> :</p>
<ul>
<li><a href="./architecture-materielle.html">Architecture Matérielle - S6</a> : pipeline, cache</li>
<li><a href="./microcontroleur.html">Microcontrôleur - S6</a> : périphériques, C embarqué</li>
<li><a href="./electronique-fonctions-numeriques.html">Électronique Fonctions Numériques - S6</a> : bus I2C/SPI</li>
<li><a href="./temps-reel.html">Temps Réel - S8</a> : contraintes temporelles</li>
</ul>

<hr/>

<h2>📚 Documents de Cours</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>📖 Séquence 1 - Introduction ARM</h4>
      <p>Introduction à l'architecture ARM Cortex-M, registres, jeu d'instructions de base et organisation mémoire.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S6/ARM-Cortex/sequence1-introduction.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S6/ARM-Cortex/sequence1-introduction.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>📖 Séquence 2 - Instructions ARM</h4>
      <p>Jeu d'instructions ARM complet : arithmétique, logique, branchements, et modes d'adressage.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S6/ARM-Cortex/sequence2-instructions.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S6/ARM-Cortex/sequence2-instructions.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>📖 Séquence 3 - Fonctions et Pile</h4>
      <p>Convention d'appel AAPCS, gestion de la pile, prologue/épilogue de fonctions et passage de paramètres.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S6/ARM-Cortex/sequence3-fonctions.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S6/ARM-Cortex/sequence3-fonctions.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>📖 Référence Jeu d'Instructions</h4>
      <p>Tableau synthétique complet du jeu d'instructions ARM Cortex-M avec syntaxe et exemples.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S6/ARM-Cortex/jeu-instructions-arm.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S6/ARM-Cortex/jeu-instructions-arm.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
  </div>
</div>

<hr/>

<em>Cours enseigné en 2022-2023 à l'INSA Toulouse, Département Génie Électrique et Informatique.</em>

</div>

<!-- ==================== ENGLISH VERSION ==================== -->
<div class="lang-en">

<h1>⚙️ ARM CORTEX Assembly Language - Semester 6</h1>

<p><strong>Academic Year</strong>: 2022-2023<br/>
<strong>Semester</strong>: 6<br/>
<strong>Credits</strong>: 2 ECTS<br/>
<strong>Specialization</strong>: Embedded Systems and Low-Level Programming</p>

<hr/>

<h2>PART A - General Course Overview</h2>

<h3 class="section-title">Overview</h3>

<p>This course teaches assembly language programming for ARM Cortex-M microcontrollers (32-bit architecture). It covers processor architecture, the Thumb-2 instruction set, and low-level programming for embedded systems. Lab sessions use STM32F103 (Cortex-M3) with the Keil µVision development environment.</p>

<p><strong>Learning objectives</strong>:</p>
<ul>
<li>Understand ARM Cortex-M architecture (registers, pipeline, memory)</li>
<li>Master the Thumb-2 instruction set</li>
<li>Program in assembly (loops, functions, peripheral access)</li>
<li>Interface with hardware (GPIO, UART, timers)</li>
<li>Optimize code for performance and size</li>
</ul>

<h3 class="section-title">Position in the curriculum</h3>

<p>This course builds upon and deepens:</p>
<ul>
<li><strong>Computer Hardware Architecture (S5)</strong>: processor architecture fundamentals</li>
<li><strong>Hardware Architecture (S6)</strong>: ARM vs x86, pipeline, caches</li>
<li><strong>Microcontroller (S6)</strong>: peripherals and C programming</li>
</ul>

<p>It prepares for applications in:</p>
<ul>
<li><strong>Real-time embedded systems</strong>: critical and optimized code</li>
<li><strong>Driver development</strong>: direct hardware access</li>
<li><strong>Bootloaders and firmware</strong>: low-level code</li>
</ul>

<hr/>

<h2>PART B - Personal Experience and Learning Context</h2>

<h3 class="section-title">Organization and resources</h3>

<p>The module was structured into 4 progressive sequences:</p>

<p><strong>1. Sequence 1: ARM Cortex-M Architecture</strong></p>
<ul>
<li>Memory organization and registers</li>
<li>Pipeline and execution modes</li>
<li>AAPCS calling conventions</li>
</ul>

<p><strong>2. Sequence 2: Basic instruction set</strong></p>
<ul>
<li>Arithmetic and logic instructions</li>
<li>Data movement and memory load operations</li>
<li>Branches and loops</li>
</ul>

<p><strong>3. Sequence 3: Subroutines and stack</strong></p>
<ul>
<li>Function calls (BL, BX)</li>
<li>Stack management (PUSH, POP)</li>
<li>Parameter passing</li>
</ul>

<p><strong>4. Sequence 4: Peripheral access</strong></p>
<ul>
<li>Memory-mapped registers</li>
<li>GPIO control</li>
<li>UART communication</li>
<li>Interrupts</li>
</ul>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S6/arm-cortex/registres-arm.svg" alt="ARM Cortex-M Registers" style="max-width: 550px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: ARM Cortex-M register organization - R0-R15, SP, LR, PC and PSR</p>
</div>

<p><strong>Development environment</strong>:</p>
<ul>
<li><strong>IDE</strong>: Keil µVision 5</li>
<li><strong>Target</strong>: STM32F103RB (Cortex-M3, 128 KB Flash, 20 KB RAM)</li>
<li><strong>Simulator</strong>: cycle-accurate simulation without physical board</li>
<li><strong>Debugging</strong>: breakpoints, registers, memory, disassembly</li>
</ul>

<h3 class="section-title">Tutorials and lab sessions</h3>

<p><strong>Tutorial 2: Conversion and display</strong></p>

<p>Objective: read 4 digits from the keyboard, convert them to an integer, and display the result.</p>

<p><strong>Functions to implement</strong>:</p>

<pre><code class="language-asm">; Reading 4 characters via UART
BL GetKey_Echo      ; Reads a character and echoes it
STRB R0,[R7]        ; Stores in RAM memory

; ASCII → number conversion
LDRB R3,[R7],#1     ; Load character
SUB R3,#'0'         ; Convert '0'-'9' to 0-9
MOV R4,#10
MUL R3,R3,R4        ; Decimal shift

; String display
Affichaine PROC
    LDRB R0,[R3],#1  ; Load character
    CBZ R0,Fin       ; If 0, end of string
    BL SendChar      ; Send via UART
    B Car_suivant    ; Loop
Fin_Chaine
    POP {R0,PC}      ; Return
    ENDP
</code></pre>

<p><strong>Key concepts</strong>:</p>
<ul>
<li>Indirect addressing with post-increment: <code>[R7],#1</code></li>
<li>Calling convention: parameters in R0-R3</li>
<li>Context saving: PUSH/POP with LR</li>
</ul>

<p><strong>Tutorial 3: Array manipulation</strong></p>

<p>Working with integer arrays: sorting, searching, statistical calculations.</p>

<p><strong>Example: finding the maximum</strong></p>

<pre><code class="language-asm">; R0 = array address
; R1 = array size
; Return: R2 = maximum value

Recherche_Max PROC
    PUSH {R3,R4,LR}
    LDR R2,[R0],#4   ; First element = initial max
    SUBS R1,#1       ; Counter -1

Boucle
    LDR R3,[R0],#4   ; Next element
    CMP R3,R2
    BLE Suivant      ; If &lt;= max, skip to next
    MOV R2,R3        ; New max
Suivant
    SUBS R1,#1       ; Decrement counter
    BNE Boucle       ; While != 0

    POP {R3,R4,PC}
    ENDP
</code></pre>

<p><strong>Tutorial 4: Mathematical functions</strong></p>

<p>Implementation of complex operations (division, square root by successive approximations).</p>

<p><strong>Lab project: "Magic Wheel"</strong></p>

<p>A multi-step ongoing project to create an LED light show.</p>

<p><strong>Step 1: Controlling an LED</strong></p>

<pre><code class="language-asm">; Turn on an LED on PC10
Allume_LED PROC
    LDR R0,=0x40010C10  ; GPIOC_BSRR address (Bit Set Reset Register)
    MOV R1,#(0x01 &lt;&lt; 10) ; Bit 10 for PC10
    STR R1,[R0]          ; Write → LED on
    BX LR                ; Return
    ENDP

; Turn off the LED
Eteint_LED PROC
    LDR R2,=0x40010C14  ; GPIOC_BRR address (Bit Reset Register)
    MOV R3,#(0x01 &lt;&lt; 10)
    STR R3,[R2]
    BX LR
    ENDP
</code></pre>

<p><strong>Step 2: Reading a button</strong></p>

<pre><code class="language-asm">; Read button state on PB8
Capteur PROC
    LDR R4,=0x40010808   ; GPIOB_IDR address (Input Data Register)
    LDRH R5,[R4]         ; 16-bit read
    AND R5,R5,#0x0100    ; Mask bit 8
    CMP R5,#0
    BEQ Bouton_Presse    ; If 0, button pressed
    BX LR
    ENDP
</code></pre>

<p><strong>Step 3: LED sequence</strong></p>

<p>Blinking multiple LEDs in sequence (chaser pattern).</p>

<p><strong>Step 4: Interrupts and timers</strong></p>

<p>Using a timer to create precise delays without busy-waiting.</p>

<h3 class="section-title">Difficulties encountered</h3>

<p><strong>Stack management</strong>:
Forgetting to POP after PUSH causes function return errors. The LR (Link Register) must be saved if the function calls other functions.</p>

<p><strong>Memory addressing</strong>:
Confusion between address and value. LDR R0,=0x2000 loads the address, LDR R0,[R1] loads the value at the address contained in R1.</p>

<p><strong>Condition flags</strong>:
Instructions with 'S' (ADDS, SUBS) modify the NZCV flags. Required before CMP for conditional branches.</p>

<p><strong>Peripheral registers</strong>:
Specific addresses to memorize or use include files. STM32 documentation is essential.</p>

<hr/>

<h2>PART C - Detailed Technical Aspects</h2>

<h3 class="section-title">1. ARM Cortex-M3 Architecture</h3>

<p><strong>Register bank</strong>:</p>

<p>The Cortex-M3 has 16 32-bit registers:</p>

<table>
<tr><th>Register</th><th>Name</th><th>Usage</th></tr>
<tr><td>R0-R12</td><td>General purpose registers</td><td>Calculations, temporary data</td></tr>
<tr><td>R13 (SP)</td><td>Stack Pointer</td><td>Stack pointer</td></tr>
<tr><td>R14 (LR)</td><td>Link Register</td><td>Function return address</td></tr>
<tr><td>R15 (PC)</td><td>Program Counter</td><td>Current instruction address</td></tr>
</table>

<p><strong>Special registers</strong>:</p>
<ul>
<li><strong>PSR</strong> (Program Status Register): N, Z, C, V flags, mode, exceptions</li>
<li><strong>PRIMASK</strong>: global interrupt mask</li>
<li><strong>CONTROL</strong>: stack selection, privilege level</li>
</ul>

<p><strong>Memory organization</strong>:</p>

<table>
<tr><th>Region</th><th>Addresses</th><th>Usage</th></tr>
<tr><td>Code</td><td>0x00000000 - 0x1FFFFFFF</td><td>Flash, instructions</td></tr>
<tr><td>SRAM</td><td>0x20000000 - 0x3FFFFFFF</td><td>RAM, data</td></tr>
<tr><td>Peripherals</td><td>0x40000000 - 0x5FFFFFFF</td><td>Memory-mapped registers</td></tr>
<tr><td>System</td><td>0xE0000000 - 0xFFFFFFFF</td><td>NVIC, SysTick, debug</td></tr>
</table>

<p><strong>3-stage pipeline</strong>:</p>
<ol>
<li>Fetch: instruction read</li>
<li>Decode: decoding</li>
<li>Execute: execution</li>
</ol>

<p>Consequence: the PC always points 2 instructions ahead (PC+4 in Thumb-2).</p>

<h3 class="section-title">2. Thumb-2 Instruction Set</h3>

<p><strong>Arithmetic instructions</strong>:</p>

<table>
<tr><th>Instruction</th><th>Syntax</th><th>Description</th></tr>
<tr><td>ADD</td><td>ADD Rd, Rn, Rm</td><td>Rd = Rn + Rm</td></tr>
<tr><td>SUB</td><td>SUB Rd, Rn, Rm</td><td>Rd = Rn - Rm</td></tr>
<tr><td>MUL</td><td>MUL Rd, Rn, Rm</td><td>Rd = Rn × Rm</td></tr>
<tr><td>SDIV</td><td>SDIV Rd, Rn, Rm</td><td>Rd = Rn / Rm (signed)</td></tr>
<tr><td>UDIV</td><td>UDIV Rd, Rn, Rm</td><td>Rd = Rn / Rm (unsigned)</td></tr>
</table>

<p>Variants with flags: ADDS, SUBS (modify NZCV).</p>

<p><strong>Logic instructions</strong>:</p>

<table>
<tr><th>Instruction</th><th>Description</th></tr>
<tr><td>AND Rd, Rn, Rm</td><td>Logical AND</td></tr>
<tr><td>ORR Rd, Rn, Rm</td><td>Logical OR</td></tr>
<tr><td>EOR Rd, Rn, Rm</td><td>Exclusive OR (XOR)</td></tr>
<tr><td>BIC Rd, Rn, Rm</td><td>Bit Clear (Rd = Rn AND NOT Rm)</td></tr>
<tr><td>MVN Rd, Rm</td><td>NOT (inversion)</td></tr>
</table>

<p><strong>Shifts</strong>:</p>

<table>
<tr><th>Instruction</th><th>Description</th></tr>
<tr><td>LSL Rd, Rn, #n</td><td>Logical Shift Left</td></tr>
<tr><td>LSR Rd, Rn, #n</td><td>Logical Shift Right (fills with 0)</td></tr>
<tr><td>ASR Rd, Rn, #n</td><td>Arithmetic Shift Right (preserves sign)</td></tr>
<tr><td>ROR Rd, Rn, #n</td><td>Rotate Right</td></tr>
</table>

<p><strong>Data movement</strong>:</p>

<pre><code class="language-asm">MOV R0,#42          ; R0 = 42 (immediate)
MOV R1,R2           ; R1 = R2 (copy)
MOVW R0,#0x1234     ; Load lower 16 bits
MOVT R0,#0x5678     ; Load upper 16 bits → R0 = 0x56781234
</code></pre>

<h3 class="section-title">3. Memory Access</h3>

<p><strong>Load instructions</strong>:</p>

<table>
<tr><th>Instruction</th><th>Size</th><th>Description</th></tr>
<tr><td>LDR Rd,[Rn]</td><td>32 bits</td><td>Load word</td></tr>
<tr><td>LDRH Rd,[Rn]</td><td>16 bits</td><td>Load halfword</td></tr>
<tr><td>LDRB Rd,[Rn]</td><td>8 bits</td><td>Load byte</td></tr>
<tr><td>LDRSB Rd,[Rn]</td><td>8 bits signed</td><td>Load byte with sign extension</td></tr>
<tr><td>LDRSH Rd,[Rn]</td><td>16 bits signed</td><td>Load halfword with sign extension</td></tr>
</table>

<p><strong>Store instructions</strong>:</p>

<table>
<tr><th>Instruction</th><th>Size</th><th>Description</th></tr>
<tr><td>STR Rd,[Rn]</td><td>32 bits</td><td>Store word</td></tr>
<tr><td>STRH Rd,[Rn]</td><td>16 bits</td><td>Store halfword</td></tr>
<tr><td>STRB Rd,[Rn]</td><td>8 bits</td><td>Store byte</td></tr>
</table>

<p><strong>Addressing modes</strong>:</p>

<pre><code class="language-asm">; Direct
LDR R0,[R1]         ; R0 = mem[R1]

; Offset
LDR R0,[R1,#8]      ; R0 = mem[R1+8]

; Pre-indexed
LDR R0,[R1,#8]!     ; R1 = R1+8, then R0 = mem[R1]

; Post-indexed
LDR R0,[R1],#8      ; R0 = mem[R1], then R1 = R1+8

; Register-indexed
LDR R0,[R1,R2]      ; R0 = mem[R1+R2]

; PC-relative (literal pool)
LDR R0,=0x20000000  ; Load address via constant pool
</code></pre>

<h3 class="section-title">4. Flow Control</h3>

<p><strong>Unconditional branches</strong>:</p>

<pre><code class="language-asm">B label             ; Simple branch
BL function         ; Branch with Link (LR = PC+4)
BX Rm               ; Branch to address in Rm
BLX Rm              ; Branch with Link to Rm
</code></pre>

<p><strong>Conditional branches</strong>:</p>

<p>Based on NZCV flags (Negative, Zero, Carry, oVerflow).</p>

<table>
<tr><th>Suffix</th><th>Condition</th><th>Flags</th></tr>
<tr><td>EQ</td><td>Equal</td><td>Z=1</td></tr>
<tr><td>NE</td><td>Not equal</td><td>Z=0</td></tr>
<tr><td>GT</td><td>Greater than (signed)</td><td>Z=0 AND N=V</td></tr>
<tr><td>LT</td><td>Less than (signed)</td><td>N!=V</td></tr>
<tr><td>GE</td><td>Greater than or equal (signed)</td><td>N=V</td></tr>
<tr><td>LE</td><td>Less than or equal (signed)</td><td>Z=1 OR N!=V</td></tr>
<tr><td>HI</td><td>Higher (unsigned)</td><td>C=1 AND Z=0</td></tr>
<tr><td>LS</td><td>Lower or same (unsigned)</td><td>C=0 OR Z=1</td></tr>
</table>

<p><strong>Comparisons</strong>:</p>

<pre><code class="language-asm">CMP R0,R1           ; Compare R0 and R1 (computes R0-R1, updates flags)
CMN R0,R1           ; Compare negative (computes R0+R1)
TST R0,R1           ; Test bits (AND, updates flags without storing)
TEQ R0,R1           ; Test equal (XOR, updates flags)
</code></pre>

<p><strong>Loop example</strong>:</p>

<pre><code class="language-asm">    MOV R0,#10      ; Counter
Boucle
    ; ... code ...
    SUBS R0,#1      ; Decrement and update flags
    BNE Boucle      ; While R0 != 0
</code></pre>

<h3 class="section-title">5. Subroutines and Stack</h3>

<p><strong>AAPCS calling convention</strong> (ARM Architecture Procedure Call Standard):</p>

<table>
<tr><th>Register</th><th>Usage</th><th>Preservation</th></tr>
<tr><td>R0-R3</td><td>Parameters and return</td><td>Caller-saved</td></tr>
<tr><td>R4-R11</td><td>Local variables</td><td>Callee-saved</td></tr>
<tr><td>R12</td><td>Temporary</td><td>Caller-saved</td></tr>
<tr><td>R13 (SP)</td><td>Stack</td><td>-</td></tr>
<tr><td>R14 (LR)</td><td>Return address</td><td>-</td></tr>
</table>

<p><strong>Function call</strong>:</p>

<pre><code class="language-asm">; Caller
    MOV R0,#5       ; First parameter
    MOV R1,#10      ; Second parameter
    BL MaFonction   ; Call (LR = return address)
    ; R0 contains the result

; Function (callee)
MaFonction PROC
    PUSH {R4,LR}    ; Save used registers

    ; Calculations using R0, R1, R4
    ADD R4,R0,R1
    MOV R0,R4       ; Result in R0

    POP {R4,PC}     ; Restore and return
    ENDP
</code></pre>

<p><strong>Stack management</strong>:</p>

<p>The stack grows toward lower addresses (full descending).</p>

<pre><code class="language-asm">PUSH {R0-R3,LR}     ; Multiple save
; SP = SP - 20 (5 registers × 4 bytes)

POP {R0-R3,PC}      ; Restore and return
; SP = SP + 20
</code></pre>

<p><strong>Equivalent</strong>:</p>
<ul>
<li>PUSH {Rx} = STMDB SP!, {Rx} (Store Multiple Decrement Before)</li>
<li>POP {Rx} = LDMIA SP!, {Rx} (Load Multiple Increment After)</li>
</ul>

<h3 class="section-title">6. Peripheral Access</h3>

<p><strong>Memory-mapped I/O</strong>:</p>

<p>Peripherals are accessible via specific memory addresses.</p>

<p><strong>Example: GPIO (General Purpose Input/Output)</strong></p>

<p>GPIOC (Port C) registers for STM32F103:</p>

<table>
<tr><th>Register</th><th>Address</th><th>Usage</th></tr>
<tr><td>CRL</td><td>0x40011000</td><td>Configuration for pins 0-7</td></tr>
<tr><td>CRH</td><td>0x40011004</td><td>Configuration for pins 8-15</td></tr>
<tr><td>IDR</td><td>0x40011008</td><td>Input Data Register (read)</td></tr>
<tr><td>ODR</td><td>0x4001100C</td><td>Output Data Register (write)</td></tr>
<tr><td>BSRR</td><td>0x40011010</td><td>Bit Set/Reset Register</td></tr>
<tr><td>BRR</td><td>0x40011014</td><td>Bit Reset Register</td></tr>
</table>

<p><strong>Configuring a pin as output</strong>:</p>

<pre><code class="language-asm">; Configure PC10 as push-pull output, 50 MHz
    LDR R0,=0x40011004  ; GPIOC_CRH
    LDR R1,[R0]
    BIC R1,#(0xF &lt;&lt; 8)  ; Clear bits for PC10
    ORR R1,#(0x3 &lt;&lt; 8)  ; MODE=11 (50MHz), CNF=00 (push-pull)
    STR R1,[R0]
</code></pre>

<p><strong>Bit manipulation</strong>:</p>

<pre><code class="language-asm">; Set a bit (set)
LDR R0,=0x40011010  ; GPIOC_BSRR
MOV R1,#(1 &lt;&lt; 10)   ; Bit 10
STR R1,[R0]         ; PC10 = 1

; Clear a bit (reset)
LDR R0,=0x40011014  ; GPIOC_BRR
MOV R1,#(1 &lt;&lt; 10)
STR R1,[R0]         ; PC10 = 0

; Read a bit
LDR R0,=0x40011008  ; GPIOC_IDR
LDR R1,[R0]
TST R1,#(1 &lt;&lt; 8)    ; Test bit 8
BEQ Bit_A_Zero      ; Branch if zero
</code></pre>

<h3 class="section-title">7. Assembler Directives</h3>

<p><strong>Code organization</strong>:</p>

<pre><code class="language-asm">    AREA MonCode, CODE, READONLY, ALIGN=2
    ; Code sections

    AREA MesDonnees, DATA, READWRITE
    ; Data sections
</code></pre>

<p><strong>Data definitions</strong>:</p>

<pre><code class="language-asm">; Constants
Valeur  EQU 42          ; Equivalent to #define

; Initialized data
Tableau DCD 1,2,3,4,5   ; Define Constant Data (32 bits)
Chaine  DCB "Hello",0   ; Define Constant Byte (8 bits)
Mot     DCW 0x1234      ; Define Constant Word (16 bits)

; Uninitialized data
Buffer  SPACE 100       ; Reserve 100 bytes
</code></pre>

<p><strong>Declarations</strong>:</p>

<pre><code class="language-asm">    EXPORT main         ; Make symbol visible externally
    IMPORT fonction     ; Import an external symbol

    PROC                ; Procedure start
    ENDP                ; Procedure end

    END                 ; End of source file
</code></pre>

<h3 class="section-title">8. Optimizations</h3>

<p><strong>Code size</strong>:</p>

<p>Thumb-2 instructions are 16 or 32 bits. Prefer 16-bit instructions when possible.</p>

<pre><code class="language-asm">; 16 bits
ADDS R0,R1,R2       ; If R0-R7 and result modifies flags

; 32 bits
ADD.W R0,R1,R2      ; Force 32 bits
</code></pre>

<p><strong>Efficient loops</strong>:</p>

<pre><code class="language-asm">; Inefficient (compares to 0 on every iteration)
    MOV R0,#0
Boucle
    ; ...
    ADD R0,#1
    CMP R0,#100
    BLT Boucle

; Efficient (decrement and implicitly test for zero)
    MOV R0,#100
Boucle
    ; ...
    SUBS R0,#1
    BNE Boucle
</code></pre>

<p><strong>Avoiding branches</strong>:</p>

<p>Use conditional instructions when possible.</p>

<pre><code class="language-asm">; With branch
    CMP R0,R1
    BLE Suivant
    MOV R2,R0
Suivant
    ; ...

; Without branch (IT = If-Then)
    CMP R0,R1
    IT GT
    MOVGT R2,R0     ; Executed if GT
</code></pre>

<hr/>

<h2>PART D - Reflective Analysis and Perspectives</h2>

<h3 class="section-title">Skills acquired</h3>

<p><strong>Low-level understanding</strong>:
Assembly programming forces you to understand exactly what happens at the processor level: every instruction, every memory access, every flag modification. This understanding helps debug and optimize C code.</p>

<p><strong>Total hardware control</strong>:
Direct access to peripheral registers, bit-level manipulation, precise timing. Essential for developing drivers or time-critical real-time code.</p>

<p><strong>Optimization</strong>:
Awareness of the cost of each instruction. Knowing where to optimize (critical loops) and when to let the compiler do the work.</p>

<h3 class="section-title">Key takeaways</h3>

<p><strong>1. The stack is your friend (and your enemy)</strong>:
PUSH/POP must always be balanced. Forgetting a POP or popping the wrong register causes bugs that are difficult to trace.</p>

<p><strong>2. LR must be saved</strong>:
If a function calls other functions, LR must be saved (PUSH {LR}) and restored (POP {PC}) to return correctly.</p>

<p><strong>3. Condition flags</strong>:
Instructions with 'S' (ADDS, SUBS) modify the flags. Required for conditional branches. Be careful not to overwrite flags between CMP and Bxx.</p>

<p><strong>4. Memory addressing</strong>:
Clearly distinguish between address and value. LDR R0,=label loads the address, LDR R0,[R1] loads the value at the address contained in R1.</p>

<p><strong>5. Documentation is essential</strong>:
Always have at hand:</p>
<ul>
<li>ARM Architecture Reference Manual (instruction set)</li>
<li>STM32 Reference Manual (peripheral addresses)</li>
<li>Cortex-M3 Technical Reference Manual (architecture)</li>
</ul>

<h3 class="section-title">Practical applications</h3>

<p><strong>Critical embedded systems</strong>:
Bootloaders, initialization routines, critical interrupt handlers. Assembly code for precise timing or extreme optimization.</p>

<p><strong>Peripheral drivers</strong>:
Direct access to hardware registers for maximum performance. Useful when HALs (Hardware Abstraction Layers) are too heavy.</p>

<p><strong>Reverse engineering</strong>:
Understanding assembly allows analyzing compiled code, debugging obscure issues, or studying malware.</p>

<p><strong>Inline assembly in C</strong>:
Integrating a few assembly instructions in C code for local optimizations.</p>

<pre><code class="language-c">// GCC inline assembly example
__asm volatile (
    "MOV R0, #42\n"
    "ADD R1, R0, R0\n"
    : "=r" (result)
    : "r" (input)
    : "r0", "r1"
);
</code></pre>

<h3 class="section-title">Assembly vs C</h3>

<p><strong>When to use assembly</strong>:</p>
<ul>
<li>Time-critical code (ultra-fast ISRs)</li>
<li>Extreme optimization (intensive loops)</li>
<li>Access to special features (SIMD instructions)</li>
<li>Bootloaders and initialization code</li>
<li>Very constrained code size</li>
</ul>

<p><strong>When to prefer C</strong>:</p>
<ul>
<li>Rapid development and maintainability</li>
<li>Portability across architectures</li>
<li>Complex business logic</li>
<li>95% of cases!</li>
</ul>

<p>Modern compilers optimize very well. Hand-written assembly is often only necessary for a few percent of the code.</p>

<h3 class="section-title">Lab project feedback</h3>

<p>The "Magic Wheel" project allowed applying all concepts:</p>
<ul>
<li>Step 1: GPIO control, register discovery</li>
<li>Step 2: input reading, conditional logic</li>
<li>Step 3: loops and sequences</li>
<li>Step 4: timers and interrupts</li>
</ul>

<p><strong>Pedagogical progression</strong>:
Each step adds complexity. We progressively build a complete system. A sense of accomplishment when seeing the LEDs light up according to our code.</p>

<p><strong>Difficulties</strong>:
Debugging in assembly is harder than in C. No easy printf. Intensive use of the debugger and register observation.</p>

<h3 class="section-title">Limitations and future directions</h3>

<p><strong>Course limitations</strong>:</p>
<ul>
<li>Little coverage of advanced interrupts (full NVIC)</li>
<li>No DMA or complex timers</li>
<li>Little optimized code (SIMD, DSP)</li>
<li>No real-time operating systems (RTOS)</li>
</ul>

<p><strong>Future directions</strong>:</p>
<ul>
<li><strong>Advanced Embedded C</strong>: inline assembly, optimizations</li>
<li><strong>RTOS</strong>: FreeRTOS, tasks, synchronization</li>
<li><strong>Compilation and linking</strong>: object files, linker</li>
<li><strong>Advanced architectures</strong>: Cortex-M4 DSP, Cortex-M7 cache</li>
<li><strong>Security</strong>: TrustZone, secure boot</li>
</ul>

<h3 class="section-title">Technological evolution</h3>

<p><strong>Current trends</strong>:</p>
<ul>
<li><strong>Cortex-M33</strong>: TrustZone for security</li>
<li><strong>Cortex-M55</strong>: Helium extensions for machine learning</li>
<li><strong>RISC-V</strong>: open-source alternative to ARM</li>
<li><strong>Just-In-Time compilation</strong>: for powerful microcontrollers</li>
</ul>

<p><strong>Modern tools</strong>:</p>
<ul>
<li>CMSIS (Cortex Microcontroller Software Interface Standard)</li>
<li>HAL (Hardware Abstraction Layer) generated automatically</li>
<li>Graphical IDEs (STM32CubeIDE, Mbed Studio)</li>
<li>Advanced debugging (Segger J-Link, Ozone)</li>
</ul>

<h3 class="section-title">Conclusion</h3>

<p>ARM assembly programming is an essential step for deeply understanding how microcontrollers work. Even though 95% of modern code is written in C/C++, knowing assembly allows you to:</p>
<ul>
<li>Better understand what the compiler does</li>
<li>Optimize critical code</li>
<li>Debug complex problems</li>
<li>Develop efficient drivers</li>
<li>Appreciate the power of high-level languages</li>
</ul>

<p>The ARM Cortex-M architecture is ubiquitous in modern embedded systems (IoT, wearables, drones, automotive). Mastering it is a major asset for any embedded systems engineer.</p>

<p><strong>Recommendations</strong>:</p>
<ul>
<li>Practice regularly (small programs, challenges)</li>
<li>Read compiler-generated assembly code (GCC -S option)</li>
<li>Participate in reverse engineering CTFs (Capture The Flag)</li>
<li>Experiment with different architectures (ARM, RISC-V, x86)</li>
</ul>

<p><strong>Links to other courses</strong>:</p>
<ul>
<li><a href="./architecture-materielle.html">Hardware Architecture - S6</a>: pipeline, cache</li>
<li><a href="./microcontroleur.html">Microcontroller - S6</a>: peripherals, embedded C</li>
<li><a href="./electronique-fonctions-numeriques.html">Digital Electronics - S6</a>: I2C/SPI bus</li>
<li><a href="./temps-reel.html">Real-Time Systems - S8</a>: timing constraints</li>
</ul>

<hr/>

<h2>📚 Course Documents</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>📖 Sequence 1 - ARM Introduction</h4>
      <p>Introduction to ARM Cortex-M architecture, registers, basic instruction set and memory organization.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S6/ARM-Cortex/sequence1-introduction.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S6/ARM-Cortex/sequence1-introduction.pdf" target="_blank">📥 Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>📖 Sequence 2 - ARM Instructions</h4>
      <p>Complete ARM instruction set: arithmetic, logic, branches, and addressing modes.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S6/ARM-Cortex/sequence2-instructions.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S6/ARM-Cortex/sequence2-instructions.pdf" target="_blank">📥 Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>📖 Sequence 3 - Functions and Stack</h4>
      <p>AAPCS calling convention, stack management, function prologue/epilogue and parameter passing.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S6/ARM-Cortex/sequence3-fonctions.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S6/ARM-Cortex/sequence3-fonctions.pdf" target="_blank">📥 Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>📖 Instruction Set Reference</h4>
      <p>Complete summary table of the ARM Cortex-M instruction set with syntax and examples.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S6/ARM-Cortex/jeu-instructions-arm.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S6/ARM-Cortex/jeu-instructions-arm.pdf" target="_blank">📥 Download</a></p>
    </div>
  </div>
</div>

<hr/>

<em>Course taught in 2022-2023 at INSA Toulouse, Department of Electrical and Computer Engineering.</em>

</div>

<div class="back-nav">
    <a href="./my-courses-2022-2023.html" data-i18n-html="back-courses-2022-2023">← Retour aux Cours 2022-2023</a>
</div>

<em class="lang-fr">Rédigé par Cédric Chanfreau, étudiant en ingénierie à l'INSA Toulouse.</em><em class="lang-en">Written by Cédric Chanfreau, engineering student at INSA Toulouse.</em>

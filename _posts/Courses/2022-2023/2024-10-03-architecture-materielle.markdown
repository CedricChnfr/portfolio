---
layout: default
title: "Architecture Matérielle - S6"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
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
</style>

<div class="back-nav">
  <a href="./my-courses-2022-2023.html">← Retour à Mes Cours 2022-2023</a>
</div>

# 🔧 Architecture Matérielle - S6

**Année**: 2022-2023 (Semestre 6)  
**Crédits**: 3 ECTS  
**Type**: Architecture et Systèmes Embarqués

---

## PART A: PRÉSENTATION GÉNÉRALE

### Objectifs du cours

Ce cours approfondit l'architecture des processeurs modernes en se concentrant sur les architectures ARM et x86, la programmation assembleur, les mécanismes de pipeline et les aspects de sécurité matérielle. L'accent est mis sur la compréhension bas niveau du fonctionnement des processeurs et les vulnérabilités matérielles.

### Compétences visées

- Comprendre les architectures ARM et x86/x64
- Programmer en assembleur ARM et x86
- Maîtriser les mécanismes de pipeline et parallélisme
- Analyser les performances des processeurs
- Comprendre la hiérarchie mémoire et les caches
- Identifier les vulnérabilités matérielles
- Analyser les attaques par canaux cachés
- Optimiser le code pour l'architecture cible
- Comprendre les compromis énergie/performance

### Organisation

- **Volume horaire**: Cours magistraux et TPs pratiques
- **Évaluation**: Examen écrit + compte-rendu de TP
- **Semestre**: 6 (2022-2023)
- **Prérequis**: Architecture de base, programmation C, systèmes d'exploitation

---

## PART B: EXPÉRIENCE, CONTEXTE ET FONCTION

### Contenu pédagogique

Le cours couvre les architectures modernes et leurs implications sécuritaires.

#### 1. Programmation Assembleur

**Introduction à l'assembleur**:

L'assembleur est le langage de plus bas niveau (avant le binaire).

Avantages:
- Contrôle total du processeur
- Performances optimales
- Compréhension du fonctionnement matériel
- Débogage bas niveau
- Reverse engineering

Utilisations:
- Noyaux de systèmes d'exploitation
- Drivers de périphériques
- Code critique en performance
- Systèmes embarqués
- Sécurité et cryptographie

**Structure d'un programme assembleur**:

Sections typiques:
- **Section .data**: données initialisées
- **Section .bss**: données non initialisées
- **Section .text**: code exécutable

**Registres**:

Mémoires ultra-rapides dans le processeur.

Types:
- Registres généraux (calculs, données)
- Pointeur de pile (SP - Stack Pointer)
- Compteur ordinal (PC - Program Counter)
- Registre d'état (flags)

#### 2. Architecture ARM

**Caractéristiques ARM**:

ARM (Advanced RISC Machine) est l'architecture dominante dans l'embarqué et mobile.

Principes RISC (Reduced Instruction Set Computer):
- Instructions simples et uniformes
- Exécution rapide (1 cycle par instruction)
- Nombreux registres
- Architecture load/store

**Registres ARM**:

| Registre | Nom | Fonction |
|----------|-----|----------|
| R0-R12 | Registres généraux | Calculs et données |
| R13 (SP) | Stack Pointer | Pointeur de pile |
| R14 (LR) | Link Register | Adresse de retour |
| R15 (PC) | Program Counter | Adresse instruction courante |
| CPSR | Current Program Status | Flags d'état |

**Instructions de base ARM**:

```armasm
; Mouvement de données
MOV R0, #5          ; R0 = 5
LDR R1, [R2]        ; R1 = mémoire[R2]
STR R0, [R1]        ; mémoire[R1] = R0

; Arithmétique
ADD R0, R1, R2      ; R0 = R1 + R2
SUB R0, R1, #10     ; R0 = R1 - 10
MUL R0, R1, R2      ; R0 = R1 × R2

; Logique
AND R0, R1, R2      ; R0 = R1 ET R2
ORR R0, R1, R2      ; R0 = R1 OU R2
EOR R0, R1, R2      ; R0 = R1 XOR R2

; Comparaison et branchements
CMP R0, R1          ; Compare R0 et R1
BEQ label           ; Branche si égal
BNE label           ; Branche si différent
BL fonction         ; Appel de fonction
```

**Convention d'appel ARM**:

- R0-R3: passage des 4 premiers arguments
- R0: valeur de retour
- R4-R11: sauvegardés par la fonction appelée
- LR (R14): adresse de retour

**Exemple de fonction ARM**:

```armasm
; Fonction addition: int add(int a, int b)
add:
    PUSH {LR}           ; Sauvegarder LR
    ADD R0, R0, R1      ; R0 = R0 + R1 (résultat)
    POP {PC}            ; Retour (restaure PC)

; Appel de la fonction
MOV R0, #5
MOV R1, #3
BL add                  ; Appel add(5, 3)
; R0 contient 8
```

#### 3. Architecture x86/x64

**Caractéristiques x86**:

x86 (Intel/AMD) est l'architecture dominante sur PC et serveurs.

Principes CISC (Complex Instruction Set Computer):
- Instructions complexes et variées
- Durée d'exécution variable
- Moins de registres
- Mémoire directement accessible

**Registres x86-64**:

| Registre | 64 bits | 32 bits | 16 bits | 8 bits | Usage |
|----------|---------|---------|---------|--------|-------|
| RAX | RAX | EAX | AX | AL | Accumulateur, retour |
| RBX | RBX | EBX | BX | BL | Base |
| RCX | RCX | ECX | CX | CL | Compteur |
| RDX | RDX | EDX | DX | DL | Données |
| RSI | RSI | ESI | SI | - | Source index |
| RDI | RDI | EDI | DI | - | Destination index |
| RBP | RBP | EBP | BP | - | Base pointer (pile) |
| RSP | RSP | ESP | SP | - | Stack pointer |
| R8-R15 | - | - | - | - | Registres additionnels |

**Instructions de base x86**:

```nasm
; Mouvement de données
mov rax, 5          ; rax = 5
mov rbx, [rax]      ; rbx = mémoire[rax]
lea rax, [rbx+8]    ; rax = adresse rbx+8

; Arithmétique
add rax, rbx        ; rax = rax + rbx
sub rax, 10         ; rax = rax - 10
imul rax, rbx       ; rax = rax × rbx
idiv rcx            ; rax = rax / rcx, rdx = reste

; Logique
and rax, rbx        ; rax = rax ET rbx
or rax, rbx         ; rax = rax OU rbx
xor rax, rax        ; rax = 0 (idiome courant)
not rax             ; rax = NON rax

; Pile
push rax            ; Empiler rax
pop rbx             ; Dépiler dans rbx

; Branchements
cmp rax, rbx        ; Comparer
je label            ; Jump if equal
jne label           ; Jump if not equal
jmp label           ; Jump inconditionnel
call fonction       ; Appel fonction
ret                 ; Retour
```

**Convention d'appel x64 (System V)**:

Arguments dans l'ordre:
1. RDI
2. RSI
3. RDX
4. RCX
5. R8
6. R9
7. Puis sur la pile

Valeur de retour: RAX

**Exemple de fonction x64**:

```nasm
; Fonction: int add(int a, int b)
add:
    push rbp            ; Prologue
    mov rbp, rsp
    
    mov eax, edi        ; a dans eax
    add eax, esi        ; eax += b
    
    pop rbp             ; Épilogue
    ret
```

**Comparaison ARM vs x86**:

| Aspect | ARM | x86 |
|--------|-----|-----|
| Philosophie | RISC | CISC |
| Instructions | Simples, régulières | Complexes, variées |
| Longueur instruction | Fixe (32 bits) | Variable (1-15 octets) |
| Registres | 16 (ARM32) | 16 (x64) |
| Consommation | Faible | Élevée |
| Performance/Watt | Excellente | Moyenne |
| Usage | Mobile, embarqué | PC, serveurs |

#### 4. Pipeline et parallélisme

**Pipeline d'instructions**:

Technique permettant d'exécuter plusieurs instructions en parallèle.

Étapes classiques (5 stages):
1. **IF** (Instruction Fetch): lecture instruction
2. **ID** (Instruction Decode): décodage
3. **EX** (Execute): exécution
4. **MEM** (Memory): accès mémoire
5. **WB** (Write Back): écriture résultat

Sans pipeline: 5 cycles par instruction.
Avec pipeline: 1 instruction/cycle en régime permanent.

**Aléas de pipeline** (hazards):

**Aléas structurels**:
Conflit sur une ressource matérielle.
Solution: dupliquer ressources.

**Aléas de données**:
Instruction dépend d'un résultat pas encore disponible.

Exemple:
```
ADD R1, R2, R3    ; R1 = R2 + R3
SUB R4, R1, R5    ; R4 = R1 - R5 (dépend de R1!)
```

Solutions:
- **Stall** (bulles): attendre
- **Forwarding**: transmettre résultat directement
- **Réorganisation**: ordonnanceur réarrange les instructions

**Aléas de contrôle**:

Branchements conditionnels perturbent le pipeline.

Le processeur ne sait pas quelle instruction charger après un branchement.

Solutions:
- **Prédiction de branchement**: deviner la direction
- **Exécution spéculative**: exécuter les deux chemins
- **Branch delay slot**: instruction après branchement toujours exécutée

**Architectures superscalaires**:

Plusieurs pipelines en parallèle → plusieurs instructions/cycle.

Exemples: processeurs modernes (4-6 instructions/cycle).

**Exécution dans le désordre (out-of-order)**:

Le processeur réordonne les instructions pour maximiser l'utilisation des unités fonctionnelles.

Masque les latences et améliore IPC (Instructions Per Cycle).

**Parallélisme au niveau instruction (ILP)**:

Exploitation automatique du parallélisme dans le code séquentiel.

Techniques:
- Pipeline
- Superscalaire
- Out-of-order execution
- Prédiction de branchement
- Renommage de registres

#### 5. Hiérarchie mémoire

**Pyramide mémoire**:

| Niveau | Taille | Latence | Coût |
|--------|--------|---------|------|
| Registres | Quelques octets | < 1 ns | Très élevé |
| Cache L1 | 32-64 KB | 1-2 ns | Élevé |
| Cache L2 | 256 KB - 1 MB | 5-10 ns | Moyen |
| Cache L3 | 4-32 MB | 20-40 ns | Bas |
| RAM | 4-64 GB | 50-100 ns | Très bas |
| SSD | 256 GB - 2 TB | 0.1 ms | Minimal |
| HDD | 1-10 TB | 10 ms | Minimal |

Principe de localité:
- **Temporelle**: donnée récemment utilisée sera probablement réutilisée
- **Spatiale**: données proches seront probablement utilisées ensemble

**Mémoire cache**:

Mémoire rapide entre processeur et RAM.

**Organisation**:

**Direct-mapped**: chaque adresse RAM a une seule place possible dans le cache.
- Simple mais conflits fréquents

**Set-associative**: chaque adresse a N places possibles.
- Bon compromis (2-way, 4-way, 8-way courant)

**Fully-associative**: adresse peut aller n'importe où.
- Flexible mais complexe et coûteux

**Politiques de remplacement**:

Quand le cache est plein, quelle ligne évincer?

- **LRU** (Least Recently Used): la moins récemment utilisée
- **FIFO**: la plus ancienne
- **Random**: au hasard
- **LFU** (Least Frequently Used): la moins fréquemment utilisée

**Politiques d'écriture**:

**Write-through**:
- Écriture simultanée cache + RAM
- Cohérence garantie
- Lent

**Write-back**:
- Écriture uniquement dans cache
- RAM mise à jour lors de l'éviction
- Rapide mais complexe
- Bit "dirty" pour tracer modifications

**Cohérence de cache**:

Dans un système multiprocesseur, comment garantir que tous les caches voient les mêmes données?

Protocoles MESI, MOESI: états des lignes de cache (Modified, Exclusive, Shared, Invalid).

#### 6. Sécurité matérielle et attaques

**Vulnérabilités matérielles**:

Le matériel n'est pas infaillible et peut être exploité.

**Attaques par canaux cachés** (side-channel attacks):

Exploitation d'informations indirectes (temps, consommation, émissions électromagnétiques).

**Attaque temporelle (timing attack)**:

Mesure du temps d'exécution pour déduire des informations secrètes.

Exemple: cache timing.

Si une donnée est en cache, l'accès est rapide.
Si elle n'y est pas, l'accès est lent.

En mesurant le temps, un attaquant peut déduire quelles données ont été accédées.

**Attaque Spectre**:

Exploite l'exécution spéculative et la prédiction de branchement.

Principe:
1. Entraîner le prédicteur de branchement
2. Faire exécuter spéculativement du code qui accède à des données sensibles
3. Observer effet de bord via cache timing
4. Récupérer données secrètes

Impact: fuite d'informations entre processus, contournement d'isolation mémoire.

**Attaque Meltdown**:

Exploite le délai entre vérification des permissions et annulation d'une instruction spéculative.

Permet à un processus utilisateur de lire la mémoire noyau.

Impact majeur: tous les processeurs Intel récents vulnérables.

Mitigation: KPTI (Kernel Page Table Isolation) avec coût en performance.

**Attaque par analyse de consommation**:

Mesure de la consommation électrique pour extraire des clés cryptographiques.

Types:
- **SPA** (Simple Power Analysis): observation directe
- **DPA** (Differential Power Analysis): analyse statistique

Cibles privilégiées: cartes à puce, systèmes embarqués.

Contre-mesures:
- Masquage (randomisation)
- Équilibrage de la consommation
- Opérations à temps constant

**Attaques électromagnétiques**:

Écoute des émissions EM du processeur.

Similaire aux attaques par consommation mais sans contact.

**Contre-mesures générales**:

- Conception sécurisée du matériel
- Patches microcode
- Modifications d'OS (KPTI)
- Code à temps constant
- Masquage et randomisation
- Enclaves sécurisées (Intel SGX, ARM TrustZone)

#### 7. Processeurs multi-cœurs

**Évolution vers le parallélisme**:

Fin de la loi de Moore: fréquences plafonnées (≈4-5 GHz).

Solution: multiplier les cœurs.

**Architectures multi-cœurs**:

| Nombre de cœurs | Usage typique |
|-----------------|---------------|
| 2-4 | Laptop, mobile |
| 4-8 | Desktop |
| 8-64 | Serveur |
| 64+ | Calcul haute performance |

**Symétrie (SMP)**:

Tous les cœurs identiques, partagent la mémoire.

**Asymétrie (AMP)**:

Cœurs de types différents (ex: ARM big.LITTLE).

Cœurs rapides (big) pour tâches lourdes.
Cœurs économes (LITTLE) pour tâches légères.

Optimise rapport performance/consommation.

**Hyperthreading (SMT)**:

Un cœur physique apparaît comme plusieurs cœurs logiques.

Partage des unités fonctionnelles entre threads.

Gain: 20-30% de performances.

**Affinité processeur**:

Lier un processus à un cœur spécifique.

Avantages:
- Meilleure utilisation du cache
- Prédictibilité temps réel
- Isolation pour sécurité

---

## PART C: ASPECTS TECHNIQUES

### Travaux Pratiques

**TP: Comparaison ARM et x86/x64**

Objectif: comprendre les différences entre architectures par la pratique.

**Exercices typiques**:

**1. Programme simple en ARM et x86**:

Écrire la même fonction dans les deux assembleurs.

Exemple: calcul de factorielle.

ARM:
```armasm
factorial:
    PUSH {R4, LR}
    MOV R4, R0          ; Sauver n
    CMP R0, #1
    BLE end_fact
    SUB R0, R0, #1
    BL factorial        ; Appel récursif
    MUL R0, R4, R0      ; n * fact(n-1)
end_fact:
    POP {R4, PC}
```

x86-64:
```nasm
factorial:
    push rbp
    mov rbp, rsp
    cmp rdi, 1
    jle end_fact
    push rdi
    dec rdi
    call factorial
    pop rdi
    imul rax, rdi
end_fact:
    pop rbp
    ret
```

**2. Analyse de performances**:

Mesurer le temps d'exécution de différentes implémentations.

Comparer:
- Code C optimisé
- Assembleur manuel
- Différentes optimisations

**3. Utilisation du cache**:

Écrire du code exploitant bien le cache vs mal.

Bon usage: parcours séquentiel d'un tableau.
Mauvais usage: accès aléatoires.

**4. Étude de vulnérabilités**:

Implémenter une attaque simple de type cache timing.

Observer la différence de temps entre:
- Donnée en cache
- Donnée pas en cache

### Outils et environnement

**Assembleurs**:
```bash
# ARM
arm-none-eabi-as programme.s -o programme.o
arm-none-eabi-ld programme.o -o programme

# x86-64
nasm -f elf64 programme.asm
ld programme.o -o programme

# Ou via GCC
gcc -S programme.c          # Générer assembleur
gcc -c programme.s          # Assembler
```

**Désassemblage**:
```bash
objdump -d programme        # Désassembler
objdump -S programme        # Avec code source entrelacé
gdb programme               # Débogueur
```

**Analyse de performances**:
```bash
perf stat ./programme       # Statistiques performances
perf record ./programme     # Enregistrer profil
perf report                 # Analyser profil

# Compteurs matériels
perf stat -e cache-misses,cache-references ./programme
```

**Simulation**:
```bash
qemu-arm programme          # Émuler ARM
qemu-x86_64 programme       # Émuler x86-64
```

### Optimisations assembleur

**Techniques courantes**:

**Déroulage de boucles** (loop unrolling):
```c
// Original
for(i=0; i<100; i++)
    a[i] = b[i] + c[i];

// Déroulé
for(i=0; i<100; i+=4) {
    a[i] = b[i] + c[i];
    a[i+1] = b[i+1] + c[i+1];
    a[i+2] = b[i+2] + c[i+2];
    a[i+3] = b[i+3] + c[i+3];
}
```

Avantages: moins de tests, meilleure utilisation pipeline.

**Vectorisation** (SIMD):

Traiter plusieurs données simultanément.

ARM NEON, x86 SSE/AVX: opérations sur 128-512 bits.

**Réorganisation pour le cache**:

Accéder aux données dans l'ordre de leur disposition en mémoire.

**Élimination de branchements**:

Remplacer if par calculs arithmétiques/logiques.

Exemple:
```c
// Avec branchement
if(x > 0) y = a; else y = b;

// Sans branchement (x86)
mov eax, a
mov ebx, b
cmp x, 0
cmovg eax, ebx  ; Conditional move
```

---

## PART D: ANALYSE ET RÉFLEXION

### Compétences acquises

**Programmation bas niveau**:
- Maîtrise de l'assembleur ARM et x86
- Compréhension du lien entre C et assembleur
- Optimisation de code critique
- Débogage au niveau matériel

**Architecture**:
- Compréhension des pipelines modernes
- Connaissance des hiérarchies mémoire
- Fonctionnement des caches
- Parallélisme matériel et multi-cœurs

**Sécurité**:
- Identification de vulnérabilités matérielles
- Compréhension des attaques par canaux cachés
- Conscience des compromis sécurité/performance
- Analyse de risques au niveau matériel

### Applications pratiques

L'architecture matérielle impacte tous les domaines de l'informatique:

**Systèmes embarqués**:
- Programmation ARM pour microcontrôleurs
- Optimisation pour contraintes (mémoire, énergie)
- Systèmes temps réel critiques
- IoT et objets connectés

**Sécurité**:
- Analyse de malwares (reverse engineering)
- Cryptographie résistante aux attaques physiques
- Systèmes sécurisés (cartes à puce, TPM)
- Détection d'attaques matérielles

**Performances**:
- Optimisation de code critique (jeux, calcul scientifique)
- Exploitation efficace du matériel (caches, SIMD)
- Parallélisation sur multi-cœurs
- Réduction de la consommation énergétique

**Développement système**:
- Noyaux de systèmes d'exploitation
- Drivers de périphériques
- Bootloaders et firmware
- Hyperviseurs et virtualisation

### Liens avec autres cours

| Cours | Lien |
|-------|------|
| Architecture Informatique (S5) | Bases de l'architecture |
| Systèmes d'Exploitation (S5) | Lien avec le logiciel système |
| Langage C (S5) | Compilation vers assembleur |
| Microcontrôleur (S6) | Programmation ARM pratique |
| Sécurité Matérielle (S7) | Approfondissement sécurité |
| Temps Réel (S8) | Optimisation et prédictibilité |

### Évolution des architectures

**Tendances actuelles**:

**Efficacité énergétique**:

Performance par Watt devient critique.

ARM domine mobile et commence à s'imposer en datacenter (AWS Graviton, Apple M1/M2).

**Architectures hétérogènes**:

Combinaison de processeurs différents:
- CPU généralistes
- GPU pour calcul parallèle
- NPU (Neural Processing Unit) pour IA
- Accélérateurs spécialisés (crypto, codecs)

**RISC-V**:

Architecture ouverte alternative à ARM et x86.

Adoption croissante dans l'embarqué et la recherche.

**Calcul quantique**:

Architectures radicalement différentes.

Encore expérimental mais prometteur pour certains problèmes.

**Mémoire non-volatile**:

Technologies émergentes (MRAM, ReRAM, 3D XPoint).

Floutent la distinction RAM/stockage.

### Sécurité: un défi permanent

**Leçons des vulnérabilités récentes**:

Spectre/Meltdown ont révélé:
- Optimisations de performance créent failles sécurité
- Corrections logicielles coûteuses en performance
- Nécessité de repenser conception matérielle

**Design sécurisé**:

Principes émergents:
- Sécurité dès la conception (security by design)
- Isolation matérielle renforcée
- Enclaves sécurisées
- Vérification formelle

**Compromis inévitables**:

Performance vs Sécurité:
- Désactiver fonctionnalités (hyperthreading)
- Isolation coûteuse (KPTI)
- Opérations à temps constant plus lentes

### Mon opinion

Ce cours est essentiel pour comprendre le fonctionnement réel des ordinateurs.

**Points forts**:
- Vision concrète du matériel
- Compréhension des optimisations compilateur
- Conscience des enjeux de sécurité
- Programmation assembleur formatrice

**Importance professionnelle**:

Ces connaissances sont critiques pour:
- Systèmes embarqués à contraintes fortes
- Optimisation de code haute performance
- Sécurité informatique (analyse, conception)
- Compréhension des architectures émergentes

**Assembleur aujourd'hui**:

Bien que rarement écrit directement, comprendre l'assembleur permet:
- Lire le code généré par le compilateur
- Optimiser les sections critiques
- Déboguer les problèmes bas niveau
- Analyser des binaires (reverse engineering)

**ARM vs x86: bataille intéressante**:

ARM:
- Domine mobile/embarqué
- Perce dans les datacenters
- Efficacité énergétique supérieure
- Apple M1/M2 impressionnants

x86:
- Toujours dominant sur PC/serveurs
- Puissance brute élevée
- Écosystème mature
- Rétrocompatibilité précieuse

**Sécurité matérielle: priorité croissante**:

Les attaques matérielles sont de plus en plus sophistiquées.

Nécessite:
- Formation des développeurs
- Outils d'analyse adaptés
- Conception consciente des risques
- Veille technologique constante

**Futur des architectures**:

Vers plus de:
- Spécialisation (accélérateurs IA, crypto)
- Hétérogénéité (big.LITTLE généralisé)
- Efficacité énergétique
- Sécurité intégrée

---

**Bilan personnel**: Ce cours a fourni une compréhension approfondie du fonctionnement bas niveau des processeurs modernes. La programmation assembleur ARM et x86 a permis de voir concrètement comment le code s'exécute sur le matériel. La prise de conscience des vulnérabilités matérielles (Spectre, Meltdown) et des attaques par canaux cachés est particulièrement importante pour concevoir des systèmes sécurisés. Ces connaissances sont directement applicables en développement embarqué, optimisation de performances, et analyse de sécurité. La comparaison ARM/x86 éclaire sur les compromis architecturaux et l'évolution future de l'informatique.

---

<style>
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
</style>

## 📚 Documents de Cours

<style>
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

## Rapports et Projets

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Compte Rendu TP - Architecture Matérielle</h4>
      <p>Rapport de travaux pratiques sur la comparaison des architectures ARM et x86/x64, la programmation assembleur et l'analyse de performances.</p>
      <p style="text-align: center;">
        <a href="/file/reports/S6/Compte rendu Architecture MatÚrielle.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Télécharger le rapport PDF
        </a>
      </p>
    </div>
  </div>
</div>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>📖 Introduction à l'Assembleur</h4>
      <p>Cours complet sur les langages assembleurs, leur rôle et leur utilisation dans l'architecture des processeurs.</p>
      <embed src="/cours-pdf/S6/Architecture-Materielle/assembleur.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Architecture-Materielle/assembleur.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>📖 Comparaison ARM vs x86</h4>
      <p>Étude comparative des architectures ARM et x86/x64 : instructions, registres, conventions d'appel et performances.</p>
      <embed src="/cours-pdf/S6/Architecture-Materielle/arm-x86.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Architecture-Materielle/arm-x86.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>📖 Introduction aux Attaques Matérielles</h4>
      <p>Présentation des vulnérabilités matérielles et des attaques par canaux cachés (Spectre, Meltdown, timing attacks).</p>
      <embed src="/cours-pdf/S6/Architecture-Materielle/intro-attaques.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Architecture-Materielle/intro-attaques.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>📖 Attaques par Consommation Énergétique</h4>
      <p>Analyse détaillée des attaques SPA et DPA sur circuits cryptographiques via l'analyse de consommation électrique.</p>
      <embed src="/cours-pdf/S6/Architecture-Materielle/attaque-consommation.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Architecture-Materielle/attaque-consommation.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
  </div>
</div>

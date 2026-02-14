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

<div class="lang-fr">

<h1>Architecture Materielle - S6</h1>

<p><strong>Annee</strong>: 2022-2023 (Semestre 6)<br/>
<strong>Credits</strong>: 3 ECTS<br/>
<strong>Type</strong>: Architecture et Systemes Embarques</p>

<hr/>

<h2>PART A: PRESENTATION GENERALE</h2>

<h3>Objectifs du cours</h3>

<p>Ce cours approfondit l'architecture des processeurs modernes en se concentrant sur les architectures ARM et x86, la programmation assembleur, les mecanismes de pipeline et les aspects de securite materielle. L'accent est mis sur la comprehension bas niveau du fonctionnement des processeurs et les vulnerabilites materielles.</p>

<h3>Competences visees</h3>

<ul>
  <li>Comprendre les architectures ARM et x86/x64</li>
  <li>Programmer en assembleur ARM et x86</li>
  <li>Maitriser les mecanismes de pipeline et parallelisme</li>
  <li>Analyser les performances des processeurs</li>
  <li>Comprendre la hierarchie memoire et les caches</li>
  <li>Identifier les vulnerabilites materielles</li>
  <li>Analyser les attaques par canaux caches</li>
  <li>Optimiser le code pour l'architecture cible</li>
  <li>Comprendre les compromis energie/performance</li>
</ul>

<h3>Organisation</h3>

<ul>
  <li><strong>Volume horaire</strong>: Cours magistraux et TPs pratiques</li>
  <li><strong>Evaluation</strong>: Examen ecrit + compte-rendu de TP</li>
  <li><strong>Semestre</strong>: 6 (2022-2023)</li>
  <li><strong>Prerequis</strong>: Architecture de base, programmation C, systemes d'exploitation</li>
</ul>

<hr/>

<h2>PART B: EXPERIENCE, CONTEXTE ET FONCTION</h2>

<h3>Contenu pedagogique</h3>

<p>Le cours couvre les architectures modernes et leurs implications securitaires.</p>

<h4>1. Programmation Assembleur</h4>

<p><strong>Introduction a l'assembleur</strong>:</p>

<p>L'assembleur est le langage de plus bas niveau (avant le binaire).</p>

<p>Avantages:</p>
<ul>
  <li>Controle total du processeur</li>
  <li>Performances optimales</li>
  <li>Comprehension du fonctionnement materiel</li>
  <li>Debogage bas niveau</li>
  <li>Reverse engineering</li>
</ul>

<p>Utilisations:</p>
<ul>
  <li>Noyaux de systemes d'exploitation</li>
  <li>Drivers de peripheriques</li>
  <li>Code critique en performance</li>
  <li>Systemes embarques</li>
  <li>Securite et cryptographie</li>
</ul>

<p><strong>Structure d'un programme assembleur</strong>:</p>

<p>Sections typiques:</p>
<ul>
  <li><strong>Section .data</strong>: donnees initialisees</li>
  <li><strong>Section .bss</strong>: donnees non initialisees</li>
  <li><strong>Section .text</strong>: code executable</li>
</ul>

<p><strong>Registres</strong>:</p>

<p>Memoires ultra-rapides dans le processeur.</p>

<p>Types:</p>
<ul>
  <li>Registres generaux (calculs, donnees)</li>
  <li>Pointeur de pile (SP - Stack Pointer)</li>
  <li>Compteur ordinal (PC - Program Counter)</li>
  <li>Registre d'etat (flags)</li>
</ul>

<h4>2. Architecture ARM</h4>

<p><strong>Caracteristiques ARM</strong>:</p>

<p>ARM (Advanced RISC Machine) est l'architecture dominante dans l'embarque et mobile.</p>

<p>Principes RISC (Reduced Instruction Set Computer):</p>
<ul>
  <li>Instructions simples et uniformes</li>
  <li>Execution rapide (1 cycle par instruction)</li>
  <li>Nombreux registres</li>
  <li>Architecture load/store</li>
</ul>

<p><strong>Registres ARM</strong>:</p>

<table>
  <thead>
    <tr><th>Registre</th><th>Nom</th><th>Fonction</th></tr>
  </thead>
  <tbody>
    <tr><td>R0-R12</td><td>Registres generaux</td><td>Calculs et donnees</td></tr>
    <tr><td>R13 (SP)</td><td>Stack Pointer</td><td>Pointeur de pile</td></tr>
    <tr><td>R14 (LR)</td><td>Link Register</td><td>Adresse de retour</td></tr>
    <tr><td>R15 (PC)</td><td>Program Counter</td><td>Adresse instruction courante</td></tr>
    <tr><td>CPSR</td><td>Current Program Status</td><td>Flags d'etat</td></tr>
  </tbody>
</table>

<p><strong>Instructions de base ARM</strong>:</p>

<pre><code>; Mouvement de donnees
MOV R0, #5          ; R0 = 5
LDR R1, [R2]        ; R1 = memoire[R2]
STR R0, [R1]        ; memoire[R1] = R0

; Arithmetique
ADD R0, R1, R2      ; R0 = R1 + R2
SUB R0, R1, #10     ; R0 = R1 - 10
MUL R0, R1, R2      ; R0 = R1 x R2

; Logique
AND R0, R1, R2      ; R0 = R1 ET R2
ORR R0, R1, R2      ; R0 = R1 OU R2
EOR R0, R1, R2      ; R0 = R1 XOR R2

; Comparaison et branchements
CMP R0, R1          ; Compare R0 et R1
BEQ label           ; Branche si egal
BNE label           ; Branche si different
BL fonction         ; Appel de fonction</code></pre>

<p><strong>Convention d'appel ARM</strong>:</p>
<ul>
  <li>R0-R3: passage des 4 premiers arguments</li>
  <li>R0: valeur de retour</li>
  <li>R4-R11: sauvegardes par la fonction appelee</li>
  <li>LR (R14): adresse de retour</li>
</ul>

<p><strong>Exemple de fonction ARM</strong>:</p>

<pre><code>; Fonction addition: int add(int a, int b)
add:
    PUSH {LR}           ; Sauvegarder LR
    ADD R0, R0, R1      ; R0 = R0 + R1 (resultat)
    POP {PC}            ; Retour (restaure PC)

; Appel de la fonction
MOV R0, #5
MOV R1, #3
BL add                  ; Appel add(5, 3)
; R0 contient 8</code></pre>

<h4>3. Architecture x86/x64</h4>

<p><strong>Caracteristiques x86</strong>:</p>

<p>x86 (Intel/AMD) est l'architecture dominante sur PC et serveurs.</p>

<p>Principes CISC (Complex Instruction Set Computer):</p>
<ul>
  <li>Instructions complexes et variees</li>
  <li>Duree d'execution variable</li>
  <li>Moins de registres</li>
  <li>Memoire directement accessible</li>
</ul>

<p><strong>Registres x86-64</strong>:</p>

<table>
  <thead>
    <tr><th>Registre</th><th>64 bits</th><th>32 bits</th><th>16 bits</th><th>8 bits</th><th>Usage</th></tr>
  </thead>
  <tbody>
    <tr><td>RAX</td><td>RAX</td><td>EAX</td><td>AX</td><td>AL</td><td>Accumulateur, retour</td></tr>
    <tr><td>RBX</td><td>RBX</td><td>EBX</td><td>BX</td><td>BL</td><td>Base</td></tr>
    <tr><td>RCX</td><td>RCX</td><td>ECX</td><td>CX</td><td>CL</td><td>Compteur</td></tr>
    <tr><td>RDX</td><td>RDX</td><td>EDX</td><td>DX</td><td>DL</td><td>Donnees</td></tr>
    <tr><td>RSI</td><td>RSI</td><td>ESI</td><td>SI</td><td>-</td><td>Source index</td></tr>
    <tr><td>RDI</td><td>RDI</td><td>EDI</td><td>DI</td><td>-</td><td>Destination index</td></tr>
    <tr><td>RBP</td><td>RBP</td><td>EBP</td><td>BP</td><td>-</td><td>Base pointer (pile)</td></tr>
    <tr><td>RSP</td><td>RSP</td><td>ESP</td><td>SP</td><td>-</td><td>Stack pointer</td></tr>
    <tr><td>R8-R15</td><td>-</td><td>-</td><td>-</td><td>-</td><td>Registres additionnels</td></tr>
  </tbody>
</table>

<p><strong>Instructions de base x86</strong>:</p>

<pre><code>; Mouvement de donnees
mov rax, 5          ; rax = 5
mov rbx, [rax]      ; rbx = memoire[rax]
lea rax, [rbx+8]    ; rax = adresse rbx+8

; Arithmetique
add rax, rbx        ; rax = rax + rbx
sub rax, 10         ; rax = rax - 10
imul rax, rbx       ; rax = rax x rbx
idiv rcx            ; rax = rax / rcx, rdx = reste

; Logique
and rax, rbx        ; rax = rax ET rbx
or rax, rbx         ; rax = rax OU rbx
xor rax, rax        ; rax = 0 (idiome courant)
not rax             ; rax = NON rax

; Pile
push rax            ; Empiler rax
pop rbx             ; Depiler dans rbx

; Branchements
cmp rax, rbx        ; Comparer
je label            ; Jump if equal
jne label           ; Jump if not equal
jmp label           ; Jump inconditionnel
call fonction       ; Appel fonction
ret                 ; Retour</code></pre>

<p><strong>Convention d'appel x64 (System V)</strong>:</p>

<p>Arguments dans l'ordre:</p>
<ol>
  <li>RDI</li>
  <li>RSI</li>
  <li>RDX</li>
  <li>RCX</li>
  <li>R8</li>
  <li>R9</li>
  <li>Puis sur la pile</li>
</ol>

<p>Valeur de retour: RAX</p>

<p><strong>Exemple de fonction x64</strong>:</p>

<pre><code>; Fonction: int add(int a, int b)
add:
    push rbp            ; Prologue
    mov rbp, rsp

    mov eax, edi        ; a dans eax
    add eax, esi        ; eax += b

    pop rbp             ; Epilogue
    ret</code></pre>

<p><strong>Comparaison ARM vs x86</strong>:</p>

<table>
  <thead>
    <tr><th>Aspect</th><th>ARM</th><th>x86</th></tr>
  </thead>
  <tbody>
    <tr><td>Philosophie</td><td>RISC</td><td>CISC</td></tr>
    <tr><td>Instructions</td><td>Simples, regulieres</td><td>Complexes, variees</td></tr>
    <tr><td>Longueur instruction</td><td>Fixe (32 bits)</td><td>Variable (1-15 octets)</td></tr>
    <tr><td>Registres</td><td>16 (ARM32)</td><td>16 (x64)</td></tr>
    <tr><td>Consommation</td><td>Faible</td><td>Elevee</td></tr>
    <tr><td>Performance/Watt</td><td>Excellente</td><td>Moyenne</td></tr>
    <tr><td>Usage</td><td>Mobile, embarque</td><td>PC, serveurs</td></tr>
  </tbody>
</table>

<h4>4. Pipeline et parallelisme</h4>

<p><strong>Pipeline d'instructions</strong>:</p>

<p>Technique permettant d'executer plusieurs instructions en parallele.</p>

<p>Etapes classiques (5 stages):</p>
<ol>
  <li><strong>IF</strong> (Instruction Fetch): lecture instruction</li>
  <li><strong>ID</strong> (Instruction Decode): decodage</li>
  <li><strong>EX</strong> (Execute): execution</li>
  <li><strong>MEM</strong> (Memory): acces memoire</li>
  <li><strong>WB</strong> (Write Back): ecriture resultat</li>
</ol>

<p>Sans pipeline: 5 cycles par instruction.<br/>
Avec pipeline: 1 instruction/cycle en regime permanent.</p>

<p><strong>Aleas de pipeline</strong> (hazards):</p>

<p><strong>Aleas structurels</strong>:</p>
<p>Conflit sur une ressource materielle.<br/>
Solution: dupliquer ressources.</p>

<p><strong>Aleas de donnees</strong>:</p>
<p>Instruction depend d'un resultat pas encore disponible.</p>

<p>Exemple:</p>
<pre><code>ADD R1, R2, R3    ; R1 = R2 + R3
SUB R4, R1, R5    ; R4 = R1 - R5 (depend de R1!)</code></pre>

<p>Solutions:</p>
<ul>
  <li><strong>Stall</strong> (bulles): attendre</li>
  <li><strong>Forwarding</strong>: transmettre resultat directement</li>
  <li><strong>Reorganisation</strong>: ordonnanceur rearrange les instructions</li>
</ul>

<p><strong>Aleas de controle</strong>:</p>

<p>Branchements conditionnels perturbent le pipeline.</p>

<p>Le processeur ne sait pas quelle instruction charger apres un branchement.</p>

<p>Solutions:</p>
<ul>
  <li><strong>Prediction de branchement</strong>: deviner la direction</li>
  <li><strong>Execution speculative</strong>: executer les deux chemins</li>
  <li><strong>Branch delay slot</strong>: instruction apres branchement toujours executee</li>
</ul>

<p><strong>Architectures superscalaires</strong>:</p>

<p>Plusieurs pipelines en parallele &rarr; plusieurs instructions/cycle.</p>

<p>Exemples: processeurs modernes (4-6 instructions/cycle).</p>

<p><strong>Execution dans le desordre (out-of-order)</strong>:</p>

<p>Le processeur reordonne les instructions pour maximiser l'utilisation des unites fonctionnelles.</p>

<p>Masque les latences et ameliore IPC (Instructions Per Cycle).</p>

<p><strong>Parallelisme au niveau instruction (ILP)</strong>:</p>

<p>Exploitation automatique du parallelisme dans le code sequentiel.</p>

<p>Techniques:</p>
<ul>
  <li>Pipeline</li>
  <li>Superscalaire</li>
  <li>Out-of-order execution</li>
  <li>Prediction de branchement</li>
  <li>Renommage de registres</li>
</ul>

<h4>5. Hierarchie memoire</h4>

<p><strong>Pyramide memoire</strong>:</p>

<table>
  <thead>
    <tr><th>Niveau</th><th>Taille</th><th>Latence</th><th>Cout</th></tr>
  </thead>
  <tbody>
    <tr><td>Registres</td><td>Quelques octets</td><td>&lt; 1 ns</td><td>Tres eleve</td></tr>
    <tr><td>Cache L1</td><td>32-64 KB</td><td>1-2 ns</td><td>Eleve</td></tr>
    <tr><td>Cache L2</td><td>256 KB - 1 MB</td><td>5-10 ns</td><td>Moyen</td></tr>
    <tr><td>Cache L3</td><td>4-32 MB</td><td>20-40 ns</td><td>Bas</td></tr>
    <tr><td>RAM</td><td>4-64 GB</td><td>50-100 ns</td><td>Tres bas</td></tr>
    <tr><td>SSD</td><td>256 GB - 2 TB</td><td>0.1 ms</td><td>Minimal</td></tr>
    <tr><td>HDD</td><td>1-10 TB</td><td>10 ms</td><td>Minimal</td></tr>
  </tbody>
</table>

<p>Principe de localite:</p>
<ul>
  <li><strong>Temporelle</strong>: donnee recemment utilisee sera probablement reutilisee</li>
  <li><strong>Spatiale</strong>: donnees proches seront probablement utilisees ensemble</li>
</ul>

<p><strong>Memoire cache</strong>:</p>

<p>Memoire rapide entre processeur et RAM.</p>

<p><strong>Organisation</strong>:</p>

<p><strong>Direct-mapped</strong>: chaque adresse RAM a une seule place possible dans le cache.</p>
<ul><li>Simple mais conflits frequents</li></ul>

<p><strong>Set-associative</strong>: chaque adresse a N places possibles.</p>
<ul><li>Bon compromis (2-way, 4-way, 8-way courant)</li></ul>

<p><strong>Fully-associative</strong>: adresse peut aller n'importe ou.</p>
<ul><li>Flexible mais complexe et couteux</li></ul>

<p><strong>Politiques de remplacement</strong>:</p>

<p>Quand le cache est plein, quelle ligne evincer?</p>
<ul>
  <li><strong>LRU</strong> (Least Recently Used): la moins recemment utilisee</li>
  <li><strong>FIFO</strong>: la plus ancienne</li>
  <li><strong>Random</strong>: au hasard</li>
  <li><strong>LFU</strong> (Least Frequently Used): la moins frequemment utilisee</li>
</ul>

<p><strong>Politiques d'ecriture</strong>:</p>

<p><strong>Write-through</strong>:</p>
<ul>
  <li>Ecriture simultanee cache + RAM</li>
  <li>Coherence garantie</li>
  <li>Lent</li>
</ul>

<p><strong>Write-back</strong>:</p>
<ul>
  <li>Ecriture uniquement dans cache</li>
  <li>RAM mise a jour lors de l'eviction</li>
  <li>Rapide mais complexe</li>
  <li>Bit "dirty" pour tracer modifications</li>
</ul>

<p><strong>Coherence de cache</strong>:</p>

<p>Dans un systeme multiprocesseur, comment garantir que tous les caches voient les memes donnees?</p>

<p>Protocoles MESI, MOESI: etats des lignes de cache (Modified, Exclusive, Shared, Invalid).</p>

<h4>6. Securite materielle et attaques</h4>

<p><strong>Vulnerabilites materielles</strong>:</p>

<p>Le materiel n'est pas infaillible et peut etre exploite.</p>

<p><strong>Attaques par canaux caches</strong> (side-channel attacks):</p>

<p>Exploitation d'informations indirectes (temps, consommation, emissions electromagnetiques).</p>

<p><strong>Attaque temporelle (timing attack)</strong>:</p>

<p>Mesure du temps d'execution pour deduire des informations secretes.</p>

<p>Exemple: cache timing.</p>

<p>Si une donnee est en cache, l'acces est rapide.<br/>
Si elle n'y est pas, l'acces est lent.</p>

<p>En mesurant le temps, un attaquant peut deduire quelles donnees ont ete accedees.</p>

<p><strong>Attaque Spectre</strong>:</p>

<p>Exploite l'execution speculative et la prediction de branchement.</p>

<p>Principe:</p>
<ol>
  <li>Entrainer le predicteur de branchement</li>
  <li>Faire executer speculativement du code qui accede a des donnees sensibles</li>
  <li>Observer effet de bord via cache timing</li>
  <li>Recuperer donnees secretes</li>
</ol>

<p>Impact: fuite d'informations entre processus, contournement d'isolation memoire.</p>

<p><strong>Attaque Meltdown</strong>:</p>

<p>Exploite le delai entre verification des permissions et annulation d'une instruction speculative.</p>

<p>Permet a un processus utilisateur de lire la memoire noyau.</p>

<p>Impact majeur: tous les processeurs Intel recents vulnerables.</p>

<p>Mitigation: KPTI (Kernel Page Table Isolation) avec cout en performance.</p>

<p><strong>Attaque par analyse de consommation</strong>:</p>

<p>Mesure de la consommation electrique pour extraire des cles cryptographiques.</p>

<p>Types:</p>
<ul>
  <li><strong>SPA</strong> (Simple Power Analysis): observation directe</li>
  <li><strong>DPA</strong> (Differential Power Analysis): analyse statistique</li>
</ul>

<p>Cibles privilegiees: cartes a puce, systemes embarques.</p>

<p>Contre-mesures:</p>
<ul>
  <li>Masquage (randomisation)</li>
  <li>Equilibrage de la consommation</li>
  <li>Operations a temps constant</li>
</ul>

<p><strong>Attaques electromagnetiques</strong>:</p>

<p>Ecoute des emissions EM du processeur.</p>

<p>Similaire aux attaques par consommation mais sans contact.</p>

<p><strong>Contre-mesures generales</strong>:</p>
<ul>
  <li>Conception securisee du materiel</li>
  <li>Patches microcode</li>
  <li>Modifications d'OS (KPTI)</li>
  <li>Code a temps constant</li>
  <li>Masquage et randomisation</li>
  <li>Enclaves securisees (Intel SGX, ARM TrustZone)</li>
</ul>

<h4>7. Processeurs multi-coeurs</h4>

<p><strong>Evolution vers le parallelisme</strong>:</p>

<p>Fin de la loi de Moore: frequences plafonnees (&approx; 4-5 GHz).</p>

<p>Solution: multiplier les coeurs.</p>

<p><strong>Architectures multi-coeurs</strong>:</p>

<table>
  <thead>
    <tr><th>Nombre de coeurs</th><th>Usage typique</th></tr>
  </thead>
  <tbody>
    <tr><td>2-4</td><td>Laptop, mobile</td></tr>
    <tr><td>4-8</td><td>Desktop</td></tr>
    <tr><td>8-64</td><td>Serveur</td></tr>
    <tr><td>64+</td><td>Calcul haute performance</td></tr>
  </tbody>
</table>

<p><strong>Symetrie (SMP)</strong>:</p>
<p>Tous les coeurs identiques, partagent la memoire.</p>

<p><strong>Asymetrie (AMP)</strong>:</p>
<p>Coeurs de types differents (ex: ARM big.LITTLE).</p>
<p>Coeurs rapides (big) pour taches lourdes.<br/>
Coeurs economes (LITTLE) pour taches legeres.</p>
<p>Optimise rapport performance/consommation.</p>

<p><strong>Hyperthreading (SMT)</strong>:</p>
<p>Un coeur physique apparait comme plusieurs coeurs logiques.</p>
<p>Partage des unites fonctionnelles entre threads.</p>
<p>Gain: 20-30% de performances.</p>

<p><strong>Affinite processeur</strong>:</p>
<p>Lier un processus a un coeur specifique.</p>
<p>Avantages:</p>
<ul>
  <li>Meilleure utilisation du cache</li>
  <li>Predictibilite temps reel</li>
  <li>Isolation pour securite</li>
</ul>

<hr/>

<h2>PART C: ASPECTS TECHNIQUES</h2>

<h3>Travaux Pratiques</h3>

<p><strong>TP: Comparaison ARM et x86/x64</strong></p>

<p>Objectif: comprendre les differences entre architectures par la pratique.</p>

<p><strong>Exercices typiques</strong>:</p>

<p><strong>1. Programme simple en ARM et x86</strong>:</p>

<p>Ecrire la meme fonction dans les deux assembleurs.</p>

<p>Exemple: calcul de factorielle.</p>

<p>ARM:</p>
<pre><code>factorial:
    PUSH {R4, LR}
    MOV R4, R0          ; Sauver n
    CMP R0, #1
    BLE end_fact
    SUB R0, R0, #1
    BL factorial        ; Appel recursif
    MUL R0, R4, R0      ; n * fact(n-1)
end_fact:
    POP {R4, PC}</code></pre>

<p>x86-64:</p>
<pre><code>factorial:
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
    ret</code></pre>

<p><strong>2. Analyse de performances</strong>:</p>

<p>Mesurer le temps d'execution de differentes implementations.</p>

<p>Comparer:</p>
<ul>
  <li>Code C optimise</li>
  <li>Assembleur manuel</li>
  <li>Differentes optimisations</li>
</ul>

<p><strong>3. Utilisation du cache</strong>:</p>

<p>Ecrire du code exploitant bien le cache vs mal.</p>

<p>Bon usage: parcours sequentiel d'un tableau.<br/>
Mauvais usage: acces aleatoires.</p>

<p><strong>4. Etude de vulnerabilites</strong>:</p>

<p>Implementer une attaque simple de type cache timing.</p>

<p>Observer la difference de temps entre:</p>
<ul>
  <li>Donnee en cache</li>
  <li>Donnee pas en cache</li>
</ul>

<h3>Outils et environnement</h3>

<p><strong>Assembleurs</strong>:</p>
<pre><code># ARM
arm-none-eabi-as programme.s -o programme.o
arm-none-eabi-ld programme.o -o programme

# x86-64
nasm -f elf64 programme.asm
ld programme.o -o programme

# Ou via GCC
gcc -S programme.c          # Generer assembleur
gcc -c programme.s          # Assembler</code></pre>

<p><strong>Desassemblage</strong>:</p>
<pre><code>objdump -d programme        # Desassembler
objdump -S programme        # Avec code source entrelace
gdb programme               # Debogueur</code></pre>

<p><strong>Analyse de performances</strong>:</p>
<pre><code>perf stat ./programme       # Statistiques performances
perf record ./programme     # Enregistrer profil
perf report                 # Analyser profil

# Compteurs materiels
perf stat -e cache-misses,cache-references ./programme</code></pre>

<p><strong>Simulation</strong>:</p>
<pre><code>qemu-arm programme          # Emuler ARM
qemu-x86_64 programme       # Emuler x86-64</code></pre>

<h3>Optimisations assembleur</h3>

<p><strong>Techniques courantes</strong>:</p>

<p><strong>Deroulage de boucles</strong> (loop unrolling):</p>
<pre><code>// Original
for(i=0; i&lt;100; i++)
    a[i] = b[i] + c[i];

// Deroule
for(i=0; i&lt;100; i+=4) {
    a[i] = b[i] + c[i];
    a[i+1] = b[i+1] + c[i+1];
    a[i+2] = b[i+2] + c[i+2];
    a[i+3] = b[i+3] + c[i+3];
}</code></pre>

<p>Avantages: moins de tests, meilleure utilisation pipeline.</p>

<p><strong>Vectorisation</strong> (SIMD):</p>
<p>Traiter plusieurs donnees simultanement.</p>
<p>ARM NEON, x86 SSE/AVX: operations sur 128-512 bits.</p>

<p><strong>Reorganisation pour le cache</strong>:</p>
<p>Acceder aux donnees dans l'ordre de leur disposition en memoire.</p>

<p><strong>Elimination de branchements</strong>:</p>
<p>Remplacer if par calculs arithmetiques/logiques.</p>

<p>Exemple:</p>
<pre><code>// Avec branchement
if(x &gt; 0) y = a; else y = b;

// Sans branchement (x86)
mov eax, a
mov ebx, b
cmp x, 0
cmovg eax, ebx  ; Conditional move</code></pre>

<hr/>

<h2>PART D: ANALYSE ET REFLEXION</h2>

<h3>Competences acquises</h3>

<p><strong>Programmation bas niveau</strong>:</p>
<ul>
  <li>Maitrise de l'assembleur ARM et x86</li>
  <li>Comprehension du lien entre C et assembleur</li>
  <li>Optimisation de code critique</li>
  <li>Debogage au niveau materiel</li>
</ul>

<p><strong>Architecture</strong>:</p>
<ul>
  <li>Comprehension des pipelines modernes</li>
  <li>Connaissance des hierarchies memoire</li>
  <li>Fonctionnement des caches</li>
  <li>Parallelisme materiel et multi-coeurs</li>
</ul>

<p><strong>Securite</strong>:</p>
<ul>
  <li>Identification de vulnerabilites materielles</li>
  <li>Comprehension des attaques par canaux caches</li>
  <li>Conscience des compromis securite/performance</li>
  <li>Analyse de risques au niveau materiel</li>
</ul>

<h3>Applications pratiques</h3>

<p>L'architecture materielle impacte tous les domaines de l'informatique:</p>

<p><strong>Systemes embarques</strong>:</p>
<ul>
  <li>Programmation ARM pour microcontroleurs</li>
  <li>Optimisation pour contraintes (memoire, energie)</li>
  <li>Systemes temps reel critiques</li>
  <li>IoT et objets connectes</li>
</ul>

<p><strong>Securite</strong>:</p>
<ul>
  <li>Analyse de malwares (reverse engineering)</li>
  <li>Cryptographie resistante aux attaques physiques</li>
  <li>Systemes securises (cartes a puce, TPM)</li>
  <li>Detection d'attaques materielles</li>
</ul>

<p><strong>Performances</strong>:</p>
<ul>
  <li>Optimisation de code critique (jeux, calcul scientifique)</li>
  <li>Exploitation efficace du materiel (caches, SIMD)</li>
  <li>Parallelisation sur multi-coeurs</li>
  <li>Reduction de la consommation energetique</li>
</ul>

<p><strong>Developpement systeme</strong>:</p>
<ul>
  <li>Noyaux de systemes d'exploitation</li>
  <li>Drivers de peripheriques</li>
  <li>Bootloaders et firmware</li>
  <li>Hyperviseurs et virtualisation</li>
</ul>

<h3>Liens avec autres cours</h3>

<table>
  <thead>
    <tr><th>Cours</th><th>Lien</th></tr>
  </thead>
  <tbody>
    <tr><td>Architecture Informatique (S5)</td><td>Bases de l'architecture</td></tr>
    <tr><td>Systemes d'Exploitation (S5)</td><td>Lien avec le logiciel systeme</td></tr>
    <tr><td>Langage C (S5)</td><td>Compilation vers assembleur</td></tr>
    <tr><td>Microcontroleur (S6)</td><td>Programmation ARM pratique</td></tr>
    <tr><td>Securite Materielle (S7)</td><td>Approfondissement securite</td></tr>
    <tr><td>Temps Reel (S8)</td><td>Optimisation et predictibilite</td></tr>
  </tbody>
</table>

<h3>Evolution des architectures</h3>

<p><strong>Tendances actuelles</strong>:</p>

<p><strong>Efficacite energetique</strong>:</p>
<p>Performance par Watt devient critique.</p>
<p>ARM domine mobile et commence a s'imposer en datacenter (AWS Graviton, Apple M1/M2).</p>

<p><strong>Architectures heterogenes</strong>:</p>
<p>Combinaison de processeurs differents:</p>
<ul>
  <li>CPU generalistes</li>
  <li>GPU pour calcul parallele</li>
  <li>NPU (Neural Processing Unit) pour IA</li>
  <li>Accelerateurs specialises (crypto, codecs)</li>
</ul>

<p><strong>RISC-V</strong>:</p>
<p>Architecture ouverte alternative a ARM et x86.</p>
<p>Adoption croissante dans l'embarque et la recherche.</p>

<p><strong>Calcul quantique</strong>:</p>
<p>Architectures radicalement differentes.</p>
<p>Encore experimental mais prometteur pour certains problemes.</p>

<p><strong>Memoire non-volatile</strong>:</p>
<p>Technologies emergentes (MRAM, ReRAM, 3D XPoint).</p>
<p>Floutent la distinction RAM/stockage.</p>

<h3>Securite: un defi permanent</h3>

<p><strong>Lecons des vulnerabilites recentes</strong>:</p>
<p>Spectre/Meltdown ont revele:</p>
<ul>
  <li>Optimisations de performance creent failles securite</li>
  <li>Corrections logicielles couteuses en performance</li>
  <li>Necessite de repenser conception materielle</li>
</ul>

<p><strong>Design securise</strong>:</p>
<p>Principes emergents:</p>
<ul>
  <li>Securite des la conception (security by design)</li>
  <li>Isolation materielle renforcee</li>
  <li>Enclaves securisees</li>
  <li>Verification formelle</li>
</ul>

<p><strong>Compromis inevitables</strong>:</p>
<p>Performance vs Securite:</p>
<ul>
  <li>Desactiver fonctionnalites (hyperthreading)</li>
  <li>Isolation couteuse (KPTI)</li>
  <li>Operations a temps constant plus lentes</li>
</ul>

<h3>Mon opinion</h3>

<p>Ce cours est essentiel pour comprendre le fonctionnement reel des ordinateurs.</p>

<p><strong>Points forts</strong>:</p>
<ul>
  <li>Vision concrete du materiel</li>
  <li>Comprehension des optimisations compilateur</li>
  <li>Conscience des enjeux de securite</li>
  <li>Programmation assembleur formatrice</li>
</ul>

<p><strong>Importance professionnelle</strong>:</p>
<p>Ces connaissances sont critiques pour:</p>
<ul>
  <li>Systemes embarques a contraintes fortes</li>
  <li>Optimisation de code haute performance</li>
  <li>Securite informatique (analyse, conception)</li>
  <li>Comprehension des architectures emergentes</li>
</ul>

<p><strong>Assembleur aujourd'hui</strong>:</p>
<p>Bien que rarement ecrit directement, comprendre l'assembleur permet:</p>
<ul>
  <li>Lire le code genere par le compilateur</li>
  <li>Optimiser les sections critiques</li>
  <li>Deboguer les problemes bas niveau</li>
  <li>Analyser des binaires (reverse engineering)</li>
</ul>

<p><strong>ARM vs x86: bataille interessante</strong>:</p>

<p>ARM:</p>
<ul>
  <li>Domine mobile/embarque</li>
  <li>Perce dans les datacenters</li>
  <li>Efficacite energetique superieure</li>
  <li>Apple M1/M2 impressionnants</li>
</ul>

<p>x86:</p>
<ul>
  <li>Toujours dominant sur PC/serveurs</li>
  <li>Puissance brute elevee</li>
  <li>Ecosysteme mature</li>
  <li>Retrocompatibilite precieuse</li>
</ul>

<p><strong>Securite materielle: priorite croissante</strong>:</p>
<p>Les attaques materielles sont de plus en plus sophistiquees.</p>
<p>Necessite:</p>
<ul>
  <li>Formation des developpeurs</li>
  <li>Outils d'analyse adaptes</li>
  <li>Conception consciente des risques</li>
  <li>Veille technologique constante</li>
</ul>

<p><strong>Futur des architectures</strong>:</p>
<p>Vers plus de:</p>
<ul>
  <li>Specialisation (accelerateurs IA, crypto)</li>
  <li>Heterogeneite (big.LITTLE generalise)</li>
  <li>Efficacite energetique</li>
  <li>Securite integree</li>
</ul>

<hr/>

<p><strong>Bilan personnel</strong>: Ce cours a fourni une comprehension approfondie du fonctionnement bas niveau des processeurs modernes. La programmation assembleur ARM et x86 a permis de voir concretement comment le code s'execute sur le materiel. La prise de conscience des vulnerabilites materielles (Spectre, Meltdown) et des attaques par canaux caches est particulierement importante pour concevoir des systemes securises. Ces connaissances sont directement applicables en developpement embarque, optimisation de performances, et analyse de securite. La comparaison ARM/x86 eclaire sur les compromis architecturaux et l'evolution future de l'informatique.</p>

<hr/>

<h2>Documents de Cours</h2>

<h2>Rapports et Projets</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Compte Rendu TP - Architecture Materielle</h4>
      <p>Rapport de travaux pratiques sur la comparaison des architectures ARM et x86/x64, la programmation assembleur et l'analyse de performances.</p>
      <p style="text-align: center;">
        <a href="/file/reports/S6/Compte rendu Architecture MatÚrielle.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Telecharger le rapport PDF
        </a>
      </p>
    </div>
  </div>
</div>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Introduction a l'Assembleur</h4>
      <p>Cours complet sur les langages assembleurs, leur role et leur utilisation dans l'architecture des processeurs.</p>
      <embed src="/cours-pdf/S6/Architecture-Materielle/assembleur.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Architecture-Materielle/assembleur.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>Comparaison ARM vs x86</h4>
      <p>Etude comparative des architectures ARM et x86/x64 : instructions, registres, conventions d'appel et performances.</p>
      <embed src="/cours-pdf/S6/Architecture-Materielle/arm-x86.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Architecture-Materielle/arm-x86.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>Introduction aux Attaques Materielles</h4>
      <p>Presentation des vulnerabilites materielles et des attaques par canaux caches (Spectre, Meltdown, timing attacks).</p>
      <embed src="/cours-pdf/S6/Architecture-Materielle/intro-attaques.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Architecture-Materielle/intro-attaques.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>Attaques par Consommation Energetique</h4>
      <p>Analyse detaillee des attaques SPA et DPA sur circuits cryptographiques via l'analyse de consommation electrique.</p>
      <embed src="/cours-pdf/S6/Architecture-Materielle/attaque-consommation.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Architecture-Materielle/attaque-consommation.pdf" target="_blank">Telecharger</a></p>
    </div>
  </div>
</div>

</div>

<div class="lang-en">

<h1>Hardware Architecture - S6</h1>

<p><strong>Year</strong>: 2022-2023 (Semester 6)<br/>
<strong>Credits</strong>: 3 ECTS<br/>
<strong>Type</strong>: Architecture and Embedded Systems</p>

<hr/>

<h2>PART A: GENERAL OVERVIEW</h2>

<h3>Course Objectives</h3>

<p>This course deepens the study of modern processor architectures, focusing on ARM and x86 architectures, assembly language programming, pipeline mechanisms, and hardware security aspects. The emphasis is on low-level understanding of processor operation and hardware vulnerabilities.</p>

<h3>Target Skills</h3>

<ul>
  <li>Understand ARM and x86/x64 architectures</li>
  <li>Program in ARM and x86 assembly</li>
  <li>Master pipeline and parallelism mechanisms</li>
  <li>Analyze processor performance</li>
  <li>Understand memory hierarchy and caches</li>
  <li>Identify hardware vulnerabilities</li>
  <li>Analyze side-channel attacks</li>
  <li>Optimize code for the target architecture</li>
  <li>Understand energy/performance trade-offs</li>
</ul>

<h3>Organization</h3>

<ul>
  <li><strong>Hours</strong>: Lectures and practical lab sessions</li>
  <li><strong>Assessment</strong>: Written exam + lab report</li>
  <li><strong>Semester</strong>: 6 (2022-2023)</li>
  <li><strong>Prerequisites</strong>: Basic architecture, C programming, operating systems</li>
</ul>

<hr/>

<h2>PART B: EXPERIENCE, CONTEXT AND FUNCTION</h2>

<h3>Pedagogical Content</h3>

<p>The course covers modern architectures and their security implications.</p>

<h4>1. Assembly Language Programming</h4>

<p><strong>Introduction to assembly</strong>:</p>

<p>Assembly is the lowest-level language (before binary).</p>

<p>Advantages:</p>
<ul>
  <li>Total control of the processor</li>
  <li>Optimal performance</li>
  <li>Understanding of hardware operation</li>
  <li>Low-level debugging</li>
  <li>Reverse engineering</li>
</ul>

<p>Uses:</p>
<ul>
  <li>Operating system kernels</li>
  <li>Device drivers</li>
  <li>Performance-critical code</li>
  <li>Embedded systems</li>
  <li>Security and cryptography</li>
</ul>

<p><strong>Structure of an assembly program</strong>:</p>

<p>Typical sections:</p>
<ul>
  <li><strong>.data section</strong>: initialized data</li>
  <li><strong>.bss section</strong>: uninitialized data</li>
  <li><strong>.text section</strong>: executable code</li>
</ul>

<p><strong>Registers</strong>:</p>

<p>Ultra-fast memory inside the processor.</p>

<p>Types:</p>
<ul>
  <li>General-purpose registers (computations, data)</li>
  <li>Stack Pointer (SP)</li>
  <li>Program Counter (PC)</li>
  <li>Status register (flags)</li>
</ul>

<h4>2. ARM Architecture</h4>

<p><strong>ARM characteristics</strong>:</p>

<p>ARM (Advanced RISC Machine) is the dominant architecture in embedded and mobile.</p>

<p>RISC principles (Reduced Instruction Set Computer):</p>
<ul>
  <li>Simple and uniform instructions</li>
  <li>Fast execution (1 cycle per instruction)</li>
  <li>Many registers</li>
  <li>Load/store architecture</li>
</ul>

<p><strong>ARM registers</strong>:</p>

<table>
  <thead>
    <tr><th>Register</th><th>Name</th><th>Function</th></tr>
  </thead>
  <tbody>
    <tr><td>R0-R12</td><td>General-purpose registers</td><td>Computations and data</td></tr>
    <tr><td>R13 (SP)</td><td>Stack Pointer</td><td>Stack pointer</td></tr>
    <tr><td>R14 (LR)</td><td>Link Register</td><td>Return address</td></tr>
    <tr><td>R15 (PC)</td><td>Program Counter</td><td>Current instruction address</td></tr>
    <tr><td>CPSR</td><td>Current Program Status</td><td>Status flags</td></tr>
  </tbody>
</table>

<p><strong>Basic ARM instructions</strong>:</p>

<pre><code>; Data movement
MOV R0, #5          ; R0 = 5
LDR R1, [R2]        ; R1 = memory[R2]
STR R0, [R1]        ; memory[R1] = R0

; Arithmetic
ADD R0, R1, R2      ; R0 = R1 + R2
SUB R0, R1, #10     ; R0 = R1 - 10
MUL R0, R1, R2      ; R0 = R1 x R2

; Logic
AND R0, R1, R2      ; R0 = R1 AND R2
ORR R0, R1, R2      ; R0 = R1 OR R2
EOR R0, R1, R2      ; R0 = R1 XOR R2

; Comparison and branching
CMP R0, R1          ; Compare R0 and R1
BEQ label           ; Branch if equal
BNE label           ; Branch if not equal
BL function         ; Function call</code></pre>

<p><strong>ARM calling convention</strong>:</p>
<ul>
  <li>R0-R3: first 4 arguments</li>
  <li>R0: return value</li>
  <li>R4-R11: saved by the called function</li>
  <li>LR (R14): return address</li>
</ul>

<p><strong>ARM function example</strong>:</p>

<pre><code>; Addition function: int add(int a, int b)
add:
    PUSH {LR}           ; Save LR
    ADD R0, R0, R1      ; R0 = R0 + R1 (result)
    POP {PC}            ; Return (restore PC)

; Function call
MOV R0, #5
MOV R1, #3
BL add                  ; Call add(5, 3)
; R0 contains 8</code></pre>

<h4>3. x86/x64 Architecture</h4>

<p><strong>x86 characteristics</strong>:</p>

<p>x86 (Intel/AMD) is the dominant architecture on PCs and servers.</p>

<p>CISC principles (Complex Instruction Set Computer):</p>
<ul>
  <li>Complex and varied instructions</li>
  <li>Variable execution time</li>
  <li>Fewer registers</li>
  <li>Directly accessible memory</li>
</ul>

<p><strong>x86-64 registers</strong>:</p>

<table>
  <thead>
    <tr><th>Register</th><th>64 bits</th><th>32 bits</th><th>16 bits</th><th>8 bits</th><th>Usage</th></tr>
  </thead>
  <tbody>
    <tr><td>RAX</td><td>RAX</td><td>EAX</td><td>AX</td><td>AL</td><td>Accumulator, return</td></tr>
    <tr><td>RBX</td><td>RBX</td><td>EBX</td><td>BX</td><td>BL</td><td>Base</td></tr>
    <tr><td>RCX</td><td>RCX</td><td>ECX</td><td>CX</td><td>CL</td><td>Counter</td></tr>
    <tr><td>RDX</td><td>RDX</td><td>EDX</td><td>DX</td><td>DL</td><td>Data</td></tr>
    <tr><td>RSI</td><td>RSI</td><td>ESI</td><td>SI</td><td>-</td><td>Source index</td></tr>
    <tr><td>RDI</td><td>RDI</td><td>EDI</td><td>DI</td><td>-</td><td>Destination index</td></tr>
    <tr><td>RBP</td><td>RBP</td><td>EBP</td><td>BP</td><td>-</td><td>Base pointer (stack)</td></tr>
    <tr><td>RSP</td><td>RSP</td><td>ESP</td><td>SP</td><td>-</td><td>Stack pointer</td></tr>
    <tr><td>R8-R15</td><td>-</td><td>-</td><td>-</td><td>-</td><td>Additional registers</td></tr>
  </tbody>
</table>

<p><strong>Basic x86 instructions</strong>:</p>

<pre><code>; Data movement
mov rax, 5          ; rax = 5
mov rbx, [rax]      ; rbx = memory[rax]
lea rax, [rbx+8]    ; rax = address rbx+8

; Arithmetic
add rax, rbx        ; rax = rax + rbx
sub rax, 10         ; rax = rax - 10
imul rax, rbx       ; rax = rax x rbx
idiv rcx            ; rax = rax / rcx, rdx = remainder

; Logic
and rax, rbx        ; rax = rax AND rbx
or rax, rbx         ; rax = rax OR rbx
xor rax, rax        ; rax = 0 (common idiom)
not rax             ; rax = NOT rax

; Stack
push rax            ; Push rax
pop rbx             ; Pop into rbx

; Branching
cmp rax, rbx        ; Compare
je label            ; Jump if equal
jne label           ; Jump if not equal
jmp label           ; Unconditional jump
call function       ; Function call
ret                 ; Return</code></pre>

<p><strong>x64 calling convention (System V)</strong>:</p>

<p>Arguments in order:</p>
<ol>
  <li>RDI</li>
  <li>RSI</li>
  <li>RDX</li>
  <li>RCX</li>
  <li>R8</li>
  <li>R9</li>
  <li>Then on the stack</li>
</ol>

<p>Return value: RAX</p>

<p><strong>x64 function example</strong>:</p>

<pre><code>; Function: int add(int a, int b)
add:
    push rbp            ; Prologue
    mov rbp, rsp

    mov eax, edi        ; a in eax
    add eax, esi        ; eax += b

    pop rbp             ; Epilogue
    ret</code></pre>

<p><strong>ARM vs x86 comparison</strong>:</p>

<table>
  <thead>
    <tr><th>Aspect</th><th>ARM</th><th>x86</th></tr>
  </thead>
  <tbody>
    <tr><td>Philosophy</td><td>RISC</td><td>CISC</td></tr>
    <tr><td>Instructions</td><td>Simple, regular</td><td>Complex, varied</td></tr>
    <tr><td>Instruction length</td><td>Fixed (32 bits)</td><td>Variable (1-15 bytes)</td></tr>
    <tr><td>Registers</td><td>16 (ARM32)</td><td>16 (x64)</td></tr>
    <tr><td>Power consumption</td><td>Low</td><td>High</td></tr>
    <tr><td>Performance/Watt</td><td>Excellent</td><td>Average</td></tr>
    <tr><td>Usage</td><td>Mobile, embedded</td><td>PC, servers</td></tr>
  </tbody>
</table>

<h4>4. Pipeline and Parallelism</h4>

<p><strong>Instruction pipeline</strong>:</p>

<p>Technique allowing multiple instructions to be executed in parallel.</p>

<p>Classic stages (5 stages):</p>
<ol>
  <li><strong>IF</strong> (Instruction Fetch): read instruction</li>
  <li><strong>ID</strong> (Instruction Decode): decoding</li>
  <li><strong>EX</strong> (Execute): execution</li>
  <li><strong>MEM</strong> (Memory): memory access</li>
  <li><strong>WB</strong> (Write Back): write result</li>
</ol>

<p>Without pipeline: 5 cycles per instruction.<br/>
With pipeline: 1 instruction/cycle at steady state.</p>

<p><strong>Pipeline hazards</strong>:</p>

<p><strong>Structural hazards</strong>:</p>
<p>Conflict on a hardware resource.<br/>
Solution: duplicate resources.</p>

<p><strong>Data hazards</strong>:</p>
<p>An instruction depends on a result that is not yet available.</p>

<p>Example:</p>
<pre><code>ADD R1, R2, R3    ; R1 = R2 + R3
SUB R4, R1, R5    ; R4 = R1 - R5 (depends on R1!)</code></pre>

<p>Solutions:</p>
<ul>
  <li><strong>Stall</strong> (bubbles): wait</li>
  <li><strong>Forwarding</strong>: transmit result directly</li>
  <li><strong>Reordering</strong>: scheduler rearranges instructions</li>
</ul>

<p><strong>Control hazards</strong>:</p>

<p>Conditional branches disrupt the pipeline.</p>

<p>The processor does not know which instruction to fetch after a branch.</p>

<p>Solutions:</p>
<ul>
  <li><strong>Branch prediction</strong>: guess the direction</li>
  <li><strong>Speculative execution</strong>: execute both paths</li>
  <li><strong>Branch delay slot</strong>: instruction after branch always executed</li>
</ul>

<p><strong>Superscalar architectures</strong>:</p>

<p>Multiple pipelines in parallel &rarr; multiple instructions/cycle.</p>

<p>Examples: modern processors (4-6 instructions/cycle).</p>

<p><strong>Out-of-order execution</strong>:</p>

<p>The processor reorders instructions to maximize functional unit utilization.</p>

<p>Hides latencies and improves IPC (Instructions Per Cycle).</p>

<p><strong>Instruction-level parallelism (ILP)</strong>:</p>

<p>Automatic exploitation of parallelism in sequential code.</p>

<p>Techniques:</p>
<ul>
  <li>Pipeline</li>
  <li>Superscalar</li>
  <li>Out-of-order execution</li>
  <li>Branch prediction</li>
  <li>Register renaming</li>
</ul>

<h4>5. Memory Hierarchy</h4>

<p><strong>Memory pyramid</strong>:</p>

<table>
  <thead>
    <tr><th>Level</th><th>Size</th><th>Latency</th><th>Cost</th></tr>
  </thead>
  <tbody>
    <tr><td>Registers</td><td>A few bytes</td><td>&lt; 1 ns</td><td>Very high</td></tr>
    <tr><td>L1 Cache</td><td>32-64 KB</td><td>1-2 ns</td><td>High</td></tr>
    <tr><td>L2 Cache</td><td>256 KB - 1 MB</td><td>5-10 ns</td><td>Medium</td></tr>
    <tr><td>L3 Cache</td><td>4-32 MB</td><td>20-40 ns</td><td>Low</td></tr>
    <tr><td>RAM</td><td>4-64 GB</td><td>50-100 ns</td><td>Very low</td></tr>
    <tr><td>SSD</td><td>256 GB - 2 TB</td><td>0.1 ms</td><td>Minimal</td></tr>
    <tr><td>HDD</td><td>1-10 TB</td><td>10 ms</td><td>Minimal</td></tr>
  </tbody>
</table>

<p>Locality principle:</p>
<ul>
  <li><strong>Temporal</strong>: recently accessed data will likely be accessed again</li>
  <li><strong>Spatial</strong>: nearby data will likely be accessed together</li>
</ul>

<p><strong>Cache memory</strong>:</p>

<p>Fast memory between processor and RAM.</p>

<p><strong>Organization</strong>:</p>

<p><strong>Direct-mapped</strong>: each RAM address has only one possible location in cache.</p>
<ul><li>Simple but frequent conflicts</li></ul>

<p><strong>Set-associative</strong>: each address has N possible locations.</p>
<ul><li>Good compromise (2-way, 4-way, 8-way common)</li></ul>

<p><strong>Fully-associative</strong>: address can go anywhere.</p>
<ul><li>Flexible but complex and expensive</li></ul>

<p><strong>Replacement policies</strong>:</p>

<p>When the cache is full, which line to evict?</p>
<ul>
  <li><strong>LRU</strong> (Least Recently Used): least recently used</li>
  <li><strong>FIFO</strong>: oldest</li>
  <li><strong>Random</strong>: random</li>
  <li><strong>LFU</strong> (Least Frequently Used): least frequently used</li>
</ul>

<p><strong>Write policies</strong>:</p>

<p><strong>Write-through</strong>:</p>
<ul>
  <li>Simultaneous write to cache + RAM</li>
  <li>Guaranteed coherence</li>
  <li>Slow</li>
</ul>

<p><strong>Write-back</strong>:</p>
<ul>
  <li>Write only to cache</li>
  <li>RAM updated upon eviction</li>
  <li>Fast but complex</li>
  <li>"Dirty" bit to track modifications</li>
</ul>

<p><strong>Cache coherence</strong>:</p>

<p>In a multiprocessor system, how to ensure all caches see the same data?</p>

<p>MESI, MOESI protocols: cache line states (Modified, Exclusive, Shared, Invalid).</p>

<h4>6. Hardware Security and Attacks</h4>

<p><strong>Hardware vulnerabilities</strong>:</p>

<p>Hardware is not infallible and can be exploited.</p>

<p><strong>Side-channel attacks</strong>:</p>

<p>Exploitation of indirect information (timing, power consumption, electromagnetic emissions).</p>

<p><strong>Timing attack</strong>:</p>

<p>Measuring execution time to deduce secret information.</p>

<p>Example: cache timing.</p>

<p>If data is in cache, access is fast.<br/>
If not, access is slow.</p>

<p>By measuring time, an attacker can deduce which data has been accessed.</p>

<p><strong>Spectre attack</strong>:</p>

<p>Exploits speculative execution and branch prediction.</p>

<p>Principle:</p>
<ol>
  <li>Train the branch predictor</li>
  <li>Cause speculative execution of code that accesses sensitive data</li>
  <li>Observe side effects via cache timing</li>
  <li>Recover secret data</li>
</ol>

<p>Impact: information leakage between processes, bypassing memory isolation.</p>

<p><strong>Meltdown attack</strong>:</p>

<p>Exploits the delay between permission checking and cancellation of a speculative instruction.</p>

<p>Allows a user process to read kernel memory.</p>

<p>Major impact: all recent Intel processors were vulnerable.</p>

<p>Mitigation: KPTI (Kernel Page Table Isolation) with performance cost.</p>

<p><strong>Power analysis attack</strong>:</p>

<p>Measuring electrical power consumption to extract cryptographic keys.</p>

<p>Types:</p>
<ul>
  <li><strong>SPA</strong> (Simple Power Analysis): direct observation</li>
  <li><strong>DPA</strong> (Differential Power Analysis): statistical analysis</li>
</ul>

<p>Prime targets: smart cards, embedded systems.</p>

<p>Countermeasures:</p>
<ul>
  <li>Masking (randomization)</li>
  <li>Power balancing</li>
  <li>Constant-time operations</li>
</ul>

<p><strong>Electromagnetic attacks</strong>:</p>

<p>Eavesdropping on processor EM emissions.</p>

<p>Similar to power analysis attacks but without contact.</p>

<p><strong>General countermeasures</strong>:</p>
<ul>
  <li>Secure hardware design</li>
  <li>Microcode patches</li>
  <li>OS modifications (KPTI)</li>
  <li>Constant-time code</li>
  <li>Masking and randomization</li>
  <li>Secure enclaves (Intel SGX, ARM TrustZone)</li>
</ul>

<h4>7. Multi-core Processors</h4>

<p><strong>Evolution towards parallelism</strong>:</p>

<p>End of Moore's Law: frequencies plateaued (&approx; 4-5 GHz).</p>

<p>Solution: multiply cores.</p>

<p><strong>Multi-core architectures</strong>:</p>

<table>
  <thead>
    <tr><th>Number of cores</th><th>Typical usage</th></tr>
  </thead>
  <tbody>
    <tr><td>2-4</td><td>Laptop, mobile</td></tr>
    <tr><td>4-8</td><td>Desktop</td></tr>
    <tr><td>8-64</td><td>Server</td></tr>
    <tr><td>64+</td><td>High-performance computing</td></tr>
  </tbody>
</table>

<p><strong>Symmetric (SMP)</strong>:</p>
<p>All cores identical, sharing memory.</p>

<p><strong>Asymmetric (AMP)</strong>:</p>
<p>Cores of different types (e.g., ARM big.LITTLE).</p>
<p>Fast cores (big) for heavy tasks.<br/>
Efficient cores (LITTLE) for light tasks.</p>
<p>Optimizes performance/power ratio.</p>

<p><strong>Hyperthreading (SMT)</strong>:</p>
<p>One physical core appears as multiple logical cores.</p>
<p>Sharing functional units between threads.</p>
<p>Gain: 20-30% performance improvement.</p>

<p><strong>Processor affinity</strong>:</p>
<p>Binding a process to a specific core.</p>
<p>Advantages:</p>
<ul>
  <li>Better cache utilization</li>
  <li>Real-time predictability</li>
  <li>Isolation for security</li>
</ul>

<hr/>

<h2>PART C: TECHNICAL ASPECTS</h2>

<h3>Lab Sessions</h3>

<p><strong>Lab: ARM vs x86/x64 comparison</strong></p>

<p>Objective: understand architectural differences through practice.</p>

<p><strong>Typical exercises</strong>:</p>

<p><strong>1. Simple program in ARM and x86</strong>:</p>

<p>Write the same function in both assembly languages.</p>

<p>Example: factorial computation.</p>

<p>ARM:</p>
<pre><code>factorial:
    PUSH {R4, LR}
    MOV R4, R0          ; Save n
    CMP R0, #1
    BLE end_fact
    SUB R0, R0, #1
    BL factorial        ; Recursive call
    MUL R0, R4, R0      ; n * fact(n-1)
end_fact:
    POP {R4, PC}</code></pre>

<p>x86-64:</p>
<pre><code>factorial:
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
    ret</code></pre>

<p><strong>2. Performance analysis</strong>:</p>

<p>Measure execution time of different implementations.</p>

<p>Compare:</p>
<ul>
  <li>Optimized C code</li>
  <li>Hand-written assembly</li>
  <li>Different optimizations</li>
</ul>

<p><strong>3. Cache usage</strong>:</p>

<p>Write code that uses the cache well vs poorly.</p>

<p>Good usage: sequential array traversal.<br/>
Bad usage: random access.</p>

<p><strong>4. Vulnerability study</strong>:</p>

<p>Implement a simple cache timing attack.</p>

<p>Observe the time difference between:</p>
<ul>
  <li>Data in cache</li>
  <li>Data not in cache</li>
</ul>

<h3>Tools and Environment</h3>

<p><strong>Assemblers</strong>:</p>
<pre><code># ARM
arm-none-eabi-as program.s -o program.o
arm-none-eabi-ld program.o -o program

# x86-64
nasm -f elf64 program.asm
ld program.o -o program

# Or via GCC
gcc -S program.c          # Generate assembly
gcc -c program.s          # Assemble</code></pre>

<p><strong>Disassembly</strong>:</p>
<pre><code>objdump -d program        # Disassemble
objdump -S program        # With interleaved source code
gdb program               # Debugger</code></pre>

<p><strong>Performance analysis</strong>:</p>
<pre><code>perf stat ./program       # Performance statistics
perf record ./program     # Record profile
perf report               # Analyze profile

# Hardware counters
perf stat -e cache-misses,cache-references ./program</code></pre>

<p><strong>Simulation</strong>:</p>
<pre><code>qemu-arm program          # Emulate ARM
qemu-x86_64 program       # Emulate x86-64</code></pre>

<h3>Assembly Optimizations</h3>

<p><strong>Common techniques</strong>:</p>

<p><strong>Loop unrolling</strong>:</p>
<pre><code>// Original
for(i=0; i&lt;100; i++)
    a[i] = b[i] + c[i];

// Unrolled
for(i=0; i&lt;100; i+=4) {
    a[i] = b[i] + c[i];
    a[i+1] = b[i+1] + c[i+1];
    a[i+2] = b[i+2] + c[i+2];
    a[i+3] = b[i+3] + c[i+3];
}</code></pre>

<p>Advantages: fewer tests, better pipeline utilization.</p>

<p><strong>Vectorization</strong> (SIMD):</p>
<p>Process multiple data simultaneously.</p>
<p>ARM NEON, x86 SSE/AVX: operations on 128-512 bits.</p>

<p><strong>Cache-friendly reordering</strong>:</p>
<p>Access data in the order of their layout in memory.</p>

<p><strong>Branch elimination</strong>:</p>
<p>Replace if with arithmetic/logical computations.</p>

<p>Example:</p>
<pre><code>// With branch
if(x &gt; 0) y = a; else y = b;

// Without branch (x86)
mov eax, a
mov ebx, b
cmp x, 0
cmovg eax, ebx  ; Conditional move</code></pre>

<hr/>

<h2>PART D: ANALYSIS AND REFLECTION</h2>

<h3>Acquired Skills</h3>

<p><strong>Low-level programming</strong>:</p>
<ul>
  <li>Proficiency in ARM and x86 assembly</li>
  <li>Understanding the link between C and assembly</li>
  <li>Critical code optimization</li>
  <li>Hardware-level debugging</li>
</ul>

<p><strong>Architecture</strong>:</p>
<ul>
  <li>Understanding modern pipelines</li>
  <li>Knowledge of memory hierarchies</li>
  <li>Cache operation</li>
  <li>Hardware parallelism and multi-core</li>
</ul>

<p><strong>Security</strong>:</p>
<ul>
  <li>Identifying hardware vulnerabilities</li>
  <li>Understanding side-channel attacks</li>
  <li>Awareness of security/performance trade-offs</li>
  <li>Hardware-level risk analysis</li>
</ul>

<h3>Practical Applications</h3>

<p>Hardware architecture impacts all areas of computing:</p>

<p><strong>Embedded systems</strong>:</p>
<ul>
  <li>ARM programming for microcontrollers</li>
  <li>Optimization under constraints (memory, energy)</li>
  <li>Critical real-time systems</li>
  <li>IoT and connected objects</li>
</ul>

<p><strong>Security</strong>:</p>
<ul>
  <li>Malware analysis (reverse engineering)</li>
  <li>Cryptography resistant to physical attacks</li>
  <li>Secure systems (smart cards, TPM)</li>
  <li>Hardware attack detection</li>
</ul>

<p><strong>Performance</strong>:</p>
<ul>
  <li>Critical code optimization (gaming, scientific computing)</li>
  <li>Efficient hardware utilization (caches, SIMD)</li>
  <li>Multi-core parallelization</li>
  <li>Energy consumption reduction</li>
</ul>

<p><strong>System development</strong>:</p>
<ul>
  <li>Operating system kernels</li>
  <li>Device drivers</li>
  <li>Bootloaders and firmware</li>
  <li>Hypervisors and virtualization</li>
</ul>

<h3>Links with Other Courses</h3>

<table>
  <thead>
    <tr><th>Course</th><th>Link</th></tr>
  </thead>
  <tbody>
    <tr><td>Computer Architecture (S5)</td><td>Architecture fundamentals</td></tr>
    <tr><td>Operating Systems (S5)</td><td>Link with system software</td></tr>
    <tr><td>C Language (S5)</td><td>Compilation to assembly</td></tr>
    <tr><td>Microcontroller (S6)</td><td>Practical ARM programming</td></tr>
    <tr><td>Hardware Security (S7)</td><td>Security deep dive</td></tr>
    <tr><td>Real-Time Systems (S8)</td><td>Optimization and predictability</td></tr>
  </tbody>
</table>

<h3>Architecture Evolution</h3>

<p><strong>Current trends</strong>:</p>

<p><strong>Energy efficiency</strong>:</p>
<p>Performance per Watt is becoming critical.</p>
<p>ARM dominates mobile and is gaining ground in datacenters (AWS Graviton, Apple M1/M2).</p>

<p><strong>Heterogeneous architectures</strong>:</p>
<p>Combination of different processors:</p>
<ul>
  <li>General-purpose CPUs</li>
  <li>GPUs for parallel computation</li>
  <li>NPU (Neural Processing Unit) for AI</li>
  <li>Specialized accelerators (crypto, codecs)</li>
</ul>

<p><strong>RISC-V</strong>:</p>
<p>Open-source architecture alternative to ARM and x86.</p>
<p>Growing adoption in embedded and research.</p>

<p><strong>Quantum computing</strong>:</p>
<p>Radically different architectures.</p>
<p>Still experimental but promising for certain problems.</p>

<p><strong>Non-volatile memory</strong>:</p>
<p>Emerging technologies (MRAM, ReRAM, 3D XPoint).</p>
<p>Blurring the distinction between RAM and storage.</p>

<h3>Security: An Ongoing Challenge</h3>

<p><strong>Lessons from recent vulnerabilities</strong>:</p>
<p>Spectre/Meltdown revealed:</p>
<ul>
  <li>Performance optimizations create security flaws</li>
  <li>Software fixes are costly in terms of performance</li>
  <li>Need to rethink hardware design</li>
</ul>

<p><strong>Secure design</strong>:</p>
<p>Emerging principles:</p>
<ul>
  <li>Security by design</li>
  <li>Reinforced hardware isolation</li>
  <li>Secure enclaves</li>
  <li>Formal verification</li>
</ul>

<p><strong>Inevitable trade-offs</strong>:</p>
<p>Performance vs Security:</p>
<ul>
  <li>Disabling features (hyperthreading)</li>
  <li>Costly isolation (KPTI)</li>
  <li>Constant-time operations are slower</li>
</ul>

<h3>My Opinion</h3>

<p>This course is essential for understanding how computers actually work.</p>

<p><strong>Strengths</strong>:</p>
<ul>
  <li>Concrete view of hardware</li>
  <li>Understanding of compiler optimizations</li>
  <li>Awareness of security challenges</li>
  <li>Educational assembly programming</li>
</ul>

<p><strong>Professional importance</strong>:</p>
<p>This knowledge is critical for:</p>
<ul>
  <li>Highly constrained embedded systems</li>
  <li>High-performance code optimization</li>
  <li>Computer security (analysis, design)</li>
  <li>Understanding emerging architectures</li>
</ul>

<p><strong>Assembly today</strong>:</p>
<p>Although rarely written directly, understanding assembly allows:</p>
<ul>
  <li>Reading compiler-generated code</li>
  <li>Optimizing critical sections</li>
  <li>Debugging low-level issues</li>
  <li>Analyzing binaries (reverse engineering)</li>
</ul>

<p><strong>ARM vs x86: an interesting battle</strong>:</p>

<p>ARM:</p>
<ul>
  <li>Dominates mobile/embedded</li>
  <li>Breaking into datacenters</li>
  <li>Superior energy efficiency</li>
  <li>Impressive Apple M1/M2</li>
</ul>

<p>x86:</p>
<ul>
  <li>Still dominant on PC/servers</li>
  <li>High raw power</li>
  <li>Mature ecosystem</li>
  <li>Valuable backward compatibility</li>
</ul>

<p><strong>Hardware security: growing priority</strong>:</p>
<p>Hardware attacks are becoming increasingly sophisticated.</p>
<p>Requires:</p>
<ul>
  <li>Developer training</li>
  <li>Adapted analysis tools</li>
  <li>Risk-aware design</li>
  <li>Constant technology watch</li>
</ul>

<p><strong>Future of architectures</strong>:</p>
<p>Towards more:</p>
<ul>
  <li>Specialization (AI accelerators, crypto)</li>
  <li>Heterogeneity (generalized big.LITTLE)</li>
  <li>Energy efficiency</li>
  <li>Integrated security</li>
</ul>

<hr/>

<p><strong>Personal assessment</strong>: This course provided an in-depth understanding of low-level operation of modern processors. ARM and x86 assembly programming allowed seeing concretely how code executes on hardware. Awareness of hardware vulnerabilities (Spectre, Meltdown) and side-channel attacks is particularly important for designing secure systems. This knowledge is directly applicable in embedded development, performance optimization, and security analysis. The ARM/x86 comparison sheds light on architectural trade-offs and the future evolution of computing.</p>

<hr/>

<h2>Course Documents</h2>

<h2>Reports and Projects</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Lab Report - Hardware Architecture</h4>
      <p>Lab report on the comparison of ARM and x86/x64 architectures, assembly programming and performance analysis.</p>
      <p style="text-align: center;">
        <a href="/file/reports/S6/Compte rendu Architecture MatÚrielle.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Download PDF report
        </a>
      </p>
    </div>
  </div>
</div>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Introduction to Assembly</h4>
      <p>Complete course on assembly languages, their role and their use in processor architecture.</p>
      <embed src="/cours-pdf/S6/Architecture-Materielle/assembleur.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Architecture-Materielle/assembleur.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>ARM vs x86 Comparison</h4>
      <p>Comparative study of ARM and x86/x64 architectures: instructions, registers, calling conventions and performance.</p>
      <embed src="/cours-pdf/S6/Architecture-Materielle/arm-x86.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Architecture-Materielle/arm-x86.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>Introduction to Hardware Attacks</h4>
      <p>Overview of hardware vulnerabilities and side-channel attacks (Spectre, Meltdown, timing attacks).</p>
      <embed src="/cours-pdf/S6/Architecture-Materielle/intro-attaques.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Architecture-Materielle/intro-attaques.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>Power Consumption Attacks</h4>
      <p>Detailed analysis of SPA and DPA attacks on cryptographic circuits via electrical power consumption analysis.</p>
      <embed src="/cours-pdf/S6/Architecture-Materielle/attaque-consommation.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Architecture-Materielle/attaque-consommation.pdf" target="_blank">Download</a></p>
    </div>
  </div>
</div>

</div>

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

---
layout: default
title: "Architecture Informatique Materielle - S5"
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
</style>

<div class="back-nav">
  <a href="./my-courses-2022-2023.html" data-i18n-html="back-courses-2022-2023">← Retour aux Cours 2022-2023</a>
</div>

<!-- ==================== FRENCH VERSION ==================== -->
<div class="lang-fr">

<h1>Architecture Informatique Materielle - S5</h1>

<p><strong>Annee</strong>: 2022-2023 (Semestre 5)<br/>
<strong>Credits</strong>: 3 ECTS<br/>
<strong>Type</strong>: Informatique / Architecture des Systemes</p>

<hr/>

<h2>PART A: PRESENTATION GENERALE</h2>

<h3>Objectifs du cours</h3>

<p>Le cours "Architecture Informatique Materielle" fournit une comprehension approfondie de l'organisation et du fonctionnement des systemes informatiques au niveau materiel. Il couvre l'ensemble de la hierarchie memoire, de l'architecture des processeurs, et des mecanismes d'optimisation des performances. Ce cours est fondamental pour comprendre comment le materiel influence les performances logicielles et pour concevoir des systemes embarques efficaces.</p>

<div style="text-align: center;">
    <img src="/img/Courses/S5/Architecture-Informatique-Matérielle/archi-info-mat-vue.png" style="width: 70%;"/>
</div>
<br>

<h3>Competences visees</h3>

<ul>
<li>Maitriser les concepts d'architecture des processeurs (RISC, pipeline, unites fonctionnelles)</li>
<li>Comprendre la hierarchie memoire (memoire physique, virtuelle, caches)</li>
<li>Analyser les performances des systemes informatiques</li>
<li>Programmer en assembleur MIPS pour le bas niveau</li>
<li>Optimiser le code en fonction de l'architecture materielle</li>
<li>Comprendre les mecanismes de pagination et de gestion memoire</li>
</ul>

<h3>Organisation</h3>

<ul>
<li><strong>Volume horaire</strong>: 30h (CM: 18h, TD: 12h)</li>
<li><strong>Evaluation</strong>: Examen ecrit + TDs notes + TP assembleur</li>
<li><strong>Semestre</strong>: 5 (2022-2023)</li>
<li><strong>Prerequis</strong>: Logique sequentielle, systemes numeriques</li>
</ul>

<hr/>

<h2>PART B: EXPERIENCE, CONTEXTE ET FONCTION</h2>

<h3>Contenu pedagogique</h3>

<h4>1. Introduction Generale aux Architectures</h4>

<p><strong>Concepts fondamentaux</strong>:</p>
<ul>
<li>Architecture de Von Neumann vs Harvard</li>
<li>Modele de Von Neumann: memoire unique pour donnees et instructions</li>
</ul>

<div style="text-align: center;">
    <img src="/img/Courses/S5/Architecture-Informatique-Matérielle/von-neumann.png" style="width: 30%;"/>
</div>

<ul>
<li>Architecture Harvard: separation physique instructions/donnees</li>
</ul>
<div style="text-align: center;">
    <img src="/img/Courses/S5/Architecture-Informatique-Matérielle/harvard.png" style="width: 60%;"/>
</div>
<ul>
<li>Bus systeme: adresses, donnees, controle</li>
<li>Cycle d'execution: Fetch-Decode-Execute</li>
</ul>

<p><strong>Evolution historique</strong>:</p>
<ul>
<li>Des premiers ordinateurs aux architectures modernes</li>
<li>Loi de Moore et ses limites actuelles</li>
<li>Passage du monoprocesseur au multiprocesseur</li>
<li>Architectures RISC (Reduced Instruction Set Computer) vs CISC (Complex)</li>
</ul>

<p><strong>Mesure de performances</strong>:</p>
<ul>
<li>CPI (Cycles Per Instruction)</li>
<li>MIPS (Millions d'Instructions Per Second)</li>
<li>Temps d'execution CPU</li>
<li>Benchmark et profiling</li>
</ul>

<p><strong>Supports de cours</strong>:
<a href="/cours-pdf/S5/Architecture-Informatique-Matérielle/1-Introduction_generale_architectures.pdf">Introduction generale aux architectures</a> (PDF)</p>

<h4>2. Memoire Physique</h4>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S5/architecture-info/von-neumann.svg" alt="Architecture Von Neumann" style="max-width: 550px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Architecture Von Neumann - Modele classique avec bus partages</p>
</div>

<p><strong>Organisation memoire</strong>:</p>
<ul>
<li>Hierarchie memoire: registres → cache → RAM → disque</li>
<li>Technologies memoire: SRAM, DRAM, ROM, Flash</li>
</ul>
<div style="text-align: center;">
    <img src="/img/Courses/S5/Architecture-Informatique-Matérielle/memoire.png" style="width: 60%;"/>
</div>
<ul>
<li>Temps d'acces et bande passante</li>
<li>Principe de localite (temporelle et spatiale)</li>
</ul>

<p><strong>Adressage memoire</strong>:</p>
<ul>
<li>Espace d'adressage lineaire</li>
<li>Adressage par mot vs par octet (byte-addressable)</li>
<li>Alignement memoire et padding</li>
<li>Endianness (big-endian vs little-endian)</li>
</ul>

<p><strong>Organisation des donnees</strong>:</p>
<pre><code>Exemple d'organisation memoire 32 bits:
Adresse    |  Contenu (hex)
-----------|-----------------
0x00000000 |  0xAABBCCDD
0x00000004 |  0x11223344
0x00000008 |  0xFFFF0000
</code></pre>

<p><strong>Supports de cours</strong>:
<a href="/cours-pdf/S5/Architecture-Informatique-Matérielle/2-Memoire_physique.pdf">Memoire physique</a> (PDF)</p>

<h4>3. Memoire Virtuelle</h4>

<p><strong>Concepts de virtualisation</strong>:</p>
<ul>
<li>Separation adresse virtuelle / adresse physique</li>
<li>Espace d'adressage par processus</li>
<li>Protection memoire et isolation</li>
<li>Partage de memoire entre processus</li>
</ul>

<p><strong>Mecanisme de pagination</strong>:</p>
<ul>
<li>Pages virtuelles et cadres physiques (frames)</li>
<li>Taille de page typique: 4 KB, 2 MB (large pages)</li>
<li>Table des pages (page table)</li>
<li>TLB (Translation Lookaside Buffer): cache pour traductions</li>
</ul>

<p><strong>Formules de traduction</strong>:</p>
<pre><code>Adresse virtuelle = Numero de page virtuelle + Offset
Adresse physique = Numero de cadre physique + Offset

Exemple avec pages de 4 KB (2^12 octets):
Adresse virtuelle: 32 bits
  - 20 bits: numero de page (2^20 pages)
  - 12 bits: offset dans la page (4096 octets)
</code></pre>

<p><strong>Gestion des defauts de page</strong>:</p>
<ul>
<li>Page fault (defaut de page)</li>
<li>Algorithmes de remplacement: LRU, FIFO, Clock</li>
<li>Swapping et pagination a la demande</li>
<li>Working set et thrashing</li>
</ul>

<p><strong>Table des pages multi-niveaux</strong>:</p>
<ul>
<li>Table des pages sur 2 niveaux (x86)</li>
<li>Table des pages sur 3/4 niveaux (x86-64)</li>
<li>Reduction de l'espace memoire pour les tables</li>
<li>Pagination inverse</li>
</ul>

<p><strong>Supports de cours</strong>:
<a href="/cours-pdf/S5/Architecture-Informatique-Matérielle/3-Memoire-virtuelle.pdf">Memoire virtuelle</a> (PDF)</p>

<h4>4. Memoires Caches</h4>

<p><strong>Principe du cache</strong>:</p>
<ul>
<li>Cache situe entre CPU et RAM</li>
<li>Exploite la localite spatiale et temporelle</li>
<li>Reduction du temps d'acces moyen</li>
<li>Hierarchie: L1 (le plus rapide), L2, L3</li>
</ul>

<p><strong>Organisation du cache</strong>:</p>

<p><strong>Cache a correspondance directe (direct-mapped)</strong>:</p>
<pre><code>Adresse memoire decomposee en:
  Tag | Index | Offset

Exemple: cache 16 KB, lignes de 64 octets
  Offset: 6 bits (64 = 2^6)
  Index: 8 bits (256 lignes)
  Tag: 18 bits (pour adresse 32 bits)
</code></pre>

<p><strong>Cache associatif par ensemble (set-associative)</strong>:</p>
<ul>
<li>N-way set-associative (2-way, 4-way, 8-way)</li>
<li>Compromis entre direct-mapped et fully associative</li>
<li>Politique de remplacement: LRU, Random, FIFO</li>
</ul>

<p><strong>Formules de performances</strong>:</p>
<pre><code>Temps d'acces moyen = Hit_time + Miss_rate x Miss_penalty

Taux de hit (hit rate) = Nombre de hits / Nombre total d'acces
Taux de miss (miss rate) = 1 - Hit rate

Exemple:
  Hit time = 1 cycle
  Miss penalty = 100 cycles
  Miss rate = 2%

  Temps moyen = 1 + 0.02 x 100 = 3 cycles
</code></pre>

<p><strong>Types de miss</strong>:</p>
<ul>
<li><strong>Compulsory miss</strong> (cold miss): premier acces</li>
<li><strong>Capacity miss</strong>: cache trop petit</li>
<li><strong>Conflict miss</strong>: collision dans direct-mapped</li>
</ul>

<p><strong>Coherence de cache</strong>:</p>
<ul>
<li>Probleme en multiprocesseur</li>
<li>Protocoles MESI, MOESI</li>
<li>Write-through vs write-back</li>
<li>Invalidation vs mise a jour</li>
</ul>

<p><strong>Supports de cours</strong>:
<a href="/cours-pdf/S5/Architecture-Informatique-Matérielle/4-les_caches.pdf">Les caches</a> (PDF)</p>

<h4>5. Architecture du Processeur</h4>

<p><strong>Processeur RISC (MIPS)</strong>:</p>
<ul>
<li>Jeu d'instructions reduit et regulier</li>
<li>Instructions de taille fixe (32 bits)</li>
<li>Load/Store architecture</li>
<li>Pipeline efficace</li>
</ul>

<p><strong>Registres MIPS</strong>:</p>
<pre><code>$zero ($0): toujours 0
$at ($1): reserve assembleur
$v0-$v1 ($2-$3): valeurs de retour
$a0-$a3 ($4-$7): arguments de fonction
$t0-$t9 ($8-$15, $24-$25): temporaires
$s0-$s7 ($16-$23): sauvegardes
$k0-$k1 ($26-$27): reserves OS
$gp ($28): pointeur global
$sp ($29): pointeur de pile
$fp ($30): pointeur de cadre
$ra ($31): adresse de retour
</code></pre>

<p><strong>Formats d'instructions</strong>:</p>

<p><strong>Format R</strong> (Register): operations arithmetiques/logiques</p>
<pre><code>| op (6) | rs (5) | rt (5) | rd (5) | shamt (5) | funct (6) |
Exemple: add $13, $11, $12
</code></pre>

<p><strong>Format I</strong> (Immediate): load/store, branches, constantes</p>
<pre><code>| op (6) | rs (5) | rt (5) | immediate (16) |
Exemple: addi $10, $zero, 53
</code></pre>

<p><strong>Format J</strong> (Jump): sauts inconditionnels</p>
<pre><code>| op (6) | address (26) |
Exemple: j add_32bits
</code></pre>

<p><strong>Pipeline du processeur</strong>:</p>
<ul>
<li><strong>IF</strong> (Instruction Fetch): chargement instruction</li>
<li><strong>ID</strong> (Instruction Decode): decodage et lecture registres</li>
<li><strong>EX</strong> (Execute): execution ALU</li>
<li><strong>MEM</strong> (Memory): acces memoire (load/store)</li>
<li><strong>WB</strong> (Write Back): ecriture resultat dans registre</li>
</ul>

<p><strong>Aleas de pipeline</strong> (hazards):</p>
<ul>
<li><strong>Aleas de donnees</strong>: RAW (Read After Write), WAR, WAW</li>
<li><strong>Aleas de controle</strong>: branches et sauts</li>
<li><strong>Aleas structurels</strong>: conflits de ressources</li>
</ul>

<p><strong>Solutions aux aleas</strong>:</p>
<ul>
<li>Forwarding (court-circuit)</li>
<li>Stall (bulles dans le pipeline)</li>
<li>Branch prediction (prediction de branchement)</li>
<li>Delayed branch</li>
</ul>

<p><strong>Supports de cours</strong>:
<a href="/cours-pdf/S5/Architecture-Informatique-Matérielle/5-Processeur.pdf">Architecture du processeur</a> (PDF)</p>

<hr/>

<h2>PART C: ASPECTS TECHNIQUES</h2>

<p>Cette section presente les elements techniques appris a travers les TPs et exercices pratiques.</p>

<h3>Programmation Assembleur MIPS</h3>

<h4>TP1: Addition 32 bits et Conversion de Temps</h4>

<p><strong>Code assembleur realise</strong>:</p>

<pre><code class="language-mips"># Initialisation des variables
addi $10, $zero, 53      # Secondes = 53
addi $1, $zero, 27       # Minutes = 27
addi $2, $zero, 3        # Heures = 3
j add_32bits             # Saut vers fonction addition

# Conversion temps en secondes totales
conv_secondes:
    addi $4, $zero, 3600     # $4 = 3600 (secondes/heure)
    addi $5, $zero, 60       # $5 = 60 (secondes/minute)
    mul $6, $2, $4           # $6 = heures x 3600
    mul $7, $1, $5           # $7 = minutes x 60
    add $8, $7, $6           # $8 = (heures x 3600) + (minutes x 60)
    add $9, $8, $10          # $9 = total + secondes

# Addition 32 bits avec detection de depassement
add_32bits:
    lw $11, var              # Charger variable a
    lw $12, var              # Charger variable b

    addu $13, $12, $11       # c = a + b (addition non signee)
    and $14, $11, $12        # e = a AND b (retenue entrante)
    xor $15, $11, $12        # x = a XOR b (somme sans retenue)

    not $18, $13             # Inversion de c
    and $16, $18, $15        # x AND (NOT c)
    or $17, $16, $14         # Calcul du bit de retenue sortante
    srl $21, $17, 31         # Decalage pour extraire bit de poids fort
                             # $21 contient le flag de depassement (overflow)

var: .word 0xFFFF0000        # Variable de test 32 bits
</code></pre>

<p><strong>Concepts appliques</strong>:</p>

<ol>
<li><strong>Instructions arithmetiques</strong>:
<ul>
<li><code>addi</code>: addition immediate (avec constante)</li>
<li><code>add</code> / <code>addu</code>: addition signee / non signee</li>
<li><code>mul</code>: multiplication</li>
</ul></li>

<li><strong>Instructions logiques</strong>:
<ul>
<li><code>and</code>: ET bit a bit</li>
<li><code>or</code>: OU bit a bit</li>
<li><code>xor</code>: OU exclusif bit a bit</li>
<li><code>not</code>: inversion (complement a 1)</li>
</ul></li>

<li><strong>Instructions memoire</strong>:
<ul>
<li><code>lw</code> (load word): chargement 32 bits depuis memoire</li>
<li>Directive <code>.word</code>: declaration de donnee 32 bits</li>
</ul></li>

<li><strong>Instructions de controle</strong>:
<ul>
<li><code>j</code> (jump): saut inconditionnel</li>
<li>Etiquettes pour les adresses</li>
</ul></li>

<li><strong>Gestion du depassement</strong>:
<ul>
<li>Detection de l'overflow sur addition</li>
<li>Utilisation de la logique booleenne pour calculer la retenue</li>
<li>Formule: <code>Overflow = Cout XOR Cin</code> (retenue sortante XOR entrante)</li>
</ul></li>
</ol>

<h4>Analyse de l'algorithme de detection de depassement</h4>

<p><strong>Principe mathematique</strong>:</p>
<pre><code>Pour detecter un depassement (overflow) sur addition:
  c = a + b
  e = a AND b  (positions ou a=1 et b=1, retenue garantie)
  x = a XOR b  (somme sans retenue)

  Retenue sortante = (x AND NOT(c)) OR e

  Si le bit de poids fort de la retenue = 1 → overflow
</code></pre>

<p><strong>Exemple numerique</strong>:</p>
<pre><code>a = 0xFFFF0000 (grand nombre negatif en complement a 2)
b = 0xFFFF0000
c = 0xFFFE0000 (resultat)

Analyse bit par bit du MSB (bit 31):
  a[31] = 1, b[31] = 1
  c[31] = 1

  Overflow detecte si signe change incorrectement
</code></pre>

<h3>Exercices de Calcul de Performances</h3>

<h4>Calcul du temps d'execution</h4>

<p><strong>Formule fondamentale</strong>:</p>
<pre><code>Temps_CPU = Nombre_instructions x CPI x Periode_horloge

Ou:
  CPI = Cycles Per Instruction
  Periode = 1 / Frequence
</code></pre>

<p><strong>Exemple d'exercice</strong>:</p>
<pre><code>Programme: 1 million d'instructions
CPI moyen: 2.5
Frequence CPU: 2 GHz

Temps_CPU = 10^6 x 2.5 x (1 / 2x10^9)
          = 2.5x10^6 / 2x10^9
          = 1.25 ms
</code></pre>

<h4>Performances du cache</h4>

<p><strong>Exercice type</strong>:</p>
<pre><code>Cache L1: 32 KB, 4-way associative, ligne 64 octets
  Hit time: 1 cycle
  Hit rate: 95%

RAM:
  Latence: 100 cycles

Calcul temps d'acces moyen:
  T_moy = 0.95 x 1 + 0.05 x 100
        = 0.95 + 5
        = 5.95 cycles

Amelioration par rapport a sans cache:
  Speedup = 100 / 5.95 = 16.8x
</code></pre>

<h4>Calcul de pagination</h4>

<p><strong>Exercice de traduction d'adresse</strong>:</p>
<pre><code>Configuration:
  - Pages de 4 KB (4096 octets = 2^12)
  - Adresses virtuelles 32 bits
  - Adresse physique 30 bits

Adresse virtuelle: 0x12345678

Decomposition:
  Bits 31-12: numero page virtuelle = 0x12345
  Bits 11-0:  offset = 0x678

Si table des pages indique: VPN 0x12345 → PFN 0x00ABC

Adresse physique:
  = (0x00ABC &lt;&lt; 12) | 0x678
  = 0x00ABC678
</code></pre>

<h3>Optimisation du Code</h3>

<h4>Exploitation du cache</h4>

<p><strong>Mauvaise utilisation</strong> (cache miss frequents):</p>
<pre><code class="language-c">// Parcours colonne par colonne (mauvaise localite spatiale)
for (int j = 0; j &lt; N; j++)
    for (int i = 0; i &lt; N; i++)
        sum += matrix[i][j];  // Acces non contigus
</code></pre>

<p><strong>Bonne utilisation</strong> (cache friendly):</p>
<pre><code class="language-c">// Parcours ligne par ligne (bonne localite spatiale)
for (int i = 0; i &lt; N; i++)
    for (int j = 0; j &lt; N; j++)
        sum += matrix[i][j];  // Acces contigus
</code></pre>

<p><strong>Explication</strong>:</p>
<ul>
<li>Les matrices en C sont stockees ligne par ligne (row-major order)</li>
<li>Lignes de cache: 64 octets = 16 entiers (4 octets chacun)</li>
<li>Parcours ligne → tous les elements d'une ligne charges ensemble</li>
<li>Parcours colonne → chaque acces charge une nouvelle ligne de cache</li>
</ul>

<h4>Blocking/Tiling pour matrices</h4>

<p><strong>Technique de blocking</strong>:</p>
<pre><code class="language-c">// Multiplication matricielle avec blocking
#define BLOCK_SIZE 32

for (int ii = 0; ii &lt; N; ii += BLOCK_SIZE)
    for (int jj = 0; jj &lt; N; jj += BLOCK_SIZE)
        for (int kk = 0; kk &lt; N; kk += BLOCK_SIZE)
            // Bloc de BLOCK_SIZE x BLOCK_SIZE
            for (int i = ii; i &lt; min(ii+BLOCK_SIZE, N); i++)
                for (int j = jj; j &lt; min(jj+BLOCK_SIZE, N); j++)
                    for (int k = kk; k &lt; min(kk+BLOCK_SIZE, N); k++)
                        C[i][j] += A[i][k] * B[k][j];
</code></pre>

<p><strong>Avantage</strong>: reutilisation des donnees en cache L1 avant eviction</p>

<hr/>

<h2>PART D: ANALYSE ET REFLEXION</h2>

<h3>Connaissances et competences mobilisees</h3>

<ul>
<li><strong>Architecture des systemes</strong>: comprehension profonde du fonctionnement materiel</li>
<li><strong>Programmation bas niveau</strong>: maitrise de l'assembleur MIPS</li>
<li><strong>Optimisation</strong>: capacite a ecrire du code efficace tenant compte du materiel</li>
<li><strong>Analyse de performances</strong>: calcul et optimisation des performances systeme</li>
<li><strong>Gestion memoire</strong>: comprehension des mecanismes de pagination et cache</li>
</ul>

<h3>Auto-evaluation</h3>

<p>Ce cours a ete fondamental pour ma comprehension des systemes informatiques. J'ai particulierement apprecie:</p>

<p><strong>Points forts</strong>:</p>
<ul>
<li><strong>Lien theorie/pratique</strong>: les TPs en assembleur MIPS ont rendu concrets les concepts abstraits</li>
<li><strong>Comprehension du materiel</strong>: vision claire de ce qui se passe "sous le capot"</li>
<li><strong>Optimisation</strong>: capacite a comprendre pourquoi certains codes sont plus rapides</li>
<li><strong>Debogage</strong>: meilleure comprehension des erreurs (segfault, cache miss, etc.)</li>
</ul>

<p><strong>Difficultes rencontrees</strong>:</p>
<ul>
<li><strong>Assembleur MIPS</strong>: syntaxe et conventions differentes du C</li>
<li><strong>Pipeline et hazards</strong>: concepts abstraits necessitant de la visualisation</li>
<li><strong>Calculs de cache</strong>: nombreuses formules et cas particuliers</li>
</ul>

<p><strong>Applications pratiques</strong>:</p>
<ul>
<li>Optimisation de code pour systemes embarques</li>
<li>Comprehension des contraintes temps reel</li>
<li>Choix d'algorithmes adaptes a l'architecture</li>
</ul>

<h3>Mon opinion</h3>

<p>Ce cours est indispensable pour tout ingenieur en informatique ou systemes embarques. Meme a l'ere des langages de haut niveau, comprendre l'architecture materielle permet:</p>

<ol>
<li><strong>Meilleure performance</strong>: code optimise pour le cache et le pipeline</li>
<li><strong>Debugging efficace</strong>: comprendre les erreurs memoire, les ralentissements</li>
<li><strong>Choix techniques</strong>: selectionner le bon processeur pour une application</li>
<li><strong>Embarque</strong>: conception de systemes avec contraintes strictes</li>
</ol>

<p><strong>Connexions avec autres cours</strong>:</p>
<ul>
<li><strong>Systemes d'exploitation</strong> (S5): gestion memoire virtuelle, ordonnancement</li>
<li><strong>Microcontroleur</strong> (S6): application pratique sur STM32</li>
<li><strong>Temps Reel</strong> (S8): contraintes de timing liees au materiel</li>
<li><strong>Systemes embarques</strong> (S7): optimisation pour ressources limitees</li>
</ul>

<p><strong>Evolution des architectures</strong>:</p>

<p>Aujourd'hui, les defis ont evolue:</p>
<ul>
<li><strong>Multiprocesseur</strong>: parallelisme, coherence cache complexe</li>
<li><strong>Heterogene</strong>: CPU + GPU + accelerateurs (TPU, NPU)</li>
<li><strong>Memoire non-volatile</strong>: nouvelles technologies (3D XPoint, ReRAM)</li>
<li><strong>Securite</strong>: Spectre, Meltdown → compromis performance/securite</li>
</ul>

<p>La <strong>loi de Moore</strong> ralentit, mais l'innovation continue:</p>
<ul>
<li>Architecture 3D (empilement)</li>
<li>Memoires proches du calcul (in-memory computing)</li>
<li>Architectures neuromorphiques</li>
<li>Calcul quantique (futur)</li>
</ul>

<p><strong>Recommandations pour bien reussir</strong>:</p>

<ol>
<li><strong>Pratiquer l'assembleur</strong>: ecrire du code MIPS, analyser le desassemblage C</li>
<li><strong>Visualiser</strong>: dessiner les pipelines, les caches, les tables de pages</li>
<li><strong>Calculer</strong>: faire et refaire les exercices de performances</li>
<li><strong>Lire les specifications</strong>: datasheets de processeurs (ARM, x86)</li>
<li><strong>Profiler</strong>: utiliser des outils (perf, valgrind) pour observer le cache</li>
</ol>

<p><strong>Applications professionnelles</strong>:</p>

<p>Ces connaissances sont utilisees dans:</p>
<ul>
<li><strong>Developpement de compilateurs</strong>: optimisations machine-specifiques</li>
<li><strong>Systemes d'exploitation</strong>: schedulers, gestionnaires memoire</li>
<li><strong>Jeux video</strong>: optimisations poussees pour FPS eleves</li>
<li><strong>HPC</strong> (High Performance Computing): supercalculateurs</li>
<li><strong>IoT</strong>: microcontroleurs a ressources limitees</li>
<li><strong>Automobile</strong>: ECU temps reel critiques</li>
<li><strong>Securite</strong>: analyse de vulnerabilites hardware</li>
</ul>

<p>En conclusion, ce cours fournit les bases essentielles pour comprendre comment le logiciel interagit avec le materiel. C'est un investissement qui porte ses fruits tout au long de la carriere, car les principes fondamentaux (hierarchie memoire, pipeline, cache) restent valables meme si les technologies evoluent.</p>

<hr/>

<h2>Documents de Cours</h2>

<p>Voici les supports de cours en PDF pour approfondir l'architecture informatique materielle :</p>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Introduction aux Architectures</h4>
      <p>Vue d'ensemble des architectures informatiques, evolution historique et concepts fondamentaux.</p>
      <embed src="/cours-pdf/S5/Architecture-Info/introduction.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S5/Architecture-Info/introduction.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Telecharger le PDF
        </a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Memoire Physique</h4>
      <p>Organisation de la memoire physique, types de memoires (RAM, ROM, Flash) et hierarchie memoire.</p>
      <embed src="/cours-pdf/S5/Architecture-Info/memoire-physique.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S5/Architecture-Info/memoire-physique.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Telecharger le PDF
        </a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Memoire Virtuelle</h4>
      <p>Gestion de la memoire virtuelle, pagination, segmentation et traduction d'adresses.</p>
      <embed src="/cours-pdf/S5/Architecture-Info/memoire-virtuelle.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S5/Architecture-Info/memoire-virtuelle.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Telecharger le PDF
        </a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Memoires Caches</h4>
      <p>Fonctionnement des caches, politiques de remplacement, coherence des caches et optimisation des performances.</p>
      <embed src="/cours-pdf/S5/Architecture-Info/caches.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S5/Architecture-Info/caches.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Telecharger le PDF
        </a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Processeur</h4>
      <p>Architecture du processeur, pipeline, parallelisme d'instructions et optimisations materielles.</p>
      <embed src="/cours-pdf/S5/Architecture-Info/processeur.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S5/Architecture-Info/processeur.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Telecharger le PDF
        </a>
      </p>
    </div>
  </div>
</div>

</div>

<!-- ==================== ENGLISH VERSION ==================== -->
<div class="lang-en">

<h1>Computer Hardware Architecture - S5</h1>

<p><strong>Year</strong>: 2022-2023 (Semester 5)<br/>
<strong>Credits</strong>: 3 ECTS<br/>
<strong>Type</strong>: Computer Science / System Architecture</p>

<hr/>

<h2>PART A: GENERAL OVERVIEW</h2>

<h3>Course Objectives</h3>

<p>The "Computer Hardware Architecture" course provides an in-depth understanding of the organization and operation of computer systems at the hardware level. It covers the entire memory hierarchy, processor architecture, and performance optimization mechanisms. This course is fundamental for understanding how hardware influences software performance and for designing efficient embedded systems.</p>

<div style="text-align: center;">
    <img src="/img/Courses/S5/Architecture-Informatique-Matérielle/archi-info-mat-vue.png" style="width: 70%;"/>
</div>
<br>

<h3>Targeted Skills</h3>

<ul>
<li>Master processor architecture concepts (RISC, pipeline, functional units)</li>
<li>Understand the memory hierarchy (physical memory, virtual memory, caches)</li>
<li>Analyze computer system performance</li>
<li>Program in MIPS assembly for low-level operations</li>
<li>Optimize code based on the hardware architecture</li>
<li>Understand pagination and memory management mechanisms</li>
</ul>

<h3>Organization</h3>

<ul>
<li><strong>Course hours</strong>: 30h (Lectures: 18h, Tutorials: 12h)</li>
<li><strong>Assessment</strong>: Written exam + Graded tutorials + Assembly lab</li>
<li><strong>Semester</strong>: 5 (2022-2023)</li>
<li><strong>Prerequisites</strong>: Sequential logic, digital systems</li>
</ul>

<hr/>

<h2>PART B: EXPERIENCE, CONTEXT AND PURPOSE</h2>

<h3>Course Content</h3>

<h4>1. General Introduction to Architectures</h4>

<p><strong>Fundamental concepts</strong>:</p>
<ul>
<li>Von Neumann vs Harvard architecture</li>
<li>Von Neumann model: single memory for data and instructions</li>
</ul>

<div style="text-align: center;">
    <img src="/img/Courses/S5/Architecture-Informatique-Matérielle/von-neumann.png" style="width: 30%;"/>
</div>

<ul>
<li>Harvard architecture: physical separation of instructions/data</li>
</ul>
<div style="text-align: center;">
    <img src="/img/Courses/S5/Architecture-Informatique-Matérielle/harvard.png" style="width: 60%;"/>
</div>
<ul>
<li>System bus: addresses, data, control</li>
<li>Execution cycle: Fetch-Decode-Execute</li>
</ul>

<p><strong>Historical evolution</strong>:</p>
<ul>
<li>From early computers to modern architectures</li>
<li>Moore's Law and its current limitations</li>
<li>Transition from single-processor to multi-processor</li>
<li>RISC (Reduced Instruction Set Computer) vs CISC (Complex) architectures</li>
</ul>

<p><strong>Performance measurement</strong>:</p>
<ul>
<li>CPI (Cycles Per Instruction)</li>
<li>MIPS (Millions of Instructions Per Second)</li>
<li>CPU execution time</li>
<li>Benchmarking and profiling</li>
</ul>

<p><strong>Course materials</strong>:
<a href="/cours-pdf/S5/Architecture-Informatique-Matérielle/1-Introduction_generale_architectures.pdf">General introduction to architectures</a> (PDF)</p>

<h4>2. Physical Memory</h4>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S5/architecture-info/von-neumann.svg" alt="Von Neumann Architecture" style="max-width: 550px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Von Neumann Architecture - Classic model with shared buses</p>
</div>

<p><strong>Memory organization</strong>:</p>
<ul>
<li>Memory hierarchy: registers → cache → RAM → disk</li>
<li>Memory technologies: SRAM, DRAM, ROM, Flash</li>
</ul>
<div style="text-align: center;">
    <img src="/img/Courses/S5/Architecture-Informatique-Matérielle/memoire.png" style="width: 60%;"/>
</div>
<ul>
<li>Access time and bandwidth</li>
<li>Locality principle (temporal and spatial)</li>
</ul>

<p><strong>Memory addressing</strong>:</p>
<ul>
<li>Linear address space</li>
<li>Word-addressable vs byte-addressable</li>
<li>Memory alignment and padding</li>
<li>Endianness (big-endian vs little-endian)</li>
</ul>

<p><strong>Data organization</strong>:</p>
<pre><code>32-bit memory organization example:
Address    |  Content (hex)
-----------|-----------------
0x00000000 |  0xAABBCCDD
0x00000004 |  0x11223344
0x00000008 |  0xFFFF0000
</code></pre>

<p><strong>Course materials</strong>:
<a href="/cours-pdf/S5/Architecture-Informatique-Matérielle/2-Memoire_physique.pdf">Physical memory</a> (PDF)</p>

<h4>3. Virtual Memory</h4>

<p><strong>Virtualization concepts</strong>:</p>
<ul>
<li>Separation of virtual address / physical address</li>
<li>Per-process address space</li>
<li>Memory protection and isolation</li>
<li>Memory sharing between processes</li>
</ul>

<p><strong>Paging mechanism</strong>:</p>
<ul>
<li>Virtual pages and physical frames</li>
<li>Typical page size: 4 KB, 2 MB (large pages)</li>
<li>Page table</li>
<li>TLB (Translation Lookaside Buffer): cache for address translations</li>
</ul>

<p><strong>Translation formulas</strong>:</p>
<pre><code>Virtual address = Virtual page number + Offset
Physical address = Physical frame number + Offset

Example with 4 KB pages (2^12 bytes):
Virtual address: 32 bits
  - 20 bits: page number (2^20 pages)
  - 12 bits: offset within the page (4096 bytes)
</code></pre>

<p><strong>Page fault handling</strong>:</p>
<ul>
<li>Page fault</li>
<li>Replacement algorithms: LRU, FIFO, Clock</li>
<li>Swapping and demand paging</li>
<li>Working set and thrashing</li>
</ul>

<p><strong>Multi-level page tables</strong>:</p>
<ul>
<li>2-level page table (x86)</li>
<li>3/4-level page table (x86-64)</li>
<li>Reducing memory space for tables</li>
<li>Inverted page table</li>
</ul>

<p><strong>Course materials</strong>:
<a href="/cours-pdf/S5/Architecture-Informatique-Matérielle/3-Memoire-virtuelle.pdf">Virtual memory</a> (PDF)</p>

<h4>4. Cache Memory</h4>

<p><strong>Cache principle</strong>:</p>
<ul>
<li>Cache located between CPU and RAM</li>
<li>Exploits spatial and temporal locality</li>
<li>Reduces average access time</li>
<li>Hierarchy: L1 (fastest), L2, L3</li>
</ul>

<p><strong>Cache organization</strong>:</p>

<p><strong>Direct-mapped cache</strong>:</p>
<pre><code>Memory address decomposed into:
  Tag | Index | Offset

Example: 16 KB cache, 64-byte lines
  Offset: 6 bits (64 = 2^6)
  Index: 8 bits (256 lines)
  Tag: 18 bits (for 32-bit address)
</code></pre>

<p><strong>Set-associative cache</strong>:</p>
<ul>
<li>N-way set-associative (2-way, 4-way, 8-way)</li>
<li>Compromise between direct-mapped and fully associative</li>
<li>Replacement policy: LRU, Random, FIFO</li>
</ul>

<p><strong>Performance formulas</strong>:</p>
<pre><code>Average access time = Hit_time + Miss_rate x Miss_penalty

Hit rate = Number of hits / Total number of accesses
Miss rate = 1 - Hit rate

Example:
  Hit time = 1 cycle
  Miss penalty = 100 cycles
  Miss rate = 2%

  Average time = 1 + 0.02 x 100 = 3 cycles
</code></pre>

<p><strong>Types of misses</strong>:</p>
<ul>
<li><strong>Compulsory miss</strong> (cold miss): first access</li>
<li><strong>Capacity miss</strong>: cache too small</li>
<li><strong>Conflict miss</strong>: collision in direct-mapped</li>
</ul>

<p><strong>Cache coherence</strong>:</p>
<ul>
<li>Multiprocessor challenge</li>
<li>MESI, MOESI protocols</li>
<li>Write-through vs write-back</li>
<li>Invalidation vs update</li>
</ul>

<p><strong>Course materials</strong>:
<a href="/cours-pdf/S5/Architecture-Informatique-Matérielle/4-les_caches.pdf">Caches</a> (PDF)</p>

<h4>5. Processor Architecture</h4>

<p><strong>RISC Processor (MIPS)</strong>:</p>
<ul>
<li>Reduced and regular instruction set</li>
<li>Fixed-size instructions (32 bits)</li>
<li>Load/Store architecture</li>
<li>Efficient pipeline</li>
</ul>

<p><strong>MIPS Registers</strong>:</p>
<pre><code>$zero ($0): always 0
$at ($1): reserved for assembler
$v0-$v1 ($2-$3): return values
$a0-$a3 ($4-$7): function arguments
$t0-$t9 ($8-$15, $24-$25): temporaries
$s0-$s7 ($16-$23): saved registers
$k0-$k1 ($26-$27): reserved for OS
$gp ($28): global pointer
$sp ($29): stack pointer
$fp ($30): frame pointer
$ra ($31): return address
</code></pre>

<p><strong>Instruction formats</strong>:</p>

<p><strong>R-format</strong> (Register): arithmetic/logic operations</p>
<pre><code>| op (6) | rs (5) | rt (5) | rd (5) | shamt (5) | funct (6) |
Example: add $13, $11, $12
</code></pre>

<p><strong>I-format</strong> (Immediate): load/store, branches, constants</p>
<pre><code>| op (6) | rs (5) | rt (5) | immediate (16) |
Example: addi $10, $zero, 53
</code></pre>

<p><strong>J-format</strong> (Jump): unconditional jumps</p>
<pre><code>| op (6) | address (26) |
Example: j add_32bits
</code></pre>

<p><strong>Processor pipeline</strong>:</p>
<ul>
<li><strong>IF</strong> (Instruction Fetch): load instruction</li>
<li><strong>ID</strong> (Instruction Decode): decode and read registers</li>
<li><strong>EX</strong> (Execute): ALU execution</li>
<li><strong>MEM</strong> (Memory): memory access (load/store)</li>
<li><strong>WB</strong> (Write Back): write result to register</li>
</ul>

<p><strong>Pipeline hazards</strong>:</p>
<ul>
<li><strong>Data hazards</strong>: RAW (Read After Write), WAR, WAW</li>
<li><strong>Control hazards</strong>: branches and jumps</li>
<li><strong>Structural hazards</strong>: resource conflicts</li>
</ul>

<p><strong>Hazard solutions</strong>:</p>
<ul>
<li>Forwarding (bypassing)</li>
<li>Stalling (pipeline bubbles)</li>
<li>Branch prediction</li>
<li>Delayed branch</li>
</ul>

<p><strong>Course materials</strong>:
<a href="/cours-pdf/S5/Architecture-Informatique-Matérielle/5-Processeur.pdf">Processor architecture</a> (PDF)</p>

<hr/>

<h2>PART C: TECHNICAL ASPECTS</h2>

<p>This section presents the technical elements learned through lab sessions and practical exercises.</p>

<h3>MIPS Assembly Programming</h3>

<h4>Lab 1: 32-bit Addition and Time Conversion</h4>

<p><strong>Assembly code written</strong>:</p>

<pre><code class="language-mips"># Variable initialization
addi $10, $zero, 53      # Seconds = 53
addi $1, $zero, 27       # Minutes = 27
addi $2, $zero, 3        # Hours = 3
j add_32bits             # Jump to addition function

# Time conversion to total seconds
conv_secondes:
    addi $4, $zero, 3600     # $4 = 3600 (seconds/hour)
    addi $5, $zero, 60       # $5 = 60 (seconds/minute)
    mul $6, $2, $4           # $6 = hours x 3600
    mul $7, $1, $5           # $7 = minutes x 60
    add $8, $7, $6           # $8 = (hours x 3600) + (minutes x 60)
    add $9, $8, $10          # $9 = total + seconds

# 32-bit addition with overflow detection
add_32bits:
    lw $11, var              # Load variable a
    lw $12, var              # Load variable b

    addu $13, $12, $11       # c = a + b (unsigned addition)
    and $14, $11, $12        # e = a AND b (incoming carry)
    xor $15, $11, $12        # x = a XOR b (sum without carry)

    not $18, $13             # Invert c
    and $16, $18, $15        # x AND (NOT c)
    or $17, $16, $14         # Compute outgoing carry bit
    srl $21, $17, 31         # Shift to extract most significant bit
                             # $21 contains the overflow flag

var: .word 0xFFFF0000        # 32-bit test variable
</code></pre>

<p><strong>Applied concepts</strong>:</p>

<ol>
<li><strong>Arithmetic instructions</strong>:
<ul>
<li><code>addi</code>: immediate addition (with constant)</li>
<li><code>add</code> / <code>addu</code>: signed / unsigned addition</li>
<li><code>mul</code>: multiplication</li>
</ul></li>

<li><strong>Logical instructions</strong>:
<ul>
<li><code>and</code>: bitwise AND</li>
<li><code>or</code>: bitwise OR</li>
<li><code>xor</code>: bitwise exclusive OR</li>
<li><code>not</code>: inversion (one's complement)</li>
</ul></li>

<li><strong>Memory instructions</strong>:
<ul>
<li><code>lw</code> (load word): 32-bit load from memory</li>
<li><code>.word</code> directive: 32-bit data declaration</li>
</ul></li>

<li><strong>Control instructions</strong>:
<ul>
<li><code>j</code> (jump): unconditional jump</li>
<li>Labels for addresses</li>
</ul></li>

<li><strong>Overflow handling</strong>:
<ul>
<li>Overflow detection on addition</li>
<li>Using Boolean logic to compute the carry</li>
<li>Formula: <code>Overflow = Cout XOR Cin</code> (outgoing carry XOR incoming carry)</li>
</ul></li>
</ol>

<h4>Analysis of the Overflow Detection Algorithm</h4>

<p><strong>Mathematical principle</strong>:</p>
<pre><code>To detect overflow on addition:
  c = a + b
  e = a AND b  (positions where a=1 and b=1, guaranteed carry)
  x = a XOR b  (sum without carry)

  Outgoing carry = (x AND NOT(c)) OR e

  If the most significant bit of the carry = 1 → overflow
</code></pre>

<p><strong>Numerical example</strong>:</p>
<pre><code>a = 0xFFFF0000 (large negative number in two's complement)
b = 0xFFFF0000
c = 0xFFFE0000 (result)

Bit-by-bit analysis of MSB (bit 31):
  a[31] = 1, b[31] = 1
  c[31] = 1

  Overflow detected if sign changes incorrectly
</code></pre>

<h3>Performance Calculation Exercises</h3>

<h4>Execution Time Calculation</h4>

<p><strong>Fundamental formula</strong>:</p>
<pre><code>CPU_Time = Number_of_instructions x CPI x Clock_period

Where:
  CPI = Cycles Per Instruction
  Period = 1 / Frequency
</code></pre>

<p><strong>Exercise example</strong>:</p>
<pre><code>Program: 1 million instructions
Average CPI: 2.5
CPU frequency: 2 GHz

CPU_Time = 10^6 x 2.5 x (1 / 2x10^9)
         = 2.5x10^6 / 2x10^9
         = 1.25 ms
</code></pre>

<h4>Cache Performance</h4>

<p><strong>Typical exercise</strong>:</p>
<pre><code>L1 Cache: 32 KB, 4-way associative, 64-byte line
  Hit time: 1 cycle
  Hit rate: 95%

RAM:
  Latency: 100 cycles

Average access time calculation:
  T_avg = 0.95 x 1 + 0.05 x 100
        = 0.95 + 5
        = 5.95 cycles

Improvement compared to no cache:
  Speedup = 100 / 5.95 = 16.8x
</code></pre>

<h4>Paging Calculation</h4>

<p><strong>Address translation exercise</strong>:</p>
<pre><code>Configuration:
  - 4 KB pages (4096 bytes = 2^12)
  - 32-bit virtual addresses
  - 30-bit physical address

Virtual address: 0x12345678

Decomposition:
  Bits 31-12: virtual page number = 0x12345
  Bits 11-0:  offset = 0x678

If page table indicates: VPN 0x12345 → PFN 0x00ABC

Physical address:
  = (0x00ABC &lt;&lt; 12) | 0x678
  = 0x00ABC678
</code></pre>

<h3>Code Optimization</h3>

<h4>Cache Exploitation</h4>

<p><strong>Poor usage</strong> (frequent cache misses):</p>
<pre><code class="language-c">// Column-by-column traversal (poor spatial locality)
for (int j = 0; j &lt; N; j++)
    for (int i = 0; i &lt; N; i++)
        sum += matrix[i][j];  // Non-contiguous accesses
</code></pre>

<p><strong>Good usage</strong> (cache friendly):</p>
<pre><code class="language-c">// Row-by-row traversal (good spatial locality)
for (int i = 0; i &lt; N; i++)
    for (int j = 0; j &lt; N; j++)
        sum += matrix[i][j];  // Contiguous accesses
</code></pre>

<p><strong>Explanation</strong>:</p>
<ul>
<li>Matrices in C are stored row by row (row-major order)</li>
<li>Cache lines: 64 bytes = 16 integers (4 bytes each)</li>
<li>Row traversal → all elements of a row loaded together</li>
<li>Column traversal → each access loads a new cache line</li>
</ul>

<h4>Blocking/Tiling for Matrices</h4>

<p><strong>Blocking technique</strong>:</p>
<pre><code class="language-c">// Matrix multiplication with blocking
#define BLOCK_SIZE 32

for (int ii = 0; ii &lt; N; ii += BLOCK_SIZE)
    for (int jj = 0; jj &lt; N; jj += BLOCK_SIZE)
        for (int kk = 0; kk &lt; N; kk += BLOCK_SIZE)
            // Block of BLOCK_SIZE x BLOCK_SIZE
            for (int i = ii; i &lt; min(ii+BLOCK_SIZE, N); i++)
                for (int j = jj; j &lt; min(jj+BLOCK_SIZE, N); j++)
                    for (int k = kk; k &lt; min(kk+BLOCK_SIZE, N); k++)
                        C[i][j] += A[i][k] * B[k][j];
</code></pre>

<p><strong>Advantage</strong>: reuse of data in L1 cache before eviction</p>

<hr/>

<h2>PART D: ANALYSIS AND REFLECTION</h2>

<h3>Knowledge and Skills Mobilized</h3>

<ul>
<li><strong>System architecture</strong>: deep understanding of hardware operation</li>
<li><strong>Low-level programming</strong>: mastery of MIPS assembly</li>
<li><strong>Optimization</strong>: ability to write efficient code accounting for hardware</li>
<li><strong>Performance analysis</strong>: computing and optimizing system performance</li>
<li><strong>Memory management</strong>: understanding of paging and caching mechanisms</li>
</ul>

<h3>Self-Assessment</h3>

<p>This course was fundamental for my understanding of computer systems. I particularly appreciated:</p>

<p><strong>Strengths</strong>:</p>
<ul>
<li><strong>Theory/practice connection</strong>: MIPS assembly labs made abstract concepts tangible</li>
<li><strong>Hardware understanding</strong>: clear vision of what happens "under the hood"</li>
<li><strong>Optimization</strong>: ability to understand why certain code is faster</li>
<li><strong>Debugging</strong>: better understanding of errors (segfault, cache miss, etc.)</li>
</ul>

<p><strong>Difficulties encountered</strong>:</p>
<ul>
<li><strong>MIPS assembly</strong>: syntax and conventions different from C</li>
<li><strong>Pipeline and hazards</strong>: abstract concepts requiring visualization</li>
<li><strong>Cache calculations</strong>: numerous formulas and special cases</li>
</ul>

<p><strong>Practical applications</strong>:</p>
<ul>
<li>Code optimization for embedded systems</li>
<li>Understanding real-time constraints</li>
<li>Choosing algorithms suited to the architecture</li>
</ul>

<h3>My Opinion</h3>

<p>This course is essential for any engineer in computer science or embedded systems. Even in the era of high-level languages, understanding hardware architecture enables:</p>

<ol>
<li><strong>Better performance</strong>: code optimized for cache and pipeline</li>
<li><strong>Effective debugging</strong>: understanding memory errors and slowdowns</li>
<li><strong>Technical decisions</strong>: selecting the right processor for an application</li>
<li><strong>Embedded systems</strong>: designing systems with strict constraints</li>
</ol>

<p><strong>Connections with other courses</strong>:</p>
<ul>
<li><strong>Operating Systems</strong> (S5): virtual memory management, scheduling</li>
<li><strong>Microcontroller</strong> (S6): practical application on STM32</li>
<li><strong>Real-Time Systems</strong> (S8): timing constraints related to hardware</li>
<li><strong>Embedded Systems</strong> (S7): optimization for limited resources</li>
</ul>

<p><strong>Evolution of architectures</strong>:</p>

<p>Today, challenges have evolved:</p>
<ul>
<li><strong>Multiprocessor</strong>: parallelism, complex cache coherence</li>
<li><strong>Heterogeneous</strong>: CPU + GPU + accelerators (TPU, NPU)</li>
<li><strong>Non-volatile memory</strong>: new technologies (3D XPoint, ReRAM)</li>
<li><strong>Security</strong>: Spectre, Meltdown → performance/security trade-offs</li>
</ul>

<p><strong>Moore's Law</strong> is slowing down, but innovation continues:</p>
<ul>
<li>3D architecture (stacking)</li>
<li>Near-memory computing (in-memory computing)</li>
<li>Neuromorphic architectures</li>
<li>Quantum computing (future)</li>
</ul>

<p><strong>Recommendations for success</strong>:</p>

<ol>
<li><strong>Practice assembly</strong>: write MIPS code, analyze C disassembly</li>
<li><strong>Visualize</strong>: draw pipelines, caches, page tables</li>
<li><strong>Calculate</strong>: do and redo performance exercises</li>
<li><strong>Read specifications</strong>: processor datasheets (ARM, x86)</li>
<li><strong>Profile</strong>: use tools (perf, valgrind) to observe cache behavior</li>
</ol>

<p><strong>Professional applications</strong>:</p>

<p>This knowledge is used in:</p>
<ul>
<li><strong>Compiler development</strong>: machine-specific optimizations</li>
<li><strong>Operating systems</strong>: schedulers, memory managers</li>
<li><strong>Video games</strong>: advanced optimizations for high FPS</li>
<li><strong>HPC</strong> (High Performance Computing): supercomputers</li>
<li><strong>IoT</strong>: resource-constrained microcontrollers</li>
<li><strong>Automotive</strong>: safety-critical real-time ECUs</li>
<li><strong>Security</strong>: hardware vulnerability analysis</li>
</ul>

<p>In conclusion, this course provides the essential foundations for understanding how software interacts with hardware. It is an investment that pays off throughout one's career, as the fundamental principles (memory hierarchy, pipeline, cache) remain valid even as technologies evolve.</p>

<hr/>

<h2>Course Documents</h2>

<p>Here are the course materials in PDF format to deepen your understanding of computer hardware architecture:</p>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Introduction to Architectures</h4>
      <p>Overview of computer architectures, historical evolution and fundamental concepts.</p>
      <embed src="/cours-pdf/S5/Architecture-Info/introduction.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S5/Architecture-Info/introduction.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Download PDF
        </a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Physical Memory</h4>
      <p>Physical memory organization, memory types (RAM, ROM, Flash) and memory hierarchy.</p>
      <embed src="/cours-pdf/S5/Architecture-Info/memoire-physique.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S5/Architecture-Info/memoire-physique.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Download PDF
        </a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Virtual Memory</h4>
      <p>Virtual memory management, paging, segmentation and address translation.</p>
      <embed src="/cours-pdf/S5/Architecture-Info/memoire-virtuelle.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S5/Architecture-Info/memoire-virtuelle.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Download PDF
        </a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Cache Memory</h4>
      <p>How caches work, replacement policies, cache coherence and performance optimization.</p>
      <embed src="/cours-pdf/S5/Architecture-Info/caches.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S5/Architecture-Info/caches.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Download PDF
        </a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Processor</h4>
      <p>Processor architecture, pipeline, instruction-level parallelism and hardware optimizations.</p>
      <embed src="/cours-pdf/S5/Architecture-Info/processeur.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S5/Architecture-Info/processeur.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Download PDF
        </a>
      </p>
    </div>
  </div>
</div>

</div>

<div class="back-nav">
  <a href="./my-courses-2022-2023.html" data-i18n-html="back-courses-2022-2023">← Retour aux Cours 2022-2023</a>
</div>

<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f9;
        color: #333;
        line-height: 1.6;
    }
    h2, h3, h4 {
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

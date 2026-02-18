---
layout: default
title: "Logique Séquentielle - S5"
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
  <a href="./my-courses-2022-2023.html" data-i18n-html="back_courses_2022_2023">&#8592; Retour à Mes Cours 2022-2023</a>
</div>

<div class="lang-fr">

<h1>Logique Sequentielle - S5</h1>

<p><strong>Annee</strong>: 2022-2023 (Semestre 5)<br/>
<strong>Credits</strong>: 3 ECTS<br/>
<strong>Type</strong>: Electronique Numerique</p>

<hr/>

<h2>PART A: PRESENTATION GENERALE</h2>

<h3>Objectifs du cours</h3>

<p>Le cours de Logique Sequentielle approfondit la conception de circuits numeriques dont l'etat depend de l'historique des entrees. Il couvre les machines a etats finis (FSM), la conception synchrone et asynchrone, ainsi que les methodes systematiques de conception de systemes sequentiels complexes. Ce cours est fondamental pour concevoir des controleurs numeriques, des protocoles de communication et des systemes embarques.</p>

<h3>Competences visees</h3>

<ul>
  <li>Maitriser les bascules et elements de memorisation</li>
  <li>Concevoir des machines a etats finis (Moore et Mealy)</li>
  <li>Analyser et synthetiser des circuits sequentiels</li>
  <li>Gerer les contraintes temporelles et la synchronisation</li>
  <li>Implementer des controleurs complexes</li>
  <li>Optimiser les codages d'etats</li>
</ul>

<h3>Organisation</h3>

<ul>
  <li><strong>Volume horaire</strong>: 32h (CM: 18h, TD: 14h)</li>
  <li><strong>Evaluation</strong>: Examen final (70%) + TDs (30%)</li>
  <li><strong>Semestre</strong>: 5 (2022-2023)</li>
  <li><strong>Prerequis</strong>: Logique combinatoire, algebre de Boole</li>
</ul>

<hr/>

<h2>PART B: EXPERIENCE, CONTEXTE ET FONCTION</h2>

<h3>Contenu pedagogique</h3>

<h4>1. Elements de Memorisation</h4>

<p><strong>Bascules et Latches</strong>:</p>

<p>Les circuits sequentiels utilisent des elements memoire pour stocker l'etat.</p>

<p><strong>Latch SR (Set-Reset)</strong>:</p>
<pre><code>S R | Q  Q'
----|-------
0 0 | Q  Q'  (memorisation)
0 1 | 0  1   (reset)
1 0 | 1  0   (set)
1 1 | X  X   (interdit)</code></pre>

<p><strong>Bascule D (Data)</strong>:</p>

<p>La plus utilisee en conception synchrone.</p>
<ul>
  <li>Sur front montant d'horloge: Q = D</li>
  <li>Memorise la valeur de D</li>
</ul>

<p><strong>Equation caracteristique</strong>: Q(t+1) = D(t)</p>

<p><strong>Bascule JK</strong>:</p>
<pre><code>J K | Q(t+1)
----|--------
0 0 | Q      (memorisation)
0 1 | 0      (reset)
1 0 | 1      (set)
1 1 | Q'     (toggle)</code></pre>

<p><strong>Bascule T (Toggle)</strong>:</p>

<p>Quand T=1, la sortie bascule: Q(t+1) = Q'(t)</p>

<p><strong>Contraintes temporelles</strong>:</p>

<ul>
  <li><strong>Setup time</strong> (tsu): temps avant front d'horloge ou D doit etre stable</li>
  <li><strong>Hold time</strong> (th): temps apres front ou D doit rester stable</li>
  <li><strong>Propagation delay</strong> (tpd): delai entre front CLK et changement de Q</li>
</ul>

<h4>2. Machines a Etats Finis (FSM)</h4>

<p><strong>FSM de Moore</strong>:</p>

<p>Les sorties dependent uniquement de l'etat courant.</p>

<p>Structure:</p>
<ul>
  <li>Etats</li>
  <li>Transitions (dependent des entrees)</li>
  <li>Sorties (fonction de l'etat uniquement)</li>
</ul>

<p><strong>Exemple: Detecteur de sequence "101"</strong></p>

<p>Diagramme d'etats Moore:</p>
<pre><code>S0 (init, out=0) --[1]--&gt; S1 (out=0)
S1 --[0]--&gt; S2 (out=0)
S2 --[1]--&gt; S3 (out=1)  // Sequence detectee!
S3 --[x]--&gt; ...</code></pre>

<p><strong>FSM de Mealy</strong>:</p>

<p>Les sorties dependent de l'etat ET des entrees.</p>

<p>Avantage: souvent moins d'etats que Moore.</p>

<p><strong>Comparaison</strong>:</p>
<ul>
  <li>Moore: sorties stables (changent seulement sur front d'horloge)</li>
  <li>Mealy: reaction plus rapide (sorties changent avec entrees)</li>
</ul>

<h4>3. Methodologie de Conception</h4>

<p><strong>Etapes de conception d'une FSM</strong>:</p>

<ol>
  <li><strong>Specification</strong>: definir le comportement souhaite</li>
  <li><strong>Diagramme d'etats</strong>: representation graphique</li>
  <li><strong>Table d'etats</strong>: forme tabulaire</li>
  <li><strong>Minimisation</strong>: reduire le nombre d'etats</li>
  <li><strong>Codage d'etats</strong>: assigner codes binaires</li>
  <li><strong>Equations logiques</strong>: deriver next-state et output logic</li>
  <li><strong>Implementation</strong>: bascules + portes logiques</li>
</ol>

<p><strong>Exemple: Controleur de feu tricolore</strong></p>

<p>Etats:</p>
<ul>
  <li>VERT (30s)</li>
  <li>ORANGE (5s)</li>
  <li>ROUGE (35s)</li>
</ul>

<p>Entrees: timer, capteur vehicule<br/>
Sorties: LED_V, LED_O, LED_R</p>

<p><strong>Table d'etats simplifiee</strong>:</p>
<pre><code>Etat actuel | Timer | Etat suivant | Sorties
------------|-------|--------------|----------
VERT        | 0     | VERT         | V=1,O=0,R=0
VERT        | 1     | ORANGE       | V=1,O=0,R=0
ORANGE      | 0     | ORANGE       | V=0,O=1,R=0
ORANGE      | 1     | ROUGE        | V=0,O=1,R=0
ROUGE       | 0     | ROUGE        | V=0,O=0,R=1
ROUGE       | 1     | VERT         | V=0,O=0,R=1</code></pre>

<h4>4. Codage d'Etats</h4>

<p><strong>Binaire naturel</strong>:</p>
<ul>
  <li>n bits pour 2^n etats</li>
  <li>Exemple 4 etats: 00, 01, 10, 11</li>
  <li>Economie de bascules</li>
</ul>

<p><strong>One-Hot</strong>:</p>
<ul>
  <li>1 bascule par etat</li>
  <li>Exemple 4 etats: 0001, 0010, 0100, 1000</li>
  <li>Logique de decodage simplifiee</li>
  <li>Utilise en FPGA</li>
</ul>

<p><strong>Gray</strong>:</p>
<ul>
  <li>1 seul bit change entre etats adjacents</li>
  <li>Reduit les aleas (glitches)</li>
  <li>Utile en asynchrone</li>
</ul>

<p><strong>Exemple 4 etats</strong>:</p>
<pre><code>Etat | Binaire | One-Hot | Gray
-----|---------|---------|------
S0   | 00      | 0001    | 00
S1   | 01      | 0010    | 01
S2   | 10      | 0100    | 11
S3   | 11      | 1000    | 10</code></pre>

<h4>5. Conception Synchrone</h4>

<p><strong>Regles de conception synchrone</strong>:</p>

<ul>
  <li>Toutes les bascules partagent la meme horloge</li>
  <li>Pas de logique combinatoire dans le chemin d'horloge</li>
  <li>Respecter les contraintes setup/hold</li>
</ul>

<p><strong>Frequence maximale</strong>:</p>

<p>fmax = 1 / (tpd_logic + tsu + tskew)</p>

<p>ou:</p>
<ul>
  <li>tpd_logic: delai combinatoire entre bascules</li>
  <li>tsu: setup time</li>
  <li>tskew: decalage d'horloge (clock skew)</li>
</ul>

<p><strong>Strategies de reset</strong>:</p>

<p><strong>Reset asynchrone</strong>:</p>
<pre><code>if (reset = '1') then
    state &lt;= S0;
elsif rising_edge(clk) then
    state &lt;= next_state;
end if;</code></pre>

<p>Avantage: reinitialisation immediate<br/>
Inconvenient: peut causer metastabilite</p>

<p><strong>Reset synchrone</strong>:</p>
<pre><code>if rising_edge(clk) then
    if (reset = '1') then
        state &lt;= S0;
    else
        state &lt;= next_state;
    end if;
end if;</code></pre>

<p>Avantage: synchronise avec horloge<br/>
Inconvenient: delai d'un cycle</p>

<h4>6. Compteurs Avances</h4>

<p><strong>Compteur modulo-N</strong>:</p>

<p>Compte de 0 a N-1 puis revient a 0.</p>

<p><strong>Compteur decimal BCD</strong>:<br/>
Compte de 0 a 9 (0000 a 1001).</p>

<p><strong>Compteur up/down</strong>:</p>

<p>Entree DIR: 1=up, 0=down</p>

<p><strong>Exemple 3 bits up/down</strong>:</p>
<pre><code>UP:   000 -&gt; 001 -&gt; 010 -&gt; 011 -&gt; 100 -&gt; 101 -&gt; 110 -&gt; 111 -&gt; 000
DOWN: 111 -&gt; 110 -&gt; 101 -&gt; 100 -&gt; 011 -&gt; 010 -&gt; 001 -&gt; 000 -&gt; 111</code></pre>

<p><strong>Compteur avec prechargement</strong>:</p>

<p>Entree LOAD: charge valeur initiale<br/>
Utilite: division de frequence precise</p>

<h4>7. Aspects Temporels</h4>

<p><strong>Metastabilite</strong>:</p>

<p>Phenomene lorsque setup/hold time violes.<br/>
La bascule peut rester dans etat indetermine.</p>

<p><strong>Solution</strong>: Synchroniseur a 2 etages</p>
<pre><code>Entree asynchrone -&gt; [FF1] -&gt; [FF2] -&gt; Sortie synchrone
                       CLK      CLK</code></pre>

<p>Reduit probabilite de metastabilite a ~10^-12.</p>

<p><strong>Analyse de chemin critique</strong>:</p>

<p>Identifier le chemin logique le plus long entre deux bascules.</p>

<p>Exemple:</p>
<pre><code>FF1 --[tpd=2ns]--&gt; NAND --[tpd=3ns]--&gt; XOR --[tpd=4ns]--&gt; FF2
                                                          [tsu=1ns]</code></pre>

<p>Delai total: 2 + 3 + 4 + 1 = 10ns<br/>
Frequence max: 1/10ns = 100MHz</p>

<p><strong>Supports de cours</strong>:<br/>
<a href="/cours-pdf/S5/Logique-Séquentielle/Poly2022.pdf">Cours Logique Sequentielle</a></p>

<hr/>

<h2>PART C: ASPECTS TECHNIQUES</h2>

<h3>Exercices de TD</h3>

<p><strong>TD1: Conception de FSM</strong></p>

<p>Exercice: Concevoir un detecteur de sequence "1011" (non chevauchant).</p>

<p><strong>Solution</strong>:</p>

<p>Etats necessaires:</p>
<ul>
  <li>S0: etat initial</li>
  <li>S1: apres "1"</li>
  <li>S2: apres "10"</li>
  <li>S3: apres "101"</li>
  <li>S4: sequence complete detectee</li>
</ul>

<p>Table de transition:</p>
<pre><code>Etat | Entree 0 | Entree 1 | Sortie
-----|----------|----------|--------
S0   | S0       | S1       | 0
S1   | S2       | S1       | 0
S2   | S0       | S3       | 0
S3   | S0       | S4       | 0
S4   | S0       | S1       | 1</code></pre>

<p><strong>TD2: Codage et equations</strong></p>

<p>Pour 4 etats codes en binaire:</p>
<ul>
  <li>Q1 Q0 = 00 (S0), 01 (S1), 10 (S2), 11 (S3)</li>
</ul>

<p>Deriver equations next-state avec Karnaugh.</p>

<p><strong>TD3: Analyse temporelle</strong></p>

<p>Calculer frequence maximale d'un circuit avec:</p>
<ul>
  <li>tpd_FF = 5ns</li>
  <li>tpd_comb = 15ns</li>
  <li>tsu = 3ns</li>
  <li>tskew = 1ns</li>
</ul>

<p>Solution:<br/>
Periode minimale = 5 + 15 + 3 + 1 = 24ns<br/>
fmax = 1/24ns = 41.67MHz</p>

<h3>Applications Pratiques</h3>

<p><strong>Controleur UART (emetteur)</strong>:</p>

<p>Etats:</p>
<ul>
  <li>IDLE: attente donnees</li>
  <li>START: envoi bit de start</li>
  <li>DATA0-DATA7: envoi 8 bits de donnees</li>
  <li>STOP: bit de stop</li>
  <li>Retour IDLE</li>
</ul>

<p><strong>Decodeur de protocole I2C</strong>:</p>

<p>FSM detectant:</p>
<ul>
  <li>Condition START (SDA chute avec SCL=1)</li>
  <li>Adresse (7 bits)</li>
  <li>R/W bit</li>
  <li>ACK/NACK</li>
  <li>Donnees</li>
  <li>Condition STOP (SDA monte avec SCL=1)</li>
</ul>

<p><strong>Controleur de distributeur automatique</strong>:</p>

<p>Entrees: pieces inserees (5c, 10c, 25c)<br/>
Sortie: produit delivre si montant atteint</p>

<p>Etats representent le credit accumule.</p>

<h3>Outils de Conception</h3>

<p><strong>Simulateurs</strong>:</p>
<ul>
  <li>Logisim: simulation graphique</li>
  <li>ModelSim: simulation VHDL/Verilog</li>
  <li>Quartus: suite complete Altera/Intel</li>
</ul>

<p><strong>Langages de description</strong>:</p>

<p><strong>VHDL exemple (FSM Moore)</strong>:</p>
<pre><code>process(clk, reset)
begin
    if reset = '1' then
        state &lt;= S0;
    elsif rising_edge(clk) then
        case state is
            when S0 =&gt;
                if input = '1' then
                    state &lt;= S1;
                end if;
            when S1 =&gt;
                -- transitions...
        end case;
    end if;
end process;

-- Logique de sortie Moore
output &lt;= '1' when state = S3 else '0';</code></pre>

<p><strong>Verilog exemple (FSM Mealy)</strong>:</p>
<pre><code>always @(posedge clk or posedge reset) begin
    if (reset)
        state &lt;= S0;
    else
        state &lt;= next_state;
end

// Logique next_state et output (combinatoire)
always @(*) begin
    case (state)
        S0: begin
            if (input)
                next_state = S1;
            output = 1'b0;
        end
        // ...
    endcase
end</code></pre>

<hr/>

<h2>PART D: ANALYSE ET REFLEXION</h2>

<h3>Competences acquises</h3>

<p><strong>Techniques</strong>:</p>
<ul>
  <li>Conception systematique de FSM</li>
  <li>Optimisation de codage d'etats</li>
  <li>Analyse temporelle de circuits sequentiels</li>
  <li>Gestion de la synchronisation</li>
  <li>Implementation en VHDL/Verilog</li>
</ul>

<p><strong>Methodologiques</strong>:</p>
<ul>
  <li>Demarche de conception rigoureuse</li>
  <li>Tests et verification de FSM</li>
  <li>Documentation (diagrammes d'etats)</li>
  <li>Debogage de circuits sequentiels</li>
</ul>

<h3>Applications professionnelles</h3>

<p>La logique sequentielle est utilisee dans:</p>
<ul>
  <li><strong>Protocoles de communication</strong>: UART, SPI, I2C, USB</li>
  <li><strong>Controleurs</strong>: machines, robots, process industriels</li>
  <li><strong>Interfaces</strong>: LCD, clavier, souris, touchscreen</li>
  <li><strong>Processeurs</strong>: unite de controle, pipelines</li>
  <li><strong>Stockage</strong>: controleurs de memoire, cache</li>
  <li><strong>Reseaux</strong>: routeurs, switches, protocoles</li>
</ul>

<h3>Connexions avec autres cours</h3>

<ul>
  <li><strong>Fondements Electronique Numerique</strong> (S5): base (bascules, compteurs)</li>
  <li><strong>Architectures Numeriques VHDL</strong> (S7): implementation FPGA</li>
  <li><strong>Microcontroleurs</strong> (S6): FSM dans firmware</li>
  <li><strong>Temps Reel</strong> (S8): ordonnancement et synchronisation</li>
  <li><strong>Reseaux</strong> (S6): protocoles en couches FSM</li>
</ul>

<h3>Evolution et Perspectives</h3>

<p><strong>Outils modernes</strong>:</p>
<ul>
  <li>Synthese automatique depuis FSM graphiques</li>
  <li>Verification formelle (model checking)</li>
  <li>Generation automatique de tests</li>
  <li>Optimisation multi-objectifs (surface/vitesse/consommation)</li>
</ul>

<p><strong>Tendances</strong>:</p>
<ul>
  <li>FSM hierarchiques (StateCharts)</li>
  <li>FSM concurrentes</li>
  <li>Langages de haut niveau (SystemVerilog, SystemC)</li>
  <li>Synthese de haut niveau (HLS)</li>
</ul>

<p><strong>Applications emergentes</strong>:</p>
<ul>
  <li>IoT: controleurs ultra-basse consommation</li>
  <li>IA embarquee: FSM pour gestion d'energie</li>
  <li>Automobile: ADAS, controle moteur</li>
  <li>5G: traitement protocoles temps reel</li>
</ul>

<h3>Recommandations</h3>

<ol>
  <li><strong>Toujours partir du diagramme d'etats</strong>: visualisation essentielle</li>
  <li><strong>Verifier tous les cas</strong>: etats non utilises, transitions manquantes</li>
  <li><strong>Prevoir etat par defaut</strong>: robustesse face aux erreurs</li>
  <li><strong>Documenter clairement</strong>: noms d'etats explicites</li>
  <li><strong>Simuler avant implementation</strong>: eviter erreurs couteuses</li>
  <li><strong>Respecter contraintes temporelles</strong>: setup/hold critiques</li>
</ol>

<p><strong>Pieges a eviter</strong>:</p>
<ul>
  <li>Boucles combinatoires (feedback sans bascule)</li>
  <li>Aleas (glitches) sur signaux critiques</li>
  <li>Reset incomplet (etats non couverts)</li>
  <li>Violations setup/hold time</li>
  <li>Clock gating sans precaution</li>
</ul>

<p>En conclusion, la logique sequentielle est au coeur de tout systeme numerique complexe. La maitrise des FSM et des techniques de conception synchrone est indispensable pour developper des controleurs fiables et performants, que ce soit en ASIC, FPGA ou microcontroleurs.</p>

</div>

<div class="lang-en">

<h1>Sequential Logic - S5</h1>

<p><strong>Year</strong>: 2022-2023 (Semester 5)<br/>
<strong>Credits</strong>: 3 ECTS<br/>
<strong>Type</strong>: Digital Electronics</p>

<hr/>

<h2>PART A: GENERAL OVERVIEW</h2>

<h3>Course Objectives</h3>

<p>The Sequential Logic course delves into the design of digital circuits whose state depends on the history of inputs. It covers finite state machines (FSM), synchronous and asynchronous design, as well as systematic methods for designing complex sequential systems. This course is fundamental for designing digital controllers, communication protocols, and embedded systems.</p>

<h3>Targeted Skills</h3>

<ul>
  <li>Master flip-flops and storage elements</li>
  <li>Design finite state machines (Moore and Mealy)</li>
  <li>Analyze and synthesize sequential circuits</li>
  <li>Manage timing constraints and synchronization</li>
  <li>Implement complex controllers</li>
  <li>Optimize state encoding</li>
</ul>

<h3>Organization</h3>

<ul>
  <li><strong>Contact hours</strong>: 32h (Lectures: 18h, Tutorials: 14h)</li>
  <li><strong>Assessment</strong>: Final exam (70%) + Tutorials (30%)</li>
  <li><strong>Semester</strong>: 5 (2022-2023)</li>
  <li><strong>Prerequisites</strong>: Combinational logic, Boolean algebra</li>
</ul>

<hr/>

<h2>PART B: EXPERIENCE, CONTEXT AND FUNCTION</h2>

<h3>Course Content</h3>

<h4>1. Storage Elements</h4>

<p><strong>Flip-Flops and Latches</strong>:</p>

<p>Sequential circuits use memory elements to store state.</p>

<p><strong>SR (Set-Reset) Latch</strong>:</p>
<pre><code>S R | Q  Q'
----|-------
0 0 | Q  Q'  (memory)
0 1 | 0  1   (reset)
1 0 | 1  0   (set)
1 1 | X  X   (forbidden)</code></pre>

<p><strong>D (Data) Flip-Flop</strong>:</p>

<p>The most commonly used in synchronous design.</p>
<ul>
  <li>On rising clock edge: Q = D</li>
  <li>Stores the value of D</li>
</ul>

<p><strong>Characteristic equation</strong>: Q(t+1) = D(t)</p>

<p><strong>JK Flip-Flop</strong>:</p>
<pre><code>J K | Q(t+1)
----|--------
0 0 | Q      (memory)
0 1 | 0      (reset)
1 0 | 1      (set)
1 1 | Q'     (toggle)</code></pre>

<p><strong>T (Toggle) Flip-Flop</strong>:</p>

<p>When T=1, the output toggles: Q(t+1) = Q'(t)</p>

<p><strong>Timing Constraints</strong>:</p>

<ul>
  <li><strong>Setup time</strong> (tsu): time before the clock edge during which D must be stable</li>
  <li><strong>Hold time</strong> (th): time after the edge during which D must remain stable</li>
  <li><strong>Propagation delay</strong> (tpd): delay between CLK edge and Q change</li>
</ul>

<h4>2. Finite State Machines (FSM)</h4>

<p><strong>Moore FSM</strong>:</p>

<p>Outputs depend only on the current state.</p>

<p>Structure:</p>
<ul>
  <li>States</li>
  <li>Transitions (depend on inputs)</li>
  <li>Outputs (function of state only)</li>
</ul>

<p><strong>Example: "101" Sequence Detector</strong></p>

<p>Moore state diagram:</p>
<pre><code>S0 (init, out=0) --[1]--&gt; S1 (out=0)
S1 --[0]--&gt; S2 (out=0)
S2 --[1]--&gt; S3 (out=1)  // Sequence detected!
S3 --[x]--&gt; ...</code></pre>

<p><strong>Mealy FSM</strong>:</p>

<p>Outputs depend on the state AND the inputs.</p>

<p>Advantage: often fewer states than Moore.</p>

<p><strong>Comparison</strong>:</p>
<ul>
  <li>Moore: stable outputs (change only on clock edge)</li>
  <li>Mealy: faster reaction (outputs change with inputs)</li>
</ul>

<h4>3. Design Methodology</h4>

<p><strong>FSM Design Steps</strong>:</p>

<ol>
  <li><strong>Specification</strong>: define the desired behavior</li>
  <li><strong>State diagram</strong>: graphical representation</li>
  <li><strong>State table</strong>: tabular form</li>
  <li><strong>Minimization</strong>: reduce the number of states</li>
  <li><strong>State encoding</strong>: assign binary codes</li>
  <li><strong>Logic equations</strong>: derive next-state and output logic</li>
  <li><strong>Implementation</strong>: flip-flops + logic gates</li>
</ol>

<p><strong>Example: Traffic Light Controller</strong></p>

<p>States:</p>
<ul>
  <li>GREEN (30s)</li>
  <li>YELLOW (5s)</li>
  <li>RED (35s)</li>
</ul>

<p>Inputs: timer, vehicle sensor<br/>
Outputs: LED_G, LED_Y, LED_R</p>

<p><strong>Simplified state table</strong>:</p>
<pre><code>Current State | Timer | Next State   | Outputs
--------------|-------|--------------|----------
GREEN         | 0     | GREEN        | G=1,Y=0,R=0
GREEN         | 1     | YELLOW       | G=1,Y=0,R=0
YELLOW        | 0     | YELLOW       | G=0,Y=1,R=0
YELLOW        | 1     | RED          | G=0,Y=1,R=0
RED           | 0     | RED          | G=0,Y=0,R=1
RED           | 1     | GREEN        | G=0,Y=0,R=1</code></pre>

<h4>4. State Encoding</h4>

<p><strong>Natural binary</strong>:</p>
<ul>
  <li>n bits for 2^n states</li>
  <li>Example 4 states: 00, 01, 10, 11</li>
  <li>Saves flip-flops</li>
</ul>

<p><strong>One-Hot</strong>:</p>
<ul>
  <li>1 flip-flop per state</li>
  <li>Example 4 states: 0001, 0010, 0100, 1000</li>
  <li>Simplified decoding logic</li>
  <li>Used in FPGAs</li>
</ul>

<p><strong>Gray</strong>:</p>
<ul>
  <li>Only 1 bit changes between adjacent states</li>
  <li>Reduces hazards (glitches)</li>
  <li>Useful in asynchronous design</li>
</ul>

<p><strong>Example with 4 states</strong>:</p>
<pre><code>State | Binary | One-Hot | Gray
------|--------|---------|------
S0    | 00     | 0001    | 00
S1    | 01     | 0010    | 01
S2    | 10     | 0100    | 11
S3    | 11     | 1000    | 10</code></pre>

<h4>5. Synchronous Design</h4>

<p><strong>Synchronous design rules</strong>:</p>

<ul>
  <li>All flip-flops share the same clock</li>
  <li>No combinational logic in the clock path</li>
  <li>Respect setup/hold constraints</li>
</ul>

<p><strong>Maximum frequency</strong>:</p>

<p>fmax = 1 / (tpd_logic + tsu + tskew)</p>

<p>where:</p>
<ul>
  <li>tpd_logic: combinational delay between flip-flops</li>
  <li>tsu: setup time</li>
  <li>tskew: clock skew</li>
</ul>

<p><strong>Reset strategies</strong>:</p>

<p><strong>Asynchronous reset</strong>:</p>
<pre><code>if (reset = '1') then
    state &lt;= S0;
elsif rising_edge(clk) then
    state &lt;= next_state;
end if;</code></pre>

<p>Advantage: immediate reset<br/>
Disadvantage: may cause metastability</p>

<p><strong>Synchronous reset</strong>:</p>
<pre><code>if rising_edge(clk) then
    if (reset = '1') then
        state &lt;= S0;
    else
        state &lt;= next_state;
    end if;
end if;</code></pre>

<p>Advantage: synchronized with clock<br/>
Disadvantage: one-cycle delay</p>

<h4>6. Advanced Counters</h4>

<p><strong>Modulo-N counter</strong>:</p>

<p>Counts from 0 to N-1 then wraps back to 0.</p>

<p><strong>BCD decimal counter</strong>:<br/>
Counts from 0 to 9 (0000 to 1001).</p>

<p><strong>Up/down counter</strong>:</p>

<p>DIR input: 1=up, 0=down</p>

<p><strong>3-bit up/down example</strong>:</p>
<pre><code>UP:   000 -&gt; 001 -&gt; 010 -&gt; 011 -&gt; 100 -&gt; 101 -&gt; 110 -&gt; 111 -&gt; 000
DOWN: 111 -&gt; 110 -&gt; 101 -&gt; 100 -&gt; 011 -&gt; 010 -&gt; 001 -&gt; 000 -&gt; 111</code></pre>

<p><strong>Counter with preload</strong>:</p>

<p>LOAD input: loads initial value<br/>
Use case: precise frequency division</p>

<h4>7. Timing Aspects</h4>

<p><strong>Metastability</strong>:</p>

<p>Phenomenon occurring when setup/hold time is violated.<br/>
The flip-flop may remain in an indeterminate state.</p>

<p><strong>Solution</strong>: 2-stage synchronizer</p>
<pre><code>Asynchronous input -&gt; [FF1] -&gt; [FF2] -&gt; Synchronous output
                        CLK      CLK</code></pre>

<p>Reduces the probability of metastability to ~10^-12.</p>

<p><strong>Critical path analysis</strong>:</p>

<p>Identify the longest logic path between two flip-flops.</p>

<p>Example:</p>
<pre><code>FF1 --[tpd=2ns]--&gt; NAND --[tpd=3ns]--&gt; XOR --[tpd=4ns]--&gt; FF2
                                                          [tsu=1ns]</code></pre>

<p>Total delay: 2 + 3 + 4 + 1 = 10ns<br/>
Max frequency: 1/10ns = 100MHz</p>

<p><strong>Course materials</strong>:<br/>
<a href="/cours-pdf/S5/Logique-Séquentielle/Poly2022.pdf">Sequential Logic Course Notes</a></p>

<hr/>

<h2>PART C: TECHNICAL ASPECTS</h2>

<h3>Tutorial Exercises</h3>

<p><strong>TD1: FSM Design</strong></p>

<p>Exercise: Design a "1011" sequence detector (non-overlapping).</p>

<p><strong>Solution</strong>:</p>

<p>Required states:</p>
<ul>
  <li>S0: initial state</li>
  <li>S1: after "1"</li>
  <li>S2: after "10"</li>
  <li>S3: after "101"</li>
  <li>S4: complete sequence detected</li>
</ul>

<p>Transition table:</p>
<pre><code>State | Input 0  | Input 1  | Output
------|----------|----------|--------
S0    | S0       | S1       | 0
S1    | S2       | S1       | 0
S2    | S0       | S3       | 0
S3    | S0       | S4       | 0
S4    | S0       | S1       | 1</code></pre>

<p><strong>TD2: Encoding and equations</strong></p>

<p>For 4 states encoded in binary:</p>
<ul>
  <li>Q1 Q0 = 00 (S0), 01 (S1), 10 (S2), 11 (S3)</li>
</ul>

<p>Derive next-state equations using Karnaugh maps.</p>

<p><strong>TD3: Timing analysis</strong></p>

<p>Calculate the maximum frequency of a circuit with:</p>
<ul>
  <li>tpd_FF = 5ns</li>
  <li>tpd_comb = 15ns</li>
  <li>tsu = 3ns</li>
  <li>tskew = 1ns</li>
</ul>

<p>Solution:<br/>
Minimum period = 5 + 15 + 3 + 1 = 24ns<br/>
fmax = 1/24ns = 41.67MHz</p>

<h3>Practical Applications</h3>

<p><strong>UART Controller (transmitter)</strong>:</p>

<p>States:</p>
<ul>
  <li>IDLE: waiting for data</li>
  <li>START: sending start bit</li>
  <li>DATA0-DATA7: sending 8 data bits</li>
  <li>STOP: stop bit</li>
  <li>Return to IDLE</li>
</ul>

<p><strong>I2C Protocol Decoder</strong>:</p>

<p>FSM detecting:</p>
<ul>
  <li>START condition (SDA falls while SCL=1)</li>
  <li>Address (7 bits)</li>
  <li>R/W bit</li>
  <li>ACK/NACK</li>
  <li>Data</li>
  <li>STOP condition (SDA rises while SCL=1)</li>
</ul>

<p><strong>Vending Machine Controller</strong>:</p>

<p>Inputs: inserted coins (5c, 10c, 25c)<br/>
Output: product delivered when amount reached</p>

<p>States represent the accumulated credit.</p>

<h3>Design Tools</h3>

<p><strong>Simulators</strong>:</p>
<ul>
  <li>Logisim: graphical simulation</li>
  <li>ModelSim: VHDL/Verilog simulation</li>
  <li>Quartus: complete Altera/Intel suite</li>
</ul>

<p><strong>Description languages</strong>:</p>

<p><strong>VHDL example (Moore FSM)</strong>:</p>
<pre><code>process(clk, reset)
begin
    if reset = '1' then
        state &lt;= S0;
    elsif rising_edge(clk) then
        case state is
            when S0 =&gt;
                if input = '1' then
                    state &lt;= S1;
                end if;
            when S1 =&gt;
                -- transitions...
        end case;
    end if;
end process;

-- Moore output logic
output &lt;= '1' when state = S3 else '0';</code></pre>

<p><strong>Verilog example (Mealy FSM)</strong>:</p>
<pre><code>always @(posedge clk or posedge reset) begin
    if (reset)
        state &lt;= S0;
    else
        state &lt;= next_state;
end

// Next_state and output logic (combinational)
always @(*) begin
    case (state)
        S0: begin
            if (input)
                next_state = S1;
            output = 1'b0;
        end
        // ...
    endcase
end</code></pre>

<hr/>

<h2>PART D: ANALYSIS AND REFLECTION</h2>

<h3>Acquired Skills</h3>

<p><strong>Technical</strong>:</p>
<ul>
  <li>Systematic FSM design</li>
  <li>State encoding optimization</li>
  <li>Timing analysis of sequential circuits</li>
  <li>Synchronization management</li>
  <li>Implementation in VHDL/Verilog</li>
</ul>

<p><strong>Methodological</strong>:</p>
<ul>
  <li>Rigorous design approach</li>
  <li>FSM testing and verification</li>
  <li>Documentation (state diagrams)</li>
  <li>Sequential circuit debugging</li>
</ul>

<h3>Professional Applications</h3>

<p>Sequential logic is used in:</p>
<ul>
  <li><strong>Communication protocols</strong>: UART, SPI, I2C, USB</li>
  <li><strong>Controllers</strong>: machines, robots, industrial processes</li>
  <li><strong>Interfaces</strong>: LCD, keyboard, mouse, touchscreen</li>
  <li><strong>Processors</strong>: control unit, pipelines</li>
  <li><strong>Storage</strong>: memory controllers, cache</li>
  <li><strong>Networks</strong>: routers, switches, protocols</li>
</ul>

<h3>Connections with Other Courses</h3>

<ul>
  <li><strong>Digital Electronics Fundamentals</strong> (S5): foundation (flip-flops, counters)</li>
  <li><strong>Digital Architectures VHDL</strong> (S7): FPGA implementation</li>
  <li><strong>Microcontrollers</strong> (S6): FSM in firmware</li>
  <li><strong>Real-Time Systems</strong> (S8): scheduling and synchronization</li>
  <li><strong>Networks</strong> (S6): layered FSM protocols</li>
</ul>

<h3>Evolution and Outlook</h3>

<p><strong>Modern tools</strong>:</p>
<ul>
  <li>Automatic synthesis from graphical FSMs</li>
  <li>Formal verification (model checking)</li>
  <li>Automatic test generation</li>
  <li>Multi-objective optimization (area/speed/power)</li>
</ul>

<p><strong>Trends</strong>:</p>
<ul>
  <li>Hierarchical FSMs (StateCharts)</li>
  <li>Concurrent FSMs</li>
  <li>High-level languages (SystemVerilog, SystemC)</li>
  <li>High-level synthesis (HLS)</li>
</ul>

<p><strong>Emerging applications</strong>:</p>
<ul>
  <li>IoT: ultra-low-power controllers</li>
  <li>Embedded AI: FSM for power management</li>
  <li>Automotive: ADAS, engine control</li>
  <li>5G: real-time protocol processing</li>
</ul>

<h3>Recommendations</h3>

<ol>
  <li><strong>Always start from the state diagram</strong>: visualization is essential</li>
  <li><strong>Check all cases</strong>: unused states, missing transitions</li>
  <li><strong>Plan a default state</strong>: robustness against errors</li>
  <li><strong>Document clearly</strong>: use explicit state names</li>
  <li><strong>Simulate before implementation</strong>: avoid costly mistakes</li>
  <li><strong>Respect timing constraints</strong>: setup/hold are critical</li>
</ol>

<p><strong>Pitfalls to avoid</strong>:</p>
<ul>
  <li>Combinational loops (feedback without flip-flop)</li>
  <li>Hazards (glitches) on critical signals</li>
  <li>Incomplete reset (uncovered states)</li>
  <li>Setup/hold time violations</li>
  <li>Clock gating without caution</li>
</ul>

<p>In conclusion, sequential logic is at the heart of every complex digital system. Mastering FSMs and synchronous design techniques is essential for developing reliable and high-performance controllers, whether in ASIC, FPGA, or microcontrollers.</p>

</div>

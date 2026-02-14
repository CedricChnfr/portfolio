---
layout: default
title: "Électronique Numérique et Conception (ENC) - S3"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

<style>
.back-nav { margin-bottom: 20px; }
.back-nav a { text-decoration: none; color: #2a7ae2; font-weight: 600; }
.back-nav a:hover { text-decoration: underline; }
.section-title { color: #2a7ae2; border-bottom: 2px solid #2a7ae2; padding-bottom: 10px; margin-top: 30px; margin-bottom: 20px; }
</style>

<div class="back-nav">
  <a href="./my-courses-2021-2022.html" data-i18n-html="back-courses-2021-2022">&larr; Retour a Mes Cours 2021-2022</a>
</div>

<div class="lang-fr">

<h1>Électronique Numérique et Conception (ENC) - Semestre 3</h1>

<p><strong>Annee</strong>: 2021-2022 | <strong>Semestre</strong>: 3 | <strong>Type</strong>: Technique</p>

<hr>

<h2>PART A - Présentation Générale du Cours</h2>

<h3>Contexte et objectifs</h3>

<p>L'ENC (Électronique Numérique et Conception) au S3 ENOC approfondit la conception de systèmes numériques programmables (FPGA/CPLD) en VHDL. Deux projets majeurs : développement de bibliothèque de composants IP et conception complète d'une platine électronique intégrant un FPGA.</p>

<p><strong>Objectifs :</strong></p>
<ul>
<li>Programmation VHDL avancée (FSM, pipeline, mémoires)</li>
<li>Synthèse et implémentation sur FPGA (Quartus, Vivado)</li>
<li>Conception de platines numériques professionnelles</li>
<li>Validation par simulation (ModelSim) et tests matériels</li>
</ul>

<h3>Prérequis</h3>
<ul>
<li>VHDL de base (S1 SIN)</li>
<li>Logique séquentielle</li>
<li>Conception PCB</li>
</ul>

<hr>

<h2>PART B: EXPÉRIENCE, CONTEXTE ET FONCTION</h2>

<h3>Module 1 : VHDL avancé</h3>

<p><strong>Structures algorithmiques :</strong></p>
<ul>
<li>Processus synchrones (rising_edge)</li>
<li>FSM : Moore (sorties = f(état)), Mealy (sorties = f(état, entrées))</li>
<li>Boucles FOR/WHILE</li>
<li>Architectures structurelles (component instantiation)</li>
</ul>

<p><strong>Blocs réutilisables :</strong></p>
<ul>
<li>Compteurs (up/down, modulo N, avec load/enable)</li>
<li>Registres à décalage (SIPO, PISO, barrel shifter)</li>
<li>Diviseurs de fréquence</li>
<li>PWM à résolution variable</li>
<li>FIFO, RAM/ROM</li>
</ul>

<p><strong>Interfaces de communication :</strong></p>
<ul>
<li>UART (Tx/Rx, baud rate configurable)</li>
<li>SPI (master/slave, modes 0-3)</li>
<li>I2C (master, arbitrage)</li>
<li>VGA (timing 640×480, palette couleurs)</li>
</ul>

<h3>Module 2 : FPGA/CPLD</h3>

<p><strong>Architecture FPGA (ex: Cyclone IV, Spartan-6) :</strong></p>
<ul>
<li>Logic Elements (LUT + FF)</li>
<li>Block RAM, DSP blocks</li>
<li>PLL (génération horloges)</li>
<li>I/O programmables (standards : LVTTL, LVCMOS, LVDS)</li>
</ul>

<p><strong>CPLD vs FPGA :</strong></p>
<ul>
<li>CPLD : non-volatile, démarrage rapide, capacité limitée</li>
<li>FPGA : volatile (Flash SPI config), haute densité, flexible</li>
</ul>

<p><strong>Outils de conception :</strong></p>
<ul>
<li>Quartus Prime (Intel/Altera)</li>
<li>Vivado (Xilinx)</li>
<li>Synthèse → Placement &amp; Routage → Bitstream</li>
<li>Contraintes timing (SDC) et pin assignment</li>
</ul>

<h3>Module 3 : Simulation et validation</h3>

<p><strong>Testbench VHDL :</strong></p>

<pre><code class="language-vhdl">entity tb_uart is end;
architecture behavior of tb_uart is
  signal clk, rst, tx_start : std_logic;
  signal tx_data : std_logic_vector(7 downto 0);
begin
  uut: entity work.uart_tx port map(...);

  clk_process: process
  begin
    clk &lt;= '0'; wait for 10 ns;
    clk &lt;= '1'; wait for 10 ns;
  end process;

  stimulus: process
  begin
    rst &lt;= '1'; wait for 100 ns;
    rst &lt;= '0';
    tx_data &lt;= X"A5";
    tx_start &lt;= '1'; wait for 20 ns;
    tx_start &lt;= '0';
    wait;
  end process;
end;</code></pre>

<p><strong>Simulation :</strong></p>
<ul>
<li>ModelSim : waveform, assertions</li>
<li>Simulation fonctionnelle (pré-synthèse)</li>
<li>Simulation temporelle (post-routage, délais réels)</li>
</ul>

<hr>

<h2>PART C: ASPECTS TECHNIQUES</h2>

<h3>Projet Composants VHDL</h3>

<p><strong>Bibliothèque IP à développer :</strong></p>
<ol>
<li>UART configurable (baud rate générique)</li>
<li>SPI master/slave</li>
<li>I2C master</li>
<li>Contrôleur VGA (synchronisation H/V, pixel pipeline)</li>
<li>Contrôleur LCD HD44780</li>
<li>Interface PS/2 clavier</li>
</ol>

<p><strong>Livrables :</strong></p>
<ul>
<li>Code VHDL commenté</li>
<li>Testbench complet</li>
<li>Rapport simulation (chronogrammes)</li>
<li>Documentation d'utilisation</li>
</ul>

<h3>Projet Platine FPGA</h3>

<p><strong>Architecture système :</strong></p>
<ul>
<li>FPGA Cyclone IV EP4CE15 ou Spartan-6 LX9</li>
<li>Configuration : Flash SPI + JTAG</li>
<li>Alimentation : 3.3V I/O, 1.2V core (régulateurs LDO)</li>
<li>Périphériques : LEDs, switches, UART-USB (FT232), extension GPIO</li>
</ul>

<p><strong>Schéma électrique (KiCad/Altium) :</strong></p>
<ul>
<li>FPGA + découplage intensif (100nF proches + 10µF)</li>
<li>Oscillateur 50 MHz (GCLK)</li>
<li>Configuration : EPCS4 (Flash SPI 4 Mbit)</li>
<li>Connecteur JTAG 10 pins</li>
<li>USB-UART (FT232RL ou CH340)</li>
<li>Connecteurs extension (compatible Arduino/Pmod)</li>
</ul>

<p><strong>PCB 4 couches :</strong></p>
<ul>
<li>L1 : Signaux Top</li>
<li>L2 : GND plane</li>
<li>L3 : 3.3V / 1.2V power planes</li>
<li>L4 : Signaux Bottom</li>
<li>Via stitching GND (espacement &lt;λ/10 à fmax)</li>
<li>Routage différentiel si LVDS</li>
</ul>

<p><strong>Programmation et test :</strong></p>
<ul>
<li>Chargement bitstream JTAG</li>
<li>Configuration Flash (boot automatique)</li>
<li>Tests unitaires (LEDs, UART loopback)</li>
<li>Application finale (ex: oscilloscope logique USB)</li>
</ul>

<hr>

<h2>PART D: ANALYSE ET RÉFLEXION</h2>

<h3>Évaluation</h3>
<ul>
<li>Projet composants VHDL (35%) : code, simulations, documentation</li>
<li>Projet platine FPGA (40%) : schéma, PCB, programmation, démo</li>
<li>Contrôles (15%)</li>
<li>Rapport technique (10%)</li>
</ul>

<h3>Compétences développées</h3>
<ul>
<li>VHDL avancé et réutilisable</li>
<li>Synthèse FPGA (timing, ressources)</li>
<li>Conception platines numériques professionnelles</li>
<li>Validation simulation + matérielle</li>
<li>Gestion projets électroniques complexes</li>
</ul>

<h3>Débouchés</h3>
<ul>
<li>Ingénieur FPGA (traitement signal, vision, crypto)</li>
<li>Concepteur systèmes embarqués numériques</li>
<li>Architecte hardware (ASIC, prototypage FPGA)</li>
</ul>

<h2>Contenu du cours</h2>

<h3>VHDL avancé</h3>

<h4>Structures de base</h4>
<ul>
<li>Entity et Architecture</li>
<li>Signaux, variables, constantes</li>
<li>Types de données (std_logic, integer, etc.)</li>
<li>Opérateurs logiques et arithmétiques</li>
<li>Assignations concurrentes et séquentielles</li>
</ul>

<h4>Structures algorithmiques</h4>
<p><strong>Processus (process) :</strong></p>
<ul>
<li>Sensibility list</li>
<li>Exécution séquentielle</li>
<li>Variables locales</li>
<li>Wait statements</li>
</ul>

<p><strong>Conditions :</strong></p>
<ul>
<li>IF-THEN-ELSE</li>
<li>CASE-WHEN</li>
<li>WITH-SELECT-WHEN</li>
</ul>

<p><strong>Boucles :</strong></p>
<ul>
<li>FOR loops</li>
<li>WHILE loops</li>
<li>LOOP-EXIT</li>
</ul>

<h4>Conception structurelle</h4>
<ul>
<li>Component declaration</li>
<li>Component instantiation</li>
<li>Port mapping</li>
<li>Generic parameters</li>
<li>Configuration</li>
</ul>

<h4>Machines à états (FSM)</h4>
<p><strong>Moore :</strong></p>
<ul>
<li>Sorties dépendent de l'état</li>
<li>2 ou 3 processus</li>
<li>Stabilité</li>
</ul>

<p><strong>Mealy :</strong></p>
<ul>
<li>Sorties dépendent état + entrées</li>
<li>Plus réactif</li>
<li>Peut être instable</li>
</ul>

<p><strong>Encodage :</strong></p>
<ul>
<li>Binary</li>
<li>One-hot</li>
<li>Gray code</li>
</ul>

<h3>Architectures numériques</h3>

<h4>Blocs de base</h4>

<p><strong>Compteurs :</strong></p>
<ul>
<li>Binaires, décimaux</li>
<li>Up, down, up/down</li>
<li>Modulo N</li>
<li>Avec enable, load, clear</li>
</ul>

<p><strong>Registres :</strong></p>
<ul>
<li>Registres simples</li>
<li>Registres à décalage (shift)</li>
<li>PISO, SIPO, PIPO</li>
<li>Barrel shifter</li>
</ul>

<p><strong>Diviseurs de fréquence :</strong></p>
<ul>
<li>Division entière</li>
<li>Division fractionnaire</li>
<li>Génération d'horloges</li>
</ul>

<p><strong>Générateurs PWM :</strong></p>
<ul>
<li>Résolution variable</li>
<li>Fréquence ajustable</li>
<li>Rapport cyclique contrôlable</li>
</ul>

<h4>Blocs arithmétiques</h4>

<p><strong>Additionneurs :</strong></p>
<ul>
<li>Half-adder, full-adder</li>
<li>Ripple-carry</li>
<li>Carry look-ahead</li>
<li>Signé/non signé</li>
</ul>

<p><strong>Multiplieurs :</strong></p>
<ul>
<li>Shift-and-add</li>
<li>Booth algorithm</li>
<li>Pipeline</li>
<li>DSP blocks</li>
</ul>

<p><strong>ALU (Arithmetic Logic Unit) :</strong></p>
<ul>
<li>Opérations arithmétiques</li>
<li>Opérations logiques</li>
<li>Shifter</li>
<li>Flags (Z, N, C, V)</li>
</ul>

<h4>Mémoires</h4>

<p><strong>RAM :</strong></p>
<ul>
<li>Single-port, dual-port</li>
<li>Block RAM (BRAM)</li>
<li>Distributed RAM</li>
<li>FIFO</li>
</ul>

<p><strong>ROM :</strong></p>
<ul>
<li>Initialization</li>
<li>Look-up tables (LUT)</li>
<li>Constantes</li>
</ul>

<h3>FPGA et CPLD</h3>

<h4>Architecture FPGA</h4>
<ul>
<li>Logic Elements (LE) / Slices</li>
<li>Look-Up Tables (LUT)</li>
<li>Flip-flops</li>
<li>Block RAM</li>
<li>DSP blocks</li>
<li>I/O blocks</li>
<li>Clock management (PLL, DLL)</li>
</ul>

<h4>Familles de FPGA</h4>
<p><strong>Xilinx :</strong></p>
<ul>
<li>Spartan (low-cost)</li>
<li>Artix, Kintex, Virtex</li>
<li>Zynq (ARM + FPGA)</li>
</ul>

<p><strong>Intel/Altera :</strong></p>
<ul>
<li>Cyclone (entry-level)</li>
<li>MAX 10 (CPLD-like)</li>
<li>Arria, Stratix</li>
</ul>

<h4>CPLD vs FPGA</h4>
<p><strong>CPLD :</strong></p>
<ul>
<li>Non-volatile</li>
<li>Démarrage rapide</li>
<li>Architecture simple</li>
<li>Capacité limitée</li>
</ul>

<p><strong>FPGA :</strong></p>
<ul>
<li>Volatile (configuration externe)</li>
<li>Haute capacité</li>
<li>Flexible</li>
<li>DSP et mémoire intégrés</li>
</ul>

<h3>Outils de conception</h3>

<h4>Synthèse</h4>
<ul>
<li>Analyse syntaxique</li>
<li>Optimisation</li>
<li>Technology mapping</li>
<li>Génération netlist</li>
</ul>

<h4>Implémentation</h4>
<ul>
<li>Placement (Placer)</li>
<li>Routage (Router)</li>
<li>Contraintes de timing</li>
<li>Utilisation des ressources</li>
</ul>

<h4>Simulation</h4>
<p><strong>Fonctionnelle :</strong></p>
<ul>
<li>Comportement logique</li>
<li>Pas de timing</li>
<li>Rapide</li>
</ul>

<p><strong>Temporelle (post-route) :</strong></p>
<ul>
<li>Délais réels</li>
<li>Setup/hold times</li>
<li>Critical path</li>
<li>Précis</li>
</ul>

<h4>Contraintes</h4>

<p><strong>Timing :</strong></p>
<ul>
<li>Fréquences d'horloge</li>
<li>Contraintes I/O</li>
<li>Chemins critiques</li>
<li>False paths</li>
</ul>

<p><strong>Placement :</strong></p>
<ul>
<li>LOC (location constraints)</li>
<li>Groupes de signaux</li>
<li>Floorplanning</li>
</ul>

<p><strong>I/O :</strong></p>
<ul>
<li>Standards (LVTTL, LVCMOS, LVDS)</li>
<li>Drive strength</li>
<li>Slew rate</li>
<li>Pull-up/down</li>
</ul>

<h2>Projets pratiques</h2>

<h3>Projet Composants VHDL</h3>

<h4>Objectif</h4>
<p>Développement de bibliothèque de composants réutilisables</p>

<p><strong>Composants à réaliser :</strong></p>
<ul>
<li>UART (transmission série)</li>
<li>SPI master/slave</li>
<li>I2C master</li>
<li>Contrôleur VGA</li>
<li>Contrôleur LCD</li>
<li>Interface PS/2 (clavier)</li>
</ul>

<p><strong>Livrables :</strong></p>
<ul>
<li>Code VHDL commenté</li>
<li>Testbench</li>
<li>Rapport de simulation</li>
<li>Documentation technique</li>
</ul>

<h3>Projet Platine avec FPGA</h3>

<h4>Description</h4>
<p>Conception complète d'une carte avec FPGA/CPLD</p>

<p><strong>Spécifications typiques :</strong></p>
<ul>
<li>FPGA/CPLD (Cyclone, Spartan)</li>
<li>Configuration (JTAG, Active Serial)</li>
<li>Alimentation (3.3V, 1.2V core)</li>
<li>I/O (LEDs, boutons, switches)</li>
<li>Interfaces (UART, USB-UART)</li>
<li>Extension (connecteurs)</li>
</ul>

<p><strong>Étapes :</strong></p>
<ol>
<li>Choix du composant</li>
<li>Schématique complet</li>
<li>PCB multicouche (4 ou 6)</li>
<li>Fabrication</li>
<li>Assemblage et test</li>
<li>Programmation et validation</li>
</ol>

<h4>Considérations techniques</h4>

<p><strong>Alimentation :</strong></p>
<ul>
<li>Séquencement (VCCINT avant VCCIO)</li>
<li>Découplage intensif</li>
<li>Filtrage</li>
<li>Supervision (Power-On Reset)</li>
</ul>

<p><strong>Configuration :</strong></p>
<ul>
<li>JTAG obligatoire</li>
<li>Flash SPI (configuration boot)</li>
<li>Mémoire suffisante</li>
<li>Schéma de configuration</li>
</ul>

<p><strong>Signaux d'horloge :</strong></p>
<ul>
<li>Oscillateur adapté</li>
<li>Entrée GCLK</li>
<li>Qualité du signal</li>
<li>Distribution</li>
</ul>

<p><strong>I/O :</strong></p>
<ul>
<li>Protection ESD</li>
<li>Résistances séries</li>
<li>Impédance contrôlée si nécessaire</li>
<li>Banques d'I/O (voltage)</li>
</ul>

<h2>Outils utilisés</h2>

<h3>Environnements de développement</h3>
<ul>
<li><strong>Quartus Prime</strong> : Intel/Altera FPGA</li>
<li><strong>Vivado</strong> : Xilinx FPGA</li>
<li><strong>ISE</strong> : Xilinx (legacy)</li>
<li><strong>Libero SoC</strong> : Microsemi/Microchip</li>
</ul>

<h3>Simulation</h3>
<ul>
<li><strong>ModelSim</strong> : Standard industrie</li>
<li><strong>GHDL</strong> : Open source</li>
<li><strong>Vivado Simulator</strong> : Intégré Xilinx</li>
<li><strong>Questa</strong> : Mentor Graphics</li>
</ul>

<h3>Conception PCB</h3>
<ul>
<li><strong>Altium Designer</strong></li>
<li><strong>KiCad</strong></li>
<li><strong>Eagle</strong></li>
<li><strong>OrCAD</strong></li>
</ul>

<h2>Évaluation</h2>
<ul>
<li>Projet composants VHDL (35%)</li>
<li>Projet platine FPGA (40%)</li>
<li>Contrôles de connaissances (15%)</li>
<li>Rapport et documentation (10%)</li>
</ul>

<h2>Liens avec d'autres cours</h2>
<ul>
<li><strong>ER</strong> : Intégration FPGA dans système</li>
<li><strong>IE</strong> : Communication FPGA-MCU</li>
<li><strong>Automatisme</strong> : Logique séquentielle</li>
<li><strong>SE</strong> : Traitement numérique signal</li>
</ul>

<h2>Exemple d'architecture VHDL</h2>

<h3>Diviseur de fréquence</h3>

<pre><code class="language-vhdl">entity freq_divider is
    generic (
        DIV_FACTOR : integer := 1000
    );
    port (
        clk_in  : in  std_logic;
        reset   : in  std_logic;
        clk_out : out std_logic
    );
end freq_divider;

architecture rtl of freq_divider is
    signal counter : integer range 0 to DIV_FACTOR-1;
    signal clk_temp : std_logic;
begin
    process(clk_in, reset)
    begin
        if reset = '1' then
            counter &lt;= 0;
            clk_temp &lt;= '0';
        elsif rising_edge(clk_in) then
            if counter = DIV_FACTOR-1 then
                counter &lt;= 0;
                clk_temp &lt;= not clk_temp;
            else
                counter &lt;= counter + 1;
            end if;
        end if;
    end process;

    clk_out &lt;= clk_temp;
end rtl;</code></pre>

<h3>Machine à états (FSM)</h3>

<pre><code class="language-vhdl">type state_type is (IDLE, START, DATA, STOP);
signal state, next_state : state_type;

-- State register
process(clk, reset)
begin
    if reset = '1' then
        state &lt;= IDLE;
    elsif rising_edge(clk) then
        state &lt;= next_state;
    end if;
end process;

-- Next state logic
process(state, inputs)
begin
    case state is
        when IDLE =&gt;
            if start = '1' then
                next_state &lt;= START;
            else
                next_state &lt;= IDLE;
            end if;
        when START =&gt;
            next_state &lt;= DATA;
        when DATA =&gt;
            if done = '1' then
                next_state &lt;= STOP;
            else
                next_state &lt;= DATA;
            end if;
        when STOP =&gt;
            next_state &lt;= IDLE;
    end case;
end process;</code></pre>

<h2>Bonnes pratiques VHDL</h2>

<h3>Horloges et resets</h3>
<ul>
<li>Un seul edge (rising ou falling)</li>
<li>Reset asynchrone ou synchrone</li>
<li>Éviter gated clocks</li>
<li>Utiliser clock enables</li>
</ul>

<h3>Synthétisabilité</h3>
<ul>
<li>Éviter délais (wait for)</li>
<li>Initialiser registres dans reset</li>
<li>Attention aux latches</li>
<li>Processus combinatoires complets</li>
</ul>

<h3>Timing</h3>
<ul>
<li>Registrer les sorties</li>
<li>Pipeline pour haute fréquence</li>
<li>Éviter chemins combinatoires longs</li>
<li>Synchronisation signaux asynchrones</li>
</ul>

<h3>Organisation code</h3>
<ul>
<li>Un fichier par entity</li>
<li>Commentaires</li>
<li>Nommage cohérent</li>
<li>Packages pour constantes</li>
</ul>

<h2>Compétences développées</h2>
<ul>
<li>Programmation VHDL avancée</li>
<li>Conception sur FPGA/CPLD</li>
<li>Simulation et validation</li>
<li>Conception de platines numériques</li>
<li>Analyse de timing</li>
<li>Debugging sur FPGA</li>
</ul>

<h2>Ressources FPGA typiques</h2>

<h3>Exemple : Cyclone IV EP4CE15</h3>
<ul>
<li>15 408 Logic Elements</li>
<li>504 Kbits RAM</li>
<li>56 multiplieurs 18×18</li>
<li>343 I/O</li>
<li>4 PLLs</li>
<li>Configuration série ou parallèle</li>
</ul>

<h3>Exemple : Spartan-6 LX9</h3>
<ul>
<li>9 152 Logic Cells</li>
<li>576 Kbits Block RAM</li>
<li>32 DSP48A1 slices</li>
<li>200 I/O</li>
<li>4 CMTs (Clock Management Tiles)</li>
</ul>

<h2>Pièges courants</h2>

<h3>VHDL</h3>
<ul>
<li>Latches involontaires</li>
<li>Signaux vs variables</li>
<li>Delta-cycle delays</li>
<li>Synthèse vs simulation</li>
</ul>

<h3>FPGA</h3>
<ul>
<li>Timing violations</li>
<li>Metastability (CDC)</li>
<li>Resource exhaustion</li>
<li>Configuration fails</li>
</ul>

<h3>PCB</h3>
<ul>
<li>Alimentation insuffisante</li>
<li>Découplage inadéquat</li>
<li>EMI/CEM</li>
<li>Signaux d'horloge mal routés</li>
</ul>

</div>

<div class="lang-en">

<h1>Digital Electronics and Design (ENC) - Semester 3</h1>

<p><strong>Year</strong>: 2021-2022 | <strong>Semester</strong>: 3 | <strong>Type</strong>: Technical</p>

<hr>

<h2>PART A - General Course Overview</h2>

<h3>Context and objectives</h3>

<p>ENC (Digital Electronics and Design) in S3 ENOC deepens the design of programmable digital systems (FPGA/CPLD) in VHDL. Two major projects: development of an IP component library and complete design of an electronic board integrating an FPGA.</p>

<p><strong>Objectives:</strong></p>
<ul>
<li>Advanced VHDL programming (FSM, pipeline, memories)</li>
<li>Synthesis and implementation on FPGA (Quartus, Vivado)</li>
<li>Professional digital board design</li>
<li>Validation through simulation (ModelSim) and hardware testing</li>
</ul>

<h3>Prerequisites</h3>
<ul>
<li>Basic VHDL (S1 SIN)</li>
<li>Sequential logic</li>
<li>PCB design</li>
</ul>

<hr>

<h2>PART B: EXPERIENCE, CONTEXT AND FUNCTION</h2>

<h3>Module 1: Advanced VHDL</h3>

<p><strong>Algorithmic structures:</strong></p>
<ul>
<li>Synchronous processes (rising_edge)</li>
<li>FSM: Moore (outputs = f(state)), Mealy (outputs = f(state, inputs))</li>
<li>FOR/WHILE loops</li>
<li>Structural architectures (component instantiation)</li>
</ul>

<p><strong>Reusable blocks:</strong></p>
<ul>
<li>Counters (up/down, modulo N, with load/enable)</li>
<li>Shift registers (SIPO, PISO, barrel shifter)</li>
<li>Frequency dividers</li>
<li>Variable resolution PWM</li>
<li>FIFO, RAM/ROM</li>
</ul>

<p><strong>Communication interfaces:</strong></p>
<ul>
<li>UART (Tx/Rx, configurable baud rate)</li>
<li>SPI (master/slave, modes 0-3)</li>
<li>I2C (master, arbitration)</li>
<li>VGA (640x480 timing, color palette)</li>
</ul>

<h3>Module 2: FPGA/CPLD</h3>

<p><strong>FPGA Architecture (e.g.: Cyclone IV, Spartan-6):</strong></p>
<ul>
<li>Logic Elements (LUT + FF)</li>
<li>Block RAM, DSP blocks</li>
<li>PLL (clock generation)</li>
<li>Programmable I/O (standards: LVTTL, LVCMOS, LVDS)</li>
</ul>

<p><strong>CPLD vs FPGA:</strong></p>
<ul>
<li>CPLD: non-volatile, fast startup, limited capacity</li>
<li>FPGA: volatile (Flash SPI config), high density, flexible</li>
</ul>

<p><strong>Design tools:</strong></p>
<ul>
<li>Quartus Prime (Intel/Altera)</li>
<li>Vivado (Xilinx)</li>
<li>Synthesis &rarr; Place &amp; Route &rarr; Bitstream</li>
<li>Timing constraints (SDC) and pin assignment</li>
</ul>

<h3>Module 3: Simulation and validation</h3>

<p><strong>VHDL Testbench:</strong></p>

<pre><code class="language-vhdl">entity tb_uart is end;
architecture behavior of tb_uart is
  signal clk, rst, tx_start : std_logic;
  signal tx_data : std_logic_vector(7 downto 0);
begin
  uut: entity work.uart_tx port map(...);

  clk_process: process
  begin
    clk &lt;= '0'; wait for 10 ns;
    clk &lt;= '1'; wait for 10 ns;
  end process;

  stimulus: process
  begin
    rst &lt;= '1'; wait for 100 ns;
    rst &lt;= '0';
    tx_data &lt;= X"A5";
    tx_start &lt;= '1'; wait for 20 ns;
    tx_start &lt;= '0';
    wait;
  end process;
end;</code></pre>

<p><strong>Simulation:</strong></p>
<ul>
<li>ModelSim: waveform, assertions</li>
<li>Functional simulation (pre-synthesis)</li>
<li>Timing simulation (post-route, real delays)</li>
</ul>

<hr>

<h2>PART C: TECHNICAL ASPECTS</h2>

<h3>VHDL Components Project</h3>

<p><strong>IP library to develop:</strong></p>
<ol>
<li>Configurable UART (generic baud rate)</li>
<li>SPI master/slave</li>
<li>I2C master</li>
<li>VGA controller (H/V synchronization, pixel pipeline)</li>
<li>LCD HD44780 controller</li>
<li>PS/2 keyboard interface</li>
</ol>

<p><strong>Deliverables:</strong></p>
<ul>
<li>Commented VHDL code</li>
<li>Complete testbench</li>
<li>Simulation report (timing diagrams)</li>
<li>Usage documentation</li>
</ul>

<h3>FPGA Board Project</h3>

<p><strong>System architecture:</strong></p>
<ul>
<li>FPGA Cyclone IV EP4CE15 or Spartan-6 LX9</li>
<li>Configuration: Flash SPI + JTAG</li>
<li>Power supply: 3.3V I/O, 1.2V core (LDO regulators)</li>
<li>Peripherals: LEDs, switches, UART-USB (FT232), GPIO extension</li>
</ul>

<p><strong>Electrical schematic (KiCad/Altium):</strong></p>
<ul>
<li>FPGA + intensive decoupling (100nF close + 10uF)</li>
<li>50 MHz oscillator (GCLK)</li>
<li>Configuration: EPCS4 (Flash SPI 4 Mbit)</li>
<li>JTAG 10-pin connector</li>
<li>USB-UART (FT232RL or CH340)</li>
<li>Extension connectors (Arduino/Pmod compatible)</li>
</ul>

<p><strong>4-layer PCB:</strong></p>
<ul>
<li>L1: Top signals</li>
<li>L2: GND plane</li>
<li>L3: 3.3V / 1.2V power planes</li>
<li>L4: Bottom signals</li>
<li>GND via stitching (spacing &lt;lambda/10 at fmax)</li>
<li>Differential routing if LVDS</li>
</ul>

<p><strong>Programming and testing:</strong></p>
<ul>
<li>JTAG bitstream loading</li>
<li>Flash configuration (automatic boot)</li>
<li>Unit tests (LEDs, UART loopback)</li>
<li>Final application (e.g.: USB logic oscilloscope)</li>
</ul>

<hr>

<h2>PART D: ANALYSIS AND REFLECTION</h2>

<h3>Assessment</h3>
<ul>
<li>VHDL components project (35%): code, simulations, documentation</li>
<li>FPGA board project (40%): schematic, PCB, programming, demo</li>
<li>Tests (15%)</li>
<li>Technical report (10%)</li>
</ul>

<h3>Skills developed</h3>
<ul>
<li>Advanced and reusable VHDL</li>
<li>FPGA synthesis (timing, resources)</li>
<li>Professional digital board design</li>
<li>Simulation + hardware validation</li>
<li>Complex electronic project management</li>
</ul>

<h3>Career opportunities</h3>
<ul>
<li>FPGA engineer (signal processing, vision, cryptography)</li>
<li>Digital embedded systems designer</li>
<li>Hardware architect (ASIC, FPGA prototyping)</li>
</ul>

<h2>Course content</h2>

<h3>Advanced VHDL</h3>

<h4>Basic structures</h4>
<ul>
<li>Entity and Architecture</li>
<li>Signals, variables, constants</li>
<li>Data types (std_logic, integer, etc.)</li>
<li>Logical and arithmetic operators</li>
<li>Concurrent and sequential assignments</li>
</ul>

<h4>Algorithmic structures</h4>
<p><strong>Process:</strong></p>
<ul>
<li>Sensitivity list</li>
<li>Sequential execution</li>
<li>Local variables</li>
<li>Wait statements</li>
</ul>

<p><strong>Conditions:</strong></p>
<ul>
<li>IF-THEN-ELSE</li>
<li>CASE-WHEN</li>
<li>WITH-SELECT-WHEN</li>
</ul>

<p><strong>Loops:</strong></p>
<ul>
<li>FOR loops</li>
<li>WHILE loops</li>
<li>LOOP-EXIT</li>
</ul>

<h4>Structural design</h4>
<ul>
<li>Component declaration</li>
<li>Component instantiation</li>
<li>Port mapping</li>
<li>Generic parameters</li>
<li>Configuration</li>
</ul>

<h4>Finite State Machines (FSM)</h4>
<p><strong>Moore:</strong></p>
<ul>
<li>Outputs depend on state</li>
<li>2 or 3 processes</li>
<li>Stability</li>
</ul>

<p><strong>Mealy:</strong></p>
<ul>
<li>Outputs depend on state + inputs</li>
<li>More reactive</li>
<li>Can be unstable</li>
</ul>

<p><strong>Encoding:</strong></p>
<ul>
<li>Binary</li>
<li>One-hot</li>
<li>Gray code</li>
</ul>

<h3>Digital architectures</h3>

<h4>Basic blocks</h4>

<p><strong>Counters:</strong></p>
<ul>
<li>Binary, decimal</li>
<li>Up, down, up/down</li>
<li>Modulo N</li>
<li>With enable, load, clear</li>
</ul>

<p><strong>Registers:</strong></p>
<ul>
<li>Simple registers</li>
<li>Shift registers</li>
<li>PISO, SIPO, PIPO</li>
<li>Barrel shifter</li>
</ul>

<p><strong>Frequency dividers:</strong></p>
<ul>
<li>Integer division</li>
<li>Fractional division</li>
<li>Clock generation</li>
</ul>

<p><strong>PWM generators:</strong></p>
<ul>
<li>Variable resolution</li>
<li>Adjustable frequency</li>
<li>Controllable duty cycle</li>
</ul>

<h4>Arithmetic blocks</h4>

<p><strong>Adders:</strong></p>
<ul>
<li>Half-adder, full-adder</li>
<li>Ripple-carry</li>
<li>Carry look-ahead</li>
<li>Signed/unsigned</li>
</ul>

<p><strong>Multipliers:</strong></p>
<ul>
<li>Shift-and-add</li>
<li>Booth algorithm</li>
<li>Pipeline</li>
<li>DSP blocks</li>
</ul>

<p><strong>ALU (Arithmetic Logic Unit):</strong></p>
<ul>
<li>Arithmetic operations</li>
<li>Logic operations</li>
<li>Shifter</li>
<li>Flags (Z, N, C, V)</li>
</ul>

<h4>Memories</h4>

<p><strong>RAM:</strong></p>
<ul>
<li>Single-port, dual-port</li>
<li>Block RAM (BRAM)</li>
<li>Distributed RAM</li>
<li>FIFO</li>
</ul>

<p><strong>ROM:</strong></p>
<ul>
<li>Initialization</li>
<li>Look-up tables (LUT)</li>
<li>Constants</li>
</ul>

<h3>FPGA and CPLD</h3>

<h4>FPGA Architecture</h4>
<ul>
<li>Logic Elements (LE) / Slices</li>
<li>Look-Up Tables (LUT)</li>
<li>Flip-flops</li>
<li>Block RAM</li>
<li>DSP blocks</li>
<li>I/O blocks</li>
<li>Clock management (PLL, DLL)</li>
</ul>

<h4>FPGA families</h4>
<p><strong>Xilinx:</strong></p>
<ul>
<li>Spartan (low-cost)</li>
<li>Artix, Kintex, Virtex</li>
<li>Zynq (ARM + FPGA)</li>
</ul>

<p><strong>Intel/Altera:</strong></p>
<ul>
<li>Cyclone (entry-level)</li>
<li>MAX 10 (CPLD-like)</li>
<li>Arria, Stratix</li>
</ul>

<h4>CPLD vs FPGA</h4>
<p><strong>CPLD:</strong></p>
<ul>
<li>Non-volatile</li>
<li>Fast startup</li>
<li>Simple architecture</li>
<li>Limited capacity</li>
</ul>

<p><strong>FPGA:</strong></p>
<ul>
<li>Volatile (external configuration)</li>
<li>High capacity</li>
<li>Flexible</li>
<li>Integrated DSP and memory</li>
</ul>

<h3>Design tools</h3>

<h4>Synthesis</h4>
<ul>
<li>Syntax analysis</li>
<li>Optimization</li>
<li>Technology mapping</li>
<li>Netlist generation</li>
</ul>

<h4>Implementation</h4>
<ul>
<li>Placement (Placer)</li>
<li>Routing (Router)</li>
<li>Timing constraints</li>
<li>Resource utilization</li>
</ul>

<h4>Simulation</h4>
<p><strong>Functional:</strong></p>
<ul>
<li>Logical behavior</li>
<li>No timing</li>
<li>Fast</li>
</ul>

<p><strong>Timing (post-route):</strong></p>
<ul>
<li>Real delays</li>
<li>Setup/hold times</li>
<li>Critical path</li>
<li>Accurate</li>
</ul>

<h4>Constraints</h4>

<p><strong>Timing:</strong></p>
<ul>
<li>Clock frequencies</li>
<li>I/O constraints</li>
<li>Critical paths</li>
<li>False paths</li>
</ul>

<p><strong>Placement:</strong></p>
<ul>
<li>LOC (location constraints)</li>
<li>Signal groups</li>
<li>Floorplanning</li>
</ul>

<p><strong>I/O:</strong></p>
<ul>
<li>Standards (LVTTL, LVCMOS, LVDS)</li>
<li>Drive strength</li>
<li>Slew rate</li>
<li>Pull-up/down</li>
</ul>

<h2>Practical projects</h2>

<h3>VHDL Components Project</h3>

<h4>Objective</h4>
<p>Development of a reusable component library</p>

<p><strong>Components to build:</strong></p>
<ul>
<li>UART (serial transmission)</li>
<li>SPI master/slave</li>
<li>I2C master</li>
<li>VGA controller</li>
<li>LCD controller</li>
<li>PS/2 interface (keyboard)</li>
</ul>

<p><strong>Deliverables:</strong></p>
<ul>
<li>Commented VHDL code</li>
<li>Testbench</li>
<li>Simulation report</li>
<li>Technical documentation</li>
</ul>

<h3>FPGA Board Project</h3>

<h4>Description</h4>
<p>Complete design of a board with FPGA/CPLD</p>

<p><strong>Typical specifications:</strong></p>
<ul>
<li>FPGA/CPLD (Cyclone, Spartan)</li>
<li>Configuration (JTAG, Active Serial)</li>
<li>Power supply (3.3V, 1.2V core)</li>
<li>I/O (LEDs, buttons, switches)</li>
<li>Interfaces (UART, USB-UART)</li>
<li>Extension (connectors)</li>
</ul>

<p><strong>Steps:</strong></p>
<ol>
<li>Component selection</li>
<li>Complete schematic</li>
<li>Multi-layer PCB (4 or 6)</li>
<li>Manufacturing</li>
<li>Assembly and testing</li>
<li>Programming and validation</li>
</ol>

<h4>Technical considerations</h4>

<p><strong>Power supply:</strong></p>
<ul>
<li>Sequencing (VCCINT before VCCIO)</li>
<li>Intensive decoupling</li>
<li>Filtering</li>
<li>Supervision (Power-On Reset)</li>
</ul>

<p><strong>Configuration:</strong></p>
<ul>
<li>JTAG mandatory</li>
<li>Flash SPI (boot configuration)</li>
<li>Sufficient memory</li>
<li>Configuration scheme</li>
</ul>

<p><strong>Clock signals:</strong></p>
<ul>
<li>Suitable oscillator</li>
<li>GCLK input</li>
<li>Signal quality</li>
<li>Distribution</li>
</ul>

<p><strong>I/O:</strong></p>
<ul>
<li>ESD protection</li>
<li>Series resistors</li>
<li>Controlled impedance if necessary</li>
<li>I/O banks (voltage)</li>
</ul>

<h2>Tools used</h2>

<h3>Development environments</h3>
<ul>
<li><strong>Quartus Prime</strong>: Intel/Altera FPGA</li>
<li><strong>Vivado</strong>: Xilinx FPGA</li>
<li><strong>ISE</strong>: Xilinx (legacy)</li>
<li><strong>Libero SoC</strong>: Microsemi/Microchip</li>
</ul>

<h3>Simulation</h3>
<ul>
<li><strong>ModelSim</strong>: Industry standard</li>
<li><strong>GHDL</strong>: Open source</li>
<li><strong>Vivado Simulator</strong>: Xilinx integrated</li>
<li><strong>Questa</strong>: Mentor Graphics</li>
</ul>

<h3>PCB design</h3>
<ul>
<li><strong>Altium Designer</strong></li>
<li><strong>KiCad</strong></li>
<li><strong>Eagle</strong></li>
<li><strong>OrCAD</strong></li>
</ul>

<h2>Assessment</h2>
<ul>
<li>VHDL components project (35%)</li>
<li>FPGA board project (40%)</li>
<li>Knowledge tests (15%)</li>
<li>Report and documentation (10%)</li>
</ul>

<h2>Links with other courses</h2>
<ul>
<li><strong>ER</strong>: FPGA integration in system</li>
<li><strong>IE</strong>: FPGA-MCU communication</li>
<li><strong>Automation</strong>: Sequential logic</li>
<li><strong>SE</strong>: Digital signal processing</li>
</ul>

<h2>VHDL architecture example</h2>

<h3>Frequency divider</h3>

<pre><code class="language-vhdl">entity freq_divider is
    generic (
        DIV_FACTOR : integer := 1000
    );
    port (
        clk_in  : in  std_logic;
        reset   : in  std_logic;
        clk_out : out std_logic
    );
end freq_divider;

architecture rtl of freq_divider is
    signal counter : integer range 0 to DIV_FACTOR-1;
    signal clk_temp : std_logic;
begin
    process(clk_in, reset)
    begin
        if reset = '1' then
            counter &lt;= 0;
            clk_temp &lt;= '0';
        elsif rising_edge(clk_in) then
            if counter = DIV_FACTOR-1 then
                counter &lt;= 0;
                clk_temp &lt;= not clk_temp;
            else
                counter &lt;= counter + 1;
            end if;
        end if;
    end process;

    clk_out &lt;= clk_temp;
end rtl;</code></pre>

<h3>Finite State Machine (FSM)</h3>

<pre><code class="language-vhdl">type state_type is (IDLE, START, DATA, STOP);
signal state, next_state : state_type;

-- State register
process(clk, reset)
begin
    if reset = '1' then
        state &lt;= IDLE;
    elsif rising_edge(clk) then
        state &lt;= next_state;
    end if;
end process;

-- Next state logic
process(state, inputs)
begin
    case state is
        when IDLE =&gt;
            if start = '1' then
                next_state &lt;= START;
            else
                next_state &lt;= IDLE;
            end if;
        when START =&gt;
            next_state &lt;= DATA;
        when DATA =&gt;
            if done = '1' then
                next_state &lt;= STOP;
            else
                next_state &lt;= DATA;
            end if;
        when STOP =&gt;
            next_state &lt;= IDLE;
    end case;
end process;</code></pre>

<h2>VHDL best practices</h2>

<h3>Clocks and resets</h3>
<ul>
<li>Single edge (rising or falling)</li>
<li>Asynchronous or synchronous reset</li>
<li>Avoid gated clocks</li>
<li>Use clock enables</li>
</ul>

<h3>Synthesizability</h3>
<ul>
<li>Avoid delays (wait for)</li>
<li>Initialize registers in reset</li>
<li>Watch out for latches</li>
<li>Complete combinatorial processes</li>
</ul>

<h3>Timing</h3>
<ul>
<li>Register outputs</li>
<li>Pipeline for high frequency</li>
<li>Avoid long combinatorial paths</li>
<li>Synchronize asynchronous signals</li>
</ul>

<h3>Code organization</h3>
<ul>
<li>One file per entity</li>
<li>Comments</li>
<li>Consistent naming</li>
<li>Packages for constants</li>
</ul>

<h2>Skills developed</h2>
<ul>
<li>Advanced VHDL programming</li>
<li>FPGA/CPLD design</li>
<li>Simulation and validation</li>
<li>Digital board design</li>
<li>Timing analysis</li>
<li>FPGA debugging</li>
</ul>

<h2>Typical FPGA resources</h2>

<h3>Example: Cyclone IV EP4CE15</h3>
<ul>
<li>15,408 Logic Elements</li>
<li>504 Kbits RAM</li>
<li>56 multipliers 18x18</li>
<li>343 I/O</li>
<li>4 PLLs</li>
<li>Serial or parallel configuration</li>
</ul>

<h3>Example: Spartan-6 LX9</h3>
<ul>
<li>9,152 Logic Cells</li>
<li>576 Kbits Block RAM</li>
<li>32 DSP48A1 slices</li>
<li>200 I/O</li>
<li>4 CMTs (Clock Management Tiles)</li>
</ul>

<h2>Common pitfalls</h2>

<h3>VHDL</h3>
<ul>
<li>Unintentional latches</li>
<li>Signals vs variables</li>
<li>Delta-cycle delays</li>
<li>Synthesis vs simulation</li>
</ul>

<h3>FPGA</h3>
<ul>
<li>Timing violations</li>
<li>Metastability (CDC)</li>
<li>Resource exhaustion</li>
<li>Configuration failures</li>
</ul>

<h3>PCB</h3>
<ul>
<li>Insufficient power supply</li>
<li>Inadequate decoupling</li>
<li>EMI/EMC</li>
<li>Poorly routed clock signals</li>
</ul>

</div>

<style>body{font-family:Arial,sans-serif;background-color:#f4f4f9;color:#333;line-height:1.6}h2,h3,h4,h5{color:#2a7ae2}p{text-align:justify}code{background-color:#f5f5f5;padding:2px 6px;border-radius:3px;font-family:'Courier New',monospace}pre{background-color:#f5f5f5;padding:15px;border-radius:5px;overflow-x:auto}</style>

<div class="back-nav">
  <a href="./my-courses-2021-2022.html" data-i18n-html="back-courses-2021-2022">&larr; Retour a Mes Cours 2021-2022</a>
</div>

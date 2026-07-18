---
layout: default
title: "Architectures Numériques Avancées VHDL - S7"
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
</style>

<div class="back-nav">
    <a href="./my-courses-2023-2024.html" data-i18n-html="back-courses-2023-2024">&larr; Retour aux Cours 2023-2024</a>
</div>

<div class="lang-fr">

<h1>Architectures Numeriques Avancees VHDL - Semestre 7</h1>

<p><strong>Annee Universitaire</strong> : 2023-2024<br/>
<strong>Semestre</strong> : 7<br/>
<strong>Credits</strong> : 2.5 ECTS<br/>
<strong>Specialite</strong> : Conception Numerique et FPGA</p>

<hr/>

<h2>PART A - Presentation Generale du Module</h2>

<h3 class="section-title">Vue d'ensemble</h3>

<p>Ce cours enseigne la conception de systemes numeriques complexes avec le langage VHDL (VHSIC Hardware Description Language) et leur implementation sur FPGA. Il couvre la conception d'architectures numeriques avancees : unite arithmetique et logique (ALU), bancs de registres, memoires, et processeurs complets.</p>

<p><strong>Objectifs pedagogiques</strong> :</p>
<ul>
<li>Maitriser le langage VHDL pour la description materielle</li>
<li>Concevoir des circuits numeriques synthetisables</li>
<li>Implementer des systemes sur FPGA (Xilinx)</li>
<li>Simuler et verifier des designs avec testbenches</li>
<li>Comprendre les machines a etats finis (FSM)</li>
<li>Concevoir un processeur simple complet</li>
</ul>

<h3 class="section-title">Position dans le cursus</h3>

<p>Ce module s'appuie sur :</p>
<ul>
<li><strong>Fondements electronique numerique (S5)</strong> : portes logiques, bascules</li>
<li><strong>Logique sequentielle (S5)</strong> : machines a etats, compteurs</li>
<li><strong>Architecture Informatique materielle (S5)</strong> : structure processeur</li>
</ul>

<p>Il prepare a :</p>
<ul>
<li><strong>Systemes embarques</strong> : accelerateurs materiels</li>
<li><strong>Traitement du signal sur FPGA</strong> : implementation de filtres numeriques</li>
<li><strong>Conception ASIC</strong> : circuits integres specialises</li>
<li><strong>Systemes temps reel</strong> : logique cablee haute performance</li>
</ul>

<hr/>

<h2>PART B - Experience Personnelle et Contexte d'Apprentissage</h2>

<h3 class="section-title">Organisation et ressources</h3>

<p>Le module etait organise en cours magistraux et bureau d'etudes pratique :</p>

<p><strong>Cours magistraux (16h)</strong> :</p>
<ul>
<li>Syntaxe et structure VHDL</li>
<li>Types de donnees et operateurs</li>
<li>Logique combinatoire et sequentielle</li>
<li>Machines a etats finis (FSM)</li>
<li>Architectures de processeurs</li>
</ul>

<p><strong>Bureau d'etudes (20h)</strong> :</p>
<p>Projets de conception progressive avec Xilinx Vivado :</p>
<ul>
<li>Projet ALU : unite arithmetique et logique</li>
<li>Projet registre : banc de registres</li>
<li>Projet buffer : memoire tampon</li>
<li>Projet memoire instruction : ROM pour code programme</li>
<li>Projet memoire donnee : RAM pour donnees</li>
<li>Projet processeur : integration complete</li>
</ul>

<p><strong>Devoirs maison</strong> :</p>
<ul>
<li>DM1 : ALU et testbench</li>
<li>DM2 : Circuit numerique complexe</li>
</ul>

<p><strong>Outils utilises</strong> :</p>
<ul>
<li>Xilinx Vivado Design Suite (synthese, simulation, implementation)</li>
<li>FPGA cible : probablement Artix-7 ou Zynq</li>
<li>Testbenches VHDL pour simulation</li>
<li>Waveform viewer (fichiers .wcfg)</li>
</ul>

<h3 class="section-title">Structure des projets</h3>

<p>Chaque projet Vivado contenait :</p>
<ul>
<li><strong>Sources</strong> : fichiers VHDL (sources_1/new/)</li>
<li><strong>Simulations</strong> : testbenches (sim_1/)</li>
<li><strong>Contraintes</strong> : fichiers .xdc pour mapping des pins (constrs_1/)</li>
<li><strong>Waveforms</strong> : fichiers .wcfg pour visualisation des signaux</li>
<li><strong>Synthese et implementation</strong> : runs/synth_1/, runs/impl_1/</li>
</ul>

<p><strong>Progression pedagogique</strong> :</p>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S7/vhdl/architecture-vhdl.svg" alt="Architecture VHDL" style="max-width: 600px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Architecture d'un processeur simple en VHDL - ALU, registres et memoire</p>
</div>

<ol>
<li><strong>Buffer</strong> : Circuit simple (FIFO ou registre a decalage)</li>
<li><strong>ALU</strong> : Operations arithmetiques et logiques</li>
<li><strong>Registre</strong> : Banc de registres avec lecture/ecriture</li>
<li><strong>Memoire instruction</strong> : ROM pour stocker le programme</li>
<li><strong>Memoire donnee</strong> : RAM pour stocker les donnees</li>
<li><strong>Processeur</strong> : Assemblage final (chemin de donnees + unite de controle)</li>
</ol>

<h3 class="section-title">Methode de travail</h3>

<p><strong>Phase 1 : Specification</strong> :</p>
<p>Definir l'interface (ports d'entree/sortie) et le comportement attendu du circuit.</p>

<p><strong>Phase 2 : Code VHDL</strong> :</p>
<p>Ecrire le code dans Vivado, respecter les regles de synthetisabilite.</p>

<p><strong>Phase 3 : Testbench</strong> :</p>
<p>Creer un testbench pour verifier fonctionnellement le circuit par simulation.</p>

<p><strong>Phase 4 : Simulation</strong> :</p>
<p>Lancer la simulation comportementale, observer les chronogrammes (waveforms), corriger les erreurs.</p>

<p><strong>Phase 5 : Synthese</strong> :</p>
<p>Verifier que le code se synthetise sans erreurs, analyser l'utilisation des ressources (LUT, FF, BRAM).</p>

<p><strong>Phase 6 : Implementation</strong> (optionnel) :</p>
<p>Placer et router le design, verifier le timing, programmer le FPGA.</p>

<h3 class="section-title">Difficultes rencontrees</h3>

<p><strong>Pensee parallele</strong> :</p>
<p>VHDL decrit du materiel ou tout s'execute en parallele, contrairement a la programmation sequentielle. Comprendre que les process s'executent simultanement demande un changement de paradigme.</p>

<p><strong>Syntaxe stricte</strong> :</p>
<p>VHDL est verbeux et type fortement. Les erreurs de syntaxe ou de typage sont frequentes au debut.</p>

<p><strong>Timing et synchronisation</strong> :</p>
<p>Gerer correctement les horloges, resets, et eviter les hazards (glitches) necessite de la rigueur.</p>

<p><strong>Debugging</strong> :</p>
<p>Sans printf ni debogueur, le debugging se fait via les chronogrammes. Savoir quels signaux observer est crucial.</p>

<hr/>

<h2>PART C - Aspects Techniques Detailles</h2>

<h3 class="section-title">1. Introduction au VHDL</h3>

<p><strong>VHDL = VHSIC Hardware Description Language</strong></p>

<p>VHSIC = Very High Speed Integrated Circuit</p>

<p><strong>Langage de description materielle</strong> :</p>
<ul>
<li>Decrit la structure et le comportement de circuits numeriques</li>
<li>Utilise pour simulation et synthese (generation de circuits reels)</li>
<li>Standard IEEE (IEEE 1076)</li>
</ul>

<p><strong>Difference programmation logicielle</strong> :</p>

<table>
<tr><th>Aspect</th><th>Logiciel</th><th>Materiel (VHDL)</th></tr>
<tr><td>Execution</td><td>Sequentielle</td><td>Parallele</td></tr>
<tr><td>Variables</td><td>Modifiees en sequence</td><td>Signaux qui evoluent dans le temps</td></tr>
<tr><td>Boucles</td><td>Iterations</td><td>Replication de materiel</td></tr>
<tr><td>Ressources</td><td>Abstraites (memoire virtuelle)</td><td>Physiques limitees (LUT, FF)</td></tr>
</table>

<h3 class="section-title">2. Structure d'un fichier VHDL</h3>

<p><strong>Entity (entite)</strong> :</p>
<p>Decrit l'interface du composant (ports d'entree/sortie).</p>

<p>Exemple :</p>
<pre><code>entity compteur is
  port (
    clk    : in  std_logic;
    reset  : in  std_logic;
    enable : in  std_logic;
    count  : out std_logic_vector(7 downto 0)
  );
end entity compteur;</code></pre>

<p><strong>Architecture</strong> :</p>
<p>Decrit le comportement ou la structure interne du composant.</p>

<p>Exemple :</p>
<pre><code>architecture behavioral of compteur is
  signal count_internal : unsigned(7 downto 0);
begin
  process(clk, reset)
  begin
    if reset = '1' then
      count_internal &lt;= (others =&gt; '0');
    elsif rising_edge(clk) then
      if enable = '1' then
        count_internal &lt;= count_internal + 1;
      end if;
    end if;
  end process;

  count &lt;= std_logic_vector(count_internal);
end architecture behavioral;</code></pre>

<p><strong>Types d'architectures</strong> :</p>

<table>
<tr><th>Type</th><th>Description</th><th>Usage</th></tr>
<tr><td>Behavioral</td><td>Description algorithmique du comportement</td><td>Haut niveau, synthese automatique</td></tr>
<tr><td>Dataflow</td><td>Affectations concurrentes, equations</td><td>Logique combinatoire</td></tr>
<tr><td>Structural</td><td>Instanciation de composants</td><td>Hierarchie, connexion de blocs</td></tr>
</table>

<h3 class="section-title">3. Types de donnees VHDL</h3>

<p><strong>Types standards</strong> :</p>

<table>
<tr><th>Type</th><th>Description</th><th>Exemple</th></tr>
<tr><td>std_logic</td><td>Bit logique (9 valeurs)</td><td>'0', '1', 'Z', 'X', etc.</td></tr>
<tr><td>std_logic_vector</td><td>Vecteur de bits</td><td>"10110101"</td></tr>
<tr><td>integer</td><td>Entier</td><td>-2147483648 a 2147483647</td></tr>
<tr><td>unsigned</td><td>Entier non signe</td><td>utilise pour calculs arithmetiques</td></tr>
<tr><td>signed</td><td>Entier signe</td><td>complement a 2</td></tr>
</table>

<p><strong>Valeurs std_logic</strong> :</p>
<ul>
<li>'0' : niveau bas</li>
<li>'1' : niveau haut</li>
<li>'Z' : haute impedance (trois etats)</li>
<li>'X' : inconnu (non initialise)</li>
<li>'-' : don't care (synthese)</li>
</ul>

<p><strong>Bibliotheques necessaires</strong> :</p>
<pre><code>library IEEE;
use IEEE.STD_LOGIC_1164.ALL;      -- std_logic, std_logic_vector
use IEEE.NUMERIC_STD.ALL;         -- unsigned, signed, conversion
use IEEE.STD_LOGIC_UNSIGNED.ALL;  -- operations sur std_logic_vector (ancien)</code></pre>

<h3 class="section-title">4. Logique combinatoire</h3>

<p><strong>Affectation concurrente</strong> :</p>

<p>Les affectations en dehors des process s'executent en parallele.</p>

<p>Exemples :</p>
<pre><code>-- Porte AND
y &lt;= a and b;

-- Multiplexeur
y &lt;= a when sel = '0' else b;

-- Multiplexeur 4 vers 1
with sel select
  y &lt;= a when "00",
       b when "01",
       c when "10",
       d when others;</code></pre>

<p><strong>Process combinatoire</strong> :</p>

<p>Pour decrire de la logique combinatoire dans un process :</p>
<pre><code>process(a, b, c)  -- Liste de sensibilite : tous les signaux lus
begin
  if a = '1' then
    y &lt;= b;
  else
    y &lt;= c;
  end if;
end process;</code></pre>

<p><strong>Attention</strong> : Si un signal lu n'est pas dans la liste de sensibilite, le process ne se met pas a jour - difference simulation/synthese.</p>

<h3 class="section-title">5. Logique sequentielle</h3>

<p><strong>Bascule D (D Flip-Flop)</strong> :</p>

<p>Element de base de la logique sequentielle. Memorise une valeur sur un front d'horloge.</p>

<pre><code>process(clk)
begin
  if rising_edge(clk) then  -- Front montant
    q &lt;= d;
  end if;
end process;</code></pre>

<p><strong>Avec reset asynchrone</strong> :</p>
<pre><code>process(clk, reset)
begin
  if reset = '1' then       -- Reset prioritaire
    q &lt;= '0';
  elsif rising_edge(clk) then
    q &lt;= d;
  end if;
end process;</code></pre>

<p><strong>Avec reset synchrone</strong> :</p>
<pre><code>process(clk)
begin
  if rising_edge(clk) then
    if reset = '1' then
      q &lt;= '0';
    else
      q &lt;= d;
    end if;
  end if;
end process;</code></pre>

<p><strong>Regle d'or</strong> :</p>
<ul>
<li>Reset asynchrone : dans la sensibilite du process et teste en premier</li>
<li>Reset synchrone : a l'interieur du test de rising_edge</li>
</ul>

<h3 class="section-title">6. Machines a etats finis (FSM)</h3>

<p><strong>Definition</strong> :</p>

<p>Une FSM (Finite State Machine) est un circuit sequentiel avec un nombre fini d'etats. Elle change d'etat selon les entrees et l'etat courant.</p>

<p><strong>Types</strong> :</p>
<ul>
<li><strong>Moore</strong> : sorties dependent seulement de l'etat</li>
<li><strong>Mealy</strong> : sorties dependent de l'etat et des entrees</li>
</ul>

<p><strong>Structure a 2 process</strong> :</p>

<p><strong>Process 1 : Registre d'etat (sequentiel)</strong></p>
<pre><code>process(clk, reset)
begin
  if reset = '1' then
    etat_courant &lt;= IDLE;
  elsif rising_edge(clk) then
    etat_courant &lt;= etat_suivant;
  end if;
end process;</code></pre>

<p><strong>Process 2 : Logique de transition (combinatoire)</strong></p>
<pre><code>process(etat_courant, entree)
begin
  case etat_courant is
    when IDLE =&gt;
      if entree = '1' then
        etat_suivant &lt;= TRAITEMENT;
      else
        etat_suivant &lt;= IDLE;
      end if;
      sortie &lt;= '0';

    when TRAITEMENT =&gt;
      if compteur_fini = '1' then
        etat_suivant &lt;= FIN;
      else
        etat_suivant &lt;= TRAITEMENT;
      end if;
      sortie &lt;= '1';

    when FIN =&gt;
      etat_suivant &lt;= IDLE;
      sortie &lt;= '0';

    when others =&gt;
      etat_suivant &lt;= IDLE;
      sortie &lt;= '0';
  end case;
end process;</code></pre>

<p><strong>Declaration des etats</strong> :</p>
<pre><code>type etat_type is (IDLE, TRAITEMENT, FIN);
signal etat_courant, etat_suivant : etat_type;</code></pre>

<h3 class="section-title">7. Unite Arithmetique et Logique (ALU)</h3>

<p><strong>Principe</strong> :</p>

<p>L'ALU effectue les operations arithmetiques (addition, soustraction) et logiques (AND, OR, XOR) d'un processeur.</p>

<p><strong>Interface typique</strong> :</p>
<pre><code>entity ALU is
  port (
    A      : in  std_logic_vector(31 downto 0);  -- Operande A
    B      : in  std_logic_vector(31 downto 0);  -- Operande B
    OP     : in  std_logic_vector(3 downto 0);   -- Code operation
    Result : out std_logic_vector(31 downto 0);  -- Resultat
    Zero   : out std_logic;                      -- Flag zero
    Carry  : out std_logic                       -- Flag retenue
  );
end entity ALU;</code></pre>

<p><strong>Operations courantes</strong> :</p>

<table>
<tr><th>Code OP</th><th>Operation</th><th>Description</th></tr>
<tr><td>0000</td><td>AND</td><td>ET logique bit a bit</td></tr>
<tr><td>0001</td><td>OR</td><td>OU logique bit a bit</td></tr>
<tr><td>0010</td><td>ADD</td><td>Addition</td></tr>
<tr><td>0110</td><td>SUB</td><td>Soustraction (A - B)</td></tr>
<tr><td>0111</td><td>SLT</td><td>Set if Less Than (A &lt; B)</td></tr>
<tr><td>1100</td><td>NOR</td><td>NON-OU logique</td></tr>
</table>

<p><strong>Implementation</strong> :</p>
<pre><code>process(A, B, OP)
  variable temp : unsigned(32 downto 0);  -- 33 bits pour la retenue
begin
  case OP is
    when "0000" =&gt;  -- AND
      Result &lt;= A and B;
      Carry &lt;= '0';

    when "0001" =&gt;  -- OR
      Result &lt;= A or B;
      Carry &lt;= '0';

    when "0010" =&gt;  -- ADD
      temp := ('0' &amp; unsigned(A)) + ('0' &amp; unsigned(B));
      Result &lt;= std_logic_vector(temp(31 downto 0));
      Carry &lt;= temp(32);

    when "0110" =&gt;  -- SUB
      temp := ('0' &amp; unsigned(A)) - ('0' &amp; unsigned(B));
      Result &lt;= std_logic_vector(temp(31 downto 0));
      Carry &lt;= temp(32);

    when others =&gt;
      Result &lt;= (others =&gt; '0');
      Carry &lt;= '0';
  end case;

  -- Flag Zero
  if Result = x"00000000" then
    Zero &lt;= '1';
  else
    Zero &lt;= '0';
  end if;
end process;</code></pre>

<h3 class="section-title">8. Banc de registres</h3>

<p><strong>Principe</strong> :</p>

<p>Ensemble de registres (16 ou 32 typiquement) pour stocker temporairement des donnees dans un processeur.</p>

<p><strong>Interface</strong> :</p>
<pre><code>entity RegisterFile is
  port (
    clk       : in  std_logic;
    reset     : in  std_logic;
    -- Lecture
    ReadAddr1 : in  std_logic_vector(4 downto 0);   -- Adresse registre 1
    ReadAddr2 : in  std_logic_vector(4 downto 0);   -- Adresse registre 2
    ReadData1 : out std_logic_vector(31 downto 0);  -- Donnee registre 1
    ReadData2 : out std_logic_vector(31 downto 0);  -- Donnee registre 2
    -- Ecriture
    WriteEn   : in  std_logic;                      -- Autorisation ecriture
    WriteAddr : in  std_logic_vector(4 downto 0);   -- Adresse ecriture
    WriteData : in  std_logic_vector(31 downto 0)   -- Donnee a ecrire
  );
end entity RegisterFile;</code></pre>

<p><strong>Implementation</strong> :</p>
<pre><code>architecture behavioral of RegisterFile is
  type reg_array is array (0 to 31) of std_logic_vector(31 downto 0);
  signal registers : reg_array;
begin
  -- Ecriture synchrone
  process(clk, reset)
  begin
    if reset = '1' then
      registers &lt;= (others =&gt; (others =&gt; '0'));
    elsif rising_edge(clk) then
      if WriteEn = '1' and WriteAddr /= "00000" then  -- R0 toujours a 0
        registers(to_integer(unsigned(WriteAddr))) &lt;= WriteData;
      end if;
    end if;
  end process;

  -- Lecture asynchrone
  ReadData1 &lt;= registers(to_integer(unsigned(ReadAddr1)));
  ReadData2 &lt;= registers(to_integer(unsigned(ReadAddr2)));
end architecture behavioral;</code></pre>

<p><strong>Particularite</strong> :</p>
<p>Le registre R0 est souvent cable a zero (convention MIPS/RISC-V).</p>

<h3 class="section-title">9. Memoires</h3>

<p><strong>ROM (Read-Only Memory)</strong> :</p>

<p>Utilisee pour stocker le programme (instructions).</p>

<pre><code>architecture behavioral of ROM is
  type rom_array is array (0 to 255) of std_logic_vector(31 downto 0);
  constant rom_data : rom_array := (
    x"00000000",  -- NOP
    x"20010005",  -- ADDI R1, R0, 5
    x"20020003",  -- ADDI R2, R0, 3
    x"00221820",  -- ADD R3, R1, R2
    -- ... autres instructions
    others =&gt; x"00000000"
  );
begin
  process(clk)
  begin
    if rising_edge(clk) then
      data_out &lt;= rom_data(to_integer(unsigned(address)));
    end if;
  end process;
end architecture behavioral;</code></pre>

<p><strong>RAM (Random Access Memory)</strong> :</p>

<p>Utilisee pour stocker les donnees.</p>

<pre><code>architecture behavioral of RAM is
  type ram_array is array (0 to 1023) of std_logic_vector(31 downto 0);
  signal ram_data : ram_array := (others =&gt; (others =&gt; '0'));
begin
  process(clk)
  begin
    if rising_edge(clk) then
      if write_enable = '1' then
        ram_data(to_integer(unsigned(address))) &lt;= data_in;
      end if;
      data_out &lt;= ram_data(to_integer(unsigned(address)));
    end if;
  end process;
end architecture behavioral;</code></pre>

<p><strong>Utilisation des BRAM (Block RAM) sur FPGA</strong> :</p>

<p>Les FPGA possedent des blocs memoire dedies (BRAM). Vivado infere automatiquement des BRAM si le code suit certains modeles (comme ci-dessus).</p>

<h3 class="section-title">10. Processeur simple</h3>

<p><strong>Architecture</strong> :</p>

<p>Un processeur minimal contient :</p>
<ul>
<li><strong>Chemin de donnees (Datapath)</strong> : ALU, registres, memoires, multiplexeurs</li>
<li><strong>Unite de controle</strong> : FSM qui genere les signaux de controle</li>
</ul>

<p><strong>Cycle d'execution</strong> :</p>

<ol>
<li><strong>Fetch</strong> : Lire l'instruction en memoire (PC &rarr; Mem_Instr &rarr; IR)</li>
<li><strong>Decode</strong> : Decoder l'instruction (champs opcode, registres, immediat)</li>
<li><strong>Execute</strong> : Executer l'operation (ALU)</li>
<li><strong>Memory</strong> : Acces memoire donnees si necessaire (LOAD/STORE)</li>
<li><strong>Write Back</strong> : Ecrire le resultat dans le registre destination</li>
</ol>

<p><strong>Signaux de controle</strong> :</p>

<p>L'unite de controle genere des signaux pour piloter le datapath :</p>
<ul>
<li>RegWrite : autoriser ecriture dans le banc de registres</li>
<li>ALUOp : selection operation ALU</li>
<li>MemRead, MemWrite : lecture/ecriture memoire donnees</li>
<li>MemToReg : selection source donnee a ecrire dans registre</li>
<li>Branch : autoriser branchement conditionnel</li>
</ul>

<p><strong>Exemple simplifie</strong> :</p>

<p>Type d'instruction R (registre-registre) :</p>
<ul>
<li>Opcode determine que c'est une instruction R</li>
<li>Lire deux registres sources (rs, rt)</li>
<li>ALU effectue l'operation (funct determine laquelle)</li>
<li>Ecrire le resultat dans registre destination (rd)</li>
</ul>

<h3 class="section-title">11. Testbench et simulation</h3>

<p><strong>Testbench</strong> :</p>

<p>Fichier VHDL sans ports (entity vide) qui instancie le circuit a tester (UUT - Unit Under Test) et genere des stimuli.</p>

<p><strong>Structure</strong> :</p>
<pre><code>entity testbench is
  -- Pas de ports
end entity testbench;

architecture test of testbench is
  -- Declaration des signaux de test
  signal clk : std_logic := '0';
  signal reset : std_logic := '1';
  signal input : std_logic_vector(7 downto 0);
  signal output : std_logic_vector(7 downto 0);

  constant CLK_PERIOD : time := 10 ns;
begin
  -- Instanciation du composant a tester
  UUT: entity work.mon_circuit
    port map (
      clk =&gt; clk,
      reset =&gt; reset,
      input =&gt; input,
      output =&gt; output
    );

  -- Generation de l'horloge
  clk_process: process
  begin
    clk &lt;= '0';
    wait for CLK_PERIOD/2;
    clk &lt;= '1';
    wait for CLK_PERIOD/2;
  end process;

  -- Generation des stimuli
  stim_process: process
  begin
    reset &lt;= '1';
    input &lt;= x"00";
    wait for 50 ns;

    reset &lt;= '0';
    wait for 10 ns;

    input &lt;= x"12";
    wait for 20 ns;

    input &lt;= x"34";
    wait for 20 ns;

    wait;  -- Arret de la simulation
  end process;
end architecture test;</code></pre>

<p><strong>Verifications</strong> :</p>

<p>Utiliser des assertions pour verifier automatiquement :</p>
<pre><code>assert (output = x"46") report "Erreur : resultat incorrect" severity error;</code></pre>

<p><strong>Waveform (chronogramme)</strong> :</p>

<p>Fichiers .wcfg dans Vivado permettent de configurer quels signaux afficher et comment. Essentiels pour le debugging visuel.</p>

<h3 class="section-title">12. Synthese et implementation sur FPGA</h3>

<p><strong>Etapes</strong> :</p>

<p><strong>1. Synthese (Synthesis)</strong> :</p>
<ul>
<li>Conversion du code VHDL en netlist (portes logiques)</li>
<li>Optimisation logique</li>
<li>Verification que le code est synthetisable</li>
</ul>

<p><strong>2. Implementation</strong> :</p>
<ul>
<li>Placement : affecter les ressources logiques aux elements du FPGA (LUT, FF)</li>
<li>Routage : connecter les elements via les interconnexions</li>
<li>Verification timing : s'assurer que les contraintes temporelles sont respectees</li>
</ul>

<p><strong>3. Generation du bitstream</strong> :</p>
<ul>
<li>Fichier .bit a programmer dans le FPGA</li>
</ul>

<p><strong>Ressources FPGA</strong> :</p>

<table>
<tr><th>Ressource</th><th>Description</th></tr>
<tr><td>LUT (Look-Up Table)</td><td>Implemente logique combinatoire (fonction quelconque de N entrees)</td></tr>
<tr><td>FF (Flip-Flop)</td><td>Bascule D pour logique sequentielle</td></tr>
<tr><td>BRAM (Block RAM)</td><td>Blocs memoire dedies (18 Kb ou 36 Kb)</td></tr>
<tr><td>DSP</td><td>Blocs multiplicateurs/accumulateurs materiels</td></tr>
<tr><td>IO</td><td>Broches d'entree/sortie configurables</td></tr>
</table>

<p><strong>Contraintes</strong> :</p>

<p>Fichier .xdc (Xilinx Design Constraints) :</p>
<ul>
<li>Affectation des pins physiques</li>
<li>Definition des horloges (periode, frequence)</li>
<li>Contraintes de timing</li>
</ul>

<p>Exemple :</p>
<pre><code># Horloge 100 MHz
create_clock -period 10.000 -name clk [get_ports clk]

# Pins
set_property PACKAGE_PIN W5 [get_ports clk]
set_property IOSTANDARD LVCMOS33 [get_ports clk]

set_property PACKAGE_PIN U16 [get_ports led[0]]
set_property IOSTANDARD LVCMOS33 [get_ports led[0]]</code></pre>

<hr/>

<h2>PART D - Analyse Reflexive et Perspectives</h2>

<h3 class="section-title">Competences acquises</h3>

<p><strong>Conception materielle</strong> :</p>
<p>Maitrise du VHDL pour decrire des circuits numeriques synthetisables. Capacite a penser en termes de parallelisme materiel plutot que sequence logicielle.</p>

<p><strong>Architecture de processeur</strong> :</p>
<p>Comprehension profonde du fonctionnement interne d'un processeur : ALU, registres, memoires, unite de controle, chemin de donnees.</p>

<p><strong>Outils professionnels</strong> :</p>
<p>Utilisation de Xilinx Vivado, outil standard de l'industrie pour FPGA. Simulation, synthese, implementation, analyse de timing.</p>

<h3 class="section-title">Points cles a retenir</h3>

<p><strong>1. VHDL = description materielle, pas programmation</strong> :</p>
<p>Le code VHDL decrit du materiel qui existe physiquement. Tout s'execute en parallele. Changement de paradigme fondamental.</p>

<p><strong>2. Synthetisabilite</strong> :</p>
<p>Tout le code VHDL ne peut pas etre synthetise en materiel. Eviter wait for (sauf dans testbenches), boucles infinies, division par variables, etc.</p>

<p><strong>3. Horloge et synchronisme</strong> :</p>
<p>Les circuits synchrones (cadences par horloge) sont plus robustes et previsibles. Toujours utiliser rising_edge(clk) pour detecter les fronts.</p>

<p><strong>4. Testbench = essentiel</strong> :</p>
<p>La simulation avec testbench permet de valider le fonctionnement avant synthese. Debug beaucoup plus facile qu'apres implementation.</p>

<p><strong>5. Ressources limitees</strong> :</p>
<p>Les FPGA ont un nombre fini de LUT, FF, BRAM. Importance de l'optimisation et du partage de ressources.</p>

<h3 class="section-title">Applications pratiques</h3>

<p><strong>Traitement du signal</strong> :</p>
<p>Implementation de filtres numeriques haute performance (FIR, IIR), FFT, traitement d'image temps reel.</p>

<p><strong>Accelerateurs materiels</strong> :</p>
<p>Acceleration de calculs intensifs (cryptographie, compression, IA) en dechargeant le processeur.</p>

<p><strong>Systemes embarques critiques</strong> :</p>
<p>Aeronautique, automobile, spatial necessitent des circuits deterministes et fiables (logique cablee sur FPGA ou ASIC).</p>

<p><strong>Prototypage ASIC</strong> :</p>
<p>Les FPGA servent a valider des designs avant fabrication d'ASIC (cout eleve, non modifiable).</p>

<h3 class="section-title">Retour d'experience</h3>

<p><strong>Courbe d'apprentissage</strong> :</p>
<p>VHDL est plus difficile que la programmation classique au debut. Necessite de comprendre le materiel sous-jacent.</p>

<p><strong>Projets progressifs</strong> :</p>
<p>La progression Buffer &rarr; ALU &rarr; Registres &rarr; Memoires &rarr; Processeur est pedagogiquement excellente. Chaque etape ajoute de la complexite.</p>

<p><strong>Vivado puissant mais complexe</strong> :</p>
<p>L'outil est complet mais l'interface peut etre intimidante. Temps de synthese/implementation parfois long.</p>

<p><strong>Debugging visuel</strong> :</p>
<p>Les waveforms (chronogrammes) sont indispensables. Savoir identifier les signaux critiques a observer facilite grandement le debugging.</p>

<h3 class="section-title">Limites et ouvertures</h3>

<p><strong>Limites du module</strong> :</p>
<ul>
<li>Pas d'implementation physique sur carte FPGA (simulation seulement)</li>
<li>Processeur tres simplifie (pas de pipeline, cache, etc.)</li>
<li>Aspects timing et optimisation peu approfondis</li>
</ul>

<p><strong>Ouvertures vers</strong> :</p>
<ul>
<li><strong>Processeurs avances</strong> : pipeline, prediction de branchement, cache</li>
<li><strong>Systemes sur puce (SoC)</strong> : processeur + peripheriques integres</li>
<li><strong>High-Level Synthesis (HLS)</strong> : generer VHDL depuis C/C++</li>
<li><strong>Verification formelle</strong> : assertions, model checking</li>
<li><strong>ASIC design</strong> : conception de circuits integres application specifique</li>
</ul>

<h3 class="section-title">Evolution technologique</h3>

<p><strong>Tendances actuelles</strong> :</p>

<p><strong>HLS (High-Level Synthesis)</strong> :</p>
<p>Outils comme Vivado HLS ou Vitis HLS permettent d'ecrire en C/C++ et generent automatiquement du VHDL/Verilog. Accelere le developpement.</p>

<p><strong>FPGA + IA</strong> :</p>
<p>Les FPGA modernes (Versal, Zynq UltraScale+) integrent des accelerateurs IA (DPU). Utilises pour inference de reseaux de neurones temps reel.</p>

<p><strong>FPGA adaptatives (Versal)</strong> :</p>
<p>Architecture hybride : FPGA + CPU + DSP + IA. Reconfiguration dynamique.</p>

<p><strong>Cloud FPGA</strong> :</p>
<p>AWS, Azure, Alibaba proposent des instances avec FPGA pour acceleration dans le cloud.</p>

<h3 class="section-title">Conseils pour reussir</h3>

<p><strong>1. Penser materiel</strong> :</p>
<p>Visualiser mentalement les portes, bascules, multiplexeurs generes par votre code VHDL.</p>

<p><strong>2. Simuler tot et souvent</strong> :</p>
<p>Ne pas attendre d'avoir ecrit tout le code. Tester chaque module independamment.</p>

<p><strong>3. Bien commenter</strong> :</p>
<p>VHDL est verbeux. Des commentaires clairs aident a relire le code plus tard.</p>

<p><strong>4. Respecter les conventions</strong> :</p>
<p>Noms de signaux explicites (clk, reset, enable), indentation coherente.</p>

<p><strong>5. Utiliser les types appropries</strong> :</p>
<p>unsigned/signed pour arithmetique, std_logic_vector pour bus de donnees generiques.</p>

<h3 class="section-title">Conclusion</h3>

<p>Ce module fournit une excellente introduction a la conception numerique avec VHDL et FPGA. La realisation d'un processeur complet, meme simple, permet de comprendre en profondeur l'architecture des ordinateurs.</p>

<p><strong>Competences transferables</strong> :</p>
<ul>
<li>Pensee parallele et conception materielle</li>
<li>Rigueur dans la specification et la verification</li>
<li>Maitrise d'outils professionnels (Vivado)</li>
<li>Comprehension de l'architecture des processeurs</li>
</ul>

<p><strong>Pertinence professionnelle</strong> :</p>
<p>Les FPGA sont utilises dans de nombreux domaines (telecommunications, defense, medical, automobile, finance). La demande en ingenieurs FPGA reste forte.</p>

<p><strong>Message principal</strong> :</p>
<p>VHDL et les FPGA offrent un controle total sur le materiel, permettant des performances et une efficacite energetique inatteignables avec du logiciel seul. La maitrise de ces outils ouvre des opportunites dans les systemes haute performance.</p>

<p><strong>Recommandations</strong> :</p>
<ul>
<li>Pratiquer sur des cartes FPGA reelles (Basys, Arty, DE10-Nano)</li>
<li>Explorer des projets plus complexes (controleurs, interfaces, DSP)</li>
<li>Apprendre Verilog en complement (langage concurrent)</li>
<li>Se former au HLS pour accelerer le developpement</li>
<li>Etudier l'architecture de processeurs reels (RISC-V open-source)</li>
</ul>

<p><strong>Liens avec les autres cours</strong> :</p>
<ul>
<li><a href="./architecture-informatique-materielle.html">Architecture Informatique materielle - S5</a> : structure processeur</li>
<li><a href="./fondements-electronique-numerique.html">Fondements electronique numerique - S5</a> : portes logiques</li>
<li><a href="./embedded-ia-iot.html">Embedded IA for IoT - S9</a> : acceleration materielle</li>
</ul>

<hr/>

<h2>Illustrations du Projet BE Pipeline</h2>

<div style="text-align: center; margin: 20px 0;">
  <img src="/img/BE_Pipeline/Pipeline_path.png" alt="Chemin de donnees du pipeline processeur" style="max-width: 700px; border: 1px solid #ddd; padding: 10px; border-radius: 8px;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Chemin de donnees (Datapath) du processeur pipeline</p>
</div>

<div style="text-align: center; margin: 20px 0;">
  <img src="/img/BE_Pipeline/ALU.png" alt="Schema de l'ALU" style="max-width: 700px; border: 1px solid #ddd; padding: 10px; border-radius: 8px;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Schema de l'Unite Arithmetique et Logique (ALU)</p>
</div>

<div style="text-align: center; margin: 20px 0;">
  <img src="/img/BE_Pipeline/Register_bench.png" alt="Banc de registres" style="max-width: 700px; border: 1px solid #ddd; padding: 10px; border-radius: 8px;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Banc de registres (Register Bench)</p>
</div>

<div style="text-align: center; margin: 20px 0;">
  <img src="/img/BE_Pipeline/Instruction_Memory.png" alt="Memoire d'instructions" style="max-width: 700px; border: 1px solid #ddd; padding: 10px; border-radius: 8px;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Memoire d'instructions (Instruction Memory)</p>
</div>

<div style="text-align: center; margin: 20px 0;">
  <img src="/img/BE_Pipeline/Data_Memory.png" alt="Memoire de donnees" style="max-width: 700px; border: 1px solid #ddd; padding: 10px; border-radius: 8px;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Memoire de donnees (Data Memory)</p>
</div>

<div style="text-align: center; margin: 20px 0;">
  <img src="/img/BE_Pipeline/ALEA.png" alt="Gestion des aleas du pipeline" style="max-width: 700px; border: 1px solid #ddd; padding: 10px; border-radius: 8px;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Gestion des aleas (hazards) dans le pipeline</p>
</div>

<hr/>

<h2>Rapports et Projets</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4><span class="lang-fr">Rapport de Projet VHDL</span><span class="lang-en">VHDL Project Report</span></h4>
      <p><span class="lang-fr">Rapport du bureau d'etudes : conception d'un processeur pipeline en VHDL, incluant ALU, banc de registres, memoires et gestion des aleas.</span><span class="lang-en">Design study report: pipeline processor design in VHDL, including ALU, register file, memories and hazard management.</span></p>
      <p style="text-align: center;">
        <a href="/file/reports/S7/Rapport_VHDL.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          <span class="lang-fr">Telecharger le rapport PDF</span><span class="lang-en">Download PDF report</span>
        </a>
      </p>
    </div>
  </div>
</div>

<hr/>

<h2><span class="lang-fr">Documents de Cours</span><span class="lang-en">Course Documents</span></h2>

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

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4><span class="lang-fr">Cours VHDL Complet</span><span class="lang-en">Complete VHDL Course</span></h4>
      <p><span class="lang-fr">Cours complet de VHDL : syntaxe, processus, machines a etats, simulation et synthese pour FPGA.</span><span class="lang-en">Complete VHDL course: syntax, processes, state machines, simulation and synthesis for FPGA.</span></p>
      <div class="pdf-lazy" data-src="/cours-pdf/S7/Archi-Numeriques-VHDL/cours-vhdl.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S7/Archi-Numeriques-VHDL/cours-vhdl.pdf" target="_blank"><span class="lang-fr">Telecharger</span><span class="lang-en">Download</span></a></p>
    </div>
    <div class="pdf-item">
      <h4><span class="lang-fr">Projet Processeur RISC</span><span class="lang-en">RISC Processor Project</span></h4>
      <p><span class="lang-fr">Sujet du projet BE : conception d'un microprocesseur RISC en VHDL avec ALU, banc de registres et memoire.</span><span class="lang-en">Design study project brief: RISC microprocessor design in VHDL with ALU, register file and memory.</span></p>
      <div class="pdf-lazy" data-src="/cours-pdf/S7/Archi-Numeriques-VHDL/projet-risc.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S7/Archi-Numeriques-VHDL/projet-risc.pdf" target="_blank"><span class="lang-fr">Telecharger</span><span class="lang-en">Download</span></a></p>
    </div>
  </div>
</div>

<hr/>

<p><em>Cours suivi en 2023-2024 a l'INSA Toulouse, Departement Genie Electrique et Informatique.</em></p>

</div>

<div class="lang-en">

<h1>Advanced Digital Architectures VHDL - Semester 7</h1>

<p><strong>Academic Year</strong>: 2023-2024<br/>
<strong>Semester</strong>: 7<br/>
<strong>Credits</strong>: 2.5 ECTS<br/>
<strong>Specialization</strong>: Digital Design and FPGA</p>

<hr/>

<h2>PART A - General Module Presentation</h2>

<h3 class="section-title">Overview</h3>

<p>This course teaches the design of complex digital systems using the VHDL language (VHSIC Hardware Description Language) and their implementation on FPGA. It covers the design of advanced digital architectures: arithmetic and logic unit (ALU), register files, memories, and complete processors.</p>

<p><strong>Learning objectives</strong>:</p>
<ul>
<li>Master the VHDL language for hardware description</li>
<li>Design synthesizable digital circuits</li>
<li>Implement systems on FPGA (Xilinx)</li>
<li>Simulate and verify designs with testbenches</li>
<li>Understand finite state machines (FSM)</li>
<li>Design a complete simple processor</li>
</ul>

<h3 class="section-title">Position in the curriculum</h3>

<p>This module builds upon:</p>
<ul>
<li><strong>Digital Electronics Fundamentals (S5)</strong>: logic gates, flip-flops</li>
<li><strong>Sequential Logic (S5)</strong>: state machines, counters</li>
<li><strong>Hardware Computer Architecture (S5)</strong>: processor structure</li>
</ul>

<p>It prepares for:</p>
<ul>
<li><strong>Embedded systems</strong>: hardware accelerators</li>
<li><strong>Signal processing on FPGA</strong>: digital filter implementation</li>
<li><strong>ASIC design</strong>: specialized integrated circuits</li>
<li><strong>Real-time systems</strong>: high-performance hardwired logic</li>
</ul>

<hr/>

<h2>PART B - Personal Experience and Learning Context</h2>

<h3 class="section-title">Organization and resources</h3>

<p>The module was organized into lectures and practical design studies:</p>

<p><strong>Lectures (16h)</strong>:</p>
<ul>
<li>VHDL syntax and structure</li>
<li>Data types and operators</li>
<li>Combinational and sequential logic</li>
<li>Finite state machines (FSM)</li>
<li>Processor architectures</li>
</ul>

<p><strong>Design studies (20h)</strong>:</p>
<p>Progressive design projects with Xilinx Vivado:</p>
<ul>
<li>ALU project: arithmetic and logic unit</li>
<li>Register project: register file</li>
<li>Buffer project: buffer memory</li>
<li>Instruction memory project: ROM for program code</li>
<li>Data memory project: RAM for data</li>
<li>Processor project: complete integration</li>
</ul>

<p><strong>Homework assignments</strong>:</p>
<ul>
<li>HW1: ALU and testbench</li>
<li>HW2: Complex digital circuit</li>
</ul>

<p><strong>Tools used</strong>:</p>
<ul>
<li>Xilinx Vivado Design Suite (synthesis, simulation, implementation)</li>
<li>Target FPGA: likely Artix-7 or Zynq</li>
<li>VHDL testbenches for simulation</li>
<li>Waveform viewer (.wcfg files)</li>
</ul>

<h3 class="section-title">Project structure</h3>

<p>Each Vivado project contained:</p>
<ul>
<li><strong>Sources</strong>: VHDL files (sources_1/new/)</li>
<li><strong>Simulations</strong>: testbenches (sim_1/)</li>
<li><strong>Constraints</strong>: .xdc files for pin mapping (constrs_1/)</li>
<li><strong>Waveforms</strong>: .wcfg files for signal visualization</li>
<li><strong>Synthesis and implementation</strong>: runs/synth_1/, runs/impl_1/</li>
</ul>

<p><strong>Pedagogical progression</strong>:</p>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S7/vhdl/architecture-vhdl.svg" alt="VHDL Architecture" style="max-width: 600px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Architecture of a simple VHDL processor - ALU, registers and memory</p>
</div>

<ol>
<li><strong>Buffer</strong>: Simple circuit (FIFO or shift register)</li>
<li><strong>ALU</strong>: Arithmetic and logic operations</li>
<li><strong>Register</strong>: Register file with read/write</li>
<li><strong>Instruction memory</strong>: ROM for storing the program</li>
<li><strong>Data memory</strong>: RAM for storing data</li>
<li><strong>Processor</strong>: Final assembly (datapath + control unit)</li>
</ol>

<h3 class="section-title">Working method</h3>

<p><strong>Phase 1: Specification</strong>:</p>
<p>Define the interface (input/output ports) and the expected behavior of the circuit.</p>

<p><strong>Phase 2: VHDL Code</strong>:</p>
<p>Write the code in Vivado, comply with synthesizability rules.</p>

<p><strong>Phase 3: Testbench</strong>:</p>
<p>Create a testbench to functionally verify the circuit through simulation.</p>

<p><strong>Phase 4: Simulation</strong>:</p>
<p>Run behavioral simulation, observe waveforms, correct errors.</p>

<p><strong>Phase 5: Synthesis</strong>:</p>
<p>Verify that the code synthesizes without errors, analyze resource utilization (LUT, FF, BRAM).</p>

<p><strong>Phase 6: Implementation</strong> (optional):</p>
<p>Place and route the design, verify timing, program the FPGA.</p>

<h3 class="section-title">Challenges encountered</h3>

<p><strong>Parallel thinking</strong>:</p>
<p>VHDL describes hardware where everything executes in parallel, unlike sequential programming. Understanding that processes execute simultaneously requires a paradigm shift.</p>

<p><strong>Strict syntax</strong>:</p>
<p>VHDL is verbose and strongly typed. Syntax and type errors are frequent at first.</p>

<p><strong>Timing and synchronization</strong>:</p>
<p>Correctly managing clocks, resets, and avoiding hazards (glitches) requires rigor.</p>

<p><strong>Debugging</strong>:</p>
<p>Without printf or debugger, debugging is done through waveforms. Knowing which signals to observe is crucial.</p>

<hr/>

<h2>PART C - Detailed Technical Aspects</h2>

<h3 class="section-title">1. Introduction to VHDL</h3>

<p><strong>VHDL = VHSIC Hardware Description Language</strong></p>

<p>VHSIC = Very High Speed Integrated Circuit</p>

<p><strong>Hardware description language</strong>:</p>
<ul>
<li>Describes the structure and behavior of digital circuits</li>
<li>Used for simulation and synthesis (real circuit generation)</li>
<li>IEEE Standard (IEEE 1076)</li>
</ul>

<p><strong>Difference from software programming</strong>:</p>

<table>
<tr><th>Aspect</th><th>Software</th><th>Hardware (VHDL)</th></tr>
<tr><td>Execution</td><td>Sequential</td><td>Parallel</td></tr>
<tr><td>Variables</td><td>Modified sequentially</td><td>Signals that evolve over time</td></tr>
<tr><td>Loops</td><td>Iterations</td><td>Hardware replication</td></tr>
<tr><td>Resources</td><td>Abstract (virtual memory)</td><td>Limited physical (LUT, FF)</td></tr>
</table>

<h3 class="section-title">2. Structure of a VHDL file</h3>

<p><strong>Entity</strong>:</p>
<p>Describes the component interface (input/output ports).</p>

<p>Example:</p>
<pre><code>entity compteur is
  port (
    clk    : in  std_logic;
    reset  : in  std_logic;
    enable : in  std_logic;
    count  : out std_logic_vector(7 downto 0)
  );
end entity compteur;</code></pre>

<p><strong>Architecture</strong>:</p>
<p>Describes the behavior or internal structure of the component.</p>

<p>Example:</p>
<pre><code>architecture behavioral of compteur is
  signal count_internal : unsigned(7 downto 0);
begin
  process(clk, reset)
  begin
    if reset = '1' then
      count_internal &lt;= (others =&gt; '0');
    elsif rising_edge(clk) then
      if enable = '1' then
        count_internal &lt;= count_internal + 1;
      end if;
    end if;
  end process;

  count &lt;= std_logic_vector(count_internal);
end architecture behavioral;</code></pre>

<p><strong>Architecture types</strong>:</p>

<table>
<tr><th>Type</th><th>Description</th><th>Usage</th></tr>
<tr><td>Behavioral</td><td>Algorithmic description of behavior</td><td>High level, automatic synthesis</td></tr>
<tr><td>Dataflow</td><td>Concurrent assignments, equations</td><td>Combinational logic</td></tr>
<tr><td>Structural</td><td>Component instantiation</td><td>Hierarchy, block connection</td></tr>
</table>

<h3 class="section-title">3. VHDL data types</h3>

<p><strong>Standard types</strong>:</p>

<table>
<tr><th>Type</th><th>Description</th><th>Example</th></tr>
<tr><td>std_logic</td><td>Logic bit (9 values)</td><td>'0', '1', 'Z', 'X', etc.</td></tr>
<tr><td>std_logic_vector</td><td>Bit vector</td><td>"10110101"</td></tr>
<tr><td>integer</td><td>Integer</td><td>-2147483648 to 2147483647</td></tr>
<tr><td>unsigned</td><td>Unsigned integer</td><td>used for arithmetic calculations</td></tr>
<tr><td>signed</td><td>Signed integer</td><td>two's complement</td></tr>
</table>

<p><strong>std_logic values</strong>:</p>
<ul>
<li>'0': low level</li>
<li>'1': high level</li>
<li>'Z': high impedance (tri-state)</li>
<li>'X': unknown (uninitialized)</li>
<li>'-': don't care (synthesis)</li>
</ul>

<p><strong>Required libraries</strong>:</p>
<pre><code>library IEEE;
use IEEE.STD_LOGIC_1164.ALL;      -- std_logic, std_logic_vector
use IEEE.NUMERIC_STD.ALL;         -- unsigned, signed, conversion
use IEEE.STD_LOGIC_UNSIGNED.ALL;  -- operations on std_logic_vector (legacy)</code></pre>

<h3 class="section-title">4. Combinational logic</h3>

<p><strong>Concurrent assignment</strong>:</p>

<p>Assignments outside processes execute in parallel.</p>

<p>Examples:</p>
<pre><code>-- AND gate
y &lt;= a and b;

-- Multiplexer
y &lt;= a when sel = '0' else b;

-- 4-to-1 multiplexer
with sel select
  y &lt;= a when "00",
       b when "01",
       c when "10",
       d when others;</code></pre>

<p><strong>Combinational process</strong>:</p>

<p>To describe combinational logic within a process:</p>
<pre><code>process(a, b, c)  -- Sensitivity list: all signals read
begin
  if a = '1' then
    y &lt;= b;
  else
    y &lt;= c;
  end if;
end process;</code></pre>

<p><strong>Warning</strong>: If a read signal is not in the sensitivity list, the process does not update - simulation/synthesis mismatch.</p>

<h3 class="section-title">5. Sequential logic</h3>

<p><strong>D Flip-Flop</strong>:</p>

<p>Basic element of sequential logic. Stores a value on a clock edge.</p>

<pre><code>process(clk)
begin
  if rising_edge(clk) then  -- Rising edge
    q &lt;= d;
  end if;
end process;</code></pre>

<p><strong>With asynchronous reset</strong>:</p>
<pre><code>process(clk, reset)
begin
  if reset = '1' then       -- Reset has priority
    q &lt;= '0';
  elsif rising_edge(clk) then
    q &lt;= d;
  end if;
end process;</code></pre>

<p><strong>With synchronous reset</strong>:</p>
<pre><code>process(clk)
begin
  if rising_edge(clk) then
    if reset = '1' then
      q &lt;= '0';
    else
      q &lt;= d;
    end if;
  end if;
end process;</code></pre>

<p><strong>Golden rule</strong>:</p>
<ul>
<li>Asynchronous reset: in the process sensitivity list and tested first</li>
<li>Synchronous reset: inside the rising_edge test</li>
</ul>

<h3 class="section-title">6. Finite State Machines (FSM)</h3>

<p><strong>Definition</strong>:</p>

<p>An FSM (Finite State Machine) is a sequential circuit with a finite number of states. It changes state based on inputs and the current state.</p>

<p><strong>Types</strong>:</p>
<ul>
<li><strong>Moore</strong>: outputs depend only on the state</li>
<li><strong>Mealy</strong>: outputs depend on the state and the inputs</li>
</ul>

<p><strong>2-process structure</strong>:</p>

<p><strong>Process 1: State register (sequential)</strong></p>
<pre><code>process(clk, reset)
begin
  if reset = '1' then
    etat_courant &lt;= IDLE;
  elsif rising_edge(clk) then
    etat_courant &lt;= etat_suivant;
  end if;
end process;</code></pre>

<p><strong>Process 2: Transition logic (combinational)</strong></p>
<pre><code>process(etat_courant, entree)
begin
  case etat_courant is
    when IDLE =&gt;
      if entree = '1' then
        etat_suivant &lt;= TRAITEMENT;
      else
        etat_suivant &lt;= IDLE;
      end if;
      sortie &lt;= '0';

    when TRAITEMENT =&gt;
      if compteur_fini = '1' then
        etat_suivant &lt;= FIN;
      else
        etat_suivant &lt;= TRAITEMENT;
      end if;
      sortie &lt;= '1';

    when FIN =&gt;
      etat_suivant &lt;= IDLE;
      sortie &lt;= '0';

    when others =&gt;
      etat_suivant &lt;= IDLE;
      sortie &lt;= '0';
  end case;
end process;</code></pre>

<p><strong>State declaration</strong>:</p>
<pre><code>type etat_type is (IDLE, TRAITEMENT, FIN);
signal etat_courant, etat_suivant : etat_type;</code></pre>

<h3 class="section-title">7. Arithmetic and Logic Unit (ALU)</h3>

<p><strong>Principle</strong>:</p>

<p>The ALU performs the arithmetic operations (addition, subtraction) and logic operations (AND, OR, XOR) of a processor.</p>

<p><strong>Typical interface</strong>:</p>
<pre><code>entity ALU is
  port (
    A      : in  std_logic_vector(31 downto 0);  -- Operand A
    B      : in  std_logic_vector(31 downto 0);  -- Operand B
    OP     : in  std_logic_vector(3 downto 0);   -- Operation code
    Result : out std_logic_vector(31 downto 0);  -- Result
    Zero   : out std_logic;                      -- Zero flag
    Carry  : out std_logic                       -- Carry flag
  );
end entity ALU;</code></pre>

<p><strong>Common operations</strong>:</p>

<table>
<tr><th>OP Code</th><th>Operation</th><th>Description</th></tr>
<tr><td>0000</td><td>AND</td><td>Bitwise logical AND</td></tr>
<tr><td>0001</td><td>OR</td><td>Bitwise logical OR</td></tr>
<tr><td>0010</td><td>ADD</td><td>Addition</td></tr>
<tr><td>0110</td><td>SUB</td><td>Subtraction (A - B)</td></tr>
<tr><td>0111</td><td>SLT</td><td>Set if Less Than (A &lt; B)</td></tr>
<tr><td>1100</td><td>NOR</td><td>Logical NOR</td></tr>
</table>

<p><strong>Implementation</strong>:</p>
<pre><code>process(A, B, OP)
  variable temp : unsigned(32 downto 0);  -- 33 bits for carry
begin
  case OP is
    when "0000" =&gt;  -- AND
      Result &lt;= A and B;
      Carry &lt;= '0';

    when "0001" =&gt;  -- OR
      Result &lt;= A or B;
      Carry &lt;= '0';

    when "0010" =&gt;  -- ADD
      temp := ('0' &amp; unsigned(A)) + ('0' &amp; unsigned(B));
      Result &lt;= std_logic_vector(temp(31 downto 0));
      Carry &lt;= temp(32);

    when "0110" =&gt;  -- SUB
      temp := ('0' &amp; unsigned(A)) - ('0' &amp; unsigned(B));
      Result &lt;= std_logic_vector(temp(31 downto 0));
      Carry &lt;= temp(32);

    when others =&gt;
      Result &lt;= (others =&gt; '0');
      Carry &lt;= '0';
  end case;

  -- Zero Flag
  if Result = x"00000000" then
    Zero &lt;= '1';
  else
    Zero &lt;= '0';
  end if;
end process;</code></pre>

<h3 class="section-title">8. Register file</h3>

<p><strong>Principle</strong>:</p>

<p>A set of registers (typically 16 or 32) for temporarily storing data in a processor.</p>

<p><strong>Interface</strong>:</p>
<pre><code>entity RegisterFile is
  port (
    clk       : in  std_logic;
    reset     : in  std_logic;
    -- Read
    ReadAddr1 : in  std_logic_vector(4 downto 0);   -- Register 1 address
    ReadAddr2 : in  std_logic_vector(4 downto 0);   -- Register 2 address
    ReadData1 : out std_logic_vector(31 downto 0);  -- Register 1 data
    ReadData2 : out std_logic_vector(31 downto 0);  -- Register 2 data
    -- Write
    WriteEn   : in  std_logic;                      -- Write enable
    WriteAddr : in  std_logic_vector(4 downto 0);   -- Write address
    WriteData : in  std_logic_vector(31 downto 0)   -- Data to write
  );
end entity RegisterFile;</code></pre>

<p><strong>Implementation</strong>:</p>
<pre><code>architecture behavioral of RegisterFile is
  type reg_array is array (0 to 31) of std_logic_vector(31 downto 0);
  signal registers : reg_array;
begin
  -- Synchronous write
  process(clk, reset)
  begin
    if reset = '1' then
      registers &lt;= (others =&gt; (others =&gt; '0'));
    elsif rising_edge(clk) then
      if WriteEn = '1' and WriteAddr /= "00000" then  -- R0 always 0
        registers(to_integer(unsigned(WriteAddr))) &lt;= WriteData;
      end if;
    end if;
  end process;

  -- Asynchronous read
  ReadData1 &lt;= registers(to_integer(unsigned(ReadAddr1)));
  ReadData2 &lt;= registers(to_integer(unsigned(ReadAddr2)));
end architecture behavioral;</code></pre>

<p><strong>Special note</strong>:</p>
<p>Register R0 is often hardwired to zero (MIPS/RISC-V convention).</p>

<h3 class="section-title">9. Memories</h3>

<p><strong>ROM (Read-Only Memory)</strong>:</p>

<p>Used for storing the program (instructions).</p>

<pre><code>architecture behavioral of ROM is
  type rom_array is array (0 to 255) of std_logic_vector(31 downto 0);
  constant rom_data : rom_array := (
    x"00000000",  -- NOP
    x"20010005",  -- ADDI R1, R0, 5
    x"20020003",  -- ADDI R2, R0, 3
    x"00221820",  -- ADD R3, R1, R2
    -- ... other instructions
    others =&gt; x"00000000"
  );
begin
  process(clk)
  begin
    if rising_edge(clk) then
      data_out &lt;= rom_data(to_integer(unsigned(address)));
    end if;
  end process;
end architecture behavioral;</code></pre>

<p><strong>RAM (Random Access Memory)</strong>:</p>

<p>Used for storing data.</p>

<pre><code>architecture behavioral of RAM is
  type ram_array is array (0 to 1023) of std_logic_vector(31 downto 0);
  signal ram_data : ram_array := (others =&gt; (others =&gt; '0'));
begin
  process(clk)
  begin
    if rising_edge(clk) then
      if write_enable = '1' then
        ram_data(to_integer(unsigned(address))) &lt;= data_in;
      end if;
      data_out &lt;= ram_data(to_integer(unsigned(address)));
    end if;
  end process;
end architecture behavioral;</code></pre>

<p><strong>Using BRAM (Block RAM) on FPGA</strong>:</p>

<p>FPGAs have dedicated memory blocks (BRAM). Vivado automatically infers BRAM if the code follows certain patterns (as shown above).</p>

<h3 class="section-title">10. Simple processor</h3>

<p><strong>Architecture</strong>:</p>

<p>A minimal processor contains:</p>
<ul>
<li><strong>Datapath</strong>: ALU, registers, memories, multiplexers</li>
<li><strong>Control unit</strong>: FSM that generates control signals</li>
</ul>

<p><strong>Execution cycle</strong>:</p>

<ol>
<li><strong>Fetch</strong>: Read the instruction from memory (PC &rarr; Instr_Mem &rarr; IR)</li>
<li><strong>Decode</strong>: Decode the instruction (opcode, register, immediate fields)</li>
<li><strong>Execute</strong>: Execute the operation (ALU)</li>
<li><strong>Memory</strong>: Data memory access if needed (LOAD/STORE)</li>
<li><strong>Write Back</strong>: Write the result to the destination register</li>
</ol>

<p><strong>Control signals</strong>:</p>

<p>The control unit generates signals to drive the datapath:</p>
<ul>
<li>RegWrite: enable writing to the register file</li>
<li>ALUOp: ALU operation selection</li>
<li>MemRead, MemWrite: data memory read/write</li>
<li>MemToReg: data source selection for register write</li>
<li>Branch: enable conditional branching</li>
</ul>

<p><strong>Simplified example</strong>:</p>

<p>R-type instruction (register-register):</p>
<ul>
<li>Opcode determines it is an R-type instruction</li>
<li>Read two source registers (rs, rt)</li>
<li>ALU performs the operation (funct determines which one)</li>
<li>Write the result to the destination register (rd)</li>
</ul>

<h3 class="section-title">11. Testbench and simulation</h3>

<p><strong>Testbench</strong>:</p>

<p>A VHDL file with no ports (empty entity) that instantiates the circuit under test (UUT - Unit Under Test) and generates stimuli.</p>

<p><strong>Structure</strong>:</p>
<pre><code>entity testbench is
  -- No ports
end entity testbench;

architecture test of testbench is
  -- Test signal declarations
  signal clk : std_logic := '0';
  signal reset : std_logic := '1';
  signal input : std_logic_vector(7 downto 0);
  signal output : std_logic_vector(7 downto 0);

  constant CLK_PERIOD : time := 10 ns;
begin
  -- Instantiation of the component under test
  UUT: entity work.mon_circuit
    port map (
      clk =&gt; clk,
      reset =&gt; reset,
      input =&gt; input,
      output =&gt; output
    );

  -- Clock generation
  clk_process: process
  begin
    clk &lt;= '0';
    wait for CLK_PERIOD/2;
    clk &lt;= '1';
    wait for CLK_PERIOD/2;
  end process;

  -- Stimulus generation
  stim_process: process
  begin
    reset &lt;= '1';
    input &lt;= x"00";
    wait for 50 ns;

    reset &lt;= '0';
    wait for 10 ns;

    input &lt;= x"12";
    wait for 20 ns;

    input &lt;= x"34";
    wait for 20 ns;

    wait;  -- Stop simulation
  end process;
end architecture test;</code></pre>

<p><strong>Verification</strong>:</p>

<p>Use assertions for automatic checking:</p>
<pre><code>assert (output = x"46") report "Error: incorrect result" severity error;</code></pre>

<p><strong>Waveform</strong>:</p>

<p>.wcfg files in Vivado allow configuring which signals to display and how. Essential for visual debugging.</p>

<h3 class="section-title">12. Synthesis and implementation on FPGA</h3>

<p><strong>Steps</strong>:</p>

<p><strong>1. Synthesis</strong>:</p>
<ul>
<li>Conversion of VHDL code into a netlist (logic gates)</li>
<li>Logic optimization</li>
<li>Verification that the code is synthesizable</li>
</ul>

<p><strong>2. Implementation</strong>:</p>
<ul>
<li>Placement: assign logic resources to FPGA elements (LUT, FF)</li>
<li>Routing: connect elements through interconnections</li>
<li>Timing verification: ensure timing constraints are met</li>
</ul>

<p><strong>3. Bitstream generation</strong>:</p>
<ul>
<li>.bit file to be programmed into the FPGA</li>
</ul>

<p><strong>FPGA resources</strong>:</p>

<table>
<tr><th>Resource</th><th>Description</th></tr>
<tr><td>LUT (Look-Up Table)</td><td>Implements combinational logic (arbitrary function of N inputs)</td></tr>
<tr><td>FF (Flip-Flop)</td><td>D flip-flop for sequential logic</td></tr>
<tr><td>BRAM (Block RAM)</td><td>Dedicated memory blocks (18 Kb or 36 Kb)</td></tr>
<tr><td>DSP</td><td>Hardware multiplier/accumulator blocks</td></tr>
<tr><td>IO</td><td>Configurable input/output pins</td></tr>
</table>

<p><strong>Constraints</strong>:</p>

<p>.xdc file (Xilinx Design Constraints):</p>
<ul>
<li>Physical pin assignment</li>
<li>Clock definition (period, frequency)</li>
<li>Timing constraints</li>
</ul>

<p>Example:</p>
<pre><code># 100 MHz clock
create_clock -period 10.000 -name clk [get_ports clk]

# Pins
set_property PACKAGE_PIN W5 [get_ports clk]
set_property IOSTANDARD LVCMOS33 [get_ports clk]

set_property PACKAGE_PIN U16 [get_ports led[0]]
set_property IOSTANDARD LVCMOS33 [get_ports led[0]]</code></pre>

<hr/>

<h2>PART D - Reflective Analysis and Perspectives</h2>

<h3 class="section-title">Skills acquired</h3>

<p><strong>Hardware design</strong>:</p>
<p>Mastery of VHDL for describing synthesizable digital circuits. Ability to think in terms of hardware parallelism rather than software sequences.</p>

<p><strong>Processor architecture</strong>:</p>
<p>Deep understanding of a processor's internal workings: ALU, registers, memories, control unit, datapath.</p>

<p><strong>Professional tools</strong>:</p>
<p>Use of Xilinx Vivado, industry-standard tool for FPGA. Simulation, synthesis, implementation, timing analysis.</p>

<h3 class="section-title">Key takeaways</h3>

<p><strong>1. VHDL = hardware description, not programming</strong>:</p>
<p>VHDL code describes hardware that physically exists. Everything executes in parallel. A fundamental paradigm shift.</p>

<p><strong>2. Synthesizability</strong>:</p>
<p>Not all VHDL code can be synthesized into hardware. Avoid wait for (except in testbenches), infinite loops, division by variables, etc.</p>

<p><strong>3. Clock and synchronism</strong>:</p>
<p>Synchronous circuits (clocked) are more robust and predictable. Always use rising_edge(clk) to detect edges.</p>

<p><strong>4. Testbench = essential</strong>:</p>
<p>Simulation with testbench allows validating functionality before synthesis. Debugging is much easier than after implementation.</p>

<p><strong>5. Limited resources</strong>:</p>
<p>FPGAs have a finite number of LUTs, FFs, BRAMs. Optimization and resource sharing are important.</p>

<h3 class="section-title">Practical applications</h3>

<p><strong>Signal processing</strong>:</p>
<p>Implementation of high-performance digital filters (FIR, IIR), FFT, real-time image processing.</p>

<p><strong>Hardware accelerators</strong>:</p>
<p>Acceleration of intensive computations (cryptography, compression, AI) by offloading the processor.</p>

<p><strong>Critical embedded systems</strong>:</p>
<p>Aerospace, automotive, and space industries require deterministic and reliable circuits (hardwired logic on FPGA or ASIC).</p>

<p><strong>ASIC prototyping</strong>:</p>
<p>FPGAs are used to validate designs before ASIC fabrication (high cost, non-modifiable).</p>

<h3 class="section-title">Experience feedback</h3>

<p><strong>Learning curve</strong>:</p>
<p>VHDL is more difficult than traditional programming at first. It requires understanding the underlying hardware.</p>

<p><strong>Progressive projects</strong>:</p>
<p>The progression Buffer &rarr; ALU &rarr; Registers &rarr; Memories &rarr; Processor is pedagogically excellent. Each step adds complexity.</p>

<p><strong>Vivado: powerful but complex</strong>:</p>
<p>The tool is comprehensive but the interface can be intimidating. Synthesis/implementation times can be long.</p>

<p><strong>Visual debugging</strong>:</p>
<p>Waveforms are indispensable. Knowing how to identify critical signals to observe greatly facilitates debugging.</p>

<h3 class="section-title">Limitations and future directions</h3>

<p><strong>Module limitations</strong>:</p>
<ul>
<li>No physical implementation on an FPGA board (simulation only)</li>
<li>Very simplified processor (no pipeline, cache, etc.)</li>
<li>Timing and optimization aspects not thoroughly covered</li>
</ul>

<p><strong>Future directions</strong>:</p>
<ul>
<li><strong>Advanced processors</strong>: pipeline, branch prediction, cache</li>
<li><strong>Systems on chip (SoC)</strong>: processor + integrated peripherals</li>
<li><strong>High-Level Synthesis (HLS)</strong>: generate VHDL from C/C++</li>
<li><strong>Formal verification</strong>: assertions, model checking</li>
<li><strong>ASIC design</strong>: application-specific integrated circuit design</li>
</ul>

<h3 class="section-title">Technological evolution</h3>

<p><strong>Current trends</strong>:</p>

<p><strong>HLS (High-Level Synthesis)</strong>:</p>
<p>Tools like Vivado HLS or Vitis HLS allow writing in C/C++ and automatically generate VHDL/Verilog. This accelerates development.</p>

<p><strong>FPGA + AI</strong>:</p>
<p>Modern FPGAs (Versal, Zynq UltraScale+) integrate AI accelerators (DPU). Used for real-time neural network inference.</p>

<p><strong>Adaptive FPGAs (Versal)</strong>:</p>
<p>Hybrid architecture: FPGA + CPU + DSP + AI. Dynamic reconfiguration.</p>

<p><strong>Cloud FPGA</strong>:</p>
<p>AWS, Azure, Alibaba offer instances with FPGA for cloud acceleration.</p>

<h3 class="section-title">Tips for success</h3>

<p><strong>1. Think hardware</strong>:</p>
<p>Mentally visualize the gates, flip-flops, and multiplexers generated by your VHDL code.</p>

<p><strong>2. Simulate early and often</strong>:</p>
<p>Don't wait until all the code is written. Test each module independently.</p>

<p><strong>3. Comment well</strong>:</p>
<p>VHDL is verbose. Clear comments help when re-reading the code later.</p>

<p><strong>4. Follow conventions</strong>:</p>
<p>Explicit signal names (clk, reset, enable), consistent indentation.</p>

<p><strong>5. Use appropriate types</strong>:</p>
<p>unsigned/signed for arithmetic, std_logic_vector for generic data buses.</p>

<h3 class="section-title">Conclusion</h3>

<p>This module provides an excellent introduction to digital design with VHDL and FPGA. Building a complete processor, even a simple one, enables a deep understanding of computer architecture.</p>

<p><strong>Transferable skills</strong>:</p>
<ul>
<li>Parallel thinking and hardware design</li>
<li>Rigor in specification and verification</li>
<li>Mastery of professional tools (Vivado)</li>
<li>Understanding of processor architecture</li>
</ul>

<p><strong>Professional relevance</strong>:</p>
<p>FPGAs are used in many domains (telecommunications, defense, medical, automotive, finance). Demand for FPGA engineers remains strong.</p>

<p><strong>Key message</strong>:</p>
<p>VHDL and FPGAs offer total control over hardware, enabling performance and energy efficiency unattainable with software alone. Mastering these tools opens opportunities in high-performance systems.</p>

<p><strong>Recommendations</strong>:</p>
<ul>
<li>Practice on real FPGA boards (Basys, Arty, DE10-Nano)</li>
<li>Explore more complex projects (controllers, interfaces, DSP)</li>
<li>Learn Verilog as a complement (concurrent language)</li>
<li>Train in HLS to accelerate development</li>
<li>Study real processor architectures (open-source RISC-V)</li>
</ul>

<p><strong>Links to other courses</strong>:</p>
<ul>
<li><a href="./architecture-informatique-materielle.html">Hardware Computer Architecture - S5</a>: processor structure</li>
<li><a href="./fondements-electronique-numerique.html">Digital Electronics Fundamentals - S5</a>: logic gates</li>
<li><a href="./embedded-ia-iot.html">Embedded AI for IoT - S9</a>: hardware acceleration</li>
</ul>

<hr/>

<h2>BE Pipeline Project Illustrations</h2>

<div style="text-align: center; margin: 20px 0;">
  <img src="/img/BE_Pipeline/Pipeline_path.png" alt="Pipeline processor datapath" style="max-width: 700px; border: 1px solid #ddd; padding: 10px; border-radius: 8px;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Pipeline processor datapath</p>
</div>

<div style="text-align: center; margin: 20px 0;">
  <img src="/img/BE_Pipeline/ALU.png" alt="ALU schematic" style="max-width: 700px; border: 1px solid #ddd; padding: 10px; border-radius: 8px;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Arithmetic and Logic Unit (ALU) schematic</p>
</div>

<div style="text-align: center; margin: 20px 0;">
  <img src="/img/BE_Pipeline/Register_bench.png" alt="Register file" style="max-width: 700px; border: 1px solid #ddd; padding: 10px; border-radius: 8px;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Register file (Register Bench)</p>
</div>

<div style="text-align: center; margin: 20px 0;">
  <img src="/img/BE_Pipeline/Instruction_Memory.png" alt="Instruction memory" style="max-width: 700px; border: 1px solid #ddd; padding: 10px; border-radius: 8px;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Instruction memory</p>
</div>

<div style="text-align: center; margin: 20px 0;">
  <img src="/img/BE_Pipeline/Data_Memory.png" alt="Data memory" style="max-width: 700px; border: 1px solid #ddd; padding: 10px; border-radius: 8px;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Data memory</p>
</div>

<div style="text-align: center; margin: 20px 0;">
  <img src="/img/BE_Pipeline/ALEA.png" alt="Pipeline hazard management" style="max-width: 700px; border: 1px solid #ddd; padding: 10px; border-radius: 8px;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Pipeline hazard management</p>
</div>

<hr/>

<h2>Reports and Projects</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>VHDL Project Report</h4>
      <p>Design study report: pipeline processor design in VHDL, including ALU, register file, memories and hazard management.</p>
      <p style="text-align: center;">
        <a href="/file/reports/S7/Rapport_VHDL.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Download PDF report
        </a>
      </p>
    </div>
  </div>
</div>

<hr/>

<h2>Course Documents</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Complete VHDL Course</h4>
      <p>Complete VHDL course: syntax, processes, state machines, simulation and synthesis for FPGA.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S7/Archi-Numeriques-VHDL/cours-vhdl.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S7/Archi-Numeriques-VHDL/cours-vhdl.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>RISC Processor Project</h4>
      <p>Design study project brief: RISC microprocessor design in VHDL with ALU, register file and memory.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S7/Archi-Numeriques-VHDL/projet-risc.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S7/Archi-Numeriques-VHDL/projet-risc.pdf" target="_blank">Download</a></p>
    </div>
  </div>
</div>

<hr/>

<p><em>Course taken in 2023-2024 at INSA Toulouse, Department of Electrical and Computer Engineering.</em></p>

</div>

<div class="back-nav">
    <a href="./my-courses-2023-2024.html" data-i18n-html="back-courses-2023-2024">&larr; Retour aux Cours 2023-2024</a>
</div>

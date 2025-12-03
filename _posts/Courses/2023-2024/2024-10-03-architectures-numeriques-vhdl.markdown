---
layout: default
title: "Architectures Numériques Avancées VHDL - S7"
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
    <a href="./my-courses-2023-2024.html">← Retour aux Cours 2023-2024</a>
</div>

# 💾 Architectures Numériques Avancées VHDL - Semestre 7

**Année Universitaire** : 2023-2024  
**Semestre** : 7  
**Crédits** : 2.5 ECTS  
**Spécialité** : Conception Numérique et FPGA

---

## PART A - Présentation Générale du Module

<h3 class="section-title">Vue d'ensemble</h3>

Ce cours enseigne la conception de systèmes numériques complexes avec le langage VHDL (VHSIC Hardware Description Language) et leur implémentation sur FPGA. Il couvre la conception d'architectures numériques avancées : unité arithmétique et logique (ALU), bancs de registres, mémoires, et processeurs complets.

**Objectifs pédagogiques** :
- Maîtriser le langage VHDL pour la description matérielle
- Concevoir des circuits numériques synthétisables
- Implémenter des systèmes sur FPGA (Xilinx)
- Simuler et vérifier des designs avec testbenches
- Comprendre les machines à états finis (FSM)
- Concevoir un processeur simple complet

<h3 class="section-title">Position dans le cursus</h3>

Ce module s'appuie sur :
- **Fondements électronique numérique (S5)** : portes logiques, bascules
- **Logique séquentielle (S5)** : machines à états, compteurs
- **Architecture Informatique matérielle (S5)** : structure processeur

Il prépare à :
- **Systèmes embarqués** : accélérateurs matériels
- **Traitement du signal sur FPGA** : implémentation de filtres numériques
- **Conception ASIC** : circuits intégrés spécialisés
- **Systèmes temps réel** : logique câblée haute performance

---

## PART B - Expérience Personnelle et Contexte d'Apprentissage

<h3 class="section-title">Organisation et ressources</h3>

Le module était organisé en cours magistraux et bureau d'études pratique :

**Cours magistraux (16h)** :
- Syntaxe et structure VHDL
- Types de données et opérateurs
- Logique combinatoire et séquentielle
- Machines à états finis (FSM)
- Architectures de processeurs

**Bureau d'études (20h)** :
Projets de conception progressive avec Xilinx Vivado :
- Projet ALU : unité arithmétique et logique
- Projet registre : banc de registres
- Projet buffer : mémoire tampon
- Projet mémoire instruction : ROM pour code programme
- Projet mémoire donnée : RAM pour données
- Projet processeur : intégration complète

**Devoirs maison** :
- DM1 : ALU et testbench
- DM2 : Circuit numérique complexe

**Outils utilisés** :
- Xilinx Vivado Design Suite (synthèse, simulation, implémentation)
- FPGA cible : probablement Artix-7 ou Zynq
- Testbenches VHDL pour simulation
- Waveform viewer (fichiers .wcfg)

<h3 class="section-title">Structure des projets</h3>

Chaque projet Vivado contenait :
- **Sources** : fichiers VHDL (sources_1/new/)
- **Simulations** : testbenches (sim_1/)
- **Contraintes** : fichiers .xdc pour mapping des pins (constrs_1/)
- **Waveforms** : fichiers .wcfg pour visualisation des signaux
- **Synthèse et implémentation** : runs/synth_1/, runs/impl_1/

**Progression pédagogique** :

1. **Buffer** : Circuit simple (FIFO ou registre à décalage)
2. **ALU** : Opérations arithmétiques et logiques
3. **Registre** : Banc de registres avec lecture/écriture
4. **Mémoire instruction** : ROM pour stocker le programme
5. **Mémoire donnée** : RAM pour stocker les données
6. **Processeur** : Assemblage final (chemin de données + unité de contrôle)

<h3 class="section-title">Méthode de travail</h3>

**Phase 1 : Spécification** :
Définir l'interface (ports d'entrée/sortie) et le comportement attendu du circuit.

**Phase 2 : Code VHDL** :
Écrire le code dans Vivado, respecter les règles de synthétisabilité.

**Phase 3 : Testbench** :
Créer un testbench pour vérifier fonctionnellement le circuit par simulation.

**Phase 4 : Simulation** :
Lancer la simulation comportementale, observer les chronogrammes (waveforms), corriger les erreurs.

**Phase 5 : Synthèse** :
Vérifier que le code se synthétise sans erreurs, analyser l'utilisation des ressources (LUT, FF, BRAM).

**Phase 6 : Implémentation** (optionnel) :
Placer et router le design, vérifier le timing, programmer le FPGA.

<h3 class="section-title">Difficultés rencontrées</h3>

**Pensée parallèle** :
VHDL décrit du matériel où tout s'exécute en parallèle, contrairement à la programmation séquentielle. Comprendre que les process s'exécutent simultanément demande un changement de paradigme.

**Syntaxe stricte** :
VHDL est verbeux et typé fortement. Les erreurs de syntaxe ou de typage sont fréquentes au début.

**Timing et synchronisation** :
Gérer correctement les horloges, resets, et éviter les hazards (glitches) nécessite de la rigueur.

**Debugging** :
Sans printf ni débogueur, le debugging se fait via les chronogrammes. Savoir quels signaux observer est crucial.

---

## PART C - Aspects Techniques Détaillés

<h3 class="section-title">1. Introduction au VHDL</h3>

**VHDL = VHSIC Hardware Description Language**

VHSIC = Very High Speed Integrated Circuit

**Langage de description matérielle** :
- Décrit la structure et le comportement de circuits numériques
- Utilisé pour simulation et synthèse (génération de circuits réels)
- Standard IEEE (IEEE 1076)

**Différence programmation logicielle** :

| Aspect | Logiciel | Matériel (VHDL) |
|--------|----------|-----------------|
| Exécution | Séquentielle | Parallèle |
| Variables | Modifiées en séquence | Signaux qui évoluent dans le temps |
| Boucles | Itérations | Réplication de matériel |
| Ressources | Abstraites (mémoire virtuelle) | Physiques limitées (LUT, FF) |

<h3 class="section-title">2. Structure d'un fichier VHDL</h3>

**Entity (entité)** :
Décrit l'interface du composant (ports d'entrée/sortie).

Exemple :
```
entity compteur is
  port (
    clk    : in  std_logic;
    reset  : in  std_logic;
    enable : in  std_logic;
    count  : out std_logic_vector(7 downto 0)
  );
end entity compteur;
```

**Architecture** :
Décrit le comportement ou la structure interne du composant.

Exemple :
```
architecture behavioral of compteur is
  signal count_internal : unsigned(7 downto 0);
begin
  process(clk, reset)
  begin
    if reset = '1' then
      count_internal <= (others => '0');
    elsif rising_edge(clk) then
      if enable = '1' then
        count_internal <= count_internal + 1;
      end if;
    end if;
  end process;
  
  count <= std_logic_vector(count_internal);
end architecture behavioral;
```

**Types d'architectures** :

| Type | Description | Usage |
|------|-------------|-------|
| Behavioral | Description algorithmique du comportement | Haut niveau, synthèse automatique |
| Dataflow | Affectations concurrentes, équations | Logique combinatoire |
| Structural | Instanciation de composants | Hiérarchie, connexion de blocs |

<h3 class="section-title">3. Types de données VHDL</h3>

**Types standards** :

| Type | Description | Exemple |
|------|-------------|---------|
| std_logic | Bit logique (9 valeurs) | '0', '1', 'Z', 'X', etc. |
| std_logic_vector | Vecteur de bits | "10110101" |
| integer | Entier | -2147483648 à 2147483647 |
| unsigned | Entier non signé | utilisé pour calculs arithmétiques |
| signed | Entier signé | complément à 2 |

**Valeurs std_logic** :
- '0' : niveau bas
- '1' : niveau haut
- 'Z' : haute impédance (trois états)
- 'X' : inconnu (non initialisé)
- '-' : don't care (synthèse)

**Bibliothèques nécessaires** :
```
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;      -- std_logic, std_logic_vector
use IEEE.NUMERIC_STD.ALL;         -- unsigned, signed, conversion
use IEEE.STD_LOGIC_UNSIGNED.ALL;  -- opérations sur std_logic_vector (ancien)
```

<h3 class="section-title">4. Logique combinatoire</h3>

**Affectation concurrente** :

Les affectations en dehors des process s'exécutent en parallèle.

Exemples :
```
-- Porte AND
y <= a and b;

-- Multiplexeur
y <= a when sel = '0' else b;

-- Multiplexeur 4 vers 1
with sel select
  y <= a when "00",
       b when "01",
       c when "10",
       d when others;
```

**Process combinatoire** :

Pour décrire de la logique combinatoire dans un process :
```
process(a, b, c)  -- Liste de sensibilité : tous les signaux lus
begin
  if a = '1' then
    y <= b;
  else
    y <= c;
  end if;
end process;
```

**Attention** : Si un signal lu n'est pas dans la liste de sensibilité, le process ne se met pas à jour → différence simulation/synthèse.

<h3 class="section-title">5. Logique séquentielle</h3>

**Bascule D (D Flip-Flop)** :

Élément de base de la logique séquentielle. Mémorise une valeur sur un front d'horloge.

```
process(clk)
begin
  if rising_edge(clk) then  -- Front montant
    q <= d;
  end if;
end process;
```

**Avec reset asynchrone** :
```
process(clk, reset)
begin
  if reset = '1' then       -- Reset prioritaire
    q <= '0';
  elsif rising_edge(clk) then
    q <= d;
  end if;
end process;
```

**Avec reset synchrone** :
```
process(clk)
begin
  if rising_edge(clk) then
    if reset = '1' then
      q <= '0';
    else
      q <= d;
    end if;
  end if;
end process;
```

**Règle d'or** :
- Reset asynchrone : dans la sensibilité du process et testé en premier
- Reset synchrone : à l'intérieur du test de rising_edge

<h3 class="section-title">6. Machines à états finis (FSM)</h3>

**Définition** :

Une FSM (Finite State Machine) est un circuit séquentiel avec un nombre fini d'états. Elle change d'état selon les entrées et l'état courant.

**Types** :
- **Moore** : sorties dépendent seulement de l'état
- **Mealy** : sorties dépendent de l'état et des entrées

**Structure à 2 process** :

**Process 1 : Registre d'état (séquentiel)**
```
process(clk, reset)
begin
  if reset = '1' then
    etat_courant <= IDLE;
  elsif rising_edge(clk) then
    etat_courant <= etat_suivant;
  end if;
end process;
```

**Process 2 : Logique de transition (combinatoire)**
```
process(etat_courant, entree)
begin
  case etat_courant is
    when IDLE =>
      if entree = '1' then
        etat_suivant <= TRAITEMENT;
      else
        etat_suivant <= IDLE;
      end if;
      sortie <= '0';
      
    when TRAITEMENT =>
      if compteur_fini = '1' then
        etat_suivant <= FIN;
      else
        etat_suivant <= TRAITEMENT;
      end if;
      sortie <= '1';
      
    when FIN =>
      etat_suivant <= IDLE;
      sortie <= '0';
      
    when others =>
      etat_suivant <= IDLE;
      sortie <= '0';
  end case;
end process;
```

**Déclaration des états** :
```
type etat_type is (IDLE, TRAITEMENT, FIN);
signal etat_courant, etat_suivant : etat_type;
```

<h3 class="section-title">7. Unité Arithmétique et Logique (ALU)</h3>

**Principe** :

L'ALU effectue les opérations arithmétiques (addition, soustraction) et logiques (AND, OR, XOR) d'un processeur.

**Interface typique** :
```
entity ALU is
  port (
    A      : in  std_logic_vector(31 downto 0);  -- Opérande A
    B      : in  std_logic_vector(31 downto 0);  -- Opérande B
    OP     : in  std_logic_vector(3 downto 0);   -- Code opération
    Result : out std_logic_vector(31 downto 0);  -- Résultat
    Zero   : out std_logic;                      -- Flag zéro
    Carry  : out std_logic                       -- Flag retenue
  );
end entity ALU;
```

**Opérations courantes** :

| Code OP | Opération | Description |
|---------|-----------|-------------|
| 0000 | AND | ET logique bit à bit |
| 0001 | OR | OU logique bit à bit |
| 0010 | ADD | Addition |
| 0110 | SUB | Soustraction (A - B) |
| 0111 | SLT | Set if Less Than (A < B) |
| 1100 | NOR | NON-OU logique |

**Implémentation** :
```
process(A, B, OP)
  variable temp : unsigned(32 downto 0);  -- 33 bits pour la retenue
begin
  case OP is
    when "0000" =>  -- AND
      Result <= A and B;
      Carry <= '0';
      
    when "0001" =>  -- OR
      Result <= A or B;
      Carry <= '0';
      
    when "0010" =>  -- ADD
      temp := ('0' & unsigned(A)) + ('0' & unsigned(B));
      Result <= std_logic_vector(temp(31 downto 0));
      Carry <= temp(32);
      
    when "0110" =>  -- SUB
      temp := ('0' & unsigned(A)) - ('0' & unsigned(B));
      Result <= std_logic_vector(temp(31 downto 0));
      Carry <= temp(32);
      
    when others =>
      Result <= (others => '0');
      Carry <= '0';
  end case;
  
  -- Flag Zero
  if Result = x"00000000" then
    Zero <= '1';
  else
    Zero <= '0';
  end if;
end process;
```

<h3 class="section-title">8. Banc de registres</h3>

**Principe** :

Ensemble de registres (16 ou 32 typiquement) pour stocker temporairement des données dans un processeur.

**Interface** :
```
entity RegisterFile is
  port (
    clk       : in  std_logic;
    reset     : in  std_logic;
    -- Lecture
    ReadAddr1 : in  std_logic_vector(4 downto 0);   -- Adresse registre 1
    ReadAddr2 : in  std_logic_vector(4 downto 0);   -- Adresse registre 2
    ReadData1 : out std_logic_vector(31 downto 0);  -- Donnée registre 1
    ReadData2 : out std_logic_vector(31 downto 0);  -- Donnée registre 2
    -- Écriture
    WriteEn   : in  std_logic;                      -- Autorisation écriture
    WriteAddr : in  std_logic_vector(4 downto 0);   -- Adresse écriture
    WriteData : in  std_logic_vector(31 downto 0)   -- Donnée à écrire
  );
end entity RegisterFile;
```

**Implémentation** :
```
architecture behavioral of RegisterFile is
  type reg_array is array (0 to 31) of std_logic_vector(31 downto 0);
  signal registers : reg_array;
begin
  -- Écriture synchrone
  process(clk, reset)
  begin
    if reset = '1' then
      registers <= (others => (others => '0'));
    elsif rising_edge(clk) then
      if WriteEn = '1' and WriteAddr /= "00000" then  -- R0 toujours à 0
        registers(to_integer(unsigned(WriteAddr))) <= WriteData;
      end if;
    end if;
  end process;
  
  -- Lecture asynchrone
  ReadData1 <= registers(to_integer(unsigned(ReadAddr1)));
  ReadData2 <= registers(to_integer(unsigned(ReadAddr2)));
end architecture behavioral;
```

**Particularité** :
Le registre R0 est souvent câblé à zéro (convention MIPS/RISC-V).

<h3 class="section-title">9. Mémoires</h3>

**ROM (Read-Only Memory)** :

Utilisée pour stocker le programme (instructions).

```
architecture behavioral of ROM is
  type rom_array is array (0 to 255) of std_logic_vector(31 downto 0);
  constant rom_data : rom_array := (
    x"00000000",  -- NOP
    x"20010005",  -- ADDI R1, R0, 5
    x"20020003",  -- ADDI R2, R0, 3
    x"00221820",  -- ADD R3, R1, R2
    -- ... autres instructions
    others => x"00000000"
  );
begin
  process(clk)
  begin
    if rising_edge(clk) then
      data_out <= rom_data(to_integer(unsigned(address)));
    end if;
  end process;
end architecture behavioral;
```

**RAM (Random Access Memory)** :

Utilisée pour stocker les données.

```
architecture behavioral of RAM is
  type ram_array is array (0 to 1023) of std_logic_vector(31 downto 0);
  signal ram_data : ram_array := (others => (others => '0'));
begin
  process(clk)
  begin
    if rising_edge(clk) then
      if write_enable = '1' then
        ram_data(to_integer(unsigned(address))) <= data_in;
      end if;
      data_out <= ram_data(to_integer(unsigned(address)));
    end if;
  end process;
end architecture behavioral;
```

**Utilisation des BRAM (Block RAM) sur FPGA** :

Les FPGA possèdent des blocs mémoire dédiés (BRAM). Vivado infère automatiquement des BRAM si le code suit certains modèles (comme ci-dessus).

<h3 class="section-title">10. Processeur simple</h3>

**Architecture** :

Un processeur minimal contient :
- **Chemin de données (Datapath)** : ALU, registres, mémoires, multiplexeurs
- **Unité de contrôle** : FSM qui génère les signaux de contrôle

**Cycle d'exécution** :

1. **Fetch** : Lire l'instruction en mémoire (PC → Mem_Instr → IR)
2. **Decode** : Décoder l'instruction (champs opcode, registres, immédiat)
3. **Execute** : Exécuter l'opération (ALU)
4. **Memory** : Accès mémoire données si nécessaire (LOAD/STORE)
5. **Write Back** : Écrire le résultat dans le registre destination

**Signaux de contrôle** :

L'unité de contrôle génère des signaux pour piloter le datapath :
- RegWrite : autoriser écriture dans le banc de registres
- ALUOp : sélection opération ALU
- MemRead, MemWrite : lecture/écriture mémoire données
- MemToReg : sélection source donnée à écrire dans registre
- Branch : autoriser branchement conditionnel

**Exemple simplifié** :

Type d'instruction R (registre-registre) :
- Opcode détermine que c'est une instruction R
- Lire deux registres sources (rs, rt)
- ALU effectue l'opération (funct détermine laquelle)
- Écrire le résultat dans registre destination (rd)

<h3 class="section-title">11. Testbench et simulation</h3>

**Testbench** :

Fichier VHDL sans ports (entity vide) qui instancie le circuit à tester (UUT - Unit Under Test) et génère des stimuli.

**Structure** :
```
entity testbench is
  -- Pas de ports
end entity testbench;

architecture test of testbench is
  -- Déclaration des signaux de test
  signal clk : std_logic := '0';
  signal reset : std_logic := '1';
  signal input : std_logic_vector(7 downto 0);
  signal output : std_logic_vector(7 downto 0);
  
  constant CLK_PERIOD : time := 10 ns;
begin
  -- Instanciation du composant à tester
  UUT: entity work.mon_circuit
    port map (
      clk => clk,
      reset => reset,
      input => input,
      output => output
    );
  
  -- Génération de l'horloge
  clk_process: process
  begin
    clk <= '0';
    wait for CLK_PERIOD/2;
    clk <= '1';
    wait for CLK_PERIOD/2;
  end process;
  
  -- Génération des stimuli
  stim_process: process
  begin
    reset <= '1';
    input <= x"00";
    wait for 50 ns;
    
    reset <= '0';
    wait for 10 ns;
    
    input <= x"12";
    wait for 20 ns;
    
    input <= x"34";
    wait for 20 ns;
    
    wait;  -- Arrêt de la simulation
  end process;
end architecture test;
```

**Vérifications** :

Utiliser des assertions pour vérifier automatiquement :
```
assert (output = x"46") report "Erreur : résultat incorrect" severity error;
```

**Waveform (chronogramme)** :

Fichiers .wcfg dans Vivado permettent de configurer quels signaux afficher et comment. Essentiels pour le debugging visuel.

<h3 class="section-title">12. Synthèse et implémentation sur FPGA</h3>

**Étapes** :

1. **Synthèse (Synthesis)** :
   - Conversion du code VHDL en netlist (portes logiques)
   - Optimisation logique
   - Vérification que le code est synthétisable

2. **Implémentation** :
   - Placement : affecter les ressources logiques aux éléments du FPGA (LUT, FF)
   - Routage : connecter les éléments via les interconnexions
   - Vérification timing : s'assurer que les contraintes temporelles sont respectées

3. **Génération du bitstream** :
   - Fichier .bit à programmer dans le FPGA

**Ressources FPGA** :

| Ressource | Description |
|-----------|-------------|
| LUT (Look-Up Table) | Implémente logique combinatoire (fonction quelconque de N entrées) |
| FF (Flip-Flop) | Bascule D pour logique séquentielle |
| BRAM (Block RAM) | Blocs mémoire dédiés (18 Kb ou 36 Kb) |
| DSP | Blocs multiplicateurs/accumulateurs matériels |
| IO | Broches d'entrée/sortie configurables |

**Contraintes** :

Fichier .xdc (Xilinx Design Constraints) :
- Affectation des pins physiques
- Définition des horloges (période, fréquence)
- Contraintes de timing

Exemple :
```
# Horloge 100 MHz
create_clock -period 10.000 -name clk [get_ports clk]

# Pins
set_property PACKAGE_PIN W5 [get_ports clk]
set_property IOSTANDARD LVCMOS33 [get_ports clk]

set_property PACKAGE_PIN U16 [get_ports led[0]]
set_property IOSTANDARD LVCMOS33 [get_ports led[0]]
```

---

## PART D - Analyse Réflexive et Perspectives

<h3 class="section-title">Compétences acquises</h3>

**Conception matérielle** :
Maîtrise du VHDL pour décrire des circuits numériques synthétisables. Capacité à penser en termes de parallélisme matériel plutôt que séquence logicielle.

**Architecture de processeur** :
Compréhension profonde du fonctionnement interne d'un processeur : ALU, registres, mémoires, unité de contrôle, chemin de données.

**Outils professionnels** :
Utilisation de Xilinx Vivado, outil standard de l'industrie pour FPGA. Simulation, synthèse, implémentation, analyse de timing.

<h3 class="section-title">Points clés à retenir</h3>

**1. VHDL = description matérielle, pas programmation** :
Le code VHDL décrit du matériel qui existe physiquement. Tout s'exécute en parallèle. Changement de paradigme fondamental.

**2. Synthétisabilité** :
Tout le code VHDL ne peut pas être synthétisé en matériel. Éviter wait for (sauf dans testbenches), boucles infinies, division par variables, etc.

**3. Horloge et synchronisme** :
Les circuits synchrones (cadencés par horloge) sont plus robustes et prévisibles. Toujours utiliser rising_edge(clk) pour détecter les fronts.

**4. Testbench = essentiel** :
La simulation avec testbench permet de valider le fonctionnement avant synthèse. Debug beaucoup plus facile qu'après implémentation.

**5. Ressources limitées** :
Les FPGA ont un nombre fini de LUT, FF, BRAM. Importance de l'optimisation et du partage de ressources.

<h3 class="section-title">Applications pratiques</h3>

**Traitement du signal** :
Implémentation de filtres numériques haute performance (FIR, IIR), FFT, traitement d'image temps réel.

**Accélérateurs matériels** :
Accélération de calculs intensifs (cryptographie, compression, IA) en déchargeant le processeur.

**Systèmes embarqués critiques** :
Aéronautique, automobile, spatial nécessitent des circuits déterministes et fiables (logique câblée sur FPGA ou ASIC).

**Prototypage ASIC** :
Les FPGA servent à valider des designs avant fabrication d'ASIC (coût élevé, non modifiable).

<h3 class="section-title">Retour d'expérience</h3>

**Courbe d'apprentissage** :
VHDL est plus difficile que la programmation classique au début. Nécessite de comprendre le matériel sous-jacent.

**Projets progressifs** :
La progression Buffer → ALU → Registres → Mémoires → Processeur est pédagogiquement excellente. Chaque étape ajoute de la complexité.

**Vivado puissant mais complexe** :
L'outil est complet mais l'interface peut être intimidante. Temps de synthèse/implémentation parfois long.

**Debugging visuel** :
Les waveforms (chronogrammes) sont indispensables. Savoir identifier les signaux critiques à observer facilite grandement le debugging.

<h3 class="section-title">Limites et ouvertures</h3>

**Limites du module** :
- Pas d'implémentation physique sur carte FPGA (simulation seulement)
- Processeur très simplifié (pas de pipeline, cache, etc.)
- Aspects timing et optimisation peu approfondis

**Ouvertures vers** :
- **Processeurs avancés** : pipeline, prédiction de branchement, cache
- **Systèmes sur puce (SoC)** : processeur + périphériques intégrés
- **High-Level Synthesis (HLS)** : générer VHDL depuis C/C++
- **Vérification formelle** : assertions, model checking
- **ASIC design** : conception de circuits intégrés application spécifique

<h3 class="section-title">Évolution technologique</h3>

**Tendances actuelles** :

**HLS (High-Level Synthesis)** :
Outils comme Vivado HLS ou Vitis HLS permettent d'écrire en C/C++ et génèrent automatiquement du VHDL/Verilog. Accélère le développement.

**FPGA + IA** :
Les FPGA modernes (Versal, Zynq UltraScale+) intègrent des accélérateurs IA (DPU). Utilisés pour inférence de réseaux de neurones temps réel.

**FPGA adaptatives (Versal)** :
Architecture hybride : FPGA + CPU + DSP + IA. Reconfiguration dynamique.

**Cloud FPGA** :
AWS, Azure, Alibaba proposent des instances avec FPGA pour accélération dans le cloud.

<h3 class="section-title">Conseils pour réussir</h3>

**1. Penser matériel** :
Visualiser mentalement les portes, bascules, multiplexeurs générés par votre code VHDL.

**2. Simuler tôt et souvent** :
Ne pas attendre d'avoir écrit tout le code. Tester chaque module indépendamment.

**3. Bien commenter** :
VHDL est verbeux. Des commentaires clairs aident à relire le code plus tard.

**4. Respecter les conventions** :
Noms de signaux explicites (clk, reset, enable), indentation cohérente.

**5. Utiliser les types appropriés** :
unsigned/signed pour arithmétique, std_logic_vector pour bus de données génériques.

<h3 class="section-title">Conclusion</h3>

Ce module fournit une excellente introduction à la conception numérique avec VHDL et FPGA. La réalisation d'un processeur complet, même simple, permet de comprendre en profondeur l'architecture des ordinateurs.

**Compétences transférables** :
- Pensée parallèle et conception matérielle
- Rigueur dans la spécification et la vérification
- Maîtrise d'outils professionnels (Vivado)
- Compréhension de l'architecture des processeurs

**Pertinence professionnelle** :
Les FPGA sont utilisés dans de nombreux domaines (télécommunications, défense, médical, automobile, finance). La demande en ingénieurs FPGA reste forte.

**Message principal** :
VHDL et les FPGA offrent un contrôle total sur le matériel, permettant des performances et une efficacité énergétique inatteignables avec du logiciel seul. La maîtrise de ces outils ouvre des opportunités dans les systèmes haute performance.

**Recommandations** :
- Pratiquer sur des cartes FPGA réelles (Basys, Arty, DE10-Nano)
- Explorer des projets plus complexes (contrôleurs, interfaces, DSP)
- Apprendre Verilog en complément (langage concurrent)
- Se former au HLS pour accélérer le développement
- Étudier l'architecture de processeurs réels (RISC-V open-source)

**Liens avec les autres cours** :
- [Architecture Informatique matérielle - S5](./architecture-informatique-materielle.html) : structure processeur
- [Fondements électronique numérique - S5](./fondements-electronique-numerique.html) : portes logiques
- [Embedded IA for IoT - S9](./embedded-ia-for-iot.html) : accélération matérielle

---

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

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>📖 Cours VHDL Complet</h4>
      <p>Cours complet de VHDL : syntaxe, processus, machines à états, simulation et synthèse pour FPGA.</p>
      <embed src="/cours-pdf/S7/Archi-Numeriques-VHDL/cours-vhdl.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Archi-Numeriques-VHDL/cours-vhdl.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>📖 Projet Processeur RISC</h4>
      <p>Sujet du projet BE : conception d'un microprocesseur RISC en VHDL avec ALU, banc de registres et mémoire.</p>
      <embed src="/cours-pdf/S7/Archi-Numeriques-VHDL/projet-risc.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Archi-Numeriques-VHDL/projet-risc.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
  </div>
</div>

---

*Cours suivi en 2023-2024 à l'INSA Toulouse, Département Génie Électrique et Informatique.*

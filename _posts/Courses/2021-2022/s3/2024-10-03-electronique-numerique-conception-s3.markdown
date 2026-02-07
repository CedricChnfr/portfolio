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
  <a href="./my-courses-2021-2022.html">&larr; Retour a Mes Cours 2021-2022</a>
</div>

# Électronique Numérique et Conception (ENC) - Semestre 3

**Annee**: 2021-2022 | **Semestre**: 3 | **Type**: Technique

---

## PART A - Présentation Générale du Cours

### Contexte et objectifs

L'ENC (Électronique Numérique et Conception) au S3 ENOC approfondit la conception de systèmes numériques programmables (FPGA/CPLD) en VHDL. Deux projets majeurs : développement de bibliothèque de composants IP et conception complète d'une platine électronique intégrant un FPGA.

**Objectifs :**
- Programmation VHDL avancée (FSM, pipeline, mémoires)
- Synthèse et implémentation sur FPGA (Quartus, Vivado)
- Conception de platines numériques professionnelles
- Validation par simulation (ModelSim) et tests matériels

### Prérequis
- VHDL de base (S1 SIN)
- Logique séquentielle
- Conception PCB

---

## PART B: EXPÉRIENCE, CONTEXTE ET FONCTION

### Module 1 : VHDL avancé

**Structures algorithmiques :**
- Processus synchrones (rising_edge)
- FSM : Moore (sorties = f(état)), Mealy (sorties = f(état, entrées))
- Boucles FOR/WHILE
- Architectures structurelles (component instantiation)

**Blocs réutilisables :**
- Compteurs (up/down, modulo N, avec load/enable)
- Registres à décalage (SIPO, PISO, barrel shifter)
- Diviseurs de fréquence
- PWM à résolution variable
- FIFO, RAM/ROM

**Interfaces de communication :**
- UART (Tx/Rx, baud rate configurable)
- SPI (master/slave, modes 0-3)
- I2C (master, arbitrage)
- VGA (timing 640×480, palette couleurs)

### Module 2 : FPGA/CPLD

**Architecture FPGA (ex: Cyclone IV, Spartan-6) :**
- Logic Elements (LUT + FF)
- Block RAM, DSP blocks
- PLL (génération horloges)
- I/O programmables (standards : LVTTL, LVCMOS, LVDS)

**CPLD vs FPGA :**
- CPLD : non-volatile, démarrage rapide, capacité limitée
- FPGA : volatile (Flash SPI config), haute densité, flexible

**Outils de conception :**
- Quartus Prime (Intel/Altera)
- Vivado (Xilinx)
- Synthèse → Placement & Routage → Bitstream
- Contraintes timing (SDC) et pin assignment

### Module 3 : Simulation et validation

**Testbench VHDL :**
```vhdl
entity tb_uart is end;
architecture behavior of tb_uart is
  signal clk, rst, tx_start : std_logic;
  signal tx_data : std_logic_vector(7 downto 0);
begin
  uut: entity work.uart_tx port map(...);
  
  clk_process: process
  begin
    clk <= '0'; wait for 10 ns;
    clk <= '1'; wait for 10 ns;
  end process;
  
  stimulus: process
  begin
    rst <= '1'; wait for 100 ns;
    rst <= '0';
    tx_data <= X"A5";
    tx_start <= '1'; wait for 20 ns;
    tx_start <= '0';
    wait;
  end process;
end;
```

**Simulation :**
- ModelSim : waveform, assertions
- Simulation fonctionnelle (pré-synthèse)
- Simulation temporelle (post-routage, délais réels)

---

## PART C: ASPECTS TECHNIQUES

### Projet Composants VHDL

**Bibliothèque IP à développer :**
1. UART configurable (baud rate générique)
2. SPI master/slave
3. I2C master
4. Contrôleur VGA (synchronisation H/V, pixel pipeline)
5. Contrôleur LCD HD44780
6. Interface PS/2 clavier

**Livrables :**
- Code VHDL commenté
- Testbench complet
- Rapport simulation (chronogrammes)
- Documentation d'utilisation

### Projet Platine FPGA

**Architecture système :**
- FPGA Cyclone IV EP4CE15 ou Spartan-6 LX9
- Configuration : Flash SPI + JTAG
- Alimentation : 3.3V I/O, 1.2V core (régulateurs LDO)
- Périphériques : LEDs, switches, UART-USB (FT232), extension GPIO

**Schéma électrique (KiCad/Altium) :**
- FPGA + découplage intensif (100nF proches + 10µF)
- Oscillateur 50 MHz (GCLK)
- Configuration : EPCS4 (Flash SPI 4 Mbit)
- Connecteur JTAG 10 pins
- USB-UART (FT232RL ou CH340)
- Connecteurs extension (compatible Arduino/Pmod)

**PCB 4 couches :**
- L1 : Signaux Top
- L2 : GND plane
- L3 : 3.3V / 1.2V power planes
- L4 : Signaux Bottom
- Via stitching GND (espacement <λ/10 à fmax)
- Routage différentiel si LVDS

**Programmation et test :**
- Chargement bitstream JTAG
- Configuration Flash (boot automatique)
- Tests unitaires (LEDs, UART loopback)
- Application finale (ex: oscilloscope logique USB)

---

## PART D: ANALYSE ET RÉFLEXION

### Évaluation
- Projet composants VHDL (35%) : code, simulations, documentation
- Projet platine FPGA (40%) : schéma, PCB, programmation, démo
- Contrôles (15%)
- Rapport technique (10%)

### Compétences développées
- VHDL avancé et réutilisable
- Synthèse FPGA (timing, ressources)
- Conception platines numériques professionnelles
- Validation simulation + matérielle
- Gestion projets électroniques complexes

### Débouchés
- Ingénieur FPGA (traitement signal, vision, crypto)
- Concepteur systèmes embarqués numériques
- Architecte hardware (ASIC, prototypage FPGA)

## 📚 Contenu du cours

### VHDL avancé

#### Structures de base
- Entity et Architecture
- Signaux, variables, constantes
- Types de données (std_logic, integer, etc.)
- Opérateurs logiques et arithmétiques
- Assignations concurrentes et séquentielles

#### Structures algorithmiques
**Processus (process) :**
- Sensibility list
- Exécution séquentielle
- Variables locales
- Wait statements

**Conditions :**
- IF-THEN-ELSE
- CASE-WHEN
- WITH-SELECT-WHEN

**Boucles :**
- FOR loops
- WHILE loops
- LOOP-EXIT

#### Conception structurelle
- Component declaration
- Component instantiation
- Port mapping
- Generic parameters
- Configuration

#### Machines à états (FSM)
**Moore :**
- Sorties dépendent de l'état
- 2 ou 3 processus
- Stabilité

**Mealy :**
- Sorties dépendent état + entrées
- Plus réactif
- Peut être instable

**Encodage :**
- Binary
- One-hot
- Gray code

### Architectures numériques

#### Blocs de base

**Compteurs :**
- Binaires, décimaux
- Up, down, up/down
- Modulo N
- Avec enable, load, clear

**Registres :**
- Registres simples
- Registres à décalage (shift)
- PISO, SIPO, PIPO
- Barrel shifter

**Diviseurs de fréquence :**
- Division entière
- Division fractionnaire
- Génération d'horloges

**Générateurs PWM :**
- Résolution variable
- Fréquence ajustable
- Rapport cyclique contrôlable

#### Blocs arithmétiques

**Additionneurs :**
- Half-adder, full-adder
- Ripple-carry
- Carry look-ahead
- Signé/non signé

**Multiplieurs :**
- Shift-and-add
- Booth algorithm
- Pipeline
- DSP blocks

**ALU (Arithmetic Logic Unit) :**
- Opérations arithmétiques
- Opérations logiques
- Shifter
- Flags (Z, N, C, V)

#### Mémoires

**RAM :**
- Single-port, dual-port
- Block RAM (BRAM)
- Distributed RAM
- FIFO

**ROM :**
- Initialization
- Look-up tables (LUT)
- Constantes

### FPGA et CPLD

#### Architecture FPGA
- Logic Elements (LE) / Slices
- Look-Up Tables (LUT)
- Flip-flops
- Block RAM
- DSP blocks
- I/O blocks
- Clock management (PLL, DLL)

#### Familles de FPGA
**Xilinx :**
- Spartan (low-cost)
- Artix, Kintex, Virtex
- Zynq (ARM + FPGA)

**Intel/Altera :**
- Cyclone (entry-level)
- MAX 10 (CPLD-like)
- Arria, Stratix

#### CPLD vs FPGA
**CPLD :**
- Non-volatile
- Démarrage rapide
- Architecture simple
- Capacité limitée

**FPGA :**
- Volatile (configuration externe)
- Haute capacité
- Flexible
- DSP et mémoire intégrés

### Outils de conception

#### Synthèse
- Analyse syntaxique
- Optimisation
- Technology mapping
- Génération netlist

#### Implémentation
- Placement (Placer)
- Routage (Router)
- Contraintes de timing
- Utilisation des ressources

#### Simulation
**Fonctionnelle :**
- Comportement logique
- Pas de timing
- Rapide

**Temporelle (post-route) :**
- Délais réels
- Setup/hold times
- Critical path
- Précis

#### Contraintes

**Timing :**
- Fréquences d'horloge
- Contraintes I/O
- Chemins critiques
- False paths

**Placement :**
- LOC (location constraints)
- Groupes de signaux
- Floorplanning

**I/O :**
- Standards (LVTTL, LVCMOS, LVDS)
- Drive strength
- Slew rate
- Pull-up/down

## 🛠️ Projets pratiques

### Projet Composants VHDL

#### Objectif
Développement de bibliothèque de composants réutilisables

**Composants à réaliser :**
- UART (transmission série)
- SPI master/slave
- I2C master
- Contrôleur VGA
- Contrôleur LCD
- Interface PS/2 (clavier)

**Livrables :**
- Code VHDL commenté
- Testbench
- Rapport de simulation
- Documentation technique

### Projet Platine avec FPGA

#### Description
Conception complète d'une carte avec FPGA/CPLD

**Spécifications typiques :**
- FPGA/CPLD (Cyclone, Spartan)
- Configuration (JTAG, Active Serial)
- Alimentation (3.3V, 1.2V core)
- I/O (LEDs, boutons, switches)
- Interfaces (UART, USB-UART)
- Extension (connecteurs)

**Étapes :**
1. Choix du composant
2. Schématique complet
3. PCB multicouche (4 ou 6)
4. Fabrication
5. Assemblage et test
6. Programmation et validation

#### Considérations techniques

**Alimentation :**
- Séquencement (VCCINT avant VCCIO)
- Découplage intensif
- Filtrage
- Supervision (Power-On Reset)

**Configuration :**
- JTAG obligatoire
- Flash SPI (configuration boot)
- Mémoire suffisante
- Schéma de configuration

**Signaux d'horloge :**
- Oscillateur adapté
- Entrée GCLK
- Qualité du signal
- Distribution

**I/O :**
- Protection ESD
- Résistances séries
- Impédance contrôlée si nécessaire
- Banques d'I/O (voltage)

## 💻 Outils utilisés

### Environnements de développement
- **Quartus Prime** : Intel/Altera FPGA
- **Vivado** : Xilinx FPGA
- **ISE** : Xilinx (legacy)
- **Libero SoC** : Microsemi/Microchip

### Simulation
- **ModelSim** : Standard industrie
- **GHDL** : Open source
- **Vivado Simulator** : Intégré Xilinx
- **Questa** : Mentor Graphics

### Conception PCB
- **Altium Designer**
- **KiCad**
- **Eagle**
- **OrCAD**

## 📊 Évaluation

- Projet composants VHDL (35%)
- Projet platine FPGA (40%)
- Contrôles de connaissances (15%)
- Rapport et documentation (10%)

## 🔗 Liens avec d'autres cours

- **ER** : Intégration FPGA dans système
- **IE** : Communication FPGA-MCU
- **Automatisme** : Logique séquentielle
- **SE** : Traitement numérique signal

## 📐 Exemple d'architecture VHDL

### Diviseur de fréquence
```vhdl
entity freq_divider is
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
            counter <= 0;
            clk_temp <= '0';
        elsif rising_edge(clk_in) then
            if counter = DIV_FACTOR-1 then
                counter <= 0;
                clk_temp <= not clk_temp;
            else
                counter <= counter + 1;
            end if;
        end if;
    end process;
    
    clk_out <= clk_temp;
end rtl;
```

### Machine à états (FSM)
```vhdl
type state_type is (IDLE, START, DATA, STOP);
signal state, next_state : state_type;

-- State register
process(clk, reset)
begin
    if reset = '1' then
        state <= IDLE;
    elsif rising_edge(clk) then
        state <= next_state;
    end if;
end process;

-- Next state logic
process(state, inputs)
begin
    case state is
        when IDLE =>
            if start = '1' then
                next_state <= START;
            else
                next_state <= IDLE;
            end if;
        when START =>
            next_state <= DATA;
        when DATA =>
            if done = '1' then
                next_state <= STOP;
            else
                next_state <= DATA;
            end if;
        when STOP =>
            next_state <= IDLE;
    end case;
end process;
```

## 💡 Bonnes pratiques VHDL

### Horloges et resets
- Un seul edge (rising ou falling)
- Reset asynchrone ou synchrone
- Éviter gated clocks
- Utiliser clock enables

### Synthétisabilité
- Éviter délais (wait for)
- Initialiser registres dans reset
- Attention aux latches
- Processus combinatoires complets

### Timing
- Registrer les sorties
- Pipeline pour haute fréquence
- Éviter chemins combinatoires longs
- Synchronisation signaux asynchrones

### Organisation code
- Un fichier par entity
- Commentaires
- Nommage cohérent
- Packages pour constantes

## 📖 Compétences développées

- Programmation VHDL avancée
- Conception sur FPGA/CPLD
- Simulation et validation
- Conception de platines numériques
- Analyse de timing
- Debugging sur FPGA

## 🎯 Ressources FPGA typiques

### Exemple : Cyclone IV EP4CE15
- 15 408 Logic Elements
- 504 Kbits RAM
- 56 multiplieurs 18×18
- 343 I/O
- 4 PLLs
- Configuration série ou parallèle

### Exemple : Spartan-6 LX9
- 9 152 Logic Cells
- 576 Kbits Block RAM
- 32 DSP48A1 slices
- 200 I/O
- 4 CMTs (Clock Management Tiles)

## ⚠️ Pièges courants

### VHDL
- Latches involontaires
- Signaux vs variables
- Delta-cycle delays
- Synthèse vs simulation

### FPGA
- Timing violations
- Metastability (CDC)
- Resource exhaustion
- Configuration fails

### PCB
- Alimentation insuffisante
- Découplage inadéquat
- EMI/CEM
- Signaux d'horloge mal routés

---

<style>body{font-family:Arial,sans-serif;background-color:#f4f4f9;color:#333;line-height:1.6}h2,h3,h4,h5{color:#2a7ae2}p{text-align:justify}code{background-color:#f5f5f5;padding:2px 6px;border-radius:3px;font-family:'Courier New',monospace}pre{background-color:#f5f5f5;padding:15px;border-radius:5px;overflow-x:auto}</style>

<div class="back-nav">
  <a href="./my-courses-2021-2022.html">&larr; Retour a Mes Cours 2021-2022</a>
</div>

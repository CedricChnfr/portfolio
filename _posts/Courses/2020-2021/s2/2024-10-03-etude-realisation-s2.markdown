---
layout: default
title: "Etude et Realisation (ER) - S2"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
---

<style>
.back-nav { margin-bottom: 20px; }
.back-nav a { text-decoration: none; color: #2a7ae2; font-weight: 600; }
.back-nav a:hover { text-decoration: underline; }
.section-title { color: #2a7ae2; border-bottom: 2px solid #2a7ae2; padding-bottom: 10px; margin-top: 30px; margin-bottom: 20px; }
</style>

<div class="back-nav">
  <a href="./my-courses-2020-2021.html">&larr; Retour a Mes Cours 2020-2021</a>
</div>

# Etude et Realisation (ER) - S2

**Annee**: 2020-2021 | **Semestre**: 2 | **Type**: Projet et Realisation

---

## PART A : PRESENTATION GENERALE

### Contexte et objectifs

Le module Etude et Realisation au semestre 2 du DUT GEII est un enseignement transversal qui integre trois sous-modules complementaires : **ER FPGA**, **ER Interface** et **ER Microcontroleur**. Ce cours met l'accent sur la realisation pratique de systemes electroniques complets, depuis la conception logique (FPGA), en passant par la conception de circuits imprimes (PCB), jusqu'a la programmation embarquee (microcontroleur). C'est un cours fondamentalement pratique ou les etudiants concoivent, assemblent et testent des systemes reels.

**Objectifs pedagogiques :**
- Concevoir des circuits logiques en VHDL et les implementer sur FPGA (Cyclone II d'Altera)
- Maitriser la conception de circuits imprimes (PCB) avec le logiciel Proteus (ISIS pour la schemathique, ARES pour le routage)
- Programmer le microcontroleur C167 pour interfacer des capteurs et des actionneurs
- Integrer les trois domaines (logique, electronique, logiciel) dans un systeme complet
- Documenter et presenter les realisations techniques

### Organisation

Le cours est organise en trois sous-modules qui se deroulent en parallele au long du semestre :

1. **ER FPGA** : conception et implementation de circuits logiques sur FPGA Altera Cyclone II, avec utilisation de Quartus II et programmation en VHDL
2. **ER Interface** : conception de cartes electroniques (schemathique et PCB) avec Proteus ISIS/ARES, puis fabrication et assemblage
3. **ER Microcontroleur** : programmation du C167 en C via Keil uVision, avec integration de peripheriques (LEDs, boutons, capteurs, afficheurs)

Chaque sous-module comprend des seances de TP encadrees, avec des livrables progressifs (comptes-rendus, fichiers de conception, demonstrations).

---

## PART B : EXPERIENCE ET CONTEXTE

### Environnement pedagogique

L'annee 2020-2021 a vu une adaptation des methodes d'enseignement en raison du contexte sanitaire. Neanmoins, les seances de TP en presentiel ont pu etre maintenues pour la plupart, ce qui etait essentiel pour ce module tres pratique. Les etudiants travaillaient en binome sur les postes de travail equipes des logiciels et du materiel necessaire.

### Plateformes et outils

**ER FPGA :**
- **FPGA** : Altera Cyclone II (EP2C20) sur carte de developpement DE1
- **IDE** : Quartus II (Altera/Intel) pour la synthese, le placement-routage et la programmation
- **Langage** : VHDL (VHSIC Hardware Description Language)
- **Peripheriques sur la carte DE1** : 10 LEDs, 4 afficheurs 7-segments, 10 interrupteurs, 4 boutons-poussoirs, oscillateur 50 MHz

**ER Interface :**
- **Schemathique** : Proteus ISIS (simulation de circuits electroniques)
- **Routage PCB** : Proteus ARES (conception de circuits imprimes)
- **Fabrication** : machine a graver, perceuse, station de soudage
- **Composants** : traversants et CMS (resistances, condensateurs, circuits integres, connecteurs)

**ER Microcontroleur :**
- **Microcontroleur** : Infineon C167 (meme plateforme que le cours d'Informatique Embarquee)
- **IDE** : Keil uVision
- **Interface** : carte d'interface reliant le C167 aux capteurs et actionneurs (platine d'interface)
- **Peripheriques** : LEDs, boutons, potentiometres, capteurs de temperature, afficheurs LCD

### Liens avec d'autres cours

Ce module est au carrefour de plusieurs enseignements :
- **Informatique Embarquee (IE)** : le sous-module ER Microcontroleur utilise la meme plateforme C167 et les memes concepts (GPIO, timers, interruptions)
- **Systemes Electroniques (SE)** : les connaissances en circuits analogiques et numeriques sont appliquees dans la conception des cartes d'interface
- **Outils Logiciels (OL)** : la comprehension des signaux et des systemes aide a la simulation sous Proteus
- **Energie** : les notions d'alimentation et de protection sont utilisees dans la conception des PCB

<img src="/assets/images/courses/S2/ER/organigramme1.png" alt="Organigramme ER" style="max-width: 100%; height: auto; margin: 20px 0; border: 1px solid #ddd; border-radius: 5px; padding: 10px;">

---

## PART C : ASPECTS TECHNIQUES

### Module 1 : ER FPGA - Logique programmable en VHDL

#### 1.1 Introduction aux FPGA

Un FPGA (Field-Programmable Gate Array) est un circuit integre dont la logique interne peut etre configuree par l'utilisateur apres fabrication. Contrairement a un microcontroleur qui execute des instructions sequentiellement, un FPGA implemente des circuits logiques qui fonctionnent en parallele.

Le FPGA Cyclone II utilise dans ce cours contient :
- 18 752 elements logiques (LE)
- 239 616 bits de memoire embarquee
- 26 multiplieurs 18x18 bits
- 4 PLL (Phase-Locked Loop)
- 315 broches d'I/O utilisateur

#### 1.2 Structure du VHDL

Un programme VHDL est compose de deux parties principales :

**La declaration d'entite (entity)** : definit l'interface du composant (ports d'entree/sortie).

**Le corps d'architecture (architecture)** : definit le comportement interne du composant.

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity exemple is
  port (
    entree_a : in  std_logic;
    entree_b : in  std_logic;
    sortie   : out std_logic
  );
end exemple;

architecture comportementale of exemple is
begin
  sortie <= entree_a and entree_b;
end comportementale;
```

Les types fondamentaux en VHDL :
- `std_logic` : signal logique a un bit (valeurs '0', '1', 'Z', 'X', etc.)
- `std_logic_vector(N-1 downto 0)` : bus de N bits
- `natural`, `integer` : types numeriques pour les generiques et les constantes

#### 1.3 Prediviseur d'horloge

Le FPGA Cyclone II sur la carte DE1 dispose d'un oscillateur a 50 MHz. Pour obtenir des frequences plus basses (visibles a l'oeil nu sur les LEDs), il faut diviser cette horloge :

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_unsigned.all;

entity prediviseur is
  generic (N : natural := 25);  -- 50MHz / 2^25 = ~1.49 Hz
  port (
    ck     : in  std_logic;
    arazb  : in  std_logic;
    ck_out : out std_logic
  );
end prediviseur;

architecture arch of prediviseur is
  signal compteur : std_logic_vector(N-1 downto 0);
begin
  process(ck, arazb)
  begin
    if arazb = '0' then
      compteur <= (others => '0');
    elsif rising_edge(ck) then
      compteur <= compteur + 1;
    end if;
  end process;

  ck_out <= compteur(N-1);  -- MSB du compteur
end arch;
```

**Calcul de la frequence de sortie** :

```
f_sortie = f_entree / 2^N

Exemples :
N = 25 : f = 50 000 000 / 2^25 = 50 000 000 / 33 554 432 = 1.49 Hz
N = 24 : f = 50 000 000 / 2^24 = 50 000 000 / 16 777 216 = 2.98 Hz
N = 1  : f = 50 000 000 / 2^1  = 25 000 000 Hz = 25 MHz
```

#### 1.4 Compteur generique

Un compteur parametrable est un composant fondamental en logique numerique :

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_unsigned.all;

entity compteur is
  generic (N : natural := 8);
  port (
    ck      : in  std_logic;
    arazb   : in  std_logic;
    enable  : in  std_logic;
    sortie  : out std_logic_vector(N-1 downto 0);
    tc      : out std_logic   -- Terminal Count
  );
end compteur;

architecture arch of compteur is
  signal cnt : std_logic_vector(N-1 downto 0);
  constant MAX_VAL : std_logic_vector(N-1 downto 0) := (others => '1');
begin
  process(ck, arazb)
  begin
    if arazb = '0' then
      cnt <= (others => '0');
    elsif rising_edge(ck) then
      if enable = '1' then
        cnt <= cnt + 1;
      end if;
    end if;
  end process;

  sortie <= cnt;
  tc <= '1' when cnt = MAX_VAL else '0';
end arch;
```

Ce compteur utilise un **generic** `N` qui permet de definir le nombre de bits a l'instanciation. Le signal `tc` (Terminal Count) passe a '1' lorsque le compteur atteint sa valeur maximale, ce qui permet de chainer des compteurs ou de generer des signaux periodiques.

#### 1.5 Generateur PWM en VHDL

Le generateur PWM est un composant cle pour le controle de puissance (variation de luminosite de LEDs, commande de moteurs). Le principe repose sur la comparaison entre un compteur et une valeur de seuil (rapport cyclique) :

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_unsigned.all;

entity pwmgn is
  generic (nprediv : natural := 2;
           npas    : natural := 3);
  port (ck, arazb  : in  std_logic;
        en_pwm     : in  std_logic;
        e_prediv   : in  std_logic_vector(nprediv-1 downto 0);
        periode, ton : in  std_logic_vector(npas-1 downto 0);
        pwm_out    : out std_logic);
end pwmgn;

architecture arch of pwmgn is
  signal cnt_prediv : std_logic_vector(nprediv-1 downto 0);
  signal cnt_pwm    : std_logic_vector(npas-1 downto 0);
  signal ck_prediv  : std_logic;
begin

  -- Prediviseur programmable
  process(ck, arazb)
  begin
    if arazb = '0' then
      cnt_prediv <= (others => '0');
    elsif rising_edge(ck) then
      if cnt_prediv = e_prediv then
        cnt_prediv <= (others => '0');
      else
        cnt_prediv <= cnt_prediv + 1;
      end if;
    end if;
  end process;

  ck_prediv <= '1' when cnt_prediv = e_prediv else '0';

  -- Compteur de periode PWM
  process(ck, arazb)
  begin
    if arazb = '0' then
      cnt_pwm <= (others => '0');
    elsif rising_edge(ck) then
      if ck_prediv = '1' then
        if cnt_pwm = periode then
          cnt_pwm <= (others => '0');
        else
          cnt_pwm <= cnt_pwm + 1;
        end if;
      end if;
    end if;
  end process;

  -- Comparaison pour la sortie PWM
  pwm_out <= '1' when (en_pwm = '1' and cnt_pwm < ton) else '0';

end arch;
```

**Principe de fonctionnement** :
1. Le prediviseur divise l'horloge d'entree par (e_prediv + 1)
2. Le compteur PWM compte de 0 a la valeur `periode` sur l'horloge predivisee
3. La sortie est a '1' tant que le compteur est inferieur a `ton`, et a '0' sinon
4. Le rapport cyclique est : `alpha = ton / (periode + 1)`

**Calcul de la frequence PWM** :

```
f_PWM = f_ck / ((e_prediv + 1) * (periode + 1))

Exemple : f_ck = 50 MHz, e_prediv = 3, periode = 7
f_PWM = 50 000 000 / (4 * 8) = 1 562 500 Hz = 1.56 MHz
```

#### 1.6 Frequencemetre numerique

Un frequencemetre mesure la frequence d'un signal en comptant le nombre d'impulsions pendant un intervalle de temps connu (porte de mesure) :

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_unsigned.all;

entity frequencemetre is
  generic (N_compteur : natural := 16;
           N_porte    : natural := 25);
  port (
    ck_ref   : in  std_logic;    -- Horloge de reference (50 MHz)
    signal_in : in  std_logic;   -- Signal a mesurer
    arazb    : in  std_logic;
    freq_out : out std_logic_vector(N_compteur-1 downto 0)
  );
end frequencemetre;

architecture arch of frequencemetre is
  signal porte       : std_logic;
  signal cnt_porte   : std_logic_vector(N_porte-1 downto 0);
  signal cnt_freq    : std_logic_vector(N_compteur-1 downto 0);
  signal freq_latch  : std_logic_vector(N_compteur-1 downto 0);
begin

  -- Generation de la porte de mesure (1 seconde avec N_porte=25 et ck=50MHz)
  process(ck_ref, arazb)
  begin
    if arazb = '0' then
      cnt_porte <= (others => '0');
    elsif rising_edge(ck_ref) then
      cnt_porte <= cnt_porte + 1;
    end if;
  end process;

  porte <= cnt_porte(N_porte-1);

  -- Compteur de frequence (compte les fronts du signal d'entree pendant la porte)
  process(signal_in, arazb, porte)
  begin
    if arazb = '0' then
      cnt_freq <= (others => '0');
    elsif porte = '0' then
      cnt_freq <= (others => '0');     -- RAZ pendant la demi-periode basse de la porte
    elsif rising_edge(signal_in) then
      cnt_freq <= cnt_freq + 1;        -- Compte pendant la demi-periode haute
    end if;
  end process;

  -- Memorisation du resultat en fin de porte
  process(porte, arazb)
  begin
    if arazb = '0' then
      freq_latch <= (others => '0');
    elsif falling_edge(porte) then
      freq_latch <= cnt_freq;
    end if;
  end process;

  freq_out <= freq_latch;
end arch;
```

#### 1.7 Decodeur 7 segments

L'affichage sur les 7 segments de la carte DE1 necessite un decodeur BCD vers 7 segments :

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity dec7seg is
  port (
    bcd    : in  std_logic_vector(3 downto 0);
    seg    : out std_logic_vector(6 downto 0)  -- segments a-g (actif bas)
  );
end dec7seg;

architecture arch of dec7seg is
begin
  with bcd select
    seg <= "1000000" when "0000",  -- 0
           "1111001" when "0001",  -- 1
           "0100100" when "0010",  -- 2
           "0110000" when "0011",  -- 3
           "0011001" when "0100",  -- 4
           "0010010" when "0101",  -- 5
           "0000010" when "0110",  -- 6
           "1111000" when "0111",  -- 7
           "0000000" when "1000",  -- 8
           "0010000" when "1001",  -- 9
           "1111111" when others;  -- Eteint
end arch;
```

### Module 2 : ER Interface - Conception de PCB avec Proteus

#### 2.1 Presentation de Proteus ISIS/ARES

Le logiciel Proteus est un outil de CAO (Conception Assistee par Ordinateur) electronique compose de deux modules complementaires :

- **ISIS** (Intelligent Schematic Input System) : editeur de schemathique et simulateur de circuits. Il permet de dessiner le schema electrique d'un circuit et de le simuler pour valider son fonctionnement avant la realisation.

- **ARES** (Advanced Routing and Editing Software) : editeur de circuits imprimes. Il permet de placer les composants sur la carte, de router les pistes et de generer les fichiers de fabrication (Gerber).

#### 2.2 Etapes de conception d'un PCB

La conception d'un circuit imprime suit un processus methodique :

**Etape 1 : Schemathique (ISIS)**
1. Placement des composants sur le schema (resistances, condensateurs, circuits integres, connecteurs)
2. Cablage des composants (fils et bus)
3. Attribution des references et des valeurs
4. Verification electrique (ERC - Electrical Rules Check) : detecte les court-circuits, les broches non connectees, etc.
5. Simulation du circuit pour valider le fonctionnement

**Etape 2 : Netlist**
- Generation de la netlist : fichier qui decrit toutes les connexions electriques entre les composants
- Transfert de la netlist d'ISIS vers ARES

**Etape 3 : Placement-routage (ARES)**
1. Definition du contour de la carte (board outline)
2. Placement des composants en respectant les contraintes mecaniques et thermiques
3. Routage des pistes : connexion physique des broches selon la netlist
4. Verification des regles de conception (DRC - Design Rules Check) : largeur de pistes, espacement, taille des pastilles
5. Ajout du plan de masse (ground plane) pour ameliorer la CEM

**Etape 4 : Fabrication**
1. Generation des fichiers Gerber (format standard pour la fabrication industrielle)
2. Gravure du circuit (chimique ou mecanique)
3. Percage des trous
4. Soudure des composants

#### 2.3 Regles de conception PCB

Les regles de conception sont essentielles pour garantir la fabricabilite et la fiabilite du circuit :

```
Largeur de piste minimale : 0.25 mm (signal), 0.5 mm (alimentation)
Espacement minimal entre pistes : 0.25 mm
Taille de pastille (pad) : > 1.8 * diametre du trou
Diametre de trou : 0.8 mm (composants traversants standard)
Largeur d'anneau (annular ring) : >= 0.3 mm
Clearance composant-bord de carte : >= 2 mm
```

#### 2.4 Platine d'interface

La platine d'interface est un PCB concu pour connecter le microcontroleur C167 aux peripheriques externes. Elle comprend :

- **Connecteurs** : liaison vers la carte C167 (bus de donnees, bus d'adresses, signaux de controle)
- **Buffers/Drivers** : circuits tampons pour proteger les ports du microcontroleur
- **Circuits de conditionnement** : diviseurs de tension, filtres, amplificateurs pour adapter les signaux des capteurs
- **Indicateurs** : LEDs de diagnostic, points de test
- **Alimentation** : regulateurs de tension, filtrage des alimentations

La conception de cette platine a ete realisee en TP avec Proteus ARES, en suivant le schema fourni dans les supports de cours.

#### 2.5 Composants et empreintes (footprints)

Chaque composant physique possede une empreinte qui definit son occupation sur le PCB :

```
Resistance traversante (axiale) : empreinte RES40 (10.16 mm entre pattes)
Condensateur ceramique         : empreinte CAP_DISC (5.08 mm entre pattes)
Circuit integre DIP-14         : empreinte DIP14 (7.62 mm entre rangees)
Connecteur HE10 (2x5)         : empreinte HE10_2x5 (2.54 mm de pas)
LED 3mm                        : empreinte LED3MM
```

Le choix de l'empreinte est critique : une erreur d'empreinte rend la carte infabricable ou impossible a assembler.

### Module 3 : ER Microcontroleur - Programmation C167 appliquee

#### 3.1 Architecture materielle du systeme

Le systeme complet ER Microcontroleur comprend :
- La carte de developpement C167 (processeur, memoire, ports serie)
- La platine d'interface (concue en ER Interface)
- Les peripheriques (LEDs, boutons, capteurs, afficheurs)

L'objectif est d'integrer les connaissances de programmation du C167 (acquises en Informatique Embarquee) avec la conception materielle (ER Interface) pour realiser un systeme embarque fonctionnel.

#### 3.2 Gestion des LEDs et afficheurs

L'affichage sur les LEDs et les afficheurs 7 segments connectes via la platine d'interface :

```c
#include <reg167.h>
#include "IUT_C167_2019.h"

/* Codes 7 segments (cathode commune) */
const unsigned char code7seg[10] = {
    0x3F,  /* 0 : segments a,b,c,d,e,f */
    0x06,  /* 1 : segments b,c */
    0x5B,  /* 2 : segments a,b,d,e,g */
    0x4F,  /* 3 : segments a,b,c,d,g */
    0x66,  /* 4 : segments b,c,f,g */
    0x6D,  /* 5 : segments a,c,d,f,g */
    0x7D,  /* 6 : segments a,c,d,e,f,g */
    0x07,  /* 7 : segments a,b,c */
    0x7F,  /* 8 : tous les segments */
    0x6F   /* 9 : segments a,b,c,d,f,g */
};

void afficher_nombre(unsigned int valeur) {
    unsigned char unite, dizaine, centaine;
    unite    = valeur % 10;
    dizaine  = (valeur / 10) % 10;
    centaine = (valeur / 100) % 10;

    /* Ecriture sur les afficheurs via les ports */
    P8 = code7seg[unite];
    /* Selection de l'afficheur par multiplexage */
}
```

#### 3.3 Acquisition analogique et traitement

Le systeme peut lire des capteurs analogiques via le CAN du C167 et afficher les resultats :

```c
#include <reg167.h>
#include "IUT_C167_2019.h"

void init_adc(void) {
    ADCON = 0x0000;   /* Configuration ADC */
}

unsigned int lire_temperature(void) {
    unsigned int valeur_brute;
    float tension, temperature;

    /* Lecture du CAN sur le canal 0 */
    ADCON = 0x0000;           /* Canal 0 */
    ADCON |= 0x0100;          /* Start conversion */
    while (ADCON & 0x0800);   /* Attente fin de conversion */
    valeur_brute = ADDAT;     /* Lecture resultat 10 bits */

    /* Conversion en tension (Vref = 5V, 10 bits) */
    tension = (float)valeur_brute * 5.0 / 1023.0;

    /* Conversion en temperature (capteur LM35 : 10 mV/degre) */
    temperature = tension * 100.0;

    return (unsigned int)temperature;
}

void main(void) {
    unsigned int temp;
    init_serie();
    init_adc();
    DP8 = 0xFF;

    do {
        temp = lire_temperature();
        printf("Temperature = %d degres\r\n", temp);
        tempo_ms(1000);   /* Mesure toutes les secondes */
    } while(1);
}
```

#### 3.4 Generation de signaux avec timer et platine d'interface

En combinant les timers du C167 et la platine d'interface, on peut generer des signaux de frequence et de rapport cyclique programmables :

```c
#include <reg167.h>
#include "IUT_C167_2019.h"

void init_pwm_hardware(unsigned int periode, unsigned int ton) {
    /* Configuration du Timer 3 en mode PWM */
    DP3 |= 0x0008;       /* P3.3 en sortie */
    T3CON = 0x0002;       /* Prescaler /8 */
    T3OTL = 0;
    T3OE = 1;             /* Active sortie toggle */
    T3UD = 1;             /* Mode decompteur */

    /* Timer 2 pour le rechargement automatique */
    T2CON = 0x0027;       /* T2 recharge T3 */
    T3 = periode - 1;
    T2 = periode - 1;

    T3R = 1;              /* Demarre le timer */
}

void main(void) {
    unsigned char sw;
    init_serie();
    DP7 = 0x00;
    DP8 = 0xFF;

    /* Generateur de frequence : 5 kHz */
    /* f = 20MHz / (8 * 250 * 2) = 5 kHz */
    init_pwm_hardware(250, 125);

    do {
        sw = (unsigned char)P7;
        P8 = sw;          /* Echo des interrupteurs sur LEDs */

        /* Modification dynamique de la frequence via les interrupteurs */
        if (sw != 0) {
            T2 = (unsigned int)sw * 10;
            T3 = (unsigned int)sw * 10;
        }
    } while(1);
}
```

#### 3.5 Machine a etats en C

Pour les systemes plus complexes, on utilise une architecture de machine a etats :

```c
#include <reg167.h>
#include "IUT_C167_2019.h"

typedef enum {
    ETAT_INIT,
    ETAT_ATTENTE,
    ETAT_ACQUISITION,
    ETAT_TRAITEMENT,
    ETAT_AFFICHAGE
} etat_t;

etat_t etat_courant = ETAT_INIT;

void machine_a_etats(void) {
    static unsigned int donnee = 0;

    switch (etat_courant) {
        case ETAT_INIT:
            DP7 = 0x00;
            DP8 = 0xFF;
            P8 = 0x00;
            etat_courant = ETAT_ATTENTE;
            break;

        case ETAT_ATTENTE:
            if (P7 & 0x01) {       /* Bouton appuye */
                etat_courant = ETAT_ACQUISITION;
            }
            break;

        case ETAT_ACQUISITION:
            ADCON = 0x0100;         /* Lance conversion ADC */
            while (ADCON & 0x0800); /* Attend fin */
            donnee = ADDAT;
            etat_courant = ETAT_TRAITEMENT;
            break;

        case ETAT_TRAITEMENT:
            donnee = donnee * 5000 / 1023;  /* Conversion en mV */
            etat_courant = ETAT_AFFICHAGE;
            break;

        case ETAT_AFFICHAGE:
            printf("Tension = %d mV\r\n", donnee);
            P8 = (unsigned char)(donnee >> 2);  /* Affichage 8 bits */
            tempo_ms(500);
            etat_courant = ETAT_ATTENTE;
            break;
    }
}

void main(void) {
    init_serie();
    do {
        machine_a_etats();
    } while(1);
}
```

Cette architecture de machine a etats est fondamentale pour structurer les programmes embarques complexes. Elle permet de separer clairement les differentes phases du traitement et de gerer les transitions de maniere explicite.

### Integration des trois modules

L'objectif final du module ER est l'integration :

1. **Conception FPGA** : implementation d'un prediviseur et d'un generateur PWM en VHDL sur le Cyclone II
2. **Conception PCB** : realisation de la platine d'interface qui connecte le FPGA et le C167 aux peripheriques
3. **Programmation C167** : logiciel embarque qui communique avec le FPGA via les ports et qui controle les peripheriques via la platine d'interface

Cette approche systeme est representative de la realite industrielle ou un produit electronique combine souvent un FPGA (pour le traitement rapide des signaux), un microcontroleur (pour la logique applicative) et une carte electronique (pour l'interface avec le monde physique).

---

## PART D : ANALYSE ET REFLEXION

### Competences acquises

Le module ER S2 m'a permis de developper des competences dans trois domaines complementaires :

- **Logique programmable (FPGA/VHDL)** : la programmation en VHDL m'a appris a penser en parallelisme materiel, ce qui est fondamentalement different de la programmation sequentielle classique. La conception de prediviseurs, compteurs et generateurs PWM m'a donne une comprehension pratique de la logique synchrone. L'utilisation des generiques VHDL pour creer des composants parametrables est une bonne pratique de conception reutilisable.

- **Conception PCB** : la maitrise de Proteus ISIS/ARES m'a initie a la conception de circuits imprimes, depuis la schemathique jusqu'au routage. Les regles de conception (largeur de piste, espacement, plan de masse) sont des connaissances directement applicables en milieu industriel. La realisation physique de la platine d'interface (gravure, percage, soudure) m'a confronte aux contraintes de fabrication.

- **Integration systeme** : la capacite a combiner un FPGA, un microcontroleur et une carte electronique dans un systeme coherent est une competence tres recherchee en electronique embarquee. Cela necessite de maitriser a la fois le materiel et le logiciel, et de comprendre les interfaces entre les differents sous-systemes.

### Auto-evaluation

La partie FPGA/VHDL a ete la plus desorientante au debut, car le paradigme de programmation est radicalement different du C. La notion que toutes les instructions s'executent simultanement (et non sequentiellement) demande un changement de mentalite. Cependant, une fois ce paradigme assimile, la conception de circuits logiques en VHDL devient tres logique et methodique.

La conception PCB avec Proteus a ete agreable car les outils sont visuels et le resultat concret (on obtient une vraie carte electronique a la fin). La difficulte principale reside dans le routage, ou il faut trouver un chemin pour toutes les pistes sans croisement (sur un PCB simple face).

La partie microcontroleur etait la plus familiere grace au cours d'Informatique Embarquee qui se deroule en parallele. L'apport specifique de l'ER est l'integration avec le materiel : on ne programme plus dans le vide, mais on interagit avec de vrais capteurs et actionneurs.

### Connexions et perspectives

Les competences acquises en ER S2 sont fondamentales pour la suite du cursus :
- **S3-S4** : les cours d'electronique numerique et de VHDL approfondissent la conception sur FPGA
- **S5** : le cours d'architecture materielle utilise les concepts de logique programmable
- **Projet de fin d'etudes** : la capacite a concevoir un systeme complet (materiel + logiciel) est au coeur du projet
- **Master REOC** : la specialisation en objets connectes repose sur l'integration de microcontroleurs, de circuits de communication et de capteurs dans des systemes embarques

Ce module est l'un des plus formateurs du DUT GEII car il oblige a manipuler l'ensemble de la chaine de conception electronique, depuis l'idee jusqu'au prototype fonctionnel.

---

## Documents de Cours

<div class="pdf-item">
  <h4>ER FPGA S2 2020-2021</h4>
  <p>Support complet du sous-module ER FPGA : introduction aux FPGA Cyclone II, langage VHDL, prediviseurs, compteurs, generateurs PWM, frequencemetre. Inclut les sujets de TP.</p>
  <embed src="/cours-pdf/S2/ER/ER_FPGA_S2_2020-2021_-_etu.pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/cours-pdf/S2/ER/ER_FPGA_S2_2020-2021_-_etu.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
  </p>
</div>

<div class="pdf-item">
  <h4>COURS interface S2</h4>
  <p>Cours sur la conception de cartes d'interface : schemathique, composants, regles de conception, connectique entre microcontroleur et peripheriques.</p>
  <embed src="/cours-pdf/S2/ER/COURS_interface_S2.pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/cours-pdf/S2/ER/COURS_interface_S2.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
  </p>
</div>

<div class="pdf-item">
  <h4>Cours Interfacage 2021 - Correction</h4>
  <p>Cours d'interfacage avec corrections des exercices : buffers, drivers, conditionnement de signaux, protection des ports.</p>
  <embed src="/cours-pdf/S2/ER/Cours_interfacage_2021_etudiant_correction.pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/cours-pdf/S2/ER/Cours_interfacage_2021_etudiant_correction.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
  </p>
</div>

<div class="pdf-item">
  <h4>Polycopie Carte Interface 2021</h4>
  <p>Documentation complete de la platine d'interface : schema electrique, nomenclature des composants, procedure d'assemblage et de test.</p>
  <embed src="/cours-pdf/S2/ER/poly_carte_interface_2021.pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/cours-pdf/S2/ER/poly_carte_interface_2021.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
  </p>
</div>

---

<style>body{font-family:Arial,sans-serif;background-color:#f4f4f9;color:#333;line-height:1.6}h2,h3,h4,h5{color:#2a7ae2}p{text-align:justify}code{background-color:#f5f5f5;padding:2px 6px;border-radius:3px;font-family:'Courier New',monospace}pre{background-color:#f5f5f5;padding:15px;border-radius:5px;overflow-x:auto}</style>

<div class="back-nav">
  <a href="./my-courses-2020-2021.html">&larr; Retour a Mes Cours 2020-2021</a>
</div>

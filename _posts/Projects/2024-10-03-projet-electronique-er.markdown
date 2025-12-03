---
layout: default
title: "Advanced Electronics System Design"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

[← Back to Academic Project](./my-projects.html)

# Introduction
This open-ended project provided complete autonomy to design and build a complex electronic system from concept to working prototype. Working in pairs over 60 hours, we could choose from various applications: multi-sensor datalogger, USB oscilloscope, programmable laboratory power supply, or other custom electronic instruments. The project synthesized knowledge from analog circuits, digital systems, embedded programming, and professional PCB design.

# Project Overview
This project represented the culmination of our electrical engineering training, requiring us to manage every aspect: specifications definition, component selection, schematic design, PCB layout, firmware development, and comprehensive testing. The emphasis was on professional-grade implementation and autonomous project management.

## Example Project Types

### Data Acquisition Systems
**Multi-Sensor Datalogger:**
- Multiple sensor inputs (temperature, pressure, humidity)
- Instrumentation amplifiers and filtering
- 12-16 bit ADC (STM32 or ADS1115)
- SD card storage via SPI
- OLED/LCD display
- Li-Ion battery with charging circuit

**USB Oscilloscope (1 MHz bandwidth):**
- Switchable input attenuator (1x, 10x)
- Differential amplifier with ±50V protection
- Fast ADC (MSPS sampling)
- USB interface to PC
- Python GUI for visualization
- Analog trigger circuit

### Power Electronics
**Programmable Laboratory Power Supply:**
- Dual output: 0-30V, 0-3A per channel
- Linear or switching regulation
- Microcontroller control with DAC setpoints
- LCD display for voltage/current
- Overvoltage and overcurrent protection
- UART interface for PC control

### Embedded Systems
**Autonomous Weather Station:**
- Environmental sensors (T°, pressure, humidity, wind, rain)
- ESP32 microcontroller with WiFi
- MQTT data transmission to cloud
- Solar panel + battery power system
- IP65 outdoor enclosure
- Low-power operation for extended autonomy

# Design Methodology

## Phase 1: Specifications and Planning
**Requirements Definition:**
- Detailed functional specifications
- Performance targets (accuracy, speed, autonomy)
- Constraints (cost, size, power budget)

**Feasibility Study:**
- Component research and selection
- Technical solution evaluation
- Cost estimation and BOM planning

## Phase 2: Electronic Design

**Functional Block Diagram:**
- System architecture decomposition
- Interface definitions between blocks
- Signal flow analysis

**Schematic Design (KiCad/Altium):**
- Power supply section (regulators, decoupling)
- Analog conditioning circuits
- Microcontroller and peripherals
- Connectors and interfaces
- Component selection with verified part numbers (Mouser/Digi-Key)

**Circuit Simulations:**
- LTspice for analog circuits
- Proteus for MCU co-simulation
- Validation of critical parameters

## Phase 3: PCB Design

**Layout Strategy:**
- 2 or 4-layer PCB depending on complexity
- Component placement (thermal, EMC considerations)
- Trace routing: width for current capacity, spacing for voltage
- Ground and power planes
- Design Rule Check (DRC) validation

**Manufacturing:**
- Gerber file generation
- Order from PCB fabricator (3-7 day turnaround)
- Inspection upon reception
- SMD and through-hole component assembly
- Soldering with iron, hot air, or reflow oven

## Phase 4: Firmware Development

**Embedded Software:**
- Peripheral configuration (ADC, I2C, UART, SPI)
- Data acquisition and processing
- Calibration algorithms
- User interface (buttons, LCD)
- Communication protocols

**PC Interface (if applicable):**
- Python/Qt GUI development
- Serial communication (UART/USB)
- Data visualization and logging

## Phase 5: Testing and Validation

**Unit Testing:**
- Power supply verification (voltages, ripple)
- Analog conditioning (gain, offset, noise)
- Digital communication (I2C, SPI, UART)
- Individual subsystem validation

**Functional Testing:**
- Specifications compliance verification
- Accuracy and repeatability measurements  
- Calibration procedures
- Performance characterization

**Documentation:**
- Test protocols and procedures
- Results tables and graphs
- Deviation analysis
- Final validation report

# Results and Analysis

The completed system met or exceeded design specifications, demonstrating successful integration of analog and digital subsystems. Key challenges included minimizing noise in sensitive analog circuits, optimizing power consumption for battery operation, and achieving reliable communication between subsystems.

Performance validation confirmed:
- Measurement accuracy within design targets
- Stable operation across specified conditions
- Reliable data acquisition and storage
- User-friendly interface operation

# Conclusion
This project provided comprehensive experience in professional electronic system development, from concept through validated prototype. The autonomous nature of the work developed critical project management skills including planning, problem-solving, and technical documentation. The working prototype demonstrates our ability to deliver complete, functional electronic systems meeting real-world requirements.

<style>
p {
  text-align: justify;
}
.modal {
  display: none; 
  position: fixed; 
  z-index: 1; 
  padding-top: 60px; 
  left: 0;
  top: 0;
  width: 100%; 
  height: 100%; 
  overflow: auto; 
  background-color: rgb(0,0,0); 
  background-color: rgba(0,0,0,0.9); 
}

.modal-content {
  margin: auto;
  display: block;
  width: 80%;
  max-width: 700px;
}

.close {
  position: absolute;
  top: 15px;
  right: 35px;
  color: #f1f1f1;
  font-size: 40px;
  font-weight: bold;
  transition: 0.3s;
}

.close:hover,
.close:focus {
  color: #bbb;
  text-decoration: none;
  cursor: pointer;
}
</style>

<!-- Modal -->
<div id="myModal" class="modal">
  <span class="close" onclick="closeModal()">&times;</span>
  <img class="modal-content" id="img01">
</div>

<script>
function openModal(src) {
  var modal = document.getElementById("myModal");
  var modalImg = document.getElementById("img01");
  modal.style.display = "block";
  modalImg.src = src;
}

function closeModal() {
  var modal = document.getElementById("myModal");
  modal.style.display = "none";
}
</script>

---

## PART B: EXPÉRIENCE, CONTEXTE ET FONCTION (Exemples projets)

### Systèmes d'acquisition

**Datalogger multi-capteurs :**
- Capteurs : température (NTC, LM35), pression (BMP280), humidité (DHT22)
- Conditionnement : amplis instrumentations, filtrage
- ADC 12-16 bits (STM32 ou ADS1115)
- Stockage : carte SD (SPI)
- Affichage : OLED I2C
- Alimentation : batterie Li-Ion + chargeur

**Oscilloscope USB 1 MHz :**
- Entrée : atténuateur commutable (1x, 10x)
- Ampli différentiel (protection ±50V)
- ADC rapide (MSPS) ou STM32F4 (2 MSPS)
- FPGA pour buffer (optionnel)
- USB vers PC (interface Python)
- Trigger analogique (comparateur)

### Systèmes de puissance

**Alimentation de laboratoire programmable :**
- Double sortie 0-30V, 0-3A
- Régulation linéaire ou à découpage
- Contrôle MCU (DAC pour consigne)
- Affichage LCD : tension, courant
- Protection : surtension, surintensité
- Interface UART (commande PC)

### Systèmes embarqués

**Station météo connectée :**
- Capteurs : T°, P, humidité, vent (anémomètre), pluie
- MCU : ESP32 (WiFi)
- Transmission : MQTT vers serveur
- Alimentation : solaire + batterie
- Boîtier extérieur IP65

---

## PART C: ASPECTS TECHNIQUES (Méthodologie)

### Phase 1 : Cahier des charges (5h)

**Spécifications :**
- Fonctionnalités précises
- Performances attendues (précision, vitesse, autonomie)
- Contraintes (coût, taille, alimentation)

**Analyse faisabilité :**
- Recherche composants
- Étude solutions techniques
- Estimation coût

### Phase 2 : Conception (20h)

**Schéma fonctionnel :**
- Blocs principaux
- Interfaces

**Schéma électrique (KiCad/Altium) :**
- Alimentation (régulateurs, découplage)
- Conditionnement analogique
- MCU et périphériques
- Connecteurs
- Choix composants (Références Mouser/Digi-Key)

**Simulations :**
- LTSpice (circuits analogiques)
- Proteus (co-simulation MCU)

### Phase 3 : PCB (15h)

**Layout :**
- 2 ou 4 couches selon complexité
- Placement composants (thermique, CEM)
- Routage : largeur pistes (courant), espacement
- Plans de masse et alimentation
- DRC (Design Rule Check)

**Fabrication :**
- Génération Gerber
- Commande fabricant (3-7 jours)
- Réception et inspection

**Assemblage :**
- Soudure CMS (fer, air chaud, four)
- Soudure traversants
- Inspection visuelle et électrique

### Phase 4 : Programmation (10h)

**Firmware MCU :**
- Configuration périphériques (ADC, I2C, UART, etc.)
- Acquisition données
- Traitements (moyennage, calibration)
- Interface utilisateur (boutons, LCD)

**Interface PC (si applicable) :**
- Python/Qt pour GUI
- Communication série (UART, USB)

### Phase 5 : Tests et validation (10h)

**Tests unitaires :**
- Alimentation (tensions, ondulations)
- Conditionnement analogique (gain, offset, bruit)
- Communication (I2C, SPI, UART)

**Tests fonctionnels :**
- Validation cahier des charges
- Mesure précision, répétabilité
- Calibration si nécessaire

**Documentation tests :**
- Protocoles
- Résultats (tableaux, courbes)
- Analyse écarts

---

## PART D: ANALYSE ET RÉFLEXION

### Livrables
- Rapport technique (35 pages) : cahier des charges, conception, réalisation, tests
- Schémas et PCB (fichiers sources)
- Code source (commenté)
- Présentation orale + démonstration fonctionnelle

### Évaluation
- Cahier des charges et conception (20%)
- Réalisation PCB et assemblage (25%)
- Programmation (15%)
- Tests et validation (20%)
- Rapport (15%)
- Présentation (5%)

### Compétences acquises
- Gestion projet électronique complet
- Conception multi-domaines (analogique, numérique, puissance)
- PCB professionnel
- Tests et validation systématiques
- Autonomie et organisation

### Débouchés
- Ingénieur conception électronique
- Chef de projet systèmes embarqués
- R&D instrumentation

## 📚 Types de projets possibles

### Systèmes d'acquisition

**Enregistreur de données (datalogger) :**
- Capteurs multiples (T°, P, humidité, etc.)
- Conditionnement analogique
- Conversion A/N haute résolution
- Microcontrôleur
- Stockage (SD card, EEPROM)
- Interface (LCD, Bluetooth)
- Autonomie sur batterie

### Instrumentation

**Oscilloscope numérique simplifié :**
- Étage d'entrée (atténuation, protection)
- Amplification variable
- ADC rapide (MSPS)
- FPGA pour acquisition
- Interface USB vers PC
- Software de visualisation

**Multimètre intelligent :**
- Mesures V, I, R, C
- Autorange
- Affichage graphique
- Enregistrement
- Communication PC

### Électronique de puissance

**Onduleur basse puissance :**
- DC/AC conversion
- Modulation PWM (sinus)
- Driver de MOSFETs
- Filtrage LC
- Protection
- Contrôle numérique

**Chargeur de batterie intelligent :**
- Buck/Boost converter
- Gestion multi-chimies (Li-ion, NiMH)
- Mesure V, I, T°
- Algorithmes de charge
- Affichage état
- Sécurités

### Communication

**Émetteur-récepteur RF simple :**
- Modulation FSK ou ASK
- Circuits RF (VCO, mélangeurs)
- Amplification
- Antenne intégrée
- Démodulation
- Interface série

**Modem acoustique :**
- Génération signaux audio
- DAC/ADC
- Filtrage analogique
- Modulation AFSK
- Démodulation
- Communication via jack audio

## 🛠️ Méthodologie de projet

### Phase 1 : Spécifications (Semaine 1-2)

#### Définition du besoin
- Analyse du problème
- Fonctions principales
- Performances attendues
- Contraintes

#### Cahier des charges fonctionnel
- Fonctions de service
- Critères de performance
- Niveaux requis
- Flexibilité

#### Cahier des charges technique
- Spécifications électriques
- Spécifications mécaniques
- Contraintes environnementales
- Normes et certifications

### Phase 2 : Conception (Semaine 3-6)

#### Architecture système
- Décomposition en blocs
- Interfaces entre blocs
- Choix technologiques
- Budgets (puissance, timing, coût)

#### Conception par blocs

**Analogique :**
- Schémas de principe
- Calcul des composants
- Simulation SPICE
- Validation performances

**Numérique :**
- Choix microcontrôleur/FPGA
- Architecture logicielle
- Périphériques nécessaires
- Timings et ressources

**Alimentation :**
- Tensions requises
- Consommation estimée
- Topologie convertisseurs
- Dimensionnement

**Mécanique :**
- Dimensions PCB
- Connecteurs et interfaces
- Boîtier
- Dissipation thermique

#### Simulations
- Circuits analogiques (LTspice, PSpice)
- Circuits de puissance
- Signaux numériques
- Co-simulation si nécessaire

#### Sélection des composants
- Caractéristiques électriques
- Disponibilité et coût
- Packaging (CMS vs traversant)
- Alternatives et second sources

### Phase 3 : Réalisation PCB (Semaine 7-9)

#### Schémas électroniques

**Règles de conception :**
- Hiérarchie et modularité
- Symboles normalisés
- Annotations claires
- Valeurs et références

**Sections :**
- Page d'accueil (infos projet)
- Alimentation
- Microcontrôleur et horloge
- Interfaces et capteurs
- Conditionnement analogique
- Puissance
- Connecteurs

#### Layout PCB

**Stratégie multicouches (4 couches typ.) :**
- Layer 1 (Top) : Composants et signaux
- Layer 2 : Plan de masse (GND)
- Layer 3 : Plan d'alimentation (VCC)
- Layer 4 (Bottom) : Signaux et composants

**Routage :**

*Analogique :*
- Pistes larges pour courants
- Éviter boucles de masse
- Garde autour des signaux sensibles
- Découplage local

*Numérique :*
- Respect des contraintes d'impédance si nécessaire
- Longueurs égalisées (bus rapides)
- Via stitching (masse)
- Séparation zones bruyantes/sensibles

*Puissance :*
- Pistes larges (calcul section)
- Plans de cuivre
- Dissipation thermique (vias thermiques)
- Découplage massif

**DFM et DFT :**
- Espacement minimum respecté
- Accessibilité pour soudure
- Points de test
- Sérigraphie lisible

#### Vérifications
- DRC (Design Rule Check)
- ERC (Electrical Rule Check)
- Simulation de l'intégrité du signal
- Revue de conception (peer review)

#### Génération fichiers de fabrication
- Gerber RS-274X
- Excellon (drill)
- Pick&Place
- BOM (Bill of Materials)

### Phase 4 : Fabrication et assemblage (Semaine 10-11)

#### Fabrication PCB
- Choix fabricant (qualité/coût/délai)
- Spécifications : épaisseur, finition, couleur
- Délai : 1-2 semaines
- Réception et contrôle qualité

#### Approvisionnement composants
- Commande fournisseurs (Mouser, Digikey, Farnell)
- Vérification références
- Stock tampon pour dépannage

#### Assemblage
- Programmation du stencil (pâte à souder)
- Placement CMS
- Refusion (four ou plaque chauffante)
- Soudure traversants
- Inspection visuelle et microscopie

#### Nettoyage et finition
- Nettoyage flux
- Application vernis (si requis)
- Installation dans boîtier

### Phase 5 : Tests et validation (Semaine 12-14)

#### Tests unitaires par blocs

**Alimentation :**
- Tensions sorties
- Ondulation (ripple)
- Régulation de charge
- Efficacité
- Protections

**Analogique :**
- Points de polarisation
- Gains d'amplificateurs
- Bandes passantes de filtres
- Linéarité
- Bruit

**Numérique :**
- Programmation MCU/FPGA
- Test périphériques (I2C, SPI, UART)
- Fréquences horloges
- Timings

#### Tests d'intégration
- Communication entre blocs
- Fonctions complètes
- Cas d'usage réels
- Cas limites

#### Caractérisation performances
- Mesures vs spécifications
- Tableaux de résultats
- Graphiques
- Écarts et explications

#### Débogage
- Identification problèmes
- Analyse racine (root cause)
- Corrections (fils volants, composants)
- Tests de non-régression

### Phase 6 : Documentation et présentation (Semaine 15)

#### Documentation technique

**Manuel utilisateur :**
- Description fonctionnalités
- Instructions utilisation
- Spécifications
- Avertissements

**Documentation technique :**
- Architecture détaillée
- Schémas commentés
- Layout PCB
- Code source documenté
- Procédures de test

**Rapport de projet :**
1. Introduction et contexte
2. Spécifications et cahier des charges
3. Conception (architecture, schémas, calculs)
4. Simulations
5. Réalisation (PCB, assemblage)
6. Tests et validation
7. Résultats et analyse
8. Difficultés rencontrées et solutions
9. Améliorations possibles
10. Conclusion
11. Annexes (datasheets, codes, mesures)

#### Soutenance finale
- Présentation 20 minutes
- Démonstration live du système
- Questions jury
- Évaluation

## 💻 Outils utilisés

### CAO Électronique
- **Altium Designer** : Professionnel complet
- **KiCad** : Open source performant
- **Eagle** : Populaire
- **OrCAD/Allegro** : Industrie

### Simulation
- **LTspice** : Circuits analogiques
- **PSpice** : Simulation avancée
- **Proteus** : Co-simulation MCU
- **MATLAB/Simulink** : Systèmes

### Programmation
- **STM32CubeIDE** : STM32
- **Quartus** : FPGA Intel
- **Vivado** : FPGA Xilinx
- **MPLAB** : Microchip

### Test et mesure
- Oscilloscope
- Analyseur de spectre
- Multimètre de précision
- Générateur de fonctions
- Alimentation de laboratoire
- Charge électronique

## 📊 Livrables

### Documents
- Cahier des charges
- Schémas électroniques
- PCB (layout + Gerber)
- Nomenclature (BOM)
- Code source documenté
- Procédures de test
- Résultats de mesures
- Rapport final (50-80 pages)

### Réalisations
- Prototype fonctionnel
- PCB assemblé
- Boîtier (optionnel)
- Démonstration

### Présentation
- Support PowerPoint/PDF
- Poster A1
- Vidéo de démonstration
- Soutenance orale

## 🔗 Liens avec les cours

- **ER (S3)** : Conception électronique
- **IE (S3)** : Programmation embarquée
- **Énergie** : Convertisseurs
- **SE** : Traitement du signal
- **OL** : Outils de simulation

## 📖 Compétences développées

- Gestion de projet technique
- Conception électronique complète
- Design de PCB professionnels
- Simulation multi-domaines
- Tests et validation systématiques
- Débogage méthodique
- Documentation technique
- Travail en équipe
- Présentation de résultats

## 💡 Exemples de projets réalisés

### Station météo connectée
- Capteurs T°, P, humidité, vent
- Acquisition STM32
- Affichage LCD
- Enregistrement sur SD
- Transmission WiFi
- Interface web
- Autonomie solaire

### Convertisseur DC/DC bidirectionnel
- 12V ↔ 48V
- Puissance 100W
- Contrôle numérique
- Synchronous rectification
- Efficacité >90%
- Protection complète

### Analyseur de protocole I2C/SPI
- Capture haute vitesse
- FPGA pour décodage
- Affichage LCD
- Mémoire tampon
- Interface USB
- Logiciel PC

## ⚠️ Pièges à éviter

### Spécifications
- Cahier des charges trop vague
- Objectifs irréalistes
- Sous-estimation de la complexité

### Conception
- Choix de composants obsolètes
- Négliger les marges de sécurité
- Oublier les protections
- Découp lage insuffisant

### PCB
- Routage trop serré
- Vias insuffisants (masse)
- Pas de points de test
- Oubli de composants de débogage

### Planning
- Démarrage tardif
- Pas de jalons intermédiaires
- Délais de fabrication sous-estimés
- Tests à la dernière minute

## 🎯 Critères d'évaluation

- Respect du cahier des charges (20%)
- Qualité de la conception (25%)
- Réalisation PCB (20%)
- Tests et validation (15%)
- Documentation (10%)
- Soutenance et démo (10%)

## 📚 Méthodologie recommandée

### Organisation
- Réunions hebdomadaires
- Répartition des tâches
- Outils collaboratifs (Git, Trello)
- Revues de conception

### Gestion des risques
- Identifier risques techniques
- Plan B pour points critiques
- Tests progressifs
- Validation par étapes

### Documentation continue
- Cahier de laboratoire
- Wiki de projet
- Commentaires dans le code
- Photos et captures d'écran

## 🔧 Conseils pratiques

1. **Commencer tôt** : 15 semaines passent vite
2. **Valider par étapes** : Simulations avant PCB
3. **Prévoir du temps** : Fabrication, livraison, débogage
4. **Documenter en continu** : Pas tout à la fin
5. **Tester méthodiquement** : Bloc par bloc
6. **Communiquer** : Dans l'équipe et avec tuteur
7. **Avoir un plan B** : Backup pour fonctions critiques
8. **Soigner la démo** : Préparer scénarios de test

---
layout: default
title: "Étude et Réalisation (ER) - S3"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

# Étude et Réalisation (ER) - Semestre 3

---

## PART A - Présentation Générale du Cours

### Contexte et objectifs

Projet majeur S3 : conception et réalisation d'un **télémètre ultrasonique** intégrant électronique analogique (amplification, filtrage), numérique (VHDL/FPGA) et traitement du signal. Projet pluridisciplinaire mobilisant toutes les compétences GEII.

**Objectifs :**
- Concevoir système complet (specs → réalisation)
- Intégrer analogique + numérique + FPGA
- PCB multicouche professionnel
- Validation par tests et mesures
- Documentation technique complète

### Prérequis
- Électronique analogique (amplis, filtres)
- VHDL (FSM, compteurs)
- Conception PCB
- Traitement du signal

---

## PART B: EXPÉRIENCE, CONTEXTE ET FONCTION

### Système Télémètre Ultrasonique

**Principe :**
Mesure de distance par temps de vol d'ondes ultrasoniques (40 kHz typique).
Distance = (c × Δt) / 2, où c ≈ 340 m/s

**Architecture :**
```
[FPGA/CPLD] → [Driver] → [Transducteur TX]
                             ↓ ondes US
                          [Cible]
                             ↓ écho
[FPGA] ← [Comparateur] ← [Filtrage] ← [Ampli] ← [Transducteur RX]
   ↓
[Affichage LCD / UART]
```

### Module 1 : Chaîne d'émission

**Génération burst 40 kHz :**
- FPGA : compteur + diviseur de fréquence
- Burst : 8-10 cycles (200-250 µs)
- Driver push-pull (transistors ou pont H)
- Transducteur piézo 40 kHz (impédance ≈ 2kΩ)

**Électronique :**
- Ampli classe B ou D pour efficacité
- Protection (clamping diodes)
- Adaptation impédance

### Module 2 : Chaîne de réception

**Transducteur RX :**
- Même fréquence que TX (40 kHz)
- Signal faible (quelques mV)

**Préamplification :**
- Ampli instrumentation ou AOP faible bruit
- Gain : 40-60 dB
- Filtrage passe-bande 38-42 kHz (Sallen-Key ordre 2)

**Détection d'enveloppe :**
- Redresseur + filtrage RC
- Ou détecteur de crête (diode + hold capacitor)

**Comparateur à seuil :**
- Seuil réglable (potentiomètre ou DAC)
- Sortie TTL/CMOS → FPGA
- Hystérésis (Schmitt trigger) pour stabilité

### Module 3 : Traitement numérique VHDL

**FSM de contrôle :**
1. IDLE : attente commande
2. EMIT : génération burst TX
3. WAIT_ECHO : comptage temps (counter++)
4. ECHO_DETECTED : calcul distance
5. DISPLAY : mise à jour affichage

**Compteur temps de vol :**
- Horloge 1 MHz → résolution 1 µs
- Comptage entre fin burst et front montant écho
- Timeout si pas d'écho (3-5 m max)

**Calcul distance :**
- Distance (cm) = (Compteur × 340 m/s) / (2 × 10^4)
- Implémentation : division ou multiplication par constante

**Interface :**
- LCD 16×2 (affichage distance)
- UART (transmission PC)
- LEDs status

### Module 4 : Intégration PCB

**PCB 4 couches :**
- L1 : Analogique (amplis, filtres)
- L2 : GND plane
- L3 : Power planes (±12V, 5V, 3.3V)
- L4 : Numérique (FPGA, affichage)

**Règles de conception :**
- Séparation analog/digital (GND unique pont à 1 point)
- Découplage intensif
- Blindage zone RF si nécessaire
- Via stitching GND

**Alimentation :**
- Entrée 12V ou USB 5V
- Régulateurs linéaires (7805, 7812, 7912) ou à découpage
- Rail dual ±12V pour amplis
- 3.3V pour FPGA

---

## PART C: ASPECTS TECHNIQUES

### Réalisation pratique

**Phase 1 : Prototypage breadboard**
- Tests amplification et filtrage
- Validation génération 40 kHz
- Tests transducteurs
- Mesure portée

**Phase 2 : Simulation Proteus**
- Schéma complet
- Simulation analogique (filtres)
- Co-simulation VHDL/analogique si possible

**Phase 3 : Conception PCB (Altium/KiCad)**
- Schéma électrique complet
- Footprints composants
- Routage 4 couches
- DRC (Design Rule Check)
- Génération Gerber + BOM

**Phase 4 : Fabrication et assemblage**
- Fabrication PCB (3-7 jours)
- Soudure CMS (fer, air chaud ou four)
- Soudure traversants
- Inspection visuelle

**Phase 5 : Tests et validation**
- Tests alimentation (tensions, ondulations)
- Tests unitaires (étage par étage)
- Programmation FPGA
- Tests fonctionnels (mesures distances)
- Calibration si nécessaire

### Outils utilisés
- **Proteus** : Simulation
- **Quartus / Vivado** : VHDL
- **Altium / KiCad** : PCB
- **Oscilloscope** : Signaux analogiques
- **Analyseur logique** : Signaux numériques
- **Multimètre** : Tensions, continuités

---

## PART D: ANALYSE ET RÉFLEXION

### Évaluation

**Livrables (100%) :**
- Analyse et spécifications (10%)
- Schémas et simulations (20%)
- PCB conception (15%)
- Code VHDL et testbench (15%)
- Réalisation matérielle (20%)
- Tests et validation (10%)
- Rapport technique (10%)

**Critères qualité :**
- Fonctionnalité complète
- Qualité conception (schéma, PCB)
- Robustesse (tests, gestion erreurs)
- Documentation (clarté, complétude)

### Compétences acquises
- Gestion projet électronique complet
- Intégration analogique/numérique/FPGA
- Conception PCB multicouche professionnelle
- Traitement du signal pratique
- Tests et validation systématiques
- Documentation technique

### Applications métier
- Ingénieur conception électronique
- Chef de projet systèmes embarqués
- Ingénieur R&D capteurs/instrumentation
- Concepteur objets connectés

## 📚 Contenu du cours

### Projet Télémètre

#### Description du projet
Conception d'un télémètre ultrasonique intégrant :
- Génération de signaux ultrasoniques
- Émission et réception d'ondes
- Traitement du signal reçu
- Mesure de distance
- Affichage et interface utilisateur
- Logique de contrôle (VHDL/FPGA)

#### Architecture système
**Partie émission :**
- Générateur de signaux (40 kHz typique)
- Amplificateur de puissance
- Transducteur ultrasonique émetteur
- Contrôle de l'émission

**Partie réception :**
- Transducteur ultrasonique récepteur
- Préamplification faible bruit
- Filtrage passe-bande
- Détection d'enveloppe
- Comparateur à seuil

**Traitement numérique :**
- Comptage du temps de vol
- Calcul de distance
- Affichage (LCD, 7 segments)
- Interface UART (communication)

**Partie logique (VHDL) :**
- Contrôleur de séquence
- Génération de timing
- Gestion d'affichage
- Interface de communication

### Conception électronique

#### Amplification et conditionnement
- Amplificateurs d'instrumentation
- Filtres actifs (Butterworth, Chebyshev)
- AGC (Automatic Gain Control)
- Comparateurs rapides
- Circuits de protection

#### Génération de signaux
- Oscillateurs à quartz
- Synthèse de fréquences
- Burst generation
- Drivers de transducteurs

#### Alimentations
- Régulateurs linéaires et à découpage
- Gestion multi-tensions
- Découplage et filtrage
- Protection et surveillance

### Conception numérique VHDL

#### Architecture FPGA/CPLD
- Sélection du composant
- Contraintes de conception
- Synthèse et routage
- Configuration et programmation

#### Modules VHDL
- Machine à états (FSM)
- Compteurs et timers
- Diviseurs de fréquence
- Gestion d'affichage
- Interface série (UART)

#### Simulation et validation
- Testbench VHDL
- Simulation fonctionnelle
- Simulation temporelle
- Vérification timing

### Conception PCB avancée

#### Multicouches
- Stratégie de routage 4 couches
- Plans de masse et alimentation
- Via stitching
- Découplage optimisé

#### Considérations RF
- Impédance contrôlée (si nécessaire)
- Séparation analogique/numérique
- Routage différentiel
- Antennes et zones sensibles

#### DFM et DFT
- Design for Manufacturing
- Design for Test
- Points de test
- Accessibilité des composants

## 🛠️ Réalisation pratique

### Prototypage
- Simulation sous Proteus
- Tests sur breadboard
- Validation par sous-ensembles
- Mesures préliminaires

### Fabrication
- Génération fichiers Gerber
- Fabrication PCB professionnelle
- Réception et contrôle qualité
- Préparation à l'assemblage

### Assemblage
- Programmation FPGA/CPLD
- Soudure CMS et traversants
- Inspection visuelle
- Tests électriques

### Mise au point
- Tests unitaires par blocs
- Intégration progressive
- Calibration
- Optimisation des performances

## 💻 Outils utilisés

### CAO Électronique
- **Proteus ISIS/ARES** : Schémas et PCB
- **Altium Designer / KiCad** : PCB avancé
- **LTspice** : Simulation analogique

### VHDL et FPGA
- **Quartus Prime** : FPGA Intel/Altera
- **Vivado** : FPGA Xilinx
- **ModelSim** : Simulation VHDL

### Mesure et test
- Oscilloscope numérique
- Analyseur de spectre
- Générateur de fonctions
- Multimètre de précision

## 📊 Évaluation

- Conception (schémas, PCB, VHDL) (30%)
- Réalisation et assemblage (25%)
- Tests et performances (25%)
- Documentation technique (15%)
- Présentation (5%)

## 🔗 Liens avec d'autres cours

- **SE** : Traitement du signal
- **ENC** : Conception numérique VHDL
- **IE** : Programmation embarquée
- **Télécommunications** : Propagation des ondes
- **OL** : Documentation et CAO

## 📐 Spécifications techniques

### Performances visées
- Portée : 2 cm à 4 m
- Résolution : ±1 cm
- Fréquence ultrasons : 40 kHz
- Temps de rafraîchissement : <100 ms
- Alimentation : 5V ou 9V
- Consommation : <100 mA

### Contraintes
- Température de fonctionnement : 0-50°C
- Bruit ambiant à filtrer
- Réponses multiples (échos)
- Zones aveugles

## 💡 Défis techniques

### Électronique analogique
- Amplification à gain élevé stable
- Filtrage sélectif 40 kHz
- Réjection du bruit
- Dynamique du signal

### Numérique
- Précision du comptage
- Gestion des timeouts
- Synchronisation émission/réception
- Débouncing et antirebond

### Mécanique/Acoustique
- Positionnement des transducteurs
- Angle de détection
- Réflexions multiples
- Absorption selon les matériaux

## 📖 Compétences développées

- Conception de systèmes mixtes (analogique/numérique)
- Programmation VHDL pour FPGA
- Design de PCB professionnels
- Traitement du signal embarqué
- Tests et validation systématiques
- Gestion de projet technique
- Documentation professionnelle

## 🎯 Livrables du projet

### Documentation technique
1. Cahier des charges détaillé
2. Schémas électroniques commentés
3. Code VHDL documenté
4. Layout PCB avec nomenclature
5. Rapport de tests et mesures
6. Manuel d'utilisation

### Réalisations
- PCB fonctionnel assemblé
- FPGA/CPLD programmé
- Boîtier (optionnel)
- Démonstration vidéo

## ⚠️ Points d'attention

### Sécurité
- Attention aux tensions d'alimentation
- Protection des entrées sensibles
- Décharge statique (ESD)

### Qualité
- Soudures propres et fiables
- Vérifications systématiques
- Tests progressifs
- Documentation à jour

### Débogage
- Mesures systématiques
- Isolation des problèmes
- Utilisation de points de test
- Comparaison simulation/réalité

## 🔧 Méthode de travail

### Phase 1 : Étude (2 semaines)
- Recherche bibliographique
- Calculs théoriques
- Simulations préliminaires
- Choix des composants

### Phase 2 : Conception (3 semaines)
- Schématique complète
- Code VHDL
- Design PCB
- Validation simulations

### Phase 3 : Réalisation (3 semaines)
- Fabrication PCB
- Assemblage
- Programmation FPGA
- Tests unitaires

### Phase 4 : Validation (2 semaines)
- Tests d'intégration
- Mesures de performances
- Optimisations
- Documentation finale

## 📚 Ressources

- Datasheets transducteurs ultrasoniques
- Application notes sur télémétrie
- Exemples VHDL de compteurs
- Normes PCB (IPC)
- Tutoriels Proteus/Quartus

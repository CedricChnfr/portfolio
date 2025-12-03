---
layout: default
title: "Quadcopter Design and Development"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
---

[← Back to Academic Project](./my-projects.html)

# Introduction
This comprehensive multidisciplinary project involved designing, building, and programming a functional quadcopter from scratch. The project integrated electronics (power systems, motor control, sensors), embedded programming (flight controller firmware, sensor fusion), control theory (PID tuning, stabilization), and mechanical design (frame, propulsion system). This synthesis project applied all skills acquired during the first year, culminating in a flying autonomous drone.

# Project Overview
Working in teams, we developed a complete quadcopter system capable of stable flight with multiple flight modes. The project spanned requirements definition, component selection, assembly, programming, PID tuning, and extensive flight testing. Safety protocols were paramount throughout all development phases.

## System Architecture

### Electronic Subsystems
**Power Management:**
- LiPo battery (3S or 4S, 2200+ mAh)
- Power Distribution Board (PDB)
- Voltage regulators (5V, 3.3V)
- Battery monitoring and protection
- Autonomy calculation and optimization

**Motor Control:**
- 4× Brushless DC motors
- 4× Electronic Speed Controllers (ESC)
- PWM control signals (1000-2000 μs)
- ESC calibration procedures
- Motor-propeller matching for efficiency

**Sensor Suite:**
- IMU (Inertial Measurement Unit):
  - 3-axis gyroscope (angular velocity)
  - 3-axis accelerometer (linear acceleration)
  - 3-axis magnetometer (compass heading)
- Barometer (altitude estimation)
- GPS module (position, velocity)
- Ultrasonic rangefinder (ground proximity)
- Telemetry radio link

### Flight Controller
**Hardware:**
- Microcontroller: STM32F4 or similar high-performance MCU
- Commercial options: Pixhawk, Naze32, F4 flight controller
- High-speed sensor sampling (>1 kHz)
- Multiple timer channels for ESC control
- Communication interfaces (UART, I2C, SPI)

**Firmware Options:**
- Betaflight (popular for racing/acro)
- Cleanflight (open-source, customizable)
- ArduPilot (feature-rich, autonomous missions)
- Custom firmware development

### Communication
**Radio Control:**
- RC transmitter/receiver (8+ channels)
- Protocols: SBUS, PPM, CRSF
- Range: 500+ meters
- Failsafe configuration

**Telemetry:**
- Real-time data downlink
- Battery voltage, GPS position, altitude
- MAVLink protocol standard
- Ground control station software


# Control System Design

## Mathematical Modeling
**6 Degree-of-Freedom Dynamics:**
- Translation: x, y, z position
- Rotation: roll (φ), pitch (θ), yaw (ψ)
- Forces and torques from four rotors
- Aerodynamic effects and disturbances

**Linearization:**
- Small-angle approximation for hover
- State-space representation
- Stability analysis

## PID Control Implementation
**Cascade Control Architecture:**
1. **Inner Loop (Rate Control):**
   - Fast response (~1 kHz)
   - Gyroscope feedback
   - Controls angular velocities

2. **Outer Loop (Angle Control):**
   - Slower response (~100 Hz)
   - Accelerometer/magnetometer feedback
   - Maintains desired attitude

**PID Tuning Process:**
- Start with low gains
- Increase P gain until oscillation
- Add D gain to dampen oscillations
- Add I gain to eliminate steady-state error
- Iterative testing and refinement

## Flight Modes
**Manual (Acro/Rate):**
- Direct angular velocity control
- No self-leveling
- For experienced pilots

**Stabilized (Angle):**
- Automatic self-leveling
- Maintains horizontal attitude
- Returns to level when sticks centered

**Altitude Hold:**
- Barometer-based altitude lock
- Automatic throttle adjustment
- Simplifies piloting

**Position Hold (GPS):**
- GPS-based position lock
- Resists wind drift
- Enables waypoint navigation

# Mechanical Design

## Frame Selection
**Materials:**
- Carbon fiber (strong, lightweight)
- Aluminum arms
- 3D printed mounts

**Configuration:**
- X or + frame geometry
- Size: 250mm to 450mm diagonal
- Center of gravity considerations
- Component mounting points

## Propulsion System
**Motor-Propeller Matching:**
- Thrust-to-weight ratio > 2:1 for acrobatics
- KV rating selection (RPM/volt)
- Propeller pitch and diameter
- Efficiency vs. performance tradeoffs

**Thrust Testing:**
- Bench measurements
- Power consumption analysis
- Efficiency curves
- Vibration assessment

# Development Process

## Phase 1: Design and Component Selection (3 weeks)
- Requirements specification
- Research and benchmarking
- Component selection and compatibility
- Budget planning
- CAD modeling (if custom parts)

## Phase 2: Assembly and Integration (3 weeks)
- Frame assembly
- Electronics installation and wiring
- Cable management (minimize vibration transmission)
- Weight distribution optimization
- Pre-flight electrical checks

## Phase 3: Configuration and Ground Testing (3 weeks)
- Flight controller setup and configuration
- Sensor calibration (accelerometer, magnetometer, gyro)
- ESC calibration
- Radio setup and failsafe configuration
- Motor direction verification
- Propeller-off testing of all functions

## Phase 4: Flight Testing and Tuning (3 weeks)
**Progressive Testing:**
1. Tethered hover test
2. Low-altitude hover (1m)
3. Basic maneuvers (forward, backward, turns)
4. Altitude testing
5. GPS and autonomous features

**Safety Protocols:**
- Propeller guards for initial tests
- Large open testing area
- Safety observer
- Emergency kill switch configured
- Pre-flight checklist every flight

**PID Tuning Flights:**
- Record flight data (logs)
- Analyze oscillations and response
- Adjust gains incrementally
- Retest after each change

# Testing Results

## Performance Metrics
Successfully achieved:
- Stable hover with minimal drift
- Responsive control across all axes
- Flight time: 8-12 minutes (depending on battery)
- Maximum altitude tested: 50m
- Smooth transitions between flight modes
- Reliable GPS hold and return-to-home

## Challenges Overcome
- Motor vibrations affecting sensors (solved with vibration dampers)
- PID oscillations (tuned through iterative testing)
- GPS acquisition time (antenna placement optimization)
- Battery voltage sag under load (appropriate C-rating selection)

# Safety and Regulations

## Safety Measures
- Pre-flight inspection checklist
- Emergency stop (kill switch) always accessible
- No flight with propellers until fully tested
- Eye protection during all tests
- Clear communication in team
- Weather conditions assessment

## Regulatory Compliance
- Drone registration (if >250g)
- Pilot training/certification requirements
- Insurance (liability coverage)
- Authorized flight zones
- Maximum altitude limit (150m)
- Privacy regulations compliance

# Conclusion
This project provided comprehensive hands-on experience in mechatronic system development, from initial concept through fully functional flying vehicle. We successfully integrated complex subsystems, developed robust control algorithms, and achieved stable autonomous flight. The iterative design-test-refine process taught valuable lessons in systematic engineering problem-solving and the critical importance of safety in unmanned aerial vehicle development.

The completed quadcopter demonstrates our ability to manage complex multidisciplinary projects and deliver functional engineered systems meeting real-world performance and safety requirements.

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

- Mener un projet technique complexe de A à Z
- Travailler en équipe sur un système complet
- Intégrer les connaissances multidisciplinaires
- Gérer un projet avec contraintes temps/budget
- Documenter et présenter un projet technique

## 📚 Aspects techniques

### Électronique
#### Alimentation et gestion de l'énergie
- Batteries LiPo (choix, caractéristiques)
- Système de distribution d'énergie (PDB)
- Régulateurs de tension (5V, 3.3V)
- Protection et monitoring batterie
- Autonomie et consommation

#### Contrôle des moteurs
- Moteurs brushless
- ESC (Electronic Speed Controllers)
- PWM et protocoles de commande
- Calibration des ESC
- Sécurités et failsafe

#### Capteurs
- IMU (Inertial Measurement Unit)
  - Gyroscope 3 axes
  - Accéléromètre 3 axes
  - Magnétomètre (compass)
- Baromètre (altitude)
- GPS (position)
- Capteur ultrason (proximité sol)
- Télémétrie

### Informatique embarquée
#### Flight Controller
- Choix du contrôleur (Pixhawk, Naze32, F4, etc.)
- Microcontrôleur (STM32 généralement)
- Firmware (Betaflight, Cleanflight, ArduPilot)
- Configuration logicielle
- Modes de vol

#### Traitement des données capteurs
- Fusion de capteurs
- Filtrage (Kalman, complémentaire)
- Estimation d'attitude
- Stabilisation
- Navigation

#### Communication
- Protocoles radio (SBUS, PPM, CRSF)
- Telemetry (MAVLink)
- Interface configuration (MSP)
- FPV (optionnel)

### Automatique et contrôle
#### Modélisation
- Modèle dynamique du quadricoptère
- 6 degrés de liberté
- Forces et moments
- Linéarisation autour d'un point

#### Asservissement
- Contrôle de l'attitude (roll, pitch, yaw)
- PID (réglage des gains)
- Contrôle en cascade
- Stabilité du système

#### Modes de vol
- Manuel (Acro)
- Stabilisé (Angle mode)
- Altitude hold
- Position hold (GPS)
- Waypoints (optionnel)

### Mécanique
#### Structure
- Frame (châssis)
- Matériaux (fibres de carbone, etc.)
- Poids et centre de gravité
- Protection des composants

#### Propulsion
- Choix moteurs/hélices
- Rapport poussée/poids
- Couple et vibrations
- Efficacité propulsive

## 🛠️ Réalisation du projet

### Phase 1 : Étude et conception (3 semaines)
**Activités :**
- Recherche documentaire
- Définition des spécifications
- Choix des composants
- Estimation budgétaire
- Schémas et architecture

**Livrables :**
- Cahier des charges
- Liste de composants
- Schémas électroniques
- Planning prévisionnel

### Phase 2 : Assemblage et intégration (3 semaines)
**Activités :**
- Assemblage de la structure
- Câblage électronique
- Montage des composants
- Vérifications électriques
- Premiers tests au sol

**Livrables :**
- Drone assemblé
- Tests de continuité
- Calibrations préliminaires

### Phase 3 : Configuration et tests (3 semaines)
**Activités :**
- Configuration du flight controller
- Calibration des capteurs
- Réglage des PID
- Tests progressifs (sol → vol)
- Optimisations

**Livrables :**
- Configuration logicielle documentée
- Résultats de tests
- Vidéos de vol

### Phase 4 : Finalisation et présentation (2 semaines)
**Activités :**
- Finitions mécaniques
- Documentation complète
- Préparation de la présentation
- Démonstrations de vol
- Bilan du projet

**Livrables :**
- Drone fonctionnel
- Rapport technique complet
- Documentation utilisateur
- Présentation orale
- Vidéo démonstrative

## 💻 Outils utilisés

### Logiciels
- **Betaflight Configurator / Mission Planner** : Configuration FC
- **Proteus** : Schémas électroniques (si circuits custom)
- **SolidWorks / Fusion 360** : Conception 3D (supports)
- **MATLAB/Python** : Simulations de contrôle

### Équipements
- Station de soudage
- Multimètres et testeurs
- Chargeur de batteries LiPo
- Émetteur RC (radiocommande)
- Ordinateur de configuration

## 📊 Évaluation

- Gestion de projet et organisation (20%)
- Réalisation technique (30%)
- Fonctionnalité et performances (20%)
- Documentation (20%)
- Présentation orale (10%)

## 🔒 Sécurité

### Règles essentielles
- **JAMAIS** tester avec hélices en intérieur sans protection
- Protection des yeux obligatoire lors des tests
- Zone de test sécurisée et dégagée
- Respect de la réglementation sur les drones
- Procédure d'arrêt d'urgence (kill switch)
- Batterie débranchée lors des manipulations

### Réglementation
- Déclaration du drone (selon poids)
- Formation pilote (si >250g)
- Assurance responsabilité civile
- Zones de vol autorisées
- Altitude maximale 150m
- Respect de la vie privée

## 🎯 Défis techniques

### Principaux challenges
1. **Équilibrage** : Centre de gravité et répartition des masses
2. **Vibrations** : Filtrage et isolation des capteurs
3. **Stabilité** : Réglage des PID
4. **Autonomie** : Optimisation énergie/performances
5. **Fiabilité** : Gestion des pannes et failsafe

### Problèmes courants
- Oscillations lors du vol
- Dérive (drift)
- Décalibration des capteurs
- Interférences électromagnétiques
- Problèmes de portée radio

## 🔗 Liens avec les cours

- **ER** : Circuits électroniques, PCB
- **IE** : Programmation embarquée, capteurs
- **Énergie** : Motorisation, batteries
- **Automatique** : Asservissement PID
- **Prog** : Traitement de données
- **Physique** : Mécanique du vol

## 📖 Compétences développées

### Techniques
- Conception de systèmes complexes
- Intégration multidisciplinaire
- Programmation de systèmes embarqués
- Asservissement et régulation
- Diagnostic et résolution de problèmes

### Gestion de projet
- Planification et organisation
- Travail en équipe
- Gestion des ressources
- Respect des délais
- Communication

### Documentation
- Rédaction technique
- Schémas et diagrammes
- Manuel utilisateur
- Présentation professionnelle

## 💡 Conseils pratiques

### Conception
- Commencer simple, complexifier progressivement
- Prévoir des marges (poids, puissance)
- Penser à la maintenance et aux réparations
- Documenter tous les choix

### Réalisation
- Tester chaque sous-système séparément
- Câblage propre et organisé
- Étiquetage des connexions
- Photos à chaque étape

### Tests
- Progressivité : tests au sol avant de voler
- Hélices enlevées pour les premiers tests moteurs
- Zone de test sécurisée
- Toujours un plan B

## 📚 Ressources

### Documentation
- Datasheets des composants
- Documentation firmware (Betaflight, etc.)
- Forums communautaires (Oscar Liang, RCGroups)
- Chaînes YouTube techniques

### Communauté
- Forums FPV et drones
- Clubs de modélisme
- Groupes Facebook spécialisés
- Discord communities

## 🎓 Résultats attendus

### Fonctionnalités minimales
- Décollage et atterrissage contrôlés
- Stabilisation en vol stationnaire
- Déplacements contrôlés (avant/arrière, gauche/droite)
- Rotations (yaw)
- Autonomie minimum 5 minutes

### Fonctionnalités avancées (bonus)
- Hold d'altitude
- Retour automatique au point de départ (RTH)
- Enregistrement télémétrie
- FPV avec caméra
- Modes de vol avancés

## 🏆 Valorisation du projet

Ce projet peut être :
- Présenté lors de forums et salons
- Utilisé pour le portfolio personnel
- Démonstré lors de journées portes ouvertes
- Point fort dans le CV
- Base pour des projets personnels futurs

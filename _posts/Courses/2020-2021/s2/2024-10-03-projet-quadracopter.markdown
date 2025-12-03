---
layout: default
title: "Projet Tuteuré: Quadracopter - S2"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
---

# Projet Tuteuré: Quadracopter - Semestre 2

## 📋 Description du projet

Projet multidisciplinaire de conception et réalisation d'un quadricoptère (drone à 4 hélices). Ce projet intègre l'électronique, l'informatique embarquée, l'automatique et la mécanique, permettant d'appliquer l'ensemble des compétences acquises durant la première année de DUT.

## 🎯 Objectifs pédagogiques

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

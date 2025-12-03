---
layout: default
title: "Circuits Hyperfréquences - S3"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

# Circuits Hyperfréquences - Semestre 3

---

## PART A - Présentation Générale du Cours

### Contexte et objectifs

Ce cours de S3 spécialisation ENOC introduit la conception de circuits fonctionnant aux fréquences RF et micro-ondes (100 MHz - 10+ GHz). Il combine théorie électromagnétique, simulation EM 3D et réalisation pratique sur PCB, avec caractérisation par analyseur de réseau vectoriel.

**Objectifs principaux :**
- Maîtriser les technologies de circuits RF planaires (microstrip, stripline, CPW)
- Concevoir filtres, adaptations d'impédance, diviseurs de puissance
- Simuler avec outils EM professionnels (ADS Momentum, HFSS, CST)
- Fabriquer sur PCB et mesurer avec VNA
- Comprendre phénomènes HF : effet de peau, pertes diélectriques, couplages

### Prérequis
- Propagation et Hyperfréquences S3 (lignes de transmission, Smith chart, paramètres S)
- Électronique analogique (composants passifs, filtrage)
- Conception PCB (ER S1-S2)

---

## PART B: EXPÉRIENCE, CONTEXTE ET FONCTION

### Module 1 : Technologies RF sur PCB

**Substrats RF :**
- FR-4 : εr≈4.3-4.7, tan δ≈0.02, économique, limité <3 GHz
- Rogers RO4003/RO4350 : εr stable (3.38/3.48), faibles pertes, 0-10+ GHz
- PTFE/Téflon : εr≈2.1, très faibles pertes, difficile à usiner

**Lignes microstrip :**
- Calcul largeur pour Z₀=50Ω : W≈3mm (FR-4 1.6mm), εr_eff≈3.2
- Pertes : conducteur (cuivre) + diélectrique (tan δ)
- Applications : alimentations, adaptations

**Composants passifs RF :**
- Résistances 50Ω (charges, atténuateurs)
- Condensateurs RF CMS (résonance série SRF critique)
- Inductances (bobines air, CMS, facteur Q)
- Vias de masse (stitching λ/10)

### Module 2 : Circuits d'adaptation et filtres

**Réseaux d'adaptation localisés (L, π, T) :**
- Transformation impédance avec L/C CMS
- Calcul par Smith chart
- Bande étroite

**Adaptation distribuée :**
- Stub simple (série/parallèle) : position et longueur
- Ligne λ/4 : $Z_{\lambda/4} = \sqrt{Z_1 \cdot Z_2}$
- Double stub : positions fixes 3λ/8

**Filtres microstrip :**
- Passe-bas/haut/bande à éléments localisés
- Filtres à stubs (bande-stop)
- Filtres à lignes couplées (passe-bande)
- Synthèse : Butterworth, Chebyshev

**Coupleurs et diviseurs :**
- Diviseur Wilkinson : division égale, isolation, résistance 100Ω
- Coupleur directionnel : couplage -3/-10/-20 dB
- Rat-race : 180° hybrid, 3λ/2 circonférence

### Module 3 : Simulation EM

**Logiciels professionnels :**
- ADS Momentum : 2.5D planar, rapide
- HFSS : 3D FEM, précis
- CST : 3D temps/fréquence
- Sonnet : 2.5D, gratuit version limitée

**Workflow simulation :**
1. Schématique circuit (calcul initial)
2. Layout PCB (dessin géométrie)
3. Simulation EM 3D (champs, courants)
4. Optimisation paramètres
5. Validation specs (S-parameters)

**Paramètres analysés :**
- S11 (adaptation), S21 (transmission)
- Champs E et H
- Courants de surface
- Pertes (conducteur, diélectrique, rayonnement)

---

## PART C: ASPECTS TECHNIQUES

### Projets pratiques

**Projet 1 : Filtre passe-bande 2.4 GHz**
- Specs : f₀=2.4 GHz, BW=200 MHz, IL<3 dB
- Topologie : lignes couplées ou stubs
- Simulation ADS → Layout → Fabrication PCB → Mesure VNA

**Projet 2 : Diviseur Wilkinson**
- Division 50Ω → 2×50Ω
- Lignes λ/4 à 70.7Ω
- Isolation >20 dB

**Projet 3 : Adaptation stub**
- Charge complexe ZL → 50Ω
- Calcul Smith chart
- Stub court-circuit ou ouvert

### Caractérisation VNA

**Calibration :**
- SOLT : Short, Open, Load, Thru
- TRL pour substrats spécifiques
- Kit de calibration précis

**Mesures :**
- Paramètres S (magnitude, phase)
- Smith chart impédance
- TDR (Time Domain Reflectometry)
- Comparaison simulation vs mesure

### Fabrication PCB RF

**Fichiers Gerber :**
- Couches cuivre (Top, Bottom)
- Plans de masse continus
- Drill (vias)
- Soldermask, Silkscreen

**Fabricants :**
- PCBWay, JLCPCB (économique)
- Eurocircuits (professionnel EU)
- Spécifier : substrat, épaisseur, εr, finition (ENIG recommandé RF)

---

## PART D: ANALYSE ET RÉFLEXION

### Évaluation
- Projets simulation + réalisation (60%)
- Mesures et rapports (25%)
- Examen théorique (15%)

### Compétences acquises
- Simulation EM 3D professionnelle
- Conception circuits RF planaires
- Utilisation VNA
- Optimisation performances RF
- Design for Manufacturing RF

### Applications industrielles
- Télécommunications (WiFi, 4G/5G, satellite)
- IoT (LoRa, Sigfox, Bluetooth)
- Radar automobile
- Instrumentation RF

## 📚 Contenu du cours

### Technologies de circuits RF

#### Substrats RF
**FR-4 :**
- εr ≈ 4.3-4.7 (variable)
- tan δ ≈ 0.02 (pertes élevées)
- Économique
- Limité à quelques GHz

**Rogers (RO4003, RO4350) :**
- εr stable (3.38, 3.48)
- tan δ faible (0.0027)
- Bon jusqu'à 10+ GHz
- Plus cher

**PTFE/Téflon :**
- εr ≈ 2.1-2.5
- tan δ très faible
- Hautes performances
- Difficile à usiner

#### Lignes de transmission sur PCB

**Microstrip :**
- Ligne sur face supérieure
- Plan de masse en dessous
- Facile à fabriquer
- Émissions rayonnées

**Stripline :**
- Ligne entre deux plans de masse
- Bien blindée
- PCB multicouche requis

**Coplanar waveguide (CPW) :**
- Plans de masse sur même face
- Bon pour composants CMS
- Bonne isolation

### Composants passifs RF

#### Résistances
- Charges 50Ω
- Atténuateurs
- Terminaisons
- Modèles hautes fréquences

#### Condensateurs
- Capacités de découplage
- Résonance série (SRF)
- ESL et ESR
- Condensateurs RF (ATC, AVX)

#### Inductances
- Bobines air
- Inductances CMS
- Facteur de qualité Q
- Auto-résonance

#### Vias
- Via de masse (stitching)
- Via thermique
- Inductance parasite
- Espacement recommandé

### Circuits d'adaptation

#### Réseaux L, π, T
- Composants localisés
- Calcul analytique
- Simulation (Smith chart)
- Réalisation CMS

#### Adaptation distribuée
- Stubs microstrip
- Lignes λ/4
- Multi-sections
- Large bande

### Filtres RF

#### Filtres à éléments localisés
- Passe-bas, passe-haut, passe-bande
- Butterworth, Chebyshev
- Transformation LC
- Réalisation CMS

#### Filtres distribués
- Filtres à stubs
- Filtres à lignes couplées
- Filtres interdigités
- Résonateurs

### Coupleurs et diviseurs

#### Coupleur directionnel
- Couplage -3dB, -10dB, -20dB
- Isolation
- Directivité
- Applications (mesure, feedback)

#### Diviseur de Wilkinson
- Division de puissance égale
- Isolation entre sorties
- Impédances 50Ω
- Résistance d'isolation

#### Rat-race (anneau hybride)
- Combineur/diviseur 180°
- 4 ports
- λg × 3/2 circonférence

### Oscillateurs RF

#### Oscillateurs à quartz
- Fréquence fixe précise
- Stabilité
- TCXO, OCXO

#### VCO (Voltage Controlled Oscillator)
- Fréquence variable
- PLL (Phase-Locked Loop)
- Plage d'accord
- Bruit de phase

### Amplificateurs RF

#### Classes d'amplification
- Classe A (linéaire)
- Classe B, AB (push-pull)
- Classe C (RF, non linéaire)
- Classe E, F (commutation)

#### Caractéristiques
- Gain (dB)
- P1dB (point de compression à 1dB)
- IP3 (point d'interception d'ordre 3)
- Facteur de bruit (NF)
- Stabilité (K-factor, µ)

## 🛠️ Projets pratiques

### Conception de composants RF

#### Projet 1 : Filtre passe-bande
- Spécifications (f0, BW, IL)
- Calcul et simulation
- Layout PCB
- Caractérisation

#### Projet 2 : Diviseur de puissance
- Wilkinson 50Ω
- Simulation EM
- Fabrication
- Mesure paramètres S

#### Projet 3 : Ligne d'adaptation
- Stub ou λ/4
- Dimensionnement
- Optimisation
- Tests sur VNA

### Simulation et conception

#### Étapes
1. **Calcul théorique** : Formules, Smith chart
2. **Simulation circuit** : Schématique
3. **Simulation EM** : Layout 3D
4. **Optimisation** : Tuning paramètres
5. **Génération Gerber** : Fabrication

### Fabrication

#### Méthodes
- **Gravure chimique** : Proto rapide
- **Fraiseuse CNC** : Précision
- **Fabrication professionnelle** : Production

#### Fichiers nécessaires
- Gerber (couches cuivre)
- Drill (perçages)
- Soldermask (vernis)
- Silkscreen (sérigraphie)

### Caractérisation

#### Mesures avec VNA
- Calibration (SOLT, TRL)
- Paramètres S (S11, S21)
- Smith chart
- Comparaison simulation/mesure

#### Paramètres mesurés
- Pertes d'insertion (IL)
- Pertes de retour (RL)
- Isolation
- Bande passante
- Impédance

## 💻 Outils utilisés

### Simulation RF
- **ADS (Advanced Design System)** : Keysight
- **AWR Microwave Office** : Cadence
- **Qucs** : Open source
- **LTspice** : Circuits RF

### Simulation EM
- **Momentum** : Intégré ADS (2.5D)
- **HFSS** : Ansys (3D)
- **CST Microwave Studio** : 3D
- **Sonnet** : 2.5D planar

### CAO PCB
- **Altium Designer**
- **KiCad** : Open source
- **Eagle**
- **PADS**

### Mesure
- **Analyseur de réseau vectoriel** (VNA)
- **Analyseur de spectre**
- **Générateur RF**
- **Oscilloscope haute fréquence**

## 📊 Évaluation

- Conception et simulation (25%)
- Réalisation PCB (25%)
- Caractérisation et mesures (30%)
- Rapport technique (15%)
- Présentation (5%)

## 🔗 Liens avec d'autres cours

- **Propagation et Hyperfréquences** : Théorie
- **ER** : Conception PCB
- **Antennes (S4)** : Systèmes rayonnants
- **OL** : Outils de simulation

## 📐 Exemples de dimensionnement

### Ligne microstrip 50Ω (FR-4, h=1.6mm)
- Largeur W ≈ 3 mm
- εr = 4.3
- εr_eff ≈ 3.2
- Z0 = 50Ω

### Stub λ/4 à 2.4 GHz
- λ0 = 125 mm
- λg = λ0/√εr_eff ≈ 70 mm
- Longueur stub ≈ 17.5 mm

### Diviseur Wilkinson 2.4 GHz
- Lignes λ/4 à 70.7Ω
- Résistance isolation 100Ω
- Impédance entrée/sorties 50Ω

## 💡 Règles de conception RF

### Layout PCB
- **Plans de masse** : Continus, via stitching
- **Largeur de piste** : Contrôlée (50Ω)
- **Courbures** : Rayon > 3× largeur
- **Espacement** : Éviter couplages parasites
- **Vias** : Minimiser sur lignes RF

### Découplage
- Condensateurs proches des composants
- Multiple valeurs (nF, µF)
- Via court vers masse
- Plans de masse séparés (analogique/numérique)

### Blindage
- Boîtier métallique si nécessaire
- Cloisons entre sections
- Absorption RF (ferrites, mousses)

## 📖 Compétences développées

- Simulation EM 3D
- Conception de circuits RF sur PCB
- Utilisation d'analyseur de réseau
- Optimisation de performances RF
- Fabrication de circuits micro-ondes
- Analyse de résultats de mesure

## 🎯 Phénomènes hautes fréquences

### Effet de peau
- Profondeur de pénétration δ
- Résistance AC > DC
- Dépend de la fréquence
- Cuivre argenté pour améliorer

### Pertes diélectriques
- tan δ du substrat
- Augmentent avec fréquence
- Chauffage du PCB
- Choix substrat crucial

### Couplages
- Couplage capacitif (E-field)
- Couplage inductif (H-field)
- Couplage par substrat
- Espacement et blindage

### Modes parasites
- Modes de cavité
- Résonances indésirables
- Rayonnement
- Via fencing pour mitiger

## ⚠️ Erreurs à éviter

### Conception
- Plans de masse discontinus
- Lignes d'impédance non contrôlée
- Transitions brusques (stubs, angles droits)
- Sous-estimation des pertes

### Fabrication
- Épaisseur cuivre non uniforme
- Gravure excessive ou insuffisante
- Désalignement des couches
- Qualité soudures CMS RF

### Mesure
- Calibration inadéquate
- Connecteurs mal serrés
- Câbles endommagés
- Gamme de fréquence incorrecte

## 🔧 Processus de conception typique

### Phase 1 : Spécifications
- Fréquence de travail
- Impédance (50Ω typique)
- Performances requises
- Contraintes (taille, coût)

### Phase 2 : Conception théorique
- Calculs analytiques
- Choix de topologie
- Simulation schématique
- Validation concept

### Phase 3 : Layout et EM
- Dessin PCB
- Simulation EM 3D
- Optimisation dimensions
- Vérification DRC

### Phase 4 : Fabrication
- Génération fichiers Gerber
- Choix fabricant
- Réception et inspection
- Assemblage CMS

### Phase 5 : Test
- Calibration VNA
- Mesures paramètres S
- Comparaison avec simulation
- Ajustements (tuning)

## 📚 Ressources

- Application notes fabricants (Mini-Circuits, Analog Devices)
- "Microwave Engineering" - Pozar
- "RF Circuit Design" - Bowick
- Tutoriels ADS/AWR
- Calculateurs en ligne (impédance, atténuation)

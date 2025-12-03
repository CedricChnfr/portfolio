---
layout: default
title: "Antennes et Propagation - S4"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

# Antennes et Propagation - Semestre 4

---

## PART A - Présentation Générale du Cours

### Contexte et objectifs

Conception, simulation et caractérisation d'antennes pour systèmes sans fil. Suite directe de Propagation-HF S3. Applications IoT, WiFi, 4G/5G, satellite.

**Objectifs :**
- Paramètres antennes (gain, diagramme, polarisation)
- Conception antennes (dipôle, patch, Yagi)
- Simulation EM (MMANA, CST, HFSS)
- Mesures chambre anéchoïque et VNA
- Bilans de liaison radio

### Prérequis
- Propagation-HF S3 (lignes, Smith, paramètres S)
- Circuits HF (adaptation)

---

## PART B: EXPÉRIENCE, CONTEXTE ET FONCTION

### Module 1 : Paramètres caractéristiques

**Diagramme de rayonnement :**
- 2D et 3D, lobe principal, lobes secondaires
- Ouverture -3dB, rapport avant/arrière

**Gain et directivité :**
- Directivité D (dBi) : concentration puissance
- Gain G = η × D (efficacité η)

**Polarisation :**
- Linéaire (H/V), circulaire (RHCP/LHCP)
- Rapport axial AR

**Impédance et adaptation :**
- Z = R + jX
- S11 < -10 dB souhaité
- TOS < 2

**Bande passante :**
- Bande d'adaptation, rayonnement, polarisation

### Module 2 : Types d'antennes

**Dipôle λ/2 :**
- Z ≈ 73Ω, gain 2.15 dBi
- Omnidirectionnel plan H

**Monopole λ/4 :**
- Plan de masse requis
- Z ≈ 36Ω
- WiFi, mobiles

**Patch rectangulaire :**
- Sur substrat (Rogers, FR-4)
- Compact, gain 6-8 dBi
- GPS, WiFi, télémétrie
- L ≈ λ_eff/2

**Yagi-Uda :**
- Réflecteur + directeurs
- Gain 6-17 dBi
- Directive, TV, radio

**Antennes large bande :**
- Log-périodique, spirale
- Rapport 10:1

### Module 3 : Propagation

**Modes :**
- Onde de sol, d'espace, ionosphérique
- Espace libre : équation de Friis

**Phénomènes :**
- Réflexion, diffraction, réfraction
- Absorption (pluie, végétation)
- Multi-trajets (fading)

**Modèles :**
- Espace libre, Okumura-Hata, COST-231
- Zone de Fresnel

---

## PART C: ASPECTS TECHNIQUES

### TP Simulation

**Logiciels :**
- MMANA-GAL (Yagi, méthode moments)
- CST Microwave Studio (3D)
- HFSS (FEM)

**Antennes simulées :**
- Dipôle, Yagi 3-5 éléments
- Patch rectangulaire
- Analyse S11, gain, diagramme

### TP Mesures

**Chambre anéchoïque :**
- Diagrammes rayonnement
- Gain absolu, polarisation

**VNA :**
- S11, impédance, TOS

### TP Bilan de liaison

**Radio Mobile :**
- Planification couverture
- Profil terrain (MNT)
- Liaison point-à-point

### Projet Antenne

**Réalisation complète :**
- Choix type (patch, Yagi)
- Dimensionnement + simulation
- Fabrication (PCB ou mécanique)
- Mesures et validation
- Documentation

---

## PART D: ANALYSE ET RÉFLEXION

### Évaluation
- TP simulation (25%)
- TP mesures (20%)
- Projet antenne (40%)
- Examen (15%)

### Compétences acquises
- Conception antennes RF
- Simulation EM professionnelle
- Mesures chambre anéchoïque et VNA
- Bilans de liaison radio
- Optimisation structures rayonnantes

### Applications
- Télécommunications (WiFi, 4G/5G, satellite)
- IoT (LoRa, Sigfox)
- GNSS (GPS, Galileo)
- RFID, radar

## 📚 Contenu du cours

### Fondamentaux des antennes

#### Paramètres caractéristiques

**Diagramme de rayonnement :**
- Représentation 2D et 3D
- Lobe principal
- Lobes secondaires
- Ouverture à -3dB
- Rapport avant/arrière (F/B)

**Directivité et gain :**
- Directivité D (dBi)
- Gain G (dBi)
- Efficacité η
- G = η × D

**Polarisation :**
- Linéaire (H, V)
- Circulaire (RHCP, LHCP)
- Elliptique
- Rapport axial (AR)

**Impédance d'entrée :**
- Partie réelle et imaginaire
- Adaptation 50Ω
- Bande passante d'adaptation
- TOS (SWR)

**Bande passante :**
- Bande d'adaptation (S11 < -10dB)
- Bande de rayonnement
- Bande de polarisation

#### Équation de Friis
$$P_r = P_t \cdot G_t \cdot G_r \cdot \left(\frac{\lambda}{4\pi d}\right)^2$$

- Puissance transmise/reçue
- Gains des antennes
- Distance
- Pertes en espace libre

### Types d'antennes

#### Antennes filaires

**Dipôle demi-onde (λ/2) :**
- Structure simple
- Impédance ≈ 73Ω
- Diagramme omnidirectionnel (plan H)
- Directivité 2.15 dBi

**Dipôle replié :**
- Impédance ≈ 300Ω
- Bande passante améliorée
- Utilisé en TV

**Monopole quart d'onde (λ/4) :**
- Nécessite plan de masse
- Impédance ≈ 36.5Ω
- Omnidirectionnel
- Utilisé en mobile, WiFi

**Antenne Yagi-Uda :**
- Éléments parasites (réflecteur, directeurs)
- Directive
- Gain 6-17 dBi
- TV, radioamateur

#### Antennes imprimées (patch)

**Patch rectangulaire :**
- Sur substrat diélectrique
- Compact et léger
- Alimentation (coaxiale, microstrip, fente)
- Gain 6-8 dBi
- Applications : GPS, WiFi, télémétrie

**Dimensions :**
- Longueur L ≈ λg/2
- Largeur W (influence impédance)
- Épaisseur substrat h
- Permittivité εr

**Avantages :**
- Fabrication PCB standard
- Faible profil
- Intégration facile
- Faible coût

**Inconvénients :**
- Bande passante étroite (2-5%)
- Efficacité moyenne
- Pertes diélectriques

#### Antennes large bande

**Antenne log-périodique :**
- Large bande (rapport 10:1)
- Gain modéré constant
- Encombrement important

**Antenne spirale :**
- Polarisation circulaire
- Large bande
- Applications militaires, GNSS

**Antenne biconique :**
- Ultra large bande
- Omnidirectionnelle
- Mesure et EMC

#### Antennes spéciales

**Antenne cornet :**
- Alimentée par guide d'onde
- Gain élevé (10-25 dBi)
- Micro-ondes, radar

**Réseau d'antennes (Array) :**
- Éléments multiples
- Déphasage contrôlé
- Balayage électronique
- Gain élevé

**Antenne RFID :**
- Proximité ou longue portée
- Polarisation circulaire souvent
- Bande UHF (865-868 MHz EU, 902-928 MHz US)

### Propagation des ondes

#### Modes de propagation

**Onde de sol :**
- Basses fréquences (VLF, LF, MF)
- Suit la courbure terrestre
- Atténuation croissante avec fréquence

**Onde de surface :**
- Contact avec le sol
- Faible portée
- AM radio

**Onde d'espace :**
- Directe + réfléchie
- Interférences (fading)
- VHF, UHF

**Onde ionosphérique :**
- Réflexion sur ionosphère
- HF (3-30 MHz)
- Longue distance
- Dépend heure/saison

#### Phénomènes de propagation

**Réflexion :**
- Sur sol, bâtiments, obstacles
- Coefficient de réflexion
- Multi-trajets

**Diffraction :**
- Contournement d'obstacles
- Zone de Fresnel
- Atténuation knife-edge

**Réfraction :**
- Changement de milieu
- Courbure du trajet
- Ducting atmosphérique

**Absorption :**
- Pluie (atténuation forte >10 GHz)
- Végétation
- Atmosphère (O2, H2O)

#### Modèles de propagation

**Espace libre :**
- Formule de Friis
- Ligne de vue (LOS)

**Okumura-Hata :**
- Environnement urbain
- 150 MHz - 1.5 GHz

**COST-231 :**
- Extension Okumura-Hata
- Jusqu'à 2 GHz

**Modèle à deux rayons :**
- Rayon direct + réfléchi
- Zone d'interférence

## 🛠️ Travaux pratiques

### TP Simulation d'antennes

**Logiciels utilisés :**
- MMANA-GAL (Yagi)
- CST Microwave Studio
- HFSS
- 4NEC2

**Antennes simulées :**
- Dipôle λ/2
- Yagi 3-5 éléments
- Patch rectangulaire
- Monopole sur plan de masse

**Paramètres analysés :**
- S11 (adaptation)
- Diagramme de rayonnement
- Gain et directivité
- Impédance d'entrée

### TP Mesures d'antennes

**Chambre anéchoïque :**
- Environnement sans réflexions
- Mesure de diagrammes
- Polarisation
- Gain absolu

**Mesure adaptation :**
- Analyseur de réseau (VNA)
- S11, TOS
- Impédance complexe

### TP Bilan de liaison

**Radio Mobile :**
- Logiciel de planification
- Modèle numérique terrain (MNT)
- Calcul de couverture
- Profil de liaison

**Scénarios étudiés :**
- Liaison point-à-point
- Couverture WiFi campus
- Liaison longue distance

### Projet Antenne

**Réalisation d'une antenne :**
- Choix du type (patch, Yagi, etc.)
- Dimensionnement théorique
- Simulation et optimisation
- Fabrication (PCB ou mécanique)
- Mesures et validation

## 💻 Outils utilisés

### Simulation EM
- **MMANA-GAL** : Antennes filaires (Yagi)
- **4NEC2** : Méthode des moments (NEC-2)
- **CST Microwave Studio** : 3D complet
- **HFSS** : FEM 3D
- **FEKO** : Large structures

### Planification radio
- **Radio Mobile** : Couverture et bilans
- **Google Earth** : Visualisation 3D
- **Splat!** : Open source propagation

### Mesure
- **Analyseur de réseau** : S11, impédance
- **Chambre anéchoïque** : Rayonnement
- **Analyseur de spectre** : Puissance rayonnée

## 📊 Évaluation

- Travaux pratiques (30%)
- Projet antenne (40%)
- Contrôle continu (15%)
- Examen final (15%)

## 🔗 Liens avec d'autres cours

- **Propagation et Hyperfréquences (S3)** : Fondements
- **Circuits Hyperfréquences** : Adaptation, alimentation
- **Télécommunications** : Systèmes de communication
- **ER** : Intégration antennes

## 📐 Formules de dimensionnement

### Dipôle λ/2
- Longueur physique : L ≈ 0.95 × λ/2
- Impédance : Z ≈ 73 + j42.5 Ω

### Patch rectangulaire
- Longueur : $L = \frac{c}{2f_r\sqrt{\varepsilon_{reff}}} - 2\Delta L$
- Largeur : $W = \frac{c}{2f_r}\sqrt{\frac{2}{\varepsilon_r + 1}}$

### Gain théorique
- Dipôle λ/2 : 2.15 dBi
- Patch : 6-8 dBi
- Yagi 3 éléments : 6-8 dBi
- Yagi 10 éléments : 13-15 dBi

## 💡 Applications pratiques

### Communications
- WiFi (2.4 GHz, 5 GHz)
- Bluetooth
- 4G/5G
- LoRa, Sigfox

### Navigation
- GPS, Galileo, GLONASS
- Antennes patch circulaires
- Polarisation circulaire

### Télédétection
- Radar
- Satellites
- Télémétrie

### RFID
- Proximité (13.56 MHz)
- Longue portée (UHF)
- Applications logistique

## 📖 Compétences développées

- Conception d'antennes
- Simulation électromagnétique
- Mesure et caractérisation
- Bilans de liaison radio
- Optimisation de structures rayonnantes
- Analyse de propagation

## 🎯 Bandes de fréquences courantes

| Bande | Fréquence | λ | Applications |
|-------|-----------|---|--------------|
| FM | 88-108 MHz | 2.8-3.4 m | Radio FM |
| VHF TV | 174-223 MHz | 1.3-1.7 m | TV analogique |
| UHF TV | 470-862 MHz | 35-64 cm | TNT |
| GSM 900 | 900 MHz | 33 cm | 2G mobile |
| GPS L1 | 1575 MHz | 19 cm | Navigation |
| DCS 1800 | 1800 MHz | 16.7 cm | 2G/4G mobile |
| WiFi 2.4G | 2.4 GHz | 12.5 cm | WiFi b/g/n |
| WiFi 5G | 5.8 GHz | 5.2 cm | WiFi a/n/ac |

## ⚠️ Pièges en conception

### Antennes patch
- Bande passante étroite
- Sensible à l'épaisseur substrat
- Pertes diélectriques à haute fréquence
- Rayonnement arrière

### Antennes filaires
- Plan de masse essentiel (monopole)
- Environnement influence performances
- Câble d'alimentation rayonne
- Effets de proximité

### Mesures
- Couplage mutuel entre antennes
- Réflexions en chambre
- Câbles et connecteurs (pertes)
- Adaptation impédance

## 🔧 Conseils pratiques

### Réalisation PCB
- Substrat bas εr pour patch (Rogers)
- Précision d'usinage importante
- Via de masse multiples
- Protection vernis si extérieur

### Tests terrain
- Hauteur d'antenne critique
- Dégagement zone de Fresnel
- Orientation et polarisation
- Mesure RSSI, SNR

### Optimisation
- Simulation avant fabrication
- Itérations de design
- Compromis gain/bande passante
- Coût vs performances

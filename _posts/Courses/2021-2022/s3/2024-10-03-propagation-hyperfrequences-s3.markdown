---
layout: default
title: "Propagation et Hyperfréquences - S3"
date:   2024-10-02 10:56:03 +0200
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

# Propagation et Hyperfréquences - Semestre 3

**Annee**: 2021-2022 | **Semestre**: 3 | **Type**: Technique

---

## PART A - Présentation Générale du Cours

### Contexte et objectifs

Fondements théoriques de la propagation électromagnétique et techniques hyperfréquences (>300 MHz). Base pour Circuits HF, Antennes S4 et conception RF.

**Objectifs :**
- Théorie lignes de transmission (coaxial, microstrip)
- Abaque de Smith (adaptation impédance graphique)
- Paramètres S (caractérisation circuits RF)
- Adaptation d'impédance (stubs, transformateurs λ/4)

### Prérequis
- Électromagnétisme de base
- Nombres complexes
- Circuits AC

---

## PART B: EXPÉRIENCE, CONTEXTE ET FONCTION

### Module 1 : Lignes de transmission

**Équations télégraphistes :**
- Impédance caractéristique : $Z_0 = \sqrt{L/C}$ (coaxial : 50Ω ou 75Ω)
- Constante de propagation : γ = α + jβ
- Vitesse de phase : vₚ = ω/β

**Coefficient de réflexion :**
$$\Gamma = \frac{Z_L - Z_0}{Z_L + Z_0}$$
- Γ = 0 : adaptation parfaite
- |Γ| = 1 : réflexion totale (court-circuit, circuit ouvert)

**TOS (Taux d'Ondes Stationnaires) :**
$$TOS = \frac{1 + |\Gamma|}{1 - |\Gamma|}$$
- TOS = 1 : adaptation parfaite
- TOS > 2 : mauvaise adaptation

**Types de lignes :**
- Coaxial : blindé, faibles pertes, flexible
- Microstrip : PCB, économique, compact
- Stripline : blindé entre plans de masse
- Guide d'onde : haute puissance, faibles pertes >10 GHz

### Module 2 : Abaque de Smith

**Principe :**
- Représentation graphique de Γ (plan complexe)
- Cercles résistance constante
- Cercles réactance constante
- Normalisation : z = Z/Z₀

**Opérations :**
- Lecture impédance (R + jX) ou admittance (G + jB)
- Déplacement sur ligne : rotation (λ/4 = 180°)
- Adaptation : ajout série (R/X) ou parallèle (G/B)

**Applications :**
- Design stubs (court-circuit ou ouvert)
- Transformateurs λ/4
- Analyse désadaptation

### Module 3 : Paramètres S

**Définition (réseau 2 ports) :**
$$\begin{bmatrix} b_1 \\ b_2 \end{bmatrix} = \begin{bmatrix} S_{11} & S_{12} \\ S_{21} & S_{22} \end{bmatrix} \begin{bmatrix} a_1 \\ a_2 \end{bmatrix}$$

- **S₁₁** : coefficient réflexion entrée (port 2 adapté)
- **S₂₁** : coefficient transmission (gain/atténuation)
- **S₂₂** : coefficient réflexion sortie
- **S₁₂** : transmission inverse (isolation)

**Mesure :**
- Analyseur de réseau vectoriel (VNA)
- Calibration SOLT (Short, Open, Load, Thru)

**Interprétation :**
- S₁₁ < -10 dB : bonne adaptation entrée
- S₂₁ en dB : gain (>0) ou pertes (<0)
- S₁₂ : isolation (idéalement très faible)

### Module 4 : Adaptation d'impédance

**Méthodes :**

1. **Stub simple :**
   - Stub parallèle (court-circuit ou ouvert)
   - Position : distance depuis charge
   - Longueur stub : calculée par Smith chart

2. **Transformateur λ/4 :**
   - Impédance : $Z_{\lambda/4} = \sqrt{Z_1 \cdot Z_2}$
   - Bande étroite

3. **Réseaux en L, π, T :**
   - Composants localisés (L, C)
   - Basse fréquence ou large bande

---

## PART C: ASPECTS TECHNIQUES

### TP Lignes et Smith chart

**TP1 : Mesure TOS**
- Ligne coaxiale 50Ω
- Charges : 50Ω (adaptée), court-circuit, ouvert, 75Ω
- Mesure TOS avec TOS-mètre

**TP2 : Adaptation par stub**
- Charge ZL = 100 + j50 Ω
- Calcul Smith chart : position et longueur stub
- Réalisation et mesure S₁₁ au VNA

**TP3 : Paramètres S**
- Mesure VNA d'un atténuateur 10 dB
- Mesure filtre passe-bande
- Analyse adaptation et transmission

### Projet adaptation

**Objectif :** Adapter antenne patch (ZL = 120 - j80 Ω) à 50Ω à 2.4 GHz

**Solutions comparées :**
- Stub simple microstrip
- Réseau en L (L + C CMS)
- Ligne λ/4 (intermédiaire)

**Critères :** S₁₁ < -15 dB, bande passante, simplicité

---

## PART D: ANALYSE ET RÉFLEXION

### Évaluation
- TP et rapports (40%)
- Projet adaptation (25%)
- Contrôles (20%)
- Examen final (15%)

### Compétences acquises
- Analyse lignes de transmission
- Utilisation abaque de Smith (calculs graphiques)
- Mesure VNA et paramètres S
- Conception adaptations d'impédance
- Fondements RF essentiels

### Applications professionnelles
- Conception circuits RF (matching networks)
- Antennes (adaptation)
- Instrumentation (VNA, analyseurs)
- Télécommunications (optimisation liaison)
- Impédance d'onde

#### Propagation en espace libre
- Atténuation en espace libre (FSPL)
- Formule de Friis
- Zone de Fresnel
- Ellipsoïde de Fresnel
- Horizon radio

#### Propagation dans les milieux
- Constante diélectrique
- Pertes diélectriques (tan δ)
- Profondeur de pénétration
- Effet de peau
- Matériaux RF (FR-4, Rogers, Téflon)

### Lignes de transmission

#### Théorie des lignes
- Équations des télégraphistes
- Impédance caractéristique Z0
- Constante de propagation γ
- Vitesse de phase
- Longueur d'onde guidée

#### Types de lignes
**Câble coaxial :**
- Structure et géométrie
- Impédance (50Ω, 75Ω)
- Atténuation
- Applications

**Ligne microstrip :**
- Circuit imprimé
- Calcul de largeur pour Z0
- Permittivité effective
- Pertes (conducteur, diélectrique)

**Stripline :**
- Ligne enterrée
- Meilleur blindage
- Moins de dispersion

**Guide d'onde :**
- Modes de propagation (TE, TM)
- Fréquence de coupure
- Dispersion

#### Paramètres S (Scattering parameters)
- S11, S21, S12, S22
- Mesure par analyseur de réseau
- Cascade de quadripôles
- Fichiers .s2p (Touchstone)

### Adaptation d'impédance

#### Coefficient de réflexion
- Définition : $\Gamma = \frac{Z_L - Z_0}{Z_L + Z_0}$
- Module et phase
- Taux d'onde stationnaire (TOS/SWR)
- Relation : $SWR = \frac{1+|\Gamma|}{1-|\Gamma|}$

#### Abaque de Smith
**Principe :**
- Représentation complexe de l'impédance
- Cercles de résistance constante
- Cercles de réactance constante
- Transformation en admittance
- Rotations (lignes λ/2, λ/4)

**Utilisation :**
- Lecture d'impédance
- Calcul de réflexion
- Détermination de SWR
- Conception d'adaptation

#### Techniques d'adaptation

**Stub simple (série ou parallèle) :**
- Ligne court-circuitée ou ouverte
- Position et longueur du stub
- Adaptation à une fréquence
- Smith chart pour dimensionnement

**Stub double :**
- Deux stubs en parallèle
- Adaptation large bande améliorée
- Positions fixes (3λ/8)

**Ligne quart d'onde (λ/4) :**
- Transformateur d'impédance
- $Z_{λ/4} = \sqrt{Z_1 \cdot Z_2}$
- Adaptation réelle vers réelle
- Bande passante limitée

**Réseau en L, π, T :**
- Composants localisés (L, C)
- Basses fréquences
- Filtrage intégré

### Circuits hyperfréquences

#### Composants passifs
- Résistances RF (charge 50Ω)
- Condensateurs RF (céramique, CMS)
- Inductances (air, ferrite)
- Transformateurs (balun)

#### Composants actifs
- Amplificateurs RF
- Mélangeurs
- Oscillateurs VCO
- Commutateurs RF

#### Dispositifs spéciaux
- Coupleurs directionnels
- Diviseurs de puissance (Wilkinson)
- Circulateurs et isolateurs
- Filtres passe-bande RF

## 🛠️ Travaux pratiques

### TP Abaque de Smith
- Manipulation de l'abaque
- Tracés d'impédances
- Calcul de réflexion et SWR
- Transformation par lignes

### TP Adaptation stub simple
- Conception sur Smith chart
- Calcul position et longueur
- Simulation LTspice ou ADS
- Réalisation et mesure

### TP Ligne quart d'onde
- Dimensionnement
- Simulation EM
- Réalisation sur PCB microstrip
- Mesure analyseur de réseau

### TP Paramètres S
- Mesure à l'analyseur de réseau
- Calibration (SOLT, TRL)
- Caractérisation composants
- Analyse de résultats

## 💻 Outils utilisés

### Simulation EM
- **LTspice** : Circuits RF
- **ADS (Advanced Design System)** : Conception RF/MW
- **CST Microwave Studio** : Simulation 3D EM
- **HFSS** : Simulation EM haute fréquence
- **Qucs** : Open source RF

### Outils graphiques
- **Smith Chart Tool** : Abaque interactif
- **AppCAD** : Calculs RF (Broadcom/Avago)
- **RF Toolbox (MATLAB)** : Calculs et simulations

### Mesure
- **Analyseur de réseau vectoriel (VNA)** : Paramètres S
- **Analyseur de spectre** : Analyse fréquentielle
- **Wattmètre RF** : Mesure de puissance
- **TDR (Time Domain Reflectometry)** : Diagnostic lignes

## 📊 Évaluation

- Travaux pratiques (40%)
- Projet d'adaptation (25%)
- Contrôles continus (20%)
- Examen final (15%)

## 🔗 Liens avec d'autres cours

- **Circuits Hyperfréquences (S3)** : Approfondissement
- **Antennes et Propagation (S4)** : Applications
- **Télécommunications** : Systèmes RF
- **ER** : Conception de circuits RF

## 📐 Formules essentielles

### Impédance caractéristique (coaxial)
$$Z_0 = \frac{60}{\sqrt{\varepsilon_r}} \ln\left(\frac{D}{d}\right)$$

### Largeur microstrip pour Z0
Formules empiriques selon h, εr, Z0

### Perte en espace libre (dB)
$$FSPL = 20\log_{10}(d) + 20\log_{10}(f) + 32.45$$
(d en km, f en MHz)

### Longueur d'onde
$$\lambda = \frac{c}{f\sqrt{\varepsilon_r}}$$

## 💡 Applications pratiques

### Communications
- Liaisons radio (2.4 GHz, 5 GHz)
- Téléphonie mobile (GSM, LTE, 5G)
- WiFi, Bluetooth
- RFID

### Radar
- Automobile (24 GHz, 77 GHz)
- Météorologie
- Aviation
- Maritime

### Instrumentation
- Analyseurs de réseau
- Générateurs RF
- Mesure sans contact

### Chauffage
- Micro-ondes domestiques (2.45 GHz)
- Soudage par induction
- Séchage industriel

## 📖 Compétences développées

- Utilisation de l'abaque de Smith
- Conception de circuits d'adaptation
- Simulation de circuits RF
- Mesure avec analyseur de réseau
- Calcul de bilans de liaison
- Dimensionnement de lignes de transmission

## 🎯 Bandes de fréquences

| Bande | Fréquence | Longueur d'onde | Applications |
|-------|-----------|-----------------|--------------|
| HF | 3-30 MHz | 100-10 m | Radio AM, amateur |
| VHF | 30-300 MHz | 10-1 m | FM, TV, aviation |
| UHF | 300 MHz - 3 GHz | 1 m - 10 cm | TV, GSM, GPS, WiFi |
| SHF | 3-30 GHz | 10-1 cm | Radar, satellite, 5G |
| EHF | 30-300 GHz | 10-1 mm | Millimétrique, imagerie |

## ⚠️ Pièges courants

### Conception
- Négliger les pertes diélectriques
- Mauvais choix de substrat
- Impédance mal contrôlée
- Couplages parasites

### Mesure
- Calibration inadéquate
- Connectique de mauvaise qualité
- Câbles endommagés
- Impédances de test incorrectes

### Adaptation
- Adaptation mono-fréquence vs large bande
- Pertes d'insertion
- Stabilité en température
- Sensibilité aux tolérances

## 🔧 Dimensionnement pratique

### Ligne microstrip 50Ω sur FR-4
- Épaisseur : 1.6 mm
- εr = 4.3
- Largeur ≈ 3 mm
- Impédance : 50Ω ± 10%

### Stub quart d'onde à 2.4 GHz
- λ0 = 12.5 cm
- λ/4 = 3.125 cm
- Sur FR-4 : λg/4 ≈ 1.5 cm

## 📚 Ressources

- "Microwave Engineering" - Pozar
- "RF Circuit Design" - Bowick
- Application notes fabricants (Analog Devices, Qorvo)
- Abaque de Smith interactif en ligne
- Tutoriels ADS/CST

---

## Documents de Cours

<div class="pdf-container">
  <div class="pdf-viewer">

    <div class="pdf-item">
      <h4>Cours Propagation - Chapitre 1</h4>
      <p>Fondements de la propagation electromagnetique : lignes de transmission, impedance caracteristique, coefficient de reflexion et TOS.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S3/Propagation/C1-Propagation_2020-21VF2.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S3/Propagation/C1-Propagation_2020-21VF2.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Cours Propagation - Chapitre 2</h4>
      <p>Approfondissement : abaque de Smith, parametres S, adaptation d'impedance et circuits hyperfrequences.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S3/Propagation/C2-Propagation_2021-22VFF.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S3/Propagation/C2-Propagation_2021-22VFF.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

  </div>
</div>

---

<style>body{font-family:Arial,sans-serif;background-color:#f4f4f9;color:#333;line-height:1.6}h2,h3,h4,h5{color:#2a7ae2}p{text-align:justify}code{background-color:#f5f5f5;padding:2px 6px;border-radius:3px;font-family:'Courier New',monospace}pre{background-color:#f5f5f5;padding:15px;border-radius:5px;overflow-x:auto}</style>

<div class="back-nav">
  <a href="./my-courses-2021-2022.html">&larr; Retour a Mes Cours 2021-2022</a>
</div>

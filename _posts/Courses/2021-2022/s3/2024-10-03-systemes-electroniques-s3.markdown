---
layout: default
title: "Systèmes Électroniques (SE) - S3"
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

# Systèmes Électroniques (SE) - Semestre 3

**Annee**: 2021-2022 | **Semestre**: 3 | **Type**: Technique

---

## PART A - Présentation Générale du Cours

### Contexte et objectifs

Traitement Numérique du Signal (TNS/DSP) appliqué aux systèmes électroniques : filtrage numérique, analyse spectrale FFT, et implémentation sur microcontrôleur/DSP. Fondement pour télécommunications et audio/vidéo.

**Objectifs :**
- Théorie échantillonnage et quantification
- Conception filtres numériques (FIR, IIR)
- Transformée de Fourier discrète (FFT)
- Implémentation DSP (MATLAB → C/STM32)

### Prérequis
- Signaux S2 (Fourier, Laplace)
- OL S3 (MATLAB, convolution)

---

## PART B: EXPÉRIENCE, CONTEXTE ET FONCTION

### Module 1 : Échantillonnage et quantification

**Théorème de Shannon :**
- Fréquence d'échantillonnage : fₛ ≥ 2·fmax
- Repliement spectral (aliasing) si fₛ trop faible
- Anti-aliasing : filtre passe-bas analogique avant ADC

**Quantification :**
- ADC N bits → 2ᴺ niveaux
- Pas de quantification : q = Vref / 2ᴺ
- Bruit de quantification : SNR ≈ 6.02N + 1.76 dB
- Exemple : ADC 12 bits → SNR ≈ 74 dB

### Module 2 : Filtres numériques

**Filtres FIR (Finite Impulse Response) :**
- Équation : y[n] = Σ bₖ·x[n-k]
- Stabilité : toujours stable
- Phase : phase linéaire possible (symétrie coefficients)
- Conception : fenêtrage (Hamming), Parks-McClellan

**Filtres IIR (Infinite Impulse Response) :**
- Équation récursive : y[n] = Σ bₖ·x[n-k] - Σ aₖ·y[n-k]
- Analogues numériques (Butterworth, Chebyshev, Elliptic)
- Transformations bilinéaire : s → 2(z-1)/(T(z+1))
- Ordre plus faible que FIR pour specs identiques
- Risque instabilité (pôles hors cercle unité)

**Comparaison :**
- FIR : phase linéaire, stable, ordre élevé
- IIR : ordre faible, phase non-linéaire, efficace

### Module 3 : Transformée de Fourier discrète

**DFT :**
$$X[k] = \sum_{n=0}^{N-1} x[n] e^{-j2\pi kn/N}, \quad k=0,1,...,N-1$$

**FFT (Fast Fourier Transform) :**
- Algorithme Cooley-Tukey : O(N log N) vs O(N²)
- N = 2ᵖ optimal (zéro-padding si besoin)
- MATLAB : `X = fft(x)`

**Applications :**
- Analyse spectrale (harmoniques, fréquences dominantes)
- Filtrage fréquentiel : FFT → multiplication → IFFT
- Compression (JPEG, MP3)
- Corrélation rapide

### Module 4 : Implémentation DSP

**Architectures :**
- Microcontrôleurs : STM32 (ARM Cortex-M4F avec FPU)
- DSP dédiés : TMS320 (Texas Instruments), SHARC (Analog Devices)
- FPGA : parallélisme, haute performance

**Optimisations :**
- Arithmétique virgule fixe (Q15, Q31) vs flottante
- CMSIS-DSP library (ARM) : fonctions optimisées assembleur
- DMA pour transferts ADC/DAC
- Buffer circulaire pour traitement temps réel

---

## PART C: ASPECTS TECHNIQUES

### TP MATLAB

**TP1 : Conception filtre FIR**
- Specs : passe-bas fc=1 kHz, fₛ=10 kHz, ordre 50
- Méthode fenêtrage (Hamming)
- Validation : réponse impulsionnelle, fréquentielle

**TP2 : Filtre IIR Butterworth**
- Ordre 4, fc=2 kHz
- Transformation bilinéaire
- Test sur signal bruité

**TP3 : Analyse FFT audio**
- Fichier WAV → FFT → spectre
- Identification notes musique
- Spectrogramme (FFT glissante)

### TP STM32

**TP Filtre temps réel :**
- ADC 10 kHz (DMA)
- Filtre FIR en C (coefficients de MATLAB)
- DAC sortie filtrée
- Mesure oscillo : comparaison entrée/sortie

### Projet DSP

**Égaliseur audio 3 bandes :**
- Entrée : ADC codec audio
- Filtres : passe-bas (<300 Hz), passe-bande (300 Hz - 3 kHz), passe-haut (>3 kHz)
- Gains réglables (potentiomètres)
- Sortie : DAC codec
- Interface : LCD + boutons

---

## PART D: ANALYSE ET RÉFLEXION

### Évaluation
- TP MATLAB (30%)
- TP STM32 (25%)
- Projet égaliseur (25%)
- Examen (20%)

### Compétences acquises
- Conception filtres numériques (FIR/IIR)
- Analyse fréquentielle (FFT)
- Programmation DSP temps réel
- Utilisation MATLAB/Python DSP
- Optimisation algorithmes embarqués

### Applications professionnelles
- Traitement audio/vidéo
- Télécommunications (modems, codecs)
- Instrumentation (oscilloscopes numériques)
- Radar et sonar
- IoT (capteurs intelligents)
- Formats de données (fixe, flottant)

#### Transformées

**Transformée de Fourier Discrète (TFD) :**
- Définition et propriétés
- DFT et FFT (Fast Fourier Transform)
- Algorithmes (Cooley-Tukey, radix-2)
- Applications (analyse spectrale)
- Fenêtrage (Hamming, Hanning, Blackman)

**Transformée en Z :**
- Définition et région de convergence
- Propriétés
- Transformée inverse
- Lien avec Laplace
- Fonction de transfert numérique

### Filtrage Numérique

#### Filtres RII (Réponse Impulsionnelle Infinie)
- Structure et équations
- Fonction de transfert en Z
- Stabilité et pôles
- Synthèse de filtres (Butterworth, Chebyshev, Elliptique)
- Transformation bilinéaire
- Structures de réalisation (directe, cascade, parallèle)

#### Filtres RIF (Réponse Impulsionnelle Finie)
- Structure FIR
- Phase linéaire
- Fenêtrage
- Méthode des moindres carrés
- Algorithme de Parks-McClellan
- Comparaison RII/RIF

#### Conception de filtres
- Spécifications (bande passante, atténuation)
- Choix RII vs RIF
- Ordre du filtre
- Quantification des coefficients
- Effets de la précision finie

### Systèmes de communication numériques

#### Modulation numérique (introduction)
- ASK, FSK, PSK
- Constellation et espace des signaux
- Probabilité d'erreur
- Rapport signal/bruit

#### Codage de canal
- Détection d'erreurs (parité, CRC)
- Correction d'erreurs (Hamming, Reed-Solomon)
- Codage convolutif
- Entrelacement

#### Synchronisation
- Synchronisation d'horloge
- Synchronisation de phase (PLL)
- Récupération de porteuse
- Synchronisation de trame

### Architectures de traitement

#### Processeurs DSP
- Architecture dédiée traitement signal
- MAC (Multiply-Accumulate)
- Unité arithmétique spécialisée
- Pipeline et parallélisme
- Mémoire et cache

#### Implémentation sur microcontrôleur
- ARM Cortex-M4F avec FPU
- Instructions SIMD
- Bibliothèques optimisées (CMSIS-DSP)
- DMA pour le traitement
- Contraintes temps réel

#### FPGA pour DSP
- Parallélisme massif
- IP cores DSP
- Pipeline profond
- Optimisation ressources

## 🛠️ Travaux pratiques

### TP Analyse spectrale
- FFT sur signaux réels
- Fenêtrage et effets
- Analyse de spectrogrammes
- Détection de fréquences

### TP Filtrage
- Implémentation de filtres RII et RIF
- Réponse fréquentielle mesurée
- Filtrage audio en temps réel
- Comparaison performances

### TP Systèmes de communication
- Simulation de modulations
- Codage/décodage CRC
- Canal bruité
- Taux d'erreur binaire (BER)

### Projet intégratif
- Système complet de traitement
- Acquisition → Filtrage → Analyse
- Sur microcontrôleur STM32
- Interface utilisateur

## 💻 Outils utilisés

### Simulation et conception
- **MATLAB/Simulink** : Simulation TNS
- **Python (NumPy, SciPy)** : Traitement signal
- **GNU Radio** : Systèmes de communication
- **Octave** : Alternative open source

### Développement embarqué
- **STM32CubeIDE** : Programmation microcontrôleur
- **CMSIS-DSP** : Bibliothèque optimisée
- **Audacity** : Analyse audio

### Mesure
- **Analyseur de spectre** : Analyse fréquentielle
- **Oscilloscope** : Signaux temporels
- **Carte son** : Acquisition audio

## 📊 Évaluation

- Travaux pratiques (35%)
- Projet de traitement signal (30%)
- Contrôles continus (20%)
- Examen final (15%)

## 🔗 Liens avec d'autres cours

- **Mathématiques** : Transformées et analyse
- **Signal (S1/S2)** : Bases théoriques
- **IE** : Implémentation embarquée
- **Télécommunications** : Applications communication
- **Filtrage Numérique (S4)** : Approfondissement

## 📐 Applications pratiques

### Audio
- Égaliseurs numériques
- Réduction de bruit
- Effets (reverb, delay, etc.)
- Compression audio
- Reconnaissance vocale

### Télécommunications
- Modems
- Codecs voix (GSM, VoIP)
- Récepteurs SDR (Software Defined Radio)
- Systèmes OFDM (WiFi, LTE)

### Instrumentation
- Analyseurs de spectre numériques
- Oscilloscopes numériques
- Acquisition de données
- Mesure et analyse

### Biomédical
- ECG, EEG
- Filtrage de signaux physiologiques
- Détection de caractéristiques
- Diagnostic assisté

## 💡 Concepts clés

### Échantillonnage
- Fréquence d'échantillonnage > 2 × Fmax
- Sur-échantillonnage
- Sous-échantillonnage
- Reconstruction du signal

### Quantification
- Résolution (nombre de bits)
- SNR quantification = 6.02n + 1.76 dB
- Dithering
- Formats numériques

### Stabilité des filtres
- Pôles dans le cercle unité
- Marge de stabilité
- Sensibilité aux coefficients
- Arithmétique finie

## 📖 Compétences développées

- Analyse fréquentielle de signaux
- Conception de filtres numériques
- Programmation DSP sur microcontrôleur
- Simulation de systèmes de communication
- Optimisation de code temps réel
- Validation expérimentale

## 🎯 Méthodologie de conception

### Spécifications
1. Définir les besoins (filtrage, analyse, etc.)
2. Contraintes (temps réel, précision, ressources)
3. Choix d'architecture (logicielle, matérielle)

### Conception
1. Simulation MATLAB/Python
2. Validation algorithme
3. Adaptation pour cible embarquée
4. Optimisation

### Implémentation
1. Portage sur microcontrôleur
2. Tests unitaires
3. Mesure de performances
4. Validation système

## ⚠️ Pièges courants

- Négliger le repliement spectral
- Sous-estimer les besoins en calcul
- Stabilité des filtres RII
- Débordements arithmétiques
- Latence de traitement
- Précision des coefficients

---

## Documents de Cours

<div class="pdf-container">
  <div class="pdf-viewer">

    <div class="pdf-item">
      <h4>Cours DDS (Direct Digital Synthesis)</h4>
      <p>Synthese numerique directe : principes, architecture DDS, generation de signaux et applications.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S3/SE/Cours_DDS_2020_Etudiant.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S3/SE/Cours_DDS_2020_Etudiant.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Cours Filtrage - Systemes Electroniques</h4>
      <p>Theorie et conception de filtres analogiques et numeriques : Butterworth, Chebyshev, FIR, IIR.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S3/SE/Cours_Filtrage_Etudiant_SE_2020.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S3/SE/Cours_Filtrage_Etudiant_SE_2020.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Cours Filtrage - Version Complete</h4>
      <p>Version complete du cours de filtrage avec corrections et exemples supplementaires.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S3/SE/Cours_Filtrage_Etudiant_SE_2020_prof.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S3/SE/Cours_Filtrage_Etudiant_SE_2020_prof.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Cours Oscillateurs Sinusoidaux</h4>
      <p>Etude des oscillateurs sinusoidaux : conditions d'oscillation, oscillateurs Wien, Colpitts, a quartz.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S3/SE/Cours_Oscillateurs_sinusoïdaux_Etudiant_2021sans_trous.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S3/SE/Cours_Oscillateurs_sinusoïdaux_Etudiant_2021sans_trous.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Cours PLL (Phase-Locked Loop)</h4>
      <p>Boucle a verrouillage de phase : principe, composants, applications en synthese de frequence et demodulation.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S3/SE/Cours_PLL_2021_sans_TROUS.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S3/SE/Cours_PLL_2021_sans_TROUS.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

  </div>
</div>

---

<style>body{font-family:Arial,sans-serif;background-color:#f4f4f9;color:#333;line-height:1.6}h2,h3,h4,h5{color:#2a7ae2}p{text-align:justify}code{background-color:#f5f5f5;padding:2px 6px;border-radius:3px;font-family:'Courier New',monospace}pre{background-color:#f5f5f5;padding:15px;border-radius:5px;overflow-x:auto}</style>

<div class="back-nav">
  <a href="./my-courses-2021-2022.html">&larr; Retour a Mes Cours 2021-2022</a>
</div>

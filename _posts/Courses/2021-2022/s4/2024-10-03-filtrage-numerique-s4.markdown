---
layout: default
title: "Filtrage Numérique - S4"
date:   2024-10-02 10:56:03 +0200
---

# Filtrage Numérique - Semestre 4

---

## PART A - Présentation Générale du Cours

### Contexte et objectifs

Approfondissement filtrage numérique (suite SE S3) avec implémentation temps réel sur STM32. Projet : filtre audio complet (conception MATLAB → code C optimisé → validation matérielle).

**Objectifs :**
- Synthèse filtres FIR/IIR avancés
- Implémentation DSP temps réel (virgule fixe/flottante)
- Optimisation performances (vitesse, mémoire)
- Analyse effets quantification
- Validation expérimentale

### Prérequis
- SE S3 (filtres FIR/IIR, FFT)
- IE S3 (STM32, DMA, ADC/DAC)
- Mathématiques (transformée en Z)

---

## PART B: EXPÉRIENCE, CONTEXTE ET FONCTION

### Module 1 : Conception filtres avancés

**Filtres IIR :**
- Butterworth, Chebyshev I/II, Elliptic
- Transformation bilinéaire : s → 2(z-1)/(T(z+1))
- Analyse stabilité (pôles cercle unité)
- MATLAB : `butter()`, `cheby1()`, `ellip()`

**Filtres FIR optimaux :**
- Parks-McClellan (equiripple)
- Fenêtrage avancé (Kaiser, Blackman-Harris)
- Phase linéaire
- MATLAB : `firpm()`, `fir1()`

**Structures de réalisation :**
- Direct Form I/II
- Cascade (sections ordre 2)
- Parallèle
- Trade-off : précision vs complexité

### Module 2 : Arithmétique virgule fixe

**Formats Qm.n :**
- Q15 : 1 bit signe + 15 bits fraction ([-1, 1))
- Q31 : 1 + 31 bits
- Multiplication : Q15 × Q15 = Q30 → shift >>15

**Quantification :**
- Troncature vs arrondi
- Saturation (clipping)
- Overflow detection

**Effets :**
- Bruit de quantification coefficients
- Bruit calcul (accumulation)
- Limit cycles (oscillations)
- SQNR (Signal-to-Quantization-Noise Ratio)

### Module 3 : Implémentation temps réel STM32

**Architecture :**
- ADC → DMA circular buffer → Filtre → DAC
- Interruption DMA half/full
- Double buffering

**Optimisations :**
- CMSIS-DSP : `arm_fir_q15()`, `arm_biquad_cascade_df1_f32()`
- Utilisation FPU (Cortex-M4F)
- Déroulage boucles (loop unrolling)
- Cache instruction

**Exemple FIR Q15 :**
```c
arm_fir_instance_q15 S;
q15_t coeffs[NUM_TAPS];
q15_t state[BLOCK_SIZE + NUM_TAPS - 1];

arm_fir_init_q15(&S, NUM_TAPS, coeffs, state, BLOCK_SIZE);
arm_fir_q15(&S, input, output, BLOCK_SIZE);
```

---

## PART C: ASPECTS TECHNIQUES

### Projet Filtre Audio

**Phase 1 : Conception MATLAB**
- Specs : passe-bande 300 Hz - 3.4 kHz (téléphonie)
- Choix : IIR Butterworth ordre 4 (faible ripple)
- Cascade 2 sections ordre 2 (biquads)
- Simulation : réponse, stabilité
- Export coefficients → C header

**Phase 2 : Implémentation STM32**
- Codec audio I2S (STM32F4-Discovery)
- Fs = 48 kHz, 16 bits
- Filtre biquad cascade CMSIS-DSP
- Buffer 128 samples (2.67 ms latence)
- Charge CPU : <30%

**Phase 3 : Validation**
- Entrée : générateur sinusoïdes sweep
- Mesure réponse fréquentielle (oscillo FFT)
- Comparaison simulation vs mesure
- Tests signaux réels (voix, musique)

### TP Comparatif virgule fixe vs flottante

**Objectif :**
Comparer Q15 vs float32 pour même filtre.

**Métriques :**
- Temps exécution (µs)
- Précision (différence sortie)
- Taille code (bytes)
- Consommation (mA)

**Résultats typiques (Cortex-M4F) :**
- Q15 : plus rapide (SIMD), moins précis
- Float32 : FPU efficace, très précis
- Choix selon application (audio pro = float)

---

## PART D: ANALYSE ET RÉFLEXION

### Évaluation
- Conception MATLAB (20%)
- Implémentation STM32 (30%)
- Validation et mesures (20%)
- Rapport technique (20%)
- Examen (10%)

### Compétences acquises
- Synthèse filtres numériques professionnelle
- Programmation DSP temps réel optimisée
- Maîtrise arithmétique virgule fixe
- Validation expérimentale rigoureuse
- Utilisation bibliothèques CMSIS-DSP

### Applications
- Audio (effets, égaliseurs, codecs)
- Télécommunications (filtres adaptateurs)
- Instrumentation (filtres anti-aliasing)
- IoT (traitement signal embarqué)

## 📚 Contenu du cours

### Synthèse de filtres numériques

#### Filtres RII (IIR)

**Méthodes de synthèse :**

*Transformation bilinéaire :*
- Conversion analogique → numérique
- $s = \frac{2}{T}\frac{1-z^{-1}}{1+z^{-1}}$
- Préwarping : $\omega_d = \frac{2}{T}\tan\left(\frac{\omega_a T}{2}\right)$
- Conservation de la stabilité

*Design direct numérique :*
- Placement de pôles et zéros
- Optimisation itérative
- Contraintes de stabilité

**Types de filtres :**
- Butterworth (maximally flat)
- Chebyshev Type I (ondulations bande passante)
- Chebyshev Type II (ondulations bande atténuée)
- Elliptique (Cauer) - ondulations des deux côtés
- Bessel (phase linéaire)

**Structures de réalisation :**

*Forme directe I :*
```
y[n] = b0*x[n] + b1*x[n-1] + ... - a1*y[n-1] - a2*y[n-2] - ...
```
- Simple mais sensible à quantification

*Forme directe II (canonique) :*
- Moins de mémoire (N au lieu de 2N)
- Structure transposée plus stable

*Cascade (SOS - Second Order Sections) :*
- Sections du 2e ordre
- Meilleure stabilité numérique
- Plus robuste à quantification
- Recommandée pour implémentation

*Forme parallèle :*
- Décomposition en fractions partielles
- Erreurs ne se propagent pas
- Plus de calculs

#### Filtres RIF (FIR)

**Avantages :**
- Toujours stable
- Phase linéaire exacte possible
- Pas de feedback
- Moins sensible à quantification

**Méthodes de synthèse :**

*Fenêtrage :*
- Réponse idéale × fenêtre
- Fenêtres : rectangulaire, Hamming, Hanning, Blackman, Kaiser
- Compromis lobe principal/lobes secondaires

*Échantillonnage fréquentiel :*
- Spécifier H(k) aux points désirés
- IDFT pour obtenir h[n]

*Méthode des moindres carrés :*
- Minimisation erreur quadratique
- Weighted least-squares

*Parks-McClellan (Remez) :*
- Équiripple (ondulations égales)
- Optimale au sens de Chebyshev
- Contrôle précis des bandes

**Structures FIR :**
- Forme directe
- Forme transposée
- Exploitation symétrie (phase linéaire)
- Polyphase (pour décimation/interpolation)

### Implémentation sur microcontrôleur

#### STM32 avec FPU (Cortex-M4F)

**Bibliothèque CMSIS-DSP :**
- Fonctions optimisées ARM
- Filtres IIR : `arm_biquad_cascade_df1_f32()`
- Filtres FIR : `arm_fir_f32()`
- Support flottant et fixed-point
- Instructions SIMD

**Formats de données :**

*Virgule flottante (float32) :*
- Dynamique élevée
- Précision
- FPU accélère calculs
- Consommation énergétique

*Virgule fixe (Q15, Q31) :*
- Entiers avec point implicite
- Plus rapide sans FPU
- Moins de mémoire
- Attention saturation et débordement

#### Optimisations

**Code :**
- Déroulage de boucles (loop unrolling)
- Inline functions
- Utilisation registres
- Éviter divisions (remplacer par shifts si possible)

**Mémoire :**
- Buffers circulaires pour historique
- DMA pour transfert sans CPU
- Allocation statique vs dynamique
- Alignement mémoire

**Temps réel :**
- Latence système
- Fréquence d'échantillonnage
- Temps de calcul par échantillon
- Marge de sécurité (50% typique)

### Effets de quantification

#### Quantification des coefficients
- Sensibilité des pôles
- Filtres IIR plus sensibles
- Forme cascade robuste
- Échelle des coefficients

#### Bruit de quantification
- SNR de quantification : 6.02N + 1.76 dB
- Arrondi vs troncature
- Propagation dans le filtre

#### Débordement arithmétique
- Saturation
- Wraparound
- Scaling des signaux internes

#### Limit cycles (oscillations parasites)
- Zero-input limit cycles
- Overflow limit cycles
- Dépend de la structure

### Architectures avancées

#### Filtres adaptatifs
- LMS (Least Mean Squares)
- NLMS (Normalized LMS)
- RLS (Recursive Least Squares)
- Applications : ANC, égalisation

#### Bancs de filtres
- Analyse multirésolution
- Décomposition en sous-bandes
- Ondelettes (wavelets)
- Applications : compression audio

#### Filtres multirate
- Décimation (↓M)
- Interpolation (↑L)
- Conversion de fréquence d'échantillonnage
- Économie de calculs

## 🛠️ Travaux pratiques

### TP Conception de filtres

**Objectif :** Synthèse de filtres sous MATLAB

**Étapes :**
1. Spécifications (Fp, Fs, Ap, As)
2. Calcul d'ordre minimal
3. Synthèse coefficients
4. Simulation réponse
5. Analyse quantification

**Outils MATLAB :**
- `butter()`, `cheby1()`, `cheby2()`, `ellip()`
- `fir1()`, `fir2()`, `firpm()` (Parks-McClellan)
- `freqz()`, `zplane()`, `impz()`
- `fdatool` (Filter Design Tool)

### TP Implémentation temps réel

**Matériel :**
- Carte STM32 (Nucleo L432 ou similaire)
- Codec audio (I2S)
- Générateur de signaux
- Oscilloscope

**Projet :** Égaliseur audio 3 bandes
- Bande basse (< 300 Hz)
- Bande médium (300 Hz - 3 kHz)
- Bande aigüe (> 3 kHz)
- Gain réglable par bande
- Traitement temps réel

**Contraintes :**
- Fréquence échantillonnage : 48 kHz
- Latence < 10 ms
- Filtres IIR ordre 2 (biquad)
- DMA pour I2S

### Mini-projet : Filtre adaptatif

**Application :** Suppression d'écho ou de bruit

**Algorithme :**
- LMS (Least Mean Squares)
- Buffer d'entrée
- Mise à jour adaptive des coefficients
- Mesure de convergence

**Implémentation :**
- STM32 avec PlatformIO
- Bibliothèque CMSIS-DSP
- Tests avec signaux réels

## 💻 Outils utilisés

### Simulation et design
- **MATLAB** : Signal Processing Toolbox
- **Python** : SciPy (scipy.signal)
- **GNU Octave** : Alternative open source

### Développement embarqué
- **STM32CubeIDE** : IDE officiel ST
- **PlatformIO** : VS Code extension
- **CMSIS-DSP** : Bibliothèque optimisée
- **Keil MDK** : IDE ARM

### Test et validation
- **Oscilloscope** : Analyse temporelle
- **Analyseur de spectre** : FFT
- **Générateur de signaux**
- **Carte son PC** : Acquisition/génération

## 📊 Évaluation

- Travaux pratiques (35%)
- Mini-projet (30%)
- Contrôles de connaissances (20%)
- Examen pratique (15%)

## 🔗 Liens avec d'autres cours

- **SE (S3)** : Fondements filtrage numérique
- **OL (S3)** : Outils de simulation
- **IE (S3)** : Programmation embarquée
- **Signal** : Traitement du signal

## 📐 Exemple de calcul

### Filtre passe-bas Butterworth

**Spécifications :**
- Fp = 1 kHz (bande passante)
- Fs = 2 kHz (bande atténuée)
- Ap = 1 dB (ondulation max bande passante)
- As = 40 dB (atténuation min bande atténuée)
- Fe = 10 kHz (fréquence échantillonnage)

**Calcul ordre :**
```matlab
[n, Wn] = buttord(Fp/(Fe/2), Fs/(Fe/2), Ap, As);
% n = 5 (ordre minimal)
```

**Synthèse :**
```matlab
[b, a] = butter(n, Wn);
[sos, g] = tf2sos(b, a); % Cascade de biquads
```

### Calcul de latence

**Latence de groupe :**
- FIR ordre N : (N-1)/2 échantillons
- À Fe = 48 kHz, N=101 : latence ≈ 1 ms

**Latence système :**
- Buffers I/S
- Temps de calcul
- Autres traitements
- Objectif : < 10-20 ms (audio)

## 💡 Applications pratiques

### Audio
- Égaliseurs
- Effets (reverb, chorus)
- Noise gate
- Compresseur/limiteur
- Correcteur de salle

### Télécommunications
- Filtres de mise en forme
- Filtres adaptatifs (égalisation)
- Suppression d'écho
- Réduction de bruit

### Biomédical
- Filtrage ECG/EEG
- Détection QRS
- Extraction de features
- Diagnostic assisté

### Instrumentation
- Filtrage anti-repliement numérique
- Extraction de signal
- Détection de défauts
- Analyse vibratoire

## 📖 Compétences développées

- Synthèse de filtres numériques
- Programmation DSP embarqué
- Optimisation temps réel
- Analyse effets quantification
- Validation expérimentale
- Utilisation CMSIS-DSP

## 🎯 Structure typique biquad (IIR ordre 2)

### Équation aux différences
```
y[n] = b0*x[n] + b1*x[n-1] + b2*x[n-2] 
       - a1*y[n-1] - a2*y[n-2]
```

### Fonction de transfert
```
H(z) = (b0 + b1*z^-1 + b2*z^-2) / (1 + a1*z^-1 + a2*z^-2)
```

### Code C (CMSIS-DSP)
```c
arm_biquad_casd_df1_inst_f32 S;
float32_t pState[4*numStages];
float32_t pCoeffs[5*numStages]; // b0,b1,b2,a1,a2

arm_biquad_cascade_df1_init_f32(&S, numStages, 
                                 pCoeffs, pState);

// Dans la boucle temps réel :
arm_biquad_cascade_df1_f32(&S, pSrc, pDst, blockSize);
```

## ⚠️ Pièges courants

### Conception
- Ordre trop élevé (instabilité, calcul)
- Forme directe pour IIR ordre élevé
- Négliger effets quantification
- Spécifications irréalistes

### Implémentation
- Débordement arithmétique
- Accumulation d'erreurs
- Buffers mal dimensionnés
- Latence excessive

### Optimisation
- Sur-optimisation prématurée
- Négliger la lisibilité
- Tests insuffisants
- Validation uniquement simulation

## 🔧 Bonnes pratiques

### Design
1. Spécifications claires
2. Choix type filtre adapté
3. Structure robuste (cascade)
4. Simulation complète

### Code
1. Utiliser bibliothèques optimisées
2. Buffers circulaires
3. DMA pour I/O
4. Mesure temps d'exécution

### Test
1. Signaux synthétiques (sinusoïdes, chirp)
2. Signaux réels
3. Cas limites
4. Validation fréquentielle et temporelle

---
layout: default
title: "Outils Logiciels (OL) - S3"
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

# Outils Logiciels (OL) - Semestre 3

**Annee**: 2021-2022 | **Semestre**: 3 | **Type**: Scientifique

---

## PART A - Présentation Générale du Cours

### Contexte et objectifs

Cours transversal fournissant outils mathématiques et logiciels (MATLAB/Octave/Python) pour traitement du signal, télécommunications et systèmes. Application directe dans cours SE, Télécom, Automatique.

**Objectifs :**
- Calcul matriciel et résolution systèmes linéaires
- Convolution, corrélation, filtrage
- Transformée de Fourier (DFT, FFT)
- Modulations numériques (simulation)
- Traitement signaux réels

### Prérequis
- Programmation de base (S1)
- Mathématiques (matrices, complexes)

---

## PART B: EXPÉRIENCE, CONTEXTE ET FONCTION

### Module 1 : Calcul matriciel

**Opérations :**
- Addition, multiplication, transposition, inverse
- Déterminant, valeurs propres, vecteurs propres
- Résolution systèmes : Ax = b → x = A⁻¹b ou x = A\b (MATLAB)

**Applications :**
- Circuits électriques (lois de Kirchhoff)
- Systèmes d'équations différentielles
- Transformations géométriques

### Module 2 : Convolution et corrélation

**Convolution :**
- Définition : y[n] = x[n] * h[n] = Σ x[k]·h[n-k]
- Interprétation : réponse système LTI à entrée x[n]
- MATLAB : `y = conv(x, h)`
- Application : filtrage (h = réponse impulsionnelle)

**Corrélation :**
- Auto-corrélation : détection périodicité
- Inter-corrélation : similitude signaux
- MATLAB : `xcorr(x, y)`
- Application : radar, synchronisation

### Module 3 : Transformée de Fourier

**DFT/FFT :**
- Passage temps → fréquence : $X[k] = \sum_{n=0}^{N-1} x[n] e^{-j2\pi kn/N}$
- FFT : algorithme rapide O(N log N)
- MATLAB : `X = fft(x)`, `x = ifft(X)`

**Analyse spectrale :**
- Spectre amplitude : `abs(X)`
- Spectre phase : `angle(X)`
- Densité spectrale de puissance (PSD)
- Fenêtrage (Hamming, Hann) pour réduire fuites spectrales

**Applications :**
- Analyse harmoniques
- Conception filtres fréquentiels
- Compression (JPEG, MP3)

### Module 4 : Modulations

**Modulations analogiques (rappel) :**
- AM : y(t) = [1 + m·cos(2πfₘt)]·cos(2πfₚt)
- FM : y(t) = cos(2πfₚt + β·sin(2πfₘt))

**Modulations numériques :**
- ASK (Amplitude Shift Keying)
- FSK (Frequency Shift Keying)
- PSK (Phase Shift Keying) : BPSK, QPSK
- QAM (Quadrature Amplitude Modulation)

**Simulation MATLAB :**
```matlab
% BPSK
bits = randi([0 1], 1, 100);
symbols = 2*bits - 1;  % 0→-1, 1→+1
fc = 1e6; fs = 10e6;
t = 0:1/fs:length(symbols)/1000;
carrier = cos(2*pi*fc*t);
modulated = symbols .* carrier;
```

---

## PART C: ASPECTS TECHNIQUES

### TP MATLAB

**TP1 : Filtrage par convolution**
- Filtre passe-bas FIR (réponse impulsionnelle rectangulaire)
- Convolution avec signal bruité
- Comparaison temps vs fréquence

**TP2 : Analyse FFT**
- Signal composite (somme sinusoïdes)
- FFT et identification fréquences
- Fenêtrage et résolution fréquentielle

**TP3 : Modulations numériques**
- Génération BPSK, QPSK
- Canal bruité (AWGN)
- Démodulation et taux d'erreur binaire (BER)

**TP4 : Filtrage audio**
- Chargement fichier WAV
- Égaliseur 3 bandes (FFT, filtrage, IFFT)
- Export audio filtré

### Outils utilisés
- **MATLAB** (ou Octave gratuit)
- **Python** : NumPy, SciPy, Matplotlib
- **Simulink** : modélisation systèmes

---

## PART D: ANALYSE ET RÉFLEXION

### Évaluation
- TP et comptes-rendus (50%)
- Mini-projets (30%)
- Contrôle final (20%)

### Compétences acquises
- Maîtrise MATLAB/Octave pour ingénierie
- Traitement du signal pratique
- Simulation systèmes de communication
- Analyse fréquentielle
- Visualisation et interprétation résultats

### Liens interdisciplinaires
- **SE S3** : filtrage numérique, FFT
- **Télécommunications S3** : modulations
- **Automatique S3** : simulation systèmes
- **Télécom Num S4** : canal de transmission
- Produit de Kronecker

#### Systèmes linéaires
- Représentation matricielle (Ax = b)
- Résolution de systèmes
- Méthodes directes (Gauss, LU)
- Méthodes itératives (Jacobi, Gauss-Seidel)
- Conditionnement

#### Valeurs et vecteurs propres
- Définition et calcul
- Diagonalisation
- Décomposition spectrale
- Applications aux systèmes dynamiques
- Modes propres

#### Décompositions
- LU (Lower-Upper)
- QR (Gram-Schmidt)
- SVD (Singular Value Decomposition)
- Cholesky
- Applications

### Applications aux systèmes

#### Représentation d'état
- Matrices A, B, C, D
- Changement de base
- Commandabilité et observabilité
- Forme canonique

#### Stabilité
- Analyse par valeurs propres
- Critère de Routh-Hurwitz
- Lieu des racines
- Marges de stabilité

### Convolution

#### Convolution continue
- Définition mathématique
- Propriétés (commutativité, associativité)
- Interprétation graphique
- Produit de convolution

#### Convolution discrète
- Définition pour signaux échantillonnés
- Algorithme de calcul
- Convolution circulaire
- Applications au filtrage

#### Systèmes LTI
- Réponse impulsionnelle
- Réponse à un signal quelconque
- Caractérisation par h(t)
- Stabilité et causalité

### Transformée de Fourier

#### Série de Fourier
- Décomposition en série
- Coefficients de Fourier
- Spectre discret
- Convergence
- Phénomène de Gibbs

#### Transformée de Fourier
- Passage série → transformée
- Propriétés (linéarité, décalage, etc.)
- Transformée de fonctions usuelles
- Dualité temps-fréquence

#### Théorème de Parseval
- Conservation d'énergie
- Analyse spectrale
- Densité spectrale de puissance

#### Applications
- Analyse de circuits
- Filtrage fréquentiel
- Analyse de spectres
- Traitement du signal

### Modulation et Démodulation

#### Modulation d'amplitude (AM)
- Modulation DSB (Double SideBand)
- Modulation DSB-SC (Suppressed Carrier)
- Modulation SSB (Single SideBand)
- Spectre et bande passante
- Rendement énergétique

#### Modulation de fréquence (FM)
- Déviation de fréquence
- Indice de modulation
- Bande passante (règle de Carson)
- Spectre FM
- Applications (radio FM)

#### Modulation de phase (PM)
- Relation avec FM
- Excursion de phase
- Spectres

#### Démodulation
- Démodulation cohérente (produit)
- Détection d'enveloppe
- Démodulation FM (discriminateur, PLL)
- Récupération de porteuse

## 🛠️ Travaux pratiques

### TP Calcul matriciel
- Résolution de systèmes
- Calcul de valeurs propres
- Analyse de stabilité
- Diagonalisation

### TP Convolution
- Convolution de signaux
- Filtrage par convolution
- Réponse de systèmes LTI
- Visualisation graphique

### TP Transformée de Fourier
- Calcul de séries de Fourier
- Spectres de signaux
- FFT et analyse spectrale
- Fenêtrage

### TP Modulation/Démodulation
- Génération de signaux modulés
- Analyse spectrale
- Démodulation et récupération
- Simulation de canal bruité

## 💻 Outils utilisés

### Environnements de calcul
- **MATLAB** : Calcul scientifique
- **Octave** : Alternative open source
- **Python (NumPy, SciPy, Matplotlib)** : Traitement scientifique
- **Maple** : Calcul symbolique

### Bibliothèques
- **NumPy** : Calcul matriciel
- **SciPy** : Outils scientifiques
- **Matplotlib** : Visualisation
- **SymPy** : Calcul symbolique Python

### Outils de visualisation
- Tracés 2D et 3D
- Spectrogrammes
- Diagrammes de Bode
- Animations

## 📊 Évaluation

- Travaux pratiques MATLAB/Python (40%)
- Projets d'application (30%)
- Contrôles continus (20%)
- Examen final (10%)

## 🔗 Liens avec d'autres cours

- **Automatique** : Représentation d'état
- **SE** : Traitement du signal
- **Télécommunications** : Modulation
- **Mathématiques** : Fondements théoriques
- **Filtrage Numérique** : Implémentation

## 📐 Formules clés

### Convolution
- Continue : $(f * g)(t) = \int_{-\infty}^{+\infty} f(\tau)g(t-\tau)d\tau$
- Discrète : $(f * g)[n] = \sum_{k=-\infty}^{+\infty} f[k]g[n-k]$

### Transformée de Fourier
- Directe : $F(\omega) = \int_{-\infty}^{+\infty} f(t)e^{-j\omega t}dt$
- Inverse : $f(t) = \frac{1}{2\pi}\int_{-\infty}^{+\infty} F(\omega)e^{j\omega t}d\omega$

### Modulation AM
- Signal modulé : $s(t) = [1 + m(t)]A_c\cos(2\pi f_c t)$
- Indice : $\mu = \frac{A_{max} - A_{min}}{A_{max} + A_{min}}$

## 💡 Applications pratiques

### Traitement d'images
- Filtrage (convolution 2D)
- Compression (DCT, FFT)
- Restauration d'images

### Audio
- Égaliseurs (filtrage)
- Effets (convolution avec IR)
- Analyse spectrale

### Télécommunications
- Radio AM/FM
- Multiplexage fréquentiel
- Analyse de canaux

### Systèmes de contrôle
- Analyse de stabilité
- Commandabilité
- Synthèse de correcteurs

## 📖 Compétences développées

- Calcul matriciel appliqué
- Analyse fréquentielle de signaux
- Programmation scientifique (MATLAB/Python)
- Simulation de systèmes
- Visualisation de données
- Résolution numérique de problèmes
- Analyse spectrale

## 🎯 Exemples de projets

### Projet 1 : Analyse d'un système dynamique
- Modélisation matricielle
- Calcul des modes propres
- Simulation temporelle
- Analyse de stabilité

### Projet 2 : Égaliseur audio
- Analyse FFT en temps réel
- Filtrage par bandes
- Convolution avec filtres RIF
- Interface graphique

### Projet 3 : Simulateur de radio AM/FM
- Génération de signaux modulés
- Ajout de bruit
- Démodulation
- Mesure SNR et BER

## ⚠️ Points d'attention

### Calcul matriciel
- Conditionnement des matrices
- Précision numérique
- Stabilité des algorithmes
- Complexité algorithmique

### Convolution
- Support des signaux
- Causalité
- Complexité O(n²)
- Utiliser FFT pour grands signaux

### Transformées
- Fréquence d'échantillonnage
- Fenêtrage (leakage spectral)
- Résolution fréquentielle
- Aliasing

### Modulation
- Bande passante requise
- SNR et qualité
- Non-linéarités
- Interférences

## 🔧 Bonnes pratiques MATLAB/Python

### Vectorisation
```matlab
% Éviter les boucles
for i = 1:n
    y(i) = a * x(i) + b;
end

% Préférer
y = a * x + b;
```

### Préallocation
```matlab
% Inefficace
for i = 1:1000
    x(i) = i^2;
end

% Efficace
x = zeros(1, 1000);
for i = 1:1000
    x(i) = i^2;
end
```

### Fonctions optimisées
- Utiliser `fft()` plutôt que calcul manuel
- `conv()` pour convolution
- `eig()` pour valeurs propres
- Bibliothèques BLAS/LAPACK

## 📚 Ressources

- Documentation MATLAB/Octave
- NumPy/SciPy documentation
- Tutoriels en ligne
- Forums de discussion (Stack Overflow)

---

## Documents de Cours

<div class="pdf-container">
  <div class="pdf-viewer">

    <div class="pdf-item">
      <h4>Polycopie de Cours OL S3</h4>
      <p>Support de cours complet : calcul matriciel, convolution, transformee de Fourier, modulations et outils MATLAB/Python.</p>
      <embed src="/cours-pdf/S3/OL/poly_S3_2021_2022.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S3/OL/poly_S3_2021_2022.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Transformation en Z et Resolution d'Equations de Recurrence</h4>
      <p>Cours sur la transformee en Z, ses proprietes et la resolution d'equations aux differences.</p>
      <embed src="/cours-pdf/S3/OL/Transformation_en_z-resolution_equa_recuurence.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S3/OL/Transformation_en_z-resolution_equa_recuurence.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

  </div>
</div>

---

<style>body{font-family:Arial,sans-serif;background-color:#f4f4f9;color:#333;line-height:1.6}h2,h3,h4,h5{color:#2a7ae2}p{text-align:justify}code{background-color:#f5f5f5;padding:2px 6px;border-radius:3px;font-family:'Courier New',monospace}pre{background-color:#f5f5f5;padding:15px;border-radius:5px;overflow-x:auto}</style>

<div class="back-nav">
  <a href="./my-courses-2021-2022.html">&larr; Retour a Mes Cours 2021-2022</a>
</div>

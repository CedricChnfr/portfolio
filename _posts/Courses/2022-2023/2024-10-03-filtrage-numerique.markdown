---
layout: default
title: "Filtrage Numérique - S6"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
---

<style>
.back-nav {
    background: #f4f4f4;
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 20px;
}

.section-title {
    color: #2a7ae2;
    border-bottom: 2px solid #2a7ae2;
    padding-bottom: 5px;
    margin-top: 30px;
}

table {
    border-collapse: collapse;
    width: 100%;
    margin: 20px 0;
}

th {
    background-color: #2a7ae2;
    color: white;
    padding: 10px;
    text-align: left;
}

td {
    border: 1px solid #ddd;
    padding: 10px;
}

tr:nth-child(even) {
    background-color: #f9f9f9;
}

.code-block {
    background: #f4f4f4;
    border-left: 4px solid #2a7ae2;
    padding: 15px;
    margin: 15px 0;
    font-family: 'Courier New', monospace;
}
</style>

<div class="back-nav">
    <a href="./my-courses-2022-2023.html">← Retour aux Cours 2022-2023</a>
</div>

# 📊 Filtrage Numérique - Semestre 6

**Année Universitaire** : 2022-2023  
**Semestre** : 6  
**Crédits** : 2,5 ECTS  
**Spécialité** : Traitement du Signal et Automatique

---

## PART A - Présentation Générale du Cours

<h3 class="section-title">Vue d'ensemble</h3>

Ce cours approfondit le traitement numérique du signal avec un focus sur la conception et l'implémentation de filtres numériques. Il couvre les deux grandes familles de filtres : FIR (Finite Impulse Response) et IIR (Infinite Impulse Response), avec leurs méthodes de conception respectives. Le cours combine théorie mathématique (transformée en Z, réponse fréquentielle) et pratique (MATLAB, implémentation).

**Objectifs pédagogiques** :
- Maîtriser la transformée en Z et l'analyse dans le domaine fréquentiel
- Concevoir des filtres FIR par méthode des fenêtres
- Concevoir des filtres IIR par transformation bilinéaire et invariance impulsionnelle
- Analyser la stabilité et les performances des filtres numériques
- Implémenter et tester des filtres en MATLAB

<h3 class="section-title">Position dans le cursus</h3>

Ce cours s'appuie sur et complète :
- **Signal (S5)** : transformée de Fourier, transformée de Laplace, échantillonnage
- **Modélisation Systèmes Linéaires (S5)** : fonctions de transfert, stabilité

Il prépare aux applications :
- **Traitement du Signal Avancé** : applications audio, biomédicales, communications
- **Embedded IA for IoT (S9)** : prétraitement de signaux pour machine learning
- **Projets de traitement de données** : analyse spectrale, filtrage adaptatif

---

## PART B - Expérience Personnelle et Contexte d'Apprentissage

<h3 class="section-title">Organisation et ressources</h3>

Le module était structuré autour de trois axes :

**1. Cours magistraux** :
- Rappels sur l'échantillonnage et la transformée en Z
- Filtres FIR : propriétés, méthodes de conception
- Filtres IIR : transformation de filtres analogiques
- Structures d'implémentation et effets de quantification

**2. Travaux dirigés** :
- Exercices de conception de filtres FIR par fenêtrage
- Transformation bilinéaire pour filtres IIR
- Analyse de stabilité (placement pôles et zéros)
- Calculs de réponses fréquentielles

**3. Travaux pratiques MATLAB** :
- Utilisation de l'outil fdatool (Filter Design and Analysis Tool)
- Conception et test de filtres FIR et IIR
- Comparaison de performances (ordre, atténuation, phase)
- Application à des signaux réels (audio, ECG)

**Ressources pédagogiques** :
- Playlist YouTube avec cours et TD : [Traitement du Signal](https://www.youtube.com/playlist?list=PL_wkaC4iMBTlJQpi7W18pkzR_kY9d-jsU)
- Annales d'examens 2022 et 2023 avec corrections
- Documentation MATLAB Signal Processing Toolbox

<h3 class="section-title">Déroulement et méthodologie</h3>

**Approche progressive** :

Le cours adoptait une approche en trois étapes :

1. **Théorie** : établir les fondements mathématiques (transformée en Z, équations aux différences)
2. **Méthodes** : appliquer des techniques systématiques de conception
3. **Pratique** : valider et optimiser avec MATLAB

**Exemple de conception de filtre passe-bas FIR** :

Cahier des charges :
- Fréquence de coupure : 1 kHz
- Fréquence d'échantillonnage : 8 kHz
- Atténuation bande coupée : > 40 dB
- Ondulation bande passante : < 0,5 dB

Démarche :
1. Choix de la méthode (fenêtre de Hamming pour compromis)
2. Calcul de l'ordre nécessaire (fonction du gabarit)
3. Génération des coefficients avec MATLAB : fir1(N, Wn, 'low')
4. Vérification de la réponse fréquentielle : freqz(b, a)
5. Test sur signal réel

<h3 class="section-title">Examens et évaluations</h3>

**Format des examens** :

Les annales montrent une structure récurrente :

**Exercice 1 : Filtres FIR** (30-40%)
- Conception par fenêtrage
- Calcul de l'ordre minimal
- Comparaison de différentes fenêtres
- Analyse de la réponse en fréquence

**Exercice 2 : Filtres IIR** (30-40%)
- Transformation bilinéaire ou invariance impulsionnelle
- Calcul de la fonction de transfert en Z
- Placement des pôles et zéros
- Vérification de la stabilité

**Exercice 3 : Implémentation** (20-30%)
- Structure directe ou en cascade
- Effets de quantification
- Optimisation du nombre de bits
- Équations aux différences

**Difficultés courantes** :
- Confusion entre fréquence normalisée (0 à 1) et fréquence physique (Hz)
- Erreurs dans la transformation bilinéaire (pré-déformation)
- Oubli de vérifier la stabilité (pôles à l'intérieur du cercle unité)
- Mauvaise interprétation des spécifications (dB vs linéaire)

<h3 class="section-title">Outils MATLAB utilisés</h3>

**Fonctions principales** :

```matlab
% Conception FIR
b = fir1(N, Wn, 'type');              % Fenêtre
b = firpm(N, F, A);                    % Parks-McClellan (optimal)

% Conception IIR
[b,a] = butter(N, Wn, 'type');         % Butterworth
[b,a] = cheby1(N, Rp, Wn, 'type');     % Chebyshev Type I
[b,a] = cheby2(N, Rs, Wn, 'type');     % Chebyshev Type II
[b,a] = ellip(N, Rp, Rs, Wn, 'type');  % Elliptique

% Analyse
freqz(b, a, N);                        % Réponse fréquentielle
zplane(b, a);                          % Diagramme pôles-zéros
grpdelay(b, a);                        % Délai de groupe
filter(b, a, x);                       % Filtrage
```

---

## PART C - Aspects Techniques Détaillés

<h3 class="section-title">1. Fondements : Transformée en Z</h3>

La transformée en Z est l'équivalent discret de la transformée de Laplace.

**Définition** :
Pour un signal discret x[n], la transformée en Z est :

X(z) = somme de x[n] × z^(-n) pour n de -infini à +infini

**Propriétés importantes** :
- Linéarité : Z{a×x[n] + b×y[n]} = a×X(z) + b×Y(z)
- Décalage temporel : Z{x[n-k]} = z^(-k) × X(z)
- Convolution : Z{x[n] * h[n]} = X(z) × H(z)

**Région de convergence (ROC)** :
Zone du plan complexe où la transformée converge. Critique pour la stabilité.

**Lien avec la transformée de Fourier** :
Sur le cercle unité (z = e^(jω)), la transformée en Z devient la DTFT (Discrete-Time Fourier Transform).

<h3 class="section-title">2. Filtres FIR (Finite Impulse Response)</h3>

**Caractéristiques** :

Un filtre FIR a une réponse impulsionnelle de durée finie :

y[n] = b0×x[n] + b1×x[n-1] + ... + bN×x[n-N]

Fonction de transfert : H(z) = b0 + b1×z^(-1) + ... + bN×z^(-N)

**Avantages** :
- Toujours stable (pas de pôles, uniquement des zéros)
- Phase linéaire possible (important pour audio, images)
- Pas de problème de rétroaction
- Implémentation simple

**Inconvénients** :
- Ordre élevé nécessaire pour sélectivité forte
- Temps de calcul proportionnel à l'ordre
- Délai de groupe constant mais parfois important

**Méthode des fenêtres** :

Principe : partir de la réponse impulsionnelle idéale (infinie) et la tronquer avec une fenêtre.

| Fenêtre | Lobe principal | Atténuation bande coupée | Ondulation |
|---------|----------------|--------------------------|------------|
| Rectangulaire | Étroit | -21 dB | Forte (9%) |
| Hamming | Moyen | -53 dB | Moyenne (0,2%) |
| Hanning | Moyen | -44 dB | Moyenne |
| Blackman | Large | -74 dB | Faible |
| Kaiser | Ajustable | Paramétrable | Paramétrable |

**Compromis** : largeur du lobe principal (bande de transition) vs atténuation bande coupée.

**Exemple : filtre passe-bas avec fenêtre de Hamming**

```matlab
% Spécifications
Fs = 8000;           % Fréquence d'échantillonnage (Hz)
Fc = 1000;           % Fréquence de coupure (Hz)
N = 50;              % Ordre du filtre

% Fréquence normalisée (0 à 1, où 1 = Fs/2)
Wn = Fc / (Fs/2);

% Conception
b = fir1(N, Wn, 'low', hamming(N+1));

% Visualisation
freqz(b, 1, 1024, Fs);
title('Filtre passe-bas FIR - Hamming');
```

**Méthode de Parks-McClellan (optimal)** :

Algorithme d'échange de Remez pour obtenir une réponse équi-ondulation (ripple égal en bande passante et bande coupée).

Avantage : ordre minimal pour un gabarit donné.

```matlab
% Spécifications
F = [0 0.2 0.3 1];     % Fréquences normalisées
A = [1 1 0 0];         % Amplitudes souhaitées
b = firpm(50, F, A);   % Conception optimale
```

<h3 class="section-title">3. Filtres IIR (Infinite Impulse Response)</h3>

**Caractéristiques** :

Un filtre IIR utilise une rétroaction (récursion) :

y[n] = b0×x[n] + b1×x[n-1] + ... - a1×y[n-1] - a2×y[n-2] - ...

Fonction de transfert : H(z) = B(z) / A(z) = (b0 + b1×z^(-1) + ...) / (1 + a1×z^(-1) + a2×z^(-2) + ...)

**Avantages** :
- Ordre faible pour sélectivité élevée (efficacité)
- Correspondent aux filtres analogiques classiques
- Moins de calculs que FIR équivalent

**Inconvénients** :
- Potentiellement instables (pôles hors cercle unité)
- Phase non-linéaire (distorsion de phase)
- Sensibles à la quantification des coefficients
- Risque de cycles limites (oscillations parasites)

**Conception par transformation de filtres analogiques** :

On part d'un filtre analogique éprouvé (Butterworth, Chebyshev, Elliptique) et on le transforme en filtre numérique.

**Approximations analogiques** :

| Type | Bande passante | Bande coupée | Phase | Ordre |
|------|----------------|--------------|-------|-------|
| Butterworth | Maximalement plate | Monotone | Bonne | Élevé |
| Chebyshev I | Ondulations | Monotone | Moyenne | Moyen |
| Chebyshev II | Plate | Ondulations | Moyenne | Moyen |
| Elliptique | Ondulations | Ondulations | Mauvaise | Faible |

**Transformation bilinéaire** :

Méthode la plus utilisée. Transforme l'axe imaginaire du plan s (analogique) vers le cercle unité du plan z (numérique).

Transformation : s = (2/T) × (1 - z^(-1)) / (1 + z^(-1))

où T est la période d'échantillonnage.

**Pré-déformation en fréquence** :

La transformation bilinéaire déforme les fréquences selon :

Omega_analogique = (2/T) × tan(omega_numérique × T/2)

Il faut donc pré-déformer les spécifications avant transformation :

```matlab
% Spécifications numériques
Fs = 1000;              % Hz
Fc = 100;               % Hz
Wn = Fc / (Fs/2);       % Fréquence normalisée

% Conception Butterworth ordre 4
[b, a] = butter(4, Wn, 'low');

% Vérification stabilité
disp(roots(a));         % Tous les pôles doivent être < 1 en module
```

**Invariance impulsionnelle** :

Consiste à échantillonner la réponse impulsionnelle analogique.

Avantage : correspondance exacte en temporel.
Inconvénient : repliement spectral (aliasing) si signal large bande.

<h3 class="section-title">4. Stabilité des Filtres Numériques</h3>

**Critère de stabilité** :

Un filtre numérique est stable si et seulement si tous ses pôles sont à l'intérieur du cercle unité du plan z.

Module de chaque pôle < 1

**Diagramme pôles-zéros** :

Outil essentiel pour visualiser et analyser la stabilité.

```matlab
[b, a] = butter(4, 0.2, 'low');
zplane(b, a);
```

- **Pôles** (×) : racines du dénominateur A(z)
- **Zéros** (○) : racines du numérateur B(z)
- **Cercle unité** : frontière de stabilité

**Interprétation** :
- Pôle proche du cercle unité → forte résonance
- Zéro sur le cercle unité → annulation à cette fréquence
- Pôles complexes conjugués → oscillations

<h3 class="section-title">5. Structures d'Implémentation</h3>

**Forme directe I** :

Implémentation littérale de l'équation aux différences.
- Avantage : simple à comprendre
- Inconvénient : sensible aux erreurs de quantification

**Forme directe II** :

Réarrangement pour minimiser les mémoires (retards).
- Avantage : moins de mémoire (N au lieu de 2N)
- Inconvénient : sensible aux débordements intermédiaires

**Forme en cascade (biquads)** :

Décomposition en cellules du 2ème ordre (sections de second ordre).

H(z) = H1(z) × H2(z) × ... × Hk(z)

- Avantage : robuste à la quantification, stabilité contrôlée
- Utilisation : standard pour IIR

**Forme parallèle** :

Décomposition en fractions partielles.

H(z) = H0 + H1(z) + H2(z) + ... + Hk(z)

- Avantage : traitement parallélisable
- Inconvénient : plus de multiplications

<h3 class="section-title">6. Effets de la Quantification</h3>

**Sources d'erreurs en virgule fixe** :

1. **Quantification des coefficients** :
   - Les coefficients b[k] et a[k] sont arrondis
   - Impact : déplacement des pôles et zéros
   - Risque : pôles sortent du cercle unité → instabilité

2. **Quantification des calculs** :
   - Produits et sommes arrondis à chaque étape
   - Accumulation d'erreurs (bruit de quantification)

3. **Débordement (overflow)** :
   - Résultats intermédiaires dépassent la capacité
   - Solution : mise à l'échelle (scaling)

**Nombre de bits nécessaires** :

Règle empirique : 
- FIR : 12-16 bits suffisent généralement
- IIR : 16-24 bits recommandés (plus sensibles)
- Forme cascade : meilleure robustesse que forme directe

<h3 class="section-title">7. Réponse Fréquentielle et Analyse</h3>

**Module et phase** :

La réponse fréquentielle H(e^(jω)) caractérise le filtre :
- Module |H(ω)| : gain à chaque fréquence
- Phase arg(H(ω)) : déphasage introduit

**Phase linéaire** :

Condition pour éviter la distorsion de phase : arg(H(ω)) = -α×ω + β

Les filtres FIR peuvent avoir une phase linéaire si leurs coefficients sont symétriques ou antisymétriques.

**Délai de groupe** :

Mesure du retard en fonction de la fréquence :

τg(ω) = -d[arg(H(ω))] / dω

Pour phase linéaire : délai de groupe constant.

**Analyse MATLAB** :

```matlab
[H, W] = freqz(b, a, 1024);
% Module en dB
subplot(2,1,1);
plot(W/pi, 20*log10(abs(H)));
ylabel('Magnitude (dB)');
% Phase
subplot(2,1,2);
plot(W/pi, angle(H));
ylabel('Phase (radians)');
xlabel('Fréquence normalisée (×π rad/échantillon)');
```

---

## PART D - Analyse Réflexive et Perspectives

<h3 class="section-title">Compétences acquises</h3>

**Conception systématique de filtres** :
Le cours a fourni une méthodologie rigoureuse pour passer d'un cahier des charges (fréquences, atténuations) à un filtre implémentable. Savoir choisir entre FIR et IIR selon les contraintes.

**Maîtrise de MATLAB** :
Les TPs ont développé une aisance avec Signal Processing Toolbox, indispensable pour le traitement du signal moderne. Capacité à prototyper rapidement des solutions.

**Analyse fréquentielle** :
Compréhension approfondie du lien temps-fréquence, importance de la stabilité, impact des pôles et zéros sur la réponse.

<h3 class="section-title">Points clés à retenir</h3>

**1. FIR vs IIR - Le choix fondamental** :

| Critère | Choisir FIR | Choisir IIR |
|---------|-------------|-------------|
| Phase linéaire requise | ✓ | ✗ |
| Ordre faible critique | ✗ | ✓ |
| Stabilité garantie | ✓ | ✗ (vérifier) |
| Audio, images | ✓ | IIR possible |
| Temps réel contraint | ✗ (ordre élevé) | ✓ |

**2. Stabilité avant tout** :
Toujours vérifier que les pôles sont dans le cercle unité. Un filtre instable est inutilisable.

**3. Fréquences normalisées** :
Attention aux conversions : fréquence physique (Hz) → normalisée (0 à 1) → pulsation numérique (0 à π).

**4. Quantification** :
En implémentation réelle (DSP, FPGA), les effets de virgule fixe peuvent détruire les performances. Toujours simuler avec quantification.

<h3 class="section-title">Applications pratiques</h3>

**Audio et musique** :
- Égaliseurs (filtres passe-bande multiples)
- Effets (réverbération, chorus utilisant IIR)
- Réduction de bruit (filtrage adaptatif)

**Biomédical** :
- Filtrage ECG : passe-bande 0,5-40 Hz pour éliminer 50 Hz secteur
- EEG : extraction de rythmes cérébraux (alpha, beta, theta)
- Détection d'anomalies cardiaques

**Télécommunications** :
- Filtres de mise en forme (raised cosine)
- Égalisation de canal
- Filtres anti-repliement (avant CAN) et de reconstruction (après CNA)

**Traitement d'images** :
- Flou (passe-bas 2D)
- Détection de contours (passe-haut 2D)
- Débruitage (filtres médians, Wiener)

<h3 class="section-title">Liens avec projets et autres cours</h3>

**Projets personnels** :
Les compétences en filtrage numérique ont été appliquées dans plusieurs contextes :
- Analyse de signaux vibratoires pour maintenance prédictive
- Traitement de signaux audio pour reconnaissance vocale
- Prétraitement de données IoT (capteurs accéléromètres)

**Complémentarité avec d'autres cours** :
- **Signal (S5)** : bases théoriques (Fourier, Laplace, échantillonnage)
- **Embedded IA (S9)** : filtrage comme étape de preprocessing pour ML
- **Chaînes d'Acquisition (S8)** : filtres anti-repliement et reconstruction
- **Temps Réel (S8)** : contraintes d'implémentation et optimisation

<h3 class="section-title">Limites et ouvertures</h3>

**Limites du cours** :
- Peu sur les filtres adaptatifs (LMS, RLS)
- Pas de traitement multirate (décimation, interpolation)
- Aspects temps réel peu développés (latence, throughput)
- Implémentation matérielle (FPGA, DSP) non abordée

**Ouvertures vers** :
- **Filtrage adaptatif** : applications en annulation d'écho, égalisation
- **Bancs de filtres** : compression audio (MP3), analyse multirésolution
- **Traitement temps-fréquence** : transformées en ondelettes
- **Filtrage optimal** : filtres de Wiener, Kalman
- **Traitement d'antenne** : beamforming, filtrage spatial

<h3 class="section-title">Évolution technologique</h3>

**Tendances actuelles** :
- **Machine learning** : remplacement de filtres classiques par réseaux de neurones pour débruitage
- **Filtrage embarqué** : accélération matérielle (GPU, FPGA, ASIC)
- **Filtrage distribué** : traitement en edge computing pour IoT
- **Filtrage quantique** : perspectives avec calcul quantique

**Outils modernes** :
- Python scipy.signal : alternative à MATLAB pour le prototypage
- TensorFlow/PyTorch : filtrage par apprentissage profond
- CMSIS-DSP : bibliothèques optimisées pour ARM Cortex-M
- High-Level Synthesis : conception FPGA en C/C++

<h3 class="section-title">Conclusion</h3>

Le filtrage numérique est un pilier du traitement du signal. Maîtriser FIR et IIR, comprendre le compromis ordre/performances, et savoir utiliser les outils de conception sont des compétences essentielles pour l'ingénieur en systèmes embarqués, télécommunications, ou traitement de données.

Ce cours a fourni une base solide théorique (transformée en Z, stabilité) et pratique (MATLAB, implémentation). La capacité à concevoir un filtre adapté à un cahier des charges, vérifier sa stabilité, et l'implémenter efficacement est désormais acquise.

**Ressources pour approfondir** :
- Playlist YouTube du cours : [Traitement du Signal](https://www.youtube.com/playlist?list=PL_wkaC4iMBTlJQpi7W18pkzR_kY9d-jsU)
- Annales avec corrections (2022, 2023) pour s'entraîner
- MATLAB Signal Processing Toolbox documentation
- Livres : "Digital Signal Processing" de Proakis & Manolakis

**Liens avec les autres cours** :
- [Signal - S5](./signal.html) : fondements théoriques
- [Électronique Fonctions Analogiques - S6](./electronique-fonctions-analogiques.html) : filtres actifs
- [Chaînes Électroniques d'Acquisition - S8](./chaines-acquisition.html) : application complète
- [Embedded IA for IoT - S9](./embedded-ia-iot.html) : prétraitement ML

---

*Cours enseigné en 2022-2023 à l'INSA Toulouse, Département Génie Électrique et Informatique.*

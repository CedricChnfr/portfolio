---
layout: default
title: "Signaux Aléatoires - S6"
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

# 🎲 Signaux Aléatoires - Semestre 6

**Année Universitaire** : 2022-2023  
**Semestre** : 6  
**Crédits** : 2.5 ECTS  
**Spécialité** : Traitement du Signal et Probabilités

---

## PART A - Présentation Générale du Module

<h3 class="section-title">Vue d'ensemble</h3>

Les signaux aléatoires sont omniprésents en ingénierie : bruit dans les circuits électroniques, perturbations dans les télécommunications, mesures avec incertitudes. Ce cours introduit les outils mathématiques pour modéliser, analyser et traiter ces signaux aléatoires en utilisant la théorie des probabilités et les processus stochastiques.
**Objectifs pédagogiques** :
- Maîtriser les concepts de probabilités et variables aléatoires
- Comprendre les processus stochastiques et leur caractérisation
- Analyser statistiquement les signaux bruités
- Modéliser le bruit dans les systèmes de communication
- Appliquer le filtrage optimal (Wiener, corrélation)

<h3 class="section-title">Position dans le cursus</h3>

Ce module s'appuie sur :
- **Signal (S5)** : transformée de Fourier, systèmes linéaires
- **Mathématiques** : probabilités, intégrales, séries
- **Filtrage Numérique (S6)** : filtres, traitement du signal

Il prépare aux applications :
- **Télécommunications** : analyse des canaux bruités, BER
- **Traitement du signal** : débruitage, estimation
- **Systèmes embarqués** : mesures avec incertitudes, capteurs

---

## PART B - Expérience Personnelle et Contexte d'Apprentissage

<h3 class="section-title">Organisation et ressources</h3>

Le module était organisé en cours magistraux et travaux dirigés sur le semestre :

**Cours magistraux (20h)** :
Structuré en 4 chapitres (ChapterI à ChapterIV) :
- Chapitre I : Rappels de probabilités et variables aléatoires
- Chapitre II : Couples et vecteurs aléatoires
- Chapitre III : Processus stochastiques
- Chapitre IV : Filtrage linéaire des signaux aléatoires

**Travaux dirigés (16h)** :
Exercices d'application avec corrections disponibles :
- TD 1.1, 1.2, 1.3 : variables aléatoires
- TD 2.1, 2.3 : couples aléatoires
- TD 3.1 : processus stochastiques

**Supports pédagogiques** :
- Fascicules de cours (4 chapitres en PDF)
- Énoncés de TD avec corrections
- Annales d'examens de 2014 à 2017 avec corrigés

<h3 class="section-title">Méthode de travail</h3>

**Cours théorique** :
Beaucoup de définitions mathématiques et de démonstrations. Nécessité de bien assimiler les concepts fondamentaux (densité de probabilité, fonction de répartition, espérance) avant d'aborder les processus stochastiques.

**TD pratiques** :
Exercices d'application directe puis problèmes plus complexes. Les corrections détaillées permettent de vérifier sa compréhension.

**Annales** :
Entraînement sur les sujets d'examens passés (2014-2017) pour se familiariser avec le type de questions posées.

<h3 class="section-title">Difficultés rencontrées</h3>

**Abstraction mathématique** :
Les processus stochastiques sont des objets mathématiques abstraits. Visualiser ce qu'est un processus aléatoire (famille infinie de variables aléatoires) demande un effort d'abstraction.

**Manipulation des densités de probabilité** :
Calculs avec densités conjointes, marginales, conditionnelles. Beaucoup d'intégrales et de changements de variables.

**Lien théorie/pratique** :
Le cours est très théorique. Le lien avec les applications concrètes (bruit dans les circuits, canaux de communication) n'est pas toujours évident.

---

## PART C - Aspects Techniques Détaillés

<h3 class="section-title">1. Rappels de probabilités</h3>

**Espace probabilisé** :

Un espace probabilisé est défini par trois éléments :
- Oméga : ensemble des éventualités (univers)
- A : ensemble des événements (sigma-algèbre)
- P : probabilité (mesure sur A)

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S6/signaux-aleatoires/pdf-gaussienne.svg" alt="Distribution gaussienne" style="max-width: 550px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Fonction de densité de probabilité (PDF) - Loi normale (gaussienne)</p>
</div>

**Propriétés de la probabilité** :
- 0 <= P(A) <= 1
- P(Oméga) = 1
- P(A ou B) = P(A) + P(B) - P(A et B)

**Probabilité conditionnelle** :

P(A sachant B) = P(A et B) / P(B) si P(B) > 0

**Formule des probabilités totales** :

Si B1, B2, ..., Bn forment une partition de Oméga :
P(A) = somme sur i de P(A sachant Bi) × P(Bi)

**Théorème de Bayes** :

P(B sachant A) = P(A sachant B) × P(B) / P(A)

Application : inférence, diagnostic, filtrage de Kalman.

**Indépendance** :

Deux événements A et B sont indépendants si :
P(A et B) = P(A) × P(B)

Équivalent à : P(A sachant B) = P(A)

<h3 class="section-title">2. Variables aléatoires</h3>

**Définition** :
Une variable aléatoire X est une fonction de Oméga vers les réels qui associe à chaque éventualité une valeur numérique.

**Variable aléatoire discrète** :

Prend un nombre fini ou dénombrable de valeurs.

**Fonction de masse (PMF)** :
p(xi) = P(X = xi)

Propriétés :
- p(xi) >= 0
- somme sur i de p(xi) = 1

**Lois discrètes classiques** :

| Loi | Paramètres | Usage | Espérance | Variance |
|-----|------------|-------|-----------|----------|
| Bernoulli | p | succès/échec | p | p(1-p) |
| Binomiale | n, p | nombre de succès sur n essais | np | np(1-p) |
| Poisson | lambda | événements rares | lambda | lambda |
| Géométrique | p | nombre d'essais avant 1er succès | 1/p | (1-p)/p² |

**Variable aléatoire continue** :

Prend ses valeurs dans un intervalle continu.

**Fonction de densité (PDF)** :
Fonction f(x) telle que :
P(a < X < b) = intégrale de a à b de f(x) dx

Propriétés :
- f(x) >= 0
- intégrale de -infini à +infini de f(x) dx = 1

**Fonction de répartition (CDF)** :
F(x) = P(X <= x) = intégrale de -infini à x de f(t) dt

Propriétés :
- F est croissante
- F(-infini) = 0, F(+infini) = 1
- f(x) = dF(x)/dx

**Lois continues classiques** :

| Loi | Densité | Usage | Espérance | Variance |
|-----|---------|-------|-----------|----------|
| Uniforme [a,b] | 1/(b-a) sur [a,b] | équiprobabilité | (a+b)/2 | (b-a)²/12 |
| Exponentielle | lambda × exp(-lambda × x) | durée de vie | 1/lambda | 1/lambda² |
| Gaussienne | (1/racine(2π)σ) exp(-(x-m)²/(2σ²)) | bruit, mesures | m | σ² |
| Rayleigh | (x/σ²) exp(-x²/(2σ²)) | enveloppe signal Gaussien | σ racine(π/2) | σ²(4-π)/2 |

**Moments d'une variable aléatoire** :

**Espérance (moyenne)** :
E[X] = intégrale de x f(x) dx (cas continu)
E[X] = somme de xi p(xi) (cas discret)

**Variance** :
Var(X) = E[(X - E[X])²] = E[X²] - (E[X])²

**Écart-type** :
sigma = racine(Var(X))

**Propriétés de l'espérance** :
- E[aX + b] = a E[X] + b
- E[X + Y] = E[X] + E[Y] (toujours)
- E[XY] = E[X] E[Y] (si X et Y indépendantes)

**Propriétés de la variance** :
- Var(aX + b) = a² Var(X)
- Var(X + Y) = Var(X) + Var(Y) (si X et Y indépendantes)

<h3 class="section-title">3. Loi gaussienne (loi normale)</h3>

**Importance fondamentale** :
La loi gaussienne est la plus importante en ingénierie car :
- Modélise le bruit dans les circuits (bruit thermique)
- Résultat du Théorème Central Limite
- Propriétés mathématiques remarquables

**Densité de probabilité** :

f(x) = (1 / (sigma racine(2π))) exp(-(x - m)² / (2 sigma²))

Paramètres :
- m : moyenne
- sigma² : variance

Notation : X suit N(m, sigma²)

**Loi gaussienne centrée réduite** :

Cas particulier avec m = 0 et sigma = 1 : N(0, 1)

Densité : φ(x) = (1/racine(2π)) exp(-x²/2)

**Standardisation** :

Si X suit N(m, sigma²), alors Z = (X - m) / sigma suit N(0, 1)

Permet d'utiliser les tables de la loi normale standard.

**Règle des 3 sigma** :

Pour une loi gaussienne N(m, sigma²) :
- 68% des valeurs dans [m - sigma, m + sigma]
- 95% des valeurs dans [m - 2sigma, m + 2sigma]
- 99,7% des valeurs dans [m - 3sigma, m + 3sigma]

**Propriétés remarquables** :
- Somme de gaussiennes est gaussienne
- Transformation linéaire d'une gaussienne est gaussienne
- Maximise l'entropie à variance donnée

<h3 class="section-title">4. Couples et vecteurs aléatoires</h3>

**Couple aléatoire** :

Paire (X, Y) de variables aléatoires.

**Densité conjointe** :
f(x, y) telle que P((X, Y) dans D) = intégrale double sur D de f(x, y) dx dy

**Densités marginales** :
Densité de X seule : f_X(x) = intégrale de f(x, y) dy
Densité de Y seule : f_Y(y) = intégrale de f(x, y) dx

**Densité conditionnelle** :
f(x sachant y) = f(x, y) / f_Y(y)

**Indépendance** :

X et Y indépendantes si et seulement si :
f(x, y) = f_X(x) × f_Y(y)

**Corrélation et covariance** :

**Espérance d'un couple** :
E[g(X, Y)] = intégrale double de g(x, y) f(x, y) dx dy

**Covariance** :
Cov(X, Y) = E[(X - E[X])(Y - E[Y])] = E[XY] - E[X] E[Y]

**Coefficient de corrélation** :
rho = Cov(X, Y) / (sigma_X sigma_Y)

Propriétés :
- -1 <= rho <= 1
- rho = 0 : variables non corrélées
- rho = ±1 : relation linéaire

**Remarque importante** :
- Indépendantes => non corrélées
- Non corrélées =/=> indépendantes (sauf cas gaussien)

**Couple gaussien** :

(X, Y) suit une loi gaussienne bidimensionnelle si leur densité conjointe est de la forme gaussienne à 2 dimensions.

**Propriété remarquable** :
Pour un couple gaussien : non corrélées <=> indépendantes

<h3 class="section-title">5. Théorèmes limites</h3>

**Loi des grands nombres** :

Moyenne empirique converge vers l'espérance théorique.

Si X1, X2, ..., Xn variables indépendantes de même loi, d'espérance m :
(X1 + X2 + ... + Xn) / n tend vers m quand n tend vers infini

**Théorème Central Limite (TCL)** :

Somme de variables aléatoires suit approximativement une loi gaussienne.

Si X1, X2, ..., Xn variables indépendantes de même loi, d'espérance m et variance sigma² :
(X1 + X2 + ... + Xn - n×m) / (sigma racine(n)) tend vers N(0, 1)

**Conséquence importante** :
Explique pourquoi tant de phénomènes naturels suivent une loi gaussienne : résultat de nombreuses petites causes indépendantes.

**Applications** :
- Modélisation du bruit (somme de nombreuses perturbations)
- Approximation binomiale par gaussienne (si n grand)
- Estimation statistique

<h3 class="section-title">6. Processus stochastiques</h3>

**Définition** :

Un processus stochastique X(t) est une famille de variables aléatoires indexées par le temps t.

Pour chaque instant t, X(t) est une variable aléatoire.

**Visualisations** :
- Réalisation : courbe X(t, omega) pour un omega fixé
- Distribution : distribution de probabilité à un instant t fixé
- Statistiques : espérance E[X(t)], variance Var[X(t)]

**Types de processus** :

| Type | Temps | Valeurs | Exemple |
|------|-------|---------|---------|
| Discret-Discret | discret | discrètes | Marche aléatoire |
| Continu-Discret | continu | discrètes | Processus de Poisson |
| Discret-Continu | discret | continues | Suite de mesures |
| Continu-Continu | continu | continues | Bruit thermique |

**Moyenne et autocorrélation** :

**Moyenne** :
m_X(t) = E[X(t)]

Fonction du temps (en général).

**Fonction d'autocorrélation** :
R_X(t1, t2) = E[X(t1) X(t2)]

Mesure la corrélation entre les valeurs du processus à deux instants différents.

**Fonction d'autocovariance** :
C_X(t1, t2) = E[(X(t1) - m_X(t1))(X(t2) - m_X(t2))]
C_X(t1, t2) = R_X(t1, t2) - m_X(t1) m_X(t2)

<h3 class="section-title">7. Processus stationnaires</h3>

**Stationnarité stricte** :

Toutes les statistiques du processus sont invariantes par translation dans le temps.

Difficile à vérifier en pratique.

**Stationnarité au sens large (WSS - Wide Sense Stationary)** :

Deux conditions suffisent :
1. Moyenne constante : m_X(t) = m (indépendant de t)
2. Autocorrélation dépend seulement de l'écart : R_X(t1, t2) = R_X(tau) avec tau = t2 - t1

**Propriétés de R_X(tau)** :
- R_X(0) = E[X²(t)] = puissance moyenne
- R_X(tau) = R_X(-tau) (fonction paire)
- |R_X(tau)| <= R_X(0)
- R_X(tau) maximum en tau = 0

**Ergodicité** :

Un processus stationnaire est ergodique si les moyennes temporelles (sur une réalisation) convergent vers les moyennes d'ensemble.

Moyenne temporelle = limite quand T tend vers infini de (1/T) intégrale de 0 à T de x(t) dt

Si ergodique :
- Moyenne temporelle = moyenne théorique E[X]
- Permet d'estimer les statistiques sur une seule réalisation

<h3 class="section-title">8. Densité spectrale de puissance (DSP)</h3>

**Théorème de Wiener-Khinchin** :

Pour un processus WSS, la densité spectrale de puissance S_X(f) est la transformée de Fourier de l'autocorrélation R_X(tau) :

S_X(f) = TF[R_X(tau)]

Réciproquement :
R_X(tau) = TF⁻¹[S_X(f)]

**Interprétation** :
S_X(f) représente la répartition de la puissance du signal en fonction de la fréquence.

**Propriétés** :
- S_X(f) >= 0 (fonction positive)
- S_X(f) = S_X(-f) (fonction paire, si X réel)
- Puissance totale = R_X(0) = intégrale de S_X(f) df

**Puissance dans une bande** :

Puissance entre f1 et f2 = intégrale de f1 à f2 de S_X(f) df

<h3 class="section-title">9. Bruit blanc</h3>

**Définition** :

Processus dont la DSP est constante sur toutes les fréquences :
S_X(f) = N0/2

Autocorrélation :
R_X(tau) = (N0/2) delta(tau)

où delta est la distribution de Dirac.

**Interprétation** :
- Puissance répartie uniformément sur toutes les fréquences
- Valeurs à deux instants différents non corrélées (delta de Dirac)

**Bruit blanc gaussien** :

Processus gaussien avec spectre plat. Noté AWGN (Additive White Gaussian Noise).

Modèle standard du bruit dans les télécommunications.

**Bruit blanc en pratique** :

Le bruit blanc idéal n'existe pas (puissance infinie). En pratique :
- Bruit blanc dans une bande limitée
- DSP plate sur la bande d'intérêt

**Bruit thermique** :

Bruit dans les résistances dû à l'agitation thermique (Johnson-Nyquist).

DSP : S_V(f) = 4 k T R

où k = constante de Boltzmann, T = température (Kelvin), R = résistance.

Approximation de bruit blanc dans une large bande.

<h3 class="section-title">10. Filtrage linéaire des signaux aléatoires</h3>

**Système linéaire invariant (SLI)** :

Caractérisé par sa réponse impulsionnelle h(t) ou sa fonction de transfert H(f).

**Entrée aléatoire X(t), sortie Y(t)** :

Si X(t) est WSS, alors Y(t) est aussi WSS.

**Relations entrée-sortie** :

**Moyenne** :
m_Y = m_X × H(0)

où H(0) est le gain DC du filtre.

**Autocorrélation** :
R_Y(tau) = R_X(tau) * h(tau) * h(-tau)

où * est la convolution.

**DSP** :
S_Y(f) = S_X(f) × |H(f)|²

**Formule fondamentale** : la DSP de sortie est la DSP d'entrée multipliée par le carré du module de la fonction de transfert.

**Variance de la sortie** :
Var(Y) = R_Y(0) = intégrale de S_Y(f) df = intégrale de S_X(f) |H(f)|² df

**Exemple : bruit blanc filtré**

Entrée : bruit blanc de DSP N0/2
Filtre : passe-bas de bande B
Sortie : DSP S_Y(f) = (N0/2) |H(f)|²

Puissance de sortie : (N0/2) × 2B = N0 B

(approximation si filtre idéal)

<h3 class="section-title">11. Rapport signal sur bruit (SNR)</h3>

**Définition** :

SNR = Puissance du signal / Puissance du bruit

En décibels : SNR_dB = 10 log10(SNR)

**Signal dans le bruit** :

Signal utile : s(t) de puissance P_s
Bruit : n(t) de puissance P_n
Signal reçu : r(t) = s(t) + n(t)

SNR = P_s / P_n

**Amélioration du SNR par filtrage** :

Filtre adapté maximise le SNR en sortie.

**Filtre de Wiener** :

Filtre optimal au sens de l'erreur quadratique moyenne minimale (MMSE).

Fonction de transfert optimale :
H_opt(f) = S_XY(f) / (S_X(f) + S_N(f))

où S_XY est l'intercorrélation signal-observation, S_X spectre du signal, S_N spectre du bruit.

**Filtre adapté** :

Pour détecter un signal connu s(t) dans du bruit blanc, le filtre optimal a :
h(t) = s(T - t)

où T est l'instant de décision.

Maximise le SNR à l'instant d'échantillonnage.

<h3 class="section-title">12. Applications en télécommunications</h3>

**Canal AWGN (Additive White Gaussian Noise)** :

Modèle standard de canal de communication.

Signal reçu : r(t) = s(t) + n(t)

où n(t) est un bruit blanc gaussien.

**Taux d'erreur binaire (BER)** :

Probabilité d'erreur sur un bit en fonction du SNR.

Pour une modulation binaire simple :
BER = fonction du rapport Eb/N0

où Eb est l'énergie par bit, N0 la DSP du bruit.

**Capacité de Shannon** :

Débit maximal théorique d'un canal :
C = B log2(1 + SNR)

où B est la bande passante, C la capacité en bits/s.

**Théorème de Shannon** :
On peut transmettre à un débit < C avec une probabilité d'erreur arbitrairement faible (grâce au codage canal).

<h3 class="section-title">13. Estimation et détection</h3>

**Estimation de paramètres** :

À partir d'observations bruitées, estimer un paramètre inconnu.

**Estimateur du maximum de vraisemblance (MLE)** :

Choisir la valeur du paramètre qui maximise la probabilité d'observer les données.

Principe : theta_MLE = argmax de la vraisemblance L(theta)

**Estimateur MMSE** :

Minimise l'erreur quadratique moyenne.

E[(theta - theta_estimé)²] minimale

**Détection d'hypothèses** :

Décider entre plusieurs hypothèses (H0 ou H1) à partir d'observations.

**Critère de Neyman-Pearson** :

Maximiser la probabilité de détection pour une probabilité de fausse alarme donnée.

**Courbe ROC (Receiver Operating Characteristic)** :

Probabilité de détection en fonction de la probabilité de fausse alarme.

Permet de comparer les performances de différents détecteurs.

---

## PART D - Analyse Réflexive et Perspectives

<h3 class="section-title">Compétences acquises</h3>

**Rigueur mathématique** :
Le cours développe une approche rigoureuse des probabilités et des processus stochastiques. Les démonstrations mathématiques renforcent la compréhension profonde des concepts.

**Modélisation de l'aléatoire** :
Capacité à modéliser des phénomènes aléatoires réels (bruit, mesures, signaux) par des lois de probabilité et des processus stochastiques appropriés.

**Analyse spectrale** :
Maîtrise de la densité spectrale de puissance comme outil d'analyse des signaux aléatoires, complément essentiel à la transformée de Fourier classique.

<h3 class="section-title">Points clés à retenir</h3>

**1. Loi gaussienne centrale** :
La loi gaussienne est omniprésente grâce au Théorème Central Limite. Comprendre ses propriétés est essentiel pour l'ingénieur.

**2. Corrélation vs indépendance** :
Non corrélation n'implique pas indépendance (sauf cas gaussien). Distinction fondamentale souvent source d'erreurs.

**3. Stationnarité = simplicité** :
Les processus stationnaires sont beaucoup plus simples à analyser. En pratique, on suppose souvent la stationnarité (au moins localement).

**4. DSP = outil de choix** :
La densité spectrale de puissance est l'outil principal pour analyser et filtrer les signaux aléatoires. Théorème de Wiener-Khinchin est fondamental.

**5. Filtrage optimal** :
Le filtre de Wiener et le filtre adapté sont des résultats théoriques importants qui guident la conception de systèmes réels.

<h3 class="section-title">Applications pratiques</h3>

**Télécommunications** :
- Modélisation du canal (bruit AWGN, évanouissements)
- Calcul du BER en fonction du SNR
- Conception de récepteurs optimaux
- Égalisation, débruitage

**Traitement du signal** :
- Estimation de paramètres (fréquence, phase, amplitude)
- Détection de signaux noyés dans le bruit
- Filtrage optimal (Wiener)
- Analyse spectrale (estimation de DSP)

**Systèmes de mesure** :
- Quantification de l'incertitude
- Amélioration du SNR par moyennage
- Conception de capteurs
- Traitement statistique des mesures

**Radar et sonar** :
- Détection de cibles
- Estimation de distance, vitesse
- Filtrage adapté pour maximiser le SNR

<h3 class="section-title">Retour d'expérience</h3>

**Cours théorique** :
Le cours est dense et mathématique. La maîtrise des concepts demande du temps et de la pratique sur des exercices variés. Les TD sont essentiels pour assimiler la théorie.

**Annales précieuses** :
Les annales de 2014 à 2017 avec corrections sont une ressource importante pour se préparer à l'examen et comprendre les attentes.

**Difficulté progressive** :
- Chapitre I (probabilités et variables aléatoires) : relativement accessible
- Chapitre II (couples aléatoires) : plus technique (intégrales doubles)
- Chapitre III (processus stochastiques) : abstrait
- Chapitre IV (filtrage) : applications concrètes, plus motivant

<h3 class="section-title">Limites et ouvertures</h3>

**Limites du module** :
- Peu d'applications pratiques (simulations MATLAB)
- Traitement limité de l'estimation (pas de Kalman détaillé)
- Pas de processus non-stationnaires (signaux transitoires)

**Ouvertures vers** :
- **Traitement statistique du signal** : estimation spectrale, analyse temps-fréquence
- **Communications numériques** : modulations, codage canal, égalisation
- **Filtrage de Kalman** : estimation récursive, systèmes dynamiques
- **Apprentissage automatique** : modèles probabilistes, inférence bayésienne
- **Traitement d'image** : bruit dans les images, restauration
- **Finance** : modélisation des marchés (mouvement brownien, processus stochastiques)

<h3 class="section-title">Liens avec d'autres domaines</h3>

**Théorie de l'information** :
Entropie, information mutuelle, capacité de canal (Shannon).

**Statistiques** :
Tests d'hypothèses, estimation, intervalles de confiance.

**Contrôle stochastique** :
Systèmes dynamiques avec incertitudes, commande optimale.

**Apprentissage automatique** :
Modèles génératifs probabilistes, réseaux bayésiens, processus gaussiens.

<h3 class="section-title">Conseils pour réussir</h3>

**1. Maîtriser les bases** :
Assurer les fondamentaux (probabilités, densités, espérance, variance) avant d'aborder les processus stochastiques.

**2. Faire les TD** :
Les exercices sont essentiels. Refaire les TD sans regarder les corrections pour tester sa compréhension.

**3. Utiliser les annales** :
S'entraîner sur les examens passés pour se familiariser avec le format et identifier les points importants.

**4. Visualiser** :
Essayer de visualiser les concepts (courbes de densité, réalisations de processus) plutôt que rester dans l'abstraction pure.

**5. Comprendre les théorèmes** :
Théorème Central Limite, Wiener-Khinchin sont fondamentaux. Bien comprendre leurs hypothèses et conséquences.

<h3 class="section-title">Conclusion</h3>

Le module Signaux Aléatoires apporte les fondements mathématiques indispensables pour traiter les signaux bruités et les phénomènes aléatoires omniprésents en ingénierie. La théorie des probabilités et des processus stochastiques, bien que parfois abstraite, fournit des outils puissants et rigoureux.

**Impact sur la formation** :
Ce cours change la vision des signaux : tout signal réel contient de l'aléatoire (bruit, incertitudes). Savoir modéliser et traiter cet aléatoire est essentiel pour l'ingénieur.

**Complémentarité** :
En complément du traitement du signal déterministe (Fourier, filtres), le traitement statistique des signaux aléatoires permet d'aborder des problèmes réels (estimation, détection, débruitage).

**Message principal** :
L'aléatoire n'est pas l'ennemi de l'ingénieur. Avec les bons outils (probabilités, processus stochastiques, DSP, filtrage optimal), on peut analyser, modéliser et traiter efficacement les signaux aléatoires.

**Recommandations** :
- Approfondir avec des simulations (MATLAB, Python) pour visualiser les concepts
- Lire des articles sur applications concrètes (radar, télécommunications)
- Se former au filtrage de Kalman (extension naturelle)
- Explorer les liens avec l'apprentissage automatique (modèles probabilistes)

**Liens avec les autres cours** :
- [Signal - S5](./signal.html) : transformée de Fourier, systèmes linéaires
- [Filtrage Numérique - S6](./filtrage-numerique.html) : filtres numériques FIR/IIR
- [Électronique Fonctions Numériques - S6](./electronique-fonctions-numeriques.html) : bruit dans les circuits

---

## 📚 Documents de Cours

<style>
    .pdf-container {
        margin: 40px 0;
        padding: 20px;
        background: #f9f9f9;
        border-radius: 8px;
    }
    .pdf-viewer {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
    }
    .pdf-item {
        flex: 1;
        min-width: 400px;
        background: white;
        padding: 15px;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .pdf-item h4 {
        color: #2a7ae2;
        margin-top: 0;
    }
</style>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>📖 Chapitre I - Probabilités</h4>
      <p>Introduction aux probabilités : espérances mathématiques, axiomes, probabilités conditionnelles et théorème de Bayes.</p>
      <embed src="/cours-pdf/S6/Signaux-Aleatoires/chapitre1-probabilites.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Signaux-Aleatoires/chapitre1-probabilites.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>📖 Chapitre II - Variables Aléatoires</h4>
      <p>Variables aléatoires discrètes et continues : lois de probabilité, moments, fonction caractéristique et espérance.</p>
      <embed src="/cours-pdf/S6/Signaux-Aleatoires/chapitre2-variables-aleatoires.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Signaux-Aleatoires/chapitre2-variables-aleatoires.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>📖 Chapitre III - Processus Stochastiques</h4>
      <p>Processus aléatoires : stationnarité, ergodicité, autocorrélation et propriétés des processus stationnaires.</p>
      <embed src="/cours-pdf/S6/Signaux-Aleatoires/chapitre3-processus-stochastiques.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Signaux-Aleatoires/chapitre3-processus-stochastiques.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>📖 Chapitre IV - Analyse Spectrale</h4>
      <p>Densité spectrale de puissance (DSP), théorème de Wiener-Khintchine et filtrage linéaire des processus aléatoires.</p>
      <embed src="/cours-pdf/S6/Signaux-Aleatoires/chapitre4-analyse-spectrale.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Signaux-Aleatoires/chapitre4-analyse-spectrale.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
  </div>
</div>

---

*Cours suivi en 2022-2023 à l'INSA Toulouse, Département Génie Électrique et Informatique.*

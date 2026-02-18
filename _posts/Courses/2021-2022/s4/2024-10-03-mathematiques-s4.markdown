---
layout: default
title: "Mathématiques - S4"
date:   2024-10-02 10:56:03 +0200
---

# Mathématiques - Semestre 4

---

## PART A - Présentation Générale du Cours

### Contexte et objectifs

Mathématiques appliquées pour l'ingénieur GEII : analyse de Fourier, transformée en Z, équations récurrence, analyse numérique. Support théorique pour signal, automatique, filtrage.

**Objectifs :**
- Séries et transformée de Fourier (analyse fréquentielle)
- Transformée en Z (systèmes numériques)
- Équations récurrence (modélisation discrète)
- Analyse numérique (méthodes approchées)
- Résolution problèmes ingénierie

### Prérequis
- Mathématiques S1-S3 (Fourier, Laplace, complexes)
- Signal (convolution, filtrage)

---

## PART B: EXPÉRIENCE, CONTEXTE ET FONCTION

### Module 1 : Séries et transformée de Fourier

**Série de Fourier (signal périodique) :**
$$f(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty} [a_n\cos(n\omega_0 t) + b_n\sin(n\omega_0 t)]$$
- Forme exponentielle : $f(t) = \sum_{n=-\infty}^{\infty} c_n e^{jn\omega_0 t}$
- Spectre discret

**Transformée de Fourier (signal non-périodique) :**
$$F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-j\omega t} dt$$
- Spectre continu
- Propriétés : linéarité, translation, modulation, convolution

**Applications :**
- Analyse harmoniques
- Filtrage fréquentiel
- Théorème de Parseval (énergie)

### Module 2 : Transformée en Z

**Définition :**
$$X(z) = \sum_{n=0}^{\infty} x[n] z^{-n}$$
- Analogue discret de Laplace
- Région de convergence (ROC)

**Propriétés :**
- Linéarité, retard : $z^{-k}$
- Convolution → multiplication
- Valeur initiale/finale

**Applications :**
- Analyse filtres numériques
- Stabilité : pôles dans cercle unité
- Fonction de transfert : $H(z) = Y(z)/X(z)$

### Module 3 : Équations de récurrence

**Forme générale :**
$$y[n] + a_1 y[n-1] + ... + a_N y[n-N] = b_0 x[n] + ... + b_M x[n-M]$$

**Résolution :**
- Transformée en Z
- Solution homogène + particulière
- Équation caractéristique

**Applications :**
- Filtres IIR (implémentation récursive)
- Systèmes dynamiques discrets
- Modèles économiques/biologiques

### Module 4 : Analyse numérique

**Intégration numérique :**
- Rectangles, trapèzes, Simpson
- Précision vs nombre points

**Résolution équations :**
- Méthode Newton-Raphson : $x_{n+1} = x_n - f(x_n)/f'(x_n)$
- Dichotomie
- Point fixe

**Interpolation :**
- Lagrange, Newton
- Splines

**Équations différentielles :**
- Euler, Runge-Kutta
- Applications automatique

---

## PART C: ASPECTS TECHNIQUES

### TD/TP

**TP1 : Séries de Fourier**
- Signal carré, triangulaire
- Calcul coefficients a_n, b_n
- Synthèse (somme N harmoniques)
- Phénomène Gibbs

**TP2 : Transformée en Z**
- Calcul Z-transform de séquences
- Analyse stabilité filtres IIR
- Diagramme pôles-zéros

**TP3 : Récurrence et filtres**
- Équation récurrence filtre ordre 2
- Résolution Z-transform
- Simulation réponse (MATLAB)

**TP4 : Méthodes numériques**
- Intégration fonction complexe
- Résolution équation non-linéaire
- Comparaison méthodes (précision, vitesse)

### Outils
- **MATLAB/Octave** : calcul symbolique, visualisation
- **Python** : NumPy, SciPy
- Calculatrice formelle (TI, Casio)

---

## PART D: ANALYSE ET RÉFLEXION

### Évaluation
- TD et exercices (30%)
- TP MATLAB (20%)
- Contrôles continus (25%)
- Examen final (25%)

### Compétences acquises
- Analyse fréquentielle (Fourier)
- Analyse systèmes numériques (Z-transform)
- Modélisation discrète (équations récurrence)
- Méthodes numériques pratiques
- Lien théorie-applications

### Applications interdisciplinaires
- **Signal** : analyse spectrale, filtrage
- **Automatique** : fonction transfert discrète
- **Télécom** : modulation, codage
- **Filtrage Num** : conception filtres

## 📚 Contenu du cours

### Séries de Fourier

#### Décomposition en série
**Série trigonométrique :**
$$f(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left[a_n\cos(n\omega_0 t) + b_n\sin(n\omega_0 t)\right]$$

**Coefficients :**
- $a_0 = \frac{2}{T}\int_0^T f(t)dt$
- $a_n = \frac{2}{T}\int_0^T f(t)\cos(n\omega_0 t)dt$
- $b_n = \frac{2}{T}\int_0^T f(t)\sin(n\omega_0 t)dt$

**Forme exponentielle (complexe) :**
$$f(t) = \sum_{n=-\infty}^{+\infty} c_n e^{jn\omega_0 t}$$

avec $c_n = \frac{1}{T}\int_0^T f(t)e^{-jn\omega_0 t}dt$

#### Propriétés
- Linéarité
- Décalage temporel
- Changement d'échelle
- Dérivation et intégration
- Produit (convolution des spectres)

#### Convergence
- Conditions de Dirichlet
- Convergence ponctuelle
- Phénomène de Gibbs (discontinuités)
- Convergence en moyenne quadratique

#### Applications
- Analyse de signaux périodiques
- Calcul de contenu harmonique
- Réponse de systèmes linéaires
- Filtrage fréquentiel

### Transformation de Fourier

#### Définition
**Transformée directe :**
$$F(\omega) = \int_{-\infty}^{+\infty} f(t)e^{-j\omega t}dt$$

**Transformée inverse :**
$$f(t) = \frac{1}{2\pi}\int_{-\infty}^{+\infty} F(\omega)e^{j\omega t}d\omega$$

#### Propriétés principales
- **Linéarité** : $\mathcal{F}\{af + bg\} = aF + bG$
- **Décalage temporel** : $\mathcal{F}\{f(t-t_0)\} = e^{-j\omega t_0}F(\omega)$
- **Décalage fréquentiel** : $\mathcal{F}\{e^{j\omega_0 t}f(t)\} = F(\omega - \omega_0)$
- **Changement d'échelle** : $\mathcal{F}\{f(at)\} = \frac{1}{|a|}F\left(\frac{\omega}{a}\right)$
- **Dérivation** : $\mathcal{F}\{f'(t)\} = j\omega F(\omega)$
- **Intégration** : $\mathcal{F}\left\{\int f(t)dt\right\} = \frac{F(\omega)}{j\omega}$
- **Convolution** : $\mathcal{F}\{f * g\} = F(\omega) \cdot G(\omega)$
- **Produit** : $\mathcal{F}\{f \cdot g\} = \frac{1}{2\pi}F * G$

#### Transformées usuelles
- Porte : $\text{rect}(t) \leftrightarrow \text{sinc}(\omega)$
- Exponentielle décroissante : $e^{-at}u(t) \leftrightarrow \frac{1}{a+j\omega}$
- Gaussienne : $e^{-at^2} \leftrightarrow \sqrt{\frac{\pi}{a}}e^{-\omega^2/4a}$
- Impulsion de Dirac : $\delta(t) \leftrightarrow 1$
- Constante : $1 \leftrightarrow 2\pi\delta(\omega)$

#### Théorème de Parseval
$$\int_{-\infty}^{+\infty} |f(t)|^2 dt = \frac{1}{2\pi}\int_{-\infty}^{+\infty} |F(\omega)|^2 d\omega$$

Conservation de l'énergie

#### Applications
- Analyse spectrale
- Filtrage
- Traitement du signal
- Résolution d'équations différentielles

### Séries entières

#### Définition
$$\sum_{n=0}^{\infty} a_n(x-x_0)^n$$

#### Rayon de convergence
**Critères :**
- D'Alembert : $R = \lim_{n\to\infty}\left|\frac{a_n}{a_{n+1}}\right|$
- Cauchy : $R = \frac{1}{\lim_{n\to\infty}\sqrt[n]{|a_n|}}$

**Domaine :** $|x - x_0| < R$

#### Opérations
- Somme et produit de séries
- Dérivation terme à terme
- Intégration terme à terme
- Composition

#### Développements usuels
- $e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}$
- $\cos(x) = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!}$
- $\sin(x) = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!}$
- $\frac{1}{1-x} = \sum_{n=0}^{\infty} x^n$ pour $|x|<1$

#### Applications
- Résolution d'équations différentielles
- Approximation de fonctions
- Analyse de systèmes

### Équations de récurrence

#### Types
**Linéaires à coefficients constants :**
$$a_n u_{n+k} + a_{n-1} u_{n+k-1} + \ldots + a_0 u_n = f(n)$$

**Homogènes** : $f(n) = 0$
**Non homogènes** : $f(n) \neq 0$

#### Résolution

**Équation caractéristique :**
Pour $u_{n+2} + au_{n+1} + bu_n = 0$
$$r^2 + ar + b = 0$$

**Solutions :**
- Racines réelles distinctes : $u_n = A r_1^n + B r_2^n$
- Racine double : $u_n = (A + Bn)r^n$
- Racines complexes : $u_n = \rho^n(A\cos(n\theta) + B\sin(n\theta))$

**Solution générale :**
Solution homogène + solution particulière

#### Applications
- Suites récurrentes
- Systèmes numériques (filtres)
- Modèles discrets
- Analyse d'algorithmes

### Analyse numérique

#### Interpolation

**Interpolation de Lagrange :**
Polynôme passant par n+1 points
$$P(x) = \sum_{i=0}^{n} y_i L_i(x)$$

avec $L_i(x) = \prod_{j\neq i}\frac{x-x_j}{x_i-x_j}$

**Splines :**
- Interpolation par morceaux
- Continuité et dérivabilité
- Splines cubiques

#### Intégration numérique

**Méthodes de quadrature :**

*Rectangles :*
$$\int_a^b f(x)dx \approx h\sum_{i=0}^{n-1} f(x_i)$$

*Trapèzes :*
$$\int_a^b f(x)dx \approx \frac{h}{2}\left[f(a) + 2\sum_{i=1}^{n-1}f(x_i) + f(b)\right]$$

*Simpson :*
$$\int_a^b f(x)dx \approx \frac{h}{3}\left[f(a) + 4\sum_{impair}f(x_i) + 2\sum_{pair}f(x_i) + f(b)\right]$$

**Erreur d'approximation :**
Dépend de la méthode et de la dérivée de f

#### Résolution d'équations différentielles

**Euler explicite :**
$$y_{n+1} = y_n + h \cdot f(t_n, y_n)$$

**Méthodes Runge-Kutta :**
- RK2 (ordre 2)
- RK4 (ordre 4) - standard
- Meilleure précision

**Stabilité :**
Contraintes sur le pas h

## 🛠️ Travaux pratiques

### TP Séries de Fourier (Maple/MATLAB)
- Calcul de coefficients
- Reconstruction du signal
- Influence du nombre de termes
- Phénomène de Gibbs

### TP Transformation de Fourier
- Calcul de transformées
- Propriétés (décalage, convolution)
- Filtrage fréquentiel
- Spectres de signaux

### TP Interpolation (Maple)
- Polynômes de Lagrange
- Splines cubiques
- Comparaison méthodes
- Erreur d'interpolation

### TP Intégration numérique
- Méthodes rectangles, trapèzes, Simpson
- Comparaison précision
- Convergence
- Applications

### TP Équations différentielles
- Euler, RK2, RK4
- Comparaison avec solution analytique
- Influence du pas
- Stabilité

## 💻 Outils utilisés

### Calcul formel
- **Maple** : Calcul symbolique
- **Mathematica** : Alternative
- **SymPy (Python)** : Open source

### Calcul numérique
- **MATLAB** : Standard industrie
- **Octave** : Compatible MATLAB
- **Python (NumPy, SciPy)** : Scientifique

### Visualisation
- Tracés de fonctions
- Spectres
- Convergence
- Animations

## 📊 Évaluation

- Travaux pratiques (30%)
- Contrôles continus (35%)
- Examen final (35%)

## 🔗 Liens avec d'autres cours

- **Signal** : Analyse de Fourier
- **SE** : Traitement numérique
- **OL** : Implémentation
- **Automatique** : Systèmes dynamiques

## 📐 Exemples d'applications

### Signal carré (séries de Fourier)
$$f(t) = \frac{4}{\pi}\sum_{n=0}^{\infty}\frac{\sin((2n+1)\omega_0 t)}{2n+1}$$

Harmoniques impairs uniquement

### Filtre passe-bas idéal
$$H(\omega) = \begin{cases} 1 & |\omega| < \omega_c \\ 0 & |\omega| > \omega_c \end{cases}$$

Réponse impulsionnelle : $h(t) = \frac{\omega_c}{\pi}\text{sinc}(\omega_c t)$

### Suite de Fibonacci
$u_{n+2} = u_{n+1} + u_n$, $u_0=0$, $u_1=1$

Solution : $u_n = \frac{1}{\sqrt{5}}\left[\phi^n - (-\phi)^{-n}\right]$

avec $\phi = \frac{1+\sqrt{5}}{2}$ (nombre d'or)

## 💡 Applications en ingénierie

### Traitement du signal
- Analyse spectrale
- Filtrage
- Compression
- Synthèse

### Systèmes de contrôle
- Analyse fréquentielle
- Réponse temporelle
- Stabilité
- Commande

### Télécommunications
- Modulation
- Analyse de canaux
- Égalisation
- Codage

## 📖 Compétences développées

- Analyse de Fourier (séries et transformée)
- Résolution d'équations de récurrence
- Méthodes numériques
- Calcul formel et numérique
- Application des mathématiques à l'ingénierie

## 🎯 Formules essentielles

### Identités trigonométriques
- $\cos^2(x) = \frac{1+\cos(2x)}{2}$
- $\sin^2(x) = \frac{1-\cos(2x)}{2}$
- $\cos(a)\cos(b) = \frac{1}{2}[\cos(a-b)+\cos(a+b)]$

### Formules d'Euler
- $e^{jx} = \cos(x) + j\sin(x)$
- $\cos(x) = \frac{e^{jx}+e^{-jx}}{2}$
- $\sin(x) = \frac{e^{jx}-e^{-jx}}{2j}$

## ⚠️ Pièges courants

### Séries de Fourier
- Oublier le facteur 1/2 pour a₀
- Convergence aux discontinuités
- Période mal identifiée

### Transformation
- Oublier le facteur 1/(2π)
- Conditions d'existence
- Interprétation physique

### Analyse numérique
- Pas trop grand (instabilité)
- Accumulation erreurs
- Conditionnement

## 🔧 Conseils pratiques

### Calculs
- Vérifier dimensions
- Symétries pour simplifier
- Cas particuliers connus
- Validation numérique

### Programmation
- Vectorisation (MATLAB)
- Bibliothèques optimisées
- Validation sur cas simples
- Visualisation résultats

---
layout: default
title: "Outils Logiciels (OL) - S4"
date:   2024-10-02 10:56:03 +0200
---

# Outils Logiciels (OL) - Semestre 4

---

## PART A - Présentation Générale du Cours

### Contexte et objectifs

Suite OL S3 : transformée en Z, commande numérique, séries. Outils mathématiques pour automatique numérique et filtrage numérique S4.

**Objectifs :**
- Transformée en Z appliquée (filtres, asservissements)
- Systèmes à temps discret
- Stabilité et performances numériques
- Séries entières et récurrence
- Simulation MATLAB/Simulink

### Prérequis
- OL S3 (MATLAB, convolution, FFT)
- Mathématiques S4 (Z-transform)
- Automatique S3 (asservissements continus)

---

## PART B: EXPÉRIENCE, CONTEXTE ET FONCTION

### Module 1 : Transformée en Z avancée

**Définition (rappel) :**
$$X(z) = \sum_{n=0}^{\infty} x[n] z^{-n}$$

**Propriétés essentielles :**
- Retard : $\mathcal{Z}\{x[n-k]\} = z^{-k} X(z)$
- Convolution : $\mathcal{Z}\{x*h\} = X(z)H(z)$
- Théorème valeur initiale/finale

**Applications :**
- Fonction transfert discrète : $H(z) = Y(z)/X(z)$
- Résolution équations récurrence
- Analyse stabilité (pôles dans cercle unité)

### Module 2 : Commande numérique

**Discrétisation systèmes continus :**
- Méthode Euler : $s \approx (z-1)/T$
- Transformation bilinéaire (Tustin) : $s \approx 2(z-1)/(T(z+1))$
- Équivalence zéro-order-hold (ZOH)

**Correcteurs numériques :**
- PID numérique :
  - P : gain constant
  - I : intégration (somme cumulée)
  - D : différence $x[n] - x[n-1]$
- Réglage : Ziegler-Nichols adapté

**Analyse performances :**
- Stabilité : pôles $|z| < 1$
- Précision statique : erreur permanente
- Rapidité : temps réponse, dépassement

### Module 3 : Séries numériques

**Séries entières :**
$$\sum_{n=0}^{\infty} a_n x^n$$
- Rayon de convergence
- Développements Taylor, Maclaurin

**Séries numériques :**
- Convergence : critères (d'Alembert, Cauchy)
- Sommes partielles

**Applications :**
- Approximations fonctions (exp, sin, cos)
- Résolution équations différentielles

---

## PART C: ASPECTS TECHNIQUES

### TP MATLAB/Simulink

**TP1 : Transformée en Z**
- Calcul Z-transform analytique
- Fonction transfert filtre IIR
- Diagramme pôles-zéros
- Stabilité et réponse temporelle

**TP2 : PID numérique**
- Discrétisation système continu (moteur DC)
- Synthèse PID discret
- Simulation Simulink
- Comparaison continu vs numérique

**TP3 : Filtrage numérique par Z-transform**
- Conception filtre passe-bas 2ème ordre
- Méthode bilinéaire
- Implémentation équation récurrence
- Validation sur signaux

**TP4 : Séries**
- Convergence séries
- Approximation fonctions
- Erreur troncature

### Outils
- **MATLAB** : Control System Toolbox, `c2d()`, `pzmap()`
- **Simulink** : modélisation systèmes asservis
- **Python** : `scipy.signal`, `control` library

---

## PART D: ANALYSE ET RÉFLEXION

### Évaluation
- TP MATLAB (50%)
- Mini-projets (25%)
- Contrôle final (25%)

### Compétences acquises
- Transformée en Z appliquée (filtres, asservissements)
- Conception correcteurs numériques
- Analyse stabilité systèmes discrets
- Simulation systèmes numériques
- Lien continu ↔ numérique

### Liens interdisciplinaires
- **Filtrage Num S4** : synthèse filtres IIR
- **Automatique S3** : discrétisation correcteurs
- **Mathématiques S4** : Z-transform théorique
- **IE S3** : implémentation STM32

## 📚 Contenu du cours

### Transformation en Z

#### Définition
**Transformée en Z directe :**
$$X(z) = \sum_{n=0}^{\infty} x[n]z^{-n}$$

**Transformée en Z inverse :**
Méthodes :
- Décomposition en fractions simples
- Division polynomiale (division longue)
- Théorème des résidus
- Inspection (transformées connues)

#### Propriétés
- **Linéarité** : $\mathcal{Z}\{ax[n]+by[n]\} = aX(z) + bY(z)$
- **Décalage temporel** : $\mathcal{Z}\{x[n-k]\} = z^{-k}X(z)$
- **Avance temporelle** : $\mathcal{Z}\{x[n+k]\} = z^k X(z)$
- **Multiplication par aⁿ** : $\mathcal{Z}\{a^n x[n]\} = X(z/a)$
- **Convolution** : $\mathcal{Z}\{x[n]*h[n]\} = X(z) \cdot H(z)$
- **Valeur initiale** : $x[0] = \lim_{z\to\infty} X(z)$
- **Valeur finale** : $\lim_{n\to\infty} x[n] = \lim_{z\to 1} (z-1)X(z)$

#### Transformées usuelles
- Impulsion : $\delta[n] \leftrightarrow 1$
- Échelon : $u[n] \leftrightarrow \frac{z}{z-1}$
- Rampe : $nu[n] \leftrightarrow \frac{z}{(z-1)^2}$
- Exponentielle : $a^n u[n] \leftrightarrow \frac{z}{z-a}$
- Sinusoïde : $\sin(\omega n)u[n] \leftrightarrow \frac{z\sin(\omega)}{z^2-2z\cos(\omega)+1}$

#### Région de convergence (ROC)
- Importance pour l'existence
- Causalité : ROC extérieur au cercle
- Stabilité : ROC inclut le cercle unité

### Asservissement numérique

#### Systèmes échantillonnés

**Échantillonnage :**
- Période d'échantillonnage Te
- Fréquence Fe = 1/Te
- Théorème de Shannon : Fe > 2·Fmax

**Bloqueur d'ordre zéro (BOZ) :**
- Maintien du signal entre échantillons
- Fonction de transfert : $H_{BOZ}(s) = \frac{1-e^{-T_e s}}{s}$

#### Fonction de transfert en Z

**Système numérique :**
$$H(z) = \frac{Y(z)}{U(z)} = \frac{b_0 + b_1z^{-1} + \ldots + b_m z^{-m}}{1 + a_1z^{-1} + \ldots + a_n z^{-n}}$$

**Équation aux différences :**
$$y[n] = -\sum_{k=1}^{n}a_k y[n-k] + \sum_{k=0}^{m}b_k u[n-k]$$

#### Discrétisation de systèmes continus

**Méthode d'Euler (avant) :**
$$s \approx \frac{z-1}{T_e}$$

**Méthode d'Euler (arrière) :**
$$s \approx \frac{z-1}{T_e z}$$

**Transformation bilinéaire (Tustin) :**
$$s \approx \frac{2}{T_e}\frac{z-1}{z+1}$$

Meilleure conservation de la stabilité

**Invariance impulsionnelle :**
Échantillonnage de la réponse impulsionnelle

#### Stabilité

**Critère :**
Tous les pôles dans le cercle unité : $|z_i| < 1$

**Tests :**
- Critère de Jury
- Lieu des racines (root locus)
- Marges de gain et de phase
- Diagramme de Bode (w-transform)

#### Analyse de performances

**Réponse temporelle :**
- Temps de réponse
- Dépassement
- Erreur statique
- Régime permanent

**Erreur en régime permanent :**
$$\epsilon_{\infty} = \lim_{n\to\infty} e[n] = \lim_{z\to 1} (z-1)E(z)$$

#### Synthèse de correcteurs

**Correcteur proportionnel (P) :**
$$C(z) = K_p$$

**Correcteur proportionnel-intégral (PI) :**
$$C(z) = K_p + K_i\frac{T_e z}{z-1}$$

**Correcteur proportionnel-intégral-dérivé (PID) :**
$$C(z) = K_p + K_i\frac{T_e z}{z-1} + K_d\frac{z-1}{T_e z}$$

**Correcteur RST :**
- Structure polynomiale
- Placement de pôles
- Suivi de trajectoire

### Séries numériques et entières

#### Convergence de séries
- Critère de d'Alembert
- Critère de Cauchy
- Comparaison
- Séries alternées (Leibniz)

#### Développements en série
- Taylor
- Mac Laurin
- Puissances

#### Applications
- Approximations
- Calcul numérique
- Analyse de convergence

## 🛠️ Travaux pratiques

### TP Transformation en Z
- Calcul de transformées
- Transformées inverses
- Propriétés
- Application aux systèmes

### TP Asservissement numérique
**Système étudié :** Position moteur DC

**Étapes :**
1. Modélisation continue
2. Discrétisation (Tustin)
3. Analyse en boucle ouverte
4. Synthèse correcteur PI ou PID
5. Simulation réponse indicielle
6. Validation robustesse

**Outils MATLAB :**
- `c2d()` : Discrétisation
- `tf()`, `zpk()` : Fonctions de transfert
- `rlocus()` : Lieu des racines
- `step()`, `impulse()` : Réponses
- `margin()` : Marges
- `pidtune()` : Synthèse automatique

### TP Comparaison méthodes de discrétisation
- Euler avant/arrière
- Bilinéaire (Tustin)
- Invariance impulsionnelle
- Influence de Te
- Préservation stabilité

### Projet : Asservissement pratique
- Régulation température ou vitesse
- Implémentation sur microcontrôleur
- Correcteur numérique
- Tests et optimisation

## 💻 Outils utilisés

### Simulation
- **MATLAB/Simulink** : Simulation systèmes
- **Control System Toolbox** : Asservissements
- **Python (control)** : Alternative open source
- **Scilab/Xcos** : Open source

### Analyse
- Tracés de Bode, Nyquist
- Lieu des racines
- Diagramme de Black
- Réponses temporelles

### Implémentation
- Code C pour microcontrôleur
- Algorithme PID discret
- Anti-windup
- Filtrage dérivée

## 📊 Évaluation

- Travaux pratiques (40%)
- Projet asservissement (30%)
- Contrôles continus (15%)
- Examen final (15%)

## 🔗 Liens avec d'autres cours

- **Automatique (S3)** : Base continue
- **Filtrage Numérique (S4)** : Filtres numériques
- **IE** : Implémentation embarquée
- **Mathématiques** : Fondements théoriques

## 📐 Exemple d'application

### Régulateur PID numérique

**Algorithme position :**
```matlab
e = r - y;           % Erreur
P = Kp * e;          % Terme proportionnel
I = I + Ki*Te*e;     % Terme intégral
D = Kd/Te * (e - e_prev);  % Terme dérivé
u = P + I + D;       % Commande
e_prev = e;          % Sauvegarde
```

**Algorithme vitesse (incrémentiel) :**
```matlab
delta_u = q0*e[n] + q1*e[n-1] + q2*e[n-2];
u[n] = u[n-1] + delta_u;
```

Avec :
- q0 = Kp + Ki·Te + Kd/Te
- q1 = -Kp - 2·Kd/Te
- q2 = Kd/Te

**Anti-windup :**
```matlab
if u > u_max
    u = u_max;
    I = I - Ki*Te*e;  % Ne pas intégrer
elseif u < u_min
    u = u_min;
    I = I - Ki*Te*e;
end
```

### Système du premier ordre

**Continu :**
$$H(s) = \frac{K}{\tau s + 1}$$

**Discret (Tustin, Te=0.1s, τ=1s, K=1) :**
$$H(z) = \frac{0.0476(z+1)}{z - 0.905}$$

## 💡 Applications pratiques

### Régulation
- Température (four, climatisation)
- Vitesse (moteur)
- Position (robotique)
- Niveau (réservoir)

### Filtrage
- Filtres RII (transformation en Z)
- Égaliseurs
- Correcteurs de phase

### Traitement du signal
- Analyse spectrale
- Détection
- Estimation

## 📖 Compétences développées

- Transformation en Z
- Analyse de systèmes numériques
- Synthèse de correcteurs
- Simulation sous MATLAB
- Implémentation pratique
- Optimisation de performances

## 🎯 Plan en Z (stabilité)

**Cercle unité :**
- Intérieur : stable
- Sur cercle : marginalement stable
- Extérieur : instable

**Correspondance plan s → plan z :**
- Axe imaginaire (s) → Cercle unité (z)
- Demi-plan gauche (s) → Intérieur cercle (z)
- $z = e^{sT_e}$

## ⚠️ Pièges courants

### Discrétisation
- Te trop grand (aliasing, instabilité)
- Méthode inadaptée
- Perte de propriétés (stabilité)
- Retard numérique

### PID numérique
- Windup de l'intégrateur
- Dérivée bruitée
- Saturations
- Quantification

### Implémentation
- Débordements arithmétiques
- Erreurs d'arrondi
- Temps de calcul
- Ordre d'opérations

## 🔧 Bonnes pratiques

### Choix de Te
- Règle : Te < τ/10 (constante temps)
- Shannon : Te < 1/(2·Fmax)
- Compromis : précision vs calcul

### Réglage PID
**Méthode de Ziegler-Nichols (numérique) :**
1. Trouver gain critique Kc
2. Période d'oscillation Tc
3. Calculer Kp, Ki, Kd

**Réglage empirique :**
1. P seul : augmenter jusqu'à oscillation
2. Ajouter I : éliminer erreur statique
3. Ajouter D : réduire dépassement

### Code embarqué
- Variables scaled (éviter float si possible)
- Anti-windup
- Limitation dérivée
- Filtrage bruit capteur

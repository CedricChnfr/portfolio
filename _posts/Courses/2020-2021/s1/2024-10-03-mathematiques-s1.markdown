---
layout: default
title: "Mathématiques - S1"
date: 2024-10-02 10:56:03 +0200
---

<style>
.back-nav { margin-bottom: 20px; }
.back-nav a { text-decoration: none; color: #2a7ae2; font-weight: 600; }
.back-nav a:hover { text-decoration: underline; }
.section-title { color: #2a7ae2; border-bottom: 2px solid #2a7ae2; padding-bottom: 10px; margin-top: 30px; margin-bottom: 20px; }
</style>

<div class="back-nav">
  <a href="./my-courses-2020-2021.html">← Retour à Mes Cours 2020-2021</a>
</div>

# Mathématiques - S1

**Année** : 2020-2021 | **Semestre** : 1 | **Type** : Sciences fondamentales

---

## PART A : PRÉSENTATION GÉNÉRALE

### Contexte et objectifs

Les mathématiques S1 constituent le socle théorique pour l'ingénieur GEII. Elles posent les fondations indispensables pour l'analyse de circuits, le traitement du signal et l'automatique. Le volume horaire est de 60h (30h CM + 30h TD).

**Objectifs :**
- Nombres complexes et applications aux circuits AC
- Fonctions de plusieurs variables
- Équations différentielles (circuits RL, RC, RLC)
- Développements limités
- Intégration (calcul de surfaces, énergies)

### Prérequis
- Terminale scientifique (fonctions, dérivation, intégration)

### Compétences visées
- Maîtriser l'analyse mathématique appliquée aux signaux et systèmes
- Manipuler les nombres complexes dans un contexte d'impédances électriques
- Résoudre des équations différentielles modélisant des systèmes physiques
- Utiliser l'algèbre linéaire pour les systèmes multi-variables
- Appliquer les transformées de Laplace et Fourier aux signaux

---

## PART B : EXPÉRIENCE ET CONTEXTE

### Programme détaillé

#### 1. Analyse réelle (15h)

**Fonctions d'une variable réelle :**
- Limites, continuité, dérivabilité
- Étude de fonctions (monotonie, extrema, convexité)
- Développements limités (DL) au voisinage d'un point
- Séries de Taylor et MacLaurin
- Applications à l'approximation de fonctions

**Intégration :**
- Primitives usuelles et techniques d'intégration
- Intégration par parties et par changement de variable
- Intégrales définies et applications (aires, volumes)
- Intégrales généralisées (convergence)

#### 2. Nombres complexes (12h)

**Représentations :**
- Forme algébrique : z = a + jb
- Forme trigonométrique : z = r(cos θ + j sin θ)
- Forme exponentielle : z = r·e^(jθ) (formule d'Euler)
- Passage d'une forme à l'autre

**Opérations et applications :**
- Addition, multiplication, division, conjugaison
- Module |z| = √(a² + b²), argument arg(z) = arctan(b/a) et propriétés
- Racines n-ièmes d'un nombre complexe
- **Application électrique** : représentation des impédances complexes (Z = R + jX)
- Circuits RLC en régime sinusoïdal

**Applications électricité :**
- Impédances complexes : Z_R = R, Z_L = jLω, Z_C = 1/(jCω)
- Loi d'Ohm complexe : V = Z·I
- Déphasage tension/courant
- Puissance complexe : S = V·I*

#### 3. Algèbre linéaire (15h)

**Vecteurs et espaces vectoriels :**
- Vecteurs de R² et R³
- Opérations vectorielles (addition, multiplication scalaire)
- Produit scalaire, norme, orthogonalité
- Base et dimension

**Matrices :**
- Définitions et opérations (addition, multiplication)
- Matrice transposée, inverse
- Déterminant et calcul (Sarrus, cofacteurs)
- Applications : résolution de systèmes linéaires

**Systèmes d'équations linéaires :**
- Méthode de Gauss (pivot de Gauss)
- Méthode de Cramer
- Interprétation géométrique

**Valeurs et vecteurs propres :**
- Définition et calcul
- Diagonalisation de matrices
- Applications aux systèmes dynamiques

#### 4. Équations différentielles (12h)

**Équations du 1er ordre :**
- Équations à variables séparables
- Équations linéaires du premier ordre : y' + ay = b
- Solution générale et particulière
- Constante de temps τ = 1/a
- Conditions initiales
- Applications : circuit RC (charge/décharge condensateur)

**Équations du 2nd ordre :**
- Équations linéaires à coefficients constants : y'' + 2ζω₀y' + ω₀²y = f(t)
- Résolution de l'équation homogène (racines caractéristiques)
- Solution particulière (second membre)
- Amortissement : ζ < 1 (oscillant), ζ = 1 (critique), ζ > 1 (apériodique)
- Applications : circuits RC, RL, RLC (charge/décharge)

#### 5. Transformations (6h)

**Transformée de Laplace :**
- Définition et propriétés fondamentales
- Transformées usuelles (échelon, exponentielle, sinus, cosinus)
- Théorèmes (linéarité, dérivation, translation)
- Application à la résolution d'équations différentielles

**Transformée de Fourier :**
- Introduction à l'analyse fréquentielle
- Décomposition en série de Fourier
- Spectre fréquentiel d'un signal périodique

### Méthodes pédagogiques

**Cours magistraux (30h) :**
- Exposés théoriques avec démonstrations rigoureuses
- Exemples d'application aux problèmes d'ingénierie
- Support de cours fourni (polycopié)

**Travaux dirigés (30h) :**
- Exercices d'application progressive
- Résolution de problèmes types
- Travail en binômes ou petits groupes
- Corrections détaillées au tableau

**Travail personnel :**
- Exercices à préparer pour chaque TD
- Devoirs à la maison (DM)
- Révision et apprentissage des démonstrations clés

---

## PART C : ASPECTS TECHNIQUES

### Outils mathématiques et logiciels

#### Calculatrices

**Calculatrice scientifique/graphique :**
- Modèles recommandés : TI-83+, TI-84, Casio Graph 35+
- Fonctionnalités utilisées :
  - Calculs avec nombres complexes
  - Résolution d'équations
  - Calcul matriciel
  - Représentation graphique de fonctions
  - Calculs statistiques de base

**Limitations et bonnes pratiques :**
- Vérifier le mode (degrés/radians) pour les fonctions trigonométriques
- Utiliser la notation scientifique pour les très grands/petits nombres
- Éviter les approximations trop précoces dans les calculs

#### Logiciels de calcul numérique

**MATLAB/GNU Octave :**
Utilisés pour les applications numériques et la visualisation.

*Exemples d'utilisation :*

```matlab
% Tracé d'une fonction
x = linspace(-pi, pi, 100);
y = sin(x) .* exp(-x.^2);
plot(x, y);
title('Fonction amortie');

% Résolution d'un système linéaire Ax = b
A = [2, -1, 0; -1, 2, -1; 0, -1, 2];
b = [1; 0; 1];
x = A \ b;  % ou x = inv(A) * b

% Nombres complexes
z1 = 3 + 4i;
z2 = 1 - 2i;
z_prod = z1 * z2;
abs(z1)      % module
angle(z1)    % argument en radians

% Résolution d'équation différentielle
% dy/dt = -2*y + sin(t), y(0) = 1
f = @(t,y) -2*y + sin(t);
[t, y] = ode45(f, [0 10], 1);
plot(t, y);
```

**Python (NumPy, SciPy, SymPy) :**
Alternative open-source pour calculs scientifiques.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import sympy as sp

# Nombres complexes
z1 = 3 + 4j
z2 = complex(1, -2)
print(f"Module: {abs(z1)}")
print(f"Argument: {np.angle(z1)}")

# Algèbre symbolique avec SymPy
x = sp.Symbol('x')
f = sp.sin(x) * sp.exp(-x**2)
f_prime = sp.diff(f, x)  # dérivée
print(sp.latex(f_prime))  # export LaTeX

# Résolution d'équation différentielle
def model(y, t):
    dydt = -2*y + np.sin(t)
    return dydt
y0 = 1
t = np.linspace(0, 10, 100)
y = odeint(model, y0, t)
plt.plot(t, y)
plt.show()
```

### Techniques de résolution

#### Méthode systématique pour les équations différentielles

**Équation du 2nd ordre : ay'' + by' + cy = f(t)**

1. **Résoudre l'équation homogène** ay'' + by' + cy = 0
   - Équation caractéristique : ar² + br + c = 0
   - Calculer Δ = b² - 4ac
   - **Cas 1 (Δ > 0)** : deux racines réelles r₁, r₂ → y_h = C₁e^(r₁t) + C₂e^(r₂t)
   - **Cas 2 (Δ = 0)** : racine double r₀ → y_h = (C₁ + C₂t)e^(r₀t)
   - **Cas 3 (Δ < 0)** : racines complexes α ± jω → y_h = e^(αt)(C₁cos(ωt) + C₂sin(ωt))

2. **Trouver une solution particulière** y_p selon f(t)
   - Si f(t) = A (constante) → y_p = K
   - Si f(t) = Ae^(λt) → y_p = Be^(λt)
   - Si f(t) = A cos(ωt) + B sin(ωt) → y_p = C cos(ωt) + D sin(ωt)

3. **Solution générale** : y = y_h + y_p

4. **Appliquer les conditions initiales** pour déterminer C₁ et C₂

**Exemple : Circuit RLC série**
$$L\frac{d^2i}{dt^2} + R\frac{di}{dt} + \frac{1}{C}i = \frac{dV_s}{dt}$$

#### Calcul matriciel efficace

**Inversion de matrice 2x2 :**
$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \implies A^{-1} = \frac{1}{ad-bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$

**Déterminant 3x3 (règle de Sarrus) :**
```
| a b c |
| d e f | = aei + bfg + cdh - ceg - afh - bdi
| g h i |
```

#### Transformée de Laplace : table des transformées usuelles

| f(t) | F(s) = L{f(t)} |
|------|----------------|
| δ(t) (Dirac) | 1 |
| u(t) (échelon) | 1/s |
| t | 1/s² |
| e^(at) | 1/(s-a) |
| sin(ωt) | ω/(s²+ω²) |
| cos(ωt) | s/(s²+ω²) |
| e^(at)sin(ωt) | ω/((s-a)²+ω²) |

**Théorèmes importants :**
- Dérivation : L{f'(t)} = sF(s) - f(0)
- Intégration : L{∫f(τ)dτ} = F(s)/s
- Translation : L{e^(at)f(t)} = F(s-a)

### Applications pratiques en GEII

#### 1. Circuits électriques en régime sinusoïdal

**Impédances complexes :**
- Résistance : Z_R = R
- Inductance : Z_L = jLω
- Capacité : Z_C = 1/(jCω) = -j/(Cω)

**Loi d'Ohm complexe :** V = Z·I

**Exemple : Diviseur de tension complexe**
```
V_in ──R──┬──C── GND
          │
         V_out
```
$$\underline{V}_{out} = \underline{V}_{in} \cdot \frac{Z_C}{Z_R + Z_C}$$

#### 2. Analyse de circuits RLC

**Circuit RLC série - Réponse transitoire :**

Équation : $$L\frac{di}{dt} + Ri + \frac{1}{C}\int i \, dt = V_s(t)$$

Forme canonique : $$\frac{d^2i}{dt^2} + \frac{R}{L}\frac{di}{dt} + \frac{1}{LC}i = 0$$

**Paramètres caractéristiques :**
- Pulsation propre : ω₀ = 1/√(LC)
- Coefficient d'amortissement : ξ = R/(2√(L/C))
- Régimes : sous-amorti (ξ<1), critique (ξ=1), sur-amorti (ξ>1)

### TD appliqués

**TD1 : Complexes et circuits AC**
- Calcul impédances séries/parallèles
- Diviseur de tension/courant
- Puissance active, réactive, apparente

**TD2 : Équations différentielles**
- Circuit RC : charge condensateur à partir de 0V
- Circuit RLC série : réponse indicielle
- Détermination τ, ω₀, ζ

**TD3 : Intégration**
- Énergie stockée condensateur : E = ½CV²
- Travail d'une force

---

## PART D : ANALYSE ET RÉFLEXION

### Évaluation des compétences

#### Modalités d'évaluation

**Contrôle continu (40%) :**
- 2 contrôles écrits (1h30 chacun)
- Porte sur l'ensemble du cours vu jusqu'à la date du contrôle
- Calculatrice autorisée, formulaire manuscrit A4 recto-verso autorisé

**Travaux dirigés (20%) :**
- Participation et travail en TD
- Devoirs maison (2-3 par semestre)
- Interrogations courtes (10-15 min)

**Examen terminal (40%) :**
- Épreuve de 2h en fin de semestre
- Synthèse de l'ensemble du programme
- Exercices d'application et problème de synthèse
- Calculatrice + formulaire manuscrit autorisés

#### Barème type d'un contrôle

**Exercice 1 - Nombres complexes (5 points) :**
- Calculs de modules et arguments (2 pts)
- Forme exponentielle et applications (2 pts)
- Application circuit RLC (1 pt)

**Exercice 2 - Algèbre linéaire (6 points) :**
- Résolution système 3x3 (3 pts)
- Calcul de déterminant et inverse (2 pts)
- Valeurs propres (1 pt)

**Exercice 3 - Équations différentielles (5 points) :**
- Résolution équation homogène (2 pts)
- Solution particulière (1 pt)
- Conditions initiales (1 pt)
- Interprétation physique (1 pt)

**Exercice 4 - Transformées (4 points) :**
- Calcul de transformée de Laplace (2 pts)
- Application à une équation différentielle (2 pts)

### Compétences acquises et progression

#### Niveaux de maîtrise

**Niveau 1 - Connaissance (fin S1) :**
- Connaître les définitions et propriétés fondamentales
- Appliquer des formules directes
- Résoudre des exercices types simples

**Niveau 2 - Application (S2-S3) :**
- Choisir la bonne méthode selon le problème
- Enchaîner plusieurs étapes de calcul
- Interpréter les résultats

**Niveau 3 - Maîtrise (S3-S4) :**
- Résoudre des problèmes complexes
- Faire le lien entre mathématiques et applications physiques
- Modéliser un système réel

### Liens avec les autres matières

#### Synergie avec le cursus GEII

| Matière | Concepts mathématiques utilisés | Applications concrètes |
|---------|--------------------------------|------------------------|
| **Énergie** | Nombres complexes, équations diff. | Impédances, circuits RLC, régimes transitoires |
| **Systèmes Électroniques** | Nombres complexes, équations diff. | Filtres actifs/passifs, fonctions de transfert |
| **Travaux de Laboratoire** | Analyse, complexes | Mesures en régime sinusoïdal, oscilloscope |
| **Signal (S2)** | Transformées Fourier/Laplace | Spectres, filtrage, convolution |
| **Automatique (S3)** | Équations diff., Laplace, matrices | Modélisation systèmes, stabilité, commande |
| **Programmation** | Algèbre, algorithmes | Implémentation calculs numériques |

#### Progression verticale

**S1 (Mathématiques 1) :**
- Fondations : analyse, complexes, algèbre linéaire, équations diff.

**S2 (Mathématiques 2) :**
- Approfondissement : séries de Fourier, convolution, probabilités
- Fonctions de plusieurs variables

**S3 (Outils Mathématiques pour l'Automatique) :**
- Transformée en Z (signaux discrets)
- Représentation d'état
- Stabilité des systèmes

**S4 (Mathématiques Appliquées) :**
- Optimisation
- Traitement statistique des données
- Méthodes numériques avancées

### Ressources et accompagnement

#### Support de cours

**Documentation fournie :**
- Polycopié de cours complet (120 pages)
- Recueils d'exercices corrigés par chapitre
- Formulaires mathématiques
- Annales d'examens des années précédentes

**Ressources en ligne :**
- Plateforme Moodle avec exercices interactifs
- Vidéos de rappels de cours
- Forums d'entraide entre étudiants

#### Accompagnement personnalisé

**Tutorat :**
- Séances de soutien hebdomadaires (2h/semaine)
- Encadrement par étudiants de 2ème année
- Groupes de 5-8 étudiants maximum

**Heures de permanence :**
- Enseignants disponibles sur rendez-vous
- Questions sur les exercices ou points de cours
- Conseils méthodologiques

### Conseils de réussite

#### Stratégies d'apprentissage

**Pendant le cours :**
- Prendre des notes structurées et lisibles
- Poser des questions sans hésiter
- Refaire les démonstrations importantes chez soi

**Pendant les TD :**
- Préparer les exercices à l'avance
- Ne pas rester bloqué : demander de l'aide rapidement
- Corriger soigneusement ses erreurs

**Travail personnel (estimé : 4h/semaine) :**
- Relire le cours dans les 24h après le CM
- Refaire les exercices de TD sans regarder la correction
- Pratiquer régulièrement (éviter le bachotage)

#### Erreurs fréquentes à éviter

- Confondre radians et degrés (notamment en complexes)
- Oublier les conditions initiales dans les équations différentielles
- Négliger les unités dans les applications physiques
- Faire des erreurs de signes dans le calcul matriciel
- Utiliser la transformée de Laplace sans vérifier les conditions
- Se précipiter sur la calculatrice sans réfléchir à la méthode

### Débouchés et perspectives

#### Utilisation dans la vie professionnelle

**Métiers de l'ingénieur GEII :**
- **Conception électronique** : calculs d'impédances, filtres, dimensionnement
- **Automaticien** : modélisation de systèmes, régulation, asservissement
- **Traitement du signal** : analyse fréquentielle, filtrage numérique
- **Énergie et puissance** : calculs de rendement, facteur de puissance

#### Poursuite d'études

Les mathématiques du S1 sont le socle pour :
- Licence professionnelle (Bac+3)
- Licence générale en EEA (Électronique, Énergie électrique, Automatique)
- École d'ingénieurs (INSA, ENSEEIHT, etc.)
- Master en Électronique, Automatique, Traitement du signal

### Bibliographie et ressources

**Ouvrages de référence :**
1. *Mathématiques pour l'ingénieur* - Jean-Pierre Lecoutre (Dunod)
2. *Analyse mathématique* - Walter Damin (De Boeck)
3. *Mathématiques appliquées à l'électronique* - François Christophe (Ellipses)
4. *Aide-mémoire Mathématiques de l'ingénieur* - Yves Leroyer (Dunod)

**Ressources numériques :**
- Khan Academy (vidéos pédagogiques en français)
- Bibmath.net (cours et exercices)
- Exo7 (cours et exercices université de Lille)
- GeoGebra (visualisation interactive)

**Logiciels gratuits :**
- **GNU Octave** : alternative gratuite à MATLAB
- **Python + Anaconda** : environnement scientifique complet
- **GeoGebra** : géométrie dynamique et graphiques
- **Maxima** : calcul formel open source
- **SageMath** : système complet de mathématiques

---

## Documents de Cours

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Nombres Complexes</h4>
      <p>Cours complet sur les nombres complexes : formes algébrique, trigonométrique et exponentielle. Applications aux impédances électriques et circuits RLC.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S1/MATHS/1_Nombres_complexe.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S1/MATHS/1_Nombres_complexe.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Télécharger le PDF
        </a>
      </p>
    </div>
    <div class="pdf-item">
      <h4>Limites d'une fonction numérique</h4>
      <p>Étude des limites de fonctions numériques : définitions, propriétés, théorèmes fondamentaux et applications.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S1/MATHS/2_Limites_d'une_fct_numérique.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S1/MATHS/2_Limites_d'une_fct_numérique.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Télécharger le PDF
        </a>
      </p>
    </div>
    <div class="pdf-item">
      <h4>Propriétés d'une fonction numérique</h4>
      <p>Propriétés des fonctions numériques : continuité, dérivabilité, étude de fonctions et applications.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S1/MATHS/3_Propriété_d'une_fct_numérique.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S1/MATHS/3_Propriété_d'une_fct_numérique.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Télécharger le PDF
        </a>
      </p>
    </div>
  </div>
</div>

---

<style>body{font-family:Arial,sans-serif;background-color:#f4f4f9;color:#333;line-height:1.6}h2,h3,h4,h5{color:#2a7ae2}p{text-align:justify}code{background-color:#f5f5f5;padding:2px 6px;border-radius:3px;font-family:'Courier New',monospace}pre{background-color:#f5f5f5;padding:15px;border-radius:5px;overflow-x:auto}</style>

<div class="back-nav">
  <a href="./my-courses-2020-2021.html">← Retour à Mes Cours 2020-2021</a>
</div>

---
layout: default
title: "Systemes Electroniques (SE) - S2"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
---

<style>
.back-nav { margin-bottom: 20px; }
.back-nav a { text-decoration: none; color: #2a7ae2; font-weight: 600; }
.back-nav a:hover { text-decoration: underline; }
.section-title { color: #2a7ae2; border-bottom: 2px solid #2a7ae2; padding-bottom: 10px; margin-top: 30px; margin-bottom: 20px; }
</style>

<div class="back-nav">
  <a href="./my-courses-2020-2021.html">← Retour a Mes Cours 2020-2021</a>
</div>

# Systemes Electroniques (SE) - S2

**Annee**: 2020-2021 | **Semestre**: 2 | **Type**: Electronique

---

## PART A : PRESENTATION GENERALE

### Contexte et objectifs

Le cours de Systemes Electroniques du semestre 2 couvre l'analyse des systemes electroniques du point de vue frequentiel et temporel. Il introduit les outils mathematiques et les methodes d'analyse necessaires pour comprendre et concevoir des circuits electroniques analogiques. Le programme s'articule autour de 7 chapitres, allant des quadripoles aux applications de l'amplificateur operationnel, en passant par les filtres passifs et la modulation d'amplitude.

**Objectifs pedagogiques :**
- Analyser des reseaux a quatre bornes (quadripoles) a l'aide de matrices impedance et admittance
- Etudier la reponse transitoire des circuits du premier ordre (RC, RL)
- Maitriser la representation frequentielle (diagrammes de Bode) et temporelle des systemes
- Concevoir et dimensionner des filtres passifs (passe-bas, passe-haut, passe-bande)
- Comprendre les principes de la modulation d'amplitude (AM)
- Appliquer les amplificateurs operationnels dans des montages avances

### Organisation du cours

Le cours est organise en 7 chapitres suivant une progression logique :
1. **Chapitre 1** : Quadripoles (reseaux a quatre bornes)
2. **Chapitre 3** : Circuits du premier ordre (passe-bas, passe-haut)
3. **Chapitre 4** : Filtres passifs et reponse frequentielle
4. **Chapitre 5** : Amplificateur operationnel (AOP) - applications avancees
5. **Chapitre 6** : Representation temporelle et frequentielle
6. **Chapitre 7** : Modulation d'amplitude (AM)
7. **TD et exercices** : Fascicules de TD pour mise en pratique

### Competences visees (BUT GEII)

Ce module contribue au bloc de competences "Electronique et Systemes" :
- Analyser le comportement frequentiel d'un circuit
- Concevoir des filtres analogiques passifs
- Utiliser les diagrammes de Bode pour caracteriser un systeme
- Comprendre les principes de modulation pour les telecommunications

---

## PART B : EXPERIENCE ET CONTEXTE

### Environnement pedagogique

L'enseignement de Systemes Electroniques se deroule sous forme de cours magistraux, de travaux diriges (TD) et de travaux de laboratoire (TL). Les TD permettent de mettre en pratique les concepts theoriques par le calcul, tandis que les TL offrent une confrontation directe avec les circuits reels sur les bancs de mesure de l'IUT.

### Deroulement du semestre

Le semestre a ete marque par la situation sanitaire (2020-2021), avec une alternance entre cours en presentiel et cours a distance. Les TD ont ete realises en partie en distanciel, avec des fascicules de TD detailles fournis par les enseignants. Les TL ont ete maintenus en presentiel autant que possible pour permettre la manipulation des instruments de mesure.

### Outils et instruments utilises

- **Oscilloscope numerique** : Visualisation des signaux temporels, mesure de dephasage et d'amplitude
- **Generateur de fonctions** : Generation de signaux sinusoidaux, carres, triangulaires pour les tests
- **Multimetre de precision** : Mesures de tensions, courants, impedances
- **LTspice** : Simulation de circuits analogiques pour verification des calculs
- **Calculatrice scientifique** : Calculs de fonctions de transfert, conversion dB

### Liens avec d'autres cours

- **Mathematiques S2** : Nombres complexes, transformees de Laplace, equations differentielles
- **OL (Outils Logiciels)** : Transformation de Laplace, series de Fourier
- **TL (Travaux de Laboratoire)** : Mise en pratique sur circuits reels
- **Energie** : Circuits triphases et puissance
- **Programmation S3+** : Simulation numerique de filtres

---

## PART C : ASPECTS TECHNIQUES

### Chapitre 1 : Quadripoles (Reseaux a quatre bornes)

Un quadripole est un reseau electrique a deux ports (quatre bornes) : un port d'entree et un port de sortie. Il est caracterise par les relations entre les tensions et courants d'entree et de sortie.

#### Matrices impedance et admittance

La **matrice impedance [Z]** relie les tensions aux courants :

```
| V1 |   | Z11  Z12 |   | I1 |
|    | = |          | x |    |
| V2 |   | Z21  Z22 |   | I2 |
```

Ou :
- Z11 = V1/I1 (quand I2 = 0) : impedance d'entree a vide
- Z22 = V2/I2 (quand I1 = 0) : impedance de sortie a vide
- Z12 = V1/I2 (quand I1 = 0) : impedance de transfert inverse
- Z21 = V2/I1 (quand I2 = 0) : impedance de transfert directe

La **matrice admittance [Y]** est l'inverse de la matrice impedance :

```
| I1 |   | Y11  Y12 |   | V1 |
|    | = |          | x |    |
| I2 |   | Y21  Y22 |   | V2 |

avec [Y] = [Z]^(-1)
```

#### Matrice de chaine (ABCD)

Pour la mise en cascade de quadripoles, on utilise la matrice chaine :

```
| V1 |   | A  B |   |  V2 |
|    | = |      | x |     |
| I1 |   | C  D |   | -I2 |
```

L'avantage de cette representation est que la mise en cascade de deux quadripoles revient a multiplier leurs matrices :

```
[T_total] = [T1] x [T2]
```

#### Exemples de matrices ABCD pour des elements simples

Pour une **impedance serie Z** :
```
| A  B |   | 1  Z |
|      | = |      |
| C  D |   | 0  1 |
```

Pour une **admittance parallele Y** :
```
| A  B |   | 1  0 |
|      | = |      |
| C  D |   | Y  1 |
```

### Chapitre 2 : Circuits du premier ordre

Les circuits du premier ordre contiennent un seul element reactif (condensateur C ou inductance L) associe a des resistances.

#### Circuit RC serie - Reponse a un echelon

Pour un circuit RC serie soumis a un echelon de tension E :

**Equation differentielle :**
```
RC * dVc/dt + Vc = E
```

**Solution (charge du condensateur) :**
```
Vc(t) = E * (1 - exp(-t / tau))

avec tau = RC  (constante de temps)
```

**Solution (decharge du condensateur) :**
```
Vc(t) = E * exp(-t / tau)
```

La constante de temps tau = RC determine la vitesse de reponse :
- A t = tau : Vc atteint 63.2% de la valeur finale
- A t = 3*tau : Vc atteint 95% de la valeur finale
- A t = 5*tau : Vc atteint 99.3% de la valeur finale (regime permanent)

#### Circuit RL serie - Reponse a un echelon

Pour un circuit RL serie soumis a un echelon de tension E :

**Equation differentielle :**
```
L * dI/dt + R * I = E
```

**Solution :**
```
I(t) = (E/R) * (1 - exp(-t / tau))

avec tau = L/R  (constante de temps)
```

#### Regime transitoire et regime permanent

Le regime transitoire correspond a la phase pendant laquelle le circuit evolue vers son etat d'equilibre. En pratique, on considere que le regime permanent est atteint apres 5 constantes de temps (5*tau). Durant cette phase transitoire, l'energie est stockee ou restituee par l'element reactif (C ou L).

### Chapitre 3 : Representation frequentielle et diagrammes de Bode

La representation frequentielle permet d'etudier le comportement d'un circuit en fonction de la frequence du signal d'entree.

#### Fonction de transfert

La fonction de transfert H(jw) est le rapport entre la tension de sortie et la tension d'entree en regime sinusoidal permanent :

```
H(jw) = Vs / Ve
```

Elle est caracterisee par :
- Le **module** : |H(jw)| (gain)
- La **phase** : arg(H(jw)) (dephasage entre sortie et entree)

#### Diagramme de Bode

Le diagramme de Bode represente le module et la phase de H(jw) en fonction de la frequence en echelle logarithmique :

**Gain en decibels :**
```
|H(jw)|_dB = 20 * log10(|H(jw)|)
```

**Echelle de frequence** : axe horizontal en log10(f) ou log10(w)

**Conventions :**
- Pente de +20 dB/decade pour un zero
- Pente de -20 dB/decade pour un pole
- La frequence de coupure fc est definie a -3 dB du gain maximal

#### Filtre passe-bas RC du premier ordre

**Fonction de transfert :**
```
H(jw) = 1 / (1 + j*R*C*w)
       = 1 / (1 + j*w/wc)

avec wc = 1/(R*C)  et  fc = 1/(2*pi*R*C)
```

**Module :**
```
|H(jw)| = 1 / sqrt(1 + (w/wc)^2)
```

**Phase :**
```
phi(w) = -arctan(w/wc)
```

**Comportement asymptotique :**
- Pour w << wc : |H| = 1 (0 dB), phi = 0 degres
- Pour w = wc : |H| = 1/sqrt(2) (-3 dB), phi = -45 degres
- Pour w >> wc : |H| tend vers wc/w (-20 dB/decade), phi tend vers -90 degres

#### Filtre passe-haut RC du premier ordre

**Fonction de transfert :**
```
H(jw) = j*R*C*w / (1 + j*R*C*w)
       = j*w/wc / (1 + j*w/wc)
```

**Module :**
```
|H(jw)| = (w/wc) / sqrt(1 + (w/wc)^2)
```

**Comportement asymptotique :**
- Pour w << wc : |H| tend vers w/wc (+20 dB/decade), phi tend vers +90 degres
- Pour w = wc : |H| = 1/sqrt(2) (-3 dB), phi = +45 degres
- Pour w >> wc : |H| = 1 (0 dB), phi = 0 degres

### Chapitre 4 : Filtres passifs du second ordre (RLC)

#### Filtre passe-bande RLC serie

Pour un circuit RLC serie, la tension aux bornes de la resistance constitue un filtre passe-bande :

**Fonction de transfert :**
```
H(jw) = (R / L) * jw / ((jw)^2 + (R/L)*jw + 1/(L*C))
```

**Parametres caracteristiques :**
```
Frequence de resonance : f0 = 1 / (2*pi*sqrt(L*C))
Pulsation de resonance : w0 = 1 / sqrt(L*C)
Facteur de qualite :     Q = (1/R) * sqrt(L/C) = L*w0/R
Bande passante :         Bp = f0 / Q = R / (2*pi*L)
```

Le facteur de qualite Q determine la selectivite du filtre :
- Q eleve : filtre tres selectif (bande passante etroite)
- Q faible : filtre peu selectif (bande passante large)

#### Filtre passe-bas RLC serie

La tension aux bornes du condensateur dans un circuit RLC serie forme un filtre passe-bas du second ordre :

**Fonction de transfert :**
```
H(jw) = 1 / (1 - (w/w0)^2 + j*(w/(Q*w0)))

avec w0 = 1/sqrt(L*C) et Q = (1/R)*sqrt(L/C)
```

**Regimes selon Q :**
- Q < 0.5 : regime sur-amorti (pas de depassement)
- Q = 0.5 : regime critique (reponse la plus rapide sans depassement)
- Q > 0.5 : regime sous-amorti (oscillations amorties)

A la resonance (w = w0), le gain peut etre superieur a 1 (surtension) si Q > 1/sqrt(2).

#### Filtre coupe-bande (rejecteur)

Le filtre coupe-bande RLC est l'inverse du passe-bande. La tension aux bornes de l'association serie LC constitue un filtre rejecteur :

**Fonction de transfert :**
```
H(jw) = (1 - (w/w0)^2) / (1 - (w/w0)^2 + j*(w/(Q*w0)))
```

A la frequence de resonance w0, le gain est nul (rejection totale en theorie).

### Chapitre 5 : Amplificateur Operationnel (AOP)

#### Rappels sur l'AOP ideal

L'AOP ideal est caracterise par :
- Impedance d'entree infinie (courants d'entree nuls : I+ = I- = 0)
- Impedance de sortie nulle
- Gain differentiel infini en boucle ouverte
- Bande passante infinie

En regime lineaire (avec contre-reaction negative) : V+ = V- (tension differentielle nulle).

#### Amplificateur differentiel

Le montage differentiel amplifie la difference entre deux signaux d'entree :

```
         R1         R2
V1 ---/\/\/\---+---/\/\/\--- Vs
               |
              (-) AOP
               |
              (+)
               |
V2 ---/\/\/\---+---/\/\/\--- GND
         R3         R4
```

**Tension de sortie :**
```
Si R1 = R3 et R2 = R4 :
Vs = (R2/R1) * (V2 - V1)

Gain differentiel : Ad = R2/R1
```

Le taux de rejection du mode commun (CMRR) mesure la capacite du montage a rejeter les signaux communs aux deux entrees. En pratique, il est essentiel d'apparier les resistances pour maximiser le CMRR.

#### Amplificateur d'instrumentation

L'amplificateur d'instrumentation est constitue de trois AOP et offre :
- Impedance d'entree tres elevee (etage d'entree non-inverseur)
- Gain reglable par une seule resistance (Rg)
- Excellent CMRR

**Gain :**
```
Vs = (1 + 2*R1/Rg) * (R3/R2) * (V2 - V1)
```

Cet amplificateur est utilise dans les chaines de mesure avec des capteurs (ponts de Wheatstone, thermocouples) ou les signaux sont faibles et differentiels.

### Chapitre 6 : Representation temporelle

#### Reponse indicielle (a un echelon)

La reponse indicielle d'un systeme du second ordre depend de son amortissement :

**Cas sous-amorti (Q > 0.5) :**
```
s(t) = 1 - (1/sqrt(1-xi^2)) * exp(-xi*w0*t) * sin(wd*t + phi)

avec xi = 1/(2Q) (coefficient d'amortissement)
     wd = w0*sqrt(1 - xi^2) (pulsation des oscillations amorties)
     phi = arccos(xi)
```

**Parametres de la reponse indicielle :**
- Temps de montee (tr) : temps pour passer de 10% a 90% de la valeur finale
- Depassement (D%) : amplitude du premier depassement en pourcentage
- Temps de reponse a 5% (t5%) : temps pour rester dans une bande de +/- 5% de la valeur finale

#### Reponse impulsionnelle

La reponse impulsionnelle h(t) est la derivee de la reponse indicielle. Elle est fondamentale pour l'analyse des systemes lineaires car la sortie d'un systeme est le produit de convolution de l'entree par h(t).

### Chapitre 7 : Modulation d'amplitude (AM)

#### Principe de la modulation AM

La modulation d'amplitude consiste a faire varier l'amplitude d'une porteuse haute frequence en fonction d'un signal modulant basse frequence.

**Signal module AM :**
```
s(t) = A * [1 + m * cos(2*pi*fm*t)] * cos(2*pi*fc*t)
```

Ou :
- A : amplitude de la porteuse
- m : indice de modulation (0 < m <= 1 pour eviter la surmodulation)
- fm : frequence du signal modulant
- fc : frequence de la porteuse (fc >> fm)

#### Spectre du signal AM

Le spectre du signal AM est compose de trois raies :
- La porteuse a fc avec une amplitude A
- La bande laterale superieure a (fc + fm) avec une amplitude m*A/2
- La bande laterale inferieure a (fc - fm) avec une amplitude m*A/2

**Bande passante du signal AM :**
```
B = 2 * fm
```

#### Indice de modulation

L'indice de modulation m determine la profondeur de la modulation :
```
m = Amax - Amin / (Amax + Amin)
```

Ou Amax et Amin sont les amplitudes maximale et minimale de l'enveloppe du signal module.

- Si m < 1 : modulation correcte, l'enveloppe reproduit fidelement le signal modulant
- Si m = 1 : modulation a 100%, l'enveloppe touche zero
- Si m > 1 : surmodulation, distorsion du signal (a eviter)

#### Puissance du signal AM

```
Puissance totale : Pt = Pc * (1 + m^2/2)
Puissance porteuse : Pc = A^2 / 2
Rendement : eta = m^2 / (2 + m^2)
```

Le rendement maximal est de 33% pour m = 1, ce qui signifie que les deux tiers de la puissance sont gaspilles dans la porteuse. C'est un inconvenient majeur de la modulation AM classique.

#### Demodulation par detection d'enveloppe

La detection d'enveloppe est la methode la plus simple de demodulation AM :
1. Le signal AM est redresse par une diode (demi-onde ou onde complete)
2. Un filtre RC passe-bas extrait l'enveloppe du signal
3. Un condensateur de liaison supprime la composante continue

**Condition de bon fonctionnement du detecteur d'enveloppe :**
```
1/fc << R*C << 1/fm
```

Le circuit RC doit etre assez rapide pour suivre les variations de l'enveloppe (fm) mais assez lent pour lisser les oscillations de la porteuse (fc).

### Travaux diriges et exercices pratiques

Les TD du cours de SE S2 couvrent l'ensemble des chapitres avec des exercices progressifs :

- **TD1** : Calculs de matrices de quadripoles, mise en cascade
- **TD2** : Circuits RC et RL du premier ordre, calculs de constantes de temps
- **TD8-TD10** : Exercices avances sur les filtres, la modulation et l'AOP

Chaque TD comprend des exercices de calcul suivis d'applications pratiques et de verifications par simulation.

---

## PART D : ANALYSE ET REFLEXION

### Competences acquises

- Capacite a analyser un circuit electronique dans le domaine frequentiel
- Maitrise des diagrammes de Bode pour la caracterisation de systemes
- Comprehension des filtres passifs et de leur dimensionnement
- Connaissance des principes de modulation/demodulation AM
- Utilisation des quadripoles pour l'analyse de circuits complexes
- Comprehension du lien entre representations temporelle et frequentielle

### Points forts du cours

Le cours de SE S2 offre une progression pedagogique bien construite : il part des outils mathematiques (quadripoles, fonctions de transfert) pour arriver aux applications concretes (filtres, modulation). La combinaison theorie/TD/TL permet une assimilation solide des concepts. L'etude de la modulation AM introduit le domaine des telecommunications, un atout pour les semestres suivants.

### Difficultes rencontrees

Les diagrammes de Bode et le passage entre domaines temporel et frequentiel ont necessite un temps d'adaptation. La rigueur mathematique requise (nombres complexes, logarithmes, exponentielles) est significative. La situation sanitaire a rendu certains TP de laboratoire plus difficiles a realiser, mais les simulations LTspice ont permis de compenser en partie.

### Connexions interdisciplinaires

- **Mathematiques S2** : Les transformees de Laplace et les nombres complexes sont les outils fondamentaux de l'analyse frequentielle
- **TL S2** : Les travaux de laboratoire mettent en pratique les concepts de SE (filtres, Bode, modulation)
- **Signal S3** : Les bases acquises en SE S2 preparent directement au cours de traitement du signal
- **Electronique S3-S5** : Les filtres actifs et les amplificateurs seront approfondis dans les semestres suivants

### Auto-evaluation

Ce cours a ete l'un des plus exigeants du semestre en termes de rigueur mathematique, mais aussi l'un des plus formateurs. La capacite a "lire" un diagramme de Bode et a en deduire le comportement d'un circuit est une competence fondamentale que j'utilise regulierement dans les cours suivants. La modulation AM, bien que classique, a ouvert les portes de la comprehension des systemes de telecommunications.

---

## Documents de Cours

### Cours - Chapitres

<div class="pdf-item">
  <h4>Chapitre 1 : Quadripoles</h4>
  <p>Polycopie de cours sur les quadripoles : matrices impedance, admittance, hybride et chaine. Mise en cascade de quadripoles et applications aux circuits electroniques.</p>
  <embed src="/cours-pdf/S2/SE/Chap1_Polycopie_cours_quadripoles.pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/cours-pdf/S2/SE/Chap1_Polycopie_cours_quadripoles.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
  </p>
</div>

<div class="pdf-item">
  <h4>Chapitre 3 : Circuits du premier ordre - Passe-bas et Passe-haut</h4>
  <p>Etude des circuits RC et RL du premier ordre : reponse temporelle, constante de temps, fonctions de transfert et diagrammes de Bode des filtres passe-bas et passe-haut.</p>
  <embed src="/cours-pdf/S2/SE/chap3_circuits_premier_ordre_passe_bas_passe_haut.pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/cours-pdf/S2/SE/chap3_circuits_premier_ordre_passe_bas_passe_haut.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
  </p>
</div>

<div class="pdf-item">
  <h4>Chapitre 4 : Filtres passifs et reponse frequentielle</h4>
  <p>Approfondissement des filtres passifs : filtres du second ordre RLC, facteur de qualite, frequence de resonance, bande passante et selectivite.</p>
  <embed src="/cours-pdf/S2/SE/CHAP4_2021.pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/cours-pdf/S2/SE/CHAP4_2021.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
  </p>
</div>

<div class="pdf-item">
  <h4>Chapitre 5 : Amplificateur Operationnel - Applications avancees</h4>
  <p>Applications de l'AOP : amplificateur differentiel, amplificateur d'instrumentation, montages non-lineaires et applications en conditionnement de signal.</p>
  <embed src="/cours-pdf/S2/SE/Chap5_SE.pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/cours-pdf/S2/SE/Chap5_SE.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
  </p>
</div>

<div class="pdf-item">
  <h4>Chapitre 6 : Representation temporelle et frequentielle</h4>
  <p>Liens entre les domaines temporel et frequentiel : reponse indicielle, reponse impulsionnelle, transformee de Fourier et analyse spectrale des systemes.</p>
  <embed src="/cours-pdf/S2/SE/Chap6_Representation-temporelle-frequentielle.pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/cours-pdf/S2/SE/Chap6_Representation-temporelle-frequentielle.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
  </p>
</div>

<div class="pdf-item">
  <h4>Chapitre 7 : Modulation d'amplitude (AM)</h4>
  <p>Principes de la modulation AM : signal module, spectre, indice de modulation, puissance, demodulation par detection d'enveloppe. Applications en radiocommunication.</p>
  <embed src="/cours-pdf/S2/SE/Chap7_modulation_AM.pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/cours-pdf/S2/SE/Chap7_modulation_AM.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
  </p>
</div>

### Travaux Diriges

<div class="pdf-item">
  <h4>TD1 : Exercices sur les quadripoles et circuits de base</h4>
  <p>Premier fascicule de travaux diriges : exercices sur les quadripoles, calculs de matrices, et circuits du premier ordre.</p>
  <embed src="/cours-pdf/S2/SE/TD1_(en_2_seances).pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/cours-pdf/S2/SE/TD1_(en_2_seances).pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
  </p>
</div>

<div class="pdf-item">
  <h4>TD2 : Exercices sur les filtres et la reponse frequentielle</h4>
  <p>Deuxieme fascicule de TD : exercices sur les filtres passe-bas, passe-haut, diagrammes de Bode et fonctions de transfert.</p>
  <embed src="/cours-pdf/S2/SE/TD2.pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/cours-pdf/S2/SE/TD2.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
  </p>
</div>

<div class="pdf-item">
  <h4>Fascicule TD complet (M. Bourennane)</h4>
  <p>Fascicule complet de travaux diriges couvrant l'ensemble du programme de SE S2, avec exercices corriges et applications.</p>
  <embed src="/cours-pdf/S2/SE/Fascicule_TD_BOURENNANE_2020_2021.pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/cours-pdf/S2/SE/Fascicule_TD_BOURENNANE_2020_2021.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
  </p>
</div>

<div class="pdf-item">
  <h4>TD8 a TD10 : Exercices avances</h4>
  <p>Fascicule de TD avances portant sur la modulation AM, les amplificateurs d'instrumentation et les applications de synthese.</p>
  <embed src="/cours-pdf/S2/SE/fascicule_TD8_a_TD10_SE_S2_2021.pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/cours-pdf/S2/SE/fascicule_TD8_a_TD10_SE_S2_2021.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
  </p>
</div>

---

<style>body{font-family:Arial,sans-serif;background-color:#f4f4f9;color:#333;line-height:1.6}h2,h3,h4,h5{color:#2a7ae2}p{text-align:justify}code{background-color:#f5f5f5;padding:2px 6px;border-radius:3px;font-family:'Courier New',monospace}pre{background-color:#f5f5f5;padding:15px;border-radius:5px;overflow-x:auto}</style>

<div class="back-nav">
  <a href="./my-courses-2020-2021.html">← Retour a Mes Cours 2020-2021</a>
</div>

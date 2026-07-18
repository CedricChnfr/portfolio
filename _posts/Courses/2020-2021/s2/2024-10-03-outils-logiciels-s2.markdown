---
layout: default
title: "Outils Logiciels (OL) - S2"
date: 2024-10-02 10:56:03 +0200
---

<style>
.back-nav { margin-bottom: 20px; }
.back-nav a { text-decoration: none; color: #2a7ae2; font-weight: 600; }
.back-nav a:hover { text-decoration: underline; }
.section-title { color: #2a7ae2; border-bottom: 2px solid #2a7ae2; padding-bottom: 10px; margin-top: 30px; margin-bottom: 20px; }
</style>

<div class="back-nav">
  <a href="./my-courses-2020-2021.html">&larr; Retour a Mes Cours 2020-2021</a>
</div>

# Outils Logiciels (OL) - S2

**Annee**: 2020-2021 | **Semestre**: 2 | **Type**: Scientifique / Outils

---

## PART A : PRESENTATION GENERALE

### Contexte et objectifs

Le cours d'Outils Logiciels du semestre 2 est consacre a l'analyse mathematique des signaux. Il s'agit d'un cours fondamental qui introduit deux outils mathematiques majeurs utilises en electronique, en automatique et en traitement du signal : les **series de Fourier** et la **transformee de Laplace**.

Les series de Fourier permettent de decomposer tout signal periodique en une somme de sinusoides, ce qui est la base de l'analyse frequentielle. La transformee de Laplace permet de transformer les equations differentielles en equations algebriques, simplifiant considerablement l'analyse des circuits et des systemes lineaires.

Ces deux outils sont complementaires : Fourier s'applique aux signaux periodiques en regime permanent, tandis que Laplace traite les regimes transitoires et les systemes avec conditions initiales.

**Objectifs pedagogiques :**
- Comprendre et calculer les coefficients de Fourier d'un signal periodique
- Maitriser le passage entre representation temporelle et representation frequentielle
- Connaitre la definition et les proprietes de la transformee de Laplace
- Savoir calculer des transformees directes et inverses de Laplace
- Appliquer la transformee de Laplace a la resolution d'equations differentielles
- Utiliser Laplace pour l'analyse de circuits electriques (fonctions de transfert)

### Organisation

Le cours est structure en deux grands modules :

**Module 1 : Series de Fourier** (environ la moitie du semestre)
- Cours magistraux sur la theorie
- Exercices diriges avec corrections detaillees
- Application a des signaux classiques (creneau, triangle, dent de scie)

**Module 2 : Transformee de Laplace** (seconde moitie du semestre)
- Cours magistraux sur la definition et les proprietes
- Exercices de calcul de transformees directes et inverses
- Application a la resolution d'equations differentielles et a l'analyse de circuits

### Prerequis

- Calcul integral (primitives, integrales definies) - cours de Mathematiques S2
- Nombres complexes (forme exponentielle, module, argument)
- Fractions rationnelles et decomposition en elements simples
- Equations differentielles du 1er et 2eme ordre
- Fonctions trigonometriques et leurs proprietes

---

## PART B : EXPERIENCE ET CONTEXTE

### Environnement pedagogique

Ce cours est etroitement lie au cours de Mathematiques du S2, dont il constitue une application directe. Les integrales, les fractions rationnelles et les equations differentielles etudiees en mathematiques trouvent ici leur utilisation concrete dans l'analyse des signaux et des systemes electroniques.

L'annee 2020-2021 etant marquee par l'enseignement a distance, les exercices diriges ont ete adaptes avec des polycopies detailles et des corrections pas a pas, permettant un travail autonome efficace.

### Ressources et supports

- **Polycopie de cours** : Document de reference sur les series de Fourier (poly1_S2_OL)
- **Cours Transformee de Laplace** : Support complet sur la definition, les proprietes et les applications
- **Fascicules d'exercices corriges** : Exercices de Fourier et de Laplace avec solutions detaillees
- **Documents complementaires** : Resolution analytique des equations differentielles par Laplace
- **Annales** : Sujets d'examens sur les series de Fourier

### Liens avec d'autres cours

- **Mathematiques (S2)** : Ce cours utilise directement le calcul integral pour les coefficients de Fourier, et les fractions rationnelles pour les transformees inverses de Laplace. Les equations differentielles resolues en maths sont ici resolues par une approche algebrique via Laplace.
- **Systemes Electroniques (SE)** : Les fonctions de transfert en s introduites ici sont le langage de l'analyse frequentielle des filtres et amplificateurs.
- **Travaux de Laboratoire (TL)** : Les filtres du 2eme ordre etudies en TP sont analyses theoriquement grace a Laplace. La reponse frequentielle mesuree est reliee aux series de Fourier.
- **Energie** : L'analyse harmonique des signaux en triphase (contenu spectral des signaux redresses) utilise les series de Fourier.
- **Cours ulterieurs (S3-S4)** : L'automatique, la regulation et le traitement du signal numerique s'appuient entierement sur Fourier et Laplace.

### Difficultes et apprentissages

La principale difficulte reside dans le passage du concret (un signal mesure sur un oscilloscope) a l'abstrait (sa decomposition en series de Fourier ou sa transformee de Laplace). Le calcul des coefficients de Fourier exige de la rigueur dans les integrales, et la transformee inverse de Laplace necessite une bonne maitrise de la decomposition en elements simples.

---

## PART C : ASPECTS TECHNIQUES

### Module 1 : Series de Fourier

#### Principe fondamental

Le theoreme de Fourier affirme que tout signal periodique f(t) de periode T peut etre decompose en une somme (eventuellement infinie) de fonctions sinusoidales dont les frequences sont des multiples entiers de la frequence fondamentale f_0 = 1/T.

**Decomposition trigonometrique :**

f(t) = a_0/2 + somme de n=1 a l'infini de [a_n * cos(n*w*t) + b_n * sin(n*w*t)]

ou w = 2*pi/T = 2*pi*f_0 est la pulsation fondamentale.

#### Calcul des coefficients

**Coefficient constant (valeur moyenne) :**

a_0 = (2/T) * integrale de 0 a T de f(t) dt

Note : a_0/2 represente la composante continue (valeur moyenne) du signal.

**Coefficients en cosinus :**

a_n = (2/T) * integrale de 0 a T de f(t) * cos(n*w*t) dt

**Coefficients en sinus :**

b_n = (2/T) * integrale de 0 a T de f(t) * sin(n*w*t) dt

**Amplitude et phase du n-ieme harmonique :**

c_n = sqrt(a_n^2 + b_n^2)

phi_n = arctan(-b_n / a_n)

f(t) = a_0/2 + somme de n=1 a l'infini de c_n * cos(n*w*t + phi_n)

#### Forme complexe (coefficients complexes)

**Formule de decomposition :**

f(t) = somme de n = -infini a +infini de C_n * e^(j*n*w*t)

**Coefficients complexes :**

C_n = (1/T) * integrale de 0 a T de f(t) * e^(-j*n*w*t) dt

**Relations avec les coefficients reels :**
- C_0 = a_0/2
- Pour n >= 1 : C_n = (a_n - j*b_n)/2
- Pour n <= -1 : C_(-n) = (a_n + j*b_n)/2 = C_n* (conjugue)
- |C_n| = c_n / 2

#### Proprietes de symetrie (simplifications)

**Signal pair** (f(-t) = f(t)) : b_n = 0 pour tout n (pas de termes en sinus)
- La decomposition ne contient que des cosinus.
- Exemple : signal triangle symetrique.

**Signal impair** (f(-t) = -f(t)) : a_n = 0 pour tout n (pas de termes en cosinus)
- La decomposition ne contient que des sinus.
- Exemple : signal creneau centre.

**Symetrie de glissement** (demi-onde) : f(t + T/2) = -f(t)
- Seuls les harmoniques impairs sont non nuls (a_2k = b_2k = 0).
- Exemple : signal carre symetrique.

#### Exemple 1 : Signal carre (creneau)

Signal carre de periode T, d'amplitude A, valant +A sur [0, T/2[ et -A sur [T/2, T[ :

Ce signal est impair (si centre) et possede la symetrie de demi-onde, donc seuls les b_n impairs sont non nuls.

**Calcul de a_0 :**
a_0 = (2/T) * [integrale de 0 a T/2 de A dt + integrale de T/2 a T de (-A) dt]
a_0 = (2/T) * [A*T/2 - A*T/2] = 0 (valeur moyenne nulle, logique par symetrie)

**Calcul de b_n :**
b_n = (2/T) * [integrale de 0 a T/2 de A*sin(n*w*t) dt + integrale de T/2 a T de (-A)*sin(n*w*t) dt]
b_n = (2A/T) * [-cos(n*w*t)/(n*w)] de 0 a T/2 + (2A/T) * [cos(n*w*t)/(n*w)] de T/2 a T

Apres calcul :
- b_n = 4A/(n*pi) pour n impair
- b_n = 0 pour n pair

**Decomposition en serie de Fourier :**
f(t) = (4A/pi) * [sin(w*t) + (1/3)*sin(3*w*t) + (1/5)*sin(5*w*t) + (1/7)*sin(7*w*t) + ...]

f(t) = (4A/pi) * somme de k=0 a l'infini de sin((2k+1)*w*t) / (2k+1)

On observe que l'amplitude des harmoniques decroit en 1/n. L'harmonique fondamental (n=1) a une amplitude de 4A/pi = 1.27A, soit 27% de plus que l'amplitude du signal carre. Plus on ajoute d'harmoniques, plus la reconstruction se rapproche du signal original (phenomene de Gibbs aux discontinuites).

#### Exemple 2 : Signal triangulaire

Signal triangulaire symetrique de periode T, d'amplitude A :
- f(t) = (4A/T)*t pour t dans [0, T/4]
- f(t) = 2A - (4A/T)*t pour t dans [T/4, 3T/4]
- f(t) = (4A/T)*t - 4A pour t dans [3T/4, T]

Ce signal est pair et possede la symetrie de demi-onde, donc seuls les a_n impairs sont non nuls.

**Resultat :**
f(t) = (8A/pi^2) * [cos(w*t) - (1/9)*cos(3*w*t) + (1/25)*cos(5*w*t) - ...]

f(t) = (8A/pi^2) * somme de k=0 a l'infini de (-1)^k * cos((2k+1)*w*t) / (2k+1)^2

L'amplitude des harmoniques decroit en 1/n^2 (beaucoup plus rapidement que pour le signal carre). Un signal triangulaire est donc beaucoup mieux approche par ses premiers harmoniques qu'un signal carre.

#### Exemple 3 : Signal en dent de scie

Signal en dent de scie de periode T, croissant de -A a +A sur [0, T[ :
f(t) = A * (2t/T - 1) pour t dans [0, T[

Ce signal est impair, donc a_n = 0 pour tout n.

**Calcul de b_n :**
b_n = (-1)^(n+1) * 2A/(n*pi)

**Decomposition :**
f(t) = (2A/pi) * [sin(w*t) - (1/2)*sin(2*w*t) + (1/3)*sin(3*w*t) - (1/4)*sin(4*w*t) + ...]

Contrairement au signal carre, tous les harmoniques (pairs et impairs) sont presents car il n'y a pas de symetrie de demi-onde.

#### Theoreme de Parseval

Le theoreme de Parseval relie la puissance d'un signal a ses coefficients de Fourier :

(1/T) * integrale de 0 a T de |f(t)|^2 dt = (a_0/2)^2 + (1/2) * somme de n=1 a l'infini de (a_n^2 + b_n^2)

Ou en forme complexe :

(1/T) * integrale de 0 a T de |f(t)|^2 dt = somme de n=-infini a +infini de |C_n|^2

Ce theoreme est essentiel pour calculer la puissance transportee par chaque harmonique et pour determiner le taux de distorsion harmonique (THD).

#### Spectre d'un signal

Le **spectre d'amplitude** represente |C_n| (ou c_n) en fonction de la frequence n*f_0. C'est un spectre discret (de raies) car le signal est periodique. Le **spectre de phase** represente l'argument de C_n en fonction de la frequence.

### Module 2 : Transformee de Laplace

#### Definition

La transformee de Laplace d'une fonction causale f(t) (definie pour t >= 0) est :

F(s) = L{f(t)} = integrale de 0 a +infini de f(t) * e^(-s*t) dt

ou s = sigma + j*w est la variable complexe de Laplace.

La transformee de Laplace transforme une fonction du domaine temporel t en une fonction du domaine frequentiel complexe s. Elle transforme les operations de derivation et d'integration en operations algebriques (multiplication et division par s).

#### Transformees de Laplace usuelles

**Fonctions de base :**
- L{1} = 1/s (echelon unitaire u(t))
- L{t} = 1/s^2
- L{t^n} = n!/s^(n+1)
- L{e^(a*t)} = 1/(s - a) (converge pour Re(s) > a)
- L{t * e^(a*t)} = 1/(s - a)^2
- L{t^n * e^(a*t)} = n!/(s - a)^(n+1)

**Fonctions trigonometriques :**
- L{sin(w*t)} = w/(s^2 + w^2)
- L{cos(w*t)} = s/(s^2 + w^2)
- L{e^(a*t) * sin(w*t)} = w/((s - a)^2 + w^2)
- L{e^(a*t) * cos(w*t)} = (s - a)/((s - a)^2 + w^2)

**Fonction impulsion :**
- L{delta(t)} = 1 (la transformee de l'impulsion de Dirac est 1)

#### Proprietes fondamentales

**Linearite :**
L{a*f(t) + b*g(t)} = a*F(s) + b*G(s)

**Derivation temporelle (propriete essentielle) :**
L{f'(t)} = s*F(s) - f(0^-)
L{f''(t)} = s^2*F(s) - s*f(0^-) - f'(0^-)
L{f^(n)(t)} = s^n*F(s) - s^(n-1)*f(0^-) - ... - f^(n-1)(0^-)

Cette propriete est la raison principale de l'utilite de Laplace : la derivation (operation differentielles) est remplacee par une multiplication par s (operation algebrique).

**Integration temporelle :**
L{integrale de 0 a t de f(tau) dtau} = F(s)/s

**Decalage temporel (retard) :**
L{f(t - a) * u(t - a)} = e^(-a*s) * F(s)

**Decalage frequentiel (amortissement) :**
L{e^(a*t) * f(t)} = F(s - a)

**Theoreme de la valeur initiale :**
f(0^+) = lim quand s tend vers +infini de s*F(s)

**Theoreme de la valeur finale :**
f(+infini) = lim quand s tend vers 0 de s*F(s)
(valable si tous les poles de s*F(s) ont une partie reelle negative)

#### Transformee inverse de Laplace

La transformee inverse permet de repasser du domaine de Laplace au domaine temporel. La methode pratique repose sur la **decomposition en elements simples** de F(s), puis l'utilisation des tables.

**Methode generale :**
1. Ecrire F(s) sous forme de fraction rationnelle N(s)/D(s)
2. Si deg(N) >= deg(D), effectuer la division euclidienne
3. Decomposer en elements simples
4. Identifier chaque terme dans la table des transformees
5. Reconstituer f(t) par linearite

**Exemple 1** : Trouver la transformee inverse de F(s) = 5/(s*(s + 2))
- Decomposition : F(s) = A/s + B/(s + 2)
- A = [s*F(s)] en s = 0 = 5/2
- B = [(s + 2)*F(s)] en s = -2 = 5/(-2) = -5/2
- F(s) = (5/2)/s + (-5/2)/(s + 2)
- f(t) = (5/2) - (5/2)*e^(-2t) = (5/2)*(1 - e^(-2t)) pour t >= 0

**Exemple 2** : Trouver la transformee inverse de F(s) = (2s + 3)/(s^2 + 4s + 13)
- On complete le carre : s^2 + 4s + 13 = (s + 2)^2 + 9 = (s + 2)^2 + 3^2
- On reecrit : F(s) = (2(s + 2) - 1)/((s + 2)^2 + 3^2) = 2*(s + 2)/((s + 2)^2 + 9) - (1/3)*3/((s + 2)^2 + 9)
- Par la table avec decalage frequentiel :
  - 2*(s + 2)/((s + 2)^2 + 9) --> 2*e^(-2t)*cos(3t)
  - (1/3)*3/((s + 2)^2 + 9) --> (1/3)*e^(-2t)*sin(3t)
- f(t) = e^(-2t) * [2*cos(3t) - (1/3)*sin(3t)] pour t >= 0

**Exemple 3** : Trouver la transformee inverse de F(s) = (s + 1)/((s + 2)*(s^2 + 1))
- Decomposition : F(s) = A/(s + 2) + (Bs + C)/(s^2 + 1)
- A = [(s + 2)*F(s)] en s = -2 = (-2 + 1)/(4 + 1) = -1/5
- Identification : (s + 1) = A*(s^2 + 1) + (Bs + C)*(s + 2)
- En developpant et identifiant les coefficients :
  - s^2 : A + B = 0 --> B = 1/5
  - s^0 : A + 2C = 1 --> C = (1 + 1/5)/2 = 3/5
  - s^1 : 2B + C = 1 --> verification : 2/5 + 3/5 = 1 (OK)
- F(s) = (-1/5)/(s + 2) + (s/5 + 3/5)/(s^2 + 1)
- f(t) = (-1/5)*e^(-2t) + (1/5)*cos(t) + (3/5)*sin(t) pour t >= 0

#### Application : Resolution d'equations differentielles par Laplace

La transformee de Laplace permet de resoudre des equations differentielles lineaires a coefficients constants avec conditions initiales de maniere systematique.

**Methode :**
1. Appliquer la transformee de Laplace a chaque terme de l'equation
2. Utiliser les proprietes de derivation pour incorporer les conditions initiales
3. Resoudre l'equation algebrique en F(s)
4. Calculer la transformee inverse pour obtenir f(t)

**Exemple** : Resoudre y'' + 3y' + 2y = 5 avec y(0) = 0 et y'(0) = 0

1. Transformee de Laplace :
   - L{y''} = s^2*Y(s) - s*y(0) - y'(0) = s^2*Y(s)
   - L{y'} = s*Y(s) - y(0) = s*Y(s)
   - L{y} = Y(s)
   - L{5} = 5/s

2. Equation algebrique : s^2*Y(s) + 3s*Y(s) + 2Y(s) = 5/s
   (s^2 + 3s + 2)*Y(s) = 5/s

3. Resolution : Y(s) = 5/(s*(s^2 + 3s + 2)) = 5/(s*(s + 1)*(s + 2))

4. Decomposition en elements simples :
   Y(s) = A/s + B/(s + 1) + C/(s + 2)
   - A = 5/((0 + 1)(0 + 2)) = 5/2
   - B = 5/((-1)(-1 + 2)) = 5/(-1) = -5
   - C = 5/((-2)(-2 + 1)) = 5/(2) = 5/2

5. Transformee inverse :
   y(t) = 5/2 - 5*e^(-t) + (5/2)*e^(-2t) pour t >= 0

6. Verification : y(0) = 5/2 - 5 + 5/2 = 0 (OK), y(+infini) = 5/2 (valeur finale)

#### Application : Analyse de circuits par Laplace

La transformee de Laplace est l'outil standard pour analyser les circuits en regime transitoire. On remplace les composants par leur impedance de Laplace :
- Resistance : Z_R(s) = R
- Condensateur : Z_C(s) = 1/(C*s)
- Bobine : Z_L(s) = L*s

**Exemple : Circuit RC serie soumis a un echelon de tension E**

L'equation de maille donne : R*i(t) + (1/C)*integrale de 0 a t de i(tau) dtau = E

En Laplace (conditions initiales nulles) :
R*I(s) + (1/(C*s))*I(s) = E/s
I(s) * (R + 1/(C*s)) = E/s
I(s) = E/(R*s + 1/C) = (E/R)/(s + 1/(RC))

Transformee inverse :
i(t) = (E/R) * e^(-t/(RC)) pour t >= 0

La tension aux bornes du condensateur :
U_C(s) = I(s)/(C*s) = E/(s*(RCs + 1)) = (E/s) - E/(s + 1/(RC))
u_c(t) = E * (1 - e^(-t/(RC))) pour t >= 0

On retrouve le resultat classique du circuit RC avec la constante de temps tau = RC.

**Fonction de transfert :**
Pour un circuit RC passe-bas, la fonction de transfert est :
H(s) = U_C(s)/U_e(s) = 1/(1 + RC*s) = 1/(1 + tau*s)

C'est un filtre passe-bas du 1er ordre avec une frequence de coupure f_c = 1/(2*pi*RC).

#### Liens entre Fourier et Laplace

La transformee de Fourier est un cas particulier de la transformee de Laplace ou s = j*w (on se place sur l'axe imaginaire). Ainsi, pour un systeme stable (tous les poles a partie reelle negative), la reponse frequentielle H(j*w) est obtenue en remplacant s par j*w dans la fonction de transfert H(s).

Cette correspondance permet de passer de l'analyse temporelle (Laplace, reponse a un echelon) a l'analyse frequentielle (Fourier, diagramme de Bode) d'un meme systeme.

### Travaux diriges et exercices

**Exercices de Fourier :**
- Calcul des coefficients de Fourier pour differents signaux periodiques
- Reconstruction de signaux a partir de leurs harmoniques
- Spectre d'amplitude et de phase
- Application du theoreme de Parseval
- Calcul de puissance par harmonique

**Exercices de Laplace :**
- Calcul de transformees directes a partir de la definition
- Utilisation des proprietes (linearite, derivation, decalage)
- Transformees inverses par decomposition en elements simples
- Resolution d'equations differentielles du 1er et 2eme ordre
- Analyse de circuits RC, RL et RLC en regime transitoire
- Calcul de fonctions de transfert

**Exercices de synthese :**
- Resolution analytique d'equations differentielles lineaires a coefficients constants (ED1 et ED2)
- Comparaison des methodes classique et par Laplace
- Verification des conditions initiales et de la valeur finale

---

## PART D : ANALYSE ET REFLEXION

### Competences acquises

- **Decomposition de Fourier** : Capacite a decomposer n'importe quel signal periodique en ses harmoniques, a interpreter un spectre et a utiliser les proprietes de symetrie pour simplifier les calculs.
- **Transformee de Laplace** : Maitrise du passage entre domaine temporel et domaine de Laplace, calcul de transformees directes et inverses, utilisation des proprietes fondamentales.
- **Resolution algebrique d'EDO** : Capacite a resoudre des equations differentielles lineaires a coefficients constants par la methode de Laplace, en incorporant les conditions initiales de maniere naturelle.
- **Analyse de circuits** : Utilisation des impedances de Laplace pour analyser des circuits en regime transitoire et determiner des fonctions de transfert.
- **Vision frequentielle** : Comprehension du lien entre representation temporelle et representation frequentielle d'un signal ou d'un systeme.

### Auto-evaluation

Le cours d'Outils Logiciels du S2 est l'un des cours les plus importants du cursus GEII car il fournit le langage et les outils mathematiques utilises dans presque tous les cours techniques ulterieurs. Les series de Fourier sont la base de l'analyse spectrale et du traitement du signal, tandis que la transformee de Laplace est l'outil fondamental de l'automatique et de l'analyse des systemes.

La difficulte principale a ete de donner un sens physique aux formules mathematiques : comprendre qu'un signal carre est compose d'une infinite de sinusoides, ou qu'une multiplication par s en Laplace correspond a une derivation temporelle. Une fois cette intuition acquise, les outils deviennent naturels.

Le lien entre les deux transformees (Fourier comme cas particulier de Laplace sur l'axe imaginaire) est une revelation qui unifie l'analyse temporelle et frequentielle.

### Connexions interdisciplinaires

- **Mathematiques (S2)** : Les outils mathematiques (integrales, fractions rationnelles, EDO) sont directement utilises. Les exercices d'OL constituent une mise en pratique concrete des mathematiques.
- **Systemes Electroniques** : Les fonctions de transfert H(s) et les diagrammes de Bode sont la traduction directe de la theorie de Laplace appliquee aux circuits.
- **Travaux de Laboratoire** : Les mesures de reponse frequentielle et de regime transitoire des filtres sont interpretees grace a Fourier et Laplace.
- **Cours futurs** : L'automatique (S3-S4), la regulation, le traitement du signal numerique, les telecommunications -- tous ces domaines reposent sur les fondements poses dans ce cours.

### Progression et perspectives

Ce cours marque le passage d'une vision purement temporelle des signaux et circuits a une vision frequentielle et algebrique. C'est un changement de paradigme fondamental en electronique : au lieu de resoudre des equations differentielles dans le domaine temporel, on manipule des fractions rationnelles dans le domaine de Laplace. Cette approche est non seulement plus simple mathematiquement, mais elle donne aussi une meilleure intuition physique du comportement des systemes.

---

## Documents de Cours

<div class="pdf-container">
  <div class="pdf-viewer">

    <div class="pdf-item">
      <h4>Polycopie de Cours - Series de Fourier</h4>
      <p>Document de reference du cours sur les series de Fourier : decomposition trigonometrique, coefficients, proprietes de symetrie, theoreme de Parseval et spectres.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S2/OL/poly1_S2_OL.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/OL/poly1_S2_OL.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Cours - Series de Fourier</h4>
      <p>Support de cours complementaire sur les series de Fourier avec exemples detailles et applications.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S2/OL/Fourier.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/OL/Fourier.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Annale - Series de Fourier</h4>
      <p>Sujet d'examen sur les series de Fourier : exercices de calcul de coefficients, spectres et applications.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S2/OL/Annale_Série_de_fourrier.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/OL/Annale_Série_de_fourrier.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Cours - Transformee de Laplace : Signaux</h4>
      <p>Support de cours sur la transformee de Laplace appliquee aux signaux : definition, transformees usuelles et exemples de calcul.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S2/OL/Cours_transformation_Laplace_signauxv2.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/OL/Cours_transformation_Laplace_signauxv2.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Cours - Proprietes de la Transformee de Laplace</h4>
      <p>Document detaillant les proprietes fondamentales de la transformee de Laplace : linearite, derivation, integration, decalages temporel et frequentiel, theoremes de la valeur initiale et finale.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S2/OL/transformation_Laplace_propriétés.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/OL/transformation_Laplace_propriétés.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Cours - Transformee de Laplace Inverse</h4>
      <p>Support sur la methode de la transformee inverse de Laplace par decomposition en elements simples : poles simples, multiples et complexes conjugues.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S2/OL/Transformation_de_Laplace_inverse.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/OL/Transformation_de_Laplace_inverse.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>TP1 - Transformee de Laplace et Signaux</h4>
      <p>Travail pratique sur la transformee de Laplace appliquee a l'analyse de signaux : calculs directs et inverses avec verification.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S2/OL/02_Laplace_signaux_TP1_S2_V-2021.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/OL/02_Laplace_signaux_TP1_S2_V-2021.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>TD1 - Correction Laplace</h4>
      <p>Corrige detaille du premier TD de Laplace : decompositions en elements simples, transformees inverses et resolution d'equations differentielles.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S2/OL/TD1_correction.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/OL/TD1_correction.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>ED1 - Resolution Analytique d'Equations Differentielles</h4>
      <p>Premier fascicule de resolution analytique d'equations differentielles lineaires a coefficients constants par la methode classique et par Laplace.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S2/OL/Résolution_des_équations_différentielles_linéaires_à_coefficients_constantsV2.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/OL/Résolution_des_équations_différentielles_linéaires_à_coefficients_constantsV2.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

  </div>
</div>

---

<style>body{font-family:Arial,sans-serif;background-color:#f4f4f9;color:#333;line-height:1.6}h2,h3,h4,h5{color:#2a7ae2}p{text-align:justify}code{background-color:#f5f5f5;padding:2px 6px;border-radius:3px;font-family:'Courier New',monospace}pre{background-color:#f5f5f5;padding:15px;border-radius:5px;overflow-x:auto}</style>

<div class="back-nav">
  <a href="./my-courses-2020-2021.html">&larr; Retour a Mes Cours 2020-2021</a>
</div>

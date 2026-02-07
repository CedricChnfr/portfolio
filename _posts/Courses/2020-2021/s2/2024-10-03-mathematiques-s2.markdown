---
layout: default
title: "Mathematiques - S2"
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
  <a href="./my-courses-2020-2021.html">&larr; Retour a Mes Cours 2020-2021</a>
</div>

# Mathematiques - S2

**Annee**: 2020-2021 | **Semestre**: 2 | **Type**: Scientifique

---

## PART A : PRESENTATION GENERALE

### Contexte et objectifs

Le cours de mathematiques du semestre 2 constitue un approfondissement majeur des outils mathematiques pour l'ingenieur. Il prolonge les bases acquises au S1 (derivees, limites, nombres complexes) en introduisant des concepts avances indispensables pour l'analyse de systemes electroniques, le traitement du signal et la modelisation de phenomenes physiques en GEII.

Ce semestre couvre cinq grands domaines : les polynomes, les fractions rationnelles, le calcul integral, les equations differentielles du premier ordre et les equations differentielles du second ordre. Chacun de ces domaines trouve des applications directes dans les cours techniques du cursus.

**Objectifs pedagogiques :**
- Maitriser les polynomes et les fractions rationnelles pour l'analyse de fonctions de transfert
- Approfondir le calcul integral et ses applications au calcul de valeurs moyennes et efficaces
- Resoudre des equations differentielles du 1er et du 2eme ordre avec conditions initiales
- Appliquer les mathematiques aux systemes reels (circuits RC, RL, RLC)
- Utiliser les outils de decomposition en elements simples pour les transformees inverses
- Interpreter graphiquement et physiquement les solutions mathematiques

### Organisation

Le cours est structure autour de cinq modules complementaires. Chaque module comprend des cours magistraux (CM) ou l'enseignant presente la theorie, des travaux diriges (TD) pour la mise en pratique, et des fascicules d'exercices corriges. Les evaluations comprennent des controles continus et un examen final de synthese.

Le volume horaire est reparti approximativement comme suit :
- Cours magistraux : environ 20 heures
- Travaux diriges : environ 20 heures
- Travail personnel et revisions : variable selon l'etudiant

### Prerequis

- Calcul de derivees et primitives de base (S1)
- Nombres complexes et formes algebrique, trigonometrique, exponentielle
- Notions de limites et continuite
- Resolution d'equations du premier et second degre

---

## PART B : EXPERIENCE ET CONTEXTE

### Environnement pedagogique

Le semestre 2 de mathematiques s'inscrit dans la continuite du S1 en consolidant les bases et en introduisant des outils plus avances necessaires pour les cours techniques. L'annee 2020-2021 a ete marquee par un enseignement partiellement a distance en raison du contexte sanitaire (COVID-19), ce qui a necessite une adaptation importante : cours en visioconference, exercices en ligne, et evaluations a distance.

Malgre ces contraintes, la qualite de l'enseignement a ete maintenue grace a des polycopies detailles, des seances de questions-reponses en ligne et des fascicules d'exercices complets avec corriges.

### Ressources et supports

- **Cours magistraux** : Polycopies detailles pour chaque module (polynomes, integrales, EDO 1er et 2nd ordre)
- **Fascicules d'exercices** : Recueils pour chaque chapitre avec solutions detaillees
- **Annales de partiels** : Sujets des annees precedentes pour la preparation aux examens
- **Rappels de calcul** : Fiches de rappel sur les fractions, fonctions de base et derivees
- **Cours sur les fractions rationnelles** : Document specifique sur la decomposition en elements simples

### Liens avec d'autres cours

- **Outils Logiciels (OL)** : Application directe des mathematiques. Les series de Fourier et la transformee de Laplace utilisent les integrales et les fractions rationnelles. La decomposition en elements simples est essentielle pour le calcul de transformees inverses de Laplace.
- **Systemes Electroniques (SE)** : L'analyse frequentielle repose sur les polynomes (numerateur et denominateur des fonctions de transfert). Les filtres sont decrits par des equations differentielles.
- **Energie** : La modelisation de systemes electriques (circuits, machines) utilise les equations differentielles. Le calcul integral permet de determiner les valeurs moyennes et efficaces en triphase.
- **Informatique Embarquee (IE)** : Les algorithmes numeriques de resolution d'equations differentielles (methode d'Euler) s'appuient sur la comprehension mathematique.
- **Travaux de Laboratoire (TL)** : L'analyse des resultats experimentaux necessite la maitrise des outils mathematiques pour comparer theorie et mesures.

### Difficultes et apprentissages

Le passage aux equations differentielles du second ordre a represente un saut de difficulte important. La distinction entre les trois regimes (aperiodique, critique, pseudo-periodique) et la determination des constantes d'integration a partir des conditions initiales necessitent une bonne maitrise de l'ensemble des outils precedents. Le contexte d'enseignement a distance a rendu l'apprentissage plus autonome et a developpe la capacite a chercher et comprendre par soi-meme.

---

## PART C : ASPECTS TECHNIQUES

### Module 1 : Polynomes

#### Definitions et proprietes fondamentales

Un polynome P(x) de degre n est une expression de la forme :

P(x) = a_n * x^n + a_(n-1) * x^(n-1) + ... + a_1 * x + a_0

ou les a_i sont des coefficients reels (ou complexes) et a_n est non nul (coefficient dominant).

**Operations sur les polynomes :**
- **Addition** : On additionne les coefficients de meme degre. Si P(x) = 3x^2 + 2x + 1 et Q(x) = x^2 - x + 4, alors P(x) + Q(x) = 4x^2 + x + 5.
- **Multiplication** : On multiplie chaque terme par chaque terme et on regroupe. Le degre du produit est la somme des degres.
- **Division euclidienne** : Pour P et D avec deg(P) >= deg(D), il existe un quotient Q et un reste R uniques tels que P = D * Q + R avec deg(R) < deg(D).

**Exemple de division euclidienne :**
Diviser P(x) = 2x^3 + 3x^2 - x + 5 par D(x) = x - 1 :
- 2x^3 / x = 2x^2, puis on soustrait 2x^2 * (x - 1) = 2x^3 - 2x^2
- Reste intermediaire : 5x^2 - x + 5
- 5x^2 / x = 5x, puis on soustrait 5x * (x - 1) = 5x^2 - 5x
- Reste intermediaire : 4x + 5
- 4x / x = 4, puis on soustrait 4 * (x - 1) = 4x - 4
- Reste final : 9
- Resultat : P(x) = (x - 1)(2x^2 + 5x + 4) + 9

#### Racines et factorisation

**Theoreme fondamental de l'algebre** : Tout polynome de degre n >= 1 a coefficients complexes possede exactement n racines dans C (comptees avec multiplicite).

**Theoreme de factorisation** : Si r_1, r_2, ..., r_n sont les racines de P(x), alors :
P(x) = a_n * (x - r_1)(x - r_2)...(x - r_n)

**Propriete des racines complexes conjuguees** : Si P(x) a des coefficients reels et si z = a + jb est une racine, alors son conjugue z* = a - jb est aussi une racine. Ces deux racines produisent un facteur quadratique irreductible :
(x - z)(x - z*) = x^2 - 2ax + (a^2 + b^2)

**Exemple** : P(x) = x^3 - 6x^2 + 11x - 6
- On teste x = 1 : P(1) = 1 - 6 + 11 - 6 = 0, donc x = 1 est racine
- Division par (x - 1) : P(x) = (x - 1)(x^2 - 5x + 6) = (x - 1)(x - 2)(x - 3)
- Les racines sont x = 1, x = 2, x = 3

#### Applications en GEII

En electronique, les polynomes interviennent dans les fonctions de transfert. Une fonction de transfert H(s) est le rapport de deux polynomes en s :

H(s) = N(s) / D(s) = (b_m * s^m + ... + b_0) / (a_n * s^n + ... + a_0)

Les racines du numerateur N(s) sont les **zeros** de H(s) et les racines du denominateur D(s) sont les **poles**. La stabilite d'un systeme est determinee par la position des poles dans le plan complexe : un systeme est stable si et seulement si tous les poles ont une partie reelle strictement negative.

**Exemple** : Pour un filtre passe-bas du 2eme ordre avec H(s) = w0^2 / (s^2 + 2*z*w0*s + w0^2), les poles sont :
s = -z*w0 +/- w0*sqrt(z^2 - 1)
Si z > 0, les poles ont une partie reelle negative et le systeme est stable.

### Module 2 : Fractions rationnelles

#### Decomposition en elements simples

Une fraction rationnelle F(x) = P(x)/Q(x) avec deg(P) < deg(Q) peut etre decomposee en somme d'elements simples.

**Cas de poles simples reels** : Si Q(x) = (x - a_1)(x - a_2)...(x - a_n) avec tous les a_i distincts, alors :
F(x) = A_1/(x - a_1) + A_2/(x - a_2) + ... + A_n/(x - a_n)

Pour trouver A_i, on multiplie par (x - a_i) et on evalue en x = a_i :
A_i = [(x - a_i) * F(x)] evalue en x = a_i

**Exemple** : Decomposer F(x) = (3x + 1) / ((x - 1)(x + 2))

F(x) = A/(x - 1) + B/(x + 2)
- A = [(x - 1) * F(x)] en x = 1 = (3 + 1) / (1 + 2) = 4/3
- B = [(x + 2) * F(x)] en x = -2 = (-6 + 1) / (-2 - 1) = -5/(-3) = 5/3
- F(x) = (4/3)/(x - 1) + (5/3)/(x + 2)

**Cas de poles multiples** : Si Q(x) contient un facteur (x - a)^k, la decomposition contient :
A_1/(x - a) + A_2/(x - a)^2 + ... + A_k/(x - a)^k

**Exemple** : F(x) = (2x + 3) / (x - 1)^2
F(x) = A/(x - 1) + B/(x - 1)^2
- B = [(x - 1)^2 * F(x)] en x = 1 = 2 + 3 = 5
- Pour A, on multiplie par (x - 1)^2 et on derive : d/dx[(2x + 3)] = 2, donc A = 2
- F(x) = 2/(x - 1) + 5/(x - 1)^2

**Cas de poles complexes conjugues** : Si Q(x) contient un facteur irreductible (x^2 + bx + c), la decomposition contient :
(Ax + B) / (x^2 + bx + c)

**Exemple** : F(x) = 1 / (x(x^2 + 1))
F(x) = A/x + (Bx + C)/(x^2 + 1)
- A = [x * F(x)] en x = 0 = 1/1 = 1
- En multipliant par x(x^2 + 1) : 1 = A(x^2 + 1) + (Bx + C)x
- 1 = (A + B)x^2 + Cx + A
- A + B = 0 donc B = -1, C = 0, A = 1
- F(x) = 1/x + (-x)/(x^2 + 1)

#### Applications aux transformees inverses de Laplace

La decomposition en elements simples est la methode principale pour calculer les transformees inverses de Laplace. On decompose F(s), puis on utilise les tables :

- A/(s - a) --> A * e^(at)
- A/(s - a)^2 --> A * t * e^(at)
- (As + B)/(s^2 + w^2) --> A*cos(wt) + (B/w)*sin(wt)

### Module 3 : Calcul integral

#### Primitives et integrales definies

**Definition** : Une primitive de f(x) est une fonction F(x) telle que F'(x) = f(x). L'integrale definie est :
integrale de a a b de f(x)dx = F(b) - F(a)

**Primitives de reference :**
- integrale de x^n dx = x^(n+1)/(n+1) + C (n different de -1)
- integrale de 1/x dx = ln|x| + C
- integrale de e^(ax) dx = (1/a) * e^(ax) + C
- integrale de cos(ax) dx = (1/a) * sin(ax) + C
- integrale de sin(ax) dx = -(1/a) * cos(ax) + C
- integrale de 1/(1 + x^2) dx = arctan(x) + C
- integrale de 1/sqrt(1 - x^2) dx = arcsin(x) + C

#### Integration par parties

**Formule** : integrale de u*dv = u*v - integrale de v*du

Le choix de u et dv est crucial. La regle mnemonique LIATE (Logarithme, Inverse trigonometrique, Algebrique, Trigonometrique, Exponentielle) aide a choisir u.

**Exemple 1** : Calculer integrale de x * e^x dx
- u = x, dv = e^x dx
- du = dx, v = e^x
- integrale de x * e^x dx = x * e^x - integrale de e^x dx = x * e^x - e^x + C = e^x(x - 1) + C

**Exemple 2** : Calculer integrale de x^2 * cos(x) dx
- u = x^2, dv = cos(x) dx --> du = 2x dx, v = sin(x)
- integrale = x^2 * sin(x) - 2 * integrale de x * sin(x) dx
- Pour le deuxieme terme : u = x, dv = sin(x) dx --> du = dx, v = -cos(x)
- integrale de x * sin(x) dx = -x * cos(x) + integrale de cos(x) dx = -x * cos(x) + sin(x) + C
- Resultat final : x^2 * sin(x) + 2x * cos(x) - 2 * sin(x) + C

**Exemple 3** : Calculer integrale de ln(x) dx
- u = ln(x), dv = dx
- du = dx/x, v = x
- integrale = x * ln(x) - integrale de dx = x * ln(x) - x + C

#### Changement de variable

**Principe** : On pose x = g(t), alors dx = g'(t)dt et on transforme l'integrale.

**Exemple** : Calculer integrale de 1/sqrt(1 - x^2) dx
- Substitution trigonometrique : x = sin(t), dx = cos(t) dt
- integrale de cos(t)/sqrt(1 - sin^2(t)) dt = integrale de cos(t)/cos(t) dt = integrale de dt = t + C
- Resultat : arcsin(x) + C

**Exemple** : Calculer integrale de 2x * e^(x^2) dx
- Substitution : u = x^2, du = 2x dx
- integrale de e^u du = e^u + C = e^(x^2) + C

#### Integration de fonctions rationnelles

Pour integrer P(x)/Q(x), on effectue d'abord la division euclidienne si deg(P) >= deg(Q), puis on decompose en elements simples :

**Exemple** : integrale de (3x + 1)/((x - 1)(x + 2)) dx
- Decomposition : (4/3)/(x - 1) + (5/3)/(x + 2) (calculee precedemment)
- integrale = (4/3)*ln|x - 1| + (5/3)*ln|x + 2| + C

**Exemple** : integrale de 1/(x^2 + 1) dx = arctan(x) + C

**Exemple** : integrale de (2x + 3)/(x^2 + 4) dx
- Separation : integrale de 2x/(x^2 + 4) dx + integrale de 3/(x^2 + 4) dx
- Premier terme : ln(x^2 + 4) (par reconnaissance de u'/u)
- Second terme : (3/2) * arctan(x/2) (par table)
- Resultat : ln(x^2 + 4) + (3/2)*arctan(x/2) + C

#### Applications en GEII

**Calcul de la valeur moyenne d'un signal** :
V_moy = (1/T) * integrale de 0 a T de v(t) dt

**Calcul de la valeur efficace (RMS)** :
V_eff = sqrt((1/T) * integrale de 0 a T de v(t)^2 dt)

**Exemple** : Pour un signal sinusoidal v(t) = V_max * sin(wt) :
- V_moy sur une periode complete = 0
- V_eff = V_max / sqrt(2)

**Calcul d'energie** :
W = integrale de 0 a T de p(t) dt = integrale de 0 a T de v(t) * i(t) dt

### Module 4 : Equations differentielles du 1er ordre

#### Forme generale et methodes de resolution

**Forme generale lineaire** : y' + a(x) * y = b(x)

**Equation homogene associee** : y' + a(x) * y = 0
- Solution : y_h = C * e^(-integrale de a(x)dx)

**Cas a coefficients constants** : y' + a*y = b(x)
- Solution homogene : y_h = C * e^(-ax)
- La constante de temps est tau = 1/a

**Methode de variation de la constante** :
1. Resoudre l'equation homogene : y_h = C * e^(-ax)
2. Poser y_p = C(x) * e^(-ax)
3. Substituer dans l'equation complete pour trouver C(x)
4. Solution generale : y = y_h + y_p

**Exemple detaille** : Resoudre y' + 2y = 6

1. Equation homogene : y' + 2y = 0 --> y_h = C * e^(-2x)
2. Solution particuliere : on cherche y_p constante (car second membre constant)
   - y_p' + 2*y_p = 6 --> 0 + 2*y_p = 6 --> y_p = 3
3. Solution generale : y(x) = C * e^(-2x) + 3
4. Avec condition initiale y(0) = 0 : 0 = C + 3 --> C = -3
5. Solution : y(x) = 3(1 - e^(-2x))

**Exemple avec second membre exponentiel** : Resoudre y' + 3y = e^(-x)

1. Solution homogene : y_h = C * e^(-3x)
2. Solution particuliere : on essaie y_p = A * e^(-x)
   - y_p' = -A * e^(-x)
   - -A * e^(-x) + 3A * e^(-x) = e^(-x) --> 2A = 1 --> A = 1/2
3. Solution generale : y(x) = C * e^(-3x) + (1/2) * e^(-x)

#### Application aux circuits RC et RL

**Circuit RC en charge** : La tension aux bornes du condensateur u_c(t) verifie :
RC * u_c' + u_c = E (avec E la tension d'alimentation)

C'est une EDO du 1er ordre avec tau = RC.
- Solution : u_c(t) = E * (1 - e^(-t/tau))
- Le condensateur atteint 63% de E apres un temps tau
- On considere la charge complete apres 5*tau (99.3% de E)

**Circuit RL** : Le courant i(t) dans une bobine verifie :
L * i' + R * i = E

Avec tau = L/R :
- Solution : i(t) = (E/R) * (1 - e^(-t/tau))

**Decharge d'un condensateur** (circuit RC sans source) :
RC * u_c' + u_c = 0
- Solution : u_c(t) = U_0 * e^(-t/tau) ou U_0 est la tension initiale

### Module 5 : Equations differentielles du 2eme ordre

#### Forme generale et equation caracteristique

**Forme generale normalisee** : y'' + 2*z*w0*y' + w0^2*y = f(t)

ou z (zeta) est le coefficient d'amortissement et w0 est la pulsation propre non amortie.

**Equation caracteristique** : r^2 + 2*z*w0*r + w0^2 = 0

Le discriminant est : Delta = 4*w0^2*(z^2 - 1)

#### Les trois regimes

**Regime aperiodique (z > 1)** : Delta > 0, deux racines reelles negatives distinctes
- r_1 = -z*w0 + w0*sqrt(z^2 - 1)
- r_2 = -z*w0 - w0*sqrt(z^2 - 1)
- Solution homogene : y_h(t) = A*e^(r_1*t) + B*e^(r_2*t)
- Le systeme revient lentement a l'equilibre sans oscillation
- Plus z est grand, plus le retour est lent

**Regime critique (z = 1)** : Delta = 0, racine double r = -w0
- Solution homogene : y_h(t) = (A + B*t)*e^(-w0*t)
- C'est le regime le plus rapide sans depassement
- Optimal pour les systemes d'asservissement

**Regime pseudo-periodique (0 < z < 1)** : Delta < 0, racines complexes conjuguees
- r = -z*w0 +/- j*w0*sqrt(1 - z^2)
- La pseudo-pulsation est : w_p = w0*sqrt(1 - z^2)
- Solution homogene : y_h(t) = e^(-z*w0*t) * [A*cos(w_p*t) + B*sin(w_p*t)]
- Le systeme oscille avec une amplitude decroissante
- La pseudo-periode est T_p = 2*pi/w_p
- Le premier depassement est : D1 = e^(-pi*z/sqrt(1 - z^2))

**Exemple detaille** : Resoudre y'' + 4y' + 3y = 6

1. Equation caracteristique : r^2 + 4r + 3 = 0
   - Delta = 16 - 12 = 4 > 0
   - r_1 = (-4 + 2)/2 = -1, r_2 = (-4 - 2)/2 = -3
2. Solution homogene : y_h(t) = A*e^(-t) + B*e^(-3t)
3. Solution particuliere (second membre constant) : y_p = 6/3 = 2
4. Solution generale : y(t) = A*e^(-t) + B*e^(-3t) + 2
5. Conditions initiales y(0) = 0, y'(0) = 0 :
   - A + B + 2 = 0
   - -A - 3B = 0 --> A = -3B
   - -3B + B + 2 = 0 --> B = 1, A = -3
6. Solution : y(t) = -3*e^(-t) + e^(-3t) + 2

**Exemple en regime pseudo-periodique** : Resoudre y'' + 2y' + 5y = 10

1. Equation caracteristique : r^2 + 2r + 5 = 0
   - Delta = 4 - 20 = -16 < 0
   - r = (-2 +/- j*4)/2 = -1 +/- j*2
2. z*w0 = 1, w0^2 = 5 --> w0 = sqrt(5), z = 1/sqrt(5) = 0.447
3. w_p = 2 (pseudo-pulsation)
4. Solution homogene : y_h(t) = e^(-t) * [A*cos(2t) + B*sin(2t)]
5. Solution particuliere : y_p = 10/5 = 2
6. Solution generale : y(t) = e^(-t) * [A*cos(2t) + B*sin(2t)] + 2
7. Conditions initiales y(0) = 0, y'(0) = 0 :
   - A + 2 = 0 --> A = -2
   - -A + 2B = 0 --> B = A/2 = -1
8. Solution : y(t) = 2 - e^(-t) * [2*cos(2t) + sin(2t)]

#### Application aux circuits RLC

**Circuit RLC serie** : La tension aux bornes du condensateur u_c(t) verifie :
LC * u_c'' + RC * u_c' + u_c = E

En forme normalisee : u_c'' + (R/L)*u_c' + (1/LC)*u_c = E/LC

On identifie :
- w0 = 1/sqrt(LC) (pulsation propre)
- z = R/(2*sqrt(L/C)) = R/(2*L*w0) (coefficient d'amortissement)
- Le facteur de qualite est Q = 1/(2*z) = (1/R)*sqrt(L/C)

**Comportement selon z** :
- z > 1 (R eleve) : regime aperiodique, le circuit se decharge lentement
- z = 1 (R = 2*sqrt(L/C)) : regime critique, retour le plus rapide sans oscillation
- z < 1 (R faible) : regime pseudo-periodique, oscillations amorties

**Exemple numerique** : Circuit RLC avec R = 100 ohms, L = 10 mH, C = 1 uF
- w0 = 1/sqrt(10e-3 * 1e-6) = 10000 rad/s (f0 = 1591 Hz)
- z = 100/(2 * sqrt(10e-3/1e-6)) = 100/(2 * 100) = 0.5
- Regime pseudo-periodique (z < 1)
- w_p = 10000 * sqrt(1 - 0.25) = 8660 rad/s
- T_p = 2*pi/8660 = 0.726 ms

### Travaux diriges et exercices

**Exercices sur les polynomes et fractions rationnelles :**
- Factorisation de polynomes de degre 3 et 4
- Decomposition en elements simples de fractions rationnelles
- Application a l'integration de fonctions rationnelles

**Exercices sur le calcul integral :**
- Calcul d'integrales par differentes methodes (par parties, changement de variable)
- Integrales de fonctions trigonometriques
- Applications au calcul de valeurs moyennes et efficaces

**Exercices sur les EDO :**
- Resolution d'equations differentielles du 1er et 2nd ordre
- Determination des constantes avec conditions initiales
- Modelisation de circuits RC, RL et RLC
- Identification du regime a partir des parametres du circuit

**Annales et preparation aux examens :**
- Sujets de partiels des annees precedentes
- Exercices de synthese melant plusieurs modules
- Problemes ouverts de modelisation

---

## PART D : ANALYSE ET REFLEXION

### Competences acquises

- **Maitrise des outils mathematiques fondamentaux** : Polynomes, fractions rationnelles, integrales et equations differentielles constituent la boite a outils essentielle de l'ingenieur en electronique.
- **Capacite a resoudre des equations differentielles lineaires** : Aussi bien du 1er que du 2nd ordre, avec conditions initiales, ce qui est directement applicable aux circuits electriques.
- **Passage entre domaine temporel et frequentiel** : La comprehension des polynomes et fractions rationnelles prepare au passage de Laplace et a l'analyse frequentielle.
- **Modelisation de phenomenes physiques** : Traduction d'un probleme physique en equation mathematique, resolution, puis interpretation du resultat.
- **Interpretation graphique et physique** : Associer une solution mathematique a un comportement physique (constante de temps, oscillations, amortissement).

### Auto-evaluation

Les mathematiques du S2 ont constitue un approfondissement majeur et un pilier pour toute la suite du cursus GEII. Les equations differentielles du second ordre, en particulier, sont omniprésentes : tout circuit RLC, tout systeme mecanique masse-ressort-amortisseur, tout filtre du second ordre est decrit par une telle equation.

La comprehension intuitive des trois regimes (aperiodique, critique, pseudo-periodique) et de leur signification physique est l'un des acquis les plus importants. Le lien entre le coefficient d'amortissement z et le comportement du systeme est une notion qui revient dans presque tous les cours techniques.

Le calcul integral, bien que plus classique, s'est revele indispensable pour le calcul de valeurs efficaces en energie (signaux triphases, redresses) et pour les coefficients de Fourier en Outils Logiciels.

Le contexte d'enseignement a distance a renforce l'autonomie et la capacite a apprendre par soi-meme, competences precieuses pour la suite des etudes.

### Connexions interdisciplinaires

- **Vers les Outils Logiciels (S2)** : Les polynomes et fractions rationnelles sont directement utilises pour les transformees de Laplace inverses. Le calcul integral est la base des coefficients de Fourier.
- **Vers les Systemes Electroniques** : Les fonctions de transfert sont des fractions rationnelles dont les poles et zeros determinent le comportement frequentiel des filtres.
- **Vers l'Energie** : Les equations differentielles modelisent les machines electriques. Les integrales calculent puissances et energies.
- **Vers les semestres suivants (S3-S4)** : Les automatismes, la regulation, le traitement du signal reposent tous sur ces fondamentaux mathematiques. La transformee de Laplace, etudiee en OL, utilise abondamment les fractions rationnelles et le calcul integral.

### Progression et perspectives

Ces outils mathematiques ne sont pas une fin en soi mais un langage commun qui permet de decrire, analyser et concevoir des systemes electroniques. Leur maitrise conditionne la reussite dans les modules techniques des semestres suivants et, au-dela, dans la vie professionnelle d'ingenieur.

---

## Documents de Cours

<div class="pdf-container">
  <div class="pdf-viewer">

    <div class="pdf-item">
      <h4>Cours Polynomes</h4>
      <p>Support de cours sur les polynomes : definitions, operations, racines, factorisation et theoreme fondamental de l'algebre. Ce document couvre egalement la division euclidienne et les applications aux fonctions de transfert.</p>
      <embed src="/cours-pdf/S2/MATHS/cours polynômes.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/MATHS/cours polynômes.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Exercices Polynomes</h4>
      <p>Fascicule d'exercices sur les polynomes : factorisation, recherche de racines, division euclidienne et applications.</p>
      <embed src="/cours-pdf/S2/MATHS/exercice polynômes.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/MATHS/exercice polynômes.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Cours Fractions Rationnelles</h4>
      <p>Support de cours sur les fractions rationnelles : decomposition en elements simples, poles simples et multiples, poles complexes conjugues. Methodes de calcul et applications aux transformees inverses.</p>
      <embed src="/cours-pdf/S2/MATHS/exercice fractions rationnels.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/MATHS/exercice fractions rationnels.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Cours Calcul Integral</h4>
      <p>Support de cours sur le calcul integral : primitives, techniques d'integration (par parties, changement de variable, fonctions rationnelles) et applications au calcul de valeurs moyennes et efficaces.</p>
      <embed src="/cours-pdf/S2/MATHS/Cours intégral.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/MATHS/Cours intégral.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Exercices Calcul Integral</h4>
      <p>Fascicule d'exercices sur le calcul integral : calculs de primitives par differentes methodes, integrales definies et applications.</p>
      <embed src="/cours-pdf/S2/MATHS/exercice intégral.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/MATHS/exercice intégral.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Correction Exercices Calcul Integral</h4>
      <p>Corriges detailles des exercices de calcul integral : methodes de resolution pas a pas et verification des resultats.</p>
      <embed src="/cours-pdf/S2/MATHS/Correction calcul intégral.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/MATHS/Correction calcul intégral.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Cours Equations Differentielles du 1er Ordre</h4>
      <p>Support de cours sur les equations differentielles du premier ordre : forme generale, solution homogene, methode de variation de la constante, constante de temps et applications aux circuits RC et RL.</p>
      <embed src="/cours-pdf/S2/MATHS/Cours équation différentiel du 1er ordre.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/MATHS/Cours équation différentiel du 1er ordre.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Cours Equations Differentielles d'Ordre 2</h4>
      <p>Support de cours sur les equations differentielles du second ordre : equation caracteristique, les trois regimes (aperiodique, critique, pseudo-periodique), solutions avec second membre et applications aux circuits RLC.</p>
      <embed src="/cours-pdf/S2/MATHS/Cours équations différentielles d'ordre 2.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/MATHS/Cours équations différentielles d'ordre 2.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Exercices EDO du 1er Ordre</h4>
      <p>Fascicule d'exercices sur les equations differentielles du premier ordre : resolution, conditions initiales et applications aux circuits du premier ordre.</p>
      <embed src="/cours-pdf/S2/MATHS/Exercices équations différentielles d'ordre 1.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/MATHS/Exercices équations différentielles d'ordre 1.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Exercices EDO du 2nd Ordre</h4>
      <p>Fascicule d'exercices sur les equations differentielles du second ordre : determination du regime, resolution complete avec conditions initiales et applications aux circuits RLC.</p>
      <embed src="/cours-pdf/S2/MATHS/Exercices  équations différentielles d'ordre 2.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/MATHS/Exercices  équations différentielles d'ordre 2.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Annale Mathematiques GEII 2018-2019</h4>
      <p>Sujet d'examen de l'annee 2018-2019 couvrant l'ensemble du programme : polynomes, integrales, equations differentielles. Utile pour la preparation aux examens.</p>
      <embed src="/cours-pdf/S2/MATHS/annale 1.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/MATHS/annale 1.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

  </div>
</div>

---

<style>body{font-family:Arial,sans-serif;background-color:#f4f4f9;color:#333;line-height:1.6}h2,h3,h4,h5{color:#2a7ae2}p{text-align:justify}code{background-color:#f5f5f5;padding:2px 6px;border-radius:3px;font-family:'Courier New',monospace}pre{background-color:#f5f5f5;padding:15px;border-radius:5px;overflow-x:auto}</style>

<div class="back-nav">
  <a href="./my-courses-2020-2021.html">&larr; Retour a Mes Cours 2020-2021</a>
</div>

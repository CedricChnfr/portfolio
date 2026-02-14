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
  <a href="./my-courses-2020-2021.html">&larr; <span data-i18n="back_to_courses_2020_2021">Retour a Mes Cours 2020-2021</span></a>
</div>

<div class="lang-fr">

<h1>Mathematiques - S2</h1>

<p><strong>Annee</strong>: 2020-2021 | <strong>Semestre</strong>: 2 | <strong>Type</strong>: Scientifique</p>

<hr/>

<h2>PART A : PRESENTATION GENERALE</h2>

<h3>Contexte et objectifs</h3>

<p>Le cours de mathematiques du semestre 2 constitue un approfondissement majeur des outils mathematiques pour l'ingenieur. Il prolonge les bases acquises au S1 (derivees, limites, nombres complexes) en introduisant des concepts avances indispensables pour l'analyse de systemes electroniques, le traitement du signal et la modelisation de phenomenes physiques en GEII.</p>

<p>Ce semestre couvre cinq grands domaines : les polynomes, les fractions rationnelles, le calcul integral, les equations differentielles du premier ordre et les equations differentielles du second ordre. Chacun de ces domaines trouve des applications directes dans les cours techniques du cursus.</p>

<p><strong>Objectifs pedagogiques :</strong></p>
<ul>
  <li>Maitriser les polynomes et les fractions rationnelles pour l'analyse de fonctions de transfert</li>
  <li>Approfondir le calcul integral et ses applications au calcul de valeurs moyennes et efficaces</li>
  <li>Resoudre des equations differentielles du 1er et du 2eme ordre avec conditions initiales</li>
  <li>Appliquer les mathematiques aux systemes reels (circuits RC, RL, RLC)</li>
  <li>Utiliser les outils de decomposition en elements simples pour les transformees inverses</li>
  <li>Interpreter graphiquement et physiquement les solutions mathematiques</li>
</ul>

<h3>Organisation</h3>

<p>Le cours est structure autour de cinq modules complementaires. Chaque module comprend des cours magistraux (CM) ou l'enseignant presente la theorie, des travaux diriges (TD) pour la mise en pratique, et des fascicules d'exercices corriges. Les evaluations comprennent des controles continus et un examen final de synthese.</p>

<p>Le volume horaire est reparti approximativement comme suit :</p>
<ul>
  <li>Cours magistraux : environ 20 heures</li>
  <li>Travaux diriges : environ 20 heures</li>
  <li>Travail personnel et revisions : variable selon l'etudiant</li>
</ul>

<h3>Prerequis</h3>

<ul>
  <li>Calcul de derivees et primitives de base (S1)</li>
  <li>Nombres complexes et formes algebrique, trigonometrique, exponentielle</li>
  <li>Notions de limites et continuite</li>
  <li>Resolution d'equations du premier et second degre</li>
</ul>

<hr/>

<h2>PART B : EXPERIENCE ET CONTEXTE</h2>

<h3>Environnement pedagogique</h3>

<p>Le semestre 2 de mathematiques s'inscrit dans la continuite du S1 en consolidant les bases et en introduisant des outils plus avances necessaires pour les cours techniques. L'annee 2020-2021 a ete marquee par un enseignement partiellement a distance en raison du contexte sanitaire (COVID-19), ce qui a necessite une adaptation importante : cours en visioconference, exercices en ligne, et evaluations a distance.</p>

<p>Malgre ces contraintes, la qualite de l'enseignement a ete maintenue grace a des polycopies detailles, des seances de questions-reponses en ligne et des fascicules d'exercices complets avec corriges.</p>

<h3>Ressources et supports</h3>

<ul>
  <li><strong>Cours magistraux</strong> : Polycopies detailles pour chaque module (polynomes, integrales, EDO 1er et 2nd ordre)</li>
  <li><strong>Fascicules d'exercices</strong> : Recueils pour chaque chapitre avec solutions detaillees</li>
  <li><strong>Annales de partiels</strong> : Sujets des annees precedentes pour la preparation aux examens</li>
  <li><strong>Rappels de calcul</strong> : Fiches de rappel sur les fractions, fonctions de base et derivees</li>
  <li><strong>Cours sur les fractions rationnelles</strong> : Document specifique sur la decomposition en elements simples</li>
</ul>

<h3>Liens avec d'autres cours</h3>

<ul>
  <li><strong>Outils Logiciels (OL)</strong> : Application directe des mathematiques. Les series de Fourier et la transformee de Laplace utilisent les integrales et les fractions rationnelles. La decomposition en elements simples est essentielle pour le calcul de transformees inverses de Laplace.</li>
  <li><strong>Systemes Electroniques (SE)</strong> : L'analyse frequentielle repose sur les polynomes (numerateur et denominateur des fonctions de transfert). Les filtres sont decrits par des equations differentielles.</li>
  <li><strong>Energie</strong> : La modelisation de systemes electriques (circuits, machines) utilise les equations differentielles. Le calcul integral permet de determiner les valeurs moyennes et efficaces en triphase.</li>
  <li><strong>Informatique Embarquee (IE)</strong> : Les algorithmes numeriques de resolution d'equations differentielles (methode d'Euler) s'appuient sur la comprehension mathematique.</li>
  <li><strong>Travaux de Laboratoire (TL)</strong> : L'analyse des resultats experimentaux necessite la maitrise des outils mathematiques pour comparer theorie et mesures.</li>
</ul>

<h3>Difficultes et apprentissages</h3>

<p>Le passage aux equations differentielles du second ordre a represente un saut de difficulte important. La distinction entre les trois regimes (aperiodique, critique, pseudo-periodique) et la determination des constantes d'integration a partir des conditions initiales necessitent une bonne maitrise de l'ensemble des outils precedents. Le contexte d'enseignement a distance a rendu l'apprentissage plus autonome et a developpe la capacite a chercher et comprendre par soi-meme.</p>

<hr/>

<h2>PART C : ASPECTS TECHNIQUES</h2>

<h3>Module 1 : Polynomes</h3>

<h4>Definitions et proprietes fondamentales</h4>

<p>Un polynome P(x) de degre n est une expression de la forme :</p>

<p>P(x) = a_n * x^n + a_(n-1) * x^(n-1) + ... + a_1 * x + a_0</p>

<p>ou les a_i sont des coefficients reels (ou complexes) et a_n est non nul (coefficient dominant).</p>

<p><strong>Operations sur les polynomes :</strong></p>
<ul>
  <li><strong>Addition</strong> : On additionne les coefficients de meme degre. Si P(x) = 3x^2 + 2x + 1 et Q(x) = x^2 - x + 4, alors P(x) + Q(x) = 4x^2 + x + 5.</li>
  <li><strong>Multiplication</strong> : On multiplie chaque terme par chaque terme et on regroupe. Le degre du produit est la somme des degres.</li>
  <li><strong>Division euclidienne</strong> : Pour P et D avec deg(P) >= deg(D), il existe un quotient Q et un reste R uniques tels que P = D * Q + R avec deg(R) &lt; deg(D).</li>
</ul>

<p><strong>Exemple de division euclidienne :</strong></p>
<p>Diviser P(x) = 2x^3 + 3x^2 - x + 5 par D(x) = x - 1 :</p>
<ul>
  <li>2x^3 / x = 2x^2, puis on soustrait 2x^2 * (x - 1) = 2x^3 - 2x^2</li>
  <li>Reste intermediaire : 5x^2 - x + 5</li>
  <li>5x^2 / x = 5x, puis on soustrait 5x * (x - 1) = 5x^2 - 5x</li>
  <li>Reste intermediaire : 4x + 5</li>
  <li>4x / x = 4, puis on soustrait 4 * (x - 1) = 4x - 4</li>
  <li>Reste final : 9</li>
  <li>Resultat : P(x) = (x - 1)(2x^2 + 5x + 4) + 9</li>
</ul>

<h4>Racines et factorisation</h4>

<p><strong>Theoreme fondamental de l'algebre</strong> : Tout polynome de degre n >= 1 a coefficients complexes possede exactement n racines dans C (comptees avec multiplicite).</p>

<p><strong>Theoreme de factorisation</strong> : Si r_1, r_2, ..., r_n sont les racines de P(x), alors :</p>
<p>P(x) = a_n * (x - r_1)(x - r_2)...(x - r_n)</p>

<p><strong>Propriete des racines complexes conjuguees</strong> : Si P(x) a des coefficients reels et si z = a + jb est une racine, alors son conjugue z* = a - jb est aussi une racine. Ces deux racines produisent un facteur quadratique irreductible :</p>
<p>(x - z)(x - z*) = x^2 - 2ax + (a^2 + b^2)</p>

<p><strong>Exemple</strong> : P(x) = x^3 - 6x^2 + 11x - 6</p>
<ul>
  <li>On teste x = 1 : P(1) = 1 - 6 + 11 - 6 = 0, donc x = 1 est racine</li>
  <li>Division par (x - 1) : P(x) = (x - 1)(x^2 - 5x + 6) = (x - 1)(x - 2)(x - 3)</li>
  <li>Les racines sont x = 1, x = 2, x = 3</li>
</ul>

<h4>Applications en GEII</h4>

<p>En electronique, les polynomes interviennent dans les fonctions de transfert. Une fonction de transfert H(s) est le rapport de deux polynomes en s :</p>

<p>H(s) = N(s) / D(s) = (b_m * s^m + ... + b_0) / (a_n * s^n + ... + a_0)</p>

<p>Les racines du numerateur N(s) sont les <strong>zeros</strong> de H(s) et les racines du denominateur D(s) sont les <strong>poles</strong>. La stabilite d'un systeme est determinee par la position des poles dans le plan complexe : un systeme est stable si et seulement si tous les poles ont une partie reelle strictement negative.</p>

<p><strong>Exemple</strong> : Pour un filtre passe-bas du 2eme ordre avec H(s) = w0^2 / (s^2 + 2*z*w0*s + w0^2), les poles sont :</p>
<p>s = -z*w0 +/- w0*sqrt(z^2 - 1)</p>
<p>Si z > 0, les poles ont une partie reelle negative et le systeme est stable.</p>

<h3>Module 2 : Fractions rationnelles</h3>

<h4>Decomposition en elements simples</h4>

<p>Une fraction rationnelle F(x) = P(x)/Q(x) avec deg(P) &lt; deg(Q) peut etre decomposee en somme d'elements simples.</p>

<p><strong>Cas de poles simples reels</strong> : Si Q(x) = (x - a_1)(x - a_2)...(x - a_n) avec tous les a_i distincts, alors :</p>
<p>F(x) = A_1/(x - a_1) + A_2/(x - a_2) + ... + A_n/(x - a_n)</p>

<p>Pour trouver A_i, on multiplie par (x - a_i) et on evalue en x = a_i :</p>
<p>A_i = [(x - a_i) * F(x)] evalue en x = a_i</p>

<p><strong>Exemple</strong> : Decomposer F(x) = (3x + 1) / ((x - 1)(x + 2))</p>

<p>F(x) = A/(x - 1) + B/(x + 2)</p>
<ul>
  <li>A = [(x - 1) * F(x)] en x = 1 = (3 + 1) / (1 + 2) = 4/3</li>
  <li>B = [(x + 2) * F(x)] en x = -2 = (-6 + 1) / (-2 - 1) = -5/(-3) = 5/3</li>
  <li>F(x) = (4/3)/(x - 1) + (5/3)/(x + 2)</li>
</ul>

<p><strong>Cas de poles multiples</strong> : Si Q(x) contient un facteur (x - a)^k, la decomposition contient :</p>
<p>A_1/(x - a) + A_2/(x - a)^2 + ... + A_k/(x - a)^k</p>

<p><strong>Exemple</strong> : F(x) = (2x + 3) / (x - 1)^2</p>
<p>F(x) = A/(x - 1) + B/(x - 1)^2</p>
<ul>
  <li>B = [(x - 1)^2 * F(x)] en x = 1 = 2 + 3 = 5</li>
  <li>Pour A, on multiplie par (x - 1)^2 et on derive : d/dx[(2x + 3)] = 2, donc A = 2</li>
  <li>F(x) = 2/(x - 1) + 5/(x - 1)^2</li>
</ul>

<p><strong>Cas de poles complexes conjugues</strong> : Si Q(x) contient un facteur irreductible (x^2 + bx + c), la decomposition contient :</p>
<p>(Ax + B) / (x^2 + bx + c)</p>

<p><strong>Exemple</strong> : F(x) = 1 / (x(x^2 + 1))</p>
<p>F(x) = A/x + (Bx + C)/(x^2 + 1)</p>
<ul>
  <li>A = [x * F(x)] en x = 0 = 1/1 = 1</li>
  <li>En multipliant par x(x^2 + 1) : 1 = A(x^2 + 1) + (Bx + C)x</li>
  <li>1 = (A + B)x^2 + Cx + A</li>
  <li>A + B = 0 donc B = -1, C = 0, A = 1</li>
  <li>F(x) = 1/x + (-x)/(x^2 + 1)</li>
</ul>

<h4>Applications aux transformees inverses de Laplace</h4>

<p>La decomposition en elements simples est la methode principale pour calculer les transformees inverses de Laplace. On decompose F(s), puis on utilise les tables :</p>

<ul>
  <li>A/(s - a) --> A * e^(at)</li>
  <li>A/(s - a)^2 --> A * t * e^(at)</li>
  <li>(As + B)/(s^2 + w^2) --> A*cos(wt) + (B/w)*sin(wt)</li>
</ul>

<h3>Module 3 : Calcul integral</h3>

<h4>Primitives et integrales definies</h4>

<p><strong>Definition</strong> : Une primitive de f(x) est une fonction F(x) telle que F'(x) = f(x). L'integrale definie est :</p>
<p>integrale de a a b de f(x)dx = F(b) - F(a)</p>

<p><strong>Primitives de reference :</strong></p>
<ul>
  <li>integrale de x^n dx = x^(n+1)/(n+1) + C (n different de -1)</li>
  <li>integrale de 1/x dx = ln|x| + C</li>
  <li>integrale de e^(ax) dx = (1/a) * e^(ax) + C</li>
  <li>integrale de cos(ax) dx = (1/a) * sin(ax) + C</li>
  <li>integrale de sin(ax) dx = -(1/a) * cos(ax) + C</li>
  <li>integrale de 1/(1 + x^2) dx = arctan(x) + C</li>
  <li>integrale de 1/sqrt(1 - x^2) dx = arcsin(x) + C</li>
</ul>

<h4>Integration par parties</h4>

<p><strong>Formule</strong> : integrale de u*dv = u*v - integrale de v*du</p>

<p>Le choix de u et dv est crucial. La regle mnemonique LIATE (Logarithme, Inverse trigonometrique, Algebrique, Trigonometrique, Exponentielle) aide a choisir u.</p>

<p><strong>Exemple 1</strong> : Calculer integrale de x * e^x dx</p>
<ul>
  <li>u = x, dv = e^x dx</li>
  <li>du = dx, v = e^x</li>
  <li>integrale de x * e^x dx = x * e^x - integrale de e^x dx = x * e^x - e^x + C = e^x(x - 1) + C</li>
</ul>

<p><strong>Exemple 2</strong> : Calculer integrale de x^2 * cos(x) dx</p>
<ul>
  <li>u = x^2, dv = cos(x) dx --> du = 2x dx, v = sin(x)</li>
  <li>integrale = x^2 * sin(x) - 2 * integrale de x * sin(x) dx</li>
  <li>Pour le deuxieme terme : u = x, dv = sin(x) dx --> du = dx, v = -cos(x)</li>
  <li>integrale de x * sin(x) dx = -x * cos(x) + integrale de cos(x) dx = -x * cos(x) + sin(x) + C</li>
  <li>Resultat final : x^2 * sin(x) + 2x * cos(x) - 2 * sin(x) + C</li>
</ul>

<p><strong>Exemple 3</strong> : Calculer integrale de ln(x) dx</p>
<ul>
  <li>u = ln(x), dv = dx</li>
  <li>du = dx/x, v = x</li>
  <li>integrale = x * ln(x) - integrale de dx = x * ln(x) - x + C</li>
</ul>

<h4>Changement de variable</h4>

<p><strong>Principe</strong> : On pose x = g(t), alors dx = g'(t)dt et on transforme l'integrale.</p>

<p><strong>Exemple</strong> : Calculer integrale de 1/sqrt(1 - x^2) dx</p>
<ul>
  <li>Substitution trigonometrique : x = sin(t), dx = cos(t) dt</li>
  <li>integrale de cos(t)/sqrt(1 - sin^2(t)) dt = integrale de cos(t)/cos(t) dt = integrale de dt = t + C</li>
  <li>Resultat : arcsin(x) + C</li>
</ul>

<p><strong>Exemple</strong> : Calculer integrale de 2x * e^(x^2) dx</p>
<ul>
  <li>Substitution : u = x^2, du = 2x dx</li>
  <li>integrale de e^u du = e^u + C = e^(x^2) + C</li>
</ul>

<h4>Integration de fonctions rationnelles</h4>

<p>Pour integrer P(x)/Q(x), on effectue d'abord la division euclidienne si deg(P) >= deg(Q), puis on decompose en elements simples :</p>

<p><strong>Exemple</strong> : integrale de (3x + 1)/((x - 1)(x + 2)) dx</p>
<ul>
  <li>Decomposition : (4/3)/(x - 1) + (5/3)/(x + 2) (calculee precedemment)</li>
  <li>integrale = (4/3)*ln|x - 1| + (5/3)*ln|x + 2| + C</li>
</ul>

<p><strong>Exemple</strong> : integrale de 1/(x^2 + 1) dx = arctan(x) + C</p>

<p><strong>Exemple</strong> : integrale de (2x + 3)/(x^2 + 4) dx</p>
<ul>
  <li>Separation : integrale de 2x/(x^2 + 4) dx + integrale de 3/(x^2 + 4) dx</li>
  <li>Premier terme : ln(x^2 + 4) (par reconnaissance de u'/u)</li>
  <li>Second terme : (3/2) * arctan(x/2) (par table)</li>
  <li>Resultat : ln(x^2 + 4) + (3/2)*arctan(x/2) + C</li>
</ul>

<h4>Applications en GEII</h4>

<p><strong>Calcul de la valeur moyenne d'un signal</strong> :</p>
<p>V_moy = (1/T) * integrale de 0 a T de v(t) dt</p>

<p><strong>Calcul de la valeur efficace (RMS)</strong> :</p>
<p>V_eff = sqrt((1/T) * integrale de 0 a T de v(t)^2 dt)</p>

<p><strong>Exemple</strong> : Pour un signal sinusoidal v(t) = V_max * sin(wt) :</p>
<ul>
  <li>V_moy sur une periode complete = 0</li>
  <li>V_eff = V_max / sqrt(2)</li>
</ul>

<p><strong>Calcul d'energie</strong> :</p>
<p>W = integrale de 0 a T de p(t) dt = integrale de 0 a T de v(t) * i(t) dt</p>

<h3>Module 4 : Equations differentielles du 1er ordre</h3>

<h4>Forme generale et methodes de resolution</h4>

<p><strong>Forme generale lineaire</strong> : y' + a(x) * y = b(x)</p>

<p><strong>Equation homogene associee</strong> : y' + a(x) * y = 0</p>
<ul>
  <li>Solution : y_h = C * e^(-integrale de a(x)dx)</li>
</ul>

<p><strong>Cas a coefficients constants</strong> : y' + a*y = b(x)</p>
<ul>
  <li>Solution homogene : y_h = C * e^(-ax)</li>
  <li>La constante de temps est tau = 1/a</li>
</ul>

<p><strong>Methode de variation de la constante</strong> :</p>
<ol>
  <li>Resoudre l'equation homogene : y_h = C * e^(-ax)</li>
  <li>Poser y_p = C(x) * e^(-ax)</li>
  <li>Substituer dans l'equation complete pour trouver C(x)</li>
  <li>Solution generale : y = y_h + y_p</li>
</ol>

<p><strong>Exemple detaille</strong> : Resoudre y' + 2y = 6</p>

<ol>
  <li>Equation homogene : y' + 2y = 0 --> y_h = C * e^(-2x)</li>
  <li>Solution particuliere : on cherche y_p constante (car second membre constant)
    <ul><li>y_p' + 2*y_p = 6 --> 0 + 2*y_p = 6 --> y_p = 3</li></ul>
  </li>
  <li>Solution generale : y(x) = C * e^(-2x) + 3</li>
  <li>Avec condition initiale y(0) = 0 : 0 = C + 3 --> C = -3</li>
  <li>Solution : y(x) = 3(1 - e^(-2x))</li>
</ol>

<p><strong>Exemple avec second membre exponentiel</strong> : Resoudre y' + 3y = e^(-x)</p>

<ol>
  <li>Solution homogene : y_h = C * e^(-3x)</li>
  <li>Solution particuliere : on essaie y_p = A * e^(-x)
    <ul>
      <li>y_p' = -A * e^(-x)</li>
      <li>-A * e^(-x) + 3A * e^(-x) = e^(-x) --> 2A = 1 --> A = 1/2</li>
    </ul>
  </li>
  <li>Solution generale : y(x) = C * e^(-3x) + (1/2) * e^(-x)</li>
</ol>

<h4>Application aux circuits RC et RL</h4>

<p><strong>Circuit RC en charge</strong> : La tension aux bornes du condensateur u_c(t) verifie :</p>
<p>RC * u_c' + u_c = E (avec E la tension d'alimentation)</p>

<p>C'est une EDO du 1er ordre avec tau = RC.</p>
<ul>
  <li>Solution : u_c(t) = E * (1 - e^(-t/tau))</li>
  <li>Le condensateur atteint 63% de E apres un temps tau</li>
  <li>On considere la charge complete apres 5*tau (99.3% de E)</li>
</ul>

<p><strong>Circuit RL</strong> : Le courant i(t) dans une bobine verifie :</p>
<p>L * i' + R * i = E</p>

<p>Avec tau = L/R :</p>
<ul>
  <li>Solution : i(t) = (E/R) * (1 - e^(-t/tau))</li>
</ul>

<p><strong>Decharge d'un condensateur</strong> (circuit RC sans source) :</p>
<p>RC * u_c' + u_c = 0</p>
<ul>
  <li>Solution : u_c(t) = U_0 * e^(-t/tau) ou U_0 est la tension initiale</li>
</ul>

<h3>Module 5 : Equations differentielles du 2eme ordre</h3>

<h4>Forme generale et equation caracteristique</h4>

<p><strong>Forme generale normalisee</strong> : y'' + 2*z*w0*y' + w0^2*y = f(t)</p>

<p>ou z (zeta) est le coefficient d'amortissement et w0 est la pulsation propre non amortie.</p>

<p><strong>Equation caracteristique</strong> : r^2 + 2*z*w0*r + w0^2 = 0</p>

<p>Le discriminant est : Delta = 4*w0^2*(z^2 - 1)</p>

<h4>Les trois regimes</h4>

<p><strong>Regime aperiodique (z > 1)</strong> : Delta > 0, deux racines reelles negatives distinctes</p>
<ul>
  <li>r_1 = -z*w0 + w0*sqrt(z^2 - 1)</li>
  <li>r_2 = -z*w0 - w0*sqrt(z^2 - 1)</li>
  <li>Solution homogene : y_h(t) = A*e^(r_1*t) + B*e^(r_2*t)</li>
  <li>Le systeme revient lentement a l'equilibre sans oscillation</li>
  <li>Plus z est grand, plus le retour est lent</li>
</ul>

<p><strong>Regime critique (z = 1)</strong> : Delta = 0, racine double r = -w0</p>
<ul>
  <li>Solution homogene : y_h(t) = (A + B*t)*e^(-w0*t)</li>
  <li>C'est le regime le plus rapide sans depassement</li>
  <li>Optimal pour les systemes d'asservissement</li>
</ul>

<p><strong>Regime pseudo-periodique (0 &lt; z &lt; 1)</strong> : Delta &lt; 0, racines complexes conjuguees</p>
<ul>
  <li>r = -z*w0 +/- j*w0*sqrt(1 - z^2)</li>
  <li>La pseudo-pulsation est : w_p = w0*sqrt(1 - z^2)</li>
  <li>Solution homogene : y_h(t) = e^(-z*w0*t) * [A*cos(w_p*t) + B*sin(w_p*t)]</li>
  <li>Le systeme oscille avec une amplitude decroissante</li>
  <li>La pseudo-periode est T_p = 2*pi/w_p</li>
  <li>Le premier depassement est : D1 = e^(-pi*z/sqrt(1 - z^2))</li>
</ul>

<p><strong>Exemple detaille</strong> : Resoudre y'' + 4y' + 3y = 6</p>

<ol>
  <li>Equation caracteristique : r^2 + 4r + 3 = 0
    <ul>
      <li>Delta = 16 - 12 = 4 > 0</li>
      <li>r_1 = (-4 + 2)/2 = -1, r_2 = (-4 - 2)/2 = -3</li>
    </ul>
  </li>
  <li>Solution homogene : y_h(t) = A*e^(-t) + B*e^(-3t)</li>
  <li>Solution particuliere (second membre constant) : y_p = 6/3 = 2</li>
  <li>Solution generale : y(t) = A*e^(-t) + B*e^(-3t) + 2</li>
  <li>Conditions initiales y(0) = 0, y'(0) = 0 :
    <ul>
      <li>A + B + 2 = 0</li>
      <li>-A - 3B = 0 --> A = -3B</li>
      <li>-3B + B + 2 = 0 --> B = 1, A = -3</li>
    </ul>
  </li>
  <li>Solution : y(t) = -3*e^(-t) + e^(-3t) + 2</li>
</ol>

<p><strong>Exemple en regime pseudo-periodique</strong> : Resoudre y'' + 2y' + 5y = 10</p>

<ol>
  <li>Equation caracteristique : r^2 + 2r + 5 = 0
    <ul>
      <li>Delta = 4 - 20 = -16 &lt; 0</li>
      <li>r = (-2 +/- j*4)/2 = -1 +/- j*2</li>
    </ul>
  </li>
  <li>z*w0 = 1, w0^2 = 5 --> w0 = sqrt(5), z = 1/sqrt(5) = 0.447</li>
  <li>w_p = 2 (pseudo-pulsation)</li>
  <li>Solution homogene : y_h(t) = e^(-t) * [A*cos(2t) + B*sin(2t)]</li>
  <li>Solution particuliere : y_p = 10/5 = 2</li>
  <li>Solution generale : y(t) = e^(-t) * [A*cos(2t) + B*sin(2t)] + 2</li>
  <li>Conditions initiales y(0) = 0, y'(0) = 0 :
    <ul>
      <li>A + 2 = 0 --> A = -2</li>
      <li>-A + 2B = 0 --> B = A/2 = -1</li>
    </ul>
  </li>
  <li>Solution : y(t) = 2 - e^(-t) * [2*cos(2t) + sin(2t)]</li>
</ol>

<h4>Application aux circuits RLC</h4>

<p><strong>Circuit RLC serie</strong> : La tension aux bornes du condensateur u_c(t) verifie :</p>
<p>LC * u_c'' + RC * u_c' + u_c = E</p>

<p>En forme normalisee : u_c'' + (R/L)*u_c' + (1/LC)*u_c = E/LC</p>

<p>On identifie :</p>
<ul>
  <li>w0 = 1/sqrt(LC) (pulsation propre)</li>
  <li>z = R/(2*sqrt(L/C)) = R/(2*L*w0) (coefficient d'amortissement)</li>
  <li>Le facteur de qualite est Q = 1/(2*z) = (1/R)*sqrt(L/C)</li>
</ul>

<p><strong>Comportement selon z</strong> :</p>
<ul>
  <li>z > 1 (R eleve) : regime aperiodique, le circuit se decharge lentement</li>
  <li>z = 1 (R = 2*sqrt(L/C)) : regime critique, retour le plus rapide sans oscillation</li>
  <li>z &lt; 1 (R faible) : regime pseudo-periodique, oscillations amorties</li>
</ul>

<p><strong>Exemple numerique</strong> : Circuit RLC avec R = 100 ohms, L = 10 mH, C = 1 uF</p>
<ul>
  <li>w0 = 1/sqrt(10e-3 * 1e-6) = 10000 rad/s (f0 = 1591 Hz)</li>
  <li>z = 100/(2 * sqrt(10e-3/1e-6)) = 100/(2 * 100) = 0.5</li>
  <li>Regime pseudo-periodique (z &lt; 1)</li>
  <li>w_p = 10000 * sqrt(1 - 0.25) = 8660 rad/s</li>
  <li>T_p = 2*pi/8660 = 0.726 ms</li>
</ul>

<h3>Travaux diriges et exercices</h3>

<p><strong>Exercices sur les polynomes et fractions rationnelles :</strong></p>
<ul>
  <li>Factorisation de polynomes de degre 3 et 4</li>
  <li>Decomposition en elements simples de fractions rationnelles</li>
  <li>Application a l'integration de fonctions rationnelles</li>
</ul>

<p><strong>Exercices sur le calcul integral :</strong></p>
<ul>
  <li>Calcul d'integrales par differentes methodes (par parties, changement de variable)</li>
  <li>Integrales de fonctions trigonometriques</li>
  <li>Applications au calcul de valeurs moyennes et efficaces</li>
</ul>

<p><strong>Exercices sur les EDO :</strong></p>
<ul>
  <li>Resolution d'equations differentielles du 1er et 2nd ordre</li>
  <li>Determination des constantes avec conditions initiales</li>
  <li>Modelisation de circuits RC, RL et RLC</li>
  <li>Identification du regime a partir des parametres du circuit</li>
</ul>

<p><strong>Annales et preparation aux examens :</strong></p>
<ul>
  <li>Sujets de partiels des annees precedentes</li>
  <li>Exercices de synthese melant plusieurs modules</li>
  <li>Problemes ouverts de modelisation</li>
</ul>

<hr/>

<h2>PART D : ANALYSE ET REFLEXION</h2>

<h3>Competences acquises</h3>

<ul>
  <li><strong>Maitrise des outils mathematiques fondamentaux</strong> : Polynomes, fractions rationnelles, integrales et equations differentielles constituent la boite a outils essentielle de l'ingenieur en electronique.</li>
  <li><strong>Capacite a resoudre des equations differentielles lineaires</strong> : Aussi bien du 1er que du 2nd ordre, avec conditions initiales, ce qui est directement applicable aux circuits electriques.</li>
  <li><strong>Passage entre domaine temporel et frequentiel</strong> : La comprehension des polynomes et fractions rationnelles prepare au passage de Laplace et a l'analyse frequentielle.</li>
  <li><strong>Modelisation de phenomenes physiques</strong> : Traduction d'un probleme physique en equation mathematique, resolution, puis interpretation du resultat.</li>
  <li><strong>Interpretation graphique et physique</strong> : Associer une solution mathematique a un comportement physique (constante de temps, oscillations, amortissement).</li>
</ul>

<h3>Auto-evaluation</h3>

<p>Les mathematiques du S2 ont constitue un approfondissement majeur et un pilier pour toute la suite du cursus GEII. Les equations differentielles du second ordre, en particulier, sont omnipresentes : tout circuit RLC, tout systeme mecanique masse-ressort-amortisseur, tout filtre du second ordre est decrit par une telle equation.</p>

<p>La comprehension intuitive des trois regimes (aperiodique, critique, pseudo-periodique) et de leur signification physique est l'un des acquis les plus importants. Le lien entre le coefficient d'amortissement z et le comportement du systeme est une notion qui revient dans presque tous les cours techniques.</p>

<p>Le calcul integral, bien que plus classique, s'est revele indispensable pour le calcul de valeurs efficaces en energie (signaux triphases, redresses) et pour les coefficients de Fourier en Outils Logiciels.</p>

<p>Le contexte d'enseignement a distance a renforce l'autonomie et la capacite a apprendre par soi-meme, competences precieuses pour la suite des etudes.</p>

<h3>Connexions interdisciplinaires</h3>

<ul>
  <li><strong>Vers les Outils Logiciels (S2)</strong> : Les polynomes et fractions rationnelles sont directement utilises pour les transformees de Laplace inverses. Le calcul integral est la base des coefficients de Fourier.</li>
  <li><strong>Vers les Systemes Electroniques</strong> : Les fonctions de transfert sont des fractions rationnelles dont les poles et zeros determinent le comportement frequentiel des filtres.</li>
  <li><strong>Vers l'Energie</strong> : Les equations differentielles modelisent les machines electriques. Les integrales calculent puissances et energies.</li>
  <li><strong>Vers les semestres suivants (S3-S4)</strong> : Les automatismes, la regulation, le traitement du signal reposent tous sur ces fondamentaux mathematiques. La transformee de Laplace, etudiee en OL, utilise abondamment les fractions rationnelles et le calcul integral.</li>
</ul>

<h3>Progression et perspectives</h3>

<p>Ces outils mathematiques ne sont pas une fin en soi mais un langage commun qui permet de decrire, analyser et concevoir des systemes electroniques. Leur maitrise conditionne la reussite dans les modules techniques des semestres suivants et, au-dela, dans la vie professionnelle d'ingenieur.</p>

<hr/>

<h2>Documents de Cours</h2>

<div class="pdf-container">
  <div class="pdf-viewer">

    <div class="pdf-item">
      <h4>Cours Polynomes</h4>
      <p>Support de cours sur les polynomes : definitions, operations, racines, factorisation et theoreme fondamental de l'algebre. Ce document couvre egalement la division euclidienne et les applications aux fonctions de transfert.</p>
      <embed src="/cours-pdf/S2/MATHS/cours_polynômes.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/MATHS/cours_polynômes.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Exercices Polynomes</h4>
      <p>Fascicule d'exercices sur les polynomes : factorisation, recherche de racines, division euclidienne et applications.</p>
      <embed src="/cours-pdf/S2/MATHS/exercice_polynômes.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/MATHS/exercice_polynômes.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Cours Fractions Rationnelles</h4>
      <p>Support de cours sur les fractions rationnelles : decomposition en elements simples, poles simples et multiples, poles complexes conjugues. Methodes de calcul et applications aux transformees inverses.</p>
      <embed src="/cours-pdf/S2/MATHS/exercice_fractions_rationnels.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/MATHS/exercice_fractions_rationnels.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Cours Calcul Integral</h4>
      <p>Support de cours sur le calcul integral : primitives, techniques d'integration (par parties, changement de variable, fonctions rationnelles) et applications au calcul de valeurs moyennes et efficaces.</p>
      <embed src="/cours-pdf/S2/MATHS/Cours_intégral.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/MATHS/Cours_intégral.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Exercices Calcul Integral</h4>
      <p>Fascicule d'exercices sur le calcul integral : calculs de primitives par differentes methodes, integrales definies et applications.</p>
      <embed src="/cours-pdf/S2/MATHS/exercice_intégral.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/MATHS/exercice_intégral.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Correction Exercices Calcul Integral</h4>
      <p>Corriges detailles des exercices de calcul integral : methodes de resolution pas a pas et verification des resultats.</p>
      <embed src="/cours-pdf/S2/MATHS/Correction_calcul_intégral.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/MATHS/Correction_calcul_intégral.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Cours Equations Differentielles du 1er Ordre</h4>
      <p>Support de cours sur les equations differentielles du premier ordre : forme generale, solution homogene, methode de variation de la constante, constante de temps et applications aux circuits RC et RL.</p>
      <embed src="/cours-pdf/S2/MATHS/Cours_équation_différentiel_du_1er_ordre.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/MATHS/Cours_équation_différentiel_du_1er_ordre.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Cours Equations Differentielles d'Ordre 2</h4>
      <p>Support de cours sur les equations differentielles du second ordre : equation caracteristique, les trois regimes (aperiodique, critique, pseudo-periodique), solutions avec second membre et applications aux circuits RLC.</p>
      <embed src="/cours-pdf/S2/MATHS/Cours_équations_différentielles_d'ordre_2.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/MATHS/Cours_équations_différentielles_d'ordre_2.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Exercices EDO du 1er Ordre</h4>
      <p>Fascicule d'exercices sur les equations differentielles du premier ordre : resolution, conditions initiales et applications aux circuits du premier ordre.</p>
      <embed src="/cours-pdf/S2/MATHS/Exercices_équations_différentielles_d'ordre_1.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/MATHS/Exercices_équations_différentielles_d'ordre_1.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Exercices EDO du 2nd Ordre</h4>
      <p>Fascicule d'exercices sur les equations differentielles du second ordre : determination du regime, resolution complete avec conditions initiales et applications aux circuits RLC.</p>
      <embed src="/cours-pdf/S2/MATHS/Exercices_équations_différentielles_d'ordre_2.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/MATHS/Exercices_équations_différentielles_d'ordre_2.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Annale Mathematiques GEII 2018-2019</h4>
      <p>Sujet d'examen de l'annee 2018-2019 couvrant l'ensemble du programme : polynomes, integrales, equations differentielles. Utile pour la preparation aux examens.</p>
      <embed src="/cours-pdf/S2/MATHS/annale_1.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/MATHS/annale_1.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

  </div>
</div>

</div>

<div class="lang-en">

<h1>Mathematics - S2</h1>

<p><strong>Year</strong>: 2020-2021 | <strong>Semester</strong>: 2 | <strong>Type</strong>: Scientific</p>

<hr/>

<h2>PART A: GENERAL OVERVIEW</h2>

<h3>Context and objectives</h3>

<p>The semester 2 mathematics course represents a major deepening of the mathematical tools for engineers. It extends the foundations acquired in S1 (derivatives, limits, complex numbers) by introducing advanced concepts essential for the analysis of electronic systems, signal processing, and the modeling of physical phenomena in GEII (Electrical Engineering and Industrial Computing).</p>

<p>This semester covers five major areas: polynomials, rational fractions, integral calculus, first-order differential equations, and second-order differential equations. Each of these areas has direct applications in the technical courses of the curriculum.</p>

<p><strong>Learning objectives:</strong></p>
<ul>
  <li>Master polynomials and rational fractions for transfer function analysis</li>
  <li>Deepen integral calculus and its applications for computing average and RMS values</li>
  <li>Solve first and second-order differential equations with initial conditions</li>
  <li>Apply mathematics to real systems (RC, RL, RLC circuits)</li>
  <li>Use partial fraction decomposition tools for inverse transforms</li>
  <li>Interpret solutions both graphically and physically</li>
</ul>

<h3>Organization</h3>

<p>The course is structured around five complementary modules. Each module includes lectures (CM) where the instructor presents the theory, tutorials (TD) for hands-on practice, and corrected exercise booklets. Assessments include continuous evaluations and a final comprehensive exam.</p>

<p>The hourly volume is approximately distributed as follows:</p>
<ul>
  <li>Lectures: approximately 20 hours</li>
  <li>Tutorials: approximately 20 hours</li>
  <li>Personal work and revision: varies by student</li>
</ul>

<h3>Prerequisites</h3>

<ul>
  <li>Basic derivative and antiderivative computation (S1)</li>
  <li>Complex numbers in algebraic, trigonometric, and exponential forms</li>
  <li>Notions of limits and continuity</li>
  <li>Solving first and second degree equations</li>
</ul>

<hr/>

<h2>PART B: EXPERIENCE AND CONTEXT</h2>

<h3>Educational environment</h3>

<p>The semester 2 mathematics course follows on from S1 by consolidating the foundations and introducing more advanced tools needed for technical courses. The 2020-2021 academic year was marked by partially remote teaching due to the health crisis (COVID-19), which required significant adaptation: video conference lectures, online exercises, and remote assessments.</p>

<p>Despite these constraints, teaching quality was maintained through detailed handouts, online Q&amp;A sessions, and comprehensive exercise booklets with solutions.</p>

<h3>Resources and materials</h3>

<ul>
  <li><strong>Lectures</strong>: Detailed handouts for each module (polynomials, integrals, 1st and 2nd order ODEs)</li>
  <li><strong>Exercise booklets</strong>: Collections for each chapter with detailed solutions</li>
  <li><strong>Past exams</strong>: Previous years' exam papers for exam preparation</li>
  <li><strong>Calculation reminders</strong>: Reference sheets on fractions, basic functions, and derivatives</li>
  <li><strong>Rational fractions course</strong>: Specific document on partial fraction decomposition</li>
</ul>

<h3>Links with other courses</h3>

<ul>
  <li><strong>Software Tools (OL)</strong>: Direct application of mathematics. Fourier series and the Laplace transform use integrals and rational fractions. Partial fraction decomposition is essential for computing inverse Laplace transforms.</li>
  <li><strong>Electronic Systems (SE)</strong>: Frequency analysis relies on polynomials (numerator and denominator of transfer functions). Filters are described by differential equations.</li>
  <li><strong>Energy</strong>: Modeling electrical systems (circuits, machines) uses differential equations. Integral calculus determines average and RMS values in three-phase systems.</li>
  <li><strong>Embedded Computing (IE)</strong>: Numerical algorithms for solving differential equations (Euler's method) rely on mathematical understanding.</li>
  <li><strong>Laboratory Work (TL)</strong>: Analyzing experimental results requires mastery of mathematical tools to compare theory and measurements.</li>
</ul>

<h3>Difficulties and learning</h3>

<p>The transition to second-order differential equations represented a significant leap in difficulty. Distinguishing between the three regimes (overdamped, critically damped, underdamped) and determining integration constants from initial conditions requires a solid command of all previous tools. The remote teaching context made learning more autonomous and developed the ability to research and understand independently.</p>

<hr/>

<h2>PART C: TECHNICAL ASPECTS</h2>

<h3>Module 1: Polynomials</h3>

<h4>Definitions and fundamental properties</h4>

<p>A polynomial P(x) of degree n is an expression of the form:</p>

<p>P(x) = a_n * x^n + a_(n-1) * x^(n-1) + ... + a_1 * x + a_0</p>

<p>where the a_i are real (or complex) coefficients and a_n is non-zero (leading coefficient).</p>

<p><strong>Operations on polynomials:</strong></p>
<ul>
  <li><strong>Addition</strong>: Add coefficients of the same degree. If P(x) = 3x^2 + 2x + 1 and Q(x) = x^2 - x + 4, then P(x) + Q(x) = 4x^2 + x + 5.</li>
  <li><strong>Multiplication</strong>: Multiply each term by each term and combine. The degree of the product is the sum of the degrees.</li>
  <li><strong>Euclidean division</strong>: For P and D with deg(P) >= deg(D), there exist unique quotient Q and remainder R such that P = D * Q + R with deg(R) &lt; deg(D).</li>
</ul>

<p><strong>Euclidean division example:</strong></p>
<p>Divide P(x) = 2x^3 + 3x^2 - x + 5 by D(x) = x - 1:</p>
<ul>
  <li>2x^3 / x = 2x^2, then subtract 2x^2 * (x - 1) = 2x^3 - 2x^2</li>
  <li>Intermediate remainder: 5x^2 - x + 5</li>
  <li>5x^2 / x = 5x, then subtract 5x * (x - 1) = 5x^2 - 5x</li>
  <li>Intermediate remainder: 4x + 5</li>
  <li>4x / x = 4, then subtract 4 * (x - 1) = 4x - 4</li>
  <li>Final remainder: 9</li>
  <li>Result: P(x) = (x - 1)(2x^2 + 5x + 4) + 9</li>
</ul>

<h4>Roots and factorization</h4>

<p><strong>Fundamental theorem of algebra</strong>: Every polynomial of degree n >= 1 with complex coefficients has exactly n roots in C (counted with multiplicity).</p>

<p><strong>Factorization theorem</strong>: If r_1, r_2, ..., r_n are the roots of P(x), then:</p>
<p>P(x) = a_n * (x - r_1)(x - r_2)...(x - r_n)</p>

<p><strong>Complex conjugate roots property</strong>: If P(x) has real coefficients and if z = a + jb is a root, then its conjugate z* = a - jb is also a root. These two roots produce an irreducible quadratic factor:</p>
<p>(x - z)(x - z*) = x^2 - 2ax + (a^2 + b^2)</p>

<p><strong>Example</strong>: P(x) = x^3 - 6x^2 + 11x - 6</p>
<ul>
  <li>Test x = 1: P(1) = 1 - 6 + 11 - 6 = 0, so x = 1 is a root</li>
  <li>Division by (x - 1): P(x) = (x - 1)(x^2 - 5x + 6) = (x - 1)(x - 2)(x - 3)</li>
  <li>The roots are x = 1, x = 2, x = 3</li>
</ul>

<h4>Applications in GEII</h4>

<p>In electronics, polynomials appear in transfer functions. A transfer function H(s) is the ratio of two polynomials in s:</p>

<p>H(s) = N(s) / D(s) = (b_m * s^m + ... + b_0) / (a_n * s^n + ... + a_0)</p>

<p>The roots of the numerator N(s) are the <strong>zeros</strong> of H(s) and the roots of the denominator D(s) are the <strong>poles</strong>. System stability is determined by the position of the poles in the complex plane: a system is stable if and only if all poles have a strictly negative real part.</p>

<p><strong>Example</strong>: For a 2nd-order low-pass filter with H(s) = w0^2 / (s^2 + 2*z*w0*s + w0^2), the poles are:</p>
<p>s = -z*w0 +/- w0*sqrt(z^2 - 1)</p>
<p>If z > 0, the poles have a negative real part and the system is stable.</p>

<h3>Module 2: Rational fractions</h3>

<h4>Partial fraction decomposition</h4>

<p>A rational fraction F(x) = P(x)/Q(x) with deg(P) &lt; deg(Q) can be decomposed into a sum of simple elements.</p>

<p><strong>Case of simple real poles</strong>: If Q(x) = (x - a_1)(x - a_2)...(x - a_n) with all a_i distinct, then:</p>
<p>F(x) = A_1/(x - a_1) + A_2/(x - a_2) + ... + A_n/(x - a_n)</p>

<p>To find A_i, multiply by (x - a_i) and evaluate at x = a_i:</p>
<p>A_i = [(x - a_i) * F(x)] evaluated at x = a_i</p>

<p><strong>Example</strong>: Decompose F(x) = (3x + 1) / ((x - 1)(x + 2))</p>

<p>F(x) = A/(x - 1) + B/(x + 2)</p>
<ul>
  <li>A = [(x - 1) * F(x)] at x = 1 = (3 + 1) / (1 + 2) = 4/3</li>
  <li>B = [(x + 2) * F(x)] at x = -2 = (-6 + 1) / (-2 - 1) = -5/(-3) = 5/3</li>
  <li>F(x) = (4/3)/(x - 1) + (5/3)/(x + 2)</li>
</ul>

<p><strong>Case of multiple poles</strong>: If Q(x) contains a factor (x - a)^k, the decomposition contains:</p>
<p>A_1/(x - a) + A_2/(x - a)^2 + ... + A_k/(x - a)^k</p>

<p><strong>Example</strong>: F(x) = (2x + 3) / (x - 1)^2</p>
<p>F(x) = A/(x - 1) + B/(x - 1)^2</p>
<ul>
  <li>B = [(x - 1)^2 * F(x)] at x = 1 = 2 + 3 = 5</li>
  <li>For A, multiply by (x - 1)^2 and differentiate: d/dx[(2x + 3)] = 2, so A = 2</li>
  <li>F(x) = 2/(x - 1) + 5/(x - 1)^2</li>
</ul>

<p><strong>Case of complex conjugate poles</strong>: If Q(x) contains an irreducible factor (x^2 + bx + c), the decomposition contains:</p>
<p>(Ax + B) / (x^2 + bx + c)</p>

<p><strong>Example</strong>: F(x) = 1 / (x(x^2 + 1))</p>
<p>F(x) = A/x + (Bx + C)/(x^2 + 1)</p>
<ul>
  <li>A = [x * F(x)] at x = 0 = 1/1 = 1</li>
  <li>Multiplying by x(x^2 + 1): 1 = A(x^2 + 1) + (Bx + C)x</li>
  <li>1 = (A + B)x^2 + Cx + A</li>
  <li>A + B = 0 so B = -1, C = 0, A = 1</li>
  <li>F(x) = 1/x + (-x)/(x^2 + 1)</li>
</ul>

<h4>Applications to inverse Laplace transforms</h4>

<p>Partial fraction decomposition is the main method for computing inverse Laplace transforms. We decompose F(s), then use the tables:</p>

<ul>
  <li>A/(s - a) --> A * e^(at)</li>
  <li>A/(s - a)^2 --> A * t * e^(at)</li>
  <li>(As + B)/(s^2 + w^2) --> A*cos(wt) + (B/w)*sin(wt)</li>
</ul>

<h3>Module 3: Integral calculus</h3>

<h4>Antiderivatives and definite integrals</h4>

<p><strong>Definition</strong>: An antiderivative of f(x) is a function F(x) such that F'(x) = f(x). The definite integral is:</p>
<p>integral from a to b of f(x)dx = F(b) - F(a)</p>

<p><strong>Reference antiderivatives:</strong></p>
<ul>
  <li>integral of x^n dx = x^(n+1)/(n+1) + C (n not equal to -1)</li>
  <li>integral of 1/x dx = ln|x| + C</li>
  <li>integral of e^(ax) dx = (1/a) * e^(ax) + C</li>
  <li>integral of cos(ax) dx = (1/a) * sin(ax) + C</li>
  <li>integral of sin(ax) dx = -(1/a) * cos(ax) + C</li>
  <li>integral of 1/(1 + x^2) dx = arctan(x) + C</li>
  <li>integral of 1/sqrt(1 - x^2) dx = arcsin(x) + C</li>
</ul>

<h4>Integration by parts</h4>

<p><strong>Formula</strong>: integral of u*dv = u*v - integral of v*du</p>

<p>The choice of u and dv is crucial. The mnemonic rule LIATE (Logarithmic, Inverse trigonometric, Algebraic, Trigonometric, Exponential) helps choose u.</p>

<p><strong>Example 1</strong>: Compute integral of x * e^x dx</p>
<ul>
  <li>u = x, dv = e^x dx</li>
  <li>du = dx, v = e^x</li>
  <li>integral of x * e^x dx = x * e^x - integral of e^x dx = x * e^x - e^x + C = e^x(x - 1) + C</li>
</ul>

<p><strong>Example 2</strong>: Compute integral of x^2 * cos(x) dx</p>
<ul>
  <li>u = x^2, dv = cos(x) dx --> du = 2x dx, v = sin(x)</li>
  <li>integral = x^2 * sin(x) - 2 * integral of x * sin(x) dx</li>
  <li>For the second term: u = x, dv = sin(x) dx --> du = dx, v = -cos(x)</li>
  <li>integral of x * sin(x) dx = -x * cos(x) + integral of cos(x) dx = -x * cos(x) + sin(x) + C</li>
  <li>Final result: x^2 * sin(x) + 2x * cos(x) - 2 * sin(x) + C</li>
</ul>

<p><strong>Example 3</strong>: Compute integral of ln(x) dx</p>
<ul>
  <li>u = ln(x), dv = dx</li>
  <li>du = dx/x, v = x</li>
  <li>integral = x * ln(x) - integral of dx = x * ln(x) - x + C</li>
</ul>

<h4>Substitution (change of variable)</h4>

<p><strong>Principle</strong>: Let x = g(t), then dx = g'(t)dt and transform the integral.</p>

<p><strong>Example</strong>: Compute integral of 1/sqrt(1 - x^2) dx</p>
<ul>
  <li>Trigonometric substitution: x = sin(t), dx = cos(t) dt</li>
  <li>integral of cos(t)/sqrt(1 - sin^2(t)) dt = integral of cos(t)/cos(t) dt = integral of dt = t + C</li>
  <li>Result: arcsin(x) + C</li>
</ul>

<p><strong>Example</strong>: Compute integral of 2x * e^(x^2) dx</p>
<ul>
  <li>Substitution: u = x^2, du = 2x dx</li>
  <li>integral of e^u du = e^u + C = e^(x^2) + C</li>
</ul>

<h4>Integration of rational functions</h4>

<p>To integrate P(x)/Q(x), first perform Euclidean division if deg(P) >= deg(Q), then decompose into partial fractions:</p>

<p><strong>Example</strong>: integral of (3x + 1)/((x - 1)(x + 2)) dx</p>
<ul>
  <li>Decomposition: (4/3)/(x - 1) + (5/3)/(x + 2) (computed previously)</li>
  <li>integral = (4/3)*ln|x - 1| + (5/3)*ln|x + 2| + C</li>
</ul>

<p><strong>Example</strong>: integral of 1/(x^2 + 1) dx = arctan(x) + C</p>

<p><strong>Example</strong>: integral of (2x + 3)/(x^2 + 4) dx</p>
<ul>
  <li>Separation: integral of 2x/(x^2 + 4) dx + integral of 3/(x^2 + 4) dx</li>
  <li>First term: ln(x^2 + 4) (by recognizing u'/u pattern)</li>
  <li>Second term: (3/2) * arctan(x/2) (from table)</li>
  <li>Result: ln(x^2 + 4) + (3/2)*arctan(x/2) + C</li>
</ul>

<h4>Applications in GEII</h4>

<p><strong>Computing the average value of a signal</strong>:</p>
<p>V_avg = (1/T) * integral from 0 to T of v(t) dt</p>

<p><strong>Computing the RMS (root mean square) value</strong>:</p>
<p>V_rms = sqrt((1/T) * integral from 0 to T of v(t)^2 dt)</p>

<p><strong>Example</strong>: For a sinusoidal signal v(t) = V_max * sin(wt):</p>
<ul>
  <li>V_avg over a complete period = 0</li>
  <li>V_rms = V_max / sqrt(2)</li>
</ul>

<p><strong>Energy calculation</strong>:</p>
<p>W = integral from 0 to T of p(t) dt = integral from 0 to T of v(t) * i(t) dt</p>

<h3>Module 4: First-order differential equations</h3>

<h4>General form and solution methods</h4>

<p><strong>General linear form</strong>: y' + a(x) * y = b(x)</p>

<p><strong>Associated homogeneous equation</strong>: y' + a(x) * y = 0</p>
<ul>
  <li>Solution: y_h = C * e^(-integral of a(x)dx)</li>
</ul>

<p><strong>Constant coefficient case</strong>: y' + a*y = b(x)</p>
<ul>
  <li>Homogeneous solution: y_h = C * e^(-ax)</li>
  <li>The time constant is tau = 1/a</li>
</ul>

<p><strong>Variation of constants method</strong>:</p>
<ol>
  <li>Solve the homogeneous equation: y_h = C * e^(-ax)</li>
  <li>Set y_p = C(x) * e^(-ax)</li>
  <li>Substitute into the complete equation to find C(x)</li>
  <li>General solution: y = y_h + y_p</li>
</ol>

<p><strong>Detailed example</strong>: Solve y' + 2y = 6</p>

<ol>
  <li>Homogeneous equation: y' + 2y = 0 --> y_h = C * e^(-2x)</li>
  <li>Particular solution: seek constant y_p (since the right-hand side is constant)
    <ul><li>y_p' + 2*y_p = 6 --> 0 + 2*y_p = 6 --> y_p = 3</li></ul>
  </li>
  <li>General solution: y(x) = C * e^(-2x) + 3</li>
  <li>With initial condition y(0) = 0: 0 = C + 3 --> C = -3</li>
  <li>Solution: y(x) = 3(1 - e^(-2x))</li>
</ol>

<p><strong>Example with exponential right-hand side</strong>: Solve y' + 3y = e^(-x)</p>

<ol>
  <li>Homogeneous solution: y_h = C * e^(-3x)</li>
  <li>Particular solution: try y_p = A * e^(-x)
    <ul>
      <li>y_p' = -A * e^(-x)</li>
      <li>-A * e^(-x) + 3A * e^(-x) = e^(-x) --> 2A = 1 --> A = 1/2</li>
    </ul>
  </li>
  <li>General solution: y(x) = C * e^(-3x) + (1/2) * e^(-x)</li>
</ol>

<h4>Application to RC and RL circuits</h4>

<p><strong>RC charging circuit</strong>: The capacitor voltage u_c(t) satisfies:</p>
<p>RC * u_c' + u_c = E (where E is the supply voltage)</p>

<p>This is a 1st order ODE with tau = RC.</p>
<ul>
  <li>Solution: u_c(t) = E * (1 - e^(-t/tau))</li>
  <li>The capacitor reaches 63% of E after one time constant tau</li>
  <li>Charging is considered complete after 5*tau (99.3% of E)</li>
</ul>

<p><strong>RL circuit</strong>: The current i(t) through an inductor satisfies:</p>
<p>L * i' + R * i = E</p>

<p>With tau = L/R:</p>
<ul>
  <li>Solution: i(t) = (E/R) * (1 - e^(-t/tau))</li>
</ul>

<p><strong>Capacitor discharge</strong> (RC circuit without source):</p>
<p>RC * u_c' + u_c = 0</p>
<ul>
  <li>Solution: u_c(t) = U_0 * e^(-t/tau) where U_0 is the initial voltage</li>
</ul>

<h3>Module 5: Second-order differential equations</h3>

<h4>General form and characteristic equation</h4>

<p><strong>Normalized general form</strong>: y'' + 2*z*w0*y' + w0^2*y = f(t)</p>

<p>where z (zeta) is the damping coefficient and w0 is the natural undamped angular frequency.</p>

<p><strong>Characteristic equation</strong>: r^2 + 2*z*w0*r + w0^2 = 0</p>

<p>The discriminant is: Delta = 4*w0^2*(z^2 - 1)</p>

<h4>The three regimes</h4>

<p><strong>Overdamped regime (z > 1)</strong>: Delta > 0, two distinct negative real roots</p>
<ul>
  <li>r_1 = -z*w0 + w0*sqrt(z^2 - 1)</li>
  <li>r_2 = -z*w0 - w0*sqrt(z^2 - 1)</li>
  <li>Homogeneous solution: y_h(t) = A*e^(r_1*t) + B*e^(r_2*t)</li>
  <li>The system slowly returns to equilibrium without oscillation</li>
  <li>The larger z is, the slower the return</li>
</ul>

<p><strong>Critically damped regime (z = 1)</strong>: Delta = 0, double root r = -w0</p>
<ul>
  <li>Homogeneous solution: y_h(t) = (A + B*t)*e^(-w0*t)</li>
  <li>This is the fastest regime without overshoot</li>
  <li>Optimal for servo-control systems</li>
</ul>

<p><strong>Underdamped regime (0 &lt; z &lt; 1)</strong>: Delta &lt; 0, complex conjugate roots</p>
<ul>
  <li>r = -z*w0 +/- j*w0*sqrt(1 - z^2)</li>
  <li>The pseudo-angular frequency is: w_p = w0*sqrt(1 - z^2)</li>
  <li>Homogeneous solution: y_h(t) = e^(-z*w0*t) * [A*cos(w_p*t) + B*sin(w_p*t)]</li>
  <li>The system oscillates with decreasing amplitude</li>
  <li>The pseudo-period is T_p = 2*pi/w_p</li>
  <li>The first overshoot is: D1 = e^(-pi*z/sqrt(1 - z^2))</li>
</ul>

<p><strong>Detailed example</strong>: Solve y'' + 4y' + 3y = 6</p>

<ol>
  <li>Characteristic equation: r^2 + 4r + 3 = 0
    <ul>
      <li>Delta = 16 - 12 = 4 > 0</li>
      <li>r_1 = (-4 + 2)/2 = -1, r_2 = (-4 - 2)/2 = -3</li>
    </ul>
  </li>
  <li>Homogeneous solution: y_h(t) = A*e^(-t) + B*e^(-3t)</li>
  <li>Particular solution (constant right-hand side): y_p = 6/3 = 2</li>
  <li>General solution: y(t) = A*e^(-t) + B*e^(-3t) + 2</li>
  <li>Initial conditions y(0) = 0, y'(0) = 0:
    <ul>
      <li>A + B + 2 = 0</li>
      <li>-A - 3B = 0 --> A = -3B</li>
      <li>-3B + B + 2 = 0 --> B = 1, A = -3</li>
    </ul>
  </li>
  <li>Solution: y(t) = -3*e^(-t) + e^(-3t) + 2</li>
</ol>

<p><strong>Underdamped example</strong>: Solve y'' + 2y' + 5y = 10</p>

<ol>
  <li>Characteristic equation: r^2 + 2r + 5 = 0
    <ul>
      <li>Delta = 4 - 20 = -16 &lt; 0</li>
      <li>r = (-2 +/- j*4)/2 = -1 +/- j*2</li>
    </ul>
  </li>
  <li>z*w0 = 1, w0^2 = 5 --> w0 = sqrt(5), z = 1/sqrt(5) = 0.447</li>
  <li>w_p = 2 (pseudo-angular frequency)</li>
  <li>Homogeneous solution: y_h(t) = e^(-t) * [A*cos(2t) + B*sin(2t)]</li>
  <li>Particular solution: y_p = 10/5 = 2</li>
  <li>General solution: y(t) = e^(-t) * [A*cos(2t) + B*sin(2t)] + 2</li>
  <li>Initial conditions y(0) = 0, y'(0) = 0:
    <ul>
      <li>A + 2 = 0 --> A = -2</li>
      <li>-A + 2B = 0 --> B = A/2 = -1</li>
    </ul>
  </li>
  <li>Solution: y(t) = 2 - e^(-t) * [2*cos(2t) + sin(2t)]</li>
</ol>

<h4>Application to RLC circuits</h4>

<p><strong>Series RLC circuit</strong>: The capacitor voltage u_c(t) satisfies:</p>
<p>LC * u_c'' + RC * u_c' + u_c = E</p>

<p>In normalized form: u_c'' + (R/L)*u_c' + (1/LC)*u_c = E/LC</p>

<p>We identify:</p>
<ul>
  <li>w0 = 1/sqrt(LC) (natural angular frequency)</li>
  <li>z = R/(2*sqrt(L/C)) = R/(2*L*w0) (damping coefficient)</li>
  <li>The quality factor is Q = 1/(2*z) = (1/R)*sqrt(L/C)</li>
</ul>

<p><strong>Behavior depending on z</strong>:</p>
<ul>
  <li>z > 1 (high R): overdamped regime, the circuit discharges slowly</li>
  <li>z = 1 (R = 2*sqrt(L/C)): critically damped regime, fastest return without oscillation</li>
  <li>z &lt; 1 (low R): underdamped regime, damped oscillations</li>
</ul>

<p><strong>Numerical example</strong>: RLC circuit with R = 100 ohms, L = 10 mH, C = 1 uF</p>
<ul>
  <li>w0 = 1/sqrt(10e-3 * 1e-6) = 10000 rad/s (f0 = 1591 Hz)</li>
  <li>z = 100/(2 * sqrt(10e-3/1e-6)) = 100/(2 * 100) = 0.5</li>
  <li>Underdamped regime (z &lt; 1)</li>
  <li>w_p = 10000 * sqrt(1 - 0.25) = 8660 rad/s</li>
  <li>T_p = 2*pi/8660 = 0.726 ms</li>
</ul>

<h3>Tutorials and exercises</h3>

<p><strong>Exercises on polynomials and rational fractions:</strong></p>
<ul>
  <li>Factorization of degree 3 and 4 polynomials</li>
  <li>Partial fraction decomposition of rational fractions</li>
  <li>Application to integration of rational functions</li>
</ul>

<p><strong>Exercises on integral calculus:</strong></p>
<ul>
  <li>Computing integrals by various methods (by parts, substitution)</li>
  <li>Integrals of trigonometric functions</li>
  <li>Applications to computing average and RMS values</li>
</ul>

<p><strong>Exercises on ODEs:</strong></p>
<ul>
  <li>Solving 1st and 2nd order differential equations</li>
  <li>Determining constants with initial conditions</li>
  <li>Modeling RC, RL, and RLC circuits</li>
  <li>Identifying the regime from circuit parameters</li>
</ul>

<p><strong>Past exams and exam preparation:</strong></p>
<ul>
  <li>Exam papers from previous years</li>
  <li>Synthesis exercises combining multiple modules</li>
  <li>Open-ended modeling problems</li>
</ul>

<hr/>

<h2>PART D: ANALYSIS AND REFLECTION</h2>

<h3>Skills acquired</h3>

<ul>
  <li><strong>Mastery of fundamental mathematical tools</strong>: Polynomials, rational fractions, integrals, and differential equations form the essential toolkit of the electronics engineer.</li>
  <li><strong>Ability to solve linear differential equations</strong>: Both 1st and 2nd order, with initial conditions, directly applicable to electrical circuits.</li>
  <li><strong>Transition between time and frequency domains</strong>: Understanding polynomials and rational fractions prepares for the Laplace transform and frequency analysis.</li>
  <li><strong>Modeling physical phenomena</strong>: Translating a physical problem into a mathematical equation, solving it, then interpreting the result.</li>
  <li><strong>Graphical and physical interpretation</strong>: Associating a mathematical solution with physical behavior (time constant, oscillations, damping).</li>
</ul>

<h3>Self-assessment</h3>

<p>The S2 mathematics course represented a major deepening and a pillar for the entire GEII curriculum. Second-order differential equations, in particular, are ubiquitous: every RLC circuit, every mass-spring-damper mechanical system, every second-order filter is described by such an equation.</p>

<p>The intuitive understanding of the three regimes (overdamped, critically damped, underdamped) and their physical meaning is one of the most important acquisitions. The link between the damping coefficient z and the system behavior is a concept that recurs in almost every technical course.</p>

<p>Integral calculus, although more classical, proved indispensable for computing RMS values in energy courses (three-phase and rectified signals) and for Fourier coefficients in Software Tools.</p>

<p>The remote teaching context strengthened autonomy and the ability to learn independently, valuable skills for the rest of the studies.</p>

<h3>Interdisciplinary connections</h3>

<ul>
  <li><strong>Towards Software Tools (S2)</strong>: Polynomials and rational fractions are directly used for inverse Laplace transforms. Integral calculus is the foundation of Fourier coefficients.</li>
  <li><strong>Towards Electronic Systems</strong>: Transfer functions are rational fractions whose poles and zeros determine the frequency behavior of filters.</li>
  <li><strong>Towards Energy</strong>: Differential equations model electrical machines. Integrals compute power and energy.</li>
  <li><strong>Towards subsequent semesters (S3-S4)</strong>: Automation, control, and signal processing all rely on these mathematical foundations. The Laplace transform, studied in OL, extensively uses rational fractions and integral calculus.</li>
</ul>

<h3>Progression and perspectives</h3>

<p>These mathematical tools are not an end in themselves but a common language that enables describing, analyzing, and designing electronic systems. Mastering them is essential for success in the technical modules of subsequent semesters and, beyond that, in the professional life of an engineer.</p>

<hr/>

<h2>Course Documents</h2>

<div class="pdf-container">
  <div class="pdf-viewer">

    <div class="pdf-item">
      <h4>Polynomials Course</h4>
      <p>Course material on polynomials: definitions, operations, roots, factorization, and the fundamental theorem of algebra. This document also covers Euclidean division and applications to transfer functions.</p>
      <embed src="/cours-pdf/S2/MATHS/cours_polynômes.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/MATHS/cours_polynômes.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Download PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Polynomials Exercises</h4>
      <p>Exercise booklet on polynomials: factorization, root finding, Euclidean division, and applications.</p>
      <embed src="/cours-pdf/S2/MATHS/exercice_polynômes.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/MATHS/exercice_polynômes.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Download PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Rational Fractions Course</h4>
      <p>Course material on rational fractions: partial fraction decomposition, simple and multiple poles, complex conjugate poles. Calculation methods and applications to inverse transforms.</p>
      <embed src="/cours-pdf/S2/MATHS/exercice_fractions_rationnels.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/MATHS/exercice_fractions_rationnels.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Download PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Integral Calculus Course</h4>
      <p>Course material on integral calculus: antiderivatives, integration techniques (by parts, substitution, rational functions), and applications to computing average and RMS values.</p>
      <embed src="/cours-pdf/S2/MATHS/Cours_intégral.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/MATHS/Cours_intégral.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Download PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Integral Calculus Exercises</h4>
      <p>Exercise booklet on integral calculus: computing antiderivatives using various methods, definite integrals, and applications.</p>
      <embed src="/cours-pdf/S2/MATHS/exercice_intégral.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/MATHS/exercice_intégral.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Download PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Integral Calculus Exercises - Solutions</h4>
      <p>Detailed solutions for integral calculus exercises: step-by-step solution methods and result verification.</p>
      <embed src="/cours-pdf/S2/MATHS/Correction_calcul_intégral.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/MATHS/Correction_calcul_intégral.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Download PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>First-Order Differential Equations Course</h4>
      <p>Course material on first-order differential equations: general form, homogeneous solution, variation of constants method, time constant, and applications to RC and RL circuits.</p>
      <embed src="/cours-pdf/S2/MATHS/Cours_équation_différentiel_du_1er_ordre.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/MATHS/Cours_équation_différentiel_du_1er_ordre.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Download PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Second-Order Differential Equations Course</h4>
      <p>Course material on second-order differential equations: characteristic equation, the three regimes (overdamped, critically damped, underdamped), solutions with right-hand side, and applications to RLC circuits.</p>
      <embed src="/cours-pdf/S2/MATHS/Cours_équations_différentielles_d'ordre_2.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/MATHS/Cours_équations_différentielles_d'ordre_2.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Download PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>First-Order ODE Exercises</h4>
      <p>Exercise booklet on first-order differential equations: solving, initial conditions, and applications to first-order circuits.</p>
      <embed src="/cours-pdf/S2/MATHS/Exercices_équations_différentielles_d'ordre_1.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/MATHS/Exercices_équations_différentielles_d'ordre_1.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Download PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Second-Order ODE Exercises</h4>
      <p>Exercise booklet on second-order differential equations: regime identification, complete solving with initial conditions, and applications to RLC circuits.</p>
      <embed src="/cours-pdf/S2/MATHS/Exercices_équations_différentielles_d'ordre_2.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/MATHS/Exercices_équations_différentielles_d'ordre_2.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Download PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>GEII Mathematics Past Exam 2018-2019</h4>
      <p>Exam paper from the 2018-2019 academic year covering the entire syllabus: polynomials, integrals, differential equations. Useful for exam preparation.</p>
      <embed src="/cours-pdf/S2/MATHS/annale_1.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/MATHS/annale_1.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Download PDF</a>
      </p>
    </div>

  </div>
</div>

</div>

<style>body{font-family:Arial,sans-serif;background-color:#f4f4f9;color:#333;line-height:1.6}h2,h3,h4,h5{color:#2a7ae2}p{text-align:justify}code{background-color:#f5f5f5;padding:2px 6px;border-radius:3px;font-family:'Courier New',monospace}pre{background-color:#f5f5f5;padding:15px;border-radius:5px;overflow-x:auto}</style>

<div class="back-nav">
  <a href="./my-courses-2020-2021.html">&larr; <span data-i18n="back_to_courses_2020_2021">Retour a Mes Cours 2020-2021</span></a>
</div>

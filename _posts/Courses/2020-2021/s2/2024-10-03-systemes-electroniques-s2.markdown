---
layout: default
title: "Systemes Electroniques (SE) - S2"
date: 2024-10-02 10:56:03 +0200
---

<style>
.back-nav { margin-bottom: 20px; }
.back-nav a { text-decoration: none; color: #2a7ae2; font-weight: 600; }
.back-nav a:hover { text-decoration: underline; }
.section-title { color: #2a7ae2; border-bottom: 2px solid #2a7ae2; padding-bottom: 10px; margin-top: 30px; margin-bottom: 20px; }
</style>

<div class="back-nav">
  <a href="./my-courses-2020-2021.html" data-i18n-html="back_courses_2020_2021">&larr; Retour a Mes Cours 2020-2021</a>
</div>

<div class="lang-fr">

<h1>Systemes Electroniques (SE) - S2</h1>

<p><strong>Annee</strong>: 2020-2021 | <strong>Semestre</strong>: 2 | <strong>Type</strong>: Electronique</p>

<hr/>

<h2>PART A : PRESENTATION GENERALE</h2>

<h3>Contexte et objectifs</h3>

<p>Le cours de Systemes Electroniques du semestre 2 couvre l'analyse des systemes electroniques du point de vue frequentiel et temporel. Il introduit les outils mathematiques et les methodes d'analyse necessaires pour comprendre et concevoir des circuits electroniques analogiques. Le programme s'articule autour de 7 chapitres, allant des quadripoles aux applications de l'amplificateur operationnel, en passant par les filtres passifs et la modulation d'amplitude.</p>

<p><strong>Objectifs pedagogiques :</strong></p>
<ul>
  <li>Analyser des reseaux a quatre bornes (quadripoles) a l'aide de matrices impedance et admittance</li>
  <li>Etudier la reponse transitoire des circuits du premier ordre (RC, RL)</li>
  <li>Maitriser la representation frequentielle (diagrammes de Bode) et temporelle des systemes</li>
  <li>Concevoir et dimensionner des filtres passifs (passe-bas, passe-haut, passe-bande)</li>
  <li>Comprendre les principes de la modulation d'amplitude (AM)</li>
  <li>Appliquer les amplificateurs operationnels dans des montages avances</li>
</ul>

<h3>Organisation du cours</h3>

<p>Le cours est organise en 7 chapitres suivant une progression logique :</p>
<ol>
  <li><strong>Chapitre 1</strong> : Quadripoles (reseaux a quatre bornes)</li>
  <li><strong>Chapitre 3</strong> : Circuits du premier ordre (passe-bas, passe-haut)</li>
  <li><strong>Chapitre 4</strong> : Filtres passifs et reponse frequentielle</li>
  <li><strong>Chapitre 5</strong> : Amplificateur operationnel (AOP) - applications avancees</li>
  <li><strong>Chapitre 6</strong> : Representation temporelle et frequentielle</li>
  <li><strong>Chapitre 7</strong> : Modulation d'amplitude (AM)</li>
  <li><strong>TD et exercices</strong> : Fascicules de TD pour mise en pratique</li>
</ol>

<h3>Competences visees (BUT GEII)</h3>

<p>Ce module contribue au bloc de competences "Electronique et Systemes" :</p>
<ul>
  <li>Analyser le comportement frequentiel d'un circuit</li>
  <li>Concevoir des filtres analogiques passifs</li>
  <li>Utiliser les diagrammes de Bode pour caracteriser un systeme</li>
  <li>Comprendre les principes de modulation pour les telecommunications</li>
</ul>

<hr/>

<h2>PART B : EXPERIENCE ET CONTEXTE</h2>

<h3>Environnement pedagogique</h3>

<p>L'enseignement de Systemes Electroniques se deroule sous forme de cours magistraux, de travaux diriges (TD) et de travaux de laboratoire (TL). Les TD permettent de mettre en pratique les concepts theoriques par le calcul, tandis que les TL offrent une confrontation directe avec les circuits reels sur les bancs de mesure de l'IUT.</p>

<h3>Deroulement du semestre</h3>

<p>Le semestre a ete marque par la situation sanitaire (2020-2021), avec une alternance entre cours en presentiel et cours a distance. Les TD ont ete realises en partie en distanciel, avec des fascicules de TD detailles fournis par les enseignants. Les TL ont ete maintenus en presentiel autant que possible pour permettre la manipulation des instruments de mesure.</p>

<h3>Outils et instruments utilises</h3>

<ul>
  <li><strong>Oscilloscope numerique</strong> : Visualisation des signaux temporels, mesure de dephasage et d'amplitude</li>
  <li><strong>Generateur de fonctions</strong> : Generation de signaux sinusoidaux, carres, triangulaires pour les tests</li>
  <li><strong>Multimetre de precision</strong> : Mesures de tensions, courants, impedances</li>
  <li><strong>LTspice</strong> : Simulation de circuits analogiques pour verification des calculs</li>
  <li><strong>Calculatrice scientifique</strong> : Calculs de fonctions de transfert, conversion dB</li>
</ul>

<h3>Liens avec d'autres cours</h3>

<ul>
  <li><strong>Mathematiques S2</strong> : Nombres complexes, transformees de Laplace, equations differentielles</li>
  <li><strong>OL (Outils Logiciels)</strong> : Transformation de Laplace, series de Fourier</li>
  <li><strong>TL (Travaux de Laboratoire)</strong> : Mise en pratique sur circuits reels</li>
  <li><strong>Energie</strong> : Circuits triphases et puissance</li>
  <li><strong>Programmation S3+</strong> : Simulation numerique de filtres</li>
</ul>

<hr/>

<h2>PART C : ASPECTS TECHNIQUES</h2>

<h3>Chapitre 1 : Quadripoles (Reseaux a quatre bornes)</h3>

<p>Un quadripole est un reseau electrique a deux ports (quatre bornes) : un port d'entree et un port de sortie. Il est caracterise par les relations entre les tensions et courants d'entree et de sortie.</p>

<h4>Matrices impedance et admittance</h4>

<p>La <strong>matrice impedance [Z]</strong> relie les tensions aux courants :</p>

<pre>
| V1 |   | Z11  Z12 |   | I1 |
|    | = |          | x |    |
| V2 |   | Z21  Z22 |   | I2 |
</pre>

<p>Ou :</p>
<ul>
  <li>Z11 = V1/I1 (quand I2 = 0) : impedance d'entree a vide</li>
  <li>Z22 = V2/I2 (quand I1 = 0) : impedance de sortie a vide</li>
  <li>Z12 = V1/I2 (quand I1 = 0) : impedance de transfert inverse</li>
  <li>Z21 = V2/I1 (quand I2 = 0) : impedance de transfert directe</li>
</ul>

<p>La <strong>matrice admittance [Y]</strong> est l'inverse de la matrice impedance :</p>

<pre>
| I1 |   | Y11  Y12 |   | V1 |
|    | = |          | x |    |
| I2 |   | Y21  Y22 |   | V2 |

avec [Y] = [Z]^(-1)
</pre>

<h4>Matrice de chaine (ABCD)</h4>

<p>Pour la mise en cascade de quadripoles, on utilise la matrice chaine :</p>

<pre>
| V1 |   | A  B |   |  V2 |
|    | = |      | x |     |
| I1 |   | C  D |   | -I2 |
</pre>

<p>L'avantage de cette representation est que la mise en cascade de deux quadripoles revient a multiplier leurs matrices :</p>

<pre>
[T_total] = [T1] x [T2]
</pre>

<h4>Exemples de matrices ABCD pour des elements simples</h4>

<p>Pour une <strong>impedance serie Z</strong> :</p>
<pre>
| A  B |   | 1  Z |
|      | = |      |
| C  D |   | 0  1 |
</pre>

<p>Pour une <strong>admittance parallele Y</strong> :</p>
<pre>
| A  B |   | 1  0 |
|      | = |      |
| C  D |   | Y  1 |
</pre>

<h3>Chapitre 2 : Circuits du premier ordre</h3>

<p>Les circuits du premier ordre contiennent un seul element reactif (condensateur C ou inductance L) associe a des resistances.</p>

<h4>Circuit RC serie - Reponse a un echelon</h4>

<p>Pour un circuit RC serie soumis a un echelon de tension E :</p>

<p><strong>Equation differentielle :</strong></p>
<pre>
RC * dVc/dt + Vc = E
</pre>

<p><strong>Solution (charge du condensateur) :</strong></p>
<pre>
Vc(t) = E * (1 - exp(-t / tau))

avec tau = RC  (constante de temps)
</pre>

<p><strong>Solution (decharge du condensateur) :</strong></p>
<pre>
Vc(t) = E * exp(-t / tau)
</pre>

<p>La constante de temps tau = RC determine la vitesse de reponse :</p>
<ul>
  <li>A t = tau : Vc atteint 63.2% de la valeur finale</li>
  <li>A t = 3*tau : Vc atteint 95% de la valeur finale</li>
  <li>A t = 5*tau : Vc atteint 99.3% de la valeur finale (regime permanent)</li>
</ul>

<h4>Circuit RL serie - Reponse a un echelon</h4>

<p>Pour un circuit RL serie soumis a un echelon de tension E :</p>

<p><strong>Equation differentielle :</strong></p>
<pre>
L * dI/dt + R * I = E
</pre>

<p><strong>Solution :</strong></p>
<pre>
I(t) = (E/R) * (1 - exp(-t / tau))

avec tau = L/R  (constante de temps)
</pre>

<h4>Regime transitoire et regime permanent</h4>

<p>Le regime transitoire correspond a la phase pendant laquelle le circuit evolue vers son etat d'equilibre. En pratique, on considere que le regime permanent est atteint apres 5 constantes de temps (5*tau). Durant cette phase transitoire, l'energie est stockee ou restituee par l'element reactif (C ou L).</p>

<h3>Chapitre 3 : Representation frequentielle et diagrammes de Bode</h3>

<p>La representation frequentielle permet d'etudier le comportement d'un circuit en fonction de la frequence du signal d'entree.</p>

<h4>Fonction de transfert</h4>

<p>La fonction de transfert H(jw) est le rapport entre la tension de sortie et la tension d'entree en regime sinusoidal permanent :</p>

<pre>
H(jw) = Vs / Ve
</pre>

<p>Elle est caracterisee par :</p>
<ul>
  <li>Le <strong>module</strong> : |H(jw)| (gain)</li>
  <li>La <strong>phase</strong> : arg(H(jw)) (dephasage entre sortie et entree)</li>
</ul>

<h4>Diagramme de Bode</h4>

<p>Le diagramme de Bode represente le module et la phase de H(jw) en fonction de la frequence en echelle logarithmique :</p>

<p><strong>Gain en decibels :</strong></p>
<pre>
|H(jw)|_dB = 20 * log10(|H(jw)|)
</pre>

<p><strong>Echelle de frequence</strong> : axe horizontal en log10(f) ou log10(w)</p>

<p><strong>Conventions :</strong></p>
<ul>
  <li>Pente de +20 dB/decade pour un zero</li>
  <li>Pente de -20 dB/decade pour un pole</li>
  <li>La frequence de coupure fc est definie a -3 dB du gain maximal</li>
</ul>

<h4>Filtre passe-bas RC du premier ordre</h4>

<p><strong>Fonction de transfert :</strong></p>
<pre>
H(jw) = 1 / (1 + j*R*C*w)
       = 1 / (1 + j*w/wc)

avec wc = 1/(R*C)  et  fc = 1/(2*pi*R*C)
</pre>

<p><strong>Module :</strong></p>
<pre>
|H(jw)| = 1 / sqrt(1 + (w/wc)^2)
</pre>

<p><strong>Phase :</strong></p>
<pre>
phi(w) = -arctan(w/wc)
</pre>

<p><strong>Comportement asymptotique :</strong></p>
<ul>
  <li>Pour w &lt;&lt; wc : |H| = 1 (0 dB), phi = 0 degres</li>
  <li>Pour w = wc : |H| = 1/sqrt(2) (-3 dB), phi = -45 degres</li>
  <li>Pour w &gt;&gt; wc : |H| tend vers wc/w (-20 dB/decade), phi tend vers -90 degres</li>
</ul>

<h4>Filtre passe-haut RC du premier ordre</h4>

<p><strong>Fonction de transfert :</strong></p>
<pre>
H(jw) = j*R*C*w / (1 + j*R*C*w)
       = j*w/wc / (1 + j*w/wc)
</pre>

<p><strong>Module :</strong></p>
<pre>
|H(jw)| = (w/wc) / sqrt(1 + (w/wc)^2)
</pre>

<p><strong>Comportement asymptotique :</strong></p>
<ul>
  <li>Pour w &lt;&lt; wc : |H| tend vers w/wc (+20 dB/decade), phi tend vers +90 degres</li>
  <li>Pour w = wc : |H| = 1/sqrt(2) (-3 dB), phi = +45 degres</li>
  <li>Pour w &gt;&gt; wc : |H| = 1 (0 dB), phi = 0 degres</li>
</ul>

<h3>Chapitre 4 : Filtres passifs du second ordre (RLC)</h3>

<h4>Filtre passe-bande RLC serie</h4>

<p>Pour un circuit RLC serie, la tension aux bornes de la resistance constitue un filtre passe-bande :</p>

<p><strong>Fonction de transfert :</strong></p>
<pre>
H(jw) = (R / L) * jw / ((jw)^2 + (R/L)*jw + 1/(L*C))
</pre>

<p><strong>Parametres caracteristiques :</strong></p>
<pre>
Frequence de resonance : f0 = 1 / (2*pi*sqrt(L*C))
Pulsation de resonance : w0 = 1 / sqrt(L*C)
Facteur de qualite :     Q = (1/R) * sqrt(L/C) = L*w0/R
Bande passante :         Bp = f0 / Q = R / (2*pi*L)
</pre>

<p>Le facteur de qualite Q determine la selectivite du filtre :</p>
<ul>
  <li>Q eleve : filtre tres selectif (bande passante etroite)</li>
  <li>Q faible : filtre peu selectif (bande passante large)</li>
</ul>

<h4>Filtre passe-bas RLC serie</h4>

<p>La tension aux bornes du condensateur dans un circuit RLC serie forme un filtre passe-bas du second ordre :</p>

<p><strong>Fonction de transfert :</strong></p>
<pre>
H(jw) = 1 / (1 - (w/w0)^2 + j*(w/(Q*w0)))

avec w0 = 1/sqrt(L*C) et Q = (1/R)*sqrt(L/C)
</pre>

<p><strong>Regimes selon Q :</strong></p>
<ul>
  <li>Q &lt; 0.5 : regime sur-amorti (pas de depassement)</li>
  <li>Q = 0.5 : regime critique (reponse la plus rapide sans depassement)</li>
  <li>Q &gt; 0.5 : regime sous-amorti (oscillations amorties)</li>
</ul>

<p>A la resonance (w = w0), le gain peut etre superieur a 1 (surtension) si Q &gt; 1/sqrt(2).</p>

<h4>Filtre coupe-bande (rejecteur)</h4>

<p>Le filtre coupe-bande RLC est l'inverse du passe-bande. La tension aux bornes de l'association serie LC constitue un filtre rejecteur :</p>

<p><strong>Fonction de transfert :</strong></p>
<pre>
H(jw) = (1 - (w/w0)^2) / (1 - (w/w0)^2 + j*(w/(Q*w0)))
</pre>

<p>A la frequence de resonance w0, le gain est nul (rejection totale en theorie).</p>

<h3>Chapitre 5 : Amplificateur Operationnel (AOP)</h3>

<h4>Rappels sur l'AOP ideal</h4>

<p>L'AOP ideal est caracterise par :</p>
<ul>
  <li>Impedance d'entree infinie (courants d'entree nuls : I+ = I- = 0)</li>
  <li>Impedance de sortie nulle</li>
  <li>Gain differentiel infini en boucle ouverte</li>
  <li>Bande passante infinie</li>
</ul>

<p>En regime lineaire (avec contre-reaction negative) : V+ = V- (tension differentielle nulle).</p>

<h4>Amplificateur differentiel</h4>

<p>Le montage differentiel amplifie la difference entre deux signaux d'entree :</p>

<pre>
         R1         R2
V1 ---/\/\/\---+---/\/\/\--- Vs
               |
              (-) AOP
               |
              (+)
               |
V2 ---/\/\/\---+---/\/\/\--- GND
         R3         R4
</pre>

<p><strong>Tension de sortie :</strong></p>
<pre>
Si R1 = R3 et R2 = R4 :
Vs = (R2/R1) * (V2 - V1)

Gain differentiel : Ad = R2/R1
</pre>

<p>Le taux de rejection du mode commun (CMRR) mesure la capacite du montage a rejeter les signaux communs aux deux entrees. En pratique, il est essentiel d'apparier les resistances pour maximiser le CMRR.</p>

<h4>Amplificateur d'instrumentation</h4>

<p>L'amplificateur d'instrumentation est constitue de trois AOP et offre :</p>
<ul>
  <li>Impedance d'entree tres elevee (etage d'entree non-inverseur)</li>
  <li>Gain reglable par une seule resistance (Rg)</li>
  <li>Excellent CMRR</li>
</ul>

<p><strong>Gain :</strong></p>
<pre>
Vs = (1 + 2*R1/Rg) * (R3/R2) * (V2 - V1)
</pre>

<p>Cet amplificateur est utilise dans les chaines de mesure avec des capteurs (ponts de Wheatstone, thermocouples) ou les signaux sont faibles et differentiels.</p>

<h3>Chapitre 6 : Representation temporelle</h3>

<h4>Reponse indicielle (a un echelon)</h4>

<p>La reponse indicielle d'un systeme du second ordre depend de son amortissement :</p>

<p><strong>Cas sous-amorti (Q &gt; 0.5) :</strong></p>
<pre>
s(t) = 1 - (1/sqrt(1-xi^2)) * exp(-xi*w0*t) * sin(wd*t + phi)

avec xi = 1/(2Q) (coefficient d'amortissement)
     wd = w0*sqrt(1 - xi^2) (pulsation des oscillations amorties)
     phi = arccos(xi)
</pre>

<p><strong>Parametres de la reponse indicielle :</strong></p>
<ul>
  <li>Temps de montee (tr) : temps pour passer de 10% a 90% de la valeur finale</li>
  <li>Depassement (D%) : amplitude du premier depassement en pourcentage</li>
  <li>Temps de reponse a 5% (t5%) : temps pour rester dans une bande de +/- 5% de la valeur finale</li>
</ul>

<h4>Reponse impulsionnelle</h4>

<p>La reponse impulsionnelle h(t) est la derivee de la reponse indicielle. Elle est fondamentale pour l'analyse des systemes lineaires car la sortie d'un systeme est le produit de convolution de l'entree par h(t).</p>

<h3>Chapitre 7 : Modulation d'amplitude (AM)</h3>

<h4>Principe de la modulation AM</h4>

<p>La modulation d'amplitude consiste a faire varier l'amplitude d'une porteuse haute frequence en fonction d'un signal modulant basse frequence.</p>

<p><strong>Signal module AM :</strong></p>
<pre>
s(t) = A * [1 + m * cos(2*pi*fm*t)] * cos(2*pi*fc*t)
</pre>

<p>Ou :</p>
<ul>
  <li>A : amplitude de la porteuse</li>
  <li>m : indice de modulation (0 &lt; m &lt;= 1 pour eviter la surmodulation)</li>
  <li>fm : frequence du signal modulant</li>
  <li>fc : frequence de la porteuse (fc &gt;&gt; fm)</li>
</ul>

<h4>Spectre du signal AM</h4>

<p>Le spectre du signal AM est compose de trois raies :</p>
<ul>
  <li>La porteuse a fc avec une amplitude A</li>
  <li>La bande laterale superieure a (fc + fm) avec une amplitude m*A/2</li>
  <li>La bande laterale inferieure a (fc - fm) avec une amplitude m*A/2</li>
</ul>

<p><strong>Bande passante du signal AM :</strong></p>
<pre>
B = 2 * fm
</pre>

<h4>Indice de modulation</h4>

<p>L'indice de modulation m determine la profondeur de la modulation :</p>
<pre>
m = Amax - Amin / (Amax + Amin)
</pre>

<p>Ou Amax et Amin sont les amplitudes maximale et minimale de l'enveloppe du signal module.</p>

<ul>
  <li>Si m &lt; 1 : modulation correcte, l'enveloppe reproduit fidelement le signal modulant</li>
  <li>Si m = 1 : modulation a 100%, l'enveloppe touche zero</li>
  <li>Si m &gt; 1 : surmodulation, distorsion du signal (a eviter)</li>
</ul>

<h4>Puissance du signal AM</h4>

<pre>
Puissance totale : Pt = Pc * (1 + m^2/2)
Puissance porteuse : Pc = A^2 / 2
Rendement : eta = m^2 / (2 + m^2)
</pre>

<p>Le rendement maximal est de 33% pour m = 1, ce qui signifie que les deux tiers de la puissance sont gaspilles dans la porteuse. C'est un inconvenient majeur de la modulation AM classique.</p>

<h4>Demodulation par detection d'enveloppe</h4>

<p>La detection d'enveloppe est la methode la plus simple de demodulation AM :</p>
<ol>
  <li>Le signal AM est redresse par une diode (demi-onde ou onde complete)</li>
  <li>Un filtre RC passe-bas extrait l'enveloppe du signal</li>
  <li>Un condensateur de liaison supprime la composante continue</li>
</ol>

<p><strong>Condition de bon fonctionnement du detecteur d'enveloppe :</strong></p>
<pre>
1/fc &lt;&lt; R*C &lt;&lt; 1/fm
</pre>

<p>Le circuit RC doit etre assez rapide pour suivre les variations de l'enveloppe (fm) mais assez lent pour lisser les oscillations de la porteuse (fc).</p>

<h3>Travaux diriges et exercices pratiques</h3>

<p>Les TD du cours de SE S2 couvrent l'ensemble des chapitres avec des exercices progressifs :</p>

<ul>
  <li><strong>TD1</strong> : Calculs de matrices de quadripoles, mise en cascade</li>
  <li><strong>TD2</strong> : Circuits RC et RL du premier ordre, calculs de constantes de temps</li>
  <li><strong>TD8-TD10</strong> : Exercices avances sur les filtres, la modulation et l'AOP</li>
</ul>

<p>Chaque TD comprend des exercices de calcul suivis d'applications pratiques et de verifications par simulation.</p>

<hr/>

<h2>PART D : ANALYSE ET REFLEXION</h2>

<h3>Competences acquises</h3>

<ul>
  <li>Capacite a analyser un circuit electronique dans le domaine frequentiel</li>
  <li>Maitrise des diagrammes de Bode pour la caracterisation de systemes</li>
  <li>Comprehension des filtres passifs et de leur dimensionnement</li>
  <li>Connaissance des principes de modulation/demodulation AM</li>
  <li>Utilisation des quadripoles pour l'analyse de circuits complexes</li>
  <li>Comprehension du lien entre representations temporelle et frequentielle</li>
</ul>

<h3>Points forts du cours</h3>

<p>Le cours de SE S2 offre une progression pedagogique bien construite : il part des outils mathematiques (quadripoles, fonctions de transfert) pour arriver aux applications concretes (filtres, modulation). La combinaison theorie/TD/TL permet une assimilation solide des concepts. L'etude de la modulation AM introduit le domaine des telecommunications, un atout pour les semestres suivants.</p>

<h3>Difficultes rencontrees</h3>

<p>Les diagrammes de Bode et le passage entre domaines temporel et frequentiel ont necessite un temps d'adaptation. La rigueur mathematique requise (nombres complexes, logarithmes, exponentielles) est significative. La situation sanitaire a rendu certains TP de laboratoire plus difficiles a realiser, mais les simulations LTspice ont permis de compenser en partie.</p>

<h3>Connexions interdisciplinaires</h3>

<ul>
  <li><strong>Mathematiques S2</strong> : Les transformees de Laplace et les nombres complexes sont les outils fondamentaux de l'analyse frequentielle</li>
  <li><strong>TL S2</strong> : Les travaux de laboratoire mettent en pratique les concepts de SE (filtres, Bode, modulation)</li>
  <li><strong>Signal S3</strong> : Les bases acquises en SE S2 preparent directement au cours de traitement du signal</li>
  <li><strong>Electronique S3-S5</strong> : Les filtres actifs et les amplificateurs seront approfondis dans les semestres suivants</li>
</ul>

<h3>Auto-evaluation</h3>

<p>Ce cours a ete l'un des plus exigeants du semestre en termes de rigueur mathematique, mais aussi l'un des plus formateurs. La capacite a "lire" un diagramme de Bode et a en deduire le comportement d'un circuit est une competence fondamentale que j'utilise regulierement dans les cours suivants. La modulation AM, bien que classique, a ouvert les portes de la comprehension des systemes de telecommunications.</p>

<hr/>

<h2>Documents de Cours</h2>

<h3>Cours - Chapitres</h3>

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

<h3>Travaux Diriges</h3>

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

</div>

<div class="lang-en">

<h1>Electronic Systems (SE) - S2</h1>

<p><strong>Year</strong>: 2020-2021 | <strong>Semester</strong>: 2 | <strong>Type</strong>: Electronics</p>

<hr/>

<h2>PART A: GENERAL OVERVIEW</h2>

<h3>Context and objectives</h3>

<p>The Electronic Systems course in semester 2 covers the analysis of electronic systems from both frequency-domain and time-domain perspectives. It introduces the mathematical tools and analysis methods needed to understand and design analog electronic circuits. The curriculum is structured around 7 chapters, ranging from two-port networks to operational amplifier applications, including passive filters and amplitude modulation.</p>

<p><strong>Learning objectives:</strong></p>
<ul>
  <li>Analyze four-terminal networks (two-port networks) using impedance and admittance matrices</li>
  <li>Study the transient response of first-order circuits (RC, RL)</li>
  <li>Master frequency-domain representation (Bode diagrams) and time-domain representation of systems</li>
  <li>Design and size passive filters (low-pass, high-pass, band-pass)</li>
  <li>Understand the principles of amplitude modulation (AM)</li>
  <li>Apply operational amplifiers in advanced configurations</li>
</ul>

<h3>Course organization</h3>

<p>The course is organized into 7 chapters following a logical progression:</p>
<ol>
  <li><strong>Chapter 1</strong>: Two-port networks (four-terminal networks)</li>
  <li><strong>Chapter 3</strong>: First-order circuits (low-pass, high-pass)</li>
  <li><strong>Chapter 4</strong>: Passive filters and frequency response</li>
  <li><strong>Chapter 5</strong>: Operational amplifier (op-amp) - advanced applications</li>
  <li><strong>Chapter 6</strong>: Time-domain and frequency-domain representation</li>
  <li><strong>Chapter 7</strong>: Amplitude modulation (AM)</li>
  <li><strong>Tutorials and exercises</strong>: Tutorial booklets for practical application</li>
</ol>

<h3>Target competencies (BUT GEII)</h3>

<p>This module contributes to the "Electronics and Systems" competency block:</p>
<ul>
  <li>Analyze the frequency-domain behavior of a circuit</li>
  <li>Design passive analog filters</li>
  <li>Use Bode diagrams to characterize a system</li>
  <li>Understand modulation principles for telecommunications</li>
</ul>

<hr/>

<h2>PART B: EXPERIENCE AND CONTEXT</h2>

<h3>Educational environment</h3>

<p>Electronic Systems teaching takes the form of lectures, tutorials (TD), and laboratory work (TL). Tutorials allow students to practice theoretical concepts through calculations, while lab sessions offer direct interaction with real circuits on the IUT measurement benches.</p>

<h3>Semester progression</h3>

<p>The semester was marked by the health situation (2020-2021), with alternating in-person and remote classes. Tutorials were partly conducted remotely, with detailed tutorial booklets provided by the instructors. Lab sessions were maintained in person as much as possible to allow hands-on use of measurement instruments.</p>

<h3>Tools and instruments used</h3>

<ul>
  <li><strong>Digital oscilloscope</strong>: Visualization of time-domain signals, phase shift and amplitude measurements</li>
  <li><strong>Function generator</strong>: Generation of sinusoidal, square, and triangular signals for testing</li>
  <li><strong>Precision multimeter</strong>: Voltage, current, and impedance measurements</li>
  <li><strong>LTspice</strong>: Analog circuit simulation for calculation verification</li>
  <li><strong>Scientific calculator</strong>: Transfer function calculations, dB conversion</li>
</ul>

<h3>Links with other courses</h3>

<ul>
  <li><strong>Mathematics S2</strong>: Complex numbers, Laplace transforms, differential equations</li>
  <li><strong>OL (Software Tools)</strong>: Laplace transform, Fourier series</li>
  <li><strong>TL (Laboratory Work)</strong>: Practical implementation on real circuits</li>
  <li><strong>Energy</strong>: Three-phase circuits and power</li>
  <li><strong>Programming S3+</strong>: Numerical simulation of filters</li>
</ul>

<hr/>

<h2>PART C: TECHNICAL ASPECTS</h2>

<h3>Chapter 1: Two-Port Networks (Four-Terminal Networks)</h3>

<p>A two-port network is an electrical network with two ports (four terminals): an input port and an output port. It is characterized by the relationships between the input and output voltages and currents.</p>

<h4>Impedance and admittance matrices</h4>

<p>The <strong>impedance matrix [Z]</strong> relates voltages to currents:</p>

<pre>
| V1 |   | Z11  Z12 |   | I1 |
|    | = |          | x |    |
| V2 |   | Z21  Z22 |   | I2 |
</pre>

<p>Where:</p>
<ul>
  <li>Z11 = V1/I1 (when I2 = 0): open-circuit input impedance</li>
  <li>Z22 = V2/I2 (when I1 = 0): open-circuit output impedance</li>
  <li>Z12 = V1/I2 (when I1 = 0): reverse transfer impedance</li>
  <li>Z21 = V2/I1 (when I2 = 0): forward transfer impedance</li>
</ul>

<p>The <strong>admittance matrix [Y]</strong> is the inverse of the impedance matrix:</p>

<pre>
| I1 |   | Y11  Y12 |   | V1 |
|    | = |          | x |    |
| I2 |   | Y21  Y22 |   | V2 |

with [Y] = [Z]^(-1)
</pre>

<h4>Chain matrix (ABCD)</h4>

<p>For cascading two-port networks, the chain matrix is used:</p>

<pre>
| V1 |   | A  B |   |  V2 |
|    | = |      | x |     |
| I1 |   | C  D |   | -I2 |
</pre>

<p>The advantage of this representation is that cascading two networks simply requires multiplying their matrices:</p>

<pre>
[T_total] = [T1] x [T2]
</pre>

<h4>ABCD matrix examples for simple elements</h4>

<p>For a <strong>series impedance Z</strong>:</p>
<pre>
| A  B |   | 1  Z |
|      | = |      |
| C  D |   | 0  1 |
</pre>

<p>For a <strong>parallel admittance Y</strong>:</p>
<pre>
| A  B |   | 1  0 |
|      | = |      |
| C  D |   | Y  1 |
</pre>

<h3>Chapter 2: First-Order Circuits</h3>

<p>First-order circuits contain a single reactive element (capacitor C or inductor L) combined with resistances.</p>

<h4>Series RC circuit - Step response</h4>

<p>For a series RC circuit subjected to a voltage step E:</p>

<p><strong>Differential equation:</strong></p>
<pre>
RC * dVc/dt + Vc = E
</pre>

<p><strong>Solution (capacitor charging):</strong></p>
<pre>
Vc(t) = E * (1 - exp(-t / tau))

with tau = RC  (time constant)
</pre>

<p><strong>Solution (capacitor discharging):</strong></p>
<pre>
Vc(t) = E * exp(-t / tau)
</pre>

<p>The time constant tau = RC determines the response speed:</p>
<ul>
  <li>At t = tau: Vc reaches 63.2% of the final value</li>
  <li>At t = 3*tau: Vc reaches 95% of the final value</li>
  <li>At t = 5*tau: Vc reaches 99.3% of the final value (steady state)</li>
</ul>

<h4>Series RL circuit - Step response</h4>

<p>For a series RL circuit subjected to a voltage step E:</p>

<p><strong>Differential equation:</strong></p>
<pre>
L * dI/dt + R * I = E
</pre>

<p><strong>Solution:</strong></p>
<pre>
I(t) = (E/R) * (1 - exp(-t / tau))

with tau = L/R  (time constant)
</pre>

<h4>Transient and steady-state regimes</h4>

<p>The transient regime corresponds to the phase during which the circuit evolves toward its equilibrium state. In practice, steady state is considered reached after 5 time constants (5*tau). During this transient phase, energy is stored or released by the reactive element (C or L).</p>

<h3>Chapter 3: Frequency Representation and Bode Diagrams</h3>

<p>Frequency representation allows studying the behavior of a circuit as a function of the input signal frequency.</p>

<h4>Transfer function</h4>

<p>The transfer function H(jw) is the ratio of the output voltage to the input voltage in sinusoidal steady state:</p>

<pre>
H(jw) = Vs / Ve
</pre>

<p>It is characterized by:</p>
<ul>
  <li>The <strong>magnitude</strong>: |H(jw)| (gain)</li>
  <li>The <strong>phase</strong>: arg(H(jw)) (phase shift between output and input)</li>
</ul>

<h4>Bode diagram</h4>

<p>The Bode diagram represents the magnitude and phase of H(jw) as a function of frequency on a logarithmic scale:</p>

<p><strong>Gain in decibels:</strong></p>
<pre>
|H(jw)|_dB = 20 * log10(|H(jw)|)
</pre>

<p><strong>Frequency scale</strong>: horizontal axis in log10(f) or log10(w)</p>

<p><strong>Conventions:</strong></p>
<ul>
  <li>Slope of +20 dB/decade for a zero</li>
  <li>Slope of -20 dB/decade for a pole</li>
  <li>The cutoff frequency fc is defined at -3 dB from the maximum gain</li>
</ul>

<h4>First-order RC low-pass filter</h4>

<p><strong>Transfer function:</strong></p>
<pre>
H(jw) = 1 / (1 + j*R*C*w)
       = 1 / (1 + j*w/wc)

with wc = 1/(R*C)  and  fc = 1/(2*pi*R*C)
</pre>

<p><strong>Magnitude:</strong></p>
<pre>
|H(jw)| = 1 / sqrt(1 + (w/wc)^2)
</pre>

<p><strong>Phase:</strong></p>
<pre>
phi(w) = -arctan(w/wc)
</pre>

<p><strong>Asymptotic behavior:</strong></p>
<ul>
  <li>For w &lt;&lt; wc: |H| = 1 (0 dB), phi = 0 degrees</li>
  <li>For w = wc: |H| = 1/sqrt(2) (-3 dB), phi = -45 degrees</li>
  <li>For w &gt;&gt; wc: |H| tends toward wc/w (-20 dB/decade), phi tends toward -90 degrees</li>
</ul>

<h4>First-order RC high-pass filter</h4>

<p><strong>Transfer function:</strong></p>
<pre>
H(jw) = j*R*C*w / (1 + j*R*C*w)
       = j*w/wc / (1 + j*w/wc)
</pre>

<p><strong>Magnitude:</strong></p>
<pre>
|H(jw)| = (w/wc) / sqrt(1 + (w/wc)^2)
</pre>

<p><strong>Asymptotic behavior:</strong></p>
<ul>
  <li>For w &lt;&lt; wc: |H| tends toward w/wc (+20 dB/decade), phi tends toward +90 degrees</li>
  <li>For w = wc: |H| = 1/sqrt(2) (-3 dB), phi = +45 degrees</li>
  <li>For w &gt;&gt; wc: |H| = 1 (0 dB), phi = 0 degrees</li>
</ul>

<h3>Chapter 4: Second-Order Passive Filters (RLC)</h3>

<h4>Series RLC band-pass filter</h4>

<p>For a series RLC circuit, the voltage across the resistance forms a band-pass filter:</p>

<p><strong>Transfer function:</strong></p>
<pre>
H(jw) = (R / L) * jw / ((jw)^2 + (R/L)*jw + 1/(L*C))
</pre>

<p><strong>Characteristic parameters:</strong></p>
<pre>
Resonant frequency:  f0 = 1 / (2*pi*sqrt(L*C))
Resonant pulsation:  w0 = 1 / sqrt(L*C)
Quality factor:      Q = (1/R) * sqrt(L/C) = L*w0/R
Bandwidth:           Bp = f0 / Q = R / (2*pi*L)
</pre>

<p>The quality factor Q determines the filter selectivity:</p>
<ul>
  <li>High Q: highly selective filter (narrow bandwidth)</li>
  <li>Low Q: less selective filter (wide bandwidth)</li>
</ul>

<h4>Series RLC low-pass filter</h4>

<p>The voltage across the capacitor in a series RLC circuit forms a second-order low-pass filter:</p>

<p><strong>Transfer function:</strong></p>
<pre>
H(jw) = 1 / (1 - (w/w0)^2 + j*(w/(Q*w0)))

with w0 = 1/sqrt(L*C) and Q = (1/R)*sqrt(L/C)
</pre>

<p><strong>Regimes depending on Q:</strong></p>
<ul>
  <li>Q &lt; 0.5: overdamped regime (no overshoot)</li>
  <li>Q = 0.5: critically damped regime (fastest response without overshoot)</li>
  <li>Q &gt; 0.5: underdamped regime (damped oscillations)</li>
</ul>

<p>At resonance (w = w0), the gain can be greater than 1 (overvoltage) if Q &gt; 1/sqrt(2).</p>

<h4>Band-reject filter (notch)</h4>

<p>The RLC band-reject filter is the inverse of the band-pass filter. The voltage across the series LC combination forms a notch filter:</p>

<p><strong>Transfer function:</strong></p>
<pre>
H(jw) = (1 - (w/w0)^2) / (1 - (w/w0)^2 + j*(w/(Q*w0)))
</pre>

<p>At the resonant frequency w0, the gain is zero (total rejection in theory).</p>

<h3>Chapter 5: Operational Amplifier (Op-Amp)</h3>

<h4>Ideal op-amp review</h4>

<p>The ideal op-amp is characterized by:</p>
<ul>
  <li>Infinite input impedance (zero input currents: I+ = I- = 0)</li>
  <li>Zero output impedance</li>
  <li>Infinite open-loop differential gain</li>
  <li>Infinite bandwidth</li>
</ul>

<p>In linear mode (with negative feedback): V+ = V- (zero differential voltage).</p>

<h4>Differential amplifier</h4>

<p>The differential configuration amplifies the difference between two input signals:</p>

<pre>
         R1         R2
V1 ---/\/\/\---+---/\/\/\--- Vs
               |
              (-) Op-Amp
               |
              (+)
               |
V2 ---/\/\/\---+---/\/\/\--- GND
         R3         R4
</pre>

<p><strong>Output voltage:</strong></p>
<pre>
If R1 = R3 and R2 = R4:
Vs = (R2/R1) * (V2 - V1)

Differential gain: Ad = R2/R1
</pre>

<p>The common-mode rejection ratio (CMRR) measures the circuit's ability to reject signals common to both inputs. In practice, it is essential to match the resistors to maximize the CMRR.</p>

<h4>Instrumentation amplifier</h4>

<p>The instrumentation amplifier consists of three op-amps and offers:</p>
<ul>
  <li>Very high input impedance (non-inverting input stage)</li>
  <li>Gain adjustable by a single resistor (Rg)</li>
  <li>Excellent CMRR</li>
</ul>

<p><strong>Gain:</strong></p>
<pre>
Vs = (1 + 2*R1/Rg) * (R3/R2) * (V2 - V1)
</pre>

<p>This amplifier is used in measurement chains with sensors (Wheatstone bridges, thermocouples) where signals are weak and differential.</p>

<h3>Chapter 6: Time-Domain Representation</h3>

<h4>Step response</h4>

<p>The step response of a second-order system depends on its damping:</p>

<p><strong>Underdamped case (Q &gt; 0.5):</strong></p>
<pre>
s(t) = 1 - (1/sqrt(1-xi^2)) * exp(-xi*w0*t) * sin(wd*t + phi)

with xi = 1/(2Q) (damping ratio)
     wd = w0*sqrt(1 - xi^2) (damped oscillation frequency)
     phi = arccos(xi)
</pre>

<p><strong>Step response parameters:</strong></p>
<ul>
  <li>Rise time (tr): time to go from 10% to 90% of the final value</li>
  <li>Overshoot (D%): amplitude of the first overshoot as a percentage</li>
  <li>5% settling time (t5%): time to stay within a +/- 5% band of the final value</li>
</ul>

<h4>Impulse response</h4>

<p>The impulse response h(t) is the derivative of the step response. It is fundamental for linear systems analysis because a system's output is the convolution product of the input with h(t).</p>

<h3>Chapter 7: Amplitude Modulation (AM)</h3>

<h4>AM modulation principle</h4>

<p>Amplitude modulation consists of varying the amplitude of a high-frequency carrier according to a low-frequency modulating signal.</p>

<p><strong>AM modulated signal:</strong></p>
<pre>
s(t) = A * [1 + m * cos(2*pi*fm*t)] * cos(2*pi*fc*t)
</pre>

<p>Where:</p>
<ul>
  <li>A: carrier amplitude</li>
  <li>m: modulation index (0 &lt; m &lt;= 1 to avoid overmodulation)</li>
  <li>fm: modulating signal frequency</li>
  <li>fc: carrier frequency (fc &gt;&gt; fm)</li>
</ul>

<h4>AM signal spectrum</h4>

<p>The AM signal spectrum consists of three spectral lines:</p>
<ul>
  <li>The carrier at fc with amplitude A</li>
  <li>The upper sideband at (fc + fm) with amplitude m*A/2</li>
  <li>The lower sideband at (fc - fm) with amplitude m*A/2</li>
</ul>

<p><strong>AM signal bandwidth:</strong></p>
<pre>
B = 2 * fm
</pre>

<h4>Modulation index</h4>

<p>The modulation index m determines the depth of modulation:</p>
<pre>
m = Amax - Amin / (Amax + Amin)
</pre>

<p>Where Amax and Amin are the maximum and minimum amplitudes of the modulated signal envelope.</p>

<ul>
  <li>If m &lt; 1: correct modulation, the envelope faithfully reproduces the modulating signal</li>
  <li>If m = 1: 100% modulation, the envelope touches zero</li>
  <li>If m &gt; 1: overmodulation, signal distortion (to be avoided)</li>
</ul>

<h4>AM signal power</h4>

<pre>
Total power:   Pt = Pc * (1 + m^2/2)
Carrier power: Pc = A^2 / 2
Efficiency:    eta = m^2 / (2 + m^2)
</pre>

<p>The maximum efficiency is 33% for m = 1, meaning that two-thirds of the power is wasted in the carrier. This is a major drawback of conventional AM modulation.</p>

<h4>Envelope detection demodulation</h4>

<p>Envelope detection is the simplest AM demodulation method:</p>
<ol>
  <li>The AM signal is rectified by a diode (half-wave or full-wave)</li>
  <li>An RC low-pass filter extracts the signal envelope</li>
  <li>A coupling capacitor removes the DC component</li>
</ol>

<p><strong>Envelope detector operating condition:</strong></p>
<pre>
1/fc &lt;&lt; R*C &lt;&lt; 1/fm
</pre>

<p>The RC circuit must be fast enough to follow the envelope variations (fm) but slow enough to smooth out the carrier oscillations (fc).</p>

<h3>Tutorials and practical exercises</h3>

<p>The SE S2 tutorials cover all chapters with progressive exercises:</p>

<ul>
  <li><strong>TD1</strong>: Two-port network matrix calculations, cascading</li>
  <li><strong>TD2</strong>: First-order RC and RL circuits, time constant calculations</li>
  <li><strong>TD8-TD10</strong>: Advanced exercises on filters, modulation, and op-amp</li>
</ul>

<p>Each tutorial includes calculation exercises followed by practical applications and simulation verifications.</p>

<hr/>

<h2>PART D: ANALYSIS AND REFLECTION</h2>

<h3>Skills acquired</h3>

<ul>
  <li>Ability to analyze an electronic circuit in the frequency domain</li>
  <li>Mastery of Bode diagrams for system characterization</li>
  <li>Understanding of passive filters and their sizing</li>
  <li>Knowledge of AM modulation/demodulation principles</li>
  <li>Use of two-port networks for complex circuit analysis</li>
  <li>Understanding of the link between time-domain and frequency-domain representations</li>
</ul>

<h3>Course strengths</h3>

<p>The SE S2 course offers a well-structured pedagogical progression: it starts from mathematical tools (two-port networks, transfer functions) and arrives at concrete applications (filters, modulation). The combination of theory/tutorials/labs enables solid concept assimilation. The study of AM modulation introduces the field of telecommunications, an asset for subsequent semesters.</p>

<h3>Difficulties encountered</h3>

<p>Bode diagrams and the transition between time and frequency domains required an adaptation period. The mathematical rigor required (complex numbers, logarithms, exponentials) is significant. The health situation made some laboratory sessions more difficult to carry out, but LTspice simulations partially compensated for this.</p>

<h3>Interdisciplinary connections</h3>

<ul>
  <li><strong>Mathematics S2</strong>: Laplace transforms and complex numbers are the fundamental tools of frequency analysis</li>
  <li><strong>TL S2</strong>: Laboratory work puts SE concepts into practice (filters, Bode, modulation)</li>
  <li><strong>Signal S3</strong>: The foundations acquired in SE S2 directly prepare for the signal processing course</li>
  <li><strong>Electronics S3-S5</strong>: Active filters and amplifiers will be explored in depth in subsequent semesters</li>
</ul>

<h3>Self-assessment</h3>

<p>This course was one of the most demanding of the semester in terms of mathematical rigor, but also one of the most formative. The ability to "read" a Bode diagram and deduce a circuit's behavior from it is a fundamental skill that I regularly use in subsequent courses. AM modulation, although classical, opened the door to understanding telecommunications systems.</p>

<hr/>

<h2>Course Documents</h2>

<h3>Lectures - Chapters</h3>

<div class="pdf-item">
  <h4>Chapter 1: Two-Port Networks</h4>
  <p>Lecture notes on two-port networks: impedance, admittance, hybrid, and chain matrices. Cascading of two-port networks and applications to electronic circuits.</p>
  <embed src="/cours-pdf/S2/SE/Chap1_Polycopie_cours_quadripoles.pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/cours-pdf/S2/SE/Chap1_Polycopie_cours_quadripoles.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Download PDF</a>
  </p>
</div>

<div class="pdf-item">
  <h4>Chapter 3: First-Order Circuits - Low-Pass and High-Pass</h4>
  <p>Study of first-order RC and RL circuits: time-domain response, time constant, transfer functions, and Bode diagrams for low-pass and high-pass filters.</p>
  <embed src="/cours-pdf/S2/SE/chap3_circuits_premier_ordre_passe_bas_passe_haut.pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/cours-pdf/S2/SE/chap3_circuits_premier_ordre_passe_bas_passe_haut.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Download PDF</a>
  </p>
</div>

<div class="pdf-item">
  <h4>Chapter 4: Passive Filters and Frequency Response</h4>
  <p>In-depth study of passive filters: second-order RLC filters, quality factor, resonant frequency, bandwidth, and selectivity.</p>
  <embed src="/cours-pdf/S2/SE/CHAP4_2021.pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/cours-pdf/S2/SE/CHAP4_2021.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Download PDF</a>
  </p>
</div>

<div class="pdf-item">
  <h4>Chapter 5: Operational Amplifier - Advanced Applications</h4>
  <p>Op-amp applications: differential amplifier, instrumentation amplifier, nonlinear configurations, and signal conditioning applications.</p>
  <embed src="/cours-pdf/S2/SE/Chap5_SE.pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/cours-pdf/S2/SE/Chap5_SE.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Download PDF</a>
  </p>
</div>

<div class="pdf-item">
  <h4>Chapter 6: Time-Domain and Frequency-Domain Representation</h4>
  <p>Links between time and frequency domains: step response, impulse response, Fourier transform, and spectral analysis of systems.</p>
  <embed src="/cours-pdf/S2/SE/Chap6_Representation-temporelle-frequentielle.pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/cours-pdf/S2/SE/Chap6_Representation-temporelle-frequentielle.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Download PDF</a>
  </p>
</div>

<div class="pdf-item">
  <h4>Chapter 7: Amplitude Modulation (AM)</h4>
  <p>AM modulation principles: modulated signal, spectrum, modulation index, power, envelope detection demodulation. Radio communication applications.</p>
  <embed src="/cours-pdf/S2/SE/Chap7_modulation_AM.pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/cours-pdf/S2/SE/Chap7_modulation_AM.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Download PDF</a>
  </p>
</div>

<h3>Tutorials</h3>

<div class="pdf-item">
  <h4>TD1: Exercises on two-port networks and basic circuits</h4>
  <p>First tutorial booklet: exercises on two-port networks, matrix calculations, and first-order circuits.</p>
  <embed src="/cours-pdf/S2/SE/TD1_(en_2_seances).pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/cours-pdf/S2/SE/TD1_(en_2_seances).pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Download PDF</a>
  </p>
</div>

<div class="pdf-item">
  <h4>TD2: Exercises on filters and frequency response</h4>
  <p>Second tutorial booklet: exercises on low-pass filters, high-pass filters, Bode diagrams, and transfer functions.</p>
  <embed src="/cours-pdf/S2/SE/TD2.pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/cours-pdf/S2/SE/TD2.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Download PDF</a>
  </p>
</div>

<div class="pdf-item">
  <h4>Complete TD Booklet (M. Bourennane)</h4>
  <p>Complete tutorial booklet covering the entire SE S2 curriculum, with corrected exercises and applications.</p>
  <embed src="/cours-pdf/S2/SE/Fascicule_TD_BOURENNANE_2020_2021.pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/cours-pdf/S2/SE/Fascicule_TD_BOURENNANE_2020_2021.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Download PDF</a>
  </p>
</div>

<div class="pdf-item">
  <h4>TD8 to TD10: Advanced Exercises</h4>
  <p>Advanced tutorial booklet covering AM modulation, instrumentation amplifiers, and synthesis applications.</p>
  <embed src="/cours-pdf/S2/SE/fascicule_TD8_a_TD10_SE_S2_2021.pdf" type="application/pdf" width="100%" height="800px" />
  <p style="text-align: center; margin-top: 10px;">
    <a href="/cours-pdf/S2/SE/fascicule_TD8_a_TD10_SE_S2_2021.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Download PDF</a>
  </p>
</div>

</div>

<style>body{font-family:Arial,sans-serif;background-color:#f4f4f9;color:#333;line-height:1.6}h2,h3,h4,h5{color:#2a7ae2}p{text-align:justify}code{background-color:#f5f5f5;padding:2px 6px;border-radius:3px;font-family:'Courier New',monospace}pre{background-color:#f5f5f5;padding:15px;border-radius:5px;overflow-x:auto}</style>

<div class="back-nav">
  <a href="./my-courses-2020-2021.html" data-i18n-html="back_courses_2020_2021">&larr; Retour a Mes Cours 2020-2021</a>
</div>

---
layout: default
title: "Systèmes Multivariables - S7"
date: 2024-10-02 10:56:03 +0200
---

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
    body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f9;
        color: #333;
        line-height: 1.6;
    }
    h2, h3, h4 {
        color: #007BFF;
    }
    p {
        text-align: justify;
    }
</style>

<div class="back-nav">
    <a href="./my-courses-2023-2024.html" data-i18n-html="back_courses_2023_2024">&#8592; Back to My Courses 2023-2024</a>
</div>

<div class="lang-fr">

<h1>Systemes Multivariables</h1>

<h2>PART A : GENERALITES</h2>

<h3>Presentation</h3>
<p>Le cours "Systemes Multivariables" etend l'analyse et la commande des systemes dynamiques au cas de systemes a plusieurs entrees et plusieurs sorties (MIMO - Multiple Input Multiple Output). Ce cours est essentiel pour traiter des systemes complexes reels qui ne peuvent etre reduits a une seule entree et une seule sortie.</p>

<p><strong>Annee Academique</strong> : 2023-2024<br/>
<strong>Semestre</strong> : 7<br/>
<strong>Categorie</strong> : Automatique / Commande</p>

<hr/>

<h2>PART B : PARTIE DESCRIPTIVE</h2>

<h3>Details de l'Experience</h3>

<h4>Environnement et Contexte</h4>
<p>Le cours combinait developpements theoriques avances (algebre lineaire, analyse matricielle) avec des applications pratiques via Matlab/Simulink. Nous avons etudie des systemes reels multivariables (avions, robots, procedes industriels) pour comprendre les defis specifiques de leur analyse et commande.</p>

<h4>Ma Fonction</h4>
<p>Dans ce cours, j'ai ete responsable de :</p>
<ul>
  <li>Modeliser des systemes MIMO par representation d'etat</li>
  <li>Analyser la commandabilite et l'observabilite</li>
  <li>Concevoir des lois de commande multivariables</li>
  <li>Utiliser des techniques de decouplage</li>
  <li>Implementer des observateurs d'etat</li>
  <li>Simuler des systemes multivariables sous Matlab</li>
  <li>Valider les performances et la robustesse</li>
</ul>

<h2>PART C : PARTIE TECHNIQUE</h2>

<p>Cette section explore les aspects techniques des systemes multivariables.</p>

<h3>Concepts Techniques Appris</h3>

<h4>1. Representation d'Etat</h4>

<p><strong>Forme generale</strong> :</p>
<div class="code-block">
x&#775;(t) = A&middot;x(t) + B&middot;u(t)<br/>
y(t) = C&middot;x(t) + D&middot;u(t)<br/><br/>
ou :<br/>
- x &isin; R^n : vecteur d'etat (n variables d'etat)<br/>
- u &isin; R^m : vecteur d'entree (m entrees)<br/>
- y &isin; R^p : vecteur de sortie (p sorties)<br/>
- A &isin; R^(n&times;n) : matrice d'evolution<br/>
- B &isin; R^(n&times;m) : matrice de commande<br/>
- C &isin; R^(p&times;n) : matrice d'observation<br/>
- D &isin; R^(p&times;m) : matrice de transmission directe
</div>

<p><strong>Avantages de la representation d'etat</strong> :</p>
<ul>
  <li>Traitement naturel des systemes MIMO</li>
  <li>Acces a toutes les variables internes</li>
  <li>Facilite l'analyse des proprietes structurelles</li>
  <li>Base pour commande moderne</li>
</ul>

<p><strong>Passage fonction de transfert &harr; representation d'etat</strong> :</p>
<ul>
  <li>Matricielle pour MIMO</li>
  <li>Multiple realisations possibles (commandable, observable, equilibree)</li>
</ul>

<h4>2. Matrice de Transfert</h4>

<p><strong>Definition</strong> :</p>
<div class="code-block">
G(s) = C(sI - A)^(-1)B + D<br/><br/>
G(s) est une matrice p&times;m de fonctions de transfert :<br/><br/>
G(s) = | G11(s)  G12(s)  ...  G1m(s) |<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| G21(s)  G22(s)  ...  G2m(s) |<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|  ...     ...    ...   ...   |<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Gp1(s)  Gp2(s)  ...  Gpm(s) |<br/><br/>
Gij(s) = Yi(s)/Uj(s) quand toutes les autres entrees sont nulles
</div>

<p><strong>Poles et Zeros</strong> :</p>
<ul>
  <li><strong>Poles</strong> : valeurs propres de A (racines de det(sI-A))</li>
  <li><strong>Zeros de transmission</strong> : annulent certains Gij(s)</li>
  <li>Plus complexe que SISO (zeros dependent de la direction)</li>
</ul>

<h4>3. Commandabilite</h4>

<p><strong>Definition</strong> :</p>
<p>Un systeme est commandable si on peut amener l'etat d'une condition initiale quelconque a n'importe quel etat final en temps fini.</p>

<p><strong>Critere de Kalman</strong> :</p>
<div class="code-block">
rang(Mc) = n<br/><br/>
ou Mc = [B  AB  A&sup2;B  ...  A^(n-1)B]<br/>
Mc &isin; R^(n&times;nm) : matrice de commandabilite
</div>

<p><strong>Interpretation</strong> :</p>
<ul>
  <li>Si commandable : on peut placer les poles en boucle fermee ou on veut</li>
  <li>Si non commandable : certains modes ne peuvent etre influences</li>
  <li>Decomposition de Kalman : partie commandable / non commandable</li>
</ul>

<p><strong>Commandabilite de sortie</strong> :</p>
<p>Peut-on commander specifiquement les sorties ?</p>
<div class="code-block">
rang(Mo) = p<br/>
ou Mo = [CB  CAB  CA&sup2;B  ...  CA^(n-1)B]
</div>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S7/systemes-multivariables/mimo-system.svg" alt="Systeme MIMO" style="max-width: 550px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Systeme MIMO (Multi-Input Multi-Output) - Couplages et decouplage</p>
</div>

<h4>4. Observabilite</h4>

<p><strong>Definition</strong> :</p>
<p>Un systeme est observable si on peut determiner l'etat initial a partir des entrees et sorties sur un intervalle de temps fini.</p>

<p><strong>Critere de Kalman</strong> :</p>
<div class="code-block">
rang(Mo) = n<br/><br/>
ou Mo = |  C   |<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| CA   |<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| CA&sup2; |<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| ...  |<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|CA^(n-1)|<br/><br/>
Mo &isin; R^(np&times;n) : matrice d'observabilite
</div>

<p><strong>Interpretation</strong> :</p>
<ul>
  <li>Si observable : on peut reconstruire l'etat a partir des mesures</li>
  <li>Si non observable : certains modes restent caches</li>
  <li>Necessaire pour implementer un observateur d'etat</li>
</ul>

<p><strong>Dualite</strong> :</p>
<p>(A,B) commandable &hArr; (A^T, C^T) observable. Cette propriete simplifie les developpements theoriques.</p>

<h4>5. Placement de Poles par Retour d'Etat</h4>

<p><strong>Loi de commande</strong> :</p>
<div class="code-block">
u(t) = -K&middot;x(t) + r(t)<br/><br/>
ou :<br/>
- K &isin; R^(m&times;n) : matrice de gains<br/>
- r(t) : reference
</div>

<p><strong>Systeme en boucle fermee</strong> :</p>
<div class="code-block">
x&#775;(t) = (A - BK)&middot;x(t) + B&middot;r(t)
</div>

<p><strong>Theoreme de placement de poles</strong> :</p>
<p>Si (A,B) est commandable, on peut placer les n poles de (A-BK) arbitrairement (en respectant conjugaison complexe).</p>

<p><strong>Methodes de calcul de K</strong> :</p>

<p><strong>Formule d'Ackermann</strong> (SISO) :</p>
<div class="code-block">
K = [0 ... 0 1]&middot;Mc^(-1)&middot;&phi;(A)<br/>
ou &phi;(s) est le polynome caracteristique desire
</div>

<p><strong>Placement de poles Matlab</strong> :</p>
<div class="code-block">
K = place(A, B, poles)  % poles = vecteur des poles desires
</div>

<p><strong>LQR (Linear Quadratic Regulator)</strong> :</p>
<p>Optimisation d'un critere quadratique :</p>
<div class="code-block">
J = &int;_0^&infin; (x^T Q x + u^T R u) dt<br/><br/>
K obtenu par resolution equation de Riccati algebrique
</div>

<h4>6. Observateur d'Etat</h4>

<p><strong>Problematique</strong> :</p>
<p>En pratique, on ne mesure que les sorties y(t), pas l'etat x(t). L'observateur estime x&#770;(t) a partir de y(t) et u(t).</p>

<p><strong>Observateur de Luenberger</strong> :</p>
<div class="code-block">
x&#770;&#775;(t) = A&middot;x&#770;(t) + B&middot;u(t) + L&middot;(y(t) - y&#770;(t))<br/>
y&#770;(t) = C&middot;x&#770;(t)<br/><br/>
ou L &isin; R^(n&times;p) : matrice de gain de l'observateur
</div>

<p><strong>Dynamique de l'erreur d'estimation</strong> :</p>
<div class="code-block">
e(t) = x(t) - x&#770;(t)<br/>
e&#775;(t) = (A - LC)&middot;e(t)
</div>

<p><strong>Theoreme</strong> :</p>
<p>Si (A,C) est observable, on peut placer les poles de (A-LC) arbitrairement.</p>

<p><strong>Choix des poles de l'observateur</strong> :</p>
<p>Generalement 2 a 5 fois plus rapides que ceux du systeme commande (principe de separation).</p>

<p><strong>Commande par retour d'etat estime</strong> :</p>
<div class="code-block">
u(t) = -K&middot;x&#770;(t) + r(t)
</div>

<p><strong>Principe de separation</strong> :</p>
<p>La dynamique globale (commande + observateur) = dynamique commande + dynamique observateur. Les deux peuvent etre concus independamment.</p>

<h4>7. Decouplage des Systemes MIMO</h4>

<p><strong>Problematique</strong> :</p>
<p>Dans un systeme MIMO, une entree ui affecte generalement plusieurs sorties. Objectif : decoupler pour que chaque ui n'affecte qu'une sortie yi.</p>

<p><strong>Decouplage statique</strong> :</p>
<p>Trouver une matrice D telle que :</p>
<div class="code-block">
C(A-BK)^(-1)BD soit diagonale
</div>

<p><strong>Decouplage dynamique</strong> :</p>
<p>Plus general, inclut predistorsion dynamique.</p>

<p><strong>Decouplage par precompensation</strong> :</p>
<div class="code-block">
u(t) = F&middot;v(t)<br/>
ou F est choisie pour decoupler
</div>

<p><strong>Indices de decouplage</strong> :</p>
<p>Lies a la structure du systeme (ordre des derivees necessaires).</p>

<h4>8. Formes Canoniques</h4>

<p><strong>Forme Commandable</strong> :</p>
<p>Representation ou la commandabilite est evidente. Utile pour placement de poles.</p>

<p><strong>Forme Observable</strong> :</p>
<p>Representation ou l'observabilite est evidente. Utile pour conception d'observateur.</p>

<p><strong>Forme de Jordan</strong> :</p>
<div class="code-block">
A est sous forme de blocs de Jordan<br/>
Revele les modes propres du systeme
</div>

<p><strong>Forme Equilibree</strong> :</p>
<p>Egalise commandabilite et observabilite. Utile pour reduction de modele.</p>

<h4>9. Stabilite des Systemes Multivariables</h4>

<p><strong>Critere</strong> :</p>
<p>Systeme stable &hArr; toutes les valeurs propres de A ont partie reelle &lt; 0.</p>

<p><strong>Critere de Lyapunov</strong> :</p>
<p>Trouver matrice P &gt; 0 telle que :</p>
<div class="code-block">
A^T P + PA &lt; 0
</div>
<p>Garantit stabilite asymptotique.</p>

<p><strong>Stabilite entree-sortie</strong> :</p>
<p>Tous les poles de G(s) (partie reelle &lt; 0).</p>

<p><strong>Marge de stabilite</strong> :</p>
<ul>
  <li>Marge de gain</li>
  <li>Marge de phase</li>
  <li>Generalisees pour MIMO (valeurs singulieres)</li>
</ul>

<h4>10. Analyse Frequentielle MIMO</h4>

<p><strong>Valeurs Singulieres</strong> :</p>
<p>Pour une matrice complexe G(j&omega;) :</p>
<div class="code-block">
&sigma;&#772;(G) = valeur singuliere maximale<br/>
&sigma;(G) = valeur singuliere minimale
</div>

<p><strong>Interpretation</strong> :</p>
<ul>
  <li>&sigma;&#772;(G(j&omega;)) : gain maximal du systeme a la frequence &omega;</li>
  <li>&sigma;(G(j&omega;)) : gain minimal</li>
</ul>

<p><strong>Diagrammes de Bode multivariables</strong> :</p>
<p>Trace de &sigma;&#772;(G(j&omega;)) et &sigma;(G(j&omega;)) en fonction de &omega;.</p>

<p><strong>Nombre de conditionnement</strong> :</p>
<div class="code-block">
&kappa;(G) = &sigma;&#772;(G) / &sigma;(G)
</div>
<p>&kappa; eleve &rArr; systeme mal conditionne (sensible aux perturbations).</p>

<h4>11. Commande LQG</h4>

<p><strong>Combinaison LQR + Observateur Stochastique</strong> :</p>
<ul>
  <li><strong>LQR</strong> : placement optimal de poles par minimisation de J</li>
  <li><strong>Filtre de Kalman</strong> : observateur optimal en presence de bruit</li>
</ul>

<p><strong>Structure LQG</strong> :</p>
<div class="code-block">
Systeme bruite :<br/>
x&#775; = Ax + Bu + w    (w : bruit d'etat)<br/>
y = Cx + v          (v : bruit de mesure)<br/><br/>
Loi de commande :<br/>
u = -K&middot;x&#770;<br/>
ou x&#770; est estime par filtre de Kalman
</div>

<p><strong>Proprietes</strong> :</p>
<ul>
  <li>Optimal si bruits gaussiens</li>
  <li>Principe de separation encore valable</li>
  <li>Peut perdre robustesse (contrairement a LQR seul)</li>
</ul>

<h4>12. Applications Pratiques</h4>

<p><strong>Avion</strong> :</p>
<ul>
  <li>Entrees : gouvernes (ailerons, gouvernail, profondeur)</li>
  <li>Sorties : angles (roulis, lacet, tangage)</li>
  <li>Fortement couple, necessite decouplage</li>
</ul>

<p><strong>Robot manipulateur</strong> :</p>
<ul>
  <li>Entrees : couples aux articulations</li>
  <li>Sorties : positions articulaires</li>
  <li>Dynamique non-lineaire linearisee autour d'un point</li>
</ul>

<p><strong>Procede chimique</strong> :</p>
<ul>
  <li>Multiples entrees (debits, temperatures)</li>
  <li>Multiples sorties (concentrations, pressions)</li>
  <li>Temps de reponse varies, couplages complexes</li>
</ul>

<p><strong>Suspension active vehicule</strong> :</p>
<ul>
  <li>Entrees : forces des actuateurs (4 roues)</li>
  <li>Sorties : accelerations, positions (confort, tenue de route)</li>
  <li>Couplage mecanique</li>
</ul>

<p><strong>Reseau electrique</strong> :</p>
<ul>
  <li>Multiples generateurs et charges</li>
  <li>Controle frequence et tension</li>
  <li>Systeme distribue de grande dimension</li>
</ul>

<h2>PART D : PARTIE ANALYTIQUE</h2>

<h3>Connaissances et Competences Mobilisees</h3>

<ul>
  <li>Algebre lineaire avancee (matrices, valeurs propres, valeurs singulieres)</li>
  <li>Analyse de systemes dynamiques</li>
  <li>Maitrise de la representation d'etat</li>
  <li>Theorie de la commande moderne</li>
  <li>Analyse structurelle (commandabilite, observabilite)</li>
  <li>Conception de lois de commande multivariables</li>
  <li>Conception d'observateurs d'etat</li>
  <li>Utilisation de Matlab/Simulink pour simulations</li>
  <li>Analyse frequentielle generalisee</li>
  <li>Comprehension des couplages entre entrees et sorties</li>
</ul>

<h3>Auto-Evaluation</h3>

<p>Ce cours a ete l'un des plus exigeants mathematiquement du cursus. La manipulation de matrices, les changements de base, et les proprietes structurelles demandent une solide maitrise de l'algebre lineaire. Les premiers cours ont ete denses et il a fallu du temps pour bien assimiler les concepts.</p>

<p>La representation d'etat, que j'avais deja vue en SISO, prend toute sa puissance en MIMO. C'est le formalisme naturel pour ces systemes, beaucoup plus pratique que les fonctions de transfert matricielles.</p>

<p>Les notions de commandabilite et d'observabilite sont fondamentales. Elles determinent ce qu'on peut faire avec le systeme. Le fait qu'elles soient duales est elegant et permet de simplifier beaucoup de demonstrations.</p>

<p>Le placement de poles par retour d'etat est puissant mais necessite de mesurer (ou estimer) tout l'etat. L'observateur de Luenberger resout ce probleme de maniere elegante. Le principe de separation est remarquable : on peut concevoir commande et observateur independamment.</p>

<p>Les simulations Matlab ont ete essentielles pour developper l'intuition. Voir l'effet du choix des poles, du gain de l'observateur, etc., sur les reponses temporelles aide enormement a comprendre la theorie.</p>

<p>Le decouplage de systemes MIMO est un probleme difficile. Mathematiquement, on peut souvent le faire, mais les solutions peuvent etre irrealistes (gains trop eleves, sensibilite aux incertitudes). Le compromis entre decouplage parfait et robustesse est important.</p>

<p>L'approche LQR/LQG est seduisante car elle fournit une methode systematique de conception. Cependant, le choix des matrices de ponderation Q et R reste un art, et le lien avec les specifications (depassement, temps de reponse) n'est pas direct.</p>

<h3>Mon Avis</h3>

<p>Ce cours est fondamental pour l'automaticien moderne. Dans l'industrie, la plupart des systemes sont multivariables : on ne peut plus se contenter de boucles SISO independantes. Les techniques MIMO sont incontournables.</p>

<p>Points forts du cours :</p>
<ul>
  <li>Rigueur mathematique des developpements</li>
  <li>Lien entre proprietes structurelles et possibilites de commande</li>
  <li>Elegance de certains resultats (dualite, separation)</li>
  <li>Applications variees et concretes</li>
  <li>Utilisation intensive de Matlab</li>
</ul>

<p>Points a ameliorer :</p>
<ul>
  <li>Plus d'exemples de dimensionnement pratique</li>
  <li>Liens avec commande robuste (H&infin;, &mu;-synthese)</li>
  <li>Aspects implementation temps reel</li>
  <li>Gestion de contraintes (saturation des actionneurs)</li>
</ul>

<p>Reflexions :</p>

<p>La representation d'etat est un changement de paradigme par rapport a l'approche fonction de transfert classique. Elle offre une vue "interne" du systeme et permet des techniques de commande beaucoup plus sophistiquees.</p>

<p>Cependant, la complexite mathematique peut etre un frein. En pratique, il faut :</p>
<ul>
  <li>Bons outils logiciels (Matlab Control Toolbox)</li>
  <li>Validation intensive par simulation</li>
  <li>Tests progressifs sur le systeme reel</li>
  <li>Robustesse face aux incertitudes de modelisation</li>
</ul>

<p>La theorie suppose souvent que le modele est parfait (matrices A,B,C,D exactes). En realite, il y a toujours des incertitudes. Les techniques de commande robuste (que nous n'avons qu'effleurees) sont donc cruciales pour l'application industrielle.</p>

<p>Le decouplage complet est seduisant sur le papier mais peut etre contre-productif : il peut necessiter des gains eleves et rendre le systeme fragile face aux incertitudes. Un decouplage partiel ou une approche multivariable qui accepte les couplages mais les gere intelligemment est souvent preferable.</p>

<p>Pour ma carriere future :</p>
<p>Ces techniques sont applicables dans de nombreux domaines :</p>
<ul>
  <li>Aeronautique et spatial (controle de vol)</li>
  <li>Automobile (ESP, suspensions actives, vehicules autonomes)</li>
  <li>Robotique (manipulateurs, drones)</li>
  <li>Procedes industriels (chimie, energie)</li>
  <li>Systemes energetiques (smart grids)</li>
</ul>

<p>La maitrise de ces outils est un atout majeur pour concevoir des systemes de commande performants et robustes. Couplee avec des competences en traitement du signal, estimation, et optimisation, elle ouvre la voie a des carrieres en R&amp;D ou ingenierie avancee dans l'automatique et les systemes embarques.</p>

<hr/>

<h2>Documents de Cours</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Polycopie Cours</h4>
      <p>Cours complet sur les systemes multivariables : representation d'etat, commandabilite, observabilite et synthese de correcteurs.</p>
      <embed src="/cours-pdf/S7/Systemes-Multivariables/polycopie.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Systemes-Multivariables/polycopie.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>Annales 2022</h4>
      <p>Sujet d'examen 2022 avec exercices sur representation d'etat, stabilite et commande multivariable.</p>
      <embed src="/cours-pdf/S7/Systemes-Multivariables/annales-2022.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Systemes-Multivariables/annales-2022.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>Correction Annales 2022</h4>
      <p>Correction detaillee de l'examen 2022 avec explications completes des methodes et resultats.</p>
      <embed src="/cours-pdf/S7/Systemes-Multivariables/correction-2022.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Systemes-Multivariables/correction-2022.pdf" target="_blank">Telecharger</a></p>
    </div>
  </div>
</div>

</div>

<div class="lang-en">

<h1>Multivariable Systems</h1>

<h2>PART A: GENERALITIES</h2>

<h3>Presentation</h3>
<p>The "Multivariable Systems" course extends the analysis and control of dynamic systems to the case of systems with multiple inputs and multiple outputs (MIMO - Multiple Input Multiple Output). This course is essential for dealing with complex real-world systems that cannot be reduced to a single input and a single output.</p>

<p><strong>Academic Year</strong>: 2023-2024<br/>
<strong>Semester</strong>: 7<br/>
<strong>Category</strong>: Control Engineering</p>

<hr/>

<h2>PART B: DESCRIPTIVE PART</h2>

<h3>Experience Details</h3>

<h4>Environment and Context</h4>
<p>The course combined advanced theoretical developments (linear algebra, matrix analysis) with practical applications via Matlab/Simulink. We studied real multivariable systems (aircraft, robots, industrial processes) to understand the specific challenges of their analysis and control.</p>

<h4>My Role</h4>
<p>In this course, I was responsible for:</p>
<ul>
  <li>Modeling MIMO systems using state-space representation</li>
  <li>Analyzing controllability and observability</li>
  <li>Designing multivariable control laws</li>
  <li>Using decoupling techniques</li>
  <li>Implementing state observers</li>
  <li>Simulating multivariable systems in Matlab</li>
  <li>Validating performance and robustness</li>
</ul>

<h2>PART C: TECHNICAL PART</h2>

<p>This section explores the technical aspects of multivariable systems.</p>

<h3>Technical Concepts Learned</h3>

<h4>1. State-Space Representation</h4>

<p><strong>General form</strong>:</p>
<div class="code-block">
x&#775;(t) = A&middot;x(t) + B&middot;u(t)<br/>
y(t) = C&middot;x(t) + D&middot;u(t)<br/><br/>
where:<br/>
- x &isin; R^n: state vector (n state variables)<br/>
- u &isin; R^m: input vector (m inputs)<br/>
- y &isin; R^p: output vector (p outputs)<br/>
- A &isin; R^(n&times;n): state matrix<br/>
- B &isin; R^(n&times;m): input matrix<br/>
- C &isin; R^(p&times;n): output matrix<br/>
- D &isin; R^(p&times;m): direct transmission matrix
</div>

<p><strong>Advantages of state-space representation</strong>:</p>
<ul>
  <li>Natural handling of MIMO systems</li>
  <li>Access to all internal variables</li>
  <li>Facilitates structural property analysis</li>
  <li>Foundation for modern control</li>
</ul>

<p><strong>Transfer function &harr; state-space conversion</strong>:</p>
<ul>
  <li>Matrix-based for MIMO</li>
  <li>Multiple possible realizations (controllable, observable, balanced)</li>
</ul>

<h4>2. Transfer Matrix</h4>

<p><strong>Definition</strong>:</p>
<div class="code-block">
G(s) = C(sI - A)^(-1)B + D<br/><br/>
G(s) is a p&times;m matrix of transfer functions:<br/><br/>
G(s) = | G11(s)  G12(s)  ...  G1m(s) |<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| G21(s)  G22(s)  ...  G2m(s) |<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|  ...     ...    ...   ...   |<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Gp1(s)  Gp2(s)  ...  Gpm(s) |<br/><br/>
Gij(s) = Yi(s)/Uj(s) when all other inputs are zero
</div>

<p><strong>Poles and Zeros</strong>:</p>
<ul>
  <li><strong>Poles</strong>: eigenvalues of A (roots of det(sI-A))</li>
  <li><strong>Transmission zeros</strong>: cancel certain Gij(s)</li>
  <li>More complex than SISO (zeros depend on direction)</li>
</ul>

<h4>3. Controllability</h4>

<p><strong>Definition</strong>:</p>
<p>A system is controllable if the state can be driven from any initial condition to any desired final state in finite time.</p>

<p><strong>Kalman Criterion</strong>:</p>
<div class="code-block">
rank(Mc) = n<br/><br/>
where Mc = [B  AB  A&sup2;B  ...  A^(n-1)B]<br/>
Mc &isin; R^(n&times;nm): controllability matrix
</div>

<p><strong>Interpretation</strong>:</p>
<ul>
  <li>If controllable: closed-loop poles can be placed anywhere</li>
  <li>If not controllable: some modes cannot be influenced</li>
  <li>Kalman decomposition: controllable / uncontrollable parts</li>
</ul>

<p><strong>Output controllability</strong>:</p>
<p>Can the outputs be specifically controlled?</p>
<div class="code-block">
rank(Mo) = p<br/>
where Mo = [CB  CAB  CA&sup2;B  ...  CA^(n-1)B]
</div>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S7/systemes-multivariables/mimo-system.svg" alt="MIMO System" style="max-width: 550px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: MIMO System (Multiple Input Multiple Output) - Couplings and decoupling</p>
</div>

<h4>4. Observability</h4>

<p><strong>Definition</strong>:</p>
<p>A system is observable if the initial state can be determined from inputs and outputs over a finite time interval.</p>

<p><strong>Kalman Criterion</strong>:</p>
<div class="code-block">
rank(Mo) = n<br/><br/>
where Mo = |  C   |<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| CA   |<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| CA&sup2; |<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| ...  |<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|CA^(n-1)|<br/><br/>
Mo &isin; R^(np&times;n): observability matrix
</div>

<p><strong>Interpretation</strong>:</p>
<ul>
  <li>If observable: the state can be reconstructed from measurements</li>
  <li>If not observable: some modes remain hidden</li>
  <li>Required to implement a state observer</li>
</ul>

<p><strong>Duality</strong>:</p>
<p>(A,B) controllable &hArr; (A^T, C^T) observable. This property simplifies theoretical developments.</p>

<h4>5. Pole Placement by State Feedback</h4>

<p><strong>Control law</strong>:</p>
<div class="code-block">
u(t) = -K&middot;x(t) + r(t)<br/><br/>
where:<br/>
- K &isin; R^(m&times;n): gain matrix<br/>
- r(t): reference
</div>

<p><strong>Closed-loop system</strong>:</p>
<div class="code-block">
x&#775;(t) = (A - BK)&middot;x(t) + B&middot;r(t)
</div>

<p><strong>Pole placement theorem</strong>:</p>
<p>If (A,B) is controllable, the n poles of (A-BK) can be placed arbitrarily (respecting complex conjugation).</p>

<p><strong>Methods for computing K</strong>:</p>

<p><strong>Ackermann's formula</strong> (SISO):</p>
<div class="code-block">
K = [0 ... 0 1]&middot;Mc^(-1)&middot;&phi;(A)<br/>
where &phi;(s) is the desired characteristic polynomial
</div>

<p><strong>Matlab pole placement</strong>:</p>
<div class="code-block">
K = place(A, B, poles)  % poles = vector of desired poles
</div>

<p><strong>LQR (Linear Quadratic Regulator)</strong>:</p>
<p>Optimization of a quadratic cost:</p>
<div class="code-block">
J = &int;_0^&infin; (x^T Q x + u^T R u) dt<br/><br/>
K obtained by solving the algebraic Riccati equation
</div>

<h4>6. State Observer</h4>

<p><strong>Problem statement</strong>:</p>
<p>In practice, only the outputs y(t) are measured, not the state x(t). The observer estimates x&#770;(t) from y(t) and u(t).</p>

<p><strong>Luenberger Observer</strong>:</p>
<div class="code-block">
x&#770;&#775;(t) = A&middot;x&#770;(t) + B&middot;u(t) + L&middot;(y(t) - y&#770;(t))<br/>
y&#770;(t) = C&middot;x&#770;(t)<br/><br/>
where L &isin; R^(n&times;p): observer gain matrix
</div>

<p><strong>Estimation error dynamics</strong>:</p>
<div class="code-block">
e(t) = x(t) - x&#770;(t)<br/>
e&#775;(t) = (A - LC)&middot;e(t)
</div>

<p><strong>Theorem</strong>:</p>
<p>If (A,C) is observable, the poles of (A-LC) can be placed arbitrarily.</p>

<p><strong>Choice of observer poles</strong>:</p>
<p>Generally 2 to 5 times faster than those of the controlled system (separation principle).</p>

<p><strong>Control using estimated state feedback</strong>:</p>
<div class="code-block">
u(t) = -K&middot;x&#770;(t) + r(t)
</div>

<p><strong>Separation principle</strong>:</p>
<p>The overall dynamics (control + observer) = control dynamics + observer dynamics. Both can be designed independently.</p>

<h4>7. MIMO System Decoupling</h4>

<p><strong>Problem statement</strong>:</p>
<p>In a MIMO system, an input ui generally affects multiple outputs. Goal: decouple so that each ui affects only one output yi.</p>

<p><strong>Static decoupling</strong>:</p>
<p>Find a matrix D such that:</p>
<div class="code-block">
C(A-BK)^(-1)BD is diagonal
</div>

<p><strong>Dynamic decoupling</strong>:</p>
<p>More general, includes dynamic pre-distortion.</p>

<p><strong>Pre-compensation decoupling</strong>:</p>
<div class="code-block">
u(t) = F&middot;v(t)<br/>
where F is chosen to decouple
</div>

<p><strong>Decoupling indices</strong>:</p>
<p>Related to the system structure (order of required derivatives).</p>

<h4>8. Canonical Forms</h4>

<p><strong>Controllable Form</strong>:</p>
<p>Representation where controllability is obvious. Useful for pole placement.</p>

<p><strong>Observable Form</strong>:</p>
<p>Representation where observability is obvious. Useful for observer design.</p>

<p><strong>Jordan Form</strong>:</p>
<div class="code-block">
A is in Jordan block form<br/>
Reveals the system's eigenmodes
</div>

<p><strong>Balanced Form</strong>:</p>
<p>Equalizes controllability and observability. Useful for model reduction.</p>

<h4>9. Stability of Multivariable Systems</h4>

<p><strong>Criterion</strong>:</p>
<p>System stable &hArr; all eigenvalues of A have real part &lt; 0.</p>

<p><strong>Lyapunov criterion</strong>:</p>
<p>Find a matrix P &gt; 0 such that:</p>
<div class="code-block">
A^T P + PA &lt; 0
</div>
<p>Guarantees asymptotic stability.</p>

<p><strong>Input-output stability</strong>:</p>
<p>All poles of G(s) have real part &lt; 0.</p>

<p><strong>Stability margins</strong>:</p>
<ul>
  <li>Gain margin</li>
  <li>Phase margin</li>
  <li>Generalized for MIMO (singular values)</li>
</ul>

<h4>10. MIMO Frequency Analysis</h4>

<p><strong>Singular Values</strong>:</p>
<p>For a complex matrix G(j&omega;):</p>
<div class="code-block">
&sigma;&#772;(G) = maximum singular value<br/>
&sigma;(G) = minimum singular value
</div>

<p><strong>Interpretation</strong>:</p>
<ul>
  <li>&sigma;&#772;(G(j&omega;)): maximum gain of the system at frequency &omega;</li>
  <li>&sigma;(G(j&omega;)): minimum gain</li>
</ul>

<p><strong>Multivariable Bode diagrams</strong>:</p>
<p>Plot of &sigma;&#772;(G(j&omega;)) and &sigma;(G(j&omega;)) as a function of &omega;.</p>

<p><strong>Condition number</strong>:</p>
<div class="code-block">
&kappa;(G) = &sigma;&#772;(G) / &sigma;(G)
</div>
<p>High &kappa; &rArr; poorly conditioned system (sensitive to disturbances).</p>

<h4>11. LQG Control</h4>

<p><strong>LQR + Stochastic Observer Combination</strong>:</p>
<ul>
  <li><strong>LQR</strong>: optimal pole placement by minimizing J</li>
  <li><strong>Kalman Filter</strong>: optimal observer in the presence of noise</li>
</ul>

<p><strong>LQG Structure</strong>:</p>
<div class="code-block">
Noisy system:<br/>
x&#775; = Ax + Bu + w    (w: state noise)<br/>
y = Cx + v          (v: measurement noise)<br/><br/>
Control law:<br/>
u = -K&middot;x&#770;<br/>
where x&#770; is estimated by the Kalman filter
</div>

<p><strong>Properties</strong>:</p>
<ul>
  <li>Optimal if noises are Gaussian</li>
  <li>Separation principle still valid</li>
  <li>May lose robustness (unlike LQR alone)</li>
</ul>

<h4>12. Practical Applications</h4>

<p><strong>Aircraft</strong>:</p>
<ul>
  <li>Inputs: control surfaces (ailerons, rudder, elevator)</li>
  <li>Outputs: angles (roll, yaw, pitch)</li>
  <li>Strongly coupled, requires decoupling</li>
</ul>

<p><strong>Robotic manipulator</strong>:</p>
<ul>
  <li>Inputs: joint torques</li>
  <li>Outputs: joint positions</li>
  <li>Nonlinear dynamics linearized around an operating point</li>
</ul>

<p><strong>Chemical process</strong>:</p>
<ul>
  <li>Multiple inputs (flow rates, temperatures)</li>
  <li>Multiple outputs (concentrations, pressures)</li>
  <li>Varying response times, complex couplings</li>
</ul>

<p><strong>Active vehicle suspension</strong>:</p>
<ul>
  <li>Inputs: actuator forces (4 wheels)</li>
  <li>Outputs: accelerations, positions (comfort, road holding)</li>
  <li>Mechanical coupling</li>
</ul>

<p><strong>Power grid</strong>:</p>
<ul>
  <li>Multiple generators and loads</li>
  <li>Frequency and voltage control</li>
  <li>Large-scale distributed system</li>
</ul>

<h2>PART D: ANALYTICAL PART</h2>

<h3>Knowledge and Skills Mobilized</h3>

<ul>
  <li>Advanced linear algebra (matrices, eigenvalues, singular values)</li>
  <li>Dynamic systems analysis</li>
  <li>Mastery of state-space representation</li>
  <li>Modern control theory</li>
  <li>Structural analysis (controllability, observability)</li>
  <li>Design of multivariable control laws</li>
  <li>State observer design</li>
  <li>Use of Matlab/Simulink for simulations</li>
  <li>Generalized frequency analysis</li>
  <li>Understanding of input-output couplings</li>
</ul>

<h3>Self-Evaluation</h3>

<p>This course was one of the most mathematically demanding in the curriculum. Matrix manipulation, basis changes, and structural properties require a solid command of linear algebra. The first lectures were dense and it took time to properly absorb the concepts.</p>

<p>State-space representation, which I had already seen in SISO, reaches its full power in MIMO. It is the natural formalism for these systems, much more practical than matrix transfer functions.</p>

<p>The concepts of controllability and observability are fundamental. They determine what can be done with the system. The fact that they are dual is elegant and simplifies many proofs.</p>

<p>Pole placement through state feedback is powerful but requires measuring (or estimating) the entire state. The Luenberger observer solves this problem elegantly. The separation principle is remarkable: control and observer can be designed independently.</p>

<p>Matlab simulations were essential for developing intuition. Seeing the effect of pole choices, observer gain, etc., on time responses greatly helps in understanding the theory.</p>

<p>Decoupling MIMO systems is a difficult problem. Mathematically, it can often be done, but solutions may be unrealistic (excessive gains, sensitivity to uncertainties). The trade-off between perfect decoupling and robustness is important.</p>

<p>The LQR/LQG approach is attractive because it provides a systematic design method. However, choosing the weighting matrices Q and R remains an art, and the link with specifications (overshoot, settling time) is not direct.</p>

<h3>My Opinion</h3>

<p>This course is fundamental for the modern control engineer. In industry, most systems are multivariable: one can no longer rely on independent SISO loops. MIMO techniques are essential.</p>

<p>Course strengths:</p>
<ul>
  <li>Mathematical rigor of the developments</li>
  <li>Link between structural properties and control possibilities</li>
  <li>Elegance of certain results (duality, separation)</li>
  <li>Varied and concrete applications</li>
  <li>Intensive use of Matlab</li>
</ul>

<p>Areas for improvement:</p>
<ul>
  <li>More practical sizing examples</li>
  <li>Links with robust control (H-infinity, mu-synthesis)</li>
  <li>Real-time implementation aspects</li>
  <li>Constraint management (actuator saturation)</li>
</ul>

<p>Reflections:</p>

<p>State-space representation is a paradigm shift from the classical transfer function approach. It offers an "internal" view of the system and enables much more sophisticated control techniques.</p>

<p>However, mathematical complexity can be a barrier. In practice, one needs:</p>
<ul>
  <li>Good software tools (Matlab Control Toolbox)</li>
  <li>Intensive validation through simulation</li>
  <li>Progressive testing on the real system</li>
  <li>Robustness against modeling uncertainties</li>
</ul>

<p>Theory often assumes a perfect model (exact A, B, C, D matrices). In reality, there are always uncertainties. Robust control techniques (which we only touched upon) are therefore crucial for industrial application.</p>

<p>Complete decoupling is appealing on paper but can be counterproductive: it may require high gains and make the system fragile in the face of uncertainties. Partial decoupling or a multivariable approach that accepts couplings but manages them intelligently is often preferable.</p>

<p>For my future career:</p>
<p>These techniques are applicable in many fields:</p>
<ul>
  <li>Aerospace (flight control)</li>
  <li>Automotive (ESP, active suspensions, autonomous vehicles)</li>
  <li>Robotics (manipulators, drones)</li>
  <li>Industrial processes (chemistry, energy)</li>
  <li>Energy systems (smart grids)</li>
</ul>

<p>Mastering these tools is a major asset for designing high-performance and robust control systems. Combined with skills in signal processing, estimation, and optimization, it opens the door to careers in R&amp;D or advanced engineering in control and embedded systems.</p>

<hr/>

<h2>Course Documents</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Course Handout</h4>
      <p>Complete course on multivariable systems: state-space representation, controllability, observability, and controller synthesis.</p>
      <embed src="/cours-pdf/S7/Systemes-Multivariables/polycopie.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Systemes-Multivariables/polycopie.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>2022 Past Exam</h4>
      <p>2022 exam paper with exercises on state-space representation, stability, and multivariable control.</p>
      <embed src="/cours-pdf/S7/Systemes-Multivariables/annales-2022.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Systemes-Multivariables/annales-2022.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>2022 Past Exam Solutions</h4>
      <p>Detailed solutions for the 2022 exam with full explanations of methods and results.</p>
      <embed src="/cours-pdf/S7/Systemes-Multivariables/correction-2022.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Systemes-Multivariables/correction-2022.pdf" target="_blank">Download</a></p>
    </div>
  </div>
</div>

</div>

---
layout: default
title: "Analyse des Systèmes Non Linéaires - S7"
date: 2024-10-02 10:56:03 +0200
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
    <a href="./my-courses-2023-2024.html" data-i18n-html="back-courses-2023-2024">&larr; Retour aux Cours 2023-2024</a>
</div>

<div class="lang-fr">

<h1>Analyse des Systemes Non Lineaires - Semestre 7</h1>

<p><strong>Annee Universitaire</strong> : 2023-2024<br/>
<strong>Semestre</strong> : 7<br/>
<strong>Credits</strong> : 2.5 ECTS<br/>
<strong>Specialite</strong> : Automatique et Systemes</p>

<hr/>

<h2>PART A - Presentation Generale du Module</h2>

<h3 class="section-title">Vue d'ensemble</h3>

<p>L'analyse des systemes non lineaires est une extension naturelle de l'automatique lineaire vers les systemes reels. Contrairement aux systemes lineaires, les systemes non lineaires peuvent exhiber des comportements complexes : points d'equilibre multiples, cycles limites, bifurcations, et meme chaos. Ce cours fournit les outils mathematiques pour analyser la stabilite et le comportement de ces systemes.</p>

<p><strong>Objectifs pedagogiques</strong> :</p>
<ul>
<li>Comprendre les phenomenes non lineaires (saturation, hysteresis, cycles limites)</li>
<li>Maitriser la theorie de stabilite de Lyapunov</li>
<li>Analyser les systemes dans le plan de phase</li>
<li>Appliquer la methode du premier harmonique (describing function)</li>
<li>Etudier les bifurcations et le chaos</li>
<li>Concevoir des lois de commande non lineaires</li>
</ul>

<h3 class="section-title">Position dans le cursus</h3>

<p>Ce module s'appuie sur :</p>
<ul>
<li><strong>Systemes multivariables (S7)</strong> : representation d'etat, stabilite</li>
<li><strong>Modelisation et commande des systemes lineaires (S5)</strong> : fonction de transfert, Bode, Nyquist</li>
<li><strong>Mathematiques</strong> : equations differentielles, analyse</li>
</ul>

<p>Il prepare a :</p>
<ul>
<li><strong>Commande avancee</strong> : commande robuste, adaptative</li>
<li><strong>Robotique</strong> : modelisation et commande de robots (systemes fortement non lineaires)</li>
<li><strong>Applications industrielles</strong> : regulation de processus, aerospatial</li>
</ul>

<hr/>

<h2>PART B - Experience Personnelle et Contexte d'Apprentissage</h2>

<h3 class="section-title">Organisation et ressources</h3>

<p>Le module etait organise en cours magistraux et travaux diriges sur le semestre :</p>

<p><strong>Cours magistraux (20h)</strong> :<br/>
Structure en 5 chapitres (chapitre1 a chapitre5) :</p>
<ul>
<li>Chapitre 1 : Introduction aux systemes non lineaires</li>
<li>Chapitre 2 : Analyse dans le plan de phase</li>
<li>Chapitre 3 : Stabilite au sens de Lyapunov</li>
<li>Chapitre 4 : Methode du premier harmonique</li>
<li>Chapitre 5 : Bifurcations et chaos</li>
</ul>

<p><strong>Travaux diriges (16h)</strong> :<br/>
9 seances de TD avec exercices d'application :</p>
<ul>
<li>TD1 a TD4 : plan de phase, points d'equilibre</li>
<li>TD5 a TD7 : stabilite de Lyapunov</li>
<li>TD8 et TD9 : methode du premier harmonique</li>
</ul>

<p><strong>Supports pedagogiques</strong> :</p>
<ul>
<li>Fascicules de cours (handout PDF)</li>
<li>Enonces de TD (td1.pdf a td9.pdf)</li>
<li>Simulations MATLAB/Simulink (simtd1.slx, simtd3.slx)</li>
<li>Annales d'examens 2013, 2016, 2017, 2023 avec corriges</li>
</ul>

<h3 class="section-title">Methode de travail</h3>

<p><strong>Cours theorique</strong> :<br/>
Le cours est mathematiquement exigeant avec de nombreuses demonstrations. La comprehension des concepts (fonctions de Lyapunov, stabilite asymptotique) demande du temps et de la pratique.</p>

<p><strong>TD et simulations</strong> :<br/>
Les TD permettent d'appliquer la theorie sur des exemples concrets (pendule, circuits electriques, systemes mecaniques). Les simulations Simulink visualisent les comportements non lineaires.</p>

<p><strong>Annales</strong> :<br/>
Les annales de 2013 a 2023 avec corrections sont essentielles pour comprendre les attentes et le type d'exercices (analyse de stabilite, plan de phase, methode du premier harmonique).</p>

<h3 class="section-title">Difficultes rencontrees</h3>

<p><strong>Abstraction mathematique</strong> :<br/>
La theorie de Lyapunov est puissante mais abstraite. Trouver une fonction de Lyapunov candidate pour prouver la stabilite n'est pas systematique et demande de l'intuition.</p>

<p><strong>Visualisation des comportements</strong> :<br/>
Comprendre les portraits de phase (trajectoires dans l'espace d'etat) necessite une bonne visualisation geometrique.</p>

<p><strong>Methode du premier harmonique</strong> :<br/>
La methode est basee sur des approximations (ne conserver que le premier harmonique). Comprendre ses limites et domaines de validite est important.</p>

<hr/>

<h2>PART C - Aspects Techniques Detailles</h2>

<h3 class="section-title">1. Introduction aux systemes non lineaires</h3>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S7/systemes-non-lineaires/non-linearite.svg" alt="Comportement non-lineaire" style="max-width: 550px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Comparaison entre systeme lineaire et non-lineaire - Phenomene de saturation</p>
</div>

<p><strong>Definition</strong> :</p>

<p>Un systeme est non lineaire si son equation ne verifie pas le principe de superposition. Formellement, si :</p>
<ul>
<li>x1(t) &rarr; y1(t)</li>
<li>x2(t) &rarr; y2(t)</li>
</ul>

<p>Alors pour un systeme lineaire : a&times;x1(t) + b&times;x2(t) &rarr; a&times;y1(t) + b&times;y2(t)</p>

<p>Si cette propriete n'est pas verifiee, le systeme est non lineaire.</p>

<p><strong>Exemples de non-linearites</strong> :</p>

<table>
<thead>
<tr><th>Type</th><th>Equation</th><th>Exemples</th></tr>
</thead>
<tbody>
<tr><td>Saturation</td><td>y = sat(u)</td><td>Actionneurs limites, amplificateurs</td></tr>
<tr><td>Zone morte</td><td>y = 0 si abs(u) &lt; delta</td><td>Jeux mecaniques, seuils</td></tr>
<tr><td>Hysteresis</td><td>y depend de l'historique</td><td>Materiaux magnetiques, frottement</td></tr>
<tr><td>Multiplication</td><td>y = u1 &times; u2</td><td>Modulation, puissance</td></tr>
<tr><td>Fonction trigonometrique</td><td>y = sin(u)</td><td>Pendule, robots</td></tr>
<tr><td>Puissance</td><td>y = u&sup2; ou u&sup3;</td><td>Aerodynamique, hydraulique</td></tr>
</tbody>
</table>

<p><strong>Consequences de la non-linearite</strong> :</p>
<ul>
<li><strong>Points d'equilibre multiples</strong> : plusieurs etats stables possibles</li>
<li><strong>Cycles limites</strong> : oscillations auto-entretenues (independantes des conditions initiales)</li>
<li><strong>Phenomenes de saut</strong> : changement brutal de comportement</li>
<li><strong>Sous-harmoniques</strong> : frequences multiples dans la reponse</li>
<li><strong>Chaos</strong> : comportement imprevisible malgre un systeme deterministe</li>
</ul>

<h3 class="section-title">2. Modelisation des systemes non lineaires</h3>

<p><strong>Representation d'etat</strong> :</p>

<p>Forme generale d'un systeme non lineaire :</p>

<p>x point = f(x, u, t)<br/>
y = g(x, u, t)</p>

<p>ou x est le vecteur d'etat, u l'entree, y la sortie.</p>

<p><strong>Systemes autonomes</strong> :</p>

<p>Si f ne depend pas explicitement du temps :<br/>
x point = f(x)</p>

<p><strong>Exemple : pendule simple</strong></p>

<p>Equation du mouvement :<br/>
theta point point + (g/L) sin(theta) = 0</p>

<p>Representation d'etat :</p>
<ul>
<li>x1 = theta (position angulaire)</li>
<li>x2 = theta point (vitesse angulaire)</li>
</ul>

<p>x1 point = x2<br/>
x2 point = -(g/L) sin(x1)</p>

<p><strong>Points d'equilibre</strong> :</p>

<p>Solutions de f(x_eq) = 0</p>

<p>Pour le pendule :</p>
<ul>
<li>x_eq1 = (0, 0) : position basse (stable)</li>
<li>x_eq2 = (pi, 0) : position haute (instable)</li>
</ul>

<h3 class="section-title">3. Analyse dans le plan de phase</h3>

<p><strong>Definition</strong> :</p>

<p>Pour un systeme du second ordre (2 variables d'etat), le plan de phase represente les trajectoires dans l'espace (x1, x2).</p>

<p><strong>Portrait de phase</strong> :</p>

<p>Ensemble des trajectoires pour differentes conditions initiales. Permet de visualiser :</p>
<ul>
<li>Points d'equilibre</li>
<li>Stabilite</li>
<li>Bassins d'attraction</li>
<li>Cycles limites</li>
</ul>

<p><strong>Classification des points d'equilibre</strong> :</p>

<p>Linearisation autour du point d'equilibre :<br/>
x point = A &times; x</p>

<p>ou A est la matrice jacobienne au point d'equilibre.</p>

<table>
<thead>
<tr><th>Valeurs propres</th><th>Type</th><th>Stabilite</th></tr>
</thead>
<tbody>
<tr><td>Reelles negatives</td><td>Noeud stable</td><td>Stable</td></tr>
<tr><td>Reelles positives</td><td>Noeud instable</td><td>Instable</td></tr>
<tr><td>Complexes Re &lt; 0</td><td>Foyer stable</td><td>Stable</td></tr>
<tr><td>Complexes Re &gt; 0</td><td>Foyer instable</td><td>Instable</td></tr>
<tr><td>Imaginaires pures</td><td>Centre</td><td>Marginalement stable</td></tr>
<tr><td>Opposees (&plusmn; lambda)</td><td>Point selle</td><td>Instable</td></tr>
</tbody>
</table>

<p><strong>Exemple : pendule amorti</strong></p>

<p>theta point point + b theta point + (g/L) sin(theta) = 0</p>

<p>Avec amortissement b &gt; 0 :</p>
<ul>
<li>Point (0, 0) : foyer stable (spirale convergeant vers l'origine)</li>
<li>Point (pi, 0) : point selle (instable)</li>
</ul>

<p><strong>Separatrices</strong> :</p>

<p>Trajectoires qui separent differents bassins d'attraction. Pour le pendule, les separatrices partent du point selle.</p>

<h3 class="section-title">4. Stabilite au sens de Lyapunov</h3>

<p><strong>Definition de la stabilite</strong> :</p>

<p>Un point d'equilibre x_eq est :</p>
<ul>
<li><strong>Stable</strong> : si pour toute condition initiale proche, la trajectoire reste proche</li>
<li><strong>Asymptotiquement stable</strong> : stable + converge vers x_eq</li>
<li><strong>Instable</strong> : sinon</li>
</ul>

<p><strong>Theoreme de Lyapunov (methode directe)</strong> :</p>

<p>Soit V(x) une fonction scalaire (fonction de Lyapunov candidate) :</p>

<p><strong>Conditions</strong> :</p>
<ol>
<li>V(x) &gt; 0 pour tout x different de 0 (definie positive)</li>
<li>V(0) = 0</li>
<li>V point(x) &lt;= 0 (derivee negative ou nulle)</li>
</ol>

<p><strong>Conclusion</strong> :<br/>
Si conditions 1, 2, 3 verifiees : point d'equilibre stable</p>

<p>Si en plus V point(x) &lt; 0 (strictement negatif) : asymptotiquement stable</p>

<p><strong>Interpretation</strong> :</p>

<p>V(x) peut etre vue comme une fonction d'energie generalisee. Si l'energie decroit (V point &lt; 0), le systeme converge vers l'equilibre.</p>

<p><strong>Exemple : systeme lineaire x point = A x</strong></p>

<p>Fonction de Lyapunov candidate : V(x) = x^T P x (forme quadratique)</p>

<p>Derivee : V point = x^T (A^T P + P A) x</p>

<p>Pour que V point &lt; 0, il faut : A^T P + P A = -Q avec Q &gt; 0</p>

<p>Cette equation (equation de Lyapunov) a une solution P &gt; 0 si et seulement si A est stable (valeurs propres a partie reelle negative).</p>

<p><strong>Exemple : pendule avec frottement</strong></p>

<p>Systeme :<br/>
x1 point = x2<br/>
x2 point = -(g/L) sin(x1) - b x2</p>

<p>Fonction de Lyapunov (energie totale) :<br/>
V(x1, x2) = (1/2) x2&sup2; + (g/L) (1 - cos(x1))</p>

<p>V(0, 0) = 0 et V(x1, x2) &gt; 0 pour (x1, x2) different de (0, 0)</p>

<p>Derivee :<br/>
V point = x2 &times; x2 point + (g/L) sin(x1) &times; x1 point<br/>
V point = x2 &times; (-(g/L) sin(x1) - b x2) + (g/L) sin(x1) &times; x2<br/>
V point = -b x2&sup2;</p>

<p>V point &lt;= 0 (negatif ou nul), donc le point (0, 0) est stable.<br/>
V point &lt; 0 pour x2 different de 0, donc asymptotiquement stable.</p>

<p><strong>Region de stabilite</strong> :</p>

<p>La region ou V(x) &lt; c (constante) et V point &lt; 0 est une estimation du bassin d'attraction.</p>

<p><strong>Limitation</strong> :</p>

<p>Trouver une fonction de Lyapunov n'est pas systematique. Il n'y a pas de methode generale. L'ingenieur doit essayer differentes fonctions candidates (souvent basees sur l'energie physique du systeme).</p>

<h3 class="section-title">5. Principe d'invariance de LaSalle</h3>

<p><strong>Extension du theoreme de Lyapunov</strong> :</p>

<p>Si V point &lt;= 0 (et non strictement &lt; 0), le theoreme de Lyapunov standard ne conclut que sur la stabilite, pas la convergence asymptotique.</p>

<p><strong>Theoreme de LaSalle</strong> :</p>

<p>Si V point &lt;= 0, le systeme converge vers le plus grand ensemble invariant contenu dans l'ensemble ou V point = 0.</p>

<p><strong>Application</strong> :</p>

<p>Pour le pendule, V point = -b x2&sup2; = 0 seulement si x2 = 0.<br/>
L'ensemble ou V point = 0 est l'axe x1 (vitesse nulle).<br/>
Le seul ensemble invariant sur cet axe est le point (0, 0).<br/>
Donc le systeme converge vers (0, 0) : stabilite asymptotique.</p>

<h3 class="section-title">6. Methode du premier harmonique (Describing Function)</h3>

<p><strong>Objectif</strong> :</p>

<p>Analyser les cycles limites (oscillations auto-entretenues) dans les systemes boucles comportant une non-linearite.</p>

<p><strong>Principe</strong> :</p>

<p>Remplacer la non-linearite par un gain equivalent qui depend de l'amplitude de l'entree.</p>

<p><strong>Systeme considere</strong> :</p>

<p>Boucle fermee : partie lineaire G(jw) + non-linearite N</p>

<p><strong>Hypothese</strong> :</p>
<ul>
<li>Si l'entree de la non-linearite est sinusoidale : e(t) = A sin(wt)</li>
<li>La sortie contient des harmoniques : s(t) = B1 sin(wt + phi1) + B2 sin(2wt + phi2) + ...</li>
<li>Si G(jw) est passe-bas, les harmoniques superieurs sont attenues</li>
<li>On ne conserve que le premier harmonique</li>
</ul>

<p><strong>Fonction de description</strong> :</p>

<p>N(A) = B1 / A &times; exp(j phi1)</p>

<p>Rapport complexe entre le premier harmonique de sortie et l'entree.</p>

<p><strong>Exemples de fonctions de description</strong> :</p>

<table>
<thead>
<tr><th>Non-linearite</th><th>N(A)</th></tr>
</thead>
<tbody>
<tr><td>Gain lineaire k</td><td>k (constant)</td></tr>
<tr><td>Saturation</td><td>(2k/pi) [arcsin(M/A) + (M/A) sqrt(1 - (M/A)&sup2;)]</td></tr>
<tr><td>Zone morte</td><td>k [1 - (delta/A)] si A &gt; delta</td></tr>
<tr><td>Relais &plusmn; M</td><td>(4M) / (pi A)</td></tr>
<tr><td>Hysteresis</td><td>Fonction complexe (dephasage)</td></tr>
</tbody>
</table>

<p><strong>Condition d'existence d'un cycle limite</strong> :</p>

<p>Un cycle limite existe si :<br/>
1 + G(jw) &times; N(A) = 0</p>

<p>Ou : G(jw) = -1 / N(A)</p>

<p><strong>Graphiquement</strong> :</p>

<p>Tracer G(jw) (Nyquist) et -1/N(A) dans le plan complexe.<br/>
Les intersections donnent les cycles limites possibles (frequence w et amplitude A).</p>

<p><strong>Stabilite du cycle limite</strong> :</p>
<ul>
<li>Si -1/N(A) croise G(jw) de droite a gauche (en augmentant w) : cycle stable</li>
<li>Si croisement de gauche a droite : cycle instable</li>
</ul>

<p><strong>Limitations</strong> :</p>
<ul>
<li>Valable si harmoniques superieurs negligeables</li>
<li>Ne fonctionne pas pour toutes les non-linearites</li>
<li>Resultats approximatifs</li>
</ul>

<h3 class="section-title">7. Linearisation par bouclage (Feedback Linearization)</h3>

<p><strong>Objectif</strong> :</p>

<p>Concevoir une loi de commande qui linearise exactement le systeme non lineaire.</p>

<p><strong>Systeme non lineaire</strong> :</p>

<p>x point = f(x) + g(x) u</p>

<p><strong>Commande linearisante</strong> :</p>

<p>u = (1/g(x)) [-f(x) + v]</p>

<p>ou v est une nouvelle entree.</p>

<p><strong>Systeme en boucle fermee</strong> :</p>

<p>x point = v (systeme lineaire !)</p>

<p>On peut alors choisir v pour obtenir la dynamique desiree (placement de poles, LQR, etc.).</p>

<p><strong>Exemple : pendule inverse</strong></p>

<p>Equation : theta point point = (g/L) sin(theta) + u</p>

<p>Avec u = -(g/L) sin(theta) + v :<br/>
theta point point = v (double integrateur lineaire)</p>

<p>On peut alors stabiliser avec v = -k1 theta - k2 theta point (PD)</p>

<p><strong>Limitations</strong> :</p>
<ul>
<li>Necessite la mesure ou estimation de tous les etats</li>
<li>Modele exact du systeme requis</li>
<li>Annulation de non-linearites peut amplifier les perturbations</li>
<li>Pas toujours possible (conditions mathematiques a verifier)</li>
</ul>

<h3 class="section-title">8. Commande par modes glissants (Sliding Mode Control)</h3>

<p><strong>Principe</strong> :</p>

<p>Concevoir une surface de glissement s(x) = 0 sur laquelle le systeme a le comportement desire, puis forcer le systeme a rester sur cette surface.</p>

<p><strong>Etapes</strong> :</p>
<ol>
<li><strong>Definir la surface</strong> : s(x) = 0 (combinaison lineaire des etats)</li>
<li><strong>Loi de commande</strong> : u force s(x) a converger vers 0</li>
<li><strong>Mode glissant</strong> : une fois sur s(x) = 0, le systeme y reste</li>
</ol>

<p><strong>Exemple : systeme du 1er ordre</strong></p>

<p>x point = f(x) + g(x) u</p>

<p>Surface : s(x) = x - x_desire</p>

<p>Commande : u = (1/g(x)) [-f(x) - k sign(s)]</p>

<p>avec k &gt; 0 suffisamment grand.</p>

<p><strong>Proprietes</strong> :</p>
<ul>
<li><strong>Robustesse</strong> : insensible aux perturbations et incertitudes de modele</li>
<li><strong>Convergence en temps fini</strong> : atteint la surface en temps fini</li>
<li><strong>Chattering</strong> : oscillations haute frequence autour de la surface (probleme pratique)</li>
</ul>

<p><strong>Reduction du chattering</strong> :</p>

<p>Remplacer sign(s) par sat(s/epsilon) ou tanh(s/epsilon) pour lisser la commande.</p>

<h3 class="section-title">9. Bifurcations</h3>

<p><strong>Definition</strong> :</p>

<p>Changement qualitatif du comportement d'un systeme quand un parametre varie.</p>

<p><strong>Types de bifurcations</strong> :</p>

<p><strong>Bifurcation selle-noeud</strong> :</p>
<ul>
<li>Apparition ou disparition de points d'equilibre</li>
<li>Exemple : x point = r + x&sup2; (pour r &lt; 0 : 2 equilibres, r = 0 : 1 equilibre, r &gt; 0 : aucun)</li>
</ul>

<p><strong>Bifurcation transcritique</strong> :</p>
<ul>
<li>Echange de stabilite entre deux points d'equilibre</li>
</ul>

<p><strong>Bifurcation fourche (pitchfork)</strong> :</p>
<ul>
<li>Un point d'equilibre se divise en trois</li>
<li>Symetrique ou asymetrique</li>
</ul>

<p><strong>Bifurcation de Hopf</strong> :</p>
<ul>
<li>Apparition d'un cycle limite a partir d'un point d'equilibre</li>
<li>Exemple : oscillateur de Van der Pol</li>
</ul>

<p><strong>Diagramme de bifurcation</strong> :</p>

<p>Graphique representant les points d'equilibre (ou amplitudes de cycles) en fonction du parametre.</p>

<h3 class="section-title">10. Introduction au chaos</h3>

<p><strong>Definition</strong> :</p>

<p>Comportement aperiodique deterministe sensible aux conditions initiales.</p>

<p><strong>Caracteristiques</strong> :</p>
<ul>
<li><strong>Deterministe</strong> : pas de hasard, equations precises</li>
<li><strong>Aperiodique</strong> : ne se repete jamais exactement</li>
<li><strong>Sensibilite aux conditions initiales</strong> : deux trajectoires proches divergent exponentiellement (effet papillon)</li>
</ul>

<p><strong>Exposants de Lyapunov</strong> :</p>

<p>Mesurent le taux moyen de divergence ou convergence des trajectoires.</p>
<ul>
<li>Exposant &gt; 0 : divergence (chaos)</li>
<li>Exposant &lt; 0 : convergence (stabilite)</li>
<li>Exposant = 0 : comportement marginal</li>
</ul>

<p><strong>Exemples de systemes chaotiques</strong> :</p>

<p><strong>Systeme de Lorenz</strong> :<br/>
x point = sigma (y - x)<br/>
y point = r x - y - x z<br/>
z point = x y - b z</p>

<p>Pour certaines valeurs de parametres (r = 28, sigma = 10, b = 8/3) : comportement chaotique (attracteur etrange).</p>

<p><strong>Attracteur de Lorenz</strong> :</p>

<p>Structure geometrique en forme de papillon dans l'espace de phase. Les trajectoires tournent autour de deux lobes sans jamais se repeter.</p>

<p><strong>Route vers le chaos</strong> :</p>

<p>Cascade de doublement de periode : oscillation de periode T &rarr; 2T &rarr; 4T &rarr; 8T &rarr; ... &rarr; chaos</p>

<p><strong>Carte de Poincare</strong> :</p>

<p>Reduction d'un systeme continu par echantillonnage (intersection avec une surface). Facilite l'analyse du chaos.</p>

<h3 class="section-title">11. Applications pratiques</h3>

<p><strong>Pendule inverse</strong> :</p>

<p>Systeme instable en boucle ouverte. Linearisation par bouclage ou commande par modes glissants pour stabilisation.</p>

<p><strong>Oscillateur de Van der Pol</strong> :</p>

<p>x point point - mu (1 - x&sup2;) x point + x = 0</p>

<p>Pour mu &gt; 0 : cycle limite (oscillation auto-entretenue). Exemple de systeme presentant une bifurcation de Hopf.</p>

<p><strong>Circuit de Chua</strong> :</p>

<p>Circuit electronique simple exhibant du chaos. Utilise pour etudier les systemes chaotiques en laboratoire.</p>

<p><strong>Systeme proie-predateur (Lotka-Volterra)</strong> :</p>

<p>x point = a x - b x y (proies)<br/>
y point = -c y + d x y (predateurs)</p>

<p>Modele biologique avec cycles (oscillations des populations).</p>

<hr/>

<h2>PART D - Analyse Reflexive et Perspectives</h2>

<h3 class="section-title">Competences acquises</h3>

<p><strong>Analyse de stabilite</strong> :<br/>
Maitrise de la theorie de Lyapunov pour prouver rigoureusement la stabilite de systemes non lineaires. Capacite a construire des fonctions de Lyapunov candidates.</p>

<p><strong>Visualisation geometrique</strong> :<br/>
Comprehension des portraits de phase et trajectoires dans l'espace d'etat. Identification des points d'equilibre et de leur nature (noeud, foyer, selle).</p>

<p><strong>Analyse frequentielle</strong> :<br/>
Application de la methode du premier harmonique pour predire l'existence de cycles limites dans les systemes boucles.</p>

<h3 class="section-title">Points cles a retenir</h3>

<p><strong>1. Non-linearite = richesse comportementale</strong> :<br/>
Les systemes non lineaires peuvent avoir des comportements tres varies (multistabilite, cycles limites, chaos) que les systemes lineaires ne peuvent pas exhiber.</p>

<p><strong>2. Lyapunov = outil fondamental</strong> :<br/>
La theorie de Lyapunov est la methode principale pour prouver la stabilite. L'energie du systeme est souvent une bonne fonction de Lyapunov candidate.</p>

<p><strong>3. Linearisation locale vs globale</strong> :<br/>
L'analyse lineaire locale (jacobienne) donne des informations pres des equilibres mais ne capture pas le comportement global.</p>

<p><strong>4. Methode du premier harmonique = approximation</strong> :<br/>
Utile pour analyser rapidement les cycles limites mais resultats approximatifs.</p>

<p><strong>5. Chaos = deterministe mais imprevisible</strong> :<br/>
Le chaos montre qu'un systeme simple et deterministe peut etre imprevisible a long terme. Importance de la sensibilite aux conditions initiales.</p>

<h3 class="section-title">Applications pratiques</h3>

<p><strong>Robotique</strong> :<br/>
Les robots sont des systemes fortement non lineaires (couplages, frottements, gravite). Les methodes de linearisation par bouclage sont couramment utilisees.</p>

<p><strong>Aerospatial</strong> :<br/>
Controle d'attitude des satellites et avions (non-linearites angulaires). Analyse de stabilite critique pour la securite.</p>

<p><strong>Processus industriels</strong> :<br/>
Regulation de temperature, pression, debit avec actionneurs satures. Analyse de stabilite et anti-windup.</p>

<p><strong>Electronique de puissance</strong> :<br/>
Convertisseurs DC-DC avec commutations (non-linearites par morceaux). Commande par modes glissants frequemment employee.</p>

<h3 class="section-title">Retour d'experience</h3>

<p><strong>Cours exigeant</strong> :<br/>
Le niveau mathematique est eleve. Les demonstrations de theoremes (Lyapunov, LaSalle) demandent rigueur et abstraction.</p>

<p><strong>TD essentiels</strong> :<br/>
Les 9 TD permettent de s'approprier les concepts sur des exemples concrets. Les simulations Simulink aident a visualiser les comportements.</p>

<p><strong>Annales precieuses</strong> :<br/>
Les annales de 2013 a 2023 montrent les types d'exercices (analyse de stabilite, plan de phase, methode harmonique). Les corrections detaillees sont tres utiles.</p>

<p><strong>Fascination pour le chaos</strong> :<br/>
Decouvrir que des systemes simples (3 equations) peuvent generer du chaos est marquant. Le paradoxe determinisme/imprevisibilite est philosophiquement interessant.</p>

<h3 class="section-title">Limites et ouvertures</h3>

<p><strong>Limites du module</strong> :</p>
<ul>
<li>Peu de TP pratiques (surtout theorique)</li>
<li>Commande adaptative et robuste non traitees en detail</li>
<li>Systemes hybrides (continus + discrets) non abordes</li>
</ul>

<p><strong>Ouvertures vers</strong> :</p>
<ul>
<li><strong>Commande robuste H-infini</strong> : prise en compte d'incertitudes</li>
<li><strong>Commande adaptative</strong> : systemes avec parametres inconnus ou variants</li>
<li><strong>Observation non lineaire</strong> : estimation d'etats pour systemes non lineaires</li>
<li><strong>Systemes hybrides</strong> : melange dynamiques continues et discretes</li>
<li><strong>Machine learning pour la commande</strong> : apprentissage de lois de commande non lineaires</li>
</ul>

<h3 class="section-title">Conseils pour reussir</h3>

<p><strong>1. Travailler les TD</strong> :<br/>
Refaire les 9 TD sans regarder les corrections. Les exercices couvrent tous les aspects du cours.</p>

<p><strong>2. Visualiser avec MATLAB</strong> :<br/>
Utiliser les simulations Simulink fournies (simtd1, simtd3) et creer ses propres simulations pour explorer les comportements.</p>

<p><strong>3. S'entrainer sur les annales</strong> :<br/>
Les examens de 2013 a 2023 montrent le format attendu. Bien comprendre les corrections.</p>

<p><strong>4. Maitriser Lyapunov</strong> :<br/>
C'est le coeur du cours. Pratiquer la construction de fonctions de Lyapunov sur differents systemes.</p>

<p><strong>5. Comprendre les limites</strong> :<br/>
Chaque methode a ses hypotheses et limites. Savoir quand elle s'applique et quand elle echoue.</p>

<h3 class="section-title">Conclusion</h3>

<p>L'analyse des systemes non lineaires est un domaine fascinant et essentiel pour l'ingenieur automaticien. Les systemes reels sont presque toujours non lineaires, et savoir analyser leur comportement est crucial.</p>

<p><strong>Philosophie du cours</strong> :<br/>
Passer du monde idealise (lineaire) au monde reel (non lineaire). Accepter la complexite et developper des outils pour la maitriser.</p>

<p><strong>Competences transferables</strong> :</p>
<ul>
<li>Rigueur mathematique dans l'analyse</li>
<li>Pensee geometrique (espace d'etat, trajectoires)</li>
<li>Intuition physique (energie, stabilite)</li>
<li>Capacite a gerer la complexite</li>
</ul>

<p><strong>Message principal</strong> :<br/>
Les systemes non lineaires ne sont pas des versions compliquees de systemes lineaires. Ils ont leur propre richesse comportementale. Les comprendre ouvre la porte a l'analyse de systemes reels complexes.</p>

<p><strong>Recommandations</strong> :</p>
<ul>
<li>Approfondir avec des simulations (MATLAB, Python)</li>
<li>Lire des articles sur applications (robotique, aerospatial)</li>
<li>Explorer les liens avec la theorie du chaos et systemes dynamiques</li>
<li>Se former a la commande non lineaire avancee (backstepping, modes glissants d'ordre superieur)</li>
</ul>

<p><strong>Liens avec les autres cours</strong> :</p>
<ul>
<li><a href="./systemes-multivariables.html">Systemes multivariables - S7</a> : representation d'etat, stabilite</li>
<li><a href="./commande-numerique.html">Commande Numerique - S8</a> : implementation discrete</li>
<li><a href="./poo-cpp.html">Programmation Orientee Objets C++ - S7</a> : simulations numeriques</li>
</ul>

<hr/>

<p><em>Cours suivi en 2023-2024 a l'INSA Toulouse, Departement Genie Electrique et Informatique.</em></p>

</div>

<div class="lang-en">

<h1>Nonlinear Systems Analysis - Semester 7</h1>

<p><strong>Academic Year</strong>: 2023-2024<br/>
<strong>Semester</strong>: 7<br/>
<strong>Credits</strong>: 2.5 ECTS<br/>
<strong>Specialization</strong>: Control Systems and Automation</p>

<hr/>

<h2>PART A - General Module Overview</h2>

<h3 class="section-title">Overview</h3>

<p>Nonlinear systems analysis is a natural extension of linear control theory toward real-world systems. Unlike linear systems, nonlinear systems can exhibit complex behaviors: multiple equilibrium points, limit cycles, bifurcations, and even chaos. This course provides the mathematical tools to analyze the stability and behavior of these systems.</p>

<p><strong>Learning objectives</strong>:</p>
<ul>
<li>Understand nonlinear phenomena (saturation, hysteresis, limit cycles)</li>
<li>Master Lyapunov stability theory</li>
<li>Analyze systems in the phase plane</li>
<li>Apply the describing function method</li>
<li>Study bifurcations and chaos</li>
<li>Design nonlinear control laws</li>
</ul>

<h3 class="section-title">Position in the curriculum</h3>

<p>This module builds upon:</p>
<ul>
<li><strong>Multivariable Systems (S7)</strong>: state-space representation, stability</li>
<li><strong>Linear Systems Modeling and Control (S5)</strong>: transfer function, Bode, Nyquist</li>
<li><strong>Mathematics</strong>: differential equations, analysis</li>
</ul>

<p>It prepares for:</p>
<ul>
<li><strong>Advanced control</strong>: robust control, adaptive control</li>
<li><strong>Robotics</strong>: modeling and control of robots (highly nonlinear systems)</li>
<li><strong>Industrial applications</strong>: process control, aerospace</li>
</ul>

<hr/>

<h2>PART B - Personal Experience and Learning Context</h2>

<h3 class="section-title">Organization and resources</h3>

<p>The module was organized into lectures and tutorials over the semester:</p>

<p><strong>Lectures (20h)</strong>:<br/>
Structured in 5 chapters (chapter 1 to chapter 5):</p>
<ul>
<li>Chapter 1: Introduction to nonlinear systems</li>
<li>Chapter 2: Phase plane analysis</li>
<li>Chapter 3: Lyapunov stability</li>
<li>Chapter 4: Describing function method</li>
<li>Chapter 5: Bifurcations and chaos</li>
</ul>

<p><strong>Tutorials (16h)</strong>:<br/>
9 tutorial sessions with application exercises:</p>
<ul>
<li>TD1 to TD4: phase plane, equilibrium points</li>
<li>TD5 to TD7: Lyapunov stability</li>
<li>TD8 and TD9: describing function method</li>
</ul>

<p><strong>Teaching materials</strong>:</p>
<ul>
<li>Course handouts (handout PDF)</li>
<li>Tutorial problem sets (td1.pdf to td9.pdf)</li>
<li>MATLAB/Simulink simulations (simtd1.slx, simtd3.slx)</li>
<li>Past exams from 2013, 2016, 2017, 2023 with solutions</li>
</ul>

<h3 class="section-title">Working method</h3>

<p><strong>Theoretical lectures</strong>:<br/>
The course is mathematically demanding with numerous proofs. Understanding the concepts (Lyapunov functions, asymptotic stability) requires time and practice.</p>

<p><strong>Tutorials and simulations</strong>:<br/>
The tutorials allow applying theory to concrete examples (pendulum, electrical circuits, mechanical systems). Simulink simulations visualize nonlinear behaviors.</p>

<p><strong>Past exams</strong>:<br/>
Past exams from 2013 to 2023 with solutions are essential for understanding expectations and the types of exercises (stability analysis, phase plane, describing function method).</p>

<h3 class="section-title">Difficulties encountered</h3>

<p><strong>Mathematical abstraction</strong>:<br/>
Lyapunov theory is powerful but abstract. Finding a candidate Lyapunov function to prove stability is not systematic and requires intuition.</p>

<p><strong>Behavior visualization</strong>:<br/>
Understanding phase portraits (trajectories in state space) requires good geometric visualization.</p>

<p><strong>Describing function method</strong>:<br/>
The method is based on approximations (retaining only the first harmonic). Understanding its limitations and domains of validity is important.</p>

<hr/>

<h2>PART C - Detailed Technical Aspects</h2>

<h3 class="section-title">1. Introduction to nonlinear systems</h3>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S7/systemes-non-lineaires/non-linearite.svg" alt="Nonlinear behavior" style="max-width: 550px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Comparison between linear and nonlinear systems - Saturation phenomenon</p>
</div>

<p><strong>Definition</strong>:</p>

<p>A system is nonlinear if its equation does not satisfy the superposition principle. Formally, if:</p>
<ul>
<li>x1(t) &rarr; y1(t)</li>
<li>x2(t) &rarr; y2(t)</li>
</ul>

<p>Then for a linear system: a&times;x1(t) + b&times;x2(t) &rarr; a&times;y1(t) + b&times;y2(t)</p>

<p>If this property is not satisfied, the system is nonlinear.</p>

<p><strong>Examples of nonlinearities</strong>:</p>

<table>
<thead>
<tr><th>Type</th><th>Equation</th><th>Examples</th></tr>
</thead>
<tbody>
<tr><td>Saturation</td><td>y = sat(u)</td><td>Limited actuators, amplifiers</td></tr>
<tr><td>Dead zone</td><td>y = 0 if abs(u) &lt; delta</td><td>Mechanical play, thresholds</td></tr>
<tr><td>Hysteresis</td><td>y depends on history</td><td>Magnetic materials, friction</td></tr>
<tr><td>Multiplication</td><td>y = u1 &times; u2</td><td>Modulation, power</td></tr>
<tr><td>Trigonometric function</td><td>y = sin(u)</td><td>Pendulum, robots</td></tr>
<tr><td>Power</td><td>y = u&sup2; or u&sup3;</td><td>Aerodynamics, hydraulics</td></tr>
</tbody>
</table>

<p><strong>Consequences of nonlinearity</strong>:</p>
<ul>
<li><strong>Multiple equilibrium points</strong>: several possible stable states</li>
<li><strong>Limit cycles</strong>: self-sustained oscillations (independent of initial conditions)</li>
<li><strong>Jump phenomena</strong>: abrupt behavior changes</li>
<li><strong>Subharmonics</strong>: multiple frequencies in the response</li>
<li><strong>Chaos</strong>: unpredictable behavior despite a deterministic system</li>
</ul>

<h3 class="section-title">2. Modeling of nonlinear systems</h3>

<p><strong>State-space representation</strong>:</p>

<p>General form of a nonlinear system:</p>

<p>x dot = f(x, u, t)<br/>
y = g(x, u, t)</p>

<p>where x is the state vector, u the input, y the output.</p>

<p><strong>Autonomous systems</strong>:</p>

<p>If f does not explicitly depend on time:<br/>
x dot = f(x)</p>

<p><strong>Example: simple pendulum</strong></p>

<p>Equation of motion:<br/>
theta double dot + (g/L) sin(theta) = 0</p>

<p>State-space representation:</p>
<ul>
<li>x1 = theta (angular position)</li>
<li>x2 = theta dot (angular velocity)</li>
</ul>

<p>x1 dot = x2<br/>
x2 dot = -(g/L) sin(x1)</p>

<p><strong>Equilibrium points</strong>:</p>

<p>Solutions of f(x_eq) = 0</p>

<p>For the pendulum:</p>
<ul>
<li>x_eq1 = (0, 0): lower position (stable)</li>
<li>x_eq2 = (pi, 0): upper position (unstable)</li>
</ul>

<h3 class="section-title">3. Phase plane analysis</h3>

<p><strong>Definition</strong>:</p>

<p>For a second-order system (2 state variables), the phase plane represents trajectories in the (x1, x2) space.</p>

<p><strong>Phase portrait</strong>:</p>

<p>Set of trajectories for different initial conditions. Allows visualization of:</p>
<ul>
<li>Equilibrium points</li>
<li>Stability</li>
<li>Basins of attraction</li>
<li>Limit cycles</li>
</ul>

<p><strong>Classification of equilibrium points</strong>:</p>

<p>Linearization around the equilibrium point:<br/>
x dot = A &times; x</p>

<p>where A is the Jacobian matrix at the equilibrium point.</p>

<table>
<thead>
<tr><th>Eigenvalues</th><th>Type</th><th>Stability</th></tr>
</thead>
<tbody>
<tr><td>Real negative</td><td>Stable node</td><td>Stable</td></tr>
<tr><td>Real positive</td><td>Unstable node</td><td>Unstable</td></tr>
<tr><td>Complex Re &lt; 0</td><td>Stable focus</td><td>Stable</td></tr>
<tr><td>Complex Re &gt; 0</td><td>Unstable focus</td><td>Unstable</td></tr>
<tr><td>Pure imaginary</td><td>Center</td><td>Marginally stable</td></tr>
<tr><td>Opposite (&plusmn; lambda)</td><td>Saddle point</td><td>Unstable</td></tr>
</tbody>
</table>

<p><strong>Example: damped pendulum</strong></p>

<p>theta double dot + b theta dot + (g/L) sin(theta) = 0</p>

<p>With damping b &gt; 0:</p>
<ul>
<li>Point (0, 0): stable focus (spiral converging toward the origin)</li>
<li>Point (pi, 0): saddle point (unstable)</li>
</ul>

<p><strong>Separatrices</strong>:</p>

<p>Trajectories that separate different basins of attraction. For the pendulum, the separatrices originate from the saddle point.</p>

<h3 class="section-title">4. Lyapunov stability</h3>

<p><strong>Definition of stability</strong>:</p>

<p>An equilibrium point x_eq is:</p>
<ul>
<li><strong>Stable</strong>: if for any nearby initial condition, the trajectory remains close</li>
<li><strong>Asymptotically stable</strong>: stable + converges to x_eq</li>
<li><strong>Unstable</strong>: otherwise</li>
</ul>

<p><strong>Lyapunov theorem (direct method)</strong>:</p>

<p>Let V(x) be a scalar function (candidate Lyapunov function):</p>

<p><strong>Conditions</strong>:</p>
<ol>
<li>V(x) &gt; 0 for all x different from 0 (positive definite)</li>
<li>V(0) = 0</li>
<li>V dot(x) &lt;= 0 (negative or zero derivative)</li>
</ol>

<p><strong>Conclusion</strong>:<br/>
If conditions 1, 2, 3 are satisfied: equilibrium point is stable</p>

<p>If additionally V dot(x) &lt; 0 (strictly negative): asymptotically stable</p>

<p><strong>Interpretation</strong>:</p>

<p>V(x) can be seen as a generalized energy function. If the energy decreases (V dot &lt; 0), the system converges to equilibrium.</p>

<p><strong>Example: linear system x dot = A x</strong></p>

<p>Candidate Lyapunov function: V(x) = x^T P x (quadratic form)</p>

<p>Derivative: V dot = x^T (A^T P + P A) x</p>

<p>For V dot &lt; 0, we need: A^T P + P A = -Q with Q &gt; 0</p>

<p>This equation (Lyapunov equation) has a solution P &gt; 0 if and only if A is stable (eigenvalues with negative real part).</p>

<p><strong>Example: pendulum with friction</strong></p>

<p>System:<br/>
x1 dot = x2<br/>
x2 dot = -(g/L) sin(x1) - b x2</p>

<p>Lyapunov function (total energy):<br/>
V(x1, x2) = (1/2) x2&sup2; + (g/L) (1 - cos(x1))</p>

<p>V(0, 0) = 0 and V(x1, x2) &gt; 0 for (x1, x2) different from (0, 0)</p>

<p>Derivative:<br/>
V dot = x2 &times; x2 dot + (g/L) sin(x1) &times; x1 dot<br/>
V dot = x2 &times; (-(g/L) sin(x1) - b x2) + (g/L) sin(x1) &times; x2<br/>
V dot = -b x2&sup2;</p>

<p>V dot &lt;= 0 (negative or zero), so the point (0, 0) is stable.<br/>
V dot &lt; 0 for x2 different from 0, so asymptotically stable.</p>

<p><strong>Stability region</strong>:</p>

<p>The region where V(x) &lt; c (constant) and V dot &lt; 0 is an estimate of the basin of attraction.</p>

<p><strong>Limitation</strong>:</p>

<p>Finding a Lyapunov function is not systematic. There is no general method. The engineer must try different candidate functions (often based on the physical energy of the system).</p>

<h3 class="section-title">5. LaSalle's invariance principle</h3>

<p><strong>Extension of the Lyapunov theorem</strong>:</p>

<p>If V dot &lt;= 0 (and not strictly &lt; 0), the standard Lyapunov theorem only concludes on stability, not asymptotic convergence.</p>

<p><strong>LaSalle's theorem</strong>:</p>

<p>If V dot &lt;= 0, the system converges to the largest invariant set contained in the set where V dot = 0.</p>

<p><strong>Application</strong>:</p>

<p>For the pendulum, V dot = -b x2&sup2; = 0 only if x2 = 0.<br/>
The set where V dot = 0 is the x1 axis (zero velocity).<br/>
The only invariant set on this axis is the point (0, 0).<br/>
Therefore the system converges to (0, 0): asymptotic stability.</p>

<h3 class="section-title">6. Describing function method</h3>

<p><strong>Objective</strong>:</p>

<p>Analyze limit cycles (self-sustained oscillations) in feedback systems containing a nonlinearity.</p>

<p><strong>Principle</strong>:</p>

<p>Replace the nonlinearity with an equivalent gain that depends on the input amplitude.</p>

<p><strong>System considered</strong>:</p>

<p>Closed loop: linear part G(jw) + nonlinearity N</p>

<p><strong>Hypothesis</strong>:</p>
<ul>
<li>If the nonlinearity input is sinusoidal: e(t) = A sin(wt)</li>
<li>The output contains harmonics: s(t) = B1 sin(wt + phi1) + B2 sin(2wt + phi2) + ...</li>
<li>If G(jw) is low-pass, higher harmonics are attenuated</li>
<li>Only the first harmonic is retained</li>
</ul>

<p><strong>Describing function</strong>:</p>

<p>N(A) = B1 / A &times; exp(j phi1)</p>

<p>Complex ratio between the first harmonic of the output and the input.</p>

<p><strong>Examples of describing functions</strong>:</p>

<table>
<thead>
<tr><th>Nonlinearity</th><th>N(A)</th></tr>
</thead>
<tbody>
<tr><td>Linear gain k</td><td>k (constant)</td></tr>
<tr><td>Saturation</td><td>(2k/pi) [arcsin(M/A) + (M/A) sqrt(1 - (M/A)&sup2;)]</td></tr>
<tr><td>Dead zone</td><td>k [1 - (delta/A)] if A &gt; delta</td></tr>
<tr><td>Relay &plusmn; M</td><td>(4M) / (pi A)</td></tr>
<tr><td>Hysteresis</td><td>Complex function (phase shift)</td></tr>
</tbody>
</table>

<p><strong>Condition for limit cycle existence</strong>:</p>

<p>A limit cycle exists if:<br/>
1 + G(jw) &times; N(A) = 0</p>

<p>Or: G(jw) = -1 / N(A)</p>

<p><strong>Graphically</strong>:</p>

<p>Plot G(jw) (Nyquist) and -1/N(A) in the complex plane.<br/>
Intersections give the possible limit cycles (frequency w and amplitude A).</p>

<p><strong>Limit cycle stability</strong>:</p>
<ul>
<li>If -1/N(A) crosses G(jw) from right to left (as w increases): stable cycle</li>
<li>If crossing from left to right: unstable cycle</li>
</ul>

<p><strong>Limitations</strong>:</p>
<ul>
<li>Valid if higher harmonics are negligible</li>
<li>Does not work for all nonlinearities</li>
<li>Approximate results</li>
</ul>

<h3 class="section-title">7. Feedback linearization</h3>

<p><strong>Objective</strong>:</p>

<p>Design a control law that exactly linearizes the nonlinear system.</p>

<p><strong>Nonlinear system</strong>:</p>

<p>x dot = f(x) + g(x) u</p>

<p><strong>Linearizing control</strong>:</p>

<p>u = (1/g(x)) [-f(x) + v]</p>

<p>where v is a new input.</p>

<p><strong>Closed-loop system</strong>:</p>

<p>x dot = v (linear system!)</p>

<p>One can then choose v to obtain the desired dynamics (pole placement, LQR, etc.).</p>

<p><strong>Example: inverted pendulum</strong></p>

<p>Equation: theta double dot = (g/L) sin(theta) + u</p>

<p>With u = -(g/L) sin(theta) + v:<br/>
theta double dot = v (linear double integrator)</p>

<p>Stabilization can then be achieved with v = -k1 theta - k2 theta dot (PD)</p>

<p><strong>Limitations</strong>:</p>
<ul>
<li>Requires measurement or estimation of all states</li>
<li>Exact system model required</li>
<li>Cancellation of nonlinearities may amplify disturbances</li>
<li>Not always possible (mathematical conditions to verify)</li>
</ul>

<h3 class="section-title">8. Sliding mode control</h3>

<p><strong>Principle</strong>:</p>

<p>Design a sliding surface s(x) = 0 on which the system has the desired behavior, then force the system to stay on this surface.</p>

<p><strong>Steps</strong>:</p>
<ol>
<li><strong>Define the surface</strong>: s(x) = 0 (linear combination of states)</li>
<li><strong>Control law</strong>: u forces s(x) to converge to 0</li>
<li><strong>Sliding mode</strong>: once on s(x) = 0, the system remains there</li>
</ol>

<p><strong>Example: first-order system</strong></p>

<p>x dot = f(x) + g(x) u</p>

<p>Surface: s(x) = x - x_desired</p>

<p>Control: u = (1/g(x)) [-f(x) - k sign(s)]</p>

<p>with k &gt; 0 sufficiently large.</p>

<p><strong>Properties</strong>:</p>
<ul>
<li><strong>Robustness</strong>: insensitive to disturbances and model uncertainties</li>
<li><strong>Finite-time convergence</strong>: reaches the surface in finite time</li>
<li><strong>Chattering</strong>: high-frequency oscillations around the surface (practical issue)</li>
</ul>

<p><strong>Chattering reduction</strong>:</p>

<p>Replace sign(s) with sat(s/epsilon) or tanh(s/epsilon) to smooth the control.</p>

<h3 class="section-title">9. Bifurcations</h3>

<p><strong>Definition</strong>:</p>

<p>Qualitative change in a system's behavior when a parameter varies.</p>

<p><strong>Types of bifurcations</strong>:</p>

<p><strong>Saddle-node bifurcation</strong>:</p>
<ul>
<li>Appearance or disappearance of equilibrium points</li>
<li>Example: x dot = r + x&sup2; (for r &lt; 0: 2 equilibria, r = 0: 1 equilibrium, r &gt; 0: none)</li>
</ul>

<p><strong>Transcritical bifurcation</strong>:</p>
<ul>
<li>Exchange of stability between two equilibrium points</li>
</ul>

<p><strong>Pitchfork bifurcation</strong>:</p>
<ul>
<li>One equilibrium point splits into three</li>
<li>Symmetric or asymmetric</li>
</ul>

<p><strong>Hopf bifurcation</strong>:</p>
<ul>
<li>Emergence of a limit cycle from an equilibrium point</li>
<li>Example: Van der Pol oscillator</li>
</ul>

<p><strong>Bifurcation diagram</strong>:</p>

<p>Graph showing equilibrium points (or cycle amplitudes) as a function of the parameter.</p>

<h3 class="section-title">10. Introduction to chaos</h3>

<p><strong>Definition</strong>:</p>

<p>Aperiodic deterministic behavior sensitive to initial conditions.</p>

<p><strong>Characteristics</strong>:</p>
<ul>
<li><strong>Deterministic</strong>: no randomness, precise equations</li>
<li><strong>Aperiodic</strong>: never repeats exactly</li>
<li><strong>Sensitivity to initial conditions</strong>: two nearby trajectories diverge exponentially (butterfly effect)</li>
</ul>

<p><strong>Lyapunov exponents</strong>:</p>

<p>Measure the average rate of divergence or convergence of trajectories.</p>
<ul>
<li>Exponent &gt; 0: divergence (chaos)</li>
<li>Exponent &lt; 0: convergence (stability)</li>
<li>Exponent = 0: marginal behavior</li>
</ul>

<p><strong>Examples of chaotic systems</strong>:</p>

<p><strong>Lorenz system</strong>:<br/>
x dot = sigma (y - x)<br/>
y dot = r x - y - x z<br/>
z dot = x y - b z</p>

<p>For certain parameter values (r = 28, sigma = 10, b = 8/3): chaotic behavior (strange attractor).</p>

<p><strong>Lorenz attractor</strong>:</p>

<p>Butterfly-shaped geometric structure in phase space. Trajectories revolve around two lobes without ever repeating.</p>

<p><strong>Route to chaos</strong>:</p>

<p>Period-doubling cascade: oscillation with period T &rarr; 2T &rarr; 4T &rarr; 8T &rarr; ... &rarr; chaos</p>

<p><strong>Poincare map</strong>:</p>

<p>Reduction of a continuous system through sampling (intersection with a surface). Facilitates chaos analysis.</p>

<h3 class="section-title">11. Practical applications</h3>

<p><strong>Inverted pendulum</strong>:</p>

<p>Open-loop unstable system. Feedback linearization or sliding mode control for stabilization.</p>

<p><strong>Van der Pol oscillator</strong>:</p>

<p>x double dot - mu (1 - x&sup2;) x dot + x = 0</p>

<p>For mu &gt; 0: limit cycle (self-sustained oscillation). Example of a system exhibiting a Hopf bifurcation.</p>

<p><strong>Chua's circuit</strong>:</p>

<p>Simple electronic circuit exhibiting chaos. Used to study chaotic systems in the laboratory.</p>

<p><strong>Predator-prey system (Lotka-Volterra)</strong>:</p>

<p>x dot = a x - b x y (prey)<br/>
y dot = -c y + d x y (predators)</p>

<p>Biological model with cycles (population oscillations).</p>

<hr/>

<h2>PART D - Reflective Analysis and Perspectives</h2>

<h3 class="section-title">Skills acquired</h3>

<p><strong>Stability analysis</strong>:<br/>
Mastery of Lyapunov theory for rigorously proving the stability of nonlinear systems. Ability to construct candidate Lyapunov functions.</p>

<p><strong>Geometric visualization</strong>:<br/>
Understanding of phase portraits and trajectories in state space. Identification of equilibrium points and their nature (node, focus, saddle).</p>

<p><strong>Frequency analysis</strong>:<br/>
Application of the describing function method to predict the existence of limit cycles in feedback systems.</p>

<h3 class="section-title">Key takeaways</h3>

<p><strong>1. Nonlinearity = behavioral richness</strong>:<br/>
Nonlinear systems can exhibit highly varied behaviors (multistability, limit cycles, chaos) that linear systems cannot.</p>

<p><strong>2. Lyapunov = fundamental tool</strong>:<br/>
Lyapunov theory is the main method for proving stability. The system's energy is often a good candidate Lyapunov function.</p>

<p><strong>3. Local vs global linearization</strong>:<br/>
Local linear analysis (Jacobian) provides information near equilibria but does not capture global behavior.</p>

<p><strong>4. Describing function method = approximation</strong>:<br/>
Useful for quickly analyzing limit cycles but yields approximate results.</p>

<p><strong>5. Chaos = deterministic but unpredictable</strong>:<br/>
Chaos shows that a simple, deterministic system can be unpredictable in the long term. Importance of sensitivity to initial conditions.</p>

<h3 class="section-title">Practical applications</h3>

<p><strong>Robotics</strong>:<br/>
Robots are highly nonlinear systems (couplings, friction, gravity). Feedback linearization methods are commonly used.</p>

<p><strong>Aerospace</strong>:<br/>
Attitude control of satellites and aircraft (angular nonlinearities). Critical stability analysis for safety.</p>

<p><strong>Industrial processes</strong>:<br/>
Temperature, pressure, and flow regulation with saturated actuators. Stability analysis and anti-windup.</p>

<p><strong>Power electronics</strong>:<br/>
DC-DC converters with switching (piecewise nonlinearities). Sliding mode control is frequently employed.</p>

<h3 class="section-title">Feedback on experience</h3>

<p><strong>Demanding course</strong>:<br/>
The mathematical level is high. Theorem proofs (Lyapunov, LaSalle) require rigor and abstraction.</p>

<p><strong>Essential tutorials</strong>:<br/>
The 9 tutorials allow appropriating the concepts through concrete examples. Simulink simulations help visualize behaviors.</p>

<p><strong>Valuable past exams</strong>:<br/>
Past exams from 2013 to 2023 show the types of exercises (stability analysis, phase plane, harmonic method). Detailed solutions are very useful.</p>

<p><strong>Fascination with chaos</strong>:<br/>
Discovering that simple systems (3 equations) can generate chaos is striking. The determinism/unpredictability paradox is philosophically interesting.</p>

<h3 class="section-title">Limitations and perspectives</h3>

<p><strong>Module limitations</strong>:</p>
<ul>
<li>Few practical labs (mostly theoretical)</li>
<li>Adaptive and robust control not covered in detail</li>
<li>Hybrid systems (continuous + discrete) not addressed</li>
</ul>

<p><strong>Perspectives toward</strong>:</p>
<ul>
<li><strong>H-infinity robust control</strong>: accounting for uncertainties</li>
<li><strong>Adaptive control</strong>: systems with unknown or varying parameters</li>
<li><strong>Nonlinear observation</strong>: state estimation for nonlinear systems</li>
<li><strong>Hybrid systems</strong>: mix of continuous and discrete dynamics</li>
<li><strong>Machine learning for control</strong>: learning nonlinear control laws</li>
</ul>

<h3 class="section-title">Tips for success</h3>

<p><strong>1. Work through the tutorials</strong>:<br/>
Redo all 9 tutorials without looking at the solutions. The exercises cover all aspects of the course.</p>

<p><strong>2. Visualize with MATLAB</strong>:<br/>
Use the provided Simulink simulations (simtd1, simtd3) and create your own simulations to explore behaviors.</p>

<p><strong>3. Practice with past exams</strong>:<br/>
Exams from 2013 to 2023 show the expected format. Thoroughly understand the solutions.</p>

<p><strong>4. Master Lyapunov</strong>:<br/>
This is the core of the course. Practice constructing Lyapunov functions for different systems.</p>

<p><strong>5. Understand the limitations</strong>:<br/>
Each method has its assumptions and limitations. Know when it applies and when it fails.</p>

<h3 class="section-title">Conclusion</h3>

<p>Nonlinear systems analysis is a fascinating and essential field for the control engineer. Real systems are almost always nonlinear, and knowing how to analyze their behavior is crucial.</p>

<p><strong>Course philosophy</strong>:<br/>
Moving from the idealized world (linear) to the real world (nonlinear). Accepting complexity and developing tools to master it.</p>

<p><strong>Transferable skills</strong>:</p>
<ul>
<li>Mathematical rigor in analysis</li>
<li>Geometric thinking (state space, trajectories)</li>
<li>Physical intuition (energy, stability)</li>
<li>Ability to manage complexity</li>
</ul>

<p><strong>Main message</strong>:<br/>
Nonlinear systems are not complicated versions of linear systems. They have their own behavioral richness. Understanding them opens the door to the analysis of complex real-world systems.</p>

<p><strong>Recommendations</strong>:</p>
<ul>
<li>Deepen knowledge with simulations (MATLAB, Python)</li>
<li>Read articles on applications (robotics, aerospace)</li>
<li>Explore connections with chaos theory and dynamical systems</li>
<li>Train in advanced nonlinear control (backstepping, higher-order sliding modes)</li>
</ul>

<p><strong>Links to other courses</strong>:</p>
<ul>
<li><a href="./systemes-multivariables.html">Multivariable Systems - S7</a>: state-space representation, stability</li>
<li><a href="./commande-numerique.html">Digital Control - S8</a>: discrete implementation</li>
<li><a href="./poo-cpp.html">Object-Oriented Programming C++ - S7</a>: numerical simulations</li>
</ul>

<hr/>

<p><em>Course taken in 2023-2024 at INSA Toulouse, Department of Electrical and Computer Engineering.</em></p>

</div>

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
      <h4><span class="lang-fr">Chapitre 1 - Introduction</span><span class="lang-en">Chapter 1 - Introduction</span></h4>
      <p><span class="lang-fr">Introduction aux systemes non lineaires : exemples, limites des approches lineaires et presentation des outils d'analyse.</span><span class="lang-en">Introduction to nonlinear systems: examples, limitations of linear approaches, and overview of analysis tools.</span></p>
      <div class="pdf-lazy" data-src="/cours-pdf/S7/Analyse-Systemes-Non-Lineaires/chapitre1.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S7/Analyse-Systemes-Non-Lineaires/chapitre1.pdf" target="_blank"><span class="lang-fr">Telecharger</span><span class="lang-en">Download</span></a></p>
    </div>
    <div class="pdf-item">
      <h4><span class="lang-fr">Chapitre 2 - Plans de Phase</span><span class="lang-en">Chapter 2 - Phase Planes</span></h4>
      <p><span class="lang-fr">Methode du plan de phase : points d'equilibre, trajectoires, portrait de phase et analyse geometrique de la stabilite.</span><span class="lang-en">Phase plane method: equilibrium points, trajectories, phase portrait, and geometric stability analysis.</span></p>
      <div class="pdf-lazy" data-src="/cours-pdf/S7/Analyse-Systemes-Non-Lineaires/chapitre2.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S7/Analyse-Systemes-Non-Lineaires/chapitre2.pdf" target="_blank"><span class="lang-fr">Telecharger</span><span class="lang-en">Download</span></a></p>
    </div>
    <div class="pdf-item">
      <h4><span class="lang-fr">Chapitre 3 - Methode de Lyapunov</span><span class="lang-en">Chapter 3 - Lyapunov Method</span></h4>
      <p><span class="lang-fr">Theorie de Lyapunov : fonctions de Lyapunov, criteres de stabilite et methode directe pour l'analyse de stabilite.</span><span class="lang-en">Lyapunov theory: Lyapunov functions, stability criteria, and the direct method for stability analysis.</span></p>
      <div class="pdf-lazy" data-src="/cours-pdf/S7/Analyse-Systemes-Non-Lineaires/chapitre3.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S7/Analyse-Systemes-Non-Lineaires/chapitre3.pdf" target="_blank"><span class="lang-fr">Telecharger</span><span class="lang-en">Download</span></a></p>
    </div>
    <div class="pdf-item">
      <h4><span class="lang-fr">Annales 2023</span><span class="lang-en">2023 Past Exam</span></h4>
      <p><span class="lang-fr">Sujet d'examen 2023 avec exercices sur la stabilite, methode de Lyapunov et cycles limites.</span><span class="lang-en">2023 exam paper with exercises on stability, Lyapunov method, and limit cycles.</span></p>
      <div class="pdf-lazy" data-src="/cours-pdf/S7/Analyse-Systemes-Non-Lineaires/annales-2023.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S7/Analyse-Systemes-Non-Lineaires/annales-2023.pdf" target="_blank"><span class="lang-fr">Telecharger</span><span class="lang-en">Download</span></a></p>
    </div>
  </div>
</div>

<div class="back-nav">
    <a href="./my-courses-2023-2024.html" data-i18n-html="back-courses-2023-2024">&larr; Retour aux Cours 2023-2024</a>
</div>

---
layout: default
title: "Modélisation et Analyse des Systèmes Linéaires et Représentation d'État - S5"
date: 2024-10-02 10:56:03 +0200
---

<style>
.back-nav {
  margin-bottom: 20px;
}
.back-nav a {
  text-decoration: none;
  color: #2a7ae2;
  font-weight: 600;
}
.back-nav a:hover {
  text-decoration: underline;
}
.section-title {
  color: #2a7ae2;
  border-bottom: 2px solid #2a7ae2;
  padding-bottom: 10px;
  margin-top: 30px;
  margin-bottom: 20px;
}
body {
  font-family: Arial, sans-serif;
  background-color: #f4f4f9;
  color: #333;
  line-height: 1.6;
}
h2, h3, h4, h5 {
  color: #2a7ae2;
}
p {
  text-align: justify;
}
code {
  background-color: #f5f5f5;
  padding: 2px 6px;
  border-radius: 3px;
  font-family: 'Courier New', monospace;
}
pre {
  background-color: #f5f5f5;
  padding: 15px;
  border-radius: 5px;
  overflow-x: auto;
}
table {
  border-collapse: collapse;
  width: 100%;
  margin: 20px 0;
}
th, td {
  border: 1px solid #ddd;
  padding: 12px;
  text-align: left;
}
th {
  background-color: #2a7ae2;
  color: white;
}
tr:nth-child(even) {
  background-color: #f9f9f9;
}
</style>

<div class="back-nav">
  <a href="./my-courses-2022-2023.html" data-i18n-html="back-courses-2022-2023">&larr; Retour aux Cours 2022-2023</a>
</div>

<!-- ==================== FRENCH VERSION ==================== -->
<div class="lang-fr">

<h1>Modelisation et Analyse des Systemes Lineaires et Representation d'Etat - S5</h1>

<p><strong>Annee</strong> : 2022-2023 (Semestre 5)<br/>
<strong>Credits</strong> : 3 ECTS<br/>
<strong>Type</strong> : Automatique et Systemes<br/>
<strong>Enseignant</strong> : Subias</p>

<hr/>

<h2>PART A : PRESENTATION GENERALE</h2>

<h3 class="section-title">Objectifs du cours</h3>

<p>Ce cours constitue une formation avancee en theorie des systemes lineaires et en representation d'etat, piliers de l'automatique moderne. L'objectif est de maitriser les techniques de modelisation mathematique, l'analyse de comportement des systemes dynamiques, et les methodes de commande par retour d'etat.</p>

<h3 class="section-title">Competences visees</h3>

<ul>
<li>Maitriser les techniques de modelisation des systemes dynamiques lineaires</li>
<li>Analyser la stabilite et les performances des systemes en boucle ouverte et fermee</li>
<li>Concevoir des lois de commande par retour d'etat avec placement de poles</li>
<li>Dimensionner des observateurs d'etat pour estimer les variables non mesurables</li>
<li>Utiliser MATLAB/Simulink pour l'analyse et la simulation de systemes automatiques</li>
<li>Appliquer les criteres de commandabilite et observabilite</li>
<li>Interpreter les reponses frequentielles (Bode, Nyquist, marges de stabilite)</li>
</ul>

<h3 class="section-title">Organisation</h3>

<ul>
<li><strong>Volume horaire</strong> : Cours magistraux, TD et TP MATLAB/Simulink</li>
<li><strong>Evaluation</strong> : Examen ecrit, TPs notes, Projet sur robot auto-equilibre</li>
<li><strong>Outils</strong> : MATLAB Control System Toolbox, Simulink</li>
<li><strong>Prerequis</strong> : Transformee de Laplace, equations differentielles, algebre lineaire</li>
</ul>

<hr/>

<h2>PART B : EXPERIENCE, CONTEXTE ET FONCTION</h2>

<h3 class="section-title">Contenu pedagogique</h3>

<p>Le cours s'articule autour de trois axes principaux : la modelisation des systemes, l'analyse de stabilite et performances, et la synthese de lois de commande.</p>

<h3>1. Modelisation des systemes lineaires</h3>

<h4>Representation par fonction de transfert</h4>

<p>La fonction de transfert relie l'entree U(s) a la sortie Y(s) en transformee de Laplace :</p>

<p>H(s) = Y(s) / U(s) = N(s) / D(s)</p>

<p>Exemple de systeme du second ordre (moteur DC) :</p>

<pre><code>H(s) = Km / (Tm*s + 1)</code></pre>

<p>Avec Km = gain statique, Tm = constante de temps.</p>

<h4>Representation d'etat</h4>

<p>Forme generale pour un systeme SISO :</p>

<pre><code>dx/dt = A*x + B*u  (equation d'etat)
y = C*x + D*u      (equation de sortie)</code></pre>

<p>Matrices d'etat :</p>
<ul>
<li>A (n x n) : matrice dynamique</li>
<li>B (n x 1) : matrice de commande</li>
<li>C (1 x n) : matrice d'observation</li>
<li>D : action directe (souvent 0)</li>
</ul>

<p>Exemple concret d'un systeme d'ordre 2 :</p>

<pre><code class="language-matlab">A = [0 1; -10 -6.316]
B = [0; 1]
C = [k/0.1001 0]
D = 0</code></pre>

<h3>2. Stabilite des systemes</h3>

<h4>Critere de Routh-Hurwitz</h4>

<p>Pour le polynome caracteristique D(s) = an*s^n + ... + a1*s + a0, on construit le tableau de Routh :</p>

<table>
<tr><th>s^n</th><th>an</th><th>an-2</th><th>an-4</th></tr>
<tr><td>s^n-1</td><td>an-1</td><td>an-3</td><td>an-5</td></tr>
<tr><td>s^n-2</td><td>b1</td><td>b2</td><td>...</td></tr>
<tr><td>...</td><td>...</td><td>...</td><td>...</td></tr>
</table>

<p>Avec b1 = (an-1*an-2 - an*an-3) / an-1</p>

<p><strong>Condition de stabilite</strong> : tous les elements de la premiere colonne doivent etre strictement positifs.</p>

<p>Implementation MATLAB disponible avec la fonction <code>routh.m</code> :</p>

<pre><code class="language-matlab">function RA=routh(poli,epsilon)
% Calcule le tableau de Routh pour un polynome
% Gere les cas particuliers (premiere colonne nulle, ligne de zeros)</code></pre>

<h4>Analyse par les poles</h4>

<p>Un systeme est stable si tous les poles (racines de D(s)) ont une partie reelle negative :</p>

<pre><code>Re(pi) &lt; 0 pour tout i</code></pre>

<p>Classification :</p>
<ul>
<li><strong>Stable asymptotiquement</strong> : tous les poles a partie reelle strictement negative</li>
<li><strong>Marginalement stable</strong> : poles sur l'axe imaginaire (non repetes)</li>
<li><strong>Instable</strong> : au moins un pole a partie reelle positive</li>
</ul>

<h3>3. Analyse frequentielle</h3>

<h4>Diagrammes de Bode</h4>

<p>Representation du gain (en dB) et de la phase (en degres) en fonction de la frequence :</p>

<pre><code>Gain(dB) = 20*log10(|H(jw)|)
Phase(deg) = arg(H(jw)) * 180/pi</code></pre>

<p>Exemple de TP1 avec fonction de transfert H(s) = 0.717 / (0.0033*s + 1) :</p>

<pre><code class="language-matlab">H = tf([0.717], [0.0033 1]);
bode(H)</code></pre>

<p>Mesures experimentales effectuees :</p>
<ul>
<li>Frequences : 0.05 a 10 Hz</li>
<li>Gains mesures : de 0.669 a 0.061 (de -3.5dB a -24dB)</li>
<li>Dephasages : de -2.2 deg a -90 deg</li>
</ul>

<h4>Marges de stabilite</h4>

<p><strong>Marge de gain (Gm)</strong> : gain additionnel avant instabilite a la frequence de coupure de phase -180 deg</p>

<p><strong>Marge de phase (Pm)</strong> : phase additionnelle avant instabilite a la frequence de coupure de gain 0dB</p>

<p>Commande MATLAB :</p>

<pre><code class="language-matlab">[Gm, Pm, Wcg, Wcp] = margin(sys);</code></pre>

<p>Criteres de robustesse :</p>
<ul>
<li>Pm &gt; 45 deg (bonne robustesse)</li>
<li>Gm &gt; 6dB (bonne robustesse)</li>
</ul>

<h3>4. Commande par retour d'etat</h3>

<h4>Placement de poles</h4>

<p>Pour un systeme commandable, on peut imposer les poles en boucle fermee avec un retour d'etat u = -K*x + r.</p>

<p>La matrice de gain K est calculee pour placer les poles desires :</p>

<pre><code class="language-matlab">K = place(A, B, poles_desired)</code></pre>

<p>Exemple du TP3 avec poles complexes conjugues :</p>

<pre><code class="language-matlab">K = place(A, B, [-2+2i, -2-2i])</code></pre>

<p>Les poles choisis determinent les performances :</p>
<ul>
<li>Partie reelle : rapidite (plus negatif = plus rapide)</li>
<li>Partie imaginaire : oscillations (plus grand = plus d'oscillations)</li>
</ul>

<h4>Commandabilite</h4>

<p>Un systeme est commandable si on peut amener l'etat de n'importe quelle condition initiale a n'importe quel etat desire en temps fini.</p>

<p><strong>Critere de Kalman</strong> : rang de la matrice de commandabilite = n</p>

<p>Matrice de commandabilite :</p>

<pre><code>Mc = [B | A*B | A^2*B | ... | A^(n-1)*B]</code></pre>

<p>Test MATLAB :</p>

<pre><code class="language-matlab">Mc = ctrb(A, B);
rank_Mc = rank(Mc);
% Systeme commandable si rank_Mc == n</code></pre>

<h3>5. Observateurs d'etat</h3>

<h4>Principe</h4>

<p>Lorsque tous les etats ne sont pas mesurables, on utilise un observateur pour reconstruire l'etat complet a partir de la sortie mesuree y.</p>

<p>Equation de l'observateur de Luenberger :</p>

<pre><code>dx_hat/dt = A*x_hat + B*u + L*(y - y_hat)
y_hat = C*x_hat</code></pre>

<p>Avec L : gain de l'observateur.</p>

<h4>Observabilite</h4>

<p>Un systeme est observable si on peut determiner l'etat initial x(0) a partir de la connaissance de u(t) et y(t) sur un intervalle fini.</p>

<p><strong>Critere de Kalman</strong> : rang de la matrice d'observabilite = n</p>

<p>Matrice d'observabilite :</p>

<pre><code>Mo = [C; C*A; C*A^2; ...; C*A^(n-1)]</code></pre>

<p>Test MATLAB :</p>

<pre><code class="language-matlab">Mo = obsv(A, C);
rank_Mo = rank(Mo);
% Systeme observable si rank_Mo == n</code></pre>

<h4>Placement des poles de l'observateur</h4>

<p>Les poles de l'observateur sont choisis plus rapides (2 a 5 fois) que ceux de la commande pour garantir une convergence rapide de l'estimation.</p>

<p>Exemples du TD :</p>

<pre><code class="language-matlab">L1 = [-0.365, -0.78]   % Poles lents
L2 = [0.59, 0.32]      % Poles rapides</code></pre>

<h3>6. Analyse modale et formes canoniques</h3>

<h4>Decomposition modale</h4>

<p>Si A est diagonalisable, on peut ecrire :</p>

<pre><code>A = P * Lambda * P^(-1)</code></pre>

<p>Avec Lambda matrice diagonale des valeurs propres et P matrice des vecteurs propres.</p>

<p>Changement de variable z = P^(-1)*x :</p>

<pre><code>dz/dt = Lambda*z + P^(-1)*B*u
y = C*P*z</code></pre>

<p>Chaque mode evolue independamment selon zi(t) = exp(lambda_i*t).</p>

<h4>Formes canoniques</h4>

<p><strong>Forme commandable</strong> : matrices A et B ont une structure particuliere facilitant le placement de poles.</p>

<p><strong>Forme observable</strong> : matrices A et C ont une structure facilitant la conception d'observateurs.</p>

<hr/>

<h2>C. Aspects techniques et pratiques</h2>

<h3>1. Travaux Pratiques MATLAB</h3>

<h4>TP1 : Identification experimentale</h4>

<p>Manipulation d'un systeme reel (moteur ou servomoteur) pour mesurer sa reponse frequentielle.</p>

<p>Code de traitement des donnees :</p>

<pre><code class="language-matlab">% Donnees experimentales
Vg = [-3.93, -2.39, -1.17, -0.44, 0, 0.37, ...];
O = [-292*(2*pi/60)*9, -179*(2*pi/60)*9, ...]; % Vitesse en rad/s

% Trace caracteristique statique
plot(O, Vg);
xlabel('Vitesse angulaire (rad/s)');
ylabel('Tension (V)');

% Analyse frequentielle
G = [0.669, 0.659, 0.609, 0.528, ...];
G_dB = 20*log10(G);
freq = [0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 7.5, 10];

semilogx(freq, G_dB);
xlabel('Frequence (Hz)');
ylabel('Gain (dB)');</code></pre>

<p>Modele identifie : H(s) = 0.717 / (0.0033*s + 1)</p>
<ul>
<li>Gain statique : K = 0.717</li>
<li>Constante de temps : T = 3.3 ms</li>
</ul>

<h4>TP2 : Analyse de stabilite en boucle fermee</h4>

<p>Systeme avec capteur, moteur et retour :</p>

<pre><code class="language-matlab">Ks = 1.55;   % Gain capteur
Km = 47.8;   % Gain moteur
Kg = 0.015;  % Gain reducteur
Tm = 0.3;    % Constante de temps moteur
K = 0.887;   % Gain global

% Fonction de transfert en boucle fermee
num = [Km*K/9];
den = [Tm, 1, Km*K*Ks/9];
sys = tf(num, den);

% Analyse de stabilite
[Gm, Pm, Wcg, Wcp] = margin(sys);
disp(['Marge de gain : ', num2str(Gm), ' (', num2str(20*log10(Gm)), ' dB)']);
disp(['Marge de phase : ', num2str(Pm), ' deg']);

% Calcul des poles
P = pole(sys);
disp('Poles du systeme :');
disp(P);</code></pre>

<p>Resultats typiques :</p>
<ul>
<li>Pm ~ 60 deg &rarr; Systeme bien amorti</li>
<li>Poles a partie reelle negative &rarr; Systeme stable</li>
</ul>

<h4>TP3 : Commande par retour d'etat</h4>

<p>Systeme d'ordre 2 avec placement de poles :</p>

<pre><code class="language-matlab">k = 5;
A = [0 1; -10 -6.316];
B = [0; 1];
C = [k/0.1001 0];

% Creation du modele d'etat
sys = ss(A, B, C, 0);

% Placement de poles en -2 +/- 2j
poles_desired = [-2+2i, -2-2i];
K = place(A, B, poles_desired);

disp('Gain de retour d''etat K :');
disp(K);

% Systeme en boucle fermee
A_cl = A - B*K;
sys_cl = ss(A_cl, B, C, 0);

% Reponse indicielle
step(sys_cl);
title('Reponse en boucle fermee avec retour d''etat');</code></pre>

<h3>2. Projet : Robot auto-equilibre (NXT Way)</h3>

<h4>Modelisation du robot Lego Mindstorms EV3</h4>

<p>Parametres physiques du fichier <code>NXP_robot_parameters.m</code> :</p>

<table>
<tr><th>Parametre</th><th>Valeur</th><th>Unite</th><th>Description</th></tr>
<tr><td>m</td><td>0.03</td><td>kg</td><td>Masse d'une roue</td></tr>
<tr><td>R</td><td>0.042</td><td>m</td><td>Rayon des roues</td></tr>
<tr><td>Jw</td><td>m*R^2/2</td><td>kg.m^2</td><td>Inertie d'une roue</td></tr>
<tr><td>M</td><td>0.67</td><td>kg</td><td>Masse du corps</td></tr>
<tr><td>H</td><td>0.152</td><td>m</td><td>Hauteur du corps</td></tr>
<tr><td>L</td><td>H/2</td><td>m</td><td>Distance centre de masse / axe roues</td></tr>
<tr><td>Jpsi</td><td>M*L^2/3</td><td>kg.m^2</td><td>Inertie en tangage</td></tr>
<tr><td>g</td><td>9.81</td><td>m/s^2</td><td>Acceleration de la gravite</td></tr>
</table>

<p>Moteur DC :</p>
<ul>
<li>Jm = 1e-5 kg.m^2 (inertie moteur)</li>
<li>Rm = 6.83 Ohm (resistance)</li>
<li>Kb = 0.468 V.s/rad (constante de force contre-electromotrice)</li>
<li>Kt = 0.3047 N.m/A (constante de couple)</li>
</ul>

<h4>Simulation Simulink</h4>

<p>Le projet utilise <code>NXTwaySim.slx</code> pour simuler le comportement du robot avec :</p>
<ul>
<li>Modele non-lineaire du pendule inverse</li>
<li>Commande par retour d'etat</li>
<li>Observateur d'etat pour estimer l'angle et la vitesse angulaire</li>
<li>Animation 3D du robot avec <code>PlayAnimation.m</code></li>
</ul>

<p>Objectif : stabiliser le robot en position verticale (theta = 0 deg) malgre les perturbations.</p>

<h3>3. Outils MATLAB essentiels</h3>

<h4>Fonctions de base</h4>

<pre><code class="language-matlab">% Creation de modele
sys = tf(num, den);              % Fonction de transfert
sys = ss(A, B, C, D);            % Representation d'etat

% Conversion
[A, B, C, D] = tf2ss(num, den);  % TF -&gt; Etat
[num, den] = ss2tf(A, B, C, D);  % Etat -&gt; TF

% Analyse
pole(sys);                       % Calcul des poles
zero(sys);                       % Calcul des zeros
eig(A);                          % Valeurs propres de A
rank(ctrb(A, B));               % Test de commandabilite
rank(obsv(A, C));               % Test d'observabilite

% Reponses temporelles
step(sys);                       % Reponse indicielle
impulse(sys);                    % Reponse impulsionnelle
lsim(sys, u, t);                % Reponse a une entree quelconque

% Analyse frequentielle
bode(sys);                       % Diagrammes de Bode
nyquist(sys);                    % Diagramme de Nyquist
nichols(sys);                    % Diagramme de Black-Nichols
margin(sys);                     % Marges de stabilite

% Synthese
K = place(A, B, poles);          % Placement de poles
L = place(A', C', poles)';       % Observateur (dualite)</code></pre>

<h3>4. Methodes de conception</h3>

<h4>Choix des poles en boucle fermee</h4>

<p>Pour un systeme d'ordre 2, forme canonique :</p>

<pre><code>H(s) = wn^2 / (s^2 + 2*zeta*wn*s + wn^2)</code></pre>

<p>Parametres de performance :</p>
<ul>
<li>wn : pulsation naturelle (rapidite)</li>
<li>zeta : coefficient d'amortissement (depassement)</li>
</ul>

<p>Relation avec les poles :</p>

<pre><code>p1,2 = -zeta*wn +/- j*wn*sqrt(1-zeta^2)</code></pre>

<p>Recommandations :</p>
<ul>
<li>zeta = 0.7 : bon compromis (depassement ~ 5%)</li>
<li>Temps de reponse a 5% : tr ~ 3 / (zeta*wn)</li>
</ul>

<h4>Separation des dynamiques</h4>

<p><strong>Principe de separation</strong> : on peut concevoir independamment le retour d'etat K et l'observateur L, puis les combiner.</p>

<p>Regle pratique : placer les poles de l'observateur 2 a 5 fois plus rapides que ceux de la commande.</p>

<p>Exemple :</p>
<ul>
<li>Poles commande : -2 +/- 2j</li>
<li>Poles observateur : -10, -12 (5 fois plus rapides)</li>
</ul>

<hr/>

<h2>D. Analyse et perspectives</h2>

<h3>1. Applications industrielles</h3>

<h4>Systemes de regulation</h4>

<ul>
<li><strong>Procedes industriels</strong> : regulation de temperature, pression, debit</li>
<li><strong>Robotique mobile</strong> : stabilisation de robots a roues, drones</li>
<li><strong>Aerospatial</strong> : pilotage automatique d'avions, fusees</li>
<li><strong>Automobile</strong> : regulation de vitesse (cruise control), ESP, suspension active</li>
</ul>

<h4>Exemples concrets</h4>

<p><strong>Segway / robots auto-equilibres</strong> : application directe du projet NXT Way avec pendule inverse et commande par retour d'etat.</p>

<p><strong>Quadrirotors</strong> : modele d'etat avec 12 etats (position, vitesse, angles, vitesses angulaires), commande hierarchique avec boucles imbriquees.</p>

<h3>2. Liens avec d'autres cours</h3>

<table>
<tr><th>Cours</th><th>Semestre</th><th>Lien avec Modelisation Systemes Lineaires</th></tr>
<tr><td>Circuits et Filtres Analogiques</td><td>S5</td><td>Analyse frequentielle, Bode, systemes du 1er et 2e ordre</td></tr>
<tr><td>Fondements Electronique Numerique</td><td>S5</td><td>Echantillonnage pour commande numerique</td></tr>
<tr><td>Systemes Boucles</td><td>S5</td><td>Asservissements, correcteurs PID</td></tr>
<tr><td>Commande Numerique</td><td>S8</td><td>Discretisation, commande echantillonnee</td></tr>
<tr><td>Temps Reel</td><td>S8</td><td>Implementation de lois de commande</td></tr>
<tr><td>Processus Stochastiques</td><td>S8</td><td>Filtre de Kalman (extension de l'observateur)</td></tr>
</table>

<h3>3. Extensions et sujets avances</h3>

<h4>Commande optimale</h4>

<p>Minimisation d'un critere de performance (LQR - Linear Quadratic Regulator) :</p>

<pre><code>J = integrale[x'Qx + u'Ru] dt</code></pre>

<p>Conduit a un gain optimal K calcule via equation de Riccati.</p>

<h4>Systemes non-lineaires</h4>

<p>Pour les systemes non-lineaires, linearisation autour d'un point d'equilibre :</p>

<pre><code>dx/dt = f(x, u) ~ f(x0, u0) + df/dx|(x0,u0) * (x-x0) + df/du|(x0,u0) * (u-u0)</code></pre>

<p>Obtention d'un modele lineaire tangent exploitable avec les techniques du cours.</p>

<h4>Systemes multivariables (MIMO)</h4>

<p>Extension a plusieurs entrees et sorties :</p>
<ul>
<li>Matrices B (n x m), C (p x n), D (p x m)</li>
<li>Analyse de couplage entre canaux</li>
<li>Commande decouplante</li>
</ul>

<h3>4. Competences professionnelles developpees</h3>

<p>Ce cours a permis de developper des competences cles en automatique moderne, essentielles pour la carriere d'ingenieur en systemes embarques, robotique, ou automatisation industrielle.</p>

<p><strong>Modelisation</strong> :</p>
<ul>
<li>Mise en equations d'un systeme physique a partir des lois fondamentales</li>
<li>Identification experimentale de parametres par analyse frequentielle</li>
<li>Validation de modeles par comparaison simulation/reel</li>
<li>Choix pertinent des variables d'etat</li>
</ul>

<p><strong>Analyse</strong> :</p>
<ul>
<li>Determination de stabilite par methodes algebriques (Routh) et graphiques (lieu des poles)</li>
<li>Evaluation de performances (rapidite, depassement, erreur statique)</li>
<li>Robustesse aux variations de parametres et perturbations</li>
<li>Interpretation des diagrammes de Bode et marges de stabilite</li>
</ul>

<p><strong>Synthese</strong> :</p>
<ul>
<li>Conception de lois de commande par placement de poles selon cahier des charges</li>
<li>Dimensionnement d'observateurs d'etat pour estimation des variables non mesurables</li>
<li>Optimisation de criteres de performance (temps de reponse, depassement)</li>
<li>Application du principe de separation</li>
</ul>

<p><strong>Outils informatiques</strong> :</p>
<ul>
<li>Maitrise de MATLAB/Simulink pour l'automatique (Control System Toolbox)</li>
<li>Programmation de fonctions d'analyse (Routh, identification, placement de poles)</li>
<li>Simulation de systemes complexes avec Simulink</li>
<li>Visualisation et interpretation de resultats</li>
</ul>

<h3>5. Methodologie de resolution de problemes</h3>

<h4>Demarche type pour un probleme d'automatique</h4>

<ol>
<li><strong>Modelisation</strong> : etablir les equations differentielles ou fonction de transfert</li>
<li><strong>Mise sous forme d'etat</strong> : definir les variables d'etat pertinentes</li>
<li><strong>Analyse du systeme en boucle ouverte</strong> :
  <ul>
  <li>Stabilite (Routh, poles)</li>
  <li>Commandabilite et observabilite</li>
  <li>Performances (reponse indicielle)</li>
  </ul>
</li>
<li><strong>Conception de la commande</strong> :
  <ul>
  <li>Choix des poles desires selon cahier des charges</li>
  <li>Calcul du gain K par placement de poles</li>
  <li>Verification des performances</li>
  </ul>
</li>
<li><strong>Conception de l'observateur</strong> (si necessaire) :
  <ul>
  <li>Choix des poles de l'observateur (plus rapides)</li>
  <li>Calcul du gain L</li>
  </ul>
</li>
<li><strong>Simulation et validation</strong> :
  <ul>
  <li>Test avec Simulink</li>
  <li>Analyse de robustesse</li>
  <li>Ajustements si necessaire</li>
  </ul>
</li>
</ol>

<h3>6. Pieges a eviter</h3>

<p>L'experience des TDs et du projet a permis d'identifier plusieurs erreurs courantes en automatique.</p>

<p><strong>Pieges theoriques</strong> :</p>
<ul>
<li><strong>Systeme non commandable/observable</strong> : toujours verifier les criteres de Kalman avant de tenter un placement de poles ou de concevoir un observateur</li>
<li><strong>Poles de l'observateur trop rapides</strong> : risque d'amplification du bruit de mesure et d'instabilite numerique</li>
<li><strong>Confusion entre poles et zeros</strong> : les poles determinent la stabilite, les zeros affectent la forme de la reponse</li>
<li><strong>Oubli des conditions initiales</strong> : la reponse complete = reponse libre + reponse forcee</li>
</ul>

<p><strong>Pieges pratiques</strong> :</p>
<ul>
<li><strong>Unites incoherentes</strong> : attention aux conversions rad/s &harr; tr/min, degres &harr; radians</li>
<li><strong>Saturation des actionneurs</strong> : prendre en compte les limites physiques (commande limitee en amplitude et vitesse)</li>
<li><strong>Modele lineaire hors zone de validite</strong> : linearisation valable uniquement autour du point d'equilibre</li>
<li><strong>Echantillonnage insuffisant</strong> : respect du critere de Shannon pour l'implementation numerique</li>
</ul>

<p><strong>Pieges MATLAB</strong> :</p>
<ul>
<li><strong>Confusion entre systemes SISO et MIMO</strong> : attention aux dimensions des matrices</li>
<li><strong>Mauvais choix de solveur dans Simulink</strong> : peut entrainer des erreurs numeriques</li>
<li><strong>Oubli de la normalisation</strong> : certaines fonctions MATLAB attendent des parametres normalises</li>
</ul>

<h3>7. Ressources et approfondissements</h3>

<h4>Documentation MATLAB</h4>

<ul>
<li><strong>Control System Toolbox User's Guide</strong> : documentation complete des fonctions</li>
<li><strong>Simulink Control Design</strong> : conception et analyse de systemes de commande</li>
<li><strong>Exemples integres</strong> : <code>help control</code>, <code>demo control</code> dans MATLAB</li>
<li><strong>MATLAB Central</strong> : communaute avec exemples et scripts partages</li>
</ul>

<h4>Ouvrages de reference</h4>

<ul>
<li><strong>"Modern Control Engineering"</strong> - Ogata : reference classique, approche pedagogique</li>
<li><strong>"Linear System Theory and Design"</strong> - Chen : approche mathematique rigoureuse</li>
<li><strong>"Feedback Control of Dynamic Systems"</strong> - Franklin, Powell, Emami-Naeini : excellent pour les applications</li>
<li><strong>"Automatique : Systemes lineaires"</strong> - Duc, Theron : en francais, adapte au cursus francais</li>
</ul>

<h4>Logiciels alternatifs</h4>

<ul>
<li><strong>Python</strong> : bibliotheques <code>control</code>, <code>scipy.signal</code> pour calculs scientifiques</li>
<li><strong>Scilab</strong> : alternative open-source a MATLAB avec Xcos (equivalent Simulink)</li>
<li><strong>Octave</strong> : compatible MATLAB, gratuit</li>
<li><strong>LabVIEW</strong> : pour applications industrielles et acquisition de donnees</li>
</ul>

<h3>Mon opinion</h3>

<p>Ce cours represente un pilier fondamental de l'automatique moderne et s'avere indispensable pour tout ingenieur travaillant dans les domaines des systemes embarques, de la robotique, ou de l'automatisation industrielle.</p>

<p><strong>Pourquoi ce cours est essentiel</strong> :</p>
<ol>
<li><strong>Approche moderne</strong> : la representation d'etat est la base de l'automatique contemporaine (vs approche classique par fonction de transfert)</li>
<li><strong>Systemes multivariables</strong> : traitement naturel des systemes MIMO (Multiple Input Multiple Output)</li>
<li><strong>Connexion avec l'informatique</strong> : structure matricielle facilite l'implementation numerique</li>
<li><strong>Base pour sujets avances</strong> : commande optimale (LQR/LQG), commande robuste (H-infini), commande predictive (MPC)</li>
</ol>

<p><strong>Apports du projet robot NXT Way</strong> :</p>

<p>Le projet de robot auto-equilibre a ete particulierement formateur :</p>
<ul>
<li><strong>Application concrete</strong> : pendule inverse = probleme classique d'automatique</li>
<li><strong>Systeme instable</strong> : necessite absolue d'une commande performante</li>
<li><strong>Multidisciplinarite</strong> : mecanique + electronique + automatique</li>
<li><strong>Defi technique</strong> : equilibrage en temps reel avec contraintes materielles</li>
</ul>

<p><strong>Connexions avec autres cours</strong> :</p>

<p>L'automatique est une discipline transversale qui s'appuie sur de nombreux autres cours :</p>
<ul>
<li><strong>Circuits et Filtres Analogiques</strong> (S5) : analyse frequentielle, diagrammes de Bode</li>
<li><strong>Fondements Electronique Numerique</strong> (S5) : echantillonnage pour commande numerique</li>
<li><strong>Systemes Boucles</strong> (S5) : asservissements, correcteurs PID (approche complementaire)</li>
<li><strong>Commande Numerique</strong> (S8) : discretisation, commande echantillonnee, microcontroleurs</li>
<li><strong>Temps Reel</strong> (S8) : implementation de lois de commande avec contraintes temporelles</li>
<li><strong>Processus Stochastiques</strong> (S8) : filtre de Kalman (extension stochastique de l'observateur)</li>
</ul>

<p><strong>Evolution technologique</strong> :</p>

<p>L'automatique evolue rapidement avec les nouvelles technologies :</p>

<p><strong>Tendances actuelles</strong> :</p>
<ul>
<li><strong>Apprentissage automatique</strong> : hybridation commande classique + IA (Deep Reinforcement Learning)</li>
<li><strong>Commande predictive</strong> : MPC (Model Predictive Control) dans l'automobile et l'industrie</li>
<li><strong>Systemes distribues</strong> : commande multi-agents, essaims de drones</li>
<li><strong>Optimisation en temps reel</strong> : calcul embarque performant (DSP, FPGA)</li>
</ul>

<p><strong>Applications emergentes</strong> :</p>
<ul>
<li><strong>Vehicules autonomes</strong> : controle longitudinal/lateral, planification de trajectoire</li>
<li><strong>Drones</strong> : stabilisation, suivi de trajectoire, vol en formation</li>
<li><strong>Exosquelettes</strong> : assistance robotique, reeducation</li>
<li><strong>Industrie 4.0</strong> : cobotique (robots collaboratifs), maintenance predictive</li>
</ul>

<p><strong>Recommandations pour reussir</strong> :</p>
<ol>
<li><strong>Comprendre avant de calculer</strong> : visualiser le comportement physique du systeme</li>
<li><strong>Maitriser MATLAB</strong> : indispensable pour l'automatique (industrie + recherche)</li>
<li><strong>Penser "etats"</strong> : raisonner en variables d'etat plutot qu'en entrees/sorties</li>
<li><strong>Simuler systematiquement</strong> : valider les calculs avant implementation reelle</li>
<li><strong>Tenir compte des limitations</strong> : saturation, bruit, echantillonnage</li>
</ol>

<p><strong>Applications professionnelles</strong> :</p>

<p>Ces competences sont tres recherchees dans de nombreux secteurs :</p>

<p><strong>Automobile</strong> :</p>
<ul>
<li>Systemes ADAS (Advanced Driver Assistance Systems) : ESP, ABS, regulateur adaptatif</li>
<li>Vehicules autonomes : controle de trajectoire, fusion de capteurs</li>
<li>Motorisation hybride/electrique : gestion d'energie, controle de traction</li>
</ul>

<p><strong>Aeronautique/Spatial</strong> :</p>
<ul>
<li>Pilotage automatique d'avions, drones, fusees</li>
<li>Stabilisation de satellites, controle d'attitude</li>
<li>Lanceurs : guidage, navigation, controle</li>
</ul>

<p><strong>Robotique</strong> :</p>
<ul>
<li>Robots mobiles : navigation, evitement d'obstacles</li>
<li>Robots manipulateurs : controle de trajectoire, force</li>
<li>Robots humanoides : equilibrage, marche dynamique</li>
</ul>

<p><strong>Industrie</strong> :</p>
<ul>
<li>Automatisation de procedes : chimie, petrochimie, agroalimentaire</li>
<li>Machines-outils : positionnement precis, usinage</li>
<li>Energies renouvelables : MPPT pour PV, controle d'eoliennes</li>
</ul>

<p><strong>Perspectives de carriere</strong> :</p>
<ul>
<li>Ingenieur automaticien : conception de systemes de commande</li>
<li>Ingenieur systeme embarque : implementation temps reel</li>
<li>Ingenieur R&amp;D : algorithmes de commande avancee</li>
<li>Consultant : expertise en automatique pour divers secteurs</li>
</ul>

<hr/>

<p><strong>Bilan personnel</strong> : Ce cours a fourni les outils mathematiques et pratiques pour analyser et commander des systemes dynamiques lineaires. L'approche etat constitue une methodologie puissante pour les systemes multivariables et la commande moderne. Les TPs MATLAB et le projet robot ont permis de concretiser ces concepts theoriques sur des applications reelles d'automatique. C'est un cours exigeant mais absolument fondamental pour une carriere en automatique, robotique, ou systemes embarques.</p>

</div>

<!-- ==================== ENGLISH VERSION ==================== -->
<div class="lang-en">

<h1>Modeling and Analysis of Linear Systems and State-Space Representation - S5</h1>

<p><strong>Year</strong>: 2022-2023 (Semester 5)<br/>
<strong>Credits</strong>: 3 ECTS<br/>
<strong>Type</strong>: Control Systems and Automation<br/>
<strong>Instructor</strong>: Subias</p>

<hr/>

<h2>PART A: GENERAL OVERVIEW</h2>

<h3 class="section-title">Course Objectives</h3>

<p>This course provides advanced training in linear systems theory and state-space representation, which are cornerstones of modern control engineering. The goal is to master mathematical modeling techniques, analyze the behavior of dynamic systems, and learn state-feedback control methods.</p>

<h3 class="section-title">Targeted Skills</h3>

<ul>
<li>Master modeling techniques for linear dynamic systems</li>
<li>Analyze the stability and performance of open-loop and closed-loop systems</li>
<li>Design state-feedback control laws with pole placement</li>
<li>Design state observers to estimate unmeasurable variables</li>
<li>Use MATLAB/Simulink for analysis and simulation of control systems</li>
<li>Apply controllability and observability criteria</li>
<li>Interpret frequency responses (Bode, Nyquist, stability margins)</li>
</ul>

<h3 class="section-title">Organization</h3>

<ul>
<li><strong>Contact hours</strong>: Lectures, tutorials, and MATLAB/Simulink lab sessions</li>
<li><strong>Assessment</strong>: Written exam, graded lab sessions, self-balancing robot project</li>
<li><strong>Tools</strong>: MATLAB Control System Toolbox, Simulink</li>
<li><strong>Prerequisites</strong>: Laplace transform, differential equations, linear algebra</li>
</ul>

<hr/>

<h2>PART B: EXPERIENCE, CONTEXT AND FUNCTION</h2>

<h3 class="section-title">Course Content</h3>

<p>The course is structured around three main axes: system modeling, stability and performance analysis, and control law synthesis.</p>

<h3>1. Modeling of Linear Systems</h3>

<h4>Transfer Function Representation</h4>

<p>The transfer function relates the input U(s) to the output Y(s) in the Laplace domain:</p>

<p>H(s) = Y(s) / U(s) = N(s) / D(s)</p>

<p>Example of a second-order system (DC motor):</p>

<pre><code>H(s) = Km / (Tm*s + 1)</code></pre>

<p>Where Km = static gain, Tm = time constant.</p>

<h4>State-Space Representation</h4>

<p>General form for a SISO system:</p>

<pre><code>dx/dt = A*x + B*u  (state equation)
y = C*x + D*u      (output equation)</code></pre>

<p>State matrices:</p>
<ul>
<li>A (n x n): dynamic matrix</li>
<li>B (n x 1): input matrix</li>
<li>C (1 x n): output matrix</li>
<li>D: direct feedthrough (often 0)</li>
</ul>

<p>Concrete example of a second-order system:</p>

<pre><code class="language-matlab">A = [0 1; -10 -6.316]
B = [0; 1]
C = [k/0.1001 0]
D = 0</code></pre>

<h3>2. System Stability</h3>

<h4>Routh-Hurwitz Criterion</h4>

<p>For the characteristic polynomial D(s) = an*s^n + ... + a1*s + a0, the Routh table is constructed:</p>

<table>
<tr><th>s^n</th><th>an</th><th>an-2</th><th>an-4</th></tr>
<tr><td>s^n-1</td><td>an-1</td><td>an-3</td><td>an-5</td></tr>
<tr><td>s^n-2</td><td>b1</td><td>b2</td><td>...</td></tr>
<tr><td>...</td><td>...</td><td>...</td><td>...</td></tr>
</table>

<p>Where b1 = (an-1*an-2 - an*an-3) / an-1</p>

<p><strong>Stability condition</strong>: all elements in the first column must be strictly positive.</p>

<p>MATLAB implementation available with the <code>routh.m</code> function:</p>

<pre><code class="language-matlab">function RA=routh(poli,epsilon)
% Computes the Routh table for a polynomial
% Handles special cases (zero first column, row of zeros)</code></pre>

<h4>Pole Analysis</h4>

<p>A system is stable if all poles (roots of D(s)) have a negative real part:</p>

<pre><code>Re(pi) &lt; 0 for all i</code></pre>

<p>Classification:</p>
<ul>
<li><strong>Asymptotically stable</strong>: all poles with strictly negative real part</li>
<li><strong>Marginally stable</strong>: poles on the imaginary axis (non-repeated)</li>
<li><strong>Unstable</strong>: at least one pole with positive real part</li>
</ul>

<h3>3. Frequency Analysis</h3>

<h4>Bode Diagrams</h4>

<p>Representation of gain (in dB) and phase (in degrees) as a function of frequency:</p>

<pre><code>Gain(dB) = 20*log10(|H(jw)|)
Phase(deg) = arg(H(jw)) * 180/pi</code></pre>

<p>Lab 1 example with transfer function H(s) = 0.717 / (0.0033*s + 1):</p>

<pre><code class="language-matlab">H = tf([0.717], [0.0033 1]);
bode(H)</code></pre>

<p>Experimental measurements taken:</p>
<ul>
<li>Frequencies: 0.05 to 10 Hz</li>
<li>Measured gains: from 0.669 to 0.061 (from -3.5dB to -24dB)</li>
<li>Phase shifts: from -2.2 deg to -90 deg</li>
</ul>

<h4>Stability Margins</h4>

<p><strong>Gain margin (Gm)</strong>: additional gain before instability at the -180 deg phase crossover frequency</p>

<p><strong>Phase margin (Pm)</strong>: additional phase before instability at the 0dB gain crossover frequency</p>

<p>MATLAB command:</p>

<pre><code class="language-matlab">[Gm, Pm, Wcg, Wcp] = margin(sys);</code></pre>

<p>Robustness criteria:</p>
<ul>
<li>Pm &gt; 45 deg (good robustness)</li>
<li>Gm &gt; 6dB (good robustness)</li>
</ul>

<h3>4. State-Feedback Control</h3>

<h4>Pole Placement</h4>

<p>For a controllable system, the closed-loop poles can be assigned using state feedback u = -K*x + r.</p>

<p>The gain matrix K is computed to place the desired poles:</p>

<pre><code class="language-matlab">K = place(A, B, poles_desired)</code></pre>

<p>Lab 3 example with complex conjugate poles:</p>

<pre><code class="language-matlab">K = place(A, B, [-2+2i, -2-2i])</code></pre>

<p>The chosen poles determine the performance:</p>
<ul>
<li>Real part: speed (more negative = faster)</li>
<li>Imaginary part: oscillations (larger = more oscillations)</li>
</ul>

<h4>Controllability</h4>

<p>A system is controllable if its state can be driven from any initial condition to any desired state in finite time.</p>

<p><strong>Kalman criterion</strong>: rank of the controllability matrix = n</p>

<p>Controllability matrix:</p>

<pre><code>Mc = [B | A*B | A^2*B | ... | A^(n-1)*B]</code></pre>

<p>MATLAB test:</p>

<pre><code class="language-matlab">Mc = ctrb(A, B);
rank_Mc = rank(Mc);
% System is controllable if rank_Mc == n</code></pre>

<h3>5. State Observers</h3>

<h4>Principle</h4>

<p>When not all states are measurable, an observer is used to reconstruct the full state from the measured output y.</p>

<p>Luenberger observer equation:</p>

<pre><code>dx_hat/dt = A*x_hat + B*u + L*(y - y_hat)
y_hat = C*x_hat</code></pre>

<p>Where L: observer gain.</p>

<h4>Observability</h4>

<p>A system is observable if the initial state x(0) can be determined from the knowledge of u(t) and y(t) over a finite interval.</p>

<p><strong>Kalman criterion</strong>: rank of the observability matrix = n</p>

<p>Observability matrix:</p>

<pre><code>Mo = [C; C*A; C*A^2; ...; C*A^(n-1)]</code></pre>

<p>MATLAB test:</p>

<pre><code class="language-matlab">Mo = obsv(A, C);
rank_Mo = rank(Mo);
% System is observable if rank_Mo == n</code></pre>

<h4>Observer Pole Placement</h4>

<p>The observer poles are chosen to be faster (2 to 5 times) than the controller poles to ensure fast convergence of the state estimate.</p>

<p>Tutorial examples:</p>

<pre><code class="language-matlab">L1 = [-0.365, -0.78]   % Slow poles
L2 = [0.59, 0.32]      % Fast poles</code></pre>

<h3>6. Modal Analysis and Canonical Forms</h3>

<h4>Modal Decomposition</h4>

<p>If A is diagonalizable, we can write:</p>

<pre><code>A = P * Lambda * P^(-1)</code></pre>

<p>Where Lambda is the diagonal matrix of eigenvalues and P is the matrix of eigenvectors.</p>

<p>Change of variable z = P^(-1)*x:</p>

<pre><code>dz/dt = Lambda*z + P^(-1)*B*u
y = C*P*z</code></pre>

<p>Each mode evolves independently as zi(t) = exp(lambda_i*t).</p>

<h4>Canonical Forms</h4>

<p><strong>Controllable canonical form</strong>: matrices A and B have a specific structure that facilitates pole placement.</p>

<p><strong>Observable canonical form</strong>: matrices A and C have a structure that facilitates observer design.</p>

<hr/>

<h2>C. Technical and Practical Aspects</h2>

<h3>1. MATLAB Lab Sessions</h3>

<h4>Lab 1: Experimental Identification</h4>

<p>Hands-on work with a real system (motor or servomotor) to measure its frequency response.</p>

<p>Data processing code:</p>

<pre><code class="language-matlab">% Experimental data
Vg = [-3.93, -2.39, -1.17, -0.44, 0, 0.37, ...];
O = [-292*(2*pi/60)*9, -179*(2*pi/60)*9, ...]; % Speed in rad/s

% Static characteristic plot
plot(O, Vg);
xlabel('Angular velocity (rad/s)');
ylabel('Voltage (V)');

% Frequency analysis
G = [0.669, 0.659, 0.609, 0.528, ...];
G_dB = 20*log10(G);
freq = [0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 7.5, 10];

semilogx(freq, G_dB);
xlabel('Frequency (Hz)');
ylabel('Gain (dB)');</code></pre>

<p>Identified model: H(s) = 0.717 / (0.0033*s + 1)</p>
<ul>
<li>Static gain: K = 0.717</li>
<li>Time constant: T = 3.3 ms</li>
</ul>

<h4>Lab 2: Closed-Loop Stability Analysis</h4>

<p>System with sensor, motor, and feedback:</p>

<pre><code class="language-matlab">Ks = 1.55;   % Sensor gain
Km = 47.8;   % Motor gain
Kg = 0.015;  % Gear ratio gain
Tm = 0.3;    % Motor time constant
K = 0.887;   % Overall gain

% Closed-loop transfer function
num = [Km*K/9];
den = [Tm, 1, Km*K*Ks/9];
sys = tf(num, den);

% Stability analysis
[Gm, Pm, Wcg, Wcp] = margin(sys);
disp(['Gain margin: ', num2str(Gm), ' (', num2str(20*log10(Gm)), ' dB)']);
disp(['Phase margin: ', num2str(Pm), ' deg']);

% Pole computation
P = pole(sys);
disp('System poles:');
disp(P);</code></pre>

<p>Typical results:</p>
<ul>
<li>Pm ~ 60 deg &rarr; Well-damped system</li>
<li>Poles with negative real part &rarr; Stable system</li>
</ul>

<h4>Lab 3: State-Feedback Control</h4>

<p>Second-order system with pole placement:</p>

<pre><code class="language-matlab">k = 5;
A = [0 1; -10 -6.316];
B = [0; 1];
C = [k/0.1001 0];

% Create state-space model
sys = ss(A, B, C, 0);

% Pole placement at -2 +/- 2j
poles_desired = [-2+2i, -2-2i];
K = place(A, B, poles_desired);

disp('State-feedback gain K:');
disp(K);

% Closed-loop system
A_cl = A - B*K;
sys_cl = ss(A_cl, B, C, 0);

% Step response
step(sys_cl);
title('Closed-loop step response with state feedback');</code></pre>

<h3>2. Project: Self-Balancing Robot (NXT Way)</h3>

<h4>Lego Mindstorms EV3 Robot Modeling</h4>

<p>Physical parameters from the <code>NXP_robot_parameters.m</code> file:</p>

<table>
<tr><th>Parameter</th><th>Value</th><th>Unit</th><th>Description</th></tr>
<tr><td>m</td><td>0.03</td><td>kg</td><td>Wheel mass</td></tr>
<tr><td>R</td><td>0.042</td><td>m</td><td>Wheel radius</td></tr>
<tr><td>Jw</td><td>m*R^2/2</td><td>kg.m^2</td><td>Wheel inertia</td></tr>
<tr><td>M</td><td>0.67</td><td>kg</td><td>Body mass</td></tr>
<tr><td>H</td><td>0.152</td><td>m</td><td>Body height</td></tr>
<tr><td>L</td><td>H/2</td><td>m</td><td>Distance from center of mass to wheel axis</td></tr>
<tr><td>Jpsi</td><td>M*L^2/3</td><td>kg.m^2</td><td>Pitch inertia</td></tr>
<tr><td>g</td><td>9.81</td><td>m/s^2</td><td>Gravitational acceleration</td></tr>
</table>

<p>DC Motor:</p>
<ul>
<li>Jm = 1e-5 kg.m^2 (motor inertia)</li>
<li>Rm = 6.83 Ohm (resistance)</li>
<li>Kb = 0.468 V.s/rad (back-EMF constant)</li>
<li>Kt = 0.3047 N.m/A (torque constant)</li>
</ul>

<h4>Simulink Simulation</h4>

<p>The project uses <code>NXTwaySim.slx</code> to simulate the robot behavior with:</p>
<ul>
<li>Nonlinear inverted pendulum model</li>
<li>State-feedback control</li>
<li>State observer to estimate angle and angular velocity</li>
<li>3D robot animation with <code>PlayAnimation.m</code></li>
</ul>

<p>Objective: stabilize the robot in the vertical position (theta = 0 deg) despite disturbances.</p>

<h3>3. Essential MATLAB Tools</h3>

<h4>Core Functions</h4>

<pre><code class="language-matlab">% Model creation
sys = tf(num, den);              % Transfer function
sys = ss(A, B, C, D);            % State-space representation

% Conversion
[A, B, C, D] = tf2ss(num, den);  % TF -&gt; State-space
[num, den] = ss2tf(A, B, C, D);  % State-space -&gt; TF

% Analysis
pole(sys);                       % Pole computation
zero(sys);                       % Zero computation
eig(A);                          % Eigenvalues of A
rank(ctrb(A, B));               % Controllability test
rank(obsv(A, C));               % Observability test

% Time responses
step(sys);                       % Step response
impulse(sys);                    % Impulse response
lsim(sys, u, t);                % Response to arbitrary input

% Frequency analysis
bode(sys);                       % Bode diagrams
nyquist(sys);                    % Nyquist diagram
nichols(sys);                    % Black-Nichols diagram
margin(sys);                     % Stability margins

% Synthesis
K = place(A, B, poles);          % Pole placement
L = place(A', C', poles)';       % Observer (duality)</code></pre>

<h3>4. Design Methods</h3>

<h4>Closed-Loop Pole Selection</h4>

<p>For a second-order system, canonical form:</p>

<pre><code>H(s) = wn^2 / (s^2 + 2*zeta*wn*s + wn^2)</code></pre>

<p>Performance parameters:</p>
<ul>
<li>wn: natural frequency (speed)</li>
<li>zeta: damping ratio (overshoot)</li>
</ul>

<p>Relationship with poles:</p>

<pre><code>p1,2 = -zeta*wn +/- j*wn*sqrt(1-zeta^2)</code></pre>

<p>Recommendations:</p>
<ul>
<li>zeta = 0.7: good compromise (overshoot ~ 5%)</li>
<li>5% settling time: ts ~ 3 / (zeta*wn)</li>
</ul>

<h4>Dynamics Separation</h4>

<p><strong>Separation principle</strong>: the state-feedback gain K and the observer L can be designed independently and then combined.</p>

<p>Practical rule: place the observer poles 2 to 5 times faster than the controller poles.</p>

<p>Example:</p>
<ul>
<li>Controller poles: -2 +/- 2j</li>
<li>Observer poles: -10, -12 (5 times faster)</li>
</ul>

<hr/>

<h2>D. Analysis and Perspectives</h2>

<h3>1. Industrial Applications</h3>

<h4>Regulation Systems</h4>

<ul>
<li><strong>Industrial processes</strong>: temperature, pressure, and flow regulation</li>
<li><strong>Mobile robotics</strong>: stabilization of wheeled robots, drones</li>
<li><strong>Aerospace</strong>: autopilot for aircraft, rockets</li>
<li><strong>Automotive</strong>: cruise control, ESP, active suspension</li>
</ul>

<h4>Concrete Examples</h4>

<p><strong>Segway / self-balancing robots</strong>: direct application of the NXT Way project with inverted pendulum and state-feedback control.</p>

<p><strong>Quadrotors</strong>: state model with 12 states (position, velocity, angles, angular velocities), hierarchical control with nested loops.</p>

<h3>2. Links with Other Courses</h3>

<table>
<tr><th>Course</th><th>Semester</th><th>Link with Linear Systems Modeling</th></tr>
<tr><td>Analog Circuits and Filters</td><td>S5</td><td>Frequency analysis, Bode, 1st and 2nd order systems</td></tr>
<tr><td>Digital Electronics Fundamentals</td><td>S5</td><td>Sampling for digital control</td></tr>
<tr><td>Closed-Loop Systems</td><td>S5</td><td>Servomechanisms, PID controllers</td></tr>
<tr><td>Digital Control</td><td>S8</td><td>Discretization, sampled-data control</td></tr>
<tr><td>Real-Time Systems</td><td>S8</td><td>Implementation of control laws</td></tr>
<tr><td>Stochastic Processes</td><td>S8</td><td>Kalman filter (extension of the observer)</td></tr>
</table>

<h3>3. Extensions and Advanced Topics</h3>

<h4>Optimal Control</h4>

<p>Minimization of a performance criterion (LQR - Linear Quadratic Regulator):</p>

<pre><code>J = integral[x'Qx + u'Ru] dt</code></pre>

<p>Leads to an optimal gain K computed via the Riccati equation.</p>

<h4>Nonlinear Systems</h4>

<p>For nonlinear systems, linearization around an equilibrium point:</p>

<pre><code>dx/dt = f(x, u) ~ f(x0, u0) + df/dx|(x0,u0) * (x-x0) + df/du|(x0,u0) * (u-u0)</code></pre>

<p>This yields a tangent linear model that can be analyzed with the techniques from this course.</p>

<h4>Multivariable Systems (MIMO)</h4>

<p>Extension to multiple inputs and outputs:</p>
<ul>
<li>Matrices B (n x m), C (p x n), D (p x m)</li>
<li>Coupling analysis between channels</li>
<li>Decoupling control</li>
</ul>

<h3>4. Professional Skills Developed</h3>

<p>This course enabled the development of key skills in modern control engineering, essential for a career as an engineer in embedded systems, robotics, or industrial automation.</p>

<p><strong>Modeling</strong>:</p>
<ul>
<li>Deriving equations for a physical system from fundamental laws</li>
<li>Experimental parameter identification through frequency analysis</li>
<li>Model validation by comparing simulation and real-world results</li>
<li>Appropriate selection of state variables</li>
</ul>

<p><strong>Analysis</strong>:</p>
<ul>
<li>Stability determination through algebraic (Routh) and graphical (root locus) methods</li>
<li>Performance evaluation (speed, overshoot, steady-state error)</li>
<li>Robustness to parameter variations and disturbances</li>
<li>Interpretation of Bode diagrams and stability margins</li>
</ul>

<p><strong>Synthesis</strong>:</p>
<ul>
<li>Designing control laws via pole placement according to specifications</li>
<li>Sizing state observers to estimate unmeasurable variables</li>
<li>Optimizing performance criteria (settling time, overshoot)</li>
<li>Applying the separation principle</li>
</ul>

<p><strong>Software tools</strong>:</p>
<ul>
<li>Proficiency in MATLAB/Simulink for control engineering (Control System Toolbox)</li>
<li>Programming analysis functions (Routh, identification, pole placement)</li>
<li>Simulation of complex systems with Simulink</li>
<li>Visualization and interpretation of results</li>
</ul>

<h3>5. Problem-Solving Methodology</h3>

<h4>Standard Approach for a Control Problem</h4>

<ol>
<li><strong>Modeling</strong>: establish the differential equations or transfer function</li>
<li><strong>State-space formulation</strong>: define the relevant state variables</li>
<li><strong>Open-loop system analysis</strong>:
  <ul>
  <li>Stability (Routh, poles)</li>
  <li>Controllability and observability</li>
  <li>Performance (step response)</li>
  </ul>
</li>
<li><strong>Controller design</strong>:
  <ul>
  <li>Selection of desired poles according to specifications</li>
  <li>Computation of gain K via pole placement</li>
  <li>Performance verification</li>
  </ul>
</li>
<li><strong>Observer design</strong> (if necessary):
  <ul>
  <li>Selection of observer poles (faster)</li>
  <li>Computation of gain L</li>
  </ul>
</li>
<li><strong>Simulation and validation</strong>:
  <ul>
  <li>Testing with Simulink</li>
  <li>Robustness analysis</li>
  <li>Adjustments if necessary</li>
  </ul>
</li>
</ol>

<h3>6. Common Pitfalls to Avoid</h3>

<p>Experience from tutorials and the project helped identify several common mistakes in control engineering.</p>

<p><strong>Theoretical pitfalls</strong>:</p>
<ul>
<li><strong>Uncontrollable/unobservable system</strong>: always check Kalman criteria before attempting pole placement or designing an observer</li>
<li><strong>Observer poles too fast</strong>: risk of measurement noise amplification and numerical instability</li>
<li><strong>Confusion between poles and zeros</strong>: poles determine stability, zeros affect the response shape</li>
<li><strong>Forgetting initial conditions</strong>: the complete response = free response + forced response</li>
</ul>

<p><strong>Practical pitfalls</strong>:</p>
<ul>
<li><strong>Inconsistent units</strong>: be careful with conversions rad/s &harr; rpm, degrees &harr; radians</li>
<li><strong>Actuator saturation</strong>: account for physical limits (command limited in amplitude and rate)</li>
<li><strong>Linear model outside validity range</strong>: linearization is valid only around the equilibrium point</li>
<li><strong>Insufficient sampling</strong>: comply with the Shannon criterion for digital implementation</li>
</ul>

<p><strong>MATLAB pitfalls</strong>:</p>
<ul>
<li><strong>Confusion between SISO and MIMO systems</strong>: pay attention to matrix dimensions</li>
<li><strong>Wrong solver choice in Simulink</strong>: can lead to numerical errors</li>
<li><strong>Forgetting normalization</strong>: some MATLAB functions expect normalized parameters</li>
</ul>

<h3>7. Resources and Further Reading</h3>

<h4>MATLAB Documentation</h4>

<ul>
<li><strong>Control System Toolbox User's Guide</strong>: comprehensive function documentation</li>
<li><strong>Simulink Control Design</strong>: control system design and analysis</li>
<li><strong>Built-in examples</strong>: <code>help control</code>, <code>demo control</code> in MATLAB</li>
<li><strong>MATLAB Central</strong>: community with shared examples and scripts</li>
</ul>

<h4>Reference Books</h4>

<ul>
<li><strong>"Modern Control Engineering"</strong> - Ogata: classic reference, pedagogical approach</li>
<li><strong>"Linear System Theory and Design"</strong> - Chen: rigorous mathematical approach</li>
<li><strong>"Feedback Control of Dynamic Systems"</strong> - Franklin, Powell, Emami-Naeini: excellent for applications</li>
<li><strong>"Automatique : Systemes lineaires"</strong> - Duc, Theron: in French, adapted to the French curriculum</li>
</ul>

<h4>Alternative Software</h4>

<ul>
<li><strong>Python</strong>: <code>control</code>, <code>scipy.signal</code> libraries for scientific computing</li>
<li><strong>Scilab</strong>: open-source alternative to MATLAB with Xcos (Simulink equivalent)</li>
<li><strong>Octave</strong>: MATLAB-compatible, free</li>
<li><strong>LabVIEW</strong>: for industrial applications and data acquisition</li>
</ul>

<h3>My Opinion</h3>

<p>This course represents a fundamental pillar of modern control engineering and proves indispensable for any engineer working in the fields of embedded systems, robotics, or industrial automation.</p>

<p><strong>Why this course is essential</strong>:</p>
<ol>
<li><strong>Modern approach</strong>: state-space representation is the foundation of contemporary control theory (vs. the classical transfer function approach)</li>
<li><strong>Multivariable systems</strong>: natural handling of MIMO (Multiple Input Multiple Output) systems</li>
<li><strong>Connection with computing</strong>: matrix-based structure facilitates digital implementation</li>
<li><strong>Foundation for advanced topics</strong>: optimal control (LQR/LQG), robust control (H-infinity), model predictive control (MPC)</li>
</ol>

<p><strong>Contributions of the NXT Way robot project</strong>:</p>

<p>The self-balancing robot project was particularly valuable for learning:</p>
<ul>
<li><strong>Concrete application</strong>: inverted pendulum = classic control problem</li>
<li><strong>Unstable system</strong>: absolute necessity of high-performance control</li>
<li><strong>Multidisciplinary</strong>: mechanics + electronics + control</li>
<li><strong>Technical challenge</strong>: real-time balancing with hardware constraints</li>
</ul>

<p><strong>Connections with other courses</strong>:</p>

<p>Control engineering is a cross-disciplinary field that builds upon many other courses:</p>
<ul>
<li><strong>Analog Circuits and Filters</strong> (S5): frequency analysis, Bode diagrams</li>
<li><strong>Digital Electronics Fundamentals</strong> (S5): sampling for digital control</li>
<li><strong>Closed-Loop Systems</strong> (S5): servomechanisms, PID controllers (complementary approach)</li>
<li><strong>Digital Control</strong> (S8): discretization, sampled-data control, microcontrollers</li>
<li><strong>Real-Time Systems</strong> (S8): implementation of control laws with timing constraints</li>
<li><strong>Stochastic Processes</strong> (S8): Kalman filter (stochastic extension of the observer)</li>
</ul>

<p><strong>Technological evolution</strong>:</p>

<p>Control engineering is evolving rapidly with new technologies:</p>

<p><strong>Current trends</strong>:</p>
<ul>
<li><strong>Machine learning</strong>: hybridization of classical control + AI (Deep Reinforcement Learning)</li>
<li><strong>Predictive control</strong>: MPC (Model Predictive Control) in automotive and industry</li>
<li><strong>Distributed systems</strong>: multi-agent control, drone swarms</li>
<li><strong>Real-time optimization</strong>: high-performance embedded computing (DSP, FPGA)</li>
</ul>

<p><strong>Emerging applications</strong>:</p>
<ul>
<li><strong>Autonomous vehicles</strong>: longitudinal/lateral control, trajectory planning</li>
<li><strong>Drones</strong>: stabilization, trajectory tracking, formation flight</li>
<li><strong>Exoskeletons</strong>: robotic assistance, rehabilitation</li>
<li><strong>Industry 4.0</strong>: cobots (collaborative robots), predictive maintenance</li>
</ul>

<p><strong>Recommendations for success</strong>:</p>
<ol>
<li><strong>Understand before computing</strong>: visualize the physical behavior of the system</li>
<li><strong>Master MATLAB</strong>: essential for control engineering (industry + research)</li>
<li><strong>Think in "states"</strong>: reason in terms of state variables rather than inputs/outputs</li>
<li><strong>Simulate systematically</strong>: validate calculations before real-world implementation</li>
<li><strong>Account for limitations</strong>: saturation, noise, sampling</li>
</ol>

<p><strong>Professional applications</strong>:</p>

<p>These skills are highly sought after in many sectors:</p>

<p><strong>Automotive</strong>:</p>
<ul>
<li>ADAS systems (Advanced Driver Assistance Systems): ESP, ABS, adaptive cruise control</li>
<li>Autonomous vehicles: trajectory control, sensor fusion</li>
<li>Hybrid/electric powertrains: energy management, traction control</li>
</ul>

<p><strong>Aerospace</strong>:</p>
<ul>
<li>Autopilot for aircraft, drones, rockets</li>
<li>Satellite stabilization, attitude control</li>
<li>Launch vehicles: guidance, navigation, control</li>
</ul>

<p><strong>Robotics</strong>:</p>
<ul>
<li>Mobile robots: navigation, obstacle avoidance</li>
<li>Robotic manipulators: trajectory control, force control</li>
<li>Humanoid robots: balancing, dynamic walking</li>
</ul>

<p><strong>Industry</strong>:</p>
<ul>
<li>Process automation: chemistry, petrochemistry, food industry</li>
<li>Machine tools: precise positioning, machining</li>
<li>Renewable energies: MPPT for PV, wind turbine control</li>
</ul>

<p><strong>Career prospects</strong>:</p>
<ul>
<li>Control engineer: design of control systems</li>
<li>Embedded systems engineer: real-time implementation</li>
<li>R&amp;D engineer: advanced control algorithms</li>
<li>Consultant: control engineering expertise for various sectors</li>
</ul>

<hr/>

<p><strong>Personal assessment</strong>: This course provided the mathematical and practical tools to analyze and control linear dynamic systems. The state-space approach is a powerful methodology for multivariable systems and modern control. The MATLAB lab sessions and the robot project allowed these theoretical concepts to be applied to real-world control applications. It is a demanding but absolutely fundamental course for a career in control engineering, robotics, or embedded systems.</p>

</div>

<div class="back-nav">
  <a href="./my-courses-2022-2023.html" data-i18n-html="back-courses-2022-2023">&larr; Retour aux Cours 2022-2023</a>
</div>

<em class="lang-fr">Redige par Cedric Chanfreau</em><em class="lang-en">Written by Cedric Chanfreau</em>

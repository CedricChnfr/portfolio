---
layout: default
title: "Modélisation et Commande des Systèmes Linéaires Continus - S5"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
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
  <a href="./my-courses-2022-2023.html">← Retour à Mes Cours 2022-2023</a>
</div>

<div class="lang-fr">

<h1>Modelisation et Commande des Systemes Lineaires Continus - S5</h1>

<p><strong>Annee</strong>: 2022-2023 (Semestre 5)<br/>
<strong>Credits</strong>: 3 ECTS<br/>
<strong>Type</strong>: Automatique et Systemes<br/>
<strong>Enseignant</strong>: Subias</p>

<hr/>

<h2>PART A: PRESENTATION GENERALE</h2>

<h3>Objectifs du cours</h3>

<p>Ce cours approfondit la commande des systemes lineaires continus avec une approche complementaire au cours de representation d'etat. Il se concentre sur les techniques de commande classiques (PID, correcteurs frequentiels) et leur application pratique sur des systemes reels. Le cours couvre la modelisation de systemes physiques, l'analyse de stabilite et de performances, ainsi que la conception de lois de commande adaptees.</p>

<h3>Competences visees</h3>

<ul>
  <li>Modeliser des systemes physiques continus (mecaniques, electriques, thermiques)</li>
  <li>Concevoir et regler des correcteurs PID pour des applications industrielles</li>
  <li>Analyser la stabilite par methodes frequentielles (Bode, Nyquist)</li>
  <li>Dimensionner des compensateurs (avance, retard de phase)</li>
  <li>Utiliser MATLAB/Simulink pour la simulation et l'analyse</li>
  <li>Evaluer les performances temporelles et frequentielles</li>
  <li>Implementer des lois de commande sur systemes reels</li>
</ul>

<h3>Organisation</h3>

<ul>
  <li><strong>Volume horaire</strong>: Cours magistraux, TD et TP MATLAB/Simulink</li>
  <li><strong>Evaluation</strong>: Examen ecrit, TPs notes, Projet robot</li>
  <li><strong>Semestre</strong>: 5 (2022-2023)</li>
  <li><strong>Prerequis</strong>: Transformee de Laplace, systemes du 1er et 2nd ordre, algebre</li>
</ul>

<hr/>

<h2>PART B: EXPERIENCE, CONTEXTE ET FONCTION</h2>

<h3>Contenu pedagogique</h3>

<p>Le cours se structure autour de la modelisation, l'analyse et la commande de systemes continus.</p>

<h4>1. Modelisation de Systemes Physiques</h4>

<p><strong>Systemes mecaniques</strong>:</p>

<p>Systeme masse-ressort-amortisseur:</p>
<ul>
  <li>m : masse</li>
  <li>k : raideur du ressort</li>
  <li>f : coefficient d'amortissement</li>
</ul>

<p>Equation: m x d²x/dt² + f x dx/dt + k x x = F(t)</p>

<p>Fonction de transfert: H(s) = 1 / (m x s² + f x s + k)</p>

<p><strong>Systemes electriques (circuit RLC)</strong>:</p>

<p>Equation: L x d²i/dt² + R x di/dt + i/C = dV/dt</p>

<p>Similitude avec systeme mecanique (L &harr; m, R &harr; f, 1/C &harr; k).</p>

<p><strong>Moteur a courant continu</strong>:</p>

<p>Modele simplifie du TP:</p>
<ul>
  <li>Constante de temps: Tm = 0.3s</li>
  <li>Gain: Km = 47.8</li>
  <li>Fonction de transfert: H(s) = Km / (Tm x s + 1)</li>
</ul>

<h4>2. Analyse Temporelle</h4>

<p><strong>Reponse indicielle d'un systeme du 2nd ordre</strong>:</p>

<p>Parametres caracteristiques:</p>
<ul>
  <li>Temps de montee (rise time)</li>
  <li>Depassement (overshoot): D = exp(-pi x zeta / sqrt(1-zeta²))</li>
  <li>Temps de reponse a 5% (settling time)</li>
  <li>Erreur statique</li>
</ul>

<p>Pour un systeme bien amorti: zeta = 0.7 donne D &approx; 5%.</p>

<p><strong>Classe d'un systeme</strong>:</p>

<p>Determine l'erreur statique selon le type d'entree:</p>
<ul>
  <li>Classe 0: erreur pour echelon</li>
  <li>Classe 1: erreur pour rampe</li>
  <li>Classe 2: erreur pour parabole</li>
</ul>

<h4>3. Analyse Frequentielle</h4>

<p><strong>Diagrammes de Bode (TP1)</strong>:</p>

<p>Representation du gain et de la phase en fonction de la frequence.</p>

<p>Systeme identifie experimentalement: H(s) = 0.717 / (0.0033 x s + 1)</p>

<p>Mesures realisees:</p>
<ul>
  <li>Frequences: 0.05 Hz a 10 Hz</li>
  <li>Gain: de -3.5 dB a -24 dB</li>
  <li>Phase: de -2.2 deg a -90 deg</li>
</ul>

<p><strong>Marges de stabilite (TP2)</strong>:</p>

<p><strong>Marge de gain (Gm)</strong>: gain supplementaire avant instabilite.</p>

<p><strong>Marge de phase (Pm)</strong>: phase supplementaire avant instabilite.</p>

<p>Criteres de robustesse:</p>
<ul>
  <li>Pm &gt; 45 deg : bon amortissement</li>
  <li>Gm &gt; 6 dB : bonne marge</li>
</ul>

<p>Commande MATLAB:</p>
<pre><code>[Gm, Pm, Wcg, Wcp] = margin(sys);</code></pre>

<p>Resultats typiques du TP: Pm &approx; 60 deg (systeme robuste).</p>

<p><strong>Diagramme de Nyquist</strong>:</p>

<p>Trace de H(j&omega;) dans le plan complexe.</p>

<p>Critere de Nyquist: nombre d'encerclements du point critique (-1, 0) determine la stabilite.</p>

<h4>4. Commande PID</h4>

<p><strong>Structure du PID</strong>:</p>

<p>Correcteur Proportionnel-Integral-Derive:</p>

<p>u(t) = Kp x e(t) + Ki x &int;e(t)dt + Kd x de(t)/dt</p>

<p>En transfert: C(s) = Kp + Ki/s + Kd x s</p>

<p><strong>Actions du PID</strong>:</p>

<table>
  <thead>
    <tr><th>Action</th><th>Effet</th><th>Utilisation</th></tr>
  </thead>
  <tbody>
    <tr><td>P (Proportionnel)</td><td>Reduit l'erreur, augmente rapidite</td><td>Toujours present</td></tr>
    <tr><td>I (Integral)</td><td>Annule erreur statique</td><td>Erreur permanente</td></tr>
    <tr><td>D (Derive)</td><td>Reduit depassement, ameliore stabilite</td><td>Systemes oscillants</td></tr>
  </tbody>
</table>

<p><strong>Reglage par Ziegler-Nichols</strong>:</p>

<p>Methode empirique pour determiner Kp, Ki, Kd:</p>
<ol>
  <li>Mettre Ki = 0, Kd = 0</li>
  <li>Augmenter Kp jusqu'a oscillations (Kp critique)</li>
  <li>Mesurer periode d'oscillation Tu</li>
  <li>Appliquer les formules de reglage</li>
</ol>

<p>Pour PID: Kp = 0.6 x Kpcritique, Ti = 0.5 x Tu, Td = 0.125 x Tu.</p>

<p><strong>Limitation anti-windup</strong>:</p>

<p>Probleme: l'integrale continue a s'accumuler meme si la commande sature.</p>

<p>Solution: limiter l'integrateur quand la sortie sature.</p>

<h4>5. Correcteurs Frequentiels</h4>

<p><strong>Correcteur a avance de phase</strong>:</p>

<p>Forme: C(s) = K x (1 + a x T x s) / (1 + T x s) avec a &gt; 1</p>

<p>Effet: augmente la marge de phase, ameliore rapidite.</p>

<p>Utilise quand: systeme trop lent ou marge de phase insuffisante.</p>

<p><strong>Correcteur a retard de phase</strong>:</p>

<p>Forme: C(s) = K x (1 + T x s) / (1 + a x T x s) avec a &gt; 1</p>

<p>Effet: augmente la marge de gain, reduit erreur statique.</p>

<p>Utilise quand: erreur statique trop importante.</p>

<p><strong>Correcteur avance-retard</strong>:</p>

<p>Combinaison des deux pour ameliorer simultanement rapidite et precision.</p>

<h4>6. Projet Robot Auto-Equilibre</h4>

<p><strong>Systeme du pendule inverse</strong>:</p>

<p>Modelisation du robot NXT Way (Lego Mindstorms):</p>

<p>Parametres physiques:</p>
<ul>
  <li>Masse roues: m = 0.03 kg</li>
  <li>Rayon roues: R = 0.042 m</li>
  <li>Masse corps: M = 0.67 kg</li>
  <li>Hauteur: H = 0.152 m</li>
  <li>Gravite: g = 9.81 m/s²</li>
</ul>

<p><strong>Objectif</strong>: maintenir le robot en equilibre vertical (angle &theta; = 0 deg).</p>

<p><strong>Strategie de commande</strong>:</p>

<p>Systeme instable en boucle ouverte &rarr; necessite commande active.</p>

<p>Approches possibles:</p>
<ul>
  <li>Retour d'etat (placement de poles)</li>
  <li>Correcteur PID sur l'angle</li>
  <li>Observateur pour estimer vitesse angulaire</li>
</ul>

<p><strong>Simulation Simulink</strong>:</p>

<p>Fichiers du projet:</p>
<ul>
  <li>NXTwaySim.slx: modele complet du robot</li>
  <li>NXP_robot_parameters.m: parametres physiques</li>
  <li>PlayAnimation.m: visualisation 3D</li>
</ul>

<p>Tests effectues:</p>
<ul>
  <li>Stabilisation apres perturbation</li>
  <li>Robustesse aux variations de parametres</li>
  <li>Rejection de perturbations externes</li>
</ul>

<hr/>

<h2>PART C: ASPECTS TECHNIQUES</h2>

<h3>Travaux Pratiques MATLAB</h3>

<p><strong>TP1: Identification experimentale</strong>:</p>

<p>Objectif: determiner la fonction de transfert d'un systeme reel a partir de mesures frequentielles.</p>

<p>Donnees mesurees (gains et phases a differentes frequences):</p>
<pre><code>freq = [0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 7.5, 10];
G = [0.669, 0.659, 0.609, 0.528, 0.396, 0.242, 0.119, 0.083, 0.061];</code></pre>

<p>Trace du diagramme de Bode:</p>
<pre><code>G_dB = 20*log10(G);
semilogx(freq, G_dB);
xlabel('Frequence (Hz)');
ylabel('Gain (dB)');</code></pre>

<p>Modele identifie: systeme du 1er ordre avec gain 0.717 et constante de temps 3.3 ms.</p>

<p><strong>TP2: Analyse de stabilite</strong>:</p>

<p>Systeme en boucle fermee avec capteur et moteur:</p>
<pre><code>Ks = 1.55;   % Gain capteur
Km = 47.8;   % Gain moteur
Tm = 0.3;    % Constante de temps

num = [Km*K/9];
den = [Tm, 1, Km*K*Ks/9];
sys = tf(num, den);

[Gm, Pm, Wcg, Wcp] = margin(sys);</code></pre>

<p>Analyse des poles:</p>
<pre><code>P = pole(sys);</code></pre>

<p>Si partie reelle negative &rarr; systeme stable.</p>

<p><strong>TP3: Commande par retour d'etat</strong>:</p>

<p>Systeme d'ordre 2:</p>
<pre><code>A = [0 1; -10 -6.316];
B = [0; 1];
C = [k/0.1001 0];

% Placement de poles
poles_desired = [-2+2i, -2-2i];
K = place(A, B, poles_desired);

% Simulation
sys_cl = ss(A-B*K, B, C, 0);
step(sys_cl);</code></pre>

<p>Choix des poles selon performances souhaitees:</p>
<ul>
  <li>Partie reelle: rapidite</li>
  <li>Partie imaginaire: oscillations</li>
</ul>

<h3>Outils MATLAB Essentiels</h3>

<p><strong>Creation de modeles</strong>:</p>
<pre><code>sys = tf(num, den);        % Fonction de transfert
sys = ss(A, B, C, D);      % Representation d'etat</code></pre>

<p><strong>Analyse</strong>:</p>
<pre><code>pole(sys);                 % Poles
zero(sys);                 % Zeros
step(sys);                 % Reponse indicielle
bode(sys);                 % Diagramme de Bode
nyquist(sys);              % Diagramme de Nyquist
margin(sys);               % Marges de stabilite</code></pre>

<p><strong>Conception</strong>:</p>
<pre><code>K = place(A, B, poles);    % Placement de poles
pidtune(sys, 'PID');       % Reglage PID automatique</code></pre>

<h3>Methodologie de Conception</h3>

<p><strong>Etapes de conception d'un asservissement</strong>:</p>

<ol>
  <li><strong>Modelisation</strong>: obtenir H(s) du systeme</li>
  <li><strong>Analyse BO</strong>: stabilite, performances en boucle ouverte</li>
  <li><strong>Specifications</strong>: definir depassement, temps de reponse, erreur admissible</li>
  <li><strong>Choix correcteur</strong>: PID, avance/retard selon besoins</li>
  <li><strong>Reglage</strong>: calcul des parametres (Kp, Ki, Kd)</li>
  <li><strong>Simulation</strong>: validation avec Simulink</li>
  <li><strong>Tests</strong>: robustesse, perturbations, variations parametres</li>
</ol>

<p><strong>Compromis a gerer</strong>:</p>
<ul>
  <li>Rapidite vs stabilite</li>
  <li>Precision vs robustesse</li>
  <li>Complexite vs performances</li>
</ul>

<hr/>

<h2>PART D: ANALYSE ET REFLEXION</h2>

<h3>Competences acquises</h3>

<p><strong>Modelisation</strong>:</p>
<ul>
  <li>Passage du systeme physique au modele mathematique</li>
  <li>Identification experimentale de parametres</li>
  <li>Validation par comparaison mesures/simulation</li>
</ul>

<p><strong>Analyse</strong>:</p>
<ul>
  <li>Stabilite par Routh, Bode, Nyquist</li>
  <li>Performances temporelles et frequentielles</li>
  <li>Evaluation de robustesse (marges)</li>
</ul>

<p><strong>Commande</strong>:</p>
<ul>
  <li>Conception de correcteurs PID</li>
  <li>Reglage par methodes empiriques et theoriques</li>
  <li>Placement de poles pour specifications donnees</li>
</ul>

<p><strong>Outils</strong>:</p>
<ul>
  <li>Maitrise de MATLAB/Simulink</li>
  <li>Interpretation de diagrammes (Bode, Nyquist)</li>
  <li>Simulation et validation</li>
</ul>

<h3>Applications pratiques</h3>

<p>Les techniques de ce cours s'appliquent a de nombreux domaines:</p>

<p><strong>Industrie</strong>:</p>
<ul>
  <li>Regulation de temperature, pression, debit</li>
  <li>Controle de vitesse de moteurs</li>
  <li>Positionnement de systemes mecaniques</li>
</ul>

<p><strong>Robotique</strong>:</p>
<ul>
  <li>Stabilisation (pendule inverse, robot equilibre)</li>
  <li>Suivi de trajectoire</li>
  <li>Controle de force</li>
</ul>

<p><strong>Aeronautique</strong>:</p>
<ul>
  <li>Pilote automatique</li>
  <li>Stabilisation d'attitude</li>
  <li>Controle de vol</li>
</ul>

<p><strong>Automobile</strong>:</p>
<ul>
  <li>Regulateur de vitesse (cruise control)</li>
  <li>Suspension active</li>
  <li>Controle de moteur</li>
</ul>

<h3>Liens avec autres cours</h3>

<table>
  <thead>
    <tr><th>Cours</th><th>Lien</th></tr>
  </thead>
  <tbody>
    <tr><td>Circuits et Filtres Analogiques (S5)</td><td>Analyse frequentielle, Bode</td></tr>
    <tr><td>Modelisation Systemes Lineaires (S5)</td><td>Representation d'etat</td></tr>
    <tr><td>Systemes Boucles (S5)</td><td>Asservissements</td></tr>
    <tr><td>Commande Numerique (S8)</td><td>Discretisation, PID numerique</td></tr>
    <tr><td>Temps Reel (S8)</td><td>Implementation des lois de commande</td></tr>
  </tbody>
</table>

<h3>Mon opinion</h3>

<p>Ce cours est complementaire au cours de representation d'etat en apportant les outils classiques de l'automatique industrielle.</p>

<p><strong>Points forts</strong>:</p>
<ul>
  <li>Approche tres pratique (PID, reglages empiriques)</li>
  <li>Outils directement utilisables en industrie</li>
  <li>TPs concrets avec identification et commande</li>
  <li>Projet robot motivant et formateur</li>
</ul>

<p><strong>Complementarite</strong>:</p>
<p>Le PID reste le correcteur le plus utilise industriellement (&gt;90% des boucles de regulation). La representation d'etat apporte la theorie moderne, le PID apporte la pratique immediate.</p>

<p><strong>Importance professionnelle</strong>:</p>
<p>Competences tres recherchees dans l'automatisation industrielle, la robotique et les systemes embarques. Le reglage de PID est une competence de base pour tout ingenieur en automatique.</p>

<hr/>

<p><strong>Bilan personnel</strong>: Ce cours a apporte les techniques classiques et eprouvees de l'automatique. La complementarite avec l'approche moderne (etat) offre une boite a outils complete. Les TPs MATLAB et le projet robot ont permis d'appliquer concretement ces concepts sur des systemes reels, preparant bien aux applications industrielles.</p>

<hr/>

<h2>Rapports et Projets</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Compte Rendu TP1 - Identification et Analyse Frequentielle</h4>
      <p>Rapport de TP sur l'identification experimentale de systemes, trace de diagrammes de Bode et analyse de stabilite avec MATLAB.</p>
      <p style="text-align: center;">
        <a href="/file/reports/S5/CHANFREAU_JUMIN_Compte_rendu_TP1.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Telecharger le rapport PDF
        </a>
      </p>
    </div>
    <div class="pdf-item">
      <h4>Compte Rendu TP3 - Commande par Retour d'Etat</h4>
      <p>Rapport de TP sur la commande de systemes lineaires continus : placement de poles, simulation Simulink et validation experimentale.</p>
      <p style="text-align: center;">
        <a href="/file/reports/S5/Compte_Rendu_TP3_Commande_JUMIN_CHANFREAU.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Telecharger le rapport PDF
        </a>
      </p>
    </div>
  </div>
</div>

</div>

<div class="lang-en">

<h1>Modeling and Control of Continuous Linear Systems - S5</h1>

<p><strong>Year</strong>: 2022-2023 (Semester 5)<br/>
<strong>Credits</strong>: 3 ECTS<br/>
<strong>Type</strong>: Control Systems and Automation<br/>
<strong>Instructor</strong>: Subias</p>

<hr/>

<h2>PART A: GENERAL OVERVIEW</h2>

<h3>Course Objectives</h3>

<p>This course deepens the study of continuous linear system control with an approach complementary to the state-space representation course. It focuses on classical control techniques (PID, frequency-domain controllers) and their practical application to real systems. The course covers physical system modeling, stability and performance analysis, as well as the design of suitable control laws.</p>

<h3>Target Skills</h3>

<ul>
  <li>Model continuous physical systems (mechanical, electrical, thermal)</li>
  <li>Design and tune PID controllers for industrial applications</li>
  <li>Analyze stability using frequency-domain methods (Bode, Nyquist)</li>
  <li>Size compensators (lead, lag phase)</li>
  <li>Use MATLAB/Simulink for simulation and analysis</li>
  <li>Evaluate time-domain and frequency-domain performance</li>
  <li>Implement control laws on real systems</li>
</ul>

<h3>Organization</h3>

<ul>
  <li><strong>Hours</strong>: Lectures, tutorials and MATLAB/Simulink lab sessions</li>
  <li><strong>Assessment</strong>: Written exam, graded lab sessions, Robot project</li>
  <li><strong>Semester</strong>: 5 (2022-2023)</li>
  <li><strong>Prerequisites</strong>: Laplace transform, 1st and 2nd order systems, algebra</li>
</ul>

<hr/>

<h2>PART B: EXPERIENCE, CONTEXT AND FUNCTION</h2>

<h3>Pedagogical Content</h3>

<p>The course is structured around modeling, analysis and control of continuous systems.</p>

<h4>1. Physical System Modeling</h4>

<p><strong>Mechanical systems</strong>:</p>

<p>Mass-spring-damper system:</p>
<ul>
  <li>m: mass</li>
  <li>k: spring stiffness</li>
  <li>f: damping coefficient</li>
</ul>

<p>Equation: m x d²x/dt² + f x dx/dt + k x x = F(t)</p>

<p>Transfer function: H(s) = 1 / (m x s² + f x s + k)</p>

<p><strong>Electrical systems (RLC circuit)</strong>:</p>

<p>Equation: L x d²i/dt² + R x di/dt + i/C = dV/dt</p>

<p>Analogy with mechanical system (L &harr; m, R &harr; f, 1/C &harr; k).</p>

<p><strong>DC motor</strong>:</p>

<p>Simplified lab model:</p>
<ul>
  <li>Time constant: Tm = 0.3s</li>
  <li>Gain: Km = 47.8</li>
  <li>Transfer function: H(s) = Km / (Tm x s + 1)</li>
</ul>

<h4>2. Time-Domain Analysis</h4>

<p><strong>Step response of a 2nd order system</strong>:</p>

<p>Characteristic parameters:</p>
<ul>
  <li>Rise time</li>
  <li>Overshoot: D = exp(-pi x zeta / sqrt(1-zeta²))</li>
  <li>5% settling time</li>
  <li>Steady-state error</li>
</ul>

<p>For a well-damped system: zeta = 0.7 gives D &approx; 5%.</p>

<p><strong>System type</strong>:</p>

<p>Determines the steady-state error depending on input type:</p>
<ul>
  <li>Type 0: error for step input</li>
  <li>Type 1: error for ramp input</li>
  <li>Type 2: error for parabolic input</li>
</ul>

<h4>3. Frequency-Domain Analysis</h4>

<p><strong>Bode diagrams (Lab 1)</strong>:</p>

<p>Representation of gain and phase as a function of frequency.</p>

<p>Experimentally identified system: H(s) = 0.717 / (0.0033 x s + 1)</p>

<p>Measurements taken:</p>
<ul>
  <li>Frequencies: 0.05 Hz to 10 Hz</li>
  <li>Gain: from -3.5 dB to -24 dB</li>
  <li>Phase: from -2.2 deg to -90 deg</li>
</ul>

<p><strong>Stability margins (Lab 2)</strong>:</p>

<p><strong>Gain margin (Gm)</strong>: additional gain before instability.</p>

<p><strong>Phase margin (Pm)</strong>: additional phase before instability.</p>

<p>Robustness criteria:</p>
<ul>
  <li>Pm &gt; 45 deg: good damping</li>
  <li>Gm &gt; 6 dB: good margin</li>
</ul>

<p>MATLAB command:</p>
<pre><code>[Gm, Pm, Wcg, Wcp] = margin(sys);</code></pre>

<p>Typical lab results: Pm &approx; 60 deg (robust system).</p>

<p><strong>Nyquist diagram</strong>:</p>

<p>Plot of H(j&omega;) in the complex plane.</p>

<p>Nyquist criterion: the number of encirclements of the critical point (-1, 0) determines stability.</p>

<h4>4. PID Control</h4>

<p><strong>PID structure</strong>:</p>

<p>Proportional-Integral-Derivative controller:</p>

<p>u(t) = Kp x e(t) + Ki x &int;e(t)dt + Kd x de(t)/dt</p>

<p>Transfer form: C(s) = Kp + Ki/s + Kd x s</p>

<p><strong>PID actions</strong>:</p>

<table>
  <thead>
    <tr><th>Action</th><th>Effect</th><th>Usage</th></tr>
  </thead>
  <tbody>
    <tr><td>P (Proportional)</td><td>Reduces error, increases speed</td><td>Always present</td></tr>
    <tr><td>I (Integral)</td><td>Eliminates steady-state error</td><td>Permanent error</td></tr>
    <tr><td>D (Derivative)</td><td>Reduces overshoot, improves stability</td><td>Oscillating systems</td></tr>
  </tbody>
</table>

<p><strong>Ziegler-Nichols tuning</strong>:</p>

<p>Empirical method to determine Kp, Ki, Kd:</p>
<ol>
  <li>Set Ki = 0, Kd = 0</li>
  <li>Increase Kp until oscillations (critical Kp)</li>
  <li>Measure oscillation period Tu</li>
  <li>Apply tuning formulas</li>
</ol>

<p>For PID: Kp = 0.6 x Kp_critical, Ti = 0.5 x Tu, Td = 0.125 x Tu.</p>

<p><strong>Anti-windup limitation</strong>:</p>

<p>Problem: the integral keeps accumulating even when the control signal saturates.</p>

<p>Solution: limit the integrator when the output saturates.</p>

<h4>5. Frequency-Domain Controllers</h4>

<p><strong>Lead compensator</strong>:</p>

<p>Form: C(s) = K x (1 + a x T x s) / (1 + T x s) with a &gt; 1</p>

<p>Effect: increases phase margin, improves speed.</p>

<p>Used when: system is too slow or phase margin is insufficient.</p>

<p><strong>Lag compensator</strong>:</p>

<p>Form: C(s) = K x (1 + T x s) / (1 + a x T x s) with a &gt; 1</p>

<p>Effect: increases gain margin, reduces steady-state error.</p>

<p>Used when: steady-state error is too large.</p>

<p><strong>Lead-lag compensator</strong>:</p>

<p>Combination of both to simultaneously improve speed and precision.</p>

<h4>6. Self-Balancing Robot Project</h4>

<p><strong>Inverted pendulum system</strong>:</p>

<p>Modeling of the NXT Way robot (Lego Mindstorms):</p>

<p>Physical parameters:</p>
<ul>
  <li>Wheel mass: m = 0.03 kg</li>
  <li>Wheel radius: R = 0.042 m</li>
  <li>Body mass: M = 0.67 kg</li>
  <li>Height: H = 0.152 m</li>
  <li>Gravity: g = 9.81 m/s²</li>
</ul>

<p><strong>Objective</strong>: keep the robot in vertical balance (angle &theta; = 0 deg).</p>

<p><strong>Control strategy</strong>:</p>

<p>Open-loop unstable system &rarr; requires active control.</p>

<p>Possible approaches:</p>
<ul>
  <li>State feedback (pole placement)</li>
  <li>PID controller on the angle</li>
  <li>Observer to estimate angular velocity</li>
</ul>

<p><strong>Simulink simulation</strong>:</p>

<p>Project files:</p>
<ul>
  <li>NXTwaySim.slx: complete robot model</li>
  <li>NXP_robot_parameters.m: physical parameters</li>
  <li>PlayAnimation.m: 3D visualization</li>
</ul>

<p>Tests performed:</p>
<ul>
  <li>Stabilization after perturbation</li>
  <li>Robustness to parameter variations</li>
  <li>External disturbance rejection</li>
</ul>

<hr/>

<h2>PART C: TECHNICAL ASPECTS</h2>

<h3>MATLAB Lab Sessions</h3>

<p><strong>Lab 1: Experimental identification</strong>:</p>

<p>Objective: determine the transfer function of a real system from frequency measurements.</p>

<p>Measured data (gains and phases at various frequencies):</p>
<pre><code>freq = [0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 7.5, 10];
G = [0.669, 0.659, 0.609, 0.528, 0.396, 0.242, 0.119, 0.083, 0.061];</code></pre>

<p>Bode diagram plot:</p>
<pre><code>G_dB = 20*log10(G);
semilogx(freq, G_dB);
xlabel('Frequency (Hz)');
ylabel('Gain (dB)');</code></pre>

<p>Identified model: 1st order system with gain 0.717 and time constant 3.3 ms.</p>

<p><strong>Lab 2: Stability analysis</strong>:</p>

<p>Closed-loop system with sensor and motor:</p>
<pre><code>Ks = 1.55;   % Sensor gain
Km = 47.8;   % Motor gain
Tm = 0.3;    % Time constant

num = [Km*K/9];
den = [Tm, 1, Km*K*Ks/9];
sys = tf(num, den);

[Gm, Pm, Wcg, Wcp] = margin(sys);</code></pre>

<p>Pole analysis:</p>
<pre><code>P = pole(sys);</code></pre>

<p>If real part is negative &rarr; system is stable.</p>

<p><strong>Lab 3: State feedback control</strong>:</p>

<p>2nd order system:</p>
<pre><code>A = [0 1; -10 -6.316];
B = [0; 1];
C = [k/0.1001 0];

% Pole placement
poles_desired = [-2+2i, -2-2i];
K = place(A, B, poles_desired);

% Simulation
sys_cl = ss(A-B*K, B, C, 0);
step(sys_cl);</code></pre>

<p>Pole selection based on desired performance:</p>
<ul>
  <li>Real part: speed</li>
  <li>Imaginary part: oscillations</li>
</ul>

<h3>Essential MATLAB Tools</h3>

<p><strong>Model creation</strong>:</p>
<pre><code>sys = tf(num, den);        % Transfer function
sys = ss(A, B, C, D);      % State-space representation</code></pre>

<p><strong>Analysis</strong>:</p>
<pre><code>pole(sys);                 % Poles
zero(sys);                 % Zeros
step(sys);                 % Step response
bode(sys);                 % Bode diagram
nyquist(sys);              % Nyquist diagram
margin(sys);               % Stability margins</code></pre>

<p><strong>Design</strong>:</p>
<pre><code>K = place(A, B, poles);    % Pole placement
pidtune(sys, 'PID');       % Automatic PID tuning</code></pre>

<h3>Design Methodology</h3>

<p><strong>Steps for designing a control system</strong>:</p>

<ol>
  <li><strong>Modeling</strong>: obtain H(s) of the system</li>
  <li><strong>Open-loop analysis</strong>: stability, open-loop performance</li>
  <li><strong>Specifications</strong>: define overshoot, settling time, allowable error</li>
  <li><strong>Controller selection</strong>: PID, lead/lag as needed</li>
  <li><strong>Tuning</strong>: parameter calculation (Kp, Ki, Kd)</li>
  <li><strong>Simulation</strong>: validation with Simulink</li>
  <li><strong>Testing</strong>: robustness, disturbances, parameter variations</li>
</ol>

<p><strong>Trade-offs to manage</strong>:</p>
<ul>
  <li>Speed vs stability</li>
  <li>Precision vs robustness</li>
  <li>Complexity vs performance</li>
</ul>

<hr/>

<h2>PART D: ANALYSIS AND REFLECTION</h2>

<h3>Acquired Skills</h3>

<p><strong>Modeling</strong>:</p>
<ul>
  <li>Going from physical system to mathematical model</li>
  <li>Experimental parameter identification</li>
  <li>Validation through measurement/simulation comparison</li>
</ul>

<p><strong>Analysis</strong>:</p>
<ul>
  <li>Stability via Routh, Bode, Nyquist</li>
  <li>Time-domain and frequency-domain performance</li>
  <li>Robustness evaluation (margins)</li>
</ul>

<p><strong>Control</strong>:</p>
<ul>
  <li>PID controller design</li>
  <li>Tuning via empirical and theoretical methods</li>
  <li>Pole placement for given specifications</li>
</ul>

<p><strong>Tools</strong>:</p>
<ul>
  <li>Proficiency in MATLAB/Simulink</li>
  <li>Interpretation of diagrams (Bode, Nyquist)</li>
  <li>Simulation and validation</li>
</ul>

<h3>Practical Applications</h3>

<p>The techniques from this course apply to many fields:</p>

<p><strong>Industry</strong>:</p>
<ul>
  <li>Temperature, pressure, and flow regulation</li>
  <li>Motor speed control</li>
  <li>Mechanical system positioning</li>
</ul>

<p><strong>Robotics</strong>:</p>
<ul>
  <li>Stabilization (inverted pendulum, balanced robot)</li>
  <li>Trajectory tracking</li>
  <li>Force control</li>
</ul>

<p><strong>Aerospace</strong>:</p>
<ul>
  <li>Autopilot</li>
  <li>Attitude stabilization</li>
  <li>Flight control</li>
</ul>

<p><strong>Automotive</strong>:</p>
<ul>
  <li>Cruise control</li>
  <li>Active suspension</li>
  <li>Engine control</li>
</ul>

<h3>Links with Other Courses</h3>

<table>
  <thead>
    <tr><th>Course</th><th>Link</th></tr>
  </thead>
  <tbody>
    <tr><td>Analog Circuits and Filters (S5)</td><td>Frequency analysis, Bode</td></tr>
    <tr><td>Linear System Modeling (S5)</td><td>State-space representation</td></tr>
    <tr><td>Feedback Systems (S5)</td><td>Servo control</td></tr>
    <tr><td>Digital Control (S8)</td><td>Discretization, digital PID</td></tr>
    <tr><td>Real-Time Systems (S8)</td><td>Control law implementation</td></tr>
  </tbody>
</table>

<h3>My Opinion</h3>

<p>This course complements the state-space representation course by providing the classical tools of industrial control.</p>

<p><strong>Strengths</strong>:</p>
<ul>
  <li>Very practical approach (PID, empirical tuning)</li>
  <li>Tools directly usable in industry</li>
  <li>Hands-on lab sessions with identification and control</li>
  <li>Motivating and educational robot project</li>
</ul>

<p><strong>Complementarity</strong>:</p>
<p>The PID remains the most widely used controller in industry (&gt;90% of regulation loops). State-space representation provides modern theory, while PID provides immediate practice.</p>

<p><strong>Professional importance</strong>:</p>
<p>Highly sought-after skills in industrial automation, robotics and embedded systems. PID tuning is a fundamental skill for any control engineer.</p>

<hr/>

<p><strong>Personal assessment</strong>: This course provided the classical and proven techniques of control engineering. The complementarity with the modern approach (state-space) offers a complete toolbox. The MATLAB labs and robot project allowed for concrete application of these concepts on real systems, providing good preparation for industrial applications.</p>

<hr/>

<h2>Reports and Projects</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Lab Report 1 - Identification and Frequency Analysis</h4>
      <p>Lab report on experimental system identification, Bode diagram plotting and stability analysis with MATLAB.</p>
      <p style="text-align: center;">
        <a href="/file/reports/S5/CHANFREAU_JUMIN_Compte_rendu_TP1.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Download PDF report
        </a>
      </p>
    </div>
    <div class="pdf-item">
      <h4>Lab Report 3 - State Feedback Control</h4>
      <p>Lab report on continuous linear system control: pole placement, Simulink simulation and experimental validation.</p>
      <p style="text-align: center;">
        <a href="/file/reports/S5/Compte_Rendu_TP3_Commande_JUMIN_CHANFREAU.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Download PDF report
        </a>
      </p>
    </div>
  </div>
</div>

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

<style>
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
</style>

---
layout: default
title: "Commande Numerique - S8"
date: 2024-10-02 10:56:03 +0200
---

<style>
.back-nav {
    margin: 20px 0;
    padding: 10px;
    background-color: #f0f0f0;
    border-radius: 5px;
}

.back-nav a {
    color: #007BFF;
    text-decoration: none;
    font-weight: bold;
}

.back-nav a:hover {
    text-decoration: underline;
}

.section-title {
    color: #007BFF;
    border-bottom: 2px solid #007BFF;
    padding-bottom: 5px;
    margin-top: 20px;
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
    background-color: #007BFF;
    color: white;
}

tr:nth-child(even) {
    background-color: #f2f2f2;
}

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
    <a href="./my-courses-2023-2024.html" data-i18n-html="back-courses-2023-2024">&larr; Retour aux Cours 2023-2024</a>
</div>

<div class="lang-fr">

<p><strong>Cours connexes</strong> :</p>
<ul>
<li><a href="./temps-reel.html">Temps Reel - S8</a> - Implementation temps reel des lois de commande</li>
<li><a href="./systemes-multivariables.html">Systemes Multivariables - S7</a> - Commande de systemes MIMO</li>
</ul>

<hr/>

<h1>Commande Numerique</h1>

<h2>PARTIE A : GENERALITES</h2>

<h3>Presentation</h3>
<p>Le cours "Commande Numerique" traite de la conception et de l'implementation de lois de commande sur calculateur numerique. Avec la generalisation des microcontroleurs et processeurs, la commande numerique est devenue la norme dans l'industrie. Ce cours couvre la theorie de l'echantillonnage, la synthese de correcteurs numeriques, et leur implementation pratique.</p>

<p><strong>Annee Academique</strong> : 2023-2024<br/>
<strong>Semestre</strong> : 8<br/>
<strong>Categorie</strong> : Automatique / Commande</p>

<hr/>

<h2>PARTIE B : PARTIE DESCRIPTIVE</h2>

<h3>Details de l'experience</h3>

<h4>Environnement et contexte</h4>
<p>Le cours combinait developpements mathematiques (transformee en Z, equations aux differences) avec implementation sur microcontroleur et simulation Matlab/Simulink. Nous avons concu des regulateurs numeriques pour differents systemes (moteur, temperature, niveau) et les avons testes en laboratoire.</p>

<h4>Ma fonction</h4>
<p>Dans ce cours, j'ai ete responsable de :</p>
<ul>
<li>Comprendre la theorie de l'echantillonnage et ses effets</li>
<li>Modeliser des systemes continus en temps discret</li>
<li>Synthetiser des correcteurs numeriques (PID, RST, predictif)</li>
<li>Choisir la periode d'echantillonnage appropriee</li>
<li>Implementer des lois de commande sur microcontroleur</li>
<li>Gerer les aspects pratiques (quantification, saturation, anti-windup)</li>
<li>Valider les performances en simulation et experimentation</li>
</ul>

<h2>PARTIE C : PARTIE TECHNIQUE</h2>

<p>Cette section explore les aspects techniques de la commande numerique.</p>

<h3>Concepts techniques appris</h3>

<h4>1. Echantillonnage et Theoreme de Shannon</h4>

<p><strong>Principe</strong> :</p>
<p>Conversion d'un signal continu s(t) en signal echantillonne s[k] :</p>
<pre><code>s[k] = s(k*Te)
ou Te est la periode d'echantillonnage
Fe = 1/Te est la frequence d'echantillonnage</code></pre>

<p><strong>Theoreme de Shannon</strong> :</p>
<pre><code>Fe &gt;= 2*Fmax</code></pre>
<p>Pour eviter le repliement spectral (aliasing).</p>

<p><strong>En pratique</strong> :</p>
<pre><code>Fe &gt;= (6 a 40) x BW_systeme</code></pre>
<p>ou BW_systeme est la bande passante du systeme.</p>

<p><strong>Choix de Te</strong> :</p>
<ul>
<li>Trop grande : perte d'information, instabilite</li>
<li>Trop petite : charge calcul, cout, problemes numeriques</li>
<li>Compromis selon application</li>
</ul>

<h4>2. Bloqueur d'Ordre Zero (BOZ / ZOH)</h4>

<p><strong>Fonction</strong> :</p>
<p>Maintenir la valeur de sortie constante entre deux echantillons :</p>
<pre><code>u(t) = u[k]  pour k*Te &lt;= t &lt; (k+1)*Te</code></pre>

<p><strong>Fonction de transfert</strong> :</p>
<pre><code>G_BOZ(s) = (1 - e^(-Te*s)) / s</code></pre>

<p><strong>Effet frequentiel</strong> :</p>
<p>Attenuation haute frequence (similaire a filtre passe-bas).</p>

<p><strong>Retard equivalent</strong> :</p>
<p>Environ Te/2 (retard moyen introduit)</p>

<h4>3. Transformee en Z</h4>

<p><strong>Definition</strong> :</p>
<pre><code>Z{s[k]} = S(z) = Sum s[k]*z^(-k)  pour k=0 a infini

ou z = e^(Te*s) relie plan de Laplace au plan en Z</code></pre>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S8/commande-numerique/systeme-echantillonne.svg" alt="Systeme en boucle fermee echantillonne"
       style="max-width: 500px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">
    <span class="lang-fr">Figure : Schema bloc d'un systeme de commande numerique avec correcteur C(z)</span>
    <span class="lang-en">Figure: Block diagram of a digital control system with controller C(z)</span>
  </p>
</div>

<p><strong>Proprietes</strong> :</p>
<ul>
<li><strong>Linearite</strong> : Z{a*x[k] + b*y[k]} = a*X(z) + b*Y(z)</li>
<li><strong>Retard</strong> : Z{x[k-n]} = z^(-n)*X(z)</li>
<li><strong>Avance</strong> : Z{x[k+n]} = z^n*(X(z) - Sum x[k]*z^(-k))</li>
<li><strong>Valeur initiale</strong> : x[0] = lim(z->infini) X(z)</li>
<li><strong>Valeur finale</strong> : x[infini] = lim(z->1) (z-1)*X(z) (si stable)</li>
</ul>

<p><strong>Transformees usuelles</strong> :</p>
<ul>
<li>Echelon : Z{1[k]} = z/(z-1)</li>
<li>Rampe : Z{k} = Te*z/(z-1)^2</li>
<li>Exponentielle : Z{e^(a*k*Te)} = z/(z-e^(a*Te))</li>
<li>Sinusoide : Z{sin(w*k*Te)} = z*sin(w*Te)/(z^2-2z*cos(w*Te)+1)</li>
</ul>

<h4>4. Fonction de Transfert en Z</h4>

<p><strong>Definition</strong> :</p>
<pre><code>H(z) = Y(z)/U(z) = (b0 + b1*z^(-1) + ... + bm*z^(-m)) / (1 + a1*z^(-1) + ... + an*z^(-n))</code></pre>

<p><strong>Equation aux differences</strong> :</p>
<pre><code>y[k] = -a1*y[k-1] - ... - an*y[k-n] + b0*u[k] + b1*u[k-1] + ... + bm*u[k-m]</code></pre>

<p>Forme directement implementable sur calculateur.</p>

<p><strong>Passage continu -> discret</strong> :</p>

<p><strong>Methode d'Euler avant</strong> :</p>
<pre><code>s -> (z-1)/Te</code></pre>

<p><strong>Methode d'Euler arriere (backward)</strong> :</p>
<pre><code>s -> (z-1)/(Te*z)</code></pre>

<p><strong>Methode de Tustin (trapezoidale)</strong> :</p>
<pre><code>s -> (2/Te)*(z-1)/(z+1)</code></pre>

<p>Plus precise, preserve mieux stabilite.</p>

<p><strong>Methode de la reponse impulsionnelle invariante</strong></p>

<p><strong>Methode ZOH (blocage d'ordre zero)</strong> :</p>
<pre><code>H(z) = Z{L^(-1){G(s)/s * (1 - e^(-Te*s))}}</code></pre>

<p>Methode exacte pour systeme precede d'un BOZ.</p>

<h4>5. Stabilite des Systemes Discrets</h4>

<p><strong>Condition de stabilite</strong> :</p>
<p>Tous les poles dans le cercle unite du plan en Z :</p>
<pre><code>|z_i| &lt; 1  pour tout pole z_i</code></pre>

<p><strong>Relation avec plan de Laplace</strong> :</p>
<ul>
<li><strong>Demi-plan gauche (stable continu)</strong> -> <strong>Interieur cercle unite (stable discret)</strong></li>
<li><strong>Axe imaginaire</strong> -> <strong>Cercle unite</strong></li>
<li><strong>Demi-plan droit (instable)</strong> -> <strong>Exterieur cercle unite</strong></li>
</ul>

<p><strong>Critere de Jury</strong> :</p>
<p>Table de Routh equivalente pour temps discret. Verifie si polynome a racines dans cercle unite.</p>

<p><strong>Lieu d'Evans discret</strong> :</p>
<p>Similaire au continu mais interpretation differente (cercle unite).</p>

<h4>6. Analyse Frequentielle Discrete</h4>

<p><strong>Reponse frequentielle</strong> :</p>
<pre><code>H(e^(jw*Te)) = H(z)|_(z=e^(jw*Te))</code></pre>

<p>Periodique de periode Fe (repliement).</p>

<p><strong>Diagrammes de Bode discrets</strong> :</p>
<ul>
<li>Gain : |H(e^(jw*Te))|_(dB)</li>
<li>Phase : arg(H(e^(jw*Te)))</li>
</ul>

<p>Traces pour w dans [0, pi/Te] (jusqu'a Fe/2).</p>

<p><strong>Marges de stabilite</strong> :</p>
<ul>
<li>Marge de gain</li>
<li>Marge de phase</li>
</ul>

<p>Interpretation similaire au continu.</p>

<h4>7. Regulateur PID Numerique</h4>

<p><strong>Forme continue</strong> :</p>
<pre><code>C(s) = Kp + Ki/s + Kd*s</code></pre>

<p><strong>Discretisation</strong> :</p>

<p><strong>Forme vitesse (incrementale)</strong> :</p>
<pre><code>Du[k] = u[k] - u[k-1]
Du[k] = q0*e[k] + q1*e[k-1] + q2*e[k-2]</code></pre>

<p>Ou :</p>
<ul>
<li>q0 = Kp + Ki*Te + Kd/Te</li>
<li>q1 = -Kp - 2*Kd/Te</li>
<li>q2 = Kd/Te</li>
</ul>

<p><strong>Forme position</strong> :</p>
<pre><code>u[k] = Kp*e[k] + Ki*Te*Sum(e[k]) + Kd*(e[k]-e[k-1])/Te</code></pre>

<p><strong>Action proportionnelle</strong> :</p>
<pre><code>uP[k] = Kp*e[k]</code></pre>

<p><strong>Action integrale (methode rectangulaire)</strong> :</p>
<pre><code>uI[k] = uI[k-1] + Ki*Te*e[k]</code></pre>

<p><strong>Action derivee</strong> :</p>
<pre><code>uD[k] = Kd*(e[k] - e[k-1])/Te</code></pre>

<p>Souvent filtree pour reduire bruit :</p>
<pre><code>uD[k] = alpha*uD[k-1] + Kd*(1-alpha)*(e[k]-e[k-1])/Te</code></pre>

<h4>8. Correcteurs Polynomiaux RST</h4>

<p><strong>Structure</strong> :</p>
<pre><code>R(z)*U(z) = T(z)*Yref(z) - S(z)*Y(z)</code></pre>

<p>Ou :</p>
<ul>
<li>R, S, T sont des polynomes en z^(-1)</li>
<li>Offre plus de degres de liberte que PID</li>
</ul>

<p><strong>Equation de commande</strong> :</p>
<pre><code>u[k] = (1/r0)*[t0*yref[k] + ... - s0*y[k] - s1*y[k-1] - ... - r1*u[k-1] - ...]</code></pre>

<p><strong>Synthese par placement de poles</strong> :</p>
<p>Resolution de l'equation diophantienne :</p>
<pre><code>A*R + B*S = P_desire</code></pre>

<p>Ou P_desire contient les poles en boucle fermee souhaites.</p>

<p><strong>Avantages</strong> :</p>
<ul>
<li>Placement precis des poles</li>
<li>Gestion des zeros du systeme</li>
<li>Robustesse ajustable</li>
</ul>

<h4>9. Commande Predictive (MPC)</h4>

<p><strong>Principe</strong> :</p>
<p>Optimiser une sequence de commandes futures pour minimiser un critere.</p>

<p><strong>Critere</strong> :</p>
<pre><code>J = Sum [w_y*(yref[k+i] - y[k+i])^2 + w_u*Du[k+i]^2]</code></pre>

<p>Sur un horizon de prediction.</p>

<p><strong>Algorithme</strong> :</p>
<ol>
<li>Predire sortie future avec modele</li>
<li>Optimiser commande pour minimiser J</li>
<li>Appliquer premiere commande u[k]</li>
<li>Repeter a chaque instant (receding horizon)</li>
</ol>

<p><strong>Avantages</strong> :</p>
<ul>
<li>Gestion naturelle des contraintes (saturation)</li>
<li>Anticipation (action predictive)</li>
<li>MIMO naturellement</li>
</ul>

<p><strong>Inconvenients</strong> :</p>
<ul>
<li>Charge calcul elevee</li>
<li>Necessite modele precis</li>
</ul>

<h4>10. Aspects Pratiques d'Implementation</h4>

<p><strong>Quantification</strong> :</p>
<ul>
<li><strong>ADC</strong> : signal analogique -> valeur numerique</li>
<li><strong>Calculs</strong> : virgule fixe ou flottante</li>
<li><strong>DAC</strong> : valeur numerique -> signal analogique</li>
</ul>

<p>Erreurs de quantification peuvent causer :</p>
<ul>
<li>Cycles limites (oscillations)</li>
<li>Degradation de performance</li>
</ul>

<p><strong>Saturations</strong> :</p>
<p>Actionneurs ont limites physiques :</p>
<pre><code>u_min &lt;= u[k] &lt;= u_max</code></pre>

<p><strong>Anti-windup</strong> :</p>
<p>Quand u sature, l'integrateur continue a s'accumuler (windup).</p>

<p>Solution :</p>
<pre><code>Si u sature:
  uI[k] = uI[k-1]  (geler integrale)
ou
  uI[k] = u_sat - uP[k] - uD[k]  (back-calculation)</code></pre>

<p><strong>Filtre derive</strong> :</p>
<p>L'action derivee amplifie le bruit. Filtrer avec passe-bas :</p>
<pre><code>D_filtre(z) = Kd*z/(z + alpha)  avec 0 &lt; alpha &lt; 1</code></pre>

<p><strong>Bumpless transfer</strong> :</p>
<p>Lors de changement de mode (manuel -> auto), eviter saut brutal :</p>
<ul>
<li>Initialiser correctement l'integrateur</li>
<li>Transition douce</li>
</ul>

<p><strong>Temps d'execution</strong> :</p>
<p>Le code de commande doit s'executer en moins de Te :</p>
<pre><code>T_exec &lt; Te</code></pre>

<p>Sinon, instabilite ou perte d'echantillons.</p>

<p>Optimisations :</p>
<ul>
<li>Code efficace (eviter fonctions couteuses)</li>
<li>Utiliser virgule fixe si necessaire</li>
<li>Interruptions pour timing precis</li>
</ul>

<h4>11. Observateurs Discrets</h4>

<p><strong>Problematique</strong> :</p>
<p>Si toutes les variables d'etat ne sont pas mesurees, les estimer.</p>

<p><strong>Observateur de Luenberger discret</strong> :</p>
<pre><code>x_hat[k+1] = A*x_hat[k] + B*u[k] + L*(y[k] - y_hat[k])
y_hat[k] = C*x_hat[k]</code></pre>

<p><strong>Placement des poles de l'observateur</strong> :</p>
<p>Plus rapides que ceux du systeme (2-5 fois).</p>

<p><strong>Filtre de Kalman</strong> :</p>
<p>Observateur optimal en presence de bruit.</p>

<h4>12. Outils de Simulation et Test</h4>

<p><strong>Matlab/Simulink</strong> :</p>
<ul>
<li>Blocs temps discret</li>
<li>Modelisation systeme mixte (continu + discret)</li>
<li>Discretisation automatique (c2d)</li>
<li>Analyse performance</li>
</ul>

<p><strong>Processor-in-the-Loop (PIL)</strong> :</p>
<p>Simulation avec code reel sur processeur cible. Verifie comportement avec quantification, timing reel.</p>

<p><strong>Hardware-in-the-Loop (HIL)</strong> :</p>
<p>Controleur reel + systeme simule temps reel. Validation avant tests sur systeme physique.</p>

<p><strong>Banc d'essai</strong> :</p>
<p>Test sur systeme reel avec instrumentation. Validation finale.</p>

<h2>PARTIE D : PARTIE ANALYTIQUE</h2>

<h3>Connaissances et competences mobilisees</h3>

<ul>
<li>Theorie de l'echantillonnage et transformee en Z</li>
<li>Discretisation de systemes continus</li>
<li>Analyse de stabilite des systemes discrets</li>
<li>Synthese de correcteurs numeriques (PID, RST, MPC)</li>
<li>Programmation de lois de commande sur microcontroleur</li>
<li>Gestion des aspects pratiques (quantification, saturation, timing)</li>
<li>Utilisation de Matlab/Simulink pour conception et simulation</li>
<li>Validation experimentale sur systemes reels</li>
<li>Optimisation de code pour temps reel</li>
</ul>

<h3>Auto-evaluation</h3>

<p>Ce cours a ete crucial pour comprendre que la commande numerique n'est pas qu'une simple discretisation de la commande continue. L'echantillonnage introduit des phenomenes specifiques (repliement, retard) qui doivent etre pris en compte.</p>

<p>La transformee en Z, initialement abstraite, est devenue un outil naturel apres pratique. La correspondance plan s <-> plan z est fondamentale pour comprendre comment les proprietes continues se transposent en discret.</p>

<p>Le choix de la periode d'echantillonnage est un compromis delicat. J'ai appris qu'il ne suffit pas de respecter Shannon; il faut echantillonner suffisamment vite pour que le comportement discret soit proche du continu, mais pas trop pour eviter problemes numeriques et charge calcul.</p>

<p>Le PID numerique semble simple mais les details d'implementation (forme vitesse vs position, anti-windup, filtre derive) sont essentiels pour performance et robustesse. Les problemes de windup peuvent causer des comportements tres surprenants.</p>

<p>Les correcteurs RST offrent beaucoup plus de flexibilite que le PID. La synthese par placement de poles est elegante mathematiquement, mais le choix des poles desires reste un art (compromis performance/robustesse).</p>

<p>La commande predictive (MPC) est seduisante pour sa capacite a gerer contraintes et anticipation. Cependant, la charge calcul peut etre prohibitive pour systemes rapides ou microcontroleurs limites. C'est un domaine de recherche actif.</p>

<p>L'implementation sur microcontroleur m'a confronte a des problemes pratiques souvent ignores en cours theoriques : timing d'interruptions, virgule fixe vs flottante, gestion des depassements arithmetiques. Le code doit etre robuste et efficace.</p>

<p>Les simulations Processor-in-the-Loop ont revele des ecarts entre theorie et pratique : quantification, arrondis, delais de calcul peuvent degrader performance voire destabiliser.</p>

<h3>Mon avis</h3>

<p>Ce cours est indispensable a l'ere du numerique. Pratiquement toute commande moderne est implementee sur calculateur. Maitriser les specificites du discret est donc essentiel.</p>

<p>Points forts :</p>
<ul>
<li>Equilibre theorie mathematique / implementation pratique</li>
<li>Outils modernes (Matlab, microcontroleurs)</li>
<li>Projets hands-on avec systemes reels</li>
<li>Prise en compte des contraintes pratiques</li>
</ul>

<p>Points a ameliorer :</p>
<ul>
<li>Plus de temps sur commande predictive (MPC)</li>
<li>Aspects multi-taches et systemes d'exploitation temps reel</li>
<li>Commande adaptative et robuste</li>
<li>Certification (normes industrielles)</li>
</ul>

<p>Reflexions personnelles :</p>

<p>La commande numerique a revolutionne l'automatique. Ce qui etait impensable en analogique (MPC, observateurs complexes, adaptation) devient possible avec des microcontroleurs peu couteux.</p>

<p>Cependant, la puissance de calcul disponible peut donner une fausse impression de facilite. Un correcteur mal concu (instabilite numerique, parametres inadaptes) ne marchera pas mieux sous pretexte qu'il est numerique.</p>

<p>La tendance est a l'augmentation de la puissance de calcul (processeurs multi-coeurs, FPGA, DSP). Cela ouvre des possibilites (fusion multi-capteurs, traitement d'image embarque, IA embarquee) mais necessite expertise en programmation temps reel et optimisation.</p>

<p>La separation traditionnelle entre electronicien et informaticien s'estompe. L'ingenieur moderne doit maitriser hardware (capteurs, actionneurs, electronique) ET software (algorithmes, programmation embarquee, architectures logicielles).</p>

<p>Applications professionnelles :</p>

<p>Ces competences sont applicables dans tous les domaines de l'automatique industrielle :</p>
<ul>
<li>Robotique (commande d'articulations)</li>
<li>Automobile (ESP, ABS, controle moteur)</li>
<li>Aeronautique (pilote automatique)</li>
<li>Procedes industriels (regulation temperature, pression, debit)</li>
<li>Energie (onduleurs, convertisseurs)</li>
<li>Drones (stabilisation, navigation)</li>
</ul>

<p>La maitrise de la commande numerique, couplee a des competences en traitement du signal et systemes embarques, est un profil tres recherche en industrie.</p>

<p>L'avenir verra probablement :</p>
<ul>
<li>Integration de l'IA dans les boucles de commande</li>
<li>Commande distribuee et collaborative (systemes multi-agents)</li>
<li>Auto-tuning et adaptation automatique</li>
<li>Co-design hardware/software pour optimisation globale</li>
</ul>

<p>Avoir des bases solides en commande numerique classique est le prerequis pour comprendre et contribuer a ces evolutions futures.</p>

<hr/>

<h2>Documents de Cours</h2>

</div>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">Polycopie Commande Numerique</span>
        <span class="lang-en">Digital Control Course Notes</span>
      </h4>
      <p>
        <span class="lang-fr">Cours complet : transformee en Z, echantillonnage, synthese de correcteurs numeriques et implementation discrete.</span>
        <span class="lang-en">Complete course: Z-transform, sampling, digital controller synthesis and discrete implementation.</span>
      </p>
      <embed src="/cours-pdf/S8/Commande-Numerique/polycopie.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S8/Commande-Numerique/polycopie.pdf" target="_blank">
        <span class="lang-fr">Telecharger</span>
        <span class="lang-en">Download</span>
      </a></p>
    </div>
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">Annales 2019</span>
        <span class="lang-en">2019 Past Exam</span>
      </h4>
      <p>
        <span class="lang-fr">Sujet d'examen 2019 avec exercices sur transformee en Z, stabilite et synthese de correcteurs PID numeriques.</span>
        <span class="lang-en">2019 exam paper with exercises on Z-transform, stability and digital PID controller synthesis.</span>
      </p>
      <embed src="/cours-pdf/S8/Commande-Numerique/annales-2019.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S8/Commande-Numerique/annales-2019.pdf" target="_blank">
        <span class="lang-fr">Telecharger</span>
        <span class="lang-en">Download</span>
      </a></p>
    </div>
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">Correction 2019</span>
        <span class="lang-en">2019 Exam Solutions</span>
      </h4>
      <p>
        <span class="lang-fr">Correction detaillee de l'examen 2019 avec methodes de resolution et explications completes.</span>
        <span class="lang-en">Detailed solutions for the 2019 exam with solving methods and complete explanations.</span>
      </p>
      <embed src="/cours-pdf/S8/Commande-Numerique/correction-2019.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S8/Commande-Numerique/correction-2019.pdf" target="_blank">
        <span class="lang-fr">Telecharger</span>
        <span class="lang-en">Download</span>
      </a></p>
    </div>
  </div>
</div>

<div class="lang-fr">
<hr/>
<p><em>Cours suivi en 2023-2024 a l'INSA Toulouse, Departement Genie Electrique et Informatique.</em></p>
</div>

<div class="lang-en">

<p><strong>Related courses</strong>:</p>
<ul>
<li><a href="./temps-reel.html">Real-Time Systems - S8</a> - Real-time implementation of control laws</li>
<li><a href="./systemes-multivariables.html">Multivariable Systems - S7</a> - MIMO system control</li>
</ul>

<hr/>

<h1>Digital Control</h1>

<h2>PART A: GENERALITIES</h2>

<h3>Presentation</h3>
<p>The "Commande Numerique" course covers the design and implementation of control laws on digital computers. With the widespread use of microcontrollers and processors, digital control has become the standard in industry. This course covers sampling theory, digital controller synthesis, and their practical implementation.</p>

<p><strong>Academic Year</strong>: 2023-2024<br/>
<strong>Semester</strong>: 8<br/>
<strong>Category</strong>: Control Engineering</p>

<hr/>

<h2>PART B: DESCRIPTIVE PART</h2>

<h3>Experience Details</h3>

<h4>Environment and Context</h4>
<p>The course combined mathematical developments (Z-transform, difference equations) with microcontroller implementation and Matlab/Simulink simulation. We designed digital controllers for various systems (motor, temperature, level) and tested them in the laboratory.</p>

<h4>My Function</h4>
<p>In this course, I was responsible for:</p>
<ul>
<li>Understanding sampling theory and its effects</li>
<li>Modeling continuous systems in discrete time</li>
<li>Synthesizing digital controllers (PID, RST, predictive)</li>
<li>Choosing the appropriate sampling period</li>
<li>Implementing control laws on a microcontroller</li>
<li>Managing practical aspects (quantization, saturation, anti-windup)</li>
<li>Validating performance through simulation and experimentation</li>
</ul>

<h2>PART C: TECHNICAL PART</h2>

<p>This section explores the technical aspects of digital control.</p>

<h3>Technical Concepts Learned</h3>

<h4>1. Sampling and the Shannon Theorem</h4>

<p><strong>Principle</strong>:</p>
<p>Conversion of a continuous signal s(t) into a sampled signal s[k]:</p>
<pre><code>s[k] = s(k*Te)
where Te is the sampling period
Fe = 1/Te is the sampling frequency</code></pre>

<p><strong>Shannon's Theorem</strong>:</p>
<pre><code>Fe &gt;= 2*Fmax</code></pre>
<p>To avoid spectral aliasing.</p>

<p><strong>In practice</strong>:</p>
<pre><code>Fe &gt;= (6 to 40) x BW_system</code></pre>
<p>where BW_system is the system bandwidth.</p>

<p><strong>Choosing Te</strong>:</p>
<ul>
<li>Too large: loss of information, instability</li>
<li>Too small: computational load, cost, numerical issues</li>
<li>Trade-off depending on the application</li>
</ul>

<h4>2. Zero-Order Hold (ZOH)</h4>

<p><strong>Function</strong>:</p>
<p>Hold the output value constant between two samples:</p>
<pre><code>u(t) = u[k]  for k*Te &lt;= t &lt; (k+1)*Te</code></pre>

<p><strong>Transfer function</strong>:</p>
<pre><code>G_ZOH(s) = (1 - e^(-Te*s)) / s</code></pre>

<p><strong>Frequency effect</strong>:</p>
<p>High-frequency attenuation (similar to a low-pass filter).</p>

<p><strong>Equivalent delay</strong>:</p>
<p>Approximately Te/2 (average delay introduced)</p>

<h4>3. The Z-Transform</h4>

<p><strong>Definition</strong>:</p>
<pre><code>Z{s[k]} = S(z) = Sum s[k]*z^(-k)  for k=0 to infinity

where z = e^(Te*s) relates the Laplace plane to the Z plane</code></pre>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S8/commande-numerique/systeme-echantillonne.svg" alt="Sampled closed-loop system"
       style="max-width: 500px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">
    <span class="lang-fr">Figure : Schema bloc d'un systeme de commande numerique avec correcteur C(z)</span>
    <span class="lang-en">Figure: Block diagram of a digital control system with controller C(z)</span>
  </p>
</div>

<p><strong>Properties</strong>:</p>
<ul>
<li><strong>Linearity</strong>: Z{a*x[k] + b*y[k]} = a*X(z) + b*Y(z)</li>
<li><strong>Delay</strong>: Z{x[k-n]} = z^(-n)*X(z)</li>
<li><strong>Advance</strong>: Z{x[k+n]} = z^n*(X(z) - Sum x[k]*z^(-k))</li>
<li><strong>Initial value</strong>: x[0] = lim(z->infinity) X(z)</li>
<li><strong>Final value</strong>: x[infinity] = lim(z->1) (z-1)*X(z) (if stable)</li>
</ul>

<p><strong>Common transforms</strong>:</p>
<ul>
<li>Step: Z{1[k]} = z/(z-1)</li>
<li>Ramp: Z{k} = Te*z/(z-1)^2</li>
<li>Exponential: Z{e^(a*k*Te)} = z/(z-e^(a*Te))</li>
<li>Sinusoid: Z{sin(w*k*Te)} = z*sin(w*Te)/(z^2-2z*cos(w*Te)+1)</li>
</ul>

<h4>4. Z-Domain Transfer Function</h4>

<p><strong>Definition</strong>:</p>
<pre><code>H(z) = Y(z)/U(z) = (b0 + b1*z^(-1) + ... + bm*z^(-m)) / (1 + a1*z^(-1) + ... + an*z^(-n))</code></pre>

<p><strong>Difference equation</strong>:</p>
<pre><code>y[k] = -a1*y[k-1] - ... - an*y[k-n] + b0*u[k] + b1*u[k-1] + ... + bm*u[k-m]</code></pre>

<p>Form directly implementable on a computer.</p>

<p><strong>Continuous-to-discrete conversion</strong>:</p>

<p><strong>Forward Euler method</strong>:</p>
<pre><code>s -> (z-1)/Te</code></pre>

<p><strong>Backward Euler method</strong>:</p>
<pre><code>s -> (z-1)/(Te*z)</code></pre>

<p><strong>Tustin (trapezoidal) method</strong>:</p>
<pre><code>s -> (2/Te)*(z-1)/(z+1)</code></pre>

<p>More accurate, better preserves stability.</p>

<p><strong>Impulse invariance method</strong></p>

<p><strong>ZOH (zero-order hold) method</strong>:</p>
<pre><code>H(z) = Z{L^(-1){G(s)/s * (1 - e^(-Te*s))}}</code></pre>

<p>Exact method for a system preceded by a ZOH.</p>

<h4>5. Stability of Discrete Systems</h4>

<p><strong>Stability condition</strong>:</p>
<p>All poles inside the unit circle of the Z plane:</p>
<pre><code>|z_i| &lt; 1  for all poles z_i</code></pre>

<p><strong>Relationship with the Laplace plane</strong>:</p>
<ul>
<li><strong>Left half-plane (continuous stable)</strong> -> <strong>Inside the unit circle (discrete stable)</strong></li>
<li><strong>Imaginary axis</strong> -> <strong>Unit circle</strong></li>
<li><strong>Right half-plane (unstable)</strong> -> <strong>Outside the unit circle</strong></li>
</ul>

<p><strong>Jury criterion</strong>:</p>
<p>Discrete-time equivalent of the Routh table. Verifies whether a polynomial has roots inside the unit circle.</p>

<p><strong>Discrete root locus</strong>:</p>
<p>Similar to continuous but with different interpretation (unit circle).</p>

<h4>6. Discrete Frequency Analysis</h4>

<p><strong>Frequency response</strong>:</p>
<pre><code>H(e^(jw*Te)) = H(z)|_(z=e^(jw*Te))</code></pre>

<p>Periodic with period Fe (aliasing).</p>

<p><strong>Discrete Bode diagrams</strong>:</p>
<ul>
<li>Gain: |H(e^(jw*Te))|_(dB)</li>
<li>Phase: arg(H(e^(jw*Te)))</li>
</ul>

<p>Plotted for w in [0, pi/Te] (up to Fe/2).</p>

<p><strong>Stability margins</strong>:</p>
<ul>
<li>Gain margin</li>
<li>Phase margin</li>
</ul>

<p>Interpretation similar to the continuous case.</p>

<h4>7. Digital PID Controller</h4>

<p><strong>Continuous form</strong>:</p>
<pre><code>C(s) = Kp + Ki/s + Kd*s</code></pre>

<p><strong>Discretization</strong>:</p>

<p><strong>Velocity (incremental) form</strong>:</p>
<pre><code>Du[k] = u[k] - u[k-1]
Du[k] = q0*e[k] + q1*e[k-1] + q2*e[k-2]</code></pre>

<p>Where:</p>
<ul>
<li>q0 = Kp + Ki*Te + Kd/Te</li>
<li>q1 = -Kp - 2*Kd/Te</li>
<li>q2 = Kd/Te</li>
</ul>

<p><strong>Position form</strong>:</p>
<pre><code>u[k] = Kp*e[k] + Ki*Te*Sum(e[k]) + Kd*(e[k]-e[k-1])/Te</code></pre>

<p><strong>Proportional action</strong>:</p>
<pre><code>uP[k] = Kp*e[k]</code></pre>

<p><strong>Integral action (rectangular method)</strong>:</p>
<pre><code>uI[k] = uI[k-1] + Ki*Te*e[k]</code></pre>

<p><strong>Derivative action</strong>:</p>
<pre><code>uD[k] = Kd*(e[k] - e[k-1])/Te</code></pre>

<p>Often filtered to reduce noise:</p>
<pre><code>uD[k] = alpha*uD[k-1] + Kd*(1-alpha)*(e[k]-e[k-1])/Te</code></pre>

<h4>8. Polynomial RST Controllers</h4>

<p><strong>Structure</strong>:</p>
<pre><code>R(z)*U(z) = T(z)*Yref(z) - S(z)*Y(z)</code></pre>

<p>Where:</p>
<ul>
<li>R, S, T are polynomials in z^(-1)</li>
<li>Offers more degrees of freedom than PID</li>
</ul>

<p><strong>Control equation</strong>:</p>
<pre><code>u[k] = (1/r0)*[t0*yref[k] + ... - s0*y[k] - s1*y[k-1] - ... - r1*u[k-1] - ...]</code></pre>

<p><strong>Pole placement synthesis</strong>:</p>
<p>Solving the Diophantine equation:</p>
<pre><code>A*R + B*S = P_desired</code></pre>

<p>Where P_desired contains the desired closed-loop poles.</p>

<p><strong>Advantages</strong>:</p>
<ul>
<li>Precise pole placement</li>
<li>Management of system zeros</li>
<li>Adjustable robustness</li>
</ul>

<h4>9. Model Predictive Control (MPC)</h4>

<p><strong>Principle</strong>:</p>
<p>Optimize a sequence of future control actions to minimize a cost function.</p>

<p><strong>Cost function</strong>:</p>
<pre><code>J = Sum [w_y*(yref[k+i] - y[k+i])^2 + w_u*Du[k+i]^2]</code></pre>

<p>Over a prediction horizon.</p>

<p><strong>Algorithm</strong>:</p>
<ol>
<li>Predict future output using the model</li>
<li>Optimize control to minimize J</li>
<li>Apply the first control action u[k]</li>
<li>Repeat at each time step (receding horizon)</li>
</ol>

<p><strong>Advantages</strong>:</p>
<ul>
<li>Natural constraint handling (saturation)</li>
<li>Anticipation (predictive action)</li>
<li>Naturally handles MIMO systems</li>
</ul>

<p><strong>Disadvantages</strong>:</p>
<ul>
<li>High computational load</li>
<li>Requires an accurate model</li>
</ul>

<h4>10. Practical Implementation Aspects</h4>

<p><strong>Quantization</strong>:</p>
<ul>
<li><strong>ADC</strong>: analog signal -> digital value</li>
<li><strong>Computation</strong>: fixed-point or floating-point</li>
<li><strong>DAC</strong>: digital value -> analog signal</li>
</ul>

<p>Quantization errors can cause:</p>
<ul>
<li>Limit cycles (oscillations)</li>
<li>Performance degradation</li>
</ul>

<p><strong>Saturation</strong>:</p>
<p>Actuators have physical limits:</p>
<pre><code>u_min &lt;= u[k] &lt;= u_max</code></pre>

<p><strong>Anti-windup</strong>:</p>
<p>When u saturates, the integrator continues accumulating (windup).</p>

<p>Solution:</p>
<pre><code>If u saturated:
  uI[k] = uI[k-1]  (freeze integral)
or
  uI[k] = u_sat - uP[k] - uD[k]  (back-calculation)</code></pre>

<p><strong>Derivative filter</strong>:</p>
<p>The derivative action amplifies noise. Filter with a low-pass:</p>
<pre><code>D_filtered(z) = Kd*z/(z + alpha)  with 0 &lt; alpha &lt; 1</code></pre>

<p><strong>Bumpless transfer</strong>:</p>
<p>When switching modes (manual -> auto), avoid abrupt jumps:</p>
<ul>
<li>Correctly initialize the integrator</li>
<li>Smooth transition</li>
</ul>

<p><strong>Execution time</strong>:</p>
<p>The control code must execute in less than Te:</p>
<pre><code>T_exec &lt; Te</code></pre>

<p>Otherwise, instability or sample loss.</p>

<p>Optimizations:</p>
<ul>
<li>Efficient code (avoid expensive functions)</li>
<li>Use fixed-point arithmetic if necessary</li>
<li>Interrupts for precise timing</li>
</ul>

<h4>11. Discrete Observers</h4>

<p><strong>Problem</strong>:</p>
<p>If not all state variables are measured, estimate them.</p>

<p><strong>Discrete Luenberger observer</strong>:</p>
<pre><code>x_hat[k+1] = A*x_hat[k] + B*u[k] + L*(y[k] - y_hat[k])
y_hat[k] = C*x_hat[k]</code></pre>

<p><strong>Observer pole placement</strong>:</p>
<p>Faster than system poles (2-5 times).</p>

<p><strong>Kalman filter</strong>:</p>
<p>Optimal observer in the presence of noise.</p>

<h4>12. Simulation and Testing Tools</h4>

<p><strong>Matlab/Simulink</strong>:</p>
<ul>
<li>Discrete-time blocks</li>
<li>Mixed system modeling (continuous + discrete)</li>
<li>Automatic discretization (c2d)</li>
<li>Performance analysis</li>
</ul>

<p><strong>Processor-in-the-Loop (PIL)</strong>:</p>
<p>Simulation with real code on the target processor. Verifies behavior with quantization and real timing.</p>

<p><strong>Hardware-in-the-Loop (HIL)</strong>:</p>
<p>Real controller + real-time simulated system. Validation before testing on the physical system.</p>

<p><strong>Test bench</strong>:</p>
<p>Testing on a real system with instrumentation. Final validation.</p>

<h2>PART D: ANALYTICAL PART</h2>

<h3>Knowledge and Skills Mobilized</h3>

<ul>
<li>Sampling theory and Z-transform</li>
<li>Discretization of continuous systems</li>
<li>Stability analysis of discrete systems</li>
<li>Digital controller synthesis (PID, RST, MPC)</li>
<li>Programming control laws on a microcontroller</li>
<li>Managing practical aspects (quantization, saturation, timing)</li>
<li>Using Matlab/Simulink for design and simulation</li>
<li>Experimental validation on real systems</li>
<li>Code optimization for real-time operation</li>
</ul>

<h3>Self Evaluation</h3>

<p>This course was crucial for understanding that digital control is not merely a discretization of continuous control. Sampling introduces specific phenomena (aliasing, delay) that must be accounted for.</p>

<p>The Z-transform, initially abstract, became a natural tool after practice. The correspondence between the s-plane and the z-plane is fundamental for understanding how continuous properties translate into discrete ones.</p>

<p>Choosing the sampling period is a delicate trade-off. I learned that simply satisfying Shannon is not enough; one must sample fast enough for the discrete behavior to approximate the continuous one, but not too fast to avoid numerical issues and computational load.</p>

<p>The digital PID seems simple, but implementation details (velocity vs position form, anti-windup, derivative filter) are essential for performance and robustness. Windup issues can cause very surprising behavior.</p>

<p>RST controllers offer much more flexibility than PID. Pole placement synthesis is mathematically elegant, but choosing the desired poles remains an art (performance/robustness trade-off).</p>

<p>Model Predictive Control (MPC) is attractive for its ability to handle constraints and anticipation. However, the computational load can be prohibitive for fast systems or limited microcontrollers. It is an active area of research.</p>

<p>Implementing on a microcontroller confronted me with practical problems often overlooked in theoretical courses: interrupt timing, fixed-point vs floating-point, arithmetic overflow management. The code must be robust and efficient.</p>

<p>Processor-in-the-Loop simulations revealed gaps between theory and practice: quantization, rounding, and computation delays can degrade performance or even destabilize the system.</p>

<h3>My Opinion</h3>

<p>This course is indispensable in the digital era. Virtually all modern control is implemented on computers. Mastering the specificities of discrete systems is therefore essential.</p>

<p>Strengths:</p>
<ul>
<li>Balance between mathematical theory and practical implementation</li>
<li>Modern tools (Matlab, microcontrollers)</li>
<li>Hands-on projects with real systems</li>
<li>Consideration of practical constraints</li>
</ul>

<p>Areas for improvement:</p>
<ul>
<li>More time on Model Predictive Control (MPC)</li>
<li>Multi-tasking aspects and real-time operating systems</li>
<li>Adaptive and robust control</li>
<li>Certification (industrial standards)</li>
</ul>

<p>Personal reflections:</p>

<p>Digital control has revolutionized control engineering. What was unthinkable in analog (MPC, complex observers, adaptation) becomes possible with inexpensive microcontrollers.</p>

<p>However, the available computing power can give a false impression of ease. A poorly designed controller (numerical instability, inappropriate parameters) will not work better just because it is digital.</p>

<p>The trend is toward increasing computational power (multi-core processors, FPGAs, DSPs). This opens up possibilities (multi-sensor fusion, embedded image processing, embedded AI) but requires expertise in real-time programming and optimization.</p>

<p>The traditional separation between electronics engineer and software engineer is fading. The modern engineer must master hardware (sensors, actuators, electronics) AND software (algorithms, embedded programming, software architectures).</p>

<p>Professional applications:</p>

<p>These skills are applicable across all fields of industrial automation:</p>
<ul>
<li>Robotics (joint control)</li>
<li>Automotive (ESP, ABS, engine control)</li>
<li>Aerospace (autopilot)</li>
<li>Industrial processes (temperature, pressure, flow regulation)</li>
<li>Energy (inverters, converters)</li>
<li>Drones (stabilization, navigation)</li>
</ul>

<p>Mastery of digital control, combined with skills in signal processing and embedded systems, is a highly sought-after profile in industry.</p>

<p>The future will likely see:</p>
<ul>
<li>Integration of AI in control loops</li>
<li>Distributed and collaborative control (multi-agent systems)</li>
<li>Auto-tuning and automatic adaptation</li>
<li>Hardware/software co-design for global optimization</li>
</ul>

<p>Having solid foundations in classical digital control is the prerequisite for understanding and contributing to these future developments.</p>

<hr/>

<h2>Course Documents</h2>

<!-- Shared PDF sections above -->

<hr/>

<p><em>Course taken in 2023-2024 at INSA Toulouse, Department of Electrical and Computer Engineering.</em></p>

</div>

<div class="back-nav">
    <a href="./my-courses-2023-2024.html" data-i18n-html="back-courses-2023-2024">&larr; Retour aux Cours 2023-2024</a>
</div>

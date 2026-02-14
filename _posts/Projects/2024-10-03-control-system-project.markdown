---
layout: default
title:  "Control Systems Project"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

<style>
p {
  text-align: justify;
}
</style>

<div class="back-nav">
    <a href="./my-projects.html" data-i18n-html="back-projects">&larr; Retour aux Projets</a>
</div>

<div class="lang-fr">
<h1>Introduction</h1>
<p>L'objectif de ce projet etait d'utiliser Matlab et Simulink pour modeliser, simuler et commander un robot a deux roues base sur le systeme Lego Mindstorms EV3. Le projet nous a permis d'explorer plusieurs techniques de commande, notamment la commande proportionnelle, la commande proportionnelle-integrale et la commande par retour d'etat pour stabiliser le systeme.</p>
</div>

<div class="lang-en">
<h1>Introduction</h1>
<p>The objective of this project was to use Matlab and Simulink to model, simulate, and control a two-wheeled robot based on the Lego Mindstorms EV3 system. The project allowed us to explore several control techniques, including proportional control, proportional-integral control, and state feedback control to stabilize the system.</p>
</div>

<div style="text-align: center;">
    <img src="/img/BE_Control_System/Robot.png" style="width: 70%;"/>
</div>

<div class="lang-fr">
<h2>Parametres du robot</h2>
<p>Le robot a deux roues a ete modelise a partir des parametres suivants :</p>
<ul>
<li>Constantes physiques : Acceleration gravitationnelle g=9.81m/s<sup>2</sup></li>
<li>Parametres Lego Mindstorms :
<ul>
<li>Poids des roues m=0.03kg</li>
<li>Rayon des roues R=0.042m</li>
<li>Poids du corps M=0.67kg</li>
<li>Largeur du corps W=0.165m</li>
<li>Hauteur du corps H=0.152m</li>
<li>Distance du centre de masse L=H/2</li>
<li>Coefficients de frottement fm=0.0022 = fw=0</li>
</ul></li>
</ul>
<p>A partir de ces parametres, nous avons calcule les constantes utilisees dans la dynamique du systeme :</p>
</div>

<div class="lang-en">
<h2>Robot Parameters</h2>
<p>The two-wheeled robot was modeled based on the following parameters:</p>
<ul>
<li>Physical Constants: Gravity acceleration g=9.81m/s<sup>2</sup></li>
<li>Lego Mindstorms Parameters:
<ul>
<li>Wheel weight m=0.03kg</li>
<li>Wheel radius R=0.042m</li>
<li>Body weight M=0.67kg</li>
<li>Body width W=0.165m</li>
<li>Body height H=0.152m</li>
<li>Center of mass distance L=H/2</li>
<li>Friction coefficients fm=0.0022 = fw=0</li>
</ul></li>
</ul>
<p>From these parameters, we calculated the constants used in the system dynamics:</p>
</div>

<img src="/img/BE_Control_System/equation.png" style="width: 20%;"/>

<div style="text-align: center;">
    <img src="/img/BE_Control_System/Robot2.png" style="width: 30%;"/>
    <img src="/img/BE_Control_System/Robot3.png" style="width: 60%;"/>
</div>

<div class="lang-fr">
<h2>Modelisation du processus</h2>
<h3>Modeles d'etat MIMO</h3>
<p>La representation d'etat du systeme a ete derivee en modelisant le mouvement du robot a l'aide de la methode de Lagrange. Les matrices suivantes definissent le systeme :</p>
</div>

<div class="lang-en">
<h2>Process Modeling</h2>
<h3>MIMO State-Space Models</h3>
<p>The system's state-space representation was derived by modeling the robot's motion using the Lagrangian method. The following matrices define the system:</p>
</div>

<img src="/img/BE_Control_System/equation2.png" style="width: 70%;"/>

<div class="lang-fr">
<h3>Modele d'etat SISO</h3>
<p>Nous avons reduit le modele MIMO a un modele d'etat SISO pour le controle de l'equilibre, en simplifiant l'entree a u=(vl+vr)/2. Le systeme resultant a ete defini comme : <code>sys = ss(A, B, C, 0)</code></p>

<h2>Simulation du systeme avec Simulink</h2>
<p>Nous avons d'abord teste la reponse en boucle ouverte du systeme a une entree echelon de 1V. Ensuite, nous avons teste la reponse du systeme a une entree impulsionnelle. Dans les deux cas, le systeme etait instable, car le signal ne se stabilisait pas et continuait d'augmenter sans limite.</p>

<h2>Analyse en boucle ouverte</h2>
<p>Nous avons analyse le systeme pour l'observabilite et la commandabilite. Les rangs des deux matrices etaient egaux au rang de la matrice A, confirmant que le systeme est observable et commandable. Le systeme s'est avere instable, comme le montre la carte poles-zeros et l'analyse de l'amortissement.</p>
</div>

<div class="lang-en">
<h3>SISO State-Space Model</h3>
<p>We reduced the MIMO model to a SISO state-space model for balance control, simplifying the input to u=(vl+vr)/2. The resulting system was defined as: <code>sys = ss(A, B, C, 0)</code></p>

<h2>Simulation of the System with Simulink</h2>
<p>We first tested the open-loop response of the system to a step input of 1V. Next, we tested the system's response to an impulse input. In both cases, the system was unstable, as the signal did not stabilize and continued increasing without bound.</p>

<h2>Open-Loop Analysis</h2>
<p>We analyzed the system for observability and controllability. Both matrices' ranks were equal to the rank of matrix A, confirming that the system is observable and controllable. The system was found to be unstable, as shown by the pole-zero map and damping analysis.</p>
</div>

<div style="text-align: center;">
    <img src="/img/BE_Control_System/pole.png" style="width: 40%;"/>
</div>

<div class="lang-fr">
<h2>Conception du systeme de commande</h2>
<h3>Commande proportionnelle</h3>
<p>Nous avons implemente un correcteur proportionnel pour stabiliser le systeme. Malgre la variation du gain Kp, le systeme est reste instable :</p>
</div>

<div class="lang-en">
<h2>Control System Design</h2>
<h3>Proportional Control</h3>
<p>We implemented a proportional controller to stabilize the system. Despite varying the gain Kp, the system remained unstable:</p>
</div>

<div style="text-align: center;">
    <img src="/img/BE_Control_System/correcteur.png" style="width: 80%;"/>
</div>

<div style="text-align: center;">
    <img src="/img/BE_Control_System/pole2.png" style="width: 40%;"/>
    <img src="/img/BE_Control_System/root.png" style="width: 40%;"/>
</div>

<div class="lang-fr">
<h3>Commande proportionnelle-integrale</h3>
<p>Ensuite, nous avons implemente un correcteur proportionnel-integral (PI). Cependant, le systeme est reste instable pour toute combinaison de Kp et Ki, car l'analyse du tableau de Routh a montre qu'il y avait toujours des termes positifs dans la premiere colonne :</p>
</div>

<div class="lang-en">
<h3>Proportional-Integral Control</h3>
<p>Next, we implemented a proportional-integral (PI) controller. However, the system remained unstable for any combination of Kp and Ki, as the Routh table analysis showed that there were always positive terms in the first column:</p>
</div>

<div style="text-align: center;">
    <img src="/img/BE_Control_System/correcteur2.png" style="width: 80%;"/>
</div>

<div class="lang-fr">
<h3>Commande par retour d'etat</h3>
<p>Enfin, nous avons implemente un correcteur par retour d'etat, qui a reussi a stabiliser le systeme. Cependant, le signal de commande presentait une erreur significative, que nous avons corrigee en ajoutant un pre-gain lc.</p>
</div>

<div class="lang-en">
<h3>State Feedback Control</h3>
<p>Finally, we implemented a state feedback controller, which successfully stabilized the system. However, the control signal exhibited significant error, which we corrected by adding a pre-gain lc.</p>
</div>

<div style="text-align: center;">
    <img src="/img/BE_Control_System/correcteur3.png" style="width: 80%;"/>
</div>

<div class="lang-fr">
<h2>Simulations non-lineaires</h2>
<p>En utilisant le fichier Simulink NXTwaySim fourni, nous avons realise des simulations non-lineaires pour valider les lois de commande. Sans retour d'etat, le systeme etait instable, mais avec le retour d'etat, le robot maintenait son equilibre :</p>
</div>

<div class="lang-en">
<h2>Nonlinear Simulations</h2>
<p>Using the provided NXTwaySim Simulink file, we performed nonlinear simulations to validate the control laws. Without feedback, the system was unstable, but with state feedback, the robot maintained balance:</p>
</div>

<div style="text-align: center;">
    <img src="/img/BE_Control_System/correcteur4.png" style="width: 80%;"/>
</div>

<div class="lang-fr">
<h1>Conclusion</h1>
<p>Ce projet nous a permis d'explorer et d'appliquer differentes techniques de commande a un systeme complexe du monde reel en utilisant Matlab et Simulink. Alors que les correcteurs proportionnels et PI n'ont pas fourni la stabilite necessaire, le correcteur par retour d'etat s'est avere etre une solution efficace. Le projet a mis en evidence l'importance du retour d'etat dans la stabilisation de systemes ou les strategies de commande plus simples echouent.</p>
<p>Le projet a egalement fourni une experience precieuse dans la modelisation et la simulation de systemes de commande et a approfondi notre comprehension des concepts theoriques abordes en cours.</p>
</div>

<div class="lang-en">
<h1>Conclusion</h1>
<p>This project allowed us to explore and apply various control techniques to a complex, real-world system using Matlab and Simulink. While proportional and PI controllers did not provide the necessary stability, the state feedback controller proved to be an effective solution. The project highlighted the importance of state feedback in stabilizing systems where simpler control strategies fail.</p>
<p>The project also provided valuable experience in modeling and simulating control systems and deepened our understanding of the theoretical concepts covered in class.</p>
</div>

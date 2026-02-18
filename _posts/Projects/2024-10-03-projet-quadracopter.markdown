---
layout: default
title: "Quadcopter Design and Development"
date: 2024-10-02 10:56:03 +0200
---

<style>
p {
  text-align: justify;
}
.modal {
  display: none;
  position: fixed;
  z-index: 1;
  padding-top: 60px;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgb(0,0,0);
  background-color: rgba(0,0,0,0.9);
}

.modal-content {
  margin: auto;
  display: block;
  width: 80%;
  max-width: 700px;
}

.close {
  position: absolute;
  top: 15px;
  right: 35px;
  color: #f1f1f1;
  font-size: 40px;
  font-weight: bold;
  transition: 0.3s;
}

.close:hover,
.close:focus {
  color: #bbb;
  text-decoration: none;
  cursor: pointer;
}
</style>

<div class="back-nav">
    <a href="./my-projects.html" data-i18n-html="back-projects">&larr; Retour aux Projets</a>
</div>

<div class="lang-fr">
<h1>Introduction</h1>
<p>Ce projet multidisciplinaire complet a consiste a concevoir, construire et programmer un quadricoptere fonctionnel de A a Z. Le projet a integre l'electronique (systemes de puissance, controle moteur, capteurs), la programmation embarquee (firmware du controleur de vol, fusion de capteurs), la theorie du controle (reglage PID, stabilisation) et la conception mecanique (chassis, systeme de propulsion). Ce projet de synthese a applique toutes les competences acquises durant la premiere annee, aboutissant a un drone volant autonome.</p>

<h1>Vue d'ensemble du projet</h1>
<p>En travaillant en equipe, nous avons developpe un systeme de quadricoptere complet capable de vol stable avec plusieurs modes de vol. Le projet a couvert la definition des exigences, la selection des composants, l'assemblage, la programmation, le reglage PID et des tests de vol approfondis. Les protocoles de securite etaient primordiaux tout au long des phases de developpement.</p>

<h2>Architecture du systeme</h2>

<h3>Sous-systemes electroniques</h3>
<p><strong>Gestion de l'alimentation :</strong></p>
<ul>
<li>Batterie LiPo (3S ou 4S, 2200+ mAh)</li>
<li>Carte de distribution de puissance (PDB)</li>
<li>Regulateurs de tension (5V, 3.3V)</li>
<li>Surveillance et protection de la batterie</li>
<li>Calcul et optimisation de l'autonomie</li>
</ul>

<p><strong>Controle des moteurs :</strong></p>
<ul>
<li>4 moteurs brushless DC</li>
<li>4 controleurs de vitesse electroniques (ESC)</li>
<li>Signaux de commande PWM (1000-2000 us)</li>
<li>Procedures de calibration des ESC</li>
<li>Appariement moteur-helice pour l'efficacite</li>
</ul>

<p><strong>Suite de capteurs :</strong></p>
<ul>
<li>IMU (Unite de mesure inertielle) : gyroscope, accelerometre et magnetometre 3 axes</li>
<li>Barometre (estimation d'altitude)</li>
<li>Module GPS (position, vitesse)</li>
<li>Telemetre ultrasonique (proximite sol)</li>
<li>Liaison radio telemetrique</li>
</ul>
</div>

<div class="lang-en">
<h1>Introduction</h1>
<p>This comprehensive multidisciplinary project involved designing, building, and programming a functional quadcopter from scratch. The project integrated electronics (power systems, motor control, sensors), embedded programming (flight controller firmware, sensor fusion), control theory (PID tuning, stabilization), and mechanical design (frame, propulsion system). This synthesis project applied all skills acquired during the first year, culminating in a flying autonomous drone.</p>

<h1>Project Overview</h1>
<p>Working in teams, we developed a complete quadcopter system capable of stable flight with multiple flight modes. The project spanned requirements definition, component selection, assembly, programming, PID tuning, and extensive flight testing. Safety protocols were paramount throughout all development phases.</p>

<h2>System Architecture</h2>

<h3>Electronic Subsystems</h3>
<p><strong>Power Management:</strong></p>
<ul>
<li>LiPo battery (3S or 4S, 2200+ mAh)</li>
<li>Power Distribution Board (PDB)</li>
<li>Voltage regulators (5V, 3.3V)</li>
<li>Battery monitoring and protection</li>
<li>Autonomy calculation and optimization</li>
</ul>

<p><strong>Motor Control:</strong></p>
<ul>
<li>4x Brushless DC motors</li>
<li>4x Electronic Speed Controllers (ESC)</li>
<li>PWM control signals (1000-2000 us)</li>
<li>ESC calibration procedures</li>
<li>Motor-propeller matching for efficiency</li>
</ul>

<p><strong>Sensor Suite:</strong></p>
<ul>
<li>IMU (Inertial Measurement Unit): 3-axis gyroscope, accelerometer, and magnetometer</li>
<li>Barometer (altitude estimation)</li>
<li>GPS module (position, velocity)</li>
<li>Ultrasonic rangefinder (ground proximity)</li>
<li>Telemetry radio link</li>
</ul>
</div>

<div class="lang-fr">
<h1>Conception du systeme de controle</h1>

<h2>Modelisation mathematique</h2>
<p><strong>Dynamique a 6 degres de liberte :</strong></p>
<ul>
<li>Translation : position x, y, z</li>
<li>Rotation : roulis, tangage, lacet</li>
<li>Forces et couples des quatre rotors</li>
<li>Effets aerodynamiques et perturbations</li>
</ul>

<h2>Implementation du controle PID</h2>
<p><strong>Architecture de controle en cascade :</strong></p>
<ol>
<li><strong>Boucle interne (controle de vitesse angulaire) :</strong> Reponse rapide (~1 kHz), retour gyroscopique, controle des vitesses angulaires</li>
<li><strong>Boucle externe (controle d'angle) :</strong> Reponse plus lente (~100 Hz), retour accelerometre/magnetometre, maintien de l'attitude desiree</li>
</ol>

<p><strong>Processus de reglage PID :</strong></p>
<ul>
<li>Commencer avec des gains faibles</li>
<li>Augmenter le gain P jusqu'a oscillation</li>
<li>Ajouter le gain D pour amortir les oscillations</li>
<li>Ajouter le gain I pour eliminer l'erreur statique</li>
<li>Tests iteratifs et affinement</li>
</ul>

<h2>Modes de vol</h2>
<ul>
<li><strong>Manuel (Acro) :</strong> Controle direct de la vitesse angulaire, pas d'auto-stabilisation</li>
<li><strong>Stabilise (Angle) :</strong> Auto-stabilisation automatique, maintien de l'attitude horizontale</li>
<li><strong>Maintien d'altitude :</strong> Verrouillage d'altitude par barometre, ajustement automatique des gaz</li>
<li><strong>Maintien de position (GPS) :</strong> Verrouillage de position par GPS, resistance au vent</li>
</ul>
</div>

<div class="lang-en">
<h1>Control System Design</h1>

<h2>Mathematical Modeling</h2>
<p><strong>6 Degree-of-Freedom Dynamics:</strong></p>
<ul>
<li>Translation: x, y, z position</li>
<li>Rotation: roll, pitch, yaw</li>
<li>Forces and torques from four rotors</li>
<li>Aerodynamic effects and disturbances</li>
</ul>

<h2>PID Control Implementation</h2>
<p><strong>Cascade Control Architecture:</strong></p>
<ol>
<li><strong>Inner Loop (Rate Control):</strong> Fast response (~1 kHz), gyroscope feedback, controls angular velocities</li>
<li><strong>Outer Loop (Angle Control):</strong> Slower response (~100 Hz), accelerometer/magnetometer feedback, maintains desired attitude</li>
</ol>

<p><strong>PID Tuning Process:</strong></p>
<ul>
<li>Start with low gains</li>
<li>Increase P gain until oscillation</li>
<li>Add D gain to dampen oscillations</li>
<li>Add I gain to eliminate steady-state error</li>
<li>Iterative testing and refinement</li>
</ul>

<h2>Flight Modes</h2>
<ul>
<li><strong>Manual (Acro):</strong> Direct angular velocity control, no self-leveling</li>
<li><strong>Stabilized (Angle):</strong> Automatic self-leveling, maintains horizontal attitude</li>
<li><strong>Altitude Hold:</strong> Barometer-based altitude lock, automatic throttle adjustment</li>
<li><strong>Position Hold (GPS):</strong> GPS-based position lock, resists wind drift</li>
</ul>
</div>

<div class="lang-fr">
<h1>Processus de developpement</h1>

<h2>Phase 1 : Conception et selection des composants (3 semaines)</h2>
<ul>
<li>Specification des exigences</li>
<li>Recherche et benchmarking</li>
<li>Selection et compatibilite des composants</li>
<li>Planification budgetaire</li>
</ul>

<h2>Phase 2 : Assemblage et integration (3 semaines)</h2>
<ul>
<li>Assemblage du chassis</li>
<li>Installation et cablage de l'electronique</li>
<li>Gestion des cables (minimiser la transmission des vibrations)</li>
<li>Optimisation de la distribution du poids</li>
</ul>

<h2>Phase 3 : Configuration et tests au sol (3 semaines)</h2>
<ul>
<li>Configuration du controleur de vol</li>
<li>Calibration des capteurs (accelerometre, magnetometre, gyroscope)</li>
<li>Calibration des ESC</li>
<li>Configuration radio et failsafe</li>
</ul>

<h2>Phase 4 : Tests de vol et reglage (3 semaines)</h2>
<p><strong>Tests progressifs :</strong></p>
<ol>
<li>Test de vol attache</li>
<li>Vol stationnaire basse altitude (1 m)</li>
<li>Manoeuvres de base (avant, arriere, virages)</li>
<li>Tests d'altitude</li>
<li>Fonctionnalites GPS et autonomes</li>
</ol>
</div>

<div class="lang-en">
<h1>Development Process</h1>

<h2>Phase 1: Design and Component Selection (3 weeks)</h2>
<ul>
<li>Requirements specification</li>
<li>Research and benchmarking</li>
<li>Component selection and compatibility</li>
<li>Budget planning</li>
</ul>

<h2>Phase 2: Assembly and Integration (3 weeks)</h2>
<ul>
<li>Frame assembly</li>
<li>Electronics installation and wiring</li>
<li>Cable management (minimize vibration transmission)</li>
<li>Weight distribution optimization</li>
</ul>

<h2>Phase 3: Configuration and Ground Testing (3 weeks)</h2>
<ul>
<li>Flight controller setup and configuration</li>
<li>Sensor calibration (accelerometer, magnetometer, gyro)</li>
<li>ESC calibration</li>
<li>Radio setup and failsafe configuration</li>
</ul>

<h2>Phase 4: Flight Testing and Tuning (3 weeks)</h2>
<p><strong>Progressive Testing:</strong></p>
<ol>
<li>Tethered hover test</li>
<li>Low-altitude hover (1 m)</li>
<li>Basic maneuvers (forward, backward, turns)</li>
<li>Altitude testing</li>
<li>GPS and autonomous features</li>
</ol>
</div>

<div class="lang-fr">
<h1>Resultats des tests</h1>

<h2>Metriques de performance</h2>
<p>Resultats obtenus avec succes :</p>
<ul>
<li>Vol stationnaire stable avec derive minimale</li>
<li>Controle reactif sur tous les axes</li>
<li>Temps de vol : 8-12 minutes (selon la batterie)</li>
<li>Altitude maximale testee : 50 m</li>
<li>Transitions fluides entre les modes de vol</li>
<li>Maintien GPS et retour au point de depart fiables</li>
</ul>

<h2>Defis surmontes</h2>
<ul>
<li>Vibrations des moteurs affectant les capteurs (resolu avec des amortisseurs)</li>
<li>Oscillations PID (reglees par tests iteratifs)</li>
<li>Temps d'acquisition GPS (optimisation du placement de l'antenne)</li>
<li>Chute de tension de la batterie sous charge (selection appropriee du taux C)</li>
</ul>

<h1>Conclusion</h1>
<p>Ce projet a fourni une experience pratique complete dans le developpement de systemes mecatroniques, du concept initial au vehicule volant entierement fonctionnel. Nous avons integre avec succes des sous-systemes complexes, developpe des algorithmes de controle robustes et atteint un vol autonome stable. Le processus iteratif de conception-test-affinement a enseigne des lecons precieuses en resolution systematique de problemes d'ingenierie et l'importance critique de la securite dans le developpement de vehicules aeriens sans pilote.</p>
</div>

<div class="lang-en">
<h1>Testing Results</h1>

<h2>Performance Metrics</h2>
<p>Successfully achieved:</p>
<ul>
<li>Stable hover with minimal drift</li>
<li>Responsive control across all axes</li>
<li>Flight time: 8-12 minutes (depending on battery)</li>
<li>Maximum altitude tested: 50 m</li>
<li>Smooth transitions between flight modes</li>
<li>Reliable GPS hold and return-to-home</li>
</ul>

<h2>Challenges Overcome</h2>
<ul>
<li>Motor vibrations affecting sensors (solved with vibration dampers)</li>
<li>PID oscillations (tuned through iterative testing)</li>
<li>GPS acquisition time (antenna placement optimization)</li>
<li>Battery voltage sag under load (appropriate C-rating selection)</li>
</ul>

<h1>Conclusion</h1>
<p>This project provided comprehensive hands-on experience in mechatronic system development, from initial concept through fully functional flying vehicle. We successfully integrated complex subsystems, developed robust control algorithms, and achieved stable autonomous flight. The iterative design-test-refine process taught valuable lessons in systematic engineering problem-solving and the critical importance of safety in unmanned aerial vehicle development.</p>
</div>

<!-- Modal -->
<div id="myModal" class="modal">
  <span class="close" onclick="closeModal()">&times;</span>
  <img class="modal-content" id="img01">
</div>

<script>
function openModal(src) {
  var modal = document.getElementById("myModal");
  var modalImg = document.getElementById("img01");
  modal.style.display = "block";
  modalImg.src = src;
}

function closeModal() {
  var modal = document.getElementById("myModal");
  modal.style.display = "none";
}
</script>

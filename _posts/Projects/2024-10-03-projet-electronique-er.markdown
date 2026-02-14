---
layout: default
title: "Advanced Electronics System Design"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
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
<p>Ce projet ouvert offrait une autonomie complete pour concevoir et construire un systeme electronique complexe, du concept au prototype fonctionnel. En travaillant en binome sur 60 heures, nous pouvions choisir parmi differentes applications : enregistreur de donnees multi-capteurs, oscilloscope USB, alimentation de laboratoire programmable ou autres instruments electroniques personnalises. Le projet a synthetise les connaissances en circuits analogiques, systemes numeriques, programmation embarquee et conception de PCB professionnelle.</p>

<h1>Vue d'ensemble du projet</h1>
<p>Ce projet representait l'aboutissement de notre formation en genie electrique, nous imposant de gerer tous les aspects : definition des specifications, selection des composants, conception du schema, routage du PCB, developpement firmware et tests complets. L'accent etait mis sur une implementation de qualite professionnelle et une gestion de projet autonome.</p>

<h2>Types de projets possibles</h2>

<h3>Systemes d'acquisition de donnees</h3>
<p><strong>Enregistreur de donnees multi-capteurs :</strong></p>
<ul>
<li>Entrees capteurs multiples (temperature, pression, humidite)</li>
<li>Amplificateurs d'instrumentation et filtrage</li>
<li>ADC 12-16 bits (STM32 ou ADS1115)</li>
<li>Stockage sur carte SD via SPI</li>
<li>Affichage OLED/LCD</li>
<li>Batterie Li-Ion avec circuit de charge</li>
</ul>

<p><strong>Oscilloscope USB (bande passante 1 MHz) :</strong></p>
<ul>
<li>Attenuateur d'entree commutable (1x, 10x)</li>
<li>Amplificateur differentiel avec protection +/-50V</li>
<li>ADC rapide (echantillonnage MSPS)</li>
<li>Interface USB vers PC</li>
<li>Interface graphique Python pour la visualisation</li>
<li>Circuit de declenchement analogique</li>
</ul>

<h3>Electronique de puissance</h3>
<p><strong>Alimentation de laboratoire programmable :</strong></p>
<ul>
<li>Double sortie : 0-30V, 0-3A par canal</li>
<li>Regulation lineaire ou a decoupage</li>
<li>Controle par microcontroleur avec consigne DAC</li>
<li>Affichage LCD tension/courant</li>
<li>Protection surtension et surintensité</li>
<li>Interface UART pour controle PC</li>
</ul>
</div>

<div class="lang-en">
<h1>Introduction</h1>
<p>This open-ended project provided complete autonomy to design and build a complex electronic system from concept to working prototype. Working in pairs over 60 hours, we could choose from various applications: multi-sensor datalogger, USB oscilloscope, programmable laboratory power supply, or other custom electronic instruments. The project synthesized knowledge from analog circuits, digital systems, embedded programming, and professional PCB design.</p>

<h1>Project Overview</h1>
<p>This project represented the culmination of our electrical engineering training, requiring us to manage every aspect: specifications definition, component selection, schematic design, PCB layout, firmware development, and comprehensive testing. The emphasis was on professional-grade implementation and autonomous project management.</p>

<h2>Example Project Types</h2>

<h3>Data Acquisition Systems</h3>
<p><strong>Multi-Sensor Datalogger:</strong></p>
<ul>
<li>Multiple sensor inputs (temperature, pressure, humidity)</li>
<li>Instrumentation amplifiers and filtering</li>
<li>12-16 bit ADC (STM32 or ADS1115)</li>
<li>SD card storage via SPI</li>
<li>OLED/LCD display</li>
<li>Li-Ion battery with charging circuit</li>
</ul>

<p><strong>USB Oscilloscope (1 MHz bandwidth):</strong></p>
<ul>
<li>Switchable input attenuator (1x, 10x)</li>
<li>Differential amplifier with +/-50V protection</li>
<li>Fast ADC (MSPS sampling)</li>
<li>USB interface to PC</li>
<li>Python GUI for visualization</li>
<li>Analog trigger circuit</li>
</ul>

<h3>Power Electronics</h3>
<p><strong>Programmable Laboratory Power Supply:</strong></p>
<ul>
<li>Dual output: 0-30V, 0-3A per channel</li>
<li>Linear or switching regulation</li>
<li>Microcontroller control with DAC setpoints</li>
<li>LCD display for voltage/current</li>
<li>Overvoltage and overcurrent protection</li>
<li>UART interface for PC control</li>
</ul>
</div>

<div class="lang-fr">
<h1>Methodologie de conception</h1>

<h2>Phase 1 : Specifications et planification</h2>
<p><strong>Definition des exigences :</strong></p>
<ul>
<li>Specifications fonctionnelles detaillees</li>
<li>Objectifs de performance (precision, vitesse, autonomie)</li>
<li>Contraintes (cout, taille, budget energetique)</li>
</ul>

<p><strong>Etude de faisabilite :</strong></p>
<ul>
<li>Recherche et selection de composants</li>
<li>Evaluation des solutions techniques</li>
<li>Estimation des couts et planification de la nomenclature</li>
</ul>

<h2>Phase 2 : Conception electronique</h2>
<p><strong>Schema fonctionnel :</strong></p>
<ul>
<li>Decomposition de l'architecture systeme</li>
<li>Definitions des interfaces entre blocs</li>
<li>Analyse des flux de signaux</li>
</ul>

<p><strong>Conception du schema (KiCad/Altium) :</strong></p>
<ul>
<li>Section alimentation (regulateurs, decouplage)</li>
<li>Circuits de conditionnement analogique</li>
<li>Microcontroleur et peripheriques</li>
<li>Connecteurs et interfaces</li>
<li>Selection de composants avec references verifiees (Mouser/Digi-Key)</li>
</ul>

<h2>Phase 3 : Conception du PCB</h2>
<p><strong>Strategie de layout :</strong></p>
<ul>
<li>PCB 2 ou 4 couches selon la complexite</li>
<li>Placement des composants (considerations thermiques, CEM)</li>
<li>Routage des pistes : largeur pour capacite en courant, espacement pour la tension</li>
<li>Plans de masse et d'alimentation</li>
<li>Validation par Design Rule Check (DRC)</li>
</ul>

<h2>Phase 4 : Developpement firmware</h2>
<p><strong>Logiciel embarque :</strong></p>
<ul>
<li>Configuration des peripheriques (ADC, I2C, UART, SPI)</li>
<li>Acquisition et traitement de donnees</li>
<li>Algorithmes de calibration</li>
<li>Interface utilisateur (boutons, LCD)</li>
<li>Protocoles de communication</li>
</ul>

<h2>Phase 5 : Tests et validation</h2>
<p><strong>Tests unitaires :</strong></p>
<ul>
<li>Verification de l'alimentation (tensions, ondulation)</li>
<li>Conditionnement analogique (gain, offset, bruit)</li>
<li>Communication numerique (I2C, SPI, UART)</li>
<li>Validation individuelle des sous-systemes</li>
</ul>
</div>

<div class="lang-en">
<h1>Design Methodology</h1>

<h2>Phase 1: Specifications and Planning</h2>
<p><strong>Requirements Definition:</strong></p>
<ul>
<li>Detailed functional specifications</li>
<li>Performance targets (accuracy, speed, autonomy)</li>
<li>Constraints (cost, size, power budget)</li>
</ul>

<p><strong>Feasibility Study:</strong></p>
<ul>
<li>Component research and selection</li>
<li>Technical solution evaluation</li>
<li>Cost estimation and BOM planning</li>
</ul>

<h2>Phase 2: Electronic Design</h2>
<p><strong>Functional Block Diagram:</strong></p>
<ul>
<li>System architecture decomposition</li>
<li>Interface definitions between blocks</li>
<li>Signal flow analysis</li>
</ul>

<p><strong>Schematic Design (KiCad/Altium):</strong></p>
<ul>
<li>Power supply section (regulators, decoupling)</li>
<li>Analog conditioning circuits</li>
<li>Microcontroller and peripherals</li>
<li>Connectors and interfaces</li>
<li>Component selection with verified part numbers (Mouser/Digi-Key)</li>
</ul>

<h2>Phase 3: PCB Design</h2>
<p><strong>Layout Strategy:</strong></p>
<ul>
<li>2 or 4-layer PCB depending on complexity</li>
<li>Component placement (thermal, EMC considerations)</li>
<li>Trace routing: width for current capacity, spacing for voltage</li>
<li>Ground and power planes</li>
<li>Design Rule Check (DRC) validation</li>
</ul>

<h2>Phase 4: Firmware Development</h2>
<p><strong>Embedded Software:</strong></p>
<ul>
<li>Peripheral configuration (ADC, I2C, UART, SPI)</li>
<li>Data acquisition and processing</li>
<li>Calibration algorithms</li>
<li>User interface (buttons, LCD)</li>
<li>Communication protocols</li>
</ul>

<h2>Phase 5: Testing and Validation</h2>
<p><strong>Unit Testing:</strong></p>
<ul>
<li>Power supply verification (voltages, ripple)</li>
<li>Analog conditioning (gain, offset, noise)</li>
<li>Digital communication (I2C, SPI, UART)</li>
<li>Individual subsystem validation</li>
</ul>
</div>

<div class="lang-fr">
<h1>Resultats et analyse</h1>
<p>Le systeme acheve a atteint ou depasse les specifications de conception, demontrant une integration reussie des sous-systemes analogiques et numeriques. Les principaux defis comprenaient la minimisation du bruit dans les circuits analogiques sensibles, l'optimisation de la consommation pour le fonctionnement sur batterie et l'obtention d'une communication fiable entre sous-systemes.</p>
<p>La validation des performances a confirme :</p>
<ul>
<li>Precision de mesure conforme aux objectifs de conception</li>
<li>Fonctionnement stable dans les conditions specifiees</li>
<li>Acquisition et stockage de donnees fiables</li>
<li>Interface utilisateur conviviale</li>
</ul>

<h1>Conclusion</h1>
<p>Ce projet a fourni une experience complete dans le developpement de systemes electroniques professionnels, du concept au prototype valide. La nature autonome du travail a developpe des competences critiques en gestion de projet, incluant la planification, la resolution de problemes et la documentation technique. Le prototype fonctionnel demontre notre capacite a livrer des systemes electroniques complets et fonctionnels repondant aux exigences du monde reel.</p>
</div>

<div class="lang-en">
<h1>Results and Analysis</h1>
<p>The completed system met or exceeded design specifications, demonstrating successful integration of analog and digital subsystems. Key challenges included minimizing noise in sensitive analog circuits, optimizing power consumption for battery operation, and achieving reliable communication between subsystems.</p>
<p>Performance validation confirmed:</p>
<ul>
<li>Measurement accuracy within design targets</li>
<li>Stable operation across specified conditions</li>
<li>Reliable data acquisition and storage</li>
<li>User-friendly interface operation</li>
</ul>

<h1>Conclusion</h1>
<p>This project provided comprehensive experience in professional electronic system development, from concept through validated prototype. The autonomous nature of the work developed critical project management skills including planning, problem-solving, and technical documentation. The working prototype demonstrates our ability to deliver complete, functional electronic systems meeting real-world requirements.</p>
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

---
layout: default
title: "Autonomous Energy Management System"
date:   2024-10-02 10:56:03 +0200
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
<p>Ce projet specialise en energie portait sur la conception de systemes autonomes avec gestion intelligente de l'alimentation et integration d'energies renouvelables. En travaillant en binome sur 60 heures, nous avons developpe des dispositifs alimentes par batterie avec charge solaire, consommation optimisee et algorithmes sophistiques de gestion energetique. Les exemples de projets comprenaient des cubes LED autonomes, des stations meteo solaires pour l'IoT et des systemes d'eclairage intelligents.</p>

<h1>Vue d'ensemble du projet</h1>
<p>Le projet a synthetise les connaissances en electronique de puissance, systemes d'energie renouvelable, programmation embarquee et techniques de conception basse consommation. L'objectif etait de creer des systemes capables de fonctionner indefiniment sur de l'energie recoltee ou d'atteindre une autonomie maximale a partir de batterie grace a une gestion intelligente de la consommation.</p>

<h2>Types de projets possibles</h2>

<h3>Systemes d'affichage autonomes</h3>
<p><strong>Cube LED 8x8x8 :</strong></p>
<ul>
<li>512 LEDs RGB (WS2812B) en matrice 3D</li>
<li>Microcontroleur STM32 pour le controle des animations</li>
<li>Batterie Li-Ion 18650 (3.7V, 3000 mAh)</li>
<li>Charge par panneau solaire (5W)</li>
<li>Autonomie cible : 2-4 heures d'utilisation continue</li>
<li>Animations et effets programmes</li>
</ul>

<h3>Systemes IoT autonomes</h3>
<p><strong>Station meteo ultra-basse consommation :</strong></p>
<ul>
<li>Capteurs environnementaux (temperature, pression, humidite)</li>
<li>STM32L0 ou ESP32 en mode deep-sleep</li>
<li>Transmission LoRa (donnees minimales)</li>
<li>Panneau solaire 1W</li>
<li>Supercondensateur ou petite batterie</li>
<li>Objectif : autonomie illimitee avec ensoleillement</li>
</ul>
</div>

<div class="lang-en">
<h1>Introduction</h1>
<p>This specialized energy project focused on designing autonomous systems with intelligent power management and renewable energy integration. Working in pairs over 60 hours, we developed battery-powered devices with solar charging, optimized power consumption, and sophisticated energy management algorithms. Example projects included autonomous LED cubes, solar-powered IoT weather stations, and intelligent lighting systems.</p>

<h1>Project Overview</h1>
<p>The project synthesized knowledge from power electronics, renewable energy systems, embedded programming, and low-power design techniques. The goal was to create systems capable of operating indefinitely on harvested energy or achieving maximum autonomy from battery power through intelligent consumption management.</p>

<h2>Example Project Types</h2>

<h3>Autonomous Display Systems</h3>
<p><strong>8x8x8 LED Cube:</strong></p>
<ul>
<li>512 RGB LEDs (WS2812B) in 3D matrix</li>
<li>STM32 microcontroller for animation control</li>
<li>Li-Ion 18650 battery (3.7V, 3000 mAh)</li>
<li>Solar panel charging (5W)</li>
<li>Target autonomy: 2-4 hours continuous use</li>
<li>Programmed animations and effects</li>
</ul>

<h3>IoT Autonomous Systems</h3>
<p><strong>Ultra-Low-Power Weather Station:</strong></p>
<ul>
<li>Environmental sensors (temperature, pressure, humidity)</li>
<li>STM32L0 or ESP32 in deep-sleep mode</li>
<li>LoRa transmission (minimal data)</li>
<li>1W solar panel</li>
<li>Supercapacitor or small battery</li>
<li>Target: indefinite autonomy with sunlight</li>
</ul>
</div>

<div class="lang-fr">
<h1>Bilan energetique et dimensionnement</h1>

<h2>Analyse de la consommation</h2>
<p>Calcul detaille de la consommation en courant pour chaque sous-systeme :</p>
<p><strong>Exemple : Cube LED</strong></p>
<ul>
<li>STM32 actif : 50 mA</li>
<li>STM32 veille : 2 mA</li>
<li>LEDs en moyenne (animations) : 400 mA</li>
<li>Total moyen : 500 mA</li>
<li>Autonomie : 3000 mAh / 500 mA = 6 heures</li>
</ul>

<h2>Dimensionnement de la batterie</h2>
<ul>
<li>Capacite requise (mAh)</li>
<li>Selection de la tension (Li-Ion 3.7V, LiFePO4 3.2V, Plomb 12V)</li>
<li>Choix de la chimie selon l'application</li>
<li>Considerations sur les cycles charge/decharge</li>
</ul>

<h2>Dimensionnement du panneau solaire</h2>
<p>Formule : P = Energie journaliere / (Heures d'ensoleillement x Rendement)</p>
<p>Exemple de calcul :</p>
<ul>
<li>Energie journaliere : 10 Wh</li>
<li>Heures de soleil : 4h</li>
<li>Rendement : 80%</li>
<li>Panneau requis : P = 10 / (4 x 0.8) = 3W minimum</li>
</ul>
</div>

<div class="lang-en">
<h1>Energy Budget and Sizing</h1>

<h2>Power Consumption Analysis</h2>
<p>Detailed current consumption calculation for each subsystem:</p>
<p><strong>Example: LED Cube</strong></p>
<ul>
<li>STM32 active: 50 mA</li>
<li>STM32 sleep: 2 mA</li>
<li>LEDs average (animations): 400 mA</li>
<li>Total average: 500 mA</li>
<li>Battery life: 3000 mAh / 500 mA = 6 hours</li>
</ul>

<h2>Battery Sizing</h2>
<ul>
<li>Capacity requirements (mAh)</li>
<li>Voltage selection (Li-Ion 3.7V, LiFePO4 3.2V, Lead-acid 12V)</li>
<li>Chemistry choice based on application</li>
<li>Charge/discharge cycle considerations</li>
</ul>

<h2>Solar Panel Dimensioning</h2>
<p>Formula: P = Daily Energy / (Sunlight Hours x Efficiency)</p>
<p>Example calculation:</p>
<ul>
<li>Daily energy: 10 Wh</li>
<li>Sun hours: 4h</li>
<li>Efficiency: 80%</li>
<li>Required panel: P = 10 / (4 x 0.8) = 3W minimum</li>
</ul>
</div>

<div class="lang-fr">
<h1>Conception de l'alimentation</h1>

<h2>Charge de batterie</h2>
<p><strong>Charge Li-Ion :</strong></p>
<ul>
<li>Chargeurs lineaires : TP4056, MCP73831 (&lt; 1A)</li>
<li>Chargeurs a decoupage : LTC4011, BQ24075 (&gt; 1A)</li>
<li>Protection : surcharge, decharge profonde, court-circuit</li>
</ul>

<p><strong>Controleur de charge :</strong></p>
<ul>
<li>Algorithme Courant Constant / Tension Constante (CC/CV)</li>
<li>Surveillance de la temperature (thermistance NTC)</li>
<li>Indication de l'etat de charge</li>
<li>MPPT (Maximum Power Point Tracking) pour l'optimisation solaire</li>
</ul>

<h2>Convertisseurs DC-DC</h2>
<p><strong>Convertisseur Buck (abaisseur) :</strong></p>
<ul>
<li>Batterie vers 3.3V/5V pour le microcontroleur</li>
<li>Rendement : 85-95%</li>
<li>Exemples : TPS54302 (3A), LM2596</li>
</ul>

<p><strong>Convertisseur Boost (elevateur) :</strong></p>
<ul>
<li>Basse tension batterie vers tension plus elevee</li>
<li>Pour drivers LED ou peripheriques 5V</li>
<li>Exemples : MT3608, TPS61070</li>
</ul>

<h2>Gestion basse consommation du microcontroleur</h2>
<p><strong>Modes de veille :</strong></p>
<ul>
<li>Sleep : CPU arrete, peripheriques actifs</li>
<li>Stop : Toutes les horloges arretees, RAM conservee</li>
<li>Standby : Consommation minimale, RAM minimale</li>
</ul>

<p><strong>Techniques d'optimisation :</strong></p>
<ul>
<li>Reveil par RTC pour mesures periodiques</li>
<li>Desactivation des peripheriques inutilises</li>
<li>Reduction de la frequence CPU quand possible</li>
<li>Architecture pilotee par evenements</li>
</ul>
</div>

<div class="lang-en">
<h1>Power Supply Design</h1>

<h2>Battery Charging</h2>
<p><strong>Li-Ion Charging:</strong></p>
<ul>
<li>Linear chargers: TP4056, MCP73831 (&lt; 1A)</li>
<li>Switching chargers: LTC4011, BQ24075 (&gt; 1A)</li>
<li>Protection: overcharge, deep discharge, short circuit</li>
</ul>

<p><strong>Charge Controller:</strong></p>
<ul>
<li>Constant Current / Constant Voltage (CC/CV) algorithm</li>
<li>Temperature monitoring (NTC thermistor)</li>
<li>Charge status indication</li>
<li>MPPT (Maximum Power Point Tracking) for solar optimization</li>
</ul>

<h2>DC-DC Converters</h2>
<p><strong>Buck Converter (Step-Down):</strong></p>
<ul>
<li>Battery to 3.3V/5V for microcontroller</li>
<li>Efficiency: 85-95%</li>
<li>Examples: TPS54302 (3A), LM2596</li>
</ul>

<p><strong>Boost Converter (Step-Up):</strong></p>
<ul>
<li>Low battery voltage to higher voltage</li>
<li>For LED drivers or 5V peripherals</li>
<li>Examples: MT3608, TPS61070</li>
</ul>

<h2>Low-Power Microcontroller Management</h2>
<p><strong>Sleep Modes:</strong></p>
<ul>
<li>Sleep: CPU stopped, peripherals active</li>
<li>Stop: All clocks stopped, RAM retained</li>
<li>Standby: Lowest power, minimal RAM</li>
</ul>

<p><strong>Optimization Techniques:</strong></p>
<ul>
<li>RTC wake-up for periodic measurements</li>
<li>Disable unused peripherals</li>
<li>Reduce CPU frequency when possible</li>
<li>Event-driven architecture</li>
</ul>
</div>

<div style="display: flex; justify-content: center; gap: 15px; margin: 30px 0; flex-wrap: wrap;">
  <img src="/img/BE_Energy_Connected_Object/dist_2_4.png" alt="Distance Test 2.4 GHz" style="width: 45%;" onclick="openModal(this.src)"/>
  <img src="/img/BE_Energy_Connected_Object/dist_8_6.png" alt="Distance Test 8.6 GHz" style="width: 45%;" onclick="openModal(this.src)"/>
</div>

<div class="lang-fr">
<h1>Resultats et analyse</h1>
<p>L'autonomie cible a ete atteinte avec succes grace a une gestion optimisee de l'alimentation. La charge solaire a fourni une energie suffisante pour un fonctionnement continu dans des conditions normales d'ensoleillement. Les modes basse consommation ont reduit la consommation en veille de 95%, prolongeant significativement l'autonomie.</p>
<p>Resultats cles :</p>
<ul>
<li>L'utilisation correcte des modes de veille est critique pour l'autonomie</li>
<li>Les convertisseurs a decoupage sont bien superieurs aux regulateurs lineaires</li>
<li>L'orientation du panneau solaire affecte significativement la charge</li>
<li>Le dimensionnement de la batterie doit inclure une marge de securite</li>
</ul>

<h1>Conclusion</h1>
<p>Ce projet a fourni une experience complete dans la conception de systemes autonomes avec integration d'energies renouvelables. Nous avons reussi a equilibrer les exigences de performance avec les contraintes de consommation, demontrant des strategies efficaces de gestion energetique. Le prototype fonctionnel valide notre capacite a concevoir des systemes electroniques durables et alimentes par batterie pour un deploiement reel.</p>
</div>

<div class="lang-en">
<h1>Results and Analysis</h1>
<p>Successfully achieved target autonomy with optimized power management. Solar charging provided sufficient energy for continuous operation under normal sunlight conditions. Low-power modes reduced standby consumption by 95%, significantly extending battery life.</p>
<p>Key findings:</p>
<ul>
<li>Proper sleep mode usage critical for autonomy</li>
<li>Switching converters far superior to linear regulators</li>
<li>Solar panel orientation significantly affects charging</li>
<li>Battery capacity sizing must include safety margin</li>
</ul>

<h1>Conclusion</h1>
<p>This project provided comprehensive experience in autonomous system design with renewable energy integration. We successfully balanced performance requirements with power consumption constraints, demonstrating effective energy management strategies. The working prototype validates our ability to design sustainable, battery-powered electronic systems for real-world deployment.</p>
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

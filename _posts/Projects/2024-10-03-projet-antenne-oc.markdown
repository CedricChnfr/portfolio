---
layout: default
title: "Antenna Design for Connected Objects"
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
<p>Ce projet tutore portait sur la conception et l'optimisation d'une antenne pour des applications IoT fonctionnant dans les bandes ISM (433/868 MHz ou 2.4 GHz). Le projet englobait le cycle complet de conception, des calculs theoriques et simulations electromagnetiques a la fabrication du PCB et a la caracterisation professionnelle par des mesures VNA et en chambre anechoique.</p>

<h1>Vue d'ensemble du projet</h1>
<p>L'objectif etait de developper une antenne compacte et efficace pour des applications LoRa, Sigfox, WiFi ou Bluetooth. Les specifications cles comprenaient un S11 &lt; -10 dB, un gain omnidirectionnel &gt; 0 dBi et une adaptation d'impedance a 50 ohms.</p>

<h2>Specifications de conception</h2>

<p><strong>Frequences cibles :</strong></p>
<ul>
<li>433 MHz ou 868 MHz (LoRa/Sigfox)</li>
<li>2.4 GHz (WiFi/Bluetooth)</li>
<li>Bande passante : +/-10 MHz minimum</li>
</ul>

<p><strong>Exigences de performance :</strong></p>
<ul>
<li>Coefficient de reflexion : S11 &lt; -10 dB</li>
<li>Gain : &gt; 0 dBi (omnidirectionnel)</li>
<li>Impedance : 50 ohms</li>
<li>Efficacite : &gt; 70%</li>
</ul>

<h2>Topologies d'antennes etudiees</h2>

<h3>Pour 433/868 MHz :</h3>
<ul>
<li>Monopole quart d'onde (lambda/4 : 7-17 cm)</li>
<li>Dipole replie</li>
<li>Antenne helicoidale (compacte)</li>
<li>PIFA (Planar Inverted-F Antenna)</li>
</ul>

<h3>Pour 2.4 GHz :</h3>
<ul>
<li>Patch rectangulaire (3x4 cm)</li>
<li>Dipole imprime</li>
<li>Antenne meandre (compacte)</li>
<li>Yagi (gain eleve)</li>
</ul>
</div>

<div class="lang-en">
<h1>Introduction</h1>
<p>This tutored project focused on designing and optimizing an antenna for IoT applications operating in ISM bands (433/868 MHz or 2.4 GHz). The project encompassed the complete design cycle from theoretical calculations and electromagnetic simulations to PCB fabrication and professional characterization using VNA and anechoic chamber measurements.</p>

<h1>Project Overview</h1>
<p>The goal was to develop a compact, efficient antenna for LoRa, Sigfox, WiFi, or Bluetooth applications. Key specifications included S11 &lt; -10 dB, omnidirectional gain &gt; 0 dBi, and 50 ohm impedance matching.</p>

<h2>Design Specifications</h2>

<p><strong>Target Frequencies:</strong></p>
<ul>
<li>433 MHz or 868 MHz (LoRa/Sigfox)</li>
<li>2.4 GHz (WiFi/Bluetooth)</li>
<li>Bandwidth: +/-10 MHz minimum</li>
</ul>

<p><strong>Performance Requirements:</strong></p>
<ul>
<li>Return Loss: S11 &lt; -10 dB</li>
<li>Gain: &gt; 0 dBi (omnidirectional)</li>
<li>Impedance: 50 ohm</li>
<li>Efficiency: &gt; 70%</li>
</ul>

<h2>Antenna Topologies Studied</h2>

<h3>For 433/868 MHz:</h3>
<ul>
<li>Quarter-wave monopole (lambda/4: 7-17 cm)</li>
<li>Folded dipole</li>
<li>Helical antenna (compact)</li>
<li>PIFA (Planar Inverted-F Antenna)</li>
</ul>

<h3>For 2.4 GHz:</h3>
<ul>
<li>Rectangular patch (3x4 cm)</li>
<li>Printed dipole</li>
<li>Meandered antenna (compact)</li>
<li>Yagi (high gain)</li>
</ul>
</div>

<div class="lang-fr">
<h1>Conception et simulation</h1>

<h2>Modelisation electromagnetique</h2>
<p>Nous avons utilise CST Studio ou HFSS pour la simulation electromagnetique 3D. Le processus de conception comprenait :</p>
</div>

<div class="lang-en">
<h1>Design and Simulation</h1>

<h2>Electromagnetic Modeling</h2>
<p>We used CST Studio or HFSS for 3D electromagnetic simulation. The design process included:</p>
</div>

<div style="display: flex; justify-content: center; gap: 15px; margin: 30px 0; flex-wrap: wrap;">
  <img src="/img/BE_Antenne/Antenne-phase-1_page1_img1.png" alt="Antenna Design Phase 1" style="width: 45%;" onclick="openModal(this.src)"/>
  <img src="/img/BE_Antenne/Antenne-phase-1_page2_img1.png" alt="Antenna Specifications" style="width: 45%;" onclick="openModal(this.src)"/>
</div>

<div class="lang-fr">
<p><strong>Dimensionnement initial :</strong></p>
<ul>
<li>Formules analytiques pour les dimensions du patch/monopole</li>
<li>Exemple : patch 2.4 GHz sur substrat FR-4 (epsilon_r=4.4) : L environ 3 cm, W environ 4 cm</li>
</ul>

<p><strong>Optimisation :</strong></p>
<ul>
<li>Balayages parametriques sur les dimensions critiques</li>
<li>Optimisation du S11 a la frequence centrale</li>
<li>Analyse du diagramme de rayonnement</li>
<li>Conception du reseau d'adaptation d'impedance (stub, L-match)</li>
</ul>
</div>

<div class="lang-en">
<p><strong>Initial Dimensioning:</strong></p>
<ul>
<li>Analytical formulas for patch/monopole dimensions</li>
<li>Example: 2.4 GHz patch on FR-4 substrate (epsilon_r=4.4): L approx. 3 cm, W approx. 4 cm</li>
</ul>

<p><strong>Optimization:</strong></p>
<ul>
<li>Parametric sweeps on critical dimensions</li>
<li>S11 optimization at center frequency</li>
<li>Radiation pattern analysis</li>
<li>Impedance matching network design (stub, L-match)</li>
</ul>
</div>

<div style="text-align: center; margin: 30px 0;">
  <img src="/img/BE_Antenne/Antenne-phase-1_page3_img1.png" alt="Simulation Setup" style="width: 60%;" onclick="openModal(this.src)"/>
</div>

<div class="lang-fr">
<p><strong>Resultats de simulation :</strong></p>
<ul>
<li>S11 &lt; -15 dB a f0</li>
<li>Gain : 6-8 dBi (patch), 2 dBi (monopole)</li>
<li>Diagramme de rayonnement 3D</li>
<li>Impedance d'entree : Z = 50 + j0 ohms</li>
</ul>
</div>

<div class="lang-en">
<p><strong>Simulation Results:</strong></p>
<ul>
<li>S11 &lt; -15 dB at f0</li>
<li>Gain: 6-8 dBi (patch), 2 dBi (monopole)</li>
<li>3D radiation pattern</li>
<li>Input impedance: Z = 50 + j0 ohm</li>
</ul>
</div>

<div style="display: flex; justify-content: center; gap: 15px; margin: 30px 0; flex-wrap: wrap;">
  <img src="/img/BE_Antenne/Antenne-phase-2_page4_img1.jpeg" alt="Simulation Results" style="width: 45%;" onclick="openModal(this.src)"/>
  <img src="/img/BE_Antenne/Antenne-phase-2_page4_img2.jpeg" alt="Radiation Pattern" style="width: 45%;" onclick="openModal(this.src)"/>
</div>

<div class="lang-fr">
<h1>Fabrication du PCB</h1>

<h2>Conception et fabrication</h2>
<ul>
<li>Conception sous KiCad/Altium Designer</li>
<li>Layout precis correspondant aux dimensions optimisees</li>
<li>Substrat : FR-4 (epsilon_r=4.4) ou Rogers pour de meilleures performances</li>
<li>Fabrication par PCBWay/JLCPCB</li>
<li>Soudure du connecteur SMA</li>
<li>Inspection visuelle et test de continuite</li>
</ul>

<h1>Caracterisation et tests</h1>

<h2>Mesures au VNA</h2>
<p>Utilisation d'un analyseur de reseau vectoriel avec calibration SOLT :</p>
<ul>
<li>Parametre S11 (coefficient de reflexion) en fonction de la frequence</li>
<li>Abaque de Smith pour l'analyse d'impedance</li>
<li>Comparaison simulation vs mesure</li>
<li>Verification de la bande passante</li>
</ul>
</div>

<div class="lang-en">
<h1>PCB Fabrication</h1>

<h2>Design and Manufacturing</h2>
<ul>
<li>Designed in KiCad/Altium Designer</li>
<li>Precise layout matching optimized dimensions</li>
<li>Substrate: FR-4 (epsilon_r=4.4) or Rogers for better performance</li>
<li>Manufactured by PCBWay/JLCPCB</li>
<li>SMA connector soldering</li>
<li>Visual inspection and continuity testing</li>
</ul>

<h1>Characterization and Testing</h1>

<h2>VNA Measurements</h2>
<p>Using Vector Network Analyzer with SOLT calibration:</p>
<ul>
<li>S11 parameter (reflection coefficient) vs frequency</li>
<li>Smith chart for impedance analysis</li>
<li>Comparison simulation vs measurement</li>
<li>Bandwidth verification</li>
</ul>
</div>

<div style="text-align: center; margin: 30px 0;">
  <img src="/img/BE_Antenne/Antenne-phase-3_page1_img1.png" alt="VNA Measurements" style="width: 70%;" onclick="openModal(this.src)"/>
</div>

<div class="lang-fr">
<h2>Tests en chambre anechoique</h2>
<p>Mesures professionnelles en chambre RF :</p>
<ul>
<li>Diagrammes de rayonnement (plan E, plan H)</li>
<li>Mesure du gain absolu</li>
<li>Caracteristiques de polarisation</li>
<li>Niveaux de polarisation croisee</li>
</ul>
</div>

<div class="lang-en">
<h2>Anechoic Chamber Testing</h2>
<p>Professional RF chamber measurements:</p>
<ul>
<li>Radiation patterns (E-plane, H-plane)</li>
<li>Absolute gain measurement</li>
<li>Polarization characteristics</li>
<li>Cross-polarization levels</li>
</ul>
</div>

<div style="display: flex; justify-content: center; gap: 15px; margin: 30px 0; flex-wrap: wrap;">
  <img src="/img/BE_Antenne/Antenne-phase-3_page2_img1.png" alt="Anechoic Chamber Setup" style="width: 45%;" onclick="openModal(this.src)"/>
  <img src="/img/BE_Antenne/Antenne-phase-3_page2_img2.png" alt="Measurement Results" style="width: 45%;" onclick="openModal(this.src)"/>
</div>

<div class="lang-fr">
<h2>Tests de liaison en conditions reelles</h2>
<ul>
<li>Connexion a un module LoRa/WiFi</li>
<li>Tests de portee avec mesures RSSI</li>
<li>Comparaison avec une antenne commerciale</li>
<li>Validation des performances en environnement reel</li>
</ul>

<h1>Resultats et analyse</h1>
<p>L'antenne fabriquee a respecte les specifications avec un S11 &lt; -12 dB a la frequence cible. Le gain mesure correspondait aux simulations a +/-1 dB pres. Les tests de liaison en conditions reelles ont demontre une portee de communication efficace pour l'application IoT visee.</p>
<p>Les enseignements cles comprenaient l'impact des proprietes du substrat sur les performances, l'importance des tolerances de fabrication precises et les effets du plan de masse sur les diagrammes de rayonnement.</p>

<h1>Conclusion</h1>
<p>Ce projet a fourni une experience pratique complete en conception d'antennes RF, de l'analyse theorique a la caracterisation professionnelle. Nous avons concu, fabrique et valide avec succes une antenne fonctionnelle pour des applications IoT, demonstrant le flux de travail complet d'ingenierie pour les systemes de communication sans fil.</p>
</div>

<div class="lang-en">
<h2>Real-World Link Testing</h2>
<ul>
<li>Connected to LoRa/WiFi module</li>
<li>Range testing with RSSI measurements</li>
<li>Comparison with commercial antenna</li>
<li>Performance validation in operating environment</li>
</ul>

<h1>Results and Analysis</h1>
<p>The fabricated antenna met specifications with S11 &lt; -12 dB at the target frequency. Measured gain matched simulations within +/-1 dB. Real-world link tests demonstrated effective communication range for the target IoT application.</p>
<p>Key learnings included the impact of substrate properties on performance, importance of precise manufacturing tolerances, and ground plane effects on radiation patterns.</p>

<h1>Conclusion</h1>
<p>This project provided comprehensive hands-on experience in RF antenna design, from theoretical analysis through professional characterization. We successfully designed, fabricated, and validated a functional antenna for IoT applications, demonstrating the complete engineering workflow for wireless communication systems.</p>
</div>

<div class="lang-fr">
<h1>Documentation du projet</h1>
<p>Ci-dessous se trouvent les trois phases de la documentation du projet d'antenne. Vous pouvez faire defiler chaque PDF cote a cote.</p>
</div>

<div class="lang-en">
<h1>Project Documentation</h1>
<p>Below are the three phases of the antenna project documentation. You can scroll through each PDF side by side.</p>
</div>

<div style="display: flex; gap: 15px; margin: 40px 0; overflow-x: auto; padding-bottom: 20px;">
  <div style="flex: 1; min-width: 400px;">
    <h3 style="color: #667eea; text-align: center; margin-bottom: 10px;">Phase 1</h3>
    <embed src="/projets-pdf/antenne/Antenne-phase-1.pdf"
           type="application/pdf"
           width="100%"
           height="800px"
           style="border: 2px solid #667eea; border-radius: 8px;" />
  </div>

  <div style="flex: 1; min-width: 400px;">
    <h3 style="color: #667eea; text-align: center; margin-bottom: 10px;">Phase 2</h3>
    <embed src="/projets-pdf/antenne/Antenne-phase-2.pdf"
           type="application/pdf"
           width="100%"
           height="800px"
           style="border: 2px solid #667eea; border-radius: 8px;" />
  </div>

  <div style="flex: 1; min-width: 400px;">
    <h3 style="color: #667eea; text-align: center; margin-bottom: 10px;">Phase 3</h3>
    <embed src="/projets-pdf/antenne/Antenne-phase-3.pdf"
           type="application/pdf"
           width="100%"
           height="800px"
           style="border: 2px solid #667eea; border-radius: 8px;" />
  </div>
</div>

<style>
@media (max-width: 1200px) {
  div[style*="display: flex"] {
    flex-direction: column;
  }
  div[style*="min-width: 400px"] {
    min-width: 100%;
  }
}
</style>

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

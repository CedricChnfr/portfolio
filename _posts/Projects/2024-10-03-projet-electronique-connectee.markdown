---
layout: default
title: "Connected Electronics System (RF Communication)"
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
<p>Ce projet de synthese complet a consiste a concevoir et implementer un systeme de communication sans fil RF de A a Z. Le systeme comprenait des modules emetteur et recepteur separes, integrant le conditionnement de capteurs analogiques, le traitement de donnees par microcontroleur, la modulation numerique (FSK/ASK), l'amplification RF et des antennes personnalisees pour realiser une transmission de donnees sans fil fiable sur 50 a 100 metres.</p>

<h1>Vue d'ensemble du projet</h1>
<p>En travaillant en binome sur 60 heures, nous avons developpe une liaison sans fil full-duplex ou half-duplex operant dans la bande ISM (433 ou 868 MHz). Le projet a synthetise les connaissances en electronique analogique, systemes numeriques, circuits RF, telecommunications et programmation embarquee.</p>

<h2>Architecture du systeme</h2>

<h3>Chaine d'emission</h3>
<ol>
<li><strong>Acquisition de donnees :</strong> Capteurs (temperature, pression, accelerometre) avec conditionnement analogique</li>
<li><strong>Traitement :</strong> Microcontroleur STM32 pour la mise en trame des donnees (preambule + donnees + CRC)</li>
<li><strong>Modulation :</strong> Implementation FSK (Frequency Shift Keying) ou ASK (Amplitude Shift Keying)</li>
<li><strong>Amplification RF :</strong> Amplificateur de puissance delivrant +10 a +20 dBm</li>
<li><strong>Antenne :</strong> Monopole ou patch adapte a 50 ohms</li>
</ol>

<h3>Chaine de reception</h3>
<ol>
<li><strong>Antenne :</strong> Antenne de reception adaptee a 50 ohms</li>
<li><strong>LNA :</strong> Amplificateur faible bruit (gain 15-20 dB, facteur de bruit &lt; 3 dB)</li>
<li><strong>Demodulation :</strong> Detecteur FSK/ASK avec comparateur a seuil</li>
<li><strong>Traitement :</strong> STM32 pour la synchronisation de trame et la validation CRC</li>
<li><strong>Affichage :</strong> Sortie LCD/OLED ou UART vers PC</li>
</ol>
</div>

<div class="lang-en">
<h1>Introduction</h1>
<p>This comprehensive synthesis project involved designing and implementing a complete RF wireless communication system from scratch. The system featured separate transmitter and receiver modules, integrating analog sensor conditioning, microcontroller data processing, digital modulation (FSK/ASK), RF amplification, and custom antennas to achieve reliable wireless data transmission over 50-100 meters.</p>

<h1>Project Overview</h1>
<p>Working in pairs over 60 hours, we developed a full duplex or half-duplex wireless link operating in the ISM band (433 or 868 MHz). The project synthesized knowledge from analog electronics, digital systems, RF circuits, telecommunications, and embedded programming.</p>

<h2>System Architecture</h2>

<h3>Transmitter Chain</h3>
<ol>
<li><strong>Data Acquisition:</strong> Sensors (temperature, pressure, accelerometer) with analog conditioning</li>
<li><strong>Processing:</strong> STM32 microcontroller for data framing (preamble + data + CRC)</li>
<li><strong>Modulation:</strong> FSK (Frequency Shift Keying) or ASK (Amplitude Shift Keying) implementation</li>
<li><strong>RF Amplification:</strong> Power amplifier delivering +10 to +20 dBm</li>
<li><strong>Antenna:</strong> Matched monopole or patch antenna (50 ohm)</li>
</ol>

<h3>Receiver Chain</h3>
<ol>
<li><strong>Antenna:</strong> Receiving antenna with 50 ohm impedance matching</li>
<li><strong>LNA:</strong> Low Noise Amplifier (15-20 dB gain, NF &lt; 3 dB)</li>
<li><strong>Demodulation:</strong> FSK/ASK detector with threshold comparator</li>
<li><strong>Processing:</strong> STM32 for frame synchronization and CRC validation</li>
<li><strong>Display:</strong> LCD/OLED or UART output to PC</li>
</ol>
</div>

<div class="lang-fr">
<h1>Conception et implementation</h1>

<h2>Bilan de liaison RF</h2>
<p>Calcul a l'aide de la formule de transmission de Friis :</p>
<ul>
<li>Puissance d'emission : +10 dBm (10 mW)</li>
<li>Frequence : 433 MHz ou 868 MHz</li>
<li>Gains d'antenne : environ 2 dBi chacun</li>
<li>Portee cible : &gt; 50 m en exterieur</li>
<li>Debit : 1-10 kbps</li>
</ul>

<h2>Schemas de modulation</h2>
<p><strong>FSK (Frequency Shift Keying) :</strong></p>
<ul>
<li>Binaire 0 : frequence f1</li>
<li>Binaire 1 : frequence f2</li>
<li>Deviation de frequence : +/-25 kHz</li>
<li>Genere par PWM du MCU ou modulateur dedie (RFM69)</li>
</ul>

<p><strong>ASK (Amplitude Shift Keying) :</strong></p>
<ul>
<li>Binaire 0 : amplitude A0 (faible/eteint)</li>
<li>Binaire 1 : amplitude A1 (elevee)</li>
<li>Implementation plus simple mais plus sensible au bruit</li>
</ul>

<h2>Conception du PCB</h2>
<p>Fabrication de deux PCB separes :</p>

<p><strong>PCB emetteur :</strong></p>
<ul>
<li>Entrees capteurs et circuits de conditionnement</li>
<li>Microcontroleur STM32</li>
<li>Etage de modulation</li>
<li>Amplificateur de puissance RF</li>
<li>Reseau d'adaptation d'antenne</li>
</ul>

<p><strong>PCB recepteur :</strong></p>
<ul>
<li>Entree antenne avec protection</li>
<li>LNA et filtre passe-bande</li>
<li>Circuit demodulateur</li>
<li>Microcontroleur STM32</li>
<li>Interface d'affichage</li>
</ul>
</div>

<div class="lang-en">
<h1>Design and Implementation</h1>

<h2>RF Link Budget</h2>
<p>Calculated using Friis transmission formula:</p>
<ul>
<li>Transmit power: +10 dBm (10 mW)</li>
<li>Frequency: 433 MHz or 868 MHz</li>
<li>Antenna gains: ~2 dBi each</li>
<li>Target range: &gt; 50 m outdoor</li>
<li>Data rate: 1-10 kbps</li>
</ul>

<h2>Modulation Schemes</h2>
<p><strong>FSK (Frequency Shift Keying):</strong></p>
<ul>
<li>Binary 0: frequency f1</li>
<li>Binary 1: frequency f2</li>
<li>Frequency deviation: +/-25 kHz</li>
<li>Generated using MCU PWM or dedicated modulator IC (RFM69)</li>
</ul>

<p><strong>ASK (Amplitude Shift Keying):</strong></p>
<ul>
<li>Binary 0: amplitude A0 (low/off)</li>
<li>Binary 1: amplitude A1 (high)</li>
<li>Simpler implementation but more susceptible to noise</li>
</ul>

<h2>PCB Design</h2>
<p>Fabricated two separate PCBs:</p>

<p><strong>Transmitter PCB:</strong></p>
<ul>
<li>Sensor inputs and conditioning circuits</li>
<li>STM32 microcontroller</li>
<li>Modulator stage</li>
<li>RF power amplifier</li>
<li>Antenna matching network</li>
</ul>

<p><strong>Receiver PCB:</strong></p>
<ul>
<li>Antenna input with protection</li>
<li>LNA and band-pass filter</li>
<li>Demodulator circuit</li>
<li>STM32 microcontroller</li>
<li>Display interface</li>
</ul>
</div>

<div class="lang-fr">
<h1>Tests et validation</h1>

<h2>Tests unitaires</h2>
<ul>
<li>Tensions et ondulations de l'alimentation</li>
<li>Qualite du signal de modulation (oscilloscope)</li>
<li>Puissance et spectre RF en sortie (analyseur de spectre)</li>
<li>Niveaux de seuil du demodulateur</li>
</ul>

<h2>Integration systeme</h2>
<ul>
<li>Tests courte portee (1 m) pour validation initiale</li>
<li>Tests de distance progressifs jusqu'a 100 m</li>
<li>Mesures RSSI (indicateur de puissance du signal recu)</li>
<li>Caracterisation du taux d'erreur binaire (BER)</li>
<li>Performances en environnement bruite</li>
</ul>

<h2>Resultats</h2>
<p>Nous avons atteint avec succes :</p>
<ul>
<li>Communication fiable a plus de 50 metres en exterieur</li>
<li>Debit de 9600 bps</li>
<li>BER &lt; 10^-3 en conditions normales</li>
<li>Consommation optimisee pour fonctionnement sur batterie</li>
</ul>

<h1>Conclusion</h1>
<p>Ce projet a fourni une experience pratique inestimable dans la conception de systemes de communication RF complets. Nous avons integre avec succes plusieurs disciplines d'ingenierie pour creer une liaison sans fil fonctionnelle, demontrant l'importance d'une conception systematique, de tests rigoureux et d'une optimisation iterative dans les systemes electroniques complexes.</p>
</div>

<div class="lang-en">
<h1>Testing and Validation</h1>

<h2>Unit Testing</h2>
<ul>
<li>Power supply voltages and ripple</li>
<li>Modulation signal quality (oscilloscope)</li>
<li>RF output power and spectrum (spectrum analyzer)</li>
<li>Demodulator threshold levels</li>
</ul>

<h2>System Integration</h2>
<ul>
<li>Short-range testing (1 m) for initial validation</li>
<li>Progressive distance testing up to 100 m</li>
<li>RSSI (Received Signal Strength Indicator) measurements</li>
<li>Bit Error Rate (BER) characterization</li>
<li>Performance in noisy environments</li>
</ul>

<h2>Results</h2>
<p>Successfully achieved:</p>
<ul>
<li>Reliable communication at 50+ meters outdoor</li>
<li>Data rate of 9600 bps</li>
<li>BER &lt; 10^-3 under normal conditions</li>
<li>Power consumption optimized for battery operation</li>
</ul>

<h1>Conclusion</h1>
<p>This project provided invaluable hands-on experience in designing complete RF communication systems. We successfully integrated multiple engineering disciplines to create a functional wireless link, demonstrating the importance of systematic design, careful testing, and iterative optimization in complex electronic systems.</p>
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

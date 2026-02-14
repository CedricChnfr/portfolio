---
layout: default
title: "Projet PCB - S6"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
---

<style>
p {
  text-align: justify;
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
</style>

<div class="back-nav">
    <a href="./my-projects.html" data-i18n-html="back-projects">&larr; Retour aux Projets</a>
</div>

<div class="lang-fr">
<h1>Projet PCB - Semestre 6</h1>

<p><strong>Annee Universitaire</strong> : 2022-2023<br/>
<strong>Semestre</strong> : 6<br/>
<strong>Credits</strong> : 2 ECTS<br/>
<strong>Specialite</strong> : Conception Electronique</p>

<h2>Vue d'ensemble</h2>
<p>Ce projet consiste a concevoir une carte electronique complete (PCB) de A a Z avec Altium Designer : schematiques, routage, creation de composants, et generation des fichiers de fabrication. Le projet est un objet connecte avec interface tactile, LED RGB, alimentation autonome sur batterie, et microcontroleur STM32.</p>

<p><strong>Objectifs pedagogiques :</strong></p>
<ul>
<li>Maitriser Altium Designer (logiciel professionnel de conception PCB)</li>
<li>Concevoir des schemas electriques hierarchiques</li>
<li>Creer des bibliotheques de composants (symboles et empreintes)</li>
<li>Router une carte multicouche</li>
<li>Generer les fichiers de fabrication (Gerber, percage, BOM)</li>
<li>Modeliser en 3D et integrer dans un boitier</li>
</ul>

<h2>Description du projet</h2>
<p><strong>Concept :</strong> Carte interactive avec interface tactile et retour visuel LED RGB.</p>
</div>

<div class="lang-en">
<h1>PCB Project - Semester 6</h1>

<p><strong>Academic Year</strong>: 2022-2023<br/>
<strong>Semester</strong>: 6<br/>
<strong>Credits</strong>: 2 ECTS<br/>
<strong>Specialty</strong>: Electronic Design</p>

<h2>Overview</h2>
<p>This project consists of designing a complete electronic board (PCB) from start to finish with Altium Designer: schematics, routing, component creation, and manufacturing file generation. The project is a connected object with touch interface, RGB LEDs, autonomous battery power supply, and STM32 microcontroller.</p>

<p><strong>Learning Objectives:</strong></p>
<ul>
<li>Master Altium Designer (professional PCB design software)</li>
<li>Design hierarchical electrical schematics</li>
<li>Create component libraries (symbols and footprints)</li>
<li>Route a multilayer board</li>
<li>Generate manufacturing files (Gerber, drill, BOM)</li>
<li>3D modeling and enclosure integration</li>
</ul>

<h2>Project Description</h2>
<p><strong>Concept:</strong> Interactive board with touch interface and RGB LED visual feedback.</p>
</div>

<table>
<tr><th>Module</th><th>Composants / Components</th><th>Fonction / Function</th></tr>
<tr><td>Alimentation / Power</td><td>Batterie Li-Ion, regulateur 3.3V</td><td>Autonomie energetique / Energy autonomy</td></tr>
<tr><td>Controle / Control</td><td>STM32F103</td><td>Cerveau du systeme / System brain</td></tr>
<tr><td>Interface utilisateur / User Interface</td><td>Capteurs tactiles capacitifs / Capacitive touch sensors</td><td>Interaction utilisateur / User interaction</td></tr>
<tr><td>Retour visuel / Visual Feedback</td><td>LED RGB WS2812B</td><td>Affichage couleurs / Color display</td></tr>
<tr><td>Communication</td><td>USB Type-C</td><td>Programmation + alimentation / Programming + power</td></tr>
</table>

<div class="lang-fr">
<h2>Modules developpes</h2>

<h3>1. Alimentation (Alimentation_PCB.SchDoc)</h3>
<p>Circuit de gestion d'alimentation avec :</p>
<ul>
<li>Connecteur USB Type-C pour charge et programmation</li>
<li>Regulateur de tension 5V vers 3.3V (pour STM32 et peripheriques)</li>
<li>Protection batterie Li-Ion (charge/decharge)</li>
<li>Condensateurs de decouplage (100 nF, 10 uF)</li>
</ul>

<h3>2. Microcontroleur (MicroControleur.SchDoc)</h3>
<p>Circuit STM32F103 avec :</p>
<ul>
<li>Oscillateur externe 8 MHz (quartz + condensateurs 22 pF)</li>
<li>Condensateurs de decouplage sur chaque alimentation (100 nF)</li>
<li>Connecteur SWD pour programmation/debogage</li>
<li>Bouton reset</li>
<li>LED de statut</li>
</ul>

<h3>3. LED RGB (LED_RGB.SchDoc)</h3>
<p>Chaine de LED adressables WS2812B :</p>
<ul>
<li>8 a 16 LED RGB connectees en serie</li>
<li>Alimentation 5V</li>
<li>Resistance de protection sur data (470 ohms)</li>
<li>Condensateur de decouplage par LED (100 nF)</li>
</ul>

<h3>4. Interface tactile (Touch.SchDoc)</h3>
<p>Capteurs tactiles capacitifs :</p>
<ul>
<li>4 a 8 zones tactiles (pads PCB en cuivre)</li>
<li>Controleur tactile dedie (TTP223 ou equivalent) ou GPIO STM32</li>
<li>Resistances de pull-up/down</li>
<li>Condensateurs de filtrage anti-bruit</li>
</ul>

<h2>Routage du PCB</h2>
<p><strong>Specifications de la carte :</strong></p>
<ul>
<li>Dimensions : environ 80 mm x 60 mm</li>
<li>Couches : 2 couches (Top + Bottom)</li>
<li>Epaisseur cuivre : 35 um (1 oz)</li>
<li>Finition : HASL ou ENIG</li>
<li>Vernis epargne : vert</li>
<li>Serigraphie : blanc</li>
</ul>

<h2>Generation des fichiers de fabrication</h2>
<p><strong>Fichiers Gerber :</strong> Format standard pour fabrication PCB. Un fichier par couche.</p>

<h2>Modelisation 3D et boitier</h2>
<p><strong>Fichiers 3D disponibles :</strong></p>
<ul>
<li>Carte_PCB.step : carte electronique avec composants</li>
<li>Boitier_PCB.step : boitier inferieur</li>
<li>Couvercle_PCB.step : couvercle superieur</li>
<li>Plaque_tactile_PCB.step : interface tactile</li>
<li>Assemblage_plecs_bois.step : assemblage complet</li>
</ul>

<h2>Difficultes rencontrees</h2>
<p><strong>Creation de bibliotheques :</strong> Chronophage et minutieux. Erreur dans empreinte = PCB inutilisable. Importance de verifier dimensions dans datasheet.</p>
<p><strong>Routage contraint :</strong> Espace limite, nombreux composants. Necessite de compromis entre ideal et faisable.</p>
<p><strong>Verifications et erreurs :</strong> DRC/ERC peuvent generer des centaines d'erreurs. Il faut toutes les corriger avant fabrication.</p>

<h2>Conclusion</h2>
<p>Le projet PCB est une experience formatrice essentielle pour tout ingenieur electronique ou systemes embarques. La capacite a concevoir ses propres cartes ouvre de nombreuses possibilites : prototypes, produits, objets connectes. Altium Designer est un outil puissant mais exigeant. La maitrise demande de la pratique, mais les competences acquises sont valorisees en entreprise.</p>
</div>

<div class="lang-en">
<h2>Developed Modules</h2>

<h3>1. Power Supply (Alimentation_PCB.SchDoc)</h3>
<p>Power management circuit with:</p>
<ul>
<li>USB Type-C connector for charging and programming</li>
<li>5V to 3.3V voltage regulator (for STM32 and peripherals)</li>
<li>Li-Ion battery protection (charge/discharge)</li>
<li>Decoupling capacitors (100 nF, 10 uF)</li>
</ul>

<h3>2. Microcontroller (MicroControleur.SchDoc)</h3>
<p>STM32F103 circuit with:</p>
<ul>
<li>External 8 MHz oscillator (crystal + 22 pF capacitors)</li>
<li>Decoupling capacitors on each power pin (100 nF)</li>
<li>SWD connector for programming/debugging</li>
<li>Reset button</li>
<li>Status LED</li>
</ul>

<h3>3. RGB LEDs (LED_RGB.SchDoc)</h3>
<p>WS2812B addressable LED chain:</p>
<ul>
<li>8 to 16 RGB LEDs connected in series</li>
<li>5V power supply</li>
<li>Protection resistor on data line (470 ohms)</li>
<li>Decoupling capacitor per LED (100 nF)</li>
</ul>

<h3>4. Touch Interface (Touch.SchDoc)</h3>
<p>Capacitive touch sensors:</p>
<ul>
<li>4 to 8 touch zones (copper PCB pads)</li>
<li>Dedicated touch controller (TTP223 or equivalent) or STM32 GPIO</li>
<li>Pull-up/down resistors</li>
<li>Noise filtering capacitors</li>
</ul>

<h2>PCB Routing</h2>
<p><strong>Board Specifications:</strong></p>
<ul>
<li>Dimensions: approximately 80 mm x 60 mm</li>
<li>Layers: 2 layers (Top + Bottom)</li>
<li>Copper thickness: 35 um (1 oz)</li>
<li>Finish: HASL or ENIG</li>
<li>Solder mask: green</li>
<li>Silkscreen: white</li>
</ul>

<h2>Manufacturing File Generation</h2>
<p><strong>Gerber Files:</strong> Standard format for PCB manufacturing. One file per layer.</p>

<h2>3D Modeling and Enclosure</h2>
<p><strong>Available 3D Files:</strong></p>
<ul>
<li>Carte_PCB.step: electronic board with components</li>
<li>Boitier_PCB.step: bottom enclosure</li>
<li>Couvercle_PCB.step: top cover</li>
<li>Plaque_tactile_PCB.step: touch interface</li>
<li>Assemblage_plecs_bois.step: complete assembly</li>
</ul>

<h2>Challenges Encountered</h2>
<p><strong>Library Creation:</strong> Time-consuming and meticulous. Footprint errors result in unusable PCBs. Critical to verify dimensions from datasheets.</p>
<p><strong>Constrained Routing:</strong> Limited space, many components. Compromises needed between ideal and feasible solutions.</p>
<p><strong>Verification and Errors:</strong> DRC/ERC can generate hundreds of errors. All must be corrected before manufacturing.</p>

<h2>Conclusion</h2>
<p>The PCB project is an essential formative experience for any electronics or embedded systems engineer. The ability to design custom boards opens many possibilities: prototypes, products, connected objects. Altium Designer is a powerful but demanding tool. Mastery requires practice, but the skills acquired are valued in industry.</p>
</div>

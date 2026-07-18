---
layout: default
title: "Circuits Hyperfréquences - S3"
date:   2024-10-02 10:56:03 +0200
---

<style>
.back-nav { margin-bottom: 20px; }
.back-nav a { text-decoration: none; color: #2a7ae2; font-weight: 600; }
.back-nav a:hover { text-decoration: underline; }
.section-title { color: #2a7ae2; border-bottom: 2px solid #2a7ae2; padding-bottom: 10px; margin-top: 30px; margin-bottom: 20px; }
</style>

<div class="back-nav">
  <a href="./my-courses-2021-2022.html" data-i18n-html="back-courses-2021-2022">&larr; Retour aux Cours 2021-2022</a>
</div>

<div class="lang-fr">

<h1>Circuits Hyperfrequences - Semestre 3</h1>

<p><strong>Annee</strong>: 2021-2022 | <strong>Semestre</strong>: 3 | <strong>Type</strong>: Technique</p>

<hr>

<h2>PART A - Presentation Generale du Cours</h2>

<h3>Contexte et objectifs</h3>

<p>Ce cours de S3 specialisation ENOC introduit la conception de circuits fonctionnant aux frequences RF et micro-ondes (100 MHz - 10+ GHz). Il combine theorie electromagnetique, simulation EM 3D et realisation pratique sur PCB, avec caracterisation par analyseur de reseau vectoriel.</p>

<p><strong>Objectifs principaux :</strong></p>
<ul>
  <li>Maitriser les technologies de circuits RF planaires (microstrip, stripline, CPW)</li>
  <li>Concevoir filtres, adaptations d'impedance, diviseurs de puissance</li>
  <li>Simuler avec outils EM professionnels (ADS Momentum, HFSS, CST)</li>
  <li>Fabriquer sur PCB et mesurer avec VNA</li>
  <li>Comprendre phenomenes HF : effet de peau, pertes dielectriques, couplages</li>
</ul>

<h3>Prerequis</h3>
<ul>
  <li>Propagation et Hyperfrequences S3 (lignes de transmission, Smith chart, parametres S)</li>
  <li>Electronique analogique (composants passifs, filtrage)</li>
  <li>Conception PCB (ER S1-S2)</li>
</ul>

<hr>

<h2>PART B: EXPERIENCE, CONTEXTE ET FONCTION</h2>

<h3>Module 1 : Technologies RF sur PCB</h3>

<p><strong>Substrats RF :</strong></p>
<ul>
  <li>FR-4 : er~4.3-4.7, tan d~0.02, economique, limite &lt;3 GHz</li>
  <li>Rogers RO4003/RO4350 : er stable (3.38/3.48), faibles pertes, 0-10+ GHz</li>
  <li>PTFE/Teflon : er~2.1, tres faibles pertes, difficile a usiner</li>
</ul>

<p><strong>Lignes microstrip :</strong></p>
<ul>
  <li>Calcul largeur pour Z0=50 Ohm : W~3mm (FR-4 1.6mm), er_eff~3.2</li>
  <li>Pertes : conducteur (cuivre) + dielectrique (tan d)</li>
  <li>Applications : alimentations, adaptations</li>
</ul>

<p><strong>Composants passifs RF :</strong></p>
<ul>
  <li>Resistances 50 Ohm (charges, attenuateurs)</li>
  <li>Condensateurs RF CMS (resonance serie SRF critique)</li>
  <li>Inductances (bobines air, CMS, facteur Q)</li>
  <li>Vias de masse (stitching lambda/10)</li>
</ul>

<h3>Module 2 : Circuits d'adaptation et filtres</h3>

<p><strong>Reseaux d'adaptation localises (L, pi, T) :</strong></p>
<ul>
  <li>Transformation impedance avec L/C CMS</li>
  <li>Calcul par Smith chart</li>
  <li>Bande etroite</li>
</ul>

<p><strong>Adaptation distribuee :</strong></p>
<ul>
  <li>Stub simple (serie/parallele) : position et longueur</li>
  <li>Ligne lambda/4 : Z_lambda/4 = sqrt(Z1 * Z2)</li>
  <li>Double stub : positions fixes 3lambda/8</li>
</ul>

<p><strong>Filtres microstrip :</strong></p>
<ul>
  <li>Passe-bas/haut/bande a elements localises</li>
  <li>Filtres a stubs (bande-stop)</li>
  <li>Filtres a lignes couplees (passe-bande)</li>
  <li>Synthese : Butterworth, Chebyshev</li>
</ul>

<p><strong>Coupleurs et diviseurs :</strong></p>
<ul>
  <li>Diviseur Wilkinson : division egale, isolation, resistance 100 Ohm</li>
  <li>Coupleur directionnel : couplage -3/-10/-20 dB</li>
  <li>Rat-race : 180 deg hybrid, 3lambda/2 circonference</li>
</ul>

<h3>Module 3 : Simulation EM</h3>

<p><strong>Logiciels professionnels :</strong></p>
<ul>
  <li>ADS Momentum : 2.5D planar, rapide</li>
  <li>HFSS : 3D FEM, precis</li>
  <li>CST : 3D temps/frequence</li>
  <li>Sonnet : 2.5D, gratuit version limitee</li>
</ul>

<p><strong>Workflow simulation :</strong></p>
<ol>
  <li>Schematique circuit (calcul initial)</li>
  <li>Layout PCB (dessin geometrie)</li>
  <li>Simulation EM 3D (champs, courants)</li>
  <li>Optimisation parametres</li>
  <li>Validation specs (S-parameters)</li>
</ol>

<p><strong>Parametres analyses :</strong></p>
<ul>
  <li>S11 (adaptation), S21 (transmission)</li>
  <li>Champs E et H</li>
  <li>Courants de surface</li>
  <li>Pertes (conducteur, dielectrique, rayonnement)</li>
</ul>

<hr>

<h2>PART C: ASPECTS TECHNIQUES</h2>

<h3>Projets pratiques</h3>

<p><strong>Projet 1 : Filtre passe-bande 2.4 GHz</strong></p>
<ul>
  <li>Specs : f0=2.4 GHz, BW=200 MHz, IL&lt;3 dB</li>
  <li>Topologie : lignes couplees ou stubs</li>
  <li>Simulation ADS &rarr; Layout &rarr; Fabrication PCB &rarr; Mesure VNA</li>
</ul>

<p><strong>Projet 2 : Diviseur Wilkinson</strong></p>
<ul>
  <li>Division 50 Ohm &rarr; 2x50 Ohm</li>
  <li>Lignes lambda/4 a 70.7 Ohm</li>
  <li>Isolation &gt;20 dB</li>
</ul>

<p><strong>Projet 3 : Adaptation stub</strong></p>
<ul>
  <li>Charge complexe ZL &rarr; 50 Ohm</li>
  <li>Calcul Smith chart</li>
  <li>Stub court-circuit ou ouvert</li>
</ul>

<h3>Caracterisation VNA</h3>

<p><strong>Calibration :</strong></p>
<ul>
  <li>SOLT : Short, Open, Load, Thru</li>
  <li>TRL pour substrats specifiques</li>
  <li>Kit de calibration precis</li>
</ul>

<p><strong>Mesures :</strong></p>
<ul>
  <li>Parametres S (magnitude, phase)</li>
  <li>Smith chart impedance</li>
  <li>TDR (Time Domain Reflectometry)</li>
  <li>Comparaison simulation vs mesure</li>
</ul>

<h3>Fabrication PCB RF</h3>

<p><strong>Fichiers Gerber :</strong></p>
<ul>
  <li>Couches cuivre (Top, Bottom)</li>
  <li>Plans de masse continus</li>
  <li>Drill (vias)</li>
  <li>Soldermask, Silkscreen</li>
</ul>

<p><strong>Fabricants :</strong></p>
<ul>
  <li>PCBWay, JLCPCB (economique)</li>
  <li>Eurocircuits (professionnel EU)</li>
  <li>Specifier : substrat, epaisseur, er, finition (ENIG recommande RF)</li>
</ul>

<hr>

<h2>PART D: ANALYSE ET REFLEXION</h2>

<h3>Evaluation</h3>
<ul>
  <li>Projets simulation + realisation (60%)</li>
  <li>Mesures et rapports (25%)</li>
  <li>Examen theorique (15%)</li>
</ul>

<h3>Competences acquises</h3>
<ul>
  <li>Simulation EM 3D professionnelle</li>
  <li>Conception circuits RF planaires</li>
  <li>Utilisation VNA</li>
  <li>Optimisation performances RF</li>
  <li>Design for Manufacturing RF</li>
</ul>

<h3>Applications industrielles</h3>
<ul>
  <li>Telecommunications (WiFi, 4G/5G, satellite)</li>
  <li>IoT (LoRa, Sigfox, Bluetooth)</li>
  <li>Radar automobile</li>
  <li>Instrumentation RF</li>
</ul>

<h3>Technologies de circuits RF</h3>

<h4>Substrats RF</h4>
<p><strong>FR-4 :</strong></p>
<ul>
  <li>er ~ 4.3-4.7 (variable)</li>
  <li>tan d ~ 0.02 (pertes elevees)</li>
  <li>Economique</li>
  <li>Limite a quelques GHz</li>
</ul>

<p><strong>Rogers (RO4003, RO4350) :</strong></p>
<ul>
  <li>er stable (3.38, 3.48)</li>
  <li>tan d faible (0.0027)</li>
  <li>Bon jusqu'a 10+ GHz</li>
  <li>Plus cher</li>
</ul>

<p><strong>PTFE/Teflon :</strong></p>
<ul>
  <li>er ~ 2.1-2.5</li>
  <li>tan d tres faible</li>
  <li>Hautes performances</li>
  <li>Difficile a usiner</li>
</ul>

<h4>Lignes de transmission sur PCB</h4>

<p><strong>Microstrip :</strong></p>
<ul>
  <li>Ligne sur face superieure</li>
  <li>Plan de masse en dessous</li>
  <li>Facile a fabriquer</li>
  <li>Emissions rayonnees</li>
</ul>

<p><strong>Stripline :</strong></p>
<ul>
  <li>Ligne entre deux plans de masse</li>
  <li>Bien blindee</li>
  <li>PCB multicouche requis</li>
</ul>

<p><strong>Coplanar waveguide (CPW) :</strong></p>
<ul>
  <li>Plans de masse sur meme face</li>
  <li>Bon pour composants CMS</li>
  <li>Bonne isolation</li>
</ul>

<h3>Composants passifs RF</h3>

<h4>Resistances</h4>
<ul>
  <li>Charges 50 Ohm</li>
  <li>Attenuateurs</li>
  <li>Terminaisons</li>
  <li>Modeles hautes frequences</li>
</ul>

<h4>Condensateurs</h4>
<ul>
  <li>Capacites de decouplage</li>
  <li>Resonance serie (SRF)</li>
  <li>ESL et ESR</li>
  <li>Condensateurs RF (ATC, AVX)</li>
</ul>

<h4>Inductances</h4>
<ul>
  <li>Bobines air</li>
  <li>Inductances CMS</li>
  <li>Facteur de qualite Q</li>
  <li>Auto-resonance</li>
</ul>

<h4>Vias</h4>
<ul>
  <li>Via de masse (stitching)</li>
  <li>Via thermique</li>
  <li>Inductance parasite</li>
  <li>Espacement recommande</li>
</ul>

<h3>Circuits d'adaptation</h3>

<h4>Reseaux L, pi, T</h4>
<ul>
  <li>Composants localises</li>
  <li>Calcul analytique</li>
  <li>Simulation (Smith chart)</li>
  <li>Realisation CMS</li>
</ul>

<h4>Adaptation distribuee</h4>
<ul>
  <li>Stubs microstrip</li>
  <li>Lignes lambda/4</li>
  <li>Multi-sections</li>
  <li>Large bande</li>
</ul>

<h3>Filtres RF</h3>

<h4>Filtres a elements localises</h4>
<ul>
  <li>Passe-bas, passe-haut, passe-bande</li>
  <li>Butterworth, Chebyshev</li>
  <li>Transformation LC</li>
  <li>Realisation CMS</li>
</ul>

<h4>Filtres distribues</h4>
<ul>
  <li>Filtres a stubs</li>
  <li>Filtres a lignes couplees</li>
  <li>Filtres interdigites</li>
  <li>Resonateurs</li>
</ul>

<h3>Coupleurs et diviseurs</h3>

<h4>Coupleur directionnel</h4>
<ul>
  <li>Couplage -3dB, -10dB, -20dB</li>
  <li>Isolation</li>
  <li>Directivite</li>
  <li>Applications (mesure, feedback)</li>
</ul>

<h4>Diviseur de Wilkinson</h4>
<ul>
  <li>Division de puissance egale</li>
  <li>Isolation entre sorties</li>
  <li>Impedances 50 Ohm</li>
  <li>Resistance d'isolation</li>
</ul>

<h4>Rat-race (anneau hybride)</h4>
<ul>
  <li>Combineur/diviseur 180 deg</li>
  <li>4 ports</li>
  <li>lambda_g x 3/2 circonference</li>
</ul>

<h3>Oscillateurs RF</h3>

<h4>Oscillateurs a quartz</h4>
<ul>
  <li>Frequence fixe precise</li>
  <li>Stabilite</li>
  <li>TCXO, OCXO</li>
</ul>

<h4>VCO (Voltage Controlled Oscillator)</h4>
<ul>
  <li>Frequence variable</li>
  <li>PLL (Phase-Locked Loop)</li>
  <li>Plage d'accord</li>
  <li>Bruit de phase</li>
</ul>

<h3>Amplificateurs RF</h3>

<h4>Classes d'amplification</h4>
<ul>
  <li>Classe A (lineaire)</li>
  <li>Classe B, AB (push-pull)</li>
  <li>Classe C (RF, non lineaire)</li>
  <li>Classe E, F (commutation)</li>
</ul>

<h4>Caracteristiques</h4>
<ul>
  <li>Gain (dB)</li>
  <li>P1dB (point de compression a 1dB)</li>
  <li>IP3 (point d'interception d'ordre 3)</li>
  <li>Facteur de bruit (NF)</li>
  <li>Stabilite (K-factor, mu)</li>
</ul>

<h3>Travaux pratiques</h3>

<h4>Conception de composants RF</h4>

<p><strong>Projet 1 : Filtre passe-bande</strong></p>
<ul>
  <li>Specifications (f0, BW, IL)</li>
  <li>Calcul et simulation</li>
  <li>Layout PCB</li>
  <li>Caracterisation</li>
</ul>

<p><strong>Projet 2 : Diviseur de puissance</strong></p>
<ul>
  <li>Wilkinson 50 Ohm</li>
  <li>Simulation EM</li>
  <li>Fabrication</li>
  <li>Mesure parametres S</li>
</ul>

<p><strong>Projet 3 : Ligne d'adaptation</strong></p>
<ul>
  <li>Stub ou lambda/4</li>
  <li>Dimensionnement</li>
  <li>Optimisation</li>
  <li>Tests sur VNA</li>
</ul>

<h3>Simulation et conception</h3>

<h4>Etapes</h4>
<ol>
  <li><strong>Calcul theorique</strong> : Formules, Smith chart</li>
  <li><strong>Simulation circuit</strong> : Schematique</li>
  <li><strong>Simulation EM</strong> : Layout 3D</li>
  <li><strong>Optimisation</strong> : Tuning parametres</li>
  <li><strong>Generation Gerber</strong> : Fabrication</li>
</ol>

<h3>Fabrication</h3>

<h4>Methodes</h4>
<ul>
  <li><strong>Gravure chimique</strong> : Proto rapide</li>
  <li><strong>Fraiseuse CNC</strong> : Precision</li>
  <li><strong>Fabrication professionnelle</strong> : Production</li>
</ul>

<h4>Fichiers necessaires</h4>
<ul>
  <li>Gerber (couches cuivre)</li>
  <li>Drill (percages)</li>
  <li>Soldermask (vernis)</li>
  <li>Silkscreen (serigraphie)</li>
</ul>

<h3>Caracterisation</h3>

<h4>Mesures avec VNA</h4>
<ul>
  <li>Calibration (SOLT, TRL)</li>
  <li>Parametres S (S11, S21)</li>
  <li>Smith chart</li>
  <li>Comparaison simulation/mesure</li>
</ul>

<h4>Parametres mesures</h4>
<ul>
  <li>Pertes d'insertion (IL)</li>
  <li>Pertes de retour (RL)</li>
  <li>Isolation</li>
  <li>Bande passante</li>
  <li>Impedance</li>
</ul>

<h3>Outils utilises</h3>

<h4>Simulation RF</h4>
<ul>
  <li><strong>ADS (Advanced Design System)</strong> : Keysight</li>
  <li><strong>AWR Microwave Office</strong> : Cadence</li>
  <li><strong>Qucs</strong> : Open source</li>
  <li><strong>LTspice</strong> : Circuits RF</li>
</ul>

<h4>Simulation EM</h4>
<ul>
  <li><strong>Momentum</strong> : Integre ADS (2.5D)</li>
  <li><strong>HFSS</strong> : Ansys (3D)</li>
  <li><strong>CST Microwave Studio</strong> : 3D</li>
  <li><strong>Sonnet</strong> : 2.5D planar</li>
</ul>

<h4>CAO PCB</h4>
<ul>
  <li><strong>Altium Designer</strong></li>
  <li><strong>KiCad</strong> : Open source</li>
  <li><strong>Eagle</strong></li>
  <li><strong>PADS</strong></li>
</ul>

<h4>Mesure</h4>
<ul>
  <li><strong>Analyseur de reseau vectoriel</strong> (VNA)</li>
  <li><strong>Analyseur de spectre</strong></li>
  <li><strong>Generateur RF</strong></li>
  <li><strong>Oscilloscope haute frequence</strong></li>
</ul>

<h3>Exemples de dimensionnement</h3>

<h4>Ligne microstrip 50 Ohm (FR-4, h=1.6mm)</h4>
<ul>
  <li>Largeur W ~ 3 mm</li>
  <li>er = 4.3</li>
  <li>er_eff ~ 3.2</li>
  <li>Z0 = 50 Ohm</li>
</ul>

<h4>Stub lambda/4 a 2.4 GHz</h4>
<ul>
  <li>lambda_0 = 125 mm</li>
  <li>lambda_g = lambda_0/sqrt(er_eff) ~ 70 mm</li>
  <li>Longueur stub ~ 17.5 mm</li>
</ul>

<h4>Diviseur Wilkinson 2.4 GHz</h4>
<ul>
  <li>Lignes lambda/4 a 70.7 Ohm</li>
  <li>Resistance isolation 100 Ohm</li>
  <li>Impedance entree/sorties 50 Ohm</li>
</ul>

<h3>Regles de conception RF</h3>

<h4>Layout PCB</h4>
<ul>
  <li><strong>Plans de masse</strong> : Continus, via stitching</li>
  <li><strong>Largeur de piste</strong> : Controlee (50 Ohm)</li>
  <li><strong>Courbures</strong> : Rayon &gt; 3x largeur</li>
  <li><strong>Espacement</strong> : Eviter couplages parasites</li>
  <li><strong>Vias</strong> : Minimiser sur lignes RF</li>
</ul>

<h4>Decouplage</h4>
<ul>
  <li>Condensateurs proches des composants</li>
  <li>Multiple valeurs (nF, uF)</li>
  <li>Via court vers masse</li>
  <li>Plans de masse separes (analogique/numerique)</li>
</ul>

<h4>Blindage</h4>
<ul>
  <li>Boitier metallique si necessaire</li>
  <li>Cloisons entre sections</li>
  <li>Absorption RF (ferrites, mousses)</li>
</ul>

<h3>Competences developpees</h3>
<ul>
  <li>Simulation EM 3D</li>
  <li>Conception de circuits RF sur PCB</li>
  <li>Utilisation d'analyseur de reseau</li>
  <li>Optimisation de performances RF</li>
  <li>Fabrication de circuits micro-ondes</li>
  <li>Analyse de resultats de mesure</li>
</ul>

<h3>Phenomenes hautes frequences</h3>

<h4>Effet de peau</h4>
<ul>
  <li>Profondeur de penetration delta</li>
  <li>Resistance AC &gt; DC</li>
  <li>Depend de la frequence</li>
  <li>Cuivre argente pour ameliorer</li>
</ul>

<h4>Pertes dielectriques</h4>
<ul>
  <li>tan d du substrat</li>
  <li>Augmentent avec frequence</li>
  <li>Chauffage du PCB</li>
  <li>Choix substrat crucial</li>
</ul>

<h4>Couplages</h4>
<ul>
  <li>Couplage capacitif (E-field)</li>
  <li>Couplage inductif (H-field)</li>
  <li>Couplage par substrat</li>
  <li>Espacement et blindage</li>
</ul>

<h4>Modes parasites</h4>
<ul>
  <li>Modes de cavite</li>
  <li>Resonances indesirables</li>
  <li>Rayonnement</li>
  <li>Via fencing pour mitiger</li>
</ul>

<h3>Erreurs a eviter</h3>

<h4>Conception</h4>
<ul>
  <li>Plans de masse discontinus</li>
  <li>Lignes d'impedance non controlee</li>
  <li>Transitions brusques (stubs, angles droits)</li>
  <li>Sous-estimation des pertes</li>
</ul>

<h4>Fabrication</h4>
<ul>
  <li>Epaisseur cuivre non uniforme</li>
  <li>Gravure excessive ou insuffisante</li>
  <li>Desalignement des couches</li>
  <li>Qualite soudures CMS RF</li>
</ul>

<h4>Mesure</h4>
<ul>
  <li>Calibration inadequate</li>
  <li>Connecteurs mal serres</li>
  <li>Cables endommages</li>
  <li>Gamme de frequence incorrecte</li>
</ul>

<h3>Processus de conception typique</h3>

<h4>Phase 1 : Specifications</h4>
<ul>
  <li>Frequence de travail</li>
  <li>Impedance (50 Ohm typique)</li>
  <li>Performances requises</li>
  <li>Contraintes (taille, cout)</li>
</ul>

<h4>Phase 2 : Conception theorique</h4>
<ul>
  <li>Calculs analytiques</li>
  <li>Choix de topologie</li>
  <li>Simulation schematique</li>
  <li>Validation concept</li>
</ul>

<h4>Phase 3 : Layout et EM</h4>
<ul>
  <li>Dessin PCB</li>
  <li>Simulation EM 3D</li>
  <li>Optimisation dimensions</li>
  <li>Verification DRC</li>
</ul>

<h4>Phase 4 : Fabrication</h4>
<ul>
  <li>Generation fichiers Gerber</li>
  <li>Choix fabricant</li>
  <li>Reception et inspection</li>
  <li>Assemblage CMS</li>
</ul>

<h4>Phase 5 : Test</h4>
<ul>
  <li>Calibration VNA</li>
  <li>Mesures parametres S</li>
  <li>Comparaison avec simulation</li>
  <li>Ajustements (tuning)</li>
</ul>

<h3>Ressources</h3>
<ul>
  <li>Application notes fabricants (Mini-Circuits, Analog Devices)</li>
  <li>"Microwave Engineering" - Pozar</li>
  <li>"RF Circuit Design" - Bowick</li>
  <li>Tutoriels ADS/AWR</li>
  <li>Calculateurs en ligne (impedance, attenuation)</li>
</ul>

</div>

<div class="lang-en">

<h1>Microwave Circuits - Semester 3</h1>

<p><strong>Year</strong>: 2021-2022 | <strong>Semester</strong>: 3 | <strong>Type</strong>: Technical</p>

<hr>

<h2>PART A - General Course Overview</h2>

<h3>Context and objectives</h3>

<p>This S3 ENOC specialization course introduces the design of circuits operating at RF and microwave frequencies (100 MHz - 10+ GHz). It combines electromagnetic theory, 3D EM simulation and practical PCB fabrication, with characterization using a vector network analyzer.</p>

<p><strong>Main objectives:</strong></p>
<ul>
  <li>Master planar RF circuit technologies (microstrip, stripline, CPW)</li>
  <li>Design filters, impedance matching networks, power dividers</li>
  <li>Simulate with professional EM tools (ADS Momentum, HFSS, CST)</li>
  <li>Fabricate on PCB and measure with VNA</li>
  <li>Understand HF phenomena: skin effect, dielectric losses, coupling</li>
</ul>

<h3>Prerequisites</h3>
<ul>
  <li>Propagation and Microwaves S3 (transmission lines, Smith chart, S-parameters)</li>
  <li>Analog electronics (passive components, filtering)</li>
  <li>PCB design (ER S1-S2)</li>
</ul>

<hr>

<h2>PART B: EXPERIENCE, CONTEXT AND FUNCTION</h2>

<h3>Module 1: RF technologies on PCB</h3>

<p><strong>RF substrates:</strong></p>
<ul>
  <li>FR-4: er~4.3-4.7, tan d~0.02, economical, limited &lt;3 GHz</li>
  <li>Rogers RO4003/RO4350: stable er (3.38/3.48), low losses, 0-10+ GHz</li>
  <li>PTFE/Teflon: er~2.1, very low losses, difficult to machine</li>
</ul>

<p><strong>Microstrip lines:</strong></p>
<ul>
  <li>Width calculation for Z0=50 Ohm: W~3mm (FR-4 1.6mm), er_eff~3.2</li>
  <li>Losses: conductor (copper) + dielectric (tan d)</li>
  <li>Applications: feeds, matching</li>
</ul>

<p><strong>RF passive components:</strong></p>
<ul>
  <li>50 Ohm resistors (loads, attenuators)</li>
  <li>RF SMD capacitors (series resonance SRF critical)</li>
  <li>Inductors (air coils, SMD, Q factor)</li>
  <li>Ground vias (stitching lambda/10)</li>
</ul>

<h3>Module 2: Matching circuits and filters</h3>

<p><strong>Lumped matching networks (L, pi, T):</strong></p>
<ul>
  <li>Impedance transformation with SMD L/C</li>
  <li>Smith chart calculation</li>
  <li>Narrowband</li>
</ul>

<p><strong>Distributed matching:</strong></p>
<ul>
  <li>Single stub (series/parallel): position and length</li>
  <li>Lambda/4 line: Z_lambda/4 = sqrt(Z1 * Z2)</li>
  <li>Double stub: fixed positions 3lambda/8</li>
</ul>

<p><strong>Microstrip filters:</strong></p>
<ul>
  <li>Low-pass/high-pass/bandpass with lumped elements</li>
  <li>Stub filters (band-stop)</li>
  <li>Coupled-line filters (bandpass)</li>
  <li>Synthesis: Butterworth, Chebyshev</li>
</ul>

<p><strong>Couplers and dividers:</strong></p>
<ul>
  <li>Wilkinson divider: equal division, isolation, 100 Ohm resistor</li>
  <li>Directional coupler: -3/-10/-20 dB coupling</li>
  <li>Rat-race: 180 deg hybrid, 3lambda/2 circumference</li>
</ul>

<h3>Module 3: EM simulation</h3>

<p><strong>Professional software:</strong></p>
<ul>
  <li>ADS Momentum: 2.5D planar, fast</li>
  <li>HFSS: 3D FEM, accurate</li>
  <li>CST: 3D time/frequency</li>
  <li>Sonnet: 2.5D, free limited version</li>
</ul>

<p><strong>Simulation workflow:</strong></p>
<ol>
  <li>Circuit schematic (initial calculation)</li>
  <li>PCB layout (geometry drawing)</li>
  <li>3D EM simulation (fields, currents)</li>
  <li>Parameter optimization</li>
  <li>Spec validation (S-parameters)</li>
</ol>

<p><strong>Analyzed parameters:</strong></p>
<ul>
  <li>S11 (matching), S21 (transmission)</li>
  <li>E and H fields</li>
  <li>Surface currents</li>
  <li>Losses (conductor, dielectric, radiation)</li>
</ul>

<hr>

<h2>PART C: TECHNICAL ASPECTS</h2>

<h3>Practical projects</h3>

<p><strong>Project 1: 2.4 GHz bandpass filter</strong></p>
<ul>
  <li>Specs: f0=2.4 GHz, BW=200 MHz, IL&lt;3 dB</li>
  <li>Topology: coupled lines or stubs</li>
  <li>ADS simulation &rarr; Layout &rarr; PCB fabrication &rarr; VNA measurement</li>
</ul>

<p><strong>Project 2: Wilkinson divider</strong></p>
<ul>
  <li>50 Ohm division &rarr; 2x50 Ohm</li>
  <li>Lambda/4 lines at 70.7 Ohm</li>
  <li>Isolation &gt;20 dB</li>
</ul>

<p><strong>Project 3: Stub matching</strong></p>
<ul>
  <li>Complex load ZL &rarr; 50 Ohm</li>
  <li>Smith chart calculation</li>
  <li>Short-circuit or open stub</li>
</ul>

<h3>VNA characterization</h3>

<p><strong>Calibration:</strong></p>
<ul>
  <li>SOLT: Short, Open, Load, Thru</li>
  <li>TRL for specific substrates</li>
  <li>Precision calibration kit</li>
</ul>

<p><strong>Measurements:</strong></p>
<ul>
  <li>S-parameters (magnitude, phase)</li>
  <li>Smith chart impedance</li>
  <li>TDR (Time Domain Reflectometry)</li>
  <li>Simulation vs measurement comparison</li>
</ul>

<h3>RF PCB fabrication</h3>

<p><strong>Gerber files:</strong></p>
<ul>
  <li>Copper layers (Top, Bottom)</li>
  <li>Continuous ground planes</li>
  <li>Drill (vias)</li>
  <li>Soldermask, Silkscreen</li>
</ul>

<p><strong>Manufacturers:</strong></p>
<ul>
  <li>PCBWay, JLCPCB (economical)</li>
  <li>Eurocircuits (professional EU)</li>
  <li>Specify: substrate, thickness, er, finish (ENIG recommended for RF)</li>
</ul>

<hr>

<h2>PART D: ANALYSIS AND REFLECTION</h2>

<h3>Assessment</h3>
<ul>
  <li>Simulation + fabrication projects (60%)</li>
  <li>Measurements and reports (25%)</li>
  <li>Theoretical exam (15%)</li>
</ul>

<h3>Skills acquired</h3>
<ul>
  <li>Professional 3D EM simulation</li>
  <li>Planar RF circuit design</li>
  <li>VNA usage</li>
  <li>RF performance optimization</li>
  <li>RF Design for Manufacturing</li>
</ul>

<h3>Industrial applications</h3>
<ul>
  <li>Telecommunications (WiFi, 4G/5G, satellite)</li>
  <li>IoT (LoRa, Sigfox, Bluetooth)</li>
  <li>Automotive radar</li>
  <li>RF instrumentation</li>
</ul>

<h3>RF circuit technologies</h3>

<h4>RF substrates</h4>
<p><strong>FR-4:</strong></p>
<ul>
  <li>er ~ 4.3-4.7 (variable)</li>
  <li>tan d ~ 0.02 (high losses)</li>
  <li>Economical</li>
  <li>Limited to a few GHz</li>
</ul>

<p><strong>Rogers (RO4003, RO4350):</strong></p>
<ul>
  <li>Stable er (3.38, 3.48)</li>
  <li>Low tan d (0.0027)</li>
  <li>Good up to 10+ GHz</li>
  <li>More expensive</li>
</ul>

<p><strong>PTFE/Teflon:</strong></p>
<ul>
  <li>er ~ 2.1-2.5</li>
  <li>Very low tan d</li>
  <li>High performance</li>
  <li>Difficult to machine</li>
</ul>

<h4>Transmission lines on PCB</h4>

<p><strong>Microstrip:</strong></p>
<ul>
  <li>Line on top face</li>
  <li>Ground plane below</li>
  <li>Easy to fabricate</li>
  <li>Radiated emissions</li>
</ul>

<p><strong>Stripline:</strong></p>
<ul>
  <li>Line between two ground planes</li>
  <li>Well shielded</li>
  <li>Multilayer PCB required</li>
</ul>

<p><strong>Coplanar waveguide (CPW):</strong></p>
<ul>
  <li>Ground planes on same face</li>
  <li>Good for SMD components</li>
  <li>Good isolation</li>
</ul>

<h3>RF passive components</h3>

<h4>Resistors</h4>
<ul>
  <li>50 Ohm loads</li>
  <li>Attenuators</li>
  <li>Terminations</li>
  <li>High frequency models</li>
</ul>

<h4>Capacitors</h4>
<ul>
  <li>Decoupling capacitors</li>
  <li>Series resonance (SRF)</li>
  <li>ESL and ESR</li>
  <li>RF capacitors (ATC, AVX)</li>
</ul>

<h4>Inductors</h4>
<ul>
  <li>Air coils</li>
  <li>SMD inductors</li>
  <li>Quality factor Q</li>
  <li>Self-resonance</li>
</ul>

<h4>Vias</h4>
<ul>
  <li>Ground via (stitching)</li>
  <li>Thermal via</li>
  <li>Parasitic inductance</li>
  <li>Recommended spacing</li>
</ul>

<h3>Matching circuits</h3>

<h4>L, pi, T networks</h4>
<ul>
  <li>Lumped components</li>
  <li>Analytical calculation</li>
  <li>Simulation (Smith chart)</li>
  <li>SMD implementation</li>
</ul>

<h4>Distributed matching</h4>
<ul>
  <li>Microstrip stubs</li>
  <li>Lambda/4 lines</li>
  <li>Multi-section</li>
  <li>Wideband</li>
</ul>

<h3>RF filters</h3>

<h4>Lumped element filters</h4>
<ul>
  <li>Low-pass, high-pass, bandpass</li>
  <li>Butterworth, Chebyshev</li>
  <li>LC transformation</li>
  <li>SMD implementation</li>
</ul>

<h4>Distributed filters</h4>
<ul>
  <li>Stub filters</li>
  <li>Coupled-line filters</li>
  <li>Interdigital filters</li>
  <li>Resonators</li>
</ul>

<h3>Couplers and dividers</h3>

<h4>Directional coupler</h4>
<ul>
  <li>Coupling -3dB, -10dB, -20dB</li>
  <li>Isolation</li>
  <li>Directivity</li>
  <li>Applications (measurement, feedback)</li>
</ul>

<h4>Wilkinson divider</h4>
<ul>
  <li>Equal power division</li>
  <li>Output isolation</li>
  <li>50 Ohm impedances</li>
  <li>Isolation resistor</li>
</ul>

<h4>Rat-race (hybrid ring)</h4>
<ul>
  <li>180 deg combiner/divider</li>
  <li>4 ports</li>
  <li>lambda_g x 3/2 circumference</li>
</ul>

<h3>RF oscillators</h3>

<h4>Crystal oscillators</h4>
<ul>
  <li>Precise fixed frequency</li>
  <li>Stability</li>
  <li>TCXO, OCXO</li>
</ul>

<h4>VCO (Voltage Controlled Oscillator)</h4>
<ul>
  <li>Variable frequency</li>
  <li>PLL (Phase-Locked Loop)</li>
  <li>Tuning range</li>
  <li>Phase noise</li>
</ul>

<h3>RF amplifiers</h3>

<h4>Amplification classes</h4>
<ul>
  <li>Class A (linear)</li>
  <li>Class B, AB (push-pull)</li>
  <li>Class C (RF, nonlinear)</li>
  <li>Class E, F (switching)</li>
</ul>

<h4>Characteristics</h4>
<ul>
  <li>Gain (dB)</li>
  <li>P1dB (1dB compression point)</li>
  <li>IP3 (third-order intercept point)</li>
  <li>Noise figure (NF)</li>
  <li>Stability (K-factor, mu)</li>
</ul>

<h3>Practical work</h3>

<h4>RF component design</h4>

<p><strong>Project 1: Bandpass filter</strong></p>
<ul>
  <li>Specifications (f0, BW, IL)</li>
  <li>Calculation and simulation</li>
  <li>PCB layout</li>
  <li>Characterization</li>
</ul>

<p><strong>Project 2: Power divider</strong></p>
<ul>
  <li>50 Ohm Wilkinson</li>
  <li>EM simulation</li>
  <li>Fabrication</li>
  <li>S-parameter measurement</li>
</ul>

<p><strong>Project 3: Matching line</strong></p>
<ul>
  <li>Stub or lambda/4</li>
  <li>Sizing</li>
  <li>Optimization</li>
  <li>VNA testing</li>
</ul>

<h3>Simulation and design</h3>

<h4>Steps</h4>
<ol>
  <li><strong>Theoretical calculation</strong>: Formulas, Smith chart</li>
  <li><strong>Circuit simulation</strong>: Schematic</li>
  <li><strong>EM simulation</strong>: 3D layout</li>
  <li><strong>Optimization</strong>: Parameter tuning</li>
  <li><strong>Gerber generation</strong>: Fabrication</li>
</ol>

<h3>Fabrication</h3>

<h4>Methods</h4>
<ul>
  <li><strong>Chemical etching</strong>: Rapid prototyping</li>
  <li><strong>CNC milling</strong>: Precision</li>
  <li><strong>Professional fabrication</strong>: Production</li>
</ul>

<h4>Required files</h4>
<ul>
  <li>Gerber (copper layers)</li>
  <li>Drill (drilling)</li>
  <li>Soldermask (varnish)</li>
  <li>Silkscreen (marking)</li>
</ul>

<h3>Characterization</h3>

<h4>VNA measurements</h4>
<ul>
  <li>Calibration (SOLT, TRL)</li>
  <li>S-parameters (S11, S21)</li>
  <li>Smith chart</li>
  <li>Simulation/measurement comparison</li>
</ul>

<h4>Measured parameters</h4>
<ul>
  <li>Insertion loss (IL)</li>
  <li>Return loss (RL)</li>
  <li>Isolation</li>
  <li>Bandwidth</li>
  <li>Impedance</li>
</ul>

<h3>Tools used</h3>

<h4>RF simulation</h4>
<ul>
  <li><strong>ADS (Advanced Design System)</strong>: Keysight</li>
  <li><strong>AWR Microwave Office</strong>: Cadence</li>
  <li><strong>Qucs</strong>: Open source</li>
  <li><strong>LTspice</strong>: RF circuits</li>
</ul>

<h4>EM simulation</h4>
<ul>
  <li><strong>Momentum</strong>: Integrated in ADS (2.5D)</li>
  <li><strong>HFSS</strong>: Ansys (3D)</li>
  <li><strong>CST Microwave Studio</strong>: 3D</li>
  <li><strong>Sonnet</strong>: 2.5D planar</li>
</ul>

<h4>PCB CAD</h4>
<ul>
  <li><strong>Altium Designer</strong></li>
  <li><strong>KiCad</strong>: Open source</li>
  <li><strong>Eagle</strong></li>
  <li><strong>PADS</strong></li>
</ul>

<h4>Measurement</h4>
<ul>
  <li><strong>Vector Network Analyzer</strong> (VNA)</li>
  <li><strong>Spectrum analyzer</strong></li>
  <li><strong>RF generator</strong></li>
  <li><strong>High frequency oscilloscope</strong></li>
</ul>

<h3>Sizing examples</h3>

<h4>50 Ohm microstrip line (FR-4, h=1.6mm)</h4>
<ul>
  <li>Width W ~ 3 mm</li>
  <li>er = 4.3</li>
  <li>er_eff ~ 3.2</li>
  <li>Z0 = 50 Ohm</li>
</ul>

<h4>Lambda/4 stub at 2.4 GHz</h4>
<ul>
  <li>lambda_0 = 125 mm</li>
  <li>lambda_g = lambda_0/sqrt(er_eff) ~ 70 mm</li>
  <li>Stub length ~ 17.5 mm</li>
</ul>

<h4>Wilkinson divider 2.4 GHz</h4>
<ul>
  <li>Lambda/4 lines at 70.7 Ohm</li>
  <li>100 Ohm isolation resistor</li>
  <li>50 Ohm input/output impedance</li>
</ul>

<h3>RF design rules</h3>

<h4>PCB layout</h4>
<ul>
  <li><strong>Ground planes</strong>: Continuous, via stitching</li>
  <li><strong>Track width</strong>: Controlled (50 Ohm)</li>
  <li><strong>Bends</strong>: Radius &gt; 3x width</li>
  <li><strong>Spacing</strong>: Avoid parasitic coupling</li>
  <li><strong>Vias</strong>: Minimize on RF lines</li>
</ul>

<h4>Decoupling</h4>
<ul>
  <li>Capacitors close to components</li>
  <li>Multiple values (nF, uF)</li>
  <li>Short via to ground</li>
  <li>Separate ground planes (analog/digital)</li>
</ul>

<h4>Shielding</h4>
<ul>
  <li>Metal enclosure if necessary</li>
  <li>Partitions between sections</li>
  <li>RF absorption (ferrites, foams)</li>
</ul>

<h3>Skills developed</h3>
<ul>
  <li>3D EM simulation</li>
  <li>RF circuit design on PCB</li>
  <li>Network analyzer usage</li>
  <li>RF performance optimization</li>
  <li>Microwave circuit fabrication</li>
  <li>Measurement result analysis</li>
</ul>

<h3>High frequency phenomena</h3>

<h4>Skin effect</h4>
<ul>
  <li>Penetration depth delta</li>
  <li>AC resistance &gt; DC</li>
  <li>Frequency dependent</li>
  <li>Silver-plated copper for improvement</li>
</ul>

<h4>Dielectric losses</h4>
<ul>
  <li>Substrate tan d</li>
  <li>Increase with frequency</li>
  <li>PCB heating</li>
  <li>Substrate choice crucial</li>
</ul>

<h4>Coupling</h4>
<ul>
  <li>Capacitive coupling (E-field)</li>
  <li>Inductive coupling (H-field)</li>
  <li>Substrate coupling</li>
  <li>Spacing and shielding</li>
</ul>

<h4>Parasitic modes</h4>
<ul>
  <li>Cavity modes</li>
  <li>Unwanted resonances</li>
  <li>Radiation</li>
  <li>Via fencing to mitigate</li>
</ul>

<h3>Mistakes to avoid</h3>

<h4>Design</h4>
<ul>
  <li>Discontinuous ground planes</li>
  <li>Uncontrolled impedance lines</li>
  <li>Abrupt transitions (stubs, right angles)</li>
  <li>Underestimating losses</li>
</ul>

<h4>Fabrication</h4>
<ul>
  <li>Non-uniform copper thickness</li>
  <li>Excessive or insufficient etching</li>
  <li>Layer misalignment</li>
  <li>RF SMD solder quality</li>
</ul>

<h4>Measurement</h4>
<ul>
  <li>Inadequate calibration</li>
  <li>Loose connectors</li>
  <li>Damaged cables</li>
  <li>Incorrect frequency range</li>
</ul>

<h3>Typical design process</h3>

<h4>Phase 1: Specifications</h4>
<ul>
  <li>Operating frequency</li>
  <li>Impedance (50 Ohm typical)</li>
  <li>Required performance</li>
  <li>Constraints (size, cost)</li>
</ul>

<h4>Phase 2: Theoretical design</h4>
<ul>
  <li>Analytical calculations</li>
  <li>Topology choice</li>
  <li>Schematic simulation</li>
  <li>Concept validation</li>
</ul>

<h4>Phase 3: Layout and EM</h4>
<ul>
  <li>PCB drawing</li>
  <li>3D EM simulation</li>
  <li>Dimension optimization</li>
  <li>DRC verification</li>
</ul>

<h4>Phase 4: Fabrication</h4>
<ul>
  <li>Gerber file generation</li>
  <li>Manufacturer selection</li>
  <li>Reception and inspection</li>
  <li>SMD assembly</li>
</ul>

<h4>Phase 5: Test</h4>
<ul>
  <li>VNA calibration</li>
  <li>S-parameter measurements</li>
  <li>Comparison with simulation</li>
  <li>Adjustments (tuning)</li>
</ul>

<h3>Resources</h3>
<ul>
  <li>Manufacturer application notes (Mini-Circuits, Analog Devices)</li>
  <li>"Microwave Engineering" - Pozar</li>
  <li>"RF Circuit Design" - Bowick</li>
  <li>ADS/AWR tutorials</li>
  <li>Online calculators (impedance, attenuation)</li>
</ul>

</div>

<div class="pdf-container">
  <div class="pdf-viewer">

    <div class="pdf-item">
      <h4 class="lang-fr">Circuits et Fonctions Hyperfrequences</h4>
      <h4 class="lang-en">Microwave Circuits and Functions</h4>
      <p class="lang-fr">Support de cours complet sur les circuits hyperfrequences : lignes de transmission, adaptation d'impedance, filtres HF et composants passifs distribues.</p>
      <p class="lang-en">Complete course material on microwave circuits: transmission lines, impedance matching, HF filters and distributed passive components.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S3/Circuits-HF/Circuits_et_Fonction_HF_2021.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S3/Circuits-HF/Circuits_et_Fonction_HF_2021.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;" class="lang-fr">Telecharger le PDF</a>
        <a href="/cours-pdf/S3/Circuits-HF/Circuits_et_Fonction_HF_2021.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;" class="lang-en">Download PDF</a>
      </p>
    </div>

  </div>
</div>

<style>body{font-family:Arial,sans-serif;background-color:#f4f4f9;color:#333;line-height:1.6}h2,h3,h4,h5{color:#2a7ae2}p{text-align:justify}code{background-color:#f5f5f5;padding:2px 6px;border-radius:3px;font-family:'Courier New',monospace}pre{background-color:#f5f5f5;padding:15px;border-radius:5px;overflow-x:auto}</style>

<div class="back-nav">
  <a href="./my-courses-2021-2022.html" data-i18n-html="back-courses-2021-2022">&larr; Retour aux Cours 2021-2022</a>
</div>

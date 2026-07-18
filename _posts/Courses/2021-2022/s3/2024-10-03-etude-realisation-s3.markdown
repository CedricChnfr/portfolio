---
layout: default
title: "Étude et Réalisation (ER) - S3"
date:   2024-10-02 10:56:03 +0200
---

<style>
.back-nav { margin-bottom: 20px; }
.back-nav a { text-decoration: none; color: #2a7ae2; font-weight: 600; }
.back-nav a:hover { text-decoration: underline; }
.section-title { color: #2a7ae2; border-bottom: 2px solid #2a7ae2; padding-bottom: 10px; margin-top: 30px; margin-bottom: 20px; }
</style>

<div class="back-nav">
  <a href="./my-courses-2021-2022.html" data-i18n-html="back-courses-2021-2022">&larr; Retour a Mes Cours 2021-2022</a>
</div>

<div class="lang-fr">

<h1>Étude et Réalisation (ER) - Semestre 3</h1>

<p><strong>Annee</strong>: 2021-2022 | <strong>Semestre</strong>: 3 | <strong>Type</strong>: Technique</p>

<hr>

<h2>PART A - Présentation Générale du Cours</h2>

<h3>Contexte et objectifs</h3>

<p>Projet majeur S3 : conception et réalisation d'un <strong>télémètre ultrasonique</strong> intégrant électronique analogique (amplification, filtrage), numérique (VHDL/FPGA) et traitement du signal. Projet pluridisciplinaire mobilisant toutes les compétences GEII.</p>

<p><strong>Objectifs :</strong></p>
<ul>
<li>Concevoir système complet (specs → réalisation)</li>
<li>Intégrer analogique + numérique + FPGA</li>
<li>PCB multicouche professionnel</li>
<li>Validation par tests et mesures</li>
<li>Documentation technique complète</li>
</ul>

<h3>Prérequis</h3>
<ul>
<li>Électronique analogique (amplis, filtres)</li>
<li>VHDL (FSM, compteurs)</li>
<li>Conception PCB</li>
<li>Traitement du signal</li>
</ul>

<hr>

<h2>PART B: EXPÉRIENCE, CONTEXTE ET FONCTION</h2>

<h3>Système Télémètre Ultrasonique</h3>

<p><strong>Principe :</strong><br>
Mesure de distance par temps de vol d'ondes ultrasoniques (40 kHz typique).<br>
Distance = (c × Δt) / 2, où c ≈ 340 m/s</p>

<p><strong>Architecture :</strong></p>
<pre><code>[FPGA/CPLD] → [Driver] → [Transducteur TX]
                             ↓ ondes US
                          [Cible]
                             ↓ écho
[FPGA] ← [Comparateur] ← [Filtrage] ← [Ampli] ← [Transducteur RX]
   ↓
[Affichage LCD / UART]</code></pre>

<h3>Module 1 : Chaîne d'émission</h3>

<p><strong>Génération burst 40 kHz :</strong></p>
<ul>
<li>FPGA : compteur + diviseur de fréquence</li>
<li>Burst : 8-10 cycles (200-250 µs)</li>
<li>Driver push-pull (transistors ou pont H)</li>
<li>Transducteur piézo 40 kHz (impédance ≈ 2kΩ)</li>
</ul>

<p><strong>Électronique :</strong></p>
<ul>
<li>Ampli classe B ou D pour efficacité</li>
<li>Protection (clamping diodes)</li>
<li>Adaptation impédance</li>
</ul>

<h3>Module 2 : Chaîne de réception</h3>

<p><strong>Transducteur RX :</strong></p>
<ul>
<li>Même fréquence que TX (40 kHz)</li>
<li>Signal faible (quelques mV)</li>
</ul>

<p><strong>Préamplification :</strong></p>
<ul>
<li>Ampli instrumentation ou AOP faible bruit</li>
<li>Gain : 40-60 dB</li>
<li>Filtrage passe-bande 38-42 kHz (Sallen-Key ordre 2)</li>
</ul>

<p><strong>Détection d'enveloppe :</strong></p>
<ul>
<li>Redresseur + filtrage RC</li>
<li>Ou détecteur de crête (diode + hold capacitor)</li>
</ul>

<p><strong>Comparateur à seuil :</strong></p>
<ul>
<li>Seuil réglable (potentiomètre ou DAC)</li>
<li>Sortie TTL/CMOS → FPGA</li>
<li>Hystérésis (Schmitt trigger) pour stabilité</li>
</ul>

<h3>Module 3 : Traitement numérique VHDL</h3>

<p><strong>FSM de contrôle :</strong></p>
<ol>
<li>IDLE : attente commande</li>
<li>EMIT : génération burst TX</li>
<li>WAIT_ECHO : comptage temps (counter++)</li>
<li>ECHO_DETECTED : calcul distance</li>
<li>DISPLAY : mise à jour affichage</li>
</ol>

<p><strong>Compteur temps de vol :</strong></p>
<ul>
<li>Horloge 1 MHz → résolution 1 µs</li>
<li>Comptage entre fin burst et front montant écho</li>
<li>Timeout si pas d'écho (3-5 m max)</li>
</ul>

<p><strong>Calcul distance :</strong></p>
<ul>
<li>Distance (cm) = (Compteur × 340 m/s) / (2 × 10^4)</li>
<li>Implémentation : division ou multiplication par constante</li>
</ul>

<p><strong>Interface :</strong></p>
<ul>
<li>LCD 16×2 (affichage distance)</li>
<li>UART (transmission PC)</li>
<li>LEDs status</li>
</ul>

<h3>Module 4 : Intégration PCB</h3>

<p><strong>PCB 4 couches :</strong></p>
<ul>
<li>L1 : Analogique (amplis, filtres)</li>
<li>L2 : GND plane</li>
<li>L3 : Power planes (±12V, 5V, 3.3V)</li>
<li>L4 : Numérique (FPGA, affichage)</li>
</ul>

<p><strong>Règles de conception :</strong></p>
<ul>
<li>Séparation analog/digital (GND unique pont à 1 point)</li>
<li>Découplage intensif</li>
<li>Blindage zone RF si nécessaire</li>
<li>Via stitching GND</li>
</ul>

<p><strong>Alimentation :</strong></p>
<ul>
<li>Entrée 12V ou USB 5V</li>
<li>Régulateurs linéaires (7805, 7812, 7912) ou à découpage</li>
<li>Rail dual ±12V pour amplis</li>
<li>3.3V pour FPGA</li>
</ul>

<hr>

<h2>PART C: ASPECTS TECHNIQUES</h2>

<h3>Réalisation pratique</h3>

<p><strong>Phase 1 : Prototypage breadboard</strong></p>
<ul>
<li>Tests amplification et filtrage</li>
<li>Validation génération 40 kHz</li>
<li>Tests transducteurs</li>
<li>Mesure portée</li>
</ul>

<p><strong>Phase 2 : Simulation Proteus</strong></p>
<ul>
<li>Schéma complet</li>
<li>Simulation analogique (filtres)</li>
<li>Co-simulation VHDL/analogique si possible</li>
</ul>

<p><strong>Phase 3 : Conception PCB (Altium/KiCad)</strong></p>
<ul>
<li>Schéma électrique complet</li>
<li>Footprints composants</li>
<li>Routage 4 couches</li>
<li>DRC (Design Rule Check)</li>
<li>Génération Gerber + BOM</li>
</ul>

<p><strong>Phase 4 : Fabrication et assemblage</strong></p>
<ul>
<li>Fabrication PCB (3-7 jours)</li>
<li>Soudure CMS (fer, air chaud ou four)</li>
<li>Soudure traversants</li>
<li>Inspection visuelle</li>
</ul>

<p><strong>Phase 5 : Tests et validation</strong></p>
<ul>
<li>Tests alimentation (tensions, ondulations)</li>
<li>Tests unitaires (étage par étage)</li>
<li>Programmation FPGA</li>
<li>Tests fonctionnels (mesures distances)</li>
<li>Calibration si nécessaire</li>
</ul>

<h3>Outils utilisés</h3>
<ul>
<li><strong>Proteus</strong> : Simulation</li>
<li><strong>Quartus / Vivado</strong> : VHDL</li>
<li><strong>Altium / KiCad</strong> : PCB</li>
<li><strong>Oscilloscope</strong> : Signaux analogiques</li>
<li><strong>Analyseur logique</strong> : Signaux numériques</li>
<li><strong>Multimètre</strong> : Tensions, continuités</li>
</ul>

<hr>

<h2>PART D: ANALYSE ET RÉFLEXION</h2>

<h3>Évaluation</h3>

<p><strong>Livrables (100%) :</strong></p>
<ul>
<li>Analyse et spécifications (10%)</li>
<li>Schémas et simulations (20%)</li>
<li>PCB conception (15%)</li>
<li>Code VHDL et testbench (15%)</li>
<li>Réalisation matérielle (20%)</li>
<li>Tests et validation (10%)</li>
<li>Rapport technique (10%)</li>
</ul>

<p><strong>Critères qualité :</strong></p>
<ul>
<li>Fonctionnalité complète</li>
<li>Qualité conception (schéma, PCB)</li>
<li>Robustesse (tests, gestion erreurs)</li>
<li>Documentation (clarté, complétude)</li>
</ul>

<h3>Compétences acquises</h3>
<ul>
<li>Gestion projet électronique complet</li>
<li>Intégration analogique/numérique/FPGA</li>
<li>Conception PCB multicouche professionnelle</li>
<li>Traitement du signal pratique</li>
<li>Tests et validation systématiques</li>
<li>Documentation technique</li>
</ul>

<h3>Applications métier</h3>
<ul>
<li>Ingénieur conception électronique</li>
<li>Chef de projet systèmes embarqués</li>
<li>Ingénieur R&amp;D capteurs/instrumentation</li>
<li>Concepteur objets connectés</li>
</ul>

<h2>Contenu du cours</h2>

<h3>Projet Télémètre</h3>

<h4>Description du projet</h4>
<p>Conception d'un télémètre ultrasonique intégrant :</p>
<ul>
<li>Génération de signaux ultrasoniques</li>
<li>Émission et réception d'ondes</li>
<li>Traitement du signal reçu</li>
<li>Mesure de distance</li>
<li>Affichage et interface utilisateur</li>
<li>Logique de contrôle (VHDL/FPGA)</li>
</ul>

<h4>Architecture système</h4>
<p><strong>Partie émission :</strong></p>
<ul>
<li>Générateur de signaux (40 kHz typique)</li>
<li>Amplificateur de puissance</li>
<li>Transducteur ultrasonique émetteur</li>
<li>Contrôle de l'émission</li>
</ul>

<p><strong>Partie réception :</strong></p>
<ul>
<li>Transducteur ultrasonique récepteur</li>
<li>Préamplification faible bruit</li>
<li>Filtrage passe-bande</li>
<li>Détection d'enveloppe</li>
<li>Comparateur à seuil</li>
</ul>

<p><strong>Traitement numérique :</strong></p>
<ul>
<li>Comptage du temps de vol</li>
<li>Calcul de distance</li>
<li>Affichage (LCD, 7 segments)</li>
<li>Interface UART (communication)</li>
</ul>

<p><strong>Partie logique (VHDL) :</strong></p>
<ul>
<li>Contrôleur de séquence</li>
<li>Génération de timing</li>
<li>Gestion d'affichage</li>
<li>Interface de communication</li>
</ul>

<h3>Conception électronique</h3>

<h4>Amplification et conditionnement</h4>
<ul>
<li>Amplificateurs d'instrumentation</li>
<li>Filtres actifs (Butterworth, Chebyshev)</li>
<li>AGC (Automatic Gain Control)</li>
<li>Comparateurs rapides</li>
<li>Circuits de protection</li>
</ul>

<h4>Génération de signaux</h4>
<ul>
<li>Oscillateurs à quartz</li>
<li>Synthèse de fréquences</li>
<li>Burst generation</li>
<li>Drivers de transducteurs</li>
</ul>

<h4>Alimentations</h4>
<ul>
<li>Régulateurs linéaires et à découpage</li>
<li>Gestion multi-tensions</li>
<li>Découplage et filtrage</li>
<li>Protection et surveillance</li>
</ul>

<h3>Conception numérique VHDL</h3>

<h4>Architecture FPGA/CPLD</h4>
<ul>
<li>Sélection du composant</li>
<li>Contraintes de conception</li>
<li>Synthèse et routage</li>
<li>Configuration et programmation</li>
</ul>

<h4>Modules VHDL</h4>
<ul>
<li>Machine à états (FSM)</li>
<li>Compteurs et timers</li>
<li>Diviseurs de fréquence</li>
<li>Gestion d'affichage</li>
<li>Interface série (UART)</li>
</ul>

<h4>Simulation et validation</h4>
<ul>
<li>Testbench VHDL</li>
<li>Simulation fonctionnelle</li>
<li>Simulation temporelle</li>
<li>Vérification timing</li>
</ul>

<h3>Conception PCB avancée</h3>

<h4>Multicouches</h4>
<ul>
<li>Stratégie de routage 4 couches</li>
<li>Plans de masse et alimentation</li>
<li>Via stitching</li>
<li>Découplage optimisé</li>
</ul>

<h4>Considérations RF</h4>
<ul>
<li>Impédance contrôlée (si nécessaire)</li>
<li>Séparation analogique/numérique</li>
<li>Routage différentiel</li>
<li>Antennes et zones sensibles</li>
</ul>

<h4>DFM et DFT</h4>
<ul>
<li>Design for Manufacturing</li>
<li>Design for Test</li>
<li>Points de test</li>
<li>Accessibilité des composants</li>
</ul>

<h2>Réalisation pratique</h2>

<h3>Prototypage</h3>
<ul>
<li>Simulation sous Proteus</li>
<li>Tests sur breadboard</li>
<li>Validation par sous-ensembles</li>
<li>Mesures préliminaires</li>
</ul>

<h3>Fabrication</h3>
<ul>
<li>Génération fichiers Gerber</li>
<li>Fabrication PCB professionnelle</li>
<li>Réception et contrôle qualité</li>
<li>Préparation à l'assemblage</li>
</ul>

<h3>Assemblage</h3>
<ul>
<li>Programmation FPGA/CPLD</li>
<li>Soudure CMS et traversants</li>
<li>Inspection visuelle</li>
<li>Tests électriques</li>
</ul>

<h3>Mise au point</h3>
<ul>
<li>Tests unitaires par blocs</li>
<li>Intégration progressive</li>
<li>Calibration</li>
<li>Optimisation des performances</li>
</ul>

<h2>Outils utilisés</h2>

<h3>CAO Électronique</h3>
<ul>
<li><strong>Proteus ISIS/ARES</strong> : Schémas et PCB</li>
<li><strong>Altium Designer / KiCad</strong> : PCB avancé</li>
<li><strong>LTspice</strong> : Simulation analogique</li>
</ul>

<h3>VHDL et FPGA</h3>
<ul>
<li><strong>Quartus Prime</strong> : FPGA Intel/Altera</li>
<li><strong>Vivado</strong> : FPGA Xilinx</li>
<li><strong>ModelSim</strong> : Simulation VHDL</li>
</ul>

<h3>Mesure et test</h3>
<ul>
<li>Oscilloscope numérique</li>
<li>Analyseur de spectre</li>
<li>Générateur de fonctions</li>
<li>Multimètre de précision</li>
</ul>

<h2>Évaluation</h2>
<ul>
<li>Conception (schémas, PCB, VHDL) (30%)</li>
<li>Réalisation et assemblage (25%)</li>
<li>Tests et performances (25%)</li>
<li>Documentation technique (15%)</li>
<li>Présentation (5%)</li>
</ul>

<h2>Liens avec d'autres cours</h2>
<ul>
<li><strong>SE</strong> : Traitement du signal</li>
<li><strong>ENC</strong> : Conception numérique VHDL</li>
<li><strong>IE</strong> : Programmation embarquée</li>
<li><strong>Télécommunications</strong> : Propagation des ondes</li>
<li><strong>OL</strong> : Documentation et CAO</li>
</ul>

<h2>Spécifications techniques</h2>

<h3>Performances visées</h3>
<ul>
<li>Portée : 2 cm à 4 m</li>
<li>Résolution : ±1 cm</li>
<li>Fréquence ultrasons : 40 kHz</li>
<li>Temps de rafraîchissement : &lt;100 ms</li>
<li>Alimentation : 5V ou 9V</li>
<li>Consommation : &lt;100 mA</li>
</ul>

<h3>Contraintes</h3>
<ul>
<li>Température de fonctionnement : 0-50°C</li>
<li>Bruit ambiant à filtrer</li>
<li>Réponses multiples (échos)</li>
<li>Zones aveugles</li>
</ul>

<h2>Défis techniques</h2>

<h3>Électronique analogique</h3>
<ul>
<li>Amplification à gain élevé stable</li>
<li>Filtrage sélectif 40 kHz</li>
<li>Réjection du bruit</li>
<li>Dynamique du signal</li>
</ul>

<h3>Numérique</h3>
<ul>
<li>Précision du comptage</li>
<li>Gestion des timeouts</li>
<li>Synchronisation émission/réception</li>
<li>Débouncing et antirebond</li>
</ul>

<h3>Mécanique/Acoustique</h3>
<ul>
<li>Positionnement des transducteurs</li>
<li>Angle de détection</li>
<li>Réflexions multiples</li>
<li>Absorption selon les matériaux</li>
</ul>

<h2>Compétences développées</h2>
<ul>
<li>Conception de systèmes mixtes (analogique/numérique)</li>
<li>Programmation VHDL pour FPGA</li>
<li>Design de PCB professionnels</li>
<li>Traitement du signal embarqué</li>
<li>Tests et validation systématiques</li>
<li>Gestion de projet technique</li>
<li>Documentation professionnelle</li>
</ul>

<h2>Livrables du projet</h2>

<h3>Documentation technique</h3>
<ol>
<li>Cahier des charges détaillé</li>
<li>Schémas électroniques commentés</li>
<li>Code VHDL documenté</li>
<li>Layout PCB avec nomenclature</li>
<li>Rapport de tests et mesures</li>
<li>Manuel d'utilisation</li>
</ol>

<h3>Réalisations</h3>
<ul>
<li>PCB fonctionnel assemblé</li>
<li>FPGA/CPLD programmé</li>
<li>Boîtier (optionnel)</li>
<li>Démonstration vidéo</li>
</ul>

<h2>Points d'attention</h2>

<h3>Sécurité</h3>
<ul>
<li>Attention aux tensions d'alimentation</li>
<li>Protection des entrées sensibles</li>
<li>Décharge statique (ESD)</li>
</ul>

<h3>Qualité</h3>
<ul>
<li>Soudures propres et fiables</li>
<li>Vérifications systématiques</li>
<li>Tests progressifs</li>
<li>Documentation à jour</li>
</ul>

<h3>Débogage</h3>
<ul>
<li>Mesures systématiques</li>
<li>Isolation des problèmes</li>
<li>Utilisation de points de test</li>
<li>Comparaison simulation/réalité</li>
</ul>

<h2>Méthode de travail</h2>

<h3>Phase 1 : Étude (2 semaines)</h3>
<ul>
<li>Recherche bibliographique</li>
<li>Calculs théoriques</li>
<li>Simulations préliminaires</li>
<li>Choix des composants</li>
</ul>

<h3>Phase 2 : Conception (3 semaines)</h3>
<ul>
<li>Schématique complète</li>
<li>Code VHDL</li>
<li>Design PCB</li>
<li>Validation simulations</li>
</ul>

<h3>Phase 3 : Réalisation (3 semaines)</h3>
<ul>
<li>Fabrication PCB</li>
<li>Assemblage</li>
<li>Programmation FPGA</li>
<li>Tests unitaires</li>
</ul>

<h3>Phase 4 : Validation (2 semaines)</h3>
<ul>
<li>Tests d'intégration</li>
<li>Mesures de performances</li>
<li>Optimisations</li>
<li>Documentation finale</li>
</ul>

<h2>Ressources</h2>
<ul>
<li>Datasheets transducteurs ultrasoniques</li>
<li>Application notes sur télémétrie</li>
<li>Exemples VHDL de compteurs</li>
<li>Normes PCB (IPC)</li>
<li>Tutoriels Proteus/Quartus</li>
</ul>

</div>

<div class="lang-en">

<h1>Study and Implementation (ER) - Semester 3</h1>

<p><strong>Year</strong>: 2021-2022 | <strong>Semester</strong>: 3 | <strong>Type</strong>: Technical</p>

<hr>

<h2>PART A - General Course Overview</h2>

<h3>Context and objectives</h3>

<p>Major S3 project: design and implementation of an <strong>ultrasonic rangefinder</strong> integrating analog electronics (amplification, filtering), digital electronics (VHDL/FPGA) and signal processing. Multidisciplinary project mobilizing all GEII skills.</p>

<p><strong>Objectives:</strong></p>
<ul>
<li>Design a complete system (specs → implementation)</li>
<li>Integrate analog + digital + FPGA</li>
<li>Professional multi-layer PCB</li>
<li>Validation through testing and measurements</li>
<li>Complete technical documentation</li>
</ul>

<h3>Prerequisites</h3>
<ul>
<li>Analog electronics (amplifiers, filters)</li>
<li>VHDL (FSM, counters)</li>
<li>PCB design</li>
<li>Signal processing</li>
</ul>

<hr>

<h2>PART B: EXPERIENCE, CONTEXT AND FUNCTION</h2>

<h3>Ultrasonic Rangefinder System</h3>

<p><strong>Principle:</strong><br>
Distance measurement by time-of-flight of ultrasonic waves (40 kHz typical).<br>
Distance = (c × Δt) / 2, where c ≈ 340 m/s</p>

<p><strong>Architecture:</strong></p>
<pre><code>[FPGA/CPLD] → [Driver] → [TX Transducer]
                             ↓ US waves
                          [Target]
                             ↓ echo
[FPGA] ← [Comparator] ← [Filtering] ← [Amp] ← [RX Transducer]
   ↓
[LCD Display / UART]</code></pre>

<h3>Module 1: Transmission Chain</h3>

<p><strong>40 kHz burst generation:</strong></p>
<ul>
<li>FPGA: counter + frequency divider</li>
<li>Burst: 8-10 cycles (200-250 us)</li>
<li>Push-pull driver (transistors or H-bridge)</li>
<li>40 kHz piezo transducer (impedance ≈ 2kOhm)</li>
</ul>

<p><strong>Electronics:</strong></p>
<ul>
<li>Class B or D amplifier for efficiency</li>
<li>Protection (clamping diodes)</li>
<li>Impedance matching</li>
</ul>

<h3>Module 2: Reception Chain</h3>

<p><strong>RX Transducer:</strong></p>
<ul>
<li>Same frequency as TX (40 kHz)</li>
<li>Weak signal (a few mV)</li>
</ul>

<p><strong>Preamplification:</strong></p>
<ul>
<li>Instrumentation amplifier or low-noise op-amp</li>
<li>Gain: 40-60 dB</li>
<li>Bandpass filtering 38-42 kHz (Sallen-Key 2nd order)</li>
</ul>

<p><strong>Envelope detection:</strong></p>
<ul>
<li>Rectifier + RC filtering</li>
<li>Or peak detector (diode + hold capacitor)</li>
</ul>

<p><strong>Threshold comparator:</strong></p>
<ul>
<li>Adjustable threshold (potentiometer or DAC)</li>
<li>TTL/CMOS output → FPGA</li>
<li>Hysteresis (Schmitt trigger) for stability</li>
</ul>

<h3>Module 3: VHDL Digital Processing</h3>

<p><strong>Control FSM:</strong></p>
<ol>
<li>IDLE: waiting for command</li>
<li>EMIT: TX burst generation</li>
<li>WAIT_ECHO: time counting (counter++)</li>
<li>ECHO_DETECTED: distance calculation</li>
<li>DISPLAY: display update</li>
</ol>

<p><strong>Time-of-flight counter:</strong></p>
<ul>
<li>1 MHz clock → 1 us resolution</li>
<li>Counting between end of burst and echo rising edge</li>
<li>Timeout if no echo (3-5 m max)</li>
</ul>

<p><strong>Distance calculation:</strong></p>
<ul>
<li>Distance (cm) = (Counter × 340 m/s) / (2 × 10^4)</li>
<li>Implementation: division or multiplication by constant</li>
</ul>

<p><strong>Interface:</strong></p>
<ul>
<li>16x2 LCD (distance display)</li>
<li>UART (PC transmission)</li>
<li>Status LEDs</li>
</ul>

<h3>Module 4: PCB Integration</h3>

<p><strong>4-layer PCB:</strong></p>
<ul>
<li>L1: Analog (amplifiers, filters)</li>
<li>L2: GND plane</li>
<li>L3: Power planes (+/-12V, 5V, 3.3V)</li>
<li>L4: Digital (FPGA, display)</li>
</ul>

<p><strong>Design rules:</strong></p>
<ul>
<li>Analog/digital separation (single GND bridge at 1 point)</li>
<li>Intensive decoupling</li>
<li>RF zone shielding if necessary</li>
<li>GND via stitching</li>
</ul>

<p><strong>Power supply:</strong></p>
<ul>
<li>12V or USB 5V input</li>
<li>Linear regulators (7805, 7812, 7912) or switching</li>
<li>Dual +/-12V rail for amplifiers</li>
<li>3.3V for FPGA</li>
</ul>

<hr>

<h2>PART C: TECHNICAL ASPECTS</h2>

<h3>Practical implementation</h3>

<p><strong>Phase 1: Breadboard prototyping</strong></p>
<ul>
<li>Amplification and filtering tests</li>
<li>40 kHz generation validation</li>
<li>Transducer tests</li>
<li>Range measurement</li>
</ul>

<p><strong>Phase 2: Proteus simulation</strong></p>
<ul>
<li>Complete schematic</li>
<li>Analog simulation (filters)</li>
<li>VHDL/analog co-simulation if possible</li>
</ul>

<p><strong>Phase 3: PCB design (Altium/KiCad)</strong></p>
<ul>
<li>Complete electrical schematic</li>
<li>Component footprints</li>
<li>4-layer routing</li>
<li>DRC (Design Rule Check)</li>
<li>Gerber + BOM generation</li>
</ul>

<p><strong>Phase 4: Manufacturing and assembly</strong></p>
<ul>
<li>PCB manufacturing (3-7 days)</li>
<li>SMD soldering (iron, hot air or oven)</li>
<li>Through-hole soldering</li>
<li>Visual inspection</li>
</ul>

<p><strong>Phase 5: Testing and validation</strong></p>
<ul>
<li>Power supply tests (voltages, ripple)</li>
<li>Unit tests (stage by stage)</li>
<li>FPGA programming</li>
<li>Functional tests (distance measurements)</li>
<li>Calibration if necessary</li>
</ul>

<h3>Tools used</h3>
<ul>
<li><strong>Proteus</strong>: Simulation</li>
<li><strong>Quartus / Vivado</strong>: VHDL</li>
<li><strong>Altium / KiCad</strong>: PCB</li>
<li><strong>Oscilloscope</strong>: Analog signals</li>
<li><strong>Logic analyzer</strong>: Digital signals</li>
<li><strong>Multimeter</strong>: Voltages, continuity</li>
</ul>

<hr>

<h2>PART D: ANALYSIS AND REFLECTION</h2>

<h3>Assessment</h3>

<p><strong>Deliverables (100%):</strong></p>
<ul>
<li>Analysis and specifications (10%)</li>
<li>Schematics and simulations (20%)</li>
<li>PCB design (15%)</li>
<li>VHDL code and testbench (15%)</li>
<li>Hardware implementation (20%)</li>
<li>Testing and validation (10%)</li>
<li>Technical report (10%)</li>
</ul>

<p><strong>Quality criteria:</strong></p>
<ul>
<li>Complete functionality</li>
<li>Design quality (schematic, PCB)</li>
<li>Robustness (tests, error handling)</li>
<li>Documentation (clarity, completeness)</li>
</ul>

<h3>Skills acquired</h3>
<ul>
<li>Complete electronic project management</li>
<li>Analog/digital/FPGA integration</li>
<li>Professional multi-layer PCB design</li>
<li>Practical signal processing</li>
<li>Systematic testing and validation</li>
<li>Technical documentation</li>
</ul>

<h3>Career applications</h3>
<ul>
<li>Electronic design engineer</li>
<li>Embedded systems project manager</li>
<li>R&amp;D engineer sensors/instrumentation</li>
<li>Connected objects designer</li>
</ul>

<h2>Course content</h2>

<h3>Rangefinder Project</h3>

<h4>Project description</h4>
<p>Design of an ultrasonic rangefinder integrating:</p>
<ul>
<li>Ultrasonic signal generation</li>
<li>Wave emission and reception</li>
<li>Received signal processing</li>
<li>Distance measurement</li>
<li>Display and user interface</li>
<li>Control logic (VHDL/FPGA)</li>
</ul>

<h4>System architecture</h4>
<p><strong>Transmission part:</strong></p>
<ul>
<li>Signal generator (40 kHz typical)</li>
<li>Power amplifier</li>
<li>Ultrasonic transmitter transducer</li>
<li>Emission control</li>
</ul>

<p><strong>Reception part:</strong></p>
<ul>
<li>Ultrasonic receiver transducer</li>
<li>Low-noise preamplification</li>
<li>Bandpass filtering</li>
<li>Envelope detection</li>
<li>Threshold comparator</li>
</ul>

<p><strong>Digital processing:</strong></p>
<ul>
<li>Time-of-flight counting</li>
<li>Distance calculation</li>
<li>Display (LCD, 7-segment)</li>
<li>UART interface (communication)</li>
</ul>

<p><strong>Logic part (VHDL):</strong></p>
<ul>
<li>Sequence controller</li>
<li>Timing generation</li>
<li>Display management</li>
<li>Communication interface</li>
</ul>

<h3>Electronic design</h3>

<h4>Amplification and conditioning</h4>
<ul>
<li>Instrumentation amplifiers</li>
<li>Active filters (Butterworth, Chebyshev)</li>
<li>AGC (Automatic Gain Control)</li>
<li>Fast comparators</li>
<li>Protection circuits</li>
</ul>

<h4>Signal generation</h4>
<ul>
<li>Crystal oscillators</li>
<li>Frequency synthesis</li>
<li>Burst generation</li>
<li>Transducer drivers</li>
</ul>

<h4>Power supplies</h4>
<ul>
<li>Linear and switching regulators</li>
<li>Multi-voltage management</li>
<li>Decoupling and filtering</li>
<li>Protection and monitoring</li>
</ul>

<h3>VHDL digital design</h3>

<h4>FPGA/CPLD architecture</h4>
<ul>
<li>Component selection</li>
<li>Design constraints</li>
<li>Synthesis and routing</li>
<li>Configuration and programming</li>
</ul>

<h4>VHDL modules</h4>
<ul>
<li>Finite State Machine (FSM)</li>
<li>Counters and timers</li>
<li>Frequency dividers</li>
<li>Display management</li>
<li>Serial interface (UART)</li>
</ul>

<h4>Simulation and validation</h4>
<ul>
<li>VHDL testbench</li>
<li>Functional simulation</li>
<li>Timing simulation</li>
<li>Timing verification</li>
</ul>

<h3>Advanced PCB design</h3>

<h4>Multi-layer</h4>
<ul>
<li>4-layer routing strategy</li>
<li>Ground and power planes</li>
<li>Via stitching</li>
<li>Optimized decoupling</li>
</ul>

<h4>RF considerations</h4>
<ul>
<li>Controlled impedance (if necessary)</li>
<li>Analog/digital separation</li>
<li>Differential routing</li>
<li>Antennas and sensitive areas</li>
</ul>

<h4>DFM and DFT</h4>
<ul>
<li>Design for Manufacturing</li>
<li>Design for Test</li>
<li>Test points</li>
<li>Component accessibility</li>
</ul>

<h2>Practical implementation</h2>

<h3>Prototyping</h3>
<ul>
<li>Proteus simulation</li>
<li>Breadboard testing</li>
<li>Sub-assembly validation</li>
<li>Preliminary measurements</li>
</ul>

<h3>Manufacturing</h3>
<ul>
<li>Gerber file generation</li>
<li>Professional PCB manufacturing</li>
<li>Reception and quality control</li>
<li>Assembly preparation</li>
</ul>

<h3>Assembly</h3>
<ul>
<li>FPGA/CPLD programming</li>
<li>SMD and through-hole soldering</li>
<li>Visual inspection</li>
<li>Electrical tests</li>
</ul>

<h3>Fine-tuning</h3>
<ul>
<li>Block-by-block unit tests</li>
<li>Progressive integration</li>
<li>Calibration</li>
<li>Performance optimization</li>
</ul>

<h2>Tools used</h2>

<h3>Electronic CAD</h3>
<ul>
<li><strong>Proteus ISIS/ARES</strong>: Schematics and PCB</li>
<li><strong>Altium Designer / KiCad</strong>: Advanced PCB</li>
<li><strong>LTspice</strong>: Analog simulation</li>
</ul>

<h3>VHDL and FPGA</h3>
<ul>
<li><strong>Quartus Prime</strong>: Intel/Altera FPGA</li>
<li><strong>Vivado</strong>: Xilinx FPGA</li>
<li><strong>ModelSim</strong>: VHDL simulation</li>
</ul>

<h3>Measurement and testing</h3>
<ul>
<li>Digital oscilloscope</li>
<li>Spectrum analyzer</li>
<li>Function generator</li>
<li>Precision multimeter</li>
</ul>

<h2>Assessment</h2>
<ul>
<li>Design (schematics, PCB, VHDL) (30%)</li>
<li>Implementation and assembly (25%)</li>
<li>Tests and performance (25%)</li>
<li>Technical documentation (15%)</li>
<li>Presentation (5%)</li>
</ul>

<h2>Links with other courses</h2>
<ul>
<li><strong>SE</strong>: Signal processing</li>
<li><strong>ENC</strong>: VHDL digital design</li>
<li><strong>IE</strong>: Embedded programming</li>
<li><strong>Telecommunications</strong>: Wave propagation</li>
<li><strong>OL</strong>: Documentation and CAD</li>
</ul>

<h2>Technical specifications</h2>

<h3>Target performance</h3>
<ul>
<li>Range: 2 cm to 4 m</li>
<li>Resolution: +/-1 cm</li>
<li>Ultrasound frequency: 40 kHz</li>
<li>Refresh time: &lt;100 ms</li>
<li>Power supply: 5V or 9V</li>
<li>Consumption: &lt;100 mA</li>
</ul>

<h3>Constraints</h3>
<ul>
<li>Operating temperature: 0-50 degrees C</li>
<li>Ambient noise to filter</li>
<li>Multiple responses (echoes)</li>
<li>Blind zones</li>
</ul>

<h2>Technical challenges</h2>

<h3>Analog electronics</h3>
<ul>
<li>Stable high-gain amplification</li>
<li>Selective 40 kHz filtering</li>
<li>Noise rejection</li>
<li>Signal dynamics</li>
</ul>

<h3>Digital</h3>
<ul>
<li>Counting accuracy</li>
<li>Timeout management</li>
<li>Transmission/reception synchronization</li>
<li>Debouncing</li>
</ul>

<h3>Mechanical/Acoustic</h3>
<ul>
<li>Transducer positioning</li>
<li>Detection angle</li>
<li>Multiple reflections</li>
<li>Material-dependent absorption</li>
</ul>

<h2>Skills developed</h2>
<ul>
<li>Mixed system design (analog/digital)</li>
<li>VHDL programming for FPGA</li>
<li>Professional PCB design</li>
<li>Embedded signal processing</li>
<li>Systematic testing and validation</li>
<li>Technical project management</li>
<li>Professional documentation</li>
</ul>

<h2>Project deliverables</h2>

<h3>Technical documentation</h3>
<ol>
<li>Detailed specifications</li>
<li>Commented electronic schematics</li>
<li>Documented VHDL code</li>
<li>PCB layout with bill of materials</li>
<li>Test and measurement report</li>
<li>User manual</li>
</ol>

<h3>Achievements</h3>
<ul>
<li>Assembled functional PCB</li>
<li>Programmed FPGA/CPLD</li>
<li>Enclosure (optional)</li>
<li>Video demonstration</li>
</ul>

<h2>Points of attention</h2>

<h3>Safety</h3>
<ul>
<li>Attention to supply voltages</li>
<li>Protection of sensitive inputs</li>
<li>Electrostatic discharge (ESD)</li>
</ul>

<h3>Quality</h3>
<ul>
<li>Clean and reliable solder joints</li>
<li>Systematic checks</li>
<li>Progressive testing</li>
<li>Up-to-date documentation</li>
</ul>

<h3>Debugging</h3>
<ul>
<li>Systematic measurements</li>
<li>Problem isolation</li>
<li>Use of test points</li>
<li>Simulation/reality comparison</li>
</ul>

<h2>Working method</h2>

<h3>Phase 1: Study (2 weeks)</h3>
<ul>
<li>Literature review</li>
<li>Theoretical calculations</li>
<li>Preliminary simulations</li>
<li>Component selection</li>
</ul>

<h3>Phase 2: Design (3 weeks)</h3>
<ul>
<li>Complete schematic</li>
<li>VHDL code</li>
<li>PCB design</li>
<li>Simulation validation</li>
</ul>

<h3>Phase 3: Implementation (3 weeks)</h3>
<ul>
<li>PCB manufacturing</li>
<li>Assembly</li>
<li>FPGA programming</li>
<li>Unit tests</li>
</ul>

<h3>Phase 4: Validation (2 weeks)</h3>
<ul>
<li>Integration tests</li>
<li>Performance measurements</li>
<li>Optimizations</li>
<li>Final documentation</li>
</ul>

<h2>Resources</h2>
<ul>
<li>Ultrasonic transducer datasheets</li>
<li>Application notes on ranging</li>
<li>VHDL counter examples</li>
<li>PCB standards (IPC)</li>
<li>Proteus/Quartus tutorials</li>
</ul>

</div>

<div class="pdf-container">
  <div class="pdf-viewer">

    <div class="pdf-item">
      <h4 class="lang-fr">OPA2350 - Amplificateur Operationnel</h4>
      <h4 class="lang-en">OPA2350 - Operational Amplifier</h4>
      <p class="lang-fr">Datasheet de l'amplificateur operationnel OPA2350 utilise dans le projet telemetre ultrasonique.</p>
      <p class="lang-en">Datasheet for the OPA2350 operational amplifier used in the ultrasonic rangefinder project.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S3/ER/opa2350.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S3/ER/opa2350.pdf" target="_blank" class="lang-fr" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
        <a href="/cours-pdf/S3/ER/opa2350.pdf" target="_blank" class="lang-en" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Download PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4 class="lang-fr">MAX941/MAX944 - Comparateurs</h4>
      <h4 class="lang-en">MAX941/MAX944 - Comparators</h4>
      <p class="lang-fr">Datasheet des comparateurs rapides MAX941-MAX944 pour la detection de seuil.</p>
      <p class="lang-en">Datasheet for the MAX941-MAX944 fast comparators for threshold detection.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S3/ER/MAX941-MAX944.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S3/ER/MAX941-MAX944.pdf" target="_blank" class="lang-fr" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
        <a href="/cours-pdf/S3/ER/MAX941-MAX944.pdf" target="_blank" class="lang-en" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Download PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4 class="lang-fr">Si9986 - Driver Pont en H</h4>
      <h4 class="lang-en">Si9986 - H-Bridge Driver</h4>
      <p class="lang-fr">Datasheet du driver de pont en H Si9986 pour la commande de l'emetteur ultrasonique.</p>
      <p class="lang-en">Datasheet for the Si9986 H-bridge driver for ultrasonic transmitter control.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S3/ER/si9986.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S3/ER/si9986.pdf" target="_blank" class="lang-fr" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
        <a href="/cours-pdf/S3/ER/si9986.pdf" target="_blank" class="lang-en" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Download PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4 class="lang-fr">MCP41xx - Potentiometre Numerique SPI</h4>
      <h4 class="lang-en">MCP41xx - SPI Digital Potentiometer</h4>
      <p class="lang-fr">Datasheet du potentiometre numerique MCP41xx commande par bus SPI.</p>
      <p class="lang-en">Datasheet for the MCP41xx digital potentiometer controlled via SPI bus.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S3/ER/mcp41xx.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S3/ER/mcp41xx.pdf" target="_blank" class="lang-fr" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
        <a href="/cours-pdf/S3/ER/mcp41xx.pdf" target="_blank" class="lang-en" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Download PDF</a>
      </p>
    </div>

  </div>
</div>

<style>body{font-family:Arial,sans-serif;background-color:#f4f4f9;color:#333;line-height:1.6}h2,h3,h4,h5{color:#2a7ae2}p{text-align:justify}code{background-color:#f5f5f5;padding:2px 6px;border-radius:3px;font-family:'Courier New',monospace}pre{background-color:#f5f5f5;padding:15px;border-radius:5px;overflow-x:auto}</style>

<div class="back-nav">
  <a href="./my-courses-2021-2022.html" data-i18n-html="back-courses-2021-2022">&larr; Retour a Mes Cours 2021-2022</a>
</div>

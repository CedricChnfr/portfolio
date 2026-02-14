---
layout: default
title: "Électronique et Réalisation (ER) - S1"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
---

<div class="lang-fr">

<h1>Electronique et Realisation (ER) - Semestre 1</h1>

<h2>PART A - Presentation Generale du Cours</h2>

<h3>Contexte de la formation</h3>
<p>Le module Electronique et Realisation (ER) constitue le coeur pratique de la formation GEII. Il combine theorie electronique et realisation concrete de circuits, permettant aux etudiants de comprendre le fonctionnement des composants electroniques et de les mettre en oeuvre dans des projets reels. L'utilisation intensive du logiciel Proteus ISIS prepare les etudiants a la conception assistee par ordinateur utilisee en entreprise.</p>

<h3>Positionnement dans le cursus</h3>
<ul>
  <li><strong>Semestre</strong> : S1 (1ere annee DUT GEII)</li>
  <li><strong>Volume horaire</strong> : 70h (30h CM + 20h TD + 20h TP + Projets)</li>
  <li><strong>Credits ECTS</strong> : 6</li>
  <li><strong>Prerequis</strong> : Bases en electricite (niveau Terminale), mathematiques (nombres complexes)</li>
  <li><strong>Continuite</strong> : ER S2 (Microcontroleurs, Interface, FPGA), puis Systemes Electroniques S3-S4</li>
</ul>

<h3>Public vise</h3>
<p>Etudiants de premiere annee decouvrant l'electronique analogique avec une approche pratique et orientee projet. Le cours s'adresse aussi bien aux debutants qu'a ceux ayant suivi une specialite scientifique au lycee.</p>

<hr/>

<h2>PART B: EXPERIENCE, CONTEXTE ET FONCTION</h2>

<h3>Objectifs pedagogiques</h3>

<p><strong>Competences en composants electroniques :</strong></p>
<ul>
  <li>Identifier et caracteriser les composants passifs (R, L, C) et actifs (diodes, transistors, AOP)</li>
  <li>Comprendre le fonctionnement physique et les modeles equivalents</li>
  <li>Choisir les composants selon les specifications d'un cahier des charges</li>
  <li>Lire et interpreter une datasheet (fiche technique)</li>
</ul>

<p><strong>Competences en conception :</strong></p>
<ul>
  <li>Concevoir des circuits analogiques simples</li>
  <li>Simuler et valider un circuit avant realisation</li>
  <li>Dimensionner les composants</li>
  <li>Optimiser un circuit selon des contraintes</li>
</ul>

<p><strong>Competences pratiques :</strong></p>
<ul>
  <li>Utiliser Proteus ISIS pour la simulation</li>
  <li>Realiser des montages sur breadboard</li>
  <li>Mesurer et valider experimentalement</li>
  <li>Deboguer et depanner des circuits</li>
</ul>

<h3>Programme detaille</h3>

<h4>1. Composants passifs (10h)</h4>

<p><strong>Resistances (R) :</strong></p>

<p><strong>Caracteristiques :</strong></p>
<ul>
  <li>Loi d'Ohm : V = R x I</li>
  <li>Puissance dissipee : P = R x I&sup2; = V&sup2;/R</li>
  <li>Technologie : couche carbone, metalliques, bobinees</li>
  <li>Code couleur (4 ou 5 anneaux)</li>
  <li>Valeurs normalisees (serie E12, E24)</li>
</ul>

<p><strong>Associations :</strong></p>
<ul>
  <li>Serie : R_eq = R1 + R2 + ... + Rn</li>
  <li>Parallele : 1/R_eq = 1/R1 + 1/R2 + ... + 1/Rn</li>
  <li>Diviseur de tension : V_out = V_in x R2/(R1+R2)</li>
</ul>

<p><strong>Condensateurs (C) :</strong></p>

<p><strong>Principe physique :</strong></p>
<ul>
  <li>Stockage d'energie electrique (champ electrique)</li>
  <li>Relation : Q = C x V</li>
  <li>Courant : I = C x dV/dt</li>
  <li>Impedance complexe : Z_C = 1/(jCw) = -j/(Cw)</li>
</ul>

<p><strong>Technologies :</strong></p>
<ul>
  <li><strong>Electrolytiques</strong> : Forte capacite (uF a mF), polarises, ESR elevee</li>
  <li><strong>Ceramiques</strong> : Moyennes valeurs (pF a uF), non polarises, rapides</li>
  <li><strong>Films</strong> : Precision, stabilite, audio</li>
</ul>

<p><strong>Applications :</strong></p>
<ul>
  <li>Filtrage d'alimentation (decouplage)</li>
  <li>Couplage/decouplage AC</li>
  <li>Filtres RC (passe-bas, passe-haut)</li>
  <li>Temporisation</li>
  <li>Stockage d'energie</li>
</ul>

<p><strong>Charge/decharge :</strong></p>
<ul>
  <li>Charge : V_C(t) = V_max x (1 - e^(-t/tau)) avec tau = RC</li>
  <li>Decharge : V_C(t) = V_max x e^(-t/tau)</li>
</ul>

<p><strong>Inductances (L) :</strong></p>

<p><strong>Principe physique :</strong></p>
<ul>
  <li>Stockage d'energie magnetique</li>
  <li>Tension : V = L x dI/dt</li>
  <li>Impedance complexe : Z_L = jLw</li>
</ul>

<p><strong>Applications :</strong></p>
<ul>
  <li>Filtrage (bobines de choc)</li>
  <li>Transformateurs</li>
  <li>Moteurs et relais</li>
  <li>Filtres LC</li>
</ul>

<p><strong>Impedances complexes (synthese) :</strong></p>
<p>En regime sinusoidal (AC), utilisation de la notation complexe :</p>
<ul>
  <li>Resistance : Z_R = R (en phase)</li>
  <li>Inductance : Z_L = jLw (courant en retard de 90 deg)</li>
  <li>Condensateur : Z_C = -j/(Cw) (courant en avance de 90 deg)</li>
</ul>

<h4>2. Diodes et applications (12h)</h4>

<p><strong>Diode a jonction PN :</strong></p>

<p><strong>Principe de fonctionnement :</strong></p>
<ul>
  <li>Jonction P-N de semi-conducteur (Si ou Ge)</li>
  <li>Conduction unidirectionnelle</li>
  <li>Polarisation directe : I = I_s x (e^(V/nV_T) - 1)</li>
  <li>Polarisation inverse : blocage (courant de fuite negligeable)</li>
</ul>

<p><strong>Caracteristiques :</strong></p>
<ul>
  <li>Tension de seuil : V_F &asymp; 0.7V (Si), 0.3V (Ge), 0.2V (Schottky)</li>
  <li>Courant maximal (I_F max)</li>
  <li>Tension inverse max (V_R max ou PIV)</li>
  <li>Temps de commutation (diodes rapides)</li>
</ul>

<p><strong>Modeles equivalents :</strong></p>
<ul>
  <li><strong>Modele ideal</strong> : Interrupteur parfait (V_F = 0)</li>
  <li><strong>Modele simplifie</strong> : Source de tension V_F + resistance r_d</li>
  <li><strong>Modele complet</strong> : Exponentiel (equation de Shockley)</li>
</ul>

<p><strong>Applications pratiques :</strong></p>

<p><strong>1. Redressement :</strong></p>
<ul>
  <li><strong>Redresseur simple alternance</strong> : Conversion AC &rarr; DC pulse</li>
  <li><strong>Redresseur double alternance (pont de Graetz)</strong> : 4 diodes, meilleur rendement</li>
  <li>Filtrage par condensateur : V_ripple &asymp; I_load / (f x C)</li>
</ul>

<p><strong>2. Ecretage :</strong></p>
<ul>
  <li>Limitation d'amplitude d'un signal</li>
  <li>Protection contre les surtensions</li>
  <li>Mise en forme de signaux</li>
</ul>

<p><strong>3. Roue libre (free-wheeling) :</strong></p>
<ul>
  <li>Protection contre les surtensions inductives</li>
  <li>Circuit avec relais, moteurs, electrovannes</li>
</ul>

<p><strong>4. Diodes speciales :</strong></p>
<ul>
  <li><strong>Diode Zener</strong> : Regulation de tension (tension de claquage controlee)</li>
  <li><strong>LED</strong> : Emission lumineuse (V_F &asymp; 1.8V a 3.3V selon couleur)</li>
  <li><strong>Diode Schottky</strong> : Faible chute de tension, rapide (alimentation a decoupage)</li>
  <li><strong>Photodiode</strong> : Conversion lumiere &rarr; courant</li>
</ul>

<h4>3. Transistors bipolaires (BJT) (15h)</h4>

<p><strong>Structure et fonctionnement :</strong></p>

<p><strong>Types :</strong></p>
<ul>
  <li><strong>NPN</strong> : Collecteur (+), Base (commande), Emetteur (reference)</li>
  <li><strong>PNP</strong> : Collecteur (-), Base (commande), Emetteur (reference)</li>
</ul>

<p><strong>Principe :</strong></p>
<ul>
  <li>3 regions : Emetteur (E), Base (B), Collecteur (C)</li>
  <li>Controle du courant I_C par le courant I_B</li>
  <li>Gain en courant : beta = I_C / I_B (typiquement 100-300)</li>
</ul>

<p><strong>Modes de fonctionnement :</strong></p>
<ul>
  <li><strong>Bloque</strong> : V_BE &lt; V_seuil, transistor ouvert (I_C &asymp; 0)</li>
  <li><strong>Actif (lineaire)</strong> : V_BE &ge; 0.7V, I_C = beta x I_B, amplification</li>
  <li><strong>Sature</strong> : V_BE &ge; 0.7V, I_C limite par charge, interrupteur ferme</li>
</ul>

<p><strong>Applications :</strong></p>

<p><strong>1. Interrupteur electronique :</strong></p>
<pre><code>        +Vcc
         |
        [R_C]  (charge)
         |
     C--+--
      NPN
      ---
       |
   [R_B]
       |
    Signal</code></pre>

<p>Dimensionnement :</p>
<ul>
  <li>I_B = (V_in - V_BE) / R_B</li>
  <li>I_C (sature) = (V_cc - V_CE(sat)) / R_C</li>
  <li>Verifier : beta x I_B &gt; I_C (saturation assuree)</li>
</ul>

<p><strong>2. Amplificateur petit signal :</strong></p>
<ul>
  <li>Montage emetteur commun</li>
  <li>Gain en tension : A_v &asymp; -R_C / R_E</li>
  <li>Polarisation par pont de base</li>
</ul>

<p><strong>3. Commande de relais/LED/moteur :</strong></p>
<ul>
  <li>Transistor en commutation</li>
  <li>Protection diode de roue libre</li>
</ul>

<h4>4. Amplificateurs operationnels (AOP) (20h)</h4>

<p><strong>Caracteristiques de l'AOP ideal :</strong></p>
<ul>
  <li>Gain en tension infini : A_v &rarr; &infin;</li>
  <li>Impedance d'entree infinie : Z_in &rarr; &infin;</li>
  <li>Impedance de sortie nulle : Z_out = 0</li>
  <li>Bande passante infinie</li>
  <li>Pas de courant d'entree : I+ = I- = 0</li>
  <li><strong>Regle d'or</strong> : En boucle fermee, V+ = V-</li>
</ul>

<p><strong>Montages fondamentaux :</strong></p>

<p><strong>1. Suiveur (Buffer) :</strong></p>
<ul>
  <li>Gain : A_v = 1</li>
  <li>Impedance d'entree tres elevee</li>
  <li>Adaptation d'impedance</li>
</ul>

<p><strong>2. Amplificateur inverseur :</strong></p>
<pre><code>    R2
   +---+
   |   |
R1 |   v
---+-  |
   |+  +--- V_out
---+   |
   +---+</code></pre>
<ul>
  <li>Gain : A_v = -R2/R1</li>
  <li>Z_in = R1</li>
</ul>

<p><strong>3. Amplificateur non-inverseur :</strong></p>
<ul>
  <li>Gain : A_v = 1 + R2/R1</li>
  <li>Z_in tres elevee</li>
</ul>

<p><strong>4. Sommateur inverseur :</strong></p>
<ul>
  <li>V_out = -(R_f/R1 x V1 + R_f/R2 x V2 + ...)</li>
  <li>Mixer audio, DAC</li>
</ul>

<p><strong>5. Integrateur :</strong></p>
<ul>
  <li>V_out = -(1/RC) &int; V_in dt</li>
  <li>Generation de rampes, filtres</li>
</ul>

<p><strong>6. Derivateur :</strong></p>
<ul>
  <li>V_out = -RC x dV_in/dt</li>
  <li>Detection de fronts</li>
</ul>

<p><strong>7. Comparateur :</strong></p>
<ul>
  <li>V_out = +V_sat si V+ &gt; V-, sinon -V_sat</li>
  <li>Detection de seuil</li>
</ul>

<p><strong>8. Trigger de Schmitt :</strong></p>
<ul>
  <li>Comparateur avec hysteresis</li>
  <li>Antirebond, mise en forme de signaux</li>
</ul>

<p><strong>AOP reels utilises :</strong></p>
<ul>
  <li>TL081/TL084 : JFET, faible courant d'entree</li>
  <li>LM741 : Classique, universel</li>
  <li>LM358 : Dual, alimentation simple</li>
  <li>OPA27 : Bas bruit, precision</li>
</ul>

<h3>Projets pratiques</h3>

<h4>Projet Radar 2020</h4>

<p><strong>Objectif :</strong> Concevoir un systeme de detection et mesure de distance par ultrasons</p>

<p><strong>Specifications :</strong></p>
<ul>
  <li>Emission d'impulsions ultrasoniques (40 kHz)</li>
  <li>Reception et amplification du signal echo</li>
  <li>Mesure du temps de vol</li>
  <li>Calcul et affichage de la distance</li>
</ul>

<p><strong>Blocs fonctionnels :</strong></p>
<ol>
  <li><strong>Emetteur ultrasonique</strong> : Oscillateur 40 kHz + transducteur</li>
  <li><strong>Recepteur</strong> : Transducteur + amplification (AOP)</li>
  <li><strong>Traitement du signal</strong> : Detection d'enveloppe, comparateur</li>
  <li><strong>Logique de mesure</strong> : Microcontroleur ou circuit numerique</li>
  <li><strong>Affichage</strong> : LCD ou LEDs</li>
</ol>

<p><strong>Competences developpees :</strong></p>
<ul>
  <li>Conception de circuits analogiques</li>
  <li>Amplification de signaux faibles</li>
  <li>Interface analogique/numerique</li>
  <li>Mesure de temps et calcul de distance</li>
</ul>

<h4>Derivateur de frequence</h4>

<p><strong>Objectif :</strong> Realiser un circuit dont la sortie est proportionnelle a la derivee du signal d'entree</p>

<p><strong>Principe :</strong></p>
<ul>
  <li>Circuit derivateur a base d'AOP : V_out = -RC x dV_in/dt</li>
  <li>Etude de la reponse frequentielle</li>
  <li>Compensation et stabilisation</li>
</ul>

<p><strong>Analyse :</strong></p>
<ul>
  <li>Fonction de transfert : H(jw) = -jRCw</li>
  <li>Gain : |H| = RCw (croissance lineaire avec f)</li>
  <li>Phase : phi = +90 deg (avance de phase)</li>
</ul>

<p><strong>Applications :</strong></p>
<ul>
  <li>Detection de fronts</li>
  <li>Calcul de vitesse (derivee de position)</li>
  <li>Filtres actifs</li>
</ul>

<h4>Semaine Projet - Filtrage de son</h4>

<p><strong>Objectif :</strong> Concevoir un systeme complet de filtrage actif pour isoler des composantes frequentielles d'un signal audio</p>

<p><strong>Cahier des charges :</strong></p>
<ul>
  <li>Entree : Signal audio (micro ou line-in)</li>
  <li>Filtres : Passe-bas, passe-bande, passe-haut</li>
  <li>Frequences de coupure ajustables</li>
  <li>Sortie : Haut-parleur ou line-out</li>
</ul>

<p><strong>Realisation :</strong></p>
<ol>
  <li><strong>Analyse</strong> : Decomposition frequentielle du signal</li>
  <li><strong>Conception</strong> : Choix topologie (Butterworth, Sallen-Key)</li>
  <li><strong>Simulation</strong> : Proteus ISIS, analyse frequentielle</li>
  <li><strong>Dimensionnement</strong> : Calcul des composants</li>
  <li><strong>Realisation</strong> : Montage sur breadboard puis PCB</li>
  <li><strong>Tests</strong> : Mesures oscilloscope et analyseur de spectre</li>
  <li><strong>Documentation</strong> : Rapport technique complet</li>
</ol>

<p><strong>Livrables :</strong></p>
<ul>
  <li>Schemas electroniques</li>
  <li>Simulations (diagrammes de Bode)</li>
  <li>Prototype fonctionnel</li>
  <li>Mesures et validation</li>
  <li>Rapport technique</li>
</ul>

<hr/>

<h2>PART C: ASPECTS TECHNIQUES</h2>

<h3>Logiciels de simulation</h3>

<h4>Proteus ISIS (Labcenter Electronics)</h4>

<p><strong>Fonctionnalites :</strong></p>
<ul>
  <li>Saisie de schemas electroniques</li>
  <li>Bibliotheque exhaustive de composants</li>
  <li>Simulation SPICE (analogique, numerique, mixte)</li>
  <li>Instruments virtuels (oscilloscope, multimetre, GBF)</li>
  <li>Simulation temporelle et frequentielle</li>
  <li>Analyse DC, AC, transitoire</li>
</ul>

<p><strong>Workflow de conception :</strong></p>

<p><strong>1. Creation de schema :</strong></p>
<ul>
  <li>Placer les composants (P)</li>
  <li>Cabler (W pour wire)</li>
  <li>Nommer les noeuds (L pour label)</li>
  <li>Definir les valeurs des composants</li>
</ul>

<p><strong>2. Instruments virtuels :</strong></p>
<ul>
  <li>Oscilloscope : Visualisation temporelle</li>
  <li>Voltmetre/Amperemetre : Mesures DC/AC</li>
  <li>GBF (generateur) : Signaux d'excitation</li>
  <li>Analyseur de spectre : Contenu frequentiel</li>
</ul>

<p><strong>3. Simulation :</strong></p>
<ul>
  <li><strong>Transient Analysis</strong> : Evolution temporelle</li>
  <li><strong>AC Sweep</strong> : Reponse frequentielle (Bode)</li>
  <li><strong>DC Sweep</strong> : Caracteristique statique</li>
</ul>

<p><strong>4. Exploitation :</strong></p>
<ul>
  <li>Releve de courbes</li>
  <li>Mesures (amplitude, phase, frequence)</li>
  <li>Export vers rapport</li>
</ul>

<p><strong>Exemple : Simulation d'un filtre RC passe-bas</strong></p>
<pre><code>1. Schema : GBF &rarr; R &rarr; C &rarr; GND
2. Parametres GBF : Sinus, amplitude 5V, sweep 1Hz-100kHz
3. Oscilloscope : Entree (GBF) et sortie (noeud RC)
4. AC Analysis : Tracer |H(f)| et Phase(f)
5. Mesure f_c a -3dB : f_c = 1/(2piRC)</code></pre>

<p><strong>Conseils pratiques :</strong></p>
<ul>
  <li>Nommer explicitement les noeuds importants</li>
  <li>Utiliser des masses communes</li>
  <li>Verifier les modeles de composants (parfois idealises)</li>
  <li>Sauvegarder regulierement</li>
  <li>Documenter avec des annotations sur le schema</li>
</ul>

<h4>Alternatives et complements</h4>

<p><strong>LTspice (Analog Devices) :</strong></p>
<ul>
  <li>Gratuit, tres performant</li>
  <li>Simulation SPICE pure</li>
  <li>Bibliotheque de composants ADI</li>
  <li>Export SPICE depuis Proteus possible</li>
</ul>

<p><strong>Tinkercad Circuits :</strong></p>
<ul>
  <li>Simulation en ligne gratuite</li>
  <li>Interface simple et intuitive</li>
  <li>Ideal pour apprentissage</li>
  <li>Limitation : Moins de composants</li>
</ul>

<h3>Equipements de laboratoire</h3>

<h4>Oscilloscope numerique</h4>

<p><strong>Fonctions principales :</strong></p>
<ul>
  <li><strong>Acquisition</strong> : Echantillonnage du signal (MHz a GHz)</li>
  <li><strong>Affichage</strong> : Visualisation temporelle</li>
  <li><strong>Mesures automatiques</strong> : V_pp, V_rms, f, periode, duty cycle</li>
  <li><strong>Declenchement (trigger)</strong> : Edge, pulse, video</li>
  <li><strong>Curseurs</strong> : Mesures precises</li>
  <li><strong>Math</strong> : Operations (A+B, A-B, FFT)</li>
</ul>

<p><strong>Utilisation typique :</strong></p>
<ul>
  <li>Reglage base de temps (s/div) et sensibilite (V/div)</li>
  <li>Declenchement sur le signal</li>
  <li>Mode AC/DC selon l'application</li>
  <li>Mesure dephasage entre 2 signaux (mode XY ou mesure temporelle)</li>
</ul>

<h4>Generateur de fonctions (GBF)</h4>

<p><strong>Signaux generes :</strong></p>
<ul>
  <li><strong>Sinusoidal</strong> : Tests frequentiels, audio</li>
  <li><strong>Carre</strong> : Signaux logiques, PWM</li>
  <li><strong>Triangle/Rampe</strong> : Balayage, integration</li>
  <li><strong>Impulsion</strong> : Tests transitoires</li>
  <li><strong>Bruit</strong> : Tests de robustesse</li>
</ul>

<p><strong>Parametres reglables :</strong></p>
<ul>
  <li>Frequence : mHz a MHz</li>
  <li>Amplitude : mV a V</li>
  <li>Offset DC : Decalage vertical</li>
  <li>Duty cycle : Rapport cyclique (signaux carres)</li>
  <li>Sweep : Balayage en frequence</li>
</ul>

<h4>Multimetre numerique</h4>

<p><strong>Mesures :</strong></p>
<ul>
  <li>Tension DC/AC (V)</li>
  <li>Courant DC/AC (A)</li>
  <li>Resistance (Ohm)</li>
  <li>Continuite (beeper)</li>
  <li>Test de diodes (V_F)</li>
  <li>Capacite (certains modeles)</li>
  <li>Frequence (certains modeles)</li>
</ul>

<p><strong>Precision :</strong></p>
<ul>
  <li>Classe 0.5% a 3% selon gamme et modele</li>
  <li>Attention aux calibres (protection fusibles)</li>
</ul>

<h3>Techniques de montage</h3>

<h4>Breadboard (plaque d'essai)</h4>

<p><strong>Avantages :</strong></p>
<ul>
  <li>Montage rapide sans soudure</li>
  <li>Modifications faciles</li>
  <li>Reutilisable</li>
</ul>

<p><strong>Inconvenients :</strong></p>
<ul>
  <li>Contacts parfois instables</li>
  <li>Capacites parasites (limite HF)</li>
  <li>Pas adapte aux courants eleves</li>
</ul>

<p><strong>Bonnes pratiques :</strong></p>
<ul>
  <li>Alimentations sur les rails lateraux</li>
  <li>Condensateurs de decouplage pres des CIs</li>
  <li>Fils courts et organises</li>
  <li>Code couleur (rouge = +, noir = GND, autres = signaux)</li>
</ul>

<h4>Soudure sur PCB</h4>

<p><strong>Etapes :</strong></p>
<ol>
  <li>Etamage du fer (pointe propre et brillante)</li>
  <li>Placer le composant</li>
  <li>Chauffer simultanement piste et patte (2-3 sec)</li>
  <li>Apporter l'etain (fusion sur zone chaude)</li>
  <li>Retirer etain puis fer</li>
  <li>Laisser refroidir naturellement</li>
</ol>

<p><strong>Soudure reussie :</strong></p>
<ul>
  <li>Forme conique brillante</li>
  <li>Piste et patte bien mouillees</li>
  <li>Pas de boule ou pont</li>
</ul>

<hr/>

<h2>PART D: ANALYSE ET REFLEXION</h2>

<h3>Evaluation des competences</h3>

<h4>Modalites d'evaluation</h4>

<p><strong>Controle continu (35%) :</strong></p>
<ul>
  <li>2 controles ecrits (15% chacun) : Exercices sur composants, AOP, transistors</li>
  <li>QCM (5%) : Theorie, composants, lecture de schemas</li>
</ul>

<p><strong>Travaux pratiques (35%) :</strong></p>
<ul>
  <li>6 TP notes avec comptes-rendus</li>
  <li>Evaluation : Montage, mesures, analyse, documentation</li>
</ul>

<p><strong>Projets (20%) :</strong></p>
<ul>
  <li>Projet Radar : 7%</li>
  <li>Projet Derivateur : 6%</li>
  <li>Semaine Projet Filtrage : 7%</li>
</ul>

<p><strong>Examen terminal (10%) :</strong></p>
<ul>
  <li>Epreuve theorique/pratique (2h)</li>
  <li>Analyse de circuit + dimensionnement</li>
</ul>

<h4>Grille d'evaluation TP</h4>

<table>
  <thead><tr><th>Critere</th><th>Bareme</th></tr></thead>
  <tbody>
    <tr><td><strong>Montage</strong> : Schema realise correctement, cablage propre</td><td>/4</td></tr>
    <tr><td><strong>Mesures</strong> : Utilisation correcte des appareils, releves precis</td><td>/5</td></tr>
    <tr><td><strong>Analyse</strong> : Comparaison theorie/pratique, interpretation</td><td>/5</td></tr>
    <tr><td><strong>Simulation</strong> : Proteus fonctionnel, coherence avec mesures</td><td>/3</td></tr>
    <tr><td><strong>Compte-rendu</strong> : Clarte, rigueur, presentation</td><td>/3</td></tr>
    <tr><td><strong>Total</strong></td><td><strong>/20</strong></td></tr>
  </tbody>
</table>

<h3>Competences acquises</h3>

<h4>Savoirs theoriques</h4>
<ul>
  <li>Connaitre les composants passifs et actifs</li>
  <li>Comprendre les modeles equivalents et limites</li>
  <li>Maitriser les montages a base d'AOP</li>
  <li>Analyser des circuits analogiques</li>
</ul>

<h4>Savoir-faire techniques</h4>
<ul>
  <li>Lire et interpreter un schema electronique</li>
  <li>Simuler un circuit avec Proteus ISIS</li>
  <li>Dimensionner des composants selon un cahier des charges</li>
  <li>Realiser des montages sur breadboard</li>
  <li>Mesurer avec oscilloscope, multimetre, GBF</li>
  <li>Deboguer un circuit (methode systematique)</li>
  <li>Rediger un compte-rendu technique</li>
</ul>

<h4>Savoir-etre</h4>
<ul>
  <li>Rigueur dans les montages et mesures</li>
  <li>Methode face a un dysfonctionnement</li>
  <li>Respect des normes de securite</li>
  <li>Travail en binome</li>
  <li>Autonomie et curiosite technique</li>
</ul>

<h3>Progression et debouches</h3>

<h4>Articulation avec le cursus</h4>

<table>
  <thead><tr><th>Semestre</th><th>Module ER</th><th>Contenu</th></tr></thead>
  <tbody>
    <tr><td><strong>S1</strong></td><td>ER 1</td><td>Composants passifs/actifs, AOP, Proteus</td></tr>
    <tr><td><strong>S2</strong></td><td>ER Microcontroleur</td><td>Programmation Arduino, capteurs/actionneurs</td></tr>
    <tr><td><strong>S2</strong></td><td>ER Interface</td><td>Circuits d'interface (drivers, optocoupleurs)</td></tr>
    <tr><td><strong>S2</strong></td><td>ER FPGA</td><td>Logique programmable (Quartus, VHDL)</td></tr>
    <tr><td><strong>S3-S4</strong></td><td>Systemes Electroniques</td><td>Conception complete de cartes PCB</td></tr>
  </tbody>
</table>

<h4>Metiers et applications</h4>

<p><strong>Metiers utilisant ces competences :</strong></p>
<ul>
  <li>Technicien/Ingenieur en electronique analogique</li>
  <li>Concepteur de cartes electroniques</li>
  <li>Technicien de maintenance electronique</li>
  <li>Testeur/Valideur de systemes electroniques</li>
  <li>Automaticien (interface capteurs/actionneurs)</li>
</ul>

<p><strong>Domaines d'application :</strong></p>
<ul>
  <li>Electronique embarquee (automobile, aeronautique)</li>
  <li>Instrumentation de mesure</li>
  <li>Audio/Video professionnel</li>
  <li>Automatismes industriels</li>
  <li>Dispositifs medicaux</li>
  <li>Objets connectes (IoT)</li>
</ul>

<h3>Conseils de reussite</h3>

<h4>Pendant les cours/TD</h4>
<ul>
  <li>Dessiner les schemas au fur et a mesure</li>
  <li>Comprendre les montages types (a connaitre par coeur)</li>
  <li>Refaire les calculs de dimensionnement chez soi</li>
</ul>

<h4>En TP</h4>
<p><strong>A faire :</strong></p>
<ul>
  <li>Lire le sujet et preparer les calculs avant la seance</li>
  <li>Verifier le montage avant la mise sous tension</li>
  <li>Mesurer methodiquement (DC avant AC)</li>
  <li>Noter immediatement les mesures dans un tableau</li>
  <li>Analyser les ecarts theorie/pratique</li>
  <li>Rediger le CR rapidement apres le TP</li>
</ul>

<p><strong>A eviter :</strong></p>
<ul>
  <li>Brancher sans reflechir</li>
  <li>Alimenter sans verifier les polarites</li>
  <li>Oublier de mettre a la masse</li>
  <li>Toucher les composants sous tension</li>
</ul>

<h4>Pour les projets</h4>
<ul>
  <li>Decomposer en blocs fonctionnels</li>
  <li>Tester chaque bloc independamment</li>
  <li>Simuler avant de realiser</li>
  <li>Documenter au fur et a mesure</li>
  <li>Prevoir du temps pour le debogage</li>
</ul>

<hr/>

<h2>Ressources complementaires</h2>

<h3>Ouvrages de reference</h3>
<ol>
  <li><em>Electronique - Fondements et applications</em> - Jose-Philippe Perez (Dunod) - <strong>LA reference</strong></li>
  <li><em>The Art of Electronics</em> - Horowitz &amp; Hill (Cambridge) - Bible de l'electronique</li>
  <li><em>Electronique analogique</em> - Francois Manneville (Dunod)</li>
  <li><em>Amplificateurs operationnels</em> - Henri Fanet (Dunod)</li>
</ol>

<h3>Datasheets (fiches techniques)</h3>

<p><strong>Ou les trouver :</strong></p>
<ul>
  <li>Sites fabricants (Texas Instruments, Analog Devices, STMicroelectronics)</li>
  <li>Distributeurs (Mouser, Digi-Key, Farnell)</li>
  <li>Google : "[reference composant] datasheet filetype:pdf"</li>
</ul>

<p><strong>Comment les lire :</strong></p>
<ul>
  <li><strong>Absolute Maximum Ratings</strong> : Ne JAMAIS depasser</li>
  <li><strong>Electrical Characteristics</strong> : Parametres typiques et limites</li>
  <li><strong>Application circuits</strong> : Exemples de montages</li>
  <li><strong>Package</strong> : Brochage (pinout)</li>
</ul>

<h3>Ressources en ligne</h3>

<p><strong>Cours et tutoriels :</strong></p>
<ul>
  <li>All About Circuits (allaboutcircuits.com) - Complet et gratuit</li>
  <li>Electronics Tutorials (electronics-tutorials.ws)</li>
  <li>Cours Fabrice Sincere (fabrice.sincere.free.fr)</li>
</ul>

<p><strong>Chaines YouTube :</strong></p>
<ul>
  <li><strong>GreatScott!</strong> : Projets DIY, explications claires</li>
  <li><strong>EEVblog</strong> : Reviews, teardowns, theorie</li>
  <li><strong>ElectroBOOM</strong> : Pedagogie avec humour</li>
  <li><strong>Andreas Spiess</strong> : Projets IoT, microcontroleurs</li>
</ul>

<p><strong>Simulateurs en ligne :</strong></p>
<ul>
  <li><strong>Falstad Circuit Simulator</strong> (falstad.com/circuit) - Tres interactif</li>
  <li><strong>EveryCircuit</strong> (everycircuit.com) - Animations</li>
  <li><strong>CircuitLab</strong> (circuitlab.com) - Complet</li>
</ul>

<hr/>

<h2>Securite et bonnes pratiques</h2>

<h3>Regles de securite</h3>
<ul>
  <li><strong>Ne jamais toucher un circuit sous tension</strong></li>
  <li><strong>Verifier les polarites avant d'alimenter</strong></li>
  <li><strong>Respecter les tensions et courants max des composants</strong></li>
  <li><strong>Eteindre avant de modifier le cablage</strong></li>
  <li><strong>Attention aux condensateurs charges (decharge avant manipulation)</strong></li>
</ul>

<h3>Demarche de debogage systematique</h3>

<p><strong>Circuit qui ne fonctionne pas :</strong></p>
<ol>
  <li>Verifier l'alimentation (tensions presentes ?)</li>
  <li>Verifier les masses (continuite)</li>
  <li>Controler le cablage (schema vs realisation)</li>
  <li>Tester les composants individuellement</li>
  <li>Verifier les polarites (diodes, condensateurs electrolytiques, CIs)</li>
  <li>Mesurer point par point (de l'entree vers la sortie)</li>
</ol>

<p><strong>Composant qui chauffe :</strong></p>
<ul>
  <li>ETEINDRE IMMEDIATEMENT</li>
  <li>Verifier polarite et branchement</li>
  <li>Verifier l'absence de court-circuit</li>
  <li>Remplacer le composant (probablement grille)</li>
</ul>

<hr/>

<p><strong>Bon courage dans votre decouverte de l'electronique !</strong></p>

<blockquote><p>"In theory, there is no difference between theory and practice. In practice, there is." - Yogi Berra</p></blockquote>

<p>L'electronique est un domaine pratique. Experimentez, testez, cassez (un peu), reparez, et surtout : amusez-vous !</p>

</div>

<div class="lang-en">

<h1>Electronics and Implementation (ER) - Semester 1</h1>

<h2>PART A - General Course Overview</h2>

<h3>Training Context</h3>
<p>The Electronics and Implementation (ER) module is the practical core of the GEII program. It combines electronic theory and hands-on circuit building, allowing students to understand the operation of electronic components and put them to work in real projects. The intensive use of Proteus ISIS software prepares students for computer-aided design used in industry.</p>

<h3>Position in the Curriculum</h3>
<ul>
  <li><strong>Semester</strong>: S1 (1st year DUT GEII)</li>
  <li><strong>Course hours</strong>: 70h (30h lectures + 20h tutorials + 20h lab sessions + Projects)</li>
  <li><strong>ECTS credits</strong>: 6</li>
  <li><strong>Prerequisites</strong>: Basics in electricity (high school level), mathematics (complex numbers)</li>
  <li><strong>Continuation</strong>: ER S2 (Microcontrollers, Interface, FPGA), then Electronic Systems S3-S4</li>
</ul>

<h3>Target Audience</h3>
<p>First-year students discovering analog electronics with a practical, project-oriented approach. The course is aimed at both beginners and those who followed a science track in high school.</p>

<hr/>

<h2>PART B: EXPERIENCE, CONTEXT AND FUNCTION</h2>

<h3>Learning Objectives</h3>

<p><strong>Electronic component skills:</strong></p>
<ul>
  <li>Identify and characterize passive (R, L, C) and active (diodes, transistors, op-amps) components</li>
  <li>Understand physical operation and equivalent models</li>
  <li>Choose components according to specification requirements</li>
  <li>Read and interpret a datasheet</li>
</ul>

<p><strong>Design skills:</strong></p>
<ul>
  <li>Design simple analog circuits</li>
  <li>Simulate and validate a circuit before building</li>
  <li>Size components</li>
  <li>Optimize a circuit according to constraints</li>
</ul>

<p><strong>Practical skills:</strong></p>
<ul>
  <li>Use Proteus ISIS for simulation</li>
  <li>Build circuits on breadboard</li>
  <li>Measure and validate experimentally</li>
  <li>Debug and troubleshoot circuits</li>
</ul>

<h3>Detailed Syllabus</h3>

<h4>1. Passive Components (10h)</h4>

<p><strong>Resistors (R):</strong></p>

<p><strong>Characteristics:</strong></p>
<ul>
  <li>Ohm's Law: V = R x I</li>
  <li>Dissipated power: P = R x I&sup2; = V&sup2;/R</li>
  <li>Technology: carbon film, metal film, wirewound</li>
  <li>Color code (4 or 5 bands)</li>
  <li>Standard values (E12, E24 series)</li>
</ul>

<p><strong>Combinations:</strong></p>
<ul>
  <li>Series: R_eq = R1 + R2 + ... + Rn</li>
  <li>Parallel: 1/R_eq = 1/R1 + 1/R2 + ... + 1/Rn</li>
  <li>Voltage divider: V_out = V_in x R2/(R1+R2)</li>
</ul>

<p><strong>Capacitors (C):</strong></p>

<p><strong>Physical principle:</strong></p>
<ul>
  <li>Electrical energy storage (electric field)</li>
  <li>Relationship: Q = C x V</li>
  <li>Current: I = C x dV/dt</li>
  <li>Complex impedance: Z_C = 1/(jCw) = -j/(Cw)</li>
</ul>

<p><strong>Technologies:</strong></p>
<ul>
  <li><strong>Electrolytic</strong>: High capacitance (uF to mF), polarized, high ESR</li>
  <li><strong>Ceramic</strong>: Medium values (pF to uF), non-polarized, fast</li>
  <li><strong>Film</strong>: Precision, stability, audio</li>
</ul>

<p><strong>Applications:</strong></p>
<ul>
  <li>Power supply filtering (decoupling)</li>
  <li>AC coupling/decoupling</li>
  <li>RC filters (low-pass, high-pass)</li>
  <li>Timing</li>
  <li>Energy storage</li>
</ul>

<p><strong>Charge/discharge:</strong></p>
<ul>
  <li>Charge: V_C(t) = V_max x (1 - e^(-t/tau)) with tau = RC</li>
  <li>Discharge: V_C(t) = V_max x e^(-t/tau)</li>
</ul>

<p><strong>Inductors (L):</strong></p>

<p><strong>Physical principle:</strong></p>
<ul>
  <li>Magnetic energy storage</li>
  <li>Voltage: V = L x dI/dt</li>
  <li>Complex impedance: Z_L = jLw</li>
</ul>

<p><strong>Applications:</strong></p>
<ul>
  <li>Filtering (choke coils)</li>
  <li>Transformers</li>
  <li>Motors and relays</li>
  <li>LC filters</li>
</ul>

<p><strong>Complex impedances (summary):</strong></p>
<p>In sinusoidal (AC) regime, using complex notation:</p>
<ul>
  <li>Resistance: Z_R = R (in phase)</li>
  <li>Inductance: Z_L = jLw (current lags by 90 deg)</li>
  <li>Capacitor: Z_C = -j/(Cw) (current leads by 90 deg)</li>
</ul>

<h4>2. Diodes and Applications (12h)</h4>

<p><strong>PN junction diode:</strong></p>

<p><strong>Operating principle:</strong></p>
<ul>
  <li>P-N semiconductor junction (Si or Ge)</li>
  <li>Unidirectional conduction</li>
  <li>Forward bias: I = I_s x (e^(V/nV_T) - 1)</li>
  <li>Reverse bias: blocking (negligible leakage current)</li>
</ul>

<p><strong>Characteristics:</strong></p>
<ul>
  <li>Threshold voltage: V_F &asymp; 0.7V (Si), 0.3V (Ge), 0.2V (Schottky)</li>
  <li>Maximum current (I_F max)</li>
  <li>Maximum reverse voltage (V_R max or PIV)</li>
  <li>Switching time (fast diodes)</li>
</ul>

<p><strong>Equivalent models:</strong></p>
<ul>
  <li><strong>Ideal model</strong>: Perfect switch (V_F = 0)</li>
  <li><strong>Simplified model</strong>: Voltage source V_F + resistance r_d</li>
  <li><strong>Complete model</strong>: Exponential (Shockley equation)</li>
</ul>

<p><strong>Practical applications:</strong></p>

<p><strong>1. Rectification:</strong></p>
<ul>
  <li><strong>Half-wave rectifier</strong>: AC &rarr; pulsed DC conversion</li>
  <li><strong>Full-wave rectifier (Graetz bridge)</strong>: 4 diodes, better efficiency</li>
  <li>Capacitor filtering: V_ripple &asymp; I_load / (f x C)</li>
</ul>

<p><strong>2. Clipping:</strong></p>
<ul>
  <li>Signal amplitude limitation</li>
  <li>Overvoltage protection</li>
  <li>Signal shaping</li>
</ul>

<p><strong>3. Freewheeling:</strong></p>
<ul>
  <li>Protection against inductive overvoltages</li>
  <li>Circuits with relays, motors, solenoid valves</li>
</ul>

<p><strong>4. Special diodes:</strong></p>
<ul>
  <li><strong>Zener diode</strong>: Voltage regulation (controlled breakdown voltage)</li>
  <li><strong>LED</strong>: Light emission (V_F &asymp; 1.8V to 3.3V depending on color)</li>
  <li><strong>Schottky diode</strong>: Low voltage drop, fast (switching power supplies)</li>
  <li><strong>Photodiode</strong>: Light &rarr; current conversion</li>
</ul>

<h4>3. Bipolar Junction Transistors (BJT) (15h)</h4>

<p><strong>Structure and operation:</strong></p>

<p><strong>Types:</strong></p>
<ul>
  <li><strong>NPN</strong>: Collector (+), Base (control), Emitter (reference)</li>
  <li><strong>PNP</strong>: Collector (-), Base (control), Emitter (reference)</li>
</ul>

<p><strong>Principle:</strong></p>
<ul>
  <li>3 regions: Emitter (E), Base (B), Collector (C)</li>
  <li>I_C current controlled by I_B current</li>
  <li>Current gain: beta = I_C / I_B (typically 100-300)</li>
</ul>

<p><strong>Operating modes:</strong></p>
<ul>
  <li><strong>Cut-off</strong>: V_BE &lt; V_threshold, transistor open (I_C &asymp; 0)</li>
  <li><strong>Active (linear)</strong>: V_BE &ge; 0.7V, I_C = beta x I_B, amplification</li>
  <li><strong>Saturated</strong>: V_BE &ge; 0.7V, I_C limited by load, closed switch</li>
</ul>

<p><strong>Applications:</strong></p>

<p><strong>1. Electronic switch:</strong></p>
<pre><code>        +Vcc
         |
        [R_C]  (load)
         |
     C--+--
      NPN
      ---
       |
   [R_B]
       |
    Signal</code></pre>

<p>Sizing:</p>
<ul>
  <li>I_B = (V_in - V_BE) / R_B</li>
  <li>I_C (saturated) = (V_cc - V_CE(sat)) / R_C</li>
  <li>Verify: beta x I_B &gt; I_C (saturation ensured)</li>
</ul>

<p><strong>2. Small signal amplifier:</strong></p>
<ul>
  <li>Common emitter configuration</li>
  <li>Voltage gain: A_v &asymp; -R_C / R_E</li>
  <li>Base bias network</li>
</ul>

<p><strong>3. Relay/LED/motor driver:</strong></p>
<ul>
  <li>Transistor in switching mode</li>
  <li>Freewheeling diode protection</li>
</ul>

<h4>4. Operational Amplifiers (Op-Amps) (20h)</h4>

<p><strong>Ideal op-amp characteristics:</strong></p>
<ul>
  <li>Infinite voltage gain: A_v &rarr; &infin;</li>
  <li>Infinite input impedance: Z_in &rarr; &infin;</li>
  <li>Zero output impedance: Z_out = 0</li>
  <li>Infinite bandwidth</li>
  <li>No input current: I+ = I- = 0</li>
  <li><strong>Golden rule</strong>: In closed loop, V+ = V-</li>
</ul>

<p><strong>Fundamental configurations:</strong></p>

<p><strong>1. Voltage follower (Buffer):</strong></p>
<ul>
  <li>Gain: A_v = 1</li>
  <li>Very high input impedance</li>
  <li>Impedance matching</li>
</ul>

<p><strong>2. Inverting amplifier:</strong></p>
<pre><code>    R2
   +---+
   |   |
R1 |   v
---+-  |
   |+  +--- V_out
---+   |
   +---+</code></pre>
<ul>
  <li>Gain: A_v = -R2/R1</li>
  <li>Z_in = R1</li>
</ul>

<p><strong>3. Non-inverting amplifier:</strong></p>
<ul>
  <li>Gain: A_v = 1 + R2/R1</li>
  <li>Very high Z_in</li>
</ul>

<p><strong>4. Inverting summing amplifier:</strong></p>
<ul>
  <li>V_out = -(R_f/R1 x V1 + R_f/R2 x V2 + ...)</li>
  <li>Audio mixer, DAC</li>
</ul>

<p><strong>5. Integrator:</strong></p>
<ul>
  <li>V_out = -(1/RC) &int; V_in dt</li>
  <li>Ramp generation, filters</li>
</ul>

<p><strong>6. Differentiator:</strong></p>
<ul>
  <li>V_out = -RC x dV_in/dt</li>
  <li>Edge detection</li>
</ul>

<p><strong>7. Comparator:</strong></p>
<ul>
  <li>V_out = +V_sat if V+ &gt; V-, otherwise -V_sat</li>
  <li>Threshold detection</li>
</ul>

<p><strong>8. Schmitt Trigger:</strong></p>
<ul>
  <li>Comparator with hysteresis</li>
  <li>Debouncing, signal shaping</li>
</ul>

<p><strong>Real op-amps used:</strong></p>
<ul>
  <li>TL081/TL084: JFET, low input current</li>
  <li>LM741: Classic, universal</li>
  <li>LM358: Dual, single supply</li>
  <li>OPA27: Low noise, precision</li>
</ul>

<h3>Practical Projects</h3>

<h4>Radar Project 2020</h4>

<p><strong>Objective:</strong> Design an ultrasonic distance detection and measurement system</p>

<p><strong>Specifications:</strong></p>
<ul>
  <li>Ultrasonic pulse emission (40 kHz)</li>
  <li>Echo signal reception and amplification</li>
  <li>Time-of-flight measurement</li>
  <li>Distance calculation and display</li>
</ul>

<p><strong>Functional blocks:</strong></p>
<ol>
  <li><strong>Ultrasonic transmitter</strong>: 40 kHz oscillator + transducer</li>
  <li><strong>Receiver</strong>: Transducer + amplification (op-amp)</li>
  <li><strong>Signal processing</strong>: Envelope detection, comparator</li>
  <li><strong>Measurement logic</strong>: Microcontroller or digital circuit</li>
  <li><strong>Display</strong>: LCD or LEDs</li>
</ol>

<p><strong>Skills developed:</strong></p>
<ul>
  <li>Analog circuit design</li>
  <li>Weak signal amplification</li>
  <li>Analog/digital interface</li>
  <li>Time measurement and distance calculation</li>
</ul>

<h4>Frequency Differentiator</h4>

<p><strong>Objective:</strong> Build a circuit whose output is proportional to the derivative of the input signal</p>

<p><strong>Principle:</strong></p>
<ul>
  <li>Op-amp-based differentiator circuit: V_out = -RC x dV_in/dt</li>
  <li>Frequency response study</li>
  <li>Compensation and stabilization</li>
</ul>

<p><strong>Analysis:</strong></p>
<ul>
  <li>Transfer function: H(jw) = -jRCw</li>
  <li>Gain: |H| = RCw (linear increase with f)</li>
  <li>Phase: phi = +90 deg (phase lead)</li>
</ul>

<p><strong>Applications:</strong></p>
<ul>
  <li>Edge detection</li>
  <li>Speed calculation (position derivative)</li>
  <li>Active filters</li>
</ul>

<h4>Project Week - Sound Filtering</h4>

<p><strong>Objective:</strong> Design a complete active filtering system to isolate frequency components of an audio signal</p>

<p><strong>Specifications:</strong></p>
<ul>
  <li>Input: Audio signal (microphone or line-in)</li>
  <li>Filters: Low-pass, band-pass, high-pass</li>
  <li>Adjustable cutoff frequencies</li>
  <li>Output: Speaker or line-out</li>
</ul>

<p><strong>Implementation:</strong></p>
<ol>
  <li><strong>Analysis</strong>: Signal frequency decomposition</li>
  <li><strong>Design</strong>: Topology selection (Butterworth, Sallen-Key)</li>
  <li><strong>Simulation</strong>: Proteus ISIS, frequency analysis</li>
  <li><strong>Sizing</strong>: Component calculation</li>
  <li><strong>Building</strong>: Breadboard assembly then PCB</li>
  <li><strong>Testing</strong>: Oscilloscope and spectrum analyzer measurements</li>
  <li><strong>Documentation</strong>: Complete technical report</li>
</ol>

<p><strong>Deliverables:</strong></p>
<ul>
  <li>Electronic schematics</li>
  <li>Simulations (Bode diagrams)</li>
  <li>Working prototype</li>
  <li>Measurements and validation</li>
  <li>Technical report</li>
</ul>

<hr/>

<h2>PART C: TECHNICAL ASPECTS</h2>

<h3>Simulation Software</h3>

<h4>Proteus ISIS (Labcenter Electronics)</h4>

<p><strong>Features:</strong></p>
<ul>
  <li>Electronic schematic capture</li>
  <li>Comprehensive component library</li>
  <li>SPICE simulation (analog, digital, mixed)</li>
  <li>Virtual instruments (oscilloscope, multimeter, function generator)</li>
  <li>Time and frequency domain simulation</li>
  <li>DC, AC, transient analysis</li>
</ul>

<p><strong>Design workflow:</strong></p>

<p><strong>1. Schematic creation:</strong></p>
<ul>
  <li>Place components (P)</li>
  <li>Wire (W for wire)</li>
  <li>Name nodes (L for label)</li>
  <li>Set component values</li>
</ul>

<p><strong>2. Virtual instruments:</strong></p>
<ul>
  <li>Oscilloscope: Time domain visualization</li>
  <li>Voltmeter/Ammeter: DC/AC measurements</li>
  <li>Function generator: Excitation signals</li>
  <li>Spectrum analyzer: Frequency content</li>
</ul>

<p><strong>3. Simulation:</strong></p>
<ul>
  <li><strong>Transient Analysis</strong>: Time domain evolution</li>
  <li><strong>AC Sweep</strong>: Frequency response (Bode)</li>
  <li><strong>DC Sweep</strong>: Static characteristic</li>
</ul>

<p><strong>4. Results processing:</strong></p>
<ul>
  <li>Curve plotting</li>
  <li>Measurements (amplitude, phase, frequency)</li>
  <li>Export to report</li>
</ul>

<p><strong>Example: RC low-pass filter simulation</strong></p>
<pre><code>1. Schematic: Function gen &rarr; R &rarr; C &rarr; GND
2. Generator parameters: Sine, 5V amplitude, sweep 1Hz-100kHz
3. Oscilloscope: Input (generator) and output (RC node)
4. AC Analysis: Plot |H(f)| and Phase(f)
5. Measure f_c at -3dB: f_c = 1/(2piRC)</code></pre>

<p><strong>Practical tips:</strong></p>
<ul>
  <li>Explicitly name important nodes</li>
  <li>Use common grounds</li>
  <li>Check component models (sometimes idealized)</li>
  <li>Save regularly</li>
  <li>Document with annotations on the schematic</li>
</ul>

<h4>Alternatives and Complements</h4>

<p><strong>LTspice (Analog Devices):</strong></p>
<ul>
  <li>Free, very powerful</li>
  <li>Pure SPICE simulation</li>
  <li>ADI component library</li>
  <li>SPICE export from Proteus possible</li>
</ul>

<p><strong>Tinkercad Circuits:</strong></p>
<ul>
  <li>Free online simulation</li>
  <li>Simple and intuitive interface</li>
  <li>Ideal for learning</li>
  <li>Limitation: Fewer components</li>
</ul>

<h3>Laboratory Equipment</h3>

<h4>Digital Oscilloscope</h4>

<p><strong>Main functions:</strong></p>
<ul>
  <li><strong>Acquisition</strong>: Signal sampling (MHz to GHz)</li>
  <li><strong>Display</strong>: Time domain visualization</li>
  <li><strong>Automatic measurements</strong>: V_pp, V_rms, f, period, duty cycle</li>
  <li><strong>Triggering</strong>: Edge, pulse, video</li>
  <li><strong>Cursors</strong>: Precise measurements</li>
  <li><strong>Math</strong>: Operations (A+B, A-B, FFT)</li>
</ul>

<p><strong>Typical use:</strong></p>
<ul>
  <li>Time base (s/div) and sensitivity (V/div) adjustment</li>
  <li>Signal triggering</li>
  <li>AC/DC mode depending on application</li>
  <li>Phase shift measurement between 2 signals (XY mode or time measurement)</li>
</ul>

<h4>Function Generator</h4>

<p><strong>Generated signals:</strong></p>
<ul>
  <li><strong>Sinusoidal</strong>: Frequency testing, audio</li>
  <li><strong>Square</strong>: Logic signals, PWM</li>
  <li><strong>Triangle/Ramp</strong>: Sweep, integration</li>
  <li><strong>Pulse</strong>: Transient tests</li>
  <li><strong>Noise</strong>: Robustness tests</li>
</ul>

<p><strong>Adjustable parameters:</strong></p>
<ul>
  <li>Frequency: mHz to MHz</li>
  <li>Amplitude: mV to V</li>
  <li>DC offset: Vertical shift</li>
  <li>Duty cycle: For square waves</li>
  <li>Sweep: Frequency sweep</li>
</ul>

<h4>Digital Multimeter</h4>

<p><strong>Measurements:</strong></p>
<ul>
  <li>DC/AC Voltage (V)</li>
  <li>DC/AC Current (A)</li>
  <li>Resistance (Ohm)</li>
  <li>Continuity (beeper)</li>
  <li>Diode test (V_F)</li>
  <li>Capacitance (some models)</li>
  <li>Frequency (some models)</li>
</ul>

<p><strong>Accuracy:</strong></p>
<ul>
  <li>0.5% to 3% class depending on range and model</li>
  <li>Mind the ranges (fuse protection)</li>
</ul>

<h3>Assembly Techniques</h3>

<h4>Breadboard</h4>

<p><strong>Advantages:</strong></p>
<ul>
  <li>Quick solderless assembly</li>
  <li>Easy modifications</li>
  <li>Reusable</li>
</ul>

<p><strong>Disadvantages:</strong></p>
<ul>
  <li>Sometimes unstable contacts</li>
  <li>Parasitic capacitance (HF limitation)</li>
  <li>Not suitable for high currents</li>
</ul>

<p><strong>Best practices:</strong></p>
<ul>
  <li>Power supplies on side rails</li>
  <li>Decoupling capacitors near ICs</li>
  <li>Short and organized wires</li>
  <li>Color code (red = +, black = GND, others = signals)</li>
</ul>

<h4>PCB Soldering</h4>

<p><strong>Steps:</strong></p>
<ol>
  <li>Tin the iron (clean and shiny tip)</li>
  <li>Place the component</li>
  <li>Heat both pad and lead simultaneously (2-3 sec)</li>
  <li>Apply solder (melts on heated area)</li>
  <li>Remove solder then iron</li>
  <li>Let cool naturally</li>
</ol>

<p><strong>Good solder joint:</strong></p>
<ul>
  <li>Shiny cone shape</li>
  <li>Pad and lead well wetted</li>
  <li>No balls or bridges</li>
</ul>

<hr/>

<h2>PART D: ANALYSIS AND REFLECTION</h2>

<h3>Skills Assessment</h3>

<h4>Assessment Methods</h4>

<p><strong>Continuous assessment (35%):</strong></p>
<ul>
  <li>2 written tests (15% each): Exercises on components, op-amps, transistors</li>
  <li>Quiz (5%): Theory, components, schematic reading</li>
</ul>

<p><strong>Lab work (35%):</strong></p>
<ul>
  <li>6 graded labs with reports</li>
  <li>Assessment: Assembly, measurements, analysis, documentation</li>
</ul>

<p><strong>Projects (20%):</strong></p>
<ul>
  <li>Radar Project: 7%</li>
  <li>Differentiator Project: 6%</li>
  <li>Filtering Project Week: 7%</li>
</ul>

<p><strong>Final exam (10%):</strong></p>
<ul>
  <li>Theoretical/practical exam (2h)</li>
  <li>Circuit analysis + component sizing</li>
</ul>

<h4>Lab Grading Rubric</h4>

<table>
  <thead><tr><th>Criterion</th><th>Points</th></tr></thead>
  <tbody>
    <tr><td><strong>Assembly</strong>: Schematic correctly built, clean wiring</td><td>/4</td></tr>
    <tr><td><strong>Measurements</strong>: Correct use of instruments, accurate readings</td><td>/5</td></tr>
    <tr><td><strong>Analysis</strong>: Theory/practice comparison, interpretation</td><td>/5</td></tr>
    <tr><td><strong>Simulation</strong>: Working Proteus, consistency with measurements</td><td>/3</td></tr>
    <tr><td><strong>Report</strong>: Clarity, rigor, presentation</td><td>/3</td></tr>
    <tr><td><strong>Total</strong></td><td><strong>/20</strong></td></tr>
  </tbody>
</table>

<h3>Skills Acquired</h3>

<h4>Theoretical Knowledge</h4>
<ul>
  <li>Know passive and active components</li>
  <li>Understand equivalent models and limitations</li>
  <li>Master op-amp-based circuits</li>
  <li>Analyze analog circuits</li>
</ul>

<h4>Technical Know-How</h4>
<ul>
  <li>Read and interpret an electronic schematic</li>
  <li>Simulate a circuit with Proteus ISIS</li>
  <li>Size components according to specifications</li>
  <li>Build circuits on breadboard</li>
  <li>Measure with oscilloscope, multimeter, function generator</li>
  <li>Debug a circuit (systematic method)</li>
  <li>Write a technical report</li>
</ul>

<h4>Soft Skills</h4>
<ul>
  <li>Rigor in assembly and measurements</li>
  <li>Systematic approach to troubleshooting</li>
  <li>Compliance with safety standards</li>
  <li>Teamwork in pairs</li>
  <li>Autonomy and technical curiosity</li>
</ul>

<h3>Progression and Career Prospects</h3>

<h4>Curriculum Integration</h4>

<table>
  <thead><tr><th>Semester</th><th>ER Module</th><th>Content</th></tr></thead>
  <tbody>
    <tr><td><strong>S1</strong></td><td>ER 1</td><td>Passive/active components, op-amps, Proteus</td></tr>
    <tr><td><strong>S2</strong></td><td>ER Microcontroller</td><td>Arduino programming, sensors/actuators</td></tr>
    <tr><td><strong>S2</strong></td><td>ER Interface</td><td>Interface circuits (drivers, optocouplers)</td></tr>
    <tr><td><strong>S2</strong></td><td>ER FPGA</td><td>Programmable logic (Quartus, VHDL)</td></tr>
    <tr><td><strong>S3-S4</strong></td><td>Electronic Systems</td><td>Complete PCB board design</td></tr>
  </tbody>
</table>

<h4>Careers and Applications</h4>

<p><strong>Careers using these skills:</strong></p>
<ul>
  <li>Analog electronics technician/engineer</li>
  <li>Electronic board designer</li>
  <li>Electronics maintenance technician</li>
  <li>Electronic systems tester/validator</li>
  <li>Automation engineer (sensor/actuator interface)</li>
</ul>

<p><strong>Application areas:</strong></p>
<ul>
  <li>Embedded electronics (automotive, aerospace)</li>
  <li>Measurement instrumentation</li>
  <li>Professional audio/video</li>
  <li>Industrial automation</li>
  <li>Medical devices</li>
  <li>Connected objects (IoT)</li>
</ul>

<h3>Tips for Success</h3>

<h4>During Lectures/Tutorials</h4>
<ul>
  <li>Draw schematics as you go</li>
  <li>Understand standard configurations (learn by heart)</li>
  <li>Redo component sizing calculations at home</li>
</ul>

<h4>In Lab Sessions</h4>
<p><strong>Do:</strong></p>
<ul>
  <li>Read the assignment and prepare calculations before the session</li>
  <li>Check the assembly before powering on</li>
  <li>Measure methodically (DC before AC)</li>
  <li>Immediately record measurements in a table</li>
  <li>Analyze theory/practice discrepancies</li>
  <li>Write the report promptly after the lab</li>
</ul>

<p><strong>Avoid:</strong></p>
<ul>
  <li>Connecting without thinking</li>
  <li>Powering on without checking polarities</li>
  <li>Forgetting to ground</li>
  <li>Touching components under voltage</li>
</ul>

<h4>For Projects</h4>
<ul>
  <li>Break down into functional blocks</li>
  <li>Test each block independently</li>
  <li>Simulate before building</li>
  <li>Document as you go</li>
  <li>Allow time for debugging</li>
</ul>

<hr/>

<h2>Additional Resources</h2>

<h3>Reference Books</h3>
<ol>
  <li><em>Electronique - Fondements et applications</em> - Jose-Philippe Perez (Dunod) - <strong>THE reference</strong></li>
  <li><em>The Art of Electronics</em> - Horowitz &amp; Hill (Cambridge) - The electronics bible</li>
  <li><em>Electronique analogique</em> - Francois Manneville (Dunod)</li>
  <li><em>Amplificateurs operationnels</em> - Henri Fanet (Dunod)</li>
</ol>

<h3>Datasheets</h3>

<p><strong>Where to find them:</strong></p>
<ul>
  <li>Manufacturer websites (Texas Instruments, Analog Devices, STMicroelectronics)</li>
  <li>Distributors (Mouser, Digi-Key, Farnell)</li>
  <li>Google: "[component reference] datasheet filetype:pdf"</li>
</ul>

<p><strong>How to read them:</strong></p>
<ul>
  <li><strong>Absolute Maximum Ratings</strong>: NEVER exceed</li>
  <li><strong>Electrical Characteristics</strong>: Typical and limit parameters</li>
  <li><strong>Application circuits</strong>: Circuit examples</li>
  <li><strong>Package</strong>: Pin assignment (pinout)</li>
</ul>

<h3>Online Resources</h3>

<p><strong>Courses and tutorials:</strong></p>
<ul>
  <li>All About Circuits (allaboutcircuits.com) - Comprehensive and free</li>
  <li>Electronics Tutorials (electronics-tutorials.ws)</li>
  <li>Cours Fabrice Sincere (fabrice.sincere.free.fr)</li>
</ul>

<p><strong>YouTube channels:</strong></p>
<ul>
  <li><strong>GreatScott!</strong>: DIY projects, clear explanations</li>
  <li><strong>EEVblog</strong>: Reviews, teardowns, theory</li>
  <li><strong>ElectroBOOM</strong>: Educational with humor</li>
  <li><strong>Andreas Spiess</strong>: IoT projects, microcontrollers</li>
</ul>

<p><strong>Online simulators:</strong></p>
<ul>
  <li><strong>Falstad Circuit Simulator</strong> (falstad.com/circuit) - Very interactive</li>
  <li><strong>EveryCircuit</strong> (everycircuit.com) - Animations</li>
  <li><strong>CircuitLab</strong> (circuitlab.com) - Comprehensive</li>
</ul>

<hr/>

<h2>Safety and Best Practices</h2>

<h3>Safety Rules</h3>
<ul>
  <li><strong>Never touch a powered circuit</strong></li>
  <li><strong>Check polarities before powering on</strong></li>
  <li><strong>Respect maximum component voltages and currents</strong></li>
  <li><strong>Turn off before modifying wiring</strong></li>
  <li><strong>Beware of charged capacitors (discharge before handling)</strong></li>
</ul>

<h3>Systematic Debugging Approach</h3>

<p><strong>Circuit not working:</strong></p>
<ol>
  <li>Check the power supply (voltages present?)</li>
  <li>Check grounds (continuity)</li>
  <li>Verify wiring (schematic vs. actual build)</li>
  <li>Test components individually</li>
  <li>Check polarities (diodes, electrolytic capacitors, ICs)</li>
  <li>Measure point by point (from input to output)</li>
</ol>

<p><strong>Component overheating:</strong></p>
<ul>
  <li>TURN OFF IMMEDIATELY</li>
  <li>Check polarity and connections</li>
  <li>Check for short circuits</li>
  <li>Replace the component (probably burned out)</li>
</ul>

<hr/>

<p><strong>Good luck discovering electronics!</strong></p>

<blockquote><p>"In theory, there is no difference between theory and practice. In practice, there is." - Yogi Berra</p></blockquote>

<p>Electronics is a hands-on field. Experiment, test, break things (a little), fix them, and most importantly: have fun!</p>

</div>

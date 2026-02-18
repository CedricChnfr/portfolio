---
layout: default
title: "Étude et Modélisation des Composants Actifs - S7"
date: 2024-10-02 10:56:03 +0200
---

<style>
.back-nav {
    background: #f4f4f4;
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 20px;
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

.code-block {
    background: #f4f4f4;
    border-left: 4px solid #2a7ae2;
    padding: 15px;
    margin: 15px 0;
    font-family: 'Courier New', monospace;
}

.pdf-container {
    margin: 40px 0;
    padding: 20px;
    background: #f9f9f9;
    border-radius: 8px;
}
.pdf-viewer {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}
.pdf-item {
    flex: 1;
    min-width: 400px;
    background: white;
    padding: 15px;
    border-radius: 5px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
.pdf-item h4 {
    color: #2a7ae2;
    margin-top: 0;
}
</style>

<div class="back-nav">
    <a href="./my-courses-2023-2024.html" data-i18n-html="back_courses_2023_2024">&#8592; Back to My Courses 2023-2024</a>
</div>

<div class="lang-fr">

<h1>Etude et Modelisation des Composants Actifs - Semestre 7</h1>

<p><strong>Annee Universitaire</strong> : 2023-2024<br/>
<strong>Semestre</strong> : 7<br/>
<strong>Credits</strong> : 2.5 ECTS<br/>
<strong>Specialite</strong> : Electronique Analogique</p>

<hr/>

<h2>PART A - Presentation Generale du Module</h2>

<h3 class="section-title">Vue d'ensemble</h3>

<p>Ce cours approfondit l'etude des composants electroniques actifs (transistors bipolaires, MOSFETs, amplificateurs operationnels) en analysant leur physique interne, leurs modeles mathematiques et leur comportement en regime statique et dynamique. Il permet de passer d'une utilisation superficielle des composants a une comprehension fine de leurs performances et limitations.</p>

<p><strong>Objectifs pedagogiques</strong> :</p>
<ul>
  <li>Comprendre la physique des semi-conducteurs et des jonctions</li>
  <li>Maitriser les modeles des transistors bipolaires (BJT) et MOS</li>
  <li>Analyser les regimes de fonctionnement (lineaire, saturation, blocage)</li>
  <li>Caracteriser experimentalement les composants actifs</li>
  <li>Utiliser des simulateurs SPICE avec modeles avances</li>
  <li>Concevoir des circuits de polarisation et d'amplification</li>
</ul>

<h3 class="section-title">Position dans le cursus</h3>

<p>Ce module s'appuie sur :</p>
<ul>
  <li><strong>Fondements electronique numerique (S5)</strong> : jonctions PN, transistors en commutation</li>
  <li><strong>Circuits et Filtres analogiques (S5)</strong> : amplification, quadripoles</li>
  <li><strong>Composants et notions de puissance (S5)</strong> : caracteristiques des composants</li>
</ul>

<p>Il prepare a :</p>
<ul>
  <li><strong>Architectures analogiques systemes embarques (S7)</strong> : OTA, circuits integres</li>
  <li><strong>Filtrage actif et modelisation sources bruit (S7)</strong> : amplificateurs operationnels</li>
  <li><strong>Chaines electroniques acquisition (S8)</strong> : conditionnement de signaux</li>
  <li><strong>Conception de circuits integres analogiques</strong> : design CMOS</li>
</ul>

<hr/>

<h2>PART B - Experience Personnelle et Contexte d'Apprentissage</h2>

<h3 class="section-title">Organisation et ressources</h3>

<p>Le module etait structure en cours magistraux et travaux diriges avec manipulations :</p>

<p><strong>Cours magistraux (18h)</strong> :</p>
<p>Divises en 5 parties thematiques (Slides_EMCA_2020-2021_1 a 5) :</p>
<ul>
  <li>Partie 1 : Physique des semi-conducteurs, jonction PN</li>
  <li>Partie 2 : Transistor bipolaire (BJT) - modeles et regimes</li>
  <li>Partie 3 : Transistor MOS - structure et fonctionnement</li>
  <li>Partie 4 : Modeles petit signal et applications</li>
  <li>Partie 5 : Amplificateurs differentiels et miroirs de courant</li>
</ul>

<p><strong>Travaux diriges (12h)</strong> :</p>
<ul>
  <li>TD1 et TD2 : Transistor bipolaire (polarisation, amplification)</li>
  <li>TD3 : Introduction au transistor MOS</li>
  <li>TD4 et TD5 : Applications MOS avancees</li>
  <li>Corrections disponibles pour tous les TD</li>
</ul>

<p><strong>Evaluations</strong> :</p>
<ul>
  <li>Controle continu (CC) en cours de semestre</li>
  <li>Examen final (annales disponibles 2015-2023)</li>
  <li>TP de caracterisation avec compte-rendu</li>
</ul>

<p><strong>Outils utilises</strong> :</p>
<ul>
  <li>SPICE (simulation circuits avec modeles Gummel-Poon, BSIM)</li>
  <li>Oscilloscope et generateur de fonctions</li>
  <li>Traceur de caracteristiques (courbes I-V)</li>
  <li>Multimetres de precision</li>
</ul>

<h3 class="section-title">Methodologie d'etude</h3>

<p><strong>Phase 1 : Comprehension physique</strong> :</p>
<p>Etudier la structure interne du composant (jonctions, dopage, canaux) pour comprendre d'ou viennent les equations.</p>

<p><strong>Phase 2 : Modelisation mathematique</strong> :</p>
<p>Maitriser les equations dans les differents regimes (blocage, actif, saturation pour BJT ; bloque, lineaire, saturation pour MOS).</p>

<p><strong>Phase 3 : Analyse graphique</strong> :</p>
<p>Tracer et interpreter les caracteristiques statiques (IC vs VCE, ID vs VDS) pour visualiser les regimes.</p>

<p><strong>Phase 4 : Petit signal</strong> :</p>
<p>Lineariser autour du point de fonctionnement et utiliser les modeles equivalents petit signal pour calculer gains et impedances.</p>

<p><strong>Phase 5 : Simulation</strong> :</p>
<p>Valider les calculs analytiques avec SPICE, comparer avec les resultats experimentaux.</p>

<h3 class="section-title">Difficultes rencontrees</h3>

<p><strong>Equations non-lineaires</strong> :</p>
<p>Les equations de Shockley et des transistors sont exponentielles (BJT) ou quadratiques (MOS). Resoudre graphiquement ou iterativement demande de la pratique.</p>

<p><strong>Regimes de fonctionnement</strong> :</p>
<p>Identifier dans quel regime se trouve le transistor necessite de verifier plusieurs conditions (VBE, VCE pour BJT ; VGS, VDS pour MOS). Erreur frequente au debut.</p>

<p><strong>Modeles petit signal</strong> :</p>
<p>Comprendre quand et comment lineariser, calculer les parametres dynamiques (gm, r&pi;, ro) a partir du point de repos.</p>

<p><strong>Ecarts theorie/pratique</strong> :</p>
<p>Les modeles simples (Ebers-Moll, quadratique MOS) donnent des resultats approximatifs. Les effets de second ordre (Early, modulation de canal, temperature) expliquent les differences.</p>

<hr/>

<h2>PART C - Aspects Techniques Detailles</h2>

<h3 class="section-title">1. Physique des semi-conducteurs</h3>

<p><strong>Semi-conducteur intrinseque</strong> :</p>
<p>Materiau pur (silicium, germanium) avec concentration egale d'electrons et de trous.</p>
<p>A temperature ambiante :</p>
<ul>
  <li>Silicium : ni = 1.5 &times; 10^10 porteurs/cm&sup3;</li>
  <li>Faible conductivite naturelle</li>
</ul>

<p><strong>Dopage</strong> :</p>
<p>Ajout d'impuretes pour augmenter la conductivite.</p>

<table>
  <tr><th>Type</th><th>Impurete</th><th>Porteurs majoritaires</th><th>Exemple</th></tr>
  <tr><td>N</td><td>Phosphore, Arsenic (5 electrons)</td><td>Electrons</td><td>Donneur d'electrons</td></tr>
  <tr><td>P</td><td>Bore, Aluminium (3 electrons)</td><td>Trous</td><td>Accepteur d'electrons</td></tr>
</table>

<p><strong>Jonction PN</strong> :</p>
<p>Interface entre zone P et zone N creant :</p>
<ul>
  <li>Zone de depletion (zone desertee de porteurs libres)</li>
  <li>Barriere de potentiel (0.7V pour Si, 0.3V pour Ge)</li>
  <li>Comportement de diode (conduction unidirectionnelle)</li>
</ul>

<p><strong>Polarisation</strong> :</p>
<ul>
  <li>Directe : P au +, N au - &rarr; conduction</li>
  <li>Inverse : P au -, N au + &rarr; blocage</li>
</ul>

<h3 class="section-title">2. Transistor bipolaire (BJT)</h3>

<p><strong>Structure</strong> :</p>
<p>Trois couches de semi-conducteurs : NPN (ou PNP symetrique).</p>
<ul>
  <li><strong>Emetteur (E)</strong> : fortement dope, source de porteurs</li>
  <li><strong>Base (B)</strong> : tres fine, faiblement dopee</li>
  <li><strong>Collecteur (C)</strong> : moderement dope, collecte les porteurs</li>
</ul>

<p><strong>Principe de fonctionnement</strong> :</p>
<p>Deux jonctions PN en serie :</p>
<ul>
  <li>Jonction Base-Emetteur (BE) : polarisee en direct</li>
  <li>Jonction Base-Collecteur (BC) : polarisee en inverse (mode actif)</li>
</ul>
<p>Les electrons injectes de l'emetteur traversent la base fine et sont collectes par le collecteur.</p>

<p><strong>Courants et relations</strong> :</p>
<p>Courant collecteur : IC = &beta; &times; IB</p>
<p>avec &beta; (gain en courant) typiquement 50 a 300.</p>
<p>Courant emetteur : IE = IC + IB &asymp; IC (car &beta; grand)</p>

<p><strong>Equation de Shockley</strong> :</p>
<p>IC = IS &times; exp(VBE / VT)</p>
<p>avec :</p>
<ul>
  <li>IS : courant de saturation (depend de la geometrie et du dopage)</li>
  <li>VT : tension thermique &asymp; 26 mV a 25&deg;C</li>
</ul>

<p><strong>Regimes de fonctionnement</strong> :</p>

<table>
  <tr><th>Regime</th><th>Jonction BE</th><th>Jonction BC</th><th>Application</th></tr>
  <tr><td>Bloque</td><td>Inverse</td><td>Inverse</td><td>Interrupteur OFF</td></tr>
  <tr><td>Actif</td><td>Directe</td><td>Inverse</td><td>Amplification</td></tr>
  <tr><td>Saturation</td><td>Directe</td><td>Directe</td><td>Interrupteur ON</td></tr>
  <tr><td>Actif inverse</td><td>Inverse</td><td>Directe</td><td>Rarement utilise</td></tr>
</table>

<p><strong>Mode actif</strong> (amplification) :</p>
<ul>
  <li>VBE &asymp; 0.7V (jonction Si en conduction)</li>
  <li>VCE &gt; 0.2V (pour rester hors saturation)</li>
  <li>IC = &beta; &times; IB</li>
</ul>

<p><strong>Mode saturation</strong> (commutation ON) :</p>
<ul>
  <li>VBE &asymp; 0.8V</li>
  <li>VCE_sat &asymp; 0.2V</li>
  <li>IC &lt; &beta; &times; IB (le gain &beta; n'est plus respecte)</li>
</ul>

<h3 class="section-title">3. Modele petit signal du BJT</h3>

<p><strong>Principe</strong> :</p>
<p>Lineariser autour du point de repos (Q) pour analyser les variations de signaux de faible amplitude.</p>

<p><strong>Parametres dynamiques</strong> :</p>

<p><strong>Transconductance</strong> :</p>
<p>gm = IC / VT &asymp; 40 &times; IC (mA)</p>
<p>Exemple : IC = 1 mA &rarr; gm = 40 mS</p>

<p><strong>Resistance d'entree dynamique</strong> :</p>
<p>r&pi; = &beta; / gm</p>
<p>Exemple : &beta; = 100, gm = 40 mS &rarr; r&pi; = 2.5 k&Omega;</p>

<p><strong>Resistance de sortie</strong> (effet Early) :</p>
<p>ro = VA / IC</p>
<p>avec VA (tension d'Early) typiquement 50 a 150V.</p>

<p><strong>Modele equivalent petit signal</strong> :</p>
<ul>
  <li>Entre base et emetteur : r&pi; en parallele avec C&pi; (capacite BE)</li>
  <li>Source de courant controlee : gm &times; vbe</li>
  <li>Resistance de sortie : ro entre collecteur et emetteur</li>
  <li>Capacite Miller : C&mu; entre base et collecteur</li>
</ul>

<h3 class="section-title">4. Transistor MOS (MOSFET)</h3>

<p><strong>Structure</strong> :</p>
<p>Transistor a effet de champ a grille isolee (oxyde).</p>
<p>Composants :</p>
<ul>
  <li><strong>Grille (G)</strong> : electrode de commande isolee par SiO2</li>
  <li><strong>Source (S)</strong> : source de porteurs</li>
  <li><strong>Drain (D)</strong> : collecte des porteurs</li>
  <li><strong>Substrat (Bulk/Body)</strong> : generalement connecte a la source</li>
</ul>

<p><strong>Types</strong> :</p>
<ul>
  <li><strong>NMOS</strong> : canal N (electrons), substrat P</li>
  <li><strong>PMOS</strong> : canal P (trous), substrat N</li>
</ul>

<p><strong>Principe de fonctionnement</strong> :</p>
<p>Tension VGS cree un champ electrique qui attire ou repousse les porteurs sous la grille, formant un canal conducteur entre source et drain.</p>

<p><strong>Tension de seuil (VTH)</strong> :</p>
<p>Tension minimale VGS pour creer le canal.</p>
<p>Typiquement :</p>
<ul>
  <li>NMOS : VTH &asymp; 0.5 a 1V</li>
  <li>PMOS : VTH &asymp; -0.5 a -1V</li>
</ul>

<p><strong>Regimes de fonctionnement</strong> :</p>

<table>
  <tr><th>Regime</th><th>Condition</th><th>Equation ID</th></tr>
  <tr><td>Bloque</td><td>VGS &lt; VTH</td><td>ID = 0</td></tr>
  <tr><td>Lineaire (triode)</td><td>VGS &gt; VTH, VDS &lt; VGS - VTH</td><td>ID &prop; VDS (resistance controlee)</td></tr>
  <tr><td>Saturation</td><td>VGS &gt; VTH, VDS &ge; VGS - VTH</td><td>ID constant (source de courant)</td></tr>
</table>

<p><strong>Region lineaire</strong> :</p>
<p>Le transistor se comporte comme une resistance controlee en tension.</p>
<p>ID = K &times; [(VGS - VTH) &times; VDS - VDS&sup2; / 2]</p>
<p>avec K = &mu;n &times; Cox &times; W/L</p>

<p><strong>Region de saturation</strong> :</p>
<p>Le transistor est une source de courant controlee en tension.</p>
<p>ID = (K / 2) &times; (VGS - VTH)&sup2; &times; (1 + &lambda; &times; VDS)</p>
<p>avec &lambda; (coefficient de modulation de canal) &lt;&lt; 1.</p>

<p><strong>Parametres technologiques</strong> :</p>

<table>
  <tr><th>Parametre</th><th>Description</th><th>Valeur typique</th></tr>
  <tr><td>&mu;n</td><td>Mobilite electrons</td><td>500 cm&sup2;/Vs</td></tr>
  <tr><td>&mu;p</td><td>Mobilite trous</td><td>200 cm&sup2;/Vs</td></tr>
  <tr><td>Cox</td><td>Capacite d'oxyde de grille</td><td>3-10 fF/&mu;m&sup2;</td></tr>
  <tr><td>W/L</td><td>Rapport geometrique</td><td>1 a 100</td></tr>
  <tr><td>VTH</td><td>Tension de seuil</td><td>0.5-1V</td></tr>
  <tr><td>&lambda;</td><td>Modulation de canal</td><td>0.01-0.1 V&sup;-1</td></tr>
</table>

<p><strong>Rapport W/L</strong> :</p>
<p>Plus W/L est grand, plus le courant ID est eleve pour un VGS donne.</p>
<p>Dimensionnement typique :</p>
<ul>
  <li>Transistors de puissance : W/L &gt; 10</li>
  <li>Transistors de signal : W/L &asymp; 2-5</li>
  <li>Transistors de charge : W/L &lt; 1</li>
</ul>

<h3 class="section-title">5. Modele petit signal du MOSFET</h3>

<p><strong>Parametres dynamiques</strong> :</p>

<p><strong>Transconductance</strong> :</p>
<p>gm = 2 &times; ID / (VGS - VTH)</p>
<p>ou</p>
<p>gm = racine(2 &times; K &times; ID)</p>

<p><strong>Resistance de sortie</strong> :</p>
<p>ro = 1 / (&lambda; &times; ID)</p>
<p>Typiquement 10 k&Omega; a 100 k&Omega;.</p>

<p><strong>Modele equivalent petit signal</strong> :</p>
<ul>
  <li>Grille : haute impedance (pratiquement infinie en DC, capacites en AC)</li>
  <li>Source de courant : gm &times; vgs</li>
  <li>Resistance de sortie : ro entre drain et source</li>
  <li>Capacites parasites : Cgs, Cgd, Cdb</li>
</ul>

<h3 class="section-title">6. Configurations d'amplification</h3>

<p>Trois configurations de base pour BJT et MOS :</p>

<p><strong>Emetteur commun (EC) / Source commune (SC)</strong> :</p>

<table>
  <tr><th>Caracteristique</th><th>Valeur typique</th></tr>
  <tr><td>Gain en tension</td><td>Av = -gm &times; RC (eleve, 10-100)</td></tr>
  <tr><td>Impedance d'entree</td><td>Moyenne (BJT : r&pi;, MOS : infinie DC)</td></tr>
  <tr><td>Impedance de sortie</td><td>Moyenne (RC // ro)</td></tr>
  <tr><td>Dephasage</td><td>180&deg; (inversion)</td></tr>
  <tr><td>Application</td><td>Amplification general usage</td></tr>
</table>

<p><strong>Base commune (BC) / Grille commune (GC)</strong> :</p>

<table>
  <tr><th>Caracteristique</th><th>Valeur typique</th></tr>
  <tr><td>Gain en tension</td><td>Av = gm &times; RC (positif)</td></tr>
  <tr><td>Impedance d'entree</td><td>Faible (1/gm &asymp; 25&Omega; pour BJT)</td></tr>
  <tr><td>Impedance de sortie</td><td>Elevee</td></tr>
  <tr><td>Dephasage</td><td>0&deg; (pas d'inversion)</td></tr>
  <tr><td>Bande passante</td><td>Tres large (pas d'effet Miller)</td></tr>
  <tr><td>Application</td><td>Amplificateur RF, adaptation d'impedance</td></tr>
</table>

<p><strong>Collecteur commun (CC) / Drain commun (DC)</strong> (suiveur) :</p>

<table>
  <tr><th>Caracteristique</th><th>Valeur typique</th></tr>
  <tr><td>Gain en tension</td><td>Av &asymp; 1 (suiveur)</td></tr>
  <tr><td>Impedance d'entree</td><td>Tres elevee</td></tr>
  <tr><td>Impedance de sortie</td><td>Tres faible (1/gm)</td></tr>
  <tr><td>Dephasage</td><td>0&deg;</td></tr>
  <tr><td>Application</td><td>Buffer, adaptation d'impedance</td></tr>
</table>

<h3 class="section-title">7. Polarisation des transistors</h3>

<p><strong>Objectif</strong> :</p>
<p>Fixer le point de repos Q (IC0, VCE0 pour BJT ; ID0, VDS0 pour MOS) pour permettre l'amplification du signal.</p>

<p><strong>Polarisation par pont de base (BJT)</strong> :</p>
<p>Circuit classique avec 4 resistances : R1, R2 (diviseur de tension base), RC (collecteur), RE (emetteur).</p>
<p>Etapes de calcul :</p>
<ol>
  <li>Calculer VB = VCC &times; R2 / (R1 + R2)</li>
  <li>Calculer VE = VB - 0.7V</li>
  <li>Calculer IE = VE / RE</li>
  <li>Calculer IC &asymp; IE</li>
  <li>Calculer VCE = VCC - RC &times; IC - RE &times; IE</li>
</ol>

<p><strong>Polarisation par source de courant (MOS)</strong> :</p>
<p>Utiliser un transistor MOS en saturation comme source de courant pour polariser un autre transistor.</p>

<p><strong>Stabilite thermique</strong> :</p>
<p>Resistance d'emetteur RE ou resistance de source RS permettent de stabiliser le point de repos contre les variations de temperature.</p>

<h3 class="section-title">8. Amplificateur differentiel</h3>

<p><strong>Structure</strong> :</p>
<p>Paire de transistors apparies avec source de courant commune.</p>

<p><strong>Signaux</strong> :</p>
<ul>
  <li>Mode differentiel : vd = v1 - v2</li>
  <li>Mode commun : vcm = (v1 + v2) / 2</li>
</ul>

<p><strong>Gains</strong> :</p>
<p>Gain differentiel : Ad = gm &times; RC</p>
<p>Gain de mode commun : Acm &asymp; -RC / (2 &times; RE) (tres faible si RE grand)</p>

<p><strong>Taux de rejection de mode commun (CMRR)</strong> :</p>
<p>CMRR = Ad / Acm</p>
<p>En dB : CMRR_dB = 20 &times; log(Ad / Acm)</p>
<p>Typiquement 60-100 dB pour un bon ampli differentiel.</p>

<p><strong>Applications</strong> :</p>
<ul>
  <li>Amplificateurs operationnels (etage d'entree)</li>
  <li>Comparateurs</li>
  <li>Amplification de signaux de capteurs (elimination du bruit de mode commun)</li>
</ul>

<h3 class="section-title">9. Miroir de courant</h3>

<p><strong>Principe</strong> :</p>
<p>Copier (recopier) un courant de reference vers une ou plusieurs branches.</p>

<p><strong>Miroir simple MOS</strong> :</p>
<p>Deux transistors NMOS avec grilles connectees :</p>
<ul>
  <li>M1 : monte en diode (grille connectee au drain), fixe IREF</li>
  <li>M2 : recopie le courant, IOUT = IREF &times; (W2/L2) / (W1/L1)</li>
</ul>
<p>Si W2/L2 = W1/L1 alors IOUT = IREF.</p>

<p><strong>Avantages</strong> :</p>
<ul>
  <li>Generation de courants de polarisation precis</li>
  <li>Economie de resistances</li>
  <li>Facilite d'integration</li>
</ul>

<p><strong>Miroir de Wilson</strong> :</p>
<p>Version amelioree avec meilleure precision et resistance de sortie plus elevee.</p>

<p><strong>Applications</strong> :</p>
<ul>
  <li>Polarisation de circuits integres</li>
  <li>Sources de courant pour amplificateurs differentiels</li>
  <li>Charges actives (remplacement de resistances RC)</li>
</ul>

<h3 class="section-title">10. Effets de second ordre</h3>

<p><strong>Effet Early (BJT)</strong> :</p>
<p>Modulation de la largeur de base par VCE. Lorsque VCE augmente, la zone de depletion de la jonction BC s'elargit, reduisant la largeur effective de la base.</p>
<p>Consequence : IC augmente legerement avec VCE (pente non nulle dans la zone active).</p>
<p>Modele : IC = IS &times; exp(VBE / VT) &times; (1 + VCE / VA)</p>
<p>Tension d'Early VA : typiquement 50-150V.</p>
<p>Impact : resistance de sortie finie ro = VA / IC.</p>

<p><strong>Modulation de canal (MOS)</strong> :</p>
<p>En saturation, l'augmentation de VDS reduit la longueur effective du canal (le point de pincement se deplace vers la source).</p>
<p>Consequence : ID augmente legerement avec VDS.</p>
<p>Modele : ID = (K/2) &times; (VGS - VTH)&sup2; &times; (1 + &lambda; &times; VDS)</p>
<p>Coefficient &lambda; : typiquement 0.01 a 0.1 V&sup;-1.</p>
<p>Impact : resistance de sortie finie ro = 1 / (&lambda; &times; ID).</p>

<p><strong>Effets thermiques</strong> :</p>

<p><strong>BJT</strong> :</p>
<ul>
  <li>VBE diminue avec temperature : -2 mV/&deg;C</li>
  <li>IC augmente si VBE est fixe (emballement thermique possible)</li>
  <li>&beta; varie avec temperature</li>
</ul>

<p><strong>MOS</strong> :</p>
<ul>
  <li>VTH diminue avec temperature : -2 a -4 mV/&deg;C</li>
  <li>Mobilite &mu; diminue avec temperature (ID diminue)</li>
  <li>Comportement plus stable thermiquement que BJT</li>
</ul>

<p><strong>Effets capacitifs</strong> :</p>
<p>Capacites parasites limitent la bande passante :</p>
<ul>
  <li><strong>BJT</strong> : C&pi; (jonction BE), C&mu; (jonction BC, effet Miller)</li>
  <li><strong>MOS</strong> : Cgs, Cgd (effet Miller), Cdb</li>
</ul>

<p>Frequence de transition fT : frequence ou le gain en courant tombe a 1.</p>
<p>fT = gm / (2&pi; &times; (C&pi; + C&mu;)) pour BJT</p>
<p>fT = gm / (2&pi; &times; (Cgs + Cgd)) pour MOS</p>

<h3 class="section-title">11. Modeles de simulation SPICE</h3>

<p><strong>Modele Ebers-Moll (BJT)</strong> :</p>
<p>Modele basique avec deux diodes et deux sources de courant controlees. Suffisant pour analyses simples.</p>

<p><strong>Modele Gummel-Poon (BJT)</strong> :</p>
<p>Modele avance incluant :</p>
<ul>
  <li>Effet Early</li>
  <li>Recombinaison dans la base</li>
  <li>Effets haute injection</li>
  <li>Dependances thermiques</li>
  <li>Capacites parasites</li>
</ul>
<p>Standard pour simulation precise.</p>

<p><strong>Modele Level 1 (MOS)</strong> :</p>
<p>Modele simple, equations quadratiques. Utilise pour enseignement.</p>

<p><strong>Modele BSIM (Berkeley Short-channel IGFET Model)</strong> :</p>
<p>Modele industriel standard pour technologies submicroniques.</p>
<p>Versions : BSIM3, BSIM4, BSIM-CMG (FinFET).</p>
<p>Parametres extraits de mesures sur silicium (plusieurs centaines de parametres).</p>
<p>Inclut : effets de canal court, effets quantiques, effets de substrat, dependances geometriques.</p>

<p><strong>Utilisation en simulation</strong> :</p>
<p>Fichier de modele fourni par le fondeur (.lib) contenant les parametres SPICE des transistors pour une technologie donnee (ex : 65nm, 28nm).</p>

<h3 class="section-title">12. Caracterisation experimentale</h3>

<p><strong>Mesures statiques (courbes I-V)</strong> :</p>

<p><strong>BJT</strong> :</p>
<ul>
  <li>Tracer IC vs VCE pour differentes valeurs de IB (reseau de courbes)</li>
  <li>Identifier zone active (pente faible, effet Early), zone de saturation (VCE &lt; 0.2V)</li>
  <li>Extraire &beta; = IC / IB dans la zone active</li>
</ul>

<p><strong>MOS</strong> :</p>
<ul>
  <li>Tracer ID vs VDS pour differentes valeurs de VGS (reseau de courbes)</li>
  <li>Identifier zone lineaire (pente forte), zone de saturation (courant constant)</li>
  <li>Extraire VTH : tension VGS ou ID commence a circuler</li>
  <li>Extraire K a partir de ID en saturation</li>
</ul>

<p><strong>Mesures dynamiques</strong> :</p>

<p><strong>Transconductance gm</strong> :</p>
<p>Mesurer la variation de IC (ou ID) pour une petite variation de VBE (ou VGS) autour du point de repos.</p>
<p>gm = &Delta;IC / &Delta;VBE (a VCE constant)</p>

<p><strong>Frequence de transition fT</strong> :</p>
<p>Mesurer le gain en courant en fonction de la frequence. fT est la frequence ou le gain vaut 1 (0 dB).</p>

<p><strong>Capacites parasites</strong> :</p>
<p>Mesures avec pont d'impedance ou analyseur de reseau vectoriel.</p>

<h3 class="section-title">13. Technologies avancees</h3>

<p><strong>MOSFET de puissance</strong> :</p>
<p>Structure verticale (VDMOS, UMOS) pour augmenter la tenue en tension et le courant.</p>
<p>Parametre cle : RDSon (resistance drain-source a l'etat passant). Plus faible = moins de pertes.</p>
<p>Applications : alimentations a decoupage, onduleurs, variateurs de vitesse.</p>

<p><strong>IGBT (Insulated Gate Bipolar Transistor)</strong> :</p>
<p>Hybride BJT + MOSFET : commande en tension (grille MOS) + conduction bipolaire (faible chute de tension).</p>
<p>Applications : traction electrique, energie renouvelable, soudage.</p>

<p><strong>Composants grand gap (GaN, SiC)</strong> :</p>
<p>Materiaux semi-conducteurs avec gap plus large que Si :</p>
<ul>
  <li>Tenue en tension plus elevee</li>
  <li>Frequences de commutation plus rapides</li>
  <li>Fonctionnement haute temperature</li>
  <li>Pertes reduites</li>
</ul>
<p>Applications : electronique de puissance haute performance, vehicules electriques, datacenters.</p>

<hr/>

<h2>PART D - Analyse Reflexive et Perspectives</h2>

<h3 class="section-title">Competences acquises</h3>

<p><strong>Comprehension physique</strong> :</p>
<p>Capacite a expliquer le fonctionnement des transistors depuis les bases physiques (jonctions, dopage, porteurs) jusqu'aux modeles mathematiques.</p>

<p><strong>Modelisation et calcul</strong> :</p>
<p>Maitrise des equations des transistors, identification des regimes de fonctionnement, calcul de points de repos et de parametres petit signal.</p>

<p><strong>Analyse de circuits</strong> :</p>
<p>Aptitude a analyser des circuits d'amplification et de polarisation, calculer gains, impedances, bande passante.</p>

<p><strong>Simulation</strong> :</p>
<p>Utilisation efficace de SPICE avec modeles avances, interpretation des resultats, comparaison theorie/simulation.</p>

<p><strong>Caracterisation experimentale</strong> :</p>
<p>Techniques de mesure des caracteristiques statiques et dynamiques, extraction de parametres, validation de modeles.</p>

<h3 class="section-title">Points cles a retenir</h3>

<p><strong>1. Regimes de fonctionnement</strong> :</p>
<p>Toujours identifier dans quel regime travaille le transistor (bloque, actif/saturation, saturation/lineaire). Les equations changent selon le regime.</p>

<p><strong>2. Petit signal vs grand signal</strong> :</p>
<p>Modeles petit signal valables seulement pour petites variations autour du point de repos. Pour grands signaux, utiliser les equations non-lineaires completes.</p>

<p><strong>3. Effets de second ordre</strong> :</p>
<p>Modeles simples (Ebers-Moll, quadratique MOS) donnent des approximations. Effets Early, modulation de canal, temperature expliquent les ecarts.</p>

<p><strong>4. BJT vs MOS</strong> :</p>
<ul>
  <li>BJT : commande en courant (IB), transconductance elevee, bruit faible, consommation statique (IB)</li>
  <li>MOS : commande en tension (VGS), haute impedance d'entree, facilite d'integration, pas de consommation statique de grille</li>
</ul>

<p><strong>5. Simulation &ne; realite</strong> :</p>
<p>Les simulations sont aussi bonnes que les modeles utilises. Toujours valider par l'experience, surtout pour les performances critiques.</p>

<h3 class="section-title">Retour d'experience</h3>

<p><strong>Courbe d'apprentissage</strong> :</p>
<p>Le cours necessite une bonne base en mathematiques et physique. La physique des semi-conducteurs est abstraite au debut mais devient claire avec les exemples concrets.</p>

<p><strong>Importance des TD</strong> :</p>
<p>Les exercices de TD (5 series avec corrections) sont essentiels pour maitriser les calculs de polarisation, les modeles petit signal, et les applications MOS. Refaire les TD avant l'examen est crucial.</p>

<p><strong>Annales precieuses</strong> :</p>
<p>Les annales d'examens (2015-2023) permettent de se familiariser avec le type de questions posees (calculs de point de repos, modeles petit signal, identification de regimes).</p>

<p><strong>Lien theorie/pratique</strong> :</p>
<p>Les TP de caracterisation ont montre les ecarts entre modeles ideaux et composants reels (dispersion des parametres, effets parasites). Cela developpe l'esprit critique.</p>

<h3 class="section-title">Applications pratiques</h3>

<p><strong>Conception analogique</strong> :</p>
<ul>
  <li>Amplificateurs audio, RF, instrumentation</li>
  <li>Oscillateurs et generateurs de signaux</li>
  <li>Alimentations lineaires et regulateurs</li>
  <li>Circuits de conditionnement de capteurs</li>
</ul>

<p><strong>Circuits integres</strong> :</p>
<ul>
  <li>Amplificateurs operationnels (etages d'entree differentiels, etages de sortie)</li>
  <li>Convertisseurs A/N et N/A</li>
  <li>Memoires (transistors MOS comme interrupteurs)</li>
  <li>Circuits logiques CMOS</li>
</ul>

<p><strong>Electronique de puissance</strong> :</p>
<ul>
  <li>Onduleurs et convertisseurs DC-DC</li>
  <li>Variateurs de vitesse moteurs</li>
  <li>Chargeurs de batteries</li>
  <li>Alimentations a decoupage</li>
</ul>

<p><strong>Instrumentation</strong> :</p>
<ul>
  <li>Preamplificateurs faible bruit</li>
  <li>Buffers haute impedance</li>
  <li>Multiplexeurs analogiques</li>
</ul>

<h3 class="section-title">Limites et ouvertures</h3>

<p><strong>Limites du cours</strong> :</p>
<ul>
  <li>Focus sur technologies Si classiques (peu sur GaN, SiC)</li>
  <li>Peu d'approfondissement sur conception de circuits integres (layout, regles de dessin)</li>
  <li>Aspects bruit et distorsion non harmonique traites superficiellement</li>
</ul>

<p><strong>Ouvertures vers</strong> :</p>
<ul>
  <li><strong>Conception de CI analogiques</strong> : amplificateurs operationnels complets, references de tension, PLL</li>
  <li><strong>Electronique RF</strong> : amplificateurs faible bruit (LNA), oscillateurs VCO, melangeurs</li>
  <li><strong>Design de circuits integres</strong> : outils CAO (Cadence, Mentor), layout, extraction parasites</li>
  <li><strong>Composants avances</strong> : FinFET, SOI (Silicon On Insulator), technologies BiCMOS</li>
</ul>

<h3 class="section-title">Evolutions technologiques</h3>

<p><strong>Miniaturisation</strong> :</p>
<p>Loi de Moore (doublement du nombre de transistors tous les 18-24 mois) continue mais ralentit.</p>
<p>Technologies actuelles : 3nm, 5nm (TSMC, Samsung).</p>
<p>Defis : effets quantiques, fuites de courant, dissipation thermique.</p>

<p><strong>Technologies emergentes</strong> :</p>
<p><strong>FinFET</strong> : transistor 3D avec grille enrobant le canal sur trois cotes. Meilleur controle du canal, moins de fuites.</p>
<p><strong>GAA (Gate-All-Around)</strong> : prochaine generation apres FinFET. Grille entoure completement le canal.</p>
<p><strong>FD-SOI (Fully Depleted Silicon On Insulator)</strong> : alternative aux FinFET avec meilleure efficacite energetique.</p>

<p><strong>Composants grand gap</strong> :</p>
<p>GaN (Nitrure de Gallium) et SiC (Carbure de Silicium) revolutionnent l'electronique de puissance et RF haute frequence.</p>

<p><strong>Integration 3D</strong> :</p>
<p>Empilement de puces pour augmenter densite et performance (HBM pour memoires, chiplets AMD/Intel).</p>

<h3 class="section-title">Conseils pour reussir</h3>

<p><strong>1. Maitriser les bases physiques</strong> :</p>
<p>Comprendre le fonctionnement interne aide a retenir les equations et a resoudre les problemes.</p>

<p><strong>2. Pratiquer les calculs</strong> :</p>
<p>Refaire tous les TD plusieurs fois jusqu'a maitriser les methodes (polarisation, petit signal, identification regimes).</p>

<p><strong>3. Utiliser SPICE</strong> :</p>
<p>Simuler les exercices pour verifier les calculs et explorer l'impact des parametres.</p>

<p><strong>4. Travailler les annales</strong> :</p>
<p>Les examens suivent des schemas recurrents. S'entrainer sur les annales 2015-2023 pour anticiper les questions.</p>

<p><strong>5. Comprendre les ordres de grandeur</strong> :</p>
<p>Savoir qu'un VBE typique est 0.7V, un gm de 40 mS pour 1 mA, un &beta; de 100, un VTH de 0.7V aide a detecter les erreurs de calcul.</p>

<h3 class="section-title">Conclusion</h3>

<p>Ce module est fondamental pour tout ingenieur en electronique. Il permet de passer d'une utilisation "boite noire" des transistors a une comprehension profonde de leur physique, modelisation et limitations.</p>

<p><strong>Competences transferables</strong> :</p>
<ul>
  <li>Modelisation de systemes physiques complexes</li>
  <li>Analyse non-lineaire et linearisation</li>
  <li>Validation experimentale de modeles theoriques</li>
  <li>Utilisation d'outils de simulation professionnels</li>
</ul>

<p><strong>Pertinence professionnelle</strong> :</p>
<p>La maitrise des composants actifs est indispensable en conception de circuits analogiques, RF, et puissance. Les competences acquises sont directement applicables en R&amp;D et en bureau d'etudes.</p>

<p><strong>Message principal</strong> :</p>
<p>Les transistors sont les briques de base de toute l'electronique moderne. Comprendre leur fonctionnement intime permet de concevoir des circuits performants, robustes et optimises.</p>

<p><strong>Recommandations</strong> :</p>
<ul>
  <li>Approfondir avec des projets de conception de circuits (amplificateurs, oscillateurs)</li>
  <li>Explorer les outils de conception de CI (Cadence, Magic VLSI)</li>
  <li>Etudier des datasheets de composants reels pour comprendre les specifications industrielles</li>
  <li>S'interesser aux nouvelles technologies (FinFET, GaN, SiC) pour rester a jour</li>
</ul>

<p><strong>Liens avec les autres cours</strong> :</p>
<ul>
  <li><a href="./circuits-filtres-analogiques.html">Circuits et Filtres analogiques - S5</a> : analyse de circuits</li>
  <li><a href="./architectures-analogiques-embarques.html">Architectures analogiques systemes embarques - S7</a> : OTA, VCA</li>
  <li><a href="./filtrage-actif-bruit.html">Filtrage actif et modelisation sources bruit - S7</a> : amplificateurs operationnels</li>
  <li><a href="./chaines-acquisition.html">Chaines electroniques acquisition - S8</a> : conditionnement capteurs</li>
</ul>

<hr/>

<h2>Documents de Cours</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Cours Complet EMCA 2023-2024</h4>
      <p>Cours complet d'etude et modelisation des composants actifs : diodes, BJT, MOSFET et amplificateurs.</p>
      <embed src="/cours-pdf/S7/Composants-Actifs/cours-complet.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Composants-Actifs/cours-complet.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>Chapitre 1 - Diodes</h4>
      <p>Modelisation physique et electrique des diodes : jonction PN, caracteristique I-V, modeles petits signaux.</p>
      <embed src="/cours-pdf/S7/Composants-Actifs/chapitre1-diodes.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Composants-Actifs/chapitre1-diodes.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>Chapitre 2 - Transistors Bipolaires</h4>
      <p>Etude des transistors BJT : principe de fonctionnement, modeles Ebers-Moll et hybride-&pi;, polarisation.</p>
      <embed src="/cours-pdf/S7/Composants-Actifs/chapitre2-bjt.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Composants-Actifs/chapitre2-bjt.pdf" target="_blank">Telecharger</a></p>
    </div>
  </div>
</div>

<hr/>

<p><em>Cours suivi en 2023-2024 a l'INSA Toulouse, Departement Genie Electrique et Informatique.</em></p>

</div>

<div class="lang-en">

<h1>Study and Modeling of Active Components - Semester 7</h1>

<p><strong>Academic Year</strong>: 2023-2024<br/>
<strong>Semester</strong>: 7<br/>
<strong>Credits</strong>: 2.5 ECTS<br/>
<strong>Specialty</strong>: Analog Electronics</p>

<hr/>

<h2>PART A - General Module Presentation</h2>

<h3 class="section-title">Overview</h3>

<p>This course provides an in-depth study of active electronic components (bipolar transistors, MOSFETs, operational amplifiers) by analyzing their internal physics, mathematical models, and behavior in static and dynamic regimes. It enables the transition from a superficial use of components to a thorough understanding of their performance and limitations.</p>

<p><strong>Learning objectives</strong>:</p>
<ul>
  <li>Understand semiconductor physics and junctions</li>
  <li>Master bipolar transistor (BJT) and MOS models</li>
  <li>Analyze operating regions (linear, saturation, cutoff)</li>
  <li>Experimentally characterize active components</li>
  <li>Use SPICE simulators with advanced models</li>
  <li>Design biasing and amplification circuits</li>
</ul>

<h3 class="section-title">Position in the curriculum</h3>

<p>This module builds on:</p>
<ul>
  <li><strong>Digital electronics fundamentals (S5)</strong>: PN junctions, transistors in switching</li>
  <li><strong>Analog circuits and filters (S5)</strong>: amplification, two-port networks</li>
  <li><strong>Components and power concepts (S5)</strong>: component characteristics</li>
</ul>

<p>It prepares for:</p>
<ul>
  <li><strong>Analog architectures for embedded systems (S7)</strong>: OTA, integrated circuits</li>
  <li><strong>Active filtering and noise source modeling (S7)</strong>: operational amplifiers</li>
  <li><strong>Electronic acquisition chains (S8)</strong>: signal conditioning</li>
  <li><strong>Analog integrated circuit design</strong>: CMOS design</li>
</ul>

<hr/>

<h2>PART B - Personal Experience and Learning Context</h2>

<h3 class="section-title">Organization and resources</h3>

<p>The module was structured as lectures and tutorial sessions with hands-on work:</p>

<p><strong>Lectures (18h)</strong>:</p>
<p>Divided into 5 thematic parts (Slides_EMCA_2020-2021_1 to 5):</p>
<ul>
  <li>Part 1: Semiconductor physics, PN junction</li>
  <li>Part 2: Bipolar transistor (BJT) - models and operating regions</li>
  <li>Part 3: MOS transistor - structure and operation</li>
  <li>Part 4: Small-signal models and applications</li>
  <li>Part 5: Differential amplifiers and current mirrors</li>
</ul>

<p><strong>Tutorials (12h)</strong>:</p>
<ul>
  <li>TD1 and TD2: Bipolar transistor (biasing, amplification)</li>
  <li>TD3: Introduction to MOS transistor</li>
  <li>TD4 and TD5: Advanced MOS applications</li>
  <li>Solutions available for all tutorials</li>
</ul>

<p><strong>Assessments</strong>:</p>
<ul>
  <li>Continuous assessment (CC) during the semester</li>
  <li>Final exam (past papers available 2015-2023)</li>
  <li>Characterization lab with report</li>
</ul>

<p><strong>Tools used</strong>:</p>
<ul>
  <li>SPICE (circuit simulation with Gummel-Poon, BSIM models)</li>
  <li>Oscilloscope and function generator</li>
  <li>Curve tracer (I-V curves)</li>
  <li>Precision multimeters</li>
</ul>

<h3 class="section-title">Study methodology</h3>

<p><strong>Phase 1: Physical understanding</strong>:</p>
<p>Study the internal structure of the component (junctions, doping, channels) to understand where the equations come from.</p>

<p><strong>Phase 2: Mathematical modeling</strong>:</p>
<p>Master the equations in different operating regions (cutoff, active, saturation for BJT; cutoff, linear, saturation for MOS).</p>

<p><strong>Phase 3: Graphical analysis</strong>:</p>
<p>Plot and interpret static characteristics (IC vs VCE, ID vs VDS) to visualize operating regions.</p>

<p><strong>Phase 4: Small signal</strong>:</p>
<p>Linearize around the operating point and use small-signal equivalent models to calculate gains and impedances.</p>

<p><strong>Phase 5: Simulation</strong>:</p>
<p>Validate analytical calculations with SPICE, compare with experimental results.</p>

<h3 class="section-title">Difficulties encountered</h3>

<p><strong>Nonlinear equations</strong>:</p>
<p>The Shockley and transistor equations are exponential (BJT) or quadratic (MOS). Solving them graphically or iteratively requires practice.</p>

<p><strong>Operating regions</strong>:</p>
<p>Identifying in which region the transistor operates requires checking several conditions (VBE, VCE for BJT; VGS, VDS for MOS). A common mistake at first.</p>

<p><strong>Small-signal models</strong>:</p>
<p>Understanding when and how to linearize, calculating dynamic parameters (gm, r-pi, ro) from the quiescent point.</p>

<p><strong>Theory/practice gaps</strong>:</p>
<p>Simple models (Ebers-Moll, quadratic MOS) give approximate results. Second-order effects (Early, channel-length modulation, temperature) explain the differences.</p>

<hr/>

<h2>PART C - Detailed Technical Aspects</h2>

<h3 class="section-title">1. Semiconductor physics</h3>

<p><strong>Intrinsic semiconductor</strong>:</p>
<p>Pure material (silicon, germanium) with equal concentration of electrons and holes.</p>
<p>At room temperature:</p>
<ul>
  <li>Silicon: ni = 1.5 &times; 10^10 carriers/cm&sup3;</li>
  <li>Low natural conductivity</li>
</ul>

<p><strong>Doping</strong>:</p>
<p>Adding impurities to increase conductivity.</p>

<table>
  <tr><th>Type</th><th>Impurity</th><th>Majority carriers</th><th>Example</th></tr>
  <tr><td>N</td><td>Phosphorus, Arsenic (5 electrons)</td><td>Electrons</td><td>Electron donor</td></tr>
  <tr><td>P</td><td>Boron, Aluminum (3 electrons)</td><td>Holes</td><td>Electron acceptor</td></tr>
</table>

<p><strong>PN Junction</strong>:</p>
<p>Interface between P and N regions creating:</p>
<ul>
  <li>Depletion zone (region depleted of free carriers)</li>
  <li>Potential barrier (0.7V for Si, 0.3V for Ge)</li>
  <li>Diode behavior (unidirectional conduction)</li>
</ul>

<p><strong>Biasing</strong>:</p>
<ul>
  <li>Forward: P to +, N to - &rarr; conduction</li>
  <li>Reverse: P to -, N to + &rarr; cutoff</li>
</ul>

<h3 class="section-title">2. Bipolar Junction Transistor (BJT)</h3>

<p><strong>Structure</strong>:</p>
<p>Three layers of semiconductors: NPN (or symmetrical PNP).</p>
<ul>
  <li><strong>Emitter (E)</strong>: heavily doped, source of carriers</li>
  <li><strong>Base (B)</strong>: very thin, lightly doped</li>
  <li><strong>Collector (C)</strong>: moderately doped, collects carriers</li>
</ul>

<p><strong>Operating principle</strong>:</p>
<p>Two PN junctions in series:</p>
<ul>
  <li>Base-Emitter (BE) junction: forward biased</li>
  <li>Base-Collector (BC) junction: reverse biased (active mode)</li>
</ul>
<p>Electrons injected from the emitter cross the thin base and are collected by the collector.</p>

<p><strong>Currents and relationships</strong>:</p>
<p>Collector current: IC = &beta; &times; IB</p>
<p>with &beta; (current gain) typically 50 to 300.</p>
<p>Emitter current: IE = IC + IB &asymp; IC (since &beta; is large)</p>

<p><strong>Shockley equation</strong>:</p>
<p>IC = IS &times; exp(VBE / VT)</p>
<p>with:</p>
<ul>
  <li>IS: saturation current (depends on geometry and doping)</li>
  <li>VT: thermal voltage &asymp; 26 mV at 25&deg;C</li>
</ul>

<p><strong>Operating regions</strong>:</p>

<table>
  <tr><th>Region</th><th>BE Junction</th><th>BC Junction</th><th>Application</th></tr>
  <tr><td>Cutoff</td><td>Reverse</td><td>Reverse</td><td>Switch OFF</td></tr>
  <tr><td>Active</td><td>Forward</td><td>Reverse</td><td>Amplification</td></tr>
  <tr><td>Saturation</td><td>Forward</td><td>Forward</td><td>Switch ON</td></tr>
  <tr><td>Reverse active</td><td>Reverse</td><td>Forward</td><td>Rarely used</td></tr>
</table>

<p><strong>Active mode</strong> (amplification):</p>
<ul>
  <li>VBE &asymp; 0.7V (Si junction in conduction)</li>
  <li>VCE &gt; 0.2V (to stay out of saturation)</li>
  <li>IC = &beta; &times; IB</li>
</ul>

<p><strong>Saturation mode</strong> (switching ON):</p>
<ul>
  <li>VBE &asymp; 0.8V</li>
  <li>VCE_sat &asymp; 0.2V</li>
  <li>IC &lt; &beta; &times; IB (the &beta; gain is no longer respected)</li>
</ul>

<h3 class="section-title">3. BJT small-signal model</h3>

<p><strong>Principle</strong>:</p>
<p>Linearize around the quiescent point (Q) to analyze small-amplitude signal variations.</p>

<p><strong>Dynamic parameters</strong>:</p>

<p><strong>Transconductance</strong>:</p>
<p>gm = IC / VT &asymp; 40 &times; IC (mA)</p>
<p>Example: IC = 1 mA &rarr; gm = 40 mS</p>

<p><strong>Dynamic input resistance</strong>:</p>
<p>r&pi; = &beta; / gm</p>
<p>Example: &beta; = 100, gm = 40 mS &rarr; r&pi; = 2.5 k&Omega;</p>

<p><strong>Output resistance</strong> (Early effect):</p>
<p>ro = VA / IC</p>
<p>with VA (Early voltage) typically 50 to 150V.</p>

<p><strong>Small-signal equivalent model</strong>:</p>
<ul>
  <li>Between base and emitter: r&pi; in parallel with C&pi; (BE capacitance)</li>
  <li>Controlled current source: gm &times; vbe</li>
  <li>Output resistance: ro between collector and emitter</li>
  <li>Miller capacitance: C&mu; between base and collector</li>
</ul>

<h3 class="section-title">4. MOS Transistor (MOSFET)</h3>

<p><strong>Structure</strong>:</p>
<p>Insulated-gate field-effect transistor (oxide).</p>
<p>Components:</p>
<ul>
  <li><strong>Gate (G)</strong>: control electrode insulated by SiO2</li>
  <li><strong>Source (S)</strong>: carrier source</li>
  <li><strong>Drain (D)</strong>: collects carriers</li>
  <li><strong>Substrate (Bulk/Body)</strong>: generally connected to the source</li>
</ul>

<p><strong>Types</strong>:</p>
<ul>
  <li><strong>NMOS</strong>: N channel (electrons), P substrate</li>
  <li><strong>PMOS</strong>: P channel (holes), N substrate</li>
</ul>

<p><strong>Operating principle</strong>:</p>
<p>Voltage VGS creates an electric field that attracts or repels carriers under the gate, forming a conductive channel between source and drain.</p>

<p><strong>Threshold voltage (VTH)</strong>:</p>
<p>Minimum VGS voltage to create the channel.</p>
<p>Typically:</p>
<ul>
  <li>NMOS: VTH &asymp; 0.5 to 1V</li>
  <li>PMOS: VTH &asymp; -0.5 to -1V</li>
</ul>

<p><strong>Operating regions</strong>:</p>

<table>
  <tr><th>Region</th><th>Condition</th><th>ID Equation</th></tr>
  <tr><td>Cutoff</td><td>VGS &lt; VTH</td><td>ID = 0</td></tr>
  <tr><td>Linear (triode)</td><td>VGS &gt; VTH, VDS &lt; VGS - VTH</td><td>ID &prop; VDS (controlled resistance)</td></tr>
  <tr><td>Saturation</td><td>VGS &gt; VTH, VDS &ge; VGS - VTH</td><td>ID constant (current source)</td></tr>
</table>

<p><strong>Linear region</strong>:</p>
<p>The transistor behaves as a voltage-controlled resistance.</p>
<p>ID = K &times; [(VGS - VTH) &times; VDS - VDS&sup2; / 2]</p>
<p>with K = &mu;n &times; Cox &times; W/L</p>

<p><strong>Saturation region</strong>:</p>
<p>The transistor is a voltage-controlled current source.</p>
<p>ID = (K / 2) &times; (VGS - VTH)&sup2; &times; (1 + &lambda; &times; VDS)</p>
<p>with &lambda; (channel-length modulation coefficient) &lt;&lt; 1.</p>

<p><strong>Technology parameters</strong>:</p>

<table>
  <tr><th>Parameter</th><th>Description</th><th>Typical value</th></tr>
  <tr><td>&mu;n</td><td>Electron mobility</td><td>500 cm&sup2;/Vs</td></tr>
  <tr><td>&mu;p</td><td>Hole mobility</td><td>200 cm&sup2;/Vs</td></tr>
  <tr><td>Cox</td><td>Gate oxide capacitance</td><td>3-10 fF/&mu;m&sup2;</td></tr>
  <tr><td>W/L</td><td>Geometric ratio</td><td>1 to 100</td></tr>
  <tr><td>VTH</td><td>Threshold voltage</td><td>0.5-1V</td></tr>
  <tr><td>&lambda;</td><td>Channel-length modulation</td><td>0.01-0.1 V^-1</td></tr>
</table>

<p><strong>W/L ratio</strong>:</p>
<p>The larger W/L, the higher the current ID for a given VGS.</p>
<p>Typical sizing:</p>
<ul>
  <li>Power transistors: W/L &gt; 10</li>
  <li>Signal transistors: W/L &asymp; 2-5</li>
  <li>Load transistors: W/L &lt; 1</li>
</ul>

<h3 class="section-title">5. MOSFET small-signal model</h3>

<p><strong>Dynamic parameters</strong>:</p>

<p><strong>Transconductance</strong>:</p>
<p>gm = 2 &times; ID / (VGS - VTH)</p>
<p>or</p>
<p>gm = sqrt(2 &times; K &times; ID)</p>

<p><strong>Output resistance</strong>:</p>
<p>ro = 1 / (&lambda; &times; ID)</p>
<p>Typically 10 k&Omega; to 100 k&Omega;.</p>

<p><strong>Small-signal equivalent model</strong>:</p>
<ul>
  <li>Gate: high impedance (virtually infinite at DC, capacitances at AC)</li>
  <li>Current source: gm &times; vgs</li>
  <li>Output resistance: ro between drain and source</li>
  <li>Parasitic capacitances: Cgs, Cgd, Cdb</li>
</ul>

<h3 class="section-title">6. Amplification configurations</h3>

<p>Three basic configurations for BJT and MOS:</p>

<p><strong>Common Emitter (CE) / Common Source (CS)</strong>:</p>

<table>
  <tr><th>Characteristic</th><th>Typical value</th></tr>
  <tr><td>Voltage gain</td><td>Av = -gm &times; RC (high, 10-100)</td></tr>
  <tr><td>Input impedance</td><td>Medium (BJT: r&pi;, MOS: infinite DC)</td></tr>
  <tr><td>Output impedance</td><td>Medium (RC // ro)</td></tr>
  <tr><td>Phase shift</td><td>180&deg; (inversion)</td></tr>
  <tr><td>Application</td><td>General purpose amplification</td></tr>
</table>

<p><strong>Common Base (CB) / Common Gate (CG)</strong>:</p>

<table>
  <tr><th>Characteristic</th><th>Typical value</th></tr>
  <tr><td>Voltage gain</td><td>Av = gm &times; RC (positive)</td></tr>
  <tr><td>Input impedance</td><td>Low (1/gm &asymp; 25&Omega; for BJT)</td></tr>
  <tr><td>Output impedance</td><td>High</td></tr>
  <tr><td>Phase shift</td><td>0&deg; (no inversion)</td></tr>
  <tr><td>Bandwidth</td><td>Very wide (no Miller effect)</td></tr>
  <tr><td>Application</td><td>RF amplifier, impedance matching</td></tr>
</table>

<p><strong>Common Collector (CC) / Common Drain (CD)</strong> (follower):</p>

<table>
  <tr><th>Characteristic</th><th>Typical value</th></tr>
  <tr><td>Voltage gain</td><td>Av &asymp; 1 (follower)</td></tr>
  <tr><td>Input impedance</td><td>Very high</td></tr>
  <tr><td>Output impedance</td><td>Very low (1/gm)</td></tr>
  <tr><td>Phase shift</td><td>0&deg;</td></tr>
  <tr><td>Application</td><td>Buffer, impedance matching</td></tr>
</table>

<h3 class="section-title">7. Transistor biasing</h3>

<p><strong>Objective</strong>:</p>
<p>Set the quiescent point Q (IC0, VCE0 for BJT; ID0, VDS0 for MOS) to enable signal amplification.</p>

<p><strong>Voltage divider biasing (BJT)</strong>:</p>
<p>Classic circuit with 4 resistors: R1, R2 (base voltage divider), RC (collector), RE (emitter).</p>
<p>Calculation steps:</p>
<ol>
  <li>Calculate VB = VCC &times; R2 / (R1 + R2)</li>
  <li>Calculate VE = VB - 0.7V</li>
  <li>Calculate IE = VE / RE</li>
  <li>Calculate IC &asymp; IE</li>
  <li>Calculate VCE = VCC - RC &times; IC - RE &times; IE</li>
</ol>

<p><strong>Current source biasing (MOS)</strong>:</p>
<p>Use a MOS transistor in saturation as a current source to bias another transistor.</p>

<p><strong>Thermal stability</strong>:</p>
<p>Emitter resistance RE or source resistance RS stabilize the quiescent point against temperature variations.</p>

<h3 class="section-title">8. Differential amplifier</h3>

<p><strong>Structure</strong>:</p>
<p>Matched transistor pair with a common current source.</p>

<p><strong>Signals</strong>:</p>
<ul>
  <li>Differential mode: vd = v1 - v2</li>
  <li>Common mode: vcm = (v1 + v2) / 2</li>
</ul>

<p><strong>Gains</strong>:</p>
<p>Differential gain: Ad = gm &times; RC</p>
<p>Common-mode gain: Acm &asymp; -RC / (2 &times; RE) (very low if RE is large)</p>

<p><strong>Common-Mode Rejection Ratio (CMRR)</strong>:</p>
<p>CMRR = Ad / Acm</p>
<p>In dB: CMRR_dB = 20 &times; log(Ad / Acm)</p>
<p>Typically 60-100 dB for a good differential amplifier.</p>

<p><strong>Applications</strong>:</p>
<ul>
  <li>Operational amplifiers (input stage)</li>
  <li>Comparators</li>
  <li>Sensor signal amplification (common-mode noise rejection)</li>
</ul>

<h3 class="section-title">9. Current mirror</h3>

<p><strong>Principle</strong>:</p>
<p>Copy a reference current to one or more branches.</p>

<p><strong>Simple MOS mirror</strong>:</p>
<p>Two NMOS transistors with connected gates:</p>
<ul>
  <li>M1: diode-connected (gate connected to drain), sets IREF</li>
  <li>M2: copies the current, IOUT = IREF &times; (W2/L2) / (W1/L1)</li>
</ul>
<p>If W2/L2 = W1/L1 then IOUT = IREF.</p>

<p><strong>Advantages</strong>:</p>
<ul>
  <li>Precise bias current generation</li>
  <li>Saves resistors</li>
  <li>Ease of integration</li>
</ul>

<p><strong>Wilson mirror</strong>:</p>
<p>Improved version with better accuracy and higher output resistance.</p>

<p><strong>Applications</strong>:</p>
<ul>
  <li>Integrated circuit biasing</li>
  <li>Current sources for differential amplifiers</li>
  <li>Active loads (replacement of RC resistors)</li>
</ul>

<h3 class="section-title">10. Second-order effects</h3>

<p><strong>Early effect (BJT)</strong>:</p>
<p>Base-width modulation by VCE. As VCE increases, the BC junction depletion region widens, reducing the effective base width.</p>
<p>Consequence: IC increases slightly with VCE (non-zero slope in the active region).</p>
<p>Model: IC = IS &times; exp(VBE / VT) &times; (1 + VCE / VA)</p>
<p>Early voltage VA: typically 50-150V.</p>
<p>Impact: finite output resistance ro = VA / IC.</p>

<p><strong>Channel-length modulation (MOS)</strong>:</p>
<p>In saturation, increasing VDS reduces the effective channel length (the pinch-off point moves toward the source).</p>
<p>Consequence: ID increases slightly with VDS.</p>
<p>Model: ID = (K/2) &times; (VGS - VTH)&sup2; &times; (1 + &lambda; &times; VDS)</p>
<p>Coefficient &lambda;: typically 0.01 to 0.1 V^-1.</p>
<p>Impact: finite output resistance ro = 1 / (&lambda; &times; ID).</p>

<p><strong>Thermal effects</strong>:</p>

<p><strong>BJT</strong>:</p>
<ul>
  <li>VBE decreases with temperature: -2 mV/&deg;C</li>
  <li>IC increases if VBE is fixed (thermal runaway possible)</li>
  <li>&beta; varies with temperature</li>
</ul>

<p><strong>MOS</strong>:</p>
<ul>
  <li>VTH decreases with temperature: -2 to -4 mV/&deg;C</li>
  <li>Mobility &mu; decreases with temperature (ID decreases)</li>
  <li>More thermally stable behavior than BJT</li>
</ul>

<p><strong>Capacitive effects</strong>:</p>
<p>Parasitic capacitances limit bandwidth:</p>
<ul>
  <li><strong>BJT</strong>: C&pi; (BE junction), C&mu; (BC junction, Miller effect)</li>
  <li><strong>MOS</strong>: Cgs, Cgd (Miller effect), Cdb</li>
</ul>

<p>Transition frequency fT: frequency where current gain drops to 1.</p>
<p>fT = gm / (2&pi; &times; (C&pi; + C&mu;)) for BJT</p>
<p>fT = gm / (2&pi; &times; (Cgs + Cgd)) for MOS</p>

<h3 class="section-title">11. SPICE simulation models</h3>

<p><strong>Ebers-Moll model (BJT)</strong>:</p>
<p>Basic model with two diodes and two controlled current sources. Sufficient for simple analyses.</p>

<p><strong>Gummel-Poon model (BJT)</strong>:</p>
<p>Advanced model including:</p>
<ul>
  <li>Early effect</li>
  <li>Base recombination</li>
  <li>High injection effects</li>
  <li>Thermal dependencies</li>
  <li>Parasitic capacitances</li>
</ul>
<p>Standard for accurate simulation.</p>

<p><strong>Level 1 model (MOS)</strong>:</p>
<p>Simple model, quadratic equations. Used for teaching.</p>

<p><strong>BSIM model (Berkeley Short-channel IGFET Model)</strong>:</p>
<p>Industry-standard model for submicron technologies.</p>
<p>Versions: BSIM3, BSIM4, BSIM-CMG (FinFET).</p>
<p>Parameters extracted from silicon measurements (several hundred parameters).</p>
<p>Includes: short-channel effects, quantum effects, substrate effects, geometric dependencies.</p>

<p><strong>Use in simulation</strong>:</p>
<p>Model file provided by the foundry (.lib) containing the SPICE parameters of transistors for a given technology (e.g., 65nm, 28nm).</p>

<h3 class="section-title">12. Experimental characterization</h3>

<p><strong>Static measurements (I-V curves)</strong>:</p>

<p><strong>BJT</strong>:</p>
<ul>
  <li>Plot IC vs VCE for different IB values (family of curves)</li>
  <li>Identify active region (low slope, Early effect), saturation region (VCE &lt; 0.2V)</li>
  <li>Extract &beta; = IC / IB in the active region</li>
</ul>

<p><strong>MOS</strong>:</p>
<ul>
  <li>Plot ID vs VDS for different VGS values (family of curves)</li>
  <li>Identify linear region (steep slope), saturation region (constant current)</li>
  <li>Extract VTH: VGS voltage where ID starts flowing</li>
  <li>Extract K from ID in saturation</li>
</ul>

<p><strong>Dynamic measurements</strong>:</p>

<p><strong>Transconductance gm</strong>:</p>
<p>Measure the variation of IC (or ID) for a small variation of VBE (or VGS) around the quiescent point.</p>
<p>gm = &Delta;IC / &Delta;VBE (at constant VCE)</p>

<p><strong>Transition frequency fT</strong>:</p>
<p>Measure current gain as a function of frequency. fT is the frequency where the gain equals 1 (0 dB).</p>

<p><strong>Parasitic capacitances</strong>:</p>
<p>Measurements with impedance bridge or vector network analyzer.</p>

<h3 class="section-title">13. Advanced technologies</h3>

<p><strong>Power MOSFET</strong>:</p>
<p>Vertical structure (VDMOS, UMOS) to increase voltage withstand capability and current.</p>
<p>Key parameter: RDSon (drain-source resistance in the on state). Lower = fewer losses.</p>
<p>Applications: switching power supplies, inverters, variable speed drives.</p>

<p><strong>IGBT (Insulated Gate Bipolar Transistor)</strong>:</p>
<p>BJT + MOSFET hybrid: voltage control (MOS gate) + bipolar conduction (low voltage drop).</p>
<p>Applications: electric traction, renewable energy, welding.</p>

<p><strong>Wide-bandgap components (GaN, SiC)</strong>:</p>
<p>Semiconductor materials with wider bandgap than Si:</p>
<ul>
  <li>Higher voltage withstand capability</li>
  <li>Faster switching frequencies</li>
  <li>High-temperature operation</li>
  <li>Reduced losses</li>
</ul>
<p>Applications: high-performance power electronics, electric vehicles, data centers.</p>

<hr/>

<h2>PART D - Reflective Analysis and Perspectives</h2>

<h3 class="section-title">Skills acquired</h3>

<p><strong>Physical understanding</strong>:</p>
<p>Ability to explain transistor operation from physical fundamentals (junctions, doping, carriers) to mathematical models.</p>

<p><strong>Modeling and calculation</strong>:</p>
<p>Mastery of transistor equations, identification of operating regions, calculation of quiescent points and small-signal parameters.</p>

<p><strong>Circuit analysis</strong>:</p>
<p>Ability to analyze amplification and biasing circuits, calculate gains, impedances, bandwidth.</p>

<p><strong>Simulation</strong>:</p>
<p>Effective use of SPICE with advanced models, interpretation of results, theory/simulation comparison.</p>

<p><strong>Experimental characterization</strong>:</p>
<p>Measurement techniques for static and dynamic characteristics, parameter extraction, model validation.</p>

<h3 class="section-title">Key takeaways</h3>

<p><strong>1. Operating regions</strong>:</p>
<p>Always identify in which region the transistor operates (cutoff, active/saturation, saturation/linear). The equations change depending on the region.</p>

<p><strong>2. Small signal vs large signal</strong>:</p>
<p>Small-signal models are valid only for small variations around the quiescent point. For large signals, use the complete nonlinear equations.</p>

<p><strong>3. Second-order effects</strong>:</p>
<p>Simple models (Ebers-Moll, quadratic MOS) give approximations. Early effect, channel-length modulation, and temperature explain the discrepancies.</p>

<p><strong>4. BJT vs MOS</strong>:</p>
<ul>
  <li>BJT: current-controlled (IB), high transconductance, low noise, static power consumption (IB)</li>
  <li>MOS: voltage-controlled (VGS), high input impedance, ease of integration, no static gate power consumption</li>
</ul>

<p><strong>5. Simulation &ne; reality</strong>:</p>
<p>Simulations are only as good as the models used. Always validate through experimentation, especially for critical performance.</p>

<h3 class="section-title">Feedback</h3>

<p><strong>Learning curve</strong>:</p>
<p>The course requires a good foundation in mathematics and physics. Semiconductor physics is abstract at first but becomes clear with concrete examples.</p>

<p><strong>Importance of tutorials</strong>:</p>
<p>Tutorial exercises (5 series with solutions) are essential for mastering biasing calculations, small-signal models, and MOS applications. Redoing tutorials before the exam is crucial.</p>

<p><strong>Valuable past exams</strong>:</p>
<p>Past exam papers (2015-2023) help familiarize with the types of questions asked (quiescent point calculations, small-signal models, region identification).</p>

<p><strong>Theory/practice link</strong>:</p>
<p>Characterization labs showed the gaps between ideal models and real components (parameter dispersion, parasitic effects). This develops critical thinking.</p>

<h3 class="section-title">Practical applications</h3>

<p><strong>Analog design</strong>:</p>
<ul>
  <li>Audio, RF, instrumentation amplifiers</li>
  <li>Oscillators and signal generators</li>
  <li>Linear power supplies and regulators</li>
  <li>Sensor conditioning circuits</li>
</ul>

<p><strong>Integrated circuits</strong>:</p>
<ul>
  <li>Operational amplifiers (differential input stages, output stages)</li>
  <li>A/D and D/A converters</li>
  <li>Memories (MOS transistors as switches)</li>
  <li>CMOS logic circuits</li>
</ul>

<p><strong>Power electronics</strong>:</p>
<ul>
  <li>Inverters and DC-DC converters</li>
  <li>Motor variable speed drives</li>
  <li>Battery chargers</li>
  <li>Switching power supplies</li>
</ul>

<p><strong>Instrumentation</strong>:</p>
<ul>
  <li>Low-noise preamplifiers</li>
  <li>High-impedance buffers</li>
  <li>Analog multiplexers</li>
</ul>

<h3 class="section-title">Limitations and perspectives</h3>

<p><strong>Course limitations</strong>:</p>
<ul>
  <li>Focus on classic Si technologies (little on GaN, SiC)</li>
  <li>Little depth on integrated circuit design (layout, design rules)</li>
  <li>Noise and non-harmonic distortion aspects treated superficially</li>
</ul>

<p><strong>Opens toward</strong>:</p>
<ul>
  <li><strong>Analog IC design</strong>: complete operational amplifiers, voltage references, PLL</li>
  <li><strong>RF electronics</strong>: low-noise amplifiers (LNA), VCO oscillators, mixers</li>
  <li><strong>IC design</strong>: CAD tools (Cadence, Mentor), layout, parasitic extraction</li>
  <li><strong>Advanced components</strong>: FinFET, SOI (Silicon On Insulator), BiCMOS technologies</li>
</ul>

<h3 class="section-title">Technology evolution</h3>

<p><strong>Miniaturization</strong>:</p>
<p>Moore's Law (doubling transistor count every 18-24 months) continues but is slowing down.</p>
<p>Current technologies: 3nm, 5nm (TSMC, Samsung).</p>
<p>Challenges: quantum effects, leakage current, thermal dissipation.</p>

<p><strong>Emerging technologies</strong>:</p>
<p><strong>FinFET</strong>: 3D transistor with gate wrapping around the channel on three sides. Better channel control, fewer leaks.</p>
<p><strong>GAA (Gate-All-Around)</strong>: next generation after FinFET. Gate completely surrounds the channel.</p>
<p><strong>FD-SOI (Fully Depleted Silicon On Insulator)</strong>: alternative to FinFET with better energy efficiency.</p>

<p><strong>Wide-bandgap components</strong>:</p>
<p>GaN (Gallium Nitride) and SiC (Silicon Carbide) are revolutionizing power electronics and high-frequency RF.</p>

<p><strong>3D integration</strong>:</p>
<p>Chip stacking to increase density and performance (HBM for memories, AMD/Intel chiplets).</p>

<h3 class="section-title">Tips for success</h3>

<p><strong>1. Master the physical fundamentals</strong>:</p>
<p>Understanding internal operation helps retain equations and solve problems.</p>

<p><strong>2. Practice calculations</strong>:</p>
<p>Redo all tutorials multiple times until mastering the methods (biasing, small signal, region identification).</p>

<p><strong>3. Use SPICE</strong>:</p>
<p>Simulate exercises to verify calculations and explore parameter impact.</p>

<p><strong>4. Work on past exams</strong>:</p>
<p>Exams follow recurring patterns. Practice on 2015-2023 past papers to anticipate questions.</p>

<p><strong>5. Understand orders of magnitude</strong>:</p>
<p>Knowing that a typical VBE is 0.7V, gm of 40 mS for 1 mA, &beta; of 100, VTH of 0.7V helps detect calculation errors.</p>

<h3 class="section-title">Conclusion</h3>

<p>This module is fundamental for any electronics engineer. It enables the transition from a "black box" use of transistors to a deep understanding of their physics, modeling, and limitations.</p>

<p><strong>Transferable skills</strong>:</p>
<ul>
  <li>Modeling of complex physical systems</li>
  <li>Nonlinear analysis and linearization</li>
  <li>Experimental validation of theoretical models</li>
  <li>Use of professional simulation tools</li>
</ul>

<p><strong>Professional relevance</strong>:</p>
<p>Mastery of active components is essential in analog, RF, and power circuit design. The skills acquired are directly applicable in R&amp;D and design offices.</p>

<p><strong>Key message</strong>:</p>
<p>Transistors are the building blocks of all modern electronics. Understanding their intimate operation enables the design of high-performance, robust, and optimized circuits.</p>

<p><strong>Recommendations</strong>:</p>
<ul>
  <li>Deepen knowledge with circuit design projects (amplifiers, oscillators)</li>
  <li>Explore IC design tools (Cadence, Magic VLSI)</li>
  <li>Study real component datasheets to understand industrial specifications</li>
  <li>Stay current with new technologies (FinFET, GaN, SiC)</li>
</ul>

<p><strong>Links with other courses</strong>:</p>
<ul>
  <li><a href="./circuits-filtres-analogiques.html">Analog Circuits and Filters - S5</a>: circuit analysis</li>
  <li><a href="./architectures-analogiques-embarques.html">Analog Architectures for Embedded Systems - S7</a>: OTA, VCA</li>
  <li><a href="./filtrage-actif-bruit.html">Active Filtering and Noise Source Modeling - S7</a>: operational amplifiers</li>
  <li><a href="./chaines-acquisition.html">Electronic Acquisition Chains - S8</a>: sensor conditioning</li>
</ul>

<hr/>

<h2>Course Documents</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Complete EMCA Course 2023-2024</h4>
      <p>Complete course on study and modeling of active components: diodes, BJT, MOSFET and amplifiers.</p>
      <embed src="/cours-pdf/S7/Composants-Actifs/cours-complet.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Composants-Actifs/cours-complet.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>Chapter 1 - Diodes</h4>
      <p>Physical and electrical modeling of diodes: PN junction, I-V characteristic, small-signal models.</p>
      <embed src="/cours-pdf/S7/Composants-Actifs/chapitre1-diodes.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Composants-Actifs/chapitre1-diodes.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>Chapter 2 - Bipolar Transistors</h4>
      <p>Study of BJT transistors: operating principle, Ebers-Moll and hybrid-pi models, biasing.</p>
      <embed src="/cours-pdf/S7/Composants-Actifs/chapitre2-bjt.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Composants-Actifs/chapitre2-bjt.pdf" target="_blank">Download</a></p>
    </div>
  </div>
</div>

<hr/>

<p><em>Course taken in 2023-2024 at INSA Toulouse, Department of Electrical Engineering and Computer Science.</em></p>

</div>

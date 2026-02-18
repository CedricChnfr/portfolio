---
layout: default
title: "Électronique Fonctions Analogiques - S6"
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
</style>

<div class="back-nav">
    <a href="./my-courses-2022-2023.html">← Retour aux Cours 2022-2023</a>
</div>

<div class="lang-fr">

<h1>Electronique Fonctions Analogiques - Semestre 6</h1>

<p><strong>Annee Universitaire</strong> : 2022-2023<br/>
<strong>Semestre</strong> : 6<br/>
<strong>Credits</strong> : 2 ECTS<br/>
<strong>Specialite</strong> : Electronique et Systemes Embarques</p>

<hr/>

<h2>PART A - Presentation Generale du Cours</h2>

<h3 class="section-title">Vue d'ensemble</h3>

<p>Ce cours approfondit l'etude des circuits et fonctions electroniques analogiques avances. L'accent est mis sur les amplificateurs operationnels (AOP) et leurs defauts reels, les filtres actifs, et les fonctions de conditionnement de signaux. Le cours combine theorie et pratique avec des TPs sur la mesure des imperfections des AOPs et la conception de filtres.</p>

<p><strong>Objectifs pedagogiques</strong> :</p>
<ul>
  <li>Comprendre et caracteriser les defauts reels des amplificateurs operationnels</li>
  <li>Concevoir et analyser des filtres actifs (passe-bas, passe-haut, passe-bande)</li>
  <li>Maitriser les fonctions de conditionnement analogique pour capteurs</li>
  <li>Mesurer et compenser les imperfections des circuits analogiques</li>
</ul>

<h3 class="section-title">Position dans le cursus</h3>

<p>Ce cours s'inscrit dans la continuite des enseignements :</p>
<ul>
  <li><strong>Circuits et Filtres Analogiques (S5)</strong> : bases des circuits RC, RL et fonctions de transfert</li>
  <li><strong>Composants et Notions de Puissance (S5)</strong> : transistors et amplification</li>
  <li><strong>Filtrage Numerique (S6)</strong> : complementarite filtres analogiques/numeriques</li>
</ul>

<p>Il prepare aux cours avances :</p>
<ul>
  <li><strong>Architectures Analogiques pour Transmission (S7)</strong> : chaines RF</li>
  <li><strong>Chaines Electroniques d'Acquisition (S8)</strong> : acquisition de donnees complete</li>
</ul>

<hr/>

<h2>PART B - Experience Personnelle et Contexte d'Apprentissage</h2>

<h3 class="section-title">Organisation et ressources</h3>

<p>Le module etait structure en 3 parties principales :</p>

<p><strong>1. Cours magistraux</strong> :</p>
<ul>
  <li>Defauts des AOPs : offset, courants de polarisation, derive thermique</li>
  <li>Structures de filtres actifs : Sallen-Key, Rauch, biquads</li>
  <li>Fonctions de conditionnement : amplificateurs d'instrumentation, isolation</li>
</ul>

<p><strong>2. Travaux diriges</strong> :</p>
<ul>
  <li>Calculs d'erreurs dues aux defauts d'AOP</li>
  <li>Dimensionnement de filtres actifs (ordres 1, 2, 3)</li>
  <li>Analyse de la stabilite et du gain en boucle fermee</li>
</ul>

<p><strong>3. Travaux pratiques</strong> :</p>
<ul>
  <li><strong>TP1 - Mesure des defauts d'AOP</strong> : caracterisation experimentale d'un LM358</li>
  <li><strong>TP2 - Filtres actifs</strong> : realisation et test de filtres Sallen-Key</li>
</ul>

<h3 class="section-title">Deroulement des TPs</h3>

<p><strong>TP1 : Mesure des Defauts d'Amplificateurs Operationnels</strong></p>

<p>Le premier TP consistait a mesurer les imperfections d'un AOP reel (LM358) :</p>

<table>
  <thead>
    <tr><th>Defaut mesure</th><th>Methode</th><th>Valeur typique</th></tr>
  </thead>
  <tbody>
    <tr><td>Tension d'offset Vos</td><td>Montage suiveur, mesure directe</td><td>2-7 mV</td></tr>
    <tr><td>Courants de polarisation Ib+ et Ib-</td><td>Resistances de forte valeur a l'entree</td><td>20-100 nA</td></tr>
    <tr><td>Gain en tension Av</td><td>Montage amplificateur non-inverseur</td><td>100 000 (100 dB)</td></tr>
    <tr><td>Bande passante BW</td><td>Reponse frequentielle</td><td>1 MHz</td></tr>
    <tr><td>Slew rate SR</td><td>Signal carre, mesure du temps de montee</td><td>0,5 V/us</td></tr>
  </tbody>
</table>

<p><strong>Manipulation pratique</strong> :</p>
<ol>
  <li>Montage suiveur pour offset : sortie non nulle meme avec entree a 0V</li>
  <li>Ajout de resistances aux entrees pour isoler les courants de polarisation</li>
  <li>Balayage frequentiel pour determiner le GBP (Gain-Bandwidth Product)</li>
</ol>

<p><strong>TP2 : Filtres Actifs</strong></p>

<p>Conception et realisation de plusieurs topologies de filtres :</p>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S6/elec-analogique/ampli-op-inverseur.svg" alt="Amplificateur operationnel inverseur" style="max-width: 550px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Schema d'un amplificateur operationnel en montage inverseur</p>
</div>

<p><strong>Filtre passe-bas Sallen-Key ordre 2</strong> :</p>
<ul>
  <li>Frequence de coupure : 1 kHz</li>
  <li>Structure : deux resistances R, deux capacites C, AOP en suiveur</li>
  <li>Pente : -40 dB/decade au-dela de fc</li>
  <li>Avantage : impedance de sortie faible, pas de charge sur les etages suivants</li>
</ul>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S6/elec-analogique/oscilloscope-1.png" alt="Mesure oscilloscope 1" style="max-width: 600px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Mesures a l'oscilloscope - Reponse d'un filtre actif (TP)</p>
</div>

<p><strong>Filtre passe-haut Sallen-Key ordre 2</strong> :</p>
<ul>
  <li>Meme principe avec permutation R et C</li>
  <li>Elimination des composantes basse frequence</li>
</ul>

<p><strong>Observations a l'oscilloscope</strong> :</p>
<ul>
  <li>Verification de l'attenuation en dB par decade</li>
  <li>Mesure du dephasage (90 deg a fc pour ordre 1, 180 deg pour ordre 2)</li>
  <li>Impact du facteur de qualite Q sur la resonance</li>
</ul>

<h3 class="section-title">Difficultes rencontrees</h3>

<p><strong>Parasites et bruit</strong> :</p>
<ul>
  <li>Les mesures d'offset et de courants etaient sensibles au bruit 50 Hz du secteur</li>
  <li>Solution : blindage, masse etoile, condensateurs de decouplage</li>
</ul>

<p><strong>Choix des composants</strong> :</p>
<ul>
  <li>Tolerances des resistances et capacites (5-10%) impactaient les frequences de coupure</li>
  <li>Necessite d'utiliser un multimetre pour mesurer les valeurs reelles</li>
</ul>

<p><strong>Stabilite des montages</strong> :</p>
<ul>
  <li>Oscillations parasites dues au GBP limite de l'AOP</li>
  <li>Ajout de capacites de compensation</li>
</ul>

<hr/>

<h2>PART C - Aspects Techniques Detailles</h2>

<h3 class="section-title">1. Defauts des Amplificateurs Operationnels</h3>

<p>Un AOP reel presente plusieurs imperfections par rapport au modele ideal :</p>

<p><strong>Tension d'offset (Vos)</strong> :</p>
<p>Difference de tension entre les entrees pour obtenir Vout = 0V. Typiquement 1-10 mV.</p>

<p>Impact sur un montage non-inverseur de gain G :</p>
<ul>
  <li>Erreur en sortie = Vos x G</li>
  <li>Exemple : Vos = 5 mV, G = 100 &rarr; erreur de 500 mV !</li>
</ul>

<p><strong>Courants de polarisation (Ib+ et Ib-)</strong> :</p>
<p>Courants d'entree necessaires au fonctionnement des transistors internes. Typiquement 10-200 nA pour un LM358.</p>

<p>Compensation : resistance Rc en serie avec l'entree non-inverseuse</p>
<ul>
  <li>Rc = R1 // R2 (parallele des resistances de gain)</li>
</ul>

<p><strong>Courant d'offset (Ios)</strong> :</p>
<p>Difference entre Ib+ et Ib- : Ios = |Ib+ - Ib-|</p>

<p><strong>Gain en tension fini (Av)</strong> :</p>
<p>Au lieu d'etre infini, le gain en boucle ouverte est limite (typiquement 100 000 = 100 dB).</p>

<p>Effet sur le gain en boucle fermee :</p>
<ul>
  <li>Gain reel legerement inferieur au gain theorique</li>
  <li>Importance pour les applications de precision</li>
</ul>

<p><strong>Produit Gain-Bande Passante (GBP)</strong> :</p>
<p>Le gain diminue avec la frequence. Produit constant GBP = Av x BW.</p>
<ul>
  <li>LM358 : GBP = 1 MHz</li>
  <li>Si gain souhaite = 100, BW max = 10 kHz</li>
</ul>

<p><strong>Slew Rate (SR)</strong> :</p>
<p>Vitesse maximale de variation de la tension de sortie. Limitee par les courants de charge internes.</p>
<ul>
  <li>LM358 : SR &approx; 0,5 V/us</li>
  <li>Limite la frequence maximale des signaux de forte amplitude</li>
</ul>

<p><strong>CMRR (Common Mode Rejection Ratio)</strong> :</p>
<p>Capacite a rejeter les signaux de mode commun. Typiquement 70-100 dB.</p>
<ul>
  <li>CMRR faible &rarr; sensibilite aux perturbations sur l'alimentation</li>
</ul>

<p><strong>PSRR (Power Supply Rejection Ratio)</strong> :</p>
<p>Rejet des variations d'alimentation. Important pour les circuits sur batterie.</p>

<h3 class="section-title">2. Filtres Actifs</h3>

<p>Les filtres actifs utilisent des AOPs pour obtenir des fonctions de transfert sans inductances.</p>

<p><strong>Avantages par rapport aux filtres passifs</strong> :</p>
<ul>
  <li>Pas d'inductances (encombrement, cout, non-idealites)</li>
  <li>Gain possible (amplification + filtrage)</li>
  <li>Impedance de sortie faible</li>
  <li>Pas d'effet de charge entre etages</li>
</ul>

<p><strong>Structure Sallen-Key (passe-bas ordre 2)</strong> :</p>

<p>Configuration typique :</p>
<ul>
  <li>Deux resistances R1 = R2 = R</li>
  <li>Deux condensateurs C1 = C2 = C</li>
  <li>AOP monte en suiveur (gain = 1)</li>
</ul>

<p>Frequence de coupure : fc = 1 / (2pi x R x C)</p>

<p>Fonction de transfert : H(p) = 1 / (1 + a1 x p + a2 x p²)</p>
<ul>
  <li>a1 et a2 dependent du facteur de qualite Q</li>
  <li>Q = 0,707 pour reponse Butterworth (maximalement plate)</li>
</ul>

<p><strong>Filtre passe-haut ordre 2</strong> :</p>
<p>Inversion des positions R et C par rapport au passe-bas.</p>

<p><strong>Filtre passe-bande</strong> :</p>
<p>Cascade d'un passe-haut et d'un passe-bas, ou structure Rauch.</p>
<ul>
  <li>Bande passante : f1 &lt; f &lt; f2</li>
  <li>Facteur de qualite : Q = f0 / (f2 - f1)</li>
</ul>

<p><strong>Filtre coupe-bande (notch)</strong> :</p>
<p>Attenue une bande de frequences (ex : eliminer le 50 Hz secteur).</p>

<p><strong>Filtres d'ordre superieur</strong> :</p>
<p>Cascade de plusieurs cellules d'ordre 2 (biquads).</p>
<ul>
  <li>Ordre 4 : deux cellules ordre 2 &rarr; pente -80 dB/decade</li>
  <li>Chaque cellule a son propre Q pour obtenir la reponse globale souhaitee</li>
</ul>

<p><strong>Types de reponses</strong> :</p>
<ul>
  <li><strong>Butterworth</strong> : maximalement plate en bande passante</li>
  <li><strong>Chebyshev</strong> : ondulations en bande passante, coupure plus raide</li>
  <li><strong>Bessel</strong> : reponse de phase lineaire, pas de distorsion temporelle</li>
</ul>

<h3 class="section-title">3. Amplificateurs d'Instrumentation</h3>

<p>Circuits specialises pour mesures de precision sur capteurs.</p>

<p><strong>Caracteristiques</strong> :</p>
<ul>
  <li>Gain differentiel eleve et stable</li>
  <li>Impedance d'entree tres elevee (&gt; 1 GOhm)</li>
  <li>CMRR tres eleve (&gt; 100 dB)</li>
  <li>Faible derive thermique</li>
</ul>

<p><strong>Structure classique a 3 AOPs</strong> :</p>
<ul>
  <li>Etage d'entree : deux AOPs en configuration non-inverseuse</li>
  <li>Etage de sortie : amplificateur differentiel</li>
  <li>Gain ajustable par une seule resistance externe</li>
</ul>

<p><strong>Applications</strong> :</p>
<ul>
  <li>Ponts de Wheatstone (jauges de contrainte)</li>
  <li>Thermocouples</li>
  <li>Mesures biomedicales (ECG, EEG)</li>
</ul>

<p><strong>Exemple : pont de Wheatstone</strong></p>

<p>Capteur de contrainte avec 4 resistances :</p>
<ul>
  <li>R1, R2 fixes</li>
  <li>R3, R4 varient avec la deformation</li>
  <li>Tension de sortie proportionnelle a la variation de resistance</li>
  <li>Amplificateur d'instrumentation amplifie cette faible difference (quelques mV)</li>
</ul>

<h3 class="section-title">4. Techniques de Conditionnement</h3>

<p><strong>Conversion tension-courant</strong> :</p>
<p>Source de courant controlee en tension (VCCS). Utile pour piloter des LEDs ou capteurs 4-20 mA.</p>

<p><strong>Conversion courant-tension (transimpedance)</strong> :</p>
<p>Photodiode &rarr; AOP &rarr; tension. Resistance de contre-reaction definit le gain.</p>

<p><strong>Detecteur de crete</strong> :</p>
<p>Capture la valeur maximale d'un signal. Diode + condensateur + suiveur.</p>

<p><strong>Redresseur de precision</strong> :</p>
<p>Redressement sans seuil de diode (0,6V). L'AOP compense la chute de tension.</p>

<p><strong>Convertisseur RMS-DC</strong> :</p>
<p>Mesure la valeur efficace d'un signal alternatif. Circuit integre dedie (ex : AD536).</p>

<h3 class="section-title">5. Aspects Pratiques de Conception</h3>

<p><strong>Choix de l'AOP</strong> :</p>

<table>
  <thead>
    <tr><th>Application</th><th>AOP recommande</th><th>Criteres</th></tr>
  </thead>
  <tbody>
    <tr><td>Instrumentation de precision</td><td>AD620, INA126</td><td>Faible offset, haut CMRR</td></tr>
    <tr><td>Audio</td><td>NE5532, OPA2134</td><td>Faible bruit, faible distorsion</td></tr>
    <tr><td>Video</td><td>AD8001</td><td>Large bande passante, fort slew rate</td></tr>
    <tr><td>Faible consommation</td><td>LMV321</td><td>Micro-puissance, rail-to-rail</td></tr>
  </tbody>
</table>

<p><strong>Regles de cablage</strong> :</p>
<ul>
  <li>Condensateurs de decouplage 100 nF au plus pres des broches d'alimentation</li>
  <li>Pistes courtes pour minimiser les inductances parasites</li>
  <li>Plan de masse continu</li>
  <li>Separation masses analogique/numerique</li>
</ul>

<p><strong>Compensation des defauts</strong> :</p>
<ul>
  <li>Potentiometre d'ajustage pour compensation d'offset</li>
  <li>Resistance de compensation Rc pour les courants de polarisation</li>
  <li>Choix d'AOP a faible derive thermique pour environnements severes</li>
</ul>

<hr/>

<h2>PART D - Analyse Reflexive et Perspectives</h2>

<h3 class="section-title">Competences acquises</h3>

<p><strong>Analyse de circuits analogiques</strong> :</p>
<p>Ce cours a renforce ma capacite a analyser les circuits reels en tenant compte des imperfections. La difference entre modele ideal et comportement reel est cruciale pour des conceptions fiables.</p>

<p><strong>Mesure et instrumentation</strong> :</p>
<p>Les TPs ont developpe des competences en metrologie : comment mesurer des grandeurs de quelques mV ou nA avec precision, eliminer les parasites, interpreter les resultats.</p>

<p><strong>Conception de filtres</strong> :</p>
<p>La maitrise des filtres actifs est essentielle pour toute chaine d'acquisition. Savoir dimensionner un filtre anti-repliement avant un CAN ou un filtre de reconstruction apres un CAN.</p>

<h3 class="section-title">Points cles a retenir</h3>

<p><strong>1. Rien n'est ideal</strong> :</p>
<p>Les AOPs reels ont des limites (offset, courants, GBP, slew rate). Il faut toujours verifier les datasheets et concevoir en tenant compte des pires cas.</p>

<p><strong>2. Filtres actifs vs passifs</strong> :</p>
<p>Les filtres actifs simplifient les conceptions (pas d'inductances) mais ajoutent des contraintes (alimentation, bruit, bande passante limitee).</p>

<p><strong>3. Importance du conditionnement</strong> :</p>
<p>Dans une chaine d'acquisition, le conditionnement analogique (amplification, filtrage, isolation) est aussi important que la conversion numerique.</p>

<p><strong>4. Compromis performances/cout</strong> :</p>
<p>Un AOP de precision coute 10-100x plus cher qu'un LM358. Il faut adapter le choix a l'application.</p>

<h3 class="section-title">Applications pratiques</h3>

<p><strong>Projet PCB (S6)</strong> :</p>
<p>Les connaissances en filtres actifs ont ete directement appliquees dans le projet PCB pour filtrer les signaux d'entree et eliminer les bruits haute frequence.</p>

<p><strong>Chaines d'acquisition (S8)</strong> :</p>
<p>Ce cours est un prerequis pour comprendre la partie analogique des systemes d'acquisition : filtres anti-repliement, amplificateurs d'instrumentation, isolation galvanique.</p>

<p><strong>Systemes embarques</strong> :</p>
<p>De nombreux capteurs (temperature, pression, acceleration) necessitent un conditionnement analogique avant numerisation par un microcontroleur.</p>

<h3 class="section-title">Limites et ouvertures</h3>

<p><strong>Limites du cours</strong> :</p>
<ul>
  <li>Peu d'aspects numeriques (CAN/CNA) : voir cours Chaines d'Acquisition S8</li>
  <li>Pas de circuits RF haute frequence : voir cours Architectures Analogiques S7</li>
  <li>Peu de circuits de puissance : voir cours Electronique de Puissance</li>
</ul>

<p><strong>Ouvertures vers</strong> :</p>
<ul>
  <li><strong>Circuits integres analogiques</strong> : conception de circuits CMOS analogiques (VLSI)</li>
  <li><strong>Capteurs intelligents</strong> : integration conditionnement + conversion + traitement sur puce</li>
  <li><strong>Systemes mixtes analogique-numerique</strong> : SoC avec parties analogiques et numeriques</li>
  <li><strong>IoT et objets connectes</strong> : circuits ultra-basse consommation pour capteurs autonomes</li>
</ul>

<h3 class="section-title">Conclusion</h3>

<p>L'electronique analogique reste incontournable malgre la predominance du numerique. Tout signal physique (temperature, pression, son, lumiere) est analogique et necessite un conditionnement avant traitement numerique.</p>

<p>Ce cours a permis de comprendre les subtilites des circuits analogiques reels, loin des approximations du modele ideal. La capacite a concevoir des filtres actifs, choisir le bon AOP, et mesurer precisement les defauts est essentielle pour tout ingenieur en systemes embarques ou instrumentation.</p>

<p><strong>Evolution du domaine</strong> :</p>
<ul>
  <li>Miniaturisation continue (circuits integres CMOS)</li>
  <li>Integration analogique/numerique sur meme puce (SoC)</li>
  <li>Ultra-basse consommation pour IoT</li>
  <li>Compensation numerique des defauts analogiques</li>
</ul>

<p><strong>Liens avec les autres cours</strong> :</p>
<ul>
  <li><a href="./circuits-filtres-analogiques.html">Circuits et Filtres Analogiques - S5</a> : fondamentaux</li>
  <li><a href="./filtrage-numerique.html">Filtrage Numerique - S6</a> : complementarite</li>
  <li><a href="./chaines-acquisition.html">Chaines Electroniques d'Acquisition - S8</a> : application complete</li>
</ul>

<hr/>

<h2>Documents de Cours</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>TD Correction</h4>
      <p>Correction des travaux diriges sur les amplificateurs operationnels et les filtres actifs avec methodes detaillees.</p>
      <embed src="/cours-pdf/S6/Elec-Fonctions-Analogiques/td-correction.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Elec-Fonctions-Analogiques/td-correction.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>TP1 - Mesure Defauts AOP</h4>
      <p>Sujet du TP sur la mesure des defauts reels des amplificateurs operationnels : offset, bande passante, slew-rate.</p>
      <embed src="/cours-pdf/S6/Elec-Fonctions-Analogiques/tp1-defauts-aop.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Elec-Fonctions-Analogiques/tp1-defauts-aop.pdf" target="_blank">Telecharger</a></p>
    </div>
  </div>
</div>

<hr/>

<h2>Captures Oscilloscope - TP Electronique Analogique</h2>

<p>Les travaux pratiques ont permis de realiser des mesures a l'oscilloscope sur les filtres actifs et les montages a amplificateurs operationnels. Voici les captures realisees lors des seances.</p>

<div style="text-align: center; margin: 20px 0;">
  <img src="/assets/images/courses/S6/electronique/scope_3.png" alt="Capture oscilloscope - Mesure 3" style="max-width: 600px; border: 1px solid #ddd; padding: 10px; border-radius: 8px;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Capture oscilloscope - Mesure 3</p>
</div>

<div style="text-align: center; margin: 20px 0;">
  <img src="/assets/images/courses/S6/electronique/scope_5.png" alt="Capture oscilloscope - Mesure 5" style="max-width: 600px; border: 1px solid #ddd; padding: 10px; border-radius: 8px;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Capture oscilloscope - Mesure 5</p>
</div>

<div style="text-align: center; margin: 20px 0;">
  <img src="/assets/images/courses/S6/electronique/scope_6.png" alt="Capture oscilloscope - Mesure 6" style="max-width: 600px; border: 1px solid #ddd; padding: 10px; border-radius: 8px;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Capture oscilloscope - Mesure 6</p>
</div>

<div style="text-align: center; margin: 20px 0;">
  <img src="/assets/images/courses/S6/electronique/scope_7.png" alt="Capture oscilloscope - Mesure 7" style="max-width: 600px; border: 1px solid #ddd; padding: 10px; border-radius: 8px;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Capture oscilloscope - Mesure 7</p>
</div>

<hr/>

<h2>Rapports et Projets</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Compte Rendu TP - Electronique et Fonctions Analogiques</h4>
      <p>Rapport de travaux pratiques sur les defauts d'AOP, les filtres actifs Sallen-Key et les mesures a l'oscilloscope.</p>
      <p style="text-align: center;">
        <a href="/file/reports/S6/Compte_Rendu_TP_Electronique_et_fonctions_analogiques_2 (1).pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Telecharger le rapport PDF
        </a>
      </p>
    </div>
  </div>
</div>

<hr/>

<p><em>Cours enseigne en 2022-2023 a l'INSA Toulouse, Departement Genie Electrique et Informatique.</em></p>

</div>

<div class="lang-en">

<h1>Analog Functions Electronics - Semester 6</h1>

<p><strong>Academic Year</strong>: 2022-2023<br/>
<strong>Semester</strong>: 6<br/>
<strong>Credits</strong>: 2 ECTS<br/>
<strong>Specialization</strong>: Electronics and Embedded Systems</p>

<hr/>

<h2>PART A - General Course Overview</h2>

<h3 class="section-title">Overview</h3>

<p>This course deepens the study of advanced analog electronic circuits and functions. The focus is on operational amplifiers (op-amps) and their real-world defects, active filters, and signal conditioning functions. The course combines theory and practice with lab sessions on measuring op-amp imperfections and filter design.</p>

<p><strong>Learning objectives</strong>:</p>
<ul>
  <li>Understand and characterize real defects of operational amplifiers</li>
  <li>Design and analyze active filters (low-pass, high-pass, band-pass)</li>
  <li>Master analog conditioning functions for sensors</li>
  <li>Measure and compensate for analog circuit imperfections</li>
</ul>

<h3 class="section-title">Position in the Curriculum</h3>

<p>This course follows up on previous teachings:</p>
<ul>
  <li><strong>Analog Circuits and Filters (S5)</strong>: RC/RL circuit basics and transfer functions</li>
  <li><strong>Components and Power Concepts (S5)</strong>: transistors and amplification</li>
  <li><strong>Digital Filtering (S6)</strong>: complementarity between analog/digital filters</li>
</ul>

<p>It prepares for advanced courses:</p>
<ul>
  <li><strong>Analog Architectures for Transmission (S7)</strong>: RF chains</li>
  <li><strong>Electronic Acquisition Chains (S8)</strong>: complete data acquisition</li>
</ul>

<hr/>

<h2>PART B - Personal Experience and Learning Context</h2>

<h3 class="section-title">Organization and Resources</h3>

<p>The module was structured in 3 main parts:</p>

<p><strong>1. Lectures</strong>:</p>
<ul>
  <li>Op-amp defects: offset, bias currents, thermal drift</li>
  <li>Active filter structures: Sallen-Key, Rauch, biquads</li>
  <li>Conditioning functions: instrumentation amplifiers, isolation</li>
</ul>

<p><strong>2. Tutorials</strong>:</p>
<ul>
  <li>Error calculations due to op-amp defects</li>
  <li>Active filter sizing (orders 1, 2, 3)</li>
  <li>Closed-loop stability and gain analysis</li>
</ul>

<p><strong>3. Lab sessions</strong>:</p>
<ul>
  <li><strong>Lab 1 - Op-amp defect measurement</strong>: experimental characterization of an LM358</li>
  <li><strong>Lab 2 - Active filters</strong>: building and testing Sallen-Key filters</li>
</ul>

<h3 class="section-title">Lab Session Details</h3>

<p><strong>Lab 1: Measuring Operational Amplifier Defects</strong></p>

<p>The first lab consisted of measuring the imperfections of a real op-amp (LM358):</p>

<table>
  <thead>
    <tr><th>Measured defect</th><th>Method</th><th>Typical value</th></tr>
  </thead>
  <tbody>
    <tr><td>Offset voltage Vos</td><td>Follower circuit, direct measurement</td><td>2-7 mV</td></tr>
    <tr><td>Bias currents Ib+ and Ib-</td><td>High-value resistors at input</td><td>20-100 nA</td></tr>
    <tr><td>Voltage gain Av</td><td>Non-inverting amplifier circuit</td><td>100,000 (100 dB)</td></tr>
    <tr><td>Bandwidth BW</td><td>Frequency response</td><td>1 MHz</td></tr>
    <tr><td>Slew rate SR</td><td>Square wave, rise time measurement</td><td>0.5 V/us</td></tr>
  </tbody>
</table>

<p><strong>Practical procedure</strong>:</p>
<ol>
  <li>Follower circuit for offset: non-zero output even with 0V input</li>
  <li>Adding resistors at inputs to isolate bias currents</li>
  <li>Frequency sweep to determine GBP (Gain-Bandwidth Product)</li>
</ol>

<p><strong>Lab 2: Active Filters</strong></p>

<p>Design and implementation of several filter topologies:</p>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S6/elec-analogique/ampli-op-inverseur.svg" alt="Inverting operational amplifier" style="max-width: 550px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Schematic of an operational amplifier in inverting configuration</p>
</div>

<p><strong>2nd order Sallen-Key low-pass filter</strong>:</p>
<ul>
  <li>Cutoff frequency: 1 kHz</li>
  <li>Structure: two resistors R, two capacitors C, op-amp as follower</li>
  <li>Slope: -40 dB/decade beyond fc</li>
  <li>Advantage: low output impedance, no loading on subsequent stages</li>
</ul>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S6/elec-analogique/oscilloscope-1.png" alt="Oscilloscope measurement 1" style="max-width: 600px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Oscilloscope measurements - Active filter response (Lab)</p>
</div>

<p><strong>2nd order Sallen-Key high-pass filter</strong>:</p>
<ul>
  <li>Same principle with R and C swapped</li>
  <li>Elimination of low-frequency components</li>
</ul>

<p><strong>Oscilloscope observations</strong>:</p>
<ul>
  <li>Verification of attenuation in dB per decade</li>
  <li>Phase shift measurement (90 deg at fc for order 1, 180 deg for order 2)</li>
  <li>Impact of quality factor Q on resonance</li>
</ul>

<h3 class="section-title">Difficulties Encountered</h3>

<p><strong>Parasitics and noise</strong>:</p>
<ul>
  <li>Offset and current measurements were sensitive to 50 Hz mains noise</li>
  <li>Solution: shielding, star grounding, decoupling capacitors</li>
</ul>

<p><strong>Component selection</strong>:</p>
<ul>
  <li>Resistor and capacitor tolerances (5-10%) impacted cutoff frequencies</li>
  <li>Need to use a multimeter to measure actual values</li>
</ul>

<p><strong>Circuit stability</strong>:</p>
<ul>
  <li>Parasitic oscillations due to limited op-amp GBP</li>
  <li>Addition of compensation capacitors</li>
</ul>

<hr/>

<h2>PART C - Detailed Technical Aspects</h2>

<h3 class="section-title">1. Operational Amplifier Defects</h3>

<p>A real op-amp has several imperfections compared to the ideal model:</p>

<p><strong>Offset voltage (Vos)</strong>:</p>
<p>Voltage difference between the inputs to obtain Vout = 0V. Typically 1-10 mV.</p>

<p>Impact on a non-inverting circuit with gain G:</p>
<ul>
  <li>Output error = Vos x G</li>
  <li>Example: Vos = 5 mV, G = 100 &rarr; 500 mV error!</li>
</ul>

<p><strong>Bias currents (Ib+ and Ib-)</strong>:</p>
<p>Input currents required for internal transistor operation. Typically 10-200 nA for an LM358.</p>

<p>Compensation: resistor Rc in series with the non-inverting input</p>
<ul>
  <li>Rc = R1 // R2 (parallel of gain resistors)</li>
</ul>

<p><strong>Offset current (Ios)</strong>:</p>
<p>Difference between Ib+ and Ib-: Ios = |Ib+ - Ib-|</p>

<p><strong>Finite voltage gain (Av)</strong>:</p>
<p>Instead of being infinite, the open-loop gain is limited (typically 100,000 = 100 dB).</p>

<p>Effect on closed-loop gain:</p>
<ul>
  <li>Actual gain slightly lower than theoretical gain</li>
  <li>Important for precision applications</li>
</ul>

<p><strong>Gain-Bandwidth Product (GBP)</strong>:</p>
<p>The gain decreases with frequency. Constant product GBP = Av x BW.</p>
<ul>
  <li>LM358: GBP = 1 MHz</li>
  <li>If desired gain = 100, max BW = 10 kHz</li>
</ul>

<p><strong>Slew Rate (SR)</strong>:</p>
<p>Maximum rate of change of the output voltage. Limited by internal charging currents.</p>
<ul>
  <li>LM358: SR &approx; 0.5 V/us</li>
  <li>Limits the maximum frequency of high-amplitude signals</li>
</ul>

<p><strong>CMRR (Common Mode Rejection Ratio)</strong>:</p>
<p>Ability to reject common-mode signals. Typically 70-100 dB.</p>
<ul>
  <li>Low CMRR &rarr; sensitivity to power supply disturbances</li>
</ul>

<p><strong>PSRR (Power Supply Rejection Ratio)</strong>:</p>
<p>Rejection of power supply variations. Important for battery-powered circuits.</p>

<h3 class="section-title">2. Active Filters</h3>

<p>Active filters use op-amps to achieve transfer functions without inductors.</p>

<p><strong>Advantages over passive filters</strong>:</p>
<ul>
  <li>No inductors (size, cost, non-idealities)</li>
  <li>Gain possible (amplification + filtering)</li>
  <li>Low output impedance</li>
  <li>No loading effect between stages</li>
</ul>

<p><strong>Sallen-Key structure (2nd order low-pass)</strong>:</p>

<p>Typical configuration:</p>
<ul>
  <li>Two resistors R1 = R2 = R</li>
  <li>Two capacitors C1 = C2 = C</li>
  <li>Op-amp in follower configuration (gain = 1)</li>
</ul>

<p>Cutoff frequency: fc = 1 / (2pi x R x C)</p>

<p>Transfer function: H(p) = 1 / (1 + a1 x p + a2 x p²)</p>
<ul>
  <li>a1 and a2 depend on the quality factor Q</li>
  <li>Q = 0.707 for Butterworth response (maximally flat)</li>
</ul>

<p><strong>2nd order high-pass filter</strong>:</p>
<p>Swapping R and C positions compared to the low-pass.</p>

<p><strong>Band-pass filter</strong>:</p>
<p>Cascade of a high-pass and a low-pass, or Rauch structure.</p>
<ul>
  <li>Bandwidth: f1 &lt; f &lt; f2</li>
  <li>Quality factor: Q = f0 / (f2 - f1)</li>
</ul>

<p><strong>Band-stop filter (notch)</strong>:</p>
<p>Attenuates a frequency band (e.g., eliminating 50 Hz mains).</p>

<p><strong>Higher-order filters</strong>:</p>
<p>Cascade of multiple 2nd order cells (biquads).</p>
<ul>
  <li>Order 4: two 2nd order cells &rarr; -80 dB/decade slope</li>
  <li>Each cell has its own Q to achieve the desired overall response</li>
</ul>

<p><strong>Response types</strong>:</p>
<ul>
  <li><strong>Butterworth</strong>: maximally flat in the passband</li>
  <li><strong>Chebyshev</strong>: passband ripple, sharper cutoff</li>
  <li><strong>Bessel</strong>: linear phase response, no temporal distortion</li>
</ul>

<h3 class="section-title">3. Instrumentation Amplifiers</h3>

<p>Specialized circuits for precision sensor measurements.</p>

<p><strong>Characteristics</strong>:</p>
<ul>
  <li>High and stable differential gain</li>
  <li>Very high input impedance (&gt; 1 GOhm)</li>
  <li>Very high CMRR (&gt; 100 dB)</li>
  <li>Low thermal drift</li>
</ul>

<p><strong>Classic 3 op-amp structure</strong>:</p>
<ul>
  <li>Input stage: two op-amps in non-inverting configuration</li>
  <li>Output stage: differential amplifier</li>
  <li>Gain adjustable by a single external resistor</li>
</ul>

<p><strong>Applications</strong>:</p>
<ul>
  <li>Wheatstone bridges (strain gauges)</li>
  <li>Thermocouples</li>
  <li>Biomedical measurements (ECG, EEG)</li>
</ul>

<p><strong>Example: Wheatstone bridge</strong></p>

<p>Strain gauge sensor with 4 resistors:</p>
<ul>
  <li>R1, R2 fixed</li>
  <li>R3, R4 vary with deformation</li>
  <li>Output voltage proportional to resistance change</li>
  <li>Instrumentation amplifier amplifies this small difference (a few mV)</li>
</ul>

<h3 class="section-title">4. Conditioning Techniques</h3>

<p><strong>Voltage-to-current conversion</strong>:</p>
<p>Voltage-controlled current source (VCCS). Useful for driving LEDs or 4-20 mA sensors.</p>

<p><strong>Current-to-voltage conversion (transimpedance)</strong>:</p>
<p>Photodiode &rarr; op-amp &rarr; voltage. Feedback resistor defines the gain.</p>

<p><strong>Peak detector</strong>:</p>
<p>Captures the maximum value of a signal. Diode + capacitor + follower.</p>

<p><strong>Precision rectifier</strong>:</p>
<p>Rectification without diode threshold (0.6V). The op-amp compensates for the voltage drop.</p>

<p><strong>RMS-to-DC converter</strong>:</p>
<p>Measures the RMS value of an AC signal. Dedicated integrated circuit (e.g., AD536).</p>

<h3 class="section-title">5. Practical Design Aspects</h3>

<p><strong>Op-amp selection</strong>:</p>

<table>
  <thead>
    <tr><th>Application</th><th>Recommended op-amp</th><th>Criteria</th></tr>
  </thead>
  <tbody>
    <tr><td>Precision instrumentation</td><td>AD620, INA126</td><td>Low offset, high CMRR</td></tr>
    <tr><td>Audio</td><td>NE5532, OPA2134</td><td>Low noise, low distortion</td></tr>
    <tr><td>Video</td><td>AD8001</td><td>Wide bandwidth, high slew rate</td></tr>
    <tr><td>Low power</td><td>LMV321</td><td>Micro-power, rail-to-rail</td></tr>
  </tbody>
</table>

<p><strong>Wiring rules</strong>:</p>
<ul>
  <li>100 nF decoupling capacitors as close as possible to power supply pins</li>
  <li>Short traces to minimize parasitic inductances</li>
  <li>Continuous ground plane</li>
  <li>Separate analog/digital grounds</li>
</ul>

<p><strong>Defect compensation</strong>:</p>
<ul>
  <li>Trimming potentiometer for offset compensation</li>
  <li>Compensation resistor Rc for bias currents</li>
  <li>Choosing low thermal drift op-amps for harsh environments</li>
</ul>

<hr/>

<h2>PART D - Reflective Analysis and Perspectives</h2>

<h3 class="section-title">Acquired Skills</h3>

<p><strong>Analog circuit analysis</strong>:</p>
<p>This course strengthened my ability to analyze real circuits while accounting for imperfections. The difference between ideal model and real behavior is crucial for reliable designs.</p>

<p><strong>Measurement and instrumentation</strong>:</p>
<p>The lab sessions developed metrology skills: how to accurately measure quantities of a few mV or nA, eliminate parasites, and interpret results.</p>

<p><strong>Filter design</strong>:</p>
<p>Mastering active filters is essential for any acquisition chain. Knowing how to size an anti-aliasing filter before an ADC or a reconstruction filter after a DAC.</p>

<h3 class="section-title">Key Takeaways</h3>

<p><strong>1. Nothing is ideal</strong>:</p>
<p>Real op-amps have limitations (offset, currents, GBP, slew rate). One must always check datasheets and design for worst-case scenarios.</p>

<p><strong>2. Active vs passive filters</strong>:</p>
<p>Active filters simplify designs (no inductors) but add constraints (power supply, noise, limited bandwidth).</p>

<p><strong>3. Importance of conditioning</strong>:</p>
<p>In an acquisition chain, analog conditioning (amplification, filtering, isolation) is as important as digital conversion.</p>

<p><strong>4. Performance/cost trade-offs</strong>:</p>
<p>A precision op-amp costs 10-100x more than an LM358. The choice must be adapted to the application.</p>

<h3 class="section-title">Practical Applications</h3>

<p><strong>PCB Project (S6)</strong>:</p>
<p>Active filter knowledge was directly applied in the PCB project to filter input signals and eliminate high-frequency noise.</p>

<p><strong>Acquisition chains (S8)</strong>:</p>
<p>This course is a prerequisite for understanding the analog portion of acquisition systems: anti-aliasing filters, instrumentation amplifiers, galvanic isolation.</p>

<p><strong>Embedded systems</strong>:</p>
<p>Many sensors (temperature, pressure, acceleration) require analog conditioning before digitization by a microcontroller.</p>

<h3 class="section-title">Limitations and Future Directions</h3>

<p><strong>Course limitations</strong>:</p>
<ul>
  <li>Few digital aspects (ADC/DAC): see Acquisition Chains S8 course</li>
  <li>No high-frequency RF circuits: see Analog Architectures S7 course</li>
  <li>Few power circuits: see Power Electronics course</li>
</ul>

<p><strong>Future directions</strong>:</p>
<ul>
  <li><strong>Analog integrated circuits</strong>: CMOS analog circuit design (VLSI)</li>
  <li><strong>Smart sensors</strong>: integration of conditioning + conversion + processing on-chip</li>
  <li><strong>Mixed analog-digital systems</strong>: SoC with analog and digital parts</li>
  <li><strong>IoT and connected objects</strong>: ultra-low-power circuits for autonomous sensors</li>
</ul>

<h3 class="section-title">Conclusion</h3>

<p>Analog electronics remains indispensable despite the predominance of digital technology. Every physical signal (temperature, pressure, sound, light) is analog and requires conditioning before digital processing.</p>

<p>This course provided an understanding of the subtleties of real analog circuits, far from ideal model approximations. The ability to design active filters, choose the right op-amp, and accurately measure defects is essential for any engineer in embedded systems or instrumentation.</p>

<p><strong>Field evolution</strong>:</p>
<ul>
  <li>Ongoing miniaturization (CMOS integrated circuits)</li>
  <li>Analog/digital integration on the same chip (SoC)</li>
  <li>Ultra-low power consumption for IoT</li>
  <li>Digital compensation of analog defects</li>
</ul>

<p><strong>Links with other courses</strong>:</p>
<ul>
  <li><a href="./circuits-filtres-analogiques.html">Analog Circuits and Filters - S5</a>: fundamentals</li>
  <li><a href="./filtrage-numerique.html">Digital Filtering - S6</a>: complementarity</li>
  <li><a href="./chaines-acquisition.html">Electronic Acquisition Chains - S8</a>: complete application</li>
</ul>

<hr/>

<h2>Course Documents</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Tutorial Correction</h4>
      <p>Correction of tutorials on operational amplifiers and active filters with detailed methods.</p>
      <embed src="/cours-pdf/S6/Elec-Fonctions-Analogiques/td-correction.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Elec-Fonctions-Analogiques/td-correction.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>Lab 1 - Op-Amp Defect Measurement</h4>
      <p>Lab assignment on measuring real operational amplifier defects: offset, bandwidth, slew rate.</p>
      <embed src="/cours-pdf/S6/Elec-Fonctions-Analogiques/tp1-defauts-aop.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Elec-Fonctions-Analogiques/tp1-defauts-aop.pdf" target="_blank">Download</a></p>
    </div>
  </div>
</div>

<hr/>

<h2>Oscilloscope Captures - Analog Electronics Lab</h2>

<p>The lab sessions allowed oscilloscope measurements on active filters and operational amplifier circuits. Here are the captures taken during the sessions.</p>

<div style="text-align: center; margin: 20px 0;">
  <img src="/assets/images/courses/S6/electronique/scope_3.png" alt="Oscilloscope capture - Measurement 3" style="max-width: 600px; border: 1px solid #ddd; padding: 10px; border-radius: 8px;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Oscilloscope capture - Measurement 3</p>
</div>

<div style="text-align: center; margin: 20px 0;">
  <img src="/assets/images/courses/S6/electronique/scope_5.png" alt="Oscilloscope capture - Measurement 5" style="max-width: 600px; border: 1px solid #ddd; padding: 10px; border-radius: 8px;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Oscilloscope capture - Measurement 5</p>
</div>

<div style="text-align: center; margin: 20px 0;">
  <img src="/assets/images/courses/S6/electronique/scope_6.png" alt="Oscilloscope capture - Measurement 6" style="max-width: 600px; border: 1px solid #ddd; padding: 10px; border-radius: 8px;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Oscilloscope capture - Measurement 6</p>
</div>

<div style="text-align: center; margin: 20px 0;">
  <img src="/assets/images/courses/S6/electronique/scope_7.png" alt="Oscilloscope capture - Measurement 7" style="max-width: 600px; border: 1px solid #ddd; padding: 10px; border-radius: 8px;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Oscilloscope capture - Measurement 7</p>
</div>

<hr/>

<h2>Reports and Projects</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Lab Report - Electronics and Analog Functions</h4>
      <p>Lab report on op-amp defects, Sallen-Key active filters and oscilloscope measurements.</p>
      <p style="text-align: center;">
        <a href="/file/reports/S6/Compte_Rendu_TP_Electronique_et_fonctions_analogiques_2 (1).pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Download PDF report
        </a>
      </p>
    </div>
  </div>
</div>

<hr/>

<p><em>Course taught in 2022-2023 at INSA Toulouse, Department of Electrical Engineering and Computer Science.</em></p>

</div>

<style>
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

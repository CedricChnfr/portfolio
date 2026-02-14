---
layout: default
title: "Filtrage Actif et Modélisation Sources Bruit - S7"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
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
    <a href="./my-courses-2023-2024.html" data-i18n-html="back-courses-2023-2024">&larr; Retour aux Cours 2023-2024</a>
</div>

<div class="lang-fr">

<h1>Filtrage Actif et Modelisation Sources Bruit - Semestre 7</h1>

<p><strong>Annee Universitaire</strong> : 2023-2024<br/>
<strong>Semestre</strong> : 7<br/>
<strong>Credits</strong> : 2.5 ECTS<br/>
<strong>Specialite</strong> : Electronique Analogique et Traitement du Signal</p>

<hr/>

<h2>PART A - Presentation Generale du Module</h2>

<h3 class="section-title">Vue d'ensemble</h3>

<p>Ce cours traite deux aspects fondamentaux de l'electronique analogique : la conception de filtres actifs avec amplificateurs operationnels (AOP) et amplificateurs a transconductance operationnels (OTA), et l'analyse du bruit dans les circuits electroniques. Ces competences sont essentielles pour concevoir des chaines d'acquisition de signaux haute performance.</p>

<p><strong>Objectifs pedagogiques</strong> :</p>
<ul>
<li>Concevoir et synthetiser des filtres actifs d'ordre eleve</li>
<li>Maitriser les topologies Sallen-Key, Rauch, et capacites commutees</li>
<li>Comprendre les sources physiques de bruit electronique</li>
<li>Modeliser et calculer le bruit dans les circuits</li>
<li>Optimiser le rapport signal sur bruit (SNR)</li>
<li>Analyser les performances de chaines d'acquisition</li>
</ul>

<h3 class="section-title">Position dans le cursus</h3>

<p>Ce module s'appuie sur :</p>
<ul>
<li><strong>Circuits et Filtres analogiques (S5)</strong> : filtres passifs, fonction de transfert</li>
<li><strong>Filtrage numerique (S6)</strong> : theorie du filtrage, approximations</li>
<li><strong>Etude et Modelisation Composants Actifs (S7)</strong> : amplificateurs operationnels</li>
</ul>

<p>Il prepare a :</p>
<ul>
<li><strong>Chaines electroniques acquisition (S8)</strong> : conditionnement de capteurs</li>
<li><strong>Processus stochastiques et files d'attente (S8)</strong> : modelisation probabiliste</li>
<li><strong>Traitement du signal avance</strong> : filtrage optimal, detection</li>
<li><strong>Conception de systemes d'instrumentation</strong> : mesures de precision</li>
</ul>

<hr/>

<h2>PART B - Experience Personnelle et Contexte d'Apprentissage</h2>

<h3 class="section-title">Organisation et ressources</h3>

<p>Le module etait divise en plusieurs volets thematiques :</p>

<p><strong>Cours magistraux (20h)</strong> :</p>
<p>Organises en 4 grandes parties :</p>
<ul>
<li>Partie 1 : Amplificateurs operationnels et OTA (dossier 1_AO_OTA)
<ul>
<li>Bruit interne des AOP</li>
<li>OTA CA3080 (amplificateur a transconductance)</li>
</ul>
</li>
<li>Partie 2 : Architecture electronique et filtres actifs (dossier 3_Archi_Elec_Filtre_Actif)
<ul>
<li>Gabarits et synthese de filtres</li>
<li>Topologies Sallen-Key et Rauch</li>
<li>Association de cellules d'ordre 2</li>
</ul>
</li>
<li>Partie 3 : Capacites commutees (dossier 4_Capa_Commute)
<ul>
<li>Principe et applications</li>
</ul>
</li>
<li>Partie 4 : Document de synthese (4AESE-filtrage4AE_2020-2021.pdf)</li>
</ul>

<p><strong>Travaux diriges (12h)</strong> :</p>
<ul>
<li>TD1 a TD6 avec corrections disponibles</li>
<li>Exercices de synthese de filtres</li>
<li>Calculs de bruit dans circuits</li>
<li>Dimensionnement de chaines d'acquisition</li>
</ul>

<p><strong>Evaluations</strong> :</p>
<ul>
<li>Annales disponibles (2016-2022) avec corrections</li>
<li>Examen portant sur filtrage ET bruit</li>
<li>Projet de conception de filtre</li>
</ul>

<p><strong>Outils utilises</strong> :</p>
<ul>
<li>SPICE (simulation circuits, analyse bruit)</li>
<li>MATLAB/Octave (synthese de filtres, calculs)</li>
<li>Analyseur de spectre (mesure bruit)</li>
<li>Oscilloscope numerique</li>
</ul>

<h3 class="section-title">Methodologie d'etude</h3>

<p><strong>Phase 1 : Specifications du filtre</strong> :</p>
<p>Definir le gabarit (frequences de coupure, ondulation, attenuation en bande coupee) selon l'application.</p>

<p><strong>Phase 2 : Choix de l'approximation</strong> :</p>
<p>Selectionner Butterworth, Chebyshev, Bessel, ou Elliptique selon le compromis selectivite/phase/temps.</p>

<p><strong>Phase 3 : Synthese de la fonction de transfert</strong> :</p>
<p>Utiliser tables ou logiciels pour obtenir les poles et zeros. Decomposer en cellules d'ordre 2.</p>

<p><strong>Phase 4 : Implementation electronique</strong> :</p>
<p>Choisir la topologie (Sallen-Key, Rauch) et calculer les composants (R, C) pour chaque cellule.</p>

<p><strong>Phase 5 : Analyse du bruit</strong> :</p>
<p>Calculer les contributions de bruit de chaque composant et AOP, puis le bruit total ramene en entree.</p>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S7/filtrage-actif/capacites-commutees.svg" alt="Filtre a capacites commutees" style="max-width: 550px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Principe des filtres a capacites commutees - Emulation de resistance par commutation</p>
</div>

<p><strong>Phase 6 : Simulation et validation</strong> :</p>
<p>Verifier la reponse frequentielle, le bruit, et les limitations pratiques (saturation, slew-rate).</p>

<h3 class="section-title">Difficultes rencontrees</h3>

<p><strong>Synthese de filtres d'ordre eleve</strong> :</p>
<p>Cascader plusieurs cellules du 2e ordre necessite de gerer les interactions, l'ordre des sections, et les niveaux de signaux inter-etages.</p>

<p><strong>Valeurs de composants</strong> :</p>
<p>Les calculs theoriques donnent souvent des valeurs non standard (resistances, capacites). Il faut ajuster avec les series E12/E24/E96.</p>

<p><strong>Analyse du bruit</strong> :</p>
<p>Identifier toutes les sources de bruit (resistances, AOP, alimentations), calculer leur contribution ramenee en entree, puis integrer sur la bande passante demande rigueur.</p>

<p><strong>Bruit en 1/f</strong> :</p>
<p>La densite spectrale n'est pas constante, ce qui complique les calculs d'integration. Necessite de connaitre la frequence de coin.</p>

<hr/>

<h2>PART C - Aspects Techniques Detailles</h2>

<h3 class="section-title">1. Amplificateurs operationnels et bruit interne</h3>

<p><strong>Modele de bruit d'un AOP</strong> :</p>

<p>Trois sources de bruit equivalentes en entree :</p>
<ul>
<li><strong>en</strong> : tension de bruit en entree (nV/racine(Hz))</li>
<li><strong>in+</strong> : courant de bruit entree non-inverseuse (pA/racine(Hz))</li>
<li><strong>in-</strong> : courant de bruit entree inverseuse (pA/racine(Hz))</li>
</ul>

<p><strong>Densite spectrale de bruit en tension</strong> :</p>

<p>Typiquement :</p>
<ul>
<li>AOP bipolaire : en = 1-10 nV/racine(Hz)</li>
<li>AOP JFET : en = 5-20 nV/racine(Hz)</li>
<li>AOP precision : en &lt; 5 nV/racine(Hz)</li>
</ul>

<p><strong>Densite spectrale de bruit en courant</strong> :</p>

<p>Typiquement :</p>
<ul>
<li>AOP bipolaire : in = 1-10 pA/racine(Hz)</li>
<li>AOP JFET : in = 0.01-1 pA/racine(Hz) (tres faible)</li>
</ul>

<p><strong>Bruit en 1/f</strong> :</p>

<p>Frequence de coin fc (transition entre bruit en 1/f et bruit blanc) :</p>
<ul>
<li>AOP bipolaire : fc = 10-100 Hz</li>
<li>AOP JFET : fc = 100-1000 Hz</li>
</ul>

<p><strong>OTA (Operational Transconductance Amplifier)</strong> :</p>

<p>Exemple : CA3080</p>
<ul>
<li>Sortie en courant (transconductance gm reglable)</li>
<li>Applications : VCA, VCF, multiplieurs</li>
<li>Bruit typiquement plus eleve que AOP classiques</li>
</ul>

<h3 class="section-title">2. Sources fondamentales de bruit</h3>

<p><strong>Bruit thermique (Johnson-Nyquist)</strong> :</p>

<p>Origine : agitation thermique des porteurs de charge dans les resistances.</p>

<p>Tension de bruit RMS :</p>
<p>Vn = racine(4 x k x T x R x Df)</p>

<p>avec :</p>
<ul>
<li>k = 1.38 x 10^-23 J/K (constante de Boltzmann)</li>
<li>T : temperature absolue (Kelvin)</li>
<li>R : resistance (Ohms)</li>
<li>Df : bande passante (Hz)</li>
</ul>

<p>Densite spectrale (spectre blanc) :</p>
<p>Sn(f) = 4 x k x T x R (V^2/Hz)</p>

<p><strong>Exemples a 25 deg C (T=298K)</strong> :</p>

<table>
<tr><th>Resistance</th><th>Bruit (nV/racine(Hz))</th></tr>
<tr><td>1 kOhm</td><td>4.1</td></tr>
<tr><td>10 kOhm</td><td>13</td></tr>
<tr><td>100 kOhm</td><td>41</td></tr>
<tr><td>1 MOhm</td><td>130</td></tr>
</table>

<p><strong>Bruit de grenaille (shot noise)</strong> :</p>

<p>Origine : nature discrete du courant electrique (quantification des electrons).</p>

<p>Courant de bruit RMS :</p>
<p>In = racine(2 x q x I x Df)</p>

<p>avec :</p>
<ul>
<li>q = 1.6 x 10^-19 C (charge electron)</li>
<li>I : courant moyen (A)</li>
</ul>

<p>Observe dans jonctions PN (diodes, transistors), tubes, photodetecteurs.</p>

<p><strong>Bruit en 1/f (flicker noise)</strong> :</p>

<p>Origine : defauts cristallins, recombinaisons de surface.</p>

<p>Densite spectrale :</p>
<p>Sn(f) = K / f</p>

<p>Dominant a basse frequence (&lt; 1 kHz typiquement).</p>

<p>Frequence de coin fc : transition vers bruit blanc.</p>

<p><strong>Comparaison des bruits</strong> :</p>

<table>
<tr><th>Type</th><th>Spectre</th><th>Amplitude</th><th>Dominant</th></tr>
<tr><td>Thermique</td><td>Blanc</td><td>4kTR</td><td>Toutes frequences</td></tr>
<tr><td>Grenaille</td><td>Blanc</td><td>2qI</td><td>Jonctions actives</td></tr>
<tr><td>1/f</td><td>Rose (1/f)</td><td>Variable</td><td>Basses frequences</td></tr>
</table>

<h3 class="section-title">3. Topologies de filtres actifs</h3>

<p><strong>Filtre Sallen-Key (VCVS)</strong> :</p>

<p>Configuration non-inverseuse avec gain K.</p>

<p><strong>Passe-bas du 2e ordre</strong> :</p>

<p>Composants : R1, R2, C1, C2, AOP en suiveur ou amplificateur.</p>

<p>Fonction de transfert generale :</p>
<p>H(s) = K x w0^2 / (s^2 + (w0/Q) x s + w0^2)</p>

<p>avec :</p>
<ul>
<li>w0 : pulsation propre (frequence de coupure)</li>
<li>Q : facteur de qualite (inverse de l'amortissement)</li>
<li>K : gain en bande passante</li>
</ul>

<p><strong>Avantages</strong> :</p>
<ul>
<li>Simple (peu de composants)</li>
<li>Gain possible en bande passante</li>
<li>Haute impedance d'entree</li>
</ul>

<p><strong>Inconvenients</strong> :</p>
<ul>
<li>Sensibilite aux composants pour Q eleve</li>
<li>Stabilite limitee si Q &gt; 10</li>
</ul>

<p><strong>Filtre Rauch (structure inverseuse)</strong> :</p>

<p>Configuration inverseuse avec gain negatif en bande passante.</p>

<p><strong>Avantages</strong> :</p>
<ul>
<li>Meilleure stabilite pour Q eleve</li>
<li>Moins sensible aux variations de composants</li>
</ul>

<p><strong>Inconvenients</strong> :</p>
<ul>
<li>Impedance d'entree plus faible</li>
<li>Gain negatif (peut necessiter un etage inverseur additionnel)</li>
</ul>

<p><strong>Comparaison</strong> :</p>

<table>
<tr><th>Critere</th><th>Sallen-Key</th><th>Rauch</th></tr>
<tr><td>Nombre composants</td><td>4 passifs + AOP</td><td>5 passifs + AOP</td></tr>
<tr><td>Impedance entree</td><td>Haute</td><td>Moyenne/Faible</td></tr>
<tr><td>Gain bande passante</td><td>Positif</td><td>Negatif</td></tr>
<tr><td>Stabilite Q eleve</td><td>Limitee</td><td>Meilleure</td></tr>
<tr><td>Usage</td><td>Polyvalent</td><td>Q &gt; 5</td></tr>
</table>

<h3 class="section-title">4. Approximations de filtres</h3>

<p><strong>Butterworth (Maximally Flat)</strong> :</p>

<p>Caracteristiques :</p>
<ul>
<li>Reponse en amplitude la plus plate possible en bande passante</li>
<li>Pas d'ondulation</li>
<li>Attenuation : 20 x n dB/decade (n = ordre du filtre)</li>
<li>Reponse en phase non-lineaire</li>
</ul>

<p>Applications : usage general, audio (reponse douce).</p>

<p><strong>Chebyshev Type I</strong> :</p>

<p>Caracteristiques :</p>
<ul>
<li>Ondulation en bande passante (ripple controle, ex : 0.5 dB, 1 dB, 3 dB)</li>
<li>Pente plus raide que Butterworth a ordre egal</li>
<li>Transition rapide</li>
</ul>

<p>Applications : anti-aliasing, filtres selectifs.</p>

<p><strong>Chebyshev Type II (Inverse)</strong> :</p>

<p>Caracteristiques :</p>
<ul>
<li>Ondulation en bande attenuee</li>
<li>Bande passante plate</li>
<li>Zeros de transmission (attenuation finie)</li>
</ul>

<p>Applications : moins courant, compromis.</p>

<p><strong>Bessel (Thomson)</strong> :</p>

<p>Caracteristiques :</p>
<ul>
<li>Reponse en phase lineaire</li>
<li>Delai de groupe constant (pas de distorsion de phase)</li>
<li>Attenuation douce (pente faible)</li>
</ul>

<p>Applications : video, impulsions (preservation de forme temporelle).</p>

<p><strong>Elliptique (Cauer)</strong> :</p>

<p>Caracteristiques :</p>
<ul>
<li>Ondulation en bande passante ET en bande attenuee</li>
<li>Pente la plus raide pour un ordre donne</li>
<li>Complexite de conception (zeros de transmission)</li>
</ul>

<p>Applications : telecommunications (selectivite maximale).</p>

<p><strong>Tableau recapitulatif</strong> :</p>

<table>
<tr><th>Type</th><th>Bande passante</th><th>Pente</th><th>Phase</th><th>Application</th></tr>
<tr><td>Butterworth</td><td>Plate</td><td>Moyenne</td><td>Non-lineaire</td><td>Usage general</td></tr>
<tr><td>Chebyshev I</td><td>Ondulation</td><td>Raide</td><td>Fortement non-lineaire</td><td>Anti-aliasing</td></tr>
<tr><td>Chebyshev II</td><td>Plate</td><td>Raide</td><td>Non-lineaire</td><td>Compromis</td></tr>
<tr><td>Bessel</td><td>Plate</td><td>Douce</td><td>Lineaire</td><td>Video, impulsions</td></tr>
<tr><td>Elliptique</td><td>Ondulation</td><td>Tres raide</td><td>Fortement non-lineaire</td><td>Telecom</td></tr>
</table>

<h3 class="section-title">5. Synthese de filtres d'ordre eleve</h3>

<p><strong>Decomposition en cascade</strong> :</p>

<p>Un filtre d'ordre n est realise par cascade de cellules :</p>
<ul>
<li>Ordre pair : n/2 cellules du 2e ordre</li>
<li>Ordre impair : (n-1)/2 cellules du 2e ordre + 1 cellule du 1er ordre</li>
</ul>

<p>Fonction de transfert totale :</p>
<p>H(s) = H1(s) x H2(s) x ... x Hk(s)</p>

<p><strong>Parametres de chaque cellule</strong> :</p>

<p>Chaque cellule du 2e ordre a ses propres :</p>
<ul>
<li>Frequence propre w0i</li>
<li>Facteur de qualite Qi</li>
<li>Gain Ki</li>
</ul>

<p><strong>Exemple : Butterworth ordre 5</strong> :</p>

<p>Decomposition : 2 cellules du 2e ordre + 1 cellule du 1er ordre</p>

<p>Cellule 1 : Q1 = 0.618, w01 = wc<br/>
Cellule 2 : Q2 = 1.618, w02 = wc<br/>
Cellule 3 : pole reel a -wc</p>

<p><strong>Ordre des sections</strong> :</p>

<p>Principe general :</p>
<ol>
<li>Placer les sections a Q eleve en fin de cascade (apres attenuation)</li>
<li>Eviter la saturation des premiers etages</li>
<li>Minimiser l'accumulation de bruit</li>
</ol>

<p><strong>Normalisation et denormalisation</strong> :</p>

<p>Etapes :</p>
<ol>
<li>Synthese normalisee (wc = 1 rad/s, R = 1 Ohm)</li>
<li>Tables de coefficients pour approximations standard</li>
<li>Denormalisation : mise a l'echelle en frequence et impedance</li>
</ol>

<p>Formules de denormalisation :</p>
<ul>
<li>Resistance : R_reel = R_normalise x Z0</li>
<li>Capacite : C_reel = C_normalise / (Z0 x wc)</li>
</ul>

<h3 class="section-title">6. Filtres a capacites commutees</h3>

<p><strong>Principe</strong> :</p>

<p>Une resistance est simulee par commutation periodique d'une capacite.</p>

<p>Resistance equivalente :</p>
<p>Req = T / C = 1 / (f x C)</p>

<p>avec :</p>
<ul>
<li>T : periode d'horloge</li>
<li>f : frequence d'horloge</li>
<li>C : capacite commutee</li>
</ul>

<p><strong>Avantages</strong> :</p>
<ul>
<li>Precision determinee par rapports de capacites (excellente en CI)</li>
<li>Pas de resistances (gain de surface en integration)</li>
<li>Accordabilite via frequence d'horloge</li>
<li>Faible sensibilite aux variations process</li>
</ul>

<p><strong>Limitations</strong> :</p>
<ul>
<li>Necessite horloge (bruit d'horloge)</li>
<li>Theoreme d'echantillonnage : f_horloge &gt;&gt; 2 x f_signal</li>
<li>Typiquement : f_horloge = 50 a 100 x f_coupure</li>
</ul>

<p><strong>Applications</strong> :</p>
<ul>
<li>Filtres anti-aliasing dans ADC</li>
<li>Filtres de reconstruction dans DAC</li>
<li>Egaliseurs audio programmables</li>
<li>Circuits integres mixtes (analog/digital)</li>
</ul>

<p><strong>Exemple commercial</strong> :</p>

<p>MAX7400 (Maxim) : filtre passe-bas 8e ordre Butterworth a capacites commutees, frequence de coupure programmable par horloge.</p>

<h3 class="section-title">7. Analyse du bruit dans un amplificateur</h3>

<p><strong>Amplificateur non-inverseur</strong> :</p>

<p>Configuration :</p>
<ul>
<li>Gain Av = 1 + (R2 / R1)</li>
<li>Entree : source de signal Vs avec impedance Rs</li>
</ul>

<p><strong>Sources de bruit</strong> :</p>

<ol>
<li>Bruit de la source : Vn_source = racine(4kTRs)</li>
<li>Bruit thermique R1 : Vn_R1 = racine(4kTR1)</li>
<li>Bruit thermique R2 : Vn_R2 = racine(4kTR2)</li>
<li>Bruit en tension AOP : en</li>
<li>Bruit en courant AOP x impedances : in x (Rs // (R1+R2))</li>
</ol>

<p><strong>Bruit total ramene en entree (RTI)</strong> :</p>

<p>Vn_total^2 = Vn_source^2 + en^2 + (in x Rs)^2 + (Vn_R1 / Av)^2 + (Vn_R2 / Av)^2</p>

<p><strong>Bruit de sortie</strong> :</p>

<p>Vn_out = Vn_total x Av</p>

<p><strong>Optimisation</strong> :</p>
<ul>
<li>Minimiser Rs (resistance de source faible)</li>
<li>Choisir R1, R2 raisonnables (compromis bruit/consommation)</li>
<li>Selectionner AOP avec en et in faibles</li>
<li>Technologies : bipolaire (faible en), JFET (faible in)</li>
</ul>

<h3 class="section-title">8. Facteur de bruit et SNR</h3>

<p><strong>Rapport Signal sur Bruit (SNR)</strong> :</p>

<p>SNR = Puissance_signal / Puissance_bruit</p>

<p>En dB :</p>
<p>SNR_dB = 10 x log10(Psignal / Pbruit)</p>

<p>ou en tensions RMS :</p>
<p>SNR_dB = 20 x log10(Vsignal_RMS / Vbruit_RMS)</p>

<p><strong>Facteur de bruit (F)</strong> :</p>

<p>Degradation du SNR par un systeme :</p>

<p>F = SNR_entree / SNR_sortie</p>

<p><strong>Figure de bruit (NF)</strong> :</p>

<p>NF_dB = 10 x log10(F)</p>

<p>Un systeme ideal (sans bruit ajoute) a F = 1, NF = 0 dB.</p>

<p><strong>Temperature de bruit equivalente</strong> :</p>

<p>Te = T0 x (F - 1)</p>

<p>avec T0 = 290 K (temperature de reference).</p>

<p><strong>Formule de Friis (cascade de systemes)</strong> :</p>

<p>Pour n etages en cascade :</p>

<p>F_total = F1 + (F2 - 1)/G1 + (F3 - 1)/(G1xG2) + ... + (Fn - 1)/(G1xG2x...xGn-1)</p>

<p>avec Fi : facteur de bruit de l'etage i, Gi : gain en puissance de l'etage i.</p>

<p><strong>Implications pratiques</strong> :</p>
<ul>
<li>Le premier etage domine le bruit total</li>
<li>Un gain eleve du premier etage reduit l'impact des suivants</li>
<li>Preamplificateur faible bruit (LNA) crucial en tete de chaine</li>
<li>Applications : recepteurs radio, instrumentation</li>
</ul>

<h3 class="section-title">9. Techniques de reduction du bruit</h3>

<p><strong>Au niveau conception circuit</strong> :</p>

<p><strong>Minimiser les impedances</strong> :</p>
<p>Les resistances generent du bruit thermique. Utiliser des valeurs raisonnables (1-100 kOhm typiquement).</p>

<p><strong>Choisir le bon AOP</strong> :</p>
<ul>
<li>Application basse impedance de source : minimiser en</li>
<li>Application haute impedance de source : minimiser in</li>
<li>Compromis vitesse/bruit (AOP rapides souvent plus bruyants)</li>
</ul>

<p><strong>Filtrage adapte</strong> :</p>
<p>Limiter la bande passante au strict necessaire reduit le bruit integre.</p>

<p><strong>Blindage et garde</strong> :</p>
<p>Reduire les interferences electromagnetiques externes.</p>

<p><strong>Alimentation propre</strong> :</p>
<p>Decouplage soigne, regulateurs faible bruit, filtrage secteur.</p>

<p><strong>Au niveau systeme</strong> :</p>

<p><strong>Filtrage optimal</strong> :</p>
<p>Filtre adapte (matched filter) maximise le SNR pour un signal connu dans du bruit blanc.</p>

<p><strong>Moyennage</strong> :</p>
<p>N mesures moyennees ameliorent le SNR de racine(N).</p>

<p><strong>Detection synchrone (lock-in)</strong> :</p>
<p>Modulation du signal, demodulation synchrone, filtrage passe-bas etroit.</p>

<p><strong>Techniques numeriques</strong> :</p>
<p>Apres conversion A/N : filtrage numerique, FFT, correlation, detection de seuil adaptative.</p>

<p><strong>Au niveau application</strong> :</p>

<p><strong>Refroidissement</strong> :</p>
<p>Reduire T diminue le bruit thermique (cryogenie pour applications extremes).</p>

<p><strong>Choix de frequence de travail</strong> :</p>
<p>Eviter la zone de bruit en 1/f si possible (modulation a frequence plus haute).</p>

<h3 class="section-title">10. Mesure du bruit</h3>

<p><strong>Analyseur de spectre</strong> :</p>

<p>Mesure de la densite spectrale de puissance (PSD).</p>

<p>Permet d'identifier :</p>
<ul>
<li>Bruit blanc (niveau constant)</li>
<li>Bruit en 1/f (pente en -10 dB/decade)</li>
<li>Raies parasites (50/60 Hz secteur, harmoniques)</li>
</ul>

<p><strong>Oscilloscope numerique</strong> :</p>

<p>Methodes :</p>
<ul>
<li>Histogramme d'amplitude (distribution du bruit)</li>
<li>Mesure RMS du signal avec/sans entree</li>
<li>FFT pour analyse spectrale</li>
</ul>

<p><strong>Multimetre True RMS</strong> :</p>

<p>Mesure directe de la tension RMS de bruit dans une bande passante donnee.</p>

<p><strong>Methode pratique</strong> :</p>

<ol>
<li>Court-circuiter l'entree</li>
<li>Mesurer Vout sans signal</li>
<li>Ramener en entree : Vn_RTI = Vout / Gain</li>
<li>Comparer avec calculs theoriques</li>
</ol>

<p><strong>Precautions</strong> :</p>
<ul>
<li>Echauffement (attendre stabilisation thermique)</li>
<li>Blindage (cage de Faraday si necessaire)</li>
<li>Masse unique (eviter boucles de masse)</li>
<li>Cables courts et de qualite</li>
</ul>

<h3 class="section-title">11. Applications pratiques</h3>

<p><strong>Chaine d'acquisition biomedicale</strong> :</p>

<p><strong>ECG (electrocardiogramme)</strong> :</p>
<ul>
<li>Signal : 0.5-5 mV</li>
<li>Bruit acceptable : &lt; 10 uVRMS</li>
<li>Bande passante : 0.05-150 Hz</li>
<li>Filtrage : passe-bande + notch 50/60 Hz (rejection secteur)</li>
<li>Amplification differentielle (CMRR &gt; 100 dB)</li>
</ul>

<p><strong>EEG (electroencephalogramme)</strong> :</p>
<ul>
<li>Signal : 10-100 uV</li>
<li>Bruit : &lt; 1 uVRMS</li>
<li>Bande : 0.5-70 Hz</li>
<li>Preampli ultra-faible bruit obligatoire</li>
</ul>

<p><strong>Instrumentation scientifique</strong> :</p>

<p><strong>Amplificateur de charge (piezoelectrique)</strong> :</p>
<ul>
<li>Capteur haute impedance</li>
<li>Integrateur de courant</li>
<li>Bruit en courant critique (JFET ou MOSFET)</li>
</ul>

<p><strong>Lock-in amplifier</strong> :</p>
<ul>
<li>Detection de signaux enfouis dans le bruit</li>
<li>Modulation + demodulation synchrone</li>
<li>Filtrage passe-bas tres etroit (mHz)</li>
<li>Applications : spectroscopie, mesures de faibles signaux</li>
</ul>

<p><strong>Audio haute-fidelite</strong> :</p>

<p>Specifications :</p>
<ul>
<li>SNR &gt; 90 dB (CD quality : 96 dB)</li>
<li>Distorsion harmonique &lt; 0.01%</li>
<li>Filtrage anti-aliasing avant ADC 44.1/48 kHz</li>
<li>Filtrage de reconstruction apres DAC</li>
</ul>

<p>Filtres de ponderation :</p>
<ul>
<li>Courbe A (simulation oreille humaine)</li>
<li>Courbe C (mesures niveau eleve)</li>
</ul>

<p><strong>Telecommunications</strong> :</p>

<p><strong>Recepteur radio</strong> :</p>
<ul>
<li>LNA (Low Noise Amplifier) en tete</li>
<li>Figure de bruit NF &lt; 2 dB typiquement</li>
<li>Filtres SAW (Surface Acoustic Wave) pour selectivite</li>
<li>Cascade : antenne &rarr; LNA &rarr; filtre &rarr; melangeur &rarr; IF</li>
</ul>

<p><strong>Conversion A/N haute resolution</strong> :</p>

<p>Filtre anti-aliasing :</p>
<ul>
<li>Attenuation &gt; 80 dB a f_Nyquist</li>
<li>Phase lineaire (Bessel) ou attenuation raide (Chebyshev)</li>
<li>Transition entre f_utile et f_Nyquist</li>
</ul>

<hr/>

<h2>PART D - Analyse Reflexive et Perspectives</h2>

<h3 class="section-title">Competences acquises</h3>

<p><strong>Conception de filtres actifs</strong> :</p>
<p>Capacite a synthetiser un filtre depuis les specifications systeme (gabarit) jusqu'a l'implementation electronique avec composants reels.</p>

<p><strong>Maitrise du bruit</strong> :</p>
<p>Comprehension physique des sources de bruit, modelisation mathematique, calcul de propagation, et techniques d'optimisation.</p>

<p><strong>Analyse systeme</strong> :</p>
<p>Vision globale d'une chaine d'acquisition : conditionnement analogique, filtrage, conversion A/N, traitement numerique.</p>

<p><strong>Utilisation d'outils</strong> :</p>
<p>Simulation SPICE pour validation, MATLAB pour synthese, analyseur de spectre pour mesures.</p>

<p><strong>Compromis ingenierie</strong> :</p>
<p>Equilibrer selectivite, phase, bruit, cout, complexite selon l'application.</p>

<h3 class="section-title">Points cles a retenir</h3>

<p><strong>1. Choix de l'approximation de filtre</strong> :</p>
<p>Pas d'approximation universellement meilleure. Le choix depend de l'application :</p>
<ul>
<li>Audio : Butterworth ou Bessel (reponse douce)</li>
<li>Anti-aliasing : Chebyshev (transition rapide)</li>
<li>Telecom : Elliptique (selectivite maximale)</li>
</ul>

<p><strong>2. Bruit = limite fondamentale</strong> :</p>
<p>Le bruit impose une limite physique au plus petit signal detectable. Aucun traitement ne peut retrouver un signal entierement noye dans le bruit.</p>

<p><strong>3. Premier etage critique</strong> :</p>
<p>Le bruit et le gain du premier etage dominent les performances de toute la chaine (formule de Friis).</p>

<p><strong>4. Bande passante minimale</strong> :</p>
<p>Limiter la bande passante au strict necessaire reduit le bruit integre (proportionnel a racine(Df)).</p>

<p><strong>5. Simulation != realite</strong> :</p>
<p>Les mesures de bruit montrent souvent des contributions parasites non modelisees (alimentation, couplages, CEM).</p>

<h3 class="section-title">Retour d'experience</h3>

<p><strong>Richesse du cours</strong> :</p>
<p>Ce module couvre deux domaines vastes et interconnectes. Le filtrage et le bruit sont omnipresents en electronique analogique.</p>

<p><strong>Importance des TD</strong> :</p>
<p>Les 6 series de TD avec corrections sont essentielles pour maitriser les calculs de synthese de filtres et d'analyse de bruit.</p>

<p><strong>Annales precieuses</strong> :</p>
<p>Les examens (2016-2022 avec corrections) permettent de comprendre les attendus : synthese complete de filtre, calcul de bruit multi-sources, optimisation.</p>

<p><strong>Lien theorie/pratique</strong> :</p>
<p>Les TP ont montre que les filtres reels different legerement de la theorie (composants non ideaux, parasites). Le bruit mesure inclut des contributions non modelisees.</p>

<h3 class="section-title">Applications pratiques</h3>

<p><strong>Instrumentation de mesure</strong> :</p>
<ul>
<li>Oscilloscopes (amplificateurs d'entree, filtres anti-aliasing)</li>
<li>Multimetres de precision (filtrage, rejection bruit secteur)</li>
<li>Analyseurs de spectre (filtres IF, reduction du bruit)</li>
</ul>

<p><strong>Biomedical</strong> :</p>
<ul>
<li>Moniteurs ECG/EEG (amplification differentielle, filtrage bruit secteur)</li>
<li>Echographes (traitement signaux ultrasonores)</li>
<li>Capteurs implantables (ultra-faible bruit et consommation)</li>
</ul>

<p><strong>Audio professionnel</strong> :</p>
<ul>
<li>Consoles de mixage (egaliseurs actifs, crossovers)</li>
<li>Systemes Hi-Fi (filtres de ponderation, anti-aliasing)</li>
<li>Effets audio (filtres accordables, VCF)</li>
</ul>

<p><strong>Telecom et RF</strong> :</p>
<ul>
<li>Recepteurs (LNA, filtres IF)</li>
<li>Emetteurs (filtres passe-bande, rejection harmoniques)</li>
<li>IoT (filtres faible consommation)</li>
</ul>

<p><strong>Aeronautique et defense</strong> :</p>
<ul>
<li>Radars (filtrage doppler, traitement signal)</li>
<li>Avionique (instrumentation embarquee haute fiabilite)</li>
<li>Systemes critiques (specifications bruit strictes)</li>
</ul>

<h3 class="section-title">Limites et ouvertures</h3>

<p><strong>Limites du module</strong> :</p>
<ul>
<li>Peu d'approfondissement sur filtres adaptatifs</li>
<li>Filtres numeriques (DSP) non traites (autre cours)</li>
<li>Aspects EMC (compatibilite electromagnetique) superficiels</li>
</ul>

<p><strong>Ouvertures vers</strong> :</p>
<ul>
<li><strong>Traitement du signal avance</strong> : filtrage optimal (Wiener, Kalman), detection statistique</li>
<li><strong>Circuits integres RF</strong> : conception LNA, VCO, melangeurs</li>
<li><strong>Systemes mixtes</strong> : interfaces analog-digital, ADC/DAC haute resolution</li>
<li><strong>Electronique quantique</strong> : limites ultimes du bruit (bruit quantique)</li>
</ul>

<h3 class="section-title">Evolutions technologiques</h3>

<p><strong>Filtres programmables</strong> :</p>

<p>Circuits integres modernes permettent de configurer filtres par logiciel :</p>
<ul>
<li>Frequence de coupure ajustable</li>
<li>Type de filtre selectionnable (Butterworth, Chebyshev...)</li>
<li>Gain programmable</li>
</ul>

<p>Exemples : MAX7400 (Maxim), LTC1563 (Linear Technology).</p>

<p><strong>Filtrage hybride</strong> :</p>

<p>Combinaison analog/digital :</p>
<ul>
<li>Filtrage analogique grossier (anti-aliasing)</li>
<li>Sur-echantillonnage ADC</li>
<li>Filtrage numerique precis (FIR, IIR)</li>
</ul>

<p><strong>Composants faible bruit nouvelle generation</strong> :</p>
<ul>
<li>AOP ultra-faible bruit : &lt; 1 nV/racine(Hz)</li>
<li>Technologies BiCMOS, SiGe pour RF</li>
<li>MEMS et capteurs intelligents avec preampli integre</li>
</ul>

<p><strong>Intelligence artificielle</strong> :</p>

<p>Filtrage adaptatif par reseaux de neurones :</p>
<ul>
<li>Apprentissage du signal utile vs bruit</li>
<li>Suppression de bruit en temps reel</li>
<li>Applications : audio (reduction bruit actif), radar (clutter rejection)</li>
</ul>

<h3 class="section-title">Conseils pour reussir</h3>

<p><strong>1. Maitriser les bases theoriques</strong> :</p>
<p>Fonctions de transfert, poles/zeros, diagrammes de Bode sont fondamentaux. Sans eux, impossible de concevoir des filtres.</p>

<p><strong>2. Pratiquer les syntheses</strong> :</p>
<p>Refaire les TD de synthese jusqu'a maitriser la demarche complete (specifications &rarr; approximation &rarr; cellules &rarr; composants).</p>

<p><strong>3. Comprendre le bruit physiquement</strong> :</p>
<p>Savoir d'ou vient chaque type de bruit (thermique, grenaille, 1/f) aide a le modeliser et le reduire.</p>

<p><strong>4. Utiliser les annales</strong> :</p>
<p>Les examens 2016-2022 sont representatifs. S'entrainer sur ces sujets avec corrections.</p>

<p><strong>5. Simuler systematiquement</strong> :</p>
<p>SPICE permet de verifier les calculs, d'explorer les sensibilites, et de visualiser le bruit.</p>

<p><strong>6. Ordre de grandeur</strong> :</p>
<p>Memoriser quelques valeurs typiques (bruit d'une resistance de 10 kOhm = 13 nV/racine(Hz), AOP bipolaire en = 5 nV/racine(Hz)) pour detecter les erreurs.</p>

<h3 class="section-title">Conclusion</h3>

<p>Ce module est essentiel pour tout ingenieur travaillant sur des systemes d'acquisition de signaux. Le filtrage et le bruit determinent la qualite finale et les limites de performance d'un systeme.</p>

<p><strong>Competences transferables</strong> :</p>
<ul>
<li>Conception rigoureuse depuis specifications systeme</li>
<li>Modelisation de phenomenes physiques (bruit)</li>
<li>Optimisation multi-criteres (selectivite, phase, bruit, cout)</li>
<li>Vision systeme (chaine complete d'acquisition)</li>
</ul>

<p><strong>Pertinence professionnelle</strong> :</p>
<p>Ces competences sont recherchees dans de nombreux domaines : instrumentation, biomedical, audio, telecommunications, aeronautique, automobile (capteurs).</p>

<p><strong>Message principal</strong> :</p>
<p>Le filtrage analogique reste indispensable malgre l'essor du numerique (conditionnement avant ADC, applications RF). Le bruit est une limite fondamentale qui ne peut etre ignoree. Concevoir des systemes performants necessite de maitriser ces deux aspects.</p>

<p><strong>Recommandations</strong> :</p>
<ul>
<li>Approfondir par projets pratiques (conception et test de filtres, mesures de bruit)</li>
<li>Explorer les outils professionnels (FilterPro de TI, ADIsimPE d'Analog Devices)</li>
<li>Etudier des designs commerciaux (datasheets de MAX7400, LTC1563, AD8429)</li>
<li>Se former au traitement numerique du signal (complement indispensable)</li>
<li>Suivre les evolutions en circuits integres (technologies BiCMOS, SiGe, GaN)</li>
</ul>

<p><strong>Liens avec les autres cours</strong> :</p>
<ul>
<li><a href="./circuits-filtres-analogiques.html">Circuits et Filtres analogiques - S5</a> : fondements</li>
<li><a href="./filtrage-numerique.html">Filtrage numerique - S6</a> : complementarite analog/digital</li>
<li><a href="./chaines-acquisition.html">Chaines electroniques acquisition - S8</a> : integration systeme</li>
<li><a href="./signaux-aleatoires.html">Signaux aleatoires - S6</a> : modelisation probabiliste du bruit</li>
</ul>

<hr/>

<h2>Documents de Cours</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Cours Filtrage Actif</h4>
      <p>Cours complet sur le filtrage actif : structures Sallen-Key, Rauch, topologies d'ordre superieur et synthese de filtres.</p>
      <embed src="/cours-pdf/S7/Filtrage-Actif-Bruit/cours-filtrage.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Filtrage-Actif-Bruit/cours-filtrage.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>Bruit dans les AOP</h4>
      <p>Modelisation des sources de bruit dans les amplificateurs operationnels : bruit thermique, flicker, calcul du bruit total.</p>
      <embed src="/cours-pdf/S7/Filtrage-Actif-Bruit/bruit-ao.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Filtrage-Actif-Bruit/bruit-ao.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>Structure Sallen-Key</h4>
      <p>Cours sur la topologie Sallen-Key : principe, conception, sensibilite aux composants et realisation pratique.</p>
      <embed src="/cours-pdf/S7/Filtrage-Actif-Bruit/sallen-key.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Filtrage-Actif-Bruit/sallen-key.pdf" target="_blank">Telecharger</a></p>
    </div>
  </div>
</div>

<hr/>

<p><em>Cours suivi en 2023-2024 a l'INSA Toulouse, Departement Genie Electrique et Informatique.</em></p>

</div>

<div class="lang-en">

<h1>Active Filtering and Noise Source Modeling - Semester 7</h1>

<p><strong>Academic Year</strong>: 2023-2024<br/>
<strong>Semester</strong>: 7<br/>
<strong>Credits</strong>: 2.5 ECTS<br/>
<strong>Specialization</strong>: Analog Electronics and Signal Processing</p>

<hr/>

<h2>PART A - General Module Presentation</h2>

<h3 class="section-title">Overview</h3>

<p>This course covers two fundamental aspects of analog electronics: the design of active filters using operational amplifiers (op-amps) and operational transconductance amplifiers (OTA), and the analysis of noise in electronic circuits. These skills are essential for designing high-performance signal acquisition chains.</p>

<p><strong>Learning Objectives</strong>:</p>
<ul>
<li>Design and synthesize high-order active filters</li>
<li>Master Sallen-Key, Rauch, and switched-capacitor topologies</li>
<li>Understand the physical sources of electronic noise</li>
<li>Model and calculate noise in circuits</li>
<li>Optimize the signal-to-noise ratio (SNR)</li>
<li>Analyze the performance of acquisition chains</li>
</ul>

<h3 class="section-title">Position in the Curriculum</h3>

<p>This module builds upon:</p>
<ul>
<li><strong>Analog Circuits and Filters (S5)</strong>: passive filters, transfer functions</li>
<li><strong>Digital Filtering (S6)</strong>: filtering theory, approximations</li>
<li><strong>Active Component Study and Modeling (S7)</strong>: operational amplifiers</li>
</ul>

<p>It prepares for:</p>
<ul>
<li><strong>Electronic Acquisition Chains (S8)</strong>: sensor conditioning</li>
<li><strong>Stochastic Processes and Queuing Theory (S8)</strong>: probabilistic modeling</li>
<li><strong>Advanced Signal Processing</strong>: optimal filtering, detection</li>
<li><strong>Instrumentation System Design</strong>: precision measurements</li>
</ul>

<hr/>

<h2>PART B - Personal Experience and Learning Context</h2>

<h3 class="section-title">Organization and Resources</h3>

<p>The module was divided into several thematic sections:</p>

<p><strong>Lectures (20h)</strong>:</p>
<p>Organized into 4 main parts:</p>
<ul>
<li>Part 1: Operational amplifiers and OTA (folder 1_AO_OTA)
<ul>
<li>Internal noise of op-amps</li>
<li>OTA CA3080 (transconductance amplifier)</li>
</ul>
</li>
<li>Part 2: Electronic architecture and active filters (folder 3_Archi_Elec_Filtre_Actif)
<ul>
<li>Filter templates and synthesis</li>
<li>Sallen-Key and Rauch topologies</li>
<li>Cascading second-order cells</li>
</ul>
</li>
<li>Part 3: Switched capacitors (folder 4_Capa_Commute)
<ul>
<li>Principle and applications</li>
</ul>
</li>
<li>Part 4: Summary document (4AESE-filtrage4AE_2020-2021.pdf)</li>
</ul>

<p><strong>Tutorials (12h)</strong>:</p>
<ul>
<li>TD1 to TD6 with solutions available</li>
<li>Filter synthesis exercises</li>
<li>Noise calculations in circuits</li>
<li>Acquisition chain sizing</li>
</ul>

<p><strong>Assessments</strong>:</p>
<ul>
<li>Past exams available (2016-2022) with solutions</li>
<li>Exam covering both filtering AND noise</li>
<li>Filter design project</li>
</ul>

<p><strong>Tools used</strong>:</p>
<ul>
<li>SPICE (circuit simulation, noise analysis)</li>
<li>MATLAB/Octave (filter synthesis, calculations)</li>
<li>Spectrum analyzer (noise measurement)</li>
<li>Digital oscilloscope</li>
</ul>

<h3 class="section-title">Study Methodology</h3>

<p><strong>Phase 1: Filter Specifications</strong>:</p>
<p>Define the template (cutoff frequencies, ripple, stopband attenuation) according to the application.</p>

<p><strong>Phase 2: Choosing the Approximation</strong>:</p>
<p>Select Butterworth, Chebyshev, Bessel, or Elliptic according to the selectivity/phase/time trade-off.</p>

<p><strong>Phase 3: Transfer Function Synthesis</strong>:</p>
<p>Use tables or software to obtain poles and zeros. Decompose into second-order cells.</p>

<p><strong>Phase 4: Electronic Implementation</strong>:</p>
<p>Choose the topology (Sallen-Key, Rauch) and calculate the components (R, C) for each cell.</p>

<p><strong>Phase 5: Noise Analysis</strong>:</p>
<p>Calculate the noise contributions of each component and op-amp, then the total input-referred noise.</p>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S7/filtrage-actif/capacites-commutees.svg" alt="Switched-capacitor filter" style="max-width: 550px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Switched-capacitor filter principle - Resistance emulation through switching</p>
</div>

<p><strong>Phase 6: Simulation and Validation</strong>:</p>
<p>Verify the frequency response, noise, and practical limitations (saturation, slew-rate).</p>

<h3 class="section-title">Difficulties Encountered</h3>

<p><strong>High-order filter synthesis</strong>:</p>
<p>Cascading multiple second-order cells requires managing interactions, section ordering, and inter-stage signal levels.</p>

<p><strong>Component values</strong>:</p>
<p>Theoretical calculations often yield non-standard values (resistors, capacitors). They must be adjusted using E12/E24/E96 series.</p>

<p><strong>Noise analysis</strong>:</p>
<p>Identifying all noise sources (resistors, op-amps, power supplies), calculating their input-referred contribution, then integrating over the bandwidth requires rigor.</p>

<p><strong>1/f noise</strong>:</p>
<p>The spectral density is not constant, which complicates integration calculations. Requires knowledge of the corner frequency.</p>

<hr/>

<h2>PART C - Detailed Technical Aspects</h2>

<h3 class="section-title">1. Operational Amplifiers and Internal Noise</h3>

<p><strong>Op-amp noise model</strong>:</p>

<p>Three equivalent input noise sources:</p>
<ul>
<li><strong>en</strong>: input voltage noise (nV/sqrt(Hz))</li>
<li><strong>in+</strong>: non-inverting input current noise (pA/sqrt(Hz))</li>
<li><strong>in-</strong>: inverting input current noise (pA/sqrt(Hz))</li>
</ul>

<p><strong>Voltage noise spectral density</strong>:</p>

<p>Typically:</p>
<ul>
<li>Bipolar op-amp: en = 1-10 nV/sqrt(Hz)</li>
<li>JFET op-amp: en = 5-20 nV/sqrt(Hz)</li>
<li>Precision op-amp: en &lt; 5 nV/sqrt(Hz)</li>
</ul>

<p><strong>Current noise spectral density</strong>:</p>

<p>Typically:</p>
<ul>
<li>Bipolar op-amp: in = 1-10 pA/sqrt(Hz)</li>
<li>JFET op-amp: in = 0.01-1 pA/sqrt(Hz) (very low)</li>
</ul>

<p><strong>1/f noise</strong>:</p>

<p>Corner frequency fc (transition between 1/f noise and white noise):</p>
<ul>
<li>Bipolar op-amp: fc = 10-100 Hz</li>
<li>JFET op-amp: fc = 100-1000 Hz</li>
</ul>

<p><strong>OTA (Operational Transconductance Amplifier)</strong>:</p>

<p>Example: CA3080</p>
<ul>
<li>Current output (adjustable transconductance gm)</li>
<li>Applications: VCA, VCF, multipliers</li>
<li>Noise typically higher than conventional op-amps</li>
</ul>

<h3 class="section-title">2. Fundamental Noise Sources</h3>

<p><strong>Thermal noise (Johnson-Nyquist)</strong>:</p>

<p>Origin: thermal agitation of charge carriers in resistors.</p>

<p>RMS noise voltage:</p>
<p>Vn = sqrt(4 x k x T x R x Df)</p>

<p>where:</p>
<ul>
<li>k = 1.38 x 10^-23 J/K (Boltzmann constant)</li>
<li>T: absolute temperature (Kelvin)</li>
<li>R: resistance (Ohms)</li>
<li>Df: bandwidth (Hz)</li>
</ul>

<p>Spectral density (white spectrum):</p>
<p>Sn(f) = 4 x k x T x R (V^2/Hz)</p>

<p><strong>Examples at 25 deg C (T=298K)</strong>:</p>

<table>
<tr><th>Resistance</th><th>Noise (nV/sqrt(Hz))</th></tr>
<tr><td>1 kOhm</td><td>4.1</td></tr>
<tr><td>10 kOhm</td><td>13</td></tr>
<tr><td>100 kOhm</td><td>41</td></tr>
<tr><td>1 MOhm</td><td>130</td></tr>
</table>

<p><strong>Shot noise</strong>:</p>

<p>Origin: discrete nature of electric current (electron quantization).</p>

<p>RMS noise current:</p>
<p>In = sqrt(2 x q x I x Df)</p>

<p>where:</p>
<ul>
<li>q = 1.6 x 10^-19 C (electron charge)</li>
<li>I: average current (A)</li>
</ul>

<p>Observed in PN junctions (diodes, transistors), vacuum tubes, photodetectors.</p>

<p><strong>1/f noise (flicker noise)</strong>:</p>

<p>Origin: crystal defects, surface recombinations.</p>

<p>Spectral density:</p>
<p>Sn(f) = K / f</p>

<p>Dominant at low frequency (&lt; 1 kHz typically).</p>

<p>Corner frequency fc: transition to white noise.</p>

<p><strong>Noise comparison</strong>:</p>

<table>
<tr><th>Type</th><th>Spectrum</th><th>Amplitude</th><th>Dominant</th></tr>
<tr><td>Thermal</td><td>White</td><td>4kTR</td><td>All frequencies</td></tr>
<tr><td>Shot</td><td>White</td><td>2qI</td><td>Active junctions</td></tr>
<tr><td>1/f</td><td>Pink (1/f)</td><td>Variable</td><td>Low frequencies</td></tr>
</table>

<h3 class="section-title">3. Active Filter Topologies</h3>

<p><strong>Sallen-Key filter (VCVS)</strong>:</p>

<p>Non-inverting configuration with gain K.</p>

<p><strong>Second-order low-pass</strong>:</p>

<p>Components: R1, R2, C1, C2, op-amp as follower or amplifier.</p>

<p>General transfer function:</p>
<p>H(s) = K x w0^2 / (s^2 + (w0/Q) x s + w0^2)</p>

<p>where:</p>
<ul>
<li>w0: natural frequency (cutoff frequency)</li>
<li>Q: quality factor (inverse of damping)</li>
<li>K: passband gain</li>
</ul>

<p><strong>Advantages</strong>:</p>
<ul>
<li>Simple (few components)</li>
<li>Possible passband gain</li>
<li>High input impedance</li>
</ul>

<p><strong>Disadvantages</strong>:</p>
<ul>
<li>Sensitivity to components for high Q</li>
<li>Limited stability if Q &gt; 10</li>
</ul>

<p><strong>Rauch filter (inverting structure)</strong>:</p>

<p>Inverting configuration with negative passband gain.</p>

<p><strong>Advantages</strong>:</p>
<ul>
<li>Better stability for high Q</li>
<li>Less sensitive to component variations</li>
</ul>

<p><strong>Disadvantages</strong>:</p>
<ul>
<li>Lower input impedance</li>
<li>Negative gain (may require an additional inverting stage)</li>
</ul>

<p><strong>Comparison</strong>:</p>

<table>
<tr><th>Criterion</th><th>Sallen-Key</th><th>Rauch</th></tr>
<tr><td>Number of components</td><td>4 passive + op-amp</td><td>5 passive + op-amp</td></tr>
<tr><td>Input impedance</td><td>High</td><td>Medium/Low</td></tr>
<tr><td>Passband gain</td><td>Positive</td><td>Negative</td></tr>
<tr><td>Stability high Q</td><td>Limited</td><td>Better</td></tr>
<tr><td>Usage</td><td>Versatile</td><td>Q &gt; 5</td></tr>
</table>

<h3 class="section-title">4. Filter Approximations</h3>

<p><strong>Butterworth (Maximally Flat)</strong>:</p>

<p>Characteristics:</p>
<ul>
<li>Flattest possible amplitude response in the passband</li>
<li>No ripple</li>
<li>Attenuation: 20 x n dB/decade (n = filter order)</li>
<li>Non-linear phase response</li>
</ul>

<p>Applications: general purpose, audio (smooth response).</p>

<p><strong>Chebyshev Type I</strong>:</p>

<p>Characteristics:</p>
<ul>
<li>Passband ripple (controlled ripple, e.g.: 0.5 dB, 1 dB, 3 dB)</li>
<li>Steeper slope than Butterworth for the same order</li>
<li>Fast transition</li>
</ul>

<p>Applications: anti-aliasing, selective filters.</p>

<p><strong>Chebyshev Type II (Inverse)</strong>:</p>

<p>Characteristics:</p>
<ul>
<li>Stopband ripple</li>
<li>Flat passband</li>
<li>Transmission zeros (finite attenuation)</li>
</ul>

<p>Applications: less common, compromise.</p>

<p><strong>Bessel (Thomson)</strong>:</p>

<p>Characteristics:</p>
<ul>
<li>Linear phase response</li>
<li>Constant group delay (no phase distortion)</li>
<li>Gentle attenuation (low slope)</li>
</ul>

<p>Applications: video, pulses (preservation of time-domain waveform).</p>

<p><strong>Elliptic (Cauer)</strong>:</p>

<p>Characteristics:</p>
<ul>
<li>Ripple in both passband AND stopband</li>
<li>Steepest slope for a given order</li>
<li>Design complexity (transmission zeros)</li>
</ul>

<p>Applications: telecommunications (maximum selectivity).</p>

<p><strong>Summary table</strong>:</p>

<table>
<tr><th>Type</th><th>Passband</th><th>Slope</th><th>Phase</th><th>Application</th></tr>
<tr><td>Butterworth</td><td>Flat</td><td>Medium</td><td>Non-linear</td><td>General purpose</td></tr>
<tr><td>Chebyshev I</td><td>Ripple</td><td>Steep</td><td>Strongly non-linear</td><td>Anti-aliasing</td></tr>
<tr><td>Chebyshev II</td><td>Flat</td><td>Steep</td><td>Non-linear</td><td>Compromise</td></tr>
<tr><td>Bessel</td><td>Flat</td><td>Gentle</td><td>Linear</td><td>Video, pulses</td></tr>
<tr><td>Elliptic</td><td>Ripple</td><td>Very steep</td><td>Strongly non-linear</td><td>Telecom</td></tr>
</table>

<h3 class="section-title">5. High-Order Filter Synthesis</h3>

<p><strong>Cascade decomposition</strong>:</p>

<p>An nth-order filter is realized by cascading cells:</p>
<ul>
<li>Even order: n/2 second-order cells</li>
<li>Odd order: (n-1)/2 second-order cells + 1 first-order cell</li>
</ul>

<p>Total transfer function:</p>
<p>H(s) = H1(s) x H2(s) x ... x Hk(s)</p>

<p><strong>Parameters for each cell</strong>:</p>

<p>Each second-order cell has its own:</p>
<ul>
<li>Natural frequency w0i</li>
<li>Quality factor Qi</li>
<li>Gain Ki</li>
</ul>

<p><strong>Example: 5th-order Butterworth</strong>:</p>

<p>Decomposition: 2 second-order cells + 1 first-order cell</p>

<p>Cell 1: Q1 = 0.618, w01 = wc<br/>
Cell 2: Q2 = 1.618, w02 = wc<br/>
Cell 3: real pole at -wc</p>

<p><strong>Section ordering</strong>:</p>

<p>General principle:</p>
<ol>
<li>Place high-Q sections at the end of the cascade (after attenuation)</li>
<li>Avoid saturation of the first stages</li>
<li>Minimize noise accumulation</li>
</ol>

<p><strong>Normalization and denormalization</strong>:</p>

<p>Steps:</p>
<ol>
<li>Normalized synthesis (wc = 1 rad/s, R = 1 Ohm)</li>
<li>Coefficient tables for standard approximations</li>
<li>Denormalization: frequency and impedance scaling</li>
</ol>

<p>Denormalization formulas:</p>
<ul>
<li>Resistance: R_actual = R_normalized x Z0</li>
<li>Capacitance: C_actual = C_normalized / (Z0 x wc)</li>
</ul>

<h3 class="section-title">6. Switched-Capacitor Filters</h3>

<p><strong>Principle</strong>:</p>

<p>A resistor is emulated by periodically switching a capacitor.</p>

<p>Equivalent resistance:</p>
<p>Req = T / C = 1 / (f x C)</p>

<p>where:</p>
<ul>
<li>T: clock period</li>
<li>f: clock frequency</li>
<li>C: switched capacitor</li>
</ul>

<p><strong>Advantages</strong>:</p>
<ul>
<li>Accuracy determined by capacitor ratios (excellent in ICs)</li>
<li>No resistors (area savings in integration)</li>
<li>Tunability via clock frequency</li>
<li>Low sensitivity to process variations</li>
</ul>

<p><strong>Limitations</strong>:</p>
<ul>
<li>Requires a clock (clock noise)</li>
<li>Sampling theorem: f_clock &gt;&gt; 2 x f_signal</li>
<li>Typically: f_clock = 50 to 100 x f_cutoff</li>
</ul>

<p><strong>Applications</strong>:</p>
<ul>
<li>Anti-aliasing filters in ADCs</li>
<li>Reconstruction filters in DACs</li>
<li>Programmable audio equalizers</li>
<li>Mixed-signal integrated circuits (analog/digital)</li>
</ul>

<p><strong>Commercial example</strong>:</p>

<p>MAX7400 (Maxim): 8th-order Butterworth switched-capacitor low-pass filter, clock-programmable cutoff frequency.</p>

<h3 class="section-title">7. Noise Analysis in an Amplifier</h3>

<p><strong>Non-inverting amplifier</strong>:</p>

<p>Configuration:</p>
<ul>
<li>Gain Av = 1 + (R2 / R1)</li>
<li>Input: signal source Vs with impedance Rs</li>
</ul>

<p><strong>Noise sources</strong>:</p>

<ol>
<li>Source noise: Vn_source = sqrt(4kTRs)</li>
<li>R1 thermal noise: Vn_R1 = sqrt(4kTR1)</li>
<li>R2 thermal noise: Vn_R2 = sqrt(4kTR2)</li>
<li>Op-amp voltage noise: en</li>
<li>Op-amp current noise x impedances: in x (Rs // (R1+R2))</li>
</ol>

<p><strong>Total input-referred noise (RTI)</strong>:</p>

<p>Vn_total^2 = Vn_source^2 + en^2 + (in x Rs)^2 + (Vn_R1 / Av)^2 + (Vn_R2 / Av)^2</p>

<p><strong>Output noise</strong>:</p>

<p>Vn_out = Vn_total x Av</p>

<p><strong>Optimization</strong>:</p>
<ul>
<li>Minimize Rs (low source impedance)</li>
<li>Choose reasonable R1, R2 (noise/power trade-off)</li>
<li>Select op-amp with low en and in</li>
<li>Technologies: bipolar (low en), JFET (low in)</li>
</ul>

<h3 class="section-title">8. Noise Figure and SNR</h3>

<p><strong>Signal-to-Noise Ratio (SNR)</strong>:</p>

<p>SNR = Signal_power / Noise_power</p>

<p>In dB:</p>
<p>SNR_dB = 10 x log10(Psignal / Pnoise)</p>

<p>or in RMS voltages:</p>
<p>SNR_dB = 20 x log10(Vsignal_RMS / Vnoise_RMS)</p>

<p><strong>Noise Factor (F)</strong>:</p>

<p>SNR degradation by a system:</p>

<p>F = SNR_input / SNR_output</p>

<p><strong>Noise Figure (NF)</strong>:</p>

<p>NF_dB = 10 x log10(F)</p>

<p>An ideal system (no added noise) has F = 1, NF = 0 dB.</p>

<p><strong>Equivalent noise temperature</strong>:</p>

<p>Te = T0 x (F - 1)</p>

<p>where T0 = 290 K (reference temperature).</p>

<p><strong>Friis formula (cascaded systems)</strong>:</p>

<p>For n cascaded stages:</p>

<p>F_total = F1 + (F2 - 1)/G1 + (F3 - 1)/(G1xG2) + ... + (Fn - 1)/(G1xG2x...xGn-1)</p>

<p>where Fi: noise factor of stage i, Gi: power gain of stage i.</p>

<p><strong>Practical implications</strong>:</p>
<ul>
<li>The first stage dominates the total noise</li>
<li>A high gain in the first stage reduces the impact of subsequent stages</li>
<li>Low-noise preamplifier (LNA) crucial at the front of the chain</li>
<li>Applications: radio receivers, instrumentation</li>
</ul>

<h3 class="section-title">9. Noise Reduction Techniques</h3>

<p><strong>At the circuit design level</strong>:</p>

<p><strong>Minimize impedances</strong>:</p>
<p>Resistors generate thermal noise. Use reasonable values (typically 1-100 kOhm).</p>

<p><strong>Choose the right op-amp</strong>:</p>
<ul>
<li>Low source impedance application: minimize en</li>
<li>High source impedance application: minimize in</li>
<li>Speed/noise trade-off (fast op-amps are often noisier)</li>
</ul>

<p><strong>Matched filtering</strong>:</p>
<p>Limiting the bandwidth to the strict minimum reduces integrated noise.</p>

<p><strong>Shielding and guarding</strong>:</p>
<p>Reduce external electromagnetic interference.</p>

<p><strong>Clean power supply</strong>:</p>
<p>Careful decoupling, low-noise regulators, mains filtering.</p>

<p><strong>At the system level</strong>:</p>

<p><strong>Optimal filtering</strong>:</p>
<p>Matched filter maximizes SNR for a known signal in white noise.</p>

<p><strong>Averaging</strong>:</p>
<p>N averaged measurements improve the SNR by sqrt(N).</p>

<p><strong>Synchronous detection (lock-in)</strong>:</p>
<p>Signal modulation, synchronous demodulation, narrow low-pass filtering.</p>

<p><strong>Digital techniques</strong>:</p>
<p>After A/D conversion: digital filtering, FFT, correlation, adaptive threshold detection.</p>

<p><strong>At the application level</strong>:</p>

<p><strong>Cooling</strong>:</p>
<p>Reducing T decreases thermal noise (cryogenics for extreme applications).</p>

<p><strong>Operating frequency selection</strong>:</p>
<p>Avoid the 1/f noise region if possible (modulate at a higher frequency).</p>

<h3 class="section-title">10. Noise Measurement</h3>

<p><strong>Spectrum analyzer</strong>:</p>

<p>Power spectral density (PSD) measurement.</p>

<p>Allows identification of:</p>
<ul>
<li>White noise (constant level)</li>
<li>1/f noise (-10 dB/decade slope)</li>
<li>Spurious lines (50/60 Hz mains, harmonics)</li>
</ul>

<p><strong>Digital oscilloscope</strong>:</p>

<p>Methods:</p>
<ul>
<li>Amplitude histogram (noise distribution)</li>
<li>RMS measurement of signal with/without input</li>
<li>FFT for spectral analysis</li>
</ul>

<p><strong>True RMS multimeter</strong>:</p>

<p>Direct measurement of RMS noise voltage within a given bandwidth.</p>

<p><strong>Practical method</strong>:</p>

<ol>
<li>Short-circuit the input</li>
<li>Measure Vout without signal</li>
<li>Refer to input: Vn_RTI = Vout / Gain</li>
<li>Compare with theoretical calculations</li>
</ol>

<p><strong>Precautions</strong>:</p>
<ul>
<li>Warm-up (wait for thermal stabilization)</li>
<li>Shielding (Faraday cage if necessary)</li>
<li>Single ground point (avoid ground loops)</li>
<li>Short, high-quality cables</li>
</ul>

<h3 class="section-title">11. Practical Applications</h3>

<p><strong>Biomedical acquisition chain</strong>:</p>

<p><strong>ECG (electrocardiogram)</strong>:</p>
<ul>
<li>Signal: 0.5-5 mV</li>
<li>Acceptable noise: &lt; 10 uVRMS</li>
<li>Bandwidth: 0.05-150 Hz</li>
<li>Filtering: band-pass + notch 50/60 Hz (mains rejection)</li>
<li>Differential amplification (CMRR &gt; 100 dB)</li>
</ul>

<p><strong>EEG (electroencephalogram)</strong>:</p>
<ul>
<li>Signal: 10-100 uV</li>
<li>Noise: &lt; 1 uVRMS</li>
<li>Bandwidth: 0.5-70 Hz</li>
<li>Ultra-low-noise preamplifier mandatory</li>
</ul>

<p><strong>Scientific instrumentation</strong>:</p>

<p><strong>Charge amplifier (piezoelectric)</strong>:</p>
<ul>
<li>High impedance sensor</li>
<li>Current integrator</li>
<li>Critical current noise (JFET or MOSFET)</li>
</ul>

<p><strong>Lock-in amplifier</strong>:</p>
<ul>
<li>Detection of signals buried in noise</li>
<li>Modulation + synchronous demodulation</li>
<li>Very narrow low-pass filtering (mHz)</li>
<li>Applications: spectroscopy, weak signal measurements</li>
</ul>

<p><strong>High-fidelity audio</strong>:</p>

<p>Specifications:</p>
<ul>
<li>SNR &gt; 90 dB (CD quality: 96 dB)</li>
<li>Harmonic distortion &lt; 0.01%</li>
<li>Anti-aliasing filtering before 44.1/48 kHz ADC</li>
<li>Reconstruction filtering after DAC</li>
</ul>

<p>Weighting filters:</p>
<ul>
<li>A-weighting curve (human ear simulation)</li>
<li>C-weighting curve (high-level measurements)</li>
</ul>

<p><strong>Telecommunications</strong>:</p>

<p><strong>Radio receiver</strong>:</p>
<ul>
<li>LNA (Low Noise Amplifier) at the front</li>
<li>Noise figure NF &lt; 2 dB typically</li>
<li>SAW (Surface Acoustic Wave) filters for selectivity</li>
<li>Cascade: antenna &rarr; LNA &rarr; filter &rarr; mixer &rarr; IF</li>
</ul>

<p><strong>High-resolution A/D conversion</strong>:</p>

<p>Anti-aliasing filter:</p>
<ul>
<li>Attenuation &gt; 80 dB at f_Nyquist</li>
<li>Linear phase (Bessel) or steep attenuation (Chebyshev)</li>
<li>Transition between f_useful and f_Nyquist</li>
</ul>

<hr/>

<h2>PART D - Reflective Analysis and Perspectives</h2>

<h3 class="section-title">Skills Acquired</h3>

<p><strong>Active filter design</strong>:</p>
<p>Ability to synthesize a filter from system specifications (template) through to electronic implementation with real components.</p>

<p><strong>Noise mastery</strong>:</p>
<p>Physical understanding of noise sources, mathematical modeling, propagation calculation, and optimization techniques.</p>

<p><strong>System analysis</strong>:</p>
<p>Overall view of an acquisition chain: analog conditioning, filtering, A/D conversion, digital processing.</p>

<p><strong>Tool usage</strong>:</p>
<p>SPICE simulation for validation, MATLAB for synthesis, spectrum analyzer for measurements.</p>

<p><strong>Engineering trade-offs</strong>:</p>
<p>Balancing selectivity, phase, noise, cost, and complexity according to the application.</p>

<h3 class="section-title">Key Takeaways</h3>

<p><strong>1. Choosing the filter approximation</strong>:</p>
<p>No universally best approximation. The choice depends on the application:</p>
<ul>
<li>Audio: Butterworth or Bessel (smooth response)</li>
<li>Anti-aliasing: Chebyshev (fast transition)</li>
<li>Telecom: Elliptic (maximum selectivity)</li>
</ul>

<p><strong>2. Noise = fundamental limit</strong>:</p>
<p>Noise imposes a physical limit on the smallest detectable signal. No processing can recover a signal completely buried in noise.</p>

<p><strong>3. Critical first stage</strong>:</p>
<p>The noise and gain of the first stage dominate the performance of the entire chain (Friis formula).</p>

<p><strong>4. Minimum bandwidth</strong>:</p>
<p>Limiting the bandwidth to the strict minimum reduces integrated noise (proportional to sqrt(Df)).</p>

<p><strong>5. Simulation != reality</strong>:</p>
<p>Noise measurements often show parasitic contributions not accounted for in models (power supply, coupling, EMC).</p>

<h3 class="section-title">Feedback</h3>

<p><strong>Course richness</strong>:</p>
<p>This module covers two vast and interconnected domains. Filtering and noise are omnipresent in analog electronics.</p>

<p><strong>Importance of tutorials</strong>:</p>
<p>The 6 tutorial series with solutions are essential for mastering filter synthesis and noise analysis calculations.</p>

<p><strong>Valuable past exams</strong>:</p>
<p>The exams (2016-2022 with solutions) help understand expectations: complete filter synthesis, multi-source noise calculation, optimization.</p>

<p><strong>Theory/practice link</strong>:</p>
<p>Lab work showed that real filters differ slightly from theory (non-ideal components, parasitic effects). Measured noise includes unmodeled contributions.</p>

<h3 class="section-title">Practical Applications</h3>

<p><strong>Measurement instrumentation</strong>:</p>
<ul>
<li>Oscilloscopes (input amplifiers, anti-aliasing filters)</li>
<li>Precision multimeters (filtering, mains noise rejection)</li>
<li>Spectrum analyzers (IF filters, noise reduction)</li>
</ul>

<p><strong>Biomedical</strong>:</p>
<ul>
<li>ECG/EEG monitors (differential amplification, mains noise filtering)</li>
<li>Ultrasound scanners (ultrasonic signal processing)</li>
<li>Implantable sensors (ultra-low noise and power consumption)</li>
</ul>

<p><strong>Professional audio</strong>:</p>
<ul>
<li>Mixing consoles (active equalizers, crossovers)</li>
<li>Hi-Fi systems (weighting filters, anti-aliasing)</li>
<li>Audio effects (tunable filters, VCF)</li>
</ul>

<p><strong>Telecom and RF</strong>:</p>
<ul>
<li>Receivers (LNA, IF filters)</li>
<li>Transmitters (band-pass filters, harmonic rejection)</li>
<li>IoT (low-power filters)</li>
</ul>

<p><strong>Aerospace and defense</strong>:</p>
<ul>
<li>Radars (Doppler filtering, signal processing)</li>
<li>Avionics (high-reliability embedded instrumentation)</li>
<li>Critical systems (strict noise specifications)</li>
</ul>

<h3 class="section-title">Limitations and Outlook</h3>

<p><strong>Module limitations</strong>:</p>
<ul>
<li>Little depth on adaptive filters</li>
<li>Digital filters (DSP) not covered (separate course)</li>
<li>EMC (electromagnetic compatibility) aspects only superficial</li>
</ul>

<p><strong>Outlook towards</strong>:</p>
<ul>
<li><strong>Advanced signal processing</strong>: optimal filtering (Wiener, Kalman), statistical detection</li>
<li><strong>RF integrated circuits</strong>: LNA, VCO, mixer design</li>
<li><strong>Mixed-signal systems</strong>: analog-digital interfaces, high-resolution ADC/DAC</li>
<li><strong>Quantum electronics</strong>: ultimate noise limits (quantum noise)</li>
</ul>

<h3 class="section-title">Technological Developments</h3>

<p><strong>Programmable filters</strong>:</p>

<p>Modern integrated circuits allow software-configurable filters:</p>
<ul>
<li>Adjustable cutoff frequency</li>
<li>Selectable filter type (Butterworth, Chebyshev...)</li>
<li>Programmable gain</li>
</ul>

<p>Examples: MAX7400 (Maxim), LTC1563 (Linear Technology).</p>

<p><strong>Hybrid filtering</strong>:</p>

<p>Analog/digital combination:</p>
<ul>
<li>Coarse analog filtering (anti-aliasing)</li>
<li>ADC oversampling</li>
<li>Precise digital filtering (FIR, IIR)</li>
</ul>

<p><strong>Next-generation low-noise components</strong>:</p>
<ul>
<li>Ultra-low-noise op-amps: &lt; 1 nV/sqrt(Hz)</li>
<li>BiCMOS, SiGe technologies for RF</li>
<li>MEMS and smart sensors with integrated preamplifier</li>
</ul>

<p><strong>Artificial intelligence</strong>:</p>

<p>Adaptive filtering with neural networks:</p>
<ul>
<li>Learning useful signal vs noise</li>
<li>Real-time noise suppression</li>
<li>Applications: audio (active noise reduction), radar (clutter rejection)</li>
</ul>

<h3 class="section-title">Tips for Success</h3>

<p><strong>1. Master the theoretical foundations</strong>:</p>
<p>Transfer functions, poles/zeros, Bode plots are fundamental. Without them, filter design is impossible.</p>

<p><strong>2. Practice synthesis exercises</strong>:</p>
<p>Redo the synthesis tutorials until mastering the complete workflow (specifications &rarr; approximation &rarr; cells &rarr; components).</p>

<p><strong>3. Understand noise physically</strong>:</p>
<p>Knowing where each type of noise comes from (thermal, shot, 1/f) helps model and reduce it.</p>

<p><strong>4. Use past exams</strong>:</p>
<p>The 2016-2022 exams are representative. Practice with these papers and their solutions.</p>

<p><strong>5. Simulate systematically</strong>:</p>
<p>SPICE allows verifying calculations, exploring sensitivities, and visualizing noise.</p>

<p><strong>6. Orders of magnitude</strong>:</p>
<p>Memorize a few typical values (noise of a 10 kOhm resistor = 13 nV/sqrt(Hz), bipolar op-amp en = 5 nV/sqrt(Hz)) to detect errors.</p>

<h3 class="section-title">Conclusion</h3>

<p>This module is essential for any engineer working on signal acquisition systems. Filtering and noise determine the final quality and performance limits of a system.</p>

<p><strong>Transferable skills</strong>:</p>
<ul>
<li>Rigorous design from system specifications</li>
<li>Modeling of physical phenomena (noise)</li>
<li>Multi-criteria optimization (selectivity, phase, noise, cost)</li>
<li>System-level perspective (complete acquisition chain)</li>
</ul>

<p><strong>Professional relevance</strong>:</p>
<p>These skills are sought after in many fields: instrumentation, biomedical, audio, telecommunications, aerospace, automotive (sensors).</p>

<p><strong>Main message</strong>:</p>
<p>Analog filtering remains indispensable despite the rise of digital (conditioning before ADC, RF applications). Noise is a fundamental limit that cannot be ignored. Designing high-performance systems requires mastering both aspects.</p>

<p><strong>Recommendations</strong>:</p>
<ul>
<li>Deepen knowledge through practical projects (filter design and testing, noise measurements)</li>
<li>Explore professional tools (TI FilterPro, Analog Devices ADIsimPE)</li>
<li>Study commercial designs (datasheets for MAX7400, LTC1563, AD8429)</li>
<li>Train in digital signal processing (essential complement)</li>
<li>Follow developments in integrated circuits (BiCMOS, SiGe, GaN technologies)</li>
</ul>

<p><strong>Links to other courses</strong>:</p>
<ul>
<li><a href="./circuits-filtres-analogiques.html">Analog Circuits and Filters - S5</a>: foundations</li>
<li><a href="./filtrage-numerique.html">Digital Filtering - S6</a>: analog/digital complementarity</li>
<li><a href="./chaines-acquisition.html">Electronic Acquisition Chains - S8</a>: system integration</li>
<li><a href="./signaux-aleatoires.html">Random Signals - S6</a>: probabilistic noise modeling</li>
</ul>

<hr/>

<h2>Course Documents</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Active Filtering Course</h4>
      <p>Complete course on active filtering: Sallen-Key and Rauch structures, higher-order topologies and filter synthesis.</p>
      <embed src="/cours-pdf/S7/Filtrage-Actif-Bruit/cours-filtrage.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Filtrage-Actif-Bruit/cours-filtrage.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>Noise in Op-Amps</h4>
      <p>Noise source modeling in operational amplifiers: thermal noise, flicker noise, total noise calculation.</p>
      <embed src="/cours-pdf/S7/Filtrage-Actif-Bruit/bruit-ao.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Filtrage-Actif-Bruit/bruit-ao.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>Sallen-Key Structure</h4>
      <p>Course on Sallen-Key topology: principle, design, component sensitivity and practical implementation.</p>
      <embed src="/cours-pdf/S7/Filtrage-Actif-Bruit/sallen-key.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Filtrage-Actif-Bruit/sallen-key.pdf" target="_blank">Download</a></p>
    </div>
  </div>
</div>

<hr/>

<p><em>Course taken in 2023-2024 at INSA Toulouse, Department of Electrical Engineering and Computer Science.</em></p>

</div>

<div class="back-nav">
    <a href="./my-courses-2023-2024.html" data-i18n-html="back-courses-2023-2024">&larr; Retour aux Cours 2023-2024</a>
</div>

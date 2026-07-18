---
layout: default
title:  "Energy Connected Object"
date:   2024-10-02 10:56:03 +0200
---

<style>
.back-nav {
    margin: 20px 0;
    padding: 10px;
    background-color: #f0f0f0;
    border-radius: 5px;
}

.back-nav a {
    color: #007BFF;
    text-decoration: none;
    font-weight: bold;
}

.back-nav a:hover {
    text-decoration: underline;
}

.section-title {
    color: #007BFF;
    border-bottom: 2px solid #007BFF;
    padding-bottom: 5px;
    margin-top: 20px;
}

table {
    border-collapse: collapse;
    width: 100%;
    margin: 20px 0;
}

th, td {
    border: 1px solid #ddd;
    padding: 12px;
    text-align: left;
}

th {
    background-color: #007BFF;
    color: white;
}

tr:nth-child(even) {
    background-color: #f2f2f2;
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

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f9;
    color: #333;
    line-height: 1.6;
}

h2, h3, h4 {
    color: #007BFF;
}

p {
    text-align: justify;
}
</style>

<div class="back-nav">
    <a href="./my-courses-2024-2025.html" data-i18n-html="back-courses-2024-2025">&larr; Retour aux Cours 2024-2025</a>
</div>

<div class="lang-fr">

<h1>Energy for Connected Objects - Semestre 9</h1>

<p><strong>Cours connexes</strong> :</p>
<ul>
<li><a href="./embedded-ia-iot.html">Embedded IA for IoT - S9</a> - Optimisation energetique de l'IA</li>
<li><a href="./wireless-sensors.html">Wireless Sensors Networks - S9</a> - Efficacite energetique WSN</li>
<li><a href="./microcontroleur_hardware.html">Microcontroleur &amp; Hardware - S9</a> - Consommation des microcontroleurs</li>
</ul>

<p><strong>Annee academique</strong> : 2024-2025<br>
<strong>Semestre</strong> : 9 (S9)<br>
<strong>Categorie</strong> : Energie et IoT<br>
<strong>Enseignant</strong> : G. Loubet</p>

<hr>

<h2>PART A - Presentation Generale</h2>

<h3 class="section-title">Vue d'ensemble</h3>

<p>Le cours "Energy for Connected Objects" porte sur les differentes methodes d'alimentation des objets connectes, un enjeu central dans le domaine de l'IoT. Dispense par G. Loubet a l'INSA Toulouse dans le cadre du parcours ISS (Innovative Smart Systems), ce module couvre la recuperation d'energie (energy harvesting), le transfert d'energie sans fil (Wireless Power Transfer), la gestion energetique efficace et le dimensionnement du budget energetique des systemes IoT.</p>

<p>L'objectif principal est de comprendre comment concevoir des systemes IoT autonomes energetiquement, capables de fonctionner sur de longues durees sans maintenance, en exploitant les sources d'energie ambiantes disponibles dans l'environnement.</p>

<h3 class="section-title">Objectifs pedagogiques</h3>

<ul>
<li>Comprendre les differentes sources d'energie ambiante exploitables pour l'IoT</li>
<li>Maitriser les principes de la recuperation d'energie (photovoltaique, thermique, mecanique, electromagnetique)</li>
<li>Concevoir un systeme de transfert d'energie sans fil (WPT)</li>
<li>Dimensionner le budget energetique complet d'un noeud IoT</li>
<li>Choisir et dimensionner les composants de gestion d'energie (regulateurs, supercondensateurs, batteries)</li>
<li>Selectionner et caracteriser des antennes pour la recuperation d'energie RF</li>
<li>Evaluer l'efficacite d'un systeme complet de recuperation et stockage d'energie</li>
</ul>

<h3 class="section-title">Organisation du module</h3>

<table>
<tr><th>Element</th><th>Details</th></tr>
<tr><td>Cours magistraux</td><td>Fondamentaux de l'energie pour l'IoT</td></tr>
<tr><td>Travaux pratiques</td><td>Experimentation WPT, mesures d'antennes, budget energetique</td></tr>
<tr><td>Projet</td><td>Application au projet innovant (What a Leak)</td></tr>
<tr><td>Evaluation</td><td>Rapport de TP et integration au projet</td></tr>
</table>

<hr>

<h2>PART B - Experience et Contexte</h2>

<h3 class="section-title">Environnement et contexte</h3>

<p>Ce cours s'inscrit dans un contexte ou la demande de solutions energetiquement autonomes pour les objets connectes ne cesse de croitre. Avec des milliards de capteurs deployes dans le monde pour des applications de surveillance environnementale, de maintenance predictive ou de villes intelligentes, la question de l'alimentation energetique devient critique. Remplacer des batteries sur des milliers de noeuds capteurs est economiquement et logistiquement intenable.</p>

<p>Le cours m'a permis d'explorer aussi bien les aspects theoriques (physique de la recuperation d'energie, equations de propagation, rendements thermodynamiques) que les aspects pratiques (mesures en laboratoire, tests d'antennes, calculs de bilan de liaison).</p>

<p>Les travaux pratiques se sont deroules en salle de TP avec du materiel de mesure RF (generateurs de signaux, analyseurs de spectre, antennes diverses) et des composants de gestion d'energie (rectifiers, regulateurs, supercondensateurs).</p>

<h3 class="section-title">Mon role</h3>

<p>Dans ce cours, j'ai ete responsable de :</p>
<ul>
<li>Etudier et comparer les differentes techniques de recuperation d'energie</li>
<li>Realiser des mesures de transfert d'energie sans fil a differentes frequences</li>
<li>Selectionner et caracteriser des antennes (patch vs whip) pour la recuperation d'energie RF</li>
<li>Calculer le budget energetique d'un noeud IoT dans le cadre du projet innovant</li>
<li>Evaluer la faisabilite de l'alimentation autonome pour notre projet "What a Leak"</li>
<li>Rediger un rapport technique detaillant les resultats experimentaux</li>
</ul>

<hr>

<h2>PART C - Aspects Techniques</h2>

<h3 class="section-title">1. Sources d'energie ambiante pour l'IoT</h3>

<p>L'une des premieres notions etudiees concerne les differentes sources d'energie disponibles dans l'environnement et exploitables pour alimenter des objets connectes. Chaque source presente des caracteristiques specifiques en termes de densite de puissance, de previsibilite et de conditions d'exploitation.</p>

<p><strong>Energie solaire (photovoltaique)</strong> :</p>

<p>La recuperation d'energie solaire repose sur l'effet photovoltaique. Les cellules solaires convertissent directement le rayonnement lumineux en electricite. C'est la source la plus mature et la plus efficace pour les applications en exterieur.</p>

<ul>
<li>Densite de puissance : 100 mW/cm2 en plein soleil, 0.1 mW/cm2 en interieur</li>
<li>Rendement des cellules : 15-25% (silicium cristallin), 5-10% (couches minces)</li>
<li>Avantages : haute densite de puissance, technologie mature</li>
<li>Inconvenients : intermittence (nuit, nuages), encombrement, degradation dans le temps</li>
</ul>

<p><strong>Energie thermique (thermoelectrique)</strong> :</p>

<p>Basee sur l'effet Seebeck, la recuperation thermoelectrique exploite les gradients de temperature entre deux faces d'un module Peltier pour generer de l'electricite.</p>

<ul>
<li>Densite de puissance : ~25 uW/cm2 pour un gradient de 5 degres C</li>
<li>Rendement typique : 1-5% du rendement de Carnot</li>
<li>Applications : capteurs sur machines industrielles, corps humain (wearables)</li>
<li>Limitation : necessite un gradient de temperature significatif et stable</li>
</ul>

<p><strong>Energie mecanique (piezoelectrique et electromagnetique)</strong> :</p>

<p>La recuperation d'energie mecanique exploite les vibrations, les mouvements ou les deformations pour generer de l'electricite via des materiaux piezoelectriques ou des systemes electromagnetiques (bobine + aimant).</p>

<ul>
<li>Densite de puissance : 1-300 uW/cm2 selon la source vibratoire</li>
<li>Applications : ponts, machines, mouvements humains</li>
<li>Avantages : disponible dans de nombreux environnements industriels</li>
<li>Inconvenients : puissance variable, dependance a la frequence de vibration</li>
</ul>

<p><strong>Energie radiofrequence (RF)</strong> :</p>

<p>La recuperation d'energie RF capte les ondes electromagnetiques ambiantes (WiFi, signaux cellulaires, broadcast TV/radio) et les convertit en electricite via une rectenna (antenne + redresseur).</p>

<ul>
<li>Densite de puissance : tres faible en ambiant (~0.1 uW/cm2), plus elevee avec source dediee</li>
<li>Frequences exploitees : 900 MHz, 2.4 GHz, 5.8 GHz</li>
<li>Avantages : disponible partout (en milieu urbain), transfert directionnel possible</li>
<li>Inconvenients : tres faible puissance recuperee, forte dependance a la distance</li>
</ul>

<p><strong>Tableau comparatif des sources d'energie</strong> :</p>

<table>
<tr><th>Source</th><th>Densite de puissance</th><th>Previsibilite</th><th>Maturite</th><th>Applications typiques</th></tr>
<tr><td>Solaire (exterieur)</td><td>100 mW/cm2</td><td>Moyenne</td><td>Elevee</td><td>Capteurs exterieurs</td></tr>
<tr><td>Solaire (interieur)</td><td>0.1 mW/cm2</td><td>Bonne</td><td>Elevee</td><td>Capteurs batiment</td></tr>
<tr><td>Thermique</td><td>25 uW/cm2</td><td>Bonne</td><td>Moyenne</td><td>Industriel, wearable</td></tr>
<tr><td>Vibrations</td><td>1-300 uW/cm2</td><td>Variable</td><td>Moyenne</td><td>Industriel</td></tr>
<tr><td>RF ambiante</td><td>0.1 uW/cm2</td><td>Bonne</td><td>Faible</td><td>Urbain, RFID</td></tr>
</table>

<h3 class="section-title">2. Transfert d'energie sans fil (Wireless Power Transfer)</h3>

<p>Le WPT (Wireless Power Transfer) est une technique qui permet de transmettre de l'energie electrique a distance sans cable, en utilisant des ondes electromagnetiques. Ce concept est fondamental pour alimenter des objets IoT difficiles d'acces ou pour recharger des batteries a distance.</p>

<p><strong>Principes physiques</strong> :</p>

<p>Le transfert d'energie sans fil repose sur la propagation des ondes electromagnetiques. L'equation de Friis est fondamentale pour calculer la puissance recue a une distance donnee :</p>

<pre><code>Pr = Pt * Gt * Gr * (lambda / (4 * pi * d))^2</code></pre>

<p>Ou :</p>
<ul>
<li>Pr : puissance recue (W)</li>
<li>Pt : puissance transmise (W)</li>
<li>Gt : gain de l'antenne d'emission</li>
<li>Gr : gain de l'antenne de reception</li>
<li>lambda : longueur d'onde (m)</li>
<li>d : distance entre les antennes (m)</li>
</ul>

<p>Cette equation montre que la puissance recue diminue en 1/d2 (loi en inverse du carre de la distance) et augmente avec la longueur d'onde (les basses frequences se propagent mieux).</p>

<p><strong>Experimentation en TP</strong> :</p>

<p>Lors des travaux pratiques, nous avons evalue la distance maximale de transfert de puissance a differentes frequences. Les resultats montrent clairement que :</p>
<ul>
<li>A 868 MHz : portee plus longue grace a une meilleure propagation</li>
<li>A 2.4 GHz : portee reduite mais antennes plus compactes</li>
<li>A 5.8 GHz : portee encore plus courte, attenuation plus forte</li>
</ul>

<div style="text-align: center; display: flex; justify-content: center; gap: 20px;">
    <div style="text-align: center;">
        <img src="/img/BE_Energy_Connected_Object/dist_8_6.png" style="max-width: 100%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
        <p style="font-style: italic; color: #666; margin-top: 10px;">
            Distance maximale de transfert a 868 MHz
        </p>
    </div>
    <div style="text-align: center;">
        <img src="/img/BE_Energy_Connected_Object/dist_2_4.png" style="max-width: 100%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
        <p style="font-style: italic; color: #666; margin-top: 10px;">
            Distance maximale de transfert a 2.4 GHz
        </p>
    </div>
</div>
<br>

<p>L'attenuation en espace libre (Free Space Path Loss - FSPL) augmente avec la frequence :</p>

<pre><code>FSPL (dB) = 20 * log10(d) + 20 * log10(f) + 20 * log10(4 * pi / c)</code></pre>

<p>En pratique, les resultats mesures montrent des distances de transfert significativement plus courtes qu'en theorie, dues aux reflexions, diffractions et absorptions dans l'environnement reel.</p>

<p><strong>Types de WPT</strong> :</p>

<table>
<tr><th>Type</th><th>Distance</th><th>Frequence</th><th>Puissance</th><th>Applications</th></tr>
<tr><td>Inductif (champ proche)</td><td>&lt; 10 cm</td><td>kHz-MHz</td><td>W a kW</td><td>Recharge smartphone, vehicules</td></tr>
<tr><td>Resonant (champ proche)</td><td>10 cm - 1 m</td><td>MHz</td><td>mW a W</td><td>Dispositifs medicaux</td></tr>
<tr><td>RF (champ lointain)</td><td>1 m - 10+ m</td><td>GHz</td><td>uW a mW</td><td>Capteurs IoT, RFID</td></tr>
</table>

<h3 class="section-title">3. Selection et caracterisation d'antennes</h3>

<p>Le choix de l'antenne est determinant pour l'efficacite du systeme de recuperation d'energie RF. Lors du cours et des TPs, nous avons compare deux types d'antennes principaux :</p>

<p><strong>Antenne patch (microstrip)</strong> :</p>

<p>L'antenne patch est une antenne planaire constituee d'un patch metallique sur un substrat dielectrique avec un plan de masse. Elle presente un diagramme de rayonnement directif.</p>

<ul>
<li>Gain typique : 5-8 dBi</li>
<li>Bande passante : etroite (1-5%)</li>
<li>Diagramme de rayonnement : directif (hemisphere)</li>
<li>Avantages : compacte, integrable sur PCB, gain eleve</li>
<li>Inconvenients : bande passante etroite, necesssite orientation vers la source</li>
</ul>

<p><strong>Antenne whip (monopole)</strong> :</p>

<p>L'antenne whip est un simple brin metallique vertical, generalement de longueur lambda/4, monte sur un plan de masse.</p>

<ul>
<li>Gain typique : 2-5 dBi</li>
<li>Bande passante : large</li>
<li>Diagramme de rayonnement : omnidirectionnel (plan horizontal)</li>
<li>Avantages : omnidirectionnelle, large bande, simple</li>
<li>Inconvenients : gain plus faible, encombrement en hauteur</li>
</ul>

<div style="text-align: center; display: flex; justify-content: center; gap: 20px;">
    <div style="text-align: center;">
        <img src="/img/BE_Energy_Connected_Object/Antenna1.png" style="max-width: 100%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
        <p style="font-style: italic; color: #666; margin-top: 10px;">
            Antenne patch - diagramme de rayonnement directif
        </p>
    </div>
    <div style="text-align: center;">
        <img src="/img/BE_Energy_Connected_Object/Antenna2.png" style="max-width: 100%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
        <p style="font-style: italic; color: #666; margin-top: 10px;">
            Antenne whip - diagramme de rayonnement omnidirectionnel
        </p>
    </div>
</div>
<br>

<p><strong>Criteres de choix</strong> :</p>

<p>Le choix entre ces deux types d'antennes depend du scenario d'utilisation :</p>

<table>
<tr><th>Critere</th><th>Patch</th><th>Whip</th></tr>
<tr><td>Mobilite de la source</td><td>Non adapte</td><td>Adapte</td></tr>
<tr><td>Gain maximal</td><td>Eleve (directif)</td><td>Moyen (omnidirectionnel)</td></tr>
<tr><td>Integration</td><td>Facile (planaire)</td><td>Moderee (3D)</td></tr>
<tr><td>Bande passante</td><td>Etroite</td><td>Large</td></tr>
<tr><td>Cas d'usage</td><td>Source fixe et connue</td><td>Source mobile ou inconnue</td></tr>
</table>

<p>Pour notre projet, le choix s'est porte sur l'antenne whip car la source d'energie RF n'etait pas dans une direction fixe et connue, necessitant une reception omnidirectionnelle.</p>

<h3 class="section-title">4. Chaine de recuperation d'energie RF</h3>

<p>La chaine complete de recuperation d'energie RF comprend plusieurs blocs fonctionnels :</p>

<p><strong>Architecture d'une rectenna</strong> :</p>

<pre><code>Antenne -> Filtre d'adaptation -> Redresseur (rectifier) -> Filtre DC -> Regulateur -> Charge (IoT)</code></pre>

<p><strong>Antenne</strong> : Capte les ondes electromagnetiques et les convertit en signal RF.</p>

<p><strong>Circuit d'adaptation d'impedance</strong> : Assure le transfert maximal de puissance entre l'antenne (typiquement 50 ohms) et le redresseur. L'adaptation est cruciale car toute desadaptation entraine des pertes par reflexion.</p>

<p><strong>Redresseur (rectifier)</strong> : Convertit le signal RF alternatif en tension continue. Les diodes Schottky sont privilegiees pour leur faible tension de seuil (~0.2V) et leur rapidite de commutation. Les architectures courantes sont :</p>
<ul>
<li>Simple diode (half-wave)</li>
<li>Doubleur de tension (Villard/Greinacher)</li>
<li>Multiplicateur de tension (Dickson)</li>
</ul>

<p><strong>Filtre DC</strong> : Lisse la tension redessee et elimine les composantes RF residuelles.</p>

<p><strong>Regulateur</strong> : Adapte la tension de sortie aux besoins de la charge. Des circuits de gestion d'energie dedies (PMIC - Power Management IC) comme le BQ25570 de Texas Instruments sont concus pour fonctionner avec des niveaux de puissance ultra-faibles.</p>

<p><strong>Rendement global</strong> : Le rendement de la chaine complete est le produit des rendements de chaque etage :</p>

<pre><code>eta_total = eta_antenne * eta_adaptation * eta_redresseur * eta_regulateur</code></pre>

<p>En pratique, le rendement global est souvent de l'ordre de 10-40% pour une rectenna bien concue, et il varie fortement avec le niveau de puissance d'entree.</p>

<h3 class="section-title">5. Budget energetique d'un noeud IoT</h3>

<p>Le dimensionnement du budget energetique est une etape essentielle dans la conception d'un systeme IoT autonome. Il s'agit de quantifier precisement la consommation de chaque composant et de chaque phase de fonctionnement.</p>

<p><strong>Modes de fonctionnement d'un noeud IoT</strong> :</p>

<p>Un noeud IoT typique alterne entre plusieurs modes de fonctionnement :</p>

<table>
<tr><th>Mode</th><th>Consommation typique</th><th>Duree typique</th></tr>
<tr><td>Deep Sleep</td><td>1-10 uA</td><td>Minutes a heures</td></tr>
<tr><td>Wake-up</td><td>1-5 mA</td><td>Quelques ms</td></tr>
<tr><td>Mesure capteur</td><td>1-50 mA</td><td>10-100 ms</td></tr>
<tr><td>Traitement (MCU actif)</td><td>5-50 mA</td><td>1-100 ms</td></tr>
<tr><td>Transmission radio</td><td>20-200 mA</td><td>10-100 ms</td></tr>
<tr><td>Reception radio</td><td>10-50 mA</td><td>Variable</td></tr>
</table>

<p><strong>Calcul de la consommation moyenne</strong> :</p>

<p>La consommation moyenne se calcule en pondorant chaque mode par sa duree :</p>

<pre><code>I_moyen = (I_sleep * T_sleep + I_actif * T_actif + I_tx * T_tx) / T_cycle</code></pre>

<p>Ou T_cycle = T_sleep + T_actif + T_tx est la periode totale d'un cycle.</p>

<p><strong>Exemple de calcul</strong> :</p>

<p>Pour un capteur qui se reveille toutes les 10 minutes, mesure pendant 50 ms et transmet pendant 100 ms :</p>
<ul>
<li>Sleep : 5 uA pendant 599.85 s</li>
<li>Actif : 10 mA pendant 50 ms</li>
<li>TX : 100 mA pendant 100 ms</li>
</ul>

<pre><code>I_moyen = (5e-6 * 599.85 + 10e-3 * 0.05 + 100e-3 * 0.1) / 600
I_moyen = (2.999e-3 + 0.5e-3 + 10e-3) / 600
I_moyen = 22.5 uA</code></pre>

<p><strong>Dimensionnement du stockage</strong> :</p>

<p>Pour une autonomie cible de T heures :</p>

<pre><code>C_batterie (mAh) = I_moyen (mA) * T (h) * facteur_securite</code></pre>

<p>Le facteur de securite (typiquement 1.2-1.5) compense la degradation de la batterie, les variations de temperature et les pics de consommation imprevus.</p>

<p><strong>Equilibre energetique pour un systeme autonome</strong> :</p>

<p>Pour un systeme alimente par recuperation d'energie, la condition d'autonomie est :</p>

<pre><code>P_recuperee_moyenne >= P_consommee_moyenne</code></pre>

<p>Si cette condition n'est pas satisfaite en permanence, un element de stockage (batterie, supercondensateur) doit compenser les periodes deficitaires.</p>

<h3 class="section-title">6. Stockage d'energie</h3>

<p>Le choix du systeme de stockage est crucial et depend des besoins en energie, en puissance et en duree de vie.</p>

<p><strong>Batteries</strong> :</p>

<ul>
<li>Lithium-ion : haute densite energetique (150-250 Wh/kg), 500-1000 cycles</li>
<li>Lithium-polymere : forme flexible, densite similaire au Li-ion</li>
<li>Lithium-primaire (non rechargeable) : tres haute densite, longue duree de vie (10+ ans)</li>
<li>Limitation : nombre de cycles limite, degradation avec le temps, sensibilite a la temperature</li>
</ul>

<p><strong>Supercondensateurs</strong> :</p>

<ul>
<li>Densite de puissance elevee (jusqu'a 10 kW/kg)</li>
<li>Nombre de cycles quasi-illimite (&gt;500 000 cycles)</li>
<li>Charge/decharge rapide</li>
<li>Faible densite energetique (5-10 Wh/kg)</li>
<li>Adaptes aux pics de puissance et aux systemes de recuperation d'energie intermittente</li>
</ul>

<p><strong>Comparaison</strong> :</p>

<table>
<tr><th>Critere</th><th>Batterie Li-ion</th><th>Supercondensateur</th></tr>
<tr><td>Densite energetique</td><td>150-250 Wh/kg</td><td>5-10 Wh/kg</td></tr>
<tr><td>Densite de puissance</td><td>0.3-1.5 kW/kg</td><td>1-10 kW/kg</td></tr>
<tr><td>Cycles de vie</td><td>500-1000</td><td>&gt;500 000</td></tr>
<tr><td>Auto-decharge</td><td>2-5%/mois</td><td>5-40%/jour</td></tr>
<tr><td>Temps de charge</td><td>Heures</td><td>Secondes</td></tr>
</table>

<h3 class="section-title">7. Gestion d'energie (Power Management)</h3>

<p>La gestion d'energie est le pont entre la source d'energie (recuperation ou batterie) et la charge (noeud IoT). Elle assure la regulation, la protection et l'optimisation du flux energetique.</p>

<p><strong>Composants cles</strong> :</p>

<p><strong>Regulateurs lineaires (LDO)</strong> :</p>
<ul>
<li>Simples, faible bruit</li>
<li>Rendement : eta = Vout/Vin (faible si grande difference)</li>
<li>Adaptes quand Vin est proche de Vout</li>
</ul>

<p><strong>Regulateurs a decoupage (DC-DC)</strong> :</p>
<ul>
<li>Buck (abaisseur) : Vout &lt; Vin</li>
<li>Boost (eleveur) : Vout &gt; Vin</li>
<li>Buck-boost : Vout peut etre superieur ou inferieur a Vin</li>
<li>Rendement eleve : 85-95%</li>
<li>Bruit de commutation a filtrer</li>
</ul>

<p><strong>PMIC dedies IoT</strong> :</p>

<p>Des circuits integres comme le BQ25570 (Texas Instruments) ou le AEM10941 (e-peas) sont specialement concus pour la recuperation d'energie ultra-faible. Ils integrent :</p>
<ul>
<li>Un boost converter avec seuil de demarrage tres bas (~100 mV)</li>
<li>Un MPPT (Maximum Power Point Tracking) pour optimiser l'extraction d'energie</li>
<li>Un chargeur de batterie/supercondensateur</li>
<li>Un regulateur de sortie</li>
</ul>

<p><strong>MPPT (Maximum Power Point Tracking)</strong> :</p>

<p>Le MPPT est un algorithme qui ajuste dynamiquement le point de fonctionnement du systeme de recuperation pour extraire la puissance maximale. Pour les cellules solaires, le point de puissance maximale correspond typiquement a 70-80% de la tension en circuit ouvert (Voc).</p>

<h3 class="section-title">8. Application au projet : What a Leak</h3>

<p>Dans le cadre de notre <a href="./innovative-project.html">projet innovant (What a Leak)</a>, nous avons cherche a appliquer les concepts du cours pour concevoir un systeme de detection de fuites d'eau autonome energetiquement.</p>

<p><strong>Objectif</strong> : Alimenter un noeud capteur (detecteur de fuite) par recuperation d'energie, elimiant la necessite de changement de batterie dans des emplacements difficiles d'acces (sous des eviers, dans des combles, etc.).</p>

<p><strong>Contraintes</strong> :</p>
<ul>
<li>Environnement interieur (faible luminosite, pas de vent)</li>
<li>Faible gradient de temperature</li>
<li>Ondes RF ambiantes faibles</li>
<li>Besoin de transmission periodique des donnees</li>
</ul>

<p><strong>Evaluation des sources</strong> :</p>

<p>Nous avons evalue chaque source d'energie pour notre cas d'usage specifique. Malheureusement, l'environnement interieur typique ne fournit pas suffisamment d'energie ambiante pour alimenter de maniere fiable notre noeud capteur. Les niveaux de puissance RF ambiants sont trop faibles et l'eclairage interieur ne genere pas assez de puissance avec de petites cellules solaires.</p>

<p>Cette analyse, bien que concluant a l'impossibilite pratique d'un systeme totalement autonome dans notre cas, a ete tres formatrice. Elle m'a appris a evaluer rigoureusement la faisabilite energetique d'un systeme avant de se lancer dans la conception.</p>

<hr>

<h2>PART D - Analyse et Reflexion</h2>

<h3 class="section-title">Competences acquises</h3>

<p><strong>Comprehension energetique globale</strong> :<br>
Capacite a identifier, evaluer et comparer les differentes sources d'energie ambiante pour des applications IoT, et a choisir la plus adaptee selon le contexte de deploiement.</p>

<p><strong>Dimensionnement de systemes</strong> :<br>
Aptitude a calculer un budget energetique complet, du capteur a la transmission, en tenant compte de tous les modes de fonctionnement et de leur duree.</p>

<p><strong>Conception RF</strong> :<br>
Connaissance des principes de propagation des ondes, de la formule de Friis, et capacite a selectionner et caracteriser des antennes pour la recuperation d'energie.</p>

<p><strong>Gestion d'energie</strong> :<br>
Comprehension des architectures de gestion d'energie (LDO, DC-DC, PMIC) et de leur adequation aux differents scenarios de recuperation d'energie.</p>

<p><strong>Approche experimentale</strong> :<br>
Competence pour realiser des mesures de transfert d'energie sans fil, interpreter les resultats et les comparer aux modeles theoriques.</p>

<h3 class="section-title">Auto-evaluation</h3>

<p>Ce cours m'a apporte beaucoup de connaissances nouvelles sur un sujet que je ne connaissais pas avant. J'ai decouvert l'etendue des possibilites pour alimenter des objets connectes a partir de l'energie ambiante, qu'il s'agisse de la lumiere, de la chaleur, des vibrations ou des ondes electromagnetiques.</p>

<p>Les travaux pratiques ont ete particulierement enrichissants. Nous avons etudie les besoins en puissance d'une petite LED rouge, teste des approches d'utilisation directe de l'energie et de stockage. Ces experimentations m'ont permis de confronter la theorie a la realite et de comprendre les limites pratiques de la recuperation d'energie.</p>

<p>J'aurais aime pouvoir appliquer davantage ces concepts a un projet concret. Si le projet innovant visait cet objectif, l'environnement de deploiement ne nous a pas permis de recuperer suffisamment d'energie ambiante. Cette limitation a toutefois ete formatrice : elle m'a appris que l'evaluation de faisabilite energetique est une etape critique dans tout projet IoT.</p>

<p>Les sessions de TP sur les antennes m'ont egalement permis de comprendre l'importance du choix de l'antenne et de son positionnement. C'est un aspect souvent neglige dans les projets IoT mais qui peut faire la difference entre un systeme fonctionnel et un systeme defaillant.</p>

<h3 class="section-title">Applications professionnelles</h3>

<p>Les competences acquises dans ce cours sont directement applicables dans de nombreux domaines :</p>

<p><strong>IoT industriel</strong> :</p>
<ul>
<li>Capteurs autonomes pour la maintenance predictive</li>
<li>Surveillance d'equipements dans des zones difficiles d'acces</li>
<li>Monitoring environnemental longue duree</li>
</ul>

<p><strong>Smart Building</strong> :</p>
<ul>
<li>Capteurs de temperature, humidite, qualite d'air sans cablage</li>
<li>Interrupteurs sans pile (piezoelectrique)</li>
<li>Compteurs de personnes autonomes</li>
</ul>

<p><strong>Sante connectee</strong> :</p>
<ul>
<li>Wearables alimentes par l'energie du corps</li>
<li>Implants medicaux avec recuperation d'energie sans fil</li>
<li>Monitoring patient en continu</li>
</ul>

<p><strong>Agriculture de precision</strong> :</p>
<ul>
<li>Capteurs de sol autonomes (solaire)</li>
<li>Surveillance des cultures sur de grandes surfaces</li>
<li>Stations meteo connectees</li>
</ul>

<h3 class="section-title">Mon avis</h3>

<p>Ce cours m'a permis de comprendre des aspects de l'IoT que je ne soupconnais pas. Par exemple, la grande variete de possibilites pour alimenter des objets avec des ondes electromagnetiques et d'autres sources d'energie disponibles dans notre environnement. De plus, apprendre a choisir une antenne et comprendre ses principes de fonctionnement etait particulierement interessant.</p>

<p>La combinaison de la theorie et de la pratique etait bien equilibree. Le cours magistral fournissait les bases necessaires, et les TPs permettaient de verifier ces concepts experimentalement. J'ai particulierement apprecie la methodologie rigoureuse pour le calcul du budget energetique, qui est une competence directement transferable a tout projet IoT.</p>

<p>Ce module m'a donne une vision plus complete de la conception de systemes IoT, en integrant la dimension energetique des le debut du processus de conception.</p>

<hr>

<h2>Documents de Cours</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Cours - Energy for IoT</h4>
      <p>Cours complet : sources d'energie ambiante, recuperation d'energie, transfert sans fil, gestion d'energie et budget energetique pour les objets connectes.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S9/Energy/5ISS_Energy_for_IoT.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S9/Energy/5ISS_Energy_for_IoT.pdf" target="_blank">Telecharger le cours</a></p>
    </div>
  </div>
</div>

<hr>

<h2>Rapports et Projets</h2>

<div style="text-align: center;">
    <h3>Rapport de TP - Energy for Connected Objects</h3>
</div>

<div style="display: flex; justify-content: center;">
    <embed src="/file/reports/S9/Report_Energy_Boukouiss_Chanfreau.pdf" width="100%" height="800px" type="application/pdf">
</div>

<p style="text-align: center;">
    <a href="/file/reports/S9/Report_Energy_Boukouiss_Chanfreau.pdf" target="_blank">Ouvrir le rapport complet</a>
</p>

<div style="text-align: center;">
    <h3>Sujet de TP</h3>
</div>

<div style="display: flex; justify-content: center;">
    <embed src="/img/BE_Energy_Connected_Object/Lab_Subject_energy.pdf" width="100%" height="800px" type="application/pdf">
</div>

<p style="text-align: center;">
    <a href="/img/BE_Energy_Connected_Object/Lab_Subject_energy.pdf" target="_blank">Ouvrir le sujet de TP</a>
</p>

<hr>
<p><em>Cours suivi en 2024-2025 a l'INSA Toulouse, Departement Genie Electrique et Informatique, parcours ISS (Innovative Smart Systems).</em></p>

</div>

<div class="lang-en">

<h1>Energy for Connected Objects - Semester 9</h1>

<p><strong>Related courses</strong>:</p>
<ul>
<li><a href="./embedded-ia-iot.html">Embedded IA for IoT - S9</a> - Energy optimization for AI</li>
<li><a href="./wireless-sensors.html">Wireless Sensors Networks - S9</a> - WSN energy efficiency</li>
<li><a href="./microcontroleur_hardware.html">Microcontroller &amp; Hardware - S9</a> - Microcontroller power consumption</li>
</ul>

<p><strong>Academic year</strong>: 2024-2025<br>
<strong>Semester</strong>: 9 (S9)<br>
<strong>Category</strong>: Energy and IoT<br>
<strong>Instructor</strong>: G. Loubet</p>

<hr>

<h2>PART A - General Presentation</h2>

<h3 class="section-title">Overview</h3>

<p>The "Energy for Connected Objects" course covers the different methods of powering connected objects, a central challenge in the IoT domain. Taught by G. Loubet at INSA Toulouse as part of the ISS (Innovative Smart Systems) program, this module covers energy harvesting, Wireless Power Transfer (WPT), efficient energy management, and energy budget sizing for IoT systems.</p>

<p>The main objective is to understand how to design energy-autonomous IoT systems, capable of operating over long periods without maintenance, by exploiting ambient energy sources available in the environment.</p>

<h3 class="section-title">Learning objectives</h3>

<ul>
<li>Understand the different ambient energy sources exploitable for IoT</li>
<li>Master the principles of energy harvesting (photovoltaic, thermal, mechanical, electromagnetic)</li>
<li>Design a wireless power transfer (WPT) system</li>
<li>Size the complete energy budget of an IoT node</li>
<li>Select and size power management components (regulators, supercapacitors, batteries)</li>
<li>Select and characterize antennas for RF energy harvesting</li>
<li>Evaluate the efficiency of a complete energy harvesting and storage system</li>
</ul>

<h3 class="section-title">Module organization</h3>

<table>
<tr><th>Element</th><th>Details</th></tr>
<tr><td>Lectures</td><td>Fundamentals of energy for IoT</td></tr>
<tr><td>Lab sessions</td><td>WPT experimentation, antenna measurements, energy budget</td></tr>
<tr><td>Project</td><td>Application to the innovative project (What a Leak)</td></tr>
<tr><td>Assessment</td><td>Lab report and project integration</td></tr>
</table>

<hr>

<h2>PART B - Experience and Context</h2>

<h3 class="section-title">Environment and context</h3>

<p>This course takes place in a context where the demand for energy-autonomous solutions for connected objects continues to grow. With billions of sensors deployed worldwide for environmental monitoring, predictive maintenance, or smart city applications, the question of energy supply becomes critical. Replacing batteries on thousands of sensor nodes is economically and logistically unsustainable.</p>

<p>The course allowed me to explore both theoretical aspects (physics of energy harvesting, propagation equations, thermodynamic efficiencies) and practical aspects (laboratory measurements, antenna testing, link budget calculations).</p>

<p>The lab sessions took place in the lab room with RF measurement equipment (signal generators, spectrum analyzers, various antennas) and power management components (rectifiers, regulators, supercapacitors).</p>

<h3 class="section-title">My role</h3>

<p>In this course, I was responsible for:</p>
<ul>
<li>Studying and comparing different energy harvesting techniques</li>
<li>Performing wireless power transfer measurements at different frequencies</li>
<li>Selecting and characterizing antennas (patch vs whip) for RF energy harvesting</li>
<li>Calculating the energy budget of an IoT node as part of the innovative project</li>
<li>Evaluating the feasibility of autonomous power supply for our "What a Leak" project</li>
<li>Writing a technical report detailing the experimental results</li>
</ul>

<hr>

<h2>PART C - Technical Aspects</h2>

<h3 class="section-title">1. Ambient energy sources for IoT</h3>

<p>One of the first concepts studied concerns the different energy sources available in the environment and exploitable to power connected objects. Each source has specific characteristics in terms of power density, predictability, and operating conditions.</p>

<p><strong>Solar energy (photovoltaic)</strong>:</p>

<p>Solar energy harvesting is based on the photovoltaic effect. Solar cells directly convert light radiation into electricity. It is the most mature and efficient source for outdoor applications.</p>

<ul>
<li>Power density: 100 mW/cm2 in full sunlight, 0.1 mW/cm2 indoors</li>
<li>Cell efficiency: 15-25% (crystalline silicon), 5-10% (thin film)</li>
<li>Advantages: high power density, mature technology</li>
<li>Disadvantages: intermittency (night, clouds), bulkiness, degradation over time</li>
</ul>

<p><strong>Thermal energy (thermoelectric)</strong>:</p>

<p>Based on the Seebeck effect, thermoelectric harvesting exploits temperature gradients between two faces of a Peltier module to generate electricity.</p>

<ul>
<li>Power density: ~25 uW/cm2 for a 5-degree C gradient</li>
<li>Typical efficiency: 1-5% of Carnot efficiency</li>
<li>Applications: sensors on industrial machines, human body (wearables)</li>
<li>Limitation: requires a significant and stable temperature gradient</li>
</ul>

<p><strong>Mechanical energy (piezoelectric and electromagnetic)</strong>:</p>

<p>Mechanical energy harvesting exploits vibrations, movements, or deformations to generate electricity via piezoelectric materials or electromagnetic systems (coil + magnet).</p>

<ul>
<li>Power density: 1-300 uW/cm2 depending on the vibration source</li>
<li>Applications: bridges, machines, human movements</li>
<li>Advantages: available in many industrial environments</li>
<li>Disadvantages: variable power, dependence on vibration frequency</li>
</ul>

<p><strong>Radiofrequency (RF) energy</strong>:</p>

<p>RF energy harvesting captures ambient electromagnetic waves (WiFi, cellular signals, TV/radio broadcast) and converts them into electricity via a rectenna (antenna + rectifier).</p>

<ul>
<li>Power density: very low in ambient conditions (~0.1 uW/cm2), higher with a dedicated source</li>
<li>Exploited frequencies: 900 MHz, 2.4 GHz, 5.8 GHz</li>
<li>Advantages: available everywhere (in urban areas), directional transfer possible</li>
<li>Disadvantages: very low harvested power, strong dependence on distance</li>
</ul>

<p><strong>Comparative table of energy sources</strong>:</p>

<table>
<tr><th>Source</th><th>Power density</th><th>Predictability</th><th>Maturity</th><th>Typical applications</th></tr>
<tr><td>Solar (outdoor)</td><td>100 mW/cm2</td><td>Medium</td><td>High</td><td>Outdoor sensors</td></tr>
<tr><td>Solar (indoor)</td><td>0.1 mW/cm2</td><td>Good</td><td>High</td><td>Building sensors</td></tr>
<tr><td>Thermal</td><td>25 uW/cm2</td><td>Good</td><td>Medium</td><td>Industrial, wearable</td></tr>
<tr><td>Vibrations</td><td>1-300 uW/cm2</td><td>Variable</td><td>Medium</td><td>Industrial</td></tr>
<tr><td>Ambient RF</td><td>0.1 uW/cm2</td><td>Good</td><td>Low</td><td>Urban, RFID</td></tr>
</table>

<h3 class="section-title">2. Wireless Power Transfer (WPT)</h3>

<p>WPT (Wireless Power Transfer) is a technique that allows transmitting electrical energy over a distance without cables, using electromagnetic waves. This concept is fundamental for powering hard-to-access IoT objects or for recharging batteries remotely.</p>

<p><strong>Physical principles</strong>:</p>

<p>Wireless power transfer relies on the propagation of electromagnetic waves. The Friis equation is fundamental for calculating the received power at a given distance:</p>

<pre><code>Pr = Pt * Gt * Gr * (lambda / (4 * pi * d))^2</code></pre>

<p>Where:</p>
<ul>
<li>Pr: received power (W)</li>
<li>Pt: transmitted power (W)</li>
<li>Gt: transmitting antenna gain</li>
<li>Gr: receiving antenna gain</li>
<li>lambda: wavelength (m)</li>
<li>d: distance between antennas (m)</li>
</ul>

<p>This equation shows that the received power decreases as 1/d2 (inverse square law) and increases with wavelength (lower frequencies propagate better).</p>

<p><strong>Lab experimentation</strong>:</p>

<p>During the lab sessions, we evaluated the maximum power transfer distance at different frequencies. The results clearly show that:</p>
<ul>
<li>At 868 MHz: longer range thanks to better propagation</li>
<li>At 2.4 GHz: reduced range but more compact antennas</li>
<li>At 5.8 GHz: even shorter range, stronger attenuation</li>
</ul>

<div style="text-align: center; display: flex; justify-content: center; gap: 20px;">
    <div style="text-align: center;">
        <img src="/img/BE_Energy_Connected_Object/dist_8_6.png" style="max-width: 100%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
        <p style="font-style: italic; color: #666; margin-top: 10px;">
            Maximum transfer distance at 868 MHz
        </p>
    </div>
    <div style="text-align: center;">
        <img src="/img/BE_Energy_Connected_Object/dist_2_4.png" style="max-width: 100%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
        <p style="font-style: italic; color: #666; margin-top: 10px;">
            Maximum transfer distance at 2.4 GHz
        </p>
    </div>
</div>
<br>

<p>Free Space Path Loss (FSPL) increases with frequency:</p>

<pre><code>FSPL (dB) = 20 * log10(d) + 20 * log10(f) + 20 * log10(4 * pi / c)</code></pre>

<p>In practice, measured results show significantly shorter transfer distances than in theory, due to reflections, diffractions, and absorptions in the real environment.</p>

<p><strong>Types of WPT</strong>:</p>

<table>
<tr><th>Type</th><th>Distance</th><th>Frequency</th><th>Power</th><th>Applications</th></tr>
<tr><td>Inductive (near field)</td><td>&lt; 10 cm</td><td>kHz-MHz</td><td>W to kW</td><td>Smartphone charging, vehicles</td></tr>
<tr><td>Resonant (near field)</td><td>10 cm - 1 m</td><td>MHz</td><td>mW to W</td><td>Medical devices</td></tr>
<tr><td>RF (far field)</td><td>1 m - 10+ m</td><td>GHz</td><td>uW to mW</td><td>IoT sensors, RFID</td></tr>
</table>

<h3 class="section-title">3. Antenna selection and characterization</h3>

<p>The choice of antenna is decisive for the efficiency of the RF energy harvesting system. During the course and lab sessions, we compared two main types of antennas:</p>

<p><strong>Patch antenna (microstrip)</strong>:</p>

<p>The patch antenna is a planar antenna consisting of a metallic patch on a dielectric substrate with a ground plane. It has a directive radiation pattern.</p>

<ul>
<li>Typical gain: 5-8 dBi</li>
<li>Bandwidth: narrow (1-5%)</li>
<li>Radiation pattern: directive (hemisphere)</li>
<li>Advantages: compact, PCB-integrable, high gain</li>
<li>Disadvantages: narrow bandwidth, requires orientation toward the source</li>
</ul>

<p><strong>Whip antenna (monopole)</strong>:</p>

<p>The whip antenna is a simple vertical metallic rod, generally lambda/4 in length, mounted on a ground plane.</p>

<ul>
<li>Typical gain: 2-5 dBi</li>
<li>Bandwidth: wide</li>
<li>Radiation pattern: omnidirectional (horizontal plane)</li>
<li>Advantages: omnidirectional, wideband, simple</li>
<li>Disadvantages: lower gain, vertical height footprint</li>
</ul>

<div style="text-align: center; display: flex; justify-content: center; gap: 20px;">
    <div style="text-align: center;">
        <img src="/img/BE_Energy_Connected_Object/Antenna1.png" style="max-width: 100%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
        <p style="font-style: italic; color: #666; margin-top: 10px;">
            Patch antenna - directive radiation pattern
        </p>
    </div>
    <div style="text-align: center;">
        <img src="/img/BE_Energy_Connected_Object/Antenna2.png" style="max-width: 100%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
        <p style="font-style: italic; color: #666; margin-top: 10px;">
            Whip antenna - omnidirectional radiation pattern
        </p>
    </div>
</div>
<br>

<p><strong>Selection criteria</strong>:</p>

<p>The choice between these two types of antennas depends on the usage scenario:</p>

<table>
<tr><th>Criterion</th><th>Patch</th><th>Whip</th></tr>
<tr><td>Source mobility</td><td>Not suitable</td><td>Suitable</td></tr>
<tr><td>Maximum gain</td><td>High (directive)</td><td>Medium (omnidirectional)</td></tr>
<tr><td>Integration</td><td>Easy (planar)</td><td>Moderate (3D)</td></tr>
<tr><td>Bandwidth</td><td>Narrow</td><td>Wide</td></tr>
<tr><td>Use case</td><td>Fixed and known source</td><td>Mobile or unknown source</td></tr>
</table>

<p>For our project, the whip antenna was chosen because the RF energy source was not in a fixed and known direction, requiring omnidirectional reception.</p>

<h3 class="section-title">4. RF energy harvesting chain</h3>

<p>The complete RF energy harvesting chain comprises several functional blocks:</p>

<p><strong>Rectenna architecture</strong>:</p>

<pre><code>Antenna -> Matching filter -> Rectifier -> DC filter -> Regulator -> Load (IoT)</code></pre>

<p><strong>Antenna</strong>: Captures electromagnetic waves and converts them into an RF signal.</p>

<p><strong>Impedance matching circuit</strong>: Ensures maximum power transfer between the antenna (typically 50 ohms) and the rectifier. Matching is crucial because any mismatch causes reflection losses.</p>

<p><strong>Rectifier</strong>: Converts the alternating RF signal into DC voltage. Schottky diodes are preferred for their low threshold voltage (~0.2V) and fast switching speed. Common architectures include:</p>
<ul>
<li>Single diode (half-wave)</li>
<li>Voltage doubler (Villard/Greinacher)</li>
<li>Voltage multiplier (Dickson)</li>
</ul>

<p><strong>DC filter</strong>: Smooths the rectified voltage and eliminates residual RF components.</p>

<p><strong>Regulator</strong>: Adapts the output voltage to the load requirements. Dedicated power management ICs (PMIC - Power Management IC) such as the BQ25570 from Texas Instruments are designed to operate with ultra-low power levels.</p>

<p><strong>Overall efficiency</strong>: The efficiency of the complete chain is the product of each stage's efficiency:</p>

<pre><code>eta_total = eta_antenna * eta_matching * eta_rectifier * eta_regulator</code></pre>

<p>In practice, the overall efficiency is typically in the range of 10-40% for a well-designed rectenna, and it varies significantly with the input power level.</p>

<h3 class="section-title">5. IoT node energy budget</h3>

<p>Energy budget sizing is an essential step in designing an autonomous IoT system. It involves precisely quantifying the consumption of each component and each operating phase.</p>

<p><strong>IoT node operating modes</strong>:</p>

<p>A typical IoT node alternates between several operating modes:</p>

<table>
<tr><th>Mode</th><th>Typical consumption</th><th>Typical duration</th></tr>
<tr><td>Deep Sleep</td><td>1-10 uA</td><td>Minutes to hours</td></tr>
<tr><td>Wake-up</td><td>1-5 mA</td><td>A few ms</td></tr>
<tr><td>Sensor measurement</td><td>1-50 mA</td><td>10-100 ms</td></tr>
<tr><td>Processing (MCU active)</td><td>5-50 mA</td><td>1-100 ms</td></tr>
<tr><td>Radio transmission</td><td>20-200 mA</td><td>10-100 ms</td></tr>
<tr><td>Radio reception</td><td>10-50 mA</td><td>Variable</td></tr>
</table>

<p><strong>Average consumption calculation</strong>:</p>

<p>The average consumption is calculated by weighting each mode by its duration:</p>

<pre><code>I_avg = (I_sleep * T_sleep + I_active * T_active + I_tx * T_tx) / T_cycle</code></pre>

<p>Where T_cycle = T_sleep + T_active + T_tx is the total period of one cycle.</p>

<p><strong>Calculation example</strong>:</p>

<p>For a sensor that wakes up every 10 minutes, measures for 50 ms, and transmits for 100 ms:</p>
<ul>
<li>Sleep: 5 uA for 599.85 s</li>
<li>Active: 10 mA for 50 ms</li>
<li>TX: 100 mA for 100 ms</li>
</ul>

<pre><code>I_avg = (5e-6 * 599.85 + 10e-3 * 0.05 + 100e-3 * 0.1) / 600
I_avg = (2.999e-3 + 0.5e-3 + 10e-3) / 600
I_avg = 22.5 uA</code></pre>

<p><strong>Storage sizing</strong>:</p>

<p>For a target autonomy of T hours:</p>

<pre><code>C_battery (mAh) = I_avg (mA) * T (h) * safety_factor</code></pre>

<p>The safety factor (typically 1.2-1.5) compensates for battery degradation, temperature variations, and unexpected consumption peaks.</p>

<p><strong>Energy balance for an autonomous system</strong>:</p>

<p>For a system powered by energy harvesting, the autonomy condition is:</p>

<pre><code>P_harvested_average >= P_consumed_average</code></pre>

<p>If this condition is not met at all times, a storage element (battery, supercapacitor) must compensate for deficit periods.</p>

<h3 class="section-title">6. Energy storage</h3>

<p>The choice of storage system is crucial and depends on energy, power, and lifetime requirements.</p>

<p><strong>Batteries</strong>:</p>

<ul>
<li>Lithium-ion: high energy density (150-250 Wh/kg), 500-1000 cycles</li>
<li>Lithium-polymer: flexible form, density similar to Li-ion</li>
<li>Primary lithium (non-rechargeable): very high density, long lifespan (10+ years)</li>
<li>Limitation: limited number of cycles, degradation over time, temperature sensitivity</li>
</ul>

<p><strong>Supercapacitors</strong>:</p>

<ul>
<li>High power density (up to 10 kW/kg)</li>
<li>Nearly unlimited number of cycles (&gt;500,000 cycles)</li>
<li>Fast charge/discharge</li>
<li>Low energy density (5-10 Wh/kg)</li>
<li>Suitable for power peaks and intermittent energy harvesting systems</li>
</ul>

<p><strong>Comparison</strong>:</p>

<table>
<tr><th>Criterion</th><th>Li-ion Battery</th><th>Supercapacitor</th></tr>
<tr><td>Energy density</td><td>150-250 Wh/kg</td><td>5-10 Wh/kg</td></tr>
<tr><td>Power density</td><td>0.3-1.5 kW/kg</td><td>1-10 kW/kg</td></tr>
<tr><td>Cycle life</td><td>500-1000</td><td>&gt;500,000</td></tr>
<tr><td>Self-discharge</td><td>2-5%/month</td><td>5-40%/day</td></tr>
<tr><td>Charge time</td><td>Hours</td><td>Seconds</td></tr>
</table>

<h3 class="section-title">7. Power management</h3>

<p>Power management is the bridge between the energy source (harvesting or battery) and the load (IoT node). It ensures regulation, protection, and optimization of the energy flow.</p>

<p><strong>Key components</strong>:</p>

<p><strong>Linear regulators (LDO)</strong>:</p>
<ul>
<li>Simple, low noise</li>
<li>Efficiency: eta = Vout/Vin (low if large difference)</li>
<li>Suitable when Vin is close to Vout</li>
</ul>

<p><strong>Switching regulators (DC-DC)</strong>:</p>
<ul>
<li>Buck (step-down): Vout &lt; Vin</li>
<li>Boost (step-up): Vout &gt; Vin</li>
<li>Buck-boost: Vout can be higher or lower than Vin</li>
<li>High efficiency: 85-95%</li>
<li>Switching noise to filter</li>
</ul>

<p><strong>IoT-dedicated PMICs</strong>:</p>

<p>Integrated circuits such as the BQ25570 (Texas Instruments) or the AEM10941 (e-peas) are specially designed for ultra-low energy harvesting. They integrate:</p>
<ul>
<li>A boost converter with a very low startup threshold (~100 mV)</li>
<li>An MPPT (Maximum Power Point Tracking) to optimize energy extraction</li>
<li>A battery/supercapacitor charger</li>
<li>An output regulator</li>
</ul>

<p><strong>MPPT (Maximum Power Point Tracking)</strong>:</p>

<p>MPPT is an algorithm that dynamically adjusts the operating point of the harvesting system to extract maximum power. For solar cells, the maximum power point typically corresponds to 70-80% of the open-circuit voltage (Voc).</p>

<h3 class="section-title">8. Application to the project: What a Leak</h3>

<p>As part of our <a href="./innovative-project.html">innovative project (What a Leak)</a>, we sought to apply the course concepts to design an energy-autonomous water leak detection system.</p>

<p><strong>Objective</strong>: Power a sensor node (leak detector) through energy harvesting, eliminating the need for battery replacement in hard-to-access locations (under sinks, in attics, etc.).</p>

<p><strong>Constraints</strong>:</p>
<ul>
<li>Indoor environment (low light, no wind)</li>
<li>Low temperature gradient</li>
<li>Weak ambient RF waves</li>
<li>Need for periodic data transmission</li>
</ul>

<p><strong>Source evaluation</strong>:</p>

<p>We evaluated each energy source for our specific use case. Unfortunately, the typical indoor environment does not provide enough ambient energy to reliably power our sensor node. Ambient RF power levels are too low, and indoor lighting does not generate enough power with small solar cells.</p>

<p>This analysis, although concluding that a fully autonomous system was impractical in our case, was very instructive. It taught me to rigorously evaluate the energy feasibility of a system before embarking on the design.</p>

<hr>

<h2>PART D - Analysis and Reflection</h2>

<h3 class="section-title">Skills acquired</h3>

<p><strong>Global energy understanding</strong>:<br>
Ability to identify, evaluate, and compare different ambient energy sources for IoT applications, and to choose the most suitable one based on the deployment context.</p>

<p><strong>System sizing</strong>:<br>
Ability to calculate a complete energy budget, from sensor to transmission, taking into account all operating modes and their durations.</p>

<p><strong>RF design</strong>:<br>
Knowledge of wave propagation principles, the Friis formula, and the ability to select and characterize antennas for energy harvesting.</p>

<p><strong>Power management</strong>:<br>
Understanding of power management architectures (LDO, DC-DC, PMIC) and their suitability for different energy harvesting scenarios.</p>

<p><strong>Experimental approach</strong>:<br>
Competence in performing wireless power transfer measurements, interpreting results, and comparing them to theoretical models.</p>

<h3 class="section-title">Self-assessment</h3>

<p>This course brought me a lot of new knowledge on a subject I was unfamiliar with before. I discovered the extent of possibilities for powering connected objects from ambient energy, whether from light, heat, vibrations, or electromagnetic waves.</p>

<p>The lab sessions were particularly enriching. We studied the power requirements of a small red LED, tested approaches for direct energy use and storage. These experiments allowed me to confront theory with reality and understand the practical limits of energy harvesting.</p>

<p>I would have liked to apply these concepts more to a concrete project. Although the innovative project aimed at this goal, the deployment environment did not allow us to harvest enough ambient energy. However, this limitation was instructive: it taught me that energy feasibility assessment is a critical step in any IoT project.</p>

<p>The antenna lab sessions also helped me understand the importance of antenna selection and positioning. This is an aspect often overlooked in IoT projects but one that can make the difference between a functional and a failing system.</p>

<h3 class="section-title">Professional applications</h3>

<p>The skills acquired in this course are directly applicable in many fields:</p>

<p><strong>Industrial IoT</strong>:</p>
<ul>
<li>Autonomous sensors for predictive maintenance</li>
<li>Equipment monitoring in hard-to-access areas</li>
<li>Long-term environmental monitoring</li>
</ul>

<p><strong>Smart Building</strong>:</p>
<ul>
<li>Temperature, humidity, air quality sensors without wiring</li>
<li>Battery-free switches (piezoelectric)</li>
<li>Autonomous people counters</li>
</ul>

<p><strong>Connected health</strong>:</p>
<ul>
<li>Wearables powered by body energy</li>
<li>Medical implants with wireless energy harvesting</li>
<li>Continuous patient monitoring</li>
</ul>

<p><strong>Precision agriculture</strong>:</p>
<ul>
<li>Autonomous soil sensors (solar)</li>
<li>Crop monitoring over large areas</li>
<li>Connected weather stations</li>
</ul>

<h3 class="section-title">My opinion</h3>

<p>This course enabled me to understand aspects of IoT that I had not suspected. For example, the wide variety of possibilities for powering objects with electromagnetic waves and other energy sources available in our environment. Moreover, learning to choose an antenna and understand its operating principles was particularly interesting.</p>

<p>The combination of theory and practice was well balanced. The lectures provided the necessary foundations, and the labs allowed these concepts to be verified experimentally. I particularly appreciated the rigorous methodology for energy budget calculation, which is a skill directly transferable to any IoT project.</p>

<p>This module gave me a more complete vision of IoT system design, integrating the energy dimension from the very beginning of the design process.</p>

<hr>

<h2>Course Documents</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Course - Energy for IoT</h4>
      <p>Complete course: ambient energy sources, energy harvesting, wireless power transfer, power management and energy budget for connected objects.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S9/Energy/5ISS_Energy_for_IoT.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S9/Energy/5ISS_Energy_for_IoT.pdf" target="_blank">Download the course</a></p>
    </div>
  </div>
</div>

<hr>

<h2>Reports and Projects</h2>

<div style="text-align: center;">
    <h3>Lab Report - Energy for Connected Objects</h3>
</div>

<div style="display: flex; justify-content: center;">
    <embed src="/file/reports/S9/Report_Energy_Boukouiss_Chanfreau.pdf" width="100%" height="800px" type="application/pdf">
</div>

<p style="text-align: center;">
    <a href="/file/reports/S9/Report_Energy_Boukouiss_Chanfreau.pdf" target="_blank">Open the full report</a>
</p>

<div style="text-align: center;">
    <h3>Lab Subject</h3>
</div>

<div style="display: flex; justify-content: center;">
    <embed src="/img/BE_Energy_Connected_Object/Lab_Subject_energy.pdf" width="100%" height="800px" type="application/pdf">
</div>

<p style="text-align: center;">
    <a href="/img/BE_Energy_Connected_Object/Lab_Subject_energy.pdf" target="_blank">Open the lab subject</a>
</p>

<hr>

<p><em>Course taken in 2024-2025 at INSA Toulouse, Department of Electrical and Computer Engineering, ISS (Innovative Smart Systems) specialization.</em></p>

</div>

<div class="back-nav">
    <a href="./my-courses-2024-2025.html" data-i18n-html="back-courses-2024-2025">&larr; Retour aux Cours 2024-2025</a>
</div>

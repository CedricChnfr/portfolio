---
layout: default
title: "Chaines Electroniques d'Acquisition de l'Information - Semestre 8"
date: 2024-10-02 10:56:03 +0200
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
</style>

<div class="back-nav">
    <a href="./my-courses-2023-2024.html" data-i18n-html="back-courses-2023-2024">&larr; Retour aux Cours 2023-2024</a>
</div>

<div class="lang-fr">

<h1>Chaines Electroniques d'Acquisition de l'Information - Semestre 8</h1>

<p><strong>Annee academique</strong> : 2023-2024<br/>
<strong>ECTS</strong> : 2.5<br/>
<strong>Categorie</strong> : Electronique Analogique et Instrumentation</p>

<hr/>

<h2>PARTIE A - Presentation Generale du Module</h2>

<h3 class="section-title">Vue d'ensemble</h3>

<p>Ce cours couvre la conception complete des systemes d'acquisition de donnees, depuis le capteur jusqu'au traitement numerique. Il traite du conditionnement de signaux analogiques, de la conversion analogique-numerique, des interfaces de communication, et des architectures de chaines d'acquisition pour applications industrielles, medicales, et scientifiques.</p>

<p><strong>Objectifs pedagogiques</strong> :</p>
<ul>
<li>Concevoir une chaine d'acquisition complete du capteur au microcontroleur</li>
<li>Maitriser le conditionnement de signaux analogiques</li>
<li>Comprendre les convertisseurs analogique-numerique et numerique-analogique</li>
<li>Implementer les interfaces de communication SPI, I2C, UART</li>
<li>Analyser le budget de bruit et optimiser le rapport signal sur bruit</li>
<li>Dimensionner les filtres anti-repliement et de reconstruction</li>
<li>Choisir les composants selon un cahier des charges</li>
</ul>

<h3 class="section-title">Position dans le cursus</h3>

<p>Ce module fait la synthese de plusieurs competences acquises :</p>
<ul>
<li><strong>Circuits Analogiques (S5, S7)</strong> : amplificateurs operationnels, filtres actifs</li>
<li><strong>Signal (S5)</strong> : echantillonnage, theoreme de Shannon, filtrage</li>
<li><strong>Microcontroleurs (S6)</strong> : interfaces, protocoles de communication</li>
<li><strong>Filtrage Numerique (S6)</strong> : traitement post-acquisition</li>
</ul>

<p>Il prepare a :</p>
<ul>
<li><strong>Machine Learning (S8)</strong> : acquisition de donnees pour apprentissage</li>
<li><strong>Temps Reel (S8)</strong> : contraintes temporelles des acquisitions</li>
<li><strong>Projets industriels</strong> : systemes embarques avec capteurs</li>
<li><strong>Instrumentation professionnelle</strong> : conception de systemes de mesure</li>
</ul>

<hr/>

<h2>PARTIE B - Experience Personnelle et Contexte d'Apprentissage</h2>

<h3 class="section-title">Organisation et ressources</h3>

<p>Le module etait structure en cours magistraux et travaux diriges pratiques :</p>

<p><strong>Cours magistraux (15h)</strong> :</p>
<ul>
<li><strong>CM1</strong> : Amplificateurs d'instrumentation, conditionneurs de signaux</li>
<li><strong>CM2</strong> : Interfaces numeriques I2C et SPI, connexion capteurs numeriques, UART</li>
<li><strong>CM3</strong> : Convertisseurs analogique-numerique (CAN) et numerique-analogique (CNA)</li>
<li><strong>CM4</strong> : Compression dynamique, codecs audio</li>
<li><strong>CM5</strong> : Architectures avancees de convertisseurs</li>
</ul>

<p><strong>Travaux diriges (12h)</strong> :</p>
<ul>
<li><strong>TD1</strong> : Multiplexage de capteurs automobiles, CAN</li>
<li><strong>TD2</strong> : Dimensionnement de chaines d'acquisition</li>
<li><strong>TD3</strong> : Lois en A (compression audio)</li>
<li><strong>TD4</strong> : Dalle tactile resistive</li>
<li><strong>TD5</strong> : Architectures de convertisseurs</li>
<li><strong>TD6</strong> : Chaine d'acquisition Bluetooth Low Energy</li>
<li><strong>TD7</strong> : Projet complet</li>
</ul>

<p><strong>Ressources</strong> :</p>
<ul>
<li>10 polycopies de cours (ampli instrumentation, interfaces, CAN/CNA, codecs)</li>
<li>7 TD avec applications pratiques</li>
<li>Annales : 6 sujets d'examens avec corrections (2014-2023)</li>
<li>Logiciel LTspice pour simulation de circuits</li>
</ul>

<h3 class="section-title">Methodologie d'etude</h3>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S8/chaines-acquisition/chaine-acquisition.svg" alt="Chaine d'acquisition de donnees"
       style="max-width: 550px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Architecture complete d'une chaine d'acquisition de donnees</p>
</div>

<p><strong>Phase 1 : Comprendre l'architecture globale</strong> :</p>
<p>Assimiler la chaine complete : capteur &rarr; conditionnement &rarr; conversion &rarr; traitement &rarr; communication.</p>

<p><strong>Phase 2 : Maitriser chaque bloc</strong> :</p>
<p>Etudier en detail chaque etage (amplification, filtrage, conversion) avec ses parametres critiques.</p>

<p><strong>Phase 3 : Dimensionnement pratique</strong> :</p>
<p>S'exercer sur les TD a choisir les composants selon un cahier des charges (resolution, bande passante, SNR).</p>

<p><strong>Phase 4 : Simulation</strong> :</p>
<p>Utiliser LTspice pour valider les circuits de conditionnement et filtres avant realisation.</p>

<p><strong>Phase 5 : Approche systeme</strong> :</p>
<p>Developper une vision d'ensemble en considerant les compromis (cout, performance, consommation).</p>

<h3 class="section-title">Difficultes rencontrees</h3>

<p><strong>Multiplicite des parametres</strong> :</p>
<p>Chaque composant a de nombreuses specifications (offset, derive thermique, CMRR, bruit). Identifier les critiques selon l'application demande de l'experience.</p>

<p><strong>Budget de bruit</strong> :</p>
<p>Calculer le bruit total de la chaine en combinant toutes les sources est complexe mais essentiel pour atteindre le SNR requis.</p>

<p><strong>Choix des composants</strong> :</p>
<p>Face a des centaines de references d'ADC ou d'amplificateurs, selectionner le bon compromis performance/cout/disponibilite n'est pas evident.</p>

<p><strong>Interfaces de communication</strong> :</p>
<p>Maitriser les protocoles SPI, I2C, UART avec leurs timings, leurs limitations, et leur implementation pratique demande de la pratique.</p>

<hr/>

<h2>PARTIE C - Aspects Techniques Detailles</h2>

<h3 class="section-title">1. Architecture generale d'une chaine d'acquisition</h3>

<p><strong>Principe de fonctionnement</strong> :</p>

<p>Une chaine d'acquisition transforme une grandeur physique (temperature, pression, vibration, etc.) en donnees numeriques exploitables par un systeme informatique.</p>

<p><strong>Blocs fonctionnels</strong> :</p>

<p>Grandeur physique &rarr; Capteur &rarr; Conditionnement &rarr; Filtrage anti-repliement &rarr; Conversion A/N &rarr; Interface numerique &rarr; Traitement</p>

<p><strong>Specifications essentielles</strong> :</p>

<table>
<tr><th>Parametre</th><th>Description</th><th>Exemple</th></tr>
<tr><td>Etendue de mesure</td><td>Plage des valeurs a acquerir</td><td>0-100 degC, +/-10V</td></tr>
<tr><td>Resolution</td><td>Plus petit changement detectable</td><td>0.1 degC, 1mV</td></tr>
<tr><td>Precision</td><td>Erreur maximale</td><td>+/-0.5%</td></tr>
<tr><td>Bande passante</td><td>Frequences du signal</td><td>DC-10kHz</td></tr>
<tr><td>Frequence d'echantillonnage</td><td>Nombre d'echantillons par seconde</td><td>44.1 kHz (audio)</td></tr>
<tr><td>Rapport signal/bruit (SNR)</td><td>Qualite du signal</td><td>90 dB</td></tr>
<tr><td>Temps de reponse</td><td>Latence de la mesure</td><td>10 ms</td></tr>
</table>

<h3 class="section-title">2. Capteurs et transducteurs</h3>

<p><strong>Role du capteur</strong> :</p>
<p>Convertir une grandeur physique en signal electrique (tension, courant, resistance, capacite).</p>

<p><strong>Principales familles de capteurs</strong> :</p>

<p><strong>Capteurs resistifs</strong> :</p>
<ul>
<li><strong>Thermistances (CTN/CTP)</strong> : resistance varie avec temperature</li>
<li><strong>Jauges de contrainte</strong> : resistance varie avec deformation mecanique</li>
<li><strong>Potentiometres</strong> : resistance varie avec position</li>
</ul>

<p><strong>Capteurs capacitifs</strong> :</p>
<ul>
<li>Variation de capacite avec distance, pression, humidite</li>
<li>Haute impedance necessitant conditionnement specifique</li>
</ul>

<p><strong>Thermocouples</strong> :</p>
<ul>
<li>Tension proportionnelle a difference de temperature (effet Seebeck)</li>
<li>Necessite compensation de soudure froide</li>
</ul>

<p><strong>Capteurs piezoelectriques</strong> :</p>
<ul>
<li>Generation de charge sous contrainte mecanique</li>
<li>Accelerometres, microphones, capteurs de pression dynamique</li>
<li>Ne mesurent que les variations (signaux AC)</li>
</ul>

<p><strong>Capteurs a effet Hall</strong> :</p>
<ul>
<li>Tension proportionnelle au champ magnetique</li>
<li>Mesure de courant sans contact, position, vitesse de rotation</li>
</ul>

<p><strong>Capteurs optiques</strong> :</p>
<ul>
<li>Photodiodes, phototransistors</li>
<li>Courant proportionnel a l'intensite lumineuse</li>
</ul>

<h3 class="section-title">3. Conditionnement de signaux</h3>

<p><strong>Objectif</strong> :</p>
<p>Adapter le signal du capteur pour optimiser la plage d'entree du convertisseur A/N.</p>

<p><strong>Amplificateur d'instrumentation</strong> :</p>
<p>Composant cle pour signaux differentiels faibles.</p>

<p><strong>Caracteristiques principales</strong> :</p>
<ul>
<li>Tres haute impedance d'entree (&gt; 1 G ohm) : ne charge pas la source</li>
<li>Excellent CMRR (&gt; 100 dB) : rejette le bruit en mode commun</li>
<li>Faible offset et derive thermique</li>
<li>Gain ajustable par une resistance externe</li>
</ul>

<p><strong>Application typique</strong> : amplification de signaux de jauges de contrainte, thermocouples.</p>

<p><strong>Pont de Wheatstone</strong> :</p>
<p>Montage pour mesurer de faibles variations de resistance (jauges de contrainte).</p>

<p><strong>Configurations</strong> :</p>
<ul>
<li><strong>Quart de pont</strong> : 1 jauge active (sensibilite 1x, temperature non compensee)</li>
<li><strong>Demi-pont</strong> : 2 jauges actives (sensibilite 2x, compensation partielle)</li>
<li><strong>Pont complet</strong> : 4 jauges actives (sensibilite 4x, compensation complete)</li>
</ul>

<p><strong>Amplificateur de charge</strong> :</p>
<p>Pour capteurs piezoelectriques qui generent une charge electrique.</p>
<p>Circuit integrateur avec AOP convertissant la charge en tension.</p>

<p><strong>Linearisation</strong> :</p>
<p>Certains capteurs ont une reponse non lineaire (thermistances).</p>
<p>Techniques de linearisation :</p>
<ul>
<li>Reseau de resistances</li>
<li>Linearisation numerique (table de conversion ou polynome)</li>
</ul>

<h3 class="section-title">4. Filtrage anti-repliement</h3>

<p><strong>Probleme du repliement spectral (aliasing)</strong> :</p>
<p>Si la frequence d'echantillonnage Fe est insuffisante par rapport au signal, les composantes haute frequence sont repliees vers les basses frequences, creant une distorsion irreversible.</p>

<p><strong>Theoreme de Shannon-Nyquist</strong> :</p>
<p>Pour eviter le repliement, la frequence d'echantillonnage doit etre au moins le double de la frequence maximale du signal :</p>
<p>Fe &ge; 2 &times; Fmax</p>

<p><strong>Filtre anti-repliement</strong> :</p>
<p>Filtre passe-bas analogique place avant le convertisseur A/N pour eliminer les frequences au-dela de Fe/2.</p>

<p><strong>Parametres de conception</strong> :</p>
<ul>
<li><strong>Frequence de coupure</strong> : juste au-dessus de la bande utile du signal</li>
<li><strong>Ordre</strong> : typiquement 4 a 8 pour pente suffisamment raide</li>
<li><strong>Type</strong> : Butterworth (reponse plate en bande passante), Bessel (phase lineaire pour preserver la forme temporelle)</li>
</ul>

<p><strong>Implementation</strong> :</p>
<ul>
<li>Filtres actifs a AOP : performances elevees, besoin alimentation</li>
<li>Filtres a capacites commutees : integration, accordabilite numerique</li>
</ul>

<h3 class="section-title">5. Conversion analogique-numerique (ADC)</h3>

<p><strong>Parametres fondamentaux</strong> :</p>

<p><strong>Resolution (N bits)</strong> :</p>
<p>Nombre de niveaux de quantification : 2 puissance N</p>
<p>Exemples :</p>
<ul>
<li>8 bits : 256 niveaux</li>
<li>12 bits : 4096 niveaux</li>
<li>16 bits : 65536 niveaux</li>
<li>24 bits : 16.7 millions de niveaux</li>
</ul>

<p><strong>Quantum (LSB)</strong> :</p>
<p>Plus petit pas de quantification.</p>
<p>Si Vref = 5V et N = 12 bits, alors LSB = 5V / 4096 &asymp; 1.22 mV</p>

<p><strong>Frequence d'echantillonnage (Fe)</strong> :</p>
<p>Nombre d'echantillons par seconde (Hz ou SPS - Samples Per Second).</p>

<p><strong>ENOB (Effective Number Of Bits)</strong> :</p>
<p>Resolution effective tenant compte du bruit et de la non-linearite, calculee a partir du SNR mesure.</p>
<p>Souvent inferieure a la resolution nominale (ADC 16 bits &rarr; ENOB 14 bits typique).</p>

<p><strong>INL et DNL</strong> :</p>
<ul>
<li><strong>INL</strong> (Integral Non-Linearity) : ecart maximum de la courbe de transfert par rapport a la droite ideale</li>
<li><strong>DNL</strong> (Differential Non-Linearity) : variation de la largeur des codes de quantification</li>
</ul>

<h3 class="section-title">6. Architectures de convertisseurs A/N</h3>

<p><strong>Convertisseur Flash (parallele)</strong> :</p>
<p>Principe : 2^N - 1 comparateurs en parallele comparent le signal a differentes tensions de reference.</p>

<p><strong>Caracteristiques</strong> :</p>
<ul>
<li>Tres rapide (quelques nanosecondes)</li>
<li>Consommation et surface importantes</li>
<li>Limite a faible resolution (6-8 bits)</li>
<li>Applications : oscilloscopes ultra-rapides, radar</li>
</ul>

<p><strong>Convertisseur a Approximations Successives (SAR)</strong> :</p>
<p>Principe : algorithme de recherche dichotomique (comme une balance a fleau).</p>
<p>En N etapes, teste successivement chaque bit du MSB au LSB.</p>

<p><strong>Caracteristiques</strong> :</p>
<ul>
<li>Bon compromis vitesse/resolution</li>
<li>8 a 18 bits, 100 kSPS a quelques MSPS</li>
<li>Faible consommation</li>
<li>Le plus repandu pour applications generales</li>
<li>Applications : acquisition industrielle, instrumentation, capteurs</li>
</ul>

<p><strong>Convertisseur Pipeline</strong> :</p>
<p>Principe : plusieurs etages en cascade, chaque etage resout quelques bits.</p>

<p><strong>Caracteristiques</strong> :</p>
<ul>
<li>Haute vitesse (&gt; 100 MSPS)</li>
<li>10 a 14 bits typique</li>
<li>Latence de plusieurs cycles (pipeline)</li>
<li>Applications : communications, video, imagerie</li>
</ul>

<p><strong>Convertisseur Sigma-Delta</strong> :</p>
<p>Principe : sur-echantillonnage massif + mise en forme du bruit (noise shaping) + filtrage numerique.</p>

<p><strong>Caracteristiques</strong> :</p>
<ul>
<li>Tres haute resolution (16 a 24 bits)</li>
<li>Vitesse moderee (quelques kHz a quelques MHz)</li>
<li>Excellente linearite</li>
<li>Filtre anti-repliement simplifie (sur-echantillonnage)</li>
<li>Applications : audio, instrumentation de precision, pesage</li>
</ul>

<p><strong>Convertisseur Double Rampe</strong> :</p>
<p>Principe : integration du signal puis decharge a vitesse constante, mesure du temps.</p>

<p><strong>Caracteristiques</strong> :</p>
<ul>
<li>Tres haute resolution</li>
<li>Tres lent (10-100 echantillons/seconde)</li>
<li>Excellent rejet du bruit 50/60 Hz (temps d'integration multiple de 20ms)</li>
<li>Applications : multimetres, balances, instrumentation DC precise</li>
</ul>

<p><strong>Tableau comparatif</strong> :</p>

<table>
<tr><th>Architecture</th><th>Resolution</th><th>Vitesse</th><th>Consommation</th><th>Applications typiques</th></tr>
<tr><td>Flash</td><td>6-8 bits</td><td>&gt; 1 GSPS</td><td>Elevee</td><td>Oscilloscopes, radar</td></tr>
<tr><td>SAR</td><td>8-18 bits</td><td>100 kSPS - 5 MSPS</td><td>Faible</td><td>Acquisition generale</td></tr>
<tr><td>Pipeline</td><td>10-14 bits</td><td>10-500 MSPS</td><td>Moyenne</td><td>Communications, video</td></tr>
<tr><td>Sigma-Delta</td><td>16-24 bits</td><td>10 SPS - 10 MSPS</td><td>Faible</td><td>Audio, instrumentation</td></tr>
<tr><td>Double rampe</td><td>16-24 bits</td><td>10-100 SPS</td><td>Tres faible</td><td>Multimetres, pesage</td></tr>
</table>

<h3 class="section-title">7. Conversion numerique-analogique (DAC)</h3>

<p><strong>Role</strong> :</p>
<p>Reconstituer un signal analogique a partir de donnees numeriques.</p>
<p>Applications : generation de signaux, audio, commande de moteurs, telecommunications.</p>

<p><strong>Architectures principales</strong> :</p>

<p><strong>DAC a reseau R-2R</strong> :</p>
<p>Reseau de resistances de valeurs R et 2R commutees selon les bits.</p>
<p>Avantages : simple, deux valeurs de resistances seulement.</p>

<p><strong>DAC a resistances ponderees</strong> :</p>
<p>Chaque bit controle une resistance de poids different (R, R/2, R/4, etc.).</p>
<p>Probleme : grande dispersion des valeurs pour haute resolution.</p>

<p><strong>DAC Sigma-Delta</strong> :</p>
<p>Sur-echantillonnage + modulation 1-bit + filtrage analogique.</p>
<p>Haute resolution pour audio.</p>

<p><strong>Filtre de reconstruction</strong> :</p>
<p>Le signal en sortie du DAC est en escalier (echantillonne).</p>
<p>Un filtre passe-bas lisse le signal et elimine les images spectrales (repliques du spectre autour de multiples de Fe).</p>

<h3 class="section-title">8. Interfaces de communication numeriques</h3>

<p><strong>SPI (Serial Peripheral Interface)</strong> :</p>

<p><strong>Caracteristiques</strong> :</p>
<ul>
<li>4 fils : CLK (horloge), MOSI (Master Out Slave In), MISO (Master In Slave Out), CS (Chip Select)</li>
<li>Communication full-duplex (emission et reception simultanees)</li>
<li>Vitesse elevee (plusieurs dizaines de MHz)</li>
<li>Architecture maitre-esclaves (un maitre, plusieurs esclaves)</li>
<li>Pas de protocole d'acquittement (pas de detection d'erreur automatique)</li>
</ul>

<p><strong>Applications</strong> : ADC, DAC, memoires Flash, ecrans, capteurs haute vitesse.</p>

<p><strong>I2C (Inter-Integrated Circuit)</strong> :</p>

<p><strong>Caracteristiques</strong> :</p>
<ul>
<li>2 fils : SDA (donnees), SCL (horloge)</li>
<li>Multi-maitres possible (arbitrage)</li>
<li>Adressage sur 7 ou 10 bits (jusqu'a 128 ou 1024 dispositifs)</li>
<li>Vitesses : 100 kHz (standard), 400 kHz (fast), 3.4 MHz (high-speed)</li>
<li>Protocole avec acquittement (ACK/NACK)</li>
</ul>

<p><strong>Applications</strong> : capteurs, memoires EEPROM, RTC, circuits d'extension I/O, nombreux capteurs numeriques.</p>

<p><strong>UART (Universal Asynchronous Receiver-Transmitter)</strong> :</p>

<p><strong>Caracteristiques</strong> :</p>
<ul>
<li>Communication serie asynchrone (pas d'horloge partagee)</li>
<li>2 fils : TX (transmission), RX (reception) + masse</li>
<li>Vitesses standards (bauds) : 9600, 19200, 38400, 115200, etc.</li>
<li>Configuration : bits de donnees (7-8), bit de parite (optionnel), bits de stop (1-2)</li>
<li>Longues distances possibles avec niveaux RS-232 (+/-12V)</li>
</ul>

<p><strong>Applications</strong> : liaison PC, communication entre microcontroleurs, GPS, modules Bluetooth/WiFi, consoles de debogage.</p>

<p><strong>Comparaison</strong> :</p>

<table>
<tr><th>Critere</th><th>SPI</th><th>I2C</th><th>UART</th></tr>
<tr><td>Fils</td><td>4 + 1 par esclave</td><td>2</td><td>2 + masse</td></tr>
<tr><td>Vitesse</td><td>Tres rapide (MHz)</td><td>Moyenne (kHz)</td><td>Lente (kbaud)</td></tr>
<tr><td>Complexite</td><td>Simple</td><td>Moyenne</td><td>Simple</td></tr>
<tr><td>Multi-dispositifs</td><td>Oui (CS multiples)</td><td>Oui (adressage)</td><td>Non (point a point)</td></tr>
<tr><td>Distance</td><td>Courte (PCB)</td><td>Courte (PCB)</td><td>Longue possible</td></tr>
</table>

<h3 class="section-title">9. Analyse du bruit et SNR</h3>

<p><strong>Sources de bruit</strong> :</p>

<p><strong>Bruit du capteur</strong> :</p>
<ul>
<li>Bruit thermique (Johnson-Nyquist) des resistances</li>
<li>Bruit de grenaille (shot noise)</li>
<li>Bruit en 1/f (flicker noise)</li>
</ul>

<p><strong>Bruit du conditionnement</strong> :</p>
<ul>
<li>Bruit en tension et en courant de l'amplificateur</li>
<li>Bruit des resistances du circuit</li>
</ul>

<p><strong>Bruit de quantification</strong> :</p>
<p>Erreur introduite par la quantification sur N bits.</p>
<p>Valeur RMS du bruit : quantum / racine(12)</p>

<p><strong>Bruit de l'ADC</strong> :</p>
<ul>
<li>Bruit thermique interne</li>
<li>Jitter d'echantillonnage (incertitude sur instant d'echantillonnage)</li>
</ul>

<p><strong>Budget de bruit</strong> :</p>
<p>Calcul du bruit total en combinant toutes les sources (somme quadratique car sources independantes).</p>
<p>Le SNR systeme est le rapport entre l'amplitude du signal et le bruit total.</p>
<p><strong>Objectif</strong> : identifier le maillon limitant pour optimiser les efforts.</p>

<h3 class="section-title">10. Techniques d'amelioration du SNR</h3>

<p><strong>Moyennage</strong> :</p>
<p>Calculer la moyenne de N mesures reduit le bruit d'un facteur racine(N).</p>
<p>Exemple : moyenner 100 mesures divise le bruit par 10.</p>
<p>Inconvenient : reduit la bande passante (temps d'acquisition multiplie par N).</p>

<p><strong>Filtrage numerique</strong> :</p>
<p>Apres conversion, filtrer numeriquement pour reduire la bande passante au strict necessaire.</p>
<p>Types : moyennage mobile, filtres FIR, IIR.</p>

<p><strong>Sur-echantillonnage</strong> :</p>
<p>Echantillonner a frequence superieure au minimum requis, puis sous-echantillonner apres filtrage numerique.</p>
<p>Ameliore le SNR pour bruit blanc (gain de 3 dB par doublement de frequence).</p>
<p>Technique exploitee par les ADC Sigma-Delta.</p>

<p><strong>Modulation-demodulation synchrone (Lock-in)</strong> :</p>
<p>Pour signaux tres faibles noyes dans le bruit :</p>
<ul>
<li>Moduler le signal a mesurer a une frequence connue</li>
<li>Apres acquisition, demoduler en multipliant par reference synchrone</li>
<li>Filtrer pour extraire uniquement le signal utile</li>
</ul>
<p>Excellente rejection du bruit hors de la frequence de modulation.</p>
<p>Utilisee en instrumentation scientifique de precision.</p>

<h3 class="section-title">11. Applications specifiques</h3>

<p><strong>Acquisition audio</strong> :</p>

<p><strong>Specifications</strong> :</p>
<ul>
<li>Resolution : 16 bits (CD), 24 bits (studio)</li>
<li>Frequence : 44.1 kHz, 48 kHz, 96 kHz, 192 kHz</li>
<li>SNR eleve : &gt; 90 dB (16 bits), &gt; 110 dB (24 bits)</li>
<li>Faible distorsion harmonique (THD &lt; 0.01%)</li>
</ul>

<p><strong>Composants</strong> : codecs audio integrant ADC + DAC, amplificateurs casque.</p>

<p><strong>Instrumentation medicale (ECG, EEG)</strong> :</p>

<p><strong>Specifications</strong> :</p>
<ul>
<li>Signaux tres faibles (uV pour EEG)</li>
<li>Isolation galvanique obligatoire (protection patient)</li>
<li>Filtres specifiques (rejet 50/60 Hz, passe-haut pour derive baseline)</li>
<li>Conformite normes medicales strictes</li>
</ul>

<p><strong>Composants</strong> : amplificateurs d'instrumentation medicaux, ADC 24 bits, isolateurs.</p>

<p><strong>Acquisition industrielle</strong> :</p>

<p><strong>Specifications</strong> :</p>
<ul>
<li>Robustesse (temperature etendue, vibrations, EMI)</li>
<li>Interfaces industrielles (4-20 mA, 0-10V)</li>
<li>Isolation galvanique pour securite</li>
<li>Auto-diagnostic et detection de defauts</li>
</ul>

<p><strong>Acquisition haute vitesse</strong> :</p>

<p><strong>Applications</strong> : oscilloscopes numeriques, radar, instrumentation RF.</p>

<p><strong>Specifications</strong> :</p>
<ul>
<li>Frequences d'echantillonnage GSPS (milliards d'echantillons/seconde)</li>
<li>Architectures paralleles (interleaving de plusieurs ADC)</li>
<li>Traitement temps reel sur FPGA</li>
<li>Memoires rapides (DDR)</li>
</ul>

<h3 class="section-title">12. Conception de PCB pour signaux mixtes</h3>

<p><strong>Regles essentielles</strong> :</p>

<p><strong>Separation analogique/numerique</strong> :</p>
<ul>
<li>Plans de masse separes, connectes en un seul point (star ground)</li>
<li>Separation physique des sections analogiques et numeriques sur le PCB</li>
</ul>

<p><strong>Routage</strong> :</p>
<ul>
<li>Pistes courtes pour signaux sensibles</li>
<li>Eviter paralleles entre pistes analogiques et numeriques (couplage)</li>
<li>Gardes de masse autour des signaux critiques</li>
</ul>

<p><strong>Alimentation</strong> :</p>
<ul>
<li>Alimentations separees analogiques et numeriques</li>
<li>Regulateurs faible bruit (LDO) pour circuits analogiques</li>
<li>Decouplage systematique (condensateurs au plus pres des composants)</li>
</ul>

<p><strong>Blindage</strong> :</p>
<ul>
<li>Boitier metallique connecte a la masse si environnement bruite</li>
<li>Plans de masse continue pour reduire impedance de retour</li>
</ul>

<hr/>

<h2>PARTIE D - Analyse Reflexive et Perspectives</h2>

<h3 class="section-title">Competences acquises</h3>

<p><strong>Vision systeme complete</strong> :</p>
<p>Capacite a concevoir une chaine d'acquisition de bout en bout en considerant tous les maillons et leurs interactions.</p>

<p><strong>Dimensionnement de circuits</strong> :</p>
<p>Aptitude a choisir les composants (amplificateurs, filtres, ADC) selon un cahier des charges (resolution, bande passante, SNR, cout).</p>

<p><strong>Analyse de performances</strong> :</p>
<p>Competence pour calculer le budget de bruit, evaluer le SNR, identifier les limitations et optimiser les performances.</p>

<p><strong>Maitrise des interfaces</strong> :</p>
<p>Capacite a implementer et deboguer les protocoles SPI, I2C, UART pour connecter capteurs et microcontroleurs.</p>

<p><strong>Approche methodologique</strong> :</p>
<p>Developpement d'une demarche rigoureuse : specifications &rarr; choix architecture &rarr; dimensionnement &rarr; simulation &rarr; validation.</p>

<h3 class="section-title">Points cles a retenir</h3>

<p><strong>1. Approche systeme indispensable</strong> :</p>
<p>Optimiser un seul maillon ne suffit pas. Il faut considerer la chaine complete pour atteindre les performances globales.</p>

<p><strong>2. Le bruit est omnipresent</strong> :</p>
<p>Dans les systemes reels, le bruit limite les performances. Savoir le caracteriser, le minimiser et vivre avec est essentiel.</p>

<p><strong>3. Compromis permanents</strong> :</p>
<p>Resolution vs vitesse, performance vs cout, precision vs consommation. Chaque choix est un equilibre selon l'application.</p>

<p><strong>4. Le filtrage anti-repliement est crucial</strong> :</p>
<p>Un ADC rapide et precis ne sert a rien sans filtre anti-repliement adapte. L'aliasing detruit l'information de facon irreversible.</p>

<p><strong>5. Datasheet = document de travail</strong> :</p>
<p>Les datasheets contiennent toutes les informations necessaires. Apprendre a les lire et les exploiter est une competence cle.</p>

<h3 class="section-title">Retour d'experience</h3>

<p><strong>Aspect formateur</strong> :</p>
<p>Ce cours est tres concret et directement applicable. Contrairement a des cours plus theoriques, chaque notion trouve immediatement une traduction pratique dans un systeme reel.</p>

<p><strong>Complexite du conditionnement</strong> :</p>
<p>Le conditionnement de signal est un art delicat : amplifier suffisamment pour exploiter la dynamique de l'ADC, sans saturer, tout en minimisant le bruit. Trouver le bon equilibre demande de l'experience.</p>

<p><strong>Choix des composants</strong> :</p>
<p>Face a des centaines de references d'ADC, d'amplificateurs d'instrumentation, de capteurs, faire le bon choix est difficile. Les TD ont permis de developper une methodologie de selection.</p>

<p><strong>Importance de la simulation</strong> :</p>
<p>LTspice et autres simulateurs permettent de valider les circuits avant fabrication. C'est un gain de temps considerable et une source d'apprentissage.</p>

<h3 class="section-title">Applications pratiques</h3>

<p><strong>Pour ingenieur en electronique embarquee</strong> :</p>
<ul>
<li>Concevoir des systemes IoT avec multiples capteurs</li>
<li>Dimensionner des cartes d'acquisition de donnees</li>
<li>Interfacer capteurs avec microcontroleurs</li>
<li>Optimiser consommation et performances</li>
</ul>

<p><strong>Pour ingenieur en instrumentation</strong> :</p>
<ul>
<li>Concevoir des appareils de mesure scientifiques</li>
<li>Developper des equipements medicaux</li>
<li>Realiser des systemes de test et validation</li>
<li>Assurer conformite aux normes (precision, securite)</li>
</ul>

<p><strong>Pour ingenieur en automobile</strong> :</p>
<ul>
<li>Acquerir donnees de multiples capteurs (pression, temperature, acceleration, etc.)</li>
<li>Bus de communication (CAN, LIN, FlexRay)</li>
<li>Contraintes severes (temperature, vibrations, EMI)</li>
</ul>

<p><strong>Pour ingenieur en audio</strong> :</p>
<ul>
<li>Concevoir des interfaces audio (microphones, casques)</li>
<li>Developper des equipements d'enregistrement</li>
<li>Optimiser qualite sonore (SNR, THD)</li>
</ul>

<h3 class="section-title">Limites et ouvertures</h3>

<p><strong>Limites du module</strong> :</p>
<ul>
<li>Peu de travaux pratiques en laboratoire (surtout TD theoriques)</li>
<li>Pas de projet complet de conception et fabrication de PCB</li>
<li>Aspects logiciels (drivers, traitement temps reel) peu approfondis</li>
</ul>

<p><strong>Ouvertures vers</strong> :</p>
<ul>
<li><strong>Traitement du signal avance</strong> : filtrage adaptatif, analyse spectrale</li>
<li><strong>Systemes temps reel</strong> : contraintes temporelles, RTOS</li>
<li><strong>Machine Learning embarque</strong> : pretraitement et classification de donnees capteurs</li>
<li><strong>IoT et communication sans fil</strong> : BLE, LoRa, WiFi pour systemes connectes</li>
</ul>

<h3 class="section-title">Evolutions recentes</h3>

<p><strong>Integration accrue</strong> :</p>
<p>Tendance vers System-on-Chip (SoC) integrant capteurs, ADC, traitement, communication.</p>
<p>Exemples : MCU avec ADC 16 bits integres, SoC Bluetooth avec ADC/DAC.</p>
<p>Avantages : compacite, faible cout, consommation reduite.</p>

<p><strong>Capteurs MEMS</strong> :</p>
<p>Microsystemes electromecaniques miniaturises et integres.</p>
<p>Accelerometres, gyroscopes, microphones, capteurs de pression sur silicium.</p>
<p>Revolutionnent l'electronique grand public (smartphones, wearables).</p>

<p><strong>Edge Computing</strong> :</p>
<p>Traitement des donnees au plus pres du capteur (au lieu du cloud).</p>
<p>Permet reduction latence, bande passante, et preservation vie privee.</p>
<p>Necessite ADC efficaces et traitement embarque optimise.</p>

<p><strong>IA embarquee</strong> :</p>
<p>Reseaux de neurones sur microcontroleurs pour classification temps reel (reconnaissance vocale, detection d'anomalies).</p>
<p>Chaines d'acquisition optimisees pour pretraitement avant inference.</p>

<h3 class="section-title">Conseils pour reussir</h3>

<p><strong>1. Comprendre la physique</strong> :</p>
<p>Derriere chaque composant, il y a un phenomene physique. Comprendre la physique aide a anticiper les limitations et optimiser.</p>

<p><strong>2. Lire les datasheets attentivement</strong> :</p>
<p>Les datasheets contiennent tout : caracteristiques electriques, schemas d'application, conditions de fonctionnement. Apprendre a les exploiter methodiquement.</p>

<p><strong>3. Simuler avant de fabriquer</strong> :</p>
<p>LTspice, TINA, autres simulateurs permettent de valider les circuits rapidement. Investir du temps en simulation evite des erreurs couteuses.</p>

<p><strong>4. Faire des calculs de budget de bruit</strong> :</p>
<p>Systematiquement evaluer chaque source de bruit pour identifier le maillon limitant et concentrer les efforts.</p>

<p><strong>5. Tester et mesurer</strong> :</p>
<p>La theorie donne le cadre, mais la pratique revele les subtilites (couplages, derives, interferences). Mesurer pour valider.</p>

<p><strong>6. Developper l'intuition</strong> :</p>
<p>Avec l'experience, developper un sens des ordres de grandeur (bruit typique d'un AOP, resolution necessaire selon application, etc.).</p>

<h3 class="section-title">Conclusion</h3>

<p>Ce module est fondamental pour tout ingenieur travaillant sur des systemes embarques, de l'instrumentation, ou de l'IoT. L'acquisition de donnees est omnipresente : smartphones, automobiles, industrie, medical, domotique, etc.</p>

<p><strong>Competences transferables</strong> :</p>
<ul>
<li>Vision systeme et approche methodique</li>
<li>Capacite a dimensionner et optimiser des systemes complexes</li>
<li>Maitrise des interfaces de communication (indispensable pour tout systeme embarque)</li>
<li>Comprehension profonde du compromis analogique/numerique</li>
</ul>

<p><strong>Pertinence professionnelle</strong> :</p>
<p>L'explosion de l'IoT et des systemes connectes accroit la demande d'ingenieurs maitrisant les chaines d'acquisition. Ces competences sont recherchees dans tous les secteurs.</p>

<p><strong>Message principal</strong> :</p>
<p>Une chaine d'acquisition n'est performante que si tous les maillons sont coherents. Le meilleur ADC du monde ne compensera pas un conditionnement mal concu ou un capteur inadapte. L'approche systeme est la cle.</p>

<p><strong>Recommandations</strong> :</p>
<ul>
<li>Approfondir par des projets personnels (Arduino, Raspberry Pi avec capteurs)</li>
<li>Etudier des designs de reference (circuits d'application dans datasheets)</li>
<li>Pratiquer la simulation (LTspice gratuit et puissant)</li>
<li>Suivre des tutoriels sur interfaces (SPI, I2C) avec oscilloscope logique</li>
<li>Realiser un projet complet : capteur &rarr; conditionnement &rarr; ADC &rarr; microcontroleur &rarr; affichage/transmission</li>
</ul>

<p><strong>Liens avec les autres cours</strong> :</p>
<ul>
<li><a href="./filtrage-actif-bruit.html">Filtrage Actif et Bruit - S7</a> : filtres analogiques, sources de bruit</li>
<li><a href="./microcontroleur.html">Microcontroleurs - S6</a> : interfaces SPI/I2C/UART</li>
<li><a href="./filtrage-numerique.html">Filtrage Numerique - S6</a> : traitement post-acquisition</li>
<li><a href="./signal.html">Signal - S5</a> : echantillonnage, theoreme de Shannon</li>
<li><a href="./machine-learning-s8.html">Machine Learning - S8</a> : pretraitement de donnees capteurs</li>
</ul>

<hr/>

<p><em>Cours suivi en 2023-2024 a l'INSA Toulouse, Departement Genie Electrique et Informatique.</em></p>

<div class="back-nav">
    <a href="./my-courses-2023-2024.html" data-i18n-html="back-courses-2023-2024">&larr; Retour aux Cours 2023-2024</a>
</div>

<hr/>

<h2><span class="lang-fr">Documents de Cours</span><span class="lang-en">Course Documents</span></h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4><span class="lang-fr">Conditionneur de Signaux</span><span class="lang-en">Signal Conditioning</span></h4>
      <p><span class="lang-fr">Cours sur le conditionnement de signaux : amplification, filtrage, adaptation d'impedance et preparation pour conversion.</span><span class="lang-en">Course on signal conditioning: amplification, filtering, impedance matching and preparation for conversion.</span></p>
      <div class="pdf-lazy" data-src="/cours-pdf/S8/Chaines-Acquisition/conditionneur.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S8/Chaines-Acquisition/conditionneur.pdf" target="_blank"><span class="lang-fr">Telecharger</span><span class="lang-en">Download</span></a></p>
    </div>
    <div class="pdf-item">
      <h4><span class="lang-fr">Convertisseurs Analogique-Numerique</span><span class="lang-en">Analog-to-Digital Converters</span></h4>
      <p><span class="lang-fr">Cours sur les CAN : architectures (flash, SAR, sigma-delta), performances (resolution, vitesse, SNR) et choix.</span><span class="lang-en">Course on ADCs: architectures (flash, SAR, sigma-delta), performance (resolution, speed, SNR) and selection.</span></p>
      <div class="pdf-lazy" data-src="/cours-pdf/S8/Chaines-Acquisition/convertisseurs-can.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S8/Chaines-Acquisition/convertisseurs-can.pdf" target="_blank"><span class="lang-fr">Telecharger</span><span class="lang-en">Download</span></a></p>
    </div>
    <div class="pdf-item">
      <h4><span class="lang-fr">Capteurs Numeriques</span><span class="lang-en">Digital Sensors</span></h4>
      <p><span class="lang-fr">Mise en oeuvre de capteurs numeriques : protocoles I2C/SPI, configuration, calibration et exploitation des donnees.</span><span class="lang-en">Implementation of digital sensors: I2C/SPI protocols, configuration, calibration and data exploitation.</span></p>
      <div class="pdf-lazy" data-src="/cours-pdf/S8/Chaines-Acquisition/capteurs-numeriques.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S8/Chaines-Acquisition/capteurs-numeriques.pdf" target="_blank"><span class="lang-fr">Telecharger</span><span class="lang-en">Download</span></a></p>
    </div>
  </div>
</div>

</div>

<div class="lang-en">

<h1>Electronic Data Acquisition Chains - Semester 8</h1>

<p><strong>Academic Year</strong>: 2023-2024<br/>
<strong>ECTS</strong>: 2.5<br/>
<strong>Category</strong>: Analog Electronics and Instrumentation</p>

<hr/>

<h2>PART A - General Module Overview</h2>

<h3 class="section-title">Overview</h3>

<p>This course covers the complete design of data acquisition systems, from the sensor to digital processing. It addresses analog signal conditioning, analog-to-digital conversion, communication interfaces, and acquisition chain architectures for industrial, medical, and scientific applications.</p>

<p><strong>Learning Objectives</strong>:</p>
<ul>
<li>Design a complete acquisition chain from sensor to microcontroller</li>
<li>Master analog signal conditioning</li>
<li>Understand analog-to-digital and digital-to-analog converters</li>
<li>Implement SPI, I2C, UART communication interfaces</li>
<li>Analyze the noise budget and optimize the signal-to-noise ratio</li>
<li>Size anti-aliasing and reconstruction filters</li>
<li>Select components according to specifications</li>
</ul>

<h3 class="section-title">Position in the Curriculum</h3>

<p>This module synthesizes several previously acquired skills:</p>
<ul>
<li><strong>Analog Circuits (S5, S7)</strong>: operational amplifiers, active filters</li>
<li><strong>Signal Processing (S5)</strong>: sampling, Shannon's theorem, filtering</li>
<li><strong>Microcontrollers (S6)</strong>: interfaces, communication protocols</li>
<li><strong>Digital Filtering (S6)</strong>: post-acquisition processing</li>
</ul>

<p>It prepares for:</p>
<ul>
<li><strong>Machine Learning (S8)</strong>: data acquisition for training</li>
<li><strong>Real-Time Systems (S8)</strong>: temporal constraints of acquisitions</li>
<li><strong>Industrial projects</strong>: embedded systems with sensors</li>
<li><strong>Professional instrumentation</strong>: measurement system design</li>
</ul>

<hr/>

<h2>PART B - Personal Experience and Learning Context</h2>

<h3 class="section-title">Organization and Resources</h3>

<p>The module was structured into lectures and practical tutorial sessions:</p>

<p><strong>Lectures (15h)</strong>:</p>
<ul>
<li><strong>L1</strong>: Instrumentation amplifiers, signal conditioners</li>
<li><strong>L2</strong>: I2C and SPI digital interfaces, digital sensor connection, UART</li>
<li><strong>L3</strong>: Analog-to-digital converters (ADC) and digital-to-analog converters (DAC)</li>
<li><strong>L4</strong>: Dynamic compression, audio codecs</li>
<li><strong>L5</strong>: Advanced converter architectures</li>
</ul>

<p><strong>Tutorials (12h)</strong>:</p>
<ul>
<li><strong>T1</strong>: Automotive sensor multiplexing, ADC</li>
<li><strong>T2</strong>: Acquisition chain sizing</li>
<li><strong>T3</strong>: A-law (audio compression)</li>
<li><strong>T4</strong>: Resistive touchscreen</li>
<li><strong>T5</strong>: Converter architectures</li>
<li><strong>T6</strong>: Bluetooth Low Energy acquisition chain</li>
<li><strong>T7</strong>: Complete project</li>
</ul>

<p><strong>Resources</strong>:</p>
<ul>
<li>10 course handouts (instrumentation amplifiers, interfaces, ADC/DAC, codecs)</li>
<li>7 tutorials with practical applications</li>
<li>Past exams: 6 exam papers with corrections (2014-2023)</li>
<li>LTspice software for circuit simulation</li>
</ul>

<h3 class="section-title">Study Methodology</h3>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S8/chaines-acquisition/chaine-acquisition.svg" alt="Data acquisition chain"
       style="max-width: 550px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Complete architecture of a data acquisition chain</p>
</div>

<p><strong>Phase 1: Understanding the overall architecture</strong>:</p>
<p>Assimilate the complete chain: sensor &rarr; conditioning &rarr; conversion &rarr; processing &rarr; communication.</p>

<p><strong>Phase 2: Mastering each block</strong>:</p>
<p>Study each stage in detail (amplification, filtering, conversion) with its critical parameters.</p>

<p><strong>Phase 3: Practical sizing</strong>:</p>
<p>Practice through tutorials selecting components according to specifications (resolution, bandwidth, SNR).</p>

<p><strong>Phase 4: Simulation</strong>:</p>
<p>Use LTspice to validate conditioning circuits and filters before implementation.</p>

<p><strong>Phase 5: System-level approach</strong>:</p>
<p>Develop an overall vision considering trade-offs (cost, performance, power consumption).</p>

<h3 class="section-title">Difficulties Encountered</h3>

<p><strong>Multiplicity of parameters</strong>:</p>
<p>Each component has numerous specifications (offset, thermal drift, CMRR, noise). Identifying the critical ones for a given application requires experience.</p>

<p><strong>Noise budget</strong>:</p>
<p>Calculating the total chain noise by combining all sources is complex but essential to achieve the required SNR.</p>

<p><strong>Component selection</strong>:</p>
<p>Faced with hundreds of ADC or amplifier references, selecting the right performance/cost/availability trade-off is not straightforward.</p>

<p><strong>Communication interfaces</strong>:</p>
<p>Mastering SPI, I2C, UART protocols with their timings, limitations, and practical implementation requires practice.</p>

<hr/>

<h2>PART C - Detailed Technical Aspects</h2>

<h3 class="section-title">1. General Architecture of an Acquisition Chain</h3>

<p><strong>Operating principle</strong>:</p>

<p>An acquisition chain transforms a physical quantity (temperature, pressure, vibration, etc.) into digital data usable by a computer system.</p>

<p><strong>Functional blocks</strong>:</p>

<p>Physical quantity &rarr; Sensor &rarr; Conditioning &rarr; Anti-aliasing filter &rarr; A/D Conversion &rarr; Digital interface &rarr; Processing</p>

<p><strong>Essential specifications</strong>:</p>

<table>
<tr><th>Parameter</th><th>Description</th><th>Example</th></tr>
<tr><td>Measurement range</td><td>Range of values to acquire</td><td>0-100 degC, +/-10V</td></tr>
<tr><td>Resolution</td><td>Smallest detectable change</td><td>0.1 degC, 1mV</td></tr>
<tr><td>Accuracy</td><td>Maximum error</td><td>+/-0.5%</td></tr>
<tr><td>Bandwidth</td><td>Signal frequencies</td><td>DC-10kHz</td></tr>
<tr><td>Sampling frequency</td><td>Number of samples per second</td><td>44.1 kHz (audio)</td></tr>
<tr><td>Signal-to-noise ratio (SNR)</td><td>Signal quality</td><td>90 dB</td></tr>
<tr><td>Response time</td><td>Measurement latency</td><td>10 ms</td></tr>
</table>

<h3 class="section-title">2. Sensors and Transducers</h3>

<p><strong>Role of the sensor</strong>:</p>
<p>Convert a physical quantity into an electrical signal (voltage, current, resistance, capacitance).</p>

<p><strong>Main sensor families</strong>:</p>

<p><strong>Resistive sensors</strong>:</p>
<ul>
<li><strong>Thermistors (NTC/PTC)</strong>: resistance varies with temperature</li>
<li><strong>Strain gauges</strong>: resistance varies with mechanical deformation</li>
<li><strong>Potentiometers</strong>: resistance varies with position</li>
</ul>

<p><strong>Capacitive sensors</strong>:</p>
<ul>
<li>Capacitance variation with distance, pressure, humidity</li>
<li>High impedance requiring specific conditioning</li>
</ul>

<p><strong>Thermocouples</strong>:</p>
<ul>
<li>Voltage proportional to temperature difference (Seebeck effect)</li>
<li>Requires cold junction compensation</li>
</ul>

<p><strong>Piezoelectric sensors</strong>:</p>
<ul>
<li>Charge generation under mechanical stress</li>
<li>Accelerometers, microphones, dynamic pressure sensors</li>
<li>Only measure variations (AC signals)</li>
</ul>

<p><strong>Hall effect sensors</strong>:</p>
<ul>
<li>Voltage proportional to magnetic field</li>
<li>Non-contact current measurement, position, rotational speed</li>
</ul>

<p><strong>Optical sensors</strong>:</p>
<ul>
<li>Photodiodes, phototransistors</li>
<li>Current proportional to light intensity</li>
</ul>

<h3 class="section-title">3. Signal Conditioning</h3>

<p><strong>Objective</strong>:</p>
<p>Adapt the sensor signal to optimize the input range of the A/D converter.</p>

<p><strong>Instrumentation amplifier</strong>:</p>
<p>Key component for weak differential signals.</p>

<p><strong>Main characteristics</strong>:</p>
<ul>
<li>Very high input impedance (&gt; 1 G ohm): does not load the source</li>
<li>Excellent CMRR (&gt; 100 dB): rejects common-mode noise</li>
<li>Low offset and thermal drift</li>
<li>Gain adjustable via an external resistor</li>
</ul>

<p><strong>Typical application</strong>: amplification of strain gauge and thermocouple signals.</p>

<p><strong>Wheatstone bridge</strong>:</p>
<p>Circuit for measuring small resistance variations (strain gauges).</p>

<p><strong>Configurations</strong>:</p>
<ul>
<li><strong>Quarter bridge</strong>: 1 active gauge (1x sensitivity, temperature uncompensated)</li>
<li><strong>Half bridge</strong>: 2 active gauges (2x sensitivity, partial compensation)</li>
<li><strong>Full bridge</strong>: 4 active gauges (4x sensitivity, full compensation)</li>
</ul>

<p><strong>Charge amplifier</strong>:</p>
<p>For piezoelectric sensors that generate an electrical charge.</p>
<p>Integrator circuit with op-amp converting charge to voltage.</p>

<p><strong>Linearization</strong>:</p>
<p>Some sensors have a non-linear response (thermistors).</p>
<p>Linearization techniques:</p>
<ul>
<li>Resistor network</li>
<li>Digital linearization (lookup table or polynomial)</li>
</ul>

<h3 class="section-title">4. Anti-aliasing Filtering</h3>

<p><strong>Spectral aliasing problem</strong>:</p>
<p>If the sampling frequency Fe is insufficient relative to the signal, high-frequency components are folded back into lower frequencies, creating irreversible distortion.</p>

<p><strong>Shannon-Nyquist theorem</strong>:</p>
<p>To avoid aliasing, the sampling frequency must be at least twice the maximum signal frequency:</p>
<p>Fe &ge; 2 &times; Fmax</p>

<p><strong>Anti-aliasing filter</strong>:</p>
<p>Analog low-pass filter placed before the A/D converter to eliminate frequencies beyond Fe/2.</p>

<p><strong>Design parameters</strong>:</p>
<ul>
<li><strong>Cutoff frequency</strong>: just above the useful signal band</li>
<li><strong>Order</strong>: typically 4 to 8 for a sufficiently steep roll-off</li>
<li><strong>Type</strong>: Butterworth (flat passband response), Bessel (linear phase to preserve temporal shape)</li>
</ul>

<p><strong>Implementation</strong>:</p>
<ul>
<li>Active op-amp filters: high performance, requires power supply</li>
<li>Switched-capacitor filters: integration, digital tunability</li>
</ul>

<h3 class="section-title">5. Analog-to-Digital Conversion (ADC)</h3>

<p><strong>Fundamental parameters</strong>:</p>

<p><strong>Resolution (N bits)</strong>:</p>
<p>Number of quantization levels: 2 to the power of N</p>
<p>Examples:</p>
<ul>
<li>8 bits: 256 levels</li>
<li>12 bits: 4096 levels</li>
<li>16 bits: 65536 levels</li>
<li>24 bits: 16.7 million levels</li>
</ul>

<p><strong>Quantum (LSB)</strong>:</p>
<p>Smallest quantization step.</p>
<p>If Vref = 5V and N = 12 bits, then LSB = 5V / 4096 &asymp; 1.22 mV</p>

<p><strong>Sampling frequency (Fe)</strong>:</p>
<p>Number of samples per second (Hz or SPS - Samples Per Second).</p>

<p><strong>ENOB (Effective Number Of Bits)</strong>:</p>
<p>Effective resolution accounting for noise and non-linearity, calculated from measured SNR.</p>
<p>Often lower than nominal resolution (16-bit ADC &rarr; 14-bit ENOB typical).</p>

<p><strong>INL and DNL</strong>:</p>
<ul>
<li><strong>INL</strong> (Integral Non-Linearity): maximum deviation of the transfer curve from the ideal straight line</li>
<li><strong>DNL</strong> (Differential Non-Linearity): variation in the width of quantization codes</li>
</ul>

<h3 class="section-title">6. A/D Converter Architectures</h3>

<p><strong>Flash converter (parallel)</strong>:</p>
<p>Principle: 2^N - 1 comparators in parallel compare the signal to different reference voltages.</p>

<p><strong>Characteristics</strong>:</p>
<ul>
<li>Very fast (a few nanoseconds)</li>
<li>Significant power consumption and die area</li>
<li>Limited to low resolution (6-8 bits)</li>
<li>Applications: ultra-fast oscilloscopes, radar</li>
</ul>

<p><strong>Successive Approximation Register (SAR) converter</strong>:</p>
<p>Principle: binary search algorithm (like a balance scale).</p>
<p>In N steps, successively tests each bit from MSB to LSB.</p>

<p><strong>Characteristics</strong>:</p>
<ul>
<li>Good speed/resolution trade-off</li>
<li>8 to 18 bits, 100 kSPS to several MSPS</li>
<li>Low power consumption</li>
<li>Most widely used for general-purpose applications</li>
<li>Applications: industrial acquisition, instrumentation, sensors</li>
</ul>

<p><strong>Pipeline converter</strong>:</p>
<p>Principle: several cascaded stages, each stage resolves a few bits.</p>

<p><strong>Characteristics</strong>:</p>
<ul>
<li>High speed (&gt; 100 MSPS)</li>
<li>Typically 10 to 14 bits</li>
<li>Multi-cycle latency (pipeline)</li>
<li>Applications: communications, video, imaging</li>
</ul>

<p><strong>Sigma-Delta converter</strong>:</p>
<p>Principle: massive oversampling + noise shaping + digital filtering.</p>

<p><strong>Characteristics</strong>:</p>
<ul>
<li>Very high resolution (16 to 24 bits)</li>
<li>Moderate speed (a few kHz to several MHz)</li>
<li>Excellent linearity</li>
<li>Simplified anti-aliasing filter (oversampling)</li>
<li>Applications: audio, precision instrumentation, weighing</li>
</ul>

<p><strong>Dual-slope converter</strong>:</p>
<p>Principle: signal integration then constant-rate discharge, time measurement.</p>

<p><strong>Characteristics</strong>:</p>
<ul>
<li>Very high resolution</li>
<li>Very slow (10-100 samples/second)</li>
<li>Excellent 50/60 Hz noise rejection (integration time multiple of 20ms)</li>
<li>Applications: multimeters, scales, precision DC instrumentation</li>
</ul>

<p><strong>Comparison table</strong>:</p>

<table>
<tr><th>Architecture</th><th>Resolution</th><th>Speed</th><th>Power consumption</th><th>Typical applications</th></tr>
<tr><td>Flash</td><td>6-8 bits</td><td>&gt; 1 GSPS</td><td>High</td><td>Oscilloscopes, radar</td></tr>
<tr><td>SAR</td><td>8-18 bits</td><td>100 kSPS - 5 MSPS</td><td>Low</td><td>General-purpose acquisition</td></tr>
<tr><td>Pipeline</td><td>10-14 bits</td><td>10-500 MSPS</td><td>Medium</td><td>Communications, video</td></tr>
<tr><td>Sigma-Delta</td><td>16-24 bits</td><td>10 SPS - 10 MSPS</td><td>Low</td><td>Audio, instrumentation</td></tr>
<tr><td>Dual-slope</td><td>16-24 bits</td><td>10-100 SPS</td><td>Very low</td><td>Multimeters, weighing</td></tr>
</table>

<h3 class="section-title">7. Digital-to-Analog Conversion (DAC)</h3>

<p><strong>Role</strong>:</p>
<p>Reconstruct an analog signal from digital data.</p>
<p>Applications: signal generation, audio, motor control, telecommunications.</p>

<p><strong>Main architectures</strong>:</p>

<p><strong>R-2R ladder DAC</strong>:</p>
<p>Resistor network with R and 2R values switched according to bits.</p>
<p>Advantages: simple, only two resistor values needed.</p>

<p><strong>Weighted resistor DAC</strong>:</p>
<p>Each bit controls a resistor of different weight (R, R/2, R/4, etc.).</p>
<p>Problem: large value spread for high resolution.</p>

<p><strong>Sigma-Delta DAC</strong>:</p>
<p>Oversampling + 1-bit modulation + analog filtering.</p>
<p>High resolution for audio.</p>

<p><strong>Reconstruction filter</strong>:</p>
<p>The DAC output signal is staircase-shaped (sampled).</p>
<p>A low-pass filter smooths the signal and eliminates spectral images (spectrum replicas around multiples of Fe).</p>

<h3 class="section-title">8. Digital Communication Interfaces</h3>

<p><strong>SPI (Serial Peripheral Interface)</strong>:</p>

<p><strong>Characteristics</strong>:</p>
<ul>
<li>4 wires: CLK (clock), MOSI (Master Out Slave In), MISO (Master In Slave Out), CS (Chip Select)</li>
<li>Full-duplex communication (simultaneous transmit and receive)</li>
<li>High speed (tens of MHz)</li>
<li>Master-slave architecture (one master, multiple slaves)</li>
<li>No acknowledgment protocol (no automatic error detection)</li>
</ul>

<p><strong>Applications</strong>: ADC, DAC, Flash memory, displays, high-speed sensors.</p>

<p><strong>I2C (Inter-Integrated Circuit)</strong>:</p>

<p><strong>Characteristics</strong>:</p>
<ul>
<li>2 wires: SDA (data), SCL (clock)</li>
<li>Multi-master capable (arbitration)</li>
<li>7-bit or 10-bit addressing (up to 128 or 1024 devices)</li>
<li>Speeds: 100 kHz (standard), 400 kHz (fast), 3.4 MHz (high-speed)</li>
<li>Protocol with acknowledgment (ACK/NACK)</li>
</ul>

<p><strong>Applications</strong>: sensors, EEPROM memories, RTC, I/O expansion circuits, numerous digital sensors.</p>

<p><strong>UART (Universal Asynchronous Receiver-Transmitter)</strong>:</p>

<p><strong>Characteristics</strong>:</p>
<ul>
<li>Asynchronous serial communication (no shared clock)</li>
<li>2 wires: TX (transmit), RX (receive) + ground</li>
<li>Standard baud rates: 9600, 19200, 38400, 115200, etc.</li>
<li>Configuration: data bits (7-8), parity bit (optional), stop bits (1-2)</li>
<li>Long distances possible with RS-232 levels (+/-12V)</li>
</ul>

<p><strong>Applications</strong>: PC connection, inter-microcontroller communication, GPS, Bluetooth/WiFi modules, debug consoles.</p>

<p><strong>Comparison</strong>:</p>

<table>
<tr><th>Criterion</th><th>SPI</th><th>I2C</th><th>UART</th></tr>
<tr><td>Wires</td><td>4 + 1 per slave</td><td>2</td><td>2 + ground</td></tr>
<tr><td>Speed</td><td>Very fast (MHz)</td><td>Medium (kHz)</td><td>Slow (kbaud)</td></tr>
<tr><td>Complexity</td><td>Simple</td><td>Medium</td><td>Simple</td></tr>
<tr><td>Multi-device</td><td>Yes (multiple CS)</td><td>Yes (addressing)</td><td>No (point-to-point)</td></tr>
<tr><td>Distance</td><td>Short (PCB)</td><td>Short (PCB)</td><td>Long possible</td></tr>
</table>

<h3 class="section-title">9. Noise Analysis and SNR</h3>

<p><strong>Noise sources</strong>:</p>

<p><strong>Sensor noise</strong>:</p>
<ul>
<li>Thermal noise (Johnson-Nyquist) from resistors</li>
<li>Shot noise</li>
<li>1/f noise (flicker noise)</li>
</ul>

<p><strong>Conditioning noise</strong>:</p>
<ul>
<li>Amplifier voltage and current noise</li>
<li>Circuit resistor noise</li>
</ul>

<p><strong>Quantization noise</strong>:</p>
<p>Error introduced by quantization on N bits.</p>
<p>RMS noise value: quantum / sqrt(12)</p>

<p><strong>ADC noise</strong>:</p>
<ul>
<li>Internal thermal noise</li>
<li>Sampling jitter (uncertainty on sampling instant)</li>
</ul>

<p><strong>Noise budget</strong>:</p>
<p>Total noise calculation by combining all sources (root-sum-square since sources are independent).</p>
<p>The system SNR is the ratio between signal amplitude and total noise.</p>
<p><strong>Objective</strong>: identify the limiting link to optimize efforts.</p>

<h3 class="section-title">10. SNR Improvement Techniques</h3>

<p><strong>Averaging</strong>:</p>
<p>Computing the average of N measurements reduces noise by a factor of sqrt(N).</p>
<p>Example: averaging 100 measurements divides noise by 10.</p>
<p>Disadvantage: reduces bandwidth (acquisition time multiplied by N).</p>

<p><strong>Digital filtering</strong>:</p>
<p>After conversion, digitally filter to reduce bandwidth to the strict minimum.</p>
<p>Types: moving average, FIR filters, IIR filters.</p>

<p><strong>Oversampling</strong>:</p>
<p>Sampling at a frequency higher than the minimum required, then downsampling after digital filtering.</p>
<p>Improves SNR for white noise (3 dB gain per frequency doubling).</p>
<p>Technique exploited by Sigma-Delta ADCs.</p>

<p><strong>Synchronous modulation-demodulation (Lock-in)</strong>:</p>
<p>For very weak signals buried in noise:</p>
<ul>
<li>Modulate the signal to be measured at a known frequency</li>
<li>After acquisition, demodulate by multiplying with a synchronous reference</li>
<li>Filter to extract only the useful signal</li>
</ul>
<p>Excellent noise rejection outside the modulation frequency.</p>
<p>Used in precision scientific instrumentation.</p>

<h3 class="section-title">11. Specific Applications</h3>

<p><strong>Audio acquisition</strong>:</p>

<p><strong>Specifications</strong>:</p>
<ul>
<li>Resolution: 16 bits (CD), 24 bits (studio)</li>
<li>Frequency: 44.1 kHz, 48 kHz, 96 kHz, 192 kHz</li>
<li>High SNR: &gt; 90 dB (16 bits), &gt; 110 dB (24 bits)</li>
<li>Low total harmonic distortion (THD &lt; 0.01%)</li>
</ul>

<p><strong>Components</strong>: audio codecs integrating ADC + DAC, headphone amplifiers.</p>

<p><strong>Medical instrumentation (ECG, EEG)</strong>:</p>

<p><strong>Specifications</strong>:</p>
<ul>
<li>Very weak signals (uV for EEG)</li>
<li>Mandatory galvanic isolation (patient protection)</li>
<li>Specific filters (50/60 Hz rejection, high-pass for baseline drift)</li>
<li>Strict medical standards compliance</li>
</ul>

<p><strong>Components</strong>: medical instrumentation amplifiers, 24-bit ADC, isolators.</p>

<p><strong>Industrial acquisition</strong>:</p>

<p><strong>Specifications</strong>:</p>
<ul>
<li>Robustness (extended temperature, vibrations, EMI)</li>
<li>Industrial interfaces (4-20 mA, 0-10V)</li>
<li>Galvanic isolation for safety</li>
<li>Self-diagnostics and fault detection</li>
</ul>

<p><strong>High-speed acquisition</strong>:</p>

<p><strong>Applications</strong>: digital oscilloscopes, radar, RF instrumentation.</p>

<p><strong>Specifications</strong>:</p>
<ul>
<li>GSPS sampling frequencies (billions of samples/second)</li>
<li>Parallel architectures (interleaving of multiple ADCs)</li>
<li>Real-time processing on FPGA</li>
<li>Fast memories (DDR)</li>
</ul>

<h3 class="section-title">12. Mixed-Signal PCB Design</h3>

<p><strong>Essential rules</strong>:</p>

<p><strong>Analog/digital separation</strong>:</p>
<ul>
<li>Separate ground planes, connected at a single point (star ground)</li>
<li>Physical separation of analog and digital sections on the PCB</li>
</ul>

<p><strong>Routing</strong>:</p>
<ul>
<li>Short traces for sensitive signals</li>
<li>Avoid parallel routing between analog and digital traces (coupling)</li>
<li>Ground guards around critical signals</li>
</ul>

<p><strong>Power supply</strong>:</p>
<ul>
<li>Separate analog and digital power supplies</li>
<li>Low-noise regulators (LDO) for analog circuits</li>
<li>Systematic decoupling (capacitors as close as possible to components)</li>
</ul>

<p><strong>Shielding</strong>:</p>
<ul>
<li>Metal enclosure connected to ground in noisy environments</li>
<li>Continuous ground planes to reduce return impedance</li>
</ul>

<hr/>

<h2>PART D - Reflective Analysis and Perspectives</h2>

<h3 class="section-title">Skills Acquired</h3>

<p><strong>Complete system vision</strong>:</p>
<p>Ability to design an acquisition chain end-to-end, considering all links and their interactions.</p>

<p><strong>Circuit sizing</strong>:</p>
<p>Ability to select components (amplifiers, filters, ADC) according to specifications (resolution, bandwidth, SNR, cost).</p>

<p><strong>Performance analysis</strong>:</p>
<p>Competence in calculating the noise budget, evaluating SNR, identifying limitations and optimizing performance.</p>

<p><strong>Interface mastery</strong>:</p>
<p>Ability to implement and debug SPI, I2C, UART protocols for connecting sensors and microcontrollers.</p>

<p><strong>Methodological approach</strong>:</p>
<p>Development of a rigorous process: specifications &rarr; architecture selection &rarr; sizing &rarr; simulation &rarr; validation.</p>

<h3 class="section-title">Key Takeaways</h3>

<p><strong>1. System-level approach is essential</strong>:</p>
<p>Optimizing a single link is not enough. The complete chain must be considered to achieve overall performance.</p>

<p><strong>2. Noise is ubiquitous</strong>:</p>
<p>In real systems, noise limits performance. Knowing how to characterize it, minimize it, and live with it is essential.</p>

<p><strong>3. Constant trade-offs</strong>:</p>
<p>Resolution vs. speed, performance vs. cost, accuracy vs. power consumption. Every choice is a balance according to the application.</p>

<p><strong>4. Anti-aliasing filtering is crucial</strong>:</p>
<p>A fast and accurate ADC is useless without a proper anti-aliasing filter. Aliasing destroys information irreversibly.</p>

<p><strong>5. Datasheet = working document</strong>:</p>
<p>Datasheets contain all necessary information. Learning to read and exploit them is a key skill.</p>

<h3 class="section-title">Feedback</h3>

<p><strong>Educational aspect</strong>:</p>
<p>This course is very practical and directly applicable. Unlike more theoretical courses, each concept immediately finds a practical application in a real system.</p>

<p><strong>Conditioning complexity</strong>:</p>
<p>Signal conditioning is a delicate art: amplifying sufficiently to exploit the ADC's dynamic range, without saturating, while minimizing noise. Finding the right balance requires experience.</p>

<p><strong>Component selection</strong>:</p>
<p>Faced with hundreds of ADC, instrumentation amplifier, and sensor references, making the right choice is difficult. The tutorials helped develop a selection methodology.</p>

<p><strong>Importance of simulation</strong>:</p>
<p>LTspice and other simulators allow circuit validation before manufacturing. This saves considerable time and provides a valuable learning experience.</p>

<h3 class="section-title">Practical Applications</h3>

<p><strong>For embedded electronics engineers</strong>:</p>
<ul>
<li>Design IoT systems with multiple sensors</li>
<li>Size data acquisition boards</li>
<li>Interface sensors with microcontrollers</li>
<li>Optimize power consumption and performance</li>
</ul>

<p><strong>For instrumentation engineers</strong>:</p>
<ul>
<li>Design scientific measurement instruments</li>
<li>Develop medical equipment</li>
<li>Build test and validation systems</li>
<li>Ensure standards compliance (accuracy, safety)</li>
</ul>

<p><strong>For automotive engineers</strong>:</p>
<ul>
<li>Acquire data from multiple sensors (pressure, temperature, acceleration, etc.)</li>
<li>Communication buses (CAN, LIN, FlexRay)</li>
<li>Severe constraints (temperature, vibrations, EMI)</li>
</ul>

<p><strong>For audio engineers</strong>:</p>
<ul>
<li>Design audio interfaces (microphones, headphones)</li>
<li>Develop recording equipment</li>
<li>Optimize sound quality (SNR, THD)</li>
</ul>

<h3 class="section-title">Limitations and Openings</h3>

<p><strong>Module limitations</strong>:</p>
<ul>
<li>Few hands-on laboratory sessions (mostly theoretical tutorials)</li>
<li>No complete PCB design and manufacturing project</li>
<li>Software aspects (drivers, real-time processing) not explored in depth</li>
</ul>

<p><strong>Openings towards</strong>:</p>
<ul>
<li><strong>Advanced signal processing</strong>: adaptive filtering, spectral analysis</li>
<li><strong>Real-time systems</strong>: temporal constraints, RTOS</li>
<li><strong>Embedded machine learning</strong>: preprocessing and classification of sensor data</li>
<li><strong>IoT and wireless communication</strong>: BLE, LoRa, WiFi for connected systems</li>
</ul>

<h3 class="section-title">Recent Developments</h3>

<p><strong>Increased integration</strong>:</p>
<p>Trend towards System-on-Chip (SoC) integrating sensors, ADC, processing, communication.</p>
<p>Examples: MCU with integrated 16-bit ADC, Bluetooth SoC with ADC/DAC.</p>
<p>Advantages: compactness, low cost, reduced power consumption.</p>

<p><strong>MEMS sensors</strong>:</p>
<p>Miniaturized and integrated micro-electromechanical systems.</p>
<p>Accelerometers, gyroscopes, microphones, silicon pressure sensors.</p>
<p>Revolutionizing consumer electronics (smartphones, wearables).</p>

<p><strong>Edge Computing</strong>:</p>
<p>Processing data as close to the sensor as possible (instead of the cloud).</p>
<p>Enables reduced latency, bandwidth, and privacy preservation.</p>
<p>Requires efficient ADCs and optimized embedded processing.</p>

<p><strong>Embedded AI</strong>:</p>
<p>Neural networks on microcontrollers for real-time classification (voice recognition, anomaly detection).</p>
<p>Acquisition chains optimized for preprocessing before inference.</p>

<h3 class="section-title">Tips for Success</h3>

<p><strong>1. Understand the physics</strong>:</p>
<p>Behind each component, there is a physical phenomenon. Understanding the physics helps anticipate limitations and optimize.</p>

<p><strong>2. Read datasheets carefully</strong>:</p>
<p>Datasheets contain everything: electrical characteristics, application schematics, operating conditions. Learn to exploit them methodically.</p>

<p><strong>3. Simulate before building</strong>:</p>
<p>LTspice, TINA, and other simulators allow rapid circuit validation. Investing time in simulation avoids costly mistakes.</p>

<p><strong>4. Perform noise budget calculations</strong>:</p>
<p>Systematically evaluate each noise source to identify the limiting link and focus efforts.</p>

<p><strong>5. Test and measure</strong>:</p>
<p>Theory provides the framework, but practice reveals subtleties (coupling, drift, interference). Measure to validate.</p>

<p><strong>6. Develop intuition</strong>:</p>
<p>With experience, develop a sense of orders of magnitude (typical op-amp noise, required resolution depending on application, etc.).</p>

<h3 class="section-title">Conclusion</h3>

<p>This module is fundamental for any engineer working on embedded systems, instrumentation, or IoT. Data acquisition is ubiquitous: smartphones, automobiles, industry, medical, home automation, etc.</p>

<p><strong>Transferable skills</strong>:</p>
<ul>
<li>System vision and methodical approach</li>
<li>Ability to size and optimize complex systems</li>
<li>Mastery of communication interfaces (essential for any embedded system)</li>
<li>Deep understanding of the analog/digital trade-off</li>
</ul>

<p><strong>Professional relevance</strong>:</p>
<p>The explosion of IoT and connected systems increases the demand for engineers mastering acquisition chains. These skills are sought after in all sectors.</p>

<p><strong>Key message</strong>:</p>
<p>An acquisition chain is only as good as its weakest link. The best ADC in the world will not compensate for poorly designed conditioning or an unsuitable sensor. The system-level approach is key.</p>

<p><strong>Recommendations</strong>:</p>
<ul>
<li>Deepen knowledge through personal projects (Arduino, Raspberry Pi with sensors)</li>
<li>Study reference designs (application circuits in datasheets)</li>
<li>Practice simulation (LTspice is free and powerful)</li>
<li>Follow tutorials on interfaces (SPI, I2C) with a logic analyzer</li>
<li>Complete a full project: sensor &rarr; conditioning &rarr; ADC &rarr; microcontroller &rarr; display/transmission</li>
</ul>

<p><strong>Related courses</strong>:</p>
<ul>
<li><a href="./filtrage-actif-bruit.html">Active Filtering and Noise - S7</a>: analog filters, noise sources</li>
<li><a href="./microcontroleur.html">Microcontrollers - S6</a>: SPI/I2C/UART interfaces</li>
<li><a href="./filtrage-numerique.html">Digital Filtering - S6</a>: post-acquisition processing</li>
<li><a href="./signal.html">Signal Processing - S5</a>: sampling, Shannon's theorem</li>
<li><a href="./machine-learning-s8.html">Machine Learning - S8</a>: sensor data preprocessing</li>
</ul>

<hr/>

<p><em>Course taken in 2023-2024 at INSA Toulouse, Department of Electrical Engineering and Computer Science.</em></p>

<div class="back-nav">
    <a href="./my-courses-2023-2024.html" data-i18n-html="back-courses-2023-2024">&larr; Back to Courses 2023-2024</a>
</div>

<hr/>

<h2>Course Documents</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Signal Conditioning</h4>
      <p>Course on signal conditioning: amplification, filtering, impedance matching and preparation for conversion.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S8/Chaines-Acquisition/conditionneur.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S8/Chaines-Acquisition/conditionneur.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>Analog-to-Digital Converters</h4>
      <p>Course on ADCs: architectures (flash, SAR, sigma-delta), performance (resolution, speed, SNR) and selection.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S8/Chaines-Acquisition/convertisseurs-can.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S8/Chaines-Acquisition/convertisseurs-can.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>Digital Sensors</h4>
      <p>Implementation of digital sensors: I2C/SPI protocols, configuration, calibration and data exploitation.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S8/Chaines-Acquisition/capteurs-numeriques.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S8/Chaines-Acquisition/capteurs-numeriques.pdf" target="_blank">Download</a></p>
    </div>
  </div>
</div>

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

<style>
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

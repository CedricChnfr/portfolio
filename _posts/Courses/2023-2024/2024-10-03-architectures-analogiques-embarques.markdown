---
layout: default
title:  "Architectures Analogiques Systèmes Embarqués - S7"
date:   2024-10-02 09:02:00 +0200
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
    <a href="./my-courses-2023-2024.html" data-i18n-html="back-courses-2023-2024">&larr; Retour aux Cours 2023-2024</a>
</div>

<div class="lang-fr">

<h1>Architectures Analogiques Systemes Embarques - Semestre 7</h1>

<p><strong>Annee Universitaire</strong> : 2023-2024<br/>
<strong>Semestre</strong> : 7<br/>
<strong>Credits</strong> : 2.5 ECTS<br/>
<strong>Specialite</strong> : Electronique Analogique et Systemes Embarques</p>

<hr/>

<h2>PART A - Presentation Generale du Module</h2>

<h3 class="section-title">Vue d'ensemble</h3>

<p>Ce cours traite des architectures analogiques specifiques aux systemes embarques : amplificateurs commandes en tension, filtres a frequence de coupure variable, modulateurs, et circuits de conditionnement de signaux. L'accent est mis sur les circuits programmables et adaptatifs essentiels pour les systemes intelligents et reconfigurables.</p>

<p><strong>Objectifs pedagogiques</strong> :</p>
<ul>
<li>Concevoir des amplificateurs a gain commande en tension (VCA)</li>
<li>Maitriser les filtres actifs commandes en tension</li>
<li>Comprendre les modulateurs et leurs applications</li>
<li>Simuler et dimensionner des circuits analogiques complexes</li>
<li>Realiser des PCB pour circuits analogiques</li>
<li>Utiliser des composants specialises (transconductance amplifiers)</li>
</ul>

<h3 class="section-title">Position dans le cursus</h3>

<p>Ce module s'appuie sur :</p>
<ul>
<li><strong>Electronique Fonctions Analogiques (S6)</strong> : AOPs, filtres actifs</li>
<li><strong>Projet PCB (S6)</strong> : conception de cartes electroniques</li>
<li><strong>Circuits et Filtres analogiques (S5)</strong> : filtres, fonction de transfert</li>
</ul>

<p>Il prepare a :</p>
<ul>
<li><strong>Systemes embarques</strong> : conditionnement de signaux, interfaces analogiques</li>
<li><strong>Instrumentation</strong> : circuits a gain programmable</li>
<li><strong>Audio professionnel</strong> : mixeurs, egaliseurs, effets</li>
<li><strong>Telecommunications</strong> : controle automatique de gain (AGC)</li>
</ul>

<hr/>

<h2>PART B - Experience Personnelle et Contexte d'Apprentissage</h2>

<h3 class="section-title">Organisation et ressources</h3>

<p>Le module etait organise en travaux diriges et bureau d'etudes pratique :</p>

<p><strong>Travaux diriges (12h)</strong> :</p>
<ul>
<li>TD1 : Amplificateur a gain commande en tension</li>
<li>TD2 : Filtre passe-bas ordre 1 a frequence de coupure commandee en tension</li>
</ul>

<p><strong>Bureau d'etudes (16h)</strong> :</p>
<p>Projet complet de conception d'un modulateur :</p>
<ul>
<li>Partie 1 : Amplificateur a gain commande en tension</li>
<li>Partie 2 : Filtre ordre 1 commande en tension</li>
<li>Projet final : Modulateur complet avec PCB sur Altium Designer</li>
</ul>

<p><strong>Supports pedagogiques</strong> :</p>
<ul>
<li>Enonces de TD en PDF</li>
<li>Documentation composant LM13700 (transconductance amplifier)</li>
<li>Simulations TINA-TI (logiciel de simulation analogique Texas Instruments)</li>
<li>Projet Altium Designer pour realisation PCB</li>
</ul>

<h3 class="section-title">Contenu du projet</h3>

<p><strong>Projet modulateur</strong> :</p>

<p>Le projet consistait a concevoir un modulateur complet integrant :</p>
<ul>
<li>Amplificateur a gain variable</li>
<li>Filtre passe-bas a frequence de coupure variable</li>
<li>Circuit de modulation</li>
<li>Design PCB complet avec Altium Designer</li>
</ul>

<p><strong>Librairies creees</strong> :</p>
<ul>
<li>4AE_LM.SCHLIB : symboles schematiques</li>
<li>LIB_V2.SCHLIB : bibliotheque de composants version 2</li>
<li>ACT.PcbLib : empreintes PCB</li>
<li>PRINT_V2.PcbLib : empreintes d'impression version 2</li>
</ul>

<p><strong>Simulations TINA</strong> :</p>
<ul>
<li>AOP_non_inverseur.TSC : amplificateur non inverseur de base</li>
<li>Passe_bas.TSC : filtre passe-bas simple</li>
<li>Filtre_Com_Tension.TSC : filtre commande en tension</li>
<li>Modulateur.TSC : circuit modulateur complet</li>
</ul>

<h3 class="section-title">Methode de travail</h3>

<p><strong>Phase 1 : Etude theorique</strong> :</p>
<p>Analyse des circuits dans les TD, calculs de fonctions de transfert, dimensionnement des composants.</p>

<p><strong>Phase 2 : Simulations</strong> :</p>
<p>Validation des circuits sous TINA-TI avant realisation. Ajustement des parametres pour obtenir les performances souhaitees.</p>

<p><strong>Phase 3 : Conception PCB</strong> :</p>
<p>Creation des schemas sous Altium Designer, routage du PCB, verifications DRC/ERC, generation des fichiers de fabrication.</p>

<h3 class="section-title">Difficultes rencontrees</h3>

<p><strong>Composant LM13700</strong> :</p>
<p>L'amplificateur de transconductance LM13700 est un composant specialise. Comprendre son fonctionnement et dimensionner les resistances externes demande une bonne comprehension de la transconductance.</p>

<p><strong>Stabilite des circuits</strong> :</p>
<p>Les circuits commandes en tension peuvent presenter des instabilites si mal dimensionnes. Importance de la compensation et des condensateurs de stabilisation.</p>

<p><strong>Routage PCB</strong> :</p>
<p>Pour des circuits analogiques precis, le routage est critique (decouplage, pistes courtes, plan de masse).</p>

<hr/>

<h2>PART C - Aspects Techniques Detailles</h2>

<h3 class="section-title">1. Amplificateurs de transconductance</h3>

<p><strong>Definition</strong> :</p>

<p>Un amplificateur de transconductance convertit une tension d'entree en un courant de sortie proportionnel.</p>

<p>I_sortie = gm x V_entree</p>

<p>ou gm est la transconductance (en Siemens ou mho).</p>

<p><strong>LM13700 - Operational Transconductance Amplifier (OTA)</strong> :</p>

<p>Circuit integre contenant deux OTA independants.</p>

<p><strong>Principe</strong> :</p>
<ul>
<li>La transconductance gm est commandee par un courant de polarisation I_abc (amplifier bias current)</li>
<li>gm = 19,2 x I_abc (approximation)</li>
<li>Permet de commander le gain en ajustant I_abc</li>
</ul>

<p><strong>Avantages</strong> :</p>
<ul>
<li>Gain programmable electroniquement</li>
<li>Large plage de variation</li>
<li>Linearite acceptable</li>
</ul>

<p><strong>Applications</strong> :</p>
<ul>
<li>VCA (Voltage Controlled Amplifier)</li>
<li>VCF (Voltage Controlled Filter)</li>
<li>Modulateurs</li>
<li>AGC (Automatic Gain Control)</li>
</ul>

<h3 class="section-title">2. Amplificateur a gain commande en tension (VCA)</h3>

<p><strong>Principe</strong> :</p>

<p>Un VCA est un amplificateur dont le gain est controle par une tension externe.</p>

<p>V_sortie = A(V_controle) x V_entree</p>

<p><strong>Realisation avec LM13700</strong> :</p>

<p><strong>Circuit de base</strong> :</p>
<ul>
<li>OTA du LM13700</li>
<li>Resistance de charge en sortie</li>
<li>Tension de commande convertie en courant I_abc via une resistance</li>
</ul>

<p><strong>Calcul du gain</strong> :</p>

<p>Gain = gm x R_charge = (19,2 x I_abc) x R_charge</p>

<p>Pour commander le gain par une tension V_ctrl :</p>
<p>I_abc = V_ctrl / R_ctrl</p>

<p>Donc : Gain = (19,2 x V_ctrl x R_charge) / R_ctrl</p>

<p><strong>Plage de gain</strong> :</p>

<p>Typiquement de -40 dB a +40 dB en variant V_ctrl.</p>

<p><strong>Linearisation</strong> :</p>

<p>Pour ameliorer la linearite, on peut utiliser :</p>
<ul>
<li>Diodes de linearisation (incluses dans le LM13700)</li>
<li>Resistances d'emetteur</li>
<li>Contre-reaction</li>
</ul>

<p><strong>Applications</strong> :</p>

<table>
<tr><th>Application</th><th>Description</th></tr>
<tr><td>Mixeur audio</td><td>Controle du niveau de chaque canal</td></tr>
<tr><td>AGC</td><td>Ajustement automatique du gain</td></tr>
<tr><td>Compresseur/limiteur</td><td>Traitement dynamique audio</td></tr>
<tr><td>Modulateur d'amplitude</td><td>Multiplication de signaux</td></tr>
</table>

<h3 class="section-title">3. Filtres commandes en tension</h3>

<p><strong>Filtre passe-bas du premier ordre commande</strong> :</p>

<p><strong>Principe</strong> :</p>
<p>Utiliser un OTA pour creer une resistance equivalente variable.</p>

<p><strong>Fonction de transfert</strong> :</p>

<p>H(jw) = 1 / (1 + jw / wc)</p>

<p>avec wc = 2pi fc (pulsation de coupure)</p>

<p><strong>Frequence de coupure commandee</strong> :</p>

<p>En utilisant un OTA, on peut faire varier fc proportionnellement a la tension de commande.</p>

<p>fc = gm / (2pi C) = (19,2 x I_abc) / (2pi C)</p>

<p>Si I_abc = V_ctrl / R_ctrl :</p>

<p>fc = (19,2 x V_ctrl) / (2pi C x R_ctrl)</p>

<p><strong>Plage de frequence</strong> :</p>

<p>Typiquement de quelques Hz a plusieurs dizaines de kHz selon V_ctrl.</p>

<p><strong>Filtre passe-bas ordre 2 (Sallen-Key commande)</strong> :</p>

<p>En cascadant deux cellules du premier ordre ou en utilisant une structure Sallen-Key avec OTA.</p>

<p>Meilleure selectivite (-40 dB/decade).</p>

<p><strong>Applications</strong> :</p>

<table>
<tr><th>Application</th><th>Description</th></tr>
<tr><td>Egaliseur parametrique</td><td>Ajustement de la frequence de coupure</td></tr>
<tr><td>Filtre anti-aliasing adaptatif</td><td>Ajuste selon frequence d'echantillonnage</td></tr>
<tr><td>Synthetiseur audio</td><td>Filtre VCF pour synthese soustractive</td></tr>
<tr><td>Traitement adaptatif</td><td>Filtrage en fonction du contenu du signal</td></tr>
</table>

<h3 class="section-title">4. Modulateurs</h3>

<p><strong>Definition</strong> :</p>

<p>Circuit qui realise la multiplication de deux signaux.</p>

<p><strong>Modulation d'amplitude</strong> :</p>

<p>s(t) = [A + m(t)] x cos(wp t)</p>

<p>ou m(t) est le signal modulant, cos(wp t) la porteuse.</p>

<p><strong>Realisation avec OTA</strong> :</p>

<p>L'OTA peut servir de multiplieur car :</p>
<p>I_sortie = gm x V_entree</p>

<p>Si gm est proportionnel a un signal (via I_abc), on obtient une multiplication.</p>

<p><strong>Circuit modulateur</strong> :</p>

<p><strong>Entrees</strong> :</p>
<ul>
<li>Signal porteur : applique a l'entree de l'OTA</li>
<li>Signal modulant : commande la transconductance gm (via I_abc)</li>
</ul>

<p><strong>Sortie</strong> :</p>
<p>Signal module en amplitude.</p>

<p><strong>Modulateur en anneau (ring modulator)</strong> :</p>

<p>Utilise 4 OTA ou diodes en pont pour realiser une multiplication exacte.</p>

<p>Sortie : s(t) = m1(t) x m2(t)</p>

<p><strong>Applications</strong> :</p>
<ul>
<li>Modulation AM</li>
<li>Melangeur de frequences (heterodynage)</li>
<li>Effets audio (tremolo, chorus)</li>
<li>Demodulation synchrone</li>
</ul>

<h3 class="section-title">5. Circuits de conditionnement</h3>

<p><strong>Conditionnement de capteurs</strong> :</p>

<p>Les signaux issus de capteurs necessitent souvent un traitement avant numerisation.</p>

<p><strong>Etapes typiques</strong> :</p>

<ol>
<li><strong>Amplification</strong> : VCA pour adapter le niveau</li>
<li><strong>Filtrage</strong> : Eliminer le bruit et les frequences indesirables</li>
<li><strong>Offset</strong> : Ajuster le niveau DC</li>
<li><strong>Protection</strong> : Ecretage, limitation</li>
</ol>

<p><strong>Amplificateur d'instrumentation</strong> :</p>

<p>Circuit specialise pour amplifier les signaux differentiels de faible amplitude.</p>

<p><strong>Caracteristiques</strong> :</p>
<ul>
<li>Tres haute impedance d'entree</li>
<li>Gain precis et stable</li>
<li>CMRR eleve (&gt; 100 dB)</li>
<li>Faible bruit</li>
</ul>

<p><strong>Applications</strong> :</p>
<ul>
<li>Jauges de contrainte</li>
<li>Thermocouples</li>
<li>Ponts de Wheatstone</li>
<li>Mesures biomedicales (ECG, EMG)</li>
</ul>

<p><strong>Filtre anti-aliasing</strong> :</p>

<p>Filtre passe-bas place avant un ADC pour eviter le repliement spectral (aliasing).</p>

<p><strong>Regle</strong> :</p>
<p>fc &lt; fs / 2 (frequence d'echantillonnage / 2)</p>

<p>Typiquement : fc = 0,4 x fs</p>

<h3 class="section-title">6. Controle automatique de gain (AGC)</h3>

<p><strong>Principe</strong> :</p>

<p>Circuit qui ajuste automatiquement le gain pour maintenir un niveau de sortie constant malgre les variations de l'entree.</p>

<p><strong>Boucle de regulation</strong> :</p>

<ol>
<li><strong>Detecteur d'amplitude</strong> : Mesure le niveau de sortie (detecteur de crete ou RMS)</li>
<li><strong>Comparateur</strong> : Compare au niveau de reference</li>
<li><strong>Integrateur</strong> : Filtre la tension d'erreur (temps de reponse)</li>
<li><strong>VCA</strong> : Ajuste le gain selon la tension de commande</li>
</ol>

<p><strong>Parametres</strong> :</p>

<ul>
<li><strong>Temps d'attaque</strong> : Rapidite de reduction du gain (signal fort)</li>
<li><strong>Temps de relachement</strong> : Rapidite d'augmentation du gain (signal faible)</li>
<li><strong>Seuil</strong> : Niveau a partir duquel l'AGC agit</li>
</ul>

<p><strong>Applications</strong> :</p>

<table>
<tr><th>Application</th><th>Description</th></tr>
<tr><td>Recepteurs radio</td><td>Maintenir le volume constant</td></tr>
<tr><td>Telephonie</td><td>Normalisation du niveau vocal</td></tr>
<tr><td>Enregistrement audio</td><td>Eviter la saturation</td></tr>
<tr><td>Instrumentation</td><td>Adapter la dynamique du signal</td></tr>
</table>

<h3 class="section-title">7. Techniques de simulation</h3>

<p><strong>TINA-TI</strong> :</p>

<p>Logiciel de simulation analogique gratuit de Texas Instruments.</p>

<p><strong>Fonctionnalites</strong> :</p>
<ul>
<li>Simulation temporelle (transitoire)</li>
<li>Analyse frequentielle (AC)</li>
<li>Analyse de bruit</li>
<li>Analyse de distorsion harmonique</li>
<li>Analyse de sensibilite</li>
</ul>

<p><strong>Methodologie</strong> :</p>

<ol>
<li><strong>Schema</strong> : Dessiner le circuit</li>
<li><strong>Modeles</strong> : Utiliser les modeles SPICE des composants</li>
<li><strong>Simulation</strong> : Choisir le type d'analyse</li>
<li><strong>Visualisation</strong> : Courbes de reponse</li>
<li><strong>Optimisation</strong> : Ajuster les valeurs</li>
</ol>

<p><strong>Exemple : amplificateur a gain variable</strong></p>

<p>Simulation :</p>
<ul>
<li>Analyse AC : reponse en frequence pour differentes tensions de commande</li>
<li>Analyse transitoire : reponse a un signal sinusoidal</li>
<li>Mesure du gain en dB</li>
<li>Verification de la linearite</li>
</ul>

<h3 class="section-title">8. Conception PCB pour circuits analogiques</h3>

<p><strong>Regles de conception</strong> :</p>

<p><strong>Layout critique</strong> :</p>

<table>
<tr><th>Aspect</th><th>Recommandation</th></tr>
<tr><td>Plan de masse</td><td>Cuivre plein pour GND</td></tr>
<tr><td>Decouplage</td><td>Condensateur 100 nF proche de chaque alimentation</td></tr>
<tr><td>Pistes courtes</td><td>Minimiser les inductances parasites</td></tr>
<tr><td>Separation analogique/numerique</td><td>Plans de masse separes si mixte</td></tr>
<tr><td>Symetrie</td><td>Circuits differentiels symetriques</td></tr>
</table>

<p><strong>Alimentation</strong> :</p>

<ul>
<li>Decouplage local : 100 nF ceramique + 10 uF electrolytique par CI</li>
<li>Pistes d'alimentation larges</li>
<li>Filtrage de l'alimentation (ferrite, LC)</li>
</ul>

<p><strong>Signaux sensibles</strong> :</p>

<ul>
<li>Pistes d'entree courtes et protegees</li>
<li>Eviter les boucles de masse</li>
<li>Garde (guard ring) autour des circuits critiques</li>
</ul>

<p><strong>Composants</strong> :</p>

<ul>
<li>Resistances : precision 1% ou mieux pour gain stable</li>
<li>Condensateurs : COG/NP0 pour circuits de precision</li>
<li>AOPs : choisir selon bande passante, bruit, offset</li>
</ul>

<h3 class="section-title">9. Altium Designer pour le projet</h3>

<p><strong>Projet BE_Archi_Sys_Emb</strong> :</p>

<p>Structure du projet :</p>
<ul>
<li>Fichier projet : BE_Archi_Sys_Emb.PrjPcb</li>
<li>Schema : Modulateur.SchDoc</li>
<li>Bibliotheques : 4AE_LM.SCHLIB, LIB_V2.SCHLIB</li>
<li>Empreintes : ACT.PcbLib, PRINT_V2.PcbLib</li>
</ul>

<p><strong>Etapes de conception</strong> :</p>

<ol>
<li><strong>Creation des bibliotheques</strong> :
<ul>
<li>Symboles schematiques (LM13700, resistances, condensateurs)</li>
<li>Empreintes PCB (DIP8, CMS 0805)</li>
</ul></li>

<li><strong>Schema electrique</strong> :
<ul>
<li>Placement des composants</li>
<li>Connexions (nets)</li>
<li>Annotations (valeurs, references)</li>
<li>Verifications ERC</li>
</ul></li>

<li><strong>PCB</strong> :
<ul>
<li>Import du schema</li>
<li>Placement des composants</li>
<li>Routage manuel ou automatique</li>
<li>Verifications DRC</li>
<li>Plans de masse et alimentation</li>
</ul></li>

<li><strong>Generation fichiers</strong> :
<ul>
<li>Gerber (fabrication)</li>
<li>BOM (liste composants)</li>
<li>Fichiers d'assemblage</li>
</ul></li>
</ol>

<h3 class="section-title">10. Applications pratiques</h3>

<p><strong>Table de mixage audio</strong> :</p>

<p>Chaque canal dispose d'un VCA pour controler le volume. Les faders ajustent la tension de commande.</p>

<p><strong>Synthetiseur analogique</strong> :</p>

<ul>
<li>VCO (Voltage Controlled Oscillator) : frequence variable</li>
<li>VCF (Voltage Controlled Filter) : filtre a fc variable</li>
<li>VCA : enveloppe d'amplitude (ADSR)</li>
</ul>

<p><strong>Compresseur audio</strong> :</p>

<p>Circuit AGC avec detecteur RMS et parametres d'attaque/relachement reglables.</p>

<p>Reduit la dynamique du signal (plage entre le plus faible et le plus fort).</p>

<p><strong>Egaliseur parametrique</strong> :</p>

<p>Plusieurs filtres passe-bande avec frequence centrale, gain et facteur Q commandes.</p>

<p><strong>Recepteur radio adaptatif</strong> :</p>

<p>AGC pour maintenir le niveau constant malgre la variation du signal RF recu.</p>
<p>Filtres FI a bande passante variable selon les conditions de reception.</p>

<hr/>

<h2>PART D - Analyse Reflexive et Perspectives</h2>

<h3 class="section-title">Competences acquises</h3>

<p><strong>Conception de circuits commandes</strong> :</p>
<p>Maitrise des amplificateurs et filtres a parametres variables electroniquement. Capacite a utiliser les OTA pour creer des circuits reconfigurables.</p>

<p><strong>Simulation analogique</strong> :</p>
<p>Utilisation efficace de TINA-TI pour valider les circuits avant realisation. Comprehension des analyses AC, transitoires, et de bruit.</p>

<p><strong>Conception PCB professionnelle</strong> :</p>
<p>Realisation complete d'un PCB sous Altium Designer : creation de bibliotheques, schema, routage, verifications.</p>

<h3 class="section-title">Points cles a retenir</h3>

<p><strong>1. OTA = composant polyvalent</strong> :</p>
<p>L'amplificateur de transconductance (LM13700) permet de creer des VCA, VCF, modulateurs simplement en exploitant la commande de gm.</p>

<p><strong>2. Linearite vs plage dynamique</strong> :</p>
<p>Les circuits commandes presentent souvent un compromis entre linearite et plage de variation. Importance de la linearisation.</p>

<p><strong>3. Stabilite essentielle</strong> :</p>
<p>Les circuits a gain variable peuvent osciller si mal compenses. Condensateurs de stabilisation critiques.</p>

<p><strong>4. Layout = performance</strong> :</p>
<p>Pour les circuits analogiques precis, le layout PCB est aussi important que le schema. Plan de masse, decouplage, symetrie.</p>

<p><strong>5. Simulation = gain de temps</strong> :</p>
<p>Simuler avant realiser evite les erreurs couteuses (PCB a refaire, composants grilles).</p>

<h3 class="section-title">Applications pratiques</h3>

<p><strong>Audio professionnel</strong> :</p>
<p>Mixeurs, compresseurs, egaliseurs, effets utilisent massivement les VCA et VCF.</p>

<p><strong>Instrumentation</strong> :</p>
<p>Amplificateurs a gain programmable pour s'adapter automatiquement a la plage du signal mesure.</p>

<p><strong>Telecommunications</strong> :</p>
<p>AGC dans tous les recepteurs radio (AM, FM, GSM, WiFi, etc.).</p>

<p><strong>Systemes embarques</strong> :</p>
<p>Conditionnement adaptatif de signaux capteurs selon les conditions.</p>

<h3 class="section-title">Retour d'experience</h3>

<p><strong>Projet complet et formateur</strong> :</p>
<p>Le BE permet de passer par toutes les etapes d'un projet reel : specifications, conception, simulation, PCB, verifications.</p>

<p><strong>LM13700 interessant</strong> :</p>
<p>Composant vintage mais toujours pertinent pedagogiquement. Les OTA modernes (OPA860, etc.) utilisent les memes principes.</p>

<p><strong>Simulations TINA utiles</strong> :</p>
<p>Les simulations permettent de visualiser immediatement l'effet des changements de parametres (resistances, condensateurs).</p>

<p><strong>Altium Designer professionnel</strong> :</p>
<p>Outil utilise en industrie. Competence valorisable en entreprise.</p>

<h3 class="section-title">Limites et ouvertures</h3>

<p><strong>Limites du module</strong> :</p>
<ul>
<li>Pas de realisation physique et test du PCB</li>
<li>Composants analogiques classiques (alternatives numeriques non abordees)</li>
<li>Aspects bruit et distorsion peu approfondis</li>
</ul>

<p><strong>Ouvertures vers</strong> :</p>
<ul>
<li><strong>DSP (Digital Signal Processing)</strong> : alternative numerique aux circuits analogiques</li>
<li><strong>Systemes mixtes</strong> : ADC, DAC, conversion analogique-numerique</li>
<li><strong>Audio numerique</strong> : codecs, effets numeriques</li>
<li><strong>Controle numerique de circuits analogiques</strong> : potentiometres numeriques, DAC pour commande</li>
<li><strong>SoC mixtes</strong> : integration analogique-numerique sur puce</li>
</ul>

<h3 class="section-title">Evolution technologique</h3>

<p><strong>Tendances actuelles</strong> :</p>

<p><strong>Circuits programmables</strong> :</p>
<ul>
<li>FPAA (Field Programmable Analog Array) : equivalent analogique des FPGA</li>
<li>Potentiometres numeriques commandes par SPI/I2C</li>
<li>VGA (Variable Gain Amplifier) integres avec controle numerique</li>
</ul>

<p><strong>Integration</strong> :</p>
<ul>
<li>AFE (Analog Front-End) integrant conditionnement complet</li>
<li>Codec audio integres (ADC + DAC + VCA + filtres)</li>
<li>SoC avec partie analogique reconfigurable</li>
</ul>

<p><strong>Performance</strong> :</p>
<ul>
<li>Tres faible bruit (&lt; 1 nV/sqrt(Hz))</li>
<li>Tres faible consommation (nA de quiescent current)</li>
<li>Large dynamique (&gt; 120 dB)</li>
</ul>

<h3 class="section-title">Conseils pour reussir</h3>

<p><strong>1. Comprendre le LM13700</strong> :</p>
<p>Bien assimiler le principe de la transconductance commandee. Lire attentivement la datasheet.</p>

<p><strong>2. Simuler systematiquement</strong> :</p>
<p>Chaque modification doit etre validee par simulation avant d'aller plus loin.</p>

<p><strong>3. Dimensionner avec soin</strong> :</p>
<p>Les valeurs de resistances et condensateurs determinent les performances. Utiliser les formules donnees.</p>

<p><strong>4. Verifier le PCB</strong> :</p>
<p>DRC/ERC sont imperatifs. Une erreur sur le PCB coute cher (refabrication).</p>

<p><strong>5. Documenter</strong> :</p>
<p>Bien annoter les schemas, calculer et noter les valeurs theoriques pour comparer avec les simulations.</p>

<h3 class="section-title">Conclusion</h3>

<p>Ce module fournit une excellente introduction aux circuits analogiques reconfigurables et commandes. La maitrise des VCA, VCF et modulateurs est essentielle pour de nombreuses applications (audio, instrumentation, telecommunications).</p>

<p><strong>Approche projet</strong> :</p>
<p>Le bureau d'etudes avec conception complete (simulation + PCB) reflete bien le travail d'un ingenieur electronique. Toutes les etapes d'un projet reel sont couvertes.</p>

<p><strong>Competences transferables</strong> :</p>
<ul>
<li>Conception de circuits analogiques complexes</li>
<li>Simulation avec outils professionnels (TINA, SPICE)</li>
<li>Conception PCB avec Altium Designer</li>
<li>Gestion de projet electronique complet</li>
</ul>

<p><strong>Message principal</strong> :</p>
<p>Les circuits commandes en tension apportent de la flexibilite et de l'adaptabilite aux systemes analogiques. Ils permettent de creer des systemes intelligents capables de s'adapter automatiquement aux conditions (AGC, filtrage adaptatif).</p>

<p><strong>Recommandations</strong> :</p>
<ul>
<li>Experimenter avec des kits d'evaluation (Texas Instruments, Analog Devices)</li>
<li>Realiser et tester physiquement le PCB concu</li>
<li>Explorer les alternatives numeriques (DSP) pour comparaison</li>
<li>Approfondir les aspects bruit, distorsion, linearite</li>
</ul>

<p><strong>Liens avec les autres cours</strong> :</p>
<ul>
<li><a href="./electronique-fonctions-analogiques.html">Electronique Fonctions Analogiques - S6</a> : AOPs, filtres actifs</li>
<li><a href="./projet-pcb.html">Projet PCB - S6</a> : conception de cartes</li>
<li><a href="./architectures-analogiques-transmission.html">Architectures Analogiques Transmission - S7</a> : modulation, RF</li>
</ul>

<hr/>

<h2>Documents de Cours</h2>

</div>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">Sujet Bureau d'Etudes</span>
        <span class="lang-en">Lab Study Subject</span>
      </h4>
      <p>
        <span class="lang-fr">Sujet complet du BE : conception d'un modulateur et filtre commandes en tension avec TINA et Altium Designer.</span>
        <span class="lang-en">Complete lab study subject: design of a voltage-controlled modulator and filter using TINA and Altium Designer.</span>
      </p>
      <div class="pdf-lazy" data-src="/cours-pdf/S7/Archi-Analogiques-Embarques/sujet-be.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S7/Archi-Analogiques-Embarques/sujet-be.pdf" target="_blank">
        <span class="lang-fr">Telecharger</span>
        <span class="lang-en">Download</span>
      </a></p>
    </div>
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">TD1 - Gain Commande en Tension</span>
        <span class="lang-en">TD1 - Voltage-Controlled Gain</span>
      </h4>
      <p>
        <span class="lang-fr">TD sur la conception d'amplificateurs a gain variable commande en tension (VCA) avec OTA et circuits integres.</span>
        <span class="lang-en">Tutorial on the design of voltage-controlled variable gain amplifiers (VCA) with OTA and integrated circuits.</span>
      </p>
      <div class="pdf-lazy" data-src="/cours-pdf/S7/Archi-Analogiques-Embarques/td1-gain-commande.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S7/Archi-Analogiques-Embarques/td1-gain-commande.pdf" target="_blank">
        <span class="lang-fr">Telecharger</span>
        <span class="lang-en">Download</span>
      </a></p>
    </div>
  </div>
</div>

<div class="lang-fr">
<hr/>
<p><em>Cours suivi en 2023-2024 a l'INSA Toulouse, Departement Genie Electrique et Informatique.</em></p>
</div>

<div class="lang-en">

<h1>Analog Architectures for Embedded Systems - Semester 7</h1>

<p><strong>Academic Year</strong>: 2023-2024<br/>
<strong>Semester</strong>: 7<br/>
<strong>Credits</strong>: 2.5 ECTS<br/>
<strong>Specialization</strong>: Analog Electronics and Embedded Systems</p>

<hr/>

<h2>PART A - General Module Presentation</h2>

<h3 class="section-title">Overview</h3>

<p>This course covers analog architectures specific to embedded systems: voltage-controlled amplifiers, variable cutoff frequency filters, modulators, and signal conditioning circuits. The emphasis is on programmable and adaptive circuits essential for intelligent and reconfigurable systems.</p>

<p><strong>Learning objectives</strong>:</p>
<ul>
<li>Design voltage-controlled gain amplifiers (VCA)</li>
<li>Master voltage-controlled active filters</li>
<li>Understand modulators and their applications</li>
<li>Simulate and size complex analog circuits</li>
<li>Design PCBs for analog circuits</li>
<li>Use specialized components (transconductance amplifiers)</li>
</ul>

<h3 class="section-title">Position in the curriculum</h3>

<p>This module builds upon:</p>
<ul>
<li><strong>Analog Functions Electronics (S6)</strong>: Op-amps, active filters</li>
<li><strong>PCB Project (S6)</strong>: electronic board design</li>
<li><strong>Analog Circuits and Filters (S5)</strong>: filters, transfer functions</li>
</ul>

<p>It prepares for:</p>
<ul>
<li><strong>Embedded systems</strong>: signal conditioning, analog interfaces</li>
<li><strong>Instrumentation</strong>: programmable gain circuits</li>
<li><strong>Professional audio</strong>: mixers, equalizers, effects</li>
<li><strong>Telecommunications</strong>: automatic gain control (AGC)</li>
</ul>

<hr/>

<h2>PART B - Personal Experience and Learning Context</h2>

<h3 class="section-title">Organization and resources</h3>

<p>The module was organized into tutorials and practical lab studies:</p>

<p><strong>Tutorials (12h)</strong>:</p>
<ul>
<li>TD1: Voltage-controlled gain amplifier</li>
<li>TD2: First-order low-pass filter with voltage-controlled cutoff frequency</li>
</ul>

<p><strong>Lab study (16h)</strong>:</p>
<p>Complete modulator design project:</p>
<ul>
<li>Part 1: Voltage-controlled gain amplifier</li>
<li>Part 2: Voltage-controlled first-order filter</li>
<li>Final project: Complete modulator with PCB on Altium Designer</li>
</ul>

<p><strong>Teaching resources</strong>:</p>
<ul>
<li>TD problem statements in PDF</li>
<li>LM13700 component documentation (transconductance amplifier)</li>
<li>TINA-TI simulations (Texas Instruments analog simulation software)</li>
<li>Altium Designer project for PCB fabrication</li>
</ul>

<h3 class="section-title">Project content</h3>

<p><strong>Modulator project</strong>:</p>

<p>The project consisted of designing a complete modulator integrating:</p>
<ul>
<li>Variable gain amplifier</li>
<li>Low-pass filter with variable cutoff frequency</li>
<li>Modulation circuit</li>
<li>Complete PCB design with Altium Designer</li>
</ul>

<p><strong>Libraries created</strong>:</p>
<ul>
<li>4AE_LM.SCHLIB: schematic symbols</li>
<li>LIB_V2.SCHLIB: component library version 2</li>
<li>ACT.PcbLib: PCB footprints</li>
<li>PRINT_V2.PcbLib: print footprints version 2</li>
</ul>

<p><strong>TINA simulations</strong>:</p>
<ul>
<li>AOP_non_inverseur.TSC: basic non-inverting amplifier</li>
<li>Passe_bas.TSC: simple low-pass filter</li>
<li>Filtre_Com_Tension.TSC: voltage-controlled filter</li>
<li>Modulateur.TSC: complete modulator circuit</li>
</ul>

<h3 class="section-title">Work methodology</h3>

<p><strong>Phase 1: Theoretical study</strong>:</p>
<p>Circuit analysis in tutorials, transfer function calculations, component sizing.</p>

<p><strong>Phase 2: Simulations</strong>:</p>
<p>Circuit validation under TINA-TI before fabrication. Parameter adjustment to achieve desired performance.</p>

<p><strong>Phase 3: PCB design</strong>:</p>
<p>Schematic creation in Altium Designer, PCB routing, DRC/ERC verifications, manufacturing file generation.</p>

<h3 class="section-title">Difficulties encountered</h3>

<p><strong>LM13700 component</strong>:</p>
<p>The LM13700 transconductance amplifier is a specialized component. Understanding its operation and sizing external resistors requires a good understanding of transconductance.</p>

<p><strong>Circuit stability</strong>:</p>
<p>Voltage-controlled circuits can exhibit instabilities if poorly sized. Compensation and stabilization capacitors are important.</p>

<p><strong>PCB routing</strong>:</p>
<p>For precise analog circuits, routing is critical (decoupling, short traces, ground plane).</p>

<hr/>

<h2>PART C - Detailed Technical Aspects</h2>

<h3 class="section-title">1. Transconductance amplifiers</h3>

<p><strong>Definition</strong>:</p>

<p>A transconductance amplifier converts an input voltage into a proportional output current.</p>

<p>I_output = gm x V_input</p>

<p>where gm is the transconductance (in Siemens or mho).</p>

<p><strong>LM13700 - Operational Transconductance Amplifier (OTA)</strong>:</p>

<p>Integrated circuit containing two independent OTAs.</p>

<p><strong>Principle</strong>:</p>
<ul>
<li>The transconductance gm is controlled by a bias current I_abc (amplifier bias current)</li>
<li>gm = 19.2 x I_abc (approximation)</li>
<li>Allows gain control by adjusting I_abc</li>
</ul>

<p><strong>Advantages</strong>:</p>
<ul>
<li>Electronically programmable gain</li>
<li>Wide variation range</li>
<li>Acceptable linearity</li>
</ul>

<p><strong>Applications</strong>:</p>
<ul>
<li>VCA (Voltage Controlled Amplifier)</li>
<li>VCF (Voltage Controlled Filter)</li>
<li>Modulators</li>
<li>AGC (Automatic Gain Control)</li>
</ul>

<h3 class="section-title">2. Voltage-controlled gain amplifier (VCA)</h3>

<p><strong>Principle</strong>:</p>

<p>A VCA is an amplifier whose gain is controlled by an external voltage.</p>

<p>V_output = A(V_control) x V_input</p>

<p><strong>Implementation with LM13700</strong>:</p>

<p><strong>Basic circuit</strong>:</p>
<ul>
<li>OTA from the LM13700</li>
<li>Load resistor at the output</li>
<li>Control voltage converted to I_abc current via a resistor</li>
</ul>

<p><strong>Gain calculation</strong>:</p>

<p>Gain = gm x R_load = (19.2 x I_abc) x R_load</p>

<p>To control gain with a voltage V_ctrl:</p>
<p>I_abc = V_ctrl / R_ctrl</p>

<p>Therefore: Gain = (19.2 x V_ctrl x R_load) / R_ctrl</p>

<p><strong>Gain range</strong>:</p>

<p>Typically from -40 dB to +40 dB by varying V_ctrl.</p>

<p><strong>Linearization</strong>:</p>

<p>To improve linearity, one can use:</p>
<ul>
<li>Linearization diodes (included in the LM13700)</li>
<li>Emitter resistors</li>
<li>Feedback</li>
</ul>

<p><strong>Applications</strong>:</p>

<table>
<tr><th>Application</th><th>Description</th></tr>
<tr><td>Audio mixer</td><td>Level control for each channel</td></tr>
<tr><td>AGC</td><td>Automatic gain adjustment</td></tr>
<tr><td>Compressor/limiter</td><td>Dynamic audio processing</td></tr>
<tr><td>Amplitude modulator</td><td>Signal multiplication</td></tr>
</table>

<h3 class="section-title">3. Voltage-controlled filters</h3>

<p><strong>Voltage-controlled first-order low-pass filter</strong>:</p>

<p><strong>Principle</strong>:</p>
<p>Use an OTA to create a variable equivalent resistance.</p>

<p><strong>Transfer function</strong>:</p>

<p>H(jw) = 1 / (1 + jw / wc)</p>

<p>where wc = 2pi fc (cutoff angular frequency)</p>

<p><strong>Voltage-controlled cutoff frequency</strong>:</p>

<p>Using an OTA, fc can be varied proportionally to the control voltage.</p>

<p>fc = gm / (2pi C) = (19.2 x I_abc) / (2pi C)</p>

<p>If I_abc = V_ctrl / R_ctrl:</p>

<p>fc = (19.2 x V_ctrl) / (2pi C x R_ctrl)</p>

<p><strong>Frequency range</strong>:</p>

<p>Typically from a few Hz to several tens of kHz depending on V_ctrl.</p>

<p><strong>Second-order low-pass filter (controlled Sallen-Key)</strong>:</p>

<p>By cascading two first-order cells or using a Sallen-Key structure with OTA.</p>

<p>Better selectivity (-40 dB/decade).</p>

<p><strong>Applications</strong>:</p>

<table>
<tr><th>Application</th><th>Description</th></tr>
<tr><td>Parametric equalizer</td><td>Cutoff frequency adjustment</td></tr>
<tr><td>Adaptive anti-aliasing filter</td><td>Adjusted according to sampling frequency</td></tr>
<tr><td>Audio synthesizer</td><td>VCF filter for subtractive synthesis</td></tr>
<tr><td>Adaptive processing</td><td>Filtering based on signal content</td></tr>
</table>

<h3 class="section-title">4. Modulators</h3>

<p><strong>Definition</strong>:</p>

<p>A circuit that performs the multiplication of two signals.</p>

<p><strong>Amplitude modulation</strong>:</p>

<p>s(t) = [A + m(t)] x cos(wp t)</p>

<p>where m(t) is the modulating signal, cos(wp t) the carrier.</p>

<p><strong>Implementation with OTA</strong>:</p>

<p>The OTA can serve as a multiplier because:</p>
<p>I_output = gm x V_input</p>

<p>If gm is proportional to a signal (via I_abc), multiplication is obtained.</p>

<p><strong>Modulator circuit</strong>:</p>

<p><strong>Inputs</strong>:</p>
<ul>
<li>Carrier signal: applied to the OTA input</li>
<li>Modulating signal: controls the transconductance gm (via I_abc)</li>
</ul>

<p><strong>Output</strong>:</p>
<p>Amplitude-modulated signal.</p>

<p><strong>Ring modulator</strong>:</p>

<p>Uses 4 OTAs or bridge diodes to achieve exact multiplication.</p>

<p>Output: s(t) = m1(t) x m2(t)</p>

<p><strong>Applications</strong>:</p>
<ul>
<li>AM modulation</li>
<li>Frequency mixer (heterodyning)</li>
<li>Audio effects (tremolo, chorus)</li>
<li>Synchronous demodulation</li>
</ul>

<h3 class="section-title">5. Conditioning circuits</h3>

<p><strong>Sensor conditioning</strong>:</p>

<p>Signals from sensors often require processing before digitization.</p>

<p><strong>Typical steps</strong>:</p>

<ol>
<li><strong>Amplification</strong>: VCA to adapt the level</li>
<li><strong>Filtering</strong>: Remove noise and unwanted frequencies</li>
<li><strong>Offset</strong>: Adjust the DC level</li>
<li><strong>Protection</strong>: Clipping, limiting</li>
</ol>

<p><strong>Instrumentation amplifier</strong>:</p>

<p>A specialized circuit for amplifying low-amplitude differential signals.</p>

<p><strong>Characteristics</strong>:</p>
<ul>
<li>Very high input impedance</li>
<li>Precise and stable gain</li>
<li>High CMRR (&gt; 100 dB)</li>
<li>Low noise</li>
</ul>

<p><strong>Applications</strong>:</p>
<ul>
<li>Strain gauges</li>
<li>Thermocouples</li>
<li>Wheatstone bridges</li>
<li>Biomedical measurements (ECG, EMG)</li>
</ul>

<p><strong>Anti-aliasing filter</strong>:</p>

<p>A low-pass filter placed before an ADC to prevent spectral folding (aliasing).</p>

<p><strong>Rule</strong>:</p>
<p>fc &lt; fs / 2 (sampling frequency / 2)</p>

<p>Typically: fc = 0.4 x fs</p>

<h3 class="section-title">6. Automatic gain control (AGC)</h3>

<p><strong>Principle</strong>:</p>

<p>A circuit that automatically adjusts the gain to maintain a constant output level despite input variations.</p>

<p><strong>Control loop</strong>:</p>

<ol>
<li><strong>Amplitude detector</strong>: Measures the output level (peak or RMS detector)</li>
<li><strong>Comparator</strong>: Compares to the reference level</li>
<li><strong>Integrator</strong>: Filters the error voltage (response time)</li>
<li><strong>VCA</strong>: Adjusts the gain according to the control voltage</li>
</ol>

<p><strong>Parameters</strong>:</p>

<ul>
<li><strong>Attack time</strong>: Speed of gain reduction (strong signal)</li>
<li><strong>Release time</strong>: Speed of gain increase (weak signal)</li>
<li><strong>Threshold</strong>: Level at which the AGC activates</li>
</ul>

<p><strong>Applications</strong>:</p>

<table>
<tr><th>Application</th><th>Description</th></tr>
<tr><td>Radio receivers</td><td>Maintain constant volume</td></tr>
<tr><td>Telephony</td><td>Voice level normalization</td></tr>
<tr><td>Audio recording</td><td>Prevent saturation</td></tr>
<tr><td>Instrumentation</td><td>Adapt signal dynamic range</td></tr>
</table>

<h3 class="section-title">7. Simulation techniques</h3>

<p><strong>TINA-TI</strong>:</p>

<p>Free analog simulation software from Texas Instruments.</p>

<p><strong>Features</strong>:</p>
<ul>
<li>Time-domain simulation (transient)</li>
<li>Frequency analysis (AC)</li>
<li>Noise analysis</li>
<li>Harmonic distortion analysis</li>
<li>Sensitivity analysis</li>
</ul>

<p><strong>Methodology</strong>:</p>

<ol>
<li><strong>Schematic</strong>: Draw the circuit</li>
<li><strong>Models</strong>: Use SPICE component models</li>
<li><strong>Simulation</strong>: Choose the analysis type</li>
<li><strong>Visualization</strong>: Response curves</li>
<li><strong>Optimization</strong>: Adjust values</li>
</ol>

<p><strong>Example: variable gain amplifier</strong></p>

<p>Simulation:</p>
<ul>
<li>AC analysis: frequency response for different control voltages</li>
<li>Transient analysis: response to a sinusoidal signal</li>
<li>Gain measurement in dB</li>
<li>Linearity verification</li>
</ul>

<h3 class="section-title">8. PCB design for analog circuits</h3>

<p><strong>Design rules</strong>:</p>

<p><strong>Critical layout</strong>:</p>

<table>
<tr><th>Aspect</th><th>Recommendation</th></tr>
<tr><td>Ground plane</td><td>Solid copper for GND</td></tr>
<tr><td>Decoupling</td><td>100 nF capacitor close to each power supply</td></tr>
<tr><td>Short traces</td><td>Minimize parasitic inductances</td></tr>
<tr><td>Analog/digital separation</td><td>Separate ground planes if mixed</td></tr>
<tr><td>Symmetry</td><td>Symmetric differential circuits</td></tr>
</table>

<p><strong>Power supply</strong>:</p>

<ul>
<li>Local decoupling: 100 nF ceramic + 10 uF electrolytic per IC</li>
<li>Wide power supply traces</li>
<li>Power supply filtering (ferrite, LC)</li>
</ul>

<p><strong>Sensitive signals</strong>:</p>

<ul>
<li>Short and protected input traces</li>
<li>Avoid ground loops</li>
<li>Guard ring around critical circuits</li>
</ul>

<p><strong>Components</strong>:</p>

<ul>
<li>Resistors: 1% precision or better for stable gain</li>
<li>Capacitors: COG/NP0 for precision circuits</li>
<li>Op-amps: choose based on bandwidth, noise, offset</li>
</ul>

<h3 class="section-title">9. Altium Designer for the project</h3>

<p><strong>BE_Archi_Sys_Emb project</strong>:</p>

<p>Project structure:</p>
<ul>
<li>Project file: BE_Archi_Sys_Emb.PrjPcb</li>
<li>Schematic: Modulateur.SchDoc</li>
<li>Libraries: 4AE_LM.SCHLIB, LIB_V2.SCHLIB</li>
<li>Footprints: ACT.PcbLib, PRINT_V2.PcbLib</li>
</ul>

<p><strong>Design steps</strong>:</p>

<ol>
<li><strong>Library creation</strong>:
<ul>
<li>Schematic symbols (LM13700, resistors, capacitors)</li>
<li>PCB footprints (DIP8, SMD 0805)</li>
</ul></li>

<li><strong>Electrical schematic</strong>:
<ul>
<li>Component placement</li>
<li>Connections (nets)</li>
<li>Annotations (values, references)</li>
<li>ERC verifications</li>
</ul></li>

<li><strong>PCB</strong>:
<ul>
<li>Schematic import</li>
<li>Component placement</li>
<li>Manual or automatic routing</li>
<li>DRC verifications</li>
<li>Ground and power planes</li>
</ul></li>

<li><strong>File generation</strong>:
<ul>
<li>Gerber (manufacturing)</li>
<li>BOM (bill of materials)</li>
<li>Assembly files</li>
</ul></li>
</ol>

<h3 class="section-title">10. Practical applications</h3>

<p><strong>Audio mixing console</strong>:</p>

<p>Each channel has a VCA to control volume. Faders adjust the control voltage.</p>

<p><strong>Analog synthesizer</strong>:</p>

<ul>
<li>VCO (Voltage Controlled Oscillator): variable frequency</li>
<li>VCF (Voltage Controlled Filter): filter with variable fc</li>
<li>VCA: amplitude envelope (ADSR)</li>
</ul>

<p><strong>Audio compressor</strong>:</p>

<p>AGC circuit with RMS detector and adjustable attack/release parameters.</p>

<p>Reduces the signal dynamic range (range between the weakest and the strongest).</p>

<p><strong>Parametric equalizer</strong>:</p>

<p>Multiple bandpass filters with controlled center frequency, gain, and Q factor.</p>

<p><strong>Adaptive radio receiver</strong>:</p>

<p>AGC to maintain a constant level despite variation in the received RF signal.</p>
<p>IF filters with variable bandwidth depending on reception conditions.</p>

<hr/>

<h2>PART D - Reflective Analysis and Perspectives</h2>

<h3 class="section-title">Skills acquired</h3>

<p><strong>Controlled circuit design</strong>:</p>
<p>Mastery of amplifiers and filters with electronically variable parameters. Ability to use OTAs to create reconfigurable circuits.</p>

<p><strong>Analog simulation</strong>:</p>
<p>Effective use of TINA-TI to validate circuits before fabrication. Understanding of AC, transient, and noise analyses.</p>

<p><strong>Professional PCB design</strong>:</p>
<p>Complete PCB realization in Altium Designer: library creation, schematic, routing, verifications.</p>

<h3 class="section-title">Key takeaways</h3>

<p><strong>1. OTA = versatile component</strong>:</p>
<p>The transconductance amplifier (LM13700) allows creating VCAs, VCFs, and modulators simply by exploiting gm control.</p>

<p><strong>2. Linearity vs dynamic range</strong>:</p>
<p>Controlled circuits often present a trade-off between linearity and variation range. Linearization is important.</p>

<p><strong>3. Stability is essential</strong>:</p>
<p>Variable gain circuits can oscillate if poorly compensated. Stabilization capacitors are critical.</p>

<p><strong>4. Layout = performance</strong>:</p>
<p>For precise analog circuits, PCB layout is as important as the schematic. Ground plane, decoupling, symmetry.</p>

<p><strong>5. Simulation = time saving</strong>:</p>
<p>Simulating before building avoids costly errors (PCBs to redo, burnt components).</p>

<h3 class="section-title">Practical applications</h3>

<p><strong>Professional audio</strong>:</p>
<p>Mixers, compressors, equalizers, and effects make extensive use of VCAs and VCFs.</p>

<p><strong>Instrumentation</strong>:</p>
<p>Programmable gain amplifiers to automatically adapt to the measured signal range.</p>

<p><strong>Telecommunications</strong>:</p>
<p>AGC in all radio receivers (AM, FM, GSM, WiFi, etc.).</p>

<p><strong>Embedded systems</strong>:</p>
<p>Adaptive sensor signal conditioning based on conditions.</p>

<h3 class="section-title">Feedback</h3>

<p><strong>Complete and educational project</strong>:</p>
<p>The lab study covers all stages of a real project: specifications, design, simulation, PCB, verifications.</p>

<p><strong>Interesting LM13700</strong>:</p>
<p>A vintage but still pedagogically relevant component. Modern OTAs (OPA860, etc.) use the same principles.</p>

<p><strong>Useful TINA simulations</strong>:</p>
<p>Simulations allow immediate visualization of the effect of parameter changes (resistors, capacitors).</p>

<p><strong>Professional Altium Designer</strong>:</p>
<p>A tool used in industry. A valuable skill for professional work.</p>

<h3 class="section-title">Limitations and perspectives</h3>

<p><strong>Module limitations</strong>:</p>
<ul>
<li>No physical fabrication and testing of the PCB</li>
<li>Classical analog components (digital alternatives not covered)</li>
<li>Noise and distortion aspects not deeply explored</li>
</ul>

<p><strong>Perspectives towards</strong>:</p>
<ul>
<li><strong>DSP (Digital Signal Processing)</strong>: digital alternative to analog circuits</li>
<li><strong>Mixed systems</strong>: ADC, DAC, analog-to-digital conversion</li>
<li><strong>Digital audio</strong>: codecs, digital effects</li>
<li><strong>Digital control of analog circuits</strong>: digital potentiometers, DAC for control</li>
<li><strong>Mixed SoCs</strong>: analog-digital integration on chip</li>
</ul>

<h3 class="section-title">Technological evolution</h3>

<p><strong>Current trends</strong>:</p>

<p><strong>Programmable circuits</strong>:</p>
<ul>
<li>FPAA (Field Programmable Analog Array): analog equivalent of FPGAs</li>
<li>Digital potentiometers controlled via SPI/I2C</li>
<li>Integrated VGA (Variable Gain Amplifier) with digital control</li>
</ul>

<p><strong>Integration</strong>:</p>
<ul>
<li>AFE (Analog Front-End) integrating complete conditioning</li>
<li>Integrated audio codecs (ADC + DAC + VCA + filters)</li>
<li>SoC with reconfigurable analog section</li>
</ul>

<p><strong>Performance</strong>:</p>
<ul>
<li>Very low noise (&lt; 1 nV/sqrt(Hz))</li>
<li>Very low power consumption (nA quiescent current)</li>
<li>Wide dynamic range (&gt; 120 dB)</li>
</ul>

<h3 class="section-title">Tips for success</h3>

<p><strong>1. Understand the LM13700</strong>:</p>
<p>Thoroughly grasp the principle of controlled transconductance. Read the datasheet carefully.</p>

<p><strong>2. Simulate systematically</strong>:</p>
<p>Each modification must be validated by simulation before proceeding further.</p>

<p><strong>3. Size carefully</strong>:</p>
<p>Resistor and capacitor values determine performance. Use the given formulas.</p>

<p><strong>4. Verify the PCB</strong>:</p>
<p>DRC/ERC are mandatory. An error on the PCB is costly (re-fabrication).</p>

<p><strong>5. Document</strong>:</p>
<p>Properly annotate schematics, calculate and note theoretical values for comparison with simulations.</p>

<h3 class="section-title">Conclusion</h3>

<p>This module provides an excellent introduction to reconfigurable and controlled analog circuits. Mastering VCAs, VCFs, and modulators is essential for many applications (audio, instrumentation, telecommunications).</p>

<p><strong>Project approach</strong>:</p>
<p>The lab study with complete design (simulation + PCB) reflects well the work of an electronic engineer. All stages of a real project are covered.</p>

<p><strong>Transferable skills</strong>:</p>
<ul>
<li>Complex analog circuit design</li>
<li>Simulation with professional tools (TINA, SPICE)</li>
<li>PCB design with Altium Designer</li>
<li>Complete electronic project management</li>
</ul>

<p><strong>Key message</strong>:</p>
<p>Voltage-controlled circuits bring flexibility and adaptability to analog systems. They allow creating intelligent systems capable of automatically adapting to conditions (AGC, adaptive filtering).</p>

<p><strong>Recommendations</strong>:</p>
<ul>
<li>Experiment with evaluation kits (Texas Instruments, Analog Devices)</li>
<li>Physically fabricate and test the designed PCB</li>
<li>Explore digital alternatives (DSP) for comparison</li>
<li>Deepen noise, distortion, and linearity aspects</li>
</ul>

<p><strong>Links to other courses</strong>:</p>
<ul>
<li><a href="./electronique-fonctions-analogiques.html">Analog Functions Electronics - S6</a>: Op-amps, active filters</li>
<li><a href="./projet-pcb.html">PCB Project - S6</a>: board design</li>
<li><a href="./architectures-analogiques-transmission.html">Analog Architectures for Transmission - S7</a>: modulation, RF</li>
</ul>

<hr/>

<h2>Course Documents</h2>

<!-- Shared PDF sections above -->

<hr/>

<p><em>Course taken in 2023-2024 at INSA Toulouse, Department of Electrical and Computer Engineering.</em></p>

</div>

<div class="back-nav">
    <a href="./my-courses-2023-2024.html" data-i18n-html="back-courses-2023-2024">&larr; Retour aux Cours 2023-2024</a>
</div>

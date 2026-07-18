---
layout: default
title:  "Innovative Project"
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

footer {
    display: flex;
    justify-content: space-around;
    margin-top: 20px;
}

.footer-section {
    flex: 1;
    text-align: center;
}

.styled-button {
    display: inline-block;
    width: 100px;
    margin: 10px;
    padding: 15px 30px;
    font-size: 16px;
    color: white;
    background-color: #66B2FF;
    text-decoration: none;
    border-radius: 25px;
    transition: background-color 0.3s, transform 0.3s;
}

.styled-button:hover {
    background-color: #3399FF;
    transform: scale(1.05);
}

p {
    text-align: justify;
}
</style>

<div class="back-nav">
    <a href="./my-courses-2024-2025.html" data-i18n-html="back-courses-2024-2025">&larr; Retour aux Cours 2024-2025</a>
</div>

<div class="lang-fr">

<h1>Projet Innovant (Innovative Project) - Semestre 9</h1>

<p><strong>Annee academique</strong> : 2024-2025<br>
<strong>Semestre</strong> : S9 - INSA Toulouse, parcours ISS (Innovative Smart Systems)<br>
<strong>Projet</strong> : What-A-Leak - Systeme de detection de fuites d'eau</p>

<hr>

<h2>PART A - Presentation Generale</h2>

<h3 class="section-title">Objectifs du projet</h3>

<p>Le Projet Innovant (Innovative Project) est le projet phare du semestre 9 du parcours ISS a l'INSA Toulouse. Il s'agit d'un projet multidisciplinaire de grande envergure visant a concevoir un prototype fonctionnel repondant a une problematique reelle. Notre projet, intitule <strong>"What-A-Leak"</strong>, avait pour objectif de developper un systeme intelligent de detection de fuites d'eau dans les reseaux de canalisations, en utilisant une approche non intrusive basee sur des capteurs vibratoires.</p>

<p><strong>Problematique</strong> :</p>
<p>Les fuites d'eau representent un enjeu majeur tant au niveau domestique qu'au niveau des infrastructures publiques. Les methodes de detection traditionnelles sont souvent intrusives, couteuses et necessitent une intervention humaine. Notre projet propose une solution connectee, autonome et securisee pour detecter les fuites en temps reel.</p>

<p><strong>Objectifs principaux</strong> :</p>
<ul>
<li>Concevoir un noeud capteur embarque capable de detecter des vibrations anormales dans les canalisations</li>
<li>Developper un protocole de communication securise pour la transmission des donnees</li>
<li>Creer une application mobile intuitive pour le suivi et la gestion des alertes</li>
<li>Realiser un boitier physique adapte via modelisation 3D et impression</li>
<li>Construire un prototype complet et fonctionnel, de l'acquisition de donnees a l'interface utilisateur</li>
</ul>

<h3 class="section-title">Organisation de l'equipe</h3>

<p>Notre equipe etait composee de <strong>cinq membres</strong>, chacun avec des responsabilites specifiques :</p>

<table>
<tr><th>Membre</th><th>Responsabilites principales</th></tr>
<tr><td>Moi-meme</td><td>Logiciel embarque, securite (AES), application mobile (React Native), modelisation 3D (CAD)</td></tr>
<tr><td>Collegue 1</td><td>Serveur backend, base de donnees, API</td></tr>
<tr><td>Collegue 2</td><td>Machine Learning, analyse des donnees vibratoires</td></tr>
<tr><td>Collegue 3</td><td>Site web de presentation, documentation</td></tr>
<tr><td>Collegue 4</td><td>Hardware, protocole LoRa, integration electronique</td></tr>
</table>

<h3 class="section-title">Chronologie et methodologie</h3>

<p>Le projet s'est deroule en <strong>4 sprints</strong> suivant une methodologie Agile :</p>

<table>
<tr><th>Sprint</th><th>Periode</th><th>Objectifs</th></tr>
<tr><td>Sprint 1</td><td>Debut du semestre</td><td>Definition du cahier des charges, choix des technologies, premieres maquettes</td></tr>
<tr><td>Sprint 2</td><td>Mi-semestre</td><td>Developpement des composants individuels (embarque, app, serveur)</td></tr>
<tr><td>Sprint 3</td><td>Fin de semestre - 1 mois</td><td>Integration des composants, premiers tests de bout en bout</td></tr>
<tr><td>Sprint 4</td><td>Dernier mois</td><td>Tests finaux, optimisation, preparation de la presentation</td></tr>
</table>

<p>Chaque sprint se terminait par une presentation devant les enseignants et les autres groupes, permettant de recevoir des retours et d'ajuster la direction du projet.</p>

<hr>

<h2>PART B - Experience et Contexte</h2>

<h3 class="section-title">Environnement et contexte</h3>

<p>Le projet s'est deroule dans un environnement collaboratif au sein du departement ISS de l'INSA Toulouse. Ce projet fait partie d'une initiative multidisciplinaire innovante ou les etudiants doivent mener un projet de A a Z, de l'idee initiale au prototype fonctionnel.</p>

<p>L'objectif initial etait de detecter les fuites d'eau dans les maisons. Cependant, au fur et a mesure de l'avancement du projet, la portee s'est elargie pour inclure une approche distribuee applicable aux infrastructures de reseaux d'eau publics. Cette evolution a permis de passer d'un cas d'usage domestique a un cas d'usage industriel, ajoutant de la complexite et de la pertinence au projet.</p>

<p>Le projet a offert une plateforme unique pour appliquer les connaissances theoriques acquises durant le cursus a des scenarios pratiques, favorisant l'innovation, la creativite et la gestion de projet.</p>

<h3 class="section-title">Outils et environnement de developpement</h3>

<p><strong>Partie embarquee</strong> :</p>
<ul>
<li><strong>Microcontroleur</strong> : ESP32 (framework ESP-IDF via le SDK Espressif)</li>
<li><strong>Capteur</strong> : Accelerometre pour la detection de vibrations</li>
<li><strong>Communication</strong> : Module LoRa pour la transmission longue portee</li>
<li><strong>IDE</strong> : VS Code avec extension ESP-IDF</li>
<li><strong>Langage</strong> : C (FreeRTOS)</li>
</ul>

<p><strong>Application mobile</strong> :</p>
<ul>
<li><strong>Framework</strong> : React Native avec Expo</li>
<li><strong>Langage</strong> : JavaScript</li>
<li><strong>Bibliotheques</strong> : React Navigation (navigation par onglets), react-native-vector-icons (icones), react-native-chart-kit (graphiques)</li>
<li><strong>Gestion de donnees</strong> : JSON synchronise avec le serveur</li>
</ul>

<p><strong>Modelisation 3D</strong> :</p>
<ul>
<li><strong>Logiciel</strong> : SolidWorks</li>
<li><strong>Fabrication</strong> : Impression 3D (PLA)</li>
<li><strong>Simulation</strong> : Analyse de contraintes mecaniques</li>
</ul>

<p><strong>Securite</strong> :</p>
<ul>
<li><strong>Algorithme</strong> : AES-128 en mode CBC</li>
<li><strong>Bibliotheque</strong> : TinyAES (tiny-AES-c)</li>
<li><strong>Cle</strong> : Pre-partagee, symetrique</li>
</ul>

<p><strong>Gestion de projet</strong> :</p>
<ul>
<li><strong>Versionning</strong> : Git / GitHub (organisation <a href="https://github.com/what-a-leak">what-a-leak</a>)</li>
<li><strong>Communication</strong> : Reunions hebdomadaires, presentations de sprint</li>
</ul>

<h3 class="section-title">Mon role dans le projet</h3>

<p>Dans ce projet, j'ai assume plusieurs responsabilites couvrant differents domaines techniques :</p>

<p><strong>1. Developpement du logiciel embarque</strong> :</p>
<ul>
<li>Programmation du microcontroleur ESP32 avec le framework ESP-IDF</li>
<li>Configuration et lecture de l'accelerometre pour l'acquisition des donnees vibratoires</li>
<li>Implementation de la collecte de metriques (vibration, son, batterie) pour la detection de fuites</li>
<li>Integration avec le module de communication LoRa</li>
</ul>

<p><strong>2. Securite des communications</strong> :</p>
<ul>
<li>Implementation du chiffrement AES-128 en mode CBC sur l'ESP32</li>
<li>Gestion des vecteurs d'initialisation (IV) avec partie aleatoire et statique</li>
<li>Padding PKCS#7 pour l'alignement des blocs de donnees</li>
<li>Tests de validation du chiffrement/dechiffrement de bout en bout</li>
</ul>

<p><strong>3. Application mobile</strong> :</p>
<ul>
<li>Developpement complet de l'application React Native avec Expo</li>
<li>Conception de l'architecture de navigation (Bottom Tab Navigator)</li>
<li>Creation des ecrans : accueil, tableau de bord, historique, fuites, statistiques</li>
<li>Integration des donnees provenant du serveur via fichiers JSON</li>
</ul>

<p><strong>4. Modelisation 3D (CAD)</strong> :</p>
<ul>
<li>Conception du boitier du capteur sous SolidWorks</li>
<li>Prise en compte des contraintes d'assemblage et de la taille des composants electroniques</li>
<li>Simulation mecanique pour valider la robustesse du design</li>
<li>Iteration avec impression 3D pour validation physique</li>
</ul>

<hr>

<h2>PART C - Aspects Techniques</h2>

<h3 class="section-title">Architecture globale du systeme</h3>

<p>Le systeme "What-A-Leak" repose sur une architecture distribuee composee de plusieurs couches :</p>

<p><strong>1. Couche capteur (Noeud)</strong> : Chaque noeud est un dispositif autonome equipe d'un ESP32, d'un accelerometre et d'un module LoRa. Il collecte les donnees vibratoires et les transmet de maniere securisee.</p>

<p><strong>2. Couche communication</strong> : Les donnees sont chiffrees en AES-128 CBC et transmises via LoRa vers une passerelle (gateway). Ce choix de LoRa permet une portee de plusieurs kilometres avec une faible consommation energetique.</p>

<p><strong>3. Couche serveur</strong> : Un serveur centralise les donnees, les stocke dans une base de donnees, et les met a disposition via une API REST.</p>

<p><strong>4. Couche application</strong> : L'application mobile React Native permet aux utilisateurs de surveiller l'etat des noeuds, visualiser les statistiques de consommation et recevoir des alertes en cas de fuite.</p>

<p><strong>5. Couche intelligence</strong> : Un module de Machine Learning analyse les donnees vibratoires pour distinguer les vibrations normales des signatures de fuites.</p>

<p>Le flux de donnees complet est le suivant :</p>

<p>Capteur (accelerometre) --> ESP32 (traitement + chiffrement AES) --> LoRa --> Gateway --> Serveur (API + BDD) --> Application mobile</p>

<hr>

<h3 class="section-title">1. Partie embarquee - ESP32 et acquisition de donnees</h3>

<p>Le coeur du systeme repose sur le microcontroleur <strong>ESP32</strong>, programme avec le framework <strong>ESP-IDF</strong> (Espressif IoT Development Framework) base sur <strong>FreeRTOS</strong>. Le choix de l'ESP32 s'est impose pour plusieurs raisons :</p>
<ul>
<li>Double coeur permettant de gerer simultanement l'acquisition de donnees et la communication</li>
<li>Support natif du WiFi et du Bluetooth (utile pour la configuration initiale)</li>
<li>Faible consommation energetique avec modes de veille profonde</li>
<li>Large ecosysteme de bibliotheques et de documentation</li>
<li>Compatible avec les modules LoRa pour la communication longue portee</li>
</ul>

<p><strong>Acquisition de donnees</strong> :</p>
<p>L'accelerometre est interface avec l'ESP32 via le bus I2C ou SPI. Le logiciel embarque realise les etapes suivantes :</p>
<ol>
<li>Initialisation du peripherique accelerometre</li>
<li>Lecture periodique des valeurs d'acceleration sur les 3 axes (X, Y, Z)</li>
<li>Pre-traitement des donnees (filtrage, calcul de la magnitude)</li>
<li>Empaquetage des metriques (vibration, niveau sonore, batterie, statut de fuite)</li>
<li>Chiffrement des donnees via AES-128 CBC</li>
<li>Transmission via le module LoRa</li>
</ol>

<p>La structure de donnees transmise par chaque noeud contient :</p>

<table>
<tr><th>Champ</th><th>Description</th><th>Type</th></tr>
<tr><td>NodeID</td><td>Identifiant unique du noeud</td><td>Entier</td></tr>
<tr><td>MesureCapteur</td><td>Valeur de mesure du capteur</td><td>Flottant</td></tr>
<tr><td>Status</td><td>Etat de fuite (0 = normal, 1 = fuite)</td><td>Booleen</td></tr>
<tr><td>TimeStamp</td><td>Horodatage de la mesure</td><td>Date/heure</td></tr>
<tr><td>Batterie</td><td>Niveau de batterie en pourcentage</td><td>Entier</td></tr>
<tr><td>Temperature</td><td>Temperature ambiante (optionnel)</td><td>Flottant</td></tr>
</table>

<hr>

<h3 class="section-title">2. Developpement de l'application mobile</h3>

<p>Nous avons choisi <strong>React Native</strong> avec <strong>Expo</strong> pour developper notre application mobile en raison de leur efficacite pour le developpement multiplateforme. React Native permet d'ecrire du code JavaScript qui se compile en code natif pour iOS et Android, reduisant le temps de developpement et les efforts de maintenance. Expo simplifie le processus de configuration et fournit un acces aux API natives.</p>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Innovative_Project/app_workspace.png" style="width: 20%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure : Structure du workspace de l'application mobile
</p>

<p><strong>Architecture de l'application</strong> :</p>

<p>L'application est structuree en plusieurs repertoires et fichiers :</p>
<ul>
<li><strong>assets/</strong> : Ressources statiques (images, icones, logo, splash screen)</li>
<li><strong>Config/</strong> : Gestion des donnees des noeuds incluant les niveaux de batterie, les mesures de vibration et de son, et le statut de fuite (fichiers JSON synchronises avec le serveur)</li>
<li><strong>Screen/</strong> : Les ecrans principaux de l'application</li>
<li><strong>App.js</strong> : Point d'entree gerant l'ecran d'accueil et la navigation</li>
<li><strong>app.json</strong> : Metadonnees de configuration de l'application</li>
</ul>

<p><strong>Systeme de navigation</strong> :</p>

<p>L'application utilise un <strong>Bottom Tab Navigator</strong> (react-navigation) avec une barre de navigation au theme violet (#6A0DAB). Les ecrans accessibles depuis la barre de navigation sont :</p>
<ul>
<li>Historique (icone "history")</li>
<li>Tableau de bord (icone "tint")</li>
<li>Statistiques (icone "bar-chart")</li>
<li>Alertes de fuites (icone "exclamation-triangle")</li>
</ul>

<p>L'ecran d'accueil (HomeScreen) est affiche en plein ecran sans barre de navigation, et les pages de detail des noeuds (NodeInfo) sont accessibles depuis le tableau de bord.</p>

<p><strong>Ecrans et fonctionnalites detaillees</strong> :</p>

<ul>
<li><strong>WelcomeScreen</strong> : Ecran de demarrage affichant un message de bienvenue et le logo de l'application pendant 1 seconde avant de rediriger vers l'ecran d'accueil.</li>
<li><strong>HomeScreen</strong> : Point d'entree principal avec options de connexion et branding de l'application.</li>
<li><strong>DashboardScreen</strong> : Vue d'ensemble de tous les noeuds avec indicateurs visuels (vert = normal, rouge = fuite), niveaux de batterie, et statut global de detection de fuite. Inclut egalement un graphique de statistiques hebdomadaires.</li>
<li><strong>HistoricScreen</strong> : Historique des activites des noeuds et positions sur une carte geographique, permettant de suivre l'evolution des mesures dans le temps.</li>
<li><strong>LeakScreen</strong> : Historique des fuites detectees avec details (localisation, horodatage, severite) et options de contact pour signaler ou intervenir.</li>
<li><strong>StatisticsScreen</strong> : Statistiques detaillees de consommation d'eau avec graphiques hebdomadaires et mensuels.</li>
<li><strong>NodeInfo</strong> : Page de detail d'un noeud individuel avec toutes ses metriques.</li>
</ul>

<div style="text-align: center; display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
    <img src="/img/BE_Innovative_Project/HomeScreen.png" style="width: 18%;"/>
    <img src="/img/BE_Innovative_Project/DashboardScreen.png" style="width: 18%;"/>
    <img src="/img/BE_Innovative_Project/HistoricScreen.png" style="width: 18%;"/>
    <img src="/img/BE_Innovative_Project/LeakScreen.png" style="width: 18%;"/>
    <img src="/img/BE_Innovative_Project/StatisticsScreen.png" style="width: 18%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure : Captures d'ecran de l'application - HomeScreen, DashboardScreen, HistoricScreen, LeakScreen, StatisticsScreen
</p>

<p>L'application lit les donnees depuis un fichier JSON dans le repertoire Config, synchronise avec le serveur pour les mises a jour en temps reel. Les evolutions futures incluent un traitement de donnees ameliore, des notifications en temps reel, une authentification utilisateur et des analyses avancees pour une meilleure comprehension de la consommation d'eau.</p>

<hr>

<h3 class="section-title">3. Modelisation 3D (CAD)</h3>

<p>Nous avons utilise <strong>SolidWorks</strong> pour concevoir le modele mecanique du boitier du capteur. Le choix de SolidWorks s'est impose pour ses fonctionnalites robustes de conception parametrique et son interface intuitive.</p>

<p><strong>Cahier des charges du boitier</strong> :</p>
<ul>
<li>Loger la carte electronique (ESP32 + accelerometre + module LoRa + batterie)</li>
<li>Prevoir des ouvertures pour les connecteurs et les capteurs</li>
<li>Assurer un contact direct entre le capteur sonore et la canalisation (essentiel pour la precision de la detection)</li>
<li>Garantir une fixation solide a la canalisation sans vibrations parasites</li>
<li>Permettre l'ouverture pour la maintenance (remplacement de batterie, mise a jour firmware)</li>
</ul>

<p><strong>Conception du boitier</strong> :</p>
<ul>
<li>Un espace dedie au capteur sonore assure le contact direct avec la canalisation</li>
<li>Des trous de vis securisent le boitier et la carte electronique, evitant les fausses lectures de vibrations</li>
<li>Les dimensions sont optimisees pour minimiser l'encombrement tout en assurant un assemblage aise</li>
</ul>

<div style="text-align: center; display: flex; justify-content: center; gap: 60px; flex-wrap: wrap;">
    <img src="/img/BE_Innovative_Project/Assembly.png" style="width: 30%;"/>
    <img src="/img/BE_Innovative_Project/3D_Model.png" style="width: 40%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure : Vue d'assemblage et modele 3D du boitier du capteur
</p>

<p><strong>Simulation et validation</strong> :</p>
<p>Des simulations de contraintes mecaniques ont ete realisees sous SolidWorks pour verifier la resistance du boitier aux efforts de serrage et aux vibrations environnantes. Le processus de validation a inclus :</p>
<ul>
<li>Analyse de contraintes (Von Mises) pour identifier les zones de faiblesse</li>
<li>Verification des deformations sous charge</li>
<li>Impression 3D iterative pour valider l'ergonomie et l'assemblage</li>
<li>Tests de fixation sur differents diametres de canalisations</li>
</ul>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Innovative_Project/simulation.png" style="width: 40%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure : Simulation de contraintes mecaniques du boitier
</p>

<hr>

<h3 class="section-title">4. Securite des communications - Chiffrement AES</h3>

<p><strong>Problematique de securite</strong> :</p>

<p>Notre projet implique un reseau distribue de capteurs (ESP32 + module LoRa) qui transmettent des metriques et des resultats d'analyse preliminaire. Sans mecanisme de securite, le systeme est vulnerable a plusieurs types d'attaques :</p>
<ul>
<li><strong>Attaque par rejeu (replay)</strong> : Un attaquant intercepte et retransmet des messages legitimes pour provoquer de fausses alertes</li>
<li><strong>Alteration des donnees (tampering)</strong> : Modification des mesures en transit pour masquer une fuite reelle</li>
<li><strong>Ecoute passive (eavesdropping)</strong> : Interception des donnees pour obtenir des informations sur l'infrastructure du reseau d'eau</li>
</ul>

<p><strong>Solution implementee</strong> :</p>

<p>Nous avons mis en place un mecanisme de securite leger mais efficace utilisant le <strong>chiffrement AES-128</strong> avec la bibliotheque <strong>TinyAES</strong> (<a href="https://github.com/kokke/tiny-AES-c">tiny-AES-c</a>) et des <strong>cles symetriques pre-partagees</strong>. Chaque capteur chiffre ses donnees en mode <strong>CBC (Cipher Block Chaining)</strong>, utilisant un <strong>vecteur d'initialisation (IV)</strong> unique pour chaque message.</p>

<p><strong>Details techniques</strong> :</p>

<ul>
<li><strong>AES-128</strong> : Algorithme de chiffrement symetrique utilisant une cle de 128 bits pour chiffrer et dechiffrer les donnees. Choisi pour son excellent rapport securite/performance, particulierement adapte aux microcontroleurs a ressources limitees.</li>
<li><strong>Mode CBC (Cipher Block Chaining)</strong> : Mode d'operation pour les chiffrements par blocs qui utilise un mecanisme de chainage. Chaque bloc de texte clair est XORe avec le bloc chiffre precedent avant d'etre chiffre, garantissant que des blocs de texte clair identiques produisent des blocs chiffres differents.</li>
<li><strong>Vecteur d'Initialisation (IV)</strong> : Valeur aleatoire ou pseudo-aleatoire utilisee pour initialiser le processus de chiffrement. Dans notre implementation, pour equilibrer securite et efficacite de transmission :
  <ul>
  <li><strong>2 octets</strong> sont generes aleatoirement a chaque message (transmis avec le message)</li>
  <li><strong>14 octets</strong> sont statiques (pre-partages entre le capteur et le serveur)</li>
  <li>Cette approche reduit la surcharge de communication tout en maintenant une entropie suffisante</li>
  </ul>
</li>
<li><strong>Padding PKCS#7</strong> : Schema de remplissage utilise pour assurer que la longueur du texte clair est un multiple de la taille du bloc (16 octets pour AES). PKCS#7 ajoute une serie d'octets dont la valeur est egale au nombre d'octets de remplissage ajoutes.</li>
</ul>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Innovative_Project/secu.png" style="width: 100%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure : Architecture de securite du systeme - flux de chiffrement et dechiffrement
</p>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Innovative_Project/aes_encrypt.png" style="width: 90%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure : Detail du processus de chiffrement AES-128 CBC avec IV partiel
</p>

<p><strong>Choix de conception pour l'embarque</strong> :</p>
<ul>
<li>TinyAES est une implementation ultra-legere d'AES (quelques Ko de Flash) compatible avec les contraintes memoire de l'ESP32</li>
<li>Le mode CBC a ete prefere au mode ECB car ce dernier ne masque pas les motifs dans les donnees</li>
<li>La cle pre-partagee evite la complexite d'un echange de cles (type Diffie-Hellman) inadapte a un microcontroleur</li>
</ul>

<hr>

<h3 class="section-title">5. Protocole de communication LoRa</h3>

<p><strong>Choix de LoRa</strong> :</p>

<p>LoRa (Long Range) a ete selectionne comme protocole de communication sans fil pour plusieurs raisons :</p>
<ul>
<li><strong>Portee</strong> : Plusieurs kilometres en milieu urbain, jusqu'a 15 km en champ libre</li>
<li><strong>Faible consommation</strong> : Compatible avec un fonctionnement sur batterie pendant plusieurs mois</li>
<li><strong>Penetration</strong> : Bonne penetration des obstacles (murs, sous-sol)</li>
<li><strong>Bande ISM</strong> : Utilisation de la bande ISM (868 MHz en Europe) sans licence</li>
</ul>

<p><strong>Integration avec l'ESP32</strong> :</p>
<p>Le module LoRa est connecte a l'ESP32 via l'interface SPI. Le firmware gere :</p>
<ul>
<li>La configuration des parametres radio (frequence, spreading factor, bande passante)</li>
<li>L'envoi des paquets chiffres a intervalles reguliers</li>
<li>La gestion de la consommation (mode veille entre les transmissions)</li>
<li>La detection d'erreurs de transmission</li>
</ul>

<hr>

<h2>PART D - Analyse et Reflexion</h2>

<h3 class="section-title">Competences acquises</h3>

<p>Ce projet m'a permis de developper et de consolider un large eventail de competences :</p>

<p><strong>Competences techniques</strong> :</p>
<ul>
<li>Analyser des problemes concrets et proposer des solutions technologiques adaptees</li>
<li>Developper du logiciel embarque pour microcontroleur (ESP32, FreeRTOS, ESP-IDF)</li>
<li>Implementer des mecanismes de securite (chiffrement AES) sur des systemes a ressources limitees</li>
<li>Creer des applications mobiles multiplateformes avec React Native et Expo</li>
<li>Concevoir des modeles 3D (CAD) avec SolidWorks et valider par simulation</li>
<li>Integrer des capteurs et des modules de communication dans un systeme embarque</li>
<li>Gerer un flux de donnees de bout en bout (capteur --> serveur --> application)</li>
</ul>

<p><strong>Competences transversales</strong> :</p>
<ul>
<li>Travailler en equipe sur un projet de grande envergure avec des sous-systemes interdependants</li>
<li>Presenter et debattre des choix techniques en anglais devant un jury</li>
<li>Rediger des rapports techniques complets en anglais</li>
<li>Appliquer une methodologie Agile (sprints, revues, retrospectives)</li>
<li>Gerer les priorites et les delais dans un projet avec de nombreux livrables</li>
</ul>

<h3 class="section-title">Auto-evaluation</h3>

<p>Ce projet a ete l'un des projets les plus avances de mon parcours. Mener un projet de zero jusqu'a un prototype fonctionnel, impliquant hardware, logiciel embarque, stockage de donnees, transmission de donnees, modelisation 3D, serveur, intelligence artificielle et interface applicative, c'etait un projet complet, un prototype pret a la commercialisation.</p>

<p>En raison de l'envergure du projet, je n'ai pas pu travailler sur tous les aspects, mais j'ai collabore etroitement avec mes collegues pour rester informe de chaque composant. Je suis fier de mes contributions, et le systeme est fonctionnel. Faire partie d'une equipe dediee ou chacun etait desireux d'apprendre de nouvelles choses a ete une experience tres enrichissante.</p>

<p>La partie qui m'a le plus challenge a ete l'implementation de la securite AES sur l'ESP32. Il a fallu comprendre en profondeur le fonctionnement du chiffrement par blocs, gerer les contraintes memoire du microcontroleur, et assurer la compatibilite du chiffrement entre l'ESP32 (C) et le serveur (Python/Node.js).</p>

<p>Le developpement de l'application mobile m'a permis de decouvrir React Native et l'ecosysteme JavaScript mobile. La creation d'une interface utilisateur intuitive avec navigation par onglets, graphiques et cartes a ete un apprentissage riche.</p>

<h3 class="section-title">Mon avis</h3>

<p>Ce projet a ete une excellente opportunite d'explorer differents domaines et de mener nos propres recherches sur la maniere de gerer le projet. A mon avis, l'organisation actuelle des sessions etait ideale pour livrer un prototype, mais pas suffisante pour livrer un produit final entierement fonctionnel avec toutes les fonctionnalites souhaitees.</p>

<p>J'ai decouvert comment integrer de nombreux concepts appris au cours de l'annee dans un projet reel, similaire a ce que l'on pourrait nous demander en entreprise. Ce projet a ete une experience formidable et je suis fier des resultats que nous avons obtenus.</p>

<p><strong>Points forts du projet</strong> :</p>
<ul>
<li>Prototype fonctionnel de bout en bout</li>
<li>Diversite des technologies maitrisees (embarque, mobile, 3D, securite)</li>
<li>Travail d'equipe efficace avec repartition claire des taches</li>
<li>Presentations regulieres favorisant la communication</li>
</ul>

<p><strong>Axes d'amelioration</strong> :</p>
<ul>
<li>Plus de temps pour l'integration et les tests systeme</li>
<li>Approfondir la partie Machine Learning pour la classification des vibrations</li>
<li>Implementer des notifications push en temps reel dans l'application</li>
<li>Ajouter une authentification utilisateur robuste</li>
</ul>

<h3 class="section-title">Gestion de projet et travail d'equipe</h3>

<p>La methodologie Agile avec des sprints de 3 a 4 semaines s'est revelee tres efficace pour ce type de projet. Les presentations de fin de sprint nous ont obliges a avoir des livrables concrets a chaque etape, evitant ainsi l'effet "tunnel" ou l'integration est repoussee a la fin.</p>

<p>La communication au sein de l'equipe a ete un facteur cle de reussite. Les reunions hebdomadaires permettaient de synchroniser les avancees, identifier les blocages et redistribuer les efforts si necessaire. L'utilisation de GitHub avec une organisation dediee a facilite la gestion du code et la collaboration.</p>

<hr>

<h2>Rapports et Projets</h2>

<div style="text-align: center;">
    <h3>
        <span class="lang-fr">Rapport de projet</span>
        <span class="lang-en">Project Report</span>
    </h3>
</div>

<p>Le code source complet du projet est disponible sur l'organisation GitHub : <a href="https://github.com/what-a-leak">What-A-Leak</a></p>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">Rapport du Projet Innovant ISS</span>
        <span class="lang-en">ISS Innovative Project Report</span>
      </h4>
      <p>
        <span class="lang-fr">Rapport complet du projet "What-A-Leak" detaillant la conception, l'implementation et les resultats du systeme de detection de fuites d'eau.</span>
        <span class="lang-en">Complete report of the "What-A-Leak" project detailing the design, implementation and results of the water leak detection system.</span>
      </p>
      <div class="pdf-lazy" data-src="/file/reports/S9/Rapport_Projet_ISS.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/file/reports/S9/Rapport_Projet_ISS.pdf" target="_blank">
        <span class="lang-fr">Telecharger le rapport</span>
        <span class="lang-en">Download the report</span>
      </a></p>
    </div>
  </div>
</div>

<div style="text-align: center;">
    <h3>
        <span class="lang-fr">Presentation finale</span>
        <span class="lang-en">Final Presentation</span>
    </h3>
</div>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">Presentation finale du projet</span>
        <span class="lang-en">Final Project Presentation</span>
      </h4>
      <p>
        <span class="lang-fr">Support de presentation utilise lors de la soutenance finale du projet devant le jury.</span>
        <span class="lang-en">Presentation slides used during the final project defense before the jury.</span>
      </p>
      <div class="pdf-lazy" data-src="/img/BE_Innovative_Project/Prez_final.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/img/BE_Innovative_Project/Prez_final.pdf" target="_blank">
        <span class="lang-fr">Telecharger la presentation</span>
        <span class="lang-en">Download the presentation</span>
      </a></p>
    </div>
  </div>
</div>

<hr>
<p><em>Projet realise en 2024-2025 a l'INSA Toulouse, Departement ISS (Innovative Smart Systems).</em></p>

</div>

<div class="lang-en">

<h1>Innovative Project - Semester 9</h1>

<p><strong>Academic year</strong>: 2024-2025<br>
<strong>Semester</strong>: S9 - INSA Toulouse, ISS track (Innovative Smart Systems)<br>
<strong>Project</strong>: What-A-Leak - Water leak detection system</p>

<hr>

<h2>PART A - General Presentation</h2>

<h3 class="section-title">Project objectives</h3>

<p>The Innovative Project is the flagship project of semester 9 in the ISS track at INSA Toulouse. It is a large-scale multidisciplinary project aimed at designing a functional prototype addressing a real-world problem. Our project, entitled <strong>"What-A-Leak"</strong>, aimed to develop an intelligent water leak detection system in pipe networks, using a non-intrusive approach based on vibration sensors.</p>

<p><strong>Problem statement</strong>:</p>
<p>Water leaks represent a major challenge at both the domestic and public infrastructure levels. Traditional detection methods are often intrusive, costly and require human intervention. Our project proposes a connected, autonomous and secure solution to detect leaks in real time.</p>

<p><strong>Main objectives</strong>:</p>
<ul>
<li>Design an embedded sensor node capable of detecting abnormal vibrations in pipes</li>
<li>Develop a secure communication protocol for data transmission</li>
<li>Create an intuitive mobile application for monitoring and alert management</li>
<li>Produce a suitable physical enclosure through 3D modeling and printing</li>
<li>Build a complete and functional prototype, from data acquisition to user interface</li>
</ul>

<h3 class="section-title">Team organization</h3>

<p>Our team consisted of <strong>five members</strong>, each with specific responsibilities:</p>

<table>
<tr><th>Member</th><th>Main responsibilities</th></tr>
<tr><td>Myself</td><td>Embedded software, security (AES), mobile application (React Native), 3D modeling (CAD)</td></tr>
<tr><td>Colleague 1</td><td>Backend server, database, API</td></tr>
<tr><td>Colleague 2</td><td>Machine Learning, vibration data analysis</td></tr>
<tr><td>Colleague 3</td><td>Presentation website, documentation</td></tr>
<tr><td>Colleague 4</td><td>Hardware, LoRa protocol, electronic integration</td></tr>
</table>

<h3 class="section-title">Timeline and methodology</h3>

<p>The project was carried out in <strong>4 sprints</strong> following an Agile methodology:</p>

<table>
<tr><th>Sprint</th><th>Period</th><th>Objectives</th></tr>
<tr><td>Sprint 1</td><td>Beginning of semester</td><td>Requirements definition, technology selection, first mockups</td></tr>
<tr><td>Sprint 2</td><td>Mid-semester</td><td>Development of individual components (embedded, app, server)</td></tr>
<tr><td>Sprint 3</td><td>End of semester - 1 month</td><td>Component integration, first end-to-end tests</td></tr>
<tr><td>Sprint 4</td><td>Last month</td><td>Final tests, optimization, presentation preparation</td></tr>
</table>

<p>Each sprint ended with a presentation before the instructors and other groups, allowing for feedback and project direction adjustments.</p>

<hr>

<h2>PART B - Experience and Context</h2>

<h3 class="section-title">Environment and context</h3>

<p>The project took place in a collaborative environment within the ISS department at INSA Toulouse. This project is part of an innovative multidisciplinary initiative where students must lead a project from start to finish, from the initial idea to a functional prototype.</p>

<p>The initial objective was to detect water leaks in houses. However, as the project progressed, the scope expanded to include a distributed approach applicable to public water network infrastructures. This evolution enabled a shift from a domestic use case to an industrial use case, adding complexity and relevance to the project.</p>

<p>The project provided a unique platform for applying the theoretical knowledge acquired during the curriculum to practical scenarios, fostering innovation, creativity and project management.</p>

<h3 class="section-title">Tools and development environment</h3>

<p><strong>Embedded part</strong>:</p>
<ul>
<li><strong>Microcontroller</strong>: ESP32 (ESP-IDF framework via Espressif SDK)</li>
<li><strong>Sensor</strong>: Accelerometer for vibration detection</li>
<li><strong>Communication</strong>: LoRa module for long-range transmission</li>
<li><strong>IDE</strong>: VS Code with ESP-IDF extension</li>
<li><strong>Language</strong>: C (FreeRTOS)</li>
</ul>

<p><strong>Mobile application</strong>:</p>
<ul>
<li><strong>Framework</strong>: React Native with Expo</li>
<li><strong>Language</strong>: JavaScript</li>
<li><strong>Libraries</strong>: React Navigation (tab navigation), react-native-vector-icons (icons), react-native-chart-kit (charts)</li>
<li><strong>Data management</strong>: JSON synchronized with the server</li>
</ul>

<p><strong>3D modeling</strong>:</p>
<ul>
<li><strong>Software</strong>: SolidWorks</li>
<li><strong>Manufacturing</strong>: 3D printing (PLA)</li>
<li><strong>Simulation</strong>: Mechanical stress analysis</li>
</ul>

<p><strong>Security</strong>:</p>
<ul>
<li><strong>Algorithm</strong>: AES-128 in CBC mode</li>
<li><strong>Library</strong>: TinyAES (tiny-AES-c)</li>
<li><strong>Key</strong>: Pre-shared, symmetric</li>
</ul>

<p><strong>Project management</strong>:</p>
<ul>
<li><strong>Versioning</strong>: Git / GitHub (organization <a href="https://github.com/what-a-leak">what-a-leak</a>)</li>
<li><strong>Communication</strong>: Weekly meetings, sprint presentations</li>
</ul>

<h3 class="section-title">My role in the project</h3>

<p>In this project, I assumed several responsibilities covering various technical domains:</p>

<p><strong>1. Embedded software development</strong>:</p>
<ul>
<li>Programming the ESP32 microcontroller with the ESP-IDF framework</li>
<li>Configuring and reading the accelerometer for vibration data acquisition</li>
<li>Implementing metrics collection (vibration, sound, battery) for leak detection</li>
<li>Integration with the LoRa communication module</li>
</ul>

<p><strong>2. Communication security</strong>:</p>
<ul>
<li>Implementation of AES-128 encryption in CBC mode on the ESP32</li>
<li>Management of initialization vectors (IV) with random and static parts</li>
<li>PKCS#7 padding for data block alignment</li>
<li>End-to-end encryption/decryption validation testing</li>
</ul>

<p><strong>3. Mobile application</strong>:</p>
<ul>
<li>Complete development of the React Native application with Expo</li>
<li>Navigation architecture design (Bottom Tab Navigator)</li>
<li>Screen creation: home, dashboard, history, leaks, statistics</li>
<li>Server data integration via JSON files</li>
</ul>

<p><strong>4. 3D modeling (CAD)</strong>:</p>
<ul>
<li>Sensor enclosure design in SolidWorks</li>
<li>Consideration of assembly constraints and electronic component sizes</li>
<li>Mechanical simulation to validate design robustness</li>
<li>Iterative 3D printing for physical validation</li>
</ul>

<hr>

<h2>PART C - Technical Aspects</h2>

<h3 class="section-title">Overall system architecture</h3>

<p>The "What-A-Leak" system relies on a distributed architecture composed of several layers:</p>

<p><strong>1. Sensor layer (Node)</strong>: Each node is an autonomous device equipped with an ESP32, an accelerometer and a LoRa module. It collects vibration data and transmits it securely.</p>

<p><strong>2. Communication layer</strong>: Data is encrypted using AES-128 CBC and transmitted via LoRa to a gateway. The choice of LoRa enables a range of several kilometers with low power consumption.</p>

<p><strong>3. Server layer</strong>: A server centralizes the data, stores it in a database, and makes it available via a REST API.</p>

<p><strong>4. Application layer</strong>: The React Native mobile application allows users to monitor node status, view consumption statistics and receive leak alerts.</p>

<p><strong>5. Intelligence layer</strong>: A Machine Learning module analyzes vibration data to distinguish normal vibrations from leak signatures.</p>

<p>The complete data flow is as follows:</p>

<p>Sensor (accelerometer) --> ESP32 (processing + AES encryption) --> LoRa --> Gateway --> Server (API + DB) --> Mobile application</p>

<hr>

<h3 class="section-title">1. Embedded part - ESP32 and data acquisition</h3>

<p>The core of the system relies on the <strong>ESP32</strong> microcontroller, programmed with the <strong>ESP-IDF</strong> framework (Espressif IoT Development Framework) based on <strong>FreeRTOS</strong>. The ESP32 was chosen for several reasons:</p>
<ul>
<li>Dual core allowing simultaneous data acquisition and communication management</li>
<li>Native WiFi and Bluetooth support (useful for initial configuration)</li>
<li>Low power consumption with deep sleep modes</li>
<li>Large ecosystem of libraries and documentation</li>
<li>Compatible with LoRa modules for long-range communication</li>
</ul>

<p><strong>Data acquisition</strong>:</p>
<p>The accelerometer is interfaced with the ESP32 via the I2C or SPI bus. The embedded software performs the following steps:</p>
<ol>
<li>Accelerometer peripheral initialization</li>
<li>Periodic reading of acceleration values on 3 axes (X, Y, Z)</li>
<li>Data pre-processing (filtering, magnitude calculation)</li>
<li>Metrics packaging (vibration, sound level, battery, leak status)</li>
<li>Data encryption via AES-128 CBC</li>
<li>Transmission via the LoRa module</li>
</ol>

<p>The data structure transmitted by each node contains:</p>

<table>
<tr><th>Field</th><th>Description</th><th>Type</th></tr>
<tr><td>NodeID</td><td>Unique node identifier</td><td>Integer</td></tr>
<tr><td>SensorMeasurement</td><td>Sensor measurement value</td><td>Float</td></tr>
<tr><td>Status</td><td>Leak state (0 = normal, 1 = leak)</td><td>Boolean</td></tr>
<tr><td>TimeStamp</td><td>Measurement timestamp</td><td>Date/time</td></tr>
<tr><td>Battery</td><td>Battery level in percentage</td><td>Integer</td></tr>
<tr><td>Temperature</td><td>Ambient temperature (optional)</td><td>Float</td></tr>
</table>

<hr>

<h3 class="section-title">2. Mobile application development</h3>

<p>We chose <strong>React Native</strong> with <strong>Expo</strong> to develop our mobile application due to their efficiency for cross-platform development. React Native allows writing JavaScript code that compiles into native code for iOS and Android, reducing development time and maintenance efforts. Expo simplifies the configuration process and provides access to native APIs.</p>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Innovative_Project/app_workspace.png" style="width: 20%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure: Mobile application workspace structure
</p>

<p><strong>Application architecture</strong>:</p>

<p>The application is structured into several directories and files:</p>
<ul>
<li><strong>assets/</strong>: Static resources (images, icons, logo, splash screen)</li>
<li><strong>Config/</strong>: Node data management including battery levels, vibration and sound measurements, and leak status (JSON files synchronized with the server)</li>
<li><strong>Screen/</strong>: Main application screens</li>
<li><strong>App.js</strong>: Entry point managing the home screen and navigation</li>
<li><strong>app.json</strong>: Application configuration metadata</li>
</ul>

<p><strong>Navigation system</strong>:</p>

<p>The application uses a <strong>Bottom Tab Navigator</strong> (react-navigation) with a purple-themed navigation bar (#6A0DAB). The screens accessible from the navigation bar are:</p>
<ul>
<li>History ("history" icon)</li>
<li>Dashboard ("tint" icon)</li>
<li>Statistics ("bar-chart" icon)</li>
<li>Leak alerts ("exclamation-triangle" icon)</li>
</ul>

<p>The home screen (HomeScreen) is displayed full screen without a navigation bar, and the node detail pages (NodeInfo) are accessible from the dashboard.</p>

<p><strong>Detailed screens and features</strong>:</p>

<ul>
<li><strong>WelcomeScreen</strong>: Startup screen displaying a welcome message and the application logo for 1 second before redirecting to the home screen.</li>
<li><strong>HomeScreen</strong>: Main entry point with login options and application branding.</li>
<li><strong>DashboardScreen</strong>: Overview of all nodes with visual indicators (green = normal, red = leak), battery levels, and overall leak detection status. Also includes a weekly statistics chart.</li>
<li><strong>HistoricScreen</strong>: History of node activities and positions on a geographic map, allowing tracking of measurement evolution over time.</li>
<li><strong>LeakScreen</strong>: History of detected leaks with details (location, timestamp, severity) and contact options for reporting or intervention.</li>
<li><strong>StatisticsScreen</strong>: Detailed water consumption statistics with weekly and monthly charts.</li>
<li><strong>NodeInfo</strong>: Individual node detail page with all its metrics.</li>
</ul>

<div style="text-align: center; display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
    <img src="/img/BE_Innovative_Project/HomeScreen.png" style="width: 18%;"/>
    <img src="/img/BE_Innovative_Project/DashboardScreen.png" style="width: 18%;"/>
    <img src="/img/BE_Innovative_Project/HistoricScreen.png" style="width: 18%;"/>
    <img src="/img/BE_Innovative_Project/LeakScreen.png" style="width: 18%;"/>
    <img src="/img/BE_Innovative_Project/StatisticsScreen.png" style="width: 18%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure: Application screenshots - HomeScreen, DashboardScreen, HistoricScreen, LeakScreen, StatisticsScreen
</p>

<p>The application reads data from a JSON file in the Config directory, synchronized with the server for real-time updates. Future developments include improved data processing, real-time notifications, user authentication and advanced analytics for better understanding of water consumption.</p>

<hr>

<h3 class="section-title">3. 3D modeling (CAD)</h3>

<p>We used <strong>SolidWorks</strong> to design the mechanical model of the sensor enclosure. SolidWorks was chosen for its robust parametric design capabilities and intuitive interface.</p>

<p><strong>Enclosure requirements</strong>:</p>
<ul>
<li>House the electronic board (ESP32 + accelerometer + LoRa module + battery)</li>
<li>Provide openings for connectors and sensors</li>
<li>Ensure direct contact between the sound sensor and the pipe (essential for detection accuracy)</li>
<li>Guarantee solid attachment to the pipe without parasitic vibrations</li>
<li>Allow opening for maintenance (battery replacement, firmware update)</li>
</ul>

<p><strong>Enclosure design</strong>:</p>
<ul>
<li>A dedicated space for the sound sensor ensures direct contact with the pipe</li>
<li>Screw holes secure the enclosure and electronic board, preventing false vibration readings</li>
<li>Dimensions are optimized to minimize footprint while ensuring easy assembly</li>
</ul>

<div style="text-align: center; display: flex; justify-content: center; gap: 60px; flex-wrap: wrap;">
    <img src="/img/BE_Innovative_Project/Assembly.png" style="width: 30%;"/>
    <img src="/img/BE_Innovative_Project/3D_Model.png" style="width: 40%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure: Assembly view and 3D model of the sensor enclosure
</p>

<p><strong>Simulation and validation</strong>:</p>
<p>Mechanical stress simulations were performed in SolidWorks to verify the enclosure's resistance to clamping forces and surrounding vibrations. The validation process included:</p>
<ul>
<li>Stress analysis (Von Mises) to identify weak areas</li>
<li>Deformation verification under load</li>
<li>Iterative 3D printing to validate ergonomics and assembly</li>
<li>Attachment tests on different pipe diameters</li>
</ul>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Innovative_Project/simulation.png" style="width: 40%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure: Mechanical stress simulation of the enclosure
</p>

<hr>

<h3 class="section-title">4. Communication security - AES encryption</h3>

<p><strong>Security problem statement</strong>:</p>

<p>Our project involves a distributed network of sensors (ESP32 + LoRa module) that transmit metrics and preliminary analysis results. Without security mechanisms, the system is vulnerable to several types of attacks:</p>
<ul>
<li><strong>Replay attack</strong>: An attacker intercepts and retransmits legitimate messages to trigger false alerts</li>
<li><strong>Data tampering</strong>: Modification of measurements in transit to conceal a real leak</li>
<li><strong>Passive eavesdropping</strong>: Data interception to obtain information about the water network infrastructure</li>
</ul>

<p><strong>Implemented solution</strong>:</p>

<p>We implemented a lightweight but effective security mechanism using <strong>AES-128 encryption</strong> with the <strong>TinyAES</strong> library (<a href="https://github.com/kokke/tiny-AES-c">tiny-AES-c</a>) and <strong>pre-shared symmetric keys</strong>. Each sensor encrypts its data in <strong>CBC (Cipher Block Chaining)</strong> mode, using a unique <strong>Initialization Vector (IV)</strong> for each message.</p>

<p><strong>Technical details</strong>:</p>

<ul>
<li><strong>AES-128</strong>: Symmetric encryption algorithm using a 128-bit key to encrypt and decrypt data. Chosen for its excellent security/performance ratio, particularly suited for resource-constrained microcontrollers.</li>
<li><strong>CBC mode (Cipher Block Chaining)</strong>: Block cipher operating mode that uses a chaining mechanism. Each plaintext block is XORed with the previous ciphertext block before being encrypted, ensuring that identical plaintext blocks produce different ciphertext blocks.</li>
<li><strong>Initialization Vector (IV)</strong>: Random or pseudo-random value used to initialize the encryption process. In our implementation, to balance security and transmission efficiency:
  <ul>
  <li><strong>2 bytes</strong> are randomly generated for each message (transmitted with the message)</li>
  <li><strong>14 bytes</strong> are static (pre-shared between the sensor and the server)</li>
  <li>This approach reduces communication overhead while maintaining sufficient entropy</li>
  </ul>
</li>
<li><strong>PKCS#7 padding</strong>: Padding scheme used to ensure that the plaintext length is a multiple of the block size (16 bytes for AES). PKCS#7 adds a series of bytes whose value equals the number of padding bytes added.</li>
</ul>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Innovative_Project/secu.png" style="width: 100%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure: System security architecture - encryption and decryption flow
</p>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Innovative_Project/aes_encrypt.png" style="width: 90%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure: Detail of the AES-128 CBC encryption process with partial IV
</p>

<p><strong>Design choices for embedded systems</strong>:</p>
<ul>
<li>TinyAES is an ultra-lightweight AES implementation (a few KB of Flash) compatible with the ESP32's memory constraints</li>
<li>CBC mode was preferred over ECB mode because the latter does not mask patterns in the data</li>
<li>The pre-shared key avoids the complexity of a key exchange (Diffie-Hellman type) unsuitable for a microcontroller</li>
</ul>

<hr>

<h3 class="section-title">5. LoRa communication protocol</h3>

<p><strong>Why LoRa</strong>:</p>

<p>LoRa (Long Range) was selected as the wireless communication protocol for several reasons:</p>
<ul>
<li><strong>Range</strong>: Several kilometers in urban environments, up to 15 km in open field</li>
<li><strong>Low power consumption</strong>: Compatible with battery operation for several months</li>
<li><strong>Penetration</strong>: Good obstacle penetration (walls, underground)</li>
<li><strong>ISM band</strong>: Use of the ISM band (868 MHz in Europe) without licensing</li>
</ul>

<p><strong>Integration with the ESP32</strong>:</p>
<p>The LoRa module is connected to the ESP32 via the SPI interface. The firmware manages:</p>
<ul>
<li>Radio parameter configuration (frequency, spreading factor, bandwidth)</li>
<li>Sending encrypted packets at regular intervals</li>
<li>Power management (sleep mode between transmissions)</li>
<li>Transmission error detection</li>
</ul>

<hr>

<h2>PART D - Analysis and Reflection</h2>

<h3 class="section-title">Skills acquired</h3>

<p>This project allowed me to develop and consolidate a wide range of skills:</p>

<p><strong>Technical skills</strong>:</p>
<ul>
<li>Analyzing concrete problems and proposing suitable technological solutions</li>
<li>Developing embedded software for microcontrollers (ESP32, FreeRTOS, ESP-IDF)</li>
<li>Implementing security mechanisms (AES encryption) on resource-constrained systems</li>
<li>Creating cross-platform mobile applications with React Native and Expo</li>
<li>Designing 3D models (CAD) with SolidWorks and validating through simulation</li>
<li>Integrating sensors and communication modules into an embedded system</li>
<li>Managing an end-to-end data flow (sensor --> server --> application)</li>
</ul>

<p><strong>Soft skills</strong>:</p>
<ul>
<li>Working in a team on a large-scale project with interdependent subsystems</li>
<li>Presenting and debating technical choices in English before a jury</li>
<li>Writing comprehensive technical reports in English</li>
<li>Applying Agile methodology (sprints, reviews, retrospectives)</li>
<li>Managing priorities and deadlines in a project with many deliverables</li>
</ul>

<h3 class="section-title">Self-assessment</h3>

<p>This project was one of the most advanced projects in my curriculum. Leading a project from scratch to a functional prototype, involving hardware, embedded software, data storage, data transmission, 3D modeling, server, artificial intelligence and application interface, it was a complete project, a prototype ready for commercialization.</p>

<p>Due to the project's scope, I was not able to work on all aspects, but I collaborated closely with my colleagues to stay informed about each component. I am proud of my contributions, and the system is functional. Being part of a dedicated team where everyone was eager to learn new things was a very enriching experience.</p>

<p>The part that challenged me the most was implementing AES security on the ESP32. It required an in-depth understanding of block cipher operation, managing the microcontroller's memory constraints, and ensuring encryption compatibility between the ESP32 (C) and the server (Python/Node.js).</p>

<p>Developing the mobile application allowed me to discover React Native and the mobile JavaScript ecosystem. Creating an intuitive user interface with tab navigation, charts and maps was a rich learning experience.</p>

<h3 class="section-title">My opinion</h3>

<p>This project was an excellent opportunity to explore different domains and conduct our own research on how to manage the project. In my opinion, the current organization of sessions was ideal for delivering a prototype, but not sufficient for delivering a fully functional final product with all desired features.</p>

<p>I discovered how to integrate many concepts learned throughout the year into a real project, similar to what we might be asked to do in a professional setting. This project was a tremendous experience and I am proud of the results we achieved.</p>

<p><strong>Project strengths</strong>:</p>
<ul>
<li>End-to-end functional prototype</li>
<li>Diversity of mastered technologies (embedded, mobile, 3D, security)</li>
<li>Effective teamwork with clear task distribution</li>
<li>Regular presentations fostering communication</li>
</ul>

<p><strong>Areas for improvement</strong>:</p>
<ul>
<li>More time for integration and system testing</li>
<li>Deepen the Machine Learning part for vibration classification</li>
<li>Implement real-time push notifications in the application</li>
<li>Add robust user authentication</li>
</ul>

<h3 class="section-title">Project management and teamwork</h3>

<p>The Agile methodology with 3 to 4 week sprints proved very effective for this type of project. End-of-sprint presentations forced us to have concrete deliverables at each stage, thus avoiding the "tunnel" effect where integration is pushed to the end.</p>

<p>Communication within the team was a key success factor. Weekly meetings allowed synchronizing progress, identifying blockers and redistributing efforts when necessary. Using GitHub with a dedicated organization facilitated code management and collaboration.</p>

<hr>

<h2>Reports and Projects</h2>

<div style="text-align: center;">
    <h3>
        <span class="lang-fr">Rapport de projet</span>
        <span class="lang-en">Project Report</span>
    </h3>
</div>

<p style="text-align: justify;">The complete source code of the project is available on the GitHub organization: <a href="https://github.com/what-a-leak">What-A-Leak</a></p>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">Rapport du Projet Innovant ISS</span>
        <span class="lang-en">ISS Innovative Project Report</span>
      </h4>
      <p>
        <span class="lang-fr">Rapport complet du projet "What-A-Leak" detaillant la conception, l'implementation et les resultats du systeme de detection de fuites d'eau.</span>
        <span class="lang-en">Complete report of the "What-A-Leak" project detailing the design, implementation and results of the water leak detection system.</span>
      </p>
      <div class="pdf-lazy" data-src="/file/reports/S9/Rapport_Projet_ISS.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/file/reports/S9/Rapport_Projet_ISS.pdf" target="_blank">
        <span class="lang-fr">Telecharger le rapport</span>
        <span class="lang-en">Download the report</span>
      </a></p>
    </div>
  </div>
</div>

<div style="text-align: center;">
    <h3>
        <span class="lang-fr">Presentation finale</span>
        <span class="lang-en">Final Presentation</span>
    </h3>
</div>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">Presentation finale du projet</span>
        <span class="lang-en">Final Project Presentation</span>
      </h4>
      <p>
        <span class="lang-fr">Support de presentation utilise lors de la soutenance finale du projet devant le jury.</span>
        <span class="lang-en">Presentation slides used during the final project defense before the jury.</span>
      </p>
      <div class="pdf-lazy" data-src="/img/BE_Innovative_Project/Prez_final.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/img/BE_Innovative_Project/Prez_final.pdf" target="_blank">
        <span class="lang-fr">Telecharger la presentation</span>
        <span class="lang-en">Download the presentation</span>
      </a></p>
    </div>
  </div>
</div>

<hr>

<p><em>Project completed in 2024-2025 at INSA Toulouse, ISS Department (Innovative Smart Systems).</em></p>

</div>

<div class="back-nav">
    <a href="./my-courses-2024-2025.html" data-i18n-html="back-courses-2024-2025">&larr; Retour aux Cours 2024-2025</a>
</div>

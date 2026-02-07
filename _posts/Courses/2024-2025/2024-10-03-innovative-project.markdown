---
layout: default
title:  "Innovative Project"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
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
    <a href="./my-courses-2024-2025.html">&larr; Retour aux Cours 2024-2025</a>
</div>

# Projet Innovant (Innovative Project) - Semestre 9

**Annee academique** : 2024-2025
**Semestre** : S9 - INSA Toulouse, parcours ISS (Innovative Smart Systems)
**Projet** : What-A-Leak - Systeme de detection de fuites d'eau

---

## PART A - Presentation Generale

<h3 class="section-title">Objectifs du projet</h3>

Le Projet Innovant (Innovative Project) est le projet phare du semestre 9 du parcours ISS a l'INSA Toulouse. Il s'agit d'un projet multidisciplinaire de grande envergure visant a concevoir un prototype fonctionnel repondant a une problematique reelle. Notre projet, intitule **"What-A-Leak"**, avait pour objectif de developper un systeme intelligent de detection de fuites d'eau dans les reseaux de canalisations, en utilisant une approche non intrusive basee sur des capteurs vibratoires.

**Problematique** :
Les fuites d'eau representent un enjeu majeur tant au niveau domestique qu'au niveau des infrastructures publiques. Les methodes de detection traditionnelles sont souvent intrusives, couteuses et necessitent une intervention humaine. Notre projet propose une solution connectee, autonome et securisee pour detecter les fuites en temps reel.

**Objectifs principaux** :
- Concevoir un noeud capteur embarque capable de detecter des vibrations anormales dans les canalisations
- Developper un protocole de communication securise pour la transmission des donnees
- Creer une application mobile intuitive pour le suivi et la gestion des alertes
- Realiser un boitier physique adapte via modelisation 3D et impression
- Construire un prototype complet et fonctionnel, de l'acquisition de donnees a l'interface utilisateur

<h3 class="section-title">Organisation de l'equipe</h3>

Notre equipe etait composee de **cinq membres**, chacun avec des responsabilites specifiques :

| Membre | Responsabilites principales |
|--------|---------------------------|
| Moi-meme | Logiciel embarque, securite (AES), application mobile (React Native), modelisation 3D (CAD) |
| Collegue 1 | Serveur backend, base de donnees, API |
| Collegue 2 | Machine Learning, analyse des donnees vibratoires |
| Collegue 3 | Site web de presentation, documentation |
| Collegue 4 | Hardware, protocole LoRa, integration electronique |

<h3 class="section-title">Chronologie et methodologie</h3>

Le projet s'est deroule en **4 sprints** suivant une methodologie Agile :

| Sprint | Periode | Objectifs |
|--------|---------|-----------|
| Sprint 1 | Debut du semestre | Definition du cahier des charges, choix des technologies, premieres maquettes |
| Sprint 2 | Mi-semestre | Developpement des composants individuels (embarque, app, serveur) |
| Sprint 3 | Fin de semestre - 1 mois | Integration des composants, premiers tests de bout en bout |
| Sprint 4 | Dernier mois | Tests finaux, optimisation, preparation de la presentation |

Chaque sprint se terminait par une presentation devant les enseignants et les autres groupes, permettant de recevoir des retours et d'ajuster la direction du projet.

---

## PART B - Experience et Contexte

<h3 class="section-title">Environnement et contexte</h3>

Le projet s'est deroule dans un environnement collaboratif au sein du departement ISS de l'INSA Toulouse. Ce projet fait partie d'une initiative multidisciplinaire innovante ou les etudiants doivent mener un projet de A a Z, de l'idee initiale au prototype fonctionnel.

L'objectif initial etait de detecter les fuites d'eau dans les maisons. Cependant, au fur et a mesure de l'avancement du projet, la portee s'est elargie pour inclure une approche distribuee applicable aux infrastructures de reseaux d'eau publics. Cette evolution a permis de passer d'un cas d'usage domestique a un cas d'usage industriel, ajoutant de la complexite et de la pertinence au projet.

Le projet a offert une plateforme unique pour appliquer les connaissances theoriques acquises durant le cursus a des scenarios pratiques, favorisant l'innovation, la creativite et la gestion de projet.

<h3 class="section-title">Outils et environnement de developpement</h3>

**Partie embarquee** :
- **Microcontroleur** : ESP32 (framework ESP-IDF via le SDK Espressif)
- **Capteur** : Accelerometre pour la detection de vibrations
- **Communication** : Module LoRa pour la transmission longue portee
- **IDE** : VS Code avec extension ESP-IDF
- **Langage** : C (FreeRTOS)

**Application mobile** :
- **Framework** : React Native avec Expo
- **Langage** : JavaScript
- **Bibliotheques** : React Navigation (navigation par onglets), react-native-vector-icons (icones), react-native-chart-kit (graphiques)
- **Gestion de donnees** : JSON synchronise avec le serveur

**Modelisation 3D** :
- **Logiciel** : SolidWorks
- **Fabrication** : Impression 3D (PLA)
- **Simulation** : Analyse de contraintes mecaniques

**Securite** :
- **Algorithme** : AES-128 en mode CBC
- **Bibliotheque** : TinyAES (tiny-AES-c)
- **Cle** : Pre-partagee, symetrique

**Gestion de projet** :
- **Versionning** : Git / GitHub (organisation [what-a-leak](https://github.com/what-a-leak))
- **Communication** : Reunions hebdomadaires, presentations de sprint

<h3 class="section-title">Mon role dans le projet</h3>

Dans ce projet, j'ai assume plusieurs responsabilites couvrant differents domaines techniques :

**1. Developpement du logiciel embarque** :
- Programmation du microcontroleur ESP32 avec le framework ESP-IDF
- Configuration et lecture de l'accelerometre pour l'acquisition des donnees vibratoires
- Implementation de la collecte de metriques (vibration, son, batterie) pour la detection de fuites
- Integration avec le module de communication LoRa

**2. Securite des communications** :
- Implementation du chiffrement AES-128 en mode CBC sur l'ESP32
- Gestion des vecteurs d'initialisation (IV) avec partie aleatoire et statique
- Padding PKCS#7 pour l'alignement des blocs de donnees
- Tests de validation du chiffrement/dechiffrement de bout en bout

**3. Application mobile** :
- Developpement complet de l'application React Native avec Expo
- Conception de l'architecture de navigation (Bottom Tab Navigator)
- Creation des ecrans : accueil, tableau de bord, historique, fuites, statistiques
- Integration des donnees provenant du serveur via fichiers JSON

**4. Modelisation 3D (CAD)** :
- Conception du boitier du capteur sous SolidWorks
- Prise en compte des contraintes d'assemblage et de la taille des composants electroniques
- Simulation mecanique pour valider la robustesse du design
- Iteration avec impression 3D pour validation physique

---

## PART C - Aspects Techniques

<h3 class="section-title">Architecture globale du systeme</h3>

Le systeme "What-A-Leak" repose sur une architecture distribuee composee de plusieurs couches :

**1. Couche capteur (Noeud)** : Chaque noeud est un dispositif autonome equipe d'un ESP32, d'un accelerometre et d'un module LoRa. Il collecte les donnees vibratoires et les transmet de maniere securisee.

**2. Couche communication** : Les donnees sont chiffrees en AES-128 CBC et transmises via LoRa vers une passerelle (gateway). Ce choix de LoRa permet une portee de plusieurs kilometres avec une faible consommation energetique.

**3. Couche serveur** : Un serveur centralise les donnees, les stocke dans une base de donnees, et les met a disposition via une API REST.

**4. Couche application** : L'application mobile React Native permet aux utilisateurs de surveiller l'etat des noeuds, visualiser les statistiques de consommation et recevoir des alertes en cas de fuite.

**5. Couche intelligence** : Un module de Machine Learning analyse les donnees vibratoires pour distinguer les vibrations normales des signatures de fuites.

Le flux de donnees complet est le suivant :

Capteur (accelerometre) --> ESP32 (traitement + chiffrement AES) --> LoRa --> Gateway --> Serveur (API + BDD) --> Application mobile

---

<h3 class="section-title">1. Partie embarquee - ESP32 et acquisition de donnees</h3>

Le coeur du systeme repose sur le microcontroleur **ESP32**, programme avec le framework **ESP-IDF** (Espressif IoT Development Framework) base sur **FreeRTOS**. Le choix de l'ESP32 s'est impose pour plusieurs raisons :
- Double coeur permettant de gerer simultanement l'acquisition de donnees et la communication
- Support natif du WiFi et du Bluetooth (utile pour la configuration initiale)
- Faible consommation energetique avec modes de veille profonde
- Large ecosysteme de bibliotheques et de documentation
- Compatible avec les modules LoRa pour la communication longue portee

**Acquisition de donnees** :
L'accelerometre est interface avec l'ESP32 via le bus I2C ou SPI. Le logiciel embarque realise les etapes suivantes :
1. Initialisation du peripherique accelerometre
2. Lecture periodique des valeurs d'acceleration sur les 3 axes (X, Y, Z)
3. Pre-traitement des donnees (filtrage, calcul de la magnitude)
4. Empaquetage des metriques (vibration, niveau sonore, batterie, statut de fuite)
5. Chiffrement des donnees via AES-128 CBC
6. Transmission via le module LoRa

La structure de donnees transmise par chaque noeud contient :

| Champ | Description | Type |
|-------|-------------|------|
| NodeID | Identifiant unique du noeud | Entier |
| MesureCapteur | Valeur de mesure du capteur | Flottant |
| Status | Etat de fuite (0 = normal, 1 = fuite) | Booleen |
| TimeStamp | Horodatage de la mesure | Date/heure |
| Batterie | Niveau de batterie en pourcentage | Entier |
| Temperature | Temperature ambiante (optionnel) | Flottant |

---

<h3 class="section-title">2. Developpement de l'application mobile</h3>

Nous avons choisi **React Native** avec **Expo** pour developper notre application mobile en raison de leur efficacite pour le developpement multiplateforme. React Native permet d'ecrire du code JavaScript qui se compile en code natif pour iOS et Android, reduisant le temps de developpement et les efforts de maintenance. Expo simplifie le processus de configuration et fournit un acces aux API natives.

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Innovative_Project/app_workspace.png" style="width: 20%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">Figure : Structure du workspace de l'application mobile</p>

**Architecture de l'application** :

L'application est structuree en plusieurs repertoires et fichiers :
- **assets/** : Ressources statiques (images, icones, logo, splash screen)
- **Config/** : Gestion des donnees des noeuds incluant les niveaux de batterie, les mesures de vibration et de son, et le statut de fuite (fichiers JSON synchronises avec le serveur)
- **Screen/** : Les ecrans principaux de l'application
- **App.js** : Point d'entree gerant l'ecran d'accueil et la navigation
- **app.json** : Metadonnees de configuration de l'application

**Systeme de navigation** :

L'application utilise un **Bottom Tab Navigator** (react-navigation) avec une barre de navigation au theme violet (#6A0DAB). Les ecrans accessibles depuis la barre de navigation sont :
- Historique (icone "history")
- Tableau de bord (icone "tint")
- Statistiques (icone "bar-chart")
- Alertes de fuites (icone "exclamation-triangle")

L'ecran d'accueil (HomeScreen) est affiche en plein ecran sans barre de navigation, et les pages de detail des noeuds (NodeInfo) sont accessibles depuis le tableau de bord.

**Ecrans et fonctionnalites detaillees** :

- **WelcomeScreen** : Ecran de demarrage affichant un message de bienvenue et le logo de l'application pendant 1 seconde avant de rediriger vers l'ecran d'accueil.
- **HomeScreen** : Point d'entree principal avec options de connexion et branding de l'application.
- **DashboardScreen** : Vue d'ensemble de tous les noeuds avec indicateurs visuels (vert = normal, rouge = fuite), niveaux de batterie, et statut global de detection de fuite. Inclut egalement un graphique de statistiques hebdomadaires.
- **HistoricScreen** : Historique des activites des noeuds et positions sur une carte geographique, permettant de suivre l'evolution des mesures dans le temps.
- **LeakScreen** : Historique des fuites detectees avec details (localisation, horodatage, severite) et options de contact pour signaler ou intervenir.
- **StatisticsScreen** : Statistiques detaillees de consommation d'eau avec graphiques hebdomadaires et mensuels.
- **NodeInfo** : Page de detail d'un noeud individuel avec toutes ses metriques.

<div style="text-align: center; display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
    <img src="/img/BE_Innovative_Project/HomeScreen.png" style="width: 18%;"/>
    <img src="/img/BE_Innovative_Project/DashboardScreen.png" style="width: 18%;"/>
    <img src="/img/BE_Innovative_Project/HistoricScreen.png" style="width: 18%;"/>
    <img src="/img/BE_Innovative_Project/LeakScreen.png" style="width: 18%;"/>
    <img src="/img/BE_Innovative_Project/StatisticsScreen.png" style="width: 18%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">Figure : Captures d'ecran de l'application - HomeScreen, DashboardScreen, HistoricScreen, LeakScreen, StatisticsScreen</p>

L'application lit les donnees depuis un fichier JSON dans le repertoire Config, synchronise avec le serveur pour les mises a jour en temps reel. Les evolutions futures incluent un traitement de donnees ameliore, des notifications en temps reel, une authentification utilisateur et des analyses avancees pour une meilleure comprehension de la consommation d'eau.

---

<h3 class="section-title">3. Modelisation 3D (CAD)</h3>

Nous avons utilise **SolidWorks** pour concevoir le modele mecanique du boitier du capteur. Le choix de SolidWorks s'est impose pour ses fonctionnalites robustes de conception parametrique et son interface intuitive.

**Cahier des charges du boitier** :
- Loger la carte electronique (ESP32 + accelerometre + module LoRa + batterie)
- Prevoir des ouvertures pour les connecteurs et les capteurs
- Assurer un contact direct entre le capteur sonore et la canalisation (essentiel pour la precision de la detection)
- Garantir une fixation solide a la canalisation sans vibrations parasites
- Permettre l'ouverture pour la maintenance (remplacement de batterie, mise a jour firmware)

**Conception du boitier** :
- Un espace dedie au capteur sonore assure le contact direct avec la canalisation
- Des trous de vis securisent le boitier et la carte electronique, evitant les fausses lectures de vibrations
- Les dimensions sont optimisees pour minimiser l'encombrement tout en assurant un assemblage aise

<div style="text-align: center; display: flex; justify-content: center; gap: 60px; flex-wrap: wrap;">
    <img src="/img/BE_Innovative_Project/Assembly.png" style="width: 30%;"/>
    <img src="/img/BE_Innovative_Project/3D_Model.png" style="width: 40%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">Figure : Vue d'assemblage et modele 3D du boitier du capteur</p>

**Simulation et validation** :
Des simulations de contraintes mecaniques ont ete realisees sous SolidWorks pour verifier la resistance du boitier aux efforts de serrage et aux vibrations environnantes. Le processus de validation a inclus :
- Analyse de contraintes (Von Mises) pour identifier les zones de faiblesse
- Verification des deformations sous charge
- Impression 3D iterative pour valider l'ergonomie et l'assemblage
- Tests de fixation sur differents diametres de canalisations

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Innovative_Project/simulation.png" style="width: 40%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">Figure : Simulation de contraintes mecaniques du boitier</p>

---

<h3 class="section-title">4. Securite des communications - Chiffrement AES</h3>

**Problematique de securite** :

Notre projet implique un reseau distribue de capteurs (ESP32 + module LoRa) qui transmettent des metriques et des resultats d'analyse preliminaire. Sans mecanisme de securite, le systeme est vulnerable a plusieurs types d'attaques :
- **Attaque par rejeu (replay)** : Un attaquant intercepte et retransmet des messages legitimes pour provoquer de fausses alertes
- **Alteration des donnees (tampering)** : Modification des mesures en transit pour masquer une fuite reelle
- **Ecoute passive (eavesdropping)** : Interception des donnees pour obtenir des informations sur l'infrastructure du reseau d'eau

**Solution implementee** :

Nous avons mis en place un mecanisme de securite leger mais efficace utilisant le **chiffrement AES-128** avec la bibliotheque **TinyAES** ([tiny-AES-c](https://github.com/kokke/tiny-AES-c)) et des **cles symetriques pre-partagees**. Chaque capteur chiffre ses donnees en mode **CBC (Cipher Block Chaining)**, utilisant un **vecteur d'initialisation (IV)** unique pour chaque message.

**Details techniques** :

- **AES-128** : Algorithme de chiffrement symetrique utilisant une cle de 128 bits pour chiffrer et dechiffrer les donnees. Choisi pour son excellent rapport securite/performance, particulierement adapte aux microcontroleurs a ressources limitees.

- **Mode CBC (Cipher Block Chaining)** : Mode d'operation pour les chiffrements par blocs qui utilise un mecanisme de chainage. Chaque bloc de texte clair est XORe avec le bloc chiffre precedent avant d'etre chiffre, garantissant que des blocs de texte clair identiques produisent des blocs chiffres differents.

- **Vecteur d'Initialisation (IV)** : Valeur aleatoire ou pseudo-aleatoire utilisee pour initialiser le processus de chiffrement. Dans notre implementation, pour equilibrer securite et efficacite de transmission :
  - **2 octets** sont generes aleatoirement a chaque message (transmis avec le message)
  - **14 octets** sont statiques (pre-partages entre le capteur et le serveur)
  - Cette approche reduit la surcharge de communication tout en maintenant une entropie suffisante

- **Padding PKCS#7** : Schema de remplissage utilise pour assurer que la longueur du texte clair est un multiple de la taille du bloc (16 octets pour AES). PKCS#7 ajoute une serie d'octets dont la valeur est egale au nombre d'octets de remplissage ajoutes.

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Innovative_Project/secu.png" style="width: 100%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">Figure : Architecture de securite du systeme - flux de chiffrement et dechiffrement</p>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Innovative_Project/aes_encrypt.png" style="width: 90%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">Figure : Detail du processus de chiffrement AES-128 CBC avec IV partiel</p>

**Choix de conception pour l'embarque** :
- TinyAES est une implementation ultra-legere d'AES (quelques Ko de Flash) compatible avec les contraintes memoire de l'ESP32
- Le mode CBC a ete prefere au mode ECB car ce dernier ne masque pas les motifs dans les donnees
- La cle pre-partagee evite la complexite d'un echange de cles (type Diffie-Hellman) inadapte a un microcontroleur

---

<h3 class="section-title">5. Protocole de communication LoRa</h3>

**Choix de LoRa** :

LoRa (Long Range) a ete selectionne comme protocole de communication sans fil pour plusieurs raisons :
- **Portee** : Plusieurs kilometres en milieu urbain, jusqu'a 15 km en champ libre
- **Faible consommation** : Compatible avec un fonctionnement sur batterie pendant plusieurs mois
- **Penetration** : Bonne penetration des obstacles (murs, sous-sol)
- **Bande ISM** : Utilisation de la bande ISM (868 MHz en Europe) sans licence

**Integration avec l'ESP32** :
Le module LoRa est connecte a l'ESP32 via l'interface SPI. Le firmware gere :
- La configuration des parametres radio (frequence, spreading factor, bande passante)
- L'envoi des paquets chiffres a intervalles reguliers
- La gestion de la consommation (mode veille entre les transmissions)
- La detection d'erreurs de transmission

---

## PART D - Analyse et Reflexion

<h3 class="section-title">Competences acquises</h3>

Ce projet m'a permis de developper et de consolider un large eventail de competences :

**Competences techniques** :
- Analyser des problemes concrets et proposer des solutions technologiques adaptees
- Developper du logiciel embarque pour microcontroleur (ESP32, FreeRTOS, ESP-IDF)
- Implementer des mecanismes de securite (chiffrement AES) sur des systemes a ressources limitees
- Creer des applications mobiles multiplateformes avec React Native et Expo
- Concevoir des modeles 3D (CAD) avec SolidWorks et valider par simulation
- Integrer des capteurs et des modules de communication dans un systeme embarque
- Gerer un flux de donnees de bout en bout (capteur --> serveur --> application)

**Competences transversales** :
- Travailler en equipe sur un projet de grande envergure avec des sous-systemes interdependants
- Presenter et debattre des choix techniques en anglais devant un jury
- Rediger des rapports techniques complets en anglais
- Appliquer une methodologie Agile (sprints, revues, retrospectives)
- Gerer les priorites et les delais dans un projet avec de nombreux livrables

<h3 class="section-title">Auto-evaluation</h3>

Ce projet a ete l'un des projets les plus avances de mon parcours. Mener un projet de zero jusqu'a un prototype fonctionnel, impliquant hardware, logiciel embarque, stockage de donnees, transmission de donnees, modelisation 3D, serveur, intelligence artificielle et interface applicative, c'etait un projet complet, un prototype pret a la commercialisation.

En raison de l'envergure du projet, je n'ai pas pu travailler sur tous les aspects, mais j'ai collabore etroitement avec mes collegues pour rester informe de chaque composant. Je suis fier de mes contributions, et le systeme est fonctionnel. Faire partie d'une equipe dediee ou chacun etait desireux d'apprendre de nouvelles choses a ete une experience tres enrichissante.

La partie qui m'a le plus challenge a ete l'implementation de la securite AES sur l'ESP32. Il a fallu comprendre en profondeur le fonctionnement du chiffrement par blocs, gerer les contraintes memoire du microcontroleur, et assurer la compatibilite du chiffrement entre l'ESP32 (C) et le serveur (Python/Node.js).

Le developpement de l'application mobile m'a permis de decouvrir React Native et l'ecosysteme JavaScript mobile. La creation d'une interface utilisateur intuitive avec navigation par onglets, graphiques et cartes a ete un apprentissage riche.

<h3 class="section-title">Mon avis</h3>

Ce projet a ete une excellente opportunite d'explorer differents domaines et de mener nos propres recherches sur la maniere de gerer le projet. A mon avis, l'organisation actuelle des sessions etait ideale pour livrer un prototype, mais pas suffisante pour livrer un produit final entierement fonctionnel avec toutes les fonctionnalites souhaitees.

J'ai decouvert comment integrer de nombreux concepts appris au cours de l'annee dans un projet reel, similaire a ce que l'on pourrait nous demander en entreprise. Ce projet a ete une experience formidable et je suis fier des resultats que nous avons obtenus.

**Points forts du projet** :
- Prototype fonctionnel de bout en bout
- Diversite des technologies maitrisees (embarque, mobile, 3D, securite)
- Travail d'equipe efficace avec repartition claire des taches
- Presentations regulieres favorisant la communication

**Axes d'amelioration** :
- Plus de temps pour l'integration et les tests systeme
- Approfondir la partie Machine Learning pour la classification des vibrations
- Implementer des notifications push en temps reel dans l'application
- Ajouter une authentification utilisateur robuste

<h3 class="section-title">Gestion de projet et travail d'equipe</h3>

La methodologie Agile avec des sprints de 3 a 4 semaines s'est revelee tres efficace pour ce type de projet. Les presentations de fin de sprint nous ont obliges a avoir des livrables concrets a chaque etape, evitant ainsi l'effet "tunnel" ou l'integration est repoussee a la fin.

La communication au sein de l'equipe a ete un facteur cle de reussite. Les reunions hebdomadaires permettaient de synchroniser les avancees, identifier les blocages et redistribuer les efforts si necessaire. L'utilisation de GitHub avec une organisation dediee a facilite la gestion du code et la collaboration.

---

## Rapports et Projets

<h3 class="section-title">Rapport de projet</h3>

Le code source complet du projet est disponible sur l'organisation GitHub : [What-A-Leak](https://github.com/what-a-leak)

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Rapport du Projet Innovant ISS</h4>
      <p>Rapport complet du projet "What-A-Leak" detaillant la conception, l'implementation et les resultats du systeme de detection de fuites d'eau.</p>
      <embed src="/file/reports/S9/Rapport_Projet_ISS.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/file/reports/S9/Rapport_Projet_ISS.pdf" target="_blank">Telecharger le rapport</a></p>
    </div>
  </div>
</div>

<h3 class="section-title">Presentation finale</h3>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Presentation finale du projet</h4>
      <p>Support de presentation utilise lors de la soutenance finale du projet devant le jury.</p>
      <embed src="/img/BE_Innovative_Project/Prez_final.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/img/BE_Innovative_Project/Prez_final.pdf" target="_blank">Telecharger la presentation</a></p>
    </div>
  </div>
</div>

---

*Projet realise en 2024-2025 a l'INSA Toulouse, Departement ISS (Innovative Smart Systems).*

<div class="back-nav">
    <a href="./my-courses-2024-2025.html">&larr; Retour aux Cours 2024-2025</a>
</div>

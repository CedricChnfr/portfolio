---
layout: default
title:  "Middleware for IoT"
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
    <a href="./my-courses-2024-2025.html" data-i18n-html="back-courses-2024-2025">&larr; Retour aux Cours 2024-2025</a>
</div>

<div class="lang-fr">

<h1>Middleware for IoT / M2M - Semestre 9</h1>

<p><strong>Annee academique</strong> : 2024-2025<br>
<strong>Enseignant</strong> : T. Monteil (LAAS-CNRS)<br>
<strong>ECTS</strong> : 2.5<br>
<strong>Categorie</strong> : IoT, Protocoles de communication, Middleware</p>

<p><strong>Cours connexes</strong> :</p>
<ul>
<li><a href="./security-object.html">Security for Connected Objects - S9</a> - Securisation IoT</li>
<li><a href="./cloud-edge.html">Cloud &amp; Edge Computing - S9</a> - Architectures IoT</li>
<li><a href="./wireless-sensors.html">Wireless Sensors Networks - S9</a> - Reseaux de capteurs</li>
</ul>

<hr>

<h2>PART A - Presentation Generale</h2>

<h3 class="section-title">Vue d'ensemble</h3>

<p>Le cours "Middleware for IoT / M2M" aborde les architectures logicielles intermediaires (middleware) et les protocoles de communication dedies a l'Internet des Objets (IoT) et aux communications Machine-to-Machine (M2M). Il couvre l'ensemble de la chaine, depuis les protocoles de messagerie leger comme MQTT jusqu'aux standards de gestion de ressources comme oneM2M, en passant par le prototypage rapide d'applications IoT avec Node-RED.</p>

<p>L'objectif est de former des ingenieurs capables de concevoir, deployer et integrer des systemes IoT complets, en maitrise des protocoles de communication adaptes aux contraintes des objets connectes (bande passante limitee, consommation energetique, fiabilite).</p>

<p><strong>Objectifs pedagogiques</strong> :</p>
<ul>
<li>Comprendre les principaux standards de l'Internet des Objets (MQTT, oneM2M, CoAP)</li>
<li>Deployer et configurer des architectures IoT avec broker MQTT et CSE oneM2M</li>
<li>Programmer des microcontroleurs (NodeMCU/ESP8266) pour communiquer via MQTT</li>
<li>Concevoir des applications IoT avec Node-RED (prototypage rapide)</li>
<li>Comparer et choisir les protocoles adaptes aux cas d'usage IoT (HTTP vs MQTT vs CoAP)</li>
<li>Integrer capteurs, actionneurs et dashboards dans une architecture IoT complete</li>
<li>Analyser les enjeux de securite, scalabilite et interoperabilite des systemes M2M</li>
</ul>

<h3 class="section-title">Position dans le cursus</h3>

<p>Ce module s'appuie sur les bases acquises anterieurement :</p>
<ul>
<li><strong>Reseau (S5-S8)</strong> : modele OSI, TCP/IP, HTTP, sockets</li>
<li><strong>Microcontroleurs (S5-S7)</strong> : programmation embarquee, Arduino</li>
<li><strong>Systemes d'exploitation</strong> : Linux, scripts Python</li>
</ul>

<p>Il prepare et se connecte a :</p>
<ul>
<li><strong>Cloud et Edge Computing (S9)</strong> : deploiement d'architectures distribuees</li>
<li><strong>Security for Connected Objects (S9)</strong> : securisation des communications IoT</li>
<li><strong>Wireless Sensors Networks (S9)</strong> : couches physiques et liaison des capteurs</li>
<li><strong>Projet Innovant (S9)</strong> : integration des protocoles IoT dans un projet reel</li>
</ul>

<hr>

<h2>PART B - Experience et Contexte</h2>

<h3 class="section-title">Organisation et ressources</h3>

<p>Le module combinait cours theoriques et travaux pratiques progressifs :</p>

<p><strong>Cours magistraux</strong> :</p>
<ul>
<li>Architecture IoT et pile protocolaire</li>
<li>Protocole MQTT : principes, QoS, topics, retain, last will</li>
<li>Standard oneM2M : architecture, ressources, CSE, AE</li>
<li>MOOC oneM2M (formation en autonomie)</li>
<li>Comparaison des protocoles IoT (HTTP, MQTT, CoAP, AMQP)</li>
<li>Patrons de communication M2M (publish/subscribe, request/response)</li>
</ul>

<p><strong>Travaux pratiques (TP)</strong> :</p>
<ul>
<li><strong>TP1-2</strong> : Installation et configuration du broker MQTT Mosquitto, communication publish/subscribe, programmation NodeMCU/ESP8266 avec ArduinoMqttClient</li>
<li><strong>TP3</strong> : Standard oneM2M avec ACME CSE, creation de ressources (AE, Container, ContentInstance) via API RESTful, script Python simple_om2m.py</li>
<li><strong>TP4</strong> : Prototypage rapide avec Node-RED, integration MQTT, dashboard, gestion de capteurs et actionneurs, notifications email</li>
</ul>

<p><strong>Bureau d'Etudes (BE)</strong> :</p>
<ul>
<li>Projet BE M2M : mise en oeuvre d'une architecture complete M2M integrant MQTT, oneM2M et Node-RED</li>
</ul>

<p><strong>Outils utilises</strong> :</p>
<ul>
<li><strong>Mosquitto</strong> : broker MQTT open-source</li>
<li><strong>Arduino IDE</strong> : programmation ESP8266/NodeMCU</li>
<li><strong>Node-RED</strong> : outil de prototypage visuel</li>
<li><strong>ACME oneM2M CSE</strong> : implementation open-source du standard oneM2M</li>
<li><strong>Python</strong> : scripts d'interaction avec les API oneM2M</li>
<li><strong>cURL / Postman</strong> : test d'API RESTful</li>
</ul>

<p><strong>Ressources</strong> :</p>
<ul>
<li>MOOC oneM2M (planning et contenu en autonomie)</li>
<li>Sujets de TP detailles (MQTT, oneM2M, Node-RED)</li>
<li>Documentation Mosquitto, ACME CSE, Node-RED</li>
<li>Sujet et presentation du BE M2M</li>
</ul>

<h3 class="section-title">Methodologie d'apprentissage</h3>

<p><strong>Phase 1 : Comprendre les fondamentaux</strong> :<br>
Etudier l'architecture IoT, les modeles de communication (publish/subscribe vs request/response) et les contraintes specifiques des objets connectes.</p>

<p><strong>Phase 2 : Maitriser MQTT</strong> :<br>
Installer un broker, tester la communication en ligne de commande, puis programmer un microcontroleur pour publier et s'abonner a des topics.</p>

<p><strong>Phase 3 : Decouvrir oneM2M</strong> :<br>
Comprendre l'arbre de ressources, deployer un CSE, creer des Application Entities et des conteneurs via API REST.</p>

<p><strong>Phase 4 : Prototypage rapide</strong> :<br>
Utiliser Node-RED pour integrer tous les elements (capteurs, MQTT, dashboard, notifications) en un systeme fonctionnel.</p>

<p><strong>Phase 5 : Integration et projet</strong> :<br>
Combiner toutes les briques dans le BE M2M pour realiser une architecture IoT complete.</p>

<h3 class="section-title">Mon role et mes responsabilites</h3>

<p>Au cours de ce module, j'ai ete amene a :</p>
<ul>
<li>Installer et configurer le broker MQTT Mosquitto sur Linux</li>
<li>Programmer un NodeMCU/ESP8266 pour la publication de donnees de capteurs (luminosite, etat bouton) via MQTT</li>
<li>Deployer et interagir avec un CSE oneM2M (ACME) via des requetes HTTP RESTful en Python</li>
<li>Concevoir des flux Node-RED integrant reception MQTT, logique de controle, dashboard et notifications</li>
<li>Rediger des rapports techniques detaillant les architectures deployees et les resultats obtenus</li>
</ul>

<h3 class="section-title">Difficultes rencontrees</h3>

<p><strong>Configuration reseau du broker</strong> :<br>
La mise en place de Mosquitto avec les bons parametres d'ecoute et d'authentification a necessite plusieurs iterations pour fonctionner correctement avec le NodeMCU.</p>

<p><strong>Programmation ESP8266</strong> :<br>
L'integration de la bibliotheque ArduinoMqttClient avec la gestion WiFi sur le NodeMCU a demande une bonne comprehension du cycle de vie de la connexion.</p>

<p><strong>Standard oneM2M</strong> :<br>
La richesse du standard oneM2M (nombreux types de ressources, droits d'acces ACP, structure hierarchique) est intimidante au debut. La documentation du MOOC a ete essentielle pour progresser.</p>

<p><strong>Integration Node-RED</strong> :<br>
La coordination entre les noeuds MQTT, les fonctions JavaScript et le dashboard a necessite du temps de mise au point pour obtenir un systeme reactif et fiable.</p>

<hr>

<h2>PART C - Aspects Techniques Detailles</h2>

<h3 class="section-title">1. Protocole MQTT - Architecture et principes</h3>

<p>MQTT (Message Queuing Telemetry Transport) est un protocole de messagerie leger, concu pour les environnements contraints (bande passante limitee, ressources reduites). Il repose sur le modele <strong>publish/subscribe</strong> avec un intermediaire central appele <strong>broker</strong>.</p>

<p><strong>Architecture MQTT</strong> :</p>

<table>
<tr><th>Composant</th><th>Role</th><th>Description</th></tr>
<tr><td>Publisher</td><td>Emetteur</td><td>Publie des messages sur des topics</td></tr>
<tr><td>Subscriber</td><td>Recepteur</td><td>S'abonne a des topics pour recevoir les messages</td></tr>
<tr><td>Broker</td><td>Intermediaire</td><td>Gere la distribution des messages entre publishers et subscribers</td></tr>
<tr><td>Topic</td><td>Canal</td><td>Chaine hierarchique identifiant le sujet du message (ex: <code>sensor/temperature</code>)</td></tr>
<tr><td>Message</td><td>Donnee</td><td>Contenu publie sur un topic (payload)</td></tr>
</table>

<p><strong>Principes du publish/subscribe</strong> :</p>
<ul>
<li>Les publishers et subscribers sont <strong>decouplees</strong> : ils ne se connaissent pas directement</li>
<li>Le broker se charge du <strong>routage</strong> des messages selon les abonnements</li>
<li>Un publisher peut publier sur plusieurs topics</li>
<li>Un subscriber peut s'abonner a plusieurs topics avec des <strong>wildcards</strong> (<code>+</code> pour un niveau, <code>#</code> pour tous les sous-niveaux)</li>
</ul>

<p><strong>Fonctionnement detaille</strong> :</p>
<ol>
<li>Le subscriber s'abonne a un topic aupres du broker (ex: <code>insa/luminosity</code>)</li>
<li>Le publisher publie un message sur ce topic</li>
<li>Le broker transmet le message a tous les subscribers abonnes a ce topic</li>
<li>Le decoupage hierarchique des topics permet une organisation flexible (ex: <code>building1/floor2/room3/temperature</code>)</li>
</ol>

<div style="display: flex; justify-content: center; margin: 20px 0;">
    <img src="/img/BE_Middleware_IOT/mqtt.png" style="width: 50%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure : Architecture MQTT - Modele publish/subscribe avec broker central
</p>

<p><strong>Niveaux de QoS (Quality of Service)</strong> :</p>

<p>MQTT propose trois niveaux de qualite de service pour la livraison des messages :</p>

<table>
<tr><th>QoS</th><th>Nom</th><th>Garantie</th><th>Usage</th></tr>
<tr><td>0</td><td>At most once</td><td>Aucune garantie, "fire and forget"</td><td>Donnees non critiques, telemetrie frequente</td></tr>
<tr><td>1</td><td>At least once</td><td>Message livre au moins une fois (doublons possibles)</td><td>Donnees importantes, tolerance aux doublons</td></tr>
<tr><td>2</td><td>Exactly once</td><td>Message livre exactement une fois (handshake en 4 etapes)</td><td>Donnees critiques (facturation, commandes)</td></tr>
</table>

<p><strong>Autres fonctionnalites MQTT</strong> :</p>
<ul>
<li><strong>Retain</strong> : le broker conserve le dernier message d'un topic et l'envoie a tout nouveau subscriber</li>
<li><strong>Last Will and Testament (LWT)</strong> : message automatiquement publie par le broker si un client se deconnecte anormalement</li>
<li><strong>Clean Session</strong> : le client peut demander au broker de conserver ou non ses abonnements entre connexions</li>
<li><strong>Keep Alive</strong> : mecanisme de ping periodique pour detecter les deconnexions</li>
</ul>

<p><strong>Securite MQTT</strong> :</p>
<ul>
<li>Authentification par nom d'utilisateur / mot de passe</li>
<li>Chiffrement TLS/SSL pour la confidentialite des echanges</li>
<li>Listes de controle d'acces (ACL) pour restreindre l'acces aux topics</li>
<li>Port standard : 1883 (non chiffre), 8883 (TLS)</li>
</ul>

<p><strong>Protocole de transport</strong> :<br>
MQTT fonctionne au-dessus de <strong>TCP/IP</strong>, ce qui garantit une communication fiable avec un overhead minimal. La taille de l'en-tete MQTT est de seulement 2 octets minimum, ce qui le rend ideal pour les reseaux contraints.</p>

<h3 class="section-title">2. Installation et test du broker MQTT Mosquitto</h3>

<p>Mosquitto est l'implementation open-source de reference du protocole MQTT. J'ai installe et configure le broker sur un environnement Linux, puis teste la communication publish/subscribe en ligne de commande.</p>

<p><strong>Installation et demarrage</strong> :</p>

<pre><code class="language-bash"># Installation
sudo apt-get install mosquitto mosquitto-clients

# Demarrage du broker
mosquitto -v

# Abonnement a un topic
mosquitto_sub -h localhost -t "test/topic"

# Publication d'un message
mosquitto_pub -h localhost -t "test/topic" -m "Hello MQTT"</code></pre>

<div style="display: flex; justify-content: center; margin: 20px 0;">
    <img src="/img/BE_Middleware_IOT/mqtt_start.png" style="width: 60%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure : Demarrage du broker Mosquitto en mode verbose
</p>

<div style="display: flex; justify-content: center; margin: 20px 0;">
    <img src="/img/BE_Middleware_IOT/mqtt_sub_pub.png" style="width: 60%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure : Test publish/subscribe avec mosquitto_pub et mosquitto_sub
</p>

<p><strong>Configuration avancee du broker</strong> :</p>
<ul>
<li>Fichier de configuration : <code>/etc/mosquitto/mosquitto.conf</code></li>
<li>Definition des ports d'ecoute, des parametres d'authentification</li>
<li>Configuration des ACL pour controler l'acces aux topics</li>
<li>Activation du logging pour le debogage</li>
</ul>

<p>Les tests ont permis de valider le bon fonctionnement de la chaine de communication : le subscriber recoit instantanement les messages publies par le publisher via le broker, confirmant le modele asynchrone du publish/subscribe.</p>

<h3 class="section-title">3. Programmation NodeMCU/ESP8266 avec MQTT</h3>

<p>Le NodeMCU est une carte de developpement basee sur le microcontroleur <strong>ESP8266</strong>, integrant un module WiFi. J'ai programme cette carte pour qu'elle communique via MQTT avec le broker Mosquitto, en utilisant l'<strong>Arduino IDE</strong> et la bibliotheque <strong>ArduinoMqttClient</strong>.</p>

<p><strong>Caracteristiques du NodeMCU/ESP8266</strong> :</p>
<ul>
<li>Processeur 32 bits a 80 MHz</li>
<li>WiFi 802.11 b/g/n integre</li>
<li>GPIO, ADC, PWM, I2C, SPI</li>
<li>Programmable via Arduino IDE</li>
<li>Ideal pour le prototypage IoT</li>
</ul>

<p><strong>Fonctionnalites implementees</strong> :</p>
<ol>
<li><strong>Connexion WiFi</strong> : le NodeMCU se connecte au reseau WiFi local</li>
<li><strong>Connexion MQTT</strong> : etablissement de la connexion avec le broker Mosquitto</li>
<li><strong>Publication de l'etat du bouton</strong> : a chaque pression sur le bouton physique, publication de l'etat sur le topic <code>button/state</code></li>
<li><strong>Publication de la luminosite</strong> : lecture du capteur de luminosite (ADC) et publication sur le topic <code>light/state</code> a chaque pression du bouton</li>
<li><strong>Abonnement a des topics</strong> : reception de commandes depuis d'autres dispositifs</li>
</ol>

<p><strong>Extrait de la logique de programmation</strong> :</p>

<pre><code class="language-cpp">// Connexion WiFi
WiFi.begin(ssid, password);

// Connexion au broker MQTT
mqttClient.connect(broker, port);

// Publication sur topic
mqttClient.beginMessage("button/state");
mqttClient.print(buttonState);
mqttClient.endMessage();

// Lecture luminosite et publication
int luminosity = analogRead(A0);
mqttClient.beginMessage("light/state");
mqttClient.print(luminosity);
mqttClient.endMessage();</code></pre>

<div style="display: flex; justify-content: center; margin: 20px 0;">
    <img src="/img/BE_Middleware_IOT/nodemcu_app.png" style="width: 70%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure : Schema de l'application NodeMCU - publication des etats bouton et luminosite via MQTT
</p>

<p><strong>Points techniques importants</strong> :</p>
<ul>
<li>La gestion du <strong>debounce</strong> du bouton est essentielle pour eviter les publications multiples</li>
<li>La reconnexion automatique au broker en cas de perte de connexion WiFi ou MQTT garantit la robustesse du systeme</li>
<li>L'utilisation de QoS 1 pour les publications critiques assure la livraison des messages</li>
</ul>

<h3 class="section-title">4. Standard oneM2M - Architecture et ressources</h3>

<p>oneM2M est un standard international pour les communications M2M et l'IoT. Il definit une architecture de middleware universelle permettant l'interoperabilite entre differents systemes IoT, independamment du reseau sous-jacent.</p>

<p><strong>Architecture oneM2M</strong> :</p>

<table>
<tr><th>Composant</th><th>Sigle</th><th>Role</th></tr>
<tr><td>Common Services Entity</td><td>CSE</td><td>Fournit les services communs (enregistrement, decouverte, gestion des donnees, securite)</td></tr>
<tr><td>Application Entity</td><td>AE</td><td>Represente une application IoT qui interagit avec le CSE</td></tr>
<tr><td>Infrastructure Node</td><td>IN</td><td>Noeud serveur hebergeant le CSE principal</td></tr>
<tr><td>Middle Node</td><td>MN</td><td>Noeud intermediaire (passerelle)</td></tr>
<tr><td>Application Service Node</td><td>ASN</td><td>Noeud capteur/actionneur</td></tr>
</table>

<p><strong>Arbre de ressources oneM2M</strong> :</p>

<p>L'architecture oneM2M organise les donnees sous forme d'un <strong>arbre de ressources hierarchique</strong> :</p>

<pre><code>CSEBase (in-cse)
  |-- ACP (Access Control Policy)
  |-- AE (Application Entity - ex: Mon_AE)
  |     |-- Container (DATA)
  |     |     |-- ContentInstance (valeur capteur)
  |     |     |-- ContentInstance (valeur capteur)
  |     |-- Container (COMMAND)
  |           |-- ContentInstance (commande actionneur)
  |-- AE (Autre application)</code></pre>

<p><strong>Types de ressources principaux</strong> :</p>

<table>
<tr><th>Type</th><th>Code (ty)</th><th>Description</th></tr>
<tr><td>ACP</td><td>1</td><td>Politique de controle d'acces (droits CRUD + Notify + Discovery)</td></tr>
<tr><td>AE</td><td>2</td><td>Application Entity - represente une application</td></tr>
<tr><td>Container</td><td>3</td><td>Conteneur de donnees (structure hierarchique)</td></tr>
<tr><td>ContentInstance</td><td>4</td><td>Instance de contenu (donnee individuelle)</td></tr>
<tr><td>Subscription</td><td>23</td><td>Abonnement pour notification automatique</td></tr>
</table>

<p><strong>Operations CRUD via API REST</strong> :</p>

<p>L'interaction avec le CSE se fait par des requetes HTTP RESTful :</p>

<pre><code class="language-python"># Creation d'une Application Entity
POST /~/in-cse/in-name
Headers: X-M2M-Origin: '', Content-Type: application/json;ty=2
Body: {"m2m:ae": {"api": "app.iot", "rr": "true", "rn": "Mon_AE"}}

# Creation d'un Container
POST /~/in-cse/in-name/Mon_AE
Headers: X-M2M-Origin: admin:admin, Content-Type: application/json;ty=3
Body: {"m2m:cnt": {"rn": "DATA"}}

# Creation d'un ContentInstance
POST /~/in-cse/in-name/Mon_AE/DATA
Headers: X-M2M-Origin: admin:admin, Content-Type: application/json;ty=4
Body: {"m2m:cin": {"con": "42"}}

# Recuperation du dernier contenu
GET /~/in-cse/in-name/Mon_AE/DATA/la
Headers: X-M2M-Origin: admin:admin, Accept: application/json</code></pre>

<p><strong>Droits d'acces (ACP)</strong> :</p>

<p>Les ACP definissent les permissions sur les ressources :</p>

<table>
<tr><th>Valeur</th><th>Permission</th></tr>
<tr><td>1</td><td>CREATE</td></tr>
<tr><td>2</td><td>RETRIEVE</td></tr>
<tr><td>4</td><td>UPDATE</td></tr>
<tr><td>8</td><td>DELETE</td></tr>
<tr><td>16</td><td>NOTIFY</td></tr>
<tr><td>32</td><td>DISCOVERY</td></tr>
<tr><td>63</td><td>Toutes les permissions</td></tr>
</table>

<p><strong>ACME CSE</strong> :</p>

<p>Pour les travaux pratiques, nous avons utilise <strong>ACME</strong>, une implementation open-source du standard oneM2M developpee pour la recherche et l'enseignement. ACME fournit un CSE complet avec interface web, support HTTP/MQTT/CoAP, et une base de donnees locale.</p>

<h3 class="section-title">5. Prototypage rapide avec Node-RED</h3>

<p>Node-RED est un outil de programmation visuelle base sur Node.js, concu pour le prototypage rapide d'applications IoT. Il permet de creer des <strong>flux de donnees</strong> en connectant des noeuds graphiques, simplifiant considerablement le developpement et l'integration de systemes IoT.</p>

<p><strong>Principes de Node-RED</strong> :</p>
<ul>
<li><strong>Flux (flows)</strong> : enchainement de noeuds connectes representant le traitement des donnees</li>
<li><strong>Noeuds (nodes)</strong> : blocs fonctionnels (entree, traitement, sortie)</li>
<li><strong>Messages</strong> : objets JSON circulant entre les noeuds (<code>msg.payload</code>, <code>msg.topic</code>)</li>
<li><strong>Interface web</strong> : editeur visuel accessible via navigateur</li>
<li><strong>Extensible</strong> : milliers de noeuds communautaires installables via npm</li>
</ul>

<p><strong>Types de noeuds utilises</strong> :</p>

<table>
<tr><th>Categorie</th><th>Noeuds</th><th>Fonction</th></tr>
<tr><td>Entree</td><td>mqtt in, inject</td><td>Reception de messages MQTT, injection de donnees</td></tr>
<tr><td>Traitement</td><td>switch, function, change</td><td>Logique conditionnelle, transformation de donnees</td></tr>
<tr><td>Sortie</td><td>mqtt out, debug, email</td><td>Publication MQTT, affichage de debug, envoi email</td></tr>
<tr><td>Dashboard</td><td>gauge, chart, button, text</td><td>Composants d'interface utilisateur</td></tr>
</table>

<div style="display: flex; justify-content: center; margin: 20px 0;">
    <img src="/img/BE_Middleware_IOT/nodered.png" style="width: 70%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure : Flux Node-RED integrant reception MQTT, logique de controle et actionneurs
</p>

<p><strong>a. Verification de la connectivite MQTT</strong></p>

<p>La premiere etape a consiste a ajouter un noeud <strong>mqtt in</strong> dans Node-RED, configure pour se connecter au broker Mosquitto et s'abonner au topic <code>insa/luminosity</code>. Le noeud <strong>debug</strong> a permis de confirmer la bonne reception des valeurs envoyees par le NodeMCU.</p>

<p><strong>b. Gestion des capteurs et actionneurs</strong></p>

<p>Un flux a ete cree pour simuler la logique de controle d'un systeme d'eclairage automatique :</p>
<ul>
<li>Un capteur de luminosite publie des valeurs sur MQTT</li>
<li>Un noeud <strong>switch</strong> evalue la valeur recue :
  <ul>
  <li>Luminosite &gt; 50 : envoi de la commande LED ON</li>
  <li>Luminosite &lt;= 50 : envoi de la commande LED OFF</li>
  </ul>
</li>
<li>Le noeud <strong>mqtt out</strong> publie la commande sur le topic de l'actionneur</li>
</ul>

<p>Cette logique illustre le patron de base d'un systeme IoT reactif : capteur &rarr; traitement &rarr; actionneur.</p>

<p><strong>c. Dashboard de visualisation et controle</strong></p>

<p>Grace au module <code>node-red-dashboard</code>, un tableau de bord interactif a ete cree pour :</p>
<ul>
<li><strong>Visualiser</strong> les donnees des capteurs en temps reel (graphiques, jauges)</li>
<li><strong>Controler</strong> les actionneurs (boutons ON/OFF pour les LEDs)</li>
<li><strong>Surveiller</strong> l'etat du systeme (indicateurs visuels)</li>
</ul>

<div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; margin: 20px 0;">
    <img src="/img/BE_Middleware_IOT/nodered_dashboard.png" style="width: 30%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <img src="/img/BE_Middleware_IOT/nodered_led.png" style="width: 55%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure : Dashboard Node-RED - visualisation capteurs et controle LED
</p>

<p><strong>d. Notifications email</strong></p>

<p>Le module <code>node-red-node-email</code> a ete integre pour envoyer des alertes automatiques par email lors de :</p>
<ul>
<li>Changement d'etat du switch (ON/OFF)</li>
<li>Depassement de seuil de luminosite</li>
<li>Detection d'anomalies (valeurs aberrantes)</li>
</ul>

<p>Ce mecanisme de notification proactive est essentiel dans les systemes IoT pour assurer une reaction rapide aux evenements critiques.</p>

<h3 class="section-title">6. Comparaison des protocoles IoT : HTTP vs MQTT vs CoAP</h3>

<p>Le choix du protocole de communication est une decision architecturale majeure dans tout projet IoT. Chaque protocole presente des avantages et contraintes specifiques.</p>

<table>
<tr><th>Critere</th><th>HTTP</th><th>MQTT</th><th>CoAP</th></tr>
<tr><td>Modele</td><td>Request/Response</td><td>Publish/Subscribe</td><td>Request/Response</td></tr>
<tr><td>Transport</td><td>TCP</td><td>TCP</td><td>UDP</td></tr>
<tr><td>Overhead</td><td>Eleve (en-tetes texte)</td><td>Faible (2 octets min)</td><td>Tres faible (4 octets)</td></tr>
<tr><td>QoS</td><td>Non natif</td><td>3 niveaux (0, 1, 2)</td><td>Confirmable/Non-confirmable</td></tr>
<tr><td>Decouverte</td><td>Non</td><td>Non</td><td>Oui (ressource .well-known/core)</td></tr>
<tr><td>Observe</td><td>Non</td><td>Oui (subscribe)</td><td>Oui (option Observe)</td></tr>
<tr><td>Securite</td><td>TLS</td><td>TLS</td><td>DTLS</td></tr>
<tr><td>Usage typique</td><td>API web, REST</td><td>Telemetrie, notification</td><td>Objets tres contraints</td></tr>
<tr><td>Consommation</td><td>Elevee</td><td>Moderee</td><td>Faible</td></tr>
<tr><td>Latence</td><td>Moderee</td><td>Faible</td><td>Tres faible</td></tr>
</table>

<p><strong>Quand utiliser quel protocole</strong> :</p>
<ul>
<li><strong>HTTP</strong> : interactions ponctuelles, API REST, integration avec le web existant, oneM2M</li>
<li><strong>MQTT</strong> : telemetrie continue, notifications temps reel, communication entre de nombreux devices</li>
<li><strong>CoAP</strong> : objets a tres faibles ressources (capteurs sur batterie), reseaux 6LoWPAN, communication directe device-to-device</li>
</ul>

<h3 class="section-title">7. API RESTful pour l'IoT</h3>

<p>L'architecture REST (Representational State Transfer) est au coeur de l'IoT moderne, notamment dans le standard oneM2M. Les principes REST appliques a l'IoT :</p>

<p><strong>Principes REST</strong> :</p>
<ul>
<li><strong>Ressources identifiees par URI</strong> : chaque capteur, actionneur ou donnee est une ressource adressable</li>
<li><strong>Operations CRUD via verbes HTTP</strong> :
  <ul>
  <li>GET : lire une ressource (ex: valeur capteur)</li>
  <li>POST : creer une ressource (ex: nouvelle ContentInstance)</li>
  <li>PUT : mettre a jour une ressource</li>
  <li>DELETE : supprimer une ressource</li>
  </ul>
</li>
<li><strong>Representations</strong> : JSON ou XML pour encoder les donnees</li>
<li><strong>Sans etat (stateless)</strong> : chaque requete contient toute l'information necessaire</li>
</ul>

<p><strong>Application au standard oneM2M</strong> :<br>
Dans oneM2M, l'arbre de ressources est accessible via des URL RESTful. Les en-tetes HTTP specifiques (<code>X-M2M-Origin</code>, <code>Content-Type</code> avec type de ressource) permettent au CSE d'identifier l'appelant et le type de creation demande.</p>

<h3 class="section-title">8. Pile protocolaire IoT</h3>

<p>L'IoT utilise une pile protocolaire adaptee aux contraintes des objets connectes :</p>

<table>
<tr><th>Couche</th><th>Protocoles standard</th><th>Protocoles IoT</th></tr>
<tr><td>Application</td><td>HTTP, FTP</td><td>MQTT, CoAP, AMQP, oneM2M</td></tr>
<tr><td>Transport</td><td>TCP, UDP</td><td>TCP (MQTT), UDP (CoAP)</td></tr>
<tr><td>Reseau</td><td>IPv4, IPv6</td><td>6LoWPAN, RPL</td></tr>
<tr><td>Liaison</td><td>Ethernet, WiFi</td><td>IEEE 802.15.4, BLE, LoRa, Sigfox</td></tr>
<tr><td>Physique</td><td>Cables, ondes</td><td>RF sub-GHz, 2.4 GHz</td></tr>
</table>

<p><strong>Specificites de la pile IoT</strong> :</p>
<ul>
<li><strong>6LoWPAN</strong> : adaptation d'IPv6 pour reseaux de capteurs a faible puissance (compression d'en-tetes)</li>
<li><strong>RPL</strong> : protocole de routage pour reseaux de capteurs (arbre DODAG)</li>
<li><strong>IEEE 802.15.4</strong> : couche liaison pour reseaux personnels sans fil a faible consommation</li>
<li>Les middlewares comme oneM2M se situent au niveau applicatif et sont <strong>independants du reseau sous-jacent</strong></li>
</ul>

<h3 class="section-title">9. Patrons de communication M2M</h3>

<p>Les communications Machine-to-Machine suivent plusieurs patrons architecturaux :</p>

<p><strong>1. Publish/Subscribe (MQTT)</strong> :</p>
<ul>
<li>Communication asynchrone via broker</li>
<li>Decoupage spatial (publisher et subscriber ne se connaissent pas)</li>
<li>Decoupage temporel (pas besoin d'etre connecte simultanement grace au retain)</li>
<li>Ideal pour : telemetrie, notification d'evenements, distribution de donnees a N recepteurs</li>
</ul>

<p><strong>2. Request/Response (HTTP, CoAP)</strong> :</p>
<ul>
<li>Communication synchrone client/serveur</li>
<li>Le client initie la requete, le serveur repond</li>
<li>Ideal pour : lecture ponctuelle, commande d'actionneur, API REST</li>
</ul>

<p><strong>3. Observer (CoAP Observe, oneM2M Subscription)</strong> :</p>
<ul>
<li>Le client s'enregistre pour etre notifie des changements</li>
<li>Le serveur envoie des notifications a chaque modification</li>
<li>Ideal pour : surveillance continue, tableaux de bord temps reel</li>
</ul>

<p><strong>4. Pipeline / Data Flow (Node-RED)</strong> :</p>
<ul>
<li>Les donnees traversent une chaine de traitements</li>
<li>Chaque noeud transforme ou filtre les donnees</li>
<li>Ideal pour : ETL IoT, traitement de flux, prototypage</li>
</ul>

<h3 class="section-title">10. Prototypage rapide avec Node-RED - Approfondissement</h3>

<p>Node-RED se revele un outil extremement puissant pour le prototypage IoT grace a plusieurs caracteristiques avancees :</p>

<p><strong>Flux JSON exportable</strong> :<br>
Les flux Node-RED sont serialises en JSON, permettant le versionnement (Git), le partage et le deploiement automatise. Lors du TP, nous avons exporte notre configuration dans le fichier <code>Boukouiss_Chanfreau_Node-Red.json</code>.</p>

<p><strong>Noeuds personnalises (function)</strong> :<br>
Le noeud <code>function</code> permet d'ecrire du code JavaScript pour des traitements complexes :</p>

<pre><code class="language-javascript">// Exemple : transformation de donnees capteur
var luminosity = msg.payload;
if (luminosity > 50) {
    msg.payload = "ON";
    msg.topic = "led/command";
} else {
    msg.payload = "OFF";
    msg.topic = "led/command";
}
return msg;</code></pre>

<p><strong>Integration multi-protocole</strong> :<br>
Node-RED supporte nativement MQTT, HTTP, WebSocket, TCP, UDP et peut etre etendu pour supporter CoAP, oneM2M, bases de donnees (InfluxDB, MongoDB), services cloud (AWS IoT, Azure IoT Hub).</p>

<p><strong>Avantages pour le prototypage IoT</strong> :</p>
<ul>
<li>Developpement visuel accelerant la mise en oeuvre</li>
<li>Test et debogage en temps reel (noeud debug)</li>
<li>Dashboard integre pour la visualisation</li>
<li>Modification a chaud sans redemarrage</li>
<li>Grande communaute et ecosysteme de noeuds</li>
</ul>

<hr>

<h2>PART D - Analyse Reflexive et Perspectives</h2>

<h3 class="section-title">Competences acquises</h3>

<p><strong>Maitrise des protocoles IoT</strong> :<br>
Comprehension approfondie de MQTT (publish/subscribe, QoS, broker), des API RESTful pour oneM2M, et des principes de CoAP. Capacite a choisir le protocole adapte selon les contraintes du projet.</p>

<p><strong>Programmation embarquee IoT</strong> :<br>
Competence pour programmer un ESP8266/NodeMCU et l'integrer dans une architecture MQTT : connexion WiFi, publication/abonnement, gestion des capteurs et actionneurs.</p>

<p><strong>Architecture middleware M2M</strong> :<br>
Comprehension du standard oneM2M, de l'arbre de ressources, des ACP, et de l'interaction avec un CSE via API REST. Capacite a deployer et configurer une infrastructure oneM2M.</p>

<p><strong>Prototypage rapide</strong> :<br>
Maitrise de Node-RED pour concevoir des flux IoT complets, integrant capture de donnees, logique de traitement, dashboard de visualisation et systemes de notification.</p>

<p><strong>Integration systeme</strong> :<br>
Capacite a combiner toutes les briques (capteurs, broker MQTT, CSE oneM2M, Node-RED, dashboard) dans une architecture IoT coherente et fonctionnelle.</p>

<h3 class="section-title">Points cles a retenir</h3>

<p><strong>1. MQTT est le protocole de reference pour l'IoT</strong> :<br>
Sa legerete, son modele publish/subscribe et ses niveaux de QoS en font le choix privilegie pour la telemetrie et la communication entre objets connectes.</p>

<p><strong>2. oneM2M standardise l'interoperabilite M2M</strong> :<br>
Ce standard international fournit une couche d'abstraction au-dessus des protocoles de transport, permettant l'interoperabilite entre systemes heterogenes.</p>

<p><strong>3. Node-RED accelere considerablement le prototypage</strong> :<br>
La programmation visuelle permet de passer rapidement de l'idee au prototype fonctionnel, ce qui est crucial dans les projets IoT ou l'iteration rapide est essentielle.</p>

<p><strong>4. Le choix du protocole depend du cas d'usage</strong> :<br>
HTTP pour les API web, MQTT pour la telemetrie temps reel, CoAP pour les objets tres contraints. Il n'existe pas de solution universelle.</p>

<p><strong>5. La securite IoT est un enjeu majeur</strong> :<br>
L'authentification, le chiffrement (TLS/DTLS) et le controle d'acces doivent etre integres des la conception de l'architecture.</p>

<h3 class="section-title">Auto-evaluation</h3>

<p>Ce cours a constitue ma premiere experience approfondie avec les protocoles IoT comme MQTT et le standard oneM2M. J'ai trouve ces technologies relativement accessibles grace aux nombreuses bibliotheques existantes et a la documentation disponible. La progression pedagogique des TP (de la ligne de commande Mosquitto a l'application Node-RED complete) a permis une montee en competence progressive et solide.</p>

<p>La mise en oeuvre pratique m'a permis de comprendre l'utilite concrete de ces concepts. J'ai par la suite reutilise certains de ces outils dans notre <strong>projet innovant</strong> pour mettre en place une communication efficace entre dispositifs, ce qui confirme la pertinence de cet enseignement.</p>

<p>La richesse du standard oneM2M m'a impressionne : la structure hierarchique des ressources, le systeme de droits d'acces et les mecanismes de notification permettent de construire des architectures IoT robustes et interoperables. Cependant, cette richesse implique une courbe d'apprentissage non negligeable.</p>

<h3 class="section-title">Mon avis</h3>

<p>Ce cours a ete l'un de mes favoris du semestre car il combine parfaitement les aspects <strong>materiel et logiciel</strong>. En tant qu'aspirant ingenieur en systemes embarques, cette association entre programmation de microcontroleurs et architectures logicielles middleware correspond exactement a mon profil de competences vise.</p>

<p><strong>Points forts</strong> :</p>
<ul>
<li>Progression pedagogique exemplaire : MQTT en CLI, puis ESP8266, puis oneM2M, puis Node-RED</li>
<li>Equilibre theorie/pratique avec des TP concrets et motivants</li>
<li>Outils open-source accessibles pour continuer a pratiquer</li>
<li>Lien direct avec les besoins de l'industrie IoT</li>
</ul>

<p><strong>Points a ameliorer</strong> :</p>
<ul>
<li>Plus de temps sur oneM2M (complexite du standard)</li>
<li>Introduction de CoAP en pratique (pas seulement en theorie)</li>
<li>Aspects securite plus approfondis (TLS, certificats)</li>
<li>Scalabilite des architectures (clusters de brokers, load balancing)</li>
</ul>

<p>La demarche progressive des labs a rendu l'apprentissage a la fois agreable et tres formateur. Partir de la communication MQTT basique en ligne de commande, evoluer vers la programmation Arduino avec la bibliotheque MQTT, puis integrer le tout avec Node-RED offre une vision complete de la chaine IoT. C'est exactement le type de cours qui prepare a des projets professionnels concrets.</p>

<h3 class="section-title">Applications professionnelles</h3>

<p><strong>Ingenieur IoT</strong> :</p>
<ul>
<li>Concevoir des architectures de communication pour objets connectes</li>
<li>Deployer et administrer des brokers MQTT a l'echelle</li>
<li>Integrer des capteurs et actionneurs dans des plateformes IoT</li>
</ul>

<p><strong>Ingenieur systemes embarques</strong> :</p>
<ul>
<li>Programmer des microcontroleurs communicants (ESP8266, ESP32, STM32)</li>
<li>Implementer des protocoles IoT sur des systemes contraints</li>
<li>Optimiser la consommation energetique des communications</li>
</ul>

<p><strong>Architecte solutions M2M</strong> :</p>
<ul>
<li>Concevoir des plateformes interoperables basees sur oneM2M</li>
<li>Definir les architectures middleware pour systemes industriels</li>
<li>Assurer la scalabilite et la securite des infrastructures</li>
</ul>

<p><strong>Liens avec les autres cours</strong> :</p>
<ul>
<li><a href="./cloud-edge.html">Cloud et Edge Computing - S9</a> : deploiement des brokers et CSE</li>
<li><a href="./security-object.html">Security for Connected Objects - S9</a> : securisation MQTT/TLS</li>
<li><a href="./wireless-sensors.html">Wireless Sensors Networks - S9</a> : couches basses des capteurs</li>
<li><a href="./service-oriented-architecture.html">Service Oriented Architecture - S9</a> : API REST, microservices</li>
</ul>

<hr>

<h2>Documents de Cours</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">Planning MOOC oneM2M</span>
        <span class="lang-en">oneM2M MOOC Planning</span>
      </h4>
      <p>
        <span class="lang-fr">Planning et contenu du MOOC oneM2M suivi en autonomie : introduction au standard, architecture, types de ressources.</span>
        <span class="lang-en">Planning and content of the self-paced oneM2M MOOC: introduction to the standard, architecture, resource types.</span>
      </p>
      <embed src="/cours-pdf/S9/Middleware/MOOC_oneM2M_planning.pdf" type="application/pdf" width="100%" height="600px" />
      <p><a href="/cours-pdf/S9/Middleware/MOOC_oneM2M_planning.pdf" target="_blank">
        <span class="lang-fr">Telecharger</span>
        <span class="lang-en">Download</span>
      </a></p>
    </div>
  </div>
</div>

<hr>

<h2>Rapports et Projets</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">Rapport Middleware for IoT - BE</span>
        <span class="lang-en">Middleware for IoT Report - Design Project</span>
      </h4>
      <p>
        <span class="lang-fr">Rapport complet du bureau d'etudes : architecture IoT deployee, integration MQTT, oneM2M et Node-RED, resultats experimentaux.</span>
        <span class="lang-en">Complete design project report: deployed IoT architecture, MQTT integration, oneM2M and Node-RED, experimental results.</span>
      </p>
      <embed src="/file/reports/S9/Report_Middleware_For_IoT.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/file/reports/S9/Report_Middleware_For_IoT.pdf" target="_blank">
        <span class="lang-fr">Telecharger le rapport BE</span>
        <span class="lang-en">Download the design project report</span>
      </a></p>
    </div>
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">Rapport TP1-2 : MQTT et NodeMCU</span>
        <span class="lang-en">Lab 1-2 Report: MQTT and NodeMCU</span>
      </h4>
      <p>
        <span class="lang-fr">Rapport des travaux pratiques 1 et 2 : installation Mosquitto, communication publish/subscribe, programmation ESP8266.</span>
        <span class="lang-en">Lab sessions 1 and 2 report: Mosquitto installation, publish/subscribe communication, ESP8266 programming.</span>
      </p>
      <embed src="/file/reports/S9/Report_Middleware_TP1-2.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/file/reports/S9/Report_Middleware_TP1-2.pdf" target="_blank">
        <span class="lang-fr">Telecharger le rapport TP1-2</span>
        <span class="lang-en">Download the Lab 1-2 report</span>
      </a></p>
    </div>
  </div>
</div>

<div style="text-align: center; margin-top: 20px;">
    <a href="/img/BE_Middleware_IOT/Lab_Subject_middleware.pdf" target="_blank">
        <span class="lang-fr">Ouvrir le sujet de TP</span>
        <span class="lang-en">Open the lab subject</span>
    </a>
</div>

<hr>
<p><em>Cours suivi en 2024-2025 a l'INSA Toulouse, Departement Genie Electrique et Informatique, specialite ISS (Innovative Smart Systems).</em></p>

</div>

<div class="lang-en">

<h1>Middleware for IoT / M2M - Semester 9</h1>

<p><strong>Academic year</strong>: 2024-2025<br>
<strong>Instructor</strong>: T. Monteil (LAAS-CNRS)<br>
<strong>ECTS</strong>: 2.5<br>
<strong>Category</strong>: IoT, Communication Protocols, Middleware</p>

<p><strong>Related courses</strong>:</p>
<ul>
<li><a href="./security-object.html">Security for Connected Objects - S9</a> - IoT security</li>
<li><a href="./cloud-edge.html">Cloud &amp; Edge Computing - S9</a> - IoT architectures</li>
<li><a href="./wireless-sensors.html">Wireless Sensors Networks - S9</a> - Sensor networks</li>
</ul>

<hr>

<h2>PART A - General Presentation</h2>

<h3 class="section-title">Overview</h3>

<p>The "Middleware for IoT / M2M" course covers middleware software architectures and communication protocols dedicated to the Internet of Things (IoT) and Machine-to-Machine (M2M) communications. It covers the entire chain, from lightweight messaging protocols such as MQTT to resource management standards like oneM2M, including rapid prototyping of IoT applications with Node-RED.</p>

<p>The objective is to train engineers capable of designing, deploying and integrating complete IoT systems, with mastery of communication protocols adapted to connected object constraints (limited bandwidth, energy consumption, reliability).</p>

<p><strong>Learning objectives</strong>:</p>
<ul>
<li>Understand the main Internet of Things standards (MQTT, oneM2M, CoAP)</li>
<li>Deploy and configure IoT architectures with MQTT broker and oneM2M CSE</li>
<li>Program microcontrollers (NodeMCU/ESP8266) to communicate via MQTT</li>
<li>Design IoT applications with Node-RED (rapid prototyping)</li>
<li>Compare and choose protocols suited to IoT use cases (HTTP vs MQTT vs CoAP)</li>
<li>Integrate sensors, actuators and dashboards into a complete IoT architecture</li>
<li>Analyze the security, scalability and interoperability challenges of M2M systems</li>
</ul>

<h3 class="section-title">Position in the curriculum</h3>

<p>This module builds on previously acquired foundations:</p>
<ul>
<li><strong>Networking (S5-S8)</strong>: OSI model, TCP/IP, HTTP, sockets</li>
<li><strong>Microcontrollers (S5-S7)</strong>: embedded programming, Arduino</li>
<li><strong>Operating Systems</strong>: Linux, Python scripts</li>
</ul>

<p>It prepares for and connects to:</p>
<ul>
<li><strong>Cloud and Edge Computing (S9)</strong>: deployment of distributed architectures</li>
<li><strong>Security for Connected Objects (S9)</strong>: securing IoT communications</li>
<li><strong>Wireless Sensors Networks (S9)</strong>: physical and link layers of sensors</li>
<li><strong>Innovative Project (S9)</strong>: integration of IoT protocols in a real project</li>
</ul>

<hr>

<h2>PART B - Experience and Context</h2>

<h3 class="section-title">Organization and resources</h3>

<p>The module combined theoretical lectures and progressive hands-on lab work:</p>

<p><strong>Lectures</strong>:</p>
<ul>
<li>IoT architecture and protocol stack</li>
<li>MQTT protocol: principles, QoS, topics, retain, last will</li>
<li>oneM2M standard: architecture, resources, CSE, AE</li>
<li>oneM2M MOOC (self-paced training)</li>
<li>Comparison of IoT protocols (HTTP, MQTT, CoAP, AMQP)</li>
<li>M2M communication patterns (publish/subscribe, request/response)</li>
</ul>

<p><strong>Lab sessions</strong>:</p>
<ul>
<li><strong>Lab 1-2</strong>: Installation and configuration of the Mosquitto MQTT broker, publish/subscribe communication, NodeMCU/ESP8266 programming with ArduinoMqttClient</li>
<li><strong>Lab 3</strong>: oneM2M standard with ACME CSE, resource creation (AE, Container, ContentInstance) via RESTful API, Python script simple_om2m.py</li>
<li><strong>Lab 4</strong>: Rapid prototyping with Node-RED, MQTT integration, dashboard, sensor and actuator management, email notifications</li>
</ul>

<p><strong>Design Project (BE)</strong>:</p>
<ul>
<li>BE M2M project: implementation of a complete M2M architecture integrating MQTT, oneM2M and Node-RED</li>
</ul>

<p><strong>Tools used</strong>:</p>
<ul>
<li><strong>Mosquitto</strong>: open-source MQTT broker</li>
<li><strong>Arduino IDE</strong>: ESP8266/NodeMCU programming</li>
<li><strong>Node-RED</strong>: visual prototyping tool</li>
<li><strong>ACME oneM2M CSE</strong>: open-source implementation of the oneM2M standard</li>
<li><strong>Python</strong>: scripts for interacting with oneM2M APIs</li>
<li><strong>cURL / Postman</strong>: RESTful API testing</li>
</ul>

<p><strong>Resources</strong>:</p>
<ul>
<li>oneM2M MOOC (self-paced planning and content)</li>
<li>Detailed lab subjects (MQTT, oneM2M, Node-RED)</li>
<li>Mosquitto, ACME CSE, Node-RED documentation</li>
<li>BE M2M subject and presentation</li>
</ul>

<h3 class="section-title">Learning methodology</h3>

<p><strong>Phase 1: Understanding the fundamentals</strong>:<br>
Study the IoT architecture, communication models (publish/subscribe vs request/response) and the specific constraints of connected objects.</p>

<p><strong>Phase 2: Mastering MQTT</strong>:<br>
Install a broker, test communication via command line, then program a microcontroller to publish and subscribe to topics.</p>

<p><strong>Phase 3: Discovering oneM2M</strong>:<br>
Understand the resource tree, deploy a CSE, create Application Entities and containers via REST API.</p>

<p><strong>Phase 4: Rapid prototyping</strong>:<br>
Use Node-RED to integrate all elements (sensors, MQTT, dashboard, notifications) into a functional system.</p>

<p><strong>Phase 5: Integration and project</strong>:<br>
Combine all building blocks in the BE M2M to build a complete IoT architecture.</p>

<h3 class="section-title">My role and responsibilities</h3>

<p>During this module, I was responsible for:</p>
<ul>
<li>Installing and configuring the Mosquitto MQTT broker on Linux</li>
<li>Programming a NodeMCU/ESP8266 for sensor data publishing (luminosity, button state) via MQTT</li>
<li>Deploying and interacting with a oneM2M CSE (ACME) via HTTP RESTful requests in Python</li>
<li>Designing Node-RED flows integrating MQTT reception, control logic, dashboard and notifications</li>
<li>Writing technical reports detailing the deployed architectures and results obtained</li>
</ul>

<h3 class="section-title">Challenges encountered</h3>

<p><strong>Broker network configuration</strong>:<br>
Setting up Mosquitto with the correct listening and authentication parameters required several iterations to work properly with the NodeMCU.</p>

<p><strong>ESP8266 programming</strong>:<br>
Integrating the ArduinoMqttClient library with WiFi management on the NodeMCU required a solid understanding of the connection lifecycle.</p>

<p><strong>oneM2M standard</strong>:<br>
The richness of the oneM2M standard (numerous resource types, ACP access rights, hierarchical structure) is intimidating at first. The MOOC documentation was essential to make progress.</p>

<p><strong>Node-RED integration</strong>:<br>
Coordinating between MQTT nodes, JavaScript functions and the dashboard required fine-tuning time to achieve a responsive and reliable system.</p>

<hr>

<h2>PART C - Detailed Technical Aspects</h2>

<h3 class="section-title">1. MQTT Protocol - Architecture and principles</h3>

<p>MQTT (Message Queuing Telemetry Transport) is a lightweight messaging protocol designed for constrained environments (limited bandwidth, reduced resources). It relies on the <strong>publish/subscribe</strong> model with a central intermediary called a <strong>broker</strong>.</p>

<p><strong>MQTT Architecture</strong>:</p>

<table>
<tr><th>Component</th><th>Role</th><th>Description</th></tr>
<tr><td>Publisher</td><td>Sender</td><td>Publishes messages on topics</td></tr>
<tr><td>Subscriber</td><td>Receiver</td><td>Subscribes to topics to receive messages</td></tr>
<tr><td>Broker</td><td>Intermediary</td><td>Manages message distribution between publishers and subscribers</td></tr>
<tr><td>Topic</td><td>Channel</td><td>Hierarchical string identifying the message subject (e.g.: <code>sensor/temperature</code>)</td></tr>
<tr><td>Message</td><td>Data</td><td>Content published on a topic (payload)</td></tr>
</table>

<p><strong>Publish/subscribe principles</strong>:</p>
<ul>
<li>Publishers and subscribers are <strong>decoupled</strong>: they do not know each other directly</li>
<li>The broker handles message <strong>routing</strong> according to subscriptions</li>
<li>A publisher can publish on multiple topics</li>
<li>A subscriber can subscribe to multiple topics with <strong>wildcards</strong> (<code>+</code> for one level, <code>#</code> for all sub-levels)</li>
</ul>

<p><strong>Detailed operation</strong>:</p>
<ol>
<li>The subscriber subscribes to a topic on the broker (e.g.: <code>insa/luminosity</code>)</li>
<li>The publisher publishes a message on that topic</li>
<li>The broker forwards the message to all subscribers subscribed to that topic</li>
<li>The hierarchical topic structure allows flexible organization (e.g.: <code>building1/floor2/room3/temperature</code>)</li>
</ol>

<div style="display: flex; justify-content: center; margin: 20px 0;">
    <img src="/img/BE_Middleware_IOT/mqtt.png" style="width: 50%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure: MQTT Architecture - Publish/subscribe model with central broker
</p>

<p><strong>QoS Levels (Quality of Service)</strong>:</p>

<p>MQTT offers three quality of service levels for message delivery:</p>

<table>
<tr><th>QoS</th><th>Name</th><th>Guarantee</th><th>Usage</th></tr>
<tr><td>0</td><td>At most once</td><td>No guarantee, "fire and forget"</td><td>Non-critical data, frequent telemetry</td></tr>
<tr><td>1</td><td>At least once</td><td>Message delivered at least once (duplicates possible)</td><td>Important data, duplicate tolerance</td></tr>
<tr><td>2</td><td>Exactly once</td><td>Message delivered exactly once (4-step handshake)</td><td>Critical data (billing, commands)</td></tr>
</table>

<p><strong>Other MQTT features</strong>:</p>
<ul>
<li><strong>Retain</strong>: the broker keeps the last message of a topic and sends it to any new subscriber</li>
<li><strong>Last Will and Testament (LWT)</strong>: message automatically published by the broker if a client disconnects abnormally</li>
<li><strong>Clean Session</strong>: the client can ask the broker to retain or discard its subscriptions between connections</li>
<li><strong>Keep Alive</strong>: periodic ping mechanism to detect disconnections</li>
</ul>

<p><strong>MQTT Security</strong>:</p>
<ul>
<li>Username/password authentication</li>
<li>TLS/SSL encryption for exchange confidentiality</li>
<li>Access Control Lists (ACL) to restrict topic access</li>
<li>Standard port: 1883 (unencrypted), 8883 (TLS)</li>
</ul>

<p><strong>Transport protocol</strong>:<br>
MQTT operates on top of <strong>TCP/IP</strong>, which ensures reliable communication with minimal overhead. The MQTT header size is only 2 bytes minimum, making it ideal for constrained networks.</p>

<h3 class="section-title">2. Installing and testing the Mosquitto MQTT broker</h3>

<p>Mosquitto is the reference open-source implementation of the MQTT protocol. I installed and configured the broker on a Linux environment, then tested publish/subscribe communication via the command line.</p>

<p><strong>Installation and startup</strong>:</p>

<pre><code class="language-bash"># Installation
sudo apt-get install mosquitto mosquitto-clients

# Demarrage du broker
mosquitto -v

# Abonnement a un topic
mosquitto_sub -h localhost -t "test/topic"

# Publication d'un message
mosquitto_pub -h localhost -t "test/topic" -m "Hello MQTT"</code></pre>

<div style="display: flex; justify-content: center; margin: 20px 0;">
    <img src="/img/BE_Middleware_IOT/mqtt_start.png" style="width: 60%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure: Starting the Mosquitto broker in verbose mode
</p>

<div style="display: flex; justify-content: center; margin: 20px 0;">
    <img src="/img/BE_Middleware_IOT/mqtt_sub_pub.png" style="width: 60%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure: Publish/subscribe test with mosquitto_pub and mosquitto_sub
</p>

<p><strong>Advanced broker configuration</strong>:</p>
<ul>
<li>Configuration file: <code>/etc/mosquitto/mosquitto.conf</code></li>
<li>Definition of listening ports and authentication parameters</li>
<li>ACL configuration to control topic access</li>
<li>Logging activation for debugging</li>
</ul>

<p>The tests validated the proper functioning of the communication chain: the subscriber instantly receives messages published by the publisher via the broker, confirming the asynchronous publish/subscribe model.</p>

<h3 class="section-title">3. NodeMCU/ESP8266 programming with MQTT</h3>

<p>The NodeMCU is a development board based on the <strong>ESP8266</strong> microcontroller, integrating a WiFi module. I programmed this board to communicate via MQTT with the Mosquitto broker, using the <strong>Arduino IDE</strong> and the <strong>ArduinoMqttClient</strong> library.</p>

<p><strong>NodeMCU/ESP8266 characteristics</strong>:</p>
<ul>
<li>32-bit processor at 80 MHz</li>
<li>Built-in WiFi 802.11 b/g/n</li>
<li>GPIO, ADC, PWM, I2C, SPI</li>
<li>Programmable via Arduino IDE</li>
<li>Ideal for IoT prototyping</li>
</ul>

<p><strong>Implemented features</strong>:</p>
<ol>
<li><strong>WiFi connection</strong>: the NodeMCU connects to the local WiFi network</li>
<li><strong>MQTT connection</strong>: establishing connection with the Mosquitto broker</li>
<li><strong>Button state publishing</strong>: on each physical button press, publishing the state on the <code>button/state</code> topic</li>
<li><strong>Luminosity publishing</strong>: reading the luminosity sensor (ADC) and publishing on the <code>light/state</code> topic on each button press</li>
<li><strong>Topic subscription</strong>: receiving commands from other devices</li>
</ol>

<p><strong>Programming logic excerpt</strong>:</p>

<pre><code class="language-cpp">// Connexion WiFi
WiFi.begin(ssid, password);

// Connexion au broker MQTT
mqttClient.connect(broker, port);

// Publication sur topic
mqttClient.beginMessage("button/state");
mqttClient.print(buttonState);
mqttClient.endMessage();

// Lecture luminosite et publication
int luminosity = analogRead(A0);
mqttClient.beginMessage("light/state");
mqttClient.print(luminosity);
mqttClient.endMessage();</code></pre>

<div style="display: flex; justify-content: center; margin: 20px 0;">
    <img src="/img/BE_Middleware_IOT/nodemcu_app.png" style="width: 70%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure: NodeMCU application diagram - publishing button and luminosity states via MQTT
</p>

<p><strong>Important technical points</strong>:</p>
<ul>
<li>Button <strong>debounce</strong> management is essential to avoid multiple publications</li>
<li>Automatic broker reconnection in case of WiFi or MQTT connection loss ensures system robustness</li>
<li>Using QoS 1 for critical publications ensures message delivery</li>
</ul>

<h3 class="section-title">4. oneM2M Standard - Architecture and resources</h3>

<p>oneM2M is an international standard for M2M communications and IoT. It defines a universal middleware architecture enabling interoperability between different IoT systems, regardless of the underlying network.</p>

<p><strong>oneM2M Architecture</strong>:</p>

<table>
<tr><th>Component</th><th>Acronym</th><th>Role</th></tr>
<tr><td>Common Services Entity</td><td>CSE</td><td>Provides common services (registration, discovery, data management, security)</td></tr>
<tr><td>Application Entity</td><td>AE</td><td>Represents an IoT application that interacts with the CSE</td></tr>
<tr><td>Infrastructure Node</td><td>IN</td><td>Server node hosting the main CSE</td></tr>
<tr><td>Middle Node</td><td>MN</td><td>Intermediate node (gateway)</td></tr>
<tr><td>Application Service Node</td><td>ASN</td><td>Sensor/actuator node</td></tr>
</table>

<p><strong>oneM2M resource tree</strong>:</p>

<p>The oneM2M architecture organizes data as a <strong>hierarchical resource tree</strong>:</p>

<pre><code>CSEBase (in-cse)
  |-- ACP (Access Control Policy)
  |-- AE (Application Entity - ex: Mon_AE)
  |     |-- Container (DATA)
  |     |     |-- ContentInstance (valeur capteur)
  |     |     |-- ContentInstance (valeur capteur)
  |     |-- Container (COMMAND)
  |           |-- ContentInstance (commande actionneur)
  |-- AE (Autre application)</code></pre>

<p><strong>Main resource types</strong>:</p>

<table>
<tr><th>Type</th><th>Code (ty)</th><th>Description</th></tr>
<tr><td>ACP</td><td>1</td><td>Access Control Policy (CRUD + Notify + Discovery rights)</td></tr>
<tr><td>AE</td><td>2</td><td>Application Entity - represents an application</td></tr>
<tr><td>Container</td><td>3</td><td>Data container (hierarchical structure)</td></tr>
<tr><td>ContentInstance</td><td>4</td><td>Content instance (individual data point)</td></tr>
<tr><td>Subscription</td><td>23</td><td>Subscription for automatic notification</td></tr>
</table>

<p><strong>CRUD operations via REST API</strong>:</p>

<p>Interaction with the CSE is done through HTTP RESTful requests:</p>

<pre><code class="language-python"># Creation d'une Application Entity
POST /~/in-cse/in-name
Headers: X-M2M-Origin: '', Content-Type: application/json;ty=2
Body: {"m2m:ae": {"api": "app.iot", "rr": "true", "rn": "Mon_AE"}}

# Creation d'un Container
POST /~/in-cse/in-name/Mon_AE
Headers: X-M2M-Origin: admin:admin, Content-Type: application/json;ty=3
Body: {"m2m:cnt": {"rn": "DATA"}}

# Creation d'un ContentInstance
POST /~/in-cse/in-name/Mon_AE/DATA
Headers: X-M2M-Origin: admin:admin, Content-Type: application/json;ty=4
Body: {"m2m:cin": {"con": "42"}}

# Recuperation du dernier contenu
GET /~/in-cse/in-name/Mon_AE/DATA/la
Headers: X-M2M-Origin: admin:admin, Accept: application/json</code></pre>

<p><strong>Access rights (ACP)</strong>:</p>

<p>ACPs define permissions on resources:</p>

<table>
<tr><th>Value</th><th>Permission</th></tr>
<tr><td>1</td><td>CREATE</td></tr>
<tr><td>2</td><td>RETRIEVE</td></tr>
<tr><td>4</td><td>UPDATE</td></tr>
<tr><td>8</td><td>DELETE</td></tr>
<tr><td>16</td><td>NOTIFY</td></tr>
<tr><td>32</td><td>DISCOVERY</td></tr>
<tr><td>63</td><td>All permissions</td></tr>
</table>

<p><strong>ACME CSE</strong>:</p>

<p>For the lab sessions, we used <strong>ACME</strong>, an open-source implementation of the oneM2M standard developed for research and education. ACME provides a complete CSE with a web interface, HTTP/MQTT/CoAP support, and a local database.</p>

<h3 class="section-title">5. Rapid prototyping with Node-RED</h3>

<p>Node-RED is a visual programming tool based on Node.js, designed for rapid prototyping of IoT applications. It allows creating <strong>data flows</strong> by connecting graphical nodes, considerably simplifying the development and integration of IoT systems.</p>

<p><strong>Node-RED principles</strong>:</p>
<ul>
<li><strong>Flows</strong>: sequence of connected nodes representing data processing</li>
<li><strong>Nodes</strong>: functional blocks (input, processing, output)</li>
<li><strong>Messages</strong>: JSON objects flowing between nodes (<code>msg.payload</code>, <code>msg.topic</code>)</li>
<li><strong>Web interface</strong>: visual editor accessible via browser</li>
<li><strong>Extensible</strong>: thousands of community nodes installable via npm</li>
</ul>

<p><strong>Types of nodes used</strong>:</p>

<table>
<tr><th>Category</th><th>Nodes</th><th>Function</th></tr>
<tr><td>Input</td><td>mqtt in, inject</td><td>MQTT message reception, data injection</td></tr>
<tr><td>Processing</td><td>switch, function, change</td><td>Conditional logic, data transformation</td></tr>
<tr><td>Output</td><td>mqtt out, debug, email</td><td>MQTT publishing, debug display, email sending</td></tr>
<tr><td>Dashboard</td><td>gauge, chart, button, text</td><td>User interface components</td></tr>
</table>

<div style="display: flex; justify-content: center; margin: 20px 0;">
    <img src="/img/BE_Middleware_IOT/nodered.png" style="width: 70%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure: Node-RED flow integrating MQTT reception, control logic and actuators
</p>

<p><strong>a. Verifying MQTT connectivity</strong></p>

<p>The first step consisted of adding an <strong>mqtt in</strong> node in Node-RED, configured to connect to the Mosquitto broker and subscribe to the <code>insa/luminosity</code> topic. The <strong>debug</strong> node confirmed the proper reception of values sent by the NodeMCU.</p>

<p><strong>b. Sensor and actuator management</strong></p>

<p>A flow was created to simulate the control logic of an automatic lighting system:</p>
<ul>
<li>A luminosity sensor publishes values on MQTT</li>
<li>A <strong>switch</strong> node evaluates the received value:
  <ul>
  <li>Luminosity &gt; 50: send LED ON command</li>
  <li>Luminosity &lt;= 50: send LED OFF command</li>
  </ul>
</li>
<li>The <strong>mqtt out</strong> node publishes the command on the actuator topic</li>
</ul>

<p>This logic illustrates the basic pattern of a reactive IoT system: sensor &rarr; processing &rarr; actuator.</p>

<p><strong>c. Visualization and control dashboard</strong></p>

<p>Using the <code>node-red-dashboard</code> module, an interactive dashboard was created to:</p>
<ul>
<li><strong>Visualize</strong> sensor data in real time (charts, gauges)</li>
<li><strong>Control</strong> actuators (ON/OFF buttons for LEDs)</li>
<li><strong>Monitor</strong> system status (visual indicators)</li>
</ul>

<div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; margin: 20px 0;">
    <img src="/img/BE_Middleware_IOT/nodered_dashboard.png" style="width: 30%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <img src="/img/BE_Middleware_IOT/nodered_led.png" style="width: 55%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure: Node-RED Dashboard - sensor visualization and LED control
</p>

<p><strong>d. Email notifications</strong></p>

<p>The <code>node-red-node-email</code> module was integrated to send automatic email alerts upon:</p>
<ul>
<li>Switch state change (ON/OFF)</li>
<li>Luminosity threshold exceeded</li>
<li>Anomaly detection (outlier values)</li>
</ul>

<p>This proactive notification mechanism is essential in IoT systems to ensure rapid response to critical events.</p>

<h3 class="section-title">6. Comparison of IoT protocols: HTTP vs MQTT vs CoAP</h3>

<p>The choice of communication protocol is a major architectural decision in any IoT project. Each protocol has specific advantages and constraints.</p>

<table>
<tr><th>Criterion</th><th>HTTP</th><th>MQTT</th><th>CoAP</th></tr>
<tr><td>Model</td><td>Request/Response</td><td>Publish/Subscribe</td><td>Request/Response</td></tr>
<tr><td>Transport</td><td>TCP</td><td>TCP</td><td>UDP</td></tr>
<tr><td>Overhead</td><td>High (text headers)</td><td>Low (2 bytes min)</td><td>Very low (4 bytes)</td></tr>
<tr><td>QoS</td><td>Not native</td><td>3 levels (0, 1, 2)</td><td>Confirmable/Non-confirmable</td></tr>
<tr><td>Discovery</td><td>No</td><td>No</td><td>Yes (.well-known/core resource)</td></tr>
<tr><td>Observe</td><td>No</td><td>Yes (subscribe)</td><td>Yes (Observe option)</td></tr>
<tr><td>Security</td><td>TLS</td><td>TLS</td><td>DTLS</td></tr>
<tr><td>Typical use</td><td>Web API, REST</td><td>Telemetry, notification</td><td>Highly constrained objects</td></tr>
<tr><td>Consumption</td><td>High</td><td>Moderate</td><td>Low</td></tr>
<tr><td>Latency</td><td>Moderate</td><td>Low</td><td>Very low</td></tr>
</table>

<p><strong>When to use which protocol</strong>:</p>
<ul>
<li><strong>HTTP</strong>: one-time interactions, REST APIs, integration with the existing web, oneM2M</li>
<li><strong>MQTT</strong>: continuous telemetry, real-time notifications, communication between many devices</li>
<li><strong>CoAP</strong>: very low-resource objects (battery-powered sensors), 6LoWPAN networks, direct device-to-device communication</li>
</ul>

<h3 class="section-title">7. RESTful APIs for IoT</h3>

<p>The REST (Representational State Transfer) architecture is at the heart of modern IoT, particularly in the oneM2M standard. REST principles applied to IoT:</p>

<p><strong>REST principles</strong>:</p>
<ul>
<li><strong>Resources identified by URI</strong>: each sensor, actuator or data point is an addressable resource</li>
<li><strong>CRUD operations via HTTP verbs</strong>:
  <ul>
  <li>GET: read a resource (e.g.: sensor value)</li>
  <li>POST: create a resource (e.g.: new ContentInstance)</li>
  <li>PUT: update a resource</li>
  <li>DELETE: delete a resource</li>
  </ul>
</li>
<li><strong>Representations</strong>: JSON or XML for encoding data</li>
<li><strong>Stateless</strong>: each request contains all necessary information</li>
</ul>

<p><strong>Application to the oneM2M standard</strong>:<br>
In oneM2M, the resource tree is accessible via RESTful URLs. Specific HTTP headers (<code>X-M2M-Origin</code>, <code>Content-Type</code> with resource type) allow the CSE to identify the caller and the type of creation requested.</p>

<h3 class="section-title">8. IoT protocol stack</h3>

<p>IoT uses a protocol stack adapted to the constraints of connected objects:</p>

<table>
<tr><th>Layer</th><th>Standard protocols</th><th>IoT protocols</th></tr>
<tr><td>Application</td><td>HTTP, FTP</td><td>MQTT, CoAP, AMQP, oneM2M</td></tr>
<tr><td>Transport</td><td>TCP, UDP</td><td>TCP (MQTT), UDP (CoAP)</td></tr>
<tr><td>Network</td><td>IPv4, IPv6</td><td>6LoWPAN, RPL</td></tr>
<tr><td>Data Link</td><td>Ethernet, WiFi</td><td>IEEE 802.15.4, BLE, LoRa, Sigfox</td></tr>
<tr><td>Physical</td><td>Cables, waves</td><td>RF sub-GHz, 2.4 GHz</td></tr>
</table>

<p><strong>IoT stack specifics</strong>:</p>
<ul>
<li><strong>6LoWPAN</strong>: IPv6 adaptation for low-power sensor networks (header compression)</li>
<li><strong>RPL</strong>: routing protocol for sensor networks (DODAG tree)</li>
<li><strong>IEEE 802.15.4</strong>: data link layer for low-power wireless personal area networks</li>
<li>Middleware such as oneM2M operates at the application level and is <strong>independent of the underlying network</strong></li>
</ul>

<h3 class="section-title">9. M2M communication patterns</h3>

<p>Machine-to-Machine communications follow several architectural patterns:</p>

<p><strong>1. Publish/Subscribe (MQTT)</strong>:</p>
<ul>
<li>Asynchronous communication via broker</li>
<li>Spatial decoupling (publisher and subscriber do not know each other)</li>
<li>Temporal decoupling (no need to be connected simultaneously thanks to retain)</li>
<li>Ideal for: telemetry, event notification, data distribution to N receivers</li>
</ul>

<p><strong>2. Request/Response (HTTP, CoAP)</strong>:</p>
<ul>
<li>Synchronous client/server communication</li>
<li>The client initiates the request, the server responds</li>
<li>Ideal for: one-time reading, actuator command, REST API</li>
</ul>

<p><strong>3. Observer (CoAP Observe, oneM2M Subscription)</strong>:</p>
<ul>
<li>The client registers to be notified of changes</li>
<li>The server sends notifications on each modification</li>
<li>Ideal for: continuous monitoring, real-time dashboards</li>
</ul>

<p><strong>4. Pipeline / Data Flow (Node-RED)</strong>:</p>
<ul>
<li>Data passes through a processing chain</li>
<li>Each node transforms or filters the data</li>
<li>Ideal for: IoT ETL, stream processing, prototyping</li>
</ul>

<h3 class="section-title">10. Rapid prototyping with Node-RED - In depth</h3>

<p>Node-RED proves to be an extremely powerful tool for IoT prototyping thanks to several advanced features:</p>

<p><strong>Exportable JSON flows</strong>:<br>
Node-RED flows are serialized in JSON, enabling versioning (Git), sharing and automated deployment. During the lab, we exported our configuration to the file <code>Boukouiss_Chanfreau_Node-Red.json</code>.</p>

<p><strong>Custom nodes (function)</strong>:<br>
The <code>function</code> node allows writing JavaScript code for complex processing:</p>

<pre><code class="language-javascript">// Exemple : transformation de donnees capteur
var luminosity = msg.payload;
if (luminosity > 50) {
    msg.payload = "ON";
    msg.topic = "led/command";
} else {
    msg.payload = "OFF";
    msg.topic = "led/command";
}
return msg;</code></pre>

<p><strong>Multi-protocol integration</strong>:<br>
Node-RED natively supports MQTT, HTTP, WebSocket, TCP, UDP and can be extended to support CoAP, oneM2M, databases (InfluxDB, MongoDB), cloud services (AWS IoT, Azure IoT Hub).</p>

<p><strong>Advantages for IoT prototyping</strong>:</p>
<ul>
<li>Visual development accelerating implementation</li>
<li>Real-time testing and debugging (debug node)</li>
<li>Built-in dashboard for visualization</li>
<li>Hot modification without restart</li>
<li>Large community and node ecosystem</li>
</ul>

<hr>

<h2>PART D - Reflective Analysis and Perspectives</h2>

<h3 class="section-title">Skills acquired</h3>

<p><strong>Mastery of IoT protocols</strong>:<br>
In-depth understanding of MQTT (publish/subscribe, QoS, broker), RESTful APIs for oneM2M, and CoAP principles. Ability to choose the appropriate protocol based on project constraints.</p>

<p><strong>Embedded IoT programming</strong>:<br>
Competence to program an ESP8266/NodeMCU and integrate it into an MQTT architecture: WiFi connection, publish/subscribe, sensor and actuator management.</p>

<p><strong>M2M middleware architecture</strong>:<br>
Understanding of the oneM2M standard, resource tree, ACPs, and interaction with a CSE via REST API. Ability to deploy and configure a oneM2M infrastructure.</p>

<p><strong>Rapid prototyping</strong>:<br>
Mastery of Node-RED for designing complete IoT flows, integrating data capture, processing logic, visualization dashboard and notification systems.</p>

<p><strong>System integration</strong>:<br>
Ability to combine all building blocks (sensors, MQTT broker, oneM2M CSE, Node-RED, dashboard) into a coherent and functional IoT architecture.</p>

<h3 class="section-title">Key takeaways</h3>

<p><strong>1. MQTT is the reference protocol for IoT</strong>:<br>
Its lightness, publish/subscribe model and QoS levels make it the preferred choice for telemetry and communication between connected objects.</p>

<p><strong>2. oneM2M standardizes M2M interoperability</strong>:<br>
This international standard provides an abstraction layer above transport protocols, enabling interoperability between heterogeneous systems.</p>

<p><strong>3. Node-RED considerably accelerates prototyping</strong>:<br>
Visual programming allows quickly moving from idea to functional prototype, which is crucial in IoT projects where rapid iteration is essential.</p>

<p><strong>4. Protocol choice depends on the use case</strong>:<br>
HTTP for web APIs, MQTT for real-time telemetry, CoAP for highly constrained objects. There is no universal solution.</p>

<p><strong>5. IoT security is a major challenge</strong>:<br>
Authentication, encryption (TLS/DTLS) and access control must be integrated from the architecture design stage.</p>

<h3 class="section-title">Self-assessment</h3>

<p>This course was my first in-depth experience with IoT protocols such as MQTT and the oneM2M standard. I found these technologies relatively accessible thanks to the many existing libraries and available documentation. The pedagogical progression of the labs (from Mosquitto command line to the complete Node-RED application) enabled progressive and solid skill building.</p>

<p>The hands-on implementation allowed me to understand the practical usefulness of these concepts. I subsequently reused some of these tools in our <strong>innovative project</strong> to set up efficient communication between devices, confirming the relevance of this teaching.</p>

<p>The richness of the oneM2M standard impressed me: the hierarchical resource structure, access rights system and notification mechanisms allow building robust and interoperable IoT architectures. However, this richness implies a significant learning curve.</p>

<h3 class="section-title">My opinion</h3>

<p>This course was one of my favorites of the semester because it perfectly combines <strong>hardware and software</strong> aspects. As an aspiring embedded systems engineer, this combination of microcontroller programming and middleware software architectures corresponds exactly to my targeted skill profile.</p>

<p><strong>Strengths</strong>:</p>
<ul>
<li>Exemplary pedagogical progression: MQTT in CLI, then ESP8266, then oneM2M, then Node-RED</li>
<li>Theory/practice balance with concrete and motivating lab sessions</li>
<li>Accessible open-source tools to continue practicing</li>
<li>Direct connection to IoT industry needs</li>
</ul>

<p><strong>Areas for improvement</strong>:</p>
<ul>
<li>More time on oneM2M (standard complexity)</li>
<li>Introduction of CoAP in practice (not only in theory)</li>
<li>More in-depth security aspects (TLS, certificates)</li>
<li>Architecture scalability (broker clusters, load balancing)</li>
</ul>

<p>The progressive approach of the labs made learning both enjoyable and highly educational. Starting from basic MQTT communication via command line, evolving to Arduino programming with the MQTT library, then integrating everything with Node-RED provides a complete view of the IoT chain. This is exactly the type of course that prepares for concrete professional projects.</p>

<h3 class="section-title">Professional applications</h3>

<p><strong>IoT Engineer</strong>:</p>
<ul>
<li>Design communication architectures for connected objects</li>
<li>Deploy and administer MQTT brokers at scale</li>
<li>Integrate sensors and actuators into IoT platforms</li>
</ul>

<p><strong>Embedded Systems Engineer</strong>:</p>
<ul>
<li>Program communicating microcontrollers (ESP8266, ESP32, STM32)</li>
<li>Implement IoT protocols on constrained systems</li>
<li>Optimize communication energy consumption</li>
</ul>

<p><strong>M2M Solutions Architect</strong>:</p>
<ul>
<li>Design interoperable platforms based on oneM2M</li>
<li>Define middleware architectures for industrial systems</li>
<li>Ensure infrastructure scalability and security</li>
</ul>

<p><strong>Links with other courses</strong>:</p>
<ul>
<li><a href="./cloud-edge.html">Cloud and Edge Computing - S9</a>: broker and CSE deployment</li>
<li><a href="./security-object.html">Security for Connected Objects - S9</a>: MQTT/TLS security</li>
<li><a href="./wireless-sensors.html">Wireless Sensors Networks - S9</a>: sensor lower layers</li>
<li><a href="./service-oriented-architecture.html">Service Oriented Architecture - S9</a>: REST APIs, microservices</li>
</ul>

<hr>

<h2>Course Documents</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">Planning MOOC oneM2M</span>
        <span class="lang-en">oneM2M MOOC Planning</span>
      </h4>
      <p>
        <span class="lang-fr">Planning et contenu du MOOC oneM2M suivi en autonomie : introduction au standard, architecture, types de ressources.</span>
        <span class="lang-en">Planning and content of the self-paced oneM2M MOOC: introduction to the standard, architecture, resource types.</span>
      </p>
      <embed src="/cours-pdf/S9/Middleware/MOOC_oneM2M_planning.pdf" type="application/pdf" width="100%" height="600px" />
      <p><a href="/cours-pdf/S9/Middleware/MOOC_oneM2M_planning.pdf" target="_blank">
        <span class="lang-fr">Telecharger</span>
        <span class="lang-en">Download</span>
      </a></p>
    </div>
  </div>
</div>

<hr>

<h2>Reports and Projects</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">Rapport Middleware for IoT - BE</span>
        <span class="lang-en">Middleware for IoT Report - Design Project</span>
      </h4>
      <p>
        <span class="lang-fr">Rapport complet du bureau d'etudes : architecture IoT deployee, integration MQTT, oneM2M et Node-RED, resultats experimentaux.</span>
        <span class="lang-en">Complete design project report: deployed IoT architecture, MQTT integration, oneM2M and Node-RED, experimental results.</span>
      </p>
      <embed src="/file/reports/S9/Report_Middleware_For_IoT.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/file/reports/S9/Report_Middleware_For_IoT.pdf" target="_blank">
        <span class="lang-fr">Telecharger le rapport BE</span>
        <span class="lang-en">Download the design project report</span>
      </a></p>
    </div>
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">Rapport TP1-2 : MQTT et NodeMCU</span>
        <span class="lang-en">Lab 1-2 Report: MQTT and NodeMCU</span>
      </h4>
      <p>
        <span class="lang-fr">Rapport des travaux pratiques 1 et 2 : installation Mosquitto, communication publish/subscribe, programmation ESP8266.</span>
        <span class="lang-en">Lab sessions 1 and 2 report: Mosquitto installation, publish/subscribe communication, ESP8266 programming.</span>
      </p>
      <embed src="/file/reports/S9/Report_Middleware_TP1-2.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/file/reports/S9/Report_Middleware_TP1-2.pdf" target="_blank">
        <span class="lang-fr">Telecharger le rapport TP1-2</span>
        <span class="lang-en">Download the Lab 1-2 report</span>
      </a></p>
    </div>
  </div>
</div>

<div style="text-align: center; margin-top: 20px;">
    <a href="/img/BE_Middleware_IOT/Lab_Subject_middleware.pdf" target="_blank">
        <span class="lang-fr">Ouvrir le sujet de TP</span>
        <span class="lang-en">Open the lab subject</span>
    </a>
</div>

<hr>

<p><em>Course taken in 2024-2025 at INSA Toulouse, Department of Electrical and Computer Engineering, ISS (Innovative Smart Systems) specialization.</em></p>

</div>

<div class="back-nav">
    <a href="./my-courses-2024-2025.html" data-i18n-html="back-courses-2024-2025">&larr; Retour aux Cours 2024-2025</a>
</div>

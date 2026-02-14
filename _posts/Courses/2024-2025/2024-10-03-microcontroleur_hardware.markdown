---
layout: default
title:  "Microcontroller Open Source Hardware and Sensors"
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

<h1>Microcontroleur Hardware / Open Source - Semestre 9</h1>

<p><strong>Annee academique</strong> : 2024-2025<br/>
<strong>Categorie</strong> : Electronique embarquee, IoT, Hardware Open Source</p>

<hr/>

<h2>PART A - Presentation Generale</h2>

<h3 class="section-title">Vue d'ensemble</h3>

<p>Ce cours, qui fait suite a la semaine de travaux pratiques au laboratoire AIME pour la fabrication d'un capteur de gaz, se concentre sur l'integration de ce capteur dans un systeme complet base sur des microcontroleurs open source. L'objectif principal est de concevoir un dispositif intelligent capable de collecter, transmettre et visualiser les donnees issues du capteur de gaz, en utilisant des technologies open source et des protocoles de communication sans fil.</p>

<p>Le projet couvre l'ensemble de la chaine, depuis le capteur physique jusqu'a l'application mobile, en passant par la programmation du microcontroleur, la mise en place d'un reseau LoRaWAN, la creation de tableaux de bord avec Node-RED et le developpement d'une application mobile avec MIT App Inventor.</p>

<p><strong>Objectifs pedagogiques</strong> :</p>
<ul>
<li>Comprendre et utiliser les plateformes microcontroleurs open source (Arduino UNO, ESP32, ESP8266)</li>
<li>Interfacer des capteurs avec un microcontroleur via les protocoles GPIO, I2C, SPI</li>
<li>Mettre en place une communication sans fil (LoRa, BLE, WiFi)</li>
<li>Concevoir des flux IoT avec Node-RED pour le traitement et la visualisation de donnees</li>
<li>Developper une application mobile avec MIT App Inventor</li>
<li>Creer un dashboard temps reel pour la supervision de capteurs</li>
<li>Concevoir un circuit imprime (PCB) avec KiCad</li>
</ul>

<p><strong>Outils et technologies</strong> :</p>

<table>
<tr><th>Outil / Technologie</th><th>Usage</th></tr>
<tr><td>Arduino UNO</td><td>Microcontroleur central du systeme</td></tr>
<tr><td>Module LoRa RN2483</td><td>Communication sans fil longue portee</td></tr>
<tr><td>ChirpStack</td><td>Serveur reseau LoRaWAN</td></tr>
<tr><td>Node-RED</td><td>Flux de traitement et dashboard IoT</td></tr>
<tr><td>MIT App Inventor</td><td>Developpement application mobile Android</td></tr>
<tr><td>KiCad</td><td>Conception de circuits imprimes (PCB)</td></tr>
<tr><td>MQTT</td><td>Protocole de messagerie IoT</td></tr>
<tr><td>Ecran OLED SSD1306</td><td>Affichage local des donnees (I2C)</td></tr>
</table>

<hr/>

<h2>PART B - Experience et Contexte</h2>

<h3 class="section-title">Environnement de travail</h3>

<p>Ce cours s'inscrit dans la continuite du module AIME ou nous avons fabrique un capteur de gaz a base de nanoparticules de WO3. L'enjeu etait desormais de transformer ce composant en un dispositif fonctionnel et connecte, en l'integrant dans un systeme electronique complet.</p>

<p>Le travail s'est deroule en plusieurs phases :</p>
<ol>
<li><strong>Cablage et integration materielle</strong> : connexion du capteur, du microcontroleur Arduino UNO, du module LoRa RN2483, de l'ecran OLED et des composants auxiliaires (LED, resistances).</li>
<li><strong>Programmation embarquee</strong> : developpement du firmware Arduino en langage C pour la lecture du capteur, l'affichage sur ecran OLED et la transmission des donnees via LoRa.</li>
<li><strong>Infrastructure reseau</strong> : configuration du serveur LoRaWAN ChirpStack et du broker MQTT pour la reception des donnees.</li>
<li><strong>Visualisation et supervision</strong> : creation de flux Node-RED et d'un dashboard temps reel pour surveiller les niveaux de gaz.</li>
<li><strong>Application mobile</strong> : developpement d'une application Android avec MIT App Inventor pour le controle et la surveillance a distance via Bluetooth.</li>
<li><strong>Conception PCB</strong> : initiation a KiCad pour la conception du circuit imprime du conditionneur de signal.</li>
</ol>

<h3 class="section-title">Ma fonction</h3>

<p>Dans le cadre de ce projet, j'etais responsable de :</p>
<ul>
<li>La comprehension des principes des technologies de microcontroleurs open source</li>
<li>La conception et l'integration du systeme complet (capteur, conditionneur, microcontroleur, communication)</li>
<li>Le cablage des differents composants sur breadboard</li>
<li>La programmation du firmware Arduino</li>
<li>La configuration des flux Node-RED et du dashboard</li>
<li>Le developpement de l'application mobile MIT App Inventor</li>
<li>La realisation d'essais pour tester la fonctionnalite et l'efficacite du systeme</li>
</ul>

<hr/>

<h2>PART C - Aspects Techniques</h2>

<h3 class="section-title">Concepts techniques approfondis</h3>

<p>Cette section detaille les aspects techniques de l'integration du capteur de gaz avec un microcontroleur et le developpement d'applications pour la collecte et la visualisation de donnees.</p>

<h3>1. Plateformes microcontroleurs open source</h3>

<p>Le projet repose sur l'utilisation d'un <strong>Arduino UNO</strong>, une plateforme open source basee sur le microcontroleur ATmega328P. Les plateformes open source telles que l'Arduino, l'ESP32 et l'ESP8266 sont au coeur de l'IoT moderne grace a leur accessibilite, leur documentation communautaire et leur ecosysteme de bibliotheques.</p>

<p><strong>Caracteristiques cles de l'Arduino UNO</strong> :</p>
<ul>
<li>Microcontroleur ATmega328P a 16 MHz</li>
<li>14 broches d'entrees/sorties numeriques (GPIO), dont 6 PWM</li>
<li>6 entrees analogiques (ADC 10 bits)</li>
<li>Interfaces de communication : UART, I2C (SDA/SCL), SPI (MOSI/MISO/SCK/SS)</li>
<li>Alimentation : USB 5V ou jack DC</li>
</ul>

<p><strong>Protocoles de communication utilises</strong> :</p>
<ul>
<li><strong>GPIO</strong> : Lecture analogique du capteur de gaz (pin A0), controle de LED (pin D4)</li>
<li><strong>I2C</strong> : Communication avec l'ecran OLED SSD1306 (adresse 0x3C)</li>
<li><strong>UART (SoftwareSerial)</strong> : Communication avec le module LoRa RN2483 (pins 10/11)</li>
<li><strong>SPI</strong> : Utilise dans d'autres configurations avec l'ESP32 pour des capteurs additionnels</li>
</ul>

<h3>2. Capteur de gaz et interfacage</h3>

<p>Le capteur de gaz a ete fabrique lors de la formation au laboratoire <a href="./aime.html">AIME</a>. Il utilise des nanoparticules de WO3 qui permettent une haute sensibilite a des gaz specifiques comme l'ethanol et l'ammoniac. Le capteur comprend :</p>
<ul>
<li><strong>Couche sensible</strong> : Nanoparticules deposees sur des peignes interdigites en aluminium</li>
<li><strong>Element chauffant</strong> : Resistance en polysilicium pour ajuster la temperature de fonctionnement</li>
<li><strong>Zone de calibration</strong> : Zone sans nanoparticules pour les mesures de reference</li>
</ul>

<table>
<tr><th>Broche</th><th>Description</th></tr>
<tr><td>2, 4</td><td>Couche sensible (avec nanoparticules)</td></tr>
<tr><td>3, 6</td><td>Element chauffant</td></tr>
<tr><td>5, 10</td><td>Capteur de temperature</td></tr>
<tr><td>7, 9</td><td>Couche de calibration</td></tr>
<tr><td>1, 8</td><td>Non utilise</td></tr>
</table>

<h3>3. Cablage et integration materielle</h3>

<p>Pour creer un systeme fonctionnel, nous avons cable les composants suivants :</p>
<ul>
<li><strong>Arduino UNO</strong> : Microcontroleur central du systeme</li>
<li><strong>Module LoRa (RN2483)</strong> : Pour la communication sans fil longue portee</li>
<li><strong>Capteur de gaz</strong> : Pour detecter les concentrations de gaz</li>
<li><strong>Ecran OLED SSD1306</strong> : Pour l'affichage local des donnees (via bus I2C)</li>
<li><strong>LED d'alerte</strong> : Indicateur visuel de depassement de seuil</li>
</ul>

</div>

<div style="text-align: center; display: flex; justify-content: center; gap: 10px;">
    <img src="/img/BE_microcontroleur/cablage.png" style="width: 50%;"/>
    <img src="/img/BE_microcontroleur/cablage2.png" style="width: 50%;"/>
</div>
<br>

<div class="lang-fr">

<p>Les connexions realisees sont les suivantes :</p>

<table>
<tr><th>Composant</th><th>Broche Arduino</th><th>Protocole</th><th>Detail</th></tr>
<tr><td>Capteur de gaz</td><td>A0</td><td>Analogique (GPIO)</td><td>Lecture ADC 10 bits</td></tr>
<tr><td>Module LoRa TX</td><td>Pin 10</td><td>UART (SoftwareSerial)</td><td>Transmission serie</td></tr>
<tr><td>Module LoRa RX</td><td>Pin 11</td><td>UART (SoftwareSerial)</td><td>Reception serie</td></tr>
<tr><td>Ecran OLED SDA</td><td>A4</td><td>I2C</td><td>Donnees</td></tr>
<tr><td>Ecran OLED SCL</td><td>A5</td><td>I2C</td><td>Horloge</td></tr>
<tr><td>LED d'alerte</td><td>Pin 4</td><td>GPIO numerique</td><td>Sortie ON/OFF</td></tr>
<tr><td>Alimentation LoRa</td><td>3.3V</td><td>-</td><td>Alimentation module</td></tr>
<tr><td>Alimentation Arduino</td><td>USB</td><td>-</td><td>5V via USB</td></tr>
</table>

<h3>4. Programmation Arduino et communication LoRa</h3>

<p>Le code Arduino se compose de deux parties principales : l'initialisation et la transmission de donnees.</p>

<p><strong>Initialisation</strong> :</p>
<ul>
<li>Configuration du module LoRa avec les identifiants AppEUI et AppKey pour l'enregistrement sur le reseau LoRaWAN (via ChirpStack)</li>
<li>Initialisation de l'ecran OLED en I2C pour le retour visuel</li>
<li>Configuration de la broche du capteur de gaz en entree analogique et de la LED en sortie numerique</li>
</ul>

<p><strong>Transmission de donnees</strong> :</p>
<ul>
<li>Lecture des valeurs du capteur de gaz via l'ADC (conversion analogique-numerique)</li>
<li>Traitement : comparaison avec un seuil d'alerte (valeur &gt; 100)</li>
<li>Envoi des donnees via LoRa au serveur ChirpStack</li>
<li>Mise a jour de l'affichage OLED et activation de la LED en cas de depassement</li>
</ul>

<p>Voici le code source utilise :</p>

</div>

```c
#include <TheThingsNetwork.h>
#include <TheThingsMessage.h>
#include <SoftwareSerial.h>
#include "SSD1306Ascii.h"
#include "SSD1306AsciiAvrI2c.h"

const char *appEui = "9314122f9f48664f";
const char *appKey = "77F85835964FC8C511F87CE864B96A6D";

#define I2C_ADDRESS 0x3C
#define GAZ_SENSOR_PIN A0
#define LED_PIN 4
#define freqPlan TTN_FP_EU868

SSD1306AsciiAvrI2c oled;
SoftwareSerial loraSerial(10, 11); // TX, RX
TheThingsNetwork ttn(loraSerial, Serial, freqPlan);

void setup() {
    loraSerial.begin(57600);
    Serial.begin(57600);
    while (!Serial && millis() < 10000);

    Serial.println("-- STATUS");
    ttn.showStatus();

    Serial.println("-- JOIN");
    ttn.join(appEui, appKey);

    pinMode(LED_PIN, OUTPUT);

    oled.begin(&Adafruit128x64, I2C_ADDRESS);
    oled.setFont(Adafruit5x7);
    oled.clear();
    oled.set2X();
    oled.println("Hello user1");
}

void loop() {
    Serial.println("-- LOOP");

    byte GAZ_VALUE = analogRead(GAZ_SENSOR_PIN);
    Serial.print("GAZ_VALUE: ");
    Serial.println(GAZ_VALUE);

    if (GAZ_VALUE > 100) {
        digitalWrite(LED_PIN, HIGH);
        oled.clearField(0, 2, 5);
        oled.println("HELP");
    } else {
        digitalWrite(LED_PIN, LOW);
        oled.clearField(0, 2, 5);
    }

    ttn.sendBytes(&GAZ_VALUE, 1);
    delay(10000);
}
```

<div class="lang-fr">

<p>Ce code initialise le module LoRa et le capteur de gaz, lit les donnees du capteur toutes les 10 secondes, et les transmet via LoRa. Il met egalement a jour l'ecran OLED et controle une LED en fonction du niveau de gaz detecte.</p>

<p><strong>Architecture de communication sans fil</strong> :</p>
<ul>
<li><strong>LoRa (Long Range)</strong> : Protocole de communication sans fil bas debit et longue portee, utilisant la bande de frequence EU868 MHz. Le module RN2483 communique avec l'Arduino via une liaison serie logicielle (SoftwareSerial).</li>
<li><strong>LoRaWAN</strong> : Protocole reseau au-dessus de LoRa, gerant l'authentification (OTAA avec AppEUI/AppKey), le routage des paquets et la gestion des dispositifs via le serveur ChirpStack.</li>
<li><strong>BLE (Bluetooth Low Energy)</strong> : Utilise pour la communication entre l'Arduino et l'application mobile MIT App Inventor, permettant le controle local et la lecture des donnees en temps reel.</li>
</ul>

<h3>5. Node-RED : flux IoT et dashboard temps reel</h3>

<p>Node-RED est un outil de programmation visuelle base sur des flux (flow-based programming), particulierement adapte au prototypage rapide d'applications IoT. Dans ce projet, Node-RED a ete utilise pour recevoir, traiter et afficher les donnees du capteur LoRa.</p>

<p><strong>Architecture du flux Node-RED</strong> :</p>

<p>Le flux se decompose en quatre etapes :</p>
<ol>
<li><strong>Reception des donnees</strong> : Un noeud MQTT ecoute les messages entrants du reseau LoRaWAN ChirpStack. Le broker MQTT est configure pour recevoir les trames du serveur reseau.</li>
<li><strong>Extraction des donnees</strong> : Un noeud fonction decode les donnees encodees en Base64 et extrait la valeur du niveau de gaz.</li>
<li><strong>Traitement et alerte</strong> : Un second noeud fonction analyse le niveau de gaz et declenche une alerte si la valeur depasse le seuil defini (par exemple 200).</li>
<li><strong>Visualisation</strong> : Un noeud graphique affiche les niveaux de gaz en temps reel dans le dashboard Node-RED.</li>
</ol>

</div>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_microcontroleur/nodered.png" style="width: 90%;"/>
</div>
<br>

<div class="lang-fr">

<p><strong>Details techniques du flux</strong> :</p>
<ul>
<li><strong>Noeud MQTT</strong> : Configure pour se connecter au broker de ChirpStack et s'abonner au topic du dispositif LoRa</li>
<li><strong>Noeuds Fonction</strong> : Code JavaScript pour le decodage Base64, l'extraction des donnees et l'analyse des seuils</li>
<li><strong>Noeud Chart</strong> : Affichage graphique en temps reel avec historique des mesures</li>
<li><strong>Dashboard</strong> : Accessible via <code>http://127.0.0.1:1880/ui</code>, interface web responsive pour la supervision</li>
</ul>

</div>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_microcontroleur/dashboard.png" style="width: 45%;"/>
</div>
<br>

<div class="lang-fr">

<p>Le dashboard Node-RED permet une visualisation en temps reel des niveaux de gaz detectes par le capteur. Les donnees sont affichees sous forme de graphique temporel, permettant de suivre l'evolution des concentrations de gaz et d'identifier rapidement les depassements de seuils.</p>

<h3>6. MIT App Inventor : application mobile Android</h3>

<p>MIT App Inventor est un environnement de developpement visuel qui permet de creer des applications Android sans ecrire de code traditionnel, en utilisant une approche par blocs logiques. Dans ce projet, nous avons developpe une application mobile pour interagir avec le systeme Arduino via Bluetooth (BLE).</p>

<p><strong>Fonctionnalites de l'application</strong> :</p>
<ul>
<li><strong>Connexion Bluetooth</strong> : L'application se connecte a l'Arduino via Bluetooth lorsque l'utilisateur appuie sur le bouton de connexion. Cela etablit un canal de communication bidirectionnel.</li>
<li><strong>Controle de LED</strong> : L'utilisateur peut allumer ou eteindre la LED d'alerte a distance en utilisant les boutons de l'interface.</li>
<li><strong>Surveillance du niveau de gaz</strong> : L'application recoit en continu les valeurs du capteur de gaz depuis l'Arduino et les affiche en temps reel.</li>
<li><strong>Alertes</strong> : Un systeme de notification previent l'utilisateur lorsque le niveau de gaz depasse un seuil predefini.</li>
</ul>

</div>

<div style="text-align: center; display: flex; justify-content: center; gap: 15px;">
    <img src="/img/BE_microcontroleur/mit_app.png" style="width: 40%;"/>
    <img src="/img/BE_microcontroleur/mit_app2.png" style="width: 40%;"/>
</div>
<br>

<div class="lang-fr">

<p><strong>Composants cles de l'application</strong> :</p>
<ul>
<li><strong>Bouton de connexion</strong> : Etablit la communication avec l'Arduino via le module Bluetooth</li>
<li><strong>Boutons de controle LED</strong> : Envoient des commandes ON/OFF a l'Arduino</li>
<li><strong>Label dynamique</strong> : Affiche le niveau de gaz actuel recu du capteur</li>
<li><strong>Notifier</strong> : Alerte l'utilisateur si le niveau de gaz depasse le seuil critique</li>
</ul>

<p>L'application fournit une interface simple et intuitive pour interagir avec le systeme Arduino en temps reel, permettant a la fois le controle et la surveillance des conditions environnementales a distance.</p>

<h3>7. Conception de circuit imprime avec KiCad</h3>

<p>KiCad est un logiciel open source de conception de circuits imprimes (PCB). Dans le cadre de ce cours, nous avons ete inities a KiCad pour concevoir le circuit du conditionneur de signal du capteur de gaz. Cette etape permet de passer du prototype sur breadboard a un circuit imprime professionnel.</p>

<p><strong>Etapes de conception</strong> :</p>
<ul>
<li>Creation du schema electrique avec les symboles des composants</li>
<li>Definition des empreintes physiques des composants</li>
<li>Routage du PCB en respectant les regles de conception (largeur de pistes, espacement)</li>
<li>Generation des fichiers Gerber pour la fabrication</li>
</ul>

<hr/>

<h2>PART D - Analyse et Reflexion</h2>

<h3 class="section-title">Competences et connaissances mobilisees</h3>

<p>Ce projet a mobilise un large ensemble de competences transversales :</p>

<ul>
<li>Comprendre l'architecture des microcontroleurs et savoir les utiliser dans un contexte IoT</li>
<li>Concevoir un systeme d'acquisition de donnees complet (capteur, conditionneur, microcontroleur) adapte a l'application</li>
<li>Interfacer des capteurs avec un microcontroleur via les protocoles GPIO, I2C, SPI et UART</li>
<li>Concevoir le circuit electronique du conditionneur de signal du capteur (conception et simulation)</li>
<li>Developper le logiciel embarque pour l'utilisation du capteur de gaz et son IHM (ecran OLED)</li>
<li>Mettre en oeuvre une communication sans fil (LoRa, BLE, WiFi) pour la transmission de donnees</li>
<li>Creer des flux Node-RED pour le traitement et la visualisation temps reel des donnees</li>
<li>Developper une application mobile avec MIT App Inventor</li>
<li>Combiner l'ensemble de ces composants en un dispositif intelligent et connecte</li>
<li>Comprendre les notions fondamentales des capteurs et de l'acquisition de donnees</li>
<li>Concevoir la fiche technique (datasheet) du capteur fabrique</li>
<li>Concevoir un PCB avec KiCad</li>
</ul>

<h3 class="section-title">Auto-evaluation</h3>

<p>Ce cours a ete une reutilisation de nombreuses competences acquises au cours de l'annee et tout au long de mes etudes d'ingenieur, notamment avec Node-RED, MQTT, le langage C et le cablage electronique. Comme je me souvenais de presque tout, je n'ai pas eu de difficulte majeure a developper le projet.</p>

<p>Une mention speciale pour MIT App Inventor, KiCad et ChirpStack, qui etaient des decouvertes pour moi, ajoutant de nouvelles connaissances a mon ensemble de competences. Le developpement d'une application mobile avec MIT App Inventor, bien que different de la programmation traditionnelle, m'a permis de comprendre les principes du developpement mobile et de l'interaction Bluetooth.</p>

<p>Je peux affirmer avec confiance que ce projet a ete mene a bien, et chaque etape que je visais a ete atteinte avec succes.</p>

<h3 class="section-title">Mon avis</h3>

<p>J'ai reellement apprecie ce cours car il impliquait de travailler sur un projet complet, depuis le composant capteur jusqu'a la creation du circuit imprime. C'est exactement le type de travail que j'apprecie : gerer un projet complet de bout en bout.</p>

<p>De plus, toucher a tous les aspects hardware et software etait interessant car cela m'a permis de comprendre l'ensemble du systeme et de rester informe de chaque aspect du projet. Travailler en equipe a ete benefique car nous avions une bonne communication, ce qui a facilite l'avancement du projet.</p>

<p>Ce qui m'a particulierement marque, c'est la coherence entre la fabrication du capteur au laboratoire AIME et son integration dans un systeme complet. Cette approche pedagogique, qui couvre l'ensemble de la chaine de valeur d'un objet connecte, est extremement formatrice et representative des defis rencontres dans le monde professionnel de l'IoT.</p>

<h4>Lien du projet</h4>
<p>Le projet complet est disponible sur <a href="https://github.com/Cyril-vsr/Capteur_Gaz">GitHub - Capteur Gaz</a>.</p>

</div>

<div class="lang-en">

<h1>Microcontroller Hardware / Open Source - Semester 9</h1>

<p><strong>Academic year</strong>: 2024-2025<br/>
<strong>Category</strong>: Embedded Electronics, IoT, Open Source Hardware</p>

<hr/>

<h2>PART A - General Overview</h2>

<h3 class="section-title">Overview</h3>

<p>This course, which follows the week of practical work at the AIME laboratory for gas sensor fabrication, focuses on integrating that sensor into a complete system based on open source microcontrollers. The main objective is to design an intelligent device capable of collecting, transmitting, and visualizing data from the gas sensor, using open source technologies and wireless communication protocols.</p>

<p>The project covers the entire chain, from the physical sensor to the mobile application, including microcontroller programming, setting up a LoRaWAN network, creating dashboards with Node-RED, and developing a mobile application with MIT App Inventor.</p>

<p><strong>Learning objectives</strong>:</p>
<ul>
<li>Understand and use open source microcontroller platforms (Arduino UNO, ESP32, ESP8266)</li>
<li>Interface sensors with a microcontroller via GPIO, I2C, SPI protocols</li>
<li>Set up wireless communication (LoRa, BLE, WiFi)</li>
<li>Design IoT flows with Node-RED for data processing and visualization</li>
<li>Develop a mobile application with MIT App Inventor</li>
<li>Create a real-time dashboard for sensor monitoring</li>
<li>Design a printed circuit board (PCB) with KiCad</li>
</ul>

<p><strong>Tools and technologies</strong>:</p>

<table>
<tr><th>Tool / Technology</th><th>Usage</th></tr>
<tr><td>Arduino UNO</td><td>Central microcontroller of the system</td></tr>
<tr><td>LoRa module RN2483</td><td>Long-range wireless communication</td></tr>
<tr><td>ChirpStack</td><td>LoRaWAN network server</td></tr>
<tr><td>Node-RED</td><td>Processing flows and IoT dashboard</td></tr>
<tr><td>MIT App Inventor</td><td>Android mobile app development</td></tr>
<tr><td>KiCad</td><td>Printed circuit board (PCB) design</td></tr>
<tr><td>MQTT</td><td>IoT messaging protocol</td></tr>
<tr><td>OLED display SSD1306</td><td>Local data display (I2C)</td></tr>
</table>

<hr/>

<h2>PART B - Experience and Context</h2>

<h3 class="section-title">Working Environment</h3>

<p>This course is a continuation of the AIME module where we fabricated a gas sensor based on WO3 nanoparticles. The challenge was now to transform this component into a functional and connected device by integrating it into a complete electronic system.</p>

<p>The work was carried out in several phases:</p>
<ol>
<li><strong>Wiring and hardware integration</strong>: connecting the sensor, Arduino UNO microcontroller, LoRa RN2483 module, OLED display, and auxiliary components (LED, resistors).</li>
<li><strong>Embedded programming</strong>: developing Arduino firmware in C language for sensor reading, OLED display, and data transmission via LoRa.</li>
<li><strong>Network infrastructure</strong>: configuring the ChirpStack LoRaWAN server and MQTT broker for data reception.</li>
<li><strong>Visualization and monitoring</strong>: creating Node-RED flows and a real-time dashboard to monitor gas levels.</li>
<li><strong>Mobile application</strong>: developing an Android application with MIT App Inventor for remote control and monitoring via Bluetooth.</li>
<li><strong>PCB design</strong>: introduction to KiCad for designing the signal conditioner printed circuit board.</li>
</ol>

<h3 class="section-title">My Role</h3>

<p>In this project, I was responsible for:</p>
<ul>
<li>Understanding the principles of open source microcontroller technologies</li>
<li>Designing and integrating the complete system (sensor, conditioner, microcontroller, communication)</li>
<li>Wiring the various components on a breadboard</li>
<li>Programming the Arduino firmware</li>
<li>Configuring Node-RED flows and the dashboard</li>
<li>Developing the MIT App Inventor mobile application</li>
<li>Conducting tests to verify system functionality and efficiency</li>
</ul>

<hr/>

<h2>PART C - Technical Aspects</h2>

<h3 class="section-title">In-depth Technical Concepts</h3>

<p>This section details the technical aspects of integrating the gas sensor with a microcontroller and developing applications for data collection and visualization.</p>

<h3>1. Open Source Microcontroller Platforms</h3>

<p>The project relies on using an <strong>Arduino UNO</strong>, an open source platform based on the ATmega328P microcontroller. Open source platforms such as Arduino, ESP32, and ESP8266 are at the heart of modern IoT thanks to their accessibility, community documentation, and library ecosystem.</p>

<p><strong>Key characteristics of the Arduino UNO</strong>:</p>
<ul>
<li>ATmega328P microcontroller at 16 MHz</li>
<li>14 digital I/O pins (GPIO), including 6 PWM</li>
<li>6 analog inputs (10-bit ADC)</li>
<li>Communication interfaces: UART, I2C (SDA/SCL), SPI (MOSI/MISO/SCK/SS)</li>
<li>Power supply: USB 5V or DC jack</li>
</ul>

<p><strong>Communication protocols used</strong>:</p>
<ul>
<li><strong>GPIO</strong>: Analog reading of the gas sensor (pin A0), LED control (pin D4)</li>
<li><strong>I2C</strong>: Communication with the SSD1306 OLED display (address 0x3C)</li>
<li><strong>UART (SoftwareSerial)</strong>: Communication with the LoRa RN2483 module (pins 10/11)</li>
<li><strong>SPI</strong>: Used in other configurations with ESP32 for additional sensors</li>
</ul>

<h3>2. Gas Sensor and Interfacing</h3>

<p>The gas sensor was fabricated during the <a href="./aime.html">AIME</a> laboratory training. It uses WO3 nanoparticles that provide high sensitivity to specific gases such as ethanol and ammonia. The sensor includes:</p>
<ul>
<li><strong>Sensitive layer</strong>: Nanoparticles deposited on aluminum interdigitated combs</li>
<li><strong>Heating element</strong>: Polysilicon resistor for adjusting operating temperature</li>
<li><strong>Calibration zone</strong>: Zone without nanoparticles for reference measurements</li>
</ul>

<table>
<tr><th>Pin</th><th>Description</th></tr>
<tr><td>2, 4</td><td>Sensitive layer (with nanoparticles)</td></tr>
<tr><td>3, 6</td><td>Heating element</td></tr>
<tr><td>5, 10</td><td>Temperature sensor</td></tr>
<tr><td>7, 9</td><td>Calibration layer</td></tr>
<tr><td>1, 8</td><td>Not used</td></tr>
</table>

<h3>3. Wiring and Hardware Integration</h3>

<p>To create a functional system, we wired the following components:</p>
<ul>
<li><strong>Arduino UNO</strong>: Central microcontroller of the system</li>
<li><strong>LoRa module (RN2483)</strong>: For long-range wireless communication</li>
<li><strong>Gas sensor</strong>: To detect gas concentrations</li>
<li><strong>OLED display SSD1306</strong>: For local data display (via I2C bus)</li>
<li><strong>Alert LED</strong>: Visual indicator of threshold exceedance</li>
</ul>

<p>The connections made are as follows:</p>

<table>
<tr><th>Component</th><th>Arduino Pin</th><th>Protocol</th><th>Detail</th></tr>
<tr><td>Gas sensor</td><td>A0</td><td>Analog (GPIO)</td><td>10-bit ADC reading</td></tr>
<tr><td>LoRa module TX</td><td>Pin 10</td><td>UART (SoftwareSerial)</td><td>Serial transmission</td></tr>
<tr><td>LoRa module RX</td><td>Pin 11</td><td>UART (SoftwareSerial)</td><td>Serial reception</td></tr>
<tr><td>OLED display SDA</td><td>A4</td><td>I2C</td><td>Data</td></tr>
<tr><td>OLED display SCL</td><td>A5</td><td>I2C</td><td>Clock</td></tr>
<tr><td>Alert LED</td><td>Pin 4</td><td>Digital GPIO</td><td>ON/OFF output</td></tr>
<tr><td>LoRa power</td><td>3.3V</td><td>-</td><td>Module power supply</td></tr>
<tr><td>Arduino power</td><td>USB</td><td>-</td><td>5V via USB</td></tr>
</table>

<h3>4. Arduino Programming and LoRa Communication</h3>

<p>The Arduino code consists of two main parts: initialization and data transmission.</p>

<p><strong>Initialization</strong>:</p>
<ul>
<li>Configuring the LoRa module with AppEUI and AppKey identifiers for registration on the LoRaWAN network (via ChirpStack)</li>
<li>Initializing the OLED display via I2C for visual feedback</li>
<li>Configuring the gas sensor pin as analog input and the LED as digital output</li>
</ul>

<p><strong>Data transmission</strong>:</p>
<ul>
<li>Reading gas sensor values via the ADC (analog-to-digital conversion)</li>
<li>Processing: comparison with an alert threshold (value &gt; 100)</li>
<li>Sending data via LoRa to the ChirpStack server</li>
<li>Updating the OLED display and activating the LED when threshold is exceeded</li>
</ul>

<p>This code initializes the LoRa module and gas sensor, reads sensor data every 10 seconds, and transmits it via LoRa. It also updates the OLED display and controls an LED based on the detected gas level.</p>

<p><strong>Wireless communication architecture</strong>:</p>
<ul>
<li><strong>LoRa (Long Range)</strong>: Low data rate, long range wireless communication protocol using the EU868 MHz frequency band. The RN2483 module communicates with the Arduino via software serial (SoftwareSerial).</li>
<li><strong>LoRaWAN</strong>: Network protocol on top of LoRa, managing authentication (OTAA with AppEUI/AppKey), packet routing, and device management via the ChirpStack server.</li>
<li><strong>BLE (Bluetooth Low Energy)</strong>: Used for communication between the Arduino and the MIT App Inventor mobile application, enabling local control and real-time data reading.</li>
</ul>

<h3>5. Node-RED: IoT Flows and Real-Time Dashboard</h3>

<p>Node-RED is a visual programming tool based on flow-based programming, particularly suited for rapid prototyping of IoT applications. In this project, Node-RED was used to receive, process, and display data from the LoRa sensor.</p>

<p><strong>Node-RED flow architecture</strong>:</p>

<p>The flow consists of four steps:</p>
<ol>
<li><strong>Data reception</strong>: An MQTT node listens for incoming messages from the ChirpStack LoRaWAN network. The MQTT broker is configured to receive frames from the network server.</li>
<li><strong>Data extraction</strong>: A function node decodes Base64-encoded data and extracts the gas level value.</li>
<li><strong>Processing and alerting</strong>: A second function node analyzes the gas level and triggers an alert if the value exceeds the defined threshold (e.g., 200).</li>
<li><strong>Visualization</strong>: A chart node displays gas levels in real time in the Node-RED dashboard.</li>
</ol>

<p><strong>Technical details of the flow</strong>:</p>
<ul>
<li><strong>MQTT node</strong>: Configured to connect to the ChirpStack broker and subscribe to the LoRa device topic</li>
<li><strong>Function nodes</strong>: JavaScript code for Base64 decoding, data extraction, and threshold analysis</li>
<li><strong>Chart node</strong>: Real-time graphical display with measurement history</li>
<li><strong>Dashboard</strong>: Accessible via <code>http://127.0.0.1:1880/ui</code>, responsive web interface for monitoring</li>
</ul>

<p>The Node-RED dashboard enables real-time visualization of gas levels detected by the sensor. Data is displayed as a time-series chart, allowing tracking of gas concentration evolution and quick identification of threshold exceedances.</p>

<h3>6. MIT App Inventor: Android Mobile Application</h3>

<p>MIT App Inventor is a visual development environment that allows creating Android applications without writing traditional code, using a block logic approach. In this project, we developed a mobile application to interact with the Arduino system via Bluetooth (BLE).</p>

<p><strong>Application features</strong>:</p>
<ul>
<li><strong>Bluetooth connection</strong>: The application connects to the Arduino via Bluetooth when the user presses the connection button. This establishes a bidirectional communication channel.</li>
<li><strong>LED control</strong>: The user can turn the alert LED on or off remotely using interface buttons.</li>
<li><strong>Gas level monitoring</strong>: The application continuously receives gas sensor values from the Arduino and displays them in real time.</li>
<li><strong>Alerts</strong>: A notification system warns the user when the gas level exceeds a predefined threshold.</li>
</ul>

<p><strong>Key application components</strong>:</p>
<ul>
<li><strong>Connection button</strong>: Establishes communication with the Arduino via the Bluetooth module</li>
<li><strong>LED control buttons</strong>: Send ON/OFF commands to the Arduino</li>
<li><strong>Dynamic label</strong>: Displays the current gas level received from the sensor</li>
<li><strong>Notifier</strong>: Alerts the user if the gas level exceeds the critical threshold</li>
</ul>

<p>The application provides a simple and intuitive interface for interacting with the Arduino system in real time, enabling both control and remote monitoring of environmental conditions.</p>

<h3>7. Printed Circuit Board Design with KiCad</h3>

<p>KiCad is an open source PCB design software. As part of this course, we were introduced to KiCad for designing the signal conditioner circuit for the gas sensor. This step allows transitioning from a breadboard prototype to a professional printed circuit board.</p>

<p><strong>Design steps</strong>:</p>
<ul>
<li>Creating the electrical schematic with component symbols</li>
<li>Defining physical footprints for components</li>
<li>PCB routing while respecting design rules (trace width, spacing)</li>
<li>Generating Gerber files for manufacturing</li>
</ul>

<hr/>

<h2>PART D - Analysis and Reflection</h2>

<h3 class="section-title">Skills and Knowledge Mobilized</h3>

<p>This project mobilized a broad set of cross-cutting skills:</p>

<ul>
<li>Understanding microcontroller architecture and using them in an IoT context</li>
<li>Designing a complete data acquisition system (sensor, conditioner, microcontroller) adapted to the application</li>
<li>Interfacing sensors with a microcontroller via GPIO, I2C, SPI, and UART protocols</li>
<li>Designing the electronic circuit for the sensor signal conditioner (design and simulation)</li>
<li>Developing embedded software for gas sensor usage and its HMI (OLED display)</li>
<li>Implementing wireless communication (LoRa, BLE, WiFi) for data transmission</li>
<li>Creating Node-RED flows for real-time data processing and visualization</li>
<li>Developing a mobile application with MIT App Inventor</li>
<li>Combining all these components into an intelligent and connected device</li>
<li>Understanding fundamental sensor and data acquisition concepts</li>
<li>Designing the datasheet for the fabricated sensor</li>
<li>Designing a PCB with KiCad</li>
</ul>

<h3 class="section-title">Self-assessment</h3>

<p>This course was a reuse of many skills acquired during the year and throughout my engineering studies, particularly with Node-RED, MQTT, C language, and electronic wiring. As I remembered almost everything, I did not encounter any major difficulty in developing the project.</p>

<p>A special mention for MIT App Inventor, KiCad, and ChirpStack, which were discoveries for me, adding new knowledge to my skill set. Developing a mobile application with MIT App Inventor, although different from traditional programming, allowed me to understand the principles of mobile development and Bluetooth interaction.</p>

<p>I can confidently say that this project was completed successfully, and every milestone I aimed for was achieved.</p>

<h3 class="section-title">My Opinion</h3>

<p>I really enjoyed this course because it involved working on a complete project, from the sensor component to the printed circuit board design. This is exactly the type of work I appreciate: managing a complete project from end to end.</p>

<p>Moreover, touching on all hardware and software aspects was interesting because it allowed me to understand the entire system and stay informed of every aspect of the project. Working as a team was beneficial because we had good communication, which facilitated project progress.</p>

<p>What particularly struck me was the coherence between the sensor fabrication at the AIME laboratory and its integration into a complete system. This pedagogical approach, which covers the entire value chain of a connected object, is extremely formative and representative of the challenges encountered in the professional IoT world.</p>

<h4>Project Link</h4>
<p>The complete project is available on <a href="https://github.com/Cyril-vsr/Capteur_Gaz">GitHub - Gas Sensor</a>.</p>

</div>

<div class="back-nav">
    <a href="./my-courses-2024-2025.html" data-i18n-html="back-courses-2024-2025">&larr; Retour aux Cours 2024-2025</a>
</div>

---
layout: default
title:  "Connected Bowl"
date:   2024-10-02 10:56:03 +0200
---

<style>
p {
  text-align: justify;
}
</style>

<div class="back-nav">
    <a href="./my-projects.html" data-i18n-html="back-projects">&larr; Retour aux Projets</a>
</div>

<div class="lang-fr">
<h1>Introduction</h1>
<p>Au cours de la semaine de bureau d'etude en programmation orientee objet, notre equipe a developpe une Gamelle Connectee. Ce projet visait a creer un systeme permettant de controler la distribution de nourriture pour animaux via une interface web, tout en integrant des capteurs et des indicateurs pour ameliorer l'experience utilisateur.</p>
</div>

<div class="lang-en">
<h1>Introduction</h1>
<p>During the week of object-oriented programming design office, our team developed a Connected Bowl. This project aimed to create a system to control the distribution of animal food using a web interface, while integrating sensors and indicators to improve the user experience.</p>
</div>

<div style="text-align: center;">
    <img src="/img/BE_Gamelle/Gamelle.png" alt="Connected Bowl" style="width: 30%;" onclick="openModal(this.src)"/>
</div>

<div class="lang-fr">
<h1>Objectifs du projet</h1>
<h2>Le systeme de Gamelle Connectee permet :</h2>
<p>De controler deux servomoteurs via une interface web pour choisir la nourriture a distribuer.<br/>
D'ajouter un capteur de pression pour surveiller la quantite de nourriture dans les reservoirs.<br/>
D'integrer des LEDs et un buzzer pour signaler a l'utilisateur le bon fonctionnement ou l'absence de nourriture.</p>
<p>Description du systeme : Le projet combine la programmation C++ sur un microcontroleur ESP8266, l'utilisation de capteurs et la creation d'une interface web. Voici les principales fonctionnalites :</p>

<h1>Interface web</h1>
<p>L'interface web permet de controler la distribution de nourriture en selectionnant deux compartiments differents. Deux boutons sont disponibles : un pour la Nourriture 1 et un pour la Nourriture 2.</p>
<p><strong>Distribution de nourriture</strong></p>
<p>Choix 1 : En selectionnant "Nourriture 1", le servomoteur correspondant est active pour ouvrir la trappe du compartiment 1.</p>
<p>Choix 2 : En selectionnant "Nourriture 2", le servomoteur associe ouvre la trappe du compartiment 2.</p>
<p><strong>Detection de nourriture</strong></p>
<p>Si de la nourriture est presente dans le compartiment, la trappe s'ouvre normalement.<br/>
Si le capteur de pression detecte une absence de nourriture :<br/>
Un buzzer emet une alerte sonore.<br/>
Une LED rouge s'allume pour indiquer l'absence de nourriture.</p>
<p><strong>Diagramme de classes</strong></p>
<p>L'architecture orientee objet de la Gamelle Connectee a ete concue pour moduler les interactions entre les composants (capteurs, servomoteurs, interface web) via des classes bien definies. Voici une representation visuelle du diagramme de classes utilise dans ce projet :</p>
</div>

<div class="lang-en">
<h1>Project objectives</h1>
<h2>The Connected Bowl system allows:</h2>
<p>To control two servomotors via a web interface to choose the food to distribute.<br/>
To add a pressure sensor to monitor the amount of food in the tanks.<br/>
To integrate LEDs and a buzzer to signal to the user the proper functioning or absence of food.</p>
<p>System description: The project combines C++ programming on an ESP8266 microcontroller, the use of sensors and the creation of a web interface. Here are the main features:</p>

<h1>Web interface</h1>
<p>The web interface allows to control the distribution of food by selecting two different compartments. Two buttons are available: one for Food 1 and one for Food 2.</p>
<p><strong>Food distribution</strong></p>
<p>Choice 1: By selecting "Food 1", the corresponding servomotor is activated to open the hatch of compartment 1.</p>
<p>Choice 2: By selecting "Food 2", the associated servomotor opens the hatch of compartment 2.</p>
<p><strong>Food detection</strong></p>
<p>If food is present in the compartment, the hatch opens normally.<br/>
If the pressure sensor detects an absence of food:<br/>
A buzzer emits an audible alert.<br/>
A red LED lights up to indicate the absence of food.</p>
<p><strong>Class diagram</strong></p>
<p>The object-oriented architecture of the Connected Bowl has been designed to modulate the interactions between the components (sensors, servomotors, web interface) via well-defined classes. Here is a visual representation of the class diagram used in this project:</p>
</div>

<img src="/img/BE_Gamelle/Class_Diag.png" alt="Class Diagram" style="width: 100%;" onclick="openModal(this.src)"/>

<div class="lang-fr">
<h1>Connexion au serveur</h1>
<p>Avant d'acceder a l'interface web, il est necessaire de s'assurer que l'ESP8266 est connecte au reseau WiFi. Vous pouvez obtenir l'adresse IP du microcontroleur via le moniteur serie ou un outil de scan reseau. Ensuite, l'interface web devient accessible via cette adresse IP dans un navigateur.</p>
</div>

<div class="lang-en">
<h1>Connecting to the server</h1>
<p>Before accessing the web interface, it is necessary to ensure that the ESP8266 is connected to the WiFi network. You can obtain the IP address of the microcontroller via the serial monitor or a network scanning tool. Then, the web interface becomes accessible via this IP address in a browser.</p>
</div>

<img src="/img/BE_Gamelle/Serveur.png" alt="Server" style="width: 100%;" onclick="openModal(this.src)"/>

<div class="lang-fr">
<h1>Conclusion</h1>
<p>Le projet Gamelle Connectee nous a permis de pratiquer plusieurs competences :</p>
<p>Programmation embarquee avec l'ESP8266 en C++.<br/>
Developpement d'une interface web interactive pour le controle a distance.<br/>
Integration de capteurs et d'actuateurs pour automatiser la distribution de nourriture et fournir un retour visuel et sonore.</p>
<p>Ce projet nous a confrontes a divers defis techniques, notamment la gestion des connexions WiFi, la manipulation de servomoteurs et la communication entre l'ESP8266 et l'interface web. Il illustre la combinaison de competences en IoT, electronique et developpement web, aboutissant a une solution innovante et pratique pour la gestion des repas des animaux.</p>
</div>

<div class="lang-en">
<h1>Conclusion</h1>
<p>The Connected Bowl project allowed us to practice several skills:</p>
<p>Embedded programming with the ESP8266 in C++.<br/>
Development of an interactive web interface for remote control.<br/>
Integration of sensors and actuators to automate food distribution and provide visual and audio feedback.</p>
<p>This project confronted us with various technical challenges, including managing WiFi connections, manipulating servomotors, and communicating between the ESP8266 and the web interface. It illustrates the combination of skills in IoT, electronics and web development, resulting in an innovative and practical solution for managing animal meals.</p>
</div>

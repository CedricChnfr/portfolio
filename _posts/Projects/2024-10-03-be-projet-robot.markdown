---
layout: default
title:  "BE Robot INSA"
date:   2024-10-02 10:52:03 +0200
categories: jekyll update
---

# Introduction
In the context of our real-time development project, we were tasked with designing and implementing various functionalities for a robot. The primary objective was to manage the robot's different tasks efficiently and securely using synchronization tools such as mutexes and semaphores. This report provides an overview of the project, the challenges encountered, and the solutions implemented.

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Robot_Project/Maquette.png" alt="Schéma du Projet Robot" style="width: 50%;" onclick="openModal(this.src)"/>
    <img src="/img/BE_Robot_Project/Schema.png" alt="Schéma du Projet Robot" style="width: 50%;" onclick="openModal(this.src)"/>
</div>

# Projet
The project involved developing several functionalities for a robot, including camera management, arena detection, and task synchronization. We used FreeRTOS to manage real-time tasks and ensure safe concurrent execution.

## Fonctionnalités du Projet

<style>
table {
    font-size: 0.8em;
}
</style>

| Nom de la fonction                | Description du comportement                                                                                                                                                                                                 | Entrées                                                                                       | Sorties                      |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|------------------------------|
| Démarrer serveur                  | Lancer serveur. Si échec, afficher un message et stopper le programme, sinon produire "serveur démarré".                                                                                                                     | Évènement : Start<br> Données : inputStream                                                   | Évènement : Serveur démarré  |
| Connecter au moniteur             | Attendre "serveur démarré", appeler AcceptClient et attendre "ouvrir socket". Si ok, produire "connexion établie".                                                                                                           | Évènement : Serveur démarré                                                                    | Évènement : connexion établie|
| Traiter message du moniteur       | Attendre "connexion établie". Tant que : Attendre message inputStream (Read). Si message = ouvrir com robot -> ouvrir comRobot. Si message = ouvrir camera -> ouvrir camera. Si message = fermer camera -> fermer camera.      | Évènement : connexion établie<br> Données : Mouvement                                         | Évènement : Ouvrir comRobot<br>Ouvrir camera<br>Fermer camera<br>Start robot<br>start recherche arène<br>start recherche robot |
| Etablissement de la connexion     | Attendre "serveur démarré", appeler AcceptClient et attendre "ouvrir socket". Si oui, connexion établie.                                                                                                                     | Évènement : ouvrirSocket<br>serveurDemarre                                                    | Évènement : connexionMonitor |
| Mettre en place la communication  | Attendre "ouvrir comRobot". Mettre en place la communication avec le robot. Si la communication est ok, poster "messageTomonACK", sinon poster "messageToMonNAC". Mettre à jour le statut de la com robot.                     | Évènement : ouvrir comRobot<br> Données : statut com robot<br>Message Poster                  |                              |
| Démarrer Robot                    | Attendre "Start robot". Si "Statut com robot" est actif, envoyer ordre de démarrage et mettre à jour "robot démarré".                                                                                                       | Évènement : ouvrir comRobot<br> Donnée : Statut com robot                                      | Donnée : robot démarré       |
| Déplacer robot                    | Toutes les 100ms, si "robot démarré" est vrai, lire "mouvement" et envoyer ordre, sinon rien.                                                                                                                                | Donnée : robot démarré                                                                         | Ordre                        |
| Envoyer message au moniteur       | Attendre "connexion établie". Tant que : Attendre messageToMon, envoyer le message au superviseur. Fin tant que.                                                                                                             | Évènement : connexion établie<br> Données : Outputstream                                       |                              |
| Lire niveau batterie              | Toutes les 500ms, si "robot démarré" est vrai, demander niveau de batterie au robot et le poster pour le moniteur. Sinon, rien.                                                                                             | Donnée : robot démarré<br> Donnée : Message Poster                                            |                              |
| Ouvrir/fermer la camera           | Attendre "ouvrir camera" ou "fermer camera". Ouvrir ou fermer la camera, envoyer un message au moniteur, mettre à jour "camera ouvert".                                                                                      | Ouvrir camera<br> Fermer camera<br> Évènement : Afficher image<br> Donnée : "Camera ouvert"    |                              |
| Afficher Image                    | Attendre "Afficher image". Toutes les 50ms, si "camera ouvert" est vrai, prendre une image du flux de la camera. Si "afficher arène" = vrai alors dessiner arène sur l'image. Poster l'image pour le moniteur.              | Évènement : Afficher image<br> Donnée : "Camera ouvert"<br> Donnée : Message Poster            |                              |
| Chercher Arène                    | Attendre "start recherche arène". Si "camera ouvert" est vrai : "camera ouvert = faux". Prendre une image du flux de la camera, analyser l'image et dessiner l'arène dessus. La poster pour le moniteur.                    | Évènement : start recherche arène<br> Donnée : Message Poster<br>afficher arène               |                              |
| Chercher Position                 | Attendre "start recherche robot". Si "camera ouvert" est vrai : Prendre une image du flux de la camera, analyser l'image et dessiner le robot. Mettre à jour "dessin robot".                                                | Évènement : start recherche robot<br> Donnée : "camera ouvert"<br> Donnée : Dessin robot       |                              |

<img src="/img/BE_Robot_Project/Graphe_Projet_Robot.png" alt="Graphe du Projet Robot" style="width: 100%;" onclick="openModal(this.src)"/>

## Existing Functionalities
Before diving into the new functionalities we implemented, it is important to note that several key functionalities were already established:

### Server Functionality
The server functionality is responsible for handling communication between the robot and external systems. This includes receiving commands and sending status updates.

### Monitor Connection
The connection with the monitor is established, enabling the robot to send real-time data and receive instructions from the monitoring system.

### Robot Movement
The functionality to move the robot is already in place, allowing the robot to navigate its environment based on the commands received.

## Battery Level Reading
Battery level reading involves monitoring the robot's battery status to ensure it has sufficient power to perform its tasks.
This ensures that the robot has sufficient power to perform its tasks and can alert the system if the battery level is low. By keeping track of the battery level, we can prevent unexpected shutdowns and ensure the robot operates efficiently.

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Robot_Project/Get_Battery_func.png" alt="Graphe du Projet Robot" style="width: 50%;" onclick="openModal(this.src)"/>
</div>

## Camera Management
Camera management involved several operations, such as opening, closing, and capturing images. We used mutexes to protect access to shared resources, such as the camera state and the camera object itself. Here is a code snippet illustrating the use of mutexes.

<div style="display: flex; justify-content: center; gap: 10px;">
  <img src="/img/BE_Robot_Project/Start_Camera_Func.png" alt="Graphe du Projet Robot" style="width: 30%;" onclick="openModal(this.src)"/>
  <img src="/img/BE_Robot_Project/Screen_Camera_Func.png" alt="Graphe du Projet Robot" style="width: 30%;" onclick="openModal(this.src)"/>
  <img src="/img/BE_Robot_Project/Stop_Camera_Func.png" alt="Graphe du Projet Robot" style="width: 30%;" onclick="openModal(this.src)"/>
</div>


## Arena Detection
For arena detection, we created a function that is called when the user presses a specific button. This function uses semaphores to synchronize execution and ensure that tasks are executed in the correct order.

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Robot_Project/Get_Arena_Func.png" alt="Graphe du Projet Robot" style="width: 50%;" onclick="openModal(this.src)"/>
</div>

# Conclusion
This project allowed us to apply advanced real-time programming concepts, such as using mutexes and semaphores for task synchronization. We successfully implemented the required functionalities for the robot while ensuring safe concurrent execution. The challenges we encountered helped us better understand the importance of synchronization and resource management in multithreaded programming.


<style>
p {
    text-align: justify;
}
.modal {
  display: none; 
  position: fixed; 
  z-index: 1; 
  padding-top: 60px; 
  left: 0;
  top: 0;
  width: 100%; 
  height: 100%; 
  overflow: auto; 
  background-color: rgb(0,0,0); 
  background-color: rgba(0,0,0,0.9); 
}

.modal-content {
  margin: auto;
  display: block;
  width: 80%;
  max-width: 700px;
}

.close {
  position: absolute;
  top: 15px;
  right: 35px;
  color: #f1f1f1;
  font-size: 40px;
  font-weight: bold;
  transition: 0.3s;
}

.close:hover,
.close:focus {
  color: #bbb;
  text-decoration: none;
  cursor: pointer;
}
</style>

<!-- Modal -->
<div id="myModal" class="modal">
  <span class="close" onclick="closeModal()">&times;</span>
  <img class="modal-content" id="img01">
</div>
<!-- JavaScript -->
<script>
function openModal(src) {
  var modal = document.getElementById("myModal");
  var modalImg = document.getElementById("img01");
  modal.style.display = "block";
  modalImg.src = src;
}

function closeModal() {
  var modal = document.getElementById("myModal");
  modal.style.display = "none";
}
</script>
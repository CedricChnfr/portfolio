---
layout: default
title:  "BE Robot INSA"
date:   2024-10-02 10:52:03 +0200
categories: jekyll update
---

<style>
table {
  font-size: 0.8em;
}
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

<div class="back-nav">
    <a href="./my-projects.html" data-i18n-html="back-projects">&larr; Retour aux Projets</a>
</div>

<div class="lang-fr">
<h1>Introduction</h1>
<p>Dans le cadre de notre projet de developpement temps reel, nous avons ete charges de concevoir et d'implementer differentes fonctionnalites pour un robot. L'objectif principal etait de gerer efficacement et de maniere securisee les differentes taches du robot en utilisant des outils de synchronisation tels que les mutex et les semaphores. Ce rapport fournit un apercu du projet, des defis rencontres et des solutions implementees.</p>
</div>

<div class="lang-en">
<h1>Introduction</h1>
<p>In the context of our real-time development project, we were tasked with designing and implementing various functionalities for a robot. The primary objective was to manage the robot's different tasks efficiently and securely using synchronization tools such as mutexes and semaphores. This report provides an overview of the project, the challenges encountered, and the solutions implemented.</p>
</div>

<div style="display: flex; justify-content: center;">
  <img src="/img/BE_Robot_Project/Maquette.png" alt="Robot Project Diagram" style="width: 50%;" onclick="openModal(this.src)"/>
  <img src="/img/BE_Robot_Project/Schema.png" alt="Robot Project Diagram" style="width: 50%;" onclick="openModal(this.src)"/>
</div>

<div class="lang-fr">
<h1>Projet</h1>
<p>Le projet impliquait le developpement de plusieurs fonctionnalites pour un robot, notamment la gestion de la camera, la detection de l'arene et la synchronisation des taches. Nous avons utilise FreeRTOS pour gerer les taches en temps reel et assurer une execution concurrente securisee.</p>
<h2>Fonctionnalites du projet</h2>
</div>

<div class="lang-en">
<h1>Project</h1>
<p>The project involved developing several functionalities for a robot, including camera management, arena detection, and task synchronization. We used FreeRTOS to manage real-time tasks and ensure safe concurrent execution.</p>
<h2>Project Functionalities</h2>
</div>

| Function Name                     | Behavior Description                                                                                                                                                                                                      | Inputs                                                                                        | Outputs                     |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|------------------------------|
| Start server                      | Launch server. If it fails, display a message and stop the program, otherwise produce "server started".                                                                                                                     | Event: Start<br> Data: inputStream                                                            | Event: Server started        |
| Connect to monitor                | Wait for "server started", call AcceptClient and wait for "open socket". If ok, produce "connection established".                                                                                                           | Event: Server started                                                                         | Event: connection established |
| Process monitor message           | Wait for "connection established". While: Wait for message inputStream (Read). If message = open com robot -> open comRobot. If message = open camera -> open camera. If message = close camera -> close camera.            | Event: connection established<br> Data: Movement                                              | Event: Open comRobot<br>Open camera<br>Close camera<br>Start robot<br>start arena search<br>start robot search |
| Establish connection              | Wait for "server started", call AcceptClient and wait for "open socket". If yes, connection established.                                                                                                                     | Event: openSocket<br>serverStarted                                                            | Event: connectionMonitor     |
| Set up communication              | Wait for "open comRobot". Set up communication with the robot. If communication is ok, post "messageToMonACK", otherwise post "messageToMonNAC". Update the robot com status.                                               | Event: open comRobot<br> Data: robot com status<br>Message Post                               |                              |
| Start Robot                       | Wait for "Start robot". If "robot com status" is active, send start order and update "robot started".                                                                                                                       | Event: open comRobot<br> Data: robot com status                                               | Data: robot started          |
| Move robot                        | Every 100ms, if "robot started" is true, read "movement" and send order, otherwise nothing.                                                                                                                                | Data: robot started                                                                           | Order                        |
| Send message to monitor           | Wait for "connection established". While: Wait for messageToMon, send the message to the supervisor. End while.                                                                                                             | Event: connection established<br> Data: Outputstream                                          |                              |
| Read battery level                | Every 500ms, if "robot started" is true, ask for battery level from the robot and post it for the monitor. Otherwise, nothing.                                                                                             | Data: robot started<br> Data: Message Post                                                    |                              |
| Open/close camera                 | Wait for "open camera" or "close camera". Open or close the camera, send a message to the monitor, update "camera open".                                                                                                   | Open camera<br> Close camera<br> Event: Display image<br> Data: "Camera open"                 |                              |
| Display Image                     | Wait for "Display image". Every 50ms, if "camera open" is true, take an image from the camera stream. If "display arena" = true then draw arena on the image. Post the image for the monitor.                             | Event: Display image<br> Data: "Camera open"<br> Data: Message Post                           |                              |
| Search Arena                      | Wait for "start arena search". If "camera open" is true: "camera open = false". Take an image from the camera stream, analyze the image and draw the arena on it. Post it for the monitor.                               | Event: start arena search<br> Data: Message Post<br>display arena                             |                              |
| Search Position                   | Wait for "start robot search". If "camera open" is true: Take an image from the camera stream, analyze the image and draw the robot. Update "robot drawing".                                                              | Event: start robot search<br> Data: "camera open"<br> Data: Robot drawing                     |                              |

<img src="/img/BE_Robot_Project/Graphe_Projet_Robot.png" alt="Robot Project Graph" style="width: 100%;" onclick="openModal(this.src)"/>

<div class="lang-fr">
<h2>Fonctionnalites existantes</h2>
<p>Avant de presenter les nouvelles fonctionnalites que nous avons implementees, il est important de noter que plusieurs fonctionnalites cles etaient deja etablies :</p>
<h3>Fonctionnalite serveur</h3>
<p>La fonctionnalite serveur est responsable de la gestion de la communication entre le robot et les systemes externes. Cela inclut la reception de commandes et l'envoi de mises a jour d'etat.</p>
<h3>Connexion au moniteur</h3>
<p>La connexion avec le moniteur est etablie, permettant au robot d'envoyer des donnees en temps reel et de recevoir des instructions du systeme de surveillance.</p>
<h3>Mouvement du robot</h3>
<p>La fonctionnalite de deplacement du robot est deja en place, permettant au robot de naviguer dans son environnement en fonction des commandes recues.</p>
<h2>Lecture du niveau de batterie</h2>
<p>La lecture du niveau de batterie consiste a surveiller l'etat de la batterie du robot pour s'assurer qu'il dispose d'une puissance suffisante pour effectuer ses taches. Cela garantit que le robot peut alerter le systeme si le niveau de batterie est faible. En suivant le niveau de batterie, nous pouvons prevenir les arrets inattendus et assurer un fonctionnement efficace du robot.</p>
</div>

<div class="lang-en">
<h2>Existing Functionalities</h2>
<p>Before diving into the new functionalities we implemented, it is important to note that several key functionalities were already established:</p>
<h3>Server Functionality</h3>
<p>The server functionality is responsible for handling communication between the robot and external systems. This includes receiving commands and sending status updates.</p>
<h3>Monitor Connection</h3>
<p>The connection with the monitor is established, enabling the robot to send real-time data and receive instructions from the monitoring system.</p>
<h3>Robot Movement</h3>
<p>The functionality to move the robot is already in place, allowing the robot to navigate its environment based on the commands received.</p>
<h2>Battery Level Reading</h2>
<p>Battery level reading involves monitoring the robot's battery status to ensure it has sufficient power to perform its tasks. This ensures that the robot has sufficient power to perform its tasks and can alert the system if the battery level is low. By keeping track of the battery level, we can prevent unexpected shutdowns and ensure the robot operates efficiently.</p>
</div>

<div style="display: flex; justify-content: center;">
  <img src="/img/BE_Robot_Project/Get_Battery_func.png" alt="Robot Project Graph" style="width: 50%;" onclick="openModal(this.src)"/>
</div>

<div class="lang-fr">
<h2>Gestion de la camera</h2>
<p>La gestion de la camera impliquait plusieurs operations, telles que l'ouverture, la fermeture et la capture d'images. Nous avons utilise des mutex pour proteger l'acces aux ressources partagees, telles que l'etat de la camera et l'objet camera lui-meme. Voici un extrait de code illustrant l'utilisation des mutex.</p>
</div>

<div class="lang-en">
<h2>Camera Management</h2>
<p>Camera management involved several operations, such as opening, closing, and capturing images. We used mutexes to protect access to shared resources, such as the camera state and the camera object itself. Here is a code snippet illustrating the use of mutexes.</p>
</div>

<div style="display: flex; justify-content: center; gap: 10px;">
  <img src="/img/BE_Robot_Project/Start_Camera_func.png" alt="Robot Project Graph" style="width: 30%;" onclick="openModal(this.src)"/>
  <img src="/img/BE_Robot_Project/Screen_Camera_func.png" alt="Robot Project Graph" style="width: 30%;" onclick="openModal(this.src)"/>
  <img src="/img/BE_Robot_Project/Stop_Camera_func.png" alt="Robot Project Graph" style="width: 30%;" onclick="openModal(this.src)"/>
</div>

<div class="lang-fr">
<h2>Detection de l'arene</h2>
<p>Pour la detection de l'arene, nous avons cree une fonction qui est appelee lorsque l'utilisateur appuie sur un bouton specifique. Cette fonction utilise des semaphores pour synchroniser l'execution et s'assurer que les taches sont executees dans le bon ordre.</p>
</div>

<div class="lang-en">
<h2>Arena Detection</h2>
<p>For arena detection, we created a function that is called when the user presses a specific button. This function uses semaphores to synchronize execution and ensure that tasks are executed in the correct order.</p>
</div>

<div style="display: flex; justify-content: center;">
  <img src="/img/BE_Robot_Project/Get_Arena_func.png" alt="Robot Project Graph" style="width: 50%;" onclick="openModal(this.src)"/>
</div>

<div class="lang-fr">
<h1>Conclusion</h1>
<p>Ce projet nous a permis d'appliquer des concepts avances de programmation temps reel, tels que l'utilisation de mutex et de semaphores pour la synchronisation des taches. Nous avons implementé avec succes les fonctionnalites requises pour le robot tout en assurant une execution concurrente securisee. Les defis rencontres nous ont permis de mieux comprendre l'importance de la synchronisation et de la gestion des ressources dans la programmation multithreadee.</p>
</div>

<div class="lang-en">
<h1>Conclusion</h1>
<p>This project allowed us to apply advanced real-time programming concepts, such as using mutexes and semaphores for task synchronization. We successfully implemented the required functionalities for the robot while ensuring safe concurrent execution. The challenges we encountered helped us better understand the importance of synchronization and resource management in multithreaded programming.</p>
</div>

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

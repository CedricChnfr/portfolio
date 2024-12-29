---
layout: default
title:  "BE Robot INSA"
date:   2024-10-02 10:52:03 +0200
categories: jekyll update
---

# Introduction
In the context of our real-time development project, we were tasked with designing and implementing various functionalities for a robot. The primary objective was to manage the robot's different tasks efficiently and securely using synchronization tools such as mutexes and semaphores. This report provides an overview of the project, the challenges encountered, and the solutions implemented.

<div style="display: flex; justify-content: center;">
  <img src="/img/BE_Robot_Project/Maquette.png" alt="Robot Project Diagram" style="width: 50%;" onclick="openModal(this.src)"/>
  <img src="/img/BE_Robot_Project/Schema.png" alt="Robot Project Diagram" style="width: 50%;" onclick="openModal(this.src)"/>
</div>

# Project
The project involved developing several functionalities for a robot, including camera management, arena detection, and task synchronization. We used FreeRTOS to manage real-time tasks and ensure safe concurrent execution.

## Project Functionalities

<style>
table {
  font-size: 0.8em;
}
</style>

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
  <img src="/img/BE_Robot_Project/Get_Battery_func.png" alt="Robot Project Graph" style="width: 50%;" onclick="openModal(this.src)"/>
</div>

## Camera Management
Camera management involved several operations, such as opening, closing, and capturing images. We used mutexes to protect access to shared resources, such as the camera state and the camera object itself. Here is a code snippet illustrating the use of mutexes.

<div style="display: flex; justify-content: center; gap: 10px;">
  <img src="/img/BE_Robot_Project/Start_Camera_Func.png" alt="Robot Project Graph" style="width: 30%;" onclick="openModal(this.src)"/>
  <img src="/img/BE_Robot_Project/Screen_Camera_Func.png" alt="Robot Project Graph" style="width: 30%;" onclick="openModal(this.src)"/>
  <img src="/img/BE_Robot_Project/Stop_Camera_Func.png" alt="Robot Project Graph" style="width: 30%;" onclick="openModal(this.src)"/>
</div>

## Arena Detection
For arena detection, we created a function that is called when the user presses a specific button. This function uses semaphores to synchronize execution and ensure that tasks are executed in the correct order.

<div style="display: flex; justify-content: center;">
  <img src="/img/BE_Robot_Project/Get_Arena_Func.png" alt="Robot Project Graph" style="width: 50%;" onclick="openModal(this.src)"/>
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

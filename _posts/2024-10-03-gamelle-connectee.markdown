---
layout: default
title:  "Gamelle Connectée!"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---
# Introduction
During the week of object-oriented programming design office, our team developed a Connected Bowl. This project aimed to create a system to control the distribution of animal food using a web interface, while integrating sensors and indicators to improve the user experience.
<div style="text-align: center;">
    <img src="/img/BE_Gamelle/Gamelle.png" alt="Graphe du Projet Robot" style="width: 30%;" onclick="openModal(this.src)"/>
</div>

# Project objectives
## The Connected Bowl system allows:

To control two servomotors via a web interface to choose the food to distribute.
To add a pressure sensor to monitor the amount of food in the tanks.
To integrate LEDs and a buzzer to signal to the user the proper functioning or absence of food.
System description
The project combines C++ programming on an ESP8266 microcontroller, the use of sensors and the creation of a web interface. Here are the main features:

# Web interface

The web interface allows to control the distribution of food by selecting two different compartments.
Two buttons are available: one for Food 1 and one for Food 2.
Food distribution

Choice 1: By selecting "Food 1", the corresponding servomotor is activated to open the hatch of compartment 1.

Choice 2: By selecting "Food 2", the associated servomotor opens the hatch of compartment 2.
Food detection

If food is present in the compartment, the hatch opens normally.
If the pressure sensor detects an absence of food:
A buzzer emits an audible alert.
A red LED lights up to indicate the absence of food.
Class diagram
The object-oriented architecture of the Connected Bowl has been designed to modulate the interactions between the components (sensors, servomotors, web interface) via well-defined classes. Here is a visual representation of the class diagram used in this project:

<img src="/img/BE_Gamelle/Class_Diag.png" alt="Graphe du Projet Robot" style="width: 100%;" onclick="openModal(this.src)"/>


# Connecting to the server
Before accessing the web interface, it is necessary to ensure that the ESP8266 is connected to the WiFi network. You can obtain the IP address of the microcontroller via the serial monitor or a network scanning tool. Then, the web interface becomes accessible via this IP address in a browser.

<img src="/img/BE_Gamelle/Serveur.png" alt="Graphe du Projet Robot" style="width: 100%;" onclick="openModal(this.src)"/>

# Conclusion
The Connected Bowl project allowed us to practice several skills:

Embedded programming with the ESP8266 in C++.
Development of an interactive web interface for remote control.
Integration of sensors and actuators to automate food distribution and provide visual and audio feedback.
This project confronted us with various technical challenges, including managing WiFi connections, manipulating servomotors, and communicating between the ESP8266 and the web interface. It illustrates the combination of skills in IoT, electronics and web development, resulting in an innovative and practical solution for managing animal meals.
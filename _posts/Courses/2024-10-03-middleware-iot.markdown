---
layout: default
title:  "Middleware for IoT"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

# Middleware for IoT

## PART A: GENERALITIES

### Presentation
The "Middleware for IoT" course, taught by T. Monteil, provided an in-depth look into communication protocols and middleware solutions for IoT. The course covered middleware architectures and their applications in IoT, focusing on how to create scalable and efficient communication systems.

## PART B: DESCRIPTIVE PART

### Experience Details

#### Environment and Context
During this course, I explored both theoretical and practical aspects of middleware for IoT. The increasing importance of efficient communication protocols in IoT highlighted the relevance of this subject. The hands-on sessions allowed me to apply the concepts learned in class to real-world scenarios, which was beneficial.

#### My Function
In this course, I was responsible for:
- Understanding different middleware architectures and their applications in IoT.
- Designing and implementing middleware solutions for IoT systems.
- Conducting experiments to test the efficiency and scalability of various middleware solutions.

## PART C: TECHNICAL PART

This section explores the technical aspects of middleware for IoT, focusing on communication protocols like MQTT, OneM2M and Node-RED and their applications in real-world scenarios.

### Technical Concepts Learned

#### 1. MQTT Protocol
I learned about the MQTT protocol, which is a lightweight messaging protocol designed for small sensors and mobile devices. MQTT uses a publish/subscribe model, making it efficient for IoT applications with limited bandwidth and resources. Key features include:
- **Architecture**: Devices (IoT nodes) publish and subscribe to topics via an MQTT broker.
- **IP Protocol**: MQTT operates over TCP/IP, ensuring reliable communication with minimal bandwidth usage.
- **Security**: MQTT supports username/password authentication and TLS encryption for secure communication.

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Middleware_IOT/mqtt.png" style="width: 50%;"/>
</div>
<br>

#### 2. Installing and Testing the MQTT Broker
I installed the Mosquitto broker, an open-source implementation of the MQTT protocol. Using commands like `mosquitto_pub` and `mosquitto_sub`, I tested the communication between the client and the broker, validating the setup.

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Middleware_IOT/mqtt_start.png" style="width: 60%;"/>
</div>

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Middleware_IOT/mqtt_sub_pub.png" style="width: 60%;"/>
</div>
<br>

#### 3. NodeMCU and MQTT Communication
I used the ESP8266 to create an IoT device that communicates via MQTT. The NodeMCU supports Wi-Fi and can be programmed using the Arduino IDE. I configured the board to publish and subscribe to MQTT topics, enabling real-time communication with other devices.

I utilized the ArduinoMqttClient library to program the board. The objective was to update the button status on the `button/state` topic each time the button was pressed. Additionally, each button press triggered the extraction of luminosity data, which was then published on the `light/state` topic.


<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Middleware_IOT/nodemcu_app.png" style="width: 70%;"/>
</div>
<br>

#### 4. Fast Application Prototyping with Node-RED
Node-RED is a visual programming tool that simplifies IoT application development. I used Node-RED to integrate real and simulated devices, accelerating development and providing clear visualization. I implemented the following features to manage sensor data and control actuators:

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Middleware_IOT/nodered.png" style="width: 70%;"/>
</div>

#### a. Check MQTT Connectivity
We added an MQTT receiver block on Node-RED subscribed to the `insa/luminosity` topic. The debugger confirmed correct value reception.

#### b. Sensors and Actuators
This flow simulates a light sensor sending values. A Switch node checks if luminosity exceeds 50, toggling LED ON or OFF:
- Light > 50 ⇒ LED ON
- Light ≤ 50 ⇒ LED OFF

#### c. Dashboard
Using `node-red-dashboard`, we created a GUI to visualize sensor data and control devices in real-time. Graphs display sensor data, and buttons control actuators.

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Middleware_IOT/nodered_dashboard.png" style="width: 30%;"/>
</div>
<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Middleware_IOT/nodered_led.png" style="width: 60%;"/>
</div>
<br>

#### d. Email and Notification
Implemented with `node-red-node-email`, this feature sends automatic alerts when switch state or luminosity changes, ensuring proactive monitoring and quick reactions to anomalies.


## PART D: ANALYTICAL PART

### The Knowledge and Skills Mobilized
- Understanding the main standards for the Internet of Things.
- Deploying and configuring IoT architectures using MQTT and OneM2M.
- Integrating new technologies into deployed architectures.
- Analyzing and evaluating optimal wireless network technologies.
- Suggesting optimal technological solutions for IoT networks.
- Optimizing communication protocols for IoT with respect to energy limitations and security concerns.
- Understanding the main processing techniques used for digital communication and explaining the basic structure of digital RF transmitter-receiver.

### Self-Evaluation

This course was my first experience with concepts like MQTT and OneM2M. I found them relatively simple to use and did not encounter significant difficulties. I am aware that tools like these are extremely useful in IoT projects. Thanks to libray that exist already and forums, it is pretty simple to put in place a communication system between devices.
Also I understood the utility of these concepts which lead to an utilization of few of them in our innovative project for a better functioning.


### My Opinion
This was one of my favorite courses as it combined both hardware and software aspects. I aspire to work as an embedded software engineer, and this course provided a perfect blend of both domains. The labs showed a clear progression in our work on the project. We started with simple MQTT communication, moved on to using the Arduino library for MQTT, and finally integrated everything with Node-RED. This step-by-step approach made the learning process both enjoyable and highly educational.



<div style="text-align: center;">
    <h1>Project Report</h1>
</div>

<div style="display: flex; justify-content: center;">
    <iframe src="/img/BE_Middleware_IOT/Report_Middleware_IOT.pdf" width="100%" height="800px" style="overflow: auto;" frameborder="0"></iframe>
</div>

<p style="text-align: center;">
    <a href="/img/BE_Middleware_IOT/Report_Middleware_IOT.pdf" target="_blank">Open Complete Report</a>
</p>

<p style="text-align: center;">
    <a href="/img/BE_Middleware_IOT/Lab_Subject_middleware.pdf" target="_blank">Open Lab Subject</a>
</p>

<style>
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
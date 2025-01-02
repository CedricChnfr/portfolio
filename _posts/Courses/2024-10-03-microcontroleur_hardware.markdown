---
layout: default
title:  "Microcontroller Open Source Hardware and Sensors"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

## Course: Microcontroller Open Source Hardware and Sensors

## PART A: GENERALITIES

### Presentation
After the week of labs at AIME to create a gas sensor, we had another course with the physical department on how to implement it in a bigger circuit with microcontrollers to collect and analyze its data. The objective of these courses was to create a datasheet for our sensor and to implement it with a microcontroller to create an application using a LoRa network able to display the results collected by the sensor.

## PART B: DESCRIPTIVE PART


### B.I. EXPERIENCE DETAILS

#### B.I.1. Environment and Context
The course focused on integrating the gas sensor created at AIME into a larger system using microcontrollers. We aimed to connect the sensor to a LoRa network and visualize the data on a dashboard. This involved both hardware and software components, including the creation of a PCB and circuit for the sensor, programming the microcontroller, and developing applications for data visualization.

#### B.I.2. Your Function
As I come from a network and computer science background, I focused on the high-level aspects of the course, such as creating the application and programming the microcontroller. I did not delve deeply into the hardware part, which involved creating a PCB and circuit for the integration of the gas sensor.

## PART C: TECHNICAL PART

### C.I.1 Presentation

#### Context
This section explores the technical aspects of integrating the gas sensor with a microcontroller and developing applications for data collection and visualization.

### C.I.2 Resolution of Problem

#### What
We connected an Arduino to the LoRa network using an RN2483 chip, programmed the Arduino to read data from the gas sensor, and developed applications to visualize the data using Node-RED and MQTT. Additionally, we created a mobile application using MIT App Inventor to control the system and view sensor data in real-time.

#### How
1. **Connecting to LoRa Network**:
   - Used an RN2483 chip to enable communication on the LoRa network.
   - Welded the component to a board for easier connection with the Arduino.
2. **Programming the Arduino**:
   - Connected the Arduino to INSA’s LoRa network using The Things Network library.
   - Programmed the Arduino to read values from the MQ-3B gas sensor and send data to the LoRa network.
3. **Data Visualization**:
   - Used Node-RED and MQTT to visualize the sensor data on a dashboard.
   - Developed a flow in Node-RED to decode the data and display it in real-time.
4. **Mobile Application**:
   - Created a mobile application using MIT App Inventor to control the system and view sensor data in real-time.
   - Implemented features such as connecting to the Arduino via Bluetooth, controlling an LED, and monitoring gas levels.

#### Why
To gain a comprehensive understanding of integrating sensors with microcontrollers and developing IoT applications. This knowledge is crucial for designing and implementing smart devices that can collect, process, and visualize data efficiently.

### C.I.3 The Knowledge and Skills Mobilized
- Understanding microcontroller architecture and how to use them.
- Designing data acquisition systems (sensor, conditioner, microcontroller) with respect to the application.
- Designing the electronic circuit of a sensor’s signal conditioner (design + simulation).
- Designing a shield to accommodate the gas sensor.
- Designing the software to use the gas sensor and its HMI.
- Combining all of the above-mentioned components into a smart device.
- Understanding basic notions of sensors, data acquisition: physics, electronics, and metrology point of view.
- Designing the datasheet of the sensor manufactured.

### C.I.4 Summary and Review
The course provided a thorough understanding of integrating sensors with microcontrollers and developing IoT applications. It was a good introduction to these concepts, especially for someone without a strong background in electronics or physics. However, the condensed schedule of the labs made it challenging to fully grasp all the concepts.

## PART D: ANALYTICAL PART

### D.I. Analysis of Skills
- **Theoretical Knowledge**: Gained insights into microcontroller architecture and sensor integration.
- **Operational Skills**: Developed skills in programming microcontrollers and designing data acquisition systems.
- **Analytical Skills**: Learned to assess the suitability of different integration techniques for IoT applications.

### D.II. Self Evaluation
- **Acquired Skills**: Developed a basic understanding of the concepts and processes involved in integrating sensors with microcontrollers and developing IoT applications. However, more focus on practical applications would be beneficial.
- **Skills to Develop**: Need to enhance proficiency in advanced data visualization techniques for IoT applications.

### D.III. Balance Sheet

#### Highlights
The course was highly relevant to my professional career, providing practical experience in integrating sensors with microcontrollers and developing IoT applications. The hands-on project work was particularly valuable in reinforcing the theoretical concepts.

### D.IV. Complementary Elements

#### Project Report
You can find the complete project report on [GitHub_Microcontroller_Project](https://github.com/Cyril-vsr/Capteur_Gaz).

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
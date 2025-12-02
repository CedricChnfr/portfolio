---
layout: default
title:  "Microcontroller Open Source Hardware and Sensors"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---



[← Back to My Courses 2024-2025](./my-courses-2024-2025.html)

# Microcontroller and Open-Source Hardware

## PART A: GENERALITIES

### Presentation
After the week of labs at AIME to create a gas sensor, we had another course with the physical department on how to implement it in a bigger circuit with microcontrollers to collect and analyze its data. The objective of these courses was to create a datasheet for our sensor and to implement it with a microcontroller to create an application using a LoRa network able to display the results collected by the sensor.

## PART B: DESCRIPTIVE PART

### Experience Details

#### Environment and Context
During this course, I had the opportunity to work on both theoretical and practical aspects of microcontroller technology. The relevance of microcontrollers in modern technology, especially in IoT applications was evident throughout the course. The hands-on sessions were particularly beneficial, allowing me to apply the concepts learned in class to real-world scenarios.

#### My Function
In this course, I was responsible for:
- Understanding the principles of microcontroller technologies.
- Designing and integrating microcontroller-based systems.
- Conducting experiments to test the functionality and efficiency of these systems.

## PART C: TECHNICAL PART

This section explain the technical aspects of integrating the gas sensor with a microcontroller and developing applications for data collection and visualization.

### Technical Concepts Learned

#### 1. Gas Sensor Fabrication
The gas sensor was fabricated during a training period at [AIME](./aime.html). It uses nanoparticles of WO3, which allows for high sensitivity to specific gases like ethanol and ammonia. The sensor includes:
- Sensitive layer: Nanoparticles deposited on interdigitated aluminum combs.
- Heating element: A polysilicon resistor to adjust operating temperature.
- Calibration zone: An area without nanoparticles for baseline measurements.

#### 2. Wiring and Integration
To create a functional system, we wired the following components:
- Arduino UNO: Central microcontroller for the system.
- LoRa Module (RN2483): For wireless communication.
- Gas Sensor: To detect gas concentrations.

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_microcontroleur/cablage.png" style="width: 50%;"/>
    <img src="/img/BE_microcontroleur/cablage2.png" style="width: 50%;"/>
</div>
<br>

The connections were as follows:
- Gas sensor: Connected to the analog pin A0 on the Arduino.
- LoRa module: TX and RX connected to pins 10 and 11 on the Arduino.
- Power: Arduino powered via USB, LoRa module powered through the 3.3V pin.

#### 3. Arduino Code
The Arduino code consists of two main parts: initialization and data transmission.

**Initialization:**
- Set up the LoRa module and gas sensor.
- Configure the OLED display for visual feedback.

**Data Transmission:**
- Read gas sensor values.
- Process and send the data via LoRa.

Here is a simplified version of the code:

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

This code initializes the LoRa module and gas sensor, reads the sensor data, and sends it via LoRa. It also updates an OLED display and controls an LED based on the gas level.


#### 4. Node-RED Overview
The Node-RED flow for this project is designed to receive, process, and display data from a LoRa sensor. The flow involves:
- Data Reception: An MQTT node listens for incoming sensor data from the LoRaWAN network ChirpStack.
- Data Extraction: A function node decodes the received Base64-encoded data and extracts the gas level value.
- Data Processing: Another function node analyzes the gas level and triggers an alert if the value exceeds a set threshold (e.g., 200).
- Visualization: A chart node displays the real-time gas levels in the Node-RED dashboard.

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_microcontroleur/nodered.png" style="width: 90%;"/>
</div>
<br>
<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_microcontroleur/dashboard.png" style="width: 40%;"/>
</div>
<br>

#### 5. MIT App Inventor
The MIT App Inventor app is designed to connect to the Arduino, allowing users to control the system and view sensor data in real-time. Features include:
- Connect to Arduino: The app connects to the Arduino via Bluetooth when the user presses a connect button.
- Control LED: Users can turn the LED on or off using buttons in the app.
- Gas Level Monitoring: The app continuously receives the current gas level from the sensor and displays it.
- Real-time Updates: Gas level data is updated in real-time on the app interface.

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_microcontroleur/mit_app.png" style="width: 40%;"/>
    <img src="/img/BE_microcontroleur/mit_app2.png" style="width: 40%;"/>
</div>
<br>

## PART D: ANALYTICAL PART

### The Knowledge and Skills Mobilized
- Understanding microcontroller architecture and how to use them.
- Designing data acquisition systems (sensor, conditioner, microcontroller) with respect to the application.
- Designing the electronic circuit of a sensor’s signal conditioner (design + simulation).
- Designing the software to use the gas sensor and its HMI.
- Combining all of the above-mentioned components into a smart device.
- Understanding basic notions of sensors, data acquisition: physics, electronics, and metrology point of view.
- Designing the datasheet of the sensor manufactured.

### Self Evaluation
This course was a reutilization of many skills acquired during the year and throughout my engineering studies, notably with Node-RED, MQTT, C language, and wiring. As I remembered almost everything, I didn't have any trouble developing the project. A special mention goes to MIT App Inventor, KitCad and ChirpStack, which was a first discovery for me, adding new knowledge to my skill set. I can confidently say that this project was carried out well, and every step I aimed to complete was successfully achieved.

### My Opinion
I really appreciated this course as it involved working on a project from the sensor component to the board creation. It is exactly the kind of work I enjoy handling a complete project from start to finish. Additionally, touching on all hardware and software was interesting as it allowed me to understand everything and stay informed about the project. Being part of a team was beneficial as we had good communication, which facilitated the project's advancement.


#### Project Link
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
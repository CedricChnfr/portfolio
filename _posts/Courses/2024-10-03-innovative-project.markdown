---
layout: default
title:  "Innovative Project"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

# Innovative Project

## PART A: GENERALITIES

### Presentation
The Innovative Project was a collaborative effort aimed at developing a solution for detecting water leaks in a house. The project involved splitting the tasks among team members, with each person focusing on different aspects such as hardware, embedded software, mobile application, website, protocol, machine learning, server, and 3D modeling (CAD). My responsibilities included embedded software development, security, data retrieval from the accelerometer for leak detection, mobile application development using React Native, and 3D modeling (CAD).

## PART B: DESCRIPTIVE PART

### Experience Details

#### Environment and Context
The project was carried out in a collaborative environment, with team members working together to brainstorm ideas, design prototypes, and implement solutions. This project is part of a multidisciplinary innovative initiative within the ISS curriculum. The objective is to develop a system that accurately detects water leaks in networks using a non-intrusive method. Initially, the focus was on detecting household water leaks. However, as the project progressed, the scope expanded to a distributed approach for public water network infrastructures. The project provided a platform to apply theoretical knowledge to practical scenarios, fostering innovation and creativity.


#### My Function
Our team consists of five members. In this project, I was responsible for:
- Developing the embedded software to retrieve data from the accelerometer for leak detection.
- Creating a mobile application using React Native to monitor and control the system.
- Designing 3D models (CAD) for the hardware components.
- Implementing security measures using AES (Advanced Encryption Standard) to ensure data integrity and confidentiality during transmission.


## PART C: TECHNICAL PART

This section explores the technical aspects of the innovative project, focusing on the problem analysis, solution design, and prototype implementation.

### Technical Concepts Learned

#### 1. Mobile Application Development
We chose React Native and Expo for developing our mobile application due to their efficiency in cross-platform development. React Native allows us to write JavaScript code that compiles into native code for both iOS and Android, reducing development time and maintenance efforts. Expo simplifies the setup process and provides access to native APIs, streamlining development.

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Innovative_Project/app_workspace.png" style="width: 20%;"/>
</div>

The application architecture includes:
- **assets**: Static resources like images and icons.
- **Config**: Manages node data including battery, vibration, sound levels, and leak status.
- **Screen**: Main screens such as Dashboard, Profile, Leak Detection, and Statistics.
- **App.js**: Entry point managing navigation.
- **app.json**: App configuration metadata.

Key screens and features:
- **WelcomeScreen**: Displays a welcome message and app logo.
- **HomeScreen**: Main entry point with login options.
- **DashboardScreen**: Overview of nodes, battery levels, and leak status.
- **HistoricScreen**: History of node activities and positions on a map.
- **LeakScreen**: History of detected leaks with details and contact options.
- **StatisticsScreen**: Detailed water consumption statistics.

<div style="text-align: center; display: flex; justify-content: center; gap: 20px;">
    <img src="/img/BE_Innovative_Project/HomeScreen.png" style="width: 20%;"/>
    <img src="/img/BE_Innovative_Project/DashboardScreen.png" style="width: 20%;"/>
    <img src="/img/BE_Innovative_Project/HistoricScreen.png" style="width: 20%;"/>
    <img src="/img/BE_Innovative_Project/LeakScreen.png" style="width: 20%;"/>
    <img src="/img/BE_Innovative_Project/StatisticsScreen.png" style="width: 20%;"/>
</div>
<br>

The app reads data from a JSON file in the Config directory, synchronized with the server for real-time updates. Future plans include enhanced data processing, real-time notifications, user authentication, and advanced analytics for better water usage insights.

#### 2. 3D Modeling (CAD)
We used SolidWorks for designing the mechanical model due to its robust features and user-friendly interface. The sensor case was designed to house the electronic board, considering size, shape, and material. It includes openings for sensor connections and mounting points. A dedicated space for the sound sensor ensures direct contact with the pipeline, essential for accurate leak detection. Screw holes secure the housing and electronic board, preventing false vibration readings. 

<div style="text-align: center; display: flex; justify-content: center; gap: 60px;">
    <img src="/img/BE_Innovative_Project/Assembly.png" style="width: 30%;"/>
    <img src="/img/BE_Innovative_Project/3D_Model.png" style="width: 40%;"/>
</div>
<br>

Simulation and testing were conducted to ensure the model meets specifications, with iterative 3D printing and stress analysis to refine the design.

<div style="text-align: center; display: flex; justify-content: center; gap: 60px;">
    <img src="/img/BE_Innovative_Project/simulation.png" style="width: 30%;"/>
</div>
<br>

#### 3. Security Features

##### Security Concern
Our project involves detecting water leaks using a distributed network of sensors (ESP32 and LoRa module). These sensors transmit metrics and preliminary analysis results. Without security, the system is vulnerable to attacks like replay, data tampering, and eavesdropping.

##### Solution
We implemented a lightweight security mechanism using AES-128 encryption with the TinyAES library (https://github.com/kokke/tiny-AES-c) and pre-shared symmetric keys. Each sensor encrypts data in Cipher Block Chaining (CBC) mode, using a unique Initialization Vector (IV) for each message. To balance security and efficiency, we transmit only two randomly generated bytes of the IV, while the remaining 14 bytes are static. Data is encrypted in blocks of 16 bytes, with padding applied using the PKCS#7 scheme to ensure proper block alignment.

- **AES-128 Encryption**: A symmetric encryption algorithm that uses a 128-bit key to encrypt and decrypt data.
- **Cipher Block Chaining (CBC)**: A mode of operation for block ciphers that uses a chaining mechanism to ensure that identical plaintext blocks yield different ciphertext blocks.
- **Initialization Vector (IV)**: A random or pseudo-random value used to initialize the encryption process, ensuring that identical plaintexts encrypt to different ciphertexts. In our implementation, 2 bytes are random, and 14 bytes are static.
- **Padding (PKCS#7)**: A padding scheme used to ensure that the plaintext length is a multiple of the block size (16 bytes for AES). PKCS#7 padding adds a series of bytes, each of which is equal to the number of padding bytes added.

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Innovative_Project/secu.png" style="width: 100%;"/>
</div>
<br>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Innovative_Project/aes_encrypt.png" style="width: 90%;"/>
</div>
<br>

## PART D: ANALYTICAL PART

### The Knowledge and Skills Mobilized
- Analyzing real-life problems.
- Suggesting technological solutions to problems.
- Implementing prototypes to solve problems.
- Developing embedded software for data retrieval from sensors.
- Creating mobile applications using React Native.
- Designing 3D models (CAD) for hardware components.
- Presenting and debating technical choices in English.
- Producing comprehensive reports in English for developed projects.


### Self Evaluation
This project was one of the most advanced projects of my life. Carrying a project from zero to completion, involving hardware, software, data storage, data transmission, modeling, server, AI, and application interface, it was a comprehensive project prototype ready for commercialization. Due to the project's scale, I couldn't work on all aspects, but I collaborated closely with my colleagues to stay informed. I am proud of my contributions, and it is functional. Being part of a dedicated team where everyone was eager to learn new things was a rewarding experience.

### My Opinion
This project was a good opportunity to explore various fields and conduct our own research on how to handle the project. In my opinion, the current session organization was great for delivering a prototype but not sufficient for delivering a fully functional final product with all the desired features. I discovered how to integrate many concepts learned during the year into a real project, similar to what we might be asked to do in a company. This project was a great experience, and I am proud of the results we achieved.



<div style="text-align: center;">
    <h1>Project Report</h1>
</div>

You can find the complete project report on [GitHub_Innovative_Project](https://github.com/what-a-leak).

<div style="display: flex; justify-content: center;">
    <embed src="/img/BE_Innovative_Project/Rapport_Projet_ISS.pdf" width="100%" height="800px" type="application/pdf">
</div>

<p style="text-align: center;">
    <a href="/img/BE_Innovative_Project/Rapport_Projet_ISS.pdf">Open the report</a>
</p>

<div style="display: flex; justify-content: center;">
    <embed src="/img/BE_Innovative_Project/Prez_final.pdf" width="100%" height="800px" type="application/pdf">
</div>

<p style="text-align: center;">
    <a href="/img/BE_Innovative_Project/Prez_final.pdf">Open the pptx presentation</a>
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
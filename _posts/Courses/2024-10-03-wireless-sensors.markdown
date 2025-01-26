---
layout: default
title:  "WSNL"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

# Wireless Sensor Networks and Localization

## PART A: GENERALITIES

### Presentation
The "Wireless Sensor Networks and Localization" course was an enlightening experience. Taught by S. Abdellatif and D. Dragomirescu, the course covered the principles and applications of wireless sensor networks (WSNs) and localization techniques. The focus was on understanding how WSNs operate, their architecture, and the various localization methods used in different scenarios.

## PART B: DESCRIPTIVE PART

### Experience Details

#### Environment and Context
During this course, I delved into the theoretical and practical aspects of WSNs and localization. The increasing importance of WSNs in various fields, such as environmental monitoring, healthcare, and smart cities, highlighted the relevance of this subject. The hands-on sessions allowed me to apply the concepts learned in class to real-world scenarios, which was beneficial.

#### My Function
In this course, I was responsible for:
- Understanding the principles and architecture of wireless sensor networks.
- Exploring various localization techniques and their applications.
- Conducting experiments to test the efficiency and accuracy of different WSN and localization solutions.

## PART C: TECHNICAL PART

This section explores the technical aspects of WSN technologies, focusing on the specifications of existing protocols like Zigbee and various MAC protocols.


#### 1. Classification of MAC Protocols

We can classify MAC protocols into three main sets: Contention-based, Schedule-based, and Hybrid (mix of the two).

**Contention-Based Protocols**

Contention-based protocols allow multiple nodes to compete for access to the communication channel. These protocols are designed to minimize collisions and ensure fair access to the medium.

- **S-MAC**: Utilizes synchronized sleep schedules to reduce idle listening and collisions, improving energy efficiency and network lifetime. Nodes alternate between sleep and active periods to conserve energy.

<img src="/img/BE_WSNL/S_MAC.png" alt="MAC Protocols" style="width: 50%; display: block; margin: 0 auto;">

- **B-MAC**: Incorporates a preamble sampling mechanism to reduce energy consumption during idle listening, suitable for low-power applications.

<img src="/img/BE_WSNL/B_MAC.png" alt="MAC Protocols" style="width: 60%; display: block; margin: 0 auto;">

- **T-MAC**: Uses duty cycling and preamble sampling to reduce energy consumption and improve scalability, suitable for low-traffic scenarios.

<img src="/img/BE_WSNL/T_MAC.png" alt="MAC Protocols" style="width: 60%; display: block; margin: 0 auto;">

**Schedule-Based Protocols**

Schedule-based protocols allocate time slots for communication, reducing contention and collisions. These protocols are suitable for applications requiring predictable communication patterns.

- **L-MAC**: An improvement over TDMA with decentralized slot allocation, enhancing scalability and adaptability while maintaining energy efficiency.

<img src="/img/BE_WSNL/L_MAC.png" alt="MAC Protocols" style="width: 60%; display: block; margin: 0 auto;">

**Hybrid Protocols**

Hybrid protocols combine contention-based and schedule-based methods to adapt to varying traffic conditions.

- **Z-MAC**: Switches between CSMA and TDMA modes depending on traffic levels, optimizing energy use and minimizing delays. Suitable for dynamic environments with fluctuating traffic patterns.

#### 2. Zigbee PHY and MAC Layer
Zigbee is a low-power, low-data-rate wireless communication protocol designed for IoT and WSN applications. It operates in the 2.4 GHz ISM band and uses IEEE 802.15.4 standard for PHY and MAC layers. 

<img src="/img/BE_WSNL/Zigbee_Layer.png" alt="Zigbee Network" style="width: 40%; display: block; margin: 0 auto;">

**Physical Layer (PHY)**

The Zigbee PHY layer is responsible for the modulation and demodulation of data, as well as the transmission and reception of radio signals. Key features include:

- **Frequency Bands**: Operates in the 2.4 GHz ISM band globally, with additional support for 868 MHz (Europe) and 915 MHz (USA) bands.
- **Modulation**: Uses Direct Sequence Spread Spectrum (DSSS) with Offset Quadrature Phase-Shift Keying (O-QPSK) modulation for robust communication.

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_WSNL/Zigbee_schema.png" style="width: 50%;"/>
    <img src="/img/BE_WSNL/Zigbee_graph.png" style="width: 50%;"/>
</div>
<br>

- **Data Rates**: Supports data rates of 250 kbps at 2.4 GHz, 40 kbps at 915 MHz, and 20 kbps at 868 MHz.
- **Transmission Power**: Typically ranges from -3 dBm to 20 dBm, allowing for flexible power management and range optimization.

**MAC Layer**

The Zigbee MAC layer provides several key features:

- **Channel Access Mechanism**: Uses CSMA-CA (Carrier Sense Multiple Access with Collision Avoidance) for channel access, minimizing collisions and ensuring the channel is clear before transmitting data.
- **Network Configurations**: Supports both beacon-enabled and non-beacon-enabled network configurations:
    - **Beacon-enabled networks**: Use periodic beacons to synchronize communication between devices, useful for applications requiring regular data transmission.
    - **Non-beacon-enabled networks**: Devices communicate asynchronously, suitable for applications with sporadic data transmission needs.
- **Security Mechanisms**: Includes robust security features to ensure data integrity and confidentiality:
    - **AES-128 Encryption**: Provides strong encryption for data transmitted over the network.

In summary, the Zigbee PHY and MAC layers are not negligible components of the Zigbee protocol, providing efficient, reliable, and secure communication for wireless sensor networks.

## PART D: ANALYTICAL PART

### The Knowledge and Skills Mobilized
- Analyzing and evaluating protocols dedicated to WSN/IoT.
- Suggesting optimal technological solutions for IoT networks.
- Optimizing communication protocols for IoT with respect to energy limitations and security concerns.
- Understanding the main processing techniques used for digital communication and explaining the basic structure of digital RF transmitter-receiver.

### Self Evaluation
I found the course on Wireless Sensor Networks and Localization to be extremely informative and engaging. The practical sessions and experiments helped me gain a deeper understanding of WSN technologies and localization methods. I feel now confident in my ability to analyze and optimize communication protocols for IoT applications.

However, I am conscious that the protocols are numerous, which means that I am not totally proficient in all of them. With the experience I will be able to learn a lot more in the field.

During the lab sessions, I developed a MAC layer in Python. This hands-on project allowed me to gain skilland see how data packets are managed and transmitted within a network.

Although I did not work on the physical layer directly, with the tool GNU Radio and I did not have specific sessions dedicated to using GNU Radio, so my practical experience with the physical layer remains limited.

### My Opinion
In my opinion, the first work that consisted of studying different protocols like LoRa, Zigbee, and Sigfox was enriching as it provided me an overview of how they operate and the main protocols they use.

The second part, where we had to study each MAC protocol, allowed me to delve deeper and helped me understand the intricacies of these protocols.

Finally, the lab sessions were useful to practice everything we worked on, reinforcing the theoretical knowledge with practical experience.

This course was well structured and provided me with a solid foundation in WSN and localization technologies.

<div style="text-align: center;">
    <h1>Project Report</h1>
</div>

Report on my analysis of the MAC layer for WSN :

<div style="display: flex; justify-content: center;">
    <iframe src="/img/BE_WSNL/Chanfreau_MAC_Layer.pdf" width="100%" height="800px" style="overflow: auto;" frameborder="0"></iframe>
</div>

<p style="text-align: center;">
    <a href="/img/BE_WSNL/Chanfreau_MAC_Layer.pdf" target="_blank">Download Complete Report</a>
</p>

Report on Zigbee, a WPAN for WSN :

<div style="display: flex; justify-content: center;">
    <iframe src="/img/BE_WSNL/Zigbee.pdf" width="100%" height="800px" style="overflow: auto;" frameborder="0"></iframe>
</div>

<p style="text-align: center;">
    <a href="/img/BE_WSNL/Zigbee.pdf" target="_blank">Download Complete Report</a>
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
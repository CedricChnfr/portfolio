---
layout: default
title:  "Energy Connected Object"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

# Course: Energy Connected Object

## PART A: GENERALITIES

### Presentation
The course "Energy for Connected Objects" aims to train engineers capable of designing and managing energy-autonomous connected systems. In a context where connected objects are multiplying, energy efficiency becomes a key issue, both for sustainability and for reducing operational costs.

This course explores innovative solutions to:

- Power connected devices: via batteries, wireless energy transfer methods, or using ambient energy sources.
- Optimize energy consumption: to extend the lifespan of devices and reduce their environmental impact.
- Design autonomous objects: that efficiently harvest, store, and manage energy.

### Some Recommendations
The key concepts covered in this course apply directly to engineering projects, particularly in the following areas:

- Connected health: wearable devices such as smartwatches or biomedical sensors.
- Smart cities: traffic sensors, autonomous streetlights, or surveillance systems.
- Industry 4.0: connected objects for industrial automation or predictive maintenance.

## PART B: DESCRIPTIVE PART

### B.I. EXPERIENCE DETAILS

#### B.I.1. Environment and Context
The "Energy for Connected Objects" course focuses on powering IoT devices efficiently, sustainably, and autonomously. Taught by Gaël Loubet, the course provides an in-depth exploration of electricity storage, ambient energy harvesting, and wireless power transfer technologies. The primary objective is to design energy-efficient connected objects that operate without reliance on traditional batteries or wired power.

#### B.I.2. Your Function
The practical work presented some challenges. The manipulations, although very formative, were sometimes hindered by technical problems related to the equipment used. These problems, understandable for a first year of PCB use, nevertheless illustrated real engineering situations where unforeseen events must be managed rigorously.

## PART C: TECHNICAL PART

### C.I.1 Presentation

#### Context
This lab report explores methods for powering connected devices by harvesting energy from electromagnetic fields and transmitting power wirelessly. The goal is to develop self-powered devices, enhancing charging efficiency, sensing capabilities, and secure data transmission.

### C.I.2 Resolution of Problem

#### What
We investigated the power requirements of a small red light, tested approaches for direct energy usage and storage, and experimented with various technologies for energy management and conversion.

#### How
1. **Study of the Load and Design**:
   - Calculated the DC power required by the LED SML-D12U1WT8 for different usage scenarios.
   - Determined the energy required to light the LED for 1 second.
   - Configured capacitance and activation/deactivation voltage thresholds for optimal performance.

2. **Rectifier Characterization**:
   - Tested the rectifier at different frequencies (868 MHz and 2.45 GHz) to determine optimal performance.
   - Measured voltage across the potentiometer during frequency and RF power sweeps.

3. **Antenna Choice**:
   - Selected the most appropriate antenna for our application based on radiation pattern and distance efficiency.

4. **Ambient Electromagnetic Energy Harvesting**:
   - Proposed tests to measure power available at the rectifier input for the targeted frequency using a spectrum analyzer.

5. **Radiative Electromagnetic Wireless Power Transfer**:
   - Estimated the maximum reachable distance between a power source and the rectenna.
   - Suggested optimization strategies for antenna gain and frequency adjustment.

#### Why
To develop efficient, self-powered wireless sensor networks (WSNs) that can significantly enhance energy management and operational capabilities in diverse fields, including healthcare, smart homes, and industrial applications.

### C.I.3 The Knowledge and Skills Mobilized
- **Theoretical Knowledge**: Understanding of energy harvesting, storage, and wireless power transfer technologies.
- **Operational Skills**: Implementing energy harvesting and storage solutions, using tools to design autonomous systems, and analyzing system performance.
- **Analytical Skills**: Assessing specific energy needs and identifying suitable solutions based on system constraints.

### C.I.4 Summary and Review
The lab provided a comprehensive understanding of powering connected devices through energy harvesting and wireless power transfer. The practical work, although challenging, was formative and illustrated real engineering situations where unforeseen events must be managed rigorously. The findings highlight the potential for developing efficient, self-powered WSNs, enhancing energy management and operational capabilities in various applications.

## PART D: ANALYTICAL PART

### D.I. Skills Analysis

#### Theoretical Knowledge:
The course allowed me to discover the fundamental concepts related to energy for connected objects. I acquired knowledge on:

- The different methods of powering embedded systems, such as the use of batteries, wireless energy transfer, and ambient energy harvesting.
- The physical and technological principles behind energy sources like solar, mechanical, thermal, and electromagnetic energy.
- The trade-offs to consider between autonomy, complexity, and energy performance of IoT systems.

#### Operational Skills:
Thanks to the practical work, I developed practical skills such as:

- Implementing energy harvesting and storage solutions.
- Using tools to design an autonomous system capable of optimizing its energy resource usage.
- Analyzing the performance of connected systems in terms of energy efficiency.
- Mastering the architecture of an energy management system.
- Sizing the storage element according to the specifications.

#### Analytical Skills:
I learned to assess the specific energy needs of a connected object and to identify the most suitable solutions based on system constraints.

### D.II. Self-Assessment

#### Acquired Skills:
This course allowed me to understand how to efficiently manage the energy of connected objects and design robust and autonomous systems. I also learned to optimize energy consumption based on usage scenarios.

#### Skills to Develop:
Despite the knowledge acquired, I feel the need to deepen certain technical aspects such as the physical modeling of complex energy systems and integrating these models into simulation tools.

### D.III. Review
At the beginning of the course, I did not expect to find this field so relevant to my professional career. However, the clarity of the explanations and the well-defined structure of the course changed my perspective. I particularly appreciated how complex concepts were presented in an accessible manner, even for someone with little background in electronics or physics.

Nevertheless, the practical work presented some challenges. The manipulations, although very formative, were sometimes hindered by technical problems related to the equipment used. These problems, understandable for a first year of PCB use, nevertheless illustrated real engineering situations where unforeseen events must be managed rigorously.

### D.IV. Additional Elements
To go further, it could be interesting to integrate a more interactive approach, such as the collaborative design of a real energy system, or to delve deeper into use cases in specific fields like healthcare or smart cities.


## Project Report
To go further, it could be interesting to integrate a more interactive approach, such as the collaborative design of a real energy system, or to delve deeper into use cases in specific fields like healthcare or smart cities.

<div style="display: flex; justify-content: center;">
    <iframe src="/img/BE_Energy_Connected_Object/Report_Energy_Boukouiss_Chanfreau.pdf" width="100%" height="800px" style="overflow: auto;" frameborder="0"></iframe>
</div>

<p style="text-align: center;">
    <a href="/img/BE_Energy_Connected_Object/Report_Energy_Boukouiss_Chanfreau.pdf" target="_blank">Download Complete Report</a>
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

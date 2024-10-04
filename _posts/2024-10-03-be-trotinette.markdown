---
layout: default
title:  "BE Trotinette"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---
# Introduction
This part presents the study and modeling of a closed-loop control system for a DC motor, with emphasis on the design and implementation of a digital corrector. The studied system includes several key components: the corrector, the chopper, the motor, a transducer, and a signal conditioner. 
The main objective of this project is to design a digital corrector to ensure precise and stable control of the motor in current to ensure its torque. This involves the modeling of each component of the system, the synthesis of the corrector, and the verification of the stability and performance of the closed loop.

# Project Development

## System Modeling
The project starts with the modeling of the DC motor and its associated components, including the transducer and the signal conditioner. The motor is represented by its electrical model and transfer function, while the transducer is modeled based on data from its datasheet.

<img src="/img/BE_Trotinette/Chaine_Acq.png" alt="Graphe du Projet Robot" style="width: 100%;" onclick="openModal(this.src)"/>

The next phase involves the design of the PI (Proportional Integral) corrector, which is used to ensure the stability and accuracy of the control. The open-loop system is analyzed to determine the phase margins and time constants, thus ensuring an optimal dynamic response.

## Simulation and Implementation
Simulations are performed using Simulink to verify the performance of the corrector and the closed-loop system. A bilinear transformation is applied to model the discrete behavior of the corrector when implemented on an STM32 microcontroller. Particular attention is paid to reaction times, system protection against overloads, and optimization of corrector settings.

### Free Regim
<img src="/img/BE_Trotinette/Graphe_sat.png" alt="Graphe du Projet Robot" style="width: 100%;" onclick="openModal(this.src)"/>
In green the instruction to apply, in yellow the current in the motor.
Two phases:
Phase one:
The system is in the control loop, it is in saturation.
Phase two:
The control cannot reach the requested current because it does not have sufficient charge. The motor therefore operates at a voltage of 24 V with its own voltage/current ratio.

### Step Response
<img src="/img/BE_Trotinette/Graphe_response.png" alt="Graphe du Projet Robot" style="width: 100%;" onclick="openModal(this.src)"/>
This gives a rise time of approximately 1.3ms, which is consistent with the Simulink simulations.

## PI Corrector Design
The heart of the control system is the proportional-integral (PI) corrector. The open-loop corrector design aimed to guarantee a phase margin of more than 45° to ensure system stability. A simple model was established using the electrical and mechanical time constant of the motor, with simulations confirming that the performance criteria were met.

## Bilinear Transform
We then applied a bilinear transform to convert this corrector into a discrete version, since the corrector would be implemented on an STM32 microcontroller. The discretization frequency was calculated to minimize the phase margin loss and ensure that the discrete-time performance was comparable to the analog version.

# Conclusion
The project has developed a reliable and efficient control system for a DC motor, integrating a digital corrector that has been simulated and then implemented on a microcontroller. The validation of the performances, both in simulation and in real implementation, shows that the system is able to precisely regulate the motor, while respecting the constraints imposed by the implementation environment.

This project paves the way for industrial applications where precise control of electromechanical systems is necessary, and provides a solid basis for future developments towards more complex or more optimized systems.
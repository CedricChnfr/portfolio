---
layout: default
title:  "Service Oriented Architecture"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

## Course: Service Oriented Architecture

## PART A: GENERALITIES

### Presentation
The "Service Oriented Architecture" course, taught by Nawal Guermouche, aims to explore legacy and modern architectures for software engineering. The theoretical part is delivered through a MOOC (Massive Open Online Course) with various videos on different topics. This course is particularly interesting for students with a computer science background as it covers different standard architectures that are likely to be encountered in the field.

## PART B: DESCRIPTIVE PART

### B.I. EXPERIENCE DETAILS

#### B.I.1. Environment and Context
The practical part of this course is divided into two segments. The first segment introduces three different architectures: SOAP, REST, and microservices. The second segment involves a project that delves deeper into the most recent type of software architecture, microservices.
#### B.I.2. Your Function
During the practical sessions, I engaged in hands-on activities that involved implementing and configuring these architectures. The project work required collaboration and problem-solving to design and deploy a microservice architecture.

## PART C: TECHNICAL PART

### C.I.1 Presentation

#### Context
This lab report explores the implementation and configuration of different service-oriented architectures, focusing on SOAP, REST, and microservices. The goal is to understand their functionalities, advantages, and limitations.

### C.I.2 Resolution of Problem

#### What
We explored three main architectures:
1. **SOAP (Simple Object Access Protocol)**: A legacy architecture that uses WSDL (Web Service Description Language) for defining services.
2. **REST (Representational State Transfer)**: An architecture that uses HTTP protocols for creating, reading, updating, and deleting resources.
3. **Microservices**: A modern architecture that divides a service into independent microservices, each handling a specific functionality.

#### How
1. **SOAP**:
   - Implemented a web service using SOAP.
   - Created and consumed WSDL documents.
   - Developed services such as User Management, Volunteer Management, and Request Management.
2. **REST**:
   - Developed RESTful APIs using HTTP methods (POST, GET, PUT, DELETE).
   - Implemented services like User Management, User Request Service, Volunteer Management, and Feedback Service.
   - Tested the APIs using tools like Postman.
3. **Microservices**:
   - Designed a microservice architecture using Spring Boot.
   - Implemented communication between microservices using REST interfaces.
   - Deployed the microservices using containerization tools like Docker.
   - Automated deployment using Microsoft Azure and GitHub Actions.

#### Why
To gain a comprehensive understanding of different service-oriented architectures and their applications in real-world scenarios. This knowledge is crucial for designing scalable, efficient, and maintainable software systems.

### C.I.3 The Knowledge and Skills Mobilized
- Understanding of service-oriented architecture concepts and features.
- Development of distributed architectures using web services.
- Deployment and configuration of SOA using SOAP and REST.
- Design, development, and deployment of microservice architectures.
- Mastering the architecture of energy management systems, simple storage, energy recovery, and sizing storage elements according to specifications.

### C.I.4 Summary and Review
The course provided a thorough understanding of service-oriented architectures. The practical sessions were particularly beneficial in illustrating the concepts. However, the focus on legacy architectures like SOAP could be reduced in favor of more emphasis on modern architectures like REST and microservices.

## PART D: ANALYTICAL PART

### D.I. Analysis of Skills
- **Theoretical Knowledge**: Gained insights into different service-oriented architectures and their applications.
- **Operational Skills**: Developed skills in implementing and configuring SOAP, REST, and microservice architectures.
- **Analytical Skills**: Learned to assess the suitability of different architectures based on project requirements.

### D.II. Self Evaluation
- **Acquired Skills**: Mastered the design, implementation, and deployment of service-oriented architectures.
- **Skills to Develop**: Need to enhance understanding of advanced cryptographic techniques and their practical applications in IoT security.

### D.III. Balance Sheet

#### Highlights
The course was highly relevant to my professional career, providing practical experience in modern software architectures. The hands-on project work was particularly valuable in reinforcing the theoretical concepts.

### D.IV. Complementary Elements
To further enhance the learning experience, integrating more interactive approaches and focusing on modern architectures would be beneficial.


## Project Report

<div style="display: flex; justify-content: center;">
    <iframe src="/img/BE_service_architecture.pdf" width="100%" height="800px" style="overflow: auto;" frameborder="0"></iframe>
</div>

<p style="text-align: center;">
    <a href="/img/BE_service_architecture.pdf" target="_blank">Download Complete Report</a>
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
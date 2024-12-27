---
layout: default
title:  "Emerging Network Technologies"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

## Course: Emerging Network Technologies

## PART A: GENERALITIES

### Presentation
Emerging Networks is a course taught by Slim Abdelatif. It is a short course of only a few hours about new paradigms for networks. We discovered these paradigms during the theoretical class and had the opportunity to manipulate Software Defined Network (SDN) during practical courses. Unfortunately, as all the labs are placed after the deadline of the portfolio report, I will not be able to talk about them in this part, which shortens the content of this section.

## PART B: DESCRIPTIVE PART

### B.I. PRESENTATION OF EXPERIENCES LINKED TO THE TRAINING
During the course adn pratical work, we engaged in various hands-on activities and projects that allowed us to apply the theoretical knowledge gained in class to real-world scenarios, enhancing our understanding of emerging network technologies.

### B.II. EXPERIENCE DETAILS

#### B.II.1. Environment and Context
In this course, we studied new network paradigms. The first one that we studied in detail is SDN. In this paradigm, we remove all intelligence from the network devices (switches and routers) and centralize it in a single point, which is the network controller. This allows network administrators to take decisions and pilot the network by interacting with the network controller using classical programming. It also allows handling packets more precisely and implementing network behavior on demand, independent of the functionalities proposed by the device manufacturer.

The other paradigm that we saw is the Locator/Identifier Separation Protocol (LISP). It consists of attributing two IP addresses to a device: one used for localization and the other to identify the device uniquely. This allows the mobility of nodes as only one address changes and not the other. To contact another node, we use the identifier node that never changes, and a protocol similar to DNS is run to find the localization address to reach the node. However, this is only possible if the edge router of the network is compatible with the LISP protocol, as it is this router that will execute the translation.

## PART C: TECHNICAL PART

### C.I.1 Presentation

#### Context
This section explores the technical aspects of SDN and LISP, focusing on their applications in network management and mobility.

### C.I.2 Resolution of Problem

#### What
We examined SDN and LISP technologies, their architectures, and their applications in network management and mobility.

#### How
1. **SDN**:
   - Centralized network intelligence in a network controller.
   - Enabled precise packet handling and on-demand network behavior implementation.
2. **LISP**:
   - Attributed two IP addresses to devices for localization and identification.
   - Enabled node mobility by changing only the localization address.

#### Why
To gain a comprehensive understanding of SDN and LISP technologies and their applications in real-world scenarios. This knowledge is crucial for designing flexible, efficient, and maintainable network systems.

### C.I.3 The Knowledge and Skills Mobilized
- Understanding and mastering the fundamentals of emerging network paradigms applied to IoT.
- Developing applications for traffic management using SDN.
- Understanding LISP and its role in enabling node mobility.
- Integrating SDN and LISP for enhanced network management and mobility.

### C.I.4 Summary and Review
The course provided a thorough understanding of SDN and LISP technologies. The combination of theoretical classes and practical labs (though not yet completed) was particularly beneficial in illustrating the concepts. However, the relevance of SDN to IoT networks was questioned, as SDN is more suited for core networks.

## PART D: ANALYTICAL PART

### D.I. Analysis of Skills
- **Theoretical Knowledge**: Gained insights into SDN and LISP technologies and their applications.
- **Operational Skills**: Developed skills in implementing and configuring SDN and LISP solutions.
- **Analytical Skills**: Learned to assess the suitability of different network management techniques based on network requirements.

### D.II. Self Evaluation
- **Acquired Skills**: Developed a solid understanding of SDN and LISP concepts and their practical applications. However, more focus on advanced topics would be beneficial.
- **Skills to Develop**: Need to deepen knowledge in continuous integration and continuous deployment (CI/CD) practices for network management.

### D.III. Balance Sheet

#### Highlights
The course was highly relevant to my professional career, providing practical experience in modern network management solutions. The hands-on project work was particularly valuable in reinforcing the theoretical concepts.

### D.IV. Complementary Elements

#### Project Report

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
</style>
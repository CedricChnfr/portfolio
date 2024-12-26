---
layout: default
title:  "Cloud Edge"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

# Course: Cloud and Edge Computing

## PART A: GENERALITIES

### Presentation
The Cloud and Edge Computing course provides a comprehensive understanding of hybrid architectures that optimize data processing and resource utilization. It bridges the gap between centralized cloud systems and decentralized edge solutions, preparing engineers to address modern technological challenges.

Taught by  Sami Yangui, the course delves into virtualization technologies, cloud services, and edge infrastructures. It emphasizes the design, deployment, and management of architectures that blend the low-latency benefits of edge computing with the scalability of cloud environments.

This training is particularly relevant in today’s context, where the rise of IoT, real-time applications, and 5G networks necessitates expertise in these fields. Students gain hands-on experience with tools such as Kubernetes, Docker, and cloud platforms like AWS and Azure, enabling them to create robust, efficient systems.

The course also addresses advanced topics, including energy-efficient protocols, security challenges, and real-time data analysis at the edge, equipping learners to deliver impactful solutions in sectors such as smart cities, healthcare, and Industry 4.0.

By combining theory and practical projects, this course fosters not only technical expertise but also an appreciation for ethical and sustainable innovation, ensuring that engineers are well-prepared for the demands of a rapidly evolving digital landscape.

## PART B: DESCRIPTIVE PART

### B.I. PRESENTATION OF EXPERIENCES LINKED TO THE TRAINING

During the Cloud and Edge Computing course, I explored both theoretical and practical aspects of hybrid architectures for modern computing environments. This course provided hands-on experience with virtualization techniques, cloud services, and edge computing solutions.

### B.II. EXPERIENCE DETAILS

#### B.II.1. Environment and Context

The Cloud and Edge Computing course was taught by Sami Yangui, emphasizing the importance of virtualization technologies in modern cloud infrastructures. The increasing demand for scalable, efficient, and low-latency services highlights the relevance of this subject in fields such as IoT, real-time systems, and 5G networks.

The course included:

- **Theoretical Classes**: Focused on cloud architecture, virtualization methods, and deployment models.
- **Practical Labs**: Hands-on sessions using tools like OpenStack for infrastructure development and edge computing implementations.

#### B.II.2. Your Function

Role in Labs and Projects:

- Designed and implemented virtualized environments using OpenStack.
- Developed an edge computing solution leveraging proximity-based data processing to minimize latency.
- Created and managed virtual machines (VMs) to simulate real-world cloud scenarios.
- Addressed the challenges of infrastructure deployment through Python-based automation.


## PART C: TECHNICAL PART


### C.I.1 Presentation

During our labs, I had the opportunity to use OpenStack, an open-source software that creates and manages different virtual machines (VMs). One of the projects required me to implement an infrastructure with a calculator service accessible from the public internet and four VMs on a private network performing arithmetic operations (addition, multiplication, subtraction, and division). The main calculator service had to call the sub-services to get the results. This project was particularly interesting as it introduced me to both cloud infrastructure and microservices architecture.

#### Context
- **Field of Responsibilities**: Implementing a cloud infrastructure using OpenStack.
- **Objectives**: Create a calculator service with public access and four VMs on a private network for arithmetic operations.
- **Resources and Constraints**: Limited documentation on the OpenStack Python client, time constraints, and the need to ensure secure and efficient communication between services.
- **Duration and Dates**: The project spanned over two weeks during the lab sessions.

### C.I.2 Resolution of Problem

#### What
The solution involved setting up an OpenStack environment with one public-facing VM for the calculator service and four private VMs for the arithmetic operations. Each VM was configured to handle specific arithmetic tasks and communicate with the main calculator service.

#### How
1. **Setup OpenStack Environment**: Installed and configured OpenStack on the host machine.
2. **Create VMs**: Created one public VM and four private VMs using the OpenStack dashboard.
3. **Configure Networking**: Set up networking to allow the public VM to communicate with the private VMs.
4. **Deploy Services**: Deployed the calculator service on the public VM and the arithmetic services on the private VMs.

#### Why
The chosen solution provided a scalable and efficient way to manage the calculator service and its sub-services. Using OpenStack allowed me to leverage cloud infrastructure capabilities, and the microservices architecture ensured modularity and ease of maintenance.

### C.I.3 The Knowledge and Skills Mobilized

To solve this problem, I had to mobilize and develop several new skills:
- **Cloud Infrastructure**: Gained hands-on experience with OpenStack, understanding its components and functionalities.
- **Networking**: Learned how to configure networking in a cloud environment to enable secure communication between VMs.
- **Microservices Architecture**: Understood the principles of microservices and how to implement them in a cloud environment.
- **REST APIs**: Developed skills in creating and consuming REST APIs for inter-service communication.

These skills were acquired through a combination of reading documentation, attending lectures, and collaborating with peers during lab sessions.

### C.I.4 Summary and Review

This experience taught me valuable lessons in cloud infrastructure and microservices architecture. I learned the importance of thorough documentation and the challenges of working with open-source software. With hindsight, I realize that additional training in Kubernetes would have been beneficial, as it is a critical technology for container orchestration in cloud environments.

Overall, the project was a great learning experience that provided practical insights into cloud computing and the implementation of microservices.


## PART D: ANALYTICAL PART

### D.I. Analysis of Skills

I have presented the significant experiences related to the training. I also presented several problem situations where I explained the acquired knowledge and the skills mobilized to solve these problems. In this last part, it is for me to make an exhaustive analysis of all the knowledge and skills acquired during these different experiences.

In the table below, for each activity, I specify my level of execution corresponding to the appropriate figure using the following criteria:

- **AP** - level of application: follow-up of instructions or procedures
- **AN** - level of analysis: improvement or optimization of solutions or proposals
- **M** - level of proficiency: program design or specification definitions
- **EX** - level of expertise: definition of orientations or strategies

| Activities | Acquired experience in terms of | Modes | Level (AP to EX) |
|------------|---------------------------------|-------|------------------|
| Understanding Cloud Computing concepts and architectures | Theoretical, technological knowledge | AN | M |
| Using IaaS services and deploying platforms with OpenStack | Operational know-how | AP | M |
| Designing autonomic microservices systems for efficient resource allocation | Theoretical, technological knowledge | AN | M |
| Comprehending the interplay between Cloud and Edge solutions in IoT ecosystems | Theoretical, technological knowledge | AN | M |

### D.II. Self Evaluation

- **Summary of Skills**: The course provided a solid foundation in cloud computing principles, including the design and deployment of cloud infrastructures. Practical labs with OpenStack allowed me to gain hands-on experience in creating and managing virtual machines, as well as understanding microservices architecture. The final lab on edge computing highlighted the importance of reducing latency and enhancing real-time services, particularly in 5G networks.
- **Skills to Improve**: While the course was comprehensive, it lacked sufficient training in Kubernetes, a critical technology for container orchestration. Enhanced exposure to Kubernetes would bridge this gap and better prepare me for real-world cloud environments.

### D.III. Balance Sheet

The Cloud and Edge Computing course has been instrumental in my professional growth, offering both theoretical knowledge and practical tools relevant to modern cloud engineering. Working with OpenStack provided valuable insight into open-source technologies, aligning with engineering values of collaboration and innovation.

#### Highlights

- **Microservices and Edge Computing**: The emphasis on microservices and edge computing highlighted their transformative role in IoT and real-time applications.
- **Virtualization Techniques**: The introduction to virtualization techniques and their applications in cloud infrastructures was particularly valuable.

### D.IV. Complementary Elements

- **Additional Elements**: The course was a great introduction to virtualization and cloud computing, providing hands-on experience with open-source technologies. However, to fully prepare students for the industry, it is essential to include comprehensive training on Kubernetes. Additionally, more emphasis on practical applications in the field of IoT would enhance the relevance of the course content.

## Project Report

<div style="display: flex; justify-content: center;">
    <embed src="/img/BE_Cloud_Computing/Boukouiss_Chanfreau_Cloud_Computing_Rapport.pdf" width="100%" height="800px" type="application/pdf">
</div>

<p style="text-align: center;">
    <a href="/img/BE_Cloud_Computing/Boukouiss_Chanfreau_Cloud_Computing_Rapport.pdf" target="_blank">Download Complete Report</a>
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
</style>

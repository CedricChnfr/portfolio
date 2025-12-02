---
layout: default
title:  "Cloud Edge Computing"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---



[← Back to My Courses 2024-2025](./my-courses-2024-2025.html)

**🔗 Cours connexes**: 
- [Emerging Network Technologies - S9](./2024-10-03-emerging-network.html) - SDN et architectures réseau
- [Middleware for IoT - S9](./2024-10-03-middleware-iot.html) - Protocoles IoT
- [Embedded IA for IoT - S9](./2024-10-03-embedded-ia-iot.html) - IA sur Edge

---

# Cloud Edge Computing

## PART A: GENERALITIES

### Presentation
The Cloud Edge Computing course shows centralized cloud systems and decentralized edge solutions, preparing me to address modern technological challenges. Taught by Sami Yangui, the course delves into virtualization technologies, cloud services, and edge infrastructures. It emphasizes the design, deployment, and management of architectures that blend the low-latency benefits of edge computing with the scalability of cloud environments.

This training is particularly relevant in today’s context, where the rise of IoT, real-time applications and networks necessitates expertise in these fields. In this course, I gained hands-on experience with tools such as Kubernetes, Docker, and VirtualBox, enabling me to create efficient systems.

## PART B: DESCRIPTIVE PART

### Experience Details

#### Environment and Context

During the Cloud and Edge Computing course, I explored both theoretical and practical aspects of hybrid architectures for modern computing environments. This course provided hands-on experience with virtualization techniques, cloud services, and edge computing solutions. The increasing demand for scalable, efficient, and low-latency services highlights the relevance of this subject in fields such as IoT, real-time systems, and 5G networks.

#### My Function

In this course, I was responsible for:
- Learning and practicing virtualization techniques such as VMs and containers.
- Designing, deploying, and managing hybrid architectures that combine cloud and edge computing.
- Gaining skill with tools like Kubernetes, Docker and VirtualBox.

## PART C: TECHNICAL PART


This section explores the technical aspects of the Cloud Edge Computing course,  mainly learnt during technical labs.

### Technical Concepts Learned

#### 1. Type 1 and Type 2 Hypervisors
One of the first concept I learned is the difference between Type 1 (bare metal) and Type 2 (hosted) hypervisors. Type 1 hypervisors run directly on the host hardware, offering better performance and increased security, while Type 2 hypervisors run as a software layer on an existing operating system, making them easier to use in desktop or development environments.

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Cloud_Computing/H_type1.png" style="width: 40%; margin-right: 10px;"/>
    <img src="/img/BE_Cloud_Computing/H_type2.png" style="width: 40%;"/>
</div>
<br>

#### 2. Virtualization with Docker
Through practical work, I learned to use Docker to create, deploy, and manage containers. Docker allows for the virtualization of applications in isolated environments, making their deployment and management easier. I discovered the advantages of containers over virtual machines, particularly in terms of virtualization cost, CPU and memory resource usage, and flexibility.
<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Cloud_Computing/Docker.png" style="width: 30%;"/>
</div>
<br>

#### 3. OpenStack for Cloud Management
In addition to Docker, I gained experience with OpenStack, an open-source platform for cloud computing. OpenStack allows for the management of large pools of compute, storage, and networking resources, all managed through a dashboard or via the OpenStack API. I learned to deploy and configure OpenStack services, create and manage virtual machines, and set up networking and storage solutions within an OpenStack environment.

<div style="text-align: center;">
    <img src="/img/BE_Cloud_Computing/sch_OpenStack.png" style="width: 40%;"/>
</div>
<br>


#### 4. Network Configuration with VirtualBox
The practical work also allowed me to configure networks using VirtualBox. I learned to create and configure virtual machines, test their connectivity, and set up port forwarding rules to enable communication between virtual machines and the host. I also configured private networks and routers to allow communication between different virtual machines.
<div style="text-align: center;">
    <img src="/img/BE_Cloud_Computing/VirtualBox.png" style="width: 40%;"/>
</div>
<br>

#### 5. Container Orchestration with Kubernetes
Finally I learned to use Kubernetes to orchestrate Docker containers. Kubernetes manages clusters of containers, automating their deployment, scaling, and management, which is essential for cloud-native applications. I configured a Kubernetes cluster and deployed services using YAML configuration files.
<br>


## PART D: ANALYTICAL PART

### Knowledge and Skills Mobilized
- Understanding virtualization technologies and their role in modern cloud infrastructures.
- Designing and managing hybrid architectures that combine cloud and edge computing.
- Gaining hands-on experience with tools like Kubernetes, Docker, AWS, and Azure.
- Addressing advanced topics such as energy-efficient protocols, security challenges, and real-time data analysis at the edge.

### Self Evaluation
I developed new skills in hybrid architectures and their applications in modern computing environments. I was able to comprehend and utilize all the concepts learned. However, I realized that I need to practice using all these tools in the future to avoid forgetting them, as I currently do not have the opportunity to work with them in my apprenticeship company.
As the session on Kubernetes was done quickly with my binom, we had to pass quickly and just launch commands. Thanks to the report we did, it was simpler to understand but in a second time.

### My Opinion
It was interesting, I had the chance to learn a lot of concepts I heard about in everyday life for some jobs. This course will be really useful for my professional path where these concepts could be applied.

The course content was well-structured, starting from the basics of virtualization and gradually moving towards more complex topics. This progression helped me for a better understanding and then expand my knowledge to more advanced concepts.

I now feel more confident in designing, deploying, and managing scalable cloud-edge solutions.

<div style="text-align: center;">
    <h1>Project Report</h1>
</div>

<div style="display: flex; justify-content: center;">
    <embed src="/img/BE_Cloud_Computing/Boukouiss_Chanfreau_Cloud_Computing_Rapport.pdf" width="100%" height="800px" type="application/pdf">
</div>

<p style="text-align: center;">
    <a href="/img/BE_Cloud_Computing/Boukouiss_Chanfreau_Cloud_Computing_Rapport.pdf">Open the full report</a>
</p>
<p style="text-align: center;">
    <a href="/img/BE_Cloud_Computing/Lab_Subject_cloud.pdf">Open Lab Subject</a>
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
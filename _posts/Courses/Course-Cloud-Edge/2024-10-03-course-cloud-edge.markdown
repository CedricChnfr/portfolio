---
layout: default
title:  "Cloud Edge Course"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

# Cloud and Edge Computing

## 1. Introduction
This course explores the fundamental concepts of cloud computing and edge computing. The goal is to illustrate how virtualization and distributed computing models provide large-scale services tailored to specific needs such as low latency, flexibility, and efficient resource management.

## 2. Relevant and Related Concepts
- **Distributed Computing**: A model where multiple remote components interact and coordinate their actions to achieve a common goal.
- **Pervasive Computing**: Allows computations to be performed on any device, anywhere, and at any time.
- **Utility Computing**: An economic model where computing resources are available on demand, with sophisticated billing systems based on consumption.
- **Service-Oriented Computing (SOC)**: A paradigm that uses services as fundamental elements for application development.

## 3. Virtualization
Virtualization allows multiple operating systems to run on a single physical system, ensuring resource isolation.

<div style="text-align: center;">
    <img src="/img/BE_Cloud_Computing/No_Virt.png" style="width: 40%;"/>
    <img src="/img/BE_Cloud_Computing/Virt.png" style="width: 40%;"/>
</div>


- **Hypervisor**:

A hardware virtualization technique that allows multiple OS to run on a single host system at the same time. A hypervisor enables the guest OS to share the hardware of the host, such that each OS appears to have its own processor, memory, and other hardware resources. A hypervisor is also a software (a.k.a Virtual Machine Manager) that allows creating, managing, and/or terminating Virtual Machines (VM).

- **Type 1**: Run directly on physical hardware (bare-metal) for optimized performance.
<div style="text-align: center;">
    <img src="/img/BE_Cloud_Computing/H_Type1.png" style="width: 50%;"/>
</div>
- **Type 2**: Run at the operating system level, easier to manage but with a slight performance drop.
<div style="text-align: center;">
    <img src="/img/BE_Cloud_Computing/H_Type2.png" style="width: 50%;"/>
</div>

- **Paravirtualization**: The guest OS interacts with the hardware via an API provided by the hypervisor.

<div style="text-align: center;">
    <img src="/img/BE_Cloud_Computing/Paravirtualization.png" style="width: 50%;"/>
</div>

- **Containers**: An OS-level virtualization method allowing isolated processes to run under a single kernel instance, promoting lightness and efficiency.

<div style="text-align: center;">
    <img src="/img/BE_Cloud_Computing/Containers.png" style="width: 50%;"/>
</div>

## 4. Cloud Computing
Cloud computing is a model offering on-demand access to a shared pool of configurable resources without the need for initial commitment. It is characterized by:
- **Characteristics**: 
<div style="text-align: center;">
    <img src="/img/BE_Cloud_Computing/Characteristics.png" style="width: 50%;"/>
</div>

### Service Models
- **IaaS (Infrastructure as a Service)**: Provides basic infrastructure (e.g., AWS EC2).
- **PaaS (Platform as a Service)**: Provides a development platform (e.g., Google App Engine).
- **SaaS (Software as a Service)**: Applications accessible via the internet (e.g., Google Workspace).

<div style="text-align: center;">
    <img src="/img/BE_Cloud_Computing/SDM.png" style="width: 70%;"/>
</div>

### Deployment Models
- **Public Cloud**: Infrastructure owned by a cloud provider, accessible to the general public.
- **Private Cloud**: Infrastructure dedicated to a specific organization.
- **Hybrid Cloud**: Combines multiple clouds (public and private) for increased flexibility.

## 5. Edge Computing and Fog Computing
Edge Computing brings cloud resources closer to end users and data sources, enabling faster processing and real-time control, especially for latency-sensitive IoT applications.

### Characteristics and Advantages
- **Scalability**: Adapts to an increasing number of distributed resources.
- **Autonomy**: Reduces the volume of data transmitted, allowing local processing.
- **Data Sovereignty**: Keeps data close to its source, securing it before transmission.

### Challenges and Research Directions
- **Quality of Service (QoS) Management**: Requires consideration of latency and availability constraints.
- **Security**: Needs rigorous device management to protect against cyberattacks.

## 6. OpenStack: Open Source Cloud Platform
OpenStack is an open-source solution for managing private and public clouds, offering capabilities for provisioning virtual machines, network management, and storage.

### Key Components
- **Nova**: Manages compute resources.
- **Swift**: Provides object storage.
- **Glance**: Catalogs and manages server images.
- **Quantum (or Neutron)**: Provides network as a service.

## 7. Autonomic Computing
Inspired by the human autonomic nervous system, autonomic computing aims to reduce the complexity of managing distributed systems through MAPE (Monitor, Analyze, Plan, Execute) feedback loops.

<div style="text-align: center;">
    <img src="/img/BE_Cloud_Computing/Automatic.png" style="width: 70%;"/>
</div>
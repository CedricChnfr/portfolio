---
layout: default
title:  "Cloud Edge Project"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---
## 1. Introduction to the project
This project aimed to familiarize oneself with Cloud hypervisors and virtualization, by implementing different techniques such as virtual machine (VM) and Docker container management. The work included exploring type 1 and type 2 virtualization, as well as network configuration and setting up Docker containers to illustrate the differences between VMs and containers in terms of performance, isolation, and resource management.

## 2. Virtualization: Type 1 and Type 2 Hypervisors
The first part of the project concerned hypervisors:

- Type 1: Also called "bare-metal" hypervisors, they run directly on the physical hardware without an intermediate operating system. They offer better isolation and performance because they have direct access to hardware resources.

- Type 2: These hypervisors run on top of a host operating system. They are easier to manage but are less performant because they have to negotiate resources with the operating system.

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Cloud_Computing/Hyperviseur1.png" alt="Schéma du Projet Robot" style="width: 50%;"/>
    <img src="/img/BE_Cloud_Computing/Hyperviseur2.png" alt="Schéma du Projet Robot" style="width: 50%;"/>
</div>

## 3. Virtual Machines vs. Containers
The next step was to compare virtual machines (VMs) with containers (CTs):

- Virtual Machine: Virtual machines (VMs) or guests are instances of an operating system that are co-located on a physical machine using a hypervisor. Each VM has its own operating system, memory, and other resources, which are isolated from other VMs on the same physical computer. This allows multiple operating systems to run on the same physical components without interfering with each other.
Each VM runs its own operating system, including a kernel. They are isolated from other VMs and the host operating system.


<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Cloud_Computing/VM.png" alt="Schéma du Projet Robot" style="width: 30%;"/>
</div>

- Containers: Containers are lightweight, portable, self-contained executable images that contain software applications and their dependencies. They enable applications to be deployed and run consistently across different environments.
They share the same host kernel but are isolated at the process and file level. They encapsulate applications with their dependencies.

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Cloud_Computing/Cont.png" alt="Schéma du Projet Robot" style="width: 30%;"/>
</div>

## 4. Network configurations: NAT and Bridge mode
Two network connection modes were used for VMs and containers:

- NAT mode: This mode allows VMs/CTs to access the Internet via a private IP address, but they cannot be reached from the outside without additional configuration (port forwarding).

- Bridge mode: In this mode, VMs/CTs have an IP address visible on the local network, allowing them to interact directly with other machines on the network.

## 5. Practical implementation: VirtualBox and Docker
In the practical part of the project, the following steps were performed:

VM creation in VirtualBox: Configuration and connectivity test in NAT mode to allow bidirectional communication with the Internet and other machines.
Docker installation: Docker was installed on the VM to provision containers. Connectivity tests showed that containers could communicate with each other, with VMs and with the outside world.
## 6. Docker: Container provisioning and management
The provisioning of Docker containers was carried out in several steps:

Downloading the Ubuntu image and running a container instance.
Testing the connectivity between containers and VMs, with conclusive results in terms of bidirectional communication.
Cloning and snapshot: Snapshots of the containers were taken to preserve their state, thus facilitating recovery and subsequent deployment.
## 7. Conclusion
This project allowed us to understand the fundamental differences between type 1 and 2 hypervisors, as well as Docker VMs and containers. In addition, NAT and Bridge network configurations were explored to ensure connectivity between different virtual machines and containers. Docker implementation demonstrated the effectiveness of containers for rapid deployments and resource management, while VMs provide stronger isolation for use cases requiring better security.
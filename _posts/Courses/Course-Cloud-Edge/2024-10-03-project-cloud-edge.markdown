---
layout: default
title:  "Cloud Edge Project"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---
# **Lab 1: Introduction to Cloud Hypervisors**

# Theoretical Part

## 1. Introduction to the project
This project aimed to familiarize oneself with Cloud hypervisors and virtualization, by implementing different techniques such as virtual machine (VM) and Docker container management. The work included exploring type 1 and type 2 virtualization, as well as network configuration and setting up Docker containers to illustrate the differences between VMs and containers in terms of performance, isolation, and resource management.

## 2. Virtualization: Type 1 and Type 2 Hypervisors
The first part of the project concerned hypervisors:

- Type 1: Also called "bare-metal" hypervisors, they run directly on the physical hardware without an intermediate operating system. They offer better isolation and performance because they have direct access to hardware resources.

- Type 2: These hypervisors run on top of a host operating system. They are easier to manage but are less performant because they have to negotiate resources with the operating system.

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Cloud_Computing/Hyperviseur1.png" style="width: 50%;"/>
    <img src="/img/BE_Cloud_Computing/Hyperviseur2.png" style="width: 50%;"/>
</div>


|         | Architecture | Performance | Use cases |
|--------------|-------------|-----------|
| **Type 1 (OpenStack)** | It operates directly on the physical host machine's bare-metal hardware without the need for an underlying OS. | It usually provides better performance by directly accessing hardware resources, eliminating the overhead of an operating system layer. | It is commonly used in enterprise data centers and cloud environments where performance, scalability, and resource isolation are critical. |
| **Type 2 (VirtualBox)** | It runs on top of an existing OS and operates as applications or processes within that traditional OS. | It generally has more overhead than Type 1 hypervisors because it depends on the host OS to manage hardware resources. | It is commonly used in desktop or developer environments where performance is less critical. |

## 3. Virtual Machines vs. Containers
The next step was to compare virtual machines (VMs) with containers (CTs):

- Virtual Machine: Virtual machines (VMs) or guests are instances of an operating system that are co-located on a physical machine using a hypervisor. Each VM has its own operating system, memory, and other resources, which are isolated from other VMs on the same physical computer. This allows multiple operating systems to run on the same physical components without interfering with each other.
Each VM runs its own operating system, including a kernel. They are isolated from other VMs and the host operating system.


<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Cloud_Computing/VM.png" style="width: 30%;"/>
</div>

- Containers: Containers are lightweight, portable, self-contained executable images that contain software applications and their dependencies. They enable applications to be deployed and run consistently across different environments.
They share the same host kernel but are isolated at the process and file level. They encapsulate applications with their dependencies.

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Cloud_Computing/Cont.png" style="width: 30%;"/>
</div>

## 3.1 Comparison from Different Perspectives

We will compare VMs and containers from two perspectives: application developers and infrastructure administrators.

### From an Application Developer’s Perspective:

| Criteria | Virtual Machine | Container |
|----------|-----------------|-----------|
| **Virtualization Cost** | Requires more memory and is more expensive due to the full OS emulation. | Requires less memory and is cheaper as it doesn't duplicate the OS. |
| **CPU, Memory, and Network Usage** | Higher CPU overhead due to hardware emulation and multiple OS instances. | Lower CPU overhead as they run as lightweight processes. |
| **Application Security** | More secure with strong isolation (each VM has its own OS). | Less secure as containers share the same kernel and libraries. |
| **Performance (Response Time)** | Higher response time due to environment regeneration for each operation. | Lower response time, starts up in milliseconds. |
| **Continuous Integration Tooling** | Limited development tools. | Comes with development kits. |
| **Flexibility and Dynamicity** | Harder to modify resources and transfer programs. | Easy to adjust resources and deploy applications. |

### From an Infrastructure Administrator’s Perspective:

| Criteria | Virtual Machine | Container |
|----------|-----------------|-----------|
| **Developer Point of View** | Useful for full machine emulation and network control but costly and resource-intensive. | Offers portability, flexibility, and quick startup, ideal for testing and deployment. |
| **System Administrator Point of View** | Valued for complete isolation and unique OS tools, despite being resource-intensive. | Challenging due to security risks, limited hardware control, and restricted network configurations. |

## 4. Similarities and Differences Between Existing Container Technologies

Different container technologies are available in the market, such as LXC/LXD, Docker, Rocket, OpenVZ, runC, and systemd-nspawn. Their respective positioning is not always obvious, but comparative analyses are available online. Here, we define the criteria used to compare these container technologies (CT):

- **Application Isolation and Resources (Multi-tenancy):** Refers to the architecture of the server hosting containers, where a single instance of the host OS supports multiple tenants (containers).
- **Containerization Level (e.g., Operating System, Application):** Containerization packages software and its dependencies, enabling it to run anywhere.
- **Tooling (e.g., API, Continuous Integration, Service Composition):** Refers to the tools offered with the container service, such as development kits, migration tools, and custom settings.

| Technology | Application Isolation | Containerization Level | Tooling |
|------------|-----------------------|------------------------|---------|
| **LXC** | Light Isolation: Although containers share the core, they remain isolated from each other, ensuring adequate security and stability. | OS level containers, allowing kernel sharing with the host. | LXC offers a CLI for container management and supports APIs. |
| **Docker** | Enhanced Container Isolation provides an additional layer of security to prevent malicious workloads running in containers from compromising Docker Desktop or the host. | Operating system level containers, allowing kernel sharing with the host. | Docker is well-known for its user-friendly CLI and API. It has strong CI/CD support with Docker Compose and Kubernetes integration. Docker Compose is useful for service composition. |
| **Rocket (RKT)** | RKT provides application isolation using proven mechanisms such as Control Groups (Cgroups) and SELinux, ensuring that containers run in protected environments and limit their access to system resources. | Application-level containers, with a layered architecture allowing for flexibility. | It features a CLI for pod-based deployments and integrates seamlessly with systemd for service management. |
| **OpenVZ** | Good isolation even if containers share the kernel. | Application level | It offers a variety of management tools. |
| **runC** | runC is a CLI tool for spawning and running containers on Linux according to the OCI specification. | Application-level containers, integrated in larger systems. | It operates with a command-line interface and adheres to OCI specifications for managing container lifecycles. |

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Cloud_Computing/CT_types.png" style="width: 90%;"/>
</div>

## 5. Network configurations: NAT and Bridge mode
Two network connection modes were used for VMs and containers:

- NAT mode: This mode allows VMs/CTs to access the Internet via a private IP address, but they cannot be reached from the outside without additional configuration (port forwarding).

- Bridge mode: In this mode, VMs/CTs have an IP address visible on the local network, allowing them to interact directly with other machines on the network.

# Pratical Part

## Practical Implementation: VirtualBox and Docker

### 1. Setting Up VirtualBox VM in NAT Mode

#### Creating and Configuring a VM
1. Open VirtualBox.
2. Unzip the provided archive.
3. Create and configure a new VM.
4. Launch the VM.

### 2. Testing VM Connectivity

#### a) VM Connection
Once logged in, use the `ifconfig` command in the VM terminal to identify the assigned IP addresses:

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Cloud_Computing/ifconfig.png" style="width: 70%;"/>
</div>

- NAT Address: `172.17.0.1`
- Virtual Machine Address: `10.0.2.15`
- Loopback Address: `127.0.0.1`

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Cloud_Computing/ifconfig_host.png" style="width: 70%;"/>
</div>

- Host Machine (VirtualBox Host-Only Network): `192.168.56.1`
- Host Ethernet Interface: `10.1.5.89`

#### b) Connectivity Verification
Test the connectivity between each component:
- VM ↔ Host Machine: Ping successful.

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Cloud_Computing/ping.png" style="width: 70%;"/>
</div>

- Host Machine ↔ NAT / VM: Ping failed.

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Cloud_Computing/ping2.png" style="width: 70%;"/>
</div>

To resolve the ping failure from the host machine to the VM, configure a port forwarding rule in VirtualBox to redirect requests from the host to a specific port inside the VM.

### 3. Setting Up Missing Connectivity

To enable communication between the host machine and the VM in NAT mode:
<br>
1- Configure port forwarding in VirtualBox to forward data arriving on the host machine at port `1234` to VM port `22`.
<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Cloud_Computing/port.png" style="width: 70%;"/>
</div>

2- Install `openssh` on the VM.
<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Cloud_Computing/ssh.png" style="width: 70%;"/>
</div>

3- Use PuTTY to test the connection.
<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Cloud_Computing/ping3.png" style="width: 70%;"/>
</div>

### 4. VM Duplication

To create a new clone with the same disk file, use the following command:

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Cloud_Computing/duplication.png" style="width: 100%;"/>
</div>

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Cloud_Computing/duplication2.png" style="width: 100%;"/>
</div>

### 5. Docker Containers Setup

1. Update the existing list of packages:

    <div style="display: flex; justify-content: center;">
        <img src="/img/BE_Cloud_Computing/update.png" style="width: 70%;"/>
    </div>

2. Install prerequisite packages: 

    <div style="display: flex; justify-content: center;">
        <img src="/img/BE_Cloud_Computing/install.png" style="width: 70%;"/>
    </div>

3. Add the GPG key for the official Docker repository + Docker repository to APT source:

    <div style="display: flex; justify-content: center;">
        <img src="/img/BE_Cloud_Computing/dw_docker.png" style="width: 70%;"/>
    </div>


4. Update the package list again:

    <div style="display: flex; justify-content: center;">
        <img src="/img/BE_Cloud_Computing/update2.png" style="width: 70%;"/>
    </div>

5. Install Docker + Check it is running:

    <div style="display: flex; justify-content: center;">
        <img src="/img/BE_Cloud_Computing/inst_docker.png" style="width: 70%;"/>
    </div>

### 6. Docker Containers Provisioning

We can now provision Docker nodes.

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Cloud_Computing/nodes.png" style="width: 70%;">
</div>

1. Pull an Ubuntu image:

    <div style="display: flex; justify-content: center;">
        <img src="/img/BE_Cloud_Computing/pull.png" style="width: 70%;">
    </div>
    
2. Execute an Ubuntu instance (CT1):

    <div style="display: flex; justify-content: center;">
        <img src="/img/BE_Cloud_Computing/instance.png" style="width: 70%;">
    </div>

3. Install required connectivity testing tools:

    <div style="display: flex; justify-content: center;">
        <img src="/img/BE_Cloud_Computing/connect.png" style="width: 70%;">
    </div>
4. Check the connectivity:
    - Use `ifconfig` to get the IP address (`172.17.0.2`).
    <div style="display: flex; justify-content: center;">
        <img src="/img/BE_Cloud_Computing/instance.png" style="width: 70%;">
    </div>
    - Ping an internet resource from Docker: Success.
    <div style="display: flex; justify-content: center;">
        <img src="/img/BE_Cloud_Computing/ping_g.png" style="width: 70%;">
    </div>
    - Ping the VM from Docker: Success.
    <div style="display: flex; justify-content: center;">
        <img src="/img/BE_Cloud_Computing/ping_vm.png" style="width: 70%;">
    </div>
    - Ping Docker from the VM: Success.
    <div style="display: flex; justify-content: center;">
        <img src="/img/BE_Cloud_Computing/ping_dc.png" style="width: 70%;">
    </div>

5. Execute a new instance (CT2) of the Ubuntu Docker:
    <div style="display: flex; justify-content: center;">
        <img src="/img/BE_Cloud_Computing/inst2.png" style="width: 70%;">
    </div>
6. Snapshot of CT2:
    <div style="display: flex; justify-content: center;">
        <img src="/img/BE_Cloud_Computing/snapshot.png" style="width: 70%;">
    </div>
7. Stop and terminate CT2:
    <div style="display: flex; justify-content: center;">
        <img src="/img/BE_Cloud_Computing/stop.png" style="width: 70%;">
    </div>
8. List available Docker images:
    <div style="display: flex; justify-content: center;">
        <img src="/img/BE_Cloud_Computing/image.png" style="width: 70%;">
    </div>
9. Execute a new instance (CT3) from the previous snapshot:
    <div style="display: flex; justify-content: center;">
        <img src="/img/BE_Cloud_Computing/inst3.png" style="width: 70%;">
    </div>
10. Create a Dockerfile for a custom image:
    <div style="display: flex; justify-content: center;">
        <img src="/img/BE_Cloud_Computing/ubuntu.png" style="width: 30%;">
    </div>
    <div style="display: flex; justify-content: center;">
        <img src="/img/BE_Cloud_Computing/build.png" style="width: 70%;">
    </div>
    <div style="display: flex; justify-content: center;">
        <img src="/img/BE_Cloud_Computing/image2.png" style="width: 70%;">
    </div>

    
## OpenStack

### 1. CT creation and configuration OpenStack

### First Part: CT creation and configuration OpenStack

- OpenStack Connection/Authentification

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Cloud_Computing/openstack.png" style="width: 70%;">
</div>

- Creation of a VM / private network and gateway

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Cloud_Computing/VM_create.png" style="width: 70%;">
</div>

A VM cannot be created from a public network for different reasons, so we created a private network:

- **Network Separation:** The private network allows isolating VMs from other networks. This means that VMs can communicate with each other without being directly exposed to external threats or unauthorized traffic from the Internet.
- **Traffic Control:** We can better manage incoming and outgoing traffic. The router plays an important role because it controls the flow between the private and public networks.

To allow ICMP traffic (ping) and SSH, we added three new security rules:

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Cloud_Computing/traffic.png" style="width: 90%;">
</div>

### Second Part: Connectivity Test
First, we associated a floating IP for the VM to access the VM from the outside via SSH.

- **IP Address from VM:** The IP address displayed on the dashboard:
    - `192.168.37.28`: Public address useful to access the VM from outside.
    - `12.7.5.176`: Private address to communicate with another machine on the private network.

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Cloud_Computing/floating.png" style="width: 70%;">
</div>

Here, the router is important because it allows us to link the private network where the VM is connected and the public network.

### Connectivity Test:
- **Ping Google from the VM:** Indicates that the network configuration is properly set up, allowing the VM to communicate with external tools.

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Cloud_Computing/ping_google.png" style="width: 70%;">
</div>

- **Pinging the VM from the Desktop:** Verifies that incoming connections to the VM are working as intended. This indicates that the VM's firewall and security group settings are appropriately configured to allow traffic from the desktop.

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Cloud_Computing/ping_vm2.png" style="width: 70%;">
</div>

- **Ping the Desktop from the VM:** Confirms that the internal network configuration is functioning correctly. This ensures that the VM can communicate with other devices on the same network.

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Cloud_Computing/ping_desk.png" style="width: 70%;">
</div>

### Third Part: Snapshot, Restore, and Resize a VM
- **Resize a Running and a Shutdown VM:** Resizing was not possible, and an error occurred due to access rights.
    - The limitation highlighted that to resize a VM, some administrative rights are necessary. A solution could be to give user roles allowing some operations of resource management. This will allow more users to benefit from the flexibility of virtualization without compromising security.
<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Cloud_Computing/danger.png" style="width: 60%;">
</div>

- **Creating a Snapshot of the VM:** We captured the current state of the system, including all files, configurations, and software installed at that time.
    - If changes are made to the VM after the snapshot is created, those changes will not be present in the snapshot, which could be useful for reverting to a previous state in case of a problem.
   - **Restoring the VM from the Latest Snapshot:** We were able to find the exact state of the machine at the time the snapshot was created and also select a new size for the VM. This allowed us to quickly recover a working system after unwanted changes or crashes.

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_Cloud_Computing/snapshot2.png" style="width: 80%;">
</div>

<!-- ## Full PDF Report

<div style="display: flex; justify-content: center;">
    <embed src="/img/BE_Cloud_Computing/Boukouiss_Chanfreau_Cloud_Computing_Rapport.pdf" width="100%" height="800px" type="application/pdf">
</div> -->

## Conclusion
This project allowed us to understand the fundamental differences between type 1 and 2 hypervisors, as well as Docker VMs and containers. In addition, NAT and Bridge network configurations were explored to ensure connectivity between different virtual machines and containers. Docker implementation demonstrated the effectiveness of containers for rapid deployments and resource management, while VMs provide stronger isolation for use cases requiring better security.
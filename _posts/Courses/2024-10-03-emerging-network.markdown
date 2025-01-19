---
layout: default
title:  "Emerging Network Technologies"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

# Emerging Network

## PART A: GENERALITIES

### Presentation
The "Emerging Network" course taught by S. Abdellatif was an exploration into the latest advancements in network technologies. The course covered topics such as Software-Defined Networking (SDN), OpenFlow, and Ryu. It was interesting to see how these emerging technologies are shaping the future of networking.

## PART B: DESCRIPTIVE PART

### Experience Details

#### Environment and Context
During this course, I delved into both the theoretical and practical aspects of emerging network technologies. The relevance of these technologies in modern networking environments was evident and the hands-on sessions allowed me to apply the concepts learned in class to real-world scenarios.

#### My Function
In this course, I was responsible for:
- Understanding the principles of SDN and OpenFlow.
- Exploring network automation and orchestration tools.
- Conducting experiments to test the efficiency and scalability of emerging network solutions.

## PART C: TECHNICAL PART

This section explores the technical aspects of SDN and OpenFlow, focusing on their applications in network management.

### Technical Concepts Learned
#### 1. SDN and OpenFlow Architecture
I learned about the architecture of Software-Defined Networking (SDN) and the role of OpenFlow in enabling SDN. SDN separates the control plane from the data plane allowing centralized control of the network through a controller. OpenFlow is a protocol that facilitates communication between the controller and the network devices, enabling dynamic management of network traffic.
```bash
# Setting the controller by specifying IP address and port
admin@picOS-OVS$ ovs-vsctl set-controller br0 tcp:192.168.0.42:6633
```

#### 2. Open vSwitch (OVS)
Open vSwitch (OVS) is a multilayer virtual switch designed to enable network automation through programmatic extensions. I learned how to configure OVS, create logical bridges, and attach physical ports. This involved using commands to set up and manage OVS instances ensuring proper connectivity and flow management.
```bash
# Adding a bridge and setting its datapath type
admin@picOS-OVS$ ovs-vsctl add-br br0 -- set bridge br0 datapath_type=pica8
```

#### 3. Manual Installation of OpenFlow Rules
I gained hands-on experience in manually installing OpenFlow rules on switches. This involved adding and deleting flow entries to control the forwarding behavior of network packets. Understanding how to manipulate flow tables allowed me to implement specific network policies and manage traffic efficiently.
```bash
# Adding a flow entry to forward packets from port 10 to ports 13 and 16
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=10,actions=output:13,16
```

#### 4. Controller Attachment and Network Control
I explored the process of attaching an OpenFlow controller (Ryu) to the network and using it to manage network devices. This included setting the controller for OVS bridges and launching the controller in verbose mode to monitor interactions. The controller's role in dynamically updating flow tables based on network events was a key learning point.
```bash
# Launching the Ryu controller in verbose mode
controleur# ryu-manager --verbose
```

#### 5. Reactive and Proactive Network Programming
I learned about reactive and proactive approaches to network programming. Reactive programming involves the controller responding to network events in real-time, while proactive programming involves pre-configuring flow entries to handle expected traffic patterns. Both approaches have their advantages and use cases in network management.
```bash
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=16,ip,nw_dst=128.0.0.4,actions=output:13
```

#### 6. Network Topology and Loop Prevention
In the final exercise, I deployed a mesh topology with multiple switches and explored the challenges of loop prevention in network design. Understanding how to manage loops and ensure efficient routing in complex topologies was crucial for maintaining network stability and performance.
```bash
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=16,tcp,tp_dst=22,actions=output:13
```

## PART D: ANALYTICAL PART

### The Knowledge and Skills Mobilized
- Understanding and mastering the fundamentals of emerging network paradigms applied to IoT.
- Developing applications for traffic management using SDN.
- Understanding LISP and its role in enabling node mobility.
- Integrating SDN and LISP for enhanced network management and mobility.

### Self Evaluation
I found the "Emerging Network" course to be highly engaging and informative, although it was a bit complicated for me as a student specializing in Automatic Electronics compared to those in the Network option. Despite this, I was actively involved in simulating topologies and testing various aspects which provided a practical understanding of how these technologies are transforming network management.

### My Opinion
As I am following the [Master REOC](./master-reoc.html), I had already worked on SDN and Ryu. It was enriching to solidify my skills. Also, the course felt more academic because we had lab sessions that we had to follow step by step to understand the concepts. In REOC, we had to work on a project with our own research which provided a more hands-on and exploratory experience.

<div style="text-align: center;">
    <h1>Project Report</h1>
</div>


<div style="display: flex; justify-content: center;">
    <iframe src="/img/BE_Emerging_Network/README.md" width="100%" height="800px" style="border:none;"></iframe>
</div>

<p style="text-align: center;">
    <a href="/img/BE_Emerging_Network/README.md">Open the README file</a>
</p>

<p style="text-align: center;">
    <a href="/img/BE_Emerging_Network/Lab_Subject_emerging.pdf">Open the Lab Subject</a>
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
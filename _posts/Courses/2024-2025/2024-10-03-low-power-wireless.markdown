---
layout: default
title:  "Low Power Wireless Personal Area Network (LP-WPAN)"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---



[← Back to My Courses 2024-2025](./my-courses-2024-2025.html)

# Low Power Wireless Personal Area Network

## PART A: GENERALITIES

### Presentation
The "Low Power Wireless Networks" course provided an in-depth look into the principles and applications of low power wireless personal area networks (LP-WPAN). The course covered various protocols and technologies used in LP-WPAN, focusing on their efficiency and scalability in IoT contexts.


## PART B: DESCRIPTIVE PART

### Experience Details

#### Environment and Context
Given the short duration of the course, we focused on a few key technical concepts. The initial part of the course covered basic network and telecommunication concepts, such as scrambled networks and interference. We then delved into the specifics of a TCP/IP protocol stack for LP-WPAN, using the 802.15.4 norm for the MAC and physical layers. This norm is commonly used in protocols like Zigbee. We also explored the use of IPv6 with an intermediate layer, 6LoWPAN, to reduce packet size.

#### New Concepts Learned
6LoWPAN, a key technology for enabling IPv6 over low power wireless networks, stands for IPv6 over Low-Power Wireless Personal Area Networks. It is designed to allow small devices with limited processing power and memory to communicate over the Internet. 6LoWPAN achieves this by compressing the IPv6 headers, making them suitable for the constrained environments of LP-WPANs.
#### My Function
In this course, I was responsible for:
- Understanding the principles and architecture of 6LoWPAN.
- Exploring various protocols and their applications in low power wireless networks.
- Conducting experiments to test the efficiency and scalability of different LP-WPAN solutions.

## PART C: TECHNICAL PART

This section explores the technical aspects of the TCP/IP protocol stack for LP-WPAN, focusing on the 802.15.4 norm, IPv6, and 6LoWPAN.

### Technical Concepts Learned

#### 1. IPv6 Basics for IoT
I learned about the basics of IPv6, including auto-configuration, router advertisements, multicasting, and routing. These concepts are necessary for understanding how IPv6 can be used in IoT networks to provide efficient and scalable communication.

#### 2. Auto-configuration of Link-local Addresses
We practiced auto-configuring link-local IPv6 addresses on network interfaces. This involved bringing up the network interface and observing the assignment of IPv6 addresses. We also analyzed the Duplicate Address Detection (DAD) procedures using tools like tcpdump and wireshark.

<div style="text-align: center; display: flex; justify-content: center; gap: 20px;">
    <img src="/img/BE_Low_Power/auto_conf.png" style="width: 70%;"/>
</div>
<br>

We executed the command `ifconfig eth0 up` to bring up the network interface `eth0`. Following this, we used `ip -6 addr show dev eth0` to display the IPv6 addresses assigned to the interface. The output showed an address in the format `inet6 fe80::527c:6fff:fe56:e8b0`.

This address is a link-local IPv6 address, which is automatically configured on all IPv6-enabled interfaces. Link-local addresses are used for communication within a single network segment and are not routable beyond that segment. 

The `fe80::/10` prefix indicates that it is a link-local address. The remaining part of the address (`527c:6fff:fe56:e8b0`) is derived from the interface's MAC address using the Modified EUI-64 format.

Understanding link-local addresses is crucial for configuring and troubleshooting IPv6 networks, as they are fundamental for neighbor discovery and other local network operations.

#### 3. Auto-configuration of Unicast Global Addresses
We explored the process of auto-configuring unicast global IPv6 addresses using router advertisements. This involved configuring the router to send advertisements and observing how end-hosts derive their network configuration from these advertisements.

<div style="text-align: center; display: flex; justify-content: center; gap: 20px;">
    <img src="/img/BE_Low_Power/dump.png" style="width:80%;"/>
</div>
<br>

We used tool tcpdump to capture and analyze the ICMPv6 messages exchanged between the router and the end-hosts. These messages indicate the neighbor solicitation and router solicitation processes, for the auto-configuration of unicast global IPv6 addresses.

The neighbor solicitation message is used to discover the link-layer address of a neighbor or to verify that a neighbor is still reachable.

The router solicitation message is sent by an end-host to request a router advertisement from a local router, which contains the necessary information for the end-host to configure its global IPv6 address.

#### 4. End-to-end IPv6 Connectivity and MQTT
We established end-to-end IPv6 connectivity with an application server and set up MQTT for data distribution. This involved configuring the MQTT broker and using tools like mosquitto_sub and mosquitto_pub to distribute data between topic publishers and consumers.

#### 5. 6LoWPAN Header Compression
We practiced some aspects of 6LoWPAN, focusing on its header compression mechanism. This involved analyzing the encapsulation of IPv6 packets in 6LoWPAN frames and identifying the modes used for compressing different fields of the IPv6 header.

<div style="text-align: center; display: flex; justify-content: center; gap: 20px;">
    <img src="/img/BE_Low_Power/header.png" style="width: 70%;"/>
</div>
<br>

We used Wireshark to capture and analyze ICMPv6 packets. By examining the ICMPv6 section, we could see the IP Header Compression (IPHC) header, which provides information about the compressed IPv6 header fields. This analysis helped us understand how 6LoWPAN reduces the overhead of IPv6 headers, making it suitable for low power and lossy networks.

<div style="text-align: center; display: flex; justify-content: center; gap: 20px;">
    <img src="/img/BE_Low_Power/compression.png" style="width: 70%;"/>
</div>
<br>

#### 6. RPL Routing Protocol
We explored the RPL routing protocol, which is designed for low power and lossy networks. This involved configuring a network topology with RPL enabled and analyzing the routing tables and traffic generated by the protocol.

<div style="text-align: center; display: flex; justify-content: center; gap: 20px;">
    <img src="/img/BE_Low_Power/node.png" style="width: 90%;"/>
</div>

- **Multipoint-to-point traffic**: Traffic from multiple nodes converging to a single root node, typically used for data collection in sensor networks.
- **Point-to-multipoint traffic**: Traffic from a single root node disseminating information to multiple nodes, often used for control messages or updates.
- **Point-to-point traffic**: Direct communication between two nodes within the network, used for peer-to-peer data exchange.


## PART D: ANALYTICAL PART

### The Knowledge and Skills Mobilized
- Understanding the fundamentals of LP-WPAN and its TCP/IP protocol stack.
- Analyzing the benefits and drawbacks of using standard protocols based on IP.
- Integrating IPv6 in low power use cases with 6LoWPAN.
- Understanding the 802.15.4 norm and its applications in protocols like Zigbee.

### Self Evaluation
I found the LP-WPAN course to be a valuable introduction to low power wireless networks. I particularly enjoyed working with IPv6 and 6LoWPAN, there is some areas where I still have uncertainties and need to deepen my knowledge but with time and practice, I am confident that I will master these concepts.

Fortunately, the labs were well guided by the teacher, which allowed me to understand better because it was pretty complex at first, but he managed to transmit the course skill effectively.

### My Opinion
It was a new concept I appreciated working on. It provided a fresh perspective on network possibilities and allowed me to explore innovative solutions in low power wireless networks. The practical experiments was interesting as they demonstrated the real-world applications of LP-WPAN technologies.


<div style="text-align: center;">
    <h1>Project Report</h1>
</div>

<div style="display: flex; justify-content: center;">
    <embed src="/img/BE_Low_Power/IPV6_Report.pdf" width="100%" height="800px" type="application/pdf">
</div>

<p style="text-align: center;">
    <a href="/img/BE_Low_Power/IPV6_Report.pdf">Open the full report</a>
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
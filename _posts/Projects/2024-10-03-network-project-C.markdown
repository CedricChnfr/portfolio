---
layout: default
title:  "C and Network Project"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---
# Introduction
This project involves developing a simple network application in C using the socket API to explore the functionalities of UDP and TCP protocols. The goal is to understand how these protocols handle message transmission in a networked environment, with focus on the differences in reliability, message delivery, and connection handling.

In this lab, we explored the fundamental differences between the UDP and TCP protocols using the tsock application in a Linux environment. The objective was to observe how each protocol handles data transmission, reliability, and connection establishment.


## **Part 1: Comparing UDP and TCP**

### UDP Transmission:

- Setup:

    - On Terminal 1 (acting as the server or sink), we started a UDP socket listening on port 9025 with a buffer size of 10 bytes using the command:

        `tsock -p -u -t 10 9025`

        `-p`: Specifies the sink mode.

        `-u`: Uses the UDP protocol.

        `-t` 10: Sets the application buffer size to 10 bytes.

        `9025`: port number created to listen (>9000)

        <div style="text-align: center;">
            <img src="/img/BE_Reseau/UDP_cmd.png" style="width: 90%;"/>
        </div>

    - On Terminal 2 (acting as the client or source), we sent 20 messages to the server using:

        `tsock -s -u -n 20 insa-20661 9025`

        `-s`: Specifies the source mode.
        
        `-n 20`: Number of messages to send.

        `insa-20661`: Destination machine identifier.

        `9025`: port number where we send (>9000)

- Observation:

    - Out of 20 messages sent, only 13 were received.

    - The application buffer on the receiver's side became saturated because it processed messages slower than they arrived.

    <div style="text-align: center;">
            <img src="/img/BE_Reseau/UDP_send.png" style="width: 90%;"/>
    </div>

- Conclusion:
    - UDP is a connectionless protocol without mechanisms for flow control or error correction.

    - Packet loss occurred due to buffer overflow at the application level.

    - UDP does not guarantee message delivery, order, or integrity.


### TCP Transmission:

- Setup:

    - On Terminal 1, we started a TCP socket listening on port 9025 with a buffer size of 20 bytes:

        `tsock -p -t 20 9025`

        - Omitting `-u` defaults to TCP.

        <div style="text-align: center;">
                <img src="/img/BE_Reseau/TCP_cmd.png" style="width: 90%;"/>
        </div>

    - On Terminal 2, we sent 20 messages to the server:

        `tsock -s -n 20 insa-20661 9025`

        <div style="text-align: center;">
                <img src="/img/BE_Reseau/TCP_send.png" style="width: 90%;"/>
        </div>

- Observation:

    - All 20 messages were successfully transmitted and received.

    - No packet loss occurred, and messages arrived in order.

- Conclusion:

    - TCP is a connection-oriented protocol that establishes a connection before data transfer.

    - It provides reliability through acknowledgments, retransmissions, and flow control.

    - TCP ensures data integrity and ordered delivery.

## **Part 2: Testing Protocol Behavior Without Open Ports**

### TCP Connection Refusal:

- Attempting to send messages to a TCP port without a listening socket resulted in a "connection refused" error.

- This confirms that TCP requires an active listener to establish a connection.

<div style="text-align: center;">
    <img src="/img/BE_Reseau/TCP_beh.png" style="width: 90%;"/>
</div>

### UDP Message Handling:

- Sending messages to a closed UDP port did not produce errors on the sender's side.

- The messages were sent into the network, but the receiver did not process them.

- UDP does not check for active listeners before sending data.

<div style="text-align: center;">
    <img src="/img/BE_Reseau/UDP_beh.png" style="width: 90%;"/>
</div>

<br>

## **Part 3: Capturing and Analyzing Network Traffic**

Using `tcpdump` to Monitor Traffic:

- Connected to a monitoring machine using:

`ssh tcpdump@insa-20673`

- Started packet capture on port 9025:

`sudo tcpdump 9025`


### Observations with UDP:

<div style="text-align: center;">
    <img src="/img/BE_Reseau/UDP_dump.png" style="width: 90%;"/>
</div>
<br>
- Messages were visible in the capture, showing source and destination IP addresses and ports.

- No connection establishment phase was observed.

- Packets contained the data payload but lacked reliability mechanisms.

<div style="text-align: center;">
    <img src="/img/BE_Reseau/UDP_dump2.png" style="width: 90%;"/>
</div>

### Observations with TCP:

- Three-Way Handshake:

    - **SYN** packet sent from client to server initiating the connection.

    - **SYN-ACK** packet sent from server to client acknowledging the SYN.

    - **ACK** packet sent from client to server completing the handshake.

- Data Transfer: 

    <div style="text-align: center;">
        <img src="/img/BE_Reseau/TCP_dump.png" style="width: 90%;"/>
    </div>

    - Data packets were sent with acknowledgment packets confirming receipt.

    - Flags such as `[P.]`, `[FP.]`, and `[F.]` indicated different stages of data transfer and connection termination.

    <div style="text-align: center;">
        <img src="/img/BE_Reseau/TCP_dump2.png" style="width: 90%;"/>
    </div>

- Connection Termination:

    - Graceful shutdown observed with final ACKs exchanged between client and server.

<br>

## **Part 4: Capturing and Analyzing Network Traffic**

Captured raw Ethernet frames using: `sudo tcpdump -xx 9025`

- Frame Structure:

    - Destination MAC Address: First 6 bytes.

    - Source MAC Address: Next 6 bytes.

    - EtherType: Following 2 bytes indicating the protocol (e.g., IPv4).

- IP Packet Details:
    - Protocol Field (9th Byte): Indicates the transport layer protocol:

    - `06` for TCP.

    - `17` for UDP.

- Source and Destination IP Addresses: Each 4 bytes in length.

    - Source Port Number: 2 bytes.

<div style="text-align: center;">
    <img src="/img/BE_Reseau/eth_trafic.png" style="width: 90%;"/>
</div>

- Utility Commands:

    - Used `ifconfig` to determine the machine's IP address for analysis.

    <div style="text-align: center;">
        <img src="/img/BE_Reseau/ifconfig.png" style="width: 70%;"/>
    </div>

<br>

## **Part 5: Exploring Broadcast Traffic**

Captured broadcast messages with: `tcpdump -xx broadcast`

- Observation:

    - Destination IP address was 169.254.255.255, representing the broadcast address.

    - Messages sent to this address are received by all machines on the local network.

    <div style="text-align: center;">
        <img src="/img/BE_Reseau/broadcast.png" style="width: 70%;"/>
    </div>

- Conclusion:

    - Broadcast allows communication with all nodes simultaneously.

    - Useful for services like network discovery and announcements.


# Conclusion

This project explored the fundamental differences between UDP and TCP protocols, practicing socket creation and machine-to-machine communication management using C. We observed the advantages and disadvantages of each protocol, including UDP's speed but lack of delivery guarantees, versus TCP's reliability and error handling. In addition, using tcpdump allowed us to analyze network traffic and better understand transmission mechanisms, such as TCP handshake and Ethernet frame structure. This project provided a solid foundation for understanding the challenges of network communication in distributed environments.
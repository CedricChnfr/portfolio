---
layout: default
title:  "Security for Connected Objects"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

# Security for Connected Objects

## PART A: GENERALITIES

### Presentation
The "Security for Connected Objects" course taught by E. Alata and V. Migliore was an essential part of my learning journey as I am interested in the security field. It provided a comprehensive understanding of the security measures required for IoT devices. The course covered various security protocols, cryptographic techniques, and the impact of security vulnerabilities on IoT systems.


## PART B: DESCRIPTIVE PART

### Experience Details

#### Environment and Context
During this course, I delved into both theoretical and practical aspects of IoT security. The relevance of securing IoT devices in today's interconnected world was evident and the hands-on labs allowed me to apply the concepts learned in class to real-world scenarios.

#### My Function
In this course, I was responsible for:
- Understanding various security protocols and cryptographic techniques.
- Implementing security measures for IoT devices.
- Conducting experiments to identify and mitigate security vulnerabilities in IoT systems.
- Analyzing and preventing Man-in-the-Middle (MITM) attacks on IoT communication protocols.

## PART C: TECHNICAL PART

This section explores the technical aspects of IoT security, focusing on the implementation and verification of security protocols.

### Technical Concepts Learned

#### 1. SQL Injection
I learned about SQL injection attacks and how they can be used to extract information from a database. For example, by entering `admin' OR 1=1 OR '1'='1` in the authentication field and any arbitrary password like `vhjvg`, an attacker can bypass the authentication mechanism. This is because the SQL query becomes always true, allowing unauthorized access to sensitive data. Understanding this vulnerability helped me to implement measures to prevent such attacks in IoT systems.

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/SQL_injection.png" style="width: 60%;"/>
</div>
<br>

#### 2. Cross-Site Scripting (XSS)
We explored XSS attacks, which involve injecting malicious scripts into web pages viewed by other users. This can lead to data theft, session hijacking, and other malicious activities. We practiced identifying and mitigating XSS vulnerabilities in web applications.

For example, we executed JavaScript code in the username field by entering `<script>alert('Bonjour');</script>` or `<script>document.write("<img src='xxxx'/>");</script>`. This demonstrated how an attacker could inject scripts to manipulate the web page or steal information. The repercussions of such attacks can be severe, including unauthorized access to user data and the spread of malware.

#### 3 Man-in-the-Middle (MITM) Attacks
I learned about Man-in-the-Middle (MITM) attacks, where an attacker intercepts and potentially alters the communication between two parties without their knowledge. This type of attack can lead to data breaches and unauthorized access to sensitive information.

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/Man_Middle.png" style="width: 60%;"/>
</div>
<br>

For example, in the attacker file we implemented a simple MITM attack using the mbedTLS library where the attacker intercepts and modifies messages between Alice and Bob. The attacker reads the message from Bob, alters it, and then sends the modified message to Alice. This demonstrates how an attacker can manipulate the communication between two parties, highlighting the importance of securing communications to prevent such attacks.

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/lab3_terminal.png" style="width: 100%;"/>
</div>
<br>

During the lab3, we worked on a scenario where Alice sends a certificate to Bob. Bob receives the certificate and verifies it. At the same time, a hacker intercepts and prints the key. Bob then sends a message back to Alice, but the hacker intercepts the message, alters it, and sends the modified message to Alice.

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/lab3_terminal2.png" style="width: 100%;"/>
</div>
<br>

## PART D: ANALYTICAL PART

### Knowledge and Skills Mobilized
- Understanding the fundamentals of security.
- Identifying security weaknesses in an IoT architecture.
- Assessing the impact of exploiting a security vulnerability in an IoT architecture.
- Proposing adequate security counter-measures.
- Designing secure communication protocols for IoT.

### Self Evaluation
I already had a first overview of all these concepts, but this course provided a more advanced and technical perspective. We delved into coding using C and tried SQL injection attacks. It was a bit challenging for me since I had never used SQL before, so I had to learn quickly to be efficient. Additionally, working alone during lab sessions pushed me to work harder to understand all the concepts thoroughly.

### My Opinion
This course was very interesting and challenging. I learned a lot about security vulnerabilities and how to prevent them. In my future career, I am interested in working in the security field that mean I have to stay informed about the latest security threats. I really appreciated the practical labs that allowed me to apply the concepts learned in class and I am a bit disappointed that we did not have more time to explore other security concepts


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
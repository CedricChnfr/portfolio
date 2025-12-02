---
layout: default
title:  "Security for Connected Objects"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---



[← Back to My Courses 2024-2025](./my-courses-2024-2025.html)

**🔗 Cours connexes**: 
- [Middleware for IoT - S9](./2024-10-03-middleware-iot.html) - Protocoles de communication sécurisés
- [Emerging Network Technologies - S9](./2024-10-03-emerging-network.html) - Sécurité réseau SDN

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

Correction:

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/lab3_terminal3.png" style="width: 100%;"/>
</div>
<br>

##### Common Name from Verify Function
In the context of verifying certificates, the Common Name (CN) is an important attribute. It is part of the certificate's Subject field and typically represents the domain name or identity of the certificate holder. During the verification process, the CN is checked against the hostname or identity to ensure that the certificate is valid for the intended recipient.

For example, if a certificate is issued to `www.alice.com`, the CN should match `www.alice.com`. If there is a mismatch, the verification process will fail, indicating a potential security issue. This check helps prevent Man-in-the-Middle (MITM) attacks by ensuring that the certificate presented by a server matches the expected identity.


#### 4. Symmetric and Asymmetric Keys
We studied the differences between symmetric and asymmetric key encryption. Symmetric key encryption uses the same key for both encryption and decryption, making it faster but requiring secure key distribution. Asymmetric key encryption uses a pair of keys (public and private) for encryption and decryption, enhancing security but at the cost of performance.

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/asymetric.png" style="width: 70%;"/>
</div>
<br>

#### 5. Caesar Cipher
We learned about the Caesar cipher, a simple encryption technique where each letter in the plaintext is shifted a certain number of places down the alphabet. Although it is not secure by modern standards, it helped us understand the basics of encryption and decryption.

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/cypher.png" style="width: 40%;"/>
</div>
<br>

#### 6. Hash Functions
We studied hash functions, which take an input and produce a fixed-size string of bytes. Hash functions are used for data integrity verification, password storage, and digital signatures. We explored various hash functions like MD5, SHA-1, and SHA-256. Additionally, we learned about lightweight hash functions specified in ISO/IEC 29192-5:2016, including:

- **PHOTON**: a lightweight hash-function with permutation sizes of 100, 144, 196, 256, and 288 bits, computing hash-codes of length 80, 128, 160, 224, and 256 bits, respectively.
- **SPONGENT**: a lightweight hash-function with permutation sizes of 88, 136, 176, 240, and 272 bits, computing hash-codes of length 88, 128, 160, 224, and 256 bits, respectively.
- **Lesamnta-LW**: a lightweight hash-function with permutation size 384 bits, computing a hash-code of length 256 bits.

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/hash.png" style="width: 60%;"/>
</div>
<br>

#### 7. AES (Advanced Encryption Standard)
We learned about AES, a symmetric key encryption standard used worldwide. AES encrypts data in fixed-size blocks using keys of 128, 192, or 256 bits. 

The AES algorithm consists of several rounds of processing, each involving four main steps: AddRoundKey, SubBytes, ShiftRows, and MixColumns.

1. **AddRoundKey**: In this step, each byte of the state is combined with a block of the round key using bitwise XOR. This step is crucial for the security of AES as it introduces the key into the encryption process.

2. **SubBytes**: This is a non-linear substitution step where each byte in the state is replaced with another byte using an S-box (substitution box). The S-box is designed to provide resistance against linear and differential cryptanalysis.

3. **ShiftRows**: In this step, the rows of the state are shifted cyclically to the left. The amount of shift depends on the row index. This step helps in the diffusion of the plaintext.

4. **MixColumns**: This is a mixing operation that operates on the columns of the state, combining the four bytes in each column. This step ensures that the columns of the state are mixed, providing further diffusion.

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/aes.png" style="width: 90%;"/>
</div>
<br>

In our [Innovative project (What a Leak)](./innovative-project.html#3-security-features), we implemented the AES algorithm with other concepts such as initialization vector, padding, and PKCS#7.

#### 8. Quantum Lab

##### **NEC Protocol**

We established communication between two boards using the NEC protocol, commonly used in remote controls. The transmitter encoded messages into NEC format and sent them via infrared pulses. The receiver decoded these signals back into the original message.

**Example:**
- **Transmitter:** Encodes "A" into NEC format and sends it.
- **Receiver:** Decodes the infrared signal back to "A".

This exercise demonstrated the importance of precise timing and reliability in infrared communication.

**Signal Data for "A":**
- **NEC Format:** The NEC protocol uses a 32-bit data frame. For the character "A", the signal data would be encoded as follows:
    - **Address:** 0x8D
    - **Address Inverse:** 0x72
    - **Command:** 0x45 (ASCII code for "A")
    - **Command Inverse:** 0x4E

The complete 32-bit data frame for "A" would be: `0x8D72454E`.

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/nec.png" style="width: 90%;"/>
</div>
<br>

##### **Quantum Key/Message Distribution (QKD)**

After completing the classical test using `/dev/tty1CM0`, we proceeded with the quantum test on `/dev/ttyACM1`. Initially, we performed a calibration by setting the angle to 0, scan resolution to 1, offset to 0, and polarization to 0. We then converted the luminosity signal into voltage by scanning and measuring the intensity after the linear polarizer as it rotated through a full 360 degrees. Following the calibration, we executed a Python script to automate key distribution and generate a 32 kbit key. 

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/cute.png" style="width: 25%;"/>
    <img src="/img/BE_Secu/hdva.png" style="width: 40%;"/>
    <img src="/img/BE_Secu/key.png" style="width: 40%;"/>
</div>
<br>

Additionally, we introduced a prism to the setup, allowing the light signals from Bob, Alice, and Eve to pass through. This was done to facilitate the sharing of the key with another user. The prism helped in splitting the light signals, ensuring that the key distribution could be securely shared with the new user without compromising the integrity of the original communication.

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/prisme.png" style="width: 90%;"/>
</div>
<br>

#### 9. Cryptographic Lab
In this lab, we explored various cryptographic concepts and techniques, enhancing our understanding of how to secure data and communications.

##### AES Encryption
We studied AES (Advanced Encryption Standard), a symmetric key encryption standard used worldwide. AES encrypts data in fixed-size blocks using keys of 128, 192, or 256 bits. The algorithm consists of several rounds of processing, each involving steps like AddRoundKey, SubBytes, ShiftRows, and MixColumns.

In the `1/source.py` file, we implemented AES encryption and decryption using the pycryptodome library.

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/flag3.png" style="width: 30%;"/>
    <img src="/img/BE_Secu/flag1.png" style="width: 50%;"/>
</div>
<br>

1. Keyword Selection
The script reads a list of words from a file named `words` and randomly selects one as the keyword.

2. Key Generation
The selected keyword is hashed using the MD5 algorithm to generate a 128-bit key for AES encryption.

3. Flag Encryption
The predefined flag is padded to a multiple of the AES block size (16 bytes) and encrypted using the generated key in ECB mode.

4. Flag Decryption
The encrypted flag is decrypted using the same key to ensure the encryption and decryption processes are correct.


##### RSA Encryption
We learned about RSA encryption, an asymmetric cryptographic algorithm that uses a pair of keys (public and private) for encryption and decryption. The security of RSA relies on the difficulty of factoring large prime numbers.

In the `2/source.py` file, RSA encryption and decryption was implemented. The script generates two large prime numbers, computes their product (`n`), and uses it along with the public exponent (`e`) to encrypt a plaintext message. The private exponent (`d`) is used to decrypt the ciphertext back to the original plaintext.

##### Cube Root Attack
We also explored a cube root attack on RSA when the public exponent (`e`) is small (e.g., `e = 3`). If the ciphertext (`c`) is small enough, we can compute the plaintext by taking the integer cube root of `c`.

In the `2/attack.py` file, we implemented this attack to recover the plaintext from the ciphertext.

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/flag4.png" style="width: 30%;"/>
    <img src="/img/BE_Secu/flag1.png" style="width: 50%;"/>
</div>
<br>

#### 10. Confidentiality, Integrity, and Authenticity
We studied the principles of confidentiality, integrity, and authenticity in information security. Confidentiality ensures that information is accessible only to those authorized to access it. Integrity ensures that the information is accurate and has not been tampered with. Authenticity verifies the identity of the parties involved in communication.


## PART D: ANALYTICAL PART

### Knowledge and Skills Mobilized
- Understanding the fundamentals of security.
- Identifying security weaknesses in an IoT architecture.
- Assessing the impact of exploiting a security vulnerability in an IoT architecture.
- Proposing adequate security counter-measures.
- Designing secure communication protocols for IoT.

### Self Evaluation
I already had a first overview of almost all these concepts, but this course provided a more advanced and technical perspective. We delved into coding using C and tried SQL injection attacks. It was a bit challenging for me since I had never used SQL before, so I had to learn quickly to be efficient.
Moreover, there were a lot of concepts explained in class that we didn't practice. I have the feeling of not being fully up to date everywhere as it was just theory. The elements explained by the teacher during the courses were a plus for me as they were clear, and I wanted to be effective on the concepts.
Additionally, working alone during lab sessions pushed me to work harder to understand all the concepts thoroughly.


### My Opinion
This course was very interesting and challenging. I learned a lot about security vulnerabilities and how to prevent them. In my future career, I am interested in working in the security field that mean I have to stay informed about the latest security threats. I really appreciated the practical labs that allowed me to apply the concepts learned in class and I am a bit disappointed that we did not have more time to explore other security concepts.
At the end of the semester, we had a quantum lab that was really interesting. Unfortunately, we were the "test class" because no one had done it before. Even though we encountered some problems finalizing it, working in partnership with the teachers was a great experience. I hope to discover more about quantum in the future as it is an interesting field.


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
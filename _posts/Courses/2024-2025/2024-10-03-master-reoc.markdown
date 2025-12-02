---
layout: default
title:  "Master REOC"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---



[← Back to My Courses 2024-2025](./my-courses-2024-2025.html)

# Master REOC

## PART A: GENERALITIES

### Presentation
The Master REOC program was an intensive and comprehensive journey into the world of embedded networks and connected objects. This program covered a wide range of topics, from network protocols and security to IoT applications and embedded systems. The depth and breadth of the curriculum provided a solid foundation for understanding the complexities of modern networked systems.

## PART B: DESCRIPTIVE PART

### Experience Details

#### Environment and Context
Throughout the Master REOC program, I was immersed in both theoretical and practical aspects of embedded networks and connected objects. The relevance of these technologies in today's interconnected world was evident, and the hands-on projects allowed me to apply the concepts learned in class to real-world scenarios.

#### My Function
In this program, I was responsible for:
- Developing the network architecture and implementing the communication protocols.
- Creating Docker instances and simulating the network topology using Containernet.
- Implementing monitoring and adaptation mechanisms for network management.
- Ensuring the security and integrity of the network data.

## PART C: TECHNICAL PART

This section explores the technical aspects of SDN and MANO, focusing on their applications in network management and orchestration.
#### 1. Network Architecture
We designed a network topology composed of multiple switches and hosts to simulate a complex network environment. The topology included components such as switches (S1, S2, S3), hosts (Z1, Z2, Z3), an intermediary gateway (GI), and a server. This setup allowed us to test data filtering and connectivity between network components.

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_REOC/topology.png" style="width: 30%;"/>
</div>

```python
def setup_topology():
    net = DCNetwork(monitor=False, enable_learning=True)

    # Adding switches
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')

    # Adding Docker containers as network hosts
    z1 = net.addDocker('z1', ip='10.0.0.1', dimage="reoc:device")
    z2 = net.addDocker('z2', ip='10.0.0.2', dimage="reoc:device")
    z3 = net.addDocker('z3', ip='10.0.0.3', dimage="reoc:device")
    
    ordonnanceur = net.addDocker('ordon', ip='10.0.0.100', dimage="reoc:test")
    gateway_inter = net.addDocker('gi', ip='10.0.0.254', dimage="reoc:gateway")
    serveur = net.addDocker('serveur', ip='10.0.0.200', dimage="reoc:server")

    # Creating links between switches and hosts
    net.addLink(s1, z1)
    net.addLink(s1, z2)
    net.addLink(s1, z3)
    net.addLink(s2, s1, intfName1='s2-s1', intfName2='s1-s2')
    net.addLink(s2, ordonnanceur)
    net.addLink(s2, gateway_inter)
    net.addLink(s3, s2, intfName1='s3-s2', intfName2='s2-s3')
    net.addLink(s3, serveur)

    # Adding datacenter and API endpoints
    dc1 = net.addDatacenter("dc1")
    api1 = OpenstackApiEndpoint("0.0.0.0", 6001)
    api1.connect_datacenter(dc1)
    api1.start()
    api1.connect_dc_network(net)

    rapi1 = RestApiEndpoint("0.0.0.0", 5001)
    rapi1.connectDCNetwork(net)
    rapi1.connectDatacenter(dc1)
    rapi1.start()

    # Starting the network
    net.start()
    net.CLI()
    net.stop()

if __name__ == '__main__':
    setup_topology()
```

#### 2. Docker Instances
We used Docker to create instances for each network component. A script was developed to build Docker images and generate instances efficiently. This setup facilitated the testing of connectivity and data transmission between different zones.

```bash
#!/bin/bash
SCRIPT_PATH=$(realpath "$0")
SCRIPT_DIR=$(dirname "$SCRIPT_PATH")
cd "$SCRIPT_DIR" || exit 1
for dockerfile in "$SCRIPT_DIR"/*.dockerfile; do
    image_tag="reoc:$(basename "$dockerfile" .dockerfile)"
    echo "Building image: $image_tag from $dockerfile"
    docker build -t "$image_tag" -f "$dockerfile" .
done
```
#### 3. Simulation with Containernet
I used Containernet, a fork of Mininet, to simulate the network topology. This involved creating and managing network links, and ensuring the connectivity between Docker instances. I developed a script to reset the simulation environment and remove any residual connections.

Once the `topology_sdn.py` script is launched I tested the connectivity between different hosts in the topology, I used the following ping commands:
Test connectivity from each instances to other hosts:
```bash
containernet> z1 ping -c 1 z2
containernet> z1 ping -c 1 serveur
```

Test connectivity from `z2` to other hosts:
```bash
containernet> z2 ping -c 1 z1
containernet> z2 ping -c 1 gi
```

Test connectivity from `ordon` (scheduler) to other hosts:
```bash
containernet> ordon ping -c 1 z3
containernet> ordon ping -c 1 serveur
```

#### 4. Application 'Moniteur'

##### 4.1 Monitoring
The monitoring interface, developed with npyscreen allows users to select and execute various scripts based on the tests they wish to perform. For instance, to monitor the data sent by each zone, we focus on switch S1. By calling the Ryu API, we can observe metrics such as incoming and outgoing traffic, packet size, and total bytes in real-time.

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_REOC/monitor.png" style="width: 60%;"/>
</div>

##### 4.2 Adaptation
Adaptation scenarios include blocking frames from Z2 and Z3 or reducing their bandwidth while prioritizing Z1. This is achieved using POST requests to the Ryu API to apply rules such as:

```json
{
    "dpid": 1,
    "table_id": 0,
    "priority": 1,
    "match": {
        "in_port": 2
    },
    "instructions": [
        {
            "type": "APPLY_ACTIONS",
            "actions": [
                {
                    "type": "DROP"
                }
            ]
        }
    ]
}
```


## PART D: ANALYTICAL PART

### The Knowledge and Skills Mobilized
- Understanding SDN architecture and its applications.
- Developing applications for traffic management using SDN.
- Deploying and orchestrating network functions dynamically.

### Self Evaluation
The Master REOC program was intensive, especially since we had INSA courses in parallel. However, it was a valuable experience as I learned new concepts that I could implement after careful analysis of libraries and understanding how SDN works. Thanks to my partner, Yohan Boujon, we were efficient as we knew each other well and developed almost everything that was required in a short time during the labs.

### My Opinion
If I had to choose again, I would undoubtedly enroll in the Master REOC program. The curriculum allowed me to extend my vision of networks in embedded systems and gain valuable experience. The teachers provided a solid foundation to understand all the concepts in the professional world. The skills I acquired will be useful for my career. This program has significantly contributed to my professional growth and prepared me for future challenges in the field of networked systems.


<div style="text-align: center;">
    <h1>Project Report</h1>
</div>

You can find the complete project report on [GitHub_SDCI_REOC](https://github.com/CedricChnfr/sdci-reoc).

<div style="display: flex; justify-content: center;">
    <iframe src="/img/BE_REOC/CHANFREAU_BOUJON_SDCI.pdf" width="100%" height="800px" style="overflow: auto;" frameborder="0"></iframe>
</div>

<p style="text-align: center;">
    <a href="/img/BE_REOC/CHANFREAU_BOUJON_SDCI.pdf" target="_blank">Open Complete Report</a>
</p>

<p style="text-align: center;">
    <a href="https://docs.google.com/presentation/d/1N_HovdFQlvxd32VUzZlEpD46pnBx_45RN4CnxDaeWEs/edit">Open Lab Subject</a>
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
---
layout: default
title:  "C and Network Project"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

<style>
p {
  text-align: justify;
}
</style>

<div class="back-nav">
    <a href="./my-projects.html" data-i18n-html="back-projects">&larr; Retour aux Projets</a>
</div>

<div class="lang-fr">
<h1>Introduction</h1>
<p>Ce projet consiste a developper une application reseau simple en C utilisant l'API socket pour explorer les fonctionnalites des protocoles UDP et TCP. L'objectif est de comprendre comment ces protocoles gerent la transmission de messages dans un environnement reseau, en se concentrant sur les differences en termes de fiabilite, de livraison des messages et de gestion des connexions.</p>
<p>Dans ce TP, nous avons explore les differences fondamentales entre les protocoles UDP et TCP en utilisant l'application tsock dans un environnement Linux. L'objectif etait d'observer comment chaque protocole gere la transmission de donnees, la fiabilite et l'etablissement de connexion.</p>

<h2>Partie 1 : Comparaison UDP et TCP</h2>
<h3>Transmission UDP :</h3>
<p><strong>Configuration :</strong></p>
<p>Sur le Terminal 1 (agissant comme serveur ou recepteur), nous avons demarre un socket UDP ecoutant sur le port 9025 avec une taille de tampon de 10 octets en utilisant la commande : <code>tsock -p -u -t 10 9025</code></p>
</div>

<div class="lang-en">
<h1>Introduction</h1>
<p>This project involves developing a simple network application in C using the socket API to explore the functionalities of UDP and TCP protocols. The goal is to understand how these protocols handle message transmission in a networked environment, with focus on the differences in reliability, message delivery, and connection handling.</p>
<p>In this lab, we explored the fundamental differences between the UDP and TCP protocols using the tsock application in a Linux environment. The objective was to observe how each protocol handles data transmission, reliability, and connection establishment.</p>

<h2>Part 1: Comparing UDP and TCP</h2>
<h3>UDP Transmission:</h3>
<p><strong>Setup:</strong></p>
<p>On Terminal 1 (acting as the server or sink), we started a UDP socket listening on port 9025 with a buffer size of 10 bytes using the command: <code>tsock -p -u -t 10 9025</code></p>
</div>

<div style="text-align: center;">
    <img src="/img/BE_Reseau/UDP_cmd.png" style="width: 90%;"/>
</div>

<div class="lang-fr">
<p>Sur le Terminal 2 (agissant comme client ou source), nous avons envoye 20 messages au serveur en utilisant : <code>tsock -s -u -n 20 insa-20661 9025</code></p>
<p><strong>Observation :</strong> Sur 20 messages envoyes, seuls 13 ont ete recus. Le tampon d'application cote recepteur est devenu sature car il traitait les messages plus lentement qu'ils n'arrivaient.</p>
</div>

<div class="lang-en">
<p>On Terminal 2 (acting as the client or source), we sent 20 messages to the server using: <code>tsock -s -u -n 20 insa-20661 9025</code></p>
<p><strong>Observation:</strong> Out of 20 messages sent, only 13 were received. The application buffer on the receiver's side became saturated because it processed messages slower than they arrived.</p>
</div>

<div style="text-align: center;">
    <img src="/img/BE_Reseau/UDP_send.png" style="width: 90%;"/>
</div>

<div class="lang-fr">
<p><strong>Conclusion :</strong> UDP est un protocole sans connexion, sans mecanismes de controle de flux ou de correction d'erreurs. Des pertes de paquets sont survenues en raison d'un debordement de tampon au niveau de l'application. UDP ne garantit ni la livraison des messages, ni l'ordre, ni l'integrite.</p>

<h3>Transmission TCP :</h3>
<p><strong>Configuration :</strong> Sur le Terminal 1, nous avons demarre un socket TCP ecoutant sur le port 9025 avec une taille de tampon de 20 octets : <code>tsock -p -t 20 9025</code></p>
</div>

<div class="lang-en">
<p><strong>Conclusion:</strong> UDP is a connectionless protocol without mechanisms for flow control or error correction. Packet loss occurred due to buffer overflow at the application level. UDP does not guarantee message delivery, order, or integrity.</p>

<h3>TCP Transmission:</h3>
<p><strong>Setup:</strong> On Terminal 1, we started a TCP socket listening on port 9025 with a buffer size of 20 bytes: <code>tsock -p -t 20 9025</code></p>
</div>

<div style="text-align: center;">
    <img src="/img/BE_Reseau/TCP_cmd.png" style="width: 90%;"/>
</div>

<div style="text-align: center;">
    <img src="/img/BE_Reseau/TCP_send.png" style="width: 90%;"/>
</div>

<div class="lang-fr">
<p><strong>Observation :</strong> Les 20 messages ont ete transmis et recus avec succes. Aucune perte de paquets n'est survenue et les messages sont arrives dans l'ordre.</p>
<p><strong>Conclusion :</strong> TCP est un protocole oriente connexion qui etablit une connexion avant le transfert de donnees. Il fournit la fiabilite grace aux acquittements, retransmissions et controle de flux. TCP assure l'integrite des donnees et la livraison ordonnee.</p>

<h2>Partie 2 : Test du comportement des protocoles sans ports ouverts</h2>
<h3>Refus de connexion TCP :</h3>
<p>La tentative d'envoi de messages a un port TCP sans socket en ecoute a resulte en une erreur "connexion refusee". Cela confirme que TCP necessite un recepteur actif pour etablir une connexion.</p>
</div>

<div class="lang-en">
<p><strong>Observation:</strong> All 20 messages were successfully transmitted and received. No packet loss occurred, and messages arrived in order.</p>
<p><strong>Conclusion:</strong> TCP is a connection-oriented protocol that establishes a connection before data transfer. It provides reliability through acknowledgments, retransmissions, and flow control. TCP ensures data integrity and ordered delivery.</p>

<h2>Part 2: Testing Protocol Behavior Without Open Ports</h2>
<h3>TCP Connection Refusal:</h3>
<p>Attempting to send messages to a TCP port without a listening socket resulted in a "connection refused" error. This confirms that TCP requires an active listener to establish a connection.</p>
</div>

<div style="text-align: center;">
    <img src="/img/BE_Reseau/TCP_beh.png" style="width: 90%;"/>
</div>

<div class="lang-fr">
<h3>Gestion des messages UDP :</h3>
<p>L'envoi de messages a un port UDP ferme n'a pas produit d'erreurs cote emetteur. Les messages ont ete envoyes sur le reseau, mais le recepteur ne les a pas traites. UDP ne verifie pas la presence de recepteurs actifs avant d'envoyer des donnees.</p>
</div>

<div class="lang-en">
<h3>UDP Message Handling:</h3>
<p>Sending messages to a closed UDP port did not produce errors on the sender's side. The messages were sent into the network, but the receiver did not process them. UDP does not check for active listeners before sending data.</p>
</div>

<div style="text-align: center;">
    <img src="/img/BE_Reseau/UDP_beh.png" style="width: 90%;"/>
</div>

<br>

<div class="lang-fr">
<h2>Partie 3 : Capture et analyse du trafic reseau</h2>
<p>Utilisation de <code>tcpdump</code> pour surveiller le trafic. Connexion a une machine de surveillance en utilisant : <code>ssh tcpdump@insa-20673</code>. Demarrage de la capture de paquets sur le port 9025 : <code>sudo tcpdump 9025</code></p>

<h3>Observations avec UDP :</h3>
<p>Les messages etaient visibles dans la capture, montrant les adresses IP et ports source et destination. Aucune phase d'etablissement de connexion n'a ete observee. Les paquets contenaient les donnees utiles mais manquaient de mecanismes de fiabilite.</p>
</div>

<div class="lang-en">
<h2>Part 3: Capturing and Analyzing Network Traffic</h2>
<p>Using <code>tcpdump</code> to Monitor Traffic. Connected to a monitoring machine using: <code>ssh tcpdump@insa-20673</code>. Started packet capture on port 9025: <code>sudo tcpdump 9025</code></p>

<h3>Observations with UDP:</h3>
<p>Messages were visible in the capture, showing source and destination IP addresses and ports. No connection establishment phase was observed. Packets contained the data payload but lacked reliability mechanisms.</p>
</div>

<div style="text-align: center;">
    <img src="/img/BE_Reseau/UDP_dump.png" style="width: 90%;"/>
</div>
<br>
<div style="text-align: center;">
    <img src="/img/BE_Reseau/UDP_dump2.png" style="width: 90%;"/>
</div>

<div class="lang-fr">
<h3>Observations avec TCP :</h3>
<p><strong>Poignee de main a trois voies :</strong></p>
<ul>
<li>Paquet <strong>SYN</strong> envoye du client au serveur pour initier la connexion.</li>
<li>Paquet <strong>SYN-ACK</strong> envoye du serveur au client pour acquitter le SYN.</li>
<li>Paquet <strong>ACK</strong> envoye du client au serveur pour completer la poignee de main.</li>
</ul>
<p><strong>Transfert de donnees :</strong> Les paquets de donnees ont ete envoyes avec des paquets d'acquittement confirmant la reception. Des drapeaux tels que <code>[P.]</code>, <code>[FP.]</code> et <code>[F.]</code> indiquaient differentes etapes du transfert de donnees et de la terminaison de connexion.</p>
<p><strong>Terminaison de connexion :</strong> Arret gracieux observe avec des ACK finaux echanges entre client et serveur.</p>
</div>

<div class="lang-en">
<h3>Observations with TCP:</h3>
<p><strong>Three-Way Handshake:</strong></p>
<ul>
<li><strong>SYN</strong> packet sent from client to server initiating the connection.</li>
<li><strong>SYN-ACK</strong> packet sent from server to client acknowledging the SYN.</li>
<li><strong>ACK</strong> packet sent from client to server completing the handshake.</li>
</ul>
<p><strong>Data Transfer:</strong> Data packets were sent with acknowledgment packets confirming receipt. Flags such as <code>[P.]</code>, <code>[FP.]</code>, and <code>[F.]</code> indicated different stages of data transfer and connection termination.</p>
<p><strong>Connection Termination:</strong> Graceful shutdown observed with final ACKs exchanged between client and server.</p>
</div>

<div style="text-align: center;">
    <img src="/img/BE_Reseau/TCP_dump.png" style="width: 90%;"/>
</div>
<div style="text-align: center;">
    <img src="/img/BE_Reseau/TCP_dump2.png" style="width: 90%;"/>
</div>

<br>

<div class="lang-fr">
<h2>Partie 4 : Capture et analyse du trafic reseau</h2>
<p>Capture de trames Ethernet brutes en utilisant : <code>sudo tcpdump -xx 9025</code></p>
<p><strong>Structure de la trame :</strong> Adresse MAC destination (6 premiers octets), Adresse MAC source (6 octets suivants), EtherType (2 octets suivants indiquant le protocole, ex : IPv4).</p>
<p><strong>Details du paquet IP :</strong> Champ protocole (9e octet) : <code>06</code> pour TCP, <code>17</code> pour UDP. Adresses IP source et destination : 4 octets chacune. Numero de port source : 2 octets.</p>
</div>

<div class="lang-en">
<h2>Part 4: Capturing and Analyzing Network Traffic</h2>
<p>Captured raw Ethernet frames using: <code>sudo tcpdump -xx 9025</code></p>
<p><strong>Frame Structure:</strong> Destination MAC Address (first 6 bytes), Source MAC Address (next 6 bytes), EtherType (following 2 bytes indicating the protocol, e.g., IPv4).</p>
<p><strong>IP Packet Details:</strong> Protocol Field (9th Byte): <code>06</code> for TCP, <code>17</code> for UDP. Source and Destination IP Addresses: each 4 bytes in length. Source Port Number: 2 bytes.</p>
</div>

<div style="text-align: center;">
    <img src="/img/BE_Reseau/eth_trafic.png" style="width: 90%;"/>
</div>

<div style="text-align: center;">
    <img src="/img/BE_Reseau/ifconfig.png" style="width: 70%;"/>
</div>

<br>

<div class="lang-fr">
<h2>Partie 5 : Exploration du trafic de diffusion</h2>
<p>Capture de messages de diffusion avec : <code>tcpdump -xx broadcast</code></p>
<p><strong>Observation :</strong> L'adresse IP de destination etait 169.254.255.255, representant l'adresse de diffusion. Les messages envoyes a cette adresse sont recus par toutes les machines du reseau local.</p>
<p><strong>Conclusion :</strong> La diffusion permet une communication avec tous les noeuds simultanement. Utile pour des services comme la decouverte de reseau et les annonces.</p>
</div>

<div class="lang-en">
<h2>Part 5: Exploring Broadcast Traffic</h2>
<p>Captured broadcast messages with: <code>tcpdump -xx broadcast</code></p>
<p><strong>Observation:</strong> Destination IP address was 169.254.255.255, representing the broadcast address. Messages sent to this address are received by all machines on the local network.</p>
<p><strong>Conclusion:</strong> Broadcast allows communication with all nodes simultaneously. Useful for services like network discovery and announcements.</p>
</div>

<div style="text-align: center;">
    <img src="/img/BE_Reseau/broadcast.png" style="width: 70%;"/>
</div>

<div class="lang-fr">
<h1>Conclusion</h1>
<p>Ce projet a explore les differences fondamentales entre les protocoles UDP et TCP, en pratiquant la creation de sockets et la gestion de la communication machine a machine en C. Nous avons observe les avantages et inconvenients de chaque protocole, notamment la vitesse d'UDP mais l'absence de garanties de livraison, contre la fiabilite de TCP et sa gestion des erreurs. De plus, l'utilisation de tcpdump nous a permis d'analyser le trafic reseau et de mieux comprendre les mecanismes de transmission, tels que la poignee de main TCP et la structure des trames Ethernet. Ce projet a fourni une base solide pour comprendre les defis de la communication reseau dans les environnements distribues.</p>
</div>

<div class="lang-en">
<h1>Conclusion</h1>
<p>This project explored the fundamental differences between UDP and TCP protocols, practicing socket creation and machine-to-machine communication management using C. We observed the advantages and disadvantages of each protocol, including UDP's speed but lack of delivery guarantees, versus TCP's reliability and error handling. In addition, using tcpdump allowed us to analyze network traffic and better understand transmission mechanisms, such as TCP handshake and Ethernet frame structure. This project provided a solid foundation for understanding the challenges of network communication in distributed environments.</p>
</div>

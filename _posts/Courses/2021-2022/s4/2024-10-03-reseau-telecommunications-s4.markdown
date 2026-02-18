---
layout: default
title: "Réseau et Télécommunications - S4"
date:   2024-10-02 10:56:03 +0200
---

# Réseau et Télécommunications - Semestre 4

---

## PART A - Présentation Générale du Cours

### Contexte et objectifs

Réseaux informatiques et protocoles TCP/IP. Configuration routeurs/switches, analyse trafic, sécurité. Applications IoT, industrie 4.0, datacenter.

**Objectifs :**
- Architecture TCP/IP (modèle OSI)
- Adressage IP, subnetting, routage
- Protocoles : Ethernet, IP, TCP/UDP, HTTP, DNS
- Configuration Cisco/Linux
- Sécurité réseau (firewall, VPN)

### Prérequis
- Informatique de base
- Notions réseaux (S2)

---

## PART B: EXPÉRIENCE, CONTEXTE ET FONCTION

### Module 1 : Modèles réseau

**OSI (7 couches) :**
1. Physique : bits, câbles, signaux
2. Liaison : trames, MAC, switches
3. Réseau : paquets, IP, routage
4. Transport : segments, TCP/UDP, ports
5. Session, Présentation, Application

**TCP/IP (4 couches) :**
- Accès réseau (Ethernet, WiFi)
- Internet (IP, ICMP)
- Transport (TCP, UDP)
- Application (HTTP, DNS, FTP)

### Module 2 : Couche Liaison et IP

**Ethernet :**
- Trame : @MAC source/dest, EtherType, CRC
- CSMA/CD (collisions)
- Switch : table CAM, apprentissage MAC

**Adressage IP :**
- IPv4 : 32 bits (4 octets), notation décimale
- Classes A/B/C (obsolètes), CIDR
- Subnetting : masque /24 = 255.255.255.0
- IPv6 : 128 bits (avenir)

**ARP :**
Résolution IP → MAC

### Module 3 : Routage

**Principe :**
Acheminement paquets entre réseaux.

**Table de routage :**
- Destination, masque, passerelle, interface
- Route par défaut (0.0.0.0/0)

**Protocoles :**
- **RIP** : vecteur distance, métrique sauts, simple
- **OSPF** : état lien, métrique coût, convergence rapide
- **BGP** : inter-AS, Internet backbone

**Configuration Cisco :**
```
Router(config)# interface GigabitEthernet0/0
Router(config-if)# ip address 192.168.1.1 255.255.255.0
Router(config-if)# no shutdown
Router(config)# ip route 0.0.0.0 0.0.0.0 192.168.1.254
```

### Module 4 : Transport et Application

**TCP (Transmission Control Protocol) :**
- Connecté, fiable, ordre garanti
- Handshake 3-way (SYN, SYN-ACK, ACK)
- Contrôle flux (fenêtre), congestion
- Applications : HTTP, FTP, SSH

**UDP (User Datagram Protocol) :**
- Non-connecté, rapide, non fiable
- Applications : DNS, streaming, VoIP

**Ports :**
- Well-known : 0-1023 (HTTP=80, HTTPS=443, SSH=22, DNS=53)
- Registered : 1024-49151
- Dynamic : 49152-65535

**Protocoles applicatifs :**
- **HTTP/HTTPS** : Web
- **DNS** : résolution noms
- **DHCP** : attribution IP automatique
- **FTP/SFTP** : transfert fichiers

---

## PART C: ASPECTS TECHNIQUES

### TP Configuration réseaux

**TP1 : Configuration switches**
- VLANs (séparation logique)
- Spanning Tree (boucles)
- Packet Tracer (simulation Cisco)

**TP2 : Routage statique/dynamique**
- Configuration 3 routeurs
- Routage statique inter-réseaux
- RIP/OSPF
- Tests ping, traceroute

**TP3 : Services réseau**
- Serveur DHCP (attribution IP)
- DNS (bind9 Linux)
- Serveur Web Apache

**TP4 : Analyse trafic Wireshark**
- Capture paquets (promiscuous mode)
- Filtres : tcp.port==80, ip.addr==x.x.x.x
- Analyse handshake TCP, requêtes HTTP

### Projet réseau entreprise

**Architecture :**
- 3 sites géographiques
- VLAN par service (admin, prod, DMZ)
- Routage inter-sites (VPN ou MPLS)
- Serveurs : DNS, DHCP, Web, File
- Sécurité : firewall, ACL

**Livrables :**
- Schéma réseau (topologie)
- Plan adressage IP
- Configuration équipements
- Tests et validation

---

## PART D: ANALYSE ET RÉFLEXION

### Évaluation
- TP configuration (40%)
- Projet réseau (30%)
- Contrôles (15%)
- Examen pratique (15%)

### Compétences acquises
- Architecture TCP/IP maîtrisée
- Configuration routeurs/switches Cisco/Linux
- Diagnostic réseau (ping, traceroute, Wireshark)
- Conception réseaux d'entreprise
- Sécurité réseau de base

### Débouchés
- Administrateur réseaux
- Ingénieur systèmes et réseaux
- Architecte réseau
- IoT (réseaux capteurs)

## 📚 Contenu du cours

### Modèle OSI et TCP/IP

#### Modèle OSI (7 couches)
1. **Physique** : Transmission bits (câbles, signaux)
2. **Liaison** : Trames, adressage MAC, contrôle d'erreur
3. **Réseau** : Routage, adressage IP
4. **Transport** : TCP/UDP, bout en bout
5. **Session** : Gestion des sessions
6. **Présentation** : Encodage, compression
7. **Application** : Services utilisateur

#### Modèle TCP/IP (4 couches)
1. **Accès réseau** : Ethernet, WiFi
2. **Internet** : IP, ICMP, ARP
3. **Transport** : TCP, UDP
4. **Application** : HTTP, FTP, DNS, etc.

### Couche Liaison de données

#### Ethernet
- **Trame Ethernet** :
  - Préambule (7 octets)
  - SFD (1 octet)
  - @ MAC destination (6 octets)
  - @ MAC source (6 octets)
  - Type/Longueur (2 octets)
  - Données (46-1500 octets)
  - FCS (4 octets)

- **Adresse MAC** : 48 bits (6 octets)
  - Format : XX:XX:XX:XX:XX:XX
  - 3 premiers octets : OUI (fabricant)
  - 3 derniers : identifiant unique

#### CSMA/CD (Ethernet filaire)
- Carrier Sense Multiple Access with Collision Detection
- Détection de porteuse
- Détection de collision
- Algorithme de backoff exponentiel

#### CSMA/CA (WiFi)
- Collision Avoidance
- RTS/CTS (Request To Send / Clear To Send)
- ACK obligatoire

#### Commutation (Switch)
- Table d'adresses MAC
- Apprentissage automatique
- Forwarding, filtering, flooding
- VLAN (Virtual LAN)
- Spanning Tree Protocol (STP)

### Couche Réseau

#### Protocole IP (Internet Protocol)

**IPv4 :**
- Adresse 32 bits (4 octets)
- Format : xxx.xxx.xxx.xxx
- Classes A, B, C, D, E
- Adresses privées (RFC 1918) :
  - 10.0.0.0/8
  - 172.16.0.0/12
  - 192.168.0.0/16

**En-tête IPv4 :**
- Version (4 bits)
- IHL (4 bits)
- Type of Service (8 bits)
- Longueur totale (16 bits)
- Identification, Flags, Fragment Offset
- TTL (Time To Live)
- Protocole (TCP=6, UDP=17, ICMP=1)
- Checksum
- @ IP source et destination

**Masque de sous-réseau :**
- Notation décimale : 255.255.255.0
- Notation CIDR : /24
- Calcul d'adresse réseau et broadcast

**IPv6 :**
- Adresse 128 bits
- Format hexadécimal : xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx
- Simplification notation
- Plus de NAT nécessaire
- Autoconfiguration (SLAAC)

#### ARP (Address Resolution Protocol)
- Résolution IP → MAC
- Cache ARP
- Requête broadcast, réponse unicast
- Commande : `arp -a`

#### ICMP (Internet Control Message Protocol)
- Messages de contrôle et d'erreur
- Echo Request/Reply (ping)
- Destination Unreachable
- Time Exceeded (traceroute)
- Redirect

#### Routage

**Principes :**
- Table de routage
- Next hop
- Métrique (coût)
- Route par défaut (default gateway)

**Routage statique :**
- Configuration manuelle
- Simple mais non scalable

**Routage dynamique :**
- RIP (Routing Information Protocol)
  - Distance vector
  - Métrique = nombre de sauts
  - Maximum 15 sauts
  
- OSPF (Open Shortest Path First)
  - Link state
  - Métrique = coût (bande passante)
  - Convergence rapide
  - Aires hiérarchiques

- BGP (Border Gateway Protocol)
  - Routage inter-domaine (Internet)
  - Path vector
  - AS (Autonomous System)

### Couche Transport

#### TCP (Transmission Control Protocol)

**Caractéristiques :**
- Orienté connexion (3-way handshake)
- Fiable (acquittements, retransmissions)
- Contrôle de flux (fenêtre glissante)
- Contrôle de congestion
- Ordre garanti

**Établissement connexion (3-way handshake) :**
1. SYN (client → serveur)
2. SYN-ACK (serveur → client)
3. ACK (client → serveur)

**Fermeture connexion (4-way handshake) :**
1. FIN (initiateur)
2. ACK
3. FIN (autre côté)
4. ACK

**En-tête TCP :**
- Port source et destination (16 bits chacun)
- Numéro de séquence (32 bits)
- Numéro d'acquittement (32 bits)
- Flags (SYN, ACK, FIN, RST, PSH, URG)
- Fenêtre (16 bits)
- Checksum
- Options

#### UDP (User Datagram Protocol)

**Caractéristiques :**
- Sans connexion
- Non fiable (pas d'acquittement)
- Pas de contrôle de flux
- Léger et rapide
- Applications temps réel (VoIP, streaming)

**En-tête UDP :**
- Port source (16 bits)
- Port destination (16 bits)
- Longueur (16 bits)
- Checksum (16 bits)

#### Ports
- Well-known ports (0-1023) : services standards
  - 20/21 : FTP
  - 22 : SSH
  - 23 : Telnet
  - 25 : SMTP
  - 53 : DNS
  - 80 : HTTP
  - 110 : POP3
  - 143 : IMAP
  - 443 : HTTPS
- Registered ports (1024-49151)
- Dynamic/Private ports (49152-65535)

### Couche Application

#### DNS (Domain Name System)
- Résolution nom de domaine → IP
- Hiérarchie : racine, TLD, domaines
- Enregistrements : A, AAAA, MX, CNAME, NS, PTR
- Requêtes récursives et itératives
- Cache DNS

#### DHCP (Dynamic Host Configuration Protocol)
- Attribution automatique d'adresses IP
- DORA : Discover, Offer, Request, Acknowledge
- Bail (lease time)
- Options : passerelle, DNS, NTP

#### HTTP/HTTPS
- Protocole Web
- Méthodes : GET, POST, PUT, DELETE
- Codes de statut : 200 OK, 404 Not Found, 500 Internal Error
- HTTPS : HTTP + TLS/SSL (chiffrement)

#### FTP (File Transfer Protocol)
- Transfert de fichiers
- Mode actif et passif
- Deux connexions : commande (21) et données (20)

#### SMTP, POP3, IMAP
- **SMTP** : Envoi de mails (port 25/587)
- **POP3** : Réception mails, téléchargement (port 110)
- **IMAP** : Réception mails, synchronisation (port 143)

### Sécurité réseau

#### Menaces
- Écoute (sniffing)
- Usurpation d'identité (spoofing)
- Man-in-the-Middle
- Déni de service (DoS, DDoS)
- Malware, ransomware

#### Protections

**Firewall :**
- Filtrage de paquets
- Règles (allow/deny)
- Stateful vs stateless

**VPN (Virtual Private Network) :**
- Tunnel chiffré
- Protocoles : IPsec, OpenVPN, WireGuard
- Accès distant sécurisé

**Chiffrement :**
- SSL/TLS pour HTTPS
- SSH pour administration
- WPA2/WPA3 pour WiFi

**Authentification :**
- Mots de passe
- Certificats
- 802.1X (authentification réseau)

## 🛠️ Travaux pratiques

### TP Configuration réseau
- Configuration IP statique/DHCP
- Test de connectivité (ping, traceroute)
- Commandes réseau (ipconfig, ifconfig)

### TP Analyse de trames
- Capture avec Wireshark
- Analyse Ethernet, IP, TCP, UDP
- Filtres d'affichage
- Reconstruction de flux

### TP Configuration switch
- VLANs
- Trunk ports
- Port security
- Spanning Tree

### TP Configuration routeur
- Configuration interfaces
- Routage statique
- NAT/PAT
- ACL (Access Control Lists)

### Projet réseau
- Architecture complète
- Routage inter-VLAN
- Services (DNS, DHCP, Web)
- Sécurisation

## 💻 Outils utilisés

### Simulation
- **Packet Tracer** : Simulation Cisco
- **GNS3** : Émulation réseaux complexes
- **EVE-NG** : Environnement virtuel

### Analyse
- **Wireshark** : Analyseur de protocoles
- **tcpdump** : Capture en ligne de commande
- **Nmap** : Scanner réseau

### Configuration
- **Cisco IOS** : Commandes routeurs/switches
- **pfSense** : Firewall open source
- **MikroTik RouterOS**

## 📊 Évaluation

- Travaux pratiques (40%)
- Projet réseau (30%)
- Contrôles de connaissances (20%)
- Examen pratique (10%)

## 🔗 Liens avec d'autres cours

- **Télécommunications** : Couche physique
- **IE** : Communication réseau embarquée
- **OL** : Outils de simulation

## 📐 Calculs réseau

### Calcul de sous-réseaux

**Exemple : 192.168.1.0/26**
- Masque : 255.255.255.192
- Nombre d'hôtes : 2^6 - 2 = 62
- Plages :
  - 192.168.1.0/26 : .1 à .62
  - 192.168.1.64/26 : .65 à .126
  - 192.168.1.128/26 : .129 à .190
  - 192.168.1.192/26 : .193 à .254

### VLSM (Variable Length Subnet Mask)
Allocation efficace d'adresses selon besoins

## 💡 Applications pratiques

### Entreprise
- Architecture réseau d'entreprise
- Segmentation par service
- Accès distant (VPN)
- Sécurité périmétrique

### Objets connectés
- Protocoles légers (MQTT, CoAP)
- IPv6 pour IoT
- Réseaux maillés
- Gateway IoT

### Data center
- Haute disponibilité
- Load balancing
- SDN (Software Defined Networking)
- Virtualisation réseau

## 📖 Compétences développées

- Configuration d'équipements réseau
- Analyse de protocoles
- Diagnostic de problèmes réseau
- Conception d'architectures
- Sécurisation des communications

## 🎯 Commandes essentielles

### Windows
```cmd
ipconfig /all
ping 8.8.8.8
tracert google.com
nslookup google.com
netstat -an
route print
arp -a
```

### Linux
```bash
ifconfig / ip addr
ping 8.8.8.8
traceroute google.com
dig google.com
netstat -tulpn / ss -tulpn
route -n / ip route
arp -n
```

### Cisco IOS
```
show ip interface brief
show running-config
show ip route
show vlan brief
ping
traceroute
```

## ⚠️ Problèmes courants

### Connectivité
- Câble débranché/défectueux
- Mauvaise configuration IP
- Passerelle incorrecte
- Firewall bloque

### Performance
- Congestion réseau
- Boucles (problème STP)
- Mauvaise configuration QoS
- Duplex mismatch

### Sécurité
- Ports ouverts inutilement
- Mots de passe faibles
- Absence de chiffrement
- Mises à jour manquantes

## 🔧 Bonnes pratiques

### Documentation
- Schéma réseau à jour
- Plan d'adressage
- Configuration sauvegardée
- Procédures

### Sécurité
- Changer mots de passe par défaut
- Désactiver services inutiles
- Segmentation réseau (VLANs)
- Monitoring et logs

### Performance
- QoS pour trafic critique
- Agrégation de liens
- Redondance
- Monitoring proactif

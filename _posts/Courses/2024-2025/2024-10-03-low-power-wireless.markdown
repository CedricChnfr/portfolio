---
layout: default
title:  "Low Power Wireless Personal Area Network (LP-WPAN)"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

<style>
.back-nav {
    margin: 20px 0;
    padding: 10px;
    background-color: #f0f0f0;
    border-radius: 5px;
}

.back-nav a {
    color: #007BFF;
    text-decoration: none;
    font-weight: bold;
}

.back-nav a:hover {
    text-decoration: underline;
}

.section-title {
    color: #007BFF;
    border-bottom: 2px solid #007BFF;
    padding-bottom: 5px;
    margin-top: 20px;
}

table {
    border-collapse: collapse;
    width: 100%;
    margin: 20px 0;
}

th, td {
    border: 1px solid #ddd;
    padding: 12px;
    text-align: left;
}

th {
    background-color: #007BFF;
    color: white;
}

tr:nth-child(even) {
    background-color: #f2f2f2;
}
</style>

<div class="back-nav">
    <a href="./my-courses-2024-2025.html">← Retour aux Cours 2024-2025</a>
</div>

# Low Power Wireless / WPAN IPv6

**Annee academique** : 2024-2025
**Semestre** : S9
**Categorie** : Reseaux sans fil et IoT

**Cours connexes** :
- [Wireless Sensor Networks - S9](./2024-10-03-wireless-sensors.html) - Protocoles MAC pour WSN, ZigBee
- [Emerging Network Technologies - S9](./2024-10-03-emerging-network.html) - SDN et architectures reseau
- [Middleware for IoT - S9](./2024-10-03-middleware-iot.html) - Protocoles applicatifs IoT (MQTT, CoAP)
- [Energy for Connected Objects - S9](./2024-10-03-energy-connected-object.html) - Gestion energetique des objets connectes

---

## PART A : PRESENTATION GENERALE

<h3 class="section-title">Vue d'ensemble</h3>

Le cours "Low Power Wireless / WPAN IPv6" offre une exploration approfondie des principes et des applications des reseaux sans fil personnels a faible consommation (LP-WPAN). L'objectif principal est de comprendre comment integrer IPv6 dans des reseaux contraints, en utilisant des mecanismes d'adaptation tels que 6LoWPAN, afin de permettre a des dispositifs a ressources limitees de communiquer sur Internet.

Ce cours couvre l'ensemble de la pile protocolaire adaptee aux objets connectes : de la couche physique IEEE 802.15.4 jusqu'aux protocoles applicatifs comme CoAP et MQTT-SN, en passant par la couche d'adaptation 6LoWPAN, le protocole de routage RPL, et les mecanismes de compression d'en-tetes IPv6.

**Objectifs pedagogiques** :
- Comprendre le panorama des technologies sans fil pour l'IoT (IEEE 802.15.4, BLE, LoRa, Sigfox, NB-IoT)
- Maitriser l'architecture 6LoWPAN et ses mecanismes de compression d'en-tetes
- Configurer et analyser des reseaux IPv6 sur des dispositifs contraints
- Comprendre le protocole de routage RPL pour les reseaux a faible puissance et a pertes (LLN)
- Mettre en oeuvre des protocoles applicatifs adaptes (CoAP, MQTT-SN)
- Analyser les compromis entre consommation energetique, portee et debit dans les LP-WPAN

<h3 class="section-title">Position dans le cursus</h3>

Ce module s'appuie sur les bases acquises precedemment :
- **Reseau (S5)** : modele OSI, Ethernet, IP de base, TCP/UDP
- **Interconnexion Reseau (S8)** : routage IP, protocoles de transport, IPv6
- **Wireless Sensor Networks (S9)** : protocoles MAC pour WSN, IEEE 802.15.4, ZigBee

Il prepare a :
- **Projets IoT** : deploiement de reseaux de capteurs communiquant en IPv6
- **Middleware for IoT** : integration de protocoles applicatifs sur reseaux contraints
- **Carriere professionnelle** : architecte IoT, ingenieur systemes embarques connectes

---

## PART B : EXPERIENCE ET CONTEXTE

<h3 class="section-title">Organisation et ressources</h3>

Le module combinait cours magistraux et travaux pratiques sur des plateformes reelles :

**Cours magistraux** :
- Panorama des technologies sans fil pour l'IoT (classification, comparaison)
- Architecture protocolaire pour les reseaux LP-WPAN
- Norme IEEE 802.15.4 : couches PHY et MAC
- 6LoWPAN : adaptation d'IPv6 pour les reseaux contraints
- Protocole de routage RPL (Routing Protocol for Low-Power and Lossy Networks)
- Technologies LPWAN : LoRa/LoRaWAN, Sigfox, NB-IoT
- Protocoles applicatifs : CoAP, MQTT-SN

**Travaux pratiques** :
- **TP1** : Auto-configuration d'adresses IPv6 link-local et globales
- **TP2** : Connectivite IPv6 de bout en bout avec serveur applicatif MQTT
- **TP3** : Compression d'en-tetes 6LoWPAN (analyse avec Wireshark)
- **TP4** : Routage RPL sur topologie multi-noeuds

**Outils utilises** :
- **Wireshark** : capture et analyse de trafic 6LoWPAN/IPv6
- **tcpdump** : capture de paquets en ligne de commande
- **Contiki-NG / RIOT OS** : systemes d'exploitation pour dispositifs contraints
- **Mosquitto** : broker MQTT pour distribution de donnees
- **ifconfig / ip** : configuration d'interfaces reseau IPv6

<h3 class="section-title">Environnement et contexte</h3>

Durant ce cours, j'ai travaille sur les aspects theoriques et pratiques des reseaux LP-WPAN. La partie initiale du cours couvrait les concepts fondamentaux des reseaux et des telecommunications, comme les interferences et les reseaux brouilles. Nous avons ensuite approfondi la pile protocolaire TCP/IP adaptee aux LP-WPAN, en utilisant la norme IEEE 802.15.4 pour les couches MAC et physique. Cette norme est couramment utilisee dans des protocoles comme ZigBee. Nous avons egalement explore l'utilisation d'IPv6 avec une couche intermediaire, 6LoWPAN, pour reduire la taille des paquets.

<h3 class="section-title">Ma fonction</h3>

Dans ce cours, j'etais responsable de :
- Comprendre les principes et l'architecture de 6LoWPAN
- Explorer les differents protocoles et leurs applications dans les reseaux sans fil a faible puissance
- Conduire des experiences pour tester l'efficacite et la scalabilite des differentes solutions LP-WPAN
- Analyser les trames 6LoWPAN avec Wireshark pour comprendre les mecanismes de compression
- Configurer le routage RPL et observer le comportement du reseau

---

## PART C : ASPECTS TECHNIQUES

<h3 class="section-title">1. Panorama des technologies sans fil pour l'IoT</h3>

Le cours commence par un panorama complet des technologies sans fil disponibles pour l'IoT. L'objectif est de comprendre les criteres de choix d'une technologie selon les contraintes de l'application : portee, debit, consommation energetique, cout, et topologie de reseau.

**Classification par portee et debit** :

| Technologie | Portee | Debit | Consommation | Usage typique |
|-------------|--------|-------|--------------|---------------|
| IEEE 802.15.4 / ZigBee | 10-100 m | 250 kbps | Tres faible | Domotique, capteurs |
| BLE (Bluetooth Low Energy) | 10-50 m | 1-2 Mbps | Tres faible | Wearables, beacons |
| Thread | 10-30 m | 250 kbps | Tres faible | Smart home |
| LoRa / LoRaWAN | 2-15 km | 0.3-50 kbps | Tres faible | Agriculture, smart city |
| Sigfox | 10-50 km | 100-600 bps | Ultra faible | Compteurs, tracking |
| NB-IoT | 1-10 km | 200 kbps | Faible | Compteurs, industriel |
| Wi-Fi (802.11ah) | 100-1000 m | 150 kbps-8 Mbps | Moyenne | IoT domestique |
| Z-Wave | 30-100 m | 100 kbps | Tres faible | Domotique |

**Distinction WPAN vs LPWAN** :

Les reseaux **WPAN** (Wireless Personal Area Network) sont des reseaux a courte portee, comme IEEE 802.15.4 et BLE, adaptes aux applications necessitant des communications frequentes a faible distance. Les reseaux **LPWAN** (Low Power Wide Area Network) comme LoRa, Sigfox et NB-IoT sont conçus pour des communications longue portee avec un debit tres faible, adaptes aux applications de telemetrie et de suivi.

**Criteres de selection** :

Le choix d'une technologie repose sur plusieurs facteurs :
- **Autonomie energetique** : duree de vie souhaitee sur batterie (mois, annees)
- **Portee necessaire** : interieur, exterieur, urbain, rural
- **Debit requis** : donnees periodiques legeres vs streaming continu
- **Latence** : temps reel vs best-effort
- **Densite de noeuds** : nombre de dispositifs par zone
- **Cout** : licence, infrastructure, dispositifs
- **Topologie** : etoile, maille, arbre

<h3 class="section-title">2. IEEE 802.15.4 : la norme fondamentale des LP-WPAN</h3>

La norme IEEE 802.15.4 definit les couches physique (PHY) et controle d'acces au medium (MAC) pour les reseaux LP-WPAN. C'est la base sur laquelle reposent de nombreux protocoles comme ZigBee, Thread et 6LoWPAN.

**Couche physique (PHY)** :

- **Bandes de frequences** :
  - 2.4 GHz (ISM mondiale) : 16 canaux, 250 kbps, modulation O-QPSK
  - 868 MHz (Europe) : 1 canal, 20 kbps, modulation BPSK
  - 915 MHz (Amerique) : 10 canaux, 40 kbps, modulation BPSK
- **Modulation** : Direct Sequence Spread Spectrum (DSSS) avec O-QPSK ou BPSK
- **Puissance d'emission** : typiquement -3 dBm a 10 dBm
- **Sensibilite du recepteur** : -85 dBm (2.4 GHz), -92 dBm (868/915 MHz)
- **Taille maximale de trame** : 127 octets (incluant en-tete MAC)

**Couche MAC** :

- **Acces au canal** : CSMA-CA (Carrier Sense Multiple Access with Collision Avoidance)
- **Modes de fonctionnement** :
  - **Mode beacon** : le coordinateur envoie des beacons periodiques pour synchroniser les noeuds ; utilise la superframe avec periodes actives et inactives
  - **Mode non-beacon** : acces asynchrone au canal, adapte aux topologies en etoile simples
- **Types de trames** : donnees, acquittement (ACK), commande MAC, beacon
- **Adressage** : adresses courtes (16 bits) ou etendues (64 bits IEEE EUI-64)
- **GTS (Guaranteed Time Slots)** : allocation de creneaux temporels garantis dans la superframe pour les applications temps reel

**Types de dispositifs** :

| Type | Role | Capacites |
|------|------|-----------|
| FFD (Full Function Device) | Coordinateur PAN, routeur | Toutes fonctions MAC, peut relayer |
| RFD (Reduced Function Device) | Noeud terminal | Fonctions limitees, ne peut pas relayer |

**Topologies supportees** :

- **Etoile** : tous les noeuds communiquent avec un coordinateur central
- **Pair-a-pair (mesh)** : les noeuds FFD peuvent communiquer entre eux directement
- **Arbre de clusters** : hierarchie de coordinateurs et sous-coordinateurs

<h3 class="section-title">3. IPv6 pour l'IoT : fondamentaux</h3>

IPv6 est le protocole de choix pour les reseaux IoT en raison de son espace d'adressage quasi illimite (2^128 adresses), de ses capacites d'auto-configuration, et de sa connectivite de bout en bout. Cependant, l'en-tete IPv6 standard (40 octets minimum) est trop volumineux pour les trames IEEE 802.15.4 limitees a 127 octets.

**Auto-configuration des adresses link-local** :

<div style="text-align: center; display: flex; justify-content: center; gap: 20px;">
    <img src="/img/BE_Low_Power/auto_conf.png" style="width: 70%;"/>
</div>
<br>

Nous avons execute la commande `ifconfig eth0 up` pour activer l'interface reseau `eth0`. Ensuite, nous avons utilise `ip -6 addr show dev eth0` pour afficher les adresses IPv6 assignees a l'interface. La sortie montrait une adresse au format `inet6 fe80::527c:6fff:fe56:e8b0`.

Cette adresse est une adresse IPv6 link-local, automatiquement configuree sur toutes les interfaces IPv6. Les adresses link-local utilisent le prefixe `fe80::/10` et la partie restante de l'adresse est derivee de l'adresse MAC de l'interface en utilisant le format Modified EUI-64.

**Processus de derivation EUI-64** :
1. Prendre l'adresse MAC 48 bits (ex: `50:7C:6F:56:E8:B0`)
2. Inserer `FF:FE` au milieu : `50:7C:6F:FF:FE:56:E8:B0`
3. Inverser le bit U/L (7eme bit du premier octet) : `52:7C:6F:FF:FE:56:E8:B0`
4. Resultat : `fe80::527c:6fff:fe56:e8b0`

**Auto-configuration des adresses unicast globales** :

<div style="text-align: center; display: flex; justify-content: center; gap: 20px;">
    <img src="/img/BE_Low_Power/dump.png" style="width:80%;"/>
</div>
<br>

Nous avons explore le processus d'auto-configuration des adresses unicast globales IPv6 en utilisant les Router Advertisements (RA). Le routeur envoie periodiquement des messages ICMPv6 Router Advertisement contenant le prefixe reseau. Les noeuds terminaux derivent leur adresse globale en combinant ce prefixe avec leur identifiant d'interface (EUI-64 ou adresse aleatoire).

**Messages ICMPv6 impliques** :
- **Router Solicitation (RS)** : envoye par un noeud pour solliciter un RA du routeur local
- **Router Advertisement (RA)** : envoye par le routeur avec le prefixe reseau et les options de configuration
- **Neighbor Solicitation (NS)** : utilise pour la detection d'adresse dupliquee (DAD) et la resolution d'adresse
- **Neighbor Advertisement (NA)** : reponse a un NS

<h3 class="section-title">4. 6LoWPAN : adaptation d'IPv6 aux reseaux contraints</h3>

6LoWPAN (IPv6 over Low-Power Wireless Personal Area Networks) est la couche d'adaptation cle qui permet l'utilisation d'IPv6 sur des reseaux IEEE 802.15.4. Il resout le probleme fondamental de l'incompatibilite entre la taille de l'en-tete IPv6 (40 octets minimum) et la taille maximale de la trame IEEE 802.15.4 (127 octets, dont seulement environ 80-100 octets utiles apres en-tete MAC).

**Fonctions principales de 6LoWPAN** :

- **Compression d'en-tetes** : reduction de l'en-tete IPv6 de 40 octets a aussi peu que 2-4 octets
- **Fragmentation et reassemblage** : decoupe des paquets IPv6 trop grands pour la MTU IEEE 802.15.4
- **Adressage mesh** : acheminement au niveau couche 2 dans un reseau maille
- **Support du multicast** : traduction des adresses multicast IPv6

**Architecture de la pile protocolaire 6LoWPAN** :

```
+-----------------------------------+
|  Application (CoAP, MQTT-SN)      |
+-----------------------------------+
|  Transport (UDP)                  |
+-----------------------------------+
|  Reseau (IPv6)                    |
+-----------------------------------+
|  Adaptation (6LoWPAN)             |
|  - Compression en-tetes (IPHC)   |
|  - Fragmentation                  |
|  - Mesh addressing                |
+-----------------------------------+
|  MAC (IEEE 802.15.4)              |
+-----------------------------------+
|  PHY (IEEE 802.15.4)              |
+-----------------------------------+
```

**Compression d'en-tetes IPHC (IP Header Compression)** :

<div style="text-align: center; display: flex; justify-content: center; gap: 20px;">
    <img src="/img/BE_Low_Power/header.png" style="width: 70%;"/>
</div>
<br>

Le mecanisme IPHC permet de compresser l'en-tete IPv6 en exploitant les informations deja disponibles dans le contexte de communication ou dans l'en-tete MAC IEEE 802.15.4 :

| Champ IPv6 | Taille originale | Methode de compression | Taille compressee |
|------------|------------------|------------------------|-------------------|
| Version | 4 bits | Toujours IPv6, elidee | 0 |
| Traffic Class | 8 bits | Souvent 0, elidee | 0-8 bits |
| Flow Label | 20 bits | Souvent 0, elidee | 0-20 bits |
| Payload Length | 16 bits | Deduite de la trame MAC | 0 |
| Next Header | 8 bits | Compressee via NHC | 0-8 bits |
| Hop Limit | 8 bits | Valeurs communes (1, 64, 255) | 0-8 bits |
| Adresse source | 128 bits | Derivee de l'adresse MAC | 0-128 bits |
| Adresse destination | 128 bits | Derivee de l'adresse MAC | 0-128 bits |

**Modes de compression des adresses** :

- **Stateless** : l'adresse est derivee de l'adresse MAC (EUI-64) dans l'en-tete IEEE 802.15.4
- **Stateful (context-based)** : le prefixe est connu via un contexte partage (identifie par un Context Identifier)
- **Multicast** : compression specifique des adresses multicast IPv6

<div style="text-align: center; display: flex; justify-content: center; gap: 20px;">
    <img src="/img/BE_Low_Power/compression.png" style="width: 70%;"/>
</div>
<br>

Nous avons utilise Wireshark pour capturer et analyser des paquets ICMPv6 encapsules dans des trames 6LoWPAN. En examinant la section ICMPv6, nous pouvions voir l'en-tete IPHC (IP Header Compression), qui fournit les informations sur les champs comprimes de l'en-tete IPv6. Cette analyse nous a permis de comprendre comment 6LoWPAN reduit l'overhead des en-tetes IPv6 pour les rendre compatibles avec les reseaux a faible puissance et a pertes.

**Fragmentation 6LoWPAN** :

Lorsqu'un paquet IPv6 depasse la MTU de la couche IEEE 802.15.4, 6LoWPAN le fragmente en plusieurs trames :
- **En-tete de fragmentation** : contient la taille du datagramme original, un tag d'identification, et l'offset du fragment
- **Premier fragment** : contient l'en-tete compresse IPHC et le debut du payload
- **Fragments suivants** : contiennent le tag, l'offset et la suite du payload
- Le reassemblage est effectue au noeud destinataire

**Adressage Mesh** :

L'en-tete mesh de 6LoWPAN permet l'acheminement des trames au niveau couche 2 dans un reseau maille. Il contient les adresses source et destination IEEE 802.15.4 originales, permettant aux noeuds intermediaires de relayer les trames sans necessite de routage IP.

<h3 class="section-title">5. Technologies LPWAN : LoRa, Sigfox, NB-IoT</h3>

En complement des technologies WPAN a courte portee, le cours aborde les technologies LPWAN (Low Power Wide Area Network) pour les communications longue portee.

**LoRa / LoRaWAN** :

LoRa (Long Range) est une technologie de modulation radio proprietaire (Semtech) utilisant la technique CSS (Chirp Spread Spectrum) :
- **Bande de frequences** : 868 MHz (Europe), 915 MHz (Amerique), 433 MHz (Asie)
- **Portee** : 2-5 km (urbain), 10-15 km (rural)
- **Debit** : 0.3 a 50 kbps selon le spreading factor (SF7 a SF12)
- **Spreading Factor** : plus le SF est eleve, plus la portee augmente mais le debit diminue

LoRaWAN est l'architecture reseau au-dessus de LoRa :
- **Topologie en etoile** : les dispositifs communiquent avec des gateways
- **Classes de dispositifs** :
  - **Classe A** : emission initiee par le dispositif, deux fenetres de reception apres emission (plus econome)
  - **Classe B** : fenetres de reception programmees via beacons (latence reduite)
  - **Classe C** : reception continue sauf pendant emission (latence minimale, consommation maximale)
- **Securite** : chiffrement AES-128 au niveau reseau et application

**Sigfox** :

- **Modulation** : Ultra Narrow Band (UNB), bande passante de 100 Hz par message
- **Portee** : 10-50 km
- **Debit** : 100 bps (uplink), 600 bps (downlink)
- **Limitation** : 140 messages/jour (uplink), 4 messages/jour (downlink)
- **Modele economique** : abonnement operateur, pas d'infrastructure propre

**NB-IoT (Narrowband IoT)** :

- **Standard** : 3GPP Release 13 (LTE Category NB1)
- **Bande de frequences** : bandes LTE licensiees (180 kHz)
- **Debit** : jusqu'a 200 kbps (downlink), 20 kbps (uplink)
- **Portee** : 1-10 km
- **Avantage** : utilise l'infrastructure cellulaire existante

<h3 class="section-title">6. ZigBee et Thread : piles protocolaires sur IEEE 802.15.4</h3>

**ZigBee** :

ZigBee est une pile protocolaire complete construite sur IEEE 802.15.4 :
- **Couche reseau** : routage par arbre ou maille, decouverte de routes AODV
- **Couche application** : profils standardises (ZigBee Home Automation, ZigBee Light Link)
- **Securite** : chiffrement AES-128, gestion de cles via Trust Center
- **Topologies** : etoile, arbre, maille
- **Limitations** : pile proprietaire (ZigBee Alliance), pas d'interoperabilite IP native

**Thread** :

Thread est une pile protocolaire moderne basee sur 6LoWPAN :
- **Base** : IEEE 802.15.4 + 6LoWPAN + IPv6
- **Routage** : protocole MLE (Mesh Link Establishment) pour la gestion du reseau maille
- **Avantage** : interoperabilite IP native, compatible avec les ecosystemes Internet
- **Securite** : DTLS (Datagram Transport Layer Security)
- **Usage** : smart home (supporte par Apple HomeKit, Google Nest)

**BLE (Bluetooth Low Energy)** :

- **Standard** : Bluetooth 4.0+ (BLE)
- **Portee** : 10-50 m
- **Debit** : 1-2 Mbps
- **IPv6 sur BLE** : 6LoWPAN peut etre utilise sur BLE via la specification IPSP (Internet Protocol Support Profile)
- **Mesh** : Bluetooth Mesh (depuis Bluetooth 5.0) pour les reseaux mailles

<h3 class="section-title">7. RPL : protocole de routage pour LLN</h3>

RPL (Routing Protocol for Low-Power and Lossy Networks, RFC 6550) est le protocole de routage standardise par l'IETF pour les reseaux 6LoWPAN. Il est specialement concu pour les reseaux a faible puissance et a pertes (LLN - Low-Power and Lossy Networks).

<div style="text-align: center; display: flex; justify-content: center; gap: 20px;">
    <img src="/img/BE_Low_Power/node.png" style="width: 90%;"/>
</div>
<br>

**Principe de fonctionnement** :

RPL construit un DODAG (Destination-Oriented Directed Acyclic Graph) : un graphe acyclique dirige oriente vers un noeud racine (root) qui sert de passerelle vers Internet.

**Construction du DODAG** :
1. Le noeud racine initie la construction en emettant des messages DIO (DODAG Information Object)
2. Chaque noeud recevant un DIO calcule son rang (distance au root) selon une fonction objectif (OF)
3. Le noeud selectionne un parent prefere parmi les voisins offrant le meilleur rang
4. Le processus se propage de proche en proche jusqu'aux feuilles

**Messages RPL** :

| Message | Direction | Role |
|---------|-----------|------|
| DIO (DODAG Information Object) | Descendant (root vers feuilles) | Annonce le DODAG, transmet parametres et metriques |
| DIS (DODAG Information Solicitation) | Montant | Sollicite un DIO des voisins |
| DAO (Destination Advertisement Object) | Montant (feuilles vers root) | Annonce les routes descendantes vers les noeuds |
| DAO-ACK | Descendant | Acquittement d'un DAO |

**Fonctions objectif** :

La fonction objectif determine comment un noeud choisit son parent et calcule son rang :
- **OF0 (Objective Function 0)** : minimise le nombre de sauts
- **MRHOF (Minimum Rank with Hysteresis Objective Function)** : minimise l'ETX (Expected Transmission Count), prenant en compte la qualite des liens

**Modes de trafic supportes** :

- **Multipoint-to-point (MP2P)** : trafic des noeuds capteurs vers le root (collecte de donnees). C'est le mode natif de RPL, le DODAG fournit naturellement les routes vers le root.
- **Point-to-multipoint (P2MP)** : trafic du root vers les noeuds (commandes, mises a jour). Utilise les routes descendantes construites via les DAO.
- **Point-to-point (P2P)** : communication directe entre deux noeuds dans le reseau. Le trafic remonte vers un ancetre commun dans le DODAG puis redescend.

<h3 class="section-title">8. Protocoles MAC economes en energie</h3>

La couche MAC est determinante pour la consommation energetique des dispositifs LP-WPAN. Plusieurs protocoles ont ete concus pour optimiser cette consommation :

**Sources de gaspillage energetique** :
- **Idle listening** : ecouter le canal alors qu'il n'y a pas de donnees (principale source de consommation)
- **Collisions** : retransmissions necessaires apres collision
- **Overhearing** : recevoir des paquets destines a d'autres noeuds
- **Overhead de controle** : messages de synchronisation, beacons

**Approches principales** :

- **Duty cycling** : alterner entre periodes actives et inactives pour reduire l'idle listening
- **Preamble sampling** : emettre un long preambule avant les donnees, le recepteur echantillonne periodiquement le canal
- **TDMA** : allocation de creneaux temporels pour eviter collisions

**Protocoles representatifs** :

- **IEEE 802.15.4 MAC** : mode beacon avec superframe (periodes actives/inactives, GTS)
- **ContikiMAC** : protocole duty-cycling utilise dans Contiki OS, base sur l'echantillonnage periodique du canal
- **TSCH (Time-Slotted Channel Hopping)** : extension de IEEE 802.15.4e combinant TDMA et saut de frequence pour ameliorer fiabilite et consommation

<h3 class="section-title">9. Protocoles applicatifs pour l'IoT contraint</h3>

**Connectivite IPv6 de bout en bout et MQTT** :

Nous avons etabli une connectivite IPv6 de bout en bout avec un serveur applicatif et mis en place MQTT pour la distribution de donnees. Cela impliquait la configuration du broker MQTT et l'utilisation d'outils comme `mosquitto_sub` et `mosquitto_pub` pour distribuer les donnees entre les producteurs et les consommateurs de topics.

**CoAP (Constrained Application Protocol)** :

CoAP est un protocole applicatif concu pour les dispositifs contraints (RFC 7252) :
- **Base** : UDP (pas TCP, trop lourd pour les dispositifs contraints)
- **Modele** : REST (GET, PUT, POST, DELETE) comme HTTP mais beaucoup plus leger
- **En-tete** : seulement 4 octets (vs dizaines d'octets pour HTTP)
- **Observation** : mecanisme de souscription aux ressources (notification automatique lors de changements)
- **Decouverte** : mecanisme de decouverte de ressources standardise (/.well-known/core)
- **Securite** : DTLS pour le chiffrement

**MQTT-SN (MQTT for Sensor Networks)** :

MQTT-SN est une adaptation de MQTT pour les reseaux de capteurs :
- **Transport** : UDP au lieu de TCP
- **Topic ID** : identifiants numeriques courts au lieu de chaines de caracteres
- **Gateway** : passerelle MQTT-SN / MQTT pour la communication avec le broker
- **QoS** : trois niveaux de qualite de service (0, 1, 2)
- **Publish/Subscribe** : modele de communication asynchrone adapte aux capteurs

<h3 class="section-title">10. Architecture reseau pour dispositifs contraints</h3>

L'architecture reseau pour les dispositifs IoT contraints suit un modele hierarchique :

```
Internet / Cloud
       |
  Border Router (6LBR)
  - Routeur de bordure 6LoWPAN
  - Traduction IPv6 <-> 6LoWPAN
  - Point d'acces au reseau IP
       |
  Reseau 6LoWPAN (maille)
  - Routeurs 6LoWPAN (6LR)
  - Relaient les trames dans le reseau maille
  - Participent au routage RPL
       |
  Noeuds terminaux (6LN)
  - Capteurs / actionneurs
  - Dispositifs a ressources limitees
  - Communiquent via 6LoWPAN
```

**Classification des dispositifs contraints (RFC 7228)** :

| Classe | RAM | Flash | Designation |
|--------|-----|-------|-------------|
| Classe 0 | < 10 KB | < 100 KB | Tres contraint (pas d'IP possible) |
| Classe 1 | ~10 KB | ~100 KB | Contraint (6LoWPAN/CoAP possible) |
| Classe 2 | ~50 KB | ~250 KB | Modere (pile IP complete possible) |

**Passerelle de bordure (6LBR)** :

Le Border Router est un element critique de l'architecture. Il assure :
- La traduction entre le monde IPv6 standard et le reseau 6LoWPAN
- La compression/decompression des en-tetes
- Le routage RPL (racine du DODAG)
- La gestion des contextes de compression d'adresses
- L'interface avec le reseau IP global

---

## PART D : ANALYSE ET REFLEXION

<h3 class="section-title">Competences acquises</h3>

**Comprehension de la pile protocolaire LP-WPAN** :
Maitrise de l'ensemble de la pile protocolaire, de la couche physique IEEE 802.15.4 aux protocoles applicatifs CoAP et MQTT-SN, en passant par la couche d'adaptation 6LoWPAN et le routage RPL.

**Analyse de trames reseau** :
Capacite a capturer et analyser des trames 6LoWPAN avec Wireshark, comprenant les mecanismes de compression d'en-tetes IPHC et la fragmentation.

**Conception d'architectures IoT** :
Aptitude a concevoir des architectures reseau adaptees aux contraintes des dispositifs IoT : energie, memoire, bande passante.

**Comparaison technologique** :
Capacite a comparer et selectionner les technologies sans fil adaptees a un cas d'usage donne (WPAN vs LPWAN, ZigBee vs Thread vs BLE).

<h3 class="section-title">Connaissances et competences mobilisees</h3>

- Comprendre les fondamentaux des LP-WPAN et de leur pile protocolaire TCP/IP adaptee
- Analyser les avantages et inconvenients de l'utilisation de protocoles standards bases sur IP dans les reseaux contraints
- Integrer IPv6 dans des cas d'usage a faible puissance grace a 6LoWPAN
- Comprendre la norme IEEE 802.15.4 et ses applications dans des protocoles comme ZigBee et Thread
- Maitriser le protocole de routage RPL pour les reseaux a pertes
- Configurer des reseaux IPv6 de bout en bout avec des protocoles applicatifs comme MQTT et CoAP

<h3 class="section-title">Auto-evaluation</h3>

J'ai trouve le cours LP-WPAN comme une introduction precieuse aux reseaux sans fil a faible puissance. J'ai particulierement apprecie travailler avec IPv6 et 6LoWPAN. Il reste des domaines ou j'ai encore des incertitudes et ou je dois approfondir mes connaissances, mais avec le temps et la pratique, je suis confiant dans ma maitrise de ces concepts.

Les travaux pratiques etaient bien guides par l'enseignant, ce qui m'a permis de mieux comprendre car le sujet etait assez complexe au depart, mais il a reussi a transmettre les competences du cours efficacement.

La partie la plus enrichissante a ete l'analyse des trames 6LoWPAN avec Wireshark : voir concretement comment les en-tetes IPv6 sont comprimes de 40 octets a quelques octets seulement est tres revelateur de l'ingenierie derriere ces protocoles.

<h3 class="section-title">Mon avis</h3>

C'etait un nouveau concept que j'ai apprecie travailler. Cela m'a offert une perspective nouvelle sur les possibilites des reseaux et m'a permis d'explorer des solutions innovantes dans les reseaux sans fil a faible puissance. Les experiences pratiques etaient interessantes car elles demontraient les applications concretes des technologies LP-WPAN.

Le panorama des technologies (LoRa, Sigfox, NB-IoT, BLE, Thread) m'a donne une vision globale des solutions disponibles pour l'IoT, ce qui est essentiel pour un ingenieur devant choisir la technologie adaptee a chaque projet.

La comprehension de l'architecture 6LoWPAN et du routage RPL est particulierement pertinente pour les projets IoT professionnels, ou la connectivite IP de bout en bout est de plus en plus recherchee.

---

## Documents de Cours

<style>
    .pdf-container {
        margin: 40px 0;
        padding: 20px;
        background: #f9f9f9;
        border-radius: 8px;
    }
    .pdf-viewer {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
    }
    .pdf-item {
        flex: 1;
        min-width: 400px;
        background: white;
        padding: 15px;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .pdf-item h4 {
        color: #2a7ae2;
        margin-top: 0;
    }
</style>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Chapitre 0 : Wireless Network Survey for IoT</h4>
      <p>Panorama des technologies sans fil pour l'IoT : classification, comparaison des protocoles, criteres de selection.</p>
      <embed src="/cours-pdf/S9/Wireless/2024.Ch0.WirelessNetsurvey4IoT.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/Wireless/2024.Ch0.WirelessNetsurvey4IoT.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>Chapitre 2 : 6LoWPAN - Network Architecture</h4>
      <p>Architecture 6LoWPAN : compression d'en-tetes, fragmentation, adressage mesh, integration IPv6.</p>
      <embed src="/cours-pdf/S9/Wireless/2024.Ch2.6LowPAN-NetworkArchitecture.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/Wireless/2024.Ch2.6LowPAN-NetworkArchitecture.pdf" target="_blank">Telecharger</a></p>
    </div>
  </div>
</div>

---

## Rapports et Projets

<div style="text-align: center;">
    <h3>Rapport de TP : LP-WPAN IPv6</h3>
</div>

<div style="display: flex; justify-content: center;">
    <embed src="/file/reports/S9/IPV6_Report.pdf" width="100%" height="800px" type="application/pdf">
</div>

<p style="text-align: center;">
    <a href="/file/reports/S9/IPV6_Report.pdf" target="_blank">Ouvrir le rapport complet</a>
</p>

<p style="text-align: center;">
    <a href="/img/BE_WPAN/Lab_Subject_wpan.pdf" target="_blank">Ouvrir le sujet de TP</a>
</p>

---

*Cours suivi en 2024-2025 a l'INSA Toulouse, Departement Genie Electrique et Informatique.*

<div class="back-nav">
    <a href="./my-courses-2024-2025.html">← Retour aux Cours 2024-2025</a>
</div>

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

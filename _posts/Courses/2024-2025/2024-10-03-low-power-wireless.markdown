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

<div class="back-nav">
    <a href="./my-courses-2024-2025.html" data-i18n-html="back-courses-2024-2025">&larr; Retour aux Cours 2024-2025</a>
</div>

<div class="lang-fr">

<p><strong>Cours connexes</strong> :</p>
<ul>
<li><a href="./wireless-sensors.html">Wireless Sensor Networks - S9</a> - Protocoles MAC pour WSN, ZigBee</li>
<li><a href="./emerging-network.html">Emerging Network Technologies - S9</a> - SDN et architectures reseau</li>
<li><a href="./middleware-iot.html">Middleware for IoT - S9</a> - Protocoles applicatifs IoT (MQTT, CoAP)</li>
<li><a href="./energy-connected-object.html">Energy for Connected Objects - S9</a> - Gestion energetique des objets connectes</li>
</ul>

<hr>

<h1>Low Power Wireless / WPAN IPv6 - Semestre 9</h1>

<p><strong>Annee academique</strong> : 2024-2025<br>
<strong>Semestre</strong> : S9<br>
<strong>Categorie</strong> : Reseaux sans fil et IoT</p>

<hr>

<h2>PART A : PRESENTATION GENERALE</h2>

<h3 class="section-title">Vue d'ensemble</h3>

<p>Le cours "Low Power Wireless / WPAN IPv6" offre une exploration approfondie des principes et des applications des reseaux sans fil personnels a faible consommation (LP-WPAN). L'objectif principal est de comprendre comment integrer IPv6 dans des reseaux contraints, en utilisant des mecanismes d'adaptation tels que 6LoWPAN, afin de permettre a des dispositifs a ressources limitees de communiquer sur Internet.</p>

<p>Ce cours couvre l'ensemble de la pile protocolaire adaptee aux objets connectes : de la couche physique IEEE 802.15.4 jusqu'aux protocoles applicatifs comme CoAP et MQTT-SN, en passant par la couche d'adaptation 6LoWPAN, le protocole de routage RPL, et les mecanismes de compression d'en-tetes IPv6.</p>

<p><strong>Objectifs pedagogiques</strong> :</p>
<ul>
<li>Comprendre le panorama des technologies sans fil pour l'IoT (IEEE 802.15.4, BLE, LoRa, Sigfox, NB-IoT)</li>
<li>Maitriser l'architecture 6LoWPAN et ses mecanismes de compression d'en-tetes</li>
<li>Configurer et analyser des reseaux IPv6 sur des dispositifs contraints</li>
<li>Comprendre le protocole de routage RPL pour les reseaux a faible puissance et a pertes (LLN)</li>
<li>Mettre en oeuvre des protocoles applicatifs adaptes (CoAP, MQTT-SN)</li>
<li>Analyser les compromis entre consommation energetique, portee et debit dans les LP-WPAN</li>
</ul>

<h3 class="section-title">Position dans le cursus</h3>

<p>Ce module s'appuie sur les bases acquises precedemment :</p>
<ul>
<li><strong>Reseau (S5)</strong> : modele OSI, Ethernet, IP de base, TCP/UDP</li>
<li><strong>Interconnexion Reseau (S8)</strong> : routage IP, protocoles de transport, IPv6</li>
<li><strong>Wireless Sensor Networks (S9)</strong> : protocoles MAC pour WSN, IEEE 802.15.4, ZigBee</li>
</ul>

<p>Il prepare a :</p>
<ul>
<li><strong>Projets IoT</strong> : deploiement de reseaux de capteurs communiquant en IPv6</li>
<li><strong>Middleware for IoT</strong> : integration de protocoles applicatifs sur reseaux contraints</li>
<li><strong>Carriere professionnelle</strong> : architecte IoT, ingenieur systemes embarques connectes</li>
</ul>

<hr>

<h2>PART B : EXPERIENCE ET CONTEXTE</h2>

<h3 class="section-title">Organisation et ressources</h3>

<p>Le module combinait cours magistraux et travaux pratiques sur des plateformes reelles :</p>

<p><strong>Cours magistraux</strong> :</p>
<ul>
<li>Panorama des technologies sans fil pour l'IoT (classification, comparaison)</li>
<li>Architecture protocolaire pour les reseaux LP-WPAN</li>
<li>Norme IEEE 802.15.4 : couches PHY et MAC</li>
<li>6LoWPAN : adaptation d'IPv6 pour les reseaux contraints</li>
<li>Protocole de routage RPL (Routing Protocol for Low-Power and Lossy Networks)</li>
<li>Technologies LPWAN : LoRa/LoRaWAN, Sigfox, NB-IoT</li>
<li>Protocoles applicatifs : CoAP, MQTT-SN</li>
</ul>

<p><strong>Travaux pratiques</strong> :</p>
<ul>
<li><strong>TP1</strong> : Auto-configuration d'adresses IPv6 link-local et globales</li>
<li><strong>TP2</strong> : Connectivite IPv6 de bout en bout avec serveur applicatif MQTT</li>
<li><strong>TP3</strong> : Compression d'en-tetes 6LoWPAN (analyse avec Wireshark)</li>
<li><strong>TP4</strong> : Routage RPL sur topologie multi-noeuds</li>
</ul>

<p><strong>Outils utilises</strong> :</p>
<ul>
<li><strong>Wireshark</strong> : capture et analyse de trafic 6LoWPAN/IPv6</li>
<li><strong>tcpdump</strong> : capture de paquets en ligne de commande</li>
<li><strong>Contiki-NG / RIOT OS</strong> : systemes d'exploitation pour dispositifs contraints</li>
<li><strong>Mosquitto</strong> : broker MQTT pour distribution de donnees</li>
<li><strong>ifconfig / ip</strong> : configuration d'interfaces reseau IPv6</li>
</ul>

<h3 class="section-title">Environnement et contexte</h3>

<p>Durant ce cours, j'ai travaille sur les aspects theoriques et pratiques des reseaux LP-WPAN. La partie initiale du cours couvrait les concepts fondamentaux des reseaux et des telecommunications, comme les interferences et les reseaux brouilles. Nous avons ensuite approfondi la pile protocolaire TCP/IP adaptee aux LP-WPAN, en utilisant la norme IEEE 802.15.4 pour les couches MAC et physique. Cette norme est couramment utilisee dans des protocoles comme ZigBee. Nous avons egalement explore l'utilisation d'IPv6 avec une couche intermediaire, 6LoWPAN, pour reduire la taille des paquets.</p>

<h3 class="section-title">Ma fonction</h3>

<p>Dans ce cours, j'etais responsable de :</p>
<ul>
<li>Comprendre les principes et l'architecture de 6LoWPAN</li>
<li>Explorer les differents protocoles et leurs applications dans les reseaux sans fil a faible puissance</li>
<li>Conduire des experiences pour tester l'efficacite et la scalabilite des differentes solutions LP-WPAN</li>
<li>Analyser les trames 6LoWPAN avec Wireshark pour comprendre les mecanismes de compression</li>
<li>Configurer le routage RPL et observer le comportement du reseau</li>
</ul>

<hr>

<h2>PART C : ASPECTS TECHNIQUES</h2>

<h3 class="section-title">1. Panorama des technologies sans fil pour l'IoT</h3>

<p>Le cours commence par un panorama complet des technologies sans fil disponibles pour l'IoT. L'objectif est de comprendre les criteres de choix d'une technologie selon les contraintes de l'application : portee, debit, consommation energetique, cout, et topologie de reseau.</p>

<p><strong>Classification par portee et debit</strong> :</p>

<table>
<tr><th>Technologie</th><th>Portee</th><th>Debit</th><th>Consommation</th><th>Usage typique</th></tr>
<tr><td>IEEE 802.15.4 / ZigBee</td><td>10-100 m</td><td>250 kbps</td><td>Tres faible</td><td>Domotique, capteurs</td></tr>
<tr><td>BLE (Bluetooth Low Energy)</td><td>10-50 m</td><td>1-2 Mbps</td><td>Tres faible</td><td>Wearables, beacons</td></tr>
<tr><td>Thread</td><td>10-30 m</td><td>250 kbps</td><td>Tres faible</td><td>Smart home</td></tr>
<tr><td>LoRa / LoRaWAN</td><td>2-15 km</td><td>0.3-50 kbps</td><td>Tres faible</td><td>Agriculture, smart city</td></tr>
<tr><td>Sigfox</td><td>10-50 km</td><td>100-600 bps</td><td>Ultra faible</td><td>Compteurs, tracking</td></tr>
<tr><td>NB-IoT</td><td>1-10 km</td><td>200 kbps</td><td>Faible</td><td>Compteurs, industriel</td></tr>
<tr><td>Wi-Fi (802.11ah)</td><td>100-1000 m</td><td>150 kbps-8 Mbps</td><td>Moyenne</td><td>IoT domestique</td></tr>
<tr><td>Z-Wave</td><td>30-100 m</td><td>100 kbps</td><td>Tres faible</td><td>Domotique</td></tr>
</table>

<p><strong>Distinction WPAN vs LPWAN</strong> :</p>

<p>Les reseaux <strong>WPAN</strong> (Wireless Personal Area Network) sont des reseaux a courte portee, comme IEEE 802.15.4 et BLE, adaptes aux applications necessitant des communications frequentes a faible distance. Les reseaux <strong>LPWAN</strong> (Low Power Wide Area Network) comme LoRa, Sigfox et NB-IoT sont conçus pour des communications longue portee avec un debit tres faible, adaptes aux applications de telemetrie et de suivi.</p>

<p><strong>Criteres de selection</strong> :</p>

<p>Le choix d'une technologie repose sur plusieurs facteurs :</p>
<ul>
<li><strong>Autonomie energetique</strong> : duree de vie souhaitee sur batterie (mois, annees)</li>
<li><strong>Portee necessaire</strong> : interieur, exterieur, urbain, rural</li>
<li><strong>Debit requis</strong> : donnees periodiques legeres vs streaming continu</li>
<li><strong>Latence</strong> : temps reel vs best-effort</li>
<li><strong>Densite de noeuds</strong> : nombre de dispositifs par zone</li>
<li><strong>Cout</strong> : licence, infrastructure, dispositifs</li>
<li><strong>Topologie</strong> : etoile, maille, arbre</li>
</ul>

<h3 class="section-title">2. IEEE 802.15.4 : la norme fondamentale des LP-WPAN</h3>

<p>La norme IEEE 802.15.4 definit les couches physique (PHY) et controle d'acces au medium (MAC) pour les reseaux LP-WPAN. C'est la base sur laquelle reposent de nombreux protocoles comme ZigBee, Thread et 6LoWPAN.</p>

<p><strong>Couche physique (PHY)</strong> :</p>

<ul>
<li><strong>Bandes de frequences</strong> :
  <ul>
  <li>2.4 GHz (ISM mondiale) : 16 canaux, 250 kbps, modulation O-QPSK</li>
  <li>868 MHz (Europe) : 1 canal, 20 kbps, modulation BPSK</li>
  <li>915 MHz (Amerique) : 10 canaux, 40 kbps, modulation BPSK</li>
  </ul>
</li>
<li><strong>Modulation</strong> : Direct Sequence Spread Spectrum (DSSS) avec O-QPSK ou BPSK</li>
<li><strong>Puissance d'emission</strong> : typiquement -3 dBm a 10 dBm</li>
<li><strong>Sensibilite du recepteur</strong> : -85 dBm (2.4 GHz), -92 dBm (868/915 MHz)</li>
<li><strong>Taille maximale de trame</strong> : 127 octets (incluant en-tete MAC)</li>
</ul>

<p><strong>Couche MAC</strong> :</p>

<ul>
<li><strong>Acces au canal</strong> : CSMA-CA (Carrier Sense Multiple Access with Collision Avoidance)</li>
<li><strong>Modes de fonctionnement</strong> :
  <ul>
  <li><strong>Mode beacon</strong> : le coordinateur envoie des beacons periodiques pour synchroniser les noeuds ; utilise la superframe avec periodes actives et inactives</li>
  <li><strong>Mode non-beacon</strong> : acces asynchrone au canal, adapte aux topologies en etoile simples</li>
  </ul>
</li>
<li><strong>Types de trames</strong> : donnees, acquittement (ACK), commande MAC, beacon</li>
<li><strong>Adressage</strong> : adresses courtes (16 bits) ou etendues (64 bits IEEE EUI-64)</li>
<li><strong>GTS (Guaranteed Time Slots)</strong> : allocation de creneaux temporels garantis dans la superframe pour les applications temps reel</li>
</ul>

<p><strong>Types de dispositifs</strong> :</p>

<table>
<tr><th>Type</th><th>Role</th><th>Capacites</th></tr>
<tr><td>FFD (Full Function Device)</td><td>Coordinateur PAN, routeur</td><td>Toutes fonctions MAC, peut relayer</td></tr>
<tr><td>RFD (Reduced Function Device)</td><td>Noeud terminal</td><td>Fonctions limitees, ne peut pas relayer</td></tr>
</table>

<p><strong>Topologies supportees</strong> :</p>

<ul>
<li><strong>Etoile</strong> : tous les noeuds communiquent avec un coordinateur central</li>
<li><strong>Pair-a-pair (mesh)</strong> : les noeuds FFD peuvent communiquer entre eux directement</li>
<li><strong>Arbre de clusters</strong> : hierarchie de coordinateurs et sous-coordinateurs</li>
</ul>

<h3 class="section-title">3. IPv6 pour l'IoT : fondamentaux</h3>

<p>IPv6 est le protocole de choix pour les reseaux IoT en raison de son espace d'adressage quasi illimite (2^128 adresses), de ses capacites d'auto-configuration, et de sa connectivite de bout en bout. Cependant, l'en-tete IPv6 standard (40 octets minimum) est trop volumineux pour les trames IEEE 802.15.4 limitees a 127 octets.</p>

<p><strong>Auto-configuration des adresses link-local</strong> :</p>

<div style="text-align: center; display: flex; justify-content: center; gap: 20px;">
    <img src="/img/BE_Low_Power/auto_conf.png" style="width: 70%;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Auto-configuration d'adresses IPv6 link-local</p>
</div>
<br>

<p>Nous avons execute la commande <code>ifconfig eth0 up</code> pour activer l'interface reseau <code>eth0</code>. Ensuite, nous avons utilise <code>ip -6 addr show dev eth0</code> pour afficher les adresses IPv6 assignees a l'interface. La sortie montrait une adresse au format <code>inet6 fe80::527c:6fff:fe56:e8b0</code>.</p>

<p>Cette adresse est une adresse IPv6 link-local, automatiquement configuree sur toutes les interfaces IPv6. Les adresses link-local utilisent le prefixe <code>fe80::/10</code> et la partie restante de l'adresse est derivee de l'adresse MAC de l'interface en utilisant le format Modified EUI-64.</p>

<p><strong>Processus de derivation EUI-64</strong> :</p>
<ol>
<li>Prendre l'adresse MAC 48 bits (ex: <code>50:7C:6F:56:E8:B0</code>)</li>
<li>Inserer <code>FF:FE</code> au milieu : <code>50:7C:6F:FF:FE:56:E8:B0</code></li>
<li>Inverser le bit U/L (7eme bit du premier octet) : <code>52:7C:6F:FF:FE:56:E8:B0</code></li>
<li>Resultat : <code>fe80::527c:6fff:fe56:e8b0</code></li>
</ol>

<p><strong>Auto-configuration des adresses unicast globales</strong> :</p>

<div style="text-align: center; display: flex; justify-content: center; gap: 20px;">
    <img src="/img/BE_Low_Power/dump.png" style="width:80%;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Capture de paquets IPv6 Router Advertisement</p>
</div>
<br>

<p>Nous avons explore le processus d'auto-configuration des adresses unicast globales IPv6 en utilisant les Router Advertisements (RA). Le routeur envoie periodiquement des messages ICMPv6 Router Advertisement contenant le prefixe reseau. Les noeuds terminaux derivent leur adresse globale en combinant ce prefixe avec leur identifiant d'interface (EUI-64 ou adresse aleatoire).</p>

<p><strong>Messages ICMPv6 impliques</strong> :</p>
<ul>
<li><strong>Router Solicitation (RS)</strong> : envoye par un noeud pour solliciter un RA du routeur local</li>
<li><strong>Router Advertisement (RA)</strong> : envoye par le routeur avec le prefixe reseau et les options de configuration</li>
<li><strong>Neighbor Solicitation (NS)</strong> : utilise pour la detection d'adresse dupliquee (DAD) et la resolution d'adresse</li>
<li><strong>Neighbor Advertisement (NA)</strong> : reponse a un NS</li>
</ul>

<h3 class="section-title">4. 6LoWPAN : adaptation d'IPv6 aux reseaux contraints</h3>

<p>6LoWPAN (IPv6 over Low-Power Wireless Personal Area Networks) est la couche d'adaptation cle qui permet l'utilisation d'IPv6 sur des reseaux IEEE 802.15.4. Il resout le probleme fondamental de l'incompatibilite entre la taille de l'en-tete IPv6 (40 octets minimum) et la taille maximale de la trame IEEE 802.15.4 (127 octets, dont seulement environ 80-100 octets utiles apres en-tete MAC).</p>

<p><strong>Fonctions principales de 6LoWPAN</strong> :</p>

<ul>
<li><strong>Compression d'en-tetes</strong> : reduction de l'en-tete IPv6 de 40 octets a aussi peu que 2-4 octets</li>
<li><strong>Fragmentation et reassemblage</strong> : decoupe des paquets IPv6 trop grands pour la MTU IEEE 802.15.4</li>
<li><strong>Adressage mesh</strong> : acheminement au niveau couche 2 dans un reseau maille</li>
<li><strong>Support du multicast</strong> : traduction des adresses multicast IPv6</li>
</ul>

<p><strong>Architecture de la pile protocolaire 6LoWPAN</strong> :</p>

<pre><code>+-----------------------------------+
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
+-----------------------------------+</code></pre>

<p><strong>Compression d'en-tetes IPHC (IP Header Compression)</strong> :</p>

<div style="text-align: center; display: flex; justify-content: center; gap: 20px;">
    <img src="/img/BE_Low_Power/header.png" style="width: 70%;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Compression d'en-tetes IPHC 6LoWPAN</p>
</div>
<br>

<p>Le mecanisme IPHC permet de compresser l'en-tete IPv6 en exploitant les informations deja disponibles dans le contexte de communication ou dans l'en-tete MAC IEEE 802.15.4 :</p>

<table>
<tr><th>Champ IPv6</th><th>Taille originale</th><th>Methode de compression</th><th>Taille compressee</th></tr>
<tr><td>Version</td><td>4 bits</td><td>Toujours IPv6, elidee</td><td>0</td></tr>
<tr><td>Traffic Class</td><td>8 bits</td><td>Souvent 0, elidee</td><td>0-8 bits</td></tr>
<tr><td>Flow Label</td><td>20 bits</td><td>Souvent 0, elidee</td><td>0-20 bits</td></tr>
<tr><td>Payload Length</td><td>16 bits</td><td>Deduite de la trame MAC</td><td>0</td></tr>
<tr><td>Next Header</td><td>8 bits</td><td>Compressee via NHC</td><td>0-8 bits</td></tr>
<tr><td>Hop Limit</td><td>8 bits</td><td>Valeurs communes (1, 64, 255)</td><td>0-8 bits</td></tr>
<tr><td>Adresse source</td><td>128 bits</td><td>Derivee de l'adresse MAC</td><td>0-128 bits</td></tr>
<tr><td>Adresse destination</td><td>128 bits</td><td>Derivee de l'adresse MAC</td><td>0-128 bits</td></tr>
</table>

<p><strong>Modes de compression des adresses</strong> :</p>

<ul>
<li><strong>Stateless</strong> : l'adresse est derivee de l'adresse MAC (EUI-64) dans l'en-tete IEEE 802.15.4</li>
<li><strong>Stateful (context-based)</strong> : le prefixe est connu via un contexte partage (identifie par un Context Identifier)</li>
<li><strong>Multicast</strong> : compression specifique des adresses multicast IPv6</li>
</ul>

<div style="text-align: center; display: flex; justify-content: center; gap: 20px;">
    <img src="/img/BE_Low_Power/compression.png" style="width: 70%;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Analyse Wireshark de la compression 6LoWPAN</p>
</div>
<br>

<p>Nous avons utilise Wireshark pour capturer et analyser des paquets ICMPv6 encapsules dans des trames 6LoWPAN. En examinant la section ICMPv6, nous pouvions voir l'en-tete IPHC (IP Header Compression), qui fournit les informations sur les champs comprimes de l'en-tete IPv6. Cette analyse nous a permis de comprendre comment 6LoWPAN reduit l'overhead des en-tetes IPv6 pour les rendre compatibles avec les reseaux a faible puissance et a pertes.</p>

<p><strong>Fragmentation 6LoWPAN</strong> :</p>

<p>Lorsqu'un paquet IPv6 depasse la MTU de la couche IEEE 802.15.4, 6LoWPAN le fragmente en plusieurs trames :</p>
<ul>
<li><strong>En-tete de fragmentation</strong> : contient la taille du datagramme original, un tag d'identification, et l'offset du fragment</li>
<li><strong>Premier fragment</strong> : contient l'en-tete compresse IPHC et le debut du payload</li>
<li><strong>Fragments suivants</strong> : contiennent le tag, l'offset et la suite du payload</li>
<li>Le reassemblage est effectue au noeud destinataire</li>
</ul>

<p><strong>Adressage Mesh</strong> :</p>

<p>L'en-tete mesh de 6LoWPAN permet l'acheminement des trames au niveau couche 2 dans un reseau maille. Il contient les adresses source et destination IEEE 802.15.4 originales, permettant aux noeuds intermediaires de relayer les trames sans necessite de routage IP.</p>

<h3 class="section-title">5. Technologies LPWAN : LoRa, Sigfox, NB-IoT</h3>

<p>En complement des technologies WPAN a courte portee, le cours aborde les technologies LPWAN (Low Power Wide Area Network) pour les communications longue portee.</p>

<p><strong>LoRa / LoRaWAN</strong> :</p>

<p>LoRa (Long Range) est une technologie de modulation radio proprietaire (Semtech) utilisant la technique CSS (Chirp Spread Spectrum) :</p>
<ul>
<li><strong>Bande de frequences</strong> : 868 MHz (Europe), 915 MHz (Amerique), 433 MHz (Asie)</li>
<li><strong>Portee</strong> : 2-5 km (urbain), 10-15 km (rural)</li>
<li><strong>Debit</strong> : 0.3 a 50 kbps selon le spreading factor (SF7 a SF12)</li>
<li><strong>Spreading Factor</strong> : plus le SF est eleve, plus la portee augmente mais le debit diminue</li>
</ul>

<p>LoRaWAN est l'architecture reseau au-dessus de LoRa :</p>
<ul>
<li><strong>Topologie en etoile</strong> : les dispositifs communiquent avec des gateways</li>
<li><strong>Classes de dispositifs</strong> :
  <ul>
  <li><strong>Classe A</strong> : emission initiee par le dispositif, deux fenetres de reception apres emission (plus econome)</li>
  <li><strong>Classe B</strong> : fenetres de reception programmees via beacons (latence reduite)</li>
  <li><strong>Classe C</strong> : reception continue sauf pendant emission (latence minimale, consommation maximale)</li>
  </ul>
</li>
<li><strong>Securite</strong> : chiffrement AES-128 au niveau reseau et application</li>
</ul>

<p><strong>Sigfox</strong> :</p>

<ul>
<li><strong>Modulation</strong> : Ultra Narrow Band (UNB), bande passante de 100 Hz par message</li>
<li><strong>Portee</strong> : 10-50 km</li>
<li><strong>Debit</strong> : 100 bps (uplink), 600 bps (downlink)</li>
<li><strong>Limitation</strong> : 140 messages/jour (uplink), 4 messages/jour (downlink)</li>
<li><strong>Modele economique</strong> : abonnement operateur, pas d'infrastructure propre</li>
</ul>

<p><strong>NB-IoT (Narrowband IoT)</strong> :</p>

<ul>
<li><strong>Standard</strong> : 3GPP Release 13 (LTE Category NB1)</li>
<li><strong>Bande de frequences</strong> : bandes LTE licensiees (180 kHz)</li>
<li><strong>Debit</strong> : jusqu'a 200 kbps (downlink), 20 kbps (uplink)</li>
<li><strong>Portee</strong> : 1-10 km</li>
<li><strong>Avantage</strong> : utilise l'infrastructure cellulaire existante</li>
</ul>

<h3 class="section-title">6. ZigBee et Thread : piles protocolaires sur IEEE 802.15.4</h3>

<p><strong>ZigBee</strong> :</p>

<p>ZigBee est une pile protocolaire complete construite sur IEEE 802.15.4 :</p>
<ul>
<li><strong>Couche reseau</strong> : routage par arbre ou maille, decouverte de routes AODV</li>
<li><strong>Couche application</strong> : profils standardises (ZigBee Home Automation, ZigBee Light Link)</li>
<li><strong>Securite</strong> : chiffrement AES-128, gestion de cles via Trust Center</li>
<li><strong>Topologies</strong> : etoile, arbre, maille</li>
<li><strong>Limitations</strong> : pile proprietaire (ZigBee Alliance), pas d'interoperabilite IP native</li>
</ul>

<p><strong>Thread</strong> :</p>

<p>Thread est une pile protocolaire moderne basee sur 6LoWPAN :</p>
<ul>
<li><strong>Base</strong> : IEEE 802.15.4 + 6LoWPAN + IPv6</li>
<li><strong>Routage</strong> : protocole MLE (Mesh Link Establishment) pour la gestion du reseau maille</li>
<li><strong>Avantage</strong> : interoperabilite IP native, compatible avec les ecosystemes Internet</li>
<li><strong>Securite</strong> : DTLS (Datagram Transport Layer Security)</li>
<li><strong>Usage</strong> : smart home (supporte par Apple HomeKit, Google Nest)</li>
</ul>

<p><strong>BLE (Bluetooth Low Energy)</strong> :</p>

<ul>
<li><strong>Standard</strong> : Bluetooth 4.0+ (BLE)</li>
<li><strong>Portee</strong> : 10-50 m</li>
<li><strong>Debit</strong> : 1-2 Mbps</li>
<li><strong>IPv6 sur BLE</strong> : 6LoWPAN peut etre utilise sur BLE via la specification IPSP (Internet Protocol Support Profile)</li>
<li><strong>Mesh</strong> : Bluetooth Mesh (depuis Bluetooth 5.0) pour les reseaux mailles</li>
</ul>

<h3 class="section-title">7. RPL : protocole de routage pour LLN</h3>

<p>RPL (Routing Protocol for Low-Power and Lossy Networks, RFC 6550) est le protocole de routage standardise par l'IETF pour les reseaux 6LoWPAN. Il est specialement concu pour les reseaux a faible puissance et a pertes (LLN - Low-Power and Lossy Networks).</p>

<div style="text-align: center; display: flex; justify-content: center; gap: 20px;">
    <img src="/img/BE_Low_Power/node.png" style="width: 90%;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Topologie RPL - DODAG avec noeuds et routes</p>
</div>
<br>

<p><strong>Principe de fonctionnement</strong> :</p>

<p>RPL construit un DODAG (Destination-Oriented Directed Acyclic Graph) : un graphe acyclique dirige oriente vers un noeud racine (root) qui sert de passerelle vers Internet.</p>

<p><strong>Construction du DODAG</strong> :</p>
<ol>
<li>Le noeud racine initie la construction en emettant des messages DIO (DODAG Information Object)</li>
<li>Chaque noeud recevant un DIO calcule son rang (distance au root) selon une fonction objectif (OF)</li>
<li>Le noeud selectionne un parent prefere parmi les voisins offrant le meilleur rang</li>
<li>Le processus se propage de proche en proche jusqu'aux feuilles</li>
</ol>

<p><strong>Messages RPL</strong> :</p>

<table>
<tr><th>Message</th><th>Direction</th><th>Role</th></tr>
<tr><td>DIO (DODAG Information Object)</td><td>Descendant (root vers feuilles)</td><td>Annonce le DODAG, transmet parametres et metriques</td></tr>
<tr><td>DIS (DODAG Information Solicitation)</td><td>Montant</td><td>Sollicite un DIO des voisins</td></tr>
<tr><td>DAO (Destination Advertisement Object)</td><td>Montant (feuilles vers root)</td><td>Annonce les routes descendantes vers les noeuds</td></tr>
<tr><td>DAO-ACK</td><td>Descendant</td><td>Acquittement d'un DAO</td></tr>
</table>

<p><strong>Fonctions objectif</strong> :</p>

<p>La fonction objectif determine comment un noeud choisit son parent et calcule son rang :</p>
<ul>
<li><strong>OF0 (Objective Function 0)</strong> : minimise le nombre de sauts</li>
<li><strong>MRHOF (Minimum Rank with Hysteresis Objective Function)</strong> : minimise l'ETX (Expected Transmission Count), prenant en compte la qualite des liens</li>
</ul>

<p><strong>Modes de trafic supportes</strong> :</p>

<ul>
<li><strong>Multipoint-to-point (MP2P)</strong> : trafic des noeuds capteurs vers le root (collecte de donnees). C'est le mode natif de RPL, le DODAG fournit naturellement les routes vers le root.</li>
<li><strong>Point-to-multipoint (P2MP)</strong> : trafic du root vers les noeuds (commandes, mises a jour). Utilise les routes descendantes construites via les DAO.</li>
<li><strong>Point-to-point (P2P)</strong> : communication directe entre deux noeuds dans le reseau. Le trafic remonte vers un ancetre commun dans le DODAG puis redescend.</li>
</ul>

<h3 class="section-title">8. Protocoles MAC economes en energie</h3>

<p>La couche MAC est determinante pour la consommation energetique des dispositifs LP-WPAN. Plusieurs protocoles ont ete concus pour optimiser cette consommation :</p>

<p><strong>Sources de gaspillage energetique</strong> :</p>
<ul>
<li><strong>Idle listening</strong> : ecouter le canal alors qu'il n'y a pas de donnees (principale source de consommation)</li>
<li><strong>Collisions</strong> : retransmissions necessaires apres collision</li>
<li><strong>Overhearing</strong> : recevoir des paquets destines a d'autres noeuds</li>
<li><strong>Overhead de controle</strong> : messages de synchronisation, beacons</li>
</ul>

<p><strong>Approches principales</strong> :</p>

<ul>
<li><strong>Duty cycling</strong> : alterner entre periodes actives et inactives pour reduire l'idle listening</li>
<li><strong>Preamble sampling</strong> : emettre un long preambule avant les donnees, le recepteur echantillonne periodiquement le canal</li>
<li><strong>TDMA</strong> : allocation de creneaux temporels pour eviter collisions</li>
</ul>

<p><strong>Protocoles representatifs</strong> :</p>

<ul>
<li><strong>IEEE 802.15.4 MAC</strong> : mode beacon avec superframe (periodes actives/inactives, GTS)</li>
<li><strong>ContikiMAC</strong> : protocole duty-cycling utilise dans Contiki OS, base sur l'echantillonnage periodique du canal</li>
<li><strong>TSCH (Time-Slotted Channel Hopping)</strong> : extension de IEEE 802.15.4e combinant TDMA et saut de frequence pour ameliorer fiabilite et consommation</li>
</ul>

<h3 class="section-title">9. Protocoles applicatifs pour l'IoT contraint</h3>

<p><strong>Connectivite IPv6 de bout en bout et MQTT</strong> :</p>

<p>Nous avons etabli une connectivite IPv6 de bout en bout avec un serveur applicatif et mis en place MQTT pour la distribution de donnees. Cela impliquait la configuration du broker MQTT et l'utilisation d'outils comme <code>mosquitto_sub</code> et <code>mosquitto_pub</code> pour distribuer les donnees entre les producteurs et les consommateurs de topics.</p>

<p><strong>CoAP (Constrained Application Protocol)</strong> :</p>

<p>CoAP est un protocole applicatif concu pour les dispositifs contraints (RFC 7252) :</p>
<ul>
<li><strong>Base</strong> : UDP (pas TCP, trop lourd pour les dispositifs contraints)</li>
<li><strong>Modele</strong> : REST (GET, PUT, POST, DELETE) comme HTTP mais beaucoup plus leger</li>
<li><strong>En-tete</strong> : seulement 4 octets (vs dizaines d'octets pour HTTP)</li>
<li><strong>Observation</strong> : mecanisme de souscription aux ressources (notification automatique lors de changements)</li>
<li><strong>Decouverte</strong> : mecanisme de decouverte de ressources standardise (/.well-known/core)</li>
<li><strong>Securite</strong> : DTLS pour le chiffrement</li>
</ul>

<p><strong>MQTT-SN (MQTT for Sensor Networks)</strong> :</p>

<p>MQTT-SN est une adaptation de MQTT pour les reseaux de capteurs :</p>
<ul>
<li><strong>Transport</strong> : UDP au lieu de TCP</li>
<li><strong>Topic ID</strong> : identifiants numeriques courts au lieu de chaines de caracteres</li>
<li><strong>Gateway</strong> : passerelle MQTT-SN / MQTT pour la communication avec le broker</li>
<li><strong>QoS</strong> : trois niveaux de qualite de service (0, 1, 2)</li>
<li><strong>Publish/Subscribe</strong> : modele de communication asynchrone adapte aux capteurs</li>
</ul>

<h3 class="section-title">10. Architecture reseau pour dispositifs contraints</h3>

<p>L'architecture reseau pour les dispositifs IoT contraints suit un modele hierarchique :</p>

<pre><code>Internet / Cloud
       |
  Border Router (6LBR)
  - Routeur de bordure 6LoWPAN
  - Traduction IPv6 &lt;-&gt; 6LoWPAN
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
  - Communiquent via 6LoWPAN</code></pre>

<p><strong>Classification des dispositifs contraints (RFC 7228)</strong> :</p>

<table>
<tr><th>Classe</th><th>RAM</th><th>Flash</th><th>Designation</th></tr>
<tr><td>Classe 0</td><td>&lt; 10 KB</td><td>&lt; 100 KB</td><td>Tres contraint (pas d'IP possible)</td></tr>
<tr><td>Classe 1</td><td>~10 KB</td><td>~100 KB</td><td>Contraint (6LoWPAN/CoAP possible)</td></tr>
<tr><td>Classe 2</td><td>~50 KB</td><td>~250 KB</td><td>Modere (pile IP complete possible)</td></tr>
</table>

<p><strong>Passerelle de bordure (6LBR)</strong> :</p>

<p>Le Border Router est un element critique de l'architecture. Il assure :</p>
<ul>
<li>La traduction entre le monde IPv6 standard et le reseau 6LoWPAN</li>
<li>La compression/decompression des en-tetes</li>
<li>Le routage RPL (racine du DODAG)</li>
<li>La gestion des contextes de compression d'adresses</li>
<li>L'interface avec le reseau IP global</li>
</ul>

<hr>

<h2>PART D : ANALYSE ET REFLEXION</h2>

<h3 class="section-title">Competences acquises</h3>

<p><strong>Comprehension de la pile protocolaire LP-WPAN</strong> :<br>
Maitrise de l'ensemble de la pile protocolaire, de la couche physique IEEE 802.15.4 aux protocoles applicatifs CoAP et MQTT-SN, en passant par la couche d'adaptation 6LoWPAN et le routage RPL.</p>

<p><strong>Analyse de trames reseau</strong> :<br>
Capacite a capturer et analyser des trames 6LoWPAN avec Wireshark, comprenant les mecanismes de compression d'en-tetes IPHC et la fragmentation.</p>

<p><strong>Conception d'architectures IoT</strong> :<br>
Aptitude a concevoir des architectures reseau adaptees aux contraintes des dispositifs IoT : energie, memoire, bande passante.</p>

<p><strong>Comparaison technologique</strong> :<br>
Capacite a comparer et selectionner les technologies sans fil adaptees a un cas d'usage donne (WPAN vs LPWAN, ZigBee vs Thread vs BLE).</p>

<h3 class="section-title">Connaissances et competences mobilisees</h3>

<ul>
<li>Comprendre les fondamentaux des LP-WPAN et de leur pile protocolaire TCP/IP adaptee</li>
<li>Analyser les avantages et inconvenients de l'utilisation de protocoles standards bases sur IP dans les reseaux contraints</li>
<li>Integrer IPv6 dans des cas d'usage a faible puissance grace a 6LoWPAN</li>
<li>Comprendre la norme IEEE 802.15.4 et ses applications dans des protocoles comme ZigBee et Thread</li>
<li>Maitriser le protocole de routage RPL pour les reseaux a pertes</li>
<li>Configurer des reseaux IPv6 de bout en bout avec des protocoles applicatifs comme MQTT et CoAP</li>
</ul>

<h3 class="section-title">Auto-evaluation</h3>

<p>J'ai trouve le cours LP-WPAN comme une introduction precieuse aux reseaux sans fil a faible puissance. J'ai particulierement apprecie travailler avec IPv6 et 6LoWPAN. Il reste des domaines ou j'ai encore des incertitudes et ou je dois approfondir mes connaissances, mais avec le temps et la pratique, je suis confiant dans ma maitrise de ces concepts.</p>

<p>Les travaux pratiques etaient bien guides par l'enseignant, ce qui m'a permis de mieux comprendre car le sujet etait assez complexe au depart, mais il a reussi a transmettre les competences du cours efficacement.</p>

<p>La partie la plus enrichissante a ete l'analyse des trames 6LoWPAN avec Wireshark : voir concretement comment les en-tetes IPv6 sont comprimes de 40 octets a quelques octets seulement est tres revelateur de l'ingenierie derriere ces protocoles.</p>

<h3 class="section-title">Mon avis</h3>

<p>C'etait un nouveau concept que j'ai apprecie travailler. Cela m'a offert une perspective nouvelle sur les possibilites des reseaux et m'a permis d'explorer des solutions innovantes dans les reseaux sans fil a faible puissance. Les experiences pratiques etaient interessantes car elles demontraient les applications concretes des technologies LP-WPAN.</p>

<p>Le panorama des technologies (LoRa, Sigfox, NB-IoT, BLE, Thread) m'a donne une vision globale des solutions disponibles pour l'IoT, ce qui est essentiel pour un ingenieur devant choisir la technologie adaptee a chaque projet.</p>

<p>La comprehension de l'architecture 6LoWPAN et du routage RPL est particulierement pertinente pour les projets IoT professionnels, ou la connectivite IP de bout en bout est de plus en plus recherchee.</p>

<hr>

<h2>Documents de Cours</h2>

</div>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">Chapitre 0 : Wireless Network Survey for IoT</span>
        <span class="lang-en">Chapter 0: Wireless Network Survey for IoT</span>
      </h4>
      <p>
        <span class="lang-fr">Panorama des technologies sans fil pour l'IoT : classification, comparaison des protocoles, criteres de selection.</span>
        <span class="lang-en">Overview of wireless technologies for IoT: classification, protocol comparison, selection criteria.</span>
      </p>
      <embed src="/cours-pdf/S9/Wireless/2024Ch0WirelessNetsurvey4IoT.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/Wireless/2024Ch0WirelessNetsurvey4IoT.pdf" target="_blank">
        <span class="lang-fr">Telecharger</span>
        <span class="lang-en">Download</span>
      </a></p>
    </div>
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">Chapitre 2 : 6LoWPAN - Network Architecture</span>
        <span class="lang-en">Chapter 2: 6LoWPAN - Network Architecture</span>
      </h4>
      <p>
        <span class="lang-fr">Architecture 6LoWPAN : compression d'en-tetes, fragmentation, adressage mesh, integration IPv6.</span>
        <span class="lang-en">6LoWPAN architecture: header compression, fragmentation, mesh addressing, IPv6 integration.</span>
      </p>
      <embed src="/cours-pdf/S9/Wireless/2024Ch26LowPANNetworkArchitecture.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/Wireless/2024Ch26LowPANNetworkArchitecture.pdf" target="_blank">
        <span class="lang-fr">Telecharger</span>
        <span class="lang-en">Download</span>
      </a></p>
    </div>
  </div>
</div>

<div class="lang-fr">

<hr>

<h2>Rapports et Projets</h2>

</div>

<div style="text-align: center;">
    <h3>
        <span class="lang-fr">Rapport de TP : LP-WPAN IPv6</span>
        <span class="lang-en">Lab Report: LP-WPAN IPv6</span>
    </h3>
</div>

<div style="display: flex; justify-content: center;">
    <embed src="/file/reports/S9/IPV6_Report.pdf" width="100%" height="800px" type="application/pdf">
</div>

<p style="text-align: center;">
    <a href="/file/reports/S9/IPV6_Report.pdf" target="_blank">
        <span class="lang-fr">Ouvrir le rapport complet</span>
        <span class="lang-en">Open the full report</span>
    </a>
</p>

<p style="text-align: center;">
    <a href="/img/BE_WPAN/Lab_Subject_wpan.pdf" target="_blank">
        <span class="lang-fr">Ouvrir le sujet de TP</span>
        <span class="lang-en">Open the lab subject</span>
    </a>
</p>

<div class="lang-fr">
<hr>
<p><em>Cours suivi en 2024-2025 a l'INSA Toulouse, Departement Genie Electrique et Informatique.</em></p>
</div>

<div class="lang-en">

<p><strong>Related courses</strong>:</p>
<ul>
<li><a href="./wireless-sensors.html">Wireless Sensor Networks - S9</a> - MAC protocols for WSN, ZigBee</li>
<li><a href="./emerging-network.html">Emerging Network Technologies - S9</a> - SDN and network architectures</li>
<li><a href="./middleware-iot.html">Middleware for IoT - S9</a> - IoT application protocols (MQTT, CoAP)</li>
<li><a href="./energy-connected-object.html">Energy for Connected Objects - S9</a> - Energy management for connected objects</li>
</ul>

<hr>

<h1>Low Power Wireless / WPAN IPv6 - Semester 9</h1>

<p><strong>Academic year</strong>: 2024-2025<br>
<strong>Semester</strong>: S9<br>
<strong>Category</strong>: Wireless networks and IoT</p>

<hr>

<h2>PART A: GENERAL PRESENTATION</h2>

<h3 class="section-title">Overview</h3>

<p>The "Low Power Wireless / WPAN IPv6" course provides an in-depth exploration of the principles and applications of Low-Power Wireless Personal Area Networks (LP-WPAN). The main objective is to understand how to integrate IPv6 into constrained networks, using adaptation mechanisms such as 6LoWPAN, to enable resource-limited devices to communicate over the Internet.</p>

<p>This course covers the entire protocol stack adapted to connected objects: from the IEEE 802.15.4 physical layer to application protocols such as CoAP and MQTT-SN, including the 6LoWPAN adaptation layer, the RPL routing protocol, and IPv6 header compression mechanisms.</p>

<p><strong>Learning objectives</strong>:</p>
<ul>
<li>Understand the landscape of wireless technologies for IoT (IEEE 802.15.4, BLE, LoRa, Sigfox, NB-IoT)</li>
<li>Master the 6LoWPAN architecture and its header compression mechanisms</li>
<li>Configure and analyze IPv6 networks on constrained devices</li>
<li>Understand the RPL routing protocol for Low-Power and Lossy Networks (LLN)</li>
<li>Implement adapted application protocols (CoAP, MQTT-SN)</li>
<li>Analyze the trade-offs between energy consumption, range and throughput in LP-WPANs</li>
</ul>

<h3 class="section-title">Position in the curriculum</h3>

<p>This module builds on previously acquired foundations:</p>
<ul>
<li><strong>Networking (S5)</strong>: OSI model, Ethernet, basic IP, TCP/UDP</li>
<li><strong>Network Interconnection (S8)</strong>: IP routing, transport protocols, IPv6</li>
<li><strong>Wireless Sensor Networks (S9)</strong>: MAC protocols for WSN, IEEE 802.15.4, ZigBee</li>
</ul>

<p>It prepares for:</p>
<ul>
<li><strong>IoT Projects</strong>: deployment of sensor networks communicating via IPv6</li>
<li><strong>Middleware for IoT</strong>: integration of application protocols on constrained networks</li>
<li><strong>Professional career</strong>: IoT architect, connected embedded systems engineer</li>
</ul>

<hr>

<h2>PART B: EXPERIENCE AND CONTEXT</h2>

<h3 class="section-title">Organization and resources</h3>

<p>The module combined lectures and hands-on lab sessions on real platforms:</p>

<p><strong>Lectures</strong>:</p>
<ul>
<li>Overview of wireless technologies for IoT (classification, comparison)</li>
<li>Protocol architecture for LP-WPAN networks</li>
<li>IEEE 802.15.4 standard: PHY and MAC layers</li>
<li>6LoWPAN: IPv6 adaptation for constrained networks</li>
<li>RPL routing protocol (Routing Protocol for Low-Power and Lossy Networks)</li>
<li>LPWAN technologies: LoRa/LoRaWAN, Sigfox, NB-IoT</li>
<li>Application protocols: CoAP, MQTT-SN</li>
</ul>

<p><strong>Lab sessions</strong>:</p>
<ul>
<li><strong>Lab 1</strong>: Auto-configuration of IPv6 link-local and global addresses</li>
<li><strong>Lab 2</strong>: End-to-end IPv6 connectivity with MQTT application server</li>
<li><strong>Lab 3</strong>: 6LoWPAN header compression (analysis with Wireshark)</li>
<li><strong>Lab 4</strong>: RPL routing on multi-node topology</li>
</ul>

<p><strong>Tools used</strong>:</p>
<ul>
<li><strong>Wireshark</strong>: 6LoWPAN/IPv6 traffic capture and analysis</li>
<li><strong>tcpdump</strong>: command-line packet capture</li>
<li><strong>Contiki-NG / RIOT OS</strong>: operating systems for constrained devices</li>
<li><strong>Mosquitto</strong>: MQTT broker for data distribution</li>
<li><strong>ifconfig / ip</strong>: IPv6 network interface configuration</li>
</ul>

<h3 class="section-title">Environment and context</h3>

<p>During this course, I worked on the theoretical and practical aspects of LP-WPAN networks. The initial part of the course covered fundamental networking and telecommunications concepts, such as interference and jammed networks. We then delved deeper into the TCP/IP protocol stack adapted for LP-WPANs, using the IEEE 802.15.4 standard for the MAC and physical layers. This standard is commonly used in protocols such as ZigBee. We also explored the use of IPv6 with an intermediate layer, 6LoWPAN, to reduce packet size.</p>

<h3 class="section-title">My role</h3>

<p>In this course, I was responsible for:</p>
<ul>
<li>Understanding the principles and architecture of 6LoWPAN</li>
<li>Exploring the different protocols and their applications in low-power wireless networks</li>
<li>Conducting experiments to test the efficiency and scalability of different LP-WPAN solutions</li>
<li>Analyzing 6LoWPAN frames with Wireshark to understand compression mechanisms</li>
<li>Configuring RPL routing and observing network behavior</li>
</ul>

<hr>

<h2>PART C: TECHNICAL ASPECTS</h2>

<h3 class="section-title">1. Overview of wireless technologies for IoT</h3>

<p>The course begins with a comprehensive overview of wireless technologies available for IoT. The objective is to understand the criteria for choosing a technology based on the application's constraints: range, throughput, energy consumption, cost, and network topology.</p>

<p><strong>Classification by range and throughput</strong>:</p>

<table>
<tr><th>Technology</th><th>Range</th><th>Throughput</th><th>Consumption</th><th>Typical use</th></tr>
<tr><td>IEEE 802.15.4 / ZigBee</td><td>10-100 m</td><td>250 kbps</td><td>Very low</td><td>Home automation, sensors</td></tr>
<tr><td>BLE (Bluetooth Low Energy)</td><td>10-50 m</td><td>1-2 Mbps</td><td>Very low</td><td>Wearables, beacons</td></tr>
<tr><td>Thread</td><td>10-30 m</td><td>250 kbps</td><td>Very low</td><td>Smart home</td></tr>
<tr><td>LoRa / LoRaWAN</td><td>2-15 km</td><td>0.3-50 kbps</td><td>Very low</td><td>Agriculture, smart city</td></tr>
<tr><td>Sigfox</td><td>10-50 km</td><td>100-600 bps</td><td>Ultra low</td><td>Meters, tracking</td></tr>
<tr><td>NB-IoT</td><td>1-10 km</td><td>200 kbps</td><td>Low</td><td>Meters, industrial</td></tr>
<tr><td>Wi-Fi (802.11ah)</td><td>100-1000 m</td><td>150 kbps-8 Mbps</td><td>Medium</td><td>Home IoT</td></tr>
<tr><td>Z-Wave</td><td>30-100 m</td><td>100 kbps</td><td>Very low</td><td>Home automation</td></tr>
</table>

<p><strong>WPAN vs LPWAN distinction</strong>:</p>

<p><strong>WPAN</strong> (Wireless Personal Area Network) networks are short-range networks, such as IEEE 802.15.4 and BLE, suited for applications requiring frequent communications over short distances. <strong>LPWAN</strong> (Low Power Wide Area Network) networks such as LoRa, Sigfox and NB-IoT are designed for long-range communications with very low throughput, suited for telemetry and tracking applications.</p>

<p><strong>Selection criteria</strong>:</p>

<p>The choice of technology depends on several factors:</p>
<ul>
<li><strong>Energy autonomy</strong>: desired battery lifetime (months, years)</li>
<li><strong>Required range</strong>: indoor, outdoor, urban, rural</li>
<li><strong>Required throughput</strong>: light periodic data vs continuous streaming</li>
<li><strong>Latency</strong>: real-time vs best-effort</li>
<li><strong>Node density</strong>: number of devices per area</li>
<li><strong>Cost</strong>: license, infrastructure, devices</li>
<li><strong>Topology</strong>: star, mesh, tree</li>
</ul>

<h3 class="section-title">2. IEEE 802.15.4: the fundamental LP-WPAN standard</h3>

<p>The IEEE 802.15.4 standard defines the physical (PHY) and medium access control (MAC) layers for LP-WPAN networks. It is the foundation upon which many protocols such as ZigBee, Thread and 6LoWPAN are built.</p>

<p><strong>Physical layer (PHY)</strong>:</p>

<ul>
<li><strong>Frequency bands</strong>:
  <ul>
  <li>2.4 GHz (worldwide ISM): 16 channels, 250 kbps, O-QPSK modulation</li>
  <li>868 MHz (Europe): 1 channel, 20 kbps, BPSK modulation</li>
  <li>915 MHz (Americas): 10 channels, 40 kbps, BPSK modulation</li>
  </ul>
</li>
<li><strong>Modulation</strong>: Direct Sequence Spread Spectrum (DSSS) with O-QPSK or BPSK</li>
<li><strong>Transmit power</strong>: typically -3 dBm to 10 dBm</li>
<li><strong>Receiver sensitivity</strong>: -85 dBm (2.4 GHz), -92 dBm (868/915 MHz)</li>
<li><strong>Maximum frame size</strong>: 127 bytes (including MAC header)</li>
</ul>

<p><strong>MAC layer</strong>:</p>

<ul>
<li><strong>Channel access</strong>: CSMA-CA (Carrier Sense Multiple Access with Collision Avoidance)</li>
<li><strong>Operating modes</strong>:
  <ul>
  <li><strong>Beacon mode</strong>: the coordinator sends periodic beacons to synchronize nodes; uses the superframe with active and inactive periods</li>
  <li><strong>Non-beacon mode</strong>: asynchronous channel access, suited for simple star topologies</li>
  </ul>
</li>
<li><strong>Frame types</strong>: data, acknowledgment (ACK), MAC command, beacon</li>
<li><strong>Addressing</strong>: short addresses (16 bits) or extended addresses (64-bit IEEE EUI-64)</li>
<li><strong>GTS (Guaranteed Time Slots)</strong>: allocation of guaranteed time slots in the superframe for real-time applications</li>
</ul>

<p><strong>Device types</strong>:</p>

<table>
<tr><th>Type</th><th>Role</th><th>Capabilities</th></tr>
<tr><td>FFD (Full Function Device)</td><td>PAN coordinator, router</td><td>All MAC functions, can relay</td></tr>
<tr><td>RFD (Reduced Function Device)</td><td>End node</td><td>Limited functions, cannot relay</td></tr>
</table>

<p><strong>Supported topologies</strong>:</p>

<ul>
<li><strong>Star</strong>: all nodes communicate with a central coordinator</li>
<li><strong>Peer-to-peer (mesh)</strong>: FFD nodes can communicate directly with each other</li>
<li><strong>Cluster tree</strong>: hierarchy of coordinators and sub-coordinators</li>
</ul>

<h3 class="section-title">3. IPv6 for IoT: fundamentals</h3>

<p>IPv6 is the protocol of choice for IoT networks due to its virtually unlimited address space (2^128 addresses), its auto-configuration capabilities, and its end-to-end connectivity. However, the standard IPv6 header (40 bytes minimum) is too large for IEEE 802.15.4 frames limited to 127 bytes.</p>

<p><strong>Link-local address auto-configuration</strong>:</p>

<div style="text-align: center; display: flex; justify-content: center; gap: 20px;">
    <img src="/img/BE_Low_Power/auto_conf.png" style="width: 70%;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: IPv6 link-local address auto-configuration</p>
</div>
<br>

<p>We executed the command <code>ifconfig eth0 up</code> to activate the <code>eth0</code> network interface. Then, we used <code>ip -6 addr show dev eth0</code> to display the IPv6 addresses assigned to the interface. The output showed an address in the format <code>inet6 fe80::527c:6fff:fe56:e8b0</code>.</p>

<p>This address is an IPv6 link-local address, automatically configured on all IPv6 interfaces. Link-local addresses use the <code>fe80::/10</code> prefix and the remaining part of the address is derived from the interface's MAC address using the Modified EUI-64 format.</p>

<p><strong>EUI-64 derivation process</strong>:</p>
<ol>
<li>Take the 48-bit MAC address (e.g.: <code>50:7C:6F:56:E8:B0</code>)</li>
<li>Insert <code>FF:FE</code> in the middle: <code>50:7C:6F:FF:FE:56:E8:B0</code></li>
<li>Invert the U/L bit (7th bit of the first byte): <code>52:7C:6F:FF:FE:56:E8:B0</code></li>
<li>Result: <code>fe80::527c:6fff:fe56:e8b0</code></li>
</ol>

<p><strong>Global unicast address auto-configuration</strong>:</p>

<div style="text-align: center; display: flex; justify-content: center; gap: 20px;">
    <img src="/img/BE_Low_Power/dump.png" style="width:80%;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: IPv6 Router Advertisement packet capture</p>
</div>
<br>

<p>We explored the IPv6 global unicast address auto-configuration process using Router Advertisements (RA). The router periodically sends ICMPv6 Router Advertisement messages containing the network prefix. End nodes derive their global address by combining this prefix with their interface identifier (EUI-64 or random address).</p>

<p><strong>ICMPv6 messages involved</strong>:</p>
<ul>
<li><strong>Router Solicitation (RS)</strong>: sent by a node to solicit an RA from the local router</li>
<li><strong>Router Advertisement (RA)</strong>: sent by the router with the network prefix and configuration options</li>
<li><strong>Neighbor Solicitation (NS)</strong>: used for Duplicate Address Detection (DAD) and address resolution</li>
<li><strong>Neighbor Advertisement (NA)</strong>: response to an NS</li>
</ul>

<h3 class="section-title">4. 6LoWPAN: adapting IPv6 to constrained networks</h3>

<p>6LoWPAN (IPv6 over Low-Power Wireless Personal Area Networks) is the key adaptation layer that enables the use of IPv6 on IEEE 802.15.4 networks. It solves the fundamental problem of incompatibility between the IPv6 header size (40 bytes minimum) and the maximum IEEE 802.15.4 frame size (127 bytes, of which only about 80-100 bytes are usable after the MAC header).</p>

<p><strong>Main 6LoWPAN functions</strong>:</p>

<ul>
<li><strong>Header compression</strong>: reduction of the IPv6 header from 40 bytes to as few as 2-4 bytes</li>
<li><strong>Fragmentation and reassembly</strong>: splitting IPv6 packets that are too large for the IEEE 802.15.4 MTU</li>
<li><strong>Mesh addressing</strong>: layer 2 forwarding in a mesh network</li>
<li><strong>Multicast support</strong>: translation of IPv6 multicast addresses</li>
</ul>

<p><strong>6LoWPAN protocol stack architecture</strong>:</p>

<pre><code>+-----------------------------------+
|  Application (CoAP, MQTT-SN)      |
+-----------------------------------+
|  Transport (UDP)                  |
+-----------------------------------+
|  Network (IPv6)                   |
+-----------------------------------+
|  Adaptation (6LoWPAN)             |
|  - Header compression (IPHC)     |
|  - Fragmentation                  |
|  - Mesh addressing                |
+-----------------------------------+
|  MAC (IEEE 802.15.4)              |
+-----------------------------------+
|  PHY (IEEE 802.15.4)              |
+-----------------------------------+</code></pre>

<p><strong>IPHC header compression (IP Header Compression)</strong>:</p>

<div style="text-align: center; display: flex; justify-content: center; gap: 20px;">
    <img src="/img/BE_Low_Power/header.png" style="width: 70%;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: 6LoWPAN IPHC header compression</p>
</div>
<br>

<p>The IPHC mechanism compresses the IPv6 header by exploiting information already available in the communication context or in the IEEE 802.15.4 MAC header:</p>

<table>
<tr><th>IPv6 field</th><th>Original size</th><th>Compression method</th><th>Compressed size</th></tr>
<tr><td>Version</td><td>4 bits</td><td>Always IPv6, elided</td><td>0</td></tr>
<tr><td>Traffic Class</td><td>8 bits</td><td>Often 0, elided</td><td>0-8 bits</td></tr>
<tr><td>Flow Label</td><td>20 bits</td><td>Often 0, elided</td><td>0-20 bits</td></tr>
<tr><td>Payload Length</td><td>16 bits</td><td>Inferred from MAC frame</td><td>0</td></tr>
<tr><td>Next Header</td><td>8 bits</td><td>Compressed via NHC</td><td>0-8 bits</td></tr>
<tr><td>Hop Limit</td><td>8 bits</td><td>Common values (1, 64, 255)</td><td>0-8 bits</td></tr>
<tr><td>Source address</td><td>128 bits</td><td>Derived from MAC address</td><td>0-128 bits</td></tr>
<tr><td>Destination address</td><td>128 bits</td><td>Derived from MAC address</td><td>0-128 bits</td></tr>
</table>

<p><strong>Address compression modes</strong>:</p>

<ul>
<li><strong>Stateless</strong>: the address is derived from the MAC address (EUI-64) in the IEEE 802.15.4 header</li>
<li><strong>Stateful (context-based)</strong>: the prefix is known via a shared context (identified by a Context Identifier)</li>
<li><strong>Multicast</strong>: specific compression of IPv6 multicast addresses</li>
</ul>

<div style="text-align: center; display: flex; justify-content: center; gap: 20px;">
    <img src="/img/BE_Low_Power/compression.png" style="width: 70%;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Wireshark analysis of 6LoWPAN compression</p>
</div>
<br>

<p>We used Wireshark to capture and analyze ICMPv6 packets encapsulated in 6LoWPAN frames. By examining the ICMPv6 section, we could see the IPHC (IP Header Compression) header, which provides information about the compressed fields of the IPv6 header. This analysis allowed us to understand how 6LoWPAN reduces IPv6 header overhead to make them compatible with low-power and lossy networks.</p>

<p><strong>6LoWPAN fragmentation</strong>:</p>

<p>When an IPv6 packet exceeds the IEEE 802.15.4 layer MTU, 6LoWPAN fragments it into multiple frames:</p>
<ul>
<li><strong>Fragmentation header</strong>: contains the original datagram size, an identification tag, and the fragment offset</li>
<li><strong>First fragment</strong>: contains the IPHC compressed header and the beginning of the payload</li>
<li><strong>Subsequent fragments</strong>: contain the tag, offset and the rest of the payload</li>
<li>Reassembly is performed at the destination node</li>
</ul>

<p><strong>Mesh addressing</strong>:</p>

<p>The 6LoWPAN mesh header enables layer 2 frame forwarding in a mesh network. It contains the original IEEE 802.15.4 source and destination addresses, allowing intermediate nodes to relay frames without the need for IP routing.</p>

<h3 class="section-title">5. LPWAN technologies: LoRa, Sigfox, NB-IoT</h3>

<p>In addition to short-range WPAN technologies, the course covers LPWAN (Low Power Wide Area Network) technologies for long-range communications.</p>

<p><strong>LoRa / LoRaWAN</strong>:</p>

<p>LoRa (Long Range) is a proprietary radio modulation technology (Semtech) using the CSS (Chirp Spread Spectrum) technique:</p>
<ul>
<li><strong>Frequency band</strong>: 868 MHz (Europe), 915 MHz (Americas), 433 MHz (Asia)</li>
<li><strong>Range</strong>: 2-5 km (urban), 10-15 km (rural)</li>
<li><strong>Throughput</strong>: 0.3 to 50 kbps depending on spreading factor (SF7 to SF12)</li>
<li><strong>Spreading Factor</strong>: the higher the SF, the greater the range but the lower the throughput</li>
</ul>

<p>LoRaWAN is the network architecture on top of LoRa:</p>
<ul>
<li><strong>Star topology</strong>: devices communicate with gateways</li>
<li><strong>Device classes</strong>:
  <ul>
  <li><strong>Class A</strong>: device-initiated transmission, two receive windows after transmission (most energy-efficient)</li>
  <li><strong>Class B</strong>: scheduled receive windows via beacons (reduced latency)</li>
  <li><strong>Class C</strong>: continuous reception except during transmission (minimal latency, maximum consumption)</li>
  </ul>
</li>
<li><strong>Security</strong>: AES-128 encryption at network and application level</li>
</ul>

<p><strong>Sigfox</strong>:</p>

<ul>
<li><strong>Modulation</strong>: Ultra Narrow Band (UNB), 100 Hz bandwidth per message</li>
<li><strong>Range</strong>: 10-50 km</li>
<li><strong>Throughput</strong>: 100 bps (uplink), 600 bps (downlink)</li>
<li><strong>Limitation</strong>: 140 messages/day (uplink), 4 messages/day (downlink)</li>
<li><strong>Business model</strong>: operator subscription, no proprietary infrastructure</li>
</ul>

<p><strong>NB-IoT (Narrowband IoT)</strong>:</p>

<ul>
<li><strong>Standard</strong>: 3GPP Release 13 (LTE Category NB1)</li>
<li><strong>Frequency band</strong>: licensed LTE bands (180 kHz)</li>
<li><strong>Throughput</strong>: up to 200 kbps (downlink), 20 kbps (uplink)</li>
<li><strong>Range</strong>: 1-10 km</li>
<li><strong>Advantage</strong>: uses existing cellular infrastructure</li>
</ul>

<h3 class="section-title">6. ZigBee and Thread: protocol stacks on IEEE 802.15.4</h3>

<p><strong>ZigBee</strong>:</p>

<p>ZigBee is a complete protocol stack built on IEEE 802.15.4:</p>
<ul>
<li><strong>Network layer</strong>: tree or mesh routing, AODV route discovery</li>
<li><strong>Application layer</strong>: standardized profiles (ZigBee Home Automation, ZigBee Light Link)</li>
<li><strong>Security</strong>: AES-128 encryption, key management via Trust Center</li>
<li><strong>Topologies</strong>: star, tree, mesh</li>
<li><strong>Limitations</strong>: proprietary stack (ZigBee Alliance), no native IP interoperability</li>
</ul>

<p><strong>Thread</strong>:</p>

<p>Thread is a modern protocol stack based on 6LoWPAN:</p>
<ul>
<li><strong>Foundation</strong>: IEEE 802.15.4 + 6LoWPAN + IPv6</li>
<li><strong>Routing</strong>: MLE protocol (Mesh Link Establishment) for mesh network management</li>
<li><strong>Advantage</strong>: native IP interoperability, compatible with Internet ecosystems</li>
<li><strong>Security</strong>: DTLS (Datagram Transport Layer Security)</li>
<li><strong>Usage</strong>: smart home (supported by Apple HomeKit, Google Nest)</li>
</ul>

<p><strong>BLE (Bluetooth Low Energy)</strong>:</p>

<ul>
<li><strong>Standard</strong>: Bluetooth 4.0+ (BLE)</li>
<li><strong>Range</strong>: 10-50 m</li>
<li><strong>Throughput</strong>: 1-2 Mbps</li>
<li><strong>IPv6 over BLE</strong>: 6LoWPAN can be used over BLE via the IPSP (Internet Protocol Support Profile) specification</li>
<li><strong>Mesh</strong>: Bluetooth Mesh (since Bluetooth 5.0) for mesh networks</li>
</ul>

<h3 class="section-title">7. RPL: routing protocol for LLN</h3>

<p>RPL (Routing Protocol for Low-Power and Lossy Networks, RFC 6550) is the routing protocol standardized by the IETF for 6LoWPAN networks. It is specially designed for Low-Power and Lossy Networks (LLN).</p>

<div style="text-align: center; display: flex; justify-content: center; gap: 20px;">
    <img src="/img/BE_Low_Power/node.png" style="width: 90%;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: RPL topology - DODAG with nodes and routes</p>
</div>
<br>

<p><strong>Operating principle</strong>:</p>

<p>RPL constructs a DODAG (Destination-Oriented Directed Acyclic Graph): a directed acyclic graph oriented toward a root node that serves as a gateway to the Internet.</p>

<p><strong>DODAG construction</strong>:</p>
<ol>
<li>The root node initiates the construction by emitting DIO (DODAG Information Object) messages</li>
<li>Each node receiving a DIO calculates its rank (distance to root) according to an objective function (OF)</li>
<li>The node selects a preferred parent among neighbors offering the best rank</li>
<li>The process propagates hop by hop to the leaves</li>
</ol>

<p><strong>RPL messages</strong>:</p>

<table>
<tr><th>Message</th><th>Direction</th><th>Role</th></tr>
<tr><td>DIO (DODAG Information Object)</td><td>Downward (root to leaves)</td><td>Announces the DODAG, transmits parameters and metrics</td></tr>
<tr><td>DIS (DODAG Information Solicitation)</td><td>Upward</td><td>Solicits a DIO from neighbors</td></tr>
<tr><td>DAO (Destination Advertisement Object)</td><td>Upward (leaves to root)</td><td>Announces downward routes to nodes</td></tr>
<tr><td>DAO-ACK</td><td>Downward</td><td>Acknowledgment of a DAO</td></tr>
</table>

<p><strong>Objective functions</strong>:</p>

<p>The objective function determines how a node chooses its parent and calculates its rank:</p>
<ul>
<li><strong>OF0 (Objective Function 0)</strong>: minimizes the number of hops</li>
<li><strong>MRHOF (Minimum Rank with Hysteresis Objective Function)</strong>: minimizes the ETX (Expected Transmission Count), taking link quality into account</li>
</ul>

<p><strong>Supported traffic modes</strong>:</p>

<ul>
<li><strong>Multipoint-to-point (MP2P)</strong>: traffic from sensor nodes to the root (data collection). This is RPL's native mode; the DODAG naturally provides routes to the root.</li>
<li><strong>Point-to-multipoint (P2MP)</strong>: traffic from the root to nodes (commands, updates). Uses downward routes built via DAOs.</li>
<li><strong>Point-to-point (P2P)</strong>: direct communication between two nodes in the network. Traffic goes up to a common ancestor in the DODAG then back down.</li>
</ul>

<h3 class="section-title">8. Energy-efficient MAC protocols</h3>

<p>The MAC layer is critical for the energy consumption of LP-WPAN devices. Several protocols have been designed to optimize this consumption:</p>

<p><strong>Sources of energy waste</strong>:</p>
<ul>
<li><strong>Idle listening</strong>: listening to the channel when there is no data (main source of consumption)</li>
<li><strong>Collisions</strong>: retransmissions required after collision</li>
<li><strong>Overhearing</strong>: receiving packets destined for other nodes</li>
<li><strong>Control overhead</strong>: synchronization messages, beacons</li>
</ul>

<p><strong>Main approaches</strong>:</p>

<ul>
<li><strong>Duty cycling</strong>: alternating between active and inactive periods to reduce idle listening</li>
<li><strong>Preamble sampling</strong>: emitting a long preamble before data, the receiver periodically samples the channel</li>
<li><strong>TDMA</strong>: time slot allocation to avoid collisions</li>
</ul>

<p><strong>Representative protocols</strong>:</p>

<ul>
<li><strong>IEEE 802.15.4 MAC</strong>: beacon mode with superframe (active/inactive periods, GTS)</li>
<li><strong>ContikiMAC</strong>: duty-cycling protocol used in Contiki OS, based on periodic channel sampling</li>
<li><strong>TSCH (Time-Slotted Channel Hopping)</strong>: IEEE 802.15.4e extension combining TDMA and frequency hopping to improve reliability and consumption</li>
</ul>

<h3 class="section-title">9. Application protocols for constrained IoT</h3>

<p><strong>End-to-end IPv6 connectivity and MQTT</strong>:</p>

<p>We established end-to-end IPv6 connectivity with an application server and set up MQTT for data distribution. This involved configuring the MQTT broker and using tools such as <code>mosquitto_sub</code> and <code>mosquitto_pub</code> to distribute data between topic producers and consumers.</p>

<p><strong>CoAP (Constrained Application Protocol)</strong>:</p>

<p>CoAP is an application protocol designed for constrained devices (RFC 7252):</p>
<ul>
<li><strong>Foundation</strong>: UDP (not TCP, too heavy for constrained devices)</li>
<li><strong>Model</strong>: REST (GET, PUT, POST, DELETE) like HTTP but much lighter</li>
<li><strong>Header</strong>: only 4 bytes (vs tens of bytes for HTTP)</li>
<li><strong>Observation</strong>: resource subscription mechanism (automatic notification on changes)</li>
<li><strong>Discovery</strong>: standardized resource discovery mechanism (/.well-known/core)</li>
<li><strong>Security</strong>: DTLS for encryption</li>
</ul>

<p><strong>MQTT-SN (MQTT for Sensor Networks)</strong>:</p>

<p>MQTT-SN is an adaptation of MQTT for sensor networks:</p>
<ul>
<li><strong>Transport</strong>: UDP instead of TCP</li>
<li><strong>Topic ID</strong>: short numerical identifiers instead of character strings</li>
<li><strong>Gateway</strong>: MQTT-SN / MQTT gateway for communication with the broker</li>
<li><strong>QoS</strong>: three quality of service levels (0, 1, 2)</li>
<li><strong>Publish/Subscribe</strong>: asynchronous communication model suited for sensors</li>
</ul>

<h3 class="section-title">10. Network architecture for constrained devices</h3>

<p>The network architecture for constrained IoT devices follows a hierarchical model:</p>

<pre><code>Internet / Cloud
       |
  Border Router (6LBR)
  - 6LoWPAN border router
  - IPv6 &lt;-&gt; 6LoWPAN translation
  - IP network access point
       |
  6LoWPAN Network (mesh)
  - 6LoWPAN Routers (6LR)
  - Relay frames in the mesh network
  - Participate in RPL routing
       |
  End Nodes (6LN)
  - Sensors / actuators
  - Resource-constrained devices
  - Communicate via 6LoWPAN</code></pre>

<p><strong>Constrained device classification (RFC 7228)</strong>:</p>

<table>
<tr><th>Class</th><th>RAM</th><th>Flash</th><th>Designation</th></tr>
<tr><td>Class 0</td><td>&lt; 10 KB</td><td>&lt; 100 KB</td><td>Very constrained (IP not possible)</td></tr>
<tr><td>Class 1</td><td>~10 KB</td><td>~100 KB</td><td>Constrained (6LoWPAN/CoAP possible)</td></tr>
<tr><td>Class 2</td><td>~50 KB</td><td>~250 KB</td><td>Moderate (full IP stack possible)</td></tr>
</table>

<p><strong>Border gateway (6LBR)</strong>:</p>

<p>The Border Router is a critical element of the architecture. It provides:</p>
<ul>
<li>Translation between the standard IPv6 world and the 6LoWPAN network</li>
<li>Header compression/decompression</li>
<li>RPL routing (DODAG root)</li>
<li>Management of address compression contexts</li>
<li>Interface with the global IP network</li>
</ul>

<hr>

<h2>PART D: ANALYSIS AND REFLECTION</h2>

<h3 class="section-title">Skills acquired</h3>

<p><strong>Understanding of the LP-WPAN protocol stack</strong>:<br>
Mastery of the entire protocol stack, from the IEEE 802.15.4 physical layer to CoAP and MQTT-SN application protocols, including the 6LoWPAN adaptation layer and RPL routing.</p>

<p><strong>Network frame analysis</strong>:<br>
Ability to capture and analyze 6LoWPAN frames with Wireshark, understanding IPHC header compression mechanisms and fragmentation.</p>

<p><strong>IoT architecture design</strong>:<br>
Ability to design network architectures adapted to IoT device constraints: energy, memory, bandwidth.</p>

<p><strong>Technology comparison</strong>:<br>
Ability to compare and select wireless technologies suited to a given use case (WPAN vs LPWAN, ZigBee vs Thread vs BLE).</p>

<h3 class="section-title">Knowledge and skills mobilized</h3>

<ul>
<li>Understanding the fundamentals of LP-WPANs and their adapted TCP/IP protocol stack</li>
<li>Analyzing the advantages and disadvantages of using standard IP-based protocols in constrained networks</li>
<li>Integrating IPv6 in low-power use cases through 6LoWPAN</li>
<li>Understanding the IEEE 802.15.4 standard and its applications in protocols such as ZigBee and Thread</li>
<li>Mastering the RPL routing protocol for lossy networks</li>
<li>Configuring end-to-end IPv6 networks with application protocols such as MQTT and CoAP</li>
</ul>

<h3 class="section-title">Self-assessment</h3>

<p>I found the LP-WPAN course to be a valuable introduction to low-power wireless networks. I particularly enjoyed working with IPv6 and 6LoWPAN. There are still areas where I have uncertainties and where I need to deepen my knowledge, but with time and practice, I am confident in my mastery of these concepts.</p>

<p>The lab sessions were well guided by the instructor, which helped me better understand because the subject was quite complex at first, but he succeeded in effectively conveying the course skills.</p>

<p>The most enriching part was the analysis of 6LoWPAN frames with Wireshark: concretely seeing how IPv6 headers are compressed from 40 bytes to just a few bytes is very revealing of the engineering behind these protocols.</p>

<h3 class="section-title">My opinion</h3>

<p>This was a new concept that I enjoyed working on. It gave me a new perspective on networking possibilities and allowed me to explore innovative solutions in low-power wireless networks. The hands-on experiments were interesting as they demonstrated the concrete applications of LP-WPAN technologies.</p>

<p>The overview of technologies (LoRa, Sigfox, NB-IoT, BLE, Thread) gave me a comprehensive view of the solutions available for IoT, which is essential for an engineer who must choose the right technology for each project.</p>

<p>Understanding the 6LoWPAN architecture and RPL routing is particularly relevant for professional IoT projects, where end-to-end IP connectivity is increasingly sought after.</p>

<hr>

<h2>Course Documents</h2>

<!-- PDF sections are shared above between lang-fr and lang-en -->

<hr>

<h2>Reports and Projects</h2>

<!-- Report/PDF sections are shared above between lang-fr and lang-en -->

<hr>

<p><em>Course taken in 2024-2025 at INSA Toulouse, Department of Electrical and Computer Engineering.</em></p>

</div>

<div class="back-nav">
    <a href="./my-courses-2024-2025.html" data-i18n-html="back-courses-2024-2025">&larr; Retour aux Cours 2024-2025</a>
</div>

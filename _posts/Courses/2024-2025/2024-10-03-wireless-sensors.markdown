---
layout: default
title:  "WSNL"
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
    <a href="./my-courses-2024-2025.html">&larr; Retour aux Cours 2024-2025</a>
</div>

# Wireless Sensors / WSNL - Semestre 9

**Annee academique** : 2024-2025
**Categorie** : Reseaux de capteurs sans fil, IoT et telecommunications
**Enseignants** : S. Abdellatif, D. Dragomirescu

---

## PART A : PRESENTATION GENERALE

<h3 class="section-title">Vue d'ensemble</h3>

Le cours "Wireless Sensor Networks and Localization" (WSNL) est un module central de la specialisation ISS (Innovative Smart Systems) en 5eme annee a l'INSA Toulouse. Ce cours explore en profondeur les principes fondamentaux des reseaux de capteurs sans fil (WSN), les protocoles de communication a faible consommation energetique, les techniques de modulation adaptees aux objets connectes, ainsi que les technologies LPWAN et les standards de communication comme ZigBee et Sigfox.

**Objectifs pedagogiques** :
- Comprendre l'architecture des reseaux de capteurs sans fil et leurs contraintes specifiques
- Analyser et evaluer les protocoles MAC dedies aux WSN (S-MAC, T-MAC, B-MAC, L-MAC, Z-MAC)
- Maitriser les techniques de modulation a faible puissance pour les communications IoT
- Etudier les piles protocolaires completes (ZigBee, Sigfox, LoRa)
- Comprendre les architectures M2M sur reseaux cellulaires 4G LTE et 5G
- Apprehender les principes du SDR (Software Defined Radio)
- Concevoir des solutions de routage energetiquement efficaces
- Developper une couche MAC en Python

<h3 class="section-title">Position dans le cursus</h3>

Ce module fait le lien entre plusieurs domaines :
- **Wireless Communication (S8)** : bases des communications sans fil
- **Interconnexion Reseau (S8)** : fondamentaux des protocoles reseaux
- **Energy for Connected Objects (S9)** : gestion energetique des noeuds capteurs
- **Middleware for IoT (S9)** : couches applicatives et integration IoT
- **Security for Connected Objects (S9)** : securisation des communications WSN
- **5G Technologies (S9)** : integration M2M dans les reseaux cellulaires

---

## PART B : EXPERIENCE ET CONTEXTE

<h3 class="section-title">Organisation et ressources</h3>

Le module combinait cours magistraux, travaux pratiques et projets de recherche :

**Cours magistraux** :
- Architecture des reseaux de capteurs sans fil (WSN)
- Protocoles MAC pour WSN : S-MAC, T-MAC, B-MAC, L-MAC, Z-MAC
- Techniques de modulation pour communications a faible puissance (DSSS, O-QPSK, BPSK, FSK)
- Pile protocolaire ZigBee (IEEE 802.15.4)
- Protocole Sigfox et technologies LPWAN
- Communications M2M sur 4G LTE et 5G
- Software Defined Radio (SDR) et GNU Radio
- Routage econome en energie dans les WSN

**Travaux pratiques** :
- **TP MAC** : Developpement d'une couche MAC en Python, gestion des paquets, acces au medium
- **TP PHY** : Introduction au SDR avec GNU Radio (couche physique)
- **TP WSN** : Mise en oeuvre d'un reseau de capteurs (Smart Subway)

**Projets et rapports** :
- Rapport d'analyse des protocoles MAC pour WSN
- Etude du protocole Sigfox et des technologies LPWAN
- Rapport sur le protocole ZigBee (WPAN pour WSN)
- Etude M2M sur 4G LTE et 5G
- Rapport TP WSN (Smart Subway)

**Outils utilises** :
- **Python** : implementation de la couche MAC
- **GNU Radio** : plateforme SDR pour la couche physique
- **IEEE 802.15.4** : standard de reference pour les WSN

<h3 class="section-title">Methodologie d'etude</h3>

**Phase 1 : Etude des protocoles existants** :
Analyse comparative des protocoles LoRa, ZigBee et Sigfox pour comprendre leurs specificites, avantages et cas d'usage.

**Phase 2 : Approfondissement des couches MAC** :
Etude detaillee de chaque protocole MAC (S-MAC, T-MAC, B-MAC, L-MAC, Z-MAC), comprenant les mecanismes de duty cycling, l'acces au medium et l'optimisation energetique.

**Phase 3 : Implementation pratique** :
Developpement d'une couche MAC en Python, permettant de comprendre concretement la gestion des trames, l'acces au canal et la coordination entre noeuds.

**Phase 4 : Etude des technologies LPWAN et cellulaires** :
Analyse des solutions Sigfox, LoRa et de l'integration M2M dans les reseaux 4G/5G.

<h3 class="section-title">Difficultes rencontrees</h3>

**Nombre de protocoles** :
La multiplicite des protocoles MAC, des standards et des technologies LPWAN rend l'assimilation complete difficile. Chaque protocole a ses propres mecanismes et compromis.

**Couche physique et SDR** :
Bien que le SDR ait ete aborde en cours, les sessions pratiques sur GNU Radio etaient limitees, ce qui a reduit l'experience pratique sur la couche physique.

**Compromis energetiques** :
Comprendre les differents compromis entre latence, debit, portee et consommation energetique pour chaque protocole necessite une analyse multi-criteres complexe.

---

## PART C : ASPECTS TECHNIQUES

Cette section explore en detail les aspects techniques des technologies WSN, en couvrant l'architecture des noeuds capteurs, les protocoles MAC, les techniques de modulation, les piles protocolaires ZigBee et Sigfox, le M2M cellulaire et le SDR.

<h3 class="section-title">1. Architecture des reseaux de capteurs sans fil (WSN)</h3>

Un reseau de capteurs sans fil (Wireless Sensor Network) est constitue d'un ensemble de noeuds capteurs autonomes, deployes pour surveiller des conditions physiques ou environnementales (temperature, pression, humidite, mouvement, etc.) et transmettre les donnees collectees a un noeud central (sink ou station de base).

**Architecture d'un noeud capteur** :

Un noeud capteur typique se compose de quatre sous-systemes :

| Sous-systeme | Composants | Role |
|--------------|------------|------|
| Capteur | Capteur(s) + ADC | Acquisition des donnees physiques |
| Traitement | Microcontroleur + memoire | Traitement local, protocoles, stockage |
| Communication | Emetteur-recepteur radio (transceiver) | Transmission/reception sans fil |
| Energie | Batterie + harvesting (optionnel) | Alimentation du noeud |

**Contraintes specifiques des WSN** :
- **Energie limitee** : les noeuds fonctionnent sur batterie, la consommation doit etre minimisee
- **Bande passante reduite** : debits faibles (250 kbps pour ZigBee, 100 bps pour Sigfox)
- **Capacite de calcul limitee** : microcontroleurs a faible puissance
- **Deploiement a grande echelle** : centaines ou milliers de noeuds
- **Environnements hostiles** : accessibilite limitee pour maintenance

**Topologies de reseau WSN** :
- **Etoile** : tous les noeuds communiquent directement avec le sink (simple, portee limitee)
- **Maille (mesh)** : communication multi-saut, resilience aux pannes
- **Arbre (cluster tree)** : hierarchique, avec noeuds coordinateurs et noeuds feuilles
- **Hybride** : combinaison des topologies precedentes

<h3 class="section-title">2. Protocoles MAC pour WSN</h3>

La couche MAC (Medium Access Control) est cruciale dans les WSN car elle gere l'acces au canal radio partage. L'objectif principal est de minimiser la consommation energetique tout en assurant une communication fiable.

**Sources de gaspillage energetique dans les WSN** :
- **Idle listening** : le transceiver reste allume en ecoute sans recevoir de donnees utiles
- **Collisions** : les retransmissions apres collision consomment de l'energie supplementaire
- **Overhearing** : reception de paquets destines a d'autres noeuds
- **Overhead des protocoles** : en-tetes et trames de controle

Les protocoles MAC pour WSN se classent en trois categories : contention-based, schedule-based et hybrides.

#### 2.1 Protocoles a contention (Contention-Based)

**S-MAC (Sensor-MAC)**

S-MAC est un protocole MAC a contention concu specifiquement pour les WSN. Il introduit le concept de **duty cycling** : les noeuds alternent entre periodes de sommeil (sleep) et periodes d'activite (listen/transmit) selon un planning synchronise.

Principes cles :
- **Planning synchronise** : les noeuds voisins se synchronisent pour avoir les memes periodes d'activite
- **Periodes de sommeil** : reduction drastique de l'idle listening
- **RTS/CTS** : mecanisme de reservation du canal pour eviter les collisions
- **Message passing** : fragmentation des longs messages pour transmission efficace

<img src="/img/BE_WSNL/S_MAC.png" alt="S-MAC : duty cycling synchronise avec periodes sleep/listen" style="width: 50%; display: block; margin: 0 auto;">
<p style="text-align: center; font-style: italic; color: #666;">Figure : S-MAC - alternance synchronisee entre periodes de sommeil et d'activite</p>

Avantages : reduction significative de l'idle listening, adapte aux applications avec trafic periodique.
Inconvenients : latence accrue due aux periodes de sommeil, probleme du "sleep delay" en multi-saut.

**B-MAC (Berkeley-MAC)**

B-MAC est un protocole MAC a contention utilisant un mecanisme de **preamble sampling** (Low Power Listening). Plutot que de synchroniser les noeuds, chaque noeud echantillonne periodiquement le canal pour detecter un preambule.

Principes cles :
- **Preamble sampling** : les noeuds se reveillent brievement a intervalles reguliers pour verifier l'activite du canal
- **Long preambule** : l'emetteur envoie un long preambule avant les donnees, garantissant que le recepteur detecte la transmission
- **CCA (Clear Channel Assessment)** : evaluation de l'etat du canal avant emission
- **Pas de synchronisation** : simplicite de mise en oeuvre

<img src="/img/BE_WSNL/B_MAC.png" alt="B-MAC : preamble sampling et low power listening" style="width: 60%; display: block; margin: 0 auto;">
<p style="text-align: center; font-style: italic; color: #666;">Figure : B-MAC - mecanisme de preamble sampling pour detecter les transmissions</p>

Avantages : simple, pas de synchronisation requise, faible overhead.
Inconvenients : long preambule consommant de l'energie, latence variable, overhead pour l'emetteur.

**T-MAC (Timeout-MAC)**

T-MAC est une amelioration de S-MAC qui adapte dynamiquement la duree des periodes d'activite. Quand aucun evenement n'est detecte pendant un timeout, le noeud retourne en sommeil plus tot.

Principes cles :
- **Timeout adaptatif** : la periode active est raccourcie si aucune activite n'est detectee
- **Meilleure adaptation** : s'adapte au trafic variable (faible et fort)
- **Early sleeping** : les noeuds peuvent dormir plus longtemps en cas de faible trafic

<img src="/img/BE_WSNL/T_MAC.png" alt="T-MAC : duty cycling adaptatif avec timeout" style="width: 60%; display: block; margin: 0 auto;">
<p style="text-align: center; font-style: italic; color: #666;">Figure : T-MAC - adaptation dynamique de la periode active selon le trafic</p>

Avantages : meilleure efficacite energetique que S-MAC en trafic variable.
Inconvenients : probleme du "early sleeping" ou un noeud s'endort alors qu'un voisin veut lui transmettre.

#### 2.2 Protocoles planifies (Schedule-Based)

**L-MAC (Lightweight-MAC)**

L-MAC est un protocole MAC base sur TDMA (Time Division Multiple Access) avec allocation decentralisee des slots temporels. Chaque noeud choisit son slot de maniere autonome, sans coordinateur central.

Principes cles :
- **TDMA decentralise** : chaque noeud s'attribue un slot unique en ecoutant les slots deja occupes par ses voisins
- **Pas de collision** : acces deterministe au canal
- **Scalabilite** : allocation autonome des slots permettant l'ajout de noeuds

<img src="/img/BE_WSNL/L_MAC.png" alt="L-MAC : TDMA decentralise avec allocation autonome des slots" style="width: 60%; display: block; margin: 0 auto;">
<p style="text-align: center; font-style: italic; color: #666;">Figure : L-MAC - allocation decentralisee des slots TDMA</p>

Avantages : pas de collision, deterministe, economie d'energie (pas d'idle listening pendant les slots des autres).
Inconvenients : necessite synchronisation, moins flexible en cas de trafic variable, complexite d'allocation des slots.

#### 2.3 Protocoles hybrides

**Z-MAC (Zebra-MAC)**

Z-MAC est un protocole hybride qui combine les avantages de CSMA (contention) et TDMA (schedule). Il s'adapte automatiquement aux conditions de trafic :

- **Faible trafic** : fonctionne en mode CSMA (acces libre, faible latence)
- **Fort trafic** : bascule en mode TDMA (acces ordonne, pas de collision)

Le noeud detecte le niveau de contention et choisit le mode le plus adapte. Cette adaptabilite rend Z-MAC performant dans les environnements dynamiques ou le trafic fluctue.

**Tableau comparatif des protocoles MAC** :

| Protocole | Type | Duty cycling | Synchronisation | Latence | Energie | Scalabilite |
|-----------|------|-------------|-----------------|---------|---------|-------------|
| S-MAC | Contention | Oui (fixe) | Oui | Moyenne | Bonne | Moyenne |
| B-MAC | Contention | Preamble sampling | Non | Variable | Bonne | Bonne |
| T-MAC | Contention | Oui (adaptatif) | Oui | Moyenne | Tres bonne | Moyenne |
| L-MAC | Schedule | TDMA | Oui | Faible | Tres bonne | Bonne |
| Z-MAC | Hybride | CSMA/TDMA | Oui | Adaptative | Tres bonne | Tres bonne |

<h3 class="section-title">3. Techniques de modulation pour communications a faible puissance</h3>

Les communications dans les WSN et les reseaux LPWAN utilisent des techniques de modulation specifiques, optimisees pour la faible consommation, la robustesse et la portee.

**Modulations de base pour WSN** :

| Technique | Description | Usage |
|-----------|-------------|-------|
| BPSK | Binary Phase Shift Keying - 1 bit par symbole | Sigfox, 868/915 MHz ZigBee |
| O-QPSK | Offset Quadrature PSK - 2 bits par symbole | ZigBee 2.4 GHz |
| FSK | Frequency Shift Keying - frequences distinctes | LoRa (base), Sigfox |
| GFSK | Gaussian FSK - transitions lissees | Bluetooth Low Energy |
| CSS | Chirp Spread Spectrum | LoRa |
| DSSS | Direct Sequence Spread Spectrum | ZigBee, 802.15.4 |

**DSSS (Direct Sequence Spread Spectrum)** :

Le DSSS est utilise par ZigBee (IEEE 802.15.4). Le principe consiste a etaler le signal sur une bande plus large que necessaire en multipliant les donnees par un code pseudo-aleatoire (PN sequence) a debit plus eleve (chip rate).

Avantages :
- Robustesse contre les interferences et le bruit
- Resistance au multi-trajet (multipath fading)
- Possibilite de partage de la bande (CDMA)
- Faible densite spectrale de puissance (discretion)

**Modulation pour LPWAN** :

Les technologies LPWAN (Sigfox, LoRa) utilisent des modulations ultra-narrowband (UNB) ou a etalement de spectre pour maximiser la portee avec une puissance d'emission tres faible :
- **Sigfox** : modulation DBPSK (Differential BPSK) sur bande ultra-etroite (100 Hz), permettant une portee de 10-50 km en zone rurale
- **LoRa** : modulation CSS (Chirp Spread Spectrum) avec facteur d'etalement variable (SF7 a SF12), compromis debit/portee/robustesse

<h3 class="section-title">4. Protocole Sigfox et technologies LPWAN</h3>

Sigfox est un protocole LPWAN (Low Power Wide Area Network) concu pour les objets connectes necessitant une transmission de petites quantites de donnees sur de longues distances avec une tres faible consommation energetique.

**Caracteristiques de Sigfox** :

| Parametre | Valeur |
|-----------|--------|
| Bande de frequence | 868 MHz (Europe), 915 MHz (USA) |
| Modulation | DBPSK (uplink), GFSK (downlink) |
| Largeur de canal | 100 Hz (ultra-narrowband) |
| Debit | 100 bps (uplink), 600 bps (downlink) |
| Taille max message | 12 octets (uplink), 8 octets (downlink) |
| Messages/jour | 140 (uplink), 4 (downlink) |
| Portee | 10-50 km (rural), 3-10 km (urbain) |
| Consommation emission | ~50 mW |
| Duree de vie batterie | 10-15 ans (typique) |

**Architecture Sigfox** :
- Les devices emettent des messages courts vers les stations de base Sigfox
- Pas de negociation prealable (protocole unidirectionnel principalement)
- Chaque message est emis 3 fois sur des frequences aleatoires (diversite frequentielle)
- Le cloud Sigfox recoit et deduque les messages

**Cas d'usage** :
- Releve de compteurs (eau, gaz, electricite)
- Suivi d'actifs (tracking logistique)
- Surveillance environnementale
- Alarmes et alertes
- Agriculture de precision

**Comparaison LPWAN** :

| Critere | Sigfox | LoRa/LoRaWAN | NB-IoT |
|---------|--------|-------------|--------|
| Spectre | Non licence (ISM) | Non licence (ISM) | Licence (LTE) |
| Portee | 10-50 km | 5-20 km | 1-10 km |
| Debit | 100 bps | 0.3-50 kbps | 200 kbps |
| Latence | Secondes | Secondes | 1-10 s |
| Bidirectionnel | Limite | Oui | Oui |
| Infra | Operateur Sigfox | Prive ou operateur | Operateur telecom |
| Cout device | Tres faible | Faible | Moyen |

<h3 class="section-title">5. Pile protocolaire ZigBee - PHY/MAC/NWK/APL</h3>

ZigBee est un protocole de communication sans fil a faible puissance et faible debit, concu pour les applications IoT et WSN. Il repose sur le standard IEEE 802.15.4 pour les couches PHY et MAC, et ajoute les couches reseau (NWK) et application (APL).

<img src="/img/BE_WSNL/Zigbee_Layer.png" alt="Pile protocolaire ZigBee : couches PHY, MAC, NWK, APL" style="width: 40%; display: block; margin: 0 auto;">
<p style="text-align: center; font-style: italic; color: #666;">Figure : Architecture en couches du protocole ZigBee</p>

#### 5.1 Couche physique (PHY) - IEEE 802.15.4

La couche PHY gere la modulation/demodulation des donnees et la transmission/reception des signaux radio.

**Bandes de frequence** :

| Bande | Frequence | Canaux | Debit | Modulation | Region |
|-------|-----------|--------|-------|------------|--------|
| 2.4 GHz | 2400-2483.5 MHz | 16 (11-26) | 250 kbps | O-QPSK + DSSS | Mondiale |
| 915 MHz | 902-928 MHz | 10 (1-10) | 40 kbps | BPSK + DSSS | Ameriques |
| 868 MHz | 868.0-868.6 MHz | 1 (0) | 20 kbps | BPSK + DSSS | Europe |

**Caracteristiques PHY** :
- **Etalement de spectre DSSS** : robustesse contre les interferences
- **Puissance d'emission** : typiquement -3 dBm a 20 dBm
- **Sensibilite** : -85 dBm (2.4 GHz), -92 dBm (868/915 MHz)
- **Portee** : 10-100 m en interieur, jusqu'a 1 km en exterieur (selon puissance et environnement)

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_WSNL/Zigbee_schema.png" style="width: 50%;"/>
    <img src="/img/BE_WSNL/Zigbee_Graph.png" style="width: 50%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">Figure : Schema de modulation ZigBee et representation spectrale du signal</p>
<br>

#### 5.2 Couche MAC - IEEE 802.15.4

La couche MAC de ZigBee gere l'acces au canal et l'adressage des noeuds.

**Mecanisme d'acces au canal** :
- **CSMA-CA** (Carrier Sense Multiple Access with Collision Avoidance) : le noeud ecoute le canal avant d'emettre pour eviter les collisions
- **Slotted CSMA-CA** : en mode beacon-enabled, l'acces se fait dans des slots temporels synchronises
- **Unslotted CSMA-CA** : en mode non-beacon, acces asynchrone

**Configurations reseau** :
- **Beacon-enabled** : le coordinateur emet des beacons periodiques pour synchroniser les noeuds. La supertrame est divisee en CAP (Contention Access Period) et CFP (Contention Free Period avec GTS)
- **Non-beacon-enabled** : les noeuds communiquent de maniere asynchrone, adapte pour les transmissions sporadiques

**Securite MAC** :
- **AES-128** : chiffrement robuste des donnees transmises
- Authentification et integrite des trames

#### 5.3 Couche reseau (NWK)

La couche NWK gere le routage des paquets et la topologie du reseau.

**Types de noeuds ZigBee** :
- **ZigBee Coordinator (ZC)** : un seul par reseau, initie la formation du reseau, attribue les adresses
- **ZigBee Router (ZR)** : relaye les paquets, etend la couverture
- **ZigBee End Device (ZED)** : noeud feuille, ne relaye pas, peut dormir pour economiser l'energie

**Topologies supportees** :
- **Etoile** : tous les noeuds communiquent avec le coordinateur
- **Arbre** : structure hierarchique via les routeurs
- **Maille** : routage multi-saut entre routeurs pour la resilience

**Routage** :
- Algorithme AODV (Ad hoc On-demand Distance Vector) pour le routage en maille
- Routage hierarchique en arbre

#### 5.4 Couche application (APL)

La couche APL comprend le framework applicatif ZigBee, incluant :
- **APS (Application Support Sub-Layer)** : gestion des liaisons, decouverte de services
- **ZDO (ZigBee Device Object)** : gestion du reseau, securite, configuration
- **Profils d'application** : ZigBee Home Automation, ZigBee Light Link, ZigBee Smart Energy

<h3 class="section-title">6. M2M sur 4G LTE et 5G</h3>

L'etude des communications Machine-to-Machine (M2M) sur les reseaux cellulaires 4G LTE et 5G est un aspect important du cours, reliant les WSN aux infrastructures de telecommunications globales.

**M2M sur 4G LTE** :

Le LTE (Long Term Evolution) a ete adapte pour supporter les communications IoT/M2M avec :
- **LTE-M (LTE Cat-M1)** : categorie de device optimisee pour l'IoT
  - Debit : 1 Mbps (downlink/uplink)
  - Bande passante reduite : 1.4 MHz (vs 20 MHz pour LTE standard)
  - Mode PSM (Power Saving Mode) pour economie d'energie
  - Support de la mobilite et du handover
- **NB-IoT (Narrowband IoT)** : deploye dans la bande LTE
  - Bande passante : 200 kHz
  - Debit : ~200 kbps
  - Portee amelioree (+20 dB MCL vs LTE)
  - Tres faible consommation

**M2M sur 5G** :

La 5G introduit des categories specifiques pour l'IoT :
- **mMTC (massive Machine Type Communications)** : support de millions de devices par km2
- **URLLC (Ultra-Reliable Low-Latency Communications)** : latence < 1 ms, fiabilite > 99.999%
- **Network Slicing** : reseaux virtuels dedies par cas d'usage

**Architecture M2M** :

L'architecture M2M comprend :
- **Domain des devices** : capteurs, actionneurs, gateways
- **Domain du reseau** : infrastructure d'acces (cellulaire, LPWAN) et coeur de reseau
- **Domain des applications** : plateformes cloud, traitement des donnees, services

**Standards M2M** :
- **oneM2M** : standard de plateforme M2M/IoT interoperable
- **ETSI M2M** : architecture de reference europeenne
- **3GPP** : specifications pour LTE-M, NB-IoT, 5G mMTC

<h3 class="section-title">7. Routage econome en energie</h3>

Le routage dans les WSN doit prendre en compte la contrainte energetique fondamentale. Plusieurs approches existent :

**Routage plat** :
- **Flooding** : chaque noeud retransmet a tous ses voisins (simple mais inefficace en energie)
- **Gossiping** : retransmission a un voisin aleatoire (reduction du trafic)
- **Directed Diffusion** : routage par requetes et gradients, elimine les transmissions inutiles

**Routage hierarchique** :
- **LEACH (Low-Energy Adaptive Clustering Hierarchy)** : formation de clusters avec un cluster head tournant qui agregue les donnees avant transmission au sink
- **TEEN (Threshold-sensitive Energy Efficient Network)** : variante de LEACH pour applications reactives
- **PEGASIS (Power-Efficient Gathering in Sensor Information Systems)** : formation de chaines pour minimiser la distance de transmission

**Criteres de selection de route** :
- Energie residuelle des noeuds
- Nombre de sauts
- Qualite du lien (RSSI, taux d'erreur)
- Latence
- Equilibrage de charge energetique dans le reseau

<h3 class="section-title">8. SDR - Software Defined Radio</h3>

Le SDR (Software Defined Radio) est un concept ou les fonctions de traitement du signal radio (modulation, demodulation, filtrage, codage) sont implementees en logiciel plutot qu'en materiel dedie.

**Principes du SDR** :
- Numerisation du signal radio le plus tot possible dans la chaine de reception
- Traitement numerique du signal (DSP) en logiciel
- Flexibilite : changement de protocole par mise a jour logicielle
- Plateforme generique pour experimenter differentes modulations

**GNU Radio** :
GNU Radio est une plateforme open-source pour le SDR. Elle permet de :
- Construire des chaines de traitement radio par blocs graphiques
- Implementer et tester des modulations (BPSK, QPSK, FSK, OFDM)
- Analyser des signaux en temps reel
- Prototyper des systemes de communication

**Application au cours** :
Le sujet de TP SDR proposait d'implementer un emetteur-recepteur numerique en utilisant GNU Radio, permettant de comprendre concretement le fonctionnement de la couche physique des protocoles WSN.

<h3 class="section-title">9. Architecture d'un noeud capteur - Details</h3>

**Sous-systeme de communication** :

Le transceiver radio est le composant le plus consommateur d'energie. Ses etats de fonctionnement sont :
- **Transmit (TX)** : emission de donnees (consommation maximale)
- **Receive (RX)** : reception active (consommation elevee)
- **Idle** : ecoute du canal sans donnees (consommation significative)
- **Sleep** : mode veille profond (consommation minimale, quelques uA)

Le duty cycling consiste a alterner entre les etats sleep et actif pour minimiser le temps passe en idle listening.

**Sous-systeme de traitement** :

Les microcontroleurs utilises dans les WSN sont optimises pour la faible consommation :
- Architecture ARM Cortex-M (STM32, nRF52)
- Modes de sommeil multiples (sleep, deep sleep, standby)
- Peripheriques a faible puissance (ADC, SPI, UART)
- Oscillateurs a faible courant

**Sous-systeme d'energie** :

Sources d'alimentation :
- Batteries primaires (non rechargeables) : longue duree de vie, capacite fixe
- Batteries secondaires (rechargeables) : couplees avec energy harvesting
- Energy harvesting : solaire, piezoelectrique, thermique, RF
- Supercondensateurs : stockage temporaire pour pics de consommation

---

## PART D : ANALYSE ET REFLEXION

<h3 class="section-title">Competences acquises</h3>

**Analyse et evaluation de protocoles WSN/IoT** :
Capacite a analyser et comparer les protocoles MAC (S-MAC, T-MAC, B-MAC, L-MAC, Z-MAC) en fonction de criteres comme la consommation energetique, la latence, la scalabilite et l'adaptation au trafic.

**Suggestion de solutions technologiques optimales** :
Aptitude a recommander les technologies de communication les plus adaptees (ZigBee, Sigfox, LoRa, NB-IoT, 5G) selon les contraintes du cas d'usage : portee, debit, consommation, cout, bidirectionnalite.

**Optimisation des protocoles de communication IoT** :
Comprehension des mecanismes de duty cycling, des techniques de modulation a faible puissance et des strategies de routage econome en energie.

**Comprehension des communications numeriques** :
Maitrise des techniques de modulation (DSSS, O-QPSK, BPSK, CSS), du fonctionnement d'un emetteur-recepteur RF numerique et des principes du SDR.

**Implementation pratique** :
Experience de developpement d'une couche MAC en Python, comprehension concrete de la gestion des trames et de l'acces au medium.

<h3 class="section-title">Points cles a retenir</h3>

**1. L'energie est la contrainte fondamentale des WSN** :
Tous les choix de conception (protocole MAC, routage, modulation, topologie) sont guides par la necessite de minimiser la consommation energetique pour prolonger la duree de vie du reseau.

**2. Le duty cycling est incontournable** :
Que ce soit par synchronisation (S-MAC, T-MAC) ou par preamble sampling (B-MAC), alterner entre sommeil et activite est la strategie cle pour economiser l'energie.

**3. Pas de protocole universel** :
Chaque protocole MAC a ses forces et faiblesses. Le choix depend du cas d'usage : trafic periodique ou evenementiel, densite du reseau, exigences de latence, topologie.

**4. Les technologies LPWAN completent les WSN** :
Sigfox et LoRa adressent les besoins de longue portee avec tres faible consommation, tandis que ZigBee est adapte aux reseaux a courte portee avec maillage.

**5. L'integration cellulaire (4G/5G) ouvre de nouvelles possibilites** :
LTE-M, NB-IoT et 5G mMTC permettent d'integrer les objets connectes dans l'infrastructure cellulaire existante, offrant couverture, QoS et interoperabilite.

<h3 class="section-title">Retour d'experience</h3>

**Premier travail - Etude comparative des protocoles** :
L'etude initiale de differents protocoles comme LoRa, ZigBee et Sigfox a ete enrichissante car elle m'a donne une vue d'ensemble de leur fonctionnement et des principaux protocoles qu'ils utilisent. Cette approche comparative permet de comprendre les compromis fondamentaux entre portee, debit, consommation et cout.

**Deuxieme partie - Analyse detaillee des protocoles MAC** :
L'etude approfondie de chaque protocole MAC m'a permis de comprendre les subtilites de ces protocoles : comment S-MAC gere la synchronisation, pourquoi B-MAC evite ce probleme avec le preamble sampling, comment T-MAC ameliore S-MAC avec le timeout adaptatif, et comment L-MAC garantit l'absence de collision avec le TDMA decentralise.

**Sessions de TP** :
Les travaux pratiques ont ete l'occasion de mettre en pratique les concepts etudies en cours. Le developpement de la couche MAC en Python m'a permis de voir concretement comment les paquets de donnees sont geres et transmis au sein d'un reseau. Cette experience pratique a renforce mes connaissances theoriques.

**Limites** :
Bien que le SDR ait ete aborde en cours avec GNU Radio, je n'ai pas eu de sessions dediees a la pratique du SDR, ce qui limite mon experience sur la couche physique. De plus, la multiplicite des protocoles rend difficile une maitrise complete de chacun d'entre eux. Avec l'experience professionnelle, je serai amene a approfondir davantage les protocoles pertinents a mon domaine d'activite.

<h3 class="section-title">Mon avis</h3>

Ce cours etait bien structure et m'a apporte une base solide en technologies WSN et localisation. L'approche progressive - d'abord l'etude comparative des protocoles, puis l'approfondissement des couches MAC, et enfin les travaux pratiques - est pedagogiquement efficace.

La diversite des sujets couverts (MAC pour WSN, ZigBee, Sigfox, M2M cellulaire, SDR) donne une vision complete de l'ecosysteme des communications pour objets connectes. Cette vision transversale est particulierement utile pour un ingenieur qui devra choisir les technologies les plus adaptees aux besoins specifiques de ses projets.

Je me sens desormais confiant dans ma capacite a analyser et optimiser des protocoles de communication pour l'IoT, tout en etant conscient que le domaine est vaste et en constante evolution.

---

## Rapports et Projets

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Analyse de la couche MAC pour WSN</h4>
      <p>Rapport detaille sur l'analyse comparative des protocoles MAC (S-MAC, T-MAC, B-MAC, L-MAC, Z-MAC) pour les reseaux de capteurs sans fil.</p>
      <iframe src="/file/reports/S9/Chanfreau_MAC_Layer.pdf" width="100%" height="600px" style="overflow: auto;" frameborder="0"></iframe>
      <p><a href="/file/reports/S9/Chanfreau_MAC_Layer.pdf" target="_blank">Telecharger le rapport MAC Layer</a></p>
    </div>
  </div>
</div>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Etude du protocole Sigfox et LPWAN</h4>
      <p>Rapport sur le protocole Sigfox, les technologies LPWAN et leurs applications dans l'IoT.</p>
      <iframe src="/file/reports/S9/Rapport_Sigfox.pdf" width="100%" height="600px" style="overflow: auto;" frameborder="0"></iframe>
      <p><a href="/file/reports/S9/Rapport_Sigfox.pdf" target="_blank">Telecharger le rapport Sigfox</a></p>
    </div>
  </div>
</div>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>TP WSN - Smart Subway</h4>
      <p>Rapport de travaux pratiques sur la mise en oeuvre d'un reseau de capteurs sans fil pour une application Smart Subway.</p>
      <iframe src="/file/reports/S9/TP_WSN_REPORT.pdf" width="100%" height="600px" style="overflow: auto;" frameborder="0"></iframe>
      <p><a href="/file/reports/S9/TP_WSN_REPORT.pdf" target="_blank">Telecharger le rapport TP WSN</a></p>
    </div>
  </div>
</div>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>M2M sur 4G LTE et 5G</h4>
      <p>Rapport sur les communications Machine-to-Machine sur les reseaux cellulaires 4G LTE et 5G, architectures et standards.</p>
      <iframe src="/file/reports/S9/REPORT_M2M_on_4G_LTE_n_5G.pdf" width="100%" height="600px" style="overflow: auto;" frameborder="0"></iframe>
      <p><a href="/file/reports/S9/REPORT_M2M_on_4G_LTE_n_5G.pdf" target="_blank">Telecharger le rapport M2M</a></p>
    </div>
  </div>
</div>

---

## Documents de Cours

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Polycopie WSN 2020</h4>
      <p>Cours complet sur les reseaux de capteurs sans fil : architecture, protocoles MAC, routage, localisation.</p>
      <embed src="/cours-pdf/S9/WSNL/PolyWSN_2020.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/WSNL/PolyWSN_2020.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>Modulations et MAC</h4>
      <p>Cours sur les techniques de modulation pour les communications a faible puissance et les protocoles MAC pour WSN.</p>
      <embed src="/cours-pdf/S9/WSNL/Modulations_et_MAC.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/WSNL/Modulations_et_MAC.pdf" target="_blank">Telecharger</a></p>
    </div>
  </div>
</div>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>SDR - Software Defined Radio (Sujet)</h4>
      <p>Sujet de TP sur le SDR : implementation d'un emetteur-recepteur numerique avec GNU Radio.</p>
      <embed src="/cours-pdf/S9/WSNL/2020-2021_5ISS_SDR_Sujet.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/WSNL/2020-2021_5ISS_SDR_Sujet.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>BE M2M - Presentation</h4>
      <p>Presentation du bureau d'etude M2M : communications machine-to-machine sur reseaux cellulaires.</p>
      <embed src="/cours-pdf/S9/WSNL/5ISS_-_BE_M2M_-_Presentation.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/WSNL/5ISS_-_BE_M2M_-_Presentation.pdf" target="_blank">Telecharger</a></p>
    </div>
  </div>
</div>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>BE M2M - Sujet</h4>
      <p>Sujet du bureau d'etude M2M sur 4G LTE et 5G.</p>
      <embed src="/cours-pdf/S9/WSNL/2023-2024_-_5ISS_-_BE_M2M_-_Sujet.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/WSNL/2023-2024_-_5ISS_-_BE_M2M_-_Sujet.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>FPGA pour systemes de communication</h4>
      <p>Article IEEE sur l'implementation FPGA pour les systemes de communication dans les WSN.</p>
      <embed src="/cours-pdf/S9/WSNL/ieee_circuitsandsystems_2021_FPGA.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/WSNL/ieee_circuitsandsystems_2021_FPGA.pdf" target="_blank">Telecharger</a></p>
    </div>
  </div>
</div>

---

*Cours suivi en 2024-2025 a l'INSA Toulouse, Departement Genie Electrique et Informatique - Specialisation ISS (Innovative Smart Systems).*

<div class="back-nav">
    <a href="./my-courses-2024-2025.html">&larr; Retour aux Cours 2024-2025</a>
</div>

---
layout: default
title: "🌐 Interconnexion Réseau - Semestre 8"
date: 2024-10-02 10:56:03 +0200
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
    <a href="./my-courses-2023-2024.html">← Retour aux Cours 2023-2024</a>
</div>

# 🌐 Interconnexion Réseau - Semestre 8

**Année académique** : 2023-2024  
**ECTS** : 2.5  
**Catégorie** : Réseaux et Télécommunications

---

## PART A - Présentation Générale du Module

<h3 class="section-title">Vue d'ensemble</h3>

Ce cours approfondit les concepts et protocoles permettant l'interconnexion de réseaux hétérogènes pour former l'Internet global. Il couvre le routage IP, les protocoles de transport TCP et UDP, la qualité de service, les VLANs, la sécurité réseau, et les architectures modernes. L'objectif est de former des ingénieurs capables de concevoir, déployer et administrer des infrastructures réseau complexes.

**Objectifs pédagogiques** :
- Maîtriser les protocoles TCP/IP et le modèle en couches
- Configurer et administrer routeurs et commutateurs Cisco
- Implémenter des protocoles de routage dynamique (RIP, OSPF, BGP)
- Concevoir des architectures réseau multi-sites
- Mettre en œuvre la qualité de service (QoS)
- Segmenter des réseaux avec VLANs
- Sécuriser les infrastructures (ACL, VPN, pare-feu)
- Diagnostiquer et résoudre des problèmes réseau

<h3 class="section-title">Position dans le cursus</h3>

Ce module approfondit les bases acquises précédemment :
- **Réseau (S5)** : modèle OSI, Ethernet, IP de base, TCP/UDP
- **Architecture Matérielle (S6)** : couche physique, signaux
- **Systèmes d'Exploitation (S5)** : sockets, communication inter-processus

Il prépare à :
- **Cloud et Edge Computing (S9)** : réseaux virtuels, SDN
- **IoT (S9)** : protocoles spécifiques, contraintes réseaux
- **Cybersécurité** : sécurité réseau avancée
- **Carrière professionnelle** : administration réseau, architecte infrastructure

---

## PART B - Expérience Personnelle et Contexte d'Apprentissage

<h3 class="section-title">Organisation et ressources</h3>

Le module combinait théorie et pratique intensive :

**Cours magistraux (15h)** :
- Modèles OSI et TCP/IP, encapsulation
- Adressage IPv4 et IPv6, subnetting
- Protocoles de routage (statique, RIP, OSPF, BGP)
- TCP et UDP en détail
- Qualité de service (QoS)
- VLANs et commutation
- Sécurité réseau (ACL, VPN, pare-feu)
- NAT et translation d'adresses

**Travaux dirigés (6h)** :
- Calculs de subnetting
- Conception d'architectures réseau
- Analyse de protocoles
- Configuration de routage

**Travaux pratiques (12h)** :
- **TP1** : Configuration de base routeurs Cisco, routage statique
- **TP2** : Protocoles de routage dynamique (RIP, OSPF)
- **TP3** : VLANs, inter-VLAN routing, ACLs

**Outils utilisés** :
- **Cisco Packet Tracer** : simulation de réseaux
- **GNS3** : émulation équipements réseau
- **Équipements Cisco** : routeurs et switches physiques
- **Wireshark** : capture et analyse de trafic
- **Cisco IOS** : système d'exploitation routeurs/switches

**Ressources** :
- Polycopié complet (4AE-Interconnexion-Rzo)
- TD avec exercices pratiques
- 3 TP guidés avec configurations
- Documentation Cisco
- RFCs des protocoles (TCP, IP, OSPF, BGP)

<h3 class="section-title">Méthodologie d'étude</h3>

**Phase 1 : Maîtriser les fondamentaux** :
Réviser modèle en couches, adressage IP, principes du routage.

**Phase 2 : Approfondir les protocoles** :
Étudier en détail TCP, UDP, OSPF, BGP avec leurs mécanismes internes.

**Phase 3 : Pratiquer la configuration** :
Utiliser Packet Tracer pour configurer des scénarios réseau de complexité croissante.

**Phase 4 : Analyser le trafic** :
Capturer avec Wireshark pour observer les échanges protocolaires réels.

**Phase 5 : Développer le troubleshooting** :
Diagnostiquer pannes réseau selon méthodologie (bottom-up ou top-down du modèle OSI).

<h3 class="section-title">Difficultés rencontrées</h3>

**Complexité des protocoles** :
OSPF et BGP sont des protocoles très riches avec de nombreux paramètres et cas particuliers.

**Syntaxe Cisco IOS** :
La ligne de commande Cisco a sa propre logique et commandes spécifiques à mémoriser.

**Débogage réseau** :
Identifier la source d'un problème dans un réseau complexe demande méthodologie et patience.

**Abstraction vs réalité** :
Les simulations sont simplifiées. Les réseaux réels ont des contraintes physiques, latences, pannes aléatoires.

---

## PART C - Aspects Techniques Détaillés

<h3 class="section-title">1. Modèles de référence réseau</h3>

**Modèle OSI (7 couches)** :

Modèle de référence théorique pour l'architecture des réseaux.

| Couche | Nom | Rôle | Exemples |
|--------|-----|------|----------|
| 7 | Application | Services aux applications | HTTP, FTP, DNS, SMTP |
| 6 | Présentation | Format, chiffrement, compression | SSL/TLS, JPEG, MPEG |
| 5 | Session | Gestion des sessions | NetBIOS, RPC |
| 4 | Transport | Transmission bout en bout | TCP, UDP |
| 3 | Réseau | Routage, adressage logique | IP, ICMP, OSPF, BGP |
| 2 | Liaison | Transmission sur lien physique, adressage MAC | Ethernet, WiFi, PPP |
| 1 | Physique | Transmission bits (signaux électriques, optiques) | Câbles, ondes radio |

**Modèle TCP/IP (4 couches)** :

Modèle pratique utilisé sur Internet.

| Couche | Équivalent OSI | Protocoles principaux |
|--------|----------------|------------------------|
| Application | 5-6-7 | HTTP, FTP, DNS, SMTP, SSH |
| Transport | 4 | TCP, UDP |
| Internet | 3 | IP, ICMP, ARP |
| Accès réseau | 1-2 | Ethernet, WiFi |

**Encapsulation** :

Chaque couche ajoute son en-tête aux données de la couche supérieure.

Données application → Segment TCP → Paquet IP → Trame Ethernet

**Désencapsulation** :

Le récepteur retire les en-têtes couche par couche pour extraire les données.

<h3 class="section-title">2. Adressage IPv4</h3>

**Format** :

Adresse sur 32 bits, notée en 4 octets décimaux séparés par des points.

Exemple : 192.168.1.10

**Classes historiques (obsolètes)** :

Remplacées par CIDR, mais utiles pour comprendre l'évolution.

- Classe A : premier bit = 0, réseau sur 8 bits (grands réseaux)
- Classe B : premiers bits = 10, réseau sur 16 bits
- Classe C : premiers bits = 110, réseau sur 24 bits

**CIDR (Classless Inter-Domain Routing)** :

Notation flexible : adresse IP / longueur préfixe réseau

Exemple : 192.168.10.0/24 signifie réseau sur 24 bits, 8 bits pour hôtes (256 adresses).

**Masque de sous-réseau** :

Détermine quelle partie de l'adresse est le réseau et quelle partie est l'hôte.

/24 correspond au masque 255.255.255.0

**Adresses spéciales** :

- **Adresse réseau** : tous les bits hôte à 0 (ex : 192.168.1.0)
- **Adresse broadcast** : tous les bits hôte à 1 (ex : 192.168.1.255)
- **Loopback** : 127.0.0.1 (interface de bouclage local)
- **Plages privées (RFC 1918)** : non routables sur Internet
  - 10.0.0.0/8
  - 172.16.0.0/12
  - 192.168.0.0/16

**Subnetting** :

Division d'un réseau en sous-réseaux plus petits pour optimiser l'utilisation des adresses et segmenter le réseau.

Exemple : 192.168.1.0/24 divisé en 4 sous-réseaux /26 :
- 192.168.1.0/26 (adresses .0 à .63)
- 192.168.1.64/26 (adresses .64 à .127)
- 192.168.1.128/26 (adresses .128 à .191)
- 192.168.1.192/26 (adresses .192 à .255)

<h3 class="section-title">3. IPv6</h3>

**Motivation** :

Épuisement des adresses IPv4 publiques. IPv6 offre un espace d'adressage quasi illimité.

**Format** :

Adresse sur 128 bits, notée en 8 groupes de 4 chiffres hexadécimaux séparés par deux-points.

Exemple : 2001:0db8:85a3:0000:0000:8a2e:0370:7334

**Simplifications d'écriture** :

- Omettre les zéros en tête de chaque groupe : 2001:db8:85a3:0:0:8a2e:370:7334
- Remplacer une séquence de groupes nuls consécutifs par :: (une seule fois) : 2001:db8:85a3::8a2e:370:7334

**Avantages** :

- Espace d'adressage immense (2 puissance 128 adresses)
- Autoconfiguration simplifiée (SLAAC)
- IPsec intégré natif
- En-tête simplifié (meilleure performance)
- Plus besoin de NAT

**Types d'adresses** :

- **Unicast** : adresse unique identifiant une interface
- **Multicast** : groupe d'interfaces (remplace broadcast)
- **Anycast** : groupe d'interfaces, routé vers la plus proche

**Adresses spéciales** :

- **Loopback** : ::1
- **Link-local** : fe80::/10 (auto-configurées, communication sur lien local)
- **Unique local** : fc00::/7 (équivalent des privées IPv4)
- **Global unicast** : 2000::/3 (routables sur Internet)

<h3 class="section-title">4. Routage - Principes fondamentaux</h3>

**Rôle du routeur** :

Transférer des paquets IP entre réseaux différents en consultant sa table de routage.

**Table de routage** :

Contient les routes vers les réseaux de destination.

Chaque entrée spécifie :
- **Réseau de destination** avec masque
- **Passerelle (next hop)** : adresse IP du prochain routeur ou "directement connecté"
- **Interface de sortie** : par quelle interface envoyer le paquet
- **Métrique** : coût de la route (distance, bande passante, etc.)

**Processus de routage** :

1. Recevoir paquet IP
2. Consulter table de routage pour trouver meilleure route (longest prefix match)
3. Décrémenter TTL (Time To Live)
4. Recalculer checksum de l'en-tête IP
5. Transférer paquet sur l'interface de sortie appropriée

**Route par défaut (default route)** :

Route 0.0.0.0/0 utilisée si aucune route spécifique ne correspond. Typiquement vers Internet via passerelle FAI.

**Routage statique vs dynamique** :

- **Statique** : routes configurées manuellement, adaptées pour petits réseaux ou routes spécifiques
- **Dynamique** : protocoles de routage automatisent la découverte et mise à jour des routes

<h3 class="section-title">5. Protocoles de routage dynamique</h3>

**Classification** :

**IGP (Interior Gateway Protocol)** : au sein d'un système autonome (AS)
- **Distance vector** : RIP, EIGRP
- **Link state** : OSPF, IS-IS

**EGP (Exterior Gateway Protocol)** : entre systèmes autonomes
- **Path vector** : BGP

**RIP (Routing Information Protocol)** :

Protocole de routage distance-vector simple.

**Caractéristiques** :
- Métrique : nombre de sauts (hop count), maximum 15
- Algorithme Bellman-Ford
- Mise à jour complète de la table toutes les 30 secondes
- Convergence lente
- Simple mais limité aux petits réseaux

**OSPF (Open Shortest Path First)** :

Protocole link-state avancé.

**Principe** :
- Chaque routeur connaît la topologie complète de la zone
- Algorithme SPF (Dijkstra) calcule l'arbre des plus courts chemins
- Métrique basée sur le coût (fonction de la bande passante)

**Fonctionnement** :
1. Découverte des voisins via paquets Hello
2. Échange de LSA (Link State Advertisement) décrivant les liens
3. Construction de la base de données topologique (LSDB)
4. Calcul SPF pour déterminer meilleures routes
5. Installation des routes dans la table de routage

**Avantages** :
- Convergence rapide (mises à jour déclenchées, pas périodiques)
- Scalabilité via hiérarchie (aires)
- Supporte VLSM et CIDR
- Authentification des mises à jour

**Hiérarchie OSPF** :

Organisation en aires pour réduire trafic et taille des tables.

- **Aire 0 (backbone)** : aire centrale obligatoire
- **Aires non-backbone** : connectées à l'aire 0 via ABR (Area Border Router)

**BGP (Border Gateway Protocol)** :

Protocole de routage d'Internet entre systèmes autonomes.

**Caractéristiques** :
- Path vector : inclut le chemin complet d'AS
- Politiques de routage complexes (business, préférences)
- eBGP (external) entre AS différents, iBGP (internal) au sein d'un AS
- Métrique : pas seulement technique mais aussi politique

**Rôle** :

BGP maintient la table de routage globale d'Internet. Chaque AS annonce ses préfixes IP.

<h3 class="section-title">6. Protocole TCP (Transmission Control Protocol)</h3>

**Caractéristiques** :

Protocole de transport orienté connexion, fiable.

- **Orienté connexion** : établissement 3-way handshake avant échange de données
- **Fiable** : accusés de réception, retransmission des segments perdus
- **Ordre préservé** : numéros de séquence garantissent l'ordre
- **Contrôle de flux** : fenêtre glissante évite débordement récepteur
- **Contrôle de congestion** : adapte débit selon état du réseau

**En-tête TCP (principaux champs)** :

- **Ports source et destination** (16 bits chacun) : identifient applications
- **Numéro de séquence** (32 bits) : position des données dans le flux
- **Numéro d'accusé de réception** (32 bits) : prochain octet attendu
- **Flags** : SYN (synchronisation), ACK (accusé), FIN (fin), RST (reset), PSH (push), URG (urgent)
- **Fenêtre** (16 bits) : taille du buffer récepteur disponible (contrôle de flux)
- **Checksum** (16 bits) : détection d'erreurs

**Établissement de connexion (3-way handshake)** :

1. **Client → Serveur : SYN** (synchronisation, numéro de séquence initial)
2. **Serveur → Client : SYN+ACK** (acquittement + son propre numéro de séquence)
3. **Client → Serveur : ACK** (acquittement final)

Connexion établie, échange de données peut commencer.

**Fermeture de connexion (4-way handshake)** :

1. **A → B : FIN** (A a fini d'envoyer)
2. **B → A : ACK** (acquittement)
3. **B → A : FIN** (B a fini d'envoyer)
4. **A → B : ACK** (acquittement final)

Ou fermeture brutale avec RST (reset).

**Contrôle de flux (fenêtre glissante)** :

Le récepteur annonce la taille de son buffer disponible (fenêtre).

L'émetteur ne peut pas envoyer plus de données que la taille de la fenêtre.

Évite débordement du buffer récepteur.

**Contrôle de congestion** :

Mécanisme pour adapter le débit selon l'état du réseau et éviter l'effondrement.

**Phases** :
- **Slow Start** : augmentation exponentielle de la fenêtre de congestion
- **Congestion Avoidance** : augmentation linéaire après atteinte d'un seuil
- **Fast Retransmit** : retransmission immédiate après 3 ACK dupliqués
- **Fast Recovery** : réduction modérée de la fenêtre après perte

**Algorithmes** : TCP Tahoe, Reno, New Reno, CUBIC (utilisé par Linux par défaut).

<h3 class="section-title">7. Protocole UDP (User Datagram Protocol)</h3>

**Caractéristiques** :

Protocole de transport simple, non connecté, non fiable.

- **Sans connexion** : pas d'établissement de connexion
- **Non fiable** : pas d'accusé de réception, pas de retransmission
- **Pas de contrôle de flux ni de congestion**
- **Pas de garantie d'ordre**
- **En-tête minimal** : seulement 8 octets

**En-tête UDP** :

- Port source (16 bits)
- Port destination (16 bits)
- Longueur (16 bits)
- Checksum (16 bits)

**Utilisations** :

Applications où la rapidité prime sur la fiabilité :
- **VoIP et vidéoconférence** : temps réel, perte acceptable
- **Streaming vidéo/audio** : retransmission inutile (déjà trop tard)
- **DNS** : requêtes courtes, retransmission gérée par application
- **DHCP** : configuration réseau initiale
- **Jeux en ligne** : latence critique
- **SNMP** : gestion réseau simple

**Avantages** :

Faible overhead, latence minimale, adapté aux applications temps réel.

<h3 class="section-title">8. Qualité de Service (QoS)</h3>

**Problématique** :

Le réseau Internet est "best-effort" (meilleur effort) : aucune garantie de bande passante, latence, ou fiabilité.

Insuffisant pour applications exigeantes : VoIP (voix), vidéoconférence, streaming.

**Paramètres de QoS** :

| Paramètre | Description | Importance pour |
|-----------|-------------|-----------------|
| Bande passante | Débit garanti | Streaming vidéo |
| Latence | Délai de transit | VoIP, jeux |
| Gigue (jitter) | Variation de latence | VoIP, vidéo |
| Perte de paquets | Taux de paquets perdus | Toutes applications |

**Mécanismes de QoS** :

**Classification et marquage** :

Identifier le type de trafic et le marquer dans l'en-tête pour traitement différencié.

- **DSCP (Differentiated Services Code Point)** : 6 bits dans en-tête IP
- **CoS (Class of Service)** : 3 bits dans tag 802.1Q (VLAN)

**Files d'attente (Queuing)** :

Gérer priorités et ordonnancement des paquets.

- **FIFO** : First In First Out (pas de priorité)
- **Priority Queuing** : files de différentes priorités (stricte)
- **WFQ (Weighted Fair Queuing)** : partage équitable avec pondération
- **CBWFQ (Class-Based WFQ)** : WFQ par classe de trafic
- **LLQ (Low Latency Queuing)** : file prioritaire + WFQ pour le reste

**Policing et Shaping** :

Contrôler le taux de trafic.

- **Policing** : limiter le débit, rejeter ou remarquer l'excédent
- **Shaping** : lisser le trafic, tamponner l'excédent dans une file

**Modèles de QoS** :

- **IntServ (Integrated Services)** : réservation de ressources par flux (RSVP), peu déployé (complexité)
- **DiffServ (Differentiated Services)** : classes de service agrégées, scalable, largement déployé

<h3 class="section-title">9. VLANs (Virtual LANs)</h3>

**Principe** :

Segmenter un réseau physique en plusieurs réseaux logiques isolés.

**Avantages** :

- **Isolation des domaines de broadcast** : réduit trafic inutile
- **Sécurité** : séparation logique du trafic (finance, RH, invités)
- **Flexibilité** : réorganisation sans recâblage physique
- **Optimisation** : grouper utilisateurs par fonction plutôt que par localisation

**Standard 802.1Q (VLAN Tagging)** :

Ajout d'un tag de 4 octets dans la trame Ethernet contenant :
- **VLAN ID** (12 bits) : identifiant du VLAN (4096 VLANs possibles)
- **Priority** (3 bits) : priorité CoS pour QoS

**Types de ports** :

| Type | Description | Utilisation |
|------|-------------|-------------|
| Access | Appartient à un seul VLAN, pas de tag | Connexion terminaux |
| Trunk | Transporte plusieurs VLANs, avec tags | Interconnexion switches |

**Communication inter-VLANs** :

Les VLANs sont isolés. Pour communiquer entre eux, il faut un routeur (ou switch layer 3).

Méthodes :
- **Router on a stick** : un seul lien physique, sous-interfaces par VLAN
- **Switch L3** : routage inter-VLAN directement sur le switch

<h3 class="section-title">10. Commutation (Switching)</h3>

**Principe** :

Un switch (commutateur) transfère des trames Ethernet selon les adresses MAC.

**Table CAM (Content Addressable Memory)** :

Associe adresses MAC aux ports du switch.

**Apprentissage** :

Le switch apprend les adresses MAC en observant l'adresse source des trames reçues.

**Transfert (Forwarding)** :

- **Adresse destination connue** : transférer sur le port associé dans la table CAM
- **Adresse inconnue** : flood (diffuser) sur tous les ports sauf celui de réception
- **Broadcast ou multicast** : flood

**Spanning Tree Protocol (STP)** :

Protocole pour éviter les boucles dans les topologies redondantes (liens multiples entre switches).

**Fonctionnement** :
1. Élection d'un root bridge (switch racine)
2. Calcul du chemin optimal vers le root bridge
3. Blocage des ports créant des boucles
4. Reconfiguration automatique en cas de panne

**Variantes** : RSTP (Rapid STP) pour convergence plus rapide, MSTP (Multiple STP) pour plusieurs VLANs.

<h3 class="section-title">11. NAT (Network Address Translation)</h3>

**Problématique** :

Pénurie d'adresses IPv4 publiques. Toutes les machines ne peuvent pas avoir une adresse publique.

**Principe** :

Traduire des adresses IP privées en adresses publiques lors de la traversée d'un routeur.

**Types de NAT** :

**NAT statique** :

Mapping fixe 1:1 entre une adresse privée et une adresse publique.

Usage : serveurs accessibles depuis Internet.

**NAT dynamique** :

Pool d'adresses publiques, allocation dynamique aux machines internes.

**PAT (Port Address Translation) ou NAT Overload** :

Plusieurs machines internes partagent une seule adresse publique.

Différenciation par numéros de port.

Table NAT associe : IP privée:port privé ↔ IP publique:port public

**Usage** : la plupart des box Internet (tous les équipements domestiques partagent l'IP publique).

**Limitations du NAT** :

- Casse la connectivité bout-à-bout (end-to-end)
- Problèmes pour protocoles incluant adresses IP dans données (FTP, SIP)
- Difficultés pour applications P2P et serveurs entrants
- Nécessite techniques de traversée (STUN, TURN) pour VoIP

**IPv6 et NAT** :

IPv6 rend NAT inutile (adresses suffisantes pour tous). Retour à la connectivité bout-à-bout.

<h3 class="section-title">12. Sécurité réseau</h3>

**Listes de Contrôle d'Accès (ACL)** :

Filtrer le trafic selon critères définis (adresses IP, ports, protocoles).

**Types** :
- **ACL standard** : filtre uniquement sur adresse IP source
- **ACL étendue** : filtre sur IP source/destination, ports, protocoles

**Application** : sur interfaces de routeurs (trafic entrant ou sortant).

**Pare-feu (Firewall)** :

Équipement ou logiciel filtrant le trafic de manière plus sophistiquée.

**Fonctionnalités** :
- Filtrage stateful (inspection d'état des connexions)
- Filtrage applicatif (deep packet inspection)
- Prévention d'intrusions (IPS)
- Journalisation et alertes

**VPN (Virtual Private Network)** :

Créer un tunnel sécurisé à travers un réseau non sécurisé (Internet).

**Types** :
- **Site-to-Site** : interconnecter des sites distants d'une entreprise
- **Remote Access** : permettre accès distant sécurisé (télétravail)

**Protocoles** :
- **IPsec** : chiffrement au niveau IP (tunnel ou transport)
- **SSL/TLS VPN** : basé sur HTTPS, plus simple pour remote access

**Menaces courantes** :

| Menace | Description | Contre-mesure |
|--------|-------------|---------------|
| DoS/DDoS | Saturation de ressources | Filtrage, limitation de taux, CDN |
| Spoofing | Usurpation d'adresse IP | Filtrage ingress/egress, authentification |
| Man-in-the-Middle | Interception de communication | Chiffrement (TLS, IPsec) |
| ARP poisoning | Corruption de tables ARP | Dynamic ARP Inspection |
| VLAN hopping | Accès non autorisé à VLANs | Configuration sécurisée trunk/access |

**Bonnes pratiques** :

- Défense en profondeur (multiples couches de sécurité)
- Principe du moindre privilège
- Segmentation réseau (VLANs, zones DMZ)
- Mises à jour régulières (firmware, patches)
- Surveillance et détection (IDS, SIEM)
- Sauvegardes de configurations

---

## PART D - Analyse Réflexive et Perspectives

<h3 class="section-title">Compétences acquises</h3>

**Compréhension approfondie TCP/IP** :
Maîtrise des protocoles fondamentaux d'Internet et de leur fonctionnement interne.

**Configuration d'équipements réseau** :
Capacité à configurer routeurs et switches Cisco via ligne de commande (CLI).

**Conception d'architectures réseau** :
Aptitude à concevoir des infrastructures multi-sites avec routage, VLANs, QoS.

**Troubleshooting méthodique** :
Compétence pour diagnostiquer et résoudre des problèmes réseau en suivant le modèle en couches.

**Sécurisation des infrastructures** :
Capacité à implémenter ACLs, VPN, segmentation pour sécuriser un réseau.

<h3 class="section-title">Points clés à retenir</h3>

**1. Le modèle en couches est fondamental** :
Comprendre l'encapsulation et le rôle de chaque couche permet de diagnostiquer efficacement les problèmes.

**2. OSPF est le protocole IGP moderne** :
RIP est obsolète pour réseaux de taille significative. OSPF offre scalabilité et convergence rapide.

**3. TCP assure la fiabilité, UDP la rapidité** :
Choisir le bon protocole de transport selon les besoins de l'application.

**4. La QoS est cruciale pour temps réel** :
VoIP et vidéo nécessitent priorité et garanties pour fonctionner correctement.

**5. VLANs = segmentation logique efficace** :
Organiser le réseau en VLANs améliore sécurité, performance, et gestion.

<h3 class="section-title">Retour d'expérience</h3>

**Aspect formateur** :
Les TP sur équipements Cisco ont donné une dimension concrète à la théorie. Voir les routes apparaître dans la table après configuration d'OSPF est satisfaisant.

**Complexité de Cisco IOS** :
La CLI Cisco a une courbe d'apprentissage. Les modes (user, privileged, configuration) et la hiérarchie des commandes demandent pratique.

**Importance du troubleshooting** :
Les configurations ne fonctionnent pas toujours du premier coup. Apprendre à diagnostiquer méthodiquement (ping, traceroute, show commands) est essentiel.

**Protocoles robustes** :
TCP et OSPF sont des merveilles d'ingénierie. Leur robustesse face aux pannes et congestions est impressionnante.

<h3 class="section-title">Applications pratiques</h3>

**Pour administrateur réseau** :
- Déployer et maintenir infrastructures réseau d'entreprise
- Configurer routeurs et switches
- Implémenter redondance et haute disponibilité
- Assurer sécurité et QoS

**Pour architecte réseau** :
- Concevoir architectures multi-sites
- Dimensionner bande passante
- Choisir équipements et protocoles
- Planifier évolution et scalabilité

**Pour ingénieur DevOps** :
- Comprendre réseaux cloud (VPC, subnets, routing tables)
- Automatiser configurations réseau (Ansible, Terraform)
- Optimiser performances applications distribuées
- Implémenter Load Balancers

**Pour développeur** :
- Comprendre latence réseau et son impact sur applications
- Choisir protocoles adaptés (TCP vs UDP)
- Implémenter retry logic et timeouts
- Optimiser pour WAN (compression, caching)

<h3 class="section-title">Limites et ouvertures</h3>

**Limites du module** :
- Focus sur Cisco (marché plus diversifié : Juniper, Arista, etc.)
- Peu sur IPv6 (transition inévitable)
- Pas de SDN (Software-Defined Networking)
- Automatisation peu abordée

**Ouvertures vers** :
- **SDN et NFV** : virtualisation réseau, OpenFlow, contrôleurs
- **Cloud networking** : AWS VPC, Azure Virtual Networks
- **Automation** : Ansible, Python avec Netmiko/NAPALM
- **Monitoring** : SNMP, NetFlow, observabilité
- **5G et réseaux mobiles** : architecture, slicing

<h3 class="section-title">Évolutions récentes</h3>

**Software-Defined Networking (SDN)** :

Séparation du plan de contrôle (décisions de routage) et du plan de données (forwarding).

Contrôleur centralisé programmable via API.

**Network Functions Virtualization (NFV)** :

Fonctions réseau (firewall, load balancer) en logiciel plutôt que matériel dédié.

Flexibilité et réduction des coûts.

**Intent-Based Networking** :

Définir l'intention (politique) plutôt que configuration détaillée.

Le système traduit automatiquement l'intention en configuration.

**Automation et Infrastructure as Code** :

Configuration réseau déclarée dans des fichiers (Ansible, Terraform).

Versionning, reproductibilité, scalabilité.

**Réseaux 5G** :

Latence ultra-faible, haut débit, slicing (réseaux virtuels dédiés par usage).

<h3 class="section-title">Conseils pour réussir</h3>

**1. Pratiquer régulièrement** :
Utiliser Packet Tracer ou GNS3 pour reproduire scénarios et expérimenter configurations.

**2. Comprendre, pas mémoriser** :
Comprendre le fonctionnement des protocoles plutôt que mémoriser syntaxe CLI.

**3. Documenter ses configurations** :
Prendre notes des commandes, architectures déployées. Constituer un référentiel personnel.

**4. Utiliser Wireshark** :
Capturer et analyser trafic réel pour voir protocoles en action.

**5. Suivre la méthodologie de troubleshooting** :
Bottom-up (couche 1 → 7) ou top-down selon symptômes. Méthodique et systématique.

**6. Se certifier** :
Cisco CCNA est une certification reconnue validant compétences réseau de base.

<h3 class="section-title">Conclusion</h3>

Ce module est essentiel pour tout ingénieur travaillant avec des systèmes connectés. Les réseaux sont omniprésents : entreprises, datacenters, cloud, IoT, télécommunications.

**Compétences transférables** :
- Vision globale des architectures réseau
- Capacité à diagnostiquer et résoudre problèmes complexes
- Compréhension des compromis (performance, sécurité, coût)
- Maîtrise des protocoles universels (TCP/IP)

**Pertinence professionnelle** :
Les compétences réseau sont recherchées dans tous les secteurs. L'explosion du cloud, de l'IoT, et des applications distribuées accroît la demande d'ingénieurs réseau qualifiés.

**Message principal** :
Internet fonctionne grâce à des protocoles robustes et des ingénieurs compétents. Comprendre ces fondamentaux permet de concevoir, déployer et maintenir des infrastructures fiables et performantes.

**Recommandations** :
- Continuer la pratique (home lab avec vieux routeurs ou VMs)
- Se former sur automatisation (Python pour réseaux)
- Explorer SDN (contrôleurs OpenDaylight, ONOS)
- Suivre l'actualité (RFCs, blogs techniques, conférences)
- Envisager certifications (CCNA, CCNP, ou équivalents autres vendors)

**Liens avec les autres cours** :
- [Réseau - S5](./reseau.html) : bases TCP/IP
- [Cloud et Edge Computing - S9](./cloud-edge-computing.html) : réseaux virtuels
- [Embedded IA for IoT - S9](./embedded-ia-iot.html) : connectivité objets
- [Temps Réel - S8](./temps-reel.html) : contraintes temporelles
- [Cybersécurité](./cybersecurite.html) : sécurité réseau avancée

---

*Cours suivi en 2023-2024 à l'INSA Toulouse, Département Génie Électrique et Informatique.*

<div class="back-nav">
    <a href="./my-courses-2023-2024.html">← Retour aux Cours 2023-2024</a>
</div>

#### 2. Protocole IP - Adressage IPv4

**Format adresse**: 32 bits (4 octets)
Exemple: 192.168.1.1

**Classes** (obsolètes, remplacées par CIDR):
- Classe A: /8 (16M hôtes)
- Classe B: /16 (65k hôtes)
- Classe C: /24 (254 hôtes)

**CIDR** (Classless Inter-Domain Routing):
Notation: IP/préfixe
Exemple: 192.168.10.0/24 (256 adresses)

**Masque de sous-réseau**:
Détermine partie réseau vs hôte.
/24 → 255.255.255.0

**Adresses spéciales**:
- **Réseau**: tous bits hôte à 0 (192.168.1.0/24)
- **Broadcast**: tous bits hôte à 1 (192.168.1.255)
- **Loopback**: 127.0.0.1
- **Privées** (RFC 1918):
  - 10.0.0.0/8
  - 172.16.0.0/12
  - 192.168.0.0/16

**Sous-réseaux (Subnetting)**:
Diviser un réseau en sous-réseaux plus petits.

Exemple: 192.168.1.0/24 → 192.168.1.0/26, 192.168.1.64/26, etc.

#### 3. Protocole IPv6

**Format**: 128 bits (16 octets)
Notation: 8 groupes de 4 chiffres hexa séparés par :
Exemple: 2001:0db8:85a3:0000:0000:8a2e:0370:7334

**Simplifications**:
- Omettre zéros de tête: 2001:db8:85a3:0:0:8a2e:370:7334
- :: pour groupes consécutifs de zéros (une fois): 2001:db8::8a2e:370:7334

**Avantages vs IPv4**:
- Espace d'adressage énorme (2^128)
- Autoconfiguration (SLAAC)
- Pas de NAT nécessaire
- IPsec intégré
- En-tête simplifié (meilleure performance)

**Types d'adresses**:
- **Unicast**: adresse unique
- **Multicast**: groupe
- **Anycast**: plus proche d'un groupe

**Adresses spéciales**:
- **Loopback**: ::1
- **Link-local**: fe80::/10 (auto-configurées)
- **Unique local**: fc00::/7 (équivalent privé)

#### 4. Routage - Principes

**Table de routage**:
Associe destination → interface/next hop.

Entrées:
- Réseau destination
- Masque
- Passerelle (next hop)
- Interface de sortie
- Métrique

**Routage direct vs indirect**:
- Direct: destination sur réseau local
- Indirect: passer par routeur (gateway)

**Route par défaut** (default route):
0.0.0.0/0 → utilisée si aucune route spécifique.

**Processus de routage**:
1. Recevoir paquet
2. Consulter table de routage (longest prefix match)
3. Décrementer TTL
4. Recalculer checksum
5. Envoyer sur interface appropriée

#### 5. Protocoles de Routage Dynamique

**Classification**:

**IGP** (Interior Gateway Protocol): au sein d'un AS
- Distance Vector: RIP
- Link State: OSPF, IS-IS

**EGP** (Exterior Gateway Protocol): entre AS
- Path Vector: BGP

**RIP** (Routing Information Protocol):
- Métrique: nombre de sauts (max 15)
- Algorithme Bellman-Ford
- Envoie toute table toutes les 30s
- Convergence lente
- Simple mais limité (petits réseaux)

**OSPF** (Open Shortest Path First):
- Link State: chaque routeur connaît topologie complète
- Algorithme Dijkstra (SPF)
- Métrique: coût (fonction bande passante)
- Mise à jour déclenchée (pas périodique)
- Convergence rapide
- Hiérarchique (aires)
- Scalable (grands réseaux)

**Processus OSPF**:
1. Découverte voisins (Hello)
2. Échange LSA (Link State Advertisement)
3. Construction base de données topologique
4. Calcul SPF → arbre des plus courts chemins
5. Construction table de routage

**BGP** (Border Gateway Protocol):
- Protocole de routage d'Internet
- Path vector: chemins AS complets
- Politiques de routage complexes
- Métrique: pas seulement distance, mais préférences business
- eBGP (external) entre AS, iBGP (internal) dans AS

#### 6. Protocole TCP

**Caractéristiques**:
- Orienté connexion (3-way handshake)
- Fiable (accusés réception, retransmission)
- Contrôle de flux (fenêtre glissante)
- Contrôle de congestion
- Ordre préservé

**En-tête TCP**:
- Ports source/destination (16 bits chacun)
- Numéro de séquence (32 bits)
- Numéro d'accusé (32 bits)
- Fenêtre (16 bits): contrôle de flux
- Flags: SYN, ACK, FIN, RST, PSH, URG
- Checksum

**Établissement connexion (3-way handshake)**:
1. Client → Server: SYN
2. Server → Client: SYN+ACK
3. Client → Server: ACK

**Fermeture connexion**:
1. FIN
2. ACK
3. FIN
4. ACK

(Ou RST pour fermeture brutale)

**Contrôle de flux**:
Fenêtre glissante: récepteur annonce taille de buffer disponible.

**Contrôle de congestion**:
- **Slow Start**: augmentation exponentielle
- **Congestion Avoidance**: augmentation linéaire
- **Fast Retransmit**: 3 ACK dupliqués → retransmission immédiate
- **Fast Recovery**: après perte, ne pas redémarrer à 1

**Algorithmes**: Tahoe, Reno, New Reno, CUBIC (Linux par défaut)

#### 7. Protocole UDP

**Caractéristiques**:
- Sans connexion
- Non fiable (pas d'accusé, pas de retransmission)
- Pas de contrôle de flux ni congestion
- Ordre non garanti
- En-tête minimal (8 octets)

**Usage**:
- Applications temps réel (VoIP, streaming)
- DNS (requêtes courtes)
- DHCP, SNMP
- Jeux en ligne

**Avantage**: faible latence, overhead minimal

#### 8. Qualité de Service (QoS)

**Problématique**:
Réseau best-effort insuffisant pour applications exigeantes (VoIP, vidéo).

**Paramètres QoS**:
- **Bande passante**: débit garanti
- **Latence**: délai de transit
- **Gigue** (jitter): variation de latence
- **Perte**: taux de paquets perdus

**Mécanismes QoS**:

**Classification et marquage**:
Identifier type de trafic, marquer paquet (DSCP, CoS).

**Queuing** (files d'attente):
- **FIFO**: First In First Out (pas de priorité)
- **Priority Queuing**: files de priorités
- **WFQ** (Weighted Fair Queuing): partage équitable pondéré
- **CBWFQ** (Class-Based WFQ): WFQ par classe
- **LLQ** (Low Latency Queuing): priorité stricte + WFQ

**Shaping et Policing**:
- **Shaping**: lisser trafic, tamponner excédent
- **Policing**: limiter taux, rejeter/marquer excédent

**Admission Control**:
Accepter/refuser nouveaux flux selon ressources.

**Modèles**:
- **IntServ** (Integrated Services): RSVP, réservation par flux (complexe, peu déployé)
- **DiffServ** (Differentiated Services): classes de service, scalable

#### 9. VLAN (Virtual LAN)

**Principe**:
Segmenter logiquement un réseau physique.

**Avantages**:
- Isolation broadcast domains
- Sécurité (séparation trafic)
- Flexibilité (réorganisation sans recâblage)

**Tagging** (802.1Q):
Ajout tag 4 octets dans trame Ethernet.
- VLAN ID (12 bits): 4096 VLANs possibles
- Priority (3 bits): CoS

**Trunk vs Access**:
- **Access port**: un seul VLAN (non-tagged)
- **Trunk port**: multiple VLANs (tagged)

**Inter-VLAN routing**:
Communication entre VLANs via routeur (ou switch L3).

#### 10. Commutation (Switching)

**Principe**:
Forward trames Ethernet selon adresse MAC.

**Table CAM** (Content Addressable Memory):
Associe MAC → port.

**Apprentissage**:
Switch apprend MACs en observant adresses source.

**Forwarding**:
- MAC destination connue → forward sur port associé
- MAC inconnue → flood sur tous ports (sauf source)
- Broadcast/multicast → flood

**Spanning Tree Protocol (STP)**:
Évite boucles L2.
- Élection root bridge
- Blocage ports redondants
- Reconfiguration si panne

Variantes: RSTP (Rapid STP), MSTP (Multiple STP)

#### 11. NAT (Network Address Translation)

**Problématique**:
Pénurie adresses IPv4 publiques.

**Principe**:
Traduire adresses privées ↔ publiques.

**Types**:

**NAT statique**: mapping 1:1 (IP privée ↔ IP publique)

**NAT dynamique**: pool d'IPs publiques, allocation dynamique

**PAT** (Port Address Translation) / NAT overload:
Plusieurs IPs privées → 1 IP publique (différenciation par ports).

**Table NAT**:
IP:port privé ↔ IP:port public

**Limitations**:
- Casse end-to-end connectivity (problèmes P2P, VoIP)
- Complexité protocoles (FTP, SIP)
- Pas de serveur entrant sans port forwarding

**IPv6** rend NAT obsolète (adresses suffisantes).

#### 12. Sécurité Réseau

**Listes de Contrôle d'Accès (ACL)**:
Filtrer trafic selon critères (IP source/dest, ports, protocole).

**Types**:
- **Standard**: IP source uniquement
- **Étendue**: IP source/dest, ports, protocole

**Application**: interface routeur (in/out).

**Pare-feu (Firewall)**:
Filtrage plus avancé, inspection état (stateful).

**VPN** (Virtual Private Network):
Tunnel sécurisé sur Internet.
- **Site-to-Site**: interconnecter réseaux d'entreprise
- **Remote Access**: accès distant sécurisé

Protocoles: IPsec, SSL/TLS VPN

**Attaques courantes**:
- **DoS/DDoS**: saturation ressources
- **Spoofing**: usurpation d'adresse
- **Man-in-the-Middle**: interception communication
- **ARP poisoning**: table ARP corrompue

**Contre-mesures**:
- ACL, firewall
- Authentification (802.1X)
- Chiffrement (IPsec, TLS)
- IDS/IPS (Intrusion Detection/Prevention)

## PART D: ANALYTICAL PART

### Knowledge and Skills Mobilized

- Compréhension approfondie des protocoles TCP/IP
- Configuration routeurs et switches (Cisco IOS)
- Implémentation protocoles de routage (OSPF, BGP)
- Conception architectures réseau multi-sites
- Analyse de trafic (Wireshark)
- Diagnostic et troubleshooting réseau
- Implémentation QoS et optimisation performances
- Sécurisation infrastructures (ACL, VPN)
- Subnetting et planification d'adressage

### Self Evaluation

Ce cours a consolidé et approfondi mes connaissances réseau. La configuration pratique sur équipements Cisco a été formatrice: la théorie prend tout son sens quand on configure réellement des routeurs et qu'on observe les échanges protocolaires.

Les protocoles de routage dynamique (OSPF en particulier) sont fascinants. Comprendre comment des milliers de routeurs convergent vers une vision cohérente du réseau est impressionnant. Les détails d'implémentation (aires OSPF, types de LSA, élection DR/BDR) sont complexes mais essentiels pour administrer de grands réseaux.

TCP est un protocole remarquablement robuste. Les mécanismes de contrôle de flux et congestion permettent à Internet de fonctionner malgré l'hétérogénéité des réseaux et la congestion. Les algorithmes d'évolution (Tahoe → Reno → CUBIC) montrent une amélioration continue basée sur décennies d'expérience.

La QoS est cruciale pour applications temps réel, mais complexe à implémenter de bout en bout. Le modèle DiffServ est pragmatique mais nécessite coordination entre tous les opérateurs d'un chemin.

Les VLANs sont un outil puissant pour segmenter réseaux. J'ai compris l'importance de bien planifier l'architecture VLAN dès le départ (difficile à réorganiser après coup).

Le NAT, bien que solution transitoire pour pénurie IPv4, est omniprésent. Comprendre ses mécanismes et limitations est important. IPv6 résoudra théoriquement le problème, mais la transition est lente.

La sécurité réseau est un vaste domaine. ACLs et firewalls sont la base, mais insuffisants face aux menaces sophistiquées. La défense en profondeur (multiple couches de sécurité) est essentielle.

Les labs pratiques m'ont confronté à des problèmes réels: configurations qui ne fonctionnent pas du premier coup, bugs subtils, importance de la documentation. Le troubleshooting méthodique (modèle OSI bottom-up ou top-down) est une compétence clé.

### My Opinion

Ce cours est indispensable à l'ère connectée. Pratiquement tout système moderne repose sur des réseaux. Comprendre leur fonctionnement, savoir les concevoir et les administrer est une compétence très recherchée.

Points forts:
- Équilibre théorie/pratique
- Labs sur équipements réels (Cisco)
- Couverture complète des protocoles essentiels
- Lien avec problématiques réelles (QoS, sécurité)

Points à améliorer:
- Plus sur IPv6 (transition inévitable)
- SDN (Software-Defined Networking) et virtualisation réseau
- Cloud networking (AWS, Azure)
- Automatisation et programmabilité (Python, APIs)

Réflexions personnelles:

Les réseaux sont la colonne vertébrale de l'informatique moderne. Internet, ce "réseau de réseaux", est une des plus grandes réalisations technologiques. Les protocoles (IP, TCP, BGP) conçus il y a des décennies tiennent encore malgré la croissance exponentielle.

Cependant, les défis évoluent:
- **Scalabilité**: croissance continue du trafic (vidéo, IoT)
- **Latence**: applications exigeantes (cloud gaming, AR/VR)
- **Sécurité**: sophistication croissante des attaques
- **Efficacité énergétique**: data centers consomment beaucoup

Les évolutions en cours:
- **SDN**: séparation plan de contrôle et plan de données, programmabilité
- **NFV** (Network Functions Virtualization): fonctions réseau en logiciel
- **5G**: latence ultra-faible, massive IoT
- **QUIC**: nouveau protocole transport (basé UDP) intégrant TLS

Applications professionnelles:

Compétences réseau applicables dans nombreux domaines:
- **Administration réseau**: opérateur, entreprise, datacenter
- **Architecte réseau**: conception infrastructures
- **Ingénieur sécurité**: protection réseaux et données
- **DevOps**: automatisation, cloud, containers
- **IoT**: connectivité objets (LoRa, NB-IoT, 5G)
- **Télécoms**: opérateurs, équipementiers

Le réseau ne se limite plus aux seuls "ingénieurs réseau". Les développeurs doivent comprendre les implications réseau de leurs applications (latence, bande passante, fiabilité). L'approche DevOps intègre infrastructure et développement.

L'automatisation des réseaux (via Python, Ansible, APIs) transforme le métier. La configuration manuelle CLI cède place à Infrastructure-as-Code. Maîtriser programmation + réseaux est un profil très recherché.

En conclusion, ce cours fournit des bases solides sur les protocoles et architectures réseau. C'est un domaine en évolution constante, nécessitant veille technologique et formation continue. Mais les fondamentaux (TCP/IP, routage, commutation) restent pertinents et constituent la base pour comprendre les innovations futures.

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
    p {
        text-align: justify;
    }
</style>

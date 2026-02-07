---
layout: default
title:  "Emerging Network Technologies"
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

# Emerging Network Technologies - Semestre 9

**Annee academique** : 2024-2025
**Categorie** : Reseaux emergents et programmabilite reseau
**Enseignant** : S. Abdellatif

---

**Cours connexes**:
- [Cloud & Edge Computing - S9](./2024-10-03-cloud-edge.html) - SDN pour Cloud/Edge
- [Interconnexion Reseau - S8](../2023-2024/2024-10-03-interconnexion-reseau.html) - Fondamentaux reseaux

---

## PART A - Presentation Generale

<h3 class="section-title">Vue d'ensemble</h3>

Le cours "Emerging Network Technologies", dispense par S. Abdellatif a l'INSA Toulouse, explore les avancees majeures dans le domaine des technologies reseau. Il se concentre sur trois piliers fondamentaux des reseaux modernes : le **Software-Defined Networking (SDN)**, la **Network Functions Virtualization (NFV)** et le protocole **LISP (Locator/ID Separation Protocol)**. Ces technologies constituent la base de la transformation des infrastructures reseau traditionnelles vers des architectures programmables, flexibles et virtualisees.

Ce cours est particulierement pertinent dans le contexte actuel ou les reseaux traditionnels, bases sur des equipements proprietaires avec des plans de controle et de donnees integres, montrent leurs limites face aux exigences de scalabilite, d'agilite et d'automatisation des environnements cloud, IoT et 5G.

**Objectifs pedagogiques** :
- Comprendre la separation du plan de controle et du plan de donnees (paradigme SDN)
- Maitriser le protocole OpenFlow et son role dans l'architecture SDN
- Configurer et administrer Open vSwitch (OVS) pour la commutation virtuelle
- Deployer et programmer des controleurs SDN (Ryu, OpenDaylight, ONOS)
- Comprendre les principes de la NFV et l'architecture MANO
- Apprehender le protocole LISP et la separation identifiant/localisateur
- Developper des applications de controle reseau en mode reactif et proactif
- Concevoir des topologies SDN et gerer les problemes de boucles reseau

<h3 class="section-title">Position dans le cursus</h3>

Ce module s'appuie sur les bases acquises precedemment :
- **Reseau (S5)** : modele OSI, Ethernet, IP, TCP/UDP
- **Interconnexion Reseau (S8)** : routage (OSPF, BGP), VLANs, commutation, QoS
- **Architecture Materielle (S6)** : couche physique, signaux

Il prepare a :
- **Cloud et Edge Computing (S9)** : virtualisation, orchestration, Kubernetes
- **IoT (S9)** : protocoles specifiques, contraintes reseaux embarques
- **Carriere professionnelle** : ingenieur reseau, architecte SDN/NFV, DevOps reseau

<h3 class="section-title">Organisation du module</h3>

| Element | Volume | Description |
|---------|--------|-------------|
| Cours magistraux | ~10h | Theorie SDN, NFV, LISP, architectures |
| Travaux pratiques | ~12h | Configuration OVS, OpenFlow, controleurs Ryu |
| Projet/Rapport | - | Rapport SDN & NFV |

---

## PART B - Experience et Contexte

<h3 class="section-title">Environnement et contexte</h3>

Durant ce cours, j'ai travaille dans un environnement de laboratoire equipe de materiel professionnel pour l'experimentation SDN/OpenFlow. L'infrastructure comprenait :

- **4 commutateurs Pica8** compatibles OpenFlow, equipes de 48 ports Gigabit Ethernet chacun
- **12 PCs** equipes de multiples cartes Ethernet, servant de routeurs et/ou de machines Linux
- **Cables Ethernet** (paires torsadees non blindees avec connecteurs RJ45), croises et droits
- **Reseau de gestion** separe du reseau de donnees (mode "out-of-band")

Ce contexte permettait une immersion complete dans les architectures SDN reelles, loin des simulations simplifiees. La manipulation d'equipements physiques Pica8 avec Open vSwitch a donne une dimension concrete aux concepts theoriques. Le deploiement progressif, depuis un simple pont OVS jusqu'a une topologie maillees multi-commutateurs avec controleur centralise, a permis de comprendre chaque brique de l'architecture SDN.

<h3 class="section-title">Outils utilises</h3>

| Outil | Role | Utilisation |
|-------|------|-------------|
| **Open vSwitch (OVS)** | Commutateur virtuel | Creation de ponts logiques, gestion des flux |
| **Ryu** | Controleur SDN | Programmation d'applications de controle reseau |
| **ovs-vsctl** | CLI d'administration OVS | Configuration des ponts et ports |
| **ovs-ofctl** | CLI OpenFlow pour OVS | Installation/suppression de regles de flux |
| **Pica8 picOS** | Systeme d'exploitation des commutateurs | Mode OVS/OpenFlow |
| **Wireshark** | Analyseur de paquets | Observation des echanges OpenFlow |
| **Python** | Programmation | Developpement d'applications controleur Ryu |

<h3 class="section-title">Mon role</h3>

Dans ce cours, j'etais responsable de :
- Comprendre les principes du SDN, de la NFV et du protocole OpenFlow
- Configurer des instances OVS sur les commutateurs Pica8
- Installer manuellement des regles OpenFlow pour controler le comportement du reseau
- Attacher et configurer un controleur Ryu pour le management centralise
- Deployer des topologies reseau complexes (maillees) et gerer les problemes de boucles
- Analyser le comportement reactif et proactif du controleur
- Rediger un rapport technique sur SDN et NFV

---

## PART C - Aspects Techniques Detailles

<h3 class="section-title">1. Software-Defined Networking (SDN) - Principes fondamentaux</h3>

Le SDN represente un changement de paradigme fondamental dans l'architecture des reseaux. Dans les reseaux traditionnels, chaque equipement (routeur, commutateur) integre a la fois le **plan de controle** (decisions de routage, protocoles) et le **plan de donnees** (acheminement effectif des paquets). Cette architecture distribuee presente plusieurs limitations : complexite de gestion, manque de vision globale, difficulte d'evolution, et dependance aux equipements proprietaires.

**Architecture SDN a trois couches** :

Le SDN repose sur une architecture en trois couches distinctes :

| Couche | Nom | Role | Exemples |
|--------|-----|------|----------|
| **Couche Application** | Application Plane | Applications de controle reseau | Firewall, Load Balancer, QoS Manager |
| **Couche Controle** | Control Plane | Decisions de routage, vision globale | Ryu, OpenDaylight, ONOS, Floodlight |
| **Couche Infrastructure** | Data Plane | Acheminement des paquets selon les regles | Open vSwitch, commutateurs OpenFlow |

**Interfaces de communication** :

- **Southbound API (ex: OpenFlow)** : interface entre le controleur et les equipements reseau. Permet au controleur de programmer les tables de flux des commutateurs.
- **Northbound API (ex: REST API)** : interface entre le controleur et les applications. Permet aux applications de demander des services reseau au controleur.
- **Eastbound/Westbound** : communication entre controleurs distribues pour la scalabilite.

**Avantages du SDN** :
- **Programmabilite** : le reseau peut etre programme et automatise via des APIs
- **Vision globale** : le controleur centralise a une vue complete de la topologie
- **Agilite** : modification rapide du comportement reseau sans reconfigurer chaque equipement
- **Independance materielle** : separation entre le logiciel de controle et le materiel
- **Innovation acceleree** : possibilite de deployer de nouveaux services reseau en logiciel

<h3 class="section-title">2. Protocole OpenFlow</h3>

OpenFlow est le protocole standard de la **Southbound API** du SDN. Il definit la communication entre le controleur SDN et les commutateurs OpenFlow, permettant au controleur de programmer directement les tables de flux des equipements reseau.

**Principes de fonctionnement** :

Un commutateur OpenFlow possede une ou plusieurs **tables de flux (flow tables)**. Chaque entree dans une table de flux contient :

| Champ | Description |
|-------|-------------|
| **Match fields** | Criteres de correspondance (port entree, adresses MAC/IP, ports TCP/UDP, VLAN, etc.) |
| **Priority** | Priorite de la regle (regles avec priorite plus elevee evaluees en premier) |
| **Counters** | Compteurs de paquets et d'octets correspondants |
| **Instructions/Actions** | Actions a effectuer (forward, drop, modifier en-tete, envoyer au controleur) |
| **Timeouts** | Duree de validite de la regle (idle timeout, hard timeout) |
| **Cookie** | Identifiant opaque defini par le controleur |

**Processus de traitement d'un paquet** :

1. Un paquet arrive sur un port du commutateur
2. Le commutateur compare les champs du paquet aux entrees de la table de flux
3. Si une correspondance est trouvee : executer les actions associees
4. Si aucune correspondance : envoyer un message **Packet-In** au controleur
5. Le controleur analyse le paquet et repond avec un **Packet-Out** ou installe une nouvelle regle via **Flow-Mod**

**Messages OpenFlow principaux** :

| Message | Direction | Description |
|---------|-----------|-------------|
| **Packet-In** | Switch → Controleur | Notification d'un paquet sans correspondance |
| **Packet-Out** | Controleur → Switch | Instruction de traitement pour un paquet |
| **Flow-Mod** | Controleur → Switch | Ajout/modification/suppression d'une regle de flux |
| **Hello** | Bidirectionnel | Etablissement de la connexion OpenFlow |
| **Features-Request/Reply** | Bidirectionnel | Decouverte des capacites du commutateur |
| **Stats-Request/Reply** | Bidirectionnel | Consultation des statistiques |

**Versions OpenFlow** : 1.0 (basique, une seule table), 1.3 (tables multiples, groupes, metres), 1.4, 1.5 (dernieres evolutions).

<h3 class="section-title">3. Open vSwitch (OVS) - Commutation virtuelle</h3>

Open vSwitch est un commutateur virtuel multi-couches concu pour permettre l'automatisation reseau par extensions programmables. Il supporte les protocoles de gestion standard (OpenFlow, sFlow, SPAN, LACP, 802.1Q) et est largement deploye dans les environnements de virtualisation et de cloud computing.

**Architecture OVS** :
- **ovsdb-server** : serveur de base de donnees de configuration
- **ovs-vswitchd** : daemon principal du commutateur, gere les tables de flux
- **ovs-vsctl** : outil CLI pour la configuration (ponts, ports, controleurs)
- **ovs-ofctl** : outil CLI pour la gestion des flux OpenFlow

**Configuration initiale d'un pont OVS** :

Creation d'une instance de pont logique et attachement des ports physiques :

```bash
# Redemarrage des processus OVS
sudo service picos restart

# Verification des processus
ps -A   # verifier ovsdb-server et ovs-vswitchd

# Creation d'un pont OVS
admin@picOS-OVS$ ovs-vsctl add-br br0 -- set bridge br0 datapath_type=pica8

# Attachement des ports physiques au pont
admin@picOS-OVS$ ovs-vsctl add-port br0 ge-1/1/10 -- set interface ge-1/1/10 type=pica8
admin@picOS-OVS$ ovs-vsctl add-port br0 ge-1/1/13 -- set interface ge-1/1/13 type=pica8
admin@picOS-OVS$ ovs-vsctl add-port br0 ge-1/1/16 -- set interface ge-1/1/16 type=pica8

# Verification de la configuration
admin@picOS-OVS$ ovs-vsctl show
admin@picOS-OVS$ ovs-ofctl show br0
admin@picOS-OVS$ ovs-ofctl dump-ports br0
```

**Comportement par defaut** :

Sans regle explicite, le pont OVS ne sait pas comment acheminer les paquets. On peut ajouter une regle par defaut qui transforme le commutateur en switch L2 classique :
```bash
admin@picOS-OVS$ ovs-ofctl add-flow br0 ,action=normal
```

<h3 class="section-title">4. Installation manuelle de regles OpenFlow</h3>

L'installation manuelle de regles OpenFlow permet de comprendre finement le mecanisme de programmation du plan de donnees. Plusieurs niveaux de granularite sont possibles.

**Niveau 1 - Regles basees sur le port d'entree** :

Regles simples redirigeant le trafic d'un port vers d'autres ports, sans distinction de contenu :

```bash
# Suppression de toutes les regles existantes
admin@picOS-OVS$ ovs-ofctl del-flows br0

# Regles de redirection basees sur les ports d'entree
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=10,actions=output:13,16
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=13,actions=output:10,16
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=16,actions=output:10,13
```

**Niveau 2 - Regles avec filtrage IP (granularite fine)** :

Pour un controle plus precis, on filtre par adresse IP de destination, avec gestion separee de l'ARP :

```bash
admin@picOS-OVS$ ovs-ofctl del-flows br0

# Regles ARP pour la resolution d'adresses
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=10,arp,actions=output:13,16
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=13,arp,actions=output:10,16
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=16,arp,actions=output:10,13

# Regles IP avec filtrage par destination
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=10,ip,nw_dst=128.0.0.4,actions=output:13
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=10,ip,nw_dst=128.0.0.5,actions=output:16
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=13,ip,nw_dst=128.0.0.3,actions=output:10
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=13,ip,nw_dst=128.0.0.5,actions=output:16
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=16,ip,nw_dst=128.0.0.3,actions=output:10
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=16,ip,nw_dst=128.0.0.4,actions=output:13
```

**Niveau 3 - Regles applicatives (filtrage protocolaire)** :

Pour un controle au niveau applicatif, on filtre sur les protocoles de transport et les ports :

```bash
# Autoriser le trafic UDP CoAP (port 5683) entre la Gateway et les devices
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=16,udp,tp_dst=5683,actions=output:10,13
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=10,udp,tp_dst=5683,actions=output:16
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=13,udp,tp_dst=5683,actions=output:16

# Autoriser les sessions SSH (port 22) de la Gateway vers les devices
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=16,tcp,tp_dst=22,actions=output:10,13
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=10,tcp,tp_src=22,actions=output:16
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=13,tcp,tp_src=22,actions=output:16
```

Cette progression illustre la puissance d'OpenFlow : depuis le simple routage par port jusqu'au controle fin des flux applicatifs, le reseau devient entierement programmable.

<h3 class="section-title">5. Attachement du controleur et controle SDN</h3>

L'attachement d'un controleur OpenFlow (ici Ryu) permet de passer d'un reseau statiquement configure a un reseau dynamiquement controle.

**Mode out-of-band** :

Le trafic OpenFlow entre le controleur et les commutateurs est transporte par un reseau different de celui utilise pour les donnees utilisateur. Cela garantit que le canal de controle reste disponible meme en cas de congestion du reseau de donnees.

```bash
# Configuration de l'interface du controleur sur le reseau de gestion
ifconfig eth1 192.168.0.42

# Declaration du controleur pour le pont br0
admin@picOS-OVS$ ovs-vsctl set-controller br0 tcp:192.168.0.42:6633

# Demarrage du controleur Ryu en mode verbose
controleur# ryu-manager --verbose

# Verification de la connexion
admin@picOS-OVS$ ovs-vsctl show
admin@picOS-OVS$ ovs-ofctl snoop br0
admin@picOS-OVS$ ovs-ofctl dump-flows br0
```

**Fonctionnement du controleur** :

Sans application lancee, le controleur recoit les evenements Packet-In mais ne propose aucun traitement. Les paquets sont donc perdus car aucune regle n'est installee dans les tables de flux.

<h3 class="section-title">6. Programmation reseau reactive et proactive</h3>

Deux approches fondamentales pour la programmation de controleurs SDN :

**Mode reactif** :

Le controleur reagit aux evenements reseau en temps reel. Lorsqu'un paquet arrive sans correspondance dans la table de flux, un Packet-In est envoye au controleur qui decide alors de l'action a entreprendre et installe eventuellement une regle pour les paquets similaires futurs.

L'application **simple_switch_14** illustre ce mode :

```bash
# Lancement de l'application simple_switch
controleur# ryu-manager --verbose simple_switch_14.py

# Verification des regles installees apres un ping
admin@picOS-OVS$ ovs-ofctl dump-flows br0
```

Le comportement de simple_switch_14 :
1. Reception d'un Packet-In pour un paquet dont le destinataire est inconnu
2. L'application demande au commutateur de diffuser le paquet sur tous les ports (flood)
3. Lorsque le destinataire repond, l'application apprend sa localisation (adresse MAC associee a un port)
4. Une regle est ajoutee dans la table de flux pour diriger les futurs paquets directement

**Mode proactif** :

Le controleur pre-configure les regles de flux avant l'arrivee du trafic, en anticipant les schemas de trafic attendus. Ce mode offre de meilleures performances (pas de latence Packet-In) mais necessite une connaissance prealable de la topologie et des flux.

```bash
# Exemple de regle proactive pour un flux specifique
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=16,ip,nw_dst=128.0.0.4,actions=output:13
```

| Critere | Mode reactif | Mode proactif |
|---------|-------------|---------------|
| **Latence** | Premier paquet retarde (Packet-In) | Aucune latence supplementaire |
| **Flexibilite** | Tres flexible, s'adapte dynamiquement | Necessite connaissance prealable |
| **Charge controleur** | Elevee (traite chaque nouveau flux) | Faible (configuration initiale) |
| **Tolerance aux pannes** | Dependant du controleur | Flux continues meme si controleur down |
| **Cas d'usage** | Reseaux dynamiques, apprentissage | Trafic previsible, performance critique |

<h3 class="section-title">7. Topologie maillee et prevention des boucles</h3>

L'exercice final du TP consistait a deployer une topologie partiellement maillee avec 4 commutateurs Pica8 interconnectes. Chaque commutateur hebergeait une instance de pont OVS, connectee a une machine terminale et a deux autres ponts sur d'autres commutateurs.

**Problematique des boucles** :

Lorsque tous les liens sont actifs dans une topologie maillee, des boucles de couche 2 se forment. L'application simple_switch, qui utilise le flooding pour les adresses inconnues, provoque une amplification infinie des trames broadcast (tempete de broadcast). Cela rend le reseau inutilisable.

**Solutions** :

La solution consiste a utiliser une application de controle integrant la gestion des boucles, similaire au Spanning Tree Protocol (STP) mais implementee au niveau du controleur SDN. Dans le repertoire de Ryu, des applications plus avancees comme **simple_switch_stp** integrent la detection et la prevention des boucles en bloquant les ports redondants.

Cette situation illustre un avantage majeur du SDN : au lieu de s'appuyer sur des protocoles distribues comme STP (convergence lente, configuration complexe), le controleur centralise peut calculer un arbre couvrant optimal grace a sa vision globale de la topologie.

<h3 class="section-title">8. Controleurs SDN - Ecosysteme</h3>

Plusieurs controleurs SDN sont disponibles, chacun avec ses specificites :

| Controleur | Langage | Licence | Caracteristiques |
|------------|---------|---------|------------------|
| **Ryu** | Python | Apache 2.0 | Leger, pedagogique, extensible, facile a programmer |
| **OpenDaylight (ODL)** | Java | Eclipse Public | Tres complet, modulaire, support industriel (Linux Foundation) |
| **ONOS** | Java | Apache 2.0 | Haute disponibilite, oriente operateurs telecom |
| **Floodlight** | Java | Apache 2.0 | Developpe par Big Switch Networks, performant |
| **POX** | Python | Apache 2.0 | Predecessor de Ryu, utilise en recherche |

**Ryu en detail** :

Ryu est un framework de controleur SDN base sur composants, ecrit en Python. Il fournit des APIs bien definies pour creer des applications de gestion reseau. Il supporte differentes versions d'OpenFlow (1.0 a 1.5) et offre une bibliotheque riche pour le parsing de paquets, la manipulation de flux, et l'interaction avec les commutateurs.

<h3 class="section-title">9. Network Functions Virtualization (NFV)</h3>

La NFV est une approche architecturale qui consiste a virtualiser les fonctions reseau traditionnellement realisees par des equipements materiels dedies (appliances proprietaires). Au lieu de deployer un pare-feu physique, un load balancer materiel ou un systeme IDS dedie, ces fonctions sont implementees en logiciel et executees sur des serveurs standards (COTS - Commercial Off-The-Shelf).

**Problematique des reseaux traditionnels** :
- Chaque fonction reseau necessite un equipement dedie et couteux
- Scalabilite limitee (achat de nouveau materiel pour augmenter la capacite)
- Cycle de deploiement long (commande, installation, configuration)
- Innovation freinee par les cycles produit des equipementiers
- Dependance aux solutions proprietaires (vendor lock-in)

**Fonctions Reseau Virtualisees (VNF)** :

Les VNFs sont les implementations logicielles des fonctions reseau :

| Fonction traditionnelle | VNF equivalente |
|------------------------|-----------------|
| Pare-feu materiel | vFirewall |
| Load Balancer physique | vLoad Balancer |
| Routeur physique | vRouter |
| IDS/IPS materiel | vIDS/vIPS |
| WAN Optimizer | vWAN Optimizer |
| DPI appliance | vDPI |

**Cycle de vie des VNFs** :

1. **Instantiation** : deploiement de la VNF sur l'infrastructure virtuelle
2. **Configuration** : parametrage initial de la fonction
3. **Scaling** : mise a l'echelle (scale-up/scale-down, scale-in/scale-out)
4. **Monitoring** : supervision des performances et de la sante
5. **Update/Upgrade** : mise a jour du logiciel sans interruption
6. **Termination** : arret et liberation des ressources

**Avantages de la NFV** :
- **Reduction des couts** : utilisation de serveurs standards (COTS)
- **Agilite** : deploiement et mise a l'echelle en minutes au lieu de semaines
- **Flexibilite** : fonctions deployees la ou necessaire, quand necessaire
- **Innovation** : cycle de developpement logiciel rapide
- **Multi-vendor** : independance vis-a-vis des equipementiers

<h3 class="section-title">10. Architecture MANO (Management and Orchestration)</h3>

L'architecture MANO, definie par l'ETSI (European Telecommunications Standards Institute), est le cadre de reference pour la gestion et l'orchestration des environnements NFV.

**Composants principaux de l'architecture MANO** :

| Composant | Role |
|-----------|------|
| **NFV Orchestrator (NFVO)** | Orchestration globale des services reseau, gestion du cycle de vie des Network Services |
| **VNF Manager (VNFM)** | Gestion du cycle de vie des VNFs individuelles (instantiation, scaling, termination) |
| **Virtualized Infrastructure Manager (VIM)** | Gestion de l'infrastructure virtuelle (compute, storage, network) - ex: OpenStack |
| **NFV Infrastructure (NFVI)** | Ressources physiques et virtuelles (serveurs, stockage, reseau) |
| **Element Management System (EMS)** | Gestion fonctionnelle des VNFs (configuration specifique a la fonction) |
| **OSS/BSS** | Systemes de support operationnel et commercial |

**Service Chaining (chaine de services)** :

Le Service Chaining consiste a connecter sequentiellement plusieurs VNFs pour creer un service reseau complet. Par exemple, le trafic d'un utilisateur peut traverser successivement :
1. vFirewall (filtrage)
2. vDPI (inspection approfondie)
3. vLoad Balancer (repartition de charge)
4. Application serveur

Le SDN facilite grandement le Service Chaining en permettant de programmer dynamiquement le chemin des flux a travers les differentes VNFs.

<h3 class="section-title">11. Protocole LISP (Locator/ID Separation Protocol)</h3>

LISP est un protocole reseau qui separe l'identifiant d'un hote de sa localisation dans le reseau. Dans l'architecture IP traditionnelle, l'adresse IP joue un double role : elle identifie l'hote ET indique sa localisation topologique. Cette ambiguite pose des problemes pour la mobilite, le multi-homing et la scalabilite des tables de routage.

**Concepts fondamentaux** :

| Concept | Description |
|---------|-------------|
| **EID (Endpoint Identifier)** | Identifiant de l'hote (adresse IP de l'hote, stable) |
| **RLOC (Routing Locator)** | Localisateur dans le reseau (adresse IP du routeur de bordure) |
| **ITR (Ingress Tunnel Router)** | Routeur d'entree qui encapsule les paquets |
| **ETR (Egress Tunnel Router)** | Routeur de sortie qui desencapsule les paquets |
| **Map-Server** | Serveur de correspondance EID → RLOC |
| **Map-Resolver** | Serveur qui resout les requetes de mapping |

**Fonctionnement** :

1. Un hote source envoie un paquet vers un EID destination
2. L'ITR interroge le systeme de mapping pour obtenir le RLOC associe a l'EID destination
3. L'ITR encapsule le paquet original dans un nouveau paquet IP avec le RLOC comme destination
4. Le paquet traverse le reseau de coeur en utilisant les RLOC
5. L'ETR desencapsule le paquet et le delivre a l'hote destination

**Avantages de LISP** :
- **Reduction des tables de routage** : seuls les RLOC sont annonces dans le coeur du reseau
- **Mobilite** : un hote peut changer de localisation (RLOC) sans changer son identite (EID)
- **Multi-homing** : un EID peut etre associe a plusieurs RLOC pour la redondance
- **Ingenierie de trafic** : selection du meilleur RLOC selon les metriques

<h3 class="section-title">12. Programmabilite reseau et API</h3>

La programmabilite est au coeur de la transformation des reseaux modernes. Le SDN et la NFV convergent pour creer des reseaux entierement automatisables et programmables.

**Niveaux de programmabilite** :

- **Configuration automatisee** : scripts et outils (Ansible, Puppet, Chef) pour deployer des configurations
- **Controleurs SDN** : programmation du comportement reseau via applications Python/Java
- **APIs REST** : interfaces standardisees pour interagir avec les controleurs et les VNFs
- **Intent-Based Networking** : expression de l'intention (politique de haut niveau) traduite automatiquement en configuration

**Convergence SDN + NFV** :

SDN et NFV sont complementaires :
- Le SDN fournit la **programmabilite du reseau** (plan de donnees)
- La NFV fournit la **virtualisation des fonctions** (plan de services)
- Ensemble, ils permettent de creer des infrastructures reseau entierement logicielles, agiles et automatisees

Cette convergence est au coeur des architectures reseau 5G, ou le network slicing repose sur la capacite a creer des tranches de reseau virtuelles avec des VNFs specifiques, interconnectees par un plan de donnees SDN.

---

## PART D - Analyse et Reflexion

<h3 class="section-title">Competences acquises</h3>

**Comprehension du paradigme SDN** :
Maitrise de la separation plan de controle / plan de donnees, du protocole OpenFlow et de l'architecture a trois couches. Capacite a expliquer les avantages et les limites du SDN par rapport aux reseaux traditionnels.

**Configuration Open vSwitch** :
Competence pratique dans la creation de ponts logiques, l'attachement de ports physiques et la gestion d'instances OVS sur des equipements Pica8 reels.

**Programmation de regles OpenFlow** :
Capacite a installer des regles de flux a differents niveaux de granularite : port d'entree, adresses IP, protocoles de transport, ports applicatifs. Comprehension de l'impact de la granularite sur la precision du controle et les performances.

**Deploiement de controleurs SDN** :
Experience avec le controleur Ryu, depuis le lancement en mode verbose jusqu'a l'execution d'applications de controle (simple_switch_14). Comprehension du fonctionnement reactif et proactif.

**Gestion de topologies complexes** :
Experience du deploiement de topologies maillees multi-commutateurs et comprehension des problemes de boucles et de leurs solutions dans un contexte SDN.

**Comprehension NFV et MANO** :
Connaissance de l'architecture de virtualisation des fonctions reseau, du cycle de vie des VNFs et du cadre MANO pour l'orchestration.

<h3 class="section-title">Auto-evaluation</h3>

J'ai trouve le cours "Emerging Network Technologies" tres engageant et formateur, bien que certains aspects aient ete un peu complexes pour moi en tant qu'etudiant specialise en Electronique Automatique par rapport a ceux de l'option Reseau. Malgre cela, j'ai ete activement implique dans la simulation de topologies et le test de divers aspects, ce qui m'a fourni une comprehension pratique de la facon dont ces technologies transforment la gestion des reseaux.

Le travail sur les equipements Pica8 reels a ete la partie la plus enrichissante. Manipuler des commutateurs physiques, installer des regles OpenFlow et observer leur effet immediat sur la connectivite donne une dimension concrete que les simulations ne peuvent pas offrir.

Le principal defi a ete la comprehension de la topologie maillee et la gestion des boucles. Voir le reseau devenir instable avec l'ajout d'un seul lien physique m'a fait comprendre l'importance critique de la prevention des boucles et la puissance du controleur SDN pour resoudre ce probleme de maniere centralisee.

Comme je suis egalement le [Master REOC](./master-reoc.html), j'avais deja travaille sur SDN et Ryu dans un contexte plus exploratoire. Ce cours a solidifie mes competences avec une approche plus structuree et progressive. En REOC, nous avions mene notre propre recherche et projet, ce qui offrait une experience plus pratique mais moins guidee.

<h3 class="section-title">Perspectives professionnelles</h3>

Les technologies emergentes vues dans ce cours sont au coeur de la transformation des infrastructures reseau :

- **Operateurs telecom** : deploiement 5G avec network slicing (SDN + NFV)
- **Cloud providers** : reseaux virtuels (VPC) et SDN pour multi-tenancy
- **Entreprises** : SD-WAN pour connecter les sites distants avec agilite
- **Data centers** : automatisation des reseaux de datacenter avec SDN
- **IoT** : gestion intelligente des flux IoT via controleurs SDN

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
      <h4>Chapitre 1 - Introduction aux reseaux emergents</h4>
      <p>Cours introductif : problematiques des reseaux traditionnels, evolution vers SDN et NFV, enjeux de la programmabilite reseau.</p>
      <embed src="/cours-pdf/S9/Reseau-Emergent/2023.ch1.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/Reseau-Emergent/2023.ch1.pdf" target="_blank">Telecharger le chapitre 1</a></p>
    </div>
    <div class="pdf-item">
      <h4>Chapitre 2 - Software-Defined Networking (SDN)</h4>
      <p>Cours approfondi sur le SDN : architecture, protocole OpenFlow, controleurs, programmation reactive et proactive.</p>
      <embed src="/cours-pdf/S9/Reseau-Emergent/2023.Ch2-SDN.english.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/Reseau-Emergent/2023.Ch2-SDN.english.pdf" target="_blank">Telecharger le chapitre 2 - SDN</a></p>
    </div>
    <div class="pdf-item">
      <h4>Chapitre 3 - Introduction a LISP</h4>
      <p>Cours sur le protocole LISP : separation identifiant/localisateur, architecture ITR/ETR, systeme de mapping EID-RLOC.</p>
      <embed src="/cours-pdf/S9/Reseau-Emergent/Ch3-Intro-LISP.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/Reseau-Emergent/Ch3-Intro-LISP.pdf" target="_blank">Telecharger le chapitre 3 - LISP</a></p>
    </div>
  </div>
</div>

---

## Rapports et Projets

<div style="text-align: center;">
    <h3 class="section-title">Rapport SDN & NFV</h3>
</div>

<div class="pdf-container">
  <div class="pdf-item" style="min-width: 100%;">
    <h4>Rapport de projet - SDN et NFV</h4>
    <p>Rapport technique detaillant les travaux pratiques sur le Software-Defined Networking et la Network Functions Virtualization.</p>
    <embed src="/file/reports/S9/Chanfreau_SDN_NFV_Report.pdf" type="application/pdf" width="100%" height="800px" />
    <p><a href="/file/reports/S9/Chanfreau_SDN_NFV_Report.pdf" target="_blank">Ouvrir le rapport complet</a></p>
  </div>
</div>

<div class="pdf-container">
  <div class="pdf-item" style="min-width: 100%;">
    <h4>Sujet de TP - Emerging Network</h4>
    <p>Sujet du TP couvrant la configuration OVS, les regles OpenFlow, l'attachement du controleur Ryu et le deploiement de topologies maillees.</p>
    <embed src="/img/BE_Emerging_Network/Lab_Subject_emerging.pdf" type="application/pdf" width="100%" height="800px" />
    <p><a href="/img/BE_Emerging_Network/Lab_Subject_emerging.pdf" target="_blank">Ouvrir le sujet de TP</a></p>
  </div>
</div>

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
    p {
        text-align: justify;
    }
</style>

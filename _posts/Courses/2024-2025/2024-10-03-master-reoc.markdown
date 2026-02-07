---
layout: default
title:  "Master REOC"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

<a href="./my-courses-2024-2025.html" class="back-nav">Retour aux cours 2024-2025</a>

---

<h1 class="section-title">Master 2 REOC - Reseaux et Objets Connectes</h1>

## PART A : PRESENTATION GENERALE

### Presentation du Master REOC

Le **Master 2 REOC** (Reseaux et Objets Connectes) est une formation dispensee a l'**ENSEEIHT** (Ecole Nationale Superieure d'Electrotechnique, d'Electronique, d'Informatique, d'Hydraulique et des Telecommunications) de Toulouse, dans le cadre d'un **double diplome avec l'INSA Toulouse**. Cette formation s'inscrit dans le semestre S9 de l'annee 2024-2025.

Ce programme intensif couvre un large spectre de technologies liees aux reseaux embarques et aux objets connectes. Il offre une vision approfondie des architectures reseau modernes, allant de la virtualisation des reseaux (SDN, NFV) aux reseaux temps reel pour l'aeronautique (AFDX, IMA), en passant par les reseaux bas debit pour l'IoT (LoRaWAN) et les processus stochastiques appliques a l'evaluation de performances.

Le cursus est organise en une dizaine de modules complementaires qui permettent de maitriser les aspects theoriques et pratiques des systemes en reseau embarques. L'approche pedagogique allie cours magistraux, travaux pratiques et projets de mise en situation reelle.

### Objectifs de la formation
- Concevoir et deployer des architectures reseau virtualisees (SDN/NFV)
- Comprendre et implementer des protocoles de communication temps reel pour les systemes embarques critiques
- Evaluer les performances des reseaux a travers la simulation et la modelisation stochastique
- Maitriser les technologies de communication bas debit pour l'Internet des Objets
- Apprehender les architectures modulaires integrees pour l'avionique

---

## PART B : EXPERIENCE ET CONTEXTE

### Environnement et contexte

Le Master REOC m'a plonge dans un environnement academique exigeant, mele a l'ENSEEIHT de Toulouse, en parallele de mes cours a l'INSA. Cette double formation a necessite une grande capacite d'organisation et d'adaptation. Les travaux pratiques etaient realises sur des plateformes variees : environnements virtualises avec Docker et Containernet, programmation P4 pour le data plane, simulateurs LoRaWAN en Python, et outils de simulation reseau avec NetworkX.

Le contexte etait celui d'une immersion complete dans les problematiques actuelles des reseaux : comment virtualiser les fonctions reseau, comment garantir le determinisme dans les communications embarquees, comment optimiser les performances des reseaux IoT a grande echelle, et comment modeliser mathematiquement le comportement des systemes en file d'attente.

### Mon role et mes responsabilites
- **Conception d'architectures reseau** : mise en place de topologies SDN avec Containernet, deploiement de conteneurs Docker pour simuler des equipements reseau
- **Programmation du data plane** : implementation de parseurs et de tables de correspondance en langage P4 pour le traitement AFDX
- **Developpement d'outils de monitoring** : creation d'interfaces de surveillance et d'adaptation du trafic via les API de controleurs SDN (Ryu)
- **Simulation et evaluation de performances** : modelisation de reseaux avec NetworkX, simulation de deploiements LoRaWAN, et calcul de metriques de performance par processus stochastiques
- **Redaction de rapports techniques** : documentation detaillee des projets realises, notamment le projet SDCI et le rapport sur les processus stochastiques

### Collaboration
La majorite des projets a ete realisee en binome avec **Yohan Boujon**, un partenaire de confiance avec lequel la collaboration etait fluide et efficace. Notre complementarite nous a permis de mener a bien les travaux pratiques dans les delais impartis, malgre la charge de travail consequente liee au double diplome.

---

## PART C : ASPECTS TECHNIQUES

Cette section detaille les differents modules du Master REOC, couvrant les aspects theoriques et pratiques de chaque thematique abordee.

---

### 1. Virtualisation des Reseaux Embarques et P4

Ce module abordait la virtualisation des reseaux dans un contexte embarque, avec un focus sur le **protocole AFDX** (Avionics Full-Duplex Switched Ethernet) utilise dans l'aeronautique. L'objectif etait de comprendre comment programmer le plan de donnees d'un commutateur reseau en utilisant le langage **P4** (Programming Protocol-Independent Packet Processors).

Le TP portait sur l'implementation d'un commutateur AFDX en P4, ou les trames sont routees en fonction de leur **Virtual Link (VL)**. Voici la structure de la trame AFDX definie en P4 :

```p4
header_type afdx_frame_t {
  fields {
  	const: 32;
  	vl: 16;
  	source: 48;
  	type: 16;
  }
}

header afdx_frame_t afdx_frame;

parser start {
       return parse_afdx_frame;
}

parser parse_afdx_frame {
	extract(afdx_frame);
	return select(afdx_frame.const) {
		0x03000000: ingress;
	}
}

table table_afdx{
	reads{
		afdx_frame.vl : exact;
	}
	actions{
		compute_afdx;
		_drop;
	}
}

action compute_afdx(port){
	modify_field(standard_metadata.egress_spec, port);
}
```

La topologie etait simulee avec **Mininet** et le commutateur comportemental de P4, permettant de tester le routage des trames AFDX selon les Virtual Links configures.

**Concepts cles** : Plan de donnees programmable, AFDX, Virtual Links, P4, Mininet, SDN pour l'embarque, Time-Sensitive Networking (TSN).

---

### 2. Information Centric Networking (ICN/NDN)

Le module sur l'**Information Centric Networking** (ICN), et plus specifiquement le paradigme **Named Data Networking** (NDN), proposait une vision radicalement differente des reseaux par rapport au modele IP classique. Au lieu de connecter des machines entre elles, le NDN centre les communications sur les **donnees elles-memes** : on ne demande plus "connecte-moi a telle machine" mais plutot "donne-moi tel contenu".

Les principes fondamentaux etudies :
- **Interest / Data** : le consommateur envoie un paquet "Interest" portant le nom du contenu souhaite, et le reseau achemine un paquet "Data" en reponse
- **Content Store (CS)** : chaque noeud du reseau peut mettre en cache les donnees traversantes, permettant de servir les requetes futures localement
- **Pending Interest Table (PIT)** : table qui enregistre les Interest non encore satisfaits et les interfaces par lesquelles ils sont arrives
- **Forwarding Information Base (FIB)** : equivalent de la table de routage, mais basee sur les noms de contenus

Ce paradigme presente des avantages significatifs pour les reseaux embarques et IoT : reduction de la latence grace au cache distribue, mobilite native des producteurs et consommateurs, et securite integree au niveau des donnees (chaque paquet Data est signe par le producteur).

**Concepts cles** : NDN, ICN, Content Store, PIT, FIB, routage par nom, cache distribue, securite centree donnees.

---

### 3. Software Defined Networking (SDN) - INSA

Le module SDN a l'INSA approfondissait les concepts de **separation du plan de controle et du plan de donnees** dans les reseaux. Le cours couvrait les architectures SDN, le protocole **OpenFlow**, et l'utilisation de controleurs SDN tels que **Ryu** pour programmer le comportement du reseau de maniere centralisee.

Les travaux pratiques portaient sur la mise en place d'une architecture SDN complete avec :
- Configuration de topologies reseau avec des commutateurs OpenFlow
- Programmation de regles de flux via le controleur Ryu
- Implementation de politiques de routage et de filtrage du trafic
- Analyse du comportement du reseau en temps reel

**Concepts cles** : OpenFlow, controleur SDN, Ryu, plan de controle centralise, regles de flux, QoS, slicing reseau.

---

### 4. Wireless Real-Time Networking

Ce module traitait des **reseaux sans fil temps reel**, une thematique essentielle pour les systemes embarques critiques dans les domaines de l'IoT industriel (IIoT) et de l'aeronautique. Le cours couvrait les protocoles et mecanismes permettant de garantir des communications deterministes sur des supports sans fil intrinsiquement non deterministes.

Les thematiques abordees incluaient :
- **Reseaux temps reel embarques** : contraintes de latence, gigue et fiabilite
- **Ad Hoc Networks** : protocoles de routage distribues pour les reseaux sans infrastructure
- **IIoT (Industrial Internet of Things)** : application des reseaux temps reel au contexte industriel, avec des contraintes de securite et de surete
- **Wireless Sensor and Actuator Networks (WSAN)** : protocoles de communication pour les reseaux de capteurs-actionneurs

L'etude de papiers de recherche recents permettait de comprendre les defis actuels : comment concilier les exigences temps reel avec les aleas du canal radio, comment dimensionner un reseau sans fil pour garantir un taux de livraison minimum, et comment integrer ces reseaux dans des architectures industrielles existantes.

**Concepts cles** : Determinisme, latence bornee, reseaux ad hoc, TDMA, ordonnancement, IIoT, WSAN.

---

### 5. Projet NFV/SDCI

Le projet **NFV/SDCI** (Network Function Virtualization / Software Defined Cloud Infrastructure) constituait le projet majeur du Master REOC. Realise en binome avec Yohan Boujon, ce projet combinait SDN et NFV pour concevoir une infrastructure reseau virtualisee complete avec orchestration.

#### 5.1 Architecture reseau

Nous avons concu une topologie reseau composee de plusieurs commutateurs et hotes pour simuler un environnement reseau complexe. La topologie incluait des composants tels que des commutateurs (S1, S2, S3), des hotes (Z1, Z2, Z3), une passerelle intermediaire (GI) et un serveur. Cette configuration nous a permis de tester le filtrage de donnees et la connectivite entre les composants reseau.

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

#### 5.2 Instances Docker

Nous avons utilise Docker pour creer des instances pour chaque composant reseau. Un script a ete developpe pour construire les images Docker et generer les instances de maniere efficace. Cette configuration a facilite les tests de connectivite et de transmission de donnees entre les differentes zones.

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

#### 5.3 Simulation avec Containernet

J'ai utilise **Containernet**, un fork de Mininet, pour simuler la topologie reseau. Cela impliquait la creation et la gestion des liens reseau, et la verification de la connectivite entre les instances Docker.

Une fois le script `topology_sdn.py` lance, j'ai teste la connectivite entre les differents hotes de la topologie :

```bash
containernet> z1 ping -c 1 z2
containernet> z1 ping -c 1 serveur
containernet> z2 ping -c 1 z1
containernet> z2 ping -c 1 gi
containernet> ordon ping -c 1 z3
containernet> ordon ping -c 1 serveur
```

#### 5.4 Application 'Moniteur'

##### Monitoring

L'interface de monitoring, developpee avec **npyscreen**, permettait aux utilisateurs de selectionner et d'executer differents scripts en fonction des tests souhaites. Pour surveiller les donnees envoyees par chaque zone, nous nous concentrions sur le commutateur S1. En appelant l'API Ryu, nous pouvions observer des metriques telles que le trafic entrant et sortant, la taille des paquets et le total d'octets en temps reel.

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_REOC/monitor.png" style="width: 60%;"/>
</div>

##### Adaptation

Les scenarios d'adaptation incluaient le blocage des trames de Z2 et Z3 ou la reduction de leur bande passante tout en priorisant Z1. Cela etait realise via des requetes POST a l'API Ryu pour appliquer des regles telles que :

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

**Concepts cles** : Containernet, Docker, NFV, MANO, orchestration, monitoring, adaptation, API REST, Ryu.

---

### 6. Architecture Modulaire

Le module sur l'**Architecture Modulaire** traitait de la conception de systemes embarques temps reel, avec un accent particulier sur le **Worst-Case Traversal Time (WCTT)**. Ce concept est fondamental dans les reseaux embarques deterministes, notamment dans l'aeronautique et l'automobile.

Le WCTT represente le temps maximal qu'un paquet peut mettre pour traverser le reseau dans le pire des cas. Le calcul du WCTT est essentiel pour :
- **Garantir le determinisme** : s'assurer que chaque message arrive dans les delais impartis
- **Dimensionner les reseaux** : choisir les capacites des liens et des commutateurs en fonction des contraintes temporelles
- **Certifier les systemes critiques** : fournir des preuves formelles du respect des echeances dans les systemes avioniques

Les methodes d'analyse etudiees incluaient le **Network Calculus** et les approches par **simulation aggregee**, permettant d'approximer les bornes du WCTT pour des topologies complexes.

**Concepts cles** : WCTT, Network Calculus, determinisme, systemes critiques, certification, bornes temporelles.

---

### 7. Simulation Avancee avec NetworkX (N7)

Ce module, dispense a l'ENSEEIHT (N7), portait sur la **simulation avancee de reseaux** en utilisant la bibliotheque Python **NetworkX**. Le sujet central etait le **probleme de consensus** dans les reseaux distribues.

#### Probleme de consensus

L'objectif est que tous les noeuds d'un reseau convergent vers une meme valeur. Chaque noeud est initialise avec une valeur aleatoire, et a chaque cycle, un noeud diffuse sa valeur a ses voisins, qui mettent alors a jour leur propre valeur par moyenne :

```
while 1 do
    if (time mod T) = 0 then
        broadcast {VAL}
    else if msgReceived(R_VAL) then
        VAL <- (VAL + R_VAL) / 2
    end if
end while
```

#### Modelisation matricielle

L'approche mathematique utilisait des **matrices de transition** pour modeliser l'evolution du systeme. Pour chaque noeud emetteur, une matrice Ei est construite, et le produit de ces matrices sur un cycle donne la matrice de transition globale Pl :

```python
import numpy as np

def create_matrix_Ei(graph, emitter):
    """Creer la matrice Ei pour un noeud emetteur donne."""
    n = len(graph.nodes)
    Ei = np.zeros((n, n))
    for node in graph.nodes:
        if node == emitter:
            Ei[node][node] = 1
        else:
            neighbors = list(graph.neighbors(emitter))
            if node in neighbors:
                Ei[node][node] = 0.5
                Ei[node][emitter] = 0.5
            else:
                Ei[node][node] = 1
    return Ei

def compute_Pl(graph, sequence):
    """Calculer la matrice Pl pour une sequence d'emissions."""
    n = len(graph.nodes)
    Po = np.eye(n)
    for emitter in sequence:
        Ei = create_matrix_Ei(graph, emitter)
        Po = Ei @ Po
    return Po
```

#### Resultats de simulation

Les simulations ont ete realisees sur differentes topologies (mesh et ligne) en variant le nombre de noeuds :

| Topologie | Noeuds | Cycles moyens | Ecart-type |
|-----------|--------|---------------|------------|
| Mesh      | 5      | 2.4           | 0.21       |
| Mesh      | 10     | 2.1           | 0.26       |
| Ligne     | 5      | 24            | 11.17      |
| Ligne     | 10     | 63            | 46.8       |

La correlation entre le **plus grand valeur propre** de la matrice Pl et le temps de convergence a ete etudiee en generant 1000 sequences aleatoires et en tracant la relation entre ces deux metriques.

**Concepts cles** : Consensus distribue, NetworkX, matrices de transition, valeurs propres, convergence, topologie reseau.

---

### 8. Integrated Modular Avionics (IMA)

Le module **Integrated Modular Avionics** (IMA) traitait de l'architecture des systemes avioniques modernes. L'IMA est un concept d'architecture informatique dans lequel les ressources de calcul sont partagees entre plusieurs applications avioniques, contrairement a l'approche federee traditionnelle ou chaque fonction dispose de son propre equipement dedie.

Les principes fondamentaux de l'IMA :
- **Partitionnement temporel et spatial** : chaque application dispose de creneaux temporels fixes et d'espaces memoire isoles, garantissant l'absence d'interference entre les fonctions
- **Norme ARINC 653** : standard definissant l'interface entre les applications avioniques et le systeme d'exploitation temps reel, assurant la portabilite et l'interchangeabilite
- **AFDX (Avionics Full-Duplex Switched Ethernet)** : reseau de communication deterministe utilise pour interconnecter les modules IMA, avec des Virtual Links garantissant des bornes temporelles
- **Certification DO-178C** : processus de certification logicielle pour les systemes embarques critiques de l'aeronautique

L'IMA represente une evolution majeure dans l'avionique, permettant de reduire le poids, la consommation energetique et les couts de maintenance des systemes de bord, tout en maintenant les niveaux de securite les plus eleves (DAL A).

**Concepts cles** : IMA, ARINC 653, AFDX, partitionnement, DO-178C, certification, systemes critiques.

---

### 9. Low Power Networks for IoT

Ce module portait sur les **reseaux basse consommation pour l'Internet des Objets**, avec un focus particulier sur la technologie **LoRaWAN**. Le cours couvrait les specificites des communications IoT, ou les contraintes de consommation energetique et de cout sont primordiales.

#### Caracteristiques de l'IoT

Les systemes IoT se distinguent par :
- **Pervasive Computing** : dispositifs nombreux, circuits bon marche, memoire et puissance de calcul limitees
- **Connectivite sans fil** : alimentation par batterie ou energy harvesting, duree de vie superieure a 10 ans
- **Cout reduit** : puce a 2$, abonnement radio a 1$ par dispositif par an
- **Longue portee** : 5 a 40 km en champ libre

#### Pile protocolaire IoT

| Couche          | Standard                          |
|-----------------|-----------------------------------|
| Application     | IETF CoAP                        |
| Transport       | IETF UDP                         |
| Adaptation      | IETF 6LoWPAN, IETF SCHC          |
| Acces reseau    | IEEE 802.15.4, LoRaWAN            |

#### Travaux pratiques : Simulation LoRaWAN

Les TP consistaient en la simulation d'un deploiement LoRaWAN avec calcul de la couverture par triangulation. L'objectif etait d'evaluer les performances d'un reseau de passerelles LoRa en termes de taux de livraison de paquets (PDR) en fonction de la densite de deploiement et des parametres radio (spreading factor, puissance d'emission).

Un rapport detaille sur le deploiement LoRaWAN et l'analyse par triangulation a ete produit, demontrant l'impact du placement des passerelles sur la couverture et la fiabilite du reseau.

**Concepts cles** : LoRaWAN, LPWAN, IoT, ALOHA, spreading factor, PDR, energy harvesting, 6LoWPAN, CoAP.

---

### 10. Processus Stochastiques

Le module sur les **processus stochastiques** traitait de la modelisation et de l'evaluation de performances des systemes en file d'attente, un outil fondamental pour l'analyse des reseaux de communication.

#### Reseaux de files d'attente fermes

Le TP portait sur la simulation et le calcul analytique des performances d'un reseau ferme compose de quatre stations (T, H, R, D) avec N clients circulant en boucle :

```python
def exact_performance_measures(lambdaH, muH, muR, muD, C, N, p):
    # Calcul des taux d'arrivee effectifs
    gamma_H = lambdaH
    gamma_R = gamma_H / p
    gamma_D = (1 - p) * gamma_H / p

    # Calcul des intensites de trafic
    rho_H = gamma_H / muH
    rho_R = gamma_R / (C * muR)
    rho_D = gamma_D / muD

    # Calcul de la constante de normalisation G4(N)
    def calculate_G4(N, rho_H, rho_R, rho_D, C):
        G4 = 0
        for n_T in range(N + 1):
            for n_H in range(N + 1 - n_T):
                for n_R in range(N + 1 - n_T - n_H):
                    n_D = N - n_T - n_H - n_R
                    term = (rho_H**n_H) * (rho_R**n_R / phi_R(n_R, C)) * (rho_D**n_D)
                    G4 += term
        return G4

    G4 = calculate_G4(N, rho_H, rho_R, rho_D, C)
    return G4
```

#### Scenarios simules

Plusieurs scenarios ont ete simules en faisant varier les parametres N (nombre de clients) et p (probabilite de routage) :

| Scenario | N  | p    | Description                                      |
|----------|----|------|--------------------------------------------------|
| Cas 1    | 15 | 0.50 | Charge moderee, routage equilibre                |
| Cas 2    | 15 | 0.22 | Charge moderee, routage vers le disque dominant   |
| Cas 3    | 30 | 0.50 | Forte charge, routage equilibre                  |
| Cas 4    | 30 | 0.22 | Forte charge, routage vers le disque dominant     |

Les metriques evaluees comprenaient le **taux d'utilisation**, le **debit**, le **temps de sejour moyen** et la **probabilite de rejet**, calculees a la fois de maniere analytique (loi de Little, distribution stationnaire) et par simulation Monte Carlo.

**Concepts cles** : Files d'attente, reseaux fermes, loi de Little, chaines de Markov, distribution stationnaire, simulation Monte Carlo, intensite de trafic.

---

## PART D : ANALYSE ET REFLEXION

### Competences et connaissances mobilisees

Le Master REOC m'a permis de mobiliser et d'approfondir un ensemble de competences variees :

- **Architecture reseau** : comprehension des architectures SDN et NFV, et leur application dans les reseaux embarques et l'orchestration cloud
- **Programmation du data plane** : maitrise du langage P4 pour le traitement des paquets au niveau materiel
- **Systemes temps reel** : comprehension des contraintes temporelles dans les reseaux embarques critiques (AFDX, IMA, TSN)
- **Simulation et modelisation** : utilisation de NetworkX, de simulateurs LoRaWAN et de modeles stochastiques pour l'evaluation de performances
- **Developpement logiciel** : programmation Python pour la simulation, l'analyse de donnees et le developpement d'outils de monitoring
- **Travail collaboratif** : gestion de projets en binome dans un contexte de double diplome exigeant

### Auto-evaluation

Le programme du Master REOC etait intense, d'autant plus que les cours de l'INSA se poursuivaient en parallele. Cependant, cette experience a ete extremement enrichissante car j'ai acquis de nouvelles competences que j'ai pu mettre en oeuvre apres une analyse approfondie des bibliotheques et la comprehension du fonctionnement du SDN. Grace a mon partenaire, Yohan Boujon, notre collaboration etait efficace car nous nous connaissions bien et avons developpe la quasi-totalite de ce qui etait demande dans le temps imparti lors des travaux pratiques.

### Mon avis

Si je devais choisir a nouveau, je m'inscrirais sans hesitation au Master REOC. Le programme m'a permis d'elargir ma vision des reseaux dans les systemes embarques et d'acquerir une experience precieuse. Les enseignants ont fourni des bases solides pour comprendre tous les concepts applicables dans le monde professionnel. Les competences acquises seront utiles pour ma carriere. Ce programme a significativement contribue a ma croissance professionnelle et m'a prepare aux defis futurs dans le domaine des systemes en reseau.

La diversite des modules -- de l'avionique deterministe a l'IoT basse consommation, en passant par la virtualisation et la modelisation stochastique -- offre une vision panoramique des enjeux actuels des reseaux embarques. Cette polyvalence est un atout majeur pour aborder les problematiques industrielles complexes qui melent souvent plusieurs de ces domaines.

---

## Rapports et Projets

### Rapport du Projet SDCI

Le rapport complet du projet SDCI est disponible sur [GitHub - sdci-reoc](https://github.com/CedricChnfr/sdci-reoc).

<div class="pdf-container" style="display: flex; justify-content: center;">
    <iframe src="/img/BE_REOC/CHANFREAU_BOUJON_SDCI.pdf" width="100%" height="800px" style="overflow: auto;" frameborder="0"></iframe>
</div>

<p style="text-align: center;">
    <a href="/img/BE_REOC/CHANFREAU_BOUJON_SDCI.pdf" target="_blank">Ouvrir le rapport complet du projet SDCI</a>
</p>

<p style="text-align: center;">
    <a href="https://docs.google.com/presentation/d/1N_HovdFQlvxd32VUzZlEpD46pnBx_45RN4CnxDaeWEs/edit">Ouvrir le sujet du TP</a>
</p>

### Rapport sur les Processus Stochastiques

<div class="pdf-container" style="display: flex; justify-content: center;">
    <iframe src="/file/reports/S9/Report_Stochastique_REOC.pdf" width="100%" height="800px" style="overflow: auto;" frameborder="0"></iframe>
</div>

<p style="text-align: center;">
    <a href="/file/reports/S9/Report_Stochastique_REOC.pdf" target="_blank">Ouvrir le rapport sur les processus stochastiques</a>
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
    .back-nav {
        display: inline-block;
        margin-bottom: 10px;
        color: #007BFF;
        text-decoration: none;
        font-weight: bold;
    }
    .back-nav:hover {
        text-decoration: underline;
    }
    .section-title {
        text-align: center;
        color: #007BFF;
        margin-bottom: 30px;
    }
    .pdf-container {
        margin: 20px 0;
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
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 15px 0;
    }
    th, td {
        border: 1px solid #ddd;
        padding: 8px 12px;
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

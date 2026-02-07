---
layout: default
title:  "Cloud Edge Computing"
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

**Cours connexes** :
- [Emerging Network Technologies - S9](./2024-10-03-emerging-network.html) - SDN et architectures reseau
- [Middleware for IoT - S9](./2024-10-03-middleware-iot.html) - Protocoles IoT
- [Embedded IA for IoT - S9](./2024-10-03-embedded-ia-iot.html) - IA sur Edge
- [Service Oriented Architecture - S9](./2024-10-03-service-oriented-architecture.html) - Architectures de services Cloud

---

# Cloud & Edge Computing - Semestre 9

**Annee academique** : 2024-2025
**Enseignant** : Sami Yangui
**Categorie** : Cloud, Virtualisation, Edge Computing

---

## PART A - Presentation Generale

<h3 class="section-title">Vue d'ensemble</h3>

Le cours de Cloud & Edge Computing presente les systemes cloud centralises et les solutions edge decentralisees, preparant a repondre aux defis technologiques modernes. Enseigne par Sami Yangui, ce cours explore les technologies de virtualisation, les services cloud et les infrastructures edge. Il met l'accent sur la conception, le deploiement et la gestion d'architectures qui combinent les avantages de faible latence du edge computing avec la scalabilite des environnements cloud.

Cette formation est particulierement pertinente dans le contexte actuel, ou la montee de l'IoT, des applications temps reel et des reseaux necessite une expertise dans ces domaines.

**Objectifs pedagogiques** :
- Comprendre les fondamentaux de la virtualisation (hyperviseurs Type 1 et Type 2, paravirtualisation)
- Maitriser la conteneurisation avec Docker et l'orchestration avec Kubernetes
- Apprehender les modeles de service cloud (IaaS, PaaS, SaaS)
- Deployer et configurer des environnements OpenStack
- Comprendre le paradigme Edge Computing, Fog Computing et MEC (Multi-access Edge Computing)
- Concevoir des architectures cloud-edge integrees

<h3 class="section-title">Position dans le cursus</h3>

Ce module s'appuie sur les bases acquises precedemment :
- **Interconnexion Reseau (S8)** : fondamentaux TCP/IP, routage, VLAN
- **Systemes d'Exploitation (S5)** : gestion des processus, systemes Unix
- **Architecture Materielle (S6)** : couche physique, materiels serveurs

Il se connecte directement aux autres cours du semestre :
- **Emerging Network Technologies (S9)** : SDN et virtualisation reseau
- **Middleware for IoT (S9)** : protocoles de communication IoT deployes sur le cloud/edge
- **Service Oriented Architecture (S9)** : architectures de services cloud

---

## PART B - Experience et Contexte

<h3 class="section-title">Organisation et ressources</h3>

Le module combinait theorie et pratique intensive :

**Cours magistraux** :
- Introduction au Cloud Computing et ses caracteristiques essentielles
- Technologies de virtualisation (hyperviseurs, conteneurs)
- Modeles de service cloud (IaaS, PaaS, SaaS) et modeles de deploiement
- Architecture OpenStack et ses composants
- Edge Computing, Fog Computing et MEC
- Continuum Cloud-Edge et orchestration

**Travaux pratiques** :
- **TP1** : Configuration de reseaux virtuels avec VirtualBox, routage inter-VM
- **TP2** : Creation et gestion de conteneurs Docker, Dockerfiles, volumes
- **TP3** : Deploiement d'une infrastructure OpenStack (Nova, Neutron, Glance, Keystone)
- **TP4** : Orchestration de conteneurs avec Kubernetes, deploiement de services

**Outils utilises** :
- **VirtualBox** : virtualisation de type 2 pour les TPs
- **Docker** : conteneurisation d'applications
- **Kubernetes** : orchestration de conteneurs
- **OpenStack** : plateforme cloud open-source (Nova, Neutron, Glance, Keystone, Horizon)
- **Linux (Ubuntu)** : systeme hote pour les environnements virtualises

<h3 class="section-title">Mon role</h3>

Dans le cadre de ce cours, j'etais responsable de :
- Apprendre et pratiquer les techniques de virtualisation (VMs et conteneurs)
- Concevoir, deployer et gerer des architectures hybrides combinant cloud et edge computing
- Acquerir des competences avec des outils comme Kubernetes, Docker et VirtualBox
- Rediger un rapport technique complet sur les travaux pratiques realises

<h3 class="section-title">Difficultes rencontrees</h3>

**Configuration reseau VirtualBox** :
La mise en place des reseaux virtuels (NAT, bridge, host-only) et la comprehension de leur interaction a necessite du temps et de la methodologie.

**Deploiement OpenStack** :
OpenStack est une plateforme complexe avec de nombreux composants interdependants. La configuration initiale et la resolution de problemes de connectivite entre services ont ete des defis formateurs.

**Kubernetes en temps limite** :
La session sur Kubernetes a ete realisee rapidement avec mon binome. Nous avons du executer les commandes sans toujours avoir le temps de comprendre chaque etape en profondeur. Le rapport redige a posteriori nous a permis de mieux assimiler les concepts.

---

## PART C - Aspects Techniques Detailles

<h3 class="section-title">1. Fondamentaux de la virtualisation</h3>

**Sans virtualisation** :

Dans un environnement sans virtualisation, une seule application s'execute directement sur le systeme d'exploitation hote qui gere le materiel physique. Cette approche presente des limitations en termes d'isolation, de scalabilite et d'utilisation des ressources.

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_Cloud_Computing/No_Virt.png" style="max-width: 300px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Architecture sans virtualisation - une seule application sur l'OS hote</p>
</div>

**Avec virtualisation** :

La virtualisation permet d'executer plusieurs systemes d'exploitation et applications sur un meme materiel physique grace a un hyperviseur. Chaque machine virtuelle (VM) dispose de ses propres ressources virtualisees (CPU, RAM, stockage, reseau).

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_Cloud_Computing/Virt.png" style="max-width: 350px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Architecture avec virtualisation - plusieurs VMs sur un meme hote physique via un hyperviseur</p>
</div>

**Avantages de la virtualisation** :
- **Consolidation de serveurs** : reduire le nombre de machines physiques
- **Isolation** : chaque VM est independante (panne d'une VM ne touche pas les autres)
- **Flexibilite** : deploiement rapide de nouveaux environnements
- **Snapshots et migration** : sauvegarde d'etat et migration a chaud
- **Optimisation des ressources** : meilleure utilisation du materiel

<h3 class="section-title">2. Hyperviseurs Type 1 et Type 2</h3>

L'hyperviseur est le composant logiciel qui permet la virtualisation. Il existe deux types principaux :

**Hyperviseur de Type 1 (Bare Metal)** :

L'hyperviseur s'execute directement sur le materiel physique, sans systeme d'exploitation hote intermediaire. Il offre de meilleures performances et une securite accrue car il a un acces direct au materiel.

**Exemples** : VMware ESXi, Microsoft Hyper-V, Citrix XenServer, KVM

**Caracteristiques** :
- Performances proches du natif
- Gestion directe des ressources materielles
- Utilise en production dans les datacenters
- Securite renforcee (surface d'attaque reduite)

**Hyperviseur de Type 2 (Hosted)** :

L'hyperviseur s'execute comme une application sur un systeme d'exploitation hote existant. Il est plus simple a installer et a utiliser mais offre des performances legerement inferieures.

**Exemples** : Oracle VirtualBox, VMware Workstation, Parallels Desktop

**Caracteristiques** :
- Facile a installer sur un poste de travail
- Ideal pour le developpement et les tests
- Performances reduites (couche OS intermediaire)
- Utilise principalement en environnement desktop

<div style="text-align: center; display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; margin: 20px 0;">
    <div>
        <img src="/img/BE_Cloud_Computing/H_type1.png" style="max-width: 350px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
        <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Hyperviseur Type 1 (Bare Metal)</p>
    </div>
    <div>
        <img src="/img/BE_Cloud_Computing/H_type2.png" style="max-width: 350px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
        <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Hyperviseur Type 2 (Hosted)</p>
    </div>
</div>

| Critere | Type 1 (Bare Metal) | Type 2 (Hosted) |
|---------|---------------------|-----------------|
| Installation | Directement sur le materiel | Sur un OS existant |
| Performance | Elevee | Moderee |
| Usage principal | Datacenters, production | Developpement, tests |
| Securite | Forte (acces direct) | Dependante de l'OS hote |
| Exemples | ESXi, KVM, Hyper-V | VirtualBox, VMware Workstation |

<h3 class="section-title">3. Paravirtualisation</h3>

La paravirtualisation est une technique ou le systeme d'exploitation invite est modifie pour communiquer directement avec l'hyperviseur via des "hypercalls", au lieu de simuler completement le materiel. Cela ameliore les performances par rapport a la virtualisation complete, car les appels systeme sont optimises pour l'environnement virtualise.

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_Cloud_Computing/Paravirtualization.png" style="max-width: 600px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Solutions de paravirtualisation - OpenNebula, OpenStack, Proxmox</p>
</div>

**Avantages de la paravirtualisation** :
- Performances ameliorees par rapport a la virtualisation complete
- Meilleure gestion des E/S (entrees/sorties)
- Overhead reduit

**Inconvenients** :
- Necessite la modification du systeme d'exploitation invite
- Compatibilite limitee aux OS modifies

<h3 class="section-title">4. Conteneurs vs Machines Virtuelles</h3>

Les conteneurs representent une evolution majeure par rapport aux machines virtuelles traditionnelles. Contrairement aux VMs qui virtualisent le materiel complet, les conteneurs partagent le noyau du systeme d'exploitation hote et n'embarquent que les bibliotheques et dependances necessaires a l'application.

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_Cloud_Computing/Containers.png" style="max-width: 600px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Ecosysteme conteneur - Container Linux, Solaris, Docker</p>
</div>

| Critere | Machine Virtuelle | Conteneur |
|---------|-------------------|-----------|
| Isolation | Complete (OS separe) | Au niveau processus |
| Taille | Go (OS complet) | Mo (bibliotheques seulement) |
| Demarrage | Minutes | Secondes |
| Performance | Overhead (hyperviseur) | Proche du natif |
| Portabilite | Limitee | Excellente |
| Densite | ~10-20 VMs par serveur | ~100+ conteneurs par serveur |
| Securite | Forte (isolation materielle) | Moderee (noyau partage) |

**Cas d'utilisation des VMs** :
- Isolation forte necessaire (multi-tenant, securite)
- OS differents sur un meme hote
- Applications legacy

**Cas d'utilisation des conteneurs** :
- Microservices
- CI/CD (integration et deploiement continus)
- Applications cloud-native
- Environnements de developpement reproductibles

<h3 class="section-title">5. Docker et conteneurisation</h3>

Docker est la plateforme de conteneurisation la plus populaire. Elle permet de creer, deployer et gerer des conteneurs de maniere efficace. Lors des travaux pratiques, j'ai appris a utiliser Docker pour virtualiser des applications dans des environnements isoles.

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_Cloud_Computing/Docker.png" style="max-width: 250px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Logo Docker</p>
</div>

**Architecture Docker** :
- **Docker Engine** : le daemon qui gere les conteneurs
- **Docker Image** : template read-only contenant l'application et ses dependances
- **Docker Container** : instance d'execution d'une image
- **Dockerfile** : fichier de configuration pour construire une image
- **Docker Hub** : registre public d'images Docker
- **Docker Compose** : outil pour definir des applications multi-conteneurs

**Commandes principales utilisees en TP** :

```bash
# Telecharger une image depuis Docker Hub
docker pull ubuntu:20.04

# Lancer un conteneur en mode interactif
docker run -it --name mon_conteneur ubuntu:20.04 /bin/bash

# Lister les conteneurs actifs
docker ps

# Lister tous les conteneurs (actifs et arretes)
docker ps -a

# Construire une image a partir d'un Dockerfile
docker build -t mon_image .

# Exposer un port et lancer un conteneur en arriere-plan
docker run -d -p 8080:80 --name serveur_web nginx

# Gerer les volumes pour la persistance
docker run -v /host/data:/container/data mon_image
```

**Exemple de Dockerfile** :

```dockerfile
FROM ubuntu:20.04
RUN apt-get update && apt-get install -y python3 pip
COPY app.py /app/
WORKDIR /app
EXPOSE 5000
CMD ["python3", "app.py"]
```

**Avantages de Docker** :
- Portabilite ("Build once, run anywhere")
- Reproductibilite des environnements
- Isolation des applications
- Demarrage rapide (secondes)
- Ecosysteme riche (Docker Hub, Docker Compose)

<h3 class="section-title">6. Modeles de service Cloud : IaaS, PaaS, SaaS</h3>

Le Cloud Computing propose differents niveaux d'abstraction pour les services, representes par trois modeles principaux :

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_Cloud_Computing/SDM.png" style="max-width: 500px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Modeles de service Cloud - IaaS, SaaS, PaaS et leurs niveaux d'abstraction</p>
</div>

**IaaS (Infrastructure as a Service)** :

Fournit les ressources d'infrastructure virtualisees (serveurs, stockage, reseau). L'utilisateur gere l'OS, les middlewares et les applications.

- **Exemples** : AWS EC2, Google Compute Engine, Azure Virtual Machines, OpenStack
- **Responsabilite utilisateur** : OS, runtime, applications, donnees
- **Responsabilite fournisseur** : materiel, virtualisation, reseau
- **Flexibilite** : maximale (controle total sur l'infrastructure)

**PaaS (Platform as a Service)** :

Fournit une plateforme de developpement et de deploiement. L'utilisateur se concentre sur le code applicatif sans gerer l'infrastructure sous-jacente.

- **Exemples** : Google App Engine, Heroku, Azure App Service, Cloud Foundry
- **Responsabilite utilisateur** : applications et donnees
- **Responsabilite fournisseur** : OS, runtime, middleware, infrastructure
- **Flexibilite** : moderee (contraintes de la plateforme)

**SaaS (Software as a Service)** :

Applications logicielles accessibles via le navigateur, entierement gerees par le fournisseur.

- **Exemples** : Google Workspace, Microsoft 365, Salesforce, Dropbox
- **Responsabilite utilisateur** : donnees et parametres
- **Responsabilite fournisseur** : tout le reste
- **Flexibilite** : limitee (configuration seulement)

| Aspect | IaaS | PaaS | SaaS |
|--------|------|------|------|
| Controle | Total | Partiel | Minimal |
| Complexite | Elevee | Moyenne | Faible |
| Scalabilite | Manuelle/Semi-auto | Automatique | Automatique |
| Cout | Pay-per-use | Pay-per-use | Abonnement |
| Public cible | Admins systeme | Developpeurs | Utilisateurs finaux |

**Caracteristiques essentielles du Cloud (NIST)** :

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_Cloud_Computing/Characteristics.png" style="max-width: 600px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Les caracteristiques essentielles du Cloud Computing selon le NIST</p>
</div>

Les cinq caracteristiques essentielles definies par le NIST :
- **On-demand self-service** : provisionnement automatique sans intervention humaine
- **Broad network access** : acces via des mecanismes standards (HTTP, API)
- **Resource pooling** : ressources mutualisees pour plusieurs clients (multi-tenant)
- **Rapid elasticity** : scalabilite automatique selon la demande
- **Measured service** : facturation a l'usage (pay-per-use)

**Modeles de deploiement Cloud** :
- **Cloud Public** : infrastructure partagee, accessible a tous (AWS, Azure, GCP)
- **Cloud Prive** : infrastructure dediee a une organisation (OpenStack on-premise)
- **Cloud Hybride** : combinaison de cloud public et prive
- **Cloud Communautaire** : partage entre organisations ayant des besoins similaires

<h3 class="section-title">7. OpenStack - Plateforme Cloud Open-Source</h3>

OpenStack est une plateforme open-source de cloud computing, principalement deployee comme IaaS. Elle permet la gestion de grands pools de ressources de calcul, de stockage et de reseau, le tout administrable via un tableau de bord (Horizon) ou via l'API OpenStack.

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_Cloud_Computing/sch_OpenStack.png" style="max-width: 500px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Architecture d'OpenStack et ses composants principaux</p>
</div>

**Composants principaux d'OpenStack** :

| Composant | Nom du projet | Fonction |
|-----------|---------------|----------|
| Compute | **Nova** | Gestion des instances de machines virtuelles |
| Networking | **Neutron** | Reseaux virtuels, sous-reseaux, routeurs, firewalls |
| Image | **Glance** | Stockage et gestion des images de VMs |
| Identity | **Keystone** | Authentification, autorisation, catalogue de services |
| Dashboard | **Horizon** | Interface web d'administration |
| Block Storage | **Cinder** | Volumes de stockage persistants |
| Object Storage | **Swift** | Stockage objet distribue |
| Orchestration | **Heat** | Templates d'infrastructure (Infrastructure as Code) |

**Architecture OpenStack** :

L'architecture OpenStack suit un modele de services distribues communiquant via des APIs REST. Keystone fournit l'authentification centralisee. Nova gere le cycle de vie des VMs en s'appuyant sur Glance pour les images, Neutron pour le reseau et Cinder pour le stockage.

**Manipulations realisees en TP** :
- Creation de reseaux virtuels et sous-reseaux avec Neutron
- Deploiement d'instances VM avec Nova
- Configuration de regles de securite (security groups)
- Utilisation du dashboard Horizon pour l'administration visuelle
- Gestion des images avec Glance

<h3 class="section-title">8. Configuration reseau avec VirtualBox</h3>

Les travaux pratiques m'ont permis de configurer des reseaux virtuels avec VirtualBox. J'ai appris a creer et configurer des machines virtuelles, tester leur connectivite, et mettre en place des regles de redirection de ports pour permettre la communication entre les VMs et l'hote.

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_Cloud_Computing/VirtualBox.png" style="max-width: 400px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Configuration reseau avec VirtualBox</p>
</div>

**Types de reseau VirtualBox configures** :

| Mode reseau | Acces Internet | Communication inter-VM | Acces depuis l'hote |
|-------------|----------------|------------------------|---------------------|
| NAT | Oui | Non | Via port forwarding |
| Bridged | Oui | Oui | Oui |
| Host-Only | Non | Oui | Oui |
| Internal | Non | Oui (meme reseau) | Non |

**Manipulations realisees** :
- Configuration de reseaux prives et routeurs pour la communication entre differentes VMs
- Mise en place de regles de port forwarding pour l'acces SSH
- Tests de connectivite (ping, traceroute) entre VMs
- Configuration de sous-reseaux isoles

<h3 class="section-title">9. Paradigme Edge Computing</h3>

Le Edge Computing est un paradigme qui consiste a traiter les donnees au plus pres de leur source de generation, plutot que de les envoyer systematiquement vers un datacenter cloud centralise. Ce concept est fondamental pour les applications necessitant une faible latence, une bande passante reduite ou une souverainete des donnees.

**Motivations du Edge Computing** :
- **Latence** : les applications temps reel (vehicules autonomes, realite augmentee) ne peuvent pas tolerer les delais aller-retour vers le cloud
- **Bande passante** : les volumes de donnees generes par l'IoT saturent les liens reseau
- **Souverainete des donnees** : certaines reglementations imposent le traitement local des donnees
- **Fiabilite** : le fonctionnement doit continuer meme en cas de perte de connexion au cloud

**Caracteristiques cles** :
- Traitement local des donnees au plus pres des utilisateurs/capteurs
- Reduction de la latence (de ~100ms a <10ms)
- Filtrage et aggregation des donnees avant envoi au cloud
- Fonctionnement en mode deconnecte possible

<h3 class="section-title">10. Fog Computing</h3>

Le Fog Computing, introduit par Cisco, est une extension du cloud computing qui rapproche les services de calcul, de stockage et de reseau des peripheriques edge. Il se situe comme une couche intermediaire entre les dispositifs IoT (edge) et le cloud centralise.

**Differences Fog vs Edge** :

| Aspect | Edge Computing | Fog Computing |
|--------|---------------|---------------|
| Localisation | Sur le dispositif ou tres proche | Entre edge et cloud |
| Capacite de calcul | Limitee | Moderee |
| Latence | Tres faible | Faible |
| Exemples | Capteurs, gateways IoT | Serveurs locaux, routeurs intelligents |
| Scope | Traitement immediat | Aggregation, pre-traitement |

**Architecture Fog Computing** :
1. **Couche Edge** : capteurs et actionneurs (collecte de donnees brutes)
2. **Couche Fog** : passerelles, serveurs locaux (pre-traitement, filtrage, decisions rapides)
3. **Couche Cloud** : datacenters (analyse approfondie, stockage long terme, machine learning)

<h3 class="section-title">11. MEC - Multi-access Edge Computing</h3>

Le MEC (Multi-access Edge Computing), standardise par l'ETSI, est un concept qui integre les capacites de calcul au niveau de l'infrastructure des operateurs de telecommunications, typiquement dans les stations de base ou les points d'acces du reseau.

**Caracteristiques du MEC** :
- Integration avec l'infrastructure reseau des operateurs (4G/5G)
- APIs standardisees pour l'acces aux informations reseau (localisation, QoS)
- Hebergement d'applications tierces au plus pres du reseau d'acces
- Faible latence garantie par la proximite avec les antennes

**Cas d'utilisation MEC** :
- **Vehicules connectes (V2X)** : communication ultra-fiable et faible latence
- **Realite augmentee/virtuelle** : rendu en temps reel
- **Gaming cloud** : streaming de jeux avec latence minimale
- **Video analytics** : analyse de flux video en temps reel
- **IoT industriel** : controle de processus industriels

<h3 class="section-title">12. Continuum Cloud-Edge</h3>

Le continuum cloud-edge represente une vision unifiee ou les ressources de calcul sont distribuees de maniere continue depuis les dispositifs edge jusqu'au cloud centralise. L'objectif est d'offrir une orchestration transparente qui place automatiquement les traitements la ou ils sont le plus pertinents.

**Principes du continuum** :
- **Placement dynamique** : les applications migrent entre edge, fog et cloud selon les besoins (latence, charge, cout)
- **Orchestration unifiee** : un plan de controle unique gere l'ensemble des ressources
- **Heterogeneite** : integration de ressources diverses (x86, ARM, GPU, FPGA)
- **Elasticite** : scalabilite horizontale et verticale a tous les niveaux

**Gestion autonomique** :

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_Cloud_Computing/Automatic.png" style="max-width: 400px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Boucle autonomique MAPE-K (Monitor, Analyze, Plan, Execute) pour la gestion du continuum cloud-edge</p>
</div>

Le modele MAPE-K (Monitor, Analyze, Plan, Execute - Knowledge) permet une gestion autonomique des ressources du continuum :
- **Monitor** : collecte des metriques (latence, charge CPU, bande passante)
- **Analyze** : detection d'anomalies et tendances
- **Plan** : decision de placement, migration, scaling
- **Execute** : application des decisions (deploiement, migration de conteneurs)
- **Knowledge** : base de connaissances partagee alimentant la boucle

<h3 class="section-title">13. Orchestration de conteneurs avec Kubernetes</h3>

Kubernetes (K8s) est la plateforme standard pour l'orchestration de conteneurs a grande echelle. Elle automatise le deploiement, la mise a l'echelle et la gestion des applications conteneurisees.

**Architecture Kubernetes** :

**Plan de controle (Control Plane)** :
- **kube-apiserver** : point d'entree pour toutes les operations (API REST)
- **etcd** : base de donnees cle-valeur distribuee (etat du cluster)
- **kube-scheduler** : placement des pods sur les noeuds
- **kube-controller-manager** : controleurs qui maintiennent l'etat desire

**Noeuds Worker** :
- **kubelet** : agent sur chaque noeud qui gere les pods
- **kube-proxy** : gestion du reseau et du load balancing
- **Container Runtime** : Docker, containerd ou CRI-O

**Concepts fondamentaux** :

| Concept | Description |
|---------|-------------|
| **Pod** | Unite de deploiement minimale (1+ conteneurs) |
| **Deployment** | Gestion declarative des pods (replicas, mises a jour) |
| **Service** | Exposition reseau stable pour un ensemble de pods |
| **Namespace** | Isolation logique au sein d'un cluster |
| **ConfigMap/Secret** | Configuration et donnees sensibles |
| **PersistentVolume** | Stockage persistant pour les pods |

**Exemple de deploiement YAML utilise en TP** :

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
  type: LoadBalancer
```

**Commandes Kubernetes utilisees en TP** :

```bash
# Deployer une application
kubectl apply -f deployment.yaml

# Voir les pods en cours d'execution
kubectl get pods

# Voir les services
kubectl get services

# Mettre a l'echelle un deploiement
kubectl scale deployment nginx-deployment --replicas=5

# Voir les logs d'un pod
kubectl logs <nom-du-pod>

# Description detaillee d'un pod
kubectl describe pod <nom-du-pod>
```

---

## PART D - Analyse et Reflexion

<h3 class="section-title">Competences acquises</h3>

**Virtualisation et conteneurisation** :
Maitrise des differences fondamentales entre VMs et conteneurs, des hyperviseurs Type 1 et Type 2, et des outils Docker et VirtualBox. Capacite a choisir la technologie adaptee selon le cas d'usage.

**Cloud Computing** :
Comprehension des modeles de service (IaaS, PaaS, SaaS) et de deploiement (public, prive, hybride). Experience pratique avec OpenStack pour le deploiement d'une infrastructure cloud.

**Edge Computing** :
Apprehension du paradigme edge et de ses variantes (Fog Computing, MEC). Comprehension du continuum cloud-edge et des enjeux d'orchestration dans un environnement distribue.

**Orchestration** :
Competence initiale avec Kubernetes pour le deploiement et la gestion de services conteneurises. Comprehension de l'architecture cluster et des fichiers de configuration YAML.

<h3 class="section-title">Points cles a retenir</h3>

**1. La virtualisation est le socle du cloud** :
Sans virtualisation (VMs ou conteneurs), le cloud computing n'existerait pas. Comprendre ces mecanismes est fondamental pour tout ingenieur cloud.

**2. Conteneurs et VMs sont complementaires** :
Les conteneurs ne remplacent pas les VMs. Chaque technologie a ses cas d'usage. En production, on utilise souvent des conteneurs deployes sur des VMs pour combiner les avantages des deux.

**3. Le edge computing repond a des besoins reels** :
L'IoT, la 5G et les applications temps reel rendent le edge computing indispensable. Le cloud seul ne suffit plus pour toutes les charges de travail.

**4. L'orchestration est essentielle a grande echelle** :
Kubernetes est devenu le standard de facto pour gerer des centaines de conteneurs. Maitriser cet outil est une competence tres demandee.

**5. Le continuum cloud-edge est l'avenir** :
La tendance est a l'integration transparente de toutes les couches (edge, fog, cloud) avec une orchestration unifiee.

<h3 class="section-title">Retour d'experience</h3>

J'ai developpe de nouvelles competences en architectures hybrides et leurs applications dans les environnements informatiques modernes. J'ai pu comprendre et utiliser l'ensemble des concepts abordes. Cependant, j'ai realise qu'il me faudra pratiquer ces outils a l'avenir pour ne pas les oublier, car je n'ai pas actuellement l'opportunite de les utiliser dans mon entreprise d'apprentissage.

La session sur Kubernetes ayant ete realisee rapidement avec mon binome, nous avons du passer vite et simplement lancer les commandes. Grace au rapport que nous avons redige, il a ete plus simple de comprendre les concepts dans un second temps.

<h3 class="section-title">Mon avis</h3>

Ce cours etait tres interessant. J'ai eu la chance d'apprendre de nombreux concepts que j'entends dans la vie courante pour certains metiers. Ce cours sera reellement utile pour mon parcours professionnel ou ces concepts pourraient etre appliques.

Le contenu du cours etait bien structure, partant des bases de la virtualisation et progressant graduellement vers des sujets plus complexes. Cette progression m'a aide a mieux comprendre puis a elargir mes connaissances vers des concepts plus avances.

Je me sens desormais plus confiant pour concevoir, deployer et gerer des solutions cloud-edge scalables.

**Applications professionnelles** :

- **Ingenieur DevOps** : deploiement d'applications conteneurisees sur Kubernetes, CI/CD
- **Architecte Cloud** : conception d'infrastructures cloud hybrides et multi-cloud
- **Ingenieur IoT** : deploiement d'architectures edge pour le traitement local des donnees
- **Administrateur systeme** : gestion d'infrastructures virtualisees et OpenStack
- **Ingenieur Telecom** : integration MEC dans les reseaux 5G

**Liens avec les autres cours** :
- [Emerging Network Technologies](./2024-10-03-emerging-network.html) : SDN pour la virtualisation du reseau dans le cloud
- [Middleware for IoT](./2024-10-03-middleware-iot.html) : protocoles IoT deployes sur edge/cloud
- [Embedded IA for IoT](./2024-10-03-embedded-ia-iot.html) : inference IA sur les dispositifs edge
- [Service Oriented Architecture](./2024-10-03-service-oriented-architecture.html) : microservices deployes dans le cloud

---

## Documents de Cours

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Cours Complet Cloud & Edge Computing</h4>
      <p>Cours complet sur le Cloud & Edge Computing : virtualisation, modeles de service, OpenStack, Edge Computing, Fog Computing, MEC, continuum cloud-edge.</p>
      <embed src="/cours-pdf/S9/Cloud/Cours_5ISS-CloudEdgeComputing.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/Cloud/Cours_5ISS-CloudEdgeComputing.pdf" target="_blank">Telecharger le cours</a></p>
    </div>
  </div>
</div>

---

## Rapports et Projets

<div style="text-align: center;">
    <h3>Rapport de Projet Cloud Computing</h3>
</div>

<div style="display: flex; justify-content: center;">
    <embed src="/file/reports/S9/Boukouiss_Chanfreau_Cloud_Computing_Rapport.pdf" width="100%" height="800px" type="application/pdf">
</div>

<p style="text-align: center;">
    <a href="/file/reports/S9/Boukouiss_Chanfreau_Cloud_Computing_Rapport.pdf" target="_blank">Ouvrir le rapport complet</a>
</p>
<p style="text-align: center;">
    <a href="/img/BE_Cloud_Computing/Lab_Subject_cloud.pdf" target="_blank">Ouvrir le sujet de TP</a>
</p>

---

*Cours suivi en 2024-2025 a l'INSA Toulouse, Departement Genie Electrique et Informatique, specialite ISS.*

<div class="back-nav">
    <a href="./my-courses-2024-2025.html">&larr; Retour aux Cours 2024-2025</a>
</div>

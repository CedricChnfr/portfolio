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
    <a href="./my-courses-2024-2025.html" data-i18n-html="back-courses-2024-2025">&larr; Retour aux Cours 2024-2025</a>
</div>

<div class="lang-fr">

<p><strong>Cours connexes</strong> :</p>
<ul>
<li><a href="./emerging-network.html">Emerging Network Technologies - S9</a> - SDN et architectures reseau</li>
<li><a href="./middleware-iot.html">Middleware for IoT - S9</a> - Protocoles IoT</li>
<li><a href="./embedded-ia-iot.html">Embedded IA for IoT - S9</a> - IA sur Edge</li>
<li><a href="./service-oriented-architecture.html">Service Oriented Architecture - S9</a> - Architectures de services Cloud</li>
</ul>

<hr>

<h1>Cloud &amp; Edge Computing - Semestre 9</h1>

<p><strong>Annee academique</strong> : 2024-2025<br>
<strong>Enseignant</strong> : Sami Yangui<br>
<strong>Categorie</strong> : Cloud, Virtualisation, Edge Computing</p>

<hr>

<h2>PART A - Presentation Generale</h2>

<h3 class="section-title">Vue d'ensemble</h3>

<p>Le cours de Cloud &amp; Edge Computing presente les systemes cloud centralises et les solutions edge decentralisees, preparant a repondre aux defis technologiques modernes. Enseigne par Sami Yangui, ce cours explore les technologies de virtualisation, les services cloud et les infrastructures edge. Il met l'accent sur la conception, le deploiement et la gestion d'architectures qui combinent les avantages de faible latence du edge computing avec la scalabilite des environnements cloud.</p>

<p>Cette formation est particulierement pertinente dans le contexte actuel, ou la montee de l'IoT, des applications temps reel et des reseaux necessite une expertise dans ces domaines.</p>

<p><strong>Objectifs pedagogiques</strong> :</p>
<ul>
<li>Comprendre les fondamentaux de la virtualisation (hyperviseurs Type 1 et Type 2, paravirtualisation)</li>
<li>Maitriser la conteneurisation avec Docker et l'orchestration avec Kubernetes</li>
<li>Apprehender les modeles de service cloud (IaaS, PaaS, SaaS)</li>
<li>Deployer et configurer des environnements OpenStack</li>
<li>Comprendre le paradigme Edge Computing, Fog Computing et MEC (Multi-access Edge Computing)</li>
<li>Concevoir des architectures cloud-edge integrees</li>
</ul>

<h3 class="section-title">Position dans le cursus</h3>

<p>Ce module s'appuie sur les bases acquises precedemment :</p>
<ul>
<li><strong>Interconnexion Reseau (S8)</strong> : fondamentaux TCP/IP, routage, VLAN</li>
<li><strong>Systemes d'Exploitation (S5)</strong> : gestion des processus, systemes Unix</li>
<li><strong>Architecture Materielle (S6)</strong> : couche physique, materiels serveurs</li>
</ul>

<p>Il se connecte directement aux autres cours du semestre :</p>
<ul>
<li><strong>Emerging Network Technologies (S9)</strong> : SDN et virtualisation reseau</li>
<li><strong>Middleware for IoT (S9)</strong> : protocoles de communication IoT deployes sur le cloud/edge</li>
<li><strong>Service Oriented Architecture (S9)</strong> : architectures de services cloud</li>
</ul>

<hr>

<h2>PART B - Experience et Contexte</h2>

<h3 class="section-title">Organisation et ressources</h3>

<p>Le module combinait theorie et pratique intensive :</p>

<p><strong>Cours magistraux</strong> :</p>
<ul>
<li>Introduction au Cloud Computing et ses caracteristiques essentielles</li>
<li>Technologies de virtualisation (hyperviseurs, conteneurs)</li>
<li>Modeles de service cloud (IaaS, PaaS, SaaS) et modeles de deploiement</li>
<li>Architecture OpenStack et ses composants</li>
<li>Edge Computing, Fog Computing et MEC</li>
<li>Continuum Cloud-Edge et orchestration</li>
</ul>

<p><strong>Travaux pratiques</strong> :</p>
<ul>
<li><strong>TP1</strong> : Configuration de reseaux virtuels avec VirtualBox, routage inter-VM</li>
<li><strong>TP2</strong> : Creation et gestion de conteneurs Docker, Dockerfiles, volumes</li>
<li><strong>TP3</strong> : Deploiement d'une infrastructure OpenStack (Nova, Neutron, Glance, Keystone)</li>
<li><strong>TP4</strong> : Orchestration de conteneurs avec Kubernetes, deploiement de services</li>
</ul>

<p><strong>Outils utilises</strong> :</p>
<ul>
<li><strong>VirtualBox</strong> : virtualisation de type 2 pour les TPs</li>
<li><strong>Docker</strong> : conteneurisation d'applications</li>
<li><strong>Kubernetes</strong> : orchestration de conteneurs</li>
<li><strong>OpenStack</strong> : plateforme cloud open-source (Nova, Neutron, Glance, Keystone, Horizon)</li>
<li><strong>Linux (Ubuntu)</strong> : systeme hote pour les environnements virtualises</li>
</ul>

<h3 class="section-title">Mon role</h3>

<p>Dans le cadre de ce cours, j'etais responsable de :</p>
<ul>
<li>Apprendre et pratiquer les techniques de virtualisation (VMs et conteneurs)</li>
<li>Concevoir, deployer et gerer des architectures hybrides combinant cloud et edge computing</li>
<li>Acquerir des competences avec des outils comme Kubernetes, Docker et VirtualBox</li>
<li>Rediger un rapport technique complet sur les travaux pratiques realises</li>
</ul>

<h3 class="section-title">Difficultes rencontrees</h3>

<p><strong>Configuration reseau VirtualBox</strong> :<br>
La mise en place des reseaux virtuels (NAT, bridge, host-only) et la comprehension de leur interaction a necessite du temps et de la methodologie.</p>

<p><strong>Deploiement OpenStack</strong> :<br>
OpenStack est une plateforme complexe avec de nombreux composants interdependants. La configuration initiale et la resolution de problemes de connectivite entre services ont ete des defis formateurs.</p>

<p><strong>Kubernetes en temps limite</strong> :<br>
La session sur Kubernetes a ete realisee rapidement avec mon binome. Nous avons du executer les commandes sans toujours avoir le temps de comprendre chaque etape en profondeur. Le rapport redige a posteriori nous a permis de mieux assimiler les concepts.</p>

<hr>

<h2>PART C - Aspects Techniques Detailles</h2>

<h3 class="section-title">1. Fondamentaux de la virtualisation</h3>

<p><strong>Sans virtualisation</strong> :</p>

<p>Dans un environnement sans virtualisation, une seule application s'execute directement sur le systeme d'exploitation hote qui gere le materiel physique. Cette approche presente des limitations en termes d'isolation, de scalabilite et d'utilisation des ressources.</p>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_Cloud_Computing/No_Virt.png" style="max-width: 300px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Architecture sans virtualisation - une seule application sur l'OS hote</p>
</div>

<p><strong>Avec virtualisation</strong> :</p>

<p>La virtualisation permet d'executer plusieurs systemes d'exploitation et applications sur un meme materiel physique grace a un hyperviseur. Chaque machine virtuelle (VM) dispose de ses propres ressources virtualisees (CPU, RAM, stockage, reseau).</p>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_Cloud_Computing/Virt.png" style="max-width: 350px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Architecture avec virtualisation - plusieurs VMs sur un meme hote physique via un hyperviseur</p>
</div>

<p><strong>Avantages de la virtualisation</strong> :</p>
<ul>
<li><strong>Consolidation de serveurs</strong> : reduire le nombre de machines physiques</li>
<li><strong>Isolation</strong> : chaque VM est independante (panne d'une VM ne touche pas les autres)</li>
<li><strong>Flexibilite</strong> : deploiement rapide de nouveaux environnements</li>
<li><strong>Snapshots et migration</strong> : sauvegarde d'etat et migration a chaud</li>
<li><strong>Optimisation des ressources</strong> : meilleure utilisation du materiel</li>
</ul>

<h3 class="section-title">2. Hyperviseurs Type 1 et Type 2</h3>

<p>L'hyperviseur est le composant logiciel qui permet la virtualisation. Il existe deux types principaux :</p>

<p><strong>Hyperviseur de Type 1 (Bare Metal)</strong> :</p>

<p>L'hyperviseur s'execute directement sur le materiel physique, sans systeme d'exploitation hote intermediaire. Il offre de meilleures performances et une securite accrue car il a un acces direct au materiel.</p>

<p><strong>Exemples</strong> : VMware ESXi, Microsoft Hyper-V, Citrix XenServer, KVM</p>

<p><strong>Caracteristiques</strong> :</p>
<ul>
<li>Performances proches du natif</li>
<li>Gestion directe des ressources materielles</li>
<li>Utilise en production dans les datacenters</li>
<li>Securite renforcee (surface d'attaque reduite)</li>
</ul>

<p><strong>Hyperviseur de Type 2 (Hosted)</strong> :</p>

<p>L'hyperviseur s'execute comme une application sur un systeme d'exploitation hote existant. Il est plus simple a installer et a utiliser mais offre des performances legerement inferieures.</p>

<p><strong>Exemples</strong> : Oracle VirtualBox, VMware Workstation, Parallels Desktop</p>

<p><strong>Caracteristiques</strong> :</p>
<ul>
<li>Facile a installer sur un poste de travail</li>
<li>Ideal pour le developpement et les tests</li>
<li>Performances reduites (couche OS intermediaire)</li>
<li>Utilise principalement en environnement desktop</li>
</ul>

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

<table>
<tr><th>Critere</th><th>Type 1 (Bare Metal)</th><th>Type 2 (Hosted)</th></tr>
<tr><td>Installation</td><td>Directement sur le materiel</td><td>Sur un OS existant</td></tr>
<tr><td>Performance</td><td>Elevee</td><td>Moderee</td></tr>
<tr><td>Usage principal</td><td>Datacenters, production</td><td>Developpement, tests</td></tr>
<tr><td>Securite</td><td>Forte (acces direct)</td><td>Dependante de l'OS hote</td></tr>
<tr><td>Exemples</td><td>ESXi, KVM, Hyper-V</td><td>VirtualBox, VMware Workstation</td></tr>
</table>

<h3 class="section-title">3. Paravirtualisation</h3>

<p>La paravirtualisation est une technique ou le systeme d'exploitation invite est modifie pour communiquer directement avec l'hyperviseur via des "hypercalls", au lieu de simuler completement le materiel. Cela ameliore les performances par rapport a la virtualisation complete, car les appels systeme sont optimises pour l'environnement virtualise.</p>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_Cloud_Computing/Paravirtualization.png" style="max-width: 600px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Solutions de paravirtualisation - OpenNebula, OpenStack, Proxmox</p>
</div>

<p><strong>Avantages de la paravirtualisation</strong> :</p>
<ul>
<li>Performances ameliorees par rapport a la virtualisation complete</li>
<li>Meilleure gestion des E/S (entrees/sorties)</li>
<li>Overhead reduit</li>
</ul>

<p><strong>Inconvenients</strong> :</p>
<ul>
<li>Necessite la modification du systeme d'exploitation invite</li>
<li>Compatibilite limitee aux OS modifies</li>
</ul>

<h3 class="section-title">4. Conteneurs vs Machines Virtuelles</h3>

<p>Les conteneurs representent une evolution majeure par rapport aux machines virtuelles traditionnelles. Contrairement aux VMs qui virtualisent le materiel complet, les conteneurs partagent le noyau du systeme d'exploitation hote et n'embarquent que les bibliotheques et dependances necessaires a l'application.</p>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_Cloud_Computing/Containers.png" style="max-width: 600px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Ecosysteme conteneur - Container Linux, Solaris, Docker</p>
</div>

<table>
<tr><th>Critere</th><th>Machine Virtuelle</th><th>Conteneur</th></tr>
<tr><td>Isolation</td><td>Complete (OS separe)</td><td>Au niveau processus</td></tr>
<tr><td>Taille</td><td>Go (OS complet)</td><td>Mo (bibliotheques seulement)</td></tr>
<tr><td>Demarrage</td><td>Minutes</td><td>Secondes</td></tr>
<tr><td>Performance</td><td>Overhead (hyperviseur)</td><td>Proche du natif</td></tr>
<tr><td>Portabilite</td><td>Limitee</td><td>Excellente</td></tr>
<tr><td>Densite</td><td>~10-20 VMs par serveur</td><td>~100+ conteneurs par serveur</td></tr>
<tr><td>Securite</td><td>Forte (isolation materielle)</td><td>Moderee (noyau partage)</td></tr>
</table>

<p><strong>Cas d'utilisation des VMs</strong> :</p>
<ul>
<li>Isolation forte necessaire (multi-tenant, securite)</li>
<li>OS differents sur un meme hote</li>
<li>Applications legacy</li>
</ul>

<p><strong>Cas d'utilisation des conteneurs</strong> :</p>
<ul>
<li>Microservices</li>
<li>CI/CD (integration et deploiement continus)</li>
<li>Applications cloud-native</li>
<li>Environnements de developpement reproductibles</li>
</ul>

<h3 class="section-title">5. Docker et conteneurisation</h3>

<p>Docker est la plateforme de conteneurisation la plus populaire. Elle permet de creer, deployer et gerer des conteneurs de maniere efficace. Lors des travaux pratiques, j'ai appris a utiliser Docker pour virtualiser des applications dans des environnements isoles.</p>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_Cloud_Computing/Docker.png" style="max-width: 250px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Logo Docker</p>
</div>

<p><strong>Architecture Docker</strong> :</p>
<ul>
<li><strong>Docker Engine</strong> : le daemon qui gere les conteneurs</li>
<li><strong>Docker Image</strong> : template read-only contenant l'application et ses dependances</li>
<li><strong>Docker Container</strong> : instance d'execution d'une image</li>
<li><strong>Dockerfile</strong> : fichier de configuration pour construire une image</li>
<li><strong>Docker Hub</strong> : registre public d'images Docker</li>
<li><strong>Docker Compose</strong> : outil pour definir des applications multi-conteneurs</li>
</ul>

<p><strong>Commandes principales utilisees en TP</strong> :</p>

<pre><code class="language-bash"># Telecharger une image depuis Docker Hub
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
</code></pre>

<p><strong>Exemple de Dockerfile</strong> :</p>

<pre><code class="language-dockerfile">FROM ubuntu:20.04
RUN apt-get update &amp;&amp; apt-get install -y python3 pip
COPY app.py /app/
WORKDIR /app
EXPOSE 5000
CMD ["python3", "app.py"]
</code></pre>

<p><strong>Avantages de Docker</strong> :</p>
<ul>
<li>Portabilite ("Build once, run anywhere")</li>
<li>Reproductibilite des environnements</li>
<li>Isolation des applications</li>
<li>Demarrage rapide (secondes)</li>
<li>Ecosysteme riche (Docker Hub, Docker Compose)</li>
</ul>

<h3 class="section-title">6. Modeles de service Cloud : IaaS, PaaS, SaaS</h3>

<p>Le Cloud Computing propose differents niveaux d'abstraction pour les services, representes par trois modeles principaux :</p>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_Cloud_Computing/SDM.png" style="max-width: 500px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Modeles de service Cloud - IaaS, SaaS, PaaS et leurs niveaux d'abstraction</p>
</div>

<p><strong>IaaS (Infrastructure as a Service)</strong> :</p>

<p>Fournit les ressources d'infrastructure virtualisees (serveurs, stockage, reseau). L'utilisateur gere l'OS, les middlewares et les applications.</p>

<ul>
<li><strong>Exemples</strong> : AWS EC2, Google Compute Engine, Azure Virtual Machines, OpenStack</li>
<li><strong>Responsabilite utilisateur</strong> : OS, runtime, applications, donnees</li>
<li><strong>Responsabilite fournisseur</strong> : materiel, virtualisation, reseau</li>
<li><strong>Flexibilite</strong> : maximale (controle total sur l'infrastructure)</li>
</ul>

<p><strong>PaaS (Platform as a Service)</strong> :</p>

<p>Fournit une plateforme de developpement et de deploiement. L'utilisateur se concentre sur le code applicatif sans gerer l'infrastructure sous-jacente.</p>

<ul>
<li><strong>Exemples</strong> : Google App Engine, Heroku, Azure App Service, Cloud Foundry</li>
<li><strong>Responsabilite utilisateur</strong> : applications et donnees</li>
<li><strong>Responsabilite fournisseur</strong> : OS, runtime, middleware, infrastructure</li>
<li><strong>Flexibilite</strong> : moderee (contraintes de la plateforme)</li>
</ul>

<p><strong>SaaS (Software as a Service)</strong> :</p>

<p>Applications logicielles accessibles via le navigateur, entierement gerees par le fournisseur.</p>

<ul>
<li><strong>Exemples</strong> : Google Workspace, Microsoft 365, Salesforce, Dropbox</li>
<li><strong>Responsabilite utilisateur</strong> : donnees et parametres</li>
<li><strong>Responsabilite fournisseur</strong> : tout le reste</li>
<li><strong>Flexibilite</strong> : limitee (configuration seulement)</li>
</ul>

<table>
<tr><th>Aspect</th><th>IaaS</th><th>PaaS</th><th>SaaS</th></tr>
<tr><td>Controle</td><td>Total</td><td>Partiel</td><td>Minimal</td></tr>
<tr><td>Complexite</td><td>Elevee</td><td>Moyenne</td><td>Faible</td></tr>
<tr><td>Scalabilite</td><td>Manuelle/Semi-auto</td><td>Automatique</td><td>Automatique</td></tr>
<tr><td>Cout</td><td>Pay-per-use</td><td>Pay-per-use</td><td>Abonnement</td></tr>
<tr><td>Public cible</td><td>Admins systeme</td><td>Developpeurs</td><td>Utilisateurs finaux</td></tr>
</table>

<p><strong>Caracteristiques essentielles du Cloud (NIST)</strong> :</p>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_Cloud_Computing/Characteristics.png" style="max-width: 600px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Les caracteristiques essentielles du Cloud Computing selon le NIST</p>
</div>

<p>Les cinq caracteristiques essentielles definies par le NIST :</p>
<ul>
<li><strong>On-demand self-service</strong> : provisionnement automatique sans intervention humaine</li>
<li><strong>Broad network access</strong> : acces via des mecanismes standards (HTTP, API)</li>
<li><strong>Resource pooling</strong> : ressources mutualisees pour plusieurs clients (multi-tenant)</li>
<li><strong>Rapid elasticity</strong> : scalabilite automatique selon la demande</li>
<li><strong>Measured service</strong> : facturation a l'usage (pay-per-use)</li>
</ul>

<p><strong>Modeles de deploiement Cloud</strong> :</p>
<ul>
<li><strong>Cloud Public</strong> : infrastructure partagee, accessible a tous (AWS, Azure, GCP)</li>
<li><strong>Cloud Prive</strong> : infrastructure dediee a une organisation (OpenStack on-premise)</li>
<li><strong>Cloud Hybride</strong> : combinaison de cloud public et prive</li>
<li><strong>Cloud Communautaire</strong> : partage entre organisations ayant des besoins similaires</li>
</ul>

<h3 class="section-title">7. OpenStack - Plateforme Cloud Open-Source</h3>

<p>OpenStack est une plateforme open-source de cloud computing, principalement deployee comme IaaS. Elle permet la gestion de grands pools de ressources de calcul, de stockage et de reseau, le tout administrable via un tableau de bord (Horizon) ou via l'API OpenStack.</p>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_Cloud_Computing/sch_OpenStack.png" style="max-width: 500px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Architecture d'OpenStack et ses composants principaux</p>
</div>

<p><strong>Composants principaux d'OpenStack</strong> :</p>

<table>
<tr><th>Composant</th><th>Nom du projet</th><th>Fonction</th></tr>
<tr><td>Compute</td><td><strong>Nova</strong></td><td>Gestion des instances de machines virtuelles</td></tr>
<tr><td>Networking</td><td><strong>Neutron</strong></td><td>Reseaux virtuels, sous-reseaux, routeurs, firewalls</td></tr>
<tr><td>Image</td><td><strong>Glance</strong></td><td>Stockage et gestion des images de VMs</td></tr>
<tr><td>Identity</td><td><strong>Keystone</strong></td><td>Authentification, autorisation, catalogue de services</td></tr>
<tr><td>Dashboard</td><td><strong>Horizon</strong></td><td>Interface web d'administration</td></tr>
<tr><td>Block Storage</td><td><strong>Cinder</strong></td><td>Volumes de stockage persistants</td></tr>
<tr><td>Object Storage</td><td><strong>Swift</strong></td><td>Stockage objet distribue</td></tr>
<tr><td>Orchestration</td><td><strong>Heat</strong></td><td>Templates d'infrastructure (Infrastructure as Code)</td></tr>
</table>

<p><strong>Architecture OpenStack</strong> :</p>

<p>L'architecture OpenStack suit un modele de services distribues communiquant via des APIs REST. Keystone fournit l'authentification centralisee. Nova gere le cycle de vie des VMs en s'appuyant sur Glance pour les images, Neutron pour le reseau et Cinder pour le stockage.</p>

<p><strong>Manipulations realisees en TP</strong> :</p>
<ul>
<li>Creation de reseaux virtuels et sous-reseaux avec Neutron</li>
<li>Deploiement d'instances VM avec Nova</li>
<li>Configuration de regles de securite (security groups)</li>
<li>Utilisation du dashboard Horizon pour l'administration visuelle</li>
<li>Gestion des images avec Glance</li>
</ul>

<h3 class="section-title">8. Configuration reseau avec VirtualBox</h3>

<p>Les travaux pratiques m'ont permis de configurer des reseaux virtuels avec VirtualBox. J'ai appris a creer et configurer des machines virtuelles, tester leur connectivite, et mettre en place des regles de redirection de ports pour permettre la communication entre les VMs et l'hote.</p>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_Cloud_Computing/VirtualBox.png" style="max-width: 400px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Configuration reseau avec VirtualBox</p>
</div>

<p><strong>Types de reseau VirtualBox configures</strong> :</p>

<table>
<tr><th>Mode reseau</th><th>Acces Internet</th><th>Communication inter-VM</th><th>Acces depuis l'hote</th></tr>
<tr><td>NAT</td><td>Oui</td><td>Non</td><td>Via port forwarding</td></tr>
<tr><td>Bridged</td><td>Oui</td><td>Oui</td><td>Oui</td></tr>
<tr><td>Host-Only</td><td>Non</td><td>Oui</td><td>Oui</td></tr>
<tr><td>Internal</td><td>Non</td><td>Oui (meme reseau)</td><td>Non</td></tr>
</table>

<p><strong>Manipulations realisees</strong> :</p>
<ul>
<li>Configuration de reseaux prives et routeurs pour la communication entre differentes VMs</li>
<li>Mise en place de regles de port forwarding pour l'acces SSH</li>
<li>Tests de connectivite (ping, traceroute) entre VMs</li>
<li>Configuration de sous-reseaux isoles</li>
</ul>

<h3 class="section-title">9. Paradigme Edge Computing</h3>

<p>Le Edge Computing est un paradigme qui consiste a traiter les donnees au plus pres de leur source de generation, plutot que de les envoyer systematiquement vers un datacenter cloud centralise. Ce concept est fondamental pour les applications necessitant une faible latence, une bande passante reduite ou une souverainete des donnees.</p>

<p><strong>Motivations du Edge Computing</strong> :</p>
<ul>
<li><strong>Latence</strong> : les applications temps reel (vehicules autonomes, realite augmentee) ne peuvent pas tolerer les delais aller-retour vers le cloud</li>
<li><strong>Bande passante</strong> : les volumes de donnees generes par l'IoT saturent les liens reseau</li>
<li><strong>Souverainete des donnees</strong> : certaines reglementations imposent le traitement local des donnees</li>
<li><strong>Fiabilite</strong> : le fonctionnement doit continuer meme en cas de perte de connexion au cloud</li>
</ul>

<p><strong>Caracteristiques cles</strong> :</p>
<ul>
<li>Traitement local des donnees au plus pres des utilisateurs/capteurs</li>
<li>Reduction de la latence (de ~100ms a &lt;10ms)</li>
<li>Filtrage et aggregation des donnees avant envoi au cloud</li>
<li>Fonctionnement en mode deconnecte possible</li>
</ul>

<h3 class="section-title">10. Fog Computing</h3>

<p>Le Fog Computing, introduit par Cisco, est une extension du cloud computing qui rapproche les services de calcul, de stockage et de reseau des peripheriques edge. Il se situe comme une couche intermediaire entre les dispositifs IoT (edge) et le cloud centralise.</p>

<p><strong>Differences Fog vs Edge</strong> :</p>

<table>
<tr><th>Aspect</th><th>Edge Computing</th><th>Fog Computing</th></tr>
<tr><td>Localisation</td><td>Sur le dispositif ou tres proche</td><td>Entre edge et cloud</td></tr>
<tr><td>Capacite de calcul</td><td>Limitee</td><td>Moderee</td></tr>
<tr><td>Latence</td><td>Tres faible</td><td>Faible</td></tr>
<tr><td>Exemples</td><td>Capteurs, gateways IoT</td><td>Serveurs locaux, routeurs intelligents</td></tr>
<tr><td>Scope</td><td>Traitement immediat</td><td>Aggregation, pre-traitement</td></tr>
</table>

<p><strong>Architecture Fog Computing</strong> :</p>
<ol>
<li><strong>Couche Edge</strong> : capteurs et actionneurs (collecte de donnees brutes)</li>
<li><strong>Couche Fog</strong> : passerelles, serveurs locaux (pre-traitement, filtrage, decisions rapides)</li>
<li><strong>Couche Cloud</strong> : datacenters (analyse approfondie, stockage long terme, machine learning)</li>
</ol>

<h3 class="section-title">11. MEC - Multi-access Edge Computing</h3>

<p>Le MEC (Multi-access Edge Computing), standardise par l'ETSI, est un concept qui integre les capacites de calcul au niveau de l'infrastructure des operateurs de telecommunications, typiquement dans les stations de base ou les points d'acces du reseau.</p>

<p><strong>Caracteristiques du MEC</strong> :</p>
<ul>
<li>Integration avec l'infrastructure reseau des operateurs (4G/5G)</li>
<li>APIs standardisees pour l'acces aux informations reseau (localisation, QoS)</li>
<li>Hebergement d'applications tierces au plus pres du reseau d'acces</li>
<li>Faible latence garantie par la proximite avec les antennes</li>
</ul>

<p><strong>Cas d'utilisation MEC</strong> :</p>
<ul>
<li><strong>Vehicules connectes (V2X)</strong> : communication ultra-fiable et faible latence</li>
<li><strong>Realite augmentee/virtuelle</strong> : rendu en temps reel</li>
<li><strong>Gaming cloud</strong> : streaming de jeux avec latence minimale</li>
<li><strong>Video analytics</strong> : analyse de flux video en temps reel</li>
<li><strong>IoT industriel</strong> : controle de processus industriels</li>
</ul>

<h3 class="section-title">12. Continuum Cloud-Edge</h3>

<p>Le continuum cloud-edge represente une vision unifiee ou les ressources de calcul sont distribuees de maniere continue depuis les dispositifs edge jusqu'au cloud centralise. L'objectif est d'offrir une orchestration transparente qui place automatiquement les traitements la ou ils sont le plus pertinents.</p>

<p><strong>Principes du continuum</strong> :</p>
<ul>
<li><strong>Placement dynamique</strong> : les applications migrent entre edge, fog et cloud selon les besoins (latence, charge, cout)</li>
<li><strong>Orchestration unifiee</strong> : un plan de controle unique gere l'ensemble des ressources</li>
<li><strong>Heterogeneite</strong> : integration de ressources diverses (x86, ARM, GPU, FPGA)</li>
<li><strong>Elasticite</strong> : scalabilite horizontale et verticale a tous les niveaux</li>
</ul>

<p><strong>Gestion autonomique</strong> :</p>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_Cloud_Computing/Automatic.png" style="max-width: 400px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Boucle autonomique MAPE-K (Monitor, Analyze, Plan, Execute) pour la gestion du continuum cloud-edge</p>
</div>

<p>Le modele MAPE-K (Monitor, Analyze, Plan, Execute - Knowledge) permet une gestion autonomique des ressources du continuum :</p>
<ul>
<li><strong>Monitor</strong> : collecte des metriques (latence, charge CPU, bande passante)</li>
<li><strong>Analyze</strong> : detection d'anomalies et tendances</li>
<li><strong>Plan</strong> : decision de placement, migration, scaling</li>
<li><strong>Execute</strong> : application des decisions (deploiement, migration de conteneurs)</li>
<li><strong>Knowledge</strong> : base de connaissances partagee alimentant la boucle</li>
</ul>

<h3 class="section-title">13. Orchestration de conteneurs avec Kubernetes</h3>

<p>Kubernetes (K8s) est la plateforme standard pour l'orchestration de conteneurs a grande echelle. Elle automatise le deploiement, la mise a l'echelle et la gestion des applications conteneurisees.</p>

<p><strong>Architecture Kubernetes</strong> :</p>

<p><strong>Plan de controle (Control Plane)</strong> :</p>
<ul>
<li><strong>kube-apiserver</strong> : point d'entree pour toutes les operations (API REST)</li>
<li><strong>etcd</strong> : base de donnees cle-valeur distribuee (etat du cluster)</li>
<li><strong>kube-scheduler</strong> : placement des pods sur les noeuds</li>
<li><strong>kube-controller-manager</strong> : controleurs qui maintiennent l'etat desire</li>
</ul>

<p><strong>Noeuds Worker</strong> :</p>
<ul>
<li><strong>kubelet</strong> : agent sur chaque noeud qui gere les pods</li>
<li><strong>kube-proxy</strong> : gestion du reseau et du load balancing</li>
<li><strong>Container Runtime</strong> : Docker, containerd ou CRI-O</li>
</ul>

<p><strong>Concepts fondamentaux</strong> :</p>

<table>
<tr><th>Concept</th><th>Description</th></tr>
<tr><td><strong>Pod</strong></td><td>Unite de deploiement minimale (1+ conteneurs)</td></tr>
<tr><td><strong>Deployment</strong></td><td>Gestion declarative des pods (replicas, mises a jour)</td></tr>
<tr><td><strong>Service</strong></td><td>Exposition reseau stable pour un ensemble de pods</td></tr>
<tr><td><strong>Namespace</strong></td><td>Isolation logique au sein d'un cluster</td></tr>
<tr><td><strong>ConfigMap/Secret</strong></td><td>Configuration et donnees sensibles</td></tr>
<tr><td><strong>PersistentVolume</strong></td><td>Stockage persistant pour les pods</td></tr>
</table>

<p><strong>Exemple de deploiement YAML utilise en TP</strong> :</p>

<pre><code class="language-yaml">apiVersion: apps/v1
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
</code></pre>

<p><strong>Commandes Kubernetes utilisees en TP</strong> :</p>

<pre><code class="language-bash"># Deployer une application
kubectl apply -f deployment.yaml

# Voir les pods en cours d'execution
kubectl get pods

# Voir les services
kubectl get services

# Mettre a l'echelle un deploiement
kubectl scale deployment nginx-deployment --replicas=5

# Voir les logs d'un pod
kubectl logs &lt;nom-du-pod&gt;

# Description detaillee d'un pod
kubectl describe pod &lt;nom-du-pod&gt;
</code></pre>

<hr>

<h2>PART D - Analyse et Reflexion</h2>

<h3 class="section-title">Competences acquises</h3>

<p><strong>Virtualisation et conteneurisation</strong> :<br>
Maitrise des differences fondamentales entre VMs et conteneurs, des hyperviseurs Type 1 et Type 2, et des outils Docker et VirtualBox. Capacite a choisir la technologie adaptee selon le cas d'usage.</p>

<p><strong>Cloud Computing</strong> :<br>
Comprehension des modeles de service (IaaS, PaaS, SaaS) et de deploiement (public, prive, hybride). Experience pratique avec OpenStack pour le deploiement d'une infrastructure cloud.</p>

<p><strong>Edge Computing</strong> :<br>
Apprehension du paradigme edge et de ses variantes (Fog Computing, MEC). Comprehension du continuum cloud-edge et des enjeux d'orchestration dans un environnement distribue.</p>

<p><strong>Orchestration</strong> :<br>
Competence initiale avec Kubernetes pour le deploiement et la gestion de services conteneurises. Comprehension de l'architecture cluster et des fichiers de configuration YAML.</p>

<h3 class="section-title">Points cles a retenir</h3>

<p><strong>1. La virtualisation est le socle du cloud</strong> :<br>
Sans virtualisation (VMs ou conteneurs), le cloud computing n'existerait pas. Comprendre ces mecanismes est fondamental pour tout ingenieur cloud.</p>

<p><strong>2. Conteneurs et VMs sont complementaires</strong> :<br>
Les conteneurs ne remplacent pas les VMs. Chaque technologie a ses cas d'usage. En production, on utilise souvent des conteneurs deployes sur des VMs pour combiner les avantages des deux.</p>

<p><strong>3. Le edge computing repond a des besoins reels</strong> :<br>
L'IoT, la 5G et les applications temps reel rendent le edge computing indispensable. Le cloud seul ne suffit plus pour toutes les charges de travail.</p>

<p><strong>4. L'orchestration est essentielle a grande echelle</strong> :<br>
Kubernetes est devenu le standard de facto pour gerer des centaines de conteneurs. Maitriser cet outil est une competence tres demandee.</p>

<p><strong>5. Le continuum cloud-edge est l'avenir</strong> :<br>
La tendance est a l'integration transparente de toutes les couches (edge, fog, cloud) avec une orchestration unifiee.</p>

<h3 class="section-title">Retour d'experience</h3>

<p>J'ai developpe de nouvelles competences en architectures hybrides et leurs applications dans les environnements informatiques modernes. J'ai pu comprendre et utiliser l'ensemble des concepts abordes. Cependant, j'ai realise qu'il me faudra pratiquer ces outils a l'avenir pour ne pas les oublier, car je n'ai pas actuellement l'opportunite de les utiliser dans mon entreprise d'apprentissage.</p>

<p>La session sur Kubernetes ayant ete realisee rapidement avec mon binome, nous avons du passer vite et simplement lancer les commandes. Grace au rapport que nous avons redige, il a ete plus simple de comprendre les concepts dans un second temps.</p>

<h3 class="section-title">Mon avis</h3>

<p>Ce cours etait tres interessant. J'ai eu la chance d'apprendre de nombreux concepts que j'entends dans la vie courante pour certains metiers. Ce cours sera reellement utile pour mon parcours professionnel ou ces concepts pourraient etre appliques.</p>

<p>Le contenu du cours etait bien structure, partant des bases de la virtualisation et progressant graduellement vers des sujets plus complexes. Cette progression m'a aide a mieux comprendre puis a elargir mes connaissances vers des concepts plus avances.</p>

<p>Je me sens desormais plus confiant pour concevoir, deployer et gerer des solutions cloud-edge scalables.</p>

<p><strong>Applications professionnelles</strong> :</p>
<ul>
<li><strong>Ingenieur DevOps</strong> : deploiement d'applications conteneurisees sur Kubernetes, CI/CD</li>
<li><strong>Architecte Cloud</strong> : conception d'infrastructures cloud hybrides et multi-cloud</li>
<li><strong>Ingenieur IoT</strong> : deploiement d'architectures edge pour le traitement local des donnees</li>
<li><strong>Administrateur systeme</strong> : gestion d'infrastructures virtualisees et OpenStack</li>
<li><strong>Ingenieur Telecom</strong> : integration MEC dans les reseaux 5G</li>
</ul>

<p><strong>Liens avec les autres cours</strong> :</p>
<ul>
<li><a href="./emerging-network.html">Emerging Network Technologies</a> : SDN pour la virtualisation du reseau dans le cloud</li>
<li><a href="./middleware-iot.html">Middleware for IoT</a> : protocoles IoT deployes sur edge/cloud</li>
<li><a href="./embedded-ia-iot.html">Embedded IA for IoT</a> : inference IA sur les dispositifs edge</li>
<li><a href="./service-oriented-architecture.html">Service Oriented Architecture</a> : microservices deployes dans le cloud</li>
</ul>

<hr>

<h2>Documents de Cours</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">Cours Complet Cloud & Edge Computing</span>
        <span class="lang-en">Full Cloud & Edge Computing Course</span>
      </h4>
      <p>
        <span class="lang-fr">Cours complet sur le Cloud & Edge Computing : virtualisation, modeles de service, OpenStack, Edge Computing, Fog Computing, MEC, continuum cloud-edge.</span>
        <span class="lang-en">Complete course on Cloud & Edge Computing: virtualization, service models, OpenStack, Edge Computing, Fog Computing, MEC, cloud-edge continuum.</span>
      </p>
      <embed src="/cours-pdf/S9/Cloud/Cours_5ISS_CloudEdgeComputing.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/Cloud/Cours_5ISS_CloudEdgeComputing.pdf" target="_blank">
        <span class="lang-fr">Telecharger le cours</span>
        <span class="lang-en">Download the course</span>
      </a></p>
    </div>
  </div>
</div>

<hr>

<h2>Rapports et Projets</h2>

<div style="text-align: center;">
    <h3>
        <span class="lang-fr">Rapport de Projet Cloud Computing</span>
        <span class="lang-en">Cloud Computing Project Report</span>
    </h3>
</div>

<div style="display: flex; justify-content: center;">
    <embed src="/file/reports/S9/Boukouiss_Chanfreau_Cloud_Computing_Rapport.pdf" width="100%" height="800px" type="application/pdf">
</div>

<p style="text-align: center;">
    <a href="/file/reports/S9/Boukouiss_Chanfreau_Cloud_Computing_Rapport.pdf" target="_blank">
        <span class="lang-fr">Ouvrir le rapport complet</span>
        <span class="lang-en">Open the full report</span>
    </a>
</p>
<p style="text-align: center;">
    <a href="/img/BE_Cloud_Computing/Lab_Subject_cloud.pdf" target="_blank">
        <span class="lang-fr">Ouvrir le sujet de TP</span>
        <span class="lang-en">Open the lab subject</span>
    </a>
</p>

<hr>
<p><em>Cours suivi en 2024-2025 a l'INSA Toulouse, Departement Genie Electrique et Informatique, specialite ISS.</em></p>

</div>

<div class="lang-en">

<p><strong>Related courses</strong>:</p>
<ul>
<li><a href="./emerging-network.html">Emerging Network Technologies - S9</a> - SDN and network architectures</li>
<li><a href="./middleware-iot.html">Middleware for IoT - S9</a> - IoT protocols</li>
<li><a href="./embedded-ia-iot.html">Embedded IA for IoT - S9</a> - AI on Edge</li>
<li><a href="./service-oriented-architecture.html">Service Oriented Architecture - S9</a> - Cloud service architectures</li>
</ul>

<hr>

<h1>Cloud &amp; Edge Computing - Semester 9</h1>

<p><strong>Academic year</strong>: 2024-2025<br>
<strong>Instructor</strong>: Sami Yangui<br>
<strong>Category</strong>: Cloud, Virtualization, Edge Computing</p>

<hr>

<h2>PART A - General Presentation</h2>

<h3 class="section-title">Overview</h3>

<p>The Cloud &amp; Edge Computing course covers centralized cloud systems and decentralized edge solutions, preparing students to address modern technological challenges. Taught by Sami Yangui, this course explores virtualization technologies, cloud services and edge infrastructures. It focuses on designing, deploying and managing architectures that combine the low-latency advantages of edge computing with the scalability of cloud environments.</p>

<p>This training is particularly relevant in the current context, where the rise of IoT, real-time applications and networks requires expertise in these areas.</p>

<p><strong>Learning objectives</strong>:</p>
<ul>
<li>Understand the fundamentals of virtualization (Type 1 and Type 2 hypervisors, paravirtualization)</li>
<li>Master containerization with Docker and orchestration with Kubernetes</li>
<li>Understand cloud service models (IaaS, PaaS, SaaS)</li>
<li>Deploy and configure OpenStack environments</li>
<li>Understand the Edge Computing, Fog Computing and MEC (Multi-access Edge Computing) paradigm</li>
<li>Design integrated cloud-edge architectures</li>
</ul>

<h3 class="section-title">Position in the curriculum</h3>

<p>This module builds on previously acquired foundations:</p>
<ul>
<li><strong>Network Interconnection (S8)</strong>: TCP/IP fundamentals, routing, VLAN</li>
<li><strong>Operating Systems (S5)</strong>: process management, Unix systems</li>
<li><strong>Hardware Architecture (S6)</strong>: physical layer, server hardware</li>
</ul>

<p>It connects directly to other courses in the semester:</p>
<ul>
<li><strong>Emerging Network Technologies (S9)</strong>: SDN and network virtualization</li>
<li><strong>Middleware for IoT (S9)</strong>: IoT communication protocols deployed on cloud/edge</li>
<li><strong>Service Oriented Architecture (S9)</strong>: cloud service architectures</li>
</ul>

<hr>

<h2>PART B - Experience and Context</h2>

<h3 class="section-title">Organization and resources</h3>

<p>The module combined theory and intensive hands-on practice:</p>

<p><strong>Lectures</strong>:</p>
<ul>
<li>Introduction to Cloud Computing and its essential characteristics</li>
<li>Virtualization technologies (hypervisors, containers)</li>
<li>Cloud service models (IaaS, PaaS, SaaS) and deployment models</li>
<li>OpenStack architecture and its components</li>
<li>Edge Computing, Fog Computing and MEC</li>
<li>Cloud-Edge continuum and orchestration</li>
</ul>

<p><strong>Lab sessions</strong>:</p>
<ul>
<li><strong>Lab 1</strong>: Configuration of virtual networks with VirtualBox, inter-VM routing</li>
<li><strong>Lab 2</strong>: Creation and management of Docker containers, Dockerfiles, volumes</li>
<li><strong>Lab 3</strong>: Deployment of an OpenStack infrastructure (Nova, Neutron, Glance, Keystone)</li>
<li><strong>Lab 4</strong>: Container orchestration with Kubernetes, service deployment</li>
</ul>

<p><strong>Tools used</strong>:</p>
<ul>
<li><strong>VirtualBox</strong>: Type 2 virtualization for lab sessions</li>
<li><strong>Docker</strong>: application containerization</li>
<li><strong>Kubernetes</strong>: container orchestration</li>
<li><strong>OpenStack</strong>: open-source cloud platform (Nova, Neutron, Glance, Keystone, Horizon)</li>
<li><strong>Linux (Ubuntu)</strong>: host system for virtualized environments</li>
</ul>

<h3 class="section-title">My role</h3>

<p>As part of this course, I was responsible for:</p>
<ul>
<li>Learning and practicing virtualization techniques (VMs and containers)</li>
<li>Designing, deploying and managing hybrid architectures combining cloud and edge computing</li>
<li>Acquiring skills with tools such as Kubernetes, Docker and VirtualBox</li>
<li>Writing a comprehensive technical report on the lab work completed</li>
</ul>

<h3 class="section-title">Challenges encountered</h3>

<p><strong>VirtualBox network configuration</strong>:<br>
Setting up virtual networks (NAT, bridge, host-only) and understanding their interactions required time and methodology.</p>

<p><strong>OpenStack deployment</strong>:<br>
OpenStack is a complex platform with many interdependent components. The initial configuration and troubleshooting connectivity issues between services were formative challenges.</p>

<p><strong>Kubernetes under time constraints</strong>:<br>
The Kubernetes session was completed quickly with my partner. We had to execute commands without always having time to understand each step in depth. The report written afterwards helped us better absorb the concepts.</p>

<hr>

<h2>PART C - Detailed Technical Aspects</h2>

<h3 class="section-title">1. Virtualization fundamentals</h3>

<p><strong>Without virtualization</strong>:</p>

<p>In an environment without virtualization, a single application runs directly on the host operating system which manages the physical hardware. This approach has limitations in terms of isolation, scalability and resource utilization.</p>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_Cloud_Computing/No_Virt.png" style="max-width: 300px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Architecture without virtualization - a single application on the host OS</p>
</div>

<p><strong>With virtualization</strong>:</p>

<p>Virtualization allows running multiple operating systems and applications on the same physical hardware through a hypervisor. Each virtual machine (VM) has its own virtualized resources (CPU, RAM, storage, network).</p>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_Cloud_Computing/Virt.png" style="max-width: 350px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Architecture with virtualization - multiple VMs on a single physical host via a hypervisor</p>
</div>

<p><strong>Advantages of virtualization</strong>:</p>
<ul>
<li><strong>Server consolidation</strong>: reduce the number of physical machines</li>
<li><strong>Isolation</strong>: each VM is independent (failure of one VM does not affect the others)</li>
<li><strong>Flexibility</strong>: rapid deployment of new environments</li>
<li><strong>Snapshots and migration</strong>: state backup and live migration</li>
<li><strong>Resource optimization</strong>: better hardware utilization</li>
</ul>

<h3 class="section-title">2. Type 1 and Type 2 Hypervisors</h3>

<p>The hypervisor is the software component that enables virtualization. There are two main types:</p>

<p><strong>Type 1 Hypervisor (Bare Metal)</strong>:</p>

<p>The hypervisor runs directly on the physical hardware, without an intermediate host operating system. It offers better performance and enhanced security as it has direct access to the hardware.</p>

<p><strong>Examples</strong>: VMware ESXi, Microsoft Hyper-V, Citrix XenServer, KVM</p>

<p><strong>Characteristics</strong>:</p>
<ul>
<li>Near-native performance</li>
<li>Direct management of hardware resources</li>
<li>Used in production in datacenters</li>
<li>Enhanced security (reduced attack surface)</li>
</ul>

<p><strong>Type 2 Hypervisor (Hosted)</strong>:</p>

<p>The hypervisor runs as an application on an existing host operating system. It is simpler to install and use but offers slightly lower performance.</p>

<p><strong>Examples</strong>: Oracle VirtualBox, VMware Workstation, Parallels Desktop</p>

<p><strong>Characteristics</strong>:</p>
<ul>
<li>Easy to install on a workstation</li>
<li>Ideal for development and testing</li>
<li>Reduced performance (intermediate OS layer)</li>
<li>Primarily used in desktop environments</li>
</ul>

<div style="text-align: center; display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; margin: 20px 0;">
    <div>
        <img src="/img/BE_Cloud_Computing/H_type1.png" style="max-width: 350px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
        <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Type 1 Hypervisor (Bare Metal)</p>
    </div>
    <div>
        <img src="/img/BE_Cloud_Computing/H_type2.png" style="max-width: 350px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
        <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Type 2 Hypervisor (Hosted)</p>
    </div>
</div>

<table>
<tr><th>Criterion</th><th>Type 1 (Bare Metal)</th><th>Type 2 (Hosted)</th></tr>
<tr><td>Installation</td><td>Directly on hardware</td><td>On an existing OS</td></tr>
<tr><td>Performance</td><td>High</td><td>Moderate</td></tr>
<tr><td>Primary use</td><td>Datacenters, production</td><td>Development, testing</td></tr>
<tr><td>Security</td><td>Strong (direct access)</td><td>Dependent on host OS</td></tr>
<tr><td>Examples</td><td>ESXi, KVM, Hyper-V</td><td>VirtualBox, VMware Workstation</td></tr>
</table>

<h3 class="section-title">3. Paravirtualization</h3>

<p>Paravirtualization is a technique where the guest operating system is modified to communicate directly with the hypervisor through "hypercalls", instead of fully simulating the hardware. This improves performance compared to full virtualization, as system calls are optimized for the virtualized environment.</p>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_Cloud_Computing/Paravirtualization.png" style="max-width: 600px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Paravirtualization solutions - OpenNebula, OpenStack, Proxmox</p>
</div>

<p><strong>Advantages of paravirtualization</strong>:</p>
<ul>
<li>Improved performance compared to full virtualization</li>
<li>Better I/O management (input/output)</li>
<li>Reduced overhead</li>
</ul>

<p><strong>Disadvantages</strong>:</p>
<ul>
<li>Requires modification of the guest operating system</li>
<li>Compatibility limited to modified OSes</li>
</ul>

<h3 class="section-title">4. Containers vs Virtual Machines</h3>

<p>Containers represent a major evolution compared to traditional virtual machines. Unlike VMs which virtualize the complete hardware, containers share the host operating system kernel and only include the libraries and dependencies necessary for the application.</p>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_Cloud_Computing/Containers.png" style="max-width: 600px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Container ecosystem - Container Linux, Solaris, Docker</p>
</div>

<table>
<tr><th>Criterion</th><th>Virtual Machine</th><th>Container</th></tr>
<tr><td>Isolation</td><td>Complete (separate OS)</td><td>Process-level</td></tr>
<tr><td>Size</td><td>GB (complete OS)</td><td>MB (libraries only)</td></tr>
<tr><td>Startup</td><td>Minutes</td><td>Seconds</td></tr>
<tr><td>Performance</td><td>Overhead (hypervisor)</td><td>Near-native</td></tr>
<tr><td>Portability</td><td>Limited</td><td>Excellent</td></tr>
<tr><td>Density</td><td>~10-20 VMs per server</td><td>~100+ containers per server</td></tr>
<tr><td>Security</td><td>Strong (hardware isolation)</td><td>Moderate (shared kernel)</td></tr>
</table>

<p><strong>VM use cases</strong>:</p>
<ul>
<li>Strong isolation needed (multi-tenant, security)</li>
<li>Different OSes on the same host</li>
<li>Legacy applications</li>
</ul>

<p><strong>Container use cases</strong>:</p>
<ul>
<li>Microservices</li>
<li>CI/CD (continuous integration and deployment)</li>
<li>Cloud-native applications</li>
<li>Reproducible development environments</li>
</ul>

<h3 class="section-title">5. Docker and containerization</h3>

<p>Docker is the most popular containerization platform. It allows creating, deploying and managing containers efficiently. During the lab sessions, I learned to use Docker to virtualize applications in isolated environments.</p>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_Cloud_Computing/Docker.png" style="max-width: 250px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Docker Logo</p>
</div>

<p><strong>Docker architecture</strong>:</p>
<ul>
<li><strong>Docker Engine</strong>: the daemon that manages containers</li>
<li><strong>Docker Image</strong>: read-only template containing the application and its dependencies</li>
<li><strong>Docker Container</strong>: running instance of an image</li>
<li><strong>Dockerfile</strong>: configuration file for building an image</li>
<li><strong>Docker Hub</strong>: public Docker image registry</li>
<li><strong>Docker Compose</strong>: tool for defining multi-container applications</li>
</ul>

<p><strong>Main commands used in lab sessions</strong>:</p>

<pre><code class="language-bash"># Download an image from Docker Hub
docker pull ubuntu:20.04

# Launch a container in interactive mode
docker run -it --name mon_conteneur ubuntu:20.04 /bin/bash

# List active containers
docker ps

# List all containers (active and stopped)
docker ps -a

# Build an image from a Dockerfile
docker build -t mon_image .

# Expose a port and launch a container in the background
docker run -d -p 8080:80 --name serveur_web nginx

# Manage volumes for persistence
docker run -v /host/data:/container/data mon_image
</code></pre>

<p><strong>Dockerfile example</strong>:</p>

<pre><code class="language-dockerfile">FROM ubuntu:20.04
RUN apt-get update &amp;&amp; apt-get install -y python3 pip
COPY app.py /app/
WORKDIR /app
EXPOSE 5000
CMD ["python3", "app.py"]
</code></pre>

<p><strong>Advantages of Docker</strong>:</p>
<ul>
<li>Portability ("Build once, run anywhere")</li>
<li>Environment reproducibility</li>
<li>Application isolation</li>
<li>Fast startup (seconds)</li>
<li>Rich ecosystem (Docker Hub, Docker Compose)</li>
</ul>

<h3 class="section-title">6. Cloud service models: IaaS, PaaS, SaaS</h3>

<p>Cloud Computing offers different levels of abstraction for services, represented by three main models:</p>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_Cloud_Computing/SDM.png" style="max-width: 500px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Cloud service models - IaaS, SaaS, PaaS and their abstraction levels</p>
</div>

<p><strong>IaaS (Infrastructure as a Service)</strong>:</p>

<p>Provides virtualized infrastructure resources (servers, storage, network). The user manages the OS, middleware and applications.</p>

<ul>
<li><strong>Examples</strong>: AWS EC2, Google Compute Engine, Azure Virtual Machines, OpenStack</li>
<li><strong>User responsibility</strong>: OS, runtime, applications, data</li>
<li><strong>Provider responsibility</strong>: hardware, virtualization, network</li>
<li><strong>Flexibility</strong>: maximum (full control over infrastructure)</li>
</ul>

<p><strong>PaaS (Platform as a Service)</strong>:</p>

<p>Provides a development and deployment platform. The user focuses on application code without managing the underlying infrastructure.</p>

<ul>
<li><strong>Examples</strong>: Google App Engine, Heroku, Azure App Service, Cloud Foundry</li>
<li><strong>User responsibility</strong>: applications and data</li>
<li><strong>Provider responsibility</strong>: OS, runtime, middleware, infrastructure</li>
<li><strong>Flexibility</strong>: moderate (platform constraints)</li>
</ul>

<p><strong>SaaS (Software as a Service)</strong>:</p>

<p>Software applications accessible via the browser, fully managed by the provider.</p>

<ul>
<li><strong>Examples</strong>: Google Workspace, Microsoft 365, Salesforce, Dropbox</li>
<li><strong>User responsibility</strong>: data and settings</li>
<li><strong>Provider responsibility</strong>: everything else</li>
<li><strong>Flexibility</strong>: limited (configuration only)</li>
</ul>

<table>
<tr><th>Aspect</th><th>IaaS</th><th>PaaS</th><th>SaaS</th></tr>
<tr><td>Control</td><td>Full</td><td>Partial</td><td>Minimal</td></tr>
<tr><td>Complexity</td><td>High</td><td>Medium</td><td>Low</td></tr>
<tr><td>Scalability</td><td>Manual/Semi-auto</td><td>Automatic</td><td>Automatic</td></tr>
<tr><td>Cost</td><td>Pay-per-use</td><td>Pay-per-use</td><td>Subscription</td></tr>
<tr><td>Target audience</td><td>System admins</td><td>Developers</td><td>End users</td></tr>
</table>

<p><strong>Essential Cloud characteristics (NIST)</strong>:</p>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_Cloud_Computing/Characteristics.png" style="max-width: 600px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Essential characteristics of Cloud Computing according to NIST</p>
</div>

<p>The five essential characteristics defined by NIST:</p>
<ul>
<li><strong>On-demand self-service</strong>: automatic provisioning without human intervention</li>
<li><strong>Broad network access</strong>: access via standard mechanisms (HTTP, API)</li>
<li><strong>Resource pooling</strong>: pooled resources for multiple clients (multi-tenant)</li>
<li><strong>Rapid elasticity</strong>: automatic scalability according to demand</li>
<li><strong>Measured service</strong>: usage-based billing (pay-per-use)</li>
</ul>

<p><strong>Cloud deployment models</strong>:</p>
<ul>
<li><strong>Public Cloud</strong>: shared infrastructure, accessible to all (AWS, Azure, GCP)</li>
<li><strong>Private Cloud</strong>: infrastructure dedicated to an organization (OpenStack on-premise)</li>
<li><strong>Hybrid Cloud</strong>: combination of public and private cloud</li>
<li><strong>Community Cloud</strong>: shared among organizations with similar needs</li>
</ul>

<h3 class="section-title">7. OpenStack - Open-Source Cloud Platform</h3>

<p>OpenStack is an open-source cloud computing platform, primarily deployed as IaaS. It enables the management of large pools of compute, storage and network resources, all manageable via a dashboard (Horizon) or via the OpenStack API.</p>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_Cloud_Computing/sch_OpenStack.png" style="max-width: 500px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: OpenStack architecture and its main components</p>
</div>

<p><strong>Main OpenStack components</strong>:</p>

<table>
<tr><th>Component</th><th>Project name</th><th>Function</th></tr>
<tr><td>Compute</td><td><strong>Nova</strong></td><td>Virtual machine instance management</td></tr>
<tr><td>Networking</td><td><strong>Neutron</strong></td><td>Virtual networks, subnets, routers, firewalls</td></tr>
<tr><td>Image</td><td><strong>Glance</strong></td><td>VM image storage and management</td></tr>
<tr><td>Identity</td><td><strong>Keystone</strong></td><td>Authentication, authorization, service catalog</td></tr>
<tr><td>Dashboard</td><td><strong>Horizon</strong></td><td>Web administration interface</td></tr>
<tr><td>Block Storage</td><td><strong>Cinder</strong></td><td>Persistent storage volumes</td></tr>
<tr><td>Object Storage</td><td><strong>Swift</strong></td><td>Distributed object storage</td></tr>
<tr><td>Orchestration</td><td><strong>Heat</strong></td><td>Infrastructure templates (Infrastructure as Code)</td></tr>
</table>

<p><strong>OpenStack architecture</strong>:</p>

<p>The OpenStack architecture follows a distributed services model communicating via REST APIs. Keystone provides centralized authentication. Nova manages the VM lifecycle relying on Glance for images, Neutron for networking and Cinder for storage.</p>

<p><strong>Lab work performed</strong>:</p>
<ul>
<li>Creation of virtual networks and subnets with Neutron</li>
<li>Deployment of VM instances with Nova</li>
<li>Configuration of security rules (security groups)</li>
<li>Use of the Horizon dashboard for visual administration</li>
<li>Image management with Glance</li>
</ul>

<h3 class="section-title">8. Network configuration with VirtualBox</h3>

<p>The lab sessions allowed me to configure virtual networks with VirtualBox. I learned to create and configure virtual machines, test their connectivity, and set up port forwarding rules to enable communication between VMs and the host.</p>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_Cloud_Computing/VirtualBox.png" style="max-width: 400px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Network configuration with VirtualBox</p>
</div>

<p><strong>VirtualBox network types configured</strong>:</p>

<table>
<tr><th>Network mode</th><th>Internet access</th><th>Inter-VM communication</th><th>Access from host</th></tr>
<tr><td>NAT</td><td>Yes</td><td>No</td><td>Via port forwarding</td></tr>
<tr><td>Bridged</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Host-Only</td><td>No</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Internal</td><td>No</td><td>Yes (same network)</td><td>No</td></tr>
</table>

<p><strong>Lab work performed</strong>:</p>
<ul>
<li>Configuration of private networks and routers for communication between different VMs</li>
<li>Setting up port forwarding rules for SSH access</li>
<li>Connectivity testing (ping, traceroute) between VMs</li>
<li>Configuration of isolated subnets</li>
</ul>

<h3 class="section-title">9. Edge Computing paradigm</h3>

<p>Edge Computing is a paradigm that consists of processing data as close as possible to its source of generation, rather than systematically sending it to a centralized cloud datacenter. This concept is fundamental for applications requiring low latency, reduced bandwidth or data sovereignty.</p>

<p><strong>Edge Computing motivations</strong>:</p>
<ul>
<li><strong>Latency</strong>: real-time applications (autonomous vehicles, augmented reality) cannot tolerate round-trip delays to the cloud</li>
<li><strong>Bandwidth</strong>: the volumes of data generated by IoT saturate network links</li>
<li><strong>Data sovereignty</strong>: some regulations require local data processing</li>
<li><strong>Reliability</strong>: operation must continue even in case of loss of cloud connection</li>
</ul>

<p><strong>Key characteristics</strong>:</p>
<ul>
<li>Local data processing as close as possible to users/sensors</li>
<li>Latency reduction (from ~100ms to &lt;10ms)</li>
<li>Data filtering and aggregation before sending to the cloud</li>
<li>Disconnected mode operation possible</li>
</ul>

<h3 class="section-title">10. Fog Computing</h3>

<p>Fog Computing, introduced by Cisco, is an extension of cloud computing that brings compute, storage and network services closer to edge devices. It sits as an intermediate layer between IoT devices (edge) and the centralized cloud.</p>

<p><strong>Fog vs Edge differences</strong>:</p>

<table>
<tr><th>Aspect</th><th>Edge Computing</th><th>Fog Computing</th></tr>
<tr><td>Location</td><td>On the device or very close</td><td>Between edge and cloud</td></tr>
<tr><td>Compute capacity</td><td>Limited</td><td>Moderate</td></tr>
<tr><td>Latency</td><td>Very low</td><td>Low</td></tr>
<tr><td>Examples</td><td>Sensors, IoT gateways</td><td>Local servers, smart routers</td></tr>
<tr><td>Scope</td><td>Immediate processing</td><td>Aggregation, pre-processing</td></tr>
</table>

<p><strong>Fog Computing architecture</strong>:</p>
<ol>
<li><strong>Edge layer</strong>: sensors and actuators (raw data collection)</li>
<li><strong>Fog layer</strong>: gateways, local servers (pre-processing, filtering, quick decisions)</li>
<li><strong>Cloud layer</strong>: datacenters (in-depth analysis, long-term storage, machine learning)</li>
</ol>

<h3 class="section-title">11. MEC - Multi-access Edge Computing</h3>

<p>MEC (Multi-access Edge Computing), standardized by ETSI, is a concept that integrates computing capabilities at the level of telecommunications operators' infrastructure, typically in base stations or network access points.</p>

<p><strong>MEC characteristics</strong>:</p>
<ul>
<li>Integration with operators' network infrastructure (4G/5G)</li>
<li>Standardized APIs for accessing network information (location, QoS)</li>
<li>Hosting of third-party applications as close as possible to the access network</li>
<li>Low latency guaranteed by proximity to antennas</li>
</ul>

<p><strong>MEC use cases</strong>:</p>
<ul>
<li><strong>Connected vehicles (V2X)</strong>: ultra-reliable and low-latency communication</li>
<li><strong>Augmented/virtual reality</strong>: real-time rendering</li>
<li><strong>Cloud gaming</strong>: game streaming with minimal latency</li>
<li><strong>Video analytics</strong>: real-time video stream analysis</li>
<li><strong>Industrial IoT</strong>: industrial process control</li>
</ul>

<h3 class="section-title">12. Cloud-Edge continuum</h3>

<p>The cloud-edge continuum represents a unified vision where computing resources are continuously distributed from edge devices to the centralized cloud. The goal is to provide seamless orchestration that automatically places processing where it is most relevant.</p>

<p><strong>Continuum principles</strong>:</p>
<ul>
<li><strong>Dynamic placement</strong>: applications migrate between edge, fog and cloud according to needs (latency, load, cost)</li>
<li><strong>Unified orchestration</strong>: a single control plane manages all resources</li>
<li><strong>Heterogeneity</strong>: integration of diverse resources (x86, ARM, GPU, FPGA)</li>
<li><strong>Elasticity</strong>: horizontal and vertical scalability at all levels</li>
</ul>

<p><strong>Autonomic management</strong>:</p>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_Cloud_Computing/Automatic.png" style="max-width: 400px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: MAPE-K autonomic loop (Monitor, Analyze, Plan, Execute) for cloud-edge continuum management</p>
</div>

<p>The MAPE-K model (Monitor, Analyze, Plan, Execute - Knowledge) enables autonomic management of continuum resources:</p>
<ul>
<li><strong>Monitor</strong>: metric collection (latency, CPU load, bandwidth)</li>
<li><strong>Analyze</strong>: anomaly and trend detection</li>
<li><strong>Plan</strong>: placement, migration, scaling decisions</li>
<li><strong>Execute</strong>: application of decisions (deployment, container migration)</li>
<li><strong>Knowledge</strong>: shared knowledge base feeding the loop</li>
</ul>

<h3 class="section-title">13. Container orchestration with Kubernetes</h3>

<p>Kubernetes (K8s) is the standard platform for large-scale container orchestration. It automates the deployment, scaling and management of containerized applications.</p>

<p><strong>Kubernetes architecture</strong>:</p>

<p><strong>Control Plane</strong>:</p>
<ul>
<li><strong>kube-apiserver</strong>: entry point for all operations (REST API)</li>
<li><strong>etcd</strong>: distributed key-value database (cluster state)</li>
<li><strong>kube-scheduler</strong>: pod placement on nodes</li>
<li><strong>kube-controller-manager</strong>: controllers that maintain the desired state</li>
</ul>

<p><strong>Worker Nodes</strong>:</p>
<ul>
<li><strong>kubelet</strong>: agent on each node that manages pods</li>
<li><strong>kube-proxy</strong>: network and load balancing management</li>
<li><strong>Container Runtime</strong>: Docker, containerd or CRI-O</li>
</ul>

<p><strong>Fundamental concepts</strong>:</p>

<table>
<tr><th>Concept</th><th>Description</th></tr>
<tr><td><strong>Pod</strong></td><td>Minimum deployment unit (1+ containers)</td></tr>
<tr><td><strong>Deployment</strong></td><td>Declarative pod management (replicas, updates)</td></tr>
<tr><td><strong>Service</strong></td><td>Stable network exposure for a set of pods</td></tr>
<tr><td><strong>Namespace</strong></td><td>Logical isolation within a cluster</td></tr>
<tr><td><strong>ConfigMap/Secret</strong></td><td>Configuration and sensitive data</td></tr>
<tr><td><strong>PersistentVolume</strong></td><td>Persistent storage for pods</td></tr>
</table>

<p><strong>YAML deployment example used in lab</strong>:</p>

<pre><code class="language-yaml">apiVersion: apps/v1
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
</code></pre>

<p><strong>Kubernetes commands used in lab</strong>:</p>

```bash
# Deploy an application
kubectl apply -f deployment.yaml

# View running pods
kubectl get pods

# View services
kubectl get services

# Scale a deployment
kubectl scale deployment nginx-deployment --replicas=5

# View pod logs
kubectl logs <pod-name>

# Detailed description of a pod
kubectl describe pod <pod-name>
```

<hr>

<h2>PART D - Analysis and Reflection</h2>

<h3 class="section-title">Skills acquired</h3>

<p><strong>Virtualization and containerization</strong>:<br>
Mastery of the fundamental differences between VMs and containers, Type 1 and Type 2 hypervisors, and Docker and VirtualBox tools. Ability to choose the appropriate technology according to the use case.</p>

<p><strong>Cloud Computing</strong>:<br>
Understanding of service models (IaaS, PaaS, SaaS) and deployment models (public, private, hybrid). Hands-on experience with OpenStack for deploying a cloud infrastructure.</p>

<p><strong>Edge Computing</strong>:<br>
Understanding of the edge paradigm and its variants (Fog Computing, MEC). Understanding of the cloud-edge continuum and orchestration challenges in a distributed environment.</p>

<p><strong>Orchestration</strong>:<br>
Initial competency with Kubernetes for deploying and managing containerized services. Understanding of cluster architecture and YAML configuration files.</p>

<h3 class="section-title">Key takeaways</h3>

<p><strong>1. Virtualization is the foundation of the cloud</strong>:<br>
Without virtualization (VMs or containers), cloud computing would not exist. Understanding these mechanisms is fundamental for any cloud engineer.</p>

<p><strong>2. Containers and VMs are complementary</strong>:<br>
Containers do not replace VMs. Each technology has its use cases. In production, containers are often deployed on VMs to combine the advantages of both.</p>

<p><strong>3. Edge computing addresses real needs</strong>:<br>
IoT, 5G and real-time applications make edge computing essential. The cloud alone is no longer sufficient for all workloads.</p>

<p><strong>4. Orchestration is essential at scale</strong>:<br>
Kubernetes has become the de facto standard for managing hundreds of containers. Mastering this tool is a highly sought-after skill.</p>

<p><strong>5. The cloud-edge continuum is the future</strong>:<br>
The trend is toward seamless integration of all layers (edge, fog, cloud) with unified orchestration.</p>

<h3 class="section-title">Feedback</h3>

<p>I developed new skills in hybrid architectures and their applications in modern computing environments. I was able to understand and use all the concepts covered. However, I realized that I will need to practice these tools in the future to avoid forgetting them, as I do not currently have the opportunity to use them in my apprenticeship company.</p>

<p>Since the Kubernetes session was completed quickly with my partner, we had to rush through and simply run the commands. Thanks to the report we wrote, it was easier to understand the concepts afterwards.</p>

<h3 class="section-title">My opinion</h3>

<p>This course was very interesting. I had the chance to learn many concepts that I hear in daily life for certain professions. This course will be truly useful for my career where these concepts could be applied.</p>

<p>The course content was well structured, starting from the basics of virtualization and gradually progressing to more complex topics. This progression helped me better understand and then broaden my knowledge toward more advanced concepts.</p>

<p>I now feel more confident in designing, deploying and managing scalable cloud-edge solutions.</p>

<p><strong>Professional applications</strong>:</p>
<ul>
<li><strong>DevOps Engineer</strong>: deployment of containerized applications on Kubernetes, CI/CD</li>
<li><strong>Cloud Architect</strong>: design of hybrid and multi-cloud cloud infrastructures</li>
<li><strong>IoT Engineer</strong>: deployment of edge architectures for local data processing</li>
<li><strong>System Administrator</strong>: management of virtualized infrastructures and OpenStack</li>
<li><strong>Telecom Engineer</strong>: MEC integration in 5G networks</li>
</ul>

<p><strong>Links with other courses</strong>:</p>
<ul>
<li><a href="./emerging-network.html">Emerging Network Technologies</a>: SDN for network virtualization in the cloud</li>
<li><a href="./middleware-iot.html">Middleware for IoT</a>: IoT protocols deployed on edge/cloud</li>
<li><a href="./embedded-ia-iot.html">Embedded IA for IoT</a>: AI inference on edge devices</li>
<li><a href="./service-oriented-architecture.html">Service Oriented Architecture</a>: microservices deployed in the cloud</li>
</ul>

<hr>

<h2>Course Documents</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">Cours Complet Cloud & Edge Computing</span>
        <span class="lang-en">Full Cloud & Edge Computing Course</span>
      </h4>
      <p>
        <span class="lang-fr">Cours complet sur le Cloud & Edge Computing : virtualisation, modeles de service, OpenStack, Edge Computing, Fog Computing, MEC, continuum cloud-edge.</span>
        <span class="lang-en">Complete course on Cloud & Edge Computing: virtualization, service models, OpenStack, Edge Computing, Fog Computing, MEC, cloud-edge continuum.</span>
      </p>
      <embed src="/cours-pdf/S9/Cloud/Cours_5ISS_CloudEdgeComputing.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/Cloud/Cours_5ISS_CloudEdgeComputing.pdf" target="_blank">
        <span class="lang-fr">Telecharger le cours</span>
        <span class="lang-en">Download the course</span>
      </a></p>
    </div>
  </div>
</div>

<hr>

<h2>Reports and Projects</h2>

<div style="text-align: center;">
    <h3>
        <span class="lang-fr">Rapport de Projet Cloud Computing</span>
        <span class="lang-en">Cloud Computing Project Report</span>
    </h3>
</div>

<div style="display: flex; justify-content: center;">
    <embed src="/file/reports/S9/Boukouiss_Chanfreau_Cloud_Computing_Rapport.pdf" width="100%" height="800px" type="application/pdf">
</div>

<p style="text-align: center;">
    <a href="/file/reports/S9/Boukouiss_Chanfreau_Cloud_Computing_Rapport.pdf" target="_blank">
        <span class="lang-fr">Ouvrir le rapport complet</span>
        <span class="lang-en">Open the full report</span>
    </a>
</p>
<p style="text-align: center;">
    <a href="/img/BE_Cloud_Computing/Lab_Subject_cloud.pdf" target="_blank">
        <span class="lang-fr">Ouvrir le sujet de TP</span>
        <span class="lang-en">Open the lab subject</span>
    </a>
</p>

<hr>

<p><em>Course taken in 2024-2025 at INSA Toulouse, Department of Electrical and Computer Engineering, ISS specialization.</em></p>

</div>

<div class="back-nav">
    <a href="./my-courses-2024-2025.html" data-i18n-html="back-courses-2024-2025">&larr; Retour aux Cours 2024-2025</a>
</div>

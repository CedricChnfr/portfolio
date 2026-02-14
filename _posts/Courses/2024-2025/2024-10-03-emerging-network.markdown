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
<li><a href="./cloud-edge.html">Cloud &amp; Edge Computing - S9</a> - SDN pour Cloud/Edge</li>
<li><a href="../2023-2024/2024-10-03-interconnexion-reseau.html">Interconnexion Reseau - S8</a> - Fondamentaux reseaux</li>
</ul>

<hr>

<h1>Emerging Network Technologies - Semestre 9</h1>

<p><strong>Annee academique</strong> : 2024-2025<br>
<strong>Categorie</strong> : Reseaux emergents et programmabilite reseau<br>
<strong>Enseignant</strong> : S. Abdellatif</p>

<hr>

<h2>PART A - Presentation Generale</h2>

<h3 class="section-title">Vue d'ensemble</h3>

<p>Le cours "Emerging Network Technologies", dispense par S. Abdellatif a l'INSA Toulouse, explore les avancees majeures dans le domaine des technologies reseau. Il se concentre sur trois piliers fondamentaux des reseaux modernes : le <strong>Software-Defined Networking (SDN)</strong>, la <strong>Network Functions Virtualization (NFV)</strong> et le protocole <strong>LISP (Locator/ID Separation Protocol)</strong>. Ces technologies constituent la base de la transformation des infrastructures reseau traditionnelles vers des architectures programmables, flexibles et virtualisees.</p>

<p>Ce cours est particulierement pertinent dans le contexte actuel ou les reseaux traditionnels, bases sur des equipements proprietaires avec des plans de controle et de donnees integres, montrent leurs limites face aux exigences de scalabilite, d'agilite et d'automatisation des environnements cloud, IoT et 5G.</p>

<p><strong>Objectifs pedagogiques</strong> :</p>
<ul>
<li>Comprendre la separation du plan de controle et du plan de donnees (paradigme SDN)</li>
<li>Maitriser le protocole OpenFlow et son role dans l'architecture SDN</li>
<li>Configurer et administrer Open vSwitch (OVS) pour la commutation virtuelle</li>
<li>Deployer et programmer des controleurs SDN (Ryu, OpenDaylight, ONOS)</li>
<li>Comprendre les principes de la NFV et l'architecture MANO</li>
<li>Apprehender le protocole LISP et la separation identifiant/localisateur</li>
<li>Developper des applications de controle reseau en mode reactif et proactif</li>
<li>Concevoir des topologies SDN et gerer les problemes de boucles reseau</li>
</ul>

<h3 class="section-title">Position dans le cursus</h3>

<p>Ce module s'appuie sur les bases acquises precedemment :</p>
<ul>
<li><strong>Reseau (S5)</strong> : modele OSI, Ethernet, IP, TCP/UDP</li>
<li><strong>Interconnexion Reseau (S8)</strong> : routage (OSPF, BGP), VLANs, commutation, QoS</li>
<li><strong>Architecture Materielle (S6)</strong> : couche physique, signaux</li>
</ul>

<p>Il prepare a :</p>
<ul>
<li><strong>Cloud et Edge Computing (S9)</strong> : virtualisation, orchestration, Kubernetes</li>
<li><strong>IoT (S9)</strong> : protocoles specifiques, contraintes reseaux embarques</li>
<li><strong>Carriere professionnelle</strong> : ingenieur reseau, architecte SDN/NFV, DevOps reseau</li>
</ul>

<h3 class="section-title">Organisation du module</h3>

<table>
<tr><th>Element</th><th>Volume</th><th>Description</th></tr>
<tr><td>Cours magistraux</td><td>~10h</td><td>Theorie SDN, NFV, LISP, architectures</td></tr>
<tr><td>Travaux pratiques</td><td>~12h</td><td>Configuration OVS, OpenFlow, controleurs Ryu</td></tr>
<tr><td>Projet/Rapport</td><td>-</td><td>Rapport SDN &amp; NFV</td></tr>
</table>

<hr>

<h2>PART B - Experience et Contexte</h2>

<h3 class="section-title">Environnement et contexte</h3>

<p>Durant ce cours, j'ai travaille dans un environnement de laboratoire equipe de materiel professionnel pour l'experimentation SDN/OpenFlow. L'infrastructure comprenait :</p>

<ul>
<li><strong>4 commutateurs Pica8</strong> compatibles OpenFlow, equipes de 48 ports Gigabit Ethernet chacun</li>
<li><strong>12 PCs</strong> equipes de multiples cartes Ethernet, servant de routeurs et/ou de machines Linux</li>
<li><strong>Cables Ethernet</strong> (paires torsadees non blindees avec connecteurs RJ45), croises et droits</li>
<li><strong>Reseau de gestion</strong> separe du reseau de donnees (mode "out-of-band")</li>
</ul>

<p>Ce contexte permettait une immersion complete dans les architectures SDN reelles, loin des simulations simplifiees. La manipulation d'equipements physiques Pica8 avec Open vSwitch a donne une dimension concrete aux concepts theoriques. Le deploiement progressif, depuis un simple pont OVS jusqu'a une topologie maillees multi-commutateurs avec controleur centralise, a permis de comprendre chaque brique de l'architecture SDN.</p>

<h3 class="section-title">Outils utilises</h3>

<table>
<tr><th>Outil</th><th>Role</th><th>Utilisation</th></tr>
<tr><td><strong>Open vSwitch (OVS)</strong></td><td>Commutateur virtuel</td><td>Creation de ponts logiques, gestion des flux</td></tr>
<tr><td><strong>Ryu</strong></td><td>Controleur SDN</td><td>Programmation d'applications de controle reseau</td></tr>
<tr><td><strong>ovs-vsctl</strong></td><td>CLI d'administration OVS</td><td>Configuration des ponts et ports</td></tr>
<tr><td><strong>ovs-ofctl</strong></td><td>CLI OpenFlow pour OVS</td><td>Installation/suppression de regles de flux</td></tr>
<tr><td><strong>Pica8 picOS</strong></td><td>Systeme d'exploitation des commutateurs</td><td>Mode OVS/OpenFlow</td></tr>
<tr><td><strong>Wireshark</strong></td><td>Analyseur de paquets</td><td>Observation des echanges OpenFlow</td></tr>
<tr><td><strong>Python</strong></td><td>Programmation</td><td>Developpement d'applications controleur Ryu</td></tr>
</table>

<h3 class="section-title">Mon role</h3>

<p>Dans ce cours, j'etais responsable de :</p>
<ul>
<li>Comprendre les principes du SDN, de la NFV et du protocole OpenFlow</li>
<li>Configurer des instances OVS sur les commutateurs Pica8</li>
<li>Installer manuellement des regles OpenFlow pour controler le comportement du reseau</li>
<li>Attacher et configurer un controleur Ryu pour le management centralise</li>
<li>Deployer des topologies reseau complexes (maillees) et gerer les problemes de boucles</li>
<li>Analyser le comportement reactif et proactif du controleur</li>
<li>Rediger un rapport technique sur SDN et NFV</li>
</ul>

<hr>

<h2>PART C - Aspects Techniques Detailles</h2>

<h3 class="section-title">1. Software-Defined Networking (SDN) - Principes fondamentaux</h3>

<p>Le SDN represente un changement de paradigme fondamental dans l'architecture des reseaux. Dans les reseaux traditionnels, chaque equipement (routeur, commutateur) integre a la fois le <strong>plan de controle</strong> (decisions de routage, protocoles) et le <strong>plan de donnees</strong> (acheminement effectif des paquets). Cette architecture distribuee presente plusieurs limitations : complexite de gestion, manque de vision globale, difficulte d'evolution, et dependance aux equipements proprietaires.</p>

<p><strong>Architecture SDN a trois couches</strong> :</p>

<p>Le SDN repose sur une architecture en trois couches distinctes :</p>

<table>
<tr><th>Couche</th><th>Nom</th><th>Role</th><th>Exemples</th></tr>
<tr><td><strong>Couche Application</strong></td><td>Application Plane</td><td>Applications de controle reseau</td><td>Firewall, Load Balancer, QoS Manager</td></tr>
<tr><td><strong>Couche Controle</strong></td><td>Control Plane</td><td>Decisions de routage, vision globale</td><td>Ryu, OpenDaylight, ONOS, Floodlight</td></tr>
<tr><td><strong>Couche Infrastructure</strong></td><td>Data Plane</td><td>Acheminement des paquets selon les regles</td><td>Open vSwitch, commutateurs OpenFlow</td></tr>
</table>

<p><strong>Interfaces de communication</strong> :</p>

<ul>
<li><strong>Southbound API (ex: OpenFlow)</strong> : interface entre le controleur et les equipements reseau. Permet au controleur de programmer les tables de flux des commutateurs.</li>
<li><strong>Northbound API (ex: REST API)</strong> : interface entre le controleur et les applications. Permet aux applications de demander des services reseau au controleur.</li>
<li><strong>Eastbound/Westbound</strong> : communication entre controleurs distribues pour la scalabilite.</li>
</ul>

<p><strong>Avantages du SDN</strong> :</p>
<ul>
<li><strong>Programmabilite</strong> : le reseau peut etre programme et automatise via des APIs</li>
<li><strong>Vision globale</strong> : le controleur centralise a une vue complete de la topologie</li>
<li><strong>Agilite</strong> : modification rapide du comportement reseau sans reconfigurer chaque equipement</li>
<li><strong>Independance materielle</strong> : separation entre le logiciel de controle et le materiel</li>
<li><strong>Innovation acceleree</strong> : possibilite de deployer de nouveaux services reseau en logiciel</li>
</ul>

<h3 class="section-title">2. Protocole OpenFlow</h3>

<p>OpenFlow est le protocole standard de la <strong>Southbound API</strong> du SDN. Il definit la communication entre le controleur SDN et les commutateurs OpenFlow, permettant au controleur de programmer directement les tables de flux des equipements reseau.</p>

<p><strong>Principes de fonctionnement</strong> :</p>

<p>Un commutateur OpenFlow possede une ou plusieurs <strong>tables de flux (flow tables)</strong>. Chaque entree dans une table de flux contient :</p>

<table>
<tr><th>Champ</th><th>Description</th></tr>
<tr><td><strong>Match fields</strong></td><td>Criteres de correspondance (port entree, adresses MAC/IP, ports TCP/UDP, VLAN, etc.)</td></tr>
<tr><td><strong>Priority</strong></td><td>Priorite de la regle (regles avec priorite plus elevee evaluees en premier)</td></tr>
<tr><td><strong>Counters</strong></td><td>Compteurs de paquets et d'octets correspondants</td></tr>
<tr><td><strong>Instructions/Actions</strong></td><td>Actions a effectuer (forward, drop, modifier en-tete, envoyer au controleur)</td></tr>
<tr><td><strong>Timeouts</strong></td><td>Duree de validite de la regle (idle timeout, hard timeout)</td></tr>
<tr><td><strong>Cookie</strong></td><td>Identifiant opaque defini par le controleur</td></tr>
</table>

<p><strong>Processus de traitement d'un paquet</strong> :</p>

<ol>
<li>Un paquet arrive sur un port du commutateur</li>
<li>Le commutateur compare les champs du paquet aux entrees de la table de flux</li>
<li>Si une correspondance est trouvee : executer les actions associees</li>
<li>Si aucune correspondance : envoyer un message <strong>Packet-In</strong> au controleur</li>
<li>Le controleur analyse le paquet et repond avec un <strong>Packet-Out</strong> ou installe une nouvelle regle via <strong>Flow-Mod</strong></li>
</ol>

<p><strong>Messages OpenFlow principaux</strong> :</p>

<table>
<tr><th>Message</th><th>Direction</th><th>Description</th></tr>
<tr><td><strong>Packet-In</strong></td><td>Switch &rarr; Controleur</td><td>Notification d'un paquet sans correspondance</td></tr>
<tr><td><strong>Packet-Out</strong></td><td>Controleur &rarr; Switch</td><td>Instruction de traitement pour un paquet</td></tr>
<tr><td><strong>Flow-Mod</strong></td><td>Controleur &rarr; Switch</td><td>Ajout/modification/suppression d'une regle de flux</td></tr>
<tr><td><strong>Hello</strong></td><td>Bidirectionnel</td><td>Etablissement de la connexion OpenFlow</td></tr>
<tr><td><strong>Features-Request/Reply</strong></td><td>Bidirectionnel</td><td>Decouverte des capacites du commutateur</td></tr>
<tr><td><strong>Stats-Request/Reply</strong></td><td>Bidirectionnel</td><td>Consultation des statistiques</td></tr>
</table>

<p><strong>Versions OpenFlow</strong> : 1.0 (basique, une seule table), 1.3 (tables multiples, groupes, metres), 1.4, 1.5 (dernieres evolutions).</p>

<h3 class="section-title">3. Open vSwitch (OVS) - Commutation virtuelle</h3>

<p>Open vSwitch est un commutateur virtuel multi-couches concu pour permettre l'automatisation reseau par extensions programmables. Il supporte les protocoles de gestion standard (OpenFlow, sFlow, SPAN, LACP, 802.1Q) et est largement deploye dans les environnements de virtualisation et de cloud computing.</p>

<p><strong>Architecture OVS</strong> :</p>
<ul>
<li><strong>ovsdb-server</strong> : serveur de base de donnees de configuration</li>
<li><strong>ovs-vswitchd</strong> : daemon principal du commutateur, gere les tables de flux</li>
<li><strong>ovs-vsctl</strong> : outil CLI pour la configuration (ponts, ports, controleurs)</li>
<li><strong>ovs-ofctl</strong> : outil CLI pour la gestion des flux OpenFlow</li>
</ul>

<p><strong>Configuration initiale d'un pont OVS</strong> :</p>

<p>Creation d'une instance de pont logique et attachement des ports physiques :</p>

<pre><code class="language-bash"># Redemarrage des processus OVS
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
</code></pre>

<p><strong>Comportement par defaut</strong> :</p>

<p>Sans regle explicite, le pont OVS ne sait pas comment acheminer les paquets. On peut ajouter une regle par defaut qui transforme le commutateur en switch L2 classique :</p>

<pre><code class="language-bash">admin@picOS-OVS$ ovs-ofctl add-flow br0 ,action=normal
</code></pre>

<h3 class="section-title">4. Installation manuelle de regles OpenFlow</h3>

<p>L'installation manuelle de regles OpenFlow permet de comprendre finement le mecanisme de programmation du plan de donnees. Plusieurs niveaux de granularite sont possibles.</p>

<p><strong>Niveau 1 - Regles basees sur le port d'entree</strong> :</p>

<p>Regles simples redirigeant le trafic d'un port vers d'autres ports, sans distinction de contenu :</p>

<pre><code class="language-bash"># Suppression de toutes les regles existantes
admin@picOS-OVS$ ovs-ofctl del-flows br0

# Regles de redirection basees sur les ports d'entree
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=10,actions=output:13,16
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=13,actions=output:10,16
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=16,actions=output:10,13
</code></pre>

<p><strong>Niveau 2 - Regles avec filtrage IP (granularite fine)</strong> :</p>

<p>Pour un controle plus precis, on filtre par adresse IP de destination, avec gestion separee de l'ARP :</p>

<pre><code class="language-bash">admin@picOS-OVS$ ovs-ofctl del-flows br0

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
</code></pre>

<p><strong>Niveau 3 - Regles applicatives (filtrage protocolaire)</strong> :</p>

<p>Pour un controle au niveau applicatif, on filtre sur les protocoles de transport et les ports :</p>

<pre><code class="language-bash"># Autoriser le trafic UDP CoAP (port 5683) entre la Gateway et les devices
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=16,udp,tp_dst=5683,actions=output:10,13
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=10,udp,tp_dst=5683,actions=output:16
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=13,udp,tp_dst=5683,actions=output:16

# Autoriser les sessions SSH (port 22) de la Gateway vers les devices
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=16,tcp,tp_dst=22,actions=output:10,13
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=10,tcp,tp_src=22,actions=output:16
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=13,tcp,tp_src=22,actions=output:16
</code></pre>

<p>Cette progression illustre la puissance d'OpenFlow : depuis le simple routage par port jusqu'au controle fin des flux applicatifs, le reseau devient entierement programmable.</p>

<h3 class="section-title">5. Attachement du controleur et controle SDN</h3>

<p>L'attachement d'un controleur OpenFlow (ici Ryu) permet de passer d'un reseau statiquement configure a un reseau dynamiquement controle.</p>

<p><strong>Mode out-of-band</strong> :</p>

<p>Le trafic OpenFlow entre le controleur et les commutateurs est transporte par un reseau different de celui utilise pour les donnees utilisateur. Cela garantit que le canal de controle reste disponible meme en cas de congestion du reseau de donnees.</p>

<pre><code class="language-bash"># Configuration de l'interface du controleur sur le reseau de gestion
ifconfig eth1 192.168.0.42

# Declaration du controleur pour le pont br0
admin@picOS-OVS$ ovs-vsctl set-controller br0 tcp:192.168.0.42:6633

# Demarrage du controleur Ryu en mode verbose
controleur# ryu-manager --verbose

# Verification de la connexion
admin@picOS-OVS$ ovs-vsctl show
admin@picOS-OVS$ ovs-ofctl snoop br0
admin@picOS-OVS$ ovs-ofctl dump-flows br0
</code></pre>

<p><strong>Fonctionnement du controleur</strong> :</p>

<p>Sans application lancee, le controleur recoit les evenements Packet-In mais ne propose aucun traitement. Les paquets sont donc perdus car aucune regle n'est installee dans les tables de flux.</p>

<h3 class="section-title">6. Programmation reseau reactive et proactive</h3>

<p>Deux approches fondamentales pour la programmation de controleurs SDN :</p>

<p><strong>Mode reactif</strong> :</p>

<p>Le controleur reagit aux evenements reseau en temps reel. Lorsqu'un paquet arrive sans correspondance dans la table de flux, un Packet-In est envoye au controleur qui decide alors de l'action a entreprendre et installe eventuellement une regle pour les paquets similaires futurs.</p>

<p>L'application <strong>simple_switch_14</strong> illustre ce mode :</p>

<pre><code class="language-bash"># Lancement de l'application simple_switch
controleur# ryu-manager --verbose simple_switch_14.py

# Verification des regles installees apres un ping
admin@picOS-OVS$ ovs-ofctl dump-flows br0
</code></pre>

<p>Le comportement de simple_switch_14 :</p>
<ol>
<li>Reception d'un Packet-In pour un paquet dont le destinataire est inconnu</li>
<li>L'application demande au commutateur de diffuser le paquet sur tous les ports (flood)</li>
<li>Lorsque le destinataire repond, l'application apprend sa localisation (adresse MAC associee a un port)</li>
<li>Une regle est ajoutee dans la table de flux pour diriger les futurs paquets directement</li>
</ol>

<p><strong>Mode proactif</strong> :</p>

<p>Le controleur pre-configure les regles de flux avant l'arrivee du trafic, en anticipant les schemas de trafic attendus. Ce mode offre de meilleures performances (pas de latence Packet-In) mais necessite une connaissance prealable de la topologie et des flux.</p>

<pre><code class="language-bash"># Exemple de regle proactive pour un flux specifique
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=16,ip,nw_dst=128.0.0.4,actions=output:13
</code></pre>

<table>
<tr><th>Critere</th><th>Mode reactif</th><th>Mode proactif</th></tr>
<tr><td><strong>Latence</strong></td><td>Premier paquet retarde (Packet-In)</td><td>Aucune latence supplementaire</td></tr>
<tr><td><strong>Flexibilite</strong></td><td>Tres flexible, s'adapte dynamiquement</td><td>Necessite connaissance prealable</td></tr>
<tr><td><strong>Charge controleur</strong></td><td>Elevee (traite chaque nouveau flux)</td><td>Faible (configuration initiale)</td></tr>
<tr><td><strong>Tolerance aux pannes</strong></td><td>Dependant du controleur</td><td>Flux continues meme si controleur down</td></tr>
<tr><td><strong>Cas d'usage</strong></td><td>Reseaux dynamiques, apprentissage</td><td>Trafic previsible, performance critique</td></tr>
</table>

<h3 class="section-title">7. Topologie maillee et prevention des boucles</h3>

<p>L'exercice final du TP consistait a deployer une topologie partiellement maillee avec 4 commutateurs Pica8 interconnectes. Chaque commutateur hebergeait une instance de pont OVS, connectee a une machine terminale et a deux autres ponts sur d'autres commutateurs.</p>

<p><strong>Problematique des boucles</strong> :</p>

<p>Lorsque tous les liens sont actifs dans une topologie maillee, des boucles de couche 2 se forment. L'application simple_switch, qui utilise le flooding pour les adresses inconnues, provoque une amplification infinie des trames broadcast (tempete de broadcast). Cela rend le reseau inutilisable.</p>

<p><strong>Solutions</strong> :</p>

<p>La solution consiste a utiliser une application de controle integrant la gestion des boucles, similaire au Spanning Tree Protocol (STP) mais implementee au niveau du controleur SDN. Dans le repertoire de Ryu, des applications plus avancees comme <strong>simple_switch_stp</strong> integrent la detection et la prevention des boucles en bloquant les ports redondants.</p>

<p>Cette situation illustre un avantage majeur du SDN : au lieu de s'appuyer sur des protocoles distribues comme STP (convergence lente, configuration complexe), le controleur centralise peut calculer un arbre couvrant optimal grace a sa vision globale de la topologie.</p>

<h3 class="section-title">8. Controleurs SDN - Ecosysteme</h3>

<p>Plusieurs controleurs SDN sont disponibles, chacun avec ses specificites :</p>

<table>
<tr><th>Controleur</th><th>Langage</th><th>Licence</th><th>Caracteristiques</th></tr>
<tr><td><strong>Ryu</strong></td><td>Python</td><td>Apache 2.0</td><td>Leger, pedagogique, extensible, facile a programmer</td></tr>
<tr><td><strong>OpenDaylight (ODL)</strong></td><td>Java</td><td>Eclipse Public</td><td>Tres complet, modulaire, support industriel (Linux Foundation)</td></tr>
<tr><td><strong>ONOS</strong></td><td>Java</td><td>Apache 2.0</td><td>Haute disponibilite, oriente operateurs telecom</td></tr>
<tr><td><strong>Floodlight</strong></td><td>Java</td><td>Apache 2.0</td><td>Developpe par Big Switch Networks, performant</td></tr>
<tr><td><strong>POX</strong></td><td>Python</td><td>Apache 2.0</td><td>Predecessor de Ryu, utilise en recherche</td></tr>
</table>

<p><strong>Ryu en detail</strong> :</p>

<p>Ryu est un framework de controleur SDN base sur composants, ecrit en Python. Il fournit des APIs bien definies pour creer des applications de gestion reseau. Il supporte differentes versions d'OpenFlow (1.0 a 1.5) et offre une bibliotheque riche pour le parsing de paquets, la manipulation de flux, et l'interaction avec les commutateurs.</p>

<h3 class="section-title">9. Network Functions Virtualization (NFV)</h3>

<p>La NFV est une approche architecturale qui consiste a virtualiser les fonctions reseau traditionnellement realisees par des equipements materiels dedies (appliances proprietaires). Au lieu de deployer un pare-feu physique, un load balancer materiel ou un systeme IDS dedie, ces fonctions sont implementees en logiciel et executees sur des serveurs standards (COTS - Commercial Off-The-Shelf).</p>

<p><strong>Problematique des reseaux traditionnels</strong> :</p>
<ul>
<li>Chaque fonction reseau necessite un equipement dedie et couteux</li>
<li>Scalabilite limitee (achat de nouveau materiel pour augmenter la capacite)</li>
<li>Cycle de deploiement long (commande, installation, configuration)</li>
<li>Innovation freinee par les cycles produit des equipementiers</li>
<li>Dependance aux solutions proprietaires (vendor lock-in)</li>
</ul>

<p><strong>Fonctions Reseau Virtualisees (VNF)</strong> :</p>

<p>Les VNFs sont les implementations logicielles des fonctions reseau :</p>

<table>
<tr><th>Fonction traditionnelle</th><th>VNF equivalente</th></tr>
<tr><td>Pare-feu materiel</td><td>vFirewall</td></tr>
<tr><td>Load Balancer physique</td><td>vLoad Balancer</td></tr>
<tr><td>Routeur physique</td><td>vRouter</td></tr>
<tr><td>IDS/IPS materiel</td><td>vIDS/vIPS</td></tr>
<tr><td>WAN Optimizer</td><td>vWAN Optimizer</td></tr>
<tr><td>DPI appliance</td><td>vDPI</td></tr>
</table>

<p><strong>Cycle de vie des VNFs</strong> :</p>

<ol>
<li><strong>Instantiation</strong> : deploiement de la VNF sur l'infrastructure virtuelle</li>
<li><strong>Configuration</strong> : parametrage initial de la fonction</li>
<li><strong>Scaling</strong> : mise a l'echelle (scale-up/scale-down, scale-in/scale-out)</li>
<li><strong>Monitoring</strong> : supervision des performances et de la sante</li>
<li><strong>Update/Upgrade</strong> : mise a jour du logiciel sans interruption</li>
<li><strong>Termination</strong> : arret et liberation des ressources</li>
</ol>

<p><strong>Avantages de la NFV</strong> :</p>
<ul>
<li><strong>Reduction des couts</strong> : utilisation de serveurs standards (COTS)</li>
<li><strong>Agilite</strong> : deploiement et mise a l'echelle en minutes au lieu de semaines</li>
<li><strong>Flexibilite</strong> : fonctions deployees la ou necessaire, quand necessaire</li>
<li><strong>Innovation</strong> : cycle de developpement logiciel rapide</li>
<li><strong>Multi-vendor</strong> : independance vis-a-vis des equipementiers</li>
</ul>

<h3 class="section-title">10. Architecture MANO (Management and Orchestration)</h3>

<p>L'architecture MANO, definie par l'ETSI (European Telecommunications Standards Institute), est le cadre de reference pour la gestion et l'orchestration des environnements NFV.</p>

<p><strong>Composants principaux de l'architecture MANO</strong> :</p>

<table>
<tr><th>Composant</th><th>Role</th></tr>
<tr><td><strong>NFV Orchestrator (NFVO)</strong></td><td>Orchestration globale des services reseau, gestion du cycle de vie des Network Services</td></tr>
<tr><td><strong>VNF Manager (VNFM)</strong></td><td>Gestion du cycle de vie des VNFs individuelles (instantiation, scaling, termination)</td></tr>
<tr><td><strong>Virtualized Infrastructure Manager (VIM)</strong></td><td>Gestion de l'infrastructure virtuelle (compute, storage, network) - ex: OpenStack</td></tr>
<tr><td><strong>NFV Infrastructure (NFVI)</strong></td><td>Ressources physiques et virtuelles (serveurs, stockage, reseau)</td></tr>
<tr><td><strong>Element Management System (EMS)</strong></td><td>Gestion fonctionnelle des VNFs (configuration specifique a la fonction)</td></tr>
<tr><td><strong>OSS/BSS</strong></td><td>Systemes de support operationnel et commercial</td></tr>
</table>

<p><strong>Service Chaining (chaine de services)</strong> :</p>

<p>Le Service Chaining consiste a connecter sequentiellement plusieurs VNFs pour creer un service reseau complet. Par exemple, le trafic d'un utilisateur peut traverser successivement :</p>
<ol>
<li>vFirewall (filtrage)</li>
<li>vDPI (inspection approfondie)</li>
<li>vLoad Balancer (repartition de charge)</li>
<li>Application serveur</li>
</ol>

<p>Le SDN facilite grandement le Service Chaining en permettant de programmer dynamiquement le chemin des flux a travers les differentes VNFs.</p>

<h3 class="section-title">11. Protocole LISP (Locator/ID Separation Protocol)</h3>

<p>LISP est un protocole reseau qui separe l'identifiant d'un hote de sa localisation dans le reseau. Dans l'architecture IP traditionnelle, l'adresse IP joue un double role : elle identifie l'hote ET indique sa localisation topologique. Cette ambiguite pose des problemes pour la mobilite, le multi-homing et la scalabilite des tables de routage.</p>

<p><strong>Concepts fondamentaux</strong> :</p>

<table>
<tr><th>Concept</th><th>Description</th></tr>
<tr><td><strong>EID (Endpoint Identifier)</strong></td><td>Identifiant de l'hote (adresse IP de l'hote, stable)</td></tr>
<tr><td><strong>RLOC (Routing Locator)</strong></td><td>Localisateur dans le reseau (adresse IP du routeur de bordure)</td></tr>
<tr><td><strong>ITR (Ingress Tunnel Router)</strong></td><td>Routeur d'entree qui encapsule les paquets</td></tr>
<tr><td><strong>ETR (Egress Tunnel Router)</strong></td><td>Routeur de sortie qui desencapsule les paquets</td></tr>
<tr><td><strong>Map-Server</strong></td><td>Serveur de correspondance EID &rarr; RLOC</td></tr>
<tr><td><strong>Map-Resolver</strong></td><td>Serveur qui resout les requetes de mapping</td></tr>
</table>

<p><strong>Fonctionnement</strong> :</p>

<ol>
<li>Un hote source envoie un paquet vers un EID destination</li>
<li>L'ITR interroge le systeme de mapping pour obtenir le RLOC associe a l'EID destination</li>
<li>L'ITR encapsule le paquet original dans un nouveau paquet IP avec le RLOC comme destination</li>
<li>Le paquet traverse le reseau de coeur en utilisant les RLOC</li>
<li>L'ETR desencapsule le paquet et le delivre a l'hote destination</li>
</ol>

<p><strong>Avantages de LISP</strong> :</p>
<ul>
<li><strong>Reduction des tables de routage</strong> : seuls les RLOC sont annonces dans le coeur du reseau</li>
<li><strong>Mobilite</strong> : un hote peut changer de localisation (RLOC) sans changer son identite (EID)</li>
<li><strong>Multi-homing</strong> : un EID peut etre associe a plusieurs RLOC pour la redondance</li>
<li><strong>Ingenierie de trafic</strong> : selection du meilleur RLOC selon les metriques</li>
</ul>

<h3 class="section-title">12. Programmabilite reseau et API</h3>

<p>La programmabilite est au coeur de la transformation des reseaux modernes. Le SDN et la NFV convergent pour creer des reseaux entierement automatisables et programmables.</p>

<p><strong>Niveaux de programmabilite</strong> :</p>

<ul>
<li><strong>Configuration automatisee</strong> : scripts et outils (Ansible, Puppet, Chef) pour deployer des configurations</li>
<li><strong>Controleurs SDN</strong> : programmation du comportement reseau via applications Python/Java</li>
<li><strong>APIs REST</strong> : interfaces standardisees pour interagir avec les controleurs et les VNFs</li>
<li><strong>Intent-Based Networking</strong> : expression de l'intention (politique de haut niveau) traduite automatiquement en configuration</li>
</ul>

<p><strong>Convergence SDN + NFV</strong> :</p>

<p>SDN et NFV sont complementaires :</p>
<ul>
<li>Le SDN fournit la <strong>programmabilite du reseau</strong> (plan de donnees)</li>
<li>La NFV fournit la <strong>virtualisation des fonctions</strong> (plan de services)</li>
<li>Ensemble, ils permettent de creer des infrastructures reseau entierement logicielles, agiles et automatisees</li>
</ul>

<p>Cette convergence est au coeur des architectures reseau 5G, ou le network slicing repose sur la capacite a creer des tranches de reseau virtuelles avec des VNFs specifiques, interconnectees par un plan de donnees SDN.</p>

<hr>

<h2>PART D - Analyse et Reflexion</h2>

<h3 class="section-title">Competences acquises</h3>

<p><strong>Comprehension du paradigme SDN</strong> :<br>
Maitrise de la separation plan de controle / plan de donnees, du protocole OpenFlow et de l'architecture a trois couches. Capacite a expliquer les avantages et les limites du SDN par rapport aux reseaux traditionnels.</p>

<p><strong>Configuration Open vSwitch</strong> :<br>
Competence pratique dans la creation de ponts logiques, l'attachement de ports physiques et la gestion d'instances OVS sur des equipements Pica8 reels.</p>

<p><strong>Programmation de regles OpenFlow</strong> :<br>
Capacite a installer des regles de flux a differents niveaux de granularite : port d'entree, adresses IP, protocoles de transport, ports applicatifs. Comprehension de l'impact de la granularite sur la precision du controle et les performances.</p>

<p><strong>Deploiement de controleurs SDN</strong> :<br>
Experience avec le controleur Ryu, depuis le lancement en mode verbose jusqu'a l'execution d'applications de controle (simple_switch_14). Comprehension du fonctionnement reactif et proactif.</p>

<p><strong>Gestion de topologies complexes</strong> :<br>
Experience du deploiement de topologies maillees multi-commutateurs et comprehension des problemes de boucles et de leurs solutions dans un contexte SDN.</p>

<p><strong>Comprehension NFV et MANO</strong> :<br>
Connaissance de l'architecture de virtualisation des fonctions reseau, du cycle de vie des VNFs et du cadre MANO pour l'orchestration.</p>

<h3 class="section-title">Auto-evaluation</h3>

<p>J'ai trouve le cours "Emerging Network Technologies" tres engageant et formateur, bien que certains aspects aient ete un peu complexes pour moi en tant qu'etudiant specialise en Electronique Automatique par rapport a ceux de l'option Reseau. Malgre cela, j'ai ete activement implique dans la simulation de topologies et le test de divers aspects, ce qui m'a fourni une comprehension pratique de la facon dont ces technologies transforment la gestion des reseaux.</p>

<p>Le travail sur les equipements Pica8 reels a ete la partie la plus enrichissante. Manipuler des commutateurs physiques, installer des regles OpenFlow et observer leur effet immediat sur la connectivite donne une dimension concrete que les simulations ne peuvent pas offrir.</p>

<p>Le principal defi a ete la comprehension de la topologie maillee et la gestion des boucles. Voir le reseau devenir instable avec l'ajout d'un seul lien physique m'a fait comprendre l'importance critique de la prevention des boucles et la puissance du controleur SDN pour resoudre ce probleme de maniere centralisee.</p>

<p>Comme je suis egalement le <a href="./master-reoc.html">Master REOC</a>, j'avais deja travaille sur SDN et Ryu dans un contexte plus exploratoire. Ce cours a solidifie mes competences avec une approche plus structuree et progressive. En REOC, nous avions mene notre propre recherche et projet, ce qui offrait une experience plus pratique mais moins guidee.</p>

<h3 class="section-title">Perspectives professionnelles</h3>

<p>Les technologies emergentes vues dans ce cours sont au coeur de la transformation des infrastructures reseau :</p>

<ul>
<li><strong>Operateurs telecom</strong> : deploiement 5G avec network slicing (SDN + NFV)</li>
<li><strong>Cloud providers</strong> : reseaux virtuels (VPC) et SDN pour multi-tenancy</li>
<li><strong>Entreprises</strong> : SD-WAN pour connecter les sites distants avec agilite</li>
<li><strong>Data centers</strong> : automatisation des reseaux de datacenter avec SDN</li>
<li><strong>IoT</strong> : gestion intelligente des flux IoT via controleurs SDN</li>
</ul>

<hr>

<h2>Documents de Cours</h2>

</div>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">Chapitre 1 - Introduction aux reseaux emergents</span>
        <span class="lang-en">Chapter 1 - Introduction to emerging networks</span>
      </h4>
      <p>
        <span class="lang-fr">Cours introductif : problematiques des reseaux traditionnels, evolution vers SDN et NFV, enjeux de la programmabilite reseau.</span>
        <span class="lang-en">Introductory lecture: traditional network issues, evolution toward SDN and NFV, network programmability challenges.</span>
      </p>
      <embed src="/cours-pdf/S9/Reseau-Emergent/2023.ch1.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/Reseau-Emergent/2023.ch1.pdf" target="_blank">
        <span class="lang-fr">Telecharger le chapitre 1</span>
        <span class="lang-en">Download chapter 1</span>
      </a></p>
    </div>
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">Chapitre 2 - Software-Defined Networking (SDN)</span>
        <span class="lang-en">Chapter 2 - Software-Defined Networking (SDN)</span>
      </h4>
      <p>
        <span class="lang-fr">Cours approfondi sur le SDN : architecture, protocole OpenFlow, controleurs, programmation reactive et proactive.</span>
        <span class="lang-en">In-depth lecture on SDN: architecture, OpenFlow protocol, controllers, reactive and proactive programming.</span>
      </p>
      <embed src="/cours-pdf/S9/Reseau-Emergent/2023Ch2SDNenglish.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/Reseau-Emergent/2023Ch2SDNenglish.pdf" target="_blank">
        <span class="lang-fr">Telecharger le chapitre 2 - SDN</span>
        <span class="lang-en">Download chapter 2 - SDN</span>
      </a></p>
    </div>
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">Chapitre 3 - Introduction a LISP</span>
        <span class="lang-en">Chapter 3 - Introduction to LISP</span>
      </h4>
      <p>
        <span class="lang-fr">Cours sur le protocole LISP : separation identifiant/localisateur, architecture ITR/ETR, systeme de mapping EID-RLOC.</span>
        <span class="lang-en">Lecture on the LISP protocol: identifier/locator separation, ITR/ETR architecture, EID-RLOC mapping system.</span>
      </p>
      <embed src="/cours-pdf/S9/Reseau-Emergent/Ch3-Intro-LISP.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/Reseau-Emergent/Ch3-Intro-LISP.pdf" target="_blank">
        <span class="lang-fr">Telecharger le chapitre 3 - LISP</span>
        <span class="lang-en">Download chapter 3 - LISP</span>
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
        <span class="lang-fr">Rapport SDN &amp; NFV</span>
        <span class="lang-en">SDN &amp; NFV Report</span>
    </h3>
</div>

<div class="pdf-container">
  <div class="pdf-item" style="min-width: 100%;">
    <h4>
      <span class="lang-fr">Rapport de projet - SDN et NFV</span>
      <span class="lang-en">Project report - SDN and NFV</span>
    </h4>
    <p>
      <span class="lang-fr">Rapport technique detaillant les travaux pratiques sur le Software-Defined Networking et la Network Functions Virtualization.</span>
      <span class="lang-en">Technical report detailing the lab work on Software-Defined Networking and Network Functions Virtualization.</span>
    </p>
    <embed src="/file/reports/S9/Chanfreau_SDN_NFV_Report.pdf" type="application/pdf" width="100%" height="800px" />
    <p><a href="/file/reports/S9/Chanfreau_SDN_NFV_Report.pdf" target="_blank">
      <span class="lang-fr">Ouvrir le rapport complet</span>
      <span class="lang-en">Open the full report</span>
    </a></p>
  </div>
</div>

<div class="pdf-container">
  <div class="pdf-item" style="min-width: 100%;">
    <h4>
      <span class="lang-fr">Sujet de TP - Emerging Network</span>
      <span class="lang-en">Lab Subject - Emerging Network</span>
    </h4>
    <p>
      <span class="lang-fr">Sujet du TP couvrant la configuration OVS, les regles OpenFlow, l'attachement du controleur Ryu et le deploiement de topologies maillees.</span>
      <span class="lang-en">Lab subject covering OVS configuration, OpenFlow rules, Ryu controller attachment and mesh topology deployment.</span>
    </p>
    <embed src="/img/BE_Emerging_Network/Lab_Subject_emerging.pdf" type="application/pdf" width="100%" height="800px" />
    <p><a href="/img/BE_Emerging_Network/Lab_Subject_emerging.pdf" target="_blank">
      <span class="lang-fr">Ouvrir le sujet de TP</span>
      <span class="lang-en">Open the lab subject</span>
    </a></p>
  </div>
</div>

<div class="lang-fr">
<hr>
<p><em>Cours suivi en 2024-2025 a l'INSA Toulouse, Departement Genie Electrique et Informatique.</em></p>
</div>

<div class="lang-en">

<p><strong>Related courses</strong>:</p>
<ul>
<li><a href="./cloud-edge.html">Cloud &amp; Edge Computing - S9</a> - SDN for Cloud/Edge</li>
<li><a href="../2023-2024/2024-10-03-interconnexion-reseau.html">Network Interconnection - S8</a> - Network fundamentals</li>
</ul>

<hr>

<h1>Emerging Network Technologies - Semester 9</h1>

<p><strong>Academic year</strong>: 2024-2025<br>
<strong>Category</strong>: Emerging networks and network programmability<br>
<strong>Instructor</strong>: S. Abdellatif</p>

<hr>

<h2>PART A - General Presentation</h2>

<h3 class="section-title">Overview</h3>

<p>The "Emerging Network Technologies" course, taught by S. Abdellatif at INSA Toulouse, explores major advances in network technologies. It focuses on three fundamental pillars of modern networks: <strong>Software-Defined Networking (SDN)</strong>, <strong>Network Functions Virtualization (NFV)</strong> and the <strong>LISP (Locator/ID Separation Protocol)</strong>. These technologies form the foundation for transforming traditional network infrastructures into programmable, flexible and virtualized architectures.</p>

<p>This course is particularly relevant in the current context where traditional networks, based on proprietary equipment with integrated control and data planes, show their limitations when facing scalability, agility and automation requirements of cloud, IoT and 5G environments.</p>

<p><strong>Learning objectives</strong>:</p>
<ul>
<li>Understand the separation of the control plane and the data plane (SDN paradigm)</li>
<li>Master the OpenFlow protocol and its role in SDN architecture</li>
<li>Configure and administer Open vSwitch (OVS) for virtual switching</li>
<li>Deploy and program SDN controllers (Ryu, OpenDaylight, ONOS)</li>
<li>Understand the principles of NFV and the MANO architecture</li>
<li>Comprehend the LISP protocol and the identifier/locator separation</li>
<li>Develop network control applications in reactive and proactive modes</li>
<li>Design SDN topologies and manage network loop problems</li>
</ul>

<h3 class="section-title">Position in the curriculum</h3>

<p>This module builds on previously acquired foundations:</p>
<ul>
<li><strong>Networking (S5)</strong>: OSI model, Ethernet, IP, TCP/UDP</li>
<li><strong>Network Interconnection (S8)</strong>: routing (OSPF, BGP), VLANs, switching, QoS</li>
<li><strong>Hardware Architecture (S6)</strong>: physical layer, signals</li>
</ul>

<p>It prepares for:</p>
<ul>
<li><strong>Cloud and Edge Computing (S9)</strong>: virtualization, orchestration, Kubernetes</li>
<li><strong>IoT (S9)</strong>: specific protocols, embedded network constraints</li>
<li><strong>Professional career</strong>: network engineer, SDN/NFV architect, network DevOps</li>
</ul>

<h3 class="section-title">Module organization</h3>

<table>
<tr><th>Element</th><th>Volume</th><th>Description</th></tr>
<tr><td>Lectures</td><td>~10h</td><td>SDN, NFV, LISP theory, architectures</td></tr>
<tr><td>Lab sessions</td><td>~12h</td><td>OVS configuration, OpenFlow, Ryu controllers</td></tr>
<tr><td>Project/Report</td><td>-</td><td>SDN &amp; NFV report</td></tr>
</table>

<hr>

<h2>PART B - Experience and Context</h2>

<h3 class="section-title">Environment and context</h3>

<p>During this course, I worked in a laboratory environment equipped with professional hardware for SDN/OpenFlow experimentation. The infrastructure included:</p>

<ul>
<li><strong>4 Pica8 switches</strong> compatible with OpenFlow, equipped with 48 Gigabit Ethernet ports each</li>
<li><strong>12 PCs</strong> equipped with multiple Ethernet cards, serving as routers and/or Linux machines</li>
<li><strong>Ethernet cables</strong> (unshielded twisted pairs with RJ45 connectors), crossover and straight-through</li>
<li><strong>Management network</strong> separate from the data network (out-of-band mode)</li>
</ul>

<p>This context allowed complete immersion in real SDN architectures, far from simplified simulations. Handling physical Pica8 equipment with Open vSwitch gave a concrete dimension to theoretical concepts. The progressive deployment, from a simple OVS bridge to a multi-switch mesh topology with a centralized controller, made it possible to understand each building block of the SDN architecture.</p>

<h3 class="section-title">Tools used</h3>

<table>
<tr><th>Tool</th><th>Role</th><th>Usage</th></tr>
<tr><td><strong>Open vSwitch (OVS)</strong></td><td>Virtual switch</td><td>Creation of logical bridges, flow management</td></tr>
<tr><td><strong>Ryu</strong></td><td>SDN controller</td><td>Programming network control applications</td></tr>
<tr><td><strong>ovs-vsctl</strong></td><td>OVS administration CLI</td><td>Bridge and port configuration</td></tr>
<tr><td><strong>ovs-ofctl</strong></td><td>OpenFlow CLI for OVS</td><td>Installation/deletion of flow rules</td></tr>
<tr><td><strong>Pica8 picOS</strong></td><td>Switch operating system</td><td>OVS/OpenFlow mode</td></tr>
<tr><td><strong>Wireshark</strong></td><td>Packet analyzer</td><td>Observation of OpenFlow exchanges</td></tr>
<tr><td><strong>Python</strong></td><td>Programming</td><td>Development of Ryu controller applications</td></tr>
</table>

<h3 class="section-title">My role</h3>

<p>In this course, I was responsible for:</p>
<ul>
<li>Understanding the principles of SDN, NFV and the OpenFlow protocol</li>
<li>Configuring OVS instances on the Pica8 switches</li>
<li>Manually installing OpenFlow rules to control network behavior</li>
<li>Attaching and configuring a Ryu controller for centralized management</li>
<li>Deploying complex network topologies (mesh) and managing loop problems</li>
<li>Analyzing the reactive and proactive behavior of the controller</li>
<li>Writing a technical report on SDN and NFV</li>
</ul>

<hr>

<h2>PART C - Detailed Technical Aspects</h2>

<h3 class="section-title">1. Software-Defined Networking (SDN) - Fundamental principles</h3>

<p>SDN represents a fundamental paradigm shift in network architecture. In traditional networks, each device (router, switch) integrates both the <strong>control plane</strong> (routing decisions, protocols) and the <strong>data plane</strong> (actual packet forwarding). This distributed architecture has several limitations: management complexity, lack of global vision, difficulty of evolution, and dependency on proprietary equipment.</p>

<p><strong>Three-layer SDN architecture</strong>:</p>

<p>SDN is based on an architecture with three distinct layers:</p>

<table>
<tr><th>Layer</th><th>Name</th><th>Role</th><th>Examples</th></tr>
<tr><td><strong>Application Layer</strong></td><td>Application Plane</td><td>Network control applications</td><td>Firewall, Load Balancer, QoS Manager</td></tr>
<tr><td><strong>Control Layer</strong></td><td>Control Plane</td><td>Routing decisions, global vision</td><td>Ryu, OpenDaylight, ONOS, Floodlight</td></tr>
<tr><td><strong>Infrastructure Layer</strong></td><td>Data Plane</td><td>Packet forwarding according to rules</td><td>Open vSwitch, OpenFlow switches</td></tr>
</table>

<p><strong>Communication interfaces</strong>:</p>

<ul>
<li><strong>Southbound API (e.g., OpenFlow)</strong>: interface between the controller and network devices. Allows the controller to program the flow tables of switches.</li>
<li><strong>Northbound API (e.g., REST API)</strong>: interface between the controller and applications. Allows applications to request network services from the controller.</li>
<li><strong>Eastbound/Westbound</strong>: communication between distributed controllers for scalability.</li>
</ul>

<p><strong>SDN advantages</strong>:</p>
<ul>
<li><strong>Programmability</strong>: the network can be programmed and automated via APIs</li>
<li><strong>Global vision</strong>: the centralized controller has a complete view of the topology</li>
<li><strong>Agility</strong>: rapid modification of network behavior without reconfiguring each device</li>
<li><strong>Hardware independence</strong>: separation between control software and hardware</li>
<li><strong>Accelerated innovation</strong>: ability to deploy new network services in software</li>
</ul>

<h3 class="section-title">2. OpenFlow protocol</h3>

<p>OpenFlow is the standard protocol for the SDN <strong>Southbound API</strong>. It defines the communication between the SDN controller and OpenFlow switches, allowing the controller to directly program the flow tables of network devices.</p>

<p><strong>Operating principles</strong>:</p>

<p>An OpenFlow switch has one or more <strong>flow tables</strong>. Each entry in a flow table contains:</p>

<table>
<tr><th>Field</th><th>Description</th></tr>
<tr><td><strong>Match fields</strong></td><td>Matching criteria (input port, MAC/IP addresses, TCP/UDP ports, VLAN, etc.)</td></tr>
<tr><td><strong>Priority</strong></td><td>Rule priority (higher priority rules evaluated first)</td></tr>
<tr><td><strong>Counters</strong></td><td>Matching packet and byte counters</td></tr>
<tr><td><strong>Instructions/Actions</strong></td><td>Actions to perform (forward, drop, modify header, send to controller)</td></tr>
<tr><td><strong>Timeouts</strong></td><td>Rule validity duration (idle timeout, hard timeout)</td></tr>
<tr><td><strong>Cookie</strong></td><td>Opaque identifier defined by the controller</td></tr>
</table>

<p><strong>Packet processing workflow</strong>:</p>

<ol>
<li>A packet arrives on a switch port</li>
<li>The switch compares packet fields against flow table entries</li>
<li>If a match is found: execute the associated actions</li>
<li>If no match: send a <strong>Packet-In</strong> message to the controller</li>
<li>The controller analyzes the packet and responds with a <strong>Packet-Out</strong> or installs a new rule via <strong>Flow-Mod</strong></li>
</ol>

<p><strong>Main OpenFlow messages</strong>:</p>

<table>
<tr><th>Message</th><th>Direction</th><th>Description</th></tr>
<tr><td><strong>Packet-In</strong></td><td>Switch &rarr; Controller</td><td>Notification of a packet with no match</td></tr>
<tr><td><strong>Packet-Out</strong></td><td>Controller &rarr; Switch</td><td>Processing instruction for a packet</td></tr>
<tr><td><strong>Flow-Mod</strong></td><td>Controller &rarr; Switch</td><td>Addition/modification/deletion of a flow rule</td></tr>
<tr><td><strong>Hello</strong></td><td>Bidirectional</td><td>OpenFlow connection establishment</td></tr>
<tr><td><strong>Features-Request/Reply</strong></td><td>Bidirectional</td><td>Discovery of switch capabilities</td></tr>
<tr><td><strong>Stats-Request/Reply</strong></td><td>Bidirectional</td><td>Statistics consultation</td></tr>
</table>

<p><strong>OpenFlow versions</strong>: 1.0 (basic, single table), 1.3 (multiple tables, groups, meters), 1.4, 1.5 (latest evolutions).</p>

<h3 class="section-title">3. Open vSwitch (OVS) - Virtual switching</h3>

<p>Open vSwitch is a multilayer virtual switch designed to enable network automation through programmable extensions. It supports standard management protocols (OpenFlow, sFlow, SPAN, LACP, 802.1Q) and is widely deployed in virtualization and cloud computing environments.</p>

<p><strong>OVS architecture</strong>:</p>
<ul>
<li><strong>ovsdb-server</strong>: configuration database server</li>
<li><strong>ovs-vswitchd</strong>: main switch daemon, manages flow tables</li>
<li><strong>ovs-vsctl</strong>: CLI tool for configuration (bridges, ports, controllers)</li>
<li><strong>ovs-ofctl</strong>: CLI tool for OpenFlow flow management</li>
</ul>

<p><strong>Initial OVS bridge configuration</strong>:</p>

<p>Creation of a logical bridge instance and attachment of physical ports:</p>

<pre><code class="language-bash"># Redemarrage des processus OVS
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
</code></pre>

<p><strong>Default behavior</strong>:</p>

<p>Without explicit rules, the OVS bridge does not know how to forward packets. A default rule can be added that transforms the switch into a classic L2 switch:</p>

<pre><code class="language-bash">admin@picOS-OVS$ ovs-ofctl add-flow br0 ,action=normal
</code></pre>

<h3 class="section-title">4. Manual installation of OpenFlow rules</h3>

<p>Manual installation of OpenFlow rules allows a fine understanding of the data plane programming mechanism. Several levels of granularity are possible.</p>

<p><strong>Level 1 - Rules based on input port</strong>:</p>

<p>Simple rules redirecting traffic from one port to other ports, without content distinction:</p>

<pre><code class="language-bash"># Suppression de toutes les regles existantes
admin@picOS-OVS$ ovs-ofctl del-flows br0

# Regles de redirection basees sur les ports d'entree
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=10,actions=output:13,16
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=13,actions=output:10,16
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=16,actions=output:10,13
</code></pre>

<p><strong>Level 2 - Rules with IP filtering (fine granularity)</strong>:</p>

<p>For more precise control, filtering is done by destination IP address, with separate ARP handling:</p>

<pre><code class="language-bash">admin@picOS-OVS$ ovs-ofctl del-flows br0

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
</code></pre>

<p><strong>Level 3 - Application-level rules (protocol filtering)</strong>:</p>

<p>For application-level control, filtering is done on transport protocols and ports:</p>

<pre><code class="language-bash"># Autoriser le trafic UDP CoAP (port 5683) entre la Gateway et les devices
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=16,udp,tp_dst=5683,actions=output:10,13
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=10,udp,tp_dst=5683,actions=output:16
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=13,udp,tp_dst=5683,actions=output:16

# Autoriser les sessions SSH (port 22) de la Gateway vers les devices
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=16,tcp,tp_dst=22,actions=output:10,13
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=10,tcp,tp_src=22,actions=output:16
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=13,tcp,tp_src=22,actions=output:16
</code></pre>

<p>This progression illustrates the power of OpenFlow: from simple port-based routing to fine-grained application flow control, the network becomes fully programmable.</p>

<h3 class="section-title">5. Controller attachment and SDN control</h3>

<p>Attaching an OpenFlow controller (here Ryu) allows transitioning from a statically configured network to a dynamically controlled network.</p>

<p><strong>Out-of-band mode</strong>:</p>

<p>OpenFlow traffic between the controller and switches is transported by a different network from the one used for user data. This ensures that the control channel remains available even in case of data network congestion.</p>

<pre><code class="language-bash"># Configuration de l'interface du controleur sur le reseau de gestion
ifconfig eth1 192.168.0.42

# Declaration du controleur pour le pont br0
admin@picOS-OVS$ ovs-vsctl set-controller br0 tcp:192.168.0.42:6633

# Demarrage du controleur Ryu en mode verbose
controleur# ryu-manager --verbose

# Verification de la connexion
admin@picOS-OVS$ ovs-vsctl show
admin@picOS-OVS$ ovs-ofctl snoop br0
admin@picOS-OVS$ ovs-ofctl dump-flows br0
</code></pre>

<p><strong>Controller operation</strong>:</p>

<p>Without a running application, the controller receives Packet-In events but does not provide any processing. Packets are therefore lost because no rules are installed in the flow tables.</p>

<h3 class="section-title">6. Reactive and proactive network programming</h3>

<p>Two fundamental approaches for SDN controller programming:</p>

<p><strong>Reactive mode</strong>:</p>

<p>The controller reacts to network events in real time. When a packet arrives without a match in the flow table, a Packet-In is sent to the controller which then decides the action to take and possibly installs a rule for similar future packets.</p>

<p>The <strong>simple_switch_14</strong> application illustrates this mode:</p>

<pre><code class="language-bash"># Lancement de l'application simple_switch
controleur# ryu-manager --verbose simple_switch_14.py

# Verification des regles installees apres un ping
admin@picOS-OVS$ ovs-ofctl dump-flows br0
</code></pre>

<p>The behavior of simple_switch_14:</p>
<ol>
<li>Reception of a Packet-In for a packet whose destination is unknown</li>
<li>The application asks the switch to broadcast the packet on all ports (flood)</li>
<li>When the destination responds, the application learns its location (MAC address associated with a port)</li>
<li>A rule is added to the flow table to direct future packets directly</li>
</ol>

<p><strong>Proactive mode</strong>:</p>

<p>The controller pre-configures flow rules before traffic arrives, anticipating expected traffic patterns. This mode offers better performance (no Packet-In latency) but requires prior knowledge of the topology and flows.</p>

<pre><code class="language-bash"># Exemple de regle proactive pour un flux specifique
admin@picOS-OVS$ ovs-ofctl add-flow br0 in_port=16,ip,nw_dst=128.0.0.4,actions=output:13
</code></pre>

<table>
<tr><th>Criterion</th><th>Reactive mode</th><th>Proactive mode</th></tr>
<tr><td><strong>Latency</strong></td><td>First packet delayed (Packet-In)</td><td>No additional latency</td></tr>
<tr><td><strong>Flexibility</strong></td><td>Very flexible, adapts dynamically</td><td>Requires prior knowledge</td></tr>
<tr><td><strong>Controller load</strong></td><td>High (processes each new flow)</td><td>Low (initial configuration)</td></tr>
<tr><td><strong>Fault tolerance</strong></td><td>Dependent on controller</td><td>Flows continue even if controller is down</td></tr>
<tr><td><strong>Use cases</strong></td><td>Dynamic networks, learning</td><td>Predictable traffic, critical performance</td></tr>
</table>

<h3 class="section-title">7. Mesh topology and loop prevention</h3>

<p>The final lab exercise consisted of deploying a partially meshed topology with 4 interconnected Pica8 switches. Each switch hosted an OVS bridge instance, connected to a terminal machine and to two other bridges on other switches.</p>

<p><strong>Loop problem</strong>:</p>

<p>When all links are active in a mesh topology, Layer 2 loops form. The simple_switch application, which uses flooding for unknown addresses, causes infinite amplification of broadcast frames (broadcast storm). This renders the network unusable.</p>

<p><strong>Solutions</strong>:</p>

<p>The solution is to use a control application that integrates loop management, similar to the Spanning Tree Protocol (STP) but implemented at the SDN controller level. In the Ryu directory, more advanced applications such as <strong>simple_switch_stp</strong> integrate loop detection and prevention by blocking redundant ports.</p>

<p>This situation illustrates a major advantage of SDN: instead of relying on distributed protocols like STP (slow convergence, complex configuration), the centralized controller can compute an optimal spanning tree thanks to its global view of the topology.</p>

<h3 class="section-title">8. SDN controllers - Ecosystem</h3>

<p>Several SDN controllers are available, each with its own specificities:</p>

<table>
<tr><th>Controller</th><th>Language</th><th>License</th><th>Characteristics</th></tr>
<tr><td><strong>Ryu</strong></td><td>Python</td><td>Apache 2.0</td><td>Lightweight, educational, extensible, easy to program</td></tr>
<tr><td><strong>OpenDaylight (ODL)</strong></td><td>Java</td><td>Eclipse Public</td><td>Very comprehensive, modular, industrial support (Linux Foundation)</td></tr>
<tr><td><strong>ONOS</strong></td><td>Java</td><td>Apache 2.0</td><td>High availability, telecom operator-oriented</td></tr>
<tr><td><strong>Floodlight</strong></td><td>Java</td><td>Apache 2.0</td><td>Developed by Big Switch Networks, performant</td></tr>
<tr><td><strong>POX</strong></td><td>Python</td><td>Apache 2.0</td><td>Predecessor of Ryu, used in research</td></tr>
</table>

<p><strong>Ryu in detail</strong>:</p>

<p>Ryu is a component-based SDN controller framework, written in Python. It provides well-defined APIs for creating network management applications. It supports different OpenFlow versions (1.0 to 1.5) and offers a rich library for packet parsing, flow manipulation, and switch interaction.</p>

<h3 class="section-title">9. Network Functions Virtualization (NFV)</h3>

<p>NFV is an architectural approach that consists of virtualizing network functions traditionally performed by dedicated hardware appliances (proprietary appliances). Instead of deploying a physical firewall, a hardware load balancer or a dedicated IDS system, these functions are implemented in software and run on standard servers (COTS - Commercial Off-The-Shelf).</p>

<p><strong>Traditional network issues</strong>:</p>
<ul>
<li>Each network function requires a dedicated and expensive device</li>
<li>Limited scalability (purchasing new hardware to increase capacity)</li>
<li>Long deployment cycle (ordering, installation, configuration)</li>
<li>Innovation slowed by equipment vendor product cycles</li>
<li>Dependency on proprietary solutions (vendor lock-in)</li>
</ul>

<p><strong>Virtualized Network Functions (VNF)</strong>:</p>

<p>VNFs are software implementations of network functions:</p>

<table>
<tr><th>Traditional function</th><th>Equivalent VNF</th></tr>
<tr><td>Hardware firewall</td><td>vFirewall</td></tr>
<tr><td>Physical load balancer</td><td>vLoad Balancer</td></tr>
<tr><td>Physical router</td><td>vRouter</td></tr>
<tr><td>Hardware IDS/IPS</td><td>vIDS/vIPS</td></tr>
<tr><td>WAN Optimizer</td><td>vWAN Optimizer</td></tr>
<tr><td>DPI appliance</td><td>vDPI</td></tr>
</table>

<p><strong>VNF lifecycle</strong>:</p>

<ol>
<li><strong>Instantiation</strong>: deployment of the VNF on the virtual infrastructure</li>
<li><strong>Configuration</strong>: initial function parameterization</li>
<li><strong>Scaling</strong>: scaling (scale-up/scale-down, scale-in/scale-out)</li>
<li><strong>Monitoring</strong>: performance and health supervision</li>
<li><strong>Update/Upgrade</strong>: software update without interruption</li>
<li><strong>Termination</strong>: shutdown and resource release</li>
</ol>

<p><strong>NFV advantages</strong>:</p>
<ul>
<li><strong>Cost reduction</strong>: use of standard servers (COTS)</li>
<li><strong>Agility</strong>: deployment and scaling in minutes instead of weeks</li>
<li><strong>Flexibility</strong>: functions deployed where needed, when needed</li>
<li><strong>Innovation</strong>: rapid software development cycle</li>
<li><strong>Multi-vendor</strong>: independence from equipment vendors</li>
</ul>

<h3 class="section-title">10. MANO Architecture (Management and Orchestration)</h3>

<p>The MANO architecture, defined by ETSI (European Telecommunications Standards Institute), is the reference framework for the management and orchestration of NFV environments.</p>

<p><strong>Main MANO architecture components</strong>:</p>

<table>
<tr><th>Component</th><th>Role</th></tr>
<tr><td><strong>NFV Orchestrator (NFVO)</strong></td><td>Global orchestration of network services, Network Services lifecycle management</td></tr>
<tr><td><strong>VNF Manager (VNFM)</strong></td><td>Individual VNF lifecycle management (instantiation, scaling, termination)</td></tr>
<tr><td><strong>Virtualized Infrastructure Manager (VIM)</strong></td><td>Virtual infrastructure management (compute, storage, network) - e.g., OpenStack</td></tr>
<tr><td><strong>NFV Infrastructure (NFVI)</strong></td><td>Physical and virtual resources (servers, storage, network)</td></tr>
<tr><td><strong>Element Management System (EMS)</strong></td><td>Functional VNF management (function-specific configuration)</td></tr>
<tr><td><strong>OSS/BSS</strong></td><td>Operational and business support systems</td></tr>
</table>

<p><strong>Service Chaining</strong>:</p>

<p>Service Chaining consists of sequentially connecting multiple VNFs to create a complete network service. For example, a user's traffic may successively pass through:</p>
<ol>
<li>vFirewall (filtering)</li>
<li>vDPI (deep inspection)</li>
<li>vLoad Balancer (load distribution)</li>
<li>Application server</li>
</ol>

<p>SDN greatly facilitates Service Chaining by allowing dynamic programming of flow paths through the various VNFs.</p>

<h3 class="section-title">11. LISP Protocol (Locator/ID Separation Protocol)</h3>

<p>LISP is a network protocol that separates a host's identifier from its location in the network. In traditional IP architecture, the IP address plays a dual role: it identifies the host AND indicates its topological location. This ambiguity causes problems for mobility, multi-homing and routing table scalability.</p>

<p><strong>Fundamental concepts</strong>:</p>

<table>
<tr><th>Concept</th><th>Description</th></tr>
<tr><td><strong>EID (Endpoint Identifier)</strong></td><td>Host identifier (host IP address, stable)</td></tr>
<tr><td><strong>RLOC (Routing Locator)</strong></td><td>Network locator (border router IP address)</td></tr>
<tr><td><strong>ITR (Ingress Tunnel Router)</strong></td><td>Ingress router that encapsulates packets</td></tr>
<tr><td><strong>ETR (Egress Tunnel Router)</strong></td><td>Egress router that decapsulates packets</td></tr>
<tr><td><strong>Map-Server</strong></td><td>EID &rarr; RLOC mapping server</td></tr>
<tr><td><strong>Map-Resolver</strong></td><td>Server that resolves mapping requests</td></tr>
</table>

<p><strong>Operation</strong>:</p>

<ol>
<li>A source host sends a packet to a destination EID</li>
<li>The ITR queries the mapping system to obtain the RLOC associated with the destination EID</li>
<li>The ITR encapsulates the original packet in a new IP packet with the RLOC as destination</li>
<li>The packet traverses the core network using RLOCs</li>
<li>The ETR decapsulates the packet and delivers it to the destination host</li>
</ol>

<p><strong>LISP advantages</strong>:</p>
<ul>
<li><strong>Routing table reduction</strong>: only RLOCs are advertised in the core network</li>
<li><strong>Mobility</strong>: a host can change its location (RLOC) without changing its identity (EID)</li>
<li><strong>Multi-homing</strong>: an EID can be associated with multiple RLOCs for redundancy</li>
<li><strong>Traffic engineering</strong>: selection of the best RLOC according to metrics</li>
</ul>

<h3 class="section-title">12. Network programmability and APIs</h3>

<p>Programmability is at the heart of the transformation of modern networks. SDN and NFV converge to create fully automatable and programmable networks.</p>

<p><strong>Programmability levels</strong>:</p>

<ul>
<li><strong>Automated configuration</strong>: scripts and tools (Ansible, Puppet, Chef) for deploying configurations</li>
<li><strong>SDN controllers</strong>: programming network behavior via Python/Java applications</li>
<li><strong>REST APIs</strong>: standardized interfaces for interacting with controllers and VNFs</li>
<li><strong>Intent-Based Networking</strong>: expression of intent (high-level policy) automatically translated into configuration</li>
</ul>

<p><strong>SDN + NFV convergence</strong>:</p>

<p>SDN and NFV are complementary:</p>
<ul>
<li>SDN provides <strong>network programmability</strong> (data plane)</li>
<li>NFV provides <strong>function virtualization</strong> (service plane)</li>
<li>Together, they enable the creation of fully software-defined, agile and automated network infrastructures</li>
</ul>

<p>This convergence is at the heart of 5G network architectures, where network slicing relies on the ability to create virtual network slices with specific VNFs, interconnected by an SDN data plane.</p>

<hr>

<h2>PART D - Analysis and Reflection</h2>

<h3 class="section-title">Skills acquired</h3>

<p><strong>Understanding of the SDN paradigm</strong>:<br>
Mastery of the control plane / data plane separation, the OpenFlow protocol and the three-layer architecture. Ability to explain the advantages and limitations of SDN compared to traditional networks.</p>

<p><strong>Open vSwitch configuration</strong>:<br>
Practical competency in creating logical bridges, attaching physical ports and managing OVS instances on real Pica8 equipment.</p>

<p><strong>OpenFlow rule programming</strong>:<br>
Ability to install flow rules at different levels of granularity: input port, IP addresses, transport protocols, application ports. Understanding of the impact of granularity on control precision and performance.</p>

<p><strong>SDN controller deployment</strong>:<br>
Experience with the Ryu controller, from verbose mode launch to running control applications (simple_switch_14). Understanding of reactive and proactive operation.</p>

<p><strong>Complex topology management</strong>:<br>
Experience deploying multi-switch mesh topologies and understanding loop problems and their solutions in an SDN context.</p>

<p><strong>NFV and MANO understanding</strong>:<br>
Knowledge of the network function virtualization architecture, VNF lifecycle and the MANO framework for orchestration.</p>

<h3 class="section-title">Self-assessment</h3>

<p>I found the "Emerging Network Technologies" course very engaging and educational, although some aspects were a bit complex for me as a student specializing in Electronics and Automation compared to those in the Network option. Despite this, I was actively involved in simulating topologies and testing various aspects, which provided me with a practical understanding of how these technologies are transforming network management.</p>

<p>Working on real Pica8 equipment was the most enriching part. Handling physical switches, installing OpenFlow rules and observing their immediate effect on connectivity provides a concrete dimension that simulations cannot offer.</p>

<p>The main challenge was understanding the mesh topology and loop management. Seeing the network become unstable with the addition of a single physical link made me understand the critical importance of loop prevention and the power of the SDN controller to solve this problem in a centralized manner.</p>

<p>As I am also enrolled in the <a href="./master-reoc.html">Master REOC</a>, I had already worked on SDN and Ryu in a more exploratory context. This course solidified my skills with a more structured and progressive approach. In REOC, we had conducted our own research and project, which offered a more hands-on but less guided experience.</p>

<h3 class="section-title">Professional perspectives</h3>

<p>The emerging technologies covered in this course are at the heart of network infrastructure transformation:</p>

<ul>
<li><strong>Telecom operators</strong>: 5G deployment with network slicing (SDN + NFV)</li>
<li><strong>Cloud providers</strong>: virtual networks (VPC) and SDN for multi-tenancy</li>
<li><strong>Enterprises</strong>: SD-WAN to connect remote sites with agility</li>
<li><strong>Data centers</strong>: datacenter network automation with SDN</li>
<li><strong>IoT</strong>: intelligent IoT flow management via SDN controllers</li>
</ul>

<hr>

<h2>Course Documents</h2>

<hr>

<h2>Reports and Projects</h2>

<hr>

<p><em>Course taken in 2024-2025 at INSA Toulouse, Department of Electrical and Computer Engineering.</em></p>

</div>

<div class="back-nav">
    <a href="./my-courses-2024-2025.html" data-i18n-html="back-courses-2024-2025">&larr; Retour aux Cours 2024-2025</a>
</div>

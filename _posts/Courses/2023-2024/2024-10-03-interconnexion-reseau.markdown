---
layout: default
title: "Interconnexion Réseau - Semestre 8"
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
    <a href="./my-courses-2023-2024.html" data-i18n-html="back-courses-2023-2024">&larr; Retour aux Cours 2023-2024</a>
</div>

<div class="lang-fr">

<h1>Interconnexion Reseau - Semestre 8</h1>

<p><strong>Annee academique</strong> : 2023-2024<br/>
<strong>ECTS</strong> : 2.5<br/>
<strong>Categorie</strong> : Reseaux et Telecommunications</p>

<hr/>

<h2>PART A - Presentation Generale du Module</h2>

<h3 class="section-title">Vue d'ensemble</h3>

<p>Ce cours approfondit les concepts et protocoles permettant l'interconnexion de reseaux heterogenes pour former l'Internet global. Il couvre le routage IP, les protocoles de transport TCP et UDP, la qualite de service, les VLANs, la securite reseau, et les architectures modernes. L'objectif est de former des ingenieurs capables de concevoir, deployer et administrer des infrastructures reseau complexes.</p>

<p><strong>Objectifs pedagogiques</strong> :</p>
<ul>
<li>Maitriser les protocoles TCP/IP et le modele en couches</li>
<li>Configurer et administrer routeurs et commutateurs Cisco</li>
<li>Implementer des protocoles de routage dynamique (RIP, OSPF, BGP)</li>
<li>Concevoir des architectures reseau multi-sites</li>
<li>Mettre en oeuvre la qualite de service (QoS)</li>
<li>Segmenter des reseaux avec VLANs</li>
<li>Securiser les infrastructures (ACL, VPN, pare-feu)</li>
<li>Diagnostiquer et resoudre des problemes reseau</li>
</ul>

<h3 class="section-title">Position dans le cursus</h3>

<p>Ce module approfondit les bases acquises precedemment :</p>
<ul>
<li><strong>Reseau (S5)</strong> : modele OSI, Ethernet, IP de base, TCP/UDP</li>
<li><strong>Architecture Materielle (S6)</strong> : couche physique, signaux</li>
<li><strong>Systemes d'Exploitation (S5)</strong> : sockets, communication inter-processus</li>
</ul>

<p>Il prepare a :</p>
<ul>
<li><strong>Cloud et Edge Computing (S9)</strong> : reseaux virtuels, SDN</li>
<li><strong>IoT (S9)</strong> : protocoles specifiques, contraintes reseaux</li>
<li><strong>Cybersecurite</strong> : securite reseau avancee</li>
<li><strong>Carriere professionnelle</strong> : administration reseau, architecte infrastructure</li>
</ul>

<hr/>

<h2>PART B - Experience Personnelle et Contexte d'Apprentissage</h2>

<h3 class="section-title">Organisation et ressources</h3>

<p>Le module combinait theorie et pratique intensive :</p>

<p><strong>Cours magistraux (15h)</strong> :</p>
<ul>
<li>Modeles OSI et TCP/IP, encapsulation</li>
<li>Adressage IPv4 et IPv6, subnetting</li>
<li>Protocoles de routage (statique, RIP, OSPF, BGP)</li>
<li>TCP et UDP en detail</li>
<li>Qualite de service (QoS)</li>
<li>VLANs et commutation</li>
<li>Securite reseau (ACL, VPN, pare-feu)</li>
<li>NAT et translation d'adresses</li>
</ul>

<p><strong>Travaux diriges (6h)</strong> :</p>
<ul>
<li>Calculs de subnetting</li>
<li>Conception d'architectures reseau</li>
<li>Analyse de protocoles</li>
<li>Configuration de routage</li>
</ul>

<p><strong>Travaux pratiques (12h)</strong> :</p>
<ul>
<li><strong>TP1</strong> : Configuration de base routeurs Cisco, routage statique</li>
<li><strong>TP2</strong> : Protocoles de routage dynamique (RIP, OSPF)</li>
<li><strong>TP3</strong> : VLANs, inter-VLAN routing, ACLs</li>
</ul>

<p><strong>Outils utilises</strong> :</p>
<ul>
<li><strong>Cisco Packet Tracer</strong> : simulation de reseaux</li>
<li><strong>GNS3</strong> : emulation equipements reseau</li>
<li><strong>Equipements Cisco</strong> : routeurs et switches physiques</li>
<li><strong>Wireshark</strong> : capture et analyse de trafic</li>
<li><strong>Cisco IOS</strong> : systeme d'exploitation routeurs/switches</li>
</ul>

<p><strong>Ressources</strong> :</p>
<ul>
<li>Polycope complet (4AE-Interconnexion-Rzo)</li>
<li>TD avec exercices pratiques</li>
<li>3 TP guides avec configurations</li>
<li>Documentation Cisco</li>
<li>RFCs des protocoles (TCP, IP, OSPF, BGP)</li>
</ul>

<h3 class="section-title">Methodologie d'etude</h3>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S8/interconnexion-reseau/modele-osi.svg" alt="Modele OSI 7 couches"
       style="max-width: 500px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Modele OSI a 7 couches avec protocoles et encapsulation</p>
</div>

<p><strong>Phase 1 : Maitriser les fondamentaux</strong> :
Reviser modele en couches, adressage IP, principes du routage.</p>

<p><strong>Phase 2 : Approfondir les protocoles</strong> :
Etudier en detail TCP, UDP, OSPF, BGP avec leurs mecanismes internes.</p>

<p><strong>Phase 3 : Pratiquer la configuration</strong> :
Utiliser Packet Tracer pour configurer des scenarios reseau de complexite croissante.</p>

<p><strong>Phase 4 : Analyser le trafic</strong> :
Capturer avec Wireshark pour observer les echanges protocolaires reels.</p>

<p><strong>Phase 5 : Developper le troubleshooting</strong> :
Diagnostiquer pannes reseau selon methodologie (bottom-up ou top-down du modele OSI).</p>

<h3 class="section-title">Difficultes rencontrees</h3>

<p><strong>Complexite des protocoles</strong> :
OSPF et BGP sont des protocoles tres riches avec de nombreux parametres et cas particuliers.</p>

<p><strong>Syntaxe Cisco IOS</strong> :
La ligne de commande Cisco a sa propre logique et commandes specifiques a memoriser.</p>

<p><strong>Debogage reseau</strong> :
Identifier la source d'un probleme dans un reseau complexe demande methodologie et patience.</p>

<p><strong>Abstraction vs realite</strong> :
Les simulations sont simplifiees. Les reseaux reels ont des contraintes physiques, latences, pannes aleatoires.</p>

<hr/>

<h2>PART C - Aspects Techniques Detailles</h2>

<h3 class="section-title">1. Modeles de reference reseau</h3>

<p><strong>Modele OSI (7 couches)</strong> :</p>

<p>Modele de reference theorique pour l'architecture des reseaux.</p>

<table>
<tr><th>Couche</th><th>Nom</th><th>Role</th><th>Exemples</th></tr>
<tr><td>7</td><td>Application</td><td>Services aux applications</td><td>HTTP, FTP, DNS, SMTP</td></tr>
<tr><td>6</td><td>Presentation</td><td>Format, chiffrement, compression</td><td>SSL/TLS, JPEG, MPEG</td></tr>
<tr><td>5</td><td>Session</td><td>Gestion des sessions</td><td>NetBIOS, RPC</td></tr>
<tr><td>4</td><td>Transport</td><td>Transmission bout en bout</td><td>TCP, UDP</td></tr>
<tr><td>3</td><td>Reseau</td><td>Routage, adressage logique</td><td>IP, ICMP, OSPF, BGP</td></tr>
<tr><td>2</td><td>Liaison</td><td>Transmission sur lien physique, adressage MAC</td><td>Ethernet, WiFi, PPP</td></tr>
<tr><td>1</td><td>Physique</td><td>Transmission bits (signaux electriques, optiques)</td><td>Cables, ondes radio</td></tr>
</table>

<p><strong>Modele TCP/IP (4 couches)</strong> :</p>

<p>Modele pratique utilise sur Internet.</p>

<table>
<tr><th>Couche</th><th>Equivalent OSI</th><th>Protocoles principaux</th></tr>
<tr><td>Application</td><td>5-6-7</td><td>HTTP, FTP, DNS, SMTP, SSH</td></tr>
<tr><td>Transport</td><td>4</td><td>TCP, UDP</td></tr>
<tr><td>Internet</td><td>3</td><td>IP, ICMP, ARP</td></tr>
<tr><td>Acces reseau</td><td>1-2</td><td>Ethernet, WiFi</td></tr>
</table>

<p><strong>Encapsulation</strong> :</p>

<p>Chaque couche ajoute son en-tete aux donnees de la couche superieure.</p>

<p>Donnees application &rarr; Segment TCP &rarr; Paquet IP &rarr; Trame Ethernet</p>

<p><strong>Desencapsulation</strong> :</p>

<p>Le recepteur retire les en-tetes couche par couche pour extraire les donnees.</p>

<h3 class="section-title">2. Adressage IPv4</h3>

<p><strong>Format</strong> :</p>

<p>Adresse sur 32 bits, notee en 4 octets decimaux separes par des points.</p>

<p>Exemple : 192.168.1.10</p>

<p><strong>Classes historiques (obsoletes)</strong> :</p>

<p>Remplacees par CIDR, mais utiles pour comprendre l'evolution.</p>

<ul>
<li>Classe A : premier bit = 0, reseau sur 8 bits (grands reseaux)</li>
<li>Classe B : premiers bits = 10, reseau sur 16 bits</li>
<li>Classe C : premiers bits = 110, reseau sur 24 bits</li>
</ul>

<p><strong>CIDR (Classless Inter-Domain Routing)</strong> :</p>

<p>Notation flexible : adresse IP / longueur prefixe reseau</p>

<p>Exemple : 192.168.10.0/24 signifie reseau sur 24 bits, 8 bits pour hotes (256 adresses).</p>

<p><strong>Masque de sous-reseau</strong> :</p>

<p>Determine quelle partie de l'adresse est le reseau et quelle partie est l'hote.</p>

<p>/24 correspond au masque 255.255.255.0</p>

<p><strong>Adresses speciales</strong> :</p>

<ul>
<li><strong>Adresse reseau</strong> : tous les bits hote a 0 (ex : 192.168.1.0)</li>
<li><strong>Adresse broadcast</strong> : tous les bits hote a 1 (ex : 192.168.1.255)</li>
<li><strong>Loopback</strong> : 127.0.0.1 (interface de bouclage local)</li>
<li><strong>Plages privees (RFC 1918)</strong> : non routables sur Internet
  <ul>
  <li>10.0.0.0/8</li>
  <li>172.16.0.0/12</li>
  <li>192.168.0.0/16</li>
  </ul>
</li>
</ul>

<p><strong>Subnetting</strong> :</p>

<p>Division d'un reseau en sous-reseaux plus petits pour optimiser l'utilisation des adresses et segmenter le reseau.</p>

<p>Exemple : 192.168.1.0/24 divise en 4 sous-reseaux /26 :</p>
<ul>
<li>192.168.1.0/26 (adresses .0 a .63)</li>
<li>192.168.1.64/26 (adresses .64 a .127)</li>
<li>192.168.1.128/26 (adresses .128 a .191)</li>
<li>192.168.1.192/26 (adresses .192 a .255)</li>
</ul>

<h3 class="section-title">3. IPv6</h3>

<p><strong>Motivation</strong> :</p>

<p>Epuisement des adresses IPv4 publiques. IPv6 offre un espace d'adressage quasi illimite.</p>

<p><strong>Format</strong> :</p>

<p>Adresse sur 128 bits, notee en 8 groupes de 4 chiffres hexadecimaux separes par deux-points.</p>

<p>Exemple : 2001:0db8:85a3:0000:0000:8a2e:0370:7334</p>

<p><strong>Simplifications d'ecriture</strong> :</p>

<ul>
<li>Omettre les zeros en tete de chaque groupe : 2001:db8:85a3:0:0:8a2e:370:7334</li>
<li>Remplacer une sequence de groupes nuls consecutifs par :: (une seule fois) : 2001:db8:85a3::8a2e:370:7334</li>
</ul>

<p><strong>Avantages</strong> :</p>

<ul>
<li>Espace d'adressage immense (2 puissance 128 adresses)</li>
<li>Autoconfiguration simplifiee (SLAAC)</li>
<li>IPsec integre natif</li>
<li>En-tete simplifie (meilleure performance)</li>
<li>Plus besoin de NAT</li>
</ul>

<p><strong>Types d'adresses</strong> :</p>

<ul>
<li><strong>Unicast</strong> : adresse unique identifiant une interface</li>
<li><strong>Multicast</strong> : groupe d'interfaces (remplace broadcast)</li>
<li><strong>Anycast</strong> : groupe d'interfaces, route vers la plus proche</li>
</ul>

<p><strong>Adresses speciales</strong> :</p>

<ul>
<li><strong>Loopback</strong> : ::1</li>
<li><strong>Link-local</strong> : fe80::/10 (auto-configurees, communication sur lien local)</li>
<li><strong>Unique local</strong> : fc00::/7 (equivalent des privees IPv4)</li>
<li><strong>Global unicast</strong> : 2000::/3 (routables sur Internet)</li>
</ul>

<h3 class="section-title">4. Routage - Principes fondamentaux</h3>

<p><strong>Role du routeur</strong> :</p>

<p>Transferer des paquets IP entre reseaux differents en consultant sa table de routage.</p>

<p><strong>Table de routage</strong> :</p>

<p>Contient les routes vers les reseaux de destination.</p>

<p>Chaque entree specifie :</p>
<ul>
<li><strong>Reseau de destination</strong> avec masque</li>
<li><strong>Passerelle (next hop)</strong> : adresse IP du prochain routeur ou "directement connecte"</li>
<li><strong>Interface de sortie</strong> : par quelle interface envoyer le paquet</li>
<li><strong>Metrique</strong> : cout de la route (distance, bande passante, etc.)</li>
</ul>

<p><strong>Processus de routage</strong> :</p>

<ol>
<li>Recevoir paquet IP</li>
<li>Consulter table de routage pour trouver meilleure route (longest prefix match)</li>
<li>Decrementer TTL (Time To Live)</li>
<li>Recalculer checksum de l'en-tete IP</li>
<li>Transferer paquet sur l'interface de sortie appropriee</li>
</ol>

<p><strong>Route par defaut (default route)</strong> :</p>

<p>Route 0.0.0.0/0 utilisee si aucune route specifique ne correspond. Typiquement vers Internet via passerelle FAI.</p>

<p><strong>Routage statique vs dynamique</strong> :</p>

<ul>
<li><strong>Statique</strong> : routes configurees manuellement, adaptees pour petits reseaux ou routes specifiques</li>
<li><strong>Dynamique</strong> : protocoles de routage automatisent la decouverte et mise a jour des routes</li>
</ul>

<h3 class="section-title">5. Protocoles de routage dynamique</h3>

<p><strong>Classification</strong> :</p>

<p><strong>IGP (Interior Gateway Protocol)</strong> : au sein d'un systeme autonome (AS)</p>
<ul>
<li><strong>Distance vector</strong> : RIP, EIGRP</li>
<li><strong>Link state</strong> : OSPF, IS-IS</li>
</ul>

<p><strong>EGP (Exterior Gateway Protocol)</strong> : entre systemes autonomes</p>
<ul>
<li><strong>Path vector</strong> : BGP</li>
</ul>

<p><strong>RIP (Routing Information Protocol)</strong> :</p>

<p>Protocole de routage distance-vector simple.</p>

<p><strong>Caracteristiques</strong> :</p>
<ul>
<li>Metrique : nombre de sauts (hop count), maximum 15</li>
<li>Algorithme Bellman-Ford</li>
<li>Mise a jour complete de la table toutes les 30 secondes</li>
<li>Convergence lente</li>
<li>Simple mais limite aux petits reseaux</li>
</ul>

<p><strong>OSPF (Open Shortest Path First)</strong> :</p>

<p>Protocole link-state avance.</p>

<p><strong>Principe</strong> :</p>
<ul>
<li>Chaque routeur connait la topologie complete de la zone</li>
<li>Algorithme SPF (Dijkstra) calcule l'arbre des plus courts chemins</li>
<li>Metrique basee sur le cout (fonction de la bande passante)</li>
</ul>

<p><strong>Fonctionnement</strong> :</p>
<ol>
<li>Decouverte des voisins via paquets Hello</li>
<li>Echange de LSA (Link State Advertisement) decrivant les liens</li>
<li>Construction de la base de donnees topologique (LSDB)</li>
<li>Calcul SPF pour determiner meilleures routes</li>
<li>Installation des routes dans la table de routage</li>
</ol>

<p><strong>Avantages</strong> :</p>
<ul>
<li>Convergence rapide (mises a jour declenchees, pas periodiques)</li>
<li>Scalabilite via hierarchie (aires)</li>
<li>Supporte VLSM et CIDR</li>
<li>Authentification des mises a jour</li>
</ul>

<p><strong>Hierarchie OSPF</strong> :</p>

<p>Organisation en aires pour reduire trafic et taille des tables.</p>

<ul>
<li><strong>Aire 0 (backbone)</strong> : aire centrale obligatoire</li>
<li><strong>Aires non-backbone</strong> : connectees a l'aire 0 via ABR (Area Border Router)</li>
</ul>

<p><strong>BGP (Border Gateway Protocol)</strong> :</p>

<p>Protocole de routage d'Internet entre systemes autonomes.</p>

<p><strong>Caracteristiques</strong> :</p>
<ul>
<li>Path vector : inclut le chemin complet d'AS</li>
<li>Politiques de routage complexes (business, preferences)</li>
<li>eBGP (external) entre AS differents, iBGP (internal) au sein d'un AS</li>
<li>Metrique : pas seulement technique mais aussi politique</li>
</ul>

<p><strong>Role</strong> :</p>

<p>BGP maintient la table de routage globale d'Internet. Chaque AS annonce ses prefixes IP.</p>

<h3 class="section-title">6. Protocole TCP (Transmission Control Protocol)</h3>

<p><strong>Caracteristiques</strong> :</p>

<p>Protocole de transport oriente connexion, fiable.</p>

<ul>
<li><strong>Oriente connexion</strong> : etablissement 3-way handshake avant echange de donnees</li>
<li><strong>Fiable</strong> : accuses de reception, retransmission des segments perdus</li>
<li><strong>Ordre preserve</strong> : numeros de sequence garantissent l'ordre</li>
<li><strong>Controle de flux</strong> : fenetre glissante evite debordement recepteur</li>
<li><strong>Controle de congestion</strong> : adapte debit selon etat du reseau</li>
</ul>

<p><strong>En-tete TCP (principaux champs)</strong> :</p>

<ul>
<li><strong>Ports source et destination</strong> (16 bits chacun) : identifient applications</li>
<li><strong>Numero de sequence</strong> (32 bits) : position des donnees dans le flux</li>
<li><strong>Numero d'accuse de reception</strong> (32 bits) : prochain octet attendu</li>
<li><strong>Flags</strong> : SYN (synchronisation), ACK (accuse), FIN (fin), RST (reset), PSH (push), URG (urgent)</li>
<li><strong>Fenetre</strong> (16 bits) : taille du buffer recepteur disponible (controle de flux)</li>
<li><strong>Checksum</strong> (16 bits) : detection d'erreurs</li>
</ul>

<p><strong>Etablissement de connexion (3-way handshake)</strong> :</p>

<ol>
<li><strong>Client &rarr; Serveur : SYN</strong> (synchronisation, numero de sequence initial)</li>
<li><strong>Serveur &rarr; Client : SYN+ACK</strong> (acquittement + son propre numero de sequence)</li>
<li><strong>Client &rarr; Serveur : ACK</strong> (acquittement final)</li>
</ol>

<p>Connexion etablie, echange de donnees peut commencer.</p>

<p><strong>Fermeture de connexion (4-way handshake)</strong> :</p>

<ol>
<li><strong>A &rarr; B : FIN</strong> (A a fini d'envoyer)</li>
<li><strong>B &rarr; A : ACK</strong> (acquittement)</li>
<li><strong>B &rarr; A : FIN</strong> (B a fini d'envoyer)</li>
<li><strong>A &rarr; B : ACK</strong> (acquittement final)</li>
</ol>

<p>Ou fermeture brutale avec RST (reset).</p>

<p><strong>Controle de flux (fenetre glissante)</strong> :</p>

<p>Le recepteur annonce la taille de son buffer disponible (fenetre).</p>

<p>L'emetteur ne peut pas envoyer plus de donnees que la taille de la fenetre.</p>

<p>Evite debordement du buffer recepteur.</p>

<p><strong>Controle de congestion</strong> :</p>

<p>Mecanisme pour adapter le debit selon l'etat du reseau et eviter l'effondrement.</p>

<p><strong>Phases</strong> :</p>
<ul>
<li><strong>Slow Start</strong> : augmentation exponentielle de la fenetre de congestion</li>
<li><strong>Congestion Avoidance</strong> : augmentation lineaire apres atteinte d'un seuil</li>
<li><strong>Fast Retransmit</strong> : retransmission immediate apres 3 ACK dupliques</li>
<li><strong>Fast Recovery</strong> : reduction moderee de la fenetre apres perte</li>
</ul>

<p><strong>Algorithmes</strong> : TCP Tahoe, Reno, New Reno, CUBIC (utilise par Linux par defaut).</p>

<h3 class="section-title">7. Protocole UDP (User Datagram Protocol)</h3>

<p><strong>Caracteristiques</strong> :</p>

<p>Protocole de transport simple, non connecte, non fiable.</p>

<ul>
<li><strong>Sans connexion</strong> : pas d'etablissement de connexion</li>
<li><strong>Non fiable</strong> : pas d'accuse de reception, pas de retransmission</li>
<li><strong>Pas de controle de flux ni de congestion</strong></li>
<li><strong>Pas de garantie d'ordre</strong></li>
<li><strong>En-tete minimal</strong> : seulement 8 octets</li>
</ul>

<p><strong>En-tete UDP</strong> :</p>

<ul>
<li>Port source (16 bits)</li>
<li>Port destination (16 bits)</li>
<li>Longueur (16 bits)</li>
<li>Checksum (16 bits)</li>
</ul>

<p><strong>Utilisations</strong> :</p>

<p>Applications ou la rapidite prime sur la fiabilite :</p>
<ul>
<li><strong>VoIP et videoconference</strong> : temps reel, perte acceptable</li>
<li><strong>Streaming video/audio</strong> : retransmission inutile (deja trop tard)</li>
<li><strong>DNS</strong> : requetes courtes, retransmission geree par application</li>
<li><strong>DHCP</strong> : configuration reseau initiale</li>
<li><strong>Jeux en ligne</strong> : latence critique</li>
<li><strong>SNMP</strong> : gestion reseau simple</li>
</ul>

<p><strong>Avantages</strong> :</p>

<p>Faible overhead, latence minimale, adapte aux applications temps reel.</p>

<h3 class="section-title">8. Qualite de Service (QoS)</h3>

<p><strong>Problematique</strong> :</p>

<p>Le reseau Internet est "best-effort" (meilleur effort) : aucune garantie de bande passante, latence, ou fiabilite.</p>

<p>Insuffisant pour applications exigeantes : VoIP (voix), videoconference, streaming.</p>

<p><strong>Parametres de QoS</strong> :</p>

<table>
<tr><th>Parametre</th><th>Description</th><th>Importance pour</th></tr>
<tr><td>Bande passante</td><td>Debit garanti</td><td>Streaming video</td></tr>
<tr><td>Latence</td><td>Delai de transit</td><td>VoIP, jeux</td></tr>
<tr><td>Gigue (jitter)</td><td>Variation de latence</td><td>VoIP, video</td></tr>
<tr><td>Perte de paquets</td><td>Taux de paquets perdus</td><td>Toutes applications</td></tr>
</table>

<p><strong>Mecanismes de QoS</strong> :</p>

<p><strong>Classification et marquage</strong> :</p>

<p>Identifier le type de trafic et le marquer dans l'en-tete pour traitement differencie.</p>

<ul>
<li><strong>DSCP (Differentiated Services Code Point)</strong> : 6 bits dans en-tete IP</li>
<li><strong>CoS (Class of Service)</strong> : 3 bits dans tag 802.1Q (VLAN)</li>
</ul>

<p><strong>Files d'attente (Queuing)</strong> :</p>

<p>Gerer priorites et ordonnancement des paquets.</p>

<ul>
<li><strong>FIFO</strong> : First In First Out (pas de priorite)</li>
<li><strong>Priority Queuing</strong> : files de differentes priorites (stricte)</li>
<li><strong>WFQ (Weighted Fair Queuing)</strong> : partage equitable avec ponderation</li>
<li><strong>CBWFQ (Class-Based WFQ)</strong> : WFQ par classe de trafic</li>
<li><strong>LLQ (Low Latency Queuing)</strong> : file prioritaire + WFQ pour le reste</li>
</ul>

<p><strong>Policing et Shaping</strong> :</p>

<p>Controler le taux de trafic.</p>

<ul>
<li><strong>Policing</strong> : limiter le debit, rejeter ou remarquer l'excedent</li>
<li><strong>Shaping</strong> : lisser le trafic, tamponner l'excedent dans une file</li>
</ul>

<p><strong>Modeles de QoS</strong> :</p>

<ul>
<li><strong>IntServ (Integrated Services)</strong> : reservation de ressources par flux (RSVP), peu deploye (complexite)</li>
<li><strong>DiffServ (Differentiated Services)</strong> : classes de service agregees, scalable, largement deploye</li>
</ul>

<h3 class="section-title">9. VLANs (Virtual LANs)</h3>

<p><strong>Principe</strong> :</p>

<p>Segmenter un reseau physique en plusieurs reseaux logiques isoles.</p>

<p><strong>Avantages</strong> :</p>

<ul>
<li><strong>Isolation des domaines de broadcast</strong> : reduit trafic inutile</li>
<li><strong>Securite</strong> : separation logique du trafic (finance, RH, invites)</li>
<li><strong>Flexibilite</strong> : reorganisation sans recablage physique</li>
<li><strong>Optimisation</strong> : grouper utilisateurs par fonction plutot que par localisation</li>
</ul>

<p><strong>Standard 802.1Q (VLAN Tagging)</strong> :</p>

<p>Ajout d'un tag de 4 octets dans la trame Ethernet contenant :</p>
<ul>
<li><strong>VLAN ID</strong> (12 bits) : identifiant du VLAN (4096 VLANs possibles)</li>
<li><strong>Priority</strong> (3 bits) : priorite CoS pour QoS</li>
</ul>

<p><strong>Types de ports</strong> :</p>

<table>
<tr><th>Type</th><th>Description</th><th>Utilisation</th></tr>
<tr><td>Access</td><td>Appartient a un seul VLAN, pas de tag</td><td>Connexion terminaux</td></tr>
<tr><td>Trunk</td><td>Transporte plusieurs VLANs, avec tags</td><td>Interconnexion switches</td></tr>
</table>

<p><strong>Communication inter-VLANs</strong> :</p>

<p>Les VLANs sont isoles. Pour communiquer entre eux, il faut un routeur (ou switch layer 3).</p>

<p>Methodes :</p>
<ul>
<li><strong>Router on a stick</strong> : un seul lien physique, sous-interfaces par VLAN</li>
<li><strong>Switch L3</strong> : routage inter-VLAN directement sur le switch</li>
</ul>

<h3 class="section-title">10. Commutation (Switching)</h3>

<p><strong>Principe</strong> :</p>

<p>Un switch (commutateur) transfere des trames Ethernet selon les adresses MAC.</p>

<p><strong>Table CAM (Content Addressable Memory)</strong> :</p>

<p>Associe adresses MAC aux ports du switch.</p>

<p><strong>Apprentissage</strong> :</p>

<p>Le switch apprend les adresses MAC en observant l'adresse source des trames recues.</p>

<p><strong>Transfert (Forwarding)</strong> :</p>

<ul>
<li><strong>Adresse destination connue</strong> : transferer sur le port associe dans la table CAM</li>
<li><strong>Adresse inconnue</strong> : flood (diffuser) sur tous les ports sauf celui de reception</li>
<li><strong>Broadcast ou multicast</strong> : flood</li>
</ul>

<p><strong>Spanning Tree Protocol (STP)</strong> :</p>

<p>Protocole pour eviter les boucles dans les topologies redondantes (liens multiples entre switches).</p>

<p><strong>Fonctionnement</strong> :</p>
<ol>
<li>Election d'un root bridge (switch racine)</li>
<li>Calcul du chemin optimal vers le root bridge</li>
<li>Blocage des ports creant des boucles</li>
<li>Reconfiguration automatique en cas de panne</li>
</ol>

<p><strong>Variantes</strong> : RSTP (Rapid STP) pour convergence plus rapide, MSTP (Multiple STP) pour plusieurs VLANs.</p>

<h3 class="section-title">11. NAT (Network Address Translation)</h3>

<p><strong>Problematique</strong> :</p>

<p>Penurie d'adresses IPv4 publiques. Toutes les machines ne peuvent pas avoir une adresse publique.</p>

<p><strong>Principe</strong> :</p>

<p>Traduire des adresses IP privees en adresses publiques lors de la traversee d'un routeur.</p>

<p><strong>Types de NAT</strong> :</p>

<p><strong>NAT statique</strong> :</p>

<p>Mapping fixe 1:1 entre une adresse privee et une adresse publique.</p>

<p>Usage : serveurs accessibles depuis Internet.</p>

<p><strong>NAT dynamique</strong> :</p>

<p>Pool d'adresses publiques, allocation dynamique aux machines internes.</p>

<p><strong>PAT (Port Address Translation) ou NAT Overload</strong> :</p>

<p>Plusieurs machines internes partagent une seule adresse publique.</p>

<p>Differenciation par numeros de port.</p>

<p>Table NAT associe : IP privee:port prive &harr; IP publique:port public</p>

<p><strong>Usage</strong> : la plupart des box Internet (tous les equipements domestiques partagent l'IP publique).</p>

<p><strong>Limitations du NAT</strong> :</p>

<ul>
<li>Casse la connectivite bout-a-bout (end-to-end)</li>
<li>Problemes pour protocoles incluant adresses IP dans donnees (FTP, SIP)</li>
<li>Difficultes pour applications P2P et serveurs entrants</li>
<li>Necessite techniques de traversee (STUN, TURN) pour VoIP</li>
</ul>

<p><strong>IPv6 et NAT</strong> :</p>

<p>IPv6 rend NAT inutile (adresses suffisantes pour tous). Retour a la connectivite bout-a-bout.</p>

<h3 class="section-title">12. Securite reseau</h3>

<p><strong>Listes de Controle d'Acces (ACL)</strong> :</p>

<p>Filtrer le trafic selon criteres definis (adresses IP, ports, protocoles).</p>

<p><strong>Types</strong> :</p>
<ul>
<li><strong>ACL standard</strong> : filtre uniquement sur adresse IP source</li>
<li><strong>ACL etendue</strong> : filtre sur IP source/destination, ports, protocoles</li>
</ul>

<p><strong>Application</strong> : sur interfaces de routeurs (trafic entrant ou sortant).</p>

<p><strong>Pare-feu (Firewall)</strong> :</p>

<p>Equipement ou logiciel filtrant le trafic de maniere plus sophistiquee.</p>

<p><strong>Fonctionnalites</strong> :</p>
<ul>
<li>Filtrage stateful (inspection d'etat des connexions)</li>
<li>Filtrage applicatif (deep packet inspection)</li>
<li>Prevention d'intrusions (IPS)</li>
<li>Journalisation et alertes</li>
</ul>

<p><strong>VPN (Virtual Private Network)</strong> :</p>

<p>Creer un tunnel securise a travers un reseau non securise (Internet).</p>

<p><strong>Types</strong> :</p>
<ul>
<li><strong>Site-to-Site</strong> : interconnecter des sites distants d'une entreprise</li>
<li><strong>Remote Access</strong> : permettre acces distant securise (teletravail)</li>
</ul>

<p><strong>Protocoles</strong> :</p>
<ul>
<li><strong>IPsec</strong> : chiffrement au niveau IP (tunnel ou transport)</li>
<li><strong>SSL/TLS VPN</strong> : base sur HTTPS, plus simple pour remote access</li>
</ul>

<p><strong>Menaces courantes</strong> :</p>

<table>
<tr><th>Menace</th><th>Description</th><th>Contre-mesure</th></tr>
<tr><td>DoS/DDoS</td><td>Saturation de ressources</td><td>Filtrage, limitation de taux, CDN</td></tr>
<tr><td>Spoofing</td><td>Usurpation d'adresse IP</td><td>Filtrage ingress/egress, authentification</td></tr>
<tr><td>Man-in-the-Middle</td><td>Interception de communication</td><td>Chiffrement (TLS, IPsec)</td></tr>
<tr><td>ARP poisoning</td><td>Corruption de tables ARP</td><td>Dynamic ARP Inspection</td></tr>
<tr><td>VLAN hopping</td><td>Acces non autorise a VLANs</td><td>Configuration securisee trunk/access</td></tr>
</table>

<p><strong>Bonnes pratiques</strong> :</p>

<ul>
<li>Defense en profondeur (multiples couches de securite)</li>
<li>Principe du moindre privilege</li>
<li>Segmentation reseau (VLANs, zones DMZ)</li>
<li>Mises a jour regulieres (firmware, patches)</li>
<li>Surveillance et detection (IDS, SIEM)</li>
<li>Sauvegardes de configurations</li>
</ul>

<hr/>

<h2>PART D - Analyse Reflexive et Perspectives</h2>

<h3 class="section-title">Competences acquises</h3>

<p><strong>Comprehension approfondie TCP/IP</strong> :
Maitrise des protocoles fondamentaux d'Internet et de leur fonctionnement interne.</p>

<p><strong>Configuration d'equipements reseau</strong> :
Capacite a configurer routeurs et switches Cisco via ligne de commande (CLI).</p>

<p><strong>Conception d'architectures reseau</strong> :
Aptitude a concevoir des infrastructures multi-sites avec routage, VLANs, QoS.</p>

<p><strong>Troubleshooting methodique</strong> :
Competence pour diagnostiquer et resoudre des problemes reseau en suivant le modele en couches.</p>

<p><strong>Securisation des infrastructures</strong> :
Capacite a implementer ACLs, VPN, segmentation pour securiser un reseau.</p>

<h3 class="section-title">Points cles a retenir</h3>

<p><strong>1. Le modele en couches est fondamental</strong> :
Comprendre l'encapsulation et le role de chaque couche permet de diagnostiquer efficacement les problemes.</p>

<p><strong>2. OSPF est le protocole IGP moderne</strong> :
RIP est obsolete pour reseaux de taille significative. OSPF offre scalabilite et convergence rapide.</p>

<p><strong>3. TCP assure la fiabilite, UDP la rapidite</strong> :
Choisir le bon protocole de transport selon les besoins de l'application.</p>

<p><strong>4. La QoS est cruciale pour temps reel</strong> :
VoIP et video necessitent priorite et garanties pour fonctionner correctement.</p>

<p><strong>5. VLANs = segmentation logique efficace</strong> :
Organiser le reseau en VLANs ameliore securite, performance, et gestion.</p>

<h3 class="section-title">Retour d'experience</h3>

<p><strong>Aspect formateur</strong> :
Les TP sur equipements Cisco ont donne une dimension concrete a la theorie. Voir les routes apparaitre dans la table apres configuration d'OSPF est satisfaisant.</p>

<p><strong>Complexite de Cisco IOS</strong> :
La CLI Cisco a une courbe d'apprentissage. Les modes (user, privileged, configuration) et la hierarchie des commandes demandent pratique.</p>

<p><strong>Importance du troubleshooting</strong> :
Les configurations ne fonctionnent pas toujours du premier coup. Apprendre a diagnostiquer methodiquement (ping, traceroute, show commands) est essentiel.</p>

<p><strong>Protocoles robustes</strong> :
TCP et OSPF sont des merveilles d'ingenierie. Leur robustesse face aux pannes et congestions est impressionnante.</p>

<h3 class="section-title">Applications pratiques</h3>

<p><strong>Pour administrateur reseau</strong> :</p>
<ul>
<li>Deployer et maintenir infrastructures reseau d'entreprise</li>
<li>Configurer routeurs et switches</li>
<li>Implementer redondance et haute disponibilite</li>
<li>Assurer securite et QoS</li>
</ul>

<p><strong>Pour architecte reseau</strong> :</p>
<ul>
<li>Concevoir architectures multi-sites</li>
<li>Dimensionner bande passante</li>
<li>Choisir equipements et protocoles</li>
<li>Planifier evolution et scalabilite</li>
</ul>

<p><strong>Pour ingenieur DevOps</strong> :</p>
<ul>
<li>Comprendre reseaux cloud (VPC, subnets, routing tables)</li>
<li>Automatiser configurations reseau (Ansible, Terraform)</li>
<li>Optimiser performances applications distribuees</li>
<li>Implementer Load Balancers</li>
</ul>

<p><strong>Pour developpeur</strong> :</p>
<ul>
<li>Comprendre latence reseau et son impact sur applications</li>
<li>Choisir protocoles adaptes (TCP vs UDP)</li>
<li>Implementer retry logic et timeouts</li>
<li>Optimiser pour WAN (compression, caching)</li>
</ul>

<h3 class="section-title">Limites et ouvertures</h3>

<p><strong>Limites du module</strong> :</p>
<ul>
<li>Focus sur Cisco (marche plus diversifie : Juniper, Arista, etc.)</li>
<li>Peu sur IPv6 (transition inevitable)</li>
<li>Pas de SDN (Software-Defined Networking)</li>
<li>Automatisation peu abordee</li>
</ul>

<p><strong>Ouvertures vers</strong> :</p>
<ul>
<li><strong>SDN et NFV</strong> : virtualisation reseau, OpenFlow, controleurs</li>
<li><strong>Cloud networking</strong> : AWS VPC, Azure Virtual Networks</li>
<li><strong>Automation</strong> : Ansible, Python avec Netmiko/NAPALM</li>
<li><strong>Monitoring</strong> : SNMP, NetFlow, observabilite</li>
<li><strong>5G et reseaux mobiles</strong> : architecture, slicing</li>
</ul>

<h3 class="section-title">Evolutions recentes</h3>

<p><strong>Software-Defined Networking (SDN)</strong> :</p>

<p>Separation du plan de controle (decisions de routage) et du plan de donnees (forwarding).</p>

<p>Controleur centralise programmable via API.</p>

<p><strong>Network Functions Virtualization (NFV)</strong> :</p>

<p>Fonctions reseau (firewall, load balancer) en logiciel plutot que materiel dedie.</p>

<p>Flexibilite et reduction des couts.</p>

<p><strong>Intent-Based Networking</strong> :</p>

<p>Definir l'intention (politique) plutot que configuration detaillee.</p>

<p>Le systeme traduit automatiquement l'intention en configuration.</p>

<p><strong>Automation et Infrastructure as Code</strong> :</p>

<p>Configuration reseau declaree dans des fichiers (Ansible, Terraform).</p>

<p>Versionning, reproductibilite, scalabilite.</p>

<p><strong>Reseaux 5G</strong> :</p>

<p>Latence ultra-faible, haut debit, slicing (reseaux virtuels dedies par usage).</p>

<h3 class="section-title">Conseils pour reussir</h3>

<p><strong>1. Pratiquer regulierement</strong> :
Utiliser Packet Tracer ou GNS3 pour reproduire scenarios et experimenter configurations.</p>

<p><strong>2. Comprendre, pas memoriser</strong> :
Comprendre le fonctionnement des protocoles plutot que memoriser syntaxe CLI.</p>

<p><strong>3. Documenter ses configurations</strong> :
Prendre notes des commandes, architectures deployees. Constituer un referentiel personnel.</p>

<p><strong>4. Utiliser Wireshark</strong> :
Capturer et analyser trafic reel pour voir protocoles en action.</p>

<p><strong>5. Suivre la methodologie de troubleshooting</strong> :
Bottom-up (couche 1 &rarr; 7) ou top-down selon symptomes. Methodique et systematique.</p>

<p><strong>6. Se certifier</strong> :
Cisco CCNA est une certification reconnue validant competences reseau de base.</p>

<h3 class="section-title">Conclusion</h3>

<p>Ce module est essentiel pour tout ingenieur travaillant avec des systemes connectes. Les reseaux sont omnipresents : entreprises, datacenters, cloud, IoT, telecommunications.</p>

<p><strong>Competences transferables</strong> :</p>
<ul>
<li>Vision globale des architectures reseau</li>
<li>Capacite a diagnostiquer et resoudre problemes complexes</li>
<li>Comprehension des compromis (performance, securite, cout)</li>
<li>Maitrise des protocoles universels (TCP/IP)</li>
</ul>

<p><strong>Pertinence professionnelle</strong> :
Les competences reseau sont recherchees dans tous les secteurs. L'explosion du cloud, de l'IoT, et des applications distribuees accroit la demande d'ingenieurs reseau qualifies.</p>

<p><strong>Message principal</strong> :
Internet fonctionne grace a des protocoles robustes et des ingenieurs competents. Comprendre ces fondamentaux permet de concevoir, deployer et maintenir des infrastructures fiables et performantes.</p>

<p><strong>Recommandations</strong> :</p>
<ul>
<li>Continuer la pratique (home lab avec vieux routeurs ou VMs)</li>
<li>Se former sur automatisation (Python pour reseaux)</li>
<li>Explorer SDN (controleurs OpenDaylight, ONOS)</li>
<li>Suivre l'actualite (RFCs, blogs techniques, conferences)</li>
<li>Envisager certifications (CCNA, CCNP, ou equivalents autres vendors)</li>
</ul>

<p><strong>Liens avec les autres cours</strong> :</p>
<ul>
<li><a href="./reseau-s5.html">Reseau - S5</a> : bases TCP/IP</li>
<li><a href="./cloud-edge.html">Cloud et Edge Computing - S9</a> : reseaux virtuels</li>
<li><a href="./embedded-ia-iot.html">Embedded IA for IoT - S9</a> : connectivite objets</li>
<li><a href="./temps-reel.html">Temps Reel - S8</a> : contraintes temporelles</li>
</ul>

<hr/>

<p><em>Cours suivi en 2023-2024 a l'INSA Toulouse, Departement Genie Electrique et Informatique.</em></p>

</div>

<div class="lang-en">

<h1>Network Interconnection - Semester 8</h1>

<p><strong>Academic Year</strong>: 2023-2024<br/>
<strong>ECTS</strong>: 2.5<br/>
<strong>Category</strong>: Networks and Telecommunications</p>

<hr/>

<h2>PART A - General Module Overview</h2>

<h3 class="section-title">Overview</h3>

<p>This course delves into the concepts and protocols enabling the interconnection of heterogeneous networks to form the global Internet. It covers IP routing, TCP and UDP transport protocols, quality of service, VLANs, network security, and modern architectures. The goal is to train engineers capable of designing, deploying, and administering complex network infrastructures.</p>

<p><strong>Learning Objectives</strong>:</p>
<ul>
<li>Master TCP/IP protocols and the layered model</li>
<li>Configure and administer Cisco routers and switches</li>
<li>Implement dynamic routing protocols (RIP, OSPF, BGP)</li>
<li>Design multi-site network architectures</li>
<li>Implement Quality of Service (QoS)</li>
<li>Segment networks with VLANs</li>
<li>Secure infrastructures (ACL, VPN, firewall)</li>
<li>Diagnose and resolve network issues</li>
</ul>

<h3 class="section-title">Position in the Curriculum</h3>

<p>This module builds on previously acquired foundations:</p>
<ul>
<li><strong>Networking (S5)</strong>: OSI model, Ethernet, basic IP, TCP/UDP</li>
<li><strong>Hardware Architecture (S6)</strong>: physical layer, signals</li>
<li><strong>Operating Systems (S5)</strong>: sockets, inter-process communication</li>
</ul>

<p>It prepares for:</p>
<ul>
<li><strong>Cloud and Edge Computing (S9)</strong>: virtual networks, SDN</li>
<li><strong>IoT (S9)</strong>: specific protocols, network constraints</li>
<li><strong>Cybersecurity</strong>: advanced network security</li>
<li><strong>Professional career</strong>: network administration, infrastructure architect</li>
</ul>

<hr/>

<h2>PART B - Personal Experience and Learning Context</h2>

<h3 class="section-title">Organization and Resources</h3>

<p>The module combined theory with intensive hands-on practice:</p>

<p><strong>Lectures (15h)</strong>:</p>
<ul>
<li>OSI and TCP/IP models, encapsulation</li>
<li>IPv4 and IPv6 addressing, subnetting</li>
<li>Routing protocols (static, RIP, OSPF, BGP)</li>
<li>TCP and UDP in detail</li>
<li>Quality of Service (QoS)</li>
<li>VLANs and switching</li>
<li>Network security (ACL, VPN, firewall)</li>
<li>NAT and address translation</li>
</ul>

<p><strong>Tutorials (6h)</strong>:</p>
<ul>
<li>Subnetting calculations</li>
<li>Network architecture design</li>
<li>Protocol analysis</li>
<li>Routing configuration</li>
</ul>

<p><strong>Lab Work (12h)</strong>:</p>
<ul>
<li><strong>Lab 1</strong>: Basic Cisco router configuration, static routing</li>
<li><strong>Lab 2</strong>: Dynamic routing protocols (RIP, OSPF)</li>
<li><strong>Lab 3</strong>: VLANs, inter-VLAN routing, ACLs</li>
</ul>

<p><strong>Tools Used</strong>:</p>
<ul>
<li><strong>Cisco Packet Tracer</strong>: network simulation</li>
<li><strong>GNS3</strong>: network equipment emulation</li>
<li><strong>Cisco Equipment</strong>: physical routers and switches</li>
<li><strong>Wireshark</strong>: traffic capture and analysis</li>
<li><strong>Cisco IOS</strong>: router/switch operating system</li>
</ul>

<p><strong>Resources</strong>:</p>
<ul>
<li>Complete course handout (4AE-Interconnexion-Rzo)</li>
<li>Tutorials with practical exercises</li>
<li>3 guided labs with configurations</li>
<li>Cisco documentation</li>
<li>Protocol RFCs (TCP, IP, OSPF, BGP)</li>
</ul>

<h3 class="section-title">Study Methodology</h3>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S8/interconnexion-reseau/modele-osi.svg" alt="OSI 7-layer model"
       style="max-width: 500px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: 7-layer OSI model with protocols and encapsulation</p>
</div>

<p><strong>Phase 1: Master the fundamentals</strong>:
Review the layered model, IP addressing, and routing principles.</p>

<p><strong>Phase 2: Deepen protocol knowledge</strong>:
Study TCP, UDP, OSPF, and BGP in detail with their internal mechanisms.</p>

<p><strong>Phase 3: Practice configuration</strong>:
Use Packet Tracer to configure network scenarios of increasing complexity.</p>

<p><strong>Phase 4: Analyze traffic</strong>:
Capture with Wireshark to observe real protocol exchanges.</p>

<p><strong>Phase 5: Develop troubleshooting skills</strong>:
Diagnose network failures using a methodical approach (bottom-up or top-down through the OSI model).</p>

<h3 class="section-title">Challenges Encountered</h3>

<p><strong>Protocol complexity</strong>:
OSPF and BGP are feature-rich protocols with many parameters and edge cases.</p>

<p><strong>Cisco IOS syntax</strong>:
The Cisco command line has its own logic and specific commands to memorize.</p>

<p><strong>Network debugging</strong>:
Identifying the source of a problem in a complex network requires methodology and patience.</p>

<p><strong>Abstraction vs. reality</strong>:
Simulations are simplified. Real networks have physical constraints, latency, and random failures.</p>

<hr/>

<h2>PART C - Detailed Technical Aspects</h2>

<h3 class="section-title">1. Network Reference Models</h3>

<p><strong>OSI Model (7 layers)</strong>:</p>

<p>Theoretical reference model for network architecture.</p>

<table>
<tr><th>Layer</th><th>Name</th><th>Role</th><th>Examples</th></tr>
<tr><td>7</td><td>Application</td><td>Application services</td><td>HTTP, FTP, DNS, SMTP</td></tr>
<tr><td>6</td><td>Presentation</td><td>Format, encryption, compression</td><td>SSL/TLS, JPEG, MPEG</td></tr>
<tr><td>5</td><td>Session</td><td>Session management</td><td>NetBIOS, RPC</td></tr>
<tr><td>4</td><td>Transport</td><td>End-to-end transmission</td><td>TCP, UDP</td></tr>
<tr><td>3</td><td>Network</td><td>Routing, logical addressing</td><td>IP, ICMP, OSPF, BGP</td></tr>
<tr><td>2</td><td>Data Link</td><td>Transmission over physical link, MAC addressing</td><td>Ethernet, WiFi, PPP</td></tr>
<tr><td>1</td><td>Physical</td><td>Bit transmission (electrical, optical signals)</td><td>Cables, radio waves</td></tr>
</table>

<p><strong>TCP/IP Model (4 layers)</strong>:</p>

<p>Practical model used on the Internet.</p>

<table>
<tr><th>Layer</th><th>OSI Equivalent</th><th>Main Protocols</th></tr>
<tr><td>Application</td><td>5-6-7</td><td>HTTP, FTP, DNS, SMTP, SSH</td></tr>
<tr><td>Transport</td><td>4</td><td>TCP, UDP</td></tr>
<tr><td>Internet</td><td>3</td><td>IP, ICMP, ARP</td></tr>
<tr><td>Network Access</td><td>1-2</td><td>Ethernet, WiFi</td></tr>
</table>

<p><strong>Encapsulation</strong>:</p>

<p>Each layer adds its header to the data from the layer above.</p>

<p>Application data &rarr; TCP Segment &rarr; IP Packet &rarr; Ethernet Frame</p>

<p><strong>Decapsulation</strong>:</p>

<p>The receiver strips headers layer by layer to extract the data.</p>

<h3 class="section-title">2. IPv4 Addressing</h3>

<p><strong>Format</strong>:</p>

<p>32-bit address, written as 4 decimal octets separated by dots.</p>

<p>Example: 192.168.1.10</p>

<p><strong>Historical classes (obsolete)</strong>:</p>

<p>Replaced by CIDR, but useful for understanding the evolution.</p>

<ul>
<li>Class A: first bit = 0, network on 8 bits (large networks)</li>
<li>Class B: first bits = 10, network on 16 bits</li>
<li>Class C: first bits = 110, network on 24 bits</li>
</ul>

<p><strong>CIDR (Classless Inter-Domain Routing)</strong>:</p>

<p>Flexible notation: IP address / network prefix length</p>

<p>Example: 192.168.10.0/24 means network on 24 bits, 8 bits for hosts (256 addresses).</p>

<p><strong>Subnet mask</strong>:</p>

<p>Determines which part of the address is the network and which part is the host.</p>

<p>/24 corresponds to the mask 255.255.255.0</p>

<p><strong>Special addresses</strong>:</p>

<ul>
<li><strong>Network address</strong>: all host bits set to 0 (e.g., 192.168.1.0)</li>
<li><strong>Broadcast address</strong>: all host bits set to 1 (e.g., 192.168.1.255)</li>
<li><strong>Loopback</strong>: 127.0.0.1 (local loopback interface)</li>
<li><strong>Private ranges (RFC 1918)</strong>: not routable on the Internet
  <ul>
  <li>10.0.0.0/8</li>
  <li>172.16.0.0/12</li>
  <li>192.168.0.0/16</li>
  </ul>
</li>
</ul>

<p><strong>Subnetting</strong>:</p>

<p>Dividing a network into smaller subnetworks to optimize address usage and segment the network.</p>

<p>Example: 192.168.1.0/24 divided into 4 /26 subnets:</p>
<ul>
<li>192.168.1.0/26 (addresses .0 to .63)</li>
<li>192.168.1.64/26 (addresses .64 to .127)</li>
<li>192.168.1.128/26 (addresses .128 to .191)</li>
<li>192.168.1.192/26 (addresses .192 to .255)</li>
</ul>

<h3 class="section-title">3. IPv6</h3>

<p><strong>Motivation</strong>:</p>

<p>Exhaustion of public IPv4 addresses. IPv6 offers a virtually unlimited address space.</p>

<p><strong>Format</strong>:</p>

<p>128-bit address, written as 8 groups of 4 hexadecimal digits separated by colons.</p>

<p>Example: 2001:0db8:85a3:0000:0000:8a2e:0370:7334</p>

<p><strong>Notation shortcuts</strong>:</p>

<ul>
<li>Omit leading zeros in each group: 2001:db8:85a3:0:0:8a2e:370:7334</li>
<li>Replace a sequence of consecutive zero groups with :: (only once): 2001:db8:85a3::8a2e:370:7334</li>
</ul>

<p><strong>Advantages</strong>:</p>

<ul>
<li>Immense address space (2 to the power of 128 addresses)</li>
<li>Simplified autoconfiguration (SLAAC)</li>
<li>Native built-in IPsec</li>
<li>Simplified header (better performance)</li>
<li>No need for NAT</li>
</ul>

<p><strong>Address types</strong>:</p>

<ul>
<li><strong>Unicast</strong>: unique address identifying one interface</li>
<li><strong>Multicast</strong>: group of interfaces (replaces broadcast)</li>
<li><strong>Anycast</strong>: group of interfaces, routed to the nearest one</li>
</ul>

<p><strong>Special addresses</strong>:</p>

<ul>
<li><strong>Loopback</strong>: ::1</li>
<li><strong>Link-local</strong>: fe80::/10 (auto-configured, local link communication)</li>
<li><strong>Unique local</strong>: fc00::/7 (equivalent of IPv4 private addresses)</li>
<li><strong>Global unicast</strong>: 2000::/3 (routable on the Internet)</li>
</ul>

<h3 class="section-title">4. Routing - Fundamental Principles</h3>

<p><strong>Role of the router</strong>:</p>

<p>Forward IP packets between different networks by consulting its routing table.</p>

<p><strong>Routing table</strong>:</p>

<p>Contains routes to destination networks.</p>

<p>Each entry specifies:</p>
<ul>
<li><strong>Destination network</strong> with mask</li>
<li><strong>Gateway (next hop)</strong>: IP address of the next router or "directly connected"</li>
<li><strong>Outgoing interface</strong>: which interface to send the packet through</li>
<li><strong>Metric</strong>: route cost (distance, bandwidth, etc.)</li>
</ul>

<p><strong>Routing process</strong>:</p>

<ol>
<li>Receive IP packet</li>
<li>Consult routing table to find the best route (longest prefix match)</li>
<li>Decrement TTL (Time To Live)</li>
<li>Recalculate IP header checksum</li>
<li>Forward packet on the appropriate outgoing interface</li>
</ol>

<p><strong>Default route</strong>:</p>

<p>Route 0.0.0.0/0 used when no specific route matches. Typically towards the Internet via the ISP gateway.</p>

<p><strong>Static vs. dynamic routing</strong>:</p>

<ul>
<li><strong>Static</strong>: manually configured routes, suitable for small networks or specific routes</li>
<li><strong>Dynamic</strong>: routing protocols automate route discovery and updates</li>
</ul>

<h3 class="section-title">5. Dynamic Routing Protocols</h3>

<p><strong>Classification</strong>:</p>

<p><strong>IGP (Interior Gateway Protocol)</strong>: within an autonomous system (AS)</p>
<ul>
<li><strong>Distance vector</strong>: RIP, EIGRP</li>
<li><strong>Link state</strong>: OSPF, IS-IS</li>
</ul>

<p><strong>EGP (Exterior Gateway Protocol)</strong>: between autonomous systems</p>
<ul>
<li><strong>Path vector</strong>: BGP</li>
</ul>

<p><strong>RIP (Routing Information Protocol)</strong>:</p>

<p>Simple distance-vector routing protocol.</p>

<p><strong>Characteristics</strong>:</p>
<ul>
<li>Metric: hop count, maximum 15</li>
<li>Bellman-Ford algorithm</li>
<li>Full table update every 30 seconds</li>
<li>Slow convergence</li>
<li>Simple but limited to small networks</li>
</ul>

<p><strong>OSPF (Open Shortest Path First)</strong>:</p>

<p>Advanced link-state protocol.</p>

<p><strong>Principle</strong>:</p>
<ul>
<li>Each router knows the complete topology of the area</li>
<li>SPF algorithm (Dijkstra) calculates the shortest path tree</li>
<li>Metric based on cost (function of bandwidth)</li>
</ul>

<p><strong>Operation</strong>:</p>
<ol>
<li>Neighbor discovery via Hello packets</li>
<li>Exchange of LSAs (Link State Advertisements) describing links</li>
<li>Construction of the topological database (LSDB)</li>
<li>SPF calculation to determine best routes</li>
<li>Installation of routes in the routing table</li>
</ol>

<p><strong>Advantages</strong>:</p>
<ul>
<li>Fast convergence (triggered updates, not periodic)</li>
<li>Scalability through hierarchy (areas)</li>
<li>Supports VLSM and CIDR</li>
<li>Update authentication</li>
</ul>

<p><strong>OSPF Hierarchy</strong>:</p>

<p>Organized into areas to reduce traffic and table size.</p>

<ul>
<li><strong>Area 0 (backbone)</strong>: mandatory central area</li>
<li><strong>Non-backbone areas</strong>: connected to area 0 via ABR (Area Border Router)</li>
</ul>

<p><strong>BGP (Border Gateway Protocol)</strong>:</p>

<p>Internet routing protocol between autonomous systems.</p>

<p><strong>Characteristics</strong>:</p>
<ul>
<li>Path vector: includes the complete AS path</li>
<li>Complex routing policies (business, preferences)</li>
<li>eBGP (external) between different ASes, iBGP (internal) within an AS</li>
<li>Metric: not only technical but also policy-based</li>
</ul>

<p><strong>Role</strong>:</p>

<p>BGP maintains the global Internet routing table. Each AS announces its IP prefixes.</p>

<h3 class="section-title">6. TCP (Transmission Control Protocol)</h3>

<p><strong>Characteristics</strong>:</p>

<p>Connection-oriented, reliable transport protocol.</p>

<ul>
<li><strong>Connection-oriented</strong>: 3-way handshake establishment before data exchange</li>
<li><strong>Reliable</strong>: acknowledgments, retransmission of lost segments</li>
<li><strong>Order preserved</strong>: sequence numbers guarantee ordering</li>
<li><strong>Flow control</strong>: sliding window prevents receiver overflow</li>
<li><strong>Congestion control</strong>: adapts throughput based on network state</li>
</ul>

<p><strong>TCP Header (main fields)</strong>:</p>

<ul>
<li><strong>Source and destination ports</strong> (16 bits each): identify applications</li>
<li><strong>Sequence number</strong> (32 bits): position of data in the stream</li>
<li><strong>Acknowledgment number</strong> (32 bits): next expected byte</li>
<li><strong>Flags</strong>: SYN (synchronization), ACK (acknowledgment), FIN (finish), RST (reset), PSH (push), URG (urgent)</li>
<li><strong>Window</strong> (16 bits): available receiver buffer size (flow control)</li>
<li><strong>Checksum</strong> (16 bits): error detection</li>
</ul>

<p><strong>Connection establishment (3-way handshake)</strong>:</p>

<ol>
<li><strong>Client &rarr; Server: SYN</strong> (synchronization, initial sequence number)</li>
<li><strong>Server &rarr; Client: SYN+ACK</strong> (acknowledgment + its own sequence number)</li>
<li><strong>Client &rarr; Server: ACK</strong> (final acknowledgment)</li>
</ol>

<p>Connection established, data exchange can begin.</p>

<p><strong>Connection teardown (4-way handshake)</strong>:</p>

<ol>
<li><strong>A &rarr; B: FIN</strong> (A has finished sending)</li>
<li><strong>B &rarr; A: ACK</strong> (acknowledgment)</li>
<li><strong>B &rarr; A: FIN</strong> (B has finished sending)</li>
<li><strong>A &rarr; B: ACK</strong> (final acknowledgment)</li>
</ol>

<p>Or abrupt closure with RST (reset).</p>

<p><strong>Flow control (sliding window)</strong>:</p>

<p>The receiver advertises the size of its available buffer (window).</p>

<p>The sender cannot send more data than the window size.</p>

<p>Prevents receiver buffer overflow.</p>

<p><strong>Congestion control</strong>:</p>

<p>Mechanism to adapt throughput based on network state and prevent collapse.</p>

<p><strong>Phases</strong>:</p>
<ul>
<li><strong>Slow Start</strong>: exponential increase of the congestion window</li>
<li><strong>Congestion Avoidance</strong>: linear increase after reaching a threshold</li>
<li><strong>Fast Retransmit</strong>: immediate retransmission after 3 duplicate ACKs</li>
<li><strong>Fast Recovery</strong>: moderate window reduction after loss</li>
</ul>

<p><strong>Algorithms</strong>: TCP Tahoe, Reno, New Reno, CUBIC (used by Linux by default).</p>

<h3 class="section-title">7. UDP (User Datagram Protocol)</h3>

<p><strong>Characteristics</strong>:</p>

<p>Simple, connectionless, unreliable transport protocol.</p>

<ul>
<li><strong>Connectionless</strong>: no connection establishment</li>
<li><strong>Unreliable</strong>: no acknowledgment, no retransmission</li>
<li><strong>No flow or congestion control</strong></li>
<li><strong>No ordering guarantee</strong></li>
<li><strong>Minimal header</strong>: only 8 bytes</li>
</ul>

<p><strong>UDP Header</strong>:</p>

<ul>
<li>Source port (16 bits)</li>
<li>Destination port (16 bits)</li>
<li>Length (16 bits)</li>
<li>Checksum (16 bits)</li>
</ul>

<p><strong>Use cases</strong>:</p>

<p>Applications where speed takes priority over reliability:</p>
<ul>
<li><strong>VoIP and video conferencing</strong>: real-time, acceptable loss</li>
<li><strong>Video/audio streaming</strong>: retransmission pointless (already too late)</li>
<li><strong>DNS</strong>: short queries, retransmission handled by the application</li>
<li><strong>DHCP</strong>: initial network configuration</li>
<li><strong>Online gaming</strong>: critical latency</li>
<li><strong>SNMP</strong>: simple network management</li>
</ul>

<p><strong>Advantages</strong>:</p>

<p>Low overhead, minimal latency, suited for real-time applications.</p>

<h3 class="section-title">8. Quality of Service (QoS)</h3>

<p><strong>Problem statement</strong>:</p>

<p>The Internet is a "best-effort" network: no guarantees of bandwidth, latency, or reliability.</p>

<p>Insufficient for demanding applications: VoIP (voice), video conferencing, streaming.</p>

<p><strong>QoS Parameters</strong>:</p>

<table>
<tr><th>Parameter</th><th>Description</th><th>Important for</th></tr>
<tr><td>Bandwidth</td><td>Guaranteed throughput</td><td>Video streaming</td></tr>
<tr><td>Latency</td><td>Transit delay</td><td>VoIP, gaming</td></tr>
<tr><td>Jitter</td><td>Latency variation</td><td>VoIP, video</td></tr>
<tr><td>Packet loss</td><td>Rate of lost packets</td><td>All applications</td></tr>
</table>

<p><strong>QoS Mechanisms</strong>:</p>

<p><strong>Classification and marking</strong>:</p>

<p>Identify traffic type and mark it in the header for differentiated treatment.</p>

<ul>
<li><strong>DSCP (Differentiated Services Code Point)</strong>: 6 bits in the IP header</li>
<li><strong>CoS (Class of Service)</strong>: 3 bits in the 802.1Q tag (VLAN)</li>
</ul>

<p><strong>Queuing</strong>:</p>

<p>Manage priorities and packet scheduling.</p>

<ul>
<li><strong>FIFO</strong>: First In First Out (no priority)</li>
<li><strong>Priority Queuing</strong>: queues with different priorities (strict)</li>
<li><strong>WFQ (Weighted Fair Queuing)</strong>: fair sharing with weighting</li>
<li><strong>CBWFQ (Class-Based WFQ)</strong>: WFQ per traffic class</li>
<li><strong>LLQ (Low Latency Queuing)</strong>: priority queue + WFQ for the rest</li>
</ul>

<p><strong>Policing and Shaping</strong>:</p>

<p>Control traffic rate.</p>

<ul>
<li><strong>Policing</strong>: limit throughput, drop or remark excess</li>
<li><strong>Shaping</strong>: smooth traffic, buffer excess in a queue</li>
</ul>

<p><strong>QoS Models</strong>:</p>

<ul>
<li><strong>IntServ (Integrated Services)</strong>: per-flow resource reservation (RSVP), rarely deployed (complexity)</li>
<li><strong>DiffServ (Differentiated Services)</strong>: aggregated service classes, scalable, widely deployed</li>
</ul>

<h3 class="section-title">9. VLANs (Virtual LANs)</h3>

<p><strong>Principle</strong>:</p>

<p>Segment a physical network into multiple isolated logical networks.</p>

<p><strong>Advantages</strong>:</p>

<ul>
<li><strong>Broadcast domain isolation</strong>: reduces unnecessary traffic</li>
<li><strong>Security</strong>: logical traffic separation (finance, HR, guests)</li>
<li><strong>Flexibility</strong>: reorganization without physical recabling</li>
<li><strong>Optimization</strong>: group users by function rather than by location</li>
</ul>

<p><strong>802.1Q Standard (VLAN Tagging)</strong>:</p>

<p>Addition of a 4-byte tag in the Ethernet frame containing:</p>
<ul>
<li><strong>VLAN ID</strong> (12 bits): VLAN identifier (4096 VLANs possible)</li>
<li><strong>Priority</strong> (3 bits): CoS priority for QoS</li>
</ul>

<p><strong>Port types</strong>:</p>

<table>
<tr><th>Type</th><th>Description</th><th>Usage</th></tr>
<tr><td>Access</td><td>Belongs to a single VLAN, no tag</td><td>End-device connection</td></tr>
<tr><td>Trunk</td><td>Carries multiple VLANs, with tags</td><td>Switch interconnection</td></tr>
</table>

<p><strong>Inter-VLAN communication</strong>:</p>

<p>VLANs are isolated. To communicate between them, a router (or layer 3 switch) is needed.</p>

<p>Methods:</p>
<ul>
<li><strong>Router on a stick</strong>: single physical link, sub-interfaces per VLAN</li>
<li><strong>L3 Switch</strong>: inter-VLAN routing directly on the switch</li>
</ul>

<h3 class="section-title">10. Switching</h3>

<p><strong>Principle</strong>:</p>

<p>A switch forwards Ethernet frames based on MAC addresses.</p>

<p><strong>CAM Table (Content Addressable Memory)</strong>:</p>

<p>Associates MAC addresses with switch ports.</p>

<p><strong>Learning</strong>:</p>

<p>The switch learns MAC addresses by observing the source address of received frames.</p>

<p><strong>Forwarding</strong>:</p>

<ul>
<li><strong>Known destination address</strong>: forward on the associated port in the CAM table</li>
<li><strong>Unknown address</strong>: flood (broadcast) on all ports except the receiving one</li>
<li><strong>Broadcast or multicast</strong>: flood</li>
</ul>

<p><strong>Spanning Tree Protocol (STP)</strong>:</p>

<p>Protocol to prevent loops in redundant topologies (multiple links between switches).</p>

<p><strong>Operation</strong>:</p>
<ol>
<li>Election of a root bridge</li>
<li>Calculation of the optimal path to the root bridge</li>
<li>Blocking ports that create loops</li>
<li>Automatic reconfiguration in case of failure</li>
</ol>

<p><strong>Variants</strong>: RSTP (Rapid STP) for faster convergence, MSTP (Multiple STP) for multiple VLANs.</p>

<h3 class="section-title">11. NAT (Network Address Translation)</h3>

<p><strong>Problem statement</strong>:</p>

<p>Shortage of public IPv4 addresses. Not all machines can have a public address.</p>

<p><strong>Principle</strong>:</p>

<p>Translate private IP addresses to public addresses when crossing a router.</p>

<p><strong>Types of NAT</strong>:</p>

<p><strong>Static NAT</strong>:</p>

<p>Fixed 1:1 mapping between a private address and a public address.</p>

<p>Usage: servers accessible from the Internet.</p>

<p><strong>Dynamic NAT</strong>:</p>

<p>Pool of public addresses, dynamic allocation to internal machines.</p>

<p><strong>PAT (Port Address Translation) or NAT Overload</strong>:</p>

<p>Multiple internal machines share a single public address.</p>

<p>Differentiation by port numbers.</p>

<p>NAT table associates: private IP:private port &harr; public IP:public port</p>

<p><strong>Usage</strong>: most home routers (all domestic devices share the public IP).</p>

<p><strong>NAT Limitations</strong>:</p>

<ul>
<li>Breaks end-to-end connectivity</li>
<li>Issues for protocols embedding IP addresses in data (FTP, SIP)</li>
<li>Difficulties for P2P applications and inbound servers</li>
<li>Requires traversal techniques (STUN, TURN) for VoIP</li>
</ul>

<p><strong>IPv6 and NAT</strong>:</p>

<p>IPv6 makes NAT unnecessary (sufficient addresses for all). Return to end-to-end connectivity.</p>

<h3 class="section-title">12. Network Security</h3>

<p><strong>Access Control Lists (ACL)</strong>:</p>

<p>Filter traffic based on defined criteria (IP addresses, ports, protocols).</p>

<p><strong>Types</strong>:</p>
<ul>
<li><strong>Standard ACL</strong>: filters only on source IP address</li>
<li><strong>Extended ACL</strong>: filters on source/destination IP, ports, protocols</li>
</ul>

<p><strong>Application</strong>: on router interfaces (inbound or outbound traffic).</p>

<p><strong>Firewall</strong>:</p>

<p>Device or software that filters traffic in a more sophisticated manner.</p>

<p><strong>Features</strong>:</p>
<ul>
<li>Stateful filtering (connection state inspection)</li>
<li>Application filtering (deep packet inspection)</li>
<li>Intrusion prevention (IPS)</li>
<li>Logging and alerts</li>
</ul>

<p><strong>VPN (Virtual Private Network)</strong>:</p>

<p>Create a secure tunnel through an unsecured network (Internet).</p>

<p><strong>Types</strong>:</p>
<ul>
<li><strong>Site-to-Site</strong>: interconnect remote sites of a company</li>
<li><strong>Remote Access</strong>: enable secure remote access (teleworking)</li>
</ul>

<p><strong>Protocols</strong>:</p>
<ul>
<li><strong>IPsec</strong>: IP-level encryption (tunnel or transport mode)</li>
<li><strong>SSL/TLS VPN</strong>: HTTPS-based, simpler for remote access</li>
</ul>

<p><strong>Common threats</strong>:</p>

<table>
<tr><th>Threat</th><th>Description</th><th>Countermeasure</th></tr>
<tr><td>DoS/DDoS</td><td>Resource saturation</td><td>Filtering, rate limiting, CDN</td></tr>
<tr><td>Spoofing</td><td>IP address impersonation</td><td>Ingress/egress filtering, authentication</td></tr>
<tr><td>Man-in-the-Middle</td><td>Communication interception</td><td>Encryption (TLS, IPsec)</td></tr>
<tr><td>ARP poisoning</td><td>ARP table corruption</td><td>Dynamic ARP Inspection</td></tr>
<tr><td>VLAN hopping</td><td>Unauthorized VLAN access</td><td>Secure trunk/access configuration</td></tr>
</table>

<p><strong>Best practices</strong>:</p>

<ul>
<li>Defense in depth (multiple security layers)</li>
<li>Principle of least privilege</li>
<li>Network segmentation (VLANs, DMZ zones)</li>
<li>Regular updates (firmware, patches)</li>
<li>Monitoring and detection (IDS, SIEM)</li>
<li>Configuration backups</li>
</ul>

<hr/>

<h2>PART D - Reflective Analysis and Perspectives</h2>

<h3 class="section-title">Skills Acquired</h3>

<p><strong>In-depth TCP/IP understanding</strong>:
Mastery of the fundamental Internet protocols and their internal operation.</p>

<p><strong>Network equipment configuration</strong>:
Ability to configure Cisco routers and switches via the command line interface (CLI).</p>

<p><strong>Network architecture design</strong>:
Ability to design multi-site infrastructures with routing, VLANs, and QoS.</p>

<p><strong>Methodical troubleshooting</strong>:
Competence in diagnosing and resolving network issues following the layered model.</p>

<p><strong>Infrastructure security</strong>:
Ability to implement ACLs, VPN, and segmentation to secure a network.</p>

<h3 class="section-title">Key Takeaways</h3>

<p><strong>1. The layered model is fundamental</strong>:
Understanding encapsulation and the role of each layer enables effective problem diagnosis.</p>

<p><strong>2. OSPF is the modern IGP protocol</strong>:
RIP is obsolete for networks of significant size. OSPF offers scalability and fast convergence.</p>

<p><strong>3. TCP provides reliability, UDP provides speed</strong>:
Choose the right transport protocol according to the application's needs.</p>

<p><strong>4. QoS is crucial for real-time</strong>:
VoIP and video require priority and guarantees to function properly.</p>

<p><strong>5. VLANs = effective logical segmentation</strong>:
Organizing the network into VLANs improves security, performance, and management.</p>

<h3 class="section-title">Feedback</h3>

<p><strong>Educational aspect</strong>:
The labs on Cisco equipment gave a concrete dimension to the theory. Seeing routes appear in the table after configuring OSPF is satisfying.</p>

<p><strong>Cisco IOS complexity</strong>:
The Cisco CLI has a learning curve. The modes (user, privileged, configuration) and command hierarchy require practice.</p>

<p><strong>Importance of troubleshooting</strong>:
Configurations do not always work on the first try. Learning to diagnose methodically (ping, traceroute, show commands) is essential.</p>

<p><strong>Robust protocols</strong>:
TCP and OSPF are engineering marvels. Their robustness in the face of failures and congestion is impressive.</p>

<h3 class="section-title">Practical Applications</h3>

<p><strong>For network administrators</strong>:</p>
<ul>
<li>Deploy and maintain enterprise network infrastructures</li>
<li>Configure routers and switches</li>
<li>Implement redundancy and high availability</li>
<li>Ensure security and QoS</li>
</ul>

<p><strong>For network architects</strong>:</p>
<ul>
<li>Design multi-site architectures</li>
<li>Size bandwidth</li>
<li>Choose equipment and protocols</li>
<li>Plan evolution and scalability</li>
</ul>

<p><strong>For DevOps engineers</strong>:</p>
<ul>
<li>Understand cloud networks (VPC, subnets, routing tables)</li>
<li>Automate network configurations (Ansible, Terraform)</li>
<li>Optimize distributed application performance</li>
<li>Implement load balancers</li>
</ul>

<p><strong>For developers</strong>:</p>
<ul>
<li>Understand network latency and its impact on applications</li>
<li>Choose appropriate protocols (TCP vs UDP)</li>
<li>Implement retry logic and timeouts</li>
<li>Optimize for WAN (compression, caching)</li>
</ul>

<h3 class="section-title">Limitations and Openings</h3>

<p><strong>Module limitations</strong>:</p>
<ul>
<li>Focus on Cisco (market is more diverse: Juniper, Arista, etc.)</li>
<li>Little on IPv6 (inevitable transition)</li>
<li>No SDN (Software-Defined Networking)</li>
<li>Automation barely covered</li>
</ul>

<p><strong>Openings towards</strong>:</p>
<ul>
<li><strong>SDN and NFV</strong>: network virtualization, OpenFlow, controllers</li>
<li><strong>Cloud networking</strong>: AWS VPC, Azure Virtual Networks</li>
<li><strong>Automation</strong>: Ansible, Python with Netmiko/NAPALM</li>
<li><strong>Monitoring</strong>: SNMP, NetFlow, observability</li>
<li><strong>5G and mobile networks</strong>: architecture, slicing</li>
</ul>

<h3 class="section-title">Recent Developments</h3>

<p><strong>Software-Defined Networking (SDN)</strong>:</p>

<p>Separation of the control plane (routing decisions) from the data plane (forwarding).</p>

<p>Centralized controller programmable via API.</p>

<p><strong>Network Functions Virtualization (NFV)</strong>:</p>

<p>Network functions (firewall, load balancer) in software rather than dedicated hardware.</p>

<p>Flexibility and cost reduction.</p>

<p><strong>Intent-Based Networking</strong>:</p>

<p>Define the intent (policy) rather than detailed configuration.</p>

<p>The system automatically translates intent into configuration.</p>

<p><strong>Automation and Infrastructure as Code</strong>:</p>

<p>Network configuration declared in files (Ansible, Terraform).</p>

<p>Versioning, reproducibility, scalability.</p>

<p><strong>5G Networks</strong>:</p>

<p>Ultra-low latency, high throughput, slicing (dedicated virtual networks per use case).</p>

<h3 class="section-title">Tips for Success</h3>

<p><strong>1. Practice regularly</strong>:
Use Packet Tracer or GNS3 to reproduce scenarios and experiment with configurations.</p>

<p><strong>2. Understand, do not memorize</strong>:
Understand how protocols work rather than memorizing CLI syntax.</p>

<p><strong>3. Document your configurations</strong>:
Take notes on commands and deployed architectures. Build a personal reference.</p>

<p><strong>4. Use Wireshark</strong>:
Capture and analyze real traffic to see protocols in action.</p>

<p><strong>5. Follow the troubleshooting methodology</strong>:
Bottom-up (layer 1 &rarr; 7) or top-down depending on symptoms. Methodical and systematic.</p>

<p><strong>6. Get certified</strong>:
Cisco CCNA is a recognized certification validating basic networking skills.</p>

<h3 class="section-title">Conclusion</h3>

<p>This module is essential for any engineer working with connected systems. Networks are ubiquitous: enterprises, data centers, cloud, IoT, telecommunications.</p>

<p><strong>Transferable skills</strong>:</p>
<ul>
<li>Global vision of network architectures</li>
<li>Ability to diagnose and resolve complex problems</li>
<li>Understanding of tradeoffs (performance, security, cost)</li>
<li>Mastery of universal protocols (TCP/IP)</li>
</ul>

<p><strong>Professional relevance</strong>:
Networking skills are sought after in all sectors. The explosion of cloud, IoT, and distributed applications increases the demand for qualified network engineers.</p>

<p><strong>Key message</strong>:
The Internet works thanks to robust protocols and competent engineers. Understanding these fundamentals enables the design, deployment, and maintenance of reliable and high-performance infrastructures.</p>

<p><strong>Recommendations</strong>:</p>
<ul>
<li>Continue practicing (home lab with old routers or VMs)</li>
<li>Train on automation (Python for networks)</li>
<li>Explore SDN (OpenDaylight, ONOS controllers)</li>
<li>Stay current (RFCs, technical blogs, conferences)</li>
<li>Consider certifications (CCNA, CCNP, or equivalents from other vendors)</li>
</ul>

<p><strong>Links with other courses</strong>:</p>
<ul>
<li><a href="./reseau-s5.html">Networking - S5</a>: TCP/IP foundations</li>
<li><a href="./cloud-edge.html">Cloud and Edge Computing - S9</a>: virtual networks</li>
<li><a href="./embedded-ia-iot.html">Embedded IA for IoT - S9</a>: object connectivity</li>
<li><a href="./temps-reel.html">Real-Time Systems - S8</a>: temporal constraints</li>
</ul>

<hr/>

<p><em>Course taken in 2023-2024 at INSA Toulouse, Department of Electrical and Computer Engineering.</em></p>

</div>

<div class="back-nav">
    <a href="./my-courses-2023-2024.html" data-i18n-html="back-courses-2023-2024">&larr; Retour aux Cours 2023-2024</a>
</div>

<hr/>

<div style="text-align: center;">
    <h2>
        <span class="lang-fr">Documents de Cours</span>
        <span class="lang-en">Course Documents</span>
    </h2>
</div>

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
      <h4>
        <span class="lang-fr">Cours Complet Interconnexion Reseaux</span>
        <span class="lang-en">Complete Network Interconnection Course</span>
      </h4>
      <p>
        <span class="lang-fr">Cours complet sur les architectures reseaux : routage, protocoles (RIP, OSPF, BGP), VLAN, qualite de service.</span>
        <span class="lang-en">Complete course on network architectures: routing, protocols (RIP, OSPF, BGP), VLAN, quality of service.</span>
      </p>
      <embed src="/cours-pdf/S8/Interconnexion-Reseau/cours-complet.pdf" type="application/pdf" width="100%" height="800px" />
      <p>
        <span class="lang-fr"><a href="/cours-pdf/S8/Interconnexion-Reseau/cours-complet.pdf" target="_blank">Telecharger</a></span>
        <span class="lang-en"><a href="/cours-pdf/S8/Interconnexion-Reseau/cours-complet.pdf" target="_blank">Download</a></span>
      </p>
    </div>
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">Travaux Diriges</span>
        <span class="lang-en">Tutorials</span>
      </h4>
      <p>
        <span class="lang-fr">TD : exercices de configuration routeurs, analyse de trames, deploiement VLAN et depannage reseau.</span>
        <span class="lang-en">Tutorials: router configuration exercises, frame analysis, VLAN deployment, and network troubleshooting.</span>
      </p>
      <embed src="/cours-pdf/S8/Interconnexion-Reseau/td.pdf" type="application/pdf" width="100%" height="800px" />
      <p>
        <span class="lang-fr"><a href="/cours-pdf/S8/Interconnexion-Reseau/td.pdf" target="_blank">Telecharger</a></span>
        <span class="lang-en"><a href="/cours-pdf/S8/Interconnexion-Reseau/td.pdf" target="_blank">Download</a></span>
      </p>
    </div>
  </div>
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

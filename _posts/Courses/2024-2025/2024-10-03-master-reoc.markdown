---
layout: default
title:  "Master REOC"
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

<h1 class="section-title">Master 2 REOC - Reseaux et Objets Connectes</h1>

<h2>PART A : PRESENTATION GENERALE</h2>

<h3 class="section-title">Presentation du Master REOC</h3>

<p>Le <strong>Master 2 REOC</strong> (Reseaux et Objets Connectes) est une formation dispensee a l'<strong>ENSEEIHT</strong> (Ecole Nationale Superieure d'Electrotechnique, d'Electronique, d'Informatique, d'Hydraulique et des Telecommunications) de Toulouse, dans le cadre d'un <strong>double diplome avec l'INSA Toulouse</strong>. Cette formation s'inscrit dans le semestre S9 de l'annee 2024-2025.</p>

<p>Ce programme intensif couvre un large spectre de technologies liees aux reseaux embarques et aux objets connectes. Il offre une vision approfondie des architectures reseau modernes, allant de la virtualisation des reseaux (SDN, NFV) aux reseaux temps reel pour l'aeronautique (AFDX, IMA), en passant par les reseaux bas debit pour l'IoT (LoRaWAN) et les processus stochastiques appliques a l'evaluation de performances.</p>

<p>Le cursus est organise en une dizaine de modules complementaires qui permettent de maitriser les aspects theoriques et pratiques des systemes en reseau embarques. L'approche pedagogique allie cours magistraux, travaux pratiques et projets de mise en situation reelle.</p>

<h3 class="section-title">Objectifs de la formation</h3>
<ul>
<li>Concevoir et deployer des architectures reseau virtualisees (SDN/NFV)</li>
<li>Comprendre et implementer des protocoles de communication temps reel pour les systemes embarques critiques</li>
<li>Evaluer les performances des reseaux a travers la simulation et la modelisation stochastique</li>
<li>Maitriser les technologies de communication bas debit pour l'Internet des Objets</li>
<li>Apprehender les architectures modulaires integrees pour l'avionique</li>
</ul>

<hr>

<h2>PART B : EXPERIENCE ET CONTEXTE</h2>

<h3 class="section-title">Environnement et contexte</h3>

<p>Le Master REOC m'a plonge dans un environnement academique exigeant, mele a l'ENSEEIHT de Toulouse, en parallele de mes cours a l'INSA. Cette double formation a necessite une grande capacite d'organisation et d'adaptation. Les travaux pratiques etaient realises sur des plateformes variees : environnements virtualises avec Docker et Containernet, programmation P4 pour le data plane, simulateurs LoRaWAN en Python, et outils de simulation reseau avec NetworkX.</p>

<p>Le contexte etait celui d'une immersion complete dans les problematiques actuelles des reseaux : comment virtualiser les fonctions reseau, comment garantir le determinisme dans les communications embarquees, comment optimiser les performances des reseaux IoT a grande echelle, et comment modeliser mathematiquement le comportement des systemes en file d'attente.</p>

<h3 class="section-title">Mon role et mes responsabilites</h3>
<ul>
<li><strong>Conception d'architectures reseau</strong> : mise en place de topologies SDN avec Containernet, deploiement de conteneurs Docker pour simuler des equipements reseau</li>
<li><strong>Programmation du data plane</strong> : implementation de parseurs et de tables de correspondance en langage P4 pour le traitement AFDX</li>
<li><strong>Developpement d'outils de monitoring</strong> : creation d'interfaces de surveillance et d'adaptation du trafic via les API de controleurs SDN (Ryu)</li>
<li><strong>Simulation et evaluation de performances</strong> : modelisation de reseaux avec NetworkX, simulation de deploiements LoRaWAN, et calcul de metriques de performance par processus stochastiques</li>
<li><strong>Redaction de rapports techniques</strong> : documentation detaillee des projets realises, notamment le projet SDCI et le rapport sur les processus stochastiques</li>
</ul>

<h3 class="section-title">Collaboration</h3>

<p>La majorite des projets a ete realisee en binome avec <strong>Yohan Boujon</strong>, un partenaire de confiance avec lequel la collaboration etait fluide et efficace. Notre complementarite nous a permis de mener a bien les travaux pratiques dans les delais impartis, malgre la charge de travail consequente liee au double diplome.</p>

<hr>

<h2>PART C : ASPECTS TECHNIQUES</h2>

<p>Cette section detaille les differents modules du Master REOC, couvrant les aspects theoriques et pratiques de chaque thematique abordee.</p>

<hr>

<h3 class="section-title">1. Virtualisation des Reseaux Embarques et P4</h3>

<p>Ce module abordait la virtualisation des reseaux dans un contexte embarque, avec un focus sur le <strong>protocole AFDX</strong> (Avionics Full-Duplex Switched Ethernet) utilise dans l'aeronautique. L'objectif etait de comprendre comment programmer le plan de donnees d'un commutateur reseau en utilisant le langage <strong>P4</strong> (Programming Protocol-Independent Packet Processors).</p>

<p>Le TP portait sur l'implementation d'un commutateur AFDX en P4, ou les trames sont routees en fonction de leur <strong>Virtual Link (VL)</strong>. Voici la structure de la trame AFDX definie en P4 :</p>

<pre><code class="language-p4">header_type afdx_frame_t {
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
}</code></pre>

<p>La topologie etait simulee avec <strong>Mininet</strong> et le commutateur comportemental de P4, permettant de tester le routage des trames AFDX selon les Virtual Links configures.</p>

<p><strong>Concepts cles</strong> : Plan de donnees programmable, AFDX, Virtual Links, P4, Mininet, SDN pour l'embarque, Time-Sensitive Networking (TSN).</p>

<hr>

<h3 class="section-title">2. Information Centric Networking (ICN/NDN)</h3>

<p>Le module sur l'<strong>Information Centric Networking</strong> (ICN), et plus specifiquement le paradigme <strong>Named Data Networking</strong> (NDN), proposait une vision radicalement differente des reseaux par rapport au modele IP classique. Au lieu de connecter des machines entre elles, le NDN centre les communications sur les <strong>donnees elles-memes</strong> : on ne demande plus "connecte-moi a telle machine" mais plutot "donne-moi tel contenu".</p>

<p>Les principes fondamentaux etudies :</p>
<ul>
<li><strong>Interest / Data</strong> : le consommateur envoie un paquet "Interest" portant le nom du contenu souhaite, et le reseau achemine un paquet "Data" en reponse</li>
<li><strong>Content Store (CS)</strong> : chaque noeud du reseau peut mettre en cache les donnees traversantes, permettant de servir les requetes futures localement</li>
<li><strong>Pending Interest Table (PIT)</strong> : table qui enregistre les Interest non encore satisfaits et les interfaces par lesquelles ils sont arrives</li>
<li><strong>Forwarding Information Base (FIB)</strong> : equivalent de la table de routage, mais basee sur les noms de contenus</li>
</ul>

<p>Ce paradigme presente des avantages significatifs pour les reseaux embarques et IoT : reduction de la latence grace au cache distribue, mobilite native des producteurs et consommateurs, et securite integree au niveau des donnees (chaque paquet Data est signe par le producteur).</p>

<p><strong>Concepts cles</strong> : NDN, ICN, Content Store, PIT, FIB, routage par nom, cache distribue, securite centree donnees.</p>

<hr>

<h3 class="section-title">3. Software Defined Networking (SDN) - INSA</h3>

<p>Le module SDN a l'INSA approfondissait les concepts de <strong>separation du plan de controle et du plan de donnees</strong> dans les reseaux. Le cours couvrait les architectures SDN, le protocole <strong>OpenFlow</strong>, et l'utilisation de controleurs SDN tels que <strong>Ryu</strong> pour programmer le comportement du reseau de maniere centralisee.</p>

<p>Les travaux pratiques portaient sur la mise en place d'une architecture SDN complete avec :</p>
<ul>
<li>Configuration de topologies reseau avec des commutateurs OpenFlow</li>
<li>Programmation de regles de flux via le controleur Ryu</li>
<li>Implementation de politiques de routage et de filtrage du trafic</li>
<li>Analyse du comportement du reseau en temps reel</li>
</ul>

<p><strong>Concepts cles</strong> : OpenFlow, controleur SDN, Ryu, plan de controle centralise, regles de flux, QoS, slicing reseau.</p>

<hr>

<h3 class="section-title">4. Wireless Real-Time Networking</h3>

<p>Ce module traitait des <strong>reseaux sans fil temps reel</strong>, une thematique essentielle pour les systemes embarques critiques dans les domaines de l'IoT industriel (IIoT) et de l'aeronautique. Le cours couvrait les protocoles et mecanismes permettant de garantir des communications deterministes sur des supports sans fil intrinsequement non deterministes.</p>

<p>Les thematiques abordees incluaient :</p>
<ul>
<li><strong>Reseaux temps reel embarques</strong> : contraintes de latence, gigue et fiabilite</li>
<li><strong>Ad Hoc Networks</strong> : protocoles de routage distribues pour les reseaux sans infrastructure</li>
<li><strong>IIoT (Industrial Internet of Things)</strong> : application des reseaux temps reel au contexte industriel, avec des contraintes de securite et de surete</li>
<li><strong>Wireless Sensor and Actuator Networks (WSAN)</strong> : protocoles de communication pour les reseaux de capteurs-actionneurs</li>
</ul>

<p>L'etude de papiers de recherche recents permettait de comprendre les defis actuels : comment concilier les exigences temps reel avec les aleas du canal radio, comment dimensionner un reseau sans fil pour garantir un taux de livraison minimum, et comment integrer ces reseaux dans des architectures industrielles existantes.</p>

<p><strong>Concepts cles</strong> : Determinisme, latence bornee, reseaux ad hoc, TDMA, ordonnancement, IIoT, WSAN.</p>

<hr>

<h3 class="section-title">5. Projet NFV/SDCI</h3>

<p>Le projet <strong>NFV/SDCI</strong> (Network Function Virtualization / Software Defined Cloud Infrastructure) constituait le projet majeur du Master REOC. Realise en binome avec Yohan Boujon, ce projet combinait SDN et NFV pour concevoir une infrastructure reseau virtualisee complete avec orchestration.</p>

<h4>5.1 Architecture reseau</h4>

<p>Nous avons concu une topologie reseau composee de plusieurs commutateurs et hotes pour simuler un environnement reseau complexe. La topologie incluait des composants tels que des commutateurs (S1, S2, S3), des hotes (Z1, Z2, Z3), une passerelle intermediaire (GI) et un serveur. Cette configuration nous a permis de tester le filtrage de donnees et la connectivite entre les composants reseau.</p>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_REOC/topology.png" style="max-width: 400px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Topologie reseau du projet SDCI</p>
</div>

<pre><code class="language-python">def setup_topology():
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
    setup_topology()</code></pre>

<h4>5.2 Instances Docker</h4>

<p>Nous avons utilise Docker pour creer des instances pour chaque composant reseau. Un script a ete developpe pour construire les images Docker et generer les instances de maniere efficace. Cette configuration a facilite les tests de connectivite et de transmission de donnees entre les differentes zones.</p>

<pre><code class="language-bash">#!/bin/bash
SCRIPT_PATH=$(realpath "$0")
SCRIPT_DIR=$(dirname "$SCRIPT_PATH")
cd "$SCRIPT_DIR" || exit 1
for dockerfile in "$SCRIPT_DIR"/*.dockerfile; do
    image_tag="reoc:$(basename "$dockerfile" .dockerfile)"
    echo "Building image: $image_tag from $dockerfile"
    docker build -t "$image_tag" -f "$dockerfile" .
done</code></pre>

<h4>5.3 Simulation avec Containernet</h4>

<p>J'ai utilise <strong>Containernet</strong>, un fork de Mininet, pour simuler la topologie reseau. Cela impliquait la creation et la gestion des liens reseau, et la verification de la connectivite entre les instances Docker.</p>

<p>Une fois le script <code>topology_sdn.py</code> lance, j'ai teste la connectivite entre les differents hotes de la topologie :</p>

<pre><code class="language-bash">containernet> z1 ping -c 1 z2
containernet> z1 ping -c 1 serveur
containernet> z2 ping -c 1 z1
containernet> z2 ping -c 1 gi
containernet> ordon ping -c 1 z3
containernet> ordon ping -c 1 serveur</code></pre>

<h4>5.4 Application 'Moniteur'</h4>

<h5>Monitoring</h5>

<p>L'interface de monitoring, developpee avec <strong>npyscreen</strong>, permettait aux utilisateurs de selectionner et d'executer differents scripts en fonction des tests souhaites. Pour surveiller les donnees envoyees par chaque zone, nous nous concentrions sur le commutateur S1. En appelant l'API Ryu, nous pouvions observer des metriques telles que le trafic entrant et sortant, la taille des paquets et le total d'octets en temps reel.</p>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_REOC/monitor.png" style="max-width: 600px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Interface de monitoring du trafic reseau</p>
</div>

<h5>Adaptation</h5>

<p>Les scenarios d'adaptation incluaient le blocage des trames de Z2 et Z3 ou la reduction de leur bande passante tout en priorisant Z1. Cela etait realise via des requetes POST a l'API Ryu pour appliquer des regles telles que :</p>

<pre><code class="language-json">{
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
}</code></pre>

<p><strong>Concepts cles</strong> : Containernet, Docker, NFV, MANO, orchestration, monitoring, adaptation, API REST, Ryu.</p>

<hr>

<h3 class="section-title">6. Architecture Modulaire</h3>

<p>Le module sur l'<strong>Architecture Modulaire</strong> traitait de la conception de systemes embarques temps reel, avec un accent particulier sur le <strong>Worst-Case Traversal Time (WCTT)</strong>. Ce concept est fondamental dans les reseaux embarques deterministes, notamment dans l'aeronautique et l'automobile.</p>

<p>Le WCTT represente le temps maximal qu'un paquet peut mettre pour traverser le reseau dans le pire des cas. Le calcul du WCTT est essentiel pour :</p>
<ul>
<li><strong>Garantir le determinisme</strong> : s'assurer que chaque message arrive dans les delais impartis</li>
<li><strong>Dimensionner les reseaux</strong> : choisir les capacites des liens et des commutateurs en fonction des contraintes temporelles</li>
<li><strong>Certifier les systemes critiques</strong> : fournir des preuves formelles du respect des echeances dans les systemes avioniques</li>
</ul>

<p>Les methodes d'analyse etudiees incluaient le <strong>Network Calculus</strong> et les approches par <strong>simulation aggregee</strong>, permettant d'approximer les bornes du WCTT pour des topologies complexes.</p>

<p><strong>Concepts cles</strong> : WCTT, Network Calculus, determinisme, systemes critiques, certification, bornes temporelles.</p>

<hr>

<h3 class="section-title">7. Simulation Avancee avec NetworkX (N7)</h3>

<p>Ce module, dispense a l'ENSEEIHT (N7), portait sur la <strong>simulation avancee de reseaux</strong> en utilisant la bibliotheque Python <strong>NetworkX</strong>. Le sujet central etait le <strong>probleme de consensus</strong> dans les reseaux distribues.</p>

<h4>Probleme de consensus</h4>

<p>L'objectif est que tous les noeuds d'un reseau convergent vers une meme valeur. Chaque noeud est initialise avec une valeur aleatoire, et a chaque cycle, un noeud diffuse sa valeur a ses voisins, qui mettent alors a jour leur propre valeur par moyenne :</p>

<pre><code>while 1 do
    if (time mod T) = 0 then
        broadcast {VAL}
    else if msgReceived(R_VAL) then
        VAL &lt;- (VAL + R_VAL) / 2
    end if
end while</code></pre>

<h4>Modelisation matricielle</h4>

<p>L'approche mathematique utilisait des <strong>matrices de transition</strong> pour modeliser l'evolution du systeme. Pour chaque noeud emetteur, une matrice Ei est construite, et le produit de ces matrices sur un cycle donne la matrice de transition globale Pl :</p>

<pre><code class="language-python">import numpy as np

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
    return Po</code></pre>

<h4>Resultats de simulation</h4>

<p>Les simulations ont ete realisees sur differentes topologies (mesh et ligne) en variant le nombre de noeuds :</p>

<table>
<tr><th>Topologie</th><th>Noeuds</th><th>Cycles moyens</th><th>Ecart-type</th></tr>
<tr><td>Mesh</td><td>5</td><td>2.4</td><td>0.21</td></tr>
<tr><td>Mesh</td><td>10</td><td>2.1</td><td>0.26</td></tr>
<tr><td>Ligne</td><td>5</td><td>24</td><td>11.17</td></tr>
<tr><td>Ligne</td><td>10</td><td>63</td><td>46.8</td></tr>
</table>

<p>La correlation entre le <strong>plus grand valeur propre</strong> de la matrice Pl et le temps de convergence a ete etudiee en generant 1000 sequences aleatoires et en tracant la relation entre ces deux metriques.</p>

<p><strong>Concepts cles</strong> : Consensus distribue, NetworkX, matrices de transition, valeurs propres, convergence, topologie reseau.</p>

<hr>

<h3 class="section-title">8. Integrated Modular Avionics (IMA)</h3>

<p>Le module <strong>Integrated Modular Avionics</strong> (IMA) traitait de l'architecture des systemes avioniques modernes. L'IMA est un concept d'architecture informatique dans lequel les ressources de calcul sont partagees entre plusieurs applications avioniques, contrairement a l'approche federee traditionnelle ou chaque fonction dispose de son propre equipement dedie.</p>

<p>Les principes fondamentaux de l'IMA :</p>
<ul>
<li><strong>Partitionnement temporel et spatial</strong> : chaque application dispose de creneaux temporels fixes et d'espaces memoire isoles, garantissant l'absence d'interference entre les fonctions</li>
<li><strong>Norme ARINC 653</strong> : standard definissant l'interface entre les applications avioniques et le systeme d'exploitation temps reel, assurant la portabilite et l'interchangeabilite</li>
<li><strong>AFDX (Avionics Full-Duplex Switched Ethernet)</strong> : reseau de communication deterministe utilise pour interconnecter les modules IMA, avec des Virtual Links garantissant des bornes temporelles</li>
<li><strong>Certification DO-178C</strong> : processus de certification logicielle pour les systemes embarques critiques de l'aeronautique</li>
</ul>

<p>L'IMA represente une evolution majeure dans l'avionique, permettant de reduire le poids, la consommation energetique et les couts de maintenance des systemes de bord, tout en maintenant les niveaux de securite les plus eleves (DAL A).</p>

<p><strong>Concepts cles</strong> : IMA, ARINC 653, AFDX, partitionnement, DO-178C, certification, systemes critiques.</p>

<hr>

<h3 class="section-title">9. Low Power Networks for IoT</h3>

<p>Ce module portait sur les <strong>reseaux basse consommation pour l'Internet des Objets</strong>, avec un focus particulier sur la technologie <strong>LoRaWAN</strong>. Le cours couvrait les specificites des communications IoT, ou les contraintes de consommation energetique et de cout sont primordiales.</p>

<h4>Caracteristiques de l'IoT</h4>

<p>Les systemes IoT se distinguent par :</p>
<ul>
<li><strong>Pervasive Computing</strong> : dispositifs nombreux, circuits bon marche, memoire et puissance de calcul limitees</li>
<li><strong>Connectivite sans fil</strong> : alimentation par batterie ou energy harvesting, duree de vie superieure a 10 ans</li>
<li><strong>Cout reduit</strong> : puce a 2$, abonnement radio a 1$ par dispositif par an</li>
<li><strong>Longue portee</strong> : 5 a 40 km en champ libre</li>
</ul>

<h4>Pile protocolaire IoT</h4>

<table>
<tr><th>Couche</th><th>Standard</th></tr>
<tr><td>Application</td><td>IETF CoAP</td></tr>
<tr><td>Transport</td><td>IETF UDP</td></tr>
<tr><td>Adaptation</td><td>IETF 6LoWPAN, IETF SCHC</td></tr>
<tr><td>Acces reseau</td><td>IEEE 802.15.4, LoRaWAN</td></tr>
</table>

<h4>Travaux pratiques : Simulation LoRaWAN</h4>

<p>Les TP consistaient en la simulation d'un deploiement LoRaWAN avec calcul de la couverture par triangulation. L'objectif etait d'evaluer les performances d'un reseau de passerelles LoRa en termes de taux de livraison de paquets (PDR) en fonction de la densite de deploiement et des parametres radio (spreading factor, puissance d'emission).</p>

<p>Un rapport detaille sur le deploiement LoRaWAN et l'analyse par triangulation a ete produit, demontrant l'impact du placement des passerelles sur la couverture et la fiabilite du reseau.</p>

<p><strong>Concepts cles</strong> : LoRaWAN, LPWAN, IoT, ALOHA, spreading factor, PDR, energy harvesting, 6LoWPAN, CoAP.</p>

<hr>

<h3 class="section-title">10. Processus Stochastiques</h3>

<p>Le module sur les <strong>processus stochastiques</strong> traitait de la modelisation et de l'evaluation de performances des systemes en file d'attente, un outil fondamental pour l'analyse des reseaux de communication.</p>

<h4>Reseaux de files d'attente fermes</h4>

<p>Le TP portait sur la simulation et le calcul analytique des performances d'un reseau ferme compose de quatre stations (T, H, R, D) avec N clients circulant en boucle :</p>

<pre><code class="language-python">def exact_performance_measures(lambdaH, muH, muR, muD, C, N, p):
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
    return G4</code></pre>

<h4>Scenarios simules</h4>

<p>Plusieurs scenarios ont ete simules en faisant varier les parametres N (nombre de clients) et p (probabilite de routage) :</p>

<table>
<tr><th>Scenario</th><th>N</th><th>p</th><th>Description</th></tr>
<tr><td>Cas 1</td><td>15</td><td>0.50</td><td>Charge moderee, routage equilibre</td></tr>
<tr><td>Cas 2</td><td>15</td><td>0.22</td><td>Charge moderee, routage vers le disque dominant</td></tr>
<tr><td>Cas 3</td><td>30</td><td>0.50</td><td>Forte charge, routage equilibre</td></tr>
<tr><td>Cas 4</td><td>30</td><td>0.22</td><td>Forte charge, routage vers le disque dominant</td></tr>
</table>

<p>Les metriques evaluees comprenaient le <strong>taux d'utilisation</strong>, le <strong>debit</strong>, le <strong>temps de sejour moyen</strong> et la <strong>probabilite de rejet</strong>, calculees a la fois de maniere analytique (loi de Little, distribution stationnaire) et par simulation Monte Carlo.</p>

<p><strong>Concepts cles</strong> : Files d'attente, reseaux fermes, loi de Little, chaines de Markov, distribution stationnaire, simulation Monte Carlo, intensite de trafic.</p>

<hr>

<h2>PART D : ANALYSE ET REFLEXION</h2>

<h3 class="section-title">Competences et connaissances mobilisees</h3>

<p>Le Master REOC m'a permis de mobiliser et d'approfondir un ensemble de competences variees :</p>

<ul>
<li><strong>Architecture reseau</strong> : comprehension des architectures SDN et NFV, et leur application dans les reseaux embarques et l'orchestration cloud</li>
<li><strong>Programmation du data plane</strong> : maitrise du langage P4 pour le traitement des paquets au niveau materiel</li>
<li><strong>Systemes temps reel</strong> : comprehension des contraintes temporelles dans les reseaux embarques critiques (AFDX, IMA, TSN)</li>
<li><strong>Simulation et modelisation</strong> : utilisation de NetworkX, de simulateurs LoRaWAN et de modeles stochastiques pour l'evaluation de performances</li>
<li><strong>Developpement logiciel</strong> : programmation Python pour la simulation, l'analyse de donnees et le developpement d'outils de monitoring</li>
<li><strong>Travail collaboratif</strong> : gestion de projets en binome dans un contexte de double diplome exigeant</li>
</ul>

<h3 class="section-title">Auto-evaluation</h3>

<p>Le programme du Master REOC etait intense, d'autant plus que les cours de l'INSA se poursuivaient en parallele. Cependant, cette experience a ete extremement enrichissante car j'ai acquis de nouvelles competences que j'ai pu mettre en oeuvre apres une analyse approfondie des bibliotheques et la comprehension du fonctionnement du SDN. Grace a mon partenaire, Yohan Boujon, notre collaboration etait efficace car nous nous connaissions bien et avons developpe la quasi-totalite de ce qui etait demande dans le temps imparti lors des travaux pratiques.</p>

<h3 class="section-title">Mon avis</h3>

<p>Si je devais choisir a nouveau, je m'inscrirais sans hesitation au Master REOC. Le programme m'a permis d'elargir ma vision des reseaux dans les systemes embarques et d'acquerir une experience precieuse. Les enseignants ont fourni des bases solides pour comprendre tous les concepts applicables dans le monde professionnel. Les competences acquises seront utiles pour ma carriere. Ce programme a significativement contribue a ma croissance professionnelle et m'a prepare aux defis futurs dans le domaine des systemes en reseau.</p>

<p>La diversite des modules -- de l'avionique deterministe a l'IoT basse consommation, en passant par la virtualisation et la modelisation stochastique -- offre une vision panoramique des enjeux actuels des reseaux embarques. Cette polyvalence est un atout majeur pour aborder les problematiques industrielles complexes qui melent souvent plusieurs de ces domaines.</p>

<hr>

<h2>Rapports et Projets</h2>

<h3>Rapport du Projet SDCI</h3>

<p>Le rapport complet du projet SDCI est disponible sur <a href="https://github.com/CedricChnfr/sdci-reoc">GitHub - sdci-reoc</a>.</p>

<div class="pdf-container" style="display: flex; justify-content: center;">
    <iframe src="/img/BE_REOC/CHANFREAU_BOUJON_SDCI.pdf" width="100%" height="800px" style="overflow: auto;" frameborder="0"></iframe>
</div>

<p style="text-align: center;">
    <a href="/img/BE_REOC/CHANFREAU_BOUJON_SDCI.pdf" target="_blank">Ouvrir le rapport complet du projet SDCI</a>
</p>

<p style="text-align: center;">
    <a href="https://docs.google.com/presentation/d/1N_HovdFQlvxd32VUzZlEpD46pnBx_45RN4CnxDaeWEs/edit">Ouvrir le sujet du TP</a>
</p>

<h3>Rapport sur les Processus Stochastiques</h3>

<div class="pdf-container" style="display: flex; justify-content: center;">
    <iframe src="/file/reports/S9/Report_Stochastique_REOC.pdf" width="100%" height="800px" style="overflow: auto;" frameborder="0"></iframe>
</div>

<p style="text-align: center;">
    <a href="/file/reports/S9/Report_Stochastique_REOC.pdf" target="_blank">Ouvrir le rapport sur les processus stochastiques</a>
</p>

<hr>
<p><em>Cours suivi en 2024-2025 dans le cadre du double diplome INSA Toulouse / ENSEEIHT, Master 2 REOC.</em></p>

</div>

<div class="lang-en">

<h1 class="section-title">Master 2 REOC - Networks and Connected Objects</h1>

<h2>PART A: GENERAL PRESENTATION</h2>

<h3 class="section-title">Presentation of the Master REOC</h3>

<p>The <strong>Master 2 REOC</strong> (Reseaux et Objets Connectes / Networks and Connected Objects) is a program offered at <strong>ENSEEIHT</strong> (Ecole Nationale Superieure d'Electrotechnique, d'Electronique, d'Informatique, d'Hydraulique et des Telecommunications) in Toulouse, as part of a <strong>dual degree with INSA Toulouse</strong>. This program is part of semester S9 of the 2024-2025 academic year.</p>

<p>This intensive program covers a broad spectrum of technologies related to embedded networks and connected objects. It provides an in-depth understanding of modern network architectures, ranging from network virtualization (SDN, NFV) to real-time networks for aeronautics (AFDX, IMA), including low-throughput networks for IoT (LoRaWAN) and stochastic processes applied to performance evaluation.</p>

<p>The curriculum is organized into about ten complementary modules that cover both theoretical and practical aspects of embedded networked systems. The teaching approach combines lectures, lab sessions and real-world project assignments.</p>

<h3 class="section-title">Training objectives</h3>
<ul>
<li>Design and deploy virtualized network architectures (SDN/NFV)</li>
<li>Understand and implement real-time communication protocols for critical embedded systems</li>
<li>Evaluate network performance through simulation and stochastic modeling</li>
<li>Master low-throughput communication technologies for the Internet of Things</li>
<li>Understand integrated modular architectures for avionics</li>
</ul>

<hr>

<h2>PART B: EXPERIENCE AND CONTEXT</h2>

<h3 class="section-title">Environment and context</h3>

<p>The Master REOC immersed me in a demanding academic environment at ENSEEIHT in Toulouse, alongside my courses at INSA. This dual program required strong organizational and adaptation skills. Lab sessions were carried out on various platforms: virtualized environments with Docker and Containernet, P4 programming for the data plane, LoRaWAN simulators in Python, and network simulation tools with NetworkX.</p>

<p>The context was one of complete immersion in current networking challenges: how to virtualize network functions, how to guarantee determinism in embedded communications, how to optimize IoT network performance at scale, and how to mathematically model the behavior of queuing systems.</p>

<h3 class="section-title">My role and responsibilities</h3>
<ul>
<li><strong>Network architecture design</strong>: setting up SDN topologies with Containernet, deploying Docker containers to simulate network equipment</li>
<li><strong>Data plane programming</strong>: implementing parsers and match-action tables in P4 language for AFDX processing</li>
<li><strong>Monitoring tool development</strong>: creating traffic monitoring and adaptation interfaces via SDN controller APIs (Ryu)</li>
<li><strong>Simulation and performance evaluation</strong>: network modeling with NetworkX, LoRaWAN deployment simulation, and performance metric computation through stochastic processes</li>
<li><strong>Technical report writing</strong>: detailed documentation of completed projects, notably the SDCI project and the stochastic processes report</li>
</ul>

<h3 class="section-title">Collaboration</h3>

<p>Most projects were carried out in pairs with <strong>Yohan Boujon</strong>, a trusted partner with whom collaboration was smooth and efficient. Our complementary skills allowed us to successfully complete lab work within the given deadlines, despite the substantial workload associated with the dual degree.</p>

<hr>

<h2>PART C: TECHNICAL ASPECTS</h2>

<p>This section details the various modules of the Master REOC, covering the theoretical and practical aspects of each topic addressed.</p>

<hr>

<h3 class="section-title">1. Embedded Network Virtualization and P4</h3>

<p>This module covered network virtualization in an embedded context, with a focus on the <strong>AFDX protocol</strong> (Avionics Full-Duplex Switched Ethernet) used in aeronautics. The objective was to understand how to program the data plane of a network switch using the <strong>P4</strong> language (Programming Protocol-Independent Packet Processors).</p>

<p>The lab session focused on implementing an AFDX switch in P4, where frames are routed based on their <strong>Virtual Link (VL)</strong>. Here is the AFDX frame structure defined in P4:</p>

<pre><code class="language-p4">header_type afdx_frame_t {
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
}</code></pre>

<p>The topology was simulated with <strong>Mininet</strong> and the P4 behavioral model switch, allowing testing of AFDX frame routing according to configured Virtual Links.</p>

<p><strong>Key concepts</strong>: Programmable data plane, AFDX, Virtual Links, P4, Mininet, SDN for embedded systems, Time-Sensitive Networking (TSN).</p>

<hr>

<h3 class="section-title">2. Information Centric Networking (ICN/NDN)</h3>

<p>The <strong>Information Centric Networking</strong> (ICN) module, and more specifically the <strong>Named Data Networking</strong> (NDN) paradigm, offered a radically different vision of networking compared to the traditional IP model. Instead of connecting machines to each other, NDN focuses communications on <strong>the data itself</strong>: rather than asking "connect me to this machine", one asks "give me this content".</p>

<p>The fundamental principles studied:</p>
<ul>
<li><strong>Interest / Data</strong>: the consumer sends an "Interest" packet carrying the name of the desired content, and the network delivers a "Data" packet in response</li>
<li><strong>Content Store (CS)</strong>: each network node can cache traversing data, enabling future requests to be served locally</li>
<li><strong>Pending Interest Table (PIT)</strong>: a table that records unsatisfied Interest packets and the interfaces through which they arrived</li>
<li><strong>Forwarding Information Base (FIB)</strong>: the equivalent of a routing table, but based on content names</li>
</ul>

<p>This paradigm presents significant advantages for embedded and IoT networks: latency reduction through distributed caching, native mobility of producers and consumers, and data-level built-in security (each Data packet is signed by the producer).</p>

<p><strong>Key concepts</strong>: NDN, ICN, Content Store, PIT, FIB, name-based routing, distributed cache, data-centric security.</p>

<hr>

<h3 class="section-title">3. Software Defined Networking (SDN) - INSA</h3>

<p>The SDN module at INSA deepened the concepts of <strong>separation between the control plane and the data plane</strong> in networks. The course covered SDN architectures, the <strong>OpenFlow</strong> protocol, and the use of SDN controllers such as <strong>Ryu</strong> to program network behavior in a centralized manner.</p>

<p>The lab sessions focused on setting up a complete SDN architecture with:</p>
<ul>
<li>Configuration of network topologies with OpenFlow switches</li>
<li>Programming flow rules via the Ryu controller</li>
<li>Implementation of routing and traffic filtering policies</li>
<li>Real-time network behavior analysis</li>
</ul>

<p><strong>Key concepts</strong>: OpenFlow, SDN controller, Ryu, centralized control plane, flow rules, QoS, network slicing.</p>

<hr>

<h3 class="section-title">4. Wireless Real-Time Networking</h3>

<p>This module addressed <strong>wireless real-time networks</strong>, a topic essential for critical embedded systems in the fields of Industrial IoT (IIoT) and aeronautics. The course covered protocols and mechanisms for guaranteeing deterministic communications over inherently non-deterministic wireless media.</p>

<p>Topics covered included:</p>
<ul>
<li><strong>Embedded real-time networks</strong>: latency, jitter and reliability constraints</li>
<li><strong>Ad Hoc Networks</strong>: distributed routing protocols for infrastructure-less networks</li>
<li><strong>IIoT (Industrial Internet of Things)</strong>: application of real-time networks to the industrial context, with safety and security constraints</li>
<li><strong>Wireless Sensor and Actuator Networks (WSAN)</strong>: communication protocols for sensor-actuator networks</li>
</ul>

<p>Studying recent research papers helped understand current challenges: how to reconcile real-time requirements with radio channel uncertainties, how to dimension a wireless network to guarantee a minimum delivery rate, and how to integrate these networks into existing industrial architectures.</p>

<p><strong>Key concepts</strong>: Determinism, bounded latency, ad hoc networks, TDMA, scheduling, IIoT, WSAN.</p>

<hr>

<h3 class="section-title">5. NFV/SDCI Project</h3>

<p>The <strong>NFV/SDCI</strong> (Network Function Virtualization / Software Defined Cloud Infrastructure) project was the major project of the Master REOC. Carried out in pairs with Yohan Boujon, this project combined SDN and NFV to design a complete virtualized network infrastructure with orchestration.</p>

<h4>5.1 Network architecture</h4>

<p>We designed a network topology consisting of multiple switches and hosts to simulate a complex network environment. The topology included components such as switches (S1, S2, S3), hosts (Z1, Z2, Z3), an intermediate gateway (GI) and a server. This configuration allowed us to test data filtering and connectivity between network components.</p>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_REOC/topology.png" style="max-width: 400px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: SDCI project network topology</p>
</div>

<pre><code class="language-python">def setup_topology():
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
    setup_topology()</code></pre>

<h4>5.2 Docker instances</h4>

<p>We used Docker to create instances for each network component. A script was developed to build Docker images and generate instances efficiently. This setup facilitated connectivity and data transmission testing between the different zones.</p>

<pre><code class="language-bash">#!/bin/bash
SCRIPT_PATH=$(realpath "$0")
SCRIPT_DIR=$(dirname "$SCRIPT_PATH")
cd "$SCRIPT_DIR" || exit 1
for dockerfile in "$SCRIPT_DIR"/*.dockerfile; do
    image_tag="reoc:$(basename "$dockerfile" .dockerfile)"
    echo "Building image: $image_tag from $dockerfile"
    docker build -t "$image_tag" -f "$dockerfile" .
done</code></pre>

<h4>5.3 Simulation with Containernet</h4>

<p>I used <strong>Containernet</strong>, a Mininet fork, to simulate the network topology. This involved creating and managing network links, and verifying connectivity between Docker instances.</p>

<p>Once the <code>topology_sdn.py</code> script was launched, I tested connectivity between the different hosts in the topology:</p>

<pre><code class="language-bash">containernet> z1 ping -c 1 z2
containernet> z1 ping -c 1 serveur
containernet> z2 ping -c 1 z1
containernet> z2 ping -c 1 gi
containernet> ordon ping -c 1 z3
containernet> ordon ping -c 1 serveur</code></pre>

<h4>5.4 'Monitor' application</h4>

<h5>Monitoring</h5>

<p>The monitoring interface, developed with <strong>npyscreen</strong>, allowed users to select and run different scripts based on the desired tests. To monitor the data sent by each zone, we focused on switch S1. By calling the Ryu API, we could observe metrics such as incoming and outgoing traffic, packet size and total bytes in real time.</p>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_REOC/monitor.png" style="max-width: 600px; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Network traffic monitoring interface</p>
</div>

<h5>Adaptation</h5>

<p>Adaptation scenarios included blocking frames from Z2 and Z3 or reducing their bandwidth while prioritizing Z1. This was achieved via POST requests to the Ryu API to apply rules such as:</p>

<pre><code class="language-json">{
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
}</code></pre>

<p><strong>Key concepts</strong>: Containernet, Docker, NFV, MANO, orchestration, monitoring, adaptation, REST API, Ryu.</p>

<hr>

<h3 class="section-title">6. Modular Architecture</h3>

<p>The <strong>Modular Architecture</strong> module dealt with the design of real-time embedded systems, with a particular emphasis on <strong>Worst-Case Traversal Time (WCTT)</strong>. This concept is fundamental in deterministic embedded networks, particularly in aeronautics and automotive.</p>

<p>WCTT represents the maximum time a packet can take to traverse the network in the worst case. Computing the WCTT is essential for:</p>
<ul>
<li><strong>Guaranteeing determinism</strong>: ensuring that every message arrives within the prescribed deadlines</li>
<li><strong>Sizing networks</strong>: choosing link and switch capacities based on timing constraints</li>
<li><strong>Certifying critical systems</strong>: providing formal proof of deadline compliance in avionics systems</li>
</ul>

<p>The analysis methods studied included <strong>Network Calculus</strong> and <strong>aggregate simulation</strong> approaches, allowing approximation of WCTT bounds for complex topologies.</p>

<p><strong>Key concepts</strong>: WCTT, Network Calculus, determinism, critical systems, certification, timing bounds.</p>

<hr>

<h3 class="section-title">7. Advanced Simulation with NetworkX (N7)</h3>

<p>This module, taught at ENSEEIHT (N7), focused on <strong>advanced network simulation</strong> using the Python <strong>NetworkX</strong> library. The central topic was the <strong>consensus problem</strong> in distributed networks.</p>

<h4>Consensus problem</h4>

<p>The goal is for all nodes in a network to converge to the same value. Each node is initialized with a random value, and at each cycle, a node broadcasts its value to its neighbors, which then update their own value by averaging:</p>

<pre><code>while 1 do
    if (time mod T) = 0 then
        broadcast {VAL}
    else if msgReceived(R_VAL) then
        VAL &lt;- (VAL + R_VAL) / 2
    end if
end while</code></pre>

<h4>Matrix modeling</h4>

<p>The mathematical approach used <strong>transition matrices</strong> to model the system's evolution. For each emitting node, a matrix Ei is constructed, and the product of these matrices over one cycle yields the global transition matrix Pl:</p>

<pre><code class="language-python">import numpy as np

def create_matrix_Ei(graph, emitter):
    """Create the Ei matrix for a given emitting node."""
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
    """Compute the Pl matrix for a given emission sequence."""
    n = len(graph.nodes)
    Po = np.eye(n)
    for emitter in sequence:
        Ei = create_matrix_Ei(graph, emitter)
        Po = Ei @ Po
    return Po</code></pre>

<h4>Simulation results</h4>

<p>Simulations were carried out on different topologies (mesh and line) with varying numbers of nodes:</p>

<table>
<tr><th>Topology</th><th>Nodes</th><th>Average cycles</th><th>Standard deviation</th></tr>
<tr><td>Mesh</td><td>5</td><td>2.4</td><td>0.21</td></tr>
<tr><td>Mesh</td><td>10</td><td>2.1</td><td>0.26</td></tr>
<tr><td>Line</td><td>5</td><td>24</td><td>11.17</td></tr>
<tr><td>Line</td><td>10</td><td>63</td><td>46.8</td></tr>
</table>

<p>The correlation between the <strong>largest eigenvalue</strong> of the Pl matrix and the convergence time was studied by generating 1000 random sequences and plotting the relationship between these two metrics.</p>

<p><strong>Key concepts</strong>: Distributed consensus, NetworkX, transition matrices, eigenvalues, convergence, network topology.</p>

<hr>

<h3 class="section-title">8. Integrated Modular Avionics (IMA)</h3>

<p>The <strong>Integrated Modular Avionics</strong> (IMA) module covered the architecture of modern avionics systems. IMA is a computing architecture concept in which computing resources are shared among multiple avionics applications, in contrast to the traditional federated approach where each function has its own dedicated equipment.</p>

<p>The fundamental principles of IMA:</p>
<ul>
<li><strong>Temporal and spatial partitioning</strong>: each application has fixed time slots and isolated memory spaces, guaranteeing no interference between functions</li>
<li><strong>ARINC 653 standard</strong>: a standard defining the interface between avionics applications and the real-time operating system, ensuring portability and interchangeability</li>
<li><strong>AFDX (Avionics Full-Duplex Switched Ethernet)</strong>: a deterministic communication network used to interconnect IMA modules, with Virtual Links guaranteeing timing bounds</li>
<li><strong>DO-178C certification</strong>: software certification process for critical embedded systems in aeronautics</li>
</ul>

<p>IMA represents a major evolution in avionics, enabling reduced weight, power consumption and maintenance costs for onboard systems, while maintaining the highest safety levels (DAL A).</p>

<p><strong>Key concepts</strong>: IMA, ARINC 653, AFDX, partitioning, DO-178C, certification, critical systems.</p>

<hr>

<h3 class="section-title">9. Low Power Networks for IoT</h3>

<p>This module focused on <strong>low-power networks for the Internet of Things</strong>, with a particular focus on <strong>LoRaWAN</strong> technology. The course covered the specifics of IoT communications, where energy consumption and cost constraints are paramount.</p>

<h4>IoT characteristics</h4>

<p>IoT systems are distinguished by:</p>
<ul>
<li><strong>Pervasive Computing</strong>: numerous devices, low-cost circuits, limited memory and computing power</li>
<li><strong>Wireless connectivity</strong>: battery-powered or energy harvesting, lifetime exceeding 10 years</li>
<li><strong>Reduced cost</strong>: $2 chip, $1 radio subscription per device per year</li>
<li><strong>Long range</strong>: 5 to 40 km in open field</li>
</ul>

<h4>IoT protocol stack</h4>

<table>
<tr><th>Layer</th><th>Standard</th></tr>
<tr><td>Application</td><td>IETF CoAP</td></tr>
<tr><td>Transport</td><td>IETF UDP</td></tr>
<tr><td>Adaptation</td><td>IETF 6LoWPAN, IETF SCHC</td></tr>
<tr><td>Network access</td><td>IEEE 802.15.4, LoRaWAN</td></tr>
</table>

<h4>Lab sessions: LoRaWAN simulation</h4>

<p>The lab sessions consisted of simulating a LoRaWAN deployment with coverage calculation through triangulation. The objective was to evaluate the performance of a LoRa gateway network in terms of Packet Delivery Rate (PDR) based on deployment density and radio parameters (spreading factor, transmission power).</p>

<p>A detailed report on LoRaWAN deployment and triangulation analysis was produced, demonstrating the impact of gateway placement on network coverage and reliability.</p>

<p><strong>Key concepts</strong>: LoRaWAN, LPWAN, IoT, ALOHA, spreading factor, PDR, energy harvesting, 6LoWPAN, CoAP.</p>

<hr>

<h3 class="section-title">10. Stochastic Processes</h3>

<p>The <strong>stochastic processes</strong> module dealt with modeling and performance evaluation of queuing systems, a fundamental tool for the analysis of communication networks.</p>

<h4>Closed queuing networks</h4>

<p>The lab session focused on simulation and analytical computation of the performance of a closed network composed of four stations (T, H, R, D) with N clients circulating in a loop:</p>

<pre><code class="language-python">def exact_performance_measures(lambdaH, muH, muR, muD, C, N, p):
    # Compute effective arrival rates
    gamma_H = lambdaH
    gamma_R = gamma_H / p
    gamma_D = (1 - p) * gamma_H / p

    # Compute traffic intensities
    rho_H = gamma_H / muH
    rho_R = gamma_R / (C * muR)
    rho_D = gamma_D / muD

    # Compute normalization constant G4(N)
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
    return G4</code></pre>

<h4>Simulated scenarios</h4>

<p>Several scenarios were simulated by varying the parameters N (number of clients) and p (routing probability):</p>

<table>
<tr><th>Scenario</th><th>N</th><th>p</th><th>Description</th></tr>
<tr><td>Case 1</td><td>15</td><td>0.50</td><td>Moderate load, balanced routing</td></tr>
<tr><td>Case 2</td><td>15</td><td>0.22</td><td>Moderate load, disk-dominant routing</td></tr>
<tr><td>Case 3</td><td>30</td><td>0.50</td><td>Heavy load, balanced routing</td></tr>
<tr><td>Case 4</td><td>30</td><td>0.22</td><td>Heavy load, disk-dominant routing</td></tr>
</table>

<p>The evaluated metrics included <strong>utilization rate</strong>, <strong>throughput</strong>, <strong>average sojourn time</strong> and <strong>rejection probability</strong>, computed both analytically (Little's law, stationary distribution) and via Monte Carlo simulation.</p>

<p><strong>Key concepts</strong>: Queuing theory, closed networks, Little's law, Markov chains, stationary distribution, Monte Carlo simulation, traffic intensity.</p>

<hr>

<h2>PART D: ANALYSIS AND REFLECTION</h2>

<h3 class="section-title">Skills and knowledge mobilized</h3>

<p>The Master REOC enabled me to mobilize and deepen a diverse set of skills:</p>

<ul>
<li><strong>Network architecture</strong>: understanding of SDN and NFV architectures and their application in embedded networks and cloud orchestration</li>
<li><strong>Data plane programming</strong>: mastery of the P4 language for hardware-level packet processing</li>
<li><strong>Real-time systems</strong>: understanding of timing constraints in critical embedded networks (AFDX, IMA, TSN)</li>
<li><strong>Simulation and modeling</strong>: use of NetworkX, LoRaWAN simulators and stochastic models for performance evaluation</li>
<li><strong>Software development</strong>: Python programming for simulation, data analysis and monitoring tool development</li>
<li><strong>Collaborative work</strong>: project management in pairs within a demanding dual-degree context</li>
</ul>

<h3 class="section-title">Self-assessment</h3>

<p>The Master REOC program was intense, especially since INSA courses continued in parallel. However, this experience was extremely enriching as I acquired new skills that I was able to apply after thorough analysis of libraries and understanding of SDN operations. Thanks to my partner, Yohan Boujon, our collaboration was efficient because we knew each other well and developed almost everything that was required within the allotted time during lab sessions.</p>

<h3 class="section-title">My opinion</h3>

<p>If I had to choose again, I would enroll in the Master REOC without hesitation. The program allowed me to broaden my vision of networking in embedded systems and gain valuable experience. The instructors provided solid foundations for understanding all concepts applicable in the professional world. The skills acquired will be useful for my career. This program significantly contributed to my professional growth and prepared me for future challenges in the field of networked systems.</p>

<p>The diversity of modules -- from deterministic avionics to low-power IoT, through virtualization and stochastic modeling -- provides a panoramic view of the current challenges in embedded networks. This versatility is a major asset for tackling complex industrial problems that often span multiple domains.</p>

<hr>

<h2>Reports and Projects</h2>

<h3>SDCI Project Report</h3>

<p>The full SDCI project report is available on <a href="https://github.com/CedricChnfr/sdci-reoc">GitHub - sdci-reoc</a>.</p>

<div class="pdf-container" style="display: flex; justify-content: center;">
    <iframe src="/img/BE_REOC/CHANFREAU_BOUJON_SDCI.pdf" width="100%" height="800px" style="overflow: auto;" frameborder="0"></iframe>
</div>

<p style="text-align: center;">
    <a href="/img/BE_REOC/CHANFREAU_BOUJON_SDCI.pdf" target="_blank">Open the full SDCI project report</a>
</p>

<p style="text-align: center;">
    <a href="https://docs.google.com/presentation/d/1N_HovdFQlvxd32VUzZlEpD46pnBx_45RN4CnxDaeWEs/edit">Open the lab subject</a>
</p>

<h3>Stochastic Processes Report</h3>

<div class="pdf-container" style="display: flex; justify-content: center;">
    <iframe src="/file/reports/S9/Report_Stochastique_REOC.pdf" width="100%" height="800px" style="overflow: auto;" frameborder="0"></iframe>
</div>

<p style="text-align: center;">
    <a href="/file/reports/S9/Report_Stochastique_REOC.pdf" target="_blank">Open the stochastic processes report</a>
</p>

<hr>

<p><em>Course taken in 2024-2025 as part of the dual degree INSA Toulouse / ENSEEIHT, Master 2 REOC.</em></p>

</div>

<div class="back-nav">
    <a href="./my-courses-2024-2025.html" data-i18n-html="back-courses-2024-2025">&larr; Retour aux Cours 2024-2025</a>
</div>

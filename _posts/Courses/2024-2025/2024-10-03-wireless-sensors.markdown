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
    <a href="./my-courses-2024-2025.html" data-i18n-html="back-courses-2024-2025">&larr; Retour aux Cours 2024-2025</a>
</div>

<div class="lang-fr">

<h1>Wireless Sensors / WSNL - Semestre 9</h1>

<p><strong>Annee academique</strong> : 2024-2025<br>
<strong>Categorie</strong> : Reseaux de capteurs sans fil, IoT et telecommunications<br>
<strong>Enseignants</strong> : S. Abdellatif, D. Dragomirescu</p>

<hr>

<h2>PART A : PRESENTATION GENERALE</h2>

<h3 class="section-title">Vue d'ensemble</h3>

<p>Le cours "Wireless Sensor Networks and Localization" (WSNL) est un module central de la specialisation ISS (Innovative Smart Systems) en 5eme annee a l'INSA Toulouse. Ce cours explore en profondeur les principes fondamentaux des reseaux de capteurs sans fil (WSN), les protocoles de communication a faible consommation energetique, les techniques de modulation adaptees aux objets connectes, ainsi que les technologies LPWAN et les standards de communication comme ZigBee et Sigfox.</p>

<p><strong>Objectifs pedagogiques</strong> :</p>
<ul>
<li>Comprendre l'architecture des reseaux de capteurs sans fil et leurs contraintes specifiques</li>
<li>Analyser et evaluer les protocoles MAC dedies aux WSN (S-MAC, T-MAC, B-MAC, L-MAC, Z-MAC)</li>
<li>Maitriser les techniques de modulation a faible puissance pour les communications IoT</li>
<li>Etudier les piles protocolaires completes (ZigBee, Sigfox, LoRa)</li>
<li>Comprendre les architectures M2M sur reseaux cellulaires 4G LTE et 5G</li>
<li>Apprehender les principes du SDR (Software Defined Radio)</li>
<li>Concevoir des solutions de routage energetiquement efficaces</li>
<li>Developper une couche MAC en Python</li>
</ul>

<h3 class="section-title">Position dans le cursus</h3>

<p>Ce module fait le lien entre plusieurs domaines :</p>
<ul>
<li><strong>Wireless Communication (S8)</strong> : bases des communications sans fil</li>
<li><strong>Interconnexion Reseau (S8)</strong> : fondamentaux des protocoles reseaux</li>
<li><strong>Energy for Connected Objects (S9)</strong> : gestion energetique des noeuds capteurs</li>
<li><strong>Middleware for IoT (S9)</strong> : couches applicatives et integration IoT</li>
<li><strong>Security for Connected Objects (S9)</strong> : securisation des communications WSN</li>
<li><strong>5G Technologies (S9)</strong> : integration M2M dans les reseaux cellulaires</li>
</ul>

<hr>

<h2>PART B : EXPERIENCE ET CONTEXTE</h2>

<h3 class="section-title">Organisation et ressources</h3>

<p>Le module combinait cours magistraux, travaux pratiques et projets de recherche :</p>

<p><strong>Cours magistraux</strong> :</p>
<ul>
<li>Architecture des reseaux de capteurs sans fil (WSN)</li>
<li>Protocoles MAC pour WSN : S-MAC, T-MAC, B-MAC, L-MAC, Z-MAC</li>
<li>Techniques de modulation pour communications a faible puissance (DSSS, O-QPSK, BPSK, FSK)</li>
<li>Pile protocolaire ZigBee (IEEE 802.15.4)</li>
<li>Protocole Sigfox et technologies LPWAN</li>
<li>Communications M2M sur 4G LTE et 5G</li>
<li>Software Defined Radio (SDR) et GNU Radio</li>
<li>Routage econome en energie dans les WSN</li>
</ul>

<p><strong>Travaux pratiques</strong> :</p>
<ul>
<li><strong>TP MAC</strong> : Developpement d'une couche MAC en Python, gestion des paquets, acces au medium</li>
<li><strong>TP PHY</strong> : Introduction au SDR avec GNU Radio (couche physique)</li>
<li><strong>TP WSN</strong> : Mise en oeuvre d'un reseau de capteurs (Smart Subway)</li>
</ul>

<p><strong>Projets et rapports</strong> :</p>
<ul>
<li>Rapport d'analyse des protocoles MAC pour WSN</li>
<li>Etude du protocole Sigfox et des technologies LPWAN</li>
<li>Rapport sur le protocole ZigBee (WPAN pour WSN)</li>
<li>Etude M2M sur 4G LTE et 5G</li>
<li>Rapport TP WSN (Smart Subway)</li>
</ul>

<p><strong>Outils utilises</strong> :</p>
<ul>
<li><strong>Python</strong> : implementation de la couche MAC</li>
<li><strong>GNU Radio</strong> : plateforme SDR pour la couche physique</li>
<li><strong>IEEE 802.15.4</strong> : standard de reference pour les WSN</li>
</ul>

<h3 class="section-title">Methodologie d'etude</h3>

<p><strong>Phase 1 : Etude des protocoles existants</strong> :<br>
Analyse comparative des protocoles LoRa, ZigBee et Sigfox pour comprendre leurs specificites, avantages et cas d'usage.</p>

<p><strong>Phase 2 : Approfondissement des couches MAC</strong> :<br>
Etude detaillee de chaque protocole MAC (S-MAC, T-MAC, B-MAC, L-MAC, Z-MAC), comprenant les mecanismes de duty cycling, l'acces au medium et l'optimisation energetique.</p>

<p><strong>Phase 3 : Implementation pratique</strong> :<br>
Developpement d'une couche MAC en Python, permettant de comprendre concretement la gestion des trames, l'acces au canal et la coordination entre noeuds.</p>

<p><strong>Phase 4 : Etude des technologies LPWAN et cellulaires</strong> :<br>
Analyse des solutions Sigfox, LoRa et de l'integration M2M dans les reseaux 4G/5G.</p>

<h3 class="section-title">Difficultes rencontrees</h3>

<p><strong>Nombre de protocoles</strong> :<br>
La multiplicite des protocoles MAC, des standards et des technologies LPWAN rend l'assimilation complete difficile. Chaque protocole a ses propres mecanismes et compromis.</p>

<p><strong>Couche physique et SDR</strong> :<br>
Bien que le SDR ait ete aborde en cours, les sessions pratiques sur GNU Radio etaient limitees, ce qui a reduit l'experience pratique sur la couche physique.</p>

<p><strong>Compromis energetiques</strong> :<br>
Comprendre les differents compromis entre latence, debit, portee et consommation energetique pour chaque protocole necessite une analyse multi-criteres complexe.</p>

<hr>

<h2>PART C : ASPECTS TECHNIQUES</h2>

<p>Cette section explore en detail les aspects techniques des technologies WSN, en couvrant l'architecture des noeuds capteurs, les protocoles MAC, les techniques de modulation, les piles protocolaires ZigBee et Sigfox, le M2M cellulaire et le SDR.</p>

<h3 class="section-title">1. Architecture des reseaux de capteurs sans fil (WSN)</h3>

<p>Un reseau de capteurs sans fil (Wireless Sensor Network) est constitue d'un ensemble de noeuds capteurs autonomes, deployes pour surveiller des conditions physiques ou environnementales (temperature, pression, humidite, mouvement, etc.) et transmettre les donnees collectees a un noeud central (sink ou station de base).</p>

<p><strong>Architecture d'un noeud capteur</strong> :</p>

<p>Un noeud capteur typique se compose de quatre sous-systemes :</p>

<table>
<tr><th>Sous-systeme</th><th>Composants</th><th>Role</th></tr>
<tr><td>Capteur</td><td>Capteur(s) + ADC</td><td>Acquisition des donnees physiques</td></tr>
<tr><td>Traitement</td><td>Microcontroleur + memoire</td><td>Traitement local, protocoles, stockage</td></tr>
<tr><td>Communication</td><td>Emetteur-recepteur radio (transceiver)</td><td>Transmission/reception sans fil</td></tr>
<tr><td>Energie</td><td>Batterie + harvesting (optionnel)</td><td>Alimentation du noeud</td></tr>
</table>

<p><strong>Contraintes specifiques des WSN</strong> :</p>
<ul>
<li><strong>Energie limitee</strong> : les noeuds fonctionnent sur batterie, la consommation doit etre minimisee</li>
<li><strong>Bande passante reduite</strong> : debits faibles (250 kbps pour ZigBee, 100 bps pour Sigfox)</li>
<li><strong>Capacite de calcul limitee</strong> : microcontroleurs a faible puissance</li>
<li><strong>Deploiement a grande echelle</strong> : centaines ou milliers de noeuds</li>
<li><strong>Environnements hostiles</strong> : accessibilite limitee pour maintenance</li>
</ul>

<p><strong>Topologies de reseau WSN</strong> :</p>
<ul>
<li><strong>Etoile</strong> : tous les noeuds communiquent directement avec le sink (simple, portee limitee)</li>
<li><strong>Maille (mesh)</strong> : communication multi-saut, resilience aux pannes</li>
<li><strong>Arbre (cluster tree)</strong> : hierarchique, avec noeuds coordinateurs et noeuds feuilles</li>
<li><strong>Hybride</strong> : combinaison des topologies precedentes</li>
</ul>

<h3 class="section-title">2. Protocoles MAC pour WSN</h3>

<p>La couche MAC (Medium Access Control) est cruciale dans les WSN car elle gere l'acces au canal radio partage. L'objectif principal est de minimiser la consommation energetique tout en assurant une communication fiable.</p>

<p><strong>Sources de gaspillage energetique dans les WSN</strong> :</p>
<ul>
<li><strong>Idle listening</strong> : le transceiver reste allume en ecoute sans recevoir de donnees utiles</li>
<li><strong>Collisions</strong> : les retransmissions apres collision consomment de l'energie supplementaire</li>
<li><strong>Overhearing</strong> : reception de paquets destines a d'autres noeuds</li>
<li><strong>Overhead des protocoles</strong> : en-tetes et trames de controle</li>
</ul>

<p>Les protocoles MAC pour WSN se classent en trois categories : contention-based, schedule-based et hybrides.</p>

<h4>2.1 Protocoles a contention (Contention-Based)</h4>

<p><strong>S-MAC (Sensor-MAC)</strong></p>

<p>S-MAC est un protocole MAC a contention concu specifiquement pour les WSN. Il introduit le concept de <strong>duty cycling</strong> : les noeuds alternent entre periodes de sommeil (sleep) et periodes d'activite (listen/transmit) selon un planning synchronise.</p>

<p>Principes cles :</p>
<ul>
<li><strong>Planning synchronise</strong> : les noeuds voisins se synchronisent pour avoir les memes periodes d'activite</li>
<li><strong>Periodes de sommeil</strong> : reduction drastique de l'idle listening</li>
<li><strong>RTS/CTS</strong> : mecanisme de reservation du canal pour eviter les collisions</li>
<li><strong>Message passing</strong> : fragmentation des longs messages pour transmission efficace</li>
</ul>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_WSNL/S_MAC.png" alt="S-MAC : duty cycling synchronise avec periodes sleep/listen" style="max-width: 50%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">
        Figure : S-MAC - alternance synchronisee entre periodes de sommeil et d'activite
    </p>
</div>

<p>Avantages : reduction significative de l'idle listening, adapte aux applications avec trafic periodique.<br>
Inconvenients : latence accrue due aux periodes de sommeil, probleme du "sleep delay" en multi-saut.</p>

<p><strong>B-MAC (Berkeley-MAC)</strong></p>

<p>B-MAC est un protocole MAC a contention utilisant un mecanisme de <strong>preamble sampling</strong> (Low Power Listening). Plutot que de synchroniser les noeuds, chaque noeud echantillonne periodiquement le canal pour detecter un preambule.</p>

<p>Principes cles :</p>
<ul>
<li><strong>Preamble sampling</strong> : les noeuds se reveillent brievement a intervalles reguliers pour verifier l'activite du canal</li>
<li><strong>Long preambule</strong> : l'emetteur envoie un long preambule avant les donnees, garantissant que le recepteur detecte la transmission</li>
<li><strong>CCA (Clear Channel Assessment)</strong> : evaluation de l'etat du canal avant emission</li>
<li><strong>Pas de synchronisation</strong> : simplicite de mise en oeuvre</li>
</ul>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_WSNL/B_MAC.png" alt="B-MAC : preamble sampling et low power listening" style="max-width: 60%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">
        Figure : B-MAC - mecanisme de preamble sampling pour detecter les transmissions
    </p>
</div>

<p>Avantages : simple, pas de synchronisation requise, faible overhead.<br>
Inconvenients : long preambule consommant de l'energie, latence variable, overhead pour l'emetteur.</p>

<p><strong>T-MAC (Timeout-MAC)</strong></p>

<p>T-MAC est une amelioration de S-MAC qui adapte dynamiquement la duree des periodes d'activite. Quand aucun evenement n'est detecte pendant un timeout, le noeud retourne en sommeil plus tot.</p>

<p>Principes cles :</p>
<ul>
<li><strong>Timeout adaptatif</strong> : la periode active est raccourcie si aucune activite n'est detectee</li>
<li><strong>Meilleure adaptation</strong> : s'adapte au trafic variable (faible et fort)</li>
<li><strong>Early sleeping</strong> : les noeuds peuvent dormir plus longtemps en cas de faible trafic</li>
</ul>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_WSNL/T_MAC.png" alt="T-MAC : duty cycling adaptatif avec timeout" style="max-width: 60%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">
        Figure : T-MAC - adaptation dynamique de la periode active selon le trafic
    </p>
</div>

<p>Avantages : meilleure efficacite energetique que S-MAC en trafic variable.<br>
Inconvenients : probleme du "early sleeping" ou un noeud s'endort alors qu'un voisin veut lui transmettre.</p>

<h4>2.2 Protocoles planifies (Schedule-Based)</h4>

<p><strong>L-MAC (Lightweight-MAC)</strong></p>

<p>L-MAC est un protocole MAC base sur TDMA (Time Division Multiple Access) avec allocation decentralisee des slots temporels. Chaque noeud choisit son slot de maniere autonome, sans coordinateur central.</p>

<p>Principes cles :</p>
<ul>
<li><strong>TDMA decentralise</strong> : chaque noeud s'attribue un slot unique en ecoutant les slots deja occupes par ses voisins</li>
<li><strong>Pas de collision</strong> : acces deterministe au canal</li>
<li><strong>Scalabilite</strong> : allocation autonome des slots permettant l'ajout de noeuds</li>
</ul>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_WSNL/L_MAC.png" alt="L-MAC : TDMA decentralise avec allocation autonome des slots" style="max-width: 60%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">
        Figure : L-MAC - allocation decentralisee des slots TDMA
    </p>
</div>

<p>Avantages : pas de collision, deterministe, economie d'energie (pas d'idle listening pendant les slots des autres).<br>
Inconvenients : necessite synchronisation, moins flexible en cas de trafic variable, complexite d'allocation des slots.</p>

<h4>2.3 Protocoles hybrides</h4>

<p><strong>Z-MAC (Zebra-MAC)</strong></p>

<p>Z-MAC est un protocole hybride qui combine les avantages de CSMA (contention) et TDMA (schedule). Il s'adapte automatiquement aux conditions de trafic :</p>
<ul>
<li><strong>Faible trafic</strong> : fonctionne en mode CSMA (acces libre, faible latence)</li>
<li><strong>Fort trafic</strong> : bascule en mode TDMA (acces ordonne, pas de collision)</li>
</ul>

<p>Le noeud detecte le niveau de contention et choisit le mode le plus adapte. Cette adaptabilite rend Z-MAC performant dans les environnements dynamiques ou le trafic fluctue.</p>

<p><strong>Tableau comparatif des protocoles MAC</strong> :</p>

<table>
<tr><th>Protocole</th><th>Type</th><th>Duty cycling</th><th>Synchronisation</th><th>Latence</th><th>Energie</th><th>Scalabilite</th></tr>
<tr><td>S-MAC</td><td>Contention</td><td>Oui (fixe)</td><td>Oui</td><td>Moyenne</td><td>Bonne</td><td>Moyenne</td></tr>
<tr><td>B-MAC</td><td>Contention</td><td>Preamble sampling</td><td>Non</td><td>Variable</td><td>Bonne</td><td>Bonne</td></tr>
<tr><td>T-MAC</td><td>Contention</td><td>Oui (adaptatif)</td><td>Oui</td><td>Moyenne</td><td>Tres bonne</td><td>Moyenne</td></tr>
<tr><td>L-MAC</td><td>Schedule</td><td>TDMA</td><td>Oui</td><td>Faible</td><td>Tres bonne</td><td>Bonne</td></tr>
<tr><td>Z-MAC</td><td>Hybride</td><td>CSMA/TDMA</td><td>Oui</td><td>Adaptative</td><td>Tres bonne</td><td>Tres bonne</td></tr>
</table>

<h3 class="section-title">3. Techniques de modulation pour communications a faible puissance</h3>

<p>Les communications dans les WSN et les reseaux LPWAN utilisent des techniques de modulation specifiques, optimisees pour la faible consommation, la robustesse et la portee.</p>

<p><strong>Modulations de base pour WSN</strong> :</p>

<table>
<tr><th>Technique</th><th>Description</th><th>Usage</th></tr>
<tr><td>BPSK</td><td>Binary Phase Shift Keying - 1 bit par symbole</td><td>Sigfox, 868/915 MHz ZigBee</td></tr>
<tr><td>O-QPSK</td><td>Offset Quadrature PSK - 2 bits par symbole</td><td>ZigBee 2.4 GHz</td></tr>
<tr><td>FSK</td><td>Frequency Shift Keying - frequences distinctes</td><td>LoRa (base), Sigfox</td></tr>
<tr><td>GFSK</td><td>Gaussian FSK - transitions lissees</td><td>Bluetooth Low Energy</td></tr>
<tr><td>CSS</td><td>Chirp Spread Spectrum</td><td>LoRa</td></tr>
<tr><td>DSSS</td><td>Direct Sequence Spread Spectrum</td><td>ZigBee, 802.15.4</td></tr>
</table>

<p><strong>DSSS (Direct Sequence Spread Spectrum)</strong> :</p>

<p>Le DSSS est utilise par ZigBee (IEEE 802.15.4). Le principe consiste a etaler le signal sur une bande plus large que necessaire en multipliant les donnees par un code pseudo-aleatoire (PN sequence) a debit plus eleve (chip rate).</p>

<p>Avantages :</p>
<ul>
<li>Robustesse contre les interferences et le bruit</li>
<li>Resistance au multi-trajet (multipath fading)</li>
<li>Possibilite de partage de la bande (CDMA)</li>
<li>Faible densite spectrale de puissance (discretion)</li>
</ul>

<p><strong>Modulation pour LPWAN</strong> :</p>

<p>Les technologies LPWAN (Sigfox, LoRa) utilisent des modulations ultra-narrowband (UNB) ou a etalement de spectre pour maximiser la portee avec une puissance d'emission tres faible :</p>
<ul>
<li><strong>Sigfox</strong> : modulation DBPSK (Differential BPSK) sur bande ultra-etroite (100 Hz), permettant une portee de 10-50 km en zone rurale</li>
<li><strong>LoRa</strong> : modulation CSS (Chirp Spread Spectrum) avec facteur d'etalement variable (SF7 a SF12), compromis debit/portee/robustesse</li>
</ul>

<h3 class="section-title">4. Protocole Sigfox et technologies LPWAN</h3>

<p>Sigfox est un protocole LPWAN (Low Power Wide Area Network) concu pour les objets connectes necessitant une transmission de petites quantites de donnees sur de longues distances avec une tres faible consommation energetique.</p>

<p><strong>Caracteristiques de Sigfox</strong> :</p>

<table>
<tr><th>Parametre</th><th>Valeur</th></tr>
<tr><td>Bande de frequence</td><td>868 MHz (Europe), 915 MHz (USA)</td></tr>
<tr><td>Modulation</td><td>DBPSK (uplink), GFSK (downlink)</td></tr>
<tr><td>Largeur de canal</td><td>100 Hz (ultra-narrowband)</td></tr>
<tr><td>Debit</td><td>100 bps (uplink), 600 bps (downlink)</td></tr>
<tr><td>Taille max message</td><td>12 octets (uplink), 8 octets (downlink)</td></tr>
<tr><td>Messages/jour</td><td>140 (uplink), 4 (downlink)</td></tr>
<tr><td>Portee</td><td>10-50 km (rural), 3-10 km (urbain)</td></tr>
<tr><td>Consommation emission</td><td>~50 mW</td></tr>
<tr><td>Duree de vie batterie</td><td>10-15 ans (typique)</td></tr>
</table>

<p><strong>Architecture Sigfox</strong> :</p>
<ul>
<li>Les devices emettent des messages courts vers les stations de base Sigfox</li>
<li>Pas de negociation prealable (protocole unidirectionnel principalement)</li>
<li>Chaque message est emis 3 fois sur des frequences aleatoires (diversite frequentielle)</li>
<li>Le cloud Sigfox recoit et deduque les messages</li>
</ul>

<p><strong>Cas d'usage</strong> :</p>
<ul>
<li>Releve de compteurs (eau, gaz, electricite)</li>
<li>Suivi d'actifs (tracking logistique)</li>
<li>Surveillance environnementale</li>
<li>Alarmes et alertes</li>
<li>Agriculture de precision</li>
</ul>

<p><strong>Comparaison LPWAN</strong> :</p>

<table>
<tr><th>Critere</th><th>Sigfox</th><th>LoRa/LoRaWAN</th><th>NB-IoT</th></tr>
<tr><td>Spectre</td><td>Non licence (ISM)</td><td>Non licence (ISM)</td><td>Licence (LTE)</td></tr>
<tr><td>Portee</td><td>10-50 km</td><td>5-20 km</td><td>1-10 km</td></tr>
<tr><td>Debit</td><td>100 bps</td><td>0.3-50 kbps</td><td>200 kbps</td></tr>
<tr><td>Latence</td><td>Secondes</td><td>Secondes</td><td>1-10 s</td></tr>
<tr><td>Bidirectionnel</td><td>Limite</td><td>Oui</td><td>Oui</td></tr>
<tr><td>Infra</td><td>Operateur Sigfox</td><td>Prive ou operateur</td><td>Operateur telecom</td></tr>
<tr><td>Cout device</td><td>Tres faible</td><td>Faible</td><td>Moyen</td></tr>
</table>

<h3 class="section-title">5. Pile protocolaire ZigBee - PHY/MAC/NWK/APL</h3>

<p>ZigBee est un protocole de communication sans fil a faible puissance et faible debit, concu pour les applications IoT et WSN. Il repose sur le standard IEEE 802.15.4 pour les couches PHY et MAC, et ajoute les couches reseau (NWK) et application (APL).</p>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_WSNL/Zigbee_Layer.png" alt="Pile protocolaire ZigBee : couches PHY, MAC, NWK, APL" style="max-width: 40%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">
        Figure : Architecture en couches du protocole ZigBee
    </p>
</div>

<h4>5.1 Couche physique (PHY) - IEEE 802.15.4</h4>

<p>La couche PHY gere la modulation/demodulation des donnees et la transmission/reception des signaux radio.</p>

<p><strong>Bandes de frequence</strong> :</p>

<table>
<tr><th>Bande</th><th>Frequence</th><th>Canaux</th><th>Debit</th><th>Modulation</th><th>Region</th></tr>
<tr><td>2.4 GHz</td><td>2400-2483.5 MHz</td><td>16 (11-26)</td><td>250 kbps</td><td>O-QPSK + DSSS</td><td>Mondiale</td></tr>
<tr><td>915 MHz</td><td>902-928 MHz</td><td>10 (1-10)</td><td>40 kbps</td><td>BPSK + DSSS</td><td>Ameriques</td></tr>
<tr><td>868 MHz</td><td>868.0-868.6 MHz</td><td>1 (0)</td><td>20 kbps</td><td>BPSK + DSSS</td><td>Europe</td></tr>
</table>

<p><strong>Caracteristiques PHY</strong> :</p>
<ul>
<li><strong>Etalement de spectre DSSS</strong> : robustesse contre les interferences</li>
<li><strong>Puissance d'emission</strong> : typiquement -3 dBm a 20 dBm</li>
<li><strong>Sensibilite</strong> : -85 dBm (2.4 GHz), -92 dBm (868/915 MHz)</li>
<li><strong>Portee</strong> : 10-100 m en interieur, jusqu'a 1 km en exterieur (selon puissance et environnement)</li>
</ul>

<div style="text-align: center; display: flex; justify-content: center; margin: 20px 0;">
    <img src="/img/BE_WSNL/Zigbee_schema.png" style="max-width: 50%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <img src="/img/BE_WSNL/Zigbee_Graph.png" style="max-width: 50%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure : Schema de modulation ZigBee et representation spectrale du signal
</p>

<h4>5.2 Couche MAC - IEEE 802.15.4</h4>

<p>La couche MAC de ZigBee gere l'acces au canal et l'adressage des noeuds.</p>

<p><strong>Mecanisme d'acces au canal</strong> :</p>
<ul>
<li><strong>CSMA-CA</strong> (Carrier Sense Multiple Access with Collision Avoidance) : le noeud ecoute le canal avant d'emettre pour eviter les collisions</li>
<li><strong>Slotted CSMA-CA</strong> : en mode beacon-enabled, l'acces se fait dans des slots temporels synchronises</li>
<li><strong>Unslotted CSMA-CA</strong> : en mode non-beacon, acces asynchrone</li>
</ul>

<p><strong>Configurations reseau</strong> :</p>
<ul>
<li><strong>Beacon-enabled</strong> : le coordinateur emet des beacons periodiques pour synchroniser les noeuds. La supertrame est divisee en CAP (Contention Access Period) et CFP (Contention Free Period avec GTS)</li>
<li><strong>Non-beacon-enabled</strong> : les noeuds communiquent de maniere asynchrone, adapte pour les transmissions sporadiques</li>
</ul>

<p><strong>Securite MAC</strong> :</p>
<ul>
<li><strong>AES-128</strong> : chiffrement robuste des donnees transmises</li>
<li>Authentification et integrite des trames</li>
</ul>

<h4>5.3 Couche reseau (NWK)</h4>

<p>La couche NWK gere le routage des paquets et la topologie du reseau.</p>

<p><strong>Types de noeuds ZigBee</strong> :</p>
<ul>
<li><strong>ZigBee Coordinator (ZC)</strong> : un seul par reseau, initie la formation du reseau, attribue les adresses</li>
<li><strong>ZigBee Router (ZR)</strong> : relaye les paquets, etend la couverture</li>
<li><strong>ZigBee End Device (ZED)</strong> : noeud feuille, ne relaye pas, peut dormir pour economiser l'energie</li>
</ul>

<p><strong>Topologies supportees</strong> :</p>
<ul>
<li><strong>Etoile</strong> : tous les noeuds communiquent avec le coordinateur</li>
<li><strong>Arbre</strong> : structure hierarchique via les routeurs</li>
<li><strong>Maille</strong> : routage multi-saut entre routeurs pour la resilience</li>
</ul>

<p><strong>Routage</strong> :</p>
<ul>
<li>Algorithme AODV (Ad hoc On-demand Distance Vector) pour le routage en maille</li>
<li>Routage hierarchique en arbre</li>
</ul>

<h4>5.4 Couche application (APL)</h4>

<p>La couche APL comprend le framework applicatif ZigBee, incluant :</p>
<ul>
<li><strong>APS (Application Support Sub-Layer)</strong> : gestion des liaisons, decouverte de services</li>
<li><strong>ZDO (ZigBee Device Object)</strong> : gestion du reseau, securite, configuration</li>
<li><strong>Profils d'application</strong> : ZigBee Home Automation, ZigBee Light Link, ZigBee Smart Energy</li>
</ul>

<h3 class="section-title">6. M2M sur 4G LTE et 5G</h3>

<p>L'etude des communications Machine-to-Machine (M2M) sur les reseaux cellulaires 4G LTE et 5G est un aspect important du cours, reliant les WSN aux infrastructures de telecommunications globales.</p>

<p><strong>M2M sur 4G LTE</strong> :</p>

<p>Le LTE (Long Term Evolution) a ete adapte pour supporter les communications IoT/M2M avec :</p>
<ul>
<li><strong>LTE-M (LTE Cat-M1)</strong> : categorie de device optimisee pour l'IoT
    <ul>
    <li>Debit : 1 Mbps (downlink/uplink)</li>
    <li>Bande passante reduite : 1.4 MHz (vs 20 MHz pour LTE standard)</li>
    <li>Mode PSM (Power Saving Mode) pour economie d'energie</li>
    <li>Support de la mobilite et du handover</li>
    </ul>
</li>
<li><strong>NB-IoT (Narrowband IoT)</strong> : deploye dans la bande LTE
    <ul>
    <li>Bande passante : 200 kHz</li>
    <li>Debit : ~200 kbps</li>
    <li>Portee amelioree (+20 dB MCL vs LTE)</li>
    <li>Tres faible consommation</li>
    </ul>
</li>
</ul>

<p><strong>M2M sur 5G</strong> :</p>

<p>La 5G introduit des categories specifiques pour l'IoT :</p>
<ul>
<li><strong>mMTC (massive Machine Type Communications)</strong> : support de millions de devices par km2</li>
<li><strong>URLLC (Ultra-Reliable Low-Latency Communications)</strong> : latence &lt; 1 ms, fiabilite &gt; 99.999%</li>
<li><strong>Network Slicing</strong> : reseaux virtuels dedies par cas d'usage</li>
</ul>

<p><strong>Architecture M2M</strong> :</p>

<p>L'architecture M2M comprend :</p>
<ul>
<li><strong>Domain des devices</strong> : capteurs, actionneurs, gateways</li>
<li><strong>Domain du reseau</strong> : infrastructure d'acces (cellulaire, LPWAN) et coeur de reseau</li>
<li><strong>Domain des applications</strong> : plateformes cloud, traitement des donnees, services</li>
</ul>

<p><strong>Standards M2M</strong> :</p>
<ul>
<li><strong>oneM2M</strong> : standard de plateforme M2M/IoT interoperable</li>
<li><strong>ETSI M2M</strong> : architecture de reference europeenne</li>
<li><strong>3GPP</strong> : specifications pour LTE-M, NB-IoT, 5G mMTC</li>
</ul>

<h3 class="section-title">7. Routage econome en energie</h3>

<p>Le routage dans les WSN doit prendre en compte la contrainte energetique fondamentale. Plusieurs approches existent :</p>

<p><strong>Routage plat</strong> :</p>
<ul>
<li><strong>Flooding</strong> : chaque noeud retransmet a tous ses voisins (simple mais inefficace en energie)</li>
<li><strong>Gossiping</strong> : retransmission a un voisin aleatoire (reduction du trafic)</li>
<li><strong>Directed Diffusion</strong> : routage par requetes et gradients, elimine les transmissions inutiles</li>
</ul>

<p><strong>Routage hierarchique</strong> :</p>
<ul>
<li><strong>LEACH (Low-Energy Adaptive Clustering Hierarchy)</strong> : formation de clusters avec un cluster head tournant qui agregue les donnees avant transmission au sink</li>
<li><strong>TEEN (Threshold-sensitive Energy Efficient Network)</strong> : variante de LEACH pour applications reactives</li>
<li><strong>PEGASIS (Power-Efficient Gathering in Sensor Information Systems)</strong> : formation de chaines pour minimiser la distance de transmission</li>
</ul>

<p><strong>Criteres de selection de route</strong> :</p>
<ul>
<li>Energie residuelle des noeuds</li>
<li>Nombre de sauts</li>
<li>Qualite du lien (RSSI, taux d'erreur)</li>
<li>Latence</li>
<li>Equilibrage de charge energetique dans le reseau</li>
</ul>

<h3 class="section-title">8. SDR - Software Defined Radio</h3>

<p>Le SDR (Software Defined Radio) est un concept ou les fonctions de traitement du signal radio (modulation, demodulation, filtrage, codage) sont implementees en logiciel plutot qu'en materiel dedie.</p>

<p><strong>Principes du SDR</strong> :</p>
<ul>
<li>Numerisation du signal radio le plus tot possible dans la chaine de reception</li>
<li>Traitement numerique du signal (DSP) en logiciel</li>
<li>Flexibilite : changement de protocole par mise a jour logicielle</li>
<li>Plateforme generique pour experimenter differentes modulations</li>
</ul>

<p><strong>GNU Radio</strong> :</p>

<p>GNU Radio est une plateforme open-source pour le SDR. Elle permet de :</p>
<ul>
<li>Construire des chaines de traitement radio par blocs graphiques</li>
<li>Implementer et tester des modulations (BPSK, QPSK, FSK, OFDM)</li>
<li>Analyser des signaux en temps reel</li>
<li>Prototyper des systemes de communication</li>
</ul>

<p><strong>Application au cours</strong> :</p>

<p>Le sujet de TP SDR proposait d'implementer un emetteur-recepteur numerique en utilisant GNU Radio, permettant de comprendre concretement le fonctionnement de la couche physique des protocoles WSN.</p>

<h3 class="section-title">9. Architecture d'un noeud capteur - Details</h3>

<p><strong>Sous-systeme de communication</strong> :</p>

<p>Le transceiver radio est le composant le plus consommateur d'energie. Ses etats de fonctionnement sont :</p>
<ul>
<li><strong>Transmit (TX)</strong> : emission de donnees (consommation maximale)</li>
<li><strong>Receive (RX)</strong> : reception active (consommation elevee)</li>
<li><strong>Idle</strong> : ecoute du canal sans donnees (consommation significative)</li>
<li><strong>Sleep</strong> : mode veille profond (consommation minimale, quelques uA)</li>
</ul>

<p>Le duty cycling consiste a alterner entre les etats sleep et actif pour minimiser le temps passe en idle listening.</p>

<p><strong>Sous-systeme de traitement</strong> :</p>

<p>Les microcontroleurs utilises dans les WSN sont optimises pour la faible consommation :</p>
<ul>
<li>Architecture ARM Cortex-M (STM32, nRF52)</li>
<li>Modes de sommeil multiples (sleep, deep sleep, standby)</li>
<li>Peripheriques a faible puissance (ADC, SPI, UART)</li>
<li>Oscillateurs a faible courant</li>
</ul>

<p><strong>Sous-systeme d'energie</strong> :</p>

<p>Sources d'alimentation :</p>
<ul>
<li>Batteries primaires (non rechargeables) : longue duree de vie, capacite fixe</li>
<li>Batteries secondaires (rechargeables) : couplees avec energy harvesting</li>
<li>Energy harvesting : solaire, piezoelectrique, thermique, RF</li>
<li>Supercondensateurs : stockage temporaire pour pics de consommation</li>
</ul>

<hr>

<h2>PART D : ANALYSE ET REFLEXION</h2>

<h3 class="section-title">Competences acquises</h3>

<p><strong>Analyse et evaluation de protocoles WSN/IoT</strong> :<br>
Capacite a analyser et comparer les protocoles MAC (S-MAC, T-MAC, B-MAC, L-MAC, Z-MAC) en fonction de criteres comme la consommation energetique, la latence, la scalabilite et l'adaptation au trafic.</p>

<p><strong>Suggestion de solutions technologiques optimales</strong> :<br>
Aptitude a recommander les technologies de communication les plus adaptees (ZigBee, Sigfox, LoRa, NB-IoT, 5G) selon les contraintes du cas d'usage : portee, debit, consommation, cout, bidirectionnalite.</p>

<p><strong>Optimisation des protocoles de communication IoT</strong> :<br>
Comprehension des mecanismes de duty cycling, des techniques de modulation a faible puissance et des strategies de routage econome en energie.</p>

<p><strong>Comprehension des communications numeriques</strong> :<br>
Maitrise des techniques de modulation (DSSS, O-QPSK, BPSK, CSS), du fonctionnement d'un emetteur-recepteur RF numerique et des principes du SDR.</p>

<p><strong>Implementation pratique</strong> :<br>
Experience de developpement d'une couche MAC en Python, comprehension concrete de la gestion des trames et de l'acces au medium.</p>

<h3 class="section-title">Points cles a retenir</h3>

<p><strong>1. L'energie est la contrainte fondamentale des WSN</strong> :<br>
Tous les choix de conception (protocole MAC, routage, modulation, topologie) sont guides par la necessite de minimiser la consommation energetique pour prolonger la duree de vie du reseau.</p>

<p><strong>2. Le duty cycling est incontournable</strong> :<br>
Que ce soit par synchronisation (S-MAC, T-MAC) ou par preamble sampling (B-MAC), alterner entre sommeil et activite est la strategie cle pour economiser l'energie.</p>

<p><strong>3. Pas de protocole universel</strong> :<br>
Chaque protocole MAC a ses forces et faiblesses. Le choix depend du cas d'usage : trafic periodique ou evenementiel, densite du reseau, exigences de latence, topologie.</p>

<p><strong>4. Les technologies LPWAN completent les WSN</strong> :<br>
Sigfox et LoRa adressent les besoins de longue portee avec tres faible consommation, tandis que ZigBee est adapte aux reseaux a courte portee avec maillage.</p>

<p><strong>5. L'integration cellulaire (4G/5G) ouvre de nouvelles possibilites</strong> :<br>
LTE-M, NB-IoT et 5G mMTC permettent d'integrer les objets connectes dans l'infrastructure cellulaire existante, offrant couverture, QoS et interoperabilite.</p>

<h3 class="section-title">Retour d'experience</h3>

<p><strong>Premier travail - Etude comparative des protocoles</strong> :<br>
L'etude initiale de differents protocoles comme LoRa, ZigBee et Sigfox a ete enrichissante car elle m'a donne une vue d'ensemble de leur fonctionnement et des principaux protocoles qu'ils utilisent. Cette approche comparative permet de comprendre les compromis fondamentaux entre portee, debit, consommation et cout.</p>

<p><strong>Deuxieme partie - Analyse detaillee des protocoles MAC</strong> :<br>
L'etude approfondie de chaque protocole MAC m'a permis de comprendre les subtilites de ces protocoles : comment S-MAC gere la synchronisation, pourquoi B-MAC evite ce probleme avec le preamble sampling, comment T-MAC ameliore S-MAC avec le timeout adaptatif, et comment L-MAC garantit l'absence de collision avec le TDMA decentralise.</p>

<p><strong>Sessions de TP</strong> :<br>
Les travaux pratiques ont ete l'occasion de mettre en pratique les concepts etudies en cours. Le developpement de la couche MAC en Python m'a permis de voir concretement comment les paquets de donnees sont geres et transmis au sein d'un reseau. Cette experience pratique a renforce mes connaissances theoriques.</p>

<p><strong>Limites</strong> :<br>
Bien que le SDR ait ete aborde en cours avec GNU Radio, je n'ai pas eu de sessions dediees a la pratique du SDR, ce qui limite mon experience sur la couche physique. De plus, la multiplicite des protocoles rend difficile une maitrise complete de chacun d'entre eux. Avec l'experience professionnelle, je serai amene a approfondir davantage les protocoles pertinents a mon domaine d'activite.</p>

<h3 class="section-title">Mon avis</h3>

<p>Ce cours etait bien structure et m'a apporte une base solide en technologies WSN et localisation. L'approche progressive - d'abord l'etude comparative des protocoles, puis l'approfondissement des couches MAC, et enfin les travaux pratiques - est pedagogiquement efficace.</p>

<p>La diversite des sujets couverts (MAC pour WSN, ZigBee, Sigfox, M2M cellulaire, SDR) donne une vision complete de l'ecosysteme des communications pour objets connectes. Cette vision transversale est particulierement utile pour un ingenieur qui devra choisir les technologies les plus adaptees aux besoins specifiques de ses projets.</p>

<p>Je me sens desormais confiant dans ma capacite a analyser et optimiser des protocoles de communication pour l'IoT, tout en etant conscient que le domaine est vaste et en constante evolution.</p>

<hr>

<h2>Rapports et Projets</h2>

</div>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">Analyse de la couche MAC pour WSN</span>
        <span class="lang-en">MAC Layer Analysis for WSN</span>
      </h4>
      <p>
        <span class="lang-fr">Rapport detaille sur l'analyse comparative des protocoles MAC (S-MAC, T-MAC, B-MAC, L-MAC, Z-MAC) pour les reseaux de capteurs sans fil.</span>
        <span class="lang-en">Detailed report on the comparative analysis of MAC protocols (S-MAC, T-MAC, B-MAC, L-MAC, Z-MAC) for wireless sensor networks.</span>
      </p>
      <iframe src="/file/reports/S9/Chanfreau_MAC_Layer.pdf" width="100%" height="600px" style="overflow: auto;" frameborder="0"></iframe>
      <p><a href="/file/reports/S9/Chanfreau_MAC_Layer.pdf" target="_blank">
        <span class="lang-fr">Telecharger le rapport MAC Layer</span>
        <span class="lang-en">Download the MAC Layer report</span>
      </a></p>
    </div>
  </div>
</div>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">Etude du protocole Sigfox et LPWAN</span>
        <span class="lang-en">Sigfox Protocol and LPWAN Study</span>
      </h4>
      <p>
        <span class="lang-fr">Rapport sur le protocole Sigfox, les technologies LPWAN et leurs applications dans l'IoT.</span>
        <span class="lang-en">Report on the Sigfox protocol, LPWAN technologies and their applications in IoT.</span>
      </p>
      <iframe src="/file/reports/S9/Rapport_Sigfox.pdf" width="100%" height="600px" style="overflow: auto;" frameborder="0"></iframe>
      <p><a href="/file/reports/S9/Rapport_Sigfox.pdf" target="_blank">
        <span class="lang-fr">Telecharger le rapport Sigfox</span>
        <span class="lang-en">Download the Sigfox report</span>
      </a></p>
    </div>
  </div>
</div>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">TP WSN - Smart Subway</span>
        <span class="lang-en">WSN Lab - Smart Subway</span>
      </h4>
      <p>
        <span class="lang-fr">Rapport de travaux pratiques sur la mise en oeuvre d'un reseau de capteurs sans fil pour une application Smart Subway.</span>
        <span class="lang-en">Lab report on the implementation of a wireless sensor network for a Smart Subway application.</span>
      </p>
      <iframe src="/file/reports/S9/TP_WSN_REPORT.pdf" width="100%" height="600px" style="overflow: auto;" frameborder="0"></iframe>
      <p><a href="/file/reports/S9/TP_WSN_REPORT.pdf" target="_blank">
        <span class="lang-fr">Telecharger le rapport TP WSN</span>
        <span class="lang-en">Download the WSN lab report</span>
      </a></p>
    </div>
  </div>
</div>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">M2M sur 4G LTE et 5G</span>
        <span class="lang-en">M2M on 4G LTE and 5G</span>
      </h4>
      <p>
        <span class="lang-fr">Rapport sur les communications Machine-to-Machine sur les reseaux cellulaires 4G LTE et 5G, architectures et standards.</span>
        <span class="lang-en">Report on Machine-to-Machine communications over 4G LTE and 5G cellular networks, architectures and standards.</span>
      </p>
      <iframe src="/file/reports/S9/REPORT_M2M_on_4G_LTE_n_5G.pdf" width="100%" height="600px" style="overflow: auto;" frameborder="0"></iframe>
      <p><a href="/file/reports/S9/REPORT_M2M_on_4G_LTE_n_5G.pdf" target="_blank">
        <span class="lang-fr">Telecharger le rapport M2M</span>
        <span class="lang-en">Download the M2M report</span>
      </a></p>
    </div>
  </div>
</div>

<div class="lang-fr">

<hr>

<h2>Documents de Cours</h2>

</div>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">Polycopie WSN 2020</span>
        <span class="lang-en">WSN Course Booklet 2020</span>
      </h4>
      <p>
        <span class="lang-fr">Cours complet sur les reseaux de capteurs sans fil : architecture, protocoles MAC, routage, localisation.</span>
        <span class="lang-en">Complete course on wireless sensor networks: architecture, MAC protocols, routing, localization.</span>
      </p>
      <embed src="/cours-pdf/S9/WSNL/PolyWSN_2020.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/WSNL/PolyWSN_2020.pdf" target="_blank">
        <span class="lang-fr">Telecharger</span>
        <span class="lang-en">Download</span>
      </a></p>
    </div>
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">Modulations et MAC</span>
        <span class="lang-en">Modulations and MAC</span>
      </h4>
      <p>
        <span class="lang-fr">Cours sur les techniques de modulation pour les communications a faible puissance et les protocoles MAC pour WSN.</span>
        <span class="lang-en">Course on modulation techniques for low-power communications and MAC protocols for WSN.</span>
      </p>
      <embed src="/cours-pdf/S9/WSNL/Modulations_et_MAC.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/WSNL/Modulations_et_MAC.pdf" target="_blank">
        <span class="lang-fr">Telecharger</span>
        <span class="lang-en">Download</span>
      </a></p>
    </div>
  </div>
</div>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">SDR - Software Defined Radio (Sujet)</span>
        <span class="lang-en">SDR - Software Defined Radio (Subject)</span>
      </h4>
      <p>
        <span class="lang-fr">Sujet de TP sur le SDR : implementation d'un emetteur-recepteur numerique avec GNU Radio.</span>
        <span class="lang-en">Lab subject on SDR: implementation of a digital transceiver with GNU Radio.</span>
      </p>
      <embed src="/cours-pdf/S9/WSNL/2020-2021_5ISS_SDR_Sujet.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/WSNL/2020-2021_5ISS_SDR_Sujet.pdf" target="_blank">
        <span class="lang-fr">Telecharger</span>
        <span class="lang-en">Download</span>
      </a></p>
    </div>
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">BE M2M - Presentation</span>
        <span class="lang-en">M2M Lab - Presentation</span>
      </h4>
      <p>
        <span class="lang-fr">Presentation du bureau d'etude M2M : communications machine-to-machine sur reseaux cellulaires.</span>
        <span class="lang-en">M2M lab study presentation: machine-to-machine communications over cellular networks.</span>
      </p>
      <embed src="/cours-pdf/S9/WSNL/5ISS_BE_M2M_Presentation.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/WSNL/5ISS_BE_M2M_Presentation.pdf" target="_blank">
        <span class="lang-fr">Telecharger</span>
        <span class="lang-en">Download</span>
      </a></p>
    </div>
  </div>
</div>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">BE M2M - Sujet</span>
        <span class="lang-en">M2M Lab - Subject</span>
      </h4>
      <p>
        <span class="lang-fr">Sujet du bureau d'etude M2M sur 4G LTE et 5G.</span>
        <span class="lang-en">M2M lab study subject on 4G LTE and 5G.</span>
      </p>
      <embed src="/cours-pdf/S9/WSNL/2023_2024_5ISS_BE_M2M_Sujet.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/WSNL/2023_2024_5ISS_BE_M2M_Sujet.pdf" target="_blank">
        <span class="lang-fr">Telecharger</span>
        <span class="lang-en">Download</span>
      </a></p>
    </div>
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">FPGA pour systemes de communication</span>
        <span class="lang-en">FPGA for Communication Systems</span>
      </h4>
      <p>
        <span class="lang-fr">Article IEEE sur l'implementation FPGA pour les systemes de communication dans les WSN.</span>
        <span class="lang-en">IEEE article on FPGA implementation for communication systems in WSN.</span>
      </p>
      <embed src="/cours-pdf/S9/WSNL/ieee_circuitsandsystems_2021_FPGA.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/WSNL/ieee_circuitsandsystems_2021_FPGA.pdf" target="_blank">
        <span class="lang-fr">Telecharger</span>
        <span class="lang-en">Download</span>
      </a></p>
    </div>
  </div>
</div>

<div class="lang-fr">
<hr>
<p><em>Cours suivi en 2024-2025 a l'INSA Toulouse, Departement Genie Electrique et Informatique - Specialisation ISS (Innovative Smart Systems).</em></p>
</div>

<div class="lang-en">

<h1>Wireless Sensors / WSNL - Semester 9</h1>

<p><strong>Academic year</strong>: 2024-2025<br>
<strong>Category</strong>: Wireless sensor networks, IoT and telecommunications<br>
<strong>Instructors</strong>: S. Abdellatif, D. Dragomirescu</p>

<hr>

<h2>PART A: GENERAL PRESENTATION</h2>

<h3 class="section-title">Overview</h3>

<p>The "Wireless Sensor Networks and Localization" (WSNL) course is a core module of the ISS (Innovative Smart Systems) specialization in the 5th year at INSA Toulouse. This course explores in depth the fundamental principles of wireless sensor networks (WSN), low-power communication protocols, modulation techniques suited to connected objects, as well as LPWAN technologies and communication standards such as ZigBee and Sigfox.</p>

<p><strong>Learning objectives</strong>:</p>
<ul>
<li>Understand the architecture of wireless sensor networks and their specific constraints</li>
<li>Analyze and evaluate MAC protocols dedicated to WSN (S-MAC, T-MAC, B-MAC, L-MAC, Z-MAC)</li>
<li>Master low-power modulation techniques for IoT communications</li>
<li>Study complete protocol stacks (ZigBee, Sigfox, LoRa)</li>
<li>Understand M2M architectures on 4G LTE and 5G cellular networks</li>
<li>Grasp the principles of SDR (Software Defined Radio)</li>
<li>Design energy-efficient routing solutions</li>
<li>Develop a MAC layer in Python</li>
</ul>

<h3 class="section-title">Position in the curriculum</h3>

<p>This module bridges several domains:</p>
<ul>
<li><strong>Wireless Communication (S8)</strong>: wireless communication fundamentals</li>
<li><strong>Network Interconnection (S8)</strong>: network protocol fundamentals</li>
<li><strong>Energy for Connected Objects (S9)</strong>: energy management of sensor nodes</li>
<li><strong>Middleware for IoT (S9)</strong>: application layers and IoT integration</li>
<li><strong>Security for Connected Objects (S9)</strong>: securing WSN communications</li>
<li><strong>5G Technologies (S9)</strong>: M2M integration in cellular networks</li>
</ul>

<hr>

<h2>PART B: EXPERIENCE AND CONTEXT</h2>

<h3 class="section-title">Organization and resources</h3>

<p>The module combined lectures, lab sessions and research projects:</p>

<p><strong>Lectures</strong>:</p>
<ul>
<li>Wireless sensor network (WSN) architecture</li>
<li>MAC protocols for WSN: S-MAC, T-MAC, B-MAC, L-MAC, Z-MAC</li>
<li>Modulation techniques for low-power communications (DSSS, O-QPSK, BPSK, FSK)</li>
<li>ZigBee protocol stack (IEEE 802.15.4)</li>
<li>Sigfox protocol and LPWAN technologies</li>
<li>M2M communications on 4G LTE and 5G</li>
<li>Software Defined Radio (SDR) and GNU Radio</li>
<li>Energy-efficient routing in WSN</li>
</ul>

<p><strong>Lab sessions</strong>:</p>
<ul>
<li><strong>MAC Lab</strong>: Development of a MAC layer in Python, packet management, medium access</li>
<li><strong>PHY Lab</strong>: Introduction to SDR with GNU Radio (physical layer)</li>
<li><strong>WSN Lab</strong>: Implementation of a sensor network (Smart Subway)</li>
</ul>

<p><strong>Projects and reports</strong>:</p>
<ul>
<li>MAC protocol analysis report for WSN</li>
<li>Sigfox protocol and LPWAN technologies study</li>
<li>Report on the ZigBee protocol (WPAN for WSN)</li>
<li>M2M study on 4G LTE and 5G</li>
<li>WSN lab report (Smart Subway)</li>
</ul>

<p><strong>Tools used</strong>:</p>
<ul>
<li><strong>Python</strong>: MAC layer implementation</li>
<li><strong>GNU Radio</strong>: SDR platform for the physical layer</li>
<li><strong>IEEE 802.15.4</strong>: reference standard for WSN</li>
</ul>

<h3 class="section-title">Study methodology</h3>

<p><strong>Phase 1: Study of existing protocols</strong>:<br>
Comparative analysis of LoRa, ZigBee and Sigfox protocols to understand their specificities, advantages and use cases.</p>

<p><strong>Phase 2: In-depth study of MAC layers</strong>:<br>
Detailed study of each MAC protocol (S-MAC, T-MAC, B-MAC, L-MAC, Z-MAC), including duty cycling mechanisms, medium access and energy optimization.</p>

<p><strong>Phase 3: Practical implementation</strong>:<br>
Development of a MAC layer in Python, providing a concrete understanding of frame management, channel access and inter-node coordination.</p>

<p><strong>Phase 4: Study of LPWAN and cellular technologies</strong>:<br>
Analysis of Sigfox, LoRa solutions and M2M integration in 4G/5G networks.</p>

<h3 class="section-title">Challenges encountered</h3>

<p><strong>Number of protocols</strong>:<br>
The multiplicity of MAC protocols, standards and LPWAN technologies makes complete assimilation difficult. Each protocol has its own mechanisms and trade-offs.</p>

<p><strong>Physical layer and SDR</strong>:<br>
Although SDR was covered in lectures, the hands-on sessions on GNU Radio were limited, which reduced practical experience on the physical layer.</p>

<p><strong>Energy trade-offs</strong>:<br>
Understanding the different trade-offs between latency, throughput, range and energy consumption for each protocol requires complex multi-criteria analysis.</p>

<hr>

<h2>PART C: TECHNICAL ASPECTS</h2>

<p>This section explores in detail the technical aspects of WSN technologies, covering sensor node architecture, MAC protocols, modulation techniques, ZigBee and Sigfox protocol stacks, cellular M2M and SDR.</p>

<h3 class="section-title">1. Wireless Sensor Network (WSN) architecture</h3>

<p>A Wireless Sensor Network (WSN) consists of a set of autonomous sensor nodes, deployed to monitor physical or environmental conditions (temperature, pressure, humidity, motion, etc.) and transmit the collected data to a central node (sink or base station).</p>

<p><strong>Sensor node architecture</strong>:</p>

<p>A typical sensor node comprises four subsystems:</p>

<table>
<tr><th>Subsystem</th><th>Components</th><th>Role</th></tr>
<tr><td>Sensing</td><td>Sensor(s) + ADC</td><td>Physical data acquisition</td></tr>
<tr><td>Processing</td><td>Microcontroller + memory</td><td>Local processing, protocols, storage</td></tr>
<tr><td>Communication</td><td>Radio transceiver</td><td>Wireless transmission/reception</td></tr>
<tr><td>Energy</td><td>Battery + harvesting (optional)</td><td>Node power supply</td></tr>
</table>

<p><strong>WSN-specific constraints</strong>:</p>
<ul>
<li><strong>Limited energy</strong>: nodes run on batteries, consumption must be minimized</li>
<li><strong>Reduced bandwidth</strong>: low data rates (250 kbps for ZigBee, 100 bps for Sigfox)</li>
<li><strong>Limited computing capacity</strong>: low-power microcontrollers</li>
<li><strong>Large-scale deployment</strong>: hundreds or thousands of nodes</li>
<li><strong>Hostile environments</strong>: limited accessibility for maintenance</li>
</ul>

<p><strong>WSN network topologies</strong>:</p>
<ul>
<li><strong>Star</strong>: all nodes communicate directly with the sink (simple, limited range)</li>
<li><strong>Mesh</strong>: multi-hop communication, fault resilience</li>
<li><strong>Cluster tree</strong>: hierarchical, with coordinator nodes and leaf nodes</li>
<li><strong>Hybrid</strong>: combination of the above topologies</li>
</ul>

<h3 class="section-title">2. MAC protocols for WSN</h3>

<p>The MAC (Medium Access Control) layer is crucial in WSN as it manages access to the shared radio channel. The main objective is to minimize energy consumption while ensuring reliable communication.</p>

<p><strong>Sources of energy waste in WSN</strong>:</p>
<ul>
<li><strong>Idle listening</strong>: the transceiver remains on listening without receiving useful data</li>
<li><strong>Collisions</strong>: retransmissions after collisions consume additional energy</li>
<li><strong>Overhearing</strong>: reception of packets intended for other nodes</li>
<li><strong>Protocol overhead</strong>: headers and control frames</li>
</ul>

<p>MAC protocols for WSN fall into three categories: contention-based, schedule-based and hybrid.</p>

<h4>2.1 Contention-Based protocols</h4>

<p><strong>S-MAC (Sensor-MAC)</strong></p>

<p>S-MAC is a contention-based MAC protocol specifically designed for WSN. It introduces the concept of <strong>duty cycling</strong>: nodes alternate between sleep periods and active periods (listen/transmit) according to a synchronized schedule.</p>

<p>Key principles:</p>
<ul>
<li><strong>Synchronized schedule</strong>: neighboring nodes synchronize to share the same active periods</li>
<li><strong>Sleep periods</strong>: drastic reduction of idle listening</li>
<li><strong>RTS/CTS</strong>: channel reservation mechanism to avoid collisions</li>
<li><strong>Message passing</strong>: fragmentation of long messages for efficient transmission</li>
</ul>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_WSNL/S_MAC.png" alt="S-MAC: synchronized duty cycling with sleep/listen periods" style="max-width: 50%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">
        Figure: S-MAC - synchronized alternation between sleep and active periods
    </p>
</div>

<p>Advantages: significant reduction of idle listening, suited to applications with periodic traffic.<br>
Disadvantages: increased latency due to sleep periods, "sleep delay" problem in multi-hop.</p>

<p><strong>B-MAC (Berkeley-MAC)</strong></p>

<p>B-MAC is a contention-based MAC protocol using a <strong>preamble sampling</strong> mechanism (Low Power Listening). Rather than synchronizing nodes, each node periodically samples the channel to detect a preamble.</p>

<p>Key principles:</p>
<ul>
<li><strong>Preamble sampling</strong>: nodes briefly wake up at regular intervals to check channel activity</li>
<li><strong>Long preamble</strong>: the transmitter sends a long preamble before data, ensuring the receiver detects the transmission</li>
<li><strong>CCA (Clear Channel Assessment)</strong>: channel state evaluation before transmission</li>
<li><strong>No synchronization</strong>: simplicity of implementation</li>
</ul>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_WSNL/B_MAC.png" alt="B-MAC: preamble sampling and low power listening" style="max-width: 60%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">
        Figure: B-MAC - preamble sampling mechanism for detecting transmissions
    </p>
</div>

<p>Advantages: simple, no synchronization required, low overhead.<br>
Disadvantages: long preamble consuming energy, variable latency, overhead for the transmitter.</p>

<p><strong>T-MAC (Timeout-MAC)</strong></p>

<p>T-MAC is an improvement over S-MAC that dynamically adapts the duration of active periods. When no event is detected during a timeout, the node returns to sleep earlier.</p>

<p>Key principles:</p>
<ul>
<li><strong>Adaptive timeout</strong>: the active period is shortened if no activity is detected</li>
<li><strong>Better adaptation</strong>: adapts to variable traffic (low and high)</li>
<li><strong>Early sleeping</strong>: nodes can sleep longer during low traffic</li>
</ul>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_WSNL/T_MAC.png" alt="T-MAC: adaptive duty cycling with timeout" style="max-width: 60%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">
        Figure: T-MAC - dynamic adaptation of the active period based on traffic
    </p>
</div>

<p>Advantages: better energy efficiency than S-MAC under variable traffic.<br>
Disadvantages: "early sleeping" problem where a node falls asleep while a neighbor wants to transmit to it.</p>

<h4>2.2 Schedule-Based protocols</h4>

<p><strong>L-MAC (Lightweight-MAC)</strong></p>

<p>L-MAC is a MAC protocol based on TDMA (Time Division Multiple Access) with decentralized time slot allocation. Each node autonomously selects its slot, without a central coordinator.</p>

<p>Key principles:</p>
<ul>
<li><strong>Decentralized TDMA</strong>: each node assigns itself a unique slot by listening to slots already occupied by its neighbors</li>
<li><strong>No collisions</strong>: deterministic channel access</li>
<li><strong>Scalability</strong>: autonomous slot allocation allowing node addition</li>
</ul>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_WSNL/L_MAC.png" alt="L-MAC: decentralized TDMA with autonomous slot allocation" style="max-width: 60%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">
        Figure: L-MAC - decentralized TDMA slot allocation
    </p>
</div>

<p>Advantages: no collisions, deterministic, energy saving (no idle listening during other nodes' slots).<br>
Disadvantages: requires synchronization, less flexible under variable traffic, slot allocation complexity.</p>

<h4>2.3 Hybrid protocols</h4>

<p><strong>Z-MAC (Zebra-MAC)</strong></p>

<p>Z-MAC is a hybrid protocol that combines the advantages of CSMA (contention) and TDMA (schedule). It automatically adapts to traffic conditions:</p>
<ul>
<li><strong>Low traffic</strong>: operates in CSMA mode (free access, low latency)</li>
<li><strong>High traffic</strong>: switches to TDMA mode (ordered access, no collisions)</li>
</ul>

<p>The node detects the contention level and selects the most suitable mode. This adaptability makes Z-MAC efficient in dynamic environments where traffic fluctuates.</p>

<p><strong>Comparative table of MAC protocols</strong>:</p>

<table>
<tr><th>Protocol</th><th>Type</th><th>Duty cycling</th><th>Synchronization</th><th>Latency</th><th>Energy</th><th>Scalability</th></tr>
<tr><td>S-MAC</td><td>Contention</td><td>Yes (fixed)</td><td>Yes</td><td>Medium</td><td>Good</td><td>Medium</td></tr>
<tr><td>B-MAC</td><td>Contention</td><td>Preamble sampling</td><td>No</td><td>Variable</td><td>Good</td><td>Good</td></tr>
<tr><td>T-MAC</td><td>Contention</td><td>Yes (adaptive)</td><td>Yes</td><td>Medium</td><td>Very good</td><td>Medium</td></tr>
<tr><td>L-MAC</td><td>Schedule</td><td>TDMA</td><td>Yes</td><td>Low</td><td>Very good</td><td>Good</td></tr>
<tr><td>Z-MAC</td><td>Hybrid</td><td>CSMA/TDMA</td><td>Yes</td><td>Adaptive</td><td>Very good</td><td>Very good</td></tr>
</table>

<h3 class="section-title">3. Modulation techniques for low-power communications</h3>

<p>Communications in WSN and LPWAN networks use specific modulation techniques, optimized for low consumption, robustness and range.</p>

<p><strong>Basic modulations for WSN</strong>:</p>

<table>
<tr><th>Technique</th><th>Description</th><th>Usage</th></tr>
<tr><td>BPSK</td><td>Binary Phase Shift Keying - 1 bit per symbol</td><td>Sigfox, 868/915 MHz ZigBee</td></tr>
<tr><td>O-QPSK</td><td>Offset Quadrature PSK - 2 bits per symbol</td><td>ZigBee 2.4 GHz</td></tr>
<tr><td>FSK</td><td>Frequency Shift Keying - distinct frequencies</td><td>LoRa (base), Sigfox</td></tr>
<tr><td>GFSK</td><td>Gaussian FSK - smoothed transitions</td><td>Bluetooth Low Energy</td></tr>
<tr><td>CSS</td><td>Chirp Spread Spectrum</td><td>LoRa</td></tr>
<tr><td>DSSS</td><td>Direct Sequence Spread Spectrum</td><td>ZigBee, 802.15.4</td></tr>
</table>

<p><strong>DSSS (Direct Sequence Spread Spectrum)</strong>:</p>

<p>DSSS is used by ZigBee (IEEE 802.15.4). The principle consists of spreading the signal over a wider band than necessary by multiplying the data with a pseudo-random code (PN sequence) at a higher rate (chip rate).</p>

<p>Advantages:</p>
<ul>
<li>Robustness against interference and noise</li>
<li>Resistance to multipath fading</li>
<li>Possibility of band sharing (CDMA)</li>
<li>Low power spectral density (discretion)</li>
</ul>

<p><strong>LPWAN modulation</strong>:</p>

<p>LPWAN technologies (Sigfox, LoRa) use ultra-narrowband (UNB) or spread spectrum modulations to maximize range with very low transmit power:</p>
<ul>
<li><strong>Sigfox</strong>: DBPSK (Differential BPSK) modulation on ultra-narrowband (100 Hz), enabling a range of 10-50 km in rural areas</li>
<li><strong>LoRa</strong>: CSS (Chirp Spread Spectrum) modulation with variable spreading factor (SF7 to SF12), throughput/range/robustness trade-off</li>
</ul>

<h3 class="section-title">4. Sigfox protocol and LPWAN technologies</h3>

<p>Sigfox is an LPWAN (Low Power Wide Area Network) protocol designed for connected objects requiring transmission of small amounts of data over long distances with very low energy consumption.</p>

<p><strong>Sigfox characteristics</strong>:</p>

<table>
<tr><th>Parameter</th><th>Value</th></tr>
<tr><td>Frequency band</td><td>868 MHz (Europe), 915 MHz (USA)</td></tr>
<tr><td>Modulation</td><td>DBPSK (uplink), GFSK (downlink)</td></tr>
<tr><td>Channel width</td><td>100 Hz (ultra-narrowband)</td></tr>
<tr><td>Data rate</td><td>100 bps (uplink), 600 bps (downlink)</td></tr>
<tr><td>Max message size</td><td>12 bytes (uplink), 8 bytes (downlink)</td></tr>
<tr><td>Messages/day</td><td>140 (uplink), 4 (downlink)</td></tr>
<tr><td>Range</td><td>10-50 km (rural), 3-10 km (urban)</td></tr>
<tr><td>Transmit power consumption</td><td>~50 mW</td></tr>
<tr><td>Battery lifetime</td><td>10-15 years (typical)</td></tr>
</table>

<p><strong>Sigfox architecture</strong>:</p>
<ul>
<li>Devices send short messages to Sigfox base stations</li>
<li>No prior negotiation (primarily unidirectional protocol)</li>
<li>Each message is transmitted 3 times on random frequencies (frequency diversity)</li>
<li>The Sigfox cloud receives and deduplicates messages</li>
</ul>

<p><strong>Use cases</strong>:</p>
<ul>
<li>Meter reading (water, gas, electricity)</li>
<li>Asset tracking (logistics tracking)</li>
<li>Environmental monitoring</li>
<li>Alarms and alerts</li>
<li>Precision agriculture</li>
</ul>

<p><strong>LPWAN comparison</strong>:</p>

<table>
<tr><th>Criterion</th><th>Sigfox</th><th>LoRa/LoRaWAN</th><th>NB-IoT</th></tr>
<tr><td>Spectrum</td><td>Unlicensed (ISM)</td><td>Unlicensed (ISM)</td><td>Licensed (LTE)</td></tr>
<tr><td>Range</td><td>10-50 km</td><td>5-20 km</td><td>1-10 km</td></tr>
<tr><td>Data rate</td><td>100 bps</td><td>0.3-50 kbps</td><td>200 kbps</td></tr>
<tr><td>Latency</td><td>Seconds</td><td>Seconds</td><td>1-10 s</td></tr>
<tr><td>Bidirectional</td><td>Limited</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Infrastructure</td><td>Sigfox operator</td><td>Private or operator</td><td>Telecom operator</td></tr>
<tr><td>Device cost</td><td>Very low</td><td>Low</td><td>Medium</td></tr>
</table>

<h3 class="section-title">5. ZigBee protocol stack - PHY/MAC/NWK/APL</h3>

<p>ZigBee is a low-power, low-data-rate wireless communication protocol designed for IoT and WSN applications. It relies on the IEEE 802.15.4 standard for the PHY and MAC layers, and adds the network (NWK) and application (APL) layers.</p>

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/BE_WSNL/Zigbee_Layer.png" alt="ZigBee protocol stack: PHY, MAC, NWK, APL layers" style="max-width: 40%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <p style="font-style: italic; color: #666; margin-top: 10px;">
        Figure: ZigBee protocol layered architecture
    </p>
</div>

<h4>5.1 Physical layer (PHY) - IEEE 802.15.4</h4>

<p>The PHY layer handles data modulation/demodulation and radio signal transmission/reception.</p>

<p><strong>Frequency bands</strong>:</p>

<table>
<tr><th>Band</th><th>Frequency</th><th>Channels</th><th>Data rate</th><th>Modulation</th><th>Region</th></tr>
<tr><td>2.4 GHz</td><td>2400-2483.5 MHz</td><td>16 (11-26)</td><td>250 kbps</td><td>O-QPSK + DSSS</td><td>Worldwide</td></tr>
<tr><td>915 MHz</td><td>902-928 MHz</td><td>10 (1-10)</td><td>40 kbps</td><td>BPSK + DSSS</td><td>Americas</td></tr>
<tr><td>868 MHz</td><td>868.0-868.6 MHz</td><td>1 (0)</td><td>20 kbps</td><td>BPSK + DSSS</td><td>Europe</td></tr>
</table>

<p><strong>PHY characteristics</strong>:</p>
<ul>
<li><strong>DSSS spread spectrum</strong>: robustness against interference</li>
<li><strong>Transmit power</strong>: typically -3 dBm to 20 dBm</li>
<li><strong>Sensitivity</strong>: -85 dBm (2.4 GHz), -92 dBm (868/915 MHz)</li>
<li><strong>Range</strong>: 10-100 m indoors, up to 1 km outdoors (depending on power and environment)</li>
</ul>

<div style="text-align: center; display: flex; justify-content: center; margin: 20px 0;">
    <img src="/img/BE_WSNL/Zigbee_schema.png" style="max-width: 50%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
    <img src="/img/BE_WSNL/Zigbee_Graph.png" style="max-width: 50%; border: 1px solid #ddd; padding: 10px; border-radius: 8px; background: white;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure: ZigBee modulation scheme and signal spectral representation
</p>

<h4>5.2 MAC layer - IEEE 802.15.4</h4>

<p>The ZigBee MAC layer manages channel access and node addressing.</p>

<p><strong>Channel access mechanism</strong>:</p>
<ul>
<li><strong>CSMA-CA</strong> (Carrier Sense Multiple Access with Collision Avoidance): the node listens to the channel before transmitting to avoid collisions</li>
<li><strong>Slotted CSMA-CA</strong>: in beacon-enabled mode, access occurs in synchronized time slots</li>
<li><strong>Unslotted CSMA-CA</strong>: in non-beacon mode, asynchronous access</li>
</ul>

<p><strong>Network configurations</strong>:</p>
<ul>
<li><strong>Beacon-enabled</strong>: the coordinator emits periodic beacons to synchronize nodes. The superframe is divided into CAP (Contention Access Period) and CFP (Contention Free Period with GTS)</li>
<li><strong>Non-beacon-enabled</strong>: nodes communicate asynchronously, suited for sporadic transmissions</li>
</ul>

<p><strong>MAC security</strong>:</p>
<ul>
<li><strong>AES-128</strong>: robust encryption of transmitted data</li>
<li>Frame authentication and integrity</li>
</ul>

<h4>5.3 Network layer (NWK)</h4>

<p>The NWK layer manages packet routing and network topology.</p>

<p><strong>ZigBee node types</strong>:</p>
<ul>
<li><strong>ZigBee Coordinator (ZC)</strong>: only one per network, initiates network formation, assigns addresses</li>
<li><strong>ZigBee Router (ZR)</strong>: relays packets, extends coverage</li>
<li><strong>ZigBee End Device (ZED)</strong>: leaf node, does not relay, can sleep to save energy</li>
</ul>

<p><strong>Supported topologies</strong>:</p>
<ul>
<li><strong>Star</strong>: all nodes communicate with the coordinator</li>
<li><strong>Tree</strong>: hierarchical structure via routers</li>
<li><strong>Mesh</strong>: multi-hop routing between routers for resilience</li>
</ul>

<p><strong>Routing</strong>:</p>
<ul>
<li>AODV algorithm (Ad hoc On-demand Distance Vector) for mesh routing</li>
<li>Hierarchical tree routing</li>
</ul>

<h4>5.4 Application layer (APL)</h4>

<p>The APL layer includes the ZigBee application framework, including:</p>
<ul>
<li><strong>APS (Application Support Sub-Layer)</strong>: binding management, service discovery</li>
<li><strong>ZDO (ZigBee Device Object)</strong>: network management, security, configuration</li>
<li><strong>Application profiles</strong>: ZigBee Home Automation, ZigBee Light Link, ZigBee Smart Energy</li>
</ul>

<h3 class="section-title">6. M2M on 4G LTE and 5G</h3>

<p>The study of Machine-to-Machine (M2M) communications on 4G LTE and 5G cellular networks is an important aspect of the course, linking WSN to global telecommunications infrastructures.</p>

<p><strong>M2M on 4G LTE</strong>:</p>

<p>LTE (Long Term Evolution) has been adapted to support IoT/M2M communications with:</p>
<ul>
<li><strong>LTE-M (LTE Cat-M1)</strong>: device category optimized for IoT
    <ul>
    <li>Data rate: 1 Mbps (downlink/uplink)</li>
    <li>Reduced bandwidth: 1.4 MHz (vs 20 MHz for standard LTE)</li>
    <li>PSM mode (Power Saving Mode) for energy savings</li>
    <li>Mobility and handover support</li>
    </ul>
</li>
<li><strong>NB-IoT (Narrowband IoT)</strong>: deployed in the LTE band
    <ul>
    <li>Bandwidth: 200 kHz</li>
    <li>Data rate: ~200 kbps</li>
    <li>Improved range (+20 dB MCL vs LTE)</li>
    <li>Very low power consumption</li>
    </ul>
</li>
</ul>

<p><strong>M2M on 5G</strong>:</p>

<p>5G introduces specific categories for IoT:</p>
<ul>
<li><strong>mMTC (massive Machine Type Communications)</strong>: support for millions of devices per km2</li>
<li><strong>URLLC (Ultra-Reliable Low-Latency Communications)</strong>: latency &lt; 1 ms, reliability &gt; 99.999%</li>
<li><strong>Network Slicing</strong>: dedicated virtual networks per use case</li>
</ul>

<p><strong>M2M architecture</strong>:</p>

<p>The M2M architecture comprises:</p>
<ul>
<li><strong>Device domain</strong>: sensors, actuators, gateways</li>
<li><strong>Network domain</strong>: access infrastructure (cellular, LPWAN) and core network</li>
<li><strong>Application domain</strong>: cloud platforms, data processing, services</li>
</ul>

<p><strong>M2M standards</strong>:</p>
<ul>
<li><strong>oneM2M</strong>: interoperable M2M/IoT platform standard</li>
<li><strong>ETSI M2M</strong>: European reference architecture</li>
<li><strong>3GPP</strong>: specifications for LTE-M, NB-IoT, 5G mMTC</li>
</ul>

<h3 class="section-title">7. Energy-efficient routing</h3>

<p>Routing in WSN must take into account the fundamental energy constraint. Several approaches exist:</p>

<p><strong>Flat routing</strong>:</p>
<ul>
<li><strong>Flooding</strong>: each node retransmits to all its neighbors (simple but energy-inefficient)</li>
<li><strong>Gossiping</strong>: retransmission to a random neighbor (traffic reduction)</li>
<li><strong>Directed Diffusion</strong>: query and gradient-based routing, eliminates unnecessary transmissions</li>
</ul>

<p><strong>Hierarchical routing</strong>:</p>
<ul>
<li><strong>LEACH (Low-Energy Adaptive Clustering Hierarchy)</strong>: cluster formation with a rotating cluster head that aggregates data before transmission to the sink</li>
<li><strong>TEEN (Threshold-sensitive Energy Efficient Network)</strong>: LEACH variant for reactive applications</li>
<li><strong>PEGASIS (Power-Efficient Gathering in Sensor Information Systems)</strong>: chain formation to minimize transmission distance</li>
</ul>

<p><strong>Route selection criteria</strong>:</p>
<ul>
<li>Residual energy of nodes</li>
<li>Number of hops</li>
<li>Link quality (RSSI, error rate)</li>
<li>Latency</li>
<li>Energy load balancing in the network</li>
</ul>

<h3 class="section-title">8. SDR - Software Defined Radio</h3>

<p>SDR (Software Defined Radio) is a concept where radio signal processing functions (modulation, demodulation, filtering, coding) are implemented in software rather than in dedicated hardware.</p>

<p><strong>SDR principles</strong>:</p>
<ul>
<li>Digitizing the radio signal as early as possible in the reception chain</li>
<li>Digital Signal Processing (DSP) in software</li>
<li>Flexibility: protocol change through software update</li>
<li>Generic platform for experimenting with different modulations</li>
</ul>

<p><strong>GNU Radio</strong>:</p>

<p>GNU Radio is an open-source platform for SDR. It allows:</p>
<ul>
<li>Building radio processing chains using graphical blocks</li>
<li>Implementing and testing modulations (BPSK, QPSK, FSK, OFDM)</li>
<li>Analyzing signals in real time</li>
<li>Prototyping communication systems</li>
</ul>

<p><strong>Application to the course</strong>:</p>

<p>The SDR lab subject proposed implementing a digital transceiver using GNU Radio, providing a concrete understanding of how the physical layer of WSN protocols works.</p>

<h3 class="section-title">9. Sensor node architecture - Details</h3>

<p><strong>Communication subsystem</strong>:</p>

<p>The radio transceiver is the most energy-consuming component. Its operating states are:</p>
<ul>
<li><strong>Transmit (TX)</strong>: data transmission (maximum consumption)</li>
<li><strong>Receive (RX)</strong>: active reception (high consumption)</li>
<li><strong>Idle</strong>: channel listening without data (significant consumption)</li>
<li><strong>Sleep</strong>: deep sleep mode (minimum consumption, a few uA)</li>
</ul>

<p>Duty cycling consists of alternating between sleep and active states to minimize the time spent in idle listening.</p>

<p><strong>Processing subsystem</strong>:</p>

<p>Microcontrollers used in WSN are optimized for low consumption:</p>
<ul>
<li>ARM Cortex-M architecture (STM32, nRF52)</li>
<li>Multiple sleep modes (sleep, deep sleep, standby)</li>
<li>Low-power peripherals (ADC, SPI, UART)</li>
<li>Low-current oscillators</li>
</ul>

<p><strong>Energy subsystem</strong>:</p>

<p>Power sources:</p>
<ul>
<li>Primary batteries (non-rechargeable): long lifetime, fixed capacity</li>
<li>Secondary batteries (rechargeable): coupled with energy harvesting</li>
<li>Energy harvesting: solar, piezoelectric, thermal, RF</li>
<li>Supercapacitors: temporary storage for consumption peaks</li>
</ul>

<hr>

<h2>PART D: ANALYSIS AND REFLECTION</h2>

<h3 class="section-title">Skills acquired</h3>

<p><strong>WSN/IoT protocol analysis and evaluation</strong>:<br>
Ability to analyze and compare MAC protocols (S-MAC, T-MAC, B-MAC, L-MAC, Z-MAC) based on criteria such as energy consumption, latency, scalability and traffic adaptation.</p>

<p><strong>Recommendation of optimal technological solutions</strong>:<br>
Ability to recommend the most suitable communication technologies (ZigBee, Sigfox, LoRa, NB-IoT, 5G) according to use case constraints: range, throughput, consumption, cost, bidirectionality.</p>

<p><strong>IoT communication protocol optimization</strong>:<br>
Understanding of duty cycling mechanisms, low-power modulation techniques and energy-efficient routing strategies.</p>

<p><strong>Digital communications understanding</strong>:<br>
Mastery of modulation techniques (DSSS, O-QPSK, BPSK, CSS), digital RF transceiver operation and SDR principles.</p>

<p><strong>Practical implementation</strong>:<br>
Experience developing a MAC layer in Python, concrete understanding of frame management and medium access.</p>

<h3 class="section-title">Key takeaways</h3>

<p><strong>1. Energy is the fundamental constraint of WSN</strong>:<br>
All design choices (MAC protocol, routing, modulation, topology) are guided by the need to minimize energy consumption to extend network lifetime.</p>

<p><strong>2. Duty cycling is essential</strong>:<br>
Whether through synchronization (S-MAC, T-MAC) or preamble sampling (B-MAC), alternating between sleep and activity is the key strategy for saving energy.</p>

<p><strong>3. There is no universal protocol</strong>:<br>
Each MAC protocol has its strengths and weaknesses. The choice depends on the use case: periodic or event-driven traffic, network density, latency requirements, topology.</p>

<p><strong>4. LPWAN technologies complement WSN</strong>:<br>
Sigfox and LoRa address the needs for long range with very low consumption, while ZigBee is suited to short-range networks with mesh capabilities.</p>

<p><strong>5. Cellular integration (4G/5G) opens new possibilities</strong>:<br>
LTE-M, NB-IoT and 5G mMTC enable the integration of connected objects into existing cellular infrastructure, offering coverage, QoS and interoperability.</p>

<h3 class="section-title">Feedback</h3>

<p><strong>First assignment - Comparative protocol study</strong>:<br>
The initial study of different protocols such as LoRa, ZigBee and Sigfox was enriching because it gave me an overview of their operation and the main protocols they use. This comparative approach allows understanding the fundamental trade-offs between range, throughput, consumption and cost.</p>

<p><strong>Second part - Detailed MAC protocol analysis</strong>:<br>
The in-depth study of each MAC protocol allowed me to understand the subtleties of these protocols: how S-MAC manages synchronization, why B-MAC avoids this problem with preamble sampling, how T-MAC improves S-MAC with adaptive timeout, and how L-MAC guarantees collision-free operation with decentralized TDMA.</p>

<p><strong>Lab sessions</strong>:<br>
The lab sessions were an opportunity to put into practice the concepts studied in lectures. Developing the MAC layer in Python allowed me to concretely see how data packets are managed and transmitted within a network. This hands-on experience reinforced my theoretical knowledge.</p>

<p><strong>Limitations</strong>:<br>
Although SDR was covered in lectures with GNU Radio, I did not have dedicated sessions to practice SDR, which limits my experience on the physical layer. Additionally, the multiplicity of protocols makes complete mastery of each one difficult. With professional experience, I will be able to deepen my knowledge of the protocols relevant to my field of activity.</p>

<h3 class="section-title">My opinion</h3>

<p>This course was well structured and gave me a solid foundation in WSN and localization technologies. The progressive approach - first the comparative study of protocols, then the in-depth study of MAC layers, and finally the lab sessions - is pedagogically effective.</p>

<p>The diversity of topics covered (MAC for WSN, ZigBee, Sigfox, cellular M2M, SDR) provides a comprehensive view of the communication ecosystem for connected objects. This cross-cutting vision is particularly useful for an engineer who will need to choose the most suitable technologies for the specific needs of their projects.</p>

<p>I now feel confident in my ability to analyze and optimize communication protocols for IoT, while being aware that the field is vast and constantly evolving.</p>

<hr>

<h2>Reports and Projects</h2>

<h2>Course Documents</h2>

<hr>

<p><em>Course taken in 2024-2025 at INSA Toulouse, Department of Electrical and Computer Engineering - ISS specialization (Innovative Smart Systems).</em></p>

</div>

<div class="back-nav">
    <a href="./my-courses-2024-2025.html" data-i18n-html="back-courses-2024-2025">&larr; Retour aux Cours 2024-2025</a>
</div>

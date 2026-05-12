---
layout: default
title:  "Network & Sysadmin Training"
date:   2025-01-01 10:00:00 +0200
---

<style>
p { text-align: justify; }
h2 { border-bottom: 2px solid #ccc; padding-bottom: 4px; margin-top: 2.5rem; }
h3 { margin-top: 1.8rem; color: #333; }
table { border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.9rem; }
th, td { border: 1px solid #ddd; padding: 6px 10px; }
th { background: #f0f0f0; }
.tip { background: #e8f5e9; border-left: 4px solid #4caf50; padding: 8px 12px; margin: 1rem 0; font-size: 0.9rem; }
.warn { background: #fff3e0; border-left: 4px solid #ff9800; padding: 8px 12px; margin: 1rem 0; font-size: 0.9rem; }
.danger { background: #fce4ec; border-left: 4px solid #f44336; padding: 8px 12px; margin: 1rem 0; font-size: 0.9rem; }
</style>

<div class="back-nav">
    <a href="./my-perso-projects.html" data-i18n-html="back-perso-projects">&larr; Retour aux Projets Personnels</a>
</div>

<!-- ==================== FRENCH ==================== -->
<div class="lang-fr">

<h1>Cours Administrateur Systemes &amp; Reseaux</h1>

<p>Notes de cours completes couvrant l'ensemble des notions d'administration systemes et reseaux niveau junior/intermediaire. Contexte : infrastructure d'une mission diplomatique internationale (~300 postes, Windows/Linux, VLANs segmentes, VPN multi-sites).</p>

<nav>
<strong>Sommaire :</strong>
<a href="#osi">OSI</a> &bull;
<a href="#tcpudp">TCP/UDP</a> &bull;
<a href="#ipv4">IPv4/Subnetting</a> &bull;
<a href="#arp">ARP/ICMP</a> &bull;
<a href="#dhcp">DHCP</a> &bull;
<a href="#dns">DNS</a> &bull;
<a href="#nat">NAT/PAT</a> &bull;
<a href="#vlan">VLAN/STP</a> &bull;
<a href="#routing">Routage</a> &bull;
<a href="#firewall">Firewall</a> &bull;
<a href="#ports">Ports</a> &bull;
<a href="#vpn">VPN</a> &bull;
<a href="#secu">Cybersecurite</a> &bull;
<a href="#ad">Active Directory</a> &bull;
<a href="#linux">Linux/SSH</a> &bull;
<a href="#powershell">PowerShell</a> &bull;
<a href="#trouble">Troubleshooting</a> &bull;
<a href="#wireshark">Wireshark</a> &bull;
<a href="#virt">Virtualisation</a> &bull;
<a href="#cmds">Reference commandes</a>
</nav>

<!-- ======================================================== -->
<h2 id="osi">1. Modele OSI</h2>

<p>Le modele OSI decoupe les communications reseau en 7 couches independantes. Il n'est pas implemente directement mais sert de reference pour comprendre les protocoles et diagnostiquer les pannes (methode "bottom-up").</p>

<table>
<tr><th>Couche</th><th>Nom</th><th>PDU</th><th>Protocoles / Equipements</th><th>Role</th></tr>
<tr><td>7</td><td>Application</td><td>Donnees</td><td>HTTP, HTTPS, FTP, DNS, SMTP, DHCP</td><td>Interface utilisateur</td></tr>
<tr><td>6</td><td>Presentation</td><td>Donnees</td><td>SSL/TLS, JPEG, ASCII, chiffrement</td><td>Traduction, compression</td></tr>
<tr><td>5</td><td>Session</td><td>Donnees</td><td>NetBIOS, RPC, SQL</td><td>Etablissement / fermeture sessions</td></tr>
<tr><td>4</td><td>Transport</td><td>Segment / Datagramme</td><td>TCP (fiable), UDP (rapide)</td><td>Transport de bout en bout</td></tr>
<tr><td>3</td><td>Reseau</td><td>Paquet</td><td>IP, ICMP, OSPF &rarr; Routeur</td><td>Adressage et routage</td></tr>
<tr><td>2</td><td>Liaison</td><td>Trame (Frame)</td><td>Ethernet, 802.1Q, WiFi &rarr; Switch L2</td><td>Acces au support, adresses MAC</td></tr>
<tr><td>1</td><td>Physique</td><td>Bit</td><td>RJ45, fibre optique, WiFi &rarr; Hub, repeteur</td><td>Signal electrique/optique</td></tr>
</table>

<div class="tip"><strong>Mnemonique (bas vers haut) :</strong> "Please Do Not Throw Sausage Pizza Away" &rarr; Physical, Data Link, Network, Transport, Session, Presentation, Application.</div>

<p><strong>Pieges frequents :</strong> ARP peut etre classe L2 ou L3 selon les auteurs (il fait le lien entre les deux). Les firewalls peuvent operer de L3 a L7. SSL/TLS est L5/L6 selon l'implementation.</p>

<p><strong>Diagnostic par couche (bottom-up) :</strong></p>
<ol>
<li><strong>L1 Physique</strong> : cable branche ? voyant switch allume ? tester avec un autre cable.</li>
<li><strong>L2 Liaison</strong> : adresse MAC visible dans ARP ? VLAN correct ? port switch configure ?</li>
<li><strong>L3 Reseau</strong> : IP correcte ? masque correct ? passerelle configuree ? route valide ?</li>
<li><strong>L4 Transport</strong> : port TCP/UDP ouvert ? firewall bloque ? service tourne ?</li>
<li><strong>L7 Application</strong> : service demarre ? configuration correcte ? logs d'erreurs ?</li>
</ol>

<!-- ======================================================== -->
<h2 id="tcpudp">2. TCP et UDP</h2>

<h3>TCP (Transmission Control Protocol)</h3>
<p>Protocole oriente connexion, fiable. Garantit la livraison des donnees dans l'ordre, avec retransmission en cas de perte. Usage : HTTP, HTTPS, SSH, FTP, SMTP, SMB.</p>

<p><strong>Etablissement de connexion &mdash; 3-Way Handshake :</strong></p>
<pre><code>Client                    Serveur
  |---- SYN (seq=x) -------->|   Client initie la connexion
  |<--- SYN-ACK (seq=y) -----|   Serveur accepte et acquitte
  |---- ACK (ack=y+1) ------>|   Client confirme
  |    [Connexion etablie]   |
</code></pre>

<p><strong>Fermeture de connexion :</strong> 4 etapes (FIN / ACK / FIN / ACK) &mdash; fermeture gracieuse des deux cotes.</p>

<h3>UDP (User Datagram Protocol)</h3>
<p>Protocole sans connexion, non fiable. Envoie les datagrammes sans accuse de reception ni garantie d'ordre. Beaucoup plus rapide que TCP car pas de handshake ni de controle de flux. Usage : DNS, DHCP, streaming video, VoIP, gaming, SNMP, NTP.</p>

<table>
<tr><th></th><th>TCP</th><th>UDP</th></tr>
<tr><td>Connexion</td><td>Oriente connexion (3-way handshake)</td><td>Sans connexion</td></tr>
<tr><td>Fiabilite</td><td>Garantie (retransmission, ordre)</td><td>Aucune</td></tr>
<tr><td>Vitesse</td><td>Plus lent (overhead)</td><td>Plus rapide</td></tr>
<tr><td>Usage</td><td>HTTP, SSH, FTP, SMTP, SMB</td><td>DNS, DHCP, VoIP, streaming</td></tr>
</table>

<!-- ======================================================== -->
<h2 id="ipv4">3. IPv4 / CIDR / Subnetting</h2>

<h3>Adresses speciales</h3>
<table>
<tr><th>Adresse</th><th>Role</th></tr>
<tr><td>127.0.0.1</td><td>Loopback &mdash; teste la pile TCP/IP locale, ne sort pas sur le reseau</td></tr>
<tr><td>169.254.x.x</td><td>APIPA &mdash; le DHCP a echoue, adresse auto-assignee</td></tr>
<tr><td>0.0.0.0</td><td>Route par defaut / adresse non configuree</td></tr>
<tr><td>255.255.255.255</td><td>Broadcast limite (tout le segment)</td></tr>
</table>

<h3>Plages privees RFC 1918</h3>
<table>
<tr><th>Plage</th><th>CIDR</th><th>Hotes max</th><th>Usage typique</th></tr>
<tr><td>10.0.0.0 &ndash; 10.255.255.255</td><td>/8</td><td>~16 millions</td><td>Grandes entreprises, datacenters</td></tr>
<tr><td>172.16.0.0 &ndash; 172.31.255.255</td><td>/12</td><td>~1 million</td><td>Entreprises moyennes</td></tr>
<tr><td>192.168.0.0 &ndash; 192.168.255.255</td><td>/16</td><td>~65 000</td><td>Domicile, petites entreprises</td></tr>
</table>

<h3>Calcul de sous-reseaux (Subnetting)</h3>
<pre><code>Bits hotes    = 32 - prefixe CIDR
Total adresses = 2^(bits hotes)
Hotes utilisables = 2^(bits hotes) - 2  (reseau + broadcast exclus)
</code></pre>

<table>
<tr><th>CIDR</th><th>Masque</th><th>Hotes utilisables</th><th>Usage typique</th></tr>
<tr><td>/24</td><td>255.255.255.0</td><td>254</td><td>LAN standard</td></tr>
<tr><td>/25</td><td>255.255.255.128</td><td>126</td><td>Sous-reseau moyen</td></tr>
<tr><td>/26</td><td>255.255.255.192</td><td>62</td><td>~60 hotes</td></tr>
<tr><td>/27</td><td>255.255.255.224</td><td>30</td><td>~30 hotes</td></tr>
<tr><td>/28</td><td>255.255.255.240</td><td>14</td><td>Petit segment</td></tr>
<tr><td>/29</td><td>255.255.255.248</td><td>6</td><td>DMZ, petits groupes</td></tr>
<tr><td>/30</td><td>255.255.255.252</td><td>2</td><td>Liaison point-a-point WAN</td></tr>
</table>

<p><strong>Methode :</strong> pour trouver le bon prefixe, chercher 2^n &ge; (hotes requis + 2). Ex : 30 hotes &rarr; 2^5 = 32 &ge; 32 &rarr; /27.</p>
<div class="warn"><strong>Piege :</strong> un sous-reseau doit commencer sur une adresse alignee sur sa taille. Ex : 10.0.0.65/26 est FAUX car 65 n'est pas un multiple de 64.</div>

<!-- ======================================================== -->
<h2 id="arp">4. ARP et ICMP</h2>

<h3>ARP (Address Resolution Protocol)</h3>
<p>ARP resout une adresse IP en adresse MAC sur le reseau local. Sans ARP, il est impossible d'envoyer une trame Ethernet a la bonne machine.</p>
<pre><code>1. PC A veut envoyer a 10.20.0.50
2. Verifie le cache ARP : arp -a
3. Si absent : broadcast "Qui a 10.20.0.50 ?" (FF:FF:FF:FF:FF:FF)
4. 10.20.0.50 repond en unicast avec sa MAC
5. PC A stocke l'entree en cache (~2 min)
</code></pre>
<p><strong>ARP Gratuit (Gratuitous ARP) :</strong> une machine annonce sa propre IP/MAC sans demande. Usage normal : detection de conflits IP. Usage malveillant : ARP Spoofing / Poisoning (attaque Man-in-the-Middle).</p>

<h3>ICMP (Internet Control Message Protocol)</h3>
<p>Protocole de diagnostic et de messages d'erreur. Utilise par ping et traceroute.</p>
<table>
<tr><th>Message</th><th>Signification</th></tr>
<tr><td>Echo Request / Echo Reply</td><td>ping &mdash; teste la joignabilite</td></tr>
<tr><td>TTL Exceeded</td><td>Le paquet a fait trop de sauts (boucle probable)</td></tr>
<tr><td>Destination Unreachable</td><td>Le routeur ne trouve pas de route vers la destination</td></tr>
<tr><td>Port Unreachable</td><td>La destination est atteinte mais le port est ferme (UDP)</td></tr>
</table>
<p><strong>TTL par OS :</strong> Linux/Mac/Cisco = 64, Windows = 128, Cisco IOS = 255. Le TTL diminue de 1 a chaque routeur traverse. Si TTL atteint 0, le paquet est detruit et un "TTL Exceeded" est envoye a l'emetteur &mdash; c'est le principe de traceroute.</p>

<!-- ======================================================== -->
<h2 id="dhcp">5. DHCP</h2>

<p>DHCP attribue automatiquement une adresse IP et la configuration reseau a chaque machine. Ports : serveur sur UDP 67, client sur UDP 68.</p>

<h3>Processus DORA</h3>
<pre><code>Client                              Serveur
  |--DISCOVER (broadcast)----------->|  "Y a-t-il un serveur DHCP ?"
  |<--OFFER (broadcast/unicast)------|  "Je t'offre 10.20.0.50 / GW / DNS"
  |--REQUEST (broadcast)------------>|  "J'accepte l'offre" (broadcast pour informer les autres serveurs)
  |<--ACKNOWLEDGE (broadcast/unicast)|  "Confirme ! Bail valide 8 jours"
</code></pre>
<p><strong>Renouvellement du bail :</strong> a 50% de la duree le client tente de renouveler (unicast). A 87,5% il reessaie. A 100% il recommence le processus DORA complet.</p>

<h3>Diagnostics DHCP</h3>
<table>
<tr><th>Symptome</th><th>Cause probable</th><th>Solution</th></tr>
<tr><td>IP 169.254.x.x (APIPA)</td><td>Le client n'a pas recu de reponse DHCP</td><td>ipconfig /release puis /renew, verifier le service DHCP et le VLAN du port</td></tr>
<tr><td>Scope epuise</td><td>Toutes les IPs sont attribuees</td><td>Agrandir la plage, supprimer les baux expires, reduire la duree de bail</td></tr>
<tr><td>Conflit d'adresse IP</td><td>IP statique dans la plage DHCP dynamique</td><td>Mettre l'IP statique hors de la plage, ou creer une reservation DHCP</td></tr>
</table>

<div class="tip"><strong>Bonne pratique :</strong> les peripheriques avec IP fixe (serveurs, imprimantes) doivent etre soit hors de la plage DHCP dynamique, soit geres par des reservations DHCP (IP fixe attribuee via adresse MAC).</div>

<div class="warn"><strong>DHCP Relay :</strong> si le serveur DHCP n'est pas sur le meme segment que les clients, un "DHCP Relay Agent" (ip helper-address sur Cisco) est necessaire pour relayer les broadcasts DHCP vers le serveur.</div>

<div class="warn"><strong>DHCP autorise dans AD :</strong> sur Windows Server dans un domaine Active Directory, le serveur DHCP doit etre explicitement autorise dans l'AD, sinon il ne repond pas (protection anti-DHCP rogue).</div>

<!-- ======================================================== -->
<h2 id="dns">6. DNS</h2>

<p>Le DNS traduit les noms de domaine en adresses IP (et inversement). Port 53 TCP+UDP. UDP pour les requetes &lt;512 octets, TCP pour les transferts de zone et les reponses plus longues (DNSSEC).</p>

<h3>Types d'enregistrements</h3>
<table>
<tr><th>Type</th><th>Role</th><th>Exemple</th></tr>
<tr><td>A</td><td>Nom &rarr; IPv4</td><td>srv01 &rarr; 10.20.0.10</td></tr>
<tr><td>AAAA</td><td>Nom &rarr; IPv6</td><td>srv01 &rarr; 2001:db8::1</td></tr>
<tr><td>CNAME</td><td>Alias &rarr; autre nom (pas une IP)</td><td>www &rarr; srv01.mission.local</td></tr>
<tr><td>MX</td><td>Serveur de messagerie (avec priorite)</td><td>10 mail.mission.local</td></tr>
<tr><td>PTR</td><td>IP &rarr; Nom (DNS inverse)</td><td>10.0.20.10 &rarr; srv01</td></tr>
<tr><td>NS</td><td>Serveur de noms autoritaire</td><td>mission.local &rarr; ns1</td></tr>
<tr><td>SOA</td><td>Start Of Authority (infos sur la zone)</td><td>Numero de serie, TTL par defaut</td></tr>
<tr><td>TXT</td><td>Texte libre</td><td>SPF, DKIM, verification de domaine</td></tr>
<tr><td>SRV</td><td>Localisateur de service</td><td>_ldap._tcp &rarr; DC01:389</td></tr>
</table>

<h3>Resolution DNS recursive</h3>
<pre><code>PC → DNS local (cache PC)
   → Serveur DNS configure (ex: 10.20.0.1) [cache local]
     → Root servers (.)
       → Serveur TLD (.com, .org...)
         → Serveur autoritaire du domaine
           → Reponse avec l'IP, mise en cache selon le TTL
</code></pre>

<p><strong>TTL (Time To Live) :</strong> duree pendant laquelle un resolveur met en cache la reponse. TTL bas = propagation rapide mais plus de requetes. TTL eleve = moins de charge mais propagation lente.</p>

<h3>Commandes DNS</h3>
<pre><code>nslookup intranet.mission.local         # Resolution standard
nslookup -type=MX mission.local         # Enregistrements MX
nslookup intranet.mission.local 8.8.8.8 # Forcer un DNS specifique
Resolve-DnsName intranet.mission.local  # PowerShell
ipconfig /flushdns                      # Vider le cache DNS client
ipconfig /displaydns                    # Afficher le cache DNS client
dig intranet.mission.local              # Linux
</code></pre>

<div class="warn"><strong>Diagnostic DNS :</strong> distinguer "DNS ne repond pas" (timeout) de "DNS repond mais l'enregistrement n'existe pas" (NXDOMAIN). Si nslookup dit "No records" mais que d'autres machines resolvent, elles ont probablement l'info en cache.</div>

<!-- ======================================================== -->
<h2 id="nat">7. NAT / PAT</h2>

<p>NAT (Network Address Translation) traduit les adresses IP privees en adresses publiques pour l'acces a Internet.</p>

<table>
<tr><th>Type</th><th>Description</th><th>Usage</th></tr>
<tr><td>NAT Statique</td><td>1 IP privee &harr; 1 IP publique fixe</td><td>Exposer un serveur (web, mail) en DMZ</td></tr>
<tr><td>NAT Dynamique</td><td>Pool d'IPs privees &harr; pool d'IPs publiques</td><td>Rarement utilise en pratique</td></tr>
<tr><td>PAT / NAT Overload</td><td>Tout le reseau prive &rarr; 1 seule IP publique (differentiation par port source)</td><td>Standard dans 99% des routeurs/box</td></tr>
</table>

<h3>Fonctionnement PAT</h3>
<p>Le routeur maintient une table de traduction qui associe chaque connexion interne a un port source unique :</p>
<pre><code>IP Privee       Port Source   IP Publique      Port Traduit
10.20.0.10      54321         203.0.113.1      54321
10.20.0.20      54321         203.0.113.1      54322   (port change si conflit)
10.20.0.50      54000         203.0.113.1      54323
</code></pre>

<p><strong>Port Forwarding (DNAT) :</strong> permet d'acceder depuis Internet a un serveur interne. Ex : tout trafic entrant sur 203.0.113.1:443 est redirige vers 10.20.0.100:443.</p>

<!-- ======================================================== -->
<h2 id="vlan">8. VLAN / Switching / STP</h2>

<h3>VLANs</h3>
<p>Un VLAN (Virtual LAN) cree des domaines de broadcast logiquement separes sur le meme equipement physique. Les avantages sont la securite (isolation des departements), la reduction des domaines de broadcast, et le controle du trafic inter-segements via firewall.</p>

<table>
<tr><th>Type de port</th><th>Description</th><th>Usage</th></tr>
<tr><td>Access port</td><td>Un seul VLAN, trafic non tague. La machine ne sait pas qu'elle est dans un VLAN.</td><td>PC, imprimantes, serveurs</td></tr>
<tr><td>Trunk port (802.1Q)</td><td>Plusieurs VLANs simultanément, trafic tague avec un identifiant de 4 octets insere dans la trame Ethernet.</td><td>Liens switch-switch, switch-routeur</td></tr>
</table>

<p><strong>Communication inter-VLAN :</strong> les VLANs sont des reseaux L3 distincts. Pour communiquer, il faut obligatoirement un equipement de couche 3 (routeur ou switch L3).</p>
<ul>
<li><strong>Router-on-a-Stick :</strong> un seul routeur avec des sous-interfaces (une par VLAN), chacune servant de passerelle.</li>
<li><strong>Switch L3 avec SVI :</strong> le switch cree une interface VLAN virtuelle (SVI) par VLAN qui sert de gateway. Plus performant.</li>
</ul>

<h3>Configuration Cisco IOS</h3>
<pre><code># Creer un VLAN
Switch(config)# vlan 10
Switch(config-vlan)# name Direction

# Port access
Switch(config)# interface fa0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10

# Port trunk
Switch(config)# interface gi0/1
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk allowed vlan 10,20,30,40,50,99
Switch(config-if)# switchport trunk native vlan 99

# Verification
Switch# show vlan brief
Switch# show interfaces trunk
Switch# show interfaces gi0/1 switchport
</code></pre>

<h3>STP (Spanning Tree Protocol)</h3>
<p>STP previent les boucles de couche 2 dans les reseaux avec des liens redondants. Une boucle L2 sans STP provoque une "tempete de broadcast" qui paralyse completement le reseau.</p>

<p><strong>Root Bridge :</strong> le switch avec le BID (Bridge ID = priorite + adresse MAC) le plus bas. Par defaut, priorite = 32768. On peut forcer un switch a devenir root : <code>spanning-tree vlan 10 priority 4096</code>.</p>

<table>
<tr><th>Etat du port STP</th><th>Description</th></tr>
<tr><td>Disabled</td><td>Port administrativement desactive</td></tr>
<tr><td>Blocking</td><td>Recoit les BPDU, ne transmet pas de donnees, n'apprend pas les MACs</td></tr>
<tr><td>Listening</td><td>Envoie/recoit des BPDU, pas de donnees (15 secondes)</td></tr>
<tr><td>Learning</td><td>Apprend les adresses MAC, pas encore de donnees (15 secondes)</td></tr>
<tr><td>Forwarding</td><td>Etat normal &mdash; transmet les donnees et apprend les MACs</td></tr>
</table>

<p><strong>RSTP (802.1w) :</strong> version rapide de STP, convergence en &lt;1 seconde au lieu de 30-50 secondes. C'est le standard actuel.</p>
<p><strong>PortFast :</strong> pour les ports connectes a des PCs/serveurs uniquement, passe directement en Forwarding. Ne jamais activer sur un port trunk.</p>
<p><strong>BPDU Guard :</strong> si un BPDU est recu sur un port PortFast, le port passe en err-disable. Protege contre la connexion non autorisee d'un switch.</p>

<!-- ======================================================== -->
<h2 id="routing">9. Routage</h2>

<p>Un routeur decide du chemin que doit emprunter un paquet en consultant sa table de routage. La decision est basee sur l'adresse IP de destination.</p>

<table>
<tr><th></th><th>Routage statique</th><th>Routage dynamique (OSPF, BGP)</th></tr>
<tr><td>Configuration</td><td>Manuelle</td><td>Automatique entre routeurs</td></tr>
<tr><td>Adaptation aux pannes</td><td>Aucune (route fixe)</td><td>Recalcul automatique</td></tr>
<tr><td>Complexite</td><td>Simple</td><td>Plus complexe</td></tr>
<tr><td>Usage</td><td>Petits reseaux, routes de secours</td><td>Grands reseaux, WAN complexe, operateurs</td></tr>
</table>

<pre><code># Cisco IOS - Routes statiques
ip route 10.30.0.0 255.255.255.0 10.99.1.2    # Route vers site Washington
ip route 172.16.0.0 255.255.0.0 10.99.2.2     # Route vers Geneve
ip route 0.0.0.0 0.0.0.0 203.0.113.2          # Route par defaut (Internet)

# Verification
show ip route
show ip route 10.30.0.0
traceroute 10.30.0.50

# Linux
ip route add 10.30.0.0/24 via 10.99.1.2
ip route show
ip route get 10.30.0.50    # Quel chemin pour cette IP ?

# Windows
route print
New-NetRoute -DestinationPrefix "10.30.0.0/24" -NextHop "10.99.1.2" -InterfaceIndex 5
</code></pre>

<!-- ======================================================== -->
<h2 id="firewall">10. Firewall</h2>

<h3>Types de firewalls</h3>
<table>
<tr><th>Type</th><th>Description</th><th>Avantages/Limites</th></tr>
<tr><td>Packet filter (stateless)</td><td>Filtre paquet par paquet sur IP/port/protocole</td><td>Rapide, ne distingue pas les sessions</td></tr>
<tr><td>Stateful inspection</td><td>Maintient l'etat des connexions, autorise automatiquement les reponses</td><td>Standard actuel, efficace</td></tr>
<tr><td>WAF (Web Application Firewall)</td><td>Analyse le contenu HTTP/HTTPS (L7), detecte SQLi, XSS, etc.</td><td>Protege les applications web</td></tr>
<tr><td>Proxy Firewall</td><td>Agit comme intermediaire, inspecte le contenu</td><td>Tres securise, peut dechiffrer le TLS</td></tr>
</table>

<h3>Principes fondamentaux</h3>
<ul>
<li><strong>Deny All :</strong> bloquer tout sauf ce qui est explicitement autorise (liste blanche). C'est l'approche la plus securisee.</li>
<li><strong>Implicit Deny :</strong> la derniere regle implicite est toujours "tout refuser". Ce qui n'est pas autorise est bloque.</li>
<li><strong>First-Match :</strong> les regles sont evaluees sequentiellement. La premiere regle qui correspond s'applique, les suivantes sont ignorees.</li>
</ul>

<div class="danger"><strong>Piege classique :</strong> une regle DENY large placee avant des regles ALLOW specifiques bloque le trafic meme si la regle ALLOW est presente plus bas. Toujours ordonner du plus specifique au plus general.</div>

<h3>Exemple de regles PFSense</h3>
<pre><code># Interface WAN (Internet &rarr; Mission)
ALLOW  ANY        &rarr; 203.0.113.50:443  TCP  (VPN SSL entrant)
ALLOW  ANY        &rarr; 203.0.113.50:25   TCP  (SMTP entrant)
DENY   ANY        &rarr; ANY              ANY  (tout le reste)

# Interface LAN VLAN10 Direction
ALLOW  VLAN10  &rarr; 10.20.0.100:22,80,445  TCP  (SSH, HTTP, SMB vers serveur fichiers)
DENY   VLAN10  &rarr; VLAN40                 ANY  (Direction ne peut pas acceder a Securite)
DENY   VLAN10  &rarr; ANY                    ANY  (tout le reste bloque)
</code></pre>

<h3>DMZ (Demilitarized Zone)</h3>
<p>Zone reseau intermediaire entre Internet et le LAN interne. Accueille les serveurs accessibles depuis Internet (web, mail, reverse proxy). Si un serveur DMZ est compromis, le firewall bloque l'acces au reseau interne.</p>

<!-- ======================================================== -->
<h2 id="ports">11. Ports et protocoles essentiels</h2>

<table>
<tr><th>Service</th><th>Port</th><th>Proto</th><th>Notes</th></tr>
<tr><td>HTTP</td><td>80</td><td>TCP</td><td>Non chiffre</td></tr>
<tr><td>HTTPS</td><td>443</td><td>TCP</td><td>TLS/SSL</td></tr>
<tr><td>FTP controle</td><td>21</td><td>TCP</td><td>Commandes FTP</td></tr>
<tr><td>FTP donnees</td><td>20</td><td>TCP</td><td>Transfert fichiers</td></tr>
<tr><td>SSH</td><td>22</td><td>TCP</td><td>TOUJOURS preferer a Telnet</td></tr>
<tr><td>Telnet</td><td>23</td><td>TCP</td><td>Non chiffre &mdash; a bannir</td></tr>
<tr><td>SMTP</td><td>25</td><td>TCP</td><td>Mail serveur a serveur</td></tr>
<tr><td>SMTP chiffre</td><td>587 / 465</td><td>TCP</td><td>587=STARTTLS, 465=SMTPS</td></tr>
<tr><td>DNS</td><td>53</td><td>TCP+UDP</td><td>UDP pour requetes, TCP pour zones</td></tr>
<tr><td>DHCP Serveur</td><td>67</td><td>UDP</td><td>Recoit les requetes clients</td></tr>
<tr><td>DHCP Client</td><td>68</td><td>UDP</td><td>Recoit les reponses serveur</td></tr>
<tr><td>LDAP</td><td>389</td><td>TCP</td><td>Active Directory non chiffre</td></tr>
<tr><td>LDAPS</td><td>636</td><td>TCP</td><td>LDAP sur TLS</td></tr>
<tr><td>Kerberos</td><td>88</td><td>TCP+UDP</td><td>Authentification AD</td></tr>
<tr><td>RDP</td><td>3389</td><td>TCP</td><td>Bureau a distance Windows</td></tr>
<tr><td>SMB/CIFS</td><td>445</td><td>TCP</td><td>Partages reseau Windows</td></tr>
<tr><td>SNMP</td><td>161/162</td><td>UDP</td><td>Monitoring (161=requetes, 162=traps)</td></tr>
<tr><td>NTP</td><td>123</td><td>UDP</td><td>Synchronisation de l'horloge</td></tr>
<tr><td>MySQL</td><td>3306</td><td>TCP</td><td>Base de donnees</td></tr>
</table>

<div class="danger"><strong>Ports a ne jamais exposer directement sur Internet :</strong> 23 (Telnet), 135-139 (NetBIOS), 445 (SMB &mdash; WannaCry/EternalBlue), 3389 (RDP), 1433 (MSSQL), 3306 (MySQL).</div>

<!-- ======================================================== -->
<h2 id="vpn">12. VPN</h2>

<table>
<tr><th>Type</th><th>Protocole</th><th>Port</th><th>Cas d'usage</th></tr>
<tr><td>IPSec IKEv2</td><td>IKEv2 + ESP</td><td>UDP 500, 4500</td><td>VPN site-a-site, tres stable avec MOBIKE (reconnexion auto)</td></tr>
<tr><td>SSL VPN</td><td>TLS</td><td>TCP 443</td><td>Acces distant via navigateur, traverse facilement les firewalls</td></tr>
<tr><td>OpenVPN</td><td>SSL/TLS</td><td>UDP 1194 (ou TCP)</td><td>Tres configurable, multi-plateforme</td></tr>
<tr><td>WireGuard</td><td>ChaCha20/Poly1305</td><td>UDP 51820</td><td>Tres rapide et leger, code simple</td></tr>
</table>

<p><strong>Split tunneling :</strong> seul le trafic destine au reseau interne passe par le VPN. Le reste (Internet) passe directement. Contraire du "full tunnel" ou tout passe par le VPN.</p>

<p><strong>NAT Traversal (NAT-T) :</strong> IKEv2 sur UDP 4500 est concu pour traverser les NAT agressifs (hotels, hotspots). Preferer IKEv2 avec NAT-T pour les connexions depuis des reseaux inconnus.</p>

<div class="warn"><strong>VPN timeout au NAT :</strong> les NAT d'hotel ont souvent des timeouts courts sur les connexions TCP inactives. Configurer des keepalives (paquets envoys toutes les 30s) pour maintenir la session NAT active.</div>

<!-- ======================================================== -->
<h2 id="secu">13. Cybersecurite</h2>

<h3>Hardening Windows Server &mdash; Checklist</h3>
<pre><code># 1. Renommer le compte Administrator (cible privilegiee des attaques)
Rename-LocalUser -Name "Administrator" -NewName "admin-srv01"

# 2. Desactiver le compte Guest
Disable-LocalUser -Name "Guest"

# 3. Desactiver SMBv1 (vulnerable - WannaCry/EternalBlue)
Set-SmbServerConfiguration -EnableSMB1Protocol $false

# 4. Activer le Firewall Windows
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True

# 5. Augmenter la taille des journaux de securite
wevtutil sl Security /ms:1073741824   # 1 Go pour Security log

# 6. Appliquer les mises a jour
Install-Module PSWindowsUpdate
Get-WUInstall -AcceptAll -AutoReboot

# 7. Desactiver les services inutiles
Set-Service -Name "Telnet" -StartupType Disabled
Set-Service -Name "RemoteRegistry" -StartupType Disabled
</code></pre>

<p><strong>Bonnes pratiques :</strong> politique de mots de passe forte (14 car. min, complexite, expiration 90 jours, historique 24), lockout apres 5 tentatives, BitLocker pour le chiffrement disque, NLA pour RDP, ne jamais exposer RDP directement sur Internet (utiliser VPN).</p>

<h3>Events Windows importants</h3>
<table>
<tr><th>Event ID</th><th>Signification</th></tr>
<tr><td>4624</td><td>Connexion reussie</td></tr>
<tr><td>4625</td><td>Echec de connexion (brute-force si repete)</td></tr>
<tr><td>4688</td><td>Creation de processus (utile pour detecter les malwares)</td></tr>
<tr><td>4698</td><td>Tache planifiee creee (persistance malware)</td></tr>
<tr><td>4663</td><td>Acces a un fichier sensible</td></tr>
<tr><td>4740</td><td>Compte verrouille</td></tr>
</table>

<h3>Reponse a incident &mdash; phases</h3>
<ol>
<li><strong>Confinement immediat :</strong> isoler la machine du reseau (debrancher le cable, desactiver le port switch), NE PAS eteindre (preservation des preuves en RAM).</li>
<li><strong>Investigation :</strong> capturer la RAM, analyser les connexions reseau (<code>netstat -anb</code>), inspecter les processus (<code>tasklist /v</code>), chercher la persistance (registre, taches planifiees, Autoruns SysInternals).</li>
<li><strong>Eradication :</strong> en environnement sensible, toujours reconstruire le poste de zero ("rebuild from scratch"). Le nettoyage est insuffisant (rootkits, backdoors).</li>
<li><strong>Amelioration :</strong> bloquer les macros Office via GPO, former les utilisateurs, deployer un EDR, configurer DMARC/DKIM/SPF pour le mail.</li>
</ol>

<!-- ======================================================== -->
<h2 id="ad">14. Active Directory / GPO</h2>

<h3>Structure Active Directory</h3>
<pre><code>mission.local
├── OU=Utilisateurs
│   ├── OU=Direction
│   ├── OU=Consulaire
│   ├── OU=Informatique
│   └── OU=Securite
├── OU=Ordinateurs
│   ├── OU=Postes-Direction
│   ├── OU=Postes-Consulaire
│   └── OU=Serveurs
└── OU=Groupes
    ├── GRP-VPN-Users
    ├── GRP-Admins-IT
    └── GRP-Partage-Fichiers
</code></pre>

<h3>Protocoles d'authentification</h3>
<table>
<tr><th>Protocole</th><th>Port</th><th>Description</th></tr>
<tr><td>Kerberos</td><td>88 TCP/UDP</td><td>Protocole principal dans un domaine AD. Tickets avec duree de vie limitee.</td></tr>
<tr><td>NTLM</td><td>&mdash;</td><td>Protocole legacy, utilise pour la compatibilite (hors domaine, anciens OS).</td></tr>
<tr><td>LDAP</td><td>389 TCP</td><td>Interrogation et modification de l'annuaire AD. Non chiffre.</td></tr>
<tr><td>LDAPS</td><td>636 TCP</td><td>LDAP sur TLS. A privilegier.</td></tr>
</table>

<h3>Commandes PowerShell Active Directory</h3>
<pre><code># Rechercher un utilisateur
Get-ADUser -Identity jmartin
Get-ADUser -Identity jmartin -Properties *            # Toutes les proprietes
Get-ADUser -Filter {Name -like "Mar*"}                # Recherche par nom

# Gestion des comptes
Search-ADAccount -LockedOut                           # Comptes verrouilles
Unlock-ADAccount -Identity jmartin                    # Deverrouiller
Enable-ADAccount -Identity jmartin                    # Activer
Disable-ADAccount -Identity jmartin                   # Desactiver
Set-ADAccountPassword -Identity jmartin -Reset -NewPassword (Read-Host -AsSecureString)

# Gestion des groupes
Get-ADGroupMember -Identity "Domain Admins"
Add-ADGroupMember -Identity "GRP-IT" -Members jmartin
Remove-ADGroupMember -Identity "GRP-IT" -Members jmartin -Confirm:$false

# Gestion des ordinateurs
Get-ADComputer -Filter {Name -like "PC-*"}
Move-ADObject -Identity "CN=PC01,CN=Computers,DC=mission,DC=local" `
              -TargetPath "OU=Postes-Direction,DC=mission,DC=local"
</code></pre>

<h3>GPO (Group Policy Objects)</h3>
<p>Les GPO permettent d'appliquer des configurations et des restrictions a des OUs entieres. L'heritage se fait de la racine vers les OUs enfants. Un GPO peut etre bloque (<em>Block Inheritance</em>) ou force (<em>Enforced / No Override</em>).</p>
<pre><code>gpupdate /force             # Forcer la mise a jour des GPO sur un poste
gpresult /r                 # Afficher les GPO appliquees (resume)
gpresult /h C:\gpo.html     # Rapport HTML detaille
gpmc.msc                    # Console de gestion des GPO
</code></pre>

<!-- ======================================================== -->
<h2 id="linux">15. Linux / SSH / Bash</h2>

<h3>Commandes systeme essentielles</h3>
<pre><code># Informations systeme
hostname -f                     # FQDN du serveur
uname -a                        # Noyau et architecture
cat /etc/os-release             # Version de l'OS
uptime                          # Temps de fonctionnement et charge
free -h                         # RAM disponible
df -h                           # Espace disque par partition
du -sh *                        # Espace par dossier

# Processus
top / htop                      # Processus en temps reel
ps aux                          # Snapshot statique des processus
kill -9 &lt;PID&gt;                   # Tuer un processus

# Services (systemd)
systemctl status nginx          # Etat d'un service
systemctl start / stop / restart nginx
systemctl enable / disable nginx  # Demarrage automatique
journalctl -u nginx -f           # Logs du service en temps reel
tail -f /var/log/syslog          # Logs systeme en temps reel
</code></pre>

<h3>Permissions Linux</h3>
<table>
<tr><th>Droit</th><th>Valeur</th><th>Sur fichier</th><th>Sur repertoire</th></tr>
<tr><td>r (read)</td><td>4</td><td>Lire le contenu</td><td>Lister le contenu (ls)</td></tr>
<tr><td>w (write)</td><td>2</td><td>Modifier</td><td>Creer/supprimer des fichiers</td></tr>
<tr><td>x (execute)</td><td>1</td><td>Executer</td><td>Entrer dans le repertoire (cd)</td></tr>
</table>
<pre><code>chmod 754 fichier      # rwx r-x r--  (proprietaire=7, groupe=5, autres=4)
chown user:group fichier   # Changer proprietaire et groupe
id / groups                # Voir les groupes de l'utilisateur courant
sudo -l                    # Voir les commandes sudo autorisees
</code></pre>

<h3>SSH</h3>
<pre><code>ssh user@10.20.0.10                          # Connexion SSH
ssh -p 2222 user@10.20.0.10                  # Port personnalise
ssh -L 8080:localhost:80 user@10.20.0.10     # Tunnel local (port forwarding)
ssh-keygen -t ed25519 -C "cedric@mission"    # Generer une paire de cles
ssh-copy-id user@10.20.0.10                  # Copier la cle publique

# Configuration SSH serveur (/etc/ssh/sshd_config)
PermitRootLogin no           # Interdire la connexion root directe
PasswordAuthentication no    # Forcer les cles SSH
Port 2222                    # Changer le port par defaut
AllowUsers jmartin cedric    # Restreindre les utilisateurs
</code></pre>

<h3>Reseau sous Linux</h3>
<pre><code>ip a                          # Interfaces et adresses IP
ip r                          # Table de routage
ip route add 10.30.0.0/24 via 10.99.1.2  # Ajouter une route
ss -tulnp                     # Ports en ecoute avec processus (remplace netstat)
netstat -an                   # Connexions actives
ping / traceroute
nslookup / dig google.com     # Resolution DNS
arp -n                        # Table ARP
nmap -sS 10.20.0.0/24        # Scan du reseau (droits root necessaires)
</code></pre>

<!-- ======================================================== -->
<h2 id="powershell">16. PowerShell</h2>

<p>PowerShell manipule des <strong>objets .NET</strong> et non du texte brut comme Bash. Le pipeline transmet des objets avec leurs proprietes, ce qui permet de filtrer et de transformer les donnees avec precision.</p>

<pre><code># Bases
Get-Command *Service*                         # Chercher une commande
Get-Help Get-Process -Examples                # Aide et exemples
Get-Process | Where-Object CPU -gt 10        # Filtrer les processus
Get-Process | Select-Object Name, CPU, ID    # Selectionner des proprietes
Get-Service | Format-List *                   # Afficher toutes les proprietes

# Reseau
ipconfig /all
Test-NetConnection -ComputerName 10.20.0.100 -Port 445  # Tester un port
Get-NetTCPConnection | Where-Object State -eq "Established"
Resolve-DnsName google.com

# DHCP (sur serveur)
Get-DhcpServerv4Scope                              # Lister les scopes
Get-DhcpServerv4ScopeStatistics -ScopeId 10.20.0.0  # % d'utilisation
Get-DhcpServerv4Lease -ScopeId 10.20.0.0          # Baux actifs
Add-DhcpServerv4Reservation -ScopeId 10.20.0.0 -IPAddress 10.20.0.200 `
  -ClientId "AA-BB-CC-DD-EE-FF" -Description "Imprimante"

# DNS (sur serveur)
Get-DnsServerZone
Get-DnsServerResourceRecord -ZoneName "mission.local"
Add-DnsServerResourceRecordA -ZoneName "mission.local" -Name "intranet" `
  -IPv4Address "10.20.0.100" -CreatePtr
Clear-DnsServerCache

# Services
Get-Service | Where-Object Status -eq "Stopped"
Start-Service -Name DHCPServer
Stop-Service -Name Spooler
</code></pre>

<h3>Execution Policy</h3>
<table>
<tr><th>Politique</th><th>Description</th></tr>
<tr><td>Restricted</td><td>Aucun script (defaut sur certains Windows Server)</td></tr>
<tr><td>AllSigned</td><td>Tous les scripts doivent etre signes par une CA approuvee</td></tr>
<tr><td>RemoteSigned</td><td>Scripts locaux OK, scripts telecharges doivent etre signes. Recommande.</td></tr>
<tr><td>Unrestricted</td><td>Tout OK. Dangereux en production.</td></tr>
<tr><td>Bypass</td><td>Rien bloque. Usage temporaire pour les admins.</td></tr>
</table>
<pre><code>Get-ExecutionPolicy
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
powershell.exe -ExecutionPolicy Bypass -File script.ps1   # Passer outre temporairement
</code></pre>

<!-- ======================================================== -->
<h2 id="trouble">17. Methodologie de Troubleshooting</h2>

<h3>Methode OSI Bottom-Up</h3>
<p>Toujours diagnostiquer depuis la couche la plus basse. Des qu'une couche est validee, passer a la suivante. Des qu'une couche echoue, c'est la qu'est le probleme.</p>

<table>
<tr><th>Couche</th><th>Questions</th><th>Outils</th></tr>
<tr><td>L1 Physique</td><td>Cable branche ? Voyant allume ? Bon cable ?</td><td>Testeur de cable, remplacer le cable</td></tr>
<tr><td>L2 Liaison</td><td>MAC visible en ARP ? VLAN correct ? Port switch configure ?</td><td>arp -a, show mac address-table, show interfaces status</td></tr>
<tr><td>L3 Reseau</td><td>IP correcte ? Masque correct ? Gateway correcte ? Route valide ?</td><td>ipconfig /all, ping gateway, tracert, route print</td></tr>
<tr><td>L4 Transport</td><td>Port ouvert ? Firewall bloque ? Service ecoute ?</td><td>netstat, telnet &lt;IP&gt; &lt;PORT&gt;, Test-NetConnection</td></tr>
<tr><td>L7 Application</td><td>Service demarre ? Configuration correcte ? Logs d'erreurs ?</td><td>services.msc, eventvwr, journalctl</td></tr>
</table>

<h3>Les 6 etapes CompTIA Network+</h3>
<ol>
<li><strong>Identifier le probleme</strong> : symptomes, perimetre, chronologie</li>
<li><strong>Etablir une theorie</strong> : cause la plus probable</li>
<li><strong>Tester la theorie</strong> : valider ou invalider</li>
<li><strong>Etablir un plan d'action</strong> et le mettre en oeuvre</li>
<li><strong>Verifier</strong> que le probleme est resolu et prevenir la recurrence</li>
<li><strong>Documenter</strong> : ticket, base de connaissances, changelog</li>
</ol>

<div class="tip"><strong>Indice APIPA :</strong> une IP en 169.254.x.x indique systematiquement un echec du processus DHCP. Verifier : le service DHCP, le VLAN du port switch, le DHCP Relay Agent si le serveur est sur un autre segment.</div>

<h3>Commandes de diagnostic Windows</h3>
<pre><code>ipconfig /all              # Config reseau complete (IP, MAC, DNS, GW, DHCP)
ipconfig /release          # Liberer le bail DHCP
ipconfig /renew            # Obtenir un nouveau bail DHCP
ipconfig /flushdns         # Vider le cache DNS
ping 127.0.0.1             # Tester la pile TCP/IP locale
ping 10.20.0.254           # Tester la gateway
ping 8.8.8.8               # Tester la connectivite Internet
ping google.com            # Tester la resolution DNS + Internet
tracert 8.8.8.8            # Tracer le chemin reseau
nslookup google.com        # Tester la resolution DNS
netstat -an                # Connexions actives
arp -a                     # Table ARP (IP &lt;-&gt; MAC)
route print                # Table de routage
pathping google.com        # ping + traceroute combines
Test-NetConnection -ComputerName 10.20.0.100 -Port 445  # Tester un port TCP
</code></pre>

<!-- ======================================================== -->
<h2 id="wireshark">18. Wireshark et Monitoring</h2>

<h3>Filtres Wireshark essentiels</h3>
<pre><code># Filtres par IP
ip.addr == 10.20.0.50                    # Tout le trafic d'une IP
ip.src == 10.20.0.50                     # Uniquement le trafic sortant
ip.dst == 10.20.0.100                    # Uniquement le trafic entrant
!(ip.addr == 10.20.0.1)                  # Exclure une IP

# Filtres par protocole
dns                                       # Tout le DNS
dhcp                                      # Tout le DHCP
arp                                       # Tout l'ARP
http                                      # Trafic HTTP
tls                                       # Trafic TLS/HTTPS
icmp                                      # Pings

# Filtres par port
tcp.port == 443                           # HTTPS
tcp.dstport == 22                         # SSH entrant
udp.port == 53                            # DNS
tcp.port in {80 443 8080 8443}           # Plusieurs ports

# Flags TCP
tcp.flags.syn == 1 &amp;&amp; tcp.flags.ack == 0  # SYN seuls (scan de ports ?)
tcp.flags.reset == 1                      # Connexions refusees ou reinitalisees
tcp.flags.fin == 1                        # Fin de connexion
tcp.analysis.retransmission              # Retransmissions (probleme reseau)
tcp.analysis.zero_window                 # Fenetre TCP nulle (perf degradee)

# Filtres avances
frame contains "password"               # Chercher du texte dans les paquets
http.request.method == "POST"           # Requetes POST
http.response.code == 404              # Erreurs 404
dns.qry.name contains "google"         # Requetes DNS contenant "google"
</code></pre>

<h3>tcpdump (ligne de commande)</h3>
<pre><code>tcpdump -i eth0 "port 445"                    # Capturer sur un port
tcpdump -i em0 "host 10.20.0.10 and port 445" # Hote et port specifiques
tcpdump -xx port 9025                          # Afficher les octets en hexa
tcpdump -w capture.pcap                        # Sauvegarder dans un fichier
</code></pre>

<h3>Lecture des logs Windows</h3>
<pre><code>eventvwr.msc                        # Visionneuse d'evenements
# Logs importants :
# Windows Logs &gt; Security  : connexions, echecs, modifications de comptes
# Windows Logs &gt; System    : demarrage, arrets, erreurs materiel/drivers
# Applications and Services &gt; ... : logs applicatifs specifiques

# PowerShell
Get-EventLog -LogName Security -Newest 100
Get-EventLog -LogName Security -EventId 4625  # Echecs de connexion
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625} -MaxEvents 50
</code></pre>

<!-- ======================================================== -->
<h2 id="virt">19. Virtualisation / Cloud / Sauvegardes</h2>

<h3>Types d'hyperviseurs</h3>
<table>
<tr><th>Type</th><th>Description</th><th>Exemples</th></tr>
<tr><td>Type 1 (Bare-metal)</td><td>S'installe directement sur le materiel physique, sans OS hote. Plus performant.</td><td>VMware ESXi, Hyper-V, Proxmox VE, XCP-ng, KVM</td></tr>
<tr><td>Type 2</td><td>S'installe sur un OS existant. Moins performant, pour tests et developpement.</td><td>VMware Workstation, VirtualBox, Parallels</td></tr>
</table>

<table>
<tr><th>Notion</th><th>Definition</th></tr>
<tr><td>Snapshot</td><td>Sauvegarde de l'etat d'une VM a un instant T, reversible. N'est PAS un backup ! Consomme de l'espace disque.</td></tr>
<tr><td>Live Migration (vMotion)</td><td>Deplacer une VM en cours d'execution vers un autre hote physique sans interruption de service.</td></tr>
<tr><td>Overcommit CPU/RAM</td><td>Attribuer plus de ressources virtuelles qu'il n'y en a en physique. Possible car les VMs n'utilisent pas 100% en meme temps.</td></tr>
<tr><td>HA (High Availability)</td><td>Redemarrage automatique d'une VM sur un autre hote en cas de panne.</td></tr>
<tr><td>FT (Fault Tolerance)</td><td>VM miroir sur un second hote, bascule instantanee sans perte.</td></tr>
</table>

<h3>Regle de sauvegarde 3-2-1</h3>
<ul>
<li><strong>3</strong> copies des donnees</li>
<li><strong>2</strong> supports differents (ex : disque interne + NAS)</li>
<li><strong>1</strong> copie hors site (cloud, site distant)</li>
</ul>

<table>
<tr><th>Terme</th><th>Definition</th></tr>
<tr><td>RPO (Recovery Point Objective)</td><td>Perte de donnees maximale acceptable. Ex : RPO = 4h &rarr; sauvegardes toutes les 4h.</td></tr>
<tr><td>RTO (Recovery Time Objective)</td><td>Duree maximale acceptable d'interruption. Ex : RTO = 2h &rarr; le systeme doit etre restaure en moins de 2h.</td></tr>
</table>

<h3>Cloud &mdash; Concepts de base</h3>
<table>
<tr><th>Modele</th><th>Description</th><th>Exemples</th></tr>
<tr><td>IaaS</td><td>Infrastructure as a Service : VM, reseau, stockage brut</td><td>AWS EC2, Azure VM, GCP Compute Engine</td></tr>
<tr><td>PaaS</td><td>Platform as a Service : environnement d'execution gere</td><td>Azure App Service, Google App Engine</td></tr>
<tr><td>SaaS</td><td>Software as a Service : application directement accessible</td><td>Microsoft 365, Google Workspace, Salesforce</td></tr>
</table>

<!-- ======================================================== -->
<h2 id="cmds">20. Reference rapide des commandes</h2>

<h3>Windows &mdash; Reseau</h3>
<pre><code>ipconfig /all                          # Toutes infos reseau (IP, MAC, DNS, GW)
ipconfig /release / /renew             # Liberer / Renouveler bail DHCP
ipconfig /flushdns / /displaydns       # Vider / Afficher cache DNS
ping 8.8.8.8 -t                        # Ping continu (Ctrl+C pour arreter)
tracert 8.8.8.8                        # Tracer le chemin reseau
nslookup google.com                    # Resolution DNS
nslookup google.com 8.8.8.8            # Forcer un DNS specifique
netstat -an                            # Connexions actives
netstat -an | findstr :443             # Filtrer par port
arp -a                                 # Table ARP
arp -d                                 # Vider la table ARP
route print                            # Table de routage
pathping google.com                    # Ping + traceroute combines
netsh winsock reset                    # Reinitialiser la pile TCP/IP
Test-NetConnection -ComputerName 10.0.0.1 -Port 443
</code></pre>

<h3>Windows &mdash; GPO</h3>
<pre><code>gpupdate /force                        # Forcer MAJ GPO
gpresult /r                            # GPO appliquees (resume)
gpresult /h C:\gpo.html &amp;&amp; start C:\gpo.html  # Rapport HTML
gpmc.msc                               # Console GPO
gpedit.msc                             # Editeur GPO local
</code></pre>

<h3>Linux &mdash; Reseau</h3>
<pre><code>ip a                           # Interfaces et adresses IP
ip r                           # Table de routage
ip route get 10.30.0.50        # Quel chemin pour cette IP ?
ss -tulnp                      # Ports en ecoute
ping / traceroute
nslookup / dig google.com
arp -n                         # Table ARP
nmap -sn 10.20.0.0/24         # Decouverte des hotes du reseau
</code></pre>

<h3>Linux &mdash; Systeme</h3>
<pre><code>top / htop                     # Processus en temps reel
ps aux | grep nginx            # Chercher un processus
kill -9 &lt;PID&gt;
df -h                          # Espace disque
du -sh *                       # Espace par dossier
free -h                        # Memoire disponible
uptime                         # Charge systeme
tail -f /var/log/syslog        # Logs en temps reel
journalctl -u &lt;service&gt; -f    # Logs systemd en temps reel
</code></pre>

<h3>Diagnostic switch Cisco</h3>
<pre><code>show version                   # Modele et version IOS
show running-config            # Configuration actuelle
show interfaces status         # Etat de tous les ports
show interface gi0/1           # Detail d'un port
show vlan brief                # VLANs configures
show interfaces trunk          # Ports trunk
show mac address-table         # Table MAC
show spanning-tree summary     # Resume STP
show ip route                  # Table de routage
show cdp neighbors             # Voisins Cisco (topologie)
show log                       # Journaux systeme
</code></pre>

</div>

<!-- ==================== ENGLISH ==================== -->
<div class="lang-en">

<h1>Network &amp; Systems Administrator Course Notes</h1>

<p>Complete course notes covering all systems and network administration concepts at junior/intermediate level. Context: infrastructure of an international diplomatic mission (~300 workstations, Windows/Linux, segmented VLANs, multi-site VPN).</p>

<nav>
<strong>Contents:</strong>
<a href="#osi-en">OSI</a> &bull;
<a href="#tcpudp-en">TCP/UDP</a> &bull;
<a href="#ipv4-en">IPv4/Subnetting</a> &bull;
<a href="#arp-en">ARP/ICMP</a> &bull;
<a href="#dhcp-en">DHCP</a> &bull;
<a href="#dns-en">DNS</a> &bull;
<a href="#nat-en">NAT/PAT</a> &bull;
<a href="#vlan-en">VLAN/STP</a> &bull;
<a href="#routing-en">Routing</a> &bull;
<a href="#firewall-en">Firewall</a> &bull;
<a href="#ports-en">Ports</a> &bull;
<a href="#vpn-en">VPN</a> &bull;
<a href="#secu-en">Cybersecurity</a> &bull;
<a href="#ad-en">Active Directory</a> &bull;
<a href="#linux-en">Linux/SSH</a> &bull;
<a href="#powershell-en">PowerShell</a> &bull;
<a href="#trouble-en">Troubleshooting</a> &bull;
<a href="#wireshark-en">Wireshark</a> &bull;
<a href="#virt-en">Virtualisation</a> &bull;
<a href="#cmds-en">Command Reference</a>
</nav>

<h2 id="osi-en">1. OSI Model</h2>

<p>The OSI model breaks network communications down into 7 independent layers. It is not implemented directly but serves as a reference for understanding protocols and diagnosing faults (bottom-up method).</p>

<table>
<tr><th>Layer</th><th>Name</th><th>PDU</th><th>Protocols / Devices</th><th>Role</th></tr>
<tr><td>7</td><td>Application</td><td>Data</td><td>HTTP, HTTPS, FTP, DNS, SMTP, DHCP</td><td>User interface</td></tr>
<tr><td>6</td><td>Presentation</td><td>Data</td><td>SSL/TLS, JPEG, ASCII, encryption</td><td>Translation, compression</td></tr>
<tr><td>5</td><td>Session</td><td>Data</td><td>NetBIOS, RPC, SQL</td><td>Session establishment/teardown</td></tr>
<tr><td>4</td><td>Transport</td><td>Segment / Datagram</td><td>TCP (reliable), UDP (fast)</td><td>End-to-end transport</td></tr>
<tr><td>3</td><td>Network</td><td>Packet</td><td>IP, ICMP, OSPF &rarr; Router</td><td>Addressing and routing</td></tr>
<tr><td>2</td><td>Data Link</td><td>Frame</td><td>Ethernet, 802.1Q, WiFi &rarr; L2 Switch</td><td>Media access, MAC addresses</td></tr>
<tr><td>1</td><td>Physical</td><td>Bit</td><td>RJ45, fiber, WiFi &rarr; Hub, repeater</td><td>Electrical/optical signal</td></tr>
</table>

<div class="tip"><strong>Mnemonic (bottom to top):</strong> "Please Do Not Throw Sausage Pizza Away" &rarr; Physical, Data Link, Network, Transport, Session, Presentation, Application.</div>

<p><strong>Bottom-up diagnostic:</strong></p>
<ol>
<li><strong>L1 Physical</strong>: cable plugged in? switch light on? try another cable.</li>
<li><strong>L2 Data Link</strong>: MAC visible in ARP? correct VLAN? switch port configured?</li>
<li><strong>L3 Network</strong>: correct IP? correct mask? gateway configured? valid route?</li>
<li><strong>L4 Transport</strong>: TCP/UDP port open? firewall blocking? service running?</li>
<li><strong>L7 Application</strong>: service started? correct configuration? error logs?</li>
</ol>

<h2 id="tcpudp-en">2. TCP and UDP</h2>

<h3>TCP (Transmission Control Protocol)</h3>
<p>Connection-oriented, reliable protocol. Guarantees ordered delivery with retransmission on loss. Use: HTTP, HTTPS, SSH, FTP, SMTP, SMB.</p>
<pre><code>Client                    Server
  |---- SYN (seq=x) -------->|   Client initiates connection
  |<--- SYN-ACK (seq=y) -----|   Server accepts and acknowledges
  |---- ACK (ack=y+1) ------>|   Client confirms
  |    [Connection established] |
</code></pre>

<h3>UDP (User Datagram Protocol)</h3>
<p>Connectionless, unreliable protocol. Sends datagrams without acknowledgement or order guarantee. Much faster than TCP. Use: DNS, DHCP, video streaming, VoIP, gaming, SNMP, NTP.</p>

<table>
<tr><th></th><th>TCP</th><th>UDP</th></tr>
<tr><td>Connection</td><td>Connection-oriented (3-way handshake)</td><td>Connectionless</td></tr>
<tr><td>Reliability</td><td>Guaranteed (retransmission, ordering)</td><td>None</td></tr>
<tr><td>Speed</td><td>Slower (overhead)</td><td>Faster</td></tr>
<tr><td>Use cases</td><td>HTTP, SSH, FTP, SMTP, SMB</td><td>DNS, DHCP, VoIP, streaming</td></tr>
</table>

<h2 id="ipv4-en">3. IPv4 / CIDR / Subnetting</h2>

<h3>Special addresses</h3>
<table>
<tr><th>Address</th><th>Role</th></tr>
<tr><td>127.0.0.1</td><td>Loopback &mdash; tests local TCP/IP stack, never leaves the host</td></tr>
<tr><td>169.254.x.x</td><td>APIPA &mdash; DHCP failed, auto-assigned address</td></tr>
<tr><td>0.0.0.0</td><td>Default route / unconfigured address</td></tr>
<tr><td>255.255.255.255</td><td>Limited broadcast (entire segment)</td></tr>
</table>

<h3>Private ranges RFC 1918</h3>
<table>
<tr><th>Range</th><th>CIDR</th><th>Max hosts</th><th>Typical use</th></tr>
<tr><td>10.0.0.0 &ndash; 10.255.255.255</td><td>/8</td><td>~16 million</td><td>Large enterprises, datacenters</td></tr>
<tr><td>172.16.0.0 &ndash; 172.31.255.255</td><td>/12</td><td>~1 million</td><td>Medium enterprises</td></tr>
<tr><td>192.168.0.0 &ndash; 192.168.255.255</td><td>/16</td><td>~65,000</td><td>Home, small offices</td></tr>
</table>

<h3>Subnetting formulas</h3>
<pre><code>Host bits        = 32 - CIDR prefix
Total addresses  = 2^(host bits)
Usable hosts     = 2^(host bits) - 2  (network + broadcast excluded)
</code></pre>

<table>
<tr><th>CIDR</th><th>Mask</th><th>Usable hosts</th></tr>
<tr><td>/24</td><td>255.255.255.0</td><td>254</td></tr>
<tr><td>/26</td><td>255.255.255.192</td><td>62</td></tr>
<tr><td>/27</td><td>255.255.255.224</td><td>30</td></tr>
<tr><td>/28</td><td>255.255.255.240</td><td>14</td></tr>
<tr><td>/29</td><td>255.255.255.248</td><td>6</td></tr>
<tr><td>/30</td><td>255.255.255.252</td><td>2 (point-to-point WAN)</td></tr>
</table>

<h2 id="arp-en">4. ARP and ICMP</h2>

<h3>ARP (Address Resolution Protocol)</h3>
<p>ARP resolves an IP address to a MAC address on the local network. Without ARP, Ethernet frames cannot be delivered to the right machine.</p>
<pre><code>1. PC A wants to send to 10.20.0.50
2. Checks ARP cache: arp -a
3. If missing: broadcast "Who has 10.20.0.50?" (FF:FF:FF:FF:FF:FF)
4. 10.20.0.50 replies with its MAC (unicast)
5. PC A stores the entry in cache (~2 min)
</code></pre>
<p><strong>Gratuitous ARP:</strong> a device announces its own IP/MAC without being asked. Normal use: IP conflict detection at boot. Malicious use: ARP Spoofing/Poisoning (Man-in-the-Middle attack).</p>

<h3>ICMP</h3>
<table>
<tr><th>Message</th><th>Meaning</th></tr>
<tr><td>Echo Request / Echo Reply</td><td>ping &mdash; tests reachability</td></tr>
<tr><td>TTL Exceeded</td><td>Packet traversed too many hops (loop probable)</td></tr>
<tr><td>Destination Unreachable</td><td>Router cannot find a route to destination</td></tr>
</table>
<p><strong>TTL by OS:</strong> Linux/Mac/Cisco = 64, Windows = 128, Cisco IOS = 255. TTL decrements by 1 at each router. This is the basis of traceroute.</p>

<h2 id="dhcp-en">5. DHCP</h2>

<p>DHCP automatically assigns an IP address and network configuration to each machine. Ports: server on UDP 67, client on UDP 68.</p>
<pre><code>Client                              Server
  |--DISCOVER (broadcast)----------->|  "Is there a DHCP server?"
  |<--OFFER (broadcast/unicast)------|  "I offer you 10.20.0.50 / GW / DNS"
  |--REQUEST (broadcast)------------>|  "I accept the offer"
  |<--ACKNOWLEDGE (broadcast/unicast)|  "Confirmed! Lease valid 8 days"
</code></pre>

<div class="tip"><strong>Best practice:</strong> devices with fixed IPs (servers, printers) should either be outside the DHCP dynamic range, or managed through DHCP reservations (fixed IP assigned via MAC address).</div>
<div class="warn"><strong>APIPA:</strong> a 169.254.x.x address always indicates a DHCP failure. Check: the DHCP service, the switch port VLAN, the DHCP Relay Agent if the server is on a different segment.</div>

<h2 id="dns-en">6. DNS</h2>

<p>DNS translates domain names to IP addresses (and vice versa). Port 53 TCP+UDP.</p>

<table>
<tr><th>Type</th><th>Role</th><th>Example</th></tr>
<tr><td>A</td><td>Name &rarr; IPv4</td><td>srv01 &rarr; 10.20.0.10</td></tr>
<tr><td>AAAA</td><td>Name &rarr; IPv6</td><td>srv01 &rarr; 2001:db8::1</td></tr>
<tr><td>CNAME</td><td>Alias &rarr; another name (not an IP)</td><td>www &rarr; srv01.mission.local</td></tr>
<tr><td>MX</td><td>Mail server (with priority)</td><td>10 mail.mission.local</td></tr>
<tr><td>PTR</td><td>IP &rarr; Name (reverse DNS)</td><td>10.0.20.10 &rarr; srv01</td></tr>
<tr><td>TXT</td><td>Free text</td><td>SPF, DKIM, domain verification</td></tr>
</table>

<pre><code>nslookup intranet.mission.local         # Standard resolution
nslookup -type=MX mission.local         # MX records
Resolve-DnsName intranet.mission.local  # PowerShell
ipconfig /flushdns                      # Flush DNS cache
ipconfig /displaydns                    # Show DNS cache
dig intranet.mission.local              # Linux
</code></pre>

<h2 id="nat-en">7. NAT / PAT</h2>

<table>
<tr><th>Type</th><th>Description</th><th>Use case</th></tr>
<tr><td>Static NAT</td><td>1 private IP &harr; 1 fixed public IP</td><td>Expose a DMZ server to the Internet</td></tr>
<tr><td>PAT / NAT Overload</td><td>Entire private network &rarr; 1 public IP (differentiated by source port)</td><td>Standard in 99% of routers/gateways</td></tr>
</table>
<p><strong>Port Forwarding (DNAT):</strong> redirects inbound Internet traffic to an internal server. E.g.: all traffic on 203.0.113.1:443 is forwarded to 10.20.0.100:443.</p>

<h2 id="vlan-en">8. VLAN / Switching / STP</h2>

<table>
<tr><th>Port type</th><th>Description</th><th>Use</th></tr>
<tr><td>Access port</td><td>Single VLAN, untagged traffic. The device does not know it is in a VLAN.</td><td>PCs, printers, servers</td></tr>
<tr><td>Trunk port (802.1Q)</td><td>Multiple VLANs simultaneously, tagged with a 4-byte identifier inserted into the Ethernet frame.</td><td>Switch-switch, switch-router links</td></tr>
</table>

<p><strong>Inter-VLAN routing:</strong> VLANs are separate L3 networks. Communication requires a Layer 3 device (router or L3 switch).</p>

<pre><code># Cisco IOS VLAN configuration
Switch(config)# vlan 10
Switch(config-vlan)# name Direction

# Access port
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10

# Trunk port
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk allowed vlan 10,20,30,40,50,99
</code></pre>

<h3>STP (Spanning Tree Protocol)</h3>
<p>STP prevents Layer 2 loops in networks with redundant links. A L2 loop without STP causes a broadcast storm that completely paralyzes the network.</p>
<p><strong>PortFast:</strong> for ports connected to PCs/servers only, skips Listening/Learning and goes directly to Forwarding. Never enable on a trunk port.</p>
<p><strong>BPDU Guard:</strong> if a BPDU is received on a PortFast port, the port enters err-disable state. Protects against unauthorized switch connections.</p>

<h2 id="routing-en">9. Routing</h2>

<pre><code># Cisco IOS static routes
ip route 10.30.0.0 255.255.255.0 10.99.1.2    # Route to Washington site
ip route 0.0.0.0 0.0.0.0 203.0.113.2          # Default route (Internet)

# Verification
show ip route
traceroute 10.30.0.50

# Linux
ip route add 10.30.0.0/24 via 10.99.1.2
ip route show

# Windows
route print
</code></pre>

<h2 id="firewall-en">10. Firewall</h2>

<p><strong>Key principles:</strong></p>
<ul>
<li><strong>Deny All:</strong> block everything except what is explicitly allowed (whitelist). Most secure approach.</li>
<li><strong>First-Match:</strong> rules are evaluated sequentially. The first matching rule applies; subsequent rules are ignored.</li>
<li><strong>Stateful:</strong> tracks connection state, automatically allows replies to internally initiated connections.</li>
</ul>

<div class="danger"><strong>Classic pitfall:</strong> a broad DENY rule placed before specific ALLOW rules will block traffic even if the ALLOW rule exists further down. Always order from most specific to most general.</div>

<h2 id="ports-en">11. Essential Ports and Protocols</h2>

<table>
<tr><th>Service</th><th>Port</th><th>Proto</th><th>Notes</th></tr>
<tr><td>HTTP</td><td>80</td><td>TCP</td><td>Unencrypted</td></tr>
<tr><td>HTTPS</td><td>443</td><td>TCP</td><td>TLS/SSL</td></tr>
<tr><td>SSH</td><td>22</td><td>TCP</td><td>Always prefer over Telnet</td></tr>
<tr><td>Telnet</td><td>23</td><td>TCP</td><td>Unencrypted &mdash; ban it</td></tr>
<tr><td>SMTP</td><td>25</td><td>TCP</td><td>Server-to-server mail</td></tr>
<tr><td>DNS</td><td>53</td><td>TCP+UDP</td><td>UDP for queries, TCP for zone transfers</td></tr>
<tr><td>DHCP Server</td><td>67</td><td>UDP</td><td>Receives client requests</td></tr>
<tr><td>DHCP Client</td><td>68</td><td>UDP</td><td>Receives server responses</td></tr>
<tr><td>LDAP</td><td>389</td><td>TCP</td><td>Active Directory (unencrypted)</td></tr>
<tr><td>LDAPS</td><td>636</td><td>TCP</td><td>LDAP over TLS</td></tr>
<tr><td>Kerberos</td><td>88</td><td>TCP+UDP</td><td>AD authentication</td></tr>
<tr><td>RDP</td><td>3389</td><td>TCP</td><td>Windows Remote Desktop</td></tr>
<tr><td>SMB/CIFS</td><td>445</td><td>TCP</td><td>Windows network shares</td></tr>
<tr><td>SNMP</td><td>161/162</td><td>UDP</td><td>Network monitoring</td></tr>
<tr><td>NTP</td><td>123</td><td>UDP</td><td>Clock synchronization</td></tr>
</table>

<h2 id="vpn-en">12. VPN</h2>

<table>
<tr><th>Type</th><th>Protocol</th><th>Port</th><th>Use case</th></tr>
<tr><td>IPSec IKEv2</td><td>IKEv2 + ESP</td><td>UDP 500, 4500</td><td>Site-to-site VPN, very stable with MOBIKE (auto-reconnect)</td></tr>
<tr><td>SSL VPN</td><td>TLS</td><td>TCP 443</td><td>Remote access, easily traverses firewalls</td></tr>
<tr><td>OpenVPN</td><td>SSL/TLS</td><td>UDP 1194</td><td>Highly configurable, cross-platform</td></tr>
<tr><td>WireGuard</td><td>ChaCha20/Poly1305</td><td>UDP 51820</td><td>Very fast and lightweight</td></tr>
</table>

<h2 id="secu-en">13. Cybersecurity</h2>

<h3>Windows Server Hardening Checklist</h3>
<pre><code># Rename the Administrator account
Rename-LocalUser -Name "Administrator" -NewName "admin-srv01"

# Disable SMBv1 (vulnerable - WannaCry/EternalBlue)
Set-SmbServerConfiguration -EnableSMB1Protocol $false

# Enable Windows Firewall
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True

# Increase Security log size
wevtutil sl Security /ms:1073741824   # 1 GB

# Disable unnecessary services
Set-Service -Name "Telnet" -StartupType Disabled

# Apply updates
Get-WUInstall -AcceptAll -AutoReboot
</code></pre>

<h3>Incident Response Phases</h3>
<ol>
<li><strong>Immediate containment:</strong> isolate the machine from the network (unplug cable, disable switch port). DO NOT power off (preserves RAM evidence).</li>
<li><strong>Investigation:</strong> capture RAM, analyze network connections (<code>netstat -anb</code>), inspect processes, check for persistence (registry, scheduled tasks, Autoruns).</li>
<li><strong>Eradication:</strong> in sensitive environments, always rebuild the workstation from scratch. Cleanup is insufficient (rootkits, backdoors).</li>
<li><strong>Improvement:</strong> block Office macros via GPO, train users, deploy EDR, configure DMARC/DKIM/SPF.</li>
</ol>

<h2 id="ad-en">14. Active Directory / GPO</h2>

<table>
<tr><th>Protocol</th><th>Port</th><th>Description</th></tr>
<tr><td>Kerberos</td><td>88 TCP/UDP</td><td>Primary AD authentication protocol. Time-limited tickets.</td></tr>
<tr><td>NTLM</td><td>&mdash;</td><td>Legacy protocol, used for compatibility.</td></tr>
<tr><td>LDAP</td><td>389 TCP</td><td>Query and modify the AD directory. Unencrypted.</td></tr>
<tr><td>LDAPS</td><td>636 TCP</td><td>LDAP over TLS. Preferred.</td></tr>
</table>

<pre><code># User management
Get-ADUser -Identity jmartin
Search-ADAccount -LockedOut                           # Locked accounts
Unlock-ADAccount -Identity jmartin
Enable-ADAccount / Disable-ADAccount -Identity jmartin
Set-ADAccountPassword -Identity jmartin -Reset -NewPassword (Read-Host -AsSecureString)

# Group management
Add-ADGroupMember -Identity "GRP-IT" -Members jmartin
Remove-ADGroupMember -Identity "GRP-IT" -Members jmartin -Confirm:$false

# GPO
gpupdate /force             # Force GPO update
gpresult /r                 # Applied GPOs (summary)
gpmc.msc                    # GPO management console
</code></pre>

<h2 id="linux-en">15. Linux / SSH / Bash</h2>

<pre><code># System info
hostname -f / uname -a / cat /etc/os-release
uptime / free -h / df -h / du -sh *

# Services
systemctl status / start / stop / restart &lt;service&gt;
systemctl enable / disable &lt;service&gt;    # Auto-start at boot
journalctl -u &lt;service&gt; -f              # Real-time service logs
tail -f /var/log/syslog                 # Real-time system logs

# Permissions
chmod 754 file         # rwx r-x r--
chown user:group file
sudo -l                # View authorized sudo commands

# SSH
ssh user@10.20.0.10
ssh -L 8080:localhost:80 user@10.20.0.10   # Local tunnel
ssh-keygen -t ed25519                       # Generate key pair
ssh-copy-id user@10.20.0.10               # Copy public key
</code></pre>

<h2 id="powershell-en">16. PowerShell</h2>

<p>PowerShell manipulates <strong>.NET objects</strong>, not plain text like Bash. The pipeline passes objects with their properties, enabling precise filtering and transformation.</p>

<pre><code>Get-Process | Where-Object CPU -gt 10        # Filter processes
Get-Service | Select-Object Name, Status     # Select properties
Test-NetConnection -ComputerName 10.20.0.100 -Port 445

# DHCP
Get-DhcpServerv4Scope
Get-DhcpServerv4ScopeStatistics -ScopeId 10.20.0.0
Get-DhcpServerv4Lease -ScopeId 10.20.0.0

# DNS
Get-DnsServerResourceRecord -ZoneName "mission.local"
Add-DnsServerResourceRecordA -ZoneName "mission.local" -Name "intranet" `
  -IPv4Address "10.20.0.100" -CreatePtr

# AD
Get-ADUser -Identity jmartin
Unlock-ADAccount -Identity jmartin
</code></pre>

<h2 id="trouble-en">17. Troubleshooting Methodology</h2>

<p><strong>OSI Bottom-Up:</strong> always diagnose from the lowest layer up. Once a layer is validated, move to the next. When a layer fails, that is where the problem lies.</p>

<table>
<tr><th>Layer</th><th>Questions</th><th>Tools</th></tr>
<tr><td>L1 Physical</td><td>Cable plugged in? Light on? Good cable?</td><td>Cable tester, replace cable</td></tr>
<tr><td>L2 Data Link</td><td>MAC visible in ARP? Correct VLAN? Switch port configured?</td><td>arp -a, show mac address-table</td></tr>
<tr><td>L3 Network</td><td>Correct IP? Correct mask? Gateway set? Valid route?</td><td>ipconfig /all, ping gateway, tracert</td></tr>
<tr><td>L4 Transport</td><td>Port open? Firewall blocking? Service listening?</td><td>netstat, Test-NetConnection, telnet</td></tr>
<tr><td>L7 Application</td><td>Service started? Correct config? Error logs?</td><td>services.msc, eventvwr, journalctl</td></tr>
</table>

<div class="tip"><strong>APIPA indicator:</strong> a 169.254.x.x IP always indicates a DHCP failure. Check: the DHCP service, the switch port VLAN, the DHCP Relay Agent if the server is on a different segment.</div>

<h2 id="wireshark-en">18. Wireshark and Monitoring</h2>

<pre><code># By IP
ip.addr == 10.20.0.50
ip.src == 10.20.0.50

# By protocol
dns / dhcp / arp / http / tls / icmp

# By port
tcp.port == 443
udp.port == 53

# TCP flags
tcp.flags.syn == 1 &amp;&amp; tcp.flags.ack == 0  # SYN only (port scan?)
tcp.flags.reset == 1                        # Refused/reset connections
tcp.analysis.retransmission                # Retransmissions (network issue)
tcp.analysis.zero_window                   # Zero window (performance issue)
</code></pre>

<h2 id="virt-en">19. Virtualisation / Cloud / Backups</h2>

<table>
<tr><th>Concept</th><th>Definition</th></tr>
<tr><td>Snapshot</td><td>Saves VM state at a point in time, reversible. NOT a backup! Consumes disk space.</td></tr>
<tr><td>Live Migration (vMotion)</td><td>Move a running VM to another physical host with zero downtime.</td></tr>
<tr><td>HA (High Availability)</td><td>Automatic VM restart on another host if the current host fails.</td></tr>
<tr><td>RPO</td><td>Maximum acceptable data loss. RPO = 4h means backups every 4h.</td></tr>
<tr><td>RTO</td><td>Maximum acceptable downtime. RTO = 2h means system must be restored within 2h.</td></tr>
</table>

<p><strong>3-2-1 Backup rule:</strong> 3 copies of data, on 2 different media, with 1 copy offsite (cloud, remote site).</p>

<table>
<tr><th>Model</th><th>Description</th><th>Examples</th></tr>
<tr><td>IaaS</td><td>Raw infrastructure: VMs, network, storage</td><td>AWS EC2, Azure VM</td></tr>
<tr><td>PaaS</td><td>Managed runtime environment</td><td>Azure App Service, Google App Engine</td></tr>
<tr><td>SaaS</td><td>Application directly accessible</td><td>Microsoft 365, Google Workspace</td></tr>
</table>

<h2 id="cmds-en">20. Command Reference</h2>

<h3>Windows &mdash; Network</h3>
<pre><code>ipconfig /all                          # All network info (IP, MAC, DNS, GW)
ipconfig /release / /renew             # Release / Renew DHCP lease
ipconfig /flushdns / /displaydns       # Flush / Show DNS cache
ping 8.8.8.8 -t                        # Continuous ping (Ctrl+C to stop)
tracert 8.8.8.8                        # Trace network path
nslookup google.com                    # DNS resolution
netstat -an                            # Active connections
netstat -an | findstr :443             # Filter by port
arp -a / arp -d                        # Show / Clear ARP table
route print                            # Routing table
Test-NetConnection -ComputerName 10.0.0.1 -Port 443
</code></pre>

<h3>Linux &mdash; Network &amp; System</h3>
<pre><code>ip a / ip r                           # Interfaces and routes
ss -tulnp                             # Listening ports with process
ping / traceroute / nslookup / dig
arp -n                                # ARP table
df -h / du -sh *                      # Disk space
free -h / uptime                      # System state
tail -f /var/log/syslog               # Real-time logs
systemctl status/start/stop/restart &lt;service&gt;
</code></pre>

<h3>Cisco Switch Diagnostics</h3>
<pre><code>show version                   # Model and IOS version
show interfaces status         # All ports status
show vlan brief                # Configured VLANs
show interfaces trunk          # Trunk ports
show mac address-table         # MAC table
show spanning-tree summary     # STP summary
show ip route                  # Routing table
show cdp neighbors             # Cisco neighbors (topology)
show log                       # System logs
</code></pre>

</div>

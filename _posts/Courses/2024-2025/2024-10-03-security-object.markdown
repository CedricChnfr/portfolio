---
layout: default
title:  "Security for Connected Objects"
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
<li><a href="./middleware-iot.html">Middleware for IoT - S9</a> - Protocoles de communication securises</li>
<li><a href="./emerging-network.html">Emerging Network Technologies - S9</a> - Securite reseau SDN</li>
<li><a href="../2023-2024/2024-10-03-securite-materielle.html">Securite Materielle - S7</a> - Fondamentaux securite hardware</li>
</ul>

<hr>

<h1>Security for Connected Objects - Semestre 9</h1>

<p><strong>Annee academique</strong> : 2024-2025<br>
<strong>Semestre</strong> : S9<br>
<strong>Enseignants</strong> : E. Alata, V. Migliore<br>
<strong>Categorie</strong> : Securite IoT et Cryptographie</p>

<hr>

<h2>PART A : PRESENTATION GENERALE</h2>

<h3 class="section-title">Vue d'ensemble</h3>

<p>Le cours "Security for Connected Objects" dispense par E. Alata et V. Migliore constitue un pilier essentiel de ma formation en securite des systemes connectes. Ce module couvre de maniere exhaustive les mecanismes de securite indispensables aux dispositifs IoT : cryptographie symetrique et asymetrique, fonctions de hachage, protocoles TLS/SSL, certificats numeriques et infrastructure a cles publiques (PKI), securite materielle, menaces specifiques a l'IoT, et methodologie d'analyse de risques EBIOS.</p>

<p>Le cours allie theorie approfondie et mise en pratique intensive a travers des travaux de laboratoire concrets : challenges CTF (Capture The Flag), attaques par injection SQL, attaques Man-in-the-Middle (MITM), migration TLS, et experimentation quantique. Cette approche m'a permis de developper une comprehension operationnelle de la securite des objets connectes.</p>

<p><strong>Objectifs pedagogiques</strong> :</p>
<ul>
<li>Comprendre les fondements de la cryptographie moderne (symetrique, asymetrique, hachage)</li>
<li>Maitriser les protocoles de securite pour les communications IoT (TLS/SSL, PKI)</li>
<li>Identifier les faiblesses de securite dans une architecture IoT (OWASP IoT Top 10)</li>
<li>Evaluer l'impact de l'exploitation d'une vulnerabilite de securite</li>
<li>Proposer des contre-mesures de securite adequates</li>
<li>Realiser une analyse de risques avec la methodologie EBIOS</li>
<li>Apprehender la securite materielle : attaques par canaux auxiliaires, injection de fautes, elements securises</li>
</ul>

<h3 class="section-title">Position dans le cursus</h3>

<p>Ce module s'inscrit dans une continuite pedagogique :</p>
<ul>
<li><strong>Securite Materielle (S7)</strong> : attaques par canaux auxiliaires, buffer overflow, analyse de consommation</li>
<li><strong>Microcontroleurs et Hardware (S9)</strong> : systemes embarques, FPGA, architecture materielle</li>
<li><strong>Middleware for IoT (S9)</strong> : protocoles de communication securises (MQTT, TLS)</li>
<li><strong>Emerging Network Technologies (S9)</strong> : securite reseau SDN/NFV</li>
</ul>

<p>Il prepare directement a :</p>
<ul>
<li><strong>Projet Innovant (S9)</strong> : implementation AES et securisation d'un systeme IoT complet</li>
<li><strong>Carriere en cybersecurite</strong> : audit de securite, pentest, conception securisee</li>
<li><strong>Recherche</strong> : cryptographie post-quantique, securite hardware avancee</li>
</ul>

<hr>

<h2>PART B : EXPERIENCE ET CONTEXTE</h2>

<h3 class="section-title">Organisation et ressources</h3>

<p>Le module etait structure en cours magistraux et travaux pratiques intensifs :</p>

<p><strong>Cours magistraux</strong> :</p>
<ul>
<li>Cryptographie symetrique (AES, DES, modes de chiffrement par blocs)</li>
<li>Cryptographie asymetrique (RSA, ECC, Diffie-Hellman)</li>
<li>Fonctions de hachage (SHA-256, MD5, fonctions legeres pour IoT)</li>
<li>Certificats numeriques et PKI (Public Key Infrastructure)</li>
<li>Protocoles TLS/SSL et securisation des communications</li>
<li>Securite materielle (attaques par canaux auxiliaires, injection de fautes)</li>
<li>Menaces specifiques IoT (OWASP IoT Top 10)</li>
<li>Methodologie d'analyse de risques EBIOS</li>
</ul>

<p><strong>Travaux pratiques</strong> :</p>
<ul>
<li><strong>Lab 1</strong> : Injection SQL et Cross-Site Scripting (XSS)</li>
<li><strong>Lab 2</strong> : Chiffrement symetrique et asymetrique (AES, RSA)</li>
<li><strong>Lab 3</strong> : Attaque Man-in-the-Middle, migration TLS, certificats</li>
<li><strong>Lab 4</strong> : Challenges CTF cryptographiques (flags)</li>
<li><strong>Lab Quantique</strong> : Distribution quantique de cles (QKD), protocole NEC</li>
</ul>

<p><strong>Ressources</strong> :</p>
<ul>
<li>Supports de cours : cryptography.pdf, Hardware-Security.pdf, ebios.pdf</li>
<li>Outils : mbedTLS, pycryptodome, OpenSSL</li>
<li>Rapports : Rapport Lab1 (injection SQL, XSS)</li>
</ul>

<h3 class="section-title">Environnement et contexte</h3>

<p>Au cours de ce module, j'ai travaille sur les aspects theoriques et pratiques de la securite IoT. La pertinence de la securisation des dispositifs IoT dans le monde interconnecte actuel est evidente : chaque objet connecte represente une surface d'attaque potentielle. Les laboratoires pratiques m'ont permis d'appliquer les concepts appris en cours a des scenarios realistes, passant de la theorie cryptographique a l'exploitation concrete de vulnerabilites.</p>

<h3 class="section-title">Mon role</h3>

<p>Dans ce cours, j'ai ete responsable de :</p>
<ul>
<li>Comprendre et implementer divers protocoles de securite et techniques cryptographiques</li>
<li>Mettre en oeuvre des mesures de securite pour les dispositifs IoT</li>
<li>Mener des experimentations pour identifier et attenuer les vulnerabilites de securite</li>
<li>Analyser et prevenir les attaques Man-in-the-Middle (MITM) sur les protocoles de communication IoT</li>
<li>Realiser des challenges CTF pour tester mes competences en cryptanalyse</li>
<li>Travailler avec la distribution quantique de cles (QKD) pour explorer la securite post-quantique</li>
</ul>

<hr>

<h2>PART C : ASPECTS TECHNIQUES</h2>

<p>Cette section explore en detail les aspects techniques de la securite des objets connectes, couvrant la cryptographie, les protocoles de securite, la securite materielle, les menaces IoT, et les travaux pratiques realises.</p>

<hr>

<h3 class="section-title">1. Cryptographie symetrique</h3>

<p>La cryptographie symetrique utilise la meme cle pour le chiffrement et le dechiffrement. Elle est rapide et efficace pour le chiffrement de donnees volumineuses, mais necessite un canal securise pour la distribution de la cle.</p>

<h4>1.1 AES (Advanced Encryption Standard)</h4>

<p>L'AES est le standard de chiffrement symetrique mondial depuis 2001. Il chiffre les donnees par blocs de 128 bits avec des cles de 128, 192 ou 256 bits.</p>

<p>L'algorithme AES est compose de plusieurs rondes de traitement, chacune impliquant quatre operations principales :</p>

<ol>
<li><strong>AddRoundKey</strong> : chaque octet de l'etat est combine avec un bloc de la sous-cle de ronde par un XOR bit a bit. Cette etape est cruciale car elle introduit la cle dans le processus de chiffrement.</li>
<li><strong>SubBytes</strong> : etape de substitution non lineaire ou chaque octet de l'etat est remplace par un autre via une S-box (boite de substitution). La S-box est concue pour resister aux cryptanalyses lineaires et differentielles.</li>
<li><strong>ShiftRows</strong> : les lignes de l'etat sont decalees cycliquement vers la gauche. Le decalage depend de l'indice de la ligne. Cette etape assure la diffusion du texte clair.</li>
<li><strong>MixColumns</strong> : operation de melange operant sur les colonnes de l'etat, combinant les quatre octets de chaque colonne. Cette etape garantit une diffusion supplementaire.</li>
</ol>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/aes.png" style="width: 90%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure : Etapes de l'algorithme AES - SubBytes, ShiftRows, MixColumns, AddRoundKey
</p>
<br>

<p><strong>Nombre de rondes selon la taille de la cle</strong> :</p>

<table>
<tr><th>Taille de cle</th><th>Nombre de rondes</th><th>Applications typiques</th></tr>
<tr><td>128 bits</td><td>10 rondes</td><td>Usage general, Wi-Fi (WPA2)</td></tr>
<tr><td>192 bits</td><td>12 rondes</td><td>Donnees sensibles</td></tr>
<tr><td>256 bits</td><td>14 rondes</td><td>Donnees classifiees, militaire</td></tr>
</table>

<p>Dans notre <a href="./innovative-project.html#3-security-features">Projet Innovant (What a Leak)</a>, nous avons implemente l'algorithme AES avec des concepts supplementaires : vecteur d'initialisation (IV), padding, et PKCS#7.</p>

<h4>1.2 DES (Data Encryption Standard)</h4>

<p>Le DES, predecesseur de l'AES, utilise des blocs de 64 bits et une cle de 56 bits. Bien qu'obsolete aujourd'hui en raison de la taille reduite de sa cle (vulnerable au brute force), il reste important pour comprendre l'evolution de la cryptographie symetrique. Le Triple-DES (3DES) applique DES trois fois avec des cles differentes pour renforcer la securite.</p>

<h4>1.3 Modes de chiffrement par blocs</h4>

<p>Les modes de chiffrement definissent comment les blocs successifs sont traites :</p>

<table>
<tr><th>Mode</th><th>Description</th><th>Avantages</th><th>Inconvenients</th></tr>
<tr><td><strong>ECB</strong> (Electronic Codebook)</td><td>Chaque bloc chiffre independamment</td><td>Simple, parallelisable</td><td>Motifs visibles, non securise</td></tr>
<tr><td><strong>CBC</strong> (Cipher Block Chaining)</td><td>Chaque bloc XOR avec le bloc chiffre precedent</td><td>Masque les motifs</td><td>Sequentiel, erreur propagee</td></tr>
<tr><td><strong>CTR</strong> (Counter)</td><td>Chiffrement d'un compteur, XOR avec le texte</td><td>Parallelisable, pas de padding</td><td>Compteur ne doit jamais se repeter</td></tr>
<tr><td><strong>GCM</strong> (Galois/Counter Mode)</td><td>CTR + authentification integree</td><td>Chiffrement authentifie</td><td>Plus complexe</td></tr>
</table>

<h4>1.4 Chiffre de Cesar</h4>

<p>Nous avons egalement etudie le chiffre de Cesar, une technique de chiffrement simple ou chaque lettre du texte clair est decalee d'un nombre fixe de positions dans l'alphabet. Bien qu'il ne soit pas securise selon les standards modernes, il a permis de comprendre les bases du chiffrement et du dechiffrement par substitution.</p>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/cypher.png" style="width: 40%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure : Principe du chiffre de Cesar - decalage alphabetique
</p>
<br>

<hr>

<h3 class="section-title">2. Cryptographie asymetrique</h3>

<p>La cryptographie asymetrique utilise une paire de cles (publique et privee) pour le chiffrement et le dechiffrement. Elle renforce la securite au prix de performances reduites par rapport au chiffrement symetrique.</p>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/asymetric.png" style="width: 70%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure : Principe de la cryptographie asymetrique - cle publique / cle privee
</p>
<br>

<h4>2.1 RSA (Rivest-Shamir-Adleman)</h4>

<p>RSA est l'algorithme asymetrique le plus repandu. Sa securite repose sur la difficulte de factoriser de grands nombres premiers.</p>

<p><strong>Principe</strong> :</p>
<ol>
<li>Generer deux grands nombres premiers p et q</li>
<li>Calculer n = p * q (module)</li>
<li>Calculer phi(n) = (p-1)(q-1)</li>
<li>Choisir l'exposant public e (generalement 65537)</li>
<li>Calculer l'exposant prive d = e^(-1) mod phi(n)</li>
</ol>

<p><strong>Chiffrement</strong> : C = M^e mod n<br>
<strong>Dechiffrement</strong> : M = C^d mod n</p>

<p>En laboratoire, nous avons implemente RSA dans le fichier <code>2/source.py</code> : le script genere deux grands nombres premiers, calcule leur produit (n), et utilise l'exposant public (e) pour chiffrer un message. L'exposant prive (d) dechiffre le texte chiffre.</p>

<p><strong>Attaque par racine cubique</strong> : Nous avons egalement explore une attaque sur RSA lorsque l'exposant public (e) est petit (e = 3). Si le texte chiffre (c) est suffisamment petit, on peut retrouver le texte clair en calculant la racine cubique entiere de c. Cette attaque a ete implementee dans <code>2/attack.py</code>.</p>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/flag4.png" style="width: 30%;"/>
    <img src="/img/BE_Secu/flag1.png" style="width: 50%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure : CTF - Flag obtenu apres attaque par racine cubique sur RSA
</p>
<br>

<h4>2.2 ECC (Elliptic Curve Cryptography)</h4>

<p>La cryptographie sur courbes elliptiques offre un niveau de securite equivalent a RSA avec des cles beaucoup plus courtes. Une cle ECC de 256 bits equivaut a une cle RSA de 3072 bits. ECC est particulierement adaptee aux objets connectes grace a sa faible empreinte memoire et sa rapidite de calcul.</p>

<p><strong>Avantages pour l'IoT</strong> :</p>
<ul>
<li>Cles plus courtes : moins de stockage et de bande passante</li>
<li>Calculs plus rapides : moins de consommation energetique</li>
<li>Securite equivalente : robustesse cryptographique maintenue</li>
</ul>

<h4>2.3 Diffie-Hellman</h4>

<p>L'echange de cles Diffie-Hellman permet a deux parties d'etablir un secret partage sur un canal non securise, sans transmission directe de la cle. Ce protocole est a la base de nombreux protocoles de securite (TLS, IPsec, SSH).</p>

<p><strong>Principe</strong> :</p>
<ol>
<li>Alice et Bob conviennent d'un nombre premier p et d'un generateur g</li>
<li>Alice choisit un secret a, calcule A = g^a mod p, et envoie A</li>
<li>Bob choisit un secret b, calcule B = g^b mod p, et envoie B</li>
<li>Alice calcule la cle partagee : K = B^a mod p</li>
<li>Bob calcule la meme cle : K = A^b mod p</li>
</ol>

<p>La securite repose sur la difficulte du probleme du logarithme discret.</p>

<hr>

<h3 class="section-title">3. Fonctions de hachage</h3>

<p>Les fonctions de hachage prennent une entree de taille arbitraire et produisent une empreinte de taille fixe. Elles sont utilisees pour la verification d'integrite des donnees, le stockage de mots de passe et les signatures numeriques.</p>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/hash.png" style="width: 60%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure : Principe d'une fonction de hachage - empreinte de taille fixe
</p>
<br>

<p><strong>Proprietes essentielles</strong> :</p>
<ul>
<li><strong>Resistance a la pre-image</strong> : impossible de retrouver l'entree a partir du hash</li>
<li><strong>Resistance aux collisions</strong> : impossible de trouver deux entrees differentes produisant le meme hash</li>
<li><strong>Effet avalanche</strong> : un changement minime en entree modifie radicalement la sortie</li>
</ul>

<h4>3.1 SHA-256</h4>

<p>SHA-256 (Secure Hash Algorithm) produit une empreinte de 256 bits (32 octets). C'est l'algorithme de hachage recommande pour la plupart des applications modernes, y compris les certificats numeriques et la blockchain.</p>

<h4>3.2 MD5</h4>

<p>MD5 produit une empreinte de 128 bits. Bien que tres repandu historiquement, il est considere comme compromis depuis la decouverte de collisions en 2004. Il reste utilise pour la verification rapide d'integrite de fichiers (checksums) mais ne doit plus etre employe pour des applications de securite.</p>

<p>Dans notre laboratoire cryptographique, MD5 a ete utilise pour generer une cle AES de 128 bits a partir d'un mot-cle selectionne aleatoirement. Cela a permis d'illustrer la generation de cles derivees (key derivation) a partir de mots de passe.</p>

<h4>3.3 Fonctions de hachage legeres pour IoT</h4>

<p>Nous avons etudie les fonctions de hachage legeres specifiees dans la norme ISO/IEC 29192-5:2016, concues pour les dispositifs a ressources limitees :</p>

<ul>
<li><strong>PHOTON</strong> : fonction de hachage legere avec des tailles de permutation de 100, 144, 196, 256 et 288 bits, produisant des hash de 80, 128, 160, 224 et 256 bits respectivement.</li>
<li><strong>SPONGENT</strong> : fonction de hachage legere avec des tailles de permutation de 88, 136, 176, 240 et 272 bits, produisant des hash de 88, 128, 160, 224 et 256 bits respectivement.</li>
<li><strong>Lesamnta-LW</strong> : fonction de hachage legere avec une taille de permutation de 384 bits, produisant un hash de 256 bits.</li>
</ul>

<hr>

<h3 class="section-title">4. Certificats numeriques et PKI</h3>

<h4>4.1 Infrastructure a cles publiques (PKI)</h4>

<p>La PKI est un ensemble de roles, politiques et procedures necessaires pour creer, gerer, distribuer, utiliser, stocker et revoquer des certificats numeriques. Elle repose sur une chaine de confiance :</p>

<ul>
<li><strong>Autorite de Certification (CA)</strong> : emet et signe les certificats</li>
<li><strong>Autorite d'Enregistrement (RA)</strong> : verifie l'identite des demandeurs</li>
<li><strong>Certificat X.509</strong> : contient la cle publique, l'identite du proprietaire, la signature de la CA, la periode de validite</li>
</ul>

<h4>4.2 Common Name et verification</h4>

<p>Dans le contexte de la verification des certificats, le Common Name (CN) est un attribut essentiel. Il fait partie du champ Subject du certificat et represente generalement le nom de domaine ou l'identite du detenteur du certificat. Lors du processus de verification, le CN est compare au nom d'hote ou a l'identite attendue pour s'assurer que le certificat est valide pour le destinataire prevu.</p>

<p>Par exemple, si un certificat est emis pour <code>www.alice.com</code>, le CN doit correspondre a <code>www.alice.com</code>. En cas de non-concordance, le processus de verification echouera, signalant un probleme de securite potentiel. Cette verification aide a prevenir les attaques Man-in-the-Middle en s'assurant que le certificat presente par un serveur correspond a l'identite attendue.</p>

<hr>

<h3 class="section-title">5. Protocoles TLS/SSL</h3>

<h4>5.1 TLS (Transport Layer Security)</h4>

<p>TLS est le protocole de securite le plus deploye pour securiser les communications sur Internet. Il assure la confidentialite, l'integrite et l'authentification des echanges.</p>

<p><strong>Fonctionnement du handshake TLS</strong> :</p>
<ol>
<li><strong>ClientHello</strong> : le client envoie les suites cryptographiques supportees</li>
<li><strong>ServerHello</strong> : le serveur selectionne une suite et envoie son certificat</li>
<li><strong>Echange de cles</strong> : Diffie-Hellman ou RSA pour etablir un secret partage</li>
<li><strong>Derivation de cles</strong> : generation des cles de session a partir du secret</li>
<li><strong>Communication chiffree</strong> : echanges proteges par chiffrement symetrique (AES-GCM)</li>
</ol>

<h4>5.2 Migration TLS en laboratoire</h4>

<p>Lors du Lab 3, nous avons travaille sur la migration TLS en utilisant la bibliotheque mbedTLS. L'objectif etait de securiser les communications entre Alice et Bob en implementant un handshake TLS complet, incluant l'echange de certificats, la verification de la chaine de confiance, et le chiffrement des messages.</p>

<hr>

<h3 class="section-title">6. Securite materielle</h3>

<p>La securite materielle traite des vulnerabilites physiques des systemes electroniques. Meme un algorithme mathematiquement sur peut etre compromis par des attaques sur son implementation physique.</p>

<h4>6.1 Attaques par canaux auxiliaires (Side-Channel Attacks)</h4>

<p>Les attaques par canaux auxiliaires exploitent les fuites d'information physiques lors de l'execution d'algorithmes cryptographiques :</p>

<table>
<tr><th>Type d'attaque</th><th>Canal exploite</th><th>Technique</th></tr>
<tr><td><strong>Timing Attack</strong></td><td>Temps d'execution</td><td>Mesure des variations temporelles</td></tr>
<tr><td><strong>Power Analysis (SPA/DPA/CPA)</strong></td><td>Consommation electrique</td><td>Correlation entre donnees et consommation</td></tr>
<tr><td><strong>EM Analysis</strong></td><td>Emissions electromagnetiques</td><td>Capture des radiations EM</td></tr>
<tr><td><strong>Cache Attack</strong></td><td>Comportement du cache CPU</td><td>Flush+Reload, Prime+Probe</td></tr>
</table>

<p><strong>Exemple sur AES</strong> : Les tables de substitution (S-box) d'AES sont stockees en memoire. L'acces a ces tables depend de la cle et du message. Si une partie de la table est en cache (acces rapide) et une autre non (acces lent), on peut deduire quelle partie a ete accedee et progressivement recuperer la cle.</p>

<h4>6.2 Injection de fautes (Fault Injection)</h4>

<p>L'injection de fautes provoque volontairement des erreurs lors de l'execution pour obtenir des informations ou contourner des protections :</p>
<ul>
<li><strong>Clock glitching</strong> : impulsions sur l'horloge causant des instructions sautees</li>
<li><strong>Voltage glitching</strong> : variation de la tension d'alimentation causant des erreurs de calcul</li>
<li><strong>Laser</strong> : faisceau laser focalise modifiant des bits en memoire</li>
</ul>

<h4>6.3 Elements securises (Secure Elements)</h4>

<p>Les elements securises sont des composants materiels dedies a la protection des donnees sensibles :</p>
<ul>
<li><strong>TPM (Trusted Platform Module)</strong> : puce securisee pour le stockage de cles et l'attestation</li>
<li><strong>Secure Enclave</strong> : environnement d'execution isole (ARM TrustZone, Intel SGX)</li>
<li><strong>HSM (Hardware Security Module)</strong> : module materiel haute securite pour la gestion de cles</li>
</ul>

<p>Ces elements sont essentiels dans l'IoT pour proteger les cles cryptographiques, les identites des dispositifs, et assurer le demarrage securise (Secure Boot).</p>

<hr>

<h3 class="section-title">7. Menaces specifiques a l'IoT - OWASP IoT Top 10</h3>

<p>L'OWASP (Open Web Application Security Project) identifie les 10 principales vulnerabilites des objets connectes :</p>

<table>
<tr><th>Rang</th><th>Vulnerabilite</th><th>Description</th></tr>
<tr><td>1</td><td>Mots de passe faibles</td><td>Identifiants par defaut, non modifies</td></tr>
<tr><td>2</td><td>Services reseau non securises</td><td>Ports ouverts, services inutiles exposes</td></tr>
<tr><td>3</td><td>Interfaces ecosysteme non securisees</td><td>API, cloud, interfaces web vulnerables</td></tr>
<tr><td>4</td><td>Absence de mecanisme de mise a jour</td><td>Pas de firmware OTA securise</td></tr>
<tr><td>5</td><td>Composants non securises ou obsoletes</td><td>Bibliotheques vulnerables</td></tr>
<tr><td>6</td><td>Protection insuffisante de la vie privee</td><td>Collecte excessive de donnees</td></tr>
<tr><td>7</td><td>Transfert et stockage de donnees non securises</td><td>Donnees en clair</td></tr>
<tr><td>8</td><td>Manque de gestion des dispositifs</td><td>Inventaire, monitoring insuffisants</td></tr>
<tr><td>9</td><td>Parametres par defaut non securises</td><td>Configurations usine dangereuses</td></tr>
<tr><td>10</td><td>Manque de durcissement physique</td><td>Acces physique non protege</td></tr>
</table>

<hr>

<h3 class="section-title">8. Methodologie d'analyse de risques EBIOS</h3>

<p>EBIOS (Expression des Besoins et Identification des Objectifs de Securite) est la methode francaise de reference pour l'analyse de risques en securite de l'information, developpee par l'ANSSI.</p>

<p><strong>Les 5 ateliers EBIOS Risk Manager</strong> :</p>
<ol>
<li><strong>Cadrage et socle de securite</strong> : identifier les missions, les valeurs metier, et le perimetre</li>
<li><strong>Sources de risque</strong> : identifier les sources de menace et leurs objectifs vises</li>
<li><strong>Scenarios strategiques</strong> : elaborer les chemins d'attaque de haut niveau</li>
<li><strong>Scenarios operationnels</strong> : detailler les modes operatoires techniques</li>
<li><strong>Traitement du risque</strong> : definir les mesures de securite et le plan d'action</li>
</ol>

<p>Cette methodologie est particulierement pertinente pour les systemes IoT ou les surfaces d'attaque sont multiples (reseau, physique, cloud, firmware).</p>

<hr>

<h3 class="section-title">9. Confidentialite, integrite et authenticite</h3>

<p>Les trois piliers fondamentaux de la securite de l'information (triade CIA) :</p>

<ul>
<li><strong>Confidentialite</strong> : garantir que l'information n'est accessible qu'aux personnes autorisees. Assuree par le chiffrement (AES, RSA, TLS).</li>
<li><strong>Integrite</strong> : garantir que l'information est exacte et n'a pas ete alteree. Assuree par les fonctions de hachage (SHA-256) et les MAC (Message Authentication Code).</li>
<li><strong>Authenticite</strong> : verifier l'identite des parties impliquees dans la communication. Assuree par les signatures numeriques et les certificats (PKI).</li>
</ul>

<hr>

<h3 class="section-title">10. Travaux pratiques - Labs de securite</h3>

<h4>10.1 Injection SQL (Lab 1)</h4>

<p>J'ai etudie les attaques par injection SQL et comment elles peuvent etre utilisees pour extraire des informations d'une base de donnees. Par exemple, en entrant <code>admin' OR 1=1 OR '1'='1</code> dans le champ d'authentification et un mot de passe arbitraire comme <code>vhjvg</code>, un attaquant peut contourner le mecanisme d'authentification. La requete SQL devient toujours vraie, permettant un acces non autorise aux donnees sensibles. Comprendre cette vulnerabilite m'a aide a implementer des mesures de prevention dans les systemes IoT.</p>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/SQL_injection.png" style="width: 60%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure : Demonstration d'une attaque par injection SQL - contournement de l'authentification
</p>
<br>

<p><strong>Mesures de prevention</strong> :</p>
<ul>
<li>Utilisation de requetes parametrees (prepared statements)</li>
<li>Validation et assainissement des entrees utilisateur</li>
<li>Principe du moindre privilege pour les comptes de base de donnees</li>
<li>Utilisation d'un ORM (Object-Relational Mapping)</li>
</ul>

<h4>10.2 Cross-Site Scripting - XSS (Lab 1)</h4>

<p>Nous avons explore les attaques XSS, qui impliquent l'injection de scripts malveillants dans les pages web consultees par d'autres utilisateurs. Cela peut mener au vol de donnees, au detournement de session, et a d'autres activites malveillantes.</p>

<p>Par exemple, nous avons execute du code JavaScript dans le champ de nom d'utilisateur en entrant <code>&lt;script&gt;alert('Bonjour');&lt;/script&gt;</code> ou <code>&lt;script&gt;document.write("&lt;img src='xxxx'/&gt;");&lt;/script&gt;</code>. Cela a demontre comment un attaquant pourrait injecter des scripts pour manipuler la page web ou voler des informations. Les repercussions de telles attaques peuvent etre severes : acces non autorise aux donnees utilisateur et propagation de malwares.</p>

<h4>10.3 Attaque Man-in-the-Middle - MITM (Lab 3)</h4>

<p>J'ai etudie les attaques Man-in-the-Middle, ou un attaquant intercepte et altere potentiellement la communication entre deux parties sans leur connaissance. Ce type d'attaque peut mener a des violations de donnees et a un acces non autorise a des informations sensibles.</p>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/Man_Middle.png" style="width: 60%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure : Schema d'une attaque Man-in-the-Middle - interception des communications
</p>
<br>

<p>Dans le fichier attaquant, nous avons implemente une attaque MITM simple en utilisant la bibliotheque mbedTLS. L'attaquant intercepte et modifie les messages entre Alice et Bob. L'attaquant lit le message de Bob, l'altere, puis envoie le message modifie a Alice. Cela demontre comment un attaquant peut manipuler la communication entre deux parties, soulignant l'importance de securiser les communications.</p>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/lab3_terminal.png" style="width: 100%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure : Terminal Lab3 - Interception et modification de messages par l'attaquant
</p>
<br>

<p>Lors du Lab 3, nous avons travaille sur un scenario ou Alice envoie un certificat a Bob. Bob recoit le certificat et le verifie. Simultanement, un hacker intercepte et imprime la cle. Bob envoie ensuite un message a Alice, mais le hacker intercepte le message, l'altere, et envoie le message modifie a Alice.</p>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/lab3_terminal2.png" style="width: 100%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure : Lab3 - Scenario d'interception de certificat et de cle
</p>
<br>

<p>Correction :</p>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/lab3_terminal3.png" style="width: 100%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure : Lab3 - Correction et verification du Common Name
</p>
<br>

<h4>10.4 Migration TLS (Lab 3)</h4>

<p>La migration TLS consistait a securiser les communications en implementant le protocole TLS complet avec mbedTLS. L'objectif etait de passer d'une communication en clair a une communication chiffree et authentifiee, en integrant :</p>
<ul>
<li>L'echange de certificats X.509</li>
<li>La verification de la chaine de confiance</li>
<li>Le chiffrement des messages avec AES-GCM</li>
<li>La protection contre les attaques de rejeu (replay attacks)</li>
</ul>

<h4>10.5 Challenges CTF cryptographiques (Lab 4)</h4>

<h5>Chiffrement AES - CTF</h5>

<p>Dans le fichier <code>1/source.py</code>, nous avons implemente le chiffrement et le dechiffrement AES en utilisant la bibliotheque pycryptodome :</p>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/flag3.png" style="width: 30%;"/>
    <img src="/img/BE_Secu/flag1.png" style="width: 50%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure : CTF - Flags obtenus apres dechiffrement AES par brute force sur dictionnaire
</p>
<br>

<p>Le processus du challenge :</p>
<ol>
<li><strong>Selection du mot-cle</strong> : le script lit une liste de mots depuis un fichier <code>words</code> et en selectionne un aleatoirement</li>
<li><strong>Generation de la cle</strong> : le mot-cle selectionne est hache avec MD5 pour generer une cle AES de 128 bits</li>
<li><strong>Chiffrement du flag</strong> : le flag predefini est complete (padding) a un multiple de la taille de bloc AES (16 octets) et chiffre en mode ECB</li>
<li><strong>Dechiffrement du flag</strong> : le flag chiffre est dechiffre avec la meme cle pour valider le processus</li>
</ol>

<h5>Chiffrement RSA - CTF</h5>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/flag4.png" style="width: 30%;"/>
    <img src="/img/BE_Secu/flag2.png" style="width: 50%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure : CTF - Flag obtenu apres exploitation de la vulnerabilite RSA
</p>
<br>

<hr>

<h3 class="section-title">11. Lab Quantique</h3>

<h4>11.1 Protocole NEC</h4>

<p>Nous avons etabli une communication entre deux cartes en utilisant le protocole NEC, couramment utilise dans les telecommandes. L'emetteur encode les messages en format NEC et les envoie via des impulsions infrarouges. Le recepteur decode ces signaux pour retrouver le message original.</p>

<p><strong>Exemple</strong> :</p>
<ul>
<li><strong>Emetteur</strong> : encode "A" en format NEC et l'envoie</li>
<li><strong>Recepteur</strong> : decode le signal infrarouge pour retrouver "A"</li>
</ul>

<p>Cet exercice a demontre l'importance de la precision du timing et de la fiabilite dans la communication infrarouge.</p>

<p><strong>Donnees du signal pour "A"</strong> :</p>
<ul>
<li><strong>Format NEC</strong> : le protocole NEC utilise une trame de 32 bits. Pour le caractere "A", les donnees du signal sont encodees comme suit :
    <ul>
    <li><strong>Adresse</strong> : 0x8D</li>
    <li><strong>Adresse inverse</strong> : 0x72</li>
    <li><strong>Commande</strong> : 0x45 (code ASCII pour "A")</li>
    <li><strong>Commande inverse</strong> : 0x4E</li>
    </ul>
</li>
</ul>

<p>La trame complete de 32 bits pour "A" est : <code>0x8D72454E</code>.</p>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/nec.png" style="width: 90%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure : Protocole NEC - Structure de la trame infrarouge
</p>
<br>

<h4>11.2 Distribution quantique de cles (QKD)</h4>

<p>Apres avoir realise le test classique sur <code>/dev/tty1CM0</code>, nous avons procede au test quantique sur <code>/dev/ttyACM1</code>. Nous avons d'abord effectue une calibration en reglant l'angle a 0, la resolution de balayage a 1, l'offset a 0, et la polarisation a 0. Nous avons ensuite converti le signal de luminosite en tension en balayant et mesurant l'intensite apres le polariseur lineaire lors d'une rotation complete de 360 degres. Suite a la calibration, nous avons execute un script Python pour automatiser la distribution de cles et generer une cle de 32 kbit.</p>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/cute.png" style="width: 25%;"/>
    <img src="/img/BE_Secu/hdva.png" style="width: 40%;"/>
    <img src="/img/BE_Secu/key.png" style="width: 40%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure : Distribution quantique de cles - Montage experimental et generation de cle
</p>
<br>

<p>De plus, nous avons introduit un prisme dans le montage, permettant aux signaux lumineux de Bob, Alice et Eve de le traverser. Cela a ete realise pour faciliter le partage de la cle avec un autre utilisateur. Le prisme a aide a diviser les signaux lumineux, assurant que la distribution de la cle puisse etre partagee de maniere securisee avec le nouvel utilisateur sans compromettre l'integrite de la communication originale.</p>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/prisme.png" style="width: 90%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure : Montage avec prisme - Partage de cle quantique multi-utilisateurs
</p>
<br>

<hr>

<h2>PART D : ANALYSE ET REFLEXION</h2>

<h3 class="section-title">Competences acquises</h3>

<p><strong>Maitrise de la cryptographie</strong> :<br>
Capacite a comprendre, implementer et evaluer les algorithmes cryptographiques (AES, RSA, ECC, fonctions de hachage) et a choisir les solutions adaptees aux contraintes IoT.</p>

<p><strong>Securisation des communications</strong> :<br>
Aptitude a mettre en oeuvre les protocoles TLS/SSL, a gerer les certificats numeriques via une PKI, et a securiser les echanges entre dispositifs IoT.</p>

<p><strong>Analyse de vulnerabilites</strong> :<br>
Competence en identification et exploitation de failles de securite (injection SQL, XSS, MITM) pour mieux concevoir des contre-mesures.</p>

<p><strong>Securite materielle</strong> :<br>
Comprehension des attaques par canaux auxiliaires, de l'injection de fautes, et des elements securises pour la protection physique des dispositifs.</p>

<p><strong>Analyse de risques</strong> :<br>
Capacite a conduire une analyse de risques methodique (EBIOS) adaptee aux systemes IoT.</p>

<p><strong>Vision globale</strong> :<br>
Integration de la securite dans l'ensemble du cycle de vie d'un systeme IoT, de la conception au deploiement.</p>

<h3 class="section-title">Points cles a retenir</h3>

<p><strong>1. La securite est multicouche</strong> :<br>
La protection d'un systeme IoT necessite des mesures a tous les niveaux : physique, reseau, applicatif, et organisationnel. Une approche de defense en profondeur est indispensable.</p>

<p><strong>2. La cryptographie est necessaire mais pas suffisante</strong> :<br>
Un algorithme mathematiquement sur peut etre vulnerable si son implementation fuit des informations (canaux auxiliaires). La securite depend de la qualite de l'implementation autant que de l'algorithme.</p>

<p><strong>3. L'IoT amplifie les risques</strong> :<br>
Le nombre massif de dispositifs, les contraintes de ressources, et les mises a jour difficiles rendent la securite IoT particulierement complexe.</p>

<p><strong>4. La pratique est essentielle</strong> :<br>
Les labs CTF, les attaques MITM, et les injections SQL m'ont permis de passer de la theorie a la pratique, renforant ma comprehension operationnelle.</p>

<p><strong>5. Le quantique est l'avenir</strong> :<br>
L'experimentation QKD a ouvert une perspective fascinante sur la cryptographie post-quantique et la distribution securisee de cles.</p>

<h3 class="section-title">Retour d'experience</h3>

<p>J'avais deja un premier apercu de la plupart de ces concepts, mais ce cours a fourni une perspective plus avancee et technique. Nous avons approfondi le codage en C avec mbedTLS et teste des attaques par injection SQL. Ce dernier point a ete un peu difficile pour moi puisque je n'avais jamais utilise SQL auparavant, et j'ai du apprendre rapidement pour etre efficace.</p>

<p>Par ailleurs, de nombreux concepts expliques en cours n'ont pas ete pratiques. J'ai le sentiment de ne pas etre totalement a jour partout car certains sujets restaient purement theoriques. Les explications du professeur pendant les cours etaient un plus pour moi car elles etaient claires, et je voulais etre operationnel sur ces concepts.</p>

<p>De plus, travailler seul pendant les sessions de laboratoire m'a pousse a travailler plus intensement pour comprendre tous les concepts en profondeur.</p>

<h3 class="section-title">Mon avis</h3>

<p>Ce cours a ete tres interessant et stimulant. J'ai beaucoup appris sur les vulnerabilites de securite et comment les prevenir. Dans ma future carriere, je suis interesse par le domaine de la securite, ce qui signifie que je dois rester informe des dernieres menaces. J'ai vraiment apprecie les travaux pratiques qui m'ont permis d'appliquer les concepts appris en cours, et je suis un peu decu que nous n'ayons pas eu plus de temps pour explorer d'autres concepts de securite.</p>

<p>A la fin du semestre, nous avons eu un lab quantique qui etait vraiment passionnant. Malheureusement, nous etions la "classe test" car personne ne l'avait fait auparavant. Meme si nous avons rencontre quelques problemes pour le finaliser, travailler en partenariat avec les enseignants a ete une excellente experience. J'espere decouvrir davantage le quantique a l'avenir car c'est un domaine fascinant.</p>

<h3 class="section-title">Perspectives professionnelles</h3>

<p><strong>Pour ingenieur en securite IoT</strong> :</p>
<ul>
<li>Audit de securite de systemes connectes</li>
<li>Conception de produits IoT securises (secure by design)</li>
<li>Tests de penetration et red teaming sur les systemes embarques</li>
</ul>

<p><strong>Pour developpeur embarque</strong> :</p>
<ul>
<li>Implementation correcte des algorithmes cryptographiques</li>
<li>Integration de TLS/SSL dans les communications IoT</li>
<li>Utilisation d'elements securises (TPM, Secure Enclave)</li>
</ul>

<p><strong>Lien avec le Projet Innovant</strong> :<br>
Les competences acquises dans ce cours ont ete directement appliquees dans notre <a href="./innovative-project.html#3-security-features">Projet Innovant (What a Leak)</a>, ou nous avons implemente le chiffrement AES avec vecteur d'initialisation et padding PKCS#7 pour securiser les communications de notre systeme IoT de detection de fuites d'eau.</p>

<hr>

<h2>Rapports et Projets</h2>

<div style="text-align: center;">
    <h3>Rapport de Laboratoire - Lab 1 (Injection SQL, XSS)</h3>
</div>

<div style="display: flex; justify-content: center;">
    <iframe src="/file/reports/S9/Rapport_Lab1.pdf" width="100%" height="800px" style="overflow: auto;" frameborder="0"></iframe>
</div>

<p style="text-align: center;">
    <a href="/file/reports/S9/Rapport_Lab1.pdf" target="_blank">
        Ouvrir le rapport complet - Lab 1
    </a>
</p>

<hr>
<p><em>Cours suivi en 2024-2025 a l'INSA Toulouse, Departement Genie Electrique et Informatique, Semestre 9.</em></p>

</div>

<div class="lang-en">

<p><strong>Related courses</strong>:</p>
<ul>
<li><a href="./middleware-iot.html">Middleware for IoT - S9</a> - Secure communication protocols</li>
<li><a href="./emerging-network.html">Emerging Network Technologies - S9</a> - SDN network security</li>
<li><a href="../2023-2024/2024-10-03-securite-materielle.html">Hardware Security - S7</a> - Hardware security fundamentals</li>
</ul>

<hr>

<h1>Security for Connected Objects - Semester 9</h1>

<p><strong>Academic year</strong>: 2024-2025<br>
<strong>Semester</strong>: S9<br>
<strong>Instructors</strong>: E. Alata, V. Migliore<br>
<strong>Category</strong>: IoT Security and Cryptography</p>

<hr>

<h2>PART A: GENERAL PRESENTATION</h2>

<h3 class="section-title">Overview</h3>

<p>The "Security for Connected Objects" course taught by E. Alata and V. Migliore is an essential pillar of my training in connected systems security. This module comprehensively covers the security mechanisms required for IoT devices: symmetric and asymmetric cryptography, hash functions, TLS/SSL protocols, digital certificates and Public Key Infrastructure (PKI), hardware security, IoT-specific threats, and the EBIOS risk analysis methodology.</p>

<p>The course combines in-depth theory with intensive hands-on practice through concrete laboratory work: CTF (Capture The Flag) challenges, SQL injection attacks, Man-in-the-Middle (MITM) attacks, TLS migration, and quantum experimentation. This approach allowed me to develop an operational understanding of connected object security.</p>

<p><strong>Learning objectives</strong>:</p>
<ul>
<li>Understand the foundations of modern cryptography (symmetric, asymmetric, hashing)</li>
<li>Master security protocols for IoT communications (TLS/SSL, PKI)</li>
<li>Identify security weaknesses in an IoT architecture (OWASP IoT Top 10)</li>
<li>Assess the impact of exploiting a security vulnerability</li>
<li>Propose adequate security countermeasures</li>
<li>Conduct a risk analysis using the EBIOS methodology</li>
<li>Understand hardware security: side-channel attacks, fault injection, secure elements</li>
</ul>

<h3 class="section-title">Position in the curriculum</h3>

<p>This module is part of a pedagogical continuity:</p>
<ul>
<li><strong>Hardware Security (S7)</strong>: side-channel attacks, buffer overflow, power analysis</li>
<li><strong>Microcontrollers and Hardware (S9)</strong>: embedded systems, FPGA, hardware architecture</li>
<li><strong>Middleware for IoT (S9)</strong>: secure communication protocols (MQTT, TLS)</li>
<li><strong>Emerging Network Technologies (S9)</strong>: SDN/NFV network security</li>
</ul>

<p>It directly prepares for:</p>
<ul>
<li><strong>Innovative Project (S9)</strong>: AES implementation and securing a complete IoT system</li>
<li><strong>Cybersecurity career</strong>: security auditing, pentesting, secure design</li>
<li><strong>Research</strong>: post-quantum cryptography, advanced hardware security</li>
</ul>

<hr>

<h2>PART B: EXPERIENCE AND CONTEXT</h2>

<h3 class="section-title">Organization and resources</h3>

<p>The module was structured around lectures and intensive lab sessions:</p>

<p><strong>Lectures</strong>:</p>
<ul>
<li>Symmetric cryptography (AES, DES, block cipher modes)</li>
<li>Asymmetric cryptography (RSA, ECC, Diffie-Hellman)</li>
<li>Hash functions (SHA-256, MD5, lightweight functions for IoT)</li>
<li>Digital certificates and PKI (Public Key Infrastructure)</li>
<li>TLS/SSL protocols and communication security</li>
<li>Hardware security (side-channel attacks, fault injection)</li>
<li>IoT-specific threats (OWASP IoT Top 10)</li>
<li>EBIOS risk analysis methodology</li>
</ul>

<p><strong>Lab sessions</strong>:</p>
<ul>
<li><strong>Lab 1</strong>: SQL Injection and Cross-Site Scripting (XSS)</li>
<li><strong>Lab 2</strong>: Symmetric and asymmetric encryption (AES, RSA)</li>
<li><strong>Lab 3</strong>: Man-in-the-Middle attack, TLS migration, certificates</li>
<li><strong>Lab 4</strong>: Cryptographic CTF challenges (flags)</li>
<li><strong>Quantum Lab</strong>: Quantum Key Distribution (QKD), NEC protocol</li>
</ul>

<p><strong>Resources</strong>:</p>
<ul>
<li>Course materials: cryptography.pdf, Hardware-Security.pdf, ebios.pdf</li>
<li>Tools: mbedTLS, pycryptodome, OpenSSL</li>
<li>Reports: Lab1 Report (SQL injection, XSS)</li>
</ul>

<h3 class="section-title">Environment and context</h3>

<p>During this module, I worked on both the theoretical and practical aspects of IoT security. The relevance of securing IoT devices in today's interconnected world is obvious: every connected object represents a potential attack surface. The hands-on labs allowed me to apply the concepts learned in lectures to realistic scenarios, moving from cryptographic theory to the concrete exploitation of vulnerabilities.</p>

<h3 class="section-title">My role</h3>

<p>In this course, I was responsible for:</p>
<ul>
<li>Understanding and implementing various security protocols and cryptographic techniques</li>
<li>Implementing security measures for IoT devices</li>
<li>Conducting experiments to identify and mitigate security vulnerabilities</li>
<li>Analyzing and preventing Man-in-the-Middle (MITM) attacks on IoT communication protocols</li>
<li>Completing CTF challenges to test my cryptanalysis skills</li>
<li>Working with Quantum Key Distribution (QKD) to explore post-quantum security</li>
</ul>

<hr>

<h2>PART C: TECHNICAL ASPECTS</h2>

<p>This section explores in detail the technical aspects of connected object security, covering cryptography, security protocols, hardware security, IoT threats, and the lab work carried out.</p>

<hr>

<h3 class="section-title">1. Symmetric cryptography</h3>

<p>Symmetric cryptography uses the same key for both encryption and decryption. It is fast and efficient for encrypting large volumes of data, but requires a secure channel for key distribution.</p>

<h4>1.1 AES (Advanced Encryption Standard)</h4>

<p>AES has been the worldwide symmetric encryption standard since 2001. It encrypts data in 128-bit blocks with keys of 128, 192, or 256 bits.</p>

<p>The AES algorithm consists of multiple processing rounds, each involving four main operations:</p>

<ol>
<li><strong>AddRoundKey</strong>: each byte of the state is combined with a block of the round subkey via bitwise XOR. This step is crucial as it introduces the key into the encryption process.</li>
<li><strong>SubBytes</strong>: a non-linear substitution step where each byte of the state is replaced by another via an S-box (substitution box). The S-box is designed to resist linear and differential cryptanalysis.</li>
<li><strong>ShiftRows</strong>: the rows of the state are cyclically shifted to the left. The shift depends on the row index. This step ensures diffusion of the plaintext.</li>
<li><strong>MixColumns</strong>: a mixing operation operating on the state columns, combining the four bytes of each column. This step provides additional diffusion.</li>
</ol>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/aes.png" style="width: 90%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure: AES algorithm steps - SubBytes, ShiftRows, MixColumns, AddRoundKey
</p>
<br>

<p><strong>Number of rounds based on key size</strong>:</p>

<table>
<tr><th>Key size</th><th>Number of rounds</th><th>Typical applications</th></tr>
<tr><td>128 bits</td><td>10 rounds</td><td>General use, Wi-Fi (WPA2)</td></tr>
<tr><td>192 bits</td><td>12 rounds</td><td>Sensitive data</td></tr>
<tr><td>256 bits</td><td>14 rounds</td><td>Classified data, military</td></tr>
</table>

<p>In our <a href="./innovative-project.html#3-security-features">Innovative Project (What a Leak)</a>, we implemented the AES algorithm with additional concepts: initialization vector (IV), padding, and PKCS#7.</p>

<h4>1.2 DES (Data Encryption Standard)</h4>

<p>DES, the predecessor of AES, uses 64-bit blocks and a 56-bit key. Although obsolete today due to its small key size (vulnerable to brute force), it remains important for understanding the evolution of symmetric cryptography. Triple-DES (3DES) applies DES three times with different keys to strengthen security.</p>

<h4>1.3 Block cipher modes</h4>

<p>Cipher modes define how successive blocks are processed:</p>

<table>
<tr><th>Mode</th><th>Description</th><th>Advantages</th><th>Disadvantages</th></tr>
<tr><td><strong>ECB</strong> (Electronic Codebook)</td><td>Each block encrypted independently</td><td>Simple, parallelizable</td><td>Visible patterns, insecure</td></tr>
<tr><td><strong>CBC</strong> (Cipher Block Chaining)</td><td>Each block XORed with previous ciphertext block</td><td>Masks patterns</td><td>Sequential, error propagation</td></tr>
<tr><td><strong>CTR</strong> (Counter)</td><td>Counter encryption, XOR with text</td><td>Parallelizable, no padding</td><td>Counter must never repeat</td></tr>
<tr><td><strong>GCM</strong> (Galois/Counter Mode)</td><td>CTR + built-in authentication</td><td>Authenticated encryption</td><td>More complex</td></tr>
</table>

<h4>1.4 Caesar cipher</h4>

<p>We also studied the Caesar cipher, a simple encryption technique where each letter of the plaintext is shifted by a fixed number of positions in the alphabet. Although it is not secure by modern standards, it helped understand the basics of substitution encryption and decryption.</p>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/cypher.png" style="width: 40%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure: Caesar cipher principle - alphabetical shift
</p>
<br>

<hr>

<h3 class="section-title">2. Asymmetric cryptography</h3>

<p>Asymmetric cryptography uses a key pair (public and private) for encryption and decryption. It enhances security at the cost of reduced performance compared to symmetric encryption.</p>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/asymetric.png" style="width: 70%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure: Asymmetric cryptography principle - public key / private key
</p>
<br>

<h4>2.1 RSA (Rivest-Shamir-Adleman)</h4>

<p>RSA is the most widely used asymmetric algorithm. Its security relies on the difficulty of factoring large prime numbers.</p>

<p><strong>Principle</strong>:</p>
<ol>
<li>Generate two large prime numbers p and q</li>
<li>Compute n = p * q (modulus)</li>
<li>Compute phi(n) = (p-1)(q-1)</li>
<li>Choose the public exponent e (typically 65537)</li>
<li>Compute the private exponent d = e^(-1) mod phi(n)</li>
</ol>

<p><strong>Encryption</strong>: C = M^e mod n<br>
<strong>Decryption</strong>: M = C^d mod n</p>

<p>In the lab, we implemented RSA in the <code>2/source.py</code> file: the script generates two large prime numbers, computes their product (n), and uses the public exponent (e) to encrypt a message. The private exponent (d) decrypts the ciphertext.</p>

<p><strong>Cube root attack</strong>: We also explored an attack on RSA when the public exponent (e) is small (e = 3). If the ciphertext (c) is small enough, the plaintext can be recovered by computing the integer cube root of c. This attack was implemented in <code>2/attack.py</code>.</p>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/flag4.png" style="width: 30%;"/>
    <img src="/img/BE_Secu/flag1.png" style="width: 50%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure: CTF - Flag obtained after cube root attack on RSA
</p>
<br>

<h4>2.2 ECC (Elliptic Curve Cryptography)</h4>

<p>Elliptic curve cryptography provides a security level equivalent to RSA with much shorter keys. A 256-bit ECC key is equivalent to a 3072-bit RSA key. ECC is particularly well-suited for connected objects due to its low memory footprint and fast computation.</p>

<p><strong>Advantages for IoT</strong>:</p>
<ul>
<li>Shorter keys: less storage and bandwidth</li>
<li>Faster computations: less energy consumption</li>
<li>Equivalent security: cryptographic robustness maintained</li>
</ul>

<h4>2.3 Diffie-Hellman</h4>

<p>The Diffie-Hellman key exchange allows two parties to establish a shared secret over an insecure channel, without direct key transmission. This protocol is the foundation of many security protocols (TLS, IPsec, SSH).</p>

<p><strong>Principle</strong>:</p>
<ol>
<li>Alice and Bob agree on a prime number p and a generator g</li>
<li>Alice chooses a secret a, computes A = g^a mod p, and sends A</li>
<li>Bob chooses a secret b, computes B = g^b mod p, and sends B</li>
<li>Alice computes the shared key: K = B^a mod p</li>
<li>Bob computes the same key: K = A^b mod p</li>
</ol>

<p>Security relies on the difficulty of the discrete logarithm problem.</p>

<hr>

<h3 class="section-title">3. Hash functions</h3>

<p>Hash functions take an input of arbitrary size and produce a fixed-size digest. They are used for data integrity verification, password storage, and digital signatures.</p>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/hash.png" style="width: 60%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure: Hash function principle - fixed-size digest
</p>
<br>

<p><strong>Essential properties</strong>:</p>
<ul>
<li><strong>Pre-image resistance</strong>: impossible to recover the input from the hash</li>
<li><strong>Collision resistance</strong>: impossible to find two different inputs producing the same hash</li>
<li><strong>Avalanche effect</strong>: a minimal change in input drastically changes the output</li>
</ul>

<h4>3.1 SHA-256</h4>

<p>SHA-256 (Secure Hash Algorithm) produces a 256-bit (32-byte) digest. It is the recommended hashing algorithm for most modern applications, including digital certificates and blockchain.</p>

<h4>3.2 MD5</h4>

<p>MD5 produces a 128-bit digest. Although historically widespread, it has been considered compromised since the discovery of collisions in 2004. It is still used for quick file integrity verification (checksums) but should no longer be used for security applications.</p>

<p>In our cryptographic lab, MD5 was used to generate a 128-bit AES key from a randomly selected keyword. This illustrated key derivation from passwords.</p>

<h4>3.3 Lightweight hash functions for IoT</h4>

<p>We studied lightweight hash functions specified in the ISO/IEC 29192-5:2016 standard, designed for resource-constrained devices:</p>

<ul>
<li><strong>PHOTON</strong>: lightweight hash function with permutation sizes of 100, 144, 196, 256 and 288 bits, producing hashes of 80, 128, 160, 224 and 256 bits respectively.</li>
<li><strong>SPONGENT</strong>: lightweight hash function with permutation sizes of 88, 136, 176, 240 and 272 bits, producing hashes of 88, 128, 160, 224 and 256 bits respectively.</li>
<li><strong>Lesamnta-LW</strong>: lightweight hash function with a permutation size of 384 bits, producing a 256-bit hash.</li>
</ul>

<hr>

<h3 class="section-title">4. Digital certificates and PKI</h3>

<h4>4.1 Public Key Infrastructure (PKI)</h4>

<p>PKI is a set of roles, policies, and procedures needed to create, manage, distribute, use, store, and revoke digital certificates. It relies on a chain of trust:</p>

<ul>
<li><strong>Certificate Authority (CA)</strong>: issues and signs certificates</li>
<li><strong>Registration Authority (RA)</strong>: verifies the identity of applicants</li>
<li><strong>X.509 Certificate</strong>: contains the public key, the owner's identity, the CA signature, and the validity period</li>
</ul>

<h4>4.2 Common Name and verification</h4>

<p>In the context of certificate verification, the Common Name (CN) is an essential attribute. It is part of the Subject field of the certificate and typically represents the domain name or the identity of the certificate holder. During the verification process, the CN is compared to the expected hostname or identity to ensure the certificate is valid for the intended recipient.</p>

<p>For example, if a certificate is issued for <code>www.alice.com</code>, the CN must match <code>www.alice.com</code>. In case of a mismatch, the verification process will fail, signaling a potential security issue. This verification helps prevent Man-in-the-Middle attacks by ensuring that the certificate presented by a server matches the expected identity.</p>

<hr>

<h3 class="section-title">5. TLS/SSL protocols</h3>

<h4>5.1 TLS (Transport Layer Security)</h4>

<p>TLS is the most widely deployed security protocol for securing Internet communications. It ensures confidentiality, integrity, and authentication of exchanges.</p>

<p><strong>TLS handshake process</strong>:</p>
<ol>
<li><strong>ClientHello</strong>: the client sends supported cipher suites</li>
<li><strong>ServerHello</strong>: the server selects a suite and sends its certificate</li>
<li><strong>Key exchange</strong>: Diffie-Hellman or RSA to establish a shared secret</li>
<li><strong>Key derivation</strong>: generation of session keys from the secret</li>
<li><strong>Encrypted communication</strong>: exchanges protected by symmetric encryption (AES-GCM)</li>
</ol>

<h4>5.2 TLS migration in the lab</h4>

<p>During Lab 3, we worked on TLS migration using the mbedTLS library. The objective was to secure communications between Alice and Bob by implementing a full TLS handshake, including certificate exchange, chain of trust verification, and message encryption.</p>

<hr>

<h3 class="section-title">6. Hardware security</h3>

<p>Hardware security addresses the physical vulnerabilities of electronic systems. Even a mathematically secure algorithm can be compromised through attacks on its physical implementation.</p>

<h4>6.1 Side-Channel Attacks</h4>

<p>Side-channel attacks exploit physical information leaks during the execution of cryptographic algorithms:</p>

<table>
<tr><th>Attack type</th><th>Exploited channel</th><th>Technique</th></tr>
<tr><td><strong>Timing Attack</strong></td><td>Execution time</td><td>Measuring temporal variations</td></tr>
<tr><td><strong>Power Analysis (SPA/DPA/CPA)</strong></td><td>Power consumption</td><td>Correlation between data and consumption</td></tr>
<tr><td><strong>EM Analysis</strong></td><td>Electromagnetic emissions</td><td>Capturing EM radiations</td></tr>
<tr><td><strong>Cache Attack</strong></td><td>CPU cache behavior</td><td>Flush+Reload, Prime+Probe</td></tr>
</table>

<p><strong>Example with AES</strong>: The AES substitution tables (S-box) are stored in memory. Access to these tables depends on the key and the message. If part of the table is in cache (fast access) and another part is not (slow access), one can infer which part was accessed and progressively recover the key.</p>

<h4>6.2 Fault Injection</h4>

<p>Fault injection deliberately causes errors during execution to obtain information or bypass protections:</p>
<ul>
<li><strong>Clock glitching</strong>: clock pulses causing skipped instructions</li>
<li><strong>Voltage glitching</strong>: supply voltage variation causing computation errors</li>
<li><strong>Laser</strong>: focused laser beam modifying bits in memory</li>
</ul>

<h4>6.3 Secure Elements</h4>

<p>Secure elements are hardware components dedicated to protecting sensitive data:</p>
<ul>
<li><strong>TPM (Trusted Platform Module)</strong>: secure chip for key storage and attestation</li>
<li><strong>Secure Enclave</strong>: isolated execution environment (ARM TrustZone, Intel SGX)</li>
<li><strong>HSM (Hardware Security Module)</strong>: high-security hardware module for key management</li>
</ul>

<p>These elements are essential in IoT to protect cryptographic keys, device identities, and ensure secure boot.</p>

<hr>

<h3 class="section-title">7. IoT-specific threats - OWASP IoT Top 10</h3>

<p>OWASP (Open Web Application Security Project) identifies the top 10 vulnerabilities of connected objects:</p>

<table>
<tr><th>Rank</th><th>Vulnerability</th><th>Description</th></tr>
<tr><td>1</td><td>Weak passwords</td><td>Default credentials, unchanged</td></tr>
<tr><td>2</td><td>Insecure network services</td><td>Open ports, unnecessary exposed services</td></tr>
<tr><td>3</td><td>Insecure ecosystem interfaces</td><td>Vulnerable APIs, cloud, web interfaces</td></tr>
<tr><td>4</td><td>Lack of update mechanism</td><td>No secure firmware OTA</td></tr>
<tr><td>5</td><td>Insecure or outdated components</td><td>Vulnerable libraries</td></tr>
<tr><td>6</td><td>Insufficient privacy protection</td><td>Excessive data collection</td></tr>
<tr><td>7</td><td>Insecure data transfer and storage</td><td>Data in cleartext</td></tr>
<tr><td>8</td><td>Lack of device management</td><td>Insufficient inventory, monitoring</td></tr>
<tr><td>9</td><td>Insecure default settings</td><td>Dangerous factory configurations</td></tr>
<tr><td>10</td><td>Lack of physical hardening</td><td>Unprotected physical access</td></tr>
</table>

<hr>

<h3 class="section-title">8. EBIOS risk analysis methodology</h3>

<p>EBIOS (Expression des Besoins et Identification des Objectifs de Securite / Expression of Needs and Identification of Security Objectives) is the French reference method for information security risk analysis, developed by ANSSI.</p>

<p><strong>The 5 EBIOS Risk Manager workshops</strong>:</p>
<ol>
<li><strong>Scoping and security baseline</strong>: identify missions, business values, and perimeter</li>
<li><strong>Risk sources</strong>: identify threat sources and their targeted objectives</li>
<li><strong>Strategic scenarios</strong>: develop high-level attack paths</li>
<li><strong>Operational scenarios</strong>: detail technical modes of operation</li>
<li><strong>Risk treatment</strong>: define security measures and action plan</li>
</ol>

<p>This methodology is particularly relevant for IoT systems where attack surfaces are multiple (network, physical, cloud, firmware).</p>

<hr>

<h3 class="section-title">9. Confidentiality, integrity, and authenticity</h3>

<p>The three fundamental pillars of information security (CIA triad):</p>

<ul>
<li><strong>Confidentiality</strong>: ensuring that information is accessible only to authorized persons. Provided by encryption (AES, RSA, TLS).</li>
<li><strong>Integrity</strong>: ensuring that information is accurate and has not been altered. Provided by hash functions (SHA-256) and MACs (Message Authentication Code).</li>
<li><strong>Authenticity</strong>: verifying the identity of the parties involved in the communication. Provided by digital signatures and certificates (PKI).</li>
</ul>

<hr>

<h3 class="section-title">10. Lab sessions - Security labs</h3>

<h4>10.1 SQL Injection (Lab 1)</h4>

<p>I studied SQL injection attacks and how they can be used to extract information from a database. For example, by entering <code>admin' OR 1=1 OR '1'='1</code> in the authentication field and an arbitrary password such as <code>vhjvg</code>, an attacker can bypass the authentication mechanism. The SQL query always evaluates to true, allowing unauthorized access to sensitive data. Understanding this vulnerability helped me implement prevention measures in IoT systems.</p>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/SQL_injection.png" style="width: 60%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure: SQL injection attack demonstration - authentication bypass
</p>
<br>

<p><strong>Prevention measures</strong>:</p>
<ul>
<li>Using parameterized queries (prepared statements)</li>
<li>Validating and sanitizing user input</li>
<li>Principle of least privilege for database accounts</li>
<li>Using an ORM (Object-Relational Mapping)</li>
</ul>

<h4>10.2 Cross-Site Scripting - XSS (Lab 1)</h4>

<p>We explored XSS attacks, which involve injecting malicious scripts into web pages viewed by other users. This can lead to data theft, session hijacking, and other malicious activities.</p>

<p>For example, we executed JavaScript code in the username field by entering <code>&lt;script&gt;alert('Hello');&lt;/script&gt;</code> or <code>&lt;script&gt;document.write("&lt;img src='xxxx'/&gt;");&lt;/script&gt;</code>. This demonstrated how an attacker could inject scripts to manipulate the web page or steal information. The repercussions of such attacks can be severe: unauthorized access to user data and malware propagation.</p>

<h4>10.3 Man-in-the-Middle Attack - MITM (Lab 3)</h4>

<p>I studied Man-in-the-Middle attacks, where an attacker intercepts and potentially alters communication between two parties without their knowledge. This type of attack can lead to data breaches and unauthorized access to sensitive information.</p>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/Man_Middle.png" style="width: 60%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure: Man-in-the-Middle attack diagram - communication interception
</p>
<br>

<p>In the attacker file, we implemented a simple MITM attack using the mbedTLS library. The attacker intercepts and modifies messages between Alice and Bob. The attacker reads Bob's message, alters it, then sends the modified message to Alice. This demonstrates how an attacker can manipulate communication between two parties, highlighting the importance of securing communications.</p>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/lab3_terminal.png" style="width: 100%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure: Lab3 Terminal - Message interception and modification by the attacker
</p>
<br>

<p>During Lab 3, we worked on a scenario where Alice sends a certificate to Bob. Bob receives the certificate and verifies it. Simultaneously, a hacker intercepts and prints the key. Bob then sends a message to Alice, but the hacker intercepts the message, alters it, and sends the modified message to Alice.</p>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/lab3_terminal2.png" style="width: 100%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure: Lab3 - Certificate and key interception scenario
</p>
<br>

<p>Fix:</p>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/lab3_terminal3.png" style="width: 100%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure: Lab3 - Fix and Common Name verification
</p>
<br>

<h4>10.4 TLS Migration (Lab 3)</h4>

<p>The TLS migration consisted of securing communications by implementing the full TLS protocol with mbedTLS. The objective was to transition from cleartext communication to encrypted and authenticated communication, integrating:</p>
<ul>
<li>X.509 certificate exchange</li>
<li>Chain of trust verification</li>
<li>Message encryption with AES-GCM</li>
<li>Protection against replay attacks</li>
</ul>

<h4>10.5 Cryptographic CTF challenges (Lab 4)</h4>

<h5>AES Encryption - CTF</h5>

<p>In the <code>1/source.py</code> file, we implemented AES encryption and decryption using the pycryptodome library:</p>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/flag3.png" style="width: 30%;"/>
    <img src="/img/BE_Secu/flag1.png" style="width: 50%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure: CTF - Flags obtained after AES decryption via dictionary brute force
</p>
<br>

<p>The challenge process:</p>
<ol>
<li><strong>Keyword selection</strong>: the script reads a word list from a <code>words</code> file and randomly selects one</li>
<li><strong>Key generation</strong>: the selected keyword is hashed with MD5 to generate a 128-bit AES key</li>
<li><strong>Flag encryption</strong>: the predefined flag is padded to a multiple of the AES block size (16 bytes) and encrypted in ECB mode</li>
<li><strong>Flag decryption</strong>: the encrypted flag is decrypted with the same key to validate the process</li>
</ol>

<h5>RSA Encryption - CTF</h5>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/flag4.png" style="width: 30%;"/>
    <img src="/img/BE_Secu/flag2.png" style="width: 50%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure: CTF - Flag obtained after exploiting the RSA vulnerability
</p>
<br>

<hr>

<h3 class="section-title">11. Quantum Lab</h3>

<h4>11.1 NEC Protocol</h4>

<p>We established communication between two boards using the NEC protocol, commonly used in remote controls. The transmitter encodes messages in NEC format and sends them via infrared pulses. The receiver decodes these signals to recover the original message.</p>

<p><strong>Example</strong>:</p>
<ul>
<li><strong>Transmitter</strong>: encodes "A" in NEC format and sends it</li>
<li><strong>Receiver</strong>: decodes the infrared signal to recover "A"</li>
</ul>

<p>This exercise demonstrated the importance of timing precision and reliability in infrared communication.</p>

<p><strong>Signal data for "A"</strong>:</p>
<ul>
<li><strong>NEC format</strong>: the NEC protocol uses a 32-bit frame. For the character "A", the signal data is encoded as follows:
    <ul>
    <li><strong>Address</strong>: 0x8D</li>
    <li><strong>Inverse address</strong>: 0x72</li>
    <li><strong>Command</strong>: 0x45 (ASCII code for "A")</li>
    <li><strong>Inverse command</strong>: 0x4E</li>
    </ul>
</li>
</ul>

<p>The complete 32-bit frame for "A" is: <code>0x8D72454E</code>.</p>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/nec.png" style="width: 90%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure: NEC Protocol - Infrared frame structure
</p>
<br>

<h4>11.2 Quantum Key Distribution (QKD)</h4>

<p>After performing the classical test on <code>/dev/tty1CM0</code>, we proceeded to the quantum test on <code>/dev/ttyACM1</code>. We first performed a calibration by setting the angle to 0, the scan resolution to 1, the offset to 0, and the polarization to 0. We then converted the brightness signal to voltage by sweeping and measuring the intensity after the linear polarizer during a full 360-degree rotation. Following calibration, we ran a Python script to automate the key distribution and generate a 32 kbit key.</p>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/cute.png" style="width: 25%;"/>
    <img src="/img/BE_Secu/hdva.png" style="width: 40%;"/>
    <img src="/img/BE_Secu/key.png" style="width: 40%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure: Quantum key distribution - Experimental setup and key generation
</p>
<br>

<p>Additionally, we introduced a prism into the setup, allowing the light signals from Bob, Alice, and Eve to pass through it. This was done to facilitate key sharing with another user. The prism helped split the light signals, ensuring that the key distribution could be securely shared with the new user without compromising the integrity of the original communication.</p>

<div style="text-align: center; display: flex; justify-content: center;">
    <img src="/img/BE_Secu/prisme.png" style="width: 90%;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666;">
    Figure: Prism setup - Multi-user quantum key sharing
</p>
<br>

<hr>

<h2>PART D: ANALYSIS AND REFLECTION</h2>

<h3 class="section-title">Skills acquired</h3>

<p><strong>Cryptography mastery</strong>:<br>
Ability to understand, implement, and evaluate cryptographic algorithms (AES, RSA, ECC, hash functions) and to choose solutions adapted to IoT constraints.</p>

<p><strong>Communication security</strong>:<br>
Ability to implement TLS/SSL protocols, manage digital certificates via PKI, and secure exchanges between IoT devices.</p>

<p><strong>Vulnerability analysis</strong>:<br>
Competency in identifying and exploiting security flaws (SQL injection, XSS, MITM) to better design countermeasures.</p>

<p><strong>Hardware security</strong>:<br>
Understanding of side-channel attacks, fault injection, and secure elements for physical device protection.</p>

<p><strong>Risk analysis</strong>:<br>
Ability to conduct a methodical risk analysis (EBIOS) adapted to IoT systems.</p>

<p><strong>Global vision</strong>:<br>
Integration of security throughout the entire lifecycle of an IoT system, from design to deployment.</p>

<h3 class="section-title">Key takeaways</h3>

<p><strong>1. Security is multi-layered</strong>:<br>
Protecting an IoT system requires measures at all levels: physical, network, application, and organizational. A defense-in-depth approach is essential.</p>

<p><strong>2. Cryptography is necessary but not sufficient</strong>:<br>
A mathematically secure algorithm can be vulnerable if its implementation leaks information (side channels). Security depends on the quality of the implementation as much as on the algorithm.</p>

<p><strong>3. IoT amplifies risks</strong>:<br>
The massive number of devices, resource constraints, and difficult updates make IoT security particularly complex.</p>

<p><strong>4. Practice is essential</strong>:<br>
CTF labs, MITM attacks, and SQL injections allowed me to move from theory to practice, strengthening my operational understanding.</p>

<p><strong>5. Quantum is the future</strong>:<br>
The QKD experimentation opened a fascinating perspective on post-quantum cryptography and secure key distribution.</p>

<h3 class="section-title">Feedback</h3>

<p>I already had a preliminary overview of most of these concepts, but this course provided a more advanced and technical perspective. We deepened our C coding with mbedTLS and tested SQL injection attacks. The latter was a bit challenging for me since I had never used SQL before, and I had to learn quickly to be effective.</p>

<p>Furthermore, many concepts explained in lectures were not practiced. I feel that I am not fully up to date on everything because some topics remained purely theoretical. The professor's explanations during lectures were a plus for me as they were clear, and I wanted to be operational on these concepts.</p>

<p>Additionally, working alone during the lab sessions pushed me to work more intensely to understand all the concepts in depth.</p>

<h3 class="section-title">My opinion</h3>

<p>This course was very interesting and stimulating. I learned a lot about security vulnerabilities and how to prevent them. In my future career, I am interested in the field of security, which means I need to stay informed about the latest threats. I really appreciated the lab work that allowed me to apply the concepts learned in class, and I am a bit disappointed that we did not have more time to explore other security concepts.</p>

<p>At the end of the semester, we had a quantum lab that was truly exciting. Unfortunately, we were the "test class" since nobody had done it before. Even though we encountered some issues finalizing it, working in partnership with the instructors was an excellent experience. I hope to discover more about quantum computing in the future as it is a fascinating field.</p>

<h3 class="section-title">Professional perspectives</h3>

<p><strong>For IoT security engineer</strong>:</p>
<ul>
<li>Security auditing of connected systems</li>
<li>Design of secure IoT products (secure by design)</li>
<li>Penetration testing and red teaming on embedded systems</li>
</ul>

<p><strong>For embedded developer</strong>:</p>
<ul>
<li>Correct implementation of cryptographic algorithms</li>
<li>Integration of TLS/SSL in IoT communications</li>
<li>Use of secure elements (TPM, Secure Enclave)</li>
</ul>

<p><strong>Link with the Innovative Project</strong>:<br>
The skills acquired in this course were directly applied in our <a href="./innovative-project.html#3-security-features">Innovative Project (What a Leak)</a>, where we implemented AES encryption with initialization vector and PKCS#7 padding to secure the communications of our IoT water leak detection system.</p>

<hr>

<h2>Reports and Projects</h2>

<div style="text-align: center;">
    <h3>Laboratory Report - Lab 1 (SQL Injection, XSS)</h3>
</div>

<div style="display: flex; justify-content: center;">
    <iframe src="/file/reports/S9/Rapport_Lab1.pdf" width="100%" height="800px" style="overflow: auto;" frameborder="0"></iframe>
</div>

<p style="text-align: center;">
    <a href="/file/reports/S9/Rapport_Lab1.pdf" target="_blank">
        Open the full report - Lab 1
    </a>
</p>

<hr>

<p><em>Course taken in 2024-2025 at INSA Toulouse, Department of Electrical and Computer Engineering, Semester 9.</em></p>

</div>

<div class="back-nav">
    <a href="./my-courses-2024-2025.html" data-i18n-html="back-courses-2024-2025">&larr; Retour aux Cours 2024-2025</a>
</div>

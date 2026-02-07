---
layout: default
title:  "5G Technologies"
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

p {
    text-align: justify;
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
</style>

<div class="back-nav">
    <a href="./my-courses-2024-2025.html">&larr; Retour aux Cours 2024-2025</a>
</div>

# Technologies 5G / De la 3G a la 6G - Semestre 9

**Annee academique** : 2024-2025
**Semestre** : S9
**Enseignant** : Etienne Sicard
**Categorie** : Telecommunications et Reseaux Mobiles

---

## PART A - Presentation Generale

<h3 class="section-title">Objectifs du module</h3>

Le cours "5G Technologies / From 3G to 6G", dispense par Etienne Sicard a l'INSA Toulouse, avait pour objectif principal d'explorer l'ensemble des technologies liees aux reseaux cellulaires, depuis la 3G jusqu'aux perspectives de la 6G, avec un accent particulier sur la 5G et ses technologies emergentes.

**Objectifs pedagogiques** :
- Comprendre l'evolution des reseaux cellulaires de la 3G a la 6G
- Maitriser les principes fondamentaux des technologies 5G (OFDM, MIMO, beamforming)
- Analyser les bandes de frequences et l'architecture reseau de la 5G NR
- Explorer les technologies emergentes pour la 6G (THz, IA, communication quantique)
- Evaluer l'impact societal et environnemental des nouvelles generations de reseaux
- Developper des competences en recherche, synthese et presentation technique

<h3 class="section-title">Competences visees</h3>

- Maitrise des concepts de modulation avancee (OFDM, OFDMA, QAM)
- Comprehension des architectures MIMO et massive MIMO
- Connaissance des bandes de frequences sub-6 GHz et mmWave
- Analyse du network slicing et de la virtualisation reseau
- Vision prospective sur les technologies 6G
- Capacite a synthetiser et presenter des sujets techniques complexes

<h3 class="section-title">Organisation du cours</h3>

Le cours employait une pedagogie inversee (reverse pedagogy) : les etudiants etaient responsables de la preparation et de la presentation de sujets specifiques. Cette approche permettait une immersion profonde dans chaque sujet grace a la recherche personnelle approfondie.

**Format** :
- Presentations par groupes d'etudiants sur des sujets varies
- Discussions et debats apres chaque presentation
- Partage de connaissances et apprentissage collaboratif

---

## PART B - Experience et Contexte

<h3 class="section-title">Environnement et contexte</h3>

Au cours de ce module, nous avons aborde un large eventail de sujets lies aux telecommunications modernes. J'ai eu l'opportunite de collaborer avec Samia Boukouiss sur une presentation dediee aux technologies pour la 6G. Notre travail a couvert de nombreux aspects :

- Les applications et opportunites de la 6G
- Les technologies cles de la 6G (THz, IA, communication quantique, VLC, ultra-massive MIMO)
- Les defis dans le developpement de la 6G
- Le calendrier de developpement et les efforts mondiaux
- L'impact de la 6G sur la societe

<h3 class="section-title">Presentations des collegues</h3>

J'ai egalement participe activement aux presentations de mes camarades, couvrant des sujets tres varies :

| Sujet | Domaine |
|-------|---------|
| Starlink, Kuiper | Constellations de satellites |
| LTE-M pour l'IoT | Reseaux cellulaires pour objets connectes |
| Samsung et la 6G | Vision industrielle de la 6G |
| Drone-trains | Transport et telecommunications |
| Orange et la 6G | Strategie operateur pour la 6G |
| Impacts environnementaux | Ecologie et telecommunications |
| 5G : Vehicle to Everything (V2X) | Communications vehiculaires |
| Cancer et ondes EM | Sante et ondes electromagnetiques |

Ces presentations m'ont permis d'acquerir une vision large et transversale des enjeux des telecommunications modernes.

<h3 class="section-title">Ma fonction</h3>

Dans le cadre de ce cours, j'etais responsable de :
- Rechercher et presenter les technologies pour la 6G en binome
- Collaborer avec mes pairs pour explorer les implications de la 5G et des futures technologies 6G
- Participer aux discussions et echanges apres chaque presentation
- Prendre des notes et synthetiser les connaissances partagees par les autres groupes

<h3 class="section-title">Outils et ressources utilises</h3>

- **Recherche documentaire** : articles scientifiques IEEE, 3GPP, publications industrielles
- **Outils de presentation** : PowerPoint, documents de synthese
- **Sources de reference** : specifications 3GPP, livres blancs des operateurs et equipementiers (Ericsson, Nokia, Samsung, Huawei)
- **Cours de reference** : support de cours "3G6G-2024" du Pr. Sicard

---

## PART C - Aspects Techniques Detailles

<h3 class="section-title">1. Evolution des reseaux cellulaires : de la 3G a la 5G</h3>

**Chronologie des generations** :

| Generation | Periode | Debit max | Technologie cle | Usage principal |
|------------|---------|-----------|-----------------|-----------------|
| 3G (UMTS) | 2001+ | 2 Mbps | WCDMA, HSPA | Internet mobile, video |
| 4G (LTE) | 2010+ | 100 Mbps - 1 Gbps | OFDMA, MIMO | Streaming HD, apps |
| 5G (NR) | 2020+ | 10-20 Gbps | mmWave, massive MIMO | IoT massif, URLLC |
| 6G (vision) | 2030+ | 1 Tbps | THz, IA, quantique | Holographie, jumeaux numeriques |

**De la 3G a la 4G** :
La transition de la 3G (UMTS/WCDMA) vers la 4G (LTE) a marque un tournant majeur avec l'adoption de l'OFDMA (Orthogonal Frequency-Division Multiple Access) comme technique d'acces, remplacant le CDMA. Cette evolution a permis une augmentation significative des debits et une meilleure efficacite spectrale, ouvrant la voie au streaming video et aux applications gourmandes en bande passante.

**De la 4G a la 5G** :
La 5G (New Radio - NR) represente une rupture technologique avec trois piliers fondamentaux :
- **eMBB** (enhanced Mobile Broadband) : debits tres eleves jusqu'a 20 Gbps
- **mMTC** (massive Machine-Type Communication) : connexion de millions d'objets IoT par km2
- **URLLC** (Ultra-Reliable Low-Latency Communication) : latence inferieure a 1 ms pour applications critiques (vehicules autonomes, chirurgie a distance)

<h3 class="section-title">2. Techniques de modulation : OFDM et au-dela</h3>

**OFDM (Orthogonal Frequency-Division Multiplexing)** :

L'OFDM est la technique de modulation fondamentale de la 5G NR. Son principe repose sur la division de la bande passante en de nombreuses sous-porteuses orthogonales, chacune transportant une partie des donnees.

**Avantages de l'OFDM** :
- Haute efficacite spectrale grace a l'orthogonalite des sous-porteuses
- Robustesse face au multi-trajet (fading selectif en frequence)
- Egalisation simple dans le domaine frequentiel
- Flexibilite dans l'allocation des ressources

<div style="text-align: center; display: flex; justify-content: center; gap: 10px;">
     <img src="/img/BE_6G/5G_graphe.png" style="width: 55%; border: 1px solid #ddd; padding: 5px; border-radius: 8px;"/>
     <img src="/img/BE_6G/5G_canal.png" style="width: 40%; border: 1px solid #ddd; padding: 5px; border-radius: 8px;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666; margin-top: 10px;">Figure : Representation du canal 5G et des sous-porteuses OFDM</p>

**Numerologie 5G NR** :

La 5G NR introduit le concept de numerologie flexible avec differentes espacements de sous-porteuses (Subcarrier Spacing - SCS) :

| Numerologie (mu) | SCS (kHz) | Duree symbole | Bande passante typique | Usage |
|-------------------|-----------|---------------|------------------------|-------|
| 0 | 15 | 66.7 us | Sub-6 GHz | eMBB bande basse |
| 1 | 30 | 33.3 us | Sub-6 GHz | eMBB bande moyenne |
| 2 | 60 | 16.7 us | Sub-6 GHz / mmWave | eMBB / URLLC |
| 3 | 120 | 8.33 us | mmWave | eMBB mmWave |
| 4 | 240 | 4.17 us | mmWave | Synchronisation |

**Modulations QAM** :

La 5G utilise des modulations QAM d'ordre eleve pour maximiser le debit :
- **QPSK** : 2 bits/symbole, robuste (utilise en conditions difficiles)
- **16-QAM** : 4 bits/symbole
- **64-QAM** : 6 bits/symbole
- **256-QAM** : 8 bits/symbole (conditions optimales)

<div style="text-align: center; margin: 20px 0;">
     <img src="/img/BE_6G/5G_modulation.png" style="width: 65%; border: 1px solid #ddd; padding: 10px; border-radius: 8px;"/>
</div>
<p style="text-align: center; font-style: italic; color: #666; margin-top: 10px;">Figure : Schemas de modulation utilises en 5G</p>

**Limites de l'OFDMA pour la 6G** :

Cependant, l'OFDMA presente des limitations pour supporter le nombre massif de dispositifs mobiles envisage pour la 6G. D'autres techniques de modulation sont envisagees pour les generations futures, telles que le multiplexage par moment angulaire orbital (OAM), qui exploite le domaine spatial pour transmettre simultanement plusieurs flux de donnees.

<h3 class="section-title">3. MIMO et Massive MIMO</h3>

**Principe du MIMO** :

Le MIMO (Multiple Input Multiple Output) utilise plusieurs antennes en emission et en reception pour ameliorer les performances du lien radio :
- **Multiplexage spatial** : transmission de flux de donnees independants sur des chemins spatiaux differents, augmentant le debit
- **Diversite spatiale** : envoi du meme signal sur plusieurs chemins pour ameliorer la fiabilite
- **Beamforming** : focalisation de l'energie radio dans une direction specifique

**Massive MIMO en 5G** :

La 5G deploie le massive MIMO avec des antennes comportant 64, 128, voire 256 elements :
- Gain de beamforming significatif (concentration de l'energie vers l'utilisateur)
- Augmentation de la capacite du reseau par multiplexage spatial multi-utilisateur (MU-MIMO)
- Reduction des interferences inter-cellulaires
- Amelioration de l'efficacite energetique (energie dirigee au lieu d'etre rayonnee dans toutes les directions)

**Beamforming** :

Le beamforming est une technique essentielle en 5G, particulierement pour les bandes mmWave :
- **Beamforming analogique** : dephaseurs analogiques, un seul faisceau a la fois
- **Beamforming numerique** : traitement numerique complet, multiples faisceaux simultanement
- **Beamforming hybride** : combinaison analogique/numerique, compromis cout/performance
- **Beam management** : procedures de recherche, selection et suivi des faisceaux (beam sweeping, beam tracking)

<h3 class="section-title">4. Bandes de frequences 5G</h3>

**Spectre 5G** :

La 5G utilise un spectre beaucoup plus large que les generations precedentes, divise en deux categories principales :

**FR1 (Frequency Range 1) - Sub-6 GHz** :
- Bandes basses (< 1 GHz) : couverture etendue, penetration des batiments, IoT
- Bandes moyennes (1-6 GHz) : bon compromis couverture/debit, bande phare 3.5 GHz (bande n78)
- Largeur de bande : jusqu'a 100 MHz par porteuse

**FR2 (Frequency Range 2) - mmWave** :
- Bandes 24.25-52.6 GHz (principalement 26 GHz et 28 GHz)
- Tres haut debit (> 1 Gbps)
- Portee limitee (quelques centaines de metres)
- Fortement attenue par les obstacles, la pluie, le feuillage
- Necessite beamforming et deploiement dense de small cells
- Largeur de bande : jusqu'a 400 MHz par porteuse

**Compromis fondamental** :

| Critere | Sub-6 GHz | mmWave |
|---------|-----------|--------|
| Couverture | Large (km) | Limitee (100-300 m) |
| Debit | Moyen (1-2 Gbps) | Tres eleve (> 5 Gbps) |
| Penetration | Bonne | Tres faible |
| Densite antennes | Moderee | Elevee (small cells) |
| Latence | Bonne | Tres faible |

<h3 class="section-title">5. Architecture reseau 5G NR</h3>

**Architecture 5G** :

L'architecture 5G introduit des concepts fondamentaux de flexibilite et de virtualisation :

**5G Core (5GC)** :
- Architecture basee sur les services (SBA - Service-Based Architecture)
- Fonctions reseau virtualisees (VNF) et conteneurisees
- Separation du plan de controle et du plan utilisateur (CUPS - Control and User Plane Separation)
- Support natif du network slicing

**gNodeB (gNB)** :
- Station de base 5G NR
- Decoupe en unites : CU (Centralized Unit), DU (Distributed Unit), RU (Radio Unit)
- Interface fronthaul (eCPRI) entre DU et RU
- Support du Dual Connectivity avec LTE (EN-DC)

**Modes de deploiement** :
- **NSA (Non-Standalone)** : 5G NR avec coeur 4G LTE (deploiement initial)
- **SA (Standalone)** : 5G NR avec coeur 5G (architecture complete)

<h3 class="section-title">6. Network Slicing</h3>

Le network slicing est une innovation majeure de la 5G qui permet de creer des reseaux virtuels dedies sur une meme infrastructure physique :

- **Slice eMBB** : optimise pour le haut debit (streaming 4K/8K, realite virtuelle)
- **Slice URLLC** : optimise pour la faible latence et la haute fiabilite (vehicules autonomes, industrie 4.0)
- **Slice mMTC** : optimise pour la connexion massive d'objets IoT (capteurs, compteurs intelligents)

Chaque slice possede ses propres parametres de qualite de service (QoS), garantissant l'isolation et les performances requises par chaque type d'application.

<h3 class="section-title">7. Technologies pour la 6G</h3>

La presentation que j'ai realisee avec Samia Boukouiss portait sur les technologies cles de la 6G. Voici les principales technologies identifiees :

**Communication Terahertz (THz)** :
- Bande de frequence 0.1 - 10 THz
- Debits ultra-eleves (potentiellement > 1 Tbps)
- Portee tres limitee (quelques metres)
- Applications : realite virtuelle haute definition, holographie, communications intra-chip
- Defis : attenuation atmospherique importante, composants encore immatures

**Intelligence Artificielle et Machine Learning pour la 6G** :
- Optimisation en temps reel des performances reseau
- Gestion predictive de la congestion et des ressources
- Routage intelligent et allocation dynamique du spectre
- Auto-configuration et auto-reparation du reseau
- L'IA comme composante native de l'architecture reseau (non plus un ajout)

**Communication quantique et securite avancee** :
- Distribution de cles quantiques (QKD - Quantum Key Distribution)
- Communications resistantes aux attaques par ordinateur quantique
- Cryptographie post-quantique
- Securite intrinseque du canal de communication

**Visible Light Communication (VLC)** :
- Utilisation du spectre de lumiere visible pour transmettre des donnees
- Bande passante enorme (400-800 THz)
- Applications : communication sous-marine, navigation interieure, LiFi
- Pas d'interference avec les systemes RF existants

**Ultra-massive MIMO** :
- Tableaux d'antennes de plusieurs milliers d'elements
- Surfaces intelligentes reconfigurables (RIS - Reconfigurable Intelligent Surfaces)
- Holographic MIMO : controle continu du champ electromagnetique
- Gain de capacite exponentiel dans les zones urbaines denses

**Autres technologies envisagees** :
- **Reseaux non-terrestres (NTN)** : satellites LEO, drones, HAPS pour couverture globale
- **Jumeaux numeriques reseau** : replique virtuelle du reseau pour simulation et optimisation
- **Sensing et communication integres (ISAC)** : le reseau devient aussi un capteur (radar, localisation)
- **Computing integre** : convergence communication/calcul/stockage

<h3 class="section-title">8. Calendrier et efforts mondiaux pour la 6G</h3>

| Periode | Etape |
|---------|-------|
| 2020-2025 | Recherche exploratoire, definition des cas d'usage |
| 2025-2028 | Standardisation initiale (3GPP Release 20+) |
| 2028-2030 | Prototypes et essais terrain |
| 2030+ | Deploiement commercial initial |

**Initiatives mondiales** :
- **Europe** : projet Hexa-X (consortium EU), 6G-IA
- **Etats-Unis** : Next G Alliance (ATIS), programmes DARPA
- **Chine** : programme national 6G, prototypes THz
- **Coree du Sud** : Samsung 6G Vision, programme gouvernemental
- **Japon** : Beyond 5G Promotion Consortium
- **Finlande** : 6G Flagship (Universite d'Oulu)

<h3 class="section-title">9. Impact societal et environnemental</h3>

**Applications societales de la 5G/6G** :
- **Sante** : chirurgie a distance, telemedicine haute definition, monitoring patient en temps reel
- **Transport** : vehicules autonomes (V2X), gestion intelligente du trafic
- **Industrie** : usines intelligentes (Industrie 4.0/5.0), robots collaboratifs
- **Education** : realite virtuelle immersive, formation a distance augmentee
- **Agriculture** : agriculture de precision, drones de surveillance

**Preoccupations environnementales** :
Les presentations sur les impacts environnementaux ont mis en evidence :
- La consommation energetique croissante des reseaux mobiles
- L'empreinte carbone de la fabrication et du deploiement des infrastructures
- La necessite de concevoir des reseaux "green" et energetiquement efficaces
- L'objectif de la 6G : reduire la consommation energetique par bit transmis d'un facteur 100

---

## PART D - Analyse et Reflexion

<h3 class="section-title">Competences acquises</h3>

**Competences techniques** :
- Comprehension de l'evolution technologique des reseaux cellulaires (3G a 6G)
- Maitrise des concepts de modulation avancee (OFDM, QAM, numerologie 5G NR)
- Connaissance des architectures MIMO et massive MIMO
- Comprehension des bandes de frequences et des compromis couverture/debit
- Vision des technologies emergentes pour la 6G

**Competences transversales** :
- Recherche bibliographique sur des sujets techniques de pointe
- Synthese et vulgarisation de concepts complexes
- Presentation orale devant un auditoire technique
- Travail en equipe et collaboration

<h3 class="section-title">Auto-evaluation</h3>

Ce cours m'a permis de me concentrer sur un sujet specifique, de l'etudier en profondeur et de presenter mes conclusions. Ce processus m'a permis de developper des competences en recherche, en presentation et en discussion de sujets techniques, competences indispensables dans le monde professionnel.

La pedagogie inversee presente l'avantage de rendre chaque etudiant acteur de son apprentissage. En preparant ma presentation sur les technologies 6G, j'ai du approfondir considerablement mes connaissances sur les communications THz, l'IA pour les reseaux, et la communication quantique.

Cependant, pour les sujets presentes par mes pairs, mon apprentissage restait au niveau de l'ecoute et de la prise de notes. Bien que cela m'ait permis de rester informe sur les technologies sans devenir un expert complet sur chaque sujet, c'est parfois un peu frustrant de ne pas pouvoir approfondir davantage.

L'ajout d'aspects pratiques (simulations, travaux de laboratoire) aurait pu renforcer la comprehension des concepts techniques, bien que la nature prospective de certains sujets (6G) rende cela difficile.

| Competence | Niveau avant | Niveau apres | Progression |
|------------|-------------|-------------|-------------|
| Modulations OFDM/QAM | Notions de base | Bonne comprehension | Significative |
| MIMO / Beamforming | Faible | Bonne comprehension | Importante |
| Architecture 5G NR | Tres faible | Correcte | Importante |
| Technologies 6G | Aucune | Bonne vision d'ensemble | Tres importante |
| Network slicing | Aucune | Comprehension des principes | Importante |
| Presentation technique | Correcte | Bonne | Moderee |

<h3 class="section-title">Applications et perspectives</h3>

Ce cours m'a permis de plonger dans des technologies du quotidien que je n'avais pas envisage d'etudier auparavant, revelant leur complexite et leur fonctionnement. Il m'a egalement permis de me projeter dans l'avenir : apres avoir etudie la 6G, j'ai une idee plus claire de ce que pourrait etre la prochaine generation de reseaux.

**Applications directes** :
- Conception de systemes IoT exploitant la 5G (mMTC, URLLC)
- Developpement d'applications tirant parti du network slicing
- Integration de capteurs et objets connectes dans les reseaux 5G
- Veille technologique sur les evolutions vers la 6G

**Lien avec les autres cours du cursus** :
- **Wireless Sensor Networks** : protocoles radio et couches basses
- **Embedded IA for IoT** : IA embarquee dans les dispositifs connectes
- **Energy for Connected Objects** : contraintes energetiques des objets 5G/IoT
- **Cloud & Edge Computing** : infrastructure de calcul pour les services 5G

Les presentations constituaient un excellent moyen d'apprendre beaucoup en peu de temps. En les preparant et en y assistant, nous avons couvert de nombreux sujets en profondeur, ce qui nous a vraiment aides a mieux comprendre les technologies 5G et 6G.

---

<div style="text-align: center;">
    <h1>Presentation de projet</h1>
</div>

<div style="display: flex; justify-content: center;">
     <iframe src="/img/BE_6G/6G.pdf" width="100%" height="800px" style="overflow: auto;" frameborder="0"></iframe>
</div>

<p style="text-align: center;">
     <a href="/img/BE_6G/6G.pdf" target="_blank">Telecharger la presentation complete</a>
</p>

---

*Cours suivi en 2024-2025 a l'INSA Toulouse, Departement Genie Electrique et Informatique, Specialite ISS (Innovative Smart Systems).*

<div class="back-nav">
    <a href="./my-courses-2024-2025.html">&larr; Retour aux Cours 2024-2025</a>
</div>

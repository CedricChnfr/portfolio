---
layout: default
title:  "Energy Connected Object"
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
</style>

<div class="back-nav">
    <a href="./my-courses-2024-2025.html">&larr; Retour aux Cours 2024-2025</a>
</div>

# Energy for Connected Objects

**Cours connexes**:
- [Embedded IA for IoT - S9](./2024-10-03-embedded-ia-iot.html) - Optimisation energetique de l'IA
- [Wireless Sensors Networks - S9](./2024-10-03-wireless-sensors.html) - Efficacite energetique WSN
- [Microcontroleur & Hardware - S9](./2024-10-03-microcontroleur_hardware.html) - Consommation des microcontroleurs

**Annee academique** : 2024-2025
**Semestre** : 9 (S9)
**Categorie** : Energie et IoT
**Enseignant** : G. Loubet

---

## PART A - Presentation Generale

<h3 class="section-title">Vue d'ensemble</h3>

Le cours "Energy for Connected Objects" porte sur les differentes methodes d'alimentation des objets connectes, un enjeu central dans le domaine de l'IoT. Dispense par G. Loubet a l'INSA Toulouse dans le cadre du parcours ISS (Innovative Smart Systems), ce module couvre la recuperation d'energie (energy harvesting), le transfert d'energie sans fil (Wireless Power Transfer), la gestion energetique efficace et le dimensionnement du budget energetique des systemes IoT.

L'objectif principal est de comprendre comment concevoir des systemes IoT autonomes energetiquement, capables de fonctionner sur de longues durees sans maintenance, en exploitant les sources d'energie ambiantes disponibles dans l'environnement.

<h3 class="section-title">Objectifs pedagogiques</h3>

- Comprendre les differentes sources d'energie ambiante exploitables pour l'IoT
- Maitriser les principes de la recuperation d'energie (photovoltaique, thermique, mecanique, electromagnetique)
- Concevoir un systeme de transfert d'energie sans fil (WPT)
- Dimensionner le budget energetique complet d'un noeud IoT
- Choisir et dimensionner les composants de gestion d'energie (regulateurs, supercondensateurs, batteries)
- Selectionner et caracteriser des antennes pour la recuperation d'energie RF
- Evaluer l'efficacite d'un systeme complet de recuperation et stockage d'energie

<h3 class="section-title">Organisation du module</h3>

| Element | Details |
|---------|---------|
| Cours magistraux | Fondamentaux de l'energie pour l'IoT |
| Travaux pratiques | Experimentation WPT, mesures d'antennes, budget energetique |
| Projet | Application au projet innovant (What a Leak) |
| Evaluation | Rapport de TP et integration au projet |

---

## PART B - Experience et Contexte

<h3 class="section-title">Environnement et contexte</h3>

Ce cours s'inscrit dans un contexte ou la demande de solutions energetiquement autonomes pour les objets connectes ne cesse de croitre. Avec des milliards de capteurs deployes dans le monde pour des applications de surveillance environnementale, de maintenance predictive ou de villes intelligentes, la question de l'alimentation energetique devient critique. Remplacer des batteries sur des milliers de noeuds capteurs est economiquement et logistiquement intenable.

Le cours m'a permis d'explorer aussi bien les aspects theoriques (physique de la recuperation d'energie, equations de propagation, rendements thermodynamiques) que les aspects pratiques (mesures en laboratoire, tests d'antennes, calculs de bilan de liaison).

Les travaux pratiques se sont deroules en salle de TP avec du materiel de mesure RF (generateurs de signaux, analyseurs de spectre, antennes diverses) et des composants de gestion d'energie (rectifiers, regulateurs, supercondensateurs).

<h3 class="section-title">Mon role</h3>

Dans ce cours, j'ai ete responsable de :
- Etudier et comparer les differentes techniques de recuperation d'energie
- Realiser des mesures de transfert d'energie sans fil a differentes frequences
- Selectionner et caracteriser des antennes (patch vs whip) pour la recuperation d'energie RF
- Calculer le budget energetique d'un noeud IoT dans le cadre du projet innovant
- Evaluer la faisabilite de l'alimentation autonome pour notre projet "What a Leak"
- Rediger un rapport technique detaillant les resultats experimentaux

---

## PART C - Aspects Techniques

<h3 class="section-title">1. Sources d'energie ambiante pour l'IoT</h3>

L'une des premieres notions etudiees concerne les differentes sources d'energie disponibles dans l'environnement et exploitables pour alimenter des objets connectes. Chaque source presente des caracteristiques specifiques en termes de densite de puissance, de previsibilite et de conditions d'exploitation.

**Energie solaire (photovoltaique)** :

La recuperation d'energie solaire repose sur l'effet photovoltaique. Les cellules solaires convertissent directement le rayonnement lumineux en electricite. C'est la source la plus mature et la plus efficace pour les applications en exterieur.

- Densite de puissance : 100 mW/cm2 en plein soleil, 0.1 mW/cm2 en interieur
- Rendement des cellules : 15-25% (silicium cristallin), 5-10% (couches minces)
- Avantages : haute densite de puissance, technologie mature
- Inconvenients : intermittence (nuit, nuages), encombrement, degradation dans le temps

**Energie thermique (thermoelectrique)** :

Basee sur l'effet Seebeck, la recuperation thermoelectrique exploite les gradients de temperature entre deux faces d'un module Peltier pour generer de l'electricite.

- Densite de puissance : ~25 uW/cm2 pour un gradient de 5 degres C
- Rendement typique : 1-5% du rendement de Carnot
- Applications : capteurs sur machines industrielles, corps humain (wearables)
- Limitation : necessite un gradient de temperature significatif et stable

**Energie mecanique (piezoelectrique et electromagnetique)** :

La recuperation d'energie mecanique exploite les vibrations, les mouvements ou les deformations pour generer de l'electricite via des materiaux piezoelectriques ou des systemes electromagnetiques (bobine + aimant).

- Densite de puissance : 1-300 uW/cm2 selon la source vibratoire
- Applications : ponts, machines, mouvements humains
- Avantages : disponible dans de nombreux environnements industriels
- Inconvenients : puissance variable, dependance a la frequence de vibration

**Energie radiofrequence (RF)** :

La recuperation d'energie RF capte les ondes electromagnetiques ambiantes (WiFi, signaux cellulaires, broadcast TV/radio) et les convertit en electricite via une rectenna (antenne + redresseur).

- Densite de puissance : tres faible en ambiant (~0.1 uW/cm2), plus elevee avec source dediee
- Frequences exploitees : 900 MHz, 2.4 GHz, 5.8 GHz
- Avantages : disponible partout (en milieu urbain), transfert directionnel possible
- Inconvenients : tres faible puissance recuperee, forte dependance a la distance

**Tableau comparatif des sources d'energie** :

| Source | Densite de puissance | Previsibilite | Maturite | Applications typiques |
|--------|---------------------|---------------|----------|----------------------|
| Solaire (exterieur) | 100 mW/cm2 | Moyenne | Elevee | Capteurs exterieurs |
| Solaire (interieur) | 0.1 mW/cm2 | Bonne | Elevee | Capteurs batiment |
| Thermique | 25 uW/cm2 | Bonne | Moyenne | Industriel, wearable |
| Vibrations | 1-300 uW/cm2 | Variable | Moyenne | Industriel |
| RF ambiante | 0.1 uW/cm2 | Bonne | Faible | Urbain, RFID |

<h3 class="section-title">2. Transfert d'energie sans fil (Wireless Power Transfer)</h3>

Le WPT (Wireless Power Transfer) est une technique qui permet de transmettre de l'energie electrique a distance sans cable, en utilisant des ondes electromagnetiques. Ce concept est fondamental pour alimenter des objets IoT difficiles d'acces ou pour recharger des batteries a distance.

**Principes physiques** :

Le transfert d'energie sans fil repose sur la propagation des ondes electromagnetiques. L'equation de Friis est fondamentale pour calculer la puissance recue a une distance donnee :

```
Pr = Pt * Gt * Gr * (lambda / (4 * pi * d))^2
```

Ou :
- Pr : puissance recue (W)
- Pt : puissance transmise (W)
- Gt : gain de l'antenne d'emission
- Gr : gain de l'antenne de reception
- lambda : longueur d'onde (m)
- d : distance entre les antennes (m)

Cette equation montre que la puissance recue diminue en 1/d2 (loi en inverse du carre de la distance) et augmente avec la longueur d'onde (les basses frequences se propagent mieux).

**Experimentation en TP** :

Lors des travaux pratiques, nous avons evalue la distance maximale de transfert de puissance a differentes frequences. Les resultats montrent clairement que :
- A 868 MHz : portee plus longue grace a une meilleure propagation
- A 2.4 GHz : portee reduite mais antennes plus compactes
- A 5.8 GHz : portee encore plus courte, attenuation plus forte

<div style="text-align: center; display: flex; justify-content: center; gap: 20px;">
    <div style="text-align: center;">
        <img src="/img/BE_Energy_Connected_Object/dist_8_6.png" style="width: 100%;"/>
        <p><em>Distance maximale de transfert a 868 MHz</em></p>
    </div>
    <div style="text-align: center;">
        <img src="/img/BE_Energy_Connected_Object/dist_2_4.png" style="width: 100%;"/>
        <p><em>Distance maximale de transfert a 2.4 GHz</em></p>
    </div>
</div>
<br>

L'attenuation en espace libre (Free Space Path Loss - FSPL) augmente avec la frequence :

```
FSPL (dB) = 20 * log10(d) + 20 * log10(f) + 20 * log10(4 * pi / c)
```

En pratique, les resultats mesures montrent des distances de transfert significativement plus courtes qu'en theorie, dues aux reflexions, diffractions et absorptions dans l'environnement reel.

**Types de WPT** :

| Type | Distance | Frequence | Puissance | Applications |
|------|----------|-----------|-----------|-------------|
| Inductif (champ proche) | < 10 cm | kHz-MHz | W a kW | Recharge smartphone, vehicules |
| Resonant (champ proche) | 10 cm - 1 m | MHz | mW a W | Dispositifs medicaux |
| RF (champ lointain) | 1 m - 10+ m | GHz | uW a mW | Capteurs IoT, RFID |

<h3 class="section-title">3. Selection et caracterisation d'antennes</h3>

Le choix de l'antenne est determinant pour l'efficacite du systeme de recuperation d'energie RF. Lors du cours et des TPs, nous avons compare deux types d'antennes principaux :

**Antenne patch (microstrip)** :

L'antenne patch est une antenne planaire constituee d'un patch metallique sur un substrat dielectrique avec un plan de masse. Elle presente un diagramme de rayonnement directif.

- Gain typique : 5-8 dBi
- Bande passante : etroite (1-5%)
- Diagramme de rayonnement : directif (hemisphere)
- Avantages : compacte, integrable sur PCB, gain eleve
- Inconvenients : bande passante etroite, necesssite orientation vers la source

**Antenne whip (monopole)** :

L'antenne whip est un simple brin metallique vertical, generalement de longueur lambda/4, monte sur un plan de masse.

- Gain typique : 2-5 dBi
- Bande passante : large
- Diagramme de rayonnement : omnidirectionnel (plan horizontal)
- Avantages : omnidirectionnelle, large bande, simple
- Inconvenients : gain plus faible, encombrement en hauteur

<div style="text-align: center; display: flex; justify-content: center; gap: 20px;">
    <div style="text-align: center;">
        <img src="/img/BE_Energy_Connected_Object/Antenna1.png" style="width: 100%;"/>
        <p><em>Antenne patch - diagramme de rayonnement directif</em></p>
    </div>
    <div style="text-align: center;">
        <img src="/img/BE_Energy_Connected_Object/Antenna2.png" style="width: 100%;"/>
        <p><em>Antenne whip - diagramme de rayonnement omnidirectionnel</em></p>
    </div>
</div>
<br>

**Criteres de choix** :

Le choix entre ces deux types d'antennes depend du scenario d'utilisation :

| Critere | Patch | Whip |
|---------|-------|------|
| Mobilite de la source | Non adapte | Adapte |
| Gain maximal | Eleve (directif) | Moyen (omnidirectionnel) |
| Integration | Facile (planaire) | Moderee (3D) |
| Bande passante | Etroite | Large |
| Cas d'usage | Source fixe et connue | Source mobile ou inconnue |

Pour notre projet, le choix s'est porte sur l'antenne whip car la source d'energie RF n'etait pas dans une direction fixe et connue, necessitant une reception omnidirectionnelle.

<h3 class="section-title">4. Chaine de recuperation d'energie RF</h3>

La chaine complete de recuperation d'energie RF comprend plusieurs blocs fonctionnels :

**Architecture d'une rectenna** :

```
Antenne -> Filtre d'adaptation -> Redresseur (rectifier) -> Filtre DC -> Regulateur -> Charge (IoT)
```

**Antenne** : Capte les ondes electromagnetiques et les convertit en signal RF.

**Circuit d'adaptation d'impedance** : Assure le transfert maximal de puissance entre l'antenne (typiquement 50 ohms) et le redresseur. L'adaptation est cruciale car toute desadaptation entraine des pertes par reflexion.

**Redresseur (rectifier)** : Convertit le signal RF alternatif en tension continue. Les diodes Schottky sont privilegiees pour leur faible tension de seuil (~0.2V) et leur rapidite de commutation. Les architectures courantes sont :
- Simple diode (half-wave)
- Doubleur de tension (Villard/Greinacher)
- Multiplicateur de tension (Dickson)

**Filtre DC** : Lisse la tension redessee et elimine les composantes RF residuelles.

**Regulateur** : Adapte la tension de sortie aux besoins de la charge. Des circuits de gestion d'energie dedies (PMIC - Power Management IC) comme le BQ25570 de Texas Instruments sont concus pour fonctionner avec des niveaux de puissance ultra-faibles.

**Rendement global** : Le rendement de la chaine complete est le produit des rendements de chaque etage :

```
eta_total = eta_antenne * eta_adaptation * eta_redresseur * eta_regulateur
```

En pratique, le rendement global est souvent de l'ordre de 10-40% pour une rectenna bien concue, et il varie fortement avec le niveau de puissance d'entree.

<h3 class="section-title">5. Budget energetique d'un noeud IoT</h3>

Le dimensionnement du budget energetique est une etape essentielle dans la conception d'un systeme IoT autonome. Il s'agit de quantifier precisement la consommation de chaque composant et de chaque phase de fonctionnement.

**Modes de fonctionnement d'un noeud IoT** :

Un noeud IoT typique alterne entre plusieurs modes de fonctionnement :

| Mode | Consommation typique | Duree typique |
|------|---------------------|---------------|
| Deep Sleep | 1-10 uA | Minutes a heures |
| Wake-up | 1-5 mA | Quelques ms |
| Mesure capteur | 1-50 mA | 10-100 ms |
| Traitement (MCU actif) | 5-50 mA | 1-100 ms |
| Transmission radio | 20-200 mA | 10-100 ms |
| Reception radio | 10-50 mA | Variable |

**Calcul de la consommation moyenne** :

La consommation moyenne se calcule en pondorant chaque mode par sa duree :

```
I_moyen = (I_sleep * T_sleep + I_actif * T_actif + I_tx * T_tx) / T_cycle
```

Ou T_cycle = T_sleep + T_actif + T_tx est la periode totale d'un cycle.

**Exemple de calcul** :

Pour un capteur qui se reveille toutes les 10 minutes, mesure pendant 50 ms et transmet pendant 100 ms :
- Sleep : 5 uA pendant 599.85 s
- Actif : 10 mA pendant 50 ms
- TX : 100 mA pendant 100 ms

```
I_moyen = (5e-6 * 599.85 + 10e-3 * 0.05 + 100e-3 * 0.1) / 600
I_moyen = (2.999e-3 + 0.5e-3 + 10e-3) / 600
I_moyen = 22.5 uA
```

**Dimensionnement du stockage** :

Pour une autonomie cible de T heures :

```
C_batterie (mAh) = I_moyen (mA) * T (h) * facteur_securite
```

Le facteur de securite (typiquement 1.2-1.5) compense la degradation de la batterie, les variations de temperature et les pics de consommation imprevus.

**Equilibre energetique pour un systeme autonome** :

Pour un systeme alimente par recuperation d'energie, la condition d'autonomie est :

```
P_recuperee_moyenne >= P_consommee_moyenne
```

Si cette condition n'est pas satisfaite en permanence, un element de stockage (batterie, supercondensateur) doit compenser les periodes deficitaires.

<h3 class="section-title">6. Stockage d'energie</h3>

Le choix du systeme de stockage est crucial et depend des besoins en energie, en puissance et en duree de vie.

**Batteries** :

- Lithium-ion : haute densite energetique (150-250 Wh/kg), 500-1000 cycles
- Lithium-polymere : forme flexible, densite similaire au Li-ion
- Lithium-primaire (non rechargeable) : tres haute densite, longue duree de vie (10+ ans)
- Limitation : nombre de cycles limite, degradation avec le temps, sensibilite a la temperature

**Supercondensateurs** :

- Densite de puissance elevee (jusqu'a 10 kW/kg)
- Nombre de cycles quasi-illimite (>500 000 cycles)
- Charge/decharge rapide
- Faible densite energetique (5-10 Wh/kg)
- Adaptes aux pics de puissance et aux systemes de recuperation d'energie intermittente

**Comparaison** :

| Critere | Batterie Li-ion | Supercondensateur |
|---------|----------------|-------------------|
| Densite energetique | 150-250 Wh/kg | 5-10 Wh/kg |
| Densite de puissance | 0.3-1.5 kW/kg | 1-10 kW/kg |
| Cycles de vie | 500-1000 | >500 000 |
| Auto-decharge | 2-5%/mois | 5-40%/jour |
| Temps de charge | Heures | Secondes |

<h3 class="section-title">7. Gestion d'energie (Power Management)</h3>

La gestion d'energie est le pont entre la source d'energie (recuperation ou batterie) et la charge (noeud IoT). Elle assure la regulation, la protection et l'optimisation du flux energetique.

**Composants cles** :

**Regulateurs lineaires (LDO)** :
- Simples, faible bruit
- Rendement : eta = Vout/Vin (faible si grande difference)
- Adaptes quand Vin est proche de Vout

**Regulateurs a decoupage (DC-DC)** :
- Buck (abaisseur) : Vout < Vin
- Boost (eleveur) : Vout > Vin
- Buck-boost : Vout peut etre superieur ou inferieur a Vin
- Rendement eleve : 85-95%
- Bruit de commutation a filtrer

**PMIC dedies IoT** :
Des circuits integres comme le BQ25570 (Texas Instruments) ou le AEM10941 (e-peas) sont specialement concus pour la recuperation d'energie ultra-faible. Ils integrent :
- Un boost converter avec seuil de demarrage tres bas (~100 mV)
- Un MPPT (Maximum Power Point Tracking) pour optimiser l'extraction d'energie
- Un chargeur de batterie/supercondensateur
- Un regulateur de sortie

**MPPT (Maximum Power Point Tracking)** :

Le MPPT est un algorithme qui ajuste dynamiquement le point de fonctionnement du systeme de recuperation pour extraire la puissance maximale. Pour les cellules solaires, le point de puissance maximale correspond typiquement a 70-80% de la tension en circuit ouvert (Voc).

<h3 class="section-title">8. Application au projet : What a Leak</h3>

Dans le cadre de notre [projet innovant (What a Leak)](./innovative-project.html), nous avons cherche a appliquer les concepts du cours pour concevoir un systeme de detection de fuites d'eau autonome energetiquement.

**Objectif** : Alimenter un noeud capteur (detecteur de fuite) par recuperation d'energie, elimiant la necessite de changement de batterie dans des emplacements difficiles d'acces (sous des eviers, dans des combles, etc.).

**Contraintes** :
- Environnement interieur (faible luminosite, pas de vent)
- Faible gradient de temperature
- Ondes RF ambiantes faibles
- Besoin de transmission periodique des donnees

**Evaluation des sources** :

Nous avons evalue chaque source d'energie pour notre cas d'usage specifique. Malheureusement, l'environnement interieur typique ne fournit pas suffisamment d'energie ambiante pour alimenter de maniere fiable notre noeud capteur. Les niveaux de puissance RF ambiants sont trop faibles et l'eclairage interieur ne genere pas assez de puissance avec de petites cellules solaires.

Cette analyse, bien que concluant a l'impossibilite pratique d'un systeme totalement autonome dans notre cas, a ete tres formatrice. Elle m'a appris a evaluer rigoureusement la faisabilite energetique d'un systeme avant de se lancer dans la conception.

---

## PART D - Analyse et Reflexion

<h3 class="section-title">Competences acquises</h3>

**Comprehension energetique globale** :
Capacite a identifier, evaluer et comparer les differentes sources d'energie ambiante pour des applications IoT, et a choisir la plus adaptee selon le contexte de deploiement.

**Dimensionnement de systemes** :
Aptitude a calculer un budget energetique complet, du capteur a la transmission, en tenant compte de tous les modes de fonctionnement et de leur duree.

**Conception RF** :
Connaissance des principes de propagation des ondes, de la formule de Friis, et capacite a selectionner et caracteriser des antennes pour la recuperation d'energie.

**Gestion d'energie** :
Comprehension des architectures de gestion d'energie (LDO, DC-DC, PMIC) et de leur adequation aux differents scenarios de recuperation d'energie.

**Approche experimentale** :
Competence pour realiser des mesures de transfert d'energie sans fil, interpreter les resultats et les comparer aux modeles theoriques.

<h3 class="section-title">Auto-evaluation</h3>

Ce cours m'a apporte beaucoup de connaissances nouvelles sur un sujet que je ne connaissais pas avant. J'ai decouvert l'etendue des possibilites pour alimenter des objets connectes a partir de l'energie ambiante, qu'il s'agisse de la lumiere, de la chaleur, des vibrations ou des ondes electromagnetiques.

Les travaux pratiques ont ete particulierement enrichissants. Nous avons etudie les besoins en puissance d'une petite LED rouge, teste des approches d'utilisation directe de l'energie et de stockage. Ces experimentations m'ont permis de confronter la theorie a la realite et de comprendre les limites pratiques de la recuperation d'energie.

J'aurais aime pouvoir appliquer davantage ces concepts a un projet concret. Si le projet innovant visait cet objectif, l'environnement de deploiement ne nous a pas permis de recuperer suffisamment d'energie ambiante. Cette limitation a toutefois ete formatrice : elle m'a appris que l'evaluation de faisabilite energetique est une etape critique dans tout projet IoT.

Les sessions de TP sur les antennes m'ont egalement permis de comprendre l'importance du choix de l'antenne et de son positionnement. C'est un aspect souvent neglige dans les projets IoT mais qui peut faire la difference entre un systeme fonctionnel et un systeme defaillant.

<h3 class="section-title">Applications professionnelles</h3>

Les competences acquises dans ce cours sont directement applicables dans de nombreux domaines :

**IoT industriel** :
- Capteurs autonomes pour la maintenance predictive
- Surveillance d'equipements dans des zones difficiles d'acces
- Monitoring environnemental longue duree

**Smart Building** :
- Capteurs de temperature, humidite, qualite d'air sans cablage
- Interrupteurs sans pile (piezoelectrique)
- Compteurs de personnes autonomes

**Sante connectee** :
- Wearables alimentes par l'energie du corps
- Implants medicaux avec recuperation d'energie sans fil
- Monitoring patient en continu

**Agriculture de precision** :
- Capteurs de sol autonomes (solaire)
- Surveillance des cultures sur de grandes surfaces
- Stations meteo connectees

<h3 class="section-title">Mon avis</h3>

Ce cours m'a permis de comprendre des aspects de l'IoT que je ne soupconnais pas. Par exemple, la grande variete de possibilites pour alimenter des objets avec des ondes electromagnetiques et d'autres sources d'energie disponibles dans notre environnement. De plus, apprendre a choisir une antenne et comprendre ses principes de fonctionnement etait particulierement interessant.

La combinaison de la theorie et de la pratique etait bien equilibree. Le cours magistral fournissait les bases necessaires, et les TPs permettaient de verifier ces concepts experimentalement. J'ai particulierement apprecie la methodologie rigoureuse pour le calcul du budget energetique, qui est une competence directement transferable a tout projet IoT.

Ce module m'a donne une vision plus complete de la conception de systemes IoT, en integrant la dimension energetique des le debut du processus de conception.

---

## Rapports et Projets

<div style="text-align: center;">
    <h3 class="section-title">Rapport de TP - Energy for Connected Objects</h3>
</div>

<div style="display: flex; justify-content: center;">
    <embed src="/file/reports/S9/Report_Energy_Boukouiss_Chanfreau.pdf" width="100%" height="800px" type="application/pdf">
</div>

<p style="text-align: center;">
    <a href="/file/reports/S9/Report_Energy_Boukouiss_Chanfreau.pdf" target="_blank">Ouvrir le rapport complet</a>
</p>

<div style="text-align: center;">
    <h3 class="section-title">Sujet de TP</h3>
</div>

<div style="display: flex; justify-content: center;">
    <embed src="/img/BE_Energy_Connected_Object/Lab_Subject_energy.pdf" width="100%" height="800px" type="application/pdf">
</div>

<p style="text-align: center;">
    <a href="/img/BE_Energy_Connected_Object/Lab_Subject_energy.pdf" target="_blank">Ouvrir le sujet de TP</a>
</p>

---

## Documents de Cours

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
      <h4>Cours - Energy for IoT</h4>
      <p>Cours complet : sources d'energie ambiante, recuperation d'energie, transfert sans fil, gestion d'energie et budget energetique pour les objets connectes.</p>
      <embed src="/cours-pdf/S9/Energy/5ISS_-_Energy_for_IoT.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/Energy/5ISS_-_Energy_for_IoT.pdf" target="_blank">Telecharger</a></p>
    </div>
  </div>
</div>

---

*Cours suivi en 2024-2025 a l'INSA Toulouse, Departement Genie Electrique et Informatique, parcours ISS (Innovative Smart Systems).*

<div class="back-nav">
    <a href="./my-courses-2024-2025.html">&larr; Retour aux Cours 2024-2025</a>
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

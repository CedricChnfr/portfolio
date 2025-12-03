---
layout: default
title: "Projet PCB - S6"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
---

<style>
.back-nav {
    background: #f4f4f4;
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 20px;
}

.section-title {
    color: #2a7ae2;
    border-bottom: 2px solid #2a7ae2;
    padding-bottom: 5px;
    margin-top: 30px;
}

table {
    border-collapse: collapse;
    width: 100%;
    margin: 20px 0;
}

th {
    background-color: #2a7ae2;
    color: white;
    padding: 10px;
    text-align: left;
}

td {
    border: 1px solid #ddd;
    padding: 10px;
}

tr:nth-child(even) {
    background-color: #f9f9f9;
}

.code-block {
    background: #f4f4f4;
    border-left: 4px solid #2a7ae2;
    padding: 15px;
    margin: 15px 0;
    font-family: 'Courier New', monospace;
}
</style>

<div class="back-nav">
    <a href="./my-courses-2022-2023.html">← Retour aux Cours 2022-2023</a>
</div>

# 🔧 Projet PCB - Semestre 6

**Année Universitaire** : 2022-2023  
**Semestre** : 6  
**Crédits** : 2 ECTS  
**Spécialité** : Conception Électronique

---

## PART A - Présentation Générale du Projet

<h3 class="section-title">Vue d'ensemble</h3>

Ce projet consiste à concevoir une carte électronique complète (PCB) de A à Z avec Altium Designer : schématiques, routage, création de composants, et génération des fichiers de fabrication. Le projet est un objet connecté avec interface tactile, LED RGB, alimentation autonome sur batterie, et microcontrôleur STM32.

**Objectifs pédagogiques** :
- Maîtriser Altium Designer (logiciel professionnel de conception PCB)
- Concevoir des schémas électriques hiérarchiques
- Créer des bibliothèques de composants (symboles et empreintes)
- Router une carte multicouche
- Générer les fichiers de fabrication (Gerber, perçage, BOM)
- Modéliser en 3D et intégrer dans un boîtier

<h3 class="section-title">Position dans le cursus</h3>

Ce projet s'appuie sur :
- **Circuits et Filtres Analogiques (S5)** : conception circuits analogiques
- **Électronique Fonctions Analogiques (S6)** : alimentation, régulation
- **Microcontrôleur (S6)** : interfaçage STM32, périphériques

Il prépare aux applications :
- **Conception de produits électroniques** : prototype → production
- **IoT et objets connectés** : cartes custom optimisées
- **Intégration système** : mécanique + électronique

---

## PART B - Expérience Personnelle et Contexte d'Apprentissage

<h3 class="section-title">Organisation et ressources</h3>

Le projet était structuré en plusieurs étapes sur le semestre :

**Phase 1 : Spécifications et architecture (2 semaines)**
- Définition du cahier des charges
- Choix des composants
- Schéma bloc fonctionnel

**Phase 2 : Schématiques (3 semaines)**
- Création des bibliothèques de composants
- Dessin des schémas électriques
- Vérifications électriques (ERC)

**Phase 3 : Routage PCB (4 semaines)**
- Placement des composants
- Routage des pistes
- Plans de masse et alimentation
- Vérifications design rules (DRC)

**Phase 4 : Fabrication et assemblage (2 semaines)**
- Génération fichiers Gerber
- Commande fabrication
- Assemblage et tests

**Environnement de travail** :
- **Logiciel** : Altium Designer 22
- **Fabricant** : JLCPCB ou PCBWay (Chine)
- **Assemblage** : manuel avec fer à souder
- **Tests** : multimètre, oscilloscope, programmation STM32

<h3 class="section-title">Description du projet</h3>

**Concept** : Carte interactive avec interface tactile et retour visuel LED RGB.

**Architecture système** :

| Module | Composants | Fonction |
|--------|------------|----------|
| Alimentation | Batterie Li-Ion, régulateur 3,3V | Autonomie énergétique |
| Contrôle | STM32F103 | Cerveau du système |
| Interface utilisateur | Capteurs tactiles capacitifs | Interaction utilisateur |
| Retour visuel | LED RGB WS2812B | Affichage couleurs |
| Communication | USB Type-C | Programmation + alimentation |

**Modules développés** :

**1. Alimentation** (Alimentation_PCB.SchDoc)

Circuit de gestion d'alimentation avec :
- Connecteur USB Type-C pour charge et programmation
- Régulateur de tension 5V → 3,3V (pour STM32 et périphériques)
- Protection batterie Li-Ion (charge/décharge)
- Convertisseur DC-DC boost/buck si nécessaire
- Condensateurs de découplage (100 nF, 10 µF)

**Composants principaux** :
- Régulateur linéaire LDO (AMS1117-3.3) ou switching (LM2596)
- Diodes de protection Schottky
- Inductances de filtrage
- Réseau de condensateurs (céramiques + électrolytiques)

**2. Microcontrôleur** (MicroContrôleur.SchDoc)

Circuit STM32F103 avec :
- Oscillateur externe 8 MHz (quartz + condensateurs 22 pF)
- Condensateurs de découplage sur chaque alimentation (100 nF)
- Connecteur SWD pour programmation/débogage (4 broches : SWDIO, SWCLK, GND, 3.3V)
- Bouton reset
- LED de statut
- Pull-up sur BOOT0 (mode normal)

**Connexions** :
- GPIO pour LED RGB (PA0 → data LED)
- GPIO pour capteurs tactiles (PB8-PB11)
- UART pour debug (PA9/PA10)
- USB (PA11/PA12) si utilisé

**3. LED RGB** (LED_RGB.SchDoc)

Chaîne de LED adressables WS2812B :
- 8 à 16 LED RGB connectées en série
- Alimentation 5V (important : ne pas alimenter en 3,3V)
- Résistance de protection sur data (470 Ω)
- Condensateur de découplage par LED (100 nF proche de chaque LED)

**Protocole** :
- 1 fil de données (protocole propriétaire WS2812)
- Timing critique (nécessite PWM précis du STM32)
- Chaque LED reçoit 24 bits (8R + 8G + 8B) puis transmet au suivant

**4. Interface tactile** (Touch.SchDoc)

Capteurs tactiles capacitifs :
- 4 à 8 zones tactiles (pads PCB en cuivre)
- Contrôleur tactile dédié (TTP223 ou équivalent) ou GPIO STM32
- Résistances de pull-up/down
- Condensateurs de filtrage anti-bruit

**Principe** :
- Capacité change quand doigt approche
- Détection par mesure de temps de charge/décharge
- Sensibilité ajustable par résistance

<h3 class="section-title">Création des bibliothèques de composants</h3>

**Symboles schématiques (.SchLib)** :

Pour chaque composant, création du symbole selon normes IEEE :
- Résistance : rectangle avec valeur
- Condensateur : deux barres parallèles
- Inductance : spirale
- Circuits intégrés : rectangle avec broches numérotées

**Propriétés à définir** :
- Nom du composant (Designator : R1, C1, U1...)
- Valeur (Value : 10k, 100nF, STM32F103...)
- Description
- Référence fournisseur (Supplier Part Number)
- Datasheet (lien)

**Empreintes PCB (.PcbLib)** :

Pour chaque composant, création du footprint :
- **Résistances/condensateurs SMD** : format 0603, 0805, 1206
  - 0603 : 1,6 mm × 0,8 mm (petits, difficiles à souder)
  - 0805 : 2,0 mm × 1,25 mm (bon compromis)
  - 1206 : 3,2 mm × 1,6 mm (gros, facile à souder)

- **Circuits intégrés** :
  - LQFP-48 pour STM32F103 (pitch 0,5 mm)
  - SOT-23 pour régulateurs
  - DIP/SOP pour autres CI

**Définition empreinte** :
- Pads (taille, forme, spacing)
- Sérigraphie (outline composant, numéro broche 1)
- Courtyard (zone réservée autour composant)
- Modèle 3D (fichier STEP pour visualisation)

**Exemple : résistance 0805**
```
Pad 1 : 1,2 mm × 1,4 mm à (-0,95, 0)
Pad 2 : 1,2 mm × 1,4 mm à (+0,95, 0)
Silkscreen : rectangle 2,0 mm × 1,25 mm
```

<h3 class="section-title">Schématiques et hiérarchie</h3>

**Organisation hiérarchique** :

Le projet utilise plusieurs feuilles de schéma :

**Main.SchDoc** : schéma principal
- Blocs fonctionnels (alimentation, MCU, LED, touch)
- Connecteurs inter-modules
- Vue d'ensemble du système

**Schémas secondaires** :
- Alimentation_PCB.SchDoc : détail circuit alimentation
- MicroContrôleur.SchDoc : détail STM32 et périphériques
- LED_RGB.SchDoc : chaîne de LED
- Touch.SchDoc : capteurs tactiles

**Avantages de la hiérarchie** :
- Clarté : chaque feuille a une fonction
- Modularité : modification d'un module sans toucher aux autres
- Réutilisabilité : modules réutilisables dans autres projets

**Connexions inter-feuilles** :
- Ports (Port) : points d'entrée/sortie d'une feuille
- Netlist : Altium gère automatiquement les connexions

<h3 class="section-title">Routage du PCB</h3>

**Spécifications de la carte** :
- Dimensions : environ 80 mm × 60 mm (adaptée au boîtier)
- Couches : 2 couches (Top + Bottom) suffisant pour ce projet
- Épaisseur cuivre : 35 µm (1 oz)
- Finition : HASL (Hot Air Solder Leveling) ou ENIG (nickel/or)
- Vernis épargne (solder mask) : vert
- Sérigraphie : blanc

**Étapes de routage** :

**1. Définition du contour** (carte_plexi_outline.PcbDoc)

Outline de la carte selon le boîtier :
- Forme rectangulaire ou custom
- Trous de fixation (M3 typiquement)
- Découpes pour connecteurs (USB Type-C)

**2. Placement des composants**

Règles de placement :
- **Alimentation** : près du connecteur USB
- **STM32** : au centre, accès facile pour routage
- **LED RGB** : en périphérie ou selon design visuel
- **Capteurs tactiles** : sur edge de la carte ou face arrière
- **Condensateurs de découplage** : au plus près des broches d'alimentation

**Considérations** :
- Hauteur composants (sous boîtier)
- Zones thermiques (régulateur chauffe)
- Accessibilité pour soudure
- Sens des composants polarisés

**3. Routage des pistes**

**Ordre de priorité** :
1. Alimentation (3,3V, 5V, GND) : pistes larges
2. Signaux critiques (data LED, oscillateur)
3. Signaux GPIO standards
4. Signaux secondaires

**Largeurs de pistes** :

| Type de signal | Courant | Largeur |
|----------------|---------|---------|
| Alimentation 5V | 500 mA | 0,5 mm minimum |
| Alimentation 3,3V | 200 mA | 0,3 mm |
| Signaux numériques | < 10 mA | 0,2 mm |
| Données LED (PWM) | < 5 mA | 0,2 mm |

Calcul : 1 A nécessite environ 1 mm de largeur sur cuivre 35 µm.

**Plans de masse** :
- Plan GND sur Bottom layer (cuivre plein)
- Vias de connexion GND fréquents
- Découplage capacitif efficace

**4. Règles de conception (Design Rules)**

Configuration Altium :
- Clearance minimum : 0,2 mm (sécurité fabrication)
- Largeur piste minimum : 0,2 mm
- Diamètre via : 0,6 mm (trou 0,3 mm)
- Distance pad-piste : 0,2 mm

**5. Vérifications**

**DRC (Design Rule Check)** :
- Aucune violation de clearance
- Pas de piste trop fine
- Pas de via trop proche du bord

**ERC (Electrical Rule Check)** sur schéma :
- Toutes les broches connectées
- Pas de court-circuit
- Alimentations correctes

<h3 class="section-title">Génération des fichiers de fabrication</h3>

**Fichiers Gerber** :

Format standard pour fabrication PCB. Un fichier par couche :

| Fichier | Extension | Contenu |
|---------|-----------|---------|
| Top layer | .GTL | Cuivre face supérieure |
| Bottom layer | .GBL | Cuivre face inférieure |
| Top solder mask | .GTS | Vernis épargne dessus |
| Bottom solder mask | .GBS | Vernis épargne dessous |
| Top silkscreen | .GTO | Sérigraphie dessus |
| Bottom silkscreen | .GBO | Sérigraphie dessous |
| Drill file | .TXT | Perçages |
| Board outline | .GKO | Contour carte |

**Fichiers complémentaires** :

**BOM (Bill of Materials)** :
Liste exhaustive des composants avec :
- Référence (R1, C5, U1...)
- Valeur (10k, 100nF, STM32F103...)
- Boîtier (0805, LQFP-48...)
- Quantité
- Fournisseur et référence (Mouser, DigiKey...)

**Pick and Place** :
Fichier CSV pour assemblage automatique (si fabriqué industriellement).
Coordonnées X,Y et rotation de chaque composant.

**3D Export** :
Fichier STEP pour vérification mécanique et intégration dans boîtier (SolidWorks, Fusion 360).

<h3 class="section-title">Modélisation 3D et boîtier</h3>

**Fichiers 3D disponibles** :
- Carte_PCB.step : carte électronique avec composants
- Boitier_PCB.step : boîtier inférieur
- Couvercle_PCB.step : couvercle supérieur
- Plaque_tactile_PCB.step : interface tactile
- Assemblage_plecs_bois.step : assemblage complet

**Intégration mécanique** :
- Vérification des interférences (composants vs boîtier)
- Accès USB Type-C
- Visibilité LED RGB
- Zones tactiles accessibles
- Fixations M3

<h3 class="section-title">Difficultés rencontrées</h3>

**Création de bibliothèques** :
Chronophage et minutieux. Erreur dans empreinte = PCB inutilisable. Importance de vérifier dimensions dans datasheet.

**Routage contraint** :
Espace limité, nombreux composants. Nécessité de compromis entre idéal (pistes courtes) et faisable.

**Vérifications et erreurs** :
DRC/ERC peuvent générer des centaines d'erreurs. Il faut toutes les corriger avant fabrication.

**Choix des composants** :
Disponibilité, coût, taille. Certains composants en rupture de stock. Prévoir des alternatives.

---

## PART C - Aspects Techniques Détaillés

<h3 class="section-title">1. Altium Designer - Fonctionnalités</h3>

**Modules principaux** :

| Module | Fonction |
|--------|----------|
| Schematic Editor | Dessin schémas électriques |
| PCB Editor | Routage carte PCB |
| Library Editor | Création symboles et empreintes |
| 3D Viewer | Visualisation 3D de la carte |
| Output Jobs | Génération fichiers fabrication |
| Project Panel | Gestion fichiers et hiérarchie |

**Raccourcis utiles** :
- P + W : placer un fil (wire)
- P + N : placer un net label
- P + P : placer un composant (part)
- T + R : tracer une piste (track route)
- T + V : placer un via
- Shift + S : afficher/masquer couches
- 3 : vue 3D

<h3 class="section-title">2. Technologies PCB</h3>

**Types de vias** :

| Type | Description | Usage |
|------|-------------|-------|
| Through-hole | Traverse toutes les couches | Standard, 2-4 couches |
| Blind | Connecte surface à couche interne | Cartes multicouches avancées |
| Buried | Entre couches internes uniquement | Haute densité |
| Micro-via | Très petit diamètre (< 0,2 mm) | HDI (High Density Interconnect) |

**Finitions de surface** :

| Finition | Avantages | Inconvénients |
|----------|-----------|---------------|
| HASL | Économique, robuste | Surface irrégulière |
| ENIG | Surface plane, bonne soudabilité | Plus cher |
| OSP | Économique, éco-friendly | Courte durée de vie |
| Immersion Tin | Bon compromis | Oxydation à long terme |

<h3 class="section-title">3. Règles de conception PCB</h3>

**Pistes d'alimentation** :

Largeur en fonction du courant :
- 0,1 A : 0,15 mm minimum
- 0,5 A : 0,4 mm
- 1 A : 0,8 mm
- 2 A : 1,5 mm

Ces valeurs supposent cuivre 35 µm et élévation température 10°C.

**Découplage** :

Condensateurs de découplage pour chaque circuit intégré :
- 100 nF céramique au plus près de chaque broche VDD/VSS
- 10 µF électrolytique ou céramique par groupe de CI
- Pistes courtes (< 5 mm idéalement)

**Oscillateur** :

Circuit critique pour STM32 :
- Pistes courtes et symétriques
- Plans GND autour (garde)
- Condensateurs 22 pF proches du quartz
- Pas de pistes de signal qui croisent

**Impédance contrôlée** :

Pour signaux haute vitesse (USB, Ethernet, HDMI) :
- Largeur piste calculée selon impédance cible (50 Ω, 90 Ω...)
- Distance au plan de référence
- Paires différentielles appariées

<h3 class="section-title">4. Processus de fabrication</h3>

**Étapes de fabrication industrielle** :

1. **Impression** : transfert motif sur substrat
2. **Gravure** : retrait du cuivre non protégé
3. **Perçage** : trous vias et composants traversants
4. **Placage** : dépôt cuivre dans les trous
5. **Vernis épargne** : application solder mask
6. **Sérigraphie** : impression textes et repères
7. **Finition** : HASL, ENIG, etc.
8. **Test électrique** : vérification continuités et isolations
9. **Découpe** : séparation des panneaux

**Délais et coûts** :

Pour fabricants chinois (JLCPCB, PCBWay) :
- 10 PCB 100×100 mm, 2 couches : 5-10 €
- Délai fabrication : 24-48h
- Expédition express : 3-7 jours
- Total : environ 30 € et 1 semaine

<h3 class="section-title">5. Assemblage et soudure</h3>

**Composants CMS (SMD)** :

Techniques de soudure :
- **Fer à souder** : pour 0805 et plus gros, ou faible quantité
- **Plaque chauffante** : pour circuits complexes
- **Four à refusion** : industriel ou DIY (contrôleur PID)

**Étapes soudure manuelle** :
1. Appliquer flux sur pads
2. Étamer un pad
3. Positionner composant avec pince
4. Souder premier côté
5. Souder second côté
6. Vérifier avec loupe

**Pâte à souder et refusion** :
1. Appliquer pâte à braser (seringue ou pochoir)
2. Placer composants (pince ou pick & place manuel)
3. Chauffer progressivement jusqu'à 220-250°C
4. Refroidir lentement

<h3 class="section-title">6. Tests et validation</h3>

**Tests de continuité** :
- Multimètre en mode testeur de continuité
- Vérifier alimentations (pas de court-circuit VCC-GND)
- Vérifier connexions critiques

**Tests fonctionnels** :
- Alimenter en 5V via USB
- Vérifier 3,3V en sortie régulateur
- Programmer STM32 via SWD
- Tester LED RGB (une par une)
- Tester capteurs tactiles

**Débogage problèmes courants** :
- Pas d'alimentation : vérifier régulateur, condensateurs
- Programmation impossible : vérifier connexions SWD, reset
- LED ne s'allument pas : vérifier alimentation 5V, data line
- Tactile ne répond pas : vérifier sensibilité, connexions

---

## PART D - Analyse Réflexive et Perspectives

<h3 class="section-title">Compétences acquises</h3>

**Maîtrise logicielle** :
Altium Designer est un outil professionnel complexe. La courbe d'apprentissage est raide, mais les compétences sont directement applicables en entreprise (standard industrie avec Eagle, KiCad).

**Vision système** :
Le projet oblige à penser l'électronique dans sa globalité : schémas, routage, mécanique, fabrication, coût. Compréhension du cycle complet conception → production.

**Rigueur et attention aux détails** :
Une erreur dans le PCB coûte temps et argent (refabrication). Importance des vérifications systématiques (DRC, ERC, revue manuelle).

<h3 class="section-title">Points clés à retenir</h3>

**1. Composants = fondation** :
Choisir les bons composants dès le départ. Vérifier disponibilité, coût, et alternatives. Une rupture de stock peut bloquer le projet.

**2. Bibliothèques = investissement** :
Créer des bibliothèques propres et vérifiées. Réutilisables dans projets futurs. Gain de temps énorme.

**3. DRC/ERC = amis** :
Ne jamais ignorer les erreurs. Toutes corriger avant fabrication. Un warning peut cacher un problème grave.

**4. Découplage = stabilité** :
Condensateurs de découplage ne sont pas optionnels. Instabilité, resets aléatoires, comportement erratique sinon.

**5. Plans de masse = impératif** :
Un bon plan de masse améliore considérablement stabilité, bruit, et facilite routage.

<h3 class="section-title">Applications pratiques</h3>

**Prototypage rapide** :
Capacité à concevoir et commander des PCB custom pour projets personnels ou professionnels en quelques jours.

**Objets connectés** :
Compétence clé pour IoT : concevoir cartes optimisées (taille, consommation, coût) plutôt que cartes dev généralistes.

**Produits commerciaux** :
De prototype à production : optimisation coûts, DFM (Design For Manufacturing), assemblage automatisé.

**Consulting** :
Service de conception PCB très demandé. Nombreux clients ont des idées mais pas les compétences pour réaliser le PCB.

<h3 class="section-title">Retour d'expérience projet</h3>

**Aspects positifs** :
- Projet concret avec résultat tangible (PCB physique)
- Liberté créative dans conception
- Utilisation d'outil professionnel (Altium)
- Valorisant de tenir sa propre carte fonctionnelle

**Défis techniques** :
- Temps d'apprentissage Altium (interface complexe)
- Nombreux détails à gérer simultanément
- Stress avant réception PCB (erreurs possibles)
- Soudure CMS difficile pour débutants

**Améliorations possibles** :
- Ajout de fonctionnalités (Bluetooth, capteurs)
- Réduction taille (optimisation placement)
- Passage 4 couches (meilleur routage)
- Assemblage professionnel (moins d'erreurs soudure)

<h3 class="section-title">Limites et ouvertures</h3>

**Limites du projet** :
- Carte relativement simple (2 couches)
- Peu de signaux haute vitesse (pas d'impédance contrôlée)
- Pas d'RF (WiFi, Bluetooth)
- Pas de circuits analogiques avancés

**Ouvertures vers** :
- **PCB avancés** : 6-8 couches, HDI, flex PCB
- **Signaux haute vitesse** : DDR, PCIe, USB 3.0
- **RF design** : antennes, adaptation d'impédance
- **Puissance** : gestion thermique, courants élevés
- **Certification** : CE, FCC pour produits commerciaux

<h3 class="section-title">Évolution technologique</h3>

**Tendances actuelles** :
- **Miniaturisation** : composants toujours plus petits (0201, 01005)
- **Intégration** : SoC intégrant tout sur puce
- **HDI** : PCB haute densité avec micro-vias
- **Flex et rigid-flex** : cartes souples ou mixtes
- **Embedded components** : composants intégrés dans PCB

**Outils modernes** :
- **KiCad** : alternative open-source à Altium
- **EasyEDA** : éditeur en ligne gratuit
- **Fusion 360 Electronics** : Autodesk (gratuit étudiants)
- **AI-assisted routing** : routage automatique intelligent

<h3 class="section-title">Conclusion</h3>

Le projet PCB est une expérience formatrice essentielle pour tout ingénieur électronique ou systèmes embarqués. La capacité à concevoir ses propres cartes ouvre de nombreuses possibilités : prototypes, produits, objets connectés.

Altium Designer est un outil puissant mais exigeant. La maîtrise demande de la pratique, mais les compétences acquises sont valorisées en entreprise. Les alternatives gratuites (KiCad) permettent de continuer à pratiquer sans licence coûteuse.

**Philosophie du projet** :
De l'idée au PCB physique en quelques semaines. Satisfaction de concevoir quelque chose de tangible et fonctionnel. Chaque erreur est une leçon (parfois coûteuse, mais formative).

**Recommandations** :
- Commencer simple (LED blinking) avant projets complexes
- Vérifier, re-vérifier, et vérifier encore avant fabrication
- Commander quelques PCB en plus (pièces de rechange)
- Documenter le projet (schémas, BOM, notes de fabrication)
- Partager sur GitHub/Hackaday pour portfolio

**Liens avec les autres cours** :
- [Microcontrôleur - S6](./microcontroleur.html) : programmation STM32
- [Électronique Fonctions Analogiques - S6](./electronique-fonctions-analogiques.html) : circuits d'alimentation
- [Électronique Fonctions Numériques - S6](./electronique-fonctions-numeriques.html) : bus I2C/SPI
- [Architecture Matérielle - S6](./architecture-materielle.html) : compréhension hardware

---

*Projet réalisé en 2022-2023 à l'INSA Toulouse, Département Génie Électrique et Informatique.*

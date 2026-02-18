---
layout: default
title: "Automatisme - S3"
date:   2024-10-02 10:56:03 +0200
---

<style>
.back-nav { margin-bottom: 20px; }
.back-nav a { text-decoration: none; color: #2a7ae2; font-weight: 600; }
.back-nav a:hover { text-decoration: underline; }
.section-title { color: #2a7ae2; border-bottom: 2px solid #2a7ae2; padding-bottom: 10px; margin-top: 30px; margin-bottom: 20px; }
</style>

<div class="back-nav">
  <a href="./my-courses-2021-2022.html">&larr; Retour a Mes Cours 2021-2022</a>
</div>

# Automatisme - Semestre 3

**Annee**: 2021-2022 | **Semestre**: 3 | **Type**: Technique

---

## PART A - Présentation Générale du Cours

### Contexte pédagogique

L'automatisme industriel représente une composante majeure du DUT GEII spécialisation ENOC (Électronique Numérique et Objets Connectés). Positionné au semestre 3, ce cours s'appuie sur les bases de logique séquentielle (S1) et approfondit la conception de systèmes automatisés complexes. Il établit la distinction fondamentale entre le contrôle continu (automatique) et le contrôle séquentiel (automatisme), deux approches complémentaires dans l'industrie.

L'automatisme trouve ses applications dans tous les secteurs industriels : manufacturier, agroalimentaire, automobile, énergie, où les automates programmables industriels (API) orchestrent les processus de production, garantissant productivité, qualité et sécurité.

### Objectifs d'apprentissage

**Objectifs principaux :**
- Maîtriser le langage normalisé GRAFCET (IEC 60848) pour la spécification fonctionnelle
- Programmer des automates industriels selon la norme IEC 61131-3
- Concevoir des systèmes séquentiels répondant à un cahier des charges industriel
- Intégrer capteurs et actionneurs dans une architecture automatisée
- Garantir la sécurité des systèmes par conception

**Compétences opérationnelles :**
- Analyse de cahier des charges et décomposition fonctionnelle
- Modélisation GRAFCET hiérarchisé (niveaux 1 et 2)
- Programmation multi-langage (Ladder, SFC, ST, FBD)
- Mise en service et diagnostic de systèmes automatisés
- Documentation technique normalisée

### Prérequis

- Logique combinatoire et séquentielle (bascules, compteurs, registres)
- Algèbre de Boole et tableaux de Karnaugh
- Bases en électrotechnique (capteurs TOR, actionneurs)
- Notions de programmation structurée
- Lecture de schémas électriques industriels

### Positionnement dans le cursus

Ce cours se situe à l'interface entre :
- **Électronique numérique** : Implémentation matérielle de la logique
- **Informatique industrielle** : Programmation et architectures
- **Automatique** : Complémentarité contrôle séquentiel/continu
- **Projets** : Application sur systèmes réels (mini-projet ascenseur, station de tri)

---

## PART B: EXPÉRIENCE, CONTEXTE ET FONCTION DU COURS

### Module 1 : GRAFCET - Graphe Fonctionnel de Commande Étape-Transition

#### Introduction au GRAFCET

**Définition :**
Le GRAFCET (Graphe Fonctionnel de Commande Étape-Transition) est un outil graphique normalisé (IEC 60848) permettant de décrire le comportement d'un automatisme séquentiel.

**Historique et normalisation :**
- Créé en France dans les années 1970 (AFCET)
- Normalisé internationalement : IEC 60848 (2002)
- Équivalent international : SFC (Sequential Function Chart) dans IEC 61131-3
- Standard dans l'industrie française

**Avantages :**
- Représentation graphique intuitive et universelle
- Indépendant de la technologie d'implémentation
- Adapté aux systèmes complexes par hiérarchisation
- Communication efficace entre concepteurs et opérateurs
- Base de la programmation SFC sur automates

**Niveaux de GRAFCET :**
- **Niveau 1** : Spécifications fonctionnelles (indépendant technologie)
- **Niveau 2** : Spécifications technologiques (capteurs/actionneurs réels)
- **Niveau 3** : Implémentation (programme automate)

#### Éléments constitutifs du GRAFCET

**1. Étapes**

Symbole : Rectangle numéroté

- **Étape** : Situation dans laquelle le comportement du système est invariant
- **Étape initiale** : Double rectangle (état au démarrage)
- **Étape active** : Étape en cours d'exécution (représentée par un jeton •)

*Règle :* À tout instant, au moins une étape est active.

**2. Actions associées aux étapes**

Les actions décrivent ce que fait le système lorsqu'une étape est active.

**Types d'actions :**

*Action continue (N - Normal) :*
```
[Étape 10]  Activer moteur M1
```
L'action est exécutée tant que l'étape est active.

*Action conditionnelle (C - Conditional) :*
```
[Étape 10]  SI température > 50°C ALORS activer ventilateur
```
Action exécutée seulement si condition vraie ET étape active.

*Action mémorisée (S/R - Set/Reset) :*
```
[Étape 5]   S: Allumer voyant    (Set - mémorisation)
[Étape 12]  R: Éteindre voyant   (Reset - annulation)
```
L'action reste active même après désactivation de l'étape, jusqu'à un ordre de reset.

*Actions temporisées :*
- **D (Delayed)** : Action retardée
  ```
  [Étape 8]  D: 5s / Activer alarme
  ```
  L'action démarre 5 secondes après l'activation de l'étape.

- **L (Limited)** : Action limitée dans le temps
  ```
  [Étape 8]  L: 3s / Activer sirène
  ```
  L'action dure 3 secondes maximum.

- **P (Pulse)** : Impulsion
  ```
  [Étape 8]  P: 0.5s / Pulse sortie
  ```
  Impulsion de durée fixe au début de l'étape.

**3. Transitions et réceptivités**

Symbole : Trait horizontal traversant une liaison

**Transition :** Possibilité d'évolution entre étapes.

**Réceptivité :** Condition associée à une transition (expression booléenne).
- Variables logiques : capteurs, boutons, temporisations
- Opérateurs : ET (·), OU (+), NON (/)
- Événements : fronts montants (↑), fronts descendants (↓)

*Exemples :*
- `a` : capteur a activé
- `a · b` : a ET b activés
- `a + /b` : a OU NON b
- `a↑` : front montant de a
- `t/5s/10` : temporisation 5s depuis activation étape 10

**Règles d'évolution :**

1. **Franchissement de transition :**
   Une transition est franchie si et seulement si :
   - L'étape immédiatement précédente est active **ET**
   - La réceptivité associée est vraie

2. **Évolution :**
   Lors du franchissement :
   - Désactivation des étapes amont
   - Activation des étapes aval
   - Toutes les évolutions sont simultanées

**4. Liaisons orientées**

- Traits reliant étapes et transitions
- Orientation implicite (haut → bas) sauf indication contraire
- Jamais de liaison directe étape-étape ou transition-transition

#### Structures de base du GRAFCET

**1. Séquence unique (linéaire)**

```
[Étape 0] (initiale)
    ↓  [condition a]
[Étape 1]  Action A
    ↓  [condition b]
[Étape 2]  Action B
    ↓  [fin]
[Étape 0]
```

Enchaînement séquentiel d'étapes et actions.

**2. Sélection de séquence (divergence/convergence en OU)**

```
        [Étape 5]
         /     \
    [choix 1] [choix 2]
       /           \
[Étape 6]         [Étape 7]
 Action A          Action B
       \           /
        [commun]
         \   /
        [Étape 8]
```

**Divergence en OU :**
- Une seule branche activée parmi plusieurs
- Dépend de la réceptivité vraie
- Priorité si plusieurs conditions vraies (dépend implémentation)

**Convergence en OU :**
- Toutes les branches mènent à la même étape suivante

*Exclusion mutuelle :* Veiller à ce que les conditions soient exclusives pour éviter conflits.

**3. Parallélisme (divergence/convergence en ET)**

```
         [Étape 10]
      ===================  [démarrage]
      ‖                 ‖
  [Étape 11]       [Étape 12]
   Action A         Action B
      ‖                 ‖
      ===================  [fin A · fin B]
         [Étape 13]
```

**Divergence en ET (synchronisation) :**
- Symbole : double trait horizontal
- Activation simultanée de toutes les branches
- Permet actions parallèles

**Convergence en ET :**
- Attend que toutes les branches soient terminées
- Synchronisation : transition franchie uniquement si toutes les étapes amont actives ET réceptivité vraie

*Applications :* Machines multi-postes, convoyeurs multiples, robots multi-axes.

#### GRAFCET hiérarchisé et structuré

**1. Macro-étapes**

Encapsulation d'un sous-GRAFCET complexe dans une seule étape.

Symbole : Rectangle avec deux traits verticaux

```
[Étape 20]
     ↓
[M - Macro traitement]  ← Contient un sous-GRAFCET
     ↓
[Étape 30]
```

*Avantages :*
- Simplification lecture graphe principal
- Modularité et réutilisabilité
- Expansion/compression par niveaux

*Règles :*
- Une macro-étape possède une étape d'entrée (E) et une ou plusieurs étapes de sortie (S)
- Activation de la macro → activation étape d'entrée
- Sortie de la macro → désactivation complète du sous-GRAFCET

**2. Forçage et figeage**

**Forçage (forcing) :**

Ordre externe modifiant l'état du GRAFCET.

Symbole : Double flèche

```
[Étape sécurité] --{X10}→→ Forçage de l'étape 10
```

*Action :*
- Désactivation de toutes les étapes actives
- Activation forcée de l'étape spécifiée
- Utilisé pour modes dégradés, arrêts d'urgence

*Syntaxe :*
- `{X10}` : forcer étape 10
- `{X0}` : forcer étape initiale (réinitialisation)
- `{}` : forcer situation vide (arrêt total)

**Figeage (freezing) :**
Gel temporaire de l'évolution du GRAFCET (étapes actives restent actives, pas de franchissement).

**3. GRAFCET de conduite et de sécurité**

Architecture hiérarchique avec plusieurs niveaux :
- **GRAFCET de sécurité** : Prioritaire, gère arrêts d'urgence
- **GRAFCET de conduite** : Gère modes (auto, manuel, maintenance)
- **GRAFCET de production** : Séquence normale

### Module 2 : Automates Programmables Industriels (API)

#### Architecture matérielle des automates

**Structure générale :**

```
[Alimentation] → [CPU] ←→ [Mémoire] ←→ [Bus] ←→ [Modules I/O]
                    ↕                      ↕
              [Communication]        [Interfaces]
```

**1. Unité Centrale (CPU)**

- **Processeur** : Exécution du programme cyclique
- **Cycle automate typique :**
  1. Lecture des entrées (image mémoire)
  2. Exécution du programme utilisateur
  3. Écriture des sorties
  4. Traitement communication et diagnostic
  5. Watchdog (surveillance)

- **Temps de cycle** : 1-50 ms typiquement (dépend taille programme)

**2. Mémoires**

**RAM (Random Access Memory) :**
- Variables, données de travail
- Image des entrées/sorties
- Volatile (perdue à la coupure)
- Batterie de sauvegarde optionnelle

**EEPROM / Flash :**
- Programme utilisateur
- Paramètres configuration
- Non volatile
- Durée de vie limitée en écriture

**ROM :**
- Système d'exploitation
- Firmware automate

**3. Modules d'entrées/sorties**

**Entrées TOR (Tout Ou Rien) :**
- Tension nominale : 24V DC, 230V AC
- Isolation galvanique (optocoupleurs)
- Filtrage anti-rebond
- Protection surten sions
- Indicateurs LED état
- Temps de réponse : 1-10 ms

*Types de capteurs connectés :*
- Détecteurs inductifs (métaux)
- Détecteurs capacitifs (tous matériaux)
- Cellules photoélectriques (présence)
- Fins de course mécaniques
- Boutons, commutateurs

**Sorties TOR :**

*Sorties à relais :*
- Isolation galvanique complète
- AC ou DC indifféremment
- Courant élevé (2A typique)
- Commutation lente (10-20 ms)
- Durée de vie limitée (cycles)

*Sorties à transistor :*
- Commutation rapide (< 1 ms)
- DC uniquement
- Courant limité (0.5-1A)
- Durée de vie élevée
- Protection court-circuit

*Sorties à triac :*
- AC uniquement
- Commutation au passage par zéro
- Pas de rebond
- Adapté charges résistives

**Entrées/Sorties analogiques :**
- Tension : ±10V, 0-10V
- Courant : 0-20mA, 4-20mA (standard industriel)
- Résolution : 12-16 bits typique
- Conversion A/N, N/A
- Capteurs : température, pression, débit, niveau

**Modules spécialisés :**
- Comptage rapide (encodeurs)
- PWM (contrôle moteurs)
- Régulation PID
- Positionnement (axes)
- Pesage

**4. Communication**

**Bus de terrain :**
- **Modbus** : Standard ouvert, RS485 ou TCP/IP
- **Profibus** : Siemens, haute performance
- **CANopen** : Automobile, temps réel
- **DeviceNet** : Rockwell
- **EtherCAT** : Temps réel déterministe

**Ethernet industriel :**
- Profinet, EtherNet/IP, Modbus TCP
- Supervision SCADA
- Interconnexion automates
- Accès distant

**Sans fil :**
- WiFi industriel
- Bluetooth
- LoRa pour IoT
- 4G/5G

#### Langages de programmation IEC 61131-3

**1. Ladder Diagram (LD) - Schéma à contacts**

Représentation graphique inspirée des schémas électriques à relais.

*Exemple équation logique : `Q = (A · B) + C`*

```
|--|A|--|B|------------(Q)|
|                         |
|--|C|-------------------|
```

*Éléments :*
- Contact NO (Normally Open) : —| |—
- Contact NF (Normally Closed) : —|/|—
- Bobine : —( )—
- Temporisations, compteurs (blocs)

*Avantages :*
- Intuitif pour électriciens
- Proche des schémas relais
- Largement utilisé en industrie

*Inconvénients :*
- Peu adapté aux calculs complexes
- Difficile pour algorithmes

**2. Function Block Diagram (FBD) - Blocs fonctionnels**

Représentation par blocs interconnectés (portes logiques, fonctions).

```
    A ─┐
        AND ──┐
    B ─┘      │
              OR ── Q
    C ────────┘
```

*Applications :*
- Régulation (PID)
- Traitement analogique
- Logique combinatoire

**3. Sequential Function Chart (SFC) - GRAFCET**

Implémentation directe du GRAFCET normalisé.

*Structure :*
- Étapes et transitions
- Actions associées
- Qualificateurs d'actions (N, S, R, L, D, P)

*Avantage :* Transposition directe du GRAFCET de conception.

**4. Structured Text (ST) - Texte structuré**

Langage de haut niveau proche du Pascal.

```pascal
IF temperature > 50.0 THEN
    ventilateur := TRUE;
    alarme := TRUE;
ELSIF temperature < 45.0 THEN
    ventilateur := FALSE;
    alarme := FALSE;
END_IF;

FOR i := 1 TO 10 DO
    resultat := resultat + valeur[i];
END_FOR;
```

*Avantages :*
- Calculs complexes
- Boucles, conditions
- Lisible et maintenable

**5. Instruction List (IL) - Liste d'instructions**

Langage assembleur de l'automate (peu utilisé aujourd'hui).

```
LD    A
AND   B
OR    C
ST    Q
```

#### Types de données et variables

**Types de base :**
- `BOOL` : Booléen (TRUE/FALSE)
- `INT` : Entier 16 bits (-32768 à 32767)
- `DINT` : Entier 32 bits
- `REAL` : Flottant 32 bits
- `TIME` : Durée (T#5s, T#1m30s)
- `STRING` : Chaîne de caractères

**Classes de variables :**
- `%I` : Entrées (Input)
- `%Q` : Sorties (Output)
- `%M` : Mémoires internes (Memory)
- `%T` : Temporisations (Timer)
- `%C` : Compteurs (Counter)

**Temporisations normalisées :**

*TON (Timer On-Delay) :*
```
    IN ─┤TON├─ Q
    PT ─┤   ├─ ET
```
Sortie Q passe à TRUE après durée PT si IN reste TRUE.

*TOF (Timer Off-Delay) :*
Sortie Q reste TRUE pendant PT après front descendant de IN.

*TP (Timer Pulse) :*
Impulsion de durée PT sur Q au front montant de IN.

**Compteurs :**

*CTU (Count Up) :*
Compte les fronts montants jusqu'à PV.

*CTD (Count Down) :*
Décompte depuis valeur initiale.

*CTUD (Count Up-Down) :*
Compteur/décompteur bidirectionnel.

### Module 3 : Capteurs et actionneurs industriels

#### Capteurs TOR (Tout Ou Rien)

**1. Détecteurs inductifs**

- **Principe** : Variation champ magnétique
- **Cibles** : Métaux uniquement
- **Portée** : 0.5-60 mm typique
- **Avantages** : Sans contact, robuste, fiable
- **Applications** : Détection pièces métalliques, comptage

*Types :*
- 2 fils (alimenté par charge)
- 3 fils (NPN ou PNP)
- Affleurant / non-affleurant

**2. Détecteurs capacitifs**

- **Principe** : Variation capacité
- **Cibles** : Tous matériaux (métaux, plastiques, liquides)
- **Portée** : 5-40 mm
- **Applications** : Niveau de liquide, détection à travers paroi

**3. Détecteurs photoélectriques**

*Barrage :*
- Émetteur et récepteur séparés
- Longue portée (30m)
- Haute précision

*Reflex :*
- Émetteur et récepteur dans même boîtier
- Réflecteur rétro-réfléchissant
- Portée moyenne (6m)

*Proximité (diffus) :*
- Réflexion sur objet lui-même
- Courte portée (1m)
- Sensibilité réglable

**4. Capteurs magnétiques (ILS - Interrupteurs à Lames Souples)**

- Détection aimants permanents
- Vérins pneumatiques (position piston)
- Très longue durée de vie
- Sensible champs parasites

**5. Fins de course mécaniques**

- Contact physique
- Robustes
- Fiables
- Usure mécanique
- Applications sécuritaires

#### Actionneurs industriels

**1. Contacteurs et relais**

*Contacteur :*
- Fort courant (jusqu'à 100A+)
- Commutation moteurs, charges puissantes
- Bobine 24V DC, 230V AC
- Contacts auxiliaires NO/NF

*Relais interface :*
- Adaptation signaux automate ↔ actionneurs
- Isolation galvanique
- Protection

**2. Électrovannes**

- Commande pneumatique ou hydraulique
- 2/2, 3/2, 5/2, 5/3 voies
- Monostable / bistable
- Commande électrique 24V DC

**3. Vérins pneumatiques**

*Simple effet :*
- Ressort de rappel
- Une chambre

*Double effet :*
- Deux chambres
- Contrôle avancée et retour

*Paramètres :*
- Diamètre (force)
- Course
- Amortisseurs fin de course

**4. Moteurs et variateurs**

*Moteur asynchrone triphasé :*
- Démarrage : direct, étoile-triangle, variateur
- Protection thermique (relais)
- Couple constant

*Variateur de vitesse :*
- Contrôle vitesse et couple
- Économie énergie
- Démarrage progressif
- Communication Modbus, Profibus

### Module 4 : Sécurité des systèmes automatisés

#### Normes de sécurité

**ISO 13849-1 : Sécurité des machines**

**Catégories de sécurité (B, 1, 2, 3, 4) :**
- **Cat B** : Composants fiables
- **Cat 1** : Composants éprouvés
- **Cat 2** : Contrôle périodique
- **Cat 3** : Détection défaut, fonctionnement dégradé
- **Cat 4** : Aucun défaut unique ne doit provoquer perte fonction sécurité

**Performance Level (PL) : a, b, c, d, e**
Plus le niveau est élevé, plus la réduction de risque est importante.

**SIL (Safety Integrity Level) - IEC 61508**

Niveaux 1 à 4 (4 = plus sûr)
- Probabilité de défaillance
- Architecture matérielle et logicielle
- Processus de développement

#### Fonctions de sécurité

**1. Arrêt d'urgence (AU)**

- Catégorie 0 : Arrêt immédiat (coupure alimentation)
- Catégorie 1 : Arrêt contrôlé puis coupure
- Bouton coup de poing (rouge, champignon)
- Non verrouillable
- Action mécanique positive

**2. Protecteurs et interverrouillages**

*Protecteurs fixes :*
- Démontables uniquement par outils

*Protecteurs mobiles :*
- Interrupteur de sécurité (codé ou non)
- Arrêt automatique si ouverture

**3. Barrières immatérielles**

- Rideaux lumineux
- Arrêt machine si faisceau coupé
- Muting (désactivation temporaire contrôlée)

**4. Relais de sécurité**

Modules de sécurité certifiés surveillant circuits de sécurité (AU, interverrouillages).

**5. Automates de sécurité**

API dédiés aux fonctions de sécurité (Safety PLC) :
- Siemens S7 F
- Schneider Modicon Safety
- Rockwell GuardLogix

#### Modes de marche

**Mode automatique :**
- Fonctionnement normal en cycle
- Portes fermées, protections actives

**Mode manuel (mode pas à pas) :**
- Validation opérateur à chaque étape
- Formation, mise au point

**Mode maintenance :**
- Protections désactivables (avec clé)
- Vitesses réduites
- Personnel habilité uniquement

---

## PART C: ASPECTS TECHNIQUES

### Environnements de développement

#### Logiciels industriels professionnels

**1. Schneider Electric**

*Unity Pro (legacy) :*
- Automates Modicon M340, Premium
- Langages : Ladder, ST, SFC, FBD
- Simulation intégrée

*EcoStruxure Machine Expert (nouveau) :*
- Modicon M2x1, M262
- Conforme IEC 61131-3
- Basé sur CODESYS

**2. Siemens - TIA Portal (Totally Integrated Automation)**

*Environnement unifié :*
- STEP 7 (programmation API)
- WinCC (supervision)
- Startdrive (variateurs)
- Safety (sécurité intégrée)

*Automates supportés :*
- S7-1200 (compact)
- S7-1500 (haute performance)
- S7-300/400 (legacy)

*Fonctionnalités :*
- Programmation graphique et textuelle
- Simulation PLCSIM
- Diagnostic en ligne
- Gestion de versions

**3. Rockwell Automation - Studio 5000**

*Logix Designer :*
- ControlLogix, CompactLogix
- Langage propriétaire + ST
- Add-On Instructions (AOI)

**4. CODESYS (Controller Development System)**

*Standard ouvert :*
- IEC 61131-3 pur
- Multi-fabricants
- Version gratuite (simulation)
- Utilisé par 400+ fabricants

*Avantages :*
- Portabilité code
- Vaste écosystème
- Support IoT / Industry 4.0

#### Outils de simulation

**Factory I/O**

Simulateur 3D de systèmes industriels :
- Environnements préfabriqués (tri, assemblage, palettisation)
- Connexion avec automates réels (Modbus, S7)
- Éditeur de scènes
- Capteurs et actionneurs virtuels

*Utilisation pédagogique :*
- Tests sans matériel physique
- Visualisation 3D du comportement
- Scénarios complexes
- Sécurité (pas de casse matériel)

**LogixPro (Rockwell)**
- Simulation Ladder pour Allen-Bradley
- Maquettes virtuelles (ascenseur, feux)

**PLCSim / PLCSim Advanced (Siemens)**
- Simulation S7-1200/1500
- API virtuels
- Tests hors ligne

### Projets pratiques réalisés

#### Projet 1 : Mini-Projet Ascenseur (Contrôle AP16)

**Cahier des charges :**
- Ascenseur 4 étages (0, 1, 2, 3)
- Cabine avec boutons destination
- Boutons d'appel à chaque étage (montée/descente)
- Gestion priorités : appels en cours de trajet
- Sécurités : portes, surcharge

**Capteurs :**
- 4 capteurs de position (étages)
- 4 capteurs portes ouvertes
- Capteur surcharge cabine
- Boutons cabine (4) + étages (6)

**Actionneurs :**
- Moteur montée/descente
- Électrovanne ouverture portes
- Voyants étages

**GRAFCET hiérarchisé :**

*GRAFCET principal :*
- Attente appels
- Sélection direction (montée/descente)
- Déplacement étage par étage
- Arrêt aux étages demandés

*Macro-étapes :*
- Ouverture porte (temporisation)
- Fermeture porte
- Déplacement inter-étages

*Modes :*
- Normal
- Maintenance (commande manuelle)
- Défaut (arrêt sécurité)

**Implémentation :**
- Programmation Unity Pro (SFC + Ladder)
- Simulation sous Factory I/O ou maquette physique
- Tests de scénarios (appels multiples, surcharge)

**Livrables :**
- GRAFCET niveau 1 et 2
- Programme automate complet
- Rapport de tests
- Vidéo de démonstration

#### Projet 2 : TP Passage à niveau

**Système automatisé :**
- Détection trains (boucles magnétiques)
- Commande barrières (moteurs + fins de course)
- Feux de signalisation (rouge/vert)
- Sirène d'alerte

**Séquence normale :**
1. Train détecté zone approche
2. Déclenchement sirène (5s)
3. Feu rouge + descente barrières
4. Train passe
5. Train quitté zone
6. Attente temporisation sécurité (2s)
7. Montée barrières + feu vert

**Sécurités :**
- Barrières fermées avant passage train
- Temporisation anti-rebond détecteurs
- Défaut barrière → arrêt système + alarme

**Programmation :**
Choix entre SFC (séquence) ou Ladder (gestion détecteurs).

#### Projet 3 : TP Château d'eau

**Régulation de niveau :**
- 3 pompes (P1, P2, P3)
- 3 capteurs niveau (bas B, moyen M, haut H)
- Gestion optimisée (rotation pompes, usure)

**Logique de commande :**
- Niveau < B : démarrage P1 + P2
- B < Niveau < M : P1 seule
- Niveau > H : arrêt toutes pompes
- Rotation : alterner pompe principale

**Défauts :**
- Timeout démarrage pompe
- Niveau anormal (fuite)
- Alarmes et commutation pompe de secours

#### Projet 4 : Station de tri (projet de synthèse)

**Système complexe multi-postes :**

*Description :*
Tri de pièces selon caractéristiques (couleur, matière, hauteur) sur convoyeur.

*Architecture :*
- Convoyeur principal motorisé
- Poste de chargement (vibration)
- Postes de détection (capteurs optiques, inductifs, hauteur)
- Éjecteurs pneumatiques (vérins)
- Bacs de récupération (3 catégories + rebut)
- Compteurs par catégorie

*GRAFCET hiérarchisé avec parallélisme :*
- Branche 1 : Gestion convoyeur
- Branche 2 : Poste détection couleur
- Branche 3 : Poste détection matière
- Branche 4 : Poste éjection

*Synchronisation :*
Pièce identifiée → mémorisation type → éjection au bon poste

*IHM (Interface Homme-Machine) :*
- Écran tactile ou pupitre
- Affichage compteurs
- Statistiques production
- Réglages (vitesse, seuils)
- Gestion modes (auto, manuel, maintenance)

*Programmation avancée :*
- Structures de données (tableaux de pièces)
- Blocs fonctionnels réutilisables
- Communication Modbus (IHM ↔ automate)

**Livrables attendus :**
- Dossier d'analyse fonctionnelle
- GRAFCET complet hiérarchisé
- Programme automate (SFC + ST pour algorithmes)
- Schémas électriques
- IHM configurée
- Documentation technique complète
- Démonstration système

#### Projet 5 : Feux de carrefour

**Intersection 2 voies avec priorité :**

*Capteurs :*
- Boucles de détection véhicules
- Boutons piétons (2)

*Actionneurs :*
- 6 feux tricolores (R, O, V) × 2 voies
- 2 feux piétons

*Séquence normale :**
Voie prioritaire verte par défaut, changement sur détection voie secondaire.

*Temps de sécurité :*
- Transition vert → orange : 3s
- Orange seul : 3s
- Tout rouge : 2s (sécurité)

*Mode dégradé :*
- Défaut capteur : orange clignotant
- Maintenance : forçage étape

### Câblage et mise en service

#### Schémas électriques

**Plan de câblage :**
- Alimentation 24V DC
- Entrées : capteurs 2 ou 3 fils
- Sorties : actionneurs (préactionneurs)
- Masse commune, blindages
- Protection (fusibles, disjoncteurs)

**Borniers :**
- Repérage normalisé
- Continuité terre
- Séparation puissance/commande

#### Mise en service

**Étapes :**
1. Vérification câblage (continuité, isolation)
2. Mise sous tension progressive
3. Test entrées/sorties (table d'animation)
4. Chargement et lancement programme
5. Tests unitaires par séquence
6. Tests intégration
7. Réglages fins (temporisations)
8. Validation complète
9. Documentation as-built

**Outils de diagnostic :**
- Voyants état CPU
- Visualisation variables en ligne
- Forçage entrées/sorties
- Trace d'exécution
- Moniteur GRAFCET (étapes actives)

---

## PART D: ANALYSE ET RÉFLEXION

### Évaluation des compétences

#### Contrôle continu (15%)

**QCM et exercices courts (Semaine 7) :**
- GRAFCET : lecture, complétion
- Langages automates
- Capteurs/actionneurs
- Normes sécurité

**Compétences :**
- Connaissance théorique
- Compréhension des concepts
- Application sur cas simples

#### Travaux pratiques (40%)

**Évaluation continue :**
- Préparation séances (5%) : étude préalable, GRAFCET préparatoire
- Manipulation (20%) : autonomie, démarche, tests
- Comptes-rendus (15%) : qualité technique, analyse

**Critères :**
- Rigueur méthodologique
- Compréhension du système
- Qualité GRAFCET et programmes
- Analyse critique des résultats
- Respect consignes sécurité

#### Mini-projets (30%)

**Projet ascenseur ou station de tri :**
- En binôme
- Durée : 3-4 séances

**Livrables :**
- Dossier technique (analyse + GRAFCET + programme)
- Démonstration fonctionnelle
- Présentation orale (10 min)

**Grille d'évaluation :**
- Analyse fonctionnelle (15%)
- GRAFCET niveau 1 et 2 (25%)
- Programme automate (30%)
- Tests et validation (20%)
- Documentation et présentation (10%)

#### Examen final (15%)

**Format (2h) :**
- Analyse de système industriel
- Conception GRAFCET
- Programmation Ladder/ST
- Questions de cours

**Sujets types :**
- Convoyeur tri de colis
- Poste de remplissage/bouchage
- Portail automatique
- Chaîne d'assemblage

### Liens interdisciplinaires

#### Avec Automatique (S3)
- **Complémentarité** : Séquentiel (automatisme) vs Continu (automatique)
- **Intégration** : Régulation (PID sur automate) dans séquence
- **Exemple** : Régulation température dans cycle de production

#### Avec Informatique Embarquée (S3)
- **Communication** : Automate ↔ microcontrôleur (Modbus, CANopen)
- **Architecture** : API comme système embarqué temps réel
- **Projet** : Puzzle/Taquin sur STM32 avec logique séquentielle

#### Avec Électronique Numérique (S3)
- **Architecture** : Logique câblée vs programmée
- **FPGA vs automate** : Choix technologique selon application
- **Conception** : Platine avec CPLD pour fonctions simples

#### Avec Énergie (S3)
- **Actionneurs** : Moteurs, variateurs commandés par automate
- **Gestion énergie** : Optimisation cycles (rotation pompes)
- **Sécurité** : Coordination électrotechnique + automatisme

### Applications industrielles par secteur

#### Industrie manufacturière (70% des applications)

**Automobile :**
- Lignes d'assemblage (robots, convoyeurs)
- Soudure automatisée (séquençage points)
- Peinture (cabines automatiques)
- Contrôle qualité (vision + rejet pièces)

**Agroalimentaire :**
- Embouteillage/conditionnement (cadences élevées)
- Process de transformation (cuisson, mélange)
- Traçabilité (étiquetage, HACCP)
- Nettoyage automatique (NEP - Nettoyage En Place)

**Pharmaceutique :**
- Dosage précis (pesée automatique)
- Conditionnement stérile (salles blanches)
- Traçabilité complète (batch records)
- Validation FDA (programmes certifiés)

#### Énergie et utilities

**Traitement de l'eau :**
- Stations de pompage (régulation niveau/débit)
- Traitement automatisé (dosage réactifs)
- Supervision SCADA
- Télégestion

**Distribution électrique :**
- Postes HTA/BT automatisés
- Délestage/relestage automatique
- Synchronisation réseaux
- Protection sélective

### Compétences professionnelles acquises

#### Compétences techniques

**Conception :**
- Analyse fonctionnelle de systèmes
- Modélisation GRAFCET normalisée
- Choix technologiques (automate, capteurs, actionneurs)
- Architecture de sécurité

**Programmation :**
- Maîtrise langages IEC 61131-3
- Structuration de programmes
- Bibliothèques réutilisables
- Optimisation temps de cycle

**Mise en œuvre :**
- Câblage armoires électriques
- Paramétrage automates
- Mise en service systèmes
- Diagnostic et dépannage

#### Compétences méthodologiques

- Lecture et création de cahiers des charges
- Documentation technique normalisée
- Tests et validation systématiques
- Gestion de projet (planning, ressources)

#### Compétences transversales

- Rigueur et précision (sécurité critique)
- Travail en équipe (projets)
- Communication technique (dossiers, présentations)
- Veille technologique

### Ressources et standards

#### Normes industrielles

- **IEC 60848** : GRAFCET
- **IEC 61131-3** : Langages programmation API
- **ISO 13849** : Sécurité des machines
- **IEC 61508** : Sécurité fonctionnelle (SIL)
- **IEC 62061** : Sécurité systèmes de commande
- **EN 60204-1** : Équipement électrique des machines

#### Documentation technique

**Constructeurs automates :**
- Manuels programmation (Schneider, Siemens)
- Application notes
- Exemples de programmes

**Sites professionnels :**
- Automation.com
- Control Engineering
- PLCopen.org (bibliothèques standards)

### Évolution vers systèmes avancés

#### Industrie 4.0

**IoT industriel (IIoT) :**
- Connectivité automates (MQTT, OPC-UA)
- Edge computing
- Cloud industriel
- Maintenance prédictive

**Supervision et SCADA :**
- WinCC, Wonderware, iFIX
- Collecte données temps réel
- Tableaux de bord (KPI)
- Alarmes centralisées

**MES (Manufacturing Execution System) :**
- Intégration ERP ↔ automates
- Ordres de fabrication
- Traçabilité lot
- Indicateurs production (TRS, OEE)

#### Technologies émergentes

**Automates hybrides :**
- CPU + FPGA (parties critiques)
- Temps réel déterministe
- Vision intégrée

**Programmation haut niveau :**
- Python sur automates (B&R, Beckhoff)
- Machine learning embarqué
- Algorithmes complexes

---

## 📖 SYNTHÈSE

L'automatisme industriel est une discipline centrale du DUT GEII, formant aux technologies qui font fonctionner l'industrie moderne. Ce cours S3 établit les fondations solides nécessaires à tout technicien ou ingénieur intervenant sur systèmes automatisés.

**Acquis essentiels :**
- Le GRAFCET comme langage universel de spécification
- La programmation d'automates selon standards internationaux
- L'intégration sécuritaire de capteurs et actionneurs
- La méthodologie de conception de systèmes séquentiels

**Perspectives :**
Les compétences acquises sont directement valorisables en industrie, l'automatisme représentant un marché d'emploi dynamique avec forte demande de profils qualifiés. Les projets réalisés constituent un portfolio technique démontrant capacités d'analyse, de conception et de réalisation.

---

## Documents de Cours

<div class="pdf-container">
  <div class="pdf-viewer">

    <div class="pdf-item">
      <h4>Introduction a l'Automatisme</h4>
      <p>Presentation generale du cours : contexte industriel, objectifs et organisation.</p>
      <embed src="/cours-pdf/S3/Automatisme/A_-_1_-_Introduction.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S3/Automatisme/A_-_1_-_Introduction.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Machines a Etats</h4>
      <p>Modelisation par machines a etats finis : etats, transitions, sorties.</p>
      <embed src="/cours-pdf/S3/Automatisme/B_-_4_-_Machines_à_états.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S3/Automatisme/B_-_4_-_Machines_à_états.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Grafcet</h4>
      <p>Modelisation par Grafcet : etapes, transitions, divergences et convergences.</p>
      <embed src="/cours-pdf/S3/Automatisme/B_-_5_-_Grafcet.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S3/Automatisme/B_-_5_-_Grafcet.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Automates Programmables Industriels (API)</h4>
      <p>Architecture et fonctionnement des API : entrees/sorties, cycle automate, programmation.</p>
      <embed src="/cours-pdf/S3/Automatisme/D_-_7_-_API_(1).pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S3/Automatisme/D_-_7_-_API_(1).pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Norme CEI 61131</h4>
      <p>La norme internationale de programmation des automates : langages normalises et bonnes pratiques.</p>
      <embed src="/cours-pdf/S3/Automatisme/D_-_8_-_La_norme_CEI_61131_(1).pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S3/Automatisme/D_-_8_-_La_norme_CEI_61131_(1).pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Le Langage Ladder Diagrams</h4>
      <p>Programmation en langage Ladder : contacts, bobines, temporisateurs et compteurs.</p>
      <embed src="/cours-pdf/S3/Automatisme/D_-_9_-_Le_langage_Ladder_Diagrams.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S3/Automatisme/D_-_9_-_Le_langage_Ladder_Diagrams.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

  </div>
</div>

---

<style>body{font-family:Arial,sans-serif;background-color:#f4f4f9;color:#333;line-height:1.6}h2,h3,h4,h5{color:#2a7ae2}p{text-align:justify}code{background-color:#f5f5f5;padding:2px 6px;border-radius:3px;font-family:'Courier New',monospace}pre{background-color:#f5f5f5;padding:15px;border-radius:5px;overflow-x:auto}</style>

<div class="back-nav">
  <a href="./my-courses-2021-2022.html">&larr; Retour a Mes Cours 2021-2022</a>
</div>



---
layout: default
title: "Électronique et Réalisation (ER) - S1"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
---

# Électronique et Réalisation (ER) - Semestre 1

## PART A - Présentation Générale du Cours

### Contexte de la formation
Le module Électronique et Réalisation (ER) constitue le cœur pratique de la formation GEII. Il combine théorie électronique et réalisation concrète de circuits, permettant aux étudiants de comprendre le fonctionnement des composants électroniques et de les mettre en œuvre dans des projets réels. L'utilisation intensive du logiciel Proteus ISIS prépare les étudiants à la conception assistée par ordinateur utilisée en entreprise.

### Positionnement dans le cursus
- **Semestre** : S1 (1ère année DUT GEII)
- **Volume horaire** : 70h (30h CM + 20h TD + 20h TP + Projets)
- **Crédits ECTS** : 6
- **Prérequis** : Bases en électricité (niveau Terminale), mathématiques (nombres complexes)
- **Continuité** : ER S2 (Microcontrôleurs, Interface, FPGA), puis Systèmes Électroniques S3-S4

### Public visé
Étudiants de première année découvrant l'électronique analogique avec une approche pratique et orientée projet. Le cours s'adresse aussi bien aux débutants qu'à ceux ayant suivi une spécialité scientifique au lycée.

---

## PART B: EXPÉRIENCE, CONTEXTE ET FONCTION

### Objectifs pédagogiques

**Compétences en composants électroniques :**
- Identifier et caractériser les composants passifs (R, L, C) et actifs (diodes, transistors, AOP)
- Comprendre le fonctionnement physique et les modèles équivalents
- Choisir les composants selon les spécifications d'un cahier des charges
- Lire et interpréter une datasheet (fiche technique)

**Compétences en conception :**
- Concevoir des circuits analogiques simples
- Simuler et valider un circuit avant réalisation
- Dimensionner les composants
- Optimiser un circuit selon des contraintes

**Compétences pratiques :**
- Utiliser Proteus ISIS pour la simulation
- Réaliser des montages sur breadboard
- Mesurer et valider expérimentalement
- Déboguer et dépanner des circuits

### Programme détaillé

#### 1. Composants passifs (10h)

**Résistances (R) :**

**Caractéristiques :**
- Loi d'Ohm : V = R × I
- Puissance dissipée : P = R × I² = V²/R
- Technologie : couche carbone, métalliques, bobinées
- Code couleur (4 ou 5 anneaux)
- Valeurs normalisées (série E12, E24)

**Associations :**
- Série : R_eq = R₁ + R₂ + ... + Rn
- Parallèle : 1/R_eq = 1/R₁ + 1/R₂ + ... + 1/Rn
- Diviseur de tension : V_out = V_in × R₂/(R₁+R₂)

**Condensateurs (C) :**

**Principe physique :**
- Stockage d'énergie électrique (champ électrique)
- Relation : Q = C × V
- Courant : I = C × dV/dt
- Impédance complexe : Z_C = 1/(jCω) = -j/(Cω)

**Technologies :**
- **Électrolytiques** : Forte capacité (µF à mF), polarisés, ESR élevée
- **Céramiques** : Moyennes valeurs (pF à µF), non polarisés, rapides
- **Films** : Précision, stabilité, audio

**Applications :**
- Filtrage d'alimentation (découplage)
- Couplage/découplage AC
- Filtres RC (passe-bas, passe-haut)
- Temporisation
- Stockage d'énergie

**Charge/décharge :**
- Charge : V_C(t) = V_max × (1 - e^(-t/τ)) avec τ = RC
- Décharge : V_C(t) = V_max × e^(-t/τ)

**Inductances (L) :**

**Principe physique :**
- Stockage d'énergie magnétique
- Tension : V = L × dI/dt
- Impédance complexe : Z_L = jLω

**Applications :**
- Filtrage (bobines de choc)
- Transformateurs
- Moteurs et relais
- Filtres LC

**Impédances complexes (synthèse) :**

En régime sinusoïdal (AC), utilisation de la notation complexe :
- Résistance : Z̄_R = R (en phase)
- Inductance : Z̄_L = jLω (courant en retard de 90°)
- Condensateur : Z̄_C = -j/(Cω) (courant en avance de 90°)

#### 2. Diodes et applications (12h)

**Diode à jonction PN :**

**Principe de fonctionnement :**
- Jonction P-N de semi-conducteur (Si ou Ge)
- Conduction unidirectionnelle
- Polarisation directe : I = I_s × (e^(V/nV_T) - 1)
- Polarisation inverse : blocage (courant de fuite négligeable)

**Caractéristiques :**
- Tension de seuil : V_F ≈ 0.7V (Si), 0.3V (Ge), 0.2V (Schottky)
- Courant maximal (I_F max)
- Tension inverse max (V_R max ou PIV)
- Temps de commutation (diodes rapides)

**Modèles équivalents :**
- **Modèle idéal** : Interrupteur parfait (V_F = 0)
- **Modèle simplifié** : Source de tension V_F + résistance r_d
- **Modèle complet** : Exponentiel (équation de Shockley)

**Applications pratiques :**

**1. Redressement :**
- **Redresseur simple alternance** : Conversion AC → DC pulsé
- **Redresseur double alternance (pont de Graetz)** : 4 diodes, meilleur rendement
- Filtrage par condensateur : V_ripple ≈ I_load / (f × C)

**2. Écrêtage :**
- Limitation d'amplitude d'un signal
- Protection contre les surtensions
- Mise en forme de signaux

**3. Roue libre (free-wheeling) :**
- Protection contre les surtensions inductives
- Circuit avec relais, moteurs, électrovannes

**4. Diodes spéciales :**
- **Diode Zener** : Régulation de tension (tension de claquage contrôlée)
- **LED** : Émission lumineuse (V_F ≈ 1.8V à 3.3V selon couleur)
- **Diode Schottky** : Faible chute de tension, rapide (alimentation à découpage)
- **Photodiode** : Conversion lumière → courant

#### 3. Transistors bipolaires (BJT) (15h)

**Structure et fonctionnement :**

**Types :**
- **NPN** : Collecteur (+), Base (commande), Émetteur (référence)
- **PNP** : Collecteur (-), Base (commande), Émetteur (référence)

**Principe :**
- 3 régions : Émetteur (E), Base (B), Collecteur (C)
- Contrôle du courant I_C par le courant I_B
- Gain en courant : β = I_C / I_B (typiquement 100-300)

**Modes de fonctionnement :**
- **Bloqué** : V_BE < V_seuil, transistor ouvert (I_C ≈ 0)
- **Actif (linéaire)** : V_BE ≥ 0.7V, I_C = β × I_B, amplification
- **Saturé** : V_BE ≥ 0.7V, I_C limité par charge, interrupteur fermé

**Applications :**

**1. Interrupteur électronique :**
```
        +Vcc
         |
        [R_C]  (charge)
         |
     C──┴──
      NPN
      ───
       |
   [R_B]
       |
    Signal
```

Dimensionnement :
- I_B = (V_in - V_BE) / R_B
- I_C (saturé) = (V_cc - V_CE(sat)) / R_C
- Vérifier : β × I_B > I_C (saturation assurée)

**2. Amplificateur petit signal :**
- Montage émetteur commun
- Gain en tension : A_v ≈ -R_C / R_E
- Polarisation par pont de base

**3. Commande de relais/LED/moteur :**
- Transistor en commutation
- Protection diode de roue libre

#### 4. Amplificateurs opérationnels (AOP) (20h)

**Caractéristiques de l'AOP idéal :**
- Gain en tension infini : A_v → ∞
- Impédance d'entrée infinie : Z_in → ∞
- Impédance de sortie nulle : Z_out = 0
- Bande passante infinie
- Pas de courant d'entrée : I⁺ = I⁻ = 0
- **Règle d'or** : En boucle fermée, V⁺ = V⁻

**Montages fondamentaux :**

**1. Suiveur (Buffer) :**
- Gain : A_v = 1
- Impédance d'entrée très élevée
- Adaptation d'impédance

**2. Amplificateur inverseur :**
```
    R2
   ┌───┐
   │   │
R1 │   v
───┤-  │
   │+  ├─── V_out
───┤   │
   └───┘
```
- Gain : A_v = -R2/R1
- Z_in = R1

**3. Amplificateur non-inverseur :**
- Gain : A_v = 1 + R2/R1
- Z_in très élevée

**4. Sommateur inverseur :**
- V_out = -(R_f/R1 × V1 + R_f/R2 × V2 + ...)
- Mixer audio, DAC

**5. Intégrateur :**
- V_out = -(1/RC) ∫ V_in dt
- Génération de rampes, filtres

**6. Dérivateur :**
- V_out = -RC × dV_in/dt
- Détection de fronts

**7. Comparateur :**
- V_out = +V_sat si V⁺ > V⁻, sinon -V_sat
- Détection de seuil

**8. Trigger de Schmitt :**
- Comparateur avec hystérésis
- Antirebond, mise en forme de signaux

**AOP réels utilisés :**
- TL081/TL084 : JFET, faible courant d'entrée
- LM741 : Classique, universel
- LM358 : Dual, alimentation simple
- OPA27 : Bas bruit, précision

### Projets pratiques

#### Projet Radar 2020

**Objectif :** Concevoir un système de détection et mesure de distance par ultrasons

**Spécifications :**
- Émission d'impulsions ultrasoniques (40 kHz)
- Réception et amplification du signal écho
- Mesure du temps de vol
- Calcul et affichage de la distance

**Blocs fonctionnels :**
1. **Émetteur ultrasonique** : Oscillateur 40 kHz + transducteur
2. **Récepteur** : Transducteur + amplification (AOP)
3. **Traitement du signal** : Détection d'enveloppe, comparateur
4. **Logique de mesure** : Microcontrôleur ou circuit numérique
5. **Affichage** : LCD ou LEDs

**Compétences développées :**
- Conception de circuits analogiques
- Amplification de signaux faibles
- Interface analogique/numérique
- Mesure de temps et calcul de distance

#### Dérivateur de fréquence

**Objectif :** Réaliser un circuit dont la sortie est proportionnelle à la dérivée du signal d'entrée

**Principe :**
- Circuit dérivateur à base d'AOP : V_out = -RC × dV_in/dt
- Étude de la réponse fréquentielle
- Compensation et stabilisation

**Analyse :**
- Fonction de transfert : H(jω) = -jRCω
- Gain : |H| = RCω (croissance linéaire avec f)
- Phase : φ = +90° (avance de phase)

**Applications :**
- Détection de fronts
- Calcul de vitesse (dérivée de position)
- Filtres actifs

#### Semaine Projet - Filtrage de son

**Objectif :** Concevoir un système complet de filtrage actif pour isoler des composantes fréquentielles d'un signal audio

**Cahier des charges :**
- Entrée : Signal audio (micro ou line-in)
- Filtres : Passe-bas, passe-bande, passe-haut
- Fréquences de coupure ajustables
- Sortie : Haut-parleur ou line-out

**Réalisation :**
1. **Analyse** : Décomposition fréquentielle du signal
2. **Conception** : Choix topologie (Butterworth, Sallen-Key)
3. **Simulation** : Proteus ISIS, analyse fréquentielle
4. **Dimensionnement** : Calcul des composants
5. **Réalisation** : Montage sur breadboard puis PCB
6. **Tests** : Mesures oscilloscope et analyseur de spectre
7. **Documentation** : Rapport technique complet

**Livrables :**
- Schémas électroniques
- Simulations (diagrammes de Bode)
- Prototype fonctionnel
- Mesures et validation
- Rapport technique

---

## PART C: ASPECTS TECHNIQUES

### Logiciels de simulation

#### Proteus ISIS (Labcenter Electronics)

**Fonctionnalités :**
- Saisie de schémas électroniques
- Bibliothèque exhaustive de composants
- Simulation SPICE (analogique, numérique, mixte)
- Instruments virtuels (oscilloscope, multimètre, GBF)
- Simulation temporelle et fréquentielle
- Analyse DC, AC, transitoire

**Workflow de conception :**

1. **Création de schéma :**
   - Placer les composants (P)
   - Câbler (W pour wire)
   - Nommer les nœuds (L pour label)
   - Définir les valeurs des composants

2. **Instruments virtuels :**
   - Oscilloscope : Visualisation temporelle
   - Voltmètre/Ampèremètre : Mesures DC/AC
   - GBF (générateur) : Signaux d'excitation
   - Analyseur de spectre : Contenu fréquentiel

3. **Simulation :**
   - **Transient Analysis** : Évolution temporelle
   - **AC Sweep** : Réponse fréquentielle (Bode)
   - **DC Sweep** : Caractéristique statique

4. **Exploitation :**
   - Relevé de courbes
   - Mesures (amplitude, phase, fréquence)
   - Export vers rapport

**Exemple : Simulation d'un filtre RC passe-bas**
```
1. Schéma : GBF → R → C → GND
2. Paramètres GBF : Sinus, amplitude 5V, sweep 1Hz-100kHz
3. Oscilloscope : Entrée (GBF) et sortie (nœud RC)
4. AC Analysis : Tracer |H(f)| et Phase(f)
5. Mesure f_c à -3dB : f_c = 1/(2πRC)
```

**Conseils pratiques :**
- Nommer explicitement les nœuds importants
- Utiliser des masses communes
- Vérifier les modèles de composants (parfois idéalisés)
- Sauvegarder régulièrement
- Documenter avec des annotations sur le schéma

#### Alternatives et compléments

**LTspice (Analog Devices) :**
- Gratuit, très performant
- Simulation SPICE pure
- Bibliothèque de composants ADI
- Export SPICE depuis Proteus possible

**Tinkercad Circuits :**
- Simulation en ligne gratuite
- Interface simple et intuitive
- Idéal pour apprentissage
- Limitation : Moins de composants

### Équipements de laboratoire

#### Oscilloscope numérique

**Fonctions principales :**
- **Acquisition** : Échantillonnage du signal (MHz à GHz)
- **Affichage** : Visualisation temporelle
- **Mesures automatiques** : V_pp, V_rms, f, période, duty cycle
- **Déclenchement (trigger)** : Edge, pulse, video
- **Curseurs** : Mesures précises
- **Math** : Opérations (A+B, A-B, FFT)

**Utilisation typique :**
- Réglage base de temps (s/div) et sensibilité (V/div)
- Déclenchement sur le signal
- Mode AC/DC selon l'application
- Mesure déphasage entre 2 signaux (mode XY ou mesure temporelle)

#### Générateur de fonctions (GBF)

**Signaux générés :**
- **Sinusoïdal** : Tests fréquentiels, audio
- **Carré** : Signaux logiques, PWM
- **Triangle/Rampe** : Balayage, intégration
- **Impulsion** : Tests transitoires
- **Bruit** : Tests de robustesse

**Paramètres réglables :**
- Fréquence : mHz à MHz
- Amplitude : mV à V
- Offset DC : Décalage vertical
- Duty cycle : Rapport cyclique (signaux carrés)
- Sweep : Balayage en fréquence

#### Multimètre numérique

**Mesures :**
- Tension DC/AC (V)
- Courant DC/AC (A)
- Résistance (Ω)
- Continuité (beeper)
- Test de diodes (V_F)
- Capacité (certains modèles)
- Fréquence (certains modèles)

**Précision :**
- Classe 0.5% à 3% selon gamme et modèle
- Attention aux calibres (protection fusibles)

### Techniques de montage

#### Breadboard (plaque d'essai)

**Avantages :**
- Montage rapide sans soudure
- Modifications faciles
- Réutilisable

**Inconvénients :**
- Contacts parfois instables
- Capacités parasites (limite HF)
- Pas adapté aux courants élevés

**Bonnes pratiques :**
- Alimentations sur les rails latéraux
- Condensateurs de découplage près des CIs
- Fils courts et organisés
- Code couleur (rouge = +, noir = GND, autres = signaux)

#### Soudure sur PCB

**Étapes :**
1. Étamage du fer (pointe propre et brillante)
2. Placer le composant
3. Chauffer simultanément piste et patte (2-3 sec)
4. Apporter l'étain (fusion sur zone chaude)
5. Retirer étain puis fer
6. Laisser refroidir naturellement

**Soudure réussie :**
- Forme conique brillante
- Piste et patte bien mouillées
- Pas de boule ou pont

---

## PART D: ANALYSE ET RÉFLEXION

### Évaluation des compétences

#### Modalités d'évaluation

**Contrôle continu (35%) :**
- 2 contrôles écrits (15% chacun) : Exercices sur composants, AOP, transistors
- QCM (5%) : Théorie, composants, lecture de schémas

**Travaux pratiques (35%) :**
- 6 TP notés avec comptes-rendus
- Évaluation : Montage, mesures, analyse, documentation

**Projets (20%) :**
- Projet Radar : 7%
- Projet Dérivateur : 6%
- Semaine Projet Filtrage : 7%

**Examen terminal (10%) :**
- Épreuve théorique/pratique (2h)
- Analyse de circuit + dimensionnement

#### Grille d'évaluation TP

| Critère | Barème |
|---------|--------|
| **Montage** : Schéma réalisé correctement, câblage propre | /4 |
| **Mesures** : Utilisation correcte des appareils, relevés précis | /5 |
| **Analyse** : Comparaison théorie/pratique, interprétation | /5 |
| **Simulation** : Proteus fonctionnel, cohérence avec mesures | /3 |
| **Compte-rendu** : Clarté, rigueur, présentation | /3 |
| **Total** | **/20** |

### Compétences acquises

#### Savoirs théoriques

✓ Connaître les composants passifs et actifs
✓ Comprendre les modèles équivalents et limites
✓ Maîtriser les montages à base d'AOP
✓ Analyser des circuits analogiques

#### Savoir-faire techniques

✓ Lire et interpréter un schéma électronique
✓ Simuler un circuit avec Proteus ISIS
✓ Dimensionner des composants selon un cahier des charges
✓ Réaliser des montages sur breadboard
✓ Mesurer avec oscilloscope, multimètre, GBF
✓ Déboguer un circuit (méthode systématique)
✓ Rédiger un compte-rendu technique

#### Savoir-être

✓ Rigueur dans les montages et mesures
✓ Méthode face à un dysfonctionnement
✓ Respect des normes de sécurité
✓ Travail en binôme
✓ Autonomie et curiosité technique

### Progression et débouchés

#### Articulation avec le cursus

| Semestre | Module ER | Contenu |
|----------|-----------|---------|
| **S1** | ER 1 | Composants passifs/actifs, AOP, Proteus |
| **S2** | ER Microcontrôleur | Programmation Arduino, capteurs/actionneurs |
| **S2** | ER Interface | Circuits d'interface (drivers, optocoupleurs) |
| **S2** | ER FPGA | Logique programmable (Quartus, VHDL) |
| **S3-S4** | Systèmes Électroniques | Conception complète de cartes PCB |

#### Métiers et applications

**Métiers utilisant ces compétences :**
- Technicien/Ingénieur en électronique analogique
- Concepteur de cartes électroniques
- Technicien de maintenance électronique
- Testeur/Valideur de systèmes électroniques
- Automaticien (interface capteurs/actionneurs)

**Domaines d'application :**
- Électronique embarquée (automobile, aéronautique)
- Instrumentation de mesure
- Audio/Vidéo professionnel
- Automatismes industriels
- Dispositifs médicaux
- Objets connectés (IoT)

### Conseils de réussite

#### Pendant les cours/TD

- Dessiner les schémas au fur et à mesure
- Comprendre les montages types (à connaître par cœur)
- Refaire les calculs de dimensionnement chez soi

#### En TP

✅ Lire le sujet et préparer les calculs avant la séance
✅ Vérifier le montage avant la mise sous tension
✅ Mesurer méthodiquement (DC avant AC)
✅ Noter immédiatement les mesures dans un tableau
✅ Analyser les écarts théorie/pratique
✅ Rédiger le CR rapidement après le TP

❌ Brancher sans réfléchir
❌ Alimenter sans vérifier les polarités
❌ Oublier de mettre à la masse
❌ Toucher les composants sous tension

#### Pour les projets

- Décomposer en blocs fonctionnels
- Tester chaque bloc indépendamment
- Simuler avant de réaliser
- Documenter au fur et à mesure
- Prévoir du temps pour le débogage

---

## 📚 Ressources complémentaires

### Ouvrages de référence

1. *Électronique - Fondements et applications* - José-Philippe Pérez (Dunod) - **LA référence**
2. *The Art of Electronics* - Horowitz & Hill (Cambridge) - Bible de l'électronique
3. *Électronique analogique* - François Manneville (Dunod)
4. *Amplificateurs opérationnels* - Henri Fanet (Dunod)

### Datasheets (fiches techniques)

**Où les trouver :**
- Sites fabricants (Texas Instruments, Analog Devices, STMicroelectronics)
- Distributeurs (Mouser, Digi-Key, Farnell)
- Google : "[référence composant] datasheet filetype:pdf"

**Comment les lire :**
- **Absolute Maximum Ratings** : Ne JAMAIS dépasser
- **Electrical Characteristics** : Paramètres typiques et limites
- **Application circuits** : Exemples de montages
- **Package** : Brochage (pinout)

### Ressources en ligne

**Cours et tutoriels :**
- All About Circuits (allaboutcircuits.com) - Complet et gratuit
- Electronics Tutorials (electronics-tutorials.ws)
- Cours Fabrice Sincère (fabrice.sincere.free.fr)

**Chaînes YouTube :**
- **GreatScott!** : Projets DIY, explications claires
- **EEVblog** : Reviews, teardowns, théorie
- **ElectroBOOM** : Pédagogie avec humour (attention aux erreurs volontaires !)
- **Andreas Spiess** : Projets IoT, microcontrôleurs

**Simulateurs en ligne :**
- **Falstad Circuit Simulator** (falstad.com/circuit) - Très interactif
- **EveryCircuit** (everycircuit.com) - Animations
- **CircuitLab** (circuitlab.com) - Complet

---

## 🎯 Sécurité et bonnes pratiques

### Règles de sécurité

🔴 **Ne jamais toucher un circuit sous tension**
🔴 **Vérifier les polarités avant d'alimenter**
🔴 **Respecter les tensions et courants max des composants**
🔴 **Éteindre avant de modifier le câblage**
🔴 **Attention aux condensateurs chargés (décharge avant manipulation)**

### Démarche de débogage systématique

**Circuit qui ne fonctionne pas :**
1. Vérifier l'alimentation (tensions présentes ?)
2. Vérifier les masses (continuité)
3. Contrôler le câblage (schéma vs réalisation)
4. Tester les composants individuellement
5. Vérifier les polarités (diodes, condensateurs électrolytiques, CIs)
6. Mesurer point par point (de l'entrée vers la sortie)

**Composant qui chauffe :**
- ÉTEINDRE IMMÉDIATEMENT
- Vérifier polarité et branchement
- Vérifier l'absence de court-circuit
- Remplacer le composant (probablement grillé)

---

**Bon courage dans votre découverte de l'électronique ! ⚡🔧**

> "In theory, there is no difference between theory and practice. In practice, there is." - Yogi Berra

L'électronique est un domaine pratique. Expérimentez, testez, cassez (un peu), réparez, et surtout : amusez-vous !

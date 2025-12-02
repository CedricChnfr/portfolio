---
layout: default
title: "Composants et Notions de Puissance - S5"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
---

<style>
.back-nav {
    margin-bottom: 20px;
}
.back-nav a {
    text-decoration: none;
    color: #2a7ae2;
    font-weight: 600;
}
.back-nav a:hover {
    text-decoration: underline;
}
.section-title {
    color: #2a7ae2;
    border-bottom: 2px solid #2a7ae2;
    padding-bottom: 10px;
    margin-top: 30px;
    margin-bottom: 20px;
}
</style>

<div class="back-nav">
    <a href="./my-courses-2022-2023.html">← Retour à Mes Cours 2022-2023</a>
</div>

# ⚡ Composants et Notions de Puissance - S5

**Année**: 2022-2023 (Semestre 5)  
**Crédits**: 3 ECTS  
**Type**: Électronique de Puissance

---

## PART A: PRÉSENTATION GÉNÉRALE

### Objectifs du cours

Le cours "Composants et Notions de Puissance" constitue une introduction fondamentale à l'électronique de puissance, domaine essentiel pour la conversion et la gestion de l'énergie électrique. Il couvre les composants semiconducteurs de puissance (diodes, transistors, thyristors), leurs caractéristiques, leurs limites, ainsi que les structures de conversion (redresseurs, hacheurs, onduleurs). Ce cours est indispensable pour comprendre les alimentations à découpage, les variateurs de vitesse, les systèmes d'énergie renouvelable, et les applications de l'électronique embarquée nécessitant une gestion efficace de l'énergie.

### Compétences visées

- Maîtriser le fonctionnement des composants semiconducteurs de puissance
- Analyser les circuits de conversion d'énergie (AC-DC, DC-DC, DC-AC)
- Dimensionner les composants de puissance (courants, tensions, dissipation thermique)
- Comprendre les pertes et calculer le rendement des convertisseurs
- Concevoir des circuits de protection et de commande rapprochée
- Analyser les contraintes thermiques et dimensionner les dissipateurs
- Appliquer les règles de sécurité en électronique de puissance

### Organisation

- **Volume horaire**: 30h (CM: 16h, TD: 10h, TP: 4h)
- **Évaluation**: 2 contrôles écrits (ACE 1: 40%, ACE 2: 40%) + TDs/TPs (20%)
- **Semestre**: 5 (2022-2023)
- **Prérequis**: Électronique fondamentale, circuits électriques, composants passifs

---

## PART B: EXPÉRIENCE, CONTEXTE ET FONCTION

### Contenu pédagogique

Le cours s'articule autour de trois axes principaux: les composants, les structures de conversion, et les aspects thermiques/pratiques.

#### 1. Composants Semiconducteurs de Puissance

##### A. Diodes de Puissance

**Diode à jonction PN**:

La diode de puissance est le composant le plus simple de l'électronique de puissance. Elle se comporte comme un interrupteur unidirectionnel (commande naturelle).

**Caractéristiques principales**:
- **Tension directe** (forward voltage): VF ≈ 0.7 - 1.5V selon le courant
- **Courant moyen** IF(AV): courant continu maximal
- **Courant de pointe** IFSM: courant de surcharge temporaire
- **Tension inverse maximale** VRRM (Peak Repetitive Reverse Voltage)
- **Temps de recouvrement inverse** trr: temps de commutation

**Modèle simplifié**:
- **État passant** (ON): VD ≈ VF0 + RD × ID où VF0 est la tension de seuil (~0.7V) et RD la résistance dynamique
- **État bloqué** (OFF): ID ≈ 0, diode supporte VR en inverse

**Recouvrement inverse**:

Lors du blocage, la diode ne se bloque pas instantanément. Il existe un temps trr pendant lequel un courant inverse IRR circule (évacuation des porteurs minoritaires).

Qrr = (1/2) × IRR × trr

où Qrr est la charge de recouvrement.

**Pertes dans la diode**:
- **Pertes en conduction**: Pcond = VF × ID(AV) + RD × ID(RMS)²
- **Pertes en commutation**: Psw = (1/2) × VR × IRR × trr × fsw

**Diodes rapides (Fast Recovery)**:
- trr < 500 ns (vs plusieurs µs pour diode standard)
- Utilisées dans les convertisseurs à haute fréquence (>10 kHz)
- Réduction des pertes de commutation

**Diodes Schottky**:
- Jonction métal-semiconducteur (pas de recouvrement inverse)
- VF plus faible (~0.3-0.5V) mais VRRM limité (<200V)
- Utilisées en basse tension, haute fréquence
- Applications: alimentations à découpage, redressement synchrone

##### B. Transistors de Puissance

**Transistor Bipolaire de Puissance (BJT)**:

Le BJT de puissance est commandé en courant.

**Caractéristiques**:
- **Gain en courant** β: IC = β × IB (typiquement β = 10-50 en puissance)
- **Tension de saturation** VCE(sat) ≈ 0.5 - 2V
- **Zone de Sécurité** (SOA - Safe Operating Area): limite VCE vs IC

**Conditions de saturation**:

IB > IC / β

En pratique, on utilise IB = IC / (5-10) pour garantir la saturation profonde.

**Pertes**:
- **Conduction**: Pcond = VCE(sat) × IC
- **Commutation**: Psw = (1/6) × VCE × IC × (ton + toff) × fsw

**Inconvénients du BJT**:
- Commande en courant (puissance de commande élevée)
- Temps de commutation élevés (µs)
- Risque de destruction en zone linéaire (chauffage)

**Transistor MOSFET de Puissance**:

Le MOSFET est commandé en tension (grille isolée).

**Caractéristiques principales**:
- **Résistance à l'état passant** RDS(on): augmente avec la tension nominale
- **Tension Drain-Source maximale** VDSS
- **Courant continu maximal** ID
- **Capacités parasites**: Cgs, Cgd (Miller), Cds
- **Charge de grille** Qg: charge nécessaire pour commuter

**Équation en saturation**:

ID = K × (VGS - Vth)²

où Vth est la tension de seuil (typiquement 2-4V).

**Pertes**:
- **Conduction**: Pcond = RDS(on) × ID(RMS)²
- **Commutation**: liées aux capacités parasites
    
    Psw = (1/2) × Coss × VDS² × fsw + VDS × ID × (tr + tf) × fsw

**Avantages du MOSFET**:
- Commande simple (tension, pas de courant permanent)
- Commutation rapide (ns)
- Pas de phénomène de stockage (comme le BJT)
- Résistance RDS(on) augmente avec la température → limitation naturelle du courant

**Diode de roue libre interne**:
Le MOSFET possède une diode intrinsèque (body diode) entre drain et source, utilisable pour les applications inductives.

**Transistor IGBT (Insulated Gate Bipolar Transistor)**:

L'IGBT combine les avantages du MOSFET (commande en tension) et du BJT (faible chute de tension à fort courant).

**Structure**: MOSFET + BJT en Darlington

**Caractéristiques**:
- **Tension de saturation**: VCE(sat) ≈ 1.5 - 3V (indépendant du courant)
- **Commande en tension** comme le MOSFET
- **Temps de commutation**: intermédiaire (100-500 ns)
- **Tension maximale**: jusqu'à plusieurs kV

**Équation**:

IC = gm × (VGE - Vth)

où gm est la transconductance.

**Applications typiques**:
- MOSFET: <1kV, haute fréquence (>100kHz), RDS(on) faible
- IGBT: >600V, fréquence moyenne (1-50kHz), puissance élevée
- BJT: obsolète (remplacé par IGBT)

**Comparaison MOSFET vs IGBT**:

| Critère | MOSFET | IGBT |
|---------|--------|------|
| Commande | Tension | Tension |
| V max | <1000V | >6500V |
| I max | <500A | >3000A |
| Fréquence | >100kHz | <50kHz |
| Pcond | RDS(on) × I² | VCE(sat) × I |
| Applications | Alim. découpage, DC-DC | Variateurs, traction, éolien |

##### C. Thyristors

**Thyristor (SCR - Silicon Controlled Rectifier)**:

Le thyristor est un composant à 4 couches (PNPN) commandé à l'amorçage uniquement.

**Principe**:
- **Amorçage** (ON): impulsion de courant sur la gâchette (gate) IG > IGT
- **Maintien**: le thyristor reste passant tant que IAK > IH (courant de maintien)
- **Blocage** (OFF): uniquement par annulation du courant IAK

**Caractéristiques**:
- **Tension directe**: VAK ≈ 1-2V à l'état passant
- **Courant de gâchette**: IGT = 20-200 mA
- **Courant de maintien**: IH ≈ 10-100 mA
- **dV/dt max**: vitesse de montée en tension maximale (risque d'amorçage intempestif)
- **dI/dt max**: vitesse de montée en courant à l'amorçage

**Limitations**:
- Commande unidirectionnelle (amorçage seulement)
- Blocage naturel (nécessite annulation du courant)
- Utilisé principalement en AC (commutation naturelle)

**TRIAC (TRIode for Alternating Current)**:

Équivalent bidirectionnel du thyristor.

**Structure**: 2 thyristors tête-bêche

**Applications**:
- Gradateurs AC (variateurs de lumière)
- Commande de puissance en AC
- Limitation: faible fréquence (<400Hz)

**GTO (Gate Turn-Off Thyristor)**:

Thyristor pouvant être bloqué par impulsion négative sur la gâchette.

**Caractéristiques**:
- Blocage commandé: IG < -IGQ (courant négatif élevé, ~20% de IAK)
- Tension élevée (>4kV)
- Applications: traction, forte puissance

Aujourd'hui, les GTO sont remplacés par les IGBT.

#### 2. Structures de Conversion d'Énergie

##### A. Redresseurs (AC → DC)

**Redressement non commandé**:

**Redresseur simple alternance**:
```
                D1
VAC ------>|---+--- VDC
                             |
                            RL    C
                             |    ||
                            GND---+
```

**Valeur moyenne** (charge résistive):

VDC = Vmax / π ≈ 0.318 × Vmax

**Valeur efficace**:

VRMS = Vmax / 2

**Taux d'ondulation**: très élevé (100%)

**Redresseur double alternance (pont de Graetz)**:
```
             D1      D3
     +---|>|--+--|>|--+
     |        |       |
VAC ~       RL      + VDC
     |        |       |
     +---|>|--+--|>|--+
             D2      D4
```

**Valeur moyenne**:

VDC = (2 × Vmax) / π ≈ 0.637 × Vmax

Pour VAC = 230V efficace:

VDC = 0.637 × 230 × √2 ≈ 207V

**Avec filtrage capacitif**:

VDC ≈ Vmax - Iload / (2 × f × C)

où f est la fréquence du réseau (50Hz en Europe).

**Dimensionnement du condensateur**:

Pour un taux d'ondulation δ (ripple):

C = Iload / (2 × f × δ × VDC)

**Exemple**: Pour Iload = 2A, VDC = 200V, δ = 5%:

C = 2 / (2 × 50 × 0.05 × 200) = 200 µF

**Redressement commandé (thyristors)**:

Redresseur à thyristors avec angle de retard α.

**Valeur moyenne**:

VDC = (2 × Vmax / π) × cos(α)

- α = 0°: VDC maximal (comme diodes)
- α = 90°: VDC = 0
- α > 90°: VDC < 0 (fonctionnement onduleur)

**Applications**: variateurs de vitesse pour moteurs DC, charges de batteries avec contrôle.

##### B. Hacheurs (DC → DC)

Les hacheurs (choppers) permettent de contrôler la tension continue par découpage à haute fréquence.

**Hacheur série (Buck / abaisseur)**:

```
Vin --[MOSFET]--+--[L]--+-- Vout
                                |       |
                             [D]     [C]  RL
                                |       |
                             GND-----GND
```

**Principe**:
- MOSFET ON pendant α × T: VL = Vin - Vout, L stocke énergie
- MOSFET OFF pendant (1-α) × T: diode conduit, L restitue énergie

**Tension de sortie**:

Vout = α × Vin

où α est le rapport cyclique (duty cycle), 0 < α < 1.

**Dimensionnement de l'inductance**:

Pour un fonctionnement en conduction continue:

L > ((1-α) × Vout) / (2 × fsw × ΔIL)

où ΔIL est l'ondulation de courant admissible.

**Exemple**: Vin = 12V, Vout = 5V, Iload = 2A, fsw = 100kHz, ΔIL = 0.4A

α = 5/12 = 0.417

L > ((1-0.417) × 5) / (2 × 100000 × 0.4) = 36.4 µH

On choisit L = 47 µH (valeur normalisée).

**Dimensionnement du condensateur**:

C > ΔIL / (8 × fsw × ΔVout)

**Hacheur boost (élévateur)**:

```
                [L]
Vin ---[===]---+--[D]---+--- Vout
                             |        |
                     [MOSFET]    [C]  RL
                             |        |
                            GND------GND
```

**Tension de sortie**:

Vout = Vin / (1 - α)

Pour α = 0.5: Vout = 2 × Vin

**Limitation**: α ne peut pas atteindre 1 (théoriquement Vout → ∞)

**Applications**: PFC (Power Factor Correction), panneaux solaires, boost pour LED.

**Hacheur buck-boost (inverseur)**:

Vout = -(α / (1-α)) × Vin

Permet d'obtenir une tension de sortie de polarité inverse.

**Rendement des hacheurs**:

η = Pout / Pin = (Vout × Iout) / (Vin × Iin)

Typiquement: η = 85-95% selon la conception.

**Pertes**:
- Conduction: RDS(on) × I²
- Commutation: proportionnelle à fsw
- Inductance: résistance série (ESR)
- Diode: VF × I

##### C. Onduleurs (DC → AC)

**Onduleur monophasé en pont (H-bridge)**:

```
                Q1        Q3
        +---|  |--+--|  |--+
        |         |       |
VDC =        Load     ~VAC
        |         |       |
        +---|  |--+--|  |--+
                Q2        Q4
```

**Commande complémentaire**:
- Q1, Q4 ON → Vload = +VDC
- Q2, Q3 ON → Vload = -VDC

**MLI (Modulation de Largeur d'Impulsion) / PWM**:

Comparaison d'une sinusoïde de référence Vref avec une porteuse triangulaire à fréquence fsw élevée.

**Indice de modulation**:

m = Vref(peak) / Vtri(peak)

**Tension efficace fondamentale**:

VAC(RMS) = (m × VDC) / √2

Pour m = 1 (pleine modulation):

VAC(RMS) = 0.707 × VDC

**Taux de distorsion harmonique (THD)**:

THD = (√(somme des Vn² pour n≥2) / V1) × 100%

La MLI permet de réduire le THD (typiquement <5% avec MLI sinusoïdale).

**Onduleur triphasé**:

3 bras (6 transistors) pour générer un système triphasé équilibré.

**Applications**:
- Variateurs de vitesse pour moteurs AC
- Onduleurs solaires (photovoltaïque)
- ASI (Alimentation Sans Interruption / UPS)
- Traction électrique (trains, voitures électriques)

#### 3. Aspects Thermiques et Pratiques

##### A. Gestion Thermique

**Modèle thermique**:

La thermique des semiconducteurs suit une analogie électrique:
- **Flux thermique** P (W) ↔ Courant I
- **Température** T (°C) ↔ Tension V
- **Résistance thermique** Rth (°C/W) ↔ Résistance R

**Loi d'Ohm thermique**:

Tj - Ta = Rth(j-a) × Pd

où:
- Tj: température de jonction (junction)
- Ta: température ambiante (ambient)
- Pd: puissance dissipée
- Rth(j-a): résistance thermique jonction-ambiant

**Chaîne thermique complète**:

Tj = Ta + (Rth(j-c) + Rth(c-h) + Rth(h-a)) × Pd

où:
- Rth(j-c): jonction → boîtier (case), donnée dans la datasheet
- Rth(c-h): boîtier → dissipateur (heatsink), dépend de l'interface (pâte thermique)
- Rth(h-a): dissipateur → ambiant, à calculer/choisir

**Température de jonction maximale**:

Typiquement: Tj(max) = 125-150°C pour les semiconducteurs de puissance.

**Calcul du dissipateur nécessaire**:

Rth(h-a) = (Tj(max) - Ta) / Pd - Rth(j-c) - Rth(c-h)

**Exemple**: MOSFET dissipant Pd = 20W
- Tj(max) = 150°C
- Ta = 40°C (ambiant max)
- Rth(j-c) = 1°C/W (datasheet)
- Rth(c-h) = 0.5°C/W (interface avec pâte thermique)

Rth(h-a) = (150 - 40) / 20 - 1 - 0.5 = 5.5 - 1.5 = 4°C/W

Il faut un dissipateur avec Rth(h-a) < 4°C/W (avec marge de sécurité: choisir 3°C/W).

**Facteurs influençant Rth(h-a)**:
- Surface du dissipateur
- Forme (ailettes, profilé)
- Matériau (aluminium: meilleur compromis coût/performance)
- Ventilation forcée vs convection naturelle

**Avec ventilation forcée**:

Rth(h-a) = Rth(natural) / k

où k = 3-10 selon le débit d'air.

##### B. Protections

**Protection en surintensité**:

- **Fusibles ultra-rapides** (aR): protection contre les courts-circuits
    - Caractéristique I²t: énergie de fusion
    - Coordination avec les semiconducteurs
    
- **Limitation par composant**:
    - MOSFET: RDS(on) augmente avec T → limitation naturelle
    - BJT/IGBT: nécessitent protection externe

**Protection en surtension**:

- **Diodes transil (TVS)**: écrêtage des surtensions
- **Varistances (VDR)**: protection réseau AC
- **Snubbers**: circuits RC ou RCD pour limiter les dV/dt

**Circuit snubber RC**:
```
             R (10-100Ω)
     +---/\/\/---+
     |           |
Component     ===  C (10-100nF)
     |           |
     +-----------+
```

Rôle: absorber l'énergie inductive lors des commutations, protéger des surtensions.

**Dimensionnement**:

C = (L × Imax²) / Vspike²

où Vspike est la surtension admissible.

**Protection thermique**:

- **Thermostat** sur dissipateur: coupure si T > Tmax
- **Capteur intégré**: certains IGBT ont protection thermique interne

##### C. Commande Rapprochée (Gate Drive)

**Driver de MOSFET/IGBT**:

**Caractéristiques nécessaires**:
- Tension de grille: typiquement VGS = 10-15V pour MOSFET, VGE = 15V pour IGBT
- Courant de grille: IG = Qg / trise (plusieurs ampères pendant les transitoires)
- Isolation galvanique: nécessaire pour les bras de pont (high-side)

**Circuit de commande**:

```
Signal PWM → [Optocoupleur] → [Driver IC] → Gate MOSFET
                                                                     ↑
                                                                Alim isolée
```

**Drivers IC populaires**:
- IR2110, IR2184 (International Rectifier): half-bridge, bootstrap
- TLP250: optocoupleur + driver pour IGBT
- UCC27321: driver bas coût pour MOSFET

**Bootstrap**:

Technique pour alimenter le driver high-side avec une simple diode et condensateur:

```
                Vcc
                 |
                [D]
                 |
        [Cboot]---[Driver]---Gate High-Side
                 |                    |
        Midpoint----------------Source
```

Lors de la phase low-side ON, le condensateur Cboot se charge. Il alimente ensuite le driver high-side.

**Dimensionnement**:

Cboot > (Qg × (1 + fmax/fmin)) / (Vboot(min) - VGS)

**Résistance de grille**:

Rg = (Vdriver - VGS(th)) / IG(peak)

Compromis:
- Rg faible: commutation rapide, mais surtensions (dV/dt, dI/dt élevés), oscillations
- Rg élevée: commutation lente, pertes accrues

Typiquement: Rg = 10-100Ω

##### D. CEM et Filtrage

**Perturbations en électronique de puissance**:

- **Conduites**: par les câbles d'alimentation
- **Rayonnées**: par les boucles de courant à haute fréquence

**Normes**:
- EN 55022 (CISPR 22): équipements IT
- EN 61000-6-3: environnement résidentiel
- Limites en dBµV pour différentes bandes de fréquence

**Filtrage CEM**:

**Filtre d'entrée AC**:
```
Phase ----[Cx]----[Lcm]----+---- Vers redresseur
                                    [Lcm]    |
Neutre ---[Cx]-------------+
                                                        |
Terre --------[Cy]----[Cy]--+
```

- **Cx**: condensateurs X (entre phase et neutre) - mode différentiel
- **Cy**: condensateurs Y (vers terre) - mode commun
- **Lcm**: inductances de mode commun (sur tore)

**Fréquence de coupure**:

fc = 1 / (2π × √(L × C))

Typiquement: fc = 10-50kHz pour un filtre d'entrée réseau.

---

## PART C: ASPECTS TECHNIQUES

### Exercices de TD

#### TD1: Dimensionnement de composants

**Exercice type**: Dimensionner les composants d'un redresseur double alternance pour une alimentation 5V/10A.

**Données**:
- Réseau: 230V AC, 50Hz
- Sortie: 5V DC, 10A
- Ondulation admissible: 5%

**1. Transformateur**:

Rapport de transformation pour obtenir ~5V en sortie après redressement:

V2(RMS) = Vout / 0.637 = 5 / 0.637 ≈ 7.85V

Avec marge et pertes: V2(RMS) = 9V

Courant secondaire: I2 = 10A (nominal) + marge 20% = 12A

**Puissance apparente**:

S = V2 × I2 = 9 × 12 = 108 VA

**2. Diodes**:

Courant moyen par diode (pont complet):

IF(AV) = Iload / 2 = 10 / 2 = 5A

Courant efficace:

IF(RMS) = Iload / √2 = 7.07A

Tension inverse maximale:

VRRM > √2 × V2 = 1.414 × 9 = 12.7V

**Choix**: diode 1N5402 (3A, 200V) en parallèle ou diode Schottky MBR20100 (20A, 100V)

**3. Condensateur de filtrage**:

C = Iload / (2 × f × δ × Vout) = 10 / (2 × 50 × 0.05 × 5) = 4000 µF

**Choix**: condensateur électrolytique 4700µF / 16V (valeur standard supérieure)

**Tension efficace sur le condensateur** (ripple):

Vripple(RMS) = δ × Vout = 0.05 × 5 = 0.25V

**Courant efficace**:

IC(RMS) = Iload × √(π²/3 - 2) ≈ 0.5 × Iload = 5A

Vérifier que le condensateur supporte ce courant (ESR suffisamment faible).

#### TD2: Hacheur Buck

**Exercice**: Concevoir un hacheur Buck Vin = 24V → Vout = 12V, Iload = 5A, fsw = 50kHz

**1. Rapport cyclique**:

α = Vout / Vin = 12 / 24 = 0.5

**2. Inductance**:

Pour ΔIL = 20% de Iload: ΔIL = 1A

L = ((Vin - Vout) × α) / (fsw × ΔIL) = ((24-12) × 0.5) / (50000 × 1) = 120 µH

**Choix**: L = 150 µH, courant de saturation Isat > 6A

**3. Condensateur de sortie**:

C = ΔIL / (8 × fsw × ΔVout)

Pour ΔVout = 1% de 12V = 0.12V:

C = 1 / (8 × 50000 × 0.12) = 208 µF

**Choix**: C = 220 µF / 25V (céramique) ou 330µF / 25V (électrolytique faible ESR)

**4. MOSFET**:

Courant: ID > Iload + ΔIL/2 = 5.5A → **choisir 10A** (facteur 2)

Tension: VDS > Vin → **choisir 40-60V**

Exemple: IRFZ44N (55V, 49A, RDS(on) = 17.5mΩ)

**Pertes en conduction**:

Pcond = RDS(on) × ID(RMS)² = 0.0175 × 5² = 0.44W

**Pertes en commutation** (estimation):

Psw ≈ (Vin × ID × (tr + tf) × fsw) / 6

Pour tr + tf ≈ 100ns:

Psw = (24 × 5 × 100 × 10⁻⁹ × 50000) / 6 ≈ 1W

**Puissance totale dissipée**: Pd = 0.44 + 1 = 1.44W

**5. Diode de roue libre**:

Courant moyen: IF(AV) = (1-α) × Iload = 0.5 × 5 = 2.5A

Tension inverse: VRRM > Vin = 24V → **choisir 40-60V**

Diode Schottky: MBR2045 (20A, 45V, VF = 0.5V)

**Pertes dans la diode**:

Pdiode = VF × IF(AV) = 0.5 × 2.5 = 1.25W

**6. Rendement**:

Pout = Vout × Iload = 12 × 5 = 60W

Plosses = PMOSFET + Pdiode + PL = 1.44 + 1.25 + 0.5 = 3.19W

η = Pout / (Pout + Plosses) = 60 / 63.19 = 95%

#### TD3: Dimensionnement thermique

**Exercice**: Un IGBT dissipe 50W dans un environnement à Ta = 50°C.

**Données**:
- Tj(max) = 150°C
- Rth(j-c) = 0.5°C/W
- Rth(c-h) = 0.2°C/W (interface thermique)

**Calculer le dissipateur nécessaire avec une marge de sécurité de 20°C**.

**Solution**:

Température de jonction cible:

Tj = Tj(max) - marge = 150 - 20 = 130°C

Résistance thermique totale admissible:

Rth(j-a) = (Tj - Ta) / Pd = (130 - 50) / 50 = 1.6°C/W

Résistance thermique du dissipateur:

Rth(h-a) = Rth(j-a) - Rth(j-c) - Rth(c-h) = 1.6 - 0.5 - 0.2 = 0.9°C/W

**Interprétation**:

Rth(h-a) = 0.9°C/W est très faible:
- Convection naturelle: dissipateurs avec Rth > 2°C/W généralement
- **Nécessite ventilation forcée** ou dissipateur très volumineux

**Avec ventilateur** (débit 30 CFM):

Rth(h-a, forced) = Rth(natural) / 5 = 0.9 × 5 = 4.5°C/W

Un dissipateur standard avec Rth = 4°C/W en convection naturelle devient suffisant avec ventilateur.

### Applications Pratiques

**Alimentation à découpage (SMPS)**:
- Buck pour abaissement de tension (chargeurs, régulateurs embarqués)
- Flyback pour isolation galvanique (alimentations PC, LED drivers)
- Forward pour puissances moyennes (télécoms)

**Variateurs de vitesse**:
- Onduleur triphasé + MLI pour moteurs asynchrones
- Contrôle vectoriel (FOC - Field Oriented Control)
- Applications: pompes, ventilateurs, ascenseurs, traction

**Énergie renouvelable**:
- Onduleurs photovoltaïques (MPPT + injection réseau)
- Hacheurs pour éoliennes
- Convertisseurs bidirectionnels pour batteries

**Automobile**:
- Convertisseurs DC-DC (12V ↔ 48V, batterie haute tension)
- Onduleurs pour moteurs électriques (VE)
- Chargeurs embarqués (OBC - On-Board Charger)

---

## PART D: ANALYSE ET RÉFLEXION

### Connaissances et compétences mobilisées

- **Semiconducteurs de puissance**: compréhension des caractéristiques et limitations des composants
- **Conversion d'énergie**: maîtrise des topologies de base (redresseurs, hacheurs, onduleurs)
- **Dimensionnement**: calculs de composants (inductances, condensateurs, dissipateurs)
- **Thermique**: gestion de la dissipation thermique et calcul de résistances thermiques
- **Protections**: conception de circuits de protection (snubbers, fusibles)
- **Commande**: drivers de grille, isolation galvanique, PWM

### Auto-évaluation

Ce cours a été essentiel pour comprendre la gestion de l'énergie dans les systèmes électroniques.

**Points forts**:
- **Vision globale**: des composants aux systèmes complets de conversion
- **Approche pratique**: dimensionnement concret avec calculs d'application
- **Thermique**: compréhension des limites réelles des composants
- **Multidisciplinarité**: électronique + thermique + commande

**Difficultés rencontrées**:
- **Choix des composants**: nombreux critères (tension, courant, fréquence, thermique, coût)
- **Compromis performances/pertes**: optimisation non triviale
- **Aspects CEM**: parasites et perturbations difficiles à prévoir/simuler

**Applications pratiques**:
- Dimensionnement d'alimentations à découpage
- Compréhension des datasheets de semiconducteurs
- Évaluation thermique de cartes électroniques

### Mon opinion

Ce cours est fondamental pour tout ingénieur en systèmes embarqués ou électronique de puissance.

**Pourquoi ce cours est essentiel**:

1. **Efficacité énergétique**: enjeu majeur (IoT, véhicules électriques, data centers)
2. **Omniprésence**: tous les systèmes ont besoin de conversion d'énergie
3. **Compétence différenciante**: moins de compétitions sur ces sujets "durs" vs programmation
4. **Complémentarité**: lie électronique analogique, numérique, et automatique

**Connexions avec autres cours**:
- **Électronique Analogique** (S5): bases sur les semiconducteurs (diodes, transistors)
- **Architectures Analogiques** (S7): amplification et conditionnement de puissance
- **Commande Numérique** (S8): MLI, contrôle de convertisseurs, MPPT
- **Temps Réel** (S8): contraintes temporelles pour les boucles de régulation

**Évolution technologique**:

Les défis actuels:
- **GaN et SiC**: nouveaux semiconducteurs (> 600V, > 200kHz, < pertes)
    - GaN: très haute fréquence (MHz), faible Qg, faible RDS(on)
    - SiC: haute tension (>1200V), haute température (>175°C)
- **Intégration**: modules de puissance complets (MOSFET + driver + protections)
- **Contrôle numérique**: DSP/FPGA pour MLI avancée, contrôle adaptatif
- **Bidirectionnalité**: V2G (Vehicle-to-Grid), stockage d'énergie

**Applications émergentes**:
- **Véhicules électriques**: OBC 11-22kW, onduleurs 100-300kW, DC-DC pour auxiliaires
- **Chargeurs rapides**: 50-350kW (Supercharger Tesla, Ionity)
- **Data centers**: alimentations redondantes, efficacité >95%
- **Énergies renouvelables**: onduleurs PV résidentiels (3-10kW) et centrales (MW)

**Tendances**:

- **Miniaturisation**: augmentation des fréquences de découpage (GaN → MHz)
- **Fiabilité**: électronique automobile (AEC-Q100), aéronautique (DO-254)
- **Modularité**: convertisseurs parallèles, redondance
- **Smart Grid**: onduleurs communicants, gestion de l'énergie

**Recommandations pour réussir**:

1. **Comprendre les limitations**: chaque composant a des contraintes (SOA, thermique)
2. **Toujours vérifier la thermique**: cause n°1 de défaillance
3. **Utiliser les datasheets**: source d'information indispensable
4. **Simuler**: LTspice, PSIM pour valider avant prototypage
5. **Layout PCB critique**: boucles de courant courtes, découplage, masse

**Applications professionnelles**:

Ces compétences sont recherchées dans:
- **Automobile**: systèmes de traction, chargeurs, convertisseurs DC-DC
- **Aéronautique/spatial**: alimentations haute fiabilité, convertisseurs 270V DC
- **Énergie**: onduleurs solaires/éoliens, HVDC, smart grids
- **Télécoms**: alimentations pour stations de base, PoE (Power over Ethernet)
- **Industriel**: variateurs de vitesse, onduleurs de soudage, alimentations process
- **Médical**: alimentations isolées, sécurité renforcée (IEC 60601)

**Aspects pratiques importants**:

- **Sécurité**: isolation galvanique, respect des distances de fuite/ligne
- **Normes**: CE (EN 60950, EN 62368), UL, CCC selon les marchés
- **Tests**: essais de tenue en tension (hipot), courant de fuite, CEM
- **Coût**: optimisation du BOM (Bill of Materials), composants standards vs custom

**Certification et normes**:
- IPC-2221: design de PCB
- IEC 61000: compatibilité électromagnétique
- EN 60950 / EN 62368: sécurité des équipements IT

En conclusion, ce cours fournit les bases indispensables pour concevoir des systèmes de conversion d'énergie efficaces et fiables. La maîtrise des composants de puissance, des topologies de conversion, et de la gestion thermique est essentielle dans un contexte de transition énergétique et d'électrification croissante des systèmes.

---

<style>
        body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                color: #333;
                line-height: 1.6;
        }
        h2, h3, h4, h5 {
                color: #2a7ae2;
        }
        p {
                text-align: justify;
        }
        code {
                background-color: #f5f5f5;
                padding: 2px 6px;
                border-radius: 3px;
                font-family: 'Courier New', monospace;
        }
        pre {
                background-color: #f5f5f5;
                padding: 15px;
                border-radius: 5px;
                overflow-x: auto;
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
                background-color: #2a7ae2;
                color: white;
        }
        tr:nth-child(even) {
                background-color: #f9f9f9;
        }
</style>


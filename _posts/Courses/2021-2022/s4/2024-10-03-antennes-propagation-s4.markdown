---
layout: default
title: "Antennes et Propagation - S4"
date:   2024-10-02 10:56:03 +0200
---

<style>
  .course-header {
    background: linear-gradient(135deg, #ffffffff 0%, #764ba2 100%);
    color: white;
    padding: 2rem;
    border-radius: 10px;
    margin-bottom: 2rem;
  }
  .section-title {
    color: #2a7ae2;
    border-left: 4px solid #2a7ae2;
    padding-left: 1rem;
    margin-top: 2rem;
    margin-bottom: 1rem;
  }
  .info-box {
    background: #f0f7ff;
    border-left: 4px solid #2a7ae2;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 5px;
  }
  .warning-box {
    background: #fff4e6;
    border-left: 4px solid #ff9800;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 5px;
  }
</style>

<div class="course-header">
  <h1>📡 Antennes et Propagation</h1>
  <p><strong>Semestre 4 - DUT GEII</strong></p>
  <p>Conception, simulation et caractérisation d'antennes pour systèmes sans fil. Applications IoT, WiFi, 4G/5G, satellite.</p>
</div>

---

## PART A - Présentation Générale du Cours

<h3 class="section-title">Contexte et objectifs</h3>

Ce module constitue la suite directe du cours de **Propagation et Hyperfréquences du S3**, en approfondissant la conception et la caractérisation d'antennes pour les communications sans fil modernes. Dans un contexte où les systèmes RF se multiplient (IoT, 5G, satellite, RFID), la maîtrise de la conception d'antennes devient une compétence clé pour l'ingénieur en électronique.

**Objectifs pédagogiques :**
- Maîtriser les **paramètres caractéristiques des antennes** (gain, diagramme de rayonnement, polarisation, adaptation)
- Concevoir différents types d'antennes (dipôle, patch, Yagi-Uda)
- Utiliser des **outils de simulation électromagnétique** professionnels (MMANA-GAL, CST, HFSS)
- Réaliser des **mesures en chambre anéchoïque** et au VNA (analyseur de réseau)
- Effectuer des **bilans de liaison radio** pour planifier des systèmes de communication

**Prérequis nécessaires :**
- Propagation et Hyperfréquences S3 (lignes de transmission, abaque de Smith, paramètres S)
- Circuits Hyperfréquences (techniques d'adaptation d'impédance)
- Électromagnétisme (équations de Maxwell, ondes planes)

---

## PART B - Expérience, Contexte et Fonction

<h3 class="section-title">Organisation et ressources</h3>

Le module était structuré en trois volets complémentaires combinant théorie, simulation et pratique :

**Cours magistraux (18h)** :
- **CM1-2** : Paramètres caractéristiques des antennes (gain, diagramme, polarisation, impédance)
- **CM3-4** : Antennes filaires (dipôle, monopole, Yagi-Uda)
- **CM5-6** : Antennes imprimées (patch rectangulaire, circulaire)
- **CM7-8** : Propagation des ondes (modes, phénomènes, modèles)
- **CM9** : Bilans de liaison radio et planification

**Travaux dirigés (12h)** :
- **TD1** : Calculs de paramètres d'antennes (gain, directivité, efficacité)
- **TD2** : Dimensionnement de dipôles et monopoles
- **TD3** : Conception d'antenne patch (formules de dimensionnement)
- **TD4** : Bilan de liaison Friis, pertes en espace libre
- **TD5** : Propagation multi-trajets, zone de Fresnel
- **TD6** : Antenne Yagi (optimisation gain/encombrement)

**Travaux pratiques (18h)** :
- **TP1-2** : Simulation d'antennes avec MMANA-GAL (Yagi) et 4NEC2 (dipôle)
- **TP3-4** : Simulation patch avec CST Microwave Studio ou HFSS
- **TP5-6** : Mesures en chambre anéchoïque (diagrammes de rayonnement, gain)
- **TP7-8** : Mesures d'adaptation au VNA (S11, impédance, TOS)
- **TP9** : Bilan de liaison avec Radio Mobile (planification couverture)

**Projet (20h)** :
Conception complète d'une antenne (patch ou Yagi) : dimensionnement, simulation, fabrication, mesures et documentation.

**Ressources pédagogiques** :
- Polycopié de cours "Antennes et Propagation EN2A 2021-2022"
- TD avec exercices d'application
- Texte global TP "Antennes EN 2021-2022"
- Datasheet antenne Yagi Siretta Oscar3A (exemple industriel)
- Logiciels : MMANA-GAL, 4NEC2, CST Microwave Studio, HFSS, Radio Mobile
- Équipements : chambre anéchoïque, VNA (analyseur de réseau), analyseur de spectre

<h3 class="section-title">Méthodologie d'étude</h3>

**Phase 1 : Comprendre les fondamentaux** :
Assimiler les paramètres caractéristiques (gain, directivité, diagramme, polarisation) et leur signification physique. Établir le lien entre géométrie de l'antenne et ses performances.

**Phase 2 : Maîtriser le dimensionnement** :
S'exercer sur les formules de calcul pour dipôles et patchs. Comprendre l'influence des paramètres (fréquence, substrat, dimensions) sur les performances. Utiliser les TD pour développer l'intuition.

**Phase 3 : Simulation intensive** :
Prendre en main les logiciels de simulation EM. Commencer par des structures simples (dipôle) puis progresser vers des antennes complexes (Yagi, patch). Analyser S11, gain, diagrammes.

**Phase 4 : Mesures et validation** :
Confronter simulations et mesures réelles en chambre anéchoïque et au VNA. Identifier les écarts et leurs causes (imperfections de fabrication, environnement, câbles).

**Phase 5 : Approche système** :
Développer une vision globale avec les bilans de liaison. Intégrer antennes, propagation, pertes et marges pour concevoir un système complet.

<h3 class="section-title">Difficultés rencontrées</h3>

**Complexité de la simulation EM** :
Les logiciels 3D (CST, HFSS) ont une courbe d'apprentissage importante. Le maillage, les conditions aux limites et les temps de calcul nécessitent de l'expérience. Commencer par des tutoriels simples avant d'aborder des structures complexes.

**Sensibilité aux paramètres de fabrication** :
Les antennes patch sont sensibles à l'épaisseur du substrat, aux tolérances d'usinage PCB et à la qualité des soudures. Un décalage de quelques % en fréquence est fréquent entre simulation et réalité.

**Environnement de mesure** :
Même en chambre anéchoïque, des réflexions résiduelles et le couplage avec les câbles affectent les mesures. L'étalonnage du VNA et le positionnement précis des antennes sont critiques.

**Compromis de conception** :
Gain, bande passante et encombrement sont antagonistes. Une antenne directive (Yagi) a un gain élevé mais est volumineuse. Un patch est compact mais a une bande étroite. Identifier le bon compromis selon l'application demande de l'expérience.

**Propagation multi-trajets** :
En environnement réel, les phénomènes de réflexion, diffraction et fading compliquent le bilan de liaison. Les modèles théoriques (Friis, Okumura-Hata) donnent des estimations qu'il faut corriger par des marges de sécurité.

---

## PART C - Aspects Techniques

<h3 class="section-title">Module 1 : Paramètres caractéristiques des antennes</h3>

#### Diagramme de rayonnement

Le diagramme de rayonnement représente la distribution spatiale de la puissance rayonnée par l'antenne.

**Représentations** :
- **2D** : Coupes dans les plans E (électrique) et H (magnétique)
- **3D** : Visualisation complète de la distribution de puissance
- **Coordonnées** : Polaires (θ, φ) ou cartésiennes

**Caractéristiques du diagramme** :
- **Lobe principal** : Direction de rayonnement maximal
- **Lobes secondaires** : Directions indésirables de rayonnement
- **Ouverture à -3 dB** : Angle dans lequel la puissance reste supérieure à la moitié du maximum
- **Rapport avant/arrière (F/B)** : Rapport entre puissance rayonnée vers l'avant et vers l'arrière (en dB)

#### Gain et directivité

**Directivité D (dBi)** :
La directivité quantifie la capacité de l'antenne à concentrer l'énergie dans une direction privilégiée, comparée à une antenne isotrope.

```
D = 4π × Umax / Prad
```
Où Umax est l'intensité de rayonnement maximale et Prad la puissance totale rayonnée.

**Gain G (dBi)** :
Le gain tient compte des pertes réelles de l'antenne (pertes ohmiques, diélectriques).

```
G = η × D
```
Où η est l'efficacité de rayonnement (typiquement 70-95%).

**Relation entre gain et ouverture** :
Plus l'antenne est directive (ouverture étroite), plus son gain est élevé.

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S4/antennes-propagation/dipole-half-wave.svg" alt="Antenne dipôle demi-onde" 
       style="max-width: 550px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure 1 : Antenne dipôle λ/2 avec caractéristiques et diagrammes de rayonnement</p>
</div>

#### Polarisation

La polarisation décrit l'orientation du champ électrique de l'onde rayonnée.

**Types de polarisation** :
- **Linéaire** : Verticale (V), Horizontale (H), ou oblique
- **Circulaire** : Droite (RHCP - Right Hand) ou Gauche (LHCP - Left Hand)
- **Elliptique** : Cas général entre linéaire et circulaire

**Rapport axial (AR)** :
Pour une polarisation circulaire, l'AR mesure la qualité de circularité :
- AR = 1 (0 dB) : polarisation circulaire parfaite
- AR > 3 (> 4.8 dB) : considérée comme linéaire

**Importance** :
Pour une communication efficace, émetteur et récepteur doivent avoir la même polarisation. Une désadaptation de polarisation entraîne des pertes (jusqu'à ∞ dB pour des polarisations orthogonales).

#### Impédance d'entrée et adaptation

**Impédance complexe** :
```
Z = R + jX
```
- R : partie résistive (rayonnement + pertes)
- X : partie réactive (stockage d'énergie)

**Adaptation 50Ω** :
La plupart des systèmes RF utilisent une impédance caractéristique de 50Ω. L'antenne doit être adaptée à cette valeur pour un transfert de puissance maximal.

**Coefficient de réflexion S11** :
```
S11 (dB) = 20 log |Γ|
où Γ = (Z - Z0) / (Z + Z0)
```
- S11 < -10 dB : adaptation acceptable (< 10% puissance réfléchie)
- S11 < -15 dB : bonne adaptation (< 3% réfléchie)
- S11 < -20 dB : excellente adaptation (< 1% réfléchie)

**Taux d'ondes stationnaires (TOS ou SWR)** :
```
TOS = (1 + |Γ|) / (1 - |Γ|)
```
- TOS = 1 : adaptation parfaite
- TOS < 2 : généralement acceptable
- TOS > 3 : adaptation médiocre

#### Bande passante

Une antenne a plusieurs bandes passantes selon le critère considéré :

**Bande d'adaptation** :
Plage de fréquences où S11 < -10 dB. Pour les antennes résonnantes (dipôle, patch), typiquement 2-5% de la fréquence centrale.

**Bande de rayonnement** :
Plage où le gain reste dans une certaine tolérance (ex: ±1 dB).

**Bande de polarisation** :
Plage où la polarisation reste acceptable (AR < 3 dB pour circulaire).

<h3 class="section-title">Module 2 : Types d'antennes</h3>

#### Antennes filaires

**Dipôle demi-onde (λ/2)** :

Structure la plus simple et fondamentale en théorie des antennes.

**Caractéristiques** :
- Longueur physique : L ≈ 0.95 × λ/2 (effet capacitif des extrémités)
- Impédance : Z ≈ 73 + j42.5 Ω au centre
- Gain : 2.15 dBi
- Diagramme : omnidirectionnel en plan H, directif en plan E
- Polarisation linéaire

**Calcul pratique** :
```
λ = c / f = 300 / f(MHz)  [en mètres]
L ≈ 143 / f(MHz)  [en mètres]
```

**Applications** : Radio FM, WiFi simple, mesures, référence.

**Dipôle replié** :

Variante avec deux brins reliés aux extrémités.
- Impédance ≈ 300Ω (transformation 4:1)
- Bande passante améliorée
- Utilisé en TV (antenne râteau)

**Monopole quart d'onde (λ/4)** :

Moitié d'un dipôle au-dessus d'un plan de masse (effet miroir).

**Caractéristiques** :
- Nécessite un plan de masse étendu (λ/4 minimum)
- Impédance : Z ≈ 36.5Ω
- Gain : 5.15 dBi (par rapport à isotrope, grâce au plan de masse)
- Omnidirectionnel en plan H

**Applications** : Antennes véhicules, WiFi, GSM, radio mobiles.

**Antenne Yagi-Uda** :

Antenne directive composée d'éléments parasites.

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S4/antennes-propagation/yagi-antenna.svg" alt="Antenne Yagi-Uda" 
       style="max-width: 550px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure 2 : Structure d'une antenne Yagi-Uda avec réflecteur et directeurs</p>
</div>

**Structure** :
- **Réflecteur** : Élément plus long que λ/2 (environ 5% de plus), placé derrière
- **Élément rayonnant** : Dipôle alimenté, longueur λ/2
- **Directeurs** : Éléments plus courts (5% de moins), devant l'élément rayonnant

**Principe** :
Les éléments parasites re-rayonnent l'énergie captée avec un déphasage qui concentre le faisceau vers l'avant.

**Caractéristiques** :
- Gain : 6-17 dBi selon nombre d'éléments (3 éléments ≈ 7 dBi, 10 éléments ≈ 13 dBi)
- Très directive (ouverture 40-70°)
- Rapport F/B : 15-25 dB
- Espacement éléments : 0.2λ à 0.35λ

**Dimensionnement** :
L'optimisation d'une Yagi nécessite des simulations (MMANA-GAL, 4NEC2) pour ajuster longueurs et espacements.

**Applications** : TNT (TV numérique terrestre), liaisons point-à-point WiFi, radioamateur, télémétrie.

#### Antennes imprimées (patch)

**Patch rectangulaire** :

Antenne constituée d'un élément métallique rectangulaire sur un substrat diélectrique avec plan de masse.

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S4/antennes-propagation/patch-antenna.svg" alt="Antenne patch rectangulaire" 
       style="max-width: 550px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure 3 : Antenne patch rectangulaire avec formules de dimensionnement</p>
</div>

**Principe de fonctionnement** :
Le patch se comporte comme une cavité résonnante. Les bords rayonnent comme deux fentes espacées de λ/2.

**Formules de dimensionnement** :

1. **Largeur W** (influence l'impédance) :
```
W = (c / 2fr) × √(2 / (εr + 1))
```

2. **Permittivité effective εreff** :
```
εreff = (εr + 1)/2 + (εr - 1)/2 × [1 + 12h/W]^(-1/2)
```

3. **Extension de longueur ΔL** (effet de frange) :
```
ΔL = 0.412h × [(εreff + 0.3)(W/h + 0.264)] / [(εreff - 0.258)(W/h + 0.8)]
```

4. **Longueur L** :
```
L = (c / 2fr√εreff) - 2ΔL
```

Où :
- fr : fréquence de résonance
- εr : permittivité relative du substrat
- h : épaisseur du substrat
- c = 3×10⁸ m/s

**Substrats courants** :
- FR-4 : εr = 4.4, tan δ = 0.02 (bas coût, pertes moyennes)
- Rogers RO4003 : εr = 3.38, tan δ = 0.0027 (faibles pertes, stable)
- Rogers RT/duroid 5880 : εr = 2.2, tan δ = 0.0009 (très faibles pertes, cher)

**Modes d'alimentation** :
- **Coaxiale** : Connecteur SMA traversant, ajustement position pour adaptation
- **Microstrip** : Ligne microruban, simple à réaliser
- **Couplage par fente** : Isolation émetteur/antenne, bande passante améliorée

**Caractéristiques** :
- Gain : 6-8 dBi
- Bande passante : 2-5% (étroite)
- Directivité : rayonnement hémisphérique (demi-espace)
- Efficacité : 70-90%
- Polarisation : linéaire (ou circulaire avec patch carré et double alimentation)

**Avantages** :
- Faible profil et léger
- Fabrication PCB standard (low-cost)
- Intégration facile dans équipements
- Réseau d'antennes (array) simple à réaliser

**Inconvénients** :
- Bande passante étroite
- Efficacité moyenne (pertes diélectriques)
- Sensible à l'épaisseur du substrat
- Rayonnement arrière (pertes vers plan de masse)

**Applications** : GPS, WiFi, télémétrie, drones, IoT, GNSS.

**Patch circulaire** :

Variante circulaire, souvent utilisée pour polarisation circulaire.
- Rayon : a ≈ λ / (2√εreff)
- Polarisation circulaire avec double alimentation en quadrature (90°)
- Applications GPS, GNSS

#### Antennes large bande

**Antenne log-périodique** :

Structure avec éléments de longueurs croissantes selon une loi logarithmique.
- Large bande : rapport 10:1 possible (ex: 100-1000 MHz)
- Gain modéré mais constant sur la bande (6-10 dBi)
- Encombrante
- Applications : mesure, EMC, radioastronomie

**Antenne spirale** :

Spirale d'Archimède ou logarithmique.
- Ultra large bande (rapport > 10:1)
- Polarisation circulaire naturelle
- Applications : militaire (guerre électronique), GNSS multi-bandes

**Antenne biconique** :

Deux cônes métalliques face à face.
- Ultra large bande (décades)
- Omnidirectionnelle
- Applications : mesure, EMC, calibration

#### Antennes spécialisées

**Antenne cornet** :

Extrémité ouverte d'un guide d'onde.
- Gain élevé : 10-25 dBi
- Bande passante : 10-30%
- Applications : radar, micro-ondes, alimentateur de parabole

**Réseau d'antennes (Array)** :

Combinaison de plusieurs antennes élémentaires avec déphasage contrôlé.
- Balayage électronique du faisceau (phased array)
- Gain élevé (N éléments → gain × N)
- Applications : radar, 5G (beamforming), satellite

**Antenne RFID** :

Antennes spécifiques pour identification radio-fréquence.
- **HF (13.56 MHz)** : boucle magnétique, courte portée (< 1m)
- **UHF (865-868 MHz EU, 902-928 MHz US)** : dipôle ou patch, longue portée (> 10m)
- Polarisation circulaire souvent préférée (lecture tous angles)

<h3 class="section-title">Module 3 : Propagation des ondes radioélectriques</h3>

#### Modes de propagation

**Onde de sol (surface wave)** :

L'onde suit la courbure terrestre en s'appuyant sur la conductivité du sol.
- Fréquences : VLF, LF, MF (< 3 MHz)
- Atténuation croissante avec la fréquence
- Portée : centaines à milliers de km
- Applications : radio maritime, navigation (Loran), radio AM

**Onde de surface (ground wave)** :

Propagation en contact direct avec le sol, faible hauteur.
- Portée limitée : quelques dizaines de km
- Utilisée en AM radio

**Onde d'espace (space wave)** :

Propagation directe + réfléchie sur le sol (two-ray model).
- Fréquences : VHF, UHF (> 30 MHz)
- Nécessite ligne de vue (LOS - Line Of Sight)
- Interférences constructives/destructives (fading)
- Portée : horizon optique étendu (~ 4/3 × horizon géométrique)
- Applications : TV, FM, GSM, WiFi

**Horizon radio** :
```
d (km) ≈ 4.12 × [√h1(m) + √h2(m)]
```
Où h1 et h2 sont les hauteurs des antennes.

**Onde ionosphérique (sky wave)** :

Réflexion sur les couches ionisées de l'atmosphère (ionosphère).
- Fréquences : HF (3-30 MHz)
- Portée : intercontinentale (milliers de km)
- Dépend de l'heure (jour/nuit), saison, activité solaire
- MUF (Maximum Usable Frequency) et LUF (Lowest Usable Frequency)
- Applications : radio ondes courtes, radioamateur

#### Phénomènes de propagation

**Réflexion** :

Rebond de l'onde sur une surface (sol, bâtiments, obstacles).
- Coefficient de réflexion dépend de l'angle d'incidence, polarisation, matériau
- Multi-trajets : somme de rayons direct + réfléchis → interférences

**Diffraction** :

Contournement d'obstacles par l'onde.
- Principe de Huygens-Fresnel
- Permet communication sans ligne de vue directe (NLOS)
- Atténuation knife-edge : pertes selon hauteur obstacle et zone de Fresnel
- Important en zone urbaine (immeubles)

**Zone de Fresnel** :

Ellipsoïde entre émetteur et récepteur. Pour un lien optimal, la première zone de Fresnel doit être dégagée à 60%.

**Rayon première zone de Fresnel** :
```
r (m) = √(λ × d1 × d2 / (d1 + d2))
```
Où d1 et d2 sont les distances aux antennes.

**Réfraction** :

Courbure de la trajectoire lors du changement de milieu (indice optique différent).
- Réfraction atmosphérique : gradient de température et humidité
- Ducting : onde piégée dans un conduit atmosphérique → portée accrue

**Absorption** :

Atténuation par absorption dans les matériaux.
- **Pluie** : atténuation importante au-dessus de 10 GHz (0.1-10 dB/km selon intensité)
- **Végétation** : pertes selon densité feuillage et fréquence
- **Atmosphère** : bandes d'absorption O2 (60 GHz) et H2O (22, 183 GHz)
- **Matériaux** : béton (5-15 dB), murs (3-10 dB), verre (2-6 dB)

**Multi-trajets et fading** :

En environnement complexe, multiples répliques du signal arrivent avec retards et phases différents.
- **Fading rapide** : interférences constructives/destructives (variations amplitude)
- **Fading lent** : masquage par obstacles
- **Fading sélectif en fréquence** : étalement temporel des trajets
- **Effet Doppler** : décalage fréquentiel dû au mouvement

#### Modèles de propagation

**Espace libre (Friis)** :

Propagation idéale sans obstacles.

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S4/antennes-propagation/friis-equation.svg" alt="Équation de Friis" 
       style="max-width: 550px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure 4 : Équation de Friis pour la propagation en espace libre</p>
</div>

**Équation de Friis** :
```
Pr = Pt + Gt + Gr + 20 log(λ / 4πd)  [en dB]
```

Ou en termes de pertes en espace libre (FSPL - Free Space Path Loss) :
```
FSPL (dB) = 32.45 + 20 log(f_MHz) + 20 log(d_km)
```

**Exemple** :
f = 2.4 GHz, d = 100 m
FSPL = 32.45 + 20 log(2400) + 20 log(0.1) = 32.45 + 67.6 - 20 = **80 dB**

**Modèle à deux rayons (two-ray model)** :

Rayon direct + rayon réfléchi sur le sol.
- Interférences selon hauteurs antennes et distance
- Plus réaliste que Friis au-dessus d'une surface

**Okumura-Hata** :

Modèle empirique pour environnements urbains/suburbains.
- Fréquences : 150 MHz - 1.5 GHz
- Hauteur BS : 30-200 m, hauteur mobile : 1-10 m
- Paramètres : type d'environnement (urbain dense, urbain, suburbain, rural)

**COST-231 Hata** :

Extension du modèle Okumura-Hata.
- Fréquences : jusqu'à 2 GHz
- Inclut correction pour bâtiments

**Modèle Walfisch-Ikegami (COST-231)** :

Modèle pour environnements urbains avec diffraction sur toits.
- Hauteur bâtiments, largeur rues
- Précis mais complexe

**Recommandation ITU-R P.1546** :

Courbes de propagation pour services VHF/UHF (broadcast).
- Basé sur mesures statistiques
- Variations selon % temps et % emplacements

<h3 class="section-title">Module 4 : Simulations et mesures</h3>

#### Outils de simulation électromagnétique

**MMANA-GAL** :

Logiciel basé sur la méthode des moments (MoM) pour antennes filaires.
- Spécialisé Yagi-Uda, dipôles
- Interface simple, rapide
- Optimisation automatique
- Gratuit

**4NEC2** :

Interface graphique pour moteur NEC-2 (Numerical Electromagnetics Code).
- Antennes filaires complexes
- Calcul S11, diagrammes, gain
- Très utilisé en radioamateur
- Open source

**CST Microwave Studio** :

Logiciel commercial 3D complet (FIT - Finite Integration Technique).
- Structures quelconques (patch, cornet, réseaux)
- Paramétrage, optimisation, analyse paramétrique
- Calcul temps/fréquence
- Visualisation 3D avancée
- Version académique disponible

**HFSS (Ansys)** :

Logiciel commercial utilisant FEM (Finite Element Method).
- Référence industrielle pour antennes
- Précision élevée
- Calcul S-parameters multi-ports
- Intégration circuits RF
- Version étudiante limitée

**FEKO** :

Logiciel hybride MoM/FEM pour structures électriquement grandes.
- Antennes sur véhicules, avions
- Radar, compatibilité EM

#### Mesures en chambre anéchoïque

**Principe** :

Chambre tapissée d'absorbants RF (pyramides ou ferrites) pour éliminer les réflexions et recréer un espace libre.

**Mesures réalisées** :

**Diagramme de rayonnement** :
- Antenne sous test (AUT) sur plateau tournant
- Antenne source fixe (cornet étalon)
- Rotation azimut et élévation
- Mesure puissance reçue → diagramme

**Gain absolu** :
Méthode des trois antennes ou comparaison avec antenne étalonnée.

**Polarisation** :
Rotation antenne source pour identifier polarisation AUT.

**Équipements** :
- Analyseur de spectre ou récepteur calibré
- Générateur RF
- Positionneur motorisé
- Antenne de référence

#### Mesures au VNA (Vector Network Analyzer)

**Analyseur de réseau vectoriel** :

Mesure amplitude et phase des paramètres S.

**S11 (coefficient de réflexion)** :
- Indique l'adaptation de l'antenne
- S11 < -10 dB souhaité

**Impédance Z** :
Calculée à partir de S11 : Z = Z0 × (1 + S11) / (1 - S11)

**TOS** :
Calculé à partir de S11 : TOS = (1 + |S11|) / (1 - |S11|)

**Procédure** :
1. Calibrage (Open, Short, Load, Thru)
2. Connexion antenne
3. Balayage fréquentiel
4. Identification fréquence de résonance (min S11)

**Pièges à éviter** :
- Câbles de test rayonnent → perturbe mesure (utiliser ferrites)
- Connecteurs mal serrés
- Proximité main/corps

#### Bilan de liaison radio

**Logiciel Radio Mobile** :

Outil de planification de couverture radio.
- Modèles numériques de terrain (MNT)
- Calcul pertes selon topographie
- Profil de liaison point-à-point
- Zones de couverture

**Paramètres d'entrée** :
- Fréquence
- Puissance émetteur (EIRP)
- Gains antennes
- Hauteurs antennes
- Sensibilité récepteur
- Modèle de propagation (Okumura-Hata, ITU, etc.)

**Sorties** :
- Profil altimétrique avec zones de Fresnel
- Pertes de trajet
- Marge de liaison
- Cartographie de couverture

**Marge de liaison** :

Différence entre puissance reçue et sensibilité récepteur.
- Marge typique : 10-20 dB (compense fading, pertes supplémentaires)

**Équation bilan** :
```
Pr (dBm) = EIRP (dBm) - FSPL (dB) + Gr (dBi) - Pertes_diverses (dB)
Marge (dB) = Pr (dBm) - Sensibilité_Rx (dBm)
```

---

## PART D - Analyse et Réflexion

<h3 class="section-title">Évaluation</h3>

Le module était évalué selon une approche mixte valorisant théorie, pratique et projet :

**Travaux pratiques (25%)** :
Évaluation continue sur les 9 séances de TP (simulation et mesures). Critères : compréhension outils, méthodologie, qualité résultats, analyse écarts simulation/mesure.

**Projet antenne (40%)** :
Conception complète d'une antenne (patch ou Yagi) en binôme sur 20h. Livrables : cahier des charges, dimensionnement théorique, simulations, fabrication, mesures, rapport technique et soutenance orale. Évaluation sur démarche scientifique, qualité réalisation et validation expérimentale.

**Contrôle continu (15%)** :
Interrogations écrites courtes (QCM, exercices) pendant les TD pour vérifier acquisition fondamentaux.

**Examen final (15%)** :
Épreuve de 2h : exercices de dimensionnement, analyse de diagrammes, calculs de bilans de liaison. Documents autorisés (polycopié, formulaire).

<h3 class="section-title">Compétences développées</h3>

**Techniques** :
- **Conception d'antennes RF** : maîtrise du dimensionnement théorique (formules analytiques) pour dipôles, monopoles, patchs et Yagi
- **Simulation électromagnétique** : utilisation professionnelle de logiciels EM (MMANA, CST, HFSS) pour analyse et optimisation
- **Mesures RF avancées** : caractérisation en chambre anéchoïque (diagrammes, gain, polarisation) et au VNA (S11, impédance)
- **Bilans de liaison** : calculs de couverture radio, planification avec Radio Mobile
- **Optimisation** : compromis gain/bande passante/encombrement selon contraintes applicatives

**Transversales** :
- Démarche scientifique : confrontation théorie/simulation/mesure, analyse des écarts
- Gestion de projet : cahier des charges, planning, fabrication, documentation technique
- Travail en équipe : répartition des tâches, collaboration TP/projet
- Communication technique : rédaction rapports, présentations orales avec support visuel

<h3 class="section-title">Apports pour la formation</h3>

**Poursuite d'études (Licence, École d'ingénieurs)** :

Ce module constitue une base solide pour des spécialisations en :
- **Télécommunications RF** : systèmes sans fil, radio logicielle (SDR)
- **Systèmes embarqués communicants** : IoT, drones, télémétrie
- **Conception de circuits RF/micro-ondes** : front-end radio, amplificateurs
- **Compatibilité électromagnétique (CEM)** : mesures, antennes de test

Les compétences en simulation EM sont directement valorisables en bureau d'études industriel.

**Vie professionnelle** :

Applications directes dans de nombreux secteurs :
- **Télécommunications** : opérateurs mobiles (antennes stations de base 4G/5G), équipementiers (Ericsson, Nokia, Huawei)
- **Aéronautique/Spatial** : antennes satellites, télémétrie avions/drones, GNSS
- **Automobile** : V2X, radar, keyless entry, TPM, télémétrie
- **IoT** : LoRa, Sigfox, Zigbee, BLE - intégration antennes dans objets connectés
- **Défense** : radars, guerre électronique, communications sécurisées
- **Recherche** : radioastronomie, radar météo, télédétection

**Métiers visés** :
- Ingénieur antennes RF
- Ingénieur systèmes radio
- Ingénieur mesures RF
- Ingénieur CEM
- Consultant en planification radio

<h3 class="section-title">Perspectives et évolutions technologiques</h3>

**Tendances actuelles** :

**Massive MIMO (Multiple-Input Multiple-Output)** :
Réseaux de dizaines/centaines d'antennes en station de base 5G pour beamforming avancé (focalisation du faisceau vers chaque utilisateur). Amélioration capacité et efficacité spectrale.

**Antennes reconfigurables** :
Modification dynamique des caractéristiques (fréquence, diagramme, polarisation) par :
- Commutateurs RF (PIN diodes, MEMS)
- Matériaux actifs (varactors, cristaux liquides)
- Métamatériaux et surfaces intelligentes reconfigurables (RIS)

**Antennes millimétriques (mmWave)** :
Bandes 26, 28, 39 GHz pour 5G. Antennes miniatures intégrées dans smartphones et stations de base. Défis : pertes de propagation, sensibilité blocage.

**Antennes imprimées 3D** :
Fabrication additive métallique pour formes complexes (spirales 3D, antennes diélectriques). Optimisation topologique par IA.

**Intégration antenne-circuit (AiP - Antenna in Package)** :
Antennes intégrées dans substrat ou boîtier du circuit (SiP, PCB multicouche). Réduction taille et coût, crucial pour IoT et wearables.

**Antennes pour satellite LEO (Low Earth Orbit)** :
Constellations Starlink, OneWeb nécessitent antennes plates à balayage électronique (phased arrays) pour suivi satellite.

**Intelligence Artificielle en conception** :
Algorithmes d'optimisation (algorithmes génétiques, réseaux neurones) pour synthèse automatique d'antennes selon spécifications.

<h3 class="section-title">Conseils pour approfondir</h3>

**Livres de référence** :
- "Antenna Theory: Analysis and Design" - C. Balanis (référence universitaire)
- "Antennes : Théorie et pratique" - Jean-Paul Yonnet (en français)
- "Microstrip Antenna Design Handbook" - Garg et al. (patch antennas)
- "The ARRL Antenna Book" (pratique radioamateur)

**Ressources en ligne** :
- **Cours vidéo** : MIT OpenCourseWare, Coursera "RF and Millimeter-Wave Circuit Design"
- **Tutoriels logiciels** : CST, HFSS sur YouTube, forums officiels
- **Communauté radioamateur** : forums, blogs, projets open-source d'antennes
- **Standards IEEE** : IEEE Transactions on Antennas and Propagation

**Projets personnels** :
- Réaliser antennes WiFi/LoRa DIY, mesurer avec RTL-SDR ou NanoVNA
- Participer à compétitions (CubeSat, CanSat) nécessitant conception antennes
- Contribuer à projets open hardware (antennes imprimables, DIY VNA)

**Certifications professionnelles** :
- Formation logiciels EM (CST, HFSS) - certifications éditeurs
- Radioamateur : licence HAREC (pratique antennes autorisée)

<h3 class="section-title">Retour d'expérience et conseils pratiques</h3>

<div class="info-box">
<strong>💡 Conseil n°1 : Simulation avant fabrication</strong><br>
Ne jamais fabriquer une antenne sans l'avoir simulée. Les erreurs de dimensionnement sont coûteuses (PCB, usinage). Une simulation bien paramétrée permet d'anticiper les performances et d'optimiser avant réalisation.
</div>

<div class="info-box">
<strong>💡 Conseil n°2 : Importance du plan de masse</strong><br>
Pour monopoles et patchs, le plan de masse est critique. Sa taille, sa qualité (continuité électrique) et sa connexion (vias) influencent directement le diagramme de rayonnement et l'adaptation.
</div>

<div class="info-box">
<strong>💡 Conseil n°3 : Gérer les écarts simulation/mesure</strong><br>
Un écart de 5-10% en fréquence entre simulation et mesure est normal. Causes : tolérances substrat (εr), usinage PCB, soudures, connecteurs. Prévoir une plage d'ajustement (stubs ajustables, trimming).
</div>

<div class="warning-box">
<strong>⚠️ Piège n°1 : Environnement de mesure</strong><br>
Mesurer une antenne sur une table métallique ou près d'un mur fausse complètement les résultats. Toujours mesurer en chambre anéchoïque ou à l'extérieur, loin d'obstacles (> 3λ).
</div>

<div class="warning-box">
<strong>⚠️ Piège n°2 : Câbles rayonnants</strong><br>
Le câble coaxial d'alimentation peut rayonner et perturber le diagramme (courant de mode commun). Utiliser des ferrites (chokes) ou un balun pour bloquer ces courants parasites.
</div>

<div class="warning-box">
<strong>⚠️ Piège n°3 : Bande passante patch</strong><br>
Les antennes patch ont une bande étroite (2-5%). Pour élargir : augmenter épaisseur substrat (h), utiliser substrat faible εr, ou empiler plusieurs patchs. Compromis gain/bande.
</div>

<h3 class="section-title">Applications pratiques et études de cas</h3>

**Cas 1 : Antenne WiFi 2.4 GHz pour drone**

**Besoin** : antenne compacte, légère, gain modéré (3-5 dBi), omnidirectionnelle.

**Solution** : Patch rectangulaire sur FR-4.
- Dimensionnement : L = 28 mm, W = 36 mm sur FR-4 h=1.6mm
- Alimentation coaxiale ajustable (x0 = 10 mm du bord pour 50Ω)
- Simulation CST : S11 = -25 dB à 2.44 GHz, gain 5.2 dBi
- Fabrication PCB standard, protection vernis
- Mesures : S11 = -18 dB à 2.42 GHz (shift 20 MHz acceptable), gain mesuré 4.8 dBi

**Cas 2 : Liaison point-à-point 5.8 GHz pour transmission vidéo**

**Besoin** : portée 2 km en zone dégagée, débit vidéo HD.

**Solution** : Antennes Yagi 18 éléments (gain 16 dBi).
- Fréquence : 5.8 GHz (ISM, pas de licence)
- Émetteur : 500 mW EIRP (27 dBm + 16 dBi = 43 dBm)
- Récepteur : sensibilité -85 dBm

**Bilan de liaison** :
- FSPL (2 km, 5.8 GHz) = 119 dB
- Pr = 43 + 16 - 119 = -60 dBm
- Marge = -60 - (-85) = **25 dB** ✓ (excellente)

Zone de Fresnel : rayon 1.5 m au milieu de la liaison. Vérifier dégagement sur profil terrain (Radio Mobile).

**Cas 3 : Antenne RFID UHF pour logistique**

**Besoin** : lecture étiquettes RFID jusqu'à 10 m, polarisation circulaire (lecture tous angles).

**Solution** : Antenne patch circulaire double alimentation en quadrature.
- Fréquence : 866 MHz (EU)
- Patch carré 160 mm × 160 mm, deux points d'alimentation à 90° avec déphasage 90°
- Polarisation circulaire (AR < 2 dB)
- Gain : 8 dBi
- Ouverture : 70° (suffisante pour zone de lecture)

## 📚 Ressources et documents complémentaires

### Documents de cours disponibles

Les ressources suivantes sont accessibles dans le dossier du cours :

**Cours théoriques** :
- 📄 `Cours Antenne EN2A 2021-2022.pdf` - Polycopié complet du cours magistral couvrant tous les chapitres (paramètres, types d'antennes, propagation)
- 📄 `Notes de cours#1.pdf` et `Notes sur le cours#2.pdf` - Notes de cours manuscrites complémentaires avec exemples détaillés

**Travaux dirigés** :
- 📄 `TD Antenne ENOC 2021-2022.pdf` - Recueil d'exercices corrigés sur dimensionnement, bilans de liaison, et calculs de paramètres

**Travaux pratiques** :
- 📄 `Texte global TL Antenne EN 2021-2022.pdf` - Guide complet des séances de TP avec protocoles de manipulation et consignes de mesure

**Documentation technique** :
- 📄 `Datasheet Antenne Yagi Siretta Oscar3A.pdf` - Exemple industriel de spécifications d'antenne Yagi (caractéristiques, diagrammes, courbes)

### Pour aller plus loin

**Logiciels et outils** :
- **MMANA-GAL** : http://www.qsl.net/mmhamsoft/mmana/ (gratuit, Windows)
- **4NEC2** : https://www.qsl.net/4nec2/ (gratuit, Windows)
- **NanoVNA** : Analyseur de réseau vectoriel portable low-cost (< 50€) pour mesures S11
- **Radio Mobile** : http://www.ve2dbe.com/rmonline.asp (gratuit, planification radio)

**Communautés et forums** :
- **IEEE Antennas and Propagation Society** : https://www.ieeeaps.org/
- **Radioamateur.org** : Forums francophones sur antennes
- **Reddit r/amateurradio** : Projets et discussions antennes
- **EEVblog Forum** : Section RF et antennes

**Bases de données** :
- **Antenna Magus** : Bibliothèque de structures d'antennes avec formules et modèles
- **Rogers Corporation** : Datasheets substrats haute fréquence
- **ITU-R Recommendations** : Modèles de propagation officiels

### Formules essentielles à retenir

**Conversion longueur d'onde / fréquence** :
```
λ (m) = c / f = 300 / f(MHz)
```

**Dipôle λ/2** :
```
L (m) ≈ 143 / f(MHz)
Z ≈ 73 Ω
Gain = 2.15 dBi
```

**Patch rectangulaire** :
```
L ≈ λ/(2√εreff) - 2ΔL
W ≈ λ/(2√((εr+1)/2))
```

**Friis et FSPL** :
```
FSPL (dB) = 32.45 + 20log(f_MHz) + 20log(d_km)
Pr (dBm) = Pt(dBm) + Gt(dBi) + Gr(dBi) - FSPL(dB)
```

**Horizon radio** :
```
d (km) ≈ 4.12 × [√h1(m) + √h2(m)]
```

**Zone de Fresnel** :
```
r (m) = √(λ × d1 × d2 / (d1 + d2))
```

### Tableau récapitulatif des antennes

| Type | Gain (dBi) | Bande passante | Encombrement | Coût | Applications |
|------|------------|----------------|--------------|------|--------------|
| Dipôle λ/2 | 2.15 | 5-10% | Moyen | Très faible | FM, WiFi simple, mesure |
| Monopole λ/4 | 5.15 | 5-10% | Faible | Très faible | GSM, radio mobile |
| Patch rectangulaire | 6-8 | 2-5% | Très faible | Faible | GPS, WiFi, IoT, drones |
| Yagi 3 éléments | 6-8 | 3-5% | Moyen | Faible | WiFi directif, TNT |
| Yagi 10 éléments | 13-15 | 2-3% | Élevé | Moyen | Liaison longue distance |
| Log-périodique | 6-10 | > 100% | Élevé | Moyen | Mesure, EMC |
| Cornet | 10-25 | 10-30% | Moyen | Moyen | Radar, micro-ondes |
| Parabole | 20-40 | 10-20% | Très élevé | Élevé | Satellite, radar |

### Bandes de fréquences et longueurs d'onde

| Bande | Fréquence | λ | Applications typiques |
|-------|-----------|---|----------------------|
| FM Radio | 88-108 MHz | 2.8-3.4 m | Radio FM, RDS |
| VHF Aéro | 108-137 MHz | 2.2-2.8 m | Communications aéronautiques |
| VHF Maritime | 156-174 MHz | 1.7-1.9 m | Maritime VHF |
| TNT (UHF TV) | 470-862 MHz | 35-64 cm | Télévision numérique terrestre |
| GSM 900 | 890-960 MHz | 31-34 cm | 2G mobile |
| LoRa EU | 863-870 MHz | 34-35 cm | IoT longue portée |
| RFID UHF | 865-868 MHz (EU) | 34-35 cm | Logistique, inventaire |
| GPS L1 | 1575 MHz | 19 cm | Navigation GNSS |
| GSM 1800 (DCS) | 1710-1880 MHz | 16-17.5 cm | 2G/4G mobile |
| WiFi 2.4G | 2.4-2.5 GHz | 12-12.5 cm | WiFi b/g/n, Bluetooth |
| 4G LTE | 2.6 GHz | 11.5 cm | 4G mobile |
| WiMAX | 3.5 GHz | 8.6 cm | Accès fixe sans fil |
| WiFi 5G | 5.15-5.85 GHz | 5.1-5.8 cm | WiFi a/n/ac/ax |
| 5G mmWave | 26-28 GHz | 1.1-1.2 cm | 5G haut débit |

---

<div style="text-align: center; margin: 40px 0; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 10px;">
  <h3 style="margin-top: 0;">🎯 Points clés à retenir</h3>
  <p><strong>1.</strong> Une antenne est un transducteur entre onde guidée (câble) et onde libre (espace) - son efficacité dépend de l'adaptation d'impédance et du rayonnement.</p>
  <p><strong>2.</strong> Le compromis gain/bande passante/encombrement est incontournable : choisir le type d'antenne selon l'application.</p>
  <p><strong>3.</strong> La simulation EM est indispensable avant fabrication, mais doit être validée par mesure expérimentale.</p>
  <p><strong>4.</strong> En propagation réelle, les phénomènes multi-trajets et l'environnement complexifient le bilan de liaison - prévoir des marges.</p>
  <p><strong>5.</strong> Les antennes sont au cœur de la révolution IoT/5G/satellite : un domaine d'avenir avec de nombreuses opportunités.</p>
</div>

---

*Ce cours a été dispensé au semestre 4 du DUT GEII à l'INSA Toulouse (2021-2022).*

#### Paramètres caractéristiques

**Diagramme de rayonnement :**
- Représentation 2D et 3D
- Lobe principal
- Lobes secondaires
- Ouverture à -3dB
- Rapport avant/arrière (F/B)

**Directivité et gain :**
- Directivité D (dBi)
- Gain G (dBi)
- Efficacité η
- G = η × D

**Polarisation :**
- Linéaire (H, V)
- Circulaire (RHCP, LHCP)
- Elliptique
- Rapport axial (AR)

**Impédance d'entrée :**
- Partie réelle et imaginaire
- Adaptation 50Ω
- Bande passante d'adaptation
- TOS (SWR)

**Bande passante :**
- Bande d'adaptation (S11 < -10dB)
- Bande de rayonnement
- Bande de polarisation

#### Équation de Friis
$$P_r = P_t \cdot G_t \cdot G_r \cdot \left(\frac{\lambda}{4\pi d}\right)^2$$

- Puissance transmise/reçue
- Gains des antennes
- Distance
- Pertes en espace libre

### Types d'antennes

#### Antennes filaires

**Dipôle demi-onde (λ/2) :**
- Structure simple
- Impédance ≈ 73Ω
- Diagramme omnidirectionnel (plan H)
- Directivité 2.15 dBi

**Dipôle replié :**
- Impédance ≈ 300Ω
- Bande passante améliorée
- Utilisé en TV

**Monopole quart d'onde (λ/4) :**
- Nécessite plan de masse
- Impédance ≈ 36.5Ω
- Omnidirectionnel
- Utilisé en mobile, WiFi

**Antenne Yagi-Uda :**
- Éléments parasites (réflecteur, directeurs)
- Directive
- Gain 6-17 dBi
- TV, radioamateur

#### Antennes imprimées (patch)

**Patch rectangulaire :**
- Sur substrat diélectrique
- Compact et léger
- Alimentation (coaxiale, microstrip, fente)
- Gain 6-8 dBi
- Applications : GPS, WiFi, télémétrie

**Dimensions :**
- Longueur L ≈ λg/2
- Largeur W (influence impédance)
- Épaisseur substrat h
- Permittivité εr

**Avantages :**
- Fabrication PCB standard
- Faible profil
- Intégration facile
- Faible coût

**Inconvénients :**
- Bande passante étroite (2-5%)
- Efficacité moyenne
- Pertes diélectriques

#### Antennes large bande

**Antenne log-périodique :**
- Large bande (rapport 10:1)
- Gain modéré constant
- Encombrement important

**Antenne spirale :**
- Polarisation circulaire
- Large bande
- Applications militaires, GNSS

**Antenne biconique :**
- Ultra large bande
- Omnidirectionnelle
- Mesure et EMC

#### Antennes spéciales

**Antenne cornet :**
- Alimentée par guide d'onde
- Gain élevé (10-25 dBi)
- Micro-ondes, radar

**Réseau d'antennes (Array) :**
- Éléments multiples
- Déphasage contrôlé
- Balayage électronique
- Gain élevé

**Antenne RFID :**
- Proximité ou longue portée
- Polarisation circulaire souvent
- Bande UHF (865-868 MHz EU, 902-928 MHz US)

### Propagation des ondes

#### Modes de propagation

**Onde de sol :**
- Basses fréquences (VLF, LF, MF)
- Suit la courbure terrestre
- Atténuation croissante avec fréquence

**Onde de surface :**
- Contact avec le sol
- Faible portée
- AM radio

**Onde d'espace :**
- Directe + réfléchie
- Interférences (fading)
- VHF, UHF

**Onde ionosphérique :**
- Réflexion sur ionosphère
- HF (3-30 MHz)
- Longue distance
- Dépend heure/saison

#### Phénomènes de propagation

**Réflexion :**
- Sur sol, bâtiments, obstacles
- Coefficient de réflexion
- Multi-trajets

**Diffraction :**
- Contournement d'obstacles
- Zone de Fresnel
- Atténuation knife-edge

**Réfraction :**
- Changement de milieu
- Courbure du trajet
- Ducting atmosphérique

**Absorption :**
- Pluie (atténuation forte >10 GHz)
- Végétation
- Atmosphère (O2, H2O)

#### Modèles de propagation

**Espace libre :**
- Formule de Friis
- Ligne de vue (LOS)

**Okumura-Hata :**
- Environnement urbain
- 150 MHz - 1.5 GHz

**COST-231 :**
- Extension Okumura-Hata
- Jusqu'à 2 GHz

**Modèle à deux rayons :**
- Rayon direct + réfléchi
- Zone d'interférence

## 🛠️ Travaux pratiques

### TP Simulation d'antennes

**Logiciels utilisés :**
- MMANA-GAL (Yagi)
- CST Microwave Studio
- HFSS
- 4NEC2

**Antennes simulées :**
- Dipôle λ/2
- Yagi 3-5 éléments
- Patch rectangulaire
- Monopole sur plan de masse

**Paramètres analysés :**
- S11 (adaptation)
- Diagramme de rayonnement
- Gain et directivité
- Impédance d'entrée

### TP Mesures d'antennes

**Chambre anéchoïque :**
- Environnement sans réflexions
- Mesure de diagrammes
- Polarisation
- Gain absolu

**Mesure adaptation :**
- Analyseur de réseau (VNA)
- S11, TOS
- Impédance complexe

### TP Bilan de liaison

**Radio Mobile :**
- Logiciel de planification
- Modèle numérique terrain (MNT)
- Calcul de couverture
- Profil de liaison

**Scénarios étudiés :**
- Liaison point-à-point
- Couverture WiFi campus
- Liaison longue distance

### Projet Antenne

**Réalisation d'une antenne :**
- Choix du type (patch, Yagi, etc.)
- Dimensionnement théorique
- Simulation et optimisation
- Fabrication (PCB ou mécanique)
- Mesures et validation

## 💻 Outils utilisés

### Simulation EM
- **MMANA-GAL** : Antennes filaires (Yagi)
- **4NEC2** : Méthode des moments (NEC-2)
- **CST Microwave Studio** : 3D complet
- **HFSS** : FEM 3D
- **FEKO** : Large structures

### Planification radio
- **Radio Mobile** : Couverture et bilans
- **Google Earth** : Visualisation 3D
- **Splat!** : Open source propagation

### Mesure
- **Analyseur de réseau** : S11, impédance
- **Chambre anéchoïque** : Rayonnement
- **Analyseur de spectre** : Puissance rayonnée

## 📊 Évaluation

- Travaux pratiques (30%)
- Projet antenne (40%)
- Contrôle continu (15%)
- Examen final (15%)

## 🔗 Liens avec d'autres cours

- **Propagation et Hyperfréquences (S3)** : Fondements
- **Circuits Hyperfréquences** : Adaptation, alimentation
- **Télécommunications** : Systèmes de communication
- **ER** : Intégration antennes

## 📐 Formules de dimensionnement

### Dipôle λ/2
- Longueur physique : L ≈ 0.95 × λ/2
- Impédance : Z ≈ 73 + j42.5 Ω

### Patch rectangulaire
- Longueur : $L = \frac{c}{2f_r\sqrt{\varepsilon_{reff}}} - 2\Delta L$
- Largeur : $W = \frac{c}{2f_r}\sqrt{\frac{2}{\varepsilon_r + 1}}$

### Gain théorique
- Dipôle λ/2 : 2.15 dBi
- Patch : 6-8 dBi
- Yagi 3 éléments : 6-8 dBi
- Yagi 10 éléments : 13-15 dBi

## 💡 Applications pratiques

### Communications
- WiFi (2.4 GHz, 5 GHz)
- Bluetooth
- 4G/5G
- LoRa, Sigfox

### Navigation
- GPS, Galileo, GLONASS
- Antennes patch circulaires
- Polarisation circulaire

### Télédétection
- Radar
- Satellites
- Télémétrie

### RFID
- Proximité (13.56 MHz)
- Longue portée (UHF)
- Applications logistique

## 📖 Compétences développées

- Conception d'antennes
- Simulation électromagnétique
- Mesure et caractérisation
- Bilans de liaison radio
- Optimisation de structures rayonnantes
- Analyse de propagation

## 🎯 Bandes de fréquences courantes

| Bande | Fréquence | λ | Applications |
|-------|-----------|---|--------------|
| FM | 88-108 MHz | 2.8-3.4 m | Radio FM |
| VHF TV | 174-223 MHz | 1.3-1.7 m | TV analogique |
| UHF TV | 470-862 MHz | 35-64 cm | TNT |
| GSM 900 | 900 MHz | 33 cm | 2G mobile |
| GPS L1 | 1575 MHz | 19 cm | Navigation |
| DCS 1800 | 1800 MHz | 16.7 cm | 2G/4G mobile |
| WiFi 2.4G | 2.4 GHz | 12.5 cm | WiFi b/g/n |
| WiFi 5G | 5.8 GHz | 5.2 cm | WiFi a/n/ac |

## ⚠️ Pièges en conception

### Antennes patch
- Bande passante étroite
- Sensible à l'épaisseur substrat
- Pertes diélectriques à haute fréquence
- Rayonnement arrière

### Antennes filaires
- Plan de masse essentiel (monopole)
- Environnement influence performances
- Câble d'alimentation rayonne
- Effets de proximité

### Mesures
- Couplage mutuel entre antennes
- Réflexions en chambre
- Câbles et connecteurs (pertes)
- Adaptation impédance

## 🔧 Conseils pratiques

### Réalisation PCB
- Substrat bas εr pour patch (Rogers)
- Précision d'usinage importante
- Via de masse multiples
- Protection vernis si extérieur

### Tests terrain
- Hauteur d'antenne critique
- Dégagement zone de Fresnel
- Orientation et polarisation
- Mesure RSSI, SNR

### Optimisation
- Simulation avant fabrication
- Itérations de design
- Compromis gain/bande passante
- Coût vs performances

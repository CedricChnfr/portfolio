---
layout: default
title: "Fondements Électronique Numérique - S5"
date: 2024-10-02 10:56:03 +0200
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

# 🔢 Fondements Électronique Numérique - S5

**Année**: 2022-2023 (Semestre 5)  
**Crédits**: 3 ECTS  
**Type**: Électronique Numérique

---

## PART A: PRÉSENTATION GÉNÉRALE

### Objectifs du cours

Le cours "Fondements Électronique Numérique" constitue une introduction complète à l'électronique numérique, couvrant les technologies des circuits logiques (TTL, CMOS), la conception de circuits combinatoires et séquentiels, ainsi que la conversion de données analogique-numérique (ADC/DAC). Ce cours est fondamental pour comprendre le fonctionnement des systèmes numériques modernes, des microprocesseurs aux systèmes embarqués, en passant par les interfaces de capteurs et les systèmes d'acquisition de données.

### Compétences visées

- Maîtriser les technologies de circuits logiques (TTL, CMOS) et leurs caractéristiques
- Concevoir des circuits combinatoires (décodeurs, multiplexeurs, comparateurs)
- Concevoir et analyser des circuits séquentiels (compteurs, registres, machines d'états)
- Comprendre les principes de conversion ADC et DAC
- Analyser les contraintes temporelles (timing, setup/hold, métastabilité)
- Dimensionner et interfacer des convertisseurs de données
- Maîtriser les outils de simulation et de conception numérique

### Organisation

- **Volume horaire**: 32h (CM: 18h, TD: 10h, TP: 4h)
- **Évaluation**: Examen final (60%) + TDs (20%) + TPs/Projets (20%)
- **Semestre**: 5 (2022-2023)
- **Prérequis**: Électronique fondamentale, algèbre de Boole, systèmes de numération

---

## PART B: EXPÉRIENCE, CONTEXTE ET FONCTION

### Contenu pédagogique

Le cours s'articule autour de quatre axes principaux: les technologies logiques, les compteurs, les convertisseurs ADC/DAC, et les aspects pratiques.

#### 1. Technologies des Circuits Logiques: TTL et CMOS

##### A. Représentation des Signaux Numériques

**Niveaux logiques**:

Un signal numérique ne prend que deux états:
- **État HAUT** (HIGH, '1', TRUE): tension élevée
- **État BAS** (LOW, '0', FALSE): tension faible

**Seuils logiques**:

Pour garantir l'immunité au bruit, on définit des plages de tension:

| État | TTL | CMOS 5V |
|------|-----|---------|
| V_OH (Output High min) | 2.4V | 4.4V |
| V_IH (Input High min) | 2.0V | 3.5V |
| V_IL (Input Low max) | 0.8V | 1.5V |
| V_OL (Output Low max) | 0.4V | 0.5V |

**Marge de bruit (Noise Margin)**:

NM_H = V_OH - V_IH

NM_L = V_IL - V_OL

Pour TTL: NM_H = 2.4 - 2.0 = 0.4V, NM_L = 0.8 - 0.4 = 0.4V

Pour CMOS 5V: NM_H = 4.4 - 3.5 = 0.9V, NM_L = 1.5 - 0.5 = 1.0V

**Conclusion**: CMOS a une meilleure immunité au bruit que TTL.

##### B. Technologie TTL (Transistor-Transistor Logic)

**Structure d'une porte NAND TTL**:

La porte TTL utilise des transistors bipolaires NPN.

**Caractéristiques principales**:

- **Alimentation**: V_CC = 5V ± 5% (critique!)
- **Courants**:
  - Courant de sortie HIGH: I_OH = -0.4mA (source)
  - Courant de sortie LOW: I_OL = 16mA (sink)
  - Courant d'entrée HIGH: I_IH = 40µA
  - Courant d'entrée LOW: I_IL = -1.6mA

**Fan-out** (coefficient de charge):

Fan-out = min(I_OL / |I_IL|, I_OH / I_IH)

Pour TTL standard:

Fan-out = min(16mA / 1.6mA, 0.4mA / 0.04mA) = min(10, 10) = 10

Une sortie TTL peut commander 10 entrées TTL.

**Familles TTL**:

| Famille | Nom | t_pd (ns) | P_diss (mW) | Produit P × t |
|---------|-----|---------------|-----------------|----------------------|
| 74xx | Standard | 10 | 10 | 100 pJ |
| 74LSxx | Low-power Schottky | 9 | 2 | 18 pJ |
| 74Sxx | Schottky | 3 | 19 | 57 pJ |
| 74ASxx | Advanced Schottky | 1.5 | 8 | 12 pJ |
| 74ALSxx | Advanced LS | 4 | 1 | 4 pJ |

**LS-TTL** (Low-power Schottky): meilleur compromis vitesse/consommation.

**Temps de propagation**:

t_pd = (t_pHL + t_pLH) / 2

où:
- t_pHL: temps de propagation HIGH → LOW
- t_pLH: temps de propagation LOW → HIGH

**Entrées non connectées**:

⚠️ **Attention**: une entrée TTL non connectée est considérée comme HIGH (tirée vers V_CC par résistance interne).

Cependant, il est **fortement recommandé** de connecter explicitement les entrées inutilisées:
- À V_CC via résistance 1-10kΩ pour forcer HIGH
- À GND pour forcer LOW
- Regroupées avec d'autres entrées utilisées

##### C. Technologie CMOS (Complementary MOS)

**Structure d'un inverseur CMOS**:

Utilise un transistor PMOS (pull-up) et un NMOS (pull-down) en série.

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S5/elec-num/porte-and.svg" alt="Porte logique AND" style="max-width: 300px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Exemple de porte logique AND - Base de l'électronique numérique</p>
</div>

**Avantages du CMOS**:
- **Consommation statique quasi-nulle**: courant uniquement pendant les transitions
- **Large plage d'alimentation**: 3V à 18V selon la famille
- **Forte immunité au bruit**: seuils proches de V_DD et GND
- **Fan-out élevé**: sortie en tension (impédance élevée)
- **Symétrie**: t_pHL ≈ t_pLH

**Inconvénients**:
- **Sensibilité aux décharges électrostatiques** (ESD)
- **Latchup**: phénomène destructeur si dépassement des rails d'alimentation

**Consommation dynamique**:

P_dyn = C_L × V_DD² × f

où:
- C_L: capacité de charge
- f: fréquence de commutation

**Familles CMOS**:

| Famille | Description | V_DD | Vitesse |
|---------|-------------|----------|---------|
| 4000B | CMOS standard | 3-18V | Lent (250ns) |
| 74HCxx | High-speed CMOS | 2-6V | Moyen (25ns) |
| 74HCTxx | HC compatible TTL | 5V | Moyen (25ns) |
| 74ACxx | Advanced CMOS | 2-6V | Rapide (10ns) |
| 74ACTxx | AC compatible TTL | 5V | Rapide (10ns) |
| 74LVxx | Low Voltage | 1.65-5.5V | Rapide |

**HC vs HCT**:
- **HC**: seuils CMOS purs (V_IH = 0.7 × V_DD)
- **HCT**: seuils compatibles TTL (V_IH ≈ 2V)

**Entrées non connectées**:

⚠️ **CMOS**: une entrée flottante est **interdite** (risque de consommation excessive, oscillations, latchup).

**Obligatoire**: connecter toutes les entrées inutilisées à V_DD ou GND.

##### D. Interfaçage TTL ↔ CMOS

**TTL → CMOS**:

Problème: V_OH(TTL) = 2.4V peut être < V_IH(HC) = 3.5V (pour V_DD = 5V)

**Solutions**:
1. Utiliser CMOS **HCT** (compatible TTL)
2. Pull-up resistor: ajouter résistance 1-10kΩ vers V_DD

**CMOS → TTL**:

Problème: courant de sortie CMOS limité.

**Vérification**:
- CMOS HC peut fournir I_OH = 4mA → suffit pour quelques portes TTL
- Pour fan-out élevé: utiliser buffer CMOS 74HC244 ou 74ACT244

**Résistances de pull-up/pull-down**:

**Pull-up** (forcer HIGH):
```
        VDD
         |
        [R] (1-10kΩ)
         |
     ----+---- Signal
```

**Pull-down** (forcer LOW):
```
     ----+---- Signal
         |
        [R] (1-10kΩ)
         |
        GND
```

Valeur typique: 4.7kΩ ou 10kΩ.

**Support de cours**: [Technologie des circuits logiques](/cours-pdf/S5/Elec-Num/Technologie-circuits-logiques.pdf)

#### 2. Compteurs Numériques

##### A. Principe et Types

Un **compteur** est un circuit séquentiel qui parcourt une suite d'états selon les impulsions d'horloge.

**Types de compteurs**:
- **Asynchrone** (ripple counter): bascules en cascade, propagation séquentielle
- **Synchrone**: toutes les bascules commandées simultanément par l'horloge

**Compteur asynchrone**:

Avantages: simple, peu de portes
Inconvénients: lent (temps de propagation cumulé), glitches

**Compteur synchrone**:

Avantages: rapide, pas de glitches
Inconvénients: logique de commande plus complexe

##### B. Compteur Modulo-N

**Modulo-N**: compte de 0 à N-1, puis revient à 0.

**Nombre de bascules nécessaires**:

n = ⌈log₂(N)⌉

**Exemples**:
- Modulo-8: 3 bascules (2³ = 8)
- Modulo-10: 4 bascules (2⁴ = 16, mais on limite à 10)
- Modulo-16: 4 bascules (2⁴ = 16)

**Compteur BCD (Binary Coded Decimal)**:

Compteur modulo-10 qui compte de 0000 à 1001 (0 à 9 en décimal).

##### C. Conception d'un Compteur Synchrone

**Méthode de conception**:

1. **Diagramme d'états**: définir les états et transitions
2. **Table de vérité**: état présent → état suivant
3. **Équations logiques**: simplifier avec Karnaugh
4. **Implémentation**: bascules + portes logiques

**Exemple: Compteur synchrone modulo-8 (3 bits)**

États: Q₂ Q₁ Q₀ de 000 à 111

**Avec bascules D**:

D_i = Q_i(next)

Table de vérité:

| Q₂ | Q₁ | Q₀ | D₂ | D₁ | D₀ |
|-------|-------|-------|-------|-------|-------|
| 0 | 0 | 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 | 1 | 1 |
| 0 | 1 | 1 | 1 | 0 | 0 |
| 1 | 0 | 0 | 1 | 0 | 1 |
| 1 | 0 | 1 | 1 | 1 | 0 |
| 1 | 1 | 0 | 1 | 1 | 1 |
| 1 | 1 | 1 | 0 | 0 | 0 |

**Équations** (après simplification Karnaugh):

D₀ = NON(Q₀)

D₁ = Q₁ XOR Q₀

D₂ = Q₂ XOR (Q₁ ET Q₀)

**Compteur avec remise à zéro (RESET)**:

Ajout d'une entrée asynchrone RESET (active HIGH ou LOW) pour forcer tous les Q_i à 0.

##### D. Compteur Modulo-N avec Détection

**Méthode par détection**:

Pour un compteur modulo-N:
1. Utiliser compteur 2ⁿ (où 2ⁿ ≥ N)
2. Détecter l'état N avec une porte logique
3. Forcer la remise à zéro (RAZ)

**Exemple: Compteur décimal (modulo-10)**

Détection de l'état 10 (1010):

RAZ = Q₃ ET NON(Q₂) ET Q₁ ET NON(Q₀)

Dès que 1010 est atteint, le compteur revient à 0000.

**Problème**: glitch transitoire à l'état 10 (quelques nanosecondes).

**Solution**: RAZ synchrone (attendre le prochain front d'horloge).

##### E. Applications des Compteurs

**Division de fréquence**:

Un compteur modulo-N divise la fréquence d'horloge par N.

f_out = f_CLK / N

**Exemple**: Horloge 1MHz, compteur modulo-1000 → sortie 1kHz

**Générateur de signaux**:
- Compteur + décodeur → signaux périodiques
- Séquenceur pour commande de systèmes

**Mesure de fréquence**:
- Compter les impulsions pendant une durée fixe (porte de temps)

**Support de cours**: [Chronogrammes compteur](/cours-pdf/S5/Elec-Num/chronogrammes-compteur.pdf)

#### 3. Convertisseurs Analogique-Numérique (ADC) et Numérique-Analogique (DAC)

##### A. Conversion Numérique → Analogique (DAC)

**Principe**:

Un DAC convertit un mot binaire de N bits en tension analogique proportionnelle.

V_out = V_ref × (D / 2ᴺ)

où:
- V_ref: tension de référence
- D: valeur numérique d'entrée (0 à 2ᴺ - 1)
- N: nombre de bits (résolution)

**Résolution**:

LSB = V_ref / 2ᴺ

**Exemple**: DAC 8 bits, V_ref = 5V

LSB = 5 / 256 = 19.53mV

Pour D = 128 (10000000):

V_out = 5 × (128 / 256) = 2.5V

##### B. Architectures de DAC

**DAC à résistances pondérées**:

```
      2R    R    R/2  R/4
Bit0 --|>|--+    |    |
Bit1 --|>|-------+    |
Bit2 --|>|------------+
Bit3 --|>|-----------------+--- [AO] → Vout
                            |
                           GND
```

Problème: large plage de valeurs de résistances (difficile à fabriquer avec précision).

**DAC R-2R (échelle de résistances)**:

Utilise uniquement deux valeurs de résistances: R et 2R.

```
        2R      2R      2R      2R
    +---/\/\----/\/\----/\/\----/\/\---GND
    |        |       |       |
Bit3|       R|      R|      R|      R
    |        |       |       |       |
   [S3]    [S2]    [S1]    [S0]    [AO] → Vout
    |        |       |       |       |
   GND      GND     GND     GND     GND
```

**Avantages**:
- Seulement 2 valeurs de résistances
- Précision élevée
- Facile à intégrer

**DAC à sources de courant**:

Utilise des sources de courant pondérées commutées.

Avantages: très rapide (DAC vidéo, RF)

##### C. Spécifications des DAC

**Linéarité**:

- **DNL** (Differential Non-Linearity): écart entre deux codes adjacents vs LSB idéal
  - DNL < 0.5 LSB: acceptable
  - DNL > 1 LSB: codes manquants possibles

- **INL** (Integral Non-Linearity): écart cumulé par rapport à la droite idéale
  - INL < 1 LSB: bonne linéarité

**Temps de stabilisation (settling time)**:

Temps pour que la sortie atteigne sa valeur finale ± 0.5 LSB après un changement de code.

Typiquement: 100ns à 10µs selon le DAC.

**Glitch**:

Transitoire bref lors du changement de code (surtout pour changement de bit majeur).

**Exemple**: 01111111 → 10000000 (127 → 128)

Tous les bits changent → glitch important.

**Solution**: latch + commutation synchrone.

##### D. Conversion Analogique → Numérique (ADC)

**Principe**:

Un ADC convertit une tension analogique en mot binaire de N bits.

D = arrondi(V_in / V_ref × 2ᴺ)

**Quantification**:

La conversion introduit une erreur de quantification:

ε_q = ± LSB/2 = ± V_ref / 2^(N+1)

**Rapport Signal/Bruit de quantification**:

SNR_q = 6.02 × N + 1.76 dB

**Exemple**: ADC 12 bits

SNR_q = 6.02 × 12 + 1.76 = 74 dB

**ENOB** (Effective Number of Bits):

ENOB = (SNR_measured - 1.76) / 6.02

Tient compte des non-linéarités réelles.

##### E. Architectures d'ADC

**ADC Flash (parallèle)**:

Le plus rapide: conversion en 1 cycle d'horloge.

**Principe**: N bits nécessitent 2ᴺ - 1 comparateurs.

**Exemple**: ADC 8 bits → 255 comparateurs!

**Avantages**: très rapide (ns)
**Inconvénients**: complexité exponentielle, consommation élevée, limité à 8-10 bits

**Applications**: oscilloscopes numériques, radar, SDR

**ADC à Approximations Successives (SAR)**:

Principe: dichotomie (recherche binaire).

**Algorithme**:
1. Essayer MSB = 1 → comparer avec DAC interne
2. Si V_in > V_DAC: garder MSB = 1, sinon MSB = 0
3. Répéter pour tous les bits (MSB → LSB)

**Temps de conversion**: N cycles d'horloge (N = nombre de bits)

**Exemple**: ADC 12 bits, f_CLK = 10MHz

t_conv = 12 / 10⁷ = 1.2 µs

**Avantages**: 
- Bon compromis vitesse/précision/coût
- Faible consommation
- Résolution jusqu'à 18-20 bits

**Inconvénients**: vitesse limitée (typiquement 100ksps - 10Msps)

**Applications**: acquisition de données, capteurs, systèmes embarqués

**ADC à double rampe (dual-slope)**:

**Principe**:
1. Intégrer V_in pendant temps fixe T₁
2. Décharger avec -V_ref et mesurer le temps T₂

V_in = V_ref × (T₂ / T₁)

**Avantages**:
- Très précis (résolution 16-24 bits)
- Rejet du bruit 50/60Hz (intégration)
- Linéarité excellente

**Inconvénients**: très lent (10-100 conversions/s)

**Applications**: multimètres, instrumentation de précision

**ADC Sigma-Delta (ΣΔ)**:

**Principe**: sur-échantillonnage + filtrage numérique + décimation

**Avantages**:
- Résolution très élevée (16-24 bits)
- Filtre anti-repliement simple (1er ordre)
- Faible coût (analogique simple)

**Inconvénients**: latence élevée (filtrage numérique)

**Applications**: audio (CD, DAC audio), capteurs de précision, pesage

##### F. Théorème d'Échantillonnage de Shannon-Nyquist

**Théorème**:

Pour échantillonner un signal de fréquence maximale f_max sans perte d'information:

f_sampling ≥ 2 × f_max

La fréquence de Nyquist est f_N = 2 × f_max.

**Aliasing (repliement spectral)**:

Si f_sampling < 2 f_max, les hautes fréquences se "replient" dans le spectre basse fréquence → distorsion irréversible.

**Solution**: filtre anti-repliement (passe-bas analogique) avant l'ADC.

**Exemple**:

Signal audio 20kHz → f_sampling ≥ 40kHz

En pratique: CD audio = 44.1kHz (marge de 10%)

**Filtre anti-repliement**: Butterworth ou Bessel, f_c = 20kHz, ordre 4-8.

##### G. Paramètres Importants des ADC

**Résolution**: nombre de bits (8, 10, 12, 16, 24 bits)

**Taux d'échantillonnage** (sampling rate): échantillons par seconde (sps)
- ksps: kilosamples/s
- Msps: megasamples/s

**Temps d'acquisition** (t_acq): temps pour charger le condensateur d'échantillonnage

**Temps de conversion** (t_conv): temps pour effectuer la conversion

**Débit total** (throughput):

f_max = 1 / (t_acq + t_conv)

**Aperture jitter**: incertitude temporelle de l'échantillonnage

Dégrade le SNR:

SNR_jitter = -20 log₁₀(2π f_in × t_jitter)

**Exemple**: Signal 1MHz, jitter 1ns

SNR_jitter = -20 log₁₀(2π × 10⁶ × 10⁻⁹) = 74 dB

Limite ENOB à ~12 bits.

**Support de cours**: [TD CAN-CNA](/cours-pdf/S5/Elec-Num/TD-IMACS-NUM-CAN.pdf)

#### 4. Aspects Temporels et Synchronisation

##### A. Contraintes Temporelles des Bascules

**Setup time** (t_setup): temps minimum stable AVANT le front d'horloge

**Hold time** (t_hold): temps minimum stable APRÈS le front d'horloge

```
      ___________
CLK _|           |______
        ↑
   _____|______|______
D  ____X======X_______
      <--> <-->
      tsu  th
```

**Violation de setup**: donnée change trop près du front d'horloge

**Violation de hold**: donnée change trop tôt après le front

**Conséquence**: état indéterminé, métastabilité possible.

##### B. Métastabilité

**Phénomène**:

Si les contraintes t_setup ou t_hold ne sont pas respectées, la bascule peut entrer dans un état métastable (ni 0 ni 1) pendant un temps imprévisible.

**Probabilité de métastabilité**:

P_meta = (T₀ × f_CLK × f_data) / exp(t_res/τ)

où:
- T₀, τ: constantes du composant
- t_res: temps de résolution disponible
- f_CLK, f_data: fréquences

**Mitigation**:

1. **Synchroniseur à double bascule**: 2 bascules en série
   - Réduit drastiquement P_meta (typiquement < 10⁻¹²)
   
2. **MTBF** (Mean Time Between Failures):

   MTBF = exp(t_res/τ) / (T₀ × f_CLK × f_data)
   
   Objectif: MTBF > durée de vie du système (ex: 100 ans)

**Exemple**:

f_CLK = 100MHz, f_data = 1MHz, synchroniseur 2 étages

MTBF ≈ 10¹⁵ s ≈ 30 millions d'années

##### C. Clock Skew et Jitter

**Clock skew**: décalage temporel entre l'arrivée de l'horloge sur différentes bascules

Causes: longueur de pistes, délais de buffers

**Impact**: peut causer violations de setup/hold

**Clock jitter**: variation aléatoire de la période d'horloge

Causes: bruit, PLL, alimentation

**Budget temporel**:

T_CLK > t_pd(logic) + t_setup + t_skew + t_jitter

où t_pd(logic) est le délai combinatoire entre bascules.

**Fréquence maximale**:

f_max = 1 / (t_pd(logic) + t_setup + t_skew + t_jitter)

##### D. Distribution d'Horloge

**Techniques**:

1. **Clock tree**: arbre équilibré de buffers
2. **H-tree**: distribution en forme de H pour égaliser les délais
3. **PLL** (Phase-Locked Loop): génération et multiplication de fréquence
4. **Clock gating**: désactivation conditionnelle (économie d'énergie)

**Règles de conception**:

- Minimiser le skew (<5% de la période)
- Buffers symétriques
- Pistes d'horloge courtes et larges (faible impédance)
- Découplage sur chaque buffer (C = 100nF)

---

## PART C: ASPECTS TECHNIQUES

### Exercices de TD

#### TD1: Interfaçage TTL-CMOS

**Exercice**: Interfacer une sortie TTL LS avec une entrée CMOS HC alimentée en 5V.

**Données**:
- 74LS00: V_OH(min) = 2.7V, I_OH = -0.4mA
- 74HC00: V_IH(min) = 3.5V (à V_DD = 5V)

**Problème**: V_OH(TTL) < V_IH(CMOS) → état HIGH non garanti!

**Solution 1**: Résistance de pull-up

```
         VDD (5V)
          |
         [R] 4.7kΩ
          |
TTL OUT --+---- CMOS IN
```

**Calcul de R**:

Courant minimal pour garantir V_IH = 3.5V:

I_pull-up = (V_DD - V_IH) / R > |I_IH(CMOS)|

Pour CMOS: I_IH ≈ 1µA (négligeable)

Contrainte TTL: la résistance ne doit pas surcharger la sortie TTL.

I_pull-up < I_OH(max) = 0.4mA

R > (V_DD - V_OH(TTL)) / I_OH = (5 - 2.7) / (0.4 × 10⁻³) = 5.75kΩ

**Choix**: R = 10kΩ (compromis vitesse/courant)

**Solution 2**: Utiliser CMOS **HCT** (compatible TTL)

74HCT00: V_IH(min) = 2.0V → compatible directement avec TTL!

#### TD2: Dimensionnement de Compteur

**Exercice**: Concevoir un compteur pour générer un signal 1kHz à partir d'une horloge 1MHz.

**Solution**:

N = f_CLK / f_out = 1MHz / 1kHz = 1000

Il faut un compteur **modulo-1000**.

**Nombre de bascules**:

n = ⌈log₂(1000)⌉ = 10 bascules

**Implémentation**:

Compteur 10 bits (0 à 1023) avec détection de l'état 1000 et remise à zéro.

**Avec circuits intégrés**:

Option 1: 2× compteur décimal 74HC390 (modulo-100 chacun)

N = 10 × 100 = 1000 ✓

Option 2: 3× compteur décimal 74HC160 (modulo-10 chacun)

N = 10 × 10 × 10 = 1000 ✓

**Chronogramme**:

```
CLK (1MHz)   __|‾|_|‾|_|‾|_|‾|_|‾|_...
             <---- 1µs ---->

OUT (1kHz)   ‾‾‾‾‾‾‾‾‾‾|___________|‾‾‾‾‾‾‾‾‾‾
             <------- 1ms -------->
```

#### TD3: Calcul de Conversion ADC

**Exercice**: ADC 12 bits, V_ref = 3.3V, fréquence d'échantillonnage 100ksps.

**Questions**:

**1) Résolution (LSB)**:

LSB = V_ref / 2¹² = 3.3 / 4096 = 0.805 mV

**2) Erreur de quantification maximale**:

ε_q(max) = ± LSB/2 = ± 0.403 mV

**3) Code numérique pour V_in = 1.65V**:

D = arrondi((V_in / V_ref) × 2¹²) = arrondi((1.65 / 3.3) × 4096) = arrondi(2048) = 2048

En hexadécimal: 2048₁₀ = 0x800

**4) Plage de tension correspondant au code 2048**:

V_min = ((2048 - 0.5) / 4096) × 3.3 = 1.649V

V_max = ((2048 + 0.5) / 4096) × 3.3 = 1.651V

**5) SNR théorique**:

SNR = 6.02 × 12 + 1.76 = 74 dB

**6) Fréquence maximale du signal d'entrée** (critère de Nyquist):

f_max = f_sampling / 2 = 100kHz / 2 = 50kHz

En pratique, avec filtre anti-repliement: f_max ≈ 40kHz (marge 20%).

**7) Temps de conversion maximal** pour 100ksps:

t_conv(max) = 1 / 100kHz = 10 µs

#### TD4: Conception de DAC R-2R

**Exercice**: Concevoir un DAC R-2R 4 bits avec V_ref = 5V.

**Schéma**:

```
        2R      2R      2R      2R
    +---/\/\----/\/\----/\/\----/\/\---GND
    |        |       |       |
Bit3|       R|      R|      R|      R
   [S]      [S]     [S]     [S]      |
    |        |       |       |      [AO]
   Vref     Vref    Vref    Vref     |
    0        0       0       0      Vout
```

**Valeurs de composants**:

Choix: R = 10kΩ, 2R = 20kΩ

**Calculs**:

Pour code 0000 (tous les switchs à GND):

V_out = 0V

Pour code 1111 (tous les switchs à V_ref):

V_out = V_ref × (15/16) = 5 × (15/16) = 4.6875V

**Résolution**:

LSB = V_ref / 16 = 5 / 16 = 0.3125V

**Table de conversion** (quelques valeurs):

| Code | Décimal | V_out |
|------|---------|-----------|
| 0000 | 0 | 0.0000V |
| 0001 | 1 | 0.3125V |
| 0010 | 2 | 0.6250V |
| 0100 | 4 | 1.2500V |
| 1000 | 8 | 2.5000V |
| 1111 | 15 | 4.6875V |

**Avantages du R-2R**:
- Seulement 2 valeurs de résistances
- Précision garantie avec résistances 1% ou 0.1%
- Faible impédance de sortie (avec AO)

**Calcul de l'AO**:

Montage inverseur avec gain:

G = -R_f / R_eq

où R_eq est la résistance équivalente du réseau R-2R vue depuis l'AO (typiquement R_eq = 2R).

Pour gain unitaire: R_f = 2R = 20kΩ

### Travaux Pratiques

#### TP1: Caractérisation TTL/CMOS

**Objectifs**:
- Mesurer les seuils logiques V_IH, V_IL, V_OH, V_OL
- Calculer les marges de bruit
- Mesurer le fan-out
- Observer les temps de propagation

**Matériel**:
- Portes 74LS00 (TTL) et 74HC00 (CMOS)
- Alimentation 5V
- Générateur BF
- Oscilloscope
- Résistances, LED

**Mesures effectuées**:

**1) Seuils logiques** (méthode statique):

Varier lentement V_in de 0 à 5V, observer V_out.

Transition LOW→HIGH: V_IH
Transition HIGH→LOW: V_IL

**Résultats typiques**:
- 74LS00: V_IH ≈ 1.3V, V_IL ≈ 0.9V
- 74HC00: V_IH ≈ 2.5V, V_IL ≈ 2.3V

**2) Temps de propagation**:

Appliquer signal carré 1kHz, mesurer à l'oscilloscope:
- t_pHL: délai HIGH → LOW (à 50%)
- t_pLH: délai LOW → HIGH (à 50%)

**Résultats typiques**:
- 74LS00: t_pd ≈ 10ns
- 74HC00: t_pd ≈ 15ns (à V_DD = 5V)

**3) Fan-out pratique**:

Connecter progressivement des portes en sortie jusqu'à dégradation de V_OH.

#### TP2: Compteur et Affichage

**Objectif**: Réaliser un compteur décimal avec affichage 7 segments.

**Circuit**:

```
Horloge → [74HC4017] → [Décodeur BCD-7seg] → Afficheur
           (Compteur)     74HC4511
```

**74HC4017**: Compteur décimal Johnson (1 sur 10)

**Chronogrammes observés**:

Avec f_CLK = 1Hz:
- Sorties Q₀ à Q₉ activées séquentiellement
- Afficheur parcourt 0 → 9
- Remise à zéro automatique après 9

**Modifications**:

Ajout d'un bouton de remise à zéro manuelle (RESET).

**Variante**: 2× compteurs en cascade → compteur 00 à 99.

#### TP3: Conversion ADC/DAC

**Objectif**: Interfacer un ADC et un DAC avec un microcontrôleur Arduino.

**Composants**:
- **DAC**: MCP4725 (12 bits, I²C)
- **ADC**: ADS1115 (16 bits, I²C, 4 canaux)
- Arduino Uno
- Potentiomètre, oscilloscope

**Montage**:

```
Arduino (I²C) ←→ MCP4725 → Vout (mesure oscilloscope)
              ←→ ADS1115 ← Vin (potentiomètre)
```

**Programme Arduino**:

```cpp
#include <Wire.h>
#include <Adafruit_MCP4725.h>
#include <Adafruit_ADS1X15.h>

Adafruit_MCP4725 dac;
Adafruit_ADS1115 adc;

void setup() {
  Serial.begin(9600);
  dac.begin(0x60);  // Adresse I²C du MCP4725
  adc.begin(0x48);  // Adresse I²C de l'ADS1115
}

void loop() {
  // Génération de rampe sur DAC
  for (int i = 0; i < 4096; i++) {
    dac.setVoltage(i, false);  // 12 bits: 0-4095
    delay(1);
  }
  
  // Lecture ADC
  int16_t adc_value = adc.readADC_SingleEnded(0);  // Canal 0
  float voltage = adc_value * 0.0001875;  // Conversion en V (gain ±6.144V)
  
  Serial.print("ADC: ");
  Serial.print(adc_value);
  Serial.print(" (");
  Serial.print(voltage);
  Serial.println(" V)");
  
  delay(100);
}
```

**Observations**:

**DAC**: Génération de rampe 0 → 3.3V (précision mesurée ~0.5mV)

**ADC**: Lecture potentiomètre avec résolution ~0.2mV (16 bits)

**Mesures**:
- Linéarité du DAC (INL, DNL) par comparaison avec voltmètre de précision
- Bruit de l'ADC (écart-type sur 1000 échantillons)
- Temps de stabilisation du DAC (~6µs mesuré)

### Applications Pratiques

**Systèmes d'acquisition de données**:
- Cartes d'acquisition multivoies (8-16 canaux ADC)
- Conditionnement de capteurs (température, pression, courant)
- Dataloggers autonomes

**Audio numérique**:
- Codecs audio (ADC + DAC): PCM1808 (ADC 24 bits), PCM5102 (DAC 32 bits)
- DSP: traitement numérique (filtres, effets)
- Fréquence d'échantillonnage: 44.1kHz (CD), 48kHz (pro), 96-192kHz (hi-res)

**Commande de moteurs**:
- ADC pour lecture de capteurs (position, courant)
- DAC pour génération de consignes analogiques
- Compteurs pour génération PWM (variateurs de vitesse)

**Instrumentation**:
- Oscilloscopes numériques: ADC rapides (Flash, 1-10Gsps)
- Multimètres: ADC Sigma-Delta (précision 6.5 digits)
- Générateurs de fonctions: DAC + DDS (Direct Digital Synthesis)

**Télécommunications**:
- Modems: ADC/DAC pour modulation/démodulation
- SDR (Software Defined Radio): ADC/DAC large bande (>100Msps)
- Stations de base 4G/5G: ADC/DAC 14-16 bits, >1Gsps

---

## PART D: ANALYSE ET RÉFLEXION

### Connaissances et compétences mobilisées

- **Technologies logiques**: maîtrise des caractéristiques TTL/CMOS, interfaçage, fan-out
- **Circuits séquentiels**: conception de compteurs synchrones/asynchrones, machines d'états
- **Conversion de données**: compréhension approfondie des ADC/DAC, architectures, performances
- **Analyse temporelle**: setup/hold time, métastabilité, synchronisation
- **Dimensionnement**: calculs de résolution, SNR, fréquences d'échantillonnage
- **Pratique**: câblage, mesures oscilloscope, debugging de circuits numériques

### Auto-évaluation

Ce cours a été fondamental pour comprendre les bases de l'électronique numérique.

**Points forts**:
- **Vision complète**: des transistors (TTL/CMOS) aux systèmes complets (ADC/DAC)
- **Aspects pratiques**: TPs concrets avec mesures et validation
- **Théorie solide**: théorème de Shannon, quantification, timing
- **Applications variées**: audio, instrumentation, télécoms

**Difficultés rencontrées**:
- **Timing analysis**: contraintes setup/hold, calcul de fréquences max
- **Métastabilité**: concept abstrait, difficile à observer en pratique
- **Choix d'architecture**: compromis vitesse/précision/coût pour ADC/DAC
- **Interfaçage**: nombreuses règles pour garantir compatibilité TTL/CMOS

**Applications pratiques**:
- Conception de cartes d'acquisition pour projets (capteurs, IoT)
- Compréhension des datasheets de composants numériques
- Debugging de circuits numériques (oscilloscope, analyseur logique)

### Mon opinion

Ce cours est essentiel pour tout ingénieur travaillant sur des systèmes embarqués ou de l'instrumentation.

**Pourquoi ce cours est essentiel**:

1. **Interface analogique-numérique**: tous les systèmes réels nécessitent des conversions ADC/DAC
2. **Fondements des systèmes numériques**: compréhension des contraintes temporelles, synchronisation
3. **Base pour FPGA/ASIC**: logique séquentielle, machines d'états, timing
4. **Compétence transversale**: utilisée dans tous les domaines (IoT, audio, télécoms, automobile)

**Connexions avec autres cours**:
- **Logique Séquentielle** (S5): machines d'états, automates
- **Microcontrôleurs** (S6): interfaçage périphériques (ADC/DAC intégrés)
- **Filtrage Numérique** (S6): DSP, traitement après ADC
- **Traitement du Signal** (S5): échantillonnage, théorème de Shannon
- **Temps Réel** (S8): contraintes temporelles strictes
- **FPGA/VHDL** (S7): implémentation de logique séquentielle

**Évolution technologique**:

Les tendances actuelles:
- **ADC/DAC haute vitesse**: >1Gsps pour SDR, radar, oscilloscopes
- **Résolution accrue**: ADC/DAC 24-32 bits pour audio haute fidélité, instrumentation
- **Intégration**: SoC avec ADC/DAC intégrés (ESP32, STM32)
- **Faible consommation**: ADC/DAC ultra-basse consommation pour IoT (<1µA)
- **SAR nouvelle génération**: compromis vitesse/résolution (18 bits @ 1Msps)

**Technologies émergentes**:

- **Σ-Δ ADC à sur-échantillonnage massif**: audio 384kHz, DSD (1-bit 2.8MHz)
- **Time-interleaved ADC**: plusieurs ADC en parallèle → Gsps
- **Calibration numérique**: correction des non-linéarités en temps réel
- **ADC pipeline avancés**: résolution 14-16 bits, vitesse 100-500Msps

**Applications modernes**:

- **IoT et capteurs**: acquisition multivoies, faible consommation
  - Exemple: MAX11200 (24 bits, 120sps, 300µA)
  
- **Audio professionnel**: consoles de mixage, interfaces audio
  - Exemple: PCM1792 (DAC 24 bits, SNR 123dB)
  
- **5G et télécoms**: conversion ultra-rapide pour bandes larges
  - Exemple: AD9213 (ADC 12 bits, 10.25Gsps)
  
- **Automobile**: ADAS, caméras, radars
  - Exemple: ADC multiplexés 16 canaux pour batteries Li-Ion
  
- **Médical**: ECG, IRM, échographie
  - Exigences: précision élevée, isolation galvanique, normes IEC 60601

**Recommandations pour réussir**:

1. **Comprendre les datasheets**: toutes les infos sont là (timing, specs électriques)
2. **Maîtriser l'oscilloscope**: outil indispensable pour le debugging numérique
3. **Respecter les contraintes temporelles**: cause n°1 de dysfonctionnement
4. **Découplage rigoureux**: condensateurs 100nF sur chaque CI, proches des broches V_CC
5. **Attention aux entrées flottantes**: CMOS interdit, TTL déconseillé

**Outils indispensables**:

- **Oscilloscope numérique**: 4 canaux, >100MHz, décodage I²C/SPI
- **Analyseur logique**: 8-16 canaux, décodage protocoles
- **Générateur de fonctions**: formes arbitraires, modulation
- **Multimètre de précision**: 6.5 digits pour validation ADC/DAC
- **Alimentation stabilisée**: 3.3V et 5V, limitation courant

**Normes et standards**:

- **JEDEC**: spécifications des circuits logiques (voltage levels, timing)
- **IEEE 1241**: standard pour test ADC (DNL, INL, ENOB)
- **IEC 61000**: CEM pour systèmes numériques
- **JESD204B**: interface série haute vitesse pour ADC/DAC (lane >12Gbps)

**Aspects pratiques PCB**:

- **Plans de masse**: essentiels pour réduire le bruit numérique
- **Séparation AGND/DGND**: connexion en un seul point (star ground)
- **Pistes d'horloge**: impédance contrôlée, longueur égale (clock tree)
- **Découplage ADC/DAC**: ferrites, condensateurs multiples (100nF + 10µF + 100µF)
- **Blindage**: cage de Faraday pour ADC haute résolution (>16 bits)

**Debugging**:

Méthodologie pour résoudre les problèmes:
1. **Vérifier l'alimentation**: tensions stables, ondulation <50mV
2. **Contrôler les signaux d'horloge**: forme carrée, pas de sur/sous-oscillations
3. **Vérifier les niveaux logiques**: compatibilité TTL/CMOS
4. **Mesurer les temps de propagation**: respect des specs
5. **Tester composant par composant**: isolation progressive

**Erreurs fréquentes**:

- ❌ Entrées CMOS flottantes → consommation élevée, comportement erratique
- ❌ Oubli de condensateurs de découplage → instabilité, oscillations
- ❌ Fils trop longs sur breadboard → capacités parasites, ralentissement
- ❌ Mauvaise masse → boucles de masse, couplage, bruit
- ❌ Sous-échantillonnage → aliasing irréversible

En conclusion, ce cours fournit les fondations indispensables pour concevoir des systèmes numériques fiables et interfacer le monde analogique (capteurs) avec le monde numérique (microprocesseurs, FPGA). La maîtrise des technologies logiques, des convertisseurs ADC/DAC, et des contraintes temporelles est essentielle dans un contexte où les systèmes embarqués sont omniprésents (IoT, automobile, télécoms, médical).

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
    .pdf-container {
        margin: 40px 0;
        padding: 20px;
        background-color: #f9f9f9;
        border-radius: 8px;
    }
    .pdf-viewer {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        margin-top: 20px;
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
        margin-top: 0;
        color: #2a7ae2;
        border-bottom: 2px solid #2a7ae2;
        padding-bottom: 10px;
    }
</style>

---

## 📚 Documents de Cours

Voici les supports de cours en PDF pour approfondir les différents aspects de l'électronique numérique :

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>📖 Technologie des Circuits Logiques</h4>
      <p>Document détaillant les technologies TTL et CMOS, leurs caractéristiques électriques, et les méthodes d'interfaçage.</p>
      <embed src="/cours-pdf/S5/Elec-Num/Technologie-circuits-logiques.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S5/Elec-Num/Technologie-circuits-logiques.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          📥 Télécharger le PDF
        </a>
      </p>
    </div>
    
    <div class="pdf-item">
      <h4>⏱️ Chronogrammes et Compteurs</h4>
      <p>Analyse des chronogrammes de compteurs synchrones et asynchrones avec exemples pratiques de conception.</p>
      <embed src="/cours-pdf/S5/Elec-Num/chronogrammes-compteur.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S5/Elec-Num/chronogrammes-compteur.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          📥 Télécharger le PDF
        </a>
      </p>
    </div>
    
    <div class="pdf-item">
      <h4>🔄 TD Convertisseurs ADC/DAC</h4>
      <p>Travaux dirigés sur les convertisseurs analogique-numérique et numérique-analogique avec exercices d'application.</p>
      <embed src="/cours-pdf/S5/Elec-Num/TD-IMACS-NUM-CAN.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S5/Elec-Num/TD-IMACS-NUM-CAN.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          📥 Télécharger le PDF
        </a>
      </p>
    </div>
  </div>
</div>

---


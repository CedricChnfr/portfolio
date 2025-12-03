---
layout: default
title:  "Architectures Analogiques Transmission Information - S7"
date:   2024-10-02 09:01:00 +0200
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
    <a href="./my-courses-2023-2024.html">← Retour aux Cours 2023-2024</a>
</div>

# 📡 Architectures Analogiques Transmission Information - Semestre 7

**Année Universitaire** : 2023-2024  
**Semestre** : 7  
**Crédits** : 2.5 ECTS  
**Spécialité** : Électronique Analogique et RF

---

## PART A - Présentation Générale du Module

<h3 class="section-title">Vue d'ensemble</h3>

Ce cours aborde les architectures analogiques pour la transmission d'information, avec un focus sur les systèmes de modulation/démodulation et les chaînes d'émission/réception radio-fréquence (RF). Il couvre les techniques de modulation analogique (AM, FM), les oscillateurs, les multipliieurs, et les architectures de récepteurs.

**Objectifs pédagogiques** :
- Maîtriser les techniques de modulation et démodulation analogiques
- Comprendre les architectures de chaînes RF (émission et réception)
- Concevoir des oscillateurs et circuits de synthèse de fréquence
- Analyser les performances des systèmes de transmission (bruit, linéarité)
- Dimensionner des circuits pour applications radio

<h3 class="section-title">Position dans le cursus</h3>

Ce module s'appuie sur :
- **Électronique Fonctions Analogiques (S6)** : AOPs, filtres actifs
- **Signal (S5)** : modulation, transformée de Fourier
- **Circuits et Filtres analogiques (S5)** : filtres, adaptation d'impédance

Il prépare à :
- **Télécommunications** : conception de systèmes RF
- **Systèmes embarqués communicants** : IoT, radio courte portée
- **Instrumentation RF** : générateurs, analyseurs

---

## PART B - Expérience Personnelle et Contexte d'Apprentissage

<h3 class="section-title">Organisation et ressources</h3>

Le module était organisé en cours magistraux et travaux dirigés :

**Cours magistraux (20h)** :
Couvrant les thèmes principaux :
- Modulation et démodulation AM/FM
- Oscillateurs (théorie et applications)
- Multipliieurs analogiques
- Architectures de récepteurs (superhétérodyne)
- Boucles à verrouillage de phase (PLL)

**Travaux dirigés (16h)** :
5 TD avec corrections disponibles :
- TD1 à TD5 : exercices d'application sur modulation, oscillateurs, multipliieurs

**Supports pédagogiques** :
- Document de cours principal (ArchiUF_2022-2023.pdf)
- Notes de cours sur oscillateurs (Notes-cours-Théorie-Osc.pdf)
- Documents techniques (multipliieurs ADI, oscillateurs à quartz)
- Annales 2018-2019, 2021-2022 avec corrections

<h3 class="section-title">Contenu des ressources</h3>

**Documents techniques disponibles** :
- **Multipliieurs** : ADI Multiplier Applications Guide, multipliieurs 1 à 4 quadrants
- **Oscillateurs** : théorie, oscillateurs à quartz (AN3208)
- **Modulation FM** : modulation et démodulation FM
- **Détection** : démodulation par détection d'enveloppe
- **Circuits spécifiques** : RLC avec résistance négative, redresseur sans seuil

<h3 class="section-title">Méthode de travail</h3>

**Cours théorique** :
Beaucoup de schémas et d'analyses de circuits. Compréhension des principes de fonctionnement des modulateurs, démodulateurs, et oscillateurs.

**TD pratiques** :
Calculs de performances (taux de modulation, déviation de fréquence, gain, bruit). Dimensionnement de composants.

**Annales** :
Examens de 2018-2019 et 2021-2022 avec corrections pour s'entraîner.

<h3 class="section-title">Difficultés rencontrées</h3>

**Analyse fréquentielle** :
Comprendre le spectre des signaux modulés (raies, bandes latérales) demande une bonne maîtrise de la transformée de Fourier.

**Circuits RF complexes** :
Les architectures superhétérodynes avec changements de fréquence multiples sont complexes à appréhender.

**Oscillateurs** :
Conditions d'oscillation (Barkhausen), stabilité de fréquence, bruit de phase sont des concepts subtils.

---

## PART C - Aspects Techniques Détaillés

<h3 class="section-title">1. Modulation d'amplitude (AM)</h3>

**Principe** :

Faire varier l'amplitude d'un signal porteur sinusoïdal en fonction du signal d'information (message).

Signal porteur : p(t) = Vp cos(2π fp t)
Signal modulant (message) : m(t)

Signal modulé AM : s(t) = Vp [1 + m × m(t)] cos(2π fp t)

où m est l'indice de modulation (0 < m <= 1).

**Indice de modulation** :

m = (Vmax - Vmin) / (Vmax + Vmin)

- Si m < 1 : pas de surmodulation (bon)
- Si m > 1 : surmodulation, distorsion (mauvais)

**Spectre du signal AM** :

Pour un signal modulant sinusoïdal m(t) = cos(2π fm t) :

s(t) = Vp cos(2π fp t) + (m Vp / 2) cos(2π (fp + fm) t) + (m Vp / 2) cos(2π (fp - fm) t)

Trois composantes :
- Porteuse à fp
- Bande latérale supérieure à fp + fm
- Bande latérale inférieure à fp - fm

**Bande passante** :

BW = 2 × fm (fréquence max du message)

**Efficacité** :

La porteuse ne contient pas d'information utile. Puissance utile seulement dans les bandes latérales.

Rendement énergétique = m² / (2 + m²)

Pour m = 1 : rendement = 33% (faible !)

**Variantes** :

| Type | Description | Avantage |
|------|-------------|----------|
| AM classique | Porteuse + 2 BL | Simple à démoduler |
| DSB (Double Sideband) | 2 BL sans porteuse | Meilleur rendement |
| SSB (Single Sideband) | 1 BL seulement | Bande passante divisée par 2 |

<h3 class="section-title">2. Démodulation AM</h3>

**Détection d'enveloppe** :

Méthode la plus simple pour démoduler l'AM.

Circuit :
- Diode (redressement)
- Condensateur (filtrage)
- Résistance (charge)

**Principe** :
La diode redresse le signal modulé. Le condensateur suit l'enveloppe (amplitude variable) du signal.

**Dimensionnement** :

Constante de temps RC doit vérifier :
- 1/fp << RC (pour filtrer la porteuse)
- RC << 1/fm (pour suivre les variations du message)

Compromis : 1/fp << RC << 1/fm

**Détection synchrone (démodulation cohérente)** :

Multiplier le signal reçu par une porteuse synchrone (même fréquence et phase).

Nécessite une récupération de porteuse (PLL).

Plus complexe mais meilleure qualité (fonctionne pour DSB et SSB).

<h3 class="section-title">3. Modulation de fréquence (FM)</h3>

**Principe** :

Faire varier la fréquence de la porteuse proportionnellement au signal modulant.

Fréquence instantanée : f(t) = fp + kf × m(t)

où kf est la sensibilité du modulateur (Hz/V).

**Déviation de fréquence** :

Delta f = kf × Vm (amplitude max du message)

**Indice de modulation** :

beta = Delta f / fm

où fm est la fréquence du message.

**Spectre du signal FM** :

Le spectre contient une infinité de raies (théoriquement) espacées de fm.

Amplitude des raies donnée par les fonctions de Bessel Jn(beta).

**Bande passante (règle de Carson)** :

BW = 2 (Delta f + fm) = 2 fm (beta + 1)

Pour beta >> 1 (large bande) : BW ≈ 2 Delta f
Pour beta << 1 (bande étroite) : BW ≈ 2 fm

**FM large bande vs bande étroite** :

| Type | beta | Bande | Application |
|------|------|-------|-------------|
| NBFM | < 0,5 | 2 fm | Communications radio professionnelles |
| WBFM | > 1 | 2 Delta f | Radio FM broadcast (88-108 MHz) |

**Avantages de la FM** :
- Immunité au bruit d'amplitude
- Meilleure qualité audio
- Capture effect (signal fort capture le récepteur)

**Inconvénient** :
Bande passante plus large que l'AM.

<h3 class="section-title">4. Démodulation FM</h3>

**Discriminateur de fréquence** :

Convertit les variations de fréquence en variations d'amplitude, puis détection d'enveloppe.

**Principe** :
- Circuit dérivateur ou réseau déphaseur
- Transforme la FM en AM
- Détection d'enveloppe classique

**Démodulateur à PLL** :

Utilise une boucle à verrouillage de phase (PLL) qui suit la fréquence instantanée.

La tension de commande du VCO (dans la PLL) est proportionnelle à la fréquence d'entrée : c'est le signal démodulé.

**Avantage** :
- Meilleure linéarité
- Moins sensible au bruit

<h3 class="section-title">5. Oscillateurs</h3>

**Définition** :

Circuit qui génère un signal périodique (sinusoïdal ou carré) sans signal d'entrée.

**Condition d'oscillation (critère de Barkhausen)** :

Pour un oscillateur bouclé (amplificateur + réseau de rétroaction) :

Boucle ouverte : H(jω) = A(jω) × Beta(jω)

Conditions pour oscillation à ω0 :
1. |H(jω0)| = 1 (gain de boucle = 1)
2. arg(H(jω0)) = 0° ou 360° (déphasage de boucle multiple de 360°)

**Démarrage des oscillations** :

En pratique, on assure |H| légèrement > 1 au démarrage pour que les oscillations s'amorcent (à partir du bruit).

Puis un mécanisme de limitation d'amplitude (saturation, compression) stabilise l'amplitude.

**Types d'oscillateurs** :

**Oscillateurs RC** :

Réseau de déphasage (3 cellules RC) + amplificateur.

Fréquence : f ≈ 1 / (2π RC sqrt(6))

Avantage : composants simples
Inconvénient : stabilité moyenne

**Oscillateurs LC** :

Utilise un circuit résonant LC pour définir la fréquence.

Fréquence : f0 = 1 / (2π sqrt(LC))

**Oscillateur Colpitts** :

Résonateur LC avec prise capacitive (2 condensateurs en série).

Très utilisé en RF pour sa stabilité.

**Oscillateur Clapp** :

Variante du Colpitts avec condensateur série dans l'inductance.

Meilleure stabilité en fréquence.

**Oscillateurs à quartz** :

Utilise un cristal de quartz comme résonateur.

**Avantages** :
- Très haute stabilité en fréquence (ppm)
- Facteur de qualité Q très élevé (10^4 à 10^6)

**Applications** :
- Horloges (montres, microcontrôleurs)
- Bases de temps précises
- Références de fréquence

**Fréquences standards** :
- 32,768 kHz (horlogerie)
- 10 MHz (référence laboratoire)
- Quelques MHz à quelques dizaines de MHz (électronique)

<h3 class="section-title">6. Multipliieurs analogiques</h3>

**Définition** :

Circuit qui réalise la multiplication de deux signaux : Vout = k × V1 × V2

**Applications** :

| Application | Description |
|-------------|-------------|
| Modulation | Multiplier porteuse × message |
| Démodulation | Multiplier signal reçu × porteuse locale |
| Mélangeur (mixer) | Transposition de fréquence |
| Détecteur de phase | Comparaison de phase dans PLL |
| Contrôle automatique de gain | Multiplication par tension de contrôle |
| Puissance | Calcul V × I |

**Types de multipliieurs** :

**Multiplicateur 4 quadrants** :

V1 et V2 peuvent être positifs ou négatifs.
Multiplication complète : Vout = k V1 V2

**Multiplicateur 2 quadrants** :

Un signal bipolaire, l'autre unipolaire.

**Multiplicateur 1 quadrant** :

Les deux signaux unipolaires (positifs seulement).

**Exemple de circuit : cellule de Gilbert** :

Circuit à transistors (BJT ou MOS) qui réalise une multiplication.

Base de nombreux multipliieurs intégrés (AD633, AD834, etc.).

**Modulation par multiplieur** :

AM : s(t) = [Vdc + m(t)] × cos(ωp t)

Le signal modulant est additionné à une composante continue avant multiplication avec la porteuse.

**Transposition de fréquence (mélangeur)** :

Multiplier deux signaux sinusoïdaux :
V1 = A cos(ω1 t)
V2 = B cos(ω2 t)

Résultat :
Vout = (AB/2) [cos((ω1 - ω2) t) + cos((ω1 + ω2) t)]

Deux nouvelles fréquences : somme et différence.

Application : changement de fréquence dans récepteurs (superhétérodyne).

<h3 class="section-title">7. Architectures de récepteurs</h3>

**Récepteur superhétérodyne** :

Architecture classique utilisée dans la majorité des récepteurs radio.

**Principe** :

Transposer le signal RF reçu vers une fréquence intermédiaire fixe (FI) où le traitement est plus facile.

**Blocs fonctionnels** :

1. **Antenne** : réception du signal RF
2. **Filtre RF** : sélection de la bande (rejet des fréquences indésirables)
3. **Amplificateur RF (LNA)** : amplification faible bruit
4. **Mélangeur** : transposition RF → FI
5. **Oscillateur local (OL)** : génération de la fréquence de transposition
6. **Filtre FI** : sélectivité du canal (bande passante étroite)
7. **Amplificateur FI** : gain principal du récepteur
8. **Démodulateur** : extraction du signal d'information
9. **Amplificateur audio/vidéo** : amplification du signal démodulé

**Fréquence intermédiaire** :

f_FI = |f_RF - f_OL|

Choix typique de FI :
- AM broadcast : 455 kHz ou 10,7 MHz
- FM broadcast : 10,7 MHz
- TV : 36-45 MHz

**Avantages du superhétérodyne** :
- Sélectivité élevée (filtre FI fixe, bien optimisé)
- Gain élevé stable (amplification à FI fixe)
- Facilité de réglage (varier seulement f_OL)

**Problème de l'image** :

Deux fréquences RF peuvent donner la même FI :
- f_RF = f_OL + f_FI (signal désiré)
- f_image = f_OL - f_FI (image indésirable)

La fréquence image est à 2 × f_FI du signal désiré.

**Solution** :
Filtre RF qui rejette la fréquence image avant le mélangeur.

**Double changement de fréquence** :

Pour améliorer le rejet de l'image et la sélectivité, on peut utiliser deux FI successives.

RF → FI1 (élevée) → FI2 (basse) → démodulation

Exemple : FI1 = 10,7 MHz, FI2 = 455 kHz

<h3 class="section-title">8. Boucle à verrouillage de phase (PLL)</h3>

**Principe** :

Système bouclé qui asservit la phase (et donc la fréquence) d'un oscillateur local sur un signal de référence.

**Blocs** :

1. **Comparateur de phase** : compare la phase du signal d'entrée et du VCO
2. **Filtre de boucle** : filtre passe-bas (intégrateur)
3. **VCO** (Voltage Controlled Oscillator) : oscillateur commandé en tension

**Fonctionnement** :

- Si phase VCO en retard : tension de commande augmente → fréquence VCO augmente
- Si phase VCO en avance : tension de commande diminue → fréquence VCO diminue

**En régime verrouillé** :
Le VCO suit exactement la fréquence et la phase de l'entrée.

**Applications** :

| Application | Description |
|-------------|-------------|
| Synthèse de fréquence | Générer des fréquences précises et programmables |
| Démodulation FM | La tension de commande du VCO est le signal démodulé |
| Récupération de porteuse | Extraire la porteuse d'un signal modulé |
| Récupération d'horloge | Synchronisation dans transmissions numériques |
| Multiplication de fréquence | Avec diviseur dans la boucle |

**Synthétiseur de fréquence** :

PLL avec diviseur de fréquence dans la boucle de retour.

f_VCO = N × f_ref

En variant N (diviseur programmable), on génère différentes fréquences multiples de f_ref.

**Exemple** :
- f_ref = 10 kHz (quartz stable)
- N variable de 8800 à 10800
- f_VCO variable de 88 MHz à 108 MHz (bande FM)

Résolution : 10 kHz (pas entre canaux)

<h3 class="section-title">9. Circuits spécifiques</h3>

**Redresseur sans seuil** :

Redresseur utilisant un AOP pour compenser la chute de tension de la diode (0,6-0,7 V).

Permet de redresser des signaux de faible amplitude (quelques mV).

**Circuit** :
- AOP en boucle fermée avec diode
- La contre-réaction compense le seuil de la diode

**Résistance négative** :

Circuit actif (avec AOP ou transistor) qui présente une résistance négative.

**Application** :
Compenser les pertes dans un circuit RLC pour maintenir les oscillations.

Circuit RLC + résistance négative = oscillateur.

**Convertisseur tension-fréquence (VCO)** :

Circuit dont la fréquence de sortie est proportionnelle à la tension d'entrée.

f_out = k × V_in

**Types** :
- VCO LC (inductance-capacité variable, varicap)
- VCO RC (multivibrateur avec temps de charge variable)
- VCO intégré (4046, 566, etc.)

**Applications** :
- Modulation FM (V_in = signal modulant)
- PLL (oscillateur commandé)
- Conversion analogique-numérique

<h3 class="section-title">10. Performances et spécifications</h3>

**Sensibilité** :

Signal minimum détectable par le récepteur.

Limitée par le bruit (thermique + composants).

Sensibilité (dBm) = Plancher de bruit + SNR minimum

**Figure de bruit (Noise Figure - NF)** :

Mesure la dégradation du rapport signal sur bruit due au récepteur.

NF (dB) = SNR_entrée (dB) - SNR_sortie (dB)

Pour des étages en cascade (formule de Friis) :

NF_total = NF1 + (NF2 - 1)/G1 + (NF3 - 1)/(G1 × G2) + ...

Importance du premier étage (LNA) : doit avoir faible NF et gain élevé.

**Sélectivité** :

Capacité à séparer le canal désiré des canaux adjacents.

Définie par la bande passante du filtre FI.

**Dynamique** :

Plage entre signal minimum (sensibilité) et signal maximum (saturation/intermodulation).

**Gain** :

Amplification totale du récepteur.

Typiquement 60-120 dB, réparti sur plusieurs étages.

**Contrôle automatique de gain (AGC)** :

Circuit qui ajuste automatiquement le gain pour maintenir un niveau de sortie constant malgré les variations du signal d'entrée.

Évite la saturation sur signaux forts et maintient SNR sur signaux faibles.

---

## PART D - Analyse Réflexive et Perspectives

<h3 class="section-title">Compétences acquises</h3>

**Conception de chaînes RF** :
Compréhension des architectures complètes d'émission et réception. Capacité à dimensionner chaque étage et analyser les performances globales.

**Modulation/démodulation** :
Maîtrise des techniques AM et FM, calculs de spectres, choix de paramètres (indice de modulation, déviation).

**Circuits RF** :
Conception d'oscillateurs, multipliieurs, mélangeurs. Compréhension des conditions d'oscillation et stabilité.

<h3 class="section-title">Points clés à retenir</h3>

**1. Superhétérodyne = architecture dominante** :
La transposition vers FI est la solution standard depuis des décennies. Simple, efficace, éprouvée.

**2. Compromis bande/qualité** :
AM : bande étroite mais qualité moyenne. FM : bande large mais meilleure qualité et immunité au bruit.

**3. Oscillateurs : stabilité cruciale** :
La stabilité de fréquence des oscillateurs détermine la qualité du système. Quartz pour haute stabilité.

**4. Bruit : limitation fondamentale** :
Le bruit thermique et le bruit des composants limitent la sensibilité. Le premier étage (LNA) est critique.

**5. PLL : outil polyvalent** :
La PLL est utilisée partout : synthèse de fréquence, démodulation, récupération de synchronisation.

<h3 class="section-title">Applications pratiques</h3>

**Radio FM/AM** :
Les récepteurs radio classiques utilisent l'architecture superhétérodyne enseignée dans ce cours.

**Télécommunications sans fil** :
GSM, WiFi, Bluetooth utilisent des architectures dérivées (souvent avec conversion numérique après la FI).

**Instrumentation** :
Analyseurs de spectre, générateurs de signaux emploient les techniques de modulation et mélange.

**Systèmes embarqués IoT** :
Modules radio courte portée (LoRa, Sigfox, ZigBee) basés sur ces principes.

<h3 class="section-title">Retour d'expérience</h3>

**Cours riche et pratique** :
Le cours couvre beaucoup d'aspects des systèmes RF. Les TD permettent de consolider avec des calculs concrets.

**Documents techniques utiles** :
Les application notes (ADI, oscillateurs à quartz) apportent une vision industrielle et pratique.

**Annales bien corrigées** :
Les corrections détaillées des examens 2018-2019 et 2021-2022 aident beaucoup à la préparation.

**Lien théorie/pratique** :
Le cours fait bien le lien entre la théorie (analyse spectrale, conditions d'oscillation) et les circuits réels.

<h3 class="section-title">Limites et ouvertures</h3>

**Limites du module** :
- Peu de TP pratiques (mesures RF)
- Modulations numériques non traitées (QPSK, QAM, etc.)
- Aspects propagation et antennes limités

**Ouvertures vers** :
- **Communications numériques** : modulations numériques, codage canal
- **RF avancée** : architectures Zero-IF, SDR (Software Defined Radio)
- **Systèmes MIMO** : diversité spatiale, beamforming
- **5G/6G** : bandes mmWave, massive MIMO
- **IoT** : protocoles radio basse consommation (LoRa, NB-IoT)

<h3 class="section-title">Évolution technologique</h3>

**Tendances actuelles** :

**SDR (Software Defined Radio)** :
Numérisation le plus tôt possible dans la chaîne, traitement en DSP. Flexibilité maximale.

**Intégration** :
SoC RF intégrant toute la chaîne sur une puce (émetteur, récepteur, DSP, processeur).

**Bandes mmWave** :
5G utilise 24-40 GHz. Défis : atténuation, conception RF complexe.

**Efficacité énergétique** :
IoT nécessite des radios ultra-basse consommation (µW en veille, mW en émission).

<h3 class="section-title">Conseils pour réussir</h3>

**1. Maîtriser les bases** :
Bien comprendre modulation AM/FM, spectres, bande passante avant d'attaquer les architectures.

**2. Faire les TD** :
Les 5 TD avec corrections sont essentiels. Refaire sans regarder les corrections.

**3. Étudier les annales** :
Les examens 2018-2019 et 2021-2022 donnent le format et le niveau attendus.

**4. Comprendre les schémas** :
Savoir lire et analyser les schémas blocs des chaînes RF (identifier chaque fonction).

**5. Ordre de grandeur** :
Connaître les valeurs typiques (FI, fréquences radio, gains, NF).

<h3 class="section-title">Conclusion</h3>

Ce cours fournit une excellente base en architectures RF analogiques. Même si la tendance est à la numérisation (SDR), la chaîne RF analogique (antenne → LNA → mélangeur → ADC) reste incontournable.

**Complémentarité** :
Ce cours s'articule bien avec les cours de traitement numérique du signal et de communications numériques pour une vision complète des télécommunications.

**Pertinence professionnelle** :
Les compétences acquises sont directement applicables dans l'industrie des télécommunications, de l'IoT, et de l'instrumentation RF.

**Message principal** :
Comprendre les architectures RF analogiques est fondamental pour tout ingénieur en électronique et télécommunications. C'est la base sur laquelle reposent tous les systèmes sans fil modernes.

**Recommandations** :
- Approfondir avec des simulations (ADS, LTspice pour RF)
- Pratiquer avec des kits RF (modules SDR, analyseurs de spectre)
- Explorer les datasheets de circuits intégrés RF (émetteurs-récepteurs)
- Se former aux communications numériques en complément

**Liens avec les autres cours** :
- [Électronique Fonctions Analogiques - S6](./electronique-fonctions-analogiques.html) : AOPs, filtres
- [Signal - S5](./signal.html) : transformée de Fourier, modulation
- [Embedded IA for IoT - S9](./embedded-ia-for-iot.html) : systèmes communicants

---

## 📚 Documents de Cours

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
      <h4>📖 Cours Complet</h4>
      <p>Cours complet sur les architectures RF : oscillateurs, PLL, mélangeurs, modulation/démodulation AM et FM.</p>
      <embed src="/cours-pdf/S7/Archi-Analogiques-Transmission/cours-complet.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Archi-Analogiques-Transmission/cours-complet.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>📖 Modulation et Démodulation FM</h4>
      <p>Cours détaillé sur la modulation de fréquence : VCO, discriminateurs, détecteurs de phase et applications.</p>
      <embed src="/cours-pdf/S7/Archi-Analogiques-Transmission/modulation-fm.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Archi-Analogiques-Transmission/modulation-fm.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>📖 Recueil TDs</h4>
      <p>Ensemble des travaux dirigés avec exercices sur oscillateurs, PLL, mélangeurs et chaînes RF complètes.</p>
      <embed src="/cours-pdf/S7/Archi-Analogiques-Transmission/tds.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Archi-Analogiques-Transmission/tds.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
  </div>
</div>

---

*Cours suivi en 2023-2024 à l'INSA Toulouse, Département Génie Électrique et Informatique.*

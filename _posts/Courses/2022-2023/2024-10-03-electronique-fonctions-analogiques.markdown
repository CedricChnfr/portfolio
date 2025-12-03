---
layout: default
title: "Électronique Fonctions Analogiques - S6"
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

# 🔌 Électronique Fonctions Analogiques - Semestre 6

**Année Universitaire** : 2022-2023  
**Semestre** : 6  
**Crédits** : 2 ECTS  
**Spécialité** : Électronique et Systèmes Embarqués

---

## PART A - Présentation Générale du Cours

<h3 class="section-title">Vue d'ensemble</h3>

Ce cours approfondit l'étude des circuits et fonctions électroniques analogiques avancés. L'accent est mis sur les amplificateurs opérationnels (AOP) et leurs défauts réels, les filtres actifs, et les fonctions de conditionnement de signaux. Le cours combine théorie et pratique avec des TPs sur la mesure des imperfections des AOPs et la conception de filtres.

**Objectifs pédagogiques** :
- Comprendre et caractériser les défauts réels des amplificateurs opérationnels
- Concevoir et analyser des filtres actifs (passe-bas, passe-haut, passe-bande)
- Maîtriser les fonctions de conditionnement analogique pour capteurs
- Mesurer et compenser les imperfections des circuits analogiques

<h3 class="section-title">Position dans le cursus</h3>

Ce cours s'inscrit dans la continuité des enseignements :
- **Circuits et Filtres Analogiques (S5)** : bases des circuits RC, RL et fonctions de transfert
- **Composants et Notions de Puissance (S5)** : transistors et amplification
- **Filtrage Numérique (S6)** : complémentarité filtres analogiques/numériques

Il prépare aux cours avancés :
- **Architectures Analogiques pour Transmission (S7)** : chaînes RF
- **Chaînes Électroniques d'Acquisition (S8)** : acquisition de données complète

---

## PART B - Expérience Personnelle et Contexte d'Apprentissage

<h3 class="section-title">Organisation et ressources</h3>

Le module était structuré en 3 parties principales :

**1. Cours magistraux** :
- Défauts des AOPs : offset, courants de polarisation, dérive thermique
- Structures de filtres actifs : Sallen-Key, Rauch, biquads
- Fonctions de conditionnement : amplificateurs d'instrumentation, isolation

**2. Travaux dirigés** :
- Calculs d'erreurs dues aux défauts d'AOP
- Dimensionnement de filtres actifs (ordres 1, 2, 3)
- Analyse de la stabilité et du gain en boucle fermée

**3. Travaux pratiques** :
- **TP1 - Mesure des défauts d'AOP** : caractérisation expérimentale d'un LM358
- **TP2 - Filtres actifs** : réalisation et test de filtres Sallen-Key

<h3 class="section-title">Déroulement des TPs</h3>

**TP1 : Mesure des Défauts d'Amplificateurs Opérationnels**

Le premier TP consistait à mesurer les imperfections d'un AOP réel (LM358) :

| Défaut mesuré | Méthode | Valeur typique |
|--------------|---------|----------------|
| Tension d'offset Vos | Montage suiveur, mesure directe | 2-7 mV |
| Courants de polarisation Ib+ et Ib- | Résistances de forte valeur à l'entrée | 20-100 nA |
| Gain en tension Av | Montage amplificateur non-inverseur | 100 000 (100 dB) |
| Bande passante BW | Réponse fréquentielle | 1 MHz |
| Slew rate SR | Signal carré, mesure du temps de montée | 0,5 V/µs |

**Manipulation pratique** :
1. Montage suiveur pour offset : sortie non nulle même avec entrée à 0V
2. Ajout de résistances aux entrées pour isoler les courants de polarisation
3. Balayage fréquentiel pour déterminer le GBP (Gain-Bandwidth Product)

**TP2 : Filtres Actifs**

Conception et réalisation de plusieurs topologies de filtres :

**Filtre passe-bas Sallen-Key ordre 2** :
- Fréquence de coupure : 1 kHz
- Structure : deux résistances R, deux capacités C, AOP en suiveur
- Pente : -40 dB/décade au-delà de fc
- Avantage : impédance de sortie faible, pas de charge sur les étages suivants

**Filtre passe-haut Sallen-Key ordre 2** :
- Même principe avec permutation R et C
- Élimination des composantes basse fréquence

**Observations à l'oscilloscope** :
- Vérification de l'atténuation en dB par décade
- Mesure du déphasage (90° à fc pour ordre 1, 180° pour ordre 2)
- Impact du facteur de qualité Q sur la résonance

<h3 class="section-title">Difficultés rencontrées</h3>

**Parasites et bruit** :
- Les mesures d'offset et de courants étaient sensibles au bruit 50 Hz du secteur
- Solution : blindage, masse étoile, condensateurs de découplage

**Choix des composants** :
- Tolérances des résistances et capacités (5-10%) impactaient les fréquences de coupure
- Nécessité d'utiliser un multimètre pour mesurer les valeurs réelles

**Stabilité des montages** :
- Oscillations parasites dues au GBP limité de l'AOP
- Ajout de capacités de compensation

---

## PART C - Aspects Techniques Détaillés

<h3 class="section-title">1. Défauts des Amplificateurs Opérationnels</h3>

Un AOP réel présente plusieurs imperfections par rapport au modèle idéal :

**Tension d'offset (Vos)** :
Différence de tension entre les entrées pour obtenir Vout = 0V. Typiquement 1-10 mV.

Impact sur un montage non-inverseur de gain G :
- Erreur en sortie = Vos × G
- Exemple : Vos = 5 mV, G = 100 → erreur de 500 mV !

**Courants de polarisation (Ib+ et Ib-)** :
Courants d'entrée nécessaires au fonctionnement des transistors internes. Typiquement 10-200 nA pour un LM358.

Compensation : résistance Rc en série avec l'entrée non-inverseuse
- Rc = R1 // R2 (parallèle des résistances de gain)

**Courant d'offset (Ios)** :
Différence entre Ib+ et Ib- : Ios = |Ib+ - Ib-|

**Gain en tension fini (Av)** :
Au lieu d'être infini, le gain en boucle ouverte est limité (typiquement 100 000 = 100 dB).

Effet sur le gain en boucle fermée :
- Gain réel légèrement inférieur au gain théorique
- Importance pour les applications de précision

**Produit Gain-Bande Passante (GBP)** :
Le gain diminue avec la fréquence. Produit constant GBP = Av × BW.
- LM358 : GBP = 1 MHz
- Si gain souhaité = 100, BW max = 10 kHz

**Slew Rate (SR)** :
Vitesse maximale de variation de la tension de sortie. Limitée par les courants de charge internes.
- LM358 : SR ≈ 0,5 V/µs
- Limite la fréquence maximale des signaux de forte amplitude

**CMRR (Common Mode Rejection Ratio)** :
Capacité à rejeter les signaux de mode commun. Typiquement 70-100 dB.
- CMRR faible → sensibilité aux perturbations sur l'alimentation

**PSRR (Power Supply Rejection Ratio)** :
Rejet des variations d'alimentation. Important pour les circuits sur batterie.

<h3 class="section-title">2. Filtres Actifs</h3>

Les filtres actifs utilisent des AOPs pour obtenir des fonctions de transfert sans inductances.

**Avantages par rapport aux filtres passifs** :
- Pas d'inductances (encombrement, coût, non-idéalités)
- Gain possible (amplification + filtrage)
- Impédance de sortie faible
- Pas d'effet de charge entre étages

**Structure Sallen-Key (passe-bas ordre 2)** :

Configuration typique :
- Deux résistances R1 = R2 = R
- Deux condensateurs C1 = C2 = C
- AOP monté en suiveur (gain = 1)

Fréquence de coupure : fc = 1 / (2π × R × C)

Fonction de transfert : H(p) = 1 / (1 + a1×p + a2×p²)
- a1 et a2 dépendent du facteur de qualité Q
- Q = 0,707 pour réponse Butterworth (maximalement plate)

**Filtre passe-haut ordre 2** :
Inversion des positions R et C par rapport au passe-bas.

**Filtre passe-bande** :
Cascade d'un passe-haut et d'un passe-bas, ou structure Rauch.
- Bande passante : f1 < f < f2
- Facteur de qualité : Q = f0 / (f2 - f1)

**Filtre coupe-bande (notch)** :
Atténue une bande de fréquences (ex : éliminer le 50 Hz secteur).

**Filtres d'ordre supérieur** :
Cascade de plusieurs cellules d'ordre 2 (biquads).
- Ordre 4 : deux cellules ordre 2 → pente -80 dB/décade
- Chaque cellule a son propre Q pour obtenir la réponse globale souhaitée

**Types de réponses** :
- **Butterworth** : maximalement plate en bande passante
- **Chebyshev** : ondulations en bande passante, coupure plus raide
- **Bessel** : réponse de phase linéaire, pas de distorsion temporelle

<h3 class="section-title">3. Amplificateurs d'Instrumentation</h3>

Circuits spécialisés pour mesures de précision sur capteurs.

**Caractéristiques** :
- Gain différentiel élevé et stable
- Impédance d'entrée très élevée (> 1 GΩ)
- CMRR très élevé (> 100 dB)
- Faible dérive thermique

**Structure classique à 3 AOPs** :
- Étage d'entrée : deux AOPs en configuration non-inverseuse
- Étage de sortie : amplificateur différentiel
- Gain ajustable par une seule résistance externe

**Applications** :
- Ponts de Wheatstone (jauges de contrainte)
- Thermocouples
- Mesures biomédicales (ECG, EEG)

**Exemple : pont de Wheatstone**

Capteur de contrainte avec 4 résistances :
- R1, R2 fixes
- R3, R4 varient avec la déformation
- Tension de sortie proportionnelle à la variation de résistance
- Amplificateur d'instrumentation amplifie cette faible différence (quelques mV)

<h3 class="section-title">4. Techniques de Conditionnement</h3>

**Conversion tension-courant** :
Source de courant contrôlée en tension (VCCS). Utile pour piloter des LEDs ou capteurs 4-20 mA.

**Conversion courant-tension (transimpédance)** :
Photodiode → AOP → tension. Résistance de contre-réaction définit le gain.

**Détecteur de crête** :
Capture la valeur maximale d'un signal. Diode + condensateur + suiveur.

**Redresseur de précision** :
Redressement sans seuil de diode (0,6V). L'AOP compense la chute de tension.

**Convertisseur RMS-DC** :
Mesure la valeur efficace d'un signal alternatif. Circuit intégré dédié (ex : AD536).

<h3 class="section-title">5. Aspects Pratiques de Conception</h3>

**Choix de l'AOP** :

| Application | AOP recommandé | Critères |
|-------------|----------------|----------|
| Instrumentation de précision | AD620, INA126 | Faible offset, haut CMRR |
| Audio | NE5532, OPA2134 | Faible bruit, faible distorsion |
| Vidéo | AD8001 | Large bande passante, fort slew rate |
| Faible consommation | LMV321 | Micro-puissance, rail-to-rail |

**Règles de câblage** :
- Condensateurs de découplage 100 nF au plus près des broches d'alimentation
- Pistes courtes pour minimiser les inductances parasites
- Plan de masse continu
- Séparation masses analogique/numérique

**Compensation des défauts** :
- Potentiomètre d'ajustage pour compensation d'offset
- Résistance de compensation Rc pour les courants de polarisation
- Choix d'AOP à faible dérive thermique pour environnements sévères

---

## PART D - Analyse Réflexive et Perspectives

<h3 class="section-title">Compétences acquises</h3>

**Analyse de circuits analogiques** :
Ce cours a renforcé ma capacité à analyser les circuits réels en tenant compte des imperfections. La différence entre modèle idéal et comportement réel est cruciale pour des conceptions fiables.

**Mesure et instrumentation** :
Les TPs ont développé des compétences en métrologie : comment mesurer des grandeurs de quelques mV ou nA avec précision, éliminer les parasites, interpréter les résultats.

**Conception de filtres** :
La maîtrise des filtres actifs est essentielle pour toute chaîne d'acquisition. Savoir dimensionner un filtre anti-repliement avant un CAN ou un filtre de reconstruction après un CAN.

<h3 class="section-title">Points clés à retenir</h3>

**1. Rien n'est idéal** :
Les AOPs réels ont des limites (offset, courants, GBP, slew rate). Il faut toujours vérifier les datasheets et concevoir en tenant compte des pires cas.

**2. Filtres actifs vs passifs** :
Les filtres actifs simplifient les conceptions (pas d'inductances) mais ajoutent des contraintes (alimentation, bruit, bande passante limitée).

**3. Importance du conditionnement** :
Dans une chaîne d'acquisition, le conditionnement analogique (amplification, filtrage, isolation) est aussi important que la conversion numérique.

**4. Compromis performances/coût** :
Un AOP de précision coûte 10-100× plus cher qu'un LM358. Il faut adapter le choix à l'application.

<h3 class="section-title">Applications pratiques</h3>

**Projet PCB (S6)** :
Les connaissances en filtres actifs ont été directement appliquées dans le projet PCB pour filtrer les signaux d'entrée et éliminer les bruits haute fréquence.

**Chaînes d'acquisition (S8)** :
Ce cours est un prérequis pour comprendre la partie analogique des systèmes d'acquisition : filtres anti-repliement, amplificateurs d'instrumentation, isolation galvanique.

**Systèmes embarqués** :
De nombreux capteurs (température, pression, accélération) nécessitent un conditionnement analogique avant numérisation par un microcontrôleur.

<h3 class="section-title">Limites et ouvertures</h3>

**Limites du cours** :
- Peu d'aspects numériques (CAN/CNA) : voir cours Chaînes d'Acquisition S8
- Pas de circuits RF haute fréquence : voir cours Architectures Analogiques S7
- Peu de circuits de puissance : voir cours Électronique de Puissance

**Ouvertures vers** :
- **Circuits intégrés analogiques** : conception de circuits CMOS analogiques (VLSI)
- **Capteurs intelligents** : intégration conditionnement + conversion + traitement sur puce
- **Systèmes mixtes analogique-numérique** : SoC avec parties analogiques et numériques
- **IoT et objets connectés** : circuits ultra-basse consommation pour capteurs autonomes

<h3 class="section-title">Conclusion</h3>

L'électronique analogique reste incontournable malgré la prédominance du numérique. Tout signal physique (température, pression, son, lumière) est analogique et nécessite un conditionnement avant traitement numérique.

Ce cours a permis de comprendre les subtilités des circuits analogiques réels, loin des approximations du modèle idéal. La capacité à concevoir des filtres actifs, choisir le bon AOP, et mesurer précisément les défauts est essentielle pour tout ingénieur en systèmes embarqués ou instrumentation.

**Évolution du domaine** :
- Miniaturisation continue (circuits intégrés CMOS)
- Intégration analogique/numérique sur même puce (SoC)
- Ultra-basse consommation pour IoT
- Compensation numérique des défauts analogiques

**Liens avec les autres cours** :
- [Circuits et Filtres Analogiques - S5](./circuits-filtres-analogiques.html) : fondamentaux
- [Filtrage Numérique - S6](./filtrage-numerique.html) : complémentarité
- [Chaînes Électroniques d'Acquisition - S8](./chaines-acquisition.html) : application complète

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
      <h4>📖 TD Correction</h4>
      <p>Correction des travaux dirigés sur les amplificateurs opérationnels et les filtres actifs avec méthodes détaillées.</p>
      <embed src="/cours-pdf/S6/Elec-Fonctions-Analogiques/td-correction.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Elec-Fonctions-Analogiques/td-correction.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>📖 TP1 - Mesure Défauts AOP</h4>
      <p>Sujet du TP sur la mesure des défauts réels des amplificateurs opérationnels : offset, bande passante, slew-rate.</p>
      <embed src="/cours-pdf/S6/Elec-Fonctions-Analogiques/tp1-defauts-aop.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Elec-Fonctions-Analogiques/tp1-defauts-aop.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
  </div>
</div>

---

*Cours enseigné en 2022-2023 à l'INSA Toulouse, Département Génie Électrique et Informatique.*

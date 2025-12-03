---
layout: default
title: "Filtrage Actif et Modélisation Sources Bruit - S7"
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
    <a href="./my-courses-2023-2024.html">← Retour aux Cours 2023-2024</a>
</div>

# 🔊 Filtrage Actif et Modélisation Sources Bruit - Semestre 7

**Année Universitaire** : 2023-2024  
**Semestre** : 7  
**Crédits** : 2.5 ECTS  
**Spécialité** : Électronique Analogique et Traitement du Signal

---

## PART A - Présentation Générale du Module

<h3 class="section-title">Vue d'ensemble</h3>

Ce cours traite deux aspects fondamentaux de l'électronique analogique : la conception de filtres actifs avec amplificateurs opérationnels (AOP) et amplificateurs à transconductance opérationnels (OTA), et l'analyse du bruit dans les circuits électroniques. Ces compétences sont essentielles pour concevoir des chaînes d'acquisition de signaux haute performance.

**Objectifs pédagogiques** :
- Concevoir et synthétiser des filtres actifs d'ordre élevé
- Maîtriser les topologies Sallen-Key, Rauch, et capacités commutées
- Comprendre les sources physiques de bruit électronique
- Modéliser et calculer le bruit dans les circuits
- Optimiser le rapport signal sur bruit (SNR)
- Analyser les performances de chaînes d'acquisition

<h3 class="section-title">Position dans le cursus</h3>

Ce module s'appuie sur :
- **Circuits et Filtres analogiques (S5)** : filtres passifs, fonction de transfert
- **Filtrage numérique (S6)** : théorie du filtrage, approximations
- **Étude et Modélisation Composants Actifs (S7)** : amplificateurs opérationnels

Il prépare à :
- **Chaînes électroniques acquisition (S8)** : conditionnement de capteurs
- **Processus stochastiques et files d'attente (S8)** : modélisation probabiliste
- **Traitement du signal avancé** : filtrage optimal, détection
- **Conception de systèmes d'instrumentation** : mesures de précision

---

## PART B - Expérience Personnelle et Contexte d'Apprentissage

<h3 class="section-title">Organisation et ressources</h3>

Le module était divisé en plusieurs volets thématiques :

**Cours magistraux (20h)** :
Organisés en 4 grandes parties :
- Partie 1 : Amplificateurs opérationnels et OTA (dossier 1_AO_OTA)
  - Bruit interne des AOP
  - OTA CA3080 (amplificateur à transconductance)
- Partie 2 : Architecture électronique et filtres actifs (dossier 3_Archi_Elec_Filtre_Actif)
  - Gabarits et synthèse de filtres
  - Topologies Sallen-Key et Rauch
  - Association de cellules d'ordre 2
- Partie 3 : Capacités commutées (dossier 4_Capa_Commute)
  - Principe et applications
- Partie 4 : Document de synthèse (4AESE-filtrage4AE_2020-2021.pdf)

**Travaux dirigés (12h)** :
- TD1 à TD6 avec corrections disponibles
- Exercices de synthèse de filtres
- Calculs de bruit dans circuits
- Dimensionnement de chaînes d'acquisition

**Évaluations** :
- Annales disponibles (2016-2022) avec corrections
- Examen portant sur filtrage ET bruit
- Projet de conception de filtre

**Outils utilisés** :
- SPICE (simulation circuits, analyse bruit)
- MATLAB/Octave (synthèse de filtres, calculs)
- Analyseur de spectre (mesure bruit)
- Oscilloscope numérique

<h3 class="section-title">Méthodologie d'étude</h3>

**Phase 1 : Spécifications du filtre** :
Définir le gabarit (fréquences de coupure, ondulation, atténuation en bande coupée) selon l'application.

**Phase 2 : Choix de l'approximation** :
Sélectionner Butterworth, Chebyshev, Bessel, ou Elliptique selon le compromis sélectivité/phase/temps.

**Phase 3 : Synthèse de la fonction de transfert** :
Utiliser tables ou logiciels pour obtenir les pôles et zéros. Décomposer en cellules d'ordre 2.

**Phase 4 : Implémentation électronique** :
Choisir la topologie (Sallen-Key, Rauch) et calculer les composants (R, C) pour chaque cellule.

**Phase 5 : Analyse du bruit** :
Calculer les contributions de bruit de chaque composant et AOP, puis le bruit total ramené en entrée.

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S7/filtrage-actif/capacites-commutees.svg" alt="Filtre à capacités commutées" style="max-width: 550px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Principe des filtres à capacités commutées - Émulation de résistance par commutation</p>
</div>

**Phase 6 : Simulation et validation** :
Vérifier la réponse fréquentielle, le bruit, et les limitations pratiques (saturation, slew-rate).

<h3 class="section-title">Difficultés rencontrées</h3>

**Synthèse de filtres d'ordre élevé** :
Cascader plusieurs cellules du 2e ordre nécessite de gérer les interactions, l'ordre des sections, et les niveaux de signaux inter-étages.

**Valeurs de composants** :
Les calculs théoriques donnent souvent des valeurs non standard (résistances, capacités). Il faut ajuster avec les séries E12/E24/E96.

**Analyse du bruit** :
Identifier toutes les sources de bruit (résistances, AOP, alimentations), calculer leur contribution ramené en entrée, puis intégrer sur la bande passante demande rigueur.

**Bruit en 1/f** :
La densité spectrale n'est pas constante, ce qui complique les calculs d'intégration. Nécessite de connaître la fréquence de coin.

---

## PART C - Aspects Techniques Détaillés

<h3 class="section-title">1. Amplificateurs opérationnels et bruit interne</h3>

**Modèle de bruit d'un AOP** :

Trois sources de bruit équivalentes en entrée :
- **en** : tension de bruit en entrée (nV/racine(Hz))
- **in+** : courant de bruit entrée non-inverseuse (pA/racine(Hz))
- **in-** : courant de bruit entrée inverseuse (pA/racine(Hz))

**Densité spectrale de bruit en tension** :

Typiquement :
- AOP bipolaire : en = 1-10 nV/racine(Hz)
- AOP JFET : en = 5-20 nV/racine(Hz)
- AOP précision : en < 5 nV/racine(Hz)

**Densité spectrale de bruit en courant** :

Typiquement :
- AOP bipolaire : in = 1-10 pA/racine(Hz)
- AOP JFET : in = 0.01-1 pA/racine(Hz) (très faible)

**Bruit en 1/f** :

Fréquence de coin fc (transition entre bruit en 1/f et bruit blanc) :
- AOP bipolaire : fc = 10-100 Hz
- AOP JFET : fc = 100-1000 Hz

**OTA (Operational Transconductance Amplifier)** :

Exemple : CA3080
- Sortie en courant (transconductance gm réglable)
- Applications : VCA, VCF, multiplieurs
- Bruit typiquement plus élevé que AOP classiques

<h3 class="section-title">2. Sources fondamentales de bruit</h3>

**Bruit thermique (Johnson-Nyquist)** :

Origine : agitation thermique des porteurs de charge dans les résistances.

Tension de bruit RMS :
Vn = racine(4 × k × T × R × Δf)

avec :
- k = 1.38 × 10^-23 J/K (constante de Boltzmann)
- T : température absolue (Kelvin)
- R : résistance (Ohms)
- Δf : bande passante (Hz)

Densité spectrale (spectre blanc) :
Sn(f) = 4 × k × T × R (V²/Hz)

**Exemples à 25°C (T=298K)** :

| Résistance | Bruit (nV/racine(Hz)) |
|------------|----------------------|
| 1 kΩ | 4.1 |
| 10 kΩ | 13 |
| 100 kΩ | 41 |
| 1 MΩ | 130 |

**Bruit de grenaille (shot noise)** :

Origine : nature discrète du courant électrique (quantification des électrons).

Courant de bruit RMS :
In = racine(2 × q × I × Δf)

avec :
- q = 1.6 × 10^-19 C (charge électron)
- I : courant moyen (A)

Observé dans jonctions PN (diodes, transistors), tubes, photodétecteurs.

**Bruit en 1/f (flicker noise)** :

Origine : défauts cristallins, recombinaisons de surface.

Densité spectrale :
Sn(f) = K / f

Dominant à basse fréquence (< 1 kHz typiquement).

Fréquence de coin fc : transition vers bruit blanc.

**Comparaison des bruits** :

| Type | Spectre | Amplitude | Dominant |
|------|---------|-----------|----------|
| Thermique | Blanc | 4kTR | Toutes fréquences |
| Grenaille | Blanc | 2qI | Jonctions actives |
| 1/f | Rose (1/f) | Variable | Basses fréquences |

<h3 class="section-title">3. Topologies de filtres actifs</h3>

**Filtre Sallen-Key (VCVS)** :

Configuration non-inverseuse avec gain K.

**Passe-bas du 2e ordre** :

Composants : R1, R2, C1, C2, AOP en suiveur ou amplificateur.

Fonction de transfert générale :
H(s) = K × ω0² / (s² + (ω0/Q) × s + ω0²)

avec :
- ω0 : pulsation propre (fréquence de coupure)
- Q : facteur de qualité (inverse de l'amortissement)
- K : gain en bande passante

**Avantages** :
- Simple (peu de composants)
- Gain possible en bande passante
- Haute impédance d'entrée

**Inconvénients** :
- Sensibilité aux composants pour Q élevé
- Stabilité limitée si Q > 10

**Filtre Rauch (structure inverseuse)** :

Configuration inverseuse avec gain négatif en bande passante.

**Avantages** :
- Meilleure stabilité pour Q élevé
- Moins sensible aux variations de composants

**Inconvénients** :
- Impédance d'entrée plus faible
- Gain négatif (peut nécessiter un étage inverseur additionnel)

**Comparaison** :

| Critère | Sallen-Key | Rauch |
|---------|------------|-------|
| Nombre composants | 4 passifs + AOP | 5 passifs + AOP |
| Impédance entrée | Haute | Moyenne/Faible |
| Gain bande passante | Positif | Négatif |
| Stabilité Q élevé | Limitée | Meilleure |
| Usage | Polyvalent | Q > 5 |

<h3 class="section-title">4. Approximations de filtres</h3>

**Butterworth (Maximally Flat)** :

Caractéristiques :
- Réponse en amplitude la plus plate possible en bande passante
- Pas d'ondulation
- Atténuation : 20 × n dB/décade (n = ordre du filtre)
- Réponse en phase non-linéaire

Applications : usage général, audio (réponse douce).

**Chebyshev Type I** :

Caractéristiques :
- Ondulation en bande passante (ripple contrôlé, ex : 0.5 dB, 1 dB, 3 dB)
- Pente plus raide que Butterworth à ordre égal
- Transition rapide

Applications : anti-aliasing, filtres sélectifs.

**Chebyshev Type II (Inverse)** :

Caractéristiques :
- Ondulation en bande atténuée
- Bande passante plate
- Zéros de transmission (atténuation finie)

Applications : moins courant, compromis.

**Bessel (Thomson)** :

Caractéristiques :
- Réponse en phase linéaire
- Délai de groupe constant (pas de distorsion de phase)
- Atténuation douce (pente faible)

Applications : vidéo, impulsions (préservation de forme temporelle).

**Elliptique (Cauer)** :

Caractéristiques :
- Ondulation en bande passante ET en bande atténuée
- Pente la plus raide pour un ordre donné
- Complexité de conception (zéros de transmission)

Applications : télécommunications (sélectivité maximale).

**Tableau récapitulatif** :

| Type | Bande passante | Pente | Phase | Application |
|------|----------------|-------|-------|-------------|
| Butterworth | Plate | Moyenne | Non-linéaire | Usage général |
| Chebyshev I | Ondulation | Raide | Fortement non-linéaire | Anti-aliasing |
| Chebyshev II | Plate | Raide | Non-linéaire | Compromis |
| Bessel | Plate | Douce | Linéaire | Vidéo, impulsions |
| Elliptique | Ondulation | Très raide | Fortement non-linéaire | Télécom |

<h3 class="section-title">5. Synthèse de filtres d'ordre élevé</h3>

**Décomposition en cascade** :

Un filtre d'ordre n est réalisé par cascade de cellules :
- Ordre pair : n/2 cellules du 2e ordre
- Ordre impair : (n-1)/2 cellules du 2e ordre + 1 cellule du 1er ordre

Fonction de transfert totale :
H(s) = H1(s) × H2(s) × ... × Hk(s)

**Paramètres de chaque cellule** :

Chaque cellule du 2e ordre a ses propres :
- Fréquence propre ω0i
- Facteur de qualité Qi
- Gain Ki

**Exemple : Butterworth ordre 5** :

Décomposition : 2 cellules du 2e ordre + 1 cellule du 1er ordre

Cellule 1 : Q1 = 0.618, ω01 = ωc
Cellule 2 : Q2 = 1.618, ω02 = ωc
Cellule 3 : pôle réel à -ωc

**Ordre des sections** :

Principe général :
1. Placer les sections à Q élevé en fin de cascade (après atténuation)
2. Éviter la saturation des premiers étages
3. Minimiser l'accumulation de bruit

**Normalisation et dénormalisation** :

Étapes :
1. Synthèse normalisée (ωc = 1 rad/s, R = 1 Ω)
2. Tables de coefficients pour approximations standard
3. Dénormalisation : mise à l'échelle en fréquence et impédance

Formules de dénormalisation :
- Résistance : R_réel = R_normalisé × Z0
- Capacité : C_réel = C_normalisé / (Z0 × ωc)

<h3 class="section-title">6. Filtres à capacités commutées</h3>

**Principe** :

Une résistance est simulée par commutation périodique d'une capacité.

Résistance équivalente :
Req = T / C = 1 / (f × C)

avec :
- T : période d'horloge
- f : fréquence d'horloge
- C : capacité commutée

**Avantages** :

- Précision déterminée par rapports de capacités (excellente en CI)
- Pas de résistances (gain de surface en intégration)
- Accordabilité via fréquence d'horloge
- Faible sensibilité aux variations process

**Limitations** :

- Nécessite horloge (bruit d'horloge)
- Théorème d'échantillonnage : f_horloge >> 2 × f_signal
- Typiquement : f_horloge = 50 à 100 × f_coupure

**Applications** :

- Filtres anti-aliasing dans ADC
- Filtres de reconstruction dans DAC
- Égaliseurs audio programmables
- Circuits intégrés mixtes (analog/digital)

**Exemple commercial** :

MAX7400 (Maxim) : filtre passe-bas 8e ordre Butterworth à capacités commutées, fréquence de coupure programmable par horloge.

<h3 class="section-title">7. Analyse du bruit dans un amplificateur</h3>

**Amplificateur non-inverseur** :

Configuration :
- Gain Av = 1 + (R2 / R1)
- Entrée : source de signal Vs avec impédance Rs

**Sources de bruit** :

1. Bruit de la source : Vn_source = racine(4kTRs)
2. Bruit thermique R1 : Vn_R1 = racine(4kTR1)
3. Bruit thermique R2 : Vn_R2 = racine(4kTR2)
4. Bruit en tension AOP : en
5. Bruit en courant AOP × impédances : in × (Rs // (R1+R2))

**Bruit total ramené en entrée (RTI)** :

Vn_total² = Vn_source² + en² + (in × Rs)² + (Vn_R1 / Av)² + (Vn_R2 / Av)²

**Bruit de sortie** :

Vn_out = Vn_total × Av

**Optimisation** :

- Minimiser Rs (résistance de source faible)
- Choisir R1, R2 raisonnables (compromis bruit/consommation)
- Sélectionner AOP avec en et in faibles
- Technologies : bipolaire (faible en), JFET (faible in)

<h3 class="section-title">8. Facteur de bruit et SNR</h3>

**Rapport Signal sur Bruit (SNR)** :

SNR = Puissance_signal / Puissance_bruit

En dB :
SNR_dB = 10 × log10(Psignal / Pbruit)

ou en tensions RMS :
SNR_dB = 20 × log10(Vsignal_RMS / Vbruit_RMS)

**Facteur de bruit (F)** :

Dégradation du SNR par un système :

F = SNR_entrée / SNR_sortie

**Figure de bruit (NF)** :

NF_dB = 10 × log10(F)

Un système idéal (sans bruit ajouté) a F = 1, NF = 0 dB.

**Température de bruit équivalente** :

Te = T0 × (F - 1)

avec T0 = 290 K (température de référence).

**Formule de Friis (cascade de systèmes)** :

Pour n étages en cascade :

F_total = F1 + (F2 - 1)/G1 + (F3 - 1)/(G1×G2) + ... + (Fn - 1)/(G1×G2×...×Gn-1)

avec Fi : facteur de bruit de l'étage i, Gi : gain en puissance de l'étage i.

**Implications pratiques** :

- Le premier étage domine le bruit total
- Un gain élevé du premier étage réduit l'impact des suivants
- Préamplificateur faible bruit (LNA) crucial en tête de chaîne
- Applications : récepteurs radio, instrumentation

<h3 class="section-title">9. Techniques de réduction du bruit</h3>

**Au niveau conception circuit** :

**Minimiser les impédances** :
Les résistances génèrent du bruit thermique. Utiliser des valeurs raisonnables (1-100 kΩ typiquement).

**Choisir le bon AOP** :
- Application basse impédance de source : minimiser en
- Application haute impédance de source : minimiser in
- Compromis vitesse/bruit (AOP rapides souvent plus bruyants)

**Filtrage adapté** :
Limiter la bande passante au strict nécessaire réduit le bruit intégré.

**Blindage et garde** :
Réduire les interférences électromagnétiques externes.

**Alimentation propre** :
Découplage soigné, régulateurs faible bruit, filtrage secteur.

**Au niveau système** :

**Filtrage optimal** :
Filtre adapté (matched filter) maximise le SNR pour un signal connu dans du bruit blanc.

**Moyennage** :
N mesures moyennées améliorent le SNR de racine(N).

**Détection synchrone (lock-in)** :
Modulation du signal, démodulation synchrone, filtrage passe-bas étroit.

**Techniques numériques** :
Après conversion A/N : filtrage numérique, FFT, corrélation, détection de seuil adaptative.

**Au niveau application** :

**Refroidissement** :
Réduire T diminue le bruit thermique (cryogénie pour applications extrêmes).

**Choix de fréquence de travail** :
Éviter la zone de bruit en 1/f si possible (modulation à fréquence plus haute).

<h3 class="section-title">10. Mesure du bruit</h3>

**Analyseur de spectre** :

Mesure de la densité spectrale de puissance (PSD).

Permet d'identifier :
- Bruit blanc (niveau constant)
- Bruit en 1/f (pente en -10 dB/décade)
- Raies parasites (50/60 Hz secteur, harmoniques)

**Oscilloscope numérique** :

Méthodes :
- Histogramme d'amplitude (distribution du bruit)
- Mesure RMS du signal avec/sans entrée
- FFT pour analyse spectrale

**Multimètre True RMS** :

Mesure directe de la tension RMS de bruit dans une bande passante donnée.

**Méthode pratique** :

1. Court-circuiter l'entrée
2. Mesurer Vout sans signal
3. Ramener en entrée : Vn_RTI = Vout / Gain
4. Comparer avec calculs théoriques

**Précautions** :

- Échauffement (attendre stabilisation thermique)
- Blindage (cage de Faraday si nécessaire)
- Masse unique (éviter boucles de masse)
- Câbles courts et de qualité

<h3 class="section-title">11. Applications pratiques</h3>

**Chaîne d'acquisition biomédicale** :

**ECG (électrocardiogramme)** :
- Signal : 0.5-5 mV
- Bruit acceptable : < 10 µVRMS
- Bande passante : 0.05-150 Hz
- Filtrage : passe-bande + notch 50/60 Hz (réjection secteur)
- Amplification différentielle (CMRR > 100 dB)

**EEG (électroencéphalogramme)** :
- Signal : 10-100 µV
- Bruit : < 1 µVRMS
- Bande : 0.5-70 Hz
- Préampli ultra-faible bruit obligatoire

**Instrumentation scientifique** :

**Amplificateur de charge (piézoélectrique)** :
- Capteur haute impédance
- Intégrateur de courant
- Bruit en courant critique (JFET ou MOSFET)

**Lock-in amplifier** :
- Détection de signaux enfouis dans le bruit
- Modulation + démodulation synchrone
- Filtrage passe-bas très étroit (mHz)
- Applications : spectroscopie, mesures de faibles signaux

**Audio haute-fidélité** :

Spécifications :
- SNR > 90 dB (CD quality : 96 dB)
- Distorsion harmonique < 0.01%
- Filtrage anti-aliasing avant ADC 44.1/48 kHz
- Filtrage de reconstruction après DAC

Filtres de pondération :
- Courbe A (simulation oreille humaine)
- Courbe C (mesures niveau élevé)

**Télécommunications** :

**Récepteur radio** :
- LNA (Low Noise Amplifier) en tête
- Figure de bruit NF < 2 dB typiquement
- Filtres SAW (Surface Acoustic Wave) pour sélectivité
- Cascade : antenne → LNA → filtre → mélangeur → IF

**Conversion A/N haute résolution** :

Filtre anti-aliasing :
- Atténuation > 80 dB à f_Nyquist
- Phase linéaire (Bessel) ou atténuation raide (Chebyshev)
- Transition entre f_utile et f_Nyquist

---

## PART D - Analyse Réflexive et Perspectives

<h3 class="section-title">Compétences acquises</h3>

**Conception de filtres actifs** :
Capacité à synthétiser un filtre depuis les spécifications système (gabarit) jusqu'à l'implémentation électronique avec composants réels.

**Maîtrise du bruit** :
Compréhension physique des sources de bruit, modélisation mathématique, calcul de propagation, et techniques d'optimisation.

**Analyse système** :
Vision globale d'une chaîne d'acquisition : conditionnement analogique, filtrage, conversion A/N, traitement numérique.

**Utilisation d'outils** :
Simulation SPICE pour validation, MATLAB pour synthèse, analyseur de spectre pour mesures.

**Compromis ingénierie** :
Équilibrer sélectivité, phase, bruit, coût, complexité selon l'application.

<h3 class="section-title">Points clés à retenir</h3>

**1. Choix de l'approximation de filtre** :
Pas d'approximation universellement meilleure. Le choix dépend de l'application :
- Audio : Butterworth ou Bessel (réponse douce)
- Anti-aliasing : Chebyshev (transition rapide)
- Télécom : Elliptique (sélectivité maximale)

**2. Bruit = limite fondamentale** :
Le bruit impose une limite physique au plus petit signal détectable. Aucun traitement ne peut retrouver un signal entièrement noyé dans le bruit.

**3. Premier étage critique** :
Le bruit et le gain du premier étage dominent les performances de toute la chaîne (formule de Friis).

**4. Bande passante minimale** :
Limiter la bande passante au strict nécessaire réduit le bruit intégré (proportionnel à racine(Δf)).

**5. Simulation ≠ réalité** :
Les mesures de bruit montrent souvent des contributions parasites non modélisées (alimentation, couplages, CEM).

<h3 class="section-title">Retour d'expérience</h3>

**Richesse du cours** :
Ce module couvre deux domaines vastes et interconnectés. Le filtrage et le bruit sont omniprésents en électronique analogique.

**Importance des TD** :
Les 6 séries de TD avec corrections sont essentielles pour maîtriser les calculs de synthèse de filtres et d'analyse de bruit.

**Annales précieuses** :
Les examens (2016-2022 avec corrections) permettent de comprendre les attendus : synthèse complète de filtre, calcul de bruit multi-sources, optimisation.

**Lien théorie/pratique** :
Les TP ont montré que les filtres réels diffèrent légèrement de la théorie (composants non idéaux, parasites). Le bruit mesuré inclut des contributions non modélisées.

<h3 class="section-title">Applications pratiques</h3>

**Instrumentation de mesure** :
- Oscilloscopes (amplificateurs d'entrée, filtres anti-aliasing)
- Multimètres de précision (filtrage, réjection bruit secteur)
- Analyseurs de spectre (filtres IF, réduction du bruit)

**Biomédical** :
- Moniteurs ECG/EEG (amplification différentielle, filtrage bruit secteur)
- Échographes (traitement signaux ultrasonores)
- Capteurs implantables (ultra-faible bruit et consommation)

**Audio professionnel** :
- Consoles de mixage (égaliseurs actifs, crossovers)
- Systèmes Hi-Fi (filtres de pondération, anti-aliasing)
- Effets audio (filtres accordables, VCF)

**Télécom et RF** :
- Récepteurs (LNA, filtres IF)
- Émetteurs (filtres passe-bande, réjection harmoniques)
- IoT (filtres faible consommation)

**Aéronautique et défense** :
- Radars (filtrage doppler, traitement signal)
- Avionique (instrumentation embarquée haute fiabilité)
- Systèmes critiques (spécifications bruit strictes)

<h3 class="section-title">Limites et ouvertures</h3>

**Limites du module** :
- Peu d'approfondissement sur filtres adaptatifs
- Filtres numériques (DSP) non traités (autre cours)
- Aspects EMC (compatibilité électromagnétique) superficiels

**Ouvertures vers** :
- **Traitement du signal avancé** : filtrage optimal (Wiener, Kalman), détection statistique
- **Circuits intégrés RF** : conception LNA, VCO, mélangeurs
- **Systèmes mixtes** : interfaces analog-digital, ADC/DAC haute résolution
- **Électronique quantique** : limites ultimes du bruit (bruit quantique)

<h3 class="section-title">Évolutions technologiques</h3>

**Filtres programmables** :

Circuits intégrés modernes permettent de configurer filtres par logiciel :
- Fréquence de coupure ajustable
- Type de filtre sélectionnable (Butterworth, Chebyshev...)
- Gain programmable

Exemples : MAX7400 (Maxim), LTC1563 (Linear Technology).

**Filtrage hybride** :

Combinaison analog/digital :
- Filtrage analogique grossier (anti-aliasing)
- Sur-échantillonnage ADC
- Filtrage numérique précis (FIR, IIR)

**Composants faible bruit nouvelle génération** :

- AOP ultra-faible bruit : < 1 nV/racine(Hz)
- Technologies BiCMOS, SiGe pour RF
- MEMS et capteurs intelligents avec préampli intégré

**Intelligence artificielle** :

Filtrage adaptatif par réseaux de neurones :
- Apprentissage du signal utile vs bruit
- Suppression de bruit en temps réel
- Applications : audio (réduction bruit actif), radar (clutter rejection)

<h3 class="section-title">Conseils pour réussir</h3>

**1. Maîtriser les bases théoriques** :
Fonctions de transfert, pôles/zéros, diagrammes de Bode sont fondamentaux. Sans eux, impossible de concevoir des filtres.

**2. Pratiquer les synthèses** :
Refaire les TD de synthèse jusqu'à maîtriser la démarche complète (spécifications → approximation → cellules → composants).

**3. Comprendre le bruit physiquement** :
Savoir d'où vient chaque type de bruit (thermique, grenaille, 1/f) aide à le modéliser et le réduire.

**4. Utiliser les annales** :
Les examens 2016-2022 sont représentatifs. S'entraîner sur ces sujets avec corrections.

**5. Simuler systématiquement** :
SPICE permet de vérifier les calculs, d'explorer les sensibilités, et de visualiser le bruit.

**6. Ordre de grandeur** :
Mémoriser quelques valeurs typiques (bruit d'une résistance de 10 kΩ ≈ 13 nV/racine(Hz), AOP bipolaire en ≈ 5 nV/racine(Hz)) pour détecter les erreurs.

<h3 class="section-title">Conclusion</h3>

Ce module est essentiel pour tout ingénieur travaillant sur des systèmes d'acquisition de signaux. Le filtrage et le bruit déterminent la qualité finale et les limites de performance d'un système.

**Compétences transférables** :
- Conception rigoureuse depuis spécifications système
- Modélisation de phénomènes physiques (bruit)
- Optimisation multi-critères (sélectivité, phase, bruit, coût)
- Vision système (chaîne complète d'acquisition)

**Pertinence professionnelle** :
Ces compétences sont recherchées dans de nombreux domaines : instrumentation, biomédical, audio, télécommunications, aéronautique, automobile (capteurs).

**Message principal** :
Le filtrage analogique reste indispensable malgré l'essor du numérique (conditionnement avant ADC, applications RF). Le bruit est une limite fondamentale qui ne peut être ignorée. Concevoir des systèmes performants nécessite de maîtriser ces deux aspects.

**Recommandations** :
- Approfondir par projets pratiques (conception et test de filtres, mesures de bruit)
- Explorer les outils professionnels (FilterPro de TI, ADIsimPE d'Analog Devices)
- Étudier des designs commerciaux (datasheets de MAX7400, LTC1563, AD8429)
- Se former au traitement numérique du signal (complément indispensable)
- Suivre les évolutions en circuits intégrés (technologies BiCMOS, SiGe, GaN)

**Liens avec les autres cours** :
- [Circuits et Filtres analogiques - S5](./circuits-filtres-analogiques.html) : fondements
- [Filtrage numérique - S6](./filtrage-numerique.html) : complémentarité analog/digital
- [Chaînes électroniques acquisition - S8](./chaines-acquisition.html) : intégration système
- [Signaux aléatoires - S6](./signaux-aleatoires.html) : modélisation probabiliste du bruit

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
      <h4>📖 Cours Filtrage Actif</h4>
      <p>Cours complet sur le filtrage actif : structures Sallen-Key, Rauch, topologies d'ordre supérieur et synthèse de filtres.</p>
      <embed src="/cours-pdf/S7/Filtrage-Actif-Bruit/cours-filtrage.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Filtrage-Actif-Bruit/cours-filtrage.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>📖 Bruit dans les AOP</h4>
      <p>Modélisation des sources de bruit dans les amplificateurs opérationnels : bruit thermique, flicker, calcul du bruit total.</p>
      <embed src="/cours-pdf/S7/Filtrage-Actif-Bruit/bruit-ao.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Filtrage-Actif-Bruit/bruit-ao.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>📖 Structure Sallen-Key</h4>
      <p>Cours sur la topologie Sallen-Key : principe, conception, sensibilité aux composants et réalisation pratique.</p>
      <embed src="/cours-pdf/S7/Filtrage-Actif-Bruit/sallen-key.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Filtrage-Actif-Bruit/sallen-key.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
  </div>
</div>

---

*Cours suivi en 2023-2024 à l'INSA Toulouse, Département Génie Électrique et Informatique.*

<div class="back-nav">
    <a href="./my-courses-2023-2024.html">← Retour aux Cours 2023-2024</a>
</div>

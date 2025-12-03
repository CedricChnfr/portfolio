---
layout: default
title: "📊 Chaînes Électroniques d'Acquisition de l'Information - Semestre 8"
date: 2024-10-02 10:56:03 +0200
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
    <a href="./my-courses-2023-2024.html">← Retour aux Cours 2023-2024</a>
</div>

# 📊 Chaînes Électroniques d'Acquisition de l'Information - Semestre 8

**Année académique** : 2023-2024  
**ECTS** : 2.5  
**Catégorie** : Électronique Analogique et Instrumentation

---

## PART A - Présentation Générale du Module

<h3 class="section-title">Vue d'ensemble</h3>

Ce cours couvre la conception complète des systèmes d'acquisition de données, depuis le capteur jusqu'au traitement numérique. Il traite du conditionnement de signaux analogiques, de la conversion analogique-numérique, des interfaces de communication, et des architectures de chaînes d'acquisition pour applications industrielles, médicales, et scientifiques.

**Objectifs pédagogiques** :
- Concevoir une chaîne d'acquisition complète du capteur au microcontrôleur
- Maîtriser le conditionnement de signaux analogiques
- Comprendre les convertisseurs analogique-numérique et numérique-analogique
- Implémenter les interfaces de communication SPI, I2C, UART
- Analyser le budget de bruit et optimiser le rapport signal sur bruit
- Dimensionner les filtres anti-repliement et de reconstruction
- Choisir les composants selon un cahier des charges

<h3 class="section-title">Position dans le cursus</h3>

Ce module fait la synthèse de plusieurs compétences acquises :
- **Circuits Analogiques (S5, S7)** : amplificateurs opérationnels, filtres actifs
- **Signal (S5)** : échantillonnage, théorème de Shannon, filtrage
- **Microcontrôleurs (S6)** : interfaces, protocoles de communication
- **Filtrage Numérique (S6)** : traitement post-acquisition

Il prépare à :
- **Machine Learning (S8)** : acquisition de données pour apprentissage
- **Temps Réel (S8)** : contraintes temporelles des acquisitions
- **Projets industriels** : systèmes embarqués avec capteurs
- **Instrumentation professionnelle** : conception de systèmes de mesure

---

## PART B - Expérience Personnelle et Contexte d'Apprentissage

<h3 class="section-title">Organisation et ressources</h3>

Le module était structuré en cours magistraux et travaux dirigés pratiques :

**Cours magistraux (15h)** :
- **CM1** : Amplificateurs d'instrumentation, conditionneurs de signaux
- **CM2** : Interfaces numériques I2C et SPI, connexion capteurs numériques, UART
- **CM3** : Convertisseurs analogique-numérique (CAN) et numérique-analogique (CNA)
- **CM4** : Compression dynamique, codecs audio
- **CM5** : Architectures avancées de convertisseurs

**Travaux dirigés (12h)** :
- **TD1** : Multiplexage de capteurs automobiles, CAN
- **TD2** : Dimensionnement de chaînes d'acquisition
- **TD3** : Lois en A (compression audio)
- **TD4** : Dalle tactile résistive
- **TD5** : Architectures de convertisseurs
- **TD6** : Chaîne d'acquisition Bluetooth Low Energy
- **TD7** : Projet complet

**Ressources** :
- 10 polycopiés de cours (ampli instrumentation, interfaces, CAN/CNA, codecs)
- 7 TD avec applications pratiques
- Annales : 6 sujets d'examens avec corrections (2014-2023)
- Logiciel LTspice pour simulation de circuits

<h3 class="section-title">Méthodologie d'étude</h3>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S8/chaines-acquisition/chaine-acquisition.svg" alt="Chaîne d'acquisition de données" 
       style="max-width: 550px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Architecture complète d'une chaîne d'acquisition de données</p>
</div>

**Phase 1 : Comprendre l'architecture globale** :
Assimiler la chaîne complète : capteur → conditionnement → conversion → traitement → communication.

**Phase 2 : Maîtriser chaque bloc** :
Étudier en détail chaque étage (amplification, filtrage, conversion) avec ses paramètres critiques.

**Phase 3 : Dimensionnement pratique** :
S'exercer sur les TD à choisir les composants selon un cahier des charges (résolution, bande passante, SNR).

**Phase 4 : Simulation** :
Utiliser LTspice pour valider les circuits de conditionnement et filtres avant réalisation.

**Phase 5 : Approche système** :
Développer une vision d'ensemble en considérant les compromis (coût, performance, consommation).

<h3 class="section-title">Difficultés rencontrées</h3>

**Multiplicité des paramètres** :
Chaque composant a de nombreuses spécifications (offset, dérive thermique, CMRR, bruit). Identifier les critiques selon l'application demande de l'expérience.

**Budget de bruit** :
Calculer le bruit total de la chaîne en combinant toutes les sources est complexe mais essentiel pour atteindre le SNR requis.

**Choix des composants** :
Face à des centaines de références d'ADC ou d'amplificateurs, sélectionner le bon compromis performance/coût/disponibilité n'est pas évident.

**Interfaces de communication** :
Maîtriser les protocoles SPI, I2C, UART avec leurs timings, leurs limitations, et leur implémentation pratique demande de la pratique.

---

## PART C - Aspects Techniques Détaillés

<h3 class="section-title">1. Architecture générale d'une chaîne d'acquisition</h3>

**Principe de fonctionnement** :

Une chaîne d'acquisition transforme une grandeur physique (température, pression, vibration, etc.) en données numériques exploitables par un système informatique.

**Blocs fonctionnels** :

Grandeur physique → Capteur → Conditionnement → Filtrage anti-repliement → Conversion A/N → Interface numérique → Traitement

**Spécifications essentielles** :

| Paramètre | Description | Exemple |
|-----------|-------------|---------|
| Étendue de mesure | Plage des valeurs à acquérir | 0-100°C, ±10V |
| Résolution | Plus petit changement détectable | 0.1°C, 1mV |
| Précision | Erreur maximale | ±0.5% |
| Bande passante | Fréquences du signal | DC-10kHz |
| Fréquence d'échantillonnage | Nombre d'échantillons par seconde | 44.1 kHz (audio) |
| Rapport signal/bruit (SNR) | Qualité du signal | 90 dB |
| Temps de réponse | Latence de la mesure | 10 ms |

<h3 class="section-title">2. Capteurs et transducteurs</h3>

**Rôle du capteur** :

Convertir une grandeur physique en signal électrique (tension, courant, résistance, capacité).

**Principales familles de capteurs** :

**Capteurs résistifs** :
- **Thermistances (CTN/CTP)** : résistance varie avec température
- **Jauges de contrainte** : résistance varie avec déformation mécanique
- **Potentiomètres** : résistance varie avec position

**Capteurs capacitifs** :
- Variation de capacité avec distance, pression, humidité
- Haute impédance nécessitant conditionnement spécifique

**Thermocouples** :
- Tension proportionnelle à différence de température (effet Seebeck)
- Nécessite compensation de soudure froide

**Capteurs piézoélectriques** :
- Génération de charge sous contrainte mécanique
- Accéléromètres, microphones, capteurs de pression dynamique
- Ne mesurent que les variations (signaux AC)

**Capteurs à effet Hall** :
- Tension proportionnelle au champ magnétique
- Mesure de courant sans contact, position, vitesse de rotation

**Capteurs optiques** :
- Photodiodes, phototransistors
- Courant proportionnel à l'intensité lumineuse

<h3 class="section-title">3. Conditionnement de signaux</h3>

**Objectif** :

Adapter le signal du capteur pour optimiser la plage d'entrée du convertisseur A/N.

**Amplificateur d'instrumentation** :

Composant clé pour signaux différentiels faibles.

**Caractéristiques principales** :
- Très haute impédance d'entrée (> 1 GΩ) : ne charge pas la source
- Excellent CMRR (> 100 dB) : rejette le bruit en mode commun
- Faible offset et dérive thermique
- Gain ajustable par une résistance externe

**Application typique** : amplification de signaux de jauges de contrainte, thermocouples.

**Pont de Wheatstone** :

Montage pour mesurer de faibles variations de résistance (jauges de contrainte).

**Configurations** :
- **Quart de pont** : 1 jauge active (sensibilité 1x, température non compensée)
- **Demi-pont** : 2 jauges actives (sensibilité 2x, compensation partielle)
- **Pont complet** : 4 jauges actives (sensibilité 4x, compensation complète)

**Amplificateur de charge** :

Pour capteurs piézoélectriques qui génèrent une charge électrique.

Circuit intégrateur avec AOP convertissant la charge en tension.

**Linéarisation** :

Certains capteurs ont une réponse non linéaire (thermistances).

Techniques de linéarisation :
- Réseau de résistances
- Linéarisation numérique (table de conversion ou polynôme)

<h3 class="section-title">4. Filtrage anti-repliement</h3>

**Problème du repliement spectral (aliasing)** :

Si la fréquence d'échantillonnage Fe est insuffisante par rapport au signal, les composantes haute fréquence sont repliées vers les basses fréquences, créant une distorsion irréversible.

**Théorème de Shannon-Nyquist** :

Pour éviter le repliement, la fréquence d'échantillonnage doit être au moins le double de la fréquence maximale du signal :

Fe ≥ 2 × Fmax

**Filtre anti-repliement** :

Filtre passe-bas analogique placé avant le convertisseur A/N pour éliminer les fréquences au-delà de Fe/2.

**Paramètres de conception** :
- **Fréquence de coupure** : juste au-dessus de la bande utile du signal
- **Ordre** : typiquement 4 à 8 pour pente suffisamment raide
- **Type** : Butterworth (réponse plate en bande passante), Bessel (phase linéaire pour préserver la forme temporelle)

**Implémentation** :
- Filtres actifs à AOP : performances élevées, besoin alimentation
- Filtres à capacités commutées : intégration, accordabilité numérique

<h3 class="section-title">5. Conversion analogique-numérique (ADC)</h3>

**Paramètres fondamentaux** :

**Résolution (N bits)** :

Nombre de niveaux de quantification : 2 puissance N

Exemples :
- 8 bits : 256 niveaux
- 12 bits : 4096 niveaux
- 16 bits : 65536 niveaux
- 24 bits : 16.7 millions de niveaux

**Quantum (LSB)** :

Plus petit pas de quantification.

Si Vref = 5V et N = 12 bits, alors LSB = 5V / 4096 ≈ 1.22 mV

**Fréquence d'échantillonnage (Fe)** :

Nombre d'échantillons par seconde (Hz ou SPS - Samples Per Second).

**ENOB (Effective Number Of Bits)** :

Résolution effective tenant compte du bruit et de la non-linéarité, calculée à partir du SNR mesuré.

Souvent inférieure à la résolution nominale (ADC 16 bits → ENOB 14 bits typique).

**INL et DNL** :
- **INL** (Integral Non-Linearity) : écart maximum de la courbe de transfert par rapport à la droite idéale
- **DNL** (Differential Non-Linearity) : variation de la largeur des codes de quantification

<h3 class="section-title">6. Architectures de convertisseurs A/N</h3>

**Convertisseur Flash (parallèle)** :

Principe : 2^N - 1 comparateurs en parallèle comparent le signal à différentes tensions de référence.

**Caractéristiques** :
- Très rapide (quelques nanosecondes)
- Consommation et surface importantes
- Limité à faible résolution (6-8 bits)
- Applications : oscilloscopes ultra-rapides, radar

**Convertisseur à Approximations Successives (SAR)** :

Principe : algorithme de recherche dichotomique (comme une balance à fléau).

En N étapes, teste successivement chaque bit du MSB au LSB.

**Caractéristiques** :
- Bon compromis vitesse/résolution
- 8 à 18 bits, 100 kSPS à quelques MSPS
- Faible consommation
- Le plus répandu pour applications générales
- Applications : acquisition industrielle, instrumentation, capteurs

**Convertisseur Pipeline** :

Principe : plusieurs étages en cascade, chaque étage résout quelques bits.

**Caractéristiques** :
- Haute vitesse (> 100 MSPS)
- 10 à 14 bits typique
- Latence de plusieurs cycles (pipeline)
- Applications : communications, vidéo, imagerie

**Convertisseur Sigma-Delta (ΔΣ)** :

Principe : sur-échantillonnage massif + mise en forme du bruit (noise shaping) + filtrage numérique.

**Caractéristiques** :
- Très haute résolution (16 à 24 bits)
- Vitesse modérée (quelques kHz à quelques MHz)
- Excellente linéarité
- Filtre anti-repliement simplifié (sur-échantillonnage)
- Applications : audio, instrumentation de précision, pesage

**Convertisseur Double Rampe** :

Principe : intégration du signal puis décharge à vitesse constante, mesure du temps.

**Caractéristiques** :
- Très haute résolution
- Très lent (10-100 échantillons/seconde)
- Excellent rejet du bruit 50/60 Hz (temps d'intégration multiple de 20ms)
- Applications : multimètres, balances, instrumentation DC précise

**Tableau comparatif** :

| Architecture | Résolution | Vitesse | Consommation | Applications typiques |
|--------------|------------|---------|--------------|------------------------|
| Flash | 6-8 bits | > 1 GSPS | Élevée | Oscilloscopes, radar |
| SAR | 8-18 bits | 100 kSPS - 5 MSPS | Faible | Acquisition générale |
| Pipeline | 10-14 bits | 10-500 MSPS | Moyenne | Communications, vidéo |
| Sigma-Delta | 16-24 bits | 10 SPS - 10 MSPS | Faible | Audio, instrumentation |
| Double rampe | 16-24 bits | 10-100 SPS | Très faible | Multimètres, pesage |

<h3 class="section-title">7. Conversion numérique-analogique (DAC)</h3>

**Rôle** :

Reconstituer un signal analogique à partir de données numériques.

Applications : génération de signaux, audio, commande de moteurs, télécommunications.

**Architectures principales** :

**DAC à réseau R-2R** :

Réseau de résistances de valeurs R et 2R commutées selon les bits.

Avantages : simple, deux valeurs de résistances seulement.

**DAC à résistances pondérées** :

Chaque bit contrôle une résistance de poids différent (R, R/2, R/4, etc.).

Problème : grande dispersion des valeurs pour haute résolution.

**DAC Sigma-Delta** :

Sur-échantillonnage + modulation 1-bit + filtrage analogique.

Haute résolution pour audio.

**Filtre de reconstruction** :

Le signal en sortie du DAC est en escalier (échantillonné).

Un filtre passe-bas lisse le signal et élimine les images spectrales (répliques du spectre autour de multiples de Fe).

<h3 class="section-title">8. Interfaces de communication numériques</h3>

**SPI (Serial Peripheral Interface)** :

**Caractéristiques** :
- 4 fils : CLK (horloge), MOSI (Master Out Slave In), MISO (Master In Slave Out), CS (Chip Select)
- Communication full-duplex (émission et réception simultanées)
- Vitesse élevée (plusieurs dizaines de MHz)
- Architecture maître-esclaves (un maître, plusieurs esclaves)
- Pas de protocole d'acquittement (pas de détection d'erreur automatique)

**Applications** : ADC, DAC, mémoires Flash, écrans, capteurs haute vitesse.

**I2C (Inter-Integrated Circuit)** :

**Caractéristiques** :
- 2 fils : SDA (données), SCL (horloge)
- Multi-maîtres possible (arbitrage)
- Adressage sur 7 ou 10 bits (jusqu'à 128 ou 1024 dispositifs)
- Vitesses : 100 kHz (standard), 400 kHz (fast), 3.4 MHz (high-speed)
- Protocole avec acquittement (ACK/NACK)

**Applications** : capteurs, mémoires EEPROM, RTC, circuits d'extension I/O, nombreux capteurs numériques.

**UART (Universal Asynchronous Receiver-Transmitter)** :

**Caractéristiques** :
- Communication série asynchrone (pas d'horloge partagée)
- 2 fils : TX (transmission), RX (réception) + masse
- Vitesses standards (bauds) : 9600, 19200, 38400, 115200, etc.
- Configuration : bits de données (7-8), bit de parité (optionnel), bits de stop (1-2)
- Longues distances possibles avec niveaux RS-232 (±12V)

**Applications** : liaison PC, communication entre microcontrôleurs, GPS, modules Bluetooth/WiFi, consoles de débogage.

**Comparaison** :

| Critère | SPI | I2C | UART |
|---------|-----|-----|------|
| Fils | 4 + 1 par esclave | 2 | 2 + masse |
| Vitesse | Très rapide (MHz) | Moyenne (kHz) | Lente (kbaud) |
| Complexité | Simple | Moyenne | Simple |
| Multi-dispositifs | Oui (CS multiples) | Oui (adressage) | Non (point à point) |
| Distance | Courte (PCB) | Courte (PCB) | Longue possible |

<h3 class="section-title">9. Analyse du bruit et SNR</h3>

**Sources de bruit** :

**Bruit du capteur** :
- Bruit thermique (Johnson-Nyquist) des résistances
- Bruit de grenaille (shot noise)
- Bruit en 1/f (flicker noise)

**Bruit du conditionnement** :
- Bruit en tension et en courant de l'amplificateur
- Bruit des résistances du circuit

**Bruit de quantification** :

Erreur introduite par la quantification sur N bits.

Valeur RMS du bruit : quantum / racine(12)

**Bruit de l'ADC** :
- Bruit thermique interne
- Jitter d'échantillonnage (incertitude sur instant d'échantillonnage)

**Budget de bruit** :

Calcul du bruit total en combinant toutes les sources (somme quadratique car sources indépendantes).

Le SNR système est le rapport entre l'amplitude du signal et le bruit total.

**Objectif** : identifier le maillon limitant pour optimiser les efforts.

<h3 class="section-title">10. Techniques d'amélioration du SNR</h3>

**Moyennage** :

Calculer la moyenne de N mesures réduit le bruit d'un facteur racine(N).

Exemple : moyenner 100 mesures divise le bruit par 10.

Inconvénient : réduit la bande passante (temps d'acquisition multiplié par N).

**Filtrage numérique** :

Après conversion, filtrer numériquement pour réduire la bande passante au strict nécessaire.

Types : moyennage mobile, filtres FIR, IIR.

**Sur-échantillonnage** :

Échantillonner à fréquence supérieure au minimum requis, puis sous-échantillonner après filtrage numérique.

Améliore le SNR pour bruit blanc (gain de 3 dB par doublement de fréquence).

Technique exploitée par les ADC Sigma-Delta.

**Modulation-démodulation synchrone (Lock-in)** :

Pour signaux très faibles noyés dans le bruit :
- Moduler le signal à mesurer à une fréquence connue
- Après acquisition, démoduler en multipliant par référence synchrone
- Filtrer pour extraire uniquement le signal utile

Excellente réjection du bruit hors de la fréquence de modulation.

Utilisée en instrumentation scientifique de précision.

<h3 class="section-title">11. Applications spécifiques</h3>

**Acquisition audio** :

**Spécifications** :
- Résolution : 16 bits (CD), 24 bits (studio)
- Fréquence : 44.1 kHz, 48 kHz, 96 kHz, 192 kHz
- SNR élevé : > 90 dB (16 bits), > 110 dB (24 bits)
- Faible distorsion harmonique (THD < 0.01%)

**Composants** : codecs audio intégrant ADC + DAC, amplificateurs casque.

**Instrumentation médicale (ECG, EEG)** :

**Spécifications** :
- Signaux très faibles (µV pour EEG)
- Isolation galvanique obligatoire (protection patient)
- Filtres spécifiques (rejet 50/60 Hz, passe-haut pour dérive baseline)
- Conformité normes médicales strictes

**Composants** : amplificateurs d'instrumentation médicaux, ADC 24 bits, isolateurs.

**Acquisition industrielle** :

**Spécifications** :
- Robustesse (température étendue, vibrations, EMI)
- Interfaces industrielles (4-20 mA, 0-10V)
- Isolation galvanique pour sécurité
- Auto-diagnostic et détection de défauts

**Acquisition haute vitesse** :

**Applications** : oscilloscopes numériques, radar, instrumentation RF.

**Spécifications** :
- Fréquences d'échantillonnage GSPS (milliards d'échantillons/seconde)
- Architectures parallèles (interleaving de plusieurs ADC)
- Traitement temps réel sur FPGA
- Mémoires rapides (DDR)

<h3 class="section-title">12. Conception de PCB pour signaux mixtes</h3>

**Règles essentielles** :

**Séparation analogique/numérique** :
- Plans de masse séparés, connectés en un seul point (star ground)
- Séparation physique des sections analogiques et numériques sur le PCB

**Routage** :
- Pistes courtes pour signaux sensibles
- Éviter parallèles entre pistes analogiques et numériques (couplage)
- Gardes de masse autour des signaux critiques

**Alimentation** :
- Alimentations séparées analogiques et numériques
- Régulateurs faible bruit (LDO) pour circuits analogiques
- Découplage systématique (condensateurs au plus près des composants)

**Blindage** :
- Boîtier métallique connecté à la masse si environnement bruité
- Plans de masse continue pour réduire impédance de retour

---

## PART D - Analyse Réflexive et Perspectives

<h3 class="section-title">Compétences acquises</h3>

**Vision système complète** :
Capacité à concevoir une chaîne d'acquisition de bout en bout en considérant tous les maillons et leurs interactions.

**Dimensionnement de circuits** :
Aptitude à choisir les composants (amplificateurs, filtres, ADC) selon un cahier des charges (résolution, bande passante, SNR, coût).

**Analyse de performances** :
Compétence pour calculer le budget de bruit, évaluer le SNR, identifier les limitations et optimiser les performances.

**Maîtrise des interfaces** :
Capacité à implémenter et déboguer les protocoles SPI, I2C, UART pour connecter capteurs et microcontrôleurs.

**Approche méthodologique** :
Développement d'une démarche rigoureuse : spécifications → choix architecture → dimensionnement → simulation → validation.

<h3 class="section-title">Points clés à retenir</h3>

**1. Approche système indispensable** :
Optimiser un seul maillon ne suffit pas. Il faut considérer la chaîne complète pour atteindre les performances globales.

**2. Le bruit est omniprésent** :
Dans les systèmes réels, le bruit limite les performances. Savoir le caractériser, le minimiser et vivre avec est essentiel.

**3. Compromis permanents** :
Résolution vs vitesse, performance vs coût, précision vs consommation. Chaque choix est un équilibre selon l'application.

**4. Le filtrage anti-repliement est crucial** :
Un ADC rapide et précis ne sert à rien sans filtre anti-repliement adapté. L'aliasing détruit l'information de façon irréversible.

**5. Datasheet = document de travail** :
Les datasheets contiennent toutes les informations nécessaires. Apprendre à les lire et les exploiter est une compétence clé.

<h3 class="section-title">Retour d'expérience</h3>

**Aspect formateur** :
Ce cours est très concret et directement applicable. Contrairement à des cours plus théoriques, chaque notion trouve immédiatement une traduction pratique dans un système réel.

**Complexité du conditionnement** :
Le conditionnement de signal est un art délicat : amplifier suffisamment pour exploiter la dynamique de l'ADC, sans saturer, tout en minimisant le bruit. Trouver le bon équilibre demande de l'expérience.

**Choix des composants** :
Face à des centaines de références d'ADC, d'amplificateurs d'instrumentation, de capteurs, faire le bon choix est difficile. Les TD ont permis de développer une méthodologie de sélection.

**Importance de la simulation** :
LTspice et autres simulateurs permettent de valider les circuits avant fabrication. C'est un gain de temps considérable et une source d'apprentissage.

<h3 class="section-title">Applications pratiques</h3>

**Pour ingénieur en électronique embarquée** :
- Concevoir des systèmes IoT avec multiples capteurs
- Dimensionner des cartes d'acquisition de données
- Interfacer capteurs avec microcontrôleurs
- Optimiser consommation et performances

**Pour ingénieur en instrumentation** :
- Concevoir des appareils de mesure scientifiques
- Développer des équipements médicaux
- Réaliser des systèmes de test et validation
- Assurer conformité aux normes (précision, sécurité)

**Pour ingénieur en automobile** :
- Acquérir données de multiples capteurs (pression, température, accélération, etc.)
- Bus de communication (CAN, LIN, FlexRay)
- Contraintes sévères (température, vibrations, EMI)

**Pour ingénieur en audio** :
- Concevoir des interfaces audio (microphones, casques)
- Développer des équipements d'enregistrement
- Optimiser qualité sonore (SNR, THD)

<h3 class="section-title">Limites et ouvertures</h3>

**Limites du module** :
- Peu de travaux pratiques en laboratoire (surtout TD théoriques)
- Pas de projet complet de conception et fabrication de PCB
- Aspects logiciels (drivers, traitement temps réel) peu approfondis

**Ouvertures vers** :
- **Traitement du signal avancé** : filtrage adaptatif, analyse spectrale
- **Systèmes temps réel** : contraintes temporelles, RTOS
- **Machine Learning embarqué** : prétraitement et classification de données capteurs
- **IoT et communication sans fil** : BLE, LoRa, WiFi pour systèmes connectés

<h3 class="section-title">Évolutions récentes</h3>

**Intégration accrue** :

Tendance vers System-on-Chip (SoC) intégrant capteurs, ADC, traitement, communication.

Exemples : MCU avec ADC 16 bits intégrés, SoC Bluetooth avec ADC/DAC.

Avantages : compacité, faible coût, consommation réduite.

**Capteurs MEMS** :

Microsystèmes électromécaniques miniaturisés et intégrés.

Accéléromètres, gyroscopes, microphones, capteurs de pression sur silicium.

Révolutionnent l'électronique grand public (smartphones, wearables).

**Edge Computing** :

Traitement des données au plus près du capteur (au lieu du cloud).

Permet réduction latence, bande passante, et préservation vie privée.

Nécessite ADC efficaces et traitement embarqué optimisé.

**IA embarquée** :

Réseaux de neurones sur microcontrôleurs pour classification temps réel (reconnaissance vocale, détection d'anomalies).

Chaînes d'acquisition optimisées pour prétraitement avant inférence.

<h3 class="section-title">Conseils pour réussir</h3>

**1. Comprendre la physique** :
Derrière chaque composant, il y a un phénomène physique. Comprendre la physique aide à anticiper les limitations et optimiser.

**2. Lire les datasheets attentivement** :
Les datasheets contiennent tout : caractéristiques électriques, schémas d'application, conditions de fonctionnement. Apprendre à les exploiter méthodiquement.

**3. Simuler avant de fabriquer** :
LTspice, TINA, autres simulateurs permettent de valider les circuits rapidement. Investir du temps en simulation évite des erreurs coûteuses.

**4. Faire des calculs de budget de bruit** :
Systématiquement évaluer chaque source de bruit pour identifier le maillon limitant et concentrer les efforts.

**5. Tester et mesurer** :
La théorie donne le cadre, mais la pratique révèle les subtilités (couplages, dérives, interférences). Mesurer pour valider.

**6. Développer l'intuition** :
Avec l'expérience, développer un sens des ordres de grandeur (bruit typique d'un AOP, résolution nécessaire selon application, etc.).

<h3 class="section-title">Conclusion</h3>

Ce module est fondamental pour tout ingénieur travaillant sur des systèmes embarqués, de l'instrumentation, ou de l'IoT. L'acquisition de données est omniprésente : smartphones, automobiles, industrie, médical, domotique, etc.

**Compétences transférables** :
- Vision système et approche méthodique
- Capacité à dimensionner et optimiser des systèmes complexes
- Maîtrise des interfaces de communication (indispensable pour tout système embarqué)
- Compréhension profonde du compromis analogique/numérique

**Pertinence professionnelle** :
L'explosion de l'IoT et des systèmes connectés accroît la demande d'ingénieurs maîtrisant les chaînes d'acquisition. Ces compétences sont recherchées dans tous les secteurs.

**Message principal** :
Une chaîne d'acquisition n'est performante que si tous les maillons sont cohérents. Le meilleur ADC du monde ne compensera pas un conditionnement mal conçu ou un capteur inadapté. L'approche système est la clé.

**Recommandations** :
- Approfondir par des projets personnels (Arduino, Raspberry Pi avec capteurs)
- Étudier des designs de référence (circuits d'application dans datasheets)
- Pratiquer la simulation (LTspice gratuit et puissant)
- Suivre des tutoriels sur interfaces (SPI, I2C) avec oscilloscope logique
- Réaliser un projet complet : capteur → conditionnement → ADC → microcontrôleur → affichage/transmission

**Liens avec les autres cours** :
- [Filtrage Actif et Bruit - S7](./filtrage-actif-bruit.html) : filtres analogiques, sources de bruit
- [Microcontrôleurs - S6](./microcontroleurs.html) : interfaces SPI/I2C/UART
- [Filtrage Numérique - S6](./filtrage-numerique.html) : traitement post-acquisition
- [Signal - S5](./signal.html) : échantillonnage, théorème de Shannon
- [Machine Learning - S8](./machine-learning.html) : prétraitement de données capteurs

---

*Cours suivi en 2023-2024 à l'INSA Toulouse, Département Génie Électrique et Informatique.*

<div class="back-nav">
    <a href="./my-courses-2023-2024.html">← Retour aux Cours 2023-2024</a>
</div>

#### 2. Capteurs et Transducteurs

**Principe**:
Conversion d'une grandeur physique en signal électrique.

**Types de capteurs**:

**Résistifs**:
- **Thermistance**: résistance varie avec température
  - CTN (Coefficient Température Négatif)
  - CTP (Coefficient Température Positif)
- **Jauge de contrainte**: résistance varie avec déformation
  - Pont de Wheatstone pour mesure précise
- **Potentiomètre**: position linéaire ou angulaire

**Capacitifs**:
- Variation de capacité avec distance, pression, humidité
- Haute impédance, sensible aux parasites

**Inductifs**:
- LVDT (Linear Variable Differential Transformer)
- Capteurs de proximité inductifs

**Piézoélectriques**:
- Génération de charge sous contrainte mécanique
- Accéléromètres, microphones, capteurs de pression dynamique
- Signal AC seulement (ne mesure pas statique)

**Thermocouples**:
- Tension proportionnelle à différence de température
- Effet Seebeck
- Compensation soudure froide nécessaire

**Capteurs à effet Hall**:
- Tension proportionnelle au champ magnétique
- Mesure de courant (sans contact), position, vitesse

**Photodiodes et phototransistors**:
- Courant proportionnel à lumière incidente
- Détection optique, codeurs rotatifs

#### 3. Conditionnement de Signal

**Amplification**:

**Amplificateur d'instrumentation**:
```
Structure à 3 AOP:
- Haute impédance d'entrée (>1GΩ)
- Fort CMRR (>100dB)
- Gain ajustable par une résistance
```

Utilisé pour amplifier signaux différentiels faibles (jauges, thermocouples).

**Amplificateur de charge**:
```
Pour capteurs piézoélectriques:
Vout = -Q/Cf
où Q est la charge générée, Cf capacité de feedback
```

**Pont de Wheatstone**:
```
Pour jauges de contrainte:
Vout = Vexc × (ΔR/R) / 4  (petites variations)
```

Configurations:
- **Quart de pont**: 1 jauge active
- **Demi-pont**: 2 jauges actives
- **Pont complet**: 4 jauges actives (meilleure sensibilité, compensation température)

**Linéarisation**:
Certains capteurs ont réponse non-linéaire (thermistance).
Techniques:
- Pont de Wheatstone modifié
- Réseau de linéarisation
- Linéarisation numérique post-conversion

**Isolation galvanique**:
- Amplificateur d'isolation
- Opto-coupleurs
- Transformateurs
Protection et élimination de boucles de masse.

#### 4. Filtrage Anti-Repliement

**Théorème de Shannon-Nyquist**:
```
Fréquence d'échantillonnage Fe ≥ 2 × Fmax

où Fmax est la fréquence maximale du signal
```

**Repliement spectral (Aliasing)**:
Si Fe insuffisant, composantes haute fréquence sont repliées en basse fréquence, causant distorsion irréversible.

**Filtre anti-repliement (anti-aliasing)**:
Passe-bas analogique avant conversion A/N.

**Spécifications**:
- **Fréquence de coupure**: juste au-dessus de la bande utile
- **Pente**: suffisamment raide pour atténuer au-delà de Fe/2
- **Ordre**: généralement 4 à 8
- **Type**: Butterworth (réponse plate), Bessel (phase linéaire)

**Implémentation**:
- Filtres passifs (R,L,C): simples, limités en performance
- Filtres actifs (AOP): meilleure caractéristique, besoin alimentation
- Filtres à capacités commutées: intégration, accordabilité

#### 5. Conversion Analogique-Numérique

**Paramètres clés**:

**Résolution (N bits)**:
```
Nombre de niveaux = 2^N
LSB (quantum) = Vref / 2^N
```

Exemples:
- 8 bits: 256 niveaux
- 12 bits: 4096 niveaux
- 16 bits: 65536 niveaux
- 24 bits: 16.7 millions de niveaux

**Fréquence d'échantillonnage (Fe)**:
Nombre d'échantillons par seconde (Hz ou SPS - Samples Per Second).

**ENOB (Effective Number Of Bits)**:
Résolution effective tenant compte du bruit:
```
ENOB = (SNR - 1.76) / 6.02
```

Souvent inférieur à la résolution nominale.

**INL/DNL**:
- **INL** (Integral Non-Linearity): écart max de la fonction de transfert à la droite idéale
- **DNL** (Differential Non-Linearity): variation de largeur des pas (codes)

#### 6. Architectures de Convertisseurs A/N

**Flash (parallèle)**:
- 2^N - 1 comparateurs
- Très rapide (ns)
- Consommation et surface élevées
- Limité à faible résolution (8 bits)

**Approximations Successives (SAR)**:
- Algorithme de recherche dichotomique
- Compromis vitesse/résolution
- 8-16 bits, quelques μs à quelques MHz
- Faible consommation
- Très répandu

**Pipeline**:
- Chaîne de plusieurs étages
- Chaque étage résout quelques bits
- Haute vitesse (>100 MSPS)
- 10-14 bits typique
- Latence de plusieurs cycles

**Sigma-Delta (ΔΣ)**:
- Sur-échantillonnage + noise shaping
- Très haute résolution (16-24 bits)
- Vitesse modérée (kHz à quelques MHz)
- Excellente linéarité
- Applications audio, instrumentation précise

**Double rampe (dual-slope)**:
- Intégration du signal puis décharge
- Très haute résolution
- Lent (10-100 SPS)
- Excellent rejet du bruit 50/60Hz
- Multimètres, balances

#### 7. Sources d'Erreur et Bruit

**Erreurs systématiques**:
- **Offset**: décalage de zéro
- **Gain**: erreur de pente
- **Linéarité**: distorsion de la courbe de transfert

Souvent calibrables (compensation logicielle/matérielle).

**Erreurs aléatoires (bruit)**:

**Bruit du capteur**:
- Bruit thermique de la résistance
- Bruit de grenaille (shot noise)
- Bruit en 1/f

**Bruit du conditionnement**:
- Bruit de l'amplificateur (en, in)
- Bruit thermique des résistances

**Bruit de quantification**:
```
σq = LSB / √12 = Vref / (2^N × √12)
Puissance: q² = (LSB)² / 12
```

**Bruit de l'ADC**:
- Jitter d'échantillonnage
- Bruit thermique interne

**Budget de bruit**:
```
Bruit total² = Σ (bruit de chaque source)²
SNR système = 20 log(Signal RMS / Bruit total RMS)
```

#### 8. Techniques d'Amélioration du SNR

**Moyennage**:
```
Réduction du bruit = √N
où N = nombre de moyennes
```

Efficace si bruit non corrélé.

**Filtrage numérique**:
- Réduire la bande passante au strict nécessaire
- Filtres FIR, IIR
- Moyennage mobile

**Sur-échantillonnage**:
```
Amélioration SNR = 10 log(OSR) / 2  (pour bruit blanc)
OSR = Over-Sampling Ratio = Fe_actual / Fe_Nyquist
```

**Modulation-Démodulation (Lock-in)**:
- Modulation du signal à mesurer à haute fréquence
- Démodulation synchrone après acquisition
- Excellente réjection du bruit 1/f et interférences
- Utilisé en instrumentation scientifique

**Corrélation**:
- Détection de signaux enfouis dans le bruit
- Amélioration proportionnelle à √(temps d'intégration)

#### 9. Interfaces Numériques

**Parallèle**:
- N fils pour N bits
- Rapide mais encombrant
- Utilisé sur courtes distances (interne PCB)

**Série**:

**SPI (Serial Peripheral Interface)**:
- 4 fils: CLK, MOSI, MISO, CS
- Full-duplex, rapide (plusieurs MHz)
- Maître-esclaves
- Utilisé pour ADC, DAC, mémoires, etc.

**I²C (Inter-Integrated Circuit)**:
- 2 fils: SDA, SCL
- Multi-maîtres, adressage
- Vitesses: 100 kHz (standard), 400 kHz (fast), 3.4 MHz (high-speed)
- Nombreux périphériques sur même bus

**UART/RS-232**:
- Communication série asynchrone
- 2 fils: TX, RX (+ masse)
- Vitesses standards (9600, 115200 baud, etc.)
- Longues distances avec niveaux RS-232

**USB**:
- Communication série haut débit
- Plug-and-play
- Alimentation possible
- USB 2.0 (480 Mbps), USB 3.0 (5 Gbps)

**Ethernet**:
- Pour acquisition distribuée
- Protocoles industriels (EtherCAT, Profinet, etc.)

#### 10. Synchronisation et Timing

**Échantillonnage synchrone**:
Multiple canaux échantillonnés simultanément.
Important si relation de phase entre signaux.

**Échantillonnage multiplexé**:
Plusieurs canaux partagent un ADC via multiplexeur analogique.
Skew temporel entre canaux (settling time du mux).

**Jitter d'échantillonnage**:
Incertitude sur instant d'échantillonnage.
Impact sur SNR, surtout pour signaux hautes fréquences:
```
SNR_jitter = -20 log(2π × f × σjitter)
```

**Horloge**:
- Stabilité cruciale pour performance
- Oscillateurs à quartz, TCXO, OCXO
- PLL pour synthèse de fréquences

#### 11. Mise en Œuvre Pratique

**Conception de PCB**:
- Séparation analogique/numérique (plans de masse)
- Blindage des sections sensibles
- Routage soigné (éviter couplages)
- Découplage alimentation (condensateurs près des composants)

**Alimentations**:
- Régulateurs faible bruit (LDO)
- Filtrage et découplage rigoureux
- Alimentations séparées analogique/numérique

**Blindage et masse**:
- Blindage électromagnétique si nécessaire
- Masse unique (star ground) ou séparation analogique/numérique selon cas
- Attention aux boucles de masse

**Logiciel d'acquisition**:
- Drivers pour ADC (SPI, I2C, etc.)
- Buffers circulaires pour acquisition continue
- DMA pour décharger processeur
- Calibration et compensation (offset, gain)
- Filtrage temps réel

#### 12. Applications Spécifiques

**Acquisition audio**:
- 16-24 bits, 44.1-192 kHz
- Codecs audio (ADC+DAC intégrés)
- Faible distorsion harmonique (THD)

**Instrumentation médicale (ECG, EEG)**:
- Très faible bruit (<10µVRMS)
- Protection patient (isolation galvanique)
- Filtres spécifiques (50/60Hz, passe-haut pour dérive baseline)
- Conformité normes médicales

**Acquisition industrielle**:
- Robustesse (température, vibration, EMI)
- Interfaces industrielles (4-20mA, 0-10V)
- Isolation galvanique
- Diagnostic et auto-test

**Acquisition scientifique haute précision**:
- Résolution 24 bits
- Calibration rigoureuse
- Compensation température
- Synchronisation précise (GPS, PTP)

**Acquisition haute vitesse**:
- Oscilloscopes numériques (GSPS)
- Pipelines, interleaving
- Mémoires rapides (FPGA, DDR)
- Traitement temps réel

## PART D: ANALYTICAL PART

### Knowledge and Skills Mobilized

- Compréhension globale d'une chaîne d'acquisition
- Sélection et interfaçage de capteurs
- Conception de circuits de conditionnement analogique
- Calcul et dimensionnement de filtres anti-repliement
- Choix de convertisseurs A/N selon cahier des charges
- Analyse de budget de bruit
- Calcul de SNR et résolution effective
- Conception de PCB pour signaux mixtes
- Programmation de drivers d'acquisition
- Validation expérimentale et caractérisation

### Self Evaluation

Ce cours a été très concret et directement applicable. Contrairement à des cours plus théoriques, ici chaque concept avait une traduction pratique immédiate. La vision système, de bout en bout, est particulièrement formatrice.

La sélection de capteurs est un exercice complexe: il faut équilibrer performance, coût, disponibilité, et contraintes d'intégration. Les datasheets deviennent des documents de travail essentiels.

Le conditionnement de signal est un art. Il faut amplifier suffisamment pour exploiter la plage de l'ADC, mais pas trop pour ne pas saturer. Le compromis bruit/bande passante est constant.

Le filtrage anti-repliement est crucial mais souvent sous-estimé. J'ai appris qu'un bon filtre analogique évite beaucoup de problèmes en aval. Le choix de l'ordre et de la fréquence de coupure demande réflexion.

Les convertisseurs A/N sont des composants fascinants. Comprendre les différentes architectures (SAR, Sigma-Delta, Pipeline) aide à choisir le bon pour chaque application. La résolution nominale est trompeuse; l'ENOB est plus réaliste.

Le budget de bruit est un exercice rigoureux mais indispensable. Identifier le maillon limitant permet d'optimiser les efforts (inutile d'avoir un ADC 24 bits si le capteur a 1% d'incertitude).

Les travaux pratiques m'ont confronté à la réalité: bruit 50Hz omniprésent, couplages parasites, dérives thermiques. La théorie donne le cadre, mais la pratique demande patience et méthodologie.

La conception de PCB pour signaux mixtes est délicate. J'ai appris l'importance du routage, des plans de masse, du découplage. Un PCB mal conçu peut ruiner les performances de composants excellents.

### My Opinion

Ce cours est essentiel pour tout ingénieur en électronique ou systèmes embarqués. L'acquisition de données est au cœur de la plupart des systèmes: capteurs IoT, drones, véhicules autonomes, instrumentation, etc.

Points forts:
- Approche système complète
- Équilibre théorie/pratique
- Travaux pratiques pertinents et formateurs
- Lien avec applications industrielles réelles
- Méthodologie de conception (specs → choix composants → validation)

Points à améliorer:
- Plus de temps sur conception PCB (layout)
- Approfondissement traitement numérique post-acquisition
- Aspects temps réel et systèmes embarqués
- Certification et normes (médical, automobile, aéronautique)

Réflexions personnelles:

L'acquisition de données semble simple en surface (convertir un signal analogique en numérique), mais les subtilités sont nombreuses. Atteindre les performances requises demande attention à chaque détail.

Le compromis coût/performance est omniprésent. Un ADC 24 bits coûte beaucoup plus cher qu'un 12 bits. Il faut évaluer si l'application justifie l'investissement ou si un moyennage logiciel sur un ADC moins cher suffit.

La tendance est à l'intégration: System-on-Chip avec ADC, processeur, interfaces intégrés. Mais comprendre chaque bloc séparément reste crucial pour optimiser le système global.

L'importance du bruit est souvent sous-estimée par les débutants. Dans les systèmes réels, le bruit est la limitation principale. Apprendre à le caractériser, le minimiser, et vivre avec est une compétence clé.

Applications futures:

Ces compétences sont directement applicables à:
- Objets connectés (IoT) et wearables
- Instrumentation médicale et scientifique
- Automobile (multiples capteurs)
- Domotique et bâtiments intelligents
- Industrie 4.0 (monitoring machines)
- Drones et robotique

Le domaine évolue rapidement avec:
- ADC plus rapides et précis
- Intégration accrue (SoC)
- Intelligence embarquée (edge computing)
- Réseaux de capteurs distribués

Maîtriser les fondamentaux de l'acquisition permet de s'adapter à ces évolutions tout en gardant une compréhension profonde des principes physiques sous-jacents.

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
      <h4>📖 Conditionneur de Signaux</h4>
      <p>Cours sur le conditionnement de signaux : amplification, filtrage, adaptation d'impédance et préparation pour conversion.</p>
      <embed src="/cours-pdf/S8/Chaines-Acquisition/conditionneur.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S8/Chaines-Acquisition/conditionneur.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>📖 Convertisseurs Analogique-Numérique</h4>
      <p>Cours sur les CAN : architectures (flash, SAR, sigma-delta), performances (résolution, vitesse, SNR) et choix.</p>
      <embed src="/cours-pdf/S8/Chaines-Acquisition/convertisseurs-can.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S8/Chaines-Acquisition/convertisseurs-can.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>📖 Capteurs Numériques</h4>
      <p>Mise en œuvre de capteurs numériques : protocoles I2C/SPI, configuration, calibration et exploitation des données.</p>
      <embed src="/cours-pdf/S8/Chaines-Acquisition/capteurs-numeriques.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S8/Chaines-Acquisition/capteurs-numeriques.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
  </div>
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

---
layout: default
title:  "Architectures Analogiques Systèmes Embarqués - S7"
date:   2024-10-02 09:02:00 +0200
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

# 🔌 Architectures Analogiques Systèmes Embarqués - Semestre 7

**Année Universitaire** : 2023-2024  
**Semestre** : 7  
**Crédits** : 2.5 ECTS  
**Spécialité** : Électronique Analogique et Systèmes Embarqués

---

## PART A - Présentation Générale du Module

<h3 class="section-title">Vue d'ensemble</h3>

Ce cours traite des architectures analogiques spécifiques aux systèmes embarqués : amplificateurs commandés en tension, filtres à fréquence de coupure variable, modulateurs, et circuits de conditionnement de signaux. L'accent est mis sur les circuits programmables et adaptatifs essentiels pour les systèmes intelligents et reconfigurables.

**Objectifs pédagogiques** :
- Concevoir des amplificateurs à gain commandé en tension (VCA)
- Maîtriser les filtres actifs commandés en tension
- Comprendre les modulateurs et leurs applications
- Simuler et dimensionner des circuits analogiques complexes
- Réaliser des PCB pour circuits analogiques
- Utiliser des composants spécialisés (transconductance amplifiers)

<h3 class="section-title">Position dans le cursus</h3>

Ce module s'appuie sur :
- **Électronique Fonctions Analogiques (S6)** : AOPs, filtres actifs
- **Projet PCB (S6)** : conception de cartes électroniques
- **Circuits et Filtres analogiques (S5)** : filtres, fonction de transfert

Il prépare à :
- **Systèmes embarqués** : conditionnement de signaux, interfaces analogiques
- **Instrumentation** : circuits à gain programmable
- **Audio professionnel** : mixeurs, égaliseurs, effets
- **Télécommunications** : contrôle automatique de gain (AGC)

---

## PART B - Expérience Personnelle et Contexte d'Apprentissage

<h3 class="section-title">Organisation et ressources</h3>

Le module était organisé en travaux dirigés et bureau d'études pratique :

**Travaux dirigés (12h)** :
- TD1 : Amplificateur à gain commandé en tension
- TD2 : Filtre passe-bas ordre 1 à fréquence de coupure commandée en tension

**Bureau d'études (16h)** :
Projet complet de conception d'un modulateur :
- Partie 1 : Amplificateur à gain commandé en tension
- Partie 2 : Filtre ordre 1 commandé en tension
- Projet final : Modulateur complet avec PCB sur Altium Designer

**Supports pédagogiques** :
- Énoncés de TD en PDF
- Documentation composant LM13700 (transconductance amplifier)
- Simulations TINA-TI (logiciel de simulation analogique Texas Instruments)
- Projet Altium Designer pour réalisation PCB

<h3 class="section-title">Contenu du projet</h3>

**Projet modulateur** :

Le projet consistait à concevoir un modulateur complet intégrant :
- Amplificateur à gain variable
- Filtre passe-bas à fréquence de coupure variable
- Circuit de modulation
- Design PCB complet avec Altium Designer

**Librairies créées** :
- 4AE_LM.SCHLIB : symboles schématiques
- LIB_V2.SCHLIB : bibliothèque de composants version 2
- ACT.PcbLib : empreintes PCB
- PRINT_V2.PcbLib : empreintes d'impression version 2

**Simulations TINA** :
- AOP_non_inverseur.TSC : amplificateur non inverseur de base
- Passe_bas.TSC : filtre passe-bas simple
- Filtre_Com_Tension.TSC : filtre commandé en tension
- Modulateur.TSC : circuit modulateur complet

<h3 class="section-title">Méthode de travail</h3>

**Phase 1 : Étude théorique** :
Analyse des circuits dans les TD, calculs de fonctions de transfert, dimensionnement des composants.

**Phase 2 : Simulations** :
Validation des circuits sous TINA-TI avant réalisation. Ajustement des paramètres pour obtenir les performances souhaitées.

**Phase 3 : Conception PCB** :
Création des schémas sous Altium Designer, routage du PCB, vérifications DRC/ERC, génération des fichiers de fabrication.

<h3 class="section-title">Difficultés rencontrées</h3>

**Composant LM13700** :
L'amplificateur de transconductance LM13700 est un composant spécialisé. Comprendre son fonctionnement et dimensionner les résistances externes demande une bonne compréhension de la transconductance.

**Stabilité des circuits** :
Les circuits commandés en tension peuvent présenter des instabilités si mal dimensionnés. Importance de la compensation et des condensateurs de stabilisation.

**Routage PCB** :
Pour des circuits analogiques précis, le routage est critique (découplage, pistes courtes, plan de masse).

---

## PART C - Aspects Techniques Détaillés

<h3 class="section-title">1. Amplificateurs de transconductance</h3>

**Définition** :

Un amplificateur de transconductance convertit une tension d'entrée en un courant de sortie proportionnel.

I_sortie = gm × V_entrée

où gm est la transconductance (en Siemens ou mho).

**LM13700 - Operational Transconductance Amplifier (OTA)** :

Circuit intégré contenant deux OTA indépendants.

**Principe** :
- La transconductance gm est commandée par un courant de polarisation I_abc (amplifier bias current)
- gm = 19,2 × I_abc (approximation)
- Permet de commander le gain en ajustant I_abc

**Avantages** :
- Gain programmable électroniquement
- Large plage de variation
- Linéarité acceptable

**Applications** :
- VCA (Voltage Controlled Amplifier)
- VCF (Voltage Controlled Filter)
- Modulateurs
- AGC (Automatic Gain Control)

<h3 class="section-title">2. Amplificateur à gain commandé en tension (VCA)</h3>

**Principe** :

Un VCA est un amplificateur dont le gain est contrôlé par une tension externe.

V_sortie = A(V_controle) × V_entrée

**Réalisation avec LM13700** :

**Circuit de base** :
- OTA du LM13700
- Résistance de charge en sortie
- Tension de commande convertie en courant I_abc via une résistance

**Calcul du gain** :

Gain = gm × R_charge = (19,2 × I_abc) × R_charge

Pour commander le gain par une tension V_ctrl :
I_abc = V_ctrl / R_ctrl

Donc : Gain = (19,2 × V_ctrl × R_charge) / R_ctrl

**Plage de gain** :

Typiquement de -40 dB à +40 dB en variant V_ctrl.

**Linéarisation** :

Pour améliorer la linéarité, on peut utiliser :
- Diodes de linéarisation (incluses dans le LM13700)
- Résistances d'émetteur
- Contre-réaction

**Applications** :

| Application | Description |
|-------------|-------------|
| Mixeur audio | Contrôle du niveau de chaque canal |
| AGC | Ajustement automatique du gain |
| Compresseur/limiteur | Traitement dynamique audio |
| Modulateur d'amplitude | Multiplication de signaux |

<h3 class="section-title">3. Filtres commandés en tension</h3>

**Filtre passe-bas du premier ordre commandé** :

**Principe** :
Utiliser un OTA pour créer une résistance équivalente variable.

**Fonction de transfert** :

H(jω) = 1 / (1 + jω / ωc)

avec ωc = 2π fc (pulsation de coupure)

**Fréquence de coupure commandée** :

En utilisant un OTA, on peut faire varier fc proportionnellement à la tension de commande.

fc = gm / (2π C) = (19,2 × I_abc) / (2π C)

Si I_abc = V_ctrl / R_ctrl :

fc = (19,2 × V_ctrl) / (2π C × R_ctrl)

**Plage de fréquence** :

Typiquement de quelques Hz à plusieurs dizaines de kHz selon V_ctrl.

**Filtre passe-bas ordre 2 (Sallen-Key commandé)** :

En cascadant deux cellules du premier ordre ou en utilisant une structure Sallen-Key avec OTA.

Meilleure sélectivité (-40 dB/décade).

**Applications** :

| Application | Description |
|-------------|-------------|
| Égaliseur paramétrique | Ajustement de la fréquence de coupure |
| Filtre anti-aliasing adaptatif | Ajusté selon fréquence d'échantillonnage |
| Synthétiseur audio | Filtre VCF pour synthèse soustractive |
| Traitement adaptatif | Filtrage en fonction du contenu du signal |

<h3 class="section-title">4. Modulateurs</h3>

**Définition** :

Circuit qui réalise la multiplication de deux signaux.

**Modulation d'amplitude** :

s(t) = [A + m(t)] × cos(ωp t)

où m(t) est le signal modulant, cos(ωp t) la porteuse.

**Réalisation avec OTA** :

L'OTA peut servir de multiplieur car :
I_sortie = gm × V_entrée

Si gm est proportionnel à un signal (via I_abc), on obtient une multiplication.

**Circuit modulateur** :

**Entrées** :
- Signal porteur : appliqué à l'entrée de l'OTA
- Signal modulant : commande la transconductance gm (via I_abc)

**Sortie** :
Signal modulé en amplitude.

**Modulateur en anneau (ring modulator)** :

Utilise 4 OTA ou diodes en pont pour réaliser une multiplication exacte.

Sortie : s(t) = m1(t) × m2(t)

**Applications** :
- Modulation AM
- Mélangeur de fréquences (hétérodynage)
- Effets audio (tremolo, chorus)
- Démodulation synchrone

<h3 class="section-title">5. Circuits de conditionnement</h3>

**Conditionnement de capteurs** :

Les signaux issus de capteurs nécessitent souvent un traitement avant numérisation.

**Étapes typiques** :

1. **Amplification** : VCA pour adapter le niveau
2. **Filtrage** : Éliminer le bruit et les fréquences indésirables
3. **Offset** : Ajuster le niveau DC
4. **Protection** : Écrêtage, limitation

**Amplificateur d'instrumentation** :

Circuit spécialisé pour amplifier les signaux différentiels de faible amplitude.

**Caractéristiques** :
- Très haute impédance d'entrée
- Gain précis et stable
- CMRR élevé (> 100 dB)
- Faible bruit

**Applications** :
- Jauges de contrainte
- Thermocouples
- Ponts de Wheatstone
- Mesures biomédicales (ECG, EMG)

**Filtre anti-aliasing** :

Filtre passe-bas placé avant un ADC pour éviter le repliement spectral (aliasing).

**Règle** :
fc < fs / 2 (fréquence d'échantillonnage / 2)

Typiquement : fc = 0,4 × fs

<h3 class="section-title">6. Contrôle automatique de gain (AGC)</h3>

**Principe** :

Circuit qui ajuste automatiquement le gain pour maintenir un niveau de sortie constant malgré les variations de l'entrée.

**Boucle de régulation** :

1. **Détecteur d'amplitude** : Mesure le niveau de sortie (détecteur de crête ou RMS)
2. **Comparateur** : Compare au niveau de référence
3. **Intégrateur** : Filtre la tension d'erreur (temps de réponse)
4. **VCA** : Ajuste le gain selon la tension de commande

**Paramètres** :

- **Temps d'attaque** : Rapidité de réduction du gain (signal fort)
- **Temps de relâchement** : Rapidité d'augmentation du gain (signal faible)
- **Seuil** : Niveau à partir duquel l'AGC agit

**Applications** :

| Application | Description |
|-------------|-------------|
| Récepteurs radio | Maintenir le volume constant |
| Téléphonie | Normalisation du niveau vocal |
| Enregistrement audio | Éviter la saturation |
| Instrumentation | Adapter la dynamique du signal |

<h3 class="section-title">7. Techniques de simulation</h3>

**TINA-TI** :

Logiciel de simulation analogique gratuit de Texas Instruments.

**Fonctionnalités** :
- Simulation temporelle (transitoire)
- Analyse fréquentielle (AC)
- Analyse de bruit
- Analyse de distorsion harmonique
- Analyse de sensibilité

**Méthodologie** :

1. **Schéma** : Dessiner le circuit
2. **Modèles** : Utiliser les modèles SPICE des composants
3. **Simulation** : Choisir le type d'analyse
4. **Visualisation** : Courbes de réponse
5. **Optimisation** : Ajuster les valeurs

**Exemple : amplificateur à gain variable**

Simulation :
- Analyse AC : réponse en fréquence pour différentes tensions de commande
- Analyse transitoire : réponse à un signal sinusoïdal
- Mesure du gain en dB
- Vérification de la linéarité

<h3 class="section-title">8. Conception PCB pour circuits analogiques</h3>

**Règles de conception** :

**Layout critique** :

| Aspect | Recommandation |
|--------|----------------|
| Plan de masse | Cuivre plein pour GND |
| Découplage | Condensateur 100 nF proche de chaque alimentation |
| Pistes courtes | Minimiser les inductances parasites |
| Séparation analogique/numérique | Plans de masse séparés si mixte |
| Symétrie | Circuits différentiels symétriques |

**Alimentation** :

- Découplage local : 100 nF céramique + 10 µF électrolytique par CI
- Pistes d'alimentation larges
- Filtrage de l'alimentation (ferrite, LC)

**Signaux sensibles** :

- Pistes d'entrée courtes et protégées
- Éviter les boucles de masse
- Garde (guard ring) autour des circuits critiques

**Composants** :

- Résistances : précision 1% ou mieux pour gain stable
- Condensateurs : COG/NP0 pour circuits de précision
- AOPs : choisir selon bande passante, bruit, offset

<h3 class="section-title">9. Altium Designer pour le projet</h3>

**Projet BE_Archi_Sys_Emb** :

Structure du projet :
- Fichier projet : BE_Archi_Sys_Emb.PrjPcb
- Schéma : Modulateur.SchDoc
- Bibliothèques : 4AE_LM.SCHLIB, LIB_V2.SCHLIB
- Empreintes : ACT.PcbLib, PRINT_V2.PcbLib

**Étapes de conception** :

1. **Création des bibliothèques** :
   - Symboles schématiques (LM13700, résistances, condensateurs)
   - Empreintes PCB (DIP8, CMS 0805)

2. **Schéma électrique** :
   - Placement des composants
   - Connexions (nets)
   - Annotations (valeurs, références)
   - Vérifications ERC

3. **PCB** :
   - Import du schéma
   - Placement des composants
   - Routage manuel ou automatique
   - Vérifications DRC
   - Plans de masse et alimentation

4. **Génération fichiers** :
   - Gerber (fabrication)
   - BOM (liste composants)
   - Fichiers d'assemblage

<h3 class="section-title">10. Applications pratiques</h3>

**Table de mixage audio** :

Chaque canal dispose d'un VCA pour contrôler le volume. Les faders ajustent la tension de commande.

**Synthétiseur analogique** :

- VCO (Voltage Controlled Oscillator) : fréquence variable
- VCF (Voltage Controlled Filter) : filtre à fc variable
- VCA : enveloppe d'amplitude (ADSR)

**Compresseur audio** :

Circuit AGC avec détecteur RMS et paramètres d'attaque/relâchement réglables.

Réduit la dynamique du signal (plage entre le plus faible et le plus fort).

**Égaliseur paramétrique** :

Plusieurs filtres passe-bande avec fréquence centrale, gain et facteur Q commandés.

**Récepteur radio adaptatif** :

AGC pour maintenir le niveau constant malgré la variation du signal RF reçu.
Filtres FI à bande passante variable selon les conditions de réception.

---

## PART D - Analyse Réflexive et Perspectives

<h3 class="section-title">Compétences acquises</h3>

**Conception de circuits commandés** :
Maîtrise des amplificateurs et filtres à paramètres variables électroniquement. Capacité à utiliser les OTA pour créer des circuits reconfigurables.

**Simulation analogique** :
Utilisation efficace de TINA-TI pour valider les circuits avant réalisation. Compréhension des analyses AC, transitoires, et de bruit.

**Conception PCB professionnelle** :
Réalisation complète d'un PCB sous Altium Designer : création de bibliothèques, schéma, routage, vérifications.

<h3 class="section-title">Points clés à retenir</h3>

**1. OTA = composant polyvalent** :
L'amplificateur de transconductance (LM13700) permet de créer des VCA, VCF, modulateurs simplement en exploitant la commande de gm.

**2. Linéarité vs plage dynamique** :
Les circuits commandés présentent souvent un compromis entre linéarité et plage de variation. Importance de la linéarisation.

**3. Stabilité essentielle** :
Les circuits à gain variable peuvent osciller si mal compensés. Condensateurs de stabilisation critiques.

**4. Layout = performance** :
Pour les circuits analogiques précis, le layout PCB est aussi important que le schéma. Plan de masse, découplage, symétrie.

**5. Simulation = gain de temps** :
Simuler avant réaliser évite les erreurs coûteuses (PCB à refaire, composants grillés).

<h3 class="section-title">Applications pratiques</h3>

**Audio professionnel** :
Mixeurs, compresseurs, égaliseurs, effets utilisent massivement les VCA et VCF.

**Instrumentation** :
Amplificateurs à gain programmable pour s'adapter automatiquement à la plage du signal mesuré.

**Télécommunications** :
AGC dans tous les récepteurs radio (AM, FM, GSM, WiFi, etc.).

**Systèmes embarqués** :
Conditionnement adaptatif de signaux capteurs selon les conditions.

<h3 class="section-title">Retour d'expérience</h3>

**Projet complet et formateur** :
Le BE permet de passer par toutes les étapes d'un projet réel : spécifications, conception, simulation, PCB, vérifications.

**LM13700 intéressant** :
Composant vintage mais toujours pertinent pédagogiquement. Les OTA modernes (OPA860, etc.) utilisent les mêmes principes.

**Simulations TINA utiles** :
Les simulations permettent de visualiser immédiatement l'effet des changements de paramètres (résistances, condensateurs).

**Altium Designer professionnel** :
Outil utilisé en industrie. Compétence valorisable en entreprise.

<h3 class="section-title">Limites et ouvertures</h3>

**Limites du module** :
- Pas de réalisation physique et test du PCB
- Composants analogiques classiques (alternatives numériques non abordées)
- Aspects bruit et distorsion peu approfondis

**Ouvertures vers** :
- **DSP (Digital Signal Processing)** : alternative numérique aux circuits analogiques
- **Systèmes mixtes** : ADC, DAC, conversion analogique-numérique
- **Audio numérique** : codecs, effets numériques
- **Contrôle numérique de circuits analogiques** : potentiomètres numériques, DAC pour commande
- **SoC mixtes** : intégration analogique-numérique sur puce

<h3 class="section-title">Évolution technologique</h3>

**Tendances actuelles** :

**Circuits programmables** :
- FPAA (Field Programmable Analog Array) : équivalent analogique des FPGA
- Potentiomètres numériques commandés par SPI/I2C
- VGA (Variable Gain Amplifier) intégrés avec contrôle numérique

**Intégration** :
- AFE (Analog Front-End) intégrant conditionnement complet
- Codec audio intégrés (ADC + DAC + VCA + filtres)
- SoC avec partie analogique reconfigurable

**Performance** :
- Très faible bruit (< 1 nV/sqrt(Hz))
- Très faible consommation (nA de quiescent current)
- Large dynamique (> 120 dB)

<h3 class="section-title">Conseils pour réussir</h3>

**1. Comprendre le LM13700** :
Bien assimiler le principe de la transconductance commandée. Lire attentivement la datasheet.

**2. Simuler systématiquement** :
Chaque modification doit être validée par simulation avant d'aller plus loin.

**3. Dimensionner avec soin** :
Les valeurs de résistances et condensateurs déterminent les performances. Utiliser les formules données.

**4. Vérifier le PCB** :
DRC/ERC sont impératifs. Une erreur sur le PCB coûte cher (refabrication).

**5. Documenter** :
Bien annoter les schémas, calculer et noter les valeurs théoriques pour comparer avec les simulations.

<h3 class="section-title">Conclusion</h3>

Ce module fournit une excellente introduction aux circuits analogiques reconfigurables et commandés. La maîtrise des VCA, VCF et modulateurs est essentielle pour de nombreuses applications (audio, instrumentation, télécommunications).

**Approche projet** :
Le bureau d'études avec conception complète (simulation + PCB) reflète bien le travail d'un ingénieur électronique. Toutes les étapes d'un projet réel sont couvertes.

**Compétences transférables** :
- Conception de circuits analogiques complexes
- Simulation avec outils professionnels (TINA, SPICE)
- Conception PCB avec Altium Designer
- Gestion de projet électronique complet

**Message principal** :
Les circuits commandés en tension apportent de la flexibilité et de l'adaptabilité aux systèmes analogiques. Ils permettent de créer des systèmes intelligents capables de s'adapter automatiquement aux conditions (AGC, filtrage adaptatif).

**Recommandations** :
- Expérimenter avec des kits d'évaluation (Texas Instruments, Analog Devices)
- Réaliser et tester physiquement le PCB conçu
- Explorer les alternatives numériques (DSP) pour comparaison
- Approfondir les aspects bruit, distorsion, linéarité

**Liens avec les autres cours** :
- [Électronique Fonctions Analogiques - S6](./electronique-fonctions-analogiques.html) : AOPs, filtres actifs
- [Projet PCB - S6](./projet-pcb.html) : conception de cartes
- [Architectures Analogiques Transmission - S7](./architectures-analogiques-transmission.html) : modulation, RF

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
      <h4>📖 Sujet Bureau d'Études</h4>
      <p>Sujet complet du BE : conception d'un modulateur et filtre commandés en tension avec TINA et Altium Designer.</p>
      <embed src="/cours-pdf/S7/Archi-Analogiques-Embarques/sujet-be.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Archi-Analogiques-Embarques/sujet-be.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>📖 TD1 - Gain Commandé en Tension</h4>
      <p>TD sur la conception d'amplificateurs à gain variable commandé en tension (VCA) avec OTA et circuits intégrés.</p>
      <embed src="/cours-pdf/S7/Archi-Analogiques-Embarques/td1-gain-commande.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Archi-Analogiques-Embarques/td1-gain-commande.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
  </div>
</div>

---

*Cours suivi en 2023-2024 à l'INSA Toulouse, Département Génie Électrique et Informatique.*

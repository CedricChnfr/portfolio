---
layout: default
title: "Télécommunications Numériques - Modulation - S4"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

# Télécommunications Numériques - Modulation - Semestre 4

---

## PART A - Présentation Générale du Cours

### Contexte et objectifs

Approfondissement modulations numériques (suite Télécom S3) : PSK, QAM, OFDM. Codage canal avancé, égalisation, performances. Applications 4G/5G, WiFi, satellite.

**Objectifs :**
- Modulations avancées (QPSK, 16/64-QAM, OFDM)
- Analyse constellation, diagramme œil
- Codage canal (convolutif, turbo, LDPC)
- Égalisation (annulation ISI)
- Performances BER vs SNR

### Prérequis
- Télécom S3 (modulations base, codage)
- OL S3 (MATLAB, FFT)
- Signal (filtrage)

---

## PART B: EXPÉRIENCE, CONTEXTE ET FONCTION

### Module 1 : Modulations numériques avancées

**QPSK (Quadrature PSK) :**
- 4 symboles (2 bits/symbole)
- Constellation : 0°, 90°, 180°, 270°
- Efficacité : 2 bits/s/Hz
- Applications : satellite, 3G

**16-QAM, 64-QAM, 256-QAM :**
- 16-QAM : 4 bits/symbole, 16 points constellation
- 64-QAM : 6 bits/symbole (WiFi, 4G)
- 256-QAM : 8 bits/symbole (5G, câble)
- Trade-off : efficacité vs robustesse bruit

**OFDM (Orthogonal Frequency Division Multiplexing) :**
- Multi-porteuses orthogonales
- Résistance multi-trajets
- IFFT/FFT pour modulation/démodulation
- Préfixe cyclique (guard interval)
- Applications : WiFi, 4G/5G, DVB-T

**Diagramme constellation :**
Points I/Q idéaux + impact bruit (nuage)

### Module 2 : Canal de transmission

**Interférence inter-symboles (ISI) :**
- Dispersion temporelle (multi-trajets)
- Élargissement symboles → chevauchement

**Diagramme de l'œil :**
- Superposition symboles temporels
- Ouverture œil ∝ qualité signal
- Fermé = ISI importante

**Égalisation :**
- **Égaliseur linéaire** : filtre inverse canal
- **Égaliseur adaptatif** : LMS, RLS (poursuite canal variant)
- **Égaliseur DFE** (Decision Feedback) : meilleure performance

### Module 3 : Codage de canal avancé

**Codes convolutifs :**
- Encodeur : registres à décalage + XOR
- Taux 1/2, 1/3 (redondance)
- Décodeur Viterbi : chemin max vraisemblance
- Applications : GSM, satellite

**Turbo codes :**
- 2 encodeurs convolutifs parallèles + entrelaceur
- Décodage itératif (SISO)
- Proches limite Shannon
- 3G, 4G

**LDPC (Low-Density Parity-Check) :**
- Matrice parité creuse
- Décodage itératif (belief propagation)
- 5G, DVB-S2, WiFi 6

**Performances :**
Gain codage : 3-8 dB (selon code et BER cible)

### Module 4 : Performances systèmes

**BER (Bit Error Rate) :**
- BPSK : $BER \approx \frac{1}{2} erfc(\sqrt{E_b/N_0})$
- QAM : dépend ordre (M-QAM)
- Courbes BER vs Eb/N0 (dB)

**Efficacité spectrale :**
- bits/s/Hz
- Trade-off avec robustesse

**Capacité de Shannon :**
$$C = B \log_2(1 + SNR)$$
Limite théorique

---

## PART C: ASPECTS TECHNIQUES

### TP MATLAB

**TP1 : Modulations QPSK, 16-QAM**
- Génération constellation
- Modulation/démodulation
- Canal AWGN
- BER vs SNR

**TP2 : OFDM**
- Création symboles OFDM (IFFT)
- Préfixe cyclique
- Canal multi-trajets
- Démodulation (FFT)

**TP3 : Codage convolutif**
- Encodage taux 1/2
- Décodage Viterbi
- Courbes BER avec/sans codage
- Gain de codage

**TP4 : Égalisation**
- Canal dispersif
- Diagramme œil sans/avec égalisation
- Égaliseur ZF (Zero-Forcing)
- Amélioration BER

### Projet Chaîne de transmission complète

**Architecture :**
```
[Bits] → [Turbo Encoder] → [16-QAM] → [Canal multi-trajets + AWGN]
          ↓
[Bits] ← [Turbo Decoder] ← [Égalisation] ← [Démod 16-QAM]
```

**Paramètres :**
- Modulation : 16-QAM
- Code : Turbo taux 1/2
- Canal : Rayleigh fading + AWGN
- Débit : 10 Mbps
- Bande : 5 MHz

**Résultats :**
- Courbes BER (non-codé, turbo, avec égalisation)
- Constellation avant/après égalisation
- Efficacité spectrale

---

## PART D: ANALYSE ET RÉFLEXION

### Évaluation
- TP MATLAB (40%)
- Projet chaîne transmission (35%)
- Contrôles (15%)
- Examen (10%)

### Compétences acquises
- Modulations numériques avancées (PSK, QAM, OFDM)
- Codage canal professionnel (turbo, LDPC)
- Égalisation et compensation canal
- Simulation systèmes complets MATLAB
- Analyse performances (BER, efficacité spectrale)

### Applications professionnelles
- Conception modems (4G/5G, WiFi)
- Systèmes satellite
- Communications sous-marines
- Ingénieur télécommunications

## 📚 Contenu du cours

### Signaux et constellation

#### Représentation des signaux

**Espace des signaux :**
- Base orthonormée
- Projection sur axes I et Q
- Énergie et puissance
- Distance euclidienne

**Constellation :**
- Représentation graphique
- Points du diagramme
- Décision au récepteur
- Régions de décision

#### Signal en bande de base vs modulé

**Bande de base :**
- Signal numérique brut
- Codage en ligne (NRZ, Manchester, etc.)
- Spectre centré autour de 0

**Modulation :**
- Translation en fréquence
- Porteuse fc
- Bande passante du canal
- Applications sans fil

### Modulations linéaires

#### ASK (Amplitude Shift Keying)

**Principe :**
- Modulation d'amplitude
- M niveaux d'amplitude
- OOK (On-Off Keying) : 2-ASK

**Signal :**
$$s(t) = A_i \cos(2\pi f_c t)$$

**Avantages :**
- Simple à implémenter
- Faible complexité

**Inconvénients :**
- Sensible au bruit
- Efficacité énergétique faible
- Rarement utilisé seul

#### PSK (Phase Shift Keying)

**BPSK (Binary PSK) :**
- 2 phases : 0° et 180°
- 1 bit par symbole
- Robuste au bruit
- Applications : GPS, RFID

**Signal :**
- Symbol 0 : $s_0(t) = A\cos(2\pi f_c t)$
- Symbol 1 : $s_1(t) = A\cos(2\pi f_c t + \pi) = -A\cos(2\pi f_c t)$

**QPSK (Quadrature PSK) :**
- 4 phases : 0°, 90°, 180°, 270°
- 2 bits par symbole
- Efficacité spectrale doublée
- Applications : satellite, DVB, LTE

**Constellation QPSK :**
```
     Q
     |
  01 | 00
-----|-----I
  11 | 10
     |
```

**8-PSK :**
- 8 phases (45° d'écart)
- 3 bits par symbole
- Plus sensible au bruit
- Applications : DVB-S2

**Signal PSK général :**
$$s_i(t) = A\cos\left(2\pi f_c t + \frac{2\pi i}{M}\right)$$
avec $i = 0, 1, ..., M-1$

#### QAM (Quadrature Amplitude Modulation)

**Principe :**
- Modulation d'amplitude et de phase
- Deux porteuses en quadrature (I et Q)
- Combinaison optimale

**Signal :**
$$s(t) = I(t)\cos(2\pi f_c t) - Q(t)\sin(2\pi f_c t)$$

**Constellations courantes :**

**16-QAM :**
- 16 symboles
- 4 bits par symbole
- Grille 4×4
- Applications : WiFi, LTE

**64-QAM :**
- 64 symboles
- 6 bits par symbole
- Grille 8×8
- Applications : câble, WiFi 5

**256-QAM :**
- 256 symboles
- 8 bits par symbole
- Nécessite excellent SNR
- Applications : WiFi 6, câble

**Avantages QAM :**
- Haute efficacité spectrale
- Flexible (4-QAM à 4096-QAM)
- Utilisée dans la plupart des standards modernes

**Inconvénients :**
- Amplification linéaire nécessaire
- Sensible au bruit (niveaux élevés)
- Synchronisation critique

### Modulations non linéaires

#### FSK (Frequency Shift Keying)

**Principe :**
- Modulation de fréquence
- M fréquences distinctes
- Enveloppe constante

**BFSK (Binary FSK) :**
- 2 fréquences : f1 et f2
- 1 bit par symbole
- Simple et robuste

**Signal :**
- Symbol 0 : $s_0(t) = A\cos(2\pi f_1 t)$
- Symbol 1 : $s_1(t) = A\cos(2\pi f_2 t)$

**MSK (Minimum Shift Keying) :**
- Forme continue de FSK
- Phase continue
- Spectre compact
- Applications : GSM

**GFSK (Gaussian FSK) :**
- MSK avec filtre gaussien
- Spectre encore plus compact
- Applications : Bluetooth

**Avantages FSK :**
- Enveloppe constante (ampli non linéaire OK)
- Robuste au bruit
- Détection non cohérente possible

**Inconvénients :**
- Efficacité spectrale limitée
- Bande passante plus large

### Mise en forme d'impulsion

#### Filtrage adapté

**Objectif :**
- Maximiser SNR au point de décision
- Filtre optimal : adapté au signal

**Critère de Nyquist :**
- Pas d'interférence entre symboles (ISI)
- Impulsion sinc idéale (irréalisable)

#### Filtre en cosinus surélevé (Raised Cosine)

**Fonction de transfert :**
Compromis entre bande passante et ISI

**Roll-off factor α :**
- α = 0 : sinc idéal (irréalisable)
- α = 1 : bande passante doublée
- α = 0.5 : compromis courant

**Bande passante :**
$$B = \frac{R_s}{2}(1 + \alpha)$$

avec Rs = débit symbole

**Root Raised Cosine (RRC) :**
- Racine carrée du RC
- Émetteur et récepteur utilisent RRC
- Cascade = RC parfait

### Performances et BER

#### Probabilité d'erreur binaire (BER)

**Définition :**
$$BER = \frac{\text{Nombre de bits erronés}}{\text{Nombre total de bits}}$$

**Dépend de :**
- Rapport signal/bruit (SNR ou Eb/N0)
- Type de modulation
- Codage de canal
- Canal de transmission

#### Rapport Eb/N0

**Eb :** Énergie par bit
**N0 :** Densité spectrale de puissance du bruit

$$\frac{E_b}{N_0} = \frac{SNR \cdot B}{R_b}$$

- SNR : rapport signal/bruit
- B : bande passante
- Rb : débit binaire

#### BER théorique

**BPSK :**
$$BER = Q\left(\sqrt{\frac{2E_b}{N_0}}\right)$$

**QPSK :**
$$BER = Q\left(\sqrt{\frac{2E_b}{N_0}}\right)$$
(même que BPSK pour même Eb/N0)

**M-QAM :**
Formules plus complexes, dépend de M

**Courbes BER vs Eb/N0 :**
- Graphique log(BER) vs Eb/N0 (dB)
- Objectif typique : BER < 10^-6
- Modulations d'ordre élevé nécessitent plus de SNR

### Codage de canal

#### Objectifs
- Détecter et corriger erreurs
- Améliorer BER
- Gain de codage (coding gain)
- Augmente débit apparent

#### Codes en bloc

**Code de Hamming :**
- (n, k) : n bits transmis, k bits données
- Distance de Hamming
- Correction d'erreurs simples

**Code de Reed-Solomon :**
- Correction de rafales d'erreurs
- Symboles non binaires
- Applications : CD, DVD, QR codes, satellite

#### Codes convolutifs

**Principe :**
- Encodage continu
- Registre à décalage
- Rendement r = k/n

**Décodage Viterbi :**
- Décodage à maximum de vraisemblance
- Algorithme optimal
- Complexité exponentielle en nombre d'états

**Applications :**
- Téléphonie mobile (2G, 3G)
- Satellite
- Deep space communication

#### Turbo codes

**Principe :**
- Codes convolutifs entrelacés
- Décodage itératif
- Performance proche de Shannon

**Applications :**
- 3G, 4G LTE
- Satellite

#### LDPC (Low Density Parity Check)

**Principe :**
- Matrice de parité creuse
- Décodage itératif
- Performance excellente

**Applications :**
- WiFi (802.11n/ac/ax)
- 5G
- DVB-S2

### Techniques avancées

#### OFDM (Orthogonal Frequency Division Multiplexing)

**Principe :**
- Multiplexage fréquentiel
- Sous-porteuses orthogonales
- Robustesse aux multi-trajets
- FFT/IFFT pour implémentation

**Applications :**
- WiFi (802.11a/g/n/ac/ax)
- 4G LTE, 5G
- DVB-T (TNT)
- ADSL

#### MIMO (Multiple Input Multiple Output)

**Principe :**
- Antennes multiples émission/réception
- Multiplexage spatial
- Diversité
- Gain de capacité

**Applications :**
- WiFi, 4G, 5G
- Augmente débit

#### Étalement de spectre (Spread Spectrum)

**DSSS (Direct Sequence) :**
- Code PN (Pseudo Noise)
- Bande étalée
- Robustesse aux interférences

**FHSS (Frequency Hopping) :**
- Saut de fréquence
- Résistance au brouillage

**Applications :**
- GPS (DSSS)
- Bluetooth (FHSS)
- WiFi (DSSS historique)

## 🛠️ Travaux pratiques

### TP Génération de modulations

**Objectifs :**
- Générer signaux BPSK, QPSK, QAM
- Tracer constellations
- Analyser spectres

**Outils :**
- MATLAB/Python
- Générateur IQ

### TP Démodulation et BER

**Simulation chaîne complète :**
1. Source binaire aléatoire
2. Mapping (bits → symboles)
3. Mise en forme (RRC)
4. Modulation (up-conversion)
5. Canal (AWGN)
6. Démodulation (down-conversion)
7. Filtrage adapté
8. Décision
9. Demapping
10. Calcul BER

**Analyses :**
- Courbes BER vs Eb/N0
- Diagrammes de constellation bruités
- Diagramme de l'œil

### TP Codage de canal

- Implémentation code de Hamming
- Codage convolutif + Viterbi
- Mesure du gain de codage
- Comparaison avec théorie

### Projet communication numérique

**Exemple :** Liaison audio numérique
- Numérisation audio
- Compression (optionnelle)
- Codage de canal
- Modulation QPSK ou QAM
- Transmission RF ou filaire
- Démodulation et décodage
- Reconstruction audio

## 💻 Outils utilisés

### Simulation
- **MATLAB** : Communications Toolbox
- **GNU Radio** : SDR et communication
- **Python** : NumPy, SciPy, CommPy
- **Simulink** : Simulation graphique

### Matériel
- **SDR (Software Defined Radio)** :
  - RTL-SDR (réception)
  - HackRF, LimeSDR, USRP (émission/réception)
- **Oscilloscope** : Analyse I/Q
- **Analyseur de spectre**

### Mesure
- **Constellation analyser**
- **EVM (Error Vector Magnitude)**
- **BERT (Bit Error Rate Tester)**

## 📊 Évaluation

- Travaux pratiques (40%)
- Projet de communication (30%)
- Contrôle continu (15%)
- Examen final (15%)

## 🔗 Liens avec d'autres cours

- **Télécommunications (S3)** : Bases
- **Filtrage Numérique** : Filtres RRC
- **SE** : Traitement du signal
- **Antennes** : Propagation

## 📐 Comparaison des modulations

| Modulation | Bits/symbole | Efficacité spectrale | Robustesse | Applications |
|------------|--------------|----------------------|------------|--------------|
| BPSK | 1 | Faible | Excellente | GPS, RFID |
| QPSK | 2 | Moyenne | Bonne | Satellite, LTE |
| 8-PSK | 3 | Bonne | Moyenne | DVB-S2 |
| 16-QAM | 4 | Bonne | Moyenne | WiFi, LTE |
| 64-QAM | 6 | Élevée | Faible | WiFi 5, Câble |
| 256-QAM | 8 | Très élevée | Très faible | WiFi 6 |

## 💡 Applications réelles

### WiFi (802.11)
- OFDM avec sous-porteuses
- BPSK à 256-QAM (adaptatif)
- Codage LDPC
- MIMO

### 4G LTE
- OFDMA (downlink)
- SC-FDMA (uplink)
- QPSK, 16-QAM, 64-QAM
- Turbo codes
- MIMO

### 5G NR
- OFDM flexible
- Jusqu'à 256-QAM
- LDPC
- Massive MIMO
- Beamforming

### DVB (TV numérique)
- OFDM (DVB-T)
- PSK, QAM (DVB-S/C)
- Reed-Solomon + convolutif
- LDPC (DVB-S2)

## 📖 Compétences développées

- Conception de systèmes de modulation
- Analyse de performances (BER)
- Simulation de chaînes de transmission
- Implémentation sur SDR
- Optimisation spectrale
- Codage de canal

## 🎯 Efficacité spectrale

**Formule :**
$$\eta = \frac{R_b}{B} \text{ (bits/s/Hz)}$$

**Exemples :**
- BPSK : ~1 bit/s/Hz
- QPSK : ~2 bits/s/Hz
- 16-QAM : ~4 bits/s/Hz
- 64-QAM : ~6 bits/s/Hz

**Avec codage :**
Efficacité réduite mais gain en robustesse

## ⚠️ Limitations pratiques

### Non-linéarités
- Amplificateurs de puissance
- Distorsion de constellation
- PAPR (Peak-to-Average Power Ratio)
- Solutions : back-off, prédistorsion

### Synchronisation
- Synchronisation porteuse (phase)
- Synchronisation symbole (timing)
- CFO (Carrier Frequency Offset)
- Algorithms : PLL, Gardner, Costas

### Canal réel
- Multi-trajets (fading)
- Effet Doppler
- Interférences
- Solutions : égalisation, OFDM, MIMO

## 🔧 Dimensionnement pratique

### Lien budget
1. Puissance émise (dBm)
2. Gain antenne TX (dBi)
3. Pertes espace libre (dB)
4. Gain antenne RX (dBi)
5. Pertes câbles, etc.
6. = Puissance reçue (dBm)

### SNR requis
Dépend de :
- Modulation utilisée
- BER cible
- Codage de canal
- Marge de liaison

### Débit maximal
$$R_b = B \cdot \log_2(1 + SNR)$$
(Capacité de Shannon)

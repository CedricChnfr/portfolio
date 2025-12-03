---
layout: default
title: "Télécommunications - S3"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

# Télécommunications - Semestre 3

---

## PART A - Présentation Générale du Cours

### Contexte et objectifs

Introduction aux systèmes de télécommunications numériques : codage, modulations, transmission sur canal bruité, détection et correction d'erreurs. Fondement pour Télécom Num S4 et Réseaux.

**Objectifs :**
- Codage en ligne (NRZ, Manchester, etc.)
- Modulations numériques de base (ASK, FSK, PSK)
- Canal de transmission (bruit, atténuation)
- Détection/correction d'erreurs (CRC, codes correcteurs)
- Analyse performances (BER, SNR)

### Prérequis
- Signaux et systèmes (Fourier)
- OL S3 (MATLAB, modulations)

---

## PART B: EXPÉRIENCE, CONTEXTE ET FONCTION

### Module 1 : Codage en ligne

**Principe :**
Transformation bits (0/1) en signal électrique adapté à la transmission.

**Codes courants :**
- **NRZ (Non-Return to Zero)** : 0→-V, 1→+V. Simple mais composante DC.
- **RZ (Return to Zero)** : retour à 0 en milieu de bit. Synchronisation facilitée.
- **Manchester (Biphase)** : 0→transition haut-bas, 1→bas-haut. Pas de DC, auto-synchronisant (Ethernet 10Base-T).
- **Miller** : transition si 1, pas si 0 (sauf deux 0 consécutifs). Économie bande passante.
- **AMI (Alternate Mark Inversion)** : 0→0V, 1→±V alternés. Pas de DC.

**Critères choix :**
- Composante DC nulle (couplage AC)
- Densité transitions (synchronisation)
- Bande passante
- Immunité bruit

### Module 2 : Modulations numériques

**ASK (Amplitude Shift Keying) :**
- Modulation amplitude porteuse
- Sensible au bruit
- Peu utilisée seule

**FSK (Frequency Shift Keying) :**
- 0→f₁, 1→f₂
- Robuste au bruit
- Applications : modems bas débit, RFID, LoRa

**PSK (Phase Shift Keying) :**
- **BPSK** : 0→0°, 1→180° (2 symboles). Robuste.
- **QPSK** : 4 phases (0°, 90°, 180°, 270°) → 2 bits/symbole. WiFi, satellite.
- **8-PSK** : 8 phases → 3 bits/symbole.

**QAM (Quadrature Amplitude Modulation) :**
- Modulation amplitude + phase
- 16-QAM, 64-QAM, 256-QAM
- Haute efficacité spectrale (bits/Hz)
- Applications : 4G/5G, câble, WiFi

**Constellation :**
Représentation I/Q (en phase / quadrature) des symboles.

### Module 3 : Canal de transmission

**Modèle canal :**
- Atténuation (pertes propagation)
- Bruit AWGN (Additive White Gaussian Noise)
- Interférences
- Distorsion (multi-trajets, dispersion)

**SNR (Signal-to-Noise Ratio) :**
$$SNR_{dB} = 10 \log_{10}\left(\frac{P_{signal}}{P_{bruit}}\right)$$

**Capacité de Shannon :**
$$C = B \log_2(1 + SNR) \quad \text{(bits/s)}$$
Capacité maximale théorique du canal.

**BER (Bit Error Rate) :**
Taux d'erreur binaire. BER < 10⁻⁶ typique pour communications fiables.

### Module 4 : Détection et correction d'erreurs

**Détection d'erreurs :**
- **Bit de parité** : pair/impair. Détecte erreurs impaires.
- **Checksum** : somme octets.
- **CRC (Cyclic Redundancy Check)** : division polynomiale. Très efficace (Ethernet, USB). CRC-16, CRC-32.

**Correction d'erreurs (FEC - Forward Error Correction) :**
- **Code de Hamming** : corrige 1 erreur, détecte 2.
- **Codes Reed-Solomon** : CD, DVD, QR codes. Correction paquets d'erreurs.
- **Codes convolutifs** : mémoire, décodage Viterbi. Espace, 4G.
- **Turbo codes, LDPC** : proches limite Shannon. 5G.

**Principe :**
Ajout redondance (bits supplémentaires) pour détecter/corriger erreurs sans retransmission.

---

## PART C: ASPECTS TECHNIQUES

### TP MATLAB

**TP1 : Codages en ligne**
- Génération séquence bits
- Codage NRZ, Manchester, AMI
- Analyse spectrale (DSP)

**TP2 : Modulation BPSK**
- Génération porteuse, modulation
- Canal AWGN (SNR variable)
- Démodulation
- Calcul BER vs SNR

**TP3 : QPSK et constellation**
- Modulation QPSK
- Diagramme constellation I/Q
- Impact bruit sur constellation

**TP4 : CRC**
- Implémentation CRC-8, CRC-16
- Test détection erreurs (1 bit, 2 bits, burst)

### Projet simulation chaîne complète

**Architecture :**
```
[Source bits] → [Codeur canal] → [Modulateur] → [Canal AWGN]
                                                     ↓
[Sink bits]  ← [Décodeur]     ← [Démodulateur]     ←
```

**Paramètres :**
- Modulation : QPSK
- Code correcteur : Hamming (7,4)
- SNR : 0 à 15 dB
- Débit : 1 Mbps

**Résultats :**
- Courbes BER vs SNR (avec/sans codage)
- Gain de codage (≈3-5 dB)

---

## PART D: ANALYSE ET RÉFLEXION

### Évaluation
- TP MATLAB (40%)
- Projet chaîne de transmission (30%)
- Contrôles (15%)
- Examen final (15%)

### Compétences acquises
- Compréhension systèmes télécommunications numériques
- Simulation MATLAB (modulations, canal, BER)
- Analyse performances (SNR, BER, capacité)
- Codage détection/correction d'erreurs
- Fondements pour 4G/5G, WiFi, satellite

### Applications professionnelles
- Télécommunications (mobiles, satellite, fibre)
- Réseaux sans fil (WiFi, LoRa, Bluetooth)
- Ingénieur RF/télécom
- IoT (protocoles bas débit)
5. Canal de transmission
6. Démodulateur
7. Décodeur de canal
8. Décodeur de source
9. Destinataire

#### Caractéristiques
- Débit binaire (bits/s)
- Bande passante (Hz)
- Efficacité spectrale (bits/s/Hz)
- Probabilité d'erreur (BER)
- Rapport signal/bruit (SNR)

### Codage en ligne

#### Principe
Représentation électrique des données binaires pour la transmission sur un canal.

#### Codes NRZ (Non Return to Zero)

**NRZ-L (Level) :**
- 0 : niveau bas
- 1 : niveau haut
- Simple mais composante continue
- Pas d'auto-synchronisation

**NRZ-I (Inverted) :**
- Transition sur les '1'
- Pas de transition sur les '0'
- Meilleure synchronisation

#### Codes RZ (Return to Zero)
- Retour à zéro au milieu du bit
- Meilleure synchronisation
- Bande passante doublée

#### Code Manchester
- Transition au milieu de chaque bit
- 0 : haut → bas
- 1 : bas → haut
- Auto-synchronisation
- Utilisé en Ethernet 10BASE-T

#### Code Manchester différentiel
- Transition en début de bit
- Présence/absence de transition au milieu

#### Code Bipolaire (AMI)
- 0 : niveau zéro
- 1 : alternance +V et -V
- Pas de composante continue
- Détection d'erreurs

#### Codes MLT-3, PAM-5
- Multi-niveaux
- Efficacité spectrale améliorée
- Utilisés en Ethernet rapide

### Transmission en bande de base

#### Critère de Nyquist
- Pas d'interférence entre symboles (ISI)
- Filtre en cosinus surélevé (raised cosine)
- Roll-off factor
- Bande passante minimale

#### Diagramme de l'œil
- Outil d'évaluation qualité
- Ouverture verticale (marge bruit)
- Ouverture horizontale (timing)
- Taux d'erreur binaire (BER)

#### Égalisation
- Compensation distorsions canal
- Égaliseur linéaire
- Égaliseur adaptatif (LMS)
- Égaliseur à retour de décision (DFE)

### Détection et correction d'erreurs

#### Codes détecteurs

**Parité simple :**
- Bit de parité pair ou impair
- Détecte erreur unique
- Ne corrige pas

**Parité croisée (2D) :**
- Parité lignes et colonnes
- Détecte et corrige certaines erreurs

**CRC (Cyclic Redundancy Check) :**
- Polynôme générateur
- Reste de division polynomiale
- CRC-8, CRC-16, CRC-32
- Très efficace pour détection

#### Codes correcteurs

**Code de Hamming :**
- Distance de Hamming
- Correction 1 bit, détection 2 bits
- Hamming(7,4), Hamming(15,11)
- Bits de parité positionnés en 2^n

**Code de Reed-Solomon :**
- Code cyclique non binaire
- Correction de rafales d'erreurs
- Utilisé en CD, DVD, QR codes
- RS(255,223) typique

**Codes convolutifs :**
- Encodage continu
- Décodage Viterbi
- Utilisés en téléphonie mobile
- Rendement r = k/n

**Turbo codes et LDPC :**
- Codes modernes haute performance
- Proche limite de Shannon
- 4G, 5G, satellites

### Performances de transmission

#### Probabilité d'erreur binaire (BER)
- BER = erreurs / bits transmis
- Dépend du SNR
- Objectifs : 10^-6 à 10^-12

#### Rapport Eb/N0
- Énergie par bit / Densité de bruit
- Mesure de qualité
- Courbes BER vs Eb/N0

#### Capacité de Shannon
- $C = B \log_2(1 + SNR)$
- Limite théorique
- Débit maximal sans erreur

## 🛠️ Travaux pratiques

### TP Codage en ligne
- Génération de codes (NRZ, Manchester, AMI)
- Analyse spectrale
- Simulation de transmission
- Diagramme de l'œil

### TP CRC
- Implémentation algorithme CRC
- Test de détection d'erreurs
- Comparaison CRC-8, CRC-16, CRC-32
- Application sur microcontrôleur

### TP Code de Hamming
- Encodage Hamming(7,4)
- Décodage et correction
- Insertion d'erreurs
- Taux de correction

### Projet communication
- Liaison série codée
- Protection par CRC
- Protocole applicatif
- Tests de robustesse

## 💻 Outils utilisés

### Simulation
- **MATLAB/Simulink** : Simulation systèmes
- **Python** : Programmation algorithmes
- **GNU Radio** : SDR et communications
- **LabVIEW** : Acquisition et traitement

### Développement
- **STM32** : Implémentation embarquée
- **Arduino** : Prototypage rapide
- **UART, SPI, I2C** : Interfaces

### Mesure
- **Oscilloscope** : Signaux et diagramme œil
- **Analyseur logique** : Décodage protocoles
- **BERT (Bit Error Rate Tester)** : Mesure BER

## 📊 Évaluation

- Travaux pratiques (40%)
- Projet de communication (30%)
- Contrôle continu (15%)
- Examen final (15%)

## 🔗 Liens avec d'autres cours

- **SE** : Traitement du signal
- **OL** : Modulation/démodulation
- **IE** : Implémentation protocoles
- **Télécommunications Numériques (S4)** : Approfondissement
- **Réseau** : Couches protocolaires

## 📐 Exemples de calculs

### Distance de Hamming
Nombre de bits différents entre deux mots :
- 1011**0**1 vs 1011**1**1 → distance = 1
- **10**1**1**01 vs **01**1**0**01 → distance = 3

### CRC-8
Polynôme : $x^8 + x^2 + x + 1$ (0x107)
```
Message : 11010011101100
Reste   : 10101010
Message transmis : 11010011101100 10101010
```

### Code de Hamming(7,4)
4 bits données : d1 d2 d3 d4
3 bits parité : p1 p2 p3

Position : p1 p2 d1 p3 d2 d3 d4
```
p1 = d1 ⊕ d2 ⊕ d4
p2 = d1 ⊕ d3 ⊕ d4
p3 = d2 ⊕ d3 ⊕ d4
```

## 💡 Applications pratiques

### Réseaux filaires
- Ethernet (Manchester)
- USB (NRZI)
- RS-232/RS-485

### Communications sans fil
- WiFi (OFDM + codes)
- Bluetooth (FEC)
- Zigbee

### Stockage
- Disques durs (Reed-Solomon)
- Mémoires flash (BCH, LDPC)
- Codes QR

### Audiovisuel
- DVB (télévision numérique)
- DAB (radio numérique)
- HDMI

## 📖 Compétences développées

- Codage et décodage de données
- Analyse de performances de transmission
- Implémentation d'algorithmes de protection
- Diagnostic de liaisons de communication
- Simulation de systèmes numériques
- Mesure et optimisation BER

## 🎯 Protocoles étudiés

### Protocole de liaison de données
- Tramage
- Synchronisation
- Détection d'erreurs (CRC)
- Acquittements (ACK/NACK)
- Retransmission (ARQ)

### Exemple : Protocole simple
```
[Start] [Length] [Data] [CRC16] [Stop]
  0x02     1B      nB      2B     0x03
```

## ⚠️ Problèmes courants

### Transmission
- Atténuation du signal
- Bruit (thermique, impulsionnel)
- Distorsion (ISI)
- Dérive d'horloge
- Réflexions (impédance)

### Codage
- Composante continue excessive
- Bande passante trop large
- Perte de synchronisation
- Détection d'erreurs insuffisante

## 🔧 Implémentation embarquée

### CRC sur microcontrôleur
```c
uint8_t crc8(uint8_t *data, uint8_t len) {
    uint8_t crc = 0;
    for(uint8_t i=0; i<len; i++) {
        crc ^= data[i];
        for(uint8_t j=0; j<8; j++) {
            if(crc & 0x80)
                crc = (crc << 1) ^ 0x07;
            else
                crc <<= 1;
        }
    }
    return crc;
}
```

### Code Manchester
```c
void manchester_encode(uint8_t data, uint16_t *output) {
    for(int i=0; i<8; i++) {
        if(data & (1<<(7-i)))
            *output |= (0b01 << (14-i*2)); // 1 → 01
        else
            *output |= (0b10 << (14-i*2)); // 0 → 10
    }
}
```

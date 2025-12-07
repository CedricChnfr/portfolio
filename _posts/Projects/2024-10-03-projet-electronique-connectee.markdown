---
layout: default
title: "Connected Electronics System (RF Communication)"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

[← Back to Academic Project](./my-projects.html)

# Introduction
This comprehensive synthesis project involved designing and implementing a complete RF wireless communication system from scratch. The system featured separate transmitter and receiver modules, integrating analog sensor conditioning, microcontroller data processing, digital modulation (FSK/ASK), RF amplification, and custom antennas to achieve reliable wireless data transmission over 50-100 meters.

# Project Overview
Working in pairs over 60 hours, we developed a full duplex or half-duplex wireless link operating in the ISM band (433 or 868 MHz). The project synthesized knowledge from analog electronics, digital systems, RF circuits, telecommunications, and embedded programming.

## System Architecture

### Transmitter Chain
1. **Data Acquisition:** Sensors (temperature, pressure, accelerometer) with analog conditioning
2. **Processing:** STM32 microcontroller for data framing (preamble + data + CRC)
3. **Modulation:** FSK (Frequency Shift Keying) or ASK (Amplitude Shift Keying) implementation
4. **RF Amplification:** Power amplifier delivering +10 to +20 dBm
5. **Antenna:** Matched monopole or patch antenna (50Ω)

### Receiver Chain
1. **Antenna:** Receiving antenna with 50Ω impedance matching
2. **LNA:** Low Noise Amplifier (15-20 dB gain, NF < 3 dB)
3. **Demodulation:** FSK/ASK detector with threshold comparator
4. **Processing:** STM32 for frame synchronization and CRC validation
5. **Display:** LCD/OLED or UART output to PC

# Design and Implementation

## RF Link Budget
Calculated using Friis transmission formula:
- Transmit power: +10 dBm (10 mW)
- Frequency: 433 MHz or 868 MHz
- Antenna gains: ~2 dBi each
- Target range: > 50 m outdoor
- Data rate: 1-10 kbps

## Modulation Schemes

**FSK (Frequency Shift Keying):**
- Binary 0 → frequency f₁
- Binary 1 → frequency f₂
- Frequency deviation: ±25 kHz
- Generated using MCU PWM or dedicated modulator IC (RFM69)

**ASK (Amplitude Shift Keying):**
- Binary 0 → amplitude A₀ (low/off)
- Binary 1 → amplitude A₁ (high)
- Simpler implementation but more susceptible to noise

## PCB Design
Fabricated two separate PCBs:

**Transmitter PCB:**
- Sensor inputs and conditioning circuits
- STM32 microcontroller
- Modulator stage
- RF power amplifier
- Antenna matching network

**Receiver PCB:**
- Antenna input with protection
- LNA and band-pass filter
- Demodulator circuit
- STM32 microcontroller
- Display interface

## Software Implementation

**Transmitter Firmware:**
```c
// Data frame structure
struct Packet {
    uint8_t preamble[4];    // Sync pattern
    uint8_t data[32];       // Payload
    uint16_t crc;           // Error detection
};

// Transmit function
void transmit_packet(uint8_t *data, uint8_t length) {
    prepare_frame(data, length);
    modulate_and_send();
    wait_for_ack();
}
```

**Receiver Firmware:**
- Preamble detection for synchronization
- CRC verification
- Error handling and retransmission requests

# Testing and Validation

## Unit Testing
- Power supply voltages and ripple
- Modulation signal quality (oscilloscope)
- RF output power and spectrum (spectrum analyzer)
- Demodulator threshold levels

## System Integration
- Short-range testing (1 m) for initial validation
- Progressive distance testing up to 100 m
- RSSI (Received Signal Strength Indicator) measurements
- Bit Error Rate (BER) characterization
- Performance in noisy environments

## Results
Successfully achieved:
- Reliable communication at 50+ meters outdoor
- Data rate of 9600 bps
- BER < 10⁻³ under normal conditions
- Power consumption optimized for battery operation

# Conclusion
This project provided invaluable hands-on experience in designing complete RF communication systems. We successfully integrated multiple engineering disciplines to create a functional wireless link, demonstrating the importance of systematic design, careful testing, and iterative optimization in complex electronic systems.

<style>
p {
  text-align: justify;
}
.modal {
  display: none; 
  position: fixed; 
  z-index: 1; 
  padding-top: 60px; 
  left: 0;
  top: 0;
  width: 100%; 
  height: 100%; 
  overflow: auto; 
  background-color: rgb(0,0,0); 
  background-color: rgba(0,0,0,0.9); 
}

.modal-content {
  margin: auto;
  display: block;
  width: 80%;
  max-width: 700px;
}

.close {
  position: absolute;
  top: 15px;
  right: 35px;
  color: #f1f1f1;
  font-size: 40px;
  font-weight: bold;
  transition: 0.3s;
}

.close:hover,
.close:focus {
  color: #bbb;
  text-decoration: none;
  cursor: pointer;
}
</style>

<!-- Modal -->
<div id="myModal" class="modal">
  <span class="close" onclick="closeModal()">&times;</span>
  <img class="modal-content" id="img01">
</div>

<script>
function openModal(src) {
  var modal = document.getElementById("myModal");
  var modalImg = document.getElementById("img01");
  modal.style.display = "block";
  modalImg.src = src;
}

function closeModal() {
  var modal = document.getElementById("myModal");
  modal.style.display = "none";
}
</script>

---

## PART B: EXPÉRIENCE, CONTEXTE ET FONCTION (Architecture système)

### Chaîne d'émission

**Bloc 1 : Acquisition :**
- Capteur (température, pression, accéléromètre)
- Conditionnement analogique (ampli, filtrage)
- ADC microcontrôleur

**Bloc 2 : Traitement et codage :**
- MCU (STM32, Arduino)
- Mise en forme données (trame : préambule, data, CRC)
- Codage source (compression si besoin)

**Bloc 3 : Modulation :**
- **FSK** (Frequency Shift Keying) : 0→f1, 1→f2
- **ASK** (Amplitude Shift Keying) : 0→A0, 1→A1
- Génération MCU (PWM, DAC) ou CI modulateur (ex: RFM69)

**Bloc 4 : Amplification RF :**
- PA (Power Amplifier) : +10 à +20 dBm
- Transistor (BFG, 2N2222) ou CI (RFX2401)
- Adaptation impédance

**Bloc 5 : Antenne TX :**
- Monopole, patch, ou dipole
- Adaptation 50Ω

### Chaîne de réception

**Bloc 1 : Antenne RX**

**Bloc 2 : Préamplification :**
- LNA (Low Noise Amplifier) : gain 15-20 dB, NF <3 dB
- Filtrage passe-bande (rejet hors-bande)

**Bloc 3 : Démodulation :**
- Détecteur FSK/ASK
- Comparateur à seuil → signal TTL

**Bloc 4 : Traitement numérique :**
- MCU réception
- Détection préambule (synchronisation)
- Vérification CRC
- Extraction données

**Bloc 5 : Affichage :**
- LCD, OLED, ou UART PC

---

## PART C: ASPECTS TECHNIQUES (Réalisation)

### Phase 1 : Conception (20h)

**Spécifications :**
- Fréquence : 433 MHz ou 868 MHz (ISM)
- Débit : 1-10 kbps
- Portée : >50 m (extérieur)
- Puissance TX : +10 dBm (10 mW)

**Schéma fonctionnel :**
- Blocs détaillés
- Calcul bilan de liaison (Friis)
- Choix composants

### Phase 2 : Simulation (10h)

**Analogique (LTSpice) :**
- Amplis RF (PA, LNA)
- Filtres passe-bande

**Numérique (MATLAB) :**
- Modulation FSK/ASK
- BER vs SNR

### Phase 3 : Réalisation PCB (15h)

**2 cartes :**
- **Carte TX** : capteur + MCU + modulateur + PA + antenne
- **Carte RX** : antenne + LNA + démodulateur + MCU + affichage

**Conception :**
- Schémas KiCad/Altium
- PCB 2-4 couches
- Séparation analog/RF/digital
- Via stitching GND
- Fabrication + assemblage

### Phase 4 : Tests et validation (15h)

**Tests unitaires :**
- Alimentation (tensions, ondulations)
- Génération modulation (oscillo)
- Amplification RF (analyseur spectre)
- Réception signal (démodulation)

**Tests système :**
- Liaison courte distance (1 m)
- Liaison longue distance (50-100 m)
- Mesure RSSI, BER
- Test en environnement bruité

---

## PART D: ANALYSE ET RÉFLEXION

### Livrables
- Rapport technique (40 pages) : conception, simulations, réalisation, tests
- Schémas et PCB
- Code source (MCU TX/RX)
- Présentation + démonstration

### Évaluation
- Conception système (20%)
- Réalisation matérielle (25%)
- Programmation (15%)
- Tests et validation (20%)
- Rapport (15%)
- Présentation (5%)

### Compétences acquises
- Conception systèmes RF complets
- Intégration analogique-numérique-RF
- Modulation/démodulation pratique
- Gestion projet complexe en binome
- Tests et validation systématiques

### Applications professionnelles
- Ingénieur systèmes IoT
- Concepteur électronique RF
- R&D télécommunications

## 📚 Contexte du projet

### Chaîne de communication complète

**Architecture générale :**
```
[Capteur] → [Conditionnement] → [MCU] → [Modulation] 
    → [Amplification RF] → [Antenne TX]
    
        ~~~ Canal radio ~~~
        
[Antenne RX] → [Amplification RF] → [Démodulation] 
    → [MCU] → [Traitement] → [Affichage/Transmission]
```

### Projets types

#### Liaison audio sans fil
- Émetteur audio FM/FSK
- Récepteur avec démodulation
- Modulation analogique ou numérique
- Bande ISM (2.4 GHz ou 433/868 MHz)

#### Télémétrie capteurs
- Émetteur multi-capteurs (T°, P, humidité)
- Modulation numérique (FSK, PSK)
- Récepteur avec décodage
- Affichage temps réel
- Stockage données

#### Commande à distance
- Émetteur (télécommande)
- Codage sécurisé
- Récepteur
- Actions sur actuateurs
- Feedback

## 🛠️ Exemple détaillé : Système de communication RF

### Cahier des charges

#### Spécifications système

**Fréquence :**
- Bande ISM : 433 MHz ou 868 MHz (Europe)
- Alternative : 2.4 GHz (WiFi/BT)
- Largeur de bande : 200 kHz

**Modulation :**
- FSK (Frequency Shift Keying)
- Débit : 9600 bps minimum
- Déviation : ±25 kHz

**Puissance :**
- Émetteur : 10 mW (10 dBm)
- Portée : 100m en champ libre
- Respect réglementation ETSI

**Communication :**
- Liaison half-duplex
- Protocole simple (préambule + données + CRC)
- Acquittements

### Conception émetteur

#### Architecture émetteur

**Blocs fonctionnels :**

1. **Acquisition données :**
   - Microcontrôleur (STM32)
   - Interface capteurs ou audio
   - Échantillonnage et conversion A/N

2. **Codage et mise en forme :**
   - Codage source (compression optionnelle)
   - Codage canal (détection erreurs)
   - Mise en paquet
   - Ajout CRC

3. **Modulation :**
   - Génération FSK
   - VCO (Voltage Controlled Oscillator)
   - Ou module RF intégré

4. **Émission RF :**
   - Amplification PA (Power Amplifier)
   - Filtrage passe-bande
   - Adaptation d'impédance
   - Antenne

#### Schémas émetteur

**Option 1 : Module RF intégré**

Utilisation module type RFM69, SX1276 (LoRa), nRF24L01, etc.

*Avantages :*
- Simple à intégrer
- Fiable
- Homologué
- Communication SPI avec MCU

*Exemple avec RFM69 :*
- Fréquence : 433/868/915 MHz
- Modulation FSK/GFSK
- Puissance : jusqu'à +20 dBm
- Sensibilité : -120 dBm
- Interface SPI
- Configuration par registres

**Connexions :**
```
STM32 (SPI) ↔ RFM69
    MOSI → MOSI
    MISO → MISO
    SCK  → SCK
    NSS  → NSS
    DIO0 → GPIO (interruption)
```

**Option 2 : Conception discrète**

*Blocs à concevoir :*

**VCO (Oscillateur) :**
- Générateur 433/868 MHz
- Modulation FM par tension
- Stabilité en fréquence (PLL + quartz)

**Amplificateur de puissance :**
- Classe C ou E (efficacité)
- Gain : 10-20 dB
- P out : 10 mW (+10 dBm)
- Transistor RF (BFR93, 2N3904, etc.)

**Filtrage :**
- Filtre passe-bande centré sur fo
- Rejection harmoniques
- Topologie LC ou SAW

**Adaptation et antenne :**
- Réseau L, π ou stub
- Smith chart
- Mesure S11 < -10 dB

#### Logiciel émetteur

**Structure code :**

```c
void transmit_packet(uint8_t *data, uint8_t length) {
    // 1. Préparation paquet
    packet[0] = PREAMBLE;     // 0xAA (synchronisation)
    packet[1] = SYNC_WORD;    // 0x2D (identification)
    packet[2] = length;       // Longueur données
    memcpy(&packet[3], data, length);
    
    // 2. Calcul CRC
    uint16_t crc = calculate_crc16(data, length);
    packet[3 + length] = (crc >> 8) & 0xFF;
    packet[4 + length] = crc & 0xFF;
    
    // 3. Émission via module RF
    RFM69_send(packet, 5 + length);
    
    // 4. Attente acquittement (optionnel)
    wait_for_ack(TIMEOUT_MS);
}
```

**Gestion protocole :**
- Détection de collision (CSMA)
- Retransmissions automatiques
- Horodatage
- Numéro de séquence

### Conception récepteur

#### Architecture récepteur

**Blocs fonctionnels :**

1. **Réception RF :**
   - Antenne
   - Filtre passe-bande
   - LNA (Low Noise Amplifier)
   - Mélangeur (down-conversion)

2. **Démodulation :**
   - Discriminateur FM
   - Ou démodulateur numérique (DSP)
   - Récupération d'horloge

3. **Décodage :**
   - Synchronisation (préambule)
   - Récupération des données
   - Vérification CRC
   - Détection et correction d'erreurs

4. **Traitement :**
   - MCU (STM32)
   - Interprétation données
   - Actions ou affichage
   - Transmission vers PC (USB/UART)

#### Schémas récepteur

**Option 1 : Module RF intégré**

Même module que l'émetteur (RFM69, etc.) en mode RX

*Configuration réception :*
```c
RFM69_setMode(RX_MODE);
RFM69_setFrequency(433.92 MHz);
RFM69_setBitrate(9600);
RFM69_setRxBandwidth(50 kHz);
```

*Interruption sur réception :*
```c
void RFM69_IRQ_Handler(void) {
    if (packet_received) {
        uint8_t length = RFM69_read_FIFO(rx_buffer);
        process_packet(rx_buffer, length);
    }
}
```

**Option 2 : Conception discrète**

**LNA (Low Noise Amplifier) :**
- Faible bruit (NF < 2 dB)
- Gain : 15-20 dB
- Transistor faible bruit (ATF-531P8, etc.)

**Mélangeur et FI (Fréquence Intermédiaire) :**
- Down-conversion vers FI (10.7 MHz typique)
- Oscillateur local (LO)
- Filtre FI

**Démodulateur FM :**
- Discriminateur (quadrature detector)
- PLL (CD4046, NE565)
- Sortie bande de base

**Comparateur :**
- Conversion analogique → numérique
- Seuil ajustable
- Hystérésis

#### Logiciel récepteur

**Structure code :**

```c
void receive_handler(void) {
    uint8_t rx_buffer[MAX_PACKET_SIZE];
    
    // 1. Attente données
    if (RFM69_available()) {
        uint8_t length = RFM69_receive(rx_buffer);
        
        // 2. Vérification préambule et sync
        if (rx_buffer[0] == PREAMBLE && 
            rx_buffer[1] == SYNC_WORD) {
            
            // 3. Extraction données
            uint8_t data_length = rx_buffer[2];
            uint8_t *data = &rx_buffer[3];
            
            // 4. Vérification CRC
            uint16_t crc_received = (rx_buffer[3+data_length] << 8) | 
                                     rx_buffer[4+data_length];
            uint16_t crc_calculated = calculate_crc16(data, data_length);
            
            if (crc_received == crc_calculated) {
                // 5. Traitement données
                process_data(data, data_length);
                
                // 6. Envoi acquittement
                send_ack();
            } else {
                // Erreur CRC
                error_count++;
            }
        }
    }
}
```

**Traitement données :**
- Affichage LCD/OLED
- Transmission UART vers PC
- Enregistrement sur SD
- Actions sur sorties

### Antennes

#### Design antennes

**Émetteur et récepteur :**
- Antennes identiques (réciprocité)
- Monopole λ/4 sur plan de masse
- Ou antenne fouet accordée
- Ou antenne PCB (économique)

**Dimensionnement 433 MHz :**
- λ = 69 cm
- λ/4 = 17.3 cm
- Avec plan de masse 20×20 cm minimum

**Dimensionnement 868 MHz :**
- λ = 34.5 cm
- λ/4 = 8.6 cm
- Plus compact

**Optimisations :**
- Simulation MMANA-GAL ou CST
- Mesure S11 avec VNA
- Ajustement longueur

### Tests et validation

#### Tests unitaires

**Émetteur :**
- Fréquence porteuse (analyseur de spectre)
- Puissance émise (wattmètre RF)
- Déviation fréquence (FSK)
- Spectre (largeur bande, harmoniques)
- Modulation visualisée

**Récepteur :**
- Sensibilité (puissance minimum détectable)
- Sélectivité (bande passante)
- Démodulation correcte
- Taux d'erreur sans bruit

#### Tests d'intégration

**Liaison complète :**
- Émission → réception
- Distance variable
- Environnements différents (indoor/outdoor)
- Obstacles

**Mesures de performances :**

**Portée :**
- Distance max pour BER acceptable
- Selon environnement
- Comparaison avec théorie (Friis)

**Taux d'erreur binaire (BER) :**
$$BER = \frac{\text{Bits erronés}}{\text{Bits totaux}}$$

Objectif : BER < 10^-3 à 10^-5

**Débit effectif :**
- Avec entêtes et CRC
- Avec retransmissions
- Débit utile vs débit brut

**Latence :**
- Temps émission → réception
- Temps de traitement
- Bout en bout

#### Tests en conditions réelles

**Scénarios d'usage :**
- Intérieur bâtiment
- Extérieur champ libre
- Avec interférences (WiFi, BT)
- Mobilité (véhicule)

**Robustesse :**
- Variation température
- Alimentation variable
- Durée continue
- Stress test

### Améliorations possibles

#### Hardware
- Amplification adaptative (AGC)
- Filtres adaptatifs
- Diversité d'antennes
- Meilleure sensibilité (LNA optimisé)

#### Software
- FEC (Forward Error Correction)
- ARQ (Automatic Repeat Request)
- Codage convolutif ou Turbo
- Compression données
- Chiffrement (AES)

#### Protocole
- CSMA/CA (éviter collisions)
- Multi-canaux
- Time-slotting (TDMA)
- Mesh networking

## 💻 Outils utilisés

### Conception RF
- **AWR Microwave Office** : Circuits RF
- **Qucs** : Open source simulation RF
- **LTspice** : Circuits RF simples

### Simulation antennes
- **MMANA-GAL** : Antennes filaires
- **CST/HFSS** : 3D EM

### PCB
- **Altium/KiCad** : Design RF

### Mesure RF
- **Analyseur de spectre** : Fréquence, puissance, spectre
- **VNA** : S-paramètres, adaptation
- **Wattmètre RF** : Puissance
- **Générateur RF** : Tests

### Software
- **STM32CubeIDE** / **PlatformIO**
- **GNU Radio** : Prototypage SDR
- **Python** : Post-traitement, GUI

## 📊 Livrables

### Documentation
- Cahier des charges
- Architecture système
- Schémas émetteur et récepteur
- PCB et layout
- Logiciels (code source commenté)
- Calculs de bilans de liaison
- Résultats de simulations
- Protocole de communication
- Tests et mesures
- Rapport technique complet (60-100 pages)

### Réalisations
- Émetteur fonctionnel
- Récepteur fonctionnel
- Antennes
- Démonstration liaison
- Interface utilisateur (PC ou LCD)

### Présentation
- Soutenance avec démo live
- Vidéo de démonstration
- Poster technique

## 🔗 Liens avec les cours

- **Télécommunications (S3, S4)** : Modulation
- **Antennes et Propagation (S4)** : Conception antennes
- **Circuits Hyperfréquences (S3)** : Circuits RF
- **Filtrage Numérique (S4)** : Traitement signal
- **IE** : Programmation embarquée
- **ER** : Conception PCB RF

## 📖 Compétences développées

- Conception de systèmes RF complets
- Modulation et démodulation
- Protocoles de communication
- Design d'antennes
- PCB RF (impédance contrôlée)
- Mesures RF
- Programmation communication
- Bilans de liaison
- Gestion de projet complexe
- Travail en équipe

## 💡 Extensions possibles

### Fonctionnalités avancées
- Liaison bidirectionnelle (full-duplex)
- Multiple émetteurs (réseau)
- Routage multi-hop
- Localisation (RSSI, TOA)
- Adaptive data rate

### Applications
- Réseau de capteurs (WSN)
- Domotique sans fil
- Télémétrie véhicules
- Commande drone
- Audio streaming

## ⚠️ Conformité réglementaire

### Puissance et fréquence
- Respecter limites ETSI EN 300 220
- Bandes ISM : 433.05-434.79 MHz, 863-870 MHz
- Puissance max : 10 mW (433 MHz), 25 mW (868 MHz)
- Duty cycle parfois limité

### Homologation
- Tests EMC nécessaires pour commercialisation
- Marquage CE
- FCC (États-Unis) si export

### Sécurité
- Pas d'interférences avec services critiques
- Tests en environnement contrôlé

## 🎯 Critères d'évaluation

- Conception système (20%)
- Réalisation émetteur (15%)
- Réalisation récepteur (15%)
- Liaison fonctionnelle (20%)
- Tests et performances (15%)
- Documentation (10%)
- Soutenance et démo (5%)

## 📚 Ressources

- "RF Circuit Design" - Chris Bowick
- "Wireless Communications" - Andrea Goldsmith
- Application notes Analog Devices, Texas Instruments
- Datasheets modules RF (RFM69, SX1276, nRF24)
- Forums RF (edaboard, electronics.stackexchange)
- Standards ETSI EN 300 220

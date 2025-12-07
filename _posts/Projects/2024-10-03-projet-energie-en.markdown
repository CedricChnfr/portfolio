---
layout: default
title: "Autonomous Energy Management System"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

[← Back to Academic Project](./my-projects.html)

# Introduction
This specialized energy project focused on designing autonomous systems with intelligent power management and renewable energy integration. Working in pairs over 60 hours, we developed battery-powered devices with solar charging, optimized power consumption, and sophisticated energy management algorithms. Example projects included autonomous LED cubes, solar-powered IoT weather stations, and intelligent lighting systems.

# Project Overview
The project synthesized knowledge from power electronics, renewable energy systems, embedded programming, and low-power design techniques. The goal was to create systems capable of operating indefinitely on harvested energy or achieving maximum autonomy from battery power through intelligent consumption management.

## Example Project Types

### Autonomous Display Systems
**8×8×8 LED Cube:**
- 512 RGB LEDs (WS2812B) in 3D matrix
- STM32 microcontroller for animation control
- Li-Ion 18650 battery (3.7V, 3000 mAh)
- Solar panel charging (5W)
- Target autonomy: 2-4 hours continuous use
- Programmed animations and effects

**Solar-Powered Smart Lamp:**
- High-power LEDs (10W total)
- PIR motion detection
- 20W solar panel
- LiFePO4 12V 10Ah battery
- Arduino MPPT charge controller
- Autonomy: 3 nights without sun

### IoT Autonomous Systems
**Ultra-Low-Power Weather Station:**
- Environmental sensors (T°, pressure, humidity)
- STM32L0 or ESP32 in deep-sleep mode
- LoRa transmission (minimal data)
- 1W solar panel
- Supercapacitor or small battery
- Target: indefinite autonomy with sunlight

**Solar GPS Tracker:**
- GPS module (NEO-6M)
- Accelerometer for motion detection
- GSM/LoRa transmission
- Solar charging system
- Optimization: transmit position only when moving

# Energy Budget and Sizing

## Power Consumption Analysis
Detailed current consumption calculation for each subsystem:

**Example: LED Cube**
- STM32 active: 50 mA
- STM32 sleep: 2 mA
- LEDs average (animations): 400 mA
- Total average: 500 mA
- Battery life: 3000 mAh / 500 mA = 6 hours

## Battery Sizing
- Capacity requirements (mAh)
- Voltage selection (Li-Ion 3.7V, LiFePO4 3.2V, Lead-acid 12V)
- Chemistry choice based on application
- Charge/discharge cycle considerations

## Solar Panel Dimensioning
Formula: P = Daily Energy / (Sunlight Hours × Efficiency)

Example calculation:
- Daily energy: 10 Wh
- Sun hours: 4h
- Efficiency: 80%
- Required panel: P = 10 / (4 × 0.8) = 3W minimum

# Power Supply Design

## Battery Charging
**Li-Ion Charging:**
- Linear chargers: TP4056, MCP73831 (< 1A)
- Switching chargers: LTC4011, BQ24075 (> 1A)
- Protection: overcharge, deep discharge, short circuit

**Charge Controller:**
- Constant Current / Constant Voltage (CC/CV) algorithm
- Temperature monitoring (NTC thermistor)
- Charge status indication
- MPPT (Maximum Power Point Tracking) for solar optimization

## DC-DC Converters
**Buck Converter (Step-Down):**
- Battery → 3.3V/5V for microcontroller
- Efficiency: 85-95%
- Examples: TPS54302 (3A), LM2596

**Boost Converter (Step-Up):**
- Low battery voltage → higher voltage
- For LED drivers or 5V peripherals
- Examples: MT3608, TPS61070

## Low-Power Microcontroller Management
**Sleep Modes:**
- Sleep: CPU stopped, peripherals active
- Stop: All clocks stopped, RAM retained
- Standby: Lowest power, minimal RAM

**Optimization Techniques:**
- RTC wake-up for periodic measurements
- Disable unused peripherals
- Reduce CPU frequency when possible
- Event-driven architecture

# PCB Design and Integration

## Layout Considerations
**Power Supply Section:**
- Short loops for switching converters
- Large copper areas for current handling
- Proper ground plane
- Thermal management for regulators

**Component Placement:**
- Solar panel connector accessible
- Battery holder secure and safe
- Charge controller near battery
- DC-DC converters near loads

## Safety Features
- Reverse polarity protection
- Overcurrent protection
- Thermal shutdown
- Battery level monitoring with ADC
- Visual indicators (LEDs)

# Software Optimization

## Power Management Firmware
```c
void energy_management() {
    measure_battery_voltage();
    
    if (battery_SOC > 80%) {
        brightness = 100%;
        enable_complex_animations();
    }
    else if (battery_SOC > 50%) {
        brightness = 70%;
    }
    else if (battery_SOC > 20%) {
        brightness = 40%;
        simple_animations_only();
    }
    else {
        emergency_mode();  // Minimal consumption
    }
}
```

**Sleep Mode Implementation:**
- Enter sleep between tasks
- Wake on interrupt (timer, button, sensor)
- Minimize active time
- Batch data transmissions

# Testing and Validation

## Power Consumption Measurements
- Series multimeter for average current
- Oscilloscope for instantaneous current and peaks
- Power profiler tools (Nordic, STM32)
- Long-term data logging

## Autonomy Testing
- Full battery → measure time to threshold
- Solar charge time measurement
- Charge/discharge cycles validation
- Performance across temperature range

<div style="display: flex; justify-content: center; gap: 15px; margin: 30px 0; flex-wrap: wrap;">
  <img src="/img/BE_Energy_Connected_Object/dist_2_4.png" alt="Distance Test 2.4 GHz" style="width: 45%;" onclick="openModal(this.src)"/>
  <img src="/img/BE_Energy_Connected_Object/dist_8_6.png" alt="Distance Test 8.6 GHz" style="width: 45%;" onclick="openModal(this.src)"/>
</div>

## Efficiency Measurements
- DC-DC converter efficiency (Pin/Pout)
- MPPT effectiveness
- Overall system efficiency
- Comparison with specifications

# Results and Analysis

Successfully achieved target autonomy with optimized power management. Solar charging provided sufficient energy for continuous operation under normal sunlight conditions. Low-power modes reduced standby consumption by 95%, significantly extending battery life.

Key findings:
- Proper sleep mode usage critical for autonomy
- Switching converters far superior to linear regulators
- Solar panel orientation significantly affects charging
- Battery capacity sizing must include safety margin

# Conclusion
This project provided comprehensive experience in autonomous system design with renewable energy integration. We successfully balanced performance requirements with power consumption constraints, demonstrating effective energy management strategies. The working prototype validates our ability to design sustainable, battery-powered electronic systems for real-world deployment.

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

## PART B: EXPÉRIENCE, CONTEXTE ET FONCTION (Exemples projets)

### Systèmes autonomes

**Cube LED 8×8×8 autonome :**
- 512 LEDs RGB (WS2812B)
- Contrôle STM32
- Batterie Li-Ion 18650 (3.7V, 3000 mAh)
- Charge solaire (panneau 5W)
- Autonomie : 2-4h utilisation, charge jour
- Animations programmées

**Lampe solaire intelligente :**
- LEDs haute puissance (10W)
- Détecteur présence (PIR)
- Panneau PV 20W
- Batterie LiFePO4 12V 10Ah
- Contrôle MPPT Arduino
- Autonomie : 3 nuits

### Systèmes IoT autonomes

**Station météo ultra-basse conso :**
- Capteurs T°/P/humidité
- MCU low-power (STM32L0, ESP32 deep-sleep)
- LoRa transmission (quelques Ko/jour)
- Panneau PV 1W
- Supercapacité ou petite batterie
- Autonomie : illimitée (si soleil)

**Tracker GPS solaire :**
- GPS (NEO-6M)
- Accéléromètre (détection mouvement)
- Transmission GSM/LoRa
- Charge solaire
- Optimisation : envoi position si mouvement uniquement

---

## PART C: ASPECTS TECHNIQUES (Réalisation)

### Phase 1 : Bilan énergétique (10h)

**Consommation système :**
- Calcul courant moyen chaque bloc
- Exemple cube LED :
  * STM32 actif : 50 mA
  * 512 LEDs max luminosité : 30 A (impossible !)
  * 512 LEDs faible : 500 mA
  * Autonomie : 3000 mAh / 500 mA = 6h

**Dimensionnement batterie :**
- Capacité nécessaire (mAh)
- Tension (Li-Ion 3.7V, LiFePO4 3.2V, Plomb 12V)
- Chimie selon application

**Dimensionnement PV :**
- Puissance panneau : P = E_jour / (Ensoleillement × η)
- Exemple : 10 Wh/jour, 4h soleil, η=80% → P = 3W

### Phase 2 : Conception (20h)

**Alimentation :**
- **Charge batterie** : 
  * Li-Ion : TP4056, MCP73831 (linéaire <1A)
  * Ou BQ24074 (switching, MPPT)
  * Protection : surcharge, décharge profonde
- **Convertisseurs DC-DC** :
  * Buck : batterie → 3.3V/5V (efficacité 85-95%)
  * Boost : batterie → 12V si nécessaire
  * Ex: TPS54302 (Buck, 3A), MT3608 (Boost)

**Gestion énergie MCU :**
- Modes low-power (Sleep, Stop, Standby)
- Réveil périodique (RTC)
- Désactivation périphériques inutiles

**Schéma électrique :**
- Panneau PV → Charge controller → Batterie → DC-DC → Charge (MCU, LEDs, etc.)
- Mesure tension batterie (ADC)
- Indicateurs LED (charge, batterie faible)

### Phase 3 : Réalisation (15h)

**PCB :**
- Layout optimisé (convertisseurs : boucles courtes, GND plan)
- Dissipation thermique (inductances, régulateurs)
- Connecteurs : batterie (JST), PV, charge

**Boîtier :**
- Protection éléments (batterie, électronique)
- Accès panneau solaire (orientation soleil)
- Fixation

### Phase 4 : Optimisation et tests (15h)

**Mesures consommation :**
- Multimètre en série (courant moyen)
- Oscilloscope (courant instantané + pics)
- Power profiler (Nordic, STM32)

**Optimisation firmware :**
- Réduction fréquence CPU
- Utilisation timers low-power
- Transmission données groupée (vs continue)

**Tests autonomie :**
- Batterie pleine → mesure durée jusqu'à seuil bas
- Test charge solaire : temps charge complète
- Cycles charge/décharge (fiabilité)

**Validation performances :**
- Autonomie vs spécifications
- Rendement convertisseurs (mesure)
- Efficacité MPPT (si implémenté)

---

## PART D: ANALYSE ET RÉFLEXION

### Livrables
- Rapport (35 pages) : bilan énergétique, conception, optimisation, tests
- Schémas et PCB
- Code source (gestion low-power)
- Mesures autonomie (courbes, tableaux)
- Présentation + démonstration

### Évaluation
- Bilan énergétique et dimensionnement (20%)
- Conception alimentation (20%)
- Réalisation (20%)
- Optimisation consommation (20%)
- Tests et validation (15%)
- Rapport et présentation (5%)

### Compétences acquises
- Dimensionnement systèmes autonomes
- Conception alimentations efficaces
- Intégration solaire/batterie
- Optimisation consommation embarquée
- Mesures énergétiques

### Débouchés
- Ingénieur énergie embarquée
- Conception IoT basse consommation
- Systèmes autonomes (solaire, batteries)
- Smart grids, véhicules électriques

## 📚 Types de projets possibles

### Systèmes autonomes

**Cube LED autonome :**
- Matrice LED 3D (8×8×8)
- Contrôle par microcontrôleur
- Alimentation sur batterie Li-ion
- Charge solaire (photovoltaïque)
- Gestion intelligente de l'énergie
- Animations et effets lumineux
- Autonomie optimisée

**Station connectée autonome :**
- Capteurs environnementaux
- Transmission LoRa/Sigfox
- Panneau solaire
- Batterie + supercondensateurs
- Sleep modes avancés
- Wake-up intelligent

### Convertisseurs de puissance

**Alimentation multiple sorties :**
- Entrée 12V (batterie auto)
- Sorties : 5V/3A, 3.3V/2A, 12V/1A, ±15V/500mA
- Topologies Buck, Boost, Inverting
- Protections (OVP, OCP, OTP)
- Efficacité >85%
- Ondulation <50mV

**Chargeur universel :**
- Entrée AC (230V) ou DC (12V)
- Multi-chimies : Li-ion, NiMH, Pb
- Détection automatique
- Phases CC/CV
- Surveillance T°, V, I
- Interface utilisateur (LCD)
- Sécurités complètes

### Systèmes de récupération d'énergie

**Energy harvesting :**
- Photovoltaïque (solaire)
- Piézoélectrique (vibrations)
- Thermoélectrique (différence T°)
- Stockage tampon
- MPPT (Maximum Power Point Tracking)
- Alimentation de capteur WSN

### Gestion de batterie

**BMS (Battery Management System) :**
- Équilibrage cellules Li-ion
- Mesure V, I, T° précise
- État de charge (SOC) et santé (SOH)
- Protections (sur/sous-tension, sur-intensité)
- Communication (CAN, I2C)
- Application véhicule électrique ou stockage

## 🛠️ Exemple détaillé : Cube LED Autonome

### Cahier des charges

#### Fonctionnalités
- Matrice LED 8×8×8 (512 LEDs)
- Animations programmables
- Contrôle par microcontrôleur (STM32)
- Alimentation batterie Li-ion
- Recharge par panneau solaire
- Autonomie > 4h en utilisation continue
- Modes économie d'énergie

#### Spécifications techniques

**Affichage :**
- 512 LEDs (8 plans de 64 LEDs)
- Multiplexage temporel
- Fréquence rafraîchissement >100 Hz
- Contrôle luminosité (PWM)
- Couleur : RGB ou monochrome

**Puissance :**
- Consommation max : 10W (toutes LEDs allumées)
- Consommation moyenne : 2-3W (animations)
- Consommation veille : <1mW

**Alimentation :**
- Batterie Li-ion 18650 (3.7V, 3000mAh)
- Panneau solaire 5V, 2W
- Convertisseur Buck-Boost 3.3V
- Charge intelligente (CC/CV)

### Conception système

#### Architecture électrique

**Blocs principaux :**

1. **Alimentation et gestion énergie :**
   - Panneau solaire → Régulateur MPPT
   - Chargeur Li-ion (TP4056 ou BQ24072)
   - Protection batterie (BMS)
   - Buck-Boost 3.3V (TPS63000 ou similaire)
   - Mesure V, I batterie (INA219)

2. **Contrôle et logique :**
   - Microcontrôleur STM32 (Low power)
   - Horloge RTC (DS3231)
   - Mémoire EEPROM (animations)
   - Interface utilisateur (boutons)

3. **Affichage LED :**
   - Drivers de colonnes (shift registers 74HC595)
   - Drivers de plans (MOSFET N)
   - LEDs avec résistances série
   - PWM pour luminosité

4. **Communication :**
   - Bluetooth LE (optionnel)
   - USB (programmation, debug)

#### Schémas électroniques

**Alimentation :**
```
Panneau solaire (5V, 2W)
    ↓
Régulateur MPPT (optionnel) ou diode Schottky
    ↓
Chargeur Li-ion (TP4056)
    ↓
Batterie Li-ion 18650 (3.7V, 3Ah)
    ↓
Protection (BMS intégré ou DW01)
    ↓
Buck-Boost 3.3V (efficace 85-95%)
    ↓
Microcontrôleur + LEDs
```

**Détection batterie :**
- Pont diviseur pour tension
- INA219 pour courant (I2C)
- Calcul SOC par coulombmétrie

**Chargeur Li-ion :**
- TP4056 : charge CC/CV, 1A max
- LED status (charge/terminé)
- Thermistance NTC pour sécurité
- Coupure fin de charge

**Convertisseur 3.3V :**
- TPS63000 (Buck-Boost)
- Efficace de 2.5V à 5.5V
- Sortie 3.3V/1A
- Enable pour power management

#### Contrôle des LEDs

**Multiplexage :**
- 8 plans activés séquentiellement
- Durée par plan : 125 µs (8 MHz)
- Fréquence refresh : 1 kHz
- Persistance rétinienne

**Drivers :**
- 3× 74HC595 pour 64 colonnes (8×8)
- 8× MOSFET pour plans
- Current limiting par résistances
- Calcul : R = (Vcc - Vled) / Iled

**PWM pour luminosité :**
- Timer STM32
- 256 niveaux (8 bits)
- Fréquence >200 Hz (anti-flicker)

### Logiciel embarqué

#### Architecture logicielle

**Tasks principales :**

1. **Display task :**
   - Rafraîchissement multiplexé
   - Haute priorité (temps réel)
   - DMA si possible pour shift registers

2. **Animation task :**
   - Calcul de la frame suivante
   - Buffer double (affichage/calcul)
   - Animations diverses (pluie, ondes, texte, etc.)

3. **Power management task :**
   - Mesure V, I batterie
   - Calcul SOC
   - Décisions économie énergie
   - Ajustement luminosité

4. **User interface task :**
   - Lecture boutons
   - Changement mode/animation
   - Affichage infos (batterie)

5. **Charge management task :**
   - Surveillance charge
   - Activation/désactivation panneau
   - Logs et statistiques

#### Optimisation énergétique

**MCU :**
- Sleep modes entre tâches
- Clock scaling (réduire fréquence)
- Périphériques désactivés si inutilisés
- DMA pour réduire CPU load

**LEDs :**
- Réduction luminosité selon batterie
- Mode veille (quelques LEDs)
- Extinction auto après timeout
- Détecteur mouvement (optionnel)

**Gestion adaptative :**
```c
if (SOC > 80%) {
    luminosité = 100%;
    animations_complexes = ON;
} else if (SOC > 50%) {
    luminosité = 70%;
} else if (SOC > 20%) {
    luminosité = 40%;
    animations_simples_only = ON;
} else {
    mode_économie_extrême();
}
```

### Réalisation pratique

#### PCB

**Structure :**
- PCB principal (contrôle + alimentation)
- 8× PCB plans de LEDs (empilés)
- Connecteurs inter-plans
- Dimensions : 10×10 cm par plan

**Contraintes :**
- Courants élevés pour LEDs (routing large)
- Dissipation thermique
- Accessibilité pour assemblage

#### Mécanique

**Structure 3D :**
- Impression 3D ou découpe laser acrylique
- Entretoises entre plans
- Diffuseurs LED (optionnel)
- Boîtier base (batterie, électronique)
- Fixation panneau solaire

**Matériaux :**
- Acrylique transparent/translucide
- PLA/ABS pour support
- Vis M3, entretoises

#### Assemblage

1. Soudure des LEDs sur 8 PCB plans
2. Test individuel de chaque plan
3. Assemblage mécanique (entretoises)
4. Câblage inter-plans
5. Connexion au PCB de contrôle
6. Test ensemble
7. Intégration batterie et panneau
8. Finitions et boîtier

### Tests et validation

#### Tests fonctionnels

**Affichage :**
- Test de toutes les LEDs
- Uniformité luminosité
- Fréquence de rafraîchissement
- Absence de flicker

**Alimentation :**
- Tensions de sortie
- Ondulation (ripple)
- Efficacité convertisseur
- Charge batterie (profil CC/CV)

#### Tests énergétiques

**Consommations mesurées :**
- Idle : < 10 mA
- Animation simple : 200-400 mA
- Animation complexe : 500-800 mA
- Toutes LEDs max : ~3A

**Autonomie :**
- Test décharge contrôlée
- Mesure temps vs SOC
- Validation >4h objectif

**Charge solaire :**
- Test avec lampe (simulation soleil)
- Mesure courant de charge
- Temps de charge complète
- Efficacité MPPT

**Efficacité globale :**
$$\eta = \frac{P_{utile}}{P_{batterie}} \times 100\%$$

Objectif : >80%

### Optimisations possibles

#### Hardware
- MPPT dédié (meilleur rendement)
- Supercondensateurs (peaks de courant)
- Drivers de LEDs constants current (mieux que résistances)
- MCU ultra-low power (STM32L4)

#### Software
- Algorithmes d'animation optimisés
- Apprentissage machine (prédiction usage)
- Calendrier intelligent (plus lumineux le soir)
- Communication Bluetooth (contrôle smartphone)

#### Mécanique
- Diffuseurs optimisés
- Refroidissement passif
- Design compact

## 💻 Outils utilisés

### Simulation
- **LTspice** : Convertisseurs de puissance
- **PLECS** : Simulation puissance avancée
- **MATLAB** : Modélisation système

### Conception
- **Altium/KiCad** : Schémas et PCB
- **Fusion 360** : Mécanique 3D
- **Cura** : Slicing impression 3D

### Programmation
- **STM32CubeIDE** : Développement STM32
- **Platformio** : Alternative VS Code

### Mesure
- **Oscilloscope** : Formes d'ondes
- **Multimètre** : V, I
- **Wattmètre** : Puissance
- **Thermomètre infrarouge** : Températures
- **Luxmètre** : Intensité lumineuse

## 📊 Livrables

### Documentation
- Cahier des charges
- Schémas électriques annotés
- PCB et fichiers Gerber
- Nomenclature (BOM)
- Modèles 3D (structure)
- Code source commenté
- Guide d'assemblage
- Procédures de test
- Caractérisations énergétiques
- Rapport technique complet

### Réalisations
- Prototype fonctionnel
- Démonstrations animations
- Mesures de performances
- Vidéo de fonctionnement

### Présentation
- Soutenance avec démo live
- Poster technique
- Documentation utilisateur

## 🔗 Liens avec les cours

- **Énergie (S3)** : Convertisseurs, batteries
- **IE** : Programmation low power
- **ER** : Conception PCB
- **Automatique** : Régulation (MPPT)

## 📖 Compétences développées

- Conception d'alimentations à découpage
- Gestion intelligente de l'énergie
- Optimisation low power
- Mesures énergétiques
- Intégration sources renouvelables
- Gestion de batteries
- Multiplexage et drivers de charge
- Programmation temps réel
- Design mécatronique

## 💡 Autres projets énergie possibles

### Micro-onduleur solaire
- MPPT
- DC/AC conversion
- Injection réseau (simulation)
- Monitoring

### Powerbank intelligent
- Charge rapide (Quick Charge, PD)
- Multi-sorties
- Affichage OLED
- Wireless charging

### Système hybride
- Panneau solaire + éolienne
- Stockage batterie
- Gestion priorités
- Alimentation charge critique

## ⚠️ Précautions

### Sécurité électrique
- Protection court-circuit batteries
- Fusibles et diodes de protection
- Respect polarités
- Chaleur et refroidissement

### Batteries Li-ion
- Ne jamais dépasser 4.2V
- Ne pas décharger sous 2.7V
- Surveillance température
- Protection BMS obligatoire
- Éviter court-circuits (risque incendie)

### LEDs et courants
- Courants élevés (câblage adapté)
- Dissipation thermique
- Current limiting (résistances)
- Protection yeux (luminosité élevée)

## 🎯 Critères d'évaluation

- Conception énergétique (25%)
- Efficacité et autonomie (25%)
- Réalisation pratique (20%)
- Tests et mesures (15%)
- Documentation (10%)
- Innovation et optimisation (5%)

## 📚 Ressources

- Texas Instruments Power Management Design Tools
- Application notes fabricants (TI, Analog Devices, ST)
- "Power Electronics" - Mohan, Undeland
- Forums électronique (EEVblog, etc.)
- YouTube (GreatScott!, ElectroBOOM, etc.)

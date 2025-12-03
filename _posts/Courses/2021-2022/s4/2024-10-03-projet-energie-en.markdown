---
layout: default
title: "Projet Tuteuté : Énergie (EN) - S4"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

# Projet Tuteuté : Énergie (EN) - Semestre 4

---

## PART A - Présentation Générale du Cours

### Contexte et objectifs

Projet énergie spécialisation EN : système autonome avec gestion énergie (solaire, batterie, optimisation conso). Cube LED, station IoT autonome, etc. Binome, 60h.

**Objectifs :**
- Concevoir alimentations efficaces (DC-DC, charge batterie)
- Intégrer sources renouvelables (PV, éolien)
- Gérer batterie (Li-Ion, BMS)
- Optimiser consommation système
- Mesurer autonomie et performances

### Prérequis
- Énergie S3 (convertisseurs, PV)
- Électronique de puissance
- MCU (low-power modes)

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

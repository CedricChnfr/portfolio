---
layout: default
title: "Microcontrôleur - S6"
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

# 🔌 Microcontrôleur - Semestre 6

**Année Universitaire** : 2022-2023  
**Semestre** : 6  
**Crédits** : 4 ECTS  
**Spécialité** : Systèmes Embarqués

---

## PART A - Présentation Générale du Cours

<h3 class="section-title">Vue d'ensemble</h3>

Ce cours approfondit la programmation de microcontrôleurs avec focus sur les STM32 (ARM Cortex-M3). Il couvre la configuration des périphériques (GPIO, timers, ADC, UART), le développement de drivers, et la gestion des interruptions. Le point culminant est le projet Voilier, un système embarqué autonome intégrant capteurs et actionneurs.

**Objectifs pédagogiques** :
- Maîtriser la programmation en C embarqué pour STM32
- Configurer les périphériques via registres (GPIO, timers, ADC, UART)
- Développer des drivers réutilisables avec HAL (Hardware Abstraction Layer)
- Gérer les interruptions et le temps réel
- Concevoir un système embarqué complet (projet Voilier)

<h3 class="section-title">Position dans le cursus</h3>

Ce cours s'appuie sur :
- **Langage C (S5)** : bases de la programmation C
- **Architecture Informatique (S5)** : fonctionnement processeur et mémoire
- **Langage Assemblage ARM (S6)** : compréhension bas niveau

Il prépare aux applications :
- **Systèmes embarqués temps réel** : contraintes temporelles
- **IoT et objets connectés** : capteurs, communication
- **Robotique et automatisation** : contrôle moteurs, asservissement

---

## PART B - Expérience Personnelle et Contexte d'Apprentissage

<h3 class="section-title">Organisation et ressources</h3>

Le module était structuré en deux parties complémentaires :

**1. Cours et TDs** :
- Architecture STM32F103 (Cortex-M3, 72 MHz, 128 KB Flash, 20 KB RAM)
- Programmation des périphériques via registres
- Développement de drivers
- Gestion des interruptions et timers

**2. Projet Voilier** :
Conception d'un voilier autonome radiocommandé avec :
- Capteurs : girouette (anémomètre), boussole, GPS
- Actionneurs : servo-moteurs (gouvernail, voile)
- Communication : liaison série, télémétrie
- Contrôle : régulation automatique de cap

**Environnement de développement** :
- **IDE** : Keil µVision
- **Carte** : STM32F103RB (Nucleo-64 ou carte custom)
- **Programmation** : ST-Link (SWD)
- **Débogage** : breakpoints, watch, mémoire

<h3 class="section-title">Déroulement du projet Voilier</h3>

**Architecture du système** :

Le voilier autonome intègre plusieurs sous-systèmes :

| Sous-système | Composants | Fonction |
|--------------|------------|----------|
| Navigation | Girouette, boussole, GPS | Déterminer position et orientation |
| Contrôle | Servo-moteurs | Ajuster gouvernail et voile |
| Communication | UART, radio | Télémétrie et commandes |
| Alimentation | Batterie, régulateur | Autonomie énergétique |

**Capteurs implémentés** :

**Girouette (anémomètre)** :
- Mesure de la direction du vent
- Interface : potentiomètre rotatif → ADC
- Résolution : 12 bits (0-4095) → 0-360°
- Calibration nécessaire

**Boussole électronique** :
- Mesure du cap (orientation)
- Interface : I2C ou SPI
- Données : azimut magnétique

**Étapes de développement** :

**Étape 1 : Drivers de base**

Développement de drivers modulaires pour chaque périphérique.

**Driver GPIO** :

```c
typedef struct {
    GPIO_TypeDef * GPIO;      // Port (GPIOA, GPIOB, GPIOC...)
    char GPIO_Pin;            // Numéro broche 0-15
    char GPIO_Conf;           // Configuration
} MyGPIO_Struct_TypeDef;

// Modes de configuration
#define In_Floating  0x4
#define In_PullUp    0x8
#define In_PullDown  0x8
#define Out_Ppull    0x2      // Push-pull
#define Out_OD       0x6      // Open-drain
#define AltOut_Ppull 0xA      // Fonction alternative

// Initialisation GPIO
void MyGPIO_Init(MyGPIO_Struct_TypeDef * GPIOStructPtr) {
    // Activation horloge du port
    if (GPIOStructPtr->GPIO == GPIOA) {
        RCC->APB2ENR |= RCC_APB2ENR_IOPAEN;
    }
    
    // Configuration de la broche
    if(GPIOStructPtr->GPIO_Pin <= 7) {
        GPIOStructPtr->GPIO->CRL &= ~(0xF << (4*GPIOStructPtr->GPIO_Pin));
        GPIOStructPtr->GPIO->CRL |= (GPIOStructPtr->GPIO_Conf << (4*GPIOStructPtr->GPIO_Pin));
    }
    else {
        GPIOStructPtr->GPIO->CRH &= ~(0xF << (4*(GPIOStructPtr->GPIO_Pin % 8)));
        GPIOStructPtr->GPIO->CRH |= (GPIOStructPtr->GPIO_Conf << (4*(GPIOStructPtr->GPIO_Pin % 8)));
    }
}

// Lecture d'une entrée
int MyGPIO_Read(GPIO_TypeDef * GPIO, char GPIO_Pin) {
    return (GPIO->IDR & (1 << GPIO_Pin)) != 0 ? 1 : 0;
}

// Mise à 1
void MyGPIO_Set(GPIO_TypeDef * GPIO, char GPIO_Pin) {
    GPIO->BSRR = (1 << GPIO_Pin);
}

// Mise à 0
void MyGPIO_Reset(GPIO_TypeDef * GPIO, char GPIO_Pin) {
    GPIO->BRR = (1 << GPIO_Pin);
}

// Basculement
void MyGPIO_Toggle(GPIO_TypeDef * GPIO, char GPIO_Pin) {
    GPIO->ODR ^= (1 << GPIO_Pin);
}
```

**Étape 2 : Timers et PWM**

Configuration des timers pour génération PWM (contrôle servo-moteurs).

```c
// Initialisation Timer en mode PWM
void MyTimer_PWM_Init(TIM_TypeDef * Timer, int frequence) {
    // Activation horloge timer
    if (Timer == TIM2) {
        RCC->APB1ENR |= RCC_APB1ENR_TIM2EN;
    }
    
    // Configuration prescaler et période
    Timer->PSC = 72 - 1;              // Prescaler (72 MHz / 72 = 1 MHz)
    Timer->ARR = 20000 - 1;           // Période 20 ms (50 Hz pour servo)
    
    // Mode PWM sur canal 1
    Timer->CCMR1 |= TIM_CCMR1_OC1M_1 | TIM_CCMR1_OC1M_2;  // PWM mode 1
    Timer->CCMR1 |= TIM_CCMR1_OC1PE;  // Preload enable
    
    // Activation sortie
    Timer->CCER |= TIM_CCER_CC1E;
    
    // Démarrage timer
    Timer->CR1 |= TIM_CR1_CEN;
}

// Réglage rapport cyclique (duty cycle)
void MyTimer_SetDutyCycle(TIM_TypeDef * Timer, int channel, int duty) {
    if (channel == 1) {
        Timer->CCR1 = duty;  // Valeur de 1000 à 2000 µs pour servo
    }
}
```

**Commande de servo-moteur** :
- Position neutre : 1500 µs
- Gauche max : 1000 µs
- Droite max : 2000 µs

**Étape 3 : ADC pour girouette**

Lecture analogique de la position de la girouette.

```c
// Initialisation ADC
void MyADC_Init(ADC_TypeDef * ADC, char channel) {
    // Activation horloge ADC
    RCC->APB2ENR |= RCC_APB2ENR_ADC1EN;
    
    // Configuration ADC
    ADC->CR2 |= ADC_CR2_ADON;         // Activation ADC
    ADC->SQR3 = channel;              // Sélection canal
    ADC->SMPR2 = 0x7 << (3*channel);  // Temps échantillonnage 239,5 cycles
}

// Lecture ADC (bloquante)
int MyADC_Read(ADC_TypeDef * ADC) {
    ADC->CR2 |= ADC_CR2_ADON;         // Démarrage conversion
    while (!(ADC->SR & ADC_SR_EOC));  // Attente fin conversion
    return ADC->DR;                   // Lecture résultat
}

// Conversion ADC → angle
int Girouette_GetAngle(void) {
    int raw = MyADC_Read(ADC1);
    return (raw * 360) / 4096;  // 12 bits → 0-360°
}
```

**Étape 4 : UART pour télémétrie**

Communication série pour envoyer données et recevoir commandes.

```c
// Initialisation UART
void MyUART_Init(USART_TypeDef * UART, int baudrate) {
    // Activation horloge
    if (UART == USART1) {
        RCC->APB2ENR |= RCC_APB2ENR_USART1EN;
    }
    
    // Configuration GPIO (TX/RX)
    // PA9 = TX (fonction alternative), PA10 = RX (input)
    
    // Configuration baudrate
    UART->BRR = 72000000 / baudrate;  // 72 MHz / 9600 bps
    
    // Activation TX et RX
    UART->CR1 |= USART_CR1_TE | USART_CR1_RE | USART_CR1_UE;
}

// Envoi d'un caractère
void MyUART_SendChar(USART_TypeDef * UART, char c) {
    while (!(UART->SR & USART_SR_TXE));  // Attente buffer vide
    UART->DR = c;
}

// Réception d'un caractère
char MyUART_ReceiveChar(USART_TypeDef * UART) {
    while (!(UART->SR & USART_SR_RXNE));  // Attente données disponibles
    return UART->DR;
}

// Envoi d'une chaîne
void MyUART_SendString(USART_TypeDef * UART, char * str) {
    while (*str) {
        MyUART_SendChar(UART, *str++);
    }
}
```

**Étape 5 : Régulation de cap**

Algorithme de contrôle pour maintenir un cap.

```c
// Structure de contrôle
typedef struct {
    int cap_consigne;      // Cap désiré
    int cap_actuel;        // Cap mesuré (boussole)
    int angle_vent;        // Direction du vent (girouette)
    int position_gouvernail;
    int position_voile;
} VoilierControl_TypeDef;

// Régulation simple (proportionnelle)
void Voilier_Regulate(VoilierControl_TypeDef * voilier) {
    // Calcul erreur de cap
    int erreur = voilier->cap_consigne - voilier->cap_actuel;
    
    // Normalisation erreur (-180° à +180°)
    if (erreur > 180) erreur -= 360;
    if (erreur < -180) erreur += 360;
    
    // Correction proportionnelle
    int correction = erreur * 5;  // Gain proportionnel
    
    // Limites
    if (correction > 500) correction = 500;
    if (correction < -500) correction = -500;
    
    // Application au gouvernail
    voilier->position_gouvernail = 1500 + correction;
    MyTimer_SetDutyCycle(TIM2, 1, voilier->position_gouvernail);
    
    // Ajustement voile selon vent
    int angle_voile = abs(voilier->angle_vent - voilier->cap_actuel);
    if (angle_voile > 180) angle_voile = 360 - angle_voile;
    voilier->position_voile = 1000 + (angle_voile * 1000) / 180;
    MyTimer_SetDutyCycle(TIM3, 1, voilier->position_voile);
}
```

**Étape 6 : Interruptions**

Gestion d'événements asynchrones (réception UART, timers).

```c
// Configuration interruption UART
void MyUART_EnableIT(USART_TypeDef * UART) {
    UART->CR1 |= USART_CR1_RXNEIE;  // Interruption réception
    NVIC_EnableIRQ(USART1_IRQn);
    NVIC_SetPriority(USART1_IRQn, 1);
}

// Handler interruption UART
void USART1_IRQHandler(void) {
    if (USART1->SR & USART_SR_RXNE) {
        char received = USART1->DR;
        // Traitement commande
        if (received == 'L') {
            // Virer à gauche
        } else if (received == 'R') {
            // Virer à droite
        }
    }
}

// Configuration interruption timer
void MyTimer_EnableIT(TIM_TypeDef * Timer, int periode_ms) {
    Timer->DIER |= TIM_DIER_UIE;  // Interruption update
    NVIC_EnableIRQ(TIM2_IRQn);
}

// Handler interruption timer (tâche périodique)
void TIM2_IRQHandler(void) {
    if (TIM2->SR & TIM_SR_UIF) {
        TIM2->SR &= ~TIM_SR_UIF;  // Clear flag
        
        // Tâche périodique (ex: lecture capteurs, régulation)
        Voilier_Regulate(&voilier);
    }
}
```

<h3 class="section-title">Difficultés rencontrées</h3>

**Configuration des registres** :
Les datasheets STM32 sont volumineuses (>1000 pages). Il faut comprendre chaque bit des registres de configuration. Erreur fréquente : oublier d'activer l'horloge du périphérique (RCC).

**Timing et interruptions** :
Conflits entre tâches : une interruption trop longue bloque les autres. Nécessité de priorités bien réglées et de handlers courts.

**Calibration des capteurs** :
La girouette nécessite une calibration (offset, linéarité). La boussole doit être compensée en perturbations magnétiques.

**Débogage matériel** :
Problèmes parfois difficiles à diagnostiquer : câblage, alimentation, interférences. Oscilloscope et analyseur logique indispensables.

---

## PART C - Aspects Techniques Détaillés

<h3 class="section-title">1. Architecture STM32F103</h3>

**Caractéristiques principales** :

| Composant | Spécification |
|-----------|---------------|
| CPU | ARM Cortex-M3, 32 bits, 72 MHz |
| Flash | 128 KB (programme) |
| RAM | 20 KB (données) |
| GPIO | 51 broches I/O |
| Timers | 4 timers 16 bits avancés |
| ADC | 2 ADC 12 bits, 16 canaux |
| Communication | 3 USART, 2 SPI, 2 I2C, USB, CAN |

**Organisation mémoire** :

| Zone | Adresses | Usage |
|------|----------|-------|
| Flash | 0x08000000 - 0x0801FFFF | Code programme |
| SRAM | 0x20000000 - 0x20004FFF | Variables, pile |
| Périphériques | 0x40000000 - 0x5FFFFFFF | Registres memory-mapped |
| Système | 0xE0000000 - 0xE00FFFFF | NVIC, SysTick |

<h3 class="section-title">2. GPIO (General Purpose Input/Output)</h3>

**Registres GPIO** :

Chaque port (A, B, C, D) dispose de registres de configuration et de contrôle.

| Registre | Fonction |
|----------|----------|
| GPIOx_CRL | Configuration broches 0-7 (4 bits par broche) |
| GPIOx_CRH | Configuration broches 8-15 |
| GPIOx_IDR | Input Data Register (lecture) |
| GPIOx_ODR | Output Data Register (écriture) |
| GPIOx_BSRR | Bit Set/Reset Register (atomique) |
| GPIOx_BRR | Bit Reset Register |

**Configuration d'une broche** :

Chaque broche nécessite 4 bits de configuration : MODE (2 bits) + CNF (2 bits).

| MODE | CNF | Configuration |
|------|-----|---------------|
| 00 | 01 | Input floating |
| 00 | 10 | Input pull-down/up |
| 01 | 00 | Output push-pull 10 MHz |
| 10 | 00 | Output push-pull 2 MHz |
| 11 | 00 | Output push-pull 50 MHz |
| 11 | 10 | Alternate function push-pull |

<h3 class="section-title">3. Timers</h3>

**Modes de fonctionnement** :

Les timers STM32 sont polyvalents :

**Mode compteur simple** :
- Compte de 0 à ARR (Auto-Reload Register)
- Génère interruption à débordement
- Utilisé pour délais, tâches périodiques

**Mode PWM** :
- Compare compteur (CNT) avec valeur de comparaison (CCR)
- Sortie HIGH si CNT < CCR, LOW sinon
- Rapport cyclique = CCR / ARR

**Mode capture** :
- Capture valeur CNT sur événement externe
- Mesure de fréquence, durée d'impulsion

**Registres principaux** :

| Registre | Fonction |
|----------|----------|
| TIMx_CR1 | Control Register (activation, mode comptage) |
| TIMx_PSC | Prescaler (diviseur fréquence) |
| TIMx_ARR | Auto-Reload (période) |
| TIMx_CNT | Compteur actuel |
| TIMx_CCR1-4 | Capture/Compare (PWM duty cycle) |
| TIMx_CCMR1-2 | Configuration canaux (PWM mode) |
| TIMx_CCER | Activation sorties |

**Calcul de fréquence PWM** :

Fréquence PWM = Horloge / (PSC + 1) / (ARR + 1)

Exemple : 72 MHz / 72 / 20000 = 50 Hz (servo-moteur)

<h3 class="section-title">4. ADC (Convertisseur Analogique-Numérique)</h3>

**Caractéristiques ADC STM32** :
- Résolution : 12 bits (0-4095)
- Temps de conversion : quelques µs
- Modes : simple, continu, scan (multicanaux)
- Déclenchement : logiciel, timer, externe

**Configuration** :

```c
// Séquence de conversion
ADC1->SQR1 = (nombre_conversions - 1) << 20;  // Longueur séquence
ADC1->SQR3 = canal;                            // Premier canal

// Temps d'échantillonnage
ADC1->SMPR2 = 0x7 << (3 * canal);  // 239,5 cycles (max précision)

// Démarrage conversion
ADC1->CR2 |= ADC_CR2_ADON;  // Activation + start
```

**Modes d'acquisition** :

| Mode | Description |
|------|-------------|
| Simple | Une conversion sur commande |
| Continu | Conversions en boucle |
| Scan | Plusieurs canaux en séquence |
| Discontinu | Sous-groupes de canaux |

<h3 class="section-title">5. UART/USART</h3>

**Paramètres de communication** :

| Paramètre | Valeur typique |
|-----------|----------------|
| Baudrate | 9600, 115200 bps |
| Bits de données | 8 bits |
| Bit de parité | Aucun |
| Bits de stop | 1 bit |

**Calcul du registre BRR** :

BRR = Horloge_périphérique / Baudrate

Exemple : 72 MHz / 115200 = 625

**Gestion du buffer** :

Pour éviter la perte de données, utiliser :
- Buffer circulaire logiciel
- Interruptions sur réception
- Contrôle de flux matériel (RTS/CTS)

<h3 class="section-title">6. Interruptions (NVIC)</h3>

**Nested Vectored Interrupt Controller** :

Le NVIC gère jusqu'à 68 interruptions avec 16 niveaux de priorité.

**Configuration** :

```c
// Activation interruption
NVIC_EnableIRQ(USART1_IRQn);

// Priorité (0 = plus haute)
NVIC_SetPriority(USART1_IRQn, 2);

// Désactivation
NVIC_DisableIRQ(USART1_IRQn);
```

**Priorités** :

Plus le numéro est faible, plus la priorité est haute. Une interruption de priorité plus haute peut préempter une interruption en cours.

**Bonnes pratiques** :
- Handlers courts et rapides
- Pas de printf ou délais dans ISR
- Utiliser des flags pour communication avec main
- Protéger variables partagées (volatile)

<h3 class="section-title">7. Horloge et RCC</h3>

**Reset and Clock Control** :

Le RCC configure les horloges et active les périphériques.

**Sources d'horloge** :
- HSI : oscillateur interne 8 MHz (précision ±1%)
- HSE : quartz externe 8 MHz (précision ±50 ppm)
- PLL : multiplieur pour atteindre 72 MHz

**Configuration typique** :

HSE 8 MHz → PLL ×9 → SYSCLK 72 MHz

**Activation périphériques** :

Chaque périphérique doit être activé via RCC avant utilisation :

```c
RCC->APB2ENR |= RCC_APB2ENR_IOPAEN;    // GPIO A
RCC->APB2ENR |= RCC_APB2ENR_USART1EN;  // USART1
RCC->APB1ENR |= RCC_APB1ENR_TIM2EN;    // Timer 2
```

---

## PART D - Analyse Réflexive et Perspectives

<h3 class="section-title">Compétences acquises</h3>

**Programmation embarquée** :
Maîtrise de la programmation bas niveau en C, manipulation directe des registres, compréhension du fonctionnement matériel. Capacité à lire et interpréter des datasheets complexes.

**Développement de drivers** :
Conception de couches d'abstraction matérielle (HAL) réutilisables. Structure modulaire du code, séparation interface/implémentation.

**Intégration système** :
Le projet Voilier a développé la capacité à intégrer plusieurs sous-systèmes (capteurs, actionneurs, communication) dans une application cohérente et fonctionnelle.

**Débogage matériel/logiciel** :
Utilisation d'outils professionnels (oscilloscope, analyseur logique, debugger). Méthodologie de diagnostic des problèmes.

<h3 class="section-title">Points clés à retenir</h3>

**1. Toujours activer l'horloge** :
Erreur n°1 : oublier RCC->APBxENR. Le périphérique ne fonctionne pas sans son horloge.

**2. Configuration complète** :
GPIO, timers, ADC nécessitent une configuration précise de nombreux bits. Bien lire la datasheet.

**3. Volatile pour registres** :
Les registres matériels doivent être déclarés volatile pour éviter l'optimisation du compilateur.

**4. Interruptions = handlers courts** :
Traitement minimal dans ISR, report du travail dans la boucle principale via flags.

**5. Débogage méthodique** :
Commencer simple (LED blinking), ajouter progressivement la complexité. Tester chaque module séparément avant intégration.

<h3 class="section-title">Retour d'expérience projet Voilier</h3>

**Aspects positifs** :
- Projet concret et motivant (système réel)
- Liberté de conception et d'implémentation
- Travail en équipe avec répartition des tâches
- Application directe de tous les concepts du cours

**Défis techniques** :
- Calibration des capteurs (girouette non linéaire)
- Gestion du timing (régulation 50 Hz + télémétrie)
- Interférences électromagnétiques (moteurs → capteurs)
- Optimisation consommation (autonomie batterie)

**Leçons apprises** :
- Importance de la modularité (drivers réutilisables)
- Tests unitaires avant intégration globale
- Documentation du code (compréhension équipe)
- Version control (Git) pour travail collaboratif

<h3 class="section-title">Applications pratiques</h3>

**Domotique** :
Contrôle d'éclairage, chauffage, volets roulants. Communication sans fil (Zigbee, LoRa).

**Robotique** :
Contrôle de moteurs, lecture de capteurs (ultrason, infrarouge), navigation autonome.

**IoT (Internet of Things)** :
Objets connectés : thermostats, trackers, stations météo. Communication WiFi, Bluetooth.

**Automobile** :
ECU (Electronic Control Unit), capteurs ABS, airbags, injection moteur.

**Médical** :
Dispositifs portables (glucomètres, tensiomètres), pompes à perfusion, stimulateurs cardiaques.

<h3 class="section-title">Limites et ouvertures</h3>

**Limites du cours** :
- Peu de communication sans fil (WiFi, Bluetooth)
- Pas de RTOS (Real-Time Operating System)
- Peu de traitement du signal (filtrage, FFT)
- Pas de sécurité (chiffrement, authentification)

**Ouvertures vers** :
- **RTOS** : FreeRTOS, gestion multitâches, synchronisation
- **Communication IoT** : MQTT, CoAP, LoRaWAN
- **Traitement signal** : filtrage numérique, FFT sur MCU
- **Bas niveau avancé** : DMA, low power modes, bootloaders
- **Machine Learning** : TensorFlow Lite Micro pour MCU

<h3 class="section-title">Évolution technologique</h3>

**Tendances actuelles** :
- **MCU 32 bits omniprésents** : Cortex-M4, M7, RISC-V
- **Connectivité intégrée** : WiFi, BLE, LoRa sur puce
- **IA embarquée** : accélérateurs ML (Cortex-M55, NPU)
- **Sécurité renforcée** : TrustZone, secure boot, crypto matériel
- **Ultra-basse consommation** : nW pour IoT batterie 10 ans

**Outils modernes** :
- **STM32CubeMX** : génération automatique code initialisation
- **PlatformIO** : IDE multiplateforme (VS Code)
- **Mbed OS** : système d'exploitation pour ARM
- **Zephyr RTOS** : RTOS open-source pour IoT

<h3 class="section-title">Conclusion</h3>

Le cours Microcontrôleur est fondamental pour tout ingénieur en systèmes embarqués. La maîtrise de la programmation bas niveau et de l'interfaçage matériel est essentielle dans un monde où les objets connectés sont omniprésents.

Le projet Voilier est l'expérience marquante du semestre : conception complète d'un système autonome intégrant capteurs, actionneurs et contrôle temps réel. Les compétences acquises (drivers, interruptions, périphériques) sont directement transférables à l'industrie.

**Évolution des compétences** :
De la simple LED clignotante au voilier autonome, le parcours montre la progression : GPIO → timers → ADC → UART → intégration système complet. Chaque brique s'ajoute pour construire des systèmes de plus en plus complexes.

**Recommandations** :
- Pratiquer régulièrement (petits projets personnels)
- Lire les datasheets en profondeur (indispensable)
- Utiliser oscilloscope et analyseur logique (débogage)
- Développer des drivers réutilisables (portfolio)
- Participer à des compétitions (Coupe de Robotique, hackathons)

**Liens avec les autres cours** :
- [Langage Assemblage ARM - S6](./assemblage-arm-cortex.html) : compréhension bas niveau
- [Électronique Fonctions Numériques - S6](./electronique-fonctions-numeriques.html) : bus I2C/SPI
- [Architecture Matérielle - S6](./architecture-materielle.html) : pipeline, cache
- [Temps Réel - S8](./temps-reel.html) : RTOS, ordonnancement
- [Embedded IA for IoT - S9](./embedded-ia-iot.html) : ML embarqué

---

## 📚 Documents de Cours

Voici les supports de cours en PDF pour approfondir la programmation des microcontrôleurs STM32 :

<style>
        .pdf-container {
                margin: 40px 0;
                padding: 20px;
                background-color: #f9f9f9;
                border-radius: 8px;
        }
        .pdf-viewer {
                display: flex;
                flex-wrap: wrap;
                gap: 20px;
                margin-top: 20px;
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
                margin-top: 0;
                color: #2a7ae2;
                border-bottom: 2px solid #2a7ae2;
                padding-bottom: 10px;
        }
</style>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>🔧 STM32 - Structures et Registres</h4>
      <p>Guide complet des structures C pour l'accès aux registres du STM32, configuration et utilisation des périphériques.</p>
      <embed src="/cours-pdf/S6/Microcontroleur/stm32-structures.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S6/Microcontroleur/stm32-structures.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          📥 Télécharger le PDF
        </a>
      </p>
    </div>
    
    <div class="pdf-item">
      <h4>📌 GPIO - Entrées/Sorties</h4>
      <p>Configuration des GPIO, modes d'entrée/sortie, pull-up/pull-down et manipulation des broches avec pointeurs.</p>
      <embed src="/cours-pdf/S6/Microcontroleur/gpio.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S6/Microcontroleur/gpio.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          📥 Télécharger le PDF
        </a>
      </p>
    </div>
    
    <div class="pdf-item">
      <h4>⚡ Interruptions</h4>
      <p>Gestion des interruptions, NVIC, priorités, handlers et bonnes pratiques de programmation temps réel.</p>
      <embed src="/cours-pdf/S6/Microcontroleur/interruptions.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S6/Microcontroleur/interruptions.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          📥 Télécharger le PDF
        </a>
      </p>
    </div>
    
    <div class="pdf-item">
      <h4>⏱️ Timers</h4>
      <p>Configuration et utilisation des timers pour génération de délais, comptage d'événements et mesures temporelles.</p>
      <embed src="/cours-pdf/S6/Microcontroleur/timers.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S6/Microcontroleur/timers.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          📥 Télécharger le PDF
        </a>
      </p>
    </div>
    
    <div class="pdf-item">
      <h4>🌊 PWM - Modulation de Largeur d'Impulsion</h4>
      <p>Génération de signaux PWM pour commande de moteurs, LEDs et variation d'intensité avec les timers.</p>
      <embed src="/cours-pdf/S6/Microcontroleur/pwm.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S6/Microcontroleur/pwm.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          📥 Télécharger le PDF
        </a>
      </p>
    </div>
    
    <div class="pdf-item">
      <h4>📊 ADC - Convertisseur Analogique-Numérique</h4>
      <p>Configuration de l'ADC, acquisition de signaux analogiques, modes de déclenchement et utilisation avec DMA.</p>
      <embed src="/cours-pdf/S6/Microcontroleur/adc.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S6/Microcontroleur/adc.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          📥 Télécharger le PDF
        </a>
      </p>
    </div>
  </div>
</div>

---

*Cours enseigné en 2022-2023 à l'INSA Toulouse, Département Génie Électrique et Informatique.*

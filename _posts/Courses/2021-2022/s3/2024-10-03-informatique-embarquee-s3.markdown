---
layout: default
title: "Informatique Embarquée (IE) - S3"
date:   2024-10-02 10:56:03 +0200
---

<style>
.back-nav { margin-bottom: 20px; }
.back-nav a { text-decoration: none; color: #2a7ae2; font-weight: 600; }
.back-nav a:hover { text-decoration: underline; }
.section-title { color: #2a7ae2; border-bottom: 2px solid #2a7ae2; padding-bottom: 10px; margin-top: 30px; margin-bottom: 20px; }
</style>

<div class="back-nav">
  <a href="./my-courses-2021-2022.html">&larr; Retour a Mes Cours 2021-2022</a>
</div>

# Informatique Embarquée (IE) - Semestre 3

**Annee**: 2021-2022 | **Semestre**: 3 | **Type**: Informatique

---

## PART A - Présentation Générale du Cours

### Contexte et objectifs

Approfondissement de la programmation embarquée sur microcontrôleurs ARM Cortex-M (STM32) avec périphériques avancés (ADC, DMA, timers complexes) et introduction aux RTOS (FreeRTOS). Suite du cours S2.

**Objectifs :**
- Programmer périphériques avancés STM32 (DMA, ADC multi-canaux, PWM, communication)
- Utiliser FreeRTOS (tâches, sémaphores, queues)
- Optimiser performances et consommation
- Déboguer systèmes temps réel

### Prérequis
- Programmation C embarquée (S2)
- Architecture ARM Cortex-M de base
- Périphériques simples (GPIO, UART, timers)

---

## PART B: EXPÉRIENCE, CONTEXTE ET FONCTION

### Module 1 : Périphériques avancés STM32

**ADC multi-canaux avec DMA :**
- Configuration multi-channel scan mode
- DMA circular pour transfert automatique
- Moyennage et filtrage
- Déclenchement par timer

**Timers avancés :**
- PWM complementary (dead-time pour ponts H)
- Input Capture (mesure fréquence/duty cycle)
- Encoder mode (quadrature)
- One-pulse mode

**Communication avancée :**
- UART avec DMA (Tx/Rx non-bloquant)
- SPI multi-slaves (CS multiples)
- I2C multi-maîtres
- CAN bus (automotive)
- USB Device/Host

**Watchdog et sécurité :**
- IWDG (Independent Watchdog)
- WWDG (Window Watchdog)
- Brown-out reset
- CRC hardware

### Module 2 : FreeRTOS

**Concepts RTOS :**
- Scheduler préemptif
- Tâches (tasks) et priorités
- États : Running, Ready, Blocked, Suspended
- Tick (1 ms typique)

**Tâches :**
```c
void vTaskLED(void *pvParameters) {
  TickType_t xLastWakeTime = xTaskGetTickCount();
  while(1) {
    HAL_GPIO_TogglePin(LED_GPIO_Port, LED_Pin);
    vTaskDelayUntil(&xLastWakeTime, pdMS_TO_TICKS(500));
  }
}

xTaskCreate(vTaskLED, "LED", 128, NULL, 1, NULL);
```

**Synchronisation :**
- **Sémaphores** : binaire (mutex), counting
- **Mutex** : exclusion mutuelle (ressources partagées)
- **Queues** : communication inter-tâches (FIFO)
- **Event Groups** : synchronisation multiple

**Gestion mémoire :**
- Heap statique configurable
- Schémas allocation (heap_1 à heap_5)
- Stack overflow detection

### Module 3 : Low Power

**Modes STM32 :**
- Run : normal
- Sleep : CPU arrêté, périphériques actifs
- Stop : horloges arrêtées, RAM conservée
- Standby : tout arrêté, réveil externe

**Techniques économie énergie :**
- Clock gating (désactiver horloges inutiles)
- Périphériques en low-power
- Wake-up sources (RTC, GPIO, UART)
- Mesure consommation (µA en Standby)

---

## PART C: ASPECTS TECHNIQUES

### TP Périphériques avancés

**TP1 : Acquisition ADC multi-canaux DMA**
- 4 canaux ADC avec DMA circular
- Timer trigger à 1 kHz
- Affichage valeurs sur UART

**TP2 : Moteur brushless avec PWM**
- 3 PWM complémentaires (phases U, V, W)
- Dead-time 2 µs
- Contrôle vitesse potentiomètre

**TP3 : Communication CAN**
- Envoi/réception messages CAN
- Filtres CAN
- Application : tableau de bord automobile

### Projet FreeRTOS

**Système multi-tâches :**
- Tâche Acquisition : ADC DMA (priorité 3)
- Tâche Traitement : calculs (priorité 2)
- Tâche Communication : UART (priorité 2)
- Tâche Affichage : LCD (priorité 1)
- Synchronisation par queues et sémaphores

**Livrables :**
- Code FreeRTOS fonctionnel
- Analyse timing (durée tâches, CPU usage)
- Documentation architecture logicielle

---

## PART D: ANALYSE ET RÉFLEXION

### Évaluation
- TP et comptes-rendus (40%)
- Projet FreeRTOS (35%)
- Contrôles (15%)
- Examen pratique (10%)

### Compétences acquises
- Programmation STM32 avancée (HAL, LL drivers)
- Conception systèmes RTOS
- Optimisation temps réel et consommation
- Débogage embarqué (JTAG/SWD, printf semi-hosting)
- Outils professionnels (STM32CubeIDE, Keil)

### Applications métier
- Systèmes embarqués temps réel (automotive, IoT)
- Objets connectés (wearables, smart devices)
- Automatismes industriels
- Instrumentation médicale
- Interruptions et exceptions

#### STM32 (STM32L152 typiquement)
- Famille STM32 (F0, F1, F4, L1, L4, H7)
- Architecture interne
- Mémoires (Flash, RAM, EEPROM)
- Horloge et reset
- Modes basse consommation

### Périphériques avancés

#### Timers avancés
- Timers général purpose
- Timers avancés (TIM1, TIM8)
- PWM avancé (center-aligned, etc.)
- Input Capture
- Output Compare
- Encodeur en quadrature

#### Communication série
**UART/USART :**
- Configuration avancée
- DMA pour réception/émission
- Gestion de buffers circulaires
- Protocoles applicatifs

**SPI :**
- Mode master et slave
- Communication multi-devices
- DMA avec SPI
- Interfaçage avec périphériques

**I2C :**
- Protocole I2C
- Multi-master
- Gestion d'erreurs
- Capteurs I2C

**CAN :**
- Bus CAN 2.0
- Filtrage de messages
- Mailboxes
- Applications automobile

#### Conversion A/N avancée
- ADC multi-canaux
- Scan mode
- DMA avec ADC
- Déclenchement par timer
- Oversampling

#### DMA (Direct Memory Access)
- Principe et architecture
- Configuration des canaux
- Transferts mémoire-périphérique
- Interruptions DMA
- Chaînage de transferts

### Programmation temps réel

#### Concepts RTOS
- Tâches et scheduling
- Préemption
- Priorités
- États des tâches
- Context switching

#### FreeRTOS
**Tâches :**
- Création de tâches (xTaskCreate)
- Suspension et reprise
- Suppression de tâches
- Yield et delays

**Synchronisation :**
- Sémaphores (binaires, compteurs)
- Mutex
- Event groups
- Task notifications

**Communication :**
- Queues (files d'attente)
- Stream buffers
- Message buffers

**Gestion mémoire :**
- Heap management
- Allocation dynamique
- Stack overflow detection

#### Programmation temps réel
- Contraintes temporelles
- Worst Case Execution Time (WCET)
- Analyse de timing
- Déterminisme

### Optimisation et débogage

#### Optimisation code
- Optimisation compilateur (-O0, -O2, -O3)
- Inline functions
- Volatile et optimisation
- Code size vs speed
- Utilisation de la RAM

#### Techniques low power
- Sleep modes (Sleep, Stop, Standby)
- Périphériques en low power
- Wake-up sources
- RTC et alarmes
- Mesure de consommation

#### Débogage embarqué
- JTAG et SWD
- Breakpoints et watchpoints
- Live expressions
- Memory browser
- ITM (Instrumentation Trace Macrocell)
- printf débogage via SWO

## 🛠️ Projets pratiques

### TP Puzzle/Taquin
**Objectif :** Jeu de taquin sur STM32
- Affichage graphique (LCD)
- Gestion d'entrées (boutons, joystick)
- Logique de jeu
- Sauvegarde en EEPROM
- Animations

**Compétences :**
- GPIO et interruptions
- Communication SPI (LCD)
- Timers pour animations
- Gestion d'états

### Projets avec RTOS
- Système multi-tâches
- Acquisition de capteurs en parallèle
- Communication série asynchrone
- Interface utilisateur
- Gestion d'alarmes

## 💻 Outils utilisés

### IDE et environnements
- **STM32CubeIDE** : IDE officiel ST
- **Keil µVision** : IDE professionnel ARM
- **PlatformIO** : Environnement VS Code
- **STM32CubeMX** : Configuration graphique

### Débogage
- **ST-Link** : Programmateur/débogueur
- **OpenOCD** : Open source debugger
- **Segger J-Link** : Débogueur professionnel
- **Logic Analyzer** : Analyse de signaux

### Analyse
- **STM32CubeMonitor** : Monitoring temps réel
- **Energy profiler** : Analyse consommation
- **Tracealyzer** : Analyse RTOS

## 📊 Évaluation

- Travaux pratiques (40%)
- Projet Puzzle/RTOS (35%)
- Contrôle de connaissances (15%)
- Examen pratique (10%)

## 🔗 Liens avec d'autres cours

- **Automatique** : Implantation de régulateurs
- **ER** : Interfaçage électronique
- **Automatisme** : Logique séquentielle embarquée
- **Signal** : Traitement numérique embarqué

## 📐 Architecture typique d'un projet

```
Projet STM32
├── Core/
│   ├── Src/
│   │   ├── main.c
│   │   ├── stm32xxx_it.c
│   │   └── peripherals.c
│   └── Inc/
│       ├── main.h
│       └── peripherals.h
├── Drivers/
│   ├── CMSIS/
│   └── STM32xxx_HAL_Driver/
├── Middlewares/
│   └── FreeRTOS/
└── Application/
    ├── Tasks/
    ├── Drivers/
    └── Utils/
```

## 💡 Bonnes pratiques

### Code embarqué
- Toujours initialiser les variables
- Éviter malloc() dans l'interruption
- Protéger les sections critiques
- Volatile pour variables partagées
- Désactiver interruptions si nécessaire

### RTOS
- Tâches bien dimensionnées (stack)
- Priorités cohérentes
- Éviter les attentes actives
- Libérer les ressources
- Gestion des timeouts

### Débogage
- Utiliser les assertions
- Logging structuré
- Mesure de temps d'exécution
- Analyse de stack usage
- Tests unitaires quand possible

## 🎯 Compétences développées

- Programmation ARM Cortex-M avancée
- Utilisation de RTOS
- Gestion de périphériques complexes
- Optimisation de code embarqué
- Débogage système embarqué
- Conception de systèmes temps réel

## 📖 Concepts avancés

### Interruptions
- NVIC (Nested Vectored Interrupt Controller)
- Priorités et sous-priorités
- Latence d'interruption
- ISR (Interrupt Service Routine)
- Nesting et preemption

### DMA
- Transferts sans CPU
- Bursts et single transfers
- Circular mode
- Double buffering
- Synchronisation avec interruptions

### Low Power
- Mode Sleep (CPU off, périph on)
- Mode Stop (clocks off, RAM retained)
- Mode Standby (tout off sauf RTC)
- Wake-up rapide
- Optimisation consommation

## ⚠️ Pièges à éviter

- Stack overflow (tailles de stack)
- Race conditions (accès concurrents)
- Deadlocks (mutex circulaires)
- Priority inversion
- Watchdog non refresh
- Débordement de buffers
- Fréquence CPU mal configurée

---

## Documents de Cours

<div class="pdf-container">
  <div class="pdf-viewer">

    <div class="pdf-item">
      <h4>Guide de Demarrage VSCode pour STM32</h4>
      <p>Guide pratique pour configurer l'environnement de developpement VSCode pour la programmation de microcontroleurs STM32.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S3/IE/guide_démarrage_vscode.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S3/IE/guide_démarrage_vscode.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

  </div>
</div>

---

<style>body{font-family:Arial,sans-serif;background-color:#f4f4f9;color:#333;line-height:1.6}h2,h3,h4,h5{color:#2a7ae2}p{text-align:justify}code{background-color:#f5f5f5;padding:2px 6px;border-radius:3px;font-family:'Courier New',monospace}pre{background-color:#f5f5f5;padding:15px;border-radius:5px;overflow-x:auto}</style>

<div class="back-nav">
  <a href="./my-courses-2021-2022.html">&larr; Retour a Mes Cours 2021-2022</a>
</div>

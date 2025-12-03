---
layout: default
title: "Électronique Fonctions Numériques - S6"
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

# 💾 Électronique Fonctions Numériques - Semestre 6

**Année Universitaire** : 2022-2023  
**Semestre** : 6  
**Crédits** : 2 ECTS  
**Spécialité** : Électronique et Systèmes Embarqués

---

## PART A - Présentation Générale du Cours

<h3 class="section-title">Vue d'ensemble</h3>

Ce cours se concentre sur les interfaces de communication numériques et leur implémentation dans les systèmes embarqués. L'accent est mis sur les bus de communication série (I2C, SPI, UART) et les aspects pratiques de programmation des microcontrôleurs (horloges, gestion de la consommation, DMA). Le cours utilise des cartes Nordic nRF52832 (Bluetooth Low Energy) pour les travaux pratiques.

**Objectifs pédagogiques** :
- Maîtriser les protocoles de communication série (I2C, SPI)
- Programmer des microcontrôleurs ARM Cortex-M4 en C
- Comprendre les mécanismes d'horloge et de gestion de puissance
- Interfacer des capteurs via bus numériques
- Optimiser la consommation énergétique

<h3 class="section-title">Position dans le cursus</h3>

Ce cours fait suite et complète :
- **Fondements Électronique Numérique (S5)** : logique combinatoire et séquentielle
- **Langage C (S5)** : programmation système en C
- **Microcontrôleur (S6)** : architecture ARM et périphériques

Il prépare aux applications :
- **Embedded IA for IoT (S9)** : objets connectés et edge computing
- **Energy for Connected Objects (S9)** : optimisation énergétique
- **Projets embarqués** : conception de systèmes complets

---

## PART B - Expérience Personnelle et Contexte d'Apprentissage

<h3 class="section-title">Organisation et ressources</h3>

Le module était organisé en deux volets complémentaires :

**1. Cours magistraux** :
- Comparaison des bus de communication (I2C, SPI, UART, CAN, USB)
- Architecture des microcontrôleurs (horloges, DMA, modes basse consommation)
- Protocoles de communication série (timing, signalisation, adressage)
- Adaptation de niveaux logiques et WiFi

**2. Travaux pratiques** :
- Carte INSA-BLE basée sur Nordic nRF52832 (ARM Cortex-M4F + BLE)
- Programmation en C avec SDK Nordic
- TP I2C : lecture d'un capteur de température MCP9804
- TP SPI : interfaçage avec capteur TC72

<h3 class="section-title">Matériel utilisé</h3>

**Carte INSA-BLE (Nordic nRF52832)** :

| Composant | Spécification |
|-----------|--------------|
| MCU | ARM Cortex-M4F 64 MHz |
| Mémoire Flash | 512 KB |
| RAM | 64 KB |
| Connectivité | Bluetooth Low Energy 5.0 |
| Capteurs embarqués | LIS2DH12 (accéléromètre I2C), MPU-9250 (IMU 9 axes SPI) |
| Alimentation | 3,3V (régulateur intégré) |

**Périphériques externes** :
- MCP9804 : capteur de température I2C haute précision (±0,25°C)
- TC72 : capteur de température SPI

<h3 class="section-title">Déroulement des TPs</h3>

**TP I2C : Communication avec MCP9804**

L'objectif était de lire la température d'un capteur I2C et l'afficher en temps réel.

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S6/elec-numerique/spi-protocol.svg" alt="Protocole SPI" style="max-width: 550px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Chronogramme du protocole SPI - Communication full-duplex avec horloge maître</p>
</div>

**Étapes de mise en œuvre** :

1. **Initialisation du bus I2C** :
   - Configuration des broches SCL (P0.27) et SDA (P0.26)
   - Fréquence : 100 kHz (mode standard)
   - Activation du périphérique TWI (Two-Wire Interface)

2. **Adressage du capteur** :
   - Adresse I2C du MCP9804 : 0x1F (7 bits)
   - Registre de température : 0x05

3. **Lecture de la température** :
   - Envoi de la commande pour accéder au registre 0x05
   - Lecture de 2 octets (température sur 13 bits)
   - Conversion : bits de données / 16 = température en °C

**Extrait de code I2C** :

```c
#define TWI_INSTANCE_ID 0
#define MCP9804_ADDRESS 0x1F

static const nrf_drv_twi_t twi_instance = NRF_DRV_TWI_INSTANCE(TWI_INSTANCE_ID);

void twi_init(void) {
    ret_code_t err_code;
    const nrf_drv_twi_config_t twi_config = {
        .scl = NRF_GPIO_PIN_MAP(0, 27),
        .sda = NRF_GPIO_PIN_MAP(0, 26),
        .frequency = NRF_TWI_FREQ_100K,
        .interrupt_priority = APP_IRQ_PRIORITY_LOWEST,
        .clear_bus_init = false
    };
    err_code = nrf_drv_twi_init(&twi_instance, &twi_config, NULL, NULL);
    APP_ERROR_CHECK(err_code);
    nrf_drv_twi_enable(&twi_instance);
}

float read_temperature(void) {
    uint8_t reg[2] = {0x05, 0x00};
    uint8_t temp_data[2] = {0};
    
    nrf_drv_twi_tx(&twi_instance, MCP9804_ADDRESS, reg, sizeof(reg), true);
    nrf_delay_ms(10);
    nrf_drv_twi_rx(&twi_instance, MCP9804_ADDRESS, temp_data, sizeof(temp_data));
    
    int16_t temp_raw = (temp_data[0] << 8) | temp_data[1];
    temp_raw &= 0x0FFF;  // Masque 12 bits utiles
    float temperature = temp_raw / 16.0;
    
    return temperature;
}
```

**TP SPI : Communication avec TC72**

Le second TP consistait à interfacer un capteur de température SPI.

**Configuration SPI** :
- Mode 1 (CPOL=0, CPHA=1)
- Fréquence : 125 kHz
- CS (Chip Select) : P0.31, géré manuellement
- MOSI : P0.28, MISO : P0.29, SCK : P0.30

**Protocole de communication** :
1. Initialisation : écrire 0x80, 0x04 pour mode conversion continue
2. Lecture : envoyer commande 0x02, recevoir 3 octets
3. Traitement des données de température

**Extrait de code SPI** :

```c
#define SPI_CS_PIN    NRF_GPIO_PIN_MAP(0,31)
#define SPI_MISO_PIN  NRF_GPIO_PIN_MAP(0,29)
#define SPI_MOSI_PIN  NRF_GPIO_PIN_MAP(0,28)
#define SPI_SCK_PIN   NRF_GPIO_PIN_MAP(0,30)

void spi_init(void) {
    nrf_drv_spi_config_t spi_config = NRF_DRV_SPI_DEFAULT_CONFIG;
    spi_config.ss_pin   = NRF_DRV_SPI_PIN_NOT_USED;
    spi_config.miso_pin = SPI_MISO_PIN;
    spi_config.mosi_pin = SPI_MOSI_PIN;
    spi_config.sck_pin  = SPI_SCK_PIN;
    spi_config.mode     = NRF_DRV_SPI_MODE_1;
    spi_config.frequency = NRF_DRV_SPI_FREQ_125K;
    APP_ERROR_CHECK(nrf_drv_spi_init(&spi, &spi_config, spi_event_handler, NULL));
}

void tc_init(void) {
    nrf_gpio_cfg_output(SPI_CS_PIN);
    nrf_gpio_pin_clear(SPI_CS_PIN);
    spi_init();
    uint8_t data_to_send[2] = {0x80, 0x04}; // Conversion continue
    nrf_gpio_pin_set(SPI_CS_PIN);
    spi_send(data_to_send, 2, NULL, 0);
    nrf_gpio_pin_clear(SPI_CS_PIN);
}
```

<h3 class="section-title">Difficultés rencontrées</h3>

**Gestion du Chip Select en SPI** :
Le CS doit être manipulé manuellement (pas géré automatiquement par le driver). Oubli de basculer le CS provoquait l'absence de communication.

**Timing I2C** :
Les délais entre transmission et réception sont critiques. Un délai trop court entraînait des données corrompues.

**Débogage** :
Utilisation de printf via UART pour afficher les valeurs lues. Configuration du port série nécessaire dans sdk_config.h.

---

## PART C - Aspects Techniques Détaillés

<h3 class="section-title">1. Bus de Communication Série</h3>

**Comparaison des principaux bus** :

| Caractéristique | I2C | SPI | UART |
|-----------------|-----|-----|------|
| Fils | 2 (SDA, SCL) | 4 (MOSI, MISO, SCK, CS) | 2 (TX, RX) |
| Vitesse max | 400 kHz (Fast), 3,4 MHz (High-Speed) | Plusieurs MHz | 115200 bauds typique |
| Maître/Esclave | Multi-maître possible | Un maître, plusieurs esclaves | Point à point |
| Adressage | Adresse 7 ou 10 bits | Chip Select physique | Pas d'adresse |
| Complexité | Moyenne | Simple | Très simple |
| Distance | Courte (< 1 m) | Très courte | Moyenne (quelques mètres) |

<h3 class="section-title">2. Protocole I2C (Inter-Integrated Circuit)</h3>

**Principe de fonctionnement** :

I2C utilise deux lignes bidirectionnelles :
- **SDA** (Serial Data) : transmission des données
- **SCL** (Serial Clock) : horloge générée par le maître

**Conditions de START et STOP** :
- START : SDA passe de HIGH à LOW alors que SCL est HIGH
- STOP : SDA passe de LOW à HIGH alors que SCL est HIGH

**Trame de communication** :
1. Condition START
2. Adresse esclave (7 bits) + bit R/W
3. Bit ACK (acknowledgement) de l'esclave
4. Données (8 bits)
5. Bit ACK
6. Condition STOP

**Avantages** :
- Seulement 2 fils pour plusieurs périphériques
- Adressage logiciel (pas de CS supplémentaire)
- Détection des collisions en multi-maître

**Inconvénients** :
- Vitesse limitée
- Résistances de pull-up nécessaires
- Capacité parasite limite la longueur des câbles

<h3 class="section-title">3. Protocole SPI (Serial Peripheral Interface)</h3>

**Signaux SPI** :
- **MOSI** (Master Out Slave In) : données du maître vers l'esclave
- **MISO** (Master In Slave Out) : données de l'esclave vers le maître
- **SCK** (Serial Clock) : horloge générée par le maître
- **CS** (Chip Select) : sélection de l'esclave (actif bas)

**Modes SPI** (4 modes selon CPOL et CPHA) :

| Mode | CPOL | CPHA | Description |
|------|------|------|-------------|
| 0 | 0 | 0 | Clock repos à 0, échantillonnage front montant |
| 1 | 0 | 1 | Clock repos à 0, échantillonnage front descendant |
| 2 | 1 | 0 | Clock repos à 1, échantillonnage front descendant |
| 3 | 1 | 1 | Clock repos à 1, échantillonnage front montant |

**Avantages** :
- Communication full-duplex (simultanée dans les deux sens)
- Vitesse élevée (jusqu'à plusieurs dizaines de MHz)
- Simple à implémenter (pas de protocole complexe)

**Inconvénients** :
- Nombre de fils augmente avec le nombre d'esclaves (un CS par esclave)
- Pas de mécanisme d'acquittement (ACK)
- Pas de détection d'erreur intégrée

<h3 class="section-title">4. Gestion des Horloges dans les Microcontrôleurs</h3>

Les microcontrôleurs modernes disposent de plusieurs sources d'horloge pour optimiser performances et consommation.

**Sources d'horloge du nRF52832** :

| Horloge | Fréquence | Précision | Consommation | Usage |
|---------|-----------|-----------|--------------|-------|
| HFCLK interne | 64 MHz | ±5% | Élevée | CPU, périphériques rapides |
| HFCLK externe (cristal) | 64 MHz | ±20 ppm | Moyenne | Bluetooth, précision |
| LFCLK interne | 32,768 kHz | ±5% | Faible | RTC, timers basse vitesse |
| LFCLK externe (cristal) | 32,768 kHz | ±20 ppm | Très faible | RTC précis, sleep modes |

**Diviseurs d'horloge** :
Chaque périphérique peut avoir son propre diviseur pour adapter la fréquence.
Exemple : SPI à 125 kHz dérivé de HFCLK 64 MHz (diviseur 512).

**Importance pour la consommation** :
- Mode actif (64 MHz) : ~5 mA
- Mode sleep (32 kHz) : quelques µA
- Transition rapide entre modes pour économiser l'énergie

<h3 class="section-title">5. DMA (Direct Memory Access)</h3>

Le DMA permet des transferts de données entre périphériques et mémoire sans intervention du CPU.

**Avantages** :
- CPU libre pour d'autres tâches
- Transferts rapides et efficaces
- Réduit la consommation (CPU peut rester en sleep)

**Cas d'usage typiques** :
- Réception UART en continu (buffer circulaire)
- Acquisition ADC multicanaux
- Transferts SPI de grandes quantités de données

**Configuration DMA pour SPI** :
- Buffer source en mémoire
- Périphérique SPI comme destination
- Génération d'interruption en fin de transfert

<h3 class="section-title">6. Gestion de la Consommation (Low Power)</h3>

**Modes de fonctionnement du nRF52832** :

| Mode | Consommation | État CPU | Périphériques actifs | Réveil |
|------|--------------|----------|----------------------|--------|
| Active | 5-15 mA | Running | Tous | N/A |
| Sleep | 1-2 µA | Halt | RTC, GPIO | Interruption, timer |
| Deep Sleep | < 1 µA | Halt | Aucun | Reset externe |

**Techniques d'économie d'énergie** :
- Utiliser les interruptions plutôt que le polling
- Désactiver les périphériques non utilisés
- Réduire la fréquence d'horloge quand possible
- Utiliser des timers basse fréquence (LFCLK)
- Sleep entre les événements

**Exemple de cycle typique** :
1. Réveil par interruption timer (toutes les secondes)
2. Lecture capteur I2C (10 ms actif)
3. Traitement données (5 ms actif)
4. Retour en sleep (985 ms à quelques µA)
5. Consommation moyenne : ~50 µA au lieu de 5 mA continu

<h3 class="section-title">7. Adaptation de Niveaux Logiques</h3>

**Problématique** :
Les différents composants fonctionnent à des tensions différentes (5V, 3,3V, 1,8V).

**Solutions** :
- **Diviseur résistif** : simple mais ne fonctionne que pour 5V → 3,3V
- **Transistor MOSFET** : bidirectionnel pour I2C
- **Circuits dédiés** : TXS0108E (8 canaux, bidirectionnel)
- **Buffer 74LVCxx** : conversion avec isolation

**Carte INSA-BLE** :
Fonctionne en 3,3V. Connexion directe à des capteurs 3,3V. Pour interfacer avec du 5V (ex : Arduino), adaptation nécessaire.

---

## PART D - Analyse Réflexive et Perspectives

<h3 class="section-title">Compétences acquises</h3>

**Programmation embarquée bas niveau** :
Ce cours a renforcé la programmation en C pour systèmes embarqués, notamment la manipulation de registres, la gestion d'interruptions, et l'interfaçage avec périphériques matériels.

**Maîtrise des protocoles de communication** :
Comprendre les différences entre I2C et SPI, savoir choisir le bon protocole selon les contraintes (nombre de fils, vitesse, consommation), et implémenter correctement les transactions.

**Optimisation énergétique** :
Les techniques de low power sont essentielles pour les objets connectés sur batterie. Savoir mesurer et réduire la consommation est une compétence clé.

<h3 class="section-title">Points clés à retenir</h3>

**1. Choix du bus de communication** :
- I2C : plusieurs capteurs, peu de fils, vitesse modérée
- SPI : haute vitesse, full-duplex, plus de fils
- UART : simple, point à point, universel

**2. Gestion rigoureuse du matériel** :
Lire attentivement les datasheets, respecter les timings, vérifier les niveaux logiques, gérer correctement les CS et ACK.

**3. Débogage méthodique** :
Oscilloscope pour vérifier les signaux, printf pour tracer l'exécution, analyseur logique pour capturer les trames complètes.

**4. Consommation énergétique** :
Concevoir dès le départ avec la consommation en tête : sleep modes, réveil par interruption, choix des horloges.

<h3 class="section-title">Applications pratiques</h3>

**Projets personnels et professionnels** :

**Objets connectés IoT** :
Les compétences acquises sont directement applicables aux projets IoT : interfacer des capteurs environnementaux (température, humidité, pression), optimiser la durée de vie sur batterie.

**Projet Embedded IA for IoT (S9)** :
Utilisation du nRF52832 pour des applications de machine learning embarqué avec capteurs (accéléromètre, gyroscope).

**Instrumentation** :
Conception de systèmes d'acquisition de données multi-capteurs avec communication série vers un PC ou cloud.

<h3 class="section-title">Limites et ouvertures</h3>

**Limites du cours** :
- Peu de UART (pourtant très utilisé)
- Pas de CAN (important pour l'automobile)
- Pas d'USB (complexe mais omniprésent)
- Bluetooth uniquement mentionné, pas approfondi

**Ouvertures vers** :
- **Protocoles industriels** : Modbus, Profibus, CAN, EtherCAT
- **Communication sans fil** : Bluetooth, WiFi, LoRa, Zigbee
- **Interfaces haute vitesse** : USB 2.0/3.0, Ethernet, PCIe
- **Sécurité des communications** : chiffrement, authentification
- **Réseaux de capteurs** : topologies mesh, routage, économie d'énergie

<h3 class="section-title">Évolution technologique</h3>

**Tendances actuelles** :
- **Intégration accrue** : SoC avec CPU + périphériques + radio
- **Ultra-basse consommation** : nW pour capteurs récoltant l'énergie ambiante
- **Protocoles unifiés** : Matter pour interopérabilité IoT
- **Edge computing** : traitement local avec IA embarquée

**Impact des nouvelles normes** :
- Bluetooth 5.0+ : portée étendue, débit augmenté
- Thread et Matter : standardisation IoT
- MIPI I3C : évolution d'I2C avec vitesses jusqu'à 12,5 MHz

<h3 class="section-title">Conclusion</h3>

Les bus de communication numériques sont le système nerveux des systèmes embarqués. Leur maîtrise est indispensable pour interfacer capteurs, actionneurs, et modules de communication.

Ce cours a fourni une base solide en I2C et SPI, avec une approche pratique sur microcontrôleur ARM. La carte nRF52832 est représentative des SoC modernes : puissant, basse consommation, connectivité intégrée.

**Complémentarité avec les autres cours** :
- [Microcontrôleur - S6](./microcontroleur.html) : architecture ARM Cortex-M
- [Langage d'Assemblage ARM - S6](./langage-assemblage-arm.html) : bas niveau ARM
- [Embedded IA for IoT - S9](./embedded-ia-iot.html) : applications avancées
- [Energy for Connected Objects - S9](./energy-connected-objects.html) : optimisation poussée

**Recommandations pour aller plus loin** :
- Étudier les datasheets complètes (nRF52, capteurs)
- Expérimenter avec d'autres bus (CAN, USB)
- Mesurer la consommation réelle avec un ampèremètre de précision
- Développer des projets complets intégrant plusieurs capteurs
- Explorer les stacks Bluetooth et WiFi

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
      <h4>📖 Protocole I2C</h4>
      <p>Cours complet sur le bus I2C : principe de fonctionnement, adressage, trame de communication et implémentation.</p>
      <embed src="/cours-pdf/S6/Elec-Fonctions-Numeriques/i2c.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Elec-Fonctions-Numeriques/i2c.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>📖 Protocole SPI</h4>
      <p>Cours sur le bus SPI : principe maître-esclave, sélection de périphérique, modes d'horloge et communication full-duplex.</p>
      <embed src="/cours-pdf/S6/Elec-Fonctions-Numeriques/spi.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Elec-Fonctions-Numeriques/spi.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>📖 Low Power Design</h4>
      <p>Techniques d'optimisation de la consommation : modes de veille, clock gating, gestion d'énergie dans les microcontrôleurs.</p>
      <embed src="/cours-pdf/S6/Elec-Fonctions-Numeriques/low-power.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Elec-Fonctions-Numeriques/low-power.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>📖 Microcontrôleur, Horloge et DMA</h4>
      <p>Architecture des microcontrôleurs : gestion des horloges système et accès direct mémoire (DMA) pour performances optimales.</p>
      <embed src="/cours-pdf/S6/Elec-Fonctions-Numeriques/microcontroleur-horloge-dma.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Elec-Fonctions-Numeriques/microcontroleur-horloge-dma.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
  </div>
</div>

---

*Cours enseigné en 2022-2023 à l'INSA Toulouse, Département Génie Électrique et Informatique.*

---
layout: default
title: "Électronique Fonctions Numériques - S6"
date: 2024-10-02 10:56:03 +0200
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

<div class="back-nav">
    <a href="./my-courses-2022-2023.html" data-i18n-html="back-courses-2022-2023">&larr; Retour aux Cours 2022-2023</a>
</div>

<!-- ==================== FRENCH VERSION ==================== -->
<div class="lang-fr">

<h1>Electronique Fonctions Numeriques - Semestre 6</h1>

<p><strong>Annee Universitaire</strong> : 2022-2023<br/>
<strong>Semestre</strong> : 6<br/>
<strong>Credits</strong> : 2 ECTS<br/>
<strong>Specialite</strong> : Electronique et Systemes Embarques</p>

<hr/>

<h2>PART A - Presentation Generale du Cours</h2>

<h3 class="section-title">Vue d'ensemble</h3>

<p>Ce cours se concentre sur les interfaces de communication numeriques et leur implementation dans les systemes embarques. L'accent est mis sur les bus de communication serie (I2C, SPI, UART) et les aspects pratiques de programmation des microcontroleurs (horloges, gestion de la consommation, DMA). Le cours utilise des cartes Nordic nRF52832 (Bluetooth Low Energy) pour les travaux pratiques.</p>

<p><strong>Objectifs pedagogiques</strong> :</p>
<ul>
<li>Maitriser les protocoles de communication serie (I2C, SPI)</li>
<li>Programmer des microcontroleurs ARM Cortex-M4 en C</li>
<li>Comprendre les mecanismes d'horloge et de gestion de puissance</li>
<li>Interfacer des capteurs via bus numeriques</li>
<li>Optimiser la consommation energetique</li>
</ul>

<h3 class="section-title">Position dans le cursus</h3>

<p>Ce cours fait suite et complete :</p>
<ul>
<li><strong>Fondements Electronique Numerique (S5)</strong> : logique combinatoire et sequentielle</li>
<li><strong>Langage C (S5)</strong> : programmation systeme en C</li>
<li><strong>Microcontroleur (S6)</strong> : architecture ARM et peripheriques</li>
</ul>

<p>Il prepare aux applications :</p>
<ul>
<li><strong>Embedded IA for IoT (S9)</strong> : objets connectes et edge computing</li>
<li><strong>Energy for Connected Objects (S9)</strong> : optimisation energetique</li>
<li><strong>Projets embarques</strong> : conception de systemes complets</li>
</ul>

<hr/>

<h2>PART B - Experience Personnelle et Contexte d'Apprentissage</h2>

<h3 class="section-title">Organisation et ressources</h3>

<p>Le module etait organise en deux volets complementaires :</p>

<p><strong>1. Cours magistraux</strong> :</p>
<ul>
<li>Comparaison des bus de communication (I2C, SPI, UART, CAN, USB)</li>
<li>Architecture des microcontroleurs (horloges, DMA, modes basse consommation)</li>
<li>Protocoles de communication serie (timing, signalisation, adressage)</li>
<li>Adaptation de niveaux logiques et WiFi</li>
</ul>

<p><strong>2. Travaux pratiques</strong> :</p>
<ul>
<li>Carte INSA-BLE basee sur Nordic nRF52832 (ARM Cortex-M4F + BLE)</li>
<li>Programmation en C avec SDK Nordic</li>
<li>TP I2C : lecture d'un capteur de temperature MCP9804</li>
<li>TP SPI : interfacage avec capteur TC72</li>
</ul>

<h3 class="section-title">Materiel utilise</h3>

<p><strong>Carte INSA-BLE (Nordic nRF52832)</strong> :</p>

<table>
<thead>
<tr><th>Composant</th><th>Specification</th></tr>
</thead>
<tbody>
<tr><td>MCU</td><td>ARM Cortex-M4F 64 MHz</td></tr>
<tr><td>Memoire Flash</td><td>512 KB</td></tr>
<tr><td>RAM</td><td>64 KB</td></tr>
<tr><td>Connectivite</td><td>Bluetooth Low Energy 5.0</td></tr>
<tr><td>Capteurs embarques</td><td>LIS2DH12 (accelerometre I2C), MPU-9250 (IMU 9 axes SPI)</td></tr>
<tr><td>Alimentation</td><td>3,3V (regulateur integre)</td></tr>
</tbody>
</table>

<p><strong>Peripheriques externes</strong> :</p>
<ul>
<li>MCP9804 : capteur de temperature I2C haute precision (+/-0,25 deg C)</li>
<li>TC72 : capteur de temperature SPI</li>
</ul>

<h3 class="section-title">Deroulement des TPs</h3>

<p><strong>TP I2C : Communication avec MCP9804</strong></p>

<p>L'objectif etait de lire la temperature d'un capteur I2C et l'afficher en temps reel.</p>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S6/elec-numerique/spi-protocol.svg" alt="Protocole SPI" style="max-width: 550px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Chronogramme du protocole SPI - Communication full-duplex avec horloge maitre</p>
</div>

<p><strong>Etapes de mise en oeuvre</strong> :</p>

<ol>
<li><strong>Initialisation du bus I2C</strong> :
<ul>
<li>Configuration des broches SCL (P0.27) et SDA (P0.26)</li>
<li>Frequence : 100 kHz (mode standard)</li>
<li>Activation du peripherique TWI (Two-Wire Interface)</li>
</ul></li>
<li><strong>Adressage du capteur</strong> :
<ul>
<li>Adresse I2C du MCP9804 : 0x1F (7 bits)</li>
<li>Registre de temperature : 0x05</li>
</ul></li>
<li><strong>Lecture de la temperature</strong> :
<ul>
<li>Envoi de la commande pour acceder au registre 0x05</li>
<li>Lecture de 2 octets (temperature sur 13 bits)</li>
<li>Conversion : bits de donnees / 16 = temperature en deg C</li>
</ul></li>
</ol>

<p><strong>Extrait de code I2C</strong> :</p>

<pre><code class="language-c">#define TWI_INSTANCE_ID 0
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
    err_code = nrf_drv_twi_init(&amp;twi_instance, &amp;twi_config, NULL, NULL);
    APP_ERROR_CHECK(err_code);
    nrf_drv_twi_enable(&amp;twi_instance);
}

float read_temperature(void) {
    uint8_t reg[2] = {0x05, 0x00};
    uint8_t temp_data[2] = {0};

    nrf_drv_twi_tx(&amp;twi_instance, MCP9804_ADDRESS, reg, sizeof(reg), true);
    nrf_delay_ms(10);
    nrf_drv_twi_rx(&amp;twi_instance, MCP9804_ADDRESS, temp_data, sizeof(temp_data));

    int16_t temp_raw = (temp_data[0] &lt;&lt; 8) | temp_data[1];
    temp_raw &amp;= 0x0FFF;  // Masque 12 bits utiles
    float temperature = temp_raw / 16.0;

    return temperature;
}</code></pre>

<p><strong>TP SPI : Communication avec TC72</strong></p>

<p>Le second TP consistait a interfacer un capteur de temperature SPI.</p>

<p><strong>Configuration SPI</strong> :</p>
<ul>
<li>Mode 1 (CPOL=0, CPHA=1)</li>
<li>Frequence : 125 kHz</li>
<li>CS (Chip Select) : P0.31, gere manuellement</li>
<li>MOSI : P0.28, MISO : P0.29, SCK : P0.30</li>
</ul>

<p><strong>Protocole de communication</strong> :</p>
<ol>
<li>Initialisation : ecrire 0x80, 0x04 pour mode conversion continue</li>
<li>Lecture : envoyer commande 0x02, recevoir 3 octets</li>
<li>Traitement des donnees de temperature</li>
</ol>

<p><strong>Extrait de code SPI</strong> :</p>

<pre><code class="language-c">#define SPI_CS_PIN    NRF_GPIO_PIN_MAP(0,31)
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
    APP_ERROR_CHECK(nrf_drv_spi_init(&amp;spi, &amp;spi_config, spi_event_handler, NULL));
}

void tc_init(void) {
    nrf_gpio_cfg_output(SPI_CS_PIN);
    nrf_gpio_pin_clear(SPI_CS_PIN);
    spi_init();
    uint8_t data_to_send[2] = {0x80, 0x04}; // Conversion continue
    nrf_gpio_pin_set(SPI_CS_PIN);
    spi_send(data_to_send, 2, NULL, 0);
    nrf_gpio_pin_clear(SPI_CS_PIN);
}</code></pre>

<h3 class="section-title">Difficultes rencontrees</h3>

<p><strong>Gestion du Chip Select en SPI</strong> :
Le CS doit etre manipule manuellement (pas gere automatiquement par le driver). Oubli de basculer le CS provoquait l'absence de communication.</p>

<p><strong>Timing I2C</strong> :
Les delais entre transmission et reception sont critiques. Un delai trop court entrainait des donnees corrompues.</p>

<p><strong>Debogage</strong> :
Utilisation de printf via UART pour afficher les valeurs lues. Configuration du port serie necessaire dans sdk_config.h.</p>

<hr/>

<h2>PART C - Aspects Techniques Detailles</h2>

<h3 class="section-title">1. Bus de Communication Serie</h3>

<p><strong>Comparaison des principaux bus</strong> :</p>

<table>
<thead>
<tr><th>Caracteristique</th><th>I2C</th><th>SPI</th><th>UART</th></tr>
</thead>
<tbody>
<tr><td>Fils</td><td>2 (SDA, SCL)</td><td>4 (MOSI, MISO, SCK, CS)</td><td>2 (TX, RX)</td></tr>
<tr><td>Vitesse max</td><td>400 kHz (Fast), 3,4 MHz (High-Speed)</td><td>Plusieurs MHz</td><td>115200 bauds typique</td></tr>
<tr><td>Maitre/Esclave</td><td>Multi-maitre possible</td><td>Un maitre, plusieurs esclaves</td><td>Point a point</td></tr>
<tr><td>Adressage</td><td>Adresse 7 ou 10 bits</td><td>Chip Select physique</td><td>Pas d'adresse</td></tr>
<tr><td>Complexite</td><td>Moyenne</td><td>Simple</td><td>Tres simple</td></tr>
<tr><td>Distance</td><td>Courte (&lt; 1 m)</td><td>Tres courte</td><td>Moyenne (quelques metres)</td></tr>
</tbody>
</table>

<h3 class="section-title">2. Protocole I2C (Inter-Integrated Circuit)</h3>

<p><strong>Principe de fonctionnement</strong> :</p>

<p>I2C utilise deux lignes bidirectionnelles :</p>
<ul>
<li><strong>SDA</strong> (Serial Data) : transmission des donnees</li>
<li><strong>SCL</strong> (Serial Clock) : horloge generee par le maitre</li>
</ul>

<p><strong>Conditions de START et STOP</strong> :</p>
<ul>
<li>START : SDA passe de HIGH a LOW alors que SCL est HIGH</li>
<li>STOP : SDA passe de LOW a HIGH alors que SCL est HIGH</li>
</ul>

<p><strong>Trame de communication</strong> :</p>
<ol>
<li>Condition START</li>
<li>Adresse esclave (7 bits) + bit R/W</li>
<li>Bit ACK (acknowledgement) de l'esclave</li>
<li>Donnees (8 bits)</li>
<li>Bit ACK</li>
<li>Condition STOP</li>
</ol>

<p><strong>Avantages</strong> :</p>
<ul>
<li>Seulement 2 fils pour plusieurs peripheriques</li>
<li>Adressage logiciel (pas de CS supplementaire)</li>
<li>Detection des collisions en multi-maitre</li>
</ul>

<p><strong>Inconvenients</strong> :</p>
<ul>
<li>Vitesse limitee</li>
<li>Resistances de pull-up necessaires</li>
<li>Capacite parasite limite la longueur des cables</li>
</ul>

<h3 class="section-title">3. Protocole SPI (Serial Peripheral Interface)</h3>

<p><strong>Signaux SPI</strong> :</p>
<ul>
<li><strong>MOSI</strong> (Master Out Slave In) : donnees du maitre vers l'esclave</li>
<li><strong>MISO</strong> (Master In Slave Out) : donnees de l'esclave vers le maitre</li>
<li><strong>SCK</strong> (Serial Clock) : horloge generee par le maitre</li>
<li><strong>CS</strong> (Chip Select) : selection de l'esclave (actif bas)</li>
</ul>

<p><strong>Modes SPI</strong> (4 modes selon CPOL et CPHA) :</p>

<table>
<thead>
<tr><th>Mode</th><th>CPOL</th><th>CPHA</th><th>Description</th></tr>
</thead>
<tbody>
<tr><td>0</td><td>0</td><td>0</td><td>Clock repos a 0, echantillonnage front montant</td></tr>
<tr><td>1</td><td>0</td><td>1</td><td>Clock repos a 0, echantillonnage front descendant</td></tr>
<tr><td>2</td><td>1</td><td>0</td><td>Clock repos a 1, echantillonnage front descendant</td></tr>
<tr><td>3</td><td>1</td><td>1</td><td>Clock repos a 1, echantillonnage front montant</td></tr>
</tbody>
</table>

<p><strong>Avantages</strong> :</p>
<ul>
<li>Communication full-duplex (simultanee dans les deux sens)</li>
<li>Vitesse elevee (jusqu'a plusieurs dizaines de MHz)</li>
<li>Simple a implementer (pas de protocole complexe)</li>
</ul>

<p><strong>Inconvenients</strong> :</p>
<ul>
<li>Nombre de fils augmente avec le nombre d'esclaves (un CS par esclave)</li>
<li>Pas de mecanisme d'acquittement (ACK)</li>
<li>Pas de detection d'erreur integree</li>
</ul>

<h3 class="section-title">4. Gestion des Horloges dans les Microcontroleurs</h3>

<p>Les microcontroleurs modernes disposent de plusieurs sources d'horloge pour optimiser performances et consommation.</p>

<p><strong>Sources d'horloge du nRF52832</strong> :</p>

<table>
<thead>
<tr><th>Horloge</th><th>Frequence</th><th>Precision</th><th>Consommation</th><th>Usage</th></tr>
</thead>
<tbody>
<tr><td>HFCLK interne</td><td>64 MHz</td><td>+/-5%</td><td>Elevee</td><td>CPU, peripheriques rapides</td></tr>
<tr><td>HFCLK externe (cristal)</td><td>64 MHz</td><td>+/-20 ppm</td><td>Moyenne</td><td>Bluetooth, precision</td></tr>
<tr><td>LFCLK interne</td><td>32,768 kHz</td><td>+/-5%</td><td>Faible</td><td>RTC, timers basse vitesse</td></tr>
<tr><td>LFCLK externe (cristal)</td><td>32,768 kHz</td><td>+/-20 ppm</td><td>Tres faible</td><td>RTC precis, sleep modes</td></tr>
</tbody>
</table>

<p><strong>Diviseurs d'horloge</strong> :
Chaque peripherique peut avoir son propre diviseur pour adapter la frequence.
Exemple : SPI a 125 kHz derive de HFCLK 64 MHz (diviseur 512).</p>

<p><strong>Importance pour la consommation</strong> :</p>
<ul>
<li>Mode actif (64 MHz) : ~5 mA</li>
<li>Mode sleep (32 kHz) : quelques uA</li>
<li>Transition rapide entre modes pour economiser l'energie</li>
</ul>

<h3 class="section-title">5. DMA (Direct Memory Access)</h3>

<p>Le DMA permet des transferts de donnees entre peripheriques et memoire sans intervention du CPU.</p>

<p><strong>Avantages</strong> :</p>
<ul>
<li>CPU libre pour d'autres taches</li>
<li>Transferts rapides et efficaces</li>
<li>Reduit la consommation (CPU peut rester en sleep)</li>
</ul>

<p><strong>Cas d'usage typiques</strong> :</p>
<ul>
<li>Reception UART en continu (buffer circulaire)</li>
<li>Acquisition ADC multicanaux</li>
<li>Transferts SPI de grandes quantites de donnees</li>
</ul>

<p><strong>Configuration DMA pour SPI</strong> :</p>
<ul>
<li>Buffer source en memoire</li>
<li>Peripherique SPI comme destination</li>
<li>Generation d'interruption en fin de transfert</li>
</ul>

<h3 class="section-title">6. Gestion de la Consommation (Low Power)</h3>

<p><strong>Modes de fonctionnement du nRF52832</strong> :</p>

<table>
<thead>
<tr><th>Mode</th><th>Consommation</th><th>Etat CPU</th><th>Peripheriques actifs</th><th>Reveil</th></tr>
</thead>
<tbody>
<tr><td>Active</td><td>5-15 mA</td><td>Running</td><td>Tous</td><td>N/A</td></tr>
<tr><td>Sleep</td><td>1-2 uA</td><td>Halt</td><td>RTC, GPIO</td><td>Interruption, timer</td></tr>
<tr><td>Deep Sleep</td><td>&lt; 1 uA</td><td>Halt</td><td>Aucun</td><td>Reset externe</td></tr>
</tbody>
</table>

<p><strong>Techniques d'economie d'energie</strong> :</p>
<ul>
<li>Utiliser les interruptions plutot que le polling</li>
<li>Desactiver les peripheriques non utilises</li>
<li>Reduire la frequence d'horloge quand possible</li>
<li>Utiliser des timers basse frequence (LFCLK)</li>
<li>Sleep entre les evenements</li>
</ul>

<p><strong>Exemple de cycle typique</strong> :</p>
<ol>
<li>Reveil par interruption timer (toutes les secondes)</li>
<li>Lecture capteur I2C (10 ms actif)</li>
<li>Traitement donnees (5 ms actif)</li>
<li>Retour en sleep (985 ms a quelques uA)</li>
<li>Consommation moyenne : ~50 uA au lieu de 5 mA continu</li>
</ol>

<h3 class="section-title">7. Adaptation de Niveaux Logiques</h3>

<p><strong>Problematique</strong> :
Les differents composants fonctionnent a des tensions differentes (5V, 3,3V, 1,8V).</p>

<p><strong>Solutions</strong> :</p>
<ul>
<li><strong>Diviseur resistif</strong> : simple mais ne fonctionne que pour 5V vers 3,3V</li>
<li><strong>Transistor MOSFET</strong> : bidirectionnel pour I2C</li>
<li><strong>Circuits dedies</strong> : TXS0108E (8 canaux, bidirectionnel)</li>
<li><strong>Buffer 74LVCxx</strong> : conversion avec isolation</li>
</ul>

<p><strong>Carte INSA-BLE</strong> :
Fonctionne en 3,3V. Connexion directe a des capteurs 3,3V. Pour interfacer avec du 5V (ex : Arduino), adaptation necessaire.</p>

<hr/>

<h2>PART D - Analyse Reflexive et Perspectives</h2>

<h3 class="section-title">Competences acquises</h3>

<p><strong>Programmation embarquee bas niveau</strong> :
Ce cours a renforce la programmation en C pour systemes embarques, notamment la manipulation de registres, la gestion d'interruptions, et l'interfacage avec peripheriques materiels.</p>

<p><strong>Maitrise des protocoles de communication</strong> :
Comprendre les differences entre I2C et SPI, savoir choisir le bon protocole selon les contraintes (nombre de fils, vitesse, consommation), et implementer correctement les transactions.</p>

<p><strong>Optimisation energetique</strong> :
Les techniques de low power sont essentielles pour les objets connectes sur batterie. Savoir mesurer et reduire la consommation est une competence cle.</p>

<h3 class="section-title">Points cles a retenir</h3>

<p><strong>1. Choix du bus de communication</strong> :</p>
<ul>
<li>I2C : plusieurs capteurs, peu de fils, vitesse moderee</li>
<li>SPI : haute vitesse, full-duplex, plus de fils</li>
<li>UART : simple, point a point, universel</li>
</ul>

<p><strong>2. Gestion rigoureuse du materiel</strong> :
Lire attentivement les datasheets, respecter les timings, verifier les niveaux logiques, gerer correctement les CS et ACK.</p>

<p><strong>3. Debogage methodique</strong> :
Oscilloscope pour verifier les signaux, printf pour tracer l'execution, analyseur logique pour capturer les trames completes.</p>

<p><strong>4. Consommation energetique</strong> :
Concevoir des le depart avec la consommation en tete : sleep modes, reveil par interruption, choix des horloges.</p>

<h3 class="section-title">Applications pratiques</h3>

<p><strong>Projets personnels et professionnels</strong> :</p>

<p><strong>Objets connectes IoT</strong> :
Les competences acquises sont directement applicables aux projets IoT : interfacer des capteurs environnementaux (temperature, humidite, pression), optimiser la duree de vie sur batterie.</p>

<p><strong>Projet Embedded IA for IoT (S9)</strong> :
Utilisation du nRF52832 pour des applications de machine learning embarque avec capteurs (accelerometre, gyroscope).</p>

<p><strong>Instrumentation</strong> :
Conception de systemes d'acquisition de donnees multi-capteurs avec communication serie vers un PC ou cloud.</p>

<h3 class="section-title">Limites et ouvertures</h3>

<p><strong>Limites du cours</strong> :</p>
<ul>
<li>Peu de UART (pourtant tres utilise)</li>
<li>Pas de CAN (important pour l'automobile)</li>
<li>Pas d'USB (complexe mais omnipresent)</li>
<li>Bluetooth uniquement mentionne, pas approfondi</li>
</ul>

<p><strong>Ouvertures vers</strong> :</p>
<ul>
<li><strong>Protocoles industriels</strong> : Modbus, Profibus, CAN, EtherCAT</li>
<li><strong>Communication sans fil</strong> : Bluetooth, WiFi, LoRa, Zigbee</li>
<li><strong>Interfaces haute vitesse</strong> : USB 2.0/3.0, Ethernet, PCIe</li>
<li><strong>Securite des communications</strong> : chiffrement, authentification</li>
<li><strong>Reseaux de capteurs</strong> : topologies mesh, routage, economie d'energie</li>
</ul>

<h3 class="section-title">Evolution technologique</h3>

<p><strong>Tendances actuelles</strong> :</p>
<ul>
<li><strong>Integration accrue</strong> : SoC avec CPU + peripheriques + radio</li>
<li><strong>Ultra-basse consommation</strong> : nW pour capteurs recoltant l'energie ambiante</li>
<li><strong>Protocoles unifies</strong> : Matter pour interoperabilite IoT</li>
<li><strong>Edge computing</strong> : traitement local avec IA embarquee</li>
</ul>

<p><strong>Impact des nouvelles normes</strong> :</p>
<ul>
<li>Bluetooth 5.0+ : portee etendue, debit augmente</li>
<li>Thread et Matter : standardisation IoT</li>
<li>MIPI I3C : evolution d'I2C avec vitesses jusqu'a 12,5 MHz</li>
</ul>

<h3 class="section-title">Conclusion</h3>

<p>Les bus de communication numeriques sont le systeme nerveux des systemes embarques. Leur maitrise est indispensable pour interfacer capteurs, actionneurs, et modules de communication.</p>

<p>Ce cours a fourni une base solide en I2C et SPI, avec une approche pratique sur microcontroleur ARM. La carte nRF52832 est representative des SoC modernes : puissant, basse consommation, connectivite integree.</p>

<p><strong>Complementarite avec les autres cours</strong> :</p>
<ul>
<li><a href="./microcontroleur.html">Microcontroleur - S6</a> : architecture ARM Cortex-M</li>
<li><a href="./langage-assemblage-arm.html">Langage d'Assemblage ARM - S6</a> : bas niveau ARM</li>
<li><a href="./embedded-ia-iot.html">Embedded IA for IoT - S9</a> : applications avancees</li>
<li><a href="./energy-connected-objects.html">Energy for Connected Objects - S9</a> : optimisation poussee</li>
</ul>

<p><strong>Recommandations pour aller plus loin</strong> :</p>
<ul>
<li>Etudier les datasheets completes (nRF52, capteurs)</li>
<li>Experimenter avec d'autres bus (CAN, USB)</li>
<li>Mesurer la consommation reelle avec un amperemetre de precision</li>
<li>Developper des projets complets integrant plusieurs capteurs</li>
<li>Explorer les stacks Bluetooth et WiFi</li>
</ul>

<hr/>

<h2>Documents de Cours</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Protocole I2C</h4>
      <p>Cours complet sur le bus I2C : principe de fonctionnement, adressage, trame de communication et implementation.</p>
      <embed src="/cours-pdf/S6/Elec-Fonctions-Numeriques/i2c.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Elec-Fonctions-Numeriques/i2c.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>Protocole SPI</h4>
      <p>Cours sur le bus SPI : principe maitre-esclave, selection de peripherique, modes d'horloge et communication full-duplex.</p>
      <embed src="/cours-pdf/S6/Elec-Fonctions-Numeriques/spi.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Elec-Fonctions-Numeriques/spi.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>Low Power Design</h4>
      <p>Techniques d'optimisation de la consommation : modes de veille, clock gating, gestion d'energie dans les microcontroleurs.</p>
      <embed src="/cours-pdf/S6/Elec-Fonctions-Numeriques/low-power.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Elec-Fonctions-Numeriques/low-power.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>Microcontroleur, Horloge et DMA</h4>
      <p>Architecture des microcontroleurs : gestion des horloges systeme et acces direct memoire (DMA) pour performances optimales.</p>
      <embed src="/cours-pdf/S6/Elec-Fonctions-Numeriques/microcontroleur-horloge-dma.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Elec-Fonctions-Numeriques/microcontroleur-horloge-dma.pdf" target="_blank">Telecharger</a></p>
    </div>
  </div>
</div>

<hr/>

</div>

<!-- ==================== ENGLISH VERSION ==================== -->
<div class="lang-en">

<h1>Digital Electronics Functions - Semester 6</h1>

<p><strong>Academic Year</strong>: 2022-2023<br/>
<strong>Semester</strong>: 6<br/>
<strong>Credits</strong>: 2 ECTS<br/>
<strong>Specialization</strong>: Electronics and Embedded Systems</p>

<hr/>

<h2>PART A - General Course Overview</h2>

<h3 class="section-title">Overview</h3>

<p>This course focuses on digital communication interfaces and their implementation in embedded systems. The emphasis is on serial communication buses (I2C, SPI, UART) and practical aspects of microcontroller programming (clocks, power management, DMA). The course uses Nordic nRF52832 boards (Bluetooth Low Energy) for the lab sessions.</p>

<p><strong>Learning objectives</strong>:</p>
<ul>
<li>Master serial communication protocols (I2C, SPI)</li>
<li>Program ARM Cortex-M4 microcontrollers in C</li>
<li>Understand clock mechanisms and power management</li>
<li>Interface sensors via digital buses</li>
<li>Optimize energy consumption</li>
</ul>

<h3 class="section-title">Position in the curriculum</h3>

<p>This course follows and complements:</p>
<ul>
<li><strong>Fundamentals of Digital Electronics (S5)</strong>: combinational and sequential logic</li>
<li><strong>C Language (S5)</strong>: systems programming in C</li>
<li><strong>Microcontroller (S6)</strong>: ARM architecture and peripherals</li>
</ul>

<p>It prepares for the following applications:</p>
<ul>
<li><strong>Embedded IA for IoT (S9)</strong>: connected objects and edge computing</li>
<li><strong>Energy for Connected Objects (S9)</strong>: energy optimization</li>
<li><strong>Embedded projects</strong>: complete system design</li>
</ul>

<hr/>

<h2>PART B - Personal Experience and Learning Context</h2>

<h3 class="section-title">Organization and resources</h3>

<p>The module was organized into two complementary components:</p>

<p><strong>1. Lectures</strong>:</p>
<ul>
<li>Comparison of communication buses (I2C, SPI, UART, CAN, USB)</li>
<li>Microcontroller architecture (clocks, DMA, low-power modes)</li>
<li>Serial communication protocols (timing, signaling, addressing)</li>
<li>Logic level shifting and WiFi</li>
</ul>

<p><strong>2. Lab sessions</strong>:</p>
<ul>
<li>INSA-BLE board based on Nordic nRF52832 (ARM Cortex-M4F + BLE)</li>
<li>C programming with Nordic SDK</li>
<li>I2C lab: reading an MCP9804 temperature sensor</li>
<li>SPI lab: interfacing with a TC72 sensor</li>
</ul>

<h3 class="section-title">Hardware used</h3>

<p><strong>INSA-BLE Board (Nordic nRF52832)</strong>:</p>

<table>
<thead>
<tr><th>Component</th><th>Specification</th></tr>
</thead>
<tbody>
<tr><td>MCU</td><td>ARM Cortex-M4F 64 MHz</td></tr>
<tr><td>Flash Memory</td><td>512 KB</td></tr>
<tr><td>RAM</td><td>64 KB</td></tr>
<tr><td>Connectivity</td><td>Bluetooth Low Energy 5.0</td></tr>
<tr><td>Onboard Sensors</td><td>LIS2DH12 (I2C accelerometer), MPU-9250 (9-axis IMU SPI)</td></tr>
<tr><td>Power Supply</td><td>3.3V (integrated regulator)</td></tr>
</tbody>
</table>

<p><strong>External peripherals</strong>:</p>
<ul>
<li>MCP9804: high-precision I2C temperature sensor (+/-0.25 deg C)</li>
<li>TC72: SPI temperature sensor</li>
</ul>

<h3 class="section-title">Lab session details</h3>

<p><strong>I2C Lab: Communication with MCP9804</strong></p>

<p>The objective was to read the temperature from an I2C sensor and display it in real time.</p>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S6/elec-numerique/spi-protocol.svg" alt="SPI Protocol" style="max-width: 550px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: SPI protocol timing diagram - Full-duplex communication with master clock</p>
</div>

<p><strong>Implementation steps</strong>:</p>

<ol>
<li><strong>I2C bus initialization</strong>:
<ul>
<li>Pin configuration for SCL (P0.27) and SDA (P0.26)</li>
<li>Frequency: 100 kHz (standard mode)</li>
<li>Enabling the TWI (Two-Wire Interface) peripheral</li>
</ul></li>
<li><strong>Sensor addressing</strong>:
<ul>
<li>MCP9804 I2C address: 0x1F (7 bits)</li>
<li>Temperature register: 0x05</li>
</ul></li>
<li><strong>Temperature reading</strong>:
<ul>
<li>Sending the command to access register 0x05</li>
<li>Reading 2 bytes (temperature on 13 bits)</li>
<li>Conversion: data bits / 16 = temperature in deg C</li>
</ul></li>
</ol>

<p><strong>I2C code excerpt</strong>:</p>

<pre><code class="language-c">#define TWI_INSTANCE_ID 0
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
    err_code = nrf_drv_twi_init(&amp;twi_instance, &amp;twi_config, NULL, NULL);
    APP_ERROR_CHECK(err_code);
    nrf_drv_twi_enable(&amp;twi_instance);
}

float read_temperature(void) {
    uint8_t reg[2] = {0x05, 0x00};
    uint8_t temp_data[2] = {0};

    nrf_drv_twi_tx(&amp;twi_instance, MCP9804_ADDRESS, reg, sizeof(reg), true);
    nrf_delay_ms(10);
    nrf_drv_twi_rx(&amp;twi_instance, MCP9804_ADDRESS, temp_data, sizeof(temp_data));

    int16_t temp_raw = (temp_data[0] &lt;&lt; 8) | temp_data[1];
    temp_raw &amp;= 0x0FFF;  // Mask for useful 12 bits
    float temperature = temp_raw / 16.0;

    return temperature;
}</code></pre>

<p><strong>SPI Lab: Communication with TC72</strong></p>

<p>The second lab consisted of interfacing an SPI temperature sensor.</p>

<p><strong>SPI configuration</strong>:</p>
<ul>
<li>Mode 1 (CPOL=0, CPHA=1)</li>
<li>Frequency: 125 kHz</li>
<li>CS (Chip Select): P0.31, manually controlled</li>
<li>MOSI: P0.28, MISO: P0.29, SCK: P0.30</li>
</ul>

<p><strong>Communication protocol</strong>:</p>
<ol>
<li>Initialization: write 0x80, 0x04 for continuous conversion mode</li>
<li>Reading: send command 0x02, receive 3 bytes</li>
<li>Temperature data processing</li>
</ol>

<p><strong>SPI code excerpt</strong>:</p>

<pre><code class="language-c">#define SPI_CS_PIN    NRF_GPIO_PIN_MAP(0,31)
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
    APP_ERROR_CHECK(nrf_drv_spi_init(&amp;spi, &amp;spi_config, spi_event_handler, NULL));
}

void tc_init(void) {
    nrf_gpio_cfg_output(SPI_CS_PIN);
    nrf_gpio_pin_clear(SPI_CS_PIN);
    spi_init();
    uint8_t data_to_send[2] = {0x80, 0x04}; // Continuous conversion
    nrf_gpio_pin_set(SPI_CS_PIN);
    spi_send(data_to_send, 2, NULL, 0);
    nrf_gpio_pin_clear(SPI_CS_PIN);
}</code></pre>

<h3 class="section-title">Difficulties encountered</h3>

<p><strong>SPI Chip Select management</strong>:
The CS must be toggled manually (not handled automatically by the driver). Forgetting to toggle the CS caused a complete loss of communication.</p>

<p><strong>I2C timing</strong>:
The delays between transmission and reception are critical. A delay that was too short resulted in corrupted data.</p>

<p><strong>Debugging</strong>:
Using printf via UART to display the read values. Serial port configuration was required in sdk_config.h.</p>

<hr/>

<h2>PART C - Detailed Technical Aspects</h2>

<h3 class="section-title">1. Serial Communication Buses</h3>

<p><strong>Comparison of the main buses</strong>:</p>

<table>
<thead>
<tr><th>Characteristic</th><th>I2C</th><th>SPI</th><th>UART</th></tr>
</thead>
<tbody>
<tr><td>Wires</td><td>2 (SDA, SCL)</td><td>4 (MOSI, MISO, SCK, CS)</td><td>2 (TX, RX)</td></tr>
<tr><td>Max speed</td><td>400 kHz (Fast), 3.4 MHz (High-Speed)</td><td>Several MHz</td><td>115200 baud typical</td></tr>
<tr><td>Master/Slave</td><td>Multi-master possible</td><td>One master, multiple slaves</td><td>Point to point</td></tr>
<tr><td>Addressing</td><td>7 or 10-bit address</td><td>Physical Chip Select</td><td>No address</td></tr>
<tr><td>Complexity</td><td>Medium</td><td>Simple</td><td>Very simple</td></tr>
<tr><td>Distance</td><td>Short (&lt; 1 m)</td><td>Very short</td><td>Medium (a few meters)</td></tr>
</tbody>
</table>

<h3 class="section-title">2. I2C Protocol (Inter-Integrated Circuit)</h3>

<p><strong>Operating principle</strong>:</p>

<p>I2C uses two bidirectional lines:</p>
<ul>
<li><strong>SDA</strong> (Serial Data): data transmission</li>
<li><strong>SCL</strong> (Serial Clock): clock generated by the master</li>
</ul>

<p><strong>START and STOP conditions</strong>:</p>
<ul>
<li>START: SDA transitions from HIGH to LOW while SCL is HIGH</li>
<li>STOP: SDA transitions from LOW to HIGH while SCL is HIGH</li>
</ul>

<p><strong>Communication frame</strong>:</p>
<ol>
<li>START condition</li>
<li>Slave address (7 bits) + R/W bit</li>
<li>ACK (acknowledgement) bit from the slave</li>
<li>Data (8 bits)</li>
<li>ACK bit</li>
<li>STOP condition</li>
</ol>

<p><strong>Advantages</strong>:</p>
<ul>
<li>Only 2 wires for multiple peripherals</li>
<li>Software addressing (no additional CS needed)</li>
<li>Collision detection in multi-master mode</li>
</ul>

<p><strong>Disadvantages</strong>:</p>
<ul>
<li>Limited speed</li>
<li>Pull-up resistors required</li>
<li>Parasitic capacitance limits cable length</li>
</ul>

<h3 class="section-title">3. SPI Protocol (Serial Peripheral Interface)</h3>

<p><strong>SPI signals</strong>:</p>
<ul>
<li><strong>MOSI</strong> (Master Out Slave In): data from master to slave</li>
<li><strong>MISO</strong> (Master In Slave Out): data from slave to master</li>
<li><strong>SCK</strong> (Serial Clock): clock generated by the master</li>
<li><strong>CS</strong> (Chip Select): slave selection (active low)</li>
</ul>

<p><strong>SPI modes</strong> (4 modes based on CPOL and CPHA):</p>

<table>
<thead>
<tr><th>Mode</th><th>CPOL</th><th>CPHA</th><th>Description</th></tr>
</thead>
<tbody>
<tr><td>0</td><td>0</td><td>0</td><td>Clock idle at 0, sampling on rising edge</td></tr>
<tr><td>1</td><td>0</td><td>1</td><td>Clock idle at 0, sampling on falling edge</td></tr>
<tr><td>2</td><td>1</td><td>0</td><td>Clock idle at 1, sampling on falling edge</td></tr>
<tr><td>3</td><td>1</td><td>1</td><td>Clock idle at 1, sampling on rising edge</td></tr>
</tbody>
</table>

<p><strong>Advantages</strong>:</p>
<ul>
<li>Full-duplex communication (simultaneous in both directions)</li>
<li>High speed (up to tens of MHz)</li>
<li>Simple to implement (no complex protocol)</li>
</ul>

<p><strong>Disadvantages</strong>:</p>
<ul>
<li>Number of wires increases with the number of slaves (one CS per slave)</li>
<li>No acknowledgement mechanism (ACK)</li>
<li>No built-in error detection</li>
</ul>

<h3 class="section-title">4. Clock Management in Microcontrollers</h3>

<p>Modern microcontrollers have multiple clock sources to optimize performance and power consumption.</p>

<p><strong>nRF52832 clock sources</strong>:</p>

<table>
<thead>
<tr><th>Clock</th><th>Frequency</th><th>Accuracy</th><th>Power Consumption</th><th>Usage</th></tr>
</thead>
<tbody>
<tr><td>Internal HFCLK</td><td>64 MHz</td><td>+/-5%</td><td>High</td><td>CPU, fast peripherals</td></tr>
<tr><td>External HFCLK (crystal)</td><td>64 MHz</td><td>+/-20 ppm</td><td>Medium</td><td>Bluetooth, precision</td></tr>
<tr><td>Internal LFCLK</td><td>32.768 kHz</td><td>+/-5%</td><td>Low</td><td>RTC, low-speed timers</td></tr>
<tr><td>External LFCLK (crystal)</td><td>32.768 kHz</td><td>+/-20 ppm</td><td>Very low</td><td>Precise RTC, sleep modes</td></tr>
</tbody>
</table>

<p><strong>Clock dividers</strong>:
Each peripheral can have its own divider to adjust the frequency.
Example: SPI at 125 kHz derived from HFCLK 64 MHz (divider 512).</p>

<p><strong>Impact on power consumption</strong>:</p>
<ul>
<li>Active mode (64 MHz): ~5 mA</li>
<li>Sleep mode (32 kHz): a few uA</li>
<li>Fast transition between modes to save energy</li>
</ul>

<h3 class="section-title">5. DMA (Direct Memory Access)</h3>

<p>DMA enables data transfers between peripherals and memory without CPU intervention.</p>

<p><strong>Advantages</strong>:</p>
<ul>
<li>CPU free for other tasks</li>
<li>Fast and efficient transfers</li>
<li>Reduces power consumption (CPU can remain in sleep)</li>
</ul>

<p><strong>Typical use cases</strong>:</p>
<ul>
<li>Continuous UART reception (circular buffer)</li>
<li>Multi-channel ADC acquisition</li>
<li>SPI transfers of large data volumes</li>
</ul>

<p><strong>DMA configuration for SPI</strong>:</p>
<ul>
<li>Source buffer in memory</li>
<li>SPI peripheral as destination</li>
<li>Interrupt generation at end of transfer</li>
</ul>

<h3 class="section-title">6. Power Management (Low Power)</h3>

<p><strong>nRF52832 operating modes</strong>:</p>

<table>
<thead>
<tr><th>Mode</th><th>Consumption</th><th>CPU State</th><th>Active Peripherals</th><th>Wake-up</th></tr>
</thead>
<tbody>
<tr><td>Active</td><td>5-15 mA</td><td>Running</td><td>All</td><td>N/A</td></tr>
<tr><td>Sleep</td><td>1-2 uA</td><td>Halt</td><td>RTC, GPIO</td><td>Interrupt, timer</td></tr>
<tr><td>Deep Sleep</td><td>&lt; 1 uA</td><td>Halt</td><td>None</td><td>External reset</td></tr>
</tbody>
</table>

<p><strong>Energy saving techniques</strong>:</p>
<ul>
<li>Use interrupts rather than polling</li>
<li>Disable unused peripherals</li>
<li>Reduce clock frequency when possible</li>
<li>Use low-frequency timers (LFCLK)</li>
<li>Sleep between events</li>
</ul>

<p><strong>Typical cycle example</strong>:</p>
<ol>
<li>Wake-up by timer interrupt (every second)</li>
<li>I2C sensor reading (10 ms active)</li>
<li>Data processing (5 ms active)</li>
<li>Return to sleep (985 ms at a few uA)</li>
<li>Average consumption: ~50 uA instead of 5 mA continuous</li>
</ol>

<h3 class="section-title">7. Logic Level Shifting</h3>

<p><strong>The problem</strong>:
Different components operate at different voltage levels (5V, 3.3V, 1.8V).</p>

<p><strong>Solutions</strong>:</p>
<ul>
<li><strong>Resistive voltage divider</strong>: simple but only works for 5V to 3.3V</li>
<li><strong>MOSFET transistor</strong>: bidirectional for I2C</li>
<li><strong>Dedicated ICs</strong>: TXS0108E (8 channels, bidirectional)</li>
<li><strong>74LVCxx buffer</strong>: conversion with isolation</li>
</ul>

<p><strong>INSA-BLE board</strong>:
Operates at 3.3V. Direct connection to 3.3V sensors. To interface with 5V devices (e.g., Arduino), level shifting is required.</p>

<hr/>

<h2>PART D - Reflective Analysis and Perspectives</h2>

<h3 class="section-title">Skills acquired</h3>

<p><strong>Low-level embedded programming</strong>:
This course reinforced C programming for embedded systems, particularly register manipulation, interrupt management, and interfacing with hardware peripherals.</p>

<p><strong>Mastery of communication protocols</strong>:
Understanding the differences between I2C and SPI, knowing how to choose the right protocol based on constraints (number of wires, speed, power consumption), and correctly implementing transactions.</p>

<p><strong>Energy optimization</strong>:
Low-power techniques are essential for battery-powered connected objects. Knowing how to measure and reduce consumption is a key skill.</p>

<h3 class="section-title">Key takeaways</h3>

<p><strong>1. Communication bus selection</strong>:</p>
<ul>
<li>I2C: multiple sensors, few wires, moderate speed</li>
<li>SPI: high speed, full-duplex, more wires</li>
<li>UART: simple, point-to-point, universal</li>
</ul>

<p><strong>2. Rigorous hardware management</strong>:
Read datasheets carefully, respect timings, verify logic levels, correctly manage CS and ACK signals.</p>

<p><strong>3. Methodical debugging</strong>:
Oscilloscope to verify signals, printf to trace execution, logic analyzer to capture complete frames.</p>

<p><strong>4. Energy consumption</strong>:
Design with power consumption in mind from the start: sleep modes, interrupt-based wake-up, clock selection.</p>

<h3 class="section-title">Practical applications</h3>

<p><strong>Personal and professional projects</strong>:</p>

<p><strong>IoT connected objects</strong>:
The skills acquired are directly applicable to IoT projects: interfacing environmental sensors (temperature, humidity, pressure), optimizing battery life.</p>

<p><strong>Embedded IA for IoT project (S9)</strong>:
Using the nRF52832 for embedded machine learning applications with sensors (accelerometer, gyroscope).</p>

<p><strong>Instrumentation</strong>:
Designing multi-sensor data acquisition systems with serial communication to a PC or cloud.</p>

<h3 class="section-title">Limitations and future directions</h3>

<p><strong>Course limitations</strong>:</p>
<ul>
<li>Limited coverage of UART (yet widely used)</li>
<li>No CAN bus (important for automotive)</li>
<li>No USB (complex but ubiquitous)</li>
<li>Bluetooth only mentioned, not covered in depth</li>
</ul>

<p><strong>Future directions</strong>:</p>
<ul>
<li><strong>Industrial protocols</strong>: Modbus, Profibus, CAN, EtherCAT</li>
<li><strong>Wireless communication</strong>: Bluetooth, WiFi, LoRa, Zigbee</li>
<li><strong>High-speed interfaces</strong>: USB 2.0/3.0, Ethernet, PCIe</li>
<li><strong>Communication security</strong>: encryption, authentication</li>
<li><strong>Sensor networks</strong>: mesh topologies, routing, energy saving</li>
</ul>

<h3 class="section-title">Technological evolution</h3>

<p><strong>Current trends</strong>:</p>
<ul>
<li><strong>Increased integration</strong>: SoC with CPU + peripherals + radio</li>
<li><strong>Ultra-low power</strong>: nW for energy-harvesting sensors</li>
<li><strong>Unified protocols</strong>: Matter for IoT interoperability</li>
<li><strong>Edge computing</strong>: local processing with embedded AI</li>
</ul>

<p><strong>Impact of new standards</strong>:</p>
<ul>
<li>Bluetooth 5.0+: extended range, increased throughput</li>
<li>Thread and Matter: IoT standardization</li>
<li>MIPI I3C: evolution of I2C with speeds up to 12.5 MHz</li>
</ul>

<h3 class="section-title">Conclusion</h3>

<p>Digital communication buses are the nervous system of embedded systems. Mastering them is essential for interfacing sensors, actuators, and communication modules.</p>

<p>This course provided a solid foundation in I2C and SPI, with a practical approach on ARM microcontrollers. The nRF52832 board is representative of modern SoCs: powerful, low-power, with integrated connectivity.</p>

<p><strong>Complementarity with other courses</strong>:</p>
<ul>
<li><a href="./microcontroleur.html">Microcontroller - S6</a>: ARM Cortex-M architecture</li>
<li><a href="./langage-assemblage-arm.html">ARM Assembly Language - S6</a>: low-level ARM</li>
<li><a href="./embedded-ia-iot.html">Embedded IA for IoT - S9</a>: advanced applications</li>
<li><a href="./energy-connected-objects.html">Energy for Connected Objects - S9</a>: advanced optimization</li>
</ul>

<p><strong>Recommendations for further study</strong>:</p>
<ul>
<li>Study complete datasheets (nRF52, sensors)</li>
<li>Experiment with other buses (CAN, USB)</li>
<li>Measure actual power consumption with a precision ammeter</li>
<li>Develop complete projects integrating multiple sensors</li>
<li>Explore Bluetooth and WiFi stacks</li>
</ul>

<hr/>

<h2>Course Documents</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>I2C Protocol</h4>
      <p>Complete course on the I2C bus: operating principle, addressing, communication frame and implementation.</p>
      <embed src="/cours-pdf/S6/Elec-Fonctions-Numeriques/i2c.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Elec-Fonctions-Numeriques/i2c.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>SPI Protocol</h4>
      <p>Course on the SPI bus: master-slave principle, peripheral selection, clock modes and full-duplex communication.</p>
      <embed src="/cours-pdf/S6/Elec-Fonctions-Numeriques/spi.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Elec-Fonctions-Numeriques/spi.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>Low Power Design</h4>
      <p>Power consumption optimization techniques: sleep modes, clock gating, energy management in microcontrollers.</p>
      <embed src="/cours-pdf/S6/Elec-Fonctions-Numeriques/low-power.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Elec-Fonctions-Numeriques/low-power.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>Microcontroller, Clock and DMA</h4>
      <p>Microcontroller architecture: system clock management and direct memory access (DMA) for optimal performance.</p>
      <embed src="/cours-pdf/S6/Elec-Fonctions-Numeriques/microcontroleur-horloge-dma.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S6/Elec-Fonctions-Numeriques/microcontroleur-horloge-dma.pdf" target="_blank">Download</a></p>
    </div>
  </div>
</div>

<hr/>

</div>

<div class="back-nav">
    <a href="./my-courses-2022-2023.html" data-i18n-html="back-courses-2022-2023">&larr; Retour aux Cours 2022-2023</a>
</div>

<em class="lang-fr">Cours enseigne en 2022-2023 a l'INSA Toulouse, Departement Genie Electrique et Informatique.</em>
<em class="lang-en">Course taught in 2022-2023 at INSA Toulouse, Department of Electrical Engineering and Computer Science.</em>

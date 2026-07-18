---
layout: default
title: "Microcontrôleur - S6"
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

<div class="back-nav">
    <a href="./my-courses-2022-2023.html" data-i18n-html="back_courses_2022_2023">&#8592; Retour aux Cours 2022-2023</a>
</div>

<div class="lang-fr">

<h1>Microcontroleur - Semestre 6</h1>

<p><strong>Annee Universitaire</strong> : 2022-2023<br/>
<strong>Semestre</strong> : 6<br/>
<strong>Credits</strong> : 4 ECTS<br/>
<strong>Specialite</strong> : Systemes Embarques</p>

<hr/>

<h2>PART A - Presentation Generale du Cours</h2>

<h3 class="section-title">Vue d'ensemble</h3>

<p>Ce cours approfondit la programmation de microcontroleurs avec focus sur les STM32 (ARM Cortex-M3). Il couvre la configuration des peripheriques (GPIO, timers, ADC, UART), le developpement de drivers, et la gestion des interruptions. Le point culminant est le projet Voilier, un systeme embarque autonome integrant capteurs et actionneurs.</p>

<p><strong>Objectifs pedagogiques</strong> :</p>
<ul>
  <li>Maitriser la programmation en C embarque pour STM32</li>
  <li>Configurer les peripheriques via registres (GPIO, timers, ADC, UART)</li>
  <li>Developper des drivers reutilisables avec HAL (Hardware Abstraction Layer)</li>
  <li>Gerer les interruptions et le temps reel</li>
  <li>Concevoir un systeme embarque complet (projet Voilier)</li>
</ul>

<h3 class="section-title">Position dans le cursus</h3>

<p>Ce cours s'appuie sur :</p>
<ul>
  <li><strong>Langage C (S5)</strong> : bases de la programmation C</li>
  <li><strong>Architecture Informatique (S5)</strong> : fonctionnement processeur et memoire</li>
  <li><strong>Langage Assemblage ARM (S6)</strong> : comprehension bas niveau</li>
</ul>

<p>Il prepare aux applications :</p>
<ul>
  <li><strong>Systemes embarques temps reel</strong> : contraintes temporelles</li>
  <li><strong>IoT et objets connectes</strong> : capteurs, communication</li>
  <li><strong>Robotique et automatisation</strong> : controle moteurs, asservissement</li>
</ul>

<hr/>

<h2>PART B - Experience Personnelle et Contexte d'Apprentissage</h2>

<h3 class="section-title">Organisation et ressources</h3>

<p>Le module etait structure en deux parties complementaires :</p>

<p><strong>1. Cours et TDs</strong> :</p>
<ul>
  <li>Architecture STM32F103 (Cortex-M3, 72 MHz, 128 KB Flash, 20 KB RAM)</li>
  <li>Programmation des peripheriques via registres</li>
  <li>Developpement de drivers</li>
  <li>Gestion des interruptions et timers</li>
</ul>

<p><strong>2. Projet Voilier</strong> :</p>
<p>Conception d'un voilier autonome radiocommande avec :</p>
<ul>
  <li>Capteurs : girouette (anemometre), boussole, GPS</li>
  <li>Actionneurs : servo-moteurs (gouvernail, voile)</li>
  <li>Communication : liaison serie, telemetrie</li>
  <li>Controle : regulation automatique de cap</li>
</ul>

<p><strong>Environnement de developpement</strong> :</p>
<ul>
  <li><strong>IDE</strong> : Keil uVision</li>
  <li><strong>Carte</strong> : STM32F103RB (Nucleo-64 ou carte custom)</li>
  <li><strong>Programmation</strong> : ST-Link (SWD)</li>
  <li><strong>Debogage</strong> : breakpoints, watch, memoire</li>
</ul>

<h3 class="section-title">Deroulement du projet Voilier</h3>

<p><strong>Architecture du systeme</strong> :</p>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S6/microcontroleur/architecture-stm32.svg" alt="Architecture STM32" style="max-width: 600px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Architecture d'un microcontroleur STM32 - CPU ARM Cortex-M4 avec peripheriques</p>
</div>

<p>Le voilier autonome integre plusieurs sous-systemes :</p>

<table>
  <tr><th>Sous-systeme</th><th>Composants</th><th>Fonction</th></tr>
  <tr><td>Navigation</td><td>Girouette, boussole, GPS</td><td>Determiner position et orientation</td></tr>
  <tr><td>Controle</td><td>Servo-moteurs</td><td>Ajuster gouvernail et voile</td></tr>
  <tr><td>Communication</td><td>UART, radio</td><td>Telemetrie et commandes</td></tr>
  <tr><td>Alimentation</td><td>Batterie, regulateur</td><td>Autonomie energetique</td></tr>
</table>

<p><strong>Capteurs implementes</strong> :</p>

<p><strong>Girouette (anemometre)</strong> :</p>
<ul>
  <li>Mesure de la direction du vent</li>
  <li>Interface : potentiometre rotatif &rarr; ADC</li>
  <li>Resolution : 12 bits (0-4095) &rarr; 0-360 deg</li>
  <li>Calibration necessaire</li>
</ul>

<p><strong>Boussole electronique</strong> :</p>
<ul>
  <li>Mesure du cap (orientation)</li>
  <li>Interface : I2C ou SPI</li>
  <li>Donnees : azimut magnetique</li>
</ul>

<p><strong>Etapes de developpement</strong> :</p>

<p><strong>Etape 1 : Drivers de base</strong></p>

<p>Developpement de drivers modulaires pour chaque peripherique.</p>

<p><strong>Driver GPIO</strong> :</p>

<pre><code>typedef struct {
    GPIO_TypeDef * GPIO;      // Port (GPIOA, GPIOB, GPIOC...)
    char GPIO_Pin;            // Numero broche 0-15
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
    if (GPIOStructPtr-&gt;GPIO == GPIOA) {
        RCC-&gt;APB2ENR |= RCC_APB2ENR_IOPAEN;
    }

    // Configuration de la broche
    if(GPIOStructPtr-&gt;GPIO_Pin &lt;= 7) {
        GPIOStructPtr-&gt;GPIO-&gt;CRL &amp;= ~(0xF &lt;&lt; (4*GPIOStructPtr-&gt;GPIO_Pin));
        GPIOStructPtr-&gt;GPIO-&gt;CRL |= (GPIOStructPtr-&gt;GPIO_Conf &lt;&lt; (4*GPIOStructPtr-&gt;GPIO_Pin));
    }
    else {
        GPIOStructPtr-&gt;GPIO-&gt;CRH &amp;= ~(0xF &lt;&lt; (4*(GPIOStructPtr-&gt;GPIO_Pin % 8)));
        GPIOStructPtr-&gt;GPIO-&gt;CRH |= (GPIOStructPtr-&gt;GPIO_Conf &lt;&lt; (4*(GPIOStructPtr-&gt;GPIO_Pin % 8)));
    }
}

// Lecture d'une entree
int MyGPIO_Read(GPIO_TypeDef * GPIO, char GPIO_Pin) {
    return (GPIO-&gt;IDR &amp; (1 &lt;&lt; GPIO_Pin)) != 0 ? 1 : 0;
}

// Mise a 1
void MyGPIO_Set(GPIO_TypeDef * GPIO, char GPIO_Pin) {
    GPIO-&gt;BSRR = (1 &lt;&lt; GPIO_Pin);
}

// Mise a 0
void MyGPIO_Reset(GPIO_TypeDef * GPIO, char GPIO_Pin) {
    GPIO-&gt;BRR = (1 &lt;&lt; GPIO_Pin);
}

// Basculement
void MyGPIO_Toggle(GPIO_TypeDef * GPIO, char GPIO_Pin) {
    GPIO-&gt;ODR ^= (1 &lt;&lt; GPIO_Pin);
}</code></pre>

<p><strong>Etape 2 : Timers et PWM</strong></p>

<p>Configuration des timers pour generation PWM (controle servo-moteurs).</p>

<pre><code>// Initialisation Timer en mode PWM
void MyTimer_PWM_Init(TIM_TypeDef * Timer, int frequence) {
    // Activation horloge timer
    if (Timer == TIM2) {
        RCC-&gt;APB1ENR |= RCC_APB1ENR_TIM2EN;
    }

    // Configuration prescaler et periode
    Timer-&gt;PSC = 72 - 1;              // Prescaler (72 MHz / 72 = 1 MHz)
    Timer-&gt;ARR = 20000 - 1;           // Periode 20 ms (50 Hz pour servo)

    // Mode PWM sur canal 1
    Timer-&gt;CCMR1 |= TIM_CCMR1_OC1M_1 | TIM_CCMR1_OC1M_2;  // PWM mode 1
    Timer-&gt;CCMR1 |= TIM_CCMR1_OC1PE;  // Preload enable

    // Activation sortie
    Timer-&gt;CCER |= TIM_CCER_CC1E;

    // Demarrage timer
    Timer-&gt;CR1 |= TIM_CR1_CEN;
}

// Reglage rapport cyclique (duty cycle)
void MyTimer_SetDutyCycle(TIM_TypeDef * Timer, int channel, int duty) {
    if (channel == 1) {
        Timer-&gt;CCR1 = duty;  // Valeur de 1000 a 2000 us pour servo
    }
}</code></pre>

<p><strong>Commande de servo-moteur</strong> :</p>
<ul>
  <li>Position neutre : 1500 us</li>
  <li>Gauche max : 1000 us</li>
  <li>Droite max : 2000 us</li>
</ul>

<p><strong>Etape 3 : ADC pour girouette</strong></p>

<p>Lecture analogique de la position de la girouette.</p>

<pre><code>// Initialisation ADC
void MyADC_Init(ADC_TypeDef * ADC, char channel) {
    // Activation horloge ADC
    RCC-&gt;APB2ENR |= RCC_APB2ENR_ADC1EN;

    // Configuration ADC
    ADC-&gt;CR2 |= ADC_CR2_ADON;         // Activation ADC
    ADC-&gt;SQR3 = channel;              // Selection canal
    ADC-&gt;SMPR2 = 0x7 &lt;&lt; (3*channel);  // Temps echantillonnage 239,5 cycles
}

// Lecture ADC (bloquante)
int MyADC_Read(ADC_TypeDef * ADC) {
    ADC-&gt;CR2 |= ADC_CR2_ADON;         // Demarrage conversion
    while (!(ADC-&gt;SR &amp; ADC_SR_EOC));  // Attente fin conversion
    return ADC-&gt;DR;                   // Lecture resultat
}

// Conversion ADC -&gt; angle
int Girouette_GetAngle(void) {
    int raw = MyADC_Read(ADC1);
    return (raw * 360) / 4096;  // 12 bits -&gt; 0-360 deg
}</code></pre>

<p><strong>Etape 4 : UART pour telemetrie</strong></p>

<p>Communication serie pour envoyer donnees et recevoir commandes.</p>

<pre><code>// Initialisation UART
void MyUART_Init(USART_TypeDef * UART, int baudrate) {
    // Activation horloge
    if (UART == USART1) {
        RCC-&gt;APB2ENR |= RCC_APB2ENR_USART1EN;
    }

    // Configuration GPIO (TX/RX)
    // PA9 = TX (fonction alternative), PA10 = RX (input)

    // Configuration baudrate
    UART-&gt;BRR = 72000000 / baudrate;  // 72 MHz / 9600 bps

    // Activation TX et RX
    UART-&gt;CR1 |= USART_CR1_TE | USART_CR1_RE | USART_CR1_UE;
}

// Envoi d'un caractere
void MyUART_SendChar(USART_TypeDef * UART, char c) {
    while (!(UART-&gt;SR &amp; USART_SR_TXE));  // Attente buffer vide
    UART-&gt;DR = c;
}

// Reception d'un caractere
char MyUART_ReceiveChar(USART_TypeDef * UART) {
    while (!(UART-&gt;SR &amp; USART_SR_RXNE));  // Attente donnees disponibles
    return UART-&gt;DR;
}

// Envoi d'une chaine
void MyUART_SendString(USART_TypeDef * UART, char * str) {
    while (*str) {
        MyUART_SendChar(UART, *str++);
    }
}</code></pre>

<p><strong>Etape 5 : Regulation de cap</strong></p>

<p>Algorithme de controle pour maintenir un cap.</p>

<pre><code>// Structure de controle
typedef struct {
    int cap_consigne;      // Cap desire
    int cap_actuel;        // Cap mesure (boussole)
    int angle_vent;        // Direction du vent (girouette)
    int position_gouvernail;
    int position_voile;
} VoilierControl_TypeDef;

// Regulation simple (proportionnelle)
void Voilier_Regulate(VoilierControl_TypeDef * voilier) {
    // Calcul erreur de cap
    int erreur = voilier-&gt;cap_consigne - voilier-&gt;cap_actuel;

    // Normalisation erreur (-180 deg a +180 deg)
    if (erreur &gt; 180) erreur -= 360;
    if (erreur &lt; -180) erreur += 360;

    // Correction proportionnelle
    int correction = erreur * 5;  // Gain proportionnel

    // Limites
    if (correction &gt; 500) correction = 500;
    if (correction &lt; -500) correction = -500;

    // Application au gouvernail
    voilier-&gt;position_gouvernail = 1500 + correction;
    MyTimer_SetDutyCycle(TIM2, 1, voilier-&gt;position_gouvernail);

    // Ajustement voile selon vent
    int angle_voile = abs(voilier-&gt;angle_vent - voilier-&gt;cap_actuel);
    if (angle_voile &gt; 180) angle_voile = 360 - angle_voile;
    voilier-&gt;position_voile = 1000 + (angle_voile * 1000) / 180;
    MyTimer_SetDutyCycle(TIM3, 1, voilier-&gt;position_voile);
}</code></pre>

<p><strong>Etape 6 : Interruptions</strong></p>

<p>Gestion d'evenements asynchrones (reception UART, timers).</p>

<pre><code>// Configuration interruption UART
void MyUART_EnableIT(USART_TypeDef * UART) {
    UART-&gt;CR1 |= USART_CR1_RXNEIE;  // Interruption reception
    NVIC_EnableIRQ(USART1_IRQn);
    NVIC_SetPriority(USART1_IRQn, 1);
}

// Handler interruption UART
void USART1_IRQHandler(void) {
    if (USART1-&gt;SR &amp; USART_SR_RXNE) {
        char received = USART1-&gt;DR;
        // Traitement commande
        if (received == 'L') {
            // Virer a gauche
        } else if (received == 'R') {
            // Virer a droite
        }
    }
}

// Configuration interruption timer
void MyTimer_EnableIT(TIM_TypeDef * Timer, int periode_ms) {
    Timer-&gt;DIER |= TIM_DIER_UIE;  // Interruption update
    NVIC_EnableIRQ(TIM2_IRQn);
}

// Handler interruption timer (tache periodique)
void TIM2_IRQHandler(void) {
    if (TIM2-&gt;SR &amp; TIM_SR_UIF) {
        TIM2-&gt;SR &amp;= ~TIM_SR_UIF;  // Clear flag

        // Tache periodique (ex: lecture capteurs, regulation)
        Voilier_Regulate(&amp;voilier);
    }
}</code></pre>

<h3 class="section-title">Difficultes rencontrees</h3>

<p><strong>Configuration des registres</strong> :<br/>
Les datasheets STM32 sont volumineuses (&gt;1000 pages). Il faut comprendre chaque bit des registres de configuration. Erreur frequente : oublier d'activer l'horloge du peripherique (RCC).</p>

<p><strong>Timing et interruptions</strong> :<br/>
Conflits entre taches : une interruption trop longue bloque les autres. Necessite de priorites bien reglees et de handlers courts.</p>

<p><strong>Calibration des capteurs</strong> :<br/>
La girouette necessite une calibration (offset, linearite). La boussole doit etre compensee en perturbations magnetiques.</p>

<p><strong>Debogage materiel</strong> :<br/>
Problemes parfois difficiles a diagnostiquer : cablage, alimentation, interferences. Oscilloscope et analyseur logique indispensables.</p>

<hr/>

<h2>PART C - Aspects Techniques Detailles</h2>

<h3 class="section-title">1. Architecture STM32F103</h3>

<p><strong>Caracteristiques principales</strong> :</p>

<table>
  <tr><th>Composant</th><th>Specification</th></tr>
  <tr><td>CPU</td><td>ARM Cortex-M3, 32 bits, 72 MHz</td></tr>
  <tr><td>Flash</td><td>128 KB (programme)</td></tr>
  <tr><td>RAM</td><td>20 KB (donnees)</td></tr>
  <tr><td>GPIO</td><td>51 broches I/O</td></tr>
  <tr><td>Timers</td><td>4 timers 16 bits avances</td></tr>
  <tr><td>ADC</td><td>2 ADC 12 bits, 16 canaux</td></tr>
  <tr><td>Communication</td><td>3 USART, 2 SPI, 2 I2C, USB, CAN</td></tr>
</table>

<p><strong>Organisation memoire</strong> :</p>

<table>
  <tr><th>Zone</th><th>Adresses</th><th>Usage</th></tr>
  <tr><td>Flash</td><td>0x08000000 - 0x0801FFFF</td><td>Code programme</td></tr>
  <tr><td>SRAM</td><td>0x20000000 - 0x20004FFF</td><td>Variables, pile</td></tr>
  <tr><td>Peripheriques</td><td>0x40000000 - 0x5FFFFFFF</td><td>Registres memory-mapped</td></tr>
  <tr><td>Systeme</td><td>0xE0000000 - 0xE00FFFFF</td><td>NVIC, SysTick</td></tr>
</table>

<h3 class="section-title">2. GPIO (General Purpose Input/Output)</h3>

<p><strong>Registres GPIO</strong> :</p>

<p>Chaque port (A, B, C, D) dispose de registres de configuration et de controle.</p>

<table>
  <tr><th>Registre</th><th>Fonction</th></tr>
  <tr><td>GPIOx_CRL</td><td>Configuration broches 0-7 (4 bits par broche)</td></tr>
  <tr><td>GPIOx_CRH</td><td>Configuration broches 8-15</td></tr>
  <tr><td>GPIOx_IDR</td><td>Input Data Register (lecture)</td></tr>
  <tr><td>GPIOx_ODR</td><td>Output Data Register (ecriture)</td></tr>
  <tr><td>GPIOx_BSRR</td><td>Bit Set/Reset Register (atomique)</td></tr>
  <tr><td>GPIOx_BRR</td><td>Bit Reset Register</td></tr>
</table>

<p><strong>Configuration d'une broche</strong> :</p>

<p>Chaque broche necessite 4 bits de configuration : MODE (2 bits) + CNF (2 bits).</p>

<table>
  <tr><th>MODE</th><th>CNF</th><th>Configuration</th></tr>
  <tr><td>00</td><td>01</td><td>Input floating</td></tr>
  <tr><td>00</td><td>10</td><td>Input pull-down/up</td></tr>
  <tr><td>01</td><td>00</td><td>Output push-pull 10 MHz</td></tr>
  <tr><td>10</td><td>00</td><td>Output push-pull 2 MHz</td></tr>
  <tr><td>11</td><td>00</td><td>Output push-pull 50 MHz</td></tr>
  <tr><td>11</td><td>10</td><td>Alternate function push-pull</td></tr>
</table>

<h3 class="section-title">3. Timers</h3>

<p><strong>Modes de fonctionnement</strong> :</p>

<p>Les timers STM32 sont polyvalents :</p>

<p><strong>Mode compteur simple</strong> :</p>
<ul>
  <li>Compte de 0 a ARR (Auto-Reload Register)</li>
  <li>Genere interruption a debordement</li>
  <li>Utilise pour delais, taches periodiques</li>
</ul>

<p><strong>Mode PWM</strong> :</p>
<ul>
  <li>Compare compteur (CNT) avec valeur de comparaison (CCR)</li>
  <li>Sortie HIGH si CNT &lt; CCR, LOW sinon</li>
  <li>Rapport cyclique = CCR / ARR</li>
</ul>

<p><strong>Mode capture</strong> :</p>
<ul>
  <li>Capture valeur CNT sur evenement externe</li>
  <li>Mesure de frequence, duree d'impulsion</li>
</ul>

<p><strong>Registres principaux</strong> :</p>

<table>
  <tr><th>Registre</th><th>Fonction</th></tr>
  <tr><td>TIMx_CR1</td><td>Control Register (activation, mode comptage)</td></tr>
  <tr><td>TIMx_PSC</td><td>Prescaler (diviseur frequence)</td></tr>
  <tr><td>TIMx_ARR</td><td>Auto-Reload (periode)</td></tr>
  <tr><td>TIMx_CNT</td><td>Compteur actuel</td></tr>
  <tr><td>TIMx_CCR1-4</td><td>Capture/Compare (PWM duty cycle)</td></tr>
  <tr><td>TIMx_CCMR1-2</td><td>Configuration canaux (PWM mode)</td></tr>
  <tr><td>TIMx_CCER</td><td>Activation sorties</td></tr>
</table>

<p><strong>Calcul de frequence PWM</strong> :</p>

<p>Frequence PWM = Horloge / (PSC + 1) / (ARR + 1)</p>

<p>Exemple : 72 MHz / 72 / 20000 = 50 Hz (servo-moteur)</p>

<h3 class="section-title">4. ADC (Convertisseur Analogique-Numerique)</h3>

<p><strong>Caracteristiques ADC STM32</strong> :</p>
<ul>
  <li>Resolution : 12 bits (0-4095)</li>
  <li>Temps de conversion : quelques us</li>
  <li>Modes : simple, continu, scan (multicanaux)</li>
  <li>Declenchement : logiciel, timer, externe</li>
</ul>

<p><strong>Configuration</strong> :</p>

<pre><code>// Sequence de conversion
ADC1-&gt;SQR1 = (nombre_conversions - 1) &lt;&lt; 20;  // Longueur sequence
ADC1-&gt;SQR3 = canal;                            // Premier canal

// Temps d'echantillonnage
ADC1-&gt;SMPR2 = 0x7 &lt;&lt; (3 * canal);  // 239,5 cycles (max precision)

// Demarrage conversion
ADC1-&gt;CR2 |= ADC_CR2_ADON;  // Activation + start</code></pre>

<p><strong>Modes d'acquisition</strong> :</p>

<table>
  <tr><th>Mode</th><th>Description</th></tr>
  <tr><td>Simple</td><td>Une conversion sur commande</td></tr>
  <tr><td>Continu</td><td>Conversions en boucle</td></tr>
  <tr><td>Scan</td><td>Plusieurs canaux en sequence</td></tr>
  <tr><td>Discontinu</td><td>Sous-groupes de canaux</td></tr>
</table>

<h3 class="section-title">5. UART/USART</h3>

<p><strong>Parametres de communication</strong> :</p>

<table>
  <tr><th>Parametre</th><th>Valeur typique</th></tr>
  <tr><td>Baudrate</td><td>9600, 115200 bps</td></tr>
  <tr><td>Bits de donnees</td><td>8 bits</td></tr>
  <tr><td>Bit de parite</td><td>Aucun</td></tr>
  <tr><td>Bits de stop</td><td>1 bit</td></tr>
</table>

<p><strong>Calcul du registre BRR</strong> :</p>

<p>BRR = Horloge_peripherique / Baudrate</p>

<p>Exemple : 72 MHz / 115200 = 625</p>

<p><strong>Gestion du buffer</strong> :</p>

<p>Pour eviter la perte de donnees, utiliser :</p>
<ul>
  <li>Buffer circulaire logiciel</li>
  <li>Interruptions sur reception</li>
  <li>Controle de flux materiel (RTS/CTS)</li>
</ul>

<h3 class="section-title">6. Interruptions (NVIC)</h3>

<p><strong>Nested Vectored Interrupt Controller</strong> :</p>

<p>Le NVIC gere jusqu'a 68 interruptions avec 16 niveaux de priorite.</p>

<p><strong>Configuration</strong> :</p>

<pre><code>// Activation interruption
NVIC_EnableIRQ(USART1_IRQn);

// Priorite (0 = plus haute)
NVIC_SetPriority(USART1_IRQn, 2);

// Desactivation
NVIC_DisableIRQ(USART1_IRQn);</code></pre>

<p><strong>Priorites</strong> :</p>

<p>Plus le numero est faible, plus la priorite est haute. Une interruption de priorite plus haute peut preempter une interruption en cours.</p>

<p><strong>Bonnes pratiques</strong> :</p>
<ul>
  <li>Handlers courts et rapides</li>
  <li>Pas de printf ou delais dans ISR</li>
  <li>Utiliser des flags pour communication avec main</li>
  <li>Proteger variables partagees (volatile)</li>
</ul>

<h3 class="section-title">7. Horloge et RCC</h3>

<p><strong>Reset and Clock Control</strong> :</p>

<p>Le RCC configure les horloges et active les peripheriques.</p>

<p><strong>Sources d'horloge</strong> :</p>
<ul>
  <li>HSI : oscillateur interne 8 MHz (precision +/-1%)</li>
  <li>HSE : quartz externe 8 MHz (precision +/-50 ppm)</li>
  <li>PLL : multiplieur pour atteindre 72 MHz</li>
</ul>

<p><strong>Configuration typique</strong> :</p>

<p>HSE 8 MHz &rarr; PLL x9 &rarr; SYSCLK 72 MHz</p>

<p><strong>Activation peripheriques</strong> :</p>

<p>Chaque peripherique doit etre active via RCC avant utilisation :</p>

<pre><code>RCC-&gt;APB2ENR |= RCC_APB2ENR_IOPAEN;    // GPIO A
RCC-&gt;APB2ENR |= RCC_APB2ENR_USART1EN;  // USART1
RCC-&gt;APB1ENR |= RCC_APB1ENR_TIM2EN;    // Timer 2</code></pre>

<hr/>

<h2>PART D - Analyse Reflexive et Perspectives</h2>

<h3 class="section-title">Competences acquises</h3>

<p><strong>Programmation embarquee</strong> :<br/>
Maitrise de la programmation bas niveau en C, manipulation directe des registres, comprehension du fonctionnement materiel. Capacite a lire et interpreter des datasheets complexes.</p>

<p><strong>Developpement de drivers</strong> :<br/>
Conception de couches d'abstraction materielle (HAL) reutilisables. Structure modulaire du code, separation interface/implementation.</p>

<p><strong>Integration systeme</strong> :<br/>
Le projet Voilier a developpe la capacite a integrer plusieurs sous-systemes (capteurs, actionneurs, communication) dans une application coherente et fonctionnelle.</p>

<p><strong>Debogage materiel/logiciel</strong> :<br/>
Utilisation d'outils professionnels (oscilloscope, analyseur logique, debugger). Methodologie de diagnostic des problemes.</p>

<h3 class="section-title">Points cles a retenir</h3>

<p><strong>1. Toujours activer l'horloge</strong> :<br/>
Erreur n 1 : oublier RCC-&gt;APBxENR. Le peripherique ne fonctionne pas sans son horloge.</p>

<p><strong>2. Configuration complete</strong> :<br/>
GPIO, timers, ADC necessitent une configuration precise de nombreux bits. Bien lire la datasheet.</p>

<p><strong>3. Volatile pour registres</strong> :<br/>
Les registres materiels doivent etre declares volatile pour eviter l'optimisation du compilateur.</p>

<p><strong>4. Interruptions = handlers courts</strong> :<br/>
Traitement minimal dans ISR, report du travail dans la boucle principale via flags.</p>

<p><strong>5. Debogage methodique</strong> :<br/>
Commencer simple (LED blinking), ajouter progressivement la complexite. Tester chaque module separement avant integration.</p>

<h3 class="section-title">Retour d'experience projet Voilier</h3>

<p><strong>Aspects positifs</strong> :</p>
<ul>
  <li>Projet concret et motivant (systeme reel)</li>
  <li>Liberte de conception et d'implementation</li>
  <li>Travail en equipe avec repartition des taches</li>
  <li>Application directe de tous les concepts du cours</li>
</ul>

<p><strong>Defis techniques</strong> :</p>
<ul>
  <li>Calibration des capteurs (girouette non lineaire)</li>
  <li>Gestion du timing (regulation 50 Hz + telemetrie)</li>
  <li>Interferences electromagnetiques (moteurs &rarr; capteurs)</li>
  <li>Optimisation consommation (autonomie batterie)</li>
</ul>

<p><strong>Lecons apprises</strong> :</p>
<ul>
  <li>Importance de la modularite (drivers reutilisables)</li>
  <li>Tests unitaires avant integration globale</li>
  <li>Documentation du code (comprehension equipe)</li>
  <li>Version control (Git) pour travail collaboratif</li>
</ul>

<h3 class="section-title">Applications pratiques</h3>

<p><strong>Domotique</strong> :<br/>
Controle d'eclairage, chauffage, volets roulants. Communication sans fil (Zigbee, LoRa).</p>

<p><strong>Robotique</strong> :<br/>
Controle de moteurs, lecture de capteurs (ultrason, infrarouge), navigation autonome.</p>

<p><strong>IoT (Internet of Things)</strong> :<br/>
Objets connectes : thermostats, trackers, stations meteo. Communication WiFi, Bluetooth.</p>

<p><strong>Automobile</strong> :<br/>
ECU (Electronic Control Unit), capteurs ABS, airbags, injection moteur.</p>

<p><strong>Medical</strong> :<br/>
Dispositifs portables (glucometres, tensiometres), pompes a perfusion, stimulateurs cardiaques.</p>

<h3 class="section-title">Limites et ouvertures</h3>

<p><strong>Limites du cours</strong> :</p>
<ul>
  <li>Peu de communication sans fil (WiFi, Bluetooth)</li>
  <li>Pas de RTOS (Real-Time Operating System)</li>
  <li>Peu de traitement du signal (filtrage, FFT)</li>
  <li>Pas de securite (chiffrement, authentification)</li>
</ul>

<p><strong>Ouvertures vers</strong> :</p>
<ul>
  <li><strong>RTOS</strong> : FreeRTOS, gestion multitaches, synchronisation</li>
  <li><strong>Communication IoT</strong> : MQTT, CoAP, LoRaWAN</li>
  <li><strong>Traitement signal</strong> : filtrage numerique, FFT sur MCU</li>
  <li><strong>Bas niveau avance</strong> : DMA, low power modes, bootloaders</li>
  <li><strong>Machine Learning</strong> : TensorFlow Lite Micro pour MCU</li>
</ul>

<h3 class="section-title">Evolution technologique</h3>

<p><strong>Tendances actuelles</strong> :</p>
<ul>
  <li><strong>MCU 32 bits omnipresents</strong> : Cortex-M4, M7, RISC-V</li>
  <li><strong>Connectivite integree</strong> : WiFi, BLE, LoRa sur puce</li>
  <li><strong>IA embarquee</strong> : accelerateurs ML (Cortex-M55, NPU)</li>
  <li><strong>Securite renforcee</strong> : TrustZone, secure boot, crypto materiel</li>
  <li><strong>Ultra-basse consommation</strong> : nW pour IoT batterie 10 ans</li>
</ul>

<p><strong>Outils modernes</strong> :</p>
<ul>
  <li><strong>STM32CubeMX</strong> : generation automatique code initialisation</li>
  <li><strong>PlatformIO</strong> : IDE multiplateforme (VS Code)</li>
  <li><strong>Mbed OS</strong> : systeme d'exploitation pour ARM</li>
  <li><strong>Zephyr RTOS</strong> : RTOS open-source pour IoT</li>
</ul>

<h3 class="section-title">Conclusion</h3>

<p>Le cours Microcontroleur est fondamental pour tout ingenieur en systemes embarques. La maitrise de la programmation bas niveau et de l'interfacage materiel est essentielle dans un monde ou les objets connectes sont omnipresents.</p>

<p>Le projet Voilier est l'experience marquante du semestre : conception complete d'un systeme autonome integrant capteurs, actionneurs et controle temps reel. Les competences acquises (drivers, interruptions, peripheriques) sont directement transferables a l'industrie.</p>

<p><strong>Evolution des competences</strong> :<br/>
De la simple LED clignotante au voilier autonome, le parcours montre la progression : GPIO &rarr; timers &rarr; ADC &rarr; UART &rarr; integration systeme complet. Chaque brique s'ajoute pour construire des systemes de plus en plus complexes.</p>

<p><strong>Recommandations</strong> :</p>
<ul>
  <li>Pratiquer regulierement (petits projets personnels)</li>
  <li>Lire les datasheets en profondeur (indispensable)</li>
  <li>Utiliser oscilloscope et analyseur logique (debogage)</li>
  <li>Developper des drivers reutilisables (portfolio)</li>
  <li>Participer a des competitions (Coupe de Robotique, hackathons)</li>
</ul>

<p><strong>Liens avec les autres cours</strong> :</p>
<ul>
  <li><a href="./assemblage-arm-cortex.html">Langage Assemblage ARM - S6</a> : comprehension bas niveau</li>
  <li><a href="./electronique-fonctions-numeriques.html">Electronique Fonctions Numeriques - S6</a> : bus I2C/SPI</li>
  <li><a href="./architecture-materielle.html">Architecture Materielle - S6</a> : pipeline, cache</li>
  <li><a href="./temps-reel.html">Temps Reel - S8</a> : RTOS, ordonnancement</li>
  <li><a href="./embedded-ia-iot.html">Embedded IA for IoT - S9</a> : ML embarque</li>
</ul>

<hr/>

<h2>Documents de Cours</h2>

<p>Voici les supports de cours en PDF pour approfondir la programmation des microcontroleurs STM32 :</p>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>STM32 - Structures et Registres</h4>
      <p>Guide complet des structures C pour l'acces aux registres du STM32, configuration et utilisation des peripheriques.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S6/Microcontroleur/stm32-structures.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S6/Microcontroleur/stm32-structures.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Telecharger le PDF
        </a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>GPIO - Entrees/Sorties</h4>
      <p>Configuration des GPIO, modes d'entree/sortie, pull-up/pull-down et manipulation des broches avec pointeurs.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S6/Microcontroleur/gpio.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S6/Microcontroleur/gpio.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Telecharger le PDF
        </a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Interruptions</h4>
      <p>Gestion des interruptions, NVIC, priorites, handlers et bonnes pratiques de programmation temps reel.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S6/Microcontroleur/interruptions.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S6/Microcontroleur/interruptions.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Telecharger le PDF
        </a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Timers</h4>
      <p>Configuration et utilisation des timers pour generation de delais, comptage d'evenements et mesures temporelles.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S6/Microcontroleur/timers.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S6/Microcontroleur/timers.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Telecharger le PDF
        </a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>PWM - Modulation de Largeur d'Impulsion</h4>
      <p>Generation de signaux PWM pour commande de moteurs, LEDs et variation d'intensite avec les timers.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S6/Microcontroleur/pwm.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S6/Microcontroleur/pwm.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Telecharger le PDF
        </a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>ADC - Convertisseur Analogique-Numerique</h4>
      <p>Configuration de l'ADC, acquisition de signaux analogiques, modes de declenchement et utilisation avec DMA.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S6/Microcontroleur/adc.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S6/Microcontroleur/adc.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Telecharger le PDF
        </a>
      </p>
    </div>
  </div>
</div>

<hr/>

<p><em>Cours enseigne en 2022-2023 a l'INSA Toulouse, Departement Genie Electrique et Informatique.</em></p>

</div>

<div class="lang-en">

<h1>Microcontroller - Semester 6</h1>

<p><strong>Academic Year</strong>: 2022-2023<br/>
<strong>Semester</strong>: 6<br/>
<strong>Credits</strong>: 4 ECTS<br/>
<strong>Specialization</strong>: Embedded Systems</p>

<hr/>

<h2>PART A - General Course Overview</h2>

<h3 class="section-title">Overview</h3>

<p>This course deepens microcontroller programming with a focus on STM32 (ARM Cortex-M3). It covers peripheral configuration (GPIO, timers, ADC, UART), driver development, and interrupt management. The highlight is the Sailboat project, an autonomous embedded system integrating sensors and actuators.</p>

<p><strong>Learning objectives</strong>:</p>
<ul>
  <li>Master embedded C programming for STM32</li>
  <li>Configure peripherals via registers (GPIO, timers, ADC, UART)</li>
  <li>Develop reusable drivers with HAL (Hardware Abstraction Layer)</li>
  <li>Manage interrupts and real-time constraints</li>
  <li>Design a complete embedded system (Sailboat project)</li>
</ul>

<h3 class="section-title">Position in the curriculum</h3>

<p>This course builds upon:</p>
<ul>
  <li><strong>C Language (S5)</strong>: C programming fundamentals</li>
  <li><strong>Computer Architecture (S5)</strong>: processor and memory operation</li>
  <li><strong>ARM Assembly Language (S6)</strong>: low-level understanding</li>
</ul>

<p>It prepares for applications in:</p>
<ul>
  <li><strong>Real-time embedded systems</strong>: timing constraints</li>
  <li><strong>IoT and connected objects</strong>: sensors, communication</li>
  <li><strong>Robotics and automation</strong>: motor control, servo systems</li>
</ul>

<hr/>

<h2>PART B - Personal Experience and Learning Context</h2>

<h3 class="section-title">Organization and resources</h3>

<p>The module was structured in two complementary parts:</p>

<p><strong>1. Lectures and Tutorials</strong>:</p>
<ul>
  <li>STM32F103 architecture (Cortex-M3, 72 MHz, 128 KB Flash, 20 KB RAM)</li>
  <li>Peripheral programming via registers</li>
  <li>Driver development</li>
  <li>Interrupt and timer management</li>
</ul>

<p><strong>2. Sailboat Project</strong>:</p>
<p>Design of an autonomous radio-controlled sailboat with:</p>
<ul>
  <li>Sensors: wind vane (anemometer), compass, GPS</li>
  <li>Actuators: servo motors (rudder, sail)</li>
  <li>Communication: serial link, telemetry</li>
  <li>Control: automatic heading regulation</li>
</ul>

<p><strong>Development environment</strong>:</p>
<ul>
  <li><strong>IDE</strong>: Keil uVision</li>
  <li><strong>Board</strong>: STM32F103RB (Nucleo-64 or custom board)</li>
  <li><strong>Programming</strong>: ST-Link (SWD)</li>
  <li><strong>Debugging</strong>: breakpoints, watch, memory</li>
</ul>

<h3 class="section-title">Sailboat project development</h3>

<p><strong>System architecture</strong>:</p>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S6/microcontroleur/architecture-stm32.svg" alt="STM32 Architecture" style="max-width: 600px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: STM32 microcontroller architecture - ARM Cortex-M4 CPU with peripherals</p>
</div>

<p>The autonomous sailboat integrates several subsystems:</p>

<table>
  <tr><th>Subsystem</th><th>Components</th><th>Function</th></tr>
  <tr><td>Navigation</td><td>Wind vane, compass, GPS</td><td>Determine position and orientation</td></tr>
  <tr><td>Control</td><td>Servo motors</td><td>Adjust rudder and sail</td></tr>
  <tr><td>Communication</td><td>UART, radio</td><td>Telemetry and commands</td></tr>
  <tr><td>Power supply</td><td>Battery, regulator</td><td>Energy autonomy</td></tr>
</table>

<p><strong>Implemented sensors</strong>:</p>

<p><strong>Wind vane (anemometer)</strong>:</p>
<ul>
  <li>Measures wind direction</li>
  <li>Interface: rotary potentiometer &rarr; ADC</li>
  <li>Resolution: 12 bits (0-4095) &rarr; 0-360 deg</li>
  <li>Calibration required</li>
</ul>

<p><strong>Electronic compass</strong>:</p>
<ul>
  <li>Measures heading (orientation)</li>
  <li>Interface: I2C or SPI</li>
  <li>Data: magnetic azimuth</li>
</ul>

<p><strong>Development steps</strong>:</p>

<p><strong>Step 1: Basic drivers</strong></p>

<p>Development of modular drivers for each peripheral.</p>

<p><strong>GPIO Driver</strong>:</p>

<pre><code>typedef struct {
    GPIO_TypeDef * GPIO;      // Port (GPIOA, GPIOB, GPIOC...)
    char GPIO_Pin;            // Pin number 0-15
    char GPIO_Conf;           // Configuration
} MyGPIO_Struct_TypeDef;

// Configuration modes
#define In_Floating  0x4
#define In_PullUp    0x8
#define In_PullDown  0x8
#define Out_Ppull    0x2      // Push-pull
#define Out_OD       0x6      // Open-drain
#define AltOut_Ppull 0xA      // Alternate function

// GPIO initialization
void MyGPIO_Init(MyGPIO_Struct_TypeDef * GPIOStructPtr) {
    // Enable port clock
    if (GPIOStructPtr-&gt;GPIO == GPIOA) {
        RCC-&gt;APB2ENR |= RCC_APB2ENR_IOPAEN;
    }

    // Pin configuration
    if(GPIOStructPtr-&gt;GPIO_Pin &lt;= 7) {
        GPIOStructPtr-&gt;GPIO-&gt;CRL &amp;= ~(0xF &lt;&lt; (4*GPIOStructPtr-&gt;GPIO_Pin));
        GPIOStructPtr-&gt;GPIO-&gt;CRL |= (GPIOStructPtr-&gt;GPIO_Conf &lt;&lt; (4*GPIOStructPtr-&gt;GPIO_Pin));
    }
    else {
        GPIOStructPtr-&gt;GPIO-&gt;CRH &amp;= ~(0xF &lt;&lt; (4*(GPIOStructPtr-&gt;GPIO_Pin % 8)));
        GPIOStructPtr-&gt;GPIO-&gt;CRH |= (GPIOStructPtr-&gt;GPIO_Conf &lt;&lt; (4*(GPIOStructPtr-&gt;GPIO_Pin % 8)));
    }
}

// Read an input
int MyGPIO_Read(GPIO_TypeDef * GPIO, char GPIO_Pin) {
    return (GPIO-&gt;IDR &amp; (1 &lt;&lt; GPIO_Pin)) != 0 ? 1 : 0;
}

// Set to 1
void MyGPIO_Set(GPIO_TypeDef * GPIO, char GPIO_Pin) {
    GPIO-&gt;BSRR = (1 &lt;&lt; GPIO_Pin);
}

// Set to 0
void MyGPIO_Reset(GPIO_TypeDef * GPIO, char GPIO_Pin) {
    GPIO-&gt;BRR = (1 &lt;&lt; GPIO_Pin);
}

// Toggle
void MyGPIO_Toggle(GPIO_TypeDef * GPIO, char GPIO_Pin) {
    GPIO-&gt;ODR ^= (1 &lt;&lt; GPIO_Pin);
}</code></pre>

<p><strong>Step 2: Timers and PWM</strong></p>

<p>Timer configuration for PWM generation (servo motor control).</p>

<pre><code>// Timer initialization in PWM mode
void MyTimer_PWM_Init(TIM_TypeDef * Timer, int frequency) {
    // Enable timer clock
    if (Timer == TIM2) {
        RCC-&gt;APB1ENR |= RCC_APB1ENR_TIM2EN;
    }

    // Configure prescaler and period
    Timer-&gt;PSC = 72 - 1;              // Prescaler (72 MHz / 72 = 1 MHz)
    Timer-&gt;ARR = 20000 - 1;           // Period 20 ms (50 Hz for servo)

    // PWM mode on channel 1
    Timer-&gt;CCMR1 |= TIM_CCMR1_OC1M_1 | TIM_CCMR1_OC1M_2;  // PWM mode 1
    Timer-&gt;CCMR1 |= TIM_CCMR1_OC1PE;  // Preload enable

    // Enable output
    Timer-&gt;CCER |= TIM_CCER_CC1E;

    // Start timer
    Timer-&gt;CR1 |= TIM_CR1_CEN;
}

// Set duty cycle
void MyTimer_SetDutyCycle(TIM_TypeDef * Timer, int channel, int duty) {
    if (channel == 1) {
        Timer-&gt;CCR1 = duty;  // Value from 1000 to 2000 us for servo
    }
}</code></pre>

<p><strong>Servo motor control</strong>:</p>
<ul>
  <li>Neutral position: 1500 us</li>
  <li>Maximum left: 1000 us</li>
  <li>Maximum right: 2000 us</li>
</ul>

<p><strong>Step 3: ADC for wind vane</strong></p>

<p>Analog reading of the wind vane position.</p>

<pre><code>// ADC initialization
void MyADC_Init(ADC_TypeDef * ADC, char channel) {
    // Enable ADC clock
    RCC-&gt;APB2ENR |= RCC_APB2ENR_ADC1EN;

    // ADC configuration
    ADC-&gt;CR2 |= ADC_CR2_ADON;         // Enable ADC
    ADC-&gt;SQR3 = channel;              // Channel selection
    ADC-&gt;SMPR2 = 0x7 &lt;&lt; (3*channel);  // Sampling time 239.5 cycles
}

// ADC read (blocking)
int MyADC_Read(ADC_TypeDef * ADC) {
    ADC-&gt;CR2 |= ADC_CR2_ADON;         // Start conversion
    while (!(ADC-&gt;SR &amp; ADC_SR_EOC));  // Wait for end of conversion
    return ADC-&gt;DR;                   // Read result
}

// ADC to angle conversion
int WindVane_GetAngle(void) {
    int raw = MyADC_Read(ADC1);
    return (raw * 360) / 4096;  // 12 bits -&gt; 0-360 deg
}</code></pre>

<p><strong>Step 4: UART for telemetry</strong></p>

<p>Serial communication to send data and receive commands.</p>

<pre><code>// UART initialization
void MyUART_Init(USART_TypeDef * UART, int baudrate) {
    // Enable clock
    if (UART == USART1) {
        RCC-&gt;APB2ENR |= RCC_APB2ENR_USART1EN;
    }

    // GPIO configuration (TX/RX)
    // PA9 = TX (alternate function), PA10 = RX (input)

    // Baudrate configuration
    UART-&gt;BRR = 72000000 / baudrate;  // 72 MHz / 9600 bps

    // Enable TX and RX
    UART-&gt;CR1 |= USART_CR1_TE | USART_CR1_RE | USART_CR1_UE;
}

// Send a character
void MyUART_SendChar(USART_TypeDef * UART, char c) {
    while (!(UART-&gt;SR &amp; USART_SR_TXE));  // Wait for buffer empty
    UART-&gt;DR = c;
}

// Receive a character
char MyUART_ReceiveChar(USART_TypeDef * UART) {
    while (!(UART-&gt;SR &amp; USART_SR_RXNE));  // Wait for data available
    return UART-&gt;DR;
}

// Send a string
void MyUART_SendString(USART_TypeDef * UART, char * str) {
    while (*str) {
        MyUART_SendChar(UART, *str++);
    }
}</code></pre>

<p><strong>Step 5: Heading regulation</strong></p>

<p>Control algorithm to maintain a heading.</p>

<pre><code>// Control structure
typedef struct {
    int target_heading;    // Desired heading
    int current_heading;   // Measured heading (compass)
    int wind_angle;        // Wind direction (wind vane)
    int rudder_position;
    int sail_position;
} SailboatControl_TypeDef;

// Simple regulation (proportional)
void Sailboat_Regulate(SailboatControl_TypeDef * sailboat) {
    // Heading error calculation
    int error = sailboat-&gt;target_heading - sailboat-&gt;current_heading;

    // Error normalization (-180 deg to +180 deg)
    if (error &gt; 180) error -= 360;
    if (error &lt; -180) error += 360;

    // Proportional correction
    int correction = error * 5;  // Proportional gain

    // Limits
    if (correction &gt; 500) correction = 500;
    if (correction &lt; -500) correction = -500;

    // Apply to rudder
    sailboat-&gt;rudder_position = 1500 + correction;
    MyTimer_SetDutyCycle(TIM2, 1, sailboat-&gt;rudder_position);

    // Sail adjustment based on wind
    int sail_angle = abs(sailboat-&gt;wind_angle - sailboat-&gt;current_heading);
    if (sail_angle &gt; 180) sail_angle = 360 - sail_angle;
    sailboat-&gt;sail_position = 1000 + (sail_angle * 1000) / 180;
    MyTimer_SetDutyCycle(TIM3, 1, sailboat-&gt;sail_position);
}</code></pre>

<p><strong>Step 6: Interrupts</strong></p>

<p>Asynchronous event handling (UART reception, timers).</p>

<pre><code>// UART interrupt configuration
void MyUART_EnableIT(USART_TypeDef * UART) {
    UART-&gt;CR1 |= USART_CR1_RXNEIE;  // Receive interrupt
    NVIC_EnableIRQ(USART1_IRQn);
    NVIC_SetPriority(USART1_IRQn, 1);
}

// UART interrupt handler
void USART1_IRQHandler(void) {
    if (USART1-&gt;SR &amp; USART_SR_RXNE) {
        char received = USART1-&gt;DR;
        // Command processing
        if (received == 'L') {
            // Turn left
        } else if (received == 'R') {
            // Turn right
        }
    }
}

// Timer interrupt configuration
void MyTimer_EnableIT(TIM_TypeDef * Timer, int period_ms) {
    Timer-&gt;DIER |= TIM_DIER_UIE;  // Update interrupt
    NVIC_EnableIRQ(TIM2_IRQn);
}

// Timer interrupt handler (periodic task)
void TIM2_IRQHandler(void) {
    if (TIM2-&gt;SR &amp; TIM_SR_UIF) {
        TIM2-&gt;SR &amp;= ~TIM_SR_UIF;  // Clear flag

        // Periodic task (e.g.: sensor reading, regulation)
        Sailboat_Regulate(&amp;sailboat);
    }
}</code></pre>

<h3 class="section-title">Difficulties encountered</h3>

<p><strong>Register configuration</strong>:<br/>
STM32 datasheets are voluminous (&gt;1000 pages). Each bit of the configuration registers must be understood. Common mistake: forgetting to enable the peripheral clock (RCC).</p>

<p><strong>Timing and interrupts</strong>:<br/>
Task conflicts: an interrupt that takes too long blocks others. Well-tuned priorities and short handlers are necessary.</p>

<p><strong>Sensor calibration</strong>:<br/>
The wind vane requires calibration (offset, linearity). The compass must be compensated for magnetic disturbances.</p>

<p><strong>Hardware debugging</strong>:<br/>
Problems sometimes difficult to diagnose: wiring, power supply, interference. Oscilloscope and logic analyzer are essential.</p>

<hr/>

<h2>PART C - Detailed Technical Aspects</h2>

<h3 class="section-title">1. STM32F103 Architecture</h3>

<p><strong>Main specifications</strong>:</p>

<table>
  <tr><th>Component</th><th>Specification</th></tr>
  <tr><td>CPU</td><td>ARM Cortex-M3, 32-bit, 72 MHz</td></tr>
  <tr><td>Flash</td><td>128 KB (program)</td></tr>
  <tr><td>RAM</td><td>20 KB (data)</td></tr>
  <tr><td>GPIO</td><td>51 I/O pins</td></tr>
  <tr><td>Timers</td><td>4 advanced 16-bit timers</td></tr>
  <tr><td>ADC</td><td>2 x 12-bit ADC, 16 channels</td></tr>
  <tr><td>Communication</td><td>3 USART, 2 SPI, 2 I2C, USB, CAN</td></tr>
</table>

<p><strong>Memory organization</strong>:</p>

<table>
  <tr><th>Region</th><th>Addresses</th><th>Usage</th></tr>
  <tr><td>Flash</td><td>0x08000000 - 0x0801FFFF</td><td>Program code</td></tr>
  <tr><td>SRAM</td><td>0x20000000 - 0x20004FFF</td><td>Variables, stack</td></tr>
  <tr><td>Peripherals</td><td>0x40000000 - 0x5FFFFFFF</td><td>Memory-mapped registers</td></tr>
  <tr><td>System</td><td>0xE0000000 - 0xE00FFFFF</td><td>NVIC, SysTick</td></tr>
</table>

<h3 class="section-title">2. GPIO (General Purpose Input/Output)</h3>

<p><strong>GPIO Registers</strong>:</p>

<p>Each port (A, B, C, D) has configuration and control registers.</p>

<table>
  <tr><th>Register</th><th>Function</th></tr>
  <tr><td>GPIOx_CRL</td><td>Configuration for pins 0-7 (4 bits per pin)</td></tr>
  <tr><td>GPIOx_CRH</td><td>Configuration for pins 8-15</td></tr>
  <tr><td>GPIOx_IDR</td><td>Input Data Register (read)</td></tr>
  <tr><td>GPIOx_ODR</td><td>Output Data Register (write)</td></tr>
  <tr><td>GPIOx_BSRR</td><td>Bit Set/Reset Register (atomic)</td></tr>
  <tr><td>GPIOx_BRR</td><td>Bit Reset Register</td></tr>
</table>

<p><strong>Pin configuration</strong>:</p>

<p>Each pin requires 4 configuration bits: MODE (2 bits) + CNF (2 bits).</p>

<table>
  <tr><th>MODE</th><th>CNF</th><th>Configuration</th></tr>
  <tr><td>00</td><td>01</td><td>Input floating</td></tr>
  <tr><td>00</td><td>10</td><td>Input pull-down/up</td></tr>
  <tr><td>01</td><td>00</td><td>Output push-pull 10 MHz</td></tr>
  <tr><td>10</td><td>00</td><td>Output push-pull 2 MHz</td></tr>
  <tr><td>11</td><td>00</td><td>Output push-pull 50 MHz</td></tr>
  <tr><td>11</td><td>10</td><td>Alternate function push-pull</td></tr>
</table>

<h3 class="section-title">3. Timers</h3>

<p><strong>Operating modes</strong>:</p>

<p>STM32 timers are versatile:</p>

<p><strong>Simple counter mode</strong>:</p>
<ul>
  <li>Counts from 0 to ARR (Auto-Reload Register)</li>
  <li>Generates interrupt on overflow</li>
  <li>Used for delays, periodic tasks</li>
</ul>

<p><strong>PWM mode</strong>:</p>
<ul>
  <li>Compares counter (CNT) with compare value (CCR)</li>
  <li>Output HIGH if CNT &lt; CCR, LOW otherwise</li>
  <li>Duty cycle = CCR / ARR</li>
</ul>

<p><strong>Capture mode</strong>:</p>
<ul>
  <li>Captures CNT value on external event</li>
  <li>Frequency measurement, pulse duration</li>
</ul>

<p><strong>Main registers</strong>:</p>

<table>
  <tr><th>Register</th><th>Function</th></tr>
  <tr><td>TIMx_CR1</td><td>Control Register (enable, counting mode)</td></tr>
  <tr><td>TIMx_PSC</td><td>Prescaler (frequency divider)</td></tr>
  <tr><td>TIMx_ARR</td><td>Auto-Reload (period)</td></tr>
  <tr><td>TIMx_CNT</td><td>Current counter</td></tr>
  <tr><td>TIMx_CCR1-4</td><td>Capture/Compare (PWM duty cycle)</td></tr>
  <tr><td>TIMx_CCMR1-2</td><td>Channel configuration (PWM mode)</td></tr>
  <tr><td>TIMx_CCER</td><td>Output enable</td></tr>
</table>

<p><strong>PWM frequency calculation</strong>:</p>

<p>PWM Frequency = Clock / (PSC + 1) / (ARR + 1)</p>

<p>Example: 72 MHz / 72 / 20000 = 50 Hz (servo motor)</p>

<h3 class="section-title">4. ADC (Analog-to-Digital Converter)</h3>

<p><strong>STM32 ADC characteristics</strong>:</p>
<ul>
  <li>Resolution: 12 bits (0-4095)</li>
  <li>Conversion time: a few us</li>
  <li>Modes: single, continuous, scan (multi-channel)</li>
  <li>Trigger: software, timer, external</li>
</ul>

<p><strong>Configuration</strong>:</p>

<pre><code>// Conversion sequence
ADC1-&gt;SQR1 = (num_conversions - 1) &lt;&lt; 20;  // Sequence length
ADC1-&gt;SQR3 = channel;                       // First channel

// Sampling time
ADC1-&gt;SMPR2 = 0x7 &lt;&lt; (3 * channel);  // 239.5 cycles (max precision)

// Start conversion
ADC1-&gt;CR2 |= ADC_CR2_ADON;  // Enable + start</code></pre>

<p><strong>Acquisition modes</strong>:</p>

<table>
  <tr><th>Mode</th><th>Description</th></tr>
  <tr><td>Single</td><td>One conversion on demand</td></tr>
  <tr><td>Continuous</td><td>Looping conversions</td></tr>
  <tr><td>Scan</td><td>Multiple channels in sequence</td></tr>
  <tr><td>Discontinuous</td><td>Channel subgroups</td></tr>
</table>

<h3 class="section-title">5. UART/USART</h3>

<p><strong>Communication parameters</strong>:</p>

<table>
  <tr><th>Parameter</th><th>Typical value</th></tr>
  <tr><td>Baudrate</td><td>9600, 115200 bps</td></tr>
  <tr><td>Data bits</td><td>8 bits</td></tr>
  <tr><td>Parity bit</td><td>None</td></tr>
  <tr><td>Stop bits</td><td>1 bit</td></tr>
</table>

<p><strong>BRR register calculation</strong>:</p>

<p>BRR = Peripheral_Clock / Baudrate</p>

<p>Example: 72 MHz / 115200 = 625</p>

<p><strong>Buffer management</strong>:</p>

<p>To avoid data loss, use:</p>
<ul>
  <li>Software circular buffer</li>
  <li>Receive interrupts</li>
  <li>Hardware flow control (RTS/CTS)</li>
</ul>

<h3 class="section-title">6. Interrupts (NVIC)</h3>

<p><strong>Nested Vectored Interrupt Controller</strong>:</p>

<p>The NVIC manages up to 68 interrupts with 16 priority levels.</p>

<p><strong>Configuration</strong>:</p>

<pre><code>// Enable interrupt
NVIC_EnableIRQ(USART1_IRQn);

// Priority (0 = highest)
NVIC_SetPriority(USART1_IRQn, 2);

// Disable
NVIC_DisableIRQ(USART1_IRQn);</code></pre>

<p><strong>Priorities</strong>:</p>

<p>The lower the number, the higher the priority. A higher-priority interrupt can preempt a running interrupt.</p>

<p><strong>Best practices</strong>:</p>
<ul>
  <li>Short and fast handlers</li>
  <li>No printf or delays in ISR</li>
  <li>Use flags for communication with main loop</li>
  <li>Protect shared variables (volatile)</li>
</ul>

<h3 class="section-title">7. Clock and RCC</h3>

<p><strong>Reset and Clock Control</strong>:</p>

<p>The RCC configures clocks and enables peripherals.</p>

<p><strong>Clock sources</strong>:</p>
<ul>
  <li>HSI: internal 8 MHz oscillator (accuracy +/-1%)</li>
  <li>HSE: external 8 MHz crystal (accuracy +/-50 ppm)</li>
  <li>PLL: multiplier to reach 72 MHz</li>
</ul>

<p><strong>Typical configuration</strong>:</p>

<p>HSE 8 MHz &rarr; PLL x9 &rarr; SYSCLK 72 MHz</p>

<p><strong>Peripheral activation</strong>:</p>

<p>Each peripheral must be enabled via RCC before use:</p>

<pre><code>RCC-&gt;APB2ENR |= RCC_APB2ENR_IOPAEN;    // GPIO A
RCC-&gt;APB2ENR |= RCC_APB2ENR_USART1EN;  // USART1
RCC-&gt;APB1ENR |= RCC_APB1ENR_TIM2EN;    // Timer 2</code></pre>

<hr/>

<h2>PART D - Reflective Analysis and Outlook</h2>

<h3 class="section-title">Acquired skills</h3>

<p><strong>Embedded programming</strong>:<br/>
Mastery of low-level C programming, direct register manipulation, understanding of hardware operation. Ability to read and interpret complex datasheets.</p>

<p><strong>Driver development</strong>:<br/>
Design of reusable hardware abstraction layers (HAL). Modular code structure, interface/implementation separation.</p>

<p><strong>System integration</strong>:<br/>
The Sailboat project developed the ability to integrate multiple subsystems (sensors, actuators, communication) into a coherent and functional application.</p>

<p><strong>Hardware/software debugging</strong>:<br/>
Use of professional tools (oscilloscope, logic analyzer, debugger). Problem diagnosis methodology.</p>

<h3 class="section-title">Key takeaways</h3>

<p><strong>1. Always enable the clock</strong>:<br/>
Mistake #1: forgetting RCC-&gt;APBxENR. The peripheral will not work without its clock.</p>

<p><strong>2. Complete configuration</strong>:<br/>
GPIO, timers, ADC require precise configuration of many bits. Read the datasheet carefully.</p>

<p><strong>3. Volatile for registers</strong>:<br/>
Hardware registers must be declared volatile to prevent compiler optimization.</p>

<p><strong>4. Interrupts = short handlers</strong>:<br/>
Minimal processing in ISR, defer work to the main loop via flags.</p>

<p><strong>5. Methodical debugging</strong>:<br/>
Start simple (LED blinking), progressively add complexity. Test each module separately before integration.</p>

<h3 class="section-title">Sailboat project feedback</h3>

<p><strong>Positive aspects</strong>:</p>
<ul>
  <li>Concrete and motivating project (real system)</li>
  <li>Freedom in design and implementation</li>
  <li>Teamwork with task distribution</li>
  <li>Direct application of all course concepts</li>
</ul>

<p><strong>Technical challenges</strong>:</p>
<ul>
  <li>Sensor calibration (non-linear wind vane)</li>
  <li>Timing management (50 Hz regulation + telemetry)</li>
  <li>Electromagnetic interference (motors &rarr; sensors)</li>
  <li>Power consumption optimization (battery life)</li>
</ul>

<p><strong>Lessons learned</strong>:</p>
<ul>
  <li>Importance of modularity (reusable drivers)</li>
  <li>Unit testing before global integration</li>
  <li>Code documentation (team understanding)</li>
  <li>Version control (Git) for collaborative work</li>
</ul>

<h3 class="section-title">Practical applications</h3>

<p><strong>Home automation</strong>:<br/>
Lighting control, heating, shutters. Wireless communication (Zigbee, LoRa).</p>

<p><strong>Robotics</strong>:<br/>
Motor control, sensor reading (ultrasonic, infrared), autonomous navigation.</p>

<p><strong>IoT (Internet of Things)</strong>:<br/>
Connected objects: thermostats, trackers, weather stations. WiFi, Bluetooth communication.</p>

<p><strong>Automotive</strong>:<br/>
ECU (Electronic Control Unit), ABS sensors, airbags, engine injection.</p>

<p><strong>Medical</strong>:<br/>
Portable devices (glucometers, blood pressure monitors), infusion pumps, cardiac pacemakers.</p>

<h3 class="section-title">Limitations and future directions</h3>

<p><strong>Course limitations</strong>:</p>
<ul>
  <li>Little wireless communication (WiFi, Bluetooth)</li>
  <li>No RTOS (Real-Time Operating System)</li>
  <li>Little signal processing (filtering, FFT)</li>
  <li>No security (encryption, authentication)</li>
</ul>

<p><strong>Future directions</strong>:</p>
<ul>
  <li><strong>RTOS</strong>: FreeRTOS, multitasking, synchronization</li>
  <li><strong>IoT communication</strong>: MQTT, CoAP, LoRaWAN</li>
  <li><strong>Signal processing</strong>: digital filtering, FFT on MCU</li>
  <li><strong>Advanced low-level</strong>: DMA, low power modes, bootloaders</li>
  <li><strong>Machine Learning</strong>: TensorFlow Lite Micro for MCU</li>
</ul>

<h3 class="section-title">Technological evolution</h3>

<p><strong>Current trends</strong>:</p>
<ul>
  <li><strong>32-bit MCUs everywhere</strong>: Cortex-M4, M7, RISC-V</li>
  <li><strong>Integrated connectivity</strong>: WiFi, BLE, LoRa on chip</li>
  <li><strong>Embedded AI</strong>: ML accelerators (Cortex-M55, NPU)</li>
  <li><strong>Enhanced security</strong>: TrustZone, secure boot, hardware crypto</li>
  <li><strong>Ultra-low power</strong>: nW for 10-year battery IoT</li>
</ul>

<p><strong>Modern tools</strong>:</p>
<ul>
  <li><strong>STM32CubeMX</strong>: automatic initialization code generation</li>
  <li><strong>PlatformIO</strong>: cross-platform IDE (VS Code)</li>
  <li><strong>Mbed OS</strong>: operating system for ARM</li>
  <li><strong>Zephyr RTOS</strong>: open-source RTOS for IoT</li>
</ul>

<h3 class="section-title">Conclusion</h3>

<p>The Microcontroller course is fundamental for any embedded systems engineer. Mastery of low-level programming and hardware interfacing is essential in a world where connected objects are ubiquitous.</p>

<p>The Sailboat project is the semester's defining experience: complete design of an autonomous system integrating sensors, actuators, and real-time control. The acquired skills (drivers, interrupts, peripherals) are directly transferable to industry.</p>

<p><strong>Skills progression</strong>:<br/>
From a simple blinking LED to an autonomous sailboat, the journey shows the progression: GPIO &rarr; timers &rarr; ADC &rarr; UART &rarr; complete system integration. Each building block adds up to create increasingly complex systems.</p>

<p><strong>Recommendations</strong>:</p>
<ul>
  <li>Practice regularly (small personal projects)</li>
  <li>Read datasheets thoroughly (essential)</li>
  <li>Use oscilloscope and logic analyzer (debugging)</li>
  <li>Develop reusable drivers (portfolio)</li>
  <li>Participate in competitions (Robotics Cup, hackathons)</li>
</ul>

<p><strong>Links with other courses</strong>:</p>
<ul>
  <li><a href="./assemblage-arm-cortex.html">ARM Assembly Language - S6</a>: low-level understanding</li>
  <li><a href="./electronique-fonctions-numeriques.html">Digital Electronics Functions - S6</a>: I2C/SPI bus</li>
  <li><a href="./architecture-materielle.html">Hardware Architecture - S6</a>: pipeline, cache</li>
  <li><a href="./temps-reel.html">Real-Time Systems - S8</a>: RTOS, scheduling</li>
  <li><a href="./embedded-ia-iot.html">Embedded AI for IoT - S9</a>: embedded ML</li>
</ul>

<hr/>

<h2>Course Documents</h2>

<p>Here are the PDF course materials for deeper study of STM32 microcontroller programming:</p>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>STM32 - Structures and Registers</h4>
      <p>Complete guide to C structures for STM32 register access, peripheral configuration and usage.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S6/Microcontroleur/stm32-structures.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S6/Microcontroleur/stm32-structures.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Download PDF
        </a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>GPIO - Inputs/Outputs</h4>
      <p>GPIO configuration, input/output modes, pull-up/pull-down and pin manipulation with pointers.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S6/Microcontroleur/gpio.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S6/Microcontroleur/gpio.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Download PDF
        </a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Interrupts</h4>
      <p>Interrupt management, NVIC, priorities, handlers and real-time programming best practices.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S6/Microcontroleur/interruptions.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S6/Microcontroleur/interruptions.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Download PDF
        </a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Timers</h4>
      <p>Timer configuration and usage for delay generation, event counting and time measurements.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S6/Microcontroleur/timers.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S6/Microcontroleur/timers.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Download PDF
        </a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>PWM - Pulse Width Modulation</h4>
      <p>PWM signal generation for motor control, LEDs and intensity variation using timers.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S6/Microcontroleur/pwm.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S6/Microcontroleur/pwm.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Download PDF
        </a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>ADC - Analog-to-Digital Converter</h4>
      <p>ADC configuration, analog signal acquisition, trigger modes and usage with DMA.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S6/Microcontroleur/adc.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S6/Microcontroleur/adc.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Download PDF
        </a>
      </p>
    </div>
  </div>
</div>

<hr/>

<p><em>Course taught in 2022-2023 at INSA Toulouse, Department of Electrical Engineering and Computer Science.</em></p>

</div>

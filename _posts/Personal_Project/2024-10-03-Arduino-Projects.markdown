---
layout: default
title: "Arduino Robotics Projects"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
---

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

<div class="back-nav">
    <a href="./my-perso-projects.html" data-i18n-html="back-perso-projects">&larr; Retour aux Projets Personnels</a>
</div>

<div class="lang-fr">
<h1>Introduction</h1>
<p>Cette collection presente divers projets de robotique et d'electronique bases sur Arduino, developpes au fil du temps, allant du simple controle de LED a des bras robotiques complexes et des vehicules teleccommandes. Ces projets demontrent des applications pratiques de la programmation de microcontroleurs, du controle de moteurs, de l'integration de capteurs et de la communication sans fil sur les plateformes Arduino.</p>

<h1>Vue d'ensemble des projets</h1>
<p>Les projets couvrent plusieurs domaines :</p>
<ul>
<li>Vehicules teleccommandes avec controle Bluetooth</li>
<li>Prototypes de bras robotiques avec controle par servomoteurs</li>
<li>Integration de capteurs (ultrasonique, infrarouge, vibration)</li>
<li>Communication sans fil (Bluetooth, ESP32)</li>
<li>Interfaces d'affichage (ecrans LCD)</li>
<li>Systemes de controle de moteurs (pont en H, driver L298N)</li>
</ul>

<h2>Technologies cles</h2>
<ul>
<li><strong>Microcontroleurs :</strong> Arduino Uno, Arduino Nano, ESP32-CAM</li>
<li><strong>Communication :</strong> Bluetooth HC-05/HC-06, WiFi (ESP32)</li>
<li><strong>Capteurs :</strong> Ultrasonique HC-SR04, capteurs infrarouges, capteurs de vibration</li>
<li><strong>Actionneurs :</strong> Moteurs DC, servomoteurs, LEDs, buzzers</li>
<li><strong>Drivers moteurs :</strong> Pont en H L298N, modules relais</li>
<li><strong>Afficheurs :</strong> LCD 16x2 avec interface I2C</li>
</ul>

<h1>Projets phares</h1>

<h2>1. Voiture telecommandee Bluetooth</h2>
</div>

<div class="lang-en">
<h1>Introduction</h1>
<p>This collection showcases various Arduino-based robotics and electronics projects developed over time, ranging from simple LED control to complex robotic arms and remote-controlled vehicles. These projects demonstrate practical applications of microcontroller programming, motor control, sensor integration, and wireless communication using Arduino platforms.</p>

<h1>Project Overview</h1>
<p>The projects span multiple domains including:</p>
<ul>
<li>Remote-controlled vehicles with Bluetooth control</li>
<li>Robotic arm prototypes with servo control</li>
<li>Sensor integration (ultrasonic, infrared, vibration)</li>
<li>Wireless communication (Bluetooth, ESP32)</li>
<li>Display interfaces (LCD screens)</li>
<li>Motor control systems (H-bridge, L298N driver)</li>
</ul>

<h2>Key Technologies</h2>
<ul>
<li><strong>Microcontrollers:</strong> Arduino Uno, Arduino Nano, ESP32-CAM</li>
<li><strong>Communication:</strong> Bluetooth HC-05/HC-06, WiFi (ESP32)</li>
<li><strong>Sensors:</strong> Ultrasonic HC-SR04, infrared sensors, vibration sensors</li>
<li><strong>Actuators:</strong> DC motors, servo motors, LEDs, buzzers</li>
<li><strong>Motor Drivers:</strong> L298N H-Bridge, relay modules</li>
<li><strong>Displays:</strong> LCD 16x2 with I2C interface</li>
</ul>

<h1>Featured Projects</h1>

<h2>1. Bluetooth-Controlled Remote Car</h2>
</div>

<div style="display: flex; justify-content: center; gap: 15px; margin: 30px 0; flex-wrap: wrap;">
  <img src="/img/Arduino_Projects/Bras1_model.png" alt="Robotic Arm Model" style="width: 60%;" onclick="openModal(this.src)"/>
</div>

<div class="lang-fr">
<h3>Description du projet</h3>
<p>Developpement d'un vehicule telecommande controle via Bluetooth depuis un smartphone. La voiture comprend :</p>
<ul>
<li><strong>Quatre roues motrices</strong> avec moteurs DC</li>
<li><strong>Pont en H L298N</strong> pour le controle bidirectionnel des moteurs</li>
<li><strong>Module Bluetooth</strong> (HC-05) pour la communication sans fil</li>
<li><strong>Capteur ultrasonique</strong> pour la detection d'obstacles</li>
<li><strong>Phares LED</strong> pour la visibilite</li>
<li><strong>Application Android</strong> pour le controle intuitif</li>
</ul>

<h3>Composants materiels</h3>
</div>

<div class="lang-en">
<h3>Project Description</h3>
<p>Development of a remote-controlled vehicle controlled via Bluetooth from a smartphone. The car features:</p>
<ul>
<li><strong>Four-wheel drive</strong> with DC motors</li>
<li><strong>L298N H-Bridge</strong> for bidirectional motor control</li>
<li><strong>Bluetooth module</strong> (HC-05) for wireless communication</li>
<li><strong>Ultrasonic sensor</strong> for obstacle detection</li>
<li><strong>LED headlights</strong> for visibility</li>
<li><strong>Android app</strong> for intuitive control</li>
</ul>

<h3>Hardware Components</h3>
</div>

<pre><code>Components List:
- Arduino Uno microcontroller
- L298N motor driver module
- 4x DC motors (6V)
- HC-05 Bluetooth module
- HC-SR04 ultrasonic sensor
- 2x LED headlights
- 7.4V Li-Po battery
- Chassis and wheels
</code></pre>

<div class="lang-fr">
<h3>Implementation logicielle</h3>
<p><strong>Fonctions de controle des moteurs :</strong></p>
</div>

<div class="lang-en">
<h3>Software Implementation</h3>
<p><strong>Motor Control Functions:</strong></p>
</div>

<pre><code class="language-cpp">// Forward motion
void avancer() {
    digitalWrite(enableBridge1, HIGH);
    digitalWrite(MotorForward1, HIGH);
    digitalWrite(MotorReverse1, LOW);
    digitalWrite(enableBridge2, HIGH);
    digitalWrite(MotorForward2, HIGH);
    digitalWrite(MotorReverse2, LOW);
}

// Reverse motion
void reculer() {
    digitalWrite(enableBridge1, HIGH);
    digitalWrite(MotorForward1, LOW);
    digitalWrite(MotorReverse1, HIGH);
    digitalWrite(enableBridge2, HIGH);
    digitalWrite(MotorForward2, LOW);
    digitalWrite(MotorReverse2, HIGH);
}

// Turn right
void droite() {
    digitalWrite(enableBridge2, HIGH);
    digitalWrite(MotorForward2, HIGH);
    digitalWrite(MotorReverse2, LOW);
}

// Turn left
void gauche() {
    digitalWrite(enableBridge1, HIGH);
    digitalWrite(MotorForward1, HIGH);
    digitalWrite(MotorReverse1, LOW);
}

// Stop all motors
void stopp() {
    digitalWrite(enableBridge1, LOW);
    digitalWrite(enableBridge2, LOW);
}
</code></pre>

<div class="lang-fr">
<p><strong>Traitement des commandes Bluetooth :</strong></p>
</div>

<div class="lang-en">
<p><strong>Bluetooth Command Processing:</strong></p>
</div>

<pre><code class="language-cpp">void loop() {
    if (Serial.available() > 0) {
        Bluetooth = Serial.read();

        switch(Bluetooth) {
            case 'F': avancer(); break;     // Forward
            case 'B': reculer(); break;     // Backward
            case 'R': droite(); break;      // Right
            case 'L': gauche(); break;      // Left
            case 'S': stopp(); break;       // Stop
            case 'W': digitalWrite(phare1, HIGH); break;  // Lights ON
            case 'w': digitalWrite(phare1, LOW); break;   // Lights OFF
        }
    }
}
</code></pre>

<div class="lang-fr">
<h3>Fonctionnalites implementees</h3>
<ul>
<li><strong>Controle directionnel :</strong> Avant, arriere, gauche, droite</li>
<li><strong>Controle de vitesse :</strong> Rapport cyclique PWM variable (0-255)</li>
<li><strong>Evitement d'obstacles :</strong> Integration du capteur ultrasonique</li>
<li><strong>Systeme d'eclairage :</strong> Commutation des phares LED</li>
<li><strong>Arret d'urgence :</strong> Coupure immediate des moteurs</li>
<li><strong>Portee :</strong> ~10 metres en Bluetooth</li>
</ul>

<h2>2. Bras robotique avec controle par servomoteurs</h2>
</div>

<div class="lang-en">
<h3>Features Implemented</h3>
<ul>
<li><strong>Directional control:</strong> Forward, backward, left, right</li>
<li><strong>Speed control:</strong> Variable PWM duty cycle (0-255)</li>
<li><strong>Obstacle avoidance:</strong> Ultrasonic sensor integration</li>
<li><strong>Lighting system:</strong> LED headlights toggle</li>
<li><strong>Emergency stop:</strong> Immediate motor shutdown</li>
<li><strong>Range:</strong> ~10 meters Bluetooth range</li>
</ul>

<h2>2. Robotic Arm with Servo Control</h2>
</div>

<div style="display: flex; justify-content: center; gap: 15px; margin: 30px 0; flex-wrap: wrap;">
  <img src="/img/Arduino_Projects/Bras2_model1.jpg" alt="Robotic Arm Design" style="width: 45%;" onclick="openModal(this.src)"/>
  <img src="/img/Arduino_Projects/Petit_bras_model.jpg" alt="Small Robotic Arm" style="width: 45%;" onclick="openModal(this.src)"/>
</div>

<div class="lang-fr">
<h3>Description du projet</h3>
<p>Conception et developpement de bras robotiques imprimes en 3D avec plusieurs degres de liberte, controles par des servomoteurs et Arduino. Le projet comprend :</p>
<ul>
<li><strong>Modelisation 3D</strong> en logiciel CAO</li>
<li><strong>Generation de fichiers STL</strong> pour l'impression 3D</li>
<li><strong>Coordination multi-servos</strong> (4-6 servomoteurs)</li>
<li><strong>Mecanisme de pince</strong> avec systeme d'engrenages</li>
<li><strong>Controle de position</strong> via commandes serie ou potentiometres</li>
</ul>

<h3>Conception mecanique</h3>
<p>Les bras robotiques ont ete concus avec :</p>
<ul>
<li><strong>Rotation de la base :</strong> Rotation continue a 360 degres</li>
<li><strong>Articulation de l'epaule :</strong> Mouvement vertical du bras</li>
<li><strong>Articulation du coude :</strong> Extension du bras vers l'avant</li>
<li><strong>Rotation du poignet :</strong> Orientation horizontale du bras</li>
<li><strong>Pince :</strong> Griffe a deux doigts avec entrainement par engrenage</li>
<li><strong>Materiaux :</strong> Pieces imprimees en PLA 3D, vis M3, supports de servomoteurs</li>
</ul>

<h3>Systeme de controle des servomoteurs</h3>
</div>

<div class="lang-en">
<h3>Project Description</h3>
<p>Design and development of 3D-printed robotic arms with multiple degrees of freedom, controlled by servo motors and Arduino. The project included:</p>
<ul>
<li><strong>3D modeling</strong> in CAD software</li>
<li><strong>STL file generation</strong> for 3D printing</li>
<li><strong>Multi-servo coordination</strong> (4-6 servos)</li>
<li><strong>Gripper mechanism</strong> with gear system</li>
<li><strong>Position control</strong> via serial commands or potentiometers</li>
</ul>

<h3>Mechanical Design</h3>
<p>The robotic arms were designed with:</p>
<ul>
<li><strong>Base rotation:</strong> 360 degree continuous rotation</li>
<li><strong>Shoulder joint:</strong> Vertical movement arm</li>
<li><strong>Elbow joint:</strong> Forward drive arm extension</li>
<li><strong>Wrist rotation:</strong> Horizontal arm orientation</li>
<li><strong>Gripper:</strong> Two-finger claw with gear drive</li>
<li><strong>Materials:</strong> PLA 3D-printed parts, M3 screws, servo brackets</li>
</ul>

<h3>Servo Control System</h3>
</div>

<pre><code class="language-cpp">#include &lt;Servo.h&gt;

Servo servoBase;
Servo servoShoulder;
Servo servoElbow;
Servo servoWrist;
Servo servoGripper;

void setup() {
    servoBase.attach(3);
    servoShoulder.attach(5);
    servoElbow.attach(6);
    servoWrist.attach(9);
    servoGripper.attach(10);

    // Initialize to neutral position
    servoBase.write(90);
    servoShoulder.write(90);
    servoElbow.write(90);
    servoWrist.write(90);
    servoGripper.write(45);
}

void moveToPosition(int base, int shoulder, int elbow, int wrist, int grip) {
    servoBase.write(base);
    delay(15);
    servoShoulder.write(shoulder);
    delay(15);
    servoElbow.write(elbow);
    delay(15);
    servoWrist.write(wrist);
    delay(15);
    servoGripper.write(grip);
}
</code></pre>

<div class="lang-fr">
<h3>Applications</h3>
<ul>
<li><strong>Operations de pick and place</strong></li>
<li><strong>Tri automatise</strong></li>
<li><strong>Demonstrations de robotique pedagogique</strong></li>
<li><strong>Experiences de manipulation d'objets</strong></li>
</ul>

<h2>3. Modules d'integration de capteurs</h2>

<h3>Mesure de distance ultrasonique</h3>
</div>

<div class="lang-en">
<h3>Applications</h3>
<ul>
<li><strong>Pick and place operations</strong></li>
<li><strong>Automated sorting</strong></li>
<li><strong>Educational robotics demonstrations</strong></li>
<li><strong>Object manipulation experiments</strong></li>
</ul>

<h2>3. Sensor Integration Modules</h2>

<h3>Ultrasonic Distance Measurement</h3>
</div>

<pre><code class="language-cpp">const int pinTrig = 6;
const int pinEcho = 7;
long temps;
float distance;

void setup() {
    pinMode(pinTrig, OUTPUT);
    pinMode(pinEcho, INPUT);
    digitalWrite(pinTrig, LOW);
    Serial.begin(9600);
}

void mesureDistance() {
    digitalWrite(pinTrig, HIGH);
    delayMicroseconds(10);
    digitalWrite(pinTrig, LOW);

    temps = pulseIn(pinEcho, HIGH);
    distance = temps * 0.034 / 2;  // Speed of sound: 340 m/s

    Serial.print("Distance: ");
    Serial.print(distance);
    Serial.println(" cm");
}
</code></pre>

<div class="lang-fr">
<h3>Integration de capteurs infrarouges</h3>
<ul>
<li><strong>Detection d'obstacles</strong> pour robots suiveurs de ligne</li>
<li><strong>Detection de proximite</strong> pour l'evitement de collision</li>
<li><strong>Traitement de sortie numerique/analogique</strong></li>
<li><strong>Ajustement du seuil</strong> pour differents environnements</li>
</ul>

<h3>Capteur de vibration</h3>
<ul>
<li><strong>Detection de chocs</strong> pour systemes de securite</li>
<li><strong>Surveillance d'impacts</strong> dans les systemes mecaniques</li>
<li><strong>Traitement de signal numerique</strong> avec gestion d'interruptions</li>
</ul>

<h2>4. Projet de streaming ESP32-CAM</h2>

<h3>Description du projet</h3>
<p>Implementation d'un systeme de camera WiFi utilisant le module ESP32-CAM :</p>
<ul>
<li><strong>Streaming video en direct</strong> via WiFi</li>
<li><strong>Interface serveur web</strong> pour le controle de la camera</li>
<li><strong>Capture d'images</strong> et stockage</li>
<li><strong>Detection de mouvement</strong></li>
<li><strong>Modes basse consommation</strong> pour fonctionnement sur batterie</li>
</ul>

<h3>Caracteristiques</h3>
<ul>
<li><strong>Resolution :</strong> Jusqu'a 2MP (1600x1200)</li>
<li><strong>Debit d'images :</strong> 10-15 FPS en streaming</li>
<li><strong>Protocoles WiFi :</strong> 802.11 b/g/n</li>
<li><strong>Interface web :</strong> Affichage video en temps reel</li>
<li><strong>Controle a distance :</strong> Pan/tilt avec servomoteurs (optionnel)</li>
</ul>

<h2>5. Integration d'ecran LCD</h2>

<h3>LCD 16x2 avec interface I2C</h3>
</div>

<div class="lang-en">
<h3>Infrared Sensor Integration</h3>
<ul>
<li><strong>Obstacle detection</strong> for line-following robots</li>
<li><strong>Proximity sensing</strong> for collision avoidance</li>
<li><strong>Digital/analog output</strong> processing</li>
<li><strong>Threshold adjustment</strong> for different environments</li>
</ul>

<h3>Vibration Sensor</h3>
<ul>
<li><strong>Shock detection</strong> for security systems</li>
<li><strong>Impact monitoring</strong> in mechanical systems</li>
<li><strong>Digital signal processing</strong> with interrupt handling</li>
</ul>

<h2>4. ESP32-CAM Streaming Project</h2>

<h3>Project Description</h3>
<p>Implementation of a WiFi-enabled camera system using the ESP32-CAM module:</p>
<ul>
<li><strong>Live video streaming</strong> over WiFi</li>
<li><strong>Web server interface</strong> for camera control</li>
<li><strong>Image capture</strong> and storage</li>
<li><strong>Motion detection</strong> capabilities</li>
<li><strong>Low-power modes</strong> for battery operation</li>
</ul>

<h3>Features</h3>
<ul>
<li><strong>Resolution:</strong> Up to 2MP (1600x1200)</li>
<li><strong>Frame rate:</strong> 10-15 FPS for streaming</li>
<li><strong>WiFi protocols:</strong> 802.11 b/g/n</li>
<li><strong>Web interface:</strong> Real-time video display</li>
<li><strong>Remote control:</strong> Pan/tilt with servos (optional)</li>
</ul>

<h2>5. LCD Display Integration</h2>

<h3>16x2 LCD with I2C Interface</h3>
</div>

<pre><code class="language-cpp">#include &lt;LiquidCrystal_I2C.h&gt;

LiquidCrystal_I2C lcd(0x27, 16, 2);  // Address 0x27, 16 columns, 2 rows

void setup() {
    lcd.init();
    lcd.backlight();
    lcd.setCursor(0, 0);
    lcd.print("Arduino Project");
    lcd.setCursor(0, 1);
    lcd.print("Ready!");
}

void displayMessage(String line1, String line2) {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print(line1);
    lcd.setCursor(0, 1);
    lcd.print(line2);
}
</code></pre>

<div class="lang-fr">
<h3>Applications</h3>
<ul>
<li><strong>Affichage de l'etat du systeme</strong></li>
<li><strong>Visualisation des donnees des capteurs</strong></li>
<li><strong>Confirmation des entrees utilisateur</strong></li>
<li><strong>Systemes de navigation par menus</strong></li>
</ul>

<h1>Defis techniques et solutions</h1>

<h2>Defi 1 : Precision du controle moteur</h2>
<p><strong>Probleme :</strong> Vitesses de moteur incoherentes dues aux variations de tension de la batterie.</p>
<p><strong>Solution :</strong> Implementation d'un controle de vitesse PWM avec surveillance et compensation de tension :</p>
</div>

<div class="lang-en">
<h3>Applications</h3>
<ul>
<li><strong>System status display</strong></li>
<li><strong>Sensor data visualization</strong></li>
<li><strong>User input confirmation</strong></li>
<li><strong>Menu navigation systems</strong></li>
</ul>

<h1>Technical Challenges and Solutions</h1>

<h2>Challenge 1: Motor Control Precision</h2>
<p><strong>Problem:</strong> Inconsistent motor speeds due to battery voltage variations.</p>
<p><strong>Solution:</strong> Implemented PWM speed control with voltage monitoring and compensation:</p>
</div>

<pre><code class="language-cpp">int compensatedSpeed(int desiredSpeed, float batteryVoltage) {
    float nominalVoltage = 7.4;
    int compensated = desiredSpeed * (nominalVoltage / batteryVoltage);
    return constrain(compensated, 0, 255);
}
</code></pre>

<div class="lang-fr">
<h2>Defi 2 : Fiabilite de la communication Bluetooth</h2>
<p><strong>Probleme :</strong> Perte de commandes et reponses retardees dans la communication Bluetooth.</p>
<p><strong>Solution :</strong></p>
<ul>
<li>Implementation d'un systeme d'acquittement de commandes</li>
<li>Ajout d'un tampon de commandes avec file FIFO</li>
<li>Augmentation du debit en bauds a 9600 pour la stabilite</li>
<li>Ajout de verification d'erreurs et mecanisme de reessai</li>
</ul>

<h2>Defi 3 : Tremblements et bruit des servomoteurs</h2>
<p><strong>Probleme :</strong> Les servomoteurs presentaient des tremblements en position maintenue.</p>
<p><strong>Solution :</strong></p>
<ul>
<li>Ajout de condensateurs (100 uF) sur les lignes d'alimentation des servos</li>
<li>Implementation d'une alimentation separee pour les servomoteurs</li>
<li>Utilisation de <code>servo.write()</code> uniquement lors des changements de position</li>
<li>Application d'un filtrage logiciel pour des transitions fluides</li>
</ul>

<h2>Defi 4 : Gestion de l'alimentation</h2>
<p><strong>Probleme :</strong> Decharge de la batterie et courant insuffisant pour tous les moteurs simultanement.</p>
<p><strong>Solution :</strong></p>
<ul>
<li>Calcul des besoins totaux en courant</li>
<li>Selection d'une capacite de batterie appropriee (2200 mAh)</li>
<li>Implementation d'un demarrage progressif des moteurs</li>
<li>Ajout d'une protection contre la basse tension</li>
</ul>

<h1>Outils de developpement et flux de travail</h1>

<h2>Outils logiciels</h2>
<ul>
<li><strong>Arduino IDE :</strong> Environnement de developpement principal</li>
<li><strong>PlatformIO :</strong> Gestion avancee de projets</li>
<li><strong>Moniteur serie :</strong> Debogage et tests</li>
<li><strong>Fritzing :</strong> Creation de schemas de circuits</li>
<li><strong>Fusion 360 :</strong> Modelisation 3D pour les pieces mecaniques</li>
</ul>

<h2>Outils materiels</h2>
<ul>
<li><strong>Multimetre :</strong> Mesures de tension et de courant</li>
<li><strong>Oscilloscope :</strong> Analyse et debogage de signaux</li>
<li><strong>Station de soudage :</strong> Assemblage de circuits</li>
<li><strong>Imprimante 3D :</strong> Fabrication de pieces mecaniques</li>
<li><strong>Alimentation de laboratoire :</strong> Tests avec tension stable</li>
</ul>

<h2>Processus de developpement</h2>
<ol>
<li><strong>Concept et planification :</strong> Definir les exigences du projet</li>
<li><strong>Conception du circuit :</strong> Creer le schema et le prototype sur breadboard</li>
<li><strong>Developpement du code :</strong> Ecrire et tester le firmware de maniere incrementale</li>
<li><strong>Tests d'integration :</strong> Combiner materiel et logiciel</li>
<li><strong>Assemblage mecanique :</strong> Imprimer en 3D et assembler les pieces</li>
<li><strong>Tests systeme :</strong> Valider toutes les fonctions</li>
<li><strong>Optimisation :</strong> Ameliorer les performances et la fiabilite</li>
<li><strong>Documentation :</strong> Enregistrer les specifications et l'utilisation</li>
</ol>

<h1>Lecons apprises</h1>

<h2>Competences techniques developpees</h2>
<ul>
<li><strong>Programmation de microcontroleurs :</strong> Maitrise du C/C++ Arduino</li>
<li><strong>Interfacage materiel :</strong> Integration de capteurs et actionneurs</li>
<li><strong>Protocoles de communication :</strong> Implementation UART, I2C, SPI</li>
<li><strong>Controle de moteurs :</strong> PWM, fonctionnement du driver pont en H</li>
<li><strong>Conception mecanique :</strong> Modelisation CAO et impression 3D</li>
<li><strong>Techniques de debogage :</strong> Approche systematique de resolution de problemes</li>
</ul>

<h2>Bonnes pratiques etablies</h2>
<ul>
<li><strong>Structure de code modulaire :</strong> Fonctions et bibliotheques reutilisables</li>
<li><strong>Documentation appropriee :</strong> Commentaires et descriptions de fonctions</li>
<li><strong>Controle de version :</strong> Developpement incremental avec sauvegardes</li>
<li><strong>Considerations d'alimentation :</strong> Separation de l'alimentation logique et moteur</li>
<li><strong>Fonctions de securite :</strong> Arrets d'urgence et protection contre la tension</li>
<li><strong>Methodologie de test :</strong> Tests unitaires avant integration systeme</li>
</ul>

<h2>Pistes d'amelioration future</h2>
<ul>
<li><strong>Algorithmes de controle avances :</strong> Implementation PID pour des mouvements precis</li>
<li><strong>Fusion de capteurs :</strong> Combinaison de plusieurs capteurs pour une meilleure precision</li>
<li><strong>Protocoles sans fil :</strong> Transition vers WiFi ou LoRa pour une portee etendue</li>
<li><strong>Navigation autonome :</strong> Implementation d'algorithmes de recherche de chemin</li>
<li><strong>Vision par ordinateur :</strong> Integration d'OpenCV avec ESP32-CAM</li>
<li><strong>Conception de PCB :</strong> Creation de cartes personnalisees pour une integration compacte</li>
</ul>

<h1>Idees de projets futurs</h1>

<h2>Objectifs a court terme</h2>
<ul>
<li><strong>Robot suiveur de ligne</strong> avec controle PID</li>
<li><strong>Voiture eviteur d'obstacles</strong> avec capteurs multiples</li>
<li><strong>Bras robotique controle par Bluetooth</strong> avec memoire de position</li>
<li><strong>Station meteo</strong> avec capteurs environnementaux multiples</li>
<li><strong>Systeme de domotique</strong> avec controle par relais</li>
</ul>

<h2>Aspirations a long terme</h2>
<ul>
<li><strong>Robot de livraison autonome</strong> avec navigation GPS</li>
<li><strong>Drone quadricoptere</strong> avec controleur de vol Arduino</li>
<li><strong>Robot bipede marchant</strong> avec coordination de servomoteurs</li>
<li><strong>Reseau de capteurs IoT</strong> avec journalisation de donnees cloud</li>
<li><strong>Coordination d'essaim de robots</strong> avec communication inter-robots</li>
</ul>

<h1>Conclusion</h1>
<p>Ces projets Arduino representent un parcours de l'electronique de base aux systemes robotiques complexes. Chaque projet a fourni une experience pratique precieuse en programmation embarquee, integration materielle et conception de systemes. Le processus de developpement iteratif, la resolution de defis et l'apprentissage continu ont construit une base solide en robotique et electronique.</p>

<p>Les competences acquises a travers ces projets sont directement applicables au developpement professionnel de systemes embarques, aux dispositifs IoT et a la robotique autonome. Les projets futurs s'appuieront sur cette base, integrant des capteurs plus avances, des algorithmes d'apprentissage automatique et des conceptions mecaniques plus sophistiquees.</p>
</div>

<div class="lang-en">
<h2>Challenge 2: Bluetooth Communication Reliability</h2>
<p><strong>Problem:</strong> Command loss and delayed responses in Bluetooth communication.</p>
<p><strong>Solution:</strong></p>
<ul>
<li>Implemented command acknowledgment system</li>
<li>Added command buffer with FIFO queue</li>
<li>Increased baud rate to 9600 for stability</li>
<li>Added error checking and retry mechanism</li>
</ul>

<h2>Challenge 3: Servo Jitter and Noise</h2>
<p><strong>Problem:</strong> Servo motors exhibited jittering during hold position.</p>
<p><strong>Solution:</strong></p>
<ul>
<li>Added capacitors (100 uF) across servo power lines</li>
<li>Implemented separate power supply for servos</li>
<li>Used <code>servo.write()</code> only when position changes</li>
<li>Applied software filtering for smooth transitions</li>
</ul>

<h2>Challenge 4: Power Management</h2>
<p><strong>Problem:</strong> Battery drain and insufficient current for all motors simultaneously.</p>
<p><strong>Solution:</strong></p>
<ul>
<li>Calculated total current requirements</li>
<li>Selected appropriate battery capacity (2200 mAh)</li>
<li>Implemented staged motor startup</li>
<li>Added low-voltage cutoff protection</li>
</ul>

<h1>Development Tools and Workflow</h1>

<h2>Software Tools</h2>
<ul>
<li><strong>Arduino IDE:</strong> Primary development environment</li>
<li><strong>PlatformIO:</strong> Advanced project management</li>
<li><strong>Serial Monitor:</strong> Debugging and testing</li>
<li><strong>Fritzing:</strong> Circuit diagram creation</li>
<li><strong>Fusion 360:</strong> 3D modeling for mechanical parts</li>
</ul>

<h2>Hardware Tools</h2>
<ul>
<li><strong>Multimeter:</strong> Voltage and current measurements</li>
<li><strong>Oscilloscope:</strong> Signal analysis and debugging</li>
<li><strong>Soldering station:</strong> Circuit assembly</li>
<li><strong>3D printer:</strong> Mechanical part fabrication</li>
<li><strong>Power supply:</strong> Testing with stable voltage</li>
</ul>

<h2>Development Process</h2>
<ol>
<li><strong>Concept and planning:</strong> Define project requirements</li>
<li><strong>Circuit design:</strong> Create schematic and breadboard prototype</li>
<li><strong>Code development:</strong> Write and test firmware incrementally</li>
<li><strong>Integration testing:</strong> Combine hardware and software</li>
<li><strong>Mechanical assembly:</strong> 3D print and assemble parts</li>
<li><strong>System testing:</strong> Validate all functions</li>
<li><strong>Optimization:</strong> Improve performance and reliability</li>
<li><strong>Documentation:</strong> Record specifications and usage</li>
</ol>

<h1>Lessons Learned</h1>

<h2>Technical Skills Developed</h2>
<ul>
<li><strong>Microcontroller programming:</strong> Arduino C/C++ proficiency</li>
<li><strong>Hardware interfacing:</strong> Sensor and actuator integration</li>
<li><strong>Communication protocols:</strong> UART, I2C, SPI implementation</li>
<li><strong>Motor control:</strong> PWM, H-bridge driver operation</li>
<li><strong>Mechanical design:</strong> CAD modeling and 3D printing</li>
<li><strong>Debugging techniques:</strong> Systematic troubleshooting approach</li>
</ul>

<h2>Best Practices Established</h2>
<ul>
<li><strong>Modular code structure:</strong> Reusable functions and libraries</li>
<li><strong>Proper documentation:</strong> Comments and function descriptions</li>
<li><strong>Version control:</strong> Incremental development with backups</li>
<li><strong>Power considerations:</strong> Separate logic and motor power</li>
<li><strong>Safety features:</strong> Emergency stops and voltage protection</li>
<li><strong>Testing methodology:</strong> Unit tests before system integration</li>
</ul>

<h2>Areas for Future Improvement</h2>
<ul>
<li><strong>Advanced control algorithms:</strong> PID implementation for precise movement</li>
<li><strong>Sensor fusion:</strong> Combining multiple sensors for better accuracy</li>
<li><strong>Wireless protocols:</strong> Transition to WiFi or LoRa for extended range</li>
<li><strong>Autonomous navigation:</strong> Implement pathfinding algorithms</li>
<li><strong>Computer vision:</strong> Integrate OpenCV with ESP32-CAM</li>
<li><strong>PCB design:</strong> Create custom boards for compact integration</li>
</ul>

<h1>Future Project Ideas</h1>

<h2>Short-term Goals</h2>
<ul>
<li><strong>Line-following robot</strong> with PID control</li>
<li><strong>Obstacle-avoiding car</strong> with multiple sensors</li>
<li><strong>Bluetooth-controlled robotic arm</strong> with position memory</li>
<li><strong>Weather station</strong> with multiple environmental sensors</li>
<li><strong>Home automation system</strong> with relay control</li>
</ul>

<h2>Long-term Aspirations</h2>
<ul>
<li><strong>Autonomous delivery robot</strong> with GPS navigation</li>
<li><strong>Quadcopter drone</strong> with Arduino flight controller</li>
<li><strong>Bipedal walking robot</strong> with servo coordination</li>
<li><strong>IoT sensor network</strong> with cloud data logging</li>
<li><strong>Robot swarm coordination</strong> with inter-robot communication</li>
</ul>

<h1>Conclusion</h1>
<p>These Arduino projects represent a journey from basic electronics to complex robotic systems. Each project provided valuable hands-on experience in embedded programming, hardware integration, and system design. The iterative development process, troubleshooting challenges, and continuous learning have built a strong foundation in robotics and electronics.</p>

<p>The skills acquired through these projects are directly applicable to professional embedded systems development, IoT devices, and autonomous robotics. Future projects will build upon this foundation, incorporating more advanced sensors, machine learning algorithms, and sophisticated mechanical designs.</p>
</div>

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

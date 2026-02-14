---
layout: default
title: "Télécommunications - S3"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

<style>
.back-nav { margin-bottom: 20px; }
.back-nav a { text-decoration: none; color: #2a7ae2; font-weight: 600; }
.back-nav a:hover { text-decoration: underline; }
.section-title { color: #2a7ae2; border-bottom: 2px solid #2a7ae2; padding-bottom: 10px; margin-top: 30px; margin-bottom: 20px; }
</style>

<div class="back-nav">
  <a href="./my-courses-2021-2022.html" data-i18n-html="back-courses-2021-2022">&larr; Retour a Mes Cours 2021-2022</a>
</div>

<div class="lang-fr">

<h1>Télécommunications - Semestre 3</h1>

<p><strong>Annee</strong>: 2021-2022 | <strong>Semestre</strong>: 3 | <strong>Type</strong>: Technique</p>

<hr>

<h2>PART A - Présentation Générale du Cours</h2>

<h3>Contexte et objectifs</h3>

<p>Introduction aux systèmes de télécommunications numériques : codage, modulations, transmission sur canal bruité, détection et correction d'erreurs. Fondement pour Télécom Num S4 et Réseaux.</p>

<p><strong>Objectifs :</strong></p>
<ul>
<li>Codage en ligne (NRZ, Manchester, etc.)</li>
<li>Modulations numériques de base (ASK, FSK, PSK)</li>
<li>Canal de transmission (bruit, atténuation)</li>
<li>Détection/correction d'erreurs (CRC, codes correcteurs)</li>
<li>Analyse performances (BER, SNR)</li>
</ul>

<h3>Prérequis</h3>
<ul>
<li>Signaux et systèmes (Fourier)</li>
<li>OL S3 (MATLAB, modulations)</li>
</ul>

<hr>

<h2>PART B: EXPÉRIENCE, CONTEXTE ET FONCTION</h2>

<h3>Module 1 : Codage en ligne</h3>

<p><strong>Principe :</strong><br>
Transformation bits (0/1) en signal électrique adapté à la transmission.</p>

<p><strong>Codes courants :</strong></p>
<ul>
<li><strong>NRZ (Non-Return to Zero)</strong> : 0→-V, 1→+V. Simple mais composante DC.</li>
<li><strong>RZ (Return to Zero)</strong> : retour à 0 en milieu de bit. Synchronisation facilitée.</li>
<li><strong>Manchester (Biphase)</strong> : 0→transition haut-bas, 1→bas-haut. Pas de DC, auto-synchronisant (Ethernet 10Base-T).</li>
<li><strong>Miller</strong> : transition si 1, pas si 0 (sauf deux 0 consécutifs). Économie bande passante.</li>
<li><strong>AMI (Alternate Mark Inversion)</strong> : 0→0V, 1→±V alternés. Pas de DC.</li>
</ul>

<p><strong>Critères choix :</strong></p>
<ul>
<li>Composante DC nulle (couplage AC)</li>
<li>Densité transitions (synchronisation)</li>
<li>Bande passante</li>
<li>Immunité bruit</li>
</ul>

<h3>Module 2 : Modulations numériques</h3>

<p><strong>ASK (Amplitude Shift Keying) :</strong></p>
<ul>
<li>Modulation amplitude porteuse</li>
<li>Sensible au bruit</li>
<li>Peu utilisée seule</li>
</ul>

<p><strong>FSK (Frequency Shift Keying) :</strong></p>
<ul>
<li>0→f₁, 1→f₂</li>
<li>Robuste au bruit</li>
<li>Applications : modems bas débit, RFID, LoRa</li>
</ul>

<p><strong>PSK (Phase Shift Keying) :</strong></p>
<ul>
<li><strong>BPSK</strong> : 0→0°, 1→180° (2 symboles). Robuste.</li>
<li><strong>QPSK</strong> : 4 phases (0°, 90°, 180°, 270°) → 2 bits/symbole. WiFi, satellite.</li>
<li><strong>8-PSK</strong> : 8 phases → 3 bits/symbole.</li>
</ul>

<p><strong>QAM (Quadrature Amplitude Modulation) :</strong></p>
<ul>
<li>Modulation amplitude + phase</li>
<li>16-QAM, 64-QAM, 256-QAM</li>
<li>Haute efficacité spectrale (bits/Hz)</li>
<li>Applications : 4G/5G, câble, WiFi</li>
</ul>

<p><strong>Constellation :</strong><br>
Représentation I/Q (en phase / quadrature) des symboles.</p>

<h3>Module 3 : Canal de transmission</h3>

<p><strong>Modèle canal :</strong></p>
<ul>
<li>Atténuation (pertes propagation)</li>
<li>Bruit AWGN (Additive White Gaussian Noise)</li>
<li>Interférences</li>
<li>Distorsion (multi-trajets, dispersion)</li>
</ul>

<p><strong>SNR (Signal-to-Noise Ratio) :</strong><br>
SNR(dB) = 10 log₁₀(P_signal / P_bruit)</p>

<p><strong>Capacité de Shannon :</strong><br>
C = B log₂(1 + SNR) (bits/s)<br>
Capacité maximale théorique du canal.</p>

<p><strong>BER (Bit Error Rate) :</strong><br>
Taux d'erreur binaire. BER &lt; 10⁻⁶ typique pour communications fiables.</p>

<h3>Module 4 : Détection et correction d'erreurs</h3>

<p><strong>Détection d'erreurs :</strong></p>
<ul>
<li><strong>Bit de parité</strong> : pair/impair. Détecte erreurs impaires.</li>
<li><strong>Checksum</strong> : somme octets.</li>
<li><strong>CRC (Cyclic Redundancy Check)</strong> : division polynomiale. Très efficace (Ethernet, USB). CRC-16, CRC-32.</li>
</ul>

<p><strong>Correction d'erreurs (FEC - Forward Error Correction) :</strong></p>
<ul>
<li><strong>Code de Hamming</strong> : corrige 1 erreur, détecte 2.</li>
<li><strong>Codes Reed-Solomon</strong> : CD, DVD, QR codes. Correction paquets d'erreurs.</li>
<li><strong>Codes convolutifs</strong> : mémoire, décodage Viterbi. Espace, 4G.</li>
<li><strong>Turbo codes, LDPC</strong> : proches limite Shannon. 5G.</li>
</ul>

<p><strong>Principe :</strong><br>
Ajout redondance (bits supplémentaires) pour détecter/corriger erreurs sans retransmission.</p>

<hr>

<h2>PART C: ASPECTS TECHNIQUES</h2>

<h3>TP MATLAB</h3>

<p><strong>TP1 : Codages en ligne</strong></p>
<ul>
<li>Génération séquence bits</li>
<li>Codage NRZ, Manchester, AMI</li>
<li>Analyse spectrale (DSP)</li>
</ul>

<p><strong>TP2 : Modulation BPSK</strong></p>
<ul>
<li>Génération porteuse, modulation</li>
<li>Canal AWGN (SNR variable)</li>
<li>Démodulation</li>
<li>Calcul BER vs SNR</li>
</ul>

<p><strong>TP3 : QPSK et constellation</strong></p>
<ul>
<li>Modulation QPSK</li>
<li>Diagramme constellation I/Q</li>
<li>Impact bruit sur constellation</li>
</ul>

<p><strong>TP4 : CRC</strong></p>
<ul>
<li>Implémentation CRC-8, CRC-16</li>
<li>Test détection erreurs (1 bit, 2 bits, burst)</li>
</ul>

<h3>Projet simulation chaîne complète</h3>

<p><strong>Architecture :</strong></p>
<pre><code>[Source bits] → [Codeur canal] → [Modulateur] → [Canal AWGN]
                                                     ↓
[Sink bits]  ← [Décodeur]     ← [Démodulateur]     ←</code></pre>

<p><strong>Paramètres :</strong></p>
<ul>
<li>Modulation : QPSK</li>
<li>Code correcteur : Hamming (7,4)</li>
<li>SNR : 0 à 15 dB</li>
<li>Débit : 1 Mbps</li>
</ul>

<p><strong>Résultats :</strong></p>
<ul>
<li>Courbes BER vs SNR (avec/sans codage)</li>
<li>Gain de codage (≈3-5 dB)</li>
</ul>

<hr>

<h2>PART D: ANALYSE ET RÉFLEXION</h2>

<h3>Évaluation</h3>
<ul>
<li>TP MATLAB (40%)</li>
<li>Projet chaîne de transmission (30%)</li>
<li>Contrôles (15%)</li>
<li>Examen final (15%)</li>
</ul>

<h3>Compétences acquises</h3>
<ul>
<li>Compréhension systèmes télécommunications numériques</li>
<li>Simulation MATLAB (modulations, canal, BER)</li>
<li>Analyse performances (SNR, BER, capacité)</li>
<li>Codage détection/correction d'erreurs</li>
<li>Fondements pour 4G/5G, WiFi, satellite</li>
</ul>

<h3>Applications professionnelles</h3>
<ul>
<li>Télécommunications (mobiles, satellite, fibre)</li>
<li>Réseaux sans fil (WiFi, LoRa, Bluetooth)</li>
<li>Ingénieur RF/télécom</li>
<li>IoT (protocoles bas débit)</li>
</ul>

<h2>Chaîne de communication numérique</h2>

<h3>Caractéristiques</h3>
<ul>
<li>Débit binaire (bits/s)</li>
<li>Bande passante (Hz)</li>
<li>Efficacité spectrale (bits/s/Hz)</li>
<li>Probabilité d'erreur (BER)</li>
<li>Rapport signal/bruit (SNR)</li>
</ul>

<h3>Codage en ligne</h3>

<h4>Principe</h4>
<p>Représentation électrique des données binaires pour la transmission sur un canal.</p>

<h4>Codes NRZ (Non Return to Zero)</h4>
<p><strong>NRZ-L (Level) :</strong></p>
<ul>
<li>0 : niveau bas</li>
<li>1 : niveau haut</li>
<li>Simple mais composante continue</li>
<li>Pas d'auto-synchronisation</li>
</ul>

<p><strong>NRZ-I (Inverted) :</strong></p>
<ul>
<li>Transition sur les '1'</li>
<li>Pas de transition sur les '0'</li>
<li>Meilleure synchronisation</li>
</ul>

<h4>Codes RZ (Return to Zero)</h4>
<ul>
<li>Retour à zéro au milieu du bit</li>
<li>Meilleure synchronisation</li>
<li>Bande passante doublée</li>
</ul>

<h4>Code Manchester</h4>
<ul>
<li>Transition au milieu de chaque bit</li>
<li>0 : haut → bas</li>
<li>1 : bas → haut</li>
<li>Auto-synchronisation</li>
<li>Utilisé en Ethernet 10BASE-T</li>
</ul>

<h4>Code Manchester différentiel</h4>
<ul>
<li>Transition en début de bit</li>
<li>Présence/absence de transition au milieu</li>
</ul>

<h4>Code Bipolaire (AMI)</h4>
<ul>
<li>0 : niveau zéro</li>
<li>1 : alternance +V et -V</li>
<li>Pas de composante continue</li>
<li>Détection d'erreurs</li>
</ul>

<h4>Codes MLT-3, PAM-5</h4>
<ul>
<li>Multi-niveaux</li>
<li>Efficacité spectrale améliorée</li>
<li>Utilisés en Ethernet rapide</li>
</ul>

<h3>Transmission en bande de base</h3>

<h4>Critère de Nyquist</h4>
<ul>
<li>Pas d'interférence entre symboles (ISI)</li>
<li>Filtre en cosinus surélevé (raised cosine)</li>
<li>Roll-off factor</li>
<li>Bande passante minimale</li>
</ul>

<h4>Diagramme de l'oeil</h4>
<ul>
<li>Outil d'évaluation qualité</li>
<li>Ouverture verticale (marge bruit)</li>
<li>Ouverture horizontale (timing)</li>
<li>Taux d'erreur binaire (BER)</li>
</ul>

<h4>Égalisation</h4>
<ul>
<li>Compensation distorsions canal</li>
<li>Égaliseur linéaire</li>
<li>Égaliseur adaptatif (LMS)</li>
<li>Égaliseur à retour de décision (DFE)</li>
</ul>

<h3>Détection et correction d'erreurs</h3>

<h4>Codes détecteurs</h4>

<p><strong>Parité simple :</strong></p>
<ul>
<li>Bit de parité pair ou impair</li>
<li>Détecte erreur unique</li>
<li>Ne corrige pas</li>
</ul>

<p><strong>Parité croisée (2D) :</strong></p>
<ul>
<li>Parité lignes et colonnes</li>
<li>Détecte et corrige certaines erreurs</li>
</ul>

<p><strong>CRC (Cyclic Redundancy Check) :</strong></p>
<ul>
<li>Polynôme générateur</li>
<li>Reste de division polynomiale</li>
<li>CRC-8, CRC-16, CRC-32</li>
<li>Très efficace pour détection</li>
</ul>

<h4>Codes correcteurs</h4>

<p><strong>Code de Hamming :</strong></p>
<ul>
<li>Distance de Hamming</li>
<li>Correction 1 bit, détection 2 bits</li>
<li>Hamming(7,4), Hamming(15,11)</li>
<li>Bits de parité positionnés en 2^n</li>
</ul>

<p><strong>Code de Reed-Solomon :</strong></p>
<ul>
<li>Code cyclique non binaire</li>
<li>Correction de rafales d'erreurs</li>
<li>Utilisé en CD, DVD, QR codes</li>
<li>RS(255,223) typique</li>
</ul>

<p><strong>Codes convolutifs :</strong></p>
<ul>
<li>Encodage continu</li>
<li>Décodage Viterbi</li>
<li>Utilisés en téléphonie mobile</li>
<li>Rendement r = k/n</li>
</ul>

<p><strong>Turbo codes et LDPC :</strong></p>
<ul>
<li>Codes modernes haute performance</li>
<li>Proche limite de Shannon</li>
<li>4G, 5G, satellites</li>
</ul>

<h3>Performances de transmission</h3>

<h4>Probabilité d'erreur binaire (BER)</h4>
<ul>
<li>BER = erreurs / bits transmis</li>
<li>Dépend du SNR</li>
<li>Objectifs : 10^-6 à 10^-12</li>
</ul>

<h4>Rapport Eb/N0</h4>
<ul>
<li>Énergie par bit / Densité de bruit</li>
<li>Mesure de qualité</li>
<li>Courbes BER vs Eb/N0</li>
</ul>

<h4>Capacité de Shannon</h4>
<ul>
<li>C = B log₂(1 + SNR)</li>
<li>Limite théorique</li>
<li>Débit maximal sans erreur</li>
</ul>

<h2>Travaux pratiques</h2>

<h3>TP Codage en ligne</h3>
<ul>
<li>Génération de codes (NRZ, Manchester, AMI)</li>
<li>Analyse spectrale</li>
<li>Simulation de transmission</li>
<li>Diagramme de l'oeil</li>
</ul>

<h3>TP CRC</h3>
<ul>
<li>Implémentation algorithme CRC</li>
<li>Test de détection d'erreurs</li>
<li>Comparaison CRC-8, CRC-16, CRC-32</li>
<li>Application sur microcontrôleur</li>
</ul>

<h3>TP Code de Hamming</h3>
<ul>
<li>Encodage Hamming(7,4)</li>
<li>Décodage et correction</li>
<li>Insertion d'erreurs</li>
<li>Taux de correction</li>
</ul>

<h3>Projet communication</h3>
<ul>
<li>Liaison série codée</li>
<li>Protection par CRC</li>
<li>Protocole applicatif</li>
<li>Tests de robustesse</li>
</ul>

<h2>Outils utilisés</h2>

<h3>Simulation</h3>
<ul>
<li><strong>MATLAB/Simulink</strong> : Simulation systèmes</li>
<li><strong>Python</strong> : Programmation algorithmes</li>
<li><strong>GNU Radio</strong> : SDR et communications</li>
<li><strong>LabVIEW</strong> : Acquisition et traitement</li>
</ul>

<h3>Développement</h3>
<ul>
<li><strong>STM32</strong> : Implémentation embarquée</li>
<li><strong>Arduino</strong> : Prototypage rapide</li>
<li><strong>UART, SPI, I2C</strong> : Interfaces</li>
</ul>

<h3>Mesure</h3>
<ul>
<li><strong>Oscilloscope</strong> : Signaux et diagramme oeil</li>
<li><strong>Analyseur logique</strong> : Décodage protocoles</li>
<li><strong>BERT (Bit Error Rate Tester)</strong> : Mesure BER</li>
</ul>

<h2>Évaluation</h2>
<ul>
<li>Travaux pratiques (40%)</li>
<li>Projet de communication (30%)</li>
<li>Contrôle continu (15%)</li>
<li>Examen final (15%)</li>
</ul>

<h2>Liens avec d'autres cours</h2>
<ul>
<li><strong>SE</strong> : Traitement du signal</li>
<li><strong>OL</strong> : Modulation/démodulation</li>
<li><strong>IE</strong> : Implémentation protocoles</li>
<li><strong>Télécommunications Numériques (S4)</strong> : Approfondissement</li>
<li><strong>Réseau</strong> : Couches protocolaires</li>
</ul>

<h2>Exemples de calculs</h2>

<h3>Distance de Hamming</h3>
<p>Nombre de bits différents entre deux mots :</p>
<ul>
<li>101101 vs 101111 → distance = 1</li>
<li>101101 vs 010001 → distance = 3</li>
</ul>

<h3>CRC-8</h3>
<p>Polynôme : x⁸ + x² + x + 1 (0x107)</p>
<pre><code>Message : 11010011101100
Reste   : 10101010
Message transmis : 11010011101100 10101010</code></pre>

<h3>Code de Hamming(7,4)</h3>
<p>4 bits données : d1 d2 d3 d4<br>
3 bits parité : p1 p2 p3</p>
<p>Position : p1 p2 d1 p3 d2 d3 d4</p>
<pre><code>p1 = d1 XOR d2 XOR d4
p2 = d1 XOR d3 XOR d4
p3 = d2 XOR d3 XOR d4</code></pre>

<h2>Applications pratiques</h2>

<h3>Réseaux filaires</h3>
<ul>
<li>Ethernet (Manchester)</li>
<li>USB (NRZI)</li>
<li>RS-232/RS-485</li>
</ul>

<h3>Communications sans fil</h3>
<ul>
<li>WiFi (OFDM + codes)</li>
<li>Bluetooth (FEC)</li>
<li>Zigbee</li>
</ul>

<h3>Stockage</h3>
<ul>
<li>Disques durs (Reed-Solomon)</li>
<li>Mémoires flash (BCH, LDPC)</li>
<li>Codes QR</li>
</ul>

<h3>Audiovisuel</h3>
<ul>
<li>DVB (télévision numérique)</li>
<li>DAB (radio numérique)</li>
<li>HDMI</li>
</ul>

<h2>Compétences développées</h2>
<ul>
<li>Codage et décodage de données</li>
<li>Analyse de performances de transmission</li>
<li>Implémentation d'algorithmes de protection</li>
<li>Diagnostic de liaisons de communication</li>
<li>Simulation de systèmes numériques</li>
<li>Mesure et optimisation BER</li>
</ul>

<h2>Protocoles étudiés</h2>

<h3>Protocole de liaison de données</h3>
<ul>
<li>Tramage</li>
<li>Synchronisation</li>
<li>Détection d'erreurs (CRC)</li>
<li>Acquittements (ACK/NACK)</li>
<li>Retransmission (ARQ)</li>
</ul>

<h3>Exemple : Protocole simple</h3>
<pre><code>[Start] [Length] [Data] [CRC16] [Stop]
  0x02     1B      nB      2B     0x03</code></pre>

<h2>Problèmes courants</h2>

<h3>Transmission</h3>
<ul>
<li>Atténuation du signal</li>
<li>Bruit (thermique, impulsionnel)</li>
<li>Distorsion (ISI)</li>
<li>Dérive d'horloge</li>
<li>Réflexions (impédance)</li>
</ul>

<h3>Codage</h3>
<ul>
<li>Composante continue excessive</li>
<li>Bande passante trop large</li>
<li>Perte de synchronisation</li>
<li>Détection d'erreurs insuffisante</li>
</ul>

<h2>Implémentation embarquée</h2>

<h3>CRC sur microcontrôleur</h3>
<pre><code class="language-c">uint8_t crc8(uint8_t *data, uint8_t len) {
    uint8_t crc = 0;
    for(uint8_t i=0; i&lt;len; i++) {
        crc ^= data[i];
        for(uint8_t j=0; j&lt;8; j++) {
            if(crc &amp; 0x80)
                crc = (crc &lt;&lt; 1) ^ 0x07;
            else
                crc &lt;&lt;= 1;
        }
    }
    return crc;
}</code></pre>

<h3>Code Manchester</h3>
<pre><code class="language-c">void manchester_encode(uint8_t data, uint16_t *output) {
    for(int i=0; i&lt;8; i++) {
        if(data &amp; (1&lt;&lt;(7-i)))
            *output |= (0b01 &lt;&lt; (14-i*2)); // 1 → 01
        else
            *output |= (0b10 &lt;&lt; (14-i*2)); // 0 → 10
    }
}</code></pre>

</div>

<div class="lang-en">

<h1>Telecommunications - Semester 3</h1>

<p><strong>Year</strong>: 2021-2022 | <strong>Semester</strong>: 3 | <strong>Type</strong>: Technical</p>

<hr>

<h2>PART A - General Course Overview</h2>

<h3>Context and objectives</h3>

<p>Introduction to digital telecommunications systems: coding, modulations, transmission over noisy channels, error detection and correction. Foundation for Digital Telecom S4 and Networks.</p>

<p><strong>Objectives:</strong></p>
<ul>
<li>Line coding (NRZ, Manchester, etc.)</li>
<li>Basic digital modulations (ASK, FSK, PSK)</li>
<li>Transmission channel (noise, attenuation)</li>
<li>Error detection/correction (CRC, error-correcting codes)</li>
<li>Performance analysis (BER, SNR)</li>
</ul>

<h3>Prerequisites</h3>
<ul>
<li>Signals and systems (Fourier)</li>
<li>OL S3 (MATLAB, modulations)</li>
</ul>

<hr>

<h2>PART B: EXPERIENCE, CONTEXT AND FUNCTION</h2>

<h3>Module 1: Line Coding</h3>

<p><strong>Principle:</strong><br>
Transforming bits (0/1) into electrical signals suitable for transmission.</p>

<p><strong>Common codes:</strong></p>
<ul>
<li><strong>NRZ (Non-Return to Zero)</strong>: 0→-V, 1→+V. Simple but has DC component.</li>
<li><strong>RZ (Return to Zero)</strong>: return to 0 in mid-bit. Easier synchronization.</li>
<li><strong>Manchester (Biphase)</strong>: 0→high-to-low transition, 1→low-to-high. No DC, self-clocking (Ethernet 10Base-T).</li>
<li><strong>Miller</strong>: transition on 1, none on 0 (except two consecutive 0s). Bandwidth efficient.</li>
<li><strong>AMI (Alternate Mark Inversion)</strong>: 0→0V, 1→alternating +/-V. No DC.</li>
</ul>

<p><strong>Selection criteria:</strong></p>
<ul>
<li>Zero DC component (AC coupling)</li>
<li>Transition density (synchronization)</li>
<li>Bandwidth</li>
<li>Noise immunity</li>
</ul>

<h3>Module 2: Digital Modulations</h3>

<p><strong>ASK (Amplitude Shift Keying):</strong></p>
<ul>
<li>Carrier amplitude modulation</li>
<li>Noise sensitive</li>
<li>Rarely used alone</li>
</ul>

<p><strong>FSK (Frequency Shift Keying):</strong></p>
<ul>
<li>0→f1, 1→f2</li>
<li>Noise robust</li>
<li>Applications: low-speed modems, RFID, LoRa</li>
</ul>

<p><strong>PSK (Phase Shift Keying):</strong></p>
<ul>
<li><strong>BPSK</strong>: 0→0 degrees, 1→180 degrees (2 symbols). Robust.</li>
<li><strong>QPSK</strong>: 4 phases (0, 90, 180, 270 degrees) → 2 bits/symbol. WiFi, satellite.</li>
<li><strong>8-PSK</strong>: 8 phases → 3 bits/symbol.</li>
</ul>

<p><strong>QAM (Quadrature Amplitude Modulation):</strong></p>
<ul>
<li>Amplitude + phase modulation</li>
<li>16-QAM, 64-QAM, 256-QAM</li>
<li>High spectral efficiency (bits/Hz)</li>
<li>Applications: 4G/5G, cable, WiFi</li>
</ul>

<p><strong>Constellation:</strong><br>
I/Q (in-phase / quadrature) representation of symbols.</p>

<h3>Module 3: Transmission Channel</h3>

<p><strong>Channel model:</strong></p>
<ul>
<li>Attenuation (propagation losses)</li>
<li>AWGN noise (Additive White Gaussian Noise)</li>
<li>Interference</li>
<li>Distortion (multipath, dispersion)</li>
</ul>

<p><strong>SNR (Signal-to-Noise Ratio):</strong><br>
SNR(dB) = 10 log10(P_signal / P_noise)</p>

<p><strong>Shannon capacity:</strong><br>
C = B log2(1 + SNR) (bits/s)<br>
Theoretical maximum channel capacity.</p>

<p><strong>BER (Bit Error Rate):</strong><br>
Bit error rate. BER &lt; 10^-6 typical for reliable communications.</p>

<h3>Module 4: Error Detection and Correction</h3>

<p><strong>Error detection:</strong></p>
<ul>
<li><strong>Parity bit</strong>: even/odd. Detects odd errors.</li>
<li><strong>Checksum</strong>: byte sum.</li>
<li><strong>CRC (Cyclic Redundancy Check)</strong>: polynomial division. Very efficient (Ethernet, USB). CRC-16, CRC-32.</li>
</ul>

<p><strong>Error correction (FEC - Forward Error Correction):</strong></p>
<ul>
<li><strong>Hamming code</strong>: corrects 1 error, detects 2.</li>
<li><strong>Reed-Solomon codes</strong>: CD, DVD, QR codes. Burst error correction.</li>
<li><strong>Convolutional codes</strong>: memory, Viterbi decoding. Space, 4G.</li>
<li><strong>Turbo codes, LDPC</strong>: near Shannon limit. 5G.</li>
</ul>

<p><strong>Principle:</strong><br>
Adding redundancy (extra bits) to detect/correct errors without retransmission.</p>

<hr>

<h2>PART C: TECHNICAL ASPECTS</h2>

<h3>MATLAB Labs</h3>

<p><strong>Lab 1: Line coding</strong></p>
<ul>
<li>Bit sequence generation</li>
<li>NRZ, Manchester, AMI coding</li>
<li>Spectral analysis (PSD)</li>
</ul>

<p><strong>Lab 2: BPSK modulation</strong></p>
<ul>
<li>Carrier generation, modulation</li>
<li>AWGN channel (variable SNR)</li>
<li>Demodulation</li>
<li>BER vs SNR calculation</li>
</ul>

<p><strong>Lab 3: QPSK and constellation</strong></p>
<ul>
<li>QPSK modulation</li>
<li>I/Q constellation diagram</li>
<li>Noise impact on constellation</li>
</ul>

<p><strong>Lab 4: CRC</strong></p>
<ul>
<li>CRC-8, CRC-16 implementation</li>
<li>Error detection testing (1 bit, 2 bits, burst)</li>
</ul>

<h3>Complete chain simulation project</h3>

<p><strong>Architecture:</strong></p>
<pre><code>[Bit source] → [Channel encoder] → [Modulator] → [AWGN Channel]
                                                        ↓
[Bit sink]   ← [Decoder]          ← [Demodulator]     ←</code></pre>

<p><strong>Parameters:</strong></p>
<ul>
<li>Modulation: QPSK</li>
<li>Error-correcting code: Hamming (7,4)</li>
<li>SNR: 0 to 15 dB</li>
<li>Bitrate: 1 Mbps</li>
</ul>

<p><strong>Results:</strong></p>
<ul>
<li>BER vs SNR curves (with/without coding)</li>
<li>Coding gain (approximately 3-5 dB)</li>
</ul>

<hr>

<h2>PART D: ANALYSIS AND REFLECTION</h2>

<h3>Assessment</h3>
<ul>
<li>MATLAB labs (40%)</li>
<li>Transmission chain project (30%)</li>
<li>Tests (15%)</li>
<li>Final exam (15%)</li>
</ul>

<h3>Skills acquired</h3>
<ul>
<li>Understanding digital telecommunications systems</li>
<li>MATLAB simulation (modulations, channel, BER)</li>
<li>Performance analysis (SNR, BER, capacity)</li>
<li>Error detection/correction coding</li>
<li>Foundations for 4G/5G, WiFi, satellite</li>
</ul>

<h3>Professional applications</h3>
<ul>
<li>Telecommunications (mobile, satellite, fiber)</li>
<li>Wireless networks (WiFi, LoRa, Bluetooth)</li>
<li>RF/telecom engineer</li>
<li>IoT (low-bitrate protocols)</li>
</ul>

<h2>Digital communication chain</h2>

<h3>Characteristics</h3>
<ul>
<li>Bit rate (bits/s)</li>
<li>Bandwidth (Hz)</li>
<li>Spectral efficiency (bits/s/Hz)</li>
<li>Error probability (BER)</li>
<li>Signal-to-noise ratio (SNR)</li>
</ul>

<h3>Line coding</h3>

<h4>Principle</h4>
<p>Electrical representation of binary data for transmission over a channel.</p>

<h4>NRZ codes (Non Return to Zero)</h4>
<p><strong>NRZ-L (Level):</strong></p>
<ul>
<li>0: low level</li>
<li>1: high level</li>
<li>Simple but has DC component</li>
<li>No self-synchronization</li>
</ul>

<p><strong>NRZ-I (Inverted):</strong></p>
<ul>
<li>Transition on '1's</li>
<li>No transition on '0's</li>
<li>Better synchronization</li>
</ul>

<h4>RZ codes (Return to Zero)</h4>
<ul>
<li>Return to zero in mid-bit</li>
<li>Better synchronization</li>
<li>Doubled bandwidth</li>
</ul>

<h4>Manchester code</h4>
<ul>
<li>Transition in the middle of each bit</li>
<li>0: high → low</li>
<li>1: low → high</li>
<li>Self-synchronization</li>
<li>Used in Ethernet 10BASE-T</li>
</ul>

<h4>Differential Manchester code</h4>
<ul>
<li>Transition at bit start</li>
<li>Presence/absence of mid-bit transition</li>
</ul>

<h4>Bipolar code (AMI)</h4>
<ul>
<li>0: zero level</li>
<li>1: alternating +V and -V</li>
<li>No DC component</li>
<li>Error detection</li>
</ul>

<h4>MLT-3, PAM-5 codes</h4>
<ul>
<li>Multi-level</li>
<li>Improved spectral efficiency</li>
<li>Used in Fast Ethernet</li>
</ul>

<h3>Baseband transmission</h3>

<h4>Nyquist criterion</h4>
<ul>
<li>No inter-symbol interference (ISI)</li>
<li>Raised cosine filter</li>
<li>Roll-off factor</li>
<li>Minimum bandwidth</li>
</ul>

<h4>Eye diagram</h4>
<ul>
<li>Quality evaluation tool</li>
<li>Vertical opening (noise margin)</li>
<li>Horizontal opening (timing)</li>
<li>Bit error rate (BER)</li>
</ul>

<h4>Equalization</h4>
<ul>
<li>Channel distortion compensation</li>
<li>Linear equalizer</li>
<li>Adaptive equalizer (LMS)</li>
<li>Decision feedback equalizer (DFE)</li>
</ul>

<h3>Error detection and correction</h3>

<h4>Detection codes</h4>

<p><strong>Simple parity:</strong></p>
<ul>
<li>Even or odd parity bit</li>
<li>Detects single error</li>
<li>Does not correct</li>
</ul>

<p><strong>Cross parity (2D):</strong></p>
<ul>
<li>Row and column parity</li>
<li>Detects and corrects some errors</li>
</ul>

<p><strong>CRC (Cyclic Redundancy Check):</strong></p>
<ul>
<li>Generator polynomial</li>
<li>Polynomial division remainder</li>
<li>CRC-8, CRC-16, CRC-32</li>
<li>Very efficient for detection</li>
</ul>

<h4>Error-correcting codes</h4>

<p><strong>Hamming code:</strong></p>
<ul>
<li>Hamming distance</li>
<li>Corrects 1 bit, detects 2 bits</li>
<li>Hamming(7,4), Hamming(15,11)</li>
<li>Parity bits positioned at 2^n</li>
</ul>

<p><strong>Reed-Solomon code:</strong></p>
<ul>
<li>Non-binary cyclic code</li>
<li>Burst error correction</li>
<li>Used in CD, DVD, QR codes</li>
<li>RS(255,223) typical</li>
</ul>

<p><strong>Convolutional codes:</strong></p>
<ul>
<li>Continuous encoding</li>
<li>Viterbi decoding</li>
<li>Used in mobile telephony</li>
<li>Rate r = k/n</li>
</ul>

<p><strong>Turbo codes and LDPC:</strong></p>
<ul>
<li>Modern high-performance codes</li>
<li>Near Shannon limit</li>
<li>4G, 5G, satellites</li>
</ul>

<h3>Transmission performance</h3>

<h4>Bit error probability (BER)</h4>
<ul>
<li>BER = errors / transmitted bits</li>
<li>Depends on SNR</li>
<li>Targets: 10^-6 to 10^-12</li>
</ul>

<h4>Eb/N0 ratio</h4>
<ul>
<li>Energy per bit / Noise density</li>
<li>Quality measure</li>
<li>BER vs Eb/N0 curves</li>
</ul>

<h4>Shannon capacity</h4>
<ul>
<li>C = B log2(1 + SNR)</li>
<li>Theoretical limit</li>
<li>Maximum error-free bitrate</li>
</ul>

<h2>Lab work</h2>

<h3>Line coding lab</h3>
<ul>
<li>Code generation (NRZ, Manchester, AMI)</li>
<li>Spectral analysis</li>
<li>Transmission simulation</li>
<li>Eye diagram</li>
</ul>

<h3>CRC lab</h3>
<ul>
<li>CRC algorithm implementation</li>
<li>Error detection testing</li>
<li>Comparison of CRC-8, CRC-16, CRC-32</li>
<li>Microcontroller application</li>
</ul>

<h3>Hamming code lab</h3>
<ul>
<li>Hamming(7,4) encoding</li>
<li>Decoding and correction</li>
<li>Error insertion</li>
<li>Correction rate</li>
</ul>

<h3>Communication project</h3>
<ul>
<li>Coded serial link</li>
<li>CRC protection</li>
<li>Application protocol</li>
<li>Robustness testing</li>
</ul>

<h2>Tools used</h2>

<h3>Simulation</h3>
<ul>
<li><strong>MATLAB/Simulink</strong>: System simulation</li>
<li><strong>Python</strong>: Algorithm programming</li>
<li><strong>GNU Radio</strong>: SDR and communications</li>
<li><strong>LabVIEW</strong>: Acquisition and processing</li>
</ul>

<h3>Development</h3>
<ul>
<li><strong>STM32</strong>: Embedded implementation</li>
<li><strong>Arduino</strong>: Rapid prototyping</li>
<li><strong>UART, SPI, I2C</strong>: Interfaces</li>
</ul>

<h3>Measurement</h3>
<ul>
<li><strong>Oscilloscope</strong>: Signals and eye diagram</li>
<li><strong>Logic analyzer</strong>: Protocol decoding</li>
<li><strong>BERT (Bit Error Rate Tester)</strong>: BER measurement</li>
</ul>

<h2>Assessment</h2>
<ul>
<li>Lab work (40%)</li>
<li>Communication project (30%)</li>
<li>Continuous assessment (15%)</li>
<li>Final exam (15%)</li>
</ul>

<h2>Links with other courses</h2>
<ul>
<li><strong>SE</strong>: Signal processing</li>
<li><strong>OL</strong>: Modulation/demodulation</li>
<li><strong>IE</strong>: Protocol implementation</li>
<li><strong>Digital Telecommunications (S4)</strong>: Advanced topics</li>
<li><strong>Network</strong>: Protocol layers</li>
</ul>

<h2>Calculation examples</h2>

<h3>Hamming distance</h3>
<p>Number of different bits between two words:</p>
<ul>
<li>101101 vs 101111 → distance = 1</li>
<li>101101 vs 010001 → distance = 3</li>
</ul>

<h3>CRC-8</h3>
<p>Polynomial: x^8 + x^2 + x + 1 (0x107)</p>
<pre><code>Message : 11010011101100
Remainder: 10101010
Transmitted message: 11010011101100 10101010</code></pre>

<h3>Hamming code (7,4)</h3>
<p>4 data bits: d1 d2 d3 d4<br>
3 parity bits: p1 p2 p3</p>
<p>Position: p1 p2 d1 p3 d2 d3 d4</p>
<pre><code>p1 = d1 XOR d2 XOR d4
p2 = d1 XOR d3 XOR d4
p3 = d2 XOR d3 XOR d4</code></pre>

<h2>Practical applications</h2>

<h3>Wired networks</h3>
<ul>
<li>Ethernet (Manchester)</li>
<li>USB (NRZI)</li>
<li>RS-232/RS-485</li>
</ul>

<h3>Wireless communications</h3>
<ul>
<li>WiFi (OFDM + codes)</li>
<li>Bluetooth (FEC)</li>
<li>Zigbee</li>
</ul>

<h3>Storage</h3>
<ul>
<li>Hard drives (Reed-Solomon)</li>
<li>Flash memory (BCH, LDPC)</li>
<li>QR codes</li>
</ul>

<h3>Audiovisual</h3>
<ul>
<li>DVB (digital television)</li>
<li>DAB (digital radio)</li>
<li>HDMI</li>
</ul>

<h2>Skills developed</h2>
<ul>
<li>Data encoding and decoding</li>
<li>Transmission performance analysis</li>
<li>Implementation of protection algorithms</li>
<li>Communication link diagnostics</li>
<li>Digital system simulation</li>
<li>BER measurement and optimization</li>
</ul>

<h2>Protocols studied</h2>

<h3>Data link protocol</h3>
<ul>
<li>Framing</li>
<li>Synchronization</li>
<li>Error detection (CRC)</li>
<li>Acknowledgments (ACK/NACK)</li>
<li>Retransmission (ARQ)</li>
</ul>

<h3>Example: Simple protocol</h3>
<pre><code>[Start] [Length] [Data] [CRC16] [Stop]
  0x02     1B      nB      2B     0x03</code></pre>

<h2>Common issues</h2>

<h3>Transmission</h3>
<ul>
<li>Signal attenuation</li>
<li>Noise (thermal, impulsive)</li>
<li>Distortion (ISI)</li>
<li>Clock drift</li>
<li>Reflections (impedance)</li>
</ul>

<h3>Coding</h3>
<ul>
<li>Excessive DC component</li>
<li>Too wide bandwidth</li>
<li>Loss of synchronization</li>
<li>Insufficient error detection</li>
</ul>

<h2>Embedded implementation</h2>

<h3>CRC on microcontroller</h3>
<pre><code class="language-c">uint8_t crc8(uint8_t *data, uint8_t len) {
    uint8_t crc = 0;
    for(uint8_t i=0; i&lt;len; i++) {
        crc ^= data[i];
        for(uint8_t j=0; j&lt;8; j++) {
            if(crc &amp; 0x80)
                crc = (crc &lt;&lt; 1) ^ 0x07;
            else
                crc &lt;&lt;= 1;
        }
    }
    return crc;
}</code></pre>

<h3>Manchester code</h3>
<pre><code class="language-c">void manchester_encode(uint8_t data, uint16_t *output) {
    for(int i=0; i&lt;8; i++) {
        if(data &amp; (1&lt;&lt;(7-i)))
            *output |= (0b01 &lt;&lt; (14-i*2)); // 1 → 01
        else
            *output |= (0b10 &lt;&lt; (14-i*2)); // 0 → 10
    }
}</code></pre>

</div>

<div style="display: flex; gap: 20px; justify-content: center; flex-wrap: wrap; margin: 20px 0;">
  <div style="text-align: center;">
    <img src="/assets/images/courses/S3/telecom/nucleo_l152re_2017_9_22_mor_left.png" alt="Nucleo L152RE" style="max-width: 400px; width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" />
    <p style="margin-top: 8px; font-style: italic; color: #666;">
      <span class="lang-fr">Carte Nucleo L152RE - Vue gauche</span>
      <span class="lang-en">Nucleo L152RE Board - Left view</span>
    </p>
  </div>
  <div style="text-align: center;">
    <img src="/assets/images/courses/S3/telecom/nucleo_l152re_2017_9_22_mor_right.png" alt="Nucleo L152RE" style="max-width: 400px; width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" />
    <p style="margin-top: 8px; font-style: italic; color: #666;">
      <span class="lang-fr">Carte Nucleo L152RE - Vue droite</span>
      <span class="lang-en">Nucleo L152RE Board - Right view</span>
    </p>
  </div>
</div>

<style>body{font-family:Arial,sans-serif;background-color:#f4f4f9;color:#333;line-height:1.6}h2,h3,h4,h5{color:#2a7ae2}p{text-align:justify}code{background-color:#f5f5f5;padding:2px 6px;border-radius:3px;font-family:'Courier New',monospace}pre{background-color:#f5f5f5;padding:15px;border-radius:5px;overflow-x:auto}</style>

<div class="back-nav">
  <a href="./my-courses-2021-2022.html" data-i18n-html="back-courses-2021-2022">&larr; Retour a Mes Cours 2021-2022</a>
</div>

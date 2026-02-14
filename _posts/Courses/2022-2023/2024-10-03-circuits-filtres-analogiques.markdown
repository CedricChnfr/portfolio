---
layout: default
title: "Circuits et Filtres Analogiques - S5"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
---

<style>
.back-nav {
  margin-bottom: 20px;
}
.back-nav a {
  text-decoration: none;
  color: #2a7ae2;
  font-weight: 600;
}
.back-nav a:hover {
  text-decoration: underline;
}
.section-title {
  color: #2a7ae2;
  border-bottom: 2px solid #2a7ae2;
  padding-bottom: 10px;
  margin-top: 30px;
  margin-bottom: 20px;
}
</style>

<div class="back-nav">
  <a href="./my-courses-2022-2023.html" data-i18n-html="back-courses-2022-2023">← Retour aux Cours 2022-2023</a>
</div>

<!-- ==================== FRENCH VERSION ==================== -->
<div class="lang-fr">

<h1>Circuits et Filtres Analogiques - S5</h1>

<p><strong>Année</strong>: 2022-2023 (Semestre 5)<br/>
<strong>Crédits</strong>: 3 ECTS<br/>
<strong>Type</strong>: Électronique Analogique</p>

<hr/>

<h2>PART A: PRÉSENTATION GÉNÉRALE</h2>

<h3>Objectifs du cours</h3>

<p>Le cours "Circuits et Filtres Analogiques" fournit une compréhension approfondie de l'analyse et de la conception de circuits électroniques analogiques, avec un accent particulier sur la théorie des filtres. Il couvre l'utilisation des amplificateurs opérationnels, l'analyse fréquentielle via les diagrammes de Bode, et l'analyse temporelle via la transformée de Laplace. Ce cours est fondamental pour la conception de chaînes d'acquisition de signaux, le conditionnement de capteurs, et le traitement analogique du signal.</p>

<h3>Compétences visées</h3>

<ul>
  <li>Maîtriser l'analyse fréquentielle des circuits (diagrammes de Bode, fonction de transfert)</li>
  <li>Concevoir des filtres actifs et passifs (passe-bas, passe-haut, passe-bande)</li>
  <li>Utiliser les amplificateurs opérationnels dans diverses configurations</li>
  <li>Appliquer la transformée de Laplace pour l'analyse temporelle</li>
  <li>Dimensionner des circuits analogiques pour des applications spécifiques</li>
  <li>Simuler et valider des circuits avec LTspice</li>
  <li>Analyser les systèmes du 1er et 2ème ordre</li>
</ul>

<h3>Organisation</h3>

<ul>
  <li><strong>Volume horaire</strong>: 36h (CM: 20h, TD: 8h, TP: 8h)</li>
  <li><strong>Évaluation</strong>: Examen écrit (60%) + TDs/TPs (30%) + Contrôle continu (10%)</li>
  <li><strong>Semestre</strong>: 5 (2022-2023)</li>
  <li><strong>Prérequis</strong>: Électronique fondamentale, mathématiques (nombres complexes, dérivées, intégrales)</li>
</ul>

<hr/>

<h2>PART B: EXPÉRIENCE, CONTEXTE ET FONCTION</h2>

<h3>Contenu pédagogique</h3>

<p>Le cours s'articule autour de trois grandes parties couvrant les aspects théoriques et pratiques de l'électronique analogique.</p>

<h4>1. Amplificateurs Opérationnels et Montages de Base</h4>

<p><strong>Amplificateur Opérationnel Idéal</strong>:</p>

<p>L'amplificateur opérationnel (AO ou op-amp) est le composant fondamental de l'électronique analogique moderne.</p>

<p><strong>Caractéristiques de l'AO idéal</strong>:</p>
<ul>
  <li>Gain en tension différentiel infini: Ad = ∞</li>
  <li>Impédance d'entrée infinie: Zin = ∞ (courants d'entrée nuls)</li>
  <li>Impédance de sortie nulle: Zout = 0</li>
  <li>Bande passante infinie</li>
  <li>Tension de décalage (offset) nulle</li>
  <li>Rejet du mode commun infini (CMRR = ∞)</li>
</ul>

<p><strong>Règles de l'AO idéal en régime linéaire</strong> (contre-réaction négative):</p>
<ol>
  <li>V+ = V- (égalité des tensions d'entrée)</li>
  <li>I+ = I- = 0 (courants d'entrée nuls)</li>
</ol>

<p><strong>Montages fondamentaux</strong>:</p>

<p><strong>Amplificateur inverseur</strong>:</p>
<div style="text-align: center; display: flex; justify-content: center; gap: 20px;">
  <img src="/img/Courses/S5/Circuits-Filtres-Analogiques/inverseur.png" style="width: 45%;"/>
  <img src="/img/Courses/S5/Circuits-Filtres-Analogiques/inverseur2.png" style="width: 45%;"/>
</div>
<br>

<p><strong>Amplificateur non-inverseur</strong>:</p>
<pre><code>         R2
     ----/\/\/----
     |           |
     +-[AO+]-----+---- Vs
     |  |  -|
Ve --+  |   |
        R1  |
         \  |
          \ |
           GND
</code></pre>

<p>Fonction de transfert:<br/>
H = Vs/Ve = 1 + (R2/R1)</p>

<p>Impédance d'entrée: Zin = ∞ (très élevée)</p>

<p><strong>Suiveur (buffer)</strong>:<br/>
Configuration non-inverseuse avec R2 = 0 et R1 = ∞</p>

<p>H = 1</p>

<p>Utilisé pour adapter les impédances (isolation).</p>

<p><strong>Sommateur inverseur</strong>:</p>
<pre><code>Ve1 -R1-\
Ve2 -R2--+-[AO-]---- Vs
Ve3 -R3-/  |   +|
           R4  |--- GND
</code></pre>

<p>Vs = -R4 × (Ve1/R1 + Ve2/R2 + Ve3/R3)</p>

<p>Si R1 = R2 = R3 = R4 = R:<br/>
Vs = -(Ve1 + Ve2 + Ve3)</p>

<p><strong>Soustracteur (amplificateur différentiel)</strong>:</p>
<pre><code>Ve1 -R1--[AO-]---R2--- Vs
         |  +|
Ve2 -R3--+   |
         R4  |
          \  |
           GND
</code></pre>

<p>Si R1 = R2 et R3 = R4:<br/>
Vs = (R2/R1) × (Ve2 - Ve1)</p>

<p><strong>Intégrateur</strong>:</p>
<pre><code>        C
    ----||----
    |        |
Ve -R1-[AO-]-+---- Vs
       |   +|
       |    |--- GND
</code></pre>

<p>Vs(t) = -(1/(R×C)) × ∫Ve(t)dt + Vs(0)</p>

<p>En fréquentiel:<br/>
H(jω) = -1/(jRCω)</p>

<p><strong>Dérivateur</strong>:</p>
<pre><code>        R2
    ----/\/\/----
    |           |
Ve -C1-[AO-]----+---- Vs
       |   +|
       |    |--- GND
</code></pre>

<p>Vs(t) = -RC × dVe(t)/dt</p>

<p>En fréquentiel:<br/>
H(jω) = -jRCω</p>

<p><strong>Supports de cours</strong>:</p>
<ul>
  <li><a href="/cours-pdf/S5/Circuits-Filtres-Analogiques/Montages_AOs.pdf">Montage à base d'AOs</a></li>
</ul>

<h4>2. Fonctions de Transfert et Analyse Fréquentielle</h4>

<p><strong>Fonction de transfert</strong>:</p>

<p>La fonction de transfert H(jω) d'un système linéaire relie la sortie à l'entrée en régime harmonique:</p>

<p>H(jω) = Vs(jω)/Ve(jω)</p>

<p>où j = √(-1) et ω = 2πf (pulsation en rad/s)</p>

<p><strong>Module et phase</strong>:<br/>
H(jω) = |H(jω)| × exp(jφ(ω))</p>

<ul>
  <li><strong>Module</strong> (gain): |H(jω)|, souvent exprimé en décibels (dB)<br/>
  GdB = 20 × log10(|H(jω)|)</li>
  <li><strong>Phase</strong>: φ(ω) = arg(H(jω)), exprimée en degrés ou radians</li>
</ul>

<p><strong>Diagramme de Bode</strong>:</p>

<p>Représentation graphique de la fonction de transfert:</p>
<ul>
  <li><strong>Diagramme de gain</strong>: GdB en fonction de log(f)</li>
  <li><strong>Diagramme de phase</strong>: φ en fonction de log(f)</li>
</ul>

<p><strong>Filtres du 1er ordre</strong>:</p>

<p><strong>Filtre passe-bas RC passif</strong>:</p>
<pre><code>Ve ---R---+--- Vs
          |
          C
          |
         GND
</code></pre>

<p>Fonction de transfert:<br/>
H(jω) = 1/(1 + jRCω) = 1/(1 + j(ω/ω0))</p>

<p>où ω0 = 1/(RC) est la pulsation de coupure.</p>

<p>Fréquence de coupure à -3dB:<br/>
f0 = 1/(2πRC)</p>

<p><strong>Comportement asymptotique</strong>:</p>
<ul>
  <li>Basses fréquences (ω &lt;&lt; ω0): H ≈ 1 → 0 dB</li>
  <li>Hautes fréquences (ω &gt;&gt; ω0): H ≈ ω0/ω → pente -20 dB/décade</li>
</ul>

<p><strong>Phase</strong>:<br/>
φ(ω) = -arctan(ω/ω0)</p>

<p>À la fréquence de coupure: φ(ω0) = -45°</p>

<p><strong>Filtre passe-haut CR passif</strong>:</p>
<pre><code>Ve ---C---+--- Vs
          |
          R
          |
         GND
</code></pre>

<p>Fonction de transfert:<br/>
H(jω) = (jRCω)/(1 + jRCω) = j(ω/ω0)/(1 + j(ω/ω0))</p>

<p><strong>Filtres du 2ème ordre</strong>:</p>

<p>Forme canonique:<br/>
H(p) = (H0 × ω0²)/(p² + (ω0/Q)×p + ω0²)</p>

<p>où:</p>
<ul>
  <li>p = jω (variable de Laplace en régime harmonique)</li>
  <li>ω0: pulsation propre (ou pulsation de résonance)</li>
  <li>Q: facteur de qualité</li>
  <li>H0: gain statique</li>
</ul>

<p><strong>Facteur de qualité Q</strong> (ou coefficient d'amortissement ξ = 1/(2Q)):</p>
<ul>
  <li>Q &lt; 0.5 (ξ &gt; 1): système suramort (pas de dépassement)</li>
  <li>Q = 0.5 (ξ = 1): amortissement critique</li>
  <li>Q = 0.707 (ξ = 0.707): réponse de Butterworth (maximalement plate)</li>
  <li>Q &gt; 0.707: système sous-amorti (dépassement, résonance)</li>
</ul>

<p><strong>Filtre passe-bas du 2ème ordre (Sallen-Key)</strong>:</p>
<pre><code>Ve -R1--+--R2--+-----[AO+]---- Vs
        |      |      |  -|
        C1     C2     +---+
        |      |          |
       GND    GND        R3
                          |
                         R4
                          |
                         GND
</code></pre>

<p>Pour un filtre de Butterworth (Q = 0.707), configuration unitaire:</p>

<p>H(jω) = 1/(1 + √2 × j(ω/ω0) - (ω/ω0)²)</p>

<p><strong>Pente de coupure</strong>: -40 dB/décade (2 × 20 dB/décade)</p>

<p><strong>Quadripôles</strong>:</p>

<p>Un quadripôle est un système à 2 ports (entrée et sortie) caractérisé par des matrices de transfert.</p>

<p><strong>Matrice impédance [Z]</strong>:</p>
<pre><code>[V1]   [Z11  Z12] [I1]
[V2] = [Z21  Z22] [I2]
</code></pre>

<p><strong>Matrice admittance [Y] = [Z]⁻¹</strong></p>

<p><strong>Matrice de transmission (ABCD)</strong>:</p>
<pre><code>[V1]   [A  B] [V2 ]
[I1] = [C  D] [-I2]
</code></pre>

<p>Avantage: pour des quadripôles en cascade, on multiplie les matrices ABCD.</p>

<p><strong>Supports de cours</strong>:</p>
<ul>
  <li><a href="/cours-pdf/S5/Circuits-Filtres-Analogiques/TransfertBode.pdf">Fonction de Transfert et Bode</a></li>
  <li><a href="/cours-pdf/S5/Circuits-Filtres-Analogiques/Ordre-deux-frequentiel.pdf">Ordre 2 fréquentiel</a></li>
  <li><a href="/cours-pdf/S5/Circuits-Filtres-Analogiques/Quadripole.pdf">Quadripôles et fonctions de transfert</a></li>
</ul>

<h4>3. Transformée de Laplace et Analyse Temporelle</h4>

<p><strong>Transformée de Laplace</strong>:</p>

<p>Outil mathématique permettant de transformer les équations différentielles en équations algébriques.</p>

<p>L{f(t)} = F(p) = ∫[0 à ∞] f(t) × exp(-pt) dt</p>

<p>où p = σ + jω est la variable complexe de Laplace.</p>

<p><strong>Transformées usuelles</strong>:</p>

<table>
  <thead>
    <tr><th>Signal temporel f(t)</th><th>Transformée F(p)</th></tr>
  </thead>
  <tbody>
    <tr><td>Échelon u(t)</td><td>1/p</td></tr>
    <tr><td>Impulsion δ(t)</td><td>1</td></tr>
    <tr><td>Rampe t×u(t)</td><td>1/p²</td></tr>
    <tr><td>Exponentielle exp(-at)×u(t)</td><td>1/(p+a)</td></tr>
    <tr><td>Sinus sin(ωt)×u(t)</td><td>ω/(p² + ω²)</td></tr>
    <tr><td>Cosinus cos(ωt)×u(t)</td><td>p/(p² + ω²)</td></tr>
  </tbody>
</table>

<p><strong>Propriétés de la transformée</strong>:</p>

<ul>
  <li><strong>Linéarité</strong>: L{a×f(t) + b×g(t)} = a×F(p) + b×G(p)</li>
  <li><strong>Dérivation</strong>: L{df/dt} = p×F(p) - f(0⁻)</li>
  <li><strong>Intégration</strong>: L{∫[0 à t] f(τ)dτ} = F(p)/p</li>
  <li><strong>Théorème du retard</strong>: L{f(t-τ)×u(t-τ)} = exp(-pτ)×F(p)</li>
  <li><strong>Théorème de la valeur initiale</strong>: f(0⁺) = lim[p→∞] p×F(p)</li>
  <li><strong>Théorème de la valeur finale</strong>: f(∞) = lim[p→0] p×F(p)</li>
</ul>

<p><strong>Application aux circuits</strong>:</p>

<p>En transformée de Laplace, les éléments deviennent:</p>
<ul>
  <li><strong>Résistance</strong>: R (inchangée)</li>
  <li><strong>Condensateur</strong>: impédance 1/(pC)</li>
  <li><strong>Inductance</strong>: impédance pL</li>
</ul>

<p><strong>Exemple - Circuit RC</strong>:</p>

<p>Équation temporelle:<br/>
RC × dVs/dt + Vs = Ve</p>

<p>En Laplace (conditions initiales nulles):<br/>
RC × p×Vs(p) + Vs(p) = Ve(p)</p>

<p>Fonction de transfert:<br/>
H(p) = Vs(p)/Ve(p) = 1/(1 + RCp)</p>

<p><strong>Réponse temporelle d'un système du 2ème ordre</strong>:</p>

<p>Pour un système du 2ème ordre:<br/>
H(p) = ω0²/(p² + 2ξω0×p + ω0²)</p>

<p><strong>Réponse indicielle</strong> (entrée échelon):</p>

<ul>
  <li><strong>Cas suramort</strong> (ξ &gt; 1): deux pôles réels distincts, pas de dépassement</li>
  <li><strong>Cas critique</strong> (ξ = 1): pôle réel double, réponse la plus rapide sans dépassement</li>
  <li><strong>Cas sous-amorti</strong> (0 &lt; ξ &lt; 1): pôles complexes conjugués, oscillations amorties</li>
</ul>

<p>Vs(t) = V0 × [1 - (exp(-ξω0×t)/√(1-ξ²)) × sin(ωd×t + φ)]</p>

<p>où ωd = ω0×√(1-ξ²) (pseudo-pulsation)</p>

<p><strong>Dépassement</strong> (overshoot):<br/>
D% = 100 × exp(-πξ/√(1-ξ²))</p>

<p>Pour Q = 0.707 (ξ = 0.707): D ≈ 4.3%</p>

<p><strong>Temps de montée</strong> tm (10% à 90%):<br/>
tm ≈ 2.2/ω0</p>

<p><strong>Temps de réponse</strong> tr (à 5%):<br/>
tr ≈ 3/(ξω0)</p>

<p><strong>Circuits RLC</strong>:</p>

<p><strong>Circuit RLC série</strong>:</p>

<p>Équation différentielle:<br/>
L × d²i/dt² + R × di/dt + (1/C)×i = dVe/dt</p>

<p>En Laplace:<br/>
H(p) = I(p)/Ve(p) = pC/(LCp² + RCp + 1)</p>

<p><strong>Pulsation propre</strong>: ω0 = 1/√(LC)</p>

<p><strong>Facteur de qualité</strong>: Q = (1/R)×√(L/C) = (ω0×L)/R</p>

<p><strong>Analyse des signaux</strong>:</p>

<ul>
  <li><strong>Fonction de transfert harmonique</strong>: réponse en régime sinusoïdal permanent</li>
  <li><strong>Réponse impulsionnelle</strong>: h(t) = L⁻¹{H(p)}</li>
  <li><strong>Réponse indicielle</strong>: s(t) = L⁻¹{H(p)/p}</li>
  <li><strong>Convolution</strong>: y(t) = h(t) * x(t) = ∫[-∞ à ∞] h(τ)×x(t-τ) dτ</li>
</ul>

<p><strong>Supports de cours</strong>:</p>
<ul>
  <li><a href="/cours-pdf/S5/Circuits-Filtres-Analogiques/Laplace.pdf">Transformée de Laplace</a></li>
  <li><a href="/cours-pdf/S5/Circuits-Filtres-Analogiques/Ordre-deux-temporel.pdf">Ordre 2 temporel</a></li>
  <li><a href="/cours-pdf/S5/Circuits-Filtres-Analogiques/Laplace-RLC.pdf">Laplace et circuits RLC</a></li>
  <li><a href="/cours-pdf/S5/Circuits-Filtres-Analogiques/Laplace-Signaux.pdf">Laplace et signaux</a></li>
</ul>

<hr/>

<h2>PART C: ASPECTS TECHNIQUES</h2>

<p>Cette section présente les travaux pratiques et exercices réalisés.</p>

<h3>Travaux Pratiques avec LTspice</h3>

<h4>TP1: Cellules CR et RC</h4>

<p><strong>Objectif</strong>: Étude des filtres passifs du 1er ordre et validation par simulation.</p>

<p><strong>Cellule RC (Passe-Bas)</strong>:</p>

<p>Schéma simulé dans LTspice:</p>
<pre><code>Circuit RC passe-bas:
V1 (AC source) --- R1 (1kΩ) ---+--- Vout
                                |
                               C1 (100nF)
                                |
                               GND
</code></pre>

<p><strong>Calcul théorique</strong>:<br/>
f0 = 1/(2π×RC) = 1/(2π × 1000 × 100×10⁻⁹) = 1.59 kHz</p>

<p><strong>Simulation</strong>:</p>
<ul>
  <li>Analyse AC de 10 Hz à 100 kHz</li>
  <li>Tracé du diagramme de Bode (gain et phase)</li>
  <li>Vérification de la fréquence de coupure à -3 dB</li>
  <li>Pente de -20 dB/décade après f0</li>
</ul>

<p><strong>Cellule CR (Passe-Haut)</strong>:</p>

<pre><code>Circuit CR passe-haut:
V1 (AC source) --- C1 (100nF) ---+--- Vout
                                 |
                                R1 (1kΩ)
                                 |
                                GND
</code></pre>

<p>Même fréquence de coupure: f0 = 1.59 kHz</p>

<p><strong>Comportement</strong>:</p>
<ul>
  <li>Atténuation des basses fréquences</li>
  <li>Gain unitaire (0 dB) aux hautes fréquences</li>
  <li>Pente de +20 dB/décade avant f0</li>
  <li>Déphasage de 0° à +90°</li>
</ul>

<p><strong>Mesures effectuées</strong>:</p>
<ul>
  <li>Gain à différentes fréquences (tableau de valeurs)</li>
  <li>Phase à différentes fréquences</li>
  <li>Comparaison mesures/théorie</li>
  <li>Impact des composants réels (tolérances)</li>
</ul>

<p><strong>Supports de cours</strong>:<br/>
<a href="/cours-pdf/S5/Circuits-Filtres-Analogiques/Compte_rendu_Chanfreau_Jumin.pdf">Compte rendu TP</a></p>

<h4>TP1: Filtre Sallen-Key</h4>

<p><strong>Objectif</strong>: Réalisation d'un filtre actif passe-bas du 2ème ordre.</p>

<p><strong>Topologie Sallen-Key unitaire</strong>:</p>

<pre><code>Circuit Sallen-Key (gain unitaire):
           R1        R2
Ve ----/\/\/\--+-/\/\/\--+-----[AO+]---- Vs
               |         |      |  -|
               C1       C2      +---+
               |         |
              GND       GND
</code></pre>

<p><strong>Dimensionnement pour Butterworth</strong>:</p>

<p>Pour f0 = 1 kHz et Q = 0.707:</p>

<p>Choix: C1 = C2 = C = 100 nF</p>

<p>R = 1/(2π×f0×C) = 1/(2π × 1000 × 100×10⁻⁹) = 1.59 kΩ</p>

<p>On prend R1 = R2 = 1.6 kΩ (valeur normalisée E24)</p>

<p><strong>Simulation LTspice</strong>:</p>
<ul>
  <li>Analyse AC: diagramme de Bode</li>
  <li>Vérification f0, Q, et pente -40 dB/décade</li>
  <li>Analyse temporelle (réponse indicielle): mesure du dépassement (~4.3% attendu)</li>
  <li>Analyse transitoire avec signal carré: observation de la réponse</li>
</ul>

<p><strong>Comparaison 1er ordre vs 2ème ordre</strong>:</p>
<ul>
  <li>Sélectivité supérieure du 2ème ordre</li>
  <li>Pente de coupure doublée</li>
  <li>Possibilité de résonance si Q &gt; 0.707</li>
</ul>

<h3>Exercices de TD</h3>

<h4>TD1: Analyse de filtres passifs</h4>

<p><strong>Exercice type</strong>: Déterminer la fonction de transfert d'un filtre RC série puis parallèle.</p>

<p><strong>Calcul d'impédances complexes</strong>:</p>

<p>Pour un condensateur: Zc = 1/(jCω)</p>

<p>Diviseur de tension:<br/>
H(jω) = Z2/(Z1 + Z2)</p>

<p><strong>Application numérique</strong>: calculer gain et phase pour plusieurs fréquences.</p>

<h4>TD2: Amplificateurs opérationnels</h4>

<p><strong>Exercice</strong>: Dimensionner un amplificateur non-inverseur de gain 10.</p>

<p>H = 1 + (R2/R1) = 10</p>

<p>Donc: R2/R1 = 9</p>

<p>Choix: R1 = 10 kΩ, R2 = 90 kΩ</p>

<p><strong>Vérification de la bande passante</strong>:</p>

<p>Pour un AO réel (ex: TL081):</p>
<ul>
  <li>GBP (Gain-Bandwidth Product) = 3 MHz</li>
  <li>Bande passante à gain 10: fBP = (3×10⁶)/10 = 300 kHz</li>
</ul>

<h4>TD3: Filtres du 2ème ordre</h4>

<p><strong>Exercice</strong>: Déterminer les valeurs de R et C pour un filtre passe-bas Sallen-Key avec:</p>
<ul>
  <li>f0 = 10 kHz</li>
  <li>Q = 1 (Bessel)</li>
</ul>

<p><strong>Méthode</strong>:</p>
<ol>
  <li>Fixer C (ex: 10 nF)</li>
  <li>Calculer R avec ω0 = 1/(RC)</li>
  <li>Ajuster pour obtenir le Q désiré (ratios de résistances/capacités)</li>
</ol>

<h4>TD4: Transformée de Laplace</h4>

<p><strong>Exercice</strong>: Calculer la réponse temporelle d'un circuit RC à un échelon de tension.</p>

<p><strong>Entrée</strong>: Ve(t) = E × u(t) où u(t) est l'échelon unité</p>

<p>En Laplace: Ve(p) = E/p</p>

<p>Fonction de transfert: H(p) = 1/(1 + RCp)</p>

<p>Vs(p) = H(p) × Ve(p) = E/(p×(1 + RCp)) = E/p - (ERC)/(1 + RCp)</p>

<p>Transformée inverse:<br/>
Vs(t) = E × (1 - exp(-t/(RC))) × u(t)</p>

<p><strong>Constante de temps</strong>: τ = RC</p>

<p>À t = τ: Vs(τ) = 0.63E (63% de la valeur finale)</p>

<h3>Applications Pratiques</h3>

<p><strong>Conditionnement de signaux capteurs</strong>:</p>
<ul>
  <li>Amplification (thermocouples, micros)</li>
  <li>Filtrage anti-repliement avant numérisation (CAN)</li>
  <li>Élimination du bruit 50 Hz (filtre coupe-bande)</li>
</ul>

<p><strong>Audio</strong>:</p>
<ul>
  <li>Égaliseurs (filtres passe-bande multiples)</li>
  <li>Crossovers pour haut-parleurs (filtres passe-bas/passe-haut)</li>
  <li>Effets (filtres résonants)</li>
</ul>

<p><strong>Instrumentation</strong>:</p>
<ul>
  <li>Amplificateurs d'instrumentation (gain précis, CMRR élevé)</li>
  <li>Intégrateurs pour capteurs de courant</li>
  <li>Dérivateurs pour capteurs de vitesse</li>
</ul>

<p><strong>Alimentation</strong>:</p>
<ul>
  <li>Filtrage de l'ondulation résiduelle</li>
  <li>Régulation linéaire avec AO</li>
</ul>

<hr/>

<h2>PART D: ANALYSE ET RÉFLEXION</h2>

<h3>Connaissances et compétences mobilisées</h3>

<ul>
  <li><strong>Analyse fréquentielle</strong>: maîtrise des diagrammes de Bode et de la représentation complexe</li>
  <li><strong>Analyse temporelle</strong>: utilisation de la transformée de Laplace pour les réponses transitoires</li>
  <li><strong>Conception de filtres</strong>: dimensionnement de filtres actifs et passifs</li>
  <li><strong>Simulation</strong>: utilisation de LTspice pour la validation de circuits</li>
  <li><strong>Mesures</strong>: utilisation d'oscilloscopes et analyseurs de spectre</li>
  <li><strong>Mathématiques appliquées</strong>: nombres complexes, équations différentielles, transformées</li>
</ul>

<h3>Auto-évaluation</h3>

<p>Ce cours a été l'un des plus importants de ma formation en électronique analogique.</p>

<p><strong>Points forts</strong>:</p>
<ul>
  <li><strong>Lien théorie/pratique</strong>: les TPs avec LTspice ont permis de valider les calculs théoriques</li>
  <li><strong>Outils mathématiques</strong>: la transformée de Laplace est un outil puissant pour l'analyse</li>
  <li><strong>Polyvalence</strong>: applications dans de nombreux domaines (audio, instrumentation, télécoms)</li>
  <li><strong>Amplificateurs opérationnels</strong>: composant universel permettant une grande variété de fonctions</li>
</ul>

<p><strong>Difficultés rencontrées</strong>:</p>
<ul>
  <li><strong>Mathématiques</strong>: manipulations complexes avec les nombres complexes et Laplace</li>
  <li><strong>Dimensionnement</strong>: choix des composants (compromis performance/coût/disponibilité)</li>
  <li><strong>Filtres d'ordre supérieur</strong>: complexité croissante, difficile à intuiter</li>
</ul>

<p><strong>Applications pratiques</strong>:</p>
<ul>
  <li>Conception de chaînes d'acquisition de données</li>
  <li>Filtrage de signaux pour systèmes embarqués</li>
  <li>Conditionnement de capteurs analogiques</li>
</ul>

<h3>Mon opinion</h3>

<p>Ce cours est fondamental pour tout ingénieur en électronique et systèmes embarqués.</p>

<p><strong>Pourquoi ce cours est essentiel</strong>:</p>

<ol>
  <li><strong>Base de l'électronique analogique</strong>: même à l'ère du numérique, l'interface avec le monde réel reste analogique</li>
  <li><strong>Filtrage indispensable</strong>: anti-repliement avant CAN, élimination du bruit</li>
  <li><strong>Conditionnement de signaux</strong>: amplification, adaptation d'impédance</li>
  <li><strong>Outils réutilisables</strong>: Laplace, Bode utilisés dans d'autres cours (automatique, télécoms)</li>
</ol>

<p><strong>Connexions avec autres cours</strong>:</p>
<ul>
  <li><strong>Filtrage Numérique</strong> (S6): équivalent numérique, transformation bilinéaire</li>
  <li><strong>Traitement du Signal</strong> (S5): complément théorique (FFT, convolution)</li>
  <li><strong>Chaînes d'Acquisition</strong> (S8): application directe pour le conditionnement</li>
  <li><strong>Automatique</strong> (S6-S8): même formalisme (Laplace, fonctions de transfert)</li>
</ul>

<p><strong>Évolution moderne</strong>:</p>

<p>Aujourd'hui, les défis sont:</p>
<ul>
  <li><strong>Mixte analogique-numérique</strong>: filtres à capacités commutées, filtres actifs programmables</li>
  <li><strong>Faible consommation</strong>: importance pour IoT et objets connectés</li>
  <li><strong>Haute fréquence</strong>: défis pour les RF (radio-fréquence)</li>
  <li><strong>Intégration</strong>: ASIC, filtres intégrés dans les puces</li>
</ul>

<p><strong>Outils modernes</strong>:</p>
<ul>
  <li><strong>Filtres numériques</strong>: remplacent souvent les filtres analogiques (flexibilité)</li>
  <li><strong>DSP</strong> (Digital Signal Processor): traitement tout-numérique</li>
  <li>Mais: <strong>filtres analogiques toujours nécessaires</strong> en amont du CAN!</li>
</ul>

<p><strong>Recommandations pour réussir</strong>:</p>

<ol>
  <li><strong>Maîtriser les bases</strong>: nombres complexes, équations différentielles</li>
  <li><strong>Pratiquer régulièrement</strong>: refaire les TDs, varier les paramètres</li>
  <li><strong>Simuler</strong>: LTspice gratuit, expérimenter sans matériel</li>
  <li><strong>Visualiser</strong>: tracer les Bode, observer les réponses temporelles</li>
  <li><strong>Comprendre physiquement</strong>: ne pas se limiter aux formules</li>
</ol>

<p><strong>Applications professionnelles</strong>:</p>

<p>Ces compétences sont utilisées dans:</p>
<ul>
  <li><strong>Conception de cartes électroniques</strong>: conditionnement de signaux</li>
  <li><strong>Instrumentation</strong>: oscilloscopes, multimètres, analyseurs</li>
  <li><strong>Audio professionnel</strong>: consoles de mixage, égaliseurs</li>
  <li><strong>Télécommunications</strong>: filtrage RF, modulation</li>
  <li><strong>Automobile</strong>: capteurs ABS, airbag (critiques)</li>
  <li><strong>Médical</strong>: ECG, EEG (amplification de signaux faibles)</li>
  <li><strong>Aéronautique</strong>: systèmes critiques, certification</li>
</ul>

<p><strong>Aspects pratiques importants</strong>:</p>

<ul>
  <li><strong>Choix de l'AO</strong>: compromis GBP, slew rate, bruit, offset, coût</li>
  <li><strong>Composants réels</strong>: tolérances (±5%, ±10%), dérive en température</li>
  <li><strong>Stabilité</strong>: éviter les oscillations (marge de phase, compensation)</li>
  <li><strong>Layout PCB</strong>: routage critique (masse, découplage, chemins de retour)</li>
</ul>

<p>En conclusion, ce cours fournit des bases solides en électronique analogique qui restent pertinentes malgré la montée du numérique. La compréhension des filtres et de l'analyse fréquentielle/temporelle est indispensable pour concevoir des systèmes électroniques complets et performants.</p>

<hr/>

<h2>Rapports et Projets</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Compte Rendu TP - Circuits et Filtres Analogiques</h4>
      <p>Rapport de travaux pratiques sur les cellules CR/RC et les filtres Sallen-Key : mesures, simulations LTspice et analyse fréquentielle.</p>
      <p style="text-align: center;">
        <a href="/file/reports/S5/Compte_rendu_Chanfreau_Jumin.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Télécharger le rapport PDF
        </a>
      </p>
    </div>
  </div>
</div>

</div>

<!-- ==================== ENGLISH VERSION ==================== -->
<div class="lang-en">

<h1>Analog Circuits and Filters - S5</h1>

<p><strong>Year</strong>: 2022-2023 (Semester 5)<br/>
<strong>Credits</strong>: 3 ECTS<br/>
<strong>Type</strong>: Analog Electronics</p>

<hr/>

<h2>PART A: GENERAL OVERVIEW</h2>

<h3>Course Objectives</h3>

<p>The "Analog Circuits and Filters" course provides an in-depth understanding of the analysis and design of analog electronic circuits, with a particular emphasis on filter theory. It covers the use of operational amplifiers, frequency-domain analysis via Bode diagrams, and time-domain analysis via the Laplace transform. This course is fundamental for the design of signal acquisition chains, sensor conditioning, and analog signal processing.</p>

<h3>Target Skills</h3>

<ul>
  <li>Master frequency-domain analysis of circuits (Bode diagrams, transfer functions)</li>
  <li>Design active and passive filters (low-pass, high-pass, band-pass)</li>
  <li>Use operational amplifiers in various configurations</li>
  <li>Apply the Laplace transform for time-domain analysis</li>
  <li>Size analog circuits for specific applications</li>
  <li>Simulate and validate circuits with LTspice</li>
  <li>Analyze 1st and 2nd order systems</li>
</ul>

<h3>Organization</h3>

<ul>
  <li><strong>Course hours</strong>: 36h (Lectures: 20h, Tutorials: 8h, Labs: 8h)</li>
  <li><strong>Assessment</strong>: Written exam (60%) + Tutorials/Labs (30%) + Continuous assessment (10%)</li>
  <li><strong>Semester</strong>: 5 (2022-2023)</li>
  <li><strong>Prerequisites</strong>: Fundamental electronics, mathematics (complex numbers, derivatives, integrals)</li>
</ul>

<hr/>

<h2>PART B: EXPERIENCE, CONTEXT AND FUNCTION</h2>

<h3>Course Content</h3>

<p>The course is structured around three main parts covering the theoretical and practical aspects of analog electronics.</p>

<h4>1. Operational Amplifiers and Basic Circuits</h4>

<p><strong>Ideal Operational Amplifier</strong>:</p>

<p>The operational amplifier (op-amp) is the fundamental component of modern analog electronics.</p>

<p><strong>Characteristics of the ideal op-amp</strong>:</p>
<ul>
  <li>Infinite differential voltage gain: Ad = ∞</li>
  <li>Infinite input impedance: Zin = ∞ (zero input currents)</li>
  <li>Zero output impedance: Zout = 0</li>
  <li>Infinite bandwidth</li>
  <li>Zero offset voltage</li>
  <li>Infinite common-mode rejection ratio (CMRR = ∞)</li>
</ul>

<p><strong>Rules of the ideal op-amp in linear mode</strong> (negative feedback):</p>
<ol>
  <li>V+ = V- (input voltage equality)</li>
  <li>I+ = I- = 0 (zero input currents)</li>
</ol>

<p><strong>Fundamental circuits</strong>:</p>

<p><strong>Inverting amplifier</strong>:</p>
<div style="text-align: center; display: flex; justify-content: center; gap: 20px;">
  <img src="/img/Courses/S5/Circuits-Filtres-Analogiques/inverseur.png" style="width: 45%;"/>
  <img src="/img/Courses/S5/Circuits-Filtres-Analogiques/inverseur2.png" style="width: 45%;"/>
</div>
<br>

<p><strong>Non-inverting amplifier</strong>:</p>
<pre><code>         R2
     ----/\/\/----
     |           |
     +-[AO+]-----+---- Vs
     |  |  -|
Ve --+  |   |
        R1  |
         \  |
          \ |
           GND
</code></pre>

<p>Transfer function:<br/>
H = Vs/Ve = 1 + (R2/R1)</p>

<p>Input impedance: Zin = ∞ (very high)</p>

<p><strong>Voltage follower (buffer)</strong>:<br/>
Non-inverting configuration with R2 = 0 and R1 = ∞</p>

<p>H = 1</p>

<p>Used for impedance matching (isolation).</p>

<p><strong>Inverting summing amplifier</strong>:</p>
<pre><code>Ve1 -R1-\
Ve2 -R2--+-[AO-]---- Vs
Ve3 -R3-/  |   +|
           R4  |--- GND
</code></pre>

<p>Vs = -R4 × (Ve1/R1 + Ve2/R2 + Ve3/R3)</p>

<p>If R1 = R2 = R3 = R4 = R:<br/>
Vs = -(Ve1 + Ve2 + Ve3)</p>

<p><strong>Subtractor (differential amplifier)</strong>:</p>
<pre><code>Ve1 -R1--[AO-]---R2--- Vs
         |  +|
Ve2 -R3--+   |
         R4  |
          \  |
           GND
</code></pre>

<p>If R1 = R2 and R3 = R4:<br/>
Vs = (R2/R1) × (Ve2 - Ve1)</p>

<p><strong>Integrator</strong>:</p>
<pre><code>        C
    ----||----
    |        |
Ve -R1-[AO-]-+---- Vs
       |   +|
       |    |--- GND
</code></pre>

<p>Vs(t) = -(1/(R×C)) × ∫Ve(t)dt + Vs(0)</p>

<p>In the frequency domain:<br/>
H(jω) = -1/(jRCω)</p>

<p><strong>Differentiator</strong>:</p>
<pre><code>        R2
    ----/\/\/----
    |           |
Ve -C1-[AO-]----+---- Vs
       |   +|
       |    |--- GND
</code></pre>

<p>Vs(t) = -RC × dVe(t)/dt</p>

<p>In the frequency domain:<br/>
H(jω) = -jRCω</p>

<p><strong>Course materials</strong>:</p>
<ul>
  <li><a href="/cours-pdf/S5/Circuits-Filtres-Analogiques/Montages_AOs.pdf">Op-amp based circuits</a></li>
</ul>

<h4>2. Transfer Functions and Frequency-Domain Analysis</h4>

<p><strong>Transfer function</strong>:</p>

<p>The transfer function H(jω) of a linear system relates the output to the input in harmonic (sinusoidal steady-state) mode:</p>

<p>H(jω) = Vs(jω)/Ve(jω)</p>

<p>where j = √(-1) and ω = 2πf (angular frequency in rad/s)</p>

<p><strong>Magnitude and phase</strong>:<br/>
H(jω) = |H(jω)| × exp(jφ(ω))</p>

<ul>
  <li><strong>Magnitude</strong> (gain): |H(jω)|, often expressed in decibels (dB)<br/>
  GdB = 20 × log10(|H(jω)|)</li>
  <li><strong>Phase</strong>: φ(ω) = arg(H(jω)), expressed in degrees or radians</li>
</ul>

<p><strong>Bode diagram</strong>:</p>

<p>Graphical representation of the transfer function:</p>
<ul>
  <li><strong>Gain plot</strong>: GdB as a function of log(f)</li>
  <li><strong>Phase plot</strong>: φ as a function of log(f)</li>
</ul>

<p><strong>1st order filters</strong>:</p>

<p><strong>Passive RC low-pass filter</strong>:</p>
<pre><code>Ve ---R---+--- Vs
          |
          C
          |
         GND
</code></pre>

<p>Transfer function:<br/>
H(jω) = 1/(1 + jRCω) = 1/(1 + j(ω/ω0))</p>

<p>where ω0 = 1/(RC) is the cutoff angular frequency.</p>

<p>Cutoff frequency at -3dB:<br/>
f0 = 1/(2πRC)</p>

<p><strong>Asymptotic behavior</strong>:</p>
<ul>
  <li>Low frequencies (ω &lt;&lt; ω0): H ≈ 1 → 0 dB</li>
  <li>High frequencies (ω &gt;&gt; ω0): H ≈ ω0/ω → slope of -20 dB/decade</li>
</ul>

<p><strong>Phase</strong>:<br/>
φ(ω) = -arctan(ω/ω0)</p>

<p>At the cutoff frequency: φ(ω0) = -45°</p>

<p><strong>Passive CR high-pass filter</strong>:</p>
<pre><code>Ve ---C---+--- Vs
          |
          R
          |
         GND
</code></pre>

<p>Transfer function:<br/>
H(jω) = (jRCω)/(1 + jRCω) = j(ω/ω0)/(1 + j(ω/ω0))</p>

<p><strong>2nd order filters</strong>:</p>

<p>Canonical form:<br/>
H(p) = (H0 × ω0²)/(p² + (ω0/Q)×p + ω0²)</p>

<p>where:</p>
<ul>
  <li>p = jω (Laplace variable in harmonic mode)</li>
  <li>ω0: natural angular frequency (or resonance frequency)</li>
  <li>Q: quality factor</li>
  <li>H0: static gain</li>
</ul>

<p><strong>Quality factor Q</strong> (or damping coefficient ξ = 1/(2Q)):</p>
<ul>
  <li>Q &lt; 0.5 (ξ &gt; 1): overdamped system (no overshoot)</li>
  <li>Q = 0.5 (ξ = 1): critical damping</li>
  <li>Q = 0.707 (ξ = 0.707): Butterworth response (maximally flat)</li>
  <li>Q &gt; 0.707: underdamped system (overshoot, resonance)</li>
</ul>

<p><strong>2nd order low-pass filter (Sallen-Key)</strong>:</p>
<pre><code>Ve -R1--+--R2--+-----[AO+]---- Vs
        |      |      |  -|
        C1     C2     +---+
        |      |          |
       GND    GND        R3
                          |
                         R4
                          |
                         GND
</code></pre>

<p>For a Butterworth filter (Q = 0.707), unity-gain configuration:</p>

<p>H(jω) = 1/(1 + √2 × j(ω/ω0) - (ω/ω0)²)</p>

<p><strong>Cutoff slope</strong>: -40 dB/decade (2 × 20 dB/decade)</p>

<p><strong>Two-port networks (Quadripoles)</strong>:</p>

<p>A two-port network is a system with 2 ports (input and output) characterized by transfer matrices.</p>

<p><strong>Impedance matrix [Z]</strong>:</p>
<pre><code>[V1]   [Z11  Z12] [I1]
[V2] = [Z21  Z22] [I2]
</code></pre>

<p><strong>Admittance matrix [Y] = [Z]⁻¹</strong></p>

<p><strong>Transmission matrix (ABCD)</strong>:</p>
<pre><code>[V1]   [A  B] [V2 ]
[I1] = [C  D] [-I2]
</code></pre>

<p>Advantage: for cascaded two-port networks, the ABCD matrices are multiplied together.</p>

<p><strong>Course materials</strong>:</p>
<ul>
  <li><a href="/cours-pdf/S5/Circuits-Filtres-Analogiques/TransfertBode.pdf">Transfer Function and Bode</a></li>
  <li><a href="/cours-pdf/S5/Circuits-Filtres-Analogiques/Ordre-deux-frequentiel.pdf">2nd Order Frequency Response</a></li>
  <li><a href="/cours-pdf/S5/Circuits-Filtres-Analogiques/Quadripole.pdf">Two-port Networks and Transfer Functions</a></li>
</ul>

<h4>3. Laplace Transform and Time-Domain Analysis</h4>

<p><strong>Laplace Transform</strong>:</p>

<p>A mathematical tool for transforming differential equations into algebraic equations.</p>

<p>L{f(t)} = F(p) = ∫[0 to ∞] f(t) × exp(-pt) dt</p>

<p>where p = σ + jω is the complex Laplace variable.</p>

<p><strong>Common transforms</strong>:</p>

<table>
  <thead>
    <tr><th>Time-domain signal f(t)</th><th>Transform F(p)</th></tr>
  </thead>
  <tbody>
    <tr><td>Step u(t)</td><td>1/p</td></tr>
    <tr><td>Impulse δ(t)</td><td>1</td></tr>
    <tr><td>Ramp t×u(t)</td><td>1/p²</td></tr>
    <tr><td>Exponential exp(-at)×u(t)</td><td>1/(p+a)</td></tr>
    <tr><td>Sine sin(ωt)×u(t)</td><td>ω/(p² + ω²)</td></tr>
    <tr><td>Cosine cos(ωt)×u(t)</td><td>p/(p² + ω²)</td></tr>
  </tbody>
</table>

<p><strong>Properties of the transform</strong>:</p>

<ul>
  <li><strong>Linearity</strong>: L{a×f(t) + b×g(t)} = a×F(p) + b×G(p)</li>
  <li><strong>Differentiation</strong>: L{df/dt} = p×F(p) - f(0⁻)</li>
  <li><strong>Integration</strong>: L{∫[0 to t] f(τ)dτ} = F(p)/p</li>
  <li><strong>Time delay theorem</strong>: L{f(t-τ)×u(t-τ)} = exp(-pτ)×F(p)</li>
  <li><strong>Initial value theorem</strong>: f(0⁺) = lim[p→∞] p×F(p)</li>
  <li><strong>Final value theorem</strong>: f(∞) = lim[p→0] p×F(p)</li>
</ul>

<p><strong>Application to circuits</strong>:</p>

<p>In the Laplace domain, circuit elements become:</p>
<ul>
  <li><strong>Resistor</strong>: R (unchanged)</li>
  <li><strong>Capacitor</strong>: impedance 1/(pC)</li>
  <li><strong>Inductor</strong>: impedance pL</li>
</ul>

<p><strong>Example - RC Circuit</strong>:</p>

<p>Time-domain equation:<br/>
RC × dVs/dt + Vs = Ve</p>

<p>In Laplace domain (zero initial conditions):<br/>
RC × p×Vs(p) + Vs(p) = Ve(p)</p>

<p>Transfer function:<br/>
H(p) = Vs(p)/Ve(p) = 1/(1 + RCp)</p>

<p><strong>Time-domain response of a 2nd order system</strong>:</p>

<p>For a 2nd order system:<br/>
H(p) = ω0²/(p² + 2ξω0×p + ω0²)</p>

<p><strong>Step response</strong> (step input):</p>

<ul>
  <li><strong>Overdamped case</strong> (ξ &gt; 1): two distinct real poles, no overshoot</li>
  <li><strong>Critically damped case</strong> (ξ = 1): double real pole, fastest response without overshoot</li>
  <li><strong>Underdamped case</strong> (0 &lt; ξ &lt; 1): complex conjugate poles, damped oscillations</li>
</ul>

<p>Vs(t) = V0 × [1 - (exp(-ξω0×t)/√(1-ξ²)) × sin(ωd×t + φ)]</p>

<p>where ωd = ω0×√(1-ξ²) (pseudo-frequency)</p>

<p><strong>Overshoot</strong>:<br/>
D% = 100 × exp(-πξ/√(1-ξ²))</p>

<p>For Q = 0.707 (ξ = 0.707): D ≈ 4.3%</p>

<p><strong>Rise time</strong> tm (10% to 90%):<br/>
tm ≈ 2.2/ω0</p>

<p><strong>Settling time</strong> tr (to 5%):<br/>
tr ≈ 3/(ξω0)</p>

<p><strong>RLC Circuits</strong>:</p>

<p><strong>Series RLC Circuit</strong>:</p>

<p>Differential equation:<br/>
L × d²i/dt² + R × di/dt + (1/C)×i = dVe/dt</p>

<p>In Laplace domain:<br/>
H(p) = I(p)/Ve(p) = pC/(LCp² + RCp + 1)</p>

<p><strong>Natural angular frequency</strong>: ω0 = 1/√(LC)</p>

<p><strong>Quality factor</strong>: Q = (1/R)×√(L/C) = (ω0×L)/R</p>

<p><strong>Signal analysis</strong>:</p>

<ul>
  <li><strong>Harmonic transfer function</strong>: response in sinusoidal steady-state mode</li>
  <li><strong>Impulse response</strong>: h(t) = L⁻¹{H(p)}</li>
  <li><strong>Step response</strong>: s(t) = L⁻¹{H(p)/p}</li>
  <li><strong>Convolution</strong>: y(t) = h(t) * x(t) = ∫[-∞ to ∞] h(τ)×x(t-τ) dτ</li>
</ul>

<p><strong>Course materials</strong>:</p>
<ul>
  <li><a href="/cours-pdf/S5/Circuits-Filtres-Analogiques/Laplace.pdf">Laplace Transform</a></li>
  <li><a href="/cours-pdf/S5/Circuits-Filtres-Analogiques/Ordre-deux-temporel.pdf">2nd Order Time Response</a></li>
  <li><a href="/cours-pdf/S5/Circuits-Filtres-Analogiques/Laplace-RLC.pdf">Laplace and RLC Circuits</a></li>
  <li><a href="/cours-pdf/S5/Circuits-Filtres-Analogiques/Laplace-Signaux.pdf">Laplace and Signals</a></li>
</ul>

<hr/>

<h2>PART C: TECHNICAL ASPECTS</h2>

<p>This section presents the lab work and exercises completed.</p>

<h3>Lab Work with LTspice</h3>

<h4>Lab 1: CR and RC Cells</h4>

<p><strong>Objective</strong>: Study of 1st order passive filters and validation through simulation.</p>

<p><strong>RC Cell (Low-Pass)</strong>:</p>

<p>Circuit simulated in LTspice:</p>
<pre><code>RC low-pass circuit:
V1 (AC source) --- R1 (1kΩ) ---+--- Vout
                                |
                               C1 (100nF)
                                |
                               GND
</code></pre>

<p><strong>Theoretical calculation</strong>:<br/>
f0 = 1/(2π×RC) = 1/(2π × 1000 × 100×10⁻⁹) = 1.59 kHz</p>

<p><strong>Simulation</strong>:</p>
<ul>
  <li>AC analysis from 10 Hz to 100 kHz</li>
  <li>Bode diagram plot (gain and phase)</li>
  <li>Verification of the -3 dB cutoff frequency</li>
  <li>Slope of -20 dB/decade above f0</li>
</ul>

<p><strong>CR Cell (High-Pass)</strong>:</p>

<pre><code>CR high-pass circuit:
V1 (AC source) --- C1 (100nF) ---+--- Vout
                                 |
                                R1 (1kΩ)
                                 |
                                GND
</code></pre>

<p>Same cutoff frequency: f0 = 1.59 kHz</p>

<p><strong>Behavior</strong>:</p>
<ul>
  <li>Attenuation of low frequencies</li>
  <li>Unity gain (0 dB) at high frequencies</li>
  <li>Slope of +20 dB/decade below f0</li>
  <li>Phase shift from 0° to +90°</li>
</ul>

<p><strong>Measurements performed</strong>:</p>
<ul>
  <li>Gain at various frequencies (data table)</li>
  <li>Phase at various frequencies</li>
  <li>Comparison of measurements vs. theory</li>
  <li>Impact of real components (tolerances)</li>
</ul>

<p><strong>Course materials</strong>:<br/>
<a href="/cours-pdf/S5/Circuits-Filtres-Analogiques/Compte_rendu_Chanfreau_Jumin.pdf">Lab report</a></p>

<h4>Lab 1: Sallen-Key Filter</h4>

<p><strong>Objective</strong>: Implementation of a 2nd order active low-pass filter.</p>

<p><strong>Unity-gain Sallen-Key topology</strong>:</p>

<pre><code>Sallen-Key circuit (unity gain):
           R1        R2
Ve ----/\/\/\--+-/\/\/\--+-----[AO+]---- Vs
               |         |      |  -|
               C1       C2      +---+
               |         |
              GND       GND
</code></pre>

<p><strong>Butterworth design</strong>:</p>

<p>For f0 = 1 kHz and Q = 0.707:</p>

<p>Choice: C1 = C2 = C = 100 nF</p>

<p>R = 1/(2π×f0×C) = 1/(2π × 1000 × 100×10⁻⁹) = 1.59 kΩ</p>

<p>We choose R1 = R2 = 1.6 kΩ (E24 standard value)</p>

<p><strong>LTspice Simulation</strong>:</p>
<ul>
  <li>AC analysis: Bode diagram</li>
  <li>Verification of f0, Q, and -40 dB/decade slope</li>
  <li>Time-domain analysis (step response): overshoot measurement (~4.3% expected)</li>
  <li>Transient analysis with square wave: response observation</li>
</ul>

<p><strong>1st order vs 2nd order comparison</strong>:</p>
<ul>
  <li>Superior selectivity of the 2nd order</li>
  <li>Doubled cutoff slope</li>
  <li>Possibility of resonance if Q &gt; 0.707</li>
</ul>

<h3>Tutorial Exercises</h3>

<h4>Tutorial 1: Passive filter analysis</h4>

<p><strong>Typical exercise</strong>: Determine the transfer function of a series then parallel RC filter.</p>

<p><strong>Complex impedance calculation</strong>:</p>

<p>For a capacitor: Zc = 1/(jCω)</p>

<p>Voltage divider:<br/>
H(jω) = Z2/(Z1 + Z2)</p>

<p><strong>Numerical application</strong>: calculate gain and phase for several frequencies.</p>

<h4>Tutorial 2: Operational amplifiers</h4>

<p><strong>Exercise</strong>: Design a non-inverting amplifier with a gain of 10.</p>

<p>H = 1 + (R2/R1) = 10</p>

<p>Therefore: R2/R1 = 9</p>

<p>Choice: R1 = 10 kΩ, R2 = 90 kΩ</p>

<p><strong>Bandwidth verification</strong>:</p>

<p>For a real op-amp (e.g., TL081):</p>
<ul>
  <li>GBP (Gain-Bandwidth Product) = 3 MHz</li>
  <li>Bandwidth at gain 10: fBP = (3×10⁶)/10 = 300 kHz</li>
</ul>

<h4>Tutorial 3: 2nd order filters</h4>

<p><strong>Exercise</strong>: Determine the R and C values for a Sallen-Key low-pass filter with:</p>
<ul>
  <li>f0 = 10 kHz</li>
  <li>Q = 1 (Bessel)</li>
</ul>

<p><strong>Method</strong>:</p>
<ol>
  <li>Fix C (e.g., 10 nF)</li>
  <li>Calculate R using ω0 = 1/(RC)</li>
  <li>Adjust to achieve the desired Q (resistance/capacitance ratios)</li>
</ol>

<h4>Tutorial 4: Laplace Transform</h4>

<p><strong>Exercise</strong>: Calculate the time-domain response of an RC circuit to a voltage step.</p>

<p><strong>Input</strong>: Ve(t) = E × u(t) where u(t) is the unit step</p>

<p>In Laplace domain: Ve(p) = E/p</p>

<p>Transfer function: H(p) = 1/(1 + RCp)</p>

<p>Vs(p) = H(p) × Ve(p) = E/(p×(1 + RCp)) = E/p - (ERC)/(1 + RCp)</p>

<p>Inverse transform:<br/>
Vs(t) = E × (1 - exp(-t/(RC))) × u(t)</p>

<p><strong>Time constant</strong>: τ = RC</p>

<p>At t = τ: Vs(τ) = 0.63E (63% of the final value)</p>

<h3>Practical Applications</h3>

<p><strong>Sensor signal conditioning</strong>:</p>
<ul>
  <li>Amplification (thermocouples, microphones)</li>
  <li>Anti-aliasing filtering before digitization (ADC)</li>
  <li>50 Hz noise elimination (notch filter)</li>
</ul>

<p><strong>Audio</strong>:</p>
<ul>
  <li>Equalizers (multiple band-pass filters)</li>
  <li>Crossovers for loudspeakers (low-pass/high-pass filters)</li>
  <li>Effects (resonant filters)</li>
</ul>

<p><strong>Instrumentation</strong>:</p>
<ul>
  <li>Instrumentation amplifiers (precise gain, high CMRR)</li>
  <li>Integrators for current sensors</li>
  <li>Differentiators for velocity sensors</li>
</ul>

<p><strong>Power supply</strong>:</p>
<ul>
  <li>Residual ripple filtering</li>
  <li>Linear regulation with op-amp</li>
</ul>

<hr/>

<h2>PART D: ANALYSIS AND REFLECTION</h2>

<h3>Knowledge and Skills Applied</h3>

<ul>
  <li><strong>Frequency-domain analysis</strong>: mastery of Bode diagrams and complex representation</li>
  <li><strong>Time-domain analysis</strong>: use of the Laplace transform for transient responses</li>
  <li><strong>Filter design</strong>: sizing of active and passive filters</li>
  <li><strong>Simulation</strong>: use of LTspice for circuit validation</li>
  <li><strong>Measurements</strong>: use of oscilloscopes and spectrum analyzers</li>
  <li><strong>Applied mathematics</strong>: complex numbers, differential equations, transforms</li>
</ul>

<h3>Self-Assessment</h3>

<p>This course was one of the most important in my analog electronics training.</p>

<p><strong>Strengths</strong>:</p>
<ul>
  <li><strong>Theory/practice connection</strong>: the labs with LTspice allowed validation of theoretical calculations</li>
  <li><strong>Mathematical tools</strong>: the Laplace transform is a powerful analysis tool</li>
  <li><strong>Versatility</strong>: applications in many fields (audio, instrumentation, telecommunications)</li>
  <li><strong>Operational amplifiers</strong>: a universal component enabling a wide variety of functions</li>
</ul>

<p><strong>Challenges encountered</strong>:</p>
<ul>
  <li><strong>Mathematics</strong>: complex manipulations with complex numbers and Laplace</li>
  <li><strong>Component sizing</strong>: component selection (performance/cost/availability trade-offs)</li>
  <li><strong>Higher-order filters</strong>: increasing complexity, difficult to intuit</li>
</ul>

<p><strong>Practical applications</strong>:</p>
<ul>
  <li>Design of data acquisition chains</li>
  <li>Signal filtering for embedded systems</li>
  <li>Analog sensor conditioning</li>
</ul>

<h3>My Opinion</h3>

<p>This course is fundamental for any engineer in electronics and embedded systems.</p>

<p><strong>Why this course is essential</strong>:</p>

<ol>
  <li><strong>Foundation of analog electronics</strong>: even in the digital era, the interface with the real world remains analog</li>
  <li><strong>Essential filtering</strong>: anti-aliasing before ADC, noise elimination</li>
  <li><strong>Signal conditioning</strong>: amplification, impedance matching</li>
  <li><strong>Reusable tools</strong>: Laplace, Bode used in other courses (control theory, telecommunications)</li>
</ol>

<p><strong>Connections with other courses</strong>:</p>
<ul>
  <li><strong>Digital Filtering</strong> (S6): digital equivalent, bilinear transformation</li>
  <li><strong>Signal Processing</strong> (S5): theoretical complement (FFT, convolution)</li>
  <li><strong>Acquisition Chains</strong> (S8): direct application for conditioning</li>
  <li><strong>Control Theory</strong> (S6-S8): same formalism (Laplace, transfer functions)</li>
</ul>

<p><strong>Modern evolution</strong>:</p>

<p>Today's challenges include:</p>
<ul>
  <li><strong>Mixed analog-digital</strong>: switched-capacitor filters, programmable active filters</li>
  <li><strong>Low power consumption</strong>: important for IoT and connected objects</li>
  <li><strong>High frequency</strong>: challenges for RF (radio frequency)</li>
  <li><strong>Integration</strong>: ASICs, filters integrated into chips</li>
</ul>

<p><strong>Modern tools</strong>:</p>
<ul>
  <li><strong>Digital filters</strong>: often replace analog filters (flexibility)</li>
  <li><strong>DSP</strong> (Digital Signal Processor): all-digital processing</li>
  <li>However: <strong>analog filters are still necessary</strong> upstream of the ADC!</li>
</ul>

<p><strong>Recommendations for success</strong>:</p>

<ol>
  <li><strong>Master the fundamentals</strong>: complex numbers, differential equations</li>
  <li><strong>Practice regularly</strong>: redo tutorials, vary parameters</li>
  <li><strong>Simulate</strong>: LTspice is free, experiment without hardware</li>
  <li><strong>Visualize</strong>: plot Bode diagrams, observe time-domain responses</li>
  <li><strong>Understand physically</strong>: don't limit yourself to formulas</li>
</ol>

<p><strong>Professional applications</strong>:</p>

<p>These skills are used in:</p>
<ul>
  <li><strong>Electronic board design</strong>: signal conditioning</li>
  <li><strong>Instrumentation</strong>: oscilloscopes, multimeters, analyzers</li>
  <li><strong>Professional audio</strong>: mixing consoles, equalizers</li>
  <li><strong>Telecommunications</strong>: RF filtering, modulation</li>
  <li><strong>Automotive</strong>: ABS sensors, airbags (safety-critical)</li>
  <li><strong>Medical</strong>: ECG, EEG (weak signal amplification)</li>
  <li><strong>Aerospace</strong>: safety-critical systems, certification</li>
</ul>

<p><strong>Important practical aspects</strong>:</p>

<ul>
  <li><strong>Op-amp selection</strong>: trade-offs between GBP, slew rate, noise, offset, cost</li>
  <li><strong>Real components</strong>: tolerances (±5%, ±10%), temperature drift</li>
  <li><strong>Stability</strong>: avoiding oscillations (phase margin, compensation)</li>
  <li><strong>PCB layout</strong>: critical routing (ground, decoupling, return paths)</li>
</ul>

<p>In conclusion, this course provides a solid foundation in analog electronics that remains relevant despite the rise of digital technology. Understanding filters and frequency/time-domain analysis is essential for designing complete and high-performance electronic systems.</p>

<hr/>

<h2>Reports and Projects</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Lab Report - Analog Circuits and Filters</h4>
      <p>Lab report on CR/RC cells and Sallen-Key filters: measurements, LTspice simulations, and frequency-domain analysis.</p>
      <p style="text-align: center;">
        <a href="/file/reports/S5/Compte_rendu_Chanfreau_Jumin.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Download the PDF report
        </a>
      </p>
    </div>
  </div>
</div>

</div>

<div class="back-nav">
  <a href="./my-courses-2022-2023.html" data-i18n-html="back-courses-2022-2023">← Retour aux Cours 2022-2023</a>
</div>

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

<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f9;
        color: #333;
        line-height: 1.6;
    }
    h2, h3, h4 {
        color: #2a7ae2;
    }
    p {
        text-align: justify;
    }
    code {
        background-color: #f5f5f5;
        padding: 2px 6px;
        border-radius: 3px;
        font-family: 'Courier New', monospace;
    }
    pre {
        background-color: #f5f5f5;
        padding: 15px;
        border-radius: 5px;
        overflow-x: auto;
    }
</style>

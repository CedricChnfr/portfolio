---
layout: default
title: "Filtrage Numérique - S6"
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
    <a href="./my-courses-2022-2023.html" data-i18n-html="back-courses-2022-2023">← Retour aux Cours 2022-2023</a>
</div>

<!-- ==================== FRENCH VERSION ==================== -->
<div class="lang-fr">

<h1>Filtrage Numerique - Semestre 6</h1>

<p><strong>Annee Universitaire</strong> : 2022-2023<br/>
<strong>Semestre</strong> : 6<br/>
<strong>Credits</strong> : 2,5 ECTS<br/>
<strong>Specialite</strong> : Traitement du Signal et Automatique</p>

<hr/>

<h2>PART A - Presentation Generale du Cours</h2>

<h3 class="section-title">Vue d'ensemble</h3>

<p>Ce cours approfondit le traitement numerique du signal avec un focus sur la conception et l'implementation de filtres numeriques. Il couvre les deux grandes familles de filtres : FIR (Finite Impulse Response) et IIR (Infinite Impulse Response), avec leurs methodes de conception respectives. Le cours combine theorie mathematique (transformee en Z, reponse frequentielle) et pratique (MATLAB, implementation).</p>

<p><strong>Objectifs pedagogiques</strong> :</p>
<ul>
<li>Maitriser la transformee en Z et l'analyse dans le domaine frequentiel</li>
<li>Concevoir des filtres FIR par methode des fenetres</li>
<li>Concevoir des filtres IIR par transformation bilineaire et invariance impulsionnelle</li>
<li>Analyser la stabilite et les performances des filtres numeriques</li>
<li>Implementer et tester des filtres en MATLAB</li>
</ul>

<h3 class="section-title">Position dans le cursus</h3>

<p>Ce cours s'appuie sur et complete :</p>
<ul>
<li><strong>Signal (S5)</strong> : transformee de Fourier, transformee de Laplace, echantillonnage</li>
<li><strong>Modelisation Systemes Lineaires (S5)</strong> : fonctions de transfert, stabilite</li>
</ul>

<p>Il prepare aux applications :</p>
<ul>
<li><strong>Traitement du Signal Avance</strong> : applications audio, biomedicales, communications</li>
<li><strong>Embedded IA for IoT (S9)</strong> : pretraitement de signaux pour machine learning</li>
<li><strong>Projets de traitement de donnees</strong> : analyse spectrale, filtrage adaptatif</li>
</ul>

<hr/>

<h2>PART B - Experience Personnelle et Contexte d'Apprentissage</h2>

<h3 class="section-title">Organisation et ressources</h3>

<p>Le module etait structure autour de trois axes :</p>

<p><strong>1. Cours magistraux</strong> :</p>
<ul>
<li>Rappels sur l'echantillonnage et la transformee en Z</li>
<li>Filtres FIR : proprietes, methodes de conception</li>
<li>Filtres IIR : transformation de filtres analogiques</li>
<li>Structures d'implementation et effets de quantification</li>
</ul>

<p><strong>2. Travaux diriges</strong> :</p>
<ul>
<li>Exercices de conception de filtres FIR par fenetrage</li>
<li>Transformation bilineaire pour filtres IIR</li>
<li>Analyse de stabilite (placement poles et zeros)</li>
<li>Calculs de reponses frequentielles</li>
</ul>

<p><strong>3. Travaux pratiques MATLAB</strong> :</p>
<ul>
<li>Utilisation de l'outil fdatool (Filter Design and Analysis Tool)</li>
<li>Conception et test de filtres FIR et IIR</li>
<li>Comparaison de performances (ordre, attenuation, phase)</li>
<li>Application a des signaux reels (audio, ECG)</li>
</ul>

<p><strong>Ressources pedagogiques</strong> :</p>
<ul>
<li>Playlist YouTube avec cours et TD : <a href="https://www.youtube.com/playlist?list=PL_wkaC4iMBTlJQpi7W18pkzR_kY9d-jsU">Traitement du Signal</a></li>
<li>Annales d'examens 2022 et 2023 avec corrections</li>
<li>Documentation MATLAB Signal Processing Toolbox</li>
</ul>

<h3 class="section-title">Deroulement et methodologie</h3>

<p><strong>Approche progressive</strong> :</p>

<p>Le cours adoptait une approche en trois etapes :</p>

<ol>
<li><strong>Theorie</strong> : etablir les fondements mathematiques (transformee en Z, equations aux differences)</li>
<li><strong>Methodes</strong> : appliquer des techniques systematiques de conception</li>
<li><strong>Pratique</strong> : valider et optimiser avec MATLAB</li>
</ol>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S6/filtrage-numerique/filtrage.svg" alt="Filtrage numerique" style="max-width: 550px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Principe du filtrage numerique - Reduction du bruit par filtrage</p>
</div>

<p><strong>Exemple de conception de filtre passe-bas FIR</strong> :</p>

<p>Cahier des charges :</p>
<ul>
<li>Frequence de coupure : 1 kHz</li>
<li>Frequence d'echantillonnage : 8 kHz</li>
<li>Attenuation bande coupee : &gt; 40 dB</li>
<li>Ondulation bande passante : &lt; 0,5 dB</li>
</ul>

<p>Demarche :</p>
<ol>
<li>Choix de la methode (fenetre de Hamming pour compromis)</li>
<li>Calcul de l'ordre necessaire (fonction du gabarit)</li>
<li>Generation des coefficients avec MATLAB : fir1(N, Wn, 'low')</li>
<li>Verification de la reponse frequentielle : freqz(b, a)</li>
<li>Test sur signal reel</li>
</ol>

<h3 class="section-title">Examens et evaluations</h3>

<p><strong>Format des examens</strong> :</p>

<p>Les annales montrent une structure recurrente :</p>

<p><strong>Exercice 1 : Filtres FIR</strong> (30-40%)</p>
<ul>
<li>Conception par fenetrage</li>
<li>Calcul de l'ordre minimal</li>
<li>Comparaison de differentes fenetres</li>
<li>Analyse de la reponse en frequence</li>
</ul>

<p><strong>Exercice 2 : Filtres IIR</strong> (30-40%)</p>
<ul>
<li>Transformation bilineaire ou invariance impulsionnelle</li>
<li>Calcul de la fonction de transfert en Z</li>
<li>Placement des poles et zeros</li>
<li>Verification de la stabilite</li>
</ul>

<p><strong>Exercice 3 : Implementation</strong> (20-30%)</p>
<ul>
<li>Structure directe ou en cascade</li>
<li>Effets de quantification</li>
<li>Optimisation du nombre de bits</li>
<li>Equations aux differences</li>
</ul>

<p><strong>Difficultes courantes</strong> :</p>
<ul>
<li>Confusion entre frequence normalisee (0 a 1) et frequence physique (Hz)</li>
<li>Erreurs dans la transformation bilineaire (pre-deformation)</li>
<li>Oubli de verifier la stabilite (poles a l'interieur du cercle unite)</li>
<li>Mauvaise interpretation des specifications (dB vs lineaire)</li>
</ul>

<h3 class="section-title">Outils MATLAB utilises</h3>

<p><strong>Fonctions principales</strong> :</p>

<pre><code class="language-matlab">% Conception FIR
b = fir1(N, Wn, 'type');              % Fenetre
b = firpm(N, F, A);                    % Parks-McClellan (optimal)

% Conception IIR
[b,a] = butter(N, Wn, 'type');         % Butterworth
[b,a] = cheby1(N, Rp, Wn, 'type');     % Chebyshev Type I
[b,a] = cheby2(N, Rs, Wn, 'type');     % Chebyshev Type II
[b,a] = ellip(N, Rp, Rs, Wn, 'type');  % Elliptique

% Analyse
freqz(b, a, N);                        % Reponse frequentielle
zplane(b, a);                          % Diagramme poles-zeros
grpdelay(b, a);                        % Delai de groupe
filter(b, a, x);                       % Filtrage
</code></pre>

<hr/>

<h2>PART C - Aspects Techniques Detailles</h2>

<h3 class="section-title">1. Fondements : Transformee en Z</h3>

<p>La transformee en Z est l'equivalent discret de la transformee de Laplace.</p>

<p><strong>Definition</strong> :<br/>
Pour un signal discret x[n], la transformee en Z est :</p>

<p>X(z) = somme de x[n] x z^(-n) pour n de -infini a +infini</p>

<p><strong>Proprietes importantes</strong> :</p>
<ul>
<li>Linearite : Z{a x x[n] + b x y[n]} = a x X(z) + b x Y(z)</li>
<li>Decalage temporel : Z{x[n-k]} = z^(-k) x X(z)</li>
<li>Convolution : Z{x[n] * h[n]} = X(z) x H(z)</li>
</ul>

<p><strong>Region de convergence (ROC)</strong> :<br/>
Zone du plan complexe ou la transformee converge. Critique pour la stabilite.</p>

<p><strong>Lien avec la transformee de Fourier</strong> :<br/>
Sur le cercle unite (z = e^(jw)), la transformee en Z devient la DTFT (Discrete-Time Fourier Transform).</p>

<h3 class="section-title">2. Filtres FIR (Finite Impulse Response)</h3>

<p><strong>Caracteristiques</strong> :</p>

<p>Un filtre FIR a une reponse impulsionnelle de duree finie :</p>

<p>y[n] = b0 x x[n] + b1 x x[n-1] + ... + bN x x[n-N]</p>

<p>Fonction de transfert : H(z) = b0 + b1 x z^(-1) + ... + bN x z^(-N)</p>

<p><strong>Avantages</strong> :</p>
<ul>
<li>Toujours stable (pas de poles, uniquement des zeros)</li>
<li>Phase lineaire possible (important pour audio, images)</li>
<li>Pas de probleme de retroaction</li>
<li>Implementation simple</li>
</ul>

<p><strong>Inconvenients</strong> :</p>
<ul>
<li>Ordre eleve necessaire pour selectivite forte</li>
<li>Temps de calcul proportionnel a l'ordre</li>
<li>Delai de groupe constant mais parfois important</li>
</ul>

<p><strong>Methode des fenetres</strong> :</p>

<p>Principe : partir de la reponse impulsionnelle ideale (infinie) et la tronquer avec une fenetre.</p>

<table>
<tr><th>Fenetre</th><th>Lobe principal</th><th>Attenuation bande coupee</th><th>Ondulation</th></tr>
<tr><td>Rectangulaire</td><td>Etroit</td><td>-21 dB</td><td>Forte (9%)</td></tr>
<tr><td>Hamming</td><td>Moyen</td><td>-53 dB</td><td>Moyenne (0,2%)</td></tr>
<tr><td>Hanning</td><td>Moyen</td><td>-44 dB</td><td>Moyenne</td></tr>
<tr><td>Blackman</td><td>Large</td><td>-74 dB</td><td>Faible</td></tr>
<tr><td>Kaiser</td><td>Ajustable</td><td>Parametrable</td><td>Parametrable</td></tr>
</table>

<p><strong>Compromis</strong> : largeur du lobe principal (bande de transition) vs attenuation bande coupee.</p>

<p><strong>Exemple : filtre passe-bas avec fenetre de Hamming</strong></p>

<pre><code class="language-matlab">% Specifications
Fs = 8000;           % Frequence d'echantillonnage (Hz)
Fc = 1000;           % Frequence de coupure (Hz)
N = 50;              % Ordre du filtre

% Frequence normalisee (0 a 1, ou 1 = Fs/2)
Wn = Fc / (Fs/2);

% Conception
b = fir1(N, Wn, 'low', hamming(N+1));

% Visualisation
freqz(b, 1, 1024, Fs);
title('Filtre passe-bas FIR - Hamming');
</code></pre>

<p><strong>Methode de Parks-McClellan (optimal)</strong> :</p>

<p>Algorithme d'echange de Remez pour obtenir une reponse equi-ondulation (ripple egal en bande passante et bande coupee).</p>

<p>Avantage : ordre minimal pour un gabarit donne.</p>

<pre><code class="language-matlab">% Specifications
F = [0 0.2 0.3 1];     % Frequences normalisees
A = [1 1 0 0];         % Amplitudes souhaitees
b = firpm(50, F, A);   % Conception optimale
</code></pre>

<h3 class="section-title">3. Filtres IIR (Infinite Impulse Response)</h3>

<p><strong>Caracteristiques</strong> :</p>

<p>Un filtre IIR utilise une retroaction (recursion) :</p>

<p>y[n] = b0 x x[n] + b1 x x[n-1] + ... - a1 x y[n-1] - a2 x y[n-2] - ...</p>

<p>Fonction de transfert : H(z) = B(z) / A(z) = (b0 + b1 x z^(-1) + ...) / (1 + a1 x z^(-1) + a2 x z^(-2) + ...)</p>

<p><strong>Avantages</strong> :</p>
<ul>
<li>Ordre faible pour selectivite elevee (efficacite)</li>
<li>Correspondent aux filtres analogiques classiques</li>
<li>Moins de calculs que FIR equivalent</li>
</ul>

<p><strong>Inconvenients</strong> :</p>
<ul>
<li>Potentiellement instables (poles hors cercle unite)</li>
<li>Phase non-lineaire (distorsion de phase)</li>
<li>Sensibles a la quantification des coefficients</li>
<li>Risque de cycles limites (oscillations parasites)</li>
</ul>

<p><strong>Conception par transformation de filtres analogiques</strong> :</p>

<p>On part d'un filtre analogique eprouve (Butterworth, Chebyshev, Elliptique) et on le transforme en filtre numerique.</p>

<p><strong>Approximations analogiques</strong> :</p>

<table>
<tr><th>Type</th><th>Bande passante</th><th>Bande coupee</th><th>Phase</th><th>Ordre</th></tr>
<tr><td>Butterworth</td><td>Maximalement plate</td><td>Monotone</td><td>Bonne</td><td>Eleve</td></tr>
<tr><td>Chebyshev I</td><td>Ondulations</td><td>Monotone</td><td>Moyenne</td><td>Moyen</td></tr>
<tr><td>Chebyshev II</td><td>Plate</td><td>Ondulations</td><td>Moyenne</td><td>Moyen</td></tr>
<tr><td>Elliptique</td><td>Ondulations</td><td>Ondulations</td><td>Mauvaise</td><td>Faible</td></tr>
</table>

<p><strong>Transformation bilineaire</strong> :</p>

<p>Methode la plus utilisee. Transforme l'axe imaginaire du plan s (analogique) vers le cercle unite du plan z (numerique).</p>

<p>Transformation : s = (2/T) x (1 - z^(-1)) / (1 + z^(-1))</p>

<p>ou T est la periode d'echantillonnage.</p>

<p><strong>Pre-deformation en frequence</strong> :</p>

<p>La transformation bilineaire deforme les frequences selon :</p>

<p>Omega_analogique = (2/T) x tan(omega_numerique x T/2)</p>

<p>Il faut donc pre-deformer les specifications avant transformation :</p>

<pre><code class="language-matlab">% Specifications numeriques
Fs = 1000;              % Hz
Fc = 100;               % Hz
Wn = Fc / (Fs/2);       % Frequence normalisee

% Conception Butterworth ordre 4
[b, a] = butter(4, Wn, 'low');

% Verification stabilite
disp(roots(a));         % Tous les poles doivent etre &lt; 1 en module
</code></pre>

<p><strong>Invariance impulsionnelle</strong> :</p>

<p>Consiste a echantillonner la reponse impulsionnelle analogique.</p>

<p>Avantage : correspondance exacte en temporel.<br/>
Inconvenient : repliement spectral (aliasing) si signal large bande.</p>

<h3 class="section-title">4. Stabilite des Filtres Numeriques</h3>

<p><strong>Critere de stabilite</strong> :</p>

<p>Un filtre numerique est stable si et seulement si tous ses poles sont a l'interieur du cercle unite du plan z.</p>

<p>Module de chaque pole &lt; 1</p>

<p><strong>Diagramme poles-zeros</strong> :</p>

<p>Outil essentiel pour visualiser et analyser la stabilite.</p>

<pre><code class="language-matlab">[b, a] = butter(4, 0.2, 'low');
zplane(b, a);
</code></pre>

<ul>
<li><strong>Poles</strong> (x) : racines du denominateur A(z)</li>
<li><strong>Zeros</strong> (o) : racines du numerateur B(z)</li>
<li><strong>Cercle unite</strong> : frontiere de stabilite</li>
</ul>

<p><strong>Interpretation</strong> :</p>
<ul>
<li>Pole proche du cercle unite &rarr; forte resonance</li>
<li>Zero sur le cercle unite &rarr; annulation a cette frequence</li>
<li>Poles complexes conjugues &rarr; oscillations</li>
</ul>

<h3 class="section-title">5. Structures d'Implementation</h3>

<p><strong>Forme directe I</strong> :</p>

<p>Implementation litterale de l'equation aux differences.</p>
<ul>
<li>Avantage : simple a comprendre</li>
<li>Inconvenient : sensible aux erreurs de quantification</li>
</ul>

<p><strong>Forme directe II</strong> :</p>

<p>Rearrangement pour minimiser les memoires (retards).</p>
<ul>
<li>Avantage : moins de memoire (N au lieu de 2N)</li>
<li>Inconvenient : sensible aux debordements intermediaires</li>
</ul>

<p><strong>Forme en cascade (biquads)</strong> :</p>

<p>Decomposition en cellules du 2eme ordre (sections de second ordre).</p>

<p>H(z) = H1(z) x H2(z) x ... x Hk(z)</p>

<ul>
<li>Avantage : robuste a la quantification, stabilite controlee</li>
<li>Utilisation : standard pour IIR</li>
</ul>

<p><strong>Forme parallele</strong> :</p>

<p>Decomposition en fractions partielles.</p>

<p>H(z) = H0 + H1(z) + H2(z) + ... + Hk(z)</p>

<ul>
<li>Avantage : traitement parallelisable</li>
<li>Inconvenient : plus de multiplications</li>
</ul>

<h3 class="section-title">6. Effets de la Quantification</h3>

<p><strong>Sources d'erreurs en virgule fixe</strong> :</p>

<p><strong>1. Quantification des coefficients</strong> :</p>
<ul>
<li>Les coefficients b[k] et a[k] sont arrondis</li>
<li>Impact : deplacement des poles et zeros</li>
<li>Risque : poles sortent du cercle unite &rarr; instabilite</li>
</ul>

<p><strong>2. Quantification des calculs</strong> :</p>
<ul>
<li>Produits et sommes arrondis a chaque etape</li>
<li>Accumulation d'erreurs (bruit de quantification)</li>
</ul>

<p><strong>3. Debordement (overflow)</strong> :</p>
<ul>
<li>Resultats intermediaires depassent la capacite</li>
<li>Solution : mise a l'echelle (scaling)</li>
</ul>

<p><strong>Nombre de bits necessaires</strong> :</p>

<p>Regle empirique :</p>
<ul>
<li>FIR : 12-16 bits suffisent generalement</li>
<li>IIR : 16-24 bits recommandes (plus sensibles)</li>
<li>Forme cascade : meilleure robustesse que forme directe</li>
</ul>

<h3 class="section-title">7. Reponse Frequentielle et Analyse</h3>

<p><strong>Module et phase</strong> :</p>

<p>La reponse frequentielle H(e^(jw)) caracterise le filtre :</p>
<ul>
<li>Module |H(w)| : gain a chaque frequence</li>
<li>Phase arg(H(w)) : dephasage introduit</li>
</ul>

<p><strong>Phase lineaire</strong> :</p>

<p>Condition pour eviter la distorsion de phase : arg(H(w)) = -a x w + b</p>

<p>Les filtres FIR peuvent avoir une phase lineaire si leurs coefficients sont symetriques ou antisymetriques.</p>

<p><strong>Delai de groupe</strong> :</p>

<p>Mesure du retard en fonction de la frequence :</p>

<p>tg(w) = -d[arg(H(w))] / dw</p>

<p>Pour phase lineaire : delai de groupe constant.</p>

<p><strong>Analyse MATLAB</strong> :</p>

<pre><code class="language-matlab">[H, W] = freqz(b, a, 1024);
% Module en dB
subplot(2,1,1);
plot(W/pi, 20*log10(abs(H)));
ylabel('Magnitude (dB)');
% Phase
subplot(2,1,2);
plot(W/pi, angle(H));
ylabel('Phase (radians)');
xlabel('Frequence normalisee (x pi rad/echantillon)');
</code></pre>

<hr/>

<h2>PART D - Analyse Reflexive et Perspectives</h2>

<h3 class="section-title">Competences acquises</h3>

<p><strong>Conception systematique de filtres</strong> :<br/>
Le cours a fourni une methodologie rigoureuse pour passer d'un cahier des charges (frequences, attenuations) a un filtre implementable. Savoir choisir entre FIR et IIR selon les contraintes.</p>

<p><strong>Maitrise de MATLAB</strong> :<br/>
Les TPs ont developpe une aisance avec Signal Processing Toolbox, indispensable pour le traitement du signal moderne. Capacite a prototyper rapidement des solutions.</p>

<p><strong>Analyse frequentielle</strong> :<br/>
Comprehension approfondie du lien temps-frequence, importance de la stabilite, impact des poles et zeros sur la reponse.</p>

<h3 class="section-title">Points cles a retenir</h3>

<p><strong>1. FIR vs IIR - Le choix fondamental</strong> :</p>

<table>
<tr><th>Critere</th><th>Choisir FIR</th><th>Choisir IIR</th></tr>
<tr><td>Phase lineaire requise</td><td>oui</td><td>non</td></tr>
<tr><td>Ordre faible critique</td><td>non</td><td>oui</td></tr>
<tr><td>Stabilite garantie</td><td>oui</td><td>non (verifier)</td></tr>
<tr><td>Audio, images</td><td>oui</td><td>IIR possible</td></tr>
<tr><td>Temps reel contraint</td><td>non (ordre eleve)</td><td>oui</td></tr>
</table>

<p><strong>2. Stabilite avant tout</strong> :<br/>
Toujours verifier que les poles sont dans le cercle unite. Un filtre instable est inutilisable.</p>

<p><strong>3. Frequences normalisees</strong> :<br/>
Attention aux conversions : frequence physique (Hz) &rarr; normalisee (0 a 1) &rarr; pulsation numerique (0 a pi).</p>

<p><strong>4. Quantification</strong> :<br/>
En implementation reelle (DSP, FPGA), les effets de virgule fixe peuvent detruire les performances. Toujours simuler avec quantification.</p>

<h3 class="section-title">Applications pratiques</h3>

<p><strong>Audio et musique</strong> :</p>
<ul>
<li>Egaliseurs (filtres passe-bande multiples)</li>
<li>Effets (reverberation, chorus utilisant IIR)</li>
<li>Reduction de bruit (filtrage adaptatif)</li>
</ul>

<p><strong>Biomedical</strong> :</p>
<ul>
<li>Filtrage ECG : passe-bande 0,5-40 Hz pour eliminer 50 Hz secteur</li>
<li>EEG : extraction de rythmes cerebraux (alpha, beta, theta)</li>
<li>Detection d'anomalies cardiaques</li>
</ul>

<p><strong>Telecommunications</strong> :</p>
<ul>
<li>Filtres de mise en forme (raised cosine)</li>
<li>Egalisation de canal</li>
<li>Filtres anti-repliement (avant CAN) et de reconstruction (apres CNA)</li>
</ul>

<p><strong>Traitement d'images</strong> :</p>
<ul>
<li>Flou (passe-bas 2D)</li>
<li>Detection de contours (passe-haut 2D)</li>
<li>Debruitage (filtres medians, Wiener)</li>
</ul>

<h3 class="section-title">Liens avec projets et autres cours</h3>

<p><strong>Projets personnels</strong> :<br/>
Les competences en filtrage numerique ont ete appliquees dans plusieurs contextes :</p>
<ul>
<li>Analyse de signaux vibratoires pour maintenance predictive</li>
<li>Traitement de signaux audio pour reconnaissance vocale</li>
<li>Pretraitement de donnees IoT (capteurs accelerometres)</li>
</ul>

<p><strong>Complementarite avec d'autres cours</strong> :</p>
<ul>
<li><strong>Signal (S5)</strong> : bases theoriques (Fourier, Laplace, echantillonnage)</li>
<li><strong>Embedded IA (S9)</strong> : filtrage comme etape de preprocessing pour ML</li>
<li><strong>Chaines d'Acquisition (S8)</strong> : filtres anti-repliement et reconstruction</li>
<li><strong>Temps Reel (S8)</strong> : contraintes d'implementation et optimisation</li>
</ul>

<h3 class="section-title">Limites et ouvertures</h3>

<p><strong>Limites du cours</strong> :</p>
<ul>
<li>Peu sur les filtres adaptatifs (LMS, RLS)</li>
<li>Pas de traitement multirate (decimation, interpolation)</li>
<li>Aspects temps reel peu developpes (latence, throughput)</li>
<li>Implementation materielle (FPGA, DSP) non abordee</li>
</ul>

<p><strong>Ouvertures vers</strong> :</p>
<ul>
<li><strong>Filtrage adaptatif</strong> : applications en annulation d'echo, egalisation</li>
<li><strong>Bancs de filtres</strong> : compression audio (MP3), analyse multiresolution</li>
<li><strong>Traitement temps-frequence</strong> : transformees en ondelettes</li>
<li><strong>Filtrage optimal</strong> : filtres de Wiener, Kalman</li>
<li><strong>Traitement d'antenne</strong> : beamforming, filtrage spatial</li>
</ul>

<h3 class="section-title">Evolution technologique</h3>

<p><strong>Tendances actuelles</strong> :</p>
<ul>
<li><strong>Machine learning</strong> : remplacement de filtres classiques par reseaux de neurones pour debruitage</li>
<li><strong>Filtrage embarque</strong> : acceleration materielle (GPU, FPGA, ASIC)</li>
<li><strong>Filtrage distribue</strong> : traitement en edge computing pour IoT</li>
<li><strong>Filtrage quantique</strong> : perspectives avec calcul quantique</li>
</ul>

<p><strong>Outils modernes</strong> :</p>
<ul>
<li>Python scipy.signal : alternative a MATLAB pour le prototypage</li>
<li>TensorFlow/PyTorch : filtrage par apprentissage profond</li>
<li>CMSIS-DSP : bibliotheques optimisees pour ARM Cortex-M</li>
<li>High-Level Synthesis : conception FPGA en C/C++</li>
</ul>

<h3 class="section-title">Conclusion</h3>

<p>Le filtrage numerique est un pilier du traitement du signal. Maitriser FIR et IIR, comprendre le compromis ordre/performances, et savoir utiliser les outils de conception sont des competences essentielles pour l'ingenieur en systemes embarques, telecommunications, ou traitement de donnees.</p>

<p>Ce cours a fourni une base solide theorique (transformee en Z, stabilite) et pratique (MATLAB, implementation). La capacite a concevoir un filtre adapte a un cahier des charges, verifier sa stabilite, et l'implementer efficacement est desormais acquise.</p>

<p><strong>Ressources pour approfondir</strong> :</p>
<ul>
<li>Playlist YouTube du cours : <a href="https://www.youtube.com/playlist?list=PL_wkaC4iMBTlJQpi7W18pkzR_kY9d-jsU">Traitement du Signal</a></li>
<li>Annales avec corrections (2022, 2023) pour s'entrainer</li>
<li>MATLAB Signal Processing Toolbox documentation</li>
<li>Livres : "Digital Signal Processing" de Proakis &amp; Manolakis</li>
</ul>

<p><strong>Liens avec les autres cours</strong> :</p>
<ul>
<li><a href="./signal.html">Signal - S5</a> : fondements theoriques</li>
<li><a href="./electronique-fonctions-analogiques.html">Electronique Fonctions Analogiques - S6</a> : filtres actifs</li>
<li><a href="./chaines-acquisition.html">Chaines Electroniques d'Acquisition - S8</a> : application complete</li>
<li><a href="./embedded-ia-iot.html">Embedded IA for IoT - S9</a> : pretraitement ML</li>
</ul>

<hr/>

<h2>Documents de Cours</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Sujet Examen 2023</h4>
      <p>Enonce de l'examen de Filtrage Numerique 2023 avec exercices sur FIR/IIR, transformee en Z et conception de filtres.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S6/Filtrage-Numerique/sujet-examen-2023.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S6/Filtrage-Numerique/sujet-examen-2023.pdf" target="_blank">Telecharger le sujet</a></p>
    </div>
    <div class="pdf-item">
      <h4>Correction Examen 2023</h4>
      <p>Correction detaillee de l'examen avec les solutions completes et explications des methodes de conception.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S6/Filtrage-Numerique/correction-examen-2023.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S6/Filtrage-Numerique/correction-examen-2023.pdf" target="_blank">Telecharger la correction</a></p>
    </div>
  </div>
</div>

</div>

<!-- ==================== ENGLISH VERSION ==================== -->
<div class="lang-en">

<h1>Digital Filtering - Semester 6</h1>

<p><strong>Academic Year</strong>: 2022-2023<br/>
<strong>Semester</strong>: 6<br/>
<strong>Credits</strong>: 2.5 ECTS<br/>
<strong>Specialization</strong>: Signal Processing and Control Systems</p>

<hr/>

<h2>PART A - General Course Overview</h2>

<h3 class="section-title">Overview</h3>

<p>This course delves into digital signal processing with a focus on the design and implementation of digital filters. It covers the two main filter families: FIR (Finite Impulse Response) and IIR (Infinite Impulse Response), along with their respective design methods. The course combines mathematical theory (Z-transform, frequency response) and practice (MATLAB, implementation).</p>

<p><strong>Learning objectives</strong>:</p>
<ul>
<li>Master the Z-transform and frequency-domain analysis</li>
<li>Design FIR filters using the windowing method</li>
<li>Design IIR filters using bilinear transformation and impulse invariance</li>
<li>Analyze the stability and performance of digital filters</li>
<li>Implement and test filters in MATLAB</li>
</ul>

<h3 class="section-title">Position in the curriculum</h3>

<p>This course builds upon and complements:</p>
<ul>
<li><strong>Signal Processing (S5)</strong>: Fourier transform, Laplace transform, sampling</li>
<li><strong>Linear Systems Modeling (S5)</strong>: transfer functions, stability</li>
</ul>

<p>It prepares for applications in:</p>
<ul>
<li><strong>Advanced Signal Processing</strong>: audio, biomedical, and communications applications</li>
<li><strong>Embedded AI for IoT (S9)</strong>: signal preprocessing for machine learning</li>
<li><strong>Data processing projects</strong>: spectral analysis, adaptive filtering</li>
</ul>

<hr/>

<h2>PART B - Personal Experience and Learning Context</h2>

<h3 class="section-title">Organization and resources</h3>

<p>The module was structured around three pillars:</p>

<p><strong>1. Lectures</strong>:</p>
<ul>
<li>Review of sampling and the Z-transform</li>
<li>FIR filters: properties, design methods</li>
<li>IIR filters: transformation of analog filters</li>
<li>Implementation structures and quantization effects</li>
</ul>

<p><strong>2. Tutorials</strong>:</p>
<ul>
<li>FIR filter design exercises using windowing</li>
<li>Bilinear transformation for IIR filters</li>
<li>Stability analysis (pole and zero placement)</li>
<li>Frequency response calculations</li>
</ul>

<p><strong>3. MATLAB lab sessions</strong>:</p>
<ul>
<li>Using the fdatool (Filter Design and Analysis Tool)</li>
<li>Design and testing of FIR and IIR filters</li>
<li>Performance comparison (order, attenuation, phase)</li>
<li>Application to real signals (audio, ECG)</li>
</ul>

<p><strong>Teaching resources</strong>:</p>
<ul>
<li>YouTube playlist with lectures and tutorials: <a href="https://www.youtube.com/playlist?list=PL_wkaC4iMBTlJQpi7W18pkzR_kY9d-jsU">Signal Processing</a></li>
<li>2022 and 2023 past exam papers with solutions</li>
<li>MATLAB Signal Processing Toolbox documentation</li>
</ul>

<h3 class="section-title">Progression and methodology</h3>

<p><strong>Progressive approach</strong>:</p>

<p>The course followed a three-step approach:</p>

<ol>
<li><strong>Theory</strong>: establish mathematical foundations (Z-transform, difference equations)</li>
<li><strong>Methods</strong>: apply systematic design techniques</li>
<li><strong>Practice</strong>: validate and optimize with MATLAB</li>
</ol>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S6/filtrage-numerique/filtrage.svg" alt="Digital filtering" style="max-width: 550px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Digital filtering principle - Noise reduction through filtering</p>
</div>

<p><strong>Example of FIR low-pass filter design</strong>:</p>

<p>Specifications:</p>
<ul>
<li>Cutoff frequency: 1 kHz</li>
<li>Sampling frequency: 8 kHz</li>
<li>Stopband attenuation: &gt; 40 dB</li>
<li>Passband ripple: &lt; 0.5 dB</li>
</ul>

<p>Design steps:</p>
<ol>
<li>Choose the method (Hamming window as a compromise)</li>
<li>Calculate the required order (based on the specification template)</li>
<li>Generate coefficients with MATLAB: fir1(N, Wn, 'low')</li>
<li>Verify the frequency response: freqz(b, a)</li>
<li>Test on a real signal</li>
</ol>

<h3 class="section-title">Exams and assessments</h3>

<p><strong>Exam format</strong>:</p>

<p>Past papers show a recurring structure:</p>

<p><strong>Exercise 1: FIR Filters</strong> (30-40%)</p>
<ul>
<li>Design by windowing</li>
<li>Calculation of the minimum order</li>
<li>Comparison of different windows</li>
<li>Frequency response analysis</li>
</ul>

<p><strong>Exercise 2: IIR Filters</strong> (30-40%)</p>
<ul>
<li>Bilinear transformation or impulse invariance</li>
<li>Calculation of the Z-domain transfer function</li>
<li>Pole and zero placement</li>
<li>Stability verification</li>
</ul>

<p><strong>Exercise 3: Implementation</strong> (20-30%)</p>
<ul>
<li>Direct form or cascade structure</li>
<li>Quantization effects</li>
<li>Bit-width optimization</li>
<li>Difference equations</li>
</ul>

<p><strong>Common difficulties</strong>:</p>
<ul>
<li>Confusion between normalized frequency (0 to 1) and physical frequency (Hz)</li>
<li>Errors in bilinear transformation (frequency pre-warping)</li>
<li>Forgetting to verify stability (poles inside the unit circle)</li>
<li>Misinterpretation of specifications (dB vs. linear)</li>
</ul>

<h3 class="section-title">MATLAB tools used</h3>

<p><strong>Key functions</strong>:</p>

<pre><code class="language-matlab">% FIR Design
b = fir1(N, Wn, 'type');              % Window method
b = firpm(N, F, A);                    % Parks-McClellan (optimal)

% IIR Design
[b,a] = butter(N, Wn, 'type');         % Butterworth
[b,a] = cheby1(N, Rp, Wn, 'type');     % Chebyshev Type I
[b,a] = cheby2(N, Rs, Wn, 'type');     % Chebyshev Type II
[b,a] = ellip(N, Rp, Rs, Wn, 'type');  % Elliptic

% Analysis
freqz(b, a, N);                        % Frequency response
zplane(b, a);                          % Pole-zero diagram
grpdelay(b, a);                        % Group delay
filter(b, a, x);                       % Filtering
</code></pre>

<hr/>

<h2>PART C - Detailed Technical Aspects</h2>

<h3 class="section-title">1. Foundations: The Z-Transform</h3>

<p>The Z-transform is the discrete equivalent of the Laplace transform.</p>

<p><strong>Definition</strong>:<br/>
For a discrete signal x[n], the Z-transform is:</p>

<p>X(z) = sum of x[n] x z^(-n) for n from -infinity to +infinity</p>

<p><strong>Important properties</strong>:</p>
<ul>
<li>Linearity: Z{a x x[n] + b x y[n]} = a x X(z) + b x Y(z)</li>
<li>Time shift: Z{x[n-k]} = z^(-k) x X(z)</li>
<li>Convolution: Z{x[n] * h[n]} = X(z) x H(z)</li>
</ul>

<p><strong>Region of Convergence (ROC)</strong>:<br/>
The region of the complex plane where the transform converges. Critical for stability.</p>

<p><strong>Relationship with the Fourier transform</strong>:<br/>
On the unit circle (z = e^(jw)), the Z-transform becomes the DTFT (Discrete-Time Fourier Transform).</p>

<h3 class="section-title">2. FIR Filters (Finite Impulse Response)</h3>

<p><strong>Characteristics</strong>:</p>

<p>An FIR filter has a finite-duration impulse response:</p>

<p>y[n] = b0 x x[n] + b1 x x[n-1] + ... + bN x x[n-N]</p>

<p>Transfer function: H(z) = b0 + b1 x z^(-1) + ... + bN x z^(-N)</p>

<p><strong>Advantages</strong>:</p>
<ul>
<li>Always stable (no poles, only zeros)</li>
<li>Linear phase possible (important for audio, images)</li>
<li>No feedback issues</li>
<li>Simple implementation</li>
</ul>

<p><strong>Disadvantages</strong>:</p>
<ul>
<li>High order required for sharp selectivity</li>
<li>Computation time proportional to order</li>
<li>Constant but sometimes significant group delay</li>
</ul>

<p><strong>Windowing method</strong>:</p>

<p>Principle: start from the ideal (infinite) impulse response and truncate it with a window function.</p>

<table>
<tr><th>Window</th><th>Main lobe</th><th>Stopband attenuation</th><th>Ripple</th></tr>
<tr><td>Rectangular</td><td>Narrow</td><td>-21 dB</td><td>High (9%)</td></tr>
<tr><td>Hamming</td><td>Medium</td><td>-53 dB</td><td>Medium (0.2%)</td></tr>
<tr><td>Hanning</td><td>Medium</td><td>-44 dB</td><td>Medium</td></tr>
<tr><td>Blackman</td><td>Wide</td><td>-74 dB</td><td>Low</td></tr>
<tr><td>Kaiser</td><td>Adjustable</td><td>Configurable</td><td>Configurable</td></tr>
</table>

<p><strong>Trade-off</strong>: main lobe width (transition band) vs. stopband attenuation.</p>

<p><strong>Example: low-pass filter with Hamming window</strong></p>

<pre><code class="language-matlab">% Specifications
Fs = 8000;           % Sampling frequency (Hz)
Fc = 1000;           % Cutoff frequency (Hz)
N = 50;              % Filter order

% Normalized frequency (0 to 1, where 1 = Fs/2)
Wn = Fc / (Fs/2);

% Design
b = fir1(N, Wn, 'low', hamming(N+1));

% Visualization
freqz(b, 1, 1024, Fs);
title('FIR Low-pass Filter - Hamming');
</code></pre>

<p><strong>Parks-McClellan method (optimal)</strong>:</p>

<p>Remez exchange algorithm to obtain an equiripple response (equal ripple in passband and stopband).</p>

<p>Advantage: minimum order for a given specification template.</p>

<pre><code class="language-matlab">% Specifications
F = [0 0.2 0.3 1];     % Normalized frequencies
A = [1 1 0 0];         % Desired amplitudes
b = firpm(50, F, A);   % Optimal design
</code></pre>

<h3 class="section-title">3. IIR Filters (Infinite Impulse Response)</h3>

<p><strong>Characteristics</strong>:</p>

<p>An IIR filter uses feedback (recursion):</p>

<p>y[n] = b0 x x[n] + b1 x x[n-1] + ... - a1 x y[n-1] - a2 x y[n-2] - ...</p>

<p>Transfer function: H(z) = B(z) / A(z) = (b0 + b1 x z^(-1) + ...) / (1 + a1 x z^(-1) + a2 x z^(-2) + ...)</p>

<p><strong>Advantages</strong>:</p>
<ul>
<li>Low order for high selectivity (efficiency)</li>
<li>Correspond to classical analog filters</li>
<li>Fewer computations than equivalent FIR</li>
</ul>

<p><strong>Disadvantages</strong>:</p>
<ul>
<li>Potentially unstable (poles outside unit circle)</li>
<li>Non-linear phase (phase distortion)</li>
<li>Sensitive to coefficient quantization</li>
<li>Risk of limit cycles (parasitic oscillations)</li>
</ul>

<p><strong>Design by transformation of analog filters</strong>:</p>

<p>Start from a proven analog filter (Butterworth, Chebyshev, Elliptic) and transform it into a digital filter.</p>

<p><strong>Analog approximations</strong>:</p>

<table>
<tr><th>Type</th><th>Passband</th><th>Stopband</th><th>Phase</th><th>Order</th></tr>
<tr><td>Butterworth</td><td>Maximally flat</td><td>Monotonic</td><td>Good</td><td>High</td></tr>
<tr><td>Chebyshev I</td><td>Ripples</td><td>Monotonic</td><td>Medium</td><td>Medium</td></tr>
<tr><td>Chebyshev II</td><td>Flat</td><td>Ripples</td><td>Medium</td><td>Medium</td></tr>
<tr><td>Elliptic</td><td>Ripples</td><td>Ripples</td><td>Poor</td><td>Low</td></tr>
</table>

<p><strong>Bilinear transformation</strong>:</p>

<p>Most widely used method. Maps the imaginary axis of the s-plane (analog) to the unit circle of the z-plane (digital).</p>

<p>Transformation: s = (2/T) x (1 - z^(-1)) / (1 + z^(-1))</p>

<p>where T is the sampling period.</p>

<p><strong>Frequency pre-warping</strong>:</p>

<p>The bilinear transformation warps frequencies according to:</p>

<p>Omega_analog = (2/T) x tan(omega_digital x T/2)</p>

<p>Therefore, specifications must be pre-warped before transformation:</p>

<pre><code class="language-matlab">% Digital specifications
Fs = 1000;              % Hz
Fc = 100;               % Hz
Wn = Fc / (Fs/2);       % Normalized frequency

% Butterworth design, order 4
[b, a] = butter(4, Wn, 'low');

% Stability verification
disp(roots(a));         % All poles must have magnitude &lt; 1
</code></pre>

<p><strong>Impulse invariance</strong>:</p>

<p>Consists of sampling the analog impulse response.</p>

<p>Advantage: exact time-domain correspondence.<br/>
Disadvantage: spectral aliasing if the signal is wideband.</p>

<h3 class="section-title">4. Stability of Digital Filters</h3>

<p><strong>Stability criterion</strong>:</p>

<p>A digital filter is stable if and only if all its poles are inside the unit circle in the z-plane.</p>

<p>Magnitude of each pole &lt; 1</p>

<p><strong>Pole-zero diagram</strong>:</p>

<p>Essential tool for visualizing and analyzing stability.</p>

<pre><code class="language-matlab">[b, a] = butter(4, 0.2, 'low');
zplane(b, a);
</code></pre>

<ul>
<li><strong>Poles</strong> (x): roots of the denominator A(z)</li>
<li><strong>Zeros</strong> (o): roots of the numerator B(z)</li>
<li><strong>Unit circle</strong>: stability boundary</li>
</ul>

<p><strong>Interpretation</strong>:</p>
<ul>
<li>Pole close to the unit circle &rarr; strong resonance</li>
<li>Zero on the unit circle &rarr; null at that frequency</li>
<li>Complex conjugate poles &rarr; oscillations</li>
</ul>

<h3 class="section-title">5. Implementation Structures</h3>

<p><strong>Direct Form I</strong>:</p>

<p>Literal implementation of the difference equation.</p>
<ul>
<li>Advantage: easy to understand</li>
<li>Disadvantage: sensitive to quantization errors</li>
</ul>

<p><strong>Direct Form II</strong>:</p>

<p>Rearrangement to minimize memory (delays).</p>
<ul>
<li>Advantage: less memory (N instead of 2N)</li>
<li>Disadvantage: sensitive to intermediate overflow</li>
</ul>

<p><strong>Cascade form (biquads)</strong>:</p>

<p>Decomposition into second-order cells (second-order sections).</p>

<p>H(z) = H1(z) x H2(z) x ... x Hk(z)</p>

<ul>
<li>Advantage: robust to quantization, controlled stability</li>
<li>Usage: standard for IIR</li>
</ul>

<p><strong>Parallel form</strong>:</p>

<p>Partial fraction decomposition.</p>

<p>H(z) = H0 + H1(z) + H2(z) + ... + Hk(z)</p>

<ul>
<li>Advantage: parallelizable processing</li>
<li>Disadvantage: more multiplications</li>
</ul>

<h3 class="section-title">6. Quantization Effects</h3>

<p><strong>Sources of error in fixed-point arithmetic</strong>:</p>

<p><strong>1. Coefficient quantization</strong>:</p>
<ul>
<li>Coefficients b[k] and a[k] are rounded</li>
<li>Impact: displacement of poles and zeros</li>
<li>Risk: poles move outside the unit circle &rarr; instability</li>
</ul>

<p><strong>2. Computation quantization</strong>:</p>
<ul>
<li>Products and sums rounded at each step</li>
<li>Error accumulation (quantization noise)</li>
</ul>

<p><strong>3. Overflow</strong>:</p>
<ul>
<li>Intermediate results exceed capacity</li>
<li>Solution: scaling</li>
</ul>

<p><strong>Required number of bits</strong>:</p>

<p>Rule of thumb:</p>
<ul>
<li>FIR: 12-16 bits generally sufficient</li>
<li>IIR: 16-24 bits recommended (more sensitive)</li>
<li>Cascade form: better robustness than direct form</li>
</ul>

<h3 class="section-title">7. Frequency Response and Analysis</h3>

<p><strong>Magnitude and phase</strong>:</p>

<p>The frequency response H(e^(jw)) characterizes the filter:</p>
<ul>
<li>Magnitude |H(w)|: gain at each frequency</li>
<li>Phase arg(H(w)): phase shift introduced</li>
</ul>

<p><strong>Linear phase</strong>:</p>

<p>Condition to avoid phase distortion: arg(H(w)) = -a x w + b</p>

<p>FIR filters can achieve linear phase if their coefficients are symmetric or antisymmetric.</p>

<p><strong>Group delay</strong>:</p>

<p>Measure of delay as a function of frequency:</p>

<p>tg(w) = -d[arg(H(w))] / dw</p>

<p>For linear phase: constant group delay.</p>

<p><strong>MATLAB analysis</strong>:</p>

<pre><code class="language-matlab">[H, W] = freqz(b, a, 1024);
% Magnitude in dB
subplot(2,1,1);
plot(W/pi, 20*log10(abs(H)));
ylabel('Magnitude (dB)');
% Phase
subplot(2,1,2);
plot(W/pi, angle(H));
ylabel('Phase (radians)');
xlabel('Normalized frequency (x pi rad/sample)');
</code></pre>

<hr/>

<h2>PART D - Reflective Analysis and Perspectives</h2>

<h3 class="section-title">Skills acquired</h3>

<p><strong>Systematic filter design</strong>:<br/>
The course provided a rigorous methodology for going from specifications (frequencies, attenuations) to an implementable filter. Knowing how to choose between FIR and IIR based on constraints.</p>

<p><strong>MATLAB proficiency</strong>:<br/>
The lab sessions developed fluency with the Signal Processing Toolbox, essential for modern signal processing. Ability to rapidly prototype solutions.</p>

<p><strong>Frequency analysis</strong>:<br/>
Deep understanding of the time-frequency relationship, importance of stability, and impact of poles and zeros on the response.</p>

<h3 class="section-title">Key takeaways</h3>

<p><strong>1. FIR vs IIR - The fundamental choice</strong>:</p>

<table>
<tr><th>Criterion</th><th>Choose FIR</th><th>Choose IIR</th></tr>
<tr><td>Linear phase required</td><td>Yes</td><td>No</td></tr>
<tr><td>Low order critical</td><td>No</td><td>Yes</td></tr>
<tr><td>Guaranteed stability</td><td>Yes</td><td>No (must verify)</td></tr>
<tr><td>Audio, images</td><td>Yes</td><td>IIR possible</td></tr>
<tr><td>Real-time constrained</td><td>No (high order)</td><td>Yes</td></tr>
</table>

<p><strong>2. Stability first</strong>:<br/>
Always verify that poles are inside the unit circle. An unstable filter is unusable.</p>

<p><strong>3. Normalized frequencies</strong>:<br/>
Pay attention to conversions: physical frequency (Hz) &rarr; normalized (0 to 1) &rarr; digital angular frequency (0 to pi).</p>

<p><strong>4. Quantization</strong>:<br/>
In real implementations (DSP, FPGA), fixed-point effects can destroy performance. Always simulate with quantization.</p>

<h3 class="section-title">Practical applications</h3>

<p><strong>Audio and music</strong>:</p>
<ul>
<li>Equalizers (multiple bandpass filters)</li>
<li>Effects (reverb, chorus using IIR)</li>
<li>Noise reduction (adaptive filtering)</li>
</ul>

<p><strong>Biomedical</strong>:</p>
<ul>
<li>ECG filtering: bandpass 0.5-40 Hz to eliminate 50 Hz mains interference</li>
<li>EEG: extraction of brain rhythms (alpha, beta, theta)</li>
<li>Cardiac anomaly detection</li>
</ul>

<p><strong>Telecommunications</strong>:</p>
<ul>
<li>Pulse-shaping filters (raised cosine)</li>
<li>Channel equalization</li>
<li>Anti-aliasing filters (before ADC) and reconstruction filters (after DAC)</li>
</ul>

<p><strong>Image processing</strong>:</p>
<ul>
<li>Blurring (2D low-pass)</li>
<li>Edge detection (2D high-pass)</li>
<li>Denoising (median filters, Wiener)</li>
</ul>

<h3 class="section-title">Links to projects and other courses</h3>

<p><strong>Personal projects</strong>:<br/>
Digital filtering skills were applied in several contexts:</p>
<ul>
<li>Vibration signal analysis for predictive maintenance</li>
<li>Audio signal processing for speech recognition</li>
<li>IoT data preprocessing (accelerometer sensors)</li>
</ul>

<p><strong>Complementarity with other courses</strong>:</p>
<ul>
<li><strong>Signal Processing (S5)</strong>: theoretical foundations (Fourier, Laplace, sampling)</li>
<li><strong>Embedded AI (S9)</strong>: filtering as a preprocessing step for ML</li>
<li><strong>Acquisition Chains (S8)</strong>: anti-aliasing and reconstruction filters</li>
<li><strong>Real-Time Systems (S8)</strong>: implementation constraints and optimization</li>
</ul>

<h3 class="section-title">Limitations and future directions</h3>

<p><strong>Course limitations</strong>:</p>
<ul>
<li>Little on adaptive filters (LMS, RLS)</li>
<li>No multirate processing (decimation, interpolation)</li>
<li>Real-time aspects underdeveloped (latency, throughput)</li>
<li>Hardware implementation (FPGA, DSP) not covered</li>
</ul>

<p><strong>Future directions</strong>:</p>
<ul>
<li><strong>Adaptive filtering</strong>: applications in echo cancellation, equalization</li>
<li><strong>Filter banks</strong>: audio compression (MP3), multiresolution analysis</li>
<li><strong>Time-frequency processing</strong>: wavelet transforms</li>
<li><strong>Optimal filtering</strong>: Wiener, Kalman filters</li>
<li><strong>Antenna processing</strong>: beamforming, spatial filtering</li>
</ul>

<h3 class="section-title">Technological evolution</h3>

<p><strong>Current trends</strong>:</p>
<ul>
<li><strong>Machine learning</strong>: replacing classical filters with neural networks for denoising</li>
<li><strong>Embedded filtering</strong>: hardware acceleration (GPU, FPGA, ASIC)</li>
<li><strong>Distributed filtering</strong>: edge computing processing for IoT</li>
<li><strong>Quantum filtering</strong>: perspectives with quantum computing</li>
</ul>

<p><strong>Modern tools</strong>:</p>
<ul>
<li>Python scipy.signal: alternative to MATLAB for prototyping</li>
<li>TensorFlow/PyTorch: deep learning-based filtering</li>
<li>CMSIS-DSP: optimized libraries for ARM Cortex-M</li>
<li>High-Level Synthesis: FPGA design in C/C++</li>
</ul>

<h3 class="section-title">Conclusion</h3>

<p>Digital filtering is a cornerstone of signal processing. Mastering FIR and IIR, understanding the order/performance trade-off, and knowing how to use design tools are essential skills for engineers in embedded systems, telecommunications, or data processing.</p>

<p>This course provided a solid theoretical foundation (Z-transform, stability) and practical experience (MATLAB, implementation). The ability to design a filter matching specifications, verify its stability, and implement it efficiently has been achieved.</p>

<p><strong>Resources for further study</strong>:</p>
<ul>
<li>Course YouTube playlist: <a href="https://www.youtube.com/playlist?list=PL_wkaC4iMBTlJQpi7W18pkzR_kY9d-jsU">Signal Processing</a></li>
<li>Past exam papers with solutions (2022, 2023) for practice</li>
<li>MATLAB Signal Processing Toolbox documentation</li>
<li>Books: "Digital Signal Processing" by Proakis &amp; Manolakis</li>
</ul>

<p><strong>Links to other courses</strong>:</p>
<ul>
<li><a href="./signal.html">Signal Processing - S5</a>: theoretical foundations</li>
<li><a href="./electronique-fonctions-analogiques.html">Analog Electronics - S6</a>: active filters</li>
<li><a href="./chaines-acquisition.html">Electronic Acquisition Chains - S8</a>: complete application</li>
<li><a href="./embedded-ia-iot.html">Embedded AI for IoT - S9</a>: ML preprocessing</li>
</ul>

<hr/>

<h2>Course Documents</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>2023 Exam Paper</h4>
      <p>2023 Digital Filtering exam paper with exercises on FIR/IIR, Z-transform, and filter design.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S6/Filtrage-Numerique/sujet-examen-2023.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S6/Filtrage-Numerique/sujet-examen-2023.pdf" target="_blank">Download the exam paper</a></p>
    </div>
    <div class="pdf-item">
      <h4>2023 Exam Solutions</h4>
      <p>Detailed exam solutions with complete answers and explanations of design methods.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S6/Filtrage-Numerique/correction-examen-2023.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S6/Filtrage-Numerique/correction-examen-2023.pdf" target="_blank">Download the solutions</a></p>
    </div>
  </div>
</div>

</div>

<div class="back-nav">
    <a href="./my-courses-2022-2023.html" data-i18n-html="back-courses-2022-2023">← Retour aux Cours 2022-2023</a>
</div>

<hr/>

<em class="lang-fr">Cours enseigne en 2022-2023 a l'INSA Toulouse, Departement Genie Electrique et Informatique.</em><em class="lang-en">Course taught in 2022-2023 at INSA Toulouse, Department of Electrical and Computer Engineering.</em>

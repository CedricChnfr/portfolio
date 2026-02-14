---
layout: default
title:  "Architectures Analogiques Transmission Information - S7"
date:   2024-10-02 09:01:00 +0200
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
    <a href="./my-courses-2023-2024.html">← Retour aux Cours 2023-2024</a>
</div>

<div class="lang-fr">

<h1>Architectures Analogiques Transmission Information - Semestre 7</h1>

<p><strong>Annee Universitaire</strong> : 2023-2024<br/>
<strong>Semestre</strong> : 7<br/>
<strong>Credits</strong> : 2.5 ECTS<br/>
<strong>Specialite</strong> : Electronique Analogique et RF</p>

<hr/>

<h2>PART A - Presentation Generale du Module</h2>

<h3 class="section-title">Vue d'ensemble</h3>

<p>Ce cours aborde les architectures analogiques pour la transmission d'information, avec un focus sur les systemes de modulation/demodulation et les chaines d'emission/reception radio-frequence (RF). Il couvre les techniques de modulation analogique (AM, FM), les oscillateurs, les multiplieurs, et les architectures de recepteurs.</p>

<p><strong>Objectifs pedagogiques</strong> :</p>
<ul>
<li>Maitriser les techniques de modulation et demodulation analogiques</li>
<li>Comprendre les architectures de chaines RF (emission et reception)</li>
<li>Concevoir des oscillateurs et circuits de synthese de frequence</li>
<li>Analyser les performances des systemes de transmission (bruit, linearite)</li>
<li>Dimensionner des circuits pour applications radio</li>
</ul>

<h3 class="section-title">Position dans le cursus</h3>

<p>Ce module s'appuie sur :</p>
<ul>
<li><strong>Electronique Fonctions Analogiques (S6)</strong> : AOPs, filtres actifs</li>
<li><strong>Signal (S5)</strong> : modulation, transformee de Fourier</li>
<li><strong>Circuits et Filtres analogiques (S5)</strong> : filtres, adaptation d'impedance</li>
</ul>

<p>Il prepare a :</p>
<ul>
<li><strong>Telecommunications</strong> : conception de systemes RF</li>
<li><strong>Systemes embarques communicants</strong> : IoT, radio courte portee</li>
<li><strong>Instrumentation RF</strong> : generateurs, analyseurs</li>
</ul>

<hr/>

<h2>PART B - Experience Personnelle et Contexte d'Apprentissage</h2>

<h3 class="section-title">Organisation et ressources</h3>

<p>Le module etait organise en cours magistraux et travaux diriges :</p>

<p><strong>Cours magistraux (20h)</strong> :</p>
<p>Couvrant les themes principaux :</p>
<ul>
<li>Modulation et demodulation AM/FM</li>
<li>Oscillateurs (theorie et applications)</li>
<li>Multiplieurs analogiques</li>
<li>Architectures de recepteurs (superheterodyne)</li>
<li>Boucles a verrouillage de phase (PLL)</li>
</ul>

<p><strong>Travaux diriges (16h)</strong> :</p>
<p>5 TD avec corrections disponibles :</p>
<ul>
<li>TD1 a TD5 : exercices d'application sur modulation, oscillateurs, multiplieurs</li>
</ul>

<p><strong>Supports pedagogiques</strong> :</p>
<ul>
<li>Document de cours principal (ArchiUF_2022-2023.pdf)</li>
<li>Notes de cours sur oscillateurs (Notes-cours-Theorie-Osc.pdf)</li>
<li>Documents techniques (multiplieurs ADI, oscillateurs a quartz)</li>
<li>Annales 2018-2019, 2021-2022 avec corrections</li>
</ul>

<h3 class="section-title">Contenu des ressources</h3>

<p><strong>Documents techniques disponibles</strong> :</p>
<ul>
<li><strong>Multiplieurs</strong> : ADI Multiplier Applications Guide, multiplieurs 1 a 4 quadrants</li>
<li><strong>Oscillateurs</strong> : theorie, oscillateurs a quartz (AN3208)</li>
<li><strong>Modulation FM</strong> : modulation et demodulation FM</li>
<li><strong>Detection</strong> : demodulation par detection d'enveloppe</li>
<li><strong>Circuits specifiques</strong> : RLC avec resistance negative, redresseur sans seuil</li>
</ul>

<h3 class="section-title">Methode de travail</h3>

<p><strong>Cours theorique</strong> :</p>
<p>Beaucoup de schemas et d'analyses de circuits. Comprehension des principes de fonctionnement des modulateurs, demodulateurs, et oscillateurs.</p>

<p><strong>TD pratiques</strong> :</p>
<p>Calculs de performances (taux de modulation, deviation de frequence, gain, bruit). Dimensionnement de composants.</p>

<p><strong>Annales</strong> :</p>
<p>Examens de 2018-2019 et 2021-2022 avec corrections pour s'entrainer.</p>

<h3 class="section-title">Difficultes rencontrees</h3>

<p><strong>Analyse frequentielle</strong> :</p>
<p>Comprendre le spectre des signaux modules (raies, bandes laterales) demande une bonne maitrise de la transformee de Fourier.</p>

<p><strong>Circuits RF complexes</strong> :</p>
<p>Les architectures superheterodynes avec changements de frequence multiples sont complexes a apprehender.</p>

<p><strong>Oscillateurs</strong> :</p>
<p>Conditions d'oscillation (Barkhausen), stabilite de frequence, bruit de phase sont des concepts subtils.</p>

<hr/>

<h2>PART C - Aspects Techniques Detailles</h2>

<h3 class="section-title">1. Modulation d'amplitude (AM)</h3>

<p><strong>Principe</strong> :</p>
<p>Faire varier l'amplitude d'un signal porteur sinusoidal en fonction du signal d'information (message).</p>

<p>Signal porteur : p(t) = Vp cos(2&pi; fp t)<br/>
Signal modulant (message) : m(t)</p>

<p>Signal module AM : s(t) = Vp [1 + m &times; m(t)] cos(2&pi; fp t)</p>

<p>ou m est l'indice de modulation (0 &lt; m &lt;= 1).</p>

<p><strong>Indice de modulation</strong> :</p>
<p>m = (Vmax - Vmin) / (Vmax + Vmin)</p>
<ul>
<li>Si m &lt; 1 : pas de surmodulation (bon)</li>
<li>Si m &gt; 1 : surmodulation, distorsion (mauvais)</li>
</ul>

<p><strong>Spectre du signal AM</strong> :</p>
<p>Pour un signal modulant sinusoidal m(t) = cos(2&pi; fm t) :</p>
<p>s(t) = Vp cos(2&pi; fp t) + (m Vp / 2) cos(2&pi; (fp + fm) t) + (m Vp / 2) cos(2&pi; (fp - fm) t)</p>

<p>Trois composantes :</p>
<ul>
<li>Porteuse a fp</li>
<li>Bande laterale superieure a fp + fm</li>
<li>Bande laterale inferieure a fp - fm</li>
</ul>

<p><strong>Bande passante</strong> :</p>
<p>BW = 2 &times; fm (frequence max du message)</p>

<p><strong>Efficacite</strong> :</p>
<p>La porteuse ne contient pas d'information utile. Puissance utile seulement dans les bandes laterales.</p>
<p>Rendement energetique = m&sup2; / (2 + m&sup2;)</p>
<p>Pour m = 1 : rendement = 33% (faible !)</p>

<p><strong>Variantes</strong> :</p>
<table>
<tr><th>Type</th><th>Description</th><th>Avantage</th></tr>
<tr><td>AM classique</td><td>Porteuse + 2 BL</td><td>Simple a demoduler</td></tr>
<tr><td>DSB (Double Sideband)</td><td>2 BL sans porteuse</td><td>Meilleur rendement</td></tr>
<tr><td>SSB (Single Sideband)</td><td>1 BL seulement</td><td>Bande passante divisee par 2</td></tr>
</table>

<h3 class="section-title">2. Demodulation AM</h3>

<p><strong>Detection d'enveloppe</strong> :</p>
<p>Methode la plus simple pour demoduler l'AM.</p>

<p>Circuit :</p>
<ul>
<li>Diode (redressement)</li>
<li>Condensateur (filtrage)</li>
<li>Resistance (charge)</li>
</ul>

<p><strong>Principe</strong> :</p>
<p>La diode redresse le signal module. Le condensateur suit l'enveloppe (amplitude variable) du signal.</p>

<p><strong>Dimensionnement</strong> :</p>
<p>Constante de temps RC doit verifier :</p>
<ul>
<li>1/fp &lt;&lt; RC (pour filtrer la porteuse)</li>
<li>RC &lt;&lt; 1/fm (pour suivre les variations du message)</li>
</ul>
<p>Compromis : 1/fp &lt;&lt; RC &lt;&lt; 1/fm</p>

<p><strong>Detection synchrone (demodulation coherente)</strong> :</p>
<p>Multiplier le signal recu par une porteuse synchrone (meme frequence et phase).</p>
<p>Necessite une recuperation de porteuse (PLL).</p>
<p>Plus complexe mais meilleure qualite (fonctionne pour DSB et SSB).</p>

<h3 class="section-title">3. Modulation de frequence (FM)</h3>

<p><strong>Principe</strong> :</p>
<p>Faire varier la frequence de la porteuse proportionnellement au signal modulant.</p>
<p>Frequence instantanee : f(t) = fp + kf &times; m(t)</p>
<p>ou kf est la sensibilite du modulateur (Hz/V).</p>

<p><strong>Deviation de frequence</strong> :</p>
<p>&Delta;f = kf &times; Vm (amplitude max du message)</p>

<p><strong>Indice de modulation</strong> :</p>
<p>&beta; = &Delta;f / fm</p>
<p>ou fm est la frequence du message.</p>

<p><strong>Spectre du signal FM</strong> :</p>
<p>Le spectre contient une infinite de raies (theoriquement) espacees de fm.</p>
<p>Amplitude des raies donnee par les fonctions de Bessel Jn(&beta;).</p>

<p><strong>Bande passante (regle de Carson)</strong> :</p>
<p>BW = 2 (&Delta;f + fm) = 2 fm (&beta; + 1)</p>
<p>Pour &beta; &gt;&gt; 1 (large bande) : BW &asymp; 2 &Delta;f<br/>
Pour &beta; &lt;&lt; 1 (bande etroite) : BW &asymp; 2 fm</p>

<p><strong>FM large bande vs bande etroite</strong> :</p>
<table>
<tr><th>Type</th><th>&beta;</th><th>Bande</th><th>Application</th></tr>
<tr><td>NBFM</td><td>&lt; 0,5</td><td>2 fm</td><td>Communications radio professionnelles</td></tr>
<tr><td>WBFM</td><td>&gt; 1</td><td>2 &Delta;f</td><td>Radio FM broadcast (88-108 MHz)</td></tr>
</table>

<p><strong>Avantages de la FM</strong> :</p>
<ul>
<li>Immunite au bruit d'amplitude</li>
<li>Meilleure qualite audio</li>
<li>Capture effect (signal fort capture le recepteur)</li>
</ul>

<p><strong>Inconvenient</strong> :</p>
<p>Bande passante plus large que l'AM.</p>

<h3 class="section-title">4. Demodulation FM</h3>

<p><strong>Discriminateur de frequence</strong> :</p>
<p>Convertit les variations de frequence en variations d'amplitude, puis detection d'enveloppe.</p>

<p><strong>Principe</strong> :</p>
<ul>
<li>Circuit derivateur ou reseau dephaseur</li>
<li>Transforme la FM en AM</li>
<li>Detection d'enveloppe classique</li>
</ul>

<p><strong>Demodulateur a PLL</strong> :</p>
<p>Utilise une boucle a verrouillage de phase (PLL) qui suit la frequence instantanee.</p>
<p>La tension de commande du VCO (dans la PLL) est proportionnelle a la frequence d'entree : c'est le signal demodule.</p>

<p><strong>Avantage</strong> :</p>
<ul>
<li>Meilleure linearite</li>
<li>Moins sensible au bruit</li>
</ul>

<h3 class="section-title">5. Oscillateurs</h3>

<p><strong>Definition</strong> :</p>
<p>Circuit qui genere un signal periodique (sinusoidal ou carre) sans signal d'entree.</p>

<p><strong>Condition d'oscillation (critere de Barkhausen)</strong> :</p>
<p>Pour un oscillateur boucle (amplificateur + reseau de retroaction) :</p>
<p>Boucle ouverte : H(j&omega;) = A(j&omega;) &times; &Beta;(j&omega;)</p>
<p>Conditions pour oscillation a &omega;0 :</p>
<ol>
<li>|H(j&omega;0)| = 1 (gain de boucle = 1)</li>
<li>arg(H(j&omega;0)) = 0&deg; ou 360&deg; (dephasage de boucle multiple de 360&deg;)</li>
</ol>

<p><strong>Demarrage des oscillations</strong> :</p>
<p>En pratique, on assure |H| legerement &gt; 1 au demarrage pour que les oscillations s'amorcent (a partir du bruit).</p>
<p>Puis un mecanisme de limitation d'amplitude (saturation, compression) stabilise l'amplitude.</p>

<p><strong>Types d'oscillateurs</strong> :</p>

<p><strong>Oscillateurs RC</strong> :</p>
<p>Reseau de dephasage (3 cellules RC) + amplificateur.</p>
<p>Frequence : f &asymp; 1 / (2&pi; RC &radic;6)</p>
<p>Avantage : composants simples<br/>
Inconvenient : stabilite moyenne</p>

<p><strong>Oscillateurs LC</strong> :</p>
<p>Utilise un circuit resonant LC pour definir la frequence.</p>
<p>Frequence : f0 = 1 / (2&pi; &radic;(LC))</p>

<p><strong>Oscillateur Colpitts</strong> :</p>
<p>Resonateur LC avec prise capacitive (2 condensateurs en serie).</p>
<p>Tres utilise en RF pour sa stabilite.</p>

<p><strong>Oscillateur Clapp</strong> :</p>
<p>Variante du Colpitts avec condensateur serie dans l'inductance.</p>
<p>Meilleure stabilite en frequence.</p>

<p><strong>Oscillateurs a quartz</strong> :</p>
<p>Utilise un cristal de quartz comme resonateur.</p>

<p><strong>Avantages</strong> :</p>
<ul>
<li>Tres haute stabilite en frequence (ppm)</li>
<li>Facteur de qualite Q tres eleve (10^4 a 10^6)</li>
</ul>

<p><strong>Applications</strong> :</p>
<ul>
<li>Horloges (montres, microcontroleurs)</li>
<li>Bases de temps precises</li>
<li>References de frequence</li>
</ul>

<p><strong>Frequences standards</strong> :</p>
<ul>
<li>32,768 kHz (horlogerie)</li>
<li>10 MHz (reference laboratoire)</li>
<li>Quelques MHz a quelques dizaines de MHz (electronique)</li>
</ul>

<h3 class="section-title">6. Multiplieurs analogiques</h3>

<p><strong>Definition</strong> :</p>
<p>Circuit qui realise la multiplication de deux signaux : Vout = k &times; V1 &times; V2</p>

<p><strong>Applications</strong> :</p>
<table>
<tr><th>Application</th><th>Description</th></tr>
<tr><td>Modulation</td><td>Multiplier porteuse &times; message</td></tr>
<tr><td>Demodulation</td><td>Multiplier signal recu &times; porteuse locale</td></tr>
<tr><td>Melangeur (mixer)</td><td>Transposition de frequence</td></tr>
<tr><td>Detecteur de phase</td><td>Comparaison de phase dans PLL</td></tr>
<tr><td>Controle automatique de gain</td><td>Multiplication par tension de controle</td></tr>
<tr><td>Puissance</td><td>Calcul V &times; I</td></tr>
</table>

<p><strong>Types de multiplieurs</strong> :</p>

<p><strong>Multiplicateur 4 quadrants</strong> :</p>
<p>V1 et V2 peuvent etre positifs ou negatifs.</p>
<p>Multiplication complete : Vout = k V1 V2</p>

<p><strong>Multiplicateur 2 quadrants</strong> :</p>
<p>Un signal bipolaire, l'autre unipolaire.</p>

<p><strong>Multiplicateur 1 quadrant</strong> :</p>
<p>Les deux signaux unipolaires (positifs seulement).</p>

<p><strong>Exemple de circuit : cellule de Gilbert</strong> :</p>
<p>Circuit a transistors (BJT ou MOS) qui realise une multiplication.</p>
<p>Base de nombreux multiplieurs integres (AD633, AD834, etc.).</p>

<p><strong>Modulation par multiplieur</strong> :</p>
<p>AM : s(t) = [Vdc + m(t)] &times; cos(&omega;p t)</p>
<p>Le signal modulant est additionne a une composante continue avant multiplication avec la porteuse.</p>

<p><strong>Transposition de frequence (melangeur)</strong> :</p>
<p>Multiplier deux signaux sinusoidaux :</p>
<p>V1 = A cos(&omega;1 t)<br/>
V2 = B cos(&omega;2 t)</p>
<p>Resultat :</p>
<p>Vout = (AB/2) [cos((&omega;1 - &omega;2) t) + cos((&omega;1 + &omega;2) t)]</p>
<p>Deux nouvelles frequences : somme et difference.</p>
<p>Application : changement de frequence dans recepteurs (superheterodyne).</p>

<h3 class="section-title">7. Architectures de recepteurs</h3>

<p><strong>Recepteur superheterodyne</strong> :</p>
<p>Architecture classique utilisee dans la majorite des recepteurs radio.</p>

<p><strong>Principe</strong> :</p>
<p>Transposer le signal RF recu vers une frequence intermediaire fixe (FI) ou le traitement est plus facile.</p>

<p><strong>Blocs fonctionnels</strong> :</p>
<ol>
<li><strong>Antenne</strong> : reception du signal RF</li>
<li><strong>Filtre RF</strong> : selection de la bande (rejet des frequences indesirables)</li>
<li><strong>Amplificateur RF (LNA)</strong> : amplification faible bruit</li>
<li><strong>Melangeur</strong> : transposition RF &rarr; FI</li>
<li><strong>Oscillateur local (OL)</strong> : generation de la frequence de transposition</li>
<li><strong>Filtre FI</strong> : selectivite du canal (bande passante etroite)</li>
<li><strong>Amplificateur FI</strong> : gain principal du recepteur</li>
<li><strong>Demodulateur</strong> : extraction du signal d'information</li>
<li><strong>Amplificateur audio/video</strong> : amplification du signal demodule</li>
</ol>

<p><strong>Frequence intermediaire</strong> :</p>
<p>f_FI = |f_RF - f_OL|</p>
<p>Choix typique de FI :</p>
<ul>
<li>AM broadcast : 455 kHz ou 10,7 MHz</li>
<li>FM broadcast : 10,7 MHz</li>
<li>TV : 36-45 MHz</li>
</ul>

<p><strong>Avantages du superheterodyne</strong> :</p>
<ul>
<li>Selectivite elevee (filtre FI fixe, bien optimise)</li>
<li>Gain eleve stable (amplification a FI fixe)</li>
<li>Facilite de reglage (varier seulement f_OL)</li>
</ul>

<p><strong>Probleme de l'image</strong> :</p>
<p>Deux frequences RF peuvent donner la meme FI :</p>
<ul>
<li>f_RF = f_OL + f_FI (signal desire)</li>
<li>f_image = f_OL - f_FI (image indesirable)</li>
</ul>
<p>La frequence image est a 2 &times; f_FI du signal desire.</p>

<p><strong>Solution</strong> :</p>
<p>Filtre RF qui rejette la frequence image avant le melangeur.</p>

<p><strong>Double changement de frequence</strong> :</p>
<p>Pour ameliorer le rejet de l'image et la selectivite, on peut utiliser deux FI successives.</p>
<p>RF &rarr; FI1 (elevee) &rarr; FI2 (basse) &rarr; demodulation</p>
<p>Exemple : FI1 = 10,7 MHz, FI2 = 455 kHz</p>

<h3 class="section-title">8. Boucle a verrouillage de phase (PLL)</h3>

<p><strong>Principe</strong> :</p>
<p>Systeme boucle qui asservit la phase (et donc la frequence) d'un oscillateur local sur un signal de reference.</p>

<p><strong>Blocs</strong> :</p>
<ol>
<li><strong>Comparateur de phase</strong> : compare la phase du signal d'entree et du VCO</li>
<li><strong>Filtre de boucle</strong> : filtre passe-bas (integrateur)</li>
<li><strong>VCO</strong> (Voltage Controlled Oscillator) : oscillateur commande en tension</li>
</ol>

<p><strong>Fonctionnement</strong> :</p>
<ul>
<li>Si phase VCO en retard : tension de commande augmente &rarr; frequence VCO augmente</li>
<li>Si phase VCO en avance : tension de commande diminue &rarr; frequence VCO diminue</li>
</ul>

<p><strong>En regime verrouille</strong> :</p>
<p>Le VCO suit exactement la frequence et la phase de l'entree.</p>

<p><strong>Applications</strong> :</p>
<table>
<tr><th>Application</th><th>Description</th></tr>
<tr><td>Synthese de frequence</td><td>Generer des frequences precises et programmables</td></tr>
<tr><td>Demodulation FM</td><td>La tension de commande du VCO est le signal demodule</td></tr>
<tr><td>Recuperation de porteuse</td><td>Extraire la porteuse d'un signal module</td></tr>
<tr><td>Recuperation d'horloge</td><td>Synchronisation dans transmissions numeriques</td></tr>
<tr><td>Multiplication de frequence</td><td>Avec diviseur dans la boucle</td></tr>
</table>

<p><strong>Synthetiseur de frequence</strong> :</p>
<p>PLL avec diviseur de frequence dans la boucle de retour.</p>
<p>f_VCO = N &times; f_ref</p>
<p>En variant N (diviseur programmable), on genere differentes frequences multiples de f_ref.</p>

<p><strong>Exemple</strong> :</p>
<ul>
<li>f_ref = 10 kHz (quartz stable)</li>
<li>N variable de 8800 a 10800</li>
<li>f_VCO variable de 88 MHz a 108 MHz (bande FM)</li>
</ul>
<p>Resolution : 10 kHz (pas entre canaux)</p>

<h3 class="section-title">9. Circuits specifiques</h3>

<p><strong>Redresseur sans seuil</strong> :</p>
<p>Redresseur utilisant un AOP pour compenser la chute de tension de la diode (0,6-0,7 V).</p>
<p>Permet de redresser des signaux de faible amplitude (quelques mV).</p>

<p><strong>Circuit</strong> :</p>
<ul>
<li>AOP en boucle fermee avec diode</li>
<li>La contre-reaction compense le seuil de la diode</li>
</ul>

<p><strong>Resistance negative</strong> :</p>
<p>Circuit actif (avec AOP ou transistor) qui presente une resistance negative.</p>

<p><strong>Application</strong> :</p>
<p>Compenser les pertes dans un circuit RLC pour maintenir les oscillations.</p>
<p>Circuit RLC + resistance negative = oscillateur.</p>

<p><strong>Convertisseur tension-frequence (VCO)</strong> :</p>
<p>Circuit dont la frequence de sortie est proportionnelle a la tension d'entree.</p>
<p>f_out = k &times; V_in</p>

<p><strong>Types</strong> :</p>
<ul>
<li>VCO LC (inductance-capacite variable, varicap)</li>
<li>VCO RC (multivibrateur avec temps de charge variable)</li>
<li>VCO integre (4046, 566, etc.)</li>
</ul>

<p><strong>Applications</strong> :</p>
<ul>
<li>Modulation FM (V_in = signal modulant)</li>
<li>PLL (oscillateur commande)</li>
<li>Conversion analogique-numerique</li>
</ul>

<h3 class="section-title">10. Performances et specifications</h3>

<p><strong>Sensibilite</strong> :</p>
<p>Signal minimum detectable par le recepteur.</p>
<p>Limitee par le bruit (thermique + composants).</p>
<p>Sensibilite (dBm) = Plancher de bruit + SNR minimum</p>

<p><strong>Figure de bruit (Noise Figure - NF)</strong> :</p>
<p>Mesure la degradation du rapport signal sur bruit due au recepteur.</p>
<p>NF (dB) = SNR_entree (dB) - SNR_sortie (dB)</p>
<p>Pour des etages en cascade (formule de Friis) :</p>
<p>NF_total = NF1 + (NF2 - 1)/G1 + (NF3 - 1)/(G1 &times; G2) + ...</p>
<p>Importance du premier etage (LNA) : doit avoir faible NF et gain eleve.</p>

<p><strong>Selectivite</strong> :</p>
<p>Capacite a separer le canal desire des canaux adjacents.</p>
<p>Definie par la bande passante du filtre FI.</p>

<p><strong>Dynamique</strong> :</p>
<p>Plage entre signal minimum (sensibilite) et signal maximum (saturation/intermodulation).</p>

<p><strong>Gain</strong> :</p>
<p>Amplification totale du recepteur.</p>
<p>Typiquement 60-120 dB, reparti sur plusieurs etages.</p>

<p><strong>Controle automatique de gain (AGC)</strong> :</p>
<p>Circuit qui ajuste automatiquement le gain pour maintenir un niveau de sortie constant malgre les variations du signal d'entree.</p>
<p>Evite la saturation sur signaux forts et maintient SNR sur signaux faibles.</p>

<hr/>

<h2>PART D - Analyse Reflexive et Perspectives</h2>

<h3 class="section-title">Competences acquises</h3>

<p><strong>Conception de chaines RF</strong> :</p>
<p>Comprehension des architectures completes d'emission et reception. Capacite a dimensionner chaque etage et analyser les performances globales.</p>

<p><strong>Modulation/demodulation</strong> :</p>
<p>Maitrise des techniques AM et FM, calculs de spectres, choix de parametres (indice de modulation, deviation).</p>

<p><strong>Circuits RF</strong> :</p>
<p>Conception d'oscillateurs, multiplieurs, melangeurs. Comprehension des conditions d'oscillation et stabilite.</p>

<h3 class="section-title">Points cles a retenir</h3>

<p><strong>1. Superheterodyne = architecture dominante</strong> :</p>
<p>La transposition vers FI est la solution standard depuis des decennies. Simple, efficace, eprouvee.</p>

<p><strong>2. Compromis bande/qualite</strong> :</p>
<p>AM : bande etroite mais qualite moyenne. FM : bande large mais meilleure qualite et immunite au bruit.</p>

<p><strong>3. Oscillateurs : stabilite cruciale</strong> :</p>
<p>La stabilite de frequence des oscillateurs determine la qualite du systeme. Quartz pour haute stabilite.</p>

<p><strong>4. Bruit : limitation fondamentale</strong> :</p>
<p>Le bruit thermique et le bruit des composants limitent la sensibilite. Le premier etage (LNA) est critique.</p>

<p><strong>5. PLL : outil polyvalent</strong> :</p>
<p>La PLL est utilisee partout : synthese de frequence, demodulation, recuperation de synchronisation.</p>

<h3 class="section-title">Applications pratiques</h3>

<p><strong>Radio FM/AM</strong> :</p>
<p>Les recepteurs radio classiques utilisent l'architecture superheterodyne enseignee dans ce cours.</p>

<p><strong>Telecommunications sans fil</strong> :</p>
<p>GSM, WiFi, Bluetooth utilisent des architectures derivees (souvent avec conversion numerique apres la FI).</p>

<p><strong>Instrumentation</strong> :</p>
<p>Analyseurs de spectre, generateurs de signaux emploient les techniques de modulation et melange.</p>

<p><strong>Systemes embarques IoT</strong> :</p>
<p>Modules radio courte portee (LoRa, Sigfox, ZigBee) bases sur ces principes.</p>

<h3 class="section-title">Retour d'experience</h3>

<p><strong>Cours riche et pratique</strong> :</p>
<p>Le cours couvre beaucoup d'aspects des systemes RF. Les TD permettent de consolider avec des calculs concrets.</p>

<p><strong>Documents techniques utiles</strong> :</p>
<p>Les application notes (ADI, oscillateurs a quartz) apportent une vision industrielle et pratique.</p>

<p><strong>Annales bien corrigees</strong> :</p>
<p>Les corrections detaillees des examens 2018-2019 et 2021-2022 aident beaucoup a la preparation.</p>

<p><strong>Lien theorie/pratique</strong> :</p>
<p>Le cours fait bien le lien entre la theorie (analyse spectrale, conditions d'oscillation) et les circuits reels.</p>

<h3 class="section-title">Limites et ouvertures</h3>

<p><strong>Limites du module</strong> :</p>
<ul>
<li>Peu de TP pratiques (mesures RF)</li>
<li>Modulations numeriques non traitees (QPSK, QAM, etc.)</li>
<li>Aspects propagation et antennes limites</li>
</ul>

<p><strong>Ouvertures vers</strong> :</p>
<ul>
<li><strong>Communications numeriques</strong> : modulations numeriques, codage canal</li>
<li><strong>RF avancee</strong> : architectures Zero-IF, SDR (Software Defined Radio)</li>
<li><strong>Systemes MIMO</strong> : diversite spatiale, beamforming</li>
<li><strong>5G/6G</strong> : bandes mmWave, massive MIMO</li>
<li><strong>IoT</strong> : protocoles radio basse consommation (LoRa, NB-IoT)</li>
</ul>

<h3 class="section-title">Evolution technologique</h3>

<p><strong>Tendances actuelles</strong> :</p>

<p><strong>SDR (Software Defined Radio)</strong> :</p>
<p>Numerisation le plus tot possible dans la chaine, traitement en DSP. Flexibilite maximale.</p>

<p><strong>Integration</strong> :</p>
<p>SoC RF integrant toute la chaine sur une puce (emetteur, recepteur, DSP, processeur).</p>

<p><strong>Bandes mmWave</strong> :</p>
<p>5G utilise 24-40 GHz. Defis : attenuation, conception RF complexe.</p>

<p><strong>Efficacite energetique</strong> :</p>
<p>IoT necessite des radios ultra-basse consommation (&mu;W en veille, mW en emission).</p>

<h3 class="section-title">Conseils pour reussir</h3>

<p><strong>1. Maitriser les bases</strong> :</p>
<p>Bien comprendre modulation AM/FM, spectres, bande passante avant d'attaquer les architectures.</p>

<p><strong>2. Faire les TD</strong> :</p>
<p>Les 5 TD avec corrections sont essentiels. Refaire sans regarder les corrections.</p>

<p><strong>3. Etudier les annales</strong> :</p>
<p>Les examens 2018-2019 et 2021-2022 donnent le format et le niveau attendus.</p>

<p><strong>4. Comprendre les schemas</strong> :</p>
<p>Savoir lire et analyser les schemas blocs des chaines RF (identifier chaque fonction).</p>

<p><strong>5. Ordre de grandeur</strong> :</p>
<p>Connaitre les valeurs typiques (FI, frequences radio, gains, NF).</p>

<h3 class="section-title">Conclusion</h3>

<p>Ce cours fournit une excellente base en architectures RF analogiques. Meme si la tendance est a la numerisation (SDR), la chaine RF analogique (antenne &rarr; LNA &rarr; melangeur &rarr; ADC) reste incontournable.</p>

<p><strong>Complementarite</strong> :</p>
<p>Ce cours s'articule bien avec les cours de traitement numerique du signal et de communications numeriques pour une vision complete des telecommunications.</p>

<p><strong>Pertinence professionnelle</strong> :</p>
<p>Les competences acquises sont directement applicables dans l'industrie des telecommunications, de l'IoT, et de l'instrumentation RF.</p>

<p><strong>Message principal</strong> :</p>
<p>Comprendre les architectures RF analogiques est fondamental pour tout ingenieur en electronique et telecommunications. C'est la base sur laquelle reposent tous les systemes sans fil modernes.</p>

<p><strong>Recommandations</strong> :</p>
<ul>
<li>Approfondir avec des simulations (ADS, LTspice pour RF)</li>
<li>Pratiquer avec des kits RF (modules SDR, analyseurs de spectre)</li>
<li>Explorer les datasheets de circuits integres RF (emetteurs-recepteurs)</li>
<li>Se former aux communications numeriques en complement</li>
</ul>

<p><strong>Liens avec les autres cours</strong> :</p>
<ul>
<li><a href="./electronique-fonctions-analogiques.html">Electronique Fonctions Analogiques - S6</a> : AOPs, filtres</li>
<li><a href="./signal.html">Signal - S5</a> : transformee de Fourier, modulation</li>
<li><a href="./embedded-ia-iot.html">Embedded IA for IoT - S9</a> : systemes communicants</li>
</ul>

<hr/>

<h2>Documents de Cours</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Cours Complet</h4>
      <p>Cours complet sur les architectures RF : oscillateurs, PLL, melangeurs, modulation/demodulation AM et FM.</p>
      <embed src="/cours-pdf/S7/Archi-Analogiques-Transmission/cours-complet.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Archi-Analogiques-Transmission/cours-complet.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>Modulation et Demodulation FM</h4>
      <p>Cours detaille sur la modulation de frequence : VCO, discriminateurs, detecteurs de phase et applications.</p>
      <embed src="/cours-pdf/S7/Archi-Analogiques-Transmission/modulation-fm.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Archi-Analogiques-Transmission/modulation-fm.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>Recueil TDs</h4>
      <p>Ensemble des travaux diriges avec exercices sur oscillateurs, PLL, melangeurs et chaines RF completes.</p>
      <embed src="/cours-pdf/S7/Archi-Analogiques-Transmission/tds.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Archi-Analogiques-Transmission/tds.pdf" target="_blank">Telecharger</a></p>
    </div>
  </div>
</div>

<hr/>

<p><em>Cours suivi en 2023-2024 a l'INSA Toulouse, Departement Genie Electrique et Informatique.</em></p>

</div>

<div class="lang-en">

<h1>Analog Architectures for Information Transmission - Semester 7</h1>

<p><strong>Academic Year</strong>: 2023-2024<br/>
<strong>Semester</strong>: 7<br/>
<strong>Credits</strong>: 2.5 ECTS<br/>
<strong>Specialization</strong>: Analog and RF Electronics</p>

<hr/>

<h2>PART A - General Module Presentation</h2>

<h3 class="section-title">Overview</h3>

<p>This course covers analog architectures for information transmission, focusing on modulation/demodulation systems and radio-frequency (RF) transmit/receive chains. It covers analog modulation techniques (AM, FM), oscillators, multipliers, and receiver architectures.</p>

<p><strong>Learning Objectives</strong>:</p>
<ul>
<li>Master analog modulation and demodulation techniques</li>
<li>Understand RF chain architectures (transmission and reception)</li>
<li>Design oscillators and frequency synthesis circuits</li>
<li>Analyze transmission system performance (noise, linearity)</li>
<li>Size circuits for radio applications</li>
</ul>

<h3 class="section-title">Position in the Curriculum</h3>

<p>This module builds upon:</p>
<ul>
<li><strong>Analog Function Electronics (S6)</strong>: Op-amps, active filters</li>
<li><strong>Signal Processing (S5)</strong>: modulation, Fourier transform</li>
<li><strong>Analog Circuits and Filters (S5)</strong>: filters, impedance matching</li>
</ul>

<p>It prepares for:</p>
<ul>
<li><strong>Telecommunications</strong>: RF system design</li>
<li><strong>Communicating embedded systems</strong>: IoT, short-range radio</li>
<li><strong>RF Instrumentation</strong>: generators, analyzers</li>
</ul>

<hr/>

<h2>PART B - Personal Experience and Learning Context</h2>

<h3 class="section-title">Organization and Resources</h3>

<p>The module was organized into lectures and tutorials:</p>

<p><strong>Lectures (20h)</strong>:</p>
<p>Covering the main topics:</p>
<ul>
<li>AM/FM modulation and demodulation</li>
<li>Oscillators (theory and applications)</li>
<li>Analog multipliers</li>
<li>Receiver architectures (superheterodyne)</li>
<li>Phase-locked loops (PLL)</li>
</ul>

<p><strong>Tutorials (16h)</strong>:</p>
<p>5 tutorials with solutions available:</p>
<ul>
<li>TD1 to TD5: application exercises on modulation, oscillators, multipliers</li>
</ul>

<p><strong>Teaching materials</strong>:</p>
<ul>
<li>Main course document (ArchiUF_2022-2023.pdf)</li>
<li>Oscillator course notes (Notes-cours-Theorie-Osc.pdf)</li>
<li>Technical documents (ADI multipliers, quartz oscillators)</li>
<li>Past exams 2018-2019, 2021-2022 with solutions</li>
</ul>

<h3 class="section-title">Resource Content</h3>

<p><strong>Available technical documents</strong>:</p>
<ul>
<li><strong>Multipliers</strong>: ADI Multiplier Applications Guide, 1 to 4 quadrant multipliers</li>
<li><strong>Oscillators</strong>: theory, quartz oscillators (AN3208)</li>
<li><strong>FM Modulation</strong>: FM modulation and demodulation</li>
<li><strong>Detection</strong>: demodulation by envelope detection</li>
<li><strong>Specific circuits</strong>: RLC with negative resistance, threshold-free rectifier</li>
</ul>

<h3 class="section-title">Working Method</h3>

<p><strong>Theoretical course</strong>:</p>
<p>Many schematics and circuit analyses. Understanding the operating principles of modulators, demodulators, and oscillators.</p>

<p><strong>Practical tutorials</strong>:</p>
<p>Performance calculations (modulation index, frequency deviation, gain, noise). Component sizing.</p>

<p><strong>Past exams</strong>:</p>
<p>2018-2019 and 2021-2022 exams with solutions for practice.</p>

<h3 class="section-title">Difficulties Encountered</h3>

<p><strong>Frequency analysis</strong>:</p>
<p>Understanding the spectrum of modulated signals (spectral lines, sidebands) requires good mastery of the Fourier transform.</p>

<p><strong>Complex RF circuits</strong>:</p>
<p>Superheterodyne architectures with multiple frequency conversions are complex to grasp.</p>

<p><strong>Oscillators</strong>:</p>
<p>Oscillation conditions (Barkhausen), frequency stability, and phase noise are subtle concepts.</p>

<hr/>

<h2>PART C - Detailed Technical Aspects</h2>

<h3 class="section-title">1. Amplitude Modulation (AM)</h3>

<p><strong>Principle</strong>:</p>
<p>Vary the amplitude of a sinusoidal carrier signal according to the information signal (message).</p>

<p>Carrier signal: p(t) = Vp cos(2&pi; fp t)<br/>
Modulating signal (message): m(t)</p>

<p>AM modulated signal: s(t) = Vp [1 + m &times; m(t)] cos(2&pi; fp t)</p>

<p>where m is the modulation index (0 &lt; m &lt;= 1).</p>

<p><strong>Modulation index</strong>:</p>
<p>m = (Vmax - Vmin) / (Vmax + Vmin)</p>
<ul>
<li>If m &lt; 1: no overmodulation (good)</li>
<li>If m &gt; 1: overmodulation, distortion (bad)</li>
</ul>

<p><strong>AM signal spectrum</strong>:</p>
<p>For a sinusoidal modulating signal m(t) = cos(2&pi; fm t):</p>
<p>s(t) = Vp cos(2&pi; fp t) + (m Vp / 2) cos(2&pi; (fp + fm) t) + (m Vp / 2) cos(2&pi; (fp - fm) t)</p>

<p>Three components:</p>
<ul>
<li>Carrier at fp</li>
<li>Upper sideband at fp + fm</li>
<li>Lower sideband at fp - fm</li>
</ul>

<p><strong>Bandwidth</strong>:</p>
<p>BW = 2 &times; fm (max frequency of the message)</p>

<p><strong>Efficiency</strong>:</p>
<p>The carrier contains no useful information. Useful power is only in the sidebands.</p>
<p>Energy efficiency = m&sup2; / (2 + m&sup2;)</p>
<p>For m = 1: efficiency = 33% (low!)</p>

<p><strong>Variants</strong>:</p>
<table>
<tr><th>Type</th><th>Description</th><th>Advantage</th></tr>
<tr><td>Classic AM</td><td>Carrier + 2 sidebands</td><td>Simple to demodulate</td></tr>
<tr><td>DSB (Double Sideband)</td><td>2 sidebands without carrier</td><td>Better efficiency</td></tr>
<tr><td>SSB (Single Sideband)</td><td>1 sideband only</td><td>Bandwidth halved</td></tr>
</table>

<h3 class="section-title">2. AM Demodulation</h3>

<p><strong>Envelope detection</strong>:</p>
<p>Simplest method to demodulate AM.</p>

<p>Circuit:</p>
<ul>
<li>Diode (rectification)</li>
<li>Capacitor (filtering)</li>
<li>Resistor (load)</li>
</ul>

<p><strong>Principle</strong>:</p>
<p>The diode rectifies the modulated signal. The capacitor follows the envelope (varying amplitude) of the signal.</p>

<p><strong>Sizing</strong>:</p>
<p>The RC time constant must satisfy:</p>
<ul>
<li>1/fp &lt;&lt; RC (to filter the carrier)</li>
<li>RC &lt;&lt; 1/fm (to follow message variations)</li>
</ul>
<p>Compromise: 1/fp &lt;&lt; RC &lt;&lt; 1/fm</p>

<p><strong>Synchronous detection (coherent demodulation)</strong>:</p>
<p>Multiply the received signal by a synchronous carrier (same frequency and phase).</p>
<p>Requires carrier recovery (PLL).</p>
<p>More complex but better quality (works for DSB and SSB).</p>

<h3 class="section-title">3. Frequency Modulation (FM)</h3>

<p><strong>Principle</strong>:</p>
<p>Vary the carrier frequency proportionally to the modulating signal.</p>
<p>Instantaneous frequency: f(t) = fp + kf &times; m(t)</p>
<p>where kf is the modulator sensitivity (Hz/V).</p>

<p><strong>Frequency deviation</strong>:</p>
<p>&Delta;f = kf &times; Vm (max amplitude of the message)</p>

<p><strong>Modulation index</strong>:</p>
<p>&beta; = &Delta;f / fm</p>
<p>where fm is the message frequency.</p>

<p><strong>FM signal spectrum</strong>:</p>
<p>The spectrum contains an infinite number of spectral lines (theoretically) spaced by fm.</p>
<p>Line amplitudes given by Bessel functions Jn(&beta;).</p>

<p><strong>Bandwidth (Carson's rule)</strong>:</p>
<p>BW = 2 (&Delta;f + fm) = 2 fm (&beta; + 1)</p>
<p>For &beta; &gt;&gt; 1 (wideband): BW &asymp; 2 &Delta;f<br/>
For &beta; &lt;&lt; 1 (narrowband): BW &asymp; 2 fm</p>

<p><strong>Wideband FM vs narrowband FM</strong>:</p>
<table>
<tr><th>Type</th><th>&beta;</th><th>Bandwidth</th><th>Application</th></tr>
<tr><td>NBFM</td><td>&lt; 0.5</td><td>2 fm</td><td>Professional radio communications</td></tr>
<tr><td>WBFM</td><td>&gt; 1</td><td>2 &Delta;f</td><td>FM broadcast radio (88-108 MHz)</td></tr>
</table>

<p><strong>Advantages of FM</strong>:</p>
<ul>
<li>Immunity to amplitude noise</li>
<li>Better audio quality</li>
<li>Capture effect (strong signal captures the receiver)</li>
</ul>

<p><strong>Disadvantage</strong>:</p>
<p>Wider bandwidth than AM.</p>

<h3 class="section-title">4. FM Demodulation</h3>

<p><strong>Frequency discriminator</strong>:</p>
<p>Converts frequency variations into amplitude variations, then envelope detection.</p>

<p><strong>Principle</strong>:</p>
<ul>
<li>Differentiator circuit or phase-shifting network</li>
<li>Transforms FM into AM</li>
<li>Classic envelope detection</li>
</ul>

<p><strong>PLL demodulator</strong>:</p>
<p>Uses a phase-locked loop (PLL) that tracks the instantaneous frequency.</p>
<p>The VCO control voltage (in the PLL) is proportional to the input frequency: this is the demodulated signal.</p>

<p><strong>Advantage</strong>:</p>
<ul>
<li>Better linearity</li>
<li>Less sensitive to noise</li>
</ul>

<h3 class="section-title">5. Oscillators</h3>

<p><strong>Definition</strong>:</p>
<p>Circuit that generates a periodic signal (sinusoidal or square) without an input signal.</p>

<p><strong>Oscillation condition (Barkhausen criterion)</strong>:</p>
<p>For a feedback oscillator (amplifier + feedback network):</p>
<p>Open loop: H(j&omega;) = A(j&omega;) &times; &Beta;(j&omega;)</p>
<p>Conditions for oscillation at &omega;0:</p>
<ol>
<li>|H(j&omega;0)| = 1 (loop gain = 1)</li>
<li>arg(H(j&omega;0)) = 0&deg; or 360&deg; (loop phase shift multiple of 360&deg;)</li>
</ol>

<p><strong>Oscillation startup</strong>:</p>
<p>In practice, |H| is set slightly &gt; 1 at startup so that oscillations begin (from noise).</p>
<p>Then an amplitude limiting mechanism (saturation, compression) stabilizes the amplitude.</p>

<p><strong>Types of oscillators</strong>:</p>

<p><strong>RC Oscillators</strong>:</p>
<p>Phase-shift network (3 RC cells) + amplifier.</p>
<p>Frequency: f &asymp; 1 / (2&pi; RC &radic;6)</p>
<p>Advantage: simple components<br/>
Disadvantage: average stability</p>

<p><strong>LC Oscillators</strong>:</p>
<p>Uses a resonant LC circuit to set the frequency.</p>
<p>Frequency: f0 = 1 / (2&pi; &radic;(LC))</p>

<p><strong>Colpitts Oscillator</strong>:</p>
<p>LC resonator with capacitive tap (2 series capacitors).</p>
<p>Widely used in RF for its stability.</p>

<p><strong>Clapp Oscillator</strong>:</p>
<p>Colpitts variant with series capacitor in the inductor.</p>
<p>Better frequency stability.</p>

<p><strong>Crystal Oscillators</strong>:</p>
<p>Uses a quartz crystal as a resonator.</p>

<p><strong>Advantages</strong>:</p>
<ul>
<li>Very high frequency stability (ppm)</li>
<li>Very high quality factor Q (10^4 to 10^6)</li>
</ul>

<p><strong>Applications</strong>:</p>
<ul>
<li>Clocks (watches, microcontrollers)</li>
<li>Precise time bases</li>
<li>Frequency references</li>
</ul>

<p><strong>Standard frequencies</strong>:</p>
<ul>
<li>32.768 kHz (timekeeping)</li>
<li>10 MHz (laboratory reference)</li>
<li>A few MHz to tens of MHz (electronics)</li>
</ul>

<h3 class="section-title">6. Analog Multipliers</h3>

<p><strong>Definition</strong>:</p>
<p>Circuit that performs multiplication of two signals: Vout = k &times; V1 &times; V2</p>

<p><strong>Applications</strong>:</p>
<table>
<tr><th>Application</th><th>Description</th></tr>
<tr><td>Modulation</td><td>Multiply carrier &times; message</td></tr>
<tr><td>Demodulation</td><td>Multiply received signal &times; local carrier</td></tr>
<tr><td>Mixer</td><td>Frequency transposition</td></tr>
<tr><td>Phase detector</td><td>Phase comparison in PLL</td></tr>
<tr><td>Automatic gain control</td><td>Multiplication by control voltage</td></tr>
<tr><td>Power</td><td>V &times; I calculation</td></tr>
</table>

<p><strong>Types of multipliers</strong>:</p>

<p><strong>4-quadrant multiplier</strong>:</p>
<p>V1 and V2 can be positive or negative.</p>
<p>Full multiplication: Vout = k V1 V2</p>

<p><strong>2-quadrant multiplier</strong>:</p>
<p>One bipolar signal, the other unipolar.</p>

<p><strong>1-quadrant multiplier</strong>:</p>
<p>Both signals unipolar (positive only).</p>

<p><strong>Example circuit: Gilbert cell</strong>:</p>
<p>Transistor circuit (BJT or MOS) that performs multiplication.</p>
<p>Basis for many integrated multipliers (AD633, AD834, etc.).</p>

<p><strong>Modulation by multiplier</strong>:</p>
<p>AM: s(t) = [Vdc + m(t)] &times; cos(&omega;p t)</p>
<p>The modulating signal is added to a DC component before multiplication with the carrier.</p>

<p><strong>Frequency transposition (mixer)</strong>:</p>
<p>Multiply two sinusoidal signals:</p>
<p>V1 = A cos(&omega;1 t)<br/>
V2 = B cos(&omega;2 t)</p>
<p>Result:</p>
<p>Vout = (AB/2) [cos((&omega;1 - &omega;2) t) + cos((&omega;1 + &omega;2) t)]</p>
<p>Two new frequencies: sum and difference.</p>
<p>Application: frequency conversion in receivers (superheterodyne).</p>

<h3 class="section-title">7. Receiver Architectures</h3>

<p><strong>Superheterodyne receiver</strong>:</p>
<p>Classic architecture used in the majority of radio receivers.</p>

<p><strong>Principle</strong>:</p>
<p>Transpose the received RF signal to a fixed intermediate frequency (IF) where processing is easier.</p>

<p><strong>Functional blocks</strong>:</p>
<ol>
<li><strong>Antenna</strong>: RF signal reception</li>
<li><strong>RF Filter</strong>: band selection (rejection of unwanted frequencies)</li>
<li><strong>RF Amplifier (LNA)</strong>: low-noise amplification</li>
<li><strong>Mixer</strong>: RF &rarr; IF transposition</li>
<li><strong>Local Oscillator (LO)</strong>: transposition frequency generation</li>
<li><strong>IF Filter</strong>: channel selectivity (narrow bandwidth)</li>
<li><strong>IF Amplifier</strong>: main receiver gain</li>
<li><strong>Demodulator</strong>: information signal extraction</li>
<li><strong>Audio/Video Amplifier</strong>: demodulated signal amplification</li>
</ol>

<p><strong>Intermediate frequency</strong>:</p>
<p>f_IF = |f_RF - f_LO|</p>
<p>Typical IF choices:</p>
<ul>
<li>AM broadcast: 455 kHz or 10.7 MHz</li>
<li>FM broadcast: 10.7 MHz</li>
<li>TV: 36-45 MHz</li>
</ul>

<p><strong>Superheterodyne advantages</strong>:</p>
<ul>
<li>High selectivity (fixed IF filter, well optimized)</li>
<li>High stable gain (amplification at fixed IF)</li>
<li>Easy tuning (only vary f_LO)</li>
</ul>

<p><strong>Image problem</strong>:</p>
<p>Two RF frequencies can produce the same IF:</p>
<ul>
<li>f_RF = f_LO + f_IF (desired signal)</li>
<li>f_image = f_LO - f_IF (unwanted image)</li>
</ul>
<p>The image frequency is 2 &times; f_IF from the desired signal.</p>

<p><strong>Solution</strong>:</p>
<p>RF filter that rejects the image frequency before the mixer.</p>

<p><strong>Dual frequency conversion</strong>:</p>
<p>To improve image rejection and selectivity, two successive IFs can be used.</p>
<p>RF &rarr; IF1 (high) &rarr; IF2 (low) &rarr; demodulation</p>
<p>Example: IF1 = 10.7 MHz, IF2 = 455 kHz</p>

<h3 class="section-title">8. Phase-Locked Loop (PLL)</h3>

<p><strong>Principle</strong>:</p>
<p>Feedback system that locks the phase (and therefore frequency) of a local oscillator to a reference signal.</p>

<p><strong>Blocks</strong>:</p>
<ol>
<li><strong>Phase comparator</strong>: compares the phase of the input signal and the VCO</li>
<li><strong>Loop filter</strong>: low-pass filter (integrator)</li>
<li><strong>VCO</strong> (Voltage Controlled Oscillator): voltage-controlled oscillator</li>
</ol>

<p><strong>Operation</strong>:</p>
<ul>
<li>If VCO phase lags: control voltage increases &rarr; VCO frequency increases</li>
<li>If VCO phase leads: control voltage decreases &rarr; VCO frequency decreases</li>
</ul>

<p><strong>In locked state</strong>:</p>
<p>The VCO exactly follows the input frequency and phase.</p>

<p><strong>Applications</strong>:</p>
<table>
<tr><th>Application</th><th>Description</th></tr>
<tr><td>Frequency synthesis</td><td>Generate precise and programmable frequencies</td></tr>
<tr><td>FM demodulation</td><td>The VCO control voltage is the demodulated signal</td></tr>
<tr><td>Carrier recovery</td><td>Extract the carrier from a modulated signal</td></tr>
<tr><td>Clock recovery</td><td>Synchronization in digital transmissions</td></tr>
<tr><td>Frequency multiplication</td><td>With divider in the loop</td></tr>
</table>

<p><strong>Frequency synthesizer</strong>:</p>
<p>PLL with frequency divider in the feedback loop.</p>
<p>f_VCO = N &times; f_ref</p>
<p>By varying N (programmable divider), different frequencies that are multiples of f_ref are generated.</p>

<p><strong>Example</strong>:</p>
<ul>
<li>f_ref = 10 kHz (stable quartz)</li>
<li>N variable from 8800 to 10800</li>
<li>f_VCO variable from 88 MHz to 108 MHz (FM band)</li>
</ul>
<p>Resolution: 10 kHz (channel spacing)</p>

<h3 class="section-title">9. Specific Circuits</h3>

<p><strong>Threshold-free rectifier</strong>:</p>
<p>Rectifier using an op-amp to compensate the diode voltage drop (0.6-0.7 V).</p>
<p>Allows rectification of low-amplitude signals (a few mV).</p>

<p><strong>Circuit</strong>:</p>
<ul>
<li>Op-amp in closed loop with diode</li>
<li>Feedback compensates the diode threshold</li>
</ul>

<p><strong>Negative resistance</strong>:</p>
<p>Active circuit (with op-amp or transistor) that presents a negative resistance.</p>

<p><strong>Application</strong>:</p>
<p>Compensate losses in an RLC circuit to maintain oscillations.</p>
<p>RLC circuit + negative resistance = oscillator.</p>

<p><strong>Voltage-to-frequency converter (VCO)</strong>:</p>
<p>Circuit whose output frequency is proportional to the input voltage.</p>
<p>f_out = k &times; V_in</p>

<p><strong>Types</strong>:</p>
<ul>
<li>LC VCO (variable inductance-capacitance, varicap)</li>
<li>RC VCO (multivibrator with variable charge time)</li>
<li>Integrated VCO (4046, 566, etc.)</li>
</ul>

<p><strong>Applications</strong>:</p>
<ul>
<li>FM modulation (V_in = modulating signal)</li>
<li>PLL (controlled oscillator)</li>
<li>Analog-to-digital conversion</li>
</ul>

<h3 class="section-title">10. Performance and Specifications</h3>

<p><strong>Sensitivity</strong>:</p>
<p>Minimum detectable signal by the receiver.</p>
<p>Limited by noise (thermal + component).</p>
<p>Sensitivity (dBm) = Noise floor + minimum SNR</p>

<p><strong>Noise Figure (NF)</strong>:</p>
<p>Measures the signal-to-noise ratio degradation due to the receiver.</p>
<p>NF (dB) = SNR_input (dB) - SNR_output (dB)</p>
<p>For cascaded stages (Friis formula):</p>
<p>NF_total = NF1 + (NF2 - 1)/G1 + (NF3 - 1)/(G1 &times; G2) + ...</p>
<p>Importance of the first stage (LNA): must have low NF and high gain.</p>

<p><strong>Selectivity</strong>:</p>
<p>Ability to separate the desired channel from adjacent channels.</p>
<p>Defined by the IF filter bandwidth.</p>

<p><strong>Dynamic range</strong>:</p>
<p>Range between minimum signal (sensitivity) and maximum signal (saturation/intermodulation).</p>

<p><strong>Gain</strong>:</p>
<p>Total receiver amplification.</p>
<p>Typically 60-120 dB, distributed across several stages.</p>

<p><strong>Automatic Gain Control (AGC)</strong>:</p>
<p>Circuit that automatically adjusts gain to maintain a constant output level despite input signal variations.</p>
<p>Prevents saturation on strong signals and maintains SNR on weak signals.</p>

<hr/>

<h2>PART D - Reflective Analysis and Perspectives</h2>

<h3 class="section-title">Skills Acquired</h3>

<p><strong>RF chain design</strong>:</p>
<p>Understanding complete transmit and receive architectures. Ability to size each stage and analyze overall performance.</p>

<p><strong>Modulation/demodulation</strong>:</p>
<p>Mastery of AM and FM techniques, spectrum calculations, parameter selection (modulation index, deviation).</p>

<p><strong>RF circuits</strong>:</p>
<p>Design of oscillators, multipliers, mixers. Understanding oscillation conditions and stability.</p>

<h3 class="section-title">Key Takeaways</h3>

<p><strong>1. Superheterodyne = dominant architecture</strong>:</p>
<p>IF transposition has been the standard solution for decades. Simple, efficient, proven.</p>

<p><strong>2. Bandwidth/quality trade-off</strong>:</p>
<p>AM: narrow bandwidth but average quality. FM: wide bandwidth but better quality and noise immunity.</p>

<p><strong>3. Oscillators: stability is crucial</strong>:</p>
<p>Oscillator frequency stability determines system quality. Crystal for high stability.</p>

<p><strong>4. Noise: fundamental limitation</strong>:</p>
<p>Thermal noise and component noise limit sensitivity. The first stage (LNA) is critical.</p>

<p><strong>5. PLL: versatile tool</strong>:</p>
<p>PLL is used everywhere: frequency synthesis, demodulation, synchronization recovery.</p>

<h3 class="section-title">Practical Applications</h3>

<p><strong>FM/AM Radio</strong>:</p>
<p>Classic radio receivers use the superheterodyne architecture taught in this course.</p>

<p><strong>Wireless telecommunications</strong>:</p>
<p>GSM, WiFi, Bluetooth use derived architectures (often with digital conversion after the IF).</p>

<p><strong>Instrumentation</strong>:</p>
<p>Spectrum analyzers, signal generators employ modulation and mixing techniques.</p>

<p><strong>IoT embedded systems</strong>:</p>
<p>Short-range radio modules (LoRa, Sigfox, ZigBee) based on these principles.</p>

<h3 class="section-title">Feedback</h3>

<p><strong>Rich and practical course</strong>:</p>
<p>The course covers many aspects of RF systems. Tutorials help consolidate with concrete calculations.</p>

<p><strong>Useful technical documents</strong>:</p>
<p>Application notes (ADI, quartz oscillators) provide an industrial and practical perspective.</p>

<p><strong>Well-corrected past exams</strong>:</p>
<p>Detailed solutions for the 2018-2019 and 2021-2022 exams greatly help with preparation.</p>

<p><strong>Theory/practice link</strong>:</p>
<p>The course effectively connects theory (spectral analysis, oscillation conditions) with real circuits.</p>

<h3 class="section-title">Limitations and Openings</h3>

<p><strong>Module limitations</strong>:</p>
<ul>
<li>Few practical labs (RF measurements)</li>
<li>Digital modulations not covered (QPSK, QAM, etc.)</li>
<li>Limited propagation and antenna aspects</li>
</ul>

<p><strong>Openings towards</strong>:</p>
<ul>
<li><strong>Digital communications</strong>: digital modulations, channel coding</li>
<li><strong>Advanced RF</strong>: Zero-IF architectures, SDR (Software Defined Radio)</li>
<li><strong>MIMO systems</strong>: spatial diversity, beamforming</li>
<li><strong>5G/6G</strong>: mmWave bands, massive MIMO</li>
<li><strong>IoT</strong>: low-power radio protocols (LoRa, NB-IoT)</li>
</ul>

<h3 class="section-title">Technological Evolution</h3>

<p><strong>Current trends</strong>:</p>

<p><strong>SDR (Software Defined Radio)</strong>:</p>
<p>Digitization as early as possible in the chain, DSP processing. Maximum flexibility.</p>

<p><strong>Integration</strong>:</p>
<p>RF SoC integrating the entire chain on a chip (transmitter, receiver, DSP, processor).</p>

<p><strong>mmWave bands</strong>:</p>
<p>5G uses 24-40 GHz. Challenges: attenuation, complex RF design.</p>

<p><strong>Energy efficiency</strong>:</p>
<p>IoT requires ultra-low power radios (&mu;W in sleep, mW in transmission).</p>

<h3 class="section-title">Tips for Success</h3>

<p><strong>1. Master the basics</strong>:</p>
<p>Thoroughly understand AM/FM modulation, spectra, bandwidth before tackling architectures.</p>

<p><strong>2. Do the tutorials</strong>:</p>
<p>The 5 tutorials with solutions are essential. Redo them without looking at the solutions.</p>

<p><strong>3. Study past exams</strong>:</p>
<p>The 2018-2019 and 2021-2022 exams show the expected format and level.</p>

<p><strong>4. Understand the schematics</strong>:</p>
<p>Know how to read and analyze RF chain block diagrams (identify each function).</p>

<p><strong>5. Orders of magnitude</strong>:</p>
<p>Know typical values (IF, radio frequencies, gains, NF).</p>

<h3 class="section-title">Conclusion</h3>

<p>This course provides an excellent foundation in analog RF architectures. Even though the trend is towards digitization (SDR), the analog RF chain (antenna &rarr; LNA &rarr; mixer &rarr; ADC) remains essential.</p>

<p><strong>Complementarity</strong>:</p>
<p>This course integrates well with digital signal processing and digital communications courses for a complete view of telecommunications.</p>

<p><strong>Professional relevance</strong>:</p>
<p>The skills acquired are directly applicable in the telecommunications, IoT, and RF instrumentation industries.</p>

<p><strong>Main message</strong>:</p>
<p>Understanding analog RF architectures is fundamental for any electronics and telecommunications engineer. It is the foundation on which all modern wireless systems are built.</p>

<p><strong>Recommendations</strong>:</p>
<ul>
<li>Deepen knowledge with simulations (ADS, LTspice for RF)</li>
<li>Practice with RF kits (SDR modules, spectrum analyzers)</li>
<li>Explore RF integrated circuit datasheets (transceivers)</li>
<li>Train in digital communications as a complement</li>
</ul>

<p><strong>Links with other courses</strong>:</p>
<ul>
<li><a href="./electronique-fonctions-analogiques.html">Analog Function Electronics - S6</a>: Op-amps, filters</li>
<li><a href="./signal.html">Signal Processing - S5</a>: Fourier transform, modulation</li>
<li><a href="./embedded-ia-iot.html">Embedded AI for IoT - S9</a>: communicating systems</li>
</ul>

<hr/>

<h2>Course Documents</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Complete Course</h4>
      <p>Complete course on RF architectures: oscillators, PLL, mixers, AM and FM modulation/demodulation.</p>
      <embed src="/cours-pdf/S7/Archi-Analogiques-Transmission/cours-complet.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Archi-Analogiques-Transmission/cours-complet.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>FM Modulation and Demodulation</h4>
      <p>Detailed course on frequency modulation: VCO, discriminators, phase detectors and applications.</p>
      <embed src="/cours-pdf/S7/Archi-Analogiques-Transmission/modulation-fm.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Archi-Analogiques-Transmission/modulation-fm.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>Tutorial Collection</h4>
      <p>Complete set of tutorials with exercises on oscillators, PLL, mixers and complete RF chains.</p>
      <embed src="/cours-pdf/S7/Archi-Analogiques-Transmission/tds.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Archi-Analogiques-Transmission/tds.pdf" target="_blank">Download</a></p>
    </div>
  </div>
</div>

<hr/>

<p><em>Course taken in 2023-2024 at INSA Toulouse, Department of Electrical Engineering and Computer Science.</em></p>

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

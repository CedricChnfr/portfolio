---
layout: default
title: "🔐 Sécurité Matérielle - Semestre 7"
date: 2024-10-02 10:56:03 +0200
---

<style>
.back-nav {
    margin: 20px 0;
    padding: 10px;
    background-color: #f0f0f0;
    border-radius: 5px;
}

.back-nav a {
    color: #007BFF;
    text-decoration: none;
    font-weight: bold;
}

.back-nav a:hover {
    text-decoration: underline;
}

.section-title {
    color: #007BFF;
    border-bottom: 2px solid #007BFF;
    padding-bottom: 5px;
    margin-top: 20px;
}

table {
    border-collapse: collapse;
    width: 100%;
    margin: 20px 0;
}

th, td {
    border: 1px solid #ddd;
    padding: 12px;
    text-align: left;
}

th {
    background-color: #007BFF;
    color: white;
}

tr:nth-child(even) {
    background-color: #f2f2f2;
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
    <a href="./my-courses-2023-2024.html" data-i18n-html="back-courses-2023-2024">&larr; Retour aux Cours 2023-2024</a>
</div>

<div class="lang-fr">

<h1>Securite Materielle - Semestre 7</h1>

<p><strong>Annee academique</strong> : 2023-2024<br/>
<strong>ECTS</strong> : 2<br/>
<strong>Categorie</strong> : Securite et Systemes Embarques</p>

<hr/>

<h2>PART A - Presentation Generale du Module</h2>

<h3 class="section-title">Vue d'ensemble</h3>

<p>Ce cours aborde la securite materielle, un domaine essentiel a l'ere des objets connectes et des systemes embarques. Il couvre les vulnerabilites physiques des systemes electroniques, les attaques par canaux auxiliaires, les mecanismes de protection, et les techniques de conception securisee pour prevenir l'extraction d'informations sensibles.</p>

<p><strong>Objectifs pedagogiques</strong> :</p>
<ul>
<li>Comprendre les menaces pesant sur la securite materielle</li>
<li>Maitriser les attaques par canaux auxiliaires (timing, cache, puissance)</li>
<li>Analyser les vulnerabilites des implementations cryptographiques</li>
<li>Decouvrir les attaques par depassement de tampon et injection de code</li>
<li>Implementer des contre-mesures efficaces</li>
<li>Evaluer la securite physique des systemes embarques</li>
</ul>

<h3 class="section-title">Position dans le cursus</h3>

<p>Ce module complete la formation en securite :</p>
<ul>
<li><strong>Architecture Materielle (S6)</strong> : fonctionnement processeurs, caches, memoires</li>
<li><strong>Microcontroleurs (S6)</strong> : systemes embarques, ARM Cortex</li>
<li><strong>Systemes d'Exploitation (S5)</strong> : gestion memoire, processus</li>
<li><strong>Langage C et Assemblage (S5, S6)</strong> : programmation bas niveau</li>
</ul>

<p>Il prepare a :</p>
<ul>
<li><strong>Embedded IA for IoT (S9)</strong> : securite des objets connectes</li>
<li><strong>Projets professionnels</strong> : conception de systemes securises</li>
<li><strong>Cybersecurite</strong> : approche globale hardware/software</li>
</ul>

<hr/>

<h2>PART B - Experience Personnelle et Contexte d'Apprentissage</h2>

<h3 class="section-title">Organisation et ressources</h3>

<p>Le module etait organise en cours magistraux et travaux pratiques intensifs :</p>

<p><strong>Cours magistraux (12h)</strong> :</p>
<ul>
<li>Introduction a la securite materielle</li>
<li>Attaques par canaux auxiliaires (timing, cache, puissance)</li>
<li>Analyse de la consommation electrique (SPA, DPA, CPA)</li>
<li>Attaques par injection de fautes</li>
<li>Vulnerabilites logicielles (buffer overflow, shellcode)</li>
<li>Contre-mesures materielles et logicielles</li>
</ul>

<p><strong>Travaux pratiques (12h)</strong> :</p>
<ul>
<li><strong>TP1</strong> : Analyse de consommation sur microcontroleur STM32</li>
<li><strong>TP Cache et SCA</strong> : Attaques par analyse de cache, detection d'ouverture de fichiers</li>
<li><strong>TP3 Overflow</strong> : Exploitation de depassements de tampon, shellcode, injection de code</li>
<li><strong>TP AES</strong> : Analyse de vulnerabilites dans implementations OpenSSL</li>
</ul>

<p><strong>Ressources</strong> :</p>
<ul>
<li>6 polycopies de cours (slides, polycopies detailles)</li>
<li>2 TD avec corrections</li>
<li>Outils : ChipWhisperer (analyse de puissance), GDB (debogage)</li>
<li>Code source AES (OpenSSL versions 0.9.7a et 1.1.1t)</li>
<li>Annales (4 sujets d'examens)</li>
</ul>

<h3 class="section-title">Methodologie d'etude</h3>

<p><strong>Phase 1 : Assimiler les concepts theoriques</strong> :</p>
<p>Comprendre les principes des attaques (canaux auxiliaires, injection de fautes, overflow).</p>

<p><strong>Phase 2 : Manipuler en TP</strong> :</p>
<p>Realiser les attaques concretes pour comprendre leur fonctionnement et leur puissance.</p>

<p><strong>Phase 3 : Analyser le code</strong> :</p>
<p>Etudier le code vulnerable (AES, programmes C) pour identifier les failles.</p>

<p><strong>Phase 4 : Concevoir des contre-mesures</strong> :</p>
<p>Reflechir aux protections possibles et a leurs limites.</p>

<p><strong>Phase 5 : Developper une vision critique</strong> :</p>
<p>Evaluer la securite globale d'un systeme en considerant tous les vecteurs d'attaque.</p>

<h3 class="section-title">Difficultes rencontrees</h3>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S7/securite-materielle/buffer-overflow.svg" alt="Attaque par buffer overflow" style="max-width: 550px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Principe d'une attaque par buffer overflow - Ecrasement de l'adresse de retour</p>
</div>

<p><strong>Complexite des attaques</strong> :</p>
<p>Les attaques par canaux auxiliaires necessitent des connaissances en electronique, traitement du signal, et statistiques.</p>

<p><strong>Environnement technique</strong> :</p>
<p>Manipuler des outils specialises (ChipWhisperer, oscilloscopes) et du code assembleur requiert de la pratique.</p>

<p><strong>Equilibre securite/performance</strong> :</p>
<p>Concevoir des contre-mesures efficaces sans degrader les performances est un defi constant.</p>

<p><strong>Diversite des vulnerabilites</strong> :</p>
<p>La securite materielle couvre un spectre large : du cache au depassement de tampon, chaque domaine a ses specificites.</p>

<hr/>

<h2>PART C - Aspects Techniques Detailles</h2>

<h3 class="section-title">1. Attaques par canaux auxiliaires</h3>

<p><strong>Principe general</strong> :</p>

<p>Les attaques par canaux auxiliaires exploitent les fuites d'information physiques lors de l'execution d'algorithmes :</p>
<ul>
<li>Consommation electrique</li>
<li>Temps d'execution</li>
<li>Emissions electromagnetiques</li>
<li>Contenu du cache</li>
</ul>

<p>Meme si l'algorithme est mathematiquement sur, son implementation peut reveler des secrets.</p>

<p><strong>Attaques temporelles (Timing Attacks)</strong> :</p>

<p>Exploitent les variations du temps d'execution.</p>

<p><strong>Exemple classique : Cache timing sur AES</strong> :</p>

<p>AES utilise des tables de substitution (S-box). L'acces a ces tables depend de la cle et du message.</p>

<p>Si une partie de la table est en cache (acces rapide) et une autre non (acces lent), on peut deduire quelle partie a ete accedee en mesurant le temps.</p>

<p><strong>Attaque</strong> :</p>
<ol>
<li>Mesurer le temps d'execution pour differents messages</li>
<li>Analyser les variations temporelles</li>
<li>Deduire quelle partie de la S-box a ete accedee</li>
<li>Recuperer progressivement les octets de la cle</li>
</ol>

<p><strong>Contre-mesures</strong> :</p>
<ul>
<li>Implementations a temps constant (meme duree quel que soit l'input)</li>
<li>Desactivation du cache pour operations sensibles</li>
<li>Ajout de bruit temporel (jitter)</li>
</ul>

<p><strong>Attaques par analyse de cache</strong> :</p>

<p>Le cache CPU peut reveler des informations sensibles.</p>

<p><strong>Technique Prime+Probe</strong> :</p>
<ol>
<li>Attaquant remplit le cache avec ses propres donnees (Prime)</li>
<li>Victime execute operation cryptographique</li>
<li>Attaquant mesure quelles lignes de cache ont ete evincees (Probe)</li>
<li>En deduire les acces memoire de la victime</li>
</ol>

<p><strong>TP realise : Detection d'ouverture de fichier</strong> :</p>

<p>Programme spy.c :</p>
<ul>
<li>Vide (flush) le cache pour une adresse du fichier cible</li>
<li>Attend un delai</li>
<li>Mesure le temps d'acces a cette adresse</li>
<li>Si temps &lt; seuil : fichier en cache &rarr; fichier a ete ouvert recemment</li>
</ul>

<p>Application : espionnage d'activite sans acces systeme.</p>

<p><strong>Attaques par analyse de la consommation (Power Analysis)</strong> :</p>

<p><strong>Simple Power Analysis (SPA)</strong> :</p>

<p>Observation directe de la trace de consommation.</p>

<p>Chaque instruction consomme differemment : multiplication, addition, lecture memoire ont des signatures distinctes.</p>

<p><strong>Exemple</strong> : Exponentiation modulaire en RSA :</p>
<ul>
<li>Operation "carre" visible</li>
<li>Operation "carre puis multiplication" visible</li>
<li>On deduit directement les bits de la cle privee</li>
</ul>

<p><strong>Differential Power Analysis (DPA)</strong> :</p>

<p>Analyse statistique sur de nombreuses traces.</p>

<p>Principe :</p>
<ol>
<li>Capturer N traces de consommation pour N messages differents</li>
<li>Faire des hypotheses sur une partie de la cle</li>
<li>Predire la consommation pour chaque hypothese</li>
<li>Correler predictions avec traces reelles</li>
<li>L'hypothese correcte donne la meilleure correlation</li>
</ol>

<p><strong>Correlation Power Analysis (CPA)</strong> :</p>

<p>Variante amelioree utilisant le coefficient de correlation de Pearson.</p>

<p>Permet d'attaquer des implementations plus resistantes.</p>

<p><strong>TP realise : Analyse de consommation sur STM32</strong> :</p>

<p>Programme main.c (TP1) :</p>
<ul>
<li>Microcontroleur execute des operations (multiplications repetees)</li>
<li>Oscilloscope capture la consommation electrique</li>
<li>Analyse des traces pour identifier les operations</li>
<li>Correlation entre donnees manipulees et consommation</li>
</ul>

<h3 class="section-title">2. Attaques par injection de fautes</h3>

<p><strong>Principe</strong> :</p>

<p>Provoquer volontairement des erreurs lors de l'execution pour obtenir des informations ou contourner des protections.</p>

<p><strong>Techniques d'injection</strong> :</p>

<table>
<tr><th>Technique</th><th>Description</th><th>Effet</th></tr>
<tr><td>Clock glitching</td><td>Impulsions sur horloge</td><td>Instructions sautees</td></tr>
<tr><td>Voltage glitching</td><td>Variation tension alimentation</td><td>Erreurs calcul</td></tr>
<tr><td>Laser</td><td>Faisceau laser focalise</td><td>Modification bit memoire</td></tr>
<tr><td>Temperature</td><td>Chauffage/refroidissement</td><td>Instabilites</td></tr>
<tr><td>EM</td><td>Impulsion electromagnetique</td><td>Perturbation circuits</td></tr>
</table>

<p><strong>Exemple : Attaque sur authentification</strong> :</p>

<p>Code vulnerable :</p>
<pre><code>if (password == correct_password) {
    grant_access();
} else {
    deny_access();
}</code></pre>

<p>Injection de faute au moment du test :</p>
<ul>
<li>Le test echoue (mauvais mot de passe)</li>
<li>Mais la faute inverse le resultat &rarr; acces accorde</li>
</ul>

<p><strong>Contre-mesures</strong> :</p>
<ul>
<li>Redondance (double verification)</li>
<li>Codes correcteurs d'erreurs</li>
<li>Detecteurs de glitches (capteurs de tension/horloge)</li>
<li>Verifications de coherence</li>
</ul>

<h3 class="section-title">3. Vulnerabilites logicielles : Buffer Overflow</h3>

<p><strong>Principe</strong> :</p>

<p>Depassement de tampon : ecrire au-dela de la taille allouee d'un buffer, ecrasant des donnees adjacentes (adresse de retour, variables).</p>

<p><strong>Mecanisme sur la pile (stack)</strong> :</p>

<p>Organisation de la pile lors d'un appel de fonction :</p>
<pre><code>[parametres]
[adresse de retour]
[ancien ebp]
[variables locales]
[buffer]</code></pre>

<p>Si on ecrit trop dans buffer, on ecrase les variables, ebp, et l'adresse de retour.</p>

<p><strong>Exploitation</strong> :</p>

<ol>
<li>Remplir le buffer avec du code malveillant (shellcode)</li>
<li>Ecraser l'adresse de retour pour pointer vers le shellcode</li>
<li>Quand la fonction retourne, le shellcode s'execute</li>
</ol>

<p><strong>TP realise : Exploitation de buffer overflow</strong> :</p>

<p><strong>Part 1 : Organisation memoire</strong> :</p>
<p>Analyse de la pile avec GDB, calcul des offsets.</p>

<p><strong>Part 2 : Exploitation simple</strong> :</p>
<p>Programme vulnerable avec strcpy sans verification de taille. Injection pour modifier une variable ou sauter une verification.</p>

<p><strong>Part 3 : Injection de shellcode</strong> :</p>

<p>shellcode.c :</p>
<pre><code>void shellcode() {
  asm(
    "mov $0x3b, %rax"    // syscall execve
    "mov $0x0, %rdx"
    "movabs $0x0068732f6e69622f, %r8"  // "/bin/sh"
    "push %r8"
    "mov %rsp, %rdi"     // adresse de "/bin/sh"
    "syscall"            // execve("/bin/sh", ...)
  );
}</code></pre>

<p>Objectif : injecter ce code et rediriger l'execution pour ouvrir un shell.</p>

<p><strong>Part 4 &amp; 5 : Exploitation complete</strong> :</p>
<ul>
<li>Calcul de l'adresse du shellcode</li>
<li>Construction du payload (NOP sled + shellcode + adresse retour)</li>
<li>Injection via upload.py</li>
<li>Obtention d'un shell avec privileges</li>
</ul>

<p><strong>Contre-mesures modernes</strong> :</p>

<table>
<tr><th>Contre-mesure</th><th>Description</th></tr>
<tr><td>Stack canaries</td><td>Valeur sentinelle avant adresse retour, verifiee</td></tr>
<tr><td>ASLR (Address Space Layout Randomization)</td><td>Adresses memoire aleatoires</td></tr>
<tr><td>DEP/NX (Data Execution Prevention)</td><td>Memoire non executable (pile, tas)</td></tr>
<tr><td>RELRO (Relocation Read-Only)</td><td>Sections memoire en lecture seule</td></tr>
<tr><td>Compilation securisee</td><td>Options -fstack-protector, -D_FORTIFY_SOURCE</td></tr>
</table>

<h3 class="section-title">4. Analyse de cache - Profiling</h3>

<p><strong>Hierarchie memoire</strong> :</p>

<p>CPU &rarr; Cache L1 (1-3 cycles) &rarr; Cache L2 (10-20 cycles) &rarr; Cache L3 (40-75 cycles) &rarr; RAM (100-300 cycles)</p>

<p>Le cache accelere l'acces aux donnees frequemment utilisees.</p>

<p><strong>Mesure du temps d'acces</strong> :</p>

<p>TP Cache Profiling (profiling.c) :</p>
<ul>
<li>Fonction memaccesstime(ptr) : mesure le temps pour acceder a une adresse</li>
<li>Fonction clflush(ptr) : vide (flush) l'adresse du cache</li>
<li>Boucle de profiling :
  <ul>
  <li>Acceder &rarr; mesurer (cache hit)</li>
  <li>Flush &rarr; acceder &rarr; mesurer (cache miss)</li>
  </ul>
</li>
<li>Generation d'histogrammes avec gnuplot</li>
</ul>

<p><strong>Resultats typiques</strong> :</p>
<ul>
<li>Cache hit : 10-50 cycles</li>
<li>Cache miss : 200-400 cycles</li>
</ul>

<p><strong>Exploitation pour attaque</strong> :</p>

<p><strong>Technique Flush+Reload</strong> :</p>
<ol>
<li>Flush une ligne de cache partagee avec la victime</li>
<li>Victime execute son code</li>
<li>Attaquant mesure le temps de rechargement</li>
<li>Si rapide : victime a accede a cette ligne</li>
</ol>

<p><strong>Application : Detection d'ouverture de fichier</strong> (spy.c) :</p>
<ul>
<li>Surveiller une adresse d'un fichier sensible</li>
<li>Si le fichier est ouvert par un processus, il sera en cache</li>
<li>Detection sans acces au systeme de fichiers</li>
</ul>

<h3 class="section-title">5. Vulnerabilites cryptographiques - AES</h3>

<p><strong>AES (Advanced Encryption Standard)</strong> :</p>

<p>Algorithme de chiffrement par blocs, standard depuis 2001.</p>

<p><strong>Structure</strong> :</p>
<ul>
<li>Blocs de 128 bits</li>
<li>Cles de 128, 192 ou 256 bits</li>
<li>10, 12 ou 14 rondes selon taille de cle</li>
<li>Operations : SubBytes (S-box), ShiftRows, MixColumns, AddRoundKey</li>
</ul>

<p><strong>Vulnerabilites d'implementation</strong> :</p>

<p><strong>Implementation naive : Acces tables dependant de la cle</strong></p>

<p>AES utilise des tables de substitution (S-box). L'implementation classique stocke ces tables en memoire.</p>

<p>Lors de l'execution :</p>
<pre><code>state[i] = Sbox[state[i] XOR key[i]]</code></pre>

<p>L'indice d'acces depend de la cle : vulnerabilite aux attaques par cache.</p>

<p><strong>TP : Comparaison OpenSSL versions</strong></p>

<p><strong>OpenSSL 0.9.7a (vulnerable)</strong> :</p>
<ul>
<li>Acces direct aux tables T0, T1, T2, T3</li>
<li>Indices dependent des donnees et de la cle</li>
<li>Vulnerable aux cache timing attacks</li>
</ul>

<p><strong>OpenSSL 1.1.1t (protegee)</strong> :</p>
<ul>
<li>Implementation AES-NI (instructions materielles)</li>
<li>Pas d'acces memoire dependant de la cle</li>
<li>Resistant aux cache timing attacks</li>
</ul>

<p><strong>AES-NI</strong> :</p>

<p>Instructions processeur dediees (Intel, AMD depuis 2010) :</p>
<ul>
<li>AESENC, AESENCLAST : chiffrement</li>
<li>AESDEC, AESDECLAST : dechiffrement</li>
<li>AESIMC, AESKEYGENASSIST : generation de cles</li>
</ul>

<p>Avantages :</p>
<ul>
<li>Performance elevee</li>
<li>Implementation resistante aux canaux auxiliaires</li>
<li>Pas de tables en memoire</li>
</ul>

<h3 class="section-title">6. Autres contre-mesures</h3>

<p><strong>Masquage (Masking)</strong> :</p>

<p>Technique contre les attaques DPA.</p>

<p>Principe : Randomiser les valeurs intermediaires.</p>

<p>Au lieu de manipuler directement x, on manipule x XOR m (m aleatoire).</p>

<p>Les fuites de consommation portent sur x XOR m, qui est aleatoire.</p>

<p><strong>Exemple</strong> :</p>
<pre><code>x' = x XOR m
y' = f(x') = f(x XOR m)
y = y' XOR m' (ou m' decoule de m)</code></pre>

<p><strong>Inconvenients</strong> :</p>
<ul>
<li>Surcout en calcul et en aleatoire</li>
<li>Difficile a implementer correctement (fuites possibles)</li>
</ul>

<p><strong>Hiding</strong> :</p>

<p>Reduire le rapport signal/bruit dans les traces de consommation.</p>

<p>Techniques :</p>
<ul>
<li>Randomisation de l'ordre des operations</li>
<li>Insertion d'operations factices (dummy operations)</li>
<li>Consommation constante (circuits a double rail)</li>
</ul>

<p><strong>Securite physique</strong> :</p>

<p><strong>Capteurs</strong> :</p>
<ul>
<li>Detecteurs d'ouverture du boitier</li>
<li>Capteurs de temperature, lumiere</li>
<li>Capteurs de tension/frequence anormales</li>
</ul>

<p><strong>Memoire effacable</strong> :</p>
<p>En cas de detection d'attaque, effacer les cles.</p>

<p><strong>Encapsulation</strong> :</p>
<p>Proteger les circuits sensibles dans des resines difficiles a retirer.</p>

<h3 class="section-title">7. Outils et methodologies</h3>

<p><strong>ChipWhisperer</strong> :</p>

<p>Plateforme open-source pour analyse de canaux auxiliaires.</p>

<p>Fonctionnalites :</p>
<ul>
<li>Capture de traces de consommation electrique</li>
<li>Synchronisation avec cible (trigger)</li>
<li>Analyses DPA, CPA</li>
<li>Injection de glitches (clock, voltage)</li>
</ul>

<p><strong>GDB (GNU Debugger)</strong> :</p>

<p>Utilise pour analyser les programmes vulnerables :</p>
<ul>
<li>Poser des breakpoints</li>
<li>Examiner la pile et les registres</li>
<li>Calculer les offsets pour exploitations</li>
</ul>

<p><strong>Commandes utiles</strong> :</p>
<pre><code>info registers    # etat des registres
x/32x $rsp       # examiner la pile
disassemble      # desassembler une fonction</code></pre>

<p><strong>Gnuplot</strong> :</p>

<p>Visualisation des distributions de temps d'acces (cache hit/miss).</p>

<h3 class="section-title">8. Domaines d'application</h3>

<p><strong>Cartes a puce</strong> :</p>

<p>Cibles privilegiees : paiement, authentification, SIM.</p>
<p>Menaces : clonage, extraction de cles.</p>
<p>Protections : masquage, capteurs, hardware securise.</p>

<p><strong>Systemes embarques critiques</strong> :</p>

<p>Automobile (CAN bus, ECU), aeronautique, medical.</p>
<p>Risques : injection de fautes, reverse engineering.</p>

<p><strong>IoT (Internet of Things)</strong> :</p>

<p>Objets connectes souvent peu proteges.</p>
<p>Attaques possibles : extraction firmware, clonage, botnets.</p>

<p><strong>Infrastructures cloud</strong> :</p>

<p>Attaques par cache entre machines virtuelles (VM).</p>
<p>Risque de fuite d'informations entre locataires (tenants).</p>

<hr/>

<h2>PART D - Analyse Reflexive et Perspectives</h2>

<h3 class="section-title">Competences acquises</h3>

<p><strong>Comprehension des menaces materielles</strong> :</p>
<p>Capacite a identifier les vulnerabilites physiques et logicielles des systemes embarques.</p>

<p><strong>Maitrise des attaques par canaux auxiliaires</strong> :</p>
<p>Aptitude a analyser les fuites d'information (timing, cache, puissance) et a exploiter ces failles.</p>

<p><strong>Exploitation de vulnerabilites logicielles</strong> :</p>
<p>Competence en exploitation de buffer overflow, injection de shellcode, et comprehension des protections modernes.</p>

<p><strong>Conception securisee</strong> :</p>
<p>Developpement de reflexes pour integrer la securite des la conception (secure by design).</p>

<p><strong>Vision d'ensemble</strong> :</p>
<p>Capacite a evaluer la securite globale d'un systeme en considerant hardware, software, et attaques physiques.</p>

<h3 class="section-title">Points cles a retenir</h3>

<p><strong>1. Securite &ne; Cryptographie seule</strong> :</p>
<p>Un algorithme mathematiquement sur peut etre vulnerable si son implementation fuit des informations.</p>

<p><strong>2. Les canaux auxiliaires sont reels</strong> :</p>
<p>Timing, cache, consommation : ces attaques sont pratiques et ont compromis des systemes reels (cartes bancaires, DRM).</p>

<p><strong>3. Defense en profondeur</strong> :</p>
<p>Pas de solution miracle. Combiner plusieurs contre-mesures pour augmenter le cout de l'attaque.</p>

<p><strong>4. Trade-off securite/performance</strong> :</p>
<p>Les protections coutent en performance, energie, et complexite. Trouver le bon equilibre selon le contexte.</p>

<p><strong>5. Evolution constante</strong> :</p>
<p>Nouvelles attaques regulierement decouvertes (Spectre, Meltdown, Rowhammer). Veille technologique indispensable.</p>

<h3 class="section-title">Retour d'experience</h3>

<p><strong>Aspect revelateur</strong> :</p>
<p>Ce cours a ouvert les yeux sur la fragilite des systemes face aux attaques physiques. Voir des attaques theoriques fonctionner en TP est impressionnant.</p>

<p><strong>Difficulte de la securite</strong> :</p>
<p>Concevoir un systeme sur est difficile. Il faut penser comme un attaquant pour identifier toutes les failles possibles.</p>

<p><strong>Outils specialises</strong> :</p>
<p>Manipuler ChipWhisperer, GDB, et analyser des traces demande de la pratique. Les TP ont permis de se familiariser avec ces outils professionnels.</p>

<p><strong>Equilibre necessaire</strong> :</p>
<p>Les contre-mesures ajoutent de la complexite. Il faut evaluer le niveau de menace et adapter la protection.</p>

<h3 class="section-title">Applications pratiques</h3>

<p><strong>Pour ingenieur en securite</strong> :</p>
<ul>
<li>Audit de securite de systemes embarques</li>
<li>Conception de produits resistants aux attaques physiques</li>
<li>Certification securitaire (Common Criteria, FIPS)</li>
</ul>

<p><strong>Pour developpeur embarque</strong> :</p>
<ul>
<li>Ecrire du code resistant aux attaques (timing constant)</li>
<li>Eviter les vulnerabilites classiques (buffer overflow)</li>
<li>Tester la robustesse face aux fautes</li>
</ul>

<p><strong>Pour concepteur hardware</strong> :</p>
<ul>
<li>Integrer des contre-mesures materielles (capteurs, masking)</li>
<li>Choisir des composants securises (TEE, Secure Element)</li>
<li>Evaluer les risques des la phase de design</li>
</ul>

<p><strong>Dans la vie courante</strong> :</p>
<ul>
<li>Comprendre les risques des objets connectes (cameras, serrures)</li>
<li>Evaluer la securite de produits (cartes bancaires, smartphones)</li>
<li>Sensibiliser aux enjeux de cybersecurite</li>
</ul>

<h3 class="section-title">Limites et ouvertures</h3>

<p><strong>Limites du module</strong> :</p>
<ul>
<li>Peu d'approfondissement sur les attaques EM (electromagnetiques)</li>
<li>Pas de manipulation reelle d'injection laser ou voltage glitching</li>
<li>Aspects legaux et ethiques peu abordes</li>
</ul>

<p><strong>Ouvertures vers</strong> :</p>
<ul>
<li><strong>Secure Elements</strong> : HSM, TPM, Trusted Execution Environments (TEE)</li>
<li><strong>Post-Quantum Cryptography</strong> : resistance aux ordinateurs quantiques</li>
<li><strong>Formal Verification</strong> : preuves formelles de securite</li>
<li><strong>Bug Bounty</strong> : recherche ethique de vulnerabilites</li>
</ul>

<h3 class="section-title">Evolutions recentes</h3>

<p><strong>Attaques Spectre et Meltdown (2018)</strong> :</p>

<p>Exploitation de l'execution speculative des processeurs modernes.</p>

<p>Spectre : forcer un programme a reveler ses secrets via le cache.</p>
<p>Meltdown : lire la memoire du noyau depuis l'espace utilisateur.</p>

<p>Impact : tous les processeurs Intel, AMD, ARM concernes.</p>

<p><strong>Rowhammer (2014)</strong> :</p>

<p>Attaque sur memoire DRAM : acces repetes a des lignes de memoire peuvent induire des flips de bits sur lignes adjacentes.</p>

<p>Exploitation : elevation de privileges, evasion de machines virtuelles.</p>

<p><strong>Attaques sur IA embarquee</strong> :</p>

<p>Les reseaux de neurones sont vulnerables :</p>
<ul>
<li>Attaques adversariales (perturbations imperceptibles)</li>
<li>Extraction de modeles par observation</li>
<li>Backdoors dans modeles</li>
</ul>

<p>Enjeu croissant avec l'IA embarquee (reconnaissance vocale, vision).</p>

<p><strong>5G et IoT</strong> :</p>

<p>Explosion du nombre d'objets connectes.</p>
<p>Surface d'attaque considerable.</p>
<p>Besoin de securite legere et efficace energetiquement.</p>

<h3 class="section-title">Conseils pour reussir</h3>

<p><strong>1. Comprendre avant d'exploiter</strong> :</p>
<p>Bien maitriser le fonctionnement normal d'un systeme avant de chercher les failles.</p>

<p><strong>2. Pratiquer les TP serieusement</strong> :</p>
<p>Les manipulations pratiques sont essentielles pour integrer les concepts.</p>

<p><strong>3. Lire le code</strong> :</p>
<p>Analyser le code source (shellcode, AES) pour comprendre les vulnerabilites.</p>

<p><strong>4. Penser en attaquant</strong> :</p>
<p>Adopter la mentalite d'un attaquant : chercher le maillon faible, les hypotheses implicites.</p>

<p><strong>5. Se documenter</strong> :</p>
<p>Lire des articles academiques, des rapports de vulnerabilites (CVE), des blogs de securite.</p>

<p><strong>6. Respecter l'ethique</strong> :</p>
<p>Ne jamais utiliser ces connaissances de maniere illegale. Hacking ethique uniquement.</p>

<h3 class="section-title">Conclusion</h3>

<p>Ce module est fondamental pour toute personne travaillant sur des systemes embarques ou critiques. La securite materielle est souvent negligee au profit de la securite logicielle, mais les attaques physiques sont reelles et efficaces.</p>

<p><strong>Competences transferables</strong> :</p>
<ul>
<li>Analyse critique de la securite d'un systeme</li>
<li>Comprehension profonde du fonctionnement des processeurs et memoires</li>
<li>Capacite a integrer la securite des la conception</li>
<li>Vision multidisciplinaire (hardware, software, cryptographie, physique)</li>
</ul>

<p><strong>Pertinence professionnelle</strong> :</p>
<p>Avec l'explosion de l'IoT, de l'industrie 4.0, et des vehicules autonomes, la securite materielle est un domaine en forte demande. Les ingenieurs formes a ces problematiques sont recherches.</p>

<p><strong>Message principal</strong> :</p>
<p>La securite est un processus, pas un produit. Il faut constamment evaluer, tester, et ameliorer. Un systeme n'est jamais 100% sur, mais on peut augmenter considerablement le cout de l'attaque.</p>

<p><strong>Recommandations</strong> :</p>
<ul>
<li>Approfondir avec des cours avances (Riscure Academy, Coursera)</li>
<li>Suivre les conferences de securite (Black Hat, DEF CON, CHES)</li>
<li>Pratiquer sur des plateformes (Hack The Box, CTF securite hardware)</li>
<li>Rejoindre des communautes (r/ReverseEngineering, forums specialises)</li>
<li>Rester informe des nouvelles vulnerabilites (CVE, bulletins de securite)</li>
</ul>

<p><strong>Liens avec les autres cours</strong> :</p>
<ul>
<li><a href="./architecture-materielle.html">Architecture Materielle - S6</a> : caches, processeurs</li>
<li><a href="./microcontroleur.html">Microcontroleurs - S6</a> : ARM Cortex, systemes embarques</li>
<li><a href="./systemes-exploitation.html">Systemes d'Exploitation - S5</a> : gestion memoire</li>
<li><a href="./langage-c.html">Langage C - S5</a> : programmation bas niveau</li>
<li><a href="./embedded-ia-iot.html">Embedded IA for IoT - S9</a> : securite des objets connectes</li>
</ul>

<hr/>

<h2>Documents de Cours</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Cours Complet</h4>
      <p>Cours complet de securite materielle : attaques par canaux caches, buffer overflow, vulnerabilites Spectre/Meltdown.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S7/Securite-Materielle/cours-complet.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S7/Securite-Materielle/cours-complet.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>Buffer Overflow</h4>
      <p>Cours sur les attaques par depassement de tampon : exploitation, stack smashing, protections et contre-mesures.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S7/Securite-Materielle/buffer-overflow.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S7/Securite-Materielle/buffer-overflow.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>TP Cache Side-Channel Attack</h4>
      <p>Sujet de TP sur les attaques par canaux caches via cache : timing attacks, Flush+Reload et experimentations.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S7/Securite-Materielle/tp-cache-sca.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S7/Securite-Materielle/tp-cache-sca.pdf" target="_blank">Telecharger</a></p>
    </div>
  </div>
</div>

<hr/>

<p><em>Cours suivi en 2023-2024 a l'INSA Toulouse, Departement Genie Electrique et Informatique.</em></p>

</div>

<div class="lang-en">

<h1>Hardware Security - Semester 7</h1>

<p><strong>Academic Year</strong>: 2023-2024<br/>
<strong>ECTS</strong>: 2<br/>
<strong>Category</strong>: Security and Embedded Systems</p>

<hr/>

<h2>PART A - General Module Presentation</h2>

<h3 class="section-title">Overview</h3>

<p>This course addresses hardware security, an essential field in the era of connected objects and embedded systems. It covers the physical vulnerabilities of electronic systems, side-channel attacks, protection mechanisms, and secure design techniques to prevent the extraction of sensitive information.</p>

<p><strong>Learning objectives</strong>:</p>
<ul>
<li>Understand threats to hardware security</li>
<li>Master side-channel attacks (timing, cache, power)</li>
<li>Analyze vulnerabilities in cryptographic implementations</li>
<li>Discover buffer overflow and code injection attacks</li>
<li>Implement effective countermeasures</li>
<li>Evaluate the physical security of embedded systems</li>
</ul>

<h3 class="section-title">Position in the curriculum</h3>

<p>This module complements the security training:</p>
<ul>
<li><strong>Hardware Architecture (S6)</strong>: processor operation, caches, memories</li>
<li><strong>Microcontrollers (S6)</strong>: embedded systems, ARM Cortex</li>
<li><strong>Operating Systems (S5)</strong>: memory management, processes</li>
<li><strong>C Language and Assembly (S5, S6)</strong>: low-level programming</li>
</ul>

<p>It prepares for:</p>
<ul>
<li><strong>Embedded IA for IoT (S9)</strong>: security of connected objects</li>
<li><strong>Professional projects</strong>: design of secure systems</li>
<li><strong>Cybersecurity</strong>: comprehensive hardware/software approach</li>
</ul>

<hr/>

<h2>PART B - Personal Experience and Learning Context</h2>

<h3 class="section-title">Organization and resources</h3>

<p>The module was organized into lectures and intensive practical work sessions:</p>

<p><strong>Lectures (12h)</strong>:</p>
<ul>
<li>Introduction to hardware security</li>
<li>Side-channel attacks (timing, cache, power)</li>
<li>Power consumption analysis (SPA, DPA, CPA)</li>
<li>Fault injection attacks</li>
<li>Software vulnerabilities (buffer overflow, shellcode)</li>
<li>Hardware and software countermeasures</li>
</ul>

<p><strong>Practical work (12h)</strong>:</p>
<ul>
<li><strong>Lab 1</strong>: Power consumption analysis on STM32 microcontroller</li>
<li><strong>Cache and SCA Lab</strong>: Cache analysis attacks, file opening detection</li>
<li><strong>Lab 3 Overflow</strong>: Buffer overflow exploitation, shellcode, code injection</li>
<li><strong>AES Lab</strong>: Vulnerability analysis in OpenSSL implementations</li>
</ul>

<p><strong>Resources</strong>:</p>
<ul>
<li>6 course handouts (slides, detailed handouts)</li>
<li>2 tutorials with corrections</li>
<li>Tools: ChipWhisperer (power analysis), GDB (debugging)</li>
<li>AES source code (OpenSSL versions 0.9.7a and 1.1.1t)</li>
<li>Past exams (4 exam papers)</li>
</ul>

<h3 class="section-title">Study methodology</h3>

<p><strong>Phase 1: Assimilate theoretical concepts</strong>:</p>
<p>Understand the principles of attacks (side channels, fault injection, overflow).</p>

<p><strong>Phase 2: Hands-on lab work</strong>:</p>
<p>Perform concrete attacks to understand how they work and their power.</p>

<p><strong>Phase 3: Analyze code</strong>:</p>
<p>Study vulnerable code (AES, C programs) to identify flaws.</p>

<p><strong>Phase 4: Design countermeasures</strong>:</p>
<p>Think about possible protections and their limitations.</p>

<p><strong>Phase 5: Develop critical thinking</strong>:</p>
<p>Evaluate the overall security of a system by considering all attack vectors.</p>

<h3 class="section-title">Difficulties encountered</h3>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S7/securite-materielle/buffer-overflow.svg" alt="Buffer overflow attack" style="max-width: 550px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Principle of a buffer overflow attack - Overwriting the return address</p>
</div>

<p><strong>Attack complexity</strong>:</p>
<p>Side-channel attacks require knowledge of electronics, signal processing, and statistics.</p>

<p><strong>Technical environment</strong>:</p>
<p>Handling specialized tools (ChipWhisperer, oscilloscopes) and assembly code requires practice.</p>

<p><strong>Security/performance balance</strong>:</p>
<p>Designing effective countermeasures without degrading performance is a constant challenge.</p>

<p><strong>Diversity of vulnerabilities</strong>:</p>
<p>Hardware security covers a broad spectrum: from cache to buffer overflow, each domain has its own specificities.</p>

<hr/>

<h2>PART C - Detailed Technical Aspects</h2>

<h3 class="section-title">1. Side-channel attacks</h3>

<p><strong>General principle</strong>:</p>

<p>Side-channel attacks exploit physical information leaks during algorithm execution:</p>
<ul>
<li>Power consumption</li>
<li>Execution time</li>
<li>Electromagnetic emissions</li>
<li>Cache contents</li>
</ul>

<p>Even if the algorithm is mathematically secure, its implementation can reveal secrets.</p>

<p><strong>Timing Attacks</strong>:</p>

<p>Exploit variations in execution time.</p>

<p><strong>Classic example: Cache timing on AES</strong>:</p>

<p>AES uses substitution tables (S-box). Access to these tables depends on the key and the message.</p>

<p>If part of the table is in cache (fast access) and another part is not (slow access), one can deduce which part was accessed by measuring the time.</p>

<p><strong>Attack</strong>:</p>
<ol>
<li>Measure execution time for different messages</li>
<li>Analyze temporal variations</li>
<li>Deduce which part of the S-box was accessed</li>
<li>Progressively recover key bytes</li>
</ol>

<p><strong>Countermeasures</strong>:</p>
<ul>
<li>Constant-time implementations (same duration regardless of input)</li>
<li>Cache disabling for sensitive operations</li>
<li>Adding temporal noise (jitter)</li>
</ul>

<p><strong>Cache analysis attacks</strong>:</p>

<p>The CPU cache can reveal sensitive information.</p>

<p><strong>Prime+Probe technique</strong>:</p>
<ol>
<li>Attacker fills the cache with their own data (Prime)</li>
<li>Victim executes cryptographic operation</li>
<li>Attacker measures which cache lines were evicted (Probe)</li>
<li>Deduce the victim's memory accesses</li>
</ol>

<p><strong>Lab performed: File opening detection</strong>:</p>

<p>Program spy.c:</p>
<ul>
<li>Flush the cache for an address of the target file</li>
<li>Wait for a delay</li>
<li>Measure access time to that address</li>
<li>If time &lt; threshold: file in cache &rarr; file was opened recently</li>
</ul>

<p>Application: activity spying without system access.</p>

<p><strong>Power consumption analysis attacks (Power Analysis)</strong>:</p>

<p><strong>Simple Power Analysis (SPA)</strong>:</p>

<p>Direct observation of the power consumption trace.</p>

<p>Each instruction consumes differently: multiplication, addition, memory read have distinct signatures.</p>

<p><strong>Example</strong>: Modular exponentiation in RSA:</p>
<ul>
<li>"Square" operation visible</li>
<li>"Square then multiply" operation visible</li>
<li>Private key bits can be directly deduced</li>
</ul>

<p><strong>Differential Power Analysis (DPA)</strong>:</p>

<p>Statistical analysis over many traces.</p>

<p>Principle:</p>
<ol>
<li>Capture N power traces for N different messages</li>
<li>Make hypotheses about part of the key</li>
<li>Predict consumption for each hypothesis</li>
<li>Correlate predictions with actual traces</li>
<li>The correct hypothesis gives the best correlation</li>
</ol>

<p><strong>Correlation Power Analysis (CPA)</strong>:</p>

<p>Improved variant using Pearson's correlation coefficient.</p>

<p>Allows attacking more resistant implementations.</p>

<p><strong>Lab performed: Power consumption analysis on STM32</strong>:</p>

<p>Program main.c (Lab 1):</p>
<ul>
<li>Microcontroller executes operations (repeated multiplications)</li>
<li>Oscilloscope captures power consumption</li>
<li>Trace analysis to identify operations</li>
<li>Correlation between manipulated data and consumption</li>
</ul>

<h3 class="section-title">2. Fault injection attacks</h3>

<p><strong>Principle</strong>:</p>

<p>Deliberately cause errors during execution to obtain information or bypass protections.</p>

<p><strong>Injection techniques</strong>:</p>

<table>
<tr><th>Technique</th><th>Description</th><th>Effect</th></tr>
<tr><td>Clock glitching</td><td>Clock pulses</td><td>Skipped instructions</td></tr>
<tr><td>Voltage glitching</td><td>Supply voltage variation</td><td>Computation errors</td></tr>
<tr><td>Laser</td><td>Focused laser beam</td><td>Memory bit modification</td></tr>
<tr><td>Temperature</td><td>Heating/cooling</td><td>Instabilities</td></tr>
<tr><td>EM</td><td>Electromagnetic pulse</td><td>Circuit disturbance</td></tr>
</table>

<p><strong>Example: Attack on authentication</strong>:</p>

<p>Vulnerable code:</p>
<pre><code>if (password == correct_password) {
    grant_access();
} else {
    deny_access();
}</code></pre>

<p>Fault injection at the time of the test:</p>
<ul>
<li>The test fails (wrong password)</li>
<li>But the fault inverts the result &rarr; access granted</li>
</ul>

<p><strong>Countermeasures</strong>:</p>
<ul>
<li>Redundancy (double verification)</li>
<li>Error-correcting codes</li>
<li>Glitch detectors (voltage/clock sensors)</li>
<li>Consistency checks</li>
</ul>

<h3 class="section-title">3. Software vulnerabilities: Buffer Overflow</h3>

<p><strong>Principle</strong>:</p>

<p>Buffer overflow: writing beyond the allocated size of a buffer, overwriting adjacent data (return address, variables).</p>

<p><strong>Stack mechanism</strong>:</p>

<p>Stack organization during a function call:</p>
<pre><code>[parameters]
[return address]
[old ebp]
[local variables]
[buffer]</code></pre>

<p>If too much is written into the buffer, it overwrites variables, ebp, and the return address.</p>

<p><strong>Exploitation</strong>:</p>

<ol>
<li>Fill the buffer with malicious code (shellcode)</li>
<li>Overwrite the return address to point to the shellcode</li>
<li>When the function returns, the shellcode executes</li>
</ol>

<p><strong>Lab performed: Buffer overflow exploitation</strong>:</p>

<p><strong>Part 1: Memory organization</strong>:</p>
<p>Stack analysis with GDB, offset calculation.</p>

<p><strong>Part 2: Simple exploitation</strong>:</p>
<p>Vulnerable program with strcpy without size checking. Injection to modify a variable or skip a verification.</p>

<p><strong>Part 3: Shellcode injection</strong>:</p>

<p>shellcode.c:</p>
<pre><code>void shellcode() {
  asm(
    "mov $0x3b, %rax"    // syscall execve
    "mov $0x0, %rdx"
    "movabs $0x0068732f6e69622f, %r8"  // "/bin/sh"
    "push %r8"
    "mov %rsp, %rdi"     // address of "/bin/sh"
    "syscall"            // execve("/bin/sh", ...)
  );
}</code></pre>

<p>Objective: inject this code and redirect execution to open a shell.</p>

<p><strong>Part 4 &amp; 5: Complete exploitation</strong>:</p>
<ul>
<li>Calculating the shellcode address</li>
<li>Constructing the payload (NOP sled + shellcode + return address)</li>
<li>Injection via upload.py</li>
<li>Obtaining a shell with privileges</li>
</ul>

<p><strong>Modern countermeasures</strong>:</p>

<table>
<tr><th>Countermeasure</th><th>Description</th></tr>
<tr><td>Stack canaries</td><td>Sentinel value before return address, verified</td></tr>
<tr><td>ASLR (Address Space Layout Randomization)</td><td>Randomized memory addresses</td></tr>
<tr><td>DEP/NX (Data Execution Prevention)</td><td>Non-executable memory (stack, heap)</td></tr>
<tr><td>RELRO (Relocation Read-Only)</td><td>Read-only memory sections</td></tr>
<tr><td>Secure compilation</td><td>Options -fstack-protector, -D_FORTIFY_SOURCE</td></tr>
</table>

<h3 class="section-title">4. Cache analysis - Profiling</h3>

<p><strong>Memory hierarchy</strong>:</p>

<p>CPU &rarr; L1 Cache (1-3 cycles) &rarr; L2 Cache (10-20 cycles) &rarr; L3 Cache (40-75 cycles) &rarr; RAM (100-300 cycles)</p>

<p>The cache speeds up access to frequently used data.</p>

<p><strong>Access time measurement</strong>:</p>

<p>Cache Profiling Lab (profiling.c):</p>
<ul>
<li>Function memaccesstime(ptr): measures the time to access an address</li>
<li>Function clflush(ptr): flushes the address from cache</li>
<li>Profiling loop:
  <ul>
  <li>Access &rarr; measure (cache hit)</li>
  <li>Flush &rarr; access &rarr; measure (cache miss)</li>
  </ul>
</li>
<li>Histogram generation with gnuplot</li>
</ul>

<p><strong>Typical results</strong>:</p>
<ul>
<li>Cache hit: 10-50 cycles</li>
<li>Cache miss: 200-400 cycles</li>
</ul>

<p><strong>Exploitation for attack</strong>:</p>

<p><strong>Flush+Reload technique</strong>:</p>
<ol>
<li>Flush a cache line shared with the victim</li>
<li>Victim executes their code</li>
<li>Attacker measures reload time</li>
<li>If fast: victim accessed that line</li>
</ol>

<p><strong>Application: File opening detection</strong> (spy.c):</p>
<ul>
<li>Monitor an address of a sensitive file</li>
<li>If the file is opened by a process, it will be in cache</li>
<li>Detection without access to the file system</li>
</ul>

<h3 class="section-title">5. Cryptographic vulnerabilities - AES</h3>

<p><strong>AES (Advanced Encryption Standard)</strong>:</p>

<p>Block cipher algorithm, standard since 2001.</p>

<p><strong>Structure</strong>:</p>
<ul>
<li>128-bit blocks</li>
<li>128, 192, or 256-bit keys</li>
<li>10, 12, or 14 rounds depending on key size</li>
<li>Operations: SubBytes (S-box), ShiftRows, MixColumns, AddRoundKey</li>
</ul>

<p><strong>Implementation vulnerabilities</strong>:</p>

<p><strong>Naive implementation: Key-dependent table access</strong></p>

<p>AES uses substitution tables (S-box). The classic implementation stores these tables in memory.</p>

<p>During execution:</p>
<pre><code>state[i] = Sbox[state[i] XOR key[i]]</code></pre>

<p>The access index depends on the key: vulnerability to cache attacks.</p>

<p><strong>Lab: OpenSSL version comparison</strong></p>

<p><strong>OpenSSL 0.9.7a (vulnerable)</strong>:</p>
<ul>
<li>Direct access to tables T0, T1, T2, T3</li>
<li>Indices depend on data and key</li>
<li>Vulnerable to cache timing attacks</li>
</ul>

<p><strong>OpenSSL 1.1.1t (protected)</strong>:</p>
<ul>
<li>AES-NI implementation (hardware instructions)</li>
<li>No key-dependent memory access</li>
<li>Resistant to cache timing attacks</li>
</ul>

<p><strong>AES-NI</strong>:</p>

<p>Dedicated processor instructions (Intel, AMD since 2010):</p>
<ul>
<li>AESENC, AESENCLAST: encryption</li>
<li>AESDEC, AESDECLAST: decryption</li>
<li>AESIMC, AESKEYGENASSIST: key generation</li>
</ul>

<p>Advantages:</p>
<ul>
<li>High performance</li>
<li>Implementation resistant to side channels</li>
<li>No tables in memory</li>
</ul>

<h3 class="section-title">6. Other countermeasures</h3>

<p><strong>Masking</strong>:</p>

<p>Technique against DPA attacks.</p>

<p>Principle: Randomize intermediate values.</p>

<p>Instead of directly manipulating x, we manipulate x XOR m (m random).</p>

<p>Consumption leaks relate to x XOR m, which is random.</p>

<p><strong>Example</strong>:</p>
<pre><code>x' = x XOR m
y' = f(x') = f(x XOR m)
y = y' XOR m' (where m' derives from m)</code></pre>

<p><strong>Drawbacks</strong>:</p>
<ul>
<li>Overhead in computation and randomness</li>
<li>Difficult to implement correctly (possible leaks)</li>
</ul>

<p><strong>Hiding</strong>:</p>

<p>Reduce the signal-to-noise ratio in power consumption traces.</p>

<p>Techniques:</p>
<ul>
<li>Randomization of operation order</li>
<li>Insertion of dummy operations</li>
<li>Constant consumption (dual-rail circuits)</li>
</ul>

<p><strong>Physical security</strong>:</p>

<p><strong>Sensors</strong>:</p>
<ul>
<li>Tamper detection sensors (case opening)</li>
<li>Temperature and light sensors</li>
<li>Abnormal voltage/frequency sensors</li>
</ul>

<p><strong>Erasable memory</strong>:</p>
<p>In case of attack detection, erase the keys.</p>

<p><strong>Encapsulation</strong>:</p>
<p>Protect sensitive circuits in resins that are difficult to remove.</p>

<h3 class="section-title">7. Tools and methodologies</h3>

<p><strong>ChipWhisperer</strong>:</p>

<p>Open-source platform for side-channel analysis.</p>

<p>Features:</p>
<ul>
<li>Power consumption trace capture</li>
<li>Synchronization with target (trigger)</li>
<li>DPA, CPA analyses</li>
<li>Glitch injection (clock, voltage)</li>
</ul>

<p><strong>GDB (GNU Debugger)</strong>:</p>

<p>Used to analyze vulnerable programs:</p>
<ul>
<li>Setting breakpoints</li>
<li>Examining the stack and registers</li>
<li>Calculating offsets for exploitation</li>
</ul>

<p><strong>Useful commands</strong>:</p>
<pre><code>info registers    # register state
x/32x $rsp       # examine the stack
disassemble      # disassemble a function</code></pre>

<p><strong>Gnuplot</strong>:</p>

<p>Visualization of access time distributions (cache hit/miss).</p>

<h3 class="section-title">8. Application domains</h3>

<p><strong>Smart cards</strong>:</p>

<p>Privileged targets: payment, authentication, SIM.</p>
<p>Threats: cloning, key extraction.</p>
<p>Protections: masking, sensors, secure hardware.</p>

<p><strong>Critical embedded systems</strong>:</p>

<p>Automotive (CAN bus, ECU), aeronautics, medical.</p>
<p>Risks: fault injection, reverse engineering.</p>

<p><strong>IoT (Internet of Things)</strong>:</p>

<p>Connected objects often poorly protected.</p>
<p>Possible attacks: firmware extraction, cloning, botnets.</p>

<p><strong>Cloud infrastructure</strong>:</p>

<p>Cache attacks between virtual machines (VMs).</p>
<p>Risk of information leakage between tenants.</p>

<hr/>

<h2>PART D - Reflective Analysis and Perspectives</h2>

<h3 class="section-title">Skills acquired</h3>

<p><strong>Understanding hardware threats</strong>:</p>
<p>Ability to identify the physical and software vulnerabilities of embedded systems.</p>

<p><strong>Mastery of side-channel attacks</strong>:</p>
<p>Ability to analyze information leaks (timing, cache, power) and exploit these flaws.</p>

<p><strong>Software vulnerability exploitation</strong>:</p>
<p>Competence in buffer overflow exploitation, shellcode injection, and understanding of modern protections.</p>

<p><strong>Secure design</strong>:</p>
<p>Development of reflexes to integrate security from the design phase (secure by design).</p>

<p><strong>Holistic vision</strong>:</p>
<p>Ability to evaluate the overall security of a system by considering hardware, software, and physical attacks.</p>

<h3 class="section-title">Key takeaways</h3>

<p><strong>1. Security &ne; Cryptography alone</strong>:</p>
<p>A mathematically secure algorithm can be vulnerable if its implementation leaks information.</p>

<p><strong>2. Side channels are real</strong>:</p>
<p>Timing, cache, power consumption: these attacks are practical and have compromised real systems (bank cards, DRM).</p>

<p><strong>3. Defense in depth</strong>:</p>
<p>No silver bullet. Combine multiple countermeasures to increase the cost of an attack.</p>

<p><strong>4. Security/performance trade-off</strong>:</p>
<p>Protections cost performance, energy, and complexity. Finding the right balance depends on the context.</p>

<p><strong>5. Constant evolution</strong>:</p>
<p>New attacks are regularly discovered (Spectre, Meltdown, Rowhammer). Continuous technology watch is essential.</p>

<h3 class="section-title">Feedback</h3>

<p><strong>Eye-opening aspect</strong>:</p>
<p>This course opened my eyes to the fragility of systems against physical attacks. Seeing theoretical attacks work in lab sessions is impressive.</p>

<p><strong>Difficulty of security</strong>:</p>
<p>Designing a secure system is difficult. You have to think like an attacker to identify all possible flaws.</p>

<p><strong>Specialized tools</strong>:</p>
<p>Handling ChipWhisperer, GDB, and analyzing traces requires practice. The lab sessions allowed familiarization with these professional tools.</p>

<p><strong>Necessary balance</strong>:</p>
<p>Countermeasures add complexity. The threat level must be assessed and protection adapted accordingly.</p>

<h3 class="section-title">Practical applications</h3>

<p><strong>For a security engineer</strong>:</p>
<ul>
<li>Security audit of embedded systems</li>
<li>Design of products resistant to physical attacks</li>
<li>Security certification (Common Criteria, FIPS)</li>
</ul>

<p><strong>For an embedded developer</strong>:</p>
<ul>
<li>Writing attack-resistant code (constant timing)</li>
<li>Avoiding classic vulnerabilities (buffer overflow)</li>
<li>Testing robustness against faults</li>
</ul>

<p><strong>For a hardware designer</strong>:</p>
<ul>
<li>Integrating hardware countermeasures (sensors, masking)</li>
<li>Choosing secure components (TEE, Secure Element)</li>
<li>Evaluating risks from the design phase</li>
</ul>

<p><strong>In everyday life</strong>:</p>
<ul>
<li>Understanding the risks of connected objects (cameras, locks)</li>
<li>Evaluating product security (bank cards, smartphones)</li>
<li>Raising awareness about cybersecurity issues</li>
</ul>

<h3 class="section-title">Limitations and perspectives</h3>

<p><strong>Module limitations</strong>:</p>
<ul>
<li>Limited coverage of EM (electromagnetic) attacks</li>
<li>No hands-on laser injection or voltage glitching</li>
<li>Legal and ethical aspects barely addressed</li>
</ul>

<p><strong>Openings towards</strong>:</p>
<ul>
<li><strong>Secure Elements</strong>: HSM, TPM, Trusted Execution Environments (TEE)</li>
<li><strong>Post-Quantum Cryptography</strong>: resistance to quantum computers</li>
<li><strong>Formal Verification</strong>: formal proofs of security</li>
<li><strong>Bug Bounty</strong>: ethical vulnerability research</li>
</ul>

<h3 class="section-title">Recent developments</h3>

<p><strong>Spectre and Meltdown attacks (2018)</strong>:</p>

<p>Exploitation of speculative execution in modern processors.</p>

<p>Spectre: force a program to reveal its secrets via the cache.</p>
<p>Meltdown: read kernel memory from user space.</p>

<p>Impact: all Intel, AMD, ARM processors affected.</p>

<p><strong>Rowhammer (2014)</strong>:</p>

<p>Attack on DRAM memory: repeated access to memory rows can induce bit flips on adjacent rows.</p>

<p>Exploitation: privilege escalation, virtual machine escape.</p>

<p><strong>Attacks on embedded AI</strong>:</p>

<p>Neural networks are vulnerable:</p>
<ul>
<li>Adversarial attacks (imperceptible perturbations)</li>
<li>Model extraction through observation</li>
<li>Backdoors in models</li>
</ul>

<p>Growing concern with embedded AI (voice recognition, vision).</p>

<p><strong>5G and IoT</strong>:</p>

<p>Explosion in the number of connected objects.</p>
<p>Considerable attack surface.</p>
<p>Need for lightweight and energy-efficient security.</p>

<h3 class="section-title">Tips for success</h3>

<p><strong>1. Understand before exploiting</strong>:</p>
<p>Master the normal operation of a system before looking for flaws.</p>

<p><strong>2. Take lab work seriously</strong>:</p>
<p>Hands-on exercises are essential for internalizing concepts.</p>

<p><strong>3. Read the code</strong>:</p>
<p>Analyze source code (shellcode, AES) to understand vulnerabilities.</p>

<p><strong>4. Think like an attacker</strong>:</p>
<p>Adopt an attacker's mindset: look for the weakest link, implicit assumptions.</p>

<p><strong>5. Do your research</strong>:</p>
<p>Read academic papers, vulnerability reports (CVE), security blogs.</p>

<p><strong>6. Respect ethics</strong>:</p>
<p>Never use this knowledge illegally. Ethical hacking only.</p>

<h3 class="section-title">Conclusion</h3>

<p>This module is fundamental for anyone working on embedded or critical systems. Hardware security is often neglected in favor of software security, but physical attacks are real and effective.</p>

<p><strong>Transferable skills</strong>:</p>
<ul>
<li>Critical analysis of a system's security</li>
<li>Deep understanding of processor and memory operation</li>
<li>Ability to integrate security from the design phase</li>
<li>Multidisciplinary vision (hardware, software, cryptography, physics)</li>
</ul>

<p><strong>Professional relevance</strong>:</p>
<p>With the explosion of IoT, Industry 4.0, and autonomous vehicles, hardware security is a field in high demand. Engineers trained in these issues are sought after.</p>

<p><strong>Key message</strong>:</p>
<p>Security is a process, not a product. You must constantly evaluate, test, and improve. A system is never 100% secure, but the cost of an attack can be significantly increased.</p>

<p><strong>Recommendations</strong>:</p>
<ul>
<li>Deepen knowledge with advanced courses (Riscure Academy, Coursera)</li>
<li>Attend security conferences (Black Hat, DEF CON, CHES)</li>
<li>Practice on platforms (Hack The Box, hardware security CTF)</li>
<li>Join communities (r/ReverseEngineering, specialized forums)</li>
<li>Stay informed about new vulnerabilities (CVE, security bulletins)</li>
</ul>

<p><strong>Links with other courses</strong>:</p>
<ul>
<li><a href="./architecture-materielle.html">Hardware Architecture - S6</a>: caches, processors</li>
<li><a href="./microcontroleur.html">Microcontrollers - S6</a>: ARM Cortex, embedded systems</li>
<li><a href="./systemes-exploitation.html">Operating Systems - S5</a>: memory management</li>
<li><a href="./langage-c.html">C Language - S5</a>: low-level programming</li>
<li><a href="./embedded-ia-iot.html">Embedded IA for IoT - S9</a>: security of connected objects</li>
</ul>

<hr/>

<h2>Course Documents</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Complete Course</h4>
      <p>Complete hardware security course: side-channel attacks, buffer overflow, Spectre/Meltdown vulnerabilities.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S7/Securite-Materielle/cours-complet.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S7/Securite-Materielle/cours-complet.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>Buffer Overflow</h4>
      <p>Course on buffer overflow attacks: exploitation, stack smashing, protections and countermeasures.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S7/Securite-Materielle/buffer-overflow.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S7/Securite-Materielle/buffer-overflow.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>Lab: Cache Side-Channel Attack</h4>
      <p>Lab subject on cache side-channel attacks: timing attacks, Flush+Reload and experiments.</p>
      <div class="pdf-lazy" data-src="/cours-pdf/S7/Securite-Materielle/tp-cache-sca.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S7/Securite-Materielle/tp-cache-sca.pdf" target="_blank">Download</a></p>
    </div>
  </div>
</div>

<hr/>

<p><em>Course taken in 2023-2024 at INSA Toulouse, Department of Electrical Engineering and Computer Science.</em></p>

</div>

<div class="back-nav">
    <a href="./my-courses-2023-2024.html" data-i18n-html="back-courses-2023-2024">&larr; Retour aux Cours 2023-2024</a>
</div>

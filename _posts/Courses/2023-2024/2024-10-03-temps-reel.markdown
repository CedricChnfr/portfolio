---
layout: default
title: "Temps Reel - S8"
date: 2024-10-02 10:56:03 +0200
---

<style>
.back-nav {
    background: #f4f4f4;
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 20px;
}
.back-nav a {
    color: #007BFF;
    text-decoration: none;
    font-weight: bold;
}
.back-nav a:hover {
    text-decoration: underline;
}

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f9;
    color: #333;
    line-height: 1.6;
}
h2, h3, h4 {
    color: #007BFF;
}
p {
    text-align: justify;
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

<h1>Temps Reel</h1>

<p><strong>Cours connexes</strong> :</p>
<ul>
<li><a href="./commande-numerique.html">Commande Numerique - S8</a> - Lois de commande numeriques</li>
<li><a href="./reseaux-petri.html">Reseaux de Petri - S8</a> - Modelisation des systemes temps reel</li>
</ul>

<hr/>

<h2>PARTIE A : GENERALITES</h2>

<h3>Presentation</h3>
<p>Le cours "Temps Reel" traite des systemes informatiques devant reagir a des evenements externes dans des contraintes temporelles strictes. Un systeme temps reel ne doit pas seulement produire des resultats corrects, mais aussi les produire a temps. Ces systemes sont omnipresents: avionique, automobile, robotique, controle industriel, telecommunications. Le cours couvre l'ordonnancement de taches, les systemes d'exploitation temps reel (RTOS), et les techniques de conception garantissant le respect des echeances.</p>

<p><strong>Annee Academique</strong> : 2023-2024<br/>
<strong>Semestre</strong> : 8<br/>
<strong>Categorie</strong> : Informatique / Systemes Embarques</p>

<hr/>

<h2>PARTIE B : PARTIE DESCRIPTIVE</h2>

<h3>Details de l'experience</h3>

<h4>Environnement et contexte</h4>
<p>Le cours combinait theorie de l'ordonnancement avec implementation pratique sur microcontroleurs et RTOS (FreeRTOS, RTOS embarques). Nous avons programme des systemes multitaches avec contraintes temporelles, analyse leur ordonnancabilite, et mesure les performances reelles. Les projets incluaient des applications concretes: acquisition de donnees periodique, controle moteur, communication temps reel.</p>

<h4>Ma fonction</h4>
<p>Dans ce cours, j'ai ete responsable de :</p>
<ul>
<li>Comprendre les contraintes temporelles (echeances, periodes, gigue)</li>
<li>Analyser l'ordonnancabilite de systemes de taches</li>
<li>Implementer des applications multitaches sur RTOS</li>
<li>Gerer les ressources partagees (mutex, semaphores)</li>
<li>Eviter interblocages et inversions de priorite</li>
<li>Mesurer et valider les performances temporelles</li>
<li>Concevoir des systemes garantissant le respect des echeances</li>
</ul>

<h2>PARTIE C : PARTIE TECHNIQUE</h2>

<p>Cette section explore les aspects techniques des systemes temps reel.</p>

<h3>Concepts techniques appris</h3>

<h4>1. Definitions et Classifications</h4>

<p><strong>Systeme Temps Reel</strong> :
Systeme dont la correction depend non seulement du resultat logique mais aussi du moment ou il est produit.</p>

<p><strong>Classification</strong> :</p>

<p><strong>Temps Reel Dur (Hard Real-Time)</strong> :
Echeance manquee = catastrophe (crash, perte, danger).
Exemples: airbag, pilote automatique d'avion, pacemaker.</p>

<p><strong>Temps Reel Mou (Soft Real-Time)</strong> :
Echeance manquee = degradation de qualite (acceptable occasionnellement).
Exemples: streaming video, jeux video, interface utilisateur.</p>

<p><strong>Temps Reel Ferme (Firm Real-Time)</strong> :
Echeance manquee = resultat inutile mais pas dangereux.
Exemples: certains capteurs (echantillon perdu acceptable).</p>

<h4>2. Modele de Taches Periodiques</h4>

<p><strong>Tache ti</strong> caracterisee par :</p>
<ul>
<li><strong>Ci</strong> : temps d'execution pire cas (WCET)</li>
<li><strong>Ti</strong> : periode (intervalle entre activations)</li>
<li><strong>Di</strong> : echeance relative (deadline)</li>
<li><strong>Pi</strong> : priorite</li>
</ul>

<p><strong>Taches periodiques</strong> :
Activees a t=0, Ti, 2Ti, 3Ti, ...</p>

<p><strong>Contrainte</strong> :
Terminer avant echeance: ti + Di (souvent Di = Ti)</p>

<p><strong>Facteur d'utilisation</strong> :</p>
<pre><code>U = Sum Ci/Ti</code></pre>

<p>Proportion du processeur utilisee.</p>

<p><strong>Condition necessaire d'ordonnancabilite</strong> :</p>
<pre><code>U &lt;= 1</code></pre>

<p>Si U > 1, impossible de respecter toutes les echeances.</p>

<h4>3. Ordonnancement a Priorites Fixes</h4>

<p><strong>Rate Monotonic (RM)</strong> :
Priorite inversement proportionnelle a la periode.
Periode courte -> priorite haute.</p>

<p><strong>Test d'ordonnancabilite (Liu &amp; Layland)</strong> :</p>
<pre><code>Si U &lt;= n(2^(1/n) - 1) alors ordonnancable par RM</code></pre>

<p>Pour n->infini : U &lt;= ln(2) ~ 0.69</p>

<p>Condition suffisante (pas necessaire).</p>

<p><strong>Test exact</strong> (analyse du temps de reponse) :
Pour chaque tache ti, calculer temps de reponse Ri :</p>
<pre><code>Ri = Ci + Sum_j(prio>prioi) ceil(Ri/Tj) x Cj</code></pre>

<p>Resolution iterative.</p>

<p>Ordonnancable si Ri &lt;= Di pour tout i.</p>

<p><strong>Deadline Monotonic (DM)</strong> :
Si Di != Ti, priorite selon echeance.
Echeance courte -> priorite haute.</p>

<p>Optimal pour priorites fixes avec Di &lt;= Ti.</p>

<h4>4. Ordonnancement a Priorites Dynamiques</h4>

<p><strong>Earliest Deadline First (EDF)</strong> :
A chaque instant, executer tache avec echeance absolue la plus proche.</p>

<p><strong>Optimalite</strong> :
EDF est optimal pour monoprocesseur.
Si un algorithme peut ordonnancer un systeme, EDF le peut.</p>

<p><strong>Test d'ordonnancabilite</strong> :</p>
<pre><code>U &lt;= 1</code></pre>

<p>Condition necessaire ET suffisante pour EDF avec Di = Ti.</p>

<p><strong>Avantages</strong> :</p>
<ul>
<li>Meilleure utilisation processeur (jusqu'a 100%)</li>
<li>Optimal</li>
</ul>

<p><strong>Inconvenients</strong> :</p>
<ul>
<li>Overhead (changements de contexte frequents)</li>
<li>Comportement moins predictible en surcharge</li>
<li>Implementation plus complexe</li>
</ul>

<h4>5. Taches Aperiodiques et Sporadiques</h4>

<p><strong>Taches aperiodiques</strong> :
Activations irregulieres, souvent sans echeance stricte.</p>

<p><strong>Taches sporadiques</strong> :
Activations irregulieres avec intervalle minimum et echeance.</p>

<p><strong>Serveurs</strong> :
Mecanismes pour integrer taches aperiodiques dans systeme periodique.</p>

<p><strong>Polling Server</strong> :
Tache periodique reservee pour aperiodiques.</p>

<p><strong>Deferrable Server</strong> :
Capacite preservee si pas utilisee.</p>

<p><strong>Sporadic Server</strong> :
Compromis performance/simplicite.</p>

<h4>6. Synchronisation et Ressources Partagees</h4>

<p><strong>Probleme</strong> :
Taches partagent ressources (variables, peripheriques).
Acces concurrent -> corruption donnees.</p>

<p><strong>Section critique</strong> :
Portion de code accedant ressource partagee.</p>

<p><strong>Mecanismes</strong> :</p>

<p><strong>Mutex</strong> (Mutual Exclusion) :
Lock/Unlock pour proteger section critique.</p>

<p><strong>Semaphore</strong> :
Compteur controlant acces.</p>
<ul>
<li>Binaire (0 ou 1) : comme mutex</li>
<li>Comptant : plusieurs acces simultanes (pool de ressources)</li>
</ul>

<p><strong>Inversion de priorite</strong> :
Tache haute priorite bloquee par tache basse priorite.</p>

<p><strong>Exemple classique (Mars Pathfinder)</strong> :
Tache priorite haute bloquee indefiniment -> reset systeme.</p>

<p><strong>Solutions</strong> :</p>

<p><strong>Priority Inheritance Protocol (PIP)</strong> :
Tache tenant ressource herite temporairement priorite de tache bloquee la plus haute.</p>

<p><strong>Priority Ceiling Protocol (PCP)</strong> :
Ressource a priorite plafond = max des priorites des taches l'utilisant.
Tache accedant a ressource acquiert temporairement cette priorite.</p>

<p>Evite inversions de priorite multiples et interblocages.</p>

<h4>7. Interblocages (Deadlocks)</h4>

<p><strong>Conditions de Coffman</strong> (4 necessaires) :</p>
<ol>
<li><strong>Exclusion mutuelle</strong> : ressources non partageables</li>
<li><strong>Hold and wait</strong> : tache tient ressources et en attend d'autres</li>
<li><strong>Pas de preemption</strong> : ressources non preemptibles</li>
<li><strong>Attente circulaire</strong> : cycle dans graphe d'allocation</li>
</ol>

<p><strong>Prevention</strong> :
Casser une des 4 conditions.</p>

<p><strong>Exemple</strong> : ordre total d'acquisition des ressources (evite cycles).</p>

<p><strong>Detection et recuperation</strong> :
Detecter cycles, puis tuer/redemarrer taches.
Couteux en temps reel.</p>

<p><strong>Evitement</strong> (algorithme du banquier) :
N'allouer que si etat sur garanti.
Overhead eleve, peu utilise en temps reel.</p>

<h4>8. Systemes d'Exploitation Temps Reel (RTOS)</h4>

<p><strong>Caracteristiques</strong> :</p>
<ul>
<li><strong>Determinisme</strong> : comportement temporel previsible</li>
<li><strong>Latence d'interruption</strong> faible et bornee</li>
<li><strong>Preemptibilite</strong> : tache haute priorite peut interrompre basse</li>
<li><strong>Ordonnancement</strong> prioritaire (souvent priorites fixes)</li>
<li><strong>Primitives de synchronisation</strong> (mutex, semaphores)</li>
<li><strong>Gestion memoire</strong> deterministe (pas de garbage collector imprevisible)</li>
</ul>

<p><strong>RTOS populaires</strong> :</p>

<p><strong>FreeRTOS</strong> :</p>
<ul>
<li>Open source</li>
<li>Leger (quelques Ko)</li>
<li>Portable (nombreux microcontroleurs)</li>
<li>API simple</li>
<li>Ordonnancement preemptif a priorites fixes</li>
</ul>

<p><strong>VxWorks</strong> :</p>
<ul>
<li>Commercial (Wind River)</li>
<li>Robuste, certifie (aerospatial, medical)</li>
<li>Riche en fonctionnalites</li>
</ul>

<p><strong>QNX</strong> :</p>
<ul>
<li>Microkernel</li>
<li>POSIX compliant</li>
<li>Automobile (BlackBerry)</li>
</ul>

<p><strong>RT-Linux / Xenomai</strong> :</p>
<ul>
<li>Extension temps reel de Linux</li>
<li>Cohabitation taches temps reel / non temps reel</li>
</ul>

<p><strong>Zephyr</strong> :</p>
<ul>
<li>Open source, moderne</li>
<li>IoT et objets connectes</li>
</ul>

<h4>9. API FreeRTOS (Exemples)</h4>

<p><strong>Creation de tache</strong> :</p>
<pre><code class="language-c">xTaskCreate(
    vTaskFunction,      // Pointeur fonction
    "TaskName",         // Nom (debug)
    STACK_SIZE,         // Taille stack
    NULL,               // Parametres
    PRIORITY,           // Priorite
    &amp;xTaskHandle        // Handle (optionnel)
);</code></pre>

<p><strong>Mutex</strong> :</p>
<pre><code class="language-c">xMutex = xSemaphoreCreateMutex();

xSemaphoreTake(xMutex, portMAX_DELAY);  // Lock
// Section critique
xSemaphoreGive(xMutex);  // Unlock</code></pre>

<p><strong>Semaphore binaire</strong> (signalisation) :</p>
<pre><code class="language-c">xSemaphore = xSemaphoreCreateBinary();

// ISR:
xSemaphoreGiveFromISR(xSemaphore, NULL);

// Tache:
xSemaphoreTake(xSemaphore, portMAX_DELAY);  // Attend signal</code></pre>

<p><strong>Queues</strong> (files FIFO) :</p>
<pre><code class="language-c">xQueue = xQueueCreate(QUEUE_LENGTH, sizeof(DataType));

xQueueSend(xQueue, &amp;data, TIMEOUT);
xQueueReceive(xQueue, &amp;buffer, TIMEOUT);</code></pre>

<p><strong>Delais</strong> :</p>
<pre><code class="language-c">vTaskDelay(pdMS_TO_TICKS(100));  // Delai 100ms</code></pre>

<h4>10. Mesure et Validation</h4>

<p><strong>WCET</strong> (Worst-Case Execution Time) :
Temps d'execution maximum.</p>

<p><strong>Methodes de determination</strong> :</p>
<ul>
<li><strong>Mesure</strong> : instrumenter code, tester scenarios</li>
<li><strong>Analyse statique</strong> : analyser code, modele processeur</li>
<li><strong>Hybride</strong> : combiner les deux</li>
</ul>

<p>Difficile a determiner precisement (caches, pipelines, branchements).</p>

<p><strong>Marges de securite</strong> :
Utiliser WCET majore pour robustesse.</p>

<p><strong>Outils de mesure</strong> :</p>
<ul>
<li>Oscilloscope logique</li>
<li>Traceurs temps reel</li>
<li>GPIO toggling (observer signaux)</li>
<li>Compteurs hardware</li>
</ul>

<p><strong>Validation</strong> :</p>
<ul>
<li>Tests de stress (charge max)</li>
<li>Injection de fautes</li>
<li>Tests de longue duree (vieillissement)</li>
</ul>

<h4>11. Conception de Systemes Temps Reel</h4>

<p><strong>Methodologie</strong> :</p>

<p><strong>1. Specification</strong> :</p>
<ul>
<li>Identifier taches et contraintes temporelles</li>
<li>Periodes, echeances, priorites</li>
</ul>

<p><strong>2. Modelisation</strong> :</p>
<ul>
<li>Diagrammes de sequence</li>
<li>Diagrammes d'etats</li>
<li>Reseaux de Petri temporises</li>
</ul>

<p><strong>3. Analyse d'ordonnancabilite</strong> :</p>
<ul>
<li>Calculer U</li>
<li>Tests RM/EDF</li>
<li>Analyse temps de reponse</li>
</ul>

<p><strong>4. Implementation</strong> :</p>
<ul>
<li>Choix RTOS</li>
<li>Codage taches</li>
<li>Synchronisation</li>
</ul>

<p><strong>5. Validation</strong> :</p>
<ul>
<li>Tests unitaires</li>
<li>Tests d'integration</li>
<li>Mesures temporelles</li>
</ul>

<p><strong>6. Optimisation</strong> :</p>
<ul>
<li>Reduire WCET (code, compilateur)</li>
<li>Ajuster priorites</li>
<li>Repartir charges</li>
</ul>

<p><strong>Patterns de conception</strong> :</p>
<ul>
<li><strong>Cyclic Executive</strong> : boucle infinie avec ordonnancement statique (simple mais peu flexible)</li>
<li><strong>Time-Triggered</strong> : activation sur timer (deterministe)</li>
<li><strong>Event-Triggered</strong> : activation sur evenements (reactif mais moins predictible)</li>
</ul>

<h4>12. Defis et Bonnes Pratiques</h4>

<p><strong>Defis</strong> :</p>

<p><strong>Jitter</strong> :
Variation du delai (problematique pour controle, audio).
Minimiser par ordonnancement approprie.</p>

<p><strong>Overhead</strong> :
Changements de contexte, gestion RTOS.
Peut etre significatif (10-20%).</p>

<p><strong>Multiprocesseur</strong> :
Ordonnancement plus complexe.
Partitionnement de taches ou migration.</p>

<p><strong>Interruptions</strong> :
Peuvent perturber ordonnancement.
Limiter duree ISR (Interrupt Service Routine).</p>

<p><strong>Bonnes pratiques</strong> :</p>

<p><strong>ISR courtes</strong> :
Minimiser traitement en interruption.
Utiliser semaphore pour debloquer tache (traitement differe).</p>

<p><strong>Sections critiques courtes</strong> :
Minimiser temps mutex tenu.</p>

<p><strong>Eviter operations bloquantes</strong> :
Pas d'I/O bloquants, pas de malloc (temps variable).</p>

<p><strong>Utiliser ressources deterministes</strong> :
Allocation statique memoire, buffers circulaires.</p>

<p><strong>Dimensionnement conservateur</strong> :
Marges sur WCET, utilisation processeur.</p>

<p><strong>Tests exhaustifs</strong> :
Valider tous scenarios, conditions limites.</p>

<h2>PARTIE D : PARTIE ANALYTIQUE</h2>

<h3>Connaissances et competences mobilisees</h3>

<ul>
<li>Theorie de l'ordonnancement</li>
<li>Analyse d'ordonnancabilite (RM, EDF)</li>
<li>Programmation systeme embarque</li>
<li>Utilisation de RTOS (FreeRTOS)</li>
<li>Synchronisation et gestion ressources partagees</li>
<li>Resolution problemes d'interblocage et inversion de priorite</li>
<li>Mesure et validation temporelle</li>
<li>Conception de systemes avec contraintes temps reel</li>
</ul>

<h3>Auto-evaluation</h3>

<p>Ce cours a ete exigeant mais passionnant. Les systemes temps reel introduisent une dimension (le temps) qui change radicalement la conception par rapport a la programmation classique.</p>

<p>La theorie de l'ordonnancement est mathematiquement rigoureuse. Les tests d'ordonnancabilite (RM, EDF) fournissent des garanties formelles, ce qui est rassurant pour systemes critiques. Cependant, determiner le WCET precisement reste un defi.</p>

<p>Le fosse entre RM (simple, utilise en pratique) et EDF (optimal mais complexe) est interessant. Le choix depend du contexte: critique (RM pour predictibilite) ou haute performance (EDF pour utilisation maximale).</p>

<p>La programmation avec RTOS a ete revelatrice. Gerer taches concurrentes, synchronisation, priorites demande rigueur. Les bugs sont souvent subtils (race conditions, deadlocks) et difficiles a reproduire.</p>

<p>L'inversion de priorite et ses solutions (PIP, PCP) montrent l'importance de comprendre les mecanismes profonds. Un simple mutex mal utilise peut causer blocages catastrophiques (cf. Mars Pathfinder).</p>

<p>Les mesures temporelles m'ont confronte a la realite: le WCET theorique et mesure peuvent differer. Les facteurs materiels (caches, interruptions) compliquent les predictions.</p>

<p>La conception d'un systeme temps reel necessite approche methodique: specification claire, analyse formelle, tests exhaustifs. L'improvisation est dangereuse.</p>

<h3>Mon avis</h3>

<p>Ce cours est indispensable pour ingenieurs en systemes embarques, automatique, ou developpant applications critiques.</p>

<p><strong>Points forts</strong> :</p>
<ul>
<li>Theorie solide (ordonnancement)</li>
<li>Pratique sur RTOS reels (FreeRTOS)</li>
<li>Conscience des pieges (inversions priorite, deadlocks)</li>
<li>Applications concretes</li>
</ul>

<p><strong>Points a ameliorer</strong> :</p>
<ul>
<li>Plus sur multiprocesseurs (multi-core omnipresents)</li>
<li>Outils d'analyse statique de WCET</li>
<li>Certification (DO-178C aerospatial, ISO 26262 automobile)</li>
<li>Temps reel distribue (reseaux, synchronisation)</li>
</ul>

<p><strong>Reflexions personnelles</strong> :</p>

<p>Le temps reel n'est pas "faire vite" mais "faire a temps". Un systeme rapide en moyenne mais avec variation importante peut etre pire qu'un systeme plus lent mais deterministe.</p>

<p>La garantie d'echeance est plus importante que la performance moyenne. C'est un changement de mentalite par rapport au developpement logiciel classique (ou on optimise le cas moyen).</p>

<p>Les systemes temps reel sont omnipresents mais invisibles: ABS dans voitures, pilotes automatiques, controleurs industriels, pacemakers. Leur fiabilite est critique car des vies en dependent.</p>

<p>La certification (aerospatial, medical, automobile) impose processus rigoureux et tracabilite. Le code doit etre prouve correct, pas juste teste. Les methodes formelles deviennent essentielles.</p>

<p>La complexite croit avec :</p>
<ul>
<li>Multiprocesseurs (partitionnement, communication)</li>
<li>Systemes distribues (horloges, latences reseau)</li>
<li>Intelligence embarquee (IA temps reel)</li>
</ul>

<p><strong>Applications professionnelles</strong> :</p>

<p>Competences temps reel applicables dans :</p>
<ul>
<li><strong>Automobile</strong> : ESP, ABS, ADAS, vehicules autonomes</li>
<li><strong>Aerospatial</strong> : controle vol, navigation</li>
<li><strong>Industrie</strong> : automates, robots, supervision</li>
<li><strong>Medical</strong> : dispositifs implantes, imagerie temps reel</li>
<li><strong>Telecoms</strong> : stations de base 5G</li>
<li><strong>Multimedia</strong> : codecs video, mixage audio</li>
<li><strong>Defense</strong> : systemes d'armes, drones</li>
</ul>

<p>Le marche des systemes embarques et temps reel est enorme et croissant (IoT, voitures connectees, Industry 4.0).</p>

<p><strong>L'avenir</strong> :</p>
<ul>
<li><strong>IA embarquee</strong> : inference reseau neuronal avec contraintes temps reel</li>
<li><strong>Edge computing</strong> : traitement local temps reel (vs cloud)</li>
<li><strong>Systemes cyber-physiques</strong> : integration software/hardware/physique</li>
<li><strong>Securite</strong> : temps reel + cybersecurite (defis combines)</li>
</ul>

<p>Les competences en temps reel resteront critiques. Meme avec processeurs plus rapides, les applications deviennent plus complexes et exigeantes.</p>

<p>En conclusion, ce cours sur les systemes temps reel fournit les bases essentielles pour concevoir des systemes embarques fiables respectant des contraintes temporelles strictes. C'est un domaine exigeant, combinant theorie (ordonnancement) et pratique (RTOS, Xenomai), crucial dans de nombreux secteurs industriels.</p>

<hr/>

<h2>Rapports et Projets</h2>

</div>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">Rapport de Projet Temps Reel</span>
        <span class="lang-en">Real-Time Project Report</span>
      </h4>
      <p>
        <span class="lang-fr">Rapport du projet temps reel : conception et implementation d'un systeme multitaches avec contraintes temporelles strictes, ordonnancement et synchronisation.</span>
        <span class="lang-en">Real-time project report: design and implementation of a multitasking system with strict timing constraints, scheduling and synchronization.</span>
      </p>
      <p style="text-align: center;">
        <a href="/file/reports/S8/Rapport_de_projet_temps_réel_FISA_Paris_Chanfreau.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          <span class="lang-fr">Telecharger le rapport PDF</span>
          <span class="lang-en">Download the PDF report</span>
        </a>
      </p>
    </div>
  </div>
</div>

<div class="lang-fr">

<hr/>

<h2>Documents de Cours</h2>

</div>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">Polycopie Xenomai</span>
        <span class="lang-en">Xenomai Handout</span>
      </h4>
      <p>
        <span class="lang-fr">Guide complet sur Xenomai : installation, APIs temps reel, taches periodiques, synchronisation et debogage.</span>
        <span class="lang-en">Complete guide on Xenomai: installation, real-time APIs, periodic tasks, synchronization and debugging.</span>
      </p>
      <div class="pdf-lazy" data-src="/cours-pdf/S8/Temps-Reel/polycopie-xenomai.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S8/Temps-Reel/polycopie-xenomai.pdf" target="_blank">
        <span class="lang-fr">Telecharger</span>
        <span class="lang-en">Download</span>
      </a></p>
    </div>
  </div>
</div>

<div class="lang-fr">

<hr/>

<p><em>Cours suivi en 2023-2024 a l'INSA Toulouse, Departement Genie Electrique et Informatique.</em></p>

</div>

<div class="lang-en">

<h1>Real-Time Systems</h1>

<p><strong>Related courses</strong>:</p>
<ul>
<li><a href="./commande-numerique.html">Digital Control - S8</a> - Digital control laws</li>
<li><a href="./reseaux-petri.html">Petri Nets - S8</a> - Real-time system modeling</li>
</ul>

<hr/>

<h2>PART A: GENERALITIES</h2>

<h3>Presentation</h3>
<p>The "Temps Reel" (Real-Time) course deals with computing systems that must react to external events within strict timing constraints. A real-time system must not only produce correct results, but also produce them on time. These systems are ubiquitous: avionics, automotive, robotics, industrial control, telecommunications. The course covers task scheduling, real-time operating systems (RTOS), and design techniques ensuring deadline compliance.</p>

<p><strong>Academic Year</strong>: 2023-2024<br/>
<strong>Semester</strong>: 8<br/>
<strong>Category</strong>: Computer Science / Embedded Systems</p>

<hr/>

<h2>PART B: DESCRIPTIVE PART</h2>

<h3>Experience Details</h3>

<h4>Environment and Context</h4>
<p>The course combined scheduling theory with practical implementation on microcontrollers and RTOS (FreeRTOS, embedded RTOS). We programmed multitasking systems with timing constraints, analyzed their schedulability, and measured real performance. Projects included concrete applications: periodic data acquisition, motor control, real-time communication.</p>

<h4>My Function</h4>
<p>In this course, I was responsible for:</p>
<ul>
<li>Understanding timing constraints (deadlines, periods, jitter)</li>
<li>Analyzing the schedulability of task systems</li>
<li>Implementing multitasking applications on RTOS</li>
<li>Managing shared resources (mutexes, semaphores)</li>
<li>Avoiding deadlocks and priority inversions</li>
<li>Measuring and validating timing performance</li>
<li>Designing systems guaranteeing deadline compliance</li>
</ul>

<h2>PART C: TECHNICAL PART</h2>

<p>This section explores the technical aspects of real-time systems.</p>

<h3>Technical Concepts Learned</h3>

<h4>1. Definitions and Classifications</h4>

<p><strong>Real-Time System</strong>:
A system whose correctness depends not only on the logical result but also on the time at which it is produced.</p>

<p><strong>Classification</strong>:</p>

<p><strong>Hard Real-Time</strong>:
Missed deadline = catastrophe (crash, loss, danger).
Examples: airbag, aircraft autopilot, pacemaker.</p>

<p><strong>Soft Real-Time</strong>:
Missed deadline = quality degradation (occasionally acceptable).
Examples: video streaming, video games, user interface.</p>

<p><strong>Firm Real-Time</strong>:
Missed deadline = useless result but not dangerous.
Examples: certain sensors (lost sample acceptable).</p>

<h4>2. Periodic Task Model</h4>

<p><strong>Task ti</strong> characterized by:</p>
<ul>
<li><strong>Ci</strong>: worst-case execution time (WCET)</li>
<li><strong>Ti</strong>: period (interval between activations)</li>
<li><strong>Di</strong>: relative deadline</li>
<li><strong>Pi</strong>: priority</li>
</ul>

<p><strong>Periodic tasks</strong>:
Activated at t=0, Ti, 2Ti, 3Ti, ...</p>

<p><strong>Constraint</strong>:
Finish before deadline: ti + Di (often Di = Ti)</p>

<p><strong>Utilization factor</strong>:</p>
<pre><code>U = Sum Ci/Ti</code></pre>

<p>Proportion of processor used.</p>

<p><strong>Necessary schedulability condition</strong>:</p>
<pre><code>U &lt;= 1</code></pre>

<p>If U > 1, it is impossible to meet all deadlines.</p>

<h4>3. Fixed-Priority Scheduling</h4>

<p><strong>Rate Monotonic (RM)</strong>:
Priority inversely proportional to the period.
Short period -> high priority.</p>

<p><strong>Schedulability test (Liu &amp; Layland)</strong>:</p>
<pre><code>If U &lt;= n(2^(1/n) - 1) then schedulable by RM</code></pre>

<p>For n->infinity: U &lt;= ln(2) ~ 0.69</p>

<p>Sufficient condition (not necessary).</p>

<p><strong>Exact test</strong> (response time analysis):
For each task ti, compute response time Ri:</p>
<pre><code>Ri = Ci + Sum_j(prio>prioi) ceil(Ri/Tj) x Cj</code></pre>

<p>Iterative resolution.</p>

<p>Schedulable if Ri &lt;= Di for all i.</p>

<p><strong>Deadline Monotonic (DM)</strong>:
If Di != Ti, priority based on deadline.
Short deadline -> high priority.</p>

<p>Optimal for fixed priorities with Di &lt;= Ti.</p>

<h4>4. Dynamic-Priority Scheduling</h4>

<p><strong>Earliest Deadline First (EDF)</strong>:
At every instant, execute the task with the closest absolute deadline.</p>

<p><strong>Optimality</strong>:
EDF is optimal for single-processor systems.
If any algorithm can schedule a system, EDF can.</p>

<p><strong>Schedulability test</strong>:</p>
<pre><code>U &lt;= 1</code></pre>

<p>Necessary AND sufficient condition for EDF with Di = Ti.</p>

<p><strong>Advantages</strong>:</p>
<ul>
<li>Better processor utilization (up to 100%)</li>
<li>Optimal</li>
</ul>

<p><strong>Disadvantages</strong>:</p>
<ul>
<li>Overhead (frequent context switches)</li>
<li>Less predictable behavior under overload</li>
<li>More complex implementation</li>
</ul>

<h4>5. Aperiodic and Sporadic Tasks</h4>

<p><strong>Aperiodic tasks</strong>:
Irregular activations, often without strict deadlines.</p>

<p><strong>Sporadic tasks</strong>:
Irregular activations with minimum interval and deadline.</p>

<p><strong>Servers</strong>:
Mechanisms for integrating aperiodic tasks into a periodic system.</p>

<p><strong>Polling Server</strong>:
Periodic task reserved for aperiodic tasks.</p>

<p><strong>Deferrable Server</strong>:
Capacity preserved if not used.</p>

<p><strong>Sporadic Server</strong>:
Performance/simplicity trade-off.</p>

<h4>6. Synchronization and Shared Resources</h4>

<p><strong>Problem</strong>:
Tasks share resources (variables, peripherals).
Concurrent access -> data corruption.</p>

<p><strong>Critical section</strong>:
Portion of code accessing a shared resource.</p>

<p><strong>Mechanisms</strong>:</p>

<p><strong>Mutex</strong> (Mutual Exclusion):
Lock/Unlock to protect critical sections.</p>

<p><strong>Semaphore</strong>:
Counter controlling access.</p>
<ul>
<li>Binary (0 or 1): like a mutex</li>
<li>Counting: multiple simultaneous accesses (resource pool)</li>
</ul>

<p><strong>Priority inversion</strong>:
High-priority task blocked by low-priority task.</p>

<p><strong>Classic example (Mars Pathfinder)</strong>:
High-priority task blocked indefinitely -> system reset.</p>

<p><strong>Solutions</strong>:</p>

<p><strong>Priority Inheritance Protocol (PIP)</strong>:
Task holding a resource temporarily inherits the priority of the highest-priority blocked task.</p>

<p><strong>Priority Ceiling Protocol (PCP)</strong>:
Resource has a ceiling priority = max priority of tasks using it.
Task accessing resource temporarily acquires this priority.</p>

<p>Prevents multiple priority inversions and deadlocks.</p>

<h4>7. Deadlocks</h4>

<p><strong>Coffman Conditions</strong> (4 necessary):</p>
<ol>
<li><strong>Mutual exclusion</strong>: non-shareable resources</li>
<li><strong>Hold and wait</strong>: task holds resources and waits for others</li>
<li><strong>No preemption</strong>: resources are not preemptible</li>
<li><strong>Circular wait</strong>: cycle in the allocation graph</li>
</ol>

<p><strong>Prevention</strong>:
Break one of the 4 conditions.</p>

<p><strong>Example</strong>: total ordering of resource acquisition (avoids cycles).</p>

<p><strong>Detection and recovery</strong>:
Detect cycles, then kill/restart tasks.
Costly in real-time systems.</p>

<p><strong>Avoidance</strong> (Banker's algorithm):
Only allocate if a safe state is guaranteed.
High overhead, rarely used in real-time systems.</p>

<h4>8. Real-Time Operating Systems (RTOS)</h4>

<p><strong>Characteristics</strong>:</p>
<ul>
<li><strong>Determinism</strong>: predictable timing behavior</li>
<li><strong>Interrupt latency</strong>: low and bounded</li>
<li><strong>Preemptibility</strong>: high-priority task can interrupt lower ones</li>
<li><strong>Priority-based scheduling</strong> (often fixed priorities)</li>
<li><strong>Synchronization primitives</strong> (mutexes, semaphores)</li>
<li><strong>Deterministic memory management</strong> (no unpredictable garbage collector)</li>
</ul>

<p><strong>Popular RTOS</strong>:</p>

<p><strong>FreeRTOS</strong>:</p>
<ul>
<li>Open source</li>
<li>Lightweight (a few KB)</li>
<li>Portable (many microcontrollers)</li>
<li>Simple API</li>
<li>Preemptive fixed-priority scheduling</li>
</ul>

<p><strong>VxWorks</strong>:</p>
<ul>
<li>Commercial (Wind River)</li>
<li>Robust, certified (aerospace, medical)</li>
<li>Feature-rich</li>
</ul>

<p><strong>QNX</strong>:</p>
<ul>
<li>Microkernel</li>
<li>POSIX compliant</li>
<li>Automotive (BlackBerry)</li>
</ul>

<p><strong>RT-Linux / Xenomai</strong>:</p>
<ul>
<li>Real-time extension for Linux</li>
<li>Coexistence of real-time / non-real-time tasks</li>
</ul>

<p><strong>Zephyr</strong>:</p>
<ul>
<li>Open source, modern</li>
<li>IoT and connected objects</li>
</ul>

<h4>9. FreeRTOS API (Examples)</h4>

<p><strong>Task creation</strong>:</p>
<pre><code class="language-c">xTaskCreate(
    vTaskFunction,      // Function pointer
    "TaskName",         // Name (debug)
    STACK_SIZE,         // Stack size
    NULL,               // Parameters
    PRIORITY,           // Priority
    &amp;xTaskHandle        // Handle (optional)
);</code></pre>

<p><strong>Mutex</strong>:</p>
<pre><code class="language-c">xMutex = xSemaphoreCreateMutex();

xSemaphoreTake(xMutex, portMAX_DELAY);  // Lock
// Critical section
xSemaphoreGive(xMutex);  // Unlock</code></pre>

<p><strong>Binary semaphore</strong> (signaling):</p>
<pre><code class="language-c">xSemaphore = xSemaphoreCreateBinary();

// ISR:
xSemaphoreGiveFromISR(xSemaphore, NULL);

// Task:
xSemaphoreTake(xSemaphore, portMAX_DELAY);  // Wait for signal</code></pre>

<p><strong>Queues</strong> (FIFO):</p>
<pre><code class="language-c">xQueue = xQueueCreate(QUEUE_LENGTH, sizeof(DataType));

xQueueSend(xQueue, &amp;data, TIMEOUT);
xQueueReceive(xQueue, &amp;buffer, TIMEOUT);</code></pre>

<p><strong>Delays</strong>:</p>
<pre><code class="language-c">vTaskDelay(pdMS_TO_TICKS(100));  // 100ms delay</code></pre>

<h4>10. Measurement and Validation</h4>

<p><strong>WCET</strong> (Worst-Case Execution Time):
Maximum execution time.</p>

<p><strong>Determination methods</strong>:</p>
<ul>
<li><strong>Measurement</strong>: instrument code, test scenarios</li>
<li><strong>Static analysis</strong>: analyze code, processor model</li>
<li><strong>Hybrid</strong>: combine both</li>
</ul>

<p>Difficult to determine precisely (caches, pipelines, branches).</p>

<p><strong>Safety margins</strong>:
Use overestimated WCET for robustness.</p>

<p><strong>Measurement tools</strong>:</p>
<ul>
<li>Logic oscilloscope</li>
<li>Real-time tracers</li>
<li>GPIO toggling (observe signals)</li>
<li>Hardware counters</li>
</ul>

<p><strong>Validation</strong>:</p>
<ul>
<li>Stress tests (max load)</li>
<li>Fault injection</li>
<li>Long-duration tests (aging)</li>
</ul>

<h4>11. Real-Time System Design</h4>

<p><strong>Methodology</strong>:</p>

<p><strong>1. Specification</strong>:</p>
<ul>
<li>Identify tasks and timing constraints</li>
<li>Periods, deadlines, priorities</li>
</ul>

<p><strong>2. Modeling</strong>:</p>
<ul>
<li>Sequence diagrams</li>
<li>State diagrams</li>
<li>Timed Petri Nets</li>
</ul>

<p><strong>3. Schedulability analysis</strong>:</p>
<ul>
<li>Calculate U</li>
<li>RM/EDF tests</li>
<li>Response time analysis</li>
</ul>

<p><strong>4. Implementation</strong>:</p>
<ul>
<li>RTOS selection</li>
<li>Task coding</li>
<li>Synchronization</li>
</ul>

<p><strong>5. Validation</strong>:</p>
<ul>
<li>Unit tests</li>
<li>Integration tests</li>
<li>Timing measurements</li>
</ul>

<p><strong>6. Optimization</strong>:</p>
<ul>
<li>Reduce WCET (code, compiler)</li>
<li>Adjust priorities</li>
<li>Distribute loads</li>
</ul>

<p><strong>Design patterns</strong>:</p>
<ul>
<li><strong>Cyclic Executive</strong>: infinite loop with static scheduling (simple but inflexible)</li>
<li><strong>Time-Triggered</strong>: activation on timer (deterministic)</li>
<li><strong>Event-Triggered</strong>: activation on events (reactive but less predictable)</li>
</ul>

<h4>12. Challenges and Best Practices</h4>

<p><strong>Challenges</strong>:</p>

<p><strong>Jitter</strong>:
Delay variation (problematic for control, audio).
Minimize through appropriate scheduling.</p>

<p><strong>Overhead</strong>:
Context switches, RTOS management.
Can be significant (10-20%).</p>

<p><strong>Multiprocessor</strong>:
More complex scheduling.
Task partitioning or migration.</p>

<p><strong>Interrupts</strong>:
Can disrupt scheduling.
Limit ISR (Interrupt Service Routine) duration.</p>

<p><strong>Best practices</strong>:</p>

<p><strong>Short ISRs</strong>:
Minimize processing in interrupts.
Use semaphore to unblock a task (deferred processing).</p>

<p><strong>Short critical sections</strong>:
Minimize time mutex is held.</p>

<p><strong>Avoid blocking operations</strong>:
No blocking I/O, no malloc (variable time).</p>

<p><strong>Use deterministic resources</strong>:
Static memory allocation, circular buffers.</p>

<p><strong>Conservative sizing</strong>:
Margins on WCET, processor utilization.</p>

<p><strong>Exhaustive testing</strong>:
Validate all scenarios, boundary conditions.</p>

<h2>PART D: ANALYTICAL PART</h2>

<h3>Knowledge and Skills Mobilized</h3>

<ul>
<li>Scheduling theory</li>
<li>Schedulability analysis (RM, EDF)</li>
<li>Embedded system programming</li>
<li>RTOS usage (FreeRTOS)</li>
<li>Synchronization and shared resource management</li>
<li>Resolving deadlock and priority inversion problems</li>
<li>Timing measurement and validation</li>
<li>Designing systems with real-time constraints</li>
</ul>

<h3>Self Evaluation</h3>

<p>This course was demanding but fascinating. Real-time systems introduce a dimension (time) that radically changes design compared to classical programming.</p>

<p>Scheduling theory is mathematically rigorous. Schedulability tests (RM, EDF) provide formal guarantees, which is reassuring for critical systems. However, determining WCET precisely remains a challenge.</p>

<p>The gap between RM (simple, used in practice) and EDF (optimal but complex) is interesting. The choice depends on the context: critical (RM for predictability) or high performance (EDF for maximum utilization).</p>

<p>Programming with an RTOS was eye-opening. Managing concurrent tasks, synchronization, and priorities requires rigor. Bugs are often subtle (race conditions, deadlocks) and difficult to reproduce.</p>

<p>Priority inversion and its solutions (PIP, PCP) demonstrate the importance of understanding underlying mechanisms. A simple misused mutex can cause catastrophic blocking (cf. Mars Pathfinder).</p>

<p>Timing measurements confronted me with reality: theoretical and measured WCET can differ. Hardware factors (caches, interrupts) complicate predictions.</p>

<p>Designing a real-time system requires a methodical approach: clear specification, formal analysis, exhaustive testing. Improvisation is dangerous.</p>

<h3>My Opinion</h3>

<p>This course is essential for engineers working in embedded systems, control, or developing critical applications.</p>

<p><strong>Strengths</strong>:</p>
<ul>
<li>Solid theory (scheduling)</li>
<li>Hands-on practice with real RTOS (FreeRTOS)</li>
<li>Awareness of pitfalls (priority inversions, deadlocks)</li>
<li>Concrete applications</li>
</ul>

<p><strong>Areas for improvement</strong>:</p>
<ul>
<li>More on multiprocessors (multi-core is ubiquitous)</li>
<li>Static WCET analysis tools</li>
<li>Certification (DO-178C aerospace, ISO 26262 automotive)</li>
<li>Distributed real-time (networks, synchronization)</li>
</ul>

<p><strong>Personal reflections</strong>:</p>

<p>Real-time is not about "being fast" but "being on time". A system that is fast on average but with high variation can be worse than a slower but deterministic system.</p>

<p>Deadline guarantee is more important than average performance. This is a mindset shift compared to classical software development (where the average case is optimized).</p>

<p>Real-time systems are ubiquitous but invisible: ABS in cars, autopilots, industrial controllers, pacemakers. Their reliability is critical because lives depend on them.</p>

<p>Certification (aerospace, medical, automotive) imposes rigorous processes and traceability. Code must be proven correct, not just tested. Formal methods become essential.</p>

<p>Complexity grows with:</p>
<ul>
<li>Multiprocessors (partitioning, communication)</li>
<li>Distributed systems (clocks, network latencies)</li>
<li>Embedded intelligence (real-time AI)</li>
</ul>

<p><strong>Professional applications</strong>:</p>

<p>Real-time skills applicable in:</p>
<ul>
<li><strong>Automotive</strong>: ESP, ABS, ADAS, autonomous vehicles</li>
<li><strong>Aerospace</strong>: flight control, navigation</li>
<li><strong>Industry</strong>: PLCs, robots, supervision</li>
<li><strong>Medical</strong>: implanted devices, real-time imaging</li>
<li><strong>Telecom</strong>: 5G base stations</li>
<li><strong>Multimedia</strong>: video codecs, audio mixing</li>
<li><strong>Defense</strong>: weapon systems, drones</li>
</ul>

<p>The embedded and real-time systems market is huge and growing (IoT, connected cars, Industry 4.0).</p>

<p><strong>The future</strong>:</p>
<ul>
<li><strong>Embedded AI</strong>: neural network inference with real-time constraints</li>
<li><strong>Edge computing</strong>: local real-time processing (vs cloud)</li>
<li><strong>Cyber-physical systems</strong>: software/hardware/physical integration</li>
<li><strong>Security</strong>: real-time + cybersecurity (combined challenges)</li>
</ul>

<p>Real-time skills will remain critical. Even with faster processors, applications are becoming more complex and demanding.</p>

<p>In conclusion, this course on real-time systems provides the essential foundations for designing reliable embedded systems that comply with strict timing constraints. It is a demanding field, combining theory (scheduling) and practice (RTOS, Xenomai), crucial in many industrial sectors.</p>

<hr/>

<h2>Reports and Projects</h2>

<!-- Shared PDF report section above -->

<hr/>

<h2>Course Documents</h2>

<!-- Shared PDF course documents section above -->

<hr/>

<p><em>Course taken in 2023-2024 at INSA Toulouse, Department of Electrical and Computer Engineering.</em></p>

</div>

<div class="back-nav">
    <a href="./my-courses-2023-2024.html" data-i18n-html="back-courses-2023-2024">&larr; Retour aux Cours 2023-2024</a>
</div>

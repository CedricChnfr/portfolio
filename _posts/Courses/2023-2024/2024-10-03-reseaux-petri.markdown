---
layout: default
title: "Réseaux de Pétri - S8"
date: 2024-10-02 10:56:03 +0200
---

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
</style>

<div class="back-nav">
    <a href="./my-courses-2023-2024.html" data-i18n-html="back-courses-2023-2024">&larr; Retour aux Cours 2023-2024</a>
</div>

<div class="lang-fr">

<h1>Reseaux de Petri</h1>

<h2>PARTIE A : GENERALITES</h2>

<h3>Presentation</h3>
<p>Le cours "Reseaux de Petri" introduit un formalisme graphique et mathematique puissant pour modeliser, analyser, et valider les systemes a evenements discrets (SED). Les reseaux de Petri sont particulierement adaptes pour representer des systemes avec concurrence, synchronisation, et partage de ressources. Ils sont utilises en automatique, informatique, logistique, et de nombreux autres domaines.</p>

<p><strong>Annee Universitaire</strong> : 2023-2024<br/>
<strong>Semestre</strong> : 8<br/>
<strong>Categorie</strong> : Automatique / Systemes a Evenements Discrets</p>

<hr/>

<h2>PARTIE B : PARTIE DESCRIPTIVE</h2>

<h3>Details de l'experience</h3>

<h4>Environnement et contexte</h4>
<p>Le cours combinait theorie formelle (algebre, theorie des graphes) avec applications pratiques via des outils logiciels de modelisation et simulation (PIPE, Tina). Nous avons modelise des systemes varies: systemes de production, protocoles de communication, workflows, et analyse leurs proprietes (vivacite, bornitude, absence de blocage).</p>

<h4>Ma fonction</h4>
<p>Dans ce cours, j'ai ete responsable de :</p>
<ul>
<li>Comprendre la syntaxe et semantique des reseaux de Petri</li>
<li>Modeliser des systemes concurrents et distribues</li>
<li>Analyser les proprietes structurelles et comportementales</li>
<li>Utiliser l'equation d'etat et invariants</li>
<li>Verifier proprietes (vivacite, bornitude, reversibilite)</li>
<li>Simuler et valider des modeles</li>
<li>Appliquer les extensions (temporises, colores, stochastiques)</li>
<li>Utiliser les reseaux de Petri pour concevoir et valider des systemes de commande</li>
</ul>

<h2>PARTIE C : PARTIE TECHNIQUE</h2>

<p>Cette section explore les aspects techniques des reseaux de Petri.</p>

<h3>Concepts techniques appris</h3>

<h4>1. Definition et Syntaxe</h4>

<p><strong>Reseau de Petri</strong> R = (P, T, Pre, Post) :</p>
<ul>
<li><strong>P</strong> : ensemble de places (etats, ressources)</li>
<li><strong>T</strong> : ensemble de transitions (evenements, actions)</li>
<li><strong>Pre</strong> : P x T &rarr; N (arcs des places vers transitions, poids)</li>
<li><strong>Post</strong> : T x P &rarr; N (arcs des transitions vers places, poids)</li>
</ul>

<p><strong>Representation graphique</strong> :</p>
<ul>
<li>Places : cercles</li>
<li>Transitions : rectangles (ou barres)</li>
<li>Arcs : fleches avec poids (1 si omis)</li>
<li>Jetons (tokens) : points noirs dans places</li>
</ul>

<p><strong>Marquage</strong> M : P &rarr; N</p>
<p>Fonction indiquant nombre de jetons dans chaque place. M0 = marquage initial.</p>

<h4>2. Regles de Franchissement</h4>

<p><strong>Transition t est franchissable</strong> (enabled) ssi :</p>
<pre><code>&forall;p &isin; P: M(p) &ge; Pre(p,t)</code></pre>

<p>Assez de jetons dans chaque place d'entree.</p>

<p><strong>Franchissement</strong> de t :</p>
<pre><code>M' = M - Pre(&middot;,t) + Post(t,&middot;)</code></pre>

<p>On retire Pre(p,t) jetons de chaque place p, on ajoute Post(t,p).</p>

<p><strong>Notation</strong> : M &rarr;t M'</p>

<p><strong>Sequence de franchissement</strong> :</p>
<pre><code>M0 &rarr;t1 M1 &rarr;t2 M2 &rarr; ... &rarr;tn Mn</code></pre>

<h4>3. Graphe de Marquage</h4>

<p><strong>Ensemble d'accessibilite</strong> R(M0) :</p>
<p>Ensemble de tous les marquages atteignables depuis M0.</p>

<p><strong>Graphe de marquage</strong> :</p>
<ul>
<li>Sommets : marquages</li>
<li>Arcs : transitions</li>
</ul>

<p>Representation de l'espace d'etats.</p>

<p><strong>Probleme</strong> : explosion combinatoire (nombre de marquages peut etre exponentiel).</p>

<h4>4. Proprietes Comportementales</h4>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S8/reseaux-petri/reseau-petri.svg" alt="Reseau de Petri avec jetons"
       style="max-width: 500px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Exemple de reseau de Petri avec places, transitions et jetons</p>
</div>

<p><strong>Bornitude</strong> :</p>
<p>&exist; k tel que &forall;M &isin; R(M0), &forall;p &isin; P : M(p) &le; k</p>

<p>Systeme borne : nombre de jetons limite. Important : evite debordements (buffers, files).</p>

<p><strong>1-sur</strong> (safe) : borne par 1.</p>

<p><strong>Vivacite</strong> (liveness) :</p>
<p>Une transition est vivante si elle peut toujours redevenir franchissable.</p>

<p><strong>Niveaux de vivacite</strong> :</p>
<ul>
<li>L0 (mort) : jamais franchissable</li>
<li>L1 (potentiellement franchissable) : franchissable au moins une fois</li>
<li>L2 : peut etre franchie infiniment sur une sequence</li>
<li>L3 : peut etre franchie infiniment souvent (sur toute sequence infinie)</li>
<li>L4 (vivante) : franchissable depuis tout marquage accessible</li>
</ul>

<p><strong>Reseau vivant</strong> : toutes transitions L4-vivantes.</p>

<p><strong>Blocage</strong> (deadlock) :</p>
<p>Marquage M ou aucune transition n'est franchissable.</p>

<p><strong>Reversibilite</strong> :</p>
<p>&forall;M &isin; R(M0) : M0 &isin; R(M)</p>
<p>On peut toujours revenir a l'etat initial.</p>

<p><strong>Quasi-vivacite</strong> :</p>
<p>&forall;t &isin; T, &exist;M &isin; R(M0) : t franchissable depuis M.</p>
<p>Toute transition peut etre franchie au moins une fois.</p>

<h4>5. Equation d'Etat</h4>

<p><strong>Matrice d'incidence</strong> C :</p>
<pre><code>C = Post^T - Pre^T</code></pre>
<p>C(t,p) = gain net de jetons dans p par franchissement de t.</p>

<p><strong>Equation d'etat fondamentale</strong> :</p>
<pre><code>M = M0 + C^T &middot; &sigma;</code></pre>
<p>Ou &sigma; est le vecteur de franchissement (nombre de fois chaque transition a ete franchie).</p>

<p><strong>Usage</strong> :</p>
<p>Condition necessaire (mais pas suffisante) d'accessibilite. Si M inaccessible, alors pas de solution entiere positive a l'equation.</p>

<h4>6. Invariants</h4>

<p><strong>P-invariants</strong> (invariants de places) :</p>
<p>Vecteur y &ge; 0 tel que :</p>
<pre><code>C &middot; y = 0</code></pre>

<p><strong>Interpretation</strong> :</p>
<pre><code>y^T &middot; M = y^T &middot; M0 = constante</code></pre>
<p>Combinaison ponderee de jetons conservee.</p>

<p><strong>Exemple</strong> : conservation de ressources.</p>

<p><strong>T-invariants</strong> (invariants de transitions) :</p>
<p>Vecteur x &ge; 0 tel que :</p>
<pre><code>C^T &middot; x = 0</code></pre>

<p><strong>Interpretation</strong> :</p>
<p>Sequence de transitions ramenant au meme marquage. Si x franchissable depuis M, alors M &rarr;* M.</p>

<p><strong>Usage</strong> : cycles, comportements repetitifs.</p>

<p><strong>Reseau couvert par P-invariants</strong> :</p>
<p>Toute place appartient a au moins un P-invariant. &rArr; Reseau borne.</p>

<h4>7. Sous-Classes de Reseaux</h4>

<p><strong>Graphe d'etats</strong> :</p>
<p>Chaque transition a exactement une place d'entree et une de sortie. Modelise automates finis.</p>

<p><strong>Graphe d'evenements</strong> :</p>
<p>Chaque place a exactement une transition d'entree et une de sortie. Modelise synchronisation.</p>

<p><strong>Reseau libre choix</strong> (free choice) :</p>
<p>Si deux transitions partagent place d'entree, elles ont meme ensemble de places d'entree. Simplifie analyse.</p>

<p><strong>Reseau sauf</strong> (safe) :</p>
<p>1-borne.</p>

<h4>8. Extensions des Reseaux de Petri</h4>

<p><strong>Reseaux de Petri Temporises</strong> (TPN) :</p>
<p>Ajout du temps : delais sur transitions ou durees de franchissement.</p>

<p><strong>Types</strong> :</p>
<ul>
<li><strong>P-temporise</strong> : jetons ont age minimal avant utilisation</li>
<li><strong>T-temporise</strong> : transition franchit apres delai</li>
</ul>

<p><strong>Analyse</strong> : plus complexe (espace d'etats infini). Classes d'etats, automates temporises.</p>

<p><strong>Reseaux de Petri Colores</strong> (CPN) :</p>
<p>Jetons ont "couleurs" (types, attributs).</p>

<p><strong>Avantages</strong> :</p>
<ul>
<li>Modele compact (un jeton colore represente plusieurs jetons classiques)</li>
<li>Donnees structurees</li>
</ul>

<p><strong>Outil</strong> : CPN Tools</p>

<p><strong>Reseaux de Petri Stochastiques</strong> (SPN) :</p>
<p>Transitions avec taux de franchissement (lois exponentielles).</p>

<p><strong>Usage</strong> : evaluation de performances (comme files d'attente). Equivalent a chaines de Markov continues.</p>

<p><strong>Reseaux de Petri Hybrides</strong> :</p>
<p>Variables continues et discretes. Modelise systemes hybrides (manufacturiers, thermiques, etc.).</p>

<h4>9. Analyse par Reduction</h4>

<p><strong>Transformations preservant proprietes</strong> :</p>

<p><strong>Fusion de places paralleles</strong> :</p>
<p>Places avec memes transitions amont/aval.</p>

<p><strong>Fusion de transitions paralleles</strong> :</p>
<p>Transitions avec memes places amont/aval.</p>

<p><strong>Elimination de places implicites</strong> :</p>
<p>Place dont marquage toujours suffit (contrainte redondante).</p>

<p><strong>Elimination de transitions</strong> :</p>
<p>Sous certaines conditions (ne change pas comportement).</p>

<p><strong>Objectif</strong> : simplifier modele avant analyse.</p>

<h4>10. Outils Logiciels</h4>

<p><strong>PIPE</strong> (Platform Independent Petri net Editor) :</p>
<ul>
<li>Modelisation graphique</li>
<li>Simulation</li>
<li>Analyse (graphe de marquage, invariants)</li>
<li>Java, open source</li>
</ul>

<p><strong>Tina</strong> :</p>
<ul>
<li>Construction graphe de marquage</li>
<li>Verification proprietes temporelles (CTL)</li>
<li>Synthese de controleurs</li>
</ul>

<p><strong>CPN Tools</strong> :</p>
<ul>
<li>Pour reseaux colores</li>
<li>Simulation, state space analysis</li>
</ul>

<p><strong>ROMEO</strong> :</p>
<ul>
<li>Reseaux temporises avec stopwatches</li>
<li>Temps dense</li>
</ul>

<p><strong>GreatSPN</strong> :</p>
<ul>
<li>Stochastiques</li>
<li>Evaluation de performances</li>
</ul>

<h4>11. Commande par Reseaux de Petri</h4>

<p><strong>Synthese de controleurs</strong> :</p>

<p><strong>Probleme</strong> : systeme (plante) + specifications &rarr; controleur</p>

<p><strong>Approches</strong> :</p>

<p><strong>Theorie de la supervision</strong> :</p>
<p>Desactiver transitions interdites pour respecter specifications.</p>

<p><strong>Controle par place de controle</strong> :</p>
<p>Ajouter places (avec arcs) pour imposer contraintes.</p>

<p><strong>Exemple</strong> : eviter blocage, limiter nombre de pieces en cours (WIP).</p>

<p><strong>Applications</strong> :</p>
<ul>
<li>Systemes de production flexibles (FMS)</li>
<li>Workflows</li>
<li>Protocoles de communication</li>
</ul>

<h4>12. Applications</h4>

<p><strong>Systemes de production</strong> :</p>
<ul>
<li>Modeliser lignes de fabrication</li>
<li>Partage de ressources (machines, robots)</li>
<li>Ordonnancement</li>
<li>Detection de blocages</li>
</ul>

<p><strong>Protocoles de communication</strong> :</p>
<ul>
<li>Handshake, synchronisation</li>
<li>Detection d'interblocages</li>
<li>Verification de protocoles</li>
</ul>

<p><strong>Workflows</strong> :</p>
<ul>
<li>Processus metier</li>
<li>Gestion de documents</li>
<li>Validation de processus</li>
</ul>

<p><strong>Systemes informatiques</strong> :</p>
<ul>
<li>Allocation memoire</li>
<li>Synchronisation de threads</li>
<li>Gestion de transactions</li>
</ul>

<p><strong>Systemes embarques</strong> :</p>
<ul>
<li>Controle concurrent</li>
<li>Verification avant implementation</li>
</ul>

<h2>PARTIE D : PARTIE ANALYTIQUE</h2>

<h3>Connaissances et competences mobilisees</h3>

<ul>
<li>Comprehension des systemes a evenements discrets</li>
<li>Modelisation graphique et formelle</li>
<li>Algebre lineaire (matrices, invariants)</li>
<li>Theorie des graphes</li>
<li>Analyse de proprietes (vivacite, bornitude)</li>
<li>Utilisation d'outils logiciels de simulation</li>
<li>Verification formelle</li>
<li>Synthese de lois de commande</li>
</ul>

<h3>Auto-evaluation</h3>

<p>Ce cours a ete mathematiquement riche et conceptuellement dense. Les reseaux de Petri sont un formalisme elegant mais necessitent un changement de paradigme par rapport aux systemes continus etudies precedemment.</p>

<p>La representation graphique est intuitive et pedagogique. Visualiser les jetons circuler dans le reseau aide a comprendre la dynamique. Cependant, passer du graphique au formel (matrices, equations) demande rigueur.</p>

<p>L'analyse des proprietes (vivacite, bornitude) est cruciale pour valider un systeme. Un modele qui bloque ou dont les files explosent est inutilisable. Les methodes d'analyse (graphe de marquage, invariants) fournissent des outils rigoureux.</p>

<p>Le graphe de marquage est conceptuellement simple mais peut devenir gigantesque (explosion combinatoire). C'est une limite pratique importante. Les techniques de reduction et les analyses partielles (invariants sans construire tout le graphe) sont essentielles.</p>

<p>Les invariants (P et T) sont puissants. Les P-invariants permettent de prouver la bornitude elegamment. Les T-invariants revelent les cycles et comportements repetitifs.</p>

<p>L'equation d'etat (M = M0 + C^T&sigma;) est centrale. Elle offre une condition necessaire d'accessibilite calculable algebriquement, sans explorer tous les etats.</p>

<p>Les extensions (temporises, colores, stochastiques) augmentent l'expressivite mais complexifient l'analyse. Il y a un trade-off entre pouvoir de modelisation et analysabilite.</p>

<p>La synthese de controleurs par theorie de la supervision ouvre des perspectives interessantes pour automatiser la conception de systemes surs.</p>

<p>Les outils logiciels (PIPE, Tina) sont indispensables pour traiter des reseaux realistes. Modeliser a la main est formateur mais limite a des exemples jouets.</p>

<p>Les applications sont nombreuses et variees. Cela montre la generalite du formalisme. Tout systeme avec evenements, concurrence, et ressources partagees peut beneficier d'une modelisation par reseau de Petri.</p>

<h3>Mon avis</h3>

<p>Ce cours fournit des outils puissants pour les systemes a evenements discrets, complementaires aux techniques continues. Il est essentiel pour l'automaticien travaillant sur systemes manufacturiers, protocoles, ou systemes embarques.</p>

<p>Points forts :</p>
<ul>
<li>Formalisme rigoureux et visuel</li>
<li>Analyse de proprietes critiques (vivacite, absence de blocage)</li>
<li>Applicabilite large</li>
<li>Outils logiciels disponibles</li>
</ul>

<p>Points a ameliorer :</p>
<ul>
<li>Plus de cas d'etudes industriels complexes</li>
<li>Lien avec implementation (code genere depuis modele)</li>
<li>Comparaison avec autres formalismes (automates, algebre de processus)</li>
<li>Techniques pour gerer explosion combinatoire</li>
</ul>

<p>Reflexions personnelles :</p>

<p>Les reseaux de Petri sont un langage graphique universel pour SED. Leur avantage majeur est l'integration de la modelisation, simulation, et verification formelle dans un meme cadre.</p>

<p>La verification formelle est cruciale pour systemes critiques (aerospatial, medical, nucleaire). Prouver mathematiquement l'absence de blocage ou de depassement de capacite evite bugs catastrophiques.</p>

<p>Cependant, l'explosion combinatoire reste le defi majeur. Pour systemes realistes de grande taille, le graphe de marquage complet est incalculable. Les techniques d'abstraction, reduction, et verification symbolique sont des recherches actives.</p>

<p>La modularite et composabilite des reseaux de Petri sont limitees. Combiner plusieurs sous-reseaux peut etre ardu. Les reseaux colores et hierarchiques aident mais la complexite reste.</p>

<p>Le lien avec l'implementation est parfois flou. Modeliser c'est bien, mais comment passer du modele au code (PLC, microcontroleur)? La generation automatique de code depuis reseaux de Petri existe mais n'est pas standard.</p>

<p>Applications professionnelles :</p>

<p>Competences en reseaux de Petri applicables dans :</p>
<ul>
<li><strong>Automatisation industrielle</strong> : conception et validation systemes de production</li>
<li><strong>Conception systemes embarques</strong> : verification proprietes temps reel</li>
<li><strong>Reseaux de communication</strong> : protocoles, gestion ressources</li>
<li><strong>Logiciels</strong> : modelisation workflows, processus metier</li>
<li><strong>Recherche</strong> : formalisation et analyse de systemes complexes</li>
</ul>

<p>Le marche :</p>
<p>Moins mainstream que controle continu ou programmation classique. Niche dans domaines critiques necessitant verification formelle. Competence differenciante pour ingenieurs systemes complexes.</p>

<p>L'avenir :</p>
<ul>
<li>Integration avec Model-Based Design (Simulink, etc.)</li>
<li>Codesign hardware/software</li>
<li>Verification de systemes cyber-physiques</li>
<li>IA et apprentissage : synthese automatique de modeles depuis donnees</li>
</ul>

<p>En conclusion, les reseaux de Petri sont un formalisme puissant pour modeliser, analyser et verifier des systemes a evenements discrets. Ils completent les automates et les langages de description (GRAFCET, Statecharts) en offrant une semantique mathematique rigoureuse et des outils d'analyse formelle. Ils restent utilises en recherche et dans l'industrie pour les systemes critiques.</p>

<hr/>

<h2>Documents de Cours</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Cours Complet Reseaux de Petri</h4>
      <p>Cours complet : modelisation, proprietes structurelles et comportementales, analyse de vivacite et blocage.</p>
      <embed src="/cours-pdf/S8/Reseaux-Petri/cours-complet.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S8/Reseaux-Petri/cours-complet.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>Examen 2023</h4>
      <p>Sujet d'examen 2023 : construction de reseaux, calcul d'invariants, analyse de blocage et synthese.</p>
      <embed src="/cours-pdf/S8/Reseaux-Petri/exam-2023.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S8/Reseaux-Petri/exam-2023.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>Correction 2023</h4>
      <p>Correction complete de l'examen 2023 avec methodes d'analyse et explications detaillees.</p>
      <embed src="/cours-pdf/S8/Reseaux-Petri/correction-2023.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S8/Reseaux-Petri/correction-2023.pdf" target="_blank">Telecharger</a></p>
    </div>
  </div>
</div>

</div>

<div class="lang-en">

<h1>Petri Nets</h1>

<h2>PART A: GENERALITIES</h2>

<h3>Presentation</h3>
<p>The "Petri Nets" course introduces a powerful graphical and mathematical formalism for modeling, analyzing, and validating discrete event systems (DES). Petri nets are particularly suited for representing systems with concurrency, synchronization, and resource sharing. They are used in control engineering, computer science, logistics, and many other fields.</p>

<p><strong>Academic Year</strong>: 2023-2024<br/>
<strong>Semester</strong>: 8<br/>
<strong>Category</strong>: Control Engineering / Discrete Event Systems</p>

<hr/>

<h2>PART B: DESCRIPTIVE PART</h2>

<h3>Experience Details</h3>

<h4>Environment and Context</h4>
<p>The course combined formal theory (algebra, graph theory) with practical applications using modeling and simulation software tools (PIPE, Tina). We modeled various systems: production systems, communication protocols, workflows, and analyzed their properties (liveness, boundedness, deadlock-freeness).</p>

<h4>My Function</h4>
<p>In this course, I was responsible for:</p>
<ul>
<li>Understanding the syntax and semantics of Petri nets</li>
<li>Modeling concurrent and distributed systems</li>
<li>Analyzing structural and behavioral properties</li>
<li>Using the state equation and invariants</li>
<li>Verifying properties (liveness, boundedness, reversibility)</li>
<li>Simulating and validating models</li>
<li>Applying extensions (timed, colored, stochastic)</li>
<li>Using Petri nets to design and validate control systems</li>
</ul>

<h2>PART C: TECHNICAL PART</h2>

<p>This section explores the technical aspects of Petri nets.</p>

<h3>Technical Concepts Learned</h3>

<h4>1. Definition and Syntax</h4>

<p><strong>Petri Net</strong> R = (P, T, Pre, Post):</p>
<ul>
<li><strong>P</strong>: set of places (states, resources)</li>
<li><strong>T</strong>: set of transitions (events, actions)</li>
<li><strong>Pre</strong>: P x T &rarr; N (arcs from places to transitions, weights)</li>
<li><strong>Post</strong>: T x P &rarr; N (arcs from transitions to places, weights)</li>
</ul>

<p><strong>Graphical representation</strong>:</p>
<ul>
<li>Places: circles</li>
<li>Transitions: rectangles (or bars)</li>
<li>Arcs: arrows with weights (1 if omitted)</li>
<li>Tokens: black dots inside places</li>
</ul>

<p><strong>Marking</strong> M: P &rarr; N</p>
<p>Function indicating the number of tokens in each place. M0 = initial marking.</p>

<h4>2. Firing Rules</h4>

<p><strong>Transition t is fireable</strong> (enabled) iff:</p>
<pre><code>&forall;p &isin; P: M(p) &ge; Pre(p,t)</code></pre>

<p>Enough tokens in each input place.</p>

<p><strong>Firing</strong> of t:</p>
<pre><code>M' = M - Pre(&middot;,t) + Post(t,&middot;)</code></pre>

<p>We remove Pre(p,t) tokens from each place p, and add Post(t,p).</p>

<p><strong>Notation</strong>: M &rarr;t M'</p>

<p><strong>Firing sequence</strong>:</p>
<pre><code>M0 &rarr;t1 M1 &rarr;t2 M2 &rarr; ... &rarr;tn Mn</code></pre>

<h4>3. Reachability Graph</h4>

<p><strong>Reachability set</strong> R(M0):</p>
<p>Set of all markings reachable from M0.</p>

<p><strong>Reachability graph</strong>:</p>
<ul>
<li>Nodes: markings</li>
<li>Edges: transitions</li>
</ul>

<p>Representation of the state space.</p>

<p><strong>Problem</strong>: combinatorial explosion (number of markings can be exponential).</p>

<h4>4. Behavioral Properties</h4>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S8/reseaux-petri/reseau-petri.svg" alt="Petri Net with tokens"
       style="max-width: 500px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Example of a Petri net with places, transitions, and tokens</p>
</div>

<p><strong>Boundedness</strong>:</p>
<p>&exist; k such that &forall;M &isin; R(M0), &forall;p &isin; P: M(p) &le; k</p>

<p>Bounded system: limited number of tokens. Important: prevents overflows (buffers, queues).</p>

<p><strong>1-safe</strong>: bounded by 1.</p>

<p><strong>Liveness</strong>:</p>
<p>A transition is live if it can always become fireable again.</p>

<p><strong>Liveness levels</strong>:</p>
<ul>
<li>L0 (dead): never fireable</li>
<li>L1 (potentially fireable): fireable at least once</li>
<li>L2: can be fired infinitely along some sequence</li>
<li>L3: can be fired infinitely often (along every infinite sequence)</li>
<li>L4 (live): fireable from any reachable marking</li>
</ul>

<p><strong>Live net</strong>: all transitions are L4-live.</p>

<p><strong>Deadlock</strong>:</p>
<p>A marking M where no transition is fireable.</p>

<p><strong>Reversibility</strong>:</p>
<p>&forall;M &isin; R(M0): M0 &isin; R(M)</p>
<p>It is always possible to return to the initial state.</p>

<p><strong>Quasi-liveness</strong>:</p>
<p>&forall;t &isin; T, &exist;M &isin; R(M0): t is fireable from M.</p>
<p>Every transition can be fired at least once.</p>

<h4>5. State Equation</h4>

<p><strong>Incidence matrix</strong> C:</p>
<pre><code>C = Post^T - Pre^T</code></pre>
<p>C(t,p) = net token gain in p by firing t.</p>

<p><strong>Fundamental state equation</strong>:</p>
<pre><code>M = M0 + C^T &middot; &sigma;</code></pre>
<p>Where &sigma; is the firing vector (number of times each transition has been fired).</p>

<p><strong>Usage</strong>:</p>
<p>Necessary (but not sufficient) condition for reachability. If M is unreachable, then there is no non-negative integer solution to the equation.</p>

<h4>6. Invariants</h4>

<p><strong>P-invariants</strong> (place invariants):</p>
<p>Vector y &ge; 0 such that:</p>
<pre><code>C &middot; y = 0</code></pre>

<p><strong>Interpretation</strong>:</p>
<pre><code>y^T &middot; M = y^T &middot; M0 = constant</code></pre>
<p>Weighted combination of tokens is conserved.</p>

<p><strong>Example</strong>: resource conservation.</p>

<p><strong>T-invariants</strong> (transition invariants):</p>
<p>Vector x &ge; 0 such that:</p>
<pre><code>C^T &middot; x = 0</code></pre>

<p><strong>Interpretation</strong>:</p>
<p>Firing sequence that returns to the same marking. If x is fireable from M, then M &rarr;* M.</p>

<p><strong>Usage</strong>: cycles, repetitive behaviors.</p>

<p><strong>Net covered by P-invariants</strong>:</p>
<p>Every place belongs to at least one P-invariant. &rArr; Bounded net.</p>

<h4>7. Petri Net Subclasses</h4>

<p><strong>State graph</strong>:</p>
<p>Each transition has exactly one input place and one output place. Models finite automata.</p>

<p><strong>Event graph</strong>:</p>
<p>Each place has exactly one input transition and one output transition. Models synchronization.</p>

<p><strong>Free choice net</strong>:</p>
<p>If two transitions share an input place, they have the same set of input places. Simplifies analysis.</p>

<p><strong>Safe net</strong>:</p>
<p>1-bounded.</p>

<h4>8. Petri Net Extensions</h4>

<p><strong>Timed Petri Nets</strong> (TPN):</p>
<p>Addition of time: delays on transitions or firing durations.</p>

<p><strong>Types</strong>:</p>
<ul>
<li><strong>P-timed</strong>: tokens have a minimum age before use</li>
<li><strong>T-timed</strong>: transition fires after a delay</li>
</ul>

<p><strong>Analysis</strong>: more complex (infinite state space). State classes, timed automata.</p>

<p><strong>Colored Petri Nets</strong> (CPN):</p>
<p>Tokens have "colors" (types, attributes).</p>

<p><strong>Advantages</strong>:</p>
<ul>
<li>Compact model (one colored token represents multiple classic tokens)</li>
<li>Structured data</li>
</ul>

<p><strong>Tool</strong>: CPN Tools</p>

<p><strong>Stochastic Petri Nets</strong> (SPN):</p>
<p>Transitions with firing rates (exponential distributions).</p>

<p><strong>Usage</strong>: performance evaluation (like queuing systems). Equivalent to continuous-time Markov chains.</p>

<p><strong>Hybrid Petri Nets</strong>:</p>
<p>Continuous and discrete variables. Models hybrid systems (manufacturing, thermal, etc.).</p>

<h4>9. Analysis by Reduction</h4>

<p><strong>Property-preserving transformations</strong>:</p>

<p><strong>Fusion of parallel places</strong>:</p>
<p>Places with the same upstream/downstream transitions.</p>

<p><strong>Fusion of parallel transitions</strong>:</p>
<p>Transitions with the same upstream/downstream places.</p>

<p><strong>Elimination of implicit places</strong>:</p>
<p>Place whose marking is always sufficient (redundant constraint).</p>

<p><strong>Elimination of transitions</strong>:</p>
<p>Under certain conditions (does not change behavior).</p>

<p><strong>Objective</strong>: simplify the model before analysis.</p>

<h4>10. Software Tools</h4>

<p><strong>PIPE</strong> (Platform Independent Petri net Editor):</p>
<ul>
<li>Graphical modeling</li>
<li>Simulation</li>
<li>Analysis (reachability graph, invariants)</li>
<li>Java, open source</li>
</ul>

<p><strong>Tina</strong>:</p>
<ul>
<li>Reachability graph construction</li>
<li>Temporal property verification (CTL)</li>
<li>Controller synthesis</li>
</ul>

<p><strong>CPN Tools</strong>:</p>
<ul>
<li>For colored nets</li>
<li>Simulation, state space analysis</li>
</ul>

<p><strong>ROMEO</strong>:</p>
<ul>
<li>Timed nets with stopwatches</li>
<li>Dense time</li>
</ul>

<p><strong>GreatSPN</strong>:</p>
<ul>
<li>Stochastic nets</li>
<li>Performance evaluation</li>
</ul>

<h4>11. Control Using Petri Nets</h4>

<p><strong>Controller synthesis</strong>:</p>

<p><strong>Problem</strong>: system (plant) + specifications &rarr; controller</p>

<p><strong>Approaches</strong>:</p>

<p><strong>Supervisory control theory</strong>:</p>
<p>Disable forbidden transitions to satisfy specifications.</p>

<p><strong>Control by control place</strong>:</p>
<p>Add places (with arcs) to enforce constraints.</p>

<p><strong>Example</strong>: avoid deadlock, limit work-in-progress (WIP).</p>

<p><strong>Applications</strong>:</p>
<ul>
<li>Flexible manufacturing systems (FMS)</li>
<li>Workflows</li>
<li>Communication protocols</li>
</ul>

<h4>12. Applications</h4>

<p><strong>Production systems</strong>:</p>
<ul>
<li>Modeling manufacturing lines</li>
<li>Resource sharing (machines, robots)</li>
<li>Scheduling</li>
<li>Deadlock detection</li>
</ul>

<p><strong>Communication protocols</strong>:</p>
<ul>
<li>Handshake, synchronization</li>
<li>Deadlock detection</li>
<li>Protocol verification</li>
</ul>

<p><strong>Workflows</strong>:</p>
<ul>
<li>Business processes</li>
<li>Document management</li>
<li>Process validation</li>
</ul>

<p><strong>Computer systems</strong>:</p>
<ul>
<li>Memory allocation</li>
<li>Thread synchronization</li>
<li>Transaction management</li>
</ul>

<p><strong>Embedded systems</strong>:</p>
<ul>
<li>Concurrent control</li>
<li>Verification before implementation</li>
</ul>

<h2>PART D: ANALYTICAL PART</h2>

<h3>Knowledge and Skills Mobilized</h3>

<ul>
<li>Understanding of discrete event systems</li>
<li>Graphical and formal modeling</li>
<li>Linear algebra (matrices, invariants)</li>
<li>Graph theory</li>
<li>Property analysis (liveness, boundedness)</li>
<li>Use of simulation software tools</li>
<li>Formal verification</li>
<li>Control law synthesis</li>
</ul>

<h3>Self Evaluation</h3>

<p>This course was mathematically rich and conceptually dense. Petri nets are an elegant formalism but require a paradigm shift compared to the continuous systems studied previously.</p>

<p>The graphical representation is intuitive and pedagogical. Visualizing tokens flowing through the net helps understand the dynamics. However, transitioning from graphical to formal (matrices, equations) requires rigor.</p>

<p>Analyzing properties (liveness, boundedness) is crucial for validating a system. A model that deadlocks or whose queues overflow is unusable. The analysis methods (reachability graph, invariants) provide rigorous tools.</p>

<p>The reachability graph is conceptually simple but can become gigantic (combinatorial explosion). This is a significant practical limitation. Reduction techniques and partial analyses (invariants without building the entire graph) are essential.</p>

<p>Invariants (P and T) are powerful. P-invariants elegantly prove boundedness. T-invariants reveal cycles and repetitive behaviors.</p>

<p>The state equation (M = M0 + C^T&sigma;) is central. It offers a necessary condition for reachability that is algebraically computable, without exploring all states.</p>

<p>Extensions (timed, colored, stochastic) increase expressiveness but complicate analysis. There is a trade-off between modeling power and analyzability.</p>

<p>Controller synthesis through supervisory control theory opens interesting perspectives for automating the design of safe systems.</p>

<p>Software tools (PIPE, Tina) are essential for handling realistic nets. Manual modeling is educational but limited to toy examples.</p>

<p>The applications are numerous and varied. This demonstrates the generality of the formalism. Any system with events, concurrency, and shared resources can benefit from Petri net modeling.</p>

<h3>My Opinion</h3>

<p>This course provides powerful tools for discrete event systems, complementary to continuous techniques. It is essential for control engineers working on manufacturing systems, protocols, or embedded systems.</p>

<p>Strengths:</p>
<ul>
<li>Rigorous and visual formalism</li>
<li>Analysis of critical properties (liveness, deadlock-freeness)</li>
<li>Broad applicability</li>
<li>Available software tools</li>
</ul>

<p>Areas for improvement:</p>
<ul>
<li>More complex industrial case studies</li>
<li>Link with implementation (code generated from model)</li>
<li>Comparison with other formalisms (automata, process algebra)</li>
<li>Techniques for managing combinatorial explosion</li>
</ul>

<p>Personal reflections:</p>

<p>Petri nets are a universal graphical language for DES. Their major advantage is the integration of modeling, simulation, and formal verification within the same framework.</p>

<p>Formal verification is crucial for critical systems (aerospace, medical, nuclear). Mathematically proving the absence of deadlock or capacity overflow prevents catastrophic bugs.</p>

<p>However, combinatorial explosion remains the major challenge. For large-scale realistic systems, the complete reachability graph is intractable. Abstraction, reduction, and symbolic verification techniques are active areas of research.</p>

<p>The modularity and composability of Petri nets are limited. Combining multiple subnets can be difficult. Colored and hierarchical nets help, but complexity remains.</p>

<p>The link with implementation is sometimes unclear. Modeling is good, but how to go from model to code (PLC, microcontroller)? Automatic code generation from Petri nets exists but is not standardized.</p>

<p>Professional applications:</p>

<p>Petri net skills are applicable in:</p>
<ul>
<li><strong>Industrial automation</strong>: design and validation of production systems</li>
<li><strong>Embedded systems design</strong>: real-time property verification</li>
<li><strong>Communication networks</strong>: protocols, resource management</li>
<li><strong>Software</strong>: workflow modeling, business processes</li>
<li><strong>Research</strong>: formalization and analysis of complex systems</li>
</ul>

<p>The market:</p>
<p>Less mainstream than continuous control or classical programming. Niche in critical domains requiring formal verification. A differentiating skill for complex systems engineers.</p>

<p>The future:</p>
<ul>
<li>Integration with Model-Based Design (Simulink, etc.)</li>
<li>Hardware/software codesign</li>
<li>Verification of cyber-physical systems</li>
<li>AI and learning: automatic model synthesis from data</li>
</ul>

<p>In conclusion, Petri nets are a powerful formalism for modeling, analyzing, and verifying discrete event systems. They complement automata and description languages (GRAFCET, Statecharts) by offering a rigorous mathematical semantics and formal analysis tools. They remain widely used in research and industry for critical systems.</p>

<hr/>

<h2>Course Documents</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Complete Petri Nets Course</h4>
      <p>Complete course: modeling, structural and behavioral properties, liveness and deadlock analysis.</p>
      <embed src="/cours-pdf/S8/Reseaux-Petri/cours-complet.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S8/Reseaux-Petri/cours-complet.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>2023 Exam</h4>
      <p>2023 exam paper: network construction, invariant computation, deadlock analysis and synthesis.</p>
      <embed src="/cours-pdf/S8/Reseaux-Petri/exam-2023.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S8/Reseaux-Petri/exam-2023.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>2023 Solutions</h4>
      <p>Complete solutions for the 2023 exam with analysis methods and detailed explanations.</p>
      <embed src="/cours-pdf/S8/Reseaux-Petri/correction-2023.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S8/Reseaux-Petri/correction-2023.pdf" target="_blank">Download</a></p>
    </div>
  </div>
</div>

</div>

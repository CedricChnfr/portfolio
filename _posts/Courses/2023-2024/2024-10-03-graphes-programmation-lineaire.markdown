---
layout: default
title: "Graphes et Programmation Linéaire - S8"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
---

<style>
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

<h1>Graphes et Programmation Lineaire</h1>

<h2>PARTIE A : GENERALITES</h2>

<h3>Presentation</h3>
<p>Le cours "Graphes et Programmation Lineaire" couvre deux domaines complementaires de la recherche operationnelle: la theorie des graphes pour modeliser des reseaux et relations, et la programmation lineaire pour optimiser des systemes sous contraintes. Ces outils mathematiques sont essentiels pour resoudre des problemes complexes d'optimisation dans l'industrie, la logistique, et les reseaux.</p>

<p><strong>Annee Academique</strong> : 2023-2024<br/>
<strong>Semestre</strong> : 8<br/>
<strong>Categorie</strong> : Mathematiques Appliquees / Recherche Operationnelle</p>

<hr/>

<h2>PARTIE B : PARTIE DESCRIPTIVE</h2>

<h3>Details de l'experience</h3>

<h4>Environnement et contexte</h4>
<p>Le cours combinait theorie mathematique rigoureuse et applications pratiques via des logiciels d'optimisation. Nous avons etudie des algorithmes classiques (Dijkstra, Ford-Fulkerson, Simplexe) et les avons appliques a des problemes reels: routage, planification, allocation de ressources, ordonnancement.</p>

<h4>Ma fonction</h4>
<p>Dans ce cours, j'ai ete responsable de :</p>
<ul>
<li>Modeliser des problemes reels en graphes ou programmes lineaires</li>
<li>Appliquer des algorithmes de recherche de chemins, flots, et arbres couvrants</li>
<li>Formuler et resoudre des problemes d'optimisation lineaire</li>
<li>Utiliser des solveurs (Python, CPLEX, GLPK)</li>
<li>Interpreter les solutions et analyses de sensibilite</li>
<li>Resoudre des problemes de transport, affectation, et ordonnancement</li>
</ul>

<h2>PARTIE C : PARTIE TECHNIQUE</h2>

<p>Cette section explore les aspects techniques des graphes et de la programmation lineaire.</p>

<h3>Concepts techniques appris</h3>

<h4>1. Theorie des Graphes - Definitions</h4>

<p><strong>Graphe G = (V, E)</strong> :</p>
<ul>
<li>V : ensemble de sommets (vertices)</li>
<li>E : ensemble d'aretes (edges) ou arcs</li>
</ul>

<p><strong>Types</strong> :</p>
<ul>
<li><strong>Graphe oriente</strong> : arcs avec direction</li>
<li><strong>Graphe non oriente</strong> : aretes sans direction</li>
<li><strong>Graphe pondere</strong> : poids sur aretes/arcs</li>
<li><strong>Graphe simple</strong> : pas de boucle ni arete multiple</li>
</ul>

<p><strong>Degre</strong> :</p>
<ul>
<li>Degre d'un sommet : nombre d'aretes incidentes</li>
<li>Degre entrant/sortant (graphe oriente)</li>
</ul>

<p><strong>Chemin</strong> : sequence de sommets relies par aretes<br/>
<strong>Cycle</strong> : chemin ferme (revient au point de depart)<br/>
<strong>Connexite</strong> : tous sommets accessibles depuis tout autre</p>

<h4>2. Algorithmes de Plus Court Chemin</h4>

<p><strong>Algorithme de Dijkstra</strong> :<br/>
Trouve plus court chemin d'une source vers tous autres sommets.</p>

<p><strong>Complexite</strong> : O((V+E)log V) avec tas</p>

<p><strong>Limitation</strong> : poids positifs uniquement</p>

<p><strong>Algorithme de Bellman-Ford</strong> :<br/>
Gere poids negatifs, detecte cycles negatifs.</p>

<p><strong>Complexite</strong> : O(VE)</p>

<p><strong>Algorithme de Floyd-Warshall</strong> :<br/>
Plus courts chemins entre toutes paires de sommets.</p>

<p><strong>Complexite</strong> : O(V³)</p>

<p><strong>Applications</strong> :</p>
<ul>
<li>GPS et navigation</li>
<li>Routage reseau</li>
<li>Planification de trajets</li>
<li>Jeux video (IA)</li>
</ul>

<h4>3. Arbres Couvrants</h4>

<p><strong>Arbre</strong> : graphe connexe acyclique<br/>
<strong>Arbre couvrant</strong> : arbre incluant tous les sommets</p>

<p><strong>Arbre Couvrant de Poids Minimum (MST)</strong> :</p>

<p><strong>Algorithme de Kruskal</strong> :</p>
<ul>
<li>Trier aretes par poids croissant</li>
<li>Ajouter arete si ne cree pas cycle</li>
<li>Utilise union-find pour detecter cycles</li>
</ul>

<p><strong>Algorithme de Prim</strong> :</p>
<ul>
<li>Partir d'un sommet</li>
<li>Ajouter arete de poids min reliant arbre a sommet exterieur</li>
<li>Repeter jusqu'a tous sommets inclus</li>
</ul>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S8/graphes/dijkstra.svg" alt="Algorithme de Dijkstra"
       style="max-width: 500px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Recherche du plus court chemin avec l'algorithme de Dijkstra</p>
</div>

<p><strong>Applications</strong> :</p>
<ul>
<li>Conception de reseaux (electrique, eau, telecoms) a cout minimum</li>
<li>Clustering</li>
</ul>

<h4>4. Flots dans les Reseaux</h4>

<p><strong>Reseau de flot</strong> :<br/>
Graphe oriente avec capacites sur arcs.</p>

<p><strong>Probleme du flot maximum</strong> :<br/>
Maximiser flot de la source s vers puits t.</p>

<p><strong>Contraintes</strong> :</p>
<ul>
<li>Flot &le; capacite sur chaque arc</li>
<li>Conservation du flot (entrant = sortant sauf s et t)</li>
</ul>

<p><strong>Algorithme de Ford-Fulkerson</strong> :</p>
<ul>
<li>Trouver chemin augmentant (capacite residuelle &gt; 0)</li>
<li>Augmenter flot le long de ce chemin</li>
<li>Repeter jusqu'a plus de chemin augmentant</li>
</ul>

<p><strong>Theoreme flot-max = coupe-min</strong> :<br/>
Valeur du flot maximal = capacite de la coupe minimale.</p>

<p><strong>Algorithme d'Edmonds-Karp</strong> :<br/>
Ford-Fulkerson avec BFS pour trouver chemin augmentant.</p>

<p><strong>Complexite</strong> : O(VE²)</p>

<p><strong>Applications</strong> :</p>
<ul>
<li>Reseaux de transport (trafic routier, fluides)</li>
<li>Reseaux de communication (bande passante)</li>
<li>Appariement biparti</li>
</ul>

<h4>5. Probleme d'Affectation</h4>

<p><strong>Probleme</strong> :<br/>
Affecter n taches a n agents, minimiser cout total.</p>

<p><strong>Matrice de couts C</strong> :<br/>
C_ij = cout d'affecter tache j a agent i</p>

<p><strong>Formulation</strong> :</p>
<pre><code>Minimiser &Sigma; &Sigma; C_ij x x_ij

Contraintes:
&Sigma;_j x_ij = 1  (chaque agent 1 tache)
&Sigma;_i x_ij = 1  (chaque tache 1 agent)
x_ij &isin; {0,1}
</code></pre>

<p><strong>Algorithme hongrois</strong> :<br/>
Resout en O(n³).</p>

<p><strong>Applications</strong> :</p>
<ul>
<li>Affectation personnel/postes</li>
<li>Planification production</li>
<li>Appariement (dating apps!)</li>
</ul>

<h4>6. Coloration de Graphes</h4>

<p><strong>Probleme</strong> :<br/>
Attribuer couleur a chaque sommet tel que sommets adjacents ont couleurs differentes.</p>

<p><strong>Nombre chromatique &chi;(G)</strong> :<br/>
Nombre minimum de couleurs necessaires.</p>

<p><strong>Theoreme des 4 couleurs</strong> :<br/>
Tout graphe planaire &chi; &le; 4.</p>

<p><strong>Algorithmes</strong> :</p>
<ul>
<li>Glouton (pas optimal mais rapide)</li>
<li>Recherche exhaustive (exponentiel)</li>
</ul>

<p><strong>Applications</strong> :</p>
<ul>
<li>Allocation frequences radio</li>
<li>Ordonnancement (conflits de ressources)</li>
<li>Allocation registres (compilateurs)</li>
</ul>

<h4>7. Programmation Lineaire - Formulation</h4>

<p><strong>Forme standard</strong> :</p>
<pre><code>Maximiser (ou Minimiser) Z = c1*x1 + c2*x2 + ... + cn*xn

Sous contraintes:
a11*x1 + a12*x2 + ... + a1n*xn &le; b1
a21*x1 + a22*x2 + ... + a2n*xn &le; b2
...
am1*x1 + am2*x2 + ... + amn*xn &le; bm

x1, x2, ..., xn &ge; 0
</code></pre>

<p><strong>Forme matricielle</strong> :</p>
<pre><code>Max c^T x
s.t. Ax &le; b, x &ge; 0
</code></pre>

<p><strong>Region admissible</strong> :<br/>
Polyedre convexe defini par contraintes.</p>

<p><strong>Theoreme fondamental</strong> :<br/>
Si solution optimale existe, elle se trouve a un sommet du polyedre.</p>

<h4>8. Algorithme du Simplexe</h4>

<p><strong>Principe</strong> :<br/>
Parcours iteratif des sommets du polyedre vers l'optimum.</p>

<p><strong>Etapes</strong> :</p>
<ol>
<li>Partir d'un sommet admissible (solution de base)</li>
<li>Tester directions ameliorantes</li>
<li>Se deplacer vers sommet adjacent ameliorant Z</li>
<li>Repeter jusqu'a optimum (aucune direction n'ameliore)</li>
</ol>

<p><strong>Tableau du simplexe</strong> :<br/>
Forme tableau pour calculs iteratifs.</p>

<p><strong>Variables d'ecart</strong> :<br/>
Transformer inegalites en egalites.</p>

<p><strong>Complexite</strong> :<br/>
Exponentielle au pire cas, mais polynomial en pratique.</p>

<h4>9. Dualite</h4>

<p><strong>Probleme Primal</strong> :</p>
<pre><code>Max c^T x
s.t. Ax &le; b, x &ge; 0
</code></pre>

<p><strong>Probleme Dual</strong> :</p>
<pre><code>Min b^T y
s.t. A^T y &ge; c, y &ge; 0
</code></pre>

<p><strong>Theoreme de dualite forte</strong> :<br/>
Si primal a solution optimale x*, dual a solution optimale y* et :</p>
<pre><code>c^T x* = b^T y*
</code></pre>

<p><strong>Interpretation economique</strong> :</p>
<ul>
<li>Primal : production optimale</li>
<li>Dual : valorisation des ressources (prix d'ombre)</li>
</ul>

<p><strong>Ecarts complementaires</strong> :</p>
<pre><code>Si x_j &gt; 0 alors contrainte duale j saturee
Si y_i &gt; 0 alors contrainte primale i saturee
</code></pre>

<h4>10. Analyse de Sensibilite</h4>

<p><strong>Questions</strong> :</p>
<ul>
<li>Comment l'optimum varie si on change un parametre (cout, ressource) ?</li>
<li>Plage de validite de la solution actuelle ?</li>
</ul>

<p><strong>Prix d'ombre (shadow price)</strong> :<br/>
Variation de Z si on augmente ressource b_i d'une unite.<br/>
= variable duale y_i*</p>

<p><strong>Cout reduit</strong> :<br/>
Pour variable hors base : combien c_j doit diminuer pour entrer en base.</p>

<p><strong>Plages de variation</strong> :</p>
<ul>
<li>Coefficients objectif c_j</li>
<li>Seconds membres b_i</li>
</ul>

<p>Dans ces plages, solution optimale (base) reste identique.</p>

<h4>11. Probleme de Transport</h4>

<p><strong>Contexte</strong> :<br/>
m sources (offres s_i), n destinations (demandes d_j).<br/>
Cout c_ij pour transporter de i vers j.</p>

<p><strong>Formulation</strong> :</p>
<pre><code>Min &Sigma;_i &Sigma;_j c_ij x x_ij

s.t.
&Sigma;_j x_ij = s_i  (offre source i)
&Sigma;_i x_ij = d_j  (demande destination j)
x_ij &ge; 0
</code></pre>

<p><strong>Condition d'existence</strong> :<br/>
&Sigma; s_i = &Sigma; d_j (offre totale = demande totale)</p>

<p><strong>Methode de resolution</strong> :</p>
<ul>
<li>Methode du coin nord-ouest (solution initiale)</li>
<li>Stepping-stone ou MODI pour optimiser</li>
</ul>

<p><strong>Applications</strong> :</p>
<ul>
<li>Logistique et distribution</li>
<li>Planification production multi-sites</li>
</ul>

<h4>12. Programmation Lineaire en Nombres Entiers</h4>

<p><strong>PLNE (Programmation Lineaire en Nombres Entiers)</strong> :</p>
<pre><code>Max c^T x
s.t. Ax &le; b, x &ge; 0, x &isin; Z^n
</code></pre>

<p><strong>Difficulte</strong> :<br/>
NP-difficile (pas de methode polynomiale connue).</p>

<p><strong>Methodes de resolution</strong> :</p>

<p><strong>Branch and Bound</strong> :</p>
<ul>
<li>Resoudre relaxation continue (ignorer contrainte entiere)</li>
<li>Brancher sur variable fractionnaire</li>
<li>Explorer arbre de decision</li>
<li>Borner avec solutions entieres trouvees</li>
</ul>

<p><strong>Coupes (Cutting Planes)</strong> :<br/>
Ajouter contraintes lineaires eliminant solutions fractionnaires sans enlever solutions entieres.</p>

<p><strong>Methodes heuristiques</strong> :<br/>
Trouver bonnes solutions (pas necessairement optimales) rapidement.</p>

<p><strong>Programmation 0-1</strong> :<br/>
Variables binaires (decisions oui/non).</p>

<p><strong>Applications</strong> :</p>
<ul>
<li>Planification</li>
<li>Ordonnancement</li>
<li>Localisation d'installations</li>
<li>Sac a dos (knapsack)</li>
<li>Tournees de vehicules</li>
</ul>

<h2>PARTIE D : PARTIE ANALYTIQUE</h2>

<h3>Connaissances et competences mobilisees</h3>

<ul>
<li>Modelisation de problemes reels en graphes ou programmes lineaires</li>
<li>Comprehension et application d'algorithmes classiques</li>
<li>Formulation mathematique de problemes d'optimisation</li>
<li>Utilisation de solveurs (Python, logiciels dedies)</li>
<li>Interpretation de solutions et analyse de sensibilite</li>
<li>Evaluation de complexite algorithmique</li>
<li>Resolution de problemes de transport, affectation, et ordonnancement</li>
<li>Esprit critique sur pertinence des modeles et limites</li>
</ul>

<h3>Auto-evaluation</h3>

<p>Ce cours a ete mathematiquement exigeant mais tres enrichissant. La theorie des graphes offre un langage puissant pour modeliser de nombreux systemes: reseaux, relations, dependances.</p>

<p>Les algorithmes classiques (Dijkstra, Kruskal, Ford-Fulkerson) sont elegants et ont fait leurs preuves. Les comprendre en profondeur (pas juste les appliquer mecaniquement) aide a adapter ou concevoir de nouveaux algorithmes.</p>

<p>La programmation lineaire est un outil d'optimisation extremement puissant. La capacite a formuler un probleme complexe en systeme d'equations lineaires est une competence precieuse. Le simplexe, bien que conceptuellement simple (parcours de sommets), demande rigueur dans les calculs.</p>

<p>L'analyse de sensibilite et la dualite sont des concepts profonds. Comprendre que chaque probleme d'optimisation a un dual avec interpretation economique (prix d'ombre) est fascinant.</p>

<p>La programmation en nombres entiers complexifie drastiquement les problemes. La frontiere entre polynomial (PL continue) et NP-difficile (PLNE) est impressionnante. Cela souligne l'importance des heuristiques et approximations en pratique.</p>

<p>Les applications sont omnipresentes: logistique, telecoms, production, transport, finance. Savoir reconnaitre qu'un probleme industriel peut se modeliser en graphe ou PL est une competence transversale.</p>

<p>L'utilisation de solveurs modernes (comme CPLEX, Gurobi, ou bibliotheques Python) democratise l'optimisation. Mais comprendre la theorie sous-jacente reste essentiel pour formuler correctement, interpreter resultats, et diagnostiquer problemes.</p>

<h3>Mon avis</h3>

<p>Ce cours est fondamental pour tout ingenieur confronte a des problemes d'optimisation, de planification, ou de gestion de reseaux.</p>

<p>Points forts :</p>
<ul>
<li>Equilibre theorie/pratique</li>
<li>Algorithmes classiques bien expliques</li>
<li>Applications variees et concretes</li>
<li>Utilisation d'outils logiciels modernes</li>
</ul>

<p>Points a ameliorer :</p>
<ul>
<li>Plus de temps sur PLNE et heuristiques</li>
<li>Cas d'etudes industriels de grande echelle</li>
<li>Programmation non-lineaire (extension naturelle)</li>
<li>Optimisation multi-objectifs</li>
</ul>

<p>Reflexions personnelles :</p>

<p>L'optimisation est au coeur de nombreux defis industriels: comment produire plus avec moins de ressources, livrer plus vite a moindre cout, utiliser au mieux l'energie, etc. Les outils mathematiques de ce cours permettent d'aborder ces questions de maniere rigoureuse.</p>

<p>La modelisation est souvent la partie la plus difficile. Transformer un probleme reel confus en modele mathematique propre demande abstraction et simplification intelligente. Un modele trop simple perd en pertinence; trop complexe devient insoluble.</p>

<p>Le fosse entre problemes polynomiaux et NP-difficiles rappelle les limites de l'optimisation exacte. Pour problemes de grande taille ou complexes, les heuristiques et metaheuristiques (algorithmes genetiques, recuit simule, etc.) sont incontournables, meme si elles ne garantissent pas l'optimalite.</p>

<p>La recherche operationnelle est un domaine vaste et actif. Les problemes reels incluent souvent incertitudes, dynamique, contraintes non-lineaires. L'optimisation stochastique, robuste, et en ligne sont des extensions importantes.</p>

<p>Applications professionnelles :</p>

<p>Ces competences sont applicables dans de nombreux secteurs :</p>
<ul>
<li><strong>Logistique</strong> : routage de vehicules, gestion d'entrepots, supply chain</li>
<li><strong>Telecommunications</strong> : routage, allocation de bande passante</li>
<li><strong>Energie</strong> : optimisation de production, smart grids</li>
<li><strong>Transport</strong> : gestion de trafic, planification de lignes</li>
<li><strong>Production</strong> : ordonnancement, allocation de ressources</li>
<li><strong>Finance</strong> : optimisation de portefeuille</li>
<li><strong>Sante</strong> : planification d'emplois du temps, allocation de ressources hospitalieres</li>
</ul>

<p>La maitrise de ces outils, couplee a des competences en data science et apprentissage automatique, ouvre des perspectives en data-driven optimization: utiliser donnees massives pour affiner modeles et predictions, puis optimiser en consequence.</p>

<p>Maitriser ces techniques en S8 est essentiel pour tout ingenieur souhaitant concevoir ou ameliorer des systemes efficaces dans un monde toujours plus connecte et complexe.</p>

<hr/>

<h2>Documents de Cours</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Annales 2018</h4>
      <p>Sujet d'examen 2018 : algorithmes de graphes (Dijkstra, Bellman-Ford), flots et programmation lineaire.</p>
      <embed src="/cours-pdf/S8/Graphes-Programmation-Lineaire/annales-2018.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S8/Graphes-Programmation-Lineaire/annales-2018.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>Correction Examen 2024</h4>
      <p>Correction complete de l'examen 2024 avec explications detaillees des algorithmes et methodes de resolution.</p>
      <embed src="/cours-pdf/S8/Graphes-Programmation-Lineaire/correction-exam-2024.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S8/Graphes-Programmation-Lineaire/correction-exam-2024.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>TP Algorithme de Dijkstra</h4>
      <p>Travaux pratiques : implementation de Dijkstra pour recherche de plus court chemin dans differents graphes.</p>
      <embed src="/cours-pdf/S8/Graphes-Programmation-Lineaire/tp-dijkstra.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S8/Graphes-Programmation-Lineaire/tp-dijkstra.pdf" target="_blank">Telecharger</a></p>
    </div>
  </div>
</div>

<hr/>

<p><em>Cours suivi en 2023-2024 a l'INSA Toulouse, Departement Genie Electrique et Informatique.</em></p>

</div>

<div class="lang-en">

<h1>Graphs and Linear Programming</h1>

<h2>PART A: GENERALITIES</h2>

<h3>Presentation</h3>
<p>The "Graphs and Linear Programming" course covers two complementary areas of operations research: graph theory for modeling networks and relationships, and linear programming for optimizing systems under constraints. These mathematical tools are essential for solving complex optimization problems in industry, logistics, and networks.</p>

<p><strong>Academic Year</strong>: 2023-2024<br/>
<strong>Semester</strong>: 8<br/>
<strong>Category</strong>: Applied Mathematics / Operations Research</p>

<hr/>

<h2>PART B: DESCRIPTIVE PART</h2>

<h3>Experience Details</h3>

<h4>Environment and Context</h4>
<p>The course combined rigorous mathematical theory with practical applications using optimization software. We studied classical algorithms (Dijkstra, Ford-Fulkerson, Simplex) and applied them to real-world problems: routing, planning, resource allocation, scheduling.</p>

<h4>My Function</h4>
<p>In this course, I was responsible for:</p>
<ul>
<li>Modeling real-world problems as graphs or linear programs</li>
<li>Applying path-finding, flow, and spanning tree algorithms</li>
<li>Formulating and solving linear optimization problems</li>
<li>Using solvers (Python, CPLEX, GLPK)</li>
<li>Interpreting solutions and sensitivity analyses</li>
<li>Solving transportation, assignment, and scheduling problems</li>
</ul>

<h2>PART C: TECHNICAL PART</h2>

<p>This section explores the technical aspects of graphs and linear programming.</p>

<h3>Technical Concepts Learned</h3>

<h4>1. Graph Theory - Definitions</h4>

<p><strong>Graph G = (V, E)</strong>:</p>
<ul>
<li>V: set of vertices</li>
<li>E: set of edges or arcs</li>
</ul>

<p><strong>Types</strong>:</p>
<ul>
<li><strong>Directed graph</strong>: arcs with direction</li>
<li><strong>Undirected graph</strong>: edges without direction</li>
<li><strong>Weighted graph</strong>: weights on edges/arcs</li>
<li><strong>Simple graph</strong>: no loops or multiple edges</li>
</ul>

<p><strong>Degree</strong>:</p>
<ul>
<li>Degree of a vertex: number of incident edges</li>
<li>In-degree/out-degree (directed graph)</li>
</ul>

<p><strong>Path</strong>: sequence of vertices connected by edges<br/>
<strong>Cycle</strong>: closed path (returns to starting point)<br/>
<strong>Connectivity</strong>: all vertices reachable from any other</p>

<h4>2. Shortest Path Algorithms</h4>

<p><strong>Dijkstra's Algorithm</strong>:<br/>
Finds shortest path from a source to all other vertices.</p>

<p><strong>Complexity</strong>: O((V+E)log V) with heap</p>

<p><strong>Limitation</strong>: positive weights only</p>

<p><strong>Bellman-Ford Algorithm</strong>:<br/>
Handles negative weights, detects negative cycles.</p>

<p><strong>Complexity</strong>: O(VE)</p>

<p><strong>Floyd-Warshall Algorithm</strong>:<br/>
Shortest paths between all pairs of vertices.</p>

<p><strong>Complexity</strong>: O(V³)</p>

<p><strong>Applications</strong>:</p>
<ul>
<li>GPS and navigation</li>
<li>Network routing</li>
<li>Route planning</li>
<li>Video games (AI)</li>
</ul>

<h4>3. Spanning Trees</h4>

<p><strong>Tree</strong>: connected acyclic graph<br/>
<strong>Spanning tree</strong>: tree including all vertices</p>

<p><strong>Minimum Spanning Tree (MST)</strong>:</p>

<p><strong>Kruskal's Algorithm</strong>:</p>
<ul>
<li>Sort edges by increasing weight</li>
<li>Add edge if it does not create a cycle</li>
<li>Uses union-find to detect cycles</li>
</ul>

<p><strong>Prim's Algorithm</strong>:</p>
<ul>
<li>Start from a vertex</li>
<li>Add minimum-weight edge connecting tree to external vertex</li>
<li>Repeat until all vertices are included</li>
</ul>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S8/graphes/dijkstra.svg" alt="Dijkstra's Algorithm"
       style="max-width: 500px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Shortest path search using Dijkstra's algorithm</p>
</div>

<p><strong>Applications</strong>:</p>
<ul>
<li>Minimum-cost network design (electrical, water, telecoms)</li>
<li>Clustering</li>
</ul>

<h4>4. Network Flows</h4>

<p><strong>Flow network</strong>:<br/>
Directed graph with capacities on arcs.</p>

<p><strong>Maximum flow problem</strong>:<br/>
Maximize flow from source s to sink t.</p>

<p><strong>Constraints</strong>:</p>
<ul>
<li>Flow &le; capacity on each arc</li>
<li>Flow conservation (inflow = outflow except at s and t)</li>
</ul>

<p><strong>Ford-Fulkerson Algorithm</strong>:</p>
<ul>
<li>Find augmenting path (residual capacity &gt; 0)</li>
<li>Increase flow along this path</li>
<li>Repeat until no augmenting path exists</li>
</ul>

<p><strong>Max-flow min-cut theorem</strong>:<br/>
Value of maximum flow = capacity of the minimum cut.</p>

<p><strong>Edmonds-Karp Algorithm</strong>:<br/>
Ford-Fulkerson with BFS to find augmenting path.</p>

<p><strong>Complexity</strong>: O(VE²)</p>

<p><strong>Applications</strong>:</p>
<ul>
<li>Transportation networks (road traffic, fluids)</li>
<li>Communication networks (bandwidth)</li>
<li>Bipartite matching</li>
</ul>

<h4>5. Assignment Problem</h4>

<p><strong>Problem</strong>:<br/>
Assign n tasks to n agents, minimize total cost.</p>

<p><strong>Cost matrix C</strong>:<br/>
C_ij = cost of assigning task j to agent i</p>

<p><strong>Formulation</strong>:</p>
<pre><code>Minimize &Sigma; &Sigma; C_ij x x_ij

Constraints:
&Sigma;_j x_ij = 1  (each agent 1 task)
&Sigma;_i x_ij = 1  (each task 1 agent)
x_ij &isin; {0,1}
</code></pre>

<p><strong>Hungarian algorithm</strong>:<br/>
Solves in O(n³).</p>

<p><strong>Applications</strong>:</p>
<ul>
<li>Staff/position assignment</li>
<li>Production planning</li>
<li>Matching (dating apps!)</li>
</ul>

<h4>6. Graph Coloring</h4>

<p><strong>Problem</strong>:<br/>
Assign a color to each vertex such that adjacent vertices have different colors.</p>

<p><strong>Chromatic number &chi;(G)</strong>:<br/>
Minimum number of colors needed.</p>

<p><strong>Four-color theorem</strong>:<br/>
Any planar graph &chi; &le; 4.</p>

<p><strong>Algorithms</strong>:</p>
<ul>
<li>Greedy (not optimal but fast)</li>
<li>Exhaustive search (exponential)</li>
</ul>

<p><strong>Applications</strong>:</p>
<ul>
<li>Radio frequency allocation</li>
<li>Scheduling (resource conflicts)</li>
<li>Register allocation (compilers)</li>
</ul>

<h4>7. Linear Programming - Formulation</h4>

<p><strong>Standard form</strong>:</p>
<pre><code>Maximize (or Minimize) Z = c1*x1 + c2*x2 + ... + cn*xn

Subject to:
a11*x1 + a12*x2 + ... + a1n*xn &le; b1
a21*x1 + a22*x2 + ... + a2n*xn &le; b2
...
am1*x1 + am2*x2 + ... + amn*xn &le; bm

x1, x2, ..., xn &ge; 0
</code></pre>

<p><strong>Matrix form</strong>:</p>
<pre><code>Max c^T x
s.t. Ax &le; b, x &ge; 0
</code></pre>

<p><strong>Feasible region</strong>:<br/>
Convex polyhedron defined by constraints.</p>

<p><strong>Fundamental theorem</strong>:<br/>
If an optimal solution exists, it is located at a vertex of the polyhedron.</p>

<h4>8. Simplex Algorithm</h4>

<p><strong>Principle</strong>:<br/>
Iterative traversal of polyhedron vertices toward the optimum.</p>

<p><strong>Steps</strong>:</p>
<ol>
<li>Start from a feasible vertex (basic solution)</li>
<li>Test improving directions</li>
<li>Move to adjacent vertex that improves Z</li>
<li>Repeat until optimum (no direction improves)</li>
</ol>

<p><strong>Simplex tableau</strong>:<br/>
Tableau form for iterative calculations.</p>

<p><strong>Slack variables</strong>:<br/>
Transform inequalities into equalities.</p>

<p><strong>Complexity</strong>:<br/>
Exponential in the worst case, but polynomial in practice.</p>

<h4>9. Duality</h4>

<p><strong>Primal Problem</strong>:</p>
<pre><code>Max c^T x
s.t. Ax &le; b, x &ge; 0
</code></pre>

<p><strong>Dual Problem</strong>:</p>
<pre><code>Min b^T y
s.t. A^T y &ge; c, y &ge; 0
</code></pre>

<p><strong>Strong duality theorem</strong>:<br/>
If the primal has an optimal solution x*, the dual has an optimal solution y* and:</p>
<pre><code>c^T x* = b^T y*
</code></pre>

<p><strong>Economic interpretation</strong>:</p>
<ul>
<li>Primal: optimal production</li>
<li>Dual: resource valuation (shadow prices)</li>
</ul>

<p><strong>Complementary slackness</strong>:</p>
<pre><code>If x_j &gt; 0 then dual constraint j is tight
If y_i &gt; 0 then primal constraint i is tight
</code></pre>

<h4>10. Sensitivity Analysis</h4>

<p><strong>Questions</strong>:</p>
<ul>
<li>How does the optimum change if a parameter (cost, resource) changes?</li>
<li>Range of validity for the current solution?</li>
</ul>

<p><strong>Shadow price</strong>:<br/>
Change in Z if resource b_i is increased by one unit.<br/>
= dual variable y_i*</p>

<p><strong>Reduced cost</strong>:<br/>
For a non-basic variable: how much c_j must decrease to enter the basis.</p>

<p><strong>Variation ranges</strong>:</p>
<ul>
<li>Objective coefficients c_j</li>
<li>Right-hand sides b_i</li>
</ul>

<p>Within these ranges, the optimal solution (basis) remains the same.</p>

<h4>11. Transportation Problem</h4>

<p><strong>Context</strong>:<br/>
m sources (supplies s_i), n destinations (demands d_j).<br/>
Cost c_ij to transport from i to j.</p>

<p><strong>Formulation</strong>:</p>
<pre><code>Min &Sigma;_i &Sigma;_j c_ij x x_ij

s.t.
&Sigma;_j x_ij = s_i  (supply at source i)
&Sigma;_i x_ij = d_j  (demand at destination j)
x_ij &ge; 0
</code></pre>

<p><strong>Existence condition</strong>:<br/>
&Sigma; s_i = &Sigma; d_j (total supply = total demand)</p>

<p><strong>Solution method</strong>:</p>
<ul>
<li>Northwest corner method (initial solution)</li>
<li>Stepping-stone or MODI for optimization</li>
</ul>

<p><strong>Applications</strong>:</p>
<ul>
<li>Logistics and distribution</li>
<li>Multi-site production planning</li>
</ul>

<h4>12. Integer Linear Programming</h4>

<p><strong>ILP (Integer Linear Programming)</strong>:</p>
<pre><code>Max c^T x
s.t. Ax &le; b, x &ge; 0, x &isin; Z^n
</code></pre>

<p><strong>Difficulty</strong>:<br/>
NP-hard (no known polynomial method).</p>

<p><strong>Solution methods</strong>:</p>

<p><strong>Branch and Bound</strong>:</p>
<ul>
<li>Solve continuous relaxation (ignore integer constraint)</li>
<li>Branch on fractional variable</li>
<li>Explore decision tree</li>
<li>Bound using found integer solutions</li>
</ul>

<p><strong>Cutting Planes</strong>:<br/>
Add linear constraints eliminating fractional solutions without removing integer solutions.</p>

<p><strong>Heuristic methods</strong>:<br/>
Find good solutions (not necessarily optimal) quickly.</p>

<p><strong>0-1 Programming</strong>:<br/>
Binary variables (yes/no decisions).</p>

<p><strong>Applications</strong>:</p>
<ul>
<li>Planning</li>
<li>Scheduling</li>
<li>Facility location</li>
<li>Knapsack problem</li>
<li>Vehicle routing</li>
</ul>

<h2>PART D: ANALYTICAL PART</h2>

<h3>Knowledge and Skills Mobilized</h3>

<ul>
<li>Modeling real-world problems as graphs or linear programs</li>
<li>Understanding and applying classical algorithms</li>
<li>Mathematical formulation of optimization problems</li>
<li>Using solvers (Python, dedicated software)</li>
<li>Interpreting solutions and sensitivity analysis</li>
<li>Evaluating algorithmic complexity</li>
<li>Solving transportation, assignment, and scheduling problems</li>
<li>Critical thinking about model relevance and limitations</li>
</ul>

<h3>Self Evaluation</h3>

<p>This course was mathematically demanding but very rewarding. Graph theory provides a powerful language for modeling many systems: networks, relationships, dependencies.</p>

<p>Classical algorithms (Dijkstra, Kruskal, Ford-Fulkerson) are elegant and well-proven. Understanding them in depth (not just applying them mechanically) helps in adapting or designing new algorithms.</p>

<p>Linear programming is an extremely powerful optimization tool. The ability to formulate a complex problem as a system of linear equations is a valuable skill. The simplex method, although conceptually simple (traversing vertices), requires rigor in calculations.</p>

<p>Sensitivity analysis and duality are deep concepts. Understanding that every optimization problem has a dual with economic interpretation (shadow prices) is fascinating.</p>

<p>Integer programming drastically increases problem complexity. The boundary between polynomial (continuous LP) and NP-hard (ILP) is striking. This underscores the importance of heuristics and approximations in practice.</p>

<p>Applications are ubiquitous: logistics, telecoms, production, transportation, finance. Knowing how to recognize that an industrial problem can be modeled as a graph or LP is a cross-cutting skill.</p>

<p>Using modern solvers (such as CPLEX, Gurobi, or Python libraries) democratizes optimization. However, understanding the underlying theory remains essential for correct formulation, result interpretation, and problem diagnosis.</p>

<h3>My Opinion</h3>

<p>This course is fundamental for any engineer facing optimization, planning, or network management problems.</p>

<p>Strengths:</p>
<ul>
<li>Balance between theory and practice</li>
<li>Well-explained classical algorithms</li>
<li>Varied and concrete applications</li>
<li>Use of modern software tools</li>
</ul>

<p>Areas for improvement:</p>
<ul>
<li>More time on ILP and heuristics</li>
<li>Large-scale industrial case studies</li>
<li>Nonlinear programming (natural extension)</li>
<li>Multi-objective optimization</li>
</ul>

<p>Personal reflections:</p>

<p>Optimization is at the heart of many industrial challenges: how to produce more with fewer resources, deliver faster at lower cost, make the best use of energy, etc. The mathematical tools from this course allow us to address these questions rigorously.</p>

<p>Modeling is often the most difficult part. Transforming a messy real-world problem into a clean mathematical model requires abstraction and intelligent simplification. A model that is too simple loses relevance; too complex becomes unsolvable.</p>

<p>The gap between polynomial and NP-hard problems serves as a reminder of the limits of exact optimization. For large-scale or complex problems, heuristics and metaheuristics (genetic algorithms, simulated annealing, etc.) are indispensable, even though they do not guarantee optimality.</p>

<p>Operations research is a vast and active field. Real-world problems often involve uncertainties, dynamics, and nonlinear constraints. Stochastic, robust, and online optimization are important extensions.</p>

<p>Professional applications:</p>

<p>These skills are applicable across many sectors:</p>
<ul>
<li><strong>Logistics</strong>: vehicle routing, warehouse management, supply chain</li>
<li><strong>Telecommunications</strong>: routing, bandwidth allocation</li>
<li><strong>Energy</strong>: production optimization, smart grids</li>
<li><strong>Transportation</strong>: traffic management, line planning</li>
<li><strong>Manufacturing</strong>: scheduling, resource allocation</li>
<li><strong>Finance</strong>: portfolio optimization</li>
<li><strong>Healthcare</strong>: staff scheduling, hospital resource allocation</li>
</ul>

<p>Mastering these tools, combined with data science and machine learning skills, opens perspectives in data-driven optimization: using massive data to refine models and predictions, then optimizing accordingly.</p>

<p>Mastering these techniques in S8 is essential for any engineer wishing to design or improve efficient systems in an increasingly connected and complex world.</p>

<hr/>

<h2>Course Documents</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>2018 Past Exam</h4>
      <p>2018 exam paper: graph algorithms (Dijkstra, Bellman-Ford), flows and linear programming.</p>
      <embed src="/cours-pdf/S8/Graphes-Programmation-Lineaire/annales-2018.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S8/Graphes-Programmation-Lineaire/annales-2018.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>2024 Exam Correction</h4>
      <p>Complete correction of the 2024 exam with detailed explanations of algorithms and solution methods.</p>
      <embed src="/cours-pdf/S8/Graphes-Programmation-Lineaire/correction-exam-2024.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S8/Graphes-Programmation-Lineaire/correction-exam-2024.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>Dijkstra Algorithm Lab</h4>
      <p>Lab work: implementation of Dijkstra for shortest path search in various graphs.</p>
      <embed src="/cours-pdf/S8/Graphes-Programmation-Lineaire/tp-dijkstra.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S8/Graphes-Programmation-Lineaire/tp-dijkstra.pdf" target="_blank">Download</a></p>
    </div>
  </div>
</div>

<hr/>

<p><em>Course taken in 2023-2024 at INSA Toulouse, Department of Electrical Engineering and Computer Science.</em></p>

</div>

<div class="back-nav">
    <a href="./my-courses-2023-2024.html" data-i18n-html="back-courses-2023-2024">&larr; Retour aux Cours 2023-2024</a>
</div>

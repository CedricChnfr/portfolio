---
layout: default
title: "Modélisation et Commande des Systèmes à Événements Discrets - S5"
date: 2024-10-02 10:56:03 +0200
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
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f9;
    color: #333;
    line-height: 1.6;
}
h2, h3, h4, h5 {
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
    background-color: #2a7ae2;
    color: white;
}
tr:nth-child(even) {
    background-color: #f9f9f9;
}
</style>

<div class="back-nav">
  <a href="./my-courses-2022-2023.html" data-i18n-html="back-courses-2022-2023">&#8592; Retour aux Cours 2022-2023</a>
</div>

<div class="lang-fr">

<h1>Modelisation et Commande des Systemes a Evenements Discrets - S5</h1>

<p><strong>Annee</strong>: 2022-2023 (Semestre 5)<br/>
<strong>Credits</strong>: 2 ECTS<br/>
<strong>Type</strong>: Automatique et Systemes<br/>
<strong>Enseignant</strong>: Vignolles</p>

<hr/>

<h2>PART A: PRESENTATION GENERALE</h2>

<h3>Objectifs du cours</h3>

<p>Ce cours introduit la modelisation et la commande des systemes a evenements discrets (SED), systemes dont l'evolution est declenchee par des evenements discrets plutot que par le temps continu. Ces systemes sont omnipresents dans l'industrie (lignes de production, systemes de transport), l'informatique (protocoles, workflows) et la robotique. Le cours couvre les automates finis et les reseaux de Petri, outils fondamentaux pour modeliser, analyser et commander ces systemes.</p>

<h3>Competences visees</h3>

<ul>
  <li>Modeliser des systemes industriels avec automates et reseaux de Petri</li>
  <li>Analyser les proprietes des systemes (vivacite, blocage, atteignabilite)</li>
  <li>Concevoir des superviseurs pour garantir des specifications</li>
  <li>Utiliser des logiciels de simulation (AutomDiscrete)</li>
  <li>Implementer des automates sur automates programmables (grafcet)</li>
  <li>Detecter et resoudre les problemes de synchronisation et blocages</li>
</ul>

<h3>Organisation</h3>

<ul>
  <li><strong>Volume horaire</strong>: 20h (CM: 10h, TD: 6h, TP: 4h)</li>
  <li><strong>Evaluation</strong>: Examen ecrit (70%) + TPs (30%)</li>
  <li><strong>Semestre</strong>: 5 (2022-2023)</li>
  <li><strong>Prerequis</strong>: Logique, algebre de base, notions d'automatique</li>
</ul>

<hr/>

<h2>PART B: EXPERIENCE, CONTEXTE ET FONCTION</h2>

<h3>Contenu pedagogique</h3>

<p>Le cours s'organise autour de deux formalismes complementaires: les automates et les reseaux de Petri.</p>

<h4>1. Systemes a Evenements Discrets</h4>

<p><strong>Caracteristiques principales</strong>:</p>

<p>Les SED evoluent par sauts discrets declenches par des evenements:</p>
<ul>
  <li><strong>Etats discrets</strong>: nombre fini ou denombrable d'etats</li>
  <li><strong>Evenements</strong>: actions instantanees causant des transitions</li>
  <li><strong>Evolution asynchrone</strong>: pas de synchronisation globale</li>
  <li><strong>Non-determinisme</strong>: plusieurs transitions possibles depuis un etat</li>
  <li><strong>Concurrence</strong>: plusieurs processus simultanes</li>
</ul>

<p><strong>Exemples typiques</strong>:</p>
<ul>
  <li>Systeme de tri de pieces (TP principal)</li>
  <li>Feux de circulation</li>
  <li>Distributeur automatique</li>
  <li>Ligne de production manufacturiere</li>
  <li>Protocole de communication</li>
</ul>

<p><strong>Difference avec systemes continus</strong>:</p>

<table>
  <thead>
    <tr><th>Critere</th><th>Systemes continus</th><th>Systemes discrets</th></tr>
  </thead>
  <tbody>
    <tr><td>Etats</td><td>Continus (reels)</td><td>Discrets (entiers)</td></tr>
    <tr><td>Temps</td><td>Evolution continue</td><td>Evenements instantanes</td></tr>
    <tr><td>Modele</td><td>Equations differentielles</td><td>Automates, Petri</td></tr>
    <tr><td>Exemple</td><td>Regulation temperature</td><td>Ligne d'assemblage</td></tr>
  </tbody>
</table>

<h4>2. Automates a Etats Finis</h4>

<p><strong>Definition</strong>:</p>

<p>Un automate est defini par:</p>
<ul>
  <li>E : ensemble d'etats</li>
  <li>e0 : etat initial</li>
  <li>&Sigma; : alphabet d'evenements</li>
  <li>&delta; : fonction de transition (E &times; &Sigma; &rarr; E)</li>
  <li>Em : etats marques (acceptants)</li>
</ul>

<p><strong>Representation graphique</strong>:</p>

<pre><code>    [e1] --a--&gt; [e2] --b--&gt; [e3]
     |                       |
     +----------c------------+
</code></pre>

<p>Etats = cercles, transitions = fleches etiquetees, etat initial = fleche entrante.</p>

<p><strong>Exemple TD: Distributeur de boissons</strong>:</p>

<p>Etats:</p>
<ul>
  <li>e0 : attente</li>
  <li>e1 : 50 centimes inseres</li>
  <li>e2 : 1 euro insere</li>
  <li>e3 : boisson servie</li>
</ul>

<p>Evenements:</p>
<ul>
  <li>p50 : insertion 50 centimes</li>
  <li>p100 : insertion 1 euro</li>
  <li>serv : servir boisson</li>
  <li>annul : annulation</li>
</ul>

<p><strong>Determinisme vs non-determinisme</strong>:</p>

<p>Automate deterministe: une seule transition possible pour chaque couple (etat, evenement).<br/>
Automate non-deterministe: plusieurs transitions possibles.</p>

<p><strong>Operations sur automates</strong>:</p>

<p><strong>Produit synchrone</strong>: combine deux automates avec synchronisation sur evenements communs.</p>

<p>Utilise pour modeliser des systemes composes de plusieurs sous-systemes interagissant.</p>

<p><strong>Accessibilite</strong>: un etat est accessible s'il existe un chemin depuis l'etat initial.</p>

<p><strong>Co-accessibilite</strong>: un etat est co-accessible s'il existe un chemin vers un etat marque.</p>

<p><strong>Trim</strong>: automate ne contenant que les etats accessibles et co-accessibles.</p>

<h4>3. Reseaux de Petri</h4>

<p><strong>Structure de base</strong>:</p>

<p>Un reseau de Petri comprend:</p>
<ul>
  <li>Places (cercles): contiennent des jetons</li>
  <li>Transitions (rectangles): evenements</li>
  <li>Arcs orientes: places &rarr; transitions ou transitions &rarr; places</li>
  <li>Marquage M: nombre de jetons dans chaque place</li>
</ul>

<p><strong>Regle de tir</strong>:</p>

<p>Une transition est franchissable si toutes les places d'entree contiennent au moins un jeton.</p>

<p>Apres franchissement:</p>
<ul>
  <li>Retirer un jeton de chaque place d'entree</li>
  <li>Ajouter un jeton a chaque place de sortie</li>
</ul>

<p><strong>Exemple: Producteur-Consommateur</strong>:</p>

<pre><code>    (Buffer vide) --produire--&gt; (Buffer plein) --consommer--&gt; (Buffer vide)
</code></pre>

<p>Places: Buffer vide (1 jeton initial), Buffer plein (0 jeton)<br/>
Transitions: produire, consommer</p>

<p><strong>Proprietes importantes</strong>:</p>

<p><strong>Bornage</strong>: nombre maximal de jetons dans une place.</p>
<ul>
  <li>Reseau borne: toutes les places ont un nombre limite de jetons</li>
  <li>Reseau sauf (safe): maximum 1 jeton par place</li>
</ul>

<p><strong>Vivacite</strong>: une transition est vivante si elle peut toujours etre franchie dans le futur (pas de blocage definitif).</p>

<p><strong>Reinitialisabilite</strong>: possibilite de revenir au marquage initial.</p>

<p><strong>Blocage (deadlock)</strong>: marquage ou aucune transition n'est franchissable.</p>

<p><strong>Analyse par graphe de marquages</strong>:</p>

<p>Graphe representant tous les marquages atteignables et les transitions entre eux.</p>

<p>Permet de:</p>
<ul>
  <li>Detecter les blocages</li>
  <li>Verifier le bornage</li>
  <li>Analyser la vivacite</li>
  <li>Calculer les etats accessibles</li>
</ul>

<h4>4. Modelisation de Systemes Industriels</h4>

<p><strong>Systeme de tri de pieces (TP)</strong>:</p>

<p>Composants:</p>
<ul>
  <li>Tapis d'entree (T_ON) et de sortie (C_ON)</li>
  <li>Capteurs: entree tapis, detection metal, detection autre</li>
  <li>Bacs de sortie: metal (B1), autre (B2), rebut (B)</li>
  <li>Verins pour diriger les pieces</li>
</ul>

<p>Etats du systeme:</p>
<ul>
  <li>Etat 0: attente (tapis arretes)</li>
  <li>Etat 1: demarrage (tapis en marche)</li>
  <li>Etat 2: piece detectee (temporisation)</li>
  <li>Etat 3: identification piece</li>
  <li>Etats 4,5,6: tri selon categorie</li>
</ul>

<p><strong>Logique de commande (automate programmable)</strong>:</p>

<pre><code>IF (STATE_TRI = 0) THEN
    T_ON := 0;  // Tapis arrete
    C_ON := 0;
    IF ((P_g1=1) AND (P_g2=1) AND (P_g3=1)) THEN
        STATE_TRI := 1;  // Tous les bacs vides, demarrer
    END_IF;
END_IF;

IF (STATE_TRI = 1) THEN
    T_ON := 1;  // Demarrer tapis
    C_ON := 1;
    IF (Pp_entreeTapis = 1) THEN
        STATE_TRI := 2;  // Piece detectee
    END_IF;
END_IF;

IF (STATE_TRI = 3) THEN
    IF ((p_autre=1) AND (p_metal=1)) THEN
        STATE_TRI := 5;  // Piece metallique
    ELSIF (p_autre=1) THEN
        STATE_TRI := 6;  // Autre piece
    ELSE
        STATE_TRI := 4;  // Rebut
    END_IF;
END_IF;
</code></pre>

<p><strong>Temporisations</strong>:</p>

<p>Les timers permettent d'attendre la stabilisation des capteurs:</p>
<ul>
  <li>Timer1, Timer2, Timer3: temporisations de 2s ou 1s</li>
  <li>Evitent les fausses detections</li>
</ul>

<h4>5. Grafcet et Automates Programmables</h4>

<p><strong>Grafcet (Graphe Fonctionnel de Commande Etape-Transition)</strong>:</p>

<p>Representation graphique pour automatismes industriels:</p>
<ul>
  <li>Etapes (carres numerotes): etats du systeme</li>
  <li>Transitions (traits horizontaux): conditions de passage</li>
  <li>Actions associees aux etapes</li>
  <li>Liaisons orientees</li>
</ul>

<p><strong>Regles d'evolution</strong>:</p>
<ol>
  <li>Etape initiale active au demarrage</li>
  <li>Transition franchie si etape amont active ET condition vraie</li>
  <li>Activation etape aval et desactivation etape amont</li>
</ol>

<p><strong>Conversion Grafcet &rarr; Automate programmable</strong>:</p>

<p>Le grafcet se traduit directement en code pour API (Automate Programmable Industriel) en langage structure ou ladder.</p>

<h4>6. Synthese de Superviseurs</h4>

<p><strong>Principe</strong>:</p>

<p>Concevoir un controleur (superviseur) qui restreint le comportement du systeme pour respecter des specifications.</p>

<p><strong>Specifications typiques</strong>:</p>
<ul>
  <li>Eviter les blocages</li>
  <li>Garantir la securite (etats interdits)</li>
  <li>Maximiser la productivite</li>
  <li>Respecter des sequences obligatoires</li>
</ul>

<p><strong>Evenements controlables vs non-controlables</strong>:</p>

<p>Controlables: le superviseur peut empecher leur occurrence (ex: demarrer machine).<br/>
Non-controlables: arrivent spontanement (ex: piece arrivee, panne).</p>

<p><strong>Methode</strong>:</p>
<ol>
  <li>Modeliser le systeme (automate ou Petri)</li>
  <li>Definir les specifications (etats ou comportements interdits)</li>
  <li>Calculer le superviseur (restreindre les transitions)</li>
  <li>Verifier les proprietes (non-blocage, controlabilite)</li>
</ol>

<hr/>

<h2>PART C: ASPECTS TECHNIQUES</h2>

<h3>Travaux Pratiques</h3>

<p><strong>TP1: Systeme de tri automatique</strong></p>

<p>Objectif: modeliser et simuler un systeme de tri de pieces sur tapis avec le logiciel AutomDiscrete.</p>

<p><strong>Cahier des charges</strong>:</p>
<ul>
  <li>Tri de 3 categories: metal, autre, rebut</li>
  <li>3 bacs de sortie avec capteurs de niveau</li>
  <li>Capteurs de detection: metal, autre matiere</li>
  <li>Temporisations pour stabilisation</li>
  <li>Arret automatique si bacs pleins</li>
</ul>

<p><strong>Modelisation par automate</strong>:</p>

<p>Etats du systeme: 7 etats (0 a 6)</p>
<ul>
  <li>0: Repos</li>
  <li>1: Tapis en marche</li>
  <li>2: Temporisation apres detection</li>
  <li>3: Identification de la piece</li>
  <li>4: Tri rebut</li>
  <li>5: Tri metal</li>
  <li>6: Tri autre</li>
</ul>

<p>Evenements:</p>
<ul>
  <li>Bacs vides (P_g1, P_g2, P_g3)</li>
  <li>Piece entree tapis</li>
  <li>Fin temporisation</li>
  <li>Detection metal, autre</li>
  <li>Bacs pleins</li>
</ul>

<p><strong>Implementation logiciel AutomDiscrete</strong>:</p>

<p>Outil graphique permettant:</p>
<ul>
  <li>Dessiner l'automate (etats, transitions)</li>
  <li>Definir les evenements et actions</li>
  <li>Simuler l'evolution du systeme</li>
  <li>Exporter en code automate programmable</li>
</ul>

<p><strong>Code genere</strong> (extrait):</p>

<p>Variables:</p>
<ul>
  <li>STATE_TRI: etat courant</li>
  <li>T_ON, C_ON: commandes tapis</li>
  <li>B_OFF, B1_ON, B2_ON: commandes verins</li>
  <li>P1-P6: etats internes</li>
  <li>Timers pour temporisations</li>
</ul>

<p><strong>Tests et validation</strong>:</p>
<ul>
  <li>Scenario nominal: tri correct selon categorie</li>
  <li>Cas limites: bacs pleins, pieces successives rapides</li>
  <li>Gestion erreurs: capteurs defaillants</li>
</ul>

<h3>Travaux Diriges</h3>

<p><strong>TD1: Automates de base</strong></p>

<p>Exercices:</p>
<ul>
  <li>Modeliser un distributeur de boissons</li>
  <li>Calculer le produit synchrone de deux automates</li>
  <li>Determiner les etats accessibles et co-accessibles</li>
  <li>Minimiser un automate</li>
</ul>

<p><strong>TD2: Reseaux de Petri</strong></p>

<p>Exercices:</p>
<ul>
  <li>Modeliser un systeme producteur-consommateur</li>
  <li>Calculer le graphe de marquages</li>
  <li>Analyser la vivacite et le bornage</li>
  <li>Detecter les blocages potentiels</li>
</ul>

<p><strong>TD: Systeme manufacturier</strong></p>

<p>Modelisation d'une cellule flexible avec:</p>
<ul>
  <li>Machines en parallele</li>
  <li>Buffers limites</li>
  <li>Ressources partagees (robot)</li>
  <li>Analyse des deadlocks</li>
</ul>

<h3>Outils Logiciels</h3>

<p><strong>AutomDiscrete</strong>:</p>
<ul>
  <li>Editeur graphique d'automates</li>
  <li>Simulation pas a pas</li>
  <li>Export en grafcet et code API</li>
  <li>Version utilisee: v4.0</li>
</ul>

<p><strong>Autres outils</strong>:</p>
<ul>
  <li>PIPE: editeur de reseaux de Petri</li>
  <li>TINA: analyse de Petri temporises</li>
  <li>Supremica: synthese de superviseurs</li>
  <li>Stateflow (Simulink): automates dans MATLAB</li>
</ul>

<h3>Methodologie de Conception</h3>

<p><strong>Etapes pour modeliser un systeme</strong>:</p>

<ol>
  <li><strong>Identifier les etats</strong>: situations distinctes du systeme</li>
  <li><strong>Lister les evenements</strong>: actions declenchant changements</li>
  <li><strong>Definir les transitions</strong>: conditions de passage entre etats</li>
  <li><strong>Specifier les actions</strong>: sorties associees aux etats ou transitions</li>
  <li><strong>Valider</strong>: simulation et verification proprietes</li>
</ol>

<p><strong>Choix entre automates et Petri</strong>:</p>

<p>Utiliser automates si:</p>
<ul>
  <li>Systeme avec etats bien definis</li>
  <li>Sequences d'evenements lineaires</li>
  <li>Peu de concurrence</li>
</ul>

<p>Utiliser reseaux de Petri si:</p>
<ul>
  <li>Forte concurrence entre processus</li>
  <li>Ressources partagees</li>
  <li>Synchronisations complexes</li>
  <li>Systemes distribues</li>
</ul>

<hr/>

<h2>PART D: ANALYSE ET REFLEXION</h2>

<h3>Competences acquises</h3>

<p><strong>Modelisation</strong>:</p>
<ul>
  <li>Capacite a abstraire un systeme reel en modele formel</li>
  <li>Choix du formalisme adapte (automate vs Petri)</li>
  <li>Representation graphique claire et structuree</li>
</ul>

<p><strong>Analyse</strong>:</p>
<ul>
  <li>Detection de blocages et situations dangereuses</li>
  <li>Verification de proprietes (vivacite, bornage)</li>
  <li>Evaluation de performances (temps de cycle)</li>
</ul>

<p><strong>Conception</strong>:</p>
<ul>
  <li>Synthese de lois de commande garantissant specifications</li>
  <li>Implementation sur automates programmables</li>
  <li>Tests et validation de systemes automatises</li>
</ul>

<h3>Applications pratiques</h3>

<p>Les SED sont omnipresents dans l'industrie et l'informatique:</p>

<p><strong>Industrie manufacturiere</strong>:</p>
<ul>
  <li>Lignes d'assemblage automobile</li>
  <li>Systemes de tri postal</li>
  <li>Chaines de conditionnement alimentaire</li>
  <li>Ateliers flexibles</li>
</ul>

<p><strong>Transport et logistique</strong>:</p>
<ul>
  <li>Controle de feux de circulation</li>
  <li>Gestion de flottes de vehicules</li>
  <li>Systemes de metro automatique</li>
  <li>Entrepots automatises</li>
</ul>

<p><strong>Informatique</strong>:</p>
<ul>
  <li>Protocoles reseau (TCP/IP)</li>
  <li>Workflows d'entreprise</li>
  <li>Systemes d'exploitation (ordonnancement)</li>
  <li>Applications reactives</li>
</ul>

<p><strong>Robotique</strong>:</p>
<ul>
  <li>Coordination multi-robots</li>
  <li>Taches sequentielles complexes</li>
  <li>Interaction avec environnement</li>
</ul>

<h3>Liens avec autres cours</h3>

<table>
  <thead>
    <tr><th>Cours</th><th>Semestre</th><th>Lien avec SED</th></tr>
  </thead>
  <tbody>
    <tr><td>Logique Sequentielle</td><td>S5</td><td>Machines d'etats, FSM</td></tr>
    <tr><td>Systemes Boucles</td><td>S5</td><td>Automatique, commande</td></tr>
    <tr><td>Programmation Orientee Objet</td><td>S7</td><td>Patterns etat (State pattern)</td></tr>
    <tr><td>Temps Reel</td><td>S8</td><td>Ordonnancement, synchronisation</td></tr>
    <tr><td>Reseaux de Petri</td><td>S8</td><td>Approfondissement Petri</td></tr>
  </tbody>
</table>

<h3>Perspectives et extensions</h3>

<p><strong>Systemes hybrides</strong>:<br/>
Combinaison de dynamique continue (equations differentielles) et evenements discrets.<br/>
Exemple: thermostat (temperature continue, chauffage on/off).</p>

<p><strong>Diagnostic et supervision</strong>:<br/>
Utilisation d'automates observateurs pour detecter pannes et anomalies.</p>

<p><strong>Optimisation</strong>:<br/>
Minimisation temps de cycle, maximisation throughput avec Petri temporises.</p>

<p><strong>Verification formelle</strong>:<br/>
Model checking pour prouver l'absence de bugs dans protocoles et systemes critiques.</p>

<h3>Recommandations</h3>

<p><strong>Pour reussir le cours</strong>:</p>
<ol>
  <li>Bien comprendre la difference etats/evenements</li>
  <li>Pratiquer la modelisation graphique (dessiner les automates)</li>
  <li>Tester systematiquement avec simulation</li>
  <li>Analyser les cas limites (bacs pleins, erreurs capteurs)</li>
</ol>

<p><strong>Ressources complementaires</strong>:</p>
<ul>
  <li>Cassandras &amp; Lafortune: "Introduction to Discrete Event Systems"</li>
  <li>David &amp; Alla: "Reseaux de Petri et Grafcet"</li>
  <li>Cours en ligne sur automates finis (theorie des langages)</li>
</ul>

<h3>Mon opinion</h3>

<p>Ce cours offre une perspective differente de l'automatique classique (systemes continus). Il est particulierement utile pour comprendre les systemes industriels reels ou la notion d'evenements discrets est naturelle.</p>

<p><strong>Points forts</strong>:</p>
<ul>
  <li>Approche graphique intuitive (automates, Petri)</li>
  <li>Applications concretes immediates (industrie)</li>
  <li>Outils logiciels facilitant la modelisation</li>
  <li>Lien direct avec automates programmables</li>
</ul>

<p><strong>Complementarite</strong>:<br/>
Les SED completent parfaitement les cours de systemes continus. Dans la realite, beaucoup de systemes sont hybrides (ex: robot avec controle position continue + sequences de taches discretes).</p>

<p><strong>Importance professionnelle</strong>:<br/>
Competences tres recherchees dans l'automatisation industrielle, la robotique, et les systemes embarques. Les grafcets sont le langage standard des automaticiens.</p>

<p><strong>Applications futures</strong>:<br/>
Ces concepts se retrouvent dans les cours de S8 (Temps Reel, Reseaux de Petri avances) et dans les projets industriels (automatisation, supervision).</p>

<hr/>

<p><strong>Bilan personnel</strong>: Ce cours a apporte une vision complementaire de l'automatique, centree sur les evenements plutot que le temps. La modelisation par automates et reseaux de Petri est intuitive et directement applicable aux systemes industriels. Le TP sur le systeme de tri a permis de concretiser ces concepts avec un cas reel d'automatisation.</p>

</div>

<div class="lang-en">

<h1>Modeling and Control of Discrete Event Systems - S5</h1>

<p><strong>Year</strong>: 2022-2023 (Semester 5)<br/>
<strong>Credits</strong>: 2 ECTS<br/>
<strong>Type</strong>: Control Systems and Automation<br/>
<strong>Instructor</strong>: Vignolles</p>

<hr/>

<h2>PART A: GENERAL OVERVIEW</h2>

<h3>Course Objectives</h3>

<p>This course introduces the modeling and control of Discrete Event Systems (DES), systems whose evolution is triggered by discrete events rather than continuous time. These systems are ubiquitous in industry (production lines, transportation systems), computer science (protocols, workflows), and robotics. The course covers finite automata and Petri nets, which are fundamental tools for modeling, analyzing, and controlling these systems.</p>

<h3>Targeted Skills</h3>

<ul>
  <li>Model industrial systems using automata and Petri nets</li>
  <li>Analyze system properties (liveness, deadlock, reachability)</li>
  <li>Design supervisors to guarantee specifications</li>
  <li>Use simulation software (AutomDiscrete)</li>
  <li>Implement automata on programmable logic controllers (Grafcet)</li>
  <li>Detect and resolve synchronization problems and deadlocks</li>
</ul>

<h3>Organization</h3>

<ul>
  <li><strong>Course hours</strong>: 20h (Lectures: 10h, Tutorials: 6h, Labs: 4h)</li>
  <li><strong>Assessment</strong>: Written exam (70%) + Labs (30%)</li>
  <li><strong>Semester</strong>: 5 (2022-2023)</li>
  <li><strong>Prerequisites</strong>: Logic, basic algebra, fundamentals of control theory</li>
</ul>

<hr/>

<h2>PART B: EXPERIENCE, CONTEXT AND FUNCTION</h2>

<h3>Course Content</h3>

<p>The course is organized around two complementary formalisms: automata and Petri nets.</p>

<h4>1. Discrete Event Systems</h4>

<p><strong>Key characteristics</strong>:</p>

<p>DES evolve through discrete jumps triggered by events:</p>
<ul>
  <li><strong>Discrete states</strong>: finite or countable number of states</li>
  <li><strong>Events</strong>: instantaneous actions causing transitions</li>
  <li><strong>Asynchronous evolution</strong>: no global synchronization</li>
  <li><strong>Non-determinism</strong>: multiple possible transitions from a state</li>
  <li><strong>Concurrency</strong>: multiple simultaneous processes</li>
</ul>

<p><strong>Typical examples</strong>:</p>
<ul>
  <li>Part sorting system (main lab project)</li>
  <li>Traffic lights</li>
  <li>Vending machine</li>
  <li>Manufacturing production line</li>
  <li>Communication protocol</li>
</ul>

<p><strong>Comparison with continuous systems</strong>:</p>

<table>
  <thead>
    <tr><th>Criterion</th><th>Continuous systems</th><th>Discrete systems</th></tr>
  </thead>
  <tbody>
    <tr><td>States</td><td>Continuous (real-valued)</td><td>Discrete (integer-valued)</td></tr>
    <tr><td>Time</td><td>Continuous evolution</td><td>Instantaneous events</td></tr>
    <tr><td>Model</td><td>Differential equations</td><td>Automata, Petri nets</td></tr>
    <tr><td>Example</td><td>Temperature regulation</td><td>Assembly line</td></tr>
  </tbody>
</table>

<h4>2. Finite State Automata</h4>

<p><strong>Definition</strong>:</p>

<p>An automaton is defined by:</p>
<ul>
  <li>E: set of states</li>
  <li>e0: initial state</li>
  <li>&Sigma;: event alphabet</li>
  <li>&delta;: transition function (E &times; &Sigma; &rarr; E)</li>
  <li>Em: marked (accepting) states</li>
</ul>

<p><strong>Graphical representation</strong>:</p>

<pre><code>    [e1] --a--&gt; [e2] --b--&gt; [e3]
     |                       |
     +----------c------------+
</code></pre>

<p>States = circles, transitions = labeled arrows, initial state = incoming arrow.</p>

<p><strong>Tutorial example: Vending machine</strong>:</p>

<p>States:</p>
<ul>
  <li>e0: idle</li>
  <li>e1: 50 cents inserted</li>
  <li>e2: 1 euro inserted</li>
  <li>e3: drink served</li>
</ul>

<p>Events:</p>
<ul>
  <li>p50: insert 50 cents</li>
  <li>p100: insert 1 euro</li>
  <li>serv: serve drink</li>
  <li>annul: cancel</li>
</ul>

<p><strong>Determinism vs non-determinism</strong>:</p>

<p>Deterministic automaton: only one possible transition for each (state, event) pair.<br/>
Non-deterministic automaton: multiple possible transitions.</p>

<p><strong>Operations on automata</strong>:</p>

<p><strong>Synchronous product</strong>: combines two automata with synchronization on shared events.</p>

<p>Used to model systems composed of multiple interacting subsystems.</p>

<p><strong>Accessibility</strong>: a state is accessible if there exists a path from the initial state.</p>

<p><strong>Co-accessibility</strong>: a state is co-accessible if there exists a path to a marked state.</p>

<p><strong>Trim</strong>: automaton containing only accessible and co-accessible states.</p>

<h4>3. Petri Nets</h4>

<p><strong>Basic structure</strong>:</p>

<p>A Petri net consists of:</p>
<ul>
  <li>Places (circles): contain tokens</li>
  <li>Transitions (rectangles): events</li>
  <li>Directed arcs: places &rarr; transitions or transitions &rarr; places</li>
  <li>Marking M: number of tokens in each place</li>
</ul>

<p><strong>Firing rule</strong>:</p>

<p>A transition is fireable if all input places contain at least one token.</p>

<p>After firing:</p>
<ul>
  <li>Remove one token from each input place</li>
  <li>Add one token to each output place</li>
</ul>

<p><strong>Example: Producer-Consumer</strong>:</p>

<pre><code>    (Buffer empty) --produce--&gt; (Buffer full) --consume--&gt; (Buffer empty)
</code></pre>

<p>Places: Buffer empty (1 initial token), Buffer full (0 tokens)<br/>
Transitions: produce, consume</p>

<p><strong>Important properties</strong>:</p>

<p><strong>Boundedness</strong>: maximum number of tokens in a place.</p>
<ul>
  <li>Bounded net: all places have a limited number of tokens</li>
  <li>Safe net: maximum 1 token per place</li>
</ul>

<p><strong>Liveness</strong>: a transition is live if it can always be fired in the future (no permanent deadlock).</p>

<p><strong>Reversibility</strong>: ability to return to the initial marking.</p>

<p><strong>Deadlock</strong>: a marking where no transition is fireable.</p>

<p><strong>Reachability graph analysis</strong>:</p>

<p>A graph representing all reachable markings and the transitions between them.</p>

<p>Allows to:</p>
<ul>
  <li>Detect deadlocks</li>
  <li>Verify boundedness</li>
  <li>Analyze liveness</li>
  <li>Compute reachable states</li>
</ul>

<h4>4. Modeling Industrial Systems</h4>

<p><strong>Part sorting system (Lab)</strong>:</p>

<p>Components:</p>
<ul>
  <li>Input conveyor (T_ON) and output conveyor (C_ON)</li>
  <li>Sensors: conveyor entry, metal detection, other detection</li>
  <li>Output bins: metal (B1), other (B2), reject (B)</li>
  <li>Actuators to direct the parts</li>
</ul>

<p>System states:</p>
<ul>
  <li>State 0: idle (conveyors stopped)</li>
  <li>State 1: startup (conveyors running)</li>
  <li>State 2: part detected (timer delay)</li>
  <li>State 3: part identification</li>
  <li>States 4,5,6: sorting by category</li>
</ul>

<p><strong>Control logic (programmable logic controller)</strong>:</p>

<pre><code>IF (STATE_TRI = 0) THEN
    T_ON := 0;  // Conveyor stopped
    C_ON := 0;
    IF ((P_g1=1) AND (P_g2=1) AND (P_g3=1)) THEN
        STATE_TRI := 1;  // All bins empty, start
    END_IF;
END_IF;

IF (STATE_TRI = 1) THEN
    T_ON := 1;  // Start conveyor
    C_ON := 1;
    IF (Pp_entreeTapis = 1) THEN
        STATE_TRI := 2;  // Part detected
    END_IF;
END_IF;

IF (STATE_TRI = 3) THEN
    IF ((p_autre=1) AND (p_metal=1)) THEN
        STATE_TRI := 5;  // Metal part
    ELSIF (p_autre=1) THEN
        STATE_TRI := 6;  // Other part
    ELSE
        STATE_TRI := 4;  // Reject
    END_IF;
END_IF;
</code></pre>

<p><strong>Timers</strong>:</p>

<p>Timers allow waiting for sensor stabilization:</p>
<ul>
  <li>Timer1, Timer2, Timer3: delays of 2s or 1s</li>
  <li>Prevent false detections</li>
</ul>

<h4>5. Grafcet and Programmable Logic Controllers</h4>

<p><strong>Grafcet (Sequential Function Chart)</strong>:</p>

<p>Graphical representation for industrial automation:</p>
<ul>
  <li>Steps (numbered squares): system states</li>
  <li>Transitions (horizontal bars): passage conditions</li>
  <li>Actions associated with steps</li>
  <li>Directed links</li>
</ul>

<p><strong>Evolution rules</strong>:</p>
<ol>
  <li>Initial step is active at startup</li>
  <li>Transition fires if upstream step is active AND condition is true</li>
  <li>Downstream step activation and upstream step deactivation</li>
</ol>

<p><strong>Grafcet &rarr; PLC conversion</strong>:</p>

<p>The Grafcet translates directly into code for PLCs (Programmable Logic Controllers) in structured text or ladder language.</p>

<h4>6. Supervisor Synthesis</h4>

<p><strong>Principle</strong>:</p>

<p>Design a controller (supervisor) that restricts the system behavior to meet specifications.</p>

<p><strong>Typical specifications</strong>:</p>
<ul>
  <li>Avoid deadlocks</li>
  <li>Guarantee safety (forbidden states)</li>
  <li>Maximize productivity</li>
  <li>Enforce mandatory sequences</li>
</ul>

<p><strong>Controllable vs uncontrollable events</strong>:</p>

<p>Controllable: the supervisor can prevent their occurrence (e.g., start machine).<br/>
Uncontrollable: occur spontaneously (e.g., part arrival, failure).</p>

<p><strong>Method</strong>:</p>
<ol>
  <li>Model the system (automaton or Petri net)</li>
  <li>Define specifications (forbidden states or behaviors)</li>
  <li>Compute the supervisor (restrict transitions)</li>
  <li>Verify properties (non-blocking, controllability)</li>
</ol>

<hr/>

<h2>PART C: TECHNICAL ASPECTS</h2>

<h3>Lab Work</h3>

<p><strong>Lab 1: Automatic sorting system</strong></p>

<p>Objective: model and simulate a part sorting system on a conveyor belt using the AutomDiscrete software.</p>

<p><strong>Specifications</strong>:</p>
<ul>
  <li>Sorting into 3 categories: metal, other, reject</li>
  <li>3 output bins with level sensors</li>
  <li>Detection sensors: metal, other material</li>
  <li>Timer delays for stabilization</li>
  <li>Automatic stop if bins are full</li>
</ul>

<p><strong>Automaton-based modeling</strong>:</p>

<p>System states: 7 states (0 to 6)</p>
<ul>
  <li>0: Idle</li>
  <li>1: Conveyor running</li>
  <li>2: Timer delay after detection</li>
  <li>3: Part identification</li>
  <li>4: Reject sorting</li>
  <li>5: Metal sorting</li>
  <li>6: Other sorting</li>
</ul>

<p>Events:</p>
<ul>
  <li>Bins empty (P_g1, P_g2, P_g3)</li>
  <li>Part entered conveyor</li>
  <li>Timer expired</li>
  <li>Metal detected, other detected</li>
  <li>Bins full</li>
</ul>

<p><strong>AutomDiscrete software implementation</strong>:</p>

<p>Graphical tool allowing:</p>
<ul>
  <li>Drawing the automaton (states, transitions)</li>
  <li>Defining events and actions</li>
  <li>Simulating system evolution</li>
  <li>Exporting to PLC code</li>
</ul>

<p><strong>Generated code</strong> (excerpt):</p>

<p>Variables:</p>
<ul>
  <li>STATE_TRI: current state</li>
  <li>T_ON, C_ON: conveyor commands</li>
  <li>B_OFF, B1_ON, B2_ON: actuator commands</li>
  <li>P1-P6: internal states</li>
  <li>Timers for delays</li>
</ul>

<p><strong>Testing and validation</strong>:</p>
<ul>
  <li>Nominal scenario: correct sorting by category</li>
  <li>Edge cases: bins full, rapid successive parts</li>
  <li>Error handling: faulty sensors</li>
</ul>

<h3>Tutorials</h3>

<p><strong>Tutorial 1: Basic automata</strong></p>

<p>Exercises:</p>
<ul>
  <li>Model a vending machine</li>
  <li>Compute the synchronous product of two automata</li>
  <li>Determine accessible and co-accessible states</li>
  <li>Minimize an automaton</li>
</ul>

<p><strong>Tutorial 2: Petri Nets</strong></p>

<p>Exercises:</p>
<ul>
  <li>Model a producer-consumer system</li>
  <li>Compute the reachability graph</li>
  <li>Analyze liveness and boundedness</li>
  <li>Detect potential deadlocks</li>
</ul>

<p><strong>Tutorial: Manufacturing system</strong></p>

<p>Modeling a flexible manufacturing cell with:</p>
<ul>
  <li>Parallel machines</li>
  <li>Limited buffers</li>
  <li>Shared resources (robot)</li>
  <li>Deadlock analysis</li>
</ul>

<h3>Software Tools</h3>

<p><strong>AutomDiscrete</strong>:</p>
<ul>
  <li>Graphical automaton editor</li>
  <li>Step-by-step simulation</li>
  <li>Export to Grafcet and PLC code</li>
  <li>Version used: v4.0</li>
</ul>

<p><strong>Other tools</strong>:</p>
<ul>
  <li>PIPE: Petri net editor</li>
  <li>TINA: timed Petri net analysis</li>
  <li>Supremica: supervisor synthesis</li>
  <li>Stateflow (Simulink): automata in MATLAB</li>
</ul>

<h3>Design Methodology</h3>

<p><strong>Steps to model a system</strong>:</p>

<ol>
  <li><strong>Identify states</strong>: distinct situations of the system</li>
  <li><strong>List events</strong>: actions triggering changes</li>
  <li><strong>Define transitions</strong>: conditions for passing between states</li>
  <li><strong>Specify actions</strong>: outputs associated with states or transitions</li>
  <li><strong>Validate</strong>: simulation and property verification</li>
</ol>

<p><strong>Choosing between automata and Petri nets</strong>:</p>

<p>Use automata if:</p>
<ul>
  <li>System with well-defined states</li>
  <li>Linear event sequences</li>
  <li>Little concurrency</li>
</ul>

<p>Use Petri nets if:</p>
<ul>
  <li>High concurrency between processes</li>
  <li>Shared resources</li>
  <li>Complex synchronizations</li>
  <li>Distributed systems</li>
</ul>

<hr/>

<h2>PART D: ANALYSIS AND REFLECTION</h2>

<h3>Acquired Skills</h3>

<p><strong>Modeling</strong>:</p>
<ul>
  <li>Ability to abstract a real system into a formal model</li>
  <li>Choosing the appropriate formalism (automaton vs Petri net)</li>
  <li>Clear and structured graphical representation</li>
</ul>

<p><strong>Analysis</strong>:</p>
<ul>
  <li>Detection of deadlocks and hazardous situations</li>
  <li>Verification of properties (liveness, boundedness)</li>
  <li>Performance evaluation (cycle time)</li>
</ul>

<p><strong>Design</strong>:</p>
<ul>
  <li>Synthesis of control laws guaranteeing specifications</li>
  <li>Implementation on programmable logic controllers</li>
  <li>Testing and validation of automated systems</li>
</ul>

<h3>Practical Applications</h3>

<p>DES are ubiquitous in industry and computer science:</p>

<p><strong>Manufacturing industry</strong>:</p>
<ul>
  <li>Automotive assembly lines</li>
  <li>Postal sorting systems</li>
  <li>Food packaging lines</li>
  <li>Flexible manufacturing cells</li>
</ul>

<p><strong>Transportation and logistics</strong>:</p>
<ul>
  <li>Traffic light control</li>
  <li>Vehicle fleet management</li>
  <li>Automated metro systems</li>
  <li>Automated warehouses</li>
</ul>

<p><strong>Computer science</strong>:</p>
<ul>
  <li>Network protocols (TCP/IP)</li>
  <li>Enterprise workflows</li>
  <li>Operating systems (scheduling)</li>
  <li>Reactive applications</li>
</ul>

<p><strong>Robotics</strong>:</p>
<ul>
  <li>Multi-robot coordination</li>
  <li>Complex sequential tasks</li>
  <li>Environment interaction</li>
</ul>

<h3>Links with Other Courses</h3>

<table>
  <thead>
    <tr><th>Course</th><th>Semester</th><th>Link with DES</th></tr>
  </thead>
  <tbody>
    <tr><td>Sequential Logic</td><td>S5</td><td>State machines, FSM</td></tr>
    <tr><td>Feedback Systems</td><td>S5</td><td>Control theory, command</td></tr>
    <tr><td>Object-Oriented Programming</td><td>S7</td><td>State pattern</td></tr>
    <tr><td>Real-Time Systems</td><td>S8</td><td>Scheduling, synchronization</td></tr>
    <tr><td>Petri Nets</td><td>S8</td><td>Advanced Petri nets</td></tr>
  </tbody>
</table>

<h3>Perspectives and Extensions</h3>

<p><strong>Hybrid systems</strong>:<br/>
Combination of continuous dynamics (differential equations) and discrete events.<br/>
Example: thermostat (continuous temperature, heating on/off).</p>

<p><strong>Diagnosis and supervision</strong>:<br/>
Use of observer automata to detect faults and anomalies.</p>

<p><strong>Optimization</strong>:<br/>
Cycle time minimization, throughput maximization with timed Petri nets.</p>

<p><strong>Formal verification</strong>:<br/>
Model checking to prove the absence of bugs in protocols and safety-critical systems.</p>

<h3>Recommendations</h3>

<p><strong>To succeed in this course</strong>:</p>
<ol>
  <li>Thoroughly understand the difference between states and events</li>
  <li>Practice graphical modeling (draw the automata)</li>
  <li>Systematically test with simulation</li>
  <li>Analyze edge cases (bins full, sensor errors)</li>
</ol>

<p><strong>Additional resources</strong>:</p>
<ul>
  <li>Cassandras &amp; Lafortune: "Introduction to Discrete Event Systems"</li>
  <li>David &amp; Alla: "Petri Nets and Grafcet"</li>
  <li>Online courses on finite automata (formal language theory)</li>
</ul>

<h3>My Opinion</h3>

<p>This course offers a different perspective from classical control theory (continuous systems). It is particularly useful for understanding real industrial systems where the notion of discrete events is natural.</p>

<p><strong>Strengths</strong>:</p>
<ul>
  <li>Intuitive graphical approach (automata, Petri nets)</li>
  <li>Immediate practical applications (industry)</li>
  <li>Software tools facilitating modeling</li>
  <li>Direct link to programmable logic controllers</li>
</ul>

<p><strong>Complementarity</strong>:<br/>
DES perfectly complement continuous systems courses. In reality, many systems are hybrid (e.g., a robot with continuous position control + discrete task sequences).</p>

<p><strong>Professional importance</strong>:<br/>
These skills are highly sought after in industrial automation, robotics, and embedded systems. Grafcets are the standard language of automation engineers.</p>

<p><strong>Future applications</strong>:<br/>
These concepts are revisited in S8 courses (Real-Time Systems, Advanced Petri Nets) and in industrial projects (automation, supervision).</p>

<hr/>

<p><strong>Personal assessment</strong>: This course provided a complementary view of control theory, centered on events rather than time. Modeling with automata and Petri nets is intuitive and directly applicable to industrial systems. The lab on the sorting system allowed me to apply these concepts to a real automation case.</p>

</div>

<div class="back-nav">
  <a href="./my-courses-2022-2023.html" data-i18n-html="back-courses-2022-2023">&#8592; Retour aux Cours 2022-2023</a>
</div>

<em class="lang-fr">Redige par Cedric Chanfreau</em>
<em class="lang-en">Written by Cedric Chanfreau</em>

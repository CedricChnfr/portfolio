---
layout: default
title: "Processus Stochastiques et Files d'Attentes - S8"
date: 2024-10-02 10:56:03 +0200
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

<h1>Processus Stochastiques et Files d'Attentes</h1>

<h2>PARTIE A : GENERALITES</h2>

<h3>Presentation</h3>
<p>Le cours "Processus Stochastiques et Files d'Attentes" etudie les systemes aleatoires evoluant dans le temps et les modeles de files d'attente. Ces outils mathematiques permettent d'analyser et d'optimiser des systemes ou l'aleatoire joue un role central: reseaux de telecommunications, systemes de production, services, trafic routier. La theorie des files d'attente est essentielle pour dimensionner des ressources et predire les performances.</p>

<p><strong>Annee Academique</strong> : 2023-2024<br/>
<strong>Semestre</strong> : 8<br/>
<strong>Categorie</strong> : Mathematiques Appliquees / Recherche Operationnelle</p>

<hr/>

<h2>PARTIE B : PARTIE DESCRIPTIVE</h2>

<h3>Details de l'experience</h3>

<h4>Environnement et contexte</h4>
<p>Le cours combinait theorie probabiliste rigoureuse avec applications pratiques via simulations (Python). Nous avons modelise et analyse divers systemes : guichets de banque, serveurs Web, lignes de production, reseaux telephoniques. Les outils developpes permettent de repondre a des questions cruciales: combien de serveurs necessaires? Quel temps d'attente moyen? Quelle probabilite de saturation?</p>

<h4>Ma fonction</h4>
<p>Dans ce cours, j'ai ete responsable de :</p>
<ul>
<li>Comprendre les processus stochastiques (chaines de Markov, processus de Poisson)</li>
<li>Modeliser des systemes par files d'attente (notation de Kendall)</li>
<li>Calculer les performances (temps d'attente, longueur de file, taux d'utilisation)</li>
<li>Analyser la stabilite des systemes</li>
<li>Optimiser le dimensionnement de ressources</li>
<li>Simuler des systemes complexes</li>
<li>Interpreter les resultats et faire des recommandations</li>
</ul>

<h2>PARTIE C : PARTIE TECHNIQUE</h2>

<p>Cette section explore les aspects techniques des processus stochastiques et des files d'attente.</p>

<h3>Concepts techniques appris</h3>

<h4>1. Variables Aleatoires et Lois de Probabilite</h4>

<p><strong>Lois Discretes</strong> :</p>

<p><strong>Bernoulli</strong> : B(p)</p>
<ul>
<li>Succes (1) avec probabilite p, echec (0) avec 1-p</li>
</ul>

<p><strong>Binomiale</strong> : B(n,p)</p>
<ul>
<li>Nombre de succes sur n essais independants</li>
<li>E[X] = np, Var(X) = np(1-p)</li>
</ul>

<p><strong>Geometrique</strong> : G(p)</p>
<ul>
<li>Nombre d'essais avant premier succes</li>
<li>E[X] = 1/p, propriete sans memoire</li>
</ul>

<p><strong>Poisson</strong> : P(lambda)</p>
<ul>
<li>Nombre d'evenements sur intervalle</li>
<li>P(X=k) = (lambda^k e^(-lambda))/k!</li>
<li>E[X] = Var(X) = lambda</li>
</ul>

<p><strong>Lois Continues</strong> :</p>

<p><strong>Uniforme</strong> : U(a,b)</p>
<ul>
<li>Equiprobable sur [a,b]</li>
</ul>

<p><strong>Exponentielle</strong> : Exp(lambda)</p>
<ul>
<li>Temps entre evenements (processus de Poisson)</li>
<li>f(x) = lambda*e^(-lambda*x) pour x>=0</li>
<li>E[X] = 1/lambda, Var(X) = 1/lambda^2</li>
<li><strong>Propriete sans memoire</strong> : P(X>s+t|X>s) = P(X>t)</li>
</ul>

<p><strong>Normale (Gaussienne)</strong> : N(mu, sigma^2)</p>
<ul>
<li>Courbe en cloche</li>
<li>Theoreme Central Limite</li>
</ul>

<h4>2. Processus de Poisson</h4>

<p><strong>Definition</strong> :</p>
<p>Processus de comptage N(t) modelisant arrivees aleatoires.</p>

<p><strong>Proprietes</strong> :</p>
<ul>
<li>Stationnaire : taux lambda constant</li>
<li>Increments independants</li>
<li>Nombre d'arrivees sur [0,t] : N(t) ~ Poisson(lambda*t)</li>
<li>Temps inter-arrivees : Exp(lambda)</li>
</ul>

<p><strong>Applications</strong> :</p>
<ul>
<li>Arrivees de clients</li>
<li>Pannes d'equipements</li>
<li>Appels telephoniques</li>
<li>Requetes Web</li>
</ul>

<h4>3. Chaines de Markov</h4>

<p><strong>Definition</strong> :</p>
<p>Processus stochastique sans memoire (propriete de Markov) :</p>
<pre><code>P(X_(n+1) | X_0,...,X_n) = P(X_(n+1) | X_n)</code></pre>

<p><strong>Matrice de transition P</strong> :</p>
<pre><code>P_ij = P(X_(n+1)=j | X_n=i)</code></pre>

<p><strong>Chaine homogene</strong> : P constante dans le temps.</p>

<p><strong>Distribution stationnaire pi</strong> :</p>
<pre><code>pi = pi * P
Somme(pi_i) = 1</code></pre>

<p>Si chaine irreductible et aperiodique, distribution stationnaire existe et unique.</p>

<p><strong>Classification des etats</strong> :</p>
<ul>
<li><strong>Recurrent</strong> : reviendra avec probabilite 1</li>
<li><strong>Transient</strong> : peut ne jamais revenir</li>
<li><strong>Absorbant</strong> : P(rester) = 1</li>
</ul>

<h4>4. Notation de Kendall</h4>

<p><strong>A/S/c/K/N/D</strong> :</p>
<ul>
<li><strong>A</strong> : loi d'arrivees (M=Markov/exponentiel, D=deterministe, G=general)</li>
<li><strong>S</strong> : loi de service</li>
<li><strong>c</strong> : nombre de serveurs</li>
<li><strong>K</strong> : capacite max (file + service)</li>
<li><strong>N</strong> : taille population</li>
<li><strong>D</strong> : discipline (FIFO, LIFO, etc.)</li>
</ul>

<p>Souvent abrege : <strong>A/S/c</strong></p>

<p>Exemples :</p>
<ul>
<li><strong>M/M/1</strong> : Poisson/Exp/1 serveur</li>
<li><strong>M/M/c</strong> : Poisson/Exp/c serveurs</li>
<li><strong>M/G/1</strong> : Poisson/General/1 serveur</li>
</ul>

<h4>5. File M/M/1</h4>

<p><strong>Systeme</strong> :</p>
<ul>
<li>Arrivees : Poisson(lambda)</li>
<li>Service : Exp(mu)</li>
<li>1 serveur</li>
<li>Capacite infinie</li>
</ul>

<p><strong>Intensite de trafic</strong> :</p>
<pre><code>rho = lambda / mu</code></pre>

<p><strong>Condition de stabilite</strong> :</p>
<pre><code>rho &lt; 1  (sinon file explose)</code></pre>

<p><strong>Performances a l'etat stationnaire</strong> :</p>

<p><strong>Probabilite de n clients</strong> :</p>
<pre><code>pi_n = (1 - rho) * rho^n</code></pre>

<p><strong>Nombre moyen de clients</strong> :</p>
<pre><code>L = rho / (1 - rho) = lambda / (mu - lambda)</code></pre>

<p><strong>Nombre moyen en file d'attente</strong> :</p>
<pre><code>Lq = rho^2 / (1 - rho) = lambda^2 / (mu * (mu - lambda))</code></pre>

<p><strong>Temps moyen dans le systeme</strong> (Little) :</p>
<pre><code>W = L / lambda = 1 / (mu - lambda)</code></pre>

<p><strong>Temps moyen d'attente</strong> :</p>
<pre><code>Wq = Lq / lambda = lambda / (mu * (mu - lambda))</code></pre>

<h4>6. Loi de Little</h4>

<p><strong>Theoreme fondamental</strong> :</p>
<pre><code>L = lambda * W</code></pre>

<p>Ou :</p>
<ul>
<li>L : nombre moyen de clients dans systeme</li>
<li>lambda : taux d'arrivee</li>
<li>W : temps moyen dans systeme</li>
</ul>

<p><strong>Valable pour</strong> :</p>
<ul>
<li>Tout systeme stable</li>
<li>Arrivees et services quelconques</li>
</ul>

<p><strong>Corollaire</strong> :</p>
<pre><code>Lq = lambda * Wq</code></pre>

<h4>7. File M/M/c</h4>

<p><strong>c serveurs en parallele</strong>.</p>

<p><strong>Intensite de trafic</strong> :</p>
<pre><code>rho = lambda / (c * mu)  (charge par serveur)</code></pre>

<p><strong>Condition de stabilite</strong> :</p>
<pre><code>lambda &lt; c * mu  (ou rho &lt; 1)</code></pre>

<p><strong>Formule d'Erlang C</strong> (probabilite d'attente) :</p>
<pre><code>P(attente) = C(c, lambda/mu)</code></pre>

<p>Formule complexe, souvent tabulee ou calculee numeriquement.</p>

<p><strong>Performances</strong> :</p>
<p>Formules plus complexes que M/M/1, mais meme logique.</p>

<p><strong>Application</strong> : centres d'appels, guichets de banque.</p>

<h4>8. File M/G/1 (Pollaczek-Khinchin)</h4>

<p><strong>Service general</strong> (pas forcement exponentiel).</p>

<p><strong>Intensite de trafic</strong> :</p>
<pre><code>rho = lambda / mu  (avec mu = 1/E[S])</code></pre>

<p><strong>Formule de Pollaczek-Khinchin</strong> :</p>
<pre><code>Lq = (lambda^2 * Var(S) + rho^2) / (2 * (1 - rho))</code></pre>

<p><strong>Implications</strong> :</p>
<ul>
<li>Plus variance du service est grande, plus la file est longue</li>
<li>Service deterministe (Var=0) minimal</li>
</ul>

<p><strong>Cas particuliers</strong> :</p>
<ul>
<li>M/M/1 : Var(S) = 1/mu^2 → retrouve formule classique</li>
<li>M/D/1 : Var(S) = 0 → Lq reduit de moitie</li>
</ul>

<h4>9. Files avec Capacite Limitee</h4>

<p><strong>File M/M/1/K</strong> :</p>
<p>Capacite max K (file + service).</p>

<p><strong>Arrivees refusees</strong> si systeme plein.</p>

<p><strong>Pas de condition de stabilite</strong> (rho peut etre >1).</p>

<p><strong>Probabilite de blocage</strong> :</p>
<pre><code>P_blocage = pi_K = (1 - rho) * rho^K / (1 - rho^(K+1))  si rho != 1
P_blocage = 1 / (K+1)  si rho = 1</code></pre>

<p><strong>Taux effectif d'arrivee</strong> :</p>
<pre><code>lambda_eff = lambda * (1 - P_blocage)</code></pre>

<p><strong>Applications</strong> : buffers limites, systemes avec rejet.</p>

<h4>10. Reseaux de Files d'Attente</h4>

<p><strong>Systemes interconnectes</strong> : sortie d'une file = entree d'une autre.</p>

<p><strong>Reseaux ouverts</strong> : arrivees externes, departs externes.</p>

<p><strong>Reseaux fermes</strong> : nombre fixe de clients circulant.</p>

<p><strong>Theoreme de Jackson</strong> :</p>
<p>Pour reseau ouvert de files M/M/· :</p>
<ul>
<li>Chaque file se comporte comme M/M/· independante</li>
<li>Distribution produit : pi = pi_1 x pi_2 x ... x pi_n</li>
</ul>

<p><strong>Simplification majeure</strong> : analyse file par file.</p>

<p><strong>Applications</strong> : reseaux informatiques, systemes de production.</p>

<h4>11. Optimisation de Systemes</h4>

<p><strong>Problemes typiques</strong> :</p>
<ul>
<li>Combien de serveurs pour temps d'attente acceptable?</li>
<li>Trade-off cout serveurs vs cout d'attente clients</li>
<li>Quelle capacite de buffer?</li>
</ul>

<p><strong>Fonction de cout</strong> :</p>
<pre><code>C = c_s * c + c_w * W</code></pre>
<p>Ou :</p>
<ul>
<li>c_s : cout par serveur</li>
<li>c : nombre de serveurs</li>
<li>c_w : cout d'attente par unite de temps</li>
<li>W : temps moyen d'attente</li>
</ul>

<p><strong>Optimisation</strong> :</p>
<p>Minimiser C en variant c.</p>

<p><strong>Niveaux de Service</strong> :</p>
<p>Exemples :</p>
<ul>
<li>80% des clients servis en moins de 20s</li>
<li>Temps d'attente moyen &lt; 5min</li>
</ul>

<h4>12. Simulation de Files d'Attente</h4>

<p><strong>Simulation a evenements discrets</strong> :</p>

<p><strong>Evenements</strong> :</p>
<ul>
<li>Arrivee client</li>
<li>Debut service</li>
<li>Fin service</li>
</ul>

<p><strong>Algorithme</strong> :</p>
<ol>
<li>Initialiser (file vide, t=0)</li>
<li>Generer evenements futurs (arrivees aleatoires)</li>
<li>Traiter evenement le plus proche dans le temps</li>
<li>Mettre a jour etat systeme</li>
<li>Generer nouveaux evenements si necessaire</li>
<li>Repeter jusqu'a temps final</li>
</ol>

<p><strong>Generateurs aleatoires</strong> :</p>
<ul>
<li>Exponentiel : -ln(U)/lambda ou U~Uniforme(0,1)</li>
<li>Autres lois : methodes de transformation</li>
</ul>

<p><strong>Analyse resultats</strong> :</p>
<ul>
<li>Phase transitoire vs regime stationnaire</li>
<li>Intervalle de confiance (simulations multiples)</li>
</ul>

<p><strong>Avantages simulation</strong> :</p>
<ul>
<li>Systemes complexes (lois non standard, priorites, etc.)</li>
<li>Validation modeles analytiques</li>
</ul>

<h2>PARTIE D : PARTIE ANALYTIQUE</h2>

<h3>Connaissances et competences mobilisees</h3>

<ul>
<li>Probabilites et statistiques</li>
<li>Processus stochastiques (Poisson, Markov)</li>
<li>Modelisation de systemes par files d'attente</li>
<li>Calcul de performances (formules analytiques)</li>
<li>Analyse de stabilite</li>
<li>Optimisation (dimensionnement)</li>
<li>Simulation (Python)</li>
<li>Interpretation et communication de resultats</li>
</ul>

<h3>Auto-evaluation</h3>

<p>Ce cours a ete mathematiquement exigeant mais tres enrichissant. La theorie des files d'attente offre des outils puissants pour analyser des systemes courants dans l'industrie et les services.</p>

<p>Les processus de Poisson et la loi exponentielle sont omnipresents en modelisation. Leur propriete sans memoire les rend mathematiquement maniables et souvent realistes pour modeliser arrivees aleatoires.</p>

<p>La file M/M/1, bien que simple, introduit tous les concepts essentiels. Comprendre intuitivement pourquoi L = rho/(1-rho) explose quand rho tend vers 1 est important. Quand le systeme est proche de la saturation, les files deviennent tres longues.</p>

<p>La loi de Little (L = lambda*W) est remarquablement generale et utile. C'est une des rares relations valables quel que soit le systeme (tant qu'il est stable).</p>

<p>Les files M/M/c et les formules d'Erlang sont pratiques pour dimensionner des centres d'appels ou guichets. La question "combien de serveurs pour un temps d'attente acceptable?" est tres concrete.</p>

<p>La formule de Pollaczek-Khinchin (M/G/1) montre l'impact de la variabilite du service. Reduire la variance (standardiser les processus) ameliore les performances meme a charge egale.</p>

<p>Les reseaux de files (theoreme de Jackson) permettent d'analyser des systemes complexes. La simplification (comportement independant) est puissante mais repose sur hypotheses fortes (Markov).</p>

<p>Les simulations sont necessaires quand les modeles analytiques deviennent intractables (files avec priorites, distributions generales, politiques complexes). Coder des simulations m'a donne une comprehension profonde de la dynamique des files.</p>

<p>L'optimisation cout/performance est au coeur des decisions industrielles. Les outils de ce cours permettent de quantifier les trade-offs et prendre des decisions eclairees.</p>

<h3>Mon avis</h3>

<p>Ce cours fournit des outils essentiels pour l'ingenieur confronte a des systemes avec alea et congestion. Les applications sont omnipresentes.</p>

<p>Points forts :</p>
<ul>
<li>Rigueur mathematique</li>
<li>Modeles analytiques elegants (formules fermees)</li>
<li>Applications variees et concretes</li>
<li>Simulation pour systemes complexes</li>
</ul>

<p>Points a ameliorer :</p>
<ul>
<li>Plus d'etudes de cas industriels</li>
<li>Lien avec theorie du controle (controle admission, regulation)</li>
<li>Files d'attente dans contexte Big Data et cloud</li>
</ul>

<p>Reflexions personnelles :</p>

<p>La theorie des files d'attente a ete developpee il y a un siecle (Erlang pour reseaux telephoniques) mais reste d'actualite. Les problemes fondamentaux (dimensionnement, optimisation) sont les memes, seul le contexte change.</p>

<p>Les limites des modeles doivent etre comprises :</p>
<ul>
<li>Hypotheses (Poisson, exponentiel) pas toujours realistes</li>
<li>Regime stationnaire suppose systeme stable longtemps</li>
<li>Modeles simplifies vs realite complexe</li>
</ul>

<p>Cependant, meme approximatifs, les modeles donnent des ordres de grandeur et intuitions precieux. "All models are wrong, but some are useful."</p>

<p>Applications modernes :</p>
<ul>
<li><strong>Cloud computing</strong> : dimensionnement serveurs, auto-scaling</li>
<li><strong>Reseaux</strong> : routeurs, buffers, QoS</li>
<li><strong>E-commerce</strong> : gestion stocks, livraisons</li>
<li><strong>Sante</strong> : urgences, blocs operatoires</li>
<li><strong>Transport</strong> : trafic, parkings</li>
</ul>

<p>L'explosion du trafic Internet et du cloud a renouvele l'interet pour ces theories. Les data centers utilisent massivement la theorie des files pour optimiser ressources.</p>

<p>Le lien avec l'IA :</p>
<p>Le Machine Learning peut predire les arrivees (lambda variable dans le temps) et adapter dynamiquement les ressources. Combiner modeles stochastiques classiques avec apprentissage automatique est une voie prometteuse.</p>

<p>En conclusion, ce cours sur les processus stochastiques et files d'attente fournit des outils puissants pour modeliser et analyser l'incertitude, les dependances temporelles et les performances des systemes. C'est une complementation essentielle aux cours de signal (aleatoire) et un prerequis pour comprendre beaucoup de problemes d'ingenierie reels.</p>

<hr/>

<h2><span class="lang-fr">Documents de Cours</span></h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4><span class="lang-fr">Polycopie Processus Stochastiques</span></h4>
      <p><span class="lang-fr">Cours complet : chaines de Markov, processus de Poisson, files d'attente et analyse de performance.</span></p>
      <div class="pdf-lazy" data-src="/cours-pdf/S8/Processus-Stochastiques/polycopie.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S8/Processus-Stochastiques/polycopie.pdf" target="_blank"><span class="lang-fr">Telecharger</span></a></p>
    </div>
    <div class="pdf-item">
      <h4><span class="lang-fr">Chaines de Markov a Temps Discret</span></h4>
      <p><span class="lang-fr">DTMC : matrices de transition, probabilites stationnaires, classification d'etats et ergodicite.</span></p>
      <div class="pdf-lazy" data-src="/cours-pdf/S8/Processus-Stochastiques/chaines-markov-discretes.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S8/Processus-Stochastiques/chaines-markov-discretes.pdf" target="_blank"><span class="lang-fr">Telecharger</span></a></p>
    </div>
    <div class="pdf-item">
      <h4><span class="lang-fr">Theorie des Files d'Attente</span></h4>
      <p><span class="lang-fr">Modeles M/M/1, M/M/c, formules de Little, temps d'attente, taux d'occupation et optimisation.</span></p>
      <div class="pdf-lazy" data-src="/cours-pdf/S8/Processus-Stochastiques/files-attente.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S8/Processus-Stochastiques/files-attente.pdf" target="_blank"><span class="lang-fr">Telecharger</span></a></p>
    </div>
  </div>
</div>

</div>

<div class="lang-en">

<h1>Stochastic Processes and Queueing Theory</h1>

<h2>PART A: GENERALITIES</h2>

<h3>Presentation</h3>
<p>The "Stochastic Processes and Queueing Theory" course studies random systems evolving over time and queueing models. These mathematical tools allow us to analyze and optimize systems where randomness plays a central role: telecommunications networks, production systems, services, and road traffic. Queueing theory is essential for sizing resources and predicting performance.</p>

<p><strong>Academic Year</strong>: 2023-2024<br/>
<strong>Semester</strong>: 8<br/>
<strong>Category</strong>: Applied Mathematics / Operations Research</p>

<hr/>

<h2>PART B: DESCRIPTIVE PART</h2>

<h3>Experience Details</h3>

<h4>Environment and Context</h4>
<p>The course combined rigorous probabilistic theory with practical applications through simulations (Python). We modeled and analyzed various systems: bank counters, Web servers, production lines, and telephone networks. The tools developed allow us to answer crucial questions: how many servers are needed? What is the average waiting time? What is the probability of saturation?</p>

<h4>My Function</h4>
<p>In this course, I was responsible for:</p>
<ul>
<li>Understanding stochastic processes (Markov chains, Poisson processes)</li>
<li>Modeling systems using queueing theory (Kendall notation)</li>
<li>Computing performance metrics (waiting time, queue length, utilization rate)</li>
<li>Analyzing system stability</li>
<li>Optimizing resource sizing</li>
<li>Simulating complex systems</li>
<li>Interpreting results and making recommendations</li>
</ul>

<h2>PART C: TECHNICAL PART</h2>

<p>This section explores the technical aspects of stochastic processes and queueing theory.</p>

<h3>Technical Concepts Learned</h3>

<h4>1. Random Variables and Probability Distributions</h4>

<p><strong>Discrete Distributions</strong>:</p>

<p><strong>Bernoulli</strong>: B(p)</p>
<ul>
<li>Success (1) with probability p, failure (0) with 1-p</li>
</ul>

<p><strong>Binomial</strong>: B(n,p)</p>
<ul>
<li>Number of successes over n independent trials</li>
<li>E[X] = np, Var(X) = np(1-p)</li>
</ul>

<p><strong>Geometric</strong>: G(p)</p>
<ul>
<li>Number of trials before first success</li>
<li>E[X] = 1/p, memoryless property</li>
</ul>

<p><strong>Poisson</strong>: P(lambda)</p>
<ul>
<li>Number of events over an interval</li>
<li>P(X=k) = (lambda^k e^(-lambda))/k!</li>
<li>E[X] = Var(X) = lambda</li>
</ul>

<p><strong>Continuous Distributions</strong>:</p>

<p><strong>Uniform</strong>: U(a,b)</p>
<ul>
<li>Equally probable over [a,b]</li>
</ul>

<p><strong>Exponential</strong>: Exp(lambda)</p>
<ul>
<li>Time between events (Poisson process)</li>
<li>f(x) = lambda*e^(-lambda*x) for x>=0</li>
<li>E[X] = 1/lambda, Var(X) = 1/lambda^2</li>
<li><strong>Memoryless property</strong>: P(X>s+t|X>s) = P(X>t)</li>
</ul>

<p><strong>Normal (Gaussian)</strong>: N(mu, sigma^2)</p>
<ul>
<li>Bell curve</li>
<li>Central Limit Theorem</li>
</ul>

<h4>2. Poisson Process</h4>

<p><strong>Definition</strong>:</p>
<p>Counting process N(t) modeling random arrivals.</p>

<p><strong>Properties</strong>:</p>
<ul>
<li>Stationary: constant rate lambda</li>
<li>Independent increments</li>
<li>Number of arrivals on [0,t]: N(t) ~ Poisson(lambda*t)</li>
<li>Inter-arrival times: Exp(lambda)</li>
</ul>

<p><strong>Applications</strong>:</p>
<ul>
<li>Customer arrivals</li>
<li>Equipment failures</li>
<li>Telephone calls</li>
<li>Web requests</li>
</ul>

<h4>3. Markov Chains</h4>

<p><strong>Definition</strong>:</p>
<p>Memoryless stochastic process (Markov property):</p>
<pre><code>P(X_(n+1) | X_0,...,X_n) = P(X_(n+1) | X_n)</code></pre>

<p><strong>Transition matrix P</strong>:</p>
<pre><code>P_ij = P(X_(n+1)=j | X_n=i)</code></pre>

<p><strong>Homogeneous chain</strong>: P constant over time.</p>

<p><strong>Stationary distribution pi</strong>:</p>
<pre><code>pi = pi * P
Sum(pi_i) = 1</code></pre>

<p>If the chain is irreducible and aperiodic, the stationary distribution exists and is unique.</p>

<p><strong>State classification</strong>:</p>
<ul>
<li><strong>Recurrent</strong>: will return with probability 1</li>
<li><strong>Transient</strong>: may never return</li>
<li><strong>Absorbing</strong>: P(staying) = 1</li>
</ul>

<h4>4. Kendall Notation</h4>

<p><strong>A/S/c/K/N/D</strong>:</p>
<ul>
<li><strong>A</strong>: arrival distribution (M=Markov/exponential, D=deterministic, G=general)</li>
<li><strong>S</strong>: service distribution</li>
<li><strong>c</strong>: number of servers</li>
<li><strong>K</strong>: maximum capacity (queue + service)</li>
<li><strong>N</strong>: population size</li>
<li><strong>D</strong>: discipline (FIFO, LIFO, etc.)</li>
</ul>

<p>Often abbreviated: <strong>A/S/c</strong></p>

<p>Examples:</p>
<ul>
<li><strong>M/M/1</strong>: Poisson/Exp/1 server</li>
<li><strong>M/M/c</strong>: Poisson/Exp/c servers</li>
<li><strong>M/G/1</strong>: Poisson/General/1 server</li>
</ul>

<h4>5. M/M/1 Queue</h4>

<p><strong>System</strong>:</p>
<ul>
<li>Arrivals: Poisson(lambda)</li>
<li>Service: Exp(mu)</li>
<li>1 server</li>
<li>Infinite capacity</li>
</ul>

<p><strong>Traffic intensity</strong>:</p>
<pre><code>rho = lambda / mu</code></pre>

<p><strong>Stability condition</strong>:</p>
<pre><code>rho &lt; 1  (otherwise queue explodes)</code></pre>

<p><strong>Steady-state performance</strong>:</p>

<p><strong>Probability of n customers</strong>:</p>
<pre><code>pi_n = (1 - rho) * rho^n</code></pre>

<p><strong>Average number of customers</strong>:</p>
<pre><code>L = rho / (1 - rho) = lambda / (mu - lambda)</code></pre>

<p><strong>Average number in queue</strong>:</p>
<pre><code>Lq = rho^2 / (1 - rho) = lambda^2 / (mu * (mu - lambda))</code></pre>

<p><strong>Average time in system</strong> (Little):</p>
<pre><code>W = L / lambda = 1 / (mu - lambda)</code></pre>

<p><strong>Average waiting time</strong>:</p>
<pre><code>Wq = Lq / lambda = lambda / (mu * (mu - lambda))</code></pre>

<h4>6. Little's Law</h4>

<p><strong>Fundamental theorem</strong>:</p>
<pre><code>L = lambda * W</code></pre>

<p>Where:</p>
<ul>
<li>L: average number of customers in system</li>
<li>lambda: arrival rate</li>
<li>W: average time in system</li>
</ul>

<p><strong>Valid for</strong>:</p>
<ul>
<li>Any stable system</li>
<li>Any arrival and service distributions</li>
</ul>

<p><strong>Corollary</strong>:</p>
<pre><code>Lq = lambda * Wq</code></pre>

<h4>7. M/M/c Queue</h4>

<p><strong>c servers in parallel</strong>.</p>

<p><strong>Traffic intensity</strong>:</p>
<pre><code>rho = lambda / (c * mu)  (load per server)</code></pre>

<p><strong>Stability condition</strong>:</p>
<pre><code>lambda &lt; c * mu  (or rho &lt; 1)</code></pre>

<p><strong>Erlang C formula</strong> (probability of waiting):</p>
<pre><code>P(wait) = C(c, lambda/mu)</code></pre>

<p>Complex formula, often tabulated or computed numerically.</p>

<p><strong>Performance</strong>:</p>
<p>Formulas more complex than M/M/1, but same logic.</p>

<p><strong>Application</strong>: call centers, bank counters.</p>

<h4>8. M/G/1 Queue (Pollaczek-Khinchin)</h4>

<p><strong>General service</strong> (not necessarily exponential).</p>

<p><strong>Traffic intensity</strong>:</p>
<pre><code>rho = lambda / mu  (with mu = 1/E[S])</code></pre>

<p><strong>Pollaczek-Khinchin formula</strong>:</p>
<pre><code>Lq = (lambda^2 * Var(S) + rho^2) / (2 * (1 - rho))</code></pre>

<p><strong>Implications</strong>:</p>
<ul>
<li>The greater the service variance, the longer the queue</li>
<li>Deterministic service (Var=0) is minimal</li>
</ul>

<p><strong>Special cases</strong>:</p>
<ul>
<li>M/M/1: Var(S) = 1/mu^2 → recovers the classical formula</li>
<li>M/D/1: Var(S) = 0 → Lq is halved</li>
</ul>

<h4>9. Queues with Limited Capacity</h4>

<p><strong>M/M/1/K Queue</strong>:</p>
<p>Maximum capacity K (queue + service).</p>

<p><strong>Arrivals rejected</strong> if system is full.</p>

<p><strong>No stability condition</strong> (rho can be >1).</p>

<p><strong>Blocking probability</strong>:</p>
<pre><code>P_blocking = pi_K = (1 - rho) * rho^K / (1 - rho^(K+1))  if rho != 1
P_blocking = 1 / (K+1)  if rho = 1</code></pre>

<p><strong>Effective arrival rate</strong>:</p>
<pre><code>lambda_eff = lambda * (1 - P_blocking)</code></pre>

<p><strong>Applications</strong>: limited buffers, systems with rejection.</p>

<h4>10. Queueing Networks</h4>

<p><strong>Interconnected systems</strong>: output of one queue = input to another.</p>

<p><strong>Open networks</strong>: external arrivals, external departures.</p>

<p><strong>Closed networks</strong>: fixed number of customers circulating.</p>

<p><strong>Jackson's Theorem</strong>:</p>
<p>For an open network of M/M/· queues:</p>
<ul>
<li>Each queue behaves as an independent M/M/· queue</li>
<li>Product-form distribution: pi = pi_1 x pi_2 x ... x pi_n</li>
</ul>

<p><strong>Major simplification</strong>: queue-by-queue analysis.</p>

<p><strong>Applications</strong>: computer networks, production systems.</p>

<h4>11. System Optimization</h4>

<p><strong>Typical problems</strong>:</p>
<ul>
<li>How many servers for an acceptable waiting time?</li>
<li>Trade-off between server cost vs customer waiting cost</li>
<li>What buffer capacity?</li>
</ul>

<p><strong>Cost function</strong>:</p>
<pre><code>C = c_s * c + c_w * W</code></pre>
<p>Where:</p>
<ul>
<li>c_s: cost per server</li>
<li>c: number of servers</li>
<li>c_w: waiting cost per unit of time</li>
<li>W: average waiting time</li>
</ul>

<p><strong>Optimization</strong>:</p>
<p>Minimize C by varying c.</p>

<p><strong>Service Levels</strong>:</p>
<p>Examples:</p>
<ul>
<li>80% of customers served in less than 20s</li>
<li>Average waiting time &lt; 5min</li>
</ul>

<h4>12. Queueing Simulation</h4>

<p><strong>Discrete-event simulation</strong>:</p>

<p><strong>Events</strong>:</p>
<ul>
<li>Customer arrival</li>
<li>Service start</li>
<li>Service end</li>
</ul>

<p><strong>Algorithm</strong>:</p>
<ol>
<li>Initialize (empty queue, t=0)</li>
<li>Generate future events (random arrivals)</li>
<li>Process the nearest event in time</li>
<li>Update system state</li>
<li>Generate new events if necessary</li>
<li>Repeat until final time</li>
</ol>

<p><strong>Random generators</strong>:</p>
<ul>
<li>Exponential: -ln(U)/lambda where U~Uniform(0,1)</li>
<li>Other distributions: transformation methods</li>
</ul>

<p><strong>Results analysis</strong>:</p>
<ul>
<li>Transient phase vs steady state</li>
<li>Confidence intervals (multiple simulations)</li>
</ul>

<p><strong>Advantages of simulation</strong>:</p>
<ul>
<li>Complex systems (non-standard distributions, priorities, etc.)</li>
<li>Validation of analytical models</li>
</ul>

<h2>PART D: ANALYTICAL PART</h2>

<h3>Knowledge and Skills Mobilized</h3>

<ul>
<li>Probability and statistics</li>
<li>Stochastic processes (Poisson, Markov)</li>
<li>System modeling using queueing theory</li>
<li>Performance computation (analytical formulas)</li>
<li>Stability analysis</li>
<li>Optimization (resource sizing)</li>
<li>Simulation (Python)</li>
<li>Interpretation and communication of results</li>
</ul>

<h3>Self Evaluation</h3>

<p>This course was mathematically demanding but very rewarding. Queueing theory provides powerful tools for analyzing common systems in industry and services.</p>

<p>Poisson processes and the exponential distribution are ubiquitous in modeling. Their memoryless property makes them mathematically tractable and often realistic for modeling random arrivals.</p>

<p>The M/M/1 queue, although simple, introduces all essential concepts. Intuitively understanding why L = rho/(1-rho) explodes as rho approaches 1 is important. When the system is close to saturation, queues become very long.</p>

<p>Little's law (L = lambda*W) is remarkably general and useful. It is one of the rare relationships valid regardless of the system (as long as it is stable).</p>

<p>M/M/c queues and Erlang formulas are practical for sizing call centers or bank counters. The question "how many servers for an acceptable waiting time?" is very concrete.</p>

<p>The Pollaczek-Khinchin formula (M/G/1) shows the impact of service variability. Reducing variance (standardizing processes) improves performance even at equal load.</p>

<p>Queueing networks (Jackson's theorem) allow analyzing complex systems. The simplification (independent behavior) is powerful but relies on strong assumptions (Markov).</p>

<p>Simulations are necessary when analytical models become intractable (queues with priorities, general distributions, complex policies). Coding simulations gave me a deep understanding of queue dynamics.</p>

<p>Cost/performance optimization is at the heart of industrial decisions. The tools from this course allow quantifying trade-offs and making informed decisions.</p>

<h3>My Opinion</h3>

<p>This course provides essential tools for engineers facing systems with randomness and congestion. The applications are ubiquitous.</p>

<p>Strengths:</p>
<ul>
<li>Mathematical rigor</li>
<li>Elegant analytical models (closed-form formulas)</li>
<li>Varied and concrete applications</li>
<li>Simulation for complex systems</li>
</ul>

<p>Areas for improvement:</p>
<ul>
<li>More industrial case studies</li>
<li>Connection with control theory (admission control, regulation)</li>
<li>Queueing theory in the context of Big Data and cloud</li>
</ul>

<p>Personal reflections:</p>

<p>Queueing theory was developed a century ago (Erlang for telephone networks) but remains current. The fundamental problems (sizing, optimization) are the same; only the context changes.</p>

<p>The limitations of models must be understood:</p>
<ul>
<li>Assumptions (Poisson, exponential) are not always realistic</li>
<li>Steady state assumes the system has been stable for a long time</li>
<li>Simplified models vs complex reality</li>
</ul>

<p>However, even when approximate, models provide valuable orders of magnitude and intuitions. "All models are wrong, but some are useful."</p>

<p>Modern applications:</p>
<ul>
<li><strong>Cloud computing</strong>: server sizing, auto-scaling</li>
<li><strong>Networks</strong>: routers, buffers, QoS</li>
<li><strong>E-commerce</strong>: inventory management, deliveries</li>
<li><strong>Healthcare</strong>: emergency rooms, operating theaters</li>
<li><strong>Transportation</strong>: traffic, parking</li>
</ul>

<p>The explosion of Internet traffic and cloud computing has renewed interest in these theories. Data centers massively use queueing theory to optimize resources.</p>

<p>The connection with AI:</p>
<p>Machine Learning can predict arrivals (time-varying lambda) and dynamically adapt resources. Combining classical stochastic models with machine learning is a promising avenue.</p>

<p>In conclusion, this course on stochastic processes and queueing theory provides powerful tools for modeling and analyzing uncertainty, temporal dependencies, and system performance. It is an essential complement to signal processing courses (random signals) and a prerequisite for understanding many real engineering problems.</p>

<hr/>

<h2><span class="lang-en">Course Documents</span></h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4><span class="lang-en">Stochastic Processes Lecture Notes</span></h4>
      <p><span class="lang-en">Complete course: Markov chains, Poisson processes, queueing theory and performance analysis.</span></p>
      <div class="pdf-lazy" data-src="/cours-pdf/S8/Processus-Stochastiques/polycopie.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S8/Processus-Stochastiques/polycopie.pdf" target="_blank"><span class="lang-en">Download</span></a></p>
    </div>
    <div class="pdf-item">
      <h4><span class="lang-en">Discrete-Time Markov Chains</span></h4>
      <p><span class="lang-en">DTMC: transition matrices, stationary probabilities, state classification and ergodicity.</span></p>
      <div class="pdf-lazy" data-src="/cours-pdf/S8/Processus-Stochastiques/chaines-markov-discretes.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S8/Processus-Stochastiques/chaines-markov-discretes.pdf" target="_blank"><span class="lang-en">Download</span></a></p>
    </div>
    <div class="pdf-item">
      <h4><span class="lang-en">Queueing Theory</span></h4>
      <p><span class="lang-en">M/M/1, M/M/c models, Little's formulas, waiting times, utilization rates and optimization.</span></p>
      <div class="pdf-lazy" data-src="/cours-pdf/S8/Processus-Stochastiques/files-attente.pdf" style="width:100%;height:800px;">
        <button type="button" class="pdf-lazy-btn" data-i18n="pdf-lazy-btn">📄 Afficher le PDF</button>
      </div>
      <p><a href="/cours-pdf/S8/Processus-Stochastiques/files-attente.pdf" target="_blank"><span class="lang-en">Download</span></a></p>
    </div>
  </div>
</div>

</div>

<div class="back-nav">
    <a href="./my-courses-2023-2024.html" data-i18n-html="back-courses-2023-2024">&larr; Retour aux Cours 2023-2024</a>
</div>

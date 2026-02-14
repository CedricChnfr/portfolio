---
layout: default
title: "Machine Learning - S8"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
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

<p><strong>Cours connexes</strong> :</p>
<ul>
<li><a href="../2024-2025/embedded-ia-iot.html">Embedded IA for IoT - S9</a> - Application de l'IA sur objets embarques</li>
<li><a href="./processus-stochastiques.html">Processus Stochastiques - S8</a> - Fondements probabilistes du ML</li>
</ul>

<hr>

<h1>Machine Learning</h1>

<h2>PARTIE A : GENERALITES</h2>

<h3>Presentation</h3>
<p>Le cours "Machine Learning" introduit les concepts fondamentaux de l'apprentissage automatique, permettant aux machines d'apprendre a partir de donnees sans etre explicitement programmees. Ce cours couvre les algorithmes classiques d'apprentissage supervise et non supervise, ainsi que leur implementation pratique avec Python et scikit-learn.</p>

<p><strong>Annee Academique</strong> : 2023-2024<br/>
<strong>Semestre</strong> : 8<br/>
<strong>Categorie</strong> : Intelligence Artificielle / Data Science</p>

<hr/>

<h2>PARTIE B : PARTIE DESCRIPTIVE</h2>

<h3>Details de l'experience</h3>

<h4>Environnement et contexte</h4>
<p>Le cours combinait theorie mathematique (statistiques, algebre lineaire, optimisation) avec implementation pratique en Python. Nous avons travaille sur des datasets reels (Iris, MNIST, etc.) et utilise des bibliotheques standard (NumPy, pandas, scikit-learn, matplotlib) pour developper des modeles predictifs.</p>

<h4>Ma fonction</h4>
<p>Dans ce cours, j'ai ete responsable de :</p>
<ul>
<li>Comprendre les fondements theoriques du Machine Learning</li>
<li>Pretraiter et explorer des donnees (nettoyage, visualisation, feature engineering)</li>
<li>Implementer des algorithmes d'apprentissage supervise (regression, classification)</li>
<li>Appliquer des techniques d'apprentissage non supervise (clustering, reduction de dimensionnalite)</li>
<li>Evaluer et optimiser les modeles (cross-validation, hyperparametres)</li>
<li>Interpreter les resultats et identifier les biais</li>
<li>Developper des pipelines ML complets de bout en bout</li>
</ul>

<h2>PARTIE C : PARTIE TECHNIQUE</h2>

<p>Cette section explore les aspects techniques du Machine Learning.</p>

<h3>Concepts techniques appris</h3>

<h4>1. Types d'Apprentissage</h4>

<p><strong>Apprentissage Supervise</strong> :<br/>
Apprendre a partir de donnees etiquetees (X, y).</p>
<ul>
<li><strong>Regression</strong> : predire valeur continue</li>
<li><strong>Classification</strong> : predire classe discrete</li>
</ul>

<p><strong>Apprentissage Non Supervise</strong> :<br/>
Trouver structure cachee dans donnees non etiquetees.</p>
<ul>
<li><strong>Clustering</strong> : regrouper donnees similaires</li>
<li><strong>Reduction de dimensionnalite</strong> : PCA, t-SNE</li>
</ul>

<p><strong>Apprentissage par Renforcement</strong> :<br/>
Agent apprend par interaction (recompenses/punitions).<br/>
(Non couvert en detail dans ce cours)</p>

<h4>2. Regression Lineaire</h4>

<p><strong>Modele</strong> :</p>
<pre><code>y = b0 + b1x1 + b2x2 + ... + bnxn + e
ou en vectoriel: y = X^T b + e</code></pre>

<p><strong>Fonction de cout</strong> (MSE) :</p>
<pre><code>J(b) = (1/2m) S(h(x(i)) - y(i))^2</code></pre>

<p><strong>Solution analytique</strong> (Normal Equation) :</p>
<pre><code>b = (X^T X)^(-1) X^T y</code></pre>

<p><strong>Gradient Descent</strong> :</p>
<pre><code>b := b - a * grad(J(b))</code></pre>

<p><strong>Regularisation</strong> :</p>
<ul>
<li><strong>Ridge</strong> (L2) : penalise ||b||^2</li>
<li><strong>Lasso</strong> (L1) : penalise ||b||_1 (selection de features)</li>
</ul>

<h4>3. Regression Logistique</h4>

<p><strong>Pour classification binaire</strong>.</p>

<p><strong>Fonction sigmoid</strong> :</p>
<pre><code>sigma(z) = 1 / (1 + e^(-z))</code></pre>

<p><strong>Modele</strong> :</p>
<pre><code>P(y=1|x) = sigma(b^T x)</code></pre>

<p><strong>Fonction de cout</strong> (cross-entropy) :</p>
<pre><code>J(b) = -(1/m) S[y log(h(x)) + (1-y) log(1-h(x))]</code></pre>

<p><strong>Optimisation</strong> : Gradient Descent</p>

<p><strong>Extension multiclasse</strong> : Softmax Regression</p>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S8/machine-learning/reseau-neurones.svg" alt="Reseau de neurones multicouche"
       style="max-width: 500px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Architecture d'un perceptron multicouche avec propagation avant</p>
</div>

<h4>4. Arbres de Decision</h4>

<p><strong>Principe</strong> :<br/>
Partitionner l'espace des features par tests successifs.</p>

<p><strong>Construction</strong> :</p>
<ul>
<li>Choisir feature et seuil qui maximisent gain d'information</li>
<li>Repeter recursivement sur sous-ensembles</li>
</ul>

<p><strong>Criteres de split</strong> :</p>
<ul>
<li><strong>Gini Impurity</strong> : 1 - S p^2_i</li>
<li><strong>Entropy</strong> : -S p_i log(p_i)</li>
</ul>

<p><strong>Avantages</strong> :</p>
<ul>
<li>Interpretable</li>
<li>Gere non-linearites</li>
<li>Pas de normalisation necessaire</li>
</ul>

<p><strong>Inconvenients</strong> :</p>
<ul>
<li>Overfitting facile</li>
<li>Instable (petite variation donnees = arbre different)</li>
</ul>

<p><strong>Regularisation</strong> :</p>
<ul>
<li>Profondeur max</li>
<li>Nombre min d'echantillons par feuille</li>
<li>Elagage (pruning)</li>
</ul>

<h4>5. Methodes d'Ensemble</h4>

<p><strong>Bagging</strong> (Bootstrap Aggregating) :<br/>
Entrainer plusieurs modeles sur sous-ensembles aleatoires, moyenner predictions.</p>

<p><strong>Random Forest</strong> :<br/>
Bagging d'arbres + selection aleatoire de features a chaque split.</p>
<ul>
<li>Reduit variance</li>
<li>Tres performant</li>
<li>Moins interpretable</li>
</ul>

<p><strong>Boosting</strong> :<br/>
Entrainer modeles sequentiellement, chacun corrigeant erreurs du precedent.</p>

<p><strong>AdaBoost</strong> :<br/>
Ponderer exemples mal classes plus fortement.</p>

<p><strong>Gradient Boosting</strong> :<br/>
Ajuster modele sur residus du modele precedent.</p>

<p><strong>XGBoost</strong> :<br/>
Implementation optimisee de Gradient Boosting.</p>
<ul>
<li>Tres performant (competitions Kaggle)</li>
<li>Regularisation integree</li>
<li>Gestion valeurs manquantes</li>
</ul>

<h4>6. Support Vector Machines (SVM)</h4>

<p><strong>Principe</strong> :<br/>
Trouver hyperplan qui maximise la marge entre classes.</p>

<p><strong>Marge</strong> : distance au point le plus proche de chaque classe.</p>

<p><strong>Hard Margin</strong> : donnees lineairement separables<br/>
<strong>Soft Margin</strong> : tolerer erreurs (parametre C)</p>

<p><strong>Kernel Trick</strong> :<br/>
Projeter donnees dans espace haute dimension ou lineairement separables.</p>

<p><strong>Kernels courants</strong> :</p>
<ul>
<li>Lineaire : K(x,x') = x^T x'</li>
<li>Polynomial : K(x,x') = (x^T x' + c)^d</li>
<li>RBF (Gaussian) : K(x,x') = exp(-gamma||x-x'||^2)</li>
</ul>

<p><strong>SVM pour regression</strong> (SVR) :<br/>
Minimiser erreur hors marge epsilon.</p>

<h4>7. K-Nearest Neighbors (KNN)</h4>

<p><strong>Principe</strong> :<br/>
Classer selon majorite des K voisins les plus proches.</p>

<p><strong>Distance</strong> : Euclidienne, Manhattan, Minkowski</p>

<p><strong>Choix de K</strong> :</p>
<ul>
<li>K petit : sensible au bruit</li>
<li>K grand : lisse, peut ignorer patterns locaux</li>
</ul>

<p><strong>Avantages</strong> :</p>
<ul>
<li>Simple, intuitif</li>
<li>Pas d'entrainement (lazy learning)</li>
<li>Gere non-linearites</li>
</ul>

<p><strong>Inconvenients</strong> :</p>
<ul>
<li>Cout prediction eleve (calculer distances)</li>
<li>Sensible a dimensionnalite (curse of dimensionality)</li>
<li>Necessite normalisation des features</li>
</ul>

<h4>8. Clustering - K-Means</h4>

<p><strong>Objectif</strong> :<br/>
Partitionner donnees en K clusters.</p>

<p><strong>Algorithme</strong> :</p>
<ol>
<li>Initialiser K centroides aleatoirement</li>
<li>Affecter chaque point au centroide le plus proche</li>
<li>Recalculer centroides (moyenne des points)</li>
<li>Repeter 2-3 jusqu'a convergence</li>
</ol>

<p><strong>Inertie</strong> : S ||x - centroide(x)||^2</p>

<p><strong>Choix de K</strong> : methode du coude (elbow method)</p>

<p><strong>Limitations</strong> :</p>
<ul>
<li>K a fixer a priori</li>
<li>Sensible a initialisation</li>
<li>Suppose clusters spheriques</li>
</ul>

<p><strong>Variantes</strong> : K-Means++, Mini-Batch K-Means</p>

<p><strong>Autres algorithmes de clustering</strong> :</p>
<ul>
<li><strong>DBSCAN</strong> : densite, decouvre formes arbitraires</li>
<li><strong>Hierarchical Clustering</strong> : dendrogramme</li>
<li><strong>Gaussian Mixture Models</strong> : probabiliste</li>
</ul>

<h4>9. Reduction de Dimensionnalite - PCA</h4>

<p><strong>PCA</strong> (Principal Component Analysis) :<br/>
Projeter donnees sur axes de variance maximale.</p>

<p><strong>Algorithme</strong> :</p>
<ol>
<li>Centrer donnees (moyenne = 0)</li>
<li>Calculer matrice de covariance</li>
<li>Decomposition en valeurs propres/vecteurs propres</li>
<li>Projeter sur k premiers vecteurs propres</li>
</ol>

<p><strong>Variance expliquee</strong> :<br/>
Proportion de variance totale conservee.</p>

<p><strong>Usages</strong> :</p>
<ul>
<li>Visualisation (projection 2D/3D)</li>
<li>Compression</li>
<li>Reduction bruit</li>
<li>Accelerer algorithmes</li>
</ul>

<p><strong>t-SNE</strong> :<br/>
Projection non-lineaire pour visualisation.<br/>
Preserve structure locale (voisinages).</p>

<h4>10. Evaluation des Modeles</h4>

<p><strong>Classification</strong> :</p>

<p><strong>Matrice de confusion</strong> :</p>
<pre><code>                Predit +    Predit -
Reel +         TP          FN
Reel -         FP          TN</code></pre>

<p><strong>Metriques</strong> :</p>
<ul>
<li><strong>Accuracy</strong> : (TP+TN)/(TP+TN+FP+FN)</li>
<li><strong>Precision</strong> : TP/(TP+FP)</li>
<li><strong>Recall (Sensibilite)</strong> : TP/(TP+FN)</li>
<li><strong>F1-Score</strong> : 2x(PrecisionxRecall)/(Precision+Recall)</li>
</ul>

<p><strong>Courbe ROC</strong> (Receiver Operating Characteristic) :<br/>
TPR vs FPR a differents seuils.</p>

<p><strong>AUC</strong> (Area Under Curve) : aire sous courbe ROC (0.5 a 1).</p>

<p><strong>Regression</strong> :</p>
<ul>
<li><strong>MSE</strong> (Mean Squared Error) : Moyenne des (y - y_hat)^2</li>
<li><strong>RMSE</strong> : racine(MSE)</li>
<li><strong>MAE</strong> (Mean Absolute Error) : Moyenne des |y - y_hat|</li>
<li><strong>R^2</strong> : proportion de variance expliquee</li>
</ul>

<h4>11. Validation et Optimisation</h4>

<p><strong>Train/Test Split</strong> :<br/>
Separer donnees (typiquement 80/20 ou 70/30).</p>

<p><strong>Cross-Validation</strong> :<br/>
K-Fold : diviser en K sous-ensembles, entrainer K fois en utilisant K-1 pour train, 1 pour validation.</p>

<p><strong>Overfitting vs Underfitting</strong> :</p>
<ul>
<li><strong>Overfitting</strong> : modele trop complexe, memorise donnees d'entrainement</li>
<li><strong>Underfitting</strong> : modele trop simple, ne capture pas patterns</li>
</ul>

<p><strong>Courbes d'apprentissage</strong> :<br/>
Erreur train et validation vs taille dataset ou complexite.</p>

<p><strong>Hyperparametres</strong> :<br/>
Parametres non appris (a fixer avant entrainement).</p>

<p><strong>Grid Search</strong> :<br/>
Tester toutes combinaisons d'hyperparametres.</p>

<p><strong>Random Search</strong> :<br/>
Echantillonner aleatoirement combinaisons.</p>

<p><strong>Regularisation</strong> :<br/>
Penaliser complexite (L1, L2, dropout, early stopping).</p>

<h4>12. Feature Engineering</h4>

<p><strong>Importance</strong> :<br/>
"Donnees > Algorithmes". Bonnes features sont cruciales.</p>

<p><strong>Techniques</strong> :</p>
<ul>
<li><strong>Scaling</strong> : MinMaxScaler, StandardScaler</li>
<li><strong>Encoding</strong> : One-Hot pour variables categorielles</li>
<li><strong>Polynomial Features</strong> : creer interactions</li>
<li><strong>Binning</strong> : discretiser variables continues</li>
<li><strong>Log Transform</strong> : pour distributions asymetriques</li>
<li><strong>Feature Selection</strong> : eliminer features redondantes/inutiles</li>
</ul>

<p><strong>Gestion valeurs manquantes</strong> :</p>
<ul>
<li>Suppression (si peu nombreuses)</li>
<li>Imputation (moyenne, mediane, mode, KNN)</li>
</ul>

<p><strong>Detection outliers</strong> :<br/>
Z-score, IQR, isolation forest</p>

<h2>PARTIE D : PARTIE ANALYTIQUE</h2>

<h3>Connaissances et competences mobilisees</h3>

<ul>
<li>Comprehension des algorithmes de Machine Learning</li>
<li>Mathematiques (algebre lineaire, probabilites, optimisation)</li>
<li>Programmation Python (NumPy, pandas, scikit-learn)</li>
<li>Pretraitement et exploration de donnees</li>
<li>Entrainement, evaluation et optimisation de modeles</li>
<li>Interpretation des resultats et diagnostic (overfitting, biais)</li>
<li>Pensee critique sur limitations et biais des modeles</li>
<li>Visualisation de donnees (matplotlib, seaborn)</li>
</ul>

<h3>Auto-evaluation</h3>

<p>Ce cours a ete une decouverte passionnante de l'apprentissage automatique. Le ML transforme de nombreux domaines et comprendre ses mecanismes est devenu essentiel pour tout ingenieur.</p>

<p>La theorie mathematique peut etre intimidante au debut (gradient descent, matrices, optimisation), mais avec la pratique, elle devient intuitive. La regression lineaire, bien que simple, introduit des concepts fondamentaux reutilises dans tous les algorithmes.</p>

<p>Le pretraitement des donnees est souvent sous-estime mais crucial. "Garbage in, garbage out" : un modele ne peut pas compenser des donnees mal preparees. Nettoyer, normaliser, gerer les valeurs manquantes sont des etapes essentielles.</p>

<p>La diversite des algorithmes est impressionnante. Chacun a ses forces et faiblesses. Il n'y a pas de "meilleur" algorithme universel (No Free Lunch Theorem). L'art du ML est de choisir et adapter l'algorithme au probleme.</p>

<p>Les Random Forests et XGBoost sont remarquablement performants sur de nombreux problemes. Leur popularite en competitions Kaggle en temoigne. Cependant, ils sont moins interpretables que des modeles simples.</p>

<p>L'evaluation rigoureuse (cross-validation, metriques adaptees) est critique. L'accuracy seule peut etre trompeuse (classes desequilibrees). Il faut choisir metrique selon contexte (precision vs recall selon cout des erreurs).</p>

<p>L'overfitting est un piege constant. La validation croisee et la regularisation sont essentielles. Voir qu'un modele performe bien sur train mais mal sur test est une lecon importante.</p>

<p>Scikit-learn est une bibliotheque excellente : API coherente, documentation claire, implementations optimisees. Elle permet de se concentrer sur la logique ML plutot que sur les details d'implementation.</p>

<p>Le feature engineering reste largement manuel et creatif. C'est la qu'intervient l'expertise metier. Creer les bonnes features peut faire plus de difference que choisir le bon algorithme.</p>

<h3>Mon avis</h3>

<p>Ce cours est incontournable a l'ere de l'IA. Le Machine Learning est applique partout : moteurs de recherche, recommandations, diagnostics medicaux, voitures autonomes, finance, etc.</p>

<p>Points forts :</p>
<ul>
<li>Couverture large des algorithmes classiques</li>
<li>Equilibre theorie/pratique</li>
<li>Projets pratiques sur donnees reelles</li>
<li>Utilisation de bibliotheques standard (scikit-learn)</li>
</ul>

<p>Points a ameliorer :</p>
<ul>
<li>Plus sur Deep Learning (reseaux de neurones)</li>
<li>Aspects de production (MLOps, deploiement)</li>
<li>Ethique et biais des modeles</li>
<li>Big Data et scalabilite</li>
</ul>

<p>Reflexions personnelles :</p>

<p>Le ML est puissant mais pas magique. Il necessite :</p>
<ul>
<li>Donnees suffisantes et de qualite</li>
<li>Probleme bien formule</li>
<li>Metriques d'evaluation pertinentes</li>
<li>Validation rigoureuse</li>
<li>Interpretation critique des resultats</li>
</ul>

<p>Les limites du ML doivent etre comprises :</p>
<ul>
<li><strong>Biais</strong> : modeles refletent biais des donnees d'entrainement</li>
<li><strong>Generalisabilite</strong> : performance peut degrader sur nouvelles donnees</li>
<li><strong>Explicabilite</strong> : modeles complexes (deep learning) sont des "boites noires"</li>
<li><strong>Causalite</strong> : ML trouve correlations, pas causalite</li>
</ul>

<p>L'ethique est cruciale :</p>
<ul>
<li>Fairness (equite entre groupes)</li>
<li>Transparence et explicabilite</li>
<li>Privacy (donnees sensibles)</li>
<li>Responsabilite (qui est responsable des erreurs ?)</li>
</ul>

<p>Applications professionnelles :</p>

<p>Competences ML applicables dans nombreux domaines :</p>
<ul>
<li><strong>Data Science</strong> : analyse predictive, insights business</li>
<li><strong>Ingenierie produit</strong> : recommandations, personnalisation</li>
<li><strong>Sante</strong> : diagnostic assiste, decouverte de medicaments</li>
<li><strong>Finance</strong> : detection fraude, trading algorithmique</li>
<li><strong>Industrie</strong> : maintenance predictive, optimisation processus</li>
<li><strong>Marketing</strong> : segmentation clients, prediction churn</li>
<li><strong>Cybersecurite</strong> : detection anomalies</li>
</ul>

<p>Le marche du ML est en forte croissance. Competences recherchees :</p>
<ul>
<li>Data Scientist</li>
<li>ML Engineer</li>
<li>Research Scientist (PhD souvent requis)</li>
</ul>

<p>La frontiere avec le Deep Learning :<br/>
Ce cours couvre ML "classique". Le Deep Learning (reseaux neurones profonds) a revolutionne certains domaines (vision, NLP) mais necessite plus de donnees et ressources. Les bases du ML restent essentielles pour comprendre le DL.</p>

<p>L'avenir :</p>
<ul>
<li><strong>AutoML</strong> : automatisation du pipeline ML</li>
<li><strong>Transfer Learning</strong> : reutiliser modeles pre-entraines</li>
<li><strong>Federated Learning</strong> : entrainer sans centraliser donnees</li>
<li><strong>Explainable AI</strong> : rendre modeles interpretables</li>
<li><strong>Quantum ML</strong> : exploiter ordinateurs quantiques</li>
</ul>

<p>Ces bases en Machine Learning nous permettent de concevoir des systemes plus "intelligents", capables d'apprendre et de s'adapter, une competence devenue essentielle dans presque tous les domaines de l'ingenierie moderne.</p>

<hr>

<h2>Documents de Cours</h2>

</div>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">Cours Complet Machine Learning</span>
        <span class="lang-en">Full Machine Learning Course</span>
      </h4>
      <p>
        <span class="lang-fr">Cours complet : apprentissage supervise/non-supervise, reseaux de neurones, arbres de decision, SVM et metriques.</span>
        <span class="lang-en">Complete course: supervised/unsupervised learning, neural networks, decision trees, SVM and metrics.</span>
      </p>
      <embed src="/cours-pdf/S8/Machine-Learning/cours-complet.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S8/Machine-Learning/cours-complet.pdf" target="_blank">
        <span class="lang-fr">Telecharger</span>
        <span class="lang-en">Download</span>
      </a></p>
    </div>
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">Perceptron &amp; Reseaux de Neurones</span>
        <span class="lang-en">Perceptron &amp; Neural Networks</span>
      </h4>
      <p>
        <span class="lang-fr">Slides sur le perceptron : modele lineaire, fonction d'activation, regle d'apprentissage et limitations.</span>
        <span class="lang-en">Slides on the perceptron: linear model, activation function, learning rule and limitations.</span>
      </p>
      <embed src="/cours-pdf/S8/Machine-Learning/perceptron.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S8/Machine-Learning/perceptron.pdf" target="_blank">
        <span class="lang-fr">Telecharger</span>
        <span class="lang-en">Download</span>
      </a></p>
    </div>
    <div class="pdf-item">
      <h4>
        <span class="lang-fr">Reseaux de Neurones Profonds</span>
        <span class="lang-en">Deep Neural Networks</span>
      </h4>
      <p>
        <span class="lang-fr">Architectures multicouches, retropropagation, fonctions d'activation avancees et techniques d'optimisation.</span>
        <span class="lang-en">Multi-layer architectures, backpropagation, advanced activation functions and optimization techniques.</span>
      </p>
      <embed src="/cours-pdf/S8/Machine-Learning/neural-networks.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S8/Machine-Learning/neural-networks.pdf" target="_blank">
        <span class="lang-fr">Telecharger</span>
        <span class="lang-en">Download</span>
      </a></p>
    </div>
  </div>
</div>

<div class="lang-fr">
<hr>
<p><em>Cours suivi en 2023-2024 a l'INSA Toulouse, Departement Genie Electrique et Informatique.</em></p>
</div>

<div class="lang-en">

<p><strong>Related courses</strong>:</p>
<ul>
<li><a href="../2024-2025/embedded-ia-iot.html">Embedded IA for IoT - S9</a> - Applying AI on embedded devices</li>
<li><a href="./processus-stochastiques.html">Stochastic Processes - S8</a> - Probabilistic foundations of ML</li>
</ul>

<hr>

<h1>Machine Learning</h1>

<h2>PART A: GENERALITIES</h2>

<h3>Presentation</h3>
<p>The "Machine Learning" course introduces the fundamental concepts of machine learning, enabling machines to learn from data without being explicitly programmed. This course covers classic supervised and unsupervised learning algorithms, as well as their practical implementation with Python and scikit-learn.</p>

<p><strong>Academic Year</strong>: 2023-2024<br/>
<strong>Semester</strong>: 8<br/>
<strong>Category</strong>: Artificial Intelligence / Data Science</p>

<hr/>

<h2>PART B: DESCRIPTIVE PART</h2>

<h3>Experience Details</h3>

<h4>Environment and Context</h4>
<p>The course combined mathematical theory (statistics, linear algebra, optimization) with practical implementation in Python. We worked on real datasets (Iris, MNIST, etc.) and used standard libraries (NumPy, pandas, scikit-learn, matplotlib) to develop predictive models.</p>

<h4>My Function</h4>
<p>In this course, I was responsible for:</p>
<ul>
<li>Understanding the theoretical foundations of Machine Learning</li>
<li>Preprocessing and exploring data (cleaning, visualization, feature engineering)</li>
<li>Implementing supervised learning algorithms (regression, classification)</li>
<li>Applying unsupervised learning techniques (clustering, dimensionality reduction)</li>
<li>Evaluating and optimizing models (cross-validation, hyperparameters)</li>
<li>Interpreting results and identifying biases</li>
<li>Developing complete end-to-end ML pipelines</li>
</ul>

<h2>PART C: TECHNICAL PART</h2>

<p>This section explores the technical aspects of Machine Learning.</p>

<h3>Technical Concepts Learned</h3>

<h4>1. Types of Learning</h4>

<p><strong>Supervised Learning</strong>:<br/>
Learning from labeled data (X, y).</p>
<ul>
<li><strong>Regression</strong>: predict continuous value</li>
<li><strong>Classification</strong>: predict discrete class</li>
</ul>

<p><strong>Unsupervised Learning</strong>:<br/>
Finding hidden structure in unlabeled data.</p>
<ul>
<li><strong>Clustering</strong>: grouping similar data</li>
<li><strong>Dimensionality Reduction</strong>: PCA, t-SNE</li>
</ul>

<p><strong>Reinforcement Learning</strong>:<br/>
Agent learns through interaction (rewards/penalties).<br/>
(Not covered in detail in this course)</p>

<h4>2. Linear Regression</h4>

<p><strong>Model</strong>:</p>
<pre><code>y = b0 + b1x1 + b2x2 + ... + bnxn + e
or in vector form: y = X^T b + e</code></pre>

<p><strong>Cost Function</strong> (MSE):</p>
<pre><code>J(b) = (1/2m) S(h(x(i)) - y(i))^2</code></pre>

<p><strong>Analytical Solution</strong> (Normal Equation):</p>
<pre><code>b = (X^T X)^(-1) X^T y</code></pre>

<p><strong>Gradient Descent</strong>:</p>
<pre><code>b := b - a * grad(J(b))</code></pre>

<p><strong>Regularization</strong>:</p>
<ul>
<li><strong>Ridge</strong> (L2): penalizes ||b||^2</li>
<li><strong>Lasso</strong> (L1): penalizes ||b||_1 (feature selection)</li>
</ul>

<h4>3. Logistic Regression</h4>

<p><strong>For binary classification</strong>.</p>

<p><strong>Sigmoid function</strong>:</p>
<pre><code>sigma(z) = 1 / (1 + e^(-z))</code></pre>

<p><strong>Model</strong>:</p>
<pre><code>P(y=1|x) = sigma(b^T x)</code></pre>

<p><strong>Cost function</strong> (cross-entropy):</p>
<pre><code>J(b) = -(1/m) S[y log(h(x)) + (1-y) log(1-h(x))]</code></pre>

<p><strong>Optimization</strong>: Gradient Descent</p>

<p><strong>Multiclass extension</strong>: Softmax Regression</p>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S8/machine-learning/reseau-neurones.svg" alt="Multi-layer neural network"
       style="max-width: 500px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Multi-layer perceptron architecture with forward propagation</p>
</div>

<h4>4. Decision Trees</h4>

<p><strong>Principle</strong>:<br/>
Partitioning the feature space through successive tests.</p>

<p><strong>Construction</strong>:</p>
<ul>
<li>Choose feature and threshold that maximize information gain</li>
<li>Repeat recursively on subsets</li>
</ul>

<p><strong>Split criteria</strong>:</p>
<ul>
<li><strong>Gini Impurity</strong>: 1 - S p^2_i</li>
<li><strong>Entropy</strong>: -S p_i log(p_i)</li>
</ul>

<p><strong>Advantages</strong>:</p>
<ul>
<li>Interpretable</li>
<li>Handles non-linearities</li>
<li>No normalization required</li>
</ul>

<p><strong>Disadvantages</strong>:</p>
<ul>
<li>Easy overfitting</li>
<li>Unstable (small data variation = different tree)</li>
</ul>

<p><strong>Regularization</strong>:</p>
<ul>
<li>Max depth</li>
<li>Min number of samples per leaf</li>
<li>Pruning</li>
</ul>

<h4>5. Ensemble Methods</h4>

<p><strong>Bagging</strong> (Bootstrap Aggregating):<br/>
Train multiple models on random subsets, average predictions.</p>

<p><strong>Random Forest</strong>:<br/>
Bagging of trees + random feature selection at each split.</p>
<ul>
<li>Reduces variance</li>
<li>Very performant</li>
<li>Less interpretable</li>
</ul>

<p><strong>Boosting</strong>:<br/>
Train models sequentially, each correcting errors of the previous one.</p>

<p><strong>AdaBoost</strong>:<br/>
Weight misclassified examples more heavily.</p>

<p><strong>Gradient Boosting</strong>:<br/>
Fit model on residuals of the previous model.</p>

<p><strong>XGBoost</strong>:<br/>
Optimized implementation of Gradient Boosting.</p>
<ul>
<li>Very performant (Kaggle competitions)</li>
<li>Built-in regularization</li>
<li>Missing value handling</li>
</ul>

<h4>6. Support Vector Machines (SVM)</h4>

<p><strong>Principle</strong>:<br/>
Find hyperplane that maximizes the margin between classes.</p>

<p><strong>Margin</strong>: distance to the closest point of each class.</p>

<p><strong>Hard Margin</strong>: linearly separable data<br/>
<strong>Soft Margin</strong>: tolerate errors (parameter C)</p>

<p><strong>Kernel Trick</strong>:<br/>
Project data into a high-dimensional space where linearly separable.</p>

<p><strong>Common kernels</strong>:</p>
<ul>
<li>Linear: K(x,x') = x^T x'</li>
<li>Polynomial: K(x,x') = (x^T x' + c)^d</li>
<li>RBF (Gaussian): K(x,x') = exp(-gamma||x-x'||^2)</li>
</ul>

<p><strong>SVM for regression</strong> (SVR):<br/>
Minimize error outside the epsilon margin.</p>

<h4>7. K-Nearest Neighbors (KNN)</h4>

<p><strong>Principle</strong>:<br/>
Classify according to the majority of the K nearest neighbors.</p>

<p><strong>Distance</strong>: Euclidean, Manhattan, Minkowski</p>

<p><strong>Choice of K</strong>:</p>
<ul>
<li>Small K: sensitive to noise</li>
<li>Large K: smooth, may ignore local patterns</li>
</ul>

<p><strong>Advantages</strong>:</p>
<ul>
<li>Simple, intuitive</li>
<li>No training (lazy learning)</li>
<li>Handles non-linearities</li>
</ul>

<p><strong>Disadvantages</strong>:</p>
<ul>
<li>High prediction cost (computing distances)</li>
<li>Sensitive to dimensionality (curse of dimensionality)</li>
<li>Requires feature normalization</li>
</ul>

<h4>8. Clustering - K-Means</h4>

<p><strong>Objective</strong>:<br/>
Partition data into K clusters.</p>

<p><strong>Algorithm</strong>:</p>
<ol>
<li>Initialize K centroids randomly</li>
<li>Assign each point to the nearest centroid</li>
<li>Recompute centroids (mean of points)</li>
<li>Repeat 2-3 until convergence</li>
</ol>

<p><strong>Inertia</strong>: S ||x - centroid(x)||^2</p>

<p><strong>Choice of K</strong>: elbow method</p>

<p><strong>Limitations</strong>:</p>
<ul>
<li>K must be set a priori</li>
<li>Sensitive to initialization</li>
<li>Assumes spherical clusters</li>
</ul>

<p><strong>Variants</strong>: K-Means++, Mini-Batch K-Means</p>

<p><strong>Other clustering algorithms</strong>:</p>
<ul>
<li><strong>DBSCAN</strong>: density-based, discovers arbitrary shapes</li>
<li><strong>Hierarchical Clustering</strong>: dendrogram</li>
<li><strong>Gaussian Mixture Models</strong>: probabilistic</li>
</ul>

<h4>9. Dimensionality Reduction - PCA</h4>

<p><strong>PCA</strong> (Principal Component Analysis):<br/>
Project data onto axes of maximum variance.</p>

<p><strong>Algorithm</strong>:</p>
<ol>
<li>Center data (mean = 0)</li>
<li>Compute covariance matrix</li>
<li>Eigenvalue/eigenvector decomposition</li>
<li>Project onto the first k eigenvectors</li>
</ol>

<p><strong>Explained variance</strong>:<br/>
Proportion of total variance retained.</p>

<p><strong>Uses</strong>:</p>
<ul>
<li>Visualization (2D/3D projection)</li>
<li>Compression</li>
<li>Noise reduction</li>
<li>Speed up algorithms</li>
</ul>

<p><strong>t-SNE</strong>:<br/>
Non-linear projection for visualization.<br/>
Preserves local structure (neighborhoods).</p>

<h4>10. Model Evaluation</h4>

<p><strong>Classification</strong>:</p>

<p><strong>Confusion matrix</strong>:</p>
<pre><code>                Predicted +    Predicted -
Actual +         TP             FN
Actual -         FP             TN</code></pre>

<p><strong>Metrics</strong>:</p>
<ul>
<li><strong>Accuracy</strong>: (TP+TN)/(TP+TN+FP+FN)</li>
<li><strong>Precision</strong>: TP/(TP+FP)</li>
<li><strong>Recall (Sensitivity)</strong>: TP/(TP+FN)</li>
<li><strong>F1-Score</strong>: 2x(PrecisionxRecall)/(Precision+Recall)</li>
</ul>

<p><strong>ROC Curve</strong> (Receiver Operating Characteristic):<br/>
TPR vs FPR at different thresholds.</p>

<p><strong>AUC</strong> (Area Under Curve): area under the ROC curve (0.5 to 1).</p>

<p><strong>Regression</strong>:</p>
<ul>
<li><strong>MSE</strong> (Mean Squared Error): Average of (y - y_hat)^2</li>
<li><strong>RMSE</strong>: sqrt(MSE)</li>
<li><strong>MAE</strong> (Mean Absolute Error): Average of |y - y_hat|</li>
<li><strong>R^2</strong>: proportion of explained variance</li>
</ul>

<h4>11. Validation and Optimization</h4>

<p><strong>Train/Test Split</strong>:<br/>
Split data (typically 80/20 or 70/30).</p>

<p><strong>Cross-Validation</strong>:<br/>
K-Fold: divide into K subsets, train K times using K-1 for training, 1 for validation.</p>

<p><strong>Overfitting vs Underfitting</strong>:</p>
<ul>
<li><strong>Overfitting</strong>: model too complex, memorizes training data</li>
<li><strong>Underfitting</strong>: model too simple, fails to capture patterns</li>
</ul>

<p><strong>Learning curves</strong>:<br/>
Train and validation error vs dataset size or complexity.</p>

<p><strong>Hyperparameters</strong>:<br/>
Parameters not learned (to be set before training).</p>

<p><strong>Grid Search</strong>:<br/>
Test all hyperparameter combinations.</p>

<p><strong>Random Search</strong>:<br/>
Randomly sample combinations.</p>

<p><strong>Regularization</strong>:<br/>
Penalize complexity (L1, L2, dropout, early stopping).</p>

<h4>12. Feature Engineering</h4>

<p><strong>Importance</strong>:<br/>
"Data > Algorithms". Good features are crucial.</p>

<p><strong>Techniques</strong>:</p>
<ul>
<li><strong>Scaling</strong>: MinMaxScaler, StandardScaler</li>
<li><strong>Encoding</strong>: One-Hot for categorical variables</li>
<li><strong>Polynomial Features</strong>: create interactions</li>
<li><strong>Binning</strong>: discretize continuous variables</li>
<li><strong>Log Transform</strong>: for skewed distributions</li>
<li><strong>Feature Selection</strong>: eliminate redundant/useless features</li>
</ul>

<p><strong>Missing value handling</strong>:</p>
<ul>
<li>Deletion (if few)</li>
<li>Imputation (mean, median, mode, KNN)</li>
</ul>

<p><strong>Outlier detection</strong>:<br/>
Z-score, IQR, isolation forest</p>

<h2>PART D: ANALYTICAL PART</h2>

<h3>Knowledge and Skills Mobilized</h3>

<ul>
<li>Understanding Machine Learning algorithms</li>
<li>Mathematics (linear algebra, probability, optimization)</li>
<li>Python programming (NumPy, pandas, scikit-learn)</li>
<li>Data preprocessing and exploration</li>
<li>Model training, evaluation and optimization</li>
<li>Interpreting results and diagnostics (overfitting, bias)</li>
<li>Critical thinking about model limitations and biases</li>
<li>Data visualization (matplotlib, seaborn)</li>
</ul>

<h3>Self Evaluation</h3>

<p>This course was a fascinating introduction to machine learning. ML is transforming many fields and understanding its mechanisms has become essential for any engineer.</p>

<p>The mathematical theory can be intimidating at first (gradient descent, matrices, optimization), but with practice it becomes intuitive. Linear regression, although simple, introduces fundamental concepts reused across all algorithms.</p>

<p>Data preprocessing is often underestimated but crucial. "Garbage in, garbage out": a model cannot compensate for poorly prepared data. Cleaning, normalizing, handling missing values are essential steps.</p>

<p>The diversity of algorithms is impressive. Each has its strengths and weaknesses. There is no universal "best" algorithm (No Free Lunch Theorem). The art of ML is choosing and adapting the algorithm to the problem.</p>

<p>Random Forests and XGBoost are remarkably performant on many problems. Their popularity in Kaggle competitions attests to this. However, they are less interpretable than simpler models.</p>

<p>Rigorous evaluation (cross-validation, appropriate metrics) is critical. Accuracy alone can be misleading (imbalanced classes). The metric must be chosen according to context (precision vs recall depending on error cost).</p>

<p>Overfitting is a constant trap. Cross-validation and regularization are essential. Seeing a model perform well on training data but poorly on test data is an important lesson.</p>

<p>Scikit-learn is an excellent library: consistent API, clear documentation, optimized implementations. It allows focusing on ML logic rather than implementation details.</p>

<p>Feature engineering remains largely manual and creative. This is where domain expertise comes in. Creating the right features can make more difference than choosing the right algorithm.</p>

<h3>My Opinion</h3>

<p>This course is essential in the age of AI. Machine Learning is applied everywhere: search engines, recommendations, medical diagnostics, autonomous vehicles, finance, etc.</p>

<p>Strengths:</p>
<ul>
<li>Broad coverage of classic algorithms</li>
<li>Theory/practice balance</li>
<li>Hands-on projects with real data</li>
<li>Use of standard libraries (scikit-learn)</li>
</ul>

<p>Areas for improvement:</p>
<ul>
<li>More on Deep Learning (neural networks)</li>
<li>Production aspects (MLOps, deployment)</li>
<li>Ethics and model biases</li>
<li>Big Data and scalability</li>
</ul>

<p>Personal reflections:</p>

<p>ML is powerful but not magic. It requires:</p>
<ul>
<li>Sufficient and quality data</li>
<li>Well-formulated problem</li>
<li>Relevant evaluation metrics</li>
<li>Rigorous validation</li>
<li>Critical interpretation of results</li>
</ul>

<p>The limitations of ML must be understood:</p>
<ul>
<li><strong>Bias</strong>: models reflect biases in training data</li>
<li><strong>Generalizability</strong>: performance can degrade on new data</li>
<li><strong>Explainability</strong>: complex models (deep learning) are "black boxes"</li>
<li><strong>Causality</strong>: ML finds correlations, not causality</li>
</ul>

<p>Ethics is crucial:</p>
<ul>
<li>Fairness (equity between groups)</li>
<li>Transparency and explainability</li>
<li>Privacy (sensitive data)</li>
<li>Accountability (who is responsible for errors?)</li>
</ul>

<p>Professional applications:</p>

<p>ML skills applicable in many fields:</p>
<ul>
<li><strong>Data Science</strong>: predictive analysis, business insights</li>
<li><strong>Product Engineering</strong>: recommendations, personalization</li>
<li><strong>Healthcare</strong>: assisted diagnosis, drug discovery</li>
<li><strong>Finance</strong>: fraud detection, algorithmic trading</li>
<li><strong>Industry</strong>: predictive maintenance, process optimization</li>
<li><strong>Marketing</strong>: customer segmentation, churn prediction</li>
<li><strong>Cybersecurity</strong>: anomaly detection</li>
</ul>

<p>The ML market is growing rapidly. In-demand skills:</p>
<ul>
<li>Data Scientist</li>
<li>ML Engineer</li>
<li>Research Scientist (PhD often required)</li>
</ul>

<p>The boundary with Deep Learning:<br/>
This course covers "classic" ML. Deep Learning (deep neural networks) has revolutionized certain fields (vision, NLP) but requires more data and resources. ML fundamentals remain essential for understanding DL.</p>

<p>The future:</p>
<ul>
<li><strong>AutoML</strong>: automation of the ML pipeline</li>
<li><strong>Transfer Learning</strong>: reuse pre-trained models</li>
<li><strong>Federated Learning</strong>: train without centralizing data</li>
<li><strong>Explainable AI</strong>: make models interpretable</li>
<li><strong>Quantum ML</strong>: leverage quantum computers</li>
</ul>

<p>These Machine Learning fundamentals enable us to design "smarter" systems, capable of learning and adapting, a skill that has become essential in nearly every field of modern engineering.</p>

<hr>

<h2>Course Documents</h2>

<!-- Shared PDF sections above -->

<hr>

<p><em>Course taken in 2023-2024 at INSA Toulouse, Department of Electrical and Computer Engineering.</em></p>

</div>

<div class="back-nav">
    <a href="./my-courses-2023-2024.html" data-i18n-html="back-courses-2023-2024">&larr; Retour aux Cours 2023-2024</a>
</div>

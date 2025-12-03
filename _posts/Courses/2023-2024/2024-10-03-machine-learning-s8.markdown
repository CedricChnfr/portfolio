---
layout: default
title: "Machine Learning - S8"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
---

[← Back to My Courses 2023-2024](./my-courses-2023-2024.html)

**🔗 Cours connexes**: 
- [Embedded IA for IoT - S9](../2024-2025/2024-10-03-embedded-ia-iot.html) - Application de l'IA sur objets embarqués
- [Processus Stochastiques - S8](./2024-10-03-processus-stochastiques.html) - Fondements probabilistes du ML

---

# Machine Learning

## PART A: GENERALITIES

### Presentation
Le cours "Machine Learning" introduit les concepts fondamentaux de l'apprentissage automatique, permettant aux machines d'apprendre à partir de données sans être explicitement programmées. Ce cours couvre les algorithmes classiques d'apprentissage supervisé et non supervisé, ainsi que leur implémentation pratique avec Python et scikit-learn.

**Année Académique**: 2023-2024  
**Semestre**: 8  
**Catégorie**: Intelligence Artificielle / Data Science

---

## PART B: DESCRIPTIVE PART

### Experience Details

#### Environment and Context
Le cours combinait théorie mathématique (statistiques, algèbre linéaire, optimisation) avec implémentation pratique en Python. Nous avons travaillé sur des datasets réels (Iris, MNIST, etc.) et utilisé des bibliothèques standard (NumPy, pandas, scikit-learn, matplotlib) pour développer des modèles prédictifs.

#### My Function
Dans ce cours, j'ai été responsable de:
- Comprendre les fondements théoriques du Machine Learning
- Prétraiter et explorer des données (nettoyage, visualisation, feature engineering)
- Implémenter des algorithmes d'apprentissage supervisé (régression, classification)
- Appliquer des techniques d'apprentissage non supervisé (clustering, réduction de dimensionnalité)
- Évaluer et optimiser les modèles (cross-validation, hyperparamètres)
- Interpréter les résultats et identifier les biais
- Développer des pipelines ML complets de bout en bout

## PART C: TECHNICAL PART

Cette section explore les aspects techniques du Machine Learning.

### Technical Concepts Learned

#### 1. Types d'Apprentissage

**Apprentissage Supervisé**:
Apprendre à partir de données étiquetées (X, y).
- **Régression**: prédire valeur continue
- **Classification**: prédire classe discrète

**Apprentissage Non Supervisé**:
Trouver structure cachée dans données non étiquetées.
- **Clustering**: regrouper données similaires
- **Réduction de dimensionnalité**: PCA, t-SNE

**Apprentissage par Renforcement**:
Agent apprend par interaction (récompenses/punitions).
(Non couvert en détail dans ce cours)

#### 2. Régression Linéaire

**Modèle**:
```
y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ + ε
ou en vectoriel: y = X^T β + ε
```

**Fonction de coût** (MSE):
```
J(β) = (1/2m) Σ(h(x⁽ⁱ⁾) - y⁽ⁱ⁾)²
```

**Solution analytique** (Normal Equation):
```
β = (X^T X)⁻¹ X^T y
```

**Gradient Descent**:
```
β := β - α ∇J(β)
```

**Régularisation**:
- **Ridge** (L2): pénalise ||β||²
- **Lasso** (L1): pénalise ||β||₁ (sélection de features)

#### 3. Régression Logistique

**Pour classification binaire**.

**Fonction sigmoid**:
```
σ(z) = 1 / (1 + e^(-z))
```

**Modèle**:
```
P(y=1|x) = σ(β^T x)
```

**Fonction de coût** (cross-entropy):
```
J(β) = -(1/m) Σ[y log(h(x)) + (1-y) log(1-h(x))]
```

**Optimisation**: Gradient Descent

**Extension multiclasse**: Softmax Regression

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S8/machine-learning/reseau-neurones.svg" alt="Réseau de neurones multicouche" 
       style="max-width: 500px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Architecture d'un perceptron multicouche avec propagation avant</p>
</div>

#### 4. Arbres de Décision

**Principe**:
Partitionner l'espace des features par tests successifs.

**Construction**:
- Choisir feature et seuil qui maximisent gain d'information
- Répéter récursivement sur sous-ensembles

**Critères de split**:
- **Gini Impurity**: 1 - Σ p²ᵢ
- **Entropy**: -Σ pᵢ log(pᵢ)

**Avantages**:
- Interprétable
- Gère non-linéarités
- Pas de normalisation nécessaire

**Inconvénients**:
- Overfitting facile
- Instable (petite variation données → arbre différent)

**Régularisation**:
- Profondeur max
- Nombre min d'échantillons par feuille
- Élagage (pruning)

#### 5. Ensembles Methods

**Bagging** (Bootstrap Aggregating):
Entraîner plusieurs modèles sur sous-ensembles aléatoires, moyenner prédictions.

**Random Forest**:
Bagging d'arbres + sélection aléatoire de features à chaque split.
- Réduit variance
- Très performant
- Moins interprétable

**Boosting**:
Entraîner modèles séquentiellement, chacun corrigeant erreurs du précédent.

**AdaBoost**:
Pondérer exemples mal classés plus fortement.

**Gradient Boosting**:
Ajuster modèle sur résidus du modèle précédent.

**XGBoost**:
Implémentation optimisée de Gradient Boosting.
- Très performant (compétitions Kaggle)
- Régularisation intégrée
- Gestion valeurs manquantes

#### 6. Support Vector Machines (SVM)

**Principe**:
Trouver hyperplan qui maximise la marge entre classes.

**Marge**: distance au point le plus proche de chaque classe.

**Hard Margin**: données linéairement séparables
**Soft Margin**: tolérer erreurs (paramètre C)

**Kernel Trick**:
Projeter données dans espace haute dimension où linéairement séparables.

**Kernels courants**:
- Linéaire: K(x,x') = x^T x'
- Polynomial: K(x,x') = (x^T x' + c)^d
- RBF (Gaussian): K(x,x') = exp(-γ||x-x'||²)

**SVM pour régression** (SVR):
Minimiser erreur hors marge ε.

#### 7. K-Nearest Neighbors (KNN)

**Principe**:
Classer selon majorité des K voisins les plus proches.

**Distance**: Euclidienne, Manhattan, Minkowski

**Choix de K**:
- K petit: sensible au bruit
- K grand: lisse, peut ignorer patterns locaux

**Avantages**:
- Simple, intuitif
- Pas d'entraînement (lazy learning)
- Gère non-linéarités

**Inconvénients**:
- Coût prédiction élevé (calculer distances)
- Sensible à dimensionnalité (curse of dimensionality)
- Nécessite normalisation des features

#### 8. Clustering - K-Means

**Objectif**:
Partitionner données en K clusters.

**Algorithme**:
1. Initialiser K centroïdes aléatoirement
2. Affecter chaque point au centroïde le plus proche
3. Recalculer centroïdes (moyenne des points)
4. Répéter 2-3 jusqu'à convergence

**Inertie**: Σ ||x - centroïde(x)||²

**Choix de K**: méthode du coude (elbow method)

**Limitations**:
- K à fixer a priori
- Sensible à initialisation
- Suppose clusters sphériques

**Variantes**: K-Means++, Mini-Batch K-Means

**Autres algorithmes de clustering**:
- **DBSCAN**: densité, découvre formes arbitraires
- **Hierarchical Clustering**: dendrogramme
- **Gaussian Mixture Models**: probabiliste

#### 9. Réduction de Dimensionnalité - PCA

**PCA** (Principal Component Analysis):
Projeter données sur axes de variance maximale.

**Algorithme**:
1. Centrer données (moyenne = 0)
2. Calculer matrice de covariance
3. Décomposition en valeurs propres/vecteurs propres
4. Projeter sur k premiers vecteurs propres

**Variance expliquée**:
Proportion de variance totale conservée.

**Usages**:
- Visualisation (projection 2D/3D)
- Compression
- Réduction bruit
- Accélérer algorithmes

**t-SNE**:
Projection non-linéaire pour visualisation.
Préserve structure locale (voisinages).

#### 10. Évaluation des Modèles

**Classification**:

**Matrice de confusion**:
```
                Prédit +    Prédit -
Réel +         TP          FN
Réel -         FP          TN
```

**Métriques**:
- **Accuracy**: (TP+TN)/(TP+TN+FP+FN)
- **Precision**: TP/(TP+FP)
- **Recall (Sensibilité)**: TP/(TP+FN)
- **F1-Score**: 2×(Precision×Recall)/(Precision+Recall)

**Courbe ROC** (Receiver Operating Characteristic):
TPR vs FPR à différents seuils.

**AUC** (Area Under Curve): aire sous courbe ROC (0.5 à 1).

**Régression**:
- **MSE** (Mean Squared Error): Moyenne des (y - ŷ)²
- **RMSE**: √MSE
- **MAE** (Mean Absolute Error): Moyenne des |y - ŷ|
- **R²**: proportion de variance expliquée

#### 11. Validation et Optimisation

**Train/Test Split**:
Séparer données (typiquement 80/20 ou 70/30).

**Cross-Validation**:
K-Fold: diviser en K sous-ensembles, entraîner K fois en utilisant K-1 pour train, 1 pour validation.

**Overfitting vs Underfitting**:
- **Overfitting**: modèle trop complexe, mémorise données d'entraînement
- **Underfitting**: modèle trop simple, ne capture pas patterns

**Courbes d'apprentissage**:
Erreur train et validation vs taille dataset ou complexité.

**Hyperparamètres**:
Paramètres non appris (à fixer avant entraînement).

**Grid Search**:
Tester toutes combinaisons d'hyperparamètres.

**Random Search**:
Échantillonner aléatoirement combinaisons.

**Régularisation**:
Pénaliser complexité (L1, L2, dropout, early stopping).

#### 12. Feature Engineering

**Importance**:
"Données > Algorithmes". Bonnes features sont cruciales.

**Techniques**:
- **Scaling**: MinMaxScaler, StandardScaler
- **Encoding**: One-Hot pour variables catégorielles
- **Polynomial Features**: créer interactions
- **Binning**: discrétiser variables continues
- **Log Transform**: pour distributions skewed
- **Feature Selection**: éliminer features redondantes/inutiles

**Gestion valeurs manquantes**:
- Suppression (si peu nombreuses)
- Imputation (moyenne, médiane, mode, KNN)

**Détection outliers**:
Z-score, IQR, isolation forest

## PART D: ANALYTICAL PART

### Knowledge and Skills Mobilized

- Compréhension des algorithmes de Machine Learning
- Mathématiques (algèbre linéaire, probabilités, optimisation)
- Programmation Python (NumPy, pandas, scikit-learn)
- Prétraitement et exploration de données
- Entraînement, évaluation et optimisation de modèles
- Interprétation des résultats et diagnostic (overfitting, biais)
- Pensée critique sur limitations et biais des modèles
- Visualisation de données (matplotlib, seaborn)

### Self Evaluation

Ce cours a été une découverte passionnante de l'apprentissage automatique. Le ML transforme de nombreux domaines et comprendre ses mécanismes est devenu essentiel pour tout ingénieur.

La théorie mathématique peut être intimidante au début (gradient descent, matrices, optimisation), mais avec la pratique, elle devient intuitive. La régression linéaire, bien que simple, introduit des concepts fondamentaux réutilisés dans tous les algorithmes.

Le prétraitement des données est souvent sous-estimé mais crucial. "Garbage in, garbage out": un modèle ne peut pas compenser des données mal préparées. Nettoyer, normaliser, gérer les valeurs manquantes sont des étapes essentielles.

La diversité des algorithmes est impressionnante. Chacun a ses forces et faiblesses. Il n'y a pas de "meilleur" algorithme universel (No Free Lunch Theorem). L'art du ML est de choisir et adapter l'algorithme au problème.

Les Random Forests et XGBoost sont remarquablement performants sur de nombreux problèmes. Leur popularité en compétitions Kaggle en témoigne. Cependant, ils sont moins interprétables que des modèles simples.

L'évaluation rigoureuse (cross-validation, métriques adaptées) est critique. L'accuracy seule peut être trompeuse (classes déséquilibrées). Il faut choisir métrique selon contexte (precision vs recall selon coût des erreurs).

L'overfitting est un piège constant. La validation croisée et la régularisation sont essentielles. Voir qu'un modèle performe bien sur train mais mal sur test est une leçon importante.

Scikit-learn est une bibliothèque excellente: API cohérente, documentation claire, implémentations optimisées. Elle permet de se concentrer sur la logique ML plutôt que sur les détails d'implémentation.

Le feature engineering reste largement manuel et créatif. C'est là qu'intervient l'expertise métier. Créer les bonnes features peut faire plus de différence que choisir le bon algorithme.

### My Opinion

Ce cours est incontournable à l'ère de l'IA. Le Machine Learning est appliqué partout: moteurs de recherche, recommandations, diagnostics médicaux, voitures autonomes, finance, etc.

Points forts:
- Couverture large des algorithmes classiques
- Équilibre théorie/pratique
- Projets pratiques sur données réelles
- Utilisation de bibliothèques standard (scikit-learn)

Points à améliorer:
- Plus sur Deep Learning (réseaux de neurones)
- Aspects de production (MLOps, déploiement)
- Éthique et biais des modèles
- Big Data et scalabilité

Réflexions personnelles:

Le ML est puissant mais pas magique. Il nécessite:
- Données suffisantes et de qualité
- Problème bien formulé
- Métriques d'évaluation pertinentes
- Validation rigoureuse
- Interprétation critique des résultats

Les limites du ML doivent être comprises:
- **Biais**: modèles reflètent biais des données d'entraînement
- **Généralisabilité**: performance peut dégrader sur nouvelles données
- **Explicabilité**: modèles complexes (deep learning) sont des "boîtes noires"
- **Causalité**: ML trouve corrélations, pas causalité

L'éthique est cruciale:
- Fairness (équité entre groupes)
- Transparence et explicabilité
- Privacy (données sensibles)
- Responsabilité (qui est responsable des erreurs?)

Applications professionnelles:

Compétences ML applicables dans nombreux domaines:
- **Data Science**: analyse prédictive, insights business
- **Ingénierie produit**: recommandations, personnalisation
- **Santé**: diagnostic assisté, découverte de médicaments
- **Finance**: détection fraude, trading algorithmique
- **Industrie**: maintenance prédictive, optimisation processus
- **Marketing**: segmentation clients, prédiction churn
- **Cybersécurité**: détection anomalies

Le marché du ML est en forte croissance. Compétences recherchées:
- Data Scientist
- ML Engineer
- Research Scientist (PhD souvent requis)

La frontière avec le Deep Learning:
Ce cours couvre ML "classique". Le Deep Learning (réseaux neurones profonds) a révolutionné certains domaines (vision, NLP) mais nécessite plus de données et ressources. Les bases du ML restent essentielles pour comprendre le DL.

L'avenir:
- **AutoML**: automatisation du pipeline ML
- **Transfer Learning**: réutiliser modèles pré-entraînés
- **Federated Learning**: entraîner sans centraliser données
- **Explainable AI**: rendre modèles interprétables
- **Quantum ML**: exploiter ordinateurs quantiques

Ces bases en Machine Learning nous permettent de concevoir des systèmes plus "intelligents", capables d'apprendre et de s'adapter, une compétence devenue essentielle dans presque tous les domaines de l'ingénierie moderne.

---

## 📚 Documents de Cours

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

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>📖 Cours Complet Machine Learning</h4>
      <p>Cours complet : apprentissage supervisé/non-supervisé, réseaux de neurones, arbres de décision, SVM et métriques.</p>
      <embed src="/cours-pdf/S8/Machine-Learning/cours-complet.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S8/Machine-Learning/cours-complet.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>📖 Perceptron & Réseaux de Neurones</h4>
      <p>Slides sur le perceptron : modèle linéaire, fonction d'activation, règle d'apprentissage et limitations.</p>
      <embed src="/cours-pdf/S8/Machine-Learning/perceptron.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S8/Machine-Learning/perceptron.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>📖 Réseaux de Neurones Profonds</h4>
      <p>Architectures multicouches, rétropropagation, fonctions d'activation avancées et techniques d'optimisation.</p>
      <embed src="/cours-pdf/S8/Machine-Learning/neural-networks.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S8/Machine-Learning/neural-networks.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
  </div>
</div>

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
</style>

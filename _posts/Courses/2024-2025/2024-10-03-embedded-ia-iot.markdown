---
layout: default
title:  "Embedded AI for IoT"
date:   2024-10-02 10:56:03 +0200
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

footer {
    display: flex;
    justify-content: space-around;
    margin-top: 20px;
}

.footer-section {
    flex: 1;
    text-align: center;
}

.styled-button {
    display: inline-block;
    width: 100px;
    margin: 10px;
    padding: 15px 30px;
    font-size: 16px;
    color: white;
    background-color: #66B2FF;
    text-decoration: none;
    border-radius: 25px;
    transition: background-color 0.3s, transform 0.3s;
}

.styled-button:hover {
    background-color: #3399FF;
    transform: scale(1.05);
}

.pdf-container {
    display: flex;
    justify-content: center;
    margin: 20px 0;
}

.pdf-container iframe {
    width: 100%;
    height: 600px;
    border: 1px solid #ddd;
    border-radius: 8px;
}
</style>

<div class="back-nav">
    <a href="./my-courses-2024-2025.html">&larr; Retour aux Cours 2024-2025</a>
</div>

# Embedded IA for IoT - Semestre 9

**Annee academique** : 2024-2025
**Semestre** : S9
**Enseignant** : Philippe Leleux
**Categorie** : Intelligence Artificielle Embarquee et Internet des Objets

**Cours connexes** :
- [Machine Learning - S8](../2023-2024/2024-10-03-machine-learning-s8.html) - Fondamentaux du Machine Learning
- [Cloud & Edge Computing - S9](./cloud-edge.html) - Architectures Edge pour l'IA
- [Energy for Connected Objects - S9](./energy-connected-object.html) - Optimisation energetique

---

## PART A - Presentation Generale

<h3 class="section-title">Objectifs du module</h3>

Le cours "Embedded IA for IoT", dispense par Philippe Leleux a l'INSA Toulouse, portait sur l'integration de l'intelligence artificielle dans les systemes embarques et les objets connectes (IoT). L'objectif principal etait de comprendre et de mettre en oeuvre des modeles d'IA capables de fonctionner sur des dispositifs a ressources limitees (microcontroleurs, capteurs intelligents), un domaine en pleine expansion connu sous le nom de TinyML.

**Objectifs pedagogiques** :
- Comprendre les fondamentaux du Machine Learning appliques aux systemes embarques
- Maitriser les techniques de preprocessing des donnees capteurs (normalisation, extraction de caracteristiques, reduction de dimension)
- Apprehender l'analyse de series temporelles issues de capteurs IoT
- Concevoir et entrainer des reseaux de neurones convolutifs (CNN) pour des taches de classification
- Appliquer des techniques d'optimisation de reseaux de neurones pour le deploiement en peripherie (edge) : quantification, elagage, distillation de connaissances
- Deployer des modeles IA optimises sur des dispositifs contraints avec TensorFlow Lite

<h3 class="section-title">Competences visees</h3>

- Maitrise des algorithmes de classification supervises (k-NN, MLP, CNN)
- Competence en reduction de dimensionnalite (PCA) et analyse de series temporelles (DTW)
- Conception d'architectures CNN adaptees aux contraintes embarquees
- Optimisation de modeles par elagage (pruning) et quantification
- Conversion et deploiement de modeles avec TensorFlow Lite
- Evaluation des performances (precision, taille du modele, temps d'inference)

<h3 class="section-title">Organisation du cours</h3>

Le cours combinait des sessions theoriques couvrant les fondamentaux du Machine Learning et du Deep Learning, avec des travaux pratiques permettant d'appliquer ces concepts a des cas d'usage IoT concrets. L'approche pedagogique etait progressive : des bases du ML aux techniques avancees d'optimisation pour le deploiement embarque.

**Format** :
- Cours magistraux : introduction au ML, preprocessing, series temporelles, CNN, optimisation de reseaux de neurones
- TP 1 : Reconnaissance d'activites humaines (HAR) avec DTW, PCA et MLP
- TP 2 : Detection de chutes par CNN, elagage et quantification pour le deploiement embarque

---

## PART B - Experience et Contexte

<h3 class="section-title">Environnement et contexte</h3>

Au cours de ce module, j'ai explore a la fois les aspects theoriques et pratiques de l'integration de l'IA dans les dispositifs IoT. Les sessions de travaux pratiques ont ete particulierement enrichissantes, me permettant d'appliquer les concepts appris en cours a des scenarios concrets. Le defi d'optimiser des modeles d'IA pour les faire fonctionner efficacement sur des dispositifs a ressources contraintes etait a la fois exigeant et gratifiant.

Le cours s'articulait autour de cinq modules theoriques couvrant l'ensemble du pipeline de l'IA embarquee : depuis l'introduction aux concepts fondamentaux du Machine Learning, en passant par le preprocessing des donnees, l'analyse de series temporelles, les reseaux de neurones convolutifs, jusqu'aux techniques d'optimisation pour le deploiement sur des plateformes a ressources limitees.

<h3 class="section-title">Ma fonction</h3>

Dans le cadre de ce cours, j'etais responsable de :
- Comprendre les principes de l'IA et son application dans l'IoT
- Implementer et optimiser des modeles d'IA pour les dispositifs embarques
- Conduire des experiences pour tester l'efficacite et la precision de ces modeles
- Appliquer des techniques de reduction de dimension (PCA) et d'alignement temporel (DTW)
- Concevoir des architectures CNN pour la detection de chutes
- Appliquer des techniques de compression de modeles (elagage, quantification) pour le deploiement embarque

<h3 class="section-title">Outils et ressources utilises</h3>

- **Langages et bibliotheques** : Python, NumPy, scikit-learn, TensorFlow / Keras, TensorFlow Model Optimization Toolkit, TensorFlow Lite
- **Environnement de developpement** : Jupyter Notebook, Anaconda
- **Donnees** : jeux de donnees de capteurs accelerometre, gyroscope, magnetometre et temperature (HAR), dataset CAUCA pour la detection de chutes
- **Concepts cles** : DTW, PCA, k-NN, MLP, CNN, pruning, quantification, TFLite

---

## PART C - Aspects Techniques Detailles

<h3 class="section-title">1. Fondamentaux du Machine Learning pour l'embarque</h3>

Le cours a debute par une introduction aux concepts fondamentaux du Machine Learning, avec un focus sur leur applicabilite aux systemes embarques et IoT.

**Apprentissage supervise** :
L'apprentissage supervise consiste a entrainer un modele a partir de donnees etiquetees, ou chaque exemple d'entrainement est associe a une sortie attendue. Dans le contexte IoT, cela implique typiquement la classification de donnees capteurs en categories predefinies (activites humaines, detection de chutes, reconnaissance de gestes). Les algorithmes etudies comprenaient le k-NN (k-Nearest Neighbors), le MLP (Multi-Layer Perceptron) et les CNN (Convolutional Neural Networks).

**Apprentissage non supervise** :
L'apprentissage non supervise opere sur des donnees non etiquetees pour decouvrir des structures cachees. Dans le contexte de l'IoT embarque, ces techniques sont utiles pour le clustering de donnees capteurs, la detection d'anomalies et la segmentation de signaux. Le cours a aborde l'utilisation de methodes comme le k-medoids pour le regroupement de series temporelles.

**Compromis pour l'embarque** :
Le choix d'un algorithme pour un systeme embarque doit prendre en compte non seulement la precision, mais aussi la complexite computationnelle, la memoire requise et la consommation energetique. Un modele plus simple (k-NN) peut etre preferable a un modele plus precis (CNN profond) si les ressources sont limitees.

<h3 class="section-title">2. Preprocessing des donnees capteurs</h3>

Le preprocessing est une etape cruciale dans tout pipeline de Machine Learning, et encore plus dans le contexte IoT ou les donnees capteurs sont souvent bruitees, heterogenes et de grande dimension.

**Normalisation et mise a l'echelle** :
La normalisation des donnees est essentielle pour garantir que tous les capteurs contribuent de maniere equitable a l'apprentissage. Dans le TP, nous avons utilise le `StandardScaler` de scikit-learn pour standardiser les mesures provenant de differents capteurs (accelerometre, gyroscope, magnetometre, temperature) :

```python
from sklearn.preprocessing import StandardScaler

N, T, S = RawData.shape
X_reshaped = RawData.reshape(N, T*S)

scaler = StandardScaler()
X_scaled_2d = scaler.fit_transform(X_reshaped)
Data = X_scaled_2d.reshape(N, T, S)
```

Cette etape transforme les donnees pour qu'elles aient une moyenne nulle et un ecart-type unitaire, ce qui est particulierement important lorsque les capteurs mesurent des grandeurs physiques tres differentes (acceleration en m/s2, vitesse angulaire en rad/s, champ magnetique en uT).

**Lissage et sous-echantillonnage** :
Les signaux capteurs a haute frequence peuvent contenir du bruit et des informations redondantes. Le lissage par moyennage glissant permet de reduire la dimension temporelle tout en preservant les tendances significatives :

```python
def smooth_signal(X, k):
    for i in range(len(X)):
        Xi = X[i]
        downsample = math.ceil(len(Xi) / k)
        for j in range(downsample):
            Xj = Xi[j*k:min((j+1)*k, len(Xi)),:]
            X[i,j] = np.mean(Xj, axis=0)
    X = X[:,:downsample,:]
    return X

SMOOTH_RATIO = 100
X = smooth_signal(Data, SMOOTH_RATIO)
```

Avec un ratio de lissage de 100, les donnees echantillonnees a 100 Hz sont reduites a 1 Hz, passant de 500 pas temporels a 5 par exemple, ce qui reduit considerablement la complexite computationnelle pour les algorithmes en aval.

**Extraction de caracteristiques** :
L'extraction de caracteristiques pertinentes a partir de donnees brutes capteurs est un enjeu majeur. Plutot que d'utiliser directement les signaux temporels bruts, il est souvent preferable d'extraire des descripteurs statistiques (moyenne, variance, energie, frequence dominante) qui capturent l'essence du signal en un nombre reduit de valeurs.

**Reduction de dimension par PCA** :
L'Analyse en Composantes Principales (PCA) est une technique de reduction de dimensionnalite qui projette les donnees de haute dimension dans un espace de dimension inferieure tout en preservant un maximum de variance. Dans le TP, nous avons utilise la PCA pour reduire le nombre de caracteristiques avant l'application des algorithmes de classification :

```python
from sklearn.decomposition import PCA

# Determination du nombre optimal de composantes
pca = PCA()
pca.fit(X_train)

cumulative_variance = np.cumsum(pca.explained_variance_ratio_)
n_components = np.argmax(cumulative_variance >= 0.99) + 1
print(f"Composantes pour 99% de variance : {n_components}")

# Application de la PCA avec le nombre optimal
pca = PCA(n_components=n_components)
pca.fit(X_train)
X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
```

Le resultat a montre que 13 composantes principales suffisaient a capturer 99% de la variance des donnees, reduisant considerablement la dimension de l'espace de caracteristiques (de 30 dimensions a 13) tout en preservant l'information pertinente pour la classification.

<h3 class="section-title">3. Analyse de series temporelles pour les donnees capteurs IoT</h3>

Les donnees IoT sont intrinsequement temporelles. L'analyse de series temporelles est donc fondamentale pour exploiter les mesures de capteurs dans le temps.

**Dynamic Time Warping (DTW)** :
Le Dynamic Time Warping est un algorithme de programmation dynamique qui mesure la similarite entre deux sequences temporelles pouvant varier en vitesse. Il est particulierement utile lorsque les sequences ne sont pas synchronisees. Dans le TP, nous avons implemente DTW pour aligner des sequences de donnees capteurs pour la reconnaissance d'activites humaines :

```python
def dtw(a, b, distance, w=(1,1,1), gamma=5):
    N = len(a)
    M = len(b)
    g = np.full((N + 1, M + 1), np.inf)
    g[0, 0] = 0

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if abs(i - j) >= gamma:
                g[i, j] = np.inf
                continue
            locald = distance(a[i - 1], b[j - 1])
            g[i, j] = min(
                g[i - 1, j] + w[0] * locald,
                g[i - 1, j - 1] + w[1] * locald,
                g[i, j - 1] + w[2] * locald
            )

    S = g[N, M] / (N + M)
    return S
```

L'algorithme construit une matrice de cout cumulatif `g` en calculant le chemin d'alignement optimal entre deux sequences. Les parametres `w` definissent les contraintes locales (couts des transitions horizontale, diagonale et verticale) et `gamma` definit la contrainte globale (bande de Sakoe-Chiba) qui limite l'ecart maximal autorise entre les indices alignes.

**Validation sur des exemples numeriques et textuels** :

```python
# Exemple 1 : sequences numeriques
a1 = (4, 6, 1)
b1 = (5, 1)
result1 = dtw(a1, b1, lambda x, y: abs(x - y), w=(1, 1, 1), gamma=2)
# Resultat : S = 0.4

# Exemple 2 : sequences de caracteres (bioinformatique)
a2 = ('A', 'T', 'G', 'G', 'T', 'A', 'C', 'G', 'T', 'C')
b2 = ('A', 'A', 'G', 'T', 'A', 'G', 'G', 'C')
def char_distance(x, y):
    return 0 if x == y else 1
result2 = dtw(a2, b2, char_distance, w=(1, 1, 1), gamma=4)
# Resultat : S = 1/6
```

Les contraintes locales affectent le cout de chaque etape individuelle dans le chemin d'alignement, tandis que les contraintes globales limitent la zone de recherche dans la matrice de cout, empechant des alignements trop distordus et reduisant la complexite computationnelle.

**Application a la reconnaissance d'activites (HAR)** :
Le DTW combine avec le k-NN a ete utilise pour classifier 8 activites humaines differentes (couche, assis, debout, marche, velo, marche nordique, aspirateur, repassage) a partir de donnees de capteurs places sur la main, le torse et la cheville. Un encapsuleur `dtw_KNN` a ete cree pour interfacer le DTW avec le `KNeighborsClassifier` de scikit-learn :

```python
def dtw_KNN(x1, x2):
    n = x1.shape[0]
    folds = Data.shape[2]
    x1 = x1.reshape(int(n/folds), folds)
    n = x2.shape[0]
    x2 = x2.reshape(int(n/folds), folds)
    res = dtw(x2, x1, w=(1,1,1), gamma=5, distance=euclidian_distance)
    return res

class KNN:
    def __init__(self, n_neighbors=1, metric=dtw_KNN, n_jobs=-1):
        self.model = KNeighborsClassifier(n_neighbors, metric=self.metric, n_jobs=-1)

    def fit(self, xtrain, y_train):
        m, n, k = xtrain.shape
        xtrain = xtrain.reshape(m, n*k)
        self.model.fit(xtrain, y_train)
```

Les resultats ont montre une precision de 60% avec k=1 pour le k-NN+DTW, mais avec un temps de calcul tres important (plus de 13 minutes pour tester 10 valeurs de k). Cette approche illustre les compromis fondamentaux en IA embarquee entre precision, complexite et temps de calcul.

<h3 class="section-title">4. Classification par k-NN et reseaux de neurones (MLP)</h3>

**k-Nearest Neighbors (k-NN)** :
L'algorithme k-NN est un classificateur non parametrique qui assigne une classe a un echantillon en fonction de la classe majoritaire parmi ses k plus proches voisins. Combine avec le DTW comme metrique de distance, il permet de classifier efficacement des series temporelles :

```python
k_values = range(1, 11)
scores = []

for k in k_values:
    clf = KNN(n_neighbors=k)
    clf.fit(X_train, y_train)
    score = clf.score(X_test, y_test)
    scores.append(score)
    print(f"k={k}, Score={score}")
```

L'avantage du k-NN est sa simplicite et l'absence d'entrainement explicite. Son inconvenient majeur est le cout computationnel de la prediction, qui necessite le calcul de distances avec tous les exemples d'entrainement, ce qui le rend peu adapte aux systemes embarques avec de grands jeux de donnees.

**Multi-Layer Perceptron (MLP)** :
Le MLP est un reseau de neurones artificiels compose de couches multiples (entree, couches cachees, sortie) connectees par des poids appris par retropropagation du gradient. Apres reduction de dimension par PCA, le MLP a ete utilise pour la classification d'activites :

```python
from sklearn.neural_network import MLPClassifier

mlp = MLPClassifier(hidden_layer_sizes=(50, 25), max_iter=300,
                    activation='relu', random_state=42)
mlp.fit(X_train_pca, y_train)
y_pred_mlp = mlp.predict(X_test_pca)
accuracy = accuracy_score(y_test, y_pred_mlp)
# Resultat : precision de 98%
```

La combinaison PCA + MLP a donne des resultats nettement superieurs au k-NN+DTW (98% contre 60%), avec un temps d'execution tres inferieur. Le MLP est plus rapide en prediction, demande moins de memoire, et offre une bien meilleure scalabilite, bien que sa configuration (nombre de couches, neurones, hyperparametres) soit plus complexe.

| Methode | Precision | Temps d'execution | Scalabilite | Memoire |
|---------|-----------|-------------------|-------------|---------|
| k-NN + DTW | ~60% | Tres long (>13 min) | Faible | Elevee |
| PCA + MLP | ~98% | Rapide (<1 min) | Bonne | Moderee |

<h3 class="section-title">5. Architectures de reseaux de neurones convolutifs (CNN)</h3>

Les CNN sont des architectures de Deep Learning concues pour traiter des donnees structurees spatialement (images) ou temporellement. Dans le TP2, nous avons utilise les CNN pour la detection de chutes a partir d'images du dataset CAUCA.

**Couches de convolution** :
Les couches convolutives appliquent des filtres (noyaux) qui glissent sur l'image d'entree pour detecter des motifs locaux (contours, textures, formes). Chaque filtre produit une carte d'activation (feature map) qui met en evidence la presence d'un motif specifique. L'empilement de couches convolutives permet d'apprendre des caracteristiques de plus en plus abstraites et complexes.

**Couches de pooling** :
Le pooling (sous-echantillonnage) reduit la dimension spatiale des cartes d'activation, ce qui diminue le nombre de parametres et la complexite computationnelle, tout en introduisant une invariance partielle aux translations. Le Max Pooling, utilise dans nos architectures, conserve la valeur maximale dans chaque region.

**Couches entierement connectees (Dense)** :
Apres les couches convolutives et de pooling, les cartes d'activation sont aplaties (Flatten) et passees a des couches entierement connectees qui effectuent la classification finale. La derniere couche utilise une activation softmax pour produire des probabilites de classe.

**Batch Normalization** :
La normalisation par lot stabilise et accelere l'entrainement en normalisant les sorties de chaque couche. Elle reduit le probleme du decalage interne des covariables (internal covariate shift) et permet l'utilisation de taux d'apprentissage plus eleves.

**Architecture CNN pour la detection de chutes** :

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, BatchNormalization

fall_detection = Sequential([
    Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(96, 96, 3)),
    BatchNormalization(),
    MaxPooling2D(pool_size=(2, 2)),

    Conv2D(32, kernel_size=(3, 3), activation='relu'),
    BatchNormalization(),
    MaxPooling2D(pool_size=(2, 2)),

    Conv2D(64, kernel_size=(3, 3), activation='relu'),
    BatchNormalization(),
    MaxPooling2D(pool_size=(2, 2)),

    Flatten(),
    Dense(64, activation='relu'),
    Dense(2, activation='softmax')
])

fall_detection.compile(optimizer='adam',
                       loss='categorical_crossentropy',
                       metrics=['accuracy'])
```

Cette architecture a trois couches convolutives avec des filtres de taille 3x3, suivies de Batch Normalization et Max Pooling, puis de couches denses pour la classification binaire (chute / non-chute). Le modele prend en entree des images de 96x96 pixels en couleur (3 canaux RGB) issues du dataset CAUCA. L'optimiseur Adam combine les avantages de l'optimisation par momentum et par taux adaptatif, et la perte est la cross-entropie categorielle, adaptee aux problemes de classification multi-classe.

Le modele a atteint une precision de plus de 97% sur les donnees de test pour la detection de chutes.

<h3 class="section-title">6. Optimisation de reseaux de neurones pour l'edge</h3>

Le deploiement de modeles de Deep Learning sur des dispositifs embarques (microcontroleurs, capteurs IoT) necessite des techniques d'optimisation pour reduire la taille du modele, le temps d'inference et la consommation energetique, tout en preservant la precision.

**Elagage (Pruning)** :
L'elagage consiste a supprimer les connexions (poids) les moins significatives du reseau de neurones. Les poids proches de zero contribuent peu a la sortie du modele et peuvent etre mis a zero sans degradation significative de la precision. Cela reduit le nombre de parametres effectifs et peut accelerer l'inference.

Dans le TP, nous avons utilise le TensorFlow Model Optimization Toolkit pour appliquer un elagage a sparsity constante :

```python
import tensorflow_model_optimization as tfmot

# Application de l'elagage avec un niveau de sparsity donne
pruning_params = {
    'pruning_schedule': tfmot.sparsity.keras.ConstantSparsity(
        target_sparsity=0.1, begin_step=0
    )
}

pruned_model = tfmot.sparsity.keras.prune_low_magnitude(
    base_model, **pruning_params
)

pruned_model.compile(optimizer='adam',
                     loss='categorical_crossentropy',
                     metrics=['accuracy'])
```

Les resultats experimentaux ont montre que meme avec un niveau de sparsity de 10% (10% des poids mis a zero), le modele elague conservait une precision de 99.76% sur la validation, demontrant que de nombreux poids du reseau sont effectivement redondants.

| Sparsity | Precision train | Precision validation | Taille modele |
|----------|----------------|---------------------|---------------|
| 0.0 (base) | 97.22% | 96.98% | Reference |
| 0.1 | 99.48% | 99.76% | ~1.63 Mo |
| 0.3 | 99.94% | 99.44% | ~1.63 Mo |
| 0.9 | 99.86% | 99.29% | ~1.63 Mo |

**Quantification** :
La quantification reduit la precision numerique des poids et des activations du modele, typiquement de flottants 32 bits (FP32) a des entiers 8 bits (INT8). Cela reduit la taille du modele d'un facteur ~4 et peut accelerer significativement l'inference sur les microcontroleurs qui disposent d'unites de calcul entier optimisees.

La quantification peut etre :
- **Post-training** : appliquee apres l'entrainement, sans re-entrainement
- **Quantization-aware training (QAT)** : integree pendant l'entrainement pour minimiser la perte de precision

**Distillation de connaissances (Knowledge Distillation)** :
La distillation de connaissances est une technique ou un modele compact (eleve) est entraine a reproduire les sorties d'un modele plus grand et plus performant (professeur). Le modele eleve apprend non seulement les etiquettes dures, mais aussi les distributions de probabilites "douces" (soft labels) du professeur, qui contiennent des informations sur les relations entre les classes. Cette approche permet de transferer les connaissances d'un modele complexe vers un modele deployable sur un dispositif embarque.

<h3 class="section-title">7. Concepts TinyML et TensorFlow Lite pour microcontroleurs</h3>

**TinyML** :
Le TinyML designe le champ de recherche et d'application qui vise a deployer des modeles de Machine Learning sur des microcontroleurs ultra-basse-consommation (quelques milliwatts). Les contraintes typiques incluent :
- Memoire RAM limitee (quelques centaines de Ko)
- Memoire Flash limitee (quelques Mo)
- Pas d'OS complet, pas de GPU
- Alimentation par batterie ou energy harvesting
- Inference en temps reel requise

**TensorFlow Lite (TFLite)** :
TensorFlow Lite est le framework de Google pour le deploiement de modeles de Machine Learning sur des dispositifs mobiles et embarques. Dans le TP2, nous avons converti notre modele CNN elague en format TFLite avec quantification :

```python
import tensorflow as tf

# Conversion du modele elague en TensorFlow Lite avec quantification
converter = tf.lite.TFLiteConverter.from_keras_model(pruned_model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()

# Sauvegarde du modele TFLite
with open('fall_detection.tflite', 'wb') as f:
    f.write(tflite_model)
```

La combinaison elagage + quantification a permis de reduire significativement la taille du modele tout en maintenant une precision acceptable pour le deploiement embarque.

**Inference sur dispositifs contraints** :
L'inference TFLite sur microcontroleur utilise un interpreteur leger qui charge le modele en memoire Flash et effectue les calculs en memoire RAM. Le pipeline typique est :
1. Charger le modele TFLite en memoire
2. Allouer les tenseurs d'entree/sortie
3. Preparer les donnees d'entree (preprocessing)
4. Executer l'inference
5. Lire les resultats de sortie

```python
# Evaluation du modele TFLite
interpreter = tf.lite.Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

for i in range(len(X_test)):
    interpreter.set_tensor(input_details[0]['index'], X_test[i:i+1])
    interpreter.invoke()
    prediction = interpreter.get_tensor(output_details[0]['index'])
```

<h3 class="section-title">8. Techniques de compression de modeles</h3>

La compression de modeles regroupe l'ensemble des techniques visant a reduire la taille et la complexite computationnelle des modeles d'IA pour les rendre deployables sur des plateformes embarquees. Le TP2 a illustre le pipeline complet de compression :

**Pipeline de compression applique** :
1. **Entrainement du modele de base** : CNN complet entraine sur le dataset CAUCA
2. **Elagage** : suppression des poids les moins significatifs (sparsity optimale : 10%)
3. **Re-entrainement** : fine-tuning du modele elague pour recuperer la precision perdue
4. **Quantification** : reduction de la precision numerique (FP32 vers INT8) via TFLite
5. **Evaluation finale** : verification de la precision et de la taille sur le jeu de test

**Resultats de la compression** :
La comparaison entre le modele original et le modele compresse (elague + quantifie) a montre qu'il est possible de reduire considerablement la taille du modele tout en conservant une precision elevee, rendant le deploiement sur microcontroleur viable.

<h3 class="section-title">9. Travaux pratiques avec le ML embarque</h3>

**TP1 - Reconnaissance d'activites humaines (HAR)** :
Le premier TP portait sur la classification de 8 activites humaines a partir de donnees de capteurs (accelerometre, gyroscope, magnetometre, temperature) places sur la main, le torse et la cheville. Les donnees comprenaient 13 477 exemples echantillonnes a 100 Hz avec des fenetres de 5 secondes (500 pas temporels, 6 capteurs).

Le TP se decomposait en trois parties :
- **Partie I** : Implementation du DTW et systeme de reconnaissance par k-NN
- **Partie II** : Reduction de dimension par PCA et classification par MLP
- **Partie III** : (Bonus) Reduction par k-medoids pour DTW + k-NN

La comparaison des deux approches a clairement demontre la superiorite du MLP apres PCA (98% de precision) par rapport au k-NN+DTW (60%), tant en termes de precision que de temps d'execution. Cette experience a illustre l'importance du choix de la methode en fonction des contraintes du systeme cible.

**TP2 - Detection de chutes par CNN et deploiement embarque** :
Le second TP etait centre sur un cas d'usage concret de l'IoT : la detection de chutes pour les personnes agees, un enjeu de sante publique majeur. Le TP utilisait le dataset CAUCA contenant des images de 96x96 pixels en couleur representant des situations de chute et de non-chute.

Le TP se decomposait en trois parties :
- **Partie 1** : Classification par CNN (conception de l'architecture, entrainement, evaluation)
- **Partie 2** : Compression du CNN par combinaison d'elagage et de quantification
- **Partie 3** : (Optionnel) Conception d'un systeme de detection de chutes en production pour maisons de retraite

Ce TP illustrait le pipeline complet de l'IA embarquee : de la conception du modele a son deploiement optimise, en passant par la compression, ce qui est exactement le workflow utilise dans l'industrie pour deployer des modeles sur des dispositifs IoT.

---

## PART D - Analyse et Reflexion

<h3 class="section-title">Competences acquises</h3>

**Competences techniques** :
- Comprehension des fondamentaux de l'IA et du Machine Learning appliques a l'IoT
- Conception et entrainement de reseaux de neurones (MLP, CNN)
- Maitrise des techniques de preprocessing : normalisation, lissage, PCA
- Implementation d'algorithmes d'analyse de series temporelles (DTW)
- Application de techniques d'elagage (pruning) pour optimiser les modeles
- Conversion de modeles vers TensorFlow Lite pour le deploiement embarque
- Evaluation et comparaison de methodes de classification
- Comprehension des compromis precision/taille/vitesse pour les systemes contraints

**Competences transversales** :
- Programmation scientifique en Python (NumPy, scikit-learn, TensorFlow)
- Analyse de donnees et interpretation de resultats experimentaux
- Methodologie experimentale : entrainement, validation, test
- Travail en binome et documentation de code

<h3 class="section-title">Auto-evaluation</h3>

Ce cours m'a permis de mieux comprendre le deploiement de l'IA et son fonctionnement, depuis les algorithmes fondamentaux jusqu'aux techniques d'optimisation pour l'embarque. Les travaux pratiques etaient assez longs, et je n'ai pas toujours eu le temps de terminer tous les exercices. De plus, n'ayant pas code en Python depuis un moment, j'ai du me remettre a niveau sur certaines bases.

C'etait une experience pratique nouvelle pour moi car je n'avais pas beaucoup travaille avec les bibliotheques de Machine Learning auparavant. J'ai pu coder les differents concepts et meme les reutiliser dans le projet innovant. Cependant, j'ai rencontre quelques difficultes de comprehension, l'IA embarquee etant un domaine relativement nouveau pour moi. Grace a mon interet pour le sujet, je sais qu'il me faut simplement plus de temps pour m'investir dans les differents aspects.

| Competence | Niveau avant | Niveau apres | Progression |
|------------|-------------|-------------|-------------|
| Machine Learning fondamental | Notions de base (S8) | Bonne comprehension | Significative |
| Deep Learning / CNN | Tres faible | Bonne maitrise pratique | Tres importante |
| Preprocessing et PCA | Faible | Bonne comprehension | Importante |
| Optimisation de modeles (pruning, quantification) | Aucune | Correcte | Importante |
| TensorFlow / Keras | Faible | Bonne utilisation | Significative |
| TFLite et deploiement embarque | Aucune | Notions correctes | Importante |
| Series temporelles / DTW | Aucune | Bonne comprehension | Tres importante |

<h3 class="section-title">Applications et perspectives</h3>

J'ai appris de nombreux concepts cles dans les deploiements actuels de l'IA. Bien que je sois tres interesse par ce domaine, je ne suis pas certain de travailler directement dans cette specialite plus tard, car ce n'est pas mon domaine principal. Cependant, j'aurai des competences de base solides pour comprendre l'IA et ses applications dans l'IoT.

A l'avenir, j'espere rencontrer l'IA dans ma carriere professionnelle car c'est un domaine actuel et en pleine evolution. Je suis desireux d'en decouvrir davantage, possiblement a travers des projets personnels. Cela me permettra d'approfondir ma comprehension et de rester a jour avec les dernieres avancees en IA et IoT.

**Applications directes** :
- Deploiement de modeles d'IA sur des microcontroleurs pour des applications IoT
- Detection d'activites et d'evenements a partir de donnees capteurs en temps reel
- Optimisation de modeles existants pour des plateformes a ressources limitees
- Conception de systemes de surveillance intelligents (detection de chutes, activites)

**Lien avec les autres cours du cursus** :
- **Machine Learning (S8)** : fondamentaux theoriques reutilises et approfondis
- **Cloud & Edge Computing** : architectures edge pour l'inference IA en peripherie
- **Energy for Connected Objects** : contraintes energetiques du deploiement IA sur batterie
- **Wireless Sensor Networks** : capteurs generant les donnees pour les modeles embarques
- **Projet Innovant** : reutilisation des concepts d'IA embarquee dans un projet concret

---

## Documents de Cours

<h3 class="section-title">Supports de cours</h3>

<div class="pdf-container">
     <iframe src="/cours-pdf/S9/Embedded-IA/1-Intro.pdf" width="100%" height="600px" style="overflow: auto;" frameborder="0"></iframe>
</div>
<p style="text-align: center;">
     <a href="/cours-pdf/S9/Embedded-IA/1-Intro.pdf" target="_blank">1 - Introduction au Machine Learning pour l'IoT</a>
</p>

<div class="pdf-container">
     <iframe src="/cours-pdf/S9/Embedded-IA/2-Data_Preprocessing.pdf" width="100%" height="600px" style="overflow: auto;" frameborder="0"></iframe>
</div>
<p style="text-align: center;">
     <a href="/cours-pdf/S9/Embedded-IA/2-Data_Preprocessing.pdf" target="_blank">2 - Preprocessing des donnees</a>
</p>

<div class="pdf-container">
     <iframe src="/cours-pdf/S9/Embedded-IA/3-Time_Series.pdf" width="100%" height="600px" style="overflow: auto;" frameborder="0"></iframe>
</div>
<p style="text-align: center;">
     <a href="/cours-pdf/S9/Embedded-IA/3-Time_Series.pdf" target="_blank">3 - Analyse de series temporelles</a>
</p>

<div class="pdf-container">
     <iframe src="/cours-pdf/S9/Embedded-IA/4-CNN.pdf" width="100%" height="600px" style="overflow: auto;" frameborder="0"></iframe>
</div>
<p style="text-align: center;">
     <a href="/cours-pdf/S9/Embedded-IA/4-CNN.pdf" target="_blank">4 - Reseaux de Neurones Convolutifs (CNN)</a>
</p>

<div class="pdf-container">
     <iframe src="/cours-pdf/S9/Embedded-IA/5NNoptimization.pdf" width="100%" height="600px" style="overflow: auto;" frameborder="0"></iframe>
</div>
<p style="text-align: center;">
     <a href="/cours-pdf/S9/Embedded-IA/5NNoptimization.pdf" target="_blank">5 - Optimisation de reseaux de neurones</a>
</p>

---

*Cours suivi en 2024-2025 a l'INSA Toulouse, Departement Genie Electrique et Informatique, Specialite ISS (Innovative Smart Systems).*

<div class="back-nav">
    <a href="./my-courses-2024-2025.html">&larr; Retour aux Cours 2024-2025</a>
</div>

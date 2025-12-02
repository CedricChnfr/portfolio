---
layout: default
title:  "Embedded AI for IoT"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---



[← Back to My Courses 2024-2025](./my-courses-2024-2025.html)

**🔗 Cours connexes**: 
- [Machine Learning - S8](../2023-2024/2024-10-03-machine-learning-s8.html) - Fondamentaux du Machine Learning
- [Cloud & Edge Computing - S9](./2024-10-03-cloud-edge.html) - Architectures Edge pour l'IA
- [Energy for Connected Objects - S9](./2024-10-03-energy-connected-object.html) - Optimisation énergétique

---

# Embedded IA for IoT

## PART A: GENERALITIES

### Presentation
The "Embedded IA for IoT" course, taught by Philippe Leleux, was an interesting experience that on the integration of artificial intelligence nowadays. The primary focus was on understanding and implementing AI models on embedded devices with limited computational resources. This course was particularly relevant given the growing importance of AI in enhancing the functionality of IoT systems.

## PART B: DESCRIPTIVE PART

### Experience Details

#### Environment and Context
During this course, I explored both theoretical and practical aspects of embedding AI in IoT devices. The hands-on sessions were beneficial, allowing me to apply the concepts learned in class to real-world scenarios. The challenge of optimizing AI models to run efficiently on resource-constrained devices was both demanding and rewarding.

#### My Function
In this course, I was responsible for:
- Understanding the principles of AI and its application in IoT.
- Implementing and optimizing AI models for embedded devices.
- Conducting experiments to test the efficiency and accuracy of these models.

## PART C: TECHNICAL PART

This section explores the technical aspects of the course, focusing on the problem analysis, solution design, and implementation of AI for an IoT application.

### Technical Concepts Learned

### 1. Dynamic Time Warping (DTW)
Dynamic Time Warping (DTW) is an algorithm used to measure the similarity between two temporal sequences that may vary in speed. It is particularly useful in time series analysis where the sequences may be out of phase. In the lab, we implemented DTW to align sequences of sensor data for human activity recognition. By calculating the optimal alignment between sequences, DTW helps in identifying similar patterns despite temporal distortions.
```python
# Define the DTW algorithm
def dtw(a, b, distance, w=(1, 1, 1), gamma=5):
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
```python
# Example 1: Numerical sequences
a1 = (4, 6, 1)
b1 = (5, 1)

# Calculate the DTW score using the absolute difference as the distance metric
result1 = dtw(a1, b1, lambda x, y: abs(x - y), w=(1, 1, 1), gamma=2)
print(f"DTW score for example 1: {result1}")
```
In example 1, the DTW algorithm calculates the similarity between two numerical sequences (4, 6, 1) and (5, 1). The resulting score S=0.4 indicates the average cost of aligning the sequences, considering the absolute difference as the local distance metric, with local constraints (1, 1, 1) and a global constraint of 2.

```python
# Example 2: Character sequences
a2 = ('A', 'T', 'G', 'G', 'T', 'A', 'C', 'G', 'T', 'C')
b2 = ('A', 'A', 'G', 'T', 'A', 'G', 'G', 'C')

# Define a custom distance function for characters
def char_distance(x, y):
    return 0 if x == y else 1

# Calculate the DTW score using the custom character distance function
result2 = dtw(a2, b2, char_distance, w=(1, 1, 1), gamma=4)
print(f"DTW score for example 2: {result2}")
```
In example 2, the DTW algorithm calculates the similarity between two character sequences "ATGGTACGTC" and "AAGTAGGC". The resulting score S=1/6 indicates the average cost of aligning the sequences, using a custom distance function where the distance is 0 if the characters are equal and 1 otherwise. The algorithm uses local constraints (1, 1, 1) and a global constraint of 4 to determine the optimal alignment.

### 2. Principal Component Analysis (PCA)
Principal Component Analysis (PCA) is a dimensionality reduction technique that transforms high-dimensional data into a lower-dimensional form while preserving as much variance as possible. In the lab, we used PCA to reduce the number of features in our sensor data before applying machine learning algorithms. By retaining only the most significant components, PCA helps in simplifying the model, reducing computational cost, and mitigating the curse of dimensionality.

```python
from sklearn.decomposition import PCA

# Apply PCA to reduce dimensionality
pca = PCA(n_components=n_components)
pca.fit(X_train)

# Transform the training and test data
X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)

print(f"Training set size after PCA: {X_train_pca.shape}")
print(f"Test set size after PCA: {X_test_pca.shape}")
```

The code above demonstrates using Principal Component Analysis (PCA) to reduce the dimensionality of datasets. By specifying `n_components`, PCA transforms high-dimensional data into a lower-dimensional form, retaining significant features. The `fit` method computes principal components from the training data, and `transform` applies this to both training and test datasets. The resulting shapes of `X_train_pca` and `X_test_pca` indicate reduced dimensions, simplifying the model and reducing computational cost.


### 3. k-Nearest Neighbors (k-NN)
k-Nearest Neighbors (k-NN) is a straightforward, non-parametric classification algorithm that assigns a class to a sample based on the majority class of its k nearest neighbors. During the lab sessions, we combined k-NN with DTW to classify human activities from sensor data. By leveraging the distance metric provided by DTW, k-NN effectively identified the most similar activity patterns.

```python
from sklearn.neighbors import KNeighborsClassifier

# Train k-NN classifier
knn = KNeighborsClassifier(n_neighbors=5, metric=dtw)
knn.fit(X_train, y_train)
```

The code snippet above demonstrates training a k-Nearest Neighbors (k-NN) classifier using the `KNeighborsClassifier` class from scikit-learn. By specifying the number of neighbors `n_neighbors` and the distance metric `metric`, we can customize the k-NN algorithm. In this case, we use the DTW function as the distance metric to calculate the similarity between samples. The `fit` method trains the k-NN model on the training data, enabling it to classify new samples based on their nearest neighbors.

```python
# Create and train the k-NN model
k_values = range(1, 11)
scores = []

for k in k_values:
    clf = KNeighborsClassifier(n_neighbors=k)
    clf.fit(X_train, y_train)
    score = clf.score(X_test, y_test)
    scores.append(score)
    print(f"k={k}, Score={score}")
```

### 4. Multi-Layer Perceptron (MLP)
Multi-Layer Perceptron (MLP) is a type of artificial neural network consisting of multiple layers of neurons, including input, hidden, and output layers. In the lab, we used MLP for classification tasks after reducing the dimensionality of our data with PCA. MLPs are capable of learning complex, non-linear relationships in data through backpropagation and gradient descent. This makes them powerful tools for tasks such as image recognition, natural language processing, and predictive analytics.

```python
from sklearn.neural_network import MLPClassifier

# Train MLP classifier
mlp = MLPClassifier(hidden_layer_sizes=(100,), max_iter=300, solver='adam', random_state=1)
mlp.fit(X_pca, y_train)
```

### 5. Convolutional Neural Networks (CNN)
Convolutional Neural Networks (CNNs) are deep learning models designed for image data. They use convolutional layers to detect patterns and features in images. In the lab, we used CNNs to create a model for fall detection. CNNs are effective for tasks like image recognition and object detection because they can automatically learn important features from raw data.

```python
# Define the CNN architecture
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 1)),
    MaxPooling2D((2, 2)),
    BatchNormalization(),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    BatchNormalization(),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)
```

The code above defines and trains a Convolutional Neural Network (CNN) using TensorFlow's Keras API. The model includes convolutional layers, max-pooling, batch normalization, and fully connected layers. It is compiled with the Adam optimizer and categorical cross-entropy loss, and trained with a validation split. This architecture is effective for image classification tasks, learning spatial patterns in the data.


## PART D: ANALYTICAL PART

### The Knowledge and Skills Mobilized
- Understanding the fundamentals of AI and Machine Learning.
- Designing and training Neural Networks.
- Applying pruning techniques to optimize AI models.
- Converting AI models to TensorFlow Lite for deployment on embedded devices.
- Implementing AI solutions for IoT applications.

### Self Evaluation
I understood better AI deployment and how it works. However, the labs were a bit long, and I didn't have the time to finish everything. Also I didn't code in Python for a long time, so I had to relearn some basics.

It was a new practical experience for me as I hadn't worked much with machine learning libraries before. I was able to code for the different concepts and even reuse them in the innovative project. However, I faced a few difficulties for understanding concepts as it is a recent area for me. But thanks to my interest in the subject, I know that I just need more time to involve myself in the different aspects.

### My Opinion
I learned a lot of new concepts that are key in today's deployments. Even though I am very interested in this field, I am unsure if I will work in this area later as it is not my specialty. However, I will have some basic skills to understand AI.

In the future, I hope to encounter AI in my professional career as it is a current and evolving area. I am eager to discover more about this subject, possibly through personal projects. This will allow me to deepen my understanding and stay updated with the latest advancements in AI and IoT.


<div style="text-align: center;">
    <h1>Project Report</h1>
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
    p {
    text-align: justify;
    }
</style>
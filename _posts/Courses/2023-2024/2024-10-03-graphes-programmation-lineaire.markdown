---
layout: default
title: "Graphes et Programmation Linéaire - S8"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
---

[← Back to My Courses 2023-2024](./my-courses-2023-2024.html)

# Graphes et Programmation Linéaire

## PART A: GENERALITIES

### Presentation
Le cours "Graphes et Programmation Linéaire" couvre deux domaines complémentaires de la recherche opérationnelle: la théorie des graphes pour modéliser des réseaux et relations, et la programmation linéaire pour optimiser des systèmes sous contraintes. Ces outils mathématiques sont essentiels pour résoudre des problèmes complexes d'optimisation dans l'industrie, la logistique, et les réseaux.

**Année Académique**: 2023-2024  
**Semestre**: 8  
**Catégorie**: Mathématiques Appliquées / Recherche Opérationnelle

---

## PART B: DESCRIPTIVE PART

### Experience Details

#### Environment and Context
Le cours combinait théorie mathématique rigoureuse et applications pratiques via des logiciels d'optimisation. Nous avons étudié des algorithmes classiques (Dijkstra, Ford-Fulkerson, Simplexe) et les avons appliqués à des problèmes réels: routage, planification, allocation de ressources, ordonnancement.

#### My Function
Dans ce cours, j'ai été responsable de:
- Modéliser des problèmes réels en graphes ou programmes linéaires
- Appliquer des algorithmes de recherche de chemins, flots, et arbres couvrants
- Formuler et résoudre des problèmes d'optimisation linéaire
- Utiliser des solveurs (Python, CPLEX, GLPK)
- Interpréter les solutions et analyses de sensibilité
- Résoudre des problèmes de transport, affectation, et ordonnancement

## PART C: TECHNICAL PART

Cette section explore les aspects techniques des graphes et de la programmation linéaire.

### Technical Concepts Learned

#### 1. Théorie des Graphes - Définitions

**Graphe G = (V, E)**:
- V: ensemble de sommets (vertices)
- E: ensemble d'arêtes (edges) ou arcs

**Types**:
- **Graphe orienté**: arcs avec direction
- **Graphe non orienté**: arêtes sans direction
- **Graphe pondéré**: poids sur arêtes/arcs
- **Graphe simple**: pas de boucle ni arête multiple

**Degré**:
- Degré d'un sommet: nombre d'arêtes incidentes
- Degré entrant/sortant (graphe orienté)

**Chemin**: séquence de sommets reliés par arêtes
**Cycle**: chemin fermé (revient au point de départ)
**Connexité**: tous sommets accessibles depuis tout autre

#### 2. Algorithmes de Plus Court Chemin

**Algorithme de Dijkstra**:
Trouve plus court chemin d'une source vers tous autres sommets.

**Complexité**: O((V+E)log V) avec tas

**Limitation**: poids positifs uniquement

**Algorithme de Bellman-Ford**:
Gère poids négatifs, détecte cycles négatifs.

**Complexité**: O(VE)

**Algorithme de Floyd-Warshall**:
Plus courts chemins entre toutes paires de sommets.

**Complexité**: O(V³)

**Applications**:
- GPS et navigation
- Routage réseau
- Planification de trajets
- Jeux vidéo (IA)

#### 3. Arbres Couvrants

**Arbre**: graphe connexe acyclique
**Arbre couvrant**: arbre incluant tous les sommets

**Arbre Couvrant de Poids Minimum (MST)**:

**Algorithme de Kruskal**:
- Trier arêtes par poids croissant
- Ajouter arête si ne crée pas cycle
- Utilise union-find pour détecter cycles

**Algorithme de Prim**:
- Partir d'un sommet
- Ajouter arête de poids min reliant arbre à sommet extérieur
- Répéter jusqu'à tous sommets inclus

**Applications**:
- Conception de réseaux (électrique, eau, télécoms) à coût minimum
- Clustering

#### 4. Flots dans les Réseaux

**Réseau de flot**:
Graphe orienté avec capacités sur arcs.

**Problème du flot maximum**:
Maximiser flot de la source s vers puits t.

**Contraintes**:
- Flot ≤ capacité sur chaque arc
- Conservation du flot (entrant = sortant sauf s et t)

**Algorithme de Ford-Fulkerson**:
- Trouver chemin augmentant (capacité résiduelle > 0)
- Augmenter flot le long de ce chemin
- Répéter jusqu'à plus de chemin augmentant

**Théorème flot-max = coupe-min**:
Valeur du flot maximal = capacité de la coupe minimale.

**Algorithme d'Edm onds-Karp**:
Ford-Fulkerson avec BFS pour trouver chemin augmentant.

**Complexité**: O(VE²)

**Applications**:
- Réseaux de transport (trafic routier, fluides)
- Réseaux de communication (bande passante)
- Appariement biparti

#### 5. Problème d'Affectation

**Problème**:
Affecter n tâches à n agents, minimiser coût total.

**Matrice de coûts C**:
Cᵢⱼ = coût d'affecter tâche j à agent i

**Formulation**:
```
Minimiser Σ Σ Cᵢⱼ × xᵢⱼ

Contraintes:
Σⱼ xᵢⱼ = 1  (chaque agent 1 tâche)
Σᵢ xᵢⱼ = 1  (chaque tâche 1 agent)
xᵢⱼ ∈ {0,1}
```

**Algorithme hongrois**:
Résout en O(n³).

**Applications**:
- Affectation personnel/postes
- Planification production
- Appariement (dating apps!)

#### 6. Coloration de Graphes

**Problème**:
Attribuer couleur à chaque sommet tel que sommets adjacents ont couleurs différentes.

**Nombre chromatique χ(G)**:
Nombre minimum de couleurs nécessaires.

**Théorème des 4 couleurs**:
Tout graphe planaire χ ≤ 4.

**Algorithmes**:
- Glouton (pas optimal mais rapide)
- Recherche exhaustive (exponentiel)

**Applications**:
- Allocation fréquences radio
- Ordonnancement (conflits de ressources)
- Allocation registres (compilateurs)

#### 7. Programmation Linéaire - Formulation

**Forme standard**:
```
Maximiser (ou Minimiser) Z = c₁x₁ + c₂x₂ + ... + cₙxₙ

Sous contraintes:
a₁₁x₁ + a₁₂x₂ + ... + a₁ₙxₙ ≤ b₁
a₂₁x₁ + a₂₂x₂ + ... + a₂ₙxₙ ≤ b₂
...
aₘ₁x₁ + aₘ₂x₂ + ... + aₘₙxₙ ≤ bₘ

x₁, x₂, ..., xₙ ≥ 0
```

**Forme matricielle**:
```
Max c^T x
s.t. Ax ≤ b, x ≥ 0
```

**Région admissible**:
Polyèdre convexe défini par contraintes.

**Théorème fondamental**:
Si solution optimale existe, elle se trouve à un sommet du polyèdre.

#### 8. Algorithme du Simplexe

**Principe**:
Parcours itératif des sommets du polyèdre vers l'optimum.

**Étapes**:
1. Partir d'un sommet admissible (solution de base)
2. Tester directions améliorantes
3. Se déplacer vers sommet adjacent améliorant Z
4. Répéter jusqu'à optimum (aucune direction n'améliore)

**Tableau du simplexe**:
Forme tableau pour calculs itératifs.

**Variables d'écart**:
Transformer inégalités en égalités.

**Complexité**:
Exponentielle au pire cas, mais polynomial en pratique.

#### 9. Dualité

**Problème Primal**:
```
Max c^T x
s.t. Ax ≤ b, x ≥ 0
```

**Problème Dual**:
```
Min b^T y
s.t. A^T y ≥ c, y ≥ 0
```

**Théorème de dualité forte**:
Si primal a solution optimale x*, dual a solution optimale y* et:
```
c^T x* = b^T y*
```

**Interprétation économique**:
- Primal: production optimale
- Dual: valorisation des ressources (prix d'ombre)

**Écarts complémentaires**:
```
Si xⱼ > 0 alors contrainte duale j saturée
Si yᵢ > 0 alors contrainte primale i saturée
```

#### 10. Analyse de Sensibilité

**Questions**:
- Comment l'optimum varie si on change un paramètre (coût, ressource)?
- Plage de validité de la solution actuelle?

**Prix d'ombre (shadow price)**:
Variation de Z si on augmente ressource bᵢ d'une unité.
= variable duale yᵢ*

**Coût réduit**:
Pour variable hors base: combien cⱼ doit diminuer pour entrer en base.

**Plages de variation**:
- Coefficients objectif cⱼ
- Seconds membres bᵢ

Dans ces plages, solution optimale (base) reste identique.

#### 11. Problème de Transport

**Contexte**:
m sources (offres sᵢ), n destinations (demandes dⱼ).
Coût cᵢⱼ pour transporter de i vers j.

**Formulation**:
```
Min Σᵢ Σⱼ cᵢⱼ × xᵢⱼ

s.t.
Σⱼ xᵢⱼ = sᵢ  (offre source i)
Σᵢ xᵢⱼ = dⱼ  (demande destination j)
xᵢⱼ ≥ 0
```

**Condition d'existence**:
Σ sᵢ = Σ dⱼ (offre totale = demande totale)

**Méthode de résolution**:
- Méthode du coin nord-ouest (solution initiale)
- Stepping-stone ou MODI pour optimiser

**Applications**:
- Logistique et distribution
- Planification production multi-sites

#### 12. Programmation Linéaire en Nombres Entiers

**PLNE (Programmation Linéaire en Nombres Entiers)**:
```
Max c^T x
s.t. Ax ≤ b, x ≥ 0, x ∈ ℤⁿ
```

**Difficulté**:
NP-difficile (pas de méthode polynomiale connue).

**Méthodes de résolution**:

**Branch and Bound**:
- Résoudre relaxation continue (ignorer contrainte entière)
- Brancher sur variable fractionnaire
- Explorer arbre de décision
- Borner avec solutions entières trouvées

**Coupes (Cutting Planes)**:
Ajouter contraintes linéaires éliminant solutions fractionnaires sans enlever solutions entières.

**Méthodes heuristiques**:
Trouver bonnes solutions (pas nécessairement optimales) rapidement.

**Programmation 0-1**:
Variables binaires (décisions oui/non).

**Applications**:
- Planification
- Ordonnancement
- Localisation d'installations
- Sac à dos (knapsack)
- Tournées de véhicules

## PART D: ANALYTICAL PART

### Knowledge and Skills Mobilized

- Modélisation de problèmes réels en graphes ou programmes linéaires
- Compréhension et application d'algorithmes classiques
- Formulation mathématique de problèmes d'optimisation
- Utilisation de solveurs (Python, logiciels dédiés)
- Interprétation de solutions et analyse de sensibilité
- Évaluation de complexité algorithmique
- Résolution de problèmes de transport, affectation, et ordonnancement
- Esprit critique sur pertinence des modèles et limites

### Self Evaluation

Ce cours a été mathématiquement exigeant mais très enrichissant. La théorie des graphes offre un langage puissant pour modéliser de nombreux systèmes: réseaux, relations, dépendances.

Les algorithmes classiques (Dijkstra, Kruskal, Ford-Fulkerson) sont élégants et ont fait leurs preuves. Les comprendre en profondeur (pas juste les appliquer mécaniquement) aide à adapter ou concevoir de nouveaux algorithmes.

La programmation linéaire est un outil d'optimisation extrêmement puissant. La capacité à formuler un problème complexe en système d'équations linéaires est une compétence précieuse. Le simplexe, bien que conceptuellement simple (parcours de sommets), demande rigueur dans les calculs.

L'analyse de sensibilité et la dualité sont des concepts profonds. Comprendre que chaque problème d'optimisation a un dual avec interprétation économique (prix d'ombre) est fascinant.

La programmation en nombres entiers complexifie drastiquement les problèmes. La frontière entre polynomial (PL continue) et NP-difficile (PLNE) est impressionnante. Cela souligne l'importance des heuristiques et approximations en pratique.

Les applications sont omniprésentes: logistique, télécoms, production, transport, finance. Savoir reconnaître qu'un problème industriel peut se modéliser en graphe ou PL est une compétence transversale.

L'utilisation de solveurs modernes (comme CPLEX, Gurobi, ou bibliothèques Python) démocratise l'optimisation. Mais comprendre la théorie sous-jacente reste essentiel pour formuler correctement, interpréter résultats, et diagnostiquer problèmes.

### My Opinion

Ce cours est fondamental pour tout ingénieur confronté à des problèmes d'optimisation, de planification, ou de gestion de réseaux.

Points forts:
- Équilibre théorie/pratique
- Algorithmes classiques bien expliqués
- Applications variées et concrètes
- Utilisation d'outils logiciels modernes

Points à améliorer:
- Plus de temps sur PLNE et heuristiques
- Cas d'études industriels de grande échelle
- Programmation non-linéaire (extension naturelle)
- Optimisation multi-objectifs

Réflexions personnelles:

L'optimisation est au cœur de nombreux défis industriels: comment produire plus avec moins de ressources, livrer plus vite à moindre coût, utiliser au mieux l'énergie, etc. Les outils mathématiques de ce cours permettent d'aborder ces questions de manière rigoureuse.

La modélisation est souvent la partie la plus difficile. Transformer un problème réel confus en modèle mathématique propre demande abstraction et simplification intelligente. Un modèle trop simple perd en pertinence; trop complexe devient insoluble.

Le fossé entre problèmes polynomiaux et NP-difficiles rappelle les limites de l'optimisation exacte. Pour problèmes de grande taille ou complexes, les heuristiques et métaheuristiques (algorithmes génétiques, recuit simulé, etc.) sont incontournables, même si elles ne garantissent pas l'optimalité.

La recherche opérationnelle est un domaine vaste et actif. Les problèmes réels incluent souvent incertitudes, dynamique, contraintes non-linéaires. L'optimisation stochastique, robuste, et en ligne sont des extensions importantes.

Applications professionnelles:

Ces compétences sont applicables dans de nombreux secteurs:
- **Logistique**: routage de véhicules, gestion d'entrepôts, supply chain
- **Télécommunications**: routage, allocation de bande passante
- **Énergie**: optimisation de production, smart grids
- **Transport**: gestion de trafic, planification de lignes
- **Production**: ordonnancement, allocation de ressources
- **Finance**: optimisation de portefeuille
- **Santé**: planification d'emplois du temps, allocation de ressources hospitalières

La maîtrise de ces outils, couplée à des compétences en data science et apprentissage automatique, ouvre des perspectives en data-driven optimization: utiliser données massives pour affiner modèles et prédictions, puis optimiser en conséquence.

Maîtriser ces techniques en S8 est essentiel pour tout ingénieur souhaitant concevoir ou améliorer des systèmes efficaces dans un monde toujours plus connecté et complex.

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
      <h4>📖 Annales 2018</h4>
      <p>Sujet d'examen 2018 : algorithmes de graphes (Dijkstra, Bellman-Ford), flots et programmation linéaire.</p>
      <embed src="/cours-pdf/S8/Graphes-Programmation-Lineaire/annales-2018.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S8/Graphes-Programmation-Lineaire/annales-2018.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>📖 Correction Examen 2024</h4>
      <p>Correction complète de l'examen 2024 avec explications détaillées des algorithmes et méthodes de résolution.</p>
      <embed src="/cours-pdf/S8/Graphes-Programmation-Lineaire/correction-exam-2024.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S8/Graphes-Programmation-Lineaire/correction-exam-2024.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>📖 TP Algorithme de Dijkstra</h4>
      <p>Travaux pratiques : implémentation de Dijkstra pour recherche de plus court chemin dans différents graphes.</p>
      <embed src="/cours-pdf/S8/Graphes-Programmation-Lineaire/tp-dijkstra.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S8/Graphes-Programmation-Lineaire/tp-dijkstra.pdf" target="_blank">📥 Télécharger</a></p>
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

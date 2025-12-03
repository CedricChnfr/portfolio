---
layout: default
title: "Réseaux de Pétri - S8"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
---

[← Back to My Courses 2023-2024](./my-courses-2023-2024.html)

# Réseaux de Pétri

## PART A: GENERALITIES

### Presentation
Le cours "Réseaux de Pétri" introduit un formalisme graphique et mathématique puissant pour modéliser, analyser, et valider les systèmes à événements discrets (SED). Les réseaux de Pétri sont particulièrement adaptés pour représenter des systèmes avec concurrence, synchronisation, et partage de ressources. Ils sont utilisés en automatique, informatique, logistique, et de nombreux autres domaines.

**Année Académique**: 2023-2024  
**Semestre**: 8  
**Catégorie**: Automatique / Systèmes à Événements Discrets

---

## PART B: DESCRIPTIVE PART

### Experience Details

#### Environment and Context
Le cours combinait théorie formelle (algèbre, théorie des graphes) avec applications pratiques via des outils logiciels de modélisation et simulation (PIPE, Tina). Nous avons modélisé des systèmes variés: systèmes de production, protocoles de communication, workflows, et analysé leurs propriétés (vivacité, bornitude, absence de blocage).

#### My Function
Dans ce cours, j'ai été responsable de:
- Comprendre la syntaxe et sémantique des réseaux de Pétri
- Modéliser des systèmes concurrents et distribués
- Analyser les propriétés structurelles et comportementales
- Utiliser l'équation d'état et invariants
- Vérifier propriétés (vivacité, bornitude, réversibilité)
- Simuler et valider des modèles
- Appliquer les extensions (temporisés, colorés, stochastiques)
- Utiliser les réseaux de Pétri pour concevoir et valider des systèmes de commande

## PART C: TECHNICAL PART

Cette section explore les aspects techniques des réseaux de Pétri.

### Technical Concepts Learned

#### 1. Définition et Syntaxe

**Réseau de Pétri** R = (P, T, Pre, Post):
- **P**: ensemble de places (états, ressources)
- **T**: ensemble de transitions (événements, actions)
- **Pre**: P×T → ℕ (arcs des places vers transitions, poids)
- **Post**: T×P → ℕ (arcs des transitions vers places, poids)

**Représentation graphique**:
- Places: cercles
- Transitions: rectangles (ou barres)
- Arcs: flèches avec poids (1 si omis)
- Jetons (tokens): points noirs dans places

**Marquage** M: P → ℕ
Fonction indiquant nombre de jetons dans chaque place.
M₀ = marquage initial.

#### 2. Règles de Franchissement

**Transition t est franchissable** (enabled) ssi:
```
∀p ∈ P: M(p) ≥ Pre(p,t)
```

Assez de jetons dans chaque place d'entrée.

**Franchissement** de t:
```
M' = M - Pre(·,t) + Post(t,·)
```

On retire Pre(p,t) jetons de chaque place p, on ajoute Post(t,p).

**Notation**: M →ᵗ M'

**Séquence de franchissement**:
```
M₀ →ᵗ¹ M₁ →ᵗ² M₂ → ... →ᵗⁿ Mₙ
```

#### 3. Graphe de Marquage

**Ensemble d'accessibilité** R(M₀):
Ensemble de tous les marquages atteignables depuis M₀.

**Graphe de marquage**:
- Sommets: marquages
- Arcs: transitions

Représentation de l'espace d'états.

**Problème**: explosion combinatoire (nombre de marquages peut être exponentiel).

#### 4. Propriétés Comportementales

**Bornitude**:
∃ k tel que ∀M ∈ R(M₀), ∀p ∈ P: M(p) ≤ k

Système borné: nombre de jetons limité.
Important: évite débordements (buffers, files).

**1-sûr** (safe): borné par 1.

**Vivacité** (liveness):
Une transition est vivante si elle peut toujours redevenir franchissable.

**Niveaux de vivacité**:
- L0 (mort): jamais franchissable
- L1 (potentiellement franchissable): franchissable au moins une fois
- L2: peut être franchie infiniment sur une séquence
- L3: peut être franchie infiniment souvent (sur toute séquence infinie)
- L4 (vivante): franchissable depuis tout marquage accessible

**Réseau vivant**: toutes transitions L4-vivantes.

**Blocage** (deadlock):
Marquage M où aucune transition n'est franchissable.

**Réversibilité**:
∀M ∈ R(M₀): M₀ ∈ R(M)

On peut toujours revenir à l'état initial.

**Quasi-vivacité**:
∀t ∈ T, ∃M ∈ R(M₀): t franchissable depuis M.

Toute transition peut être franchie au moins une fois.

#### 5. Équation d'État

**Matrice d'incidence** C:
```
C = Post^T - Pre^T
```

C(t,p) = gain net de jetons dans p par franchissement de t.

**Équation d'état fondamentale**:
```
M = M₀ + C^T · σ
```

Où σ est le vecteur de franchissement (nombre de fois chaque transition a été franchie).

**Usage**:
Condition nécessaire (mais pas suffisante) d'accessibilité.
Si M inaccessible, alors pas de solution entière positive à l'équation.

#### 6. Invariants

**P-invariants** (invariants de places):
Vecteur y ≥ 0 tel que:
```
C · y = 0
```

**Interprétation**:
```
y^T · M = y^T · M₀ = constante
```

Combinaison pondérée de jetons conservée.

**Exemple**: conservation de ressources.

**T-invariants** (invariants de transitions):
Vecteur x ≥ 0 tel que:
```
C^T · x = 0
```

**Interprétation**:
Séquence de transitions ramenant au même marquage.
Si x franchissable depuis M, alors M →* M.

**Usage**: cycles, comportements répétitifs.

**Réseau couvert par P-invariants**:
Toute place appartient à au moins un P-invariant.
⇒ Réseau borné.

#### 7. Sous-Classes de Réseaux

**Graphe d'états**:
Chaque transition a exactement une place d'entrée et une de sortie.
Modélise automates finis.

**Graphe d'événements**:
Chaque place a exactement une transition d'entrée et une de sortie.
Modélise synchronisation.

**Réseau libre choix** (free choice):
Si deux transitions partagent place d'entrée, elles ont même ensemble de places d'entrée.
Simplifie analyse.

**Réseau sauf** (safe):
1-borné.

#### 8. Extensions des Réseaux de Pétri

**Réseaux de Pétri Temporisés** (TPN):
Ajout du temps: délais sur transitions ou durées de franchissement.

**Types**:
- **P-temporisé**: jetons ont âge minimal avant utilisation
- **T-temporisé**: transition franchit après délai

**Analyse**: plus complexe (espace d'états infini).
Classes d'états, automates temporisés.

**Réseaux de Pétri Colorés** (CPN):
Jetons ont "couleurs" (types, attributs).

**Avantages**:
- Modèle compact (un jeton coloré représente plusieurs jetons classiques)
- Données structurées

**Outil**: CPN Tools

**Réseaux de Pétri Stochastiques** (SPN):
Transitions avec taux de franchissement (lois exponentielles).

**Usage**: évaluation de performances (comme files d'attente).
Équivalent à chaînes de Markov continues.

**Réseaux de Pétri Hybrides**:
Variables continues et discrètes.
Modélise systèmes hybrides (manufacturiers, thermiques, etc.).

#### 9. Analyse par Réduction

**Transformations préservant propriétés**:

**Fusion de places parallèles**:
Places avec mêmes transitions amont/aval.

**Fusion de transitions parallèles**:
Transitions avec mêmes places amont/aval.

**Élimination de places implicites**:
Place dont marquage toujours suffit (contrainte redondante).

**Élimination de transitions**:
Sous certaines conditions (ne change pas comportement).

**Objectif**: simplifier modèle avant analyse.

#### 10. Outils Logiciels

**PIPE** (Platform Independent Petri net Editor):
- Modélisation graphique
- Simulation
- Analyse (graphe de marquage, invariants)
- Java, open source

**Tina**:
- Construction graphe de marquage
- Vérification propriétés temporelles (CTL)
- Synthèse de contrôleurs

**CPN Tools**:
- Pour réseaux colorés
- Simulation, state space analysis

**ROMEO**:
- Réseaux temporisés avec stopwatches
- Temps dense

**GreatSPN**:
- Stochastiques
- Évaluation de performances

#### 11. Commande par Réseaux de Pétri

**Synthèse de contrôleurs**:

**Problème**: système (plante) + spécifications → contrôleur

**Approches**:

**Théorie de la supervision**:
Désactiver transitions interdites pour respecter spécifications.

**Contrôle par place de contrôle**:
Ajouter places (avec arcs) pour imposer contraintes.

**Exemple**: éviter blocage, limiter nombre de pièces en cours (WIP).

**Applications**:
- Systèmes de production flexibles (FMS)
- Workflows
- Protocoles de communication

#### 12. Applications

**Systèmes de production**:
- Modéliser lignes de fabrication
- Partage de ressources (machines, robots)
- Ordonnancement
- Détection de blocages

**Protocoles de communication**:
- Handshake, synchronisation
- Détection d'interblocages
- Vérification de protocoles

**Workflows**:
- Processus métier
- Gestion de documents
- Validation de processus

**Systèmes informatiques**:
- Allocation mémoire
- Synchronisation de threads
- Gestion de transactions

**Systèmes embarqués**:
- Contrôle concurrent
- Vérification avant implémentation

## PART D: ANALYTICAL PART

### Knowledge and Skills Mobilized

- Compréhension des systèmes à événements discrets
- Modélisation graphique et formelle
- Algèbre linéaire (matrices, invariants)
- Théorie des graphes
- Analyse de propriétés (vivacité, bornitude)
- Utilisation d'outils logiciels de simulation
- Vérification formelle
- Synthèse de lois de commande

### Self Evaluation

Ce cours a été mathématiquement riche et conceptuellement dense. Les réseaux de Pétri sont un formalisme élégant mais nécessitent un changement de paradigme par rapport aux systèmes continus étudiés précédemment.

La représentation graphique est intuitive et pédagogique. Visualiser les jetons circuler dans le réseau aide à comprendre la dynamique. Cependant, passer du graphique au formel (matrices, équations) demande rigueur.

L'analyse des propriétés (vivacité, bornitude) est cruciale pour valider un système. Un modèle qui bloque ou dont les files explosent est inutilisable. Les méthodes d'analyse (graphe de marquage, invariants) fournissent des outils rigoureux.

Le graphe de marquage est conceptuellement simple mais peut devenir gigantesque (explosion combinatoire). C'est une limite pratique importante. Les techniques de réduction et les analyses partielles (invariants sans construire tout le graphe) sont essentielles.

Les invariants (P et T) sont puissants. Les P-invariants permettent de prouver la bornitude élégamment. Les T-invariants révèlent les cycles et comportements répétitifs.

L'équation d'état (M = M₀ + C^Tσ) est centrale. Elle offre une condition nécessaire d'accessibilité calculable algebraiquement, sans explorer tous les états.

Les extensions (temporisés, colorés, stochastiques) augmentent l'expressivité mais complexifient l'analyse. Il y a un trade-off entre pouvoir de modélisation et analysabilité.

La synthèse de contrôleurs par théorie de la supervision ouvre des perspectives intéressantes pour automatiser la conception de systèmes sûrs.

Les outils logiciels (PIPE, Tina) sont indispensables pour traiter des réseaux réalistes. Modéliser à la main est formateur mais limité à des exemples jouets.

Les applications sont nombreuses et variées. Cela montre la généralité du formalisme. Tout système avec événements, concurrence, et ressources partagées peut bénéficier d'une modélisation par réseau de Pétri.

### My Opinion

Ce cours fournit des outils puissants pour les systèmes à événements discrets, complémentaires aux techniques continues. Il est essentiel pour l'automaticien travaillant sur systèmes manufacturiers, protocoles, ou systèmes embarqués.

Points forts:
- Formalisme rigoureux et visuel
- Analyse de propriétés critiques (vivacité, absence de blocage)
- Applicabilité large
- Outils logiciels disponibles

Points à améliorer:
- Plus de cas d'études industriels complexes
- Lien avec implémentation (code généré depuis modèle)
- Comparaison avec autres formalismes (automates, algèbre de processus)
- Techniques pour gérer explosion combinatoire

Réflexions personnelles:

Les réseaux de Pétri sont un langage graphique universel pour SED. Leur avantage majeur est l'intégration de la modélisation, simulation, et vérification formelle dans un même cadre.

La vérification formelle est cruciale pour systèmes critiques (aérospatial, médical, nucléaire). Prouver mathématiquement l'absence de blocage ou de dépassement de capacité évite bugs catastrophiques.

Cependant, l'explosion combinatoire reste le défi majeur. Pour systèmes réalistes de grande taille, le graphe de marquage complet est incalculable. Les techniques d'abstraction, réduction, et vérification symbolique sont actives recherches.

La modularité et composabilité des réseaux de Pétri sont limitées. Combiner plusieurs sous-réseaux peut être ardu. Les réseaux colorés et hiérarchiques aident mais la complexité reste.

Le lien avec l'implémentation est parfois flou. Modéliser c'est bien, mais comment passer du modèle au code (PLC, microcontrôleur)? La génération automatique de code depuis réseaux de Pétri existe mais n'est pas standard.

Applications professionnelles:

Compétences en réseaux de Pétri applicables dans:
- **Automatisation industrielle**: conception et validation systèmes de production
- **Conception systèmes embarqués**: vérification propriétés temps réel
- **Réseaux de communication**: protocoles, gestion ressources
- **Logiciels**: modélisation workflows, processus métier
- **Recherche**: formalisation et analyse de systèmes complexes

Le marché:
Moins mainstream que contrôle continu ou programmation classique.
Niche dans domaines critiques nécessitant vérification formelle.
Compétence différenciante pour ingénieurs systèmes complexes.

L'avenir:
- Intégration avec Model-Based Design (Simulink, etc.)
- Codesign hardware/software
- Vérification de systèmes cyber-physiques
- IA et apprentissage: synthèse automatique de modèles depuis données

En conclusion, les réseaux de Pétri sont un formalisme puissant pour modéliser, analyser et vérifier des systèmes à événements discrets. Ils complètent les automates et les langages de description (GRAFCET, Statecharts) en offrant une sémantique mathématique rigoureuse et des outils d'analyse formelle. Ils restent utilisés en recherche et dans l'industrie pour les systèmes critiques.

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
      <h4>📖 Cours Complet Réseaux de Pétri</h4>
      <p>Cours complet : modélisation, propriétés structurelles et comportementales, analyse de vivacité et blocage.</p>
      <embed src="/cours-pdf/S8/Reseaux-Petri/cours-complet.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S8/Reseaux-Petri/cours-complet.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>📖 Examen 2023</h4>
      <p>Sujet d'examen 2023 : construction de réseaux, calcul d'invariants, analyse de blocage et synthèse.</p>
      <embed src="/cours-pdf/S8/Reseaux-Petri/exam-2023.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S8/Reseaux-Petri/exam-2023.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>📖 Correction 2023</h4>
      <p>Correction complète de l'examen 2023 avec méthodes d'analyse et explications détaillées.</p>
      <embed src="/cours-pdf/S8/Reseaux-Petri/correction-2023.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S8/Reseaux-Petri/correction-2023.pdf" target="_blank">📥 Télécharger</a></p>
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

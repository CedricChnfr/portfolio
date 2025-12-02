---
layout: default
title: "Systèmes Multivariables - S7"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
---

[← Back to My Courses 2023-2024](./my-courses-2023-2024.html)

# Systèmes Multivariables

## PART A: GENERALITIES

### Presentation
Le cours "Systèmes Multivariables" étend l'analyse et la commande des systèmes dynamiques au cas de systèmes à plusieurs entrées et plusieurs sorties (MIMO - Multiple Input Multiple Output). Ce cours est essentiel pour traiter des systèmes complexes réels qui ne peuvent être réduits à une seule entrée et une seule sortie.

**Année Académique**: 2023-2024  
**Semestre**: 7  
**Catégorie**: Automatique / Commande

---

## PART B: DESCRIPTIVE PART

### Experience Details

#### Environment and Context
Le cours combinait développements théoriques avancés (algèbre linéaire, analyse matricielle) avec des applications pratiques via Matlab/Simulink. Nous avons étudié des systèmes réels multivariables (avions, robots, procédés industriels) pour comprendre les défis spécifiques de leur analyse et commande.

#### My Function
Dans ce cours, j'ai été responsable de:
- Modéliser des systèmes MIMO par représentation d'état
- Analyser la commandabilité et l'observabilité
- Concevoir des lois de commande multivariables
- Utiliser des techniques de découplage
- Implémenter des observateurs d'état
- Simuler des systèmes multivariables sous Matlab
- Valider les performances et la robustesse

## PART C: TECHNICAL PART

Cette section explore les aspects techniques des systèmes multivariables.

### Technical Concepts Learned

#### 1. Représentation d'État

**Forme générale**:
```
ẋ(t) = A·x(t) + B·u(t)
y(t) = C·x(t) + D·u(t)

où:
- x ∈ ℝⁿ: vecteur d'état (n variables d'état)
- u ∈ ℝᵐ: vecteur d'entrée (m entrées)
- y ∈ ℝᵖ: vecteur de sortie (p sorties)
- A ∈ ℝⁿˣⁿ: matrice d'évolution
- B ∈ ℝⁿˣᵐ: matrice de commande
- C ∈ ℝᵖˣⁿ: matrice d'observation
- D ∈ ℝᵖˣᵐ: matrice de transmission directe
```

**Avantages de la représentation d'état**:
- Traitement naturel des systèmes MIMO
- Accès à toutes les variables internes
- Facilite l'analyse des propriétés structurelles
- Base pour commande moderne

**Passage fonction de transfert ↔ représentation d'état**:
- Matricielle pour MIMO
- Multiple réalisations possibles (commandable, observable, équilibrée)

#### 2. Matrice de Transfert

**Définition**:
```
G(s) = C(sI - A)⁻¹B + D

G(s) est une matrice p×m de fonctions de transfert:

     ⎡ G₁₁(s)  G₁₂(s)  ...  G₁ₘ(s) ⎤
G(s)=⎢ G₂₁(s)  G₂₂(s)  ...  G₂ₘ(s) ⎥
     ⎢   ...      ...    ...    ...  ⎥
     ⎣ Gₚ₁(s)  Gₚ₂(s)  ...  Gₚₘ(s) ⎦

Gᵢⱼ(s) = Yᵢ(s)/Uⱼ(s) quand toutes les autres entrées sont nulles
```

**Pôles et Zéros**:
- **Pôles**: valeurs propres de A (racines de det(sI-A))
- **Zéros de transmission**: annulent certains Gᵢⱼ(s)
- Plus complexe que SISO (zéros dépendent de la direction)

#### 3. Commandabilité

**Définition**:
Un système est commandable si on peut amener l'état d'une condition initiale quelconque à n'importe quel état final en temps fini.

**Critère de Kalman**:
```
rang(Mc) = n

où Mc = [B  AB  A²B  ...  Aⁿ⁻¹B]
Mc ∈ ℝⁿˣ⁽ⁿᵐ⁾ : matrice de commandabilité
```

**Interprétation**:
- Si commandable: on peut placer les pôles en boucle fermée où on veut
- Si non commandable: certains modes ne peuvent être influencés
- Décomposition de Kalman: partie commandable / non commandable

**Commandabilité de sortie**:
Peut-on commander spécifiquement les sorties?
```
rang(Mo) = p
où Mo = [CB  CAB  CA²B  ...  CAⁿ⁻¹B]
```

#### 4. Observabilité

**Définition**:
Un système est observable si on peut déterminer l'état initial à partir des entrées et sorties sur un intervalle de temps fini.

**Critère de Kalman**:
```
rang(Mo) = n

où Mo = ⎡  C  ⎤
          ⎢ CA  ⎥
          ⎢ CA² ⎥
          ⎢ ...  ⎥
          ⎣CAⁿ⁻¹⎦

Mo ∈ ℝ⁽ⁿᵖ⁾ˣⁿ : matrice d'observabilité
```

**Interprétation**:
- Si observable: on peut reconstruire l'état à partir des mesures
- Si non observable: certains modes restent cachés
- Nécessaire pour implémenter un observateur d'état

**Dualité**:
(A,B) commandable ⇔ (Aᵀ,Cᵀ) observable
Cette propriété simplifie les développements théoriques.

#### 5. Placement de Pôles par Retour d'État

**Loi de commande**:
```
u(t) = -K·x(t) + r(t)

où:
- K ∈ ℝᵐˣⁿ: matrice de gains
- r(t): référence
```

**Système en boucle fermée**:
```
ẋ(t) = (A - BK)·x(t) + B·r(t)
```

**Théorème de placement de pôles**:
Si (A,B) est commandable, on peut placer les n pôles de (A-BK) arbitrairement (en respectant conjugaison complexe).

**Méthodes de calcul de K**:

**Formule d'Ackermann** (SISO):
```
K = [0 ... 0 1]·Mc⁻¹·φ(A)
où φ(s) est le polynôme caractéristique désiré
```

**Placement de pôles Matlab**:
```matlab
K = place(A, B, poles)  % poles = vecteur des pôles désirés
```

**LQR (Linear Quadratic Regulator)**:
Optimisation d'un critère quadratique:
```
J = ∫₀^∞ (xᵀQx + uᵀRu) dt

K obtenu par résolution équation de Riccati algébrique
```

#### 6. Observateur d'État

**Problématique**:
En pratique, on ne mesure que les sorties y(t), pas l'état x(t).
L'observateur estime x̂(t) à partir de y(t) et u(t).

**Observateur de Luenberger**:
```
˙̂x(t) = A·x̂(t) + B·u(t) + L·(y(t) - ŷ(t))
ŷ(t) = C·x̂(t)

où L ∈ ℝⁿˣᵖ: matrice de gain de l'observateur
```

**Dynamique de l'erreur d'estimation**:
```
e(t) = x(t) - x̂(t)
ė(t) = (A - LC)·e(t)
```

**Théorème**:
Si (A,C) est observable, on peut placer les pôles de (A-LC) arbitrairement.

**Choix des pôles de l'observateur**:
Généralement 2 à 5 fois plus rapides que ceux du système commandé (principe de séparation).

**Commande par retour d'état estimé**:
```
u(t) = -K·x̂(t) + r(t)
```

**Principe de séparation**:
La dynamique globale (commande + observateur) = dynamique commande + dynamique observateur.
Les deux peuvent être conçus indépendamment.

#### 7. Découplage des Systèmes MIMO

**Problématique**:
Dans un système MIMO, une entrée uᵢ affecte généralement plusieurs sorties.
Objectif: découpler pour que chaque uᵢ n'affecte qu'une sortie yᵢ.

**Découplage statique**:
Trouver une matrice D telle que:
```
C(A-BK)⁻¹BD soit diagonale
```

**Découplage dynamique**:
Plus général, inclut prédistorsion dynamique.

**Découplage par précompensation**:
```
u(t) = F·v(t)
où F est choisie pour découpler
```

**Indices de découplage**:
Liés à la structure du système (ordre des dérivées nécessaires).

#### 8. Formes Canoniques

**Forme Commandable**:
Représentation où la commandabilité est évidente.
Utile pour placement de pôles.

**Forme Observable**:
Représentation où l'observabilité est évidente.
Utile pour conception d'observateur.

**Forme de Jordan**:
```
A est sous forme de blocs de Jordan
Révèle les modes propres du système
```

**Forme Équilibrée**:
Égalise commandabilité et observabilité.
Utile pour réduction de modèle.

#### 9. Stabilité des Systèmes Multivariables

**Critère**:
Système stable ⇔ toutes les valeurs propres de A ont partie réelle < 0.

**Critère de Lyapunov**:
Trouver matrice P > 0 telle que:
```
AᵀP + PA < 0
```

Garantit stabilité asymptotique.

**Stabilité entrée-sortie**:
Tous les pôles de G(s) (partie réelle < 0).

**Marge de stabilité**:
- Marge de gain
- Marge de phase
Généralisées pour MIMO (valeurs singulières).

#### 10. Analyse Fréquentielle MIMO

**Valeurs Singulières**:
Pour une matrice complexe G(jω):
```
σ̄(G) = valeur singulière maximale
σ(G) = valeur singulière minimale
```

**Interprétation**:
- σ̄(G(jω)): gain maximal du système à la fréquence ω
- σ(G(jω)): gain minimal

**Diagrammes de Bode multivar iables**:
Tracé de σ̄(G(jω)) et σ(G(jω)) en fonction de ω.

**Nombre de conditionnement**:
```
κ(G) = σ̄(G) / σ(G)
```

κ élevé ⇒ système mal conditionné (sensible aux perturbations).

#### 11. Commande LQG

**Combinaison LQR + Observateur Stochastique**:

**LQR**: placement optimal de pôles par minimisation de J
**Filtre de Kalman**: observateur optimal en présence de bruit

**Structure LQG**:
```
Système bruité:
ẋ = Ax + Bu + w    (w: bruit d'état)
y = Cx + v          (v: bruit de mesure)

Loi de commande:
u = -K·x̂
où x̂ est estimé par filtre de Kalman
```

**Propriétés**:
- Optimal si bruits gaussiens
- Principe de séparation encore valable
- Peut perdre robustesse (contrairement à LQR seul)

#### 12. Applications Pratiques

**Avion**:
- Entrées: gouvernes (ailerons, gouvernail, profondeur)
- Sorties: angles (roulis, lacet, tangage)
- Fortement couplé, nécessite découplage

**Robot manipulateur**:
- Entrées: couples aux articulations
- Sorties: positions articulaires
- Dynamique non-linéaire linéarisée autour d'un point

**Procédé chimique**:
- Multiples entrées (débits, températures)
- Multiples sorties (concentrations, pressions)
- Temps de réponse variés, couplages complexes

**Suspension active véhicule**:
- Entrées: forces des actuateurs (4 roues)
- Sorties: accélérations, positions (confort, tenue de route)
- Couplage mécanique

**Réseau électrique**:
- Multiples générateurs et charges
- Contrôle fréquence et tension
- Système distribué de grande dimension

## PART D: ANALYTICAL PART

### Knowledge and Skills Mobilized

- Algèbre linéaire avancée (matrices, valeurs propres, valeurs singulières)
- Analyse de systèmes dynamiques
- Maîtrise de la représentation d'état
- Théorie de la commande moderne
- Analyse structurelle (commandabilité, observabilité)
- Conception de lois de commande multivariables
- Conception d'observateurs d'état
- Utilisation de Matlab/Simulink pour simulations
- Analyse fréquentielle généralisée
- Compréhension des couplages entre entrées et sorties

### Self Evaluation

Ce cours a été l'un des plus exigeants mathématiquement du cursus. La manipulation de matrices, les changements de base, et les propriétés structurelles demandent une solide maîtrise de l'algèbre linéaire. Les premiers cours ont été denses et il a fallu du temps pour bien assimiler les concepts.

La représentation d'état, que j'avais déjà vue en SISO, prend toute sa puissance en MIMO. C'est le formalisme naturel pour ces systèmes, beaucoup plus pratique que les fonctions de transfert matricielles.

Les notions de commandabilité et d'observabilité sont fondamentales. Elles déterminent ce qu'on peut faire avec le système. Le fait qu'elles soient duales est élégant et permet de simplifier beaucoup de démonstrations.

Le placement de pôles par retour d'état est puissant mais nécessite de mesurer (ou estimer) tout l'état. L'observateur de Luenberger résout ce problème de manière élégante. Le principe de séparation est remarquable: on peut concevoir commande et observateur indépendamment.

Les simulations Matlab ont été essentielles pour développer l'intuition. Voir l'effet du choix des pôles, du gain de l'observateur, etc., sur les réponses temporelles aide énormément à comprendre la théorie.

Le découplage de systèmes MIMO est un problème difficile. Mathématiquement, on peut souvent le faire, mais les solutions peuvent être irréalistes (gains trop élevés, sensibilité aux incertitudes). Le compromis entre découplage parfait et robustesse est important.

L'approche LQR/LQG est séduisante car elle fournit une méthode systématique de conception. Cependant, le choix des matrices de pondération Q et R reste un art, et le lien avec les spécifications (dépassement, temps de réponse) n'est pas direct.

### My Opinion

Ce cours est fondamental pour l'automaticien moderne. Dans l'industrie, la plupart des systèmes sont multivariables: on ne peut plus se contenter de boucles SISO indépendantes. Les techniques MIMO sont incontournables.

Points forts du cours:
- Rigueur mathématique des développements
- Lien entre propriétés structurelles et possibilités de commande
- Élégance de certains résultats (dualité, séparation)
- Applications variées et concrètes
- Utilisation intensive de Matlab

Points à améliorer:
- Plus d'exemples de dimensionnement pratique
- Liens avec commande robuste (H∞, µ-synthèse)
- Aspects implémentation temps réel
- Gestion de contraintes (saturation des actionneurs)

Réflexions:

La représentation d'état est un changement de paradigme par rapport à l'approche fonction de transfert classique. Elle offre une vue "interne" du système et permet des techniques de commande beaucoup plus sophistiquées.

Cependant, la complexité mathématique peut être un frein. En pratique, il faut:
- Bons outils logiciels (Matlab Control Toolbox)
- Validation intensive par simulation
- Tests progressifs sur le système réel
- Robustesse face aux incertitudes de modélisation

La théorie suppose souvent que le modèle est parfait (matrices A,B,C,D exactes). En réalité, il y a toujours des incertitudes. Les techniques de commande robuste (que nous n'avons qu'effleurées) sont donc cruciales pour l'application industrielle.

Le découplage complet est séduisant sur le papier mais peut être contre-productif: il peut nécessiter des gains élevés et rendre le système fragile face aux incertitudes. Un découplage partiel ou une approche multivariable qui accepte les couplages mais les gère intelligemment est souvent préférable.

Pour ma carrière future:

Ces techniques sont applicables dans de nombreux domaines:
- Aéronautique et spatial (contrôle de vol)
- Automobile (ESP, suspensions actives, véhicules autonomes)
- Robotique (manipulateurs, drones)
- Procédés industriels (chimie, énergie)
- Systèmes énergétiques (smart grids)

La maîtrise de ces outils est un atout majeur pour concevoir des systèmes de commande performants et robustes. Couplée avec des compétences en traitement du signal, estimation, et optimisation, elle ouvre la voie à des carrières en R&D ou ingénierie avancée dans l'automatique et les systèmes embarqués.

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

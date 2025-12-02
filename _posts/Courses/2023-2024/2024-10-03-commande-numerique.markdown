---
layout: default
title: "Commande Numérique - S8"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
---

[← Back to My Courses 2023-2024](./my-courses-2023-2024.html)

**🔗 Cours connexes**: 
- [Temps Réel - S8](./2024-10-03-temps-reel.html) - Implémentation temps réel des lois de commande
- [Systèmes Multivariables - S7](./2024-10-03-systemes-multivariables.html) - Commande de systèmes MIMO

---

# Commande Numérique

## PART A: GENERALITIES

### Presentation
Le cours "Commande Numérique" traite de la conception et de l'implémentation de lois de commande sur calculateur numérique. Avec la généralisation des microcontrôleurs et processeurs, la commande numérique est devenue la norme dans l'industrie. Ce cours couvre la théorie de l'échantillonnage, la synthèse de correcteurs numériques, et leur implémentation pratique.

**Année Académique**: 2023-2024  
**Semestre**: 8  
**Catégorie**: Automatique / Commande

---

## PART B: DESCRIPTIVE PART

### Experience Details

#### Environment and Context
Le cours combinait développements mathématiques (transformée en Z, équations aux différences) avec implémentation sur microcontrôleur et simulation Matlab/Simulink. Nous avons conçu des régulateurs numériques pour différents systèmes (moteur, température, niveau) et les avons testés en laboratoire.

#### My Function
Dans ce cours, j'ai été responsable de:
- Comprendre la théorie de l'échantillonnage et ses effets
- Modéliser des systèmes continus en temps discret
- Synthétiser des correcteurs numériques (PID, RST, prédictif)
- Choisir la période d'échantillonnage appropriée
- Implémenter des lois de commande sur microcontrôleur
- Gérer les aspects pratiques (quantification, saturation, anti-windup)
- Valider les performances en simulation et expérimentation

## PART C: TECHNICAL PART

Cette section explore les aspects techniques de la commande numérique.

### Technical Concepts Learned

#### 1. Échantillonnage et Théorème de Shannon

**Principe**:
Conversion d'un signal continu s(t) en signal échantillonné s[k]:
```
s[k] = s(k·Te)
où Te est la période d'échantillonnage
Fe = 1/Te est la fréquence d'échantillonnage
```

**Théorème de Shannon**:
```
Fe ≥ 2·Fmax
```
Pour éviter le repliement spectral (aliasing).

**En pratique**:
```
Fe ≥ (6 à 40) × BW_système
```
où BW_système est la bande passante du système.

**Choix de Te**:
- Trop grande: perte d'information, instabilité
- Trop petite: charge calcul, coût, problèmes numériques
- Compromis selon application

#### 2. Bloqueur d'Ordre Zéro (BOZ / ZOH)

**Fonction**:
Maintenir la valeur de sortie constante entre deux échantillons:
```
u(t) = u[k]  pour k·Te ≤ t < (k+1)·Te
```

**Fonction de transfert**:
```
G_BOZ(s) = (1 - e^(-Te·s)) / s
```

**Effet fréquentiel**:
Atténuation haute fréquence (similaire à filtre passe-bas).

**Retard équivalent**:
≈ Te/2 (retard moyen introduit)

#### 3. Transformée en Z

**Définition**:
```
Z{s[k]} = S(z) = Σ s[k]·z^(-k)  pour k=0 à ∞

où z = e^(Te·s) relie plan de Laplace au plan en Z
```

**Propriétés**:
- **Linéarité**: Z{a·x[k] + b·y[k]} = a·X(z) + b·Y(z)
- **Retard**: Z{x[k-n]} = z^(-n)·X(z)
- **Avance**: Z{x[k+n]} = z^n·(X(z) - Σ x[k]·z^(-k))
- **Valeur initiale**: x[0] = lim(z→∞) X(z)
- **Valeur finale**: x[∞] = lim(z→1) (z-1)·X(z)  (si stable)

**Transformées usuelles**:
- Échelon: Z{1[k]} = z/(z-1)
- Rampe: Z{k} = Te·z/(z-1)²
- Exponentielle: Z{e^(a·k·Te)} = z/(z-e^(a·Te))
- Sinusoïde: Z{sin(ω·k·Te)} = z·sin(ω·Te)/(z²-2z·cos(ω·Te)+1)

#### 4. Fonction de Transfert en Z

**Définition**:
```
H(z) = Y(z)/U(z) = (b₀ + b₁·z^(-1) + ... + bₘ·z^(-m)) / (1 + a₁·z^(-1) + ... + aₙ·z^(-n))
```

**Équation aux différences**:
```
y[k] = -a₁·y[k-1] - ... - aₙ·y[k-n] + b₀·u[k] + b₁·u[k-1] + ... + bₘ·u[k-m]
```

Forme directement implémentable sur calculateur.

**Passage continu → discret**:

**Méthode d'Euler avant**:
```
s → (z-1)/Te
```

**Méthode d'Euler arrière (backward)**:
```
s → (z-1)/(Te·z)
```

**Méthode de Tustin (trapézoïdale)**:
```
s → (2/Te)·(z-1)/(z+1)
```

Plus précise, préserve mieux stabilité.

**Méthode de la réponse impulsionnelle invariante**

**Méthode ZOH (blocage d'ordre zéro)**:
```
H(z) = Z{L^(-1){G(s)/s · (1 - e^(-Te·s))}}
```

Méthode exacte pour système précédé d'un BOZ.

#### 5. Stabilité des Systèmes Discrets

**Condition de stabilité**:
Tous les pôles dans le cercle unité du plan en Z:
```
|z_i| < 1  pour tout pôle z_i
```

**Relation avec plan de Laplace**:
- **Demi-plan gauche (stable continu)** → **Intérieur cercle unité (stable discret)**
- **Axe imaginaire** → **Cercle unité**
- **Demi-plan droit (instable)** → **Extérieur cercle unité**

**Critère de Jury**:
Table de Routh équivalente pour temps discret.
Vérifie si polynôme a racines dans cercle unité.

**Lieu d'Evans discret**:
Similaire au continu mais interprétation différente (cercle unité).

#### 6. Analyse Fréquentielle Discrète

**Réponse fréquentielle**:
```
H(e^(jω·Te)) = H(z)|_(z=e^(jω·Te))
```

Périodique de période Fe (repliement).

**Diagrammes de Bode discrets**:
- Gain: |H(e^(jω·Te))|_(dB)
- Phase: arg(H(e^(jω·Te)))

Tracés pour ω ∈ [0, π/Te] (jusqu'à Fe/2).

**Marges de stabilité**:
- Marge de gain
- Marge de phase

Interprétation similaire au continu.

#### 7. Régulateur PID Numérique

**Forme continue**:
```
C(s) = Kp + Ki/s + Kd·s
```

**Discrétisation**:

**Forme vitesse (incrémentale)**:
```
Δu[k] = u[k] - u[k-1]
Δu[k] = q0·e[k] + q1·e[k-1] + q2·e[k-2]
```

Où:
- q0 = Kp + Ki·Te + Kd/Te
- q1 = -Kp - 2·Kd/Te
- q2 = Kd/Te

**Forme position**:
```
u[k] = Kp·e[k] + Ki·Te·Σe[k] + Kd·(e[k]-e[k-1])/Te
```

**Action proportionnelle**:
```
uP[k] = Kp·e[k]
```

**Action intégrale (méthode rectangulaire)**:
```
uI[k] = uI[k-1] + Ki·Te·e[k]
```

**Action dérivée**:
```
uD[k] = Kd·(e[k] - e[k-1])/Te
```

Souvent filtrée pour réduire bruit:
```
uD[k] = α·uD[k-1] + Kd·(1-α)·(e[k]-e[k-1])/Te
```

#### 8. Correcteurs Polynomiaux RST

**Structure**:
```
R(z)·U(z) = T(z)·Yref(z) - S(z)·Y(z)
```

Où:
- R, S, T sont des polynômes en z^(-1)
- Offre plus de degrés de liberté que PID

**Équation de commande**:
```
u[k] = (1/r₀)·[t₀·yref[k] + ... - s₀·y[k] - s₁·y[k-1] - ... - r₁·u[k-1] - ...]
```

**Synthèse par placement de pôles**:
Résolution de l'équation diophantienne:
```
A·R + B·S = P_désiré
```

Où P_désiré contient les pôles en boucle fermée souhaités.

**Avantages**:
- Placement précis des pôles
- Gestion des zéros du système
- Robustesse ajustable

#### 9. Commande Prédictive (MPC)

**Principe**:
Optimiser une séquence de commandes futures pour minimiser un critère.

**Critère**:
```
J = Σ [w_y·(yref[k+i] - y[k+i])² + w_u·Δu[k+i]²]
```

Sur un horizon de prédiction.

**Algorithme**:
1. Prédire sortie future avec modèle
2. Optimiser commande pour minimiser J
3. Appliquer première commande u[k]
4. Répéter à chaque instant (receding horizon)

**Avantages**:
- Gestion naturelle des contraintes (saturation)
- Anticipation (action prédictive)
- MIMO naturellement

**Inconvénients**:
- Charge calcul élevée
- Nécessite modèle précis

#### 10. Aspects Pratiques d'Implémentation

**Quantification**:
- **ADC**: signal analogique → valeur numérique
- **Calculs**: virgule fixe ou flottante
- **DAC**: valeur numérique → signal analogique

Erreurs de quantification peuvent causer:
- Cycles limites (oscillations)
- Dégradation de performance

**Saturations**:
Actionneurs ont limites physiques:
```
u_min ≤ u[k] ≤ u_max
```

**Anti-windup**:
Quand u sature, l'intégrateur continue à s'accumuler (windup).

Solution:
```
Si u saturé:
  uI[k] = uI[k-1]  (geler intégrale)
ou
  uI[k] = u_sat - uP[k] - uD[k]  (back-calculation)
```

**Filtre dérivé**:
L'action dérivée amplifie le bruit.
Filtrer avec passe-bas:
```
D_filtré(z) = Kd·z/(z + α)  avec 0 < α < 1
```

**Bumpless transfer**:
Lors de changement de mode (manuel → auto), éviter saut brutal:
- Initialiser correctement l'intégrateur
- Transition douce

**Temps d'exécution**:
Le code de commande doit s'exécuter en moins de Te:
```
T_exec < Te
```

Sinon, instabilité ou perte d'échantillons.

Optimisations:
- Code efficace (éviter fonctions coûteuses)
- Utiliser virgule fixe si nécessaire
- Interruptions pour timing précis

#### 11. Observateurs Discrets

**Problématique**:
Si toutes les variables d'état ne sont pas mesurées, les estimer.

**Observateur de Luenberger discret**:
```
x̂[k+1] = A·x̂[k] + B·u[k] + L·(y[k] - ŷ[k])
ŷ[k] = C·x̂[k]
```

**Placement des pôles de l'observateur**:
Plus rapides que ceux du système (2-5 fois).

**Filtre de Kalman**:
Observateur optimal en présence de bruit.

#### 12. Outils de Simulation et Test

**Matlab/Simulink**:
- Blocs temps discret
- Modélisation système mixte (continu + discret)
- Discrétisation automatique (c2d)
- Analyse performance

**Processor-in-the-Loop (PIL)**:
Simulation avec code réel sur processeur cible.
Vérifie comportement avec quantification, timing réel.

**Hardware-in-the-Loop (HIL)**:
Contrôleur réel + système simulé temps réel.
Validation avant tests sur système physique.

**Banc d'essai**:
Test sur système réel avec instrumentation.
Validation finale.

## PART D: ANALYTICAL PART

### Knowledge and Skills Mobilized

- Théorie de l'échantillonnage et transformée en Z
- Discrétisation de systèmes continus
- Analyse de stabilité des systèmes discrets
- Synthèse de correcteurs numériques (PID, RST, MPC)
- Programmation de lois de commande sur microcontrôleur
- Gestion des aspects pratiques (quantification, saturation, timing)
- Utilisation de Matlab/Simulink pour conception et simulation
- Validation expérimentale sur systèmes réels
- Optimisation de code pour temps réel

### Self Evaluation

Ce cours a été crucial pour comprendre que la commande numérique n'est pas qu'une simple discrétisation de la commande continue. L'échantillonnage introduit des phénomènes spécifiques (repliement, retard) qui doivent être pris en compte.

La transformée en Z, initialement abstraite, est devenue un outil naturel après pratique. La correspondance plan s ↔ plan z est fondamentale pour comprendre comment les propriétés continues se transposent en discret.

Le choix de la période d'échantillonnage est un compromis délicat. J'ai appris qu'il ne suffit pas de respecter Shannon; il faut échantillonner suffisamment vite pour que le comportement discret soit proche du continu, mais pas trop pour éviter problèmes numériques et charge calcul.

Le PID numérique semble simple mais les détails d'implémentation (forme vitesse vs position, anti-windup, filtre dérivé) sont essentiels pour performance et robustesse. Les problèmes de windup peuvent causer des comportements très surprenants.

Les correcteurs RST offrent beaucoup plus de flexibilité que le PID. La synthèse par placement de pôles est élégante mathématiquement, mais le choix des pôles désirés reste un art (compromis performance/robustesse).

La commande prédictive (MPC) est séduisante pour sa capacité à gérer contraintes et anticipation. Cependant, la charge calcul peut être prohibitive pour systèmes rapides ou microcontrôleurs limités. C'est un domaine de recherche actif.

L'implémentation sur microcontrôleur m'a confronté à des problèmes pratiques souvent ignorés en cours théoriques: timing d'interruptions, virgule fixe vs flottante, gestion des dépassements arithmétiques. Le code doit être robuste et efficace.

Les simulations Processor-in-the-Loop ont révélé des écarts entre théorie et pratique: quantification, arrondis, délais de calcul peuvent dégrader performance voire déstabiliser.

### My Opinion

Ce cours est indispensable à l'ère du numérique. Pratiquement toute commande moderne est implémentée sur calculateur. Maîtriser les spécificités du discret est donc essentiel.

Points forts:
- Équilibre théorie mathématique / implémentation pratique
- Outils modernes (Matlab, microcontrôleurs)
- Projets hands-on avec systèmes réels
- Prise en compte des contraintes pratiques

Points à améliorer:
- Plus de temps sur commande prédictive (MPC)
- Aspects multi-tâches et systèmes d'exploitation temps réel
- Commande adaptative et robuste
- Certification (normes industrielles)

Réflexions personnelles:

La commande numérique a révolutionné l'automatique. Ce qui était impensable en analogique (MPC, observateurs complexes, adaptation) devient possible avec des microcontrôleurs peu coûteux.

Cependant, la puissance de calcul disponible peut donner une fausse impression de facilité. Un correcteur mal conçu (instabilité numérique, paramètres inadaptés) ne marchera pas mieux sous prétexte qu'il est numérique.

La tendance est à l'augmentation de la puissance de calcul (processeurs multi-cœurs, FPGA, DSP). Cela ouvre des possibilités (fusion multi-capteurs, traitement d'image embarqué, IA embarquée) mais nécessite expertise en programmation temps réel et optimisation.

La séparation traditionnelle entre électronicien et informaticien s'estompe. L'ingénieur moderne doit maîtriser hardware (capteurs, actionneurs, électronique) ET software (algorithmes, programmation embarquée, architectures logicielles).

Applications professionnelles:

Ces compétences sont applicables dans tous les domaines de l'automatique industrielle:
- Robotique (commande d'articulations)
- Automobile (ESP, ABS, contrôle moteur)
- Aéronautique (pilote automatique)
- Procédés industriels (régulation température, pression, débit)
- Énergie (onduleurs, convertisseurs)
- Drones (stabilisation, navigation)

La maîtrise de la commande numérique, couplée à des compétences en traitement du signal et systèmes embarqués, est un profil très recherché en industrie.

L'avenir verra probablement:
- Intégration de l'IA dans les boucles de commande
- Commande distribuée et collaborative (systèmes multi-agents)
- Auto-tuning et adaptation automatique
- Co-design hardware/software pour optimisation globale

Avoir des bases solides en commande numérique classique est le prérequis pour comprendre et contribuer à ces évolutions futures.

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

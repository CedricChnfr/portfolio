---
layout: default
title: "Analyse des Systèmes Non Linéaires - S7"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
---

<style>
.back-nav {
    background: #f4f4f4;
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 20px;
}

.section-title {
    color: #2a7ae2;
    border-bottom: 2px solid #2a7ae2;
    padding-bottom: 5px;
    margin-top: 30px;
}

table {
    border-collapse: collapse;
    width: 100%;
    margin: 20px 0;
}

th {
    background-color: #2a7ae2;
    color: white;
    padding: 10px;
    text-align: left;
}

td {
    border: 1px solid #ddd;
    padding: 10px;
}

tr:nth-child(even) {
    background-color: #f9f9f9;
}

.code-block {
    background: #f4f4f4;
    border-left: 4px solid #2a7ae2;
    padding: 15px;
    margin: 15px 0;
    font-family: 'Courier New', monospace;
}
</style>

<div class="back-nav">
    <a href="./my-courses-2023-2024.html">← Retour aux Cours 2023-2024</a>
</div>

# 🔄 Analyse des Systèmes Non Linéaires - Semestre 7

**Année Universitaire** : 2023-2024  
**Semestre** : 7  
**Crédits** : 2.5 ECTS  
**Spécialité** : Automatique et Systèmes

---

## PART A - Présentation Générale du Module

<h3 class="section-title">Vue d'ensemble</h3>

L'analyse des systèmes non linéaires est une extension naturelle de l'automatique linéaire vers les systèmes réels. Contrairement aux systèmes linéaires, les systèmes non linéaires peuvent exhiber des comportements complexes : points d'équilibre multiples, cycles limites, bifurcations, et même chaos. Ce cours fournit les outils mathématiques pour analyser la stabilité et le comportement de ces systèmes.

**Objectifs pédagogiques** :
- Comprendre les phénomènes non linéaires (saturation, hystérésis, cycles limites)
- Maîtriser la théorie de stabilité de Lyapunov
- Analyser les systèmes dans le plan de phase
- Appliquer la méthode du premier harmonique (describing function)
- Étudier les bifurcations et le chaos
- Concevoir des lois de commande non linéaires

<h3 class="section-title">Position dans le cursus</h3>

Ce module s'appuie sur :
- **Systèmes multivariables (S7)** : représentation d'état, stabilité
- **Modélisation et commande des systèmes linéaires (S5)** : fonction de transfert, Bode, Nyquist
- **Mathématiques** : équations différentielles, analyse

Il prépare à :
- **Commande avancée** : commande robuste, adaptative
- **Robotique** : modélisation et commande de robots (systèmes fortement non linéaires)
- **Applications industrielles** : régulation de processus, aérospatial

---

## PART B - Expérience Personnelle et Contexte d'Apprentissage

<h3 class="section-title">Organisation et ressources</h3>

Le module était organisé en cours magistraux et travaux dirigés sur le semestre :

**Cours magistraux (20h)** :
Structuré en 5 chapitres (chapitre1 à chapitre5) :
- Chapitre 1 : Introduction aux systèmes non linéaires
- Chapitre 2 : Analyse dans le plan de phase
- Chapitre 3 : Stabilité au sens de Lyapunov
- Chapitre 4 : Méthode du premier harmonique
- Chapitre 5 : Bifurcations et chaos

**Travaux dirigés (16h)** :
9 séances de TD avec exercices d'application :
- TD1 à TD4 : plan de phase, points d'équilibre
- TD5 à TD7 : stabilité de Lyapunov
- TD8 et TD9 : méthode du premier harmonique

**Supports pédagogiques** :
- Fascicules de cours (handout PDF)
- Énoncés de TD (td1.pdf à td9.pdf)
- Simulations MATLAB/Simulink (simtd1.slx, simtd3.slx)
- Annales d'examens 2013, 2016, 2017, 2023 avec corrigés

<h3 class="section-title">Méthode de travail</h3>

**Cours théorique** :
Le cours est mathématiquement exigeant avec de nombreuses démonstrations. La compréhension des concepts (fonctions de Lyapunov, stabilité asymptotique) demande du temps et de la pratique.

**TD et simulations** :
Les TD permettent d'appliquer la théorie sur des exemples concrets (pendule, circuits électriques, systèmes mécaniques). Les simulations Simulink visualisent les comportements non linéaires.

**Annales** :
Les annales de 2013 à 2023 avec corrections sont essentielles pour comprendre les attentes et le type d'exercices (analyse de stabilité, plan de phase, méthode du premier harmonique).

<h3 class="section-title">Difficultés rencontrées</h3>

**Abstraction mathématique** :
La théorie de Lyapunov est puissante mais abstraite. Trouver une fonction de Lyapunov candidate pour prouver la stabilité n'est pas systématique et demande de l'intuition.

**Visualisation des comportements** :
Comprendre les portraits de phase (trajectoires dans l'espace d'état) nécessite une bonne visualisation géométrique.

**Méthode du premier harmonique** :
La méthode est basée sur des approximations (ne conserver que le premier harmonique). Comprendre ses limites et domaines de validité est important.

---

## PART C - Aspects Techniques Détaillés

<h3 class="section-title">1. Introduction aux systèmes non linéaires</h3>

**Définition** :

Un système est non linéaire si son équation ne vérifie pas le principe de superposition. Formellement, si :
- x1(t) → y1(t)
- x2(t) → y2(t)

Alors pour un système linéaire : a×x1(t) + b×x2(t) → a×y1(t) + b×y2(t)

Si cette propriété n'est pas vérifiée, le système est non linéaire.

**Exemples de non-linéarités** :

| Type | Equation | Exemples |
|------|----------|----------|
| Saturation | y = sat(u) | Actionneurs limités, amplificateurs |
| Zone morte | y = 0 si abs(u) < delta | Jeux mécaniques, seuils |
| Hystérésis | y dépend de l'historique | Matériaux magnétiques, frottement |
| Multiplication | y = u1 × u2 | Modulation, puissance |
| Fonction trigonométrique | y = sin(u) | Pendule, robots |
| Puissance | y = u² ou u³ | Aerodynamique, hydraulique |

**Conséquences de la non-linéarité** :

- **Points d'équilibre multiples** : plusieurs états stables possibles
- **Cycles limites** : oscillations auto-entretenues (indépendantes des conditions initiales)
- **Phénomènes de saut** : changement brutal de comportement
- **Sous-harmoniques** : fréquences multiples dans la réponse
- **Chaos** : comportement imprévisible malgré un système déterministe

<h3 class="section-title">2. Modélisation des systèmes non linéaires</h3>

**Représentation d'état** :

Forme générale d'un système non linéaire :

x point = f(x, u, t)
y = g(x, u, t)

où x est le vecteur d'état, u l'entrée, y la sortie.

**Systèmes autonomes** :

Si f ne dépend pas explicitement du temps :
x point = f(x)

**Exemple : pendule simple**

Équation du mouvement :
theta point point + (g/L) sin(theta) = 0

Représentation d'état :
- x1 = theta (position angulaire)
- x2 = theta point (vitesse angulaire)

x1 point = x2
x2 point = -(g/L) sin(x1)

**Points d'équilibre** :

Solutions de f(x_eq) = 0

Pour le pendule :
- x_eq1 = (0, 0) : position basse (stable)
- x_eq2 = (π, 0) : position haute (instable)

<h3 class="section-title">3. Analyse dans le plan de phase</h3>

**Définition** :

Pour un système du second ordre (2 variables d'état), le plan de phase représente les trajectoires dans l'espace (x1, x2).

**Portrait de phase** :

Ensemble des trajectoires pour différentes conditions initiales. Permet de visualiser :
- Points d'équilibre
- Stabilité
- Bassins d'attraction
- Cycles limites

**Classification des points d'équilibre** :

Linéarisation autour du point d'équilibre :
x point = A × x

où A est la matrice jacobienne au point d'équilibre.

| Valeurs propres | Type | Stabilité |
|-----------------|------|-----------|
| Réelles négatives | Nœud stable | Stable |
| Réelles positives | Nœud instable | Instable |
| Complexes Re < 0 | Foyer stable | Stable |
| Complexes Re > 0 | Foyer instable | Instable |
| Imaginaires pures | Centre | Marginalement stable |
| Opposées (± lambda) | Point selle | Instable |

**Exemple : pendule amorti**

theta point point + b theta point + (g/L) sin(theta) = 0

Avec amortissement b > 0 :
- Point (0, 0) : foyer stable (spirale convergeant vers l'origine)
- Point (π, 0) : point selle (instable)

**Séparatrices** :

Trajectoires qui séparent différents bassins d'attraction. Pour le pendule, les séparatrices partent du point selle.

<h3 class="section-title">4. Stabilité au sens de Lyapunov</h3>

**Définition de la stabilité** :

Un point d'équilibre x_eq est :
- **Stable** : si pour toute condition initiale proche, la trajectoire reste proche
- **Asymptotiquement stable** : stable + converge vers x_eq
- **Instable** : sinon

**Théorème de Lyapunov (méthode directe)** :

Soit V(x) une fonction scalaire (fonction de Lyapunov candidate) :

**Conditions** :
1. V(x) > 0 pour tout x différent de 0 (définie positive)
2. V(0) = 0
3. V point(x) <= 0 (dérivée négative ou nulle)

**Conclusion** :
Si conditions 1, 2, 3 vérifiées : point d'équilibre stable

Si en plus V point(x) < 0 (strictement négatif) : asymptotiquement stable

**Interprétation** :

V(x) peut être vue comme une fonction d'énergie généralisée. Si l'énergie décroît (V point < 0), le système converge vers l'équilibre.

**Exemple : système linéaire x point = A x**

Fonction de Lyapunov candidate : V(x) = x^T P x (forme quadratique)

Dérivée : V point = x^T (A^T P + P A) x

Pour que V point < 0, il faut : A^T P + P A = -Q avec Q > 0

Cette équation (équation de Lyapunov) a une solution P > 0 si et seulement si A est stable (valeurs propres à partie réelle négative).

**Exemple : pendule avec frottement**

Système :
x1 point = x2
x2 point = -(g/L) sin(x1) - b x2

Fonction de Lyapunov (énergie totale) :
V(x1, x2) = (1/2) x2² + (g/L) (1 - cos(x1))

V(0, 0) = 0 et V(x1, x2) > 0 pour (x1, x2) différent de (0, 0)

Dérivée :
V point = x2 × x2 point + (g/L) sin(x1) × x1 point
V point = x2 × (-(g/L) sin(x1) - b x2) + (g/L) sin(x1) × x2
V point = -b x2²

V point <= 0 (négatif ou nul), donc le point (0, 0) est stable.
V point < 0 pour x2 différent de 0, donc asymptotiquement stable.

**Région de stabilité** :

La région où V(x) < c (constante) et V point < 0 est une estimation du bassin d'attraction.

**Limitation** :

Trouver une fonction de Lyapunov n'est pas systématique. Il n'y a pas de méthode générale. L'ingénieur doit essayer différentes fonctions candidates (souvent basées sur l'énergie physique du système).

<h3 class="section-title">5. Principe d'invariance de LaSalle</h3>

**Extension du théorème de Lyapunov** :

Si V point <= 0 (et non strictement < 0), le théorème de Lyapunov standard ne conclut que sur la stabilité, pas la convergence asymptotique.

**Théorème de LaSalle** :

Si V point <= 0, le système converge vers le plus grand ensemble invariant contenu dans l'ensemble où V point = 0.

**Application** :

Pour le pendule, V point = -b x2² = 0 seulement si x2 = 0.
L'ensemble où V point = 0 est l'axe x1 (vitesse nulle).
Le seul ensemble invariant sur cet axe est le point (0, 0).
Donc le système converge vers (0, 0) : stabilité asymptotique.

<h3 class="section-title">6. Méthode du premier harmonique (Describing Function)</h3>

**Objectif** :

Analyser les cycles limites (oscillations auto-entretenues) dans les systèmes bouclés comportant une non-linéarité.

**Principe** :

Remplacer la non-linéarité par un gain équivalent qui dépend de l'amplitude de l'entrée.

**Système considéré** :

Boucle fermée : partie linéaire G(jω) + non-linéarité N

**Hypothèse** :
- Si l'entrée de la non-linéarité est sinusoïdale : e(t) = A sin(ωt)
- La sortie contient des harmoniques : s(t) = B1 sin(ωt + φ1) + B2 sin(2ωt + φ2) + ...
- Si G(jω) est passe-bas, les harmoniques supérieurs sont atténués
- On ne conserve que le premier harmonique

**Fonction de description** :

N(A) = B1 / A × exp(j φ1)

Rapport complexe entre le premier harmonique de sortie et l'entrée.

**Exemples de fonctions de description** :

| Non-linéarité | N(A) |
|---------------|------|
| Gain linéaire k | k (constant) |
| Saturation | (2k/π) [arcsin(M/A) + (M/A) sqrt(1 - (M/A)²)] |
| Zone morte | k [1 - (delta/A)] si A > delta |
| Relais ± M | (4M) / (π A) |
| Hystérésis | Fonction complexe (déphasage) |

**Condition d'existence d'un cycle limite** :

Un cycle limite existe si :
1 + G(jω) × N(A) = 0

Ou : G(jω) = -1 / N(A)

**Graphiquement** :

Tracer G(jω) (Nyquist) et -1/N(A) dans le plan complexe.
Les intersections donnent les cycles limites possibles (fréquence ω et amplitude A).

**Stabilité du cycle limite** :

- Si -1/N(A) croise G(jω) de droite à gauche (en augmentant ω) : cycle stable
- Si croisement de gauche à droite : cycle instable

**Limitations** :

- Valable si harmoniques supérieurs négligeables
- Ne fonctionne pas pour toutes les non-linéarités
- Résultats approximatifs

<h3 class="section-title">7. Linéarisation par bouclage (Feedback Linearization)</h3>

**Objectif** :

Concevoir une loi de commande qui linéarise exactement le système non linéaire.

**Système non linéaire** :

x point = f(x) + g(x) u

**Commande linéarisante** :

u = (1/g(x)) [-f(x) + v]

où v est une nouvelle entrée.

**Système en boucle fermée** :

x point = v (système linéaire !)

On peut alors choisir v pour obtenir la dynamique désirée (placement de pôles, LQR, etc.).

**Exemple : pendule inversé**

Équation : theta point point = (g/L) sin(theta) + u

Avec u = -(g/L) sin(theta) + v :
theta point point = v (double intégrateur linéaire)

On peut alors stabiliser avec v = -k1 theta - k2 theta point (PD)

**Limitations** :

- Nécessite la mesure ou estimation de tous les états
- Modèle exact du système requis
- Annulation de non-linéarités peut amplifier les perturbations
- Pas toujours possible (conditions mathématiques à vérifier)

<h3 class="section-title">8. Commande par modes glissants (Sliding Mode Control)</h3>

**Principe** :

Concevoir une surface de glissement s(x) = 0 sur laquelle le système a le comportement désiré, puis forcer le système à rester sur cette surface.

**Étapes** :

1. **Définir la surface** : s(x) = 0 (combinaison linéaire des états)
2. **Loi de commande** : u force s(x) à converger vers 0
3. **Mode glissant** : une fois sur s(x) = 0, le système y reste

**Exemple : système du 1er ordre**

x point = f(x) + g(x) u

Surface : s(x) = x - x_désiré

Commande : u = (1/g(x)) [-f(x) - k sign(s)]

avec k > 0 suffisamment grand.

**Propriétés** :

- **Robustesse** : insensible aux perturbations et incertitudes de modèle
- **Convergence en temps fini** : atteint la surface en temps fini
- **Chattering** : oscillations haute fréquence autour de la surface (problème pratique)

**Réduction du chattering** :

Remplacer sign(s) par sat(s/epsilon) ou tanh(s/epsilon) pour lisser la commande.

<h3 class="section-title">9. Bifurcations</h3>

**Définition** :

Changement qualitatif du comportement d'un système quand un paramètre varie.

**Types de bifurcations** :

**Bifurcation selle-nœud** :
- Apparition ou disparition de points d'équilibre
- Exemple : x point = r + x² (pour r < 0 : 2 équilibres, r = 0 : 1 équilibre, r > 0 : aucun)

**Bifurcation transcritique** :
- Échange de stabilité entre deux points d'équilibre

**Bifurcation fourche (pitchfork)** :
- Un point d'équilibre se divise en trois
- Symétrique ou asymétrique

**Bifurcation de Hopf** :
- Apparition d'un cycle limite à partir d'un point d'équilibre
- Exemple : oscillateur de Van der Pol

**Diagramme de bifurcation** :

Graphique représentant les points d'équilibre (ou amplitudes de cycles) en fonction du paramètre.

<h3 class="section-title">10. Introduction au chaos</h3>

**Définition** :

Comportement apériodique déterministe sensible aux conditions initiales.

**Caractéristiques** :

- **Déterministe** : pas de hasard, équations précises
- **Apériodique** : ne se répète jamais exactement
- **Sensibilité aux conditions initiales** : deux trajectoires proches divergent exponentiellement (effet papillon)

**Exposants de Lyapunov** :

Mesurent le taux moyen de divergence ou convergence des trajectoires.
- Exposant > 0 : divergence (chaos)
- Exposant < 0 : convergence (stabilité)
- Exposant = 0 : comportement marginal

**Exemples de systèmes chaotiques** :

**Système de Lorenz** :
x point = sigma (y - x)
y point = r x - y - x z
z point = x y - b z

Pour certaines valeurs de paramètres (r = 28, sigma = 10, b = 8/3) : comportement chaotique (attracteur étrange).

**Attracteur de Lorenz** :

Structure géométrique en forme de papillon dans l'espace de phase. Les trajectoires tournent autour de deux lobes sans jamais se répéter.

**Route vers le chaos** :

Cascade de doublement de période : oscillation de période T → 2T → 4T → 8T → ... → chaos

**Carte de Poincaré** :

Réduction d'un système continu par échantillonnage (intersection avec une surface). Facilite l'analyse du chaos.

<h3 class="section-title">11. Applications pratiques</h3>

**Pendule inversé** :

Système instable en boucle ouverte. Linéarisation par bouclage ou commande par modes glissants pour stabilisation.

**Oscillateur de Van der Pol** :

x point point - mu (1 - x²) x point + x = 0

Pour mu > 0 : cycle limite (oscillation auto-entretenue). Exemple de système présentant une bifurcation de Hopf.

**Circuit de Chua** :

Circuit électronique simple exhibant du chaos. Utilisé pour étudier les systèmes chaotiques en laboratoire.

**Système proie-prédateur (Lotka-Volterra)** :

x point = a x - b x y (proies)
y point = -c y + d x y (prédateurs)

Modèle biologique avec cycles (oscillations des populations).

---

## PART D - Analyse Réflexive et Perspectives

<h3 class="section-title">Compétences acquises</h3>

**Analyse de stabilité** :
Maîtrise de la théorie de Lyapunov pour prouver rigoureusement la stabilité de systèmes non linéaires. Capacité à construire des fonctions de Lyapunov candidates.

**Visualisation géométrique** :
Compréhension des portraits de phase et trajectoires dans l'espace d'état. Identification des points d'équilibre et de leur nature (nœud, foyer, selle).

**Analyse fréquentielle** :
Application de la méthode du premier harmonique pour prédire l'existence de cycles limites dans les systèmes bouclés.

<h3 class="section-title">Points clés à retenir</h3>

**1. Non-linéarité = richesse comportementale** :
Les systèmes non linéaires peuvent avoir des comportements très variés (multistabilité, cycles limites, chaos) que les systèmes linéaires ne peuvent pas exhiber.

**2. Lyapunov = outil fondamental** :
La théorie de Lyapunov est la méthode principale pour prouver la stabilité. L'énergie du système est souvent une bonne fonction de Lyapunov candidate.

**3. Linéarisation locale vs globale** :
L'analyse linéaire locale (jacobienne) donne des informations près des équilibres mais ne capture pas le comportement global.

**4. Méthode du premier harmonique = approximation** :
Utile pour analyser rapidement les cycles limites mais résultats approximatifs.

**5. Chaos = déterministe mais imprévisible** :
Le chaos montre qu'un système simple et déterministe peut être imprévisible à long terme. Importance de la sensibilité aux conditions initiales.

<h3 class="section-title">Applications pratiques</h3>

**Robotique** :
Les robots sont des systèmes fortement non linéaires (couplages, frottements, gravité). Les méthodes de linéarisation par bouclage sont couramment utilisées.

**Aérospatial** :
Contrôle d'attitude des satellites et avions (non-linéarités angulaires). Analyse de stabilité critique pour la sécurité.

**Processus industriels** :
Régulation de température, pression, débit avec actionneurs saturés. Analyse de stabilité et anti-windup.

**Électronique de puissance** :
Convertisseurs DC-DC avec commutations (non-linéarités par morceaux). Commande par modes glissants fréquemment employée.

<h3 class="section-title">Retour d'expérience</h3>

**Cours exigeant** :
Le niveau mathématique est élevé. Les démonstrations de théorèmes (Lyapunov, LaSalle) demandent rigueur et abstraction.

**TD essentiels** :
Les 9 TD permettent de s'approprier les concepts sur des exemples concrets. Les simulations Simulink aident à visualiser les comportements.

**Annales précieuses** :
Les annales de 2013 à 2023 montrent les types d'exercices (analyse de stabilité, plan de phase, méthode harmonique). Les corrections détaillées sont très utiles.

**Fascination pour le chaos** :
Découvrir que des systèmes simples (3 équations) peuvent générer du chaos est marquant. Le paradoxe déterminisme/imprévisibilité est philosophiquement intéressant.

<h3 class="section-title">Limites et ouvertures</h3>

**Limites du module** :
- Peu de TP pratiques (surtout théorique)
- Commande adaptative et robuste non traitées en détail
- Systèmes hybrides (continus + discrets) non abordés

**Ouvertures vers** :
- **Commande robuste H-infini** : prise en compte d'incertitudes
- **Commande adaptative** : systèmes avec paramètres inconnus ou variants
- **Observation non linéaire** : estimation d'états pour systèmes non linéaires
- **Systèmes hybrides** : mélange dynamiques continues et discrètes
- **Machine learning pour la commande** : apprentissage de lois de commande non linéaires

<h3 class="section-title">Conseils pour réussir</h3>

**1. Travailler les TD** :
Refaire les 9 TD sans regarder les corrections. Les exercices couvrent tous les aspects du cours.

**2. Visualiser avec MATLAB** :
Utiliser les simulations Simulink fournies (simtd1, simtd3) et créer ses propres simulations pour explorer les comportements.

**3. S'entraîner sur les annales** :
Les examens de 2013 à 2023 montrent le format attendu. Bien comprendre les corrections.

**4. Maîtriser Lyapunov** :
C'est le cœur du cours. Pratiquer la construction de fonctions de Lyapunov sur différents systèmes.

**5. Comprendre les limites** :
Chaque méthode a ses hypothèses et limites. Savoir quand elle s'applique et quand elle échoue.

<h3 class="section-title">Conclusion</h3>

L'analyse des systèmes non linéaires est un domaine fascinant et essentiel pour l'ingénieur automaticien. Les systèmes réels sont presque toujours non linéaires, et savoir analyser leur comportement est crucial.

**Philosophie du cours** :
Passer du monde idéalisé (linéaire) au monde réel (non linéaire). Accepter la complexité et développer des outils pour la maîtriser.

**Compétences transférables** :
- Rigueur mathématique dans l'analyse
- Pensée géométrique (espace d'état, trajectoires)
- Intuition physique (énergie, stabilité)
- Capacité à gérer la complexité

**Message principal** :
Les systèmes non linéaires ne sont pas des versions compliquées de systèmes linéaires. Ils ont leur propre richesse comportementale. Les comprendre ouvre la porte à l'analyse de systèmes réels complexes.

**Recommandations** :
- Approfondir avec des simulations (MATLAB, Python)
- Lire des articles sur applications (robotique, aérospatial)
- Explorer les liens avec la théorie du chaos et systèmes dynamiques
- Se former à la commande non linéaire avancée (backstepping, modes glissants d'ordre supérieur)

**Liens avec les autres cours** :
- [Systèmes multivariables - S7](./systemes-multivariable.html) : représentation d'état, stabilité
- [Commande Numérique - S8](./commande-numerique.html) : implémentation discrète
- [Programmation Orientée Objets C++ - S7](./programmation-orientee-objets-cpp.html) : simulations numériques

---

*Cours suivi en 2023-2024 à l'INSA Toulouse, Département Génie Électrique et Informatique.**Cours suivi en 2023-2024 à l'INSA Toulouse, Département Génie Électrique et Informatique.*

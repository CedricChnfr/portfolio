---
layout: default
title: "Modélisation et Commande des Systèmes à Événements Discrets - S5"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
---

<style>
.back-nav {
  margin-bottom: 20px;
}
.back-nav a {
  text-decoration: none;
  color: #2a7ae2;
  font-weight: 600;
}
.back-nav a:hover {
  text-decoration: underline;
}
.section-title {
  color: #2a7ae2;
  border-bottom: 2px solid #2a7ae2;
  padding-bottom: 10px;
  margin-top: 30px;
  margin-bottom: 20px;
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
    background-color: #2a7ae2;
    color: white;
}
tr:nth-child(even) {
    background-color: #f9f9f9;
}
</style>

<div class="back-nav">
  <a href="./my-courses-2022-2023.html">← Retour à Mes Cours 2022-2023</a>
</div>

# 🔄 Modélisation et Commande des Systèmes à Événements Discrets - S5

**Année**: 2022-2023 (Semestre 5)  
**Crédits**: 2 ECTS  
**Type**: Automatique et Systèmes  
**Enseignant**: Vignolles

---

## PART A: PRÉSENTATION GÉNÉRALE

### Objectifs du cours

Ce cours introduit la modélisation et la commande des systèmes à événements discrets (SED), systèmes dont l'évolution est déclenchée par des événements discrets plutôt que par le temps continu. Ces systèmes sont omniprésents dans l'industrie (lignes de production, systèmes de transport), l'informatique (protocoles, workflows) et la robotique. Le cours couvre les automates finis et les réseaux de Petri, outils fondamentaux pour modéliser, analyser et commander ces systèmes.

### Compétences visées

- Modéliser des systèmes industriels avec automates et réseaux de Petri
- Analyser les propriétés des systèmes (vivacité, blocage, atteignabilité)
- Concevoir des superviseurs pour garantir des spécifications
- Utiliser des logiciels de simulation (AutomDiscrete)
- Implémenter des automates sur automates programmables (grafcet)
- Détecter et résoudre les problèmes de synchronisation et blocages

### Organisation

- **Volume horaire**: 20h (CM: 10h, TD: 6h, TP: 4h)
- **Évaluation**: Examen écrit (70%) + TPs (30%)
- **Semestre**: 5 (2022-2023)
- **Prérequis**: Logique, algèbre de base, notions d'automatique

---

## PART B: EXPÉRIENCE, CONTEXTE ET FONCTION

### Contenu pédagogique

Le cours s'organise autour de deux formalismes complémentaires: les automates et les réseaux de Petri.

#### 1. Systèmes à Événements Discrets

**Caractéristiques principales**:

Les SED évoluent par sauts discrets déclenchés par des événements:
- **États discrets**: nombre fini ou dénombrable d'états
- **Événements**: actions instantanées causant des transitions
- **Évolution asynchrone**: pas de synchronisation globale
- **Non-déterminisme**: plusieurs transitions possibles depuis un état
- **Concurrence**: plusieurs processus simultanés

**Exemples typiques**:
- Système de tri de pièces (TP principal)
- Feux de circulation
- Distributeur automatique
- Ligne de production manufacturière
- Protocole de communication

**Différence avec systèmes continus**:

| Critère | Systèmes continus | Systèmes discrets |
|---------|-------------------|-------------------|
| États | Continus (réels) | Discrets (entiers) |
| Temps | Évolution continue | Événements instantanés |
| Modèle | Équations différentielles | Automates, Petri |
| Exemple | Régulation température | Ligne d'assemblage |

#### 2. Automates à États Finis

**Définition**:

Un automate est défini par:
- E : ensemble d'états
- e0 : état initial
- Σ : alphabet d'événements
- δ : fonction de transition (E × Σ → E)
- Em : états marqués (acceptants)

**Représentation graphique**:

```
    [e1] --a--> [e2] --b--> [e3]
     |                       |
     +----------c------------+
```

États = cercles, transitions = flèches étiquetées, état initial = flèche entrante.

**Exemple TD: Distributeur de boissons**:

États:
- e0 : attente
- e1 : 50 centimes insérés
- e2 : 1 euro inséré
- e3 : boisson servie

Événements:
- p50 : insertion 50 centimes
- p100 : insertion 1 euro
- serv : servir boisson
- annul : annulation

**Déterminisme vs non-déterminisme**:

Automate déterministe: une seule transition possible pour chaque couple (état, événement).
Automate non-déterministe: plusieurs transitions possibles.

**Opérations sur automates**:

**Produit synchrone**: combine deux automates avec synchronisation sur événements communs.

Utilisé pour modéliser des systèmes composés de plusieurs sous-systèmes interagissant.

**Accessibilité**: un état est accessible s'il existe un chemin depuis l'état initial.

**Co-accessibilité**: un état est co-accessible s'il existe un chemin vers un état marqué.

**Trim**: automate ne contenant que les états accessibles et co-accessibles.

#### 3. Réseaux de Petri

**Structure de base**:

Un réseau de Petri comprend:
- Places (cercles): contiennent des jetons
- Transitions (rectangles): événements
- Arcs orientés: places → transitions ou transitions → places
- Marquage M: nombre de jetons dans chaque place

**Règle de tir**:

Une transition est franchissable si toutes les places d'entrée contiennent au moins un jeton.

Après franchissement:
- Retirer un jeton de chaque place d'entrée
- Ajouter un jeton à chaque place de sortie

**Exemple: Producteur-Consommateur**:

```
    (Buffer vide) --produire--> (Buffer plein) --consommer--> (Buffer vide)
```

Places: Buffer vide (1 jeton initial), Buffer plein (0 jeton)
Transitions: produire, consommer

**Propriétés importantes**:

**Bornage**: nombre maximal de jetons dans une place.
- Réseau borné: toutes les places ont un nombre limité de jetons
- Réseau sauf (safe): maximum 1 jeton par place

**Vivacité**: une transition est vivante si elle peut toujours être franchie dans le futur (pas de blocage définitif).

**Réinitialisabilité**: possibilité de revenir au marquage initial.

**Blocage (deadlock)**: marquage où aucune transition n'est franchissable.

**Analyse par graphe de marquages**:

Graphe représentant tous les marquages atteignables et les transitions entre eux.

Permet de:
- Détecter les blocages
- Vérifier la bornage
- Analyser la vivacité
- Calculer les états accessibles

#### 4. Modélisation de Systèmes Industriels

**Système de tri de pièces (TP)**:

Composants:
- Tapis d'entrée (T_ON) et de sortie (C_ON)
- Capteurs: entrée tapis, détection métal, détection autre
- Bacs de sortie: métal (B1), autre (B2), rebut (B)
- Vérins pour diriger les pièces

États du système:
- État 0: attente (tapis arrêtés)
- État 1: démarrage (tapis en marche)
- État 2: pièce détectée (temporisation)
- État 3: identification pièce
- États 4,5,6: tri selon catégorie

**Logique de commande (automate programmable)**:

```
IF (STATE_TRI = 0) THEN
    T_ON := 0;  // Tapis arrêté
    C_ON := 0;
    IF ((P_g1=1) AND (P_g2=1) AND (P_g3=1)) THEN
        STATE_TRI := 1;  // Tous les bacs vides, démarrer
    END_IF;
END_IF;

IF (STATE_TRI = 1) THEN
    T_ON := 1;  // Démarrer tapis
    C_ON := 1;
    IF (Pp_entreeTapis = 1) THEN
        STATE_TRI := 2;  // Pièce détectée
    END_IF;
END_IF;

IF (STATE_TRI = 3) THEN
    IF ((p_autre=1) AND (p_metal=1)) THEN
        STATE_TRI := 5;  // Pièce métallique
    ELSIF (p_autre=1) THEN
        STATE_TRI := 6;  // Autre pièce
    ELSE
        STATE_TRI := 4;  // Rebut
    END_IF;
END_IF;
```

**Temporisations**:

Les timers permettent d'attendre la stabilisation des capteurs:
- Timer1, Timer2, Timer3: temporisations de 2s ou 1s
- Évitent les fausses détections

#### 5. Grafcet et Automates Programmables

**Grafcet (Graphe Fonctionnel de Commande Étape-Transition)**:

Représentation graphique pour automatismes industriels:
- Étapes (carrés numérotés): états du système
- Transitions (traits horizontaux): conditions de passage
- Actions associées aux étapes
- Liaisons orientées

**Règles d'évolution**:
1. Étape initiale active au démarrage
2. Transition franchie si étape amont active ET condition vraie
3. Activation étape aval et désactivation étape amont

**Conversion Grafcet → Automate programmable**:

Le grafcet se traduit directement en code pour API (Automate Programmable Industriel) en langage structuré ou ladder.

#### 6. Synthèse de Superviseurs

**Principe**:

Concevoir un contrôleur (superviseur) qui restreint le comportement du système pour respecter des spécifications.

**Spécifications typiques**:
- Éviter les blocages
- Garantir la sécurité (états interdits)
- Maximiser la productivité
- Respecter des séquences obligatoires

**Événements contrôlables vs non-contrôlables**:

Contrôlables: le superviseur peut empêcher leur occurrence (ex: démarrer machine).
Non-contrôlables: arrivent spontanément (ex: pièce arrivée, panne).

**Méthode**:
1. Modéliser le système (automate ou Petri)
2. Définir les spécifications (états ou comportements interdits)
3. Calculer le superviseur (restreindre les transitions)
4. Vérifier les propriétés (non-blocage, contrôlabilité)

---

## PART C: ASPECTS TECHNIQUES

### Travaux Pratiques

**TP1: Système de tri automatique**

Objectif: modéliser et simuler un système de tri de pièces sur tapis avec le logiciel AutomDiscrete.

**Cahier des charges**:
- Tri de 3 catégories: métal, autre, rebut
- 3 bacs de sortie avec capteurs de niveau
- Capteurs de détection: métal, autre matière
- Temporisations pour stabilisation
- Arrêt automatique si bacs pleins

**Modélisation par automate**:

États du système: 7 états (0 à 6)
- 0: Repos
- 1: Tapis en marche
- 2: Temporisation après détection
- 3: Identification de la pièce
- 4: Tri rebut
- 5: Tri métal
- 6: Tri autre

Événements:
- Bacs vides (P_g1, P_g2, P_g3)
- Pièce entrée tapis
- Fin temporisation
- Détection métal, autre
- Bacs pleins

**Implémentation logiciel AutomDiscrete**:

Outil graphique permettant:
- Dessiner l'automate (états, transitions)
- Définir les événements et actions
- Simuler l'évolution du système
- Exporter en code automate programmable

**Code généré** (extrait):

Variables:
- STATE_TRI: état courant
- T_ON, C_ON: commandes tapis
- B_OFF, B1_ON, B2_ON: commandes vérins
- P1-P6: états internes
- Timers pour temporisations

**Tests et validation**:
- Scénario nominal: tri correct selon catégorie
- Cas limites: bacs pleins, pièces successives rapides
- Gestion erreurs: capteurs défaillants

### Travaux Dirigés

**TD1: Automates de base**

Exercices:
- Modéliser un distributeur de boissons
- Calculer le produit synchrone de deux automates
- Déterminer les états accessibles et co-accessibles
- Minimiser un automate

**TD2: Réseaux de Petri**

Exercices:
- Modéliser un système producteur-consommateur
- Calculer le graphe de marquages
- Analyser la vivacité et le bornage
- Détecter les blocages potentiels

**TD: Système manufacturier**

Modélisation d'une cellule flexible avec:
- Machines en parallèle
- Buffers limités
- Ressources partagées (robot)
- Analyse des deadlocks

### Outils Logiciels

**AutomDiscrete**:
- Éditeur graphique d'automates
- Simulation pas à pas
- Export en grafcet et code API
- Version utilisée: v4.0

**Autres outils**:
- PIPE: éditeur de réseaux de Petri
- TINA: analyse de Petri temporisés
- Supremica: synthèse de superviseurs
- Stateflow (Simulink): automates dans MATLAB

### Méthodologie de Conception

**Étapes pour modéliser un système**:

1. **Identifier les états**: situations distinctes du système
2. **Lister les événements**: actions déclenchant changements
3. **Définir les transitions**: conditions de passage entre états
4. **Spécifier les actions**: sorties associées aux états ou transitions
5. **Valider**: simulation et vérification propriétés

**Choix entre automates et Petri**:

Utiliser automates si:
- Système avec états bien définis
- Séquences d'événements linéaires
- Peu de concurrence

Utiliser réseaux de Petri si:
- Forte concurrence entre processus
- Ressources partagées
- Synchronisations complexes
- Systèmes distribués

---

## PART D: ANALYSE ET RÉFLEXION

### Compétences acquises

**Modélisation**:
- Capacité à abstraire un système réel en modèle formel
- Choix du formalisme adapté (automate vs Petri)
- Représentation graphique claire et structurée

**Analyse**:
- Détection de blocages et situations dangereuses
- Vérification de propriétés (vivacité, bornage)
- Évaluation de performances (temps de cycle)

**Conception**:
- Synthèse de lois de commande garantissant spécifications
- Implémentation sur automates programmables
- Tests et validation de systèmes automatisés

### Applications pratiques

Les SED sont omniprésents dans l'industrie et l'informatique:

**Industrie manufacturière**:
- Lignes d'assemblage automobile
- Systèmes de tri postal
- Chaînes de conditionnement alimentaire
- Ateliers flexibles

**Transport et logistique**:
- Contrôle de feux de circulation
- Gestion de flottes de véhicules
- Systèmes de métro automatique
- Entrepôts automatisés

**Informatique**:
- Protocoles réseau (TCP/IP)
- Workflows d'entreprise
- Systèmes d'exploitation (ordonnancement)
- Applications réactives

**Robotique**:
- Coordination multi-robots
- Tâches séquentielles complexes
- Interaction avec environnement

### Liens avec autres cours

| Cours | Semestre | Lien avec SED |
|-------|----------|---------------|
| Logique Séquentielle | S5 | Machines d'états, FSM |
| Systèmes Bouclés | S5 | Automatique, commande |
| Programmation Orientée Objet | S7 | Patterns état (State pattern) |
| Temps Réel | S8 | Ordonnancement, synchronisation |
| Réseaux de Pétri | S8 | Approfondissement Petri |

### Perspectives et extensions

**Systèmes hybrides**:
Combinaison de dynamique continue (équations différentielles) et événements discrets.
Exemple: thermostat (température continue, chauffage on/off).

**Diagnostic et supervision**:
Utilisation d'automates observateurs pour détecter pannes et anomalies.

**Optimisation**:
Minimisation temps de cycle, maximisation throughput avec Petri temporisés.

**Vérification formelle**:
Model checking pour prouver l'absence de bugs dans protocoles et systèmes critiques.

### Recommandations

**Pour réussir le cours**:
1. Bien comprendre la différence états/événements
2. Pratiquer la modélisation graphique (dessiner les automates)
3. Tester systématiquement avec simulation
4. Analyser les cas limites (bacs pleins, erreurs capteurs)

**Ressources complémentaires**:
- Cassandras & Lafortune: "Introduction to Discrete Event Systems"
- David & Alla: "Réseaux de Petri et Grafcet"
- Cours en ligne sur automates finis (théorie des langages)

### Mon opinion

Ce cours offre une perspective différente de l'automatique classique (systèmes continus). Il est particulièrement utile pour comprendre les systèmes industriels réels où la notion d'événements discrets est naturelle.

**Points forts**:
- Approche graphique intuitive (automates, Petri)
- Applications concrètes immédiates (industrie)
- Outils logiciels facilitant la modélisation
- Lien direct avec automates programmables

**Complémentarité**:
Les SED complètent parfaitement les cours de systèmes continus. Dans la réalité, beaucoup de systèmes sont hybrides (ex: robot avec contrôle position continue + séquences de tâches discrètes).

**Importance professionnelle**:
Compétences très recherchées dans l'automatisation industrielle, la robotique, et les systèmes embarqués. Les grafcets sont le langage standard des automaticiens.

**Applications futures**:
Ces concepts se retrouvent dans les cours de S8 (Temps Réel, Réseaux de Pétri avancés) et dans les projets industriels (automatisation, supervision).

---

**Bilan personnel**: Ce cours a apporté une vision complémentaire de l'automatique, centrée sur les événements plutôt que le temps. La modélisation par automates et réseaux de Petri est intuitive et directement applicable aux systèmes industriels. Le TP sur le système de tri a permis de concrétiser ces concepts avec un cas réel d'automatisation.

---

<style>
        body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                color: #333;
                line-height: 1.6;
        }
        h2, h3, h4, h5 {
                color: #2a7ae2;
        }
        p {
                text-align: justify;
        }
        code {
                background-color: #f5f5f5;
                padding: 2px 6px;
                border-radius: 3px;
                font-family: 'Courier New', monospace;
        }
        pre {
                background-color: #f5f5f5;
                padding: 15px;
                border-radius: 5px;
                overflow-x: auto;
        }
</style>

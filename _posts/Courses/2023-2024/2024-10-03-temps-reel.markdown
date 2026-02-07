---
layout: default
title: "Temps Réel - S8"
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
.back-nav a {
    color: #007BFF;
    text-decoration: none;
    font-weight: bold;
}
.back-nav a:hover {
    text-decoration: underline;
}
</style>

<div class="back-nav">
    <a href="./my-courses-2023-2024.html">&larr; Retour aux Cours 2023-2024</a>
</div>

**🔗 Cours connexes**: 
- [Commande Numérique - S8](./2024-10-03-commande-numerique.html) - Lois de commande numériques
- [Réseaux de Pétri - S8](./2024-10-03-reseaux-petri.html) - Modélisation des systèmes temps réel

---

# Temps Réel

## PART A: GENERALITIES

### Presentation
Le cours "Temps Réel" traite des systèmes informatiques devant réagir à des événements externes dans des contraintes temporelles strictes. Un système temps réel ne doit pas seulement produire des résultats corrects, mais aussi les produire à temps. Ces systèmes sont omniprésents: avionique, automobile, robotique, contrôle industriel, télécommunications. Le cours couvre l'ordonnancement de tâches, les systèmes d'exploitation temps réel (RTOS), et les techniques de conception garantissant le respect des échéances.

**Année Académique**: 2023-2024  
**Semestre**: 8  
**Catégorie**: Informatique / Systèmes Embarqués

---

## PART B: DESCRIPTIVE PART

### Experience Details

#### Environment and Context
Le cours combinait théorie de l'ordonnancement avec implémentation pratique sur microcontrôleurs et RTOS (FreeRTOS, RTOS embarqués). Nous avons programmé des systèmes multitâches avec contraintes temporelles, analysé leur ordonnançabilité, et mesuré les performances réelles. Les projets incluaient des applications concrètes: acquisition de données périodique, contrôle moteur, communication temps réel.

#### My Function
Dans ce cours, j'ai été responsable de:
- Comprendre les contraintes temporelles (échéances, périodes, gigue)
- Analyser l'ordonnançabilité de systèmes de tâches
- Implémenter des applications multitâches sur RTOS
- Gérer les ressources partagées (mutex, sémaphores)
- Éviter interblocages et inversions de priorité
- Mesurer et valider les performances temporelles
- Concevoir des systèmes garantissant le respect des échéances

## PART C: TECHNICAL PART

Cette section explore les aspects techniques des systèmes temps réel.

### Technical Concepts Learned

#### 1. Définitions et Classifications

**Système Temps Réel**:
Système dont la correction dépend non seulement du résultat logique mais aussi du moment où il est produit.

**Classification**:

**Temps Réel Dur (Hard Real-Time)**:
Échéance manquée = catastrophe (crash, perte, danger).
Exemples: airbag, pilote automatique d'avion, pacemaker.

**Temps Réel Mou (Soft Real-Time)**:
Échéance manquée = dégradation de qualité (acceptable occasionnellement).
Exemples: streaming vidéo, jeux vidéo, interface utilisateur.

**Temps Réel Ferme (Firm Real-Time)**:
Échéance manquée = résultat inutile mais pas dangereux.
Exemples: certains capteurs (échantillon perdu acceptable).

#### 2. Modèle de Tâches Périodiques

**Tâche τᵢ** caractérisée par:
- **Cᵢ**: temps d'exécution pire cas (WCET)
- **Tᵢ**: période (intervalle entre activations)
- **Dᵢ**: échéance relative (deadline)
- **Pᵢ**: priorité

**Tâches périodiques**:
Activées à t=0, Tᵢ, 2Tᵢ, 3Tᵢ, ...

**Contrainte**:
Terminer avant échéance: tᵢ + Dᵢ (souvent Dᵢ = Tᵢ)

**Facteur d'utilisation**:
```
U = Σ Cᵢ/Tᵢ
```

Proportion du processeur utilisée.

**Condition nécessaire d'ordonnançabilité**:
```
U ≤ 1
```

Si U > 1, impossible de respecter toutes les échéances.

#### 3. Ordonnancement à Priorités Fixes

**Rate Monotonic (RM)**:
Priorité inversement proportionnelle à la période.
Période courte → priorité haute.

**Test d'ordonnançabilité (Liu & Layland)**:
```
Si U ≤ n(2^(1/n) - 1) alors ordonnançable par RM
```

Pour n→∞: U ≤ ln(2) ≈ 0.69

Condition suffisante (pas nécessaire).

**Test exact** (analyse du temps de réponse):
Pour chaque tâche τᵢ, calculer temps de réponse Rᵢ:
```
Rᵢ = Cᵢ + Σⱼ₍ₚᵣᵢₒ>ₚᵣᵢₒᵢ₎ ⌈Rᵢ/Tⱼ⌉ × Cⱼ
```

Résolution itérative.

Ordonnançable si Rᵢ ≤ Dᵢ pour tout i.

**Deadline Monotonic (DM)**:
Si Dᵢ ≠ Tᵢ, priorité selon échéance.
Échéance courte → priorité haute.

Optimal pour priorités fixes avec Dᵢ ≤ Tᵢ.

#### 4. Ordonnancement à Priorités Dynamiques

**Earliest Deadline First (EDF)**:
À chaque instant, exécuter tâche avec échéance absolue la plus proche.

**Optimalité**:
EDF est optimal pour monoprocesseur.
Si un algorithme peut ordonnancer un système, EDF le peut.

**Test d'ordonnançabilité**:
```
U ≤ 1
```

Condition nécessaire ET suffisante pour EDF avec Dᵢ = Tᵢ.

**Avantages**:
- Meilleure utilisation processeur (jusqu'à 100%)
- Optimal

**Inconvénients**:
- Overhead (changements de contexte fréquents)
- Comportement moins prédictible en surcharge
- Implémentation plus complexe

#### 5. Tâches Apériodiques et Sporadiques

**Tâches apériodiques**:
Activations irrégulières, souvent sans échéance stricte.

**Tâches sporadiques**:
Activations irrégulières avec intervalle minimum et échéance.

**Serveurs**:
Mécanismes pour intégrer tâches apériodiques dans système périodique.

**Polling Server**:
Tâche périodique réservée pour apériodiques.

**Deferrable Server**:
Capacité préservée si pas utilisée.

**Sporadic Server**:
Compromis performance/simplicité.

#### 6. Synchronisation et Ressources Partagées

**Problème**:
Tâches partagent ressources (variables, périphériques).
Accès concurrent → corruption données.

**Section critique**:
Portion de code accédant ressource partagée.

**Mécanismes**:

**Mutex** (Mutual Exclusion):
Lock/Unlock pour protéger section critique.

**Sémaphore**:
Compteur contrôlant accès.
- Binaire (0 ou 1): comme mutex
- Comptant: plusieurs accès simultanés (pool de ressources)

**Inversion de priorité**:
Tâche haute priorité bloquée par tâche basse priorité.

**Exemple classique (Mars Pathfinder)**:
Tâche priorité haute bloquée indéfiniment → reset système.

**Solutions**:

**Priority Inheritance Protocol (PIP)**:
Tâche tenant ressource hérite temporairement priorité de tâche bloquée la plus haute.

**Priority Ceiling Protocol (PCP)**:
Ressource a priorité plafond = max des priorités des tâches l'utilisant.
Tâche accédant à ressource acquiert temporairement cette priorité.

Évite inversions de priorité multiples et interblocages.

#### 7. Interblocages (Deadlocks)

**Conditions de Coffman** (4 nécessaires):
1. **Exclusion mutuelle**: ressources non partageables
2. **Hold and wait**: tâche tient ressources et en attend d'autres
3. **Pas de préemption**: ressources non préemptibles
4. **Attente circulaire**: cycle dans graphe d'allocation

**Prévention**:
Casser une des 4 conditions.

**Exemple**: ordre total d'acquisition des ressources (évite cycles).

**Détection et récupération**:
Détecter cycles, puis tuer/redémarrer tâches.
Coûteux en temps réel.

**Évitement** (algorithme du banquier):
N'allouer que si état sûr garanti.
Overhead élevé, peu utilisé en temps réel.

#### 8. Systèmes d'Exploitation Temps Réel (RTOS)

**Caractéristiques**:
- **Déterminisme**: comportement temporel prévisible
- **Latence d'interruption** faible et bornée
- **Préemptibilité**: tâche haute priorité peut interrompre basse
- **Ordonnancement** prioritaire (souvent priorités fixes)
- **Primitives de synchronisation** (mutex, sémaphores)
- **Gestion mémoire** déterministe (pas de garbage collector imprévisible)

**RTOS populaires**:

**FreeRTOS**:
- Open source
- Léger (quelques Ko)
- Portable (nombreux microcontrôleurs)
- API simple
- Ordonnancement préemptif à priorités fixes

**VxWorks**:
- Commercial (Wind River)
- Robuste, certifié (aérospatial, médical)
- Riche en fonctionnalités

**QNX**:
- Microkernel
- POSIX compliant
- Automobile (BlackBerry)

**RT-Linux / Xenomai**:
- Extension temps réel de Linux
- Cohabitation tâches temps réel / non temps réel

**Zephyr**:
- Open source, moderne
- IoT et objets connectés

#### 9. API FreeRTOS (Exemples)

**Création de tâche**:
```c
xTaskCreate(
    vTaskFunction,      // Pointeur fonction
    "TaskName",         // Nom (debug)
    STACK_SIZE,         // Taille stack
    NULL,               // Paramètres
    PRIORITY,           // Priorité
    &xTaskHandle        // Handle (optionnel)
);
```

**Mutex**:
```c
xMutex = xSemaphoreCreateMutex();

xSemaphoreTake(xMutex, portMAX_DELAY);  // Lock
// Section critique
xSemaphoreGive(xMutex);  // Unlock
```

**Sémaphore binaire** (signalisation):
```c
xSemaphore = xSemaphoreCreateBinary();

// ISR:
xSemaphoreGiveFromISR(xSemaphore, NULL);

// Tâche:
xSemaphoreTake(xSemaphore, portMAX_DELAY);  // Attend signal
```

**Queues** (files FIFO):
```c
xQueue = xQueueCreate(QUEUE_LENGTH, sizeof(DataType));

xQueueSend(xQueue, &data, TIMEOUT);
xQueueReceive(xQueue, &buffer, TIMEOUT);
```

**Délais**:
```c
vTaskDelay(pdMS_TO_TICKS(100));  // Délai 100ms
```

#### 10. Mesure et Validation

**WCET** (Worst-Case Execution Time):
Temps d'exécution maximum.

**Méthodes de détermination**:
- **Mesure**: instrumenter code, tester scénarios
- **Analyse statique**: analyser code, modèle processeur
- **Hybride**: combiner les deux

Difficile à déterminer précisément (caches, pipelines, branchements).

**Marges de sécurité**:
Utiliser WCET majoré pour robustesse.

**Outils de mesure**:
- Oscilloscope logique
- Traceurs temps réel
- GPIO toggling (observer signaux)
- Compteurs hardware

**Validation**:
- Tests de stress (charge max)
- Injection de fautes
- Tests de longue durée (vieillissement)

#### 11. Conception de Systèmes Temps Réel

**Méthodologie**:

**1. Spécification**:
- Identifier tâches et contraintes temporelles
- Périodes, échéances, priorités

**2. Modélisation**:
- Diagrammes de séquence
- Diagrammes d'états
- Réseaux de Pétri temporisés

**3. Analyse d'ordonnançabilité**:
- Calculer U
- Tests RM/EDF
- Analyse temps de réponse

**4. Implémentation**:
- Choix RTOS
- Codage tâches
- Synchronisation

**5. Validation**:
- Tests unitaires
- Tests d'intégration
- Mesures temporelles

**6. Optimisation**:
- Réduire WCET (code, compilateur)
- Ajuster priorités
- Répartir charges

**Patterns de conception**:
- **Cyclic Executive**: boucle infinie avec ordonnancement statique (simple mais peu flexible)
- **Time-Triggered**: activation sur timer (déterministe)
- **Event-Triggered**: activation sur événements (réactif mais moins prédictible)

#### 12. Défis et Bonnes Pratiques

**Défis**:

**Jitter**:
Variation du délai (problématique pour contrôle, audio).
Minimiser par ordonnancement approprié.

**Overhead**:
Changements de contexte, gestion RTOS.
Peut être significatif (10-20%).

**Multiprocesseur**:
Ordonnancement plus complexe.
Partitionnement de tâches ou migration.

**Interruptions**:
Peuvent perturber ordonnancement.
Limiter durée ISR (Interrupt Service Routine).

**Bonnes pratiques**:

**ISR courtes**:
Minimiser traitement en interruption.
Utiliser sémaphore pour débloquer tâche (traitement différé).

**Sections critiques courtes**:
Minimiser temps mutex tenu.

**Éviter opérations bloquantes**:
Pas d'I/O bloquants, pas de malloc (temps variable).

**Utiliser ressources déterministes**:
Allocation statique mémoire, buffers circulaires.

**Dimensionnement conservateur**:
Marges sur WCET, utilisation processeur.

**Tests exhaustifs**:
Valider tous scénarios, conditions limites.

## PART D: ANALYTICAL PART

### Knowledge and Skills Mobilized

- Théorie de l'ordonnancement
- Analyse d'ordonnançabilité (RM, EDF)
- Programmation système embarqué
- Utilisation de RTOS (FreeRTOS)
- Synchronisation et gestion ressources partagées
- Résolution problèmes d'interblocage et inversion de priorité
- Mesure et validation temporelle
- Conception de systèmes avec contraintes temps réel

### Self Evaluation

Ce cours a été exigeant mais passionnant. Les systèmes temps réel introduisent une dimension (le temps) qui change radicalement la conception par rapport à la programmation classique.

La théorie de l'ordonnancement est mathématiquement rigoureuse. Les tests d'ordonnançabilité (RM, EDF) fournissent des garanties formelles, ce qui est rassurant pour systèmes critiques. Cependant, déterminer le WCET précisément reste un défi.

Le fossé entre RM (simple, utilisé en pratique) et EDF (optimal mais complexe) est intéressant. Le choix dépend du contexte: critique (RM pour prédictibilité) ou haute performance (EDF pour utilisation maximale).

La programmation avec RTOS a été révélatrice. Gérer tâches concurrentes, synchronisation, priorités demande rigueur. Les bugs sont souvent subtils (race conditions, deadlocks) et difficiles à reproduire.

L'inversion de priorité et ses solutions (PIP, PCP) montrent l'importance de comprendre les mécanismes profonds. Un simple mutex mal utilisé peut causer blocages catastrophiques (cf. Mars Pathfinder).

Les mesures temporelles m'ont confronté à la réalité: le WCET théorique et mesuré peuvent différer. Les facteurs matériels (caches, interruptions) compliquent les prédictions.

La conception d'un système temps réel nécessite approche méthodique: spécification claire, analyse formelle, tests exhaustifs. L'improvisation est dangereuse.

### My Opinion

Ce cours est indispensable pour ingénieurs en systèmes embarqués, automatique, ou développant applications critiques.

Points forts:
- Théorie solide (ordonnancement)
- Pratique sur RTOS réels (FreeRTOS)
- Conscience des pièges (inversions priorité, deadlocks)
- Applications concrètes

Points à améliorer:
- Plus sur multiprocesseurs (multi-core omniprésents)
- Outils d'analyse statique de WCET
- Certification (DO-178C aérospatial, ISO 26262 automobile)
- Temps réel distribué (réseaux, synchronisation)

Réflexions personnelles:

Le temps réel n'est pas "faire vite" mais "faire à temps". Un système rapide en moyenne mais avec variation importante peut être pire qu'un système plus lent mais déterministe.

La garantie d'échéance est plus importante que la performance moyenne. C'est un changement de mentalité par rapport au développement logiciel classique (où on optimise le cas moyen).

Les systèmes temps réel sont omniprésents mais invisibles: ABS dans voitures, pilotes automatiques, contrôleurs industriels, pacemakers. Leur fiabilité est critique car des vies en dépendent.

La certification (aérospatial, médical, automobile) impose processus rigoureux et traçabilité. Le code doit être prouvé correct, pas juste testé. Les méthodes formelles deviennent essentielles.

La complexité croît avec:
- Multiprocesseurs (partitionnement, communication)
- Systèmes distribués (horloges, latences réseau)
- Intelligence embarquée (IA temps réel)

Applications professionnelles:

Compétences temps réel applicables dans:
- **Automobile**: ESP, ABS, ADAS, véhicules autonomes
- **Aérospatial**: contrôle vol, navigation
- **Industrie**: automates, robots, supervision
- **Médical**: dispositifs implantés, imagerie temps réel
- **Télécoms**: stations de base 5G
- **Multimédia**: codecs vidéo, mixage audio
- **Défense**: systèmes d'armes, drones

Le marché des systèmes embarqués et temps réel est énorme et croissant (IoT, voitures connectées, Industry 4.0).

L'avenir:

- **IA embarquée**: inférence réseau neuronal avec contraintes temps réel
- **Edge computing**: traitement local temps réel (vs cloud)
- **Systèmes cyber-physiques**: intégration software/hardware/physique
- **Sécurité**: temps réel + cybersécurité (défis combinés)

Les compétences en temps réel resteront critiques. Même avec processeurs plus rapides, les applications deviennent plus complexes et exigeantes.

En conclusion, ce cours sur les systèmes temps réel fournit les bases essentielles pour concevoir des systèmes embarqués fiables respectant des contraintes temporelles strictes. C'est un domaine exigeant, combinant théorie (ordonnancement) et pratique (RTOS, Xenomai), crucial dans de nombreux secteurs industriels.

---

## Rapports et Projets

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Rapport de Projet Temps Reel</h4>
      <p>Rapport du projet temps reel : conception et implementation d'un systeme multitaches avec contraintes temporelles strictes, ordonnancement et synchronisation.</p>
      <p style="text-align: center;">
        <a href="/file/reports/S8/Rapport_de_projet_temps_réel_FISA_Paris_Chanfreau.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Telecharger le rapport PDF
        </a>
      </p>
    </div>
  </div>
</div>

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
      <h4>📖 Polycopié Xenomai</h4>
      <p>Guide complet sur Xenomai : installation, APIs temps réel, tâches périodiques, synchronisation et débogage.</p>
      <embed src="/cours-pdf/S8/Temps-Reel/polycopie-xenomai.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S8/Temps-Reel/polycopie-xenomai.pdf" target="_blank">📥 Télécharger</a></p>
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

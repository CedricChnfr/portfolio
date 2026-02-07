---
layout: default
title: "Modélisation et Commande des Systèmes Linéaires Continus - S5"
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

# 🎚️ Modélisation et Commande des Systèmes Linéaires Continus - S5

**Année**: 2022-2023 (Semestre 5)  
**Crédits**: 3 ECTS  
**Type**: Automatique et Systèmes  
**Enseignant**: Subias

---

## PART A: PRÉSENTATION GÉNÉRALE

### Objectifs du cours

Ce cours approfondit la commande des systèmes linéaires continus avec une approche complémentaire au cours de représentation d'état. Il se concentre sur les techniques de commande classiques (PID, correcteurs fréquentiels) et leur application pratique sur des systèmes réels. Le cours couvre la modélisation de systèmes physiques, l'analyse de stabilité et de performances, ainsi que la conception de lois de commande adaptées.

### Compétences visées

- Modéliser des systèmes physiques continus (mécaniques, électriques, thermiques)
- Concevoir et régler des correcteurs PID pour des applications industrielles
- Analyser la stabilité par méthodes fréquentielles (Bode, Nyquist)
- Dimensionner des compensateurs (avance, retard de phase)
- Utiliser MATLAB/Simulink pour la simulation et l'analyse
- Évaluer les performances temporelles et fréquentielles
- Implémenter des lois de commande sur systèmes réels

### Organisation

- **Volume horaire**: Cours magistraux, TD et TP MATLAB/Simulink
- **Évaluation**: Examen écrit, TPs notés, Projet robot
- **Semestre**: 5 (2022-2023)
- **Prérequis**: Transformée de Laplace, systèmes du 1er et 2nd ordre, algèbre

---

## PART B: EXPÉRIENCE, CONTEXTE ET FONCTION

### Contenu pédagogique

Le cours se structure autour de la modélisation, l'analyse et la commande de systèmes continus.

#### 1. Modélisation de Systèmes Physiques

**Systèmes mécaniques**:

Système masse-ressort-amortisseur:
- m : masse
- k : raideur du ressort
- f : coefficient d'amortissement

Équation: m × d²x/dt² + f × dx/dt + k × x = F(t)

Fonction de transfert: H(s) = 1 / (m×s² + f×s + k)

**Systèmes électriques (circuit RLC)**:

Équation: L × d²i/dt² + R × di/dt + i/C = dV/dt

Similitude avec système mécanique (L ↔ m, R ↔ f, 1/C ↔ k).

**Moteur à courant continu**:

Modèle simplifié du TP:
- Constante de temps: Tm = 0.3s
- Gain: Km = 47.8
- Fonction de transfert: H(s) = Km / (Tm×s + 1)

#### 2. Analyse Temporelle

**Réponse indicielle d'un système du 2nd ordre**:

Paramètres caractéristiques:
- Temps de montée (rise time)
- Dépassement (overshoot): D = exp(-π×ζ / sqrt(1-ζ²))
- Temps de réponse à 5% (settling time)
- Erreur statique

Pour un système bien amorti: ζ = 0.7 donne D ≈ 5%.

**Classe d'un système**:

Détermine l'erreur statique selon le type d'entrée:
- Classe 0: erreur pour échelon
- Classe 1: erreur pour rampe
- Classe 2: erreur pour parabole

#### 3. Analyse Fréquentielle

**Diagrammes de Bode (TP1)**:

Représentation du gain et de la phase en fonction de la fréquence.

Système identifié expérimentalement: H(s) = 0.717 / (0.0033×s + 1)

Mesures réalisées:
- Fréquences: 0.05 Hz à 10 Hz
- Gain: de -3.5 dB à -24 dB
- Phase: de -2.2° à -90°

**Marges de stabilité (TP2)**:

**Marge de gain (Gm)**: gain supplémentaire avant instabilité.

**Marge de phase (Pm)**: phase supplémentaire avant instabilité.

Critères de robustesse:
- Pm > 45° : bon amortissement
- Gm > 6 dB : bonne marge

Commande MATLAB:
```matlab
[Gm, Pm, Wcg, Wcp] = margin(sys);
```

Résultats typiques du TP: Pm ≈ 60° (système robuste).

**Diagramme de Nyquist**:

Tracé de H(jω) dans le plan complexe.

Critère de Nyquist: nombre d'encerclements du point critique (-1, 0) détermine la stabilité.

#### 4. Commande PID

**Structure du PID**:

Correcteur Proportionnel-Intégral-Dérivé:

u(t) = Kp × e(t) + Ki × ∫e(t)dt + Kd × de(t)/dt

En transfert: C(s) = Kp + Ki/s + Kd×s

**Actions du PID**:

| Action | Effet | Utilisation |
|--------|-------|-------------|
| P (Proportionnel) | Réduit l'erreur, augmente rapidité | Toujours présent |
| I (Intégral) | Annule erreur statique | Erreur permanente |
| D (Dérivé) | Réduit dépassement, améliore stabilité | Systèmes oscillants |

**Réglage par Ziegler-Nichols**:

Méthode empirique pour déterminer Kp, Ki, Kd:
1. Mettre Ki = 0, Kd = 0
2. Augmenter Kp jusqu'à oscillations (Kp critique)
3. Mesurer période d'oscillation Tu
4. Appliquer les formules de réglage

Pour PID: Kp = 0.6×Kpcritique, Ti = 0.5×Tu, Td = 0.125×Tu.

**Limitation anti-windup**:

Problème: l'intégrale continue à s'accumuler même si la commande sature.

Solution: limiter l'intégrateur quand la sortie sature.

#### 5. Correcteurs Fréquentiels

**Correcteur à avance de phase**:

Forme: C(s) = K × (1 + a×T×s) / (1 + T×s) avec a > 1

Effet: augmente la marge de phase, améliore rapidité.

Utilisé quand: système trop lent ou marge de phase insuffisante.

**Correcteur à retard de phase**:

Forme: C(s) = K × (1 + T×s) / (1 + a×T×s) avec a > 1

Effet: augmente la marge de gain, réduit erreur statique.

Utilisé quand: erreur statique trop importante.

**Correcteur avance-retard**:

Combinaison des deux pour améliorer simultanément rapidité et précision.

#### 6. Projet Robot Auto-Équilibré

**Système du pendule inversé**:

Modélisation du robot NXT Way (Lego Mindstorms):

Paramètres physiques:
- Masse roues: m = 0.03 kg
- Rayon roues: R = 0.042 m
- Masse corps: M = 0.67 kg
- Hauteur: H = 0.152 m
- Gravité: g = 9.81 m/s²

**Objectif**: maintenir le robot en équilibre vertical (angle θ = 0°).

**Stratégie de commande**:

Système instable en boucle ouverte → nécessite commande active.

Approches possibles:
- Retour d'état (placement de pôles)
- Correcteur PID sur l'angle
- Observateur pour estimer vitesse angulaire

**Simulation Simulink**:

Fichiers du projet:
- NXTwaySim.slx: modèle complet du robot
- NXP_robot_parameters.m: paramètres physiques
- PlayAnimation.m: visualisation 3D

Tests effectués:
- Stabilisation après perturbation
- Robustesse aux variations de paramètres
- Rejection de perturbations externes

---

## PART C: ASPECTS TECHNIQUES

### Travaux Pratiques MATLAB

**TP1: Identification expérimentale**:

Objectif: déterminer la fonction de transfert d'un système réel à partir de mesures fréquentielles.

Données mesurées (gains et phases à différentes fréquences):
```matlab
freq = [0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 7.5, 10];
G = [0.669, 0.659, 0.609, 0.528, 0.396, 0.242, 0.119, 0.083, 0.061];
```

Tracé du diagramme de Bode:
```matlab
G_dB = 20*log10(G);
semilogx(freq, G_dB);
xlabel('Fréquence (Hz)');
ylabel('Gain (dB)');
```

Modèle identifié: système du 1er ordre avec gain 0.717 et constante de temps 3.3 ms.

**TP2: Analyse de stabilité**:

Système en boucle fermée avec capteur et moteur:
```matlab
Ks = 1.55;   % Gain capteur
Km = 47.8;   % Gain moteur
Tm = 0.3;    % Constante de temps

num = [Km*K/9];
den = [Tm, 1, Km*K*Ks/9];
sys = tf(num, den);

[Gm, Pm, Wcg, Wcp] = margin(sys);
```

Analyse des pôles:
```matlab
P = pole(sys);
```

Si partie réelle négative → système stable.

**TP3: Commande par retour d'état**:

Système d'ordre 2:
```matlab
A = [0 1; -10 -6.316];
B = [0; 1];
C = [k/0.1001 0];

% Placement de pôles
poles_desired = [-2+2i, -2-2i];
K = place(A, B, poles_desired);

% Simulation
sys_cl = ss(A-B*K, B, C, 0);
step(sys_cl);
```

Choix des pôles selon performances souhaitées:
- Partie réelle: rapidité
- Partie imaginaire: oscillations

### Outils MATLAB Essentiels

**Création de modèles**:
```matlab
sys = tf(num, den);        % Fonction de transfert
sys = ss(A, B, C, D);      % Représentation d'état
```

**Analyse**:
```matlab
pole(sys);                 % Pôles
zero(sys);                 % Zéros
step(sys);                 % Réponse indicielle
bode(sys);                 % Diagramme de Bode
nyquist(sys);              % Diagramme de Nyquist
margin(sys);               % Marges de stabilité
```

**Conception**:
```matlab
K = place(A, B, poles);    % Placement de pôles
pidtune(sys, 'PID');       % Réglage PID automatique
```

### Méthodologie de Conception

**Étapes de conception d'un asservissement**:

1. **Modélisation**: obtenir H(s) du système
2. **Analyse BO**: stabilité, performances en boucle ouverte
3. **Spécifications**: définir dépassement, temps de réponse, erreur admissible
4. **Choix correcteur**: PID, avance/retard selon besoins
5. **Réglage**: calcul des paramètres (Kp, Ki, Kd)
6. **Simulation**: validation avec Simulink
7. **Tests**: robustesse, perturbations, variations paramètres

**Compromis à gérer**:
- Rapidité vs stabilité
- Précision vs robustesse
- Complexité vs performances

---

## PART D: ANALYSE ET RÉFLEXION

### Compétences acquises

**Modélisation**:
- Passage du système physique au modèle mathématique
- Identification expérimentale de paramètres
- Validation par comparaison mesures/simulation

**Analyse**:
- Stabilité par Routh, Bode, Nyquist
- Performances temporelles et fréquentielles
- Évaluation de robustesse (marges)

**Commande**:
- Conception de correcteurs PID
- Réglage par méthodes empiriques et théoriques
- Placement de pôles pour spécifications données

**Outils**:
- Maîtrise de MATLAB/Simulink
- Interprétation de diagrammes (Bode, Nyquist)
- Simulation et validation

### Applications pratiques

Les techniques de ce cours s'appliquent à de nombreux domaines:

**Industrie**:
- Régulation de température, pression, débit
- Contrôle de vitesse de moteurs
- Positionnement de systèmes mécaniques

**Robotique**:
- Stabilisation (pendule inversé, robot équilibré)
- Suivi de trajectoire
- Contrôle de force

**Aéronautique**:
- Pilote automatique
- Stabilisation d'attitude
- Contrôle de vol

**Automobile**:
- Régulateur de vitesse (cruise control)
- Suspension active
- Contrôle de moteur

### Liens avec autres cours

| Cours | Lien |
|-------|------|
| Circuits et Filtres Analogiques (S5) | Analyse fréquentielle, Bode |
| Modélisation Systèmes Linéaires (S5) | Représentation d'état |
| Systèmes Bouclés (S5) | Asservissements |
| Commande Numérique (S8) | Discrétisation, PID numérique |
| Temps Réel (S8) | Implémentation des lois de commande |

### Mon opinion

Ce cours est complémentaire au cours de représentation d'état en apportant les outils classiques de l'automatique industrielle.

**Points forts**:
- Approche très pratique (PID, réglages empiriques)
- Outils directement utilisables en industrie
- TPs concrets avec identification et commande
- Projet robot motivant et formateur

**Complémentarité**:
Le PID reste le correcteur le plus utilisé industriellement (>90% des boucles de régulation). La représentation d'état apporte la théorie moderne, le PID apporte la pratique immédiate.

**Importance professionnelle**:
Compétences très recherchées dans l'automatisation industrielle, la robotique et les systèmes embarqués. Le réglage de PID est une compétence de base pour tout ingénieur en automatique.

---

**Bilan personnel**: Ce cours a apporté les techniques classiques et éprouvées de l'automatique. La complémentarité avec l'approche moderne (état) offre une boîte à outils complète. Les TPs MATLAB et le projet robot ont permis d'appliquer concrètement ces concepts sur des systèmes réels, préparant bien aux applications industrielles.

---

## Rapports et Projets

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Compte Rendu TP1 - Identification et Analyse Fréquentielle</h4>
      <p>Rapport de TP sur l'identification expérimentale de systèmes, tracé de diagrammes de Bode et analyse de stabilité avec MATLAB.</p>
      <p style="text-align: center;">
        <a href="/file/reports/S5/CHANFREAU_JUMIN_Compte_rendu_TP1.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Télécharger le rapport PDF
        </a>
      </p>
    </div>
    <div class="pdf-item">
      <h4>Compte Rendu TP3 - Commande par Retour d'État</h4>
      <p>Rapport de TP sur la commande de systèmes linéaires continus : placement de pôles, simulation Simulink et validation expérimentale.</p>
      <p style="text-align: center;">
        <a href="/file/reports/S5/Compte_Rendu_TP3_Commande_JUMIN_CHANFREAU.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          Télécharger le rapport PDF
        </a>
      </p>
    </div>
  </div>
</div>

---

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

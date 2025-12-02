---
layout: default
title: "Modélisation et Analyse des Systèmes Linéaires et Représentation d'État - S5"
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
</style>

<div class="back-nav">
  <a href="./my-courses-2022-2023.html">← Retour à Mes Cours 2022-2023</a>
</div>

# 📊 Modélisation et Analyse des Systèmes Linéaires et Représentation d'État - S5

**Année**: 2022-2023 (Semestre 5)  
**Crédits**: 3 ECTS  
**Type**: Automatique et Systèmes  
**Enseignant**: Subias

---

## PART A: PRÉSENTATION GÉNÉRALE

### Objectifs du cours

Ce cours constitue une formation avancée en théorie des systèmes linéaires et en représentation d'état, piliers de l'automatique moderne. L'objectif est de maîtriser les techniques de modélisation mathématique, l'analyse de comportement des systèmes dynamiques, et les méthodes de commande par retour d'état.

### Compétences visées

- Maîtriser les techniques de modélisation des systèmes dynamiques linéaires
- Analyser la stabilité et les performances des systèmes en boucle ouverte et fermée
- Concevoir des lois de commande par retour d'état avec placement de pôles
- Dimensionner des observateurs d'état pour estimer les variables non mesurables
- Utiliser MATLAB/Simulink pour l'analyse et la simulation de systèmes automatiques
- Appliquer les critères de commandabilité et observabilité
- Interpréter les réponses fréquentielles (Bode, Nyquist, marges de stabilité)

### Organisation

- **Volume horaire**: Cours magistraux, TD et TP MATLAB/Simulink
- **Évaluation**: Examen écrit, TPs notés, Projet sur robot auto-équilibré
- **Outils**: MATLAB Control System Toolbox, Simulink
- **Prérequis**: Transformée de Laplace, équations différentielles, algèbre linéaire

---

## PART B: EXPÉRIENCE, CONTEXTE ET FONCTION

### Contenu pédagogique

Le cours s'articule autour de trois axes principaux: la modélisation des systèmes, l'analyse de stabilité et performances, et la synthèse de lois de commande.

### 1. Modélisation des systèmes linéaires

#### Représentation par fonction de transfert

La fonction de transfert relie l'entrée U(s) à la sortie Y(s) en transformée de Laplace :

H(s) = Y(s) / U(s) = N(s) / D(s)

Exemple de système du second ordre (moteur DC) :
```
H(s) = Km / (Tm*s + 1)
```

Avec Km = gain statique, Tm = constante de temps.

#### Représentation d'état

Forme générale pour un système SISO :
```
dx/dt = A*x + B*u  (équation d'état)
y = C*x + D*u      (équation de sortie)
```

Matrices d'état :
- A (n×n) : matrice dynamique
- B (n×1) : matrice de commande
- C (1×n) : matrice d'observation
- D : action directe (souvent 0)

Exemple concret d'un système d'ordre 2 :
```matlab
A = [0 1; -10 -6.316]
B = [0; 1]
C = [k/0.1001 0]
D = 0
```

### 2. Stabilité des systèmes

#### Critère de Routh-Hurwitz

Pour le polynôme caractéristique D(s) = an*s^n + ... + a1*s + a0, on construit le tableau de Routh :

| s^n   | an    | an-2  | an-4  |
| s^n-1 | an-1  | an-3  | an-5  |
| s^n-2 | b1    | b2    | ...   |
| ...   | ...   | ...   | ...   |

Avec b1 = (an-1*an-2 - an*an-3) / an-1

**Condition de stabilité** : tous les éléments de la première colonne doivent être strictement positifs.

Implémentation MATLAB disponible avec la fonction `routh.m` :
```matlab
function RA=routh(poli,epsilon)
% Calcule le tableau de Routh pour un polynôme
% Gère les cas particuliers (première colonne nulle, ligne de zéros)
```

#### Analyse par les pôles

Un système est stable si tous les pôles (racines de D(s)) ont une partie réelle négative :
```
Re(pi) < 0 pour tout i
```

Classification :
- **Stable asymptotiquement** : tous les pôles à partie réelle strictement négative
- **Marginalement stable** : pôles sur l'axe imaginaire (non répétés)
- **Instable** : au moins un pôle à partie réelle positive

### 3. Analyse fréquentielle

#### Diagrammes de Bode

Représentation du gain (en dB) et de la phase (en degrés) en fonction de la fréquence :
```
Gain(dB) = 20*log10(|H(jω)|)
Phase(°) = arg(H(jω)) * 180/π
```

Exemple de TP1 avec fonction de transfert H(s) = 0.717 / (0.0033*s + 1) :
```matlab
H = tf([0.717], [0.0033 1]);
bode(H)
```

Mesures expérimentales effectuées :
- Fréquences : 0.05 à 10 Hz
- Gains mesurés : de 0.669 à 0.061 (de -3.5dB à -24dB)
- Déphasages : de -2.2° à -90°

#### Marges de stabilité

**Marge de gain (Gm)** : gain additionnel avant instabilité à la fréquence de coupure de phase -180°

**Marge de phase (Pm)** : phase additionnelle avant instabilité à la fréquence de coupure de gain 0dB

Commande MATLAB :
```matlab
[Gm, Pm, Wcg, Wcp] = margin(sys);
```

Critères de robustesse :
- Pm > 45° (bonne robustesse)
- Gm > 6dB (bonne robustesse)

### 4. Commande par retour d'état

#### Placement de pôles

Pour un système commandable, on peut imposer les pôles en boucle fermée avec un retour d'état u = -K*x + r.

La matrice de gain K est calculée pour placer les pôles désirés :
```matlab
K = place(A, B, poles_desired)
```

Exemple du TP3 avec pôles complexes conjugués :
```matlab
K = place(A, B, [-2+2i, -2-2i])
```

Les pôles choisis déterminent les performances :
- Partie réelle : rapidité (plus négatif = plus rapide)
- Partie imaginaire : oscillations (plus grand = plus d'oscillations)

#### Commandabilité

Un système est commandable si on peut amener l'état de n'importe quelle condition initiale à n'importe quel état désiré en temps fini.

**Critère de Kalman** : rang de la matrice de commandabilité = n

Matrice de commandabilité :
```
Mc = [B | A*B | A^2*B | ... | A^(n-1)*B]
```

Test MATLAB :
```matlab
Mc = ctrb(A, B);
rank_Mc = rank(Mc);
% Système commandable si rank_Mc == n
```

### 5. Observateurs d'état

#### Principe

Lorsque tous les états ne sont pas mesurables, on utilise un observateur pour reconstruire l'état complet à partir de la sortie mesurée y.

Équation de l'observateur de Luenberger :
```
dx_hat/dt = A*x_hat + B*u + L*(y - y_hat)
y_hat = C*x_hat
```

Avec L : gain de l'observateur.

#### Observabilité

Un système est observable si on peut déterminer l'état initial x(0) à partir de la connaissance de u(t) et y(t) sur un intervalle fini.

**Critère de Kalman** : rang de la matrice d'observabilité = n

Matrice d'observabilité :
```
Mo = [C; C*A; C*A^2; ...; C*A^(n-1)]
```

Test MATLAB :
```matlab
Mo = obsv(A, C);
rank_Mo = rank(Mo);
% Système observable si rank_Mo == n
```

#### Placement des pôles de l'observateur

Les pôles de l'observateur sont choisis plus rapides (2 à 5 fois) que ceux de la commande pour garantir une convergence rapide de l'estimation.

Exemples du TD :
```matlab
L1 = [-0.365, -0.78]   % Pôles lents
L2 = [0.59, 0.32]      % Pôles rapides
```

### 6. Analyse modale et formes canoniques

#### Décomposition modale

Si A est diagonalisable, on peut écrire :
```
A = P * Λ * P^(-1)
```

Avec Λ matrice diagonale des valeurs propres et P matrice des vecteurs propres.

Changement de variable z = P^(-1)*x :
```
dz/dt = Λ*z + P^(-1)*B*u
y = C*P*z
```

Chaque mode évolue indépendamment selon zi(t) = exp(λi*t).

#### Formes canoniques

**Forme commandable** : matrices A et B ont une structure particulière facilitant le placement de pôles.

**Forme observable** : matrices A et C ont une structure facilitant la conception d'observateurs.

---

## C. Aspects techniques et pratiques

### 1. Travaux Pratiques MATLAB

#### TP1 : Identification expérimentale

Manipulation d'un système réel (moteur ou servomoteur) pour mesurer sa réponse fréquentielle.

Code de traitement des données :
```matlab
% Données expérimentales
Vg = [-3.93, -2.39, -1.17, -0.44, 0, 0.37, ...];
O = [-292*(2*pi/60)*9, -179*(2*pi/60)*9, ...]; % Vitesse en rad/s

% Tracé caractéristique statique
plot(O, Vg);
xlabel('Vitesse angulaire (rad/s)');
ylabel('Tension (V)');

% Analyse fréquentielle
G = [0.669, 0.659, 0.609, 0.528, ...];
G_dB = 20*log10(G);
freq = [0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 7.5, 10];

semilogx(freq, G_dB);
xlabel('Fréquence (Hz)');
ylabel('Gain (dB)');
```

Modèle identifié : H(s) = 0.717 / (0.0033*s + 1)
- Gain statique : K = 0.717
- Constante de temps : T = 3.3 ms

#### TP2 : Analyse de stabilité en boucle fermée

Système avec capteur, moteur et retour :
```matlab
Ks = 1.55;   % Gain capteur
Km = 47.8;   % Gain moteur
Kg = 0.015;  % Gain réducteur
Tm = 0.3;    % Constante de temps moteur
K = 0.887;   % Gain global

% Fonction de transfert en boucle fermée
num = [Km*K/9];
den = [Tm, 1, Km*K*Ks/9];
sys = tf(num, den);

% Analyse de stabilité
[Gm, Pm, Wcg, Wcp] = margin(sys);
disp(['Marge de gain : ', num2str(Gm), ' (', num2str(20*log10(Gm)), ' dB)']);
disp(['Marge de phase : ', num2str(Pm), '°']);

% Calcul des pôles
P = pole(sys);
disp('Pôles du système :');
disp(P);
```

Résultats typiques :
- Pm ≈ 60° → Système bien amorti
- Pôles à partie réelle négative → Système stable

#### TP3 : Commande par retour d'état

Système d'ordre 2 avec placement de pôles :
```matlab
k = 5;
A = [0 1; -10 -6.316];
B = [0; 1];
C = [k/0.1001 0];

% Création du modèle d'état
sys = ss(A, B, C, 0);

% Placement de pôles en -2±2j
poles_desired = [-2+2i, -2-2i];
K = place(A, B, poles_desired);

disp('Gain de retour d''état K :');
disp(K);

% Système en boucle fermée
A_cl = A - B*K;
sys_cl = ss(A_cl, B, C, 0);

% Réponse indicielle
step(sys_cl);
title('Réponse en boucle fermée avec retour d''état');
```

### 2. Projet : Robot auto-équilibré (NXT Way)

#### Modélisation du robot Lego Mindstorms EV3

Paramètres physiques du fichier `NXP_robot_parameters.m` :

| Paramètre | Valeur | Unité | Description |
|-----------|--------|-------|-------------|
| m | 0.03 | kg | Masse d'une roue |
| R | 0.042 | m | Rayon des roues |
| Jw | m*R²/2 | kg·m² | Inertie d'une roue |
| M | 0.67 | kg | Masse du corps |
| H | 0.152 | m | Hauteur du corps |
| L | H/2 | m | Distance centre de masse / axe roues |
| Jpsi | M*L²/3 | kg·m² | Inertie en tangage |
| g | 9.81 | m/s² | Accélération de la gravité |

Moteur DC :
- Jm = 1e-5 kg·m² (inertie moteur)
- Rm = 6.83 Ω (résistance)
- Kb = 0.468 V·s/rad (constante de force contre-électromotrice)
- Kt = 0.3047 N·m/A (constante de couple)

#### Simulation Simulink

Le projet utilise `NXTwaySim.slx` pour simuler le comportement du robot avec :
- Modèle non-linéaire du pendule inversé
- Commande par retour d'état
- Observateur d'état pour estimer l'angle et la vitesse angulaire
- Animation 3D du robot avec `PlayAnimation.m`

Objectif : stabiliser le robot en position verticale (θ = 0°) malgré les perturbations.

### 3. Outils MATLAB essentiels

#### Fonctions de base

```matlab
% Création de modèle
sys = tf(num, den);              % Fonction de transfert
sys = ss(A, B, C, D);            % Représentation d'état

% Conversion
[A, B, C, D] = tf2ss(num, den);  % TF → État
[num, den] = ss2tf(A, B, C, D);  % État → TF

% Analyse
pole(sys);                       % Calcul des pôles
zero(sys);                       % Calcul des zéros
eig(A);                          % Valeurs propres de A
rank(ctrb(A, B));               % Test de commandabilité
rank(obsv(A, C));               % Test d'observabilité

% Réponses temporelles
step(sys);                       % Réponse indicielle
impulse(sys);                    % Réponse impulsionnelle
lsim(sys, u, t);                % Réponse à une entrée quelconque

% Analyse fréquentielle
bode(sys);                       % Diagrammes de Bode
nyquist(sys);                    % Diagramme de Nyquist
nichols(sys);                    % Diagramme de Black-Nichols
margin(sys);                     % Marges de stabilité

% Synthèse
K = place(A, B, poles);          % Placement de pôles
L = place(A', C', poles)';       % Observateur (dualité)
```

### 4. Méthodes de conception

#### Choix des pôles en boucle fermée

Pour un système d'ordre 2, forme canonique :
```
H(s) = ωn² / (s² + 2ζωn*s + ωn²)
```

Paramètres de performance :
- ωn : pulsation naturelle (rapidité)
- ζ : coefficient d'amortissement (dépassement)

Relation avec les pôles :
```
p1,2 = -ζωn ± jωn*sqrt(1-ζ²)
```

Recommandations :
- ζ = 0.7 : bon compromis (dépassement ≈ 5%)
- Temps de réponse à 5% : tr ≈ 3 / (ζωn)

#### Séparation des dynamiques

**Principe de séparation** : on peut concevoir indépendamment le retour d'état K et l'observateur L, puis les combiner.

Règle pratique : placer les pôles de l'observateur 2 à 5 fois plus rapides que ceux de la commande.

Exemple :
- Pôles commande : -2±2j
- Pôles observateur : -10, -12 (5 fois plus rapides)

---

## D. Analyse et perspectives

### 1. Applications industrielles

#### Systèmes de régulation

- **Procédés industriels** : régulation de température, pression, débit
- **Robotique mobile** : stabilisation de robots à roues, drones
- **Aérospatial** : pilotage automatique d'avions, fusées
- **Automobile** : régulation de vitesse (cruise control), ESP, suspension active

#### Exemples concrets

**Segway / robots auto-équilibrés** : application directe du projet NXT Way avec pendule inversé et commande par retour d'état.

**Quadrirotors** : modèle d'état avec 12 états (position, vitesse, angles, vitesses angulaires), commande hiérarchique avec boucles imbriquées.

### 2. Liens avec d'autres cours

| Cours | Semestre | Lien avec Modélisation Systèmes Linéaires |
|-------|----------|-------------------------------------------|
| Circuits et Filtres Analogiques | S5 | Analyse fréquentielle, Bode, systèmes du 1er et 2e ordre |
| Fondements Électronique Numérique | S5 | Échantillonnage pour commande numérique |
| Systèmes Bouclés | S5 | Asservissements, correcteurs PID |
| Commande Numérique | S8 | Discrétisation, commande échantillonnée |
| Temps Réel | S8 | Implémentation de lois de commande |
| Processus Stochastiques | S8 | Filtre de Kalman (extension de l'observateur) |

### 3. Extensions et sujets avancés

#### Commande optimale

Minimisation d'un critère de performance (LQR - Linear Quadratic Regulator) :
```
J = ∫[x'Qx + u'Ru] dt
```

Conduit à un gain optimal K calculé via équation de Riccati.

#### Systèmes non-linéaires

Pour les systèmes non-linéaires, linéarisation autour d'un point d'équilibre :
```
dx/dt = f(x, u) ≈ f(x0, u0) + ∂f/∂x|(x0,u0) * (x-x0) + ∂f/∂u|(x0,u0) * (u-u0)
```

Obtention d'un modèle linéaire tangent exploitable avec les techniques du cours.

#### Systèmes multivariables (MIMO)

Extension à plusieurs entrées et sorties :
- Matrices B (n×m), C (p×n), D (p×m)
- Analyse de couplage entre canaux
- Commande découplante

### 4. Compétences professionnelles développées

Ce cours a permis de développer des compétences clés en automatique moderne, essentielles pour la carrière d'ingénieur en systèmes embarqués, robotique, ou automatisation industrielle.

**Modélisation**:
- Mise en équations d'un système physique à partir des lois fondamentales
- Identification expérimentale de paramètres par analyse fréquentielle
- Validation de modèles par comparaison simulation/réel
- Choix pertinent des variables d'état

**Analyse**:
- Détermination de stabilité par méthodes algébriques (Routh) et graphiques (lieu des pôles)
- Évaluation de performances (rapidité, dépassement, erreur statique)
- Robustesse aux variations de paramètres et perturbations
- Interprétation des diagrammes de Bode et marges de stabilité

**Synthèse**:
- Conception de lois de commande par placement de pôles selon cahier des charges
- Dimensionnement d'observateurs d'état pour estimation des variables non mesurables
- Optimisation de critères de performance (temps de réponse, dépassement)
- Application du principe de séparation

**Outils informatiques**:
- Maîtrise de MATLAB/Simulink pour l'automatique (Control System Toolbox)
- Programmation de fonctions d'analyse (Routh, identification, placement de pôles)
- Simulation de systèmes complexes avec Simulink
- Visualisation et interprétation de résultats

### 5. Méthodologie de résolution de problèmes

#### Démarche type pour un problème d'automatique

1. **Modélisation** : établir les équations différentielles ou fonction de transfert
2. **Mise sous forme d'état** : définir les variables d'état pertinentes
3. **Analyse du système en boucle ouverte** :
   - Stabilité (Routh, pôles)
   - Commandabilité et observabilité
   - Performances (réponse indicielle)
4. **Conception de la commande** :
   - Choix des pôles désirés selon cahier des charges
   - Calcul du gain K par placement de pôles
   - Vérification des performances
5. **Conception de l'observateur** (si nécessaire) :
   - Choix des pôles de l'observateur (plus rapides)
   - Calcul du gain L
6. **Simulation et validation** :
   - Test avec Simulink
   - Analyse de robustesse
   - Ajustements si nécessaire

### 6. Pièges à éviter

L'expérience des TDs et du projet a permis d'identifier plusieurs erreurs courantes en automatique.

**Pièges théoriques**:
- **Système non commandable/observable**: toujours vérifier les critères de Kalman avant de tenter un placement de pôles ou de concevoir un observateur
- **Pôles de l'observateur trop rapides**: risque d'amplification du bruit de mesure et d'instabilité numérique
- **Confusion entre pôles et zéros**: les pôles déterminent la stabilité, les zéros affectent la forme de la réponse
- **Oubli des conditions initiales**: la réponse complète = réponse libre + réponse forcée

**Pièges pratiques**:
- **Unités incohérentes**: attention aux conversions rad/s ↔ tr/min, degrés ↔ radians
- **Saturation des actionneurs**: prendre en compte les limites physiques (commande limitée en amplitude et vitesse)
- **Modèle linéaire hors zone de validité**: linéarisation valable uniquement autour du point d'équilibre
- **Échantillonnage insuffisant**: respect du critère de Shannon pour l'implémentation numérique

**Pièges MATLAB**:
- **Confusion entre systèmes SISO et MIMO**: attention aux dimensions des matrices
- **Mauvais choix de solveur dans Simulink**: peut entraîner des erreurs numériques
- **Oubli de la normalisation**: certaines fonctions MATLAB attendent des paramètres normalisés

### 7. Ressources et approfondissements

#### Documentation MATLAB

- **Control System Toolbox User's Guide**: documentation complète des fonctions
- **Simulink Control Design**: conception et analyse de systèmes de commande
- **Exemples intégrés**: `help control`, `demo control` dans MATLAB
- **MATLAB Central**: communauté avec exemples et scripts partagés

#### Ouvrages de référence

- **"Modern Control Engineering"** - Ogata: référence classique, approche pédagogique
- **"Linear System Theory and Design"** - Chen: approche mathématique rigoureuse
- **"Feedback Control of Dynamic Systems"** - Franklin, Powell, Emami-Naeini: excellent pour les applications
- **"Automatique: Systèmes linéaires"** - Duc, Théron: en français, adapté au cursus français

#### Logiciels alternatifs

- **Python**: bibliothèques `control`, `scipy.signal` pour calculs scientifiques
- **Scilab**: alternative open-source à MATLAB avec Xcos (équivalent Simulink)
- **Octave**: compatible MATLAB, gratuit
- **LabVIEW**: pour applications industrielles et acquisition de données

### Mon opinion

Ce cours représente un pilier fondamental de l'automatique moderne et s'avère indispensable pour tout ingénieur travaillant dans les domaines des systèmes embarqués, de la robotique, ou de l'automatisation industrielle.

**Pourquoi ce cours est essentiel**:

1. **Approche moderne**: la représentation d'état est la base de l'automatique contemporaine (vs approche classique par fonction de transfert)
2. **Systèmes multivariables**: traitement naturel des systèmes MIMO (Multiple Input Multiple Output)
3. **Connexion avec l'informatique**: structure matricielle facilite l'implémentation numérique
4. **Base pour sujets avancés**: commande optimale (LQR/LQG), commande robuste (H∞), commande prédictive (MPC)

**Apports du projet robot NXT Way**:

Le projet de robot auto-équilibré a été particulièrement formateur:
- **Application concrète**: pendule inversé = problème classique d'automatique
- **Système instable**: nécessité absolue d'une commande performante
- **Multidisciplinarité**: mécanique + électronique + automatique
- **Défi technique**: équilibrage en temps réel avec contraintes matérielles

**Connexions avec autres cours**:

L'automatique est une discipline transversale qui s'appuie sur de nombreux autres cours:
- **Circuits et Filtres Analogiques** (S5): analyse fréquentielle, diagrammes de Bode
- **Fondements Électronique Numérique** (S5): échantillonnage pour commande numérique
- **Systèmes Bouclés** (S5): asservissements, correcteurs PID (approche complémentaire)
- **Commande Numérique** (S8): discrétisation, commande échantillonnée, microcontrôleurs
- **Temps Réel** (S8): implémentation de lois de commande avec contraintes temporelles
- **Processus Stochastiques** (S8): filtre de Kalman (extension stochastique de l'observateur)

**Évolution technologique**:

L'automatique évolue rapidement avec les nouvelles technologies:

**Tendances actuelles**:
- **Apprentissage automatique**: hybridation commande classique + IA (Deep Reinforcement Learning)
- **Commande prédictive**: MPC (Model Predictive Control) dans l'automobile et l'industrie
- **Systèmes distribués**: commande multi-agents, essaims de drones
- **Optimisation en temps réel**: calcul embarqué performant (DSP, FPGA)

**Applications émergentes**:
- **Véhicules autonomes**: contrôle longitudinal/latéral, planification de trajectoire
- **Drones**: stabilisation, suivi de trajectoire, vol en formation
- **Exosquelettes**: assistance robotique, rééducation
- **Industrie 4.0**: cobotique (robots collaboratifs), maintenance prédictive

**Recommandations pour réussir**:

1. **Comprendre avant de calculer**: visualiser le comportement physique du système
2. **Maîtriser MATLAB**: indispensable pour l'automatique (industrie + recherche)
3. **Penser "états"**: raisonner en variables d'état plutôt qu'en entrées/sorties
4. **Simuler systématiquement**: valider les calculs avant implémentation réelle
5. **Tenir compte des limitations**: saturation, bruit, échantillonnage

**Applications professionnelles**:

Ces compétences sont très recherchées dans de nombreux secteurs:

**Automobile**:
- Systèmes ADAS (Advanced Driver Assistance Systems): ESP, ABS, régulateur adaptatif
- Véhicules autonomes: contrôle de trajectoire, fusion de capteurs
- Motorisation hybride/électrique: gestion d'énergie, contrôle de traction

**Aéronautique/Spatial**:
- Pilotage automatique d'avions, drones, fusées
- Stabilisation de satellites, contrôle d'attitude
- Lanceurs: guidage, navigation, contrôle

**Robotique**:
- Robots mobiles: navigation, évitement d'obstacles
- Robots manipulateurs: contrôle de trajectoire, force
- Robots humanoïdes: équilibrage, marche dynamique

**Industrie**:
- Automatisation de procédés: chimie, pétrochimie, agroalimentaire
- Machines-outils: positionnement précis, usinage
- Énergies renouvelables: MPPT pour PV, contrôle d'éoliennes

**Perspectives de carrière**:
- Ingénieur automaticien: conception de systèmes de commande
- Ingénieur système embarqué: implémentation temps réel
- Ingénieur R&D: algorithmes de commande avancée
- Consultant: expertise en automatique pour divers secteurs

---

**Bilan personnel**: Ce cours a fourni les outils mathématiques et pratiques pour analyser et commander des systèmes dynamiques linéaires. L'approche état constitue une méthodologie puissante pour les systèmes multivariables et la commande moderne. Les TPs MATLAB et le projet robot ont permis de concrétiser ces concepts théoriques sur des applications réelles d'automatique. C'est un cours exigeant mais absolument fondamental pour une carrière en automatique, robotique, ou systèmes embarqués.

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

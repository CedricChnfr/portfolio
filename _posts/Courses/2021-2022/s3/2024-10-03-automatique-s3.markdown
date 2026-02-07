---
layout: default
title: "Automatique - S3"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

<style>
.back-nav { margin-bottom: 20px; }
.back-nav a { text-decoration: none; color: #2a7ae2; font-weight: 600; }
.back-nav a:hover { text-decoration: underline; }
.section-title { color: #2a7ae2; border-bottom: 2px solid #2a7ae2; padding-bottom: 10px; margin-top: 30px; margin-bottom: 20px; }
</style>

<div class="back-nav">
  <a href="./my-courses-2021-2022.html">&larr; Retour a Mes Cours 2021-2022</a>
</div>

# Automatique - Semestre 3

**Annee**: 2021-2022 | **Semestre**: 3 | **Type**: Scientifique

---

## PART A - Présentation Générale du Cours

### Contexte pédagogique

L'automatique constitue une discipline centrale du DUT GEII, positionnée au semestre 3 après l'acquisition des bases en mathématiques (transformée de Laplace, équations différentielles), traitement du signal et systèmes linéaires. Ce cours établit le pont entre la théorie des systèmes et leur application pratique en régulation et contrôle, compétences essentielles pour l'ingénieur en électronique et informatique industrielle.

### Objectifs d'apprentissage

**Objectifs principaux :**
- Comprendre les principes fondamentaux des systèmes asservis et de la boucle de rétroaction
- Maîtriser la représentation des systèmes par fonctions de transfert et schémas-blocs
- Analyser les performances temporelles et fréquentielles des systèmes bouclés
- Concevoir et régler des régulateurs classiques (P, PI, PID)
- Évaluer la stabilité des systèmes par critères algébriques et fréquentiels

**Compétences visées :**
- Modélisation de systèmes physiques par fonctions de transfert
- Analyse de la stabilité et des performances
- Conception de correcteurs pour répondre à un cahier des charges
- Utilisation d'outils de simulation (MATLAB/Simulink)
- Validation expérimentale sur systèmes réels

### Prérequis

- Transformée de Laplace et transformées inverses
- Résolution d'équations différentielles linéaires
- Analyse fréquentielle (diagrammes de Bode)
- Nombres complexes et représentation polaire
- Bases en physique (mécanique, électricité)

---

## PART B: EXPÉRIENCE, CONTEXTE ET FONCTION DU COURS

### Module 1 : Fondamentaux des systèmes asservis

#### Introduction à l'automatique

**Définitions et vocabulaire :**
- **Automatique** : Science de la commande automatique des systèmes
- **Système** : Ensemble d'éléments en interaction avec son environnement
- **Grandeur de consigne** (référence) : Valeur désirée en sortie
- **Grandeur de commande** : Variable d'entrée pour agir sur le système
- **Grandeur de sortie** (mesure) : Variable que l'on cherche à réguler
- **Perturbation** : Signal externe non désiré affectant le système

**Commande en boucle ouverte :**
```
Consigne → [Contrôleur] → [Système] → Sortie
```
- Pas de mesure de la sortie
- Pas de correction en temps réel
- Sensible aux perturbations et incertitudes
- Simple mais peu précis

**Commande en boucle fermée (asservissement) :**
```
Consigne ─→(+)→ [Contrôleur] → [Système] → Sortie
           │                                  ↓
           └──────────[Capteur]←──────────────┘
                  (rétroaction)
```
- Mesure continue de la sortie
- Comparaison avec la consigne (calcul d'erreur)
- Correction automatique
- Robustesse aux perturbations

**Avantages de l'asservissement :**
- Précision accrue (réduction d'erreur statique)
- Insensibilité aux perturbations
- Compensation des variations de paramètres
- Amélioration de la dynamique

**Limitations :**
- Risque d'instabilité
- Complexité accrue
- Coût des capteurs et traitement

#### Représentation par schémas-blocs

**Blocs élémentaires :**
- **Bloc** : Fonction de transfert H(s) = Sortie(s)/Entrée(s)
- **Sommateur** : Addition/soustraction de signaux
- **Point de prélèvement** : Mesure d'un signal

**Règles de simplification :**
- Blocs en série : $H(s) = H_1(s) \cdot H_2(s)$
- Blocs en parallèle : $H(s) = H_1(s) + H_2(s)$
- Boucle de rétroaction : $H(s) = \frac{H_G(s)}{1 \pm H_G(s) \cdot H_R(s)}$

**Fonction de transfert en boucle ouverte (FTBO) :**
$$\text{FTBO}(s) = C(s) \cdot G(s) \cdot H(s)$$
où C = correcteur, G = processus, H = capteur

**Fonction de transfert en boucle fermée (FTBF) :**
$$\text{FTBF}(s) = \frac{Y(s)}{R(s)} = \frac{C(s)G(s)}{1 + C(s)G(s)H(s)}$$

### Module 2 : Étude des systèmes du 1er et 2ème ordre

#### Systèmes du premier ordre

**Forme canonique :**
$$H(s) = \frac{K}{1 + \tau s}$$
- K = gain statique
- τ = constante de temps (secondes)

**Réponse indicielle (échelon unitaire) :**
$$y(t) = K(1 - e^{-t/\tau})$$

**Caractéristiques temporelles :**
- Valeur finale : y(∞) = K
- Temps de réponse à 5% : $t_{r5\%} = 3\tau$
- Temps de réponse à 2% : $t_{r2\%} = 4\tau$
- Pente initiale : K/τ

**Réponse fréquentielle :**
- Gain : $|H(j\omega)| = \frac{K}{\sqrt{1 + (\omega\tau)^2}}$
- Phase : $\phi(\omega) = -\arctan(\omega\tau)$
- Pulsation de coupure : $\omega_c = 1/\tau$

**Exemples physiques :**
- Circuit RC : τ = RC
- Circuit RL : τ = L/R
- Système thermique : τ = capacité thermique / conductance

#### Systèmes du second ordre

**Forme canonique :**
$$H(s) = \frac{K\omega_0^2}{s^2 + 2\zeta\omega_0 s + \omega_0^2}$$
- K = gain statique
- ω₀ = pulsation propre non amortie (rad/s)
- ζ = coefficient d'amortissement (sans dimension)

**Types de régime selon ζ :**

1. **Régime apériodique (ζ > 1) :**
   - Deux pôles réels distincts
   - Pas de dépassement
   - Montée lente

2. **Régime critique (ζ = 1) :**
   - Deux pôles réels confondus
   - Temps de montée optimal sans dépassement
   - Compromis idéal

3. **Régime pseudo-périodique (0 < ζ < 1) :**
   - Deux pôles complexes conjugués
   - Oscillations amorties
   - Dépassement présent

**Paramètres du régime pseudo-périodique :**

- **Premier dépassement :**
$$D_1(\%) = 100 \cdot e^{-\pi\zeta/\sqrt{1-\zeta^2}}$$

- **Pseudo-période :**
$$T_p = \frac{2\pi}{\omega_0\sqrt{1-\zeta^2}}$$

- **Temps de réponse à 5% :**
$$t_{r5\%} \approx \frac{3}{\zeta\omega_0}$$

- **Temps de montée :**
$$t_m \approx \frac{1.8}{\omega_0}$$ (pour 0.4 < ζ < 0.8)

**Relation dépassement-amortissement :**
- ζ = 0.7 → D₁ ≈ 5% (valeur optimale courante)
- ζ = 0.5 → D₁ ≈ 16%
- ζ = 0.3 → D₁ ≈ 37%

### Module 3 : Stabilité des systèmes

#### Notion de stabilité

**Définition BIBO (Bounded Input Bounded Output) :**
Un système est stable si toute entrée bornée produit une sortie bornée.

**Critère des pôles :**
Un système linéaire est stable si et seulement si tous les pôles de sa fonction de transfert ont une partie réelle strictement négative (dans le demi-plan gauche de Laplace).

#### Critère algébrique de Routh-Hurwitz

**Objectif :**
Déterminer la stabilité sans calculer explicitement les pôles.

**Méthode :**
Pour un polynôme caractéristique :
$$D(s) = a_n s^n + a_{n-1} s^{n-1} + \ldots + a_1 s + a_0$$

1. Construction du tableau de Routh
2. Analyse de la première colonne
3. Système stable ⇔ tous les termes de la 1ère colonne sont de même signe

**Cas particulier :**
Changement de signe → pôle(s) dans le demi-plan droit → instabilité

#### Critères fréquentiels

**Diagramme de Bode :**
- Gain en dB : $G_{dB} = 20\log_{10}|H(j\omega)|$
- Phase en degrés : $\phi = \arg(H(j\omega))$

**Marge de gain (MG) :**
$$MG_{dB} = -G_{dB}(\omega_{180°})$$
où ω₁₈₀° est la pulsation pour laquelle φ = -180°

- MG > 0 dB → stable
- MG recommandée : 6 à 12 dB

**Marge de phase (Mφ) :**
$$M\phi = 180° + \phi(\omega_c)$$
où ω_c est la pulsation de coupure à 0 dB

- Mφ > 0° → stable
- Mφ recommandée : 45° à 60°

**Critère du revers (Nyquist simplifié) :**
Tracé de FTBO(jω) dans le plan complexe
- Si le lieu n'entoure pas le point critique (-1, 0), le système bouclé est stable

**Lieu de Black :**
Représentation FTBO dans plan (Gain dB, Phase)
- Permet lecture directe des marges
- Visualisation de la robustesse

### Module 4 : Performances des systèmes asservis

#### Critères de performance

**Précision (erreur statique) :**

L'erreur en régime permanent dépend de la classe du système et du type d'entrée.

**Classe d'un système :**
Nombre d'intégrateurs dans la FTBO → ordre du zéro en s = 0

- Classe 0 : $\text{FTBO}(s) = \frac{K \cdot (\ldots)}{(\ldots)}$
- Classe 1 : $\text{FTBO}(s) = \frac{K \cdot (\ldots)}{s \cdot (\ldots)}$
- Classe 2 : $\text{FTBO}(s) = \frac{K \cdot (\ldots)}{s^2 \cdot (\ldots)}$

**Erreurs selon le type d'entrée :**

| Entrée | Classe 0 | Classe 1 | Classe 2 |
|--------|----------|----------|----------|
| Échelon | $\frac{1}{1+K}$ | 0 | 0 |
| Rampe | ∞ | $\frac{1}{K}$ | 0 |
| Parabole | ∞ | ∞ | $\frac{1}{K}$ |

**Rapidité :**
- Temps de réponse à 5% ou 2%
- Temps de montée (10% → 90%)
- Bande passante à -3 dB

**Dépassement :**
- Premier dépassement D₁ (%)
- Nombre d'oscillations avant stabilisation

**Compromis fondamental :**
Rapidité ↔ Dépassement ↔ Stabilité

Augmenter le gain améliore la précision mais peut dégrader la stabilité et augmenter le dépassement.

### Module 5 : Correction des systèmes

#### Régulateurs PID classiques

**Correcteur Proportionnel (P) :**
$$C(s) = K_p$$

*Effet :*
- Réduit l'erreur statique (mais ne l'annule pas pour classe 0)
- Améliore la rapidité
- Peut réduire la stabilité (marges)

*Limitations :*
- Erreur statique résiduelle
- Risque d'instabilité si Kp trop élevé

**Correcteur Proportionnel-Intégral (PI) :**
$$C(s) = K_p\left(1 + \frac{1}{T_i s}\right) = K_p \frac{T_i s + 1}{T_i s}$$

*Effet :*
- Annule l'erreur statique (ajout d'un intégrateur = classe +1)
- Améliore la précision
- Ralentit légèrement la réponse
- Réduit la marge de phase

*Réglage :*
- Kp : gain proportionnel
- Ti : temps intégral (plus Ti est grand, plus l'action intégrale est faible)

**Correcteur Proportionnel-Intégral-Dérivé (PID) :**
$$C(s) = K_p\left(1 + \frac{1}{T_i s} + T_d s\right)$$

*Effet :*
- Action proportionnelle : réactivité
- Action intégrale : précision (annule erreur statique)
- Action dérivée : anticipe l'évolution, améliore stabilité et réduit dépassement

*Limitations action dérivée :*
- Amplifie le bruit de mesure
- Nécessite souvent un filtrage
- Forme pratique : $C(s) = K_p\left(1 + \frac{1}{T_i s} + \frac{T_d s}{1 + \frac{T_d}{N}s}\right)$ avec N ≈ 10

#### Méthodes de réglage

**Méthode de Ziegler-Nichols (réponse indicielle) :**

À partir de la réponse indicielle en boucle ouverte, identifier :
- Retard τ
- Constante de temps T

| Type | Kp | Ti | Td |
|------|-----|-----|-----|
| P | T/τ | - | - |
| PI | 0.9T/τ | 3τ | - |
| PID | 1.2T/τ | 2τ | 0.5τ |

**Méthode de Ziegler-Nichols (pompage) :**

1. Régler un P pur, augmenter Kp jusqu'à obtenir des oscillations permanentes
2. Noter Ku (gain ultime) et Tu (période d'oscillation)

| Type | Kp | Ti | Td |
|------|-----|-----|-----|
| P | 0.5Ku | - | - |
| PI | 0.45Ku | Tu/1.2 | - |
| PID | 0.6Ku | Tu/2 | Tu/8 |

**Méthode de placement de pôles :**
- Spécifier la dynamique désirée en boucle fermée
- Calculer les paramètres du correcteur pour obtenir ces pôles
- Nécessite un modèle précis du système

**Optimisation par critères :**
- ITAE (Integral of Time-weighted Absolute Error)
- IAE (Integral of Absolute Error)
- ISE (Integral of Squared Error)
- Minimisation numérique

---

## PART C: ASPECTS TECHNIQUES

### Outils de simulation et d'analyse

#### MATLAB/Simulink

**MATLAB - Control System Toolbox :**

*Fonctions principales :*
```matlab
% Définition fonction de transfert
G = tf([num], [den]);  % Numérateur, dénominateur
G = tf(5, [1 2 3]);    % Exemple : 5/(s² + 2s + 3)

% Analyse temporelle
step(G);               % Réponse indicielle
impulse(G);            % Réponse impulsionnelle
lsim(G, u, t);         % Réponse à signal quelconque

% Analyse fréquentielle
bode(G);               % Diagramme de Bode
nyquist(G);            % Lieu de Nyquist
nichols(G);            % Lieu de Black
margin(G);             % Marges de gain et phase

% Stabilité
pole(G);               % Calcul des pôles
rlocus(G);             % Lieu des racines
pzmap(G);              % Carte pôles-zéros

% Performances
stepinfo(G);           % Caractéristiques temporelles
bandwidth(G);          % Bande passante
```

*Analyse d'un système bouclé :*
```matlab
% Système
G = tf(10, [1 2 1]);

% Correcteur PID
Kp = 5; Ki = 2; Kd = 0.5;
C = pid(Kp, Ki, Kd);

% Boucle fermée
T = feedback(C*G, 1);

% Analyse
step(T);
stepinfo(T)
margin(C*G);
```

**Simulink :**

*Blocs principaux :*
- **Sources** : Step, Ramp, Sine Wave, Signal Generator
- **Systèmes** : Transfer Fcn, State-Space, PID Controller
- **Maths** : Sum, Gain, Product, Integrator, Derivative
- **Sinks** : Scope, To Workspace, Display

*Exemple de modèle Simulink :*
1. Consigne (Step) → Sommateur (comparer avec sortie)
2. Erreur → PID Controller → Système (Transfer Fcn)
3. Sortie → Scope + retour vers sommateur

*Paramétrage simulation :*
- Solver : ode45 (Runge-Kutta variable step)
- Stop time : durée simulation
- Max step size : précision

**Simulink PID Tuner :**
- Réglage automatique de PID
- Optimisation selon critères (robustesse, rapidité)
- Visualisation réponse temps réel

#### Python - Control Systems Library

**Installation :**
```bash
pip install control matplotlib numpy scipy
```

**Utilisation :**
```python
import control as ct
import matplotlib.pyplot as plt
import numpy as np

# Définition système
num = [10]
den = [1, 2, 1]
G = ct.TransferFunction(num, den)

# Réponse indicielle
t, y = ct.step_response(G)
plt.plot(t, y)
plt.title('Réponse indicielle')
plt.xlabel('Temps (s)')
plt.ylabel('Sortie')
plt.grid(True)
plt.show()

# Diagramme de Bode
ct.bode_plot(G)
plt.show()

# Marges de stabilité
gm, pm, wg, wp = ct.margin(G)
print(f"Marge de gain : {20*np.log10(gm):.2f} dB")
print(f"Marge de phase : {pm:.2f}°")

# Système bouclé
T = ct.feedback(G, 1)
ct.step_response(T)
```

### Travaux pratiques

#### TP1 : Systèmes du 1er et 2ème ordre

**Objectifs :**
- Identifier paramètres (τ, ω₀, ζ) sur réponses temporelles
- Vérifier formules théoriques
- Analyser influence des paramètres

**Systèmes étudiés :**
1. **Circuit RC (1er ordre) :**
   - Mesure constante de temps
   - Validation $\tau = RC$
   - Temps de réponse

2. **Circuit RLC (2ème ordre) :**
   - Variation de R pour modifier ζ
   - Mesure dépassement et pseudo-période
   - Validation formules

**Matériel :**
- GBF (générateur basse fréquence)
- Oscilloscope numérique
- Composants R, L, C
- Breadboard

**Livrables :**
- Relevés oscilloscope
- Calculs théoriques vs mesures
- Analyse des écarts

#### TP2 : Asservissement de vitesse moteur DC

**Description système :**
```
Consigne → [Correcteur] → [Amplificateur] → [Moteur DC] → Vitesse
  (V)          (µC)           (H-bridge)        + charge      (rpm)
                 ↑                                              ↓
                 └──────────[Codeur incrémental]────────────────┘
```

**Objectifs :**
- Identifier fonction de transfert du moteur
- Implémenter régulateurs P, PI, PID
- Comparer performances
- Analyser effet de perturbations (charge variable)

**Étapes :**

1. **Identification :**
   - Réponse en boucle ouverte à échelon de tension
   - Détermination de K, τ (approximation 1er ordre)

2. **Régulation P :**
   - Variation de Kp
   - Mesure erreur statique, dépassement, stabilité
   - Limite de Kp avant instabilité

3. **Régulation PI :**
   - Réglage Kp et Ti
   - Annulation erreur statique
   - Robustesse aux variations de charge

4. **Régulation PID :**
   - Ajout action dérivée
   - Amélioration dépassement
   - Filtrage du bruit

**Matériel :**
- Moteur DC avec réducteur
- Codeur incrémental (mesure vitesse)
- Pont en H (L298, VNH3SP30)
- Microcontrôleur STM32 ou Arduino
- Alimentation 12V
- Charge mécanique variable

**Mesures :**
- Consigne vs vitesse réelle
- Temps de réponse
- Dépassement
- Erreur statique
- Effet de perturbations

#### TP3 : Régulation de température

**Système :**
- Chambre thermique (enceinte isolée)
- Résistance chauffante (actuateur)
- Sonde PT100 ou thermistance (capteur)
- Carte d'acquisition + PC

**Problématique :**
Système lent (grande constante de temps thermique) → nécessite méthodes d'identification adaptées.

**Travaux :**
1. Identification par réponse indicielle (plusieurs minutes)
2. Modélisation 1er ordre : $G(s) = \frac{K}{1 + \tau s}$ avec τ ≈ 100-300s
3. Synthèse correcteur PI
4. Validation régulation sur plusieurs cycles
5. Test perturbations (ouverture porte)

#### TP4 : Asservissement de position

**Système :**
Servomoteur ou moteur + codeur absolu pour asservissement angulaire.

**Objectifs :**
- Positionnement précis
- Rapidité de réponse
- Absence de dépassement (important pour positionnement)
- Rejet de perturbations (couple résistant)

**Types de consignes :**
- Échelon (saut de position)
- Rampe (vitesse constante)
- Trajectoire complexe (polynomiale)

**Critères de performance :**
- Précision de positionnement : ±0.1°
- Temps de stabilisation : < 0.5s
- Pas de dépassement (ou < 2%)

### Projets applicatifs

#### Projet 1 : Régulateur de vol de drone (simulation)

**Contexte :**
Stabilisation d'attitude d'un quadricoptère (contrôle roulis, tangage, lacet).

**Modélisation :**
- 3 axes indépendants (approximation)
- Modèle simplifié 2ème ordre par axe
- Mesure par IMU (gyroscope + accéléromètre)

**Correcteurs :**
- PID pour chaque axe
- Réglage selon dynamique désirée
- Simulation sous Simulink ou Python

**Critères :**
- Temps de stabilisation < 0.5s
- Dépassement < 10%
- Robustesse aux rafales de vent

#### Projet 2 : Station de régulation industrielle

**Description :**
Simulateur de processus industriel (niveau, débit, pression, température).

**Cahier des charges :**
- Interface homme-machine (HMI)
- Régulation multi-variables
- Gestion alarmes et sécurités
- Traçabilité (enregistrement données)

**Technologies :**
- MATLAB/Simulink pour modèle
- Interface graphique (App Designer, PyQt)
- Communication série vers automate (optionnel)

---

## PART D: ANALYSE ET RÉFLEXION

### Évaluation des connaissances

#### Contrôle continu 1 (Semaine 6) - 1h30

**Sujets abordés :**
- Systèmes du 1er et 2ème ordre
- Calcul de réponses temporelles
- Identification de paramètres (τ, ω₀, ζ)
- Interprétation de courbes

**Compétences évaluées :**
- Calcul de fonctions de transfert
- Analyse de stabilité élémentaire
- Application formules temporelles

#### Contrôle continu 2 (Semaine 11) - 1h30

**Sujets abordés :**
- Stabilité (Routh-Hurwitz, marges)
- Diagrammes de Bode
- Performances (précision, classe)
- Correction P, PI, PID

**Compétences évaluées :**
- Analyse de stabilité
- Lecture de diagrammes
- Synthèse de correcteurs simples

#### Travaux pratiques (Continu)

**Évaluation :**
- Préparation (10%) : questionnaire avant séance
- Manipulation (50%) : démarche, mesures, analyse critique
- Compte-rendu (40%) : qualité, rigueur scientifique, interprétation

**Critères :**
- Compréhension des phénomènes
- Qualité des mesures
- Comparaison théorie/pratique
- Analyse des écarts et limites

#### Projet (Semaines 12-14)

**Livrables :**
- Rapport technique (30 pages max)
- Présentation orale (15 min + 5 min questions)
- Démonstration système (simulation ou réel)

**Critères d'évaluation :**
- Qualité de la modélisation (20%)
- Pertinence du correcteur (30%)
- Validation expérimentale (25%)
- Communication écrite et orale (25%)

#### Examen final (2h)

**Structure :**
- Exercice 1 (6 pts) : Analyse de système (calculs, stabilité)
- Exercice 2 (8 pts) : Synthèse de correcteur
- Exercice 3 (6 pts) : Problème applicatif complet

**Compétences évaluées :**
- Maîtrise globale du cours
- Capacité de synthèse
- Résolution de problèmes
- Autonomie

### Liens interdisciplinaires

#### Avec Mathématiques (S1-S2)
- **Transformée de Laplace** : outil fondamental pour fonctions de transfert
- **Équations différentielles** : modélisation des systèmes dynamiques
- **Nombres complexes** : analyse fréquentielle
- **Algèbre linéaire** : représentation d'état (aperçu)

#### Avec Traitement du Signal (S2)
- **Transformée de Fourier** : lien avec analyse fréquentielle
- **Filtrage** : analogie avec correcteurs
- **Réponse fréquentielle** : diagrammes de Bode

#### Avec Énergie (S1-S3)
- **Moteurs électriques** : systèmes à réguler (vitesse, position)
- **Convertisseurs** : actionneurs de puissance
- **Modélisation** : équations électromécaniques

#### Avec Informatique Embarquée (S3)
- **Implémentation de régulateurs** : PID numériques sur microcontrôleur
- **Acquisition de données** : ADC pour capteurs
- **Temps réel** : contraintes temporelles des boucles de régulation

#### Avec Automatisme (S3)
- **Contrôle séquentiel vs continu** : complémentarité GRAFCET/asservissement
- **Supervision** : intégration régulation dans système global

### Applications professionnelles

#### Secteur industriel

**Automobile :**
- Régulateur de vitesse adaptatif (ACC)
- Contrôle ESP (stabilité)
- Gestion moteur (injection, turbo)
- Direction assistée électrique

**Aéronautique et spatial :**
- Pilote automatique
- Contrôle d'attitude satellites
- Régulation de poussée
- Stabilisation plateformes

**Robotique :**
- Asservissement d'axes (robots industriels)
- Équilibrage robots mobiles
- Contrôle de force (cobotique)
- Drones (stabilisation, suivi de trajectoire)

**Processus industriels :**
- Régulation de température (fours, réacteurs)
- Contrôle de niveau, débit, pression
- Régulation de pH
- Systèmes HVAC (chauffage, ventilation, climatisation)

**Énergie :**
- Régulation de turbines (hydraulique, éolien)
- Contrôle de réseaux électriques
- Batteries et stockage (régulation charge/décharge)
- Suivi point de puissance maximale (MPPT) photovoltaïque

#### Compétences métier

**Ingénieur automaticien :**
- Modélisation de systèmes physiques
- Conception de lois de commande
- Mise en œuvre industrielle
- Validation et certification

**Ingénieur systèmes embarqués :**
- Implémentation régulateurs sur cibles embarquées
- Optimisation temps réel
- Intégration capteurs/actionneurs

**Ingénieur R&D :**
- Algorithmes de commande avancés
- Commande robuste, optimale, prédictive
- Simulation et prototypage virtuel

### Ressources complémentaires

#### Ouvrages de référence

**Niveau DUT/Licence :**
- "Automatique : Systèmes linéaires" - Michel Aubé
- "Automatique appliquée" - Didier Leclercq
- "Introduction aux systèmes asservis" - Jean-Jacques Ruch

**Niveau approfondi :**
- "Modern Control Engineering" - Katsuhiko Ogata
- "Feedback Control of Dynamic Systems" - Franklin, Powell, Emami-Naeini
- "Control Systems Engineering" - Norman Nise

#### Tutoriels et cours en ligne

**MATLAB :**
- Control System Toolbox documentation
- Simulink tutorials (MathWorks)
- MATLAB Onramp (formation gratuite)

**MOOCs :**
- "Control of Mobile Robots" - Coursera (Georgia Tech)
- "Introduction to Control System Design" - edX (MIT)
- "Automatique" - Fun MOOC (CNAM)

**Chaînes YouTube :**
- Brian Douglas - Control Systems Lectures
- MATLAB
- Steve Brunton - Control Bootcamp

#### Logiciels

**Open source :**
- Scilab + Xcos (alternative à MATLAB/Simulink)
- Python Control Systems Library
- GNU Octave + Control package

**Simulateurs :**
- LabVIEW Control Design Toolkit
- PLECS (pour systèmes power electronics)

#### Normes et standards

- **IEC 61131-3** : Langages de programmation automates (dont régulateurs)
- **ISA-5.1** : Instrumentation et symboles
- **ISA-88** : Procédures batch control

### Perspectives et évolutions

#### Vers la commande avancée (S7-S8 INSA)

**Représentation d'état :**
- Modèle matriciel : $\dot{x} = Ax + Bu$, $y = Cx + Du$
- Commandabilité et observabilité
- Commande par retour d'état
- Observateurs d'état

**Commande robuste :**
- Incertitudes de modélisation
- Méthodes H∞
- µ-synthèse
- Approches LMI (Linear Matrix Inequalities)

**Commande optimale :**
- Régulateur LQR (Linear Quadratic Regulator)
- Commande prédictive (MPC - Model Predictive Control)
- Optimisation sous contraintes

**Systèmes non-linéaires :**
- Linéarisation autour d'un point
- Commande par mode glissant
- Lyapunov et stabilité non-linéaire
- Backstepping

#### Tendances actuelles

**Industrie 4.0 :**
- Intégration IoT et automatique
- Digital twins (jumeaux numériques)
- Maintenance prédictive
- Auto-tuning et apprentissage

**Intelligence artificielle :**
- Réglage de PID par algorithmes génétiques
- Apprentissage par renforcement pour commande
- Réseaux de neurones pour modélisation
- Fusion commande classique + IA

**Systèmes distribués :**
- Commande multi-agents
- Contrôle de formations (drones, robots)
- Réseaux de capteurs

---

## 📖 SYNTHÈSE

L'automatique constitue un pilier fondamental de l'ingénierie des systèmes, permettant de concevoir des systèmes autonomes, précis et robustes. Ce cours de S3 établit les bases théoriques et pratiques nécessaires à la compréhension et à la conception de systèmes asservis, compétences essentielles pour l'ingénieur GEII.

**Points clés à retenir :**
- La boucle de rétroaction permet précision et robustesse
- L'analyse de stabilité est primordiale (critères algébriques et fréquentiels)
- Les PID, bien que classiques, restent majoritaires en industrie (>90% des régulateurs)
- Le compromis stabilité-précision-rapidité guide toute conception
- La validation expérimentale est indispensable

**Compétences acquises :**
- Modélisation par fonctions de transfert
- Analyse temporelle et fréquentielle
- Synthèse de régulateurs PID
- Utilisation d'outils professionnels (MATLAB/Simulink)
- Validation sur systèmes réels

---

## Documents de Cours

<div class="pdf-container">
  <div class="pdf-viewer">

    <div class="pdf-item">
      <h4>Introduction a l'Automatique</h4>
      <p>Presentation generale du cours d'automatique : definitions, vocabulaire et objectifs.</p>
      <embed src="/cours-pdf/S3/Automatique/C_00_Introduction (1).pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S3/Automatique/C_00_Introduction (1).pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Systemes et Reponses</h4>
      <p>Etude des systemes lineaires et de leurs reponses temporelles et frequentielles.</p>
      <embed src="/cours-pdf/S3/Automatique/C_01_Système_et_Réponses.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S3/Automatique/C_01_Système_et_Réponses.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Formes Canoniques et Systeme Asservi</h4>
      <p>Formes canoniques des systemes, schemas-blocs et principe de l'asservissement.</p>
      <embed src="/cours-pdf/S3/Automatique/C_02_Formes_canoniques_et_Système_asservi.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S3/Automatique/C_02_Formes_canoniques_et_Système_asservi.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Poles et Stabilite</h4>
      <p>Analyse de stabilite par les poles, criteres de Routh-Hurwitz et marges de stabilite.</p>
      <embed src="/cours-pdf/S3/Automatique/C_03_Pôles_et_Stabilité.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S3/Automatique/C_03_Pôles_et_Stabilité.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Precision des Systemes Asservis</h4>
      <p>Etude de la precision en regime permanent, erreur statique et classe des systemes.</p>
      <embed src="/cours-pdf/S3/Automatique/C_04_Précision.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S3/Automatique/C_04_Précision.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Introduction a la Correction</h4>
      <p>Correcteurs P, PI, PID : principes, reglage et methodes de Ziegler-Nichols.</p>
      <embed src="/cours-pdf/S3/Automatique/C_05_Introduction à la correction.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S3/Automatique/C_05_Introduction à la correction.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

  </div>
</div>

---

<style>body{font-family:Arial,sans-serif;background-color:#f4f4f9;color:#333;line-height:1.6}h2,h3,h4,h5{color:#2a7ae2}p{text-align:justify}code{background-color:#f5f5f5;padding:2px 6px;border-radius:3px;font-family:'Courier New',monospace}pre{background-color:#f5f5f5;padding:15px;border-radius:5px;overflow-x:auto}</style>

<div class="back-nav">
  <a href="./my-courses-2021-2022.html">&larr; Retour a Mes Cours 2021-2022</a>
</div>



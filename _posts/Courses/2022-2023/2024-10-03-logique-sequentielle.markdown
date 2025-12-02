---
layout: default
title: "Logique Séquentielle - S5"
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

# 🔄 Logique Séquentielle - S5

**Année**: 2022-2023 (Semestre 5)  
**Crédits**: 3 ECTS  
**Type**: Électronique Numérique

---

## PART A: PRÉSENTATION GÉNÉRALE

### Objectifs du cours

Le cours de Logique Séquentielle approfondit la conception de circuits numériques dont l'état dépend de l'historique des entrées. Il couvre les machines à états finis (FSM), la conception synchrone et asynchrone, ainsi que les méthodes systématiques de conception de systèmes séquentiels complexes. Ce cours est fondamental pour concevoir des contrôleurs numériques, des protocoles de communication et des systèmes embarqués.

### Compétences visées

- Maîtriser les bascules et éléments de mémorisation
- Concevoir des machines à états finis (Moore et Mealy)
- Analyser et synthétiser des circuits séquentiels
- Gérer les contraintes temporelles et la synchronisation
- Implémenter des contrôleurs complexes
- Optimiser les codages d'états

### Organisation

- **Volume horaire**: 32h (CM: 18h, TD: 14h)
- **Évaluation**: Examen final (70%) + TDs (30%)
- **Semestre**: 5 (2022-2023)
- **Prérequis**: Logique combinatoire, algèbre de Boole

---

## PART B: EXPÉRIENCE, CONTEXTE ET FONCTION

### Contenu pédagogique

#### 1. Éléments de Mémorisation

**Bascules et Latches**:

Les circuits séquentiels utilisent des éléments mémoire pour stocker l'état.

**Latch SR (Set-Reset)**:
```
S R | Q  Q'
----|-------
0 0 | Q  Q'  (mémorisation)
0 1 | 0  1   (reset)
1 0 | 1  0   (set)
1 1 | X  X   (interdit)
```

**Bascule D (Data)**:

La plus utilisée en conception synchrone.
- Sur front montant d'horloge: Q = D
- Mémorise la valeur de D

**Équation caractéristique**: Q(t+1) = D(t)

**Bascule JK**:
```
J K | Q(t+1)
----|--------
0 0 | Q      (mémorisation)
0 1 | 0      (reset)
1 0 | 1      (set)
1 1 | Q'     (toggle)
```

**Bascule T (Toggle)**:

Quand T=1, la sortie bascule: Q(t+1) = Q'(t)

**Contraintes temporelles**:

- **Setup time** (tsu): temps avant front d'horloge où D doit être stable
- **Hold time** (th): temps après front où D doit rester stable
- **Propagation delay** (tpd): délai entre front CLK et changement de Q

#### 2. Machines à États Finis (FSM)

**FSM de Moore**:

Les sorties dépendent uniquement de l'état courant.

Structure:
- États
- Transitions (dépendent des entrées)
- Sorties (fonction de l'état uniquement)

**Exemple: Détecteur de séquence "101"**

Diagramme d'états Moore:
```
S0 (init, out=0) --[1]--> S1 (out=0)
S1 --[0]--> S2 (out=0)
S2 --[1]--> S3 (out=1)  // Séquence détectée!
S3 --[x]--> ...
```

**FSM de Mealy**:

Les sorties dépendent de l'état ET des entrées.

Avantage: souvent moins d'états que Moore.

**Comparaison**:
- Moore: sorties stables (changent seulement sur front d'horloge)
- Mealy: réaction plus rapide (sorties changent avec entrées)

#### 3. Méthodologie de Conception

**Étapes de conception d'une FSM**:

1. **Spécification**: définir le comportement souhaité
2. **Diagramme d'états**: représentation graphique
3. **Table d'états**: forme tabulaire
4. **Minimisation**: réduire le nombre d'états
5. **Codage d'états**: assigner codes binaires
6. **Équations logiques**: dériver next-state et output logic
7. **Implémentation**: bascules + portes logiques

**Exemple: Contrôleur de feu tricolore**

États:
- VERT (30s)
- ORANGE (5s)
- ROUGE (35s)

Entrées: timer, capteur véhicule
Sorties: LED_V, LED_O, LED_R

**Table d'états simplifiée**:
```
État actuel | Timer | État suivant | Sorties
------------|-------|--------------|----------
VERT        | 0     | VERT         | V=1,O=0,R=0
VERT        | 1     | ORANGE       | V=1,O=0,R=0
ORANGE      | 0     | ORANGE       | V=0,O=1,R=0
ORANGE      | 1     | ROUGE        | V=0,O=1,R=0
ROUGE       | 0     | ROUGE        | V=0,O=0,R=1
ROUGE       | 1     | VERT         | V=0,O=0,R=1
```

#### 4. Codage d'États

**Binaire naturel**:
- n bits pour 2^n états
- Exemple 4 états: 00, 01, 10, 11
- Économie de bascules

**One-Hot**:
- 1 bascule par état
- Exemple 4 états: 0001, 0010, 0100, 1000
- Logique de décodage simplifiée
- Utilisé en FPGA

**Gray**:
- 1 seul bit change entre états adjacents
- Réduit les aléas (glitches)
- Utile en asynchrone

**Exemple 4 états**:
```
État | Binaire | One-Hot | Gray
-----|---------|---------|------
S0   | 00      | 0001    | 00
S1   | 01      | 0010    | 01
S2   | 10      | 0100    | 11
S3   | 11      | 1000    | 10
```

#### 5. Conception Synchrone

**Règles de conception synchrone**:

- Toutes les bascules partagent la même horloge
- Pas de logique combinatoire dans le chemin d'horloge
- Respecter les contraintes setup/hold

**Fréquence maximale**:

fmax = 1 / (tpd_logic + tsu + tskew)

où:
- tpd_logic: délai combinatoire entre bascules
- tsu: setup time
- tskew: décalage d'horloge (clock skew)

**Stratégies de reset**:

**Reset asynchrone**:
```vhdl
if (reset = '1') then
    state <= S0;
elsif rising_edge(clk) then
    state <= next_state;
end if;
```

Avantage: réinitialisation immédiate
Inconvénient: peut causer métastabilité

**Reset synchrone**:
```vhdl
if rising_edge(clk) then
    if (reset = '1') then
        state <= S0;
    else
        state <= next_state;
    end if;
end if;
```

Avantage: synchronisé avec horloge
Inconvénient: délai d'un cycle

#### 6. Compteurs Avancés

**Compteur modulo-N**:

Compte de 0 à N-1 puis revient à 0.

**Compteur décimal BCD**:
Compte de 0 à 9 (0000 à 1001).

**Compteur up/down**:

Entrée DIR: 1=up, 0=down

**Exemple 3 bits up/down**:
```
UP:   000 -> 001 -> 010 -> 011 -> 100 -> 101 -> 110 -> 111 -> 000
DOWN: 111 -> 110 -> 101 -> 100 -> 011 -> 010 -> 001 -> 000 -> 111
```

**Compteur avec préchargement**:

Entrée LOAD: charge valeur initiale
Utilité: division de fréquence précise

#### 7. Aspects Temporels

**Métastabilité**:

Phénomène lorsque setup/hold time violés.
La bascule peut rester dans état indéterminé.

**Solution**: Synchroniseur à 2 étages
```
Entrée asynchrone -> [FF1] -> [FF2] -> Sortie synchrone
                       CLK      CLK
```

Réduit probabilité de métastabilité à ~10^-12.

**Analyse de chemin critique**:

Identifier le chemin logique le plus long entre deux bascules.

Exemple:
```
FF1 --[tpd=2ns]--> NAND --[tpd=3ns]--> XOR --[tpd=4ns]--> FF2
                                                          [tsu=1ns]
```

Délai total: 2 + 3 + 4 + 1 = 10ns
Fréquence max: 1/10ns = 100MHz

**Supports de cours**:
[Cours Logique Séquentielle](/cours-pdf/S5/Logique-Séquentielle/Poly2022.pdf)


---

## PART C: ASPECTS TECHNIQUES

### Exercices de TD

**TD1: Conception de FSM**

Exercice: Concevoir un détecteur de séquence "1011" (non chevauchant).

**Solution**:

États nécessaires:
- S0: état initial
- S1: après "1"
- S2: après "10"
- S3: après "101"
- S4: séquence complète détectée

Table de transition:
```
État | Entrée 0 | Entrée 1 | Sortie
-----|----------|----------|--------
S0   | S0       | S1       | 0
S1   | S2       | S1       | 0
S2   | S0       | S3       | 0
S3   | S0       | S4       | 0
S4   | S0       | S1       | 1
```

**TD2: Codage et équations**

Pour 4 états codés en binaire:
- Q1 Q0 = 00 (S0), 01 (S1), 10 (S2), 11 (S3)

Dériver équations next-state avec Karnaugh.

**TD3: Analyse temporelle**

Calculer fréquence maximale d'un circuit avec:
- tpd_FF = 5ns
- tpd_comb = 15ns
- tsu = 3ns
- tskew = 1ns

Solution:
Période minimale = 5 + 15 + 3 + 1 = 24ns
fmax = 1/24ns = 41.67MHz

### Applications Pratiques

**Contrôleur UART (émetteur)**:

États:
- IDLE: attente données
- START: envoi bit de start
- DATA0-DATA7: envoi 8 bits de données
- STOP: bit de stop
- Retour IDLE

**Décodeur de protocole I2C**:

FSM détectant:
- Condition START (SDA chute avec SCL=1)
- Adresse (7 bits)
- R/W bit
- ACK/NACK
- Données
- Condition STOP (SDA monte avec SCL=1)

**Contrôleur de distributeur automatique**:

Entrées: pièces insérées (5c, 10c, 25c)
Sortie: produit délivré si montant atteint

États représentent le crédit accumulé.

### Outils de Conception

**Simulateurs**:
- Logisim: simulation graphique
- ModelSim: simulation VHDL/Verilog
- Quartus: suite complète Altera/Intel

**Langages de description**:

**VHDL exemple (FSM Moore)**:
```vhdl
process(clk, reset)
begin
    if reset = '1' then
        state <= S0;
    elsif rising_edge(clk) then
        case state is
            when S0 =>
                if input = '1' then
                    state <= S1;
                end if;
            when S1 =>
                -- transitions...
        end case;
    end if;
end process;

-- Logique de sortie Moore
output <= '1' when state = S3 else '0';
```

**Verilog exemple (FSM Mealy)**:
```verilog
always @(posedge clk or posedge reset) begin
    if (reset)
        state <= S0;
    else
        state <= next_state;
end

// Logique next_state et output (combinatoire)
always @(*) begin
    case (state)
        S0: begin
            if (input)
                next_state = S1;
            output = 1'b0;
        end
        // ...
    endcase
end
```

---

## PART D: ANALYSE ET RÉFLEXION

### Compétences acquises

**Techniques**:
- Conception systématique de FSM
- Optimisation de codage d'états
- Analyse temporelle de circuits séquentiels
- Gestion de la synchronisation
- Implémentation en VHDL/Verilog

**Méthodologiques**:
- Démarche de conception rigoureuse
- Tests et vérification de FSM
- Documentation (diagrammes d'états)
- Débogage de circuits séquentiels

### Applications professionnelles

La logique séquentielle est utilisée dans:
- **Protocoles de communication**: UART, SPI, I2C, USB
- **Contrôleurs**: machines, robots, process industriels
- **Interfaces**: LCD, clavier, souris, touchscreen
- **Processeurs**: unité de contrôle, pipelines
- **Stockage**: contrôleurs de mémoire, cache
- **Réseaux**: routeurs, switches, protocoles

### Connexions avec autres cours

- **Fondements Électronique Numérique** (S5): base (bascules, compteurs)
- **Architectures Numériques VHDL** (S7): implémentation FPGA
- **Microcontrôleurs** (S6): FSM dans firmware
- **Temps Réel** (S8): ordonnancement et synchronisation
- **Réseaux** (S6): protocoles en couches FSM

### Évolution et Perspectives

**Outils modernes**:
- Synthèse automatique depuis FSM graphiques
- Vérification formelle (model checking)
- Génération automatique de tests
- Optimisation multi-objectifs (surface/vitesse/consommation)

**Tendances**:
- FSM hiérarchiques (StateCharts)
- FSM concurrentes
- Langages de haut niveau (SystemVerilog, SystemC)
- Synthèse de haut niveau (HLS)

**Applications émergentes**:
- IoT: contrôleurs ultra-basse consommation
- IA embarquée: FSM pour gestion d'énergie
- Automobile: ADAS, contrôle moteur
- 5G: traitement protocoles temps réel

### Recommandations

1. **Toujours partir du diagramme d'états**: visualisation essentielle
2. **Vérifier tous les cas**: états non utilisés, transitions manquantes
3. **Prévoir état par défaut**: robustesse face aux erreurs
4. **Documenter clairement**: noms d'états explicites
5. **Simuler avant implémentation**: éviter erreurs coûteuses
6. **Respecter contraintes temporelles**: setup/hold critiques

**Pièges à éviter**:
- Boucles combinatoires (feedback sans bascule)
- Aléas (glitches) sur signaux critiques
- Reset incomplet (états non couverts)
- Violations setup/hold time
- Clock gating sans précaution

En conclusion, la logique séquentielle est au cœur de tout système numérique complexe. La maîtrise des FSM et des techniques de conception synchrone est indispensable pour développer des contrôleurs fiables et performants, que ce soit en ASIC, FPGA ou microcontrôleurs.

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

<div class="back-nav">
  <a href="./my-courses-2022-2023.html">← Retour à Mes Cours 2022-2023</a>
</div>



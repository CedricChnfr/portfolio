---
layout: default
title: "Systèmes Bouclés - S5"
date: 2024-10-02 10:56:03 +0200
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
  <a href="./my-courses-2022-2023.html" data-i18n-html="back-courses-2022-2023">← Retour aux Cours 2022-2023</a>
</div>

<!-- ==================== FRENCH VERSION ==================== -->
<div class="lang-fr">

<h1>🔄 Systèmes Bouclés - S5</h1>

<p><strong>Année</strong>: 2022-2023 (Semestre 5)<br/>
<strong>Crédits</strong>: 3 ECTS<br/>
<strong>Type</strong>: Automatique et Régulation</p>

<hr/>

<h2>PART A: PRÉSENTATION GÉNÉRALE</h2>

<h3>Objectifs du cours</h3>

<p>Ce cours traite des systèmes asservis (bouclés) en se concentrant sur l'analyse des performances, la stabilité, et la synthèse de correcteurs. L'accent est mis sur les méthodes classiques de l'automatique (PID, correcteurs fréquentiels) et leur application pratique sur des systèmes réels comme les asservissements de position.</p>

<h3>Compétences visées</h3>

<ul>
  <li>Comprendre les principes de l'asservissement et du retour d'information</li>
  <li>Analyser la stabilité des systèmes bouclés (Routh, Bode, Nyquist)</li>
  <li>Évaluer les performances temporelles et fréquentielles</li>
  <li>Concevoir des correcteurs PID et à avance/retard de phase</li>
  <li>Utiliser le lieu des racines pour la synthèse</li>
  <li>Maîtriser MATLAB pour la simulation d'asservissements</li>
  <li>Dimensionner des correcteurs selon un cahier des charges</li>
  <li>Analyser les compromis stabilité/rapidité/précision</li>
</ul>

<h3>Organisation</h3>

<ul>
  <li><strong>Volume horaire</strong>: Cours magistraux, TD et TP MATLAB</li>
  <li><strong>Évaluation</strong>: Examen écrit + TPs</li>
  <li><strong>Semestre</strong>: 5 (2022-2023)</li>
  <li><strong>Prérequis</strong>: Transformée de Laplace, fonctions de transfert, systèmes linéaires</li>
</ul>

<hr/>

<h2>PART B: EXPÉRIENCE, CONTEXTE ET FONCTION</h2>

<h3>Contenu pédagogique</h3>

<p>Le cours s'articule autour de l'asservissement et de la régulation automatique.</p>

<h4>1. Introduction aux systèmes asservis</h4>

<p><strong>Principe de l'asservissement</strong>:</p>

<p>Un système asservi compare continuellement la sortie (mesurée) à la consigne (référence) et ajuste la commande pour minimiser l'écart (erreur).</p>

<p><strong>Boucle ouverte vs boucle fermée</strong>:</p>

<table>
  <tr><th>Aspect</th><th>Boucle ouverte</th><th>Boucle fermée (asservie)</th></tr>
  <tr><td>Structure</td><td>Pas de retour</td><td>Retour de la sortie</td></tr>
  <tr><td>Précision</td><td>Dépend de la qualité du système</td><td>Compense les perturbations</td></tr>
  <tr><td>Stabilité</td><td>Généralement stable</td><td>Peut devenir instable</td></tr>
  <tr><td>Robustesse</td><td>Sensible aux variations</td><td>Robuste aux perturbations</td></tr>
  <tr><td>Exemple</td><td>Machine à laver</td><td>Thermostat</td></tr>
</table>

<p><strong>Avantages de la boucle fermée</strong>:</p>

<ul>
  <li>Réduction de l'erreur statique</li>
  <li>Réjection des perturbations</li>
  <li>Réduction de la sensibilité aux variations de paramètres</li>
  <li>Amélioration de la dynamique</li>
</ul>

<p><strong>Inconvénients</strong>:</p>

<ul>
  <li>Risque d'instabilité</li>
  <li>Nécessite des capteurs</li>
  <li>Plus complexe à concevoir</li>
</ul>

<p><strong>Structure générale d'un asservissement</strong>:</p>

<p>Composants:</p>
<ul>
  <li><strong>Consigne</strong> (référence): valeur désirée</li>
  <li><strong>Comparateur</strong>: calcule l'erreur = consigne - mesure</li>
  <li><strong>Correcteur</strong>: élabore la commande à partir de l'erreur</li>
  <li><strong>Actionneur</strong>: exécute la commande (moteur, vanne, chauffage)</li>
  <li><strong>Système</strong> (procédé): élément à commander</li>
  <li><strong>Capteur</strong>: mesure la sortie</li>
  <li><strong>Perturbations</strong>: influences externes</li>
</ul>

<h4>2. Analyse temporelle</h4>

<p><strong>Caractéristiques de la réponse indicielle</strong>:</p>

<p>Pour un échelon en entrée, on observe:</p>

<table>
  <tr><th>Paramètre</th><th>Notation</th><th>Description</th></tr>
  <tr><td>Temps de montée</td><td>tm</td><td>Temps pour passer de 10% à 90%</td></tr>
  <tr><td>Temps de réponse</td><td>tr</td><td>Temps pour rester dans 5% de la valeur finale</td></tr>
  <tr><td>Dépassement</td><td>D</td><td>Amplitude du premier pic au-dessus de la valeur finale</td></tr>
  <tr><td>Temps de pic</td><td>tp</td><td>Temps pour atteindre le premier pic</td></tr>
  <tr><td>Erreur statique</td><td>eps</td><td>Écart permanent entre consigne et sortie</td></tr>
</table>

<p><strong>Systèmes du 1er ordre</strong>:</p>

<p>Forme canonique: H(s) = K / (1 + T×s)</p>

<p>Caractéristiques:</p>
<ul>
  <li>Pas de dépassement</li>
  <li>Temps de réponse à 5%: tr = 3×T</li>
  <li>Constante de temps T détermine la rapidité</li>
</ul>

<p><strong>Systèmes du 2nd ordre</strong>:</p>

<p>Forme canonique: H(s) = omega_n² / (s² + 2×zeta×omega_n×s + omega_n²)</p>

<p>Paramètres:</p>
<ul>
  <li><strong>omega_n</strong>: pulsation naturelle (rapidité)</li>
  <li><strong>zeta</strong>: coefficient d'amortissement (oscillations)</li>
</ul>

<p>Comportement selon zeta:</p>
<ul>
  <li>zeta &gt; 1: sur-amorti (lent, pas de dépassement)</li>
  <li>zeta = 1: amorti critique (optimal)</li>
  <li>0 &lt; zeta &lt; 1: sous-amorti (rapide, avec dépassement)</li>
  <li>zeta = 0: oscillations permanentes</li>
</ul>

<p>Dépassement: D = exp(-pi×zeta / sqrt(1-zeta²))</p>

<p>Pour zeta = 0.7: D ≈ 5% (bon compromis)</p>

<p><strong>Erreur statique</strong>:</p>

<p>Dépend de la classe du système en boucle ouverte:</p>

<table>
  <tr><th>Classe</th><th>Intégrateurs</th><th>Erreur échelon</th><th>Erreur rampe</th></tr>
  <tr><td>0</td><td>Aucun</td><td>eps ≠ 0</td><td>Infinie</td></tr>
  <tr><td>1</td><td>1/s</td><td>eps = 0</td><td>eps ≠ 0</td></tr>
  <tr><td>2</td><td>1/s²</td><td>eps = 0</td><td>eps = 0</td></tr>
</table>

<p>Pour réduire l'erreur statique: ajouter un intégrateur (action I du PID).</p>

<h4>3. Stabilité des systèmes bouclés</h4>

<p><strong>Définition</strong>:</p>

<p>Un système est stable si toute entrée bornée produit une sortie bornée (stabilité BIBO).</p>

<p>Condition: tous les pôles de la fonction de transfert en boucle fermée doivent avoir une partie réelle négative.</p>

<p><strong>Critère de Routh-Hurwitz</strong>:</p>

<p>Méthode algébrique pour déterminer la stabilité sans calculer les pôles.</p>

<p>Construction du tableau de Routh à partir du polynôme caractéristique.</p>

<p>Règle: le système est stable si tous les éléments de la première colonne sont strictement positifs.</p>

<p>Avantage: détection de l'instabilité sans résoudre l'équation.</p>

<p><strong>Marges de stabilité</strong>:</p>

<p><strong>Marge de gain (Mg)</strong>:</p>
<ul>
  <li>Gain supplémentaire admissible avant instabilité</li>
  <li>Mesurée à la pulsation où la phase vaut -180°</li>
  <li>Exprimée en dB</li>
  <li>Mg &gt; 6 dB souhaitable</li>
</ul>

<p><strong>Marge de phase (Mphi)</strong>:</p>
<ul>
  <li>Phase supplémentaire admissible avant instabilité</li>
  <li>Mesurée à la pulsation de coupure (gain = 0 dB)</li>
  <li>Exprimée en degrés</li>
  <li>Mphi &gt; 45° souhaitable</li>
</ul>

<p>Plus les marges sont grandes, plus le système est robuste.</p>

<h4>4. Analyse fréquentielle</h4>

<p><strong>Diagrammes de Bode</strong>:</p>

<p>Représentation du gain (en dB) et de la phase (en degrés) en fonction de la fréquence (échelle logarithmique).</p>

<p><strong>Gain en dB</strong>: G_dB = 20×log10(module de H(jw))</p>

<p><strong>Intérêt</strong>:</p>
<ul>
  <li>Visualiser bande passante</li>
  <li>Lire marges de stabilité</li>
  <li>Concevoir correcteurs graphiquement</li>
</ul>

<p><strong>Comportements asymptotiques</strong>:</p>

<table>
  <tr><th>Élément</th><th>Gain (dB/décade)</th><th>Phase</th></tr>
  <tr><td>Gain K</td><td>20×log(K)</td><td>0°</td></tr>
  <tr><td>1/s</td><td>-20</td><td>-90°</td></tr>
  <tr><td>1/(1+T×s)</td><td>0 puis -20</td><td>0° puis -90°</td></tr>
  <tr><td>(1+T×s)</td><td>0 puis +20</td><td>0° puis +90°</td></tr>
</table>

<p><strong>Pulsation de coupure</strong>: fréquence où le gain vaut 0 dB.
Liée à la rapidité du système.</p>

<p><strong>Diagramme de Nyquist</strong>:</p>

<p>Tracé de H(jw) dans le plan complexe quand w varie de 0 à l'infini.</p>

<p><strong>Critère de Nyquist</strong>:
Le système bouclé est stable si le point critique (-1, 0) n'est pas encerclé par la courbe.</p>

<p>Distance au point critique: indicateur de robustesse.</p>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S5/systemes-boucles/systeme-sans-retour.png" alt="Système en boucle ouverte" style="max-width: 600px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Simulation d'un système en boucle ouverte (sans retour)</p>
</div>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S5/systemes-boucles/systeme-avec-retour.png" alt="Système avec retour" style="max-width: 600px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Système avec retour - amélioration de la stabilité et de la précision</p>
</div>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S5/systemes-boucles/correcteur-proportionnel.png" alt="Correcteur proportionnel" style="max-width: 600px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Réponse d'un système avec correcteur proportionnel</p>
</div>

<p><strong>Abaque de Black-Nichols</strong>:</p>

<p>Combinaison gain-phase avec courbes iso-gain et iso-phase en boucle fermée.</p>

<p>Permet de lire directement les performances en boucle fermée à partir de la boucle ouverte.</p>

<h4>5. Correcteurs classiques</h4>

<p><strong>Correcteur Proportionnel (P)</strong>:</p>

<p>Forme: C(s) = Kp</p>

<p>Effet:</p>
<ul>
  <li>Réduit l'erreur statique</li>
  <li>Augmente la rapidité</li>
  <li>Peut dégrader la stabilité (diminue marges)</li>
  <li>Ne supprime pas l'erreur statique</li>
</ul>

<p><strong>Correcteur Proportionnel-Intégral (PI)</strong>:</p>

<p>Forme: C(s) = Kp × (1 + 1/(Ti×s))</p>

<p>Effet:</p>
<ul>
  <li>Annule l'erreur statique (intégrateur)</li>
  <li>Améliore la précision</li>
  <li>Dégrade la marge de phase (retard de phase)</li>
  <li>Ralentit légèrement le système</li>
</ul>

<p><strong>Correcteur Proportionnel-Dérivé (PD)</strong>:</p>

<p>Forme: C(s) = Kp × (1 + Td×s)</p>

<p>Effet:</p>
<ul>
  <li>Améliore la stabilité (avance de phase)</li>
  <li>Augmente la rapidité</li>
  <li>Amplifie le bruit haute fréquence</li>
  <li>N'améliore pas l'erreur statique</li>
</ul>

<p><strong>Correcteur PID</strong>:</p>

<p>Forme: C(s) = Kp × (1 + 1/(Ti×s) + Td×s)</p>

<p>Combinaison des trois actions:</p>
<ul>
  <li><strong>P</strong>: action principale, proportionnelle à l'erreur</li>
  <li><strong>I</strong>: supprime l'erreur statique</li>
  <li><strong>D</strong>: anticipe l'évolution, améliore stabilité</li>
</ul>

<p><strong>Réglage de Ziegler-Nichols (méthode de la boucle fermée)</strong>:</p>

<ol>
  <li>Mettre Ti = infini et Td = 0 (correcteur P)</li>
  <li>Augmenter Kp jusqu'à obtenir des oscillations permanentes</li>
  <li>Noter Kp_critique et période d'oscillation Tu</li>
  <li>Calculer les paramètres selon le type:</li>
</ol>

<table>
  <tr><th>Type</th><th>Kp</th><th>Ti</th><th>Td</th></tr>
  <tr><td>P</td><td>0.5×Kp_critique</td><td>-</td><td>-</td></tr>
  <tr><td>PI</td><td>0.45×Kp_critique</td><td>0.83×Tu</td><td>-</td></tr>
  <tr><td>PID</td><td>0.6×Kp_critique</td><td>0.5×Tu</td><td>0.125×Tu</td></tr>
</table>

<p><strong>Correcteur à avance de phase</strong>:</p>

<p>Forme: C(s) = K × (1 + a×T×s) / (1 + T×s) avec a &gt; 1</p>

<p>Effet:</p>
<ul>
  <li>Apporte une avance de phase (améliore marge de phase)</li>
  <li>Augmente la rapidité</li>
  <li>Permet de stabiliser un système instable</li>
</ul>

<p>Utilisé quand: marge de phase insuffisante ou système trop lent.</p>

<p><strong>Correcteur à retard de phase</strong>:</p>

<p>Forme: C(s) = K × (1 + T×s) / (1 + a×T×s) avec a &gt; 1</p>

<p>Effet:</p>
<ul>
  <li>Augmente le gain basse fréquence</li>
  <li>Réduit l'erreur statique</li>
  <li>Peu d'impact sur la dynamique</li>
</ul>

<p>Utilisé quand: erreur statique trop importante.</p>

<h4>6. Lieu des racines</h4>

<p><strong>Principe</strong>:</p>

<p>Représentation graphique des pôles en boucle fermée quand un paramètre (généralement le gain K) varie de 0 à l'infini.</p>

<p><strong>Utilité</strong>:</p>
<ul>
  <li>Visualiser l'évolution de la stabilité</li>
  <li>Choisir le gain pour placer les pôles</li>
  <li>Identifier les zones de stabilité</li>
  <li>Concevoir des compensateurs</li>
</ul>

<p><strong>Règles de construction</strong>:</p>

<ul>
  <li>Commence aux pôles de H(s) en boucle ouverte (K=0)</li>
  <li>Se termine aux zéros de H(s) (K→∞) ou à l'infini</li>
  <li>Nombre de branches = nombre de pôles</li>
  <li>Symétrie par rapport à l'axe réel</li>
  <li>Asymptotes vers l'infini</li>
</ul>

<p><strong>Pôles dominants</strong>:</p>

<p>Pôles les plus proches de l'axe imaginaire, qui gouvernent principalement la dynamique.</p>

<p>Les pôles éloignés ont moins d'influence sur la réponse temporelle.</p>

<p>Permet de simplifier l'analyse en ne considérant que les pôles dominants.</p>

<hr/>

<h2>PART C: ASPECTS TECHNIQUES</h2>

<h3>Travaux Pratiques</h3>

<p><strong>TP: Asservissement de position d'un bras</strong></p>

<p>Objectif: concevoir un asservissement de position pour un système mécanique.</p>

<p>Système typique: bras robotique avec moteur DC.</p>

<p><strong>Étapes du TP</strong>:</p>

<ol>
  <li><strong>Modélisation</strong>: obtenir la fonction de transfert du système</li>
  <li><strong>Analyse en boucle ouverte</strong>: stabilité, performances</li>
  <li><strong>Étude en boucle fermée</strong>: avec correcteur proportionnel</li>
  <li><strong>Conception de correcteur</strong>: PID ou avance de phase</li>
  <li><strong>Simulation</strong>: validation avec MATLAB/Simulink</li>
  <li><strong>Évaluation</strong>: vérification du cahier des charges</li>
</ol>

<p><strong>Cahier des charges typique</strong>:</p>

<ul>
  <li>Temps de réponse &lt; 0.5 s</li>
  <li>Dépassement &lt; 10%</li>
  <li>Erreur statique nulle</li>
  <li>Marge de phase &gt; 45°</li>
  <li>Rejet de perturbations</li>
</ul>

<h3>Outils MATLAB</h3>

<p><strong>Fonctions de base</strong>:</p>

<pre><code class="language-matlab">% Définir fonction de transfert
num = [1];
den = [1 2 1];
H = tf(num, den);

% Boucle fermée
Hbf = feedback(H, 1);

% Réponse indicielle
step(Hbf);
grid;

% Diagrammes de Bode
bode(H);
margin(H);  % Avec marges

% Lieu des racines
rlocus(H);

% Nyquist
nyquist(H);

% Pôles et zéros
pole(H)
zero(H)</code></pre>

<p><strong>Conception de correcteur PID</strong>:</p>

<pre><code class="language-matlab">% Correcteur PID manuel
Kp = 10;
Ki = 5;
Kd = 2;
C = pid(Kp, Ki, Kd);

% Système corrigé
Hcorrige = C * H;
Hbf = feedback(Hcorrige, 1);

% Validation
step(Hbf);

% Réglage automatique
C_auto = pidtune(H, 'PID');</code></pre>

<p><strong>Analyse de performances</strong>:</p>

<pre><code class="language-matlab">% Informations sur la réponse
info = stepinfo(Hbf);
% Contient: RiseTime, SettlingTime, Overshoot, etc.

% Marges de stabilité
[Gm, Pm, Wcg, Wcp] = margin(H);
fprintf('Marge de phase: %.1f degrés\n', Pm);
fprintf('Marge de gain: %.1f dB\n', 20*log10(Gm));</code></pre>

<h3>Travaux Dirigés</h3>

<p><strong>TD1: Systèmes du 1er et 2nd ordre</strong></p>

<p>Exercices sur:</p>
<ul>
  <li>Calcul de constantes de temps</li>
  <li>Détermination de paramètres (zeta, omega_n)</li>
  <li>Calcul de dépassement et temps de réponse</li>
  <li>Identification à partir de réponse temporelle</li>
</ul>

<p><strong>TD2: Stabilité et précision</strong></p>

<p>Problématiques:</p>
<ul>
  <li>Application du critère de Routh</li>
  <li>Détermination de plage de gains stables</li>
  <li>Calcul d'erreurs statiques</li>
  <li>Choix de correcteurs selon spécifications</li>
</ul>

<p><strong>TD3: Analyse fréquentielle</strong></p>

<p>Exercices sur:</p>
<ul>
  <li>Tracé de diagrammes de Bode asymptotiques</li>
  <li>Lecture de marges de stabilité</li>
  <li>Interprétation de Nyquist</li>
  <li>Conception graphique de correcteurs</li>
</ul>

<p><strong>TD4: Synthèse de correcteurs</strong></p>

<p>Applications:</p>
<ul>
  <li>Réglage de PID par Ziegler-Nichols</li>
  <li>Dimensionnement de correcteur à avance de phase</li>
  <li>Utilisation du lieu des racines</li>
  <li>Validation de cahier des charges</li>
</ul>

<h3>Méthodologie de conception</h3>

<p><strong>Démarche type</strong>:</p>

<ol>
  <li><strong>Analyse du système</strong>: fonction de transfert, pôles, zéros</li>
  <li><strong>Spécifications</strong>: traduire cahier des charges en contraintes techniques</li>
  <li><strong>Choix du correcteur</strong>: selon défauts à corriger</li>
  <li><strong>Dimensionnement</strong>: calcul des paramètres (Kp, Ki, Kd, a, T)</li>
  <li><strong>Simulation</strong>: validation avec MATLAB</li>
  <li><strong>Ajustement</strong>: itérations si nécessaire</li>
  <li><strong>Robustesse</strong>: test avec variations de paramètres</li>
</ol>

<p><strong>Compromis à gérer</strong>:</p>

<table>
  <tr><th>Objectif</th><th>Compromis</th></tr>
  <tr><td>Rapidité vs Stabilité</td><td>Gain élevé accélère mais déstabilise</td></tr>
  <tr><td>Précision vs Robustesse</td><td>Gain élevé améliore précision mais réduit marges</td></tr>
  <tr><td>Filtrage du bruit vs Rapidité</td><td>Dérivée amplifie le bruit</td></tr>
</table>

<p><strong>Règles pratiques</strong>:</p>

<ul>
  <li>Commencer par un P, ajouter I si erreur statique</li>
  <li>Ajouter D si dépassement trop important</li>
  <li>Vérifier marges: Mphi &gt; 45°, Mg &gt; 6 dB</li>
  <li>Tester robustesse avec ±20% de variations</li>
</ul>

<hr/>

<h2>PART D: ANALYSE ET RÉFLEXION</h2>

<h3>Compétences acquises</h3>

<p><strong>Analyse</strong>:</p>
<ul>
  <li>Évaluation de performances temporelles (tr, D, eps)</li>
  <li>Détermination de stabilité (Routh, marges)</li>
  <li>Interprétation de diagrammes fréquentiels</li>
  <li>Identification de systèmes par expérimentation</li>
</ul>

<p><strong>Conception</strong>:</p>
<ul>
  <li>Choix de correcteur adapté au problème</li>
  <li>Dimensionnement de PID</li>
  <li>Synthèse par méthodes fréquentielles</li>
  <li>Optimisation de compromis</li>
</ul>

<p><strong>Outils</strong>:</p>
<ul>
  <li>Maîtrise de MATLAB/Simulink pour l'automatique</li>
  <li>Utilisation de diagrammes (Bode, Nyquist, lieu racines)</li>
  <li>Simulation et validation de lois de commande</li>
</ul>

<h3>Applications industrielles</h3>

<p>Les systèmes asservis sont omniprésents dans l'industrie:</p>

<p><strong>Procédés industriels</strong>:</p>
<ul>
  <li>Régulation de température (fours, réacteurs)</li>
  <li>Contrôle de pression (compresseurs, cuves)</li>
  <li>Régulation de débit (pompes, vannes)</li>
  <li>Contrôle de niveau (réservoirs)</li>
</ul>

<p><strong>Robotique</strong>:</p>
<ul>
  <li>Asservissement de position des articulations</li>
  <li>Contrôle de trajectoire</li>
  <li>Stabilisation (robots équilibrés, drones)</li>
  <li>Contrôle de force (préhension, assemblage)</li>
</ul>

<p><strong>Automobile</strong>:</p>
<ul>
  <li>Régulateur de vitesse (cruise control)</li>
  <li>ABS (antiblocage de roues)</li>
  <li>ESP (contrôle de stabilité)</li>
  <li>Suspension active</li>
</ul>

<p><strong>Aéronautique</strong>:</p>
<ul>
  <li>Pilote automatique</li>
  <li>Contrôle d'attitude (tangage, roulis, lacet)</li>
  <li>Régulation de poussée</li>
  <li>Commandes de vol électriques</li>
</ul>

<p><strong>Électronique de puissance</strong>:</p>
<ul>
  <li>Alimentations à découpage régulées</li>
  <li>Onduleurs pour moteurs</li>
  <li>Redresseurs actifs</li>
  <li>Batteries et chargeurs</li>
</ul>

<h3>Liens avec autres cours</h3>

<table>
  <tr><th>Cours</th><th>Lien</th></tr>
  <tr><td>Modélisation Systèmes Linéaires (S5)</td><td>Représentation d'état, observateurs</td></tr>
  <tr><td>Systèmes Linéaires Continus (S5)</td><td>Fonctions de transfert, Laplace</td></tr>
  <tr><td>Circuits Analogiques (S5)</td><td>Filtres, correcteurs analogiques</td></tr>
  <tr><td>Électronique de Puissance (S6)</td><td>Asservissement de convertisseurs</td></tr>
  <tr><td>Commande Numérique (S8)</td><td>Discrétisation, PID numérique</td></tr>
  <tr><td>Temps Réel (S8)</td><td>Implémentation de régulateurs</td></tr>
</table>

<h3>Différences avec autres cours d'automatique</h3>

<p><strong>Systèmes Bouclés vs Systèmes Linéaires</strong>:</p>

<table>
  <tr><th>Aspect</th><th>Systèmes Bouclés</th><th>Systèmes Linéaires</th></tr>
  <tr><td>Focus</td><td>Asservissement, correcteurs</td><td>Représentation d'état</td></tr>
  <tr><td>Méthodes</td><td>Fréquentielles (Bode, Nyquist)</td><td>Temporelles (placement pôles)</td></tr>
  <tr><td>Outils</td><td>PID, lieu racines</td><td>Retour d'état, observateurs</td></tr>
  <tr><td>Approche</td><td>Classique, industrielle</td><td>Moderne, théorique</td></tr>
</table>

<p>Complémentarité:</p>
<ul>
  <li>Systèmes Bouclés: pratique industrielle immédiate (PID)</li>
  <li>Systèmes Linéaires: théorie moderne pour systèmes complexes</li>
</ul>

<h3>Évolution et perspectives</h3>

<p><strong>Commande avancée</strong>:</p>

<p>Les méthodes classiques restent majoritaires en industrie mais sont complétées par:</p>

<p><strong>Commande optimale</strong>: LQR, LQG (minimisation de critère)</p>

<p><strong>Commande robuste</strong>: H-infini, mu-synthèse (incertitudes)</p>

<p><strong>Commande adaptative</strong>: ajustement automatique des paramètres</p>

<p><strong>Commande prédictive</strong>: MPC (Model Predictive Control)</p>

<p><strong>Intelligence artificielle</strong>:</p>
<ul>
  <li>Réseaux de neurones pour identification</li>
  <li>Apprentissage par renforcement pour optimisation</li>
  <li>Contrôle flou (fuzzy logic)</li>
</ul>

<p><strong>Industrie 4.0</strong>:</p>
<ul>
  <li>Supervision et monitoring en temps réel</li>
  <li>Maintenance prédictive</li>
  <li>Optimisation énergétique</li>
  <li>Jumeau numérique</li>
</ul>

<h3>Mon opinion</h3>

<p>Ce cours est essentiel pour comprendre comment fonctionne la régulation automatique dans les systèmes réels.</p>

<p><strong>Points forts</strong>:</p>
<ul>
  <li>Approche pratique et industrielle</li>
  <li>Outils immédiatement utilisables (PID)</li>
  <li>Méthodes graphiques intuitives (Bode)</li>
  <li>TPs concrets avec systèmes physiques</li>
</ul>

<p><strong>Complémentarité</strong>:</p>

<p>Le PID reste le correcteur le plus utilisé industriellement (&gt;90% des boucles de régulation). Sa simplicité et son efficacité en font un outil incontournable.</p>

<p>La compréhension des compromis stabilité/rapidité/précision est fondamentale pour toute conception de système automatique.</p>

<p><strong>Applications concrètes</strong>:</p>

<p>Les notions apprises s'appliquent directement à:</p>
<ul>
  <li>Thermostat domestique (régulation température)</li>
  <li>Régulateur de vitesse automobile</li>
  <li>Drones et stabilisation</li>
  <li>Robots industriels</li>
  <li>Procédés chimiques</li>
</ul>

<p><strong>Importance professionnelle</strong>:</p>

<p>La maîtrise des asservissements est recherchée dans:</p>
<ul>
  <li>Automatisation industrielle</li>
  <li>Robotique</li>
  <li>Aéronautique</li>
  <li>Automobile</li>
  <li>Électronique de puissance</li>
  <li>Systèmes embarqués</li>
</ul>

<p><strong>Lien avec la pratique</strong>:</p>

<p>Ce cours prépare à:</p>
<ul>
  <li>Régler des régulateurs industriels</li>
  <li>Diagnostiquer problèmes d'instabilité</li>
  <li>Optimiser performances de boucles existantes</li>
  <li>Concevoir nouvelles régulations</li>
</ul>

<hr/>

<p><strong>Bilan personnel</strong>: Ce cours a fourni les outils classiques de l'automatique industrielle. La compréhension du PID et des méthodes fréquentielles est directement applicable en contexte professionnel. La combinaison avec le cours de représentation d'état offre une vision complète de l'automatique moderne. Les TPs sur systèmes réels (asservissement de position) ont permis de confronter théorie et pratique, révélant l'importance des compromis et de la robustesse dans les applications concrètes.</p>

<hr/>

<h2>📚 Documents de Cours</h2>

<p>Voici les supports de cours en PDF pour approfondir les systèmes bouclés :</p>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>📖 Chapitre 1 - Fondamentaux</h4>
      <p>Introduction aux systèmes bouclés, concepts de base de l'automatique et premières notions de commande.</p>
      <embed src="/cours-pdf/S5/Systemes-Boucles/chapitre1.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S5/Systemes-Boucles/chapitre1.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          📥 Télécharger le PDF
        </a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>📊 Chapitre 2 - Analyse et Synthèse</h4>
      <p>Analyse fréquentielle, stabilité, marges de gain et de phase, méthodes de synthèse de correcteurs.</p>
      <embed src="/cours-pdf/S5/Systemes-Boucles/chapitre2.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S5/Systemes-Boucles/chapitre2.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          📥 Télécharger le PDF
        </a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>📈 Chapitre 3 - Diagrammes de Bode</h4>
      <p>Tracé et analyse des diagrammes de Bode, identification de systèmes et réglage de correcteurs.</p>
      <embed src="/cours-pdf/S5/Systemes-Boucles/chapitre3.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S5/Systemes-Boucles/chapitre3.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          📥 Télécharger le PDF
        </a>
      </p>
    </div>
  </div>
</div>

</div>

<!-- ==================== ENGLISH VERSION ==================== -->
<div class="lang-en">

<h1>🔄 Closed-Loop Systems - S5</h1>

<p><strong>Year</strong>: 2022-2023 (Semester 5)<br/>
<strong>Credits</strong>: 3 ECTS<br/>
<strong>Type</strong>: Control Systems and Regulation</p>

<hr/>

<h2>PART A: GENERAL OVERVIEW</h2>

<h3>Course Objectives</h3>

<p>This course covers feedback (closed-loop) systems, focusing on performance analysis, stability, and controller design. Emphasis is placed on classical control methods (PID, frequency-domain controllers) and their practical application to real systems such as position servo systems.</p>

<h3>Targeted Skills</h3>

<ul>
  <li>Understand the principles of feedback control and information return</li>
  <li>Analyze the stability of closed-loop systems (Routh, Bode, Nyquist)</li>
  <li>Evaluate time-domain and frequency-domain performance</li>
  <li>Design PID and lead/lag compensators</li>
  <li>Use root locus for controller synthesis</li>
  <li>Master MATLAB for control system simulation</li>
  <li>Size controllers according to specifications</li>
  <li>Analyze stability/speed/accuracy trade-offs</li>
</ul>

<h3>Organization</h3>

<ul>
  <li><strong>Teaching hours</strong>: Lectures, tutorials (TD) and MATLAB lab sessions (TP)</li>
  <li><strong>Assessment</strong>: Written exam + Lab sessions</li>
  <li><strong>Semester</strong>: 5 (2022-2023)</li>
  <li><strong>Prerequisites</strong>: Laplace transform, transfer functions, linear systems</li>
</ul>

<hr/>

<h2>PART B: EXPERIENCE, CONTEXT AND FUNCTION</h2>

<h3>Course Content</h3>

<p>The course is structured around feedback control and automatic regulation.</p>

<h4>1. Introduction to Feedback Systems</h4>

<p><strong>Feedback control principle</strong>:</p>

<p>A feedback system continuously compares the output (measured) to the setpoint (reference) and adjusts the control input to minimize the error.</p>

<p><strong>Open-loop vs closed-loop</strong>:</p>

<table>
  <tr><th>Aspect</th><th>Open-loop</th><th>Closed-loop (feedback)</th></tr>
  <tr><td>Structure</td><td>No feedback</td><td>Output feedback</td></tr>
  <tr><td>Accuracy</td><td>Depends on system quality</td><td>Compensates for disturbances</td></tr>
  <tr><td>Stability</td><td>Generally stable</td><td>May become unstable</td></tr>
  <tr><td>Robustness</td><td>Sensitive to variations</td><td>Robust to disturbances</td></tr>
  <tr><td>Example</td><td>Washing machine</td><td>Thermostat</td></tr>
</table>

<p><strong>Advantages of closed-loop</strong>:</p>

<ul>
  <li>Reduction of steady-state error</li>
  <li>Disturbance rejection</li>
  <li>Reduced sensitivity to parameter variations</li>
  <li>Improved dynamics</li>
</ul>

<p><strong>Disadvantages</strong>:</p>

<ul>
  <li>Risk of instability</li>
  <li>Requires sensors</li>
  <li>More complex to design</li>
</ul>

<p><strong>General structure of a feedback system</strong>:</p>

<p>Components:</p>
<ul>
  <li><strong>Setpoint</strong> (reference): desired value</li>
  <li><strong>Comparator</strong>: computes error = setpoint - measurement</li>
  <li><strong>Controller</strong>: generates the control signal from the error</li>
  <li><strong>Actuator</strong>: executes the control command (motor, valve, heater)</li>
  <li><strong>Plant</strong> (process): element to be controlled</li>
  <li><strong>Sensor</strong>: measures the output</li>
  <li><strong>Disturbances</strong>: external influences</li>
</ul>

<h4>2. Time-Domain Analysis</h4>

<p><strong>Step response characteristics</strong>:</p>

<p>For a step input, we observe:</p>

<table>
  <tr><th>Parameter</th><th>Notation</th><th>Description</th></tr>
  <tr><td>Rise time</td><td>tr</td><td>Time to go from 10% to 90%</td></tr>
  <tr><td>Settling time</td><td>ts</td><td>Time to remain within 5% of the final value</td></tr>
  <tr><td>Overshoot</td><td>D</td><td>Amplitude of the first peak above the final value</td></tr>
  <tr><td>Peak time</td><td>tp</td><td>Time to reach the first peak</td></tr>
  <tr><td>Steady-state error</td><td>eps</td><td>Permanent deviation between setpoint and output</td></tr>
</table>

<p><strong>First-order systems</strong>:</p>

<p>Canonical form: H(s) = K / (1 + T×s)</p>

<p>Characteristics:</p>
<ul>
  <li>No overshoot</li>
  <li>5% settling time: ts = 3×T</li>
  <li>Time constant T determines the speed</li>
</ul>

<p><strong>Second-order systems</strong>:</p>

<p>Canonical form: H(s) = omega_n² / (s² + 2×zeta×omega_n×s + omega_n²)</p>

<p>Parameters:</p>
<ul>
  <li><strong>omega_n</strong>: natural frequency (speed)</li>
  <li><strong>zeta</strong>: damping ratio (oscillations)</li>
</ul>

<p>Behavior depending on zeta:</p>
<ul>
  <li>zeta &gt; 1: overdamped (slow, no overshoot)</li>
  <li>zeta = 1: critically damped (optimal)</li>
  <li>0 &lt; zeta &lt; 1: underdamped (fast, with overshoot)</li>
  <li>zeta = 0: sustained oscillations</li>
</ul>

<p>Overshoot: D = exp(-pi×zeta / sqrt(1-zeta²))</p>

<p>For zeta = 0.7: D ≈ 5% (good compromise)</p>

<p><strong>Steady-state error</strong>:</p>

<p>Depends on the system type (class) in open-loop:</p>

<table>
  <tr><th>Type</th><th>Integrators</th><th>Step error</th><th>Ramp error</th></tr>
  <tr><td>0</td><td>None</td><td>eps ≠ 0</td><td>Infinite</td></tr>
  <tr><td>1</td><td>1/s</td><td>eps = 0</td><td>eps ≠ 0</td></tr>
  <tr><td>2</td><td>1/s²</td><td>eps = 0</td><td>eps = 0</td></tr>
</table>

<p>To reduce steady-state error: add an integrator (I action of PID).</p>

<h4>3. Stability of Closed-Loop Systems</h4>

<p><strong>Definition</strong>:</p>

<p>A system is stable if every bounded input produces a bounded output (BIBO stability).</p>

<p>Condition: all poles of the closed-loop transfer function must have negative real parts.</p>

<p><strong>Routh-Hurwitz criterion</strong>:</p>

<p>Algebraic method to determine stability without computing the poles.</p>

<p>Construction of the Routh table from the characteristic polynomial.</p>

<p>Rule: the system is stable if all elements in the first column are strictly positive.</p>

<p>Advantage: detection of instability without solving the equation.</p>

<p><strong>Stability margins</strong>:</p>

<p><strong>Gain margin (Gm)</strong>:</p>
<ul>
  <li>Additional gain allowable before instability</li>
  <li>Measured at the frequency where the phase equals -180°</li>
  <li>Expressed in dB</li>
  <li>Gm &gt; 6 dB desirable</li>
</ul>

<p><strong>Phase margin (Pm)</strong>:</p>
<ul>
  <li>Additional phase allowable before instability</li>
  <li>Measured at the crossover frequency (gain = 0 dB)</li>
  <li>Expressed in degrees</li>
  <li>Pm &gt; 45° desirable</li>
</ul>

<p>The larger the margins, the more robust the system.</p>

<h4>4. Frequency-Domain Analysis</h4>

<p><strong>Bode diagrams</strong>:</p>

<p>Representation of gain (in dB) and phase (in degrees) as a function of frequency (logarithmic scale).</p>

<p><strong>Gain in dB</strong>: G_dB = 20×log10(|H(jw)|)</p>

<p><strong>Purpose</strong>:</p>
<ul>
  <li>Visualize bandwidth</li>
  <li>Read stability margins</li>
  <li>Design controllers graphically</li>
</ul>

<p><strong>Asymptotic behaviors</strong>:</p>

<table>
  <tr><th>Element</th><th>Gain (dB/decade)</th><th>Phase</th></tr>
  <tr><td>Gain K</td><td>20×log(K)</td><td>0°</td></tr>
  <tr><td>1/s</td><td>-20</td><td>-90°</td></tr>
  <tr><td>1/(1+T×s)</td><td>0 then -20</td><td>0° then -90°</td></tr>
  <tr><td>(1+T×s)</td><td>0 then +20</td><td>0° then +90°</td></tr>
</table>

<p><strong>Crossover frequency</strong>: frequency where the gain equals 0 dB.
Related to the system's speed.</p>

<p><strong>Nyquist diagram</strong>:</p>

<p>Plot of H(jw) in the complex plane as w varies from 0 to infinity.</p>

<p><strong>Nyquist criterion</strong>:
The closed-loop system is stable if the critical point (-1, 0) is not encircled by the curve.</p>

<p>Distance to the critical point: robustness indicator.</p>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S5/systemes-boucles/systeme-sans-retour.png" alt="Open-loop system" style="max-width: 600px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Simulation of an open-loop system (no feedback)</p>
</div>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S5/systemes-boucles/systeme-avec-retour.png" alt="System with feedback" style="max-width: 600px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: System with feedback - improved stability and accuracy</p>
</div>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S5/systemes-boucles/correcteur-proportionnel.png" alt="Proportional controller" style="max-width: 600px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure: Response of a system with proportional controller</p>
</div>

<p><strong>Black-Nichols chart</strong>:</p>

<p>Gain-phase combination with iso-gain and iso-phase curves in closed-loop.</p>

<p>Allows direct reading of closed-loop performance from the open-loop data.</p>

<h4>5. Classical Controllers</h4>

<p><strong>Proportional Controller (P)</strong>:</p>

<p>Form: C(s) = Kp</p>

<p>Effect:</p>
<ul>
  <li>Reduces steady-state error</li>
  <li>Increases speed</li>
  <li>May degrade stability (reduces margins)</li>
  <li>Does not eliminate steady-state error</li>
</ul>

<p><strong>Proportional-Integral Controller (PI)</strong>:</p>

<p>Form: C(s) = Kp × (1 + 1/(Ti×s))</p>

<p>Effect:</p>
<ul>
  <li>Eliminates steady-state error (integrator)</li>
  <li>Improves accuracy</li>
  <li>Degrades phase margin (phase lag)</li>
  <li>Slightly slows down the system</li>
</ul>

<p><strong>Proportional-Derivative Controller (PD)</strong>:</p>

<p>Form: C(s) = Kp × (1 + Td×s)</p>

<p>Effect:</p>
<ul>
  <li>Improves stability (phase lead)</li>
  <li>Increases speed</li>
  <li>Amplifies high-frequency noise</li>
  <li>Does not improve steady-state error</li>
</ul>

<p><strong>PID Controller</strong>:</p>

<p>Form: C(s) = Kp × (1 + 1/(Ti×s) + Td×s)</p>

<p>Combination of three actions:</p>
<ul>
  <li><strong>P</strong>: main action, proportional to the error</li>
  <li><strong>I</strong>: eliminates steady-state error</li>
  <li><strong>D</strong>: anticipates evolution, improves stability</li>
</ul>

<p><strong>Ziegler-Nichols tuning (closed-loop method)</strong>:</p>

<ol>
  <li>Set Ti = infinity and Td = 0 (P controller)</li>
  <li>Increase Kp until sustained oscillations are obtained</li>
  <li>Record Kp_critical and oscillation period Tu</li>
  <li>Calculate parameters according to type:</li>
</ol>

<table>
  <tr><th>Type</th><th>Kp</th><th>Ti</th><th>Td</th></tr>
  <tr><td>P</td><td>0.5×Kp_critical</td><td>-</td><td>-</td></tr>
  <tr><td>PI</td><td>0.45×Kp_critical</td><td>0.83×Tu</td><td>-</td></tr>
  <tr><td>PID</td><td>0.6×Kp_critical</td><td>0.5×Tu</td><td>0.125×Tu</td></tr>
</table>

<p><strong>Lead compensator</strong>:</p>

<p>Form: C(s) = K × (1 + a×T×s) / (1 + T×s) with a &gt; 1</p>

<p>Effect:</p>
<ul>
  <li>Provides phase lead (improves phase margin)</li>
  <li>Increases speed</li>
  <li>Can stabilize an unstable system</li>
</ul>

<p>Used when: insufficient phase margin or system too slow.</p>

<p><strong>Lag compensator</strong>:</p>

<p>Form: C(s) = K × (1 + T×s) / (1 + a×T×s) with a &gt; 1</p>

<p>Effect:</p>
<ul>
  <li>Increases low-frequency gain</li>
  <li>Reduces steady-state error</li>
  <li>Little impact on dynamics</li>
</ul>

<p>Used when: steady-state error too large.</p>

<h4>6. Root Locus</h4>

<p><strong>Principle</strong>:</p>

<p>Graphical representation of closed-loop poles as a parameter (typically the gain K) varies from 0 to infinity.</p>

<p><strong>Purpose</strong>:</p>
<ul>
  <li>Visualize stability evolution</li>
  <li>Choose the gain to place the poles</li>
  <li>Identify stability regions</li>
  <li>Design compensators</li>
</ul>

<p><strong>Construction rules</strong>:</p>

<ul>
  <li>Starts at the open-loop poles of H(s) (K=0)</li>
  <li>Ends at the zeros of H(s) (K→∞) or at infinity</li>
  <li>Number of branches = number of poles</li>
  <li>Symmetry with respect to the real axis</li>
  <li>Asymptotes toward infinity</li>
</ul>

<p><strong>Dominant poles</strong>:</p>

<p>Poles closest to the imaginary axis, which primarily govern the dynamics.</p>

<p>Distant poles have less influence on the time response.</p>

<p>Allows simplifying the analysis by considering only the dominant poles.</p>

<hr/>

<h2>PART C: TECHNICAL ASPECTS</h2>

<h3>Lab Sessions</h3>

<p><strong>Lab: Position control of a robotic arm</strong></p>

<p>Objective: design a position control system for a mechanical system.</p>

<p>Typical system: robotic arm with DC motor.</p>

<p><strong>Lab steps</strong>:</p>

<ol>
  <li><strong>Modeling</strong>: obtain the system transfer function</li>
  <li><strong>Open-loop analysis</strong>: stability, performance</li>
  <li><strong>Closed-loop study</strong>: with proportional controller</li>
  <li><strong>Controller design</strong>: PID or lead compensator</li>
  <li><strong>Simulation</strong>: validation with MATLAB/Simulink</li>
  <li><strong>Evaluation</strong>: verification against specifications</li>
</ol>

<p><strong>Typical specifications</strong>:</p>

<ul>
  <li>Settling time &lt; 0.5 s</li>
  <li>Overshoot &lt; 10%</li>
  <li>Zero steady-state error</li>
  <li>Phase margin &gt; 45°</li>
  <li>Disturbance rejection</li>
</ul>

<h3>MATLAB Tools</h3>

<p><strong>Basic functions</strong>:</p>

<pre><code class="language-matlab">% Define transfer function
num = [1];
den = [1 2 1];
H = tf(num, den);

% Closed-loop
Hcl = feedback(H, 1);

% Step response
step(Hcl);
grid;

% Bode diagrams
bode(H);
margin(H);  % With margins

% Root locus
rlocus(H);

% Nyquist
nyquist(H);

% Poles and zeros
pole(H)
zero(H)</code></pre>

<p><strong>PID controller design</strong>:</p>

<pre><code class="language-matlab">% Manual PID controller
Kp = 10;
Ki = 5;
Kd = 2;
C = pid(Kp, Ki, Kd);

% Corrected system
Hcorrected = C * H;
Hcl = feedback(Hcorrected, 1);

% Validation
step(Hcl);

% Automatic tuning
C_auto = pidtune(H, 'PID');</code></pre>

<p><strong>Performance analysis</strong>:</p>

<pre><code class="language-matlab">% Step response information
info = stepinfo(Hcl);
% Contains: RiseTime, SettlingTime, Overshoot, etc.

% Stability margins
[Gm, Pm, Wcg, Wcp] = margin(H);
fprintf('Phase margin: %.1f degrees\n', Pm);
fprintf('Gain margin: %.1f dB\n', 20*log10(Gm));</code></pre>

<h3>Tutorials</h3>

<p><strong>Tutorial 1: First and second-order systems</strong></p>

<p>Exercises on:</p>
<ul>
  <li>Time constant calculation</li>
  <li>Parameter determination (zeta, omega_n)</li>
  <li>Overshoot and settling time calculation</li>
  <li>Identification from time response</li>
</ul>

<p><strong>Tutorial 2: Stability and accuracy</strong></p>

<p>Topics:</p>
<ul>
  <li>Applying the Routh criterion</li>
  <li>Determining stable gain ranges</li>
  <li>Steady-state error calculation</li>
  <li>Controller selection based on specifications</li>
</ul>

<p><strong>Tutorial 3: Frequency-domain analysis</strong></p>

<p>Exercises on:</p>
<ul>
  <li>Asymptotic Bode diagram plotting</li>
  <li>Reading stability margins</li>
  <li>Nyquist interpretation</li>
  <li>Graphical controller design</li>
</ul>

<p><strong>Tutorial 4: Controller synthesis</strong></p>

<p>Applications:</p>
<ul>
  <li>PID tuning using Ziegler-Nichols</li>
  <li>Lead compensator sizing</li>
  <li>Root locus usage</li>
  <li>Specification verification</li>
</ul>

<h3>Design Methodology</h3>

<p><strong>Typical approach</strong>:</p>

<ol>
  <li><strong>System analysis</strong>: transfer function, poles, zeros</li>
  <li><strong>Specifications</strong>: translate requirements into technical constraints</li>
  <li><strong>Controller selection</strong>: based on defects to correct</li>
  <li><strong>Sizing</strong>: parameter calculation (Kp, Ki, Kd, a, T)</li>
  <li><strong>Simulation</strong>: validation with MATLAB</li>
  <li><strong>Adjustment</strong>: iterations if necessary</li>
  <li><strong>Robustness</strong>: testing with parameter variations</li>
</ol>

<p><strong>Trade-offs to manage</strong>:</p>

<table>
  <tr><th>Objective</th><th>Trade-off</th></tr>
  <tr><td>Speed vs Stability</td><td>High gain speeds up but destabilizes</td></tr>
  <tr><td>Accuracy vs Robustness</td><td>High gain improves accuracy but reduces margins</td></tr>
  <tr><td>Noise filtering vs Speed</td><td>Derivative amplifies noise</td></tr>
</table>

<p><strong>Practical rules</strong>:</p>

<ul>
  <li>Start with P, add I if there is steady-state error</li>
  <li>Add D if overshoot is too large</li>
  <li>Check margins: Pm &gt; 45°, Gm &gt; 6 dB</li>
  <li>Test robustness with ±20% variations</li>
</ul>

<hr/>

<h2>PART D: ANALYSIS AND REFLECTION</h2>

<h3>Acquired Skills</h3>

<p><strong>Analysis</strong>:</p>
<ul>
  <li>Time-domain performance evaluation (ts, D, eps)</li>
  <li>Stability determination (Routh, margins)</li>
  <li>Frequency diagram interpretation</li>
  <li>System identification through experimentation</li>
</ul>

<p><strong>Design</strong>:</p>
<ul>
  <li>Selecting the appropriate controller for the problem</li>
  <li>PID sizing</li>
  <li>Synthesis using frequency methods</li>
  <li>Trade-off optimization</li>
</ul>

<p><strong>Tools</strong>:</p>
<ul>
  <li>Proficiency in MATLAB/Simulink for control systems</li>
  <li>Use of diagrams (Bode, Nyquist, root locus)</li>
  <li>Simulation and validation of control laws</li>
</ul>

<h3>Industrial Applications</h3>

<p>Feedback systems are ubiquitous in industry:</p>

<p><strong>Industrial processes</strong>:</p>
<ul>
  <li>Temperature regulation (furnaces, reactors)</li>
  <li>Pressure control (compressors, tanks)</li>
  <li>Flow regulation (pumps, valves)</li>
  <li>Level control (reservoirs)</li>
</ul>

<p><strong>Robotics</strong>:</p>
<ul>
  <li>Joint position control</li>
  <li>Trajectory control</li>
  <li>Stabilization (balanced robots, drones)</li>
  <li>Force control (gripping, assembly)</li>
</ul>

<p><strong>Automotive</strong>:</p>
<ul>
  <li>Cruise control</li>
  <li>ABS (anti-lock braking system)</li>
  <li>ESP (electronic stability program)</li>
  <li>Active suspension</li>
</ul>

<p><strong>Aerospace</strong>:</p>
<ul>
  <li>Autopilot</li>
  <li>Attitude control (pitch, roll, yaw)</li>
  <li>Thrust regulation</li>
  <li>Fly-by-wire controls</li>
</ul>

<p><strong>Power electronics</strong>:</p>
<ul>
  <li>Regulated switching power supplies</li>
  <li>Motor inverters</li>
  <li>Active rectifiers</li>
  <li>Batteries and chargers</li>
</ul>

<h3>Links with Other Courses</h3>

<table>
  <tr><th>Course</th><th>Connection</th></tr>
  <tr><td>Linear Systems Modeling (S5)</td><td>State-space representation, observers</td></tr>
  <tr><td>Continuous Linear Systems (S5)</td><td>Transfer functions, Laplace</td></tr>
  <tr><td>Analog Circuits (S5)</td><td>Filters, analog controllers</td></tr>
  <tr><td>Power Electronics (S6)</td><td>Converter control</td></tr>
  <tr><td>Digital Control (S8)</td><td>Discretization, digital PID</td></tr>
  <tr><td>Real-Time Systems (S8)</td><td>Controller implementation</td></tr>
</table>

<h3>Differences with Other Control Courses</h3>

<p><strong>Closed-Loop Systems vs Linear Systems</strong>:</p>

<table>
  <tr><th>Aspect</th><th>Closed-Loop Systems</th><th>Linear Systems</th></tr>
  <tr><td>Focus</td><td>Feedback control, controllers</td><td>State-space representation</td></tr>
  <tr><td>Methods</td><td>Frequency-domain (Bode, Nyquist)</td><td>Time-domain (pole placement)</td></tr>
  <tr><td>Tools</td><td>PID, root locus</td><td>State feedback, observers</td></tr>
  <tr><td>Approach</td><td>Classical, industrial</td><td>Modern, theoretical</td></tr>
</table>

<p>Complementarity:</p>
<ul>
  <li>Closed-Loop Systems: immediate industrial practice (PID)</li>
  <li>Linear Systems: modern theory for complex systems</li>
</ul>

<h3>Evolution and Perspectives</h3>

<p><strong>Advanced control</strong>:</p>

<p>Classical methods remain predominant in industry but are complemented by:</p>

<p><strong>Optimal control</strong>: LQR, LQG (criterion minimization)</p>

<p><strong>Robust control</strong>: H-infinity, mu-synthesis (uncertainties)</p>

<p><strong>Adaptive control</strong>: automatic parameter adjustment</p>

<p><strong>Predictive control</strong>: MPC (Model Predictive Control)</p>

<p><strong>Artificial intelligence</strong>:</p>
<ul>
  <li>Neural networks for identification</li>
  <li>Reinforcement learning for optimization</li>
  <li>Fuzzy logic control</li>
</ul>

<p><strong>Industry 4.0</strong>:</p>
<ul>
  <li>Real-time supervision and monitoring</li>
  <li>Predictive maintenance</li>
  <li>Energy optimization</li>
  <li>Digital twin</li>
</ul>

<h3>My Opinion</h3>

<p>This course is essential to understand how automatic regulation works in real systems.</p>

<p><strong>Strengths</strong>:</p>
<ul>
  <li>Practical and industry-oriented approach</li>
  <li>Immediately usable tools (PID)</li>
  <li>Intuitive graphical methods (Bode)</li>
  <li>Hands-on lab sessions with physical systems</li>
</ul>

<p><strong>Complementarity</strong>:</p>

<p>PID remains the most widely used controller in industry (&gt;90% of control loops). Its simplicity and effectiveness make it an indispensable tool.</p>

<p>Understanding stability/speed/accuracy trade-offs is fundamental for any control system design.</p>

<p><strong>Practical applications</strong>:</p>

<p>The concepts learned apply directly to:</p>
<ul>
  <li>Home thermostat (temperature regulation)</li>
  <li>Automotive cruise control</li>
  <li>Drones and stabilization</li>
  <li>Industrial robots</li>
  <li>Chemical processes</li>
</ul>

<p><strong>Professional importance</strong>:</p>

<p>Mastery of feedback control is sought after in:</p>
<ul>
  <li>Industrial automation</li>
  <li>Robotics</li>
  <li>Aerospace</li>
  <li>Automotive</li>
  <li>Power electronics</li>
  <li>Embedded systems</li>
</ul>

<p><strong>Link with practice</strong>:</p>

<p>This course prepares for:</p>
<ul>
  <li>Tuning industrial regulators</li>
  <li>Diagnosing instability problems</li>
  <li>Optimizing existing loop performance</li>
  <li>Designing new control systems</li>
</ul>

<hr/>

<p><strong>Personal assessment</strong>: This course provided the classical tools of industrial control engineering. Understanding PID and frequency-domain methods is directly applicable in a professional context. Combined with the state-space representation course, it offers a comprehensive view of modern control theory. Lab sessions on real systems (position control) allowed confronting theory with practice, revealing the importance of trade-offs and robustness in real-world applications.</p>

<hr/>

<h2>📚 Course Documents</h2>

<p>Here are the course materials in PDF to deepen your understanding of closed-loop systems:</p>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>📖 Chapter 1 - Fundamentals</h4>
      <p>Introduction to closed-loop systems, basic control concepts and first notions of feedback control.</p>
      <embed src="/cours-pdf/S5/Systemes-Boucles/chapitre1.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S5/Systemes-Boucles/chapitre1.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          📥 Download PDF
        </a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>📊 Chapter 2 - Analysis and Synthesis</h4>
      <p>Frequency analysis, stability, gain and phase margins, controller synthesis methods.</p>
      <embed src="/cours-pdf/S5/Systemes-Boucles/chapitre2.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S5/Systemes-Boucles/chapitre2.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          📥 Download PDF
        </a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>📈 Chapter 3 - Bode Diagrams</h4>
      <p>Bode diagram plotting and analysis, system identification and controller tuning.</p>
      <embed src="/cours-pdf/S5/Systemes-Boucles/chapitre3.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S5/Systemes-Boucles/chapitre3.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">
          📥 Download PDF
        </a>
      </p>
    </div>
  </div>
</div>

</div>

<div class="back-nav">
  <a href="./my-courses-2022-2023.html" data-i18n-html="back-courses-2022-2023">← Retour aux Cours 2022-2023</a>
</div>

<em class="lang-fr">Rédigé par Cédric Chanfreau</em><em class="lang-en">Written by Cédric Chanfreau</em>

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
        .pdf-container {
                margin: 40px 0;
                padding: 20px;
                background-color: #f9f9f9;
                border-radius: 8px;
        }
        .pdf-viewer {
                display: flex;
                flex-wrap: wrap;
                gap: 20px;
                margin-top: 20px;
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
                margin-top: 0;
                color: #2a7ae2;
                border-bottom: 2px solid #2a7ae2;
                padding-bottom: 10px;
        }
</style>

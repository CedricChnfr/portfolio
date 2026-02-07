---
layout: default
title: "Travaux de Laboratoire (TL) - S2"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
---

<style>
.back-nav { margin-bottom: 20px; }
.back-nav a { text-decoration: none; color: #2a7ae2; font-weight: 600; }
.back-nav a:hover { text-decoration: underline; }
.section-title { color: #2a7ae2; border-bottom: 2px solid #2a7ae2; padding-bottom: 10px; margin-top: 30px; margin-bottom: 20px; }
</style>

<div class="back-nav">
  <a href="./my-courses-2020-2021.html">&larr; Retour a Mes Cours 2020-2021</a>
</div>

# Travaux de Laboratoire (TL) - S2

**Annee**: 2020-2021 | **Semestre**: 2 | **Type**: Pratique / Laboratoire

---

## PART A : PRESENTATION GENERALE

### Contexte et objectifs

Les Travaux de Laboratoire du semestre 2 constituent le volet pratique essentiel de la formation GEII. Ils permettent de confronter la theorie etudiee en cours (Systemes Electroniques, Mathematiques, Outils Logiciels) a la realite des montages et mesures en laboratoire. Le S2 approfondit les competences acquises au S1 en abordant des systemes plus complexes : circuits triphases, amplificateurs operationnels en regime sinusoidal, filtres passifs et actifs du premier et second ordre, modulation d'amplitude et capteurs.

Les TPs sont organises en trois series thematiques, chacune comprenant trois a quatre seances de travaux pratiques. Chaque serie explore un domaine specifique de l'electronique et de l'electrotechnique, avec une progression du simple vers le complexe.

**Objectifs pedagogiques :**
- Approfondir la manipulation d'equipements de mesure (oscilloscopes, generateurs, multimetres)
- Valider experimentalement les concepts theoriques etudies en cours
- Developper l'autonomie et la rigueur en laboratoire
- Analyser des systemes complets avec plusieurs composants
- Rediger des comptes-rendus techniques detailles
- Comparer resultats theoriques, simules et experimentaux

### Organisation

Les TPs sont structures en trois series :

**Serie 1** (4 TPs) : Electrotechnique et AOP en regime sinusoidal
- TL1_1 : Triphase (mesures de puissance en triphase)
- TL1_2 : AOP en regime sinusoidal
- TL1_3 : Filtre passif rejecteur (filtre coupe-bande)
- TL1_4 : AOP reel (limitations de l'AOP reel)

**Serie 2** (3 TPs) : Filtres du second ordre
- TL2_1 : Filtre du 2eme ordre - analyse temporelle
- TL2_2 : Filtre du 2eme ordre - analyse frequentielle
- TL2_3 : Filtre actif du 1er ordre

**Serie 3** (3 TPs) : Modulation et capteurs
- TL3_1 : Modulation AM (modulation d'amplitude)
- TL3_2 : Amplificateur d'instrumentation (INA126)
- TL3_3 : Pont de Wheatstone (jauges de contrainte)

Chaque seance dure environ 3 heures et se deroule en binome. Un compte-rendu est attendu apres chaque TP. L'annee 2020-2021 a necessite l'adaptation de certains TPs en format distanciel, avec des simulations et des donnees experimentales fournies.

### Prerequis

- Utilisation de l'oscilloscope et du generateur de fonctions (acquis au S1)
- Lois de Kirchhoff, theoremes de Thevenin et Norton
- Amplificateur operationnel ideal (S1)
- Notions de filtres passifs (S1)
- Calcul de fonctions de transfert (cours SE et OL)

---

## PART B : EXPERIENCE ET CONTEXTE

### Environnement pedagogique

Les TPs du S2 s'appuient sur les connaissances theoriques de plusieurs cours : les Systemes Electroniques (SE) pour la theorie des filtres et des AOP, les Mathematiques pour les equations differentielles et les fonctions de transfert, et les Outils Logiciels (OL) pour l'analyse frequentielle (Fourier, Laplace).

L'annee 2020-2021 a ete fortement impactee par le contexte sanitaire. Plusieurs TPs ont ete realises en format distanciel, avec des sujets adaptes comprenant des simulations, des photos de montages, des captures d'oscilloscope et des mesures pre-enregistrees a analyser. Cette adaptation a permis de maintenir l'acquisition des competences d'analyse, meme si la manipulation directe des equipements a ete reduite.

### Ressources et supports

- **Sujets de TP** : Documents detailles pour chaque seance avec schema de montage, protocole de mesure et questions d'analyse
- **Fiches de mesures** : Formulaires a remplir pendant les manipulations
- **Documentation Moodle** : Complements pour les TPs distanciels (captures, donnees, consignes)
- **Datasheets** : Fiches techniques des composants utilises (TL082, INA126, AN 6N11, MCP6N16, FSR 406)
- **Notes de TP** : Bareme detaille pour la Serie 1

### Liens avec d'autres cours

- **Systemes Electroniques (SE)** : Les fonctions de transfert, les diagrammes de Bode et les filtres etudies en SE sont valides experimentalement en TL.
- **Mathematiques** : Les equations differentielles du 1er et 2eme ordre modelisent les circuits etudies en TP (RC, RLC). Les regimes transitoires (aperiodique, critique, pseudo-periodique) sont observes.
- **Outils Logiciels (OL)** : Les transformees de Laplace et de Fourier donnent le cadre theorique pour analyser les resultats de mesure.
- **Energie** : Le TP triphase fait le lien avec le cours d'energie sur les systemes triphases equilibres et desequilibres.

### Equipements de mesure

Les equipements utilises en laboratoire comprennent :
- Oscilloscopes numeriques (2 et 4 voies) avec curseurs et mesures automatiques
- Generateurs de fonctions arbitraires (sinusoidal, carre, triangle, rampe)
- Alimentations stabilisees continues (simple et double)
- Multimetres numeriques de precision
- Composants passifs (resistances, condensateurs, bobines) et actifs (AOP TL082, INA126)
- Plaques de prototypage et cables de connexion
- Capteurs : jauges de contrainte (FSR 406), capteurs de force

---

## PART C : ASPECTS TECHNIQUES

### Serie 1 : Electrotechnique et AOP en regime sinusoidal

#### TL1_1 : Mesures en triphase

**Objectif** : Realiser des mesures de puissance sur un systeme triphase equilibre et desequilibre.

**Principe** : Un systeme triphase est constitue de trois tensions sinusoidales de meme amplitude et de meme frequence, dephasees de 120 degres les unes par rapport aux autres :
- v_1(t) = V_max * sin(w*t)
- v_2(t) = V_max * sin(w*t - 2*pi/3)
- v_3(t) = V_max * sin(w*t - 4*pi/3)

**Montages etudies** :
- Montage etoile (Y) : chaque charge est connectee entre une phase et le neutre. La tension aux bornes de chaque charge est la tension simple V (V = U/sqrt(3) ou U est la tension composee).
- Montage triangle (Delta) : chaque charge est connectee entre deux phases. La tension aux bornes de chaque charge est la tension composee U.

**Mesures realisees** :
- Tensions simples et composees a l'oscilloscope
- Verification de la relation U = sqrt(3) * V en systeme equilibre
- Courants de ligne et courants de phase
- Puissance active par la methode des deux wattmetres (theoreme de Blondel)
- Puissance reactive et facteur de puissance

**Formules** :
- Puissance active totale : P = sqrt(3) * U * I * cos(phi)
- Puissance reactive totale : Q = sqrt(3) * U * I * sin(phi)
- Puissance apparente : S = sqrt(3) * U * I
- Methode des deux wattmetres : P = P_1 + P_2 et Q = sqrt(3) * (P_1 - P_2)

#### TL1_2 : AOP en regime sinusoidal

**Objectif** : Etudier le comportement de l'amplificateur operationnel en regime sinusoidal et mesurer ses limitations.

**Montages etudies** :
- Amplificateur inverseur : V_s = -(R_2/R_1) * V_e, gain en dB = 20*log(R_2/R_1)
- Amplificateur non-inverseur : V_s = (1 + R_2/R_1) * V_e
- Sommateur : V_s = -(R_f/R_1 * V_1 + R_f/R_2 * V_2)
- Derivateur et integrateur

**Mesures** :
- Gain en tension en fonction de la frequence (trace du diagramme de Bode)
- Dephasage entre entree et sortie
- Produit gain-bande passante (GBW) : pour le TL082, GBW = 4 MHz environ
- Slew rate (vitesse de balayage) : pour le TL082, SR = 13 V/us environ
- Influence du slew rate sur les signaux a haute frequence et grande amplitude

**Observations** :
- A basse frequence, le gain est constant et conforme a la theorie (AOP ideal)
- Au-dela de la frequence de coupure, le gain diminue de -20 dB/decade
- Le slew rate limite l'amplitude maximale a haute frequence : f_max = SR/(2*pi*V_max)

#### TL1_3 : Filtre passif rejecteur (coupe-bande)

**Objectif** : Realiser et caracteriser un filtre coupe-bande (ou rejecteur de bande) passif.

**Principe** : Un filtre rejecteur laisse passer toutes les frequences sauf une bande centree sur la frequence de rejection f_0. Il est typiquement realise avec un circuit RLC serie ou une cellule en T a double T.

**Circuit etudie** : Circuit RLC serie avec sortie aux bornes de la resistance.

**Fonction de transfert** :
H(j*w) = (R) / (R + j*(L*w - 1/(C*w)))

Le module est : |H(j*w)| = R / sqrt(R^2 + (L*w - 1/(C*w))^2)

A la frequence de resonance f_0 = 1/(2*pi*sqrt(LC)) :
- L*w_0 = 1/(C*w_0), donc |H(j*w_0)| = 1 (maximum)
- Pour un filtre rejecteur, on prend la sortie sur L+C en serie

**Mesures** :
- Trace du diagramme de Bode (gain et phase) point par point
- Determination de la frequence de rejection
- Mesure de la bande passante a -3 dB
- Calcul du facteur de qualite Q = f_0 / (f_2 - f_1) = (1/R)*sqrt(L/C)
- Comparaison theorie / mesure

#### TL1_4 : AOP reel - Limitations

**Objectif** : Mettre en evidence et quantifier les limitations de l'amplificateur operationnel reel par rapport au modele ideal.

**Limitations etudiees** :

**Tension d'offset (V_os)** : L'AOP reel presente une tension de decalage en entree (typiquement quelques mV pour le TL082). Cette tension provoque une tension de sortie non nulle meme quand l'entree est nulle.
- Mesure : connecter les entrees ensemble a la masse, mesurer V_s. V_os = V_s / gain

**Courants de polarisation (I_b)** : Les entrees de l'AOP reel absorbent un faible courant (quelques pA a quelques nA pour le TL082, qui a des entrees JFET).
- Mesure : appliquer des resistances de valeurs differentes aux entrees et observer l'effet sur la sortie

**Bande passante et produit gain-bande** : Le gain en boucle ouverte diminue avec la frequence. En boucle fermee, la bande passante est : BP = GBW / gain
- Mesure : tracer le gain en fonction de la frequence pour differentes valeurs de gain en boucle fermee

**Slew rate** : Vitesse maximale de variation de la tension de sortie.
- Mesure : appliquer un signal carre a l'entree et observer le temps de montee de la sortie. SR = delta_V / delta_t

**Saturation de sortie** : La tension de sortie est limitee par l'alimentation : V_s_max = V_cc - V_sat (typiquement 1 a 2 V en dessous de V_cc)

### Serie 2 : Filtres du second ordre

#### TL2_1 : Filtre du 2eme ordre - Analyse temporelle

**Objectif** : Etudier la reponse temporelle d'un filtre du second ordre (circuit RLC) a un echelon de tension.

**Circuit** : Circuit RLC serie avec mesure de la tension aux bornes du condensateur u_c(t).

**Equation differentielle** : LC * u_c'' + RC * u_c' + u_c = E

**Parametres** :
- Pulsation propre : w_0 = 1/sqrt(LC)
- Coefficient d'amortissement : z = R/(2*sqrt(L/C))
- Facteur de qualite : Q = 1/(2*z) = (1/R)*sqrt(L/C)

**Manipulations** :
On fait varier R pour obtenir les trois regimes :

**Regime aperiodique (z > 1)** : R grand, la tension u_c(t) monte lentement vers E sans oscillation ni depassement. On observe deux exponentielles dont la plus lente domine le comportement.
- Temps de montee long
- Pas de depassement

**Regime critique (z = 1)** : R = R_c = 2*sqrt(L/C)
- Retour a l'equilibre le plus rapide sans depassement
- R_c est la resistance critique
- La reponse est de la forme : u_c(t) = E * [1 - (1 + w_0*t) * e^(-w_0*t)]

**Regime pseudo-periodique (z < 1)** : R faible, la tension u_c(t) oscille autour de E avec une amplitude decroissante.
- La pseudo-pulsation est w_p = w_0 * sqrt(1 - z^2)
- La pseudo-periode est T_p = 2*pi/w_p
- Le premier depassement est : D_1% = 100 * e^(-pi*z/sqrt(1 - z^2))
- Le nombre d'oscillations visibles depend de z

**Mesures** :
- Identification du regime pour differentes valeurs de R
- Mesure de la pseudo-periode T_p et deduction de w_p
- Mesure du depassement D_1 et deduction de z
- Mesure du temps de reponse a 5% (temps pour rester dans une bande de +/-5% autour de la valeur finale)
- Verification de la resistance critique R_c

#### TL2_2 : Filtre du 2eme ordre - Analyse frequentielle

**Objectif** : Tracer le diagramme de Bode (gain et phase) d'un filtre du second ordre et relier les resultats a l'analyse temporelle.

**Principe** : On applique un signal sinusoidal d'amplitude constante et on fait varier la frequence. Pour chaque frequence, on mesure le gain (rapport des amplitudes sortie/entree) et le dephasage.

**Fonction de transfert du filtre passe-bas du 2eme ordre** :
H(j*w) = 1 / (1 - (w/w_0)^2 + j*2*z*(w/w_0))

**Module** :
|H(j*w)| = 1 / sqrt((1 - (w/w_0)^2)^2 + (2*z*(w/w_0))^2)

**Phase** :
phi(w) = -arctan(2*z*(w/w_0) / (1 - (w/w_0)^2))

**Comportement asymptotique** :
- w << w_0 : |H| = 1 (0 dB), phi = 0
- w = w_0 : |H| = 1/(2*z) = Q, phi = -90 degres
- w >> w_0 : |H| diminue a -40 dB/decade, phi tend vers -180 degres

**Resonance** : Pour z < 1/sqrt(2) (Q > 1/sqrt(2)), il y a une resonance a :
w_r = w_0 * sqrt(1 - 2*z^2)
Avec un gain au pic de : |H|_max = 1/(2*z*sqrt(1 - z^2))

**Mesures** :
- Trace du diagramme de Bode point par point (environ 15-20 frequences)
- Identification de la frequence de coupure a -3 dB
- Mesure de la resonance (si z < 0.707)
- Verification de la pente asymptotique (-40 dB/decade)
- Trace du diagramme de phase
- Comparaison avec les resultats theoriques et temporels

#### TL2_3 : Filtre actif du premier ordre

**Objectif** : Realiser et caracteriser un filtre actif du premier ordre base sur un AOP.

**Filtre passe-bas actif** : Un filtre passe-bas actif du premier ordre est realise avec un AOP en configuration inverseur ou non-inverseur avec un condensateur dans la boucle de retour.

**Montage integrateur inverseur** :
- Entree par R, contre-reaction par C
- H(j*w) = -1/(j*R*C*w) (integrateur pur, instable a basse frequence)
- En pratique, on ajoute une resistance R_2 en parallele de C pour limiter le gain DC

**Montage passe-bas actif inverseur** :
- H(j*w) = -(R_2/R_1) / (1 + j*R_2*C*w)
- Gain a basse frequence : G_0 = R_2/R_1
- Frequence de coupure : f_c = 1/(2*pi*R_2*C)
- Pente au-dela de f_c : -20 dB/decade

**Mesures** :
- Trace du diagramme de Bode (gain et phase)
- Verification du gain a basse frequence
- Mesure de la frequence de coupure a -3 dB
- Verification de la pente asymptotique (-20 dB/decade)
- Comparaison filtre passif RC / filtre actif

### Serie 3 : Modulation et capteurs

#### TL3_1 : Modulation d'amplitude (AM)

**Objectif** : Realiser et observer une modulation d'amplitude a double bande avec porteuse (AM-DBAP).

**Principe** : La modulation d'amplitude consiste a faire varier l'amplitude d'un signal porteur haute frequence f_p en fonction d'un signal modulant basse frequence f_m.

**Signal AM** :
s(t) = A_p * (1 + m * cos(2*pi*f_m*t)) * cos(2*pi*f_p*t)

ou m est l'indice de modulation (0 < m <= 1 pour eviter la surmodulation).

**Spectre du signal AM** :
Le spectre contient trois raies :
- La porteuse a la frequence f_p avec l'amplitude A_p
- La bande laterale inferieure a f_p - f_m avec l'amplitude m*A_p/2
- La bande laterale superieure a f_p + f_m avec l'amplitude m*A_p/2

**Mesures** :
- Observation du signal AM sur l'oscilloscope
- Determination de l'indice de modulation : m = (A_max - A_min)/(A_max + A_min)
- Observation du spectre (si analyseur de spectre disponible)
- Etude de la surmodulation (m > 1) : distorsion du signal
- Demodulation par detection d'enveloppe (diode + RC)

#### TL3_2 : Amplificateur d'instrumentation (INA126)

**Objectif** : Caracteriser un amplificateur d'instrumentation (INA126) et comparer avec un montage discret.

**Principe** : L'amplificateur d'instrumentation est un circuit specialise pour l'amplification de signaux differentiels faibles en presence de bruit de mode commun important. C'est la brique de base des chaines d'acquisition.

**INA126** : Circuit integre Texas Instruments
- Gain ajustable par une seule resistance externe R_G : G = 5 + 80k/R_G
- Taux de rejection du mode commun (CMRR) eleve : typiquement 90 dB a G = 100
- Impedance d'entree tres elevee
- Alimentation simple ou double

**Montage discret equivalent** : Realise avec trois AOP
- Deux AOP en entree (etage differentiel) pour l'impedance d'entree elevee
- Un AOP soustracteur en sortie
- Le gain est regle par une seule resistance entre les deux AOP d'entree

**Mesures** :
- Mesure du gain pour differentes valeurs de R_G
- Verification de la formule G = 5 + 80k/R_G
- Mesure du CMRR : appliquer le meme signal sur les deux entrees et mesurer la sortie residuelle
- CMRR = 20*log(G_diff / G_mc) en dB
- Mesure de la bande passante en fonction du gain
- Comparaison INA126 / montage discret (3 AOP)
- Avantages du circuit integre : simplicite, performance, stabilite

<img src="/assets/images/courses/S2/TL/Ampli_Instrum_discrets_schema (3).jpg" alt="Schema amplificateur d'instrumentation discret" style="max-width: 100%; height: auto;" />
<p style="text-align: center; font-style: italic;">Schema de l'amplificateur d'instrumentation discret a trois AOP</p>

#### TL3_3 : Pont de Wheatstone et jauges de contrainte

**Objectif** : Utiliser un pont de Wheatstone avec des jauges de contrainte pour mesurer une deformation mecanique.

**Principe du pont de Wheatstone** : Le pont de Wheatstone est un circuit de mesure compose de quatre resistances formant un pont. Il est equilibre lorsque R_1/R_2 = R_3/R_4, et dans ce cas la tension de sortie est nulle.

Lorsqu'une ou plusieurs resistances varient (par exemple une jauge de contrainte), le pont se desequilibre et une tension de sortie proportionnelle a la variation apparait.

**Tension de sortie** :
V_s = V_alim * (R_1*R_4 - R_2*R_3) / ((R_1 + R_2)(R_3 + R_4))

Pour une variation delta_R petite devant R :
V_s = V_alim * (delta_R / (4*R)) (en quart de pont)

**Jauges de contrainte** : Une jauge de contrainte est une resistance dont la valeur varie proportionnellement a la deformation mecanique :
delta_R / R = k * epsilon

ou k est le facteur de jauge (typiquement k = 2 pour les jauges metalliques) et epsilon est la deformation.

**Capteur FSR 406** : Capteur de force a resistance variable (Force Sensing Resistor). Sa resistance diminue quand on applique une force. Il est utilise ici pour observer le principe du pont desequilibre.

**Chaine de mesure complete** :
1. Jauge(s) de contrainte dans le pont de Wheatstone
2. Amplificateur d'instrumentation (INA126) pour amplifier le signal differentiel faible
3. Eventuel filtrage pour eliminer le bruit
4. Acquisition numerique

**Mesures** :
- Equilibrage du pont (V_s = 0 sans contrainte)
- Application de forces connues et mesure de V_s
- Trace de la courbe V_s = f(Force)
- Verification de la linearite
- Calcul de la sensibilite du capteur
- Influence du nombre de jauges actives (quart de pont, demi-pont, pont complet)

### Photos de laboratoire

<img src="/assets/images/courses/S2/TL/IMG20201027123442.jpg" alt="Photo du laboratoire - montage electronique" style="max-width: 100%; height: auto;" />
<p style="text-align: center; font-style: italic;">Montage electronique en laboratoire</p>

<img src="/assets/images/courses/S2/TL/IMG20210504153833.jpg" alt="Photo laboratoire - mesures" style="max-width: 100%; height: auto;" />
<p style="text-align: center; font-style: italic;">Mesures sur oscilloscope en laboratoire</p>

<img src="/assets/images/courses/S2/TL/IMG20210504154918.jpg" alt="Photo laboratoire - circuit" style="max-width: 100%; height: auto;" />
<p style="text-align: center; font-style: italic;">Circuit en cours de test</p>

<img src="/assets/images/courses/S2/TL/schema_bande_passante_petits_signaux.jpg" alt="Schema bande passante petits signaux" style="max-width: 100%; height: auto;" />
<p style="text-align: center; font-style: italic;">Schema de la bande passante en petits signaux de l'AOP</p>

<img src="/assets/images/courses/S2/TL/schema_limitation_en_tension.jpg" alt="Schema limitation en tension" style="max-width: 100%; height: auto;" />
<p style="text-align: center; font-style: italic;">Schema illustrant la limitation en tension de l'AOP reel</p>

### Methodologie generale des TPs

**Preparation** :
- Etude du sujet de TP et comprehension des objectifs
- Calculs previsionnels (valeurs theoriques attendues)
- Lecture des datasheets des composants utilises
- Preparation du schema de montage

**Realisation** :
- Cablage methodique et verification avant mise sous tension
- Releve des mesures dans la fiche de mesures
- Captures d'ecran de l'oscilloscope
- Prise de photos du montage
- Analyse en temps reel : coherence des resultats avec la theorie

**Compte-rendu** :
- Introduction et rappels theoriques
- Description du montage et du protocole
- Presentation des resultats (tableaux, courbes)
- Comparaison theorie / mesure et analyse des ecarts
- Conclusion et perspectives

---

## PART D : ANALYSE ET REFLEXION

### Competences acquises

- **Manipulation d'equipements professionnels** : Maitrise des oscilloscopes numeriques, generateurs de fonctions, alimentations et multimetres pour realiser des mesures precises.
- **Montage de circuits** : Capacite a realiser un montage a partir d'un schema electronique, en assurant un cablage fiable et organise.
- **Analyse de resultats experimentaux** : Comparaison systematique entre theorie, simulation et mesure, identification des sources d'ecart et estimation des incertitudes.
- **Filtres et AOP** : Comprehension pratique du comportement des filtres (diagramme de Bode, regimes transitoires) et des limitations de l'AOP reel (offset, slew rate, bande passante).
- **Capteurs et chaines d'acquisition** : Mise en oeuvre d'une chaine de mesure complete, du capteur a l'acquisition numerique.
- **Communication technique** : Redaction de comptes-rendus structures et rigoureux.

### Auto-evaluation

Les TPs du S2 ont ete un moment cle de la formation car ils ont permis de donner un sens concret aux notions theoriques. Voir sur l'oscilloscope les trois regimes d'un circuit RLC (aperiodique, critique, pseudo-periodique) en faisant varier une simple resistance est beaucoup plus marquant que de resoudre l'equation differentielle sur papier.

La serie sur les capteurs (amplificateur d'instrumentation et pont de Wheatstone) a ete particulierement interessante car elle montre comment on passe d'une grandeur physique (force, deformation) a un signal electrique exploitable. C'est exactement ce que font les objets connectes, ce qui a conforte le choix de la coloration ENOC.

Le format distanciel impose par le COVID a ete une contrainte mais aussi un apprentissage : travailler a partir de donnees experimentales fournies a developpe la capacite d'analyse critique des resultats, meme sans avoir realise le montage soi-meme.

### Connexions interdisciplinaires

- **Systemes Electroniques (SE)** : La theorie des filtres et des AOP est validee experimentalement. Le diagramme de Bode trace en TP correspond a la fonction de transfert calculee en SE.
- **Mathematiques** : Les trois regimes du circuit RLC sont l'illustration directe des trois cas de l'equation caracteristique du second ordre (discriminant positif, nul, negatif).
- **Outils Logiciels (OL)** : L'analyse frequentielle (Fourier) et les fonctions de transfert (Laplace) sont les outils theoriques pour comprendre les mesures en TP.
- **Cours futurs** : La chaine de mesure (capteur - pont de Wheatstone - ampli d'instrumentation) est un precurseur des systemes d'acquisition des objets connectes etudies en S5-S9.

### Progression et perspectives

Les TPs du S2 ont complete de maniere essentielle les acquis du S1. La progression va des circuits simples (RC) aux systemes complets (chaine de mesure avec capteur). Les competences acquises -- mesure, analyse, comparaison theorie/pratique -- sont fondamentales pour tout ingenieur en electronique et seront approfondies dans les semestres suivants.

---

## Documents de Cours

<div class="pdf-container">
  <div class="pdf-viewer">

    <div class="pdf-item">
      <h4>TL1_2 - TP Triphase (Distanciel)</h4>
      <p>Sujet du TP sur les mesures en triphase, adapte au format distanciel. Mesures de tensions, courants et puissances en systeme triphase equilibre.</p>
      <embed src="/cours-pdf/S2/TL/TL1_2_Triphase_Distanciel_Texte.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/TL/TL1_2_Triphase_Distanciel_Texte.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>TL1_2 - Feuille de Mesures Triphase</h4>
      <p>Feuille de mesures a completer pour le TP triphase : releve des tensions, courants, puissances et facteurs de puissance.</p>
      <embed src="/cours-pdf/S2/TL/TL_s2_1_2_Triphase_Distanciel_Mesures.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/TL/TL_s2_1_2_Triphase_Distanciel_Mesures.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>TL1_4 - AOP Reel (Distanciel)</h4>
      <p>Sujet du TP sur les limitations de l'AOP reel : tension d'offset, courants de polarisation, slew rate, bande passante et saturation.</p>
      <embed src="/cours-pdf/S2/TL/S2_TL1_4_AOP_Réel_distanciel_2021.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/TL/S2_TL1_4_AOP_Réel_distanciel_2021.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>TL1_4 - Feuille de Mesures AOP Reel</h4>
      <p>Feuille de mesures pour le TP AOP reel : releve des tensions d'offset, gains, bande passante et slew rate.</p>
      <embed src="/cours-pdf/S2/TL/S2_TL1_4_AOP_reel_feuille_mesures_2021.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/TL/S2_TL1_4_AOP_reel_feuille_mesures_2021.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Notes TL S2 - Serie 1</h4>
      <p>Bareme de notation de la Serie 1 des TPs : criteres d'evaluation pour les TPs triphase, AOP sinusoidal, filtre rejecteur et AOP reel.</p>
      <embed src="/cours-pdf/S2/TL/Notes_TL_S2_serie1.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/TL/Notes_TL_S2_serie1.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>TL2 - Filtre du 2eme Ordre Temporel (Distanciel)</h4>
      <p>Sujet du TP sur l'analyse temporelle d'un filtre du second ordre : reponse a un echelon, identification des regimes, mesure du depassement et de la pseudo-periode.</p>
      <embed src="/cours-pdf/S2/TL/S2_TP_2_4_2eme_ordre_temporel_distanciel_2021.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/TL/S2_TP_2_4_2eme_ordre_temporel_distanciel_2021.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>TL2 - Filtre du 2eme Ordre Temporel - Documentation Moodle</h4>
      <p>Documentation complementaire Moodle pour le TP 2eme ordre temporel : donnees experimentales et consignes pour le travail distanciel.</p>
      <embed src="/cours-pdf/S2/TL/S2_TP_2_4_2eme_ordre_temporel_doc_moodle_2021.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/TL/S2_TP_2_4_2eme_ordre_temporel_doc_moodle_2021.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>TL2 - Filtre du 2eme Ordre Frequentiel (Distanciel)</h4>
      <p>Sujet du TP sur l'analyse frequentielle d'un filtre du second ordre : trace du diagramme de Bode, resonance, bande passante et facteur de qualite.</p>
      <embed src="/cours-pdf/S2/TL/S2_TP_2_2_2°ordre_frequentiel_distanciel_2021.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/TL/S2_TP_2_2_2°ordre_frequentiel_distanciel_2021.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>TL2 - Filtre du 2eme Ordre Frequentiel - Documentation Moodle</h4>
      <p>Documentation complementaire Moodle pour le TP 2eme ordre frequentiel : captures d'oscilloscope et donnees de mesure.</p>
      <embed src="/cours-pdf/S2/TL/S2_TP_2_2_2°ordre_frequentiel_doc_moodle_2021.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/TL/S2_TP_2_2_2°ordre_frequentiel_doc_moodle_2021.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>TL2 - Filtre Rejecteur Passif (Distanciel)</h4>
      <p>Sujet du TP sur le filtre passif rejecteur (coupe-bande) : realisation, trace de la reponse frequentielle et mesure du facteur de qualite.</p>
      <embed src="/cours-pdf/S2/TL/S2-TP2-6-filtre-rejecteur_passif_2021_distanciel.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/TL/S2-TP2-6-filtre-rejecteur_passif_2021_distanciel.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>TL2 - Filtre Actif du 1er Ordre (Distanciel)</h4>
      <p>Sujet du TP sur le filtre actif du premier ordre : montage avec AOP, trace du diagramme de Bode et comparaison avec le filtre passif.</p>
      <embed src="/cours-pdf/S2/TL/TL2_6_PremierOrdreActif_Distanciel_Texte.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/TL/TL2_6_PremierOrdreActif_Distanciel_Texte.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>TL2 - Filtre Actif 1er Ordre - Feuille de Mesures</h4>
      <p>Feuille de mesures pour le TP filtre actif du premier ordre.</p>
      <embed src="/cours-pdf/S2/TL/TL2_6_PremierOrdreActif_Distanciel_Feuille_Mesure.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/TL/TL2_6_PremierOrdreActif_Distanciel_Feuille_Mesure.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>TL3 - Modulation AM DBAP</h4>
      <p>Sujet du TP sur la modulation d'amplitude a double bande avec porteuse : realisation du modulateur, mesure de l'indice de modulation et demodulation.</p>
      <embed src="/cours-pdf/S2/TL/TP3_4_modulation_AMDBAP.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/TL/TP3_4_modulation_AMDBAP.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>TL3 - Amplificateur d'Instrumentation INA126</h4>
      <p>Sujet du TP sur l'amplificateur d'instrumentation INA126 : mesure du gain, CMRR, bande passante et comparaison avec un montage discret.</p>
      <embed src="/cours-pdf/S2/TL/TL3-2-Caracterisation_Ampli_Instrum_INA126_distanciel_2021.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/TL/TL3-2-Caracterisation_Ampli_Instrum_INA126_distanciel_2021.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>TL3 - Pont de Wheatstone</h4>
      <p>Sujet du TP sur le pont de Wheatstone avec jauges de contrainte : equilibrage du pont, mesure de force, linearite et sensibilite.</p>
      <embed src="/cours-pdf/S2/TL/TP3_3Pont_Wheatstone_2021.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/TL/TP3_3Pont_Wheatstone_2021.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Datasheet - TL082 (AOP JFET)</h4>
      <p>Fiche technique du TL082 : amplificateur operationnel a entrees JFET utilise dans la plupart des TPs. Caracteristiques : GBW = 4 MHz, SR = 13 V/us, V_os = 5 mV max.</p>
      <embed src="/cours-pdf/S2/TL/TL082.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/TL/TL082.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Datasheet - INA126 (Amplificateur d'Instrumentation)</h4>
      <p>Fiche technique de l'INA126 : amplificateur d'instrumentation Texas Instruments. Gain ajustable par R_G, CMRR eleve, alimentation simple ou double.</p>
      <embed src="/cours-pdf/S2/TL/MCP6N16.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/TL/MCP6N16.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

    <div class="pdf-item">
      <h4>Datasheet - FSR 406 (Capteur de Force)</h4>
      <p>Fiche technique du capteur de force FSR 406 : capteur a resistance variable, caracteristique force-resistance, plage de mesure et integration dans un pont de Wheatstone.</p>
      <embed src="/cours-pdf/S2/TL/fiche_technique_FSR_406.pdf" type="application/pdf" width="100%" height="800px" />
      <p style="text-align: center; margin-top: 10px;">
        <a href="/cours-pdf/S2/TL/fiche_technique_FSR_406.pdf" target="_blank" style="color: #2a7ae2; text-decoration: none; font-weight: 600;">Telecharger le PDF</a>
      </p>
    </div>

  </div>
</div>

---

<style>body{font-family:Arial,sans-serif;background-color:#f4f4f9;color:#333;line-height:1.6}h2,h3,h4,h5{color:#2a7ae2}p{text-align:justify}code{background-color:#f5f5f5;padding:2px 6px;border-radius:3px;font-family:'Courier New',monospace}pre{background-color:#f5f5f5;padding:15px;border-radius:5px;overflow-x:auto}</style>

<div class="back-nav">
  <a href="./my-courses-2020-2021.html">&larr; Retour a Mes Cours 2020-2021</a>
</div>

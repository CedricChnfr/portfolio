---
layout: default
title: "🔐 Sécurité Matérielle - Semestre 7"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
---

<style>
.back-nav {
    margin: 20px 0;
    padding: 10px;
    background-color: #f0f0f0;
    border-radius: 5px;
}

.back-nav a {
    color: #007BFF;
    text-decoration: none;
    font-weight: bold;
}

.back-nav a:hover {
    text-decoration: underline;
}

.section-title {
    color: #007BFF;
    border-bottom: 2px solid #007BFF;
    padding-bottom: 5px;
    margin-top: 20px;
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
    background-color: #007BFF;
    color: white;
}

tr:nth-child(even) {
    background-color: #f2f2f2;
}
</style>

<div class="back-nav">
    <a href="./my-courses-2023-2024.html">← Retour aux Cours 2023-2024</a>
</div>

# 🔐 Sécurité Matérielle - Semestre 7

**Année académique** : 2023-2024  
**ECTS** : 2  
**Catégorie** : Sécurité et Systèmes Embarqués

---

## PART A - Présentation Générale du Module

<h3 class="section-title">Vue d'ensemble</h3>

Ce cours aborde la sécurité matérielle, un domaine essentiel à l'ère des objets connectés et des systèmes embarqués. Il couvre les vulnérabilités physiques des systèmes électroniques, les attaques par canaux auxiliaires, les mécanismes de protection, et les techniques de conception sécurisée pour prévenir l'extraction d'informations sensibles.

**Objectifs pédagogiques** :
- Comprendre les menaces pesant sur la sécurité matérielle
- Maîtriser les attaques par canaux auxiliaires (timing, cache, puissance)
- Analyser les vulnérabilités des implémentations cryptographiques
- Découvrir les attaques par dépassement de tampon et injection de code
- Implémenter des contre-mesures efficaces
- Évaluer la sécurité physique des systèmes embarqués

<h3 class="section-title">Position dans le cursus</h3>

Ce module complète la formation en sécurité :
- **Architecture Matérielle (S6)** : fonctionnement processeurs, caches, mémoires
- **Microcontrôleurs (S6)** : systèmes embarqués, ARM Cortex
- **Systèmes d'Exploitation (S5)** : gestion mémoire, processus
- **Langage C et Assemblage (S5, S6)** : programmation bas niveau

Il prépare à :
- **Embedded IA for IoT (S9)** : sécurité des objets connectés
- **Projets professionnels** : conception de systèmes sécurisés
- **Cybersécurité** : approche globale hardware/software

---

## PART B - Expérience Personnelle et Contexte d'Apprentissage

<h3 class="section-title">Organisation et ressources</h3>

Le module était organisé en cours magistraux et travaux pratiques intensifs :

**Cours magistraux (12h)** :
- Introduction à la sécurité matérielle
- Attaques par canaux auxiliaires (timing, cache, puissance)
- Analyse de la consommation électrique (SPA, DPA, CPA)
- Attaques par injection de fautes
- Vulnérabilités logicielles (buffer overflow, shellcode)
- Contre-mesures matérielles et logicielles

**Travaux pratiques (12h)** :
- **TP1** : Analyse de consommation sur microcontrôleur STM32
- **TP Cache et SCA** : Attaques par analyse de cache, détection d'ouverture de fichiers
- **TP3 Overflow** : Exploitation de dépassements de tampon, shellcode, injection de code
- **TP AES** : Analyse de vulnérabilités dans implémentations OpenSSL

**Ressources** :
- 6 polycopiés de cours (slides, polycopiés détaillés)
- 2 TD avec corrections
- Outils : ChipWhisperer (analyse de puissance), GDB (débogage)
- Code source AES (OpenSSL versions 0.9.7a et 1.1.1t)
- Annales (4 sujets d'examens)

<h3 class="section-title">Méthodologie d'étude</h3>

**Phase 1 : Assimiler les concepts théoriques** :
Comprendre les principes des attaques (canaux auxiliaires, injection de fautes, overflow).

**Phase 2 : Manipuler en TP** :
Réaliser les attaques concrètes pour comprendre leur fonctionnement et leur puissance.

**Phase 3 : Analyser le code** :
Étudier le code vulnérable (AES, programmes C) pour identifier les failles.

**Phase 4 : Concevoir des contre-mesures** :
Réfléchir aux protections possibles et à leurs limites.

**Phase 5 : Développer une vision critique** :
Évaluer la sécurité globale d'un système en considérant tous les vecteurs d'attaque.

<h3 class="section-title">Difficultés rencontrées</h3>

<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/images/courses/S7/securite-materielle/buffer-overflow.svg" alt="Attaque par buffer overflow" style="max-width: 550px; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background: white;" />
  <p style="font-style: italic; color: #666; margin-top: 10px;">Figure : Principe d'une attaque par buffer overflow - Écrasement de l'adresse de retour</p>
</div>

**Complexité des attaques** :
Les attaques par canaux auxiliaires nécessitent des connaissances en électronique, traitement du signal, et statistiques.

**Environnement technique** :
Manipuler des outils spécialisés (ChipWhisperer, oscilloscopes) et du code assembleur requiert de la pratique.

**Équilibre sécurité/performance** :
Concevoir des contre-mesures efficaces sans dégrader les performances est un défi constant.

**Diversité des vulnérabilités** :
La sécurité matérielle couvre un spectre large : du cache au dépassement de tampon, chaque domaine a ses spécificités.

---

## PART C - Aspects Techniques Détaillés

<h3 class="section-title">1. Attaques par canaux auxiliaires</h3>

**Principe général** :

Les attaques par canaux auxiliaires exploitent les fuites d'information physiques lors de l'exécution d'algorithmes :
- Consommation électrique
- Temps d'exécution
- Émissions électromagnétiques
- Contenu du cache

Même si l'algorithme est mathématiquement sûr, son implémentation peut révéler des secrets.

**Attaques temporelles (Timing Attacks)** :

Exploitent les variations du temps d'exécution.

**Exemple classique : Cache timing sur AES** :

AES utilise des tables de substitution (S-box). L'accès à ces tables dépend de la clé et du message.

Si une partie de la table est en cache (accès rapide) et une autre non (accès lent), on peut déduire quelle partie a été accédée en mesurant le temps.

**Attaque** :
1. Mesurer le temps d'exécution pour différents messages
2. Analyser les variations temporelles
3. Déduire quelle partie de la S-box a été accédée
4. Récupérer progressivement les octets de la clé

**Contre-mesures** :
- Implémentations à temps constant (même durée quel que soit l'input)
- Désactivation du cache pour opérations sensibles
- Ajout de bruit temporel (jitter)

**Attaques par analyse de cache** :

Le cache CPU peut révéler des informations sensibles.

**Technique Prime+Probe** :
1. Attaquant remplit le cache avec ses propres données (Prime)
2. Victime exécute opération cryptographique
3. Attaquant mesure quelles lignes de cache ont été évincées (Probe)
4. En déduire les accès mémoire de la victime

**TP réalisé : Détection d'ouverture de fichier** :

Programme spy.c :
- Vide (flush) le cache pour une adresse du fichier cible
- Attend un délai
- Mesure le temps d'accès à cette adresse
- Si temps < seuil : fichier en cache → fichier a été ouvert récemment

Application : espionnage d'activité sans accès système.

**Attaques par analyse de la consommation (Power Analysis)** :

**Simple Power Analysis (SPA)** :

Observation directe de la trace de consommation.

Chaque instruction consomme différemment : multiplication, addition, lecture mémoire ont des signatures distinctes.

**Exemple** : Exponentiation modulaire en RSA :
- Opération "carré" visible
- Opération "carré puis multiplication" visible
- On déduit directement les bits de la clé privée

**Differential Power Analysis (DPA)** :

Analyse statistique sur de nombreuses traces.

Principe :
1. Capturer N traces de consommation pour N messages différents
2. Faire des hypothèses sur une partie de la clé
3. Prédire la consommation pour chaque hypothèse
4. Corréler prédictions avec traces réelles
5. L'hypothèse correcte donne la meilleure corrélation

**Correlation Power Analysis (CPA)** :

Variante améliorée utilisant le coefficient de corrélation de Pearson.

Permet d'attaquer des implémentations plus résistantes.

**TP réalisé : Analyse de consommation sur STM32** :

Programme main.c (TP1) :
- Microcontrôleur exécute des opérations (multiplications répétées)
- Oscilloscope capture la consommation électrique
- Analyse des traces pour identifier les opérations
- Corrélation entre données manipulées et consommation

<h3 class="section-title">2. Attaques par injection de fautes</h3>

**Principe** :

Provoquer volontairement des erreurs lors de l'exécution pour obtenir des informations ou contourner des protections.

**Techniques d'injection** :

| Technique | Description | Effet |
|-----------|-------------|-------|
| Clock glitching | Impulsions sur horloge | Instructions sautées |
| Voltage glitching | Variation tension alimentation | Erreurs calcul |
| Laser | Faisceau laser focalisé | Modification bit mémoire |
| Température | Chauffage/refroidissement | Instabilités |
| EM | Impulsion électromagnétique | Perturbation circuits |

**Exemple : Attaque sur authentification** :

Code vulnérable :
```
if (password == correct_password) {
    grant_access();
} else {
    deny_access();
}
```

Injection de faute au moment du test :
- Le test échoue (mauvais mot de passe)
- Mais la faute inverse le résultat → accès accordé

**Contre-mesures** :
- Redondance (double vérification)
- Codes correcteurs d'erreurs
- Détecteurs de glitches (capteurs de tension/horloge)
- Vérifications de cohérence

<h3 class="section-title">3. Vulnérabilités logicielles : Buffer Overflow</h3>

**Principe** :

Dépassement de tampon : écrire au-delà de la taille allouée d'un buffer, écrasant des données adjacentes (adresse de retour, variables).

**Mécanisme sur la pile (stack)** :

Organisation de la pile lors d'un appel de fonction :
```
[paramètres]
[adresse de retour]
[ancien ebp]
[variables locales]
[buffer]
```

Si on écrit trop dans buffer, on écrase les variables, ebp, et l'adresse de retour.

**Exploitation** :

1. Remplir le buffer avec du code malveillant (shellcode)
2. Écraser l'adresse de retour pour pointer vers le shellcode
3. Quand la fonction retourne, le shellcode s'exécute

**TP réalisé : Exploitation de buffer overflow** :

**Part 1 : Organisation mémoire** :
Analyse de la pile avec GDB, calcul des offsets.

**Part 2 : Exploitation simple** :
Programme vulnérable avec strcpy sans vérification de taille.
Injection pour modifier une variable ou sauter une vérification.

**Part 3 : Injection de shellcode** :

shellcode.c :
```
void shellcode() {
  asm(
    "mov $0x3b, %rax"    // syscall execve
    "mov $0x0, %rdx"
    "movabs $0x0068732f6e69622f, %r8"  // "/bin/sh"
    "push %r8"
    "mov %rsp, %rdi"     // adresse de "/bin/sh"
    "syscall"            // execve("/bin/sh", ...)
  );
}
```

Objectif : injecter ce code et rediriger l'exécution pour ouvrir un shell.

**Part 4 & 5 : Exploitation complète** :
- Calcul de l'adresse du shellcode
- Construction du payload (NOP sled + shellcode + adresse retour)
- Injection via upload.py
- Obtention d'un shell avec privilèges

**Contre-mesures modernes** :

| Contre-mesure | Description |
|---------------|-------------|
| Stack canaries | Valeur sentinelle avant adresse retour, vérifiée |
| ASLR (Address Space Layout Randomization) | Adresses mémoire aléatoires |
| DEP/NX (Data Execution Prevention) | Mémoire non exécutable (pile, tas) |
| RELRO (Relocation Read-Only) | Sections mémoire en lecture seule |
| Compilation sécurisée | Options -fstack-protector, -D_FORTIFY_SOURCE |

<h3 class="section-title">4. Analyse de cache - Profiling</h3>

**Hiérarchie mémoire** :

CPU → Cache L1 (1-3 cycles) → Cache L2 (10-20 cycles) → Cache L3 (40-75 cycles) → RAM (100-300 cycles)

Le cache accélère l'accès aux données fréquemment utilisées.

**Mesure du temps d'accès** :

TP Cache Profiling (profiling.c) :
- Fonction memaccesstime(ptr) : mesure le temps pour accéder à une adresse
- Fonction clflush(ptr) : vide (flush) l'adresse du cache
- Boucle de profiling :
  - Accéder → mesurer (cache hit)
  - Flush → accéder → mesurer (cache miss)
- Génération d'histogrammes avec gnuplot

**Résultats typiques** :
- Cache hit : 10-50 cycles
- Cache miss : 200-400 cycles

**Exploitation pour attaque** :

**Technique Flush+Reload** :
1. Flush une ligne de cache partagée avec la victime
2. Victime exécute son code
3. Attaquant mesure le temps de rechargement
4. Si rapide : victime a accédé à cette ligne

**Application : Détection d'ouverture de fichier** (spy.c) :
- Surveiller une adresse d'un fichier sensible
- Si le fichier est ouvert par un processus, il sera en cache
- Détection sans accès au système de fichiers

<h3 class="section-title">5. Vulnérabilités cryptographiques - AES</h3>

**AES (Advanced Encryption Standard)** :

Algorithme de chiffrement par blocs, standard depuis 2001.

**Structure** :
- Blocs de 128 bits
- Clés de 128, 192 ou 256 bits
- 10, 12 ou 14 rondes selon taille de clé
- Opérations : SubBytes (S-box), ShiftRows, MixColumns, AddRoundKey

**Vulnérabilités d'implémentation** :

**Implémentation naïve : Accès tables dépendant de la clé**

AES utilise des tables de substitution (S-box). L'implémentation classique stocke ces tables en mémoire.

Lors de l'exécution :
```
state[i] = Sbox[state[i] XOR key[i]]
```

L'indice d'accès dépend de la clé : vulnérabilité aux attaques par cache.

**TP : Comparaison OpenSSL versions**

**OpenSSL 0.9.7a (vulnérable)** :
- Accès direct aux tables T0, T1, T2, T3
- Indices dépendent des données et de la clé
- Vulnérable aux cache timing attacks

**OpenSSL 1.1.1t (protégée)** :
- Implémentation AES-NI (instructions matérielles)
- Pas d'accès mémoire dépendant de la clé
- Résistant aux cache timing attacks

**AES-NI** :

Instructions processeur dédiées (Intel, AMD depuis 2010) :
- AESENC, AESENCLAST : chiffrement
- AESDEC, AESDECLAST : déchiffrement
- AESIMC, AESKEYGENASSIST : génération de clés

Avantages :
- Performance élevée
- Implémentation résistante aux canaux auxiliaires
- Pas de tables en mémoire

<h3 class="section-title">6. Autres contre-mesures</h3>

**Masquage (Masking)** :

Technique contre les attaques DPA.

Principe : Randomiser les valeurs intermédiaires.

Au lieu de manipuler directement x, on manipule x XOR m (m aléatoire).

Les fuites de consommation portent sur x XOR m, qui est aléatoire.

**Exemple** :
```
x' = x XOR m
y' = f(x') = f(x XOR m)
y = y' XOR m' (où m' découle de m)
```

**Inconvénients** :
- Surcoût en calcul et en aléatoire
- Difficile à implémenter correctement (fuites possibles)

**Hiding** :

Réduire le rapport signal/bruit dans les traces de consommation.

Techniques :
- Randomisation de l'ordre des opérations
- Insertion d'opérations factices (dummy operations)
- Consommation constante (circuits à double rail)

**Sécurité physique** :

**Capteurs** :
- Détecteurs d'ouverture du boîtier
- Capteurs de température, lumière
- Capteurs de tension/fréquence anormales

**Mémoire effaçable** :
En cas de détection d'attaque, effacer les clés.

**Encapsulation** :
Protéger les circuits sensibles dans des résines difficiles à retirer.

<h3 class="section-title">7. Outils et méthodologies</h3>

**ChipWhisperer** :

Plateforme open-source pour analyse de canaux auxiliaires.

Fonctionnalités :
- Capture de traces de consommation électrique
- Synchronisation avec cible (trigger)
- Analyses DPA, CPA
- Injection de glitches (clock, voltage)

**GDB (GNU Debugger)** :

Utilisé pour analyser les programmes vulnérables :
- Poser des breakpoints
- Examiner la pile et les registres
- Calculer les offsets pour exploitations

**Commandes utiles** :
```
info registers    # état des registres
x/32x $rsp       # examiner la pile
disassemble      # désassembler une fonction
```

**Gnuplot** :

Visualisation des distributions de temps d'accès (cache hit/miss).

<h3 class="section-title">8. Domaines d'application</h3>

**Cartes à puce** :

Cibles privilégiées : paiement, authentification, SIM.
Menaces : clonage, extraction de clés.
Protections : masquage, capteurs, hardware sécurisé.

**Systèmes embarqués critiques** :

Automobile (CAN bus, ECU), aéronautique, médical.
Risques : injection de fautes, reverse engineering.

**IoT (Internet of Things)** :

Objets connectés souvent peu protégés.
Attaques possibles : extraction firmware, clonage, botnets.

**Infrastructures cloud** :

Attaques par cache entre machines virtuelles (VM).
Risque de fuite d'informations entre locataires (tenants).

---

## PART D - Analyse Réflexive et Perspectives

<h3 class="section-title">Compétences acquises</h3>

**Compréhension des menaces matérielles** :
Capacité à identifier les vulnérabilités physiques et logicielles des systèmes embarqués.

**Maîtrise des attaques par canaux auxiliaires** :
Aptitude à analyser les fuites d'information (timing, cache, puissance) et à exploiter ces failles.

**Exploitation de vulnérabilités logicielles** :
Compétence en exploitation de buffer overflow, injection de shellcode, et compréhension des protections modernes.

**Conception sécurisée** :
Développement de réflexes pour intégrer la sécurité dès la conception (secure by design).

**Vision d'ensemble** :
Capacité à évaluer la sécurité globale d'un système en considérant hardware, software, et attaques physiques.

<h3 class="section-title">Points clés à retenir</h3>

**1. Sécurité ≠ Cryptographie seule** :
Un algorithme mathématiquement sûr peut être vulnérable si son implémentation fuit des informations.

**2. Les canaux auxiliaires sont réels** :
Timing, cache, consommation : ces attaques sont pratiques et ont compromis des systèmes réels (cartes bancaires, DRM).

**3. Défense en profondeur** :
Pas de solution miracle. Combiner plusieurs contre-mesures pour augmenter le coût de l'attaque.

**4. Trade-off sécurité/performance** :
Les protections coûtent en performance, énergie, et complexité. Trouver le bon équilibre selon le contexte.

**5. Évolution constante** :
Nouvelles attaques régulièrement découvertes (Spectre, Meltdown, Rowhammer). Veille technologique indispensable.

<h3 class="section-title">Retour d'expérience</h3>

**Aspect révélateur** :
Ce cours a ouvert les yeux sur la fragilité des systèmes face aux attaques physiques. Voir des attaques théoriques fonctionner en TP est impressionnant.

**Difficulté de la sécurité** :
Concevoir un système sûr est difficile. Il faut penser comme un attaquant pour identifier toutes les failles possibles.

**Outils spécialisés** :
Manipuler ChipWhisperer, GDB, et analyser des traces demande de la pratique. Les TP ont permis de se familiariser avec ces outils professionnels.

**Équilibre nécessaire** :
Les contre-mesures ajoutent de la complexité. Il faut évaluer le niveau de menace et adapter la protection.

<h3 class="section-title">Applications pratiques</h3>

**Pour ingénieur en sécurité** :
- Audit de sécurité de systèmes embarqués
- Conception de produits résistants aux attaques physiques
- Certification sécuritaire (Common Criteria, FIPS)

**Pour développeur embarqué** :
- Écrire du code résistant aux attaques (timing constant)
- Éviter les vulnérabilités classiques (buffer overflow)
- Tester la robustesse face aux fautes

**Pour concepteur hardware** :
- Intégrer des contre-mesures matérielles (capteurs, masking)
- Choisir des composants sécurisés (TEE, Secure Element)
- Évaluer les risques dès la phase de design

**Dans la vie courante** :
- Comprendre les risques des objets connectés (caméras, serrures)
- Évaluer la sécurité de produits (cartes bancaires, smartphones)
- Sensibiliser aux enjeux de cybersécurité

<h3 class="section-title">Limites et ouvertures</h3>

**Limites du module** :
- Peu d'approfondissement sur les attaques EM (électromagnétiques)
- Pas de manipulation réelle d'injection laser ou voltage glitching
- Aspects légaux et éthiques peu abordés

**Ouvertures vers** :
- **Secure Elements** : HSM, TPM, Trusted Execution Environments (TEE)
- **Post-Quantum Cryptography** : résistance aux ordinateurs quantiques
- **Formal Verification** : preuves formelles de sécurité
- **Bug Bounty** : recherche éthique de vulnérabilités

<h3 class="section-title">Évolutions récentes</h3>

**Attaques Spectre et Meltdown (2018)** :

Exploitation de l'exécution spéculative des processeurs modernes.

Spectre : forcer un programme à révéler ses secrets via le cache.
Meltdown : lire la mémoire du noyau depuis l'espace utilisateur.

Impact : tous les processeurs Intel, AMD, ARM concernés.

**Rowhammer (2014)** :

Attaque sur mémoire DRAM : accès répétés à des lignes de mémoire peuvent induire des flips de bits sur lignes adjacentes.

Exploitation : élévation de privilèges, évasion de machines virtuelles.

**Attaques sur IA embarquée** :

Les réseaux de neurones sont vulnérables :
- Attaques adversariales (perturbations imperceptibles)
- Extraction de modèles par observation
- Backdoors dans modèles

Enjeu croissant avec l'IA embarquée (reconnaissance vocale, vision).

**5G et IoT** :

Explosion du nombre d'objets connectés.
Surface d'attaque considérable.
Besoin de sécurité légère et efficace énergétiquement.

<h3 class="section-title">Conseils pour réussir</h3>

**1. Comprendre avant d'exploiter** :
Bien maîtriser le fonctionnement normal d'un système avant de chercher les failles.

**2. Pratiquer les TP sérieusement** :
Les manipulations pratiques sont essentielles pour intégrer les concepts.

**3. Lire le code** :
Analyser le code source (shellcode, AES) pour comprendre les vulnérabilités.

**4. Penser en attaquant** :
Adopter la mentalité d'un attaquant : chercher le maillon faible, les hypothèses implicites.

**5. Se documenter** :
Lire des articles académiques, des rapports de vulnérabilités (CVE), des blogs de sécurité.

**6. Respecter l'éthique** :
Ne jamais utiliser ces connaissances de manière illégale. Hacking éthique uniquement.

<h3 class="section-title">Conclusion</h3>

Ce module est fondamental pour toute personne travaillant sur des systèmes embarqués ou critiques. La sécurité matérielle est souvent négligée au profit de la sécurité logicielle, mais les attaques physiques sont réelles et efficaces.

**Compétences transférables** :
- Analyse critique de la sécurité d'un système
- Compréhension profonde du fonctionnement des processeurs et mémoires
- Capacité à intégrer la sécurité dès la conception
- Vision multidisciplinaire (hardware, software, cryptographie, physique)

**Pertinence professionnelle** :
Avec l'explosion de l'IoT, de l'industrie 4.0, et des véhicules autonomes, la sécurité matérielle est un domaine en forte demande. Les ingénieurs formés à ces problématiques sont recherchés.

**Message principal** :
La sécurité est un processus, pas un produit. Il faut constamment évaluer, tester, et améliorer. Un système n'est jamais 100% sûr, mais on peut augmenter considérablement le coût de l'attaque.

**Recommandations** :
- Approfondir avec des cours avancés (Riscure Academy, Coursera)
- Suivre les conférences de sécurité (Black Hat, DEF CON, CHES)
- Pratiquer sur des plateformes (Hack The Box, CTF sécurité hardware)
- Rejoindre des communautés (r/ReverseEngineering, forums spécialisés)
- Rester informé des nouvelles vulnérabilités (CVE, bulletins de sécurité)

**Liens avec les autres cours** :
- [Architecture Matérielle - S6](./architecture-materielle.html) : caches, processeurs
- [Microcontrôleurs - S6](./microcontroleurs.html) : ARM Cortex, systèmes embarqués
- [Systèmes d'Exploitation - S5](./systemes-exploitation.html) : gestion mémoire
- [Langage C - S5](./langage-c.html) : programmation bas niveau
- [Embedded IA for IoT - S9](./embedded-ia-iot.html) : sécurité des objets connectés

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
      <h4>📖 Cours Complet</h4>
      <p>Cours complet de sécurité matérielle : attaques par canaux cachés, buffer overflow, vulnérabilités Spectre/Meltdown.</p>
      <embed src="/cours-pdf/S7/Securite-Materielle/cours-complet.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Securite-Materielle/cours-complet.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>📖 Buffer Overflow</h4>
      <p>Cours sur les attaques par dépassement de tampon : exploitation, stack smashing, protections et contre-mesures.</p>
      <embed src="/cours-pdf/S7/Securite-Materielle/buffer-overflow.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Securite-Materielle/buffer-overflow.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>📖 TP Cache Side-Channel Attack</h4>
      <p>Sujet de TP sur les attaques par canaux cachés via cache : timing attacks, Flush+Reload et expérimentations.</p>
      <embed src="/cours-pdf/S7/Securite-Materielle/tp-cache-sca.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Securite-Materielle/tp-cache-sca.pdf" target="_blank">📥 Télécharger</a></p>
    </div>
  </div>
</div>

---

*Cours suivi en 2023-2024 à l'INSA Toulouse, Département Génie Électrique et Informatique.*

<div class="back-nav">
    <a href="./my-courses-2023-2024.html">← Retour aux Cours 2023-2024</a>
</div>

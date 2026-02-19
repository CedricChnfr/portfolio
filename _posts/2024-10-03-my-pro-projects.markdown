---
layout: default
title: "Projets Professionnels"
description: "Projets professionnels de Cédric Chanfreau - Secure Logger ECU, automatisation tests, Flash Memory, banc de tests électroniques."
date: 2024-10-03 10:56:03 +0200
---

<style>
.page-content { padding: 0 !important; }
.page-content .wrapper { max-width: 100% !important; padding: 0 !important; }

/* ── Hero ── */
.pro-hero {
    background: linear-gradient(135deg, #f7971e 0%, #ffd200 60%, #f7971e 100%);
    padding: 70px 40px 80px;
    text-align: center;
    position: relative;
    overflow: hidden;
    width: 100vw;
    margin-left: calc(-50vw + 50%);
}
.pro-hero::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background:
        radial-gradient(circle at 20% 50%, rgba(255,255,255,0.15) 0%, transparent 50%),
        radial-gradient(circle at 80% 30%, rgba(255,255,255,0.10) 0%, transparent 50%);
}
.pro-hero-content { position: relative; z-index: 1; max-width: 800px; margin: 0 auto; }
.pro-hero h1 {
    font-size: 3em;
    color: white;
    font-weight: 800;
    margin: 0 0 16px 0;
    text-shadow: 0 2px 12px rgba(0,0,0,0.15);
}
.pro-hero p {
    font-size: 1.2em;
    color: rgba(255,255,255,0.9);
    max-width: 600px;
    margin: 0 auto;
    line-height: 1.7;
}
.pro-hero-badge {
    display: inline-block;
    background: rgba(255,255,255,0.2);
    color: white;
    padding: 6px 18px;
    border-radius: 50px;
    font-size: 0.9em;
    font-weight: 600;
    margin-bottom: 20px;
    border: 1px solid rgba(255,255,255,0.3);
}

/* ── Main container ── */
.pro-page-container {
    max-width: 900px;
    margin: 60px auto 80px;
    padding: 0 20px;
}

/* ── Back link ── */
.back-link {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    color: #f7971e;
    text-decoration: none;
    font-weight: 600;
    font-size: 0.95em;
    margin-bottom: 40px;
    transition: gap 0.2s ease;
}
.back-link:hover { gap: 14px; }

/* ── Accordion item ── */
.pro-project-item {
    background: white;
    border-radius: 20px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.06);
    border-left: 5px solid transparent;
    margin-bottom: 24px;
    transition: box-shadow 0.3s ease, border-color 0.3s ease;
    overflow: hidden;
}
.pro-project-item:hover {
    box-shadow: 0 12px 35px rgba(247,151,30,0.15);
    border-left-color: #f7971e;
}
.pro-project-item.expanded {
    border-left-color: #f7971e;
    box-shadow: 0 12px 35px rgba(247,151,30,0.18);
}

/* ── Header (always visible, clickable) ── */
.pro-project-header {
    display: flex;
    gap: 24px;
    padding: 28px 30px;
    cursor: pointer;
    align-items: flex-start;
    user-select: none;
    -webkit-user-select: none;
}
.pro-project-icon {
    font-size: 2.2em;
    width: 68px;
    height: 68px;
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #f7971e, #ffd200);
    border-radius: 50%;
    box-shadow: 0 6px 18px rgba(247,151,30,0.3);
}
.pro-project-summary { flex: 1; min-width: 0; }
.pro-project-title-row {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 12px;
    margin-bottom: 6px;
}
.pro-project-summary h3 {
    font-size: 1.45em;
    color: #2d3748;
    margin: 0 0 5px 0;
    font-weight: 700;
}
.pro-project-summary h4 {
    font-size: 1em;
    color: #f7971e;
    margin: 0;
    font-weight: 600;
}
.expand-arrow {
    font-size: 1.2em;
    color: #f7971e;
    transition: transform 0.35s ease;
    flex-shrink: 0;
    margin-top: 4px;
    display: inline-block;
}
.pro-project-item.expanded .expand-arrow {
    transform: rotate(180deg);
}
.pro-project-summary p {
    color: #718096;
    line-height: 1.6;
    margin: 12px 0 14px 0;
    font-size: 0.97em;
}
.pro-project-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}
.pro-project-tags .tag {
    background: linear-gradient(135deg, rgba(247,151,30,0.10), rgba(255,210,0,0.10));
    color: #d97706;
    border: 1px solid rgba(247,151,30,0.25);
    padding: 4px 12px;
    border-radius: 50px;
    font-size: 0.82em;
    font-weight: 600;
    transition: all 0.2s ease;
}
.pro-project-tags .tag:hover {
    background: linear-gradient(135deg, #f7971e, #ffd200);
    color: white;
    border-color: transparent;
}

/* ── Accordion body ── */
.pro-project-details {
    display: none;
    padding: 0 30px 28px 30px;
    border-top: 1px solid rgba(247,151,30,0.15);
    animation: fadeInDown 0.3s ease;
}
.pro-project-item.expanded .pro-project-details {
    display: block;
}
@keyframes fadeInDown {
    from { opacity: 0; transform: translateY(-8px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* ── Detail sections ── */
.detail-section {
    margin-top: 22px;
}
.detail-section-title {
    font-size: 0.88em;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #f7971e;
    font-weight: 700;
    margin: 0 0 12px 0;
    display: flex;
    align-items: center;
    gap: 8px;
}
.detail-section-title::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(to right, rgba(247,151,30,0.3), transparent);
}

/* Tools grid */
.tools-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}
.tool-badge {
    background: #fff7ed;
    color: #92400e;
    border: 1px solid #fed7aa;
    padding: 5px 14px;
    border-radius: 8px;
    font-size: 0.85em;
    font-weight: 600;
    font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
    transition: all 0.2s ease;
}
.tool-badge:hover {
    background: linear-gradient(135deg, #f7971e, #ffd200);
    color: white;
    border-color: transparent;
}

/* Skills list */
.skills-list {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    gap: 8px;
}
.skills-list li {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    color: #4a5568;
    font-size: 0.95em;
    line-height: 1.5;
}
.skills-list li::before {
    content: '▸';
    color: #f7971e;
    flex-shrink: 0;
    margin-top: 1px;
}

/* Challenge box */
.challenge-box {
    background: linear-gradient(135deg, #fff7ed, #fffbf0);
    border: 1px solid rgba(247,151,30,0.2);
    border-radius: 12px;
    padding: 16px 20px;
    color: #4a5568;
    font-size: 0.95em;
    line-height: 1.7;
}

/* ── Responsive ── */
@media (max-width: 700px) {
    .pro-hero h1 { font-size: 2em; }
    .pro-project-header { flex-direction: column; align-items: center; text-align: center; }
    .pro-project-title-row { flex-direction: column; align-items: center; }
    .pro-project-details { padding: 0 20px 24px; }
    .pro-hero { padding: 50px 20px 60px; }
}
</style>

<div class="pro-hero">
    <div class="pro-hero-content">
        <div class="pro-hero-badge" data-i18n="pp-hero-badge">💼 Alternance &amp; Stage</div>
        <h1 data-i18n="pp-hero-title">Projets Professionnels</h1>
        <p data-i18n="pp-hero-subtitle">Mini-projets techniques réalisés au cours de mes 3 ans d'alternance et de mon stage d'ingénieur, dans le secteur de l'automobile embarqué.</p>
    </div>
</div>

<div class="pro-page-container">

<a href="/" class="back-link" data-i18n="pp-back">← Retour à l'accueil</a>

<!-- ══════════════════════════════════════════════════
     1. SecESM — Schaeffler PFE S9
══════════════════════════════════════════════════ -->
<div class="pro-project-item" id="proj-schaeffler">
    <div class="pro-project-header" onclick="toggleProject(this)">
        <div class="pro-project-icon">🔒</div>
        <div class="pro-project-summary">
            <div class="pro-project-title-row">
                <div>
                    <h3 data-i18n="pp-1-title">SecESM – Secure Event Storage Manager</h3>
                    <h4 data-i18n="pp-1-company">Schaeffler · Oct. 2024 – Sept. 2025 · PFE</h4>
                </div>
                <span class="expand-arrow">▼</span>
            </div>
            <p data-i18n="pp-1-summary">Développement d'un composant logiciel embarqué C pour la gestion sécurisée des événements de sécurité dans les ECUs automobiles, au sein de l'équipe EAP (ECU Access Protection), conformément aux standards AUTOSAR Classic et ISO 21434.</p>
            <div class="pro-project-tags">
                <span class="tag">C</span>
                <span class="tag">AUTOSAR Classic</span>
                <span class="tag">Cybersécurité</span>
                <span class="tag">ISO 21434</span>
                <span class="tag">HSM</span>
            </div>
        </div>
    </div>
    <div class="pro-project-details">

        <div class="detail-section">
            <h5 class="detail-section-title" data-i18n="pp-tools-title">Outils &amp; Technologies</h5>
            <div class="tools-grid">
                <span class="tool-badge">C</span>
                <span class="tool-badge">AUTOSAR Classic</span>
                <span class="tool-badge">HSM</span>
                <span class="tool-badge">H2H (Host↔HSM)</span>
                <span class="tool-badge">IDSM</span>
                <span class="tool-badge">NvM</span>
                <span class="tool-badge">RTE</span>
                <span class="tool-badge">CryIf / CSM</span>
                <span class="tool-badge">Tresos / Cessar</span>
                <span class="tool-badge">Collaborator</span>
                <span class="tool-badge">Polarion</span>
                <span class="tool-badge">Axivion</span>
                <span class="tool-badge">Git</span>
            </div>
        </div>

        <div class="detail-section">
            <h5 class="detail-section-title" data-i18n="pp-skills-title">Compétences développées</h5>
            <ul class="skills-list" data-i18n-html="pp-1-skills">
                <li>Conception du composant SecESM en C sur plateforme AUTOSAR Classic : gestion de la pile d'événements de sécurité, persistance NvM, interfaces RTE</li>
                <li>Intégration des services cryptographiques CryIf/CSM : AES, CMAC, SHA-256 pour la signature et la vérification des événements stockés</li>
                <li>Communication H2H (Host↔HSM) pour déléguer les opérations cryptographiques au Hardware Security Module</li>
                <li>Interaction avec l'IDSM (Intrusion Detection System Manager) pour la remontée d'événements de sécurité</li>
                <li>Configuration ECU avec Tresos/Cessar, revue de code sur Collaborator, suivi qualité sur Polarion et analyse statique Axivion</li>
                <li>Travail en équipe EAP (ECU Access Protection) en méthodologie Agile (sprints)</li>
            </ul>
        </div>

        <div class="detail-section">
            <h5 class="detail-section-title" data-i18n="pp-challenge-title">Défis techniques</h5>
            <div class="challenge-box" data-i18n-html="pp-1-challenge">
                Concevoir un composant embarqué générique en C sur AUTOSAR Classic garantissant l'<strong>intégrité cryptographique</strong> de chaque événement de sécurité stocké, tout en respectant les contraintes temps réel et mémoire d'un ECU automobile. La délégation des opérations au <strong>HSM</strong> via le canal H2H impliquait une gestion fine des latences et des erreurs de communication.
            </div>
        </div>

    </div>
</div>

<!-- ══════════════════════════════════════════════════
     2. Automatisation des Tests ECU — Vitesco S7/S8
══════════════════════════════════════════════════ -->
<div class="pro-project-item" id="proj-vitesco-tests">
    <div class="pro-project-header" onclick="toggleProject(this)">
        <div class="pro-project-icon">🤖</div>
        <div class="pro-project-summary">
            <div class="pro-project-title-row">
                <div>
                    <h3 data-i18n="pp-2-title">Automatisation des Tests ECU</h3>
                    <h4 data-i18n="pp-2-company">Vitesco Technologies · Sept. 2022 – Sept. 2024 · Alternance</h4>
                </div>
                <span class="expand-arrow">▼</span>
            </div>
            <p data-i18n="pp-2-summary">Développement de 56 scripts Python automatisant les tests ECRP et OTAM pour la reprogrammation des ECUs, ainsi que la correction de violations MISRA-C/CERT-C via l'outil Axivion, dans un contexte d'alternance de 2 ans.</p>
            <div class="pro-project-tags">
                <span class="tag">Python</span>
                <span class="tag">Jenkins</span>
                <span class="tag">MISRA / CERT-C</span>
                <span class="tag">ECU</span>
                <span class="tag">Axivion</span>
                <span class="tag">Polarion</span>
            </div>
        </div>
    </div>
    <div class="pro-project-details">

        <div class="detail-section">
            <h5 class="detail-section-title" data-i18n="pp-tools-title">Outils &amp; Technologies</h5>
            <div class="tools-grid">
                <span class="tool-badge">Python 3</span>
                <span class="tool-badge">Jenkins CI/CD</span>
                <span class="tool-badge">CMM / Lauterbach PRACTICE</span>
                <span class="tool-badge">Trace32</span>
                <span class="tool-badge">TestExecutor</span>
                <span class="tool-badge">Contest</span>
                <span class="tool-badge">Axivion</span>
                <span class="tool-badge">Polarion</span>
                <span class="tool-badge">C (MISRA-C)</span>
                <span class="tool-badge">Git</span>
            </div>
        </div>

        <div class="detail-section">
            <h5 class="detail-section-title" data-i18n="pp-skills-title">Compétences développées</h5>
            <ul class="skills-list" data-i18n-html="pp-2-skills">
                <li>Développement de 56 scripts Python automatisant les tests de reprogrammation ECU (ECRP) et de mise à jour OTA (OTAM), intégrés à Jenkins pour exécution nocturne</li>
                <li>Utilisation du framework interne Contest et de l'outil TestExecutor pour piloter et valider les séquences de test</li>
                <li>Débogage bas niveau avec CMM/Lauterbach PRACTICE et Trace32 : inspection mémoire, points d'arrêt, traçage d'exécution</li>
                <li>Correction de violations MISRA-C:2012 et CERT-C identifiées par Axivion : analyse statique, revue et correction du code embarqué C</li>
                <li>Suivi qualité et traçabilité des exigences sur Polarion, travail en équipe internationale (France, Allemagne, Inde)</li>
            </ul>
        </div>

        <div class="detail-section">
            <h5 class="detail-section-title" data-i18n="pp-challenge-title">Défis techniques</h5>
            <div class="challenge-box" data-i18n-html="pp-2-challenge">
                Rendre les 56 scripts de test <strong>robustes et maintenables</strong> face à la diversité des configurations ECU (ECRP vs OTAM), tout en intégrant les résultats dans un pipeline Jenkins fiable. La correction systématique des violations <strong>MISRA-C/CERT-C</strong> avec Axivion nécessitait une compréhension approfondie des règles de codage sans dégrader les fonctionnalités existantes.
            </div>
        </div>

    </div>
</div>

<!-- ══════════════════════════════════════════════════
     3. Validation MCU Renesas RH850/U2B — Vitesco Iasi S8
══════════════════════════════════════════════════ -->
<div class="pro-project-item" id="proj-vitesco-flash">
    <div class="pro-project-header" onclick="toggleProject(this)">
        <div class="pro-project-icon">💾</div>
        <div class="pro-project-summary">
            <div class="pro-project-title-row">
                <div>
                    <h3 data-i18n="pp-3-title">Validation MCU Renesas RH850/U2B</h3>
                    <h4 data-i18n="pp-3-company">Vitesco Technologies · Juil. – Sept. 2024 · Mission Iasi, Roumanie</h4>
                </div>
                <span class="expand-arrow">▼</span>
            </div>
            <p data-i18n="pp-3-summary">Portage et validation des scripts de gestion mémoire Flash (Code Flash + Data Flash) sur le nouveau MCU Renesas RH850/U2B, dans le cadre d'un projet de réduction de dépendance fournisseur (remplacement de l'Infineon TC39), avec un rôle d'intermédiaire entre les équipes France et Roumanie.</p>
            <div class="pro-project-tags">
                <span class="tag">C</span>
                <span class="tag">Renesas RH850/U2B</span>
                <span class="tag">Flash Memory</span>
                <span class="tag">CMM</span>
                <span class="tag">Validation</span>
            </div>
        </div>
    </div>
    <div class="pro-project-details">

        <div class="detail-section">
            <h5 class="detail-section-title" data-i18n="pp-tools-title">Outils &amp; Technologies</h5>
            <div class="tools-grid">
                <span class="tool-badge">C</span>
                <span class="tool-badge">Renesas RH850/U2B</span>
                <span class="tool-badge">CMM Data Flash</span>
                <span class="tool-badge">CMM Code Flash</span>
                <span class="tool-badge">Lauterbach TRACE32</span>
                <span class="tool-badge">Jenkins</span>
                <span class="tool-badge">Git</span>
                <span class="tool-badge">Polarion</span>
            </div>
        </div>

        <div class="detail-section">
            <h5 class="detail-section-title" data-i18n="pp-skills-title">Compétences développées</h5>
            <ul class="skills-list" data-i18n-html="pp-3-skills">
                <li>Analyse du datasheet Renesas RH850/U2B pour comprendre les registres de contrôle Flash, les timings et les modes d'accès</li>
                <li>Développement et adaptation des scripts CMM pour la gestion de la Data Flash et de la Code Flash sur le nouveau MCU</li>
                <li>Validation fonctionnelle complète : tests de lecture, écriture et effacement sur les deux types de mémoire Flash</li>
                <li>Rôle d'intermédiaire technique entre l'équipe de Toulouse (France) et l'équipe locale de Iasi (Roumanie) : coordination, traduction des exigences et remontée des résultats</li>
                <li>Débogage avec Lauterbach TRACE32 : inspection mémoire et vérification des séquences d'initialisation</li>
            </ul>
        </div>

        <div class="detail-section">
            <h5 class="detail-section-title" data-i18n="pp-challenge-title">Défis techniques</h5>
            <div class="challenge-box" data-i18n-html="pp-3-challenge">
                S'approprier rapidement le datasheet du <strong>Renesas RH850/U2B</strong> — un MCU inconnu jusque-là — pour adapter les scripts CMM existants sans documentation interne préalable. Le rôle d'<strong>intermédiaire bilingue</strong> entre Toulouse et Iasi impliquait de centraliser les décisions techniques et d'assurer la cohérence des exigences dans les deux sens, dans un délai de mission court.
            </div>
        </div>

    </div>
</div>

<!-- ══════════════════════════════════════════════════
     4. Banc de Tests VAL208NG — Siemens
══════════════════════════════════════════════════ -->
<div class="pro-project-item" id="proj-siemens">
    <div class="pro-project-header" onclick="toggleProject(this)">
        <div class="pro-project-icon">⚙️</div>
        <div class="pro-project-summary">
            <div class="pro-project-title-row">
                <div>
                    <h3 data-i18n="pp-4-title">Banc de Tests Électroniques VAL208NG</h3>
                    <h4 data-i18n="pp-4-company">Siemens · Avr. – Juil. 2022 · Stage ingénieur</h4>
                </div>
                <span class="expand-arrow">▼</span>
            </div>
            <p data-i18n="pp-4-summary">Analyse du système de rack frein ferroviaire VAL208NG et développement d'un banc de tests complet pour la carte entrées-sorties. Rédaction des procédures et validation fonctionnelle des cartes électroniques.</p>
            <div class="pro-project-tags">
                <span class="tag">Électronique</span>
                <span class="tag">PCB</span>
                <span class="tag">Banc de Tests</span>
                <span class="tag">Ferroviaire</span>
                <span class="tag">LabVIEW</span>
            </div>
        </div>
    </div>
    <div class="pro-project-details">

        <div class="detail-section">
            <h5 class="detail-section-title" data-i18n="pp-tools-title">Outils &amp; Technologies</h5>
            <div class="tools-grid">
                <span class="tool-badge">Altium Designer</span>
                <span class="tool-badge">LabVIEW</span>
                <span class="tool-badge">Oscilloscope</span>
                <span class="tool-badge">Analyseur logique</span>
                <span class="tool-badge">Multimètre / LCR-mètre</span>
                <span class="tool-badge">Générateur de signaux</span>
                <span class="tool-badge">MS Excel</span>
            </div>
        </div>

        <div class="detail-section">
            <h5 class="detail-section-title" data-i18n="pp-skills-title">Compétences développées</h5>
            <ul class="skills-list" data-i18n-html="pp-4-skills">
                <li>Lecture et analyse schématique de la carte IO du rack frein VAL208NG : alimentation, signaux TOR (Tout-Ou-Rien), entrées analogiques 4-20 mA</li>
                <li>Conception du câblage du banc de test et sélection des équipements de mesure adaptés aux niveaux de tension ferroviaires</li>
                <li>Développement d'une interface LabVIEW pour piloter le banc et enregistrer automatiquement les mesures</li>
                <li>Rédaction des procédures de test et fiches de validation selon les normes qualité Siemens</li>
                <li>Tests fonctionnels complets : validation des entrées/sorties TOR, linéarité des voies analogiques, immunité aux perturbations</li>
            </ul>
        </div>

        <div class="detail-section">
            <h5 class="detail-section-title" data-i18n="pp-challenge-title">Défis techniques</h5>
            <div class="challenge-box" data-i18n-html="pp-4-challenge">
                Comprendre rapidement l'architecture complexe d'un système ferroviaire critique (rack frein VAL208NG) en tant que stagiaire, et concevoir un banc de test <strong>fiable et reproductible</strong> respectant les contraintes de sécurité ferroviaire. La principale difficulté était de couvrir l'ensemble des cas de test en un minimum de temps tout en documentant chaque résultat avec le niveau de rigueur requis.
            </div>
        </div>

    </div>
</div>

</div><!-- /pro-page-container -->

<script>
function toggleProject(header) {
    var item = header.closest('.pro-project-item');
    item.classList.toggle('expanded');
}
</script>

---
layout: default
title: About
permalink: /about/
---

<style>
.page-content { padding: 0 !important; }
.page-content .wrapper { max-width: 100% !important; padding: 0 !important; }

/* ---- Hero ---- */
.ab-hero {
    position: relative;
    min-height: 48vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 55%, #f093fb 100%);
    overflow: hidden;
    padding: 80px 40px;
    width: 100vw;
    margin-left: calc(-50vw + 50%);
}
.ab-hero-blob {
    position: absolute;
    border-radius: 50%;
    pointer-events: none;
}
.ab-hero-blob-1 {
    width: 380px; height: 380px;
    top: -120px; right: -80px;
    background: rgba(255,255,255,0.07);
    animation: abFloat 18s ease-in-out infinite;
}
.ab-hero-blob-2 {
    width: 220px; height: 220px;
    bottom: -70px; left: -50px;
    background: rgba(255,255,255,0.05);
    animation: abFloat 24s ease-in-out infinite reverse;
}
.ab-hero-ring {
    position: absolute;
    width: 200px; height: 200px;
    border-radius: 50%;
    border: 1px solid rgba(255,255,255,0.08);
    top: 10%; right: 25%;
    animation: abSpin 40s linear infinite;
}
.ab-hero-dots {
    position: absolute;
    bottom: 25px; right: 50px;
    width: 110px; height: 80px;
    background-image: radial-gradient(circle, rgba(255,255,255,0.22) 1.5px, transparent 1.5px);
    background-size: 14px 14px;
}
.ab-hero-sq {
    position: absolute;
    bottom: 22%; left: 18%;
    width: 55px; height: 55px;
    border: 1.5px solid rgba(255,255,255,0.1);
    animation: abSpin 30s linear infinite;
}
@keyframes abFloat {
    0%, 100% { transform: translate(0, 0); }
    33% { transform: translate(20px, -15px); }
    66% { transform: translate(-15px, 20px); }
}
@keyframes abSpin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}
.ab-hero-content {
    position: relative;
    z-index: 1;
    text-align: center;
    max-width: 700px;
}
.ab-hero-tag {
    display: inline-block;
    font-family: 'Courier New', monospace;
    font-size: 0.82em;
    color: rgba(255,255,255,0.85);
    background: rgba(255,255,255,0.1);
    border: 1px solid rgba(255,255,255,0.2);
    padding: 5px 18px;
    border-radius: 50px;
    margin-bottom: 22px;
    letter-spacing: 0.07em;
}
.ab-hero-title {
    font-size: 3.6em;
    font-weight: 900;
    color: white;
    margin: 0 0 16px 0;
    line-height: 1.1;
}
.ab-hero-sub {
    font-size: 1.1em;
    color: rgba(255,255,255,0.78);
    margin: 0;
    line-height: 1.7;
}

/* ---- Page body ---- */
.ab-page {
    max-width: 1000px;
    margin: 0 auto;
    padding: 90px 40px 60px;
}
.ab-label {
    display: block;
    font-family: 'Courier New', monospace;
    font-size: 0.78em;
    color: #667eea;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 10px;
}
.ab-section-title {
    font-size: 2em;
    font-weight: 800;
    color: #1a202c;
    margin: 0 0 40px 0;
    position: relative;
    padding-bottom: 16px;
}
.ab-section-title::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0;
    width: 55px; height: 4px;
    background: linear-gradient(90deg, #667eea, #f093fb);
    border-radius: 2px;
}

/* ---- Identity + bio ---- */
.ab-identity {
    display: grid;
    grid-template-columns: 310px 1fr;
    gap: 55px;
    align-items: center;
    margin-bottom: 100px;
}
.ab-id-card {
    background: linear-gradient(160deg, #1e1b4b, #312e81);
    border-radius: 28px;
    padding: 38px 28px;
    position: relative;
    overflow: hidden;
    color: white;
    box-shadow: 0 22px 55px rgba(102,126,234,0.25);
}
.ab-id-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
    border-radius: 28px 28px 0 0;
}
.ab-id-glow {
    position: absolute;
    width: 200px; height: 200px;
    top: -70px; right: -60px;
    border-radius: 50%;
    background: rgba(102,126,234,0.3);
    filter: blur(50px);
    pointer-events: none;
}
.ab-id-photo-wrap {
    position: relative;
    width: 110px; height: 110px;
    margin: 0 auto 26px;
}
.ab-id-photo-wrap img {
    width: 110px; height: 110px;
    border-radius: 50%;
    object-fit: cover;
    border: 3px solid rgba(255,255,255,0.18);
    position: relative;
    z-index: 2;
    display: block;
}
.ab-id-ring-1 {
    position: absolute;
    top: -9px; left: -9px; right: -9px; bottom: -9px;
    border-radius: 50%;
    border: 2px dashed rgba(102,126,234,0.55);
    animation: abSpin 16s linear infinite;
    z-index: 1;
}
.ab-id-ring-2 {
    position: absolute;
    top: -20px; left: -20px; right: -20px; bottom: -20px;
    border-radius: 50%;
    border: 1px solid rgba(240,147,251,0.22);
    animation: abSpin 30s linear infinite reverse;
    z-index: 1;
}
.ab-id-badge {
    position: absolute;
    bottom: -7px; right: -18px;
    background: linear-gradient(135deg, #10b981, #059669);
    color: white;
    font-size: 0.67em;
    font-weight: 700;
    padding: 5px 12px;
    border-radius: 50px;
    z-index: 3;
    display: flex;
    align-items: center;
    gap: 6px;
    white-space: nowrap;
    box-shadow: 0 4px 14px rgba(16,185,129,0.45);
}
.ab-pulse-dot {
    width: 7px; height: 7px;
    background: white;
    border-radius: 50%;
    position: relative;
    flex-shrink: 0;
}
.ab-pulse-dot::after {
    content: '';
    position: absolute;
    top: -3px; left: -3px;
    width: 13px; height: 13px;
    border-radius: 50%;
    background: rgba(255,255,255,0.38);
    animation: abPulse 1.5s ease-out infinite;
}
@keyframes abPulse {
    0% { transform: scale(0.8); opacity: 1; }
    100% { transform: scale(2.3); opacity: 0; }
}
.ab-id-name {
    text-align: center;
    margin-bottom: 24px;
    position: relative;
    z-index: 1;
}
.ab-id-name h3 { font-size: 1.25em; font-weight: 700; color: white; margin: 0 0 5px 0; }
.ab-id-name p { color: rgba(255,255,255,0.45); font-size: 0.85em; margin: 0; }
.ab-id-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
    margin: 0 0 20px 0;
    position: relative; z-index: 1;
}
.ab-id-facts { display: flex; flex-direction: column; gap: 9px; position: relative; z-index: 1; }
.ab-id-fact {
    display: flex;
    align-items: center;
    gap: 11px;
    padding: 10px 13px;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 11px;
    transition: all 0.3s ease;
    cursor: default;
}
.ab-id-fact:hover {
    background: rgba(102,126,234,0.18);
    border-color: rgba(102,126,234,0.3);
    transform: translateX(5px);
}
.ab-id-fact-icon { font-size: 1.1em; flex-shrink: 0; }
.ab-id-fact-info { display: flex; flex-direction: column; gap: 1px; }
.ab-id-fact-label { font-size: 0.67em; text-transform: uppercase; letter-spacing: 0.09em; color: rgba(255,255,255,0.3); }
.ab-id-fact-value { font-size: 0.86em; color: rgba(255,255,255,0.82); font-weight: 500; }

/* Bio text */
.ab-bio-text {
    font-size: 1.08em;
    line-height: 1.9;
    color: #4a5568;
    margin: 0;
    position: relative;
    padding-left: 22px;
    text-align: left;
}
.ab-bio-text::before {
    content: '';
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 3px;
    background: linear-gradient(180deg, #667eea, #f093fb);
    border-radius: 2px;
}

/* ---- Motivation cards (Why INSA + Why ISS) ---- */
.ab-motiv { margin-bottom: 100px; }
.ab-motiv-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
}
.ab-motiv-card {
    border-radius: 24px;
    padding: 40px 35px;
    position: relative;
    overflow: hidden;
    transition: transform 0.32s ease, box-shadow 0.32s ease;
}
.ab-motiv-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 18px 45px rgba(0,0,0,0.1);
}
.ab-motiv-card-a {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    box-shadow: 0 12px 35px rgba(102,126,234,0.25);
}
.ab-motiv-card-b {
    background: linear-gradient(135deg, #1e1b4b, #312e81);
    color: white;
    box-shadow: 0 12px 35px rgba(30,27,75,0.25);
}
.ab-motiv-blob {
    position: absolute;
    border-radius: 50%;
    filter: blur(40px);
    pointer-events: none;
    top: -50px; right: -50px;
    width: 160px; height: 160px;
    background: rgba(255,255,255,0.08);
}
.ab-motiv-dots {
    position: absolute;
    bottom: 15px; left: 20px;
    width: 80px; height: 55px;
    background-image: radial-gradient(circle, rgba(255,255,255,0.15) 1.5px, transparent 1.5px);
    background-size: 12px 12px;
    pointer-events: none;
}
.ab-motiv-card-inner { position: relative; z-index: 1; }
.ab-motiv-icon { font-size: 2.5em; display: block; margin-bottom: 18px; }
.ab-motiv-card h3 { font-size: 1.2em; font-weight: 800; color: white; margin: 0 0 8px 0; }
.ab-motiv-card h4 { font-size: 0.82em; color: rgba(255,255,255,0.55); font-weight: 600; margin: 0 0 18px 0; letter-spacing: 0.03em; }
.ab-motiv-card p { color: rgba(255,255,255,0.78); line-height: 1.78; font-size: 0.93em; margin: 0; text-align: left; }

/* ---- CTA ---- */
.ab-cta {
    position: relative;
    background: linear-gradient(160deg, #0f0c29, #302b63);
    border-radius: 30px;
    padding: 65px 55px;
    text-align: center;
    overflow: hidden;
    margin-bottom: 40px;
}
.ab-cta-blob {
    position: absolute;
    border-radius: 50%;
    filter: blur(60px);
    pointer-events: none;
}
.ab-cta-blob-1 { width: 230px; height: 230px; top: -70px; left: -55px; background: rgba(102,126,234,0.22); }
.ab-cta-blob-2 { width: 180px; height: 180px; bottom: -55px; right: -45px; background: rgba(240,147,251,0.18); }
.ab-cta-inner { position: relative; z-index: 1; }
.ab-cta h2 { font-size: 2.1em; color: white; font-weight: 800; margin: 0 0 16px 0; }
.ab-cta p { color: rgba(255,255,255,0.65); font-size: 1em; line-height: 1.8; max-width: 540px; margin: 0 auto 34px; text-align: center; }
.ab-cta-btns { display: flex; gap: 16px; justify-content: center; flex-wrap: wrap; }
.ab-btn-p {
    padding: 13px 30px;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white; text-decoration: none;
    border-radius: 50px; font-weight: 700; font-size: 0.96em;
    transition: all 0.3s ease;
    box-shadow: 0 8px 22px rgba(102,126,234,0.42);
    display: inline-block;
}
.ab-btn-p:hover { transform: translateY(-3px); box-shadow: 0 14px 32px rgba(102,126,234,0.55); color: white; text-decoration: none; }
.ab-btn-s {
    padding: 13px 30px;
    background: rgba(255,255,255,0.08); color: white; text-decoration: none;
    border-radius: 50px; font-weight: 700; font-size: 0.96em;
    border: 1px solid rgba(255,255,255,0.16);
    transition: all 0.3s ease; display: inline-block;
}
.ab-btn-s:hover { background: rgba(255,255,255,0.15); transform: translateY(-3px); color: white; text-decoration: none; }

/* Responsive */
@media (max-width: 860px) {
    .ab-identity { grid-template-columns: 1fr; }
    .ab-id-card { max-width: 380px; margin: 0 auto; }
    .ab-motiv-grid { grid-template-columns: 1fr; }
    .ab-hero-title { font-size: 2.6em; }
}
@media (max-width: 600px) {
    .ab-page { padding: 60px 20px 40px; }
    .ab-hero-title { font-size: 2em; }
    .ab-cta { padding: 45px 24px; }
    .ab-cta h2 { font-size: 1.6em; }
}
</style>

<!-- Hero -->
<div class="ab-hero">
    <div class="ab-hero-blob ab-hero-blob-1"></div>
    <div class="ab-hero-blob ab-hero-blob-2"></div>
    <div class="ab-hero-ring"></div>
    <div class="ab-hero-dots"></div>
    <div class="ab-hero-sq"></div>
    <div class="ab-hero-content">
        <span class="ab-hero-tag">// ABOUT ME</span>
        <h1 class="ab-hero-title" data-i18n="about-background-title">Mon Parcours</h1>
        <p class="ab-hero-sub" data-i18n="hero-subtitle">Ingénieur INSA Toulouse · Automatique & Électronique</p>
    </div>
</div>

<div class="ab-page">

    <!-- Identity + Bio -->
    <div class="ab-identity">
        <div class="ab-id-card">
            <div class="ab-id-glow"></div>
            <div class="ab-id-photo-wrap">
                <img src="/img/Photo.jpg" alt="Cédric Chanfreau">
                <div class="ab-id-ring-1"></div>
                <div class="ab-id-ring-2"></div>
                <div class="ab-id-badge">
                    <span class="ab-pulse-dot"></span>
                    Open to work
                </div>
            </div>
            <div class="ab-id-name">
                <h3>Cédric Chanfreau</h3>
                <p>Embedded Systems Engineer</p>
            </div>
            <div class="ab-id-divider"></div>
            <div class="ab-id-facts">
                <div class="ab-id-fact">
                    <span class="ab-id-fact-icon">📍</span>
                    <div class="ab-id-fact-info">
                        <span class="ab-id-fact-label">Location</span>
                        <span class="ab-id-fact-value">Toulouse, France</span>
                    </div>
                </div>
                <div class="ab-id-fact">
                    <span class="ab-id-fact-icon">🎓</span>
                    <div class="ab-id-fact-info">
                        <span class="ab-id-fact-label" data-i18n="about-label-education">Formation</span>
                        <span class="ab-id-fact-value">INSA Toulouse · ENSEEIHT</span>
                    </div>
                </div>
                <div class="ab-id-fact">
                    <span class="ab-id-fact-icon">🗣️</span>
                    <div class="ab-id-fact-info">
                        <span class="ab-id-fact-label" data-i18n="about-label-languages">Langues</span>
                        <span class="ab-id-fact-value">Français · English · Español</span>
                    </div>
                </div>
                <div class="ab-id-fact">
                    <span class="ab-id-fact-icon">🏭</span>
                    <div class="ab-id-fact-info">
                        <span class="ab-id-fact-label" data-i18n="about-label-experience">Expérience</span>
                        <span class="ab-id-fact-value">3 ans · Automotive Industry</span>
                    </div>
                </div>
            </div>
        </div>

        <div>
            <span class="ab-label">// MY STORY</span>
            <h2 class="ab-section-title" data-i18n="about-background-title">Qui suis-je ?</h2>
            <p class="ab-bio-text">
                Driven by a passion for electronics, computer science, and embedded systems,
                I decided to pursue an engineering career after obtaining my scientific baccalaureate.
                I started with a GEII degree in Toulouse, then joined INSA Toulouse — combining
                academic rigor with 3 years of real-world professional experience through an apprenticeship
                in the automotive industry.
            </p>
        </div>
    </div>

    <!-- Motivations -->
    <div class="ab-motiv">
        <span class="ab-label">// MY MOTIVATIONS</span>
        <h2 class="ab-section-title" data-i18n="about-motiv-title">Pourquoi ces choix</h2>
        <div class="ab-motiv-grid">

            <div class="ab-motiv-card ab-motiv-card-a">
                <div class="ab-motiv-blob"></div>
                <div class="ab-motiv-dots"></div>
                <div class="ab-motiv-card-inner">
                    <span class="ab-motiv-icon">🏛️</span>
                    <h3 data-i18n="about-insa-title">Pourquoi l'INSA Toulouse</h3>
                    <h4 data-i18n="about-insa-subtitle">Ingénieur · Automatique & Électronique</h4>
                    <p>The school's reputation and hands-on approach convinced me. The apprenticeship program perfectly aligns with my learning style — gaining real professional experience alongside theoretical knowledge, an invaluable asset for an engineering career.</p>
                </div>
            </div>

            <div class="ab-motiv-card ab-motiv-card-b">
                <div class="ab-motiv-blob"></div>
                <div class="ab-motiv-dots"></div>
                <div class="ab-motiv-card-inner">
                    <span class="ab-motiv-icon">💡</span>
                    <h3 data-i18n="about-iss-title">Pourquoi la spécialisation ISS</h3>
                    <h4>Innovative Smart Systems · ENSEEIHT REOC</h4>
                    <p>ISS perfectly aligns with my interest in cutting-edge technologies: IoT, AI, and cyber-physical systems. The multidisciplinary approach — combining hardware and software — fits my goal of tackling complex challenges at the frontier of embedded engineering.</p>
                </div>
            </div>

        </div>
    </div>

    <!-- CTA -->
    <div class="ab-cta">
        <div class="ab-cta-blob ab-cta-blob-1"></div>
        <div class="ab-cta-blob ab-cta-blob-2"></div>
        <div class="ab-cta-inner">
            <h2 data-i18n="about-after-title">Et maintenant ?</h2>
            <p data-i18n="about-cta-text">
                Diplômé en 2025, je suis activement à la recherche d'un poste d'Ingénieur Logiciel Embarqué.
                Ouvert aux opportunités en France et à l'international.
            </p>
            <div class="ab-cta-btns">
                <a href="/my-cv.html" class="ab-btn-p" data-i18n="about-cta-btn-cv">Voir mon CV</a>
                <a href="/my-projects.html" class="ab-btn-s" data-i18n="about-cta-btn-projects">Mes Projets</a>
            </div>
        </div>
    </div>

</div>

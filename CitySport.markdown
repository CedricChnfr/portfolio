---
layout: default
title: CitySport
description: "CitySport - plateforme communautaire sportive multi-villes. Toulouse Sport (France) et NY Sport (New York, USA)."
permalink: /CitySport.html
nav_exclude: true
---

<style>
p { text-align: justify; }

.cs-hero {
  background: linear-gradient(135deg, #0f172a 0%, #1e3a5f 55%, #7c2d12 100%);
  color: white;
  border-radius: 12px;
  padding: 2.5rem 2rem;
  margin-bottom: 2rem;
  text-align: center;
}
.cs-hero h1 { color: white; margin-bottom: 0.5rem; font-size: 2.1rem; }
.cs-hero p  { color: #cbd5e1; text-align: center; font-size: 1.05rem; margin: 0; }
.cs-hero .tagline { font-size: 1.2rem; color: #93c5fd; margin-bottom: 1rem; }

.cs-badges {
  display: flex; flex-wrap: wrap; gap: 0.5rem;
  justify-content: center; margin-top: 1.2rem;
}
.cs-badge {
  background: rgba(255,255,255,0.15);
  border: 1px solid rgba(255,255,255,0.3);
  border-radius: 20px;
  padding: 0.3rem 0.9rem;
  font-size: 0.8rem;
  color: white;
}

.cs-section-label {
  text-transform: uppercase; letter-spacing: 0.1em;
  font-size: 0.75rem; color: #2563eb; font-weight: 700;
  margin-bottom: 0.3rem;
  text-align: center;
}

.cs-city-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 1.5rem;
  margin: 1.5rem 0 2rem;
}
.cs-city-card {
  border-radius: 14px;
  overflow: hidden;
  text-decoration: none;
  color: inherit;
  border: 1px solid #e2e8f0;
  background: #fff;
  box-shadow: 0 2px 10px rgba(15,23,42,0.06);
  transition: transform 0.2s, box-shadow 0.2s;
  display: block;
}
.cs-city-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 24px rgba(15,23,42,0.14);
  text-decoration: none;
}
.cs-city-banner {
  width: 100%;
  height: 180px;
  object-fit: cover;
  display: block;
}
.cs-city-body { padding: 1.4rem 1.5rem 1.6rem; }
.cs-city-body h3 { margin: 0 0 0.3rem; font-size: 1.4rem; color: #0f172a; }
.cs-city-tag { font-size: 0.85rem; color: #64748b; margin-bottom: 0.8rem; }
.cs-status {
  display: inline-block;
  border-radius: 20px;
  padding: 0.25rem 0.8rem;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.03em;
  margin-bottom: 0.8rem;
}
.cs-status-live { background: #dcfce7; color: #166534; }
.cs-status-pilot { background: #fff7ed; color: #9a3412; }
.cs-city-cta {
  font-weight: 600;
  color: #2563eb;
  font-size: 0.92rem;
}
.cs-city-card:hover .cs-city-cta { text-decoration: underline; }

.cs-value-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1rem;
  margin: 1.5rem 0;
}
.cs-value-card {
  background: #f8faff;
  border: 1px solid #dbeafe;
  border-radius: 10px;
  padding: 1.2rem;
}
.cs-value-card .icon { font-size: 1.8rem; margin-bottom: 0.5rem; }
.cs-value-card strong { display: block; margin-bottom: 0.4rem; color: #1e40af; }

.cs-cta-bar {
  display: flex; gap: 1rem; flex-wrap: wrap;
  justify-content: center; margin: 2rem 0;
}
.cs-btn {
  display: inline-block;
  padding: 0.75rem 1.8rem;
  border-radius: 8px;
  font-weight: 600;
  text-decoration: none;
  font-size: 0.95rem;
  transition: opacity 0.2s;
}
.cs-btn:hover { opacity: 0.85; text-decoration: none; }
.cs-btn-primary { background: #2563eb; color: white; }
.cs-btn-secondary { background: #f1f5f9; color: #1e3a5f; border: 1px solid #cbd5e1; }
</style>

<!-- ═══════════════════════════════════════════════ HERO ═══ -->

<div class="cs-hero">
  <div class="lang-fr">
    <h1>CitySport</h1>
    <p class="tagline">Une plateforme, chaque ville</p>
    <p>La technologie qui connecte les habitants par le sport, pensée pour être déployée ville par ville.</p>
  </div>
  <div class="lang-en">
    <h1>CitySport</h1>
    <p class="tagline">One platform, every city</p>
    <p>The technology that connects residents through sport, built to be deployed city by city.</p>
  </div>
  <div class="cs-badges">
    <span class="cs-badge">React Native</span>
    <span class="cs-badge">Next.js 15</span>
    <span class="cs-badge">Supabase</span>
    <span class="cs-badge">TypeScript</span>
    <span class="cs-badge">iOS &amp; Android</span>
    <span class="cs-badge">Multi-city ready</span>
  </div>
</div>

<div class="lang-fr">
<p>CitySport est le socle technique commun derrière une famille d'applications sportives communautaires locales. Chaque édition — même application mobile, même dashboard analytique pour les agents de la collectivité — est adaptée à une ville : ses quartiers, ses équipements, sa langue. Choisissez une édition ci-dessous pour découvrir son dossier complet.</p>
</div>
<div class="lang-en">
<p>CitySport is the shared technical foundation behind a family of local, community-driven sports apps. Each edition — same mobile app, same analytics dashboard for city agents — is adapted to one city: its districts, its facilities, its language. Choose an edition below to see its full profile.</p>
</div>

<!-- ═══════════════════════════════════════════════ CITY CARDS ═══ -->

<div class="cs-section-label">
  <span class="lang-fr">Éditions disponibles</span>
  <span class="lang-en">Available editions</span>
</div>

<div class="cs-city-grid">
  <a class="cs-city-card" href="./Toulouse-Sport.html">
    <img class="cs-city-banner" src="/img/toulouse-sport/capitole-banner.png" alt="Toulouse" />
    <div class="cs-city-body">
      <span class="cs-status cs-status-live lang-fr">🇫🇷 En ligne à Toulouse</span>
      <span class="cs-status cs-status-live lang-en">🇫🇷 Live in Toulouse</span>
      <h3>Toulouse Sport</h3>
      <div class="cs-city-tag lang-fr">L'application qui connecte les Toulousains par le sport</div>
      <div class="cs-city-tag lang-en">The app that connects Toulouse residents through sport</div>
      <div class="cs-city-cta"><span class="lang-fr">Découvrir Toulouse Sport</span><span class="lang-en">Discover Toulouse Sport</span> →</div>
    </div>
  </a>

  <a class="cs-city-card" href="./NYSport.html">
    <img class="cs-city-banner" src="/img/ny-sport/nyc-skyline-banner.png" alt="New York City" />
    <div class="cs-city-body">
      <span class="cs-status cs-status-pilot lang-fr">🇺🇸 Prête pour un pilote à New York</span>
      <span class="cs-status cs-status-pilot lang-en">🇺🇸 Pilot-ready for New York City</span>
      <h3>NY Sport</h3>
      <div class="cs-city-tag lang-fr">L'application qui connecte les New-Yorkais par le sport</div>
      <div class="cs-city-tag lang-en">The app that connects New Yorkers through sport</div>
      <div class="cs-city-cta"><span class="lang-fr">Découvrir NY Sport</span><span class="lang-en">Discover NY Sport</span> →</div>
    </div>
  </a>
</div>

---

<!-- ═══════════════════════════════════════════════ WHY CITYSPORT ═══ -->

<div class="lang-fr">
<div class="cs-section-label">Pourquoi CitySport</div>
<h2 style="text-align:center;">Une seule plateforme, adaptée à chaque territoire</h2>
</div>
<div class="lang-en">
<div class="cs-section-label">Why CitySport</div>
<h2 style="text-align:center;">One platform, adapted to every territory</h2>
</div>

<div class="cs-value-grid">
  <div class="cs-value-card">
    <div class="icon">🏗️</div>
    <strong class="lang-fr">Base technique éprouvée</strong>
    <strong class="lang-en">Proven technical foundation</strong>
    <span class="lang-fr">Le même moteur — application mobile React Native + dashboard analytique Next.js — déjà en production à Toulouse.</span>
    <span class="lang-en">The same engine — React Native mobile app + Next.js analytics dashboard — already running in production in Toulouse.</span>
  </div>
  <div class="cs-value-card">
    <div class="icon">📊</div>
    <strong class="lang-fr">Intelligence territoriale</strong>
    <strong class="lang-en">Territorial intelligence</strong>
    <span class="lang-fr">Un dashboard exclusif donne aux agents de chaque ville une vision en temps réel des usages sportifs spontanés.</span>
    <span class="lang-en">An exclusive dashboard gives each city's agents real-time visibility into spontaneous sports activity.</span>
  </div>
  <div class="cs-value-card">
    <div class="icon">💸</div>
    <strong class="lang-fr">Zéro charge pour la collectivité</strong>
    <strong class="lang-en">Zero burden for the city</strong>
    <span class="lang-fr">Gratuite pour les habitants, sans intégration SI requise, sans maintenance côté ville.</span>
    <span class="lang-en">Free for residents, no IT integration required, no maintenance on the city's side.</span>
  </div>
  <div class="cs-value-card">
    <div class="icon">🌍</div>
    <strong class="lang-fr">Pensée pour se dupliquer</strong>
    <strong class="lang-en">Built to replicate</strong>
    <span class="lang-fr">Chaque nouvelle édition (langue, quartiers, équipements) se déploie sur la même base — de Toulouse à New York.</span>
    <span class="lang-en">Each new edition (language, districts, facilities) deploys on the same base — from Toulouse to New York.</span>
  </div>
</div>

<div class="cs-cta-bar">
  <a href="/my-cv.html" class="cs-btn cs-btn-primary">👤 <span class="lang-fr">Voir mon profil</span><span class="lang-en">View my profile</span></a>
  <a href="/my-perso-projects.html" class="cs-btn cs-btn-secondary">← <span class="lang-fr">Autres projets</span><span class="lang-en">Other projects</span></a>
</div>

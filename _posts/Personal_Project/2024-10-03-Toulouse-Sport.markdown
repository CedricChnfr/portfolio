---
layout: default
title:  "Toulouse Sport"
date:   2024-10-02 10:56:03 +0200
---

<style>
p { text-align: justify; }

.ts-hero {
  background: linear-gradient(135deg, #1e3a5f 0%, #2563eb 100%);
  color: white;
  border-radius: 12px;
  padding: 2.5rem 2rem;
  margin-bottom: 2rem;
  text-align: center;
}
.ts-hero h1 { color: white; margin-bottom: 0.5rem; font-size: 2rem; }
.ts-hero p  { color: #bfdbfe; text-align: center; font-size: 1.05rem; margin: 0; }
.ts-hero .tagline { font-size: 1.2rem; color: #93c5fd; margin-bottom: 1rem; }

.ts-badges {
  display: flex; flex-wrap: wrap; gap: 0.5rem;
  justify-content: center; margin-top: 1.2rem;
}
.ts-badge {
  background: rgba(255,255,255,0.15);
  border: 1px solid rgba(255,255,255,0.3);
  border-radius: 20px;
  padding: 0.3rem 0.9rem;
  font-size: 0.8rem;
  color: white;
}

.ts-value-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1rem;
  margin: 1.5rem 0;
}
.ts-value-card {
  background: #f8faff;
  border: 1px solid #dbeafe;
  border-radius: 10px;
  padding: 1.2rem;
}
.ts-value-card .icon { font-size: 1.8rem; margin-bottom: 0.5rem; }
.ts-value-card strong { display: block; margin-bottom: 0.4rem; color: #1e40af; }

.ts-kpi-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin: 1.5rem 0;
}
.ts-kpi {
  text-align: center;
  background: #eff6ff;
  border-radius: 10px;
  padding: 1rem;
}
.ts-kpi .number { font-size: 2rem; font-weight: 700; color: #2563eb; }
.ts-kpi .label  { font-size: 0.8rem; color: #64748b; margin-top: 0.2rem; }

.ts-offer {
  background: linear-gradient(135deg, #0f172a 0%, #1e3a5f 100%);
  color: white;
  border-radius: 12px;
  padding: 2rem;
  margin: 1.5rem 0;
}
.ts-offer h3 { color: #93c5fd; margin-bottom: 1rem; }
.ts-offer ul { color: #e2e8f0; }

.ts-cta-bar {
  display: flex; gap: 1rem; flex-wrap: wrap;
  justify-content: center; margin: 2rem 0;
}
.ts-btn {
  display: inline-block;
  padding: 0.75rem 1.8rem;
  border-radius: 8px;
  font-weight: 600;
  text-decoration: none;
  font-size: 0.95rem;
  transition: opacity 0.2s;
}
.ts-btn:hover { opacity: 0.85; text-decoration: none; }
.ts-btn-primary { background: #2563eb; color: white; }
.ts-btn-secondary { background: #f1f5f9; color: #1e3a5f; border: 1px solid #cbd5e1; }

.ts-step { display: flex; gap: 1rem; margin-bottom: 1rem; align-items: flex-start; }
.ts-step-num {
  background: #2563eb; color: white; border-radius: 50%;
  width: 28px; height: 28px; flex-shrink: 0;
  display: flex; align-items: center; justify-content: center;
  font-weight: 700; font-size: 0.85rem; margin-top: 2px;
}

.ts-section-label {
  text-transform: uppercase; letter-spacing: 0.1em;
  font-size: 0.75rem; color: #2563eb; font-weight: 700;
  margin-bottom: 0.3rem;
}

.highlight-box {
  border-left: 4px solid #2563eb;
  background: #eff6ff;
  padding: 1rem 1.2rem;
  border-radius: 0 8px 8px 0;
  margin: 1.2rem 0;
}
</style>

<div class="back-nav">
    <a href="./my-perso-projects.html" data-i18n-html="back-perso-projects">&larr; Retour aux Projets Personnels</a>
</div>

<!-- ═══════════════════════════════════════════════ HERO ═══ -->

<div class="ts-hero">
  <div class="lang-fr">
    <h1>Toulouse Sport</h1>
    <p class="tagline">L'application qui connecte les Toulousains par le sport</p>
    <p>Application mobile gratuite (iOS &amp; Android) + Dashboard analytique temps réel pour les agents de la collectivité</p>
  </div>
  <div class="lang-en">
    <h1>Toulouse Sport</h1>
    <p class="tagline">The app that connects Toulouse residents through sport</p>
    <p>Free mobile app (iOS &amp; Android) + Real-time analytics dashboard for city hall agents</p>
  </div>
  <div class="ts-badges">
    <span class="ts-badge">React Native</span>
    <span class="ts-badge">Next.js 15</span>
    <span class="ts-badge">Supabase</span>
    <span class="ts-badge">TypeScript</span>
    <span class="ts-badge">iOS &amp; Android</span>
    <span class="ts-badge">RGPD ✓</span>
    <span class="ts-badge">Hébergement EU ✓</span>
  </div>
</div>

<!-- ─── CTA top ─── -->
<div class="ts-cta-bar">
  <a href="/my-cv.html" class="ts-btn ts-btn-primary" data-i18n-html="btn-see-profile">👤 Voir mon profil</a>
  <a href="/my-perso-projects.html" class="ts-btn ts-btn-secondary" data-i18n-html="btn-other-projects">← Autres projets</a>
</div>

---

<!-- ═══════════════════════════════════════════════ PROBLÈME ═══ -->

<div class="lang-fr">
<div class="ts-section-label">Le problème</div>
<h2>Faire du sport à Toulouse : un frein invisible</h2>

<p>Les Toulousains veulent faire du sport mais peinent à trouver des partenaires de leur niveau, près de chez eux. Pendant ce temps, les équipements sportifs municipaux sont sous-occupés — faute d'outils pour mettre en relation les habitants qui veulent les utiliser spontanément.</p>

<div class="ts-value-grid">
  <div class="ts-value-card">
    <div class="icon">🏟️</div>
    <strong>Équipements sous-utilisés</strong>
    Les terrains, salles et espaces sportifs publics sont souvent vides faute d'organisation entre habitants.
  </div>
  <div class="ts-value-card">
    <div class="icon">🔍</div>
    <strong>Partenaires introuvables</strong>
    Aucun outil simple pour trouver quelqu'un de son niveau pour jouer au tennis ou courir ensemble.
  </div>
  <div class="ts-value-card">
    <div class="icon">📊</div>
    <strong>Zéro donnée pour la ville</strong>
    Malgré 38 M€/an investis dans le sport, aucune donnée fine n'existe sur la pratique sportive spontanée des citoyens.
  </div>
  <div class="ts-value-card">
    <div class="icon">🏘️</div>
    <strong>Isolement social</strong>
    Les nouveaux arrivants et étudiants peinent à s'intégrer dans des cercles sportifs existants.
  </div>
</div>
</div>

<div class="lang-en">
<div class="ts-section-label">The Problem</div>
<h2>Playing sport in Toulouse: an invisible barrier</h2>

<p>Toulouse residents want to play sports but struggle to find partners at their level, near their home. Meanwhile, municipal sports facilities sit under-used — for lack of tools to connect residents who want to use them spontaneously.</p>

<div class="ts-value-grid">
  <div class="ts-value-card">
    <div class="icon">🏟️</div>
    <strong>Under-used facilities</strong>
    Public sports grounds, gyms, and spaces are often empty due to lack of coordination between residents.
  </div>
  <div class="ts-value-card">
    <div class="icon">🔍</div>
    <strong>Partners nowhere to be found</strong>
    No simple tool to find someone at your level to play tennis or go running together.
  </div>
  <div class="ts-value-card">
    <div class="icon">📊</div>
    <strong>Zero data for the city</strong>
    Despite €38M/year invested in sport, no fine-grained data exists on citizens' spontaneous sports activity.
  </div>
  <div class="ts-value-card">
    <div class="icon">🏘️</div>
    <strong>Social isolation</strong>
    Newcomers and students struggle to integrate into existing sports circles.
  </div>
</div>
</div>

---

<!-- ═══════════════════════════════════════════════ SOLUTION ═══ -->

<div class="lang-fr">
<div class="ts-section-label">La solution</div>
<h2>Toulouse Sport — Une plateforme communautaire sportive, 100% locale</h2>

<p>Toulouse Sport est une <strong>application mobile gratuite</strong> (iOS &amp; Android) qui permet à chaque habitant de Toulouse de créer ou rejoindre une activité sportive en moins de 2 minutes, trouver des partenaires de son niveau dans son quartier, et découvrir les équipements géolocalisés sur la carte interactive.</p>

<div class="highlight-box">
  Un habitant crée une activité : <em>"Football à Empalot, samedi 10h, niveau débutant, 8 places"</em> — d'autres rejoignent, un chat s'ouvre, l'activité a lieu. Simple, gratuit, immédiat.
</div>
</div>

<div class="lang-en">
<div class="ts-section-label">The Solution</div>
<h2>Toulouse Sport — A community sports platform, 100% local</h2>

<p>Toulouse Sport is a <strong>free mobile app</strong> (iOS &amp; Android) that lets every Toulouse resident create or join a sports activity in under 2 minutes, find partners at their level in their district, and discover geolocated facilities on an interactive map.</p>

<div class="highlight-box">
  A resident creates an activity: <em>"Football at Empalot, Saturday 10am, beginner level, 8 spots"</em> — others join, a chat opens, the activity happens. Simple, free, immediate.
</div>
</div>

<!-- KPIs -->
<div class="ts-kpi-grid">
  <div class="ts-kpi"><div class="number">30+</div><div class="label">Sports (football, tennis, yoga, padel, pétanque, trail...)</div></div>
  <div class="ts-kpi"><div class="number">12</div><div class="label lang-fr">Quartiers de Toulouse couverts</div><div class="label lang-en">Toulouse districts covered</div></div>
  <div class="ts-kpi"><div class="number">200+</div><div class="label lang-fr">Équipements sportifs géolocalisés</div><div class="label lang-en">Geolocated sports facilities</div></div>
  <div class="ts-kpi"><div class="number">3</div><div class="label lang-fr">Niveaux de pratique</div><div class="label lang-en">Skill levels</div></div>
  <div class="ts-kpi"><div class="number">100%</div><div class="label lang-fr">Gratuit pour les utilisateurs</div><div class="label lang-en">Free for end users</div></div>
  <div class="ts-kpi"><div class="number">iOS + Android</div><div class="label lang-fr">Application native</div><div class="label lang-en">Native application</div></div>
</div>

---

<!-- ═══════════════════════════════════════════════ SCREENSHOTS APP ═══ -->

<div class="lang-fr">
<div class="ts-section-label">L'application mobile</div>
<h2>Découvrir, rejoindre, créer — en quelques taps</h2>
</div>
<div class="lang-en">
<div class="ts-section-label">The mobile app</div>
<h2>Discover, join, create — in a few taps</h2>
</div>

<img src="/img/toulouse-sport/home.png" alt="Écran principal" style="width:32%; display:inline-block; margin-right:1%;"/>
<img src="/img/toulouse-sport/map.png" alt="Carte interactive" style="width:32%; display:inline-block; margin-right:1%;"/>
<img src="/img/toulouse-sport/profile.png" alt="Profil utilisateur" style="width:32%; display:inline-block;"/>

<p style="text-align:center; color:#64748b; font-size:0.85rem; margin-top:0.5rem;">
  <span class="lang-fr">Fil d'activités avec calendrier · Carte interactive Toulouse · Profil avec statistiques personnelles</span>
  <span class="lang-en">Activity feed with calendar · Interactive Toulouse map · Profile with personal statistics</span>
</p>

<img src="/img/toulouse-sport/new-activity.png" alt="Créer une activité" style="width:32%; display:inline-block; margin-right:1%;"/>
<img src="/img/toulouse-sport/activity-detail.png" alt="Détail activité et chat" style="width:32%; display:inline-block; margin-right:1%;"/>
<img src="/img/toulouse-sport/friends.png" alt="Réseau social" style="width:32%; display:inline-block;"/>

<p style="text-align:center; color:#64748b; font-size:0.85rem; margin-top:0.5rem;">
  <span class="lang-fr">Création d'activité · Détail avec chat temps réel · Réseau d'amis</span>
  <span class="lang-en">Activity creation · Detail with real-time chat · Friends network</span>
</p>

<img src="/img/toulouse-sport/notifications.png" alt="Notifications" style="width:32%; display:inline-block;"/>

---

<!-- ═══════════════════════════════════════════════ PARCOURS ═══ -->

<div class="lang-fr">
<div class="ts-section-label">Parcours utilisateur</div>
<h2>De l'inscription à l'activité en 6 étapes</h2>

<div class="ts-step"><div class="ts-step-num">1</div><div><strong>Inscription &amp; personnalisation</strong> — profil, quartier, sports favoris, niveau. L'application s'adapte immédiatement.</div></div>
<div class="ts-step"><div class="ts-step-num">2</div><div><strong>Trouver une activité</strong> — fil d'actualité filtré, vue calendrier sur 14 jours, carte interactive avec toutes les venues de Toulouse.</div></div>
<div class="ts-step"><div class="ts-step-num">3</div><div><strong>Rejoindre en un tap</strong> — si des places sont disponibles. Système de liste d'attente avec promotion automatique si une place se libère.</div></div>
<div class="ts-step"><div class="ts-step-num">4</div><div><strong>Chat temps réel</strong> — messagerie intégrée par activité, accessible aux participants uniquement. Notifications push pour les messages et rappels.</div></div>
<div class="ts-step"><div class="ts-step-num">5</div><div><strong>Inviter ses amis</strong> — système d'amis intégré : recherche par pseudo, envoi d'invitation, inviter directement depuis une activité.</div></div>
<div class="ts-step"><div class="ts-step-num">6</div><div><strong>Suivre ses progrès</strong> — statistiques personnelles (activités créées, rejointes, personnes rencontrées, sports pratiqués, streak hebdomadaire).</div></div>
</div>

<div class="lang-en">
<div class="ts-section-label">User Journey</div>
<h2>From sign-up to activity in 6 steps</h2>

<div class="ts-step"><div class="ts-step-num">1</div><div><strong>Sign-up &amp; personalization</strong> — profile, district, favorite sports, skill level. The app adapts immediately.</div></div>
<div class="ts-step"><div class="ts-step-num">2</div><div><strong>Find an activity</strong> — filtered activity feed, 14-day calendar view, interactive map with all Toulouse venues.</div></div>
<div class="ts-step"><div class="ts-step-num">3</div><div><strong>Join with one tap</strong> — if spots are available. Waiting list with automatic promotion if a spot opens up.</div></div>
<div class="ts-step"><div class="ts-step-num">4</div><div><strong>Real-time chat</strong> — per-activity messaging, accessible to participants only. Push notifications for messages and reminders.</div></div>
<div class="ts-step"><div class="ts-step-num">5</div><div><strong>Invite friends</strong> — integrated friend system: search by username, send invitation, invite directly from an activity.</div></div>
<div class="ts-step"><div class="ts-step-num">6</div><div><strong>Track progress</strong> — personal stats (activities created, joined, people met, sports played, weekly streak).</div></div>
</div>

---

<!-- ═══════════════════════════════════════════════ DASHBOARD ═══ -->

<div class="lang-fr">
<div class="ts-section-label">Pour la collectivité</div>
<h2>Dashboard analytique — Accès exclusif agents de la mairie</h2>

<p>En parallèle de l'application mobile, un <strong>dashboard web analytique</strong> donne aux agents de la collectivité une <strong>intelligence territoriale sport en temps réel</strong>, impossible à obtenir autrement. Quels sports, quels quartiers, quels horaires, quels équipements sont réellement utilisés par les citoyens — pour la première fois, ces données existent.</p>

<div class="highlight-box">
  <strong>Accès sécurisé</strong> : connexion nominative, rôles agent / admin, données 100% anonymisées et agrégées — aucune donnée personnelle transmise à la collectivité (conforme RGPD).
</div>
</div>

<div class="lang-en">
<div class="ts-section-label">For the city</div>
<h2>Analytics Dashboard — Exclusive access for city hall agents</h2>

<p>Alongside the mobile app, a <strong>web analytics dashboard</strong> gives municipal agents <strong>real-time territorial sports intelligence</strong>, impossible to obtain otherwise. Which sports, which districts, which time slots, which facilities are actually being used by citizens — for the first time, this data exists.</p>

<div class="highlight-box">
  <strong>Secured access</strong>: named logins, agent / admin roles, 100% anonymized and aggregated data — no personal data transmitted to the city (GDPR compliant).
</div>
</div>

<img src="/img/toulouse-sport/dashboard-login.png" alt="Dashboard - Connexion agents mairie" style="width:48%; display:inline-block; margin-right:2%;"/>
<img src="/img/toulouse-sport/dashboard-overview.png" alt="Dashboard - KPIs temps réel" style="width:48%; display:inline-block;"/>
<p style="text-align:center; color:#64748b; font-size:0.85rem; margin-top:0.5rem;">
  <span class="lang-fr">Page de connexion sécurisée · Vue d'ensemble KPIs temps réel</span>
  <span class="lang-en">Secure login page · Real-time KPI overview</span>
</p>

<div class="lang-fr">
<h3>Vue d'ensemble — 10 KPIs + 14 graphiques</h3>
<p>Filtrable par période (7j, 30j, 3 mois, 1 an, dates libres), sport, quartier et niveau de pratique :</p>
<ul>
<li><strong>10 KPI cards</strong> : utilisateurs inscrits, organisateurs actifs, nouveaux inscrits, séances organisées, inscriptions, taux d'engagement, taux de remplissage, moyenne participants, récurrence, annulations</li>
<li><strong>Funnel d'engagement</strong> : conversion inscrits → actifs → participants</li>
<li><strong>Tendances</strong> : courbe globale, évolution 12 mois, tendance par sport (top 4)</li>
<li><strong>Heatmap jour × créneau</strong> : densité des activités par moment de la journée</li>
<li><strong>Répartition par sport</strong> (pie chart) et <strong>sports par quartier</strong> (stacked bar)</li>
<li><strong>Zones prioritaires</strong> : quartiers nécessitant une attention particulière</li>
<li><strong>Top 10 équipements</strong> : classement des venues les plus utilisées</li>
<li><strong>Panel d'insights automatiques</strong> : alertes et tendances générées depuis les KPIs</li>
<li><strong>Export PDF</strong> : rapport complet exportable en un clic, prêt pour le conseil municipal</li>
</ul>
</div>

<div class="lang-en">
<h3>Overview — 10 KPIs + 14 charts</h3>
<p>Filterable by period (7d, 30d, 3 months, 1 year, custom dates), sport, district, and skill level:</p>
<ul>
<li><strong>10 KPI cards</strong>: registered users, active organizers, new signups, sessions organized, participations, engagement rate, fill rate, avg participants, repeat rate, cancellations</li>
<li><strong>Engagement funnel</strong>: registered → active → participants conversion</li>
<li><strong>Trends</strong>: global curve, 12-month evolution, per-sport trend (top 4)</li>
<li><strong>Day × time slot heatmap</strong>: activity density by time of day</li>
<li><strong>Sport breakdown</strong> (pie chart) and <strong>sports by district</strong> (stacked bar)</li>
<li><strong>Priority zones</strong>: districts needing special attention</li>
<li><strong>Top 10 equipment</strong>: ranking of most-used venues</li>
<li><strong>Auto insights panel</strong>: alerts and trends generated from KPIs</li>
<li><strong>PDF export</strong>: full exportable report in one click, ready for city council</li>
</ul>
</div>

<img src="/img/toulouse-sport/dashboard-full.png" alt="Dashboard - Vue complète" style="width:100%; display:block; margin-bottom:1rem;"/>

<div class="lang-fr"><h3>Carte de chaleur</h3>
<p>Visualisation géographique de l'intensité des activités sportives sur Toulouse. Les zones les plus actives ressortent clairement pour identifier les équipements sous-utilisés et orienter les actions de terrain.</p>
</div>
<div class="lang-en"><h3>Heat Map</h3>
<p>Geographic visualization of sports activity intensity across Toulouse. The most active areas stand out clearly to identify under-used facilities and guide field actions.</p>
</div>

<img src="/img/toulouse-sport/dashboard-carte.png" alt="Dashboard - Carte de chaleur Toulouse" style="width:100%; display:block; margin-bottom:1rem;"/>

<div class="lang-fr"><h3>Calendrier des activités</h3>
<p>Vue mensuelle de toutes les séances créées sur la plateforme. Un clic sur un jour affiche le détail des activités : sport, lieu, heure, participants, organisateur.</p>
</div>
<div class="lang-en"><h3>Activity Calendar</h3>
<p>Monthly view of all sessions created on the platform. Clicking a day shows activity details: sport, location, time, participants, organizer.</p>
</div>

<img src="/img/toulouse-sport/dashboard-calendrier.png" alt="Dashboard - Calendrier des activités" style="width:100%; display:block; margin-bottom:1rem;"/>

<img src="/img/toulouse-sport/dashboard-signalements.png" alt="Dashboard - Signalements équipements" style="width:48%; display:inline-block; margin-right:2%;"/>
<img src="/img/toulouse-sport/dashboard-agents.png" alt="Dashboard - Administration agents" style="width:48%; display:inline-block;"/>
<p style="text-align:center; color:#64748b; font-size:0.85rem; margin-top:0.5rem;">
  <span class="lang-fr">Signalements d'équipements (suivi ouvert/résolu) · Administration des agents (rôles, accès)</span>
  <span class="lang-en">Equipment reports (open/resolved tracking) · Agent administration (roles, access)</span>
</p>

<div class="lang-fr">
<h3>Démo vidéo du dashboard</h3>
<p>Navigation complète dans le dashboard : vue d'ensemble, filtres, graphiques, carte de chaleur, calendrier, signalements et gestion des agents.</p>
</div>
<div class="lang-en">
<h3>Dashboard Video Demo</h3>
<p>Full navigation through the dashboard: overview, filters, charts, heat map, calendar, equipment reports, and agent management.</p>
</div>

<video controls style="width:100%; border-radius:8px; margin-bottom:1.5rem;" poster="/img/toulouse-sport/dashboard-overview.png">
  <source src="/img/toulouse-sport/dashboard.mp4" type="video/mp4" />
</video>

---

<!-- ═══════════════════════════════════════════════ VALEUR MAIRIE ═══ -->

<div class="lang-fr">
<div class="ts-section-label">Valeur pour la collectivité</div>
<h2>5 bénéfices directs pour la Mairie de Toulouse</h2>
<div class="ts-value-grid">
  <div class="ts-value-card">
    <div class="icon">📈</div>
    <strong>Données d'usage en temps réel</strong>
    Pour la première fois : quels sports, quels quartiers, quels horaires, quels équipements sont réellement utilisés — une intelligence territoriale impossible à obtenir autrement.
  </div>
  <div class="ts-value-card">
    <div class="icon">🏟️</div>
    <strong>Valorisation du patrimoine sportif</strong>
    Les 200+ équipements publics (stades, gymnases, parcs) mis en visibilité et activés par la communauté. Zéro charge opérationnelle pour la ville.
  </div>
  <div class="ts-value-card">
    <div class="icon">❤️</div>
    <strong>Levier de santé publique</strong>
    La pratique régulière encouragée par la gamification. L'application s'inscrit directement dans les objectifs de prévention santé de la ville.
  </div>
  <div class="ts-value-card">
    <div class="icon">🤝</div>
    <strong>Outil de cohésion sociale</strong>
    Facilite le brassage entre quartiers et profils sociaux, en ligne avec les valeurs de mixité portées par la Mairie.
  </div>
  <div class="ts-value-card">
    <div class="icon">⚙️</div>
    <strong>Zéro charge opérationnelle</strong>
    L'application gère elle-même les inscriptions, la modération et les notifications. Aucun agent municipal requis. Solution clé en main.
  </div>
</div>
</div>

<div class="lang-en">
<div class="ts-section-label">Value for the city</div>
<h2>5 direct benefits for Toulouse City Hall</h2>
<div class="ts-value-grid">
  <div class="ts-value-card">
    <div class="icon">📈</div>
    <strong>Real-time usage data</strong>
    For the first time: which sports, which districts, which time slots, which facilities are actually being used — territorial intelligence impossible to obtain otherwise.
  </div>
  <div class="ts-value-card">
    <div class="icon">🏟️</div>
    <strong>Sports heritage enhancement</strong>
    30+ public facilities (stadiums, gyms, parks) made visible and activated by the community. Zero operational burden for the city.
  </div>
  <div class="ts-value-card">
    <div class="icon">❤️</div>
    <strong>Public health lever</strong>
    Regular practice encouraged through gamification. The app directly aligns with the city's health prevention objectives.
  </div>
  <div class="ts-value-card">
    <div class="icon">🤝</div>
    <strong>Social cohesion tool</strong>
    Facilitates mixing between districts and social profiles, aligned with the city's social diversity values.
  </div>
  <div class="ts-value-card">
    <div class="icon">⚙️</div>
    <strong>Zero operational burden</strong>
    The app self-manages registrations, moderation, and notifications. No city agent required. Turnkey solution.
  </div>
</div>
</div>

---

<!-- ═══════════════════════════════════════════════ SÉCURITÉ ═══ -->

<div class="lang-fr">
<div class="ts-section-label">Technologie &amp; conformité</div>
<h2>Une infrastructure sécurisée, hébergée en Europe</h2>
</div>
<div class="lang-en">
<div class="ts-section-label">Technology &amp; Compliance</div>
<h2>A secure infrastructure, hosted in Europe</h2>
</div>

<table>
<tr><th>Élément / Element</th><th>Détail / Detail</th><th>Statut / Status</th></tr>
<tr><td>Hébergement géographique</td><td>AWS eu-west-1 — Dublin, Irlande (UE)</td><td>✅ Conforme RGPD</td></tr>
<tr><td>Chiffrement transit</td><td>HTTPS / TLS 1.3 obligatoire</td><td>✅ Actif</td></tr>
<tr><td>Chiffrement au repos</td><td>AES-256 (chiffrement AWS disque)</td><td>✅ Actif</td></tr>
<tr><td>Contrôle d'accès</td><td>Row Level Security PostgreSQL sur toutes les tables</td><td>✅ Actif</td></tr>
<tr><td>Authentification</td><td>JWT signés + bcrypt, expiration 1h + refresh token</td><td>✅ Actif</td></tr>
<tr><td>Données collectivité</td><td>100% agrégées et anonymisées — aucune donnée personnelle transmise</td><td>✅ Garanti</td></tr>
<tr><td>DPA sous-traitant</td><td>DPA signé avec Supabase</td><td>✅ Signé</td></tr>
<tr><td>SLA infrastructure</td><td>99,9% garanti contractuellement (plan Pro Supabase)</td><td>✅ Contractuel</td></tr>
<tr><td>Sauvegardes</td><td>Automatiques quotidiennes, rétention 30 jours</td><td>✅ Actif</td></tr>
<tr><td>Intégration SI requis</td><td>Aucune en phase 1 — accès dashboard via navigateur uniquement</td><td>✅ Clé en main</td></tr>
</table>

<div class="lang-fr">
<p><strong>Ce que la collectivité n'a PAS à faire :</strong> aucune installation sur ses serveurs, aucune maintenance d'infrastructure, aucune gestion des mises à jour, aucune modération des utilisateurs.</p>
</div>
<div class="lang-en">
<p><strong>What the city does NOT have to do:</strong> no installation on their servers, no infrastructure maintenance, no update management, no user moderation.</p>
</div>

---

<!-- ═══════════════════════════════════════════════ STACK ═══ -->

<div class="lang-fr">
<div class="ts-section-label">Architecture technique</div>
<h2>Stack complet</h2>
</div>
<div class="lang-en">
<div class="ts-section-label">Technical Architecture</div>
<h2>Full Stack</h2>
</div>

<table>
<tr><th>Composant / Component</th><th>Technologies</th></tr>
<tr><td><strong>Application mobile</strong></td><td>React Native 0.81, Expo 54, TypeScript 5.9, React 19</td></tr>
<tr><td><strong>Dashboard web collectivité</strong></td><td>Next.js 15, React 19, TailwindCSS, Recharts, Lucide Icons</td></tr>
<tr><td><strong>Navigation mobile</strong></td><td>React Navigation 6 (Stack + Bottom Tabs + Deep Linking)</td></tr>
<tr><td><strong>Backend</strong></td><td>Supabase (PostgreSQL 15, Auth, Storage, Realtime WebSockets)</td></tr>
<tr><td><strong>Authentification</strong></td><td>Supabase Auth — email/mdp, OAuth Google &amp; Apple (PKCE)</td></tr>
<tr><td><strong>Temps réel</strong></td><td>Supabase Realtime (WebSockets) — chat activités, notifications</td></tr>
<tr><td><strong>Notifications push</strong></td><td>Expo Notifications + Supabase Edge Functions</td></tr>
<tr><td><strong>Carte interactive</strong></td><td>React Native Maps (mobile) + composants carte (dashboard)</td></tr>
<tr><td><strong>Base de données</strong></td><td>PostgreSQL 15, 12 tables, RLS activé, 72 migrations versionnées</td></tr>
<tr><td><strong>Internationalisation</strong></td><td>i18next (FR / EN) + date-fns localisation française</td></tr>
<tr><td><strong>Thème</strong></td><td>Context API (mode clair / sombre)</td></tr>
<tr><td><strong>Upload &amp; stockage</strong></td><td>Expo Image Picker + Supabase Storage (S3-compatible)</td></tr>
</table>

---

<!-- ═══════════════════════════════════════════════ ROADMAP ═══ -->

<div class="lang-fr">
<div class="ts-section-label">Roadmap</div>
<h2>Vision &amp; prochaines étapes</h2>

<p><strong>Court terme (0–6 mois)</strong></p>
<ul>
<li>✅ Application mobile fonctionnelle iOS &amp; Android</li>
<li>✅ Dashboard analytique agents mairie</li>
<li>📋 Lancement public avec communication de la Mairie</li>
<li>📋 Enrichissement de la base des équipements municipaux</li>
<li>📋 Intégration des événements sportifs officiels de la ville dans le calendrier</li>
</ul>

<p><strong>Moyen terme (6–18 mois)</strong></p>
<ul>
<li>📋 API partenaire pour les clubs et associations sportives agréées</li>
<li>📋 Messagerie directe entre amis, groupes pour équipes récurrentes</li>
<li>📋 Intégration calendrier iOS/Android</li>
<li>📋 Recommandations d'activités personnalisées</li>
</ul>

<p><strong>Long terme (18 mois+)</strong></p>
<ul>
<li>📋 Extension aux 37 communes de Toulouse Métropole</li>
<li>📋 Déploiement white-label pour d'autres villes françaises</li>
<li>📋 Programme de récompenses en partenariat avec la Mairie</li>
<li>📋 Synchronisation trackers fitness (Strava, Garmin)</li>
</ul>
</div>

<div class="lang-en">
<div class="ts-section-label">Roadmap</div>
<h2>Vision &amp; Next Steps</h2>

<p><strong>Short term (0–6 months)</strong></p>
<ul>
<li>✅ Functional mobile app iOS &amp; Android</li>
<li>✅ Analytics dashboard for city agents</li>
<li>📋 Public launch with City Hall communication</li>
<li>📋 Enrichment of the municipal facilities database</li>
<li>📋 Integration of official city sports events into the calendar</li>
</ul>

<p><strong>Medium term (6–18 months)</strong></p>
<ul>
<li>📋 Partner API for approved sports clubs and associations</li>
<li>📋 Direct messaging between friends, groups for recurring teams</li>
<li>📋 iOS/Android calendar integration</li>
<li>📋 Personalized activity recommendations</li>
</ul>

<p><strong>Long term (18 months+)</strong></p>
<ul>
<li>📋 Expansion to all 37 communes of Toulouse Métropole</li>
<li>📋 White-label deployment for other French cities</li>
<li>📋 Rewards program in partnership with City Hall</li>
<li>📋 Fitness tracker sync (Strava, Garmin)</li>
</ul>
</div>

---

<!-- ═══════════════════════════════════════════════ CTA FINAL ═══ -->

<div class="lang-fr">
<div class="ts-section-label">En résumé</div>
<h2>Toulouse Sport : prête, locale, gratuite pour les citoyens</h2>
<ul>
<li>✅ Application <strong>100% toulousaine</strong>, pensée pour les besoins réels des habitants</li>
<li>✅ <strong>Gratuite</strong> pour les utilisateurs, sans publicité intrusive</li>
<li>✅ <strong>Déjà fonctionnelle</strong> — React Native, Supabase, temps réel</li>
<li>✅ <strong>30+ sports, 12 quartiers, 200+ lieux</strong> — couverture immédiate de toute la ville</li>
<li>✅ <strong>Dashboard analytique</strong> exclusif pour les agents de la collectivité</li>
<li>✅ <strong>RGPD</strong>, hébergement EU, RLS, chiffrement — conforme dès aujourd'hui</li>
</ul>
</div>

<div class="lang-en">
<div class="ts-section-label">In summary</div>
<h2>Toulouse Sport: ready, local, free for citizens</h2>
<ul>
<li>✅ <strong>100% local app</strong>, built for the real needs of Toulouse residents</li>
<li>✅ <strong>Free</strong> for users, no intrusive advertising</li>
<li>✅ <strong>Already functional</strong> — React Native, Supabase, real-time</li>
<li>✅ <strong>30+ sports, 12 districts, 30+ venues</strong> — immediate full-city coverage</li>
<li>✅ <strong>Analytics dashboard</strong> exclusive for city agents</li>
<li>✅ <strong>GDPR</strong>, EU hosting, RLS, encryption — compliant from day one</li>
</ul>
</div>

<div class="ts-cta-bar">
  <a href="/my-cv.html" class="ts-btn ts-btn-primary">👤 <span class="lang-fr">Voir mon profil</span><span class="lang-en">View my profile</span></a>
  <a href="/my-perso-projects.html" class="ts-btn ts-btn-secondary">← <span class="lang-fr">Autres projets</span><span class="lang-en">Other projects</span></a>
</div>

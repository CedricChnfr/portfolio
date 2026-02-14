---
layout: default
title:  "IA Automation"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

<style>
p {
  text-align: justify;
}
</style>

<div class="back-nav">
    <a href="./my-perso-projects.html" data-i18n-html="back-perso-projects">&larr; Retour aux Projets Personnels</a>
</div>

<div class="lang-fr">
<h1>Projet IA Automation - Vue d'ensemble</h1>

<p><strong><a href="https://video-automation.littlenuage.com/">Essayez l'application ici : https://video-automation.littlenuage.com/</a></strong></p>

<p>Ce projet est une plateforme de production video entierement automatisee propulsee par l'IA. A partir d'un simple sujet textuel, le systeme genere un script structure, cree des images, synthetise la narration, applique des animations de camera, ajoute des sous-titres et de la musique de fond, et livre une video prete a publier - le tout orchestre via une interface web Streamlit avec gestion de file d'attente et notifications Discord.</p>

<h2>Contexte du projet</h2>

<p>Developpe comme projet personnel pour industrialiser la creation de contenu video, cette plateforme elimine le besoin de montage manuel. Elle prend en charge plusieurs categories de videos (biographies de celebrites, documentaires geographiques, reportages d'actualite, analyses de films, monuments, oeuvres d'art), plusieurs langues (francais, anglais, espagnol) et deux modes de production (format court et format long). L'application est deployee en ligne et accessible a tous.</p>

<h2>Vue d'ensemble de l'architecture</h2>

<p>Le systeme suit une architecture modulaire orientee services avec une separation claire des responsabilites :</p>
</div>

<div class="lang-en">
<h1>IA Automation Project Overview</h1>

<p><strong><a href="https://video-automation.littlenuage.com/">Try the application here: https://video-automation.littlenuage.com/</a></strong></p>

<p>This project is a fully automated video production platform powered by AI. From a simple text topic, the system generates a structured script, creates images, synthesizes narration, applies camera animations, adds subtitles and background music, and delivers a ready-to-publish video -- all orchestrated through a Streamlit web interface with job queue management and Discord notifications.</p>

<h2>Project Context</h2>

<p>Developed as a personal project to industrialize video content creation, this platform eliminates the need for manual editing. It supports multiple video categories (celebrity biographies, geography documentaries, news reports, movie analyses, monuments, artworks), multiple languages (French, English, Spanish), and two production modes (short-form and long-form). The application is deployed online and accessible to anyone.</p>

<h2>Architecture Overview</h2>

<p>The system follows a modular, service-oriented architecture with clear separation of concerns:</p>
</div>

<pre><code>User (Streamlit UI)
    |
    v
app2.py --&gt; queue_manager.py --&gt; run_pipeline.py --&gt; pipeline_executor.py
                                                          |
                                    +---------------------+---------------------+
                                    v                     v                     v
                              services/             scripts/              AI Models
                          (script, image,       (generation &amp;          (SD, TTS, LLM,
                          audio, video)          processing)           CLIP, Whisper...)
</code></pre>

<div class="lang-fr">
<h2>Ce que j'ai developpe</h2>

<h3>1. Application Web Streamlit (app2.py)</h3>

<p>L'interface utilisateur principale construite avec Streamlit, remplacant le premier prototype Flask :</p>
<ul>
<li><strong>Acces authentifie</strong> via <code>streamlit_authenticator</code> avec identifiants YAML</li>
<li><strong>Configuration video</strong> : selection du type (celebrite, geographie, actu, film, oeuvre, monument), categorie, entite, mode (court/long), langue (FR/EN/ES)</li>
<li><strong>Interface a trois onglets</strong> : Generation (flux de travail etape par etape), File d'attente (gestion des taches), Historique (productions passees)</li>
<li><strong>Controle WebUI</strong> : surveillance et lancement du serveur WebUI Stable Diffusion directement depuis l'interface</li>
<li><strong>Preferences utilisateur</strong> : parametres persistants sauvegardes entre les sessions (<code>user_preferences.json</code>)</li>
<li><strong>Integration Excel</strong> : listes d'entites chargees depuis des fichiers Excel par categorie</li>
</ul>

<h3>2. Moteur d'execution du pipeline (pipeline_executor.py)</h3>

<p>L'orchestrateur principal implementant un pipeline robuste en 6 etapes :</p>
</div>

<div class="lang-en">
<h2>What I Developed</h2>

<h3>1. Streamlit Web Application (app2.py)</h3>

<p>The main user interface built with Streamlit, replacing the earlier Flask prototype:</p>
<ul>
<li><strong>Authenticated access</strong> via <code>streamlit_authenticator</code> with YAML-based credentials</li>
<li><strong>Video configuration</strong>: type selection (celebrity, geography, actu, movie, oeuvre, monument), category, entity, mode (short/long), language (FR/EN/ES)</li>
<li><strong>Three-tab interface</strong>: Generation (step-by-step workflow), Queue (job management), History (past productions)</li>
<li><strong>WebUI control</strong>: monitor and launch the Stable Diffusion WebUI server directly from the interface</li>
<li><strong>User preferences</strong>: persistent settings saved between sessions (<code>user_preferences.json</code>)</li>
<li><strong>Excel integration</strong>: entity lists loaded from category-specific Excel files</li>
</ul>

<h3>2. Pipeline Execution Engine (pipeline_executor.py)</h3>

<p>The core orchestrator implementing a robust 6-step pipeline:</p>
</div>

<table>
<tr><th>Step</th><th>Description</th><th>Script</th></tr>
<tr><td>1</td><td><strong>Script Generation</strong></td><td><code>generate_script.py</code> / <code>generate_script_actu.py</code></td></tr>
<tr><td>2</td><td><strong>Image Generation</strong></td><td><code>generate_image.py</code> / <code>get_image_pexels.py</code></td></tr>
<tr><td>3</td><td><strong>Audio Synthesis</strong></td><td><code>generate_audio.py</code></td></tr>
<tr><td>4</td><td><strong>Camera Movement &amp; Animation</strong></td><td><code>generate_movement.py</code> / <code>generate_movement_from_db.py</code></td></tr>
<tr><td>5</td><td><strong>Subtitle Alignment</strong></td><td><code>align_subtitles.py</code> (short mode)</td></tr>
<tr><td>6</td><td><strong>Music Generation</strong></td><td><code>generate_music.py</code> (short mode)</td></tr>
</table>

<div class="lang-fr">
<p>Fonctionnalites cles :</p>
<ul>
<li><strong>Execution parallele</strong> : les etapes 2 (images) et 3 (audio) s'executent simultanement</li>
<li><strong>Reessai automatique</strong> : jusqu'a 2 tentatives par etape en cas d'echec</li>
<li><strong>Gestion des processus</strong> : arret des processus orphelins avant chaque etape pour eviter les conflits de ressources</li>
<li><strong>Suivi d'execution</strong> : metriques de temps completes par etape et duree totale du pipeline</li>
</ul>

<h3>3. Systeme de file d'attente (queue_manager.py)</h3>

<p>Une file d'attente thread-safe pour la production video sequentielle :</p>
<ul>
<li><strong>Etat persistant</strong> stocke dans <code>generation_queue.json</code></li>
<li><strong>Cycle de vie des taches</strong> : en attente - en cours - termine/echoue</li>
<li><strong>Reprise apres echec</strong> : redemarrage d'une tache echouee a partir de l'etape exacte qui a echoue</li>
<li><strong>Historique</strong> : stocke les 50 dernieres taches terminees/echouees</li>
<li><strong>Statistiques</strong> : comptages en temps reel des taches en attente, en cours, terminees, echouees</li>
<li><strong>Thread worker global</strong> : traite les taches sequentiellement en arriere-plan</li>
</ul>

<h3>4. Couche de services (services/)</h3>

<p>Quatre classes de services encapsulent les E/S fichiers et l'execution de sous-processus :</p>
<ul>
<li><strong>script_service.py</strong> : charger, sauvegarder, generer et valider les fichiers JSON de scripts</li>
<li><strong>image_service.py</strong> : gerer les images/videos generees, suppression par scene, recuperation d'images avec mapping de scenes</li>
<li><strong>audio_service.py</strong> : resolution des chemins audio, verifications d'existence, segmentation audio, orchestration de generation</li>
<li><strong>video_service.py</strong> : generation de mouvements, alignement de sous-titres, overlay texte, integration musique, upload YouTube, decoupage TikTok</li>
</ul>

<p>Tous les services suivent un pattern coherent avec des chemins organises :</p>
</div>

<div class="lang-en">
<p>Key features:</p>
<ul>
<li><strong>Parallel execution</strong>: steps 2 (images) and 3 (audio) run concurrently</li>
<li><strong>Automatic retry</strong>: up to 2 retries per step on failure</li>
<li><strong>Process management</strong>: kills orphan processes before each step to prevent resource conflicts</li>
<li><strong>Execution tracking</strong>: full timing metrics per step and total pipeline duration</li>
</ul>

<h3>3. Job Queue System (queue_manager.py)</h3>

<p>A thread-safe job queue for sequential video production:</p>
<ul>
<li><strong>Persistent state</strong> stored in <code>generation_queue.json</code></li>
<li><strong>Job lifecycle</strong>: pending - running - completed/failed</li>
<li><strong>Retry from failure</strong>: restart a failed job from the exact step that failed</li>
<li><strong>History</strong>: stores the last 50 completed/failed jobs</li>
<li><strong>Statistics</strong>: real-time counts of pending, running, completed, failed jobs</li>
<li><strong>Global worker thread</strong>: processes jobs sequentially in the background</li>
</ul>

<h3>4. Service Layer (services/)</h3>

<p>Four service classes encapsulate file I/O and subprocess execution:</p>
<ul>
<li><strong>script_service.py</strong>: load, save, generate, and validate script JSON files</li>
<li><strong>image_service.py</strong>: manage generated images/videos, scene-level deletion, image retrieval with scene mapping</li>
<li><strong>audio_service.py</strong>: audio path resolution, existence checks, audio segmentation, generation orchestration</li>
<li><strong>video_service.py</strong>: movement generation, subtitle alignment, text overlay, music integration, YouTube upload, TikTok cutting</li>
</ul>

<p>All services follow a consistent pattern with organized paths:</p>
</div>

<pre><code>output/{type}/{video}/{category}/{entity_name}/{mode}/{language_code}/</code></pre>

<div class="lang-fr">
<h3>5. Composants UI (ui/)</h3>

<p>Composants Streamlit modulaires separes pour la maintenabilite :</p>
<ul>
<li><strong>generation_tab.py</strong> : flux de travail progressif en 9 sections (script - images - audio - mouvement - sous-titres - overlay texte - musique - TikTok - YouTube)</li>
<li><strong>queue_tab.py</strong> : surveillance de file d'attente, gestion des taches, reessai, navigation historique, upload YouTube rapide</li>
<li><strong>components.py</strong> : utilitaires reutilisables (arret de processus, preferences, controle WebUI)</li>
<li><strong>styles.py</strong> : CSS personnalise pour indicateurs de statut, boutons, lecteurs video, cartes de metriques</li>
</ul>

<h3>6. Modules d'infrastructure</h3>

<p><strong>Gestionnaire de cache (cache_manager.py)</strong> :</p>
<ul>
<li>Generation de cles de cache basee sur MD5 par categorie (scripts, images, audio)</li>
<li>Index de cache stocke dans <code>cache/cache_index.json</code></li>
<li>Nettoyage du cache obsolete avec age configurable</li>
<li>Prevention de la regeneration inutile des ressources existantes</li>
</ul>

<p><strong>Logger (logger.py)</strong> :</p>
<ul>
<li>Handlers de fichiers rotatifs (10 Mo max, 5 sauvegardes)</li>
<li>Fichiers de logs specifiques aux taches (<code>logs/job_{id}.log</code>)</li>
<li>Loggers dedies pour le pipeline, la file d'attente et l'application</li>
<li>Journalisation structuree du cycle de vie des etapes (debut, fin, echec)</li>
</ul>

<p><strong>Notifications (notifications.py)</strong> :</p>
<ul>
<li>Integration webhook Discord avec embeds enrichis</li>
<li>Messages de statut codes par couleur (vert=succes, rouge=erreur, orange=avertissement, bleu=info)</li>
<li>Notifications du cycle de vie des taches (demarrage, progression des etapes, fin, echec)</li>
</ul>

<h3>7. Organisation des scripts (scripts/)</h3>

<p>Tous les scripts de traitement sont organises par domaine :</p>
</div>

<div class="lang-en">
<h3>5. UI Components (ui/)</h3>

<p>Modular Streamlit components split for maintainability:</p>
<ul>
<li><strong>generation_tab.py</strong>: 9-section progressive workflow (script - images - audio - movement - subtitles - text overlay - music - TikTok - YouTube)</li>
<li><strong>queue_tab.py</strong>: queue monitoring, job management, retry, history browsing, quick YouTube upload</li>
<li><strong>components.py</strong>: reusable utilities (process killing, preferences, WebUI control)</li>
<li><strong>styles.py</strong>: custom CSS for status indicators, buttons, video players, metric cards</li>
</ul>

<h3>6. Infrastructure Modules</h3>

<p><strong>Cache Manager (cache_manager.py)</strong>:</p>
<ul>
<li>MD5-based cache key generation per category (scripts, images, audio)</li>
<li>Cache index stored in <code>cache/cache_index.json</code></li>
<li>Stale cache cleanup with configurable age</li>
<li>Prevents unnecessary regeneration of existing assets</li>
</ul>

<p><strong>Logger (logger.py)</strong>:</p>
<ul>
<li>Rotating file handlers (10 MB max, 5 backups)</li>
<li>Job-specific log files (<code>logs/job_{id}.log</code>)</li>
<li>Dedicated loggers for pipeline, queue, and application</li>
<li>Structured step lifecycle logging (start, complete, fail)</li>
</ul>

<p><strong>Notifications (notifications.py)</strong>:</p>
<ul>
<li>Discord webhook integration with rich embeds</li>
<li>Color-coded status messages (green=success, red=error, orange=warning, blue=info)</li>
<li>Job lifecycle notifications (started, step progress, completed, failed)</li>
</ul>

<h3>7. Scripts Organization (scripts/)</h3>

<p>All processing scripts are organized by domain:</p>
</div>

<pre><code>scripts/
├── script/           # LLM-based script generation &amp; verification
├── images/           # Image generation, validation &amp; thumbnails
├── audio/            # TTS synthesis &amp; audio processing
├── video/            # Video editing, animation &amp; subtitles
├── music/            # Background music generation
├── batch/            # Batch operations
├── publishing/       # Publishing &amp; promotion
└── experimental/     # Experimental features
</code></pre>

<div class="lang-fr">
<h2>Organisation des fichiers</h2>
</div>

<div class="lang-en">
<h2>File Organization</h2>
</div>

<pre><code>.
├── app2.py                    # Streamlit web application
├── pipeline_executor.py       # 6-step pipeline engine
├── queue_manager.py           # Job queue management
├── run_pipeline.py            # Subprocess launcher
├── utils.py                   # Configuration &amp; environment utilities
├── cache_manager.py           # Intelligent caching system
├── logger.py                  # Structured logging
├── notifications.py           # Discord webhook notifications
├── config.xml                 # Application configuration
├── services/
│   ├── script_service.py
│   ├── image_service.py
│   ├── audio_service.py
│   └── video_service.py
├── ui/
│   ├── generation_tab.py
│   ├── queue_tab.py
│   ├── components.py
│   └── styles.py
├── scripts/                   # Processing scripts
├── input/
│   ├── Audio/                 # Voice reference files (FR/EN/ES)
│   └── Video_List/            # Excel entity lists per category
├── output/                    # Generated content
├── logs/                      # Rotating log files
├── cache/                     # Cache index &amp; metadata
└── stable-diffusion-webui/    # AUTOMATIC1111 WebUI (submodule)
</code></pre>

<div class="lang-fr">
<h2>Flux de travail du pipeline automatise</h2>

<h3>Pipeline complet (mode file d'attente)</h3>

<ol>
<li><strong>L'utilisateur configure</strong> le type de video, la categorie, l'entite, le mode et la langue dans l'interface Streamlit</li>
<li><strong>La tache est ajoutee</strong> a la file d'attente persistante via <code>queue_manager.py</code></li>
<li><strong>Le thread worker</strong> prend la tache et lance <code>run_pipeline.py</code> comme sous-processus</li>
<li><strong>PipelineExecutor</strong> orchestre les 6 etapes :
    <ul>
    <li>Etape 1 : Le LLM genere un script JSON structure (scenes, prompts, titres)</li>
    <li>Etapes 2-3 : <strong>Images et audio s'executent en parallele</strong> - Stable Diffusion ou Pexels pour les images, XTTS v2 pour le clonage vocal</li>
    <li>Etape 4 : Animation de mouvement de camera appliquee a chaque scene (zoom, pan, slide)</li>
    <li>Etape 5 : Alignement des sous-titres base sur Whisper (mode court)</li>
    <li>Etape 6 : Generation de musique de fond MusicGen (mode court)</li>
    </ul>
</li>
<li><strong>Notification Discord</strong> envoyee au demarrage, a la fin ou en cas d'echec de la tache</li>
<li><strong>L'utilisateur consulte</strong> le resultat dans l'onglet Historique, peut uploader sur YouTube directement</li>
</ol>

<h3>Mode manuel (onglet Generation)</h3>

<p>Chaque etape peut aussi etre executee individuellement avec apercu en direct :</p>
<ul>
<li>Editer le JSON du script directement dans l'interface</li>
<li>Previsualiser les images generees en grille</li>
<li>Ecouter l'audio par scene avec edition des prompts</li>
<li>Regarder les previsualisations video animees</li>
<li>Editer le JSON des sous-titres avec rendu en direct</li>
<li>Decouper les videos pour TikTok avec selection temporelle</li>
<li>Uploader sur YouTube avec miniature et metadonnees</li>
</ul>

<h2>Configuration (config.xml)</h2>
</div>

<div class="lang-en">
<h2>Automated Pipeline Workflow</h2>

<h3>Full Pipeline (Queue Mode)</h3>

<ol>
<li><strong>User configures</strong> video type, category, entity, mode, language in the Streamlit UI</li>
<li><strong>Job added</strong> to the persistent queue via <code>queue_manager.py</code></li>
<li><strong>Worker thread</strong> picks up the job and spawns <code>run_pipeline.py</code> as a subprocess</li>
<li><strong>PipelineExecutor</strong> orchestrates the 6 steps:
    <ul>
    <li>Step 1: LLM generates a structured JSON script (scenes, prompts, titles)</li>
    <li>Steps 2-3: <strong>Images and audio run in parallel</strong> - Stable Diffusion or Pexels for images, XTTS v2 for voice cloning</li>
    <li>Step 4: Camera movement animation applied to each scene (zoom, pan, slide)</li>
    <li>Step 5: Whisper-based subtitle alignment (short mode)</li>
    <li>Step 6: MusicGen background music generation (short mode)</li>
    </ul>
</li>
<li><strong>Discord notification</strong> sent at job start, completion, or failure</li>
<li><strong>User reviews</strong> the result in the History tab, can upload to YouTube directly</li>
</ol>

<h3>Manual Mode (Generation Tab)</h3>

<p>Each step can also be executed individually with live preview:</p>
<ul>
<li>Edit the script JSON directly in the UI</li>
<li>Preview generated images in a grid view</li>
<li>Listen to audio per scene with prompt editing</li>
<li>Watch animated video previews</li>
<li>Edit subtitle JSON with live rendering</li>
<li>Cut videos for TikTok with time-based selection</li>
<li>Upload to YouTube with thumbnail and metadata</li>
</ul>

<h2>Configuration (config.xml)</h2>
</div>

<pre><code class="language-xml">&lt;!-- Languages with voice reference files --&gt;
&lt;languages&gt;
  &lt;language name="Francais" code="fr" audio="Enregistrement-francais.wav" /&gt;
  &lt;language name="English" code="en" audio="Enregistrement-anglais.wav" /&gt;
  &lt;language name="Espanol" code="es" audio="Enregistrement-espagnol.wav" /&gt;
&lt;/languages&gt;

&lt;!-- Production modes --&gt;
&lt;modes&gt;
  &lt;mode name="short" nb_scenes="5" nb_images="3" width="1024" height="1024" /&gt;
  &lt;mode name="long" nb_scenes="20" nb_images="3" width="1280" height="720" /&gt;
&lt;/modes&gt;

&lt;!-- AI Models --&gt;
&lt;models&gt;
  &lt;model name="juggernaut-xl" type="image" /&gt;
  &lt;model name="xtts_v2" type="audio" /&gt;
  &lt;script_models&gt;gemma, deepseek-r1, ministral&lt;/script_models&gt;
&lt;/models&gt;
</code></pre>

<div class="lang-fr">
<h2>Architecture technique</h2>

<p><strong>Stack backend</strong> :</p>
<ul>
<li><strong>Python 3.9+</strong> : Langage principal</li>
<li><strong>Streamlit</strong> : Framework web avec authentification</li>
<li><strong>XML/YAML/JSON</strong> : Gestion de la configuration</li>
<li><strong>Threading</strong> : Execution parallele et worker de file d'attente</li>
</ul>

<p><strong>Modeles IA</strong> (8 modeles integres) :</p>
<ul>
<li><strong>Stable Diffusion</strong> (AUTOMATIC1111 WebUI) - Generation d'images</li>
<li><strong>Coqui TTS</strong> (XTTS v2) - Clonage vocal multilingue</li>
<li><strong>Ollama</strong> (Gemma, DeepSeek, Ministral) - Generation de scripts via LLM</li>
<li><strong>CLIP</strong> (OpenAI) - Verification de similarite image-texte</li>
<li><strong>Whisper</strong> (OpenAI) - Alignement de sous-titres depuis l'audio</li>
<li><strong>MediaPipe</strong> - Detection de visages dans les images generees</li>
<li><strong>Facebook MusicGen</strong> - Musique de fond generee par IA</li>
<li><strong>MoviePy + OpenCV</strong> - Edition video, animation, effets</li>
</ul>

<p><strong>APIs externes</strong> :</p>
<ul>
<li>API Stable Diffusion (<code>http://127.0.0.1:7860</code>)</li>
<li>API Ollama (<code>http://localhost:11434</code>)</li>
<li>API Pexels (images/videos stock pour geographie/actu)</li>
<li>API YouTube Data v3 (uploads automatises)</li>
<li>Webhooks Discord (notifications)</li>
</ul>

<p><strong>Categories de traitement</strong> :</p>
</div>

<div class="lang-en">
<h2>Technical Architecture</h2>

<p><strong>Backend Stack</strong>:</p>
<ul>
<li><strong>Python 3.9+</strong>: Core language</li>
<li><strong>Streamlit</strong>: Web framework with authentication</li>
<li><strong>XML/YAML/JSON</strong>: Configuration management</li>
<li><strong>Threading</strong>: Parallel execution and queue worker</li>
</ul>

<p><strong>AI Models</strong> (8 models integrated):</p>
<ul>
<li><strong>Stable Diffusion</strong> (AUTOMATIC1111 WebUI) - Image generation</li>
<li><strong>Coqui TTS</strong> (XTTS v2) - Multilingual voice cloning</li>
<li><strong>Ollama</strong> (Gemma, DeepSeek, Ministral) - Script generation via LLM</li>
<li><strong>CLIP</strong> (OpenAI) - Image-text similarity verification</li>
<li><strong>Whisper</strong> (OpenAI) - Subtitle alignment from audio</li>
<li><strong>MediaPipe</strong> - Face detection in generated images</li>
<li><strong>Facebook MusicGen</strong> - AI-generated background music</li>
<li><strong>MoviePy + OpenCV</strong> - Video editing, animation, effects</li>
</ul>

<p><strong>External APIs</strong>:</p>
<ul>
<li>Stable Diffusion API (<code>http://127.0.0.1:7860</code>)</li>
<li>Ollama API (<code>http://localhost:11434</code>)</li>
<li>Pexels API (stock images/videos for geography/actu)</li>
<li>YouTube Data API v3 (automated uploads)</li>
<li>Discord Webhooks (notifications)</li>
</ul>

<p><strong>Processing Categories</strong>:</p>
</div>

<table>
<tr><th>Category</th><th>Image Source</th><th>Script Model</th><th>Description</th></tr>
<tr><td>Celebrity</td><td>Stable Diffusion</td><td>LLM</td><td>Biography and career videos</td></tr>
<tr><td>Geography</td><td>Pexels API</td><td>LLM</td><td>Location and travel documentaries</td></tr>
<tr><td>Actu (News)</td><td>Pexels API</td><td>LLM (actu variant)</td><td>Current events reports</td></tr>
<tr><td>Movie</td><td>Pexels API</td><td>LLM</td><td>Film analysis and summaries</td></tr>
<tr><td>Monument</td><td>Stable Diffusion</td><td>LLM</td><td>Historical and architectural features</td></tr>
<tr><td>Oeuvre (Art)</td><td>Stable Diffusion</td><td>LLM</td><td>Artistic works and analysis</td></tr>
</table>

<div class="lang-fr">
<h2>Defis de developpement et solutions</h2>

<p><strong>Defi 1 : Fiabilite du pipeline</strong></p>
<ul>
<li><strong>Probleme</strong> : Les pipelines de longue duree (5-20 scenes) pouvaient echouer en cours d'execution, gaspillant tout le travail precedent</li>
<li><strong>Solution</strong> : Execution etape par etape avec reessai automatique (2 tentatives par etape), gestion des processus pour arreter les orphelins, et redemarrage des taches de la file d'attente a partir de l'etape exacte d'echec</li>
</ul>

<p><strong>Defi 2 : Synchronisation audio-visuelle</strong></p>
<ul>
<li><strong>Probleme</strong> : S'assurer que la narration audio correspond parfaitement a la duree video sur toutes les scenes</li>
<li><strong>Solution</strong> : Calcul dynamique du timing, alignement des sous-titres base sur Whisper, et ajustement du debit d'images avec MoviePy</li>
</ul>

<p><strong>Defi 3 : Contention des ressources</strong></p>
<ul>
<li><strong>Probleme</strong> : Plusieurs modeles IA (SD, TTS, LLM) en competition pour le GPU et la memoire</li>
<li><strong>Solution</strong> : Execution sequentielle des taches via le worker de file d'attente, etapes image/audio paralleles au sein d'une tache, et arret des processus avant chaque etape pour liberer les ressources</li>
</ul>

<p><strong>Defi 4 : Coherence de qualite</strong></p>
<ul>
<li><strong>Probleme</strong> : Le contenu genere par IA varie en qualite entre les scenes</li>
<li><strong>Solution</strong> : Pipeline de verification multi-etapes (score CLIP pour les images, detection de visages via MediaPipe, validation du script via LLM), avec points d'intervention manuelle dans l'interface</li>
</ul>

<p><strong>Defi 5 : Support multilingue</strong></p>
<ul>
<li><strong>Probleme</strong> : Prendre en charge plusieurs langues pour la narration, les scripts et les sous-titres</li>
<li><strong>Solution</strong> : Fichiers de reference vocale par langue, repertoires de sortie par langue, et prompts LLM adaptes pour chaque langue</li>
</ul>

<p><strong>Defi 6 : Observabilite</strong></p>
<ul>
<li><strong>Probleme</strong> : Deboguer les taches echouees dans un pipeline automatise avec plusieurs modeles IA</li>
<li><strong>Solution</strong> : Journalisation structuree avec fichiers rotatifs, fichiers de logs specifiques aux taches, suivi du cycle de vie des etapes, et notifications Discord avec details d'erreur</li>
</ul>

<h2>Prerequis</h2>
<ul>
<li>Python 3.9+</li>
<li>ffmpeg installe sur le systeme</li>
<li>GPU recommande (NVIDIA pour le support CUDA)</li>
</ul>

<p><strong>Packages Python</strong> :</p>
</div>

<div class="lang-en">
<h2>Development Challenges and Solutions</h2>

<p><strong>Challenge 1: Pipeline Reliability</strong></p>
<ul>
<li><strong>Problem</strong>: Long-running pipelines (5-20 scenes) could fail mid-execution, wasting all prior work</li>
<li><strong>Solution</strong>: Step-by-step execution with automatic retry (2 attempts per step), process management to kill orphans, and queue-based job restart from the exact failed step</li>
</ul>

<p><strong>Challenge 2: Audio-Visual Synchronization</strong></p>
<ul>
<li><strong>Problem</strong>: Ensuring audio narration perfectly matches video duration across scenes</li>
<li><strong>Solution</strong>: Dynamic timing calculation, Whisper-based subtitle alignment, and frame rate adjustment with MoviePy</li>
</ul>

<p><strong>Challenge 3: Resource Contention</strong></p>
<ul>
<li><strong>Problem</strong>: Multiple AI models (SD, TTS, LLM) competing for GPU and memory</li>
<li><strong>Solution</strong>: Sequential job execution via queue worker, parallel image/audio steps within a job, and process killing before each step to release resources</li>
</ul>

<p><strong>Challenge 4: Quality Consistency</strong></p>
<ul>
<li><strong>Problem</strong>: AI-generated content varies in quality across scenes</li>
<li><strong>Solution</strong>: Multi-stage verification pipeline (CLIP score for images, face detection via MediaPipe, script validation via LLM), with manual intervention points in the UI</li>
</ul>

<p><strong>Challenge 5: Multi-language Support</strong></p>
<ul>
<li><strong>Problem</strong>: Supporting multiple languages for narration, scripts, and subtitles</li>
<li><strong>Solution</strong>: Language-specific voice reference files, per-language output directories, and LLM prompts adapted for each language</li>
</ul>

<p><strong>Challenge 6: Observability</strong></p>
<ul>
<li><strong>Problem</strong>: Debugging failed jobs in an automated pipeline with multiple AI models</li>
<li><strong>Solution</strong>: Structured logging with rotating files, job-specific log files, step lifecycle tracking, and Discord notifications with error details</li>
</ul>

<h2>Prerequisites</h2>
<ul>
<li>Python 3.9+</li>
<li>ffmpeg installed on the system</li>
<li>GPU recommended (NVIDIA for CUDA support)</li>
</ul>

<p><strong>Python packages</strong>:</p>
</div>

<pre><code class="language-sh">pip install streamlit streamlit-authenticator
pip install moviepy requests TTS openai-whisper
pip install transformers mediapipe ollama
pip install pydub soundfile openpyxl pyyaml
pip install -r stable-diffusion-webui/requirements.txt
</code></pre>

<div class="lang-fr">
<p><strong>Services a executer</strong> :</p>
</div>

<div class="lang-en">
<p><strong>Services to run</strong>:</p>
</div>

<pre><code class="language-sh"># Stable Diffusion WebUI (image generation)
cd stable-diffusion-webui &amp;&amp; ./webui.sh --api

# Ollama (LLM for script generation)
ollama serve
ollama pull gemma3:12b

# Streamlit application
streamlit run app2.py
</code></pre>

<div class="lang-fr">
<h2>Depannage</h2>
<ul>
<li><strong>Erreur API Stable Diffusion</strong> : verifier que le WebUI est en cours d'execution sur le port 7860 avec le flag <code>--api</code></li>
<li><strong>Connexion Ollama refusee</strong> : s'assurer que <code>ollama serve</code> est en cours d'execution sur le port 11434</li>
<li><strong>Audio non genere</strong> : verifier le chemin du fichier WAV de reference vocale dans <code>config.xml</code></li>
<li><strong>File d'attente bloquee</strong> : verifier <code>logs/queue.log</code> et <code>logs/job_{id}.log</code> pour les details d'erreur</li>
<li><strong>Notifications Discord non envoyees</strong> : verifier l'URL du webhook dans <code>.env</code></li>
<li><strong>Decalage image/audio</strong> : s'assurer que les numeros de scenes correspondent dans le JSON du script</li>
<li><strong>Conflits de processus</strong> : utiliser le bouton "kill process" dans l'interface ou verifier les processus Python orphelins</li>
</ul>

<h2>Cas d'utilisation et applications</h2>
<ul>
<li><strong>Contenu educatif</strong> : Videos explicatives sur n'importe quel sujet avec narration IA</li>
<li><strong>Reseaux sociaux</strong> : Contenu format court pret pour TikTok avec decoupage automatique</li>
<li><strong>Actualites</strong> : Reportages automatises avec images stock Pexels</li>
<li><strong>Documentaire</strong> : Documentaires geographiques et monumentaux avec images</li>
<li><strong>Divertissement</strong> : Biographies de celebrites, analyses de films, presentations d'oeuvres d'art</li>
<li><strong>Marketing</strong> : Presentations de produits avec voix et musique personnalisees</li>
</ul>

<h2>Ameliorations futures</h2>
<ul>
<li>Apercu et streaming de generation video en temps reel</li>
<li>Effets d'animation avances (transitions 3D, particules)</li>
<li>Transfert de style video et filtres artistiques</li>
<li>Integration avec d'autres modeles TTS (ElevenLabs, Bark)</li>
<li>Deploiement cloud pour scalabilite horizontale</li>
<li>Tests A/B pour l'optimisation des miniatures et titres</li>
<li>Tableau de bord analytique pour les performances du contenu genere</li>
</ul>

<h2>Metriques de performance</h2>
<ul>
<li><strong>Generation de script</strong> : ~10-30 secondes (selon le LLM)</li>
<li><strong>Generation d'images</strong> : ~5-10 secondes par scene (selon le GPU)</li>
<li><strong>Synthese audio</strong> : ~3-5 secondes par scene</li>
<li><strong>Animation video</strong> : ~2-4 secondes par scene</li>
<li><strong>Alignement sous-titres</strong> : ~5-10 secondes au total</li>
<li><strong>Generation musique</strong> : ~15-30 secondes</li>
<li><strong>Pipeline total (court, 5 scenes)</strong> : ~3-5 minutes</li>
<li><strong>Pipeline total (long, 20 scenes)</strong> : ~15-25 minutes</li>
</ul>

<hr/>

<h2>Modeles IA detailles</h2>

<h3>1. Stable Diffusion (AUTOMATIC1111 WebUI)</h3>
<p><strong>Modele</strong> : Juggernaut-XL avec LoRA de detail de visage. Utilise pour la generation d'images a partir de prompts textuels (scenes, miniatures). Prerequis : WebUI en cours d'execution avec le flag <code>--api</code>, modeles <code>.safetensors</code> dans <code>models/Stable-diffusion/</code>.</p>

<h3>2. Coqui TTS (XTTS v2)</h3>
<p><strong>Modele</strong> : <code>tts_models/multilingual/multi-dataset/xtts_v2</code>. Clonage vocal multilingue a partir d'un fichier WAV de reference. Prerequis : <code>pip install TTS</code>, fichier WAV de reference par langue.</p>

<h3>3. Ollama (Gemma, DeepSeek, Ministral)</h3>
<p><strong>Modeles</strong> : <code>gemma3:12b</code>, <code>deepseek-r1:latest</code>, <code>ministral-3:14b</code>. Generation de scripts basee sur LLM, verification, traduction. Sortie JSON structuree avec scenes, titres et prompts.</p>

<h3>4. CLIP (OpenAI)</h3>
<p><strong>Modele</strong> : <code>openai/clip-vit-base-patch32</code>. Scoring de similarite image-texte pour la verification de qualite. Filtrage automatique des images a faible pertinence.</p>

<h3>5. Whisper (OpenAI)</h3>
<p><strong>Modele</strong> : Whisper base. Alignement automatique des sous-titres a partir de la transcription audio. Timing au niveau des mots et export JSON des sous-titres.</p>

<h3>6. MediaPipe (Detection de visages)</h3>
<p>Detection de visages dans les images generees pour le filtrage qualite. Rejet automatique des images sans visages attendus.</p>

<h3>7. Facebook MusicGen</h3>
<p><strong>Modele</strong> : <code>facebook/musicgen-medium</code>. Musique de fond generee par IA a partir de prompts textuels. Correspondance automatique de la duree et integration directe dans le pipeline.</p>

<h3>8. MoviePy + OpenCV</h3>
<p>Edition video, animation de camera (zoom, pan, slide), synchronisation audio, overlay de sous-titres. Recadrage TikTok/YouTube, rendu de sous-titres, concatenation video, mixage musical.</p>

<hr/>

<h2>Ressources et credits</h2>
<ul>
<li><a href="https://github.com/AUTOMATIC1111/stable-diffusion-webui">Stable Diffusion WebUI</a></li>
<li><a href="https://github.com/coqui-ai/TTS">Coqui TTS</a></li>
<li><a href="https://ollama.ai/">Ollama</a></li>
<li><a href="https://zulko.github.io/moviepy/">MoviePy</a></li>
<li><a href="https://github.com/openai/whisper">OpenAI Whisper</a></li>
<li><a href="https://huggingface.co/facebook/musicgen-medium">Facebook MusicGen</a></li>
<li><a href="https://www.pexels.com/api/">Pexels API</a></li>
<li><strong>Developpeur</strong> : Cedric Chanfreau</li>
<li><strong>Application Web</strong> : <a href="https://video-automation.littlenuage.com/">video-automation.littlenuage.com</a></li>
</ul>

<hr/>

<h2>Essayez vous-meme !</h2>

<p><strong>Acceder a l'application</strong> : <a href="https://video-automation.littlenuage.com/">https://video-automation.littlenuage.com/</a></p>

<ol>
<li>Selectionnez votre type de video et categorie</li>
<li>Choisissez une entite dans la liste (ou ajoutez la votre)</li>
<li>Choisissez une langue et un mode de production (court/long)</li>
<li>Ajoutez la tache a la file d'attente ou generez etape par etape</li>
<li>Suivez la progression via les notifications Discord</li>
<li>Telechargez ou uploadez directement sur YouTube</li>
</ol>
</div>

<div class="lang-en">
<h2>Troubleshooting</h2>
<ul>
<li><strong>Stable Diffusion API error</strong>: check that the WebUI is running on port 7860 with <code>--api</code> flag</li>
<li><strong>Ollama connection refused</strong>: ensure <code>ollama serve</code> is running on port 11434</li>
<li><strong>Audio not generated</strong>: verify the voice reference WAV file path in <code>config.xml</code></li>
<li><strong>Queue stuck</strong>: check <code>logs/queue.log</code> and <code>logs/job_{id}.log</code> for error details</li>
<li><strong>Discord notifications not sent</strong>: verify the webhook URL in <code>.env</code></li>
<li><strong>Image/audio mismatch</strong>: ensure scene numbers match in the script JSON</li>
<li><strong>Process conflicts</strong>: use the "kill process" button in the UI or check for orphan Python processes</li>
</ul>

<h2>Use Cases and Applications</h2>
<ul>
<li><strong>Educational Content</strong>: Explainer videos on any topic with AI narration</li>
<li><strong>Social Media</strong>: TikTok-ready short-form content with automatic cutting</li>
<li><strong>News</strong>: Automated news reports with Pexels stock footage</li>
<li><strong>Documentary</strong>: Geography and monument documentaries with images</li>
<li><strong>Entertainment</strong>: Celebrity biographies, movie analyses, art features</li>
<li><strong>Marketing</strong>: Product presentations with custom voice and music</li>
</ul>

<h2>Future Enhancements</h2>
<ul>
<li>Real-time video generation preview and streaming</li>
<li>Advanced animation effects (3D transitions, particles)</li>
<li>Video style transfer and artistic filters</li>
<li>Integration with more TTS models (ElevenLabs, Bark)</li>
<li>Cloud deployment for horizontal scalability</li>
<li>A/B testing for thumbnail and title optimization</li>
<li>Analytics dashboard for generated content performance</li>
</ul>

<h2>Performance Metrics</h2>
<ul>
<li><strong>Script Generation</strong>: ~10-30 seconds (LLM-dependent)</li>
<li><strong>Image Generation</strong>: ~5-10 seconds per scene (GPU-dependent)</li>
<li><strong>Audio Synthesis</strong>: ~3-5 seconds per scene</li>
<li><strong>Video Animation</strong>: ~2-4 seconds per scene</li>
<li><strong>Subtitle Alignment</strong>: ~5-10 seconds total</li>
<li><strong>Music Generation</strong>: ~15-30 seconds</li>
<li><strong>Total Pipeline (short, 5 scenes)</strong>: ~3-5 minutes</li>
<li><strong>Total Pipeline (long, 20 scenes)</strong>: ~15-25 minutes</li>
</ul>

<hr/>

<h2>Detailed AI Models</h2>

<h3>1. Stable Diffusion (AUTOMATIC1111 WebUI)</h3>
<p><strong>Model</strong>: Juggernaut-XL with face detail LoRA. Used for image generation from text prompts (scenes, thumbnails). Prerequisites: WebUI running with <code>--api</code> flag, <code>.safetensors</code> models in <code>models/Stable-diffusion/</code>.</p>

<h3>2. Coqui TTS (XTTS v2)</h3>
<p><strong>Model</strong>: <code>tts_models/multilingual/multi-dataset/xtts_v2</code>. Multilingual voice cloning from a WAV reference file. Prerequisites: <code>pip install TTS</code>, WAV reference file per language.</p>

<h3>3. Ollama (Gemma, DeepSeek, Ministral)</h3>
<p><strong>Models</strong>: <code>gemma3:12b</code>, <code>deepseek-r1:latest</code>, <code>ministral-3:14b</code>. LLM-based script generation, verification, translation. Structured JSON output with scenes, titles, and prompts.</p>

<h3>4. CLIP (OpenAI)</h3>
<p><strong>Model</strong>: <code>openai/clip-vit-base-patch32</code>. Image-text similarity scoring for quality verification. Automatic filtering of low-relevance images.</p>

<h3>5. Whisper (OpenAI)</h3>
<p><strong>Model</strong>: Whisper base. Automatic subtitle alignment from audio transcription. Word-level timing and subtitle JSON export.</p>

<h3>6. MediaPipe (Face Detection)</h3>
<p>Face detection in generated images for quality filtering. Automatic rejection of images without expected faces.</p>

<h3>7. Facebook MusicGen</h3>
<p><strong>Model</strong>: <code>facebook/musicgen-medium</code>. AI-generated background music from text prompts. Automatic duration matching and direct pipeline integration.</p>

<h3>8. MoviePy + OpenCV</h3>
<p>Video editing, camera animation (zoom, pan, slide), audio synchronization, subtitle overlay. TikTok/YouTube crop, subtitle rendering, video concatenation, music mixing.</p>

<hr/>

<h2>Resources and Credits</h2>
<ul>
<li><a href="https://github.com/AUTOMATIC1111/stable-diffusion-webui">Stable Diffusion WebUI</a></li>
<li><a href="https://github.com/coqui-ai/TTS">Coqui TTS</a></li>
<li><a href="https://ollama.ai/">Ollama</a></li>
<li><a href="https://zulko.github.io/moviepy/">MoviePy</a></li>
<li><a href="https://github.com/openai/whisper">OpenAI Whisper</a></li>
<li><a href="https://huggingface.co/facebook/musicgen-medium">Facebook MusicGen</a></li>
<li><a href="https://www.pexels.com/api/">Pexels API</a></li>
<li><strong>Developer</strong>: Cedric Chanfreau</li>
<li><strong>Web Application</strong>: <a href="https://video-automation.littlenuage.com/">video-automation.littlenuage.com</a></li>
</ul>

<hr/>

<h2>Try It Yourself!</h2>

<p><strong>Access the application</strong>: <a href="https://video-automation.littlenuage.com/">https://video-automation.littlenuage.com/</a></p>

<ol>
<li>Select your video type and category</li>
<li>Choose an entity from the list (or add your own)</li>
<li>Pick a language and production mode (short/long)</li>
<li>Add the job to the queue or generate step-by-step</li>
<li>Monitor progress via Discord notifications</li>
<li>Download or upload directly to YouTube</li>
</ol>
</div>

<img src="/img/automation-video/workflow.png" alt="IA Automation Workflow" style="width: 100%;" />

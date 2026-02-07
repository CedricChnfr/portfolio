---
layout: default
title:  "IA Automation"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

[← Back to Personal Project](./my-perso-projects.html)

# IA Automation Project Overview

**[Try the application here: https://video-automation.littlenuage.com/](https://video-automation.littlenuage.com/)**

This project is a fully automated video production platform powered by AI. From a simple text topic, the system generates a structured script, creates images, synthesizes narration, applies camera animations, adds subtitles and background music, and delivers a ready-to-publish video — all orchestrated through a Streamlit web interface with job queue management and Discord notifications.

## Project Context

Developed as a personal project to industrialize video content creation, this platform eliminates the need for manual editing. It supports multiple video categories (celebrity biographies, geography documentaries, news reports, movie analyses, monuments, artworks), multiple languages (French, English, Spanish), and two production modes (short-form and long-form). The application is deployed online and accessible to anyone.

## Architecture Overview

The system follows a modular, service-oriented architecture with clear separation of concerns:

```
User (Streamlit UI)
    │
    ▼
app2.py ──► queue_manager.py ──► run_pipeline.py ──► pipeline_executor.py
                                                          │
                                    ┌─────────────────────┼─────────────────────┐
                                    ▼                     ▼                     ▼
                              services/             scripts/              AI Models
                          (script, image,       (generation &          (SD, TTS, LLM,
                          audio, video)          processing)           CLIP, Whisper...)
```

## What I Developed

### 1. Streamlit Web Application (`app2.py`)

The main user interface built with Streamlit, replacing the earlier Flask prototype:

- **Authenticated access** via `streamlit_authenticator` with YAML-based credentials
- **Video configuration**: type selection (celebrity, geography, actu, movie, oeuvre, monument), category, entity, mode (short/long), language (FR/EN/ES)
- **Three-tab interface**: Generation (step-by-step workflow), Queue (job management), History (past productions)
- **WebUI control**: monitor and launch the Stable Diffusion WebUI server directly from the interface
- **User preferences**: persistent settings saved between sessions (`user_preferences.json`)
- **Excel integration**: entity lists loaded from category-specific Excel files

### 2. Pipeline Execution Engine (`pipeline_executor.py`)

The core orchestrator implementing a robust 6-step pipeline:

| Step | Description | Script |
|------|------------|--------|
| 1 | **Script Generation** | `generate_script.py` / `generate_script_actu.py` |
| 2 | **Image Generation** | `generate_image.py` / `get_image_pexels.py` |
| 3 | **Audio Synthesis** | `generate_audio.py` |
| 4 | **Camera Movement & Animation** | `generate_movement.py` / `generate_movement_from_db.py` |
| 5 | **Subtitle Alignment** | `align_subtitles.py` (short mode) |
| 6 | **Music Generation** | `generate_music.py` (short mode) |

Key features:
- **Parallel execution**: steps 2 (images) and 3 (audio) run concurrently
- **Automatic retry**: up to 2 retries per step on failure
- **Process management**: kills orphan processes before each step to prevent resource conflicts
- **Execution tracking**: full timing metrics per step and total pipeline duration

### 3. Job Queue System (`queue_manager.py`)

A thread-safe job queue for sequential video production:

- **Persistent state** stored in `generation_queue.json`
- **Job lifecycle**: pending → running → completed/failed
- **Retry from failure**: restart a failed job from the exact step that failed
- **History**: stores the last 50 completed/failed jobs
- **Statistics**: real-time counts of pending, running, completed, failed jobs
- **Global worker thread**: processes jobs sequentially in the background

### 4. Service Layer (`services/`)

Four service classes encapsulate file I/O and subprocess execution:

- **`script_service.py`**: load, save, generate, and validate script JSON files
- **`image_service.py`**: manage generated images/videos, scene-level deletion, image retrieval with scene mapping
- **`audio_service.py`**: audio path resolution, existence checks, audio segmentation, generation orchestration
- **`video_service.py`**: movement generation, subtitle alignment, text overlay, music integration, YouTube upload, TikTok cutting

All services follow a consistent pattern with organized paths:
```
output/{type}/{video}/{category}/{entity_name}/{mode}/{language_code}/
```

### 5. UI Components (`ui/`)

Modular Streamlit components split for maintainability:

- **`generation_tab.py`**: 9-section progressive workflow (script → images → audio → movement → subtitles → text overlay → music → TikTok → YouTube)
- **`queue_tab.py`**: queue monitoring, job management, retry, history browsing, quick YouTube upload
- **`components.py`**: reusable utilities (process killing, preferences, WebUI control)
- **`styles.py`**: custom CSS for status indicators, buttons, video players, metric cards

### 6. Infrastructure Modules

**Cache Manager (`cache_manager.py`)**:
- MD5-based cache key generation per category (scripts, images, audio)
- Cache index stored in `cache/cache_index.json`
- Stale cache cleanup with configurable age
- Prevents unnecessary regeneration of existing assets

**Logger (`logger.py`)**:
- Rotating file handlers (10 MB max, 5 backups)
- Job-specific log files (`logs/job_{id}.log`)
- Dedicated loggers for pipeline, queue, and application
- Structured step lifecycle logging (start, complete, fail)

**Notifications (`notifications.py`)**:
- Discord webhook integration with rich embeds
- Color-coded status messages (green=success, red=error, orange=warning, blue=info)
- Job lifecycle notifications (started, step progress, completed, failed)

### 7. Scripts Organization (`scripts/`)

All processing scripts are organized by domain:

```
scripts/
├── script/           # LLM-based script generation & verification
│   ├── generate_script.py
│   ├── generate_script_actu.py
│   ├── verify_script.py
│   └── verify_script_actu.py
├── images/           # Image generation, validation & thumbnails
│   ├── generate_image.py          # Stable Diffusion (celebrity mode)
│   ├── get_image_pexels.py        # Pexels API (geography/actu/movie)
│   ├── generate_mignature.py      # Thumbnail generation
│   ├── verify_image.py            # CLIP score + face detection
│   ├── validate_sequential_images.py
│   ├── configure_images.py
│   └── add_image_details.py
├── audio/            # TTS synthesis & audio processing
│   ├── generate_audio.py          # XTTS v2 voice cloning
│   ├── cut_audio.py
│   ├── verify_audio.py
│   └── correct_text_aft_verif.py
├── video/            # Video editing, animation & subtitles
│   ├── generate_movement.py       # Celebrity image animation
│   ├── generate_movement_from_db.py  # DB-based animation (geography/actu)
│   ├── align_subtitles.py         # Whisper-based subtitle timing
│   ├── generate_text_on_video.py
│   ├── cut_txt_video.py           # TikTok video cutting
│   ├── generate_video_image.py
│   └── cut.py
├── music/            # Background music generation
│   └── generate_music.py          # Facebook MusicGen
├── batch/            # Batch operations
│   ├── generate_all_audio.py
│   ├── generate_all_image.py
│   └── checklist_final.py
├── publishing/       # Publishing & promotion
│   ├── send_to_youtube.py
│   └── short_end_pub.py
└── experimental/     # Experimental features
    └── (image-to-video, deforum)
```

## File Organization

```
.
├── app2.py                    # Streamlit web application
├── pipeline_executor.py       # 6-step pipeline engine
├── queue_manager.py           # Job queue management
├── run_pipeline.py            # Subprocess launcher
├── utils.py                   # Configuration & environment utilities
├── cache_manager.py           # Intelligent caching system
├── logger.py                  # Structured logging
├── notifications.py           # Discord webhook notifications
├── config.xml                 # Application configuration (languages, modes, models, paths)
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
├── scripts/                   # Processing scripts (see above)
├── authentification/          # OAuth2 & credentials
├── input/
│   ├── Audio/                 # Voice reference files (FR/EN/ES)
│   └── Video_List/            # Excel entity lists per category
├── output/
│   ├── Script/                # Generated JSON scripts
│   ├── Image/                 # Generated scene images
│   ├── Audio/                 # Synthesized narration audio
│   ├── Video/                 # Text-overlay videos
│   ├── Video_Anime/           # Animated scene videos
│   ├── Final-Video/           # Final assembled videos + TikTok cuts
│   ├── Music/                 # Generated background music
│   └── Miniature/             # Video thumbnails
├── logs/                      # Rotating log files
├── cache/                     # Cache index & metadata
└── stable-diffusion-webui/    # AUTOMATIC1111 WebUI (submodule)
```

## Automated Pipeline Workflow

### Full Pipeline (Queue Mode)

1. **User configures** video type, category, entity, mode, language in the Streamlit UI
2. **Job added** to the persistent queue via `queue_manager.py`
3. **Worker thread** picks up the job and spawns `run_pipeline.py` as a subprocess
4. **PipelineExecutor** orchestrates the 6 steps:
   - Step 1: LLM generates a structured JSON script (scenes, prompts, titles)
   - Steps 2-3: **Images and audio run in parallel** — Stable Diffusion or Pexels for images, XTTS v2 for voice cloning
   - Step 4: Camera movement animation applied to each scene (zoom, pan, slide)
   - Step 5: Whisper-based subtitle alignment (short mode)
   - Step 6: MusicGen background music generation (short mode)
5. **Discord notification** sent at job start, completion, or failure
6. **User reviews** the result in the History tab, can upload to YouTube directly

### Manual Mode (Generation Tab)

Each step can also be executed individually with live preview:
- Edit the script JSON directly in the UI
- Preview generated images in a grid view
- Listen to audio per scene with prompt editing
- Watch animated video previews
- Edit subtitle JSON with live rendering
- Cut videos for TikTok with time-based selection
- Upload to YouTube with thumbnail and metadata

## Configuration (`config.xml`)

```xml
<!-- Languages with voice reference files -->
<languages>
  <language name="Francais" code="fr" audio="Enregistrement-francais.wav" />
  <language name="English" code="en" audio="Enregistrement-anglais.wav" />
  <language name="Espanol" code="es" audio="Enregistrement-espagnol.wav" />
</languages>

<!-- Production modes -->
<modes>
  <mode name="short" nb_scenes="5" nb_images="3" width="1024" height="1024" />
  <mode name="long" nb_scenes="20" nb_images="3" width="1280" height="720" />
</modes>

<!-- AI Models -->
<models>
  <model name="juggernaut-xl" type="image" />
  <model name="xtts_v2" type="audio" />
  <script_models>gemma, deepseek-r1, ministral</script_models>
</models>
```

## Technical Architecture

**Backend Stack**:
- **Python 3.9+**: Core language
- **Streamlit**: Web framework with authentication
- **XML/YAML/JSON**: Configuration management
- **Threading**: Parallel execution and queue worker

**AI Models** (8 models integrated):
- **Stable Diffusion** (AUTOMATIC1111 WebUI) — Image generation
- **Coqui TTS** (XTTS v2) — Multilingual voice cloning
- **Ollama** (Gemma, DeepSeek, Ministral) — Script generation via LLM
- **CLIP** (OpenAI) — Image-text similarity verification
- **Whisper** (OpenAI) — Subtitle alignment from audio
- **MediaPipe** — Face detection in generated images
- **Facebook MusicGen** — AI-generated background music
- **MoviePy + OpenCV** — Video editing, animation, effects

**External APIs**:
- Stable Diffusion API (`http://127.0.0.1:7860`)
- Ollama API (`http://localhost:11434`)
- Pexels API (stock images/videos for geography/actu)
- YouTube Data API v3 (automated uploads)
- Discord Webhooks (notifications)

**Processing Categories**:

| Category | Image Source | Script Model | Description |
|----------|-------------|-------------|-------------|
| Celebrity | Stable Diffusion | LLM | Biography and career videos |
| Geography | Pexels API | LLM | Location and travel documentaries |
| Actu (News) | Pexels API | LLM (actu variant) | Current events reports |
| Movie | Pexels API | LLM | Film analysis and summaries |
| Monument | Stable Diffusion | LLM | Historical and architectural features |
| Oeuvre (Art) | Stable Diffusion | LLM | Artistic works and analysis |

## Development Challenges & Solutions

**Challenge 1: Pipeline Reliability**
- **Problem**: Long-running pipelines (5-20 scenes) could fail mid-execution, wasting all prior work
- **Solution**: Step-by-step execution with automatic retry (2 attempts per step), process management to kill orphans, and queue-based job restart from the exact failed step

**Challenge 2: Audio-Visual Synchronization**
- **Problem**: Ensuring audio narration perfectly matches video duration across scenes
- **Solution**: Dynamic timing calculation, Whisper-based subtitle alignment, and frame rate adjustment with MoviePy

**Challenge 3: Resource Contention**
- **Problem**: Multiple AI models (SD, TTS, LLM) competing for GPU and memory
- **Solution**: Sequential job execution via queue worker, parallel image/audio steps within a job, and process killing before each step to release resources

**Challenge 4: Quality Consistency**
- **Problem**: AI-generated content varies in quality across scenes
- **Solution**: Multi-stage verification pipeline (CLIP score for images, face detection via MediaPipe, script validation via LLM), with manual intervention points in the UI

**Challenge 5: Multi-language Support**
- **Problem**: Supporting multiple languages for narration, scripts, and subtitles
- **Solution**: Language-specific voice reference files, per-language output directories, and LLM prompts adapted for each language

**Challenge 6: Observability**
- **Problem**: Debugging failed jobs in an automated pipeline with multiple AI models
- **Solution**: Structured logging with rotating files, job-specific log files, step lifecycle tracking, and Discord notifications with error details

## Prerequisites

- Python 3.9+
- ffmpeg installed on the system
- GPU recommended (NVIDIA for CUDA support)

**Python packages**:
```sh
pip install streamlit streamlit-authenticator
pip install moviepy requests TTS openai-whisper
pip install transformers mediapipe ollama
pip install pydub soundfile openpyxl pyyaml
pip install -r stable-diffusion-webui/requirements.txt
```

**Services to run**:
```sh
# Stable Diffusion WebUI (image generation)
cd stable-diffusion-webui && ./webui.sh --api

# Ollama (LLM for script generation)
ollama serve
ollama pull gemma3:12b

# Streamlit application
streamlit run app2.py
```

## Troubleshooting

- **Stable Diffusion API error**: check that the WebUI is running on port 7860 with `--api` flag
- **Ollama connection refused**: ensure `ollama serve` is running on port 11434
- **Audio not generated**: verify the voice reference WAV file path in `config.xml`
- **Queue stuck**: check `logs/queue.log` and `logs/job_{id}.log` for error details
- **Discord notifications not sent**: verify the webhook URL in `.env`
- **Image/audio mismatch**: ensure scene numbers match in the script JSON
- **Process conflicts**: use the "kill process" button in the UI or check for orphan Python processes

## Use Cases & Applications

- **Educational Content**: Explainer videos on any topic with AI narration
- **Social Media**: TikTok-ready short-form content with automatic cutting
- **News**: Automated news reports with Pexels stock footage
- **Documentary**: Geography and monument documentaries with images
- **Entertainment**: Celebrity biographies, movie analyses, art features
- **Marketing**: Product presentations with custom voice and music

## Future Enhancements

- Real-time video generation preview and streaming
- Advanced animation effects (3D transitions, particles)
- Video style transfer and artistic filters
- Integration with more TTS models (ElevenLabs, Bark)
- Cloud deployment for horizontal scalability
- A/B testing for thumbnail and title optimization
- Analytics dashboard for generated content performance

## Performance Metrics

- **Script Generation**: ~10-30 seconds (LLM-dependent)
- **Image Generation**: ~5-10 seconds per scene (GPU-dependent)
- **Audio Synthesis**: ~3-5 seconds per scene
- **Video Animation**: ~2-4 seconds per scene
- **Subtitle Alignment**: ~5-10 seconds total
- **Music Generation**: ~15-30 seconds
- **Total Pipeline (short, 5 scenes)**: ~3-5 minutes
- **Total Pipeline (long, 20 scenes)**: ~15-25 minutes

---

## Detailed AI Models

### 1. **Stable Diffusion (AUTOMATIC1111 WebUI)**
- **Model**: Juggernaut-XL with face detail LoRA
- **Usage**: Image generation from text prompts (scenes, thumbnails)
- **Code excerpt**:
  ```python
  # filepath: scripts/images/generate_image.py
  STABLE_DIFFUSION_URL = "http://127.0.0.1:7860/sdapi/v1/txt2img"
  response = requests.post(STABLE_DIFFUSION_URL, json=payload)
  ```
- **Prerequisites**:
  - WebUI running with `--api` flag
  - Models `.safetensors` in `models/Stable-diffusion/`
  - LoRA in `models/Lora/`
- **Features**: txt2img, img2img, LoRA, VAE, upscalers, face restoration

---

### 2. **Coqui TTS (XTTS v2)**
- **Model**: `tts_models/multilingual/multi-dataset/xtts_v2`
- **Usage**: Multilingual voice cloning from a WAV reference file
- **Code excerpt**:
  ```python
  # filepath: scripts/audio/generate_audio.py
  from TTS.api import TTS
  tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)
  tts.tts_to_file(text=scene_text, speaker_wav=reference_wav, file_path=output_path)
  ```
- **Prerequisites**: `pip install TTS`, WAV reference file per language
- **Features**: multilingual synthesis (FR/EN/ES), voice cloning, per-scene audio generation

---

### 3. **Ollama (Gemma, DeepSeek, Ministral)**
- **Models**: `gemma3:12b`, `deepseek-r1:latest`, `ministral-3:14b`
- **Usage**: LLM-based script generation, verification, translation
- **Code excerpt**:
  ```python
  # filepath: scripts/script/generate_script.py
  from ollama import Client
  client = Client(host='http://localhost:11434')
  response = client.generate(model="gemma3:12b", prompt=prompt)
  ```
- **Prerequisites**: Ollama server running, models pulled
- **Features**: structured JSON script output, scene/title/prompt generation, double LLM validation

---

### 4. **CLIP (OpenAI)**
- **Model**: `openai/clip-vit-base-patch32`
- **Usage**: Image-text similarity scoring for quality verification
- **Code excerpt**:
  ```python
  # filepath: scripts/images/verify_image.py
  from transformers import CLIPProcessor, CLIPModel
  clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
  clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
  ```
- **Prerequisites**: `pip install transformers`, GPU recommended
- **Features**: CLIP score calculation, automatic filtering of low-relevance images

---

### 5. **Whisper (OpenAI)**
- **Model**: Whisper base
- **Usage**: Automatic subtitle alignment from audio transcription
- **Code excerpt**:
  ```python
  # filepath: scripts/video/align_subtitles.py
  import whisper
  model = whisper.load_model("base")
  result = model.transcribe(audio_path)
  ```
- **Prerequisites**: `pip install openai-whisper`, ffmpeg
- **Features**: multilingual transcription, word-level timing, subtitle JSON export

---

### 6. **MediaPipe (Face Detection)**
- **Model**: MediaPipe Face Detection
- **Usage**: Detect faces in generated images for quality filtering
- **Code excerpt**:
  ```python
  # filepath: scripts/images/verify_image.py
  import mediapipe as mp
  mp_face_detection = mp.solutions.face_detection
  ```
- **Prerequisites**: `pip install mediapipe`
- **Features**: face detection, automatic rejection of images without expected faces

---

### 7. **Facebook MusicGen**
- **Model**: `facebook/musicgen-medium`
- **Usage**: AI-generated background music from text prompts
- **Code excerpt**:
  ```python
  # filepath: scripts/music/generate_music.py
  from transformers import AutoProcessor, MusicgenForConditionalGeneration
  processor = AutoProcessor.from_pretrained("facebook/musicgen-medium")
  model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-medium")
  ```
- **Prerequisites**: `pip install transformers pydub soundfile`, ffmpeg
- **Features**: original music generation from prompts, automatic duration matching, direct pipeline integration

---

### 8. **MoviePy + OpenCV**
- **Usage**: Video editing, camera animation (zoom, pan, slide), audio synchronization, subtitle overlay
- **Code excerpt**:
  ```python
  # filepath: scripts/video/generate_movement.py
  from moviepy.editor import ImageSequenceClip, AudioFileClip, VideoFileClip, concatenate_videoclips
  ```
- **Prerequisites**: `pip install moviepy opencv-python`, ffmpeg
- **Features**: image animation, TikTok/YouTube crop, subtitle rendering, video concatenation, music mixing

---

## Resources & Credits

- [Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
- [Coqui TTS](https://github.com/coqui-ai/TTS)
- [Ollama](https://ollama.ai/)
- [MoviePy](https://zulko.github.io/moviepy/)
- [OpenAI Whisper](https://github.com/openai/whisper)
- [Facebook MusicGen](https://huggingface.co/facebook/musicgen-medium)
- [Pexels API](https://www.pexels.com/api/)
- **Developer**: Cedric Chanfreau
- **Web Application**: [video-automation.littlenuage.com](https://video-automation.littlenuage.com/)

## License

See `stable-diffusion-webui/LICENSE.txt` for the WebUI license. Other scripts are under your chosen license.

---

## Try It Yourself!

**Access the application**: [https://video-automation.littlenuage.com/](https://video-automation.littlenuage.com/)

1. Select your video type and category
2. Choose an entity from the list (or add your own)
3. Pick a language and production mode (short/long)
4. Add the job to the queue or generate step-by-step
5. Monitor progress via Discord notifications
6. Download or upload directly to YouTube

<img src="/img/automation-video/workflow.png" alt="IA Automation Workflow" style="width: 100%;" />

---
layout: default
title:  "IA Automation"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

[← Back to Personal Project](./my-perso-projects.html)

# IA Automation Project Overview

**🚀 [Try the application here: https://video-automation.littlenuage.com/](https://video-automation.littlenuage.com/)**

This project automates the creation of narrated videos from a script, leveraging AI for image generation, voice synthesis, and video assembly. The workflow is fully automated: you provide a script, and the system generates images, audio, and assembles everything into a video.

## Project Context

Developed as a personal project to streamline video content creation, this system enables rapid production of professional-quality narrated videos without manual intervention. The application is deployed online and accessible via a web interface, allowing anyone to generate videos from text descriptions.

## Overview

The pipeline takes a written script, splits it into scenes, generates images for each scene using Stable Diffusion, creates narration with Coqui TTS, and then assembles everything into an animated video (slow zoom on each image, audio synchronization).

## What I Developed

### Core Features

**1. Automated Video Generation Pipeline**
- **Script Processing**: Parse and structure text into scenes with image prompts
- **AI Image Generation**: Integration with Stable Diffusion API for scene visualization
- **Voice Synthesis**: Coqui TTS integration with custom voice cloning from reference audio
- **Video Assembly**: MoviePy-based animation system with synchronized audio/video

**2. Web Application (Flask)**
- **User Interface** (`app.py`, `app2.py`): Web-based interface for script upload and video generation
- **RESTful API**: Backend endpoints for processing requests and monitoring progress
- **File Management**: Organized input/output system for scripts, images, audio, and videos
- **Multi-category Support**: Specialized workflows for celebrities, geography, monuments, movies, etc.

**3. Advanced Processing Tools**

**Script Generation & Verification**:
- `generate-script.py`: Create structured JSON scripts from text
- `generate-script-actu.py`: Generate news/current events scripts
- `verify-script.py`: Validate script structure and content

**Image Processing**:
- `generate_all_image.py`: Batch image generation for multiple scenes
- `generate-mignature.py`, `generate-mignature2.py`: Thumbnail creation
- `verify-image.py`: Quality control and validation
- `generate-new-image.py`: Regenerate specific scenes

**Audio Processing**:
- `generate_all_audio.py`: Batch audio synthesis
- `cut-audio.py`: Audio trimming and segmentation
- `verify-audio.py`: Audio quality checks
- `extend-audio.py`: Audio extension for timing adjustments
- `extract-audio-from-mp4.py`: Audio extraction from video files

**Video Processing**:
- `generate-movement.py`: Camera movement effects (zoom, pan)
- `generate-text-on-video.py`: Subtitle and text overlay
- `cut_txt_video.py`: Video segmentation with text sync
- `align-subtitles.py`: Subtitle alignment and timing
- `corrected-subtitles-by-words.py`: Word-level subtitle correction
- `short-end-pub.py`: Add promotional end screens

**4. Integration & Deployment**
- `send-to-youtube.py`: Automated YouTube upload with metadata
- `authentification/`: OAuth and API authentication system
- `utils.py`: Shared utilities and helper functions
- `main.py`: Orchestration script for full pipeline execution

**5. Music & Audio Enhancement**
- `generate-music.py`: Background music generation/selection
- Audio mixing and volume normalization
- Multi-track audio synchronization

### Technical Architecture

**Backend Stack**:
- **Python 3.9+**: Core programming language
- **Flask**: Web framework for API and UI
- **Stable Diffusion WebUI**: Local deployment for image generation
- **Coqui TTS**: Neural voice synthesis
- **MoviePy**: Video editing and assembly
- **OpenCV**: Image processing and effects

**Key Integrations**:
- Stable Diffusion API (local `http://127.0.0.1:7860`)
- YouTube Data API v3 (automated uploads)
- Custom authentication system (OAuth2)
- Configuration management (YAML, JSON, XML)

**Processing Categories**:
- **Celebrity**: Biography and career videos
- **Geography**: Location and travel documentaries
- **Monument**: Historical and architectural features
- **Movie**: Film analysis and summaries
- **News/Actu**: Current events and news reports
- **Art/Oeuvre**: Artistic works and analysis

### Innovation & Features

**Intelligent Scene Management**:
- Automatic scene detection and splitting
- Context-aware prompt generation for images
- Duration optimization based on narration length

**Quality Control System**:
- Multi-stage verification (script, image, audio)
- Automated error detection and correction
- Manual intervention points for quality assurance

**Scalability**:
- Batch processing for multiple videos
- Parallel generation of images and audio
- Caching system for reusable assets

**Customization**:
- Template system for different video styles
- Configurable animation parameters
- Multiple voice profiles and languages

## File Organization

```
.
├── generate-script.py
├── generate-image.py
├── generate-audio.py
├── generate-animation.py
├── generate-video-image.py
├── input/
│   └── Audio/
│       └── Enregistrement-francais.wav
├── output/
│   ├── Script/
│   ├── Image/
│   ├── Audio/
│   │   └── scenes/
│   ├── Video/
└── stable-diffusion-webui/
```
- **input/**: source files (text, reference audio)
- **output/**: generated results (JSON scripts, images, audios, videos)
- **stable-diffusion-webui/**: WebUI and models for Stable Diffusion

## Workflow

### 1. Script Preparation

- Write your script and split it into scenes.
- Each scene contains text and an image prompt.
- Save the script as JSON in `output/Script/script.json`:

```json
[
  {
    "scene": 1,
    "texte": "Le soleil se lève sur la ville.",
    "prompt_image": "A beautiful sunrise over a city skyline, vibrant colors."
  }
]
```

### 2. Image Generation

- Run `generate-image.py` to generate one image per scene via Stable Diffusion.
- Images are saved in `output/Image/scene_X.png`.

### 3. Audio Generation

- Run `generate-audio.py` to generate narration for each scene with Coqui TTS and a reference audio file.
- Audio files are saved in `output/Audio/scenes/scene_X.wav`.

### 4. Animation & Video Editing

- Run `generate-animation.py` to create a video for each scene: animation (slow zoom) and audio synchronization.
- Videos are saved in `output/Video/scene_X.mp4`.

### 5. Final Assembly

- (Optional) Use `generate-video-image.py` to merge all scenes into a complete video.

## Scripts

- `generate-script.py`: prepares the JSON script
- `generate-image.py`: generates images via Stable Diffusion
- `generate-audio.py`: synthesizes voice-over with Coqui TTS
- `generate-animation.py`: assembles image and audio into animated video
- `generate-video-image.py`: merges scene videos

## Stable Diffusion WebUI

- Used for image generation ([Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui))
- Must be run locally (`http://127.0.0.1:7860`)
- Place your models and configure the WebUI as needed

## Prerequisites

- Python 3.9+
- [moviepy](https://pypi.org/project/moviepy/)
- [requests](https://pypi.org/project/requests/)
- [Coqui TTS](https://github.com/coqui-ai/TTS)
- [Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
- Dependencies from `stable-diffusion-webui/requirements.txt`

Installation:
```sh
pip install -r stable-diffusion-webui/requirements.txt
pip install moviepy requests TTS
```

## Troubleshooting

- **Stable Diffusion API error**: check that the WebUI is running and the model is loaded
- **Module not found**: install missing Python packages
- **Audio not generated**: check the path to the reference WAV file
- **Image/audio mismatch**: ensure scene numbers match

## Development Challenges & Solutions

**Challenge 1: Audio-Visual Synchronization**
- **Problem**: Ensuring audio narration perfectly matches video duration
- **Solution**: Dynamic timing calculation, audio stretching/compression, and frame rate adjustment

**Challenge 2: AI Model Integration**
- **Problem**: Stable Diffusion and TTS models require significant computational resources
- **Solution**: Local GPU deployment, request queuing, and caching mechanisms

**Challenge 3: Quality Consistency**
- **Problem**: AI-generated content can vary in quality
- **Solution**: Multi-stage verification pipeline with manual review checkpoints

**Challenge 4: Scalability**
- **Problem**: Processing multiple videos simultaneously
- **Solution**: Asynchronous task processing, batch operations, and resource management

## Use Cases & Applications

- **Educational Content**: Create explainer videos on any topic
- **Social Media**: Generate engaging short-form content
- **Marketing**: Product presentations and promotional videos
- **Documentation**: Tutorial and how-to videos
- **News**: Automated news reports with visual support
- **Entertainment**: Story-telling and narrative videos

## Future Enhancements

- Multi-language support with automatic translation
- Real-time video generation and streaming
- Advanced animation effects (3D transitions, particles)
- AI-powered script writing assistance
- Video style transfer and artistic filters
- Integration with more TTS and image generation models
- Cloud deployment for scalability

## Performance Metrics

- **Image Generation**: ~5-10 seconds per scene (GPU-dependent)
- **Audio Synthesis**: ~2-3 seconds per scene
- **Video Assembly**: ~1-2 seconds per scene
- **Total Pipeline**: ~2-5 minutes for a 5-scene video

## Resources & Credits

- [Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
- [Coqui TTS](https://github.com/coqui-ai/TTS)
- [moviepy](https://zulko.github.io/moviepy/)
- **Developer**: Cédric Chanfreau
- **Web Application**: [video-automation.littlenuage.com](https://video-automation.littlenuage.com/)

## License

See `stable-diffusion-webui/LICENSE.txt` for the WebUI license. Other scripts are under your chosen license.

---

## Try It Yourself!

**Access the application**: [https://video-automation.littlenuage.com/](https://video-automation.littlenuage.com/)

1. Write your script with scene descriptions
2. Provide image prompts for each scene
3. Upload a voice reference (optional)
4. Click generate and wait for your video!

<img src="/img/automation-video/workflow.png" alt="IA Automation Workflow" style="width: 100%;" />


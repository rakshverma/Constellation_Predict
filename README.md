# Constellation Predictor 🌟

An AI-powered web application for constellation identification and exploration, featuring YOLO-based image recognition (via Hugging Face Space API), real-time GPS location services, and multilingual chatbot assistance with speech capabilities.

## ✨ Features

### 🔍 **Smart Constellation Detection**
- **Cloud AI Inference**: Constellation detection powered by a custom YOLOv8 model hosted on [Hugging Face Spaces](https://huggingface.co/spaces/rverma0631/Constellation_YOLO)
- **16 Supported Constellations**: Aquila, Boötes, Canis Major, Canis Minor, Cassiopeia, Cygnus, Gemini, Leo, Lyra, Moon, Orion, Pleiades, Sagittarius, Scorpius, Taurus, Ursa Major
- **Real-time Processing**: Instant constellation recognition from uploaded images

### 🗺️ **Interactive Constellation Locator**
- **GPS Integration**: Automatic location detection for personalized sky mapping
- **Compass Navigation**: Built-in calibration for accurate mobile positioning
- **Nearest Constellation Finder**: Discover visible constellations based on your location

### 🤖 **Multilingual AI Chatbot**
- **Dual Language Support**: English and Hindi with optimized speech recognition
- **Voice Interaction**: Speech-to-text input and text-to-speech output
- **Gemini AI Integration**: Powered by Google's advanced language model
- **Constellation Knowledge Base**: Comprehensive astronomical information

### 📊 **Constellation Database**
- All 88 IAU-recognized constellations for browsing
- Detailed metadata and astronomical information
- High-quality constellation imagery

---

## 🚀 Quick Start

### Prerequisites

Install `uv` package manager:

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```bash
winget install --id=astral-sh.uv -e
```

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Constellation_Predict
   ```

2. **Run the build script:**
   ```bash
   chmod +x build.sh start.sh
   ./build.sh
   ```

3. **Configure environment variables:**

   Create `.env` file in the project root:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   SECRET_KEY=your_django_secret_key_here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   HF_SPACE=rverma0631/Constellation_YOLO
   ```

   Get your Gemini API key from [Google AI Studio](https://studio.google.com/apikey)

4. **Start the server:**
   ```bash
   ./start.sh
   ```

5. **Access the application:**

   Open your browser and navigate to `http://127.0.0.1:8000`

---

## 🛠️ Technology Stack

### Backend
- **Framework**: Django 6.0.2
- **Language**: Python 3.11-3.12
- **Database**: SQLite (default) / PostgreSQL (optional)
- **Package Manager**: uv

### AI/ML
- **Constellation Detection**: Custom YOLOv8 model (16 classes) — hosted on Hugging Face Spaces, called via `gradio-client`
- **Speech Recognition**: Whisper (via Gradio Client — `rverma0631/Whisper`)
- **Language Model**: Google Gemini AI (Gemini 2.0 Flash)
- **Computer Vision**: OpenCV 4.11+

### APIs & Services
- **Gradio Client**: Remote YOLO & Whisper API integration
- **Google Generative AI**: Chatbot intelligence
- **gTTS**: Text-to-speech synthesis

### Frontend
- **HTML5/CSS3/JavaScript**: Responsive design
- **Image Format**: WebP optimization for fast loading

---

## 📁 Project Structure

```
Constellation_Predict/
├── build.sh                             # Setup and build script
├── start.sh                             # Server startup script
├── pyproject.toml                       # Project dependencies
├── .gitignore                           # Git ignore rules
│
└── ConstellationPredictor/              # Main Django project
    ├── manage.py                        # Django management script
    ├── db.sqlite3                       # SQLite database
    ├── .env.example                     # Environment template
    │
    ├── ConstellationPredictor/          # Project settings
    │   ├── settings.py                  # Django configuration
    │   ├── urls.py                      # URL routing
    │   └── wsgi.py                      # WSGI configuration
    │
    ├── Predictor/                       # Core prediction engine
    │   ├── static/images/               # 88 constellation images (WebP)
    │   ├── templates/                   # HTML templates
    │   ├── models.py                    # Database models
    │   └── views.py                     # Prediction logic (calls HF Space API)
    │
    ├── chatbot/                         # AI chatbot module
    │   ├── templates/                   # Chatbot interface
    │   ├── views.py                     # Chatbot logic & Gemini integration
    │   └── urls.py                      # Chatbot routes
    │
    └── Locator/                         # GPS & compass module
        ├── templates/Locator/           # Location interface
        ├── models.py                    # Location data models
        ├── views.py                     # Location services
        └── urls.py                      # Locator routes
```

---

## 🎯 Model Specifications

### Constellation Detection Model

Hosted at: [rverma0631/Constellation_YOLO](https://huggingface.co/spaces/rverma0631/Constellation_YOLO)

| Metric | Value |
|--------|-------|
| **Architecture** | YOLOv8n |
| **Classes** | 16 |
| **mAP@50** | 95.8% |
| **mAP@50-95** | 59.0% |
| **Precision** | 90.5% |
| **Recall** | 95.6% |
| **Training Epochs** | 60 |

### Detectable Constellations (16)

| # | Constellation | # | Constellation |
|---|--------------|---|--------------|
| 1 | Aquila | 9 | Lyra |
| 2 | Boötes | 10 | Moon |
| 3 | Canis Major | 11 | Orion |
| 4 | Canis Minor | 12 | Pleiades |
| 5 | Cassiopeia | 13 | Sagittarius |
| 6 | Cygnus | 14 | Scorpius |
| 7 | Gemini | 15 | Taurus |
| 8 | Leo | 16 | Ursa Major |

---

## 🌐 Application Routes

| Route | Description |
|-------|-------------|
| `/` | Home page with project overview |
| `/predict/` | Constellation prediction interface |
| `/upload/` | Image upload for detection |
| `/detect/` | Real-time detection |
| `/database/` | Browse all 88 IAU constellations |
| `/chatbot/` | AI assistant with voice support |
| `/locator/` | GPS-based constellation finder |

---

## 📸 Application Screenshots

### 🏠 Home Page
![Home Page](images/home.png)

### 🔮 Predict
![Predict Page](images/predict.png)

### 📤 Upload
![Upload Page](images/upload.png)

### 🎯 Detect
![Detection Results](images/detect.png)

### 📚 Database
![Database Page](images/database.png)

### 🤖 Chatbot
![Chatbot Page](images/chatbot.png)

### 🧭 Locator
![Locator Page](images/locator.png)

---

## ⚙️ Configuration

### Environment Variables

```env
# Required
GEMINI_API_KEY=your_gemini_api_key_here

# Django Settings
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Hugging Face Space (constellation model)
HF_SPACE=rverma0631/Constellation_YOLO

# Optional: PostgreSQL (default is SQLite)
# DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

### Production Deployment

1. Set `DEBUG=False`
2. Configure `ALLOWED_HOSTS` with your domain
3. Generate a strong `SECRET_KEY`
4. Optionally configure PostgreSQL via `DATABASE_URL`

---

## 📦 Core Dependencies

| Package | Purpose |
|---------|---------|
| `django>=5.2.3` | Web framework |
| `gradio-client>=1.3.0` | YOLO & Whisper API calls |
| `opencv-python>=4.11.0` | Image preprocessing |
| `google-generativeai>=0.8.0` | Gemini AI chatbot |
| `gtts>=2.5.4` | Text-to-speech |
| `python-dotenv>=1.0.0` | Environment management |
| `pillow>=11.0.0` | Image processing |
| `numpy>=2.0.0` | Numerical computing |

> **No local ML models required** — YOLO inference runs on Hugging Face Spaces.

---

## 🚢 Deployment

```bash
# 1. Build (run once)
./build.sh

# 2. Start server
./start.sh
```

**Deployment size**: ~200 MB (no PyTorch/YOLO weights needed locally)

---

## 🌟 Acknowledgments

- **Ultralytics YOLOv8**: Object detection framework
- **Hugging Face Spaces**: Model hosting
- **Google Gemini**: AI language model
- **IAU**: International Astronomical Union for constellation standards

---

**Explore the cosmos with AI-powered precision! 🌌✨**

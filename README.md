# Constellation Predictor 🌟

An AI-powered web application for constellation identification and exploration, featuring advanced YOLO-based image recognition, real-time GPS location services, and multilingual chatbot assistance with speech capabilities.

## ✨ Features

### 🔍 **Smart Constellation Detection**
- **Dual-Model AI System**: Custom-trained YOLO models for accurate constellation identification
- **COCO Dataset Validation**: Prevents false positives from everyday objects
- **Real-time Processing**: Instant constellation recognition from uploaded images
- **88 IAU Constellations**: Complete database of officially recognized constellations

### 🗺️ **Interactive Constellation Locator**
- **GPS Integration**: Automatic location detection for personalized sky mapping
- **Compass Navigation**: Built-in calibration for accurate mobile positioning
- **Nearest Constellation Finder**: Discover visible constellations based on your location

### 🤖 **Multilingual AI Chatbot**
- **Dual Language Support**: English and Hindi with optimized speech recognition
- **Voice Interaction**: Speech-to-text input and text-to-speech output
- **Gemini AI Integration**: Powered by Google's advanced language model
- **Constellation Knowledge Base**: Comprehensive astronomical information

### 📊 **Complete IAU Database**
- All 88 officially recognized constellations
- Detailed metadata and astronomical information
- High-quality constellation imagery
- Interactive database exploration

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
   cd Constellation_predictor2
   ```

2. **Run the build script:**
   ```bash
   chmod +x build.sh start.sh
   ./build.sh
   ```

3. **Configure environment variables:**
   
   Create `.env` file in `ConstellationPredictor/` directory:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   SECRET_KEY=your_django_secret_key_here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
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

### AI/ML Models
- **Object Detection**: YOLO v8 & v11 (Ultralytics)
- **Model Weights**:
  - `yolo11n.pt` - YOLO v11 Nano (6.2 MB) - COCO object detection
  - `yolov8n.pt` - YOLO v8 Nano (6.2 MB) - Backup model
  - `best.pt` - Custom-trained constellation model (12.4 MB)
  - `last.pt` - Latest training checkpoint (12.4 MB)
- **Speech Recognition**: Whisper (via Gradio Client)
- **Language Model**: Google Gemini AI
- **Computer Vision**: OpenCV 4.11+

### APIs & Services
- **Gradio Client**: Remote Whisper API integration
- **Google Generative AI**: Chatbot intelligence
- **gTTS**: Text-to-speech synthesis

### Frontend
- **HTML5/CSS3/JavaScript**: Responsive design
- **Image Format**: WebP optimization for fast loading

---

## 📁 Project Structure

```
Constellation_predictor2/
├── build.sh                             # Setup and build script
├── start.sh                             # Server startup script
├── pyproject.toml                       # Project dependencies
├── .gitignore                           # Git ignore rules
│
└── ConstellationPredictor/              # Main Django project
    ├── manage.py                        # Django management script
    ├── db.sqlite3                       # SQLite database
    ├── .env                             # Environment variables (create this)
    ├── .env.example                     # Environment template
    │
    ├── ConstellationPredictor/          # Project settings
    │   ├── settings.py                  # Django configuration
    │   ├── urls.py                      # URL routing
    │   └── wsgi.py                      # WSGI configuration
    │
    ├── Predictor/                       # Core prediction engine
    │   ├── REAL_TIME_DETECTOR/          # YOLO models and training
    │   │   ├── yolo11n.pt               # YOLO v11 Nano (6.2 MB)
    │   │   ├── yolov8n.pt               # YOLO v8 Nano (6.2 MB)
    │   │   └── runs/detect/train/weights/
    │   │       ├── best.pt              # Best constellation model (12.4 MB)
    │   │       └── last.pt              # Latest checkpoint (12.4 MB)
    │   ├── static/images/               # 88 constellation images (WebP)
    │   ├── templates/                   # HTML templates
    │   ├── models.py                    # Database models
    │   └── views.py                     # Prediction logic
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

### YOLO Models

| Model | Size | Purpose | Accuracy |
|-------|------|---------|----------|
| `yolo11n.pt` | 5.4 MB | COCO object detection | High |
| `yolov8n.pt` | 6.2 MB | Backup object detection | High |
| `best.pt` | 12.4 MB | Custom constellation detection | Optimized |
| `last.pt` | 12.4 MB | Latest training checkpoint | Training |

### Custom Constellation Model Performance

Our custom-trained YOLO model (`best.pt`) achieves excellent performance on constellation detection:

| Metric | Value | Description |
|--------|-------|-------------|
| **mAP@50** | **95.8%** | Mean Average Precision at IoU threshold 0.5 |
| **mAP@50-95** | **59.0%** | Mean Average Precision across IoU 0.5-0.95 |
| **Precision** | **90.5%** | Accuracy of positive predictions |
| **Recall** | **95.6%** | Ability to find all constellations |
| **Training Epochs** | 60 | Total training iterations |

#### Performance Highlights
- ✅ **High Recall (95.6%)**: Excellent at detecting all constellations in images
- ✅ **Strong Precision (90.5%)**: Minimal false positives
- ✅ **Robust mAP@50 (95.8%)**: Outstanding performance at standard IoU threshold
- ✅ **COCO Validation**: Prevents misclassification of everyday objects

### Training Details
- **Primary Dataset**: Custom constellation imagery
- **Validation Dataset**: COCO dataset (80 object classes)
- **Training Framework**: Ultralytics YOLOv8/v11
- **Purpose**: Distinguish celestial objects from terrestrial items
- **Optimization**: Prevents false positives on everyday objects
- **Training Time**: ~2,078 seconds (34.6 minutes)

### Available Training Artifacts
The model includes comprehensive training visualizations:
- **Confusion Matrix**: Classification accuracy breakdown
- **F1 Curve**: F1-score vs confidence threshold
- **Precision-Recall Curve**: Model performance trade-offs
- **Training Batches**: Sample training images with annotations
- **Validation Results**: Predicted vs ground truth comparisons

---

## 🌐 Application Routes

| Route | Description |
|-------|-------------|
| `/` | Home page with project overview |
| `/predict/` | Constellation prediction interface |
| `/upload/` | Image upload for detection |
| `/detect/` | Detection results display |
| `/database/` | Browse all 88 IAU constellations |
| `/chatbot/` | AI assistant with voice support |
| `/locator/` | GPS-based constellation finder |

---

## � Application Screenshots

### 🏠 Home Page
Landing page with project overview and navigation

![Home Page](images/home.png)

### 🔮 Predict
Choose between uploaded image or real database prediction

![Predict Page](images/predict.png)

### 📤 Upload
Direct image upload interface for constellation detection

![Upload Page](images/upload.png)

### 🎯 Detect
Real-time constellation detection results with AI analysis

![Detection Results](images/detect.png)

### 📚 Database
Browse all 88 IAU-recognized constellations with detailed information

![Database Page](images/database.png)

### 🤖 Chatbot
AI assistant with voice support (English/Hindi) and constellation knowledge

![Chatbot Page](images/chatbot.png)

### 🧭 Locator
GPS-based constellation finder with compass navigation for mobile devices

![Locator Page](images/locator.png)

---

## �🔧 Configuration

### Environment Variables

Create `.env` in `ConstellationPredictor/` directory:

```env
# Required
GEMINI_API_KEY=your_gemini_api_key_here

# Django Settings
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Optional: PostgreSQL (default is SQLite)
# DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

### Production Deployment

For production deployment:

1. Set `DEBUG=False`
2. Configure `ALLOWED_HOSTS` with your domain
3. Generate a strong `SECRET_KEY`
4. Optionally configure PostgreSQL via `DATABASE_URL`

---

## 📦 Dependencies

### Core Dependencies
- `django>=5.2.3` - Web framework
- `ultralytics>=8.3.0` - YOLO models
- `opencv-python>=4.11.0` - Computer vision
- `google-generativeai>=0.8.0` - Gemini AI
- `gradio-client>=0.10.0` - Whisper API
- `gtts>=2.5.4` - Text-to-speech
- `python-dotenv>=1.0.0` - Environment management
- `psycopg2-binary>=2.9.0` - PostgreSQL support
- `dj-database-url>=2.0.0` - Database URL parsing
- `pillow>=11.0.0` - Image processing
- `numpy>=2.0.0` - Numerical computing

**Total Package Count**: 82 Python packages  
**System Dependencies**: None required

---

## 🧪 Testing

The application includes comprehensive testing resources:

### Test Images
Use sample constellation images to validate model accuracy and demonstrate capabilities.

### Model Validation
- COCO dataset integration prevents false positives
- Custom constellation training ensures accurate celestial object recognition
- Multiple model checkpoints for performance comparison

---

## 📊 Performance

### Model Performance
- **Detection Speed**: Real-time (<1s per image)
- **Accuracy**: Optimized for constellation recognition
- **False Positive Rate**: Minimized via COCO validation

### Application Performance
- **Image Format**: WebP for 30-50% size reduction
- **Database**: SQLite for lightweight deployment
- **API Integration**: Async Gradio client for speech processing

---

## 🚢 Deployment

### Build & Deploy

```bash
# 1. Build (run once)
./build.sh

# 2. Start server
./start.sh
```

### Docker Deployment (Optional)

The application is optimized for lightweight deployment without Docker, but can be containerized if needed.

**Note**: Total deployment size is approximately 4-5GB due to ML dependencies (PyTorch, YOLO models, OpenCV).

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is open source. Please check the repository for specific license information.

---

## 🆘 Support

For issues, questions, or contributions:
- Open an issue on GitHub
- Check existing documentation
- Review the deployment summary

---

## 🌟 Acknowledgments

- **YOLO**: Ultralytics for object detection framework
- **Google Gemini**: AI language model
- **IAU**: International Astronomical Union for constellation standards
- **COCO Dataset**: Object detection validation

---

**Explore the cosmos with AI-powered precision! 🌌✨**

import cv2
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import numpy as np
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import base64
from datetime import datetime
import os
from django.conf import settings
import time
from PIL import Image
import io
import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from dotenv import load_dotenv

# ── Gradio API client ──────────────────────────────────────────────────────────
from gradio_client import Client, handle_file

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

HF_SPACE = os.getenv("HF_SPACE", "rverma0631/Constellation_YOLO")

# Shared client — created once at startup
_gradio_client = None

def get_gradio_client():
    global _gradio_client
    if _gradio_client is None:
        _gradio_client = Client(HF_SPACE)
        print(f"Gradio client connected to {HF_SPACE}")
    return _gradio_client


# ── Constellation info helpers (unchanged) ────────────────────────────────────
@csrf_exempt
@require_http_methods(["POST"])
def get_constellation_info(request):
    try:
        data = json.loads(request.body)
        constellation_name = data.get('constellation_name', '')

        if not constellation_name:
            return JsonResponse({'error': 'Constellation name is required'}, status=400)

        prompt = f"""
        Provide a brief, fascinating description of the constellation {constellation_name}. 
        Include key mythological background, notable stars, and interesting facts.
        Keep it concise, under 100 words, and engaging for general audience.
        """

        gemini_response = call_gemini_api(prompt)

        if gemini_response:
            info = gemini_response
        else:
            info = get_basic_constellation_info(constellation_name)

        return JsonResponse({
            'name': constellation_name,
            'info': info
        })

    except Exception as e:
        print(f"Error in get_constellation_info: {str(e)}")
        return JsonResponse({'error': 'Internal server error'}, status=500)


def call_gemini_api(prompt):
    try:
        headers = {'Content-Type': 'application/json'}
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"temperature": 0.7, "maxOutputTokens": 150},
        }
        response = requests.post(
            f"{GEMINI_API_URL}?key={GEMINI_API_KEY}",
            headers=headers,
            json=payload,
            timeout=10,
        )
        if response.status_code == 200:
            result = response.json()
            if 'candidates' in result and len(result['candidates']) > 0:
                return result['candidates'][0]['content']['parts'][0]['text']
        return None
    except Exception as e:
        print(f"Gemini API error: {str(e)}")
        return None


def get_basic_constellation_info(constellation_name):
    """Fallback constellation information"""
    basic_info = {
        'Andromeda': 'Named after the chained princess in Greek mythology. Contains the Andromeda Galaxy, our nearest major galactic neighbor, visible as a fuzzy patch to the naked eye.',
        'Orion': 'The Hunter constellation, featuring bright stars Betelgeuse and Rigel, plus the famous Orion Nebula where new stars are born.',
        'Ursa Major': 'The Great Bear, home to the Big Dipper. Its pointer stars lead to the North Star, making it crucial for navigation.',
        'Cassiopeia': 'The vain Queen forms a distinctive W-shape. This circumpolar constellation is visible year-round from northern latitudes.',
        'Leo': 'The Lion of spring skies. Bright star Regulus marks the lion\'s heart, while the "backwards question mark" forms its mane.',
        'Cygnus': 'The Swan flies along the Milky Way. Features Deneb, one of the most luminous stars known, and is also called the Northern Cross.',
        'Scorpius': 'The Scorpion with red heart Antares. In mythology, it killed Orion, which is why they\'re never visible together.',
        'Sagittarius': 'The Archer points toward our galaxy\'s center. Rich in star clusters and nebulae, including the beautiful Lagoon Nebula.',
        'Draco': 'The Dragon winds around the north pole. Its star Thuban was the pole star when Egyptian pyramids were built.',
        'Pegasus': 'The Winged Horse features the Great Square. Contains the first exoplanet discovered around a sun-like star.',
    }
    return basic_info.get(
        constellation_name,
        f"{constellation_name} is a constellation with rich astronomical and mythological significance, "
        f"containing unique stars and deep-sky objects that have fascinated humanity for millennia."
    )


# ── Gradio API inference helper ───────────────────────────────────────────────
def run_constellation_api(image_path: str, confidence: float = 0.25):
    """
    Call the HF Space Gradio API with a local image file path.
    Returns (annotated_image_path, summary_text) or raises on error.
    """
    client = get_gradio_client()
    result = client.predict(
        image=handle_file(image_path),
        confidence=confidence,
        api_name="/predict_constellation",
    )
    # result is a tuple: (annotated_image_path, summary_markdown)
    return result


# ── Real-time frame processing (uses API) ────────────────────────────────────
@csrf_exempt
def process_frame(request):
    """Frame processing for real-time video — calls Gradio API"""
    if request.method != 'POST' or 'frame' not in request.FILES:
        return HttpResponse(status=400)

    try:
        file = request.FILES['frame']
        if file.size > 5 * 1024 * 1024:
            return HttpResponse(status=413)

        # Save frame to a temp file for the API
        tmp_path = f"/tmp/frame_{int(time.time()*1000)}.jpg"
        with open(tmp_path, 'wb') as f:
            f.write(file.read())

        try:
            annotated_path, _ = run_constellation_api(tmp_path, confidence=0.25)

            # Read annotated image and return as JPEG bytes
            with open(annotated_path, 'rb') as f:
                return HttpResponse(f.read(), content_type='image/jpeg')
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    except Exception as e:
        print(f"Frame processing error: {e}")
        return HttpResponse(status=500)


# ── Views ─────────────────────────────────────────────────────────────────────
def home(request):
    return render(request, 'home.html')

def detect_view(request):
    return render(request, 'detect.html')

def database(request):
    return render(request, 'database.html')

def upload(request):
    return render(request, 'upload.html')

def predict(request):
    return render(request, 'predict.html')


# ── Static image upload processing (uses API) ─────────────────────────────────
@csrf_exempt
def process_upload(request):
    """Upload processing — calls Gradio API for constellation detection"""
    if request.method == 'POST':
        try:
            if 'image' not in request.FILES:
                messages.error(request, 'No image file uploaded.')
                return redirect('upload')

            file = request.FILES['image']
            location = request.POST.get('location', '').strip()
            capture_time = request.POST.get('capture_time', '')

            # Validate file type
            allowed_extensions = ['.jpg', '.jpeg', '.png']
            file_extension = os.path.splitext(file.name)[1].lower()
            if file_extension not in allowed_extensions:
                messages.error(request, 'Invalid file format. Please upload JPG, JPEG, or PNG files only.')
                return redirect('upload')

            # Validate file size (10MB limit)
            if file.size > 10 * 1024 * 1024:
                messages.error(request, 'File size too large. Please upload files smaller than 10MB.')
                return redirect('upload')

            # Read image for dimension info
            img_data = np.frombuffer(file.read(), np.uint8)
            frame = cv2.imdecode(img_data, cv2.IMREAD_COLOR)
            if frame is None:
                messages.error(request, 'Invalid image file. Please upload a valid image.')
                return redirect('upload')

            height, width = frame.shape[:2]

            # Save to temp file for API call
            tmp_path = f"/tmp/upload_{int(time.time()*1000)}{file_extension}"
            cv2.imwrite(tmp_path, frame)

            try:
                # ── Call Gradio API ──
                annotated_path, summary_text = run_constellation_api(tmp_path, confidence=0.25)

                # Parse detections from summary markdown
                detected_constellations = []
                for line in summary_text.splitlines():
                    line = line.strip()
                    if line.startswith('- **') and '—' in line:
                        # Format: "- **Name** — XX.X% confidence"
                        name_part = line.split('**')[1]
                        conf_part = line.split('—')[1].strip()
                        conf_val = float(conf_part.replace('% confidence', '').replace('%', '').strip()) / 100
                        detected_constellations.append({
                            'name': name_part,
                            'confidence': conf_val,
                        })

                # Read annotated image → base64
                with open(annotated_path, 'rb') as f:
                    img_base64 = base64.b64encode(f.read()).decode('utf-8')

            finally:
                if os.path.exists(tmp_path):
                    os.remove(tmp_path)

            context = {
                'processed_image': img_base64,
                'original_filename': file.name,
                'file_size': f"{file.size / 1024 / 1024:.2f} MB",
                'image_dimensions': f"{width} x {height}",
                'location': location,
                'capture_time': capture_time,
                'analysis_type': 'constellation',
                'max_confidence': max((d['confidence'] for d in detected_constellations), default=0),
                'detected_constellations': detected_constellations,
                'detected_objects': [],
                'total_detections': len(detected_constellations),
                'processing_timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }

            return render(request, 'results.html', context)

        except Exception as e:
            print(f"Error processing upload: {str(e)}")
            messages.error(request, f'Error processing image: {str(e)}')
            return redirect('upload')

    return redirect('upload')


def chatbot(request):
    return render(request, 'chatbot.html')

# cloudflared tunnel --url http://localhost:8000

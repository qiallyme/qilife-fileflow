import os
import pytesseract
from PIL import Image
from datetime import datetime

def extract_text_from_image(path):
    try:
        return pytesseract.image_to_string(Image.open(path))
    except Exception:
        return ""

def analyze_file(filepath):
    filename = os.path.basename(filepath)
    timestamp = os.path.getmtime(filepath)
    return {
        "text": extract_text_from_image(filepath),
        "timestamp": datetime.fromtimestamp(timestamp).strftime("%Y%m%d_%H%M%S"),
        "original_filename": filename
    }

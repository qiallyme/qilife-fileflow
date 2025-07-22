import os

def generate_new_name(filepath, metadata):
    # Basic rule: timestamp + first 5 words of OCR text
    base = metadata["timestamp"]
    text = metadata.get("text", "").strip().replace("\n", " ").replace("  ", " ")
    snippet = "_".join(text.split()[:5]) or "untitled"
    ext = os.path.splitext(filepath)[1]
    return f"{base}_{snippet}{ext}"

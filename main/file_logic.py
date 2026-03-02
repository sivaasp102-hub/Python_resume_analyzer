import os
from werkzeug.utils import secure_filename

def extract_text_from_file(file):
    if not file or file.filename == "":
        return None, "No file selected"
        
    if not file.filename.endswith('.txt'):
        return None, "Only .txt files are allowed"
        
    try:
        content = file.read().decode('utf-8')
        return content, None
    except Exception as e:
        return None, f"Error reading file: {str(e)}"

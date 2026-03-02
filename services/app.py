from flask import Flask, request, jsonify
from services.nlp_service import analyze_resume_service
from services.file_service import read_resume_file
from services.database_service import init_db, save_analysis, get_all_analyses
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "resume-analyzer-siva")


try:
    init_db()
except Exception as e:
    print(f"Database initialization warning: {e}, Ensure SQL Server is running and accessible.")

@app.route('/analyze-resume', methods=['POST'])
def analyze_resume():
    resume_text = ""
    
    if request.is_json:
        data = request.get_json()
        resume_text = data.get("resume_text", "")
        
    elif 'file' in request.files:
        file = request.files['file']
        text, error = read_resume_file(file)
        if error:
            return jsonify({"error": error}), 400
        resume_text = text
        
    else:
        return jsonify({"error": "No resume text or file provided"}), 400

    if not resume_text.strip():
        return jsonify({"error": "Empty resume content"}), 400

    try:
        analysis_result = analyze_resume_service(resume_text)
        
        try:
            save_analysis(analysis_result)
        except Exception as e:
            print(f"Error saving to database: {e}")
            
        return jsonify(analysis_result), 200
        
    except Exception as e:
        return jsonify({"error": f"Internal processing error: {str(e)}"}), 500

@app.route('/analyses', methods=['GET'])
def get_past_analyses():
    try:
        analyses = get_all_analyses()
        return jsonify(analyses), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

from flask import Flask, render_template, request, send_file
from neurodoc_core.ocr_engine import extract_text_from_file
from neurodoc_core.summarizer import summarize_text
import os
import uuid

app = Flask(__name__)

# Folders
UPLOAD_FOLDER = "uploads"
SUMMARY_FOLDER = "summaries"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(SUMMARY_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files['document']
    if uploaded_file.filename == '':
        return "No file selected"

    # Save the uploaded file
    file_id = str(uuid.uuid4())
    file_path = os.path.join(UPLOAD_FOLDER, file_id + "_" + uploaded_file.filename)
    uploaded_file.save(file_path)

    # OCR + Summarization
    ocr_text = extract_text_from_file(file_path)
    print("\n🔍 OCR Extracted Text (first 1000 chars):\n", ocr_text[:1000])
    summary = summarize_text(ocr_text)

    # Save summary
    summary_filename = file_id + "_summary.txt"
    summary_path = os.path.join(SUMMARY_FOLDER, summary_filename)
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write(summary)

    # Send to frontend
    return render_template("index.html", summary=summary, ocr_text=ocr_text, filename=summary_filename)

@app.route('/download/<filename>')
def download(filename):
    return send_file(os.path.join(SUMMARY_FOLDER, filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

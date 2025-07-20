# 🧠 NeuroDoc – Intelligent Offline Document Analyzer

NeuroDoc is a Flask-based offline AI application designed to analyze documents (PDFs/images) using OCR and summarization models. It extracts text from uploaded documents, generates human-readable summaries, and allows users to download them—all without requiring internet access during inference.

---

## 🚀 Features

- 📄 Upload PDF or image documents
- 🔍 Extract text using OCR (Tesseract)
- 🧠 Summarize text using a Transformer-based model (`facebook/bart-large-cnn`)
- 💾 Save and download summaries
- 🌐 Web-based interface built with Flask
- 📴 Runs **offline** after model download

---

## 📂 Folder Structure

```
NeuroDoc/
│
├── app.py                          # Main Flask backend
├── requirements.txt               # Python dependencies
├── Procfile                       # For Render deployment
├── render.yaml                    # Optional: Render config
│
├── templates/
│   └── index.html                 # Main frontend UI
│
├── static/                        # Static files (CSS/JS)
│
├── uploads/                       # Uploaded documents (auto-created)
├── summaries/                     # Generated summaries (auto-created)
│
├── neurodoc_core/                 # Core logic
│   ├── ocr_engine.py              # OCR using PyMuPDF + Tesseract
│   └── summarizer.py              # Summarization logic
```

---

## ⚙️ Installation (Offline / Local)

> Prerequisites:
> - Python 3.8+
> - Tesseract OCR installed on system

```bash
# Clone the repo
git clone https://github.com/BABIN-JOE/NeuroDoc.git
cd NeuroDoc

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Then open `http://localhost:5000` in your browser.

---

## 🧠 Models Used

| Task           | Model                     | Source                     |
|----------------|---------------------------|----------------------------|
| OCR            | Tesseract + PyMuPDF       | Local                      |
| Summarization  | facebook/bart-large-cnn   | HuggingFace Transformers  |

You can download and cache the BART model beforehand to make the app work fully offline.

---

## ☁️ Deploying on Render (Free Hosting)

1. Go to [https://render.com](https://render.com)
2. Click **"New Web Service"**
3. Connect your GitHub repo
4. Set:
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`
5. Select **Free Plan**
6. Click Deploy

> Make sure your `requirements.txt` and `Procfile` are present at the root.

---

## 📥 Upload Formats Supported

- PDF
- JPG / PNG / BMP
- TIFF (if Tesseract supports it)

---

## 📌 Notes

- Summaries and uploads are stored locally in `/summaries` and `/uploads`
- You can customize output format, compression, or add highlight detection easily
- Make sure Tesseract is installed and added to `PATH`

---

## 🧑‍💻 Developed By

**Babin Joe**  
[🌐 Portfolio](https://babin-joe-portfolio.vercel.app) • [GitHub](https://github.com/BABIN-JOE) • [LinkedIn](https://www.linkedin.com/in/babin-joe)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
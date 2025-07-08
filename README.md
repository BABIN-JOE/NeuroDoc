# 🧠 NeuroDoc - Intelligent Document Summarizer

**NeuroDoc** is an offline AI-powered document summarizer that extracts text from scanned or digital PDFs and generates concise summaries using local BART-based transformers.

## 🚀 Features
- ✅ OCR text extraction (Tesseract / PaddleOCR)
- ✅ Local summarization using `facebook/bart-large-cnn`
- ✅ Responsive frontend with light/dark toggle
- ✅ Summary + Raw OCR preview
- ✅ Downloadable summaries
- ✅ 100% offline and private

## 🛠️ Tech Stack
- Python, Flask
- HuggingFace Transformers (BART)
- PyMuPDF / pdf2image
- Tesseract OCR or PaddleOCR
- HTML / CSS / JS (Frontend)

## 🗂 Folder Structure
```
NeuroDoc/
├── app.py
├── neurodoc_core/
│   ├── ocr_engine.py
│   └── summarizer.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── model/
│   └── bart-large-cnn/     # (Locally stored model, not uploaded to GitHub)
├── uploads/                # Auto-created
├── summaries/              # Auto-created
├── README.md
├── requirements.txt
└── .gitignore
```

## ⚙️ How to Run
```bash
pip install -r requirements.txt
python app.py
```

## 🔐 Note
> Model files (`bart-large-cnn`) and large folders like `uploads/`, `summaries/` are excluded from GitHub due to size limits.

## 👤 Author
**Babin Joe**  
[GitHub](https://github.com/BABIN-JOE) • [LinkedIn](https://www.linkedin.com/in/babin-joe)

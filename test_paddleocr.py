from paddleocr import PaddleOCR

ocr = PaddleOCR(use_textline_orientation=True, lang='en')  # Recommended
image_path = r"C:\NeuroDoc\sample_image.jpg"  # full raw string path

try:
    result = ocr.ocr(image_path)
    
    if not result or not result[0]:
        print("⚠️ No text detected in the image.")
    else:
        for line in result[0]:  # Safely access first result
            text = line[1][0]
            score = line[1][1]
            print(f"📄 Text: {text} (Confidence: {score:.2f})")

except Exception as e:
    print("❌ ERROR:", e)

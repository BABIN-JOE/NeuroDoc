import re
from transformers import BartTokenizer, BartForConditionalGeneration

# ✅ Load the local model
MODEL_PATH = r"C:\NeuroDoc\model\bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(MODEL_PATH)
model = BartForConditionalGeneration.from_pretrained(MODEL_PATH)

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # remove excessive whitespace/newlines
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)  # remove non-ASCII characters
    text = re.sub(r'(nd JavaScript\.?)+', '', text, flags=re.I)
    text = re.sub(r'(Click here.*?\.com)', '', text, flags=re.I)
    text = re.sub(r'(CNN\.com.*?iReport\.com)', '', text, flags=re.I)
    return text.strip()

def summarize_text(full_text):
    full_text = clean_text(full_text)
    max_chunk_size = 3000  # approx 1024 tokens
    chunks = [full_text[i:i+max_chunk_size] for i in range(0, len(full_text), max_chunk_size)]

    # Optionally limit the number of chunks to process
    max_chunks = 3
    chunks = chunks[:max_chunks]

    final_summary = ""

    for i, chunk in enumerate(chunks):
        print(f"\n🧩 CHUNK {i+1} LENGTH: {len(chunk)}")
        print(f"🧩 CHUNK {i+1} TEXT (start): {chunk[:150]}")

        inputs = tokenizer([chunk], max_length=1024, return_tensors='pt', truncation=True)
        summary_ids = model.generate(
            inputs['input_ids'],
            max_length=350,               # increased output length
            min_length=100,               # ensure richer summaries
            length_penalty=1.0,           # balanced output
            num_beams=6,                  # better quality
            no_repeat_ngram_size=3,       # avoid repetitive phrases
            early_stopping=True
        )

        partial_summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        print(f"📝 GENERATED SUMMARY {i+1} (start): {partial_summary[:200]}")

        if len(partial_summary.strip()) < 50:
            partial_summary = "[Content too short or unclear for summarization]"

        final_summary += partial_summary + "\n\n"

    return final_summary.strip()

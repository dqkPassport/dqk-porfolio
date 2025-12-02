import PyPDF2
import openai

openai.api_key = "YOUR_API_KEY"

def extract_text(path):
    text = ""
    reader = PyPDF2.PdfReader(path)
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def summarize(text):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Summarize this:\n{text}"}]
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    pdf_path = "sample.pdf"
    content = extract_text(pdf_path)
    print("Summary:\n")
    print(summarize(content))

from docx import Document
from pypdf import PdfReader

def load_file(file):
    if file.name.endswith(".txt"):
        return file.read().decode("utf-8")

    if file.name.endswith(".pdf"):
        reader = PdfReader(file)
        return "\n".join([p.extract_text() for p in reader.pages])

    if file.name.endswith(".docx"):
        doc = Document(file)
        return "\n".join([p.text for p in doc.paragraphs])

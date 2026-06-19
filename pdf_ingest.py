
from pypdf import PdfReader

pdf_file = "RegsNavyII.pdf"

reader = PdfReader(pdf_file)

text = ""

# PDF Extraction
for page in reader.pages:
    page_text = page.extract_text()

    if page_text:
        text += page_text + "\n"

# Chunking
chunk_size = 500
overlap = 100

chunks = []

for i in range(0, len(text), chunk_size - overlap):

    chunk = text[i:i + chunk_size]

    if len(chunk.strip()) > 50:
        chunks.append(chunk)

print("Pages:", len(reader.pages))
print("Total Chunks:", len(chunks))

print("\nSample Chunk:\n")
print(chunks[0])

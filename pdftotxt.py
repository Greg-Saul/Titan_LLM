from PyPDF2 import PdfReader

reader = PdfReader("Introduction_to_Python_Programming_-_WEB.pdf")
with open("Introduction_to_Python_Programming.txt", "w", encoding="utf-8") as f:
    for page in reader.pages:
        t = page.extract_text()
        if t:
            f.write(t + "\n")
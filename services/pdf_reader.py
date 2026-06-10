import pdfplumber 

def read_pdf(file_path: str) -> str:
    text:str = ""

    try:
        with pdfplumber.open(file_path) as file:
            for page in file.pages:
                if (page := page.extract_text()):
                    text += page + "\n"
    except Exception as error:
        raise ValueError("PDF soubor se nepodařilo přečíst.") from error

    return text

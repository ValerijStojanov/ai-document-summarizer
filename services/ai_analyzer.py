import os
from dotenv import load_dotenv
from openai import OpenAI

model: str = 'gpt-4.1-mini'
instructions: str = """
Analyzuj dokument a odpověz česky.

Vrať výstup v této struktuře:

1. Shrnutí
2. Klíčové body
3. Akční kroky
4. Důležitá data, čísla a termíny

Piš stručně, jasně a profesionálně.
"""

def analyze_document(document_text: str) -> str:

    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Chybí OPENAI_API_KEY v .env souboru.")

    client = OpenAI(
        api_key=api_key,
    )

    try:
        response = client.responses.create(
            model=model,
            instructions=instructions,
            input=document_text,
        )
    except Exception as error:
        raise ValueError("Nepodařilo se získat odpověď z OpenAI.") from error

    analysis_text = response.output_text

    return analysis_text

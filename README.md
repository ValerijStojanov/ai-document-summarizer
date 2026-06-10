# AI Document Summarizer

Jednoduchá Streamlit aplikace pro analýzu PDF dokumentů pomocí OpenAI.

Uživatel nahraje PDF soubor, aplikace z něj vytáhne text a následně vrátí stručnou analýzu v češtině.

## Co aplikace umí

- nahrát PDF soubor
- přečíst text z PDF
- vygenerovat shrnutí a klíčové body
- zobrazit základní chybové hlášky místo pádu aplikace

## Použité technologie

- Python
- Streamlit
- pdfplumber
- OpenAI API

## Spuštění

1. Aktivuj virtuální prostředí.
2. Nastav `OPENAI_API_KEY` do `.env` souboru.
3. Volitelně můžeš nastavit `APP_PIN` do `.env`, pokud chceš aplikaci zamknout PINem.
4. Spusť aplikaci:

```bash
streamlit run app.py
```

Příklad `.env`:

```env
OPENAI_API_KEY=tvuj_klic
APP_PIN=1234
```

## Poznámka

Aplikace funguje nejlépe pro PDF soubory, které obsahují běžný text. Pokud je PDF jen jako obrázek nebo je poškozené, analýza nemusí proběhnout správně.

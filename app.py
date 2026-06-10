
import os
import time

import streamlit as st
from dotenv import load_dotenv
from services.pdf_reader import read_pdf
from services.ai_analyzer import analyze_document


load_dotenv()

app_pin = os.getenv("APP_PIN")
analyze_cooldown_seconds = 15

if "pin_verified" not in st.session_state:
    st.session_state.pin_verified = False

if "last_analysis_at" not in st.session_state:
    st.session_state.last_analysis_at = 0.0

if "is_analyzing" not in st.session_state:
    st.session_state.is_analyzing = False

if "last_analysis_result" not in st.session_state:
    st.session_state.last_analysis_result = ""

if app_pin and not st.session_state.pin_verified:
    st.header("Zabezpečený přístup")
    with st.form("pin_form"):
        entered_pin = st.text_input("Zadej PIN")
        unlock_submitted = st.form_submit_button("Odemknout")

    if unlock_submitted:
        if entered_pin == app_pin:
            st.session_state.pin_verified = True
            st.rerun()
        else:
            st.error("Neplatný PIN.")

    st.stop()

st.header('Analýza PDF souborů')

uploaded_file = st.file_uploader(
     f"Nahraj PDF soubor", accept_multiple_files=False, type="pdf"
)


def main(uploaded_file: object) -> str:
    pdf_file_with_text: str = read_pdf(uploaded_file)

    if not pdf_file_with_text.strip():
        raise ValueError("V PDF se nepodařilo najít žádný text.")

    response: str = analyze_document(pdf_file_with_text)

    return response


if uploaded_file:
    st.write(':green[Soubor nahrán]')

    seconds_since_last_analysis = time.time() - st.session_state.last_analysis_at
    is_cooldown_active = seconds_since_last_analysis < analyze_cooldown_seconds

    if is_cooldown_active:
        remaining_seconds = int(analyze_cooldown_seconds - seconds_since_last_analysis) + 1
        st.info(f"Další analýzu můžeš spustit za {remaining_seconds} s.")

    if st.button(
        'Provést analýzu',
        key='analyze_button',
        disabled=st.session_state.is_analyzing or is_cooldown_active,
    ):
        st.session_state.is_analyzing = True

        try:
            analysis = main(uploaded_file)
            st.session_state.last_analysis_result = analysis
            st.session_state.last_analysis_at = time.time()
        except ValueError as error:
            st.warning(str(error))
        except Exception:
            st.error("Při analýze nastala chyba. Zkus jiný PDF soubor nebo to spusť znovu.")
        finally:
            st.session_state.is_analyzing = False

    if st.session_state.last_analysis_result:
        st.write(st.session_state.last_analysis_result)
else:
    st.write("")

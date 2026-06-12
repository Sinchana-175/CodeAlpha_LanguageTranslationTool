import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Language Translation Tool")

st.title(" Language Translation Tool")
st.write("Translate text between different languages")

languages = {
    "English": "en",
    "Hindi": "hi",
    "Kannada": "kn",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Tamil": "ta",
    "Telugu": "te",
    "Malayalam": "ml"
}

text = st.text_area("Enter Text")

source_lang = st.selectbox(
    "Source Language",
    list(languages.keys())
)

target_lang = st.selectbox(
    "Target Language",
    list(languages.keys())
)

if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:
            translated = GoogleTranslator(
                source=languages[source_lang],
                target=languages[target_lang]
            ).translate(text)

            st.success("Translation Successful")
            st.text_area(
                "Translated Text",
                translated,
                height=150
            )

        except Exception as e:
            st.error(f"Error: {e}")
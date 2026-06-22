import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Language Translator", page_icon="🌐")
st.title("🌐 CodeAlpha - Language Translation Tool")

st.markdown("### Translate text to 100+ languages")

text = st.text_area("Enter text to translate:", "Hello, how are you?")

languages = {
    "Urdu": "ur", "Hindi": "hi", "Arabic": "ar", "French": "fr",
    "Spanish": "es", "German": "de", "Chinese": "zh-cn", 
    "Japanese": "ja", "Korean": "ko", "Turkish": "tr", "Russian": "ru"
}

target_lang = st.selectbox("Select target language:", list(languages.keys()))

if st.button("Translate"):
    if text:
        try:
            translated = GoogleTranslator(source='auto', target=languages[target_lang]).translate(text)
            st.success("Translation:")
            st.write(f"**{translated}**")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter some text")

st.markdown("---")
st.caption("Task 1 - CodeAlpha AI Internship | Built by Kinza Saleem")

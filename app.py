import streamlit as st
from googletrans import Translator

st.set_page_config(page_title="AI Translator - CodeAlpha", page_icon="🌐")

st.title("🌐 Language Translation Tool")
st.caption("CodeAlpha AI Internship - Task 1 | Made by Kinza Saleem")

translator = Translator()

languages = {
    'English': 'en', 'Urdu': 'ur', 'Hindi': 'hi', 'Arabic': 'ar', 
    'French': 'fr', 'Spanish': 'es', 'German': 'de', 'Chinese': 'zh-cn'
}

col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("From:", list(languages.keys()), index=0)
with col2:
    target_lang = st.selectbox("To:", list(languages.keys()), index=1)

text_input = st.text_area("Enter text to translate:", height=150, 
                          placeholder="Type something in English...")

if st.button("Translate", type="primary", use_container_width=True):
    if text_input:
        try:
            with st.spinner("Translating..."):
                result = translator.translate(
                    text_input, 
                    src=languages[source_lang], 
                    dest=languages[target_lang]
                )
            st.success("✅ Translation Complete:")
            st.text_area("Result:", value=result.text, height=150)
            st.code(result.text, language=None)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("⚠️ Please enter text first")

st.markdown("---")
st.markdown("**CodeAlpha Artificial Intelligence Internship | Task 1**")

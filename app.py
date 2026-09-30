import streamlit as st
import pandas as pd
from gtts import gTTS
import io
st.set_page_config(page_title="KarzaFree Bot", page_icon="🌾")
def bolo(text, lang):
    try:
        tts=gTTS(text=text, lang=lang, slow=False)
        mp3=io.BytesIO()
        tts.write_to_fp(mp3)
        mp3.seek(0)
        st.audio(mp3, format="audio/mp3")
    except:
        st.warning("Voice loading...")
st.title("🌾 KarzaFree - Bada Bhai")
st.success("Tension mat le, main hu na! 💚")
lang = st.sidebar.selectbox("Bhasha Chun", ["hi","mr","pa","gu","bn","ta","te","en"])
if st.sidebar.button("🔊 Bhai ko Suna"):
    bolo("Tension mat le bhai, main hu na!", lang)
karza = st.number_input("Kul Karza (₹)", value=50000)
income = st.number_input("Fasal/Aay (₹)", value=80000)
mahine = st.slider("Mahine", 1, 12, 6)
if st.button("Plan Bana Bhai", type="primary"):
    kisht=karza/mahine
    st.balloons()
    st.success(f"Har mahine ₹{kisht:.0f} dena hai")
    bolo(f"Har mahine {int(kisht)} rupaye dena hai", lang)
    df=pd.DataFrame([{"Mahina":f"M{i}", "Dena":f"₹{kisht:.0f}"} for i in range(1,mahine+1)])
    st.table(df)

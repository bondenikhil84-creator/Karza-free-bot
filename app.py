import streamlit as st
import pandas as pd
from gtts import gTTS
import io

st.set_page_config(page_title="KarzaFree V5 PRO", page_icon="🌾")

# PRO Messages - Har bhasha ka apna message
MSG = {
 "hi": "Tension mat le bhai, main hu na! Tera karza khatam karne ka zimma mera hai!",
 "mr": "Tension gheu nako bhava, mi aahe na! Tuza karza sampavnyachi jababdari majhi aahe!",
 "pa": "Tension na le veer, main haan na! Tera karza khatam karan di zimmevari meri hai!",
 "gu": "Chinta na kar bhai, hu chu ne! Taru karza khatam karvani javabdari mari che!",
 "bn": "Chinta koris na bhai, ami achi! Tor rin sesh korar daitto amar!",
 "ta": "Kavalaipada bhai, naan irukken! Un kadanai mudikka poruppu enathu!",
 "te": "Chinta padaku bhai, nenu unnanu! Nee appu teerchadam naa badhyata!",
 "en": "Don't worry brother, I am here! Your debt free journey starts now!"
}

def bolo(text, lang):
    try:
        tts=gTTS(text=text, lang=lang, slow=False, lang_check=False)
        mp3=io.BytesIO()
        tts.write_to_fp(mp3)
        mp3.seek(0)
        st.audio(mp3, format="audio/mp3", autoplay=True)
    except Exception as e:
        st.error(f"Voice error: {e}")

st.title("🌾 KarzaFree V5 - PRO Bada Bhai")

st.sidebar.header("🌍 Bhasha Chun")
lang_code = st.sidebar.selectbox("Bhasha / Language:", list(MSG.keys()), format_func=lambda x: {"hi":"हिंदी","mr":"मराठी","pa":"ਪੰਜਾਬੀ","gu":"ગુજરાતી","bn":"বাংলা","ta":"தமிழ்","te":"తెలుగు","en":"English"}[x])

if st.sidebar.button("🔊 Bhai ko Suna - PRO Voice"):
    bolo(MSG[lang_code], lang_code)

st.success(MSG[lang_code])

karza = st.number_input("Kul Karza (₹)", value=50000)
income = st.number_input("Fasal/Aay (₹)", value=80000)
mahine = st.slider("Kitne Mahine me khatam?", 1, 12, 6)

if st.button("🚀 90 Din Ka PRO Plan Bana", type="primary"):
    kisht=karza/mahine
    st.balloons()
    st.metric("Har Mahine Dena Hai", f"₹{kisht:,.0f}")
    bolo(f"{lang_code} bhasha me plan taiyaar hai! Har mahine {int(kisht)} rupaye dena hai. {MSG[lang_code]}", lang_code)
    df=pd.DataFrame([{"Mahina":f"Month {i}", "Dena Hai":f"₹{kisht:.0f}", "Status":"Plan Ready"} for i in range(1,mahine+1)])
    st.table(df)
    st.download_button("📥 Plan Download Kar", df.to_csv(index=False), "karza_plan.csv")

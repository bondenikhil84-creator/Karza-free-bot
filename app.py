import streamlit as st
import pandas as pd
import asyncio
import edge_tts
import io

st.set_page_config(page_title="KarzaFree V6 GENTS", page_icon="💪")

VOICE = {
 "hi": "hi-IN-MadhurNeural",
 "mr": "mr-IN-ManoharNeural",
 "pa": "en-IN-PrabhatNeural",
 "en": "en-IN-PrabhatNeural"
}

MSG = {
 "hi": "Tension mat le bhai, main Madhur bol raha hu! Tera karza khatam karne ka zimma mera hai!",
 "mr": "Tension gheu nako bhava, mi boltoy! Tuza karza sampavnyachi jababdari majhi!",
 "pa": "Tension na le veer, main haan na!",
 "en": "Don't worry brother, I am here! Your debt free plan is ready!"
}

async def make_audio(text, voice_id):
    comm = edge_tts.Communicate(text, voice_id, rate="+15%")
    data = b""
    async for chunk in comm.stream():
        if chunk["type"] == "audio":
            data += chunk["data"]
    return data

def bolo(text, lang):
    vid = VOICE.get(lang, "hi-IN-MadhurNeural")
    try:
        with st.spinner("💪 Gents Bhai bol raha hai..."):
            audio = asyncio.run(make_audio(text, vid))
            st.audio(audio, format="audio/mp3", autoplay=True)
    except Exception as e:
        st.error(f"Error: {e}")

st.title("💪 KarzaFree V6 - GENTS Voice")

lang = st.sidebar.selectbox("Bhasha Chun:", ["hi","mr","pa","en"], format_func=lambda x: {"hi":"हिंदी - Madhur (Gents)","mr":"मराठी","pa":"ਪੰਜਾਬੀ","en":"English - Prabhat"}[x])

if st.sidebar.button("🔊 GENTS Bhai ko Suna"):
    bolo(MSG.get(lang, MSG["hi"]), lang)

st.success(MSG.get(lang, MSG["hi"]))

karza = st.number_input("Kul Karza (₹)", value=50000)
mahine = st.slider("Kitne Mahine?", 1, 12, 6)

if st.button("🚀 Plan Bana Bhai", type="primary"):
    kisht = karza / mahine
    st.balloons()
    st.metric("Har Mahine Dena Hai", f"₹{kisht:,.0f}")
    bolo(f"Plan taiyaar hai bhai! Har mahine {int(kisht)} rupaye dena hai. Tension mat le!", lang)
    df = pd.DataFrame([{"Mahina": i, "Kisht": int(kisht)} for i in range(1, mahine+1)])
    st.table(df)

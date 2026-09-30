import streamlit as st
import pandas as pd

st.set_page_config(page_title="KarzaFree - Bada Bhai", page_icon="🌾", layout="centered")

LANGUAGES = {"Hindi":"हिंदी","Marathi":"मराठी","Punjabi":"ਪੰਜਾਬੀ","Bhojpuri":"भोजपुरी","Haryanvi":"हरयाणवी","Gujarati":"ગુજરાતી","Bengali":"বাংলা","Tamil":"தமிழ்","Telugu":"తెలుగు","Kannada":"ಕನ್ನಡ","Malayalam":"മലയാളം","Odia":"ଓଡ଼ିଆ","Assamese":"অসমীয়া","Rajasthani":"राजस्थानी","Urdu":"اردو","English":"English"}

st.title("🌾 KarzaFree - Tera Bada Bhai")
st.success("Tension mat le bhai, main hu na! 💚 Tera karza khatam karne ka zimma ab mera hai.")

with st.sidebar:
    st.header("🌍 Bhasha Chun Bhai")
    selected_lang = st.selectbox("Apni Bhasha Chun:", list(LANGUAGES.keys()))
    st.info(f"Tera bhai {LANGUAGES[selected_lang]} me baat karega!")

tab1, tab2 = st.tabs(["👨‍🌾 Bada Bhai Kisan Mode", "💼 Bada Bhai Naukri Mode"])

with tab1:
    st.subheader("👨‍🌾 Bada Bhai Kisan Mode")
    total_karza = st.number_input("Kul Karza Kitna Hai? (₹)", value=50000, step=5000)
    fasal_income = st.number_input("Agli Fasal se kitni kamai hogi? (₹)", value=80000, step=5000)
    mahine = st.slider("Kitne mahine me khatam karna hai?", 1, 12, 6)
    if st.button("🚀 Mera 90 Din Ka Plan Bana Bhai", type="primary"):
        st.balloons()
        kisht = total_karza / mahine
        st.success(f"Bhai, har mahine ₹{kisht:,.0f} nikalna hai. Fasal bikte hi pehle karza khatam!")
        plan = []
        for i in range(1, mahine+1):
            plan.append({"Mahina": f"Mahina {i}", "Dena Hai": f"₹{kisht:,.0f}", "Tip": "Fasal ka 30% pehle karze ko de de!"})
        st.table(pd.DataFrame(plan))

with tab2:
    st.subheader("💼 Bada Bhai Naukri Mode")
    salary = st.number_input("Mahine ki Pagar?", value=25000, step=2000)
    karza2 = st.number_input("Kul Karza?", value=50000, step=5000, key="k2")
    if st.button("Mera Plan Bana"):
        st.info(f"Roz ka ₹{karza2/90:.0f} bacha le, 90 din me free!")

st.caption("Made with ❤️ by Nikhil Bondre | Tera Bada Bhai hamesha tere saath hai")

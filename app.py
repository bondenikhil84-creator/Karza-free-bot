import streamlit as st

st.set_page_config(page_title="Karza Free Bot V2", page_icon="💰")

st.title("💰 Karza-Free-Bot V2")
st.subheader("Tera Karza Mukti Saathi - Kisan Mode")

st.write("---")

mode = st.radio("Tu kaunsa mode chaahta hai?", ["Normal Naukri Wala", "🌾 Kisan Bhai Mode"])

karza = st.number_input("Tera total karza kitna hai? (Rs)", min_value=0, value=50000)
mahine = st.slider("Kitne mahine me khatam karna hai?", 1, 60, 12)
income = st.number_input("Mahine ki kamai kitni hai? (Rs)", min_value=0, value=20000)

if mode == "🌾 Kisan Bhai Mode":
    fasal_income = st.number_input("Fasal se extra income (saal ki)", value=0)
    st.info(f"Kisan Bhai, {fasal_income} ko 12 se divide karke jod denge")

if st.button("Plan Banao"):
    if karza == 0:
        st.success("Wah! Tu toh pehle se hi Karza-Free hai! 🎉")
    else:
        mahina_kist = karza / mahine
        
        if mode == "🌾 Kisan Bhai Mode":
            total_monthly = income + (fasal_income/12)
        else:
            total_monthly = income
            
        bacha = total_monthly - mahina_kist
        
        st.write("---")
        st.metric("Har Mahine Dena Hoga", f"Rs {mahina_kist:.0f}")
        st.metric("Teri Bachi Kamai", f"Rs {bacha:.0f}")

        if bacha < 0:
            st.error("Bhai thoda time badha de, nahi toh ghar kaise chalega?")
        elif bacha < 5000:
            st.warning("Thoda tight hai, par ho jayega! Himmat rakh.")
        else:
            st.success("Solid Plan Hai! Tu Karza-Free ho jayega! 🚀")
            st.balloons()

st.write("---")
st.caption("Made with ❤️ for Bharat")

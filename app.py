import streamlit as st

st.set_page_config(page_title="Karza Free Helper", page_icon="💰")

st.title("💰 Karza-Free-Bot")
st.subheader("Tera Karza Mukti Saathi")

st.write("---")

karza = st.number_input("Tera total karza kitna hai? (₹ me)", min_value=0, value=50000)
mahine = st.slider("Kitne mahine me khatam karna hai?", 1, 60, 12)
income = st.number_input("Mahine ki kamai kitni hai? (₹ me)", min_value=0, value=20000)

if st.button("Plan Banao"):
    if karza == 0:
        st.success("Wah! Tu toh pehle se hi Karza-Free hai! 🎉")
    else:
        mahine_ka_bhugtan = karza / mahine
        bacha_hua = income - mahine_ka_bhugtan
        
        st.write("---")
        st.metric("Har mahine dena hai", f"₹ {mahine_ka_bhugtan:.0f}")
        
        if bacha_hua < 0:
            st.error(f"⚠️ Dhyaan de: Is plan se tere paas ₹ {bacha_hua:.0f} kam padega. Ya to mahine badha, ya kamai badha.")
        else:
            st.success(f"✅ Super! Bhugtan ke baad bhi tere paas ₹ {bacha_hua:.0f} bachega.")
        
        st.info(f"Tip: Roz ₹ {mahine_ka_bhugtan/30:.0f} alag nikal ke rakh. Karza jaldi khatam!")

st.write("---")
st.caption("Banaya hai bondenikhil84-creator ne ❤️")

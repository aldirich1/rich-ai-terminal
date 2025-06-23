
import streamlit as st
import datetime

st.set_page_config(page_title="Rich AI Terminal", layout="wide", page_icon="📊")

# ---------------------- HEADER ----------------------
st.markdown("<h1 style='text-align: center;'>Rich AI Terminal</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Analyze. Execute. Dominate.</h4>", unsafe_allow_html=True)
st.markdown("---")

# ---------------------- RUNNING TIME ----------------------
now = datetime.datetime.utcnow()
wib = now + datetime.timedelta(hours=7)
ny = now - datetime.timedelta(hours=4)
sydney = now + datetime.timedelta(hours=10)
col1, col2, col3 = st.columns(3)
with col1:
    st.success(f"🇮🇩 Jakarta: {wib.strftime('%H:%M:%S')}")
with col2:
    st.info(f"🇺🇸 New York: {ny.strftime('%H:%M:%S')}")
with col3:
    st.warning(f"🇦🇺 Sydney: {sydney.strftime('%H:%M:%S')}")

# ---------------------- LIVE CHART ----------------------
st.subheader("📈 Live Chart")
chart_html = '''
<iframe src="https://s.tradingview.com/widgetembed/?frameElementId=tradingview_xx&symbol=OANDA:XAUUSD&interval=15&hidesidetoolbar=1&symboledit=1&saveimage=1&toolbarbg=F1F3F6&studies=[]&theme=dark&style=1&timezone=Etc%2FUTC&studies_overrides={}" width="100%" height="500" frameborder="0"></iframe>
'''
st.components.v1.html(chart_html, height=500)

# ---------------------- AI ASSISTANT ----------------------
st.subheader("🧠 Rich AI Assistant")
with st.chat_message("assistant"):
    st.markdown("Halo Rivaldi! Siap bantu analisa. Mau pakai strategi SMC, Elliott Wave, atau Fibonacci hari ini?")

# ---------------------- NEWS & ALERT ----------------------
st.subheader("📢 News & Alerts")
st.warning("🔴 15 menit lagi: High Impact News (NFP). Jangan bar-bar mau moment!")

# ---------------------- SYSTEM STATUS ----------------------
st.markdown("---")
st.markdown("✅ Online • 📶 Feed: Aktif • ⏱️ Delay: 0.2s")

# ---------------------- TRADE SIGNAL ----------------------
st.subheader("📊 Trade Suggestion (XAU/USD)")
st.info("Rekomendasi: BUY di 2320, SL: 2310, TP1: 2345, TP2: 2370 | Timeframe: H1")

st.caption("Versi lengkap pertama Rich AI Terminal © 2025")

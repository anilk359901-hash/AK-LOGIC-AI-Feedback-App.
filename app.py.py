import streamlit as st
from streamlit_drawable_canvas import st_canvas
from datetime import datetime

# ऐप का टाइटल और लोगो
st.set_page_config(page_title="AK-LOGIC AI Feedback", page_icon="🚖")

st.title("🚖 AK-LOGIC AI: Customer Feedback")
st.write("आपका फीडबैक हमें बेहतर बनाने में मदद करेगा!")

# इनपुट फील्ड्स
name = st.text_input("ग्राहक का नाम:")
vehicle = st.selectbox("गाड़ी का प्रकार:", ["Auto-Rickshaw", "BMW", "Mercedes", "Audi", "Other"])
rating = st.slider("हमें रेटिंग दें (1-5):", 1, 5, 5)
comments = st.text_area("आपका संदेश:")

# रेटिंग स्टार्स में दिखाएँ
st.write(f"आपकी रेटिंग: {'⭐' * rating} ({rating}/5)")

# डिजिटल सिग्नेचर
st.write("डिजिटल सिग्नेचर यहाँ करें:")
canvas_result = st_canvas(
    stroke_width=2,
    stroke_color="#000000",
    background_color="#eeeeee",
    height=150,
    drawing_mode="freedraw",
    key="canvas",
)

# सबमिट और क्लियर बटन
col1, col2 = st.columns(2)

with col1:
    submit = st.button("✅ Submit Feedback", type="primary")

with col2:
    clear = st.button("🔄 Clear Form")

if submit:
    if not name.strip():
        st.warning("कृपया अपना नाम दर्ज करें!")
    else:
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        st.success(f"धन्यवाद {name}! आपका फीडबैक सुरक्षित कर लिया गया है।")

        # फीडबैक सारांश दिखाएँ
        st.subheader("📋 फीडबैक सारांश")
        st.write(f"**नाम:** {name}")
        st.write(f"**गाड़ी का प्रकार:** {vehicle}")
        st.write(f"**रेटिंग:** {'⭐' * rating} ({rating}/5)")
        st.write(f"**संदेश:** {comments if comments.strip() else 'कोई संदेश नहीं'}")
        st.write(f"**दिनांक और समय:** {timestamp}")
        st.write(f"**सिग्नेचर:** ✅ दर्ज किया गया")

if clear:
    st.rerun()

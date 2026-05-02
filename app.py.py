import streamlit as st
from streamlit_drawable_canvas import st_canvas

# ऐप का टाइटल और लोगो
st.set_page_config(page_title="AK-LOGIC AI Feedback", page_icon="🚖")
st.title("🚖 AK-LOGIC AI: Customer Feedback")
st.write("आपका फीडबैक हमें बेहतर बनाने में मदद करेगा!")

# इनपुट फील्ड्स
name = st.text_input("ग्राहक का नाम:")
vehicle = st.selectbox("गाड़ी का प्रकार:", ["Auto-Rickshaw", "BMW", "Mercedes", "Audi", "Other"])
rating = st.slider("हमें रेटिंग दें (1-5):", 1, 5, 5)
comments = st.text_area("आपका संदेश:")

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

# सबमिट बटन
if st.button("Submit Feedback"):
    st.success(f"धन्यवाद {name}! आपका फीडबैक सुरक्षित कर लिया गया है।")
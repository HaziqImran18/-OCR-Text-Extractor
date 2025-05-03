import streamlit as st
from PIL import Image
import pytesseract
import io
import requests
import base64
import os
from dotenv import load_dotenv

load_dotenv()
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

API_KEY = os.getenv("GROQ_API_KEY")
GROQ_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"

# Streamlit UI config
st.set_page_config(page_title="OCR with Tesseract + Groq", layout="wide")
st.sidebar.title("📤 Upload Image for OCR")

st.sidebar.header("Upload Image")
uploaded_file = st.sidebar.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.sidebar.image(image, caption="Uploaded Image", use_column_width=True)

    st.markdown("### 🧠 Extracted Text (via Tesseract)")
    extracted_text = pytesseract.image_to_string(image)
    st.text_area("📄 Raw Text", extracted_text, height=300)

    st.download_button("💾 Download Raw Text", extracted_text, file_name="raw_text.txt")

    if st.button("🚀 Summarize or Format with Groq"):
        with st.spinner("Sending to Groq..."):
            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            }

            prompt = f"""Here is raw OCR text from an image. Clean it up, correct any errors, and present it in well-formatted Markdown:\n\n{extracted_text}"""

            payload = {
                "model": "llama-3.1-8b-instant",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.3
            }

            try:
                res = requests.post(GROQ_ENDPOINT, headers=headers, json=payload)
                if res.status_code == 200:
                    result_text = res.json()['choices'][0]['message']['content']
                    st.success("✅ Successfully formatted with Groq!")
                    st.markdown(result_text)
                    st.download_button("💾 Download Formatted Text", result_text, file_name="formatted_text.md")
                else:
                    st.error("❌ Groq failed. Response below:")
                    st.json(res.json())
            except Exception as e:
                st.error(f"⚠️ Error: {e}")

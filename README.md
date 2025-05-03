# 🧠 OCR Text Extractor with Groq & Streamlit

## A production-grade Optical Character Recognition (OCR) app powered by [Groq](https://groq.com/) and [Streamlit](https://streamlit.io/). Upload any image and extract clean, readable text using AI.

### 🧠 Project Overview
This application leverages Groq's blazing-fast LLMs alongside OpenAI Whisper and Tesseract OCR to extract text from uploaded images directly in your browser. Built with Streamlit, it offers a clean and interactive UI, allowing users to:

📤 Upload .jpg, .jpeg, or .png images

🖼️ View the image in-app

🧾 Extract all readable text using **pytesseract**

📑 Summarize & Format the raw text using Groq API for llama-3.1-8b-instant LLM

💾 Download the extracted content as a .txt file

⚙️ Automatically fallback to Tesseract OCR if needed

This makes it a powerful tool for students, researchers, and developers working with scanned documents, receipts, notes, or visual data.

---

## 📸 Demo Preview

> Upload an image (JPG/PNG), click **"Extract Text"**, and get perfectly extracted content.

![Screenshot (368)](https://github.com/user-attachments/assets/cf33d375-5890-4503-a5a7-394aafdd5125)

![Screenshot (369)](https://github.com/user-attachments/assets/3d1c97c0-dbe1-4b34-b2b2-8d338f2c9b6b)

![Screenshot (370)](https://github.com/user-attachments/assets/ad6c27c4-0d9e-461e-966f-05cadecfc5d7)


## 🚀 Features

- ✅ Upload image files (JPG, JPEG, PNG)
- ✅ Uses **Groq’s LLaMA 3.1 8B Instant** multimodal model
- ✅ Clean Markdown output
- ✅ Download extracted text
- ✅ Sidebar image display
- ✅ Deployed with **Streamlit**

---

## 🧰 Technologies Used

| Tool        | Purpose                        |
|-------------|--------------------------------|
| Streamlit   | Web UI                         |
| Groq API    | For formating & Summarizing    |
| Pillow      | Image processing               |
| Tesseract   | For extracting text            |
| Python-dotenv | Secure API key loading       |

---

## 📥 Installation & Setup (Windows)

### 1. Clone the repo

### 2. Create virtual environment
python -m venv OCR
OCR\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Set your Groq API Key
Create a .env file:
GROQ_API_KEY=your_actual_groq_api_key_here

### 5. Download & Install Tesseract OCR
🔗 Download Tesseract OCR for Windows (UB Mannheim Build)

📁 Typical install path:
C:\Program Files\Tesseract-OCR\tesseract.exe

### 6. Run the App
streamlit run app.py

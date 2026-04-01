import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# ==============================
# 🔑 API CONFIG
# ==============================
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

# ==============================
# ⚙️ PAGE SETTINGS
# ==============================
st.set_page_config(page_title="AI Code Debugger", layout="wide")

st.title("🧠 AI Code Debugger & Explainer (Gemini AI)")

# ==============================
# 🎛 SIDEBAR SETTINGS
# ==============================
st.sidebar.title("⚙️ Settings")
temperature = st.sidebar.slider("Creativity", 0.0, 1.0, 0.3)

# ==============================
# 📂 FILE UPLOAD
# ==============================
uploaded_file = st.file_uploader("📂 Upload Code File", type=["py", "txt", "csv", "pdf"])

def read_file(file):
    try:
        return file.read().decode("utf-8", errors="ignore")
    except:
        return "⚠️ Unable to read file properly."

code_input = ""

if uploaded_file:
    code_input = read_file(uploaded_file)
else:
    code_input = st.text_area("✍️ Paste your code here:", height=300)

# Show code nicely
if code_input:
    st.code(code_input, language="python")

# ==============================
# ⚡ FUNCTION TO CALL GEMINI
# ==============================
def ask_ai(prompt):
    try:
        with st.spinner("⏳ Processing..."):
            response = model.generate_content(
                prompt,
                generation_config={"temperature": temperature}
            )
            return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}"

# ==============================
# 🎯 BUTTONS SECTION
# ==============================
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

# ==============================
# 🔍 DEBUG
# ==============================
if col1.button("🔍 Debug Code"):
    if code_input:
        prompt = f"""
        Analyze this code:
        {code_input}

        Give:
        1. Errors
        2. Reasons
        3. Fix
        4. Corrected Code
        """
        result = ask_ai(prompt)
        st.subheader("🛠 Debugging Result")
        st.write(result)

# ==============================
# 💡 EXPLAIN
# ==============================
if col2.button("💡 Explain Code"):
    if code_input:
        prompt = f"Explain this code step by step in simple English:\n{code_input}"
        result = ask_ai(prompt)
        st.subheader("📘 Explanation")
        st.write(result)

# ==============================
# ⚡ OPTIMIZE
# ==============================
if col3.button("⚡ Optimize Code"):
    if code_input:
        prompt = f"""
        Optimize this code:
        {code_input}

        Give improved version + explanation
        """
        result = ask_ai(prompt)
        st.subheader("🚀 Optimized Code")
        st.write(result)

# ==============================
# 🔐 SECURITY CHECK
# ==============================
if col4.button("🔐 Security Check"):
    if code_input:
        prompt = f"""
        Check this code for security issues:
        {code_input}

        Give vulnerabilities + fixes
        """
        result = ask_ai(prompt)
        st.subheader("🔐 Security Report")
        st.write(result)

# ==============================
# 🧪 TEST CASES
# ==============================
if col5.button("🧪 Generate Tests"):
    if code_input:
        prompt = f"""
        Generate pytest test cases for this code:
        {code_input}
        """
        result = ask_ai(prompt)
        st.subheader("🧪 Test Cases")
        st.write(result)

# ==============================
# 🔄 CODE CONVERTER
# ==============================
lang = st.selectbox("🌐 Convert Code To:", ["None", "Python", "Java", "C++", "JavaScript"])

if col6.button("🔄 Convert Code"):
    if code_input and lang != "None":
        prompt = f"Convert this code to {lang}:\n{code_input}"
        result = ask_ai(prompt)
        st.subheader("🔄 Converted Code")
        st.write(result)

# ==============================
# 💬 CHAT MODE
# ==============================
st.subheader("💬 Ask Questions About Code")
user_question = st.text_input("Ask anything...")

if st.button("Ask AI"):
    if code_input and user_question:
        prompt = f"""
        Code:
        {code_input}

        Question:
        {user_question}
        """
        result = ask_ai(prompt)
        st.write(result)

# ==============================
# 📥 DOWNLOAD RESULT
# ==============================
if 'result' in locals():
    st.download_button(
        label="📥 Download Result",
        data=result,
        file_name="ai_code_report.txt",
        mime="text/plain"
    )
import google.generativeai as genai

model = genai.GenerativeModel("gemini-2.5-flash")

def ask_ai(prompt, temperature=0.3):
    try:
        response = model.generate_content(
            prompt,
            generation_config={"temperature": temperature}
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
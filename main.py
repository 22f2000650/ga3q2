from fastapi import FastAPI, HTTPException
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

@app.get("/")
def home():
    return {"message": "API is working 🚀"}

@app.post("/comment")
async def generate_comment(data: dict):
    try:
        text = data.get("text")

        if not text:
            raise HTTPException(status_code=400, detail="Text is required")

        response = model.generate_content(
            f"Write a short professional comment about: {text}"
        )

        return {
            "comment": response.text
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
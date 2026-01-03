import os
import json
from fastapi import FastAPI, UploadFile, File, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import google.generativeai as genai
from dotenv import load_dotenv

import models, schemas, database

# 1. Load Environment Variables (Security Best Practice)
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("CRITICAL WARNING: API Key not found in .env file!")

# 2. Configure Gemini AI
genai.configure(api_key=API_KEY)
# We use 'gemini-1.5-flash' because it's fast and cheap for receipts
model = genai.GenerativeModel('gemini-2.5-flash-preview-09-2025')

# 3. Database Setup
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="SnapSpend Backend")

# This tells the server: "It is safe to accept requests from any website"
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (Safe for development)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (POST, GET, etc.)
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"status": "active", "message": "SnapSpend Backend v2 (Python) is Live"}

@app.post("/scan/", response_model=schemas.Expense)
async def scan_receipt(file: UploadFile = File(...), db: Session = Depends(get_db)):
    
    # A. Read the image file
    content = await file.read()
    
    # B. Define the Prompt (The same logic you used in JS)
    prompt = """
    Analyze this receipt. Extract the following fields in JSON format:
    - merchant (string)
    - date (YYYY-MM-DD)
    - amount (float)
    - currency (symbol)
    - category (one of: Food, Transport, Shopping, Utilities, Health, Other)
    
    Return ONLY raw JSON. No markdown.
    """

    try:
        # C. Call Gemini API
        # We pass the raw bytes directly to the model
        response = model.generate_content([
            {'mime_type': file.content_type, 'data': content},
            prompt
        ])
        
        # D. Clean the response (Remove markdown ```json ... ``` if present)
        raw_text = response.text
        clean_json = raw_text.replace("```json", "").replace("```", "").strip()
        
        data = json.loads(clean_json)
        
        # E. Save to SQL Database (The "Full Stack" Part)
        db_expense = models.Expense(
            merchant=data.get("merchant", "Unknown"),
            amount=data.get("amount", 0.0),
            currency=data.get("currency", "₹"),
            category=data.get("category", "Other"),
            date=data.get("date", ""),
            ai_raw_summary=raw_text[:500] # Save a snippet for debugging
        )
        
        db.add(db_expense)
        db.commit()
        db.refresh(db_expense)
        
        return db_expense

    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

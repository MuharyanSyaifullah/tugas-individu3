# backend/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from database import engine, SessionLocal, Base
from models import Feedback
from schemas import FeedbackInput, FeedbackResponse
from services.sentiment import analyze_sentiment_text
from services.keypoints import generate_pros_cons

# Buat tabel otomatis
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Feedback Insight API")

# Setup CORS agar frontend bisa akses
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Bisa diubah ke URL frontend spesifik saat production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/v1/submit", response_model=FeedbackResponse)
async def submit_feedback_endpoint(data: FeedbackInput, db: Session = Depends(get_db)):
    # 1. Analisis Sentimen
    sentiment = await analyze_sentiment_text(data.content)
    
    # 2. Ekstraksi Pros & Cons via Gemini
    analysis = generate_pros_cons(data.content)
    
    # 3. Simpan ke Database
    new_entry = Feedback(
        content=data.content,
        sentiment_label=sentiment,
        analysis_result=analysis
    )
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    
    return new_entry

@app.get("/api/v1/history", response_model=list[FeedbackResponse])
def get_history_endpoint(db: Session = Depends(get_db)):
    # Ambil data urut dari yang terbaru
    return db.query(Feedback).order_by(Feedback.id.desc()).all()
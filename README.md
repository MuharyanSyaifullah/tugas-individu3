# ✨ Smart Feedback Insight

Aplikasi analisis ulasan produk cerdas yang menggunakan **Hugging Face** untuk deteksi sentimen dan **Google Gemini AI** untuk mengekstrak kelebihan dan kekurangan produk secara otomatis.

## 🚀 Fitur Utama
- **Analisis Sentimen Otomatis**: Mendeteksi apakah ulasan bersifat Positif, Negatif, atau Netral.
- **AI Pros & Cons Extraction**: Menggunakan Generative AI untuk merangkum poin plus dan minus produk.
- **Dark Mode UI**: Antarmuka modern yang nyaman di mata.
- **Database History**: Semua hasil analisis tersimpan otomatis (PostgreSQL/SQLite).

## 🛠 Teknologi
- **Backend**: FastAPI, SQLAlchemy, Google Gemini API, Hugging Face Inference.
- **Frontend**: React JS, Vite, CSS Modules (Custom Dark Theme).
- **Database**: PostgreSQL.

## 📦 Cara Menjalankan

### Backend
1. Masuk folder `backend`.
2. Buat file `.env` dan isi `DATABASE_URL`, `HF_API_KEY`, dan `GEMINI_API_KEY`.
3. Install dependencies: `pip install -r requirements.txt`.
4. Jalankan: `uvicorn main:app --reload`.

### Frontend
1. Masuk folder `frontend`.
2. Install dependencies: `npm install`.
3. Jalankan: `npm run dev`.

---
**Tugas Individu 3** Nama: Muharyan Syaifullah 
NIM: 123140045
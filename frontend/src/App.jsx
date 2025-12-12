// frontend/src/App.jsx
import React, { useState, useEffect } from "react";
import axios from "axios";
import "./styles.css";

const API_BASE = "http://localhost:8000/api/v1";

function App() {
  const [inputContent, setInputContent] = useState("");
  const [feedbacks, setFeedbacks] = useState([]);
  const [loading, setLoading] = useState(false);

  // Load data saat pertama kali buka
  useEffect(() => {
    fetchHistory();
  }, []);

  const fetchHistory = async () => {
    try {
      const res = await axios.get(`${API_BASE}/history`);
      setFeedbacks(res.data);
    } catch (error) {
      console.error("Gagal mengambil data history:", error);
    }
  };

  const handleAnalyze = async (e) => {
    e.preventDefault();
    if (!inputContent.trim()) return;

    setLoading(true);
    try {
      // Kirim ke backend
      const res = await axios.post(`${API_BASE}/submit`, {
        content: inputContent
      });
      
      // Tambahkan hasil baru ke paling atas list
      setFeedbacks([res.data, ...feedbacks]);
      setInputContent(""); // Reset form
    } catch (error) {
      alert("Terjadi kesalahan saat analisis. Cek koneksi backend.");
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  // Helper untuk menentukan warna border card berdasarkan sentimen
  const getBorderColor = (sentiment) => {
    if (sentiment === "positive") return "#10b981";
    if (sentiment === "negative") return "#ef4444";
    return "#64748b";
  };

  return (
    <div className="app-wrapper">
      <header>
        <h1>✨ Smart Feedback Insight</h1>
        <p>Analisis sentimen & poin kunci ulasan produk berbasis AI</p>
      </header>

      <section className="input-card">
        <form onSubmit={handleAnalyze}>
          <textarea
            placeholder="Masukkan ulasan pelanggan di sini..."
            value={inputContent}
            onChange={(e) => setInputContent(e.target.value)}
            disabled={loading}
          />
          <button type="submit" className="analyze-btn" disabled={loading}>
            {loading ? "Sedang Menganalisis..." : "🚀 Analisis Sekarang"}
          </button>
        </form>
      </section>

      <div className="feed-label">Riwayat Analisis</div>

      <div className="results-feed">
        {feedbacks.map((item) => (
          <article 
            key={item.id} 
            className="feedback-card"
            style={{ borderLeftColor: getBorderColor(item.sentiment_label) }}
          >
            <div className="card-header">
              <span className={`badge sentiment-${item.sentiment_label || 'neutral'}`}>
                {item.sentiment_label || 'Unknown'}
              </span>
              <span className="timestamp">
                #{item.id} • {new Date(item.created_at).toLocaleDateString()}
              </span>
            </div>

            <div className="content-text">
              "{item.content}"
            </div>

            {item.analysis_result && (
              <div className="analysis-box">
                <h4>🤖 AI Analysis (Pros & Cons)</h4>
                <div className="analysis-content">
                  {item.analysis_result}
                </div>
              </div>
            )}
          </article>
        ))}
      </div>
    </div>
  );
}

export default App;
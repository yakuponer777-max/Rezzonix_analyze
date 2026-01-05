from flask import Flask, render_template_string, request, redirect, url_for
import math

app = Flask(__name__)

# -------------------------------
# ÖRNEK FREKANS & HASTALIK VERİLERİ
# -------------------------------
FREQUENCIES = {
    "Baş Ağrısı": [7.83, 10.5, 14.1],
    "Mide Problemleri": [3.5, 5.2, 8.0],
    "Uyku Bozukluğu": [1.2, 2.4, 6.3],
    "Stres & Anksiyete": [6.8, 9.1, 12.0],
    "Bağışıklık Zayıflığı": [15.5, 18.2, 21.0]
}

# -------------------------------
# ANA SAYFA
# -------------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    selected = None

    if request.method == "POST":
        selected = request.form.get("problem")
        result = FREQUENCIES.get(selected)

    html = """
    <html>
    <head>
        <title>Rezzonix Analyzer</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { font-family: Arial; background:#f5f7fa; padding:20px; }
            .card { background:white; padding:20px; border-radius:10px; max-width:600px; margin:auto; }
            h1 { text-align:center; }
            select, button { width:100%; padding:12px; margin-top:10px; font-size:16px; }
            .result { margin-top:20px; background:#eef; padding:15px; border-radius:8px; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🔬 Rezzonix Sağlık Analyzer</h1>
            <form method="post">
                <label>Analiz edilecek durumu seçin:</label>
                <select name="problem" required>
                    <option value="">Seçiniz</option>
                    {% for p in problems %}
                    <option value="{{p}}" {% if p==selected %}selected{% endif %}>{{p}}</option>
                    {% endfor %}
                </select>
                <button type="submit">Analizi Başlat</button>
            </form>

            {% if result %}
            <div class="result">
                <h3>📊 Önerilen Frekanslar</h3>
                <ul>
                    {% for f in result %}
                    <li>{{f}} Hz</li>
                    {% endfor %}
                </ul>
                <p><b>Uygulama Önerisi:</b> Frekanslar günde 15–20 dk, sakin ortamda uygulanmalıdır.</p>
            </div>
            {% endif %}
        </div>
    </body>
    </html>
    """

    return render_template_string(
        html,
        problems=FREQUENCIES.keys(),
        result=result,
        selected=selected
    )

# -------------------------------
# UYGULAMA BAŞLAT
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)

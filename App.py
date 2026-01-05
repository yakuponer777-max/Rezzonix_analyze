from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <html>
    <head>
        <title>Rezzonix Analyzer</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
        <h1 style="text-align:center; margin-top:50px;">🔬 Rezzonix Analyzer Çalışıyor!</h1>
        <p style="text-align:center;">Bu sayfa artık boş ekran değil. Tablet ve Render uyumlu.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

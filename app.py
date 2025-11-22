import os
import json
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# --- Lecture automatique des backups depuis links.txt ---
with open("links.txt", "r", encoding="utf-8") as f:
    BACKUPS = json.load(f)

# --- ROUTE ACCUEIL ---
@app.route("/")
def index():
    return render_template("index.html", backups=BACKUPS)

# --- GOOGLE SEARCH CONSOLE ---
@app.route("/robots.txt")
def robots():
    return send_from_directory("tools/google_search-console", "robots.txt")

@app.route("/sitemap.xml")
def sitemap():
    return send_from_directory("tools/google_search-console", "sitemap.xml")

@app.route("/googlea.html")
def google_verify():
    return send_from_directory("tools/google_search-console", "googlea---------.html")

# --- RENDER COMPAT ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

import os
from flask import Flask, render_template
import requests

app = Flask(__name__)

BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:8000")


@app.route("/")
def home():
    try:
        response = requests.get(f"{BACKEND_URL}/api/v1/alunos/")
        alunos = response.json()
    except Exception:
        alunos = []

    return render_template("index.html", alunos=alunos)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=3000, host="0.0.0.0")
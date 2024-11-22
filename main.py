from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def page_index():
    return render_template("index.html")

@app.route("/history")
def page_history():
    return render_template("history.html")

@app.route("/settings")
def page_settings():
    return render_template("settings.html")

if __name__ == "__main":
    app.run(debug=True, host="0.0.0.0", port=5000)
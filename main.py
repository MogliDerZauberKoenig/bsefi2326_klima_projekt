from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", sensors="")

if __name__ == "__main":
    app.run(debug=True, host="0.0.0.0", port=5000)
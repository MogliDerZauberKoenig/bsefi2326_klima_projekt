from flask import Flask, render_template
import random

def generatesensordata():
    return [
        {"name": "CPU Usage", "value": random.randint(10, 100), "unit": "%"},
        {"name": "Memory Usage", "value": random.randint(10, 100), "unit": "%"},
        {"name": "Disk Usage", "value": random.randint(10, 100), "unit": "%"},
        {"name": "Network Traffic", "value": random.randint(1, 1000), "unit": "Mbps"},
    ]

app = Flask(__name__)

@app.route("/")
def hello_world():
    sensors = generatesensordata()
    return render_template("index.html", sensors=sensors)

if __name__ == "__main":
    app.run(debug=True, host="0.0.0.0", port=5000)
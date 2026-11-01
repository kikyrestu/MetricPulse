from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return {"app": "MetricPulse", "status": "rebuilding", "milestone": "M1-M4 rebuild"}

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.r
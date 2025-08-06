from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """<pre>
🟢 Status: Healthy  
📦 Service: Flask Web API  
🔁 Environment: Docker + Compose  
✅ All systems operational
</pre>"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

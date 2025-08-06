from flask import Flask

app = Flask(__name__)

@app.route("/")
def health_check():
    return """<!DOCTYPE html>
<html>
<head>
  <title>Status Page</title>
  <style>
    body {
      background-color: #0e1117;
      color: #e6edf3;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }
    .status-box {
      background-color: #161b22;
      border: 1px solid #30363d;
      border-radius: 12px;
      padding: 30px 50px;
      box-shadow: 0 0 20px rgba(0, 255, 153, 0.2);
      text-align: left;
    }
    h1 {
      color: #39ffcc;
      margin-bottom: 10px;
    }
    p {
      margin: 6px 0;
      font-size: 1.1rem;
    }
    .success {
      color: #00ff88;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <div class="status-box">
    <h1>🚀 Flask App Status</h1>
    <p class="success">🟢 Healthy & Running</p>
    <p>📦 Service: <strong>Flask Web API</strong></p>
    <p>🔁 Environment: <strong>Docker + Compose</strong></p>
    <p>✅ Systems: <strong>All Operational</strong></p>
  </div>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

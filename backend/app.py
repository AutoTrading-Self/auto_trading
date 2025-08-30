from flask import Flask, jsonify
from flask_cors import CORS
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

app.config['DEBUG'] = os.getenv('FLASK_DEBUG', True)

@app.route('/')
def home():
    return jsonify({
        "service": "Trading Project API",
        "status": "running",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/info')
def api_info():
    return jsonify({
        "api_version": "v1",
        "endpoints": {
            "/": "홈페이지",
            "/health": "헬스체크",
            "/api/info": "API 정보"
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

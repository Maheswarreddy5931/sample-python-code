from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Hello from Python App!",
        "status": "running"
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy"
    }), 200

@app.route('/about')
def about():
    return jsonify({
        "app": "My Python App",
        "version": "1.0.0",
        "author": "Your Name"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
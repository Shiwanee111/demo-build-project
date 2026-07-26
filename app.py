from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Hello from Shiwanee's DevOps Pipeline!"

@app.route('/health')
def health():
    return "✅ App is healthy and running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
#app.py
from flask import Flask

app = Flask(__name__)  # âœ… Corrected

@app.route('/')
def hello():
    return "Hello, World from gowri hs, this is my final project from microdegree !"

if __name__ == '__main__':  # âœ… Corrected
    app.run(host='0.0.0.0', port=5000)


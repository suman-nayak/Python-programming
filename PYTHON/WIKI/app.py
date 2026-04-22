from flask import Flask, render_template, request, jsonify
import wikipedia
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    topic = data.get('topic')
    try:
        summary = wikipedia.summary(topic, sentences=3)
        return jsonify({"status": "success", "topic": topic, "summary": summary})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/random', methods=['GET'])
def get_random():
    # Wikipedia's random function returns a list
    random_title = wikipedia.random(pages=1)
    return jsonify({"topic": random_title})

if __name__ == '__main__':
    app.run(debug=True)
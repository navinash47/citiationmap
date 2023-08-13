from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/get_citations', methods=['GET'])
def get_citations():
    data = {
        "nodes": [
            {"id": "Paper A", "group": 1},
            {"id": "Paper B", "group": 2},
            {"id": "Paper C", "group": 2}
        ],
        "links": [
            {"source": "Paper A", "target": "Paper B", "value": 1},
            {"source": "Paper B", "target": "Paper C", "value": 1}
        ]
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

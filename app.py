# app.py
from flask import Flask, jsonify
from scraper import obtener_partidos

app = Flask(__name__)

@app.route('/api/partidos')
def api_partidos():
    data = obtener_partidos()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify
import redis
import time

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

@app.route('/data/<key>')
def get_data(key):
    cached = r.get(key)
    if cached:
        return jsonify({'source': 'cache', 'data': cached})

    time.sleep(2)
    data = f"valeur_{key}"
    r.setex(key, 60, data)

    return jsonify({'source': 'slow-db', 'data': data})

if __name__ == '__main__':
    app.run(debug=True)

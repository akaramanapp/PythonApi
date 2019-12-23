#!flask/bin/python
from flask import Flask, jsonify
import os

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

@app.route('/city')
def index():
    cityList = ["Istanbul", "Ankara", "Izmir", "Erzincan", "Kayseri"];
    return jsonify({'city': cityList})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=port)



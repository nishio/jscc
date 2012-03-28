import hashlib
import json
import cPickle
from datetime import datetime
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect, url_for
data = {
    "when": datetime.now().isoformat(),
    "error": 0,
    "warning": 0,
    "lint": 0,
    "success": True,
}
cPickle.dump(data, file("database", "wb"))

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/api/put")
def put_data():
    data = json.loads(request.args['json'])
    cPickle.dump(data, file("database", "wb"))
    return 'OK'

@app.route("/api/get")
def get_data():
    data = cPickle.load(file("database", "rb"))
    return json.dumps(data)


if __name__ == "__main__":
    app.run('0.0.0.0', 8104)

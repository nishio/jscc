import argparse
import hashlib
import json
import cPickle
from datetime import datetime
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect, url_for
import os
import sqlite3

data = {
    "when": datetime.now().isoformat(),
    "error": 0,
    "warning": 0,
    "lint": 0,
    "success": True,
}

cPickle.dump(data, file("database", "wb"))

DATABASE = 'database.sqlite'
if not os.path.isfile(DATABASE):
    # Create table
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE log
             (when_ TEXT, user TEXT, proj TEXT,
              error INTEGER, warning INTEGER, lint INTEGER,
              success INTEGER, message TEXT)''')
    conn.commit()
    conn.close()



app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/api/put")
def put_data():
    data = json.loads(request.args['json'])
    cPickle.dump(data, file("database", "wb"))

    when = datetime.now().isoformat()
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        '''INSERT INTO log VALUES(?, ?, ?, ?, ?, ?, ?, ?)''',
        (when, 'default-user', 'default-proj',
         data['error'], data['warning'], data['lint'],
         data['success'], data.get('message', '')))
    conn.commit()
    conn.close()
    return 'OK'

@app.route("/api/get")
def get_data():
    data = cPickle.load(file("database", "rb"))
    return json.dumps(data)


@app.route("/api/get_multi")
def get_data_multi():
    when_ = request.args.get('when', datetime.now().isoformat())
    number = request.args.get('number', 10)

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        '''SELECT error, warning, lint FROM log WHERE when_ < ? AND user = ? AND proj = ? LIMIT ?''',
        (when_, 'default-user', 'default-proj', number))

    data = cursor.fetchall()
    conn.commit()
    conn.close()
    #data = map(lambda (e, w, l): dict(error=e, warn=w, lint=l), data)
    return json.dumps(data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Visualizing server')
    parser.add_argument('--port', default=8104, type=int)

    args = parser.parse_args()
    app.run('0.0.0.0', args.port)

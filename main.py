#!/usr/bin/python
"""
JSON based data saving in sqlite db and retrieval of sqlite data.
    Oct 17, 2023.
    Work towards ALX profolio project 

Model serving with model id saved with client id.

    + features:
        + training a simple model (regression model given 
            + two inputs [2 columns]  input: x : [1,2], y: [1,2]
            + and output [1 column])  output : "VL": [1, 1]
        + model versioninng with a random key generated each time a model train is posted.
        + model id is used for using the model.
            + model(Structure, input-> put contrained) is currently fixed
"""
import flask
import time
from utils import notify_msg
from flask import jsonify
import json
import numpy as np
import sqlite3
from sklearn.linear_model import LinearRegression
from flask import request, jsonify, session
import os
import sys
app = flask.Flask(__name__)

app.secret_key = 'UHXMU'  # Change to a secure secret key in production

conn = sqlite3.connect('mydatabase.sqlite')

c = conn.cursor()

# Create a table
# c.execute("DROP TABLE IF EXISTS mytable2")
c.execute('CREATE TABLE IF NOT EXISTS mytable2 (id INTEGER PRIMARY KEY, REF TEXT, data BLOB)')
# binary_data = b'38434'
# ref = 1
# # Insert binary data into the column
# c.execute('INSERT INTO mytable2 (REF, data) VALUES (?,?)', (1, binary_data,))

# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()
# connect to the databa


# User data 
users = {
    "1": {"password": "password1", "credits": 100},
    "2": {"password": "password2", "credits": 3},
    "4": {"password": "password4", "credits": 500},
    "5": {"password": "password5", "credits": 0}
}

# Credit keys 
keys = {
    "34213": 10,
    "fher3": 1,
    "3434": 20
}

# Models 
models = {
    "3433r": lambda x: x ** 2,
    "3434": lambda y: y - 2
}

# Function to check if the user is logged in
def is_logged_in():
    return 'user' in session

@app.route("/", methods=["GET", "POST"])
def index():
    if is_logged_in():
        return f"Hello, {session['user']}!"
    return "Not login, need to login /login or first register at /register"

@app.route("/register", methods=["POST"])
def register():
    if is_logged_in():
        return "Already logged in."

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in users:
        return "User already exists."

    users[username] = {"password": password, "credits": 10}
    session['user'] = username

    return f"Registration successful, {username}!"

@app.route("/login", methods=["POST"])
def login():
    if is_logged_in():
        return "Already logged in."

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in users and users[username]["password"] == password:
        session['user'] = username
        return f"Login successful, {username}."
    else:
        return "Login failed."

@app.route("/logout", methods=["GET"])
def logout():
    if is_logged_in():
        username = session['user']
        session.pop('user', None)
        return f"Logged out, {username}!"
    return "Not logged in."

@app.route("/credits/increase/<key>", methods=["POST"])
def credit_increase(key):
    user = session.get('user')
    if not user:
        return "Login required."

    credit_up = keys.get(key, 0)
    if user in users:
        users[user]["credits"] += credit_up
        return f"New Balance: {users[user]['credits']}"

@app.route("/credits/status")
def credit_check():
    user = session.get('user')
    if not user:
        return "Login required."

    if user in users:
        return f"Remaining Credits: {users[user]['credits']}"

@app.route("/models/all")
def model_list():
    user = session.get('user')
    if not user:
        return "Login required."

    if rate_limit(user):
        model_references = list(models.keys())
        return jsonify(model_references)
    else:
        return "Insufficient credits to access this endpoint."

@app.route("/train", methods=["POST"])
def training_data():
    user = session.get('user')
    if not user:
        return "Login required."

    if rate_limit(user):
        current_time = time.time()
        conn = sqlite3.connect('mydatabase.sqlite')

        c = conn.cursor()

        data = request.get_json()

        X = data['input']['x']
        Y = data['input']['y']
        INPUT = np.array([X, Y]).T
        Z = data['output']['VL']
        output = np.array(Z).reshape(-1, 1)
        newData = {}

        reg = LinearRegression().fit(INPUT, output)
        data['input_shape'] = INPUT.shape
        data['output_shape'] = output.shape
        data['intercept'] = reg.intercept_.tolist()
        data['score'] = str(reg.score(INPUT, output))
        data['coeff'] = reg.coef_.tolist()

        data['modelReference'] = hash(str(data))
        data['trained'] = True

        c.execute('INSERT INTO mytable2 (REF, data) VALUES (?, ?)', (data['modelReference'], json.dumps(data),))
        conn.commit()
        conn.close()
        notify_msg("Model trained and POSTed")

        return data
    else:
        return "Insufficient credits to access this endpoint."


@app.route("/test", methods=["GET"])
def test_data():
    user = session.get('user')
    if not user:
        return "Login required."

    if rate_limit(user):
        current_time = time.time()
        conn = sqlite3.connect('mydatabase.sqlite')

        c = conn.cursor()

        data = request.get_json()
        print(flask.request)


        data = flask.request.get_json()
        notify_msg("model called GET {}".format(str(data)))

        # do something with the data
        modelReference = data.get("input",{"LOL":"LOL"}).get("modelReference", 1)
        print(data, modelReference)
        # return modelReference
        current_time = time.time()
        print(current_time)
        conn = sqlite3.connect('mydatabase.sqlite')

        c = conn.cursor()

        
        c.execute('SELECT data from mytable2 WHERE REF = ?', (modelReference,))
        results = c.fetchall()
            # return modelReference
        conn.close()
        if results:
           
                # return str(results)
                # print(data,'34')
                # intercept = data[0].get('intercept', 0)
                results = json.loads(str(results[0][0].replace("'",'"')))
                results
                coeff =  np.array(results['coeff'])  
                intercept_ =np.array(results['intercept']).T
                X = data['input']['x']
                Y = data['input']['y']

                INPUT = np.array([X, Y], dtype='f').T
                output =  np.dot(INPUT,coeff.T) + intercept_

                return jsonify(output.tolist())

                print(jsonify(results[0][0]))#W#['intercept'])
                jsonify(data)
                # return data
                notify_msg("model called v0")
                return jsonify(results[0])


        else:
            data['Modeled'] = "NOT CHECKED"
            data['results'] = [str(results), modelReference]
            return (data)

        return "Hello, World!"
    else:
        return "Insufficient credits to access this endpoint."

@app.route("/models/run/<model_id>", methods=["GET"])
def execute_request(model_id):
    user = session.get('user')
    if not user:
        return "Login required."

    if rate_limit(user):
        model = models.get(model_id)
        if model:
            input_data = 5
            result = model(input_data)
            return f"Result: {result}"
        else:
            return "Model not found."
    else:
        return "Insufficient credits to access this endpoint."

def rate_limit(user):
    if user in users and users[user]["credits"] > 0:
        users[user]["credits"] -= 1
        return True
    else:
        return False

def decrease_credits(user, n):
    if user in users:
        users[user]["credits"] -= n
        remaining = users[user]["credits"]
        valid = remaining >= 0
        return {"remaining": remaining, "valid": valid}

if __name__ == "__main__":
    num_args = len(sys.argv)
    if num_args<=1:
        app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
    else:
        app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

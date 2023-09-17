"""
JSON based data saving in sqlite db and retrieval of sqlite data.
    Sept 16, 2023.
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

app = flask.Flask(__name__)

import sqlite3
import json

from flask import jsonify
import numpy as np
from sklearn.linear_model import LinearRegression
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

@app.route("/", methods=["GET", "POST"])
def index():
    """
    This project entry point. Would have links to other end points or call them.
    to be implemented further
    """
    if flask.request.method == "POST":
        data = flask.request.get_json()
        # do something with the data
        return data
    return "Hello, World!"


@app.route("/train", methods=["GET", "POST"])
def trainingModel():
    """
    Post -> model training data, for now there is one model. List of models and input, 
    output structures can be list in advanced implementation
    """
    if flask.request.method == "POST":
        current_time = time.time()
        conn = sqlite3.connect('mydatabase.sqlite')

        c = conn.cursor()

        data = flask.request.get_json()
        # do something with the data
        X = data['input']['x']
        Y = data['input']['y']

        INPUT = np.array([X, Y]).T
        Z = data['output']['VL']
        output = np.array(Z).reshape(-1,1)
        newData = {}
        data = newData
        reg = LinearRegression().fit(INPUT, output)
        data['input_shape'] = INPUT.shape
        data['output_shape'] = output.shape
        data['intercept'] = reg.intercept_.tolist()
        data['score'] = str(reg.score(INPUT,output))
        data['coeff'] =reg.coef_.tolist()
        
        data['time'] = current_time
        data['modelReference'] =  hash(str(data))
        data['trained'] = True
        c.execute('INSERT INTO mytable2 (REF, data) VALUES (?,?)', (     data['modelReference'],json.dumps(data),))

        # Commit the changes to the database
        conn.commit()

        # Close the connection
        conn.close()
        return data
    if flask.request.method == "GET":
        print(flask.request)
        data = flask.request.get_json()
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
                return jsonify(results[0])


        else:
            data['Modeled'] = "NOT CHECKED"
            data['results'] = [str(results), modelReference]
            return (data)

        return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
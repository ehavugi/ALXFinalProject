"""
JSON based data saving in sqlite db and retrieval of sqlite data.
    Sept 16, 2023.
    Work towards ALX profolio project

Model serving with model id saved with client id
"""
import flask
import time

app = flask.Flask(__name__)

import sqlite3
from flask import jsonify
conn = sqlite3.connect('mydatabase.sqlite')

c = conn.cursor()

# Create a table
# c.execute("DROP TABLE IF EXISTS mytable2")
c.execute('CREATE TABLE IF NOT EXISTS mytable2 (id INTEGER PRIMARY KEY, REF TEXT, data BLOB)')
binary_data = b'38434'
ref = 1
# Insert binary data into the column
c.execute('INSERT INTO mytable2 (REF, data) VALUES (?,?)', (1, binary_data,))

# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()
# connect to the databa

@app.route("/", methods=["GET", "POST"])
def index():
    if flask.request.method == "POST":
        data = flask.request.get_json()
        # do something with the data
        return data
    return "Hello, World!"


@app.route("/train", methods=["GET", "POST"])
def trainingModel():
    if flask.request.method == "POST":
        current_time = time.time()
        conn = sqlite3.connect('mydatabase.sqlite')

        c = conn.cursor()

        data = flask.request.get_json()
        # do something with the data
        data['time'] = current_time
        data['modelReference'] =  hash(str(data))
        data['trained'] = True
        c.execute('INSERT INTO mytable2 (REF, data) VALUES (?,?)', (     data['modelReference'],str(data),))

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
                jsonify(data)
                # return data
                return jsonify(results[0])

        #     # print the results
        #     # for row in results:
        #     #   print(row)


        #     # Commit the changes to the database
        #     conn.commit()

        #     # Close the connection
        #     return results
        else:
            data['Modeled'] = "NOT CHECKED"
            data['results'] = [str(results), modelReference]
            return (data)

        return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
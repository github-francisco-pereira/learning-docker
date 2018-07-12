import uuid
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.mydb

@app.route("/")
def retrieve():

    _items = db.cidades.find()
    items = [item for item in _items]

    return render_template('cidade.html', items=items)


@app.route('/new', methods=['POST'])
def insert():

    item_doc = {
        'nome': request.form['nome'],
        'pais': request.form['pais']
    }
    db.cidades.insert_one(item_doc)

    return redirect(url_for('retrieve'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

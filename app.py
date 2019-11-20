# SQL Alchemy Homework 

# Creating a simple flask application, that creates 
# an API, that uses SQL Alchemy, to interact with SQL

from flask import Flask, jsonify

from db import Db
from tables import Studios, Actor

app = Flask(__name__)

pg_db = Db("films")

@app.route("/")
def home_page():
    return jsonify({'Home':'Page'})

@app.route("/studios")
def list_studios():
    session = pg_db.get_session()
    all_studios = session.query(Studios)
    s = []
    for a in all_studios:
        s.append({'name': a.name, 'owner':  a.owner})
    session.close()
    return jsonify(s)

@app.route("/actors/<last_name>")
def get_actor_by_last_name(last_name):
    session = pg_db.get_session()
    actor_info = session.query(Actor).filter(Actor.last_name == last_name.upper())
    session.close()
    output = {}
    for actor in actor_info:
        output['name'] = f"{actor.first_name} {actor.last_name}"
    return jsonify(output)
    

if __name__ == "__main__":
    app.run(debug=True)
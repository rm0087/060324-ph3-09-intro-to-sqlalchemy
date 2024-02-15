#!/usr/bin/env python3

from flask import Flask, request, jsonify, make_request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, Deli, Hamburger

app = Flask(__name__)
# the config for the uri determines the name of the database we'll use
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# the setup for migrate and the init_app connects everything together with alembic (the migration tool)
migrate = Migrate(app, db)

db.init_app(app)

# the next three lines aren't necessary (I don't generally add them) but they'll add shortcuts if you want them
add = db.session.add
commit = db.session.commit
delete = db.session.delete

@app.get('/')
def index():
    return "Hello World"

# an example get request for all our delis
# don't worry too much about what this does yet
@app.get('/delis')
def get_delis():
    delis = Deli.query.all()
    return make_request( jsonify( [deli.to_dict() for deli in delis] ) )

if __name__ == '__main__':
    app.run(port=5555, debug=True)

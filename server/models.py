from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# the metadata here creates certain naming convensions in the database
# in this case it handles foreign keys
# you generally won't have to set this up
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

# this sets up the database connection
db = SQLAlchemy(metadata=metadata)

class Hamburger(db.Model):
    
    # the tablename is essential
    __tablename__ = 'hamburgers_table'

    # we always need an id (primary_key=True)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    combo = db.Column(db.Boolean)
    price = db.Column(db.Integer)
    combo_price = db.Column(db.Integer)


class Deli(db.Model):
    
    __tablename__ = 'delis_table'

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String)
    name = db.Column(db.String, nullable=False)
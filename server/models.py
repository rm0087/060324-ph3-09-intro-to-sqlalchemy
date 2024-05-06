from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# the metadata here creates naming convensions in the database
# in this case it handles foreign keys
# you generally won't have to set this up
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

# this sets up the database connection
db = SQLAlchemy(metadata=metadata)

# hey we're using sqlalchemy and the db.Model for this class
class Deli(db.Model):
    
    __tablename__ = "delis_table"

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String)
    name = db.Column(db.String)



class Hamburger(db.Model):
    
    __tablename__ = "hamburgers_table"

    id = db.Column(db.Integer, primary_key=True)
    meat = db.Column(db.String)
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    calories = db.Column(db.Integer)
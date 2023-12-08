import flask_cors
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_praetorian import Praetorian
from dotenv import dotenv_values
from dataclasses import dataclass

# Import credentials from .env file
# Define config of app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:port/DBNAME'  # RDS url

# Initialize connection to database
db = SQLAlchemy(app)

"""
Table 1: Sample Level information
"""
@dataclass
class SampleInfo(db.Model):
    # Name for table
    __tablename__='sample_info'
    
    # Set Up Columns for the table in the postgres database aka attributes?
    id = db.Column(db.Integer, primary_key=True)
    link_id = db.Column(db.Text, unique=True)   # pb_5000nm_10x_date
    filename = db.Column(db.Text)
    date = db.Column(db.Text)
    metal = db.Column(db.Text)
    objective=db.Column(db.Text)
    frame = db.Column(db.Text)
    # Add additional columns....

"""
Table 2: Measurement information
    -- Values within csv file
"""
@dataclass
class Measurements(db.Model):
    # Name for table
    __tablename__='measurement_values'

    # Type casting
    id: str
    intensity: int
    ramanshift: int

    # Set up columns for new table
    id = db.Column(db.Integer, primary_key=True)
    link_id = db.Column(db.Integer, db.ForeignKey("sample_info.link_id")) # Link to measurements table
    intensity = db.Column(db.Text)
    ramanshift = db.Column(db.Text)

# Creates all the tables
with app.app_context():
    db.create_all()
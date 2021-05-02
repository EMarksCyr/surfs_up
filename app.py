#!/usr/python3
#import dependencies

import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)
app = Flask(__name__)

#first route will be the welcome route
@app.route("/")
def welcome():
     return(
    '''
    <h2> Welcome to the Climate Analysis API! </h2>

     Available Routes:
     <ul style="list-style-type:none;">
     <li>/api/v1.0/precipitation</li>
     <li>/api/v1.0/stations</li>
     <li>/api/v1.0/tobs</li>
     <li>/api/v1.0/temp/start/end</li>
     </ul>
     ''')

if __name__ == "__main__":
     app.run()   
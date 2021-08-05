#
import psycopg2
from flask import Flask
import os

db = psycopg2.connect('dbname=fabrica user=postgres password=DIREITOpenal100 host=127.0.0.1')

app = Flask(__name__)
app.secret_key = 'jaca2021'
app.config['UPLOAD_PATH'] = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
db = psycopg2.connect('dbname=fabrica user=postgres password=DIREITOpenal100 host=127.0.0.1')

from views import *

if __name__ == "__main__":
    app.run(debug=True)
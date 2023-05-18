from server import *

import os

os.environ['PGPASSWORD'] = '12345'

from flask import (Flask, request, render_template)
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/Pharmacy'
db = SQLAlchemy(app)


# 日本語

# coding: utf-8

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_object('flaskr.config')


import flaskr.views
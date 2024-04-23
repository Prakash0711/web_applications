import os
from flask import Flask, request
from lib.database_connection import DatabaseConnection

app = Flask(__name__)

# == Your Routes Here ==
@app.route("/albums", methods=['POST'])
def post_album():
    return ""

@app.route("/albums", methods=['GET'])
def get_albums():
    return ""
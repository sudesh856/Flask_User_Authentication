from flask import render_template, request, url_for, redirect

from models import User

from app import db

def register_routes(app,db):
    @app.route('/', methods = ['POST', 'GET'])
    def index():
        return ""
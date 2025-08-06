from flask import render_template, request, url_for, redirect
from flask_login import login_user, logout_user, current_user, login_required

from models import User

from app import db

def register_routes(app,db, bcrypt):
    @app.route('/', methods = ['POST', 'GET'])
    def index():

        if current_user.is_authenticated:
            return str(current_user.username)
        
        else:
            return 'No User is logged in.'
    

    @app.route('/login/<int:uid>')
    def login(uid):
        user=User.query.get(uid)
        if not user:
            return "User not found! ", 404
        
        login_user(user)
        return 'Success'
    

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return 'Success'
    


    
   
   

from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__, template_folder='templates')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./testdb.db'

    app.secret_key = 'SOME KEY'

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # 💡 Import models *after* db is initialized to avoid circular import
    from models import User

    @login_manager.user_loader
    def load_user(uid):
        return User.query.get(int(uid))
    
    @login_manager.unauthorized_handler
    def unauthorized_callback():
        return redirect(url_for('index'))

    from routes import register_routes
    register_routes(app, db, bcrypt)

    migrate = Migrate(app, db)

    with app.app_context():
        db.create_all()

    return app

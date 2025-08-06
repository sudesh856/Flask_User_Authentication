from flask_login import UserMixin
from app import db


class User(db.Model, UserMixin):
    __tablename__ = "users"

    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable = False)

    password = db.Column(db.String, nullable=False)

    role = db.Column(db.String)

    description = db.Column(db.String)

    def __repr__(self):
        return f'<Person username: {self.username} and role {self.role}.>'
    
    def get_id(self):
        return str(self.uid)
    

    
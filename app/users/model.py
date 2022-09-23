from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, date
import pytz
from pytz import timezone
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(64),unique=True,index=True)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(64),index=True, nullable=False)
    phone = db.Column(db.String(64),index=True)
    admin = db.Column(db.String(12),index=True, default='no')
    date = db.Column(db.DateTime, nullable=False, default=datetime.now)


    def __init__(self,email,password,name, phone):
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.name = name
        self.phone = phone


    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def json(self):
        return {
            'email': self.email,
            'name': self.name,
            'phone': self.phone,
            'admin': self.admin,
            'password': self.password_hash,
            'date': str(self.date),
            }

    @classmethod
    def find_by_email(cls, email):
        user = cls.query.filter_by(email=email).first()
        if user:
            return user.json()
        return None
    
    
    def set_password(self, password, commit=False):
        self.password_hash = generate_password_hash(password)
        if commit:
            db.session.commit()


    def __repr__(self):
        return f"email {self.email}"
        

from app import db
from sqlalchemy import func, select
from passlib.apps import custom_app_context as pwd_context

class User(db.Model):
    __tablename__ = 'users'
    
    id                      = db.Column(db.Integer,     nullable=False, unique=True, primary_key=True)
    date_created            = db.Column(db.DateTime(timezone=True), default=func.now())
    date_updated            = db.Column(db.DateTime(timezone=True), default=func.now())
    username               = db.Column(db.String(150), nullable=False, unique=True)
    email_address           = db.Column(db.String(100), nullable=False, unique=True)
    password                = db.Column(db.String(200), nullable=False, unique=False)
    role                    = db.Column(db.String(6),   nullable=False,  unique=False)
    status                  = db.Column(db.String(10),  nullable=True,  unique=False)
    token                   = db.Column(db.String(64),  nullable=True,  unique=False)
    token_created_date_time = db.Column(db.DateTime(timezone=True), default=func.now())    
    session_id              = db.Column(db.String(30),  nullable=True,  unique=False)
    
    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)
        
    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)
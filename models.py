from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
 
db = SQLAlchemy()
 
class Users(db.Model):
    __tablename__ = "users"
 
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String())
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
 
    def __init__(self, email,f_name,l_name):
        
        self.email = email
        self.first_name = f_name
        self.last_name = l_name
 
    def __repr__(self):
        return f"{self.first_name}:{self.id}"

class publications(db.Model):
    __tablename__ = "publications"

    id = db.Column(db.Integer,  primary_key=True)
    student_id = db.Column(db.Integer(),ForeignKey(Users.id))
    title = db.Column(db.String())
    year = db.Column(db.String())
 
    def __init__(self, student_id,title,year):
        
        self.student_id = student_id
        self.title = title
        self.year = year
 
    def __repr__(self):
        return f"{self.title}:{self.id}"
from database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Patient(UserMixin, db.Model):
    __tablename__ = "patients"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    ci = db.Column(db.String(50), nullable=False)
    birth_date = db.Column(db.String(50), nullable=False)
    
    def __init__(self, name, lastname, ci, birth_date):
        self.name = name
        self.lastname = lastname
        self.ci = ci
        self.birth_date = birth_date
        
    def save(self):
        db.session.add(self)
        db.session.commit()
    @staticmethod
    def get_by_id(id):
        return Patient.query.get(id)

    @staticmethod
    def get_all():
        return Patient.query.all()

    def update(self, name=None, lastname=None, ci=None, birth_date=None):
        if name is not None:
            self.name = name
        if lastname is not None:
            self.lastname = lastname
        if ci is not None:
            self.ci = ci
        if birth_date is not None:
            self.birth_date = birth_date
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()


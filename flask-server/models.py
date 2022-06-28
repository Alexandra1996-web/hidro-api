from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)
db.init_app(current_app)
db.Model.metadata.reflect(db.engine)


class FlaskHidrometricaModel(db.Model):
    __tablename__ = 'Hidrometrica'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String(50))
    nivel = db.Column(db.String(50))
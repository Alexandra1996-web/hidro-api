from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from app import app
# Esta funcion se usa para controlar la integracion con aplicaciones Flask
db = SQLAlchemy(app)

# Este callback se utiliza para inicializar la aplicacion con el uso de esta base de datos. Nunca usar bases de datos en un contexto no inicializado o pueden ocurrir problemas
# El parametro current_app hace referencia a la aplicacion de flask que estamos creando "Flask(__name__)"
db.init_app(current_app)

# Reflejar tablas desde una base de datos existente.
db.Model.metadata.reflect(db.engine)

#Creacion de un modelo de tabla para la base de datos
class FlaskHidrometricaModel(db.Model):
    # Este parámetro es para asignar un nombre a la tabla
    __tablename__ = 'Hidrometrica'
    # Este parámetro es para determinar si esta tabla puede añadir nuevas columnas para sus clases heredadas, o para "extender" por así decirlo.
    __table_args__ = {'extend_existing': True}
    # Determinamos los campos y tipos en la base de datos.
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String(50))
    nivel = db.Column(db.String(50))
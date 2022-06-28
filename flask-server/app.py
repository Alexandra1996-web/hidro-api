import requests
from flask import Flask, jsonify

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db.sqlite3'


with app.app_context():
    from models import FlaskHidrometricaModel, db

    @app.route("/api/crear")
    def api():
        fecha = "2015-01-01"
        fechasig = "2016-06-24"
        estacion = "12"

        url = f'https://hidroinformatica.itaipu.gov.py/services/hidrometricaestacion/{fecha}/{fechasig}/{estacion}/'

        respuesta = requests.get(url)
        respuesta_json = respuesta.json()

        print("Registro -------------------->")
        print(f"fecha:  {respuesta_json[0]['fecha']}")
        print(f"nivel: {respuesta_json[0]['nivel']}")
        
        for result in respuesta_json:
            obj = FlaskHidrometricaModel(fecha=result['fecha'], nivel=result['nivel'])
            db.session.add(obj)
            db.session.commit()
        
        
        return jsonify(respuesta_json)
      
    @app.route("/")
    def index():
        return "Funcionaaaa"

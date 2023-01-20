#mandar llamar los servicios: crear usuario y consultar usuario
#recibe variables
#recibe los datos, verifica que esta correcto y manda llamar el servicio
#el servicio se conecta al modelo pero el controlador no
#el controler dice si esta autenticado o no

from flask import Flask, jsonify
from db import Session, engine
from models.user import User


app = Flask(__name__)

session = Session()


@app.route('/', methods=['GET'])
def hola():
    return jsonify({'message': "Endpoint desde hola"})


@app.route('/create_user', methods=['POST'])
def create_user():
    with engine.connect() as con:
        new_user = User(username='omar', password='password')
        session.add(new_user)
        try:
            session.commit()
        except:
            return jsonify({'message': "User Already Exists"})
    return jsonify({'message': "User Created Succesfully"})


if __name__ == "__main__":
    app.run(debug=True)

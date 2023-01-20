#corre app flask
# crear migraciones
# crear conexion a db
# crear tabla y conexion a la db
#crear tabla en base a flask migrate
#conecta al controlador
#crear una funcion en el controller que recibe como parametro la app flask
#se puede usar blueprint

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)
migrate = Migrate(app,db)

class User(db.model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(16))
    password = db.Column(db.String(64))


if __name__ == __main__:
    app.run(debug=True)


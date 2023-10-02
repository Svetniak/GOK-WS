import os
from flask import Flask

#Esta es la fabrica de aplicaciones.
def create_app():
    app = Flask(__name__)
#__name__ es el nombre del modulo de Python actual, la aplicacion necesita saber donde se encuentra para configurar las trayectorias a los archivos.

#from mapping - crea algunas configuraciones basicas que usara la aplicaion
#Se crean las configuraciones de entorno para conectar la base de datos.
    app.config.from_mapping(
        SECRET_KEY='mikey',
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE=os.environ.get('FLASK_DATABASE'),
    )

    #llama a la funcion de db.py
    from . import db
    db.init_app(app)

    @app.route('/hola')
    def hola():
        return 'Chanchito feliz'

    return app

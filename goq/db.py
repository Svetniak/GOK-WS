import mariadb
import click
from flask import current_app, g
from flask.cli import with_appcontext
from .schema import instructions

#busca el atributo db en g
#Llama a las configuraciones que se definieron en db.py
def get_db():
    if 'db' not in g:
        g.db = mariadb.connect(
            host=current_app.config['DATABASE_HOST'],
            user=current_app.config['DATABASE_USER'],
            password=current_app.config['DATABASE_PASSWORD'],
            database=current_app.config['DATABASE'],
        )
        #asigna la propiedad c, para traer los valores como un dic al cursor
        g.c = g.db.cursor(dictionary=True)
    return g.db, g.c

#funcion para cerrar la base de datos.
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

#cierra la base de datos despues de hacer una peticion.
def init_db():
    db, c = get_db()
    for i in instructions:
        c.execute(i)

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Database initialized')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

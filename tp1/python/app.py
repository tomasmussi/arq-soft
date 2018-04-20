from flask import Flask


app = Flask(__name__)

@app.route('/hola/<id>')


def hola(id = None):
	return "Hola mundo...!" + id

"""
gunicorn app:app

ejecuta minimo dos procesos: un master y un worker al menos

Los requests llegan al master y se los pasa al worker que ejecuta el codigo

El master puede hacer varios workers

Para mas workers, hay que cambiar el comando de gunicorn
"""
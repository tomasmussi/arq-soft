from flask import Flask
import time

TENTH_OF_SECOND = 0.1 # Time in seconds
MAX_ITERATIONS = 524288

app = Flask(__name__)

@app.route('/empty')
def empty():
	return "Empty"


@app.route('/test/<id>')
def test(id):
	return "Hola mundo...!" + str(id)

"""
Defines a slow and light endpoint, this means that the endpoint is slow
but it does not demand a lot of resources, such as CPU time, Memory, Disk operations, etc
"""
@app.route('/light')
def light():
	# For now a simple sleap will do
	time.sleep(TENTH_OF_SECOND)
	return "Finished waiting " + str(TENTH_OF_SECOND) + " seconds"


"""
Defines a slow and heavy endpoint, this means that the endpoint is slow and demands
a resource:
 - CPU TIME: a for loop from 1 to a high number
 - Memory: an expanding list could be, appending elements and requiring more memory
 - Disk: reading/writing to disk something, seek operations
"""
@app.route('/heavy')
def heavy():
	# For now a simple for loop will do
	start = time.time()
	for i in xrange(MAX_ITERATIONS):
		l = 1 # Do nothing
	end = time.time()
	elapsed = end - start
	return "Finished waiting " + str(elapsed) + " seconds"



"""
gunicorn app:app

ejecuta minimo dos procesos: un master y un worker al menos

Los requests llegan al master y se los pasa al worker que ejecuta el codigo

El master puede hacer varios workers

Para mas workers, hay que cambiar el comando de gunicorn
"""
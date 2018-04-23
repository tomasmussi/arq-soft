from flask import Flask
import time

SLEEP_TIME = 0.1 # in seconds
MAX_ITERATIONS = 5242880

app = Flask(__name__)

@app.route('/empty')
def empty():
	return "Empty"

@app.route('/test/<id>')
def test(id):
	return "Hola mundo...! " + str(id)

"""
Defines a slow and light endpoint. This means that the endpoint is slow
but it does not demand a lot of resources, such as CPU time, Memory, Disk operations, etc
"""
@app.route('/light')
def light():
	# For now a simple sleep will do
	time.sleep(SLEEP_TIME)
	return "Finalizo en " + str(SLEEP_TIME) + " segundos"

"""
Defines a slow and heavy endpoint. This means that the endpoint is slow and demands a resource:
 - CPU time: a for loop from 1 to a high number
 - Memory: an expanding list could be, appending elements and requiring more memory
 - Disk: reading/writing to disk something, seek operations
"""
@app.route('/heavy')
def heavy():
	# For now a simple for spin loop will do
	start = time.time()
	for i in xrange(MAX_ITERATIONS):
		l = 1 # Do nothing
	end = time.time()
	elapsed = end - start
	return "Finalizo en " + str(elapsed) + " segundos"

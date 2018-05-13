from flask import Flask
import time
import logging

SLEEP_TIME = 0.1 # in seconds
MAX_ITERATIONS = 5242880

app = Flask(__name__)

# This allow us to log with app.logger to gunicorn_logger. That way, by sending those
# logs to stdout (--log-file=-) in the docker-compose, we can check directly for them there
if __name__ != "__main__":
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

@app.route('/')
def home():
	app.logger.info("Request arrived")
	return "Home python"

@app.route('/test')
def test():
	print("Request arrived")
	l = []
	for i in range(MAX_ITERATIONS * 100):
		l.append(i)
		l.pop()
	return "Hola mundo!"

# @app.route('/test/<id>')
# def test(id):
# 	return "Hola mundo! " + str(id)

"""
Defines a slow and light endpoint. This means that the endpoint is slow
but it does not demand a lot of resources, such as CPU time, Memory, Disk operations, etc
"""
@app.route('/light')
def light():
	# For now a simple sleep will do
	time.sleep(SLEEP_TIME)

	response = "Finalizo en " + str(SLEEP_TIME) + " segundos"
	print(response)
	return response

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

	response = "Finalizo en " + str(elapsed) + " segundos"
	print(response)
	return response

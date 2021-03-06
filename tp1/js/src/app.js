const express = require('express');
const app = express();
// In order to serve static files
app.use(express.static('.'));

// Constants
const PORT = process.env.PORT || 3000;
const MAX_ITERATIONS = 5242880;
const SLEEP_TIME = 100; // in miliseconds

// Endpoints
app.get('/', (req, res) => {
	console.log("Request arrived")
	res.send("Home node");
})

app.get('/test', (req, res) => {
	console.log("Request arrived")
	for (let i = 0; i < (MAX_ITERATIONS*100); i++) {};
	res.send("Hola mundo!");
});

/*
 * Defines a slow and light endpoint. This means that the endpoint is slow
 * but it does not demand a lot of resources, such as CPU time, memory, disk operations, etc
 */
app.get('/light', (req, res) => {
	console.log("Request arrived")

	// For now a simple sleep will do
	const begin = Date.now();
	setTimeout((begin) => {
		const end = Date.now();
		const elapsed = end - begin;

		const response = "Finalizo luego de " + elapsed + " milisegundos";
		console.log(response);
		res.send(response);
	}, SLEEP_TIME, begin);
});

/*
 * Defines a slow and heavy endpoint. This means that the endpoint is slow and demands a resource:
 * - CPU time: a for loop from 1 to a high number
 * - Memory: an expanding list could be, appending elements and requiring more memory
 * - Disk: reading/writing to disk something, seek operations
 */
app.get('/heavy', (req, res) => {
	console.log("Request arrived")
	
	// For now a simple for spin loop will do
	const t0 = Date.now();
	for (let i = 0; i < MAX_ITERATIONS; i++) {
		let div = 6.98/3.02;
	};
	const t1 = Date.now();

	response = "Termino loop luego de " + (t1 - t0) + " milisegundos";
	console.log(response);
	res.send(response);
});

app.listen(PORT, () => console.log('Escuchando en el puerto ' + PORT));

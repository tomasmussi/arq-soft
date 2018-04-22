
const express = require('express');

//Multiples instancias de node:
// const cluster = require('cluster');
const app = express();
const PORT = 3000;
const TENTH_SECOND_IN_MILLIS = 1;
const MAX_ITERATIONS = 5242880;

/*
for (let i = 0; i < 5; i++) {
	fork();
	if (hijo) {
		worker();
	}
}
*/

app.get('/test', test);
app.get('/light', light);
app.get('/heavy', heavy);

// Definicion de una funcion anonima que recibe dos parametros
app.get('/test/:id', (req, res) => {
	res.send("Hola mundo.!" +  req.params.id);
});

function test(req, res) {
	res.send("Hola mundo.!");
}

/*
 * Defines a slow and light endpoint, this means that the endpoint is slow
 *but it does not demand a lot of resources, such as CPU time, Memory, Disk operations, etc
*/
function light(req, res) {
	// For now a simple sleap will do
	var begin = Date.now();
	setTimeout((begin) => {
		var end = Date.now();
		console.log("Finalizo luego de " + (end-begin) + " milisegundos");
		res.send("Finalizo luego de " + (end-begin) + " milisegundos");
	}, 1000, begin);
}


/*
 * Defines a slow and light endpoint, this means that the endpoint is slow
 *but it does not demand a lot of resources, such as CPU time, Memory, Disk operations, etc
*/
function heavy(req, res) {
	// For now a simple for spin loop will do
	var t0 = Date.now();
	for (var i = 0; i < MAX_ITERATIONS; i++){
	};
	var t1 = Date.now();
	res.send("Termino loop luego de " + (t1 - t0) + " milisegundos");
}

app.listen(PORT, () => console.log('Escuchando en el puerto ' + PORT));

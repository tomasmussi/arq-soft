
const express = require('express');

//Multiples instancias de node:
const cluster = require('cluster');
const app = express();

/*
for (let i = 0; i < 5; i++) {
	fork();
	if (hijo) {
		worker();
	}
}
*/


app.get('/hola', hola);

// Definicion de una funcion anonima que recibe dos parametros
app.get('/hola/:id', (req, res) => {
	res.send("Hola mundo.!" +  req.params.id);
});

function hola(req, res) {
	res.send("Hola mundo.!");
}


const PORT = 3000;

app.listen(PORT, () => console.log('Escuchando en el puerto ' + PORT));

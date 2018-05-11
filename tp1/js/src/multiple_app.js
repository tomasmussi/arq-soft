const cluster = require('cluster');
const http = require('http');

if (cluster.isMaster) {
  console.log(`Master ${process.pid} is running`);

  // Fork workers.
  for (let i = 0; i < 5; i++) {
    cluster.fork();
  }

  cluster.on('exit', (worker, code, signal) => {
    console.log(`worker ${worker.process.pid} died`);
  });
} else {
  // Workers can share any TCP connection
  // In this case it is an HTTP server
  http.createServer((req, res) => {
    var pid = require('process').pid;
    res.writeHead(200);
    res.end('hello world' +  pid + '\n');
  }).listen(8000);

  console.log(`Worker ${process.pid} started`);
}

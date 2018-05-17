## Node Cluster

Para correr el servidor `node` con la aplicación, es necesario instalar los paquetes necesarios con el comando:

```bash
npm install
```

Una vez instalado, se puede indicar el puerto en donde se quiere levantar dicho servidor mediante la variable de ambiente `PORT`, haciendo que correr el servidor sea tan simple como ejecutar:

```bash
PORT=3000 npm start
```

Esto levantará un servidor con una determinada cantidad de workers (3) que podrán responder los requests.
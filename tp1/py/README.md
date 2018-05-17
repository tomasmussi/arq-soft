## Python

Para correr el servidor de `python`, es necesario primero instalar las dependencias con el comando:

```bash
pip install -r requirements.txt
```

Luego, utilizando `gunicorn`, podemos levantar el servidor correspondiente con el comando:

```bash
gunicorn app:app
```

O bien si se quieren correr `n` `workers` al mismo tiempo:

```bash
gunicorn app:app -w n
```

Así como también si se quiere levantar en otro puerto distinto al 8000, se le puede pasar el binding de puerto:

```bash
gunicorn app:app -b port
```

Esto está resumido en el script `init.sh`:

```bash
./init.sh port
./init.sh port n
```

En caso de usar dicho script, en caso de querer especificar la cantidad de workers, es necesario también especificar el puerto de binding en el cual estará escuchando el server.

### Explicación

`gunicorn` ejecuta siempre, al menos, 2 procesos: un `master` y un `worker`. Los requests llegan al master y se los pasa al `worker` que ejecuta el código. Tal como mencionamos anteriormente, se pueden utilizar varios `workers`, de forma que el `master` pueda direccionar esos pedidos a varios de ellos.
## Docker compose
Dado que vamos a usar imagenes docker para el tp entero, incluido el profiling, hay que usar `docker-compose up` para ejecutar todo

En el tp1, tenemos 1 instancia de node, 1 instancia de gunicorn y, segun el siguiente comando, 3 instancias de gunicorn cuya será repartida por Nginx. Para poder ejecutar los containers `docker-compose up --scale n-gunicorn=3` y si no se creó un usergroup docker para que no sea necesario ejecutarlo como root, hay que ejecutar el comando con sudo: `sudo docker-compose up --scale n-gunicorn=3`
Tener cuidado que si se quiere escalar algún otro container, hay que modificar el archivo `nginx_reverse_proxy.conf` que esta en este directorio (si hay dudas, revisar a donde apunta la configuración de nginx en `docker-compose.yml`) para hacer de load balancer

## Nginx

`nginx` es un reverse proxy y load balancer. Para pode utilizarlo, es necesario instalarlo en la máquina. Desde mac, se puede hacer mediante el manejador de paquetes `brew` (`brew install nginx`) y desde `ubuntu` (o similares) con `apt` (`apt-get install nginx`).

Una vez instalado, se puede levantar fácilmente con el comando `nginx`. En nuestro caso, para no utilizar la configuración default (Que se encuentra en `/usr/local/etc/nginx/nginx.conf`), vamos a utilizar la configuración que se encuentra en el archivo `nginx.conf` de esta carpeta. Entonces:

```bash
nginx -p . -c nginx.conf
```

Este mismo comando se encuentra en el script `./nginx.sh`

Además, provee algunas facilidades para "restartearlo" mediante el uso de señales:

```bash
nginx -s reload
```

Así como se usa la misma metodología para cerrarlo:

```bash
nginx -s quit
```
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
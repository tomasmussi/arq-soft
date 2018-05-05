## Artillery

Para instalar artillery, primero ejecutar el comando:

```
npm install --save artillery artillery-plugin-statsd
```

Asegurarse de que esta instalado:

```
artillery -V
```

Ahora bien, artillery puede usar archivos de escenarios en el cual simularemos carga para nuestro web server, y es bastante versatil porque permite definir distintas etapas de carga, mucho mas de lo que se puede hacer con ab (apache benchmark) y ademas envía la información de benchmarking a statsd.

Tomar el escenario ```root.yaml``` de base para crear escenarios de prueba.

Para ejecutar un escenario, lo que hay que hacer una vez que ya se tiene escrito el escenario es:

```
./run-scenario.sh *escenario.yaml* *nombre-escenario*
```

Por ejemplo, el caso base que tenemos:

```
./run-scenario.sh *root* *prueba*
```

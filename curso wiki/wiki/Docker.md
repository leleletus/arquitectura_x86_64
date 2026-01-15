# Contenido
* ## [Antes de empezar](#antes-de-empezar-1)
* ## [Imagen disponible](#imagen-disponible-1)
* ## [Establecer el contenedor](#establecer-el-contenedor-1)
* ## [Vincular el contenedor con VSCode](#vincular-el-contenedor-con-vscode-1)
* ## [Ejemplo de uso](#ejemplo-de-uso-1)

# Antes de empezar

> **IMPORTANTE:** 
>
> **La versión de Docker Desktop que se está usando es ` 20.10.21`, y la versión de VSCode es `1.74.3`.**

* Debe tener por lo menos 30 GB de espacio libre en su disco duro.
* Instalar **Docker Desktop** que se puede encontrar en este [enlace](https://www.docker.com/products/docker-desktop/).
* Debe tener instalado Visual Studio Code con la extensión Dev Containers. [↑](#contenidos)

# Imagen disponible

Los paquetes principales que se usarán en el curso ya están instalados. Los repositorios con los ejemplos ya están clonados y listos para usarse.

  * [Docker-Ubuntu-22.04](https://hub.docker.com/r/stefanoandre/arq)

La clave es ubuntu y el usuario es ubuntu. [↑](#contenidos)

# Establecer el contenedor

* Primero debe "jalar" la imagen:

```
docker pull stefanoandre/arq
```

* Verifique que tiene la imagen:

```
docker images
```

Debería observar un resultado similar al siguiente:

```
REPOSITORY         TAG       IMAGE ID       CREATED             SIZE
stefanoandre/arq   latest    5cf514c60333   About an hour ago   1.7GB
```

* Después debe crear el contenedor:

```
docker run --interactive --tty stefanoandre/arq
```

Este comando lo llevará al "interior" del sistema de archivos del contenedor, debe salir de allí. Para esto ejecute el comando `exit` y volverá a su terminal de su anfitrión.

* Vea el "estado" del contenedor:

```
docker ps --all
```

Observará una salida similar a la siguiente:

```
CONTAINER ID   IMAGE              COMMAND   CREATED         STATUS                     PORTS     NAMES
1f7ee4424d15   stefanoandre/arq   "bash"    2 minutes ago   Exited (0) 3 seconds ago             adoring_yalow
```

Note que el `STATUS` del contenedor es `Exited`.

* Vuelva a iniciar el contenedor:

```
docker start 1f7ee4424d15
```

El valor al final del comando fue obtenido de la columna `CONTAINER ID` del comando anterior.

* Vea el "estado" del contenedor otra vez:

```
docker ps --all
```

Observará una salida similar a la siguiente:

```
CONTAINER ID   IMAGE              COMMAND   CREATED         STATUS         PORTS      NAMES
1f7ee4424d15   stefanoandre/arq   "bash"    5 minutes ago   Up 2 seconds   8888/tcp   adoring_yalow
```

Ahora el contenedor ya está en marcha y listo para ser vinculado a VSCode.

## Usando `docker-compose`:

Los pasos presentados en la sección anterior se pueden simplificar empleando un archivo `.yaml`. En un directorio cree el archivo `docker-compose.yaml` y edítelo para que contenga el siguiente contenido:

```yaml
version: '2.13.0'
services:
  arq:
    image: stefanoandre/arq
    container_name: arq_container
    stdin_open: true 
    tty: true       
    networks:
      - mynet
networks:
  mynet:
    driver: bridge
```
La versión puede variar conforme a la versión de `docker-compose` que usted tenga instalado. Puede ver la versión con el siguiente comando:

```
docker-compose --version
```

Luego, dentro del directorio donde se encuentra este archivo, ejecute el siguiente comando:

```
docker-compose up --detach
```
Y con este procedimiento también debería el contenedor listo para ser usado desde VSCode.

# Vincular el contenedor con VSCode

* Abra una ventana de VSCode:

![paso-cero](https://github.com/stefano-sosac/iee240-learning-material/blob/master/imgsWiki/dockers/docker-00-abrir-vscode.png)

* Ubique el ícono de `Remote-Explorer`:

![paso-uno](https://github.com/stefano-sosac/iee240-learning-material/blob/master/imgsWiki/dockers/docker-01-ubicar-remote-explorer.png)

* Haga click en el ícono de `Remote-Explorer` y en el menú desplegable seleccione la opción `Containers`:

![paso-dos](https://github.com/stefano-sosac/iee240-learning-material/blob/master/imgsWiki/dockers/docker-02-click-remote-explorer.png)

* Haga click en el ícono de `Attach To Container`:

![paso-tres](https://github.com/stefano-sosac/iee240-learning-material/blob/master/imgsWiki/dockers/docker-03-atar-al-contenedor.png)

* Le debería aparecer otra ventana con el símbolo de la esquina inferior izquierda indicando que se encuentra dentro del contenedor:

![paso-cuatro](https://github.com/stefano-sosac/iee240-learning-material/blob/master/imgsWiki/dockers/docker-04-ventana-auxiliar.png)

* Maximice la pantalla, haga click en la pestaña `File` y seleccione `Open Folder`. En las opciones que le salen, elija el directorio `arq`, y luego de click en `OK`:

![paso-cinco](https://github.com/stefano-sosac/iee240-learning-material/blob/master/imgsWiki/dockers/docker-05-abrir-arq.png)

Luego de esto usted debería observar los directorios del curso en el explorador de archivos.

# Ejemplo de uso

Luego de ejecutado todo lo anterior usted debería tener su entorno similar a la siguiente ventana:

![ejemplo-paso-cero](https://github.com/stefano-sosac/iee240-learning-material/blob/master/imgsWiki/dockers/docker-ejemplo-00.png)

En caso no le salga el terminal, solo vaya a la pestaña "Terminal" y elija la opción "Open Terminal". En caso usted esté usando la nueva versión de la imagen de Docker su terminal debería iniciar directo con `bash`. En caso contrario, en su terminal escriba el comando `bash`, y debería observar que el terminal cambia a lo siguiente:

![ejemplo-paso-uno](https://github.com/stefano-sosac/iee240-learning-material/blob/master/imgsWiki/dockers/docker-ejemplo-01.png)

Desde el terminal, ingrese a la carpeta del curso y empiece a probar los ejemplos.
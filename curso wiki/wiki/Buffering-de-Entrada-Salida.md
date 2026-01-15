# Buffering para E/S

De manera simplificada, la información se desplaza a través de varias capas antes de llegar al dispositivo de almacenamiento estable como se muestra en la siguiente imagen:

![caminodelosdatos](https://static.lwn.net/images/2011/jm-data-flow.png)

En la parte superior está la aplicación en ejecución que tiene datos que deben ser guardados en un almacenamiento estable. Esos datos comienzan como uno o más bloques de memoria, o _buffers_, en la propia aplicación. Esos _buffers_ también se pueden entregar a una librería, que puede realizar su propio almacenamiento en _buffer_. Independientemente de si los datos se almacenan en _buffers_ de aplicación o mediante una biblioteca, los datos viven en el espacio de direcciones de la aplicación. La siguiente capa por la que pasan los datos es el kernel, que mantiene su propia versión de una caché de reescritura llamada caché de página. Las páginas desfasadas pueden vivir en la caché de páginas durante un período de tiempo indeterminado, el cual depende de la carga general del sistema y los patrones de E/S. Cuando los datos desfasados finalmente se expulsan de la caché de páginas del núcleo, se escriben en un dispositivo de almacenamiento (como un disco duro). El dispositivo de almacenamiento puede almacenar en _buffer_ los datos en una caché de reescritura volátil. Si se pierde energía mientras los datos están en esta caché, los datos se perderán. Por último, en la parte inferior de la torre está el almacenamiento no volátil. Cuando los datos llega a esta capa, se considera que son "seguros".

Como ejemplo de como funcionan las capas de almacenamiento en búfer, considere una aplicación que escucha en un socket de red para las conexiones y escribe los datos recibidos de cada cliente en un archivo. Antes de cerrar la conexión, el servidor se asegura de que los datos recibidos se escribieron en un almacenamiento estable y envía una confirmación de dichos datos al cliente.

Después de aceptar una conexión de un cliente, la aplicación deberá leer los datos del socket de red en un búfer. La siguiente función lee la cantidad especificada de datos del socket de red y los escribe en un archivo. El llamador ya determinó desde el cliente la cantidad de datos que se esperan y abrió una secuencia de archivos en la que escribir los datos. Se espera que la función (algo simplificada) siguiente guarde los datos leídos del socket de red en el disco antes de devolverlos.

```c
int sock_read(int sockfd, FILE *outfp, size_t nrbytes)
{
    int ret;
    size_t written = 0;
    char *buf = malloc(BUF_TAM);

    if (!buf)
        return -1;

    while (written < nrbytes)
    {
        ret = read(sockfd, buf, BUF_TAM);
        if (ret <= 0)
        {
            if (errno == EINTR)
                continue;
            return ret;
        }
        written += ret;
        ret = fwrite((void *)buf, ret, 1, outfp);
        if (ret != 1)
            return ferror(outfp);
    }

    ret = fflush(outfp);
    if (ret != 0)
        return -1;

    ret = fsync(fileno(outfp));
    if (ret < 0)
        return -1;
    return 0;
}
```

La línea `char *buf = malloc(BUF_TAM)` es un ejemplo de un búfer de aplicación; los datos leídos del socket se colocan en este búfer. Ahora, dado que la cantidad de datos transferidos ya se conoce, y dada la naturaleza de las comunicaciones de red (pueden ser bursty y / o lentas), se emplean las funciones de flujo de libc (fwrite() y fflush(), representadas por "_Library buffers_" en la figura anterior) para almacenar los datos. Las líneas del bucle `while` se encargan de leer los datos del socket y escribirlos en la secuencia de archivos. Cuando termina el bucle `while`, todos los datos se han escrito en la secuencia de archivos. En la línea `ret = fflush(outfp)`, la secuencia de archivos se vacía, lo que hace que los datos se muevan a la capa "Kernel Buffers". Luego, en la línea `ret = fsync(fileno(outfp))`, los datos se guardan en la capa "_Stable storage_".


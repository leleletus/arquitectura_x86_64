# Contenido
* ## [Antes de empezar](#antes-de-empezar-1)
* ## [Imágenes disponibles](#imágenes-disponibles-1)
* ## [Importar VM](#importar-vm-1)
* ## [Modificar el archivo `config`](#modificar-el-archivo-config-1)
* ## [Iniciar la VM](#iniciar-la-vm-1)
* ## [Establecer conexión SSH con la VM](#establecer-conexión-ssh-con-la-vm-1)
* ## [Cerrar la conexión SSH](#cerrar-la-conexión-ssh-1)

# Antes de empezar

> **IMPORTANTE:** 
>
> **Estos apuntes están dirigidos a usuarios de Windows10. La versión de VirtualBox que se está usando es la 7.0.4. La máquinas virtual disponible está configurada para disponer de 2 cores y 2 GB de memoria RAM, pero usted puede cambiar esta configuración desde VirtualBox.**

* Debe tener por lo menos 30 GB de espacio libre en su disco duro.
* Instalar **Virtualbox** que se puede encontrar en este [enlace](https://www.virtualbox.org/wiki/Downloads).
* Instalar el **VM VirtualBox Extension Pack** que se puede encontrar en este [enlace](https://www.virtualbox.org/wiki/Downloads).
* La ruta donde se encuentra VirtualBox, sus dependencias y utilidades deben estar en la variable de entorno "Path".
* Debe habilitar el OpenSSH Client de Windows.
* Debe tener instalado Visual Studio Code con la extensión Remote-SSH. [↑](#contenidos)

# Imágenes disponibles

Los paquetes principales que se usarán en el curso ya están instalados. Los repositorios con los ejemplos ya están clonados y listos para usarse.

<!---  * [Ubuntu-18.04](https://drive.google.com/file/d/1lQXXdfGuLRHf5ktGbrCcM_zRyaTSoOsS/view?usp=sharing) --->
  * [Ubuntu-Desktop-22.04](https://drive.google.com/file/d/1f6SFmxHhWZUu-eNGoo4ChK7tBxf7GByU/view?usp=sharing)
  * [Ubuntu-Server-22.04](https://drive.google.com/file/d/1XOeWTxUkZLa2llnnlOh_Dza7ki913jWY/view?usp=sharing)

La clave de las dos VMs es ubuntu y el usuario es ubuntu. [↑](#contenidos)

# Importar VM

* Desde la GUI de VirtualBox ir a la opción Archivo, luego seleccionar "Importar servicio virtualizado"

![primer-paso](https://github.com/stefano-sosac/iee240-learning-material/blob/master/imgsWiki/vms/importar-vm.png)

* Debería observar una ventana de diálogo como la siguiente, haga click en el ícono del directorio

![segundo-paso](https://github.com/stefano-sosac/iee240-learning-material/blob/master/imgsWiki/vms/importar-vm-dialogo-1.png)

* Se debe ubicar en el directorio donde está alguna de las VMs que ha descargado y hacer click en "Abrir"

![tercer-paso](https://github.com/stefano-sosac/iee240-learning-material/blob/master/imgsWiki/vms/importar-vm-dialogo-2.png)

* Debería observar una ventana de diálogo como la siguiente, haga click en "Next"

![cuarto-paso](https://github.com/stefano-sosac/iee240-learning-material/blob/master/imgsWiki/vms/importar-vm-dialogo-3.png)

* Por último, hacer click en "Terminar" y espera a que el servicio termine de importar la máquina virtual. [↑](#contenidos)

![quinto-paso](https://github.com/stefano-sosac/iee240-learning-material/blob/master/imgsWiki/vms/importar-vm-dialogo-4.png)

# Modificar el archivo `config`

Para abrir el archivo `config` hace click en el ícono azul (el color del ícono puede variar con el tema que esté usando en VSCode) ubicado en la esquina inferior izquierda y selecciona la opción "Open SSH Configuration File ..."

![vscode-config-file](https://github.com/alexandrojim/iee240-learning-material/blob/master/imgsWiki/vms/vscode-config-file.png)

Luego seleccionar la primera opción

![vscode-config-file-2](https://github.com/stefano-sosac/iee240-learning-material/blob/master/imgsWiki/vms/vscode-config-file-2.png)

En el archivo que se abra coloque lo siguiente [↑](#contenidos)

```shell
Host ubuntu-desktop
    HostName 127.0.0.1
    User ubuntu
    Port 2222

Host ubuntu-server
    HostName 127.0.0.1
    User ubuntu
    Port 2223
```

# Iniciar la VM

* Desde la GUI de Virtualbox, seleccionar la VM que desea utilizar

![iniciar-vm-1](https://github.com/stefano-sosac/iee240-learning-material/blob/master/imgsWiki/vms/iniciar-vm-dialogo-1.png)

* Luego, en el botón que dice "Iniciar". Seguido, presionar la flecha que apunta hacia abajo y escoja la opción "Inicio sin pantalla"

![iniciar-vm-2](https://github.com/stefano-sosac/iee240-learning-material/blob/master/imgsWiki/vms/iniciar-vm-dialogo-2.png)

* Cuando la VM termine de levantar, y en la sección de "Previsualización" sea una imagen similar a la siguiente:

![iniciar-vm-3](https://github.com/stefano-sosac/iee240-learning-material/blob/master/imgsWiki/vms/iniciar-vm-dialogo-3.png)

* En caso esté usando la VM **ubuntu_server** la "Previsualización" es más similar a la siguiente imagen:

![iniciar-vm-4](https://github.com/stefano-sosac/iee240-learning-material/blob/master/imgsWiki/vms/iniciar-vm-dialogo-4.png)

Si ya se encuentra en alguno de estos casos, significa que la VM ya está lista para poder realizar la conexión remota.

<!--- Primero, debe abrir un terminal desde Visual Studio Code. Para esto, va a la pestaña "Terminal" y elige "Nuevo terminal" --->

<!--- ![vscode-terminal](https://github.com/alexandrojim/iee240-learning-material/blob/master/imgsWiki/vms/vscode-terminal.png) --->

<!--- Debería observar una sección similar a la siguiente, y se ubica en ella para poder ejecutar los comandos. --->

<!--- ![vscode-terminal-2](https://github.com/alexandrojim/iee240-learning-material/blob/master/imgsWiki/vms/vscode-terminal-2.png) --->

<!--- * Para ver las máquinas virtuales disponibles --->

<!--- ```shell --->
<!--- VBoxManage.exe list vms --->
<!--- ``` --->

<!--- * Para poner en funcionamiento una máquina virtual sin GUI: --->

<!--- ```shell --->
<!--- VBoxManage.exe startvm "ubuntu-22.04-amd64" --type headless --->
<!--- ``` --->

<!--- Note que se está usando "ubuntu-22.04-amd64". --->

<!--- * Para apagar la máquina virtual --->

<!--- > **NOTA:** --->
<!--- > --->
<!--- > **¡Ejecutar esto en el Terminal de Ubuntu una vez realizada la conexión SSH. No ejecutar en el shell de Windows! [↑](#contenidos)** --->

<!--- ```shell --->
<!--- sudo shutdown -P now --->
<!--- ``` --->

# Establecer conexión SSH con la VM

<!--- Primero, verifique que las VMs importadas están disponibles --->

<!--- ![vervmsdisponibles](https://github.com/alexandrojim/iee240-learning-material/blob/master/imgsWiki/vms/vscode-ver-vms-disponibles.png) --->

<!--- Luego, ponga en marcha la VM que desee usar --->

<!--- ![encendervm](https://github.com/alexandrojim/iee240-learning-material/blob/master/imgsWiki/vms/vscode-encender-vm.png) --->

Desde Visual Studio Code, haga click en el ícono de Remote SSH, que está ubicado en la esquina inferior izquierda

![iconoremotessh](https://github.com/stefano-sosac/iee240-learning-material/blob/master/imgsWiki/vms/vscode-icono-remote-ssh.png)

Seleccione la opción "Connect to Host"

![connecttohost](https://github.com/stefano-sosac/iee240-learning-material/blob/master/imgsWiki/vms/vscode-connect-to-host.png)

Haga click en la VM que encendió

![elegiralgunhost](https://github.com/stefano-sosac/iee240-learning-material/blob/master/imgsWiki/vms/vscode-elegir-algun-host.png)

Le saldrá una pantalla parecida a la siguiente, deberá ingresar la clave de la VM.

![ingresarclave](https://github.com/stefano-sosac/iee240-learning-material/blob/master/imgsWiki/vms/vscode-clave.png)

Luego, debería observar en la esquina inferior izquierda que dice "SSH:" seguido del nombre de la VM a la que está conectado

![sshexitoso](https://github.com/stefano-sosac/iee240-learning-material/blob/master/imgsWiki/vms/vscode-ssh-exitoso.png)

Lo siguiente es abrir un directorio de trabajo, para esto haga click en el ícono del "Explorador" que está arriba de la "lupa"

![clickexplorador](https://github.com/stefano-sosac/iee240-learning-material/blob/master/imgsWiki/vms/vscode-click-explorador.png)

Al hacer click, debería observar un columna con un botón que dice "Open Folder"

![abracarpeta](https://github.com/stefano-sosac/iee240-learning-material/blob/master/imgsWiki/vms/vscode-abra-carpeta.png)

Se recomienda trabajar en el directorio "oac"

![abracarpetadocs](https://github.com/stefano-sosac/iee240-learning-material/blob/master/imgsWiki/vms/vscode-abrir-carpeta-oac.png)

Y dar click en "OK"

![aceptardocs](https://github.com/stefano-sosac/iee240-learning-material/blob/master/imgsWiki/vms/vscode-abrir-carpeta-documentos-aceptar.png)

Es probable que se le vuelva a solicitar la clave. [↑](#contenidos)

# Cerrar la conexión SSH

Hacer click en la pestaña "File" de su interfaz de VSCode

![iconoparacerrar](https://github.com/stefano-sosac/iee240-learning-material/blob/master/imgsWiki/vms/vscode-cerrar-conexi%C3%B3n.png)

Luego elige la opción "Close remote connection"

![cerrarconexionremota](https://github.com/stefano-sosac/iee240-learning-material/blob/master/imgsWiki/vms/vscode-cerrar-conexi%C3%B3n-remota.png)

En caso desee volver a establecer conexión con el mismo directorio en el que estuvo trabajando, solo haga click en el directorio que desee en "Recent" [↑](#contenidos)

![dirreciente](https://github.com/stefano-sosac/iee240-learning-material/blob/master/imgsWiki/vms/vscode-reciente.png)

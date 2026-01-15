# Sobre Python

El propósito de estos apuntes es servir de ayuda memoria a los que aún no somos nativos de Python. Las pruebas se realizaron en una instancia de WSL con Ubuntu 22.04 de una computadora Core-i7 Lenovo Legion.

## Antes de clonar

* Si estás en Ubuntu 20.04

Actualizar:

```
sudo apt update
```

En caso no tenga instalado pipenv, lo puede instalar con el siguiente comando:

```
sudo apt install pipenv
```

Para probar el cuaderno de ctypes, requiere nasm y gcc:

```
sudo apt install gcc
sudo apt install nasm
```

* Si estás en Ubuntu 22.04

La versión por defecto es 3.10, y los cuadernos están hechos en 3.8. No sé si habrán problemas de compatibilidad, pero no quiero correr riesgos:

Actualizar:

```
sudo apt update
sudo apt upgrade -y
```

Instalar `pip`:

```
sudo apt install python3-pip -y
```

Instalar `pyenv`:

```
curl https://pyenv.run | bash
```

Luego editar el archivo `.bashrc`, y al final del archivo incluir lo siguiente:

```bash
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

Instalar `pipenv`:

```
pip install --user pipenv
```

Luego editar el archivo `.bashrc`, y al final del archivo incluir lo siguiente:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Instalar las siguientes dependencias:

```
sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev
```

Para que los cambios realizados en `.bashrc` tengan efecto debes cerrar el terminal y volver a abrirlo o ejecutar el siguiente comando:

```
source ~/.bashrc
```

Para validar que los cambios han tenido efecto puede hacer lo siguiente:

```
pyenv --version
```

Y debería observar lo siguiente:

```
pyenv 2.3.8
```

También:

```
pipenv --version
```

Y debería observar lo siguiente:

```
pipenv, version 2022.11.30
```

Ahora ya puede instalar `Python 3.8`:

```
pyenv install 3.8
```

## Luego de clonar

Dentro del directorio clonado, ejecute el siguiente comando para crear el entorno virtual:

```
pipenv shell
```

Luego, para sincronizar las dependencias:

```
pipenv sync
```

Para activar el entorno:

```
pipenv shell
```

Para ejecutar el cuaderno de `jupyter`:

```
pipenv run jupyter notebook
```

Para salir del entorno de `pipenv`:

```
exit
```

En caso tenga dificultad para ver los cuadernos en el repositorio, puede usar los siguientes enlaces:

- [Apuntes de Python](https://nbviewer.jupyter.org/github/stefano-andre/sobre-python/blob/main/python-general.ipynb)
  - [Interacción con el sistema operativo](https://nbviewer.org/github/stefano-andre/sobre-python/blob/main/python-os-sys.ipynb)
- [Apuntes de Numpy](https://nbviewer.jupyter.org/github/stefano-andre/sobre-python/blob/main/numpy-general.ipynb)
- [Apuntes de Pandas](https://nbviewer.jupyter.org/github/stefano-andre/sobre-python/blob/main/pandas-general.ipynb)
  - [Perfil de una función](https://nbviewer.jupyter.org/github/stefano-andre/sobre-python/blob/main/perfil-pthreads.ipynb)
- [Apuntes de Matplotlib](https://nbviewer.jupyter.org/github/stefano-andre/sobre-python/blob/main/matplotlib-general.ipynb)
- [Apuntes de Time y Timeit](https://nbviewer.jupyter.org/github/stefano-andre/sobre-python/blob/main/python-timing.ipynb)
  - [Apuntes sobre el factorial](https://nbviewer.jupyter.org/github/stefano-andre/sobre-python/blob/main/factorial.ipynb)
  - [Apuntes sobre el seno y el coseno](https://nbviewer.org/github/stefano-andre/sobre-python/blob/main/seno_coseno.ipynb)
  - [Apuntes de localidad espacial - I](https://nbviewer.jupyter.org/github/stefano-andre/sobre-python/blob/main/efectos-localidad.ipynb)
  - [Apuntes de localidad espacial - II](https://nbviewer.org/github/stefano-andre/sobre-python/blob/main/efectos-localidad-matriz-matriz.ipynb)
  - [Algoritmos por bloques](https://nbviewer.org/github/stefano-andre/sobre-python/blob/main/algoritmos-por-bloques.ipynb)
  - [Desenroscado de bucles](https://nbviewer.org/github/stefano-andre/sobre-python/blob/main/loop-unrolling.ipynb)
- [Apuntes de Ctypes](https://nbviewer.jupyter.org/github/stefano-andre/sobre-python/blob/main/python-ctypes.ipynb)
  - [Apuntes sobre las optimizaciones de GCC](https://nbviewer.jupyter.org/github/stefano-andre/sobre-python/blob/main/gcc-optis.ipynb)
  - [Apuntes sobre estructuras](https://nbviewer.org/github/stefano-andre/sobre-python/blob/main/ctypes-structure.ipynb)
- [Apuntes de Multiprocessing](https://nbviewer.org/github/stefano-andre/sobre-python/blob/main/python-multiprocessing.ipynb)
- [Problema de los N-cuerpos](https://nbviewer.jupyter.org/github/stefano-andre/sobre-python/blob/main/euler-nbprob.ipynb)

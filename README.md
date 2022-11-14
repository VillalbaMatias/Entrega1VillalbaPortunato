
# Entrega Intermedia - Entrega1

En el proyecto se van a encontrar con un navbar de 7 botones, y un index
El cual los botones se pueden realizar busquedas crear objetos y de la pagina principal.

Ademas de eso, todas las vistas tienen herencia de html. La imagen del Home es traida
desde otro HTML. Y en las vistas de los formularios y buscadores se trae todo menos la 
imagen del Home. 

Asi si se quiere navegar por las funcionalidades no hace falta cambiar
el url para volver para atras o retroceder en la pagina, simplemente clickear en el navbar
nuevamente


## Home

En la pagina del home, se va a mostrar una imagen con un texto, en donde indica que en 
el navbar se pueden realizar las acciones que deseen.


## Botones: Buscar

En el navbar se puede apreciar tres botones con el nombre Buscar. En todas las busquedas que se
realicen en los tres tipos de botones, van a arrojar todos los que sean iguales a los datos
ingresados. 

Osea que si en buscar comision hay mas de una comision a buscar, apareceran todas ellas


### Buscar Comision:

Este boton sirve para buscar los cursos que queramos, cuando ingresemos un numero de Comision.

Siempre y cuando haya sido creada

### Buscar Profesor:

Este boton sirve para buscar los profesores que queramos, cuando ingresemos un apellido.

Siempre y cuando haya sido creado


### Buscar Estudiante:

Este boton sirve para buscar los estudiantes que queramos, cuando ingresemos un apellido.

Siempre y cuando haya sido creado
## Botones: Crear

En el navbar se puede apreciar tres botones con el nombre Crear. En ellas se van a poder 
crear diferentes tipos de objetos

Osea que si en buscar comision hay mas de una comision a buscar, apareceran todas ellas


### Crear Curso:

Este boton sirve para crear un curso, va aparecer un formulario el cual aparecera para completar los valores:
Nombre y Comision. 

### Buscar Profesor:

Este boton sirve para crear un curso, va aparecer un formulario el cual aparecera para completar los valores:
Nombre, Apellido, Email, Profesion, DNI

Siempre y cuando haya sido creado


### Buscar Estudiante:

Este boton sirve para crear un curso, va aparecer un formulario el cual aparecera para completar los valores:
Nombre, Apellido, Email, DNI

Siempre y cuando haya sido creado
## Installation

### virtualenv

Vamos a suponer que ya se tiene instalado Python3, pip y virtualenv.

Con lo cual restaria crear el entorno virtual para levantar nuestro servidor.

En el mismo nivel que se encuentra la carpeta MVT:
C:\Entrega1VillalbaPortunato\MVT

Se va ejecutar el siguiente comando en nuestra powershell:
```
  virtualenv venv

```
Luego activamos el entorno virtual:
```
  .\venv\Scripts\activate

```
Una vez activo entramos a la carpeta MVT
```
  cd MVT

```
Y por ultimo iniciamos el servidor con este comando:
```
  python manage.py runserver

```

### Decouple

Lo que se va a realizar a continuacion se hace para poder nosotros poder hacer un gitignore
al archivo .env que vamo a crear y asi no subir a github nuestra SECRET_KEY y el DEBUG

Necesitamos instalar una libreria de Python, podemos instalarla global o en nuestro entorno virtual.
Esto lo dejo a criterio de cada uno.

Una vez instalado abriremos nuestro settings.py y pegaremos este import:
```
from decouple import config
```

Vamos a necesitar crear un archivo con extension .env en el directorio MVT

El cual deberemos de copiar desde nuestro settings.py las constantes:

SECRET_KEY ; DEBUG

Debemos copiar todo, hasta su valor y las pegaremos en nuestro archivo creado .env
Ahi lo que haremos va a ser borrar el espaciado y las comillas
```
SECRET_KEY = 'valor' DEBUG = 'valor'
```
Quedando asi: 
```
SECRET_KEY=valor
```
Replicamos lo mismo con DEBUG 
```
DEBUG=valor
```

Luego volveremos a nuestro settings.py y lo que haremos va a ser donde estaba SECRET_KEY y DEBUG

Lo remplazaremos y por este valor:
```
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', cast=bool)
```

## FAQ

#### ¿Por que la guia de instalacion es muy breve y solo a un SO?

Por el momento la guia de instalacion esta orientada a Windows ya que es el SO que poseo,
ademas de eso es breve ya que esta orientada a un publico que ya posee los recursos para
abrir Django, de igual manera se va a ampliar mas en un futuro.



## Iniciar proyecto

_Para iniciar un proyecto con Django, se debe tener instalado Python y pip._

- Crear el entorno virtual:
  > python -m venv nombre_entorno
  > py -m venv nombre_entorno
- Activar el entorno virtual:
  > .\nombre_entorno\Scripts\activate
- Crear una archivo llamado requirements.txt y agregar las dependencias:
  > django
  > djangorestframework
  > django-cors-headers
- Instalar las dependencias:
  > pip install -r requirements.txt
- Crear usuario administrador:
  > python manage.py createsuperuser

## Ejecutar migraciones

> python manage.py migrate

## Crear un proyecto

> django-admin startproject Taller

- Correr el servidor:
  > python manage.py runserver
- Abreviatura para correr el servidor:
  > py manage.py runserver

### Cear una aplicación

> python manage.py startapp App1

### Contruir la base de datos ejecutando las migraciones

> python manage.py makemigrations

### Solucion de errores

- Class 'NameClase' has no 'objects' memberPylintE1101:no-member
  > pip install pylint-django

```
Then in Visual Studio Code goto: User Settings (Ctrl + , or File > Preferences > Settings if available ) Put in the following (please note the curly braces which are required for custom user settings in VSC):
```

> "pylint.args": ["load-plugins=pylint_django"],

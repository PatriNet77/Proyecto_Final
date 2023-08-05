# Proyecto_Final

#MySQL Server

https://dev.mysql.com/downloads/installer/

#requirements.txt

asgiref==3.7.2
distlib==0.3.7
Django==4.2.3
filelock==3.12.2
Pillow==10.0.0
platformdirs==3.9.1
sqlparse==0.4.4
tzdata==2023.3
virtualenv==20.24.2

#Migración
python manage.py makemigrations
python manage.py migrate

#Poniendo en marcha el servidor
python manage.py runserver

#Comandos Git

→ En carpeta contenedora del proyecto
Para ejecutar comandos de git(clonar)
- git clone url_del_repo

- git remote add origin url_repo

→ En la carpeta del repositorio
Para ejecutar comandos del entorno(crearlo, activarlo o desactivarlo)
- python -m venv nombre_entorno
- .\nombre_entorno\Scripts\activate
- .\nombre_entorno\Scripts\deactivate
- Si no les reconoce el comando >>> cd nombre_entorno >>> cd Scripts >>> activate o deactivate
- python -m pip install --upgrade pip

- django-admin startproject nombre_proyecto

- pip install nombre_paquete
- pip freeze

- Creaando un archivo requirementes.txt y definiendo el paquete y sus version
- pip freeze > requeriments.txt

- Instalando requeriments.txt
- pip install -r requeriments.txt

- git status
- git add .
- git add archivo_especifico
- git commit -m "mensaje_del_commit"
- git push
- git fetch
- git pull
- etc

→ En la carpeta del proyecto
Para ejecutar comandos del manage.py
- python manage.py runserver
- python manage.py startapp nombre_aplicacion
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser

- pip install nombre_del_paquete
```

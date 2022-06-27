# Taller de Django Rest Framework
## Desarrollo de una API sencilla utilizando Django REST Framework

## **Tecnologías:**
- Django 4
- SQLite3

> Descargue o clone este proyecto y luego siga las siguientes instrucciones:

## Intrucciones para la instalación sistemas basados en UNIX(Linux/Mac):

### Para correr la aplicación primero debemos crear nuestro entorno virtual:
```
python3 -m venv venv
```


### Ahora activamos nuestro entorno:
```
source ./venv/bin/activate
```

### Instalamos las dependencias
```
pip install -r requirements.txt
```

### Creamos las migraciones correspondientes
```
python3 manage.py makemigrations
python3 manage.py migrate
```

### Por úiltimo ejecutamos el programa
```
python3 manage.py runserver
```


## Intrucciones para la instalación en Windows:
### Para correr la aplicación primero debemos crear nuestro entorno virtual:
```
py -m venv venv
```

### Ahora activamos nuestro entorno:
```
.\venv\Scripts\activate
```

### Instalamos las dependencias
```
py -m pip install -r requirements.txt
```

### Creamos las migraciones correspondientes
```
py manage.py makemigrations
py manage.py migrate
```

### Por úiltimo ejecutamos el programa
```
python3 manage.py runserver
```


![Logo](https://i.ibb.co/txq16pT/1111.png)

## Proyecto Veterinaria Flask + mongoDB
Contexto:

Una veterinaria necesita registrar los datos de las mascotas de sus clientes. Los datos que se manejarán son los siguientes:

- Nombre de la mascota.
- Fecha de nacimiento.
- Raza.
- Nombre del propietario.
- DNI del propietario.

La veterinaria requiere de un sitio web que permita:

- Registrar los datos de una mascota.
- Mostrar los datos de una determinada mascota.
- Listar todas las mascotas registradas en la veterinaria ordenadas por: fecha de nacimiento, nombre, raza o nombre del propietario.
- Listar todas las mascotas de un determinado propietario.
- Actualizar los datos de una mascota.

## Inicialización

Para inicializar el programa, se necesita tener los módulos instalados, especificados en requeriments.txt:

```bash
pip install -r requirements.txt
```

Además, se necesita crear un archivo .env con el siguiente contenido:

```python
SECRET_KEY=INGRESE_KEY
FLASK_APP=app.py
```

Para ejecutar el sistema, deberás tener la ruta especificada e iniciar flask:

```bash
flask run
```

## Login
Para ingresar al sistema de registro, necesitarás un usuario y una contraseña.

Por defecto, esta es:

```python
usuario: admin
password: admin
```

## 

Proyecto creado para Silabuz, en base a los módulos desarrollados en clase de Flask + mongoDB.

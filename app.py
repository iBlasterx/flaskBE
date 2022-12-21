from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_login import LoginManager
from flask_wtf import CSRFProtect
from pymongo import MongoClient
from bson.objectid import ObjectId

#from forms import RegistroVeterinaria
from models import Users
from config import Config
from auth import auth_bp

app = Flask(__name__)
app.config.from_object(Config)
client = MongoClient('localhost', 27017)
db = client["veterinaria"]
clientes_collection = db["clientes"]
csrf = CSRFProtect()
login_manager = LoginManager()
login_manager.init_app(app)
app.register_blueprint(auth_bp)

@login_manager.user_loader
def load_user(user_id):
    return Users.objects(id=user_id).first()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/clientes/", methods=['GET', 'POST'])
def clientes():
    clientes = list(clientes_collection.find())
    return render_template("registro.html", clientes=clientes)

@app.route("/nuevo/", methods=['GET', 'POST'])
def nuevo():
    return render_template("agregar.html")

# FORMS: no guarda los datos en la db.
'''
@app.route("/guardar/", methods=['GET', 'POST'])
def agregar2():
    form = RegistroVeterinaria()
    if request.method == 'POST' and form.validate_on_submit():

        nombre = form.propietario.data
        dni = form.dni.data
        mascota = form.mascota.data
        fecha_nacimiento = form.mascota_nac.data
        tipo = form.tipo.data
        raza = form.raza.data

        clientes_collection.insert_one (
                    {
                        "nombre": nombre,
                        "dni" : dni,
                        "mascota" : mascota,
                        "fecha_nacimiento" : fecha_nacimiento,
                        "tipo" : tipo,
                        "raza" : raza,
                    }
            )
    return render_template("guardar.html", form=form)
'''

@app.route("/agregar/", methods=("POST",))
def agregar():
    if request.method == "POST":
        clientes_collection.insert_one(
                {
                "nombre": request.form["nombre"],
                "dni": request.form["dni"],
                "mascota" : request.form["mascota"],
                "fecha_nacimiento":  request.form["fecha_nacimiento"],
                "tipo" : request.form["tipo"],
                "raza" : request.form["raza"],
                }
            )
        return redirect(url_for("clientes"))
    else:
        return notFound()

'''
@app.route("/busqueda/", methods=['GET', 'POST'])
def busqueda():
    valor1 = request.form["test"]
    valor2 = request.form["test2"]
    clientes = list(clientes_collection.find({nombre: valor}))
    clientes = [clientes for clientes in clientes_collection]
    return render_template('search.html', clientes=clientes)
'''

@app.route("/clientes/<id>/borrar", methods=("GET", "POST"))
def borrar_cliente(id):
    clientes_collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("clientes"))

@app.route("/clientes/<id>/editar", methods=("POST",))
def editar_cliente(id):
    clientes_collection.find_one({"_id": ObjectId(id)})
    if request.method == "POST":
        clientes_collection.update_one(
            {"_id": ObjectId(id)},
                {
                    "$set": {
                        "nombre": request.form["nombre"],
                        "dni": request.form["dni"],
                        "mascota" : request.form["mascota"],
                        "fecha_nacimiento":  request.form["fecha_nacimiento"],
                        "tipo" : request.form["tipo"],
                        "raza" : request.form["raza"],
                    }
                },
        )
        return redirect(url_for("clientes"))
    else:
        return notFound()

@app.errorhandler(404)
def notFound(error = None):
    message = {
        'message': "No encontrado" + request.url,
        'status': "404 Not Found"
    }
    response =jsonify(message)
    response.status = 404
    return response

if __name__ == "__main__":
    app.run(debug=True)
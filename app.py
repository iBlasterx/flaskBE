from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from flask_login import LoginManager, login_required
from flask_wtf import CSRFProtect
from pymongo import MongoClient, ASCENDING
from bson.objectid import ObjectId
# import datetime

from forms import SearchForm, RegistroVeterinaria, OrdenarRegistro
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

@login_manager.unauthorized_handler
def unauthorized_callback():
    flash("Necesitas iniciar sesión para hacer eso.")
    return redirect(url_for('auth_bp.login'))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/registro/", methods=['GET', 'POST'])
@login_required
def registro():
    form = OrdenarRegistro()
    buscar = SearchForm()
    clientes = list(clientes_collection.find())
    return render_template("registro.html", clientes=clientes, form=form, buscar=buscar)
    
@app.route('/ordenar_registro/', methods=['GET', 'POST'])
def ordenar_registro():
    form = OrdenarRegistro()
    clientes = clientes_collection.find()
    if form.validate_on_submit():
        criterio = form.criterio_select.data
        clientes = clientes_collection.find().sort([(criterio, ASCENDING)])
        return render_template('registro.html', form=form, clientes=clientes)
    return "Error"

@app.route("/nuevo_registro/", methods=['GET', 'POST'])
@login_required
def nuevo():
    return render_template("nuevo_registro.html")

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
        flash("¡Registro creado con éxito!")
        return redirect(url_for("registro"))
    else:
        return notFound()

@app.route("/clientes/<id>/borrar", methods=("GET", "POST"))
@login_required
def borrar_cliente(id):
    clientes_collection.delete_one({"_id": ObjectId(id)})
    flash("Registro eliminado.")
    return redirect(url_for("registro"))

@app.route("/clientes/<id>/editar", methods=("POST",))
@login_required
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
        flash("Registro editado.")
        return redirect(url_for("registro"))
    else:
        return notFound()
    
@app.route("/busqueda/", methods=['GET', 'POST'])
def busqueda():
    buscar = SearchForm()
    resultados = []
    if buscar.validate_on_submit():
        term_busqueda = buscar.term_busqueda.data
        busqueda_select = buscar.busqueda_select.data
        if busqueda_select == 'nombre':
            resultados = clientes_collection.find({'nombre': {'$regex': term_busqueda}})
        if busqueda_select == 'dni':
            resultados = clientes_collection.find({'dni': {'$regex': term_busqueda}})
        if busqueda_select == 'mascota':
            resultados = clientes_collection.find({'mascota': {'$regex': term_busqueda}})
        if busqueda_select == 'fecha_nacimiento':
            resultados = clientes_collection.find({'fecha_nacimiento': {'$regex': term_busqueda}})
        if busqueda_select == 'tipo':
            resultados = clientes_collection.find({'tipo': {'$regex': term_busqueda}})
        elif busqueda_select == 'raza':
            resultados = clientes_collection.find({'raza': {'$regex': term_busqueda}})
    return render_template('busqueda.html', buscar=buscar, resultados=resultados)

# Testing
@app.route("/nuevo_registro_test/", methods=['GET', 'POST'])
def agregar2():
    form = RegistroVeterinaria()
    if request.method == 'POST' and form.validate_on_submit():

        nombre = form.propietario.data
        dni = form.dni.data
        mascota = form.mascota.data
        #fecha_nacimiento = datetime.datetime.fromordinal(form.mascota_nac.data.toordinal())
        tipo = form.tipo.data
        raza = form.raza.data

        clientes_collection.insert_one (
                    {
                        "nombre": nombre,
                        "dni" : dni,
                        "mascota" : mascota,
                        #fecha_nacimiento" : fecha_nacimiento,
                        "tipo" : tipo,
                        "raza" : raza,
                    }
            )
    return render_template("guardar.html", form=form)

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
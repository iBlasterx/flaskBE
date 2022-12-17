from flask import Flask, render_template, request
from app import client

app = Flask(__name__)
db = client['mi_base_de_datos']

@app.route('/register')
def register_form():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register_submit():
    username = request.form['username']
    password = request.form['password']
    
    db.users.insert_one({
        'username': username,
        'password': password
    })
    
    return 'Usuario registrado'
from flask import Blueprint, redirect, request, render_template, url_for
from flask_login import current_user, login_required, login_user, logout_user

from forms import LoginForm, SignupForm
from models import Users

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route("/auth/signup", methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("home", nombre=current_user.username))
    form = SignupForm()
    if request.method == 'POST' and form.validate_on_submit():
        existing_user = Users.objects(username=form.username.data).first()
        if existing_user is None:
            user = Users(username=form.username.data.lower())
            user.set_password(form.password.data)
            user.save()
            return redirect(url_for('login'))
    return render_template("signup.html", form=form)

@auth_bp.route("/auth/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home", nombre=current_user.username))
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = Users.objects(username=form.username.data).first()
        if user is not None and user.check_password(password=form.password.data):
            login_user(user)
            return redirect(url_for("home", nombre=user.username))
    return render_template("login.html", form=form)

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth_bp.login'))
from flask import Blueprint, render_template, url_for, redirect, session, request, flash, g

admin = Blueprint('admin', __name__, template_folder='templates', static_folder='static')


def login_admin():
    session['admin_logged'] = 1


@admin.route('/')
def index():
    return "admin"


@admin.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        if request.form['user'] == "admin" and request.form['psw'] == "12345":
            login_admin()
            return redirect(url_for('.index'))
        else:
            flash("Неверная пара логин/пароль", "error")

    return render_template('admin/login.html', title='Админ-панель')


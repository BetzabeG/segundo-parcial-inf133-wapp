from flask import render_template
from flask_login import current_user
def usuarios(users):
    return render_template("patients.html", users=users, title="LISTA DE PACIENTES",
        current_user=current_user,
    )

def registro():
    return render_template(
        "register.html", title="REGISTRO DE PACIENTES", current_user=current_user
    )

def actualizar(user):
    return render_template("update_patient.html", title="ACTUALIZAR PACIENTE", user=user,
        current_user=current_user,
    )

def login():
    return render_template(
        "login.html", title="Inicio de sesion", current_user=current_user
    )


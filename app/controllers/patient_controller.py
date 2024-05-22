from flask import Blueprint, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from models.patient_model import Patient
from views import patient_view
from utils.decorators import role_required

paciente_bp = Blueprint("paciente", __name__)


@paciente_bp.route("/patients")
@login_required
def list_patients():
    patients = Patient.get_all()
    return patient_view.list_patients(patients)


@paciente_bp.route("/patients/create", methods=["GET", "POST"])
@login_required
@role_required("admin")
def create_patient():
    if request.method == "POST":
        if current_user.has_role("admin"):
            name = request.form["name"]
            lastname = request.form["lastname"]
            ci = request.form["ci"]
            birth_date = request.form["birth_date"]
            paciente = Patient(name=name, lastname=lastname, ci=ci, birth_date=birth_date)
            paciente.save()
            flash("Paciente creado", "success")
            return redirect(url_for("paciente.list_patients"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return patient_view.create_patient()


@paciente_bp.route("/patients/<int:id>/update", methods=["GET", "POST"])
@login_required
@role_required("admin")
def update_patient(id):
    paciente = Patient.get_by_id(id)
    if not paciente:
        return "Paciente no encontrado", 404
    if request.method == "POST":
        if current_user.has_role("admin"):
            name = request.form["name"]
            lastname = request.form["lastname"]
            ci = request.form["ci"]
            birth_date = request.form["birth_date"]
            paciente.update(name=name, lastname=lastname, ci=ci, birth_date=birth_date)
            flash("Paciente actualizado exitosamente", "success")
            return redirect(url_for("paciente.list_patients"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return patient_view.update_patient(paciente)


@paciente_bp.route("/patients/<int:id>/delete")
@login_required
@role_required("admin")
def delete_patient(id):
    paciente = Patient.get_by_id(id)
    if not paciente:
        return "Paciente no encontrado", 404
    if current_user.has_role("admin"):
        paciente.delete()
        flash("Paciente eliminado exitosamente", "success")
        return redirect(url_for("paciente.list_patients"))
    else:
        return jsonify({"message": "Unauthorized"}), 403

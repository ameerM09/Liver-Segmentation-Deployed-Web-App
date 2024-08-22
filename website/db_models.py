from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class PatientScan(db.Model):
    id = db.Column(db.Integer, primary_key = True)

    # Stores the patient's name on record
    patient_name = db.Column(db.String(150), nullable = False)

    # Meant to store the specific type of cancer affiliated with the patient (e.g. liver, pancreatic, etc)
    patient_case_of_cancer = db.Column(db.String(150), nullable = False)

    # Meant to keep track of when each patient directory was created
    date_of_patient_scan = db.Column(db.DateTime(timezone = True), default = func.now())

    # Meant to keep track of the CT scans associated with each respective patient
    patient_scan_on_record = db.Column(db.String(150), nullable = True)

    account_id = db.Column(db.Integer, db.ForeignKey("account.id"))

class Account(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)

    # Enforces that no two accounts can hold the same associated email
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))

    patient_scans_on_account = db.relationship("PatientScan")
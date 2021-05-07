from flask import Flask, render_template, request, session, redirect
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'u8sAAN1FngnOJzKp-fME8NpDUfFm65r3XmYKWjw3Vs'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT']= False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['FLASK_APP'] = os.environ.get('FLASK_APP')
app.config['FLASK_ENV'] = os.environ.get('FLASK_ENV')


db = SQLAlchemy(app)

Session(app)

db.create_all()

class Patient:
    def __init__(self, firstname="", lastname="", id_number="", contact_number="", logged_by="", queue="", logged_time=""):
        self.firstname = firstname
        self.lastname = lastname
        self.id_number = id_number
        self.contact_number = contact_number
        self.logged_by = logged_by
        self.queue = queue 
        self.logged_time = logged_time

    def __lt__(self, other):
        if self.logged_by < other.logged_by:
            return other
        else:
            return self


class Staff:
    def __init__(self, firstname="", lastname="", contact_number="", hospital_code="", staff_code="", password=""):
        self.firstname = firstname
        self.lastname = lastname
        self.contact_number = contact_number
        self.hospital_code = hospital_code
        self.staff_code = staff_code
        self.password = password 

class Blank:
    pass 

patient_1 = Patient("Aviwe", "Ntloko", "8507310000000", "072 876 1234", "Lee-anne Matthews (AA78291)", "Registration", "7:21am")
patient_2 = Patient("Nazeem", "Parker", "7205020000000", "", "Lee-anne Matthews (AA78291)", "Vital Signs", "8:32am")
patient_3 = Patient("Warren", "Edwards", "9901020000000", "", "Lee-anne Matthews (AA78291)", "Doctor’s consultation", "8:56am")
patient_4 = Patient("Jade Marie", "Peters", "8906060000000", "", "Lee-anne Matthews (AA78291)", "Pharmacy", "9:13am")
patient_5 = Patient("Wade", "Peters", "8906060000000", "", "Lee-anne Matthews (AA78291)", "Pharmacy", "9:30am")

staff_1 = Staff("Lee-Anne", "Matthews", "080000000", "G29350GP", "AA78291", "12345")
staff_2 = Staff("Roger", "Hendricks", "0700000000", "G23423EC", "AA79234", "12345")
staff_3 = Staff("David", "Madison", "0600000000", "G23235KZN", "AA23523", "12345")


patient_list = [patient_1, patient_2, patient_3, patient_4, patient_5]
staff_list = [staff_1, staff_2, staff_3]

new_list = sorted(patient_list)
    

@app.route('/', methods=["GET", "POST"])
def index():
    session["hospital_code"] = "G29350GP"
    session["staff_code"] = "AA78291"
    session["password"] = "12345"
    if request.method == "POST":
        for x in staff_list:
            if x.hospital_code.casefold() == session["hospital_code"].casefold() and x.staff_code.casefold() == session["staff_code"].casefold() and x.password == session["password"]:
                return render_template('queues.html', user=x, len = len(patient_list), patient_list=patient_list)

    return render_template('index.html')

@app.route('/queues/', methods=["GET", "POST"])
def queue():
    x = staff_list[0]
    return render_template('queues.html', user=x, len = len(patient_list), patient_list=patient_list)

@app.route('/queues/registration', methods=["GET", "POST"])
def reg():
    x = staff_list[0]
    registration_queue = []
    for x in patient_list:
        if x.queue.casefold() == "Registration".casefold():
            registration_queue.append(x)
    return render_template('registration.html', user=x, len = len(registration_queue), registration_queue=registration_queue)

@app.route('/queues/vitals', methods=["GET", "POST"])
def vitals():
    x = staff_list[0]
    vitals_queue = []
    for x in patient_list:
        if x.queue.casefold() == "Vital Signs".casefold():
            vitals_queue.append(x)
    return render_template('vitals.html', user=x, len = len(vitals_queue), vitals_queue=vitals_queue)

@app.route('/queues/consultation', methods=["GET", "POST"])
def consultation():
    x = staff_list[0]
    consultation_queue = []
    for x in patient_list:
        if x.queue.casefold() == "Doctor’s consultation".casefold():
            consultation_queue.append(x)
    return render_template('consultation.html', user=x, len = len(consultation_queue), consultation_queue=consultation_queue)

@app.route('/queues/pharmacy', methods=["GET", "POST"])
def pharmacy():
    x = staff_list[0]
    pharmacy_queue = []
    for x in patient_list:
        if x.queue.casefold() == "Pharmacy".casefold():
            pharmacy_queue.append(x)
    return render_template('pharmacy.html', user=x, len = len(pharmacy_queue), pharmacy_queue=pharmacy_queue)

@app.route('/queues/other', methods=["GET", "POST"])
def other():
    x = staff_list[0]
    other_queue = []
    for x in patient_list:
        if x.queue.casefold() == "Other".casefold():
            other_queue.append(x)
    return render_template('other.html', user=x, len = len(other_queue), other_queue=other_queue)

@app.route('/add-patient', methods=["GET","POST"])
def add():
    x = staff_list[0]
    return render_template('add.html', user=x)

@app.route('/logout', methods=["GET", "POST"])
def logout():
    return redirect("/")

@app.route('/contact', methods=["GET", "POST"])
def contact():
    x = staff_list[0]
    return render_template("contact.html", user=x)

@app.route('/move-up', methods=["GET", "POST"])
def moveup():
    x = staff_list[0]
    return render_template('queues.html', len=len(patient_list), user=x, patient_list=patient_list)

@app.route('/move-down', methods=["GET", "POST"])
def movedown():
    x = staff_list[0]
    return render_template('queues.html', len=len(patient_list), user=x, patient_list=patient_list)

@app.route('/remove/{firstname}', methods=["GET", "POST"])
def remove():
    x = staff_list[0]
    return render_template('queues.html', len=len(patient_list), user=x, patient_list=patient_list)

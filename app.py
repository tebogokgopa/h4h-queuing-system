from flask import Flask, render_template, request, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_sqlalchemy import SQLAlchemy 
from flask_login import UserMixin, LoginManager, login_required, logout_user, login_user, current_user
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash
 
import os 

class RegisterForm(FlaskForm):
    firstName = StringField(label="First Name", validators=[DataRequired()])
    lastName = StringField(label="Last Name", validators=[DataRequired()])
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    condition = StringField(label="Condition")
    phone = StringField(label="Phone")
    password = PasswordField(label="Password")
    registerButton = SubmitField(label="Register")

class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired()])
   

app = Flask(__name__)

app.config['SECRET_KEY'] = 'u8sAAN1FngnOJzKp-fME8NpDUfFOm65r3XmYKWjw3Vs'

class Patient:
    def __init__(self, firstname="", lastname="", id_number="", contact_number="", logged_by="", queue=""):
        self.firstname = firstname
        self.lastname = lastname
        self.id_number = id_number
        self.contact_number = contact_number
        self.logged_by = logged_by
        self.queue = queue 
    
  

patient_1 = Patient("Aviwe", "Ntloko", "8507310000000", "072 876 1234", "Lee-anne Matthews (AA78291)", "Registration")
patient_2 = Patient("Nazeem", "Parker", "7205020000000", "", "Lee-anne Matthews (AA78291)", "Vital Signs")
patient_3 = Patient("Warren", "Edwards", "9901020000000", "", "Lee-anne Matthews (AA78291)", "Doctor’s consultation")
patient_4 = Patient("Jade Marie", "Peters", "8906060000000", "", "Lee-anne Matthews (AA78291)", "Pharmacy")
patient_5 = Patient("Wade", "Peters", "8906060000000", "", "Lee-anne Matthews (AA78291)", "Pharmacy")

patient_list = [patient_1, patient_2, patient_3, patient_4, patient_5]


@app.route('/', methods=["GET", "POST"])
def index():
    form = LoginForm()
    return render_template("index.html", form=form)

@app.route('/queues', methods=["GET", "POST"])
def queue():
    return render_template("queues.html", patient_list=patient_list)

@app.route('/add-patient', methods=["GET", "POST"])
def add():
    return render_template("add.html")

@app.route('/login', methods=["GET", "POST"] )
def login():
    form = LoginForm()
    return render_template("login.html", form=form)

@app.route('/signup', methods=["GET", "POST"] )
def signup():
    form = RegisterForm()
    return render_template("signup.html", form=form)

@app.route('/demo', methods=["GET", "POST"] )
def demo():
    return render_template("demo.html")

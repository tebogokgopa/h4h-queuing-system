from flask import Flask, render_template, request, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_sqlalchemy import SQLAlchemy 
from flask_login import UserMixin, LoginManager, login_required, logout_user, login_user, current_user
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash

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

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://b3c105d8-7951-9:f3d2734e-6e45-2@https://h4h-queuing-system-edsnwb.codecapsules.co.za/data-capsule-zgmfcr"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

db.create_all()

#csrf = CSRFProtect(app)

#login_manager = LoginManager()
#login_manager.session_protection = 'strong'
#login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(80), primary_key=True)
    firstname = db.Column(db.String(80), unique=False, nullable=False)
    lastname = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(120), unique=True, nullable=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.firstname


@app.route('/', methods=["GET", "POST"])

def index():
    form = LoginForm()
    return render_template("index.html", form=form)

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
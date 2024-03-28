from flask import Flask, redirect, render_template, request, session
from flask_session import Session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

# Don't update automatically each refresh
app.config['SESSION_REFRESH_EACH_REQUEST'] = False

# Don't store in cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

Session(app)

# If changes here, change also layout.html
HEADERiTEMS = [
    "Home",
    "Clases de Yoga",
    "Psiconutrición",
    "Psicologia"
]

# HOME PAGE
@app.route("/")
def home():
    return render_template ("home-esp.html")

# PSICONUTRICION
@app.route("/psiconutricion")
def psiconutricion():
    return render_template("psiconutricion-esp.html")

# PSICOLOGIA
@app.route("/psicologia")
def psicologia():
    return render_template("psicologia-cat.html")


# Clases de Yoga
@app.route("/clases-de-yoga")
def clasesYoga():
    return render_template("clasesYoga-cat.html")

# Yoga para embarazadas
@app.route("/yoga-para-embarazadas")
def yogaEmbarazadas():
    return render_template("yogaEmbarazadas.html")

# Yoga infantil
@app.route("/yoga-infantil")
def yogaInfantil():
    return render_template("yogaInfantil.html")

# Yoga postnatal
@app.route("/yoga-postnatal")
def yogaPostnatal():
    return render_template("yogaPostnatal.html")

# 404 NOT FOUND Entrena tu mente cuida tu cuerpo
@app.route("/entrena-tu-mente-cuida-tu-cuerpo")
def entrenaMenteCuidaCuerpo():
    return render_template ("entrenaCuida.html")

# Lo que nos importa
@app.route("/sobre-mes-millor")
def sobreMesMillor():
    return render_template ("sobreMesMillor-cat.html")
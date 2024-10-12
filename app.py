import sys
import os
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from flask_frozen import Freezer

# Configure application
app = Flask(__name__)
freezer = Freezer(app)

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
# "" Para github, "." para local
baseUri = ""

@app.route("/")
def home0():
    return redirect ("/es/")
# HOME PAGE
@app.route("/es/")
def home():
    return render_template ("home-esp2.html", baseUri=baseUri)


# PSICONUTRICION
@app.route("/es/psiconutricion")
def psiconutricion():
    return render_template("psiconutricion-esp.html")

# PSICOLOGIA
@app.route("/ca/psicologia")
def psicologia():
    return render_template("psicologia-cat.html")


# Clases de Yoga
@app.route("/ca/clases-de-yoga")
def clasesYoga():
    return render_template("clasesYoga-cat.html")

""" # Yoga para embarazadas
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
@app.route("/ca/sobre-mes-millor")
def sobreMesMillor():
    return render_template ("sobreMesMillor-cat.html") """

if __name__ == '__main__':
    # Esta condición es importante para asegurarse de que la aplicación se ejecute
    # correctamente tanto cuando se ejecuta como una aplicación Flask en vivo
    # como cuando se genera estáticamente con Frozen-Flask.
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
    else:
        app.run(debug=True)
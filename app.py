import sys
from flask import Flask, redirect, render_template, request, session, url_for, render_template_string
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
# Definir la variable global base_uri
base_uri = "es"

@app.route('/')
def home():
    return redirect("/es")

@app.route('/<string:base_uri>')
# def index(base_uri=None):
def index(base_uri):
    if base_uri == 'es':
        return render_template("home-esp.html")
    elif base_uri == 'ca':
        return render_template('home-cat.html')
    
@app.route('/<string:base_uri>/psiconutricion')
def psiconutricion(base_uri):
    if base_uri == 'es':
        return render_template('psiconutricion-esp.html')
    elif base_uri == 'ca':
        return render_template('psiconutricio-cat.html')


# PSICOLOGIA
@app.route("/<string:base_uri>/psicologia")
def psicologia(base_uri):
    if base_uri == 'es':
        return render_template('psicologia-esp.html')
    elif base_uri == 'ca':
        return render_template('psicologia-cat.html')


# Clases de Yoga
@app.route("/<string:base_uri>/clases-de-yoga")
def clasesYoga(base_uri):
    if base_uri == 'es':
        return render_template('clasesYoga-esp.html')
    elif base_uri == 'ca':
        return render_template('clasesYoga-cat.html')

# Yoga para embarazadas
@app.route("/<string:base_uri>/yoga-para-embarazadas")
def yogaEmbarazadas(base_uri):
    if base_uri == 'es':
        return render_template('yogaEmbarazadas-esp.html')
    elif base_uri == 'ca':
        return render_template('iogaEmbarassades-cat.html')

""" # Yoga infantil
@app.route("/yoga-infantil")
def yogaInfantil():
    return render_template("yogaInfantil.html") """

# Yoga postnatal
@app.route("/<string:base_uri>/yoga-postnatal")
def yogaPostnatal(base_uri):
    if base_uri == 'es':
        return render_template('yogaPostnatal-esp.html')
    elif base_uri == 'ca':
        return render_template('iogaPostnatal-cat.html')

# 404 NOT FOUND Entrena tu mente cuida tu cuerpo
@app.route("/<string:base_uri>/entrena-tu-mente-cuida-tu-cuerpo")
def entrenaMenteCuidaCuerpo(base_uri):
    if base_uri == 'es':
        return render_template('entrenaCuida-esp.html')
    elif base_uri == 'ca':
        return render_template('entrenaCuida-cat.html')

# Lo que nos importa
@app.route("/<string:base_uri>/sobre-mes-millor")
def sobreMesMillor(base_uri):
    if base_uri == 'es':
        return render_template('sobreMesMillor-esp.html')
    elif base_uri == 'ca':
        return render_template('sobreMesMillor-cat.html')

if __name__ == '__main__':
    # Esta condición es importante para asegurarse de que la aplicación se ejecute
    # correctamente tanto cuando se ejecuta como una aplicación Flask en vivo
    # como cuando se genera estáticamente con Frozen-Flask.
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
    else:
        app.run(debug=True)

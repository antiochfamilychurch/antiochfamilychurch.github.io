from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage"""
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/whoweare')
def whoweare():
    return render_template("who_we_are.html")

@app.route('/services')
def services():
    return render_template("services.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/visitus')
def visitus():
    return render_template("visitus.html")

@app.route('/espanol')
def espanol():
    return render_template("inicio.html")

@app.route('/inicio')
def inicio():
    return render_template("inicio.html")

@app.route('/quienes')
def quienes():
    return render_template("quienes.html")

@app.route('/servicios')
def servicios():
    return render_template("servicios.html")

@app.route('/contactenos')
def contactenos():
    return render_template("contactenos.html")

@app.route('/visitenos')
def visitenos():
    return render_template("visitenos.html")

if __name__ == "__main__":
    app.debug = True
    app.run(port=5000, host='0.0.0.0')
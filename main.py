from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<a href="/miRuta">Siguiente ruta</a>'

@app.route("/miRuta")
def rutaMia():
    return 'Mi propia ruta'

app.run(debug=True)
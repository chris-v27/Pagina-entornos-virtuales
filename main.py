from flask import Flask
import random

app = Flask(__name__)

facts_list = ["La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos",
              "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones",
              "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna",
              "Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo",
              "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo",
              "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas",
              ]

@app.route("/")
def hello_world():
    return '<h1>Esta página da datos interesantes sobre las dependencias tecnológicas</h1> <a href="/random_fact">¡Ver un dato aleatorio!</a> <a href="/flip_coin">Lanzamiento de moneda</a>'
    
@app.route("/random_fact")
def datos():
    return f'<p>{random.choice(facts_list)}</p> <a href="/">Regresar a la pagina principal</a>'

@app.route("/flip_coin")
def flip_coin():
    side = random.randint(1,2)
    if side == 1:
        side = 'Cara'
    elif side == 2: 
        side = 'Cruz'
    return f'<p>{side}</p> <a href="/">Regresar a la pagina principal</a>'

app.run(debug=True)
from flask import Flask, request, render_template


app = Flask(__name__)

# RUTAS
@app.route('/', methods=['GET', 'POST'])
def raiz():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        tarifa_diaria = request.form['tarifa_diaria']
        distancia_casa = request.form['distancia_casa']
        nivel_educativo = request.form['nivel_educativo']
        experiencia = request.form['experiencia']
        balance = request.form['balance']
        viajes_negocios = request.form['viajes_negocios']
        dependencia = request.form['dependencia']
        ambito_educativo = request.form['ambito_educativo']

        #return render_template('resultado.html', nombre=nombre, edad=edad)
    return render_template('index.html')

#Bloque de prueba
if __name__== "__main__":
    app.run(debug = True)
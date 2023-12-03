from flask import Flask, render_template


app = Flask(__name__)

# RUTAS
@app.route('/')
def raiz():
    return render_template('index.html')

#ruta para nosotros
@app.route('/base')
def base():
    return render_template('base.html')

#Bloque de prueba
if __name__== "__main__":
    app.run(debug=True)
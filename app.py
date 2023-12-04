from flask import Flask, request, render_template
from backend import proyecto_final as pf

app = Flask(__name__)

# RUTAS
@app.route('/', methods=['GET', 'POST'])
def raiz():
    model = pf.Modelo()

    if request.method == 'POST':
        BussinessTravel_Non_Travel = 0
        BusinessTravel_Travel_Frequently = 0
        BusinessTravel_Travel_Rarely = 0
        Department_Human_Resources = 0
        Department_Research_Development = 0
        Department_Sales = 0
        EducationField_Human_Resources = 0
        EducationField_Life_Sciences = 0
        EducationField_Marketing = 0
        EducationField_Medical = 0
        EducationField_Other = 0
        EducationField_Technical_Degree = 0

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

        #VIAJES
        if(viajes_negocios == "No viaja"):
            BussinessTravel_Non_Travel = 1
        elif(viajes_negocios == "Viaja Frecuentemente"):
            BusinessTravel_Travel_Frequently = 1
        elif(viajes_negocios == "Raramente viaja"):
            BusinessTravel_Travel_Rarely = 1
        
        #DEPENDENCIA
        if(dependencia == "Recursos Humanos"):
            Department_Human_Resources = 1
        elif(dependencia == "Investigación y Desarrollo"):
            Department_Research_Development = 1
        elif(dependencia == "Ventas"):
            Department_Sales = 1

        #CAMPO EDUCATIVO
        if(ambito_educativo == "Recursos Humanos"):
            EducationField_Human_Resources = 1
        elif(ambito_educativo == "Ciencias de la vida"):
            EducationField_Life_Sciences = 1
        elif(ambito_educativo == "Marketing"):
            EducationField_Marketing = 1
        elif(ambito_educativo == "Medicina"):
            EducationField_Medical = 1
        elif(ambito_educativo == "Otro"):
            EducationField_Other = 1
        elif(ambito_educativo == "Titulación técnica"):
            EducationField_Technical_Degree = 1
        
        data = [edad, tarifa_diaria, distancia_casa, nivel_educativo, experiencia, balance, BussinessTravel_Non_Travel, 
                        BusinessTravel_Travel_Frequently, BusinessTravel_Travel_Rarely, Department_Human_Resources, Department_Research_Development, 
                        Department_Sales, EducationField_Human_Resources, EducationField_Life_Sciences, EducationField_Marketing, EducationField_Medical,
                        EducationField_Other, EducationField_Technical_Degree]
        
        resultado = model.consultar(data)
        return render_template('resultado.html', nombre=nombre, resultado=resultado)
    return render_template('index.html')

#Bloque de prueba
if __name__== "__main__":
    app.run(debug = True)
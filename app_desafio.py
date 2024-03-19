#==============================================================================================================================
# ESTE ES EL CUERPO DE LA APP 
# ACCIONES QUE SE REALIZARÁN EN LAS ESTANCIAS DEFINIDAS:
#    
#    Implementacion de modelo de ML elegido y visualizacion de su predicción a traves de un paquete de datos json
#    que estara en un tercer script que llamaremos ataque (opcion requests de peticiones)
#          
#===============================================================================================================================

from flask import Flask, request, jsonify
import pickle
import pandas as pd
import numpy as np
import csv, sqlite3, json

app = Flask(__name__)
app.config["DEBUG"] = True

#===============================================================================================================================
# Endpoint HOME 

@app.route('/', methods=['GET'])
def home():
    return "<h1>Prueba Desafío Andrada</h1>"


#===============================================================================================================================
# Endpoint de VERIFICACION DE FUNCIONAMIENTO de mi app
 
@app.route('/health/', methods=['GET'])
def health():
    return "todo bien chamigo"


# ==============================================================================================================================
# [2] PREDICCION  2 --> ( Empleamos el mismo modelo,pero pasando los datos a traves de un script + requests + [POST] )
# ==============================================================================================================================

@app.route('/api/', methods=['POST']) # <-- Esta info me viene del requests
def makecalc():
    data = request.get_json() # tomo los valores que tengo en mi json y los guardo en data
    # ubicacion = data[ubicacion]
    # maquina = data[maquina]
    # producto = data[producto]
    # fecha = data[fecha]
    # data_procesado = algo que depende de ubicacion, maquina, producto, fecha

    # prediction = model.predict(data_procesado)
    prediction = model.predict(data)
    dict_result = {
        'lunes' : prediction[0],
        'martes' : prediction[1],
        'miercoles' : prediction[2],
        'jueves' : prediction[3],
        'viernes' : prediction[4],
        'sabado' : prediction[5],
        'domingo' : prediction[6],                
    }
    
    return jsonify(dict_result)


modelfile = r'/home/ubuntu/prod/endpoint/model_linreg.pkl'  # ruta a donde tenemos el modelo guardado (Nube amazon?)
model = pickle.load(open(modelfile, 'rb'))

if __name__ == "__main__":
    print("hello")
    app.run(debug=False)


app.run()
from flask import Flask, render_template, jsonify, request
import numpy as np
from joblib import load
import os

#Cargar el modelo 
dt = load("dt1.joblib")

servidorWeb = Flask(__name__)
@servidorWeb.route("/holamundo",methods = ['GET'])
def holamundo():
    return render_template('pagina1.html')

#Envio de datos a través de JSON
@servidorWeb.route("/modelo", methods=['POST'])
def modeloPrediccion():
    #Procesar los datos
    contenido = request.json #Para extraer la información que le estamos dando
    print(contenido)
    return jsonify({"resultado":"Hola"})

if __name__ == '__main__':
    servidorWeb.run(debug=False, host = '0.0.0.0', port ='8080')
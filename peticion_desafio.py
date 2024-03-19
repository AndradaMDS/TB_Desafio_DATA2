import requests
import json
import numpy as np

# data = [[2010, 1.3, 0.1, 0.22],  #Año 2010, ventas NA = 1.3M , ventas JP = 0.1M y ventas resto del mundo = 0.22
# [2023, 1.5, 0.2, 0.3]]           #Año 2023, ventas NA = 1.5M , ventas JP = 0.2M y ventas resto del mundo = 0.3                                                           
# j_data = json.dumps(data) 
# print(j_data)
# print(type(j_data))

# Aquí va la url de nuestra API de nuestra intancia EC2 de AWS
url = "http://13.53.171.181/api"  

# Aquí va la url que nos proporcionen los de fullstack
# j_data = './peticion_prueba.json'  

array = np.array([[2., 6., 2., 4., 1., 1.],
                  [2., 0., 2., 0., 3., 5.],
                  [4., 1., 0., 0., 2., 4.],
                  [0., 2., 0., 1., 4., 3.],
                  [1., 1., 0., 6., 5., 4.],
                  [1., 4., 3., 4., 2., 0.],
                  [0., 4., 1., 3., 4., 1.]])
j_data = json.dumps(array)

headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

r = requests.post(url, data=j_data, headers=headers) 

# Se guarda el resultado de la prediccion en un json en la misma carpeta
with open('./respuesta_desafio', 'w') as file:
    json.dump(r, file) 

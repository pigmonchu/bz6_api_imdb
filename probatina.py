import requests

direccion = "http://www.omdbapi.com/?apikey=da22215a1&i=tt3896198" #url a la que quiero llamar

#hacer petición HTTP
respuesta = requests.get(direccion)

if respuesta.status_code == 200:
    print(respuesta.text)
    datos = respuesta.json()
    print(datos)
else:
    print("Se ha producido un error", respuesta.status_code)


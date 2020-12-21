import requests

API_KEY="da22215 a"
#TODO - Arreglar urls para evitar tanta repeticion
url_template = "http://www.omdbapi.com/?apikey={}&{}={}"

class PeticionError(Exception):
    pass

def peticion(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        if datos['Response'] == "False":
            raise PeticionError(datos["Error"])
        else: 
            return datos
    else: 
        raise PeticionError("Error en consulta: {}".format(respuesta.status_code))

repetir = 'S'
while repetir == 'S' or repetir == 's':
    try:
        pregunta = input("Titulo de la película: ")
        respuesta = peticion(url_template.format(API_KEY, 's', pregunta))
        primera_peli = respuesta['Search'][0]
        clave = primera_peli['imdbID']

        respuesta = peticion(url_template.format(API_KEY, 'i', clave))
        titulo = respuesta['Title']
        agno = respuesta['Year']
        director = respuesta ['Director']
        print("La peli '{}', estrenada en el año {}, fue dirigida por {}".format(titulo, agno, director))

        repetir = input('Otra peli (S/N)? ')

    except PeticionError as e:
        print(e)




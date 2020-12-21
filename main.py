import requests

API_KEY="da22215a"
#TODO - Arreglar urls para evitar tanta repeticion
url_template = "http://www.omdbapi.com/?apikey={}&{}={}"

def peticion(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        if datos['Response'] == "False":
            return datos["Error"]
        else: 
            return datos
    else: 
        return "Error en consulta por id:" + respuesta.status_code

repetir = 'S'
while repetir == 'S':
    pregunta = input("Titulo de la película: ")

    respuesta = peticion(url_template.format(API_KEY, 's', pregunta))
    if isinstance(respuesta, str):
        print(respuesta)
    else:
        primera_peli = respuesta['Search'][0]
        clave = primera_peli['imdbID']

        respuesta = peticion(url_template.format(API_KEY, 'i', clave))
        if isinstance(respuesta, str):
            print(respuesta)
        else:
            titulo = respuesta['Title']
            agno = respuesta['Year']
            director = respuesta ['Director']
            print("La peli {}, estrenada en el año {}, fue dirigida por {}".format(titulo, agno, director))

    repetir = input('Quieres otra peli? (S/N) ')
    repetir = repetir.upper()

from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import pandas as pd
import ast

#creo la app FastApi
app = FastAPI(title = "Consultas peliculas")

#http://127.0.0.1:8000
@app.get("/")
def index():
    return {"messsage" : "hola, den"}



# Mapeo de meses en español a números de mes
meses_espanol = {
    'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5, 'junio': 6,
      'julio': 7,  'agosto': 8, 'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12
}
# Mapeo de dias en español a números de mes
dias_espanol = {
    'lunes' :1 , 'martes': 2, 'miercoles' : 3, 'jueves' :4, 'viernes':5, 'sabado':6, 'domingo':7
}





#consultas

@app.get("/score_titulo")
def score_titulo(titulo: str):
    #dataframe 
    data=pd.read_csv(r'D:\Denise_Estudio\henry\PI\datos\movies_data.csv')
    movie = data[data['title'].str.lower() == titulo.lower()]
    # Obtener los detalles de la película
    anio_estreno = movie.iloc[0]['release_year']
    score = movie.iloc[0]['popularity']
    return f"La película {titulo} fue estrenada en el año {anio_estreno} con un score de {score}"


''' def cantidad_filmaciones_mes( Mes ): Se ingresa un mes en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en el mes consultado en la totalidad del dataset.
                    Ejemplo de retorno: X cantidad de películas fueron estrenadas en el mes de X '''
@app.get("/filmaciones_mes")
def cantidad_filmaciones_mes( mes ):
    mes = mes.lower()
    data=pd.read_csv(r'D:\Denise_Estudio\henry\PI\datos\movies_data.csv')
    #paso a datatime
    data['release_date'] = pd.to_datetime(data['release_date'], errors='coerce')
    #encontrar nro de mes
    mes_numero = meses_espanol[mes]
    #filtrar parametros por mes
    cantidad = data[data['release_date'].dt.month == mes_numero].shape[0]
    return f"{cantidad} cantidad de películas fueron estrenadas en el mes de {mes}"



'''def cantidad_filmaciones_dia( Dia ): Se ingresa un día en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en día consultado en la totalidad del dataset.
                    Ejemplo de retorno: X cantidad de películas fueron estrenadas en los días X'''
@app.get("/filmaciones_dia")
def cantidad_filmaciones_dia( dia ):
    dia=dia.lower()
    data= pd.read_csv(r'D:\Denise_Estudio\henry\PI\datos\movies_data.csv')
    #paso a datatime
    data['release_date'] = pd.to_datetime(data['release_date'], errors='coerce')
    nro_dia = dias_espanol[dia]
    #filtrar
    cantidad = data[data['release_date'].dt.day_of_week == nro_dia].shape[0]
    return f"{cantidad} cantidad de películas fueron estrenadas en los días {dia}"

print(cantidad_filmaciones_dia("lunes"))

'''def votos_titulo( titulo_de_la_filmación ): Se ingresa el título de una filmación esperando como respuesta el título,
 la cantidad de votos y el valor promedio de las votaciones. La misma variable deberá de contar con al menos 2000 
 valoraciones, o contar con un mensaje avisando que no cumple esta condición y que por ende,  no se devuelve ningun valor.
    Ejemplo La película X fue estrenada en el año X. La misma cuenta con un total de X valoraciones, con un promedio de X
'''
@app.get("/votos_titulo")
def votos_titulo( titulo):
    titulo = titulo.lower()
    data=pd.read_csv(r'D:\Denise_Estudio\henry\PI\datos\movies_data.csv')
    #voy a la fila
    movie = data[data['title'].str.lower() == titulo]
    #tomo cantidad de votos y verifico que sea mayor a 2000  'vote_count'
    cantidad_votos = movie.iloc[0]['vote_count']
    if not cantidad_votos>= 2000:
        return f"la pelicula {titulo} no posee las valoraciones suficientes"
    else:
        promedio_votos = movie.iloc[0]['vote_average']
        anio_estreno = movie.iloc[0]['release_year']
        return f"La película {titulo} fue estrenada en el año {anio_estreno}. La misma cuenta con un total de {cantidad_votos} valoraciones, con un promedio de {promedio_votos}"

'''def get_actor( nombre_actor ): Se ingresa el nombre de un actor que se encuentre dentro de un dataset debiendo devolver
 el éxito del mismo medido a través del retorno. Además, la cantidad de películas que en las que ha participado y 
 el promedio de retorno. La definición no deberá considerar directores.
    Ejemplo de retorno: El actor X ha participado de X cantidad de filmaciones, el mismo ha conseguido un 
    retorno de X con un promedio de X por filmación'''

# Función para convertir una cadena separada por comas en una lista de nombres
def convertir_a_lista(cadena):
    if pd.isna(cadena):
        return []
    return [nombre.strip().lower() for nombre in cadena.split(',')]

@app.get("/actor")
def get_actor(nombre_actor: str):
    nombre_actor = nombre_actor.lower()

    # Leer el dataset
    data = pd.read_csv(r'D:\Denise_Estudio\henry\PI\datos\movies_data.csv')

    # Convertir la columna 'cast' a lista de nombres limpiados
    if 'cast_clean' in data.columns:
        data['cast_clean'] = data['cast_clean'].apply(convertir_a_lista)

    # Filtrar las películas en las que ha participado el actor
    peliculas_actor = data[data['cast_clean'].apply(lambda cast: nombre_actor in cast)]

    # Calcular el retorno total
    retorno_total = peliculas_actor['return'].sum()

    # Cantidad de películas
    cantidad_peliculas = peliculas_actor.shape[0]

    # Promedio de retorno
    promedio_retorno = retorno_total / cantidad_peliculas if cantidad_peliculas > 0 else 0

    # Convertir a tipos de datos nativos de Python
    retorno_total = float(retorno_total)
    promedio_retorno = float(promedio_retorno)

    return {
        "actor": nombre_actor,
        "cantidad_peliculas": cantidad_peliculas,
        "retorno_total": retorno_total,
        "promedio_retorno": promedio_retorno
    }

# Función para calcular el retorno (ganancia / costo)
#def calcular_retorno(row):
#    return row['return'] / row['budget'] if row['budget'] != 0 else 0

# Función para obtener detalles de las películas de un director
@app.get("/director")
def get_director(nombre_director):
    nombre_director = nombre_director.lower()

    # Leer el dataset
    data = pd.read_csv(r'D:\Denise_Estudio\henry\PI\datos\movies_data.csv')

    # Filtrar las películas del director específico
    peliculas_director = data[data['director'].str.lower() == nombre_director]

    # Usar la columna 'return' para el retorno individual
    peliculas_director['retorno_individual'] = peliculas_director['return']

    # Preparar la salida
    detalles_peliculas = []
    for index, row in peliculas_director.iterrows():
        detalle_pelicula = {
            "nombre_pelicula": row['title'],
            "fecha_lanzamiento": row['release_date'],
            "retorno_individual": float(row['retorno_individual']),
            "costo": float(row['budget']),
            "ganancia": float(row['revenue'])
        }
        detalles_peliculas.append(detalle_pelicula)

    # Calcular el éxito del director (retorno total de todas las películas)
    retorno_total = peliculas_director['return'].sum()

    # Convertir a tipos de datos nativos de Python
    retorno_total = float(retorno_total)

    return {
        "director": nombre_director,
        "detalles_peliculas": detalles_peliculas,
        "retorno_total": retorno_total
    }

#print(get_actor("Tom Hanks"))

#testing
#print(score_titulo("toy story"))
#print(cantidad_filmaciones_mes("enero"))
#print(votos_titulo("toy story"))
#print(get_actor("Tom Hanks"))
from fastapi import fastapi, httpexception
from pydantic import basemodel
import pandas as pd
import ast
import gc
from funciones_main import score_titulo, cantidad_filmaciones_mes, cantidad_filmaciones_dia, votos_titulo, get_actor, get_director
from sklearn.feature_extraction.text import tfidfvectorizer
from sklearn.metrics.pairwise import linear_kernel

#creo la app fastapi
app = fastapi(title="consultas peliculas")

#defino las rutas de los archivos
movies_data_path = "datos/movies_data.csv"
muestra_data_path = "datos/muestra.csv"

#función para cargar el dataframe de películas
def load_movies_data():
    return pd.read_csv(movies_data_path)

#función para cargar el dataframe de muestra
def load_muestra_data():
    muestra = pd.read_csv(muestra_data_path)
    valid_columns = ['title', 'genres_clean', 'companies_names', 'director', 'overview']
    muestra = muestra[valid_columns].fillna("")
    muestra['combined'] = muestra['genres_clean'] + ' ' + muestra['companies_names'] + ' ' + muestra['director']
    return muestra

#inicialización del tf-idf y matriz de similitud coseno
muestra = load_muestra_data()
tfidf = tfidfvectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(muestra['combined'])
cosine_similarity = linear_kernel(tfidf_matrix, tfidf_matrix)

@app.get("/")
def index():
    return {"message": "hola, este es mi proyecto"}

@app.get("/score_titulo")
def get_score_titulo(titulo: str):
    df = load_movies_data()
    resultado = score_titulo(titulo, df)
    del df
    gc.collect()
    return resultado

@app.get("/filmaciones_mes")
def get_cantidad_filmaciones_mes(mes):
    df = load_movies_data()
    resultado = cantidad_filmaciones_mes(mes, df)
    del df
    gc.collect()
    return resultado

@app.get("/filmaciones_dia")
def get_cantidad_filmaciones_dia(dia):
    df = load_movies_data()
    resultado = cantidad_filmaciones_dia(dia, df)
    del df
    gc.collect()
    return resultado

@app.get("/votos_titulo")
def get_votos_titulo(titulo):
    df = load_movies_data()
    resultado = votos_titulo(titulo, df)
    del df
    gc.collect()
    return resultado

@app.get("/actor")
def get_get_actor(nombre_actor: str):
    df = load_movies_data()
    resultado = get_actor(nombre_actor, df)
    del df
    gc.collect()
    return resultado

@app.get("/director")
def get_get_director(nombre_director):
    df = load_movies_data()
    resultado = get_director(nombre_director, df)
    del df
    gc.collect()
    return resultado

@app.get("/recomendacion")
def recomendacion_movie(title: str):
    title = title.lower()
    if title not in muestra['title'].values:
        return {'mensaje': 'no hay datos de la pelicula'}
    
    idx = muestra[muestra['title'] == title].index[0]
    sim_cosine = list(enumerate(cosine_similarity[idx]))
    sim_scores = sorted(sim_cosine, key=lambda x: x[1], reverse=True)
    sim_ind = [i for i, _ in sim_scores[1:6]]
    sim_movies = muestra['title'].iloc[sim_ind].values.tolist()
    return {f'peliculas recomendadas para {title}': list(sim_movies)}

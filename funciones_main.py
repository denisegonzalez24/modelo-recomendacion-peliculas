import pandas as pd

# Mapeo de meses en español a números de mes
meses_espanol = {
    'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5, 'junio': 6,
    'julio': 7, 'agosto': 8, 'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12
}

# Mapeo de días en español a números de mes
dias_espanol = {
    'lunes': 1, 'martes': 2, 'miércoles': 3, 'jueves': 4, 'viernes': 5, 'sábado': 6, 'domingo': 7
}

def score_titulo(titulo: str, df):
    movie = df[df['title'].str.lower() == titulo.lower()]
    if not movie.empty:
        anio_estreno = movie.iloc[0]['release_year']
        score = movie.iloc[0]['popularity']
        score_formatted = f"{score:.3f}"  # Formato con tres cifras significativas
        return f"La película {titulo} fue estrenada en el año {anio_estreno} con un score de {score_formatted}"
    else:
        return f"No se encontró información para la película {titulo}"
    
def cantidad_filmaciones_mes(mes, df):
    mes = mes.lower()
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    mes_numero = meses_espanol.get(mes)
    if mes_numero is None:
        return f"Mes {mes} no válido"
    cantidad = df[df['release_date'].dt.month == mes_numero].shape[0]
    return f"{cantidad} cantidad de películas fueron estrenadas en el mes de {mes}"

def cantidad_filmaciones_dia(dia, df):
    dia = dia.lower()
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    nro_dia = dias_espanol.get(dia)
    if nro_dia is None:
        return f"Día {dia} no válido"
    cantidad = df[df['release_date'].dt.day_of_week == nro_dia].shape[0]
    return f"{cantidad} cantidad de películas fueron estrenadas en los días {dia}"

def votos_titulo(titulo: str, df):
    titulo = titulo.lower()
    movie = df[df['title'].str.lower() == titulo]
    if movie.empty:
        return f"No se encontró la película con el título {titulo}"
    cantidad_votos = int(movie.iloc[0]['vote_count'])  # Convertir a entero
    if cantidad_votos < 2000:
        return f"La película {titulo} no posee las valoraciones suficientes"
    promedio_votos = movie.iloc[0]['vote_average']
    anio_estreno = movie.iloc[0]['release_year']
    return f"La película {titulo} fue estrenada en el año {anio_estreno}. La misma cuenta con un total de {cantidad_votos} valoraciones, con un promedio de {promedio_votos}"

def convertir_a_lista(cadena):
    if pd.isna(cadena):
        return []
    return [nombre.strip().lower() for nombre in cadena.split(',')]

def get_actor(nombre_actor: str, df):
    nombre_actor = nombre_actor.lower()
    if 'cast_clean' in df.columns:
        df['cast_clean'] = df['cast_clean'].apply(convertir_a_lista)
    peliculas_actor = df[df['cast_clean'].apply(lambda cast: nombre_actor in cast)]
    peliculas_actor = peliculas_actor[~peliculas_actor['director'].apply(lambda director: nombre_actor in director)]
    if peliculas_actor.empty:
        return f"No se encontraron películas donde el actor {nombre_actor} participara como actor y no fuera director."
    peliculas_actor = peliculas_actor[['return']].dropna()
    retorno_total = peliculas_actor['return'].sum()
    cantidad_peliculas = peliculas_actor.shape[0]
    promedio_retorno = retorno_total / cantidad_peliculas if cantidad_peliculas > 0 else 0
    retorno_total = float(retorno_total)
    promedio_retorno = round(float(promedio_retorno))
    return f"El actor {nombre_actor} ha participado en {cantidad_peliculas} películas, con un retorno total de {retorno_total} y un promedio de retorno de {promedio_retorno} por película."

def get_director(nombre_director, df):
    nombre_director = nombre_director.lower()
    peliculas_director = df[df['director'].str.lower() == nombre_director]
    if peliculas_director.empty:
        return f"No se encontraron películas del director {nombre_director}"
    peliculas_director['retorno_individual'] = peliculas_director['return']
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
    retorno_total = peliculas_director['return'].sum()
    retorno_total = float(retorno_total)
    return {
        "director": nombre_director,
        "detalles_peliculas": detalles_peliculas,
        "retorno_total": retorno_total
    }

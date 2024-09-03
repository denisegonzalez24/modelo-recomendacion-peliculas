

# <h1 align=center> Proyecto de Recomendación de Películas </h1>

<p align=center><img src=https://img.freepik.com/premium-vector/video-camera-icon-comic-style-movie-play-vector-cartoon-illustration-pictogram-video-streaming-business-concept-splash-effect_157943-5803.jpg?w=200><p>
  
¡Bienvenidx a mi Proyecto de Recomendación de Películas! En esta ocasión, me he situado en el rol de un MLOps Engineer para desarrollar un sistema de recomendación de películas.

  
## Descripción del problema

<details>
  <summary>Contexto</summary>
  El ciclo de vida de un proyecto de Machine Learning debe incluir desde el tratamiento y recolección de los datos hasta el entrenamiento y mantenimiento del modelo de ML según llegan nuevos datos.
</details>


  <summary>Rol a desarrollar</summary>
Pensado para una plataforma de streaming. Se realizará un modelo de ML que soluciona un problema de negocio: un sistema de recomendación que aún no ha sido puesto en marcha.

  Luego de la obtención, se observa que la madurez de los datos es problemática, se encuentran datos anidados, sin transformar, no hay procesos automatizados para la actualización de nuevas películas o series, entre otras cosas.
  Se comienza desde cero, realizando procesos como Data Engineer y tener un MVP (Minimum Viable Product)


## Propuesta de trabajo

<details>
  <summary>Transformaciones</summary>
 ⏩ Realicé las siguientes transformaciones a los datos: (ETL)

  - Desanidar campos como `belongs_to_collection`, `production_companies`,`genres`,`movies_companys`,`spoken_languages`.
  - Rellenar valores nulos en `revenue` y `budget` con 0.
  - Eliminar valores nulos en `release_date`.
  - Formatear fechas a `AAAA-mm-dd` y crear una columna `release_year` extrayendo el año de la fecha de estreno.
  - Crear la columna `return` calculando `revenue / budget`, con valor 0 cuando no hay datos disponibles.
  - Eliminar columnas no utilizadas: `video`, `imdb_id`, `adult`, `original_title`, `poster_path`, `homepage`, `tagline`.
</details>

<details>
  <summary>Desarrollo API</summary>
  Para disponibilizar los datos, propongo usar el framework FastAPI. Las consultas propuestas son:

  - **cantidad_filmaciones_mes(Mes)**: Devuelve la cantidad de películas estrenadas en el mes consultado.
  - **cantidad_filmaciones_dia(Dia)**: Devuelve la cantidad de películas estrenadas en el día consultado.
  - **score_titulo(titulo_de_la_filmación)**: Devuelve el título, año de estreno y score de una película.
  - **votos_titulo(titulo_de_la_filmación)**: Devuelve el título, cantidad de votos y promedio de votaciones de una película.
  - **get_actor(nombre_actor)**: Devuelve el éxito del actor medido a través del retorno, cantidad de películas y promedio de retorno.
  - **get_director(nombre_director)**: Devuelve el éxito del director medido a través del retorno, nombre de cada película con fecha de lanzamiento, retorno individual, costo y ganancia.
</details>

<details>
  <summary>Deployment</summary>
  En esta ocasión he optado por Render.
</details>

<details>
  <summary>Análisis exploratorio de los datos (EDA)</summary>
  Después de limpiar los datos, he decidido investigar las relaciones entre las variables, buscar outliers o anomalías y patrones interesantes, también opté por un gráfico de nube de palabras para ver las frecuencias.
</details>

<details>
  <summary>Sistema de recomendación</summary>
  Una vez que la data es consumible por la API, está lista para ser utilizada por los departamentos de Analytics y Machine Learning. Entreno mi modelo de machine learning para crear un sistema de recomendación de películas. Debo encontrar la similitud de puntuación entre películas y devolver una lista de 5 películas similares.

  **Endpoint:**
  - **recomendacion(titulo)**: Devuelve una lista de 5 películas similares al título ingresado.
</details>

## Cómo ejecutar el proyecto

Desde la web

Puedes hacer uso de la API a traves del siguiente link
 ```sh
https://api-proyecto-individual.onrender.com
```

De manera local

1. Clona el repositorio:
   ```sh
   git clone https://github.com/tu-usuario/tu-repo.git
   cd tu-repo
   ```

2. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```

3. Ejecuta la aplicación:
   ```sh
   uvicorn main:app --reload
   ```

4. Accede a la documentación de la API en tu navegador:
   ```
   http://127.0.0.1:8000/docs
   ```
## Stack Tecnológico

- python
- sklearn
- TfidfVectorizer
- pandas
- numpy
- matplotlib
- seaborn
- Render
- FastApi
## Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio importante.

## Mis datos
linkedin 
www.linkedin.com/in/nissedgonzalezm

## Gracias por llegar hasta aquí

# <h1 align=center> Read Me </h1>

## <h1 align=center> PRIMER PROYECTO INDIVIDUAL </h1>

<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>


# <h1 align=center> Proyecto de Recomendación de Películas </h1>

<p align=center><img src=https://img.freepik.com/premium-vector/video-camera-icon-comic-style-movie-play-vector-cartoon-illustration-pictogram-video-streaming-business-concept-splash-effect_157943-5803.jpg?w=300><p>
  
¡Bienvenido a mi Proyecto de Recomendación de Películas! En esta ocasión, me he situado en el rol de un MLOps Engineer para desarrollar un sistema de recomendación de películas.

## Índice

- [Descripción del problema](#descripción-del-problema)
- [Propuesta de trabajo](#propuesta-de-trabajo)
- [Cómo ejecutar el proyecto](#cómo-ejecutar-el-proyecto)
- [Contribuciones](#contribuciones)

## Descripción del problema

<details>
  <summary>Contexto</summary>
  Tengo un modelo de recomendación con buenas métricas 😏, y ahora, ¿cómo lo llevo al mundo real? 👀

  El ciclo de vida de un proyecto de Machine Learning debe incluir desde el tratamiento y recolección de los datos (Data Engineer stuff) hasta el entrenamiento y mantenimiento del modelo de ML según llegan nuevos datos.
</details>

<details>
  <summary>Rol a desarrollar</summary>
  Empecé a trabajar como Data Scientist en una start-up que provee servicios de agregación de plataformas de streaming. El mundo es bello y voy a crear mi primer modelo de ML que soluciona un problema de negocio: un sistema de recomendación que aún no ha sido puesto en marcha!

  Voy a los datos y me doy cuenta que la madurez de los mismos es poca (ok, es nula 😭): Datos anidados, sin transformar, no hay procesos automatizados para la actualización de nuevas películas o series, entre otras cosas… haciendo mi trabajo imposible 😩.

  Debo empezar desde cero, haciendo un trabajo rápido de Data Engineer y tener un MVP (Minimum Viable Product) para las próximas semanas! Mi cabeza va a explotar 🤯, pero al menos sé cuál es, conceptualmente, el camino que debo seguir ❗. Así que me espanto los miedos y me pongo manos a la obra 💪
</details>

## Propuesta de trabajo

<details>
  <summary>Transformaciones</summary>
  Para este MVP no necesito perfección, ¡necesito rapidez! ⏩ Realicé estas transformaciones a los datos:

  - Desanidar campos como `belongs_to_collection`, `production_companies`.
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

## Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio importante.

import csv
from collections import namedtuple
from datetime import date, datetime

Pelicula = namedtuple('Pelicula', [
    "fecha_estreno",   # tipo date
    "titulo",          # tipo str
    "director",        # tipo str
    "genero",          # tipo list[str]
    "duracion",        # tipo int
    "presupuesto",     # tipo int
    "recaudacion",     # tipo int
    "reparto"          # tipo list[str]
])

def lee_peliculas(ruta_fichero: str) -> list[Pelicula]:    
    with open(ruta_fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector) # Saltamos la cabecera
        pelicula = []
        for linea in lector:
            fecha_estreno, titulo, director, genero, duracion, presupuesto, recaudacion, reparto = linea
            fecha_estreno = datetime.strptime(fecha_estreno, "%Y-%m-%d").date()
            genero = genero.split(",")
            duracion = int(duracion)
            presupuesto = int(presupuesto)
            recaudacion = int(recaudacion)
            reparto = reparto.split(",")
            añadir_pelicula = Pelicula(fecha_estreno,titulo, director,genero,duracion,presupuesto,recaudacion,reparto)
            pelicula.append(añadir_pelicula)
        return pelicula
    

def existe_pelicula(peliculas: list[Pelicula], cadena_en_titulo: str) -> bool:
    """
    Comprueba si existe alguna película cuyo título contenga la cadena dada.
    Parámetros:
    peliculas (list[Pelicula]): Lista de películas.
    cadena_en_titulo (str): Cadena a buscar en los títulos de las películas.
    Devuelve:
    bool: True si existe al menos una película cuyo título contiene la cadena, False en caso
    contrario.
    """
    for c in peliculas:
        if cadena_en_titulo in c.titulo:
            return True
    return False

def son_todas_director_genero(peliculas: list[Pelicula], director: str, genero: str) -> bool:
    """
    Comprueba si todas las películas del director dado pertenecen al género indicado.
    Parámetros:
    peliculas (list[Pelicula]): Lista de películas.
    director (str): Nombre del director.
    genero (str): Género a comprobar.
    Devuelve:
    bool: True si todas las películas del director pertenecen al género, False en caso contrario.
    """
    for c in peliculas:
       if c.director == director:
           if genero not in c.genero:
               return False
    return True

        


def construye_lista_titulos_actor(peliculas: list[Pelicula], actor: str) -> list[str]:
    """
    Devuelve una lista de títulos en los que el actor indicado aparece en el reparto.
    Parámetros:
    peliculas (list[Pelicula]): Lista de películas.
    actor (str): Nombre del actor.
    Devuelve:
    list[str]: Lista de títulos de películas en las que aparece el actor.
    """    
    lista_actor = []
    for c in peliculas:
        if actor in c.reparto:
            lista_actor.append(c.titulo)
    return lista_actor


def calcula_presupuesto_total_año(peliculas: list[Pelicula], año: int) -> int:
    """
    Suma y devuelve el presupuesto total de las películas cuyo año de estreno es el indicado.
    Parámetros:
    peliculas (list[Pelicula]): Lista de películas.
    año (int): Año de estreno.
    Devuelve:
    int: Presupuesto total de las películas estrenadas en el año indicado.
    """
    presupuesto_total = 0
    for c in peliculas:
        if c.fecha_estreno.year == año:
            presupuesto_total += c.presupuesto
    return presupuesto_total

def encuentra_pelicula_mayor_recaudacion(peliculas: list[Pelicula], genero: str) -> Pelicula | None:
    """
    Devuelve la película con mayor recaudacion entre las que incluyen el genero dado.
    Parámetros:
    peliculas (list[Pelicula]): Lista de películas.
    genero (str): Género a buscar.
    Devuelve:
    Pelicula | None: Película con mayor recaudación del género indicado, o None si no existe ninguna.
    """
    pelicula_maxima = None
    for c in peliculas:
        if genero in c.genero:
            if pelicula_maxima is None:
                pelicula_maxima = c
            elif c.recaudacion > pelicula_maxima.recaudacion:
                pelicula_maxima = c
    return pelicula_maxima

    

                






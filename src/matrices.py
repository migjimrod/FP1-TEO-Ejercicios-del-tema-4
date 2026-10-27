def es_matriz(matriz: list[list[int | float]]) -> bool:
    """
    Comprueba si una lista de listas representa una matriz válida.

    Parámetros:
    matriz (list[list[int | float]]): Lista de listas que se quiere comprobar.

    Devuelve:
    bool: True si todas las filas tienen el mismo número de elementos.
    """
    if len(matriz) == 0:
        return True
    # TODO: Ejecutar con el depurador
    # Esto es un esquema de para todo
    num_columnas = len(matriz[0])

    es_rectangular = True
    for fila in matriz[1:]:
        # Si NO se cumple la condicion
        if len(fila) != num_columnas:
            es_rectangular = False
            break
    return es_rectangular


def suma_matrices(
    m1: list[list[int | float]], m2: list[list[int | float]]
) -> list[list[int | float]] | None:
    """
    Suma dos matrices de las mismas dimensiones.

    Parámetros:
    m1 (list[list[int | float]]): Primera matriz.
    m2 (list[list[int | float]]): Segunda matriz.

    Devuelve:
    list[list[int | float]] | None: Matriz resultante, o None si las matrices
    no son válidas o tienen dimensiones distintas.
    """
    if not es_matriz(m1) or not es_matriz(m2):
        return None
    
    if len(m1) != len(m2):
        return None

    if len(m1) == 0:
        # Si ambas matrices están vacías, se permite la suma y el 
        # resultado es la matriz vacía
        return []

    if len(m1[0]) != len(m2[0]):
        return None

    ''' SOLUCION 1:
    matriz_suma = []
    for fila1, fila2 in zip(m1, m2):
        fila_suma = []
        for elem1, elem2 in zip(fila1, fila2):
            fila_suma.append(elem1 + elem2)
        matriz_suma.append(fila_suma)

    return matriz_suma
    '''

    # Solución 2:
    # Primero, tenemos que construir una matriz de ceros
    # con el mismo número de filas y columnas que m1 y m2
    num_filas = len(m1)
    num_columnas = len(m1[0])
    matriz_suma = []
    for i in range(num_filas):
        fila = [0] * num_columnas
        #fila = []
        #for j in range(num_columnas):
        #    fila.append(0)
        matriz_suma.append(fila)

    for i in range(num_filas):
        for j in range(num_columnas):
            matriz_suma[i][j] = m1[i][j] + m2[i][j]
    return matriz_suma



    
    
    


def suma_filas(
    matriz: list[list[int | float]],
) -> list[int | float] | None:
    """
    Suma los elementos de cada fila de una matriz.

    Parámetros:
    matriz (list[list[int | float]]): Matriz cuyos elementos se sumarán.

    Devuelve:
    list[int | float] | None: Lista con la suma de cada fila, o None si la
    matriz no es válida.
    """
    if not es_matriz(matriz):
        return None

    res = []
    for fila in matriz:
        #suma = 0
        #for elem in fila:
        #    suma += elem
        suma = sum(fila) 
        res.append(suma)
    return res

def suma_diagonal(matriz: list[list[int | float]]) -> int | float | None:
    """
    Suma los elementos de la diagonal principal de una matriz cuadrada.

    Parámetros:
    matriz (list[list[int | float]]): Matriz cuadrada de números.

    Devuelve:
    int | float | None: Suma de la diagonal, o None si la matriz no es válida
    o no es cuadrada.
    """
    if not es_matriz(matriz) or len(matriz) == 0 or len(matriz) != len(matriz[0]):
        return None
    # La matriz es cuadrada

    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][i]
    return suma

def suma_diagonal_secundaria(matriz: list[list[int | float]]) -> int | float | None:
    '''
    Devuelve la suma de la diagonal secundaria
    '''
    # TODO: Para hacer en casa
    

def transponer(
    matriz: list[list[int | float]],
) -> list[list[int | float]] | None:
    """
    Devuelve la matriz transpuesta.

    Parámetros:
    matriz (list[list[int | float]]): Matriz que se quiere transponer.

    Devuelve:
    list[list[int | float]] | None: Matriz transpuesta, o None si la matriz
    no es válida.
    """
    if not es_matriz(matriz):
        return None

    if len(matriz) == 0:
        return []

    num_columnas = len(matriz[0])
    matriz_transpuesta = []
    for i in range(num_columnas):
        fila_transpuesta = []
        for fila in matriz:
            fila_transpuesta.append(fila[i]) # accedo a la columna i-esima de la fila actual
        matriz_transpuesta.append(fila_transpuesta)
    return matriz_transpuesta


def multiplicar(m1: list[list[int | float]], m2: list[list[int | float]]
) -> list[list[int | float]] | None:
    '''
    Devuelve la matriz multiplicación m1xm2.
    '''
    # TODO: Para casa

def es_matriz(matriz: list[list[int | float]]) -> bool:
    """
    Comprueba si una lista de listas representa una matriz válida.

    Parámetros:
    matriz (list[list[int | float]]): Lista de listas que se quiere comprobar.

    Devuelve:
    bool: True si todas las filas tienen el mismo número de elementos.
    """
    for fila in matriz:
        if len(matriz[0]) != len(fila):
            return False
    return True


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
    if es_matriz(m1) and es_matriz(m2):
        if len(m1)==len(m2)==0:
            resultado_vacio = []
            return resultado_vacio 
        elif (len(m1) == len(m2)) and (len(m1[0])==len(m2[0])):
            resultado = []
            for i in range(len(m1)):
                fila_temporal = []
                for j in range(len(m2[0])):
                    suma = m1[i][j] + m2[i][j]
                    fila_temporal.append(suma)
                resultado.append(fila_temporal)
            return resultado
        else: 
            return None
    else: 
        return None



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
    if es_matriz(matriz):
        resultado = []
        for i in range(len(matriz)):
            suma = 0
            for j in range(len(matriz[0])): 
                suma += matriz[i][j] 
            resultado.append(suma)
        return resultado 
    else:
        return None      
            
def suma_diagonal(matriz: list[list[int | float]]) -> int | float | None:
    """
    Suma los elementos de la diagonal principal de una matriz cuadrada.

    Parámetros:
    matriz (list[list[int | float]]): Matriz cuadrada de números.

    Devuelve:
    int | float | None: Suma de la diagonal, o None si la matriz no es válida
    o no es cuadrada.
    """
    # TODO: Implementa esta función
    pass


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
    # TODO: Implementa esta función
    pass

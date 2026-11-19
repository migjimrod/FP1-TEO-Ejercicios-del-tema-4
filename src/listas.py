import random

def genera_aleatorios(n: int, minimo: int, maximo: int) -> list[int]:
    """
    Genera una lista con n números enteros aleatorios en un rango dado,
    asegurando que no haya dos elementos consecutivos iguales.

    Parámetros:
    n (int): Número de elementos en la lista.
    minimo (int): Valor mínimo del rango (inclusive).
    maximo (int): Valor máximo del rango (inclusive).

    Devuelve:
    list[int]: Lista con n números enteros aleatorios.
    """
    numeros = []
    while len(numeros)<n:
        nuevo = random.randint(minimo, maximo)
        if len(numeros) == 0 or nuevo != numeros[-1]:
            numeros.append(nuevo)
    return numeros





def intercala_listas(lista1: list, lista2: list) -> list:
    """
    Intercala dos listas. Si una lista es mayor que la otra, los elementos sobrantes se añaden al final.

    Parámetros:
    lista1 (list): Primera lista.
    lista2 (list): Segunda lista.

    Devuelve:
    list: Lista resultante de intercalar las dos listas.
    """
    lista = []
    for n1,n2 in zip(lista1,lista2):
        lista.append(n1)
        lista.append(n2)
    if len(lista1)<len(lista2):
        nueva_lista= lista2[len(lista1):]
        lista.extend(nueva_lista)
    elif len(lista2)<len(lista1):
        nueva_lista= lista1[len(lista2):]
        lista.extend(nueva_lista)
    return lista



def mezcla_ordenadas(lista1: list, lista2: list) -> list:
    """
    Mezcla dos listas ordenadas en una sola lista ordenada.

    Parámetros:
    lista1 (list): Primera lista ordenada.
    lista2 (list): Segunda lista ordenada.

    Devuelve:
    list: Lista resultante de mezclar las dos listas ordenadas.
    """
    lista1_ordenada = sorted(lista1)
    lista2_ordenada = sorted(lista2)
    nueva_lista_total = lista1_ordenada + lista2_ordenada
    nueva_lista_total_ordenada = sorted(nueva_lista_total)
    return nueva_lista_total_ordenada
    

def ordena_bubble_sort(lista: list) -> None:
    """
    Ordena una lista de números enteros utilizando el algoritmo de ordenamiento bubble sort. 

    Parámetros:
    lista (list[int]): Lista de números enteros a ordenar.
    """  
    intercambio = True
    while intercambio==True:
        intercambio = False
        for i in range(len(lista) - 1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                intercambio = True




def inserta_ordenado(lista_nombres: list[str], nombre: str) -> None:
    """
    Inserta un nombre en una lista de nombres manteniendo el orden (de menor a mayor longitud).
    Si la lista recibida no estuviera ordenada por longitud, la función no hace nada.

    Parámetros:
    lista_nombres (list[str]): Lista de nombres ordenada por longitud.
    nombre (str): Nombre a insertar.
    """
    







def busca_duplicados(lista: list) -> list:
    """
    Busca y devuelve una lista con los elementos duplicados en la lista recibida.

    Parámetros:
    lista (list): Lista en la que buscar duplicados.

    Devuelve:
    list: Lista con los elementos duplicados.
    """
    # TODO: Implementa esta función:
    # - usando count
    # - usando slicing y sin usar count
    pass
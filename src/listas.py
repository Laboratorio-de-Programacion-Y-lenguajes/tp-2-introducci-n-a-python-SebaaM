# ============================================================
# MÓDULO 3: Listas
# ============================================================

def suma_lista(numeros: list) -> int | float:
    """Calcular la suma de todos los elementos de una lista.

    Args:
        numeros (list): Lista de números (int o float).

    Returns:
        int | float: La suma de todos los elementos. Si la lista está vacía,
        retorna 0.

    Examples:
        >>> suma_lista([1, 2, 3])
        6
        >>> suma_lista([1.5, 2.5])
        4.0
        >>> suma_lista([])
        0
    """
    total: int | float = 0
    for numero in numeros:
        total += numero
    return total


def filtrar_pares(numeros: list) -> list:
    """Filtrar los números pares de una lista.

    Args:
        numeros (list): Lista de números enteros.

    Returns:
        list: Nueva lista con solo los números pares.

    Examples:
        >>> filtrar_pares([1, 2, 3, 4])
        [2, 4]
        >>> filtrar_pares([5, 7, 9])
        []
    """
    pares: list = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares


def invertir_lista(lista: list) -> list:
    """Invertir una lista sin modificar la original.

    Args:
        lista (list): Lista de elementos.

    Returns:
        list: Nueva lista con los elementos en orden inverso.

    Examples:
        >>> invertir_lista([1, 2, 3])
        [3, 2, 1]
        >>> invertir_lista([])
        []
    """
    return lista[::-1]


def eliminar_duplicados(lista: list) -> list:
    """Eliminar elementos duplicados de una lista.

    Mantiene el orden de la primera aparición de cada elemento.

    Args:
        lista (list): Lista de elementos.

    Returns:
        list: Nueva lista sin duplicados.

    Examples:
        >>> eliminar_duplicados([1, 2, 1, 3, 2])
        [1, 2, 3]
        >>> eliminar_duplicados([4, 4, 4])
        [4]
    """
    resultado: list = []
    for elemento in lista:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado


def aplanar_lista(lista: list) -> list:
    """Aplanar una lista de listas en una sola lista.

    Args:
        lista (list): Lista que contiene sublistas.

    Returns:
        list: Nueva lista con todos los elementos concatenados.

    Examples:
        >>> aplanar_lista([[1, 2], [3, 4]])
        [1, 2, 3, 4]
        >>> aplanar_lista([[], [5]])
        [5]
    """
    resultado: list = []
    for sublista in lista:
        for elemento in sublista:
            resultado.append(elemento)
    return resultado
# ============================================================
# MÓDULO 6: Funciones
# ============================================================


def aplicar_funcion(lista: list, func) -> list:
    """Aplicar una función a cada elemento de una lista.

    Args:
        lista (list): Lista de elementos.
        func (callable): Función que se aplicará a cada elemento.

    Returns:
        list: Nueva lista con los resultados de aplicar func.

    Examples:
        >>> aplicar_funcion([1, 2, 3], lambda x: x * 2)
        [2, 4, 6]
    """
    if not isinstance(lista, list):
        raise TypeError("El parámetro 'lista' debe ser de tipo list")
    if not callable(func):
        raise TypeError("El parámetro 'func' debe ser una función")

    return [func(elemento) for elemento in lista]


def componer(f, g):
    """Componer dos funciones.

    Retorna una nueva función que aplica primero g y luego f.

    Args:
        f (callable): Función externa.
        g (callable): Función interna.

    Returns:
        callable: Función compuesta.

    Examples:
        >>> h = componer(lambda x: x + 1, lambda y: y * 2)
        >>> h(3)
        7
    """
    if not callable(f) or not callable(g):
        raise TypeError("Ambos parámetros deben ser funciones")

    def funcion_compuesta(x):
        return f(g(x))

    return funcion_compuesta


def memoizar(func):
    """Memoizar una función.

    Retorna una versión de func que cachea sus resultados. Si se llama
    con los mismos argumentos, retorna el resultado cacheado.

    Args:
        func (callable): Función a memoizar.

    Returns:
        callable: Función memoizada.

    Examples:
        >>> f = memoizar(lambda x: x * x)
        >>> f(4)
        16
        >>> f(4)  # Usa el cache
        16
    """
    if not callable(func):
        raise TypeError("El parámetro 'func' debe ser una función")

    cache: dict = {}

    def funcion_memoizada(*args, **kwargs):
        clave = (args, tuple(sorted(kwargs.items())))
        if clave not in cache:
            cache[clave] = func(*args, **kwargs)
        return cache[clave]

    return funcion_memoizada


def reducir(lista: list, func, inicial):
    """Reducir una lista aplicando una función acumulativa.

    Aplica func acumulativamente a los elementos de lista, comenzando
    con el valor inicial.

    Args:
        lista (list): Lista de elementos.
        func (callable): Función acumulativa que recibe dos parámetros.
        inicial: Valor inicial para la acumulación.

    Returns:
        Resultado de aplicar la reducción.

    Examples:
        >>> reducir([1, 2, 3], lambda a, b: a + b, 0)
        6
    """
    if not isinstance(lista, list):
        raise TypeError("El parámetro 'lista' debe ser de tipo list")
    if not callable(func):
        raise TypeError("El parámetro 'func' debe ser una función")

    acumulador = inicial
    for elemento in lista:
        acumulador = func(acumulador, elemento)
    return acumulador
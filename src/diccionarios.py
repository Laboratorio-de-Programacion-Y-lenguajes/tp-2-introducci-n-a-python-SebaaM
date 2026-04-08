# ============================================================
# MÓDULO 4: Diccionarios
# ============================================================


def contar_palabras(texto: str) -> dict:
    """Contar la frecuencia de palabras en un texto.

    Convierte el texto a minúsculas y retorna un diccionario con la
    frecuencia de cada palabra. Las palabras se separan por espacios.

    Args:
        texto (str): Texto de entrada.

    Returns:
        dict: Diccionario con cada palabra como clave y su frecuencia
        como valor.

    Examples:
        >>> contar_palabras("hola mundo hola")
        {'hola': 2, 'mundo': 1}
    """
    if not isinstance(texto, str):
        raise TypeError("El parámetro 'texto' debe ser de tipo str")

    palabras: list = texto.lower().split()
    frecuencias: dict = {}
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    return frecuencias


def invertir_diccionario(d: dict) -> dict:
    """Invertir claves y valores de un diccionario.

    Args:
        d (dict): Diccionario de entrada.

    Returns:
        dict: Nuevo diccionario con claves y valores intercambiados.

    Raises:
        ValueError: Si hay valores duplicados en el diccionario original.

    Examples:
        >>> invertir_diccionario({'a': 1})
        {1: 'a'}
    """
    if not isinstance(d, dict):
        raise TypeError("El parámetro 'd' debe ser de tipo dict")

    invertido: dict = {}
    for clave, valor in d.items():
        if valor in invertido:
            raise ValueError("No se puede invertir: valores duplicados")
        invertido[valor] = clave
    return invertido


def merge_diccionarios(d1: dict, d2: dict) -> dict:
    """Combinar dos diccionarios.

    Si hay claves repetidas, prevalece el valor de d2.

    Args:
        d1 (dict): Primer diccionario.
        d2 (dict): Segundo diccionario.

    Returns:
        dict: Diccionario combinado.

    Examples:
        >>> merge_diccionarios({'a': 1}, {'a': 2, 'b': 3})
        {'a': 2, 'b': 3}
    """
    if not isinstance(d1, dict) or not isinstance(d2, dict):
        raise TypeError("Ambos parámetros deben ser de tipo dict")

    combinado: dict = {}
    for clave, valor in d1.items():
        combinado[clave] = valor
    for clave, valor in d2.items():
        combinado[clave] = valor
    return combinado


def filtrar_por_valor(d: dict, minimo: int) -> dict:
    """Filtrar pares clave-valor por un valor mínimo.

    Args:
        d (dict): Diccionario de entrada.
        minimo (int): Valor mínimo para filtrar.

    Returns:
        dict: Nuevo diccionario con pares cuyo valor >= minimo.

    Examples:
        >>> filtrar_por_valor({'a': 5, 'b': 2}, 3)
        {'a': 5}
    """
    if not isinstance(d, dict):
        raise TypeError("El parámetro 'd' debe ser de tipo dict")
    if not isinstance(minimo, int):
        raise TypeError("El parámetro 'minimo' debe ser de tipo int")

    filtrado: dict = {}
    for clave, valor in d.items():
        if isinstance(valor, (int, float)) and valor >= minimo:
            filtrado[clave] = valor
    return filtrado

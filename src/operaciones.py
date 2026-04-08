# ============================================================
# MÓDULO 7: Operaciones con Strings
# ============================================================


def es_palindromo(texto: str) -> bool:
    """Verificar si un texto es palíndromo.

    Ignora espacios y mayúsculas al realizar la comparación.

    Args:
        texto (str): Texto a evaluar.

    Returns:
        bool: True si el texto es palíndromo, False en caso contrario.

    Examples:
        >>> es_palindromo("Anita lava la tina")
        True
        >>> es_palindromo("Hola mundo")
        False
    """
    if not isinstance(texto, str):
        raise TypeError("El parámetro 'texto' debe ser de tipo str")

    limpio: str = "".join(texto.lower().split())
    return limpio == limpio[::-1]


def capitalizar_palabras(texto: str) -> str:
    """Capitalizar la primera letra de cada palabra.

    Args:
        texto (str): Texto de entrada.

    Returns:
        str: Texto con cada palabra capitalizada.

    Examples:
        >>> capitalizar_palabras("hola mundo")
        'Hola Mundo'
    """
    if not isinstance(texto, str):
        raise TypeError("El parámetro 'texto' debe ser de tipo str")

    return " ".join(palabra.capitalize() for palabra in texto.split())


def contar_vocales(texto: str) -> int:
    """Contar la cantidad de vocales en un texto.

    No distingue entre mayúsculas y minúsculas.

    Args:
        texto (str): Texto de entrada.

    Returns:
        int: Cantidad de vocales encontradas.

    Examples:
        >>> contar_vocales("Hola Mundo")
        4
    """
    if not isinstance(texto, str):
        raise TypeError("El parámetro 'texto' debe ser de tipo str")

    vocales: str = "aeiou"
    contador: int = 0
    for caracter in texto.lower():
        if caracter in vocales:
            contador += 1
    return contador


def caesar_cipher(texto: str, desplazamiento: int) -> str:
    """Aplicar el cifrado César a un texto.

    Solo desplaza letras (a-z, A-Z). Los demás caracteres no cambian.

    Args:
        texto (str): Texto a cifrar.
        desplazamiento (int): Número de posiciones a desplazar.

    Returns:
        str: Texto cifrado.

    Examples:
        >>> caesar_cipher("abc", 1)
        'bcd'
        >>> caesar_cipher("XYZ", 3)
        'ABC'
    """
    if not isinstance(texto, str):
        raise TypeError("El parámetro 'texto' debe ser de tipo str")
    if not isinstance(desplazamiento, int):
        raise TypeError("El parámetro 'desplazamiento' debe ser de tipo int")

    resultado: list = []
    for caracter in texto:
        if "a" <= caracter <= "z":
            base = ord("a")
            nuevo = (ord(caracter) - base + desplazamiento) % 26 + base
            resultado.append(chr(nuevo))
        elif "A" <= caracter <= "Z":
            base = ord("A")
            nuevo = (ord(caracter) - base + desplazamiento) % 26 + base
            resultado.append(chr(nuevo))
        else:
            resultado.append(caracter)
    return "".join(resultado)
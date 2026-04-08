# ============================================================
# MÓDULO 1: Variables y Tipos de Datos
# ============================================================
# Completá cada función siguiendo las instrucciones.
# NO modifiques los nombres de las funciones ni sus parámetros.
# ============================================================


def crear_saludo(nombre: str) -> str:
    """Crear un saludo personalizado.

    Esta función recibe un nombre y retorna un saludo en formato
    "Hola, <nombre>!".

    Args:
        nombre (str): El nombre de la persona.

    Returns:
        str: El saludo personalizado.

    Examples:
        >>> crear_saludo("Ana")
        'Hola, Ana!'
    """
    return f"Hola, {nombre}!"


def suma_enteros(a: int, b: int) -> int:
    """Calcular la suma de dos enteros.

    Args:
        a (int): Primer número entero.
        b (int): Segundo número entero.

    Returns:
        int: La suma de los dos enteros.

    Examples:
        >>> suma_enteros(3, 5)
        8
    """
    return a + b


def es_mayor_de_edad(edad: int) -> bool:
    """Verificar si una persona es mayor de edad.

    Args:
        edad (int): Edad de la persona.

    Returns:
        bool: True si la edad es mayor o igual a 18,
        False en caso contrario.

    Examples:
        >>> es_mayor_de_edad(20)
        True
        >>> es_mayor_de_edad(15)
        False
    """
    return edad >= 18


def tipo_de_dato(valor) -> str:
    """Obtener el tipo de dato de un valor.

    Args:
        valor: El valor a evaluar.

    Returns:
        str: El nombre del tipo de dato.

    Examples:
        >>> tipo_de_dato(42)
        'int'
        >>> tipo_de_dato("hola")
        'str'
    """
    return type(valor).__name__


def convertir_a_float(valor: str) -> float:
    """Convertir un string numérico a float.

    Args:
        valor (str): El valor numérico en formato string.

    Returns:
        float: El valor convertido a número decimal.

    Examples:
        >>> convertir_a_float("3.14")
        3.14
    """
    return float(valor)

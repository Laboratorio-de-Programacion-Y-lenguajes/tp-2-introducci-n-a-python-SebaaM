# ============================================================
# MÓDULO 2: Condicionales
# ============================================================


def clasificar_numero(n: int) -> str:
    """Clasificar un número entero como positivo, negativo o cero.

    Esta función recibe un número entero y devuelve un string indicando
    si el número es positivo, negativo o cero.

    Args:
        n (int): El número entero a clasificar.

    Returns:
        str: Una cadena que puede ser:
            - "positivo" si el número es mayor que cero.
            - "negativo" si el número es menor que cero.
            - "cero" si el número es exactamente cero.

    Examples:
        >>> clasificar_numero(10)
        'positivo'
        >>> clasificar_numero(-5)
        'negativo'
        >>> clasificar_numero(0)
        'cero'
    """
    # Caso: número mayor que cero
    if n > 0:
        return "positivo"

    # Caso: número menor que cero
    if n < 0:
        return "negativo"

    # Caso: número igual a cero
    return "cero"

def mayor_de_tres(a: int, b: int, c: int) -> int:
    """Determinar el mayor de tres números enteros.

    Esta función recibe tres números enteros y devuelve el mayor de ellos.
    Utiliza comparaciones directas para obtener el resultado de manera
    eficiente sin necesidad de estructuras adicionales.

    Args:
        a (int): Primer número entero.
        b (int): Segundo número entero.
        c (int): Tercer número entero.

    Returns:
        int: El mayor de los tres números.

    Examples:
        >>> mayor_de_tres(5, 8, 3)
        8
        >>> mayor_de_tres(-2, -7, -1)
        -1
        >>> mayor_de_tres(10, 10, 7)
        10
    """
    # Inicializar con el primer número
    mayor: int = a

    # Comparar con el segundo número
    if b > mayor:
        mayor = b

    # Comparar con el tercer número
    if c > mayor:
        mayor = c

    return mayor


def clasificar_nota(nota: float) -> str:
    """Clasificar una nota numérica en categorías.

    Esta función recibe una nota en formato decimal y devuelve una cadena
    indicando la categoría correspondiente según el valor de la nota.

    Args:
        nota (float): La nota a clasificar.

    Returns:
        str: Una cadena que puede ser:
            - "Sobresaliente" si la nota es mayor o igual a 9.
            - "Bueno" si la nota es mayor o igual a 7.
            - "Aprobado" si la nota es mayor o igual a 6.
            - "Desaprobado" si la nota es menor que 6.

    Examples:
        >>> clasificar_nota(9.5)
        'Sobresaliente'
        >>> clasificar_nota(7.2)
        'Bueno'
        >>> clasificar_nota(6.0)
        'Aprobado'
        >>> clasificar_nota(4.5)
        'Desaprobado'
    """
    # Caso: nota mayor o igual a 9
    if nota >= 9:
        return "Sobresaliente"

    # Caso: nota mayor o igual a 7
    if nota >= 7:
        return "Bueno"

    # Caso: nota mayor o igual a 6
    if nota >= 6:
        return "Aprobado"

    # Caso: nota menor que 6
    return "Desaprobado"


def es_bisiesto(anio: int) -> bool:
    """Determinar si un año es bisiesto.

    Un año es bisiesto si cumple las siguientes condiciones:
    - Es divisible por 4.
    - No es divisible por 100, salvo que también lo sea por 400.

    Args:
        anio (int): Año a evaluar.

    Returns:
        bool: True si el año es bisiesto, False en caso contrario.

    Examples:
        >>> es_bisiesto(2020)
        True
        >>> es_bisiesto(1900)
        False
        >>> es_bisiesto(2000)
        True
    """
    # Caso: divisible por 400 → bisiesto
    if anio % 400 == 0:
        return True

    # Caso: divisible por 100 → no bisiesto
    if anio % 100 == 0:
        return False

    # Caso: divisible por 4 → bisiesto
    if anio % 4 == 0:
        return True

    # Caso: no cumple ninguna condición → no bisiesto
    return False

# ============================================================
# MÓDULO 5: Loops
# ============================================================


def contar_hasta(n: int) -> list:
    """Generar una lista con números del 1 al n.

    Args:
        n (int): Número límite superior.

    Returns:
        list: Lista con los números desde 1 hasta n inclusive.

    Examples:
        >>> contar_hasta(5)
        [1, 2, 3, 4, 5]
    """
    if not isinstance(n, int):
        raise TypeError("El parámetro 'n' debe ser un entero")
    if n < 1:
        return []
    return list(range(1, n + 1))


def tabla_multiplicar(n: int) -> list:
    """Generar la tabla de multiplicar de un número.

    Retorna los primeros 10 múltiplos de n.

    Args:
        n (int): Número base.

    Returns:
        list: Lista con los múltiplos de n desde n hasta 10 * n.

    Examples:
        >>> tabla_multiplicar(3)
        [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
    """
    if not isinstance(n, int):
        raise TypeError("El parámetro 'n' debe ser un entero")
    return [n * i for i in range(1, 11)]


def suma_digitos(n: int) -> int:
    """Calcular la suma de los dígitos de un número entero positivo.

    Args:
        n (int): Número entero positivo.

    Returns:
        int: Suma de los dígitos.

    Examples:
        >>> suma_digitos(123)
        6
    """
    if not isinstance(n, int):
        raise TypeError("El parámetro 'n' debe ser un entero")
    if n < 0:
        raise ValueError("El número debe ser positivo")
    total: int = 0
    for digito in str(n):
        total += int(digito)
    return total


def es_primo(n: int) -> bool:
    """Verificar si un número es primo.

    Args:
        n (int): Número entero a evaluar.

    Returns:
        bool: True si el número es primo, False en caso contrario.

    Examples:
        >>> es_primo(2)
        True
        >>> es_primo(15)
        False
    """
    if not isinstance(n, int):
        raise TypeError("El parámetro 'n' debe ser un entero")
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limite: int = int(n ** 0.5) + 1
    for divisor in range(3, limite, 2):
        if n % divisor == 0:
            return False
    return True


def fibonacci(n: int) -> list:
    """Generar los primeros n números de la serie de Fibonacci.

    Args:
        n (int): Cantidad de números a generar.

    Returns:
        list: Lista con los primeros n números de Fibonacci.

    Examples:
        >>> fibonacci(6)
        [0, 1, 1, 2, 3, 5]
    """
    if not isinstance(n, int):
        raise TypeError("El parámetro 'n' debe ser un entero")
    if n < 0:
        raise ValueError("El parámetro 'n' debe ser no negativo")

    serie: list = []
    a: int = 0
    b: int = 1
    for _ in range(n):
        serie.append(a)
        a, b = b, a + b
    return serie
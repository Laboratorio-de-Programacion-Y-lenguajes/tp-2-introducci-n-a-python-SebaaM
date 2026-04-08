# Registro de Prompts

En este archivo debés documentar los prompts que usaste con herramientas de IA
(GitHub Copilot, ChatGPT, etc.) durante el desarrollo del TP.

**¿Por qué?** Queremos que aprendas a trabajar con IA de forma reflexiva:
que sepas qué le pediste, qué obtuviste, y si tuviste que corregirlo.

---

## Formato para cada entrada

```
### [Número] - [Módulo]

**Herramienta**: ChatGPT-5

**Prompt usado**:
> Escribí acá exactamente lo que le pediste a la IA

**Resultado obtenido**:
Describí brevemente qué generó (código, explicación, etc.)

**¿Lo usaste tal cual o lo modificaste?**
Explicá qué cambios hiciste y por qué (o por qué no cambiaste nada).
```

---

## Mis prompts

Cumple con esto en todas tus respuestas.
Actuá como tutor de Python 3.13. Dame una receta paso a paso para:

- Docstring completa (Google format)
- Type hints
- Lógica eficiente (no verificar hasta n, solo hasta sqrtn)
  Restricciones:
- Sin imports. Solo built-ins de Python
- Seguir PEP 8 estrictamente
- Compatible con Python 3.13

### 1 - variables.py

**Herramienta**: CHATGPT-5

**Prompt usado**:
Completá cada función siguiendo las instrucciones.
NO modifiques los nombres de las funciones ni sus parámetros.
def crear_saludo(nombre: str) -> str: """ Retorna un saludo personalizado. Ejemplo: crear_saludo("Ana") -> "Hola, Ana!" """
def suma_enteros(a: int, b: int) -> int: """ Retorna la suma de dos enteros. """
def es_mayor_de_edad(edad: int) -> bool: """ Retorna True si edad >= 18, False caso contrario. """
def tipo_de_dato(valor) -> str: """ Retorna el nombre del tipo de dato del valor recibido. Ejemplo: tipo_de_dato(42) -> "int" tipo_de_dato("hola") -> "str" """
def convertir_a_float(valor: str) -> float: """ Convierte un string numérico a float. Ejemplo: convertir_a_float("3.14") -> 3.14 ""

>

**Resultado obtenido**:

**¿Lo usaste tal cual o lo modificaste?**
tal cual

---

### 2 - condicionales.py

**Herramienta**:

**Prompt usado**: necesito una función que clasifique un numero recibido por parámetro y devolver en string según corresponda: positivo, negativo, cero.
Implementá la función clasificar_numero(n: int) -> strl con:

>

**Resultado obtenido**:

**¿Lo usaste tal cual o lo modificaste?**

---

### 3 - listas.py

**Herramienta**:

**Prompt usado**:

> estoy resolviendo un ejercicio de listas en Python con estas reglas:
> ¿Podés revisar mi lógica como verificador cognitivo? enumerá casos borde que debería testear, proponé 3 tests con entradas y salidas esperadas (sin escribir el código final por mí)

**Resultado obtenido**:
🔍 Casos borde a considerar

- Listas vacías → ¿qué retorna cada función si no hay elementos?
- Listas con un solo elemento → comportamiento mínimo.
- Listas con valores negativos, cero o mixtos → asegurar que la lógica no asuma solo positivos.
- Listas con floats además de enteros → verificar que suma_lista maneje ambos.
- Listas con duplicados consecutivos y no consecutivos → importante para eliminar_duplicados.
- Listas anidadas vacías o con un solo subelemento → para aplanar_lista.
- Orden y no modificación de la original → clave en invertir_lista y eliminar_duplicados.

🧪 Propuesta de 3 tests con entradas y salidas esperadas
Test 1: combinación de enteros y floats

- Entrada: suma_lista([1, 2.5, -3])
- Salida esperada: 0.5
  Test 2: duplicados y orden
- Entrada: eliminar_duplicados([1, 2, 1, 3, 2, 4])
- Salida esperada: [1, 2, 3, 4]
  (mantiene el orden de primera aparición)
  Test 3: lista de listas con vacíos
- Entrada: aplanar_lista([[1, 2], [], [3], [4, 5]])
- Salida esperada: [1, 2, 3, 4, 5]

**¿Lo usaste tal cual o lo modificaste?**

---

### 4 - diccionarios.py

**Herramienta**:

**Prompt usado**:
Siguiendo las instrucciones previas, utilizando diccionarios. Respetar la firma de la función. Agregar verifiaciones según correspondan

>

**Resultado obtenido**:

**¿Lo usaste tal cual o lo modificaste?**

---

### 5 - loops.py

**Herramienta**:

**Prompt usado**:

>

**Resultado obtenido**:

**¿Lo usaste tal cual o lo modificaste?**

---

### 6 - funciones.py

**Herramienta**:

**Prompt usado**:

>

**Resultado obtenido**:

**¿Lo usaste tal cual o lo modificaste?**

---

### 7 - operaciones.py

**Herramienta**:

**Prompt usado**:

>

**Resultado obtenido**:

**¿Lo usaste tal cual o lo modificaste?**

---

## Reflexión final

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts?
  Una base correcta para optimizar las respuestas es importante, variaciones segun contexto, chequeo y entendimiento de la lineas es fundamental..
- ¿En qué casos la IA fue útil y en cuáles no?
  Con patrones en pasos en algoritmos largos, los prompts deben ser claros y concisos, pero pueden llegar a ser confusos o presentar ambiguedades.
- ¿Qué harías diferente la próxima vez?
  Contemplar verifiaciones de datos, comentarios claros y claridad de lógica.

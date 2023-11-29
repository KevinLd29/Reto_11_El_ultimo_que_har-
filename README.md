# Reto 11 El ultimo que haré
Contra todo pronostico, creo que si se puede salvar la materia, aprendí mucho más de lo que creia, no solo en programación, también en general, temas de la vida, vida universitaria, lecciones de vida SJAhjhkas

Bueno, el tema que se trabajará en este repo serán las matrices, un pequeño abre bocas antes de entrar a sufrir con el algebra lineal.

Como retos propuestos y resueltos, con códigos funcionlas (si hay algún error, comentario, sugerencia, contactarse conmigo y hacermelo saber, por favor), tenemos:
# Punto 1
Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

### 1. Suma/Resta de Matrices
Posible solución que le dí sería:
```python
def validarDimensiones(matriz1, matriz2):
    # Verifica que las matrices tengan las mismas dimensiones
    return len(matriz1) == len(matriz2) and all(len(fila) == len(matriz2[0]) for fila in matriz1)

def sumaMatrices(matriz1, matriz2):
    if validarDimensiones(matriz1, matriz2):
        return [[matriz1[i][j] + matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]
    else:
        return None  # Cuando la operación no es válida

def restaMatrices(matriz1, matriz2):
    if validarDimensiones(matriz1, matriz2):
        return [[matriz1[i][j] - matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]
    else:
        return None  # Cuando la operación no es válida

# Ejemplo de uso (Cambie las matrices si quiere)
matrizA = [[1, 2], [3, 4]]
matrizB = [[5, 6], [7, 8]]

resultadoSuma = sumaMatrices(matrizA, matrizB)
resultadoResta = restaMatrices(matrizA, matrizB)

print("Suma de matrices:", resultadoSuma)
print("Resta de matrices:", resultadoResta)
````
Este código si salió un poco largo pero espero sea entendible, sin embargo, les doy una pequeña explicación:
- Imagina que tienes dos matrices (como tablas de números).
- La función `validarDimensiones` revisa si estas matrices se pueden sumar o restar (tienen el mismo número de filas y columnas).
- `sumaMatrices` y `restaMatrices` toman dos matrices y devuelven su suma o resta, siempre que tengan las dimensiones correctas.

**Ejemplo:**
- Si tienes matrices A = [[1, 2], [3, 4]] y B = [[5, 6], [7, 8]], el programa te dirá que A + B es [[6, 8], [10, 12]] y A - B es [[-4, -4], [-4, -4]].

# Punto 2
Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

### 2. Producto de Matrices
Esta fue la manera en la que me sirvió (Puedes copiar el código y probar cambiando los datos de la matriz):
```python
def validarMultiplicacion(matriz1, matriz2):
    # Verifica que el número de columnas de la primera matriz sea igual al número de filas de la segunda matriz
    return len(matriz1[0]) == len(matriz2)

def productoMatrices(matriz1, matriz2):
    if validarMultiplicacion(matriz1, matriz2):
        return [[sum(matriz1[i][k] * matriz2[k][j] for k in range(len(matriz1[0])))
                 for j in range(len(matriz2[0]))] for i in range(len(matriz1))]
    else:
        return None  # Operación no válida

# Ejemplo de uso
matrizC = [[1, 2], [3, 4]]
matrizD = [[5, 6], [7, 8]]

resultadoProducto = productoMatrices(matrizC, matrizD)
print("Producto de matrices:", resultadoProducto)
````
- Ahora, piensa en dos matrices que quieres multiplicar.
- `validarMultiplicacion` verifica si las matrices pueden multiplicarse (el número de columnas en la primera debe ser igual al número de filas en la segunda).
- `productoMatrices` toma dos matrices y devuelve su producto, si la multiplicación es válida.

**Ejemplo:**
- Si tienes matrices C = [[1, 2], [3, 4]] y D = [[5, 6], [7, 8]], el programa te dirá que C * D es [[19, 22], [43, 50]].


# Punto 3
Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.

### 3. Matriz Transpuesta
Una solución que a mi parecer está muy optimizada sería algo así:
```python
def obtenerTranspuesta(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

# Ejemplo de uso
matrizE = [[1, 2, 3], [4, 5, 6]]

transpuesta = obtenerTranspuesta(matrizE)
print("Matriz transpuesta:", transpuesta)
````
Este punto fue bastante más fácil y sencillo de realizar, bueno, tambíen fue porque lo vimos en clase, como todo, mejor dicho, vimos como darle solución de una manera sencilla en dos clases despues jaja.
Explicando un poco:
- Ahora, piensa en una sola matriz.
- La función `obtenerTranspuesta` toma una matriz y devuelve su "transpuesta" (las filas se vuelven columnas y viceversa).

**Ejemplo:**
- Si tienes la matriz E = [[1, 2, 3], [4, 5, 6]], el programa te dirá que la transpuesta es [[1, 4], [2, 5], [3, 6]].

# Punto 4
Desarrollar un programa que sume los elementos de una columna dada de una matriz.

### 4. Suma de Columna
Recuerda que si quieres probar, copia y pega en tu compilador de preferencia y cambia los datos de las matrices para acercarlo o usarlo mejor en tu caso:
```python
def sumaColumna(matriz, columna):
    # Verifica que la columna sea válida
    if columna < 0 or columna >= len(matriz[0]):
        return None
    
    return sum(matriz[i][columna] for i in range(len(matriz)))

# Ejemplo de uso
matrizF = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

columnaSuma = 1
resultadoSumaColumna = sumaColumna(matrizF, columnaSuma)
print(f"Suma de la columna {columnaSuma + 1}:", resultadoSumaColumna)
````
- Piensa en una matriz y selecciona una columna.
- La función `sumaColumna` suma todos los números en esa columna.

**Ejemplo:**
- Si tienes la matriz F = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], y eliges la columna 1 (empezando desde 0), el programa dirá que la suma es 15 (1 + 4 + 7).

# Punto 5
Desarrollar un programa que sume los elementos de una fila dada de una matriz.

### 5. Suma de Fila
Y como último punto, finalmente:
```python
def sumaFila(matriz, fila):
    # Verifica que la fila sea válida
    if fila < 0 or fila >= len(matriz):
        return None
    
    return sum(matriz[fila])

# Ejemplo de uso
matrizG = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

filaSuma = 2
resultadoSumaFila = sumaFila(matrizG, filaSuma)
print(f"Suma de la fila {filaSuma + 1}:", resultadoSumaFila)
````
- Similar a la suma de columna, pero esta vez suma los números en una fila.

**Ejemplo:**
- Con la matriz G = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], y eliges la fila 2, el programa te dirá que la suma es 21 (7 + 8 + 9).

En resumen, estos programas son como herramientas matemáticas que realizan diferentes operaciones con matrices, de una manera sencilla, antes del traume que se vendrá cuando se esté viendo líneal. Espero que esto haya sido claro y divertido! (por el momento, como les digo, en líneal ya no será tan lindo)

Y yo sinceramente creo que por cuestiones de tiempo, esté será el ultimo reto que haga, no fueron hechos en orden pero se hicieron varios, sin nada más que decir, nos veremos en una próxima ocasión. ¡Muchas gracias!

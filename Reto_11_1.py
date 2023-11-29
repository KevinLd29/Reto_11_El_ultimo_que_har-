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

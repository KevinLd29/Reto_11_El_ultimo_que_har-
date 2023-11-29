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

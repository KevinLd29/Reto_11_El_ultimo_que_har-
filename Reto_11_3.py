def obtenerTranspuesta(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

# Ejemplo de uso
matrizE = [[1, 2, 3], [4, 5, 6]]

transpuesta = obtenerTranspuesta(matrizE)
print("Matriz transpuesta:", transpuesta)

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

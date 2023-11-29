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

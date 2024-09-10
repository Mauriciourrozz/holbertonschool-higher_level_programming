#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matriz_cuadrada = []
    for seccion in matrix:
        seccion_cuadrada = []
        for num in seccion:
             seccion_cuadrada.append(num**2)
        matriz_cuadrada.append(seccion_cuadrada)
    return matriz_cuadrada

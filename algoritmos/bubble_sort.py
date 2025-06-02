"""
    Algoritmo de ordenação adaptado de W3School
    Disponível em: https://www.w3schools.com/dsa/dsa_algo_bubblesort.php
"""
def ordenar(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr

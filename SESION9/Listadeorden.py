import random
import time
import pandas as pd

def burbuja(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insercion(arr):
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        while j >= 0 and clave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave

def seleccion(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def merge(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge(L)
        merge(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def medir_tiempo(funcion, datos):
    inicio = time.time()
    funcion(datos.copy())  # Usar .copy() para no modificar la lista original
    fin = time.time()
    return fin - inicio

# Pedir cantidad de datos
cantidad = int(input("Ingresa la cantidad de datos a ordenar: "))

# Generar lista de números aleatorios
datos = [random.randint(1, 100000) for _ in range(cantidad)]

# Medir tiempos
tiempos = {
    'Método': [],
    'Tiempo (s)': []
}

for metodo in [("Burbuja", burbuja), ("Inserción", insercion), ("Selección", seleccion), ("Merge Sort", merge)]:
    tiempo = medir_tiempo(metodo[1], datos)
    tiempos['Método'].append(metodo[0])
    tiempos['Tiempo (s)'].append(tiempo)

# Crear DataFrame y mostrar tabla
df = pd.DataFrame(tiempos)
print("\nTiempos de ordenamiento:")
print(df)

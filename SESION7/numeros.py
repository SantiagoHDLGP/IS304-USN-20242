# Crear una lista del 1 al 100
lista = list(range(1, 101))

# Reemplazar los elementos según las condiciones
for i in range(len(lista)):
    if lista[i] % 3 == 0 and lista[i] % 5 == 0:
        lista[i] = "fizzbuzz"
    elif lista[i] % 3 == 0:
        lista[i] = "fizz"
    elif lista[i] % 5 == 0:
        lista[i] = "buzz"

# Imprimir la lista resultante
print(lista)

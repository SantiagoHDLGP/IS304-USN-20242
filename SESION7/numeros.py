# Escríbeme un programa que cree una lista con los números del 1 al 100 (ambos incluidos), sustituyendo posteriormente los elementos siguientes: Posiciones múltiplos de 3 por la palabra "fizz" , Posiciones múltiplos de 5 por la palabra "buzz" , Posiciones múltiplos de 3 y de 5 a la vez  por la palabra "fizzbuzz" 
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

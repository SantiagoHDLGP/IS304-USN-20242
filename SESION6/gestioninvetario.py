# Inicializa el inventario
inventario = []

def agregar(item, cantidad):
    for i in range(len(inventario)):
        if inventario[i][0] == item:
            inventario[i][1] += cantidad
            return
    inventario.append([item, cantidad])

def eliminar(item, cantidad):
    for i in range(len(inventario)):
        if inventario[i][0] == item:
            inventario[i][1] -= cantidad
            if inventario[i][1] <= 0:
                inventario.pop(i)
            return

def mostrar_inventario():
    print("Inventario:")
    for item, cantidad in inventario:
        print(f"{item}: {cantidad}")
    print()

def productos_bajos(umbral):
    print(f"Productos con menos de {umbral} unidades:")
    productos_bajos = [item for item, cantidad in inventario if cantidad < umbral]
    print("Elementos:", productos_bajos)
    print()

def mostrar_menu():
    print("Menú de opciones:")
    print("1. Agregar elemento")
    print("2. Eliminar elemento")
    print("3. Mostrar inventario")
    print("4. Productos bajos")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ").strip()

        if opcion == "1":
            item = input("Ingresa el elemento a agregar: ")
            cantidad = int(input("Ingresa la cantidad: "))
            agregar(item, cantidad)

        elif opcion == "2":
            item = input("Ingresa el elemento a eliminar: ")
            cantidad = int(input("Ingresa la cantidad: "))
            eliminar(item, cantidad)

        elif opcion == "3":
            mostrar_inventario()

        elif opcion == "4":
            umbral = int(input("Ingresa el umbral: "))
            productos_bajos(umbral)

        elif opcion == "5":
            print("Saliendo...")
            break

        else:
            print("Opción no reconocida. Intenta de nuevo.")

if __name__ == "__main__":
    main()

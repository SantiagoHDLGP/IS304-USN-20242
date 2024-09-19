# Inicializa el inventario
frutas = ["manzana", "naranja", "plátano"]
cantidades = [0, 0, 0]  # Cantidades correspondientes a cada fruta

def agregar(fruta, cantidad):
    if fruta in frutas:
        index = frutas.index(fruta)
        cantidades[index] += cantidad
    else:
        frutas.append(fruta)
        cantidades.append(cantidad)

def eliminar(fruta, cantidad):
    if fruta in frutas:
        index = frutas.index(fruta)
        cantidades[index] -= cantidad
        if cantidades[index] <= 0:
            frutas.pop(index)
            cantidades.pop(index)

def mostrar_inventario():
    print("Inventario:")
    print("Frutas:", frutas)
    print("Cantidades:", cantidades)
    print()

def productos_bajos(umbral):
    print(f"Productos con menos de {umbral} unidades:")
    productos_bajos = [fruta for fruta, cantidad in zip(frutas, cantidades) if cantidad < umbral]
    print("Frutas:", productos_bajos)
    print()

def mostrar_menu():
    print("Menú de opciones:")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Mostrar inventario")
    print("4. Productos bajos")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ").strip()

        if opcion == "1":
            fruta = input("Ingresa la fruta a agregar: ")
            cantidad = int(input("Ingresa la cantidad: "))
            agregar(fruta, cantidad)

        elif opcion == "2":
            fruta = input("Ingresa la fruta a eliminar: ")
            cantidad = int(input("Ingresa la cantidad: "))
            eliminar(fruta, cantidad)

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

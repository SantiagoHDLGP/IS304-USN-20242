'''
Crear un programa que permita crear objetos de la clase CuentaBancaria, cuyos atributos son: numeroCta, nombreCliente, saldoCta, fechaApertura, ultimoRetiro, ultimaConsignacion.
Aplicar encapsulamiento y definir los métodos apropiados para controlar y gestionar los atributos de los objetos creados.
Utilizar un menu para las diferentes opciones, tales como aperturaCta, consignar, retirar y transferencia entre otros.
'''
class CuentaBancaria
    
    def __init__(self, NumeroCta=0, NombreCliente, SaldoCta=0, FechaApertura=0, UltimoRetiro=0, UltimaConsignacion=0):
        self.__NumeroCta = NumeroCta
        self.__NombreCliente = Nombrecliente
        self.__SaldoCta = SaldoCta
        self.__FechaApertura = FechaApertura
        self.__UltimoRetiro = UltimoRetiro
        self.__UltimaConsignacion = UltimaConsignacion 
        
    def set(self, NumeroCta, NombreCliente, SaldoCta, FechaApertura, UltimoRetiro, UltimaConsignacion):
        self.__NumeroCta = NumeroCta
        self.__NombreCliente = Nombrecliente
        self.__SaldoCta = SaldoCta
        self.__FechaApertura = FechaApertura
        self.__UltimoRetiro = UltimoRetiro
        self.__UltimaConsignacion = UltimaConsignacion 
        
    def set__NumeroCta(self, x):
        self.__NumeroCta = 
        
    def set__NombreCliente(self, y):
        self.__NombreCliente = 
        
    def set__SaldoCta(self, x):
        self.__SaldoCta = 
        
    def set__FechaApertura(self, x):
        self.__FechaApertura = 
        
    def set__UltimoRetiro(self, x):
        self.__UltimoRetiroa = 

    def set__UltimaConsignacion(self, x):
        self.__UltimaConsignacion =   

  # DEFINIMOS LAS OPERACIONAS A REALIZAR
    def consignar(self, cantidad):
        if cantidad > 0:
            self.__saldoCta += cantidad
            self.__ultimaConsignacion = cantidad
            return True
        return False
    
    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldoCta:
            self.__saldoCta -= cantidad
            self.__ultimoRetiro = cantidad
            return True
        return False
    
    def transferir(self, cantidad, cuenta_destino):
        if self.retirar(cantidad):
            cuenta_destino.consignar(cantidad)
            return True
        return False
        
  # DEFINIMOS EL MENU ///////////////////////////////////////////////////////

def menu():
    cuentas = {}
    while True:
        print("\nMenu:")
        print("1. Apertura de Cuenta")
        print("2. Consignar Dinero")
        print("3. Retirar Dinero")
        print("4. Transferir Dinero")
        print("5. Consultar Saldo")
        print("6. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            numero = input("Número de cuenta: ")
            nombre = input("Nombre del cliente: ")
            saldo = float(input("Saldo inicial: "))
            fecha = input("Fecha de apertura: ")
            cuentas[numero] = CuentaBancaria(numero, nombre, saldo, fecha)
            print(f"Cuenta {numero} abierta exitosamente.")
        
        elif opcion == '2':
            numero = input("Número de cuenta: ")
            if numero in cuentas:
                cantidad = float(input("Cantidad a consignar: "))
                if cuentas[numero].consignar(cantidad):
                    print("Consignación exitosa.")
                else:
                    print("Cantidad inválida.")
            else:
                print("Cuenta no encontrada.")
        
        elif opcion == '3':
            numero = input("Número de cuenta: ")
            if numero in cuentas:
                cantidad = float(input("Cantidad a retirar: "))
                if cuentas[numero].retirar(cantidad):
                    print("Retiro exitoso.")
                else:
                    print("Fondos insuficientes o cantidad inválida.")
            else:
                print("Cuenta no encontrada.")
        
        elif opcion == '4':
            numero_origen = input("Número de cuenta origen: ")
            numero_destino = input("Número de cuenta destino: ")
            if numero_origen in cuentas and numero_destino in cuentas:
                cantidad = float(input("Cantidad a transferir: "))
                if cuentas[numero_origen].transferir(cantidad, cuentas[numero_destino]):
                    print("Transferencia exitosa.")
                else:
                    print("Fondos insuficientes o cantidad inválida.")
            else:
                print("Una o ambas cuentas no se encuentran.")
        
        elif opcion == '5':
            numero = input("Número de cuenta: ")
            if numero in cuentas:
                cuenta = cuentas[numero]
                print(f"Saldo de la cuenta {numero}: {cuenta.get_saldoCta()}")
            else:
                print("Cuenta no encontrada.")
        
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Intenta nuevamente.")

# LLAMAMOS MENU //////////////////////////////
menu()



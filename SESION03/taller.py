'''
Crear un programa que permita crear objetos de la clase CuentaBancaria, cuyos atributos son: numeroCta, nombreCliente, saldoCta, fechaApertura, ultimoRetiro, ultimaConsignacion.
Aplicar encapsulamiento y definir los métodos apropiados para controlar y gestionar los atributos de los objetos creados.
Utilizar un menu para las diferentes opciones, tales como aperturaCta, consignar, retirar y transferencia entre otros.
'''
from datetime import datetime

class CuentaBancaria:
    def __init__(self, numeroCta="", nombreCliente="", saldoCta=0.0, fechaApertura=None):
        if fechaApertura is None:
            fechaApertura = datetime.now()
        self._numeroCta = numeroCta
        self._nombreCliente = nombreCliente
        self._saldoCta = saldoCta
        self._fechaApertura = fechaApertura
        self._ultimoRetiro = None
        self._ultimaConsignacion = None

    def set(self, numeroCta, nombreCliente, saldoCta, fechaApertura=None):
        self._numeroCta = numeroCta
        self._nombreCliente = nombreCliente
        self._saldoCta = saldoCta
        if fechaApertura is None:
            self._fechaApertura = datetime.now()
        else:
            self._fechaApertura = fechaApertura

    def set_numeroCta(self, numeroCta):
        self._numeroCta = numeroCta

    def set_nombreCliente(self, nombreCliente):
        self._nombreCliente = nombreCliente

    def set_saldoCta(self, saldoCta):
        if saldoCta < 0:
            self._saldoCta = 0
        else:
            self._saldoCta = saldoCta

    def set_fechaApertura(self, fechaApertura):
        self._fechaApertura = fechaApertura

    def get_numeroCta(self):
        return self._numeroCta

    def get_nombreCliente(self):
        return self._nombreCliente

    def get_saldoCta(self):
        return self._saldoCta

    def get_fechaApertura(self):
        return self._fechaApertura

    def get_ultimoRetiro(self):
        return self._ultimoRetiro

    def get_ultimaConsignacion(self):
        return self._ultimaConsignacion

    def consignar(self, monto):
        if monto > 0:
            self._saldoCta += monto
            self._ultimaConsignacion = datetime.now()
            print(f"Consignación exitosa. Nuevo saldo: {self._saldoCta}")
        else:
            print("El monto debe ser mayor a cero.")

    def retirar(self, monto):
        if monto > 0:
            if self._saldoCta >= monto:
                self._saldoCta -= monto
                self._ultimoRetiro = datetime.now()
                print(f"Retiro exitoso. Nuevo saldo: {self._saldoCta}")
            else:
                print("Saldo insuficiente.")
        else:
            print("El monto debe ser mayor a cero.")

    def transferencia(self, monto, cuenta_destino):
        if monto > 0:
            if self._saldoCta >= monto:
                self.retirar(monto)
                cuenta_destino.consignar(monto)
                print(f"Transferencia exitosa a la cuenta {cuenta_destino.get_numeroCta()}.")
            else:
                print("Saldo insuficiente para la transferencia.")
        else:
            print("El monto debe ser mayor a cero.")

class CuentaAhorros(CuentaBancaria):
    def __init__(self, numeroCta="", nombreCliente="", saldoCta=0.0, fechaApertura=None, tasaInteres=0.02):
        super().__init__(numeroCta, nombreCliente, saldoCta, fechaApertura)
        self._tasaInteres = tasaInteres

    def aplicar_interes(self):
        interes = self.get_saldoCta() * self._tasaInteres
        self.consignar(interes)
        print(f"Interés aplicado. Nuevo saldo: {self.get_saldoCta()}")

    def set_tasaInteres(self, tasaInteres):
        if tasaInteres >= 0:
            self._tasaInteres = tasaInteres
        else:
            print("La tasa de interés debe ser mayor o igual a cero.")

    def get_tasaInteres(self):
        return self._tasaInteres

class CuentaCorriente(CuentaBancaria):
    def __init__(self, numeroCta="", nombreCliente="", saldoCta=0.0, fechaApertura=None, limiteSobregiro=0.0):
        super().__init__(numeroCta, nombreCliente, saldoCta, fechaApertura)
        self._limiteSobregiro = limiteSobregiro

    def retirar(self, monto):
        if monto > 0:
            if self.get_saldoCta() + self._limiteSobregiro >= monto:
                self._saldoCta -= monto
                self._ultimoRetiro = datetime.now()
                print(f"Retiro exitoso. Nuevo saldo: {self.get_saldoCta()}")
            else:
                print("Saldo insuficiente, incluso con el límite de sobregiro.")
        else:
            print("El monto debe ser mayor a cero.")

    def set_limiteSobregiro(self, limiteSobregiro):
        if limiteSobregiro >= 0:
            self._limiteSobregiro = limiteSobregiro
        else:
            print("El límite de sobregiro debe ser mayor o igual a cero.")

    def get_limiteSobregiro(self):
        return self._limiteSobregiro

def main():
    cuentas = {}
    
    while True:
        print("\n--- Menú ---")
        print("1. Apertura de cuenta")
        print("2. Consignar")
        print("3. Retirar")
        print("4. Transferencia")
        print("5. Aplicar interés (Cuenta de Ahorros)")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            tipo_cuenta = input("Tipo de cuenta (Ahorros/Corriente): ")
            numero = input("Número de cuenta: ")
            nombre = input("Nombre del cliente: ")
            saldo = float(input("Saldo inicial: "))
            if tipo_cuenta.lower() == 'ahorros':
                tasa_interes = float(input("Tasa de interés: "))
                cuenta = CuentaAhorros(numero, nombre, saldo, tasaInteres=tasa_interes)
            elif tipo_cuenta.lower() == 'corriente':
                limite_sobregiro = float(input("Límite de sobregiro: "))
                cuenta = CuentaCorriente(numero, nombre, saldo, limiteSobregiro=limite_sobregiro)
            else:
                print("Tipo de cuenta no válido.")
                continue
            cuentas[numero] = cuenta
            print("Cuenta abierta exitosamente.")
        
        elif opcion == '2':
            numero = input("Número de cuenta: ")
            if numero in cuentas:
                monto = float(input("Monto a consignar: "))
                cuentas[numero].consignar(monto)
            else:
                print("Número de cuenta no encontrado.")
        
        elif opcion == '3':
            numero = input("Número de cuenta: ")
            if numero in cuentas:
                monto = float(input("Monto a retirar: "))
                cuentas[numero].retirar(monto)
            else:
                print("Número de cuenta no encontrado.")
        
        elif opcion == '4':
            numero_origen = input("Número de cuenta origen: ")
            numero_destino = input("Número de cuenta destino: ")
            if numero_origen in cuentas and numero_destino in cuentas:
                monto = float(input("Monto a transferir: "))
                cuentas[numero_origen].transferencia(monto, cuentas[numero_destino])
            else:
                print("Número de cuenta origen o destino no encontrado.")
        
        elif opcion == '5':
            numero = input("Número de cuenta de ahorros: ")
            if numero in cuentas and isinstance(cuentas[numero], CuentaAhorros):
                cuentas[numero].aplicar_interes()
            else:
                print("Número de cuenta no encontrado o no es una cuenta de ahorros.")
        
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()

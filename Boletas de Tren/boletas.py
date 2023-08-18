import random
import string

class MaquinaBoletos:
    destinos = {
        "A": {"nombre": "Bogota", "precio": 100000.00},
        "B": {"nombre": "Medellin", "precio": 50000.00},
        "C": {"nombre": "Cali", "precio": 25000.00}
    }

    def __init__(self):
        self.tarjeta_credito = None

    def mostrar_destinos(self):
        print("Destinos disponibles:")
        for letra, destino_info in self.destinos.items():
            print(f"{letra}: {destino_info['nombre']} - ${destino_info['precio']:.2f} COP")
    
    def seleccionar_destino(self):
        while True:
            destino = input("Seleccione un destino (A/B/C): ").upper()
            if destino in self.destinos:
                return destino
            else:
                print("Destino inválido. Por favor seleccione una opción válida.")

    def ingresar_tarjeta_credito(self):
        numero_tarjeta = input("Ingrese el número de su tarjeta de crédito: ")
        identificacion = input("Ingrese su Número de Identificación: ")
        # Realizar validación de tarjeta de crédito aquí (simulada para simplificar)
        self.tarjeta_credito = numero_tarjeta

    def validar_transaccion(self, monto):
        if self.tarjeta_credito:
            return True
        else:
            return False

    def generar_numero_boleto(self):
        caracteres = string.ascii_uppercase + string.digits
        numero_boleto = ''.join(random.choice(caracteres) for _ in range(10))
        return numero_boleto

    def emitir_boleto(self, destino):
        if self.validar_transaccion(self.destinos[destino]["precio"]):
            numero_boleto = self.generar_numero_boleto()
            nombre_destino = self.destinos[destino]["nombre"]
            print(f"Boleto a {nombre_destino} emitido.")
            print(f"Número de boleto: {numero_boleto}")
            print("¡Buen viaje!")
        else:
            print("No se pudo validar la transacción. No se emitió el boleto.")

def main():
    maquina_boletos = MaquinaBoletos()

    print("Bienvenido a la Máquina de Boletos!")
    maquina_boletos.mostrar_destinos()

    inicio = input("Presione el botón de inicio para comenzar (S/N): ").upper()
    if inicio == "S":
        maquina_boletos.mostrar_destinos()
        destino_seleccionado = maquina_boletos.seleccionar_destino()
        maquina_boletos.ingresar_tarjeta_credito()
        maquina_boletos.emitir_boleto(destino_seleccionado)
    else:
        print("¡Hasta luego!")

if __name__ == "__main__":
    main()

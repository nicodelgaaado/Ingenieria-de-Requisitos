class Calculadora:
    def __init__(self):
        self.valor1 = int(input("Ingrese el primer valor entero: "))
        self.valor2 = int(input("Ingrese el segundo valor entero: "))

    def suma(self):
        resultado = self.valor1 + self.valor2
        print(f"Suma: {self.valor1} + {self.valor2} = {resultado}")

    def resta(self):
        resultado = self.valor1 - self.valor2
        print(f"Resta: {self.valor1} - {self.valor2} = {resultado}")

    def multiplicacion(self):
        resultado = self.valor1 * self.valor2
        print(f"Multiplicación: {self.valor1} * {self.valor2} = {resultado}")

    def division(self):
        if self.valor2 == 0:
            print("Error: No se puede dividir por cero.")
        else:
            resultado = self.valor1 / self.valor2
            print(f"División: {self.valor1} / {self.valor2} = {resultado}")

# Crear una instancia de la clase Calculadora
mi_calculadora = Calculadora()

# Realizar las operaciones e imprimir los resultados
mi_calculadora.suma()
mi_calculadora.resta()
mi_calculadora.multiplicacion()
mi_calculadora.division()

class Usuario:
    def __init__(self, nombre, correo, marca_tarjeta, numero_tarjeta, vencimiento, codigo_verificacion):
        self.nombre = nombre
        self.correo = correo
        self.marca_tarjeta = marca_tarjeta
        self.numero_tarjeta = numero_tarjeta
        self.vencimiento = vencimiento
        self.codigo_verificacion = codigo_verificacion
        self.dispositivos = []
        self.compras = []
        self.puntos = 0

    def agregar_dispositivo(self, dispositivo):
        self.dispositivos.append(dispositivo)
        print(f"Dispositivo {dispositivo} agregado a tu cuenta.")

    def hacer_compra(self, aplicacion):
        self.compras.append(aplicacion)
        self.puntos += calcular_puntos(aplicacion.precio)
        print(f"Compra de {aplicacion.nombre} realizada con éxito.")
        print(f"Puntos acumulados: {self.puntos}")

    def canjear_premio(self, premio):
        if self.puntos >= premio.puntos_necesarios:
            self.puntos -= premio.puntos_necesarios
            certificado = generar_certificado(self, premio)
            print(f"¡Felicidades! Has canjeado el premio '{premio.nombre}'.")
            print(f"Puntos restantes: {self.puntos}")
            return certificado
        else:
            print("No tienes suficientes puntos para canjear este premio.")
            print(f"Puntos acumulados: {self.puntos}")

class Aplicacion:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Premio:
    def __init__(self, nombre, puntos_necesarios):
        self.nombre = nombre
        self.puntos_necesarios = puntos_necesarios

def calcular_puntos(monto):
    return int(monto / 10)

def generar_certificado(usuario, premio):
    certificado = f"CERTIFICADO\nUsuario: {usuario.nombre}\nPremio: {premio.nombre}"
    return certificado

# Ejemplo de uso
if __name__ == "__main__":
    print("¡Bienvenido a la plataforma de venta de aplicaciones Fandroid!")
    nombre = input("Ingrese su nombre: ")
    correo = input("Ingrese su correo electrónico: ")
    marca_tarjeta = input("Ingrese la marca de su tarjeta de crédito (Visa, MasterCard, American Express): ")
    numero_tarjeta = input("Ingrese el número de su tarjeta de crédito: ")
    vencimiento = input("Ingrese la fecha de vencimiento (mes/año): ")
    codigo_verificacion = input("Ingrese el código de verificación (tres dígitos): ")
    
    usuario1 = Usuario(nombre, correo, marca_tarjeta, numero_tarjeta, vencimiento, codigo_verificacion)

    while True:
        print("\nOpciones:")
        print("1. Agregar dispositivo")
        print("2. Comprar aplicación")
        print("3. Canjear premio")
        print("4. Ver información de cuenta")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            dispositivo = input("Ingrese el nombre del dispositivo: ")
            usuario1.agregar_dispositivo(dispositivo)
        elif opcion == "2":
            nombre_app = input("Ingrese el nombre de la aplicación: ")
            precio_app = float(input("Ingrese el precio de la aplicación: "))
            app = Aplicacion(nombre_app, precio_app)
            usuario1.hacer_compra(app)
        elif opcion == "3":
            nombre_premio = input("Ingrese el nombre del premio: ")
            puntos_premio = int(input("Ingrese los puntos necesarios para el premio: "))
            premio = Premio(nombre_premio, puntos_premio)
            certificado = usuario1.canjear_premio(premio)
            if certificado:
                print("Aquí está tu certificado:")
                print(certificado)
        elif opcion == "4":
            print("\nInformación de cuenta:")
            print(f"Nombre: {usuario1.nombre}")
            print(f"Correo: {usuario1.correo}")
            print(f"Número de tarjeta: {usuario1.tarjeta}")
            print(f"Dispositivos: {', '.join(usuario1.dispositivos)}")
            print(f"Compras realizadas: {len(usuario1.compras)}")
            print(f"Puntos acumulados: {usuario1.puntos}")
        elif opcion == "5":
            print("Gracias por utilizar la plataforma de venta de aplicaciones Fandroid. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

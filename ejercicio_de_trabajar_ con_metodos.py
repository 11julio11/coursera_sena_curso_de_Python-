class RegistroDePersonas:
    def __init__(self, nombre, apellido, edad, ciudad, codigo_postal):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ciudad = ciudad
        self.codigo_postal = codigo_postal

    def mostrar_info(self):
        """Muestra la información del registro."""
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Ciudad: {self.ciudad}")
        print(f"Código Postal: {self.codigo_postal}")

class Registro:
    def __init__(self):
        self.registros = []

    def agregar_registro(self):
        """Solicita al usuario que ingrese la información y la agrega a la lista de registros."""
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        edad = int(input("Ingrese la edad: "))
        ciudad = input("Ingrese la ciudad: ")
        codigo_postal = input("Ingrese el código postal: ")
        
        nuevo_registro = RegistroDePersonas(nombre, apellido, edad, ciudad, codigo_postal)
        self.registros.append(nuevo_registro)
        print("Registro agregado exitosamente.")

    def mostrar_registros(self):
        """Muestra todos los registros almacenados."""
        if not self.registros:
            print("No hay registros disponibles.")
        for idx, registro in enumerate(self.registros, 1):
            print(f"\nRegistro {idx}:")
            registro.mostrar_info()

def main():
    registro = Registro()
    while True:
        print("\n1. Agregar nuevo registro")
        print("2. Mostrar todos los registros")
        print("3. Salir")
        
        opcion = input("Seleccione una opción (1/2/3): ")
        
        if opcion == '1':
            registro.agregar_registro()
        elif opcion == '2':
            registro.mostrar_registros()
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()


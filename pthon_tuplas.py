#tupla
# my_tuple = 1 , 'etring', 4.5, True , False

# for x in my_tuple:
#   print(x)

'''
Ejercicio: Gestión de Inventario de Supermercado
Crea un programa que permita:

Añadir un nuevo producto con su precio al inventario.
Mostrar todos los productos y sus precios.
'''

# # Diccionario para almacenar productos y precios
# inventario = {}

# # Función para mostrar el menú
# def mostrar_menu():
#     print("\nBienvenido al Sistema de Gestión de Inventario del Supermercado")
#     print("1. Añadir producto")
#     print("2. Mostrar inventario")
#     print("3. Salir")

# # Función para añadir un producto al inventario
# def añadir_producto():
#     producto = input("Introduzca el nombre del producto: ")
#     precio = float(input("Introduzca el precio del producto: "))
#     inventario[producto] = precio
#     print("Producto añadido con éxito!")

# # Función para mostrar el inventario
# def mostrar_inventario():
#     print("\nInventario del Supermercado:")
#     for producto, precio in inventario.items():
#         print(f"{producto}: ${precio:.2f}")

# # Función principal que controla el flujo del programa
# def main():
#     while True:
#         mostrar_menu()
#         opcion = input("Elija una opción: ")
#         if opcion == '1':
#             añadir_producto()
#         elif opcion == '2':
#             mostrar_inventario()
#         elif opcion == '3':
#             print("Gracias por usar el sistema de gestión de inventario.")
#             break
#         else:
#             print("Opción no válida. Por favor, elija una opción del 1 al 3.")

# # Ejecutar la función principal
# if __name__ == "__main__":
#     main()

#---------------------------------------------------------------------------------------------------------------#
'''
#haga un programa que permita añadir sus rutas de aprendizaje y muestre las rutas de aprendizaje añadidas
'''

rutas_de_aprendizaje = {}

def Mostras_menu():
    print("\nle damos la bienvenida a su ruta de aprendizaje")
    print("1. Añadir nueva ruta de aprendizaje")
    print("2. Mostrar ruta de aprendizaje")
    print("3. Salir de ruta de aprendizaje")
    
def Añadir_ruta():
    nueva_ruta = input("coloque el nombre de la nueva ruta: ")
    precio_ruta = float(input("ingrese el costo de la nueva ruta: "))
    rutas_de_aprendizaje[nueva_ruta] = precio_ruta # type: ignore
    print("Ruta añadida con éxito!")

def Mostrar_rutas():
    print("\nrutas de aprendizaje:")
    for nueva_ruta, precio_ruta in rutas_de_aprendizaje.items():
        print(f"{nueva_ruta}: ${precio_ruta:.2f}")
        
def main():
    while True:
        Mostras_menu()
        opcion = input("Elija una opción: ")
        if opcion == '1':
            Añadir_ruta()
        elif opcion == '2':
            Mostrar_rutas()
        elif opcion == '3':
            print("Gracias por usar el sistema de gestión de rutas de aprendizaje.")
            break
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 3.")

# Ejecutar la función principal

if __name__ == "__main__":
    main()
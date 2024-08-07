# total_factura = 210
# descuento1 = 10
# descuento2 = 20

# if total_factura > 100 and total_factura < 200:
#     print('¡La factura es mayor que 100!')
#     total_factura = total_factura - descuento1

# elif total_factura > 200:
#     print("¡La factura es mayor que 200!")
#     total_factura = total_factura - descuento2

# else:
#     print("¡La factura es menor que 100!")

# print("Total de la factura: " + str(total_factura))

# def calcular_costo_curso(costo_de_curso):
#     descuento1 = 50
#     descuento2 = 45

#     if costo_de_curso > 500 and costo_de_curso < 500:
#         print('¡El valor del curso es mayor que 500!')
#         costo_de_curso -= descuento1
#     elif costo_de_curso > 500:
#         print('¡El costo del curso es mayor que 500!')
#         costo_de_curso -= descuento2
#     else:
#         print('¡El valor del curso es menor que 500!')

#     return costo_de_curso

# # Valor inicial del costo del curso
# costo_inicial = 520

# # Calcular el costo después de aplicar el descuento
# costo_final = calcular_costo_curso(costo_inicial)

# # Imprimir el costo final del curso
# print('El costo del curso: ' + str(costo_final))

#crea un programa que permita calcular la venta de mostos

def limpiar_y_convertir(valor):
    # Elimina los puntos y convierte el valor a float
    valor_limpio = valor.replace('.', '')
    return float(valor_limpio)

def calcular_venta_de_motos(cantidad_motos, precio_por_moto):
    # Calcular el total sin descuento
    total_venta = cantidad_motos * precio_por_moto
    
    # Aplicar descuentos según el total de la venta
    if total_venta > 500 and total_venta < 1000:
        descuento = 0.05  # 5% de descuento
        print('¡El total de la venta es mayor que 500, se aplica un 5% de descuento!')
    elif total_venta >= 1000:
        descuento = 0.10  # 10% de descuento
        print('¡El total de la venta es mayor que 1000, se aplica un 10% de descuento!')
    else:
        descuento = 0
        print('¡El total de la venta es menor que 500, no se aplica descuento!')

    total_con_descuento = total_venta * (1 - descuento)
    
    return total_con_descuento

def main():
    # Solicitar la cantidad de motos vendidas al usuario
    cantidad_motos = float(input('Ingrese la cantidad de motos vendidas: '))
    
    # Solicitar el precio por moto al usuario
    precio_por_moto_input = input('Ingrese el precio por moto (usando punto como separador decimal): $ ')
    precio_por_moto = limpiar_y_convertir(precio_por_moto_input)
    
    # Calcular el total de la venta
    total_final = calcular_venta_de_motos(cantidad_motos, precio_por_moto)
    
    # Mostrar el total de la venta
    print(f'El total de la venta después de aplicar descuentos es: $ {total_final:.2f}')

# Ejecutar el programa principal
if __name__ == '__main__':
    main()



    
    
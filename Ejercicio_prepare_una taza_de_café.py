'''
Introducción
En este ejercicio, practicará el uso de un algoritmo para preparar una taza de café instantáneo.
El objetivo es establecer los pasos necesarios para obtener el producto final. 

Instrucciones
Paso 1: Comience con las entradas: ¿qué se necesita para preparar una taza de café instantáneo?

Paso 2: Piense en todos los pasos necesarios en el aspecto físico para preparar una taza de café instantáneo.

Paso 3: Considere los casos extremos de productos opcionales como la leche o el azúcar, algunas personas pueden solicitarlos. 

Paso 4: El algoritmo cuando está completo debería tener como resultado final "una taza de café".

Consejos: la planificación es clave con cualquier algoritmo. Asegúrese de tener todos los pasos bien ordenados. 
'''

def preparar_cafe(tiene_azucar=False, cantidad_azucar=0, tiene_leche=False, cantidad_leche=0):
    # Paso 1: Llenar el hervidor con agua y hervirla
    print("1. Llenar el hervidor con agua.")
    print("2. Encender el hervidor y esperar a que el agua hierva.")

    # Paso 2: Preparar la taza
    print("3. Colocar una taza en la mesa.")
    print("4. Añadir una cucharada de café instantáneo en la taza.")

    # Paso 3: Verter el agua hervida en la taza
    print("5. Verter el agua hervida en la taza.")
    print("6. Remover con una cuchara hasta que el café esté completamente disuelto.")

    # Paso 4: Añadir azúcar si se desea
    if tiene_azucar:
        print(f"7. Añadir {cantidad_azucar} cucharada(s) de azúcar.")
        print("8. Remover hasta que el azúcar esté completamente disuelta.")

    # Paso 5: Añadir leche si se desea
    if tiene_leche:
        print(f"9. Añadir {cantidad_leche} cantidad de leche.")
        print("10. Remover hasta que la leche esté completamente mezclada.")

    # Resultado final
    print("11. ¡Disfrutar de tu taza de café!")

# Ejemplo de uso
preparar_cafe(tiene_azucar=True, cantidad_azucar=2, tiene_leche=True, cantidad_leche=1)

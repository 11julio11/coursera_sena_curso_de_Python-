'''
Instrucciones
1.   En num_list cree un bucle "for" nuevo e imprima cada valor de la lista en orden secuencial.

2. Dentro del bucle "for", cree una condición que busque todos los números mayores que 45 e imprima solo números que cumplan esa condición.

3. Cambie la sentencia "print" a "Más de 45" y agregue una condición "else" con una sentencia "print" de "Menos de 45".

4. Actualice el bucle "for" para utilizar la función enumerar y poder obtener y utilizar el índice. Modifique la condición para buscar el número 36 e imprima lo siguiente: "Número encontrado en la posición:", número de índice

5. A continuación, cree una nueva variable denominada "count", asígnele el valor 0 y ubíquela fuera del bucle "for".

6. Dentro del bucle "for" incremente el contador en 1.

7. Agregue una sentencia "print" fuera del bucle "for" para imprimir el valor de la variable "count".

8. Por último, agregue una sentencia "break" directamente luego de la sentencia "print" dentro de la condición "if" para encontrar el número. 

'''
# # Paso 1: Crear la lista num_list
# num_list = [10, 20, 36, 48, 55, 30, 42, 60, 75]

# # Paso 5: Crear la variable count y asignarle el valor 0
# count = 0

# # Paso 1-7: Crear un bucle "for" para imprimir cada valor de la lista en orden secuencial y realizar las operaciones
# for index, num in enumerate(num_list):
#     # Paso 6: Incrementar el contador en 1
#     count += 1

#     # Paso 2-4: Crear condiciones para buscar números mayores a 45 y el número 36
#     if num == 36:
#         print("Número encontrado en la posición:", index)
#         # Paso 8: Agregar una sentencia "break"
#         break
#     elif num > 45:
#         print("Más de 45")
#     else:
#         print("Menos de 45")

# # Paso 7: Imprimir el valor de la variable count fuera del bucle "for"
# print("Total de iteraciones:", count)

#---------------------------------------------------------------------------------------------------------------------------------------------#

# #lista de frutas
# # Definición de la lista de frutas
# lista_frutas = ['mango', 'pera', 'manzana', 'banana', 'uva', 'piña', 'fresa', 'melon', 'durazno', 'caimito']

# # Inicialización del contador
# count = 0

# # Bucle para iterar sobre la lista de frutas
# for index, fruta in enumerate(lista_frutas):
#     count += 1  # Incrementar el contador
    
#     if fruta == 'manzana':
#         print("La fruta encontrada en la posición:", index)
#         break
#     elif fruta == 'manzana':  # Cambié la comparación a una verificación si es 'coco'
#         print('Hay poquito cocos')
#     else:
#         print('No hay cocos')

# # Imprimir el total de iteraciones
# print('Total de iteraciones:', count)



'''
Introducción a kwargs:

Kwargs permite pasar cualquier cantidad de argumentos con palabras clave a una función.
Se utiliza el doble asterisco (**) para definir kwargs.
Con kwargs, se puede acceder a los valores utilizando las palabras clave asociadas.
Ejemplo de uso de kwargs:

Se muestra un ejemplo de cómo calcular el total de una cuenta de restaurante utilizando kwargs.
Se utiliza un bucle for para iterar a través de los argumentos y sumar los valores.
Se utiliza la función round para limitar el resultado a dos decimales.
'''

def sum_of(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    return round(sum, 2)
        

print(sum_of(coffee=2.99, cake=4.55, juice=2.99))
'''
Introducción a args:

Args permite pasar cualquier cantidad de variables sin palabras clave a una función.
Se utiliza el símbolo de asterisco (*) para definir args.
Con args, se puede iterar a través de los argumentos y realizar operaciones con ellos.

Ejemplo de uso de args:

Se muestra un ejemplo de una función de suma que acepta dos parámetros, a y b.
Si se intenta pasar un tercer valor sin args, se produce un error.
Al utilizar args, se puede pasar cualquier cantidad de argumentos y obtener la suma total.

'''


def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum
        

print(sum_of(4, 5, 6, 9, 6, 5, 4))
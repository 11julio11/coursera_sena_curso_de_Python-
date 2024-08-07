'''
Una excepción es un error que ocurre durante la ejecución de un programa. Por ejemplo, si intentas dividir un número entre cero,
Python mostrará un error de "división por cero".

Para manejar estas excepciones de manera más amigable para el usuario, 
puedes utilizar las declaraciones "try" y "except" en Python. La declaración "try" se utiliza para ejecutar un 
bloque de código que podría generar una excepción. Si ocurre una excepción, la declaración "except" se ejecuta y puedes mostrar un mensaje
de error personalizado en lugar del mensaje de error predeterminado de Python.

Por ejemplo, si tienes una función que divide dos números, puedes envolver el código 
de la función en un bloque "try". Si ocurre una excepción, puedes mostrar un mensaje de error personalizado en el bloque "except". 
Esto ayuda a que los usuarios comprendan mejor el error y cómo solucionarlo.

En resumen, el manejo de excepciones en Python te permite controlar los errores que ocurren durante la ejecución de tu programa
y mostrar mensajes de error más amigables para los usuarios.

'''

def divide_by(a, b):
    return a / b

try:
    ans = divide_by(40, 0)
except ZeroDivisionError as e:
    print(e, "we cannet divide by zero")
except Exception as e:
    print(e, "something went wroung")
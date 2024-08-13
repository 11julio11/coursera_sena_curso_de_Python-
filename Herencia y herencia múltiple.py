# '''
# Herencia simple: La herencia simple en Python se 
# realiza pasando la clase padre como parámetro a la
# clase hija. Esto permite que la clase hija acceda a 
# los atributos y métodos de la clase padre. Ejemplo de 
# código:
# '''

# class A: # type: ignore
#     def method_a(self):
#         print("This is method A")

# class B: # type: ignore
#     def method_b(self):
#         print("This is method B")

# b = B()
# b.method.a # type: ignore
# b.method_b()

# '''
# Herencia múltiple: Python también permite la herencia múltiple, donde una clase puede heredar
# de múltiples clases. El orden de las clases es importante. Ejemplo de código:
# '''
# class A:
#     def method_a(self):
#         print("This is method A")

# class B:
#     def method_b(self):
#         print("This is method B")

# class C(A, B):
#     def method_c(self):
#         print("This is method C")

# c = C()
# c.method_a()  # Output: This is method A
# c.method_b()  # Output: This is method B
# c.method_c() 

# Herencia de varios niveles: En la herencia de varios niveles, una clase derivada hereda de una clase base que a su vez hereda de otra clase base. Ejemplo de código:
# class A:
#     def method_a(self):
#         print("This is method A")

# class B(A): # type: ignore
#     def method_b(self):
#         print("This is method B")

# class C(B):
#     def method_c(self):
#         print("This is method C")

# c = C()
# c.method_a()  # Output: This is method A
# c.method_b()  # Output: This is method B
# c.method_c()  # Output: This is method C
# "Funciones integradas: Python proporciona dos funciones integradas útiles para trabajar con clases y objetos: issubclass() e isinstance(). issubclass() verifica si una clase es una subclase de otra, mientras que isinstance() verifica si un objeto es una instancia de una clase. Ejemplo de código:"
# class A:
#     pass

# class B(A):
#     pass

# print(issubclass(B, A))  # Output: True
# print(isinstance(B(), A))  # Output: True
# Función super(): La función super() se utiliza para acceder a los métodos y variables de las clases padre o hermanas en una clase derivada. Ayuda a gestionar el flujo de ejecución del código y permite la inicialización de la clase base en la clase derivada. Ejemplo de código:
# class Fruit:
#     def __init__(self, fruit):
#         print('Fruit type:', fruit)

# class FruitFlavour(Fruit):
#     def __init__(self):
#         super().__init__('Apple')
#         print('Apple is sweet')

# apple = FruitFlavour()  # Output: Fruit type: Apple, Apple is sweet
# Espero que esto te ayude a entender los conceptos de herencia y funciones integradas en Python. Si tienes alguna otra pregunta, no dudes en preguntar.
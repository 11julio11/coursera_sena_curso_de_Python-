# def sum(n):
#     if n == 1:
#         return 0
#     return n + sum(n-1)

# a = sum(5)
# print(a)

# numbers = [15, 30, 47, 82, 95]
# def lesser(numbers):
#     return numbers < 50

# small = list(filter(lesser, numbers))
# print(small)   

# class Alpha:

# # def __init__ (self):
# #  self._a = 2. # Protected member 'a'
# #  self.__b = 2. # Private member 'b' 


# Programa para preguntar cómo mejorar en Python
def mejorar_en_python():
    # Preguntar al usuario cómo mejorar en Python
    respuesta = input("¿Qué debe hacer un estudiante para mejorar sus conocimientos en Python? ")
    
    # Preguntar al usuario si ha investigado sobre el tema que está estudiando
    ayuda = input("¿Has investigado sobre el tema que estás estudiando para mejorar? ")

    # Condicional que pide información adicional sobre el horario de dormir
    if respuesta.lower() in ["estudiar mas", "practicar mas", "dedicar más tiempo"]:
        horario = input("¿Cuál es tu horario de dormir? ")
        print(f"\nEs importante balancear tu tiempo de estudio y descanso. Dormir a las {horario} podría ayudarte a ser más productivo.")
    
    # Condicional que sugiere buscar ayuda adicional
    if ayuda.lower() in ["no se nada", "no tengo tiempo", "no se por donde empezar"]:
        buscar_habitos = input("Busca ayuda con una persona que sepa del tema: ")
        print("\nDebes ser autodidacta y ser más creativo en tu aprendizaje.")

    # Mostrar la respuesta principal del usuario    
    print("\nGracias por tu consejo. Tu recomendación es:\n")
    print(f"- {respuesta}")

# Ejecutar la función
mejorar_en_python() 
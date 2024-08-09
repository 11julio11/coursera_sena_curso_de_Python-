# # # class Myclass:
# # #     a = 5
    
# # #     def hello(self):
# # #         print("Hello, world!")
    
# # # #instancia de Myclass        
# # # myc = Myclass()

# # # #imprimimos el atributo 'a'
# # # print(myc.a)

# # # #llamr al metodo 'hello0
# # # myc.hello() 

# # #----------------------------------------------------------------#
# # class House:
# #     '''
# #     This class represents a house and provides methods to evaluate different metrics, such as the cost of constructing the house.
# #     '''
    
# #     def __init__(self, num_rooms=5, bathrooms=2):
# #         '''
# #         Initializes a new House object with the specified number of rooms and bathrooms.
        
# #         :param num_rooms: Number of rooms in the house.
# #         :param bathrooms: Number of bathrooms in the house.
# #         '''
# #         self.num_rooms = num_rooms
# #         self.bathrooms = bathrooms

# #     def cost_evaluation(self, area, cost_per_square_meter):
# #         '''
# #         Evaluates the cost of constructing the house based on its area and cost per square meter.
        
# #         :param area: The total area of the house in square meters.
# #         :param cost_per_square_meter: The cost of construction per square meter.
# #         :return: The total estimated cost of constructing the house.
# #         '''
# #         total_cost = area * cost_per_square_meter
# #         print(f"The total cost of constructing the house is: ${total_cost:.2f}")
# #         return total_cost

# #     def __str__(self):
# #         '''
# #         Returns a string representation of the House object, including the number of rooms and bathrooms.
# #         '''
# #         return f"House with {self.num_rooms} rooms and {self.bathrooms} bathrooms."

# # # Crear una instancia de la clase House
# # my_house = House(num_rooms=4, bathrooms=3)

# # # Imprimir la representación en cadena de la instancia
# # print(my_house)

# # # Evaluar el costo de construcción
# area = 150  # área en metros cuadrados
#  cost_per_square_meter = 1000  # costo por metro cuadrado en la moneda local
#  my_house.cost_evaluation(area, cost_per_square_meter)


#---------------------------------------------------------------------#


value = 7 
class A:
    value = 5
a = A()
a.value = 3
print(value)


bravo = 3
b = B()  # type: ignore
class B:
    bravo = 5
    print("Inside class B")
c = B()
print(b.bravo)



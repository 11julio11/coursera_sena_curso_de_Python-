# class Recipe():
#     def __init__(self, dish, items, time) -> None:
#         self.dish = dish
#         self.items = items
#         self.time = time
    
#     def contents(self):
#         print("the" + self.dish + "has" +str(self.items) +\
#               "and takes " + str(self.time) + "min to propare")
        
# pizza = Recipe("pizza", ["cheese", "bread", "tomato"], 45)
# pasta = Recipe("pasta", ["penne", "saure"], 55)

# print(pizza.items)
# print(pasta.items)

# print(pizza.contents())

##############################################
# Diccionario de colores
colores = {
    1: 'amarillo',
    2: 'azul',
    3: 'rojo',
    4: 'blanco',
}


# Clase para manejar la selección de colores
class Colors:
    def escoger(self): 
        elegir_color = input('Escoge un color (amarillo, azul, rojo, blanco): ').lower()
        
        # Validar si el color escogido está en el diccionario
        for key, value in colores.items():
            if value == elegir_color:
                print(f"Has escogido el color {elegir_color}, que corresponde al número {key}.")
                return key, value
        
        # Si el color no se encuentra en el diccionario
        print("Color no encontrado, por favor escoge uno de la lista.")
        return None

# Crear una instancia de la clase Colors
color_selector = Colors()

# Llamar al método escoger para probarlo
color_selector.escoger()

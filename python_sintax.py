
#funcion1
name = "David"
if name == "David":
    print(name)

#funcion2 

def estres_maxivo():
    return "preocupacion severa"

print(estres_maxivo())

#funcion3

def colors():
    color1 = input("Introduce el primer color: ")
    color2 = input("Introduce el segundo color: ")
    color3 = input("Introduce el tercer color: ")
    
    # Multiplicar las cadenas por números específicos
    combined_color = color1 * 2 + color2 * 2 + color3 * 2
    
    # Comparar la cadena resultante con una cadena específica
    if combined_color == color1 + color1 + color2 + color2 + color3 + color3:
        return "muchos colores"
    
    print("colors")

# Llamar a la función
print(colors())





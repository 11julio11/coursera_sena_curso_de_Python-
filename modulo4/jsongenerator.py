# jsongenerator.py

import json  # Paso 2: Importar el paquete json integrado
from employee import details, employee_name, age, title  # Paso 3: Importar la función details y las variables

def create_dict(name, age, title):
    """ Creates a dictionary that stores an employee's information

    Args:
        name: Name of employee
        age: Age of employee
        title: Title of employee

    Returns:
        dict - A dictionary that maps "first_name", "age", and "title" to the
               name, age, and title arguments, respectively. Make sure that 
               the values are typecasted correctly (name - string, age - int, 
               title - string)
    """
    # Paso 4: Implementar la función create_dict
    employee_dict = {
        "first_name": name,
        "age": int(age),  # Asegurarse de que el valor de edad sea un entero
        "title": title
    }
    return employee_dict

def write_json_to_file(json_obj, output_file):
    """ Write json string to file

    Args:
        json_obj: json string containing employee information
        output_file: the file the json is being written to
    """
    # Paso 6: Implementar la función write_json_to_file
    with open(output_file, "w") as newfile:
        newfile.write(json_obj)
        # El archivo se cierra automáticamente al salir del bloque with

def main():
    # Imprimir el contenido de details() -- Esto debe imprimir los detalles del empleado
    details()

    # Crear el diccionario del empleado
    employee_dict = create_dict(employee_name, age, title)
    print("employee_dict: " + str(employee_dict))

    # Paso 5: Convertir employee_dict en una cadena JSON
    json_object = json.dumps(employee_dict)
    print("json_object: " + str(json_object))

    # Escribir el objeto JSON en un archivo
    write_json_to_file(json_object, "employee.json")

if __name__ == "__main__":
    main()

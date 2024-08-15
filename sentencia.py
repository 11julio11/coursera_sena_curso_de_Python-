'''
declaraciones de importación para acceder a módulos 
desde diferentes directorios. También aprenderás cómo crear paquetes 
desde el índice de paquetes de Python utilizando pip. Cada archivo de Python,
que significa cualquier archivo con extensión .py que contiene un script, es efectivamente
un módulo. El archivo "check imports" que se está creando actualmente es, por lo tanto, un
módulo para algunos de los archivos. El código con el que estás trabajando se llama generalmente el 
módulo principal. En este caso, "check imports" es el módulo principal presente en el directorio de trabajo actual. 
También llamado el alcance del proyecto, puedes importar cualquier archivo de Python que esté presente en el alcance actual.
Por ejemplo, puedes importar el archivo "sample.py" escribiendo "import" seguido del nombre del archivo sin la extensión.
Luego, haces clic en "run" en el menú superior. El sistema devuelve un mensaje en el pin del terminal de que la importación 
fue exitosa. Si intentas importar un archivo con extensión .txt, la importación no será exitosa. Por ejemplo, si escribes 
"import sample_text" y haces clic en "run", el sistema devolverá un mensaje de error en el pin del terminal, ya que no es un 
archivo de Python. Python tiene una biblioteca de módulos estándar llamados módulos integrados. Estos módulos están directamente 
integrados en el intérprete de Python y no es necesario instalarlos por separado. Puedes importar un módulo como "json" escribiendo 
"import json". Una vez que ejecutas el comando, puedes comenzar a usar sus funciones directamente. La lista de módulos integrados se 
puede encontrar en la biblioteca estándar de Python. Puedes pensar en los paquetes como la estructuración de los módulos de Python como
una colección. Se requieren archivos especiales llamados archivos init.py para que Python trate los directorios que contienen el archivo 
como paquetes. Python tiene una amplia colección de paquetes creados por la comunidad que se pueden encontrar en el índice de paquetes de 
Python, o pyPI. Pyp o pyp3 es el instalador de paquetes predeterminado para Python y ayuda con la instalación de paquetes desde pyPI. 
Dado que ya has instalado numpy, puedes importarlo directamente en Python. Haces esto escribiendo "import numpy", limpiando tu terminal
y haciendo clic en "run". Si intentas importar un paquete que no está instalado, recibirás un mensaje de error. Por ejemplo, si escribes
"import seaborn" y haces clic en "run", se devolverá el mensaje "ModuleNotFoundError". Si el paquete seaborn estuviera instalado, podrías
ejecutar el comando nuevamente en Python sin ningún mensaje de error. Para hacer esto, ejecutarías "pip install seaborn" en el terminal 
para descargar el paquete desde el índice de pyPI. También puedes importar archivos que hayas creado en una de las carpetas dentro del 
directorio de trabajo actual. Tienes una carpeta llamada "workplace" que contiene un archivo llamado "trial.py". El archivo consiste en 
una lista con los nombres de variables y dos entradas dentro de ella. Voy a importar este archivo y acceder a su contenido. Comienzo 
importando el módulo "sys". Luego uso una función "path" en "sys" escribiendo "sys.path.insert". Ahora debo ingresar el nombre de la 
ruta a mi paquete "workplace" en la primera ubicación del índice. Para hacer esto, hago clic derecho en el directorio "workplace" y 
selecciono "copy path". Ingreso este nombre de ruta como la primera ubicación del índice al pasar la ruta como argumento. Debo usar 
comillas simples y escribir la letra R delante de la cadena de la ruta. La lista "sys.path" ahora tiene un nuevo directorio donde
buscará módulos. Ahora debo importar mi archivo "trial" aquí escribiendo "import trial" y presionando enter. Aparece una línea 
ondulada debajo de la palabra "trial". Esto se debe a que el IDE no conoce la ruta que he agregado dentro de "sys.path". 
Sin embargo, aún puedo continuar ya que el intérprete conocerá esta ruta. Para imprimir la salida, escribo "print" seguido de 
"trial.names" y hago clic en el botón "run" para ejecutarlo. Se imprimen los valores de "Adrian" y "Maria" de la variable "names" S
de la lista. En este video, aprendiste cómo se pueden importar módulos desde cualquier lugar dentro de tu sistema, aunque insertar 
el nombre de la ruta puede ser muy específico y a menudo confuso. No te preocupes demasiado por esto por ahora. Es más importante 

centrarse en importar archivos desde el directorio actual. Es bueno saber que importar módulos desde otros directorios es una opción
si la necesitas. Sin embargo, es una buena práctica mover los archivos requeridos al directorio en el que estás trabajando.

'''
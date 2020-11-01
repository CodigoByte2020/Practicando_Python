'''Se carga sólo una vez por importacion de módulo, y se crea un archivo en la carpeta __pycache__,
Siempre y cuando no cambiemos de lugar el módulo a importar'''

# Se importan todos los componentes y toda la funcionalidad del módulo
from modulo_vehiculos2 import *

mi_chatarra = Vehiculo("aluminio", 1500)
print(mi_chatarra.informacion())


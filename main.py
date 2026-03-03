
"""
import os
from dotenv import load_dotenv
load_dotenv()

## VARIABLES DE ENTORNO
CLAVE = os.getenv("CLAVE")

print('hola, planetaaaaa')
print('baaaai')
print(CLAVE)


## sdasdasdd titulos
#@ sadasdasd subtitulos y descripciones
#! asdasd problemas y atencion
#* sdasdasd otros
#? sdasdasd enlaces o investigacion
"""

import os
from dotenv import load_dotenv
load_dotenv()

DB_PORT = os.getenv('DB_PORT')
DB_HOST = os.getenv('DB_HOST') #no subir con default
DB_USER = os.getenv('DB_USER', "AdminPostgreSQL")
print(DB_HOST)
print(DB_PORT)
print(DB_USER)
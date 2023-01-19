print('hello (pre gen)')

import os
import sys

#invocamos el nombre del proyecto y lo asignamos a una variable para usarlo en el archivo
project_slug = "{{ cookiecutter.project_slug }}"

ERROR_COLOR = "\x1b[31m" # le asignamos un color para que se vea en la terminal
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL =  "\x1b[0m"

# si el nombre empieza con x, no es válido
if project_slug.startswith("x"):
    print(f"{ERROR_COLOR}ERROR: {project_slug=} is not a valid name for this template")
    
    sys.exit(1) #se aborta la ejecución de creación de plantilla
    
print(f"{MESSAGE_COLOR}Let's do it! You're going to create something awesome")
print(f"Creating project at { os.getcwd()} {RESET_ALL}")






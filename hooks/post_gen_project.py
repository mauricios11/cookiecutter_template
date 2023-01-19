print('Template generated successfully (post gen)')

#iniciar un repositorio de git, una vez creado el proyecto
import subprocess #lo usamos para ejecutar comandos en la terminal

MESSAGE_COLOR = "\x1b[34m" #colores que se mostrarán en la terminal
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR} almost done!")
print(f"Initializing a git repository . . . {RESET_ALL}")

#ejecutando comandos
subprocess.call(['git', 'init']) # iniciar el repositorio
subprocess.call(['git','add', '*']) #agregar todos los archivos que se encuentren en el template
subprocess.call(['git', 'commit', '-m', 'Initial commit']) # hará el primer commit llamado "initial c"

print(f"{MESSAGE_COLOR} The beginning of yout destiny is defined now! Create and have fun :D{RESET_ALL}")
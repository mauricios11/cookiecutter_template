print("Hello :D")

import os
import sys

project_slug = "{{ cookiecutter.project_slug }}"

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR_B = "\x1b[34m"
MESSAGE_COLOR_G = "\x1b[32m"
RESET_ALL = "\x1b[0m"

if project_slug.startswith("x"):
    print(f"{ERROR_COLOR}ERROR:  uuuuuy no, that name {project_slug=} is not valid for this template :/")
    sys.exit(1)
        
print(f"{MESSAGE_COLOR_B}Template creation process initalized ")
print(f" *Template location: {os.getcwd()}{RESET_ALL}")

import os
import sys
import subprocess

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR_C = "\x1b[36m"
MESSAGE_COLOR_B = "\x1b[34m"
MESSAGE_COLOR_Y = "\x1b[33m"
MESSAGE_COLOR_G = "\x1b[32m"

RESET_ALL = "\x1b[0m"

activate_git = input("Do you want to initialize git? [yes] [no]:")

if activate_git == "yes":
    subprocess.call(['git', 'init'])
    subprocess.call(['git', 'add', '*'])
    subprocess.call(['git' ,'commit', '-m', 'Initial commit'])
    subprocess.call(['git','branch','-M', 'main'])

input_ =input("Do you want to install the enviroment? [y][n]: ")

if input_ == "y":
    conda_or_mamba = input(f"select the package manager mamba[1], conda[2]: ")
    if conda_or_mamba == "1":
        subprocess.call(['mamba', 'env', 'create', '--file', 'enviroment.yml'])
        
    if conda_or_mamba == "2":
        subprocess.call(['conda', 'env', 'create', '--file', 'enviroment.yml'])
          
else:
    print(f"{MESSAGE_COLOR_B}To create the enviroment you need to choose a package manager: [1]mamba [2]conda")
    print(f"{MESSAGE_COLOR_Y} use: [conda | mamba] env create --file enviroment.yml")
    
print(f"{MESSAGE_COLOR_G}The template has been successfully created in the next location:")
print(f"{os.getcwd()}{RESET_ALL}")
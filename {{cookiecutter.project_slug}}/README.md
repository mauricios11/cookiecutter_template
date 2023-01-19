# {{ cookiecutter.project_title }}

By: {{ cookiecutter.project_author_name }}

Short description: {{ cookiecutter.project_description }}

Version: {{ cookiecutter.project_version }}

## Prerequisites
packages: {{ cookiecutter.project_packages }}
python version: {{ cookiecutter.python_version }}


## How to activate the enviroment
you could review the libraries and dependencies to use in *eviroment.yalm* file

- Create a new enviroment with conda:

```
conda env create -f environment.yml
activate {{ cookiecutter.project_slug }}
```

- If you are using pip
  
create a new enviroment to this proyect (env is the enviroment's name, so could have another name) 

``` 
python3 -m venv env
```

then activate

``` 
source env/bin/activate
```
finally install the libraries:

``` 
pip install -r requirements.txt 
```



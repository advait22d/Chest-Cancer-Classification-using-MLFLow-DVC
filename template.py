#This script is used to make a basic folder structure for the project. This template can be used to create a similar folder structure in any other projects
import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s:')

project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py", #The __init__.py constructor file will help me to create this folder as my local package
    f"src/{project_name}/components/__init__.py",#This will create data ingestion, data validation, model jnr, prepare-based model etc functionalities
    f"src/{project_name}/utils/__init__.py",#This will have utility related code
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",#before implementing any kind of modular coding we do the experiment with this notebook. If it works fine we will convert this notebook to modular coding
    "templates/index.html"


]



for filepath in list_of_files:
    filepath = Path(filepath) #This converts the file path to the format of the pc os(windows, linux,etc)
    filedir, filename = os.path.split(filepath) 


    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")
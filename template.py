import os
from pathlib import Path
import logging

# Create Logging string
# Displays Information and format of the Log
# Extracts ascii time and prints message
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'cnnClassifier'

list_of_files = [
                ".github/workflows/.gitkeep",
                 f"src/{project_name}/__init__.py",
                 f"src/{project_name}/components/__init__.py",
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
                 "research/trials.ipynb",
                 "templates/index.html",
                 "test.py"
                 ]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")
        
    if not os.path.exists(filepath) or (os.path.getsize(filepath) == 0) : 
        with open(filepath,"w") as f:
            pass
        logging.info(f"Creating Empty file: {filepath}")
        
    else:
        logging.info(f"{filename} already exists")
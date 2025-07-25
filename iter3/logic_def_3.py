import os 
from dotenv import load_dotenv
from pathlib import Path
from typing import Dict
import shutil 
from utils import check_path, get_ENV, get_origin_path, dir_is_empty, create_dir

## TODO Obten origin dir path and Check it exist

def validate_directory(path:str)->bool:
    path_obj=Path(path)
    return Path.exists(path_obj)


## TODO  Check origin is not empty (utility tool)

## TODO Classify stuff and create dedicate dirs 

def classifier(origin_path:str,categories:Dict)->bool:
    try:
        parent_dir=os.path.dirname(origin_path)
        for path_list in os.listdir(origin_path):
            root, ext = os.path.splitext(path_list)
            for key,value in categories.items():
                if ext in value:
                    cat_path=os.path.join(parent_dir,key)
                    if create_dir(parent_dir=parent_dir,target=key) or check_path(cat_path):
                    ### Move file to dir
                        origin=os.path.join(origin_path,path_list)
                        shutil.move(Path(origin),Path(cat_path))
        return True
    except Exception as e:
        print(e)
        return False

           
## TODO - clean dir  
def clean_dir(target_path:str):
    path=Path(target_path)
    if Path.is_dir(path):
        for file in os.listdir(path):
            file_path=Path(os.path.join(path,file))
            if Path.is_file(file_path):
                os.remove(file_path)
                print(f"File: {file} succesfully removed")

    
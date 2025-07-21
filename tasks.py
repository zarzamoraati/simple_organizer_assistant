from pathlib import Path
from typing import Dict,List
import os 
from iter2.utils import transfer_files


# TODO - Vlidate directory exists and not empty 

def validate_directory(path:str)->bool:
    path_obj=Path(path)
    return Path.exists(path_obj)


# TODO - List and Classify stuff within a given directory into categories

def classifier(origin_path:str, categories:List[str])->Dict:
    ##TODO list content and classify
    paths=os.listdir(origin_path)
    categories={"media":[],"file":[]} ## TODO - refactoring avoid hardcoding

    for path in paths:
        if path.endswith(("txt","pdf","epub")):
            categories["file"].append(path)
        elif path.endswith(("avi","mp4","mp3","jpg","jpeg","gif","png")):
            categories["media"].append(path)
    return categories   
    ## TODO - REFACTORING REPETITIVE TASK 


# TODO - Cretae dedicate directories base on that categories 

def make_dir(cat_list:list,origin_path:str)->Dict:
    try:    
        cat_directories={}
        for cat in cat_list:
            dest_path=os.path.dirname(origin_path)
            temp_path=os.path.join(dest_path,cat)
            Path.mkdir(Path(temp_path),exist_ok=True,parents=True)
            cat_directories[cat]=temp_path
            print(f"Directorie:{cat},succesfully created")
        return cat_directories
    except Exception as e:
        print(e)



# TODO - Move stuff to its correspond directorie
def move_files(src_cat:Dict,dest_cat:Dict,origin:str)->None:
    try:
        #TODO get dest directories
        for cat in dest_cat:
            transfer_files(src_cat,cat,dest_cat,origin)    
    except Exception as e:
        print(e)




# TODO - Remove all the stuff that not match in any categorie

def clean_dir(dir_path:str):
    dir_path=Path(dir_path)
    try:
        if Path.is_dir(dir_path):
            for item in os.listdir(dir_path): ## REFACTORING -> handle subdirectories too
                os.remove(os.path.join(dir_path,item)) 
                
        print(f"Directories:{dir_path},succesfully removed")
    except Exception as e:
        print(e)
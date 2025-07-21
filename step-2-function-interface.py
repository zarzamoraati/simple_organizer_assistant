from pathlib import Path
from typing import Dict,List
import os 

# TODO - Vlidate directory exists and not empty 

def validate_directory(path:str)->bool:
    return Path.exists(path)

# TODO - List and Classify stuff within a given directory into categories

def classifier(origin_path:str, categories:List[str])->Dict:
    ##TODO list content and classify
    paths=os.listdir(origin_path)
    categories={"media":[],"file":[]} ## TODO - refactoring avoid hardcoding

    for path in paths:
        if path.endswith("txt","pdf","epub"):
            categories["file"].append(path)
        elif path.endswith("avi","mp4","mp3","jpg","jpeg","gif","png"):
            categories["media"].append(path)
    return categories   
    ## TODO - REFACTORING REPETITIVE TASK 


# TODO - Cretae dedicate directories base on that categories 

def make_dir(*args,origin_path:str)->Dict:
    try:
        cat_directories={}
        for cat in args:
            temp_path=os.path.join(origin_path,cat)
            Path.mkdir(temp_path,exist_ok=True,parents=True)
            cat_directories[cat]=temp_path
            print(f"Directorie:{cat},succesfully created")
        return cat_directories
    except:
        print("Something went wrong")


# TODO - Move stuff to its correspond directorie
def move_files(src_cat:Dict,dest_cat:Dict)->None:
    try:
        #TODO get dest directories
        for cat in dest_cat:
            transfer_files(src_cat,cat,dest_cat)    
    except:
        print("Something went wrong")


def transfer_files(src_cat:Dict,cat,dest_cat)->None: ## TODO move to utilities
    for file_src_path in src_cat[cat]:
        shutil.move(file_src_path,dest_cat[cat])

# TODO - Remove all the stuff that not match in any categorie

def clean_dir(dir_path:str):
    try:
        os.remove(dir_path)
        print(f"Directories:{dir_path},succesfully removed")
    except:
        print("Something went wrong")


# TODO - Chck origin is empty 
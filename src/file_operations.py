import os
from pathlib import Path
import shutil 
from typing import Dict
from utilities import dir_is_empty,valid_dir,valid_file,join_path


def create_dir(origin:str)->str:
    try:
        Path.mkdir(Path(origin),exist_ok=True,parents=True)
        return origin
    except Exception as e:
        print(e)
        return ""

def move_files(src:str,dst:str)->bool:
    try:
        shutil.move(Path(src),Path(dst))
        return True
    except Exception as e:
        print(e)
        return False

def undo_changes(files_log:list[tuple])->bool:
    #Check if any movement is doing yet
    if not len(files_log) > 0:
        print("No logs matched yet")
        return False
    prev_path,new_path=list(reversed(files_log))[0]
    #Check if src and dst are still valid paths 
    if not valid_dir(prev_path):
        print(f"Previos path:{prev_path}, not founded")
        return False
    #Check if the file exist 
    if not valid_file(new_path):
        print(f"Filepath:{new_path}, not founded")
        return False
    
    move_files(new_path,prev_path)
    return True


def clean_dir(origin_path:str):
    if not valid_dir(origin_path) or dir_is_empty(origin_path):
        return 
    
    for path in os.listdir(origin_path):
        complete_path=join_path(origin_path,path)
        if valid_file(complete_path):
            os.remove(complete_path)
        
        
    
    
    

    
    

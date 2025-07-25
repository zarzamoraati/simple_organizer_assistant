import os
from pathlib import Path


def join_path(root:str,sub_path:str)->str:
    return os.path.join(root,sub_path) 

def dir_is_empty(origin:str)->bool:
    if len(os.listdir(origin)) > 0:
        return False
    else:
        return True 

def valid_dir(origin:str)->bool:
    print("hello2",origin)
    return os.path.exists(Path(origin)) and os.path.isdir(Path(origin))

def valid_file(origin:str)->bool:
    return os.path.isfile(Path(origin))

def obtain_basename(origin:str)->str:
    return os.path.basename(origin)

def obtain_ext(basename:str)->tuple:
    return os.path.splitext(Path(basename))

def obtain_parent(origin:str)->str:
    return os.path.dirname(Path(origin))

def list_files(origin_path:str)->list:
    return os.listdir(Path(origin_path))





   
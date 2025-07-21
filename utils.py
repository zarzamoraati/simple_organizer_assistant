import os 
from dotenv import load_dotenv
from pathlib import Path
from typing import Dict

def create_cat()->Dict:
    category={"text":(".txt",".pdf",".epub"),"media":(".mp4",".avi",".jpg",".png",".gif",".mp3")}
    return category

def create_dir(parent_dir:str,target:str)->bool:
    path_dir=os.path.join(parent_dir,target)
    try:
        Path.mkdir(Path(path_dir),parents=True)
        return True
    except Exception as e:
        print(e)
        return False

        
def check_path(path:str):
    path_obj=Path(path)
    return Path.exists(path_obj)    

def get_origin_path(origin:str):
    origin_path=get_ENV(path=origin)
    return check_path(path=origin_path)
    
def get_ENV(path:str):
    return os.getenv(path)
    

def dir_is_empty(path:str)->bool:
    if len(os.listdir(path)) == 0:
        return True
    else:
        return False


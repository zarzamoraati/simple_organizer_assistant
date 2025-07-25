import os
from pathlib import Path
import shutil 
from typing import Dict
from utilities import dir_is_empty,valid_dir,valid_file,join_path, obtain_ext
from configuration import CATEGORIES



def create_dir(origin:str)->bool:
    try:
        Path.mkdir(Path(origin),exist_ok=True,parents=True)
        return True
    except Exception as e:
        print(e)
        return False

def move_file(src:str,cat:str,log_operation)->bool:
    try:
        # print(src)
        # print(cat)
        newdir_path=os.path.join(src,cat)  
        if not create_dir(newdir_path):
            print(f"Directory {newdir_path}, couldn't be created")
            return False
        for basename  in os.listdir(src):
            ## TODO CLASSIFICA 
                if cat in CATEGORIES:
                    valid_ext=CATEGORIES[cat]
                    name,ext=obtain_ext(basename=basename)
                    if ext in valid_ext:
                        ## move the file  
                        file_path = os.path.join(src,basename)
                        shutil.move(file_path,newdir_path)
                        print(f"File:{basename}, moved to {newdir_path}")
                        dest_path=join_path(newdir_path,basename)

                        log_operation.register_mov(type_mov="move",mov=(src,dest_path))
        return True
    except Exception as e:
        print(e)
        return False

# def undo_changes(files_log:list[tuple])->bool:


#     #Check if any movement is doing yet
#     if not len(files_log) > 0:
#         print("No logs matched yet")
#         return False
#     prev_path,new_path=list(reversed(files_log))[0]
#     #Check if src and dst are still valid paths 
#     if not valid_dir(prev_path):
#         print(f"Previos path:{prev_path}, not founded")
#         return False
#     #Check if the file exist 
#     if not valid_file(new_path):
#         print(f"Filepath:{new_path}, not founded")
#         return False
    
#     move_files(new_path,prev_path)
#     return True


def clean_dir(origin_path:str):
    if not valid_dir(origin_path) or dir_is_empty(origin_path):
        return 
    
    for path in os.listdir(origin_path):
        complete_path=join_path(origin_path,path)
        if valid_file(complete_path):
            os.remove(complete_path)
        
        
    
    
    

    
    

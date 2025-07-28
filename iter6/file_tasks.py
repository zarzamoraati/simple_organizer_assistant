from pathlib import Path
from utilities import check_is_file, join_path,check_is_dir, buil_command
from configuration import keywords
import os 
import re
import subprocess
import shutil


def check_dir_exists(path_dir:str)->bool:
    return Path.exists(Path(path_dir)) and Path.is_dir(Path(path_dir))

def create_dir(path_dir:str)->bool:
    try:
        Path.mkdir(Path(path_dir),exist_ok=True)
        return True
    except Exception as e:
        print(e)
        return False
    
def remove_no_tar_files(source:str): ### checked
    ## remove all files except tar files
    for basename in os.listdir(source):
        #obtain ext
        file_path=join_path(source,basename)

        name,ext=os.path.splitext(basename)
        if check_is_file(file_path) and not ext == ".tar":
            try:
                os.remove(file_path)
                print(f"Removing File {file_path}")
            except Exception as e:
                print(e)
                return 

def handle_discharged_files(origin_path:str,dest_path): #CHECKED
    for basename in os.listdir(origin_path):
        file_path=join_path(origin_path,basename)
        name, ext = os.path.splitext(basename)
        if check_is_file(file_path):
            try:
                dir_path=join_path(origin_path,dest_path)
                Path.mkdir(Path(dir_path),exist_ok=True)
                shutil.move(file_path,dir_path)
            except Exception as e:
                print(e)

def classifier(source:str):##CHECKED
    # TODO classify files
    for basename in os.listdir(source):
        full_path=join_path(source,basename)
        if check_is_file(full_path):
            name,_=os.path.splitext(basename)
            matched_keyword = None
                   
            for keyword in keywords:
                normalized_name = re.sub(r'[_\-]', ' ', name).lower()
                words = normalized_name.split()
                key_lower = keyword.lower()
                matched = False
                # Check exact word matches
                if key_lower in words:
                    matched = True
                else:
                    # Check each word segment for substring match (even if underscores/dashes exist)
                    for segment in words:
                        if key_lower in segment:
                            matched = True
                            break
                if matched:
                    matched_keyword = keyword
                    #print(f"Matched keyword: {matched_keyword} in {name}")
                    break

            if matched_keyword:
               keyword_dir=join_path(source,matched_keyword)
               create_dir(keyword_dir)
               shutil.move(full_path,keyword_dir)

    #  TODO HANDLE DESCHARGED FILES
    handle_discharged_files(origin_path=source,dest_path="others")

def process_to_tar(origin:str): ##CHECKED

    for basename in os.listdir(origin):
        full_path=join_path(origin,basename)
        if check_is_dir(full_path):
            command=buil_command(full_path,"tar")
            try:
                subprocess.run(command,cwd=full_path)
                remove_no_tar_files(full_path)
            except Exception as e:
                print(e)

def compress_directories(origin):##CHECKED
    command=buil_command(source=origin,type="zip",tar_files=False)
    try:
        subprocess.run(command,cwd=origin)
    except Exception as e:
        print(e)      

def delete_subdirs(origin:str):## CHECKED 
    for basename in os.listdir(origin):
        full_path=join_path(origin,basename)
        if check_is_dir(full_path):
            try:
                shutil.rmtree(full_path)
            except Exception as e:
                print(e)
        
def move_compressed_files(source:str,dest:str):
    if check_is_dir(source):
        
        for basename in os.listdir(source):
            _,ext = os.path.splitext(basename)
            if ext == ".7z":
                full_path=join_path(source,basename)
                try:
                    Path.mkdir(dest,exist_ok=True)
                    shutil.move(full_path,dest)
                except Exception as e :
                    print(e)
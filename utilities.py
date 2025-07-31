import os 
from pathlib import Path
import json
from configuration import password,json_file

def check_is_file(source_path:str)->bool:##checked
    return os.path.isfile(Path(source_path))

def check_is_dir(source_path:str)->bool: ##checked
    return os.path.isdir(source_path)

def join_path(source:str,name:str)->str:##checked
    return os.path.join(source,name)

def check_dir_exists(path_dir:str)->bool: ##checked
    return Path.exists(Path(path_dir)) and Path.is_dir(Path(path_dir))


def get_session()->int|None: ## checked
    init_json={"session":1}
    try:
        if not os.path.exists(json_file):
            # create it 
            with open(json_file,"w") as file:
                json.dump(init_json,file,indent=4)
            
       
        with open(json_file,"r") as file:
            loaded_dict=json.load(file)

        counter=loaded_dict["session"]
        loaded_dict["session"]= counter + 1

        with open(json_file,"w") as file:
            json.dump(loaded_dict,file,indent=4)
        
        return counter
            
    except Exception as e:
        print(e)
        return None


def obtain_basenames(source:str,is_file:bool=True)->list[str]: ##checked
    basename_list=[]

    for path in os.listdir(source):
        full_path=join_path(source,path)
        if is_file and check_is_file(full_path):
            basename_list.append(path)
        elif check_is_dir(full_path):
            basename_list.append(path)

    return basename_list


def buil_command(source:str,type:str,tar_files:bool=True)->str|None: ##checked
    
    basename_list=obtain_basenames(source,is_file=tar_files)
    basename=os.path.basename(source)
    command = None
    if type == "tar":
        command=['tar','-cvf',f'{basename}.tar'] + basename_list
    # print(str_command)
    if type == "zip":
        ## implement read json method to obtain session number
        session_serie=get_session()
        if session_serie:
            command=['7z','a',f'session{session_serie}.7z','-mhe=on',f'-p{password}'] + basename_list
    
    if command:
        print(command)
        return command
    return None



def classifier(basename:str,keywords:set):
    pass

def get_basename()->str:
    pass
def get_name()->str:
    pass
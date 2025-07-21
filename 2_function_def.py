## TODO Obten origin dir path and Check it exist
from utils import get_ENV,check_path


def get_origin_path(origin:str)-> bool:
    origin_path=get_ENV(path=origin)
    return check_path(path=origin_path)
    


## TODO  Check origin is not empty 

def dir_is_empty(path:str)->bool:
    return 

## TODO Classify stuff and create dedicate dirs 

def classifier(origin_path:str)->None:
    return 
    
## TODO Move stuff to dedicate dirs , remove eveything else 
def move_files(origin_path:str,dest_path:Dict)->None:
    return 
## TODO  Check origin is clean

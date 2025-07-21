import shutil 
from typing import Dict,List
from dotenv import load_dotenv
import os 

load_dotenv()

def get_ENV(*args)->List[str]:
    return [os.getenv(env_path) for env_path in args]

def transfer_files(src_cat:Dict,cat,dest_cat,origin)->None: ## TODO move to utilities
    for file_src_path in src_cat[cat]:
        origin_path=os.path.join(origin,file_src_path)
        shutil.move(origin_path,dest_cat[cat])
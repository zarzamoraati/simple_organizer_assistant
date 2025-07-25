
from logic_def_3 import validate_directory, classifier, clean_dir
from iter2.utils import get_ENV
from utils import create_cat,dir_is_empty

def assistant_organizer():
# TODO - get origin path 
    origin=get_ENV(("DOWNLOAD_DIR"))[0]
# TODO - Vlidate directory exists and not empty 
    if not validate_directory(origin) or dir_is_empty(origin):
        print("Invalid or empty directory")
        return 
# TODO -  Classify stuff , create dedicate dirs and move stuff to them
    else: 
        cat_obj=create_cat()
        state=classifier(origin_path=origin,categories=cat_obj)
        if state :
                clean_dir(origin)
        else:
             print("Something went wrong")
             return


assistant_organizer()
                                
                    
            
        
    



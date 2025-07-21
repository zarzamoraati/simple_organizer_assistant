from tasks import validate_directory,classifier,make_dir,move_files,clean_dir
from utils import get_ENV

def assistant_organizer():
# TODO - get origin path 
    origin=get_ENV(["DOWNLOAD_DIR"])[0]
# TODO - Vlidate directory exists and not empty 
    if not validate_directory(origin):
        print("Invalid path or directory")
        return 
# TODO -  Classify stuff within a given directory into categories
    else:
        src_cat_paths=classifier(origin,("media","text"))
# TODO - Cretae dedicate directories base on that categories 
        categories=[cat for cat in src_cat_paths]
        dest_cat_paths=make_dir(origin, categories)
# TODO - Move stuff to its correspond directorie
        move_files(src_cat_paths,dest_cat_paths)
# TODO - Remove all the stuff that not match in any categorie
        clean_dir(origin)
# TODO - Chck origin is empty 
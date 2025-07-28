from utilities import join_path,check_is_file,check_is_dir,buil_command
from typing import  Dict
from file_tasks import  create_dir
import os 
import shutil 
import subprocess
from pathlib import Path
from configuration import keywords
from file_tasks import remove_no_tar_files, handle_discharged_files,classifier

## TODO LOW LOGIC 

# origin_dir="/home/polo/Descargas/test"

# # create dir dummy

# dummy_path_dir=join_path(origin_dir,"dummy")
# if not check_dir_exists(dummy_path_dir):
#     create_dir(dummy_path_dir)

# # # move only files

# for basename in os.listdir(origin_dir):
#     path=join_path(origin_dir,basename)
#     if check_is_file(path):
#         try:
#             shutil.move(path,dummy_path_dir)
#         except Exception as e:
#             print(e)

# tar files within a directory 
    # Obtain file names

    ## Build command

#source="/home/polo/Descargas/test/dummy"

# command=buil_command(source=source,type="tar")

#     ## use subprocess to run the command 

# try:
#     subprocess.run(command, cwd=source)
# except Exception as e:
#     print(e)

# ## TODO clean dedicate subdirs after tar file is creacted 



# remove_no_tar_files(source=source)


# compress only directories on a single file zip


#source="/home/polo/Descargas/test/dummy"
# source="/home/polo/Descargas/test"

#     ## obtain coammd to compress subdirectories  

# command=buil_command(source=source,type="zip",tar_files=False)    

# try:
#     subprocess.run(command,cwd=source)
# except Exception as e:
#     print(e)


## TODO HANDLE STUFF NOT FIT ON ANY CATEGORIE 



# source="/home/polo/Descargas/test"
# dest="others"

# handle_discharged_files(source,dest)

## TODO HIGH LOGIC  LOGIC 




# TODO TAR FILES IN EACH DIRECTORY 



## TODO compress directories



## TODO delete directoies



source="/home/polo/Descargas/test"

#classifier(source=source)

# print(keywords)
# print(keywords.split())

# KEYWORDS=["lick","licking","mom"]

# names=["image","file1"]
# for name in names:

#     if any(key in name for key in KEYWORDS):
#         print(name)


# file1="swudu.pdf"

# name,ext=os.path.splitext(file1)

#test 1 - shouldn't match 

#print(any(key in name for key in KEYWORDS))

#test 2 - TRUE?

# file2="image.jpg"
# name,ext=os.path.splitext(file2)


# print(any(key in name for key in KEYWORDS))


#test 3 - TRUE?

# file3="file1.txt"
# name,ext=os.path.splitext(file3)


# print(any(key in name for key in KEYWORDS))



def move_compressed_files(source:str,dest:str): ##CHECKED
    if check_is_dir(source):
        
        for basename in os.listdir(source):
            _,ext = os.path.splitext(basename)
            if ext == ".7z":
                full_path=join_path(source,basename)
                try:
                    Path.mkdir(Path(dest),exist_ok=True)
                    shutil.move(full_path,dest)
                except Exception as e :
                    print(e)


move_compressed_files(source=source,dest="/home/polo/Descargas/compressed_downloads")
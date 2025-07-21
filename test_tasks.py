import pytest 
from utils import create_cat
import os
from logic_def_3 import classifier, validate_directory
from pathlib import Path
from utils import dir_is_empty,create_dir
import shutil



# TODO Check shape and content of cat obj 

def test_validate_obj():
    cat_obj=create_cat()
    assert "text" in cat_obj
    assert "media" in cat_obj
    assert not "stuff" in cat_obj
    assert isinstance(cat_obj["text"], tuple)
    assert len(cat_obj["text"]) > 0 
    assert not isinstance(cat_obj["text"][0],bool)
    assert isinstance(cat_obj["text"][0],str)
    assert isinstance(cat_obj["media"], tuple)
    assert len(cat_obj["media"]) > 0
    assert not isinstance(cat_obj["media"][0],bool)
    assert isinstance(cat_obj["text"][0],str)


## TODO  Check dir exists 

def test_validate_dir():
    dummy_path="something/dir1/dir2"
    real_path=os.getcwd()
    
    assert isinstance(validate_directory(dummy_path),bool)
    assert validate_directory(dummy_path) == False
    assert validate_directory(real_path) == True


## TODO  Check origin is not empty 
def test_is_empty():
    # Create empty dir
    temp_path_empty=os.path.join(Path(os.getcwd(),"empty"))
    temp_path_noempty=os.path.join(Path(os.getcwd(),"noempty"))
    parent=os.getcwd()
    create_dir(parent_dir=parent, target=temp_path_empty)
    create_dir(parent_dir=parent,target=temp_path_noempty)

    ## pupulate no-empty dir
    n=3
    try:
        for i in range(n): 
            with open(f"dummy{i}.txt","x") as file:
                file.write("lorenipsus")
                file.close()
            origin=os.path.join(os.getcwd(),f"dummy{i}.txt")
            shutil.move(Path(origin),Path(temp_path_noempty))
    ## assert
        print(len(os.listdir(temp_path_empty)),len(os.listdir(temp_path_noempty)))
        assert dir_is_empty(temp_path_noempty) == False
        assert dir_is_empty(temp_path_empty) == True
              
    except FileExistsError as e:
        print(e)
         


import pytest
from utilities import obtain_basename,join_path,dir_is_empty,valid_dir,valid_file,obtain_ext,obtain_parent
import os


## TODO testing configurations

## TODO testing utilities

def test_utils():
    
    real_path="/home/polo/Documentos/VSCode/VSCode/Projects/Stage1/assistant-organizer/objectives.py"
    dummy_path="Documentos/VSCode/VSCode/Projects/Stage1/dumdum"
    
    ## should return the basename of givenpath on string format 
    basename=obtain_basename(real_path)
    dummy_basename=obtain_basename(dummy_path)
    

    assert isinstance(basename, str)
    assert isinstance(dummy_basename,str)

    ## shoudl retur a tuple of both root and ext 
    ext_tuple=obtain_ext(basename=basename)
    name,ext=ext_tuple

    assert isinstance(ext_tuple,tuple) 
    assert not isinstance(ext_tuple,list)
    assert isinstance(name,str)
    assert isinstance(ext,str)

    ## should return True if the path refer to an existing dir or False on any other case
    
    assert not valid_dir(basename) 
    
    parent_path=obtain_parent(real_path)
    
    assert valid_dir(parent_path)
    

    ## Should return True if the path refers to an existing file or False on any other case

    assert valid_file(real_path)
    
    assert not valid_file(parent_path)

    ## Should return True if a valid dir is empty and False on any other case 

    work_dir=os.getcwd()
    empty_dir=os.path.join(work_dir,"temp")
    
    assert not dir_is_empty(work_dir)

    assert dir_is_empty(empty_dir)

    ## should return a full path on str format

    path_join=join_path(work_dir,"something")
    
    assert isinstance(path_join,str)

    assert obtain_basename(path_join) == "something"

    assert obtain_parent(path_join) == work_dir
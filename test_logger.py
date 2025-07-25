import pytest
from log_operations import store_movement
from typing import Dict


def test_loger():
    ## store movement shoudl return None when either typeofmove or moves are not defined

    assert store_movement(type_mov="",mov=("something","hello"))== None
    
    ## store movement should return None of we pass  an empty tuple

    assert store_movement(type_mov="copy",mov=()) == None

    ## Store movement should return a dictionary in any other case 

    assert isinstance(store_movement(type_mov="delete",mov=("src","dst")),Dict) 

    ##  The key returned shoudl have the same value as the key input

    movements=store_movement(type_mov="delete",mov=("src","dst")) 

    assert "delete" in movements

    assert len(movements["delete"]) == 1

    assert isinstance(movements["delete"][0],tuple)
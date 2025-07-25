from typing import Dict

## This should converted to a class since diff types of mov require a different structure to storage moves

def store_movement(action:str,payload:tuple)->Dict|None:
    movement={}
    if not isinstance(action,str) or action == "" or not payload:
        return None
    print(f"New movement was made: \nType:{action}\nChange:{payload}")
    if not action in movement:
        movement[action]=[]
    movement[action].append(payload)
    return movement

    
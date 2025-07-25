from abc import ABC,abstractmethod
from file_operations import create_dir,move_file,clean_dir
from configuration import CATEGORIES, ORIGIN_DIR
from utilities import valid_dir, valid_file, join_path, dir_is_empty, obtain_basename, obtain_ext, obtain_parent,list_files
from config_logger import valid_moves
from time import time

### Inyectar todos los parametros paar acda estrategia  

### define concrete strategies like MoveItems

        ### define a implement strategy for each ocncret strategy that use user input
         

class LogSystem(ABC):
    # @property
    # @abstractmethod
    # def movements():
    #     pass

    @abstractmethod
    def register_mov(self,type_mov:str,mov:tuple):
        pass


class Logger(LogSystem):
    def __init__(self):
        self.movements={} 
            
    def register_mov(self, type_mov:str, mov:tuple):
       #movements=store_movement(action=type_mov,payload=mov)
        if not type_mov in self.movements:
           self.movements[type_mov]=[]
        print(f"Logging new operation, \nType:{type_mov}\npayload:{mov}")
        self.movements[type_mov].append(mov)

        
        ## change to a dictionary to avoid redundancy , instead of have a list of dicts 
        ## better have a dict with keys (types of move) tath mpa to its specific data soreage strcture


    # @property
    # def movements(self):  # Implement the abstract property
    #     return self._movements



class FileStrategy(ABC):
    @abstractmethod
    def implementStrategy(self,log_operation:Logger,source:str="",category:str=""):
        pass

class MoveOperation(FileStrategy):
    def __init__(self):
        self.valid_cat={"1":"File","2":"Video","3":"Image","4":"Music"}
        
    def implementStrategy(self,log_operation:Logger,source:str="",category:str=""):
        
        if source and category:##REFACTORING
            if not move_file(source,category,log_operation):
                print("Operation 'moving file' failed")
                return
            print(f"succesfully moving {category} files to new directory")
            return 
        

        directory_path=input("Type the name of full path of the directory")
        userResponse=""
        while  not userResponse == "5":            
            categorie=input("Type the categorie file you want to move:\n1)File\n2)Video\n3)Image\n4)Music\n")
            
            if not categorie in self.valid_cat: 
                print("Categoria no valida, intentelo de nuevo")
                continue
            
            if not move_file(directory_path,self.valid_cat[categorie],log_operation):##REFACTORING
                print("Operation 'moving file' failed")
                continue
            print(f"succesfully moving {self.valid_cat[categorie]} files to new directory")

            userResponse=input("pulse q para salir o cualquier otra tecla para ingresar otro directorio")
            
        
class HandleFile(ABC):
    @abstractmethod
    def organize(self,called_by_user:bool=True):
        pass
    # @abstractmethod
    # def undo_operation(self,movement):
    #     pass


class FileOrganizer(HandleFile):

    def __init__(self,movements:Logger):
        #self.operation_log=[]
        self.logger=movements
        self.last_action=""
        #self.origin_path=ORIGIN_DIR ## inject this through user input
        #self.categories=CATEGORIES ## inject this through organize method or user inputs
        self._valid_actions={"1":MoveOperation}
        
    def organize(self,called_by_user:bool=True,payload:tuple=None):
        
        if not called_by_user :
           src,cat = payload
           move_operation= MoveOperation()
           move_operation.implementStrategy(log_operation=self.logger,source=src,category=cat) ## modfy implemnet strategy to recive cron parameters
           ## print the exact time when the operation was made
           
           return 
        
        file_operation=""
        while file_operation != "6":
            file_operation=input("Seleccione una accion : \n1)Move\n2)Copy\n3)Delete\n4)Compress\n5)Undo Changes\n6)Exit")
   

            if not file_operation in self._valid_actions:
                print("No a valid action")
                continue
            if file_operation == "1":
                operation=self._valid_actions[file_operation]()
                self.last_action="move"
                operation.implementStrategy(log_operation=self.logger)
            if  file_operation == "5" and self.last_action:
                continue
                #undo_operation(self.last_action)
            
                
        # # select Strategy
        # if movement in self.moves:
        #     ## call strategy
            
        #     concrete_strategy=self.strategy.select_strategy[movement]
            
            
        #     if movement == "move":


        #         ## TODO create dedicate dir
        #         for cat in self.categories:
        #             base_path=obtain_parent(self.origin_path)
        #             new_dir=join_path(base_path,cat)
        #             create_dir(new_dir)

                    
        #         ## TODO move files 
        #         parent_dir=obtain_parent(self.origin_path)
        #         for file_path in list_files(self.origin_path):
        #             file_path=join_path(self.origin_path,file_path)
        #             basename=obtain_basename(file_path)
        #             name,ext=obtain_ext(basename=basename)
        #             for cat,ext_files in self.categories.items():
        #                 if ext in ext_files:
        #                     ## move that file to its corresponding cat
        #                     dest_path=join_path(parent_dir,cat)
        #                     dest_path_file=join_path(dest_path,name)
        #                     self.operation.register_mov(type_mov=movement,mov=(self.origin_path,dest_path_file))
        #                     #self.operation_log.append((self.origin_path,dest_path_file))
        #                     #move_files(file_path,dest_path)
        #                     concrete_strategy(file_path,dest_path)
                                
        #         ## TODO clean origin dir
        #         clean_dir(self.origin_path)
        
        
        # def undo_operation(self,last_action:str):
        #     ## Implement different startegies depending of the last action
        #     pass




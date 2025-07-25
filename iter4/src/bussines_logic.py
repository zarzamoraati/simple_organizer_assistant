from abc import ABC,abstractmethod
from file_operations import create_dir,move_files,undo_changes,clean_dir
from configuration import CATEGORIES, ORIGIN_DIR
from utilities import valid_dir, valid_file, join_path, dir_is_empty, obtain_basename, obtain_ext, obtain_parent,list_files
class HandleFile(ABC):
    
    @abstractmethod
    def organize(self):
        pass
    @abstractmethod
    def undo_operation(self):
        pass


class FileOrganizer(HandleFile):

    def __init__(self):
        self.operation_log=[]
        self.origin_path=ORIGIN_DIR
        self.categories=CATEGORIES
        
    def organize(self):
        ## TODO validate origin dir 
        if not valid_dir(self.origin_path):
            return
        ## TODO check is not empty 
        elif dir_is_empty(self.origin_path):
            return
        ## TODO get categories

        ## new files are gonna move 

        self.operation_log.clear()

        ## TODO create dedicate dir
        for cat in self.categories:
            base_path=obtain_parent(self.origin_path)
            new_dir=join_path(base_path,cat)
            dest_dir=create_dir(new_dir)

            
        ## TODO move files 
        parent_dir=obtain_parent(self.origin_path)
        for file_path in list_files(self.origin_path):
            file_path=join_path(self.origin_path,file_path)
            basename=obtain_basename(file_path)
            name,ext=obtain_ext(basename=basename)
            for cat,ext_files in self.categories.items():
                if ext in ext_files:
                    ## move that file to its corresponding cat
                    dest_path=join_path(parent_dir,cat)
                    dest_path_file=join_path(dest_path,name)
                    self.operation_log.append((self.origin_path,dest_path_file))
                    move_files(file_path,dest_path)
        
        ## TODO clean origin dir
        clean_dir(self.origin_path)
        
        
    def undo_operation(self):
        if not undo_changes(self.operation_log):
            return 
        else:
            print("Latest change discarded succesfully ")





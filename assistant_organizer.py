from abc import ABC,abstractmethod
from file_tasks import classifier, process_to_tar, compress_directories,move_compressed_files,delete_subdirs

class Organizer(ABC):

    @abstractmethod
    def implementPipeline():
        pass

class PipeOrganizer(Organizer):
    def __init__(self,path:str,compress_dest:str):
        self.origin_path=path
        self.compress_dest=compress_dest

    ## TODO Build pipleine
    def implementPipeline(self):
            ## TODO Classify and move files
                classifier(source=self.origin_path)
            # TODO TAR FILES IN EACH DIRECTORY 
                process_to_tar(origin=self.origin_path)
            ## TODO compress directories
                compress_directories(origin=self.origin_path)
            ## TODO delete directoies
                delete_subdirs(self.origin_path)
            ## TODO move compressed files
                move_compressed_files(self.origin_path,self.compress_dest)
                
                

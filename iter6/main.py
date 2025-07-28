from assistant_organizer import PipeOrganizer
from configuration import compress_path, origin_path


pipe=PipeOrganizer(path=origin_path,compress_dest=compress_path)

pipe.implementPipeline()

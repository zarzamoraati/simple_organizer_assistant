from utilities import valid_dir
import os
from pathlib import Path 



real_path="/home/polo/Documentos/VSCode/VSCode/Projects/Stage1/assistant-organizer/objectives.py"


basename= os.path.basename(Path(real_path))
print(basename)



parent=os.path.dirname(real_path)
print(parent)

print(os.path.isdir(parent))

print(os.getcwd())

print(os.listdir(os.getcwd()))

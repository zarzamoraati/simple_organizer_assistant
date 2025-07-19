import os
from dotenv import load_dotenv
import shutil


load_dotenv()

#print(os.listdir(os.getenv("DOWNLOAD_DIR")))
origin_dir=os.getenv("DOWNLOAD_DIR")
text_dir=os.getenv("TEXT_DIR")

temp_path=""
for paths in os.listdir(origin_dir):
    temp_path=os.path.join(origin_dir,paths)
    if temp_path.endswith(("txt","pdf")):
        shutil.move(temp_path,text_dir)
        print(temp_path)
    if os.path.exists(temp_path):
        os.remove(temp_path)


    




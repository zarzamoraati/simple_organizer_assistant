import os
from dotenv import load_dotenv
import shutil
load_dotenv()

#print(os.getenv("DOWNLOAD_DIR"))

origin_dir=os.getenv("DOWNLOAD_DIR")

# media_dir=os.getenv("MEDIA_DIR")
# text_dir=os.getenv("TEXT_DIR")
media_dir=None
text_dir=None
print(origin_dir)
print(os.path.dirname(origin_dir))

def main(media_dir=media_dir,text_dir=text_dir, origin_dir=origin_dir):
    #TODO Check if origin directory exist 
    if not os.path.exists(origin_dir):
        return
    else:
    #TODO Check if subdirectories exist 
        temp_dir=""
        if not media_dir:
            #TODO create media dir 
            temp_dir=os.path.dirname(origin_dir)
            media_dir=os.path.join(temp_dir,"media")
            os.mkdir(media_dir)
        if not text_dir:
            #TODO create text dir
            temp_dir=os.path.dirname(origin_dir)
            text_dir=os.path.join(temp_dir,"text")
            os.mkdir(text_dir)

    #TODO Check for files on origin directory
        
        if len(os.listdir(origin_dir))==0: # REPLACE WITH os.path.exist()
            print("Directory is empty")
            exit()
                # 
        else:
            #TODO Classify files
            temp_dir="" 
            for paths in os.listdir(origin_dir):
                temp_dir=os.path.join(origin_dir,paths)
                if temp_dir.endswith(("txt","pdf","epub")):
                    ## TODO move to text dir
                    shutil.move(temp_dir,text_dir)
                if temp_dir.endswith(("gif", "jpg","jpeg","png","tiff","webp","mp4","avi","mkv")):
                    ## TODO move to media dir 
                    shutil.move(temp_dir,media_dir)
                 ## TODO Remove any other stuff
                
                if os.path.exists(temp_dir):
                    os.remove(temp_dir)

main(media_dir,text_dir,origin_dir)

                
                
                
                                
                    
            
        
    



import os
from dotenv import load_dotenv

load_dotenv()

#print(os.getenv("DOWNLOAD_DIR"))

origin_dir=os.getenv("DOWNLOAD_DIR")

media_dir=os.getenv("MEDIA_DIR")
text_dir=os.getenv("TEXT_DIR")

print(origin_dir)
print(os.path.dirname(origin_dir))

# def main():
#     #TODO Check if origin directory exist 
#     if origin_dir == None:
#         print("Download directory not exists")
#     else:
#     #TODO Check if subdirectories exist
#         if media_dir == None:
#             #TODO create media dir 
        
#         if text_dir == None:
#             #TODO create text dir
            
            
        
    



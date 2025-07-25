from dotenv import load_dotenv
import os
load_dotenv()

ORIGIN_DIR=os.getenv("DOWNLOAD_DIR")

CATEGORIES={"File":(".txt",".pdf","epub"),"Media":(".avi",".mp4",".jpg",".png",".gif",".webp",".mp3")}
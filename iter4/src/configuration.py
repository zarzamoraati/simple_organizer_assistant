from dotenv import load_dotenv
import os
load_dotenv()

ORIGIN_DIR=os.getenv("DOWNLOAD_DIR")

CATEGORIES={"text":(".txt",".pdf","epub"),"media":(".avi",".mp4",".jpg",".png",".gif",".webp",".mp3")}
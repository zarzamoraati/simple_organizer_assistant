from dotenv import load_dotenv
import os 
import json
load_dotenv()

password=os.getenv("PASS")
json_file=os.getenv("JSON_FILE_NAME")
keywords_string=os.getenv("KEYWORDS")
keywords=json.loads(keywords_string)

origin_path=os.getenv("ORIGIN")
compress_path=os.getenv("COMPRESS_PATH")
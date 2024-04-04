# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "22547959")

API_HASH = os.environ.get("API_HASH", "3f27ae243c72d6ca397afb9194e5c89e")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

FORCE_SUB = os.environ.get("FORCE_SUB", "GAURAV_BOTS") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "Hackx")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://Hackx:Hackx@hackx.6flteju.mongodb.net/?retryWrites=true&w=majority&appName=Hackx")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/d5d23e541737366550aef.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5606411877').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

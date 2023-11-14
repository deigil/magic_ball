from supabase import create_client, Client
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
    
def insert_word(text):
    local_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    url = os.getenv('url')
    key = os.getenv('key')
    supabase: Client = create_client(url, key)
    # Log the user in to Supabase
    data = supabase.auth.sign_in_with_password({"email": "afranco7@hawk.iit.edu", "password": "smartpenreader2023"})
    print(data.user.id)

    word_object = {
        "created_at": local_time,
        "text": text,
        "favorite": False,
        "user_id": data.user.id,
    }
    
    # Insert the word into Supabase
    supabase.table("words").insert(word_object).execute()
    supabase.auth.sign_out()

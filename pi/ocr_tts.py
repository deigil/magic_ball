from picamera2 import Picamera2
import pytesseract
import time
import os
from supabase import create_client, Client
import time
import datetime
import time
from PIL import Image

def supabase_initialization():
    url = "https://mqalxvluagdxoihxjlsm.supabase.co"
    key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1xYWx4dmx1YWdkeG9paHhqbHNtIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTgzNDgzNDIsImV4cCI6MjAxMzkyNDM0Mn0.t3cNfV9Has7pvCZTw7ObN91IRjOaxVWcoUnFXiJZAL4"
    supabase: Client = create_client(url, key)

    # Log the user in to Supabase
    data = supabase.auth.sign_in_with_password({"email": "afranco7@hawk.iit.edu", "password": "smartpenreader2023"})
    # print(data)

    # user = supabase.auth.getUser()
    print(data.user.id)

    # Return the variables supabase, session_token, and user_id
    return supabase, data.user.id

# Check file output path
if not os.path.exists("/home/borat/Desktop/output"):
    os.makedirs("/home/borat/Desktop/output")
image_path = "/home/borat/Desktop/output/img.jpg"

def ocr_tts():
    picam2 = Picamera2()
    picam2.configure()
    # Start the camera
    picam2.start(show_preview=True)
    # Wait for 1 second
    time.sleep(1)
    # Capture the image
    picam2.capture_file(image_path, format='jpeg')
    # Convert the image to monochrome
    image = Image.open(image_path).convert("L")
    # Save the monochrome image
    image.save(image_path)
    # Perform OCR using Pytesseract
    text = pytesseract.image_to_string(image_path)
    print("Text: ", text)
    # Measure confidence
    confidence = pytesseract.image_to_data(image_path, output_type=pytesseract.Output.DICT)['conf'][0]
    print("Confidence: ", confidence)
    # Close the camera
    picam2.stop()
    
ocr_tts()

def insert_word(supabase, text, user):
    word_object = {
        "created_at": local_time,
        "text": text,
        "favorite": False,
        "user_id": user,
    }
    # Insert the word into Supabase
    response = supabase.table("words").insert(word_object).execute()
    if response["error"]:
        print(response["error"])
    else:
        print("Word inserted successfully!")

# Call the supabase_initilization() method and get the variables
#supabase, session_token, user_id = supabase_initialization()
#insert_word(supabase, session_token, text, user_id)

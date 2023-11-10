from picamera2 import Picamera2, Preview
import pytesseract
import pyttsx3
import cv2
import time
import os
from supabase import create_client, Client
import time
import datetime
import time
from PIL import Image

local_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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

# Check file output path
if not os.path.exists("/home/borat/OUTPUT"):
    os.makedirs("/home/borat/OUTPUT")
image_path = "/home/borat/OUTPUT/img.jpg"

def ocr_tts():
    picam2 = Picamera2()
    camera_config = picam2.create_preview_configuration()
    picam2.configure(camera_config)
    picam2.start_preview(Preview.QTGL)
    picam2.start()
    time.sleep(3)
    picam2.capture_file(image_path)
    # Load image
    img = cv2.imread(image_path)
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply threshold to convert to binary image
    threshold_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    # Pass the image through pytesseract
    text = pytesseract.image_to_string(threshold_img)
    # Print the extracted text
    print("Extracted text: ")
    print(text)
    # Read the text out loud using the Python TTS engine.
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    # Call the supabase_initilization() method and get the variables
    supabase, session_token, user_id = supabase_initialization()
    insert_word(supabase, session_token, text, user_id)

# Call the function
ocr_tts()

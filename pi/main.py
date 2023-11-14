# main.py

from capture import capture_image
from ocr import ocr
from tts import text_to_speech
from db import insert_word

def main():
    image_path = capture_image()
    text = ocr(image_path)
    text_to_speech(text)
    insert_word(text)

if __name__ == "__main__":
    main()
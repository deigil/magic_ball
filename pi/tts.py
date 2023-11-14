import pyttsx3

def text_to_speech(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set the rate of speech (optional)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 70)

    # Set the voice (optional, you can skip this part)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Change the index to choose a different voice

    # Set the language to English (US)
    engine.setProperty('lang', 'en-us')

    # Read the text out loud
    engine.say(text)
    engine.runAndWait()


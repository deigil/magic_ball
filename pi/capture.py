# capture.py

from picamera2 import Picamera2, Preview
import os
import time

def capture_image():
    # image path
    if not os.path.exists("/home/borat/OUTPUT"):
        os.makedirs("/home/borat/OUTPUT")
    image_path = "/home/borat/OUTPUT/img.jpg"

    picam2 = Picamera2()
    prev_config = picam2.create_preview_configuration(main={"size": (800, 600)})
    capt_config = picam2.create_still_configuration()
    picam2.configure(prev_config)
    picam2.start_preview(Preview.QT)
    picam2.start()
    time.sleep(5)
    picam2.switch_mode(capt_config)
    picam2.capture_file(image_path)           
    picam2.stop_preview()
    picam2.stop()

    return image_path


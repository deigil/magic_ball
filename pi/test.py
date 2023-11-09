#!/usr/bin/python3

# Capture a full resolution image to memory rather than to a file.

import time

from picamera2 import Picamera2, Preview
from PIL import Image

picam2 = Picamera2()
picam2.start_preview(Preview.QTGL)
preview_config = picam2.create_preview_configuration()
capture_config = picam2.create_still_configuration()

picam2.configure(preview_config)
picam2.start()
time.sleep(2)

image = picam2.switch_mode_and_capture_image(capture_config)
mono = Image.open(image).convert("L")
mono.show()

time.sleep(1)

picam2.close()
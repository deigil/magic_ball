from picamera2 import Picamera2, Preview
import time

def test():
    picam2 = Picamera2()
    prev_config = picam2.create_preview_configuration(main={"size": (800, 600)})
    picam2.configure(prev_config)
    picam2.start_preview(Preview.QT)
    picam2.start()
    time.sleep(900)
    picam2.stop_preview()
    picam2.stop()



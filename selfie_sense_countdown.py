## selfie.py

from PIL import Image
from picamera import PiCamera
from sense_hat import SenseHat
from time import sleep

im = Image.open("/home/pi/selfie1.jpg")
camera = PiCamera()
sense = SenseHat()

im.show()
sense.show_message("3,2,1")
camera.start_preview(alpha=192)
sleep(3)
camera.capture("/home/pi/image1.jpg")
camera.stop_preview()

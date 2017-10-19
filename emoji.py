from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

r = (255, 0, 0)
w = (255, 255, 255)

smile = [
    w,w,w,r,r,w,w,w,
    w,w,r,w,w,r,w,w,
    w,r,w,w,w,w,r,w,
    r,w,r,w,w,r,w,r,
    r,w,w,w,w,w,w,r,
    w,r,w,r,r,w,r,w,
    w,w,r,w,w,r,w,w,
    w,w,w,r,r,w,w,w,
]

no_smile = [
    w,w,w,r,r,w,w,w,
    w,w,r,w,w,r,w,w,
    w,r,w,w,w,w,r,w,
    r,w,r,w,w,r,w,r,
    r,w,w,w,w,w,w,r,
    w,r,w,w,w,w,r,w,
    w,w,r,w,w,r,w,w,
    w,w,w,r,r,w,w,w,
]


sense.set_pixels(smile)
sleep(1)
sense.set_pixels(no_smile)

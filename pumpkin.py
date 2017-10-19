from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
start_humidity = sense.humidity

o = (255, 165, 0)
r = (255, 0, 0)
w = (255, 255, 255)
g = (0, 128, 0)
b = (0, 0, 0)

light = [
    b,b,b,b,g,b,b,b,
    b,b,o,g,o,o,b,b,
    b,o,o,o,o,o,o,b,
    o,o,r,o,o,r,o,o,
    o,o,o,o,o,o,o,o,
    w,o,o,r,r,o,o,w,
    w,w,o,o,o,o,w,w,
    w,w,w,o,o,w,w,w,
]

nolight = [
    w,w,w,w,g,w,w,w,
    w,w,o,g,o,o,w,w,
    w,o,o,o,o,o,o,w,
    o,o,b,o,o,b,o,o,
    o,o,o,o,o,o,o,o,
    w,o,o,b,b,o,o,w,
    w,w,o,o,o,o,w,w,
    w,w,w,o,o,w,w,w,
]

while True:
    print(sense.humidity)
    if sense.humidity > start_humidity + 10:
        sense.set_pixels(nolight)
    elif sense.humidity > start_humidity + 5:
        sense.set_pixels(nolight)
    else:
        sense.set_pixels(light)
    sleep(1)

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
start_temp = sense.temperature

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
    b,o,o,r,r,o,o,b,
    b,b,o,o,o,o,b,b,
    b,b,o,o,o,o,b,b,
]

nolight = [
    b,b,b,b,g,b,b,b,
    b,b,o,g,o,o,b,b,
    b,o,o,o,o,o,o,b,
    o,o,b,o,o,b,o,o,
    o,o,o,o,o,o,o,o,
    b,o,o,b,b,o,o,b,
    b,b,o,o,o,o,b,b,
    b,b,o,o,o,o,b,b,
]


while True:
    print(sense.temperature)
    if sense.temperature > start_temp + 10:
        sense.set_pixels(nolight)
    elif sense.temperature > start_temp + 5:
        sense.set_pixels(nolight)
    else:
        sense.set_pixels(light)
    sleep(1)

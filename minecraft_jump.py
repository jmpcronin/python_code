import time
import RPi.GPIO as GPIO

from picraft import World
from picraft import Vector

# GPIO04
pin = 4
# Mode BCM eg. GPIO04 = 4
GPIO.setmode(GPIO.BCM)
# Setup GPIO04 as input
GPIO.setup(pin, GPIO.IN)

# Initialise
world = World()
# Say greeting
world.say('ahoj')
# Reset player's position to 0,0,0
world.player.pos = Vector(0,0,0)

# Initialise is button pressed
button_pressed_already = False

# Main loop
while True:
    # Read button
    button_pressed = GPIO.input(pin)
    # When button gets pressed and is not pressed already
    if button_pressed and not button_pressed_already:
        # Say "jump"
        world.say('jump')
        # Read player's position
        pos = world.player.pos
        # Change player's Y position ie. jump up
        world.player.pos += Vector(y=pos.y+10)
    # Was the button pressed?
    button_pressed_already = button_pressed
    # Pause so one push of the button is only one jump
        time.sleep(0.05)

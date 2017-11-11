import time
import RPi.GPIO as GPIO

from mcpi.minecraft import Minecraft
from picraft import World
from picraft import Vector


mc = Minecraft.create()
# GPIO04
pin = 4
# Mode BCM eg. GPIO04 = 4
GPIO.setmode(GPIO.BCM)
# Setup GPIO04 as input
GPIO.setup(pin, GPIO.IN)

# Initialise
world = World()
# Say greeting
world.say('bombs away')


# Initialise is button pressed
button_pressed_already = False

# Main loop
while True:
    # Read button
    button_pressed = GPIO.input(pin)
    # When button gets pressed and is not pressed already
    if button_pressed and not button_pressed_already:
        # Say "boom"
        world.say('Cut the red wire')
        # Read player's position
        x, y, z = mc.player.getPos()
        # Place the block
        mc.setBlocks(x+1, y+1, z+1, x+5, y+5, z+5, 46, 1)
    # Was the button pressed?
    button_pressed_already = button_pressed
    # Pause so one push of the button is only one jump
    time.sleep(0.05)

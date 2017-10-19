from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

sleep(5)

#mc.postToChat("Teleporting")
#mc.player.setPos(11, 11, 100)

stone = 1

sleep(5)

mc.postToChat("Building")

mc.setBlocks(0, 0, 0, 35, 35, 35, stone)

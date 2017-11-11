from mcpi.minecraft import Minecraft

mc = Minecraft.create()

mc.postToChat("Hello world")

x, y, z = mc.player.getPos()

mc.setBlocks(x+1, y+1, z+1, x+5, y+5, z+5, 46, 1)


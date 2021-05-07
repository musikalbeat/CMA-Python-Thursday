from mcpi.minecraft import Minecraft
import random

mc = Minecraft.create("95.156.238.224", 4711)
username = "Monoen"

myId = mc.getPlayerEntityId(username)
myPos = mc.entity.getPos(myId)

x = myPos.x
y = myPos.y - 1
z = myPos.z

# Starting Platform
mc.setBlocks(x-2, y, z-2, x+2, y, z+2, 133)

for i in range(50):
	mc.setBlock(x, y, z, 133)
	x = x + random.randint(1, 3)
	y = y + random.randint(-1, 1)
	z = z + random.randint(-2, 2)

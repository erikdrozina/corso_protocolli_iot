import random

# position of the drone
def GetPosition(id):
    position_x = random.randint(0, 1000)
    position_y = random.randint(0, 1000)
    position_z = random.randint(0, 1000)
    return [position_x, position_y, position_z]

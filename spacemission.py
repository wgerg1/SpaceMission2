WIDTH = 800
HEIGHT = 600
roommap = []
roomheight = 7
roomwidth = 10
roomnumber = 31
OBJECT_LIST = [images.floor, images.pillar, images.soil]
TILE_SIZE = 30
top_left_x = 100
top_left_y = 150

def draw():
    if len(roommap) > 0:
        for i in range(roomheight):
            for j in range(roomwidth):
                tiledata = roommap[i][j]
                screen.blit(OBJECT_LIST[tiledata], (j * TILE_SIZE + top_left_x, i * TILE_SIZE - OBJECT_LIST[tiledata].get_height() + top_left_y))

def generate_room():
    temprow = []
    floor_material =0
    wall_material = 1
    if roomnumber < 26:
        floor_material = 2
        wall_material = 2
    for i in range(roomwidth):
        temprow.append(wall_material)
    roommap.append(temprow)
    for i in range(roomheight - 2):
        temprow = []
        temprow.append(wall_material)
        for j in range(roomwidth - 2):
            temprow.append(floor_material)
        temprow.append(wall_material)
        roommap.append(temprow)
    temprow = []
    for i in range(roomwidth):
        temprow.append(wall_material)
    roommap.append(temprow)
    print(roommap)
generate_room()
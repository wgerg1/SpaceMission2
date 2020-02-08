from objects import *
from gamemap import *
from scenery import *

WIDTH = 800
HEIGHT = 600
roommap = []
roomheight = 7
roomwidth = 10
roomnumber = 45
OBJECT_LIST = objects
TILE_SIZE = 30
top_left_x = 100
top_left_y = 150

def draw():
    if len(roommap) > 0:
        for i in range(roomheight):
            for j in range(roomwidth):
                tiledata = roommap[i][j]
                screen.blit(OBJECT_LIST[tiledata][0], (j * TILE_SIZE + top_left_x, i * TILE_SIZE - OBJECT_LIST[tiledata][0].get_height() + top_left_y))

def generate_room():
    global roommap, roomwidth, roomheight
    roomwidth = GAME_MAP[roomnumber][2]
    roomheight = GAME_MAP[roomnumber][1]
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

    #add in exits
    if GAME_MAP[roomnumber][3]: #data position of top exit
        exitpos = roomwidth // 2 #floor division
        roommap[0][exitpos] = floor_material
        roommap[0][exitpos+1] = floor_material
    if GAME_MAP[roomnumber][4]: #right exit
        exitpos = roomheight // 2
        roommap[exitpos][roomwidth-1] = floor_material
        roommap[exitpos+1][roomwidth-1] = floor_material
        roommap[exitpos+1][roomwidth-1] = floor_material
    #add fence where needed
    #top fence
    if roomnumber < 6:
        temprow = []
        for i in range(roomwidth):
            temprow.append(31)
        roommap[0] = temprow.copy()
    if roomnumber < 26:
        #left fence
        if roomnumber % 5 == 1:
            for row in roommap:
                row[0] = 31
        #right fence
        if roomnumber % 5 == 0:
            for row in roommap:
                row[roomwidth-1] = 31
    #add scenery
    if roomnumber in scenery:
        scenlist = scenery[roomnumber]
        for scenitem in scenlist: #scenitem is a mini list
            roommap[scenitem[1]][scenitem[2]] = scenitem[0]

    print(roommap)
generate_room()
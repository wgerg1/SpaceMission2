from objects import *
from gamemap import *
from scenery import *
from player import *
import time

WIDTH = 800
HEIGHT = 600
roommap = []
roomheight = 7
roomwidth = 10
roomnumber = 31
OBJECT_LIST = objects
TILE_SIZE = 30
top_left_x = 100
top_left_y = 150

#PLAYER VARIABLES
playerX = 5
playerY = 2
playerOffsetX = 0
playerOffsetY = 0
playerDirection = "right"
playerFrame = 0
PlayerOldX = 5
PlayerOldY = 2


###PILLARS###
PILLARS = [images.pillar, images.pillar_95, images.pillar_80, images.pillar_60, images.pillar_50]
pillarFrame = 0
def draw_image(image, x, y):
    screen.blit(image, (top_left_x + x * TILE_SIZE, top_left_y + (y * TILE_SIZE) - image.get_height()))

def draw_shadow(image, x, y):
     screen.blit(image, (top_left_x + x * TILE_SIZE, top_left_y + (y * TILE_SIZE)))

def draw_player():
    p_img = PLAYER[playerDirection][playerFrame]
    draw_image(p_img, playerX + playerOffsetX, playerY +playerOffsetY)
    p_shw_img = PLAYER_SHADOW[playerDirection][playerFrame]
    draw_shadow(p_shw_img, playerX + playerOffsetX, playerY + playerOffsetY)

def draw():
    floor_material = get_floor_material()
    box = Rect((0,150), (WIDTH, HEIGHT))
    screen.draw.filled_rect(box, (0,0,0))
    screen.clear()

    if len(roommap) > 0:
        for i in range(roomheight):
            for j in range(roomwidth):
                draw_image(OBJECT_LIST[floor_material][0], j, i)

                if roomnumber == 26:
                    if i == 8 and j == 2:
                        pp_img = OBJECT_LIST[39][0]
                        draw_image(pp_img, j, i)

            for i in range(roomheight):
                for j in range(roomwidth):
                    tiledata = roommap[i][j]
                    if tiledata not in items_player_may_stand_on + [255]:
                        obj_img = OBJECT_LIST[tiledata][0]
                        draw_image(obj_img, j , i)

                        #front wall transparency
                        if i == roomheight - 1 and roommap[i][j] == 1:
                            obj_images = PILLARS[pillarFrame]


                #add a shadow if needed
                        if OBJECT_LIST[tiledata][1]:
                            shadow_image = (OBJECT_LIST[tiledata][1])
                            if shadow_image in [images.full_shadow, images.half_shadow]:
                                shadow_width = int(obj_img.get_width() / TILE_SIZE)
                                for z in range(shadow_width):
                                    draw_shadow(shadow_image, j + z, i)
                            else:
                                draw_shadow(shadow_image, j, i)
                if playerY == i:
                    draw_player()

def adjust_w_fade():
    global pillarFrame

    #fade out



    #fade in
    if (playerY < roomheight -2 or roommap[roomheight -1[playerX] != 1) and pillarFrame > 0:

def get_floor_material():
    floor_material =0
    if roomnumber < 26:
        floor_material = 2
    return floor_material

def generate_room():
    global roommap, roomwidth, roomheight
    roommap = []
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
    #add building for rooms 21-25
    if roomnumber >= 21 and roomnumber <=25:
        for i in range (roomwidth):
            roommap[roomheight - 1][i] = 1
    #add in exits
    if GAME_MAP[roomnumber][3]: #data position of top exit
        exitpos = roomwidth // 2 #floor division
        roommap[0][exitpos] = floor_material
        roommap[0][exitpos+1] = floor_material
    if roomnumber < 46: #bottom exits don't exist on bottom row
        if GAME_MAP[roomnumber+5][3]: #data position of top exit
            exitpos = roomwidth // 2 #floor division
            roommap[roomheight - 1][exitpos] = floor_material
            roommap[roomheight - 1][exitpos+1] = floor_material
    if GAME_MAP[roomnumber][4]: #right exit
        exitpos = roomheight // 2
        roommap[exitpos][roomwidth-1] = floor_material
        roommap[exitpos+1][roomwidth-1] = floor_material
        roommap[exitpos+1][roomwidth-1] = floor_material
    if roomnumber % 5 != 1:
        if GAME_MAP[roomnumber - 1][4]:
            exitpos = roomheight // 2
            roommap[exitpos][0] = floor_material
            roommap[exitpos+1][0] = floor_material
            roommap[exitpos+1][0] = floor_material
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

            scen_image = OBJECT_LIST[scenitem[0]][0]
            si_width = scen_image.get_width()
            tile_width = int(si_width / TILE_SIZE)

            for tile_num in range(1, tile_width):
                roommap[scenitem[1]][scenitem[2] + tile_num] = 255

    print(roommap)

def game_loop():
    global playerDirection, playerX, playerY, playerOffsetX, playerOffsetY, playerFrame, PlayerOldX, PlayerOldY, roomnumber

    if playerFrame > 0:
        playerFrame += 1
        time.sleep(0.05)
        if playerFrame == 5:
            playerFrame = 0
            playerOffsetX = 0
            playerOffsetY = 0
    if playerFrame == 0:
        PlayerOldX = playerX
        playerOldY = playerY
        if keyboard.right:
            playerDirection = "right"
            playerX +=1
            playerFrame = 1
        if keyboard.left:
            playerDirection = "left"
            playerX -=1
            playerFrame = 1
        if keyboard.down:
            playerDirection = "down"
            playerY +=1
            playerFrame = 1
        if keyboard.up:
            playerDirection = "up"
            playerY -=1
            playerFrame = 1

    if playerY == -1:
        roomnumber -= 5
        generate_room()
        playerY = GAME_MAP[roomnumber][1] - 2
        playerX = GAME_MAP[roomnumber][2]//2
        playerframe =0

    if playerY == GAME_MAP[roomnumber][1]:
        roomnumber += 5
        generate_room()
        playerY = 0
        playerX = GAME_MAP[roomnumber][2]//2
        #RIGHT
    if playerX == GAME_MAP[roomnumber][2]:
        playerframe =0
        roomnumber += 1
        generate_room()
        playerX = 0
        playerY = GAME_MAP[roomnumber][1]//2
        playerframe = -1
        #LEFT
    if playerX == -1:
        roomnumber -= 1
        generate_room()
        playerX = GAME_MAP[roomnumber][2]-2
        playerY = GAME_MAP[roomnumber][1]//2
        playerframe = 0

    if roommap[playerY][playerX] not in items_player_may_stand_on:
        playerX = PlayerOldX
        playerY = PlayerOldY
        playerFrame = 0
    if playerFrame > 0 and playerDirection == "right":
        playerOffsetX = -1 + (0.25 * playerFrame)
    if playerFrame > 0 and playerDirection == "left":
        playerOffsetX = 1 + (-0.25 * playerFrame)
    if playerFrame > 0 and playerDirection == "up":
        playerOffsetY = -1 + (-0.25 * playerFrame)
    if playerFrame > 0 and playerDirection == "down":
        playerOffsetY = -1 + (0.25 * playerFrame)
    #runs multiple times per second
generate_room()
clock.schedule_interval(game_loop, 0.03)
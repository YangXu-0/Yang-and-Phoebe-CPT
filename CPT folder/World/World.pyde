#past = False
keys_pressed = [False for key_code in range(256)]
map_offset = [0, 0]
slide = 0
movement = True
text_list_index = 0
WORLD_BOUNDARIES = [304, -563, -644, 224]

def setup():
    global landscape
    global PLAYER_POS_WORLD
    rectMode(CORNERS)
    
    size(640, 480)
    
    landscape = loadImage("HOSA skeleton diagram.PNG")
    PLAYER_POS_WORLD = [width/2, height/2]
    
    

def draw():
    global slide, movement, map_offset
    
    background(0)
    
    if slide == 0:
        landscape.resize(900, 900)
        image(landscape, map_offset[0], map_offset[1])
        rect(310 + map_offset[0], 59 + map_offset[1], 330 + map_offset[0], 72 + map_offset[1])
        draw_user(PLAYER_POS_WORLD[0], PLAYER_POS_WORLD[1], 13)
        
        if movement:
            map_offset = user_movement(1.5, map_offset, WORLD_BOUNDARIES)
            #print(map_offset)
        
        if map_offset[1] >= 174:
            movement = False
            textbox([11, 324], [629, 468])
    
    
def textbox(corner_one, corner_two):
    global text_list_index, slide
    enemy_text = ["Hi!", "Let's fight"]
    
    fill(0)
    rect(corner_one[0], corner_one[1], corner_two[0], corner_two[1])
    fill(255)
    try:
        text(enemy_text[text_list_index], 15, 396)
    except:
        text_list_index == len(enemy_text)
        slide += 1

"""
def user_movement(speed):
    global map_offset, past 
    #border_x_pos = [0, 900, 0, 900]
    #border_y_pos = [0, 0, 900, 900]
    enemy_location = [240 + map_offset[0], 59 + map_offset[1], 258 + map_offset[0], 72 + map_offset[1]]
    enemy_offset_location = [80, 181, 62, 168]

    
    if keys_pressed[38]:
        map_offset[1] += speed
    if keys_pressed[40]:
        map_offset[1] -= speed
    if keys_pressed[37]:
        map_offset[0] += speed
    if keys_pressed[39]:
        map_offset[0] -= speed
        
    if map_offset[0] >= (314):
        map_offset[0] = (314)
    if map_offset[0] <= (-573):
        map_offset[0] = (-573)
    
    
    draw_user(player_pos[0], player_pos[1], 13)
"""


def user_movement(speed, position, boundary_values):
    if keys_pressed[38]:
        position[1] -= speed
    if keys_pressed[40]:
        position[1] += speed
    if keys_pressed[37]:
        position[0] -= speed
    if keys_pressed[39]:
        position[0] += speed
    
    """  
    if not(position[0] >= (boundary_values[2] + 10)):
        position[0] = (boundary_values[0] + 10)
    if not(position[0] <= (boundary_values[0] - 10)):
        position[0] = (430 - 10)
    if not(player_pos[1] >= (boundary_values[3] + 10)):
        position[1] = (boundary_values[3] + 10)
    if not(position[1] <= (boundary_values[1] - 10)):
        position[1] = (boundary_values[1] - 10)
    """
    return position
    
    
def draw_user(x_pos, y_pos, size):
    fill(255, 0, 0)
    ellipse(x_pos, y_pos, 13, 13)
    
    
def enemy_collision(enemy_coordinates, enemy_offset_coordinates, direction, axis):
    global player_pos
    
    if player_pos[0] > enemy_coordinates[0] and player_pos[0] < enemy_coordinates[2] and player_pos[1] > enemy_coordinates[1] and player_pos[1] < enemy_coordinates[3]:
        map_offset[axis] = enemy_offset_coordinates[direction]
    
    #if player_pos[0] < enemy_coordinates[0] and player_pos[0] > enemy_coordinates[1] and player_pos[1] < enemy_coordinates[2] and player_pos[1] > enemy_coordinates[3]:
     #   map_offset[axis] = enemy_coordinates[direction]
    
    
def keyPressed():
    global keys_pressed
    keys_pressed[keyCode] = True
    

def keyReleased():
    global keys_pressed, text_list_index, slide
    keys_pressed[keyCode] = False
    
    if key == "z":
        if slide == 0 and movement == False:
            text_list_index += 1
        elif slide != 0:
            slide += 1
    
    
def mousePressed():
    print(str(mouseX) + ", " + str(mouseY))

import random

player_pos = []
obstacle_pos = []
obstacle_pos_checker = []
offset = 0
collision_immune = False
IMMUNE_TIME = 3
immune_time_elapsed = 0
health = 20
slide = 0
seconds_elapsed = 0

def setup():
    size(640, 480)
    rectMode(CORNERS)


def draw():
    global health, player_pos, obstacle_pos, slide
    
    background(0)
    if slide == 0:
        battle_screen_display()
        user_movement()
        attack1()
        health -= damage_calc(obstacle_pos, player_pos)
        print(health)
        if len(obstacle_pos) == 0:
            slide += 1
    

def battle_screen_display():    
    # Fight box
    fill(0)
    stroke(255)
    strokeWeight(5)
    rect(width/2 - 110, height/2 - 4, width/2 + 110, height/2 + 139)
    
    # Selection boxes
    stroke("#FF8503")
    rect(12, 417, 157, 467)
    rect(169, 417, 314, 467)
    rect(326, 417, 471, 467)
    rect(483, 417, 628, 467)


def user_movement():
    global player_pos # Ya so this is breaking it
    
    if keyPressed:
        if keyCode == UP:
            player_pos[1] -= 1.5
        elif keyCode == DOWN:
            player_pos[1] += 1.5
        elif keyCode == LEFT:
            player_pos[0] -= 1.5
        elif keyCode == RIGHT:
            player_pos[0] += 1.5
            
    if not(player_pos[0] >= (210 + 10)):
        player_pos[0] = (210 + 10)
    if not(player_pos[0] <= (430 - 10)):
        player_pos[0] = (430 - 10)
    if not(player_pos[1] >= (236 + 10)):
        player_pos[1] = (236 + 10)
    if not(player_pos[1] <= (379 - 10)):
        player_pos[1] = (379 - 10)
            
    draw_user(player_pos[0], player_pos[1])
    

def draw_user(x_pos, y_pos):
    fill(255, 0, 0)
    ellipse(x_pos, y_pos, 10, 10)
    
    
def damage_calc(obstacle_locations, player_location):
    global IMMUNE_TIME, collision_immune, immune_time_elapsed
    
    if collision_immune == True:
        if second() - immune_time_elapsed >= IMMUNE_TIME:
            collision_immune = False
            immune_time_elapsed = 0
    
    for i in range(0, len(obstacle_locations), 4):
        if player_location[0] >= obstacle_locations[i] and player_location[0] <= obstacle_locations[i + 2] and player_location[1] >= obstacle_locations[i + 1] and player_location[1] <= obstacle_locations[i + 3] and collision_immune == False:
            collision_immune = True
            immune_time_elapsed = second()
            return 4
    else:
        return 0
    
    


        

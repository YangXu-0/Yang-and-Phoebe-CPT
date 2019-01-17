import random
import time

player_pos = [320, 308]
obstacle_pos = []
obstacle_pos_checker = []
offset = 0
collision_immune = False
IMMUNE_TIME = 3
immune_time_elapsed = 0
health = 20
slide = 0
seconds_elapsed = 0
ratio = random.random() 

keys_pressed = [False for key_code in range(256)]

def setup():
    size(640, 480)
    rectMode(CORNERS)


def draw():
    global health, player_pos, obstacle_pos, slide
    
    background(0)
    battle_screen_display()
    if slide == 0:
        user_movement()
        patch_attack() # Change this each time
        health -= damage_calc(obstacle_pos, player_pos)
        if len(obstacle_pos) == 0:
            slide += 1
    
    user_movement()

def patch_attack(self):
        global offset, obstacle_pos, ratio
        
        if offset < 220:
            offset += 1

        fill(255)
        stroke(255)
        strokeWeight(5)
        self.obstacle_pos = [width/2  - 110 + offset, (height/2) + 8.3 * ratio, width/2 - 50 + offset, (height/2 + 50) + 8.3 * ratio]
        rect(self.obstacle_pos[0], self.obstacle_pos[1], self.obstacle_pos[2], self.obstacle_pos[3])
        
        if offset >= 153:
            offset = 0
            ratio = random.randint(0, 10) 

def quack_attack(self):
        global offset, obstacle_pos, ratio
        
        if offset < 220:
            offset += 3

        fill(255)
        stroke(255)
        strokeWeight(5)
        self.obstacle_pos = [width/2  - 110 + offset, (height/2) + 10.85 * ratio, width/2 - 80 + offset, (height/2 + 30) + 10.85 * ratio]
        rect(self.obstacle_pos[0], self.obstacle_pos[1], self.obstacle_pos[2], self.obstacle_pos[3])
        
        if offset >= 187:
            offset = 0
            ratio = random.randint(0, 10) 

def desdemona_attack(self):
        global offset, obstacle_pos, ratio
        
        if offset < 220:
            offset += 2.5

        fill(255)
        stroke(255)
        strokeWeight(5)
        self.obstacle_pos = [width/2  - 110 + offset, (height/2) + 8.3 * ratio, width/2 - 50 + offset, (height/2 + 50) + 8.3 * ratio]
        rect(self.obstacle_pos[0], self.obstacle_pos[1], self.obstacle_pos[2], self.obstacle_pos[3])
        
        if offset >= 157:
            offset = 0
            ratio = random.randint(0, 10) 
        
def rosalind_attack(self):
        global offset, obstacle_pos, ratio
        
        if offset < 220:
            offset += 2

        fill(255)
        stroke(255)
        strokeWeight(5)
        self.obstacle_pos = [width/2  - 110 + 15.4 * ratio, (height/2) + offset, width/2 - 50 + 15.4 * ratio , (height/2 + 50) + offset]
        rect(self.obstacle_pos[0], self.obstacle_pos[1], self.obstacle_pos[2], self.obstacle_pos[3])
        
        if offset >= 90:
            offset = 0
            ratio = random.randint(0, 10) 
            
def gallo_attack(self):
        global offset, obstacle_pos, ratio
        
        if offset < 220:
            offset += 2.5

        fill(255)
        stroke(255)
        strokeWeight(5)
        self.obstacle_pos = [width/2  - 110 + 19 * ratio, (height/2) + offset, width/2 - 80 + 19 * ratio , (height/2 + 80) + offset]
        rect(self.obstacle_pos[0], self.obstacle_pos[1], self.obstacle_pos[2], self.obstacle_pos[3])
        
        if offset >= 56:
            offset = 0
            ratio = random.randint(0, 10) 

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
    if keys_pressed[38]:
        player_pos[1] -= 1.5
    if keys_pressed[40]:
        player_pos[1] += 1.5
    if keys_pressed[37]:
        player_pos[0] -= 1.5
    if keys_pressed[39]:
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
    
    
def keyPressed():
    global keys_pressed
    keys_pressed[keyCode] = True
    
    
def keyReleased():
    global keys_pressed
    keys_pressed[keyCode] = False
    

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
    

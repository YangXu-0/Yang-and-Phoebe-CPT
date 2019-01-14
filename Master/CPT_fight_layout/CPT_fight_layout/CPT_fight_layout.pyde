import random
import time

user_option_selection_counter = 0
option_selection = 0
slide = 0
player_pos = [320, 308]
offset = 0 # For some reason it doesn't repeatedly add to this when it's a class variable so gotta fix later
keys_pressed = [False for key_code in range(256)]
enemy_dialogue = []
movement = True
text_list_index = 0
ENEMY_ATTACK_BOUNDARIES = [430, 379, 210, 236]
WORLD_BOUNDARIES = [0, 150, -891, -72]
map_offset = [0, 0]
counter = 0
attack_functions = 0
enemy_attack = None
user_color = "#FF0000"


def setup():
    global user, enemy, landscape, PLAYER_POS_WORLD
    size(640, 480)
    rectMode(CORNERS)
    frameRate(100)

    text_font = loadFont("CharterBT-Bold-48.vlw")
    textFont(text_font)
    
    landscape = loadImage("map.png")
    PLAYER_POS_WORLD = [width/2, height/2]
    
    enemy = Enemy()
    user = User()

    enemy.patch() # Defined at beginning just to get program running


def draw():
    global slide, user_option_selection_counter, option_selection, user, enemy, offset, player_pos, movement, map_offset, counter, keys_pressed, enemy_attack
    
    background(0)
        
    print(map_offset) 
    
    if slide == 2 or slide == 3 or slide == 4 or slide == 5:
        battle_screen_display(user, enemy)
      
    if slide == 0:
        title_screen()
    elif slide == 1:
        landscape.resize(0, 800)
        image(landscape, map_offset[0], map_offset[1])
        draw_user(PLAYER_POS_WORLD[0], PLAYER_POS_WORLD[1], 13, "#FFFF00")
        
        if movement:
            map_offset = user_movement(-1.5, map_offset, WORLD_BOUNDARIES) # Is using a negative speed ok?
        
        if map_offset[0] <= enemy.enemy_attributes[4]:
            movement = False
            textbox([11, 324], [629, 468])
    elif slide == 2:
        enemy_attack = random.choice(attack_functions)  # Needs to be defined at the beginning of turn
        
        user_selection()
        fill(255)
        textSize(20)
        text(enemy_dialogue[2], 60, 320)    
    elif slide == 3:
        fill(255)
        
        if user_option_selection_counter == 0:
            fight()
        elif user_option_selection_counter == 1:
            print_options(0, 4, enemy.act_path)
            user_selection()        
        elif user_option_selection_counter == 2:
            print_options(0, 4, user.items)
            user_selection()
        else:
            # Is using a try except this way good practice?
            try:
                slide = int(user.spare(enemy.enemy_attributes))
            except:
                user.spare(enemy.enemy_attributes)
    elif slide == 4:
        if user_option_selection_counter == 0:
            if enemy.enemy_attributes[1] - user_attack_damage_calc() < 0:
                enemy.enemy_attributes[1] = 0
            else:
                enemy.enemy_attributes[1] -= user_attack_damage_calc()
            if enemy.enemy_attributes[1] <= 0:
                slide = 7
            else:
                offset = 0
                slide += 1
        elif user_option_selection_counter == 1:
            enemy.act(option_selection)
            
        elif user_option_selection_counter == 2:
            user.use_item(option_selection)
            slide += 1
        else:
            slide += 1
    elif slide == 5:
        enemy_attack()
        player_pos = user_movement(1.5, player_pos, ENEMY_ATTACK_BOUNDARIES)
        enemy.end_attack() # Needs to be before damage calculation
        draw_user(player_pos[0], player_pos[1], 13, user_color)
        user.user_attributes[0] -= enemy.damage_calc()
    elif slide == 6:
        fill(255)
        textSize(80)
        text("You Lose.", width/2 - 175, height/2 + 40)
        textSize(10)
        text("how unfortunate :)", width/2+85, height/2+75)
    elif slide == 7:
        fill(255)
        textSize(80)
        text("You Win!", width/2 - 175, height/2 + 40)
        textSize(10)
        text("...we'll get you next time", width/2+50, height/2+75)
    elif slide == 8:
        counter += 1
        if counter == 1:
            enemy.rosalind()
        elif counter == 2:
            enemy.quack()
        elif counter == 3:
            enemy.desdemona()
        elif counter == 4:
            enemy.gallo()
        
        movement = True
        offset = 0
        keys_pressed = [False for key_code in range(256)]
        user.items = ["Burger", "Ice Cream", "Over Priced Cookie", "Cake"]
        user.item_values = [12, 6, 2, 8]
        user.user_attributes[0] = 20
        slide = 1
        

def title_screen():
    fill(255)
    textSize(80)
    text("Blundertale", width/2 - 205, height/2 + 40)
    textSize(20)
    text("Press 'z' to start", width/2 - 70, height/2 + 70)

        
def battle_screen_display(user_info, enemy_info):   
    if slide == 5:
        # Fight box
        fill(0)
        stroke(255)
        strokeWeight(5)
        rect(width/2 - 110, height/2 - 4, width/2 + 110, height/2 + 139)
    else:
        # Textbox
        fill(0)
        stroke(255)
        strokeWeight(5)
        rect(width/2 - 308, height/2 - 4, width/2 + 308, height/2 + 139)
    
    # Selection boxes
    stroke("#FF8503")
    rect(width/2 - 308, height/2 + 177, width/2 - 163, height/2 + 227)
    rect(width/2 - 151, height/2 + 177, width/2 - 6, height/2 + 227)  
    rect(width/2 + 6, height/2 + 177, width/2 + 151, height/2 + 227)
    rect(width/2 + 163, height/2 + 177, width/2 + 308, height/2 + 227)
    
    # Selection text
    fill("#FF8503")
    textSize(30)
    text("Fight", width/2 - 260, height/2 + 190, width/2 - 163, height/2 + 235)
    text("Act", width/2 - 103, height/2 + 190, width/2 - 6, height/2 + 235)
    text("Items", width/2 + 54, height/2 + 190, width/2 + 151, height/2 + 235)
    text("Spare", width/2 + 211, height/2 + 190, width/2 + 308, height/2 + 235)
    
    # Health fractions
    fill(255)
    textSize(16)
    text("Player Health {}/{}".format(user_info.user_attributes[0], user_info.user_attributes[1]), width/2 - 308, height/2 + 165)
    text("Enemy Health {}/{}".format(enemy_info.enemy_attributes[1], enemy_info.enemy_attributes[2]), width/2 - 120, height/2 + 165)
    
    
def textbox(corner_one, corner_two):
    global text_list_index, slide
        
    fill(0)
    rect(corner_one[0], corner_one[1], corner_two[0], corner_two[1])
    fill(255)
    if enemy_dialogue[text_list_index] != "":
        text(enemy_dialogue[text_list_index], 15, 396)
    else:
        text_list_index = 0
        slide += 1
    
    
def user_selection():
    global user_option_selection_counter, option_selection
    selection_pos = []
        
    if slide == 2:
        selection_pos = [37 + (157 * user_option_selection_counter), 442]
    elif slide == 3:
        selection_pos = [56 + (151 * option_selection), 320]

    # Player
    draw_user(selection_pos[0], selection_pos[1], 13, user_color)


def fight():
    global offset, slide
    
    # Box
    fill(0)  
    stroke(255)
    strokeWeight(5)
    rect(width/2 - 250, height/2 + 15, width/2 + 250, height/2 + 120)
    
    # Red line
    stroke(255, 59, 59)
    rect(width/2, height/2 + 15, width/2, height/2 + 120)
    
    stroke(255)
    strokeWeight(10)
    rect((width/2 - 246) + offset, height/2 + 15, (width/2 - 245) + offset, height/2 + 120)
    
    if offset >= 490:
        offset = 0
        slide += 1

    offset += 2
    
    
def user_attack_damage_calc():
    global offset
    # Need to abstract midpoint and endpoints somehow
    damage = int(24.5 - (abs(245 - offset) / 10))

    return damage
    

def user_movement(speed, position, boundary_values):
    if keys_pressed[38]:
        position[1] -= speed
    if keys_pressed[40]:
        position[1] += speed
    if keys_pressed[37]:
        position[0] -= speed
    if keys_pressed[39]:
        position[0] += speed
    
    if not(position[0] >= (boundary_values[2] + 10)):
        position[0] = (boundary_values[2] + 10)
    if not(position[0] <= (boundary_values[0] - 10)):
        position[0] = (boundary_values[0] - 10)
    if not(position[1] >= (boundary_values[3] + 10)):
        position[1] = (boundary_values[3] + 10)
    if not(position[1] <= (boundary_values[1] - 10)):
        position[1] = (boundary_values[1] - 10)
    
    return position
    
    
def draw_user(x_pos, y_pos, length, color):
    if slide == 1:
        fill(color)
        ellipse(x_pos, y_pos, length, length)
    else:
        fill(color)
        noStroke()
        ellipse(x_pos, y_pos, length, length)
    

def print_options(min_range, max_range, options_list):
    slice_list = options_list[min_range: max_range]
    
    for option in range(0, len(slice_list)):
        text(slice_list[option], 60 + (option * 151), 320)


def keyPressed():
    global keys_pressed
    
    if slide == 5 or slide == 1:
        keys_pressed[keyCode] = True


def keyReleased():
    global user_option_selection_counter, slide, option_selection, keys_pressed, text_list_index
    
    if key == "z":
        if slide == 1 and movement == False:
            text_list_index += 1
        elif slide in [0, 2, 3, 4, 7]:
            time.sleep(0.15)
            slide += 1
            print(slide)
    
    if key == "x" and slide in [3] and user_option_selection_counter not in [0, 3]:
        slide -= 1
        print(slide)
    
    if slide == 2:
        # Changes option selection counter
        if keyCode == RIGHT and user_option_selection_counter < 3:
            user_option_selection_counter += 1
        elif keyCode == LEFT and user_option_selection_counter > 0:
            user_option_selection_counter -= 1
    if slide == 3:
        # Changes option selection counter
        if keyCode == RIGHT:
            if user_option_selection_counter == 2 and option_selection < len(user.items) - 1:
                option_selection += 1
            elif user_option_selection_counter == 1 and option_selection < 3:
                option_selection += 1
        elif keyCode == LEFT and option_selection > 0:
            option_selection -= 1
            
    if slide == 5 or slide == 1:
        keys_pressed[keyCode] = False


def mousePressed():
    print(str(mouseX) + ", " + str(mouseY))
    
    
class Enemy:
    enemy_attributes = []
    act_path = []
    obstacle_pos = []
    collision_immune = False
    immune_time_elapsed = 0
    IMMUNE_TIME = 70 # Frames

    def patch(self):
        global enemy_dialogue, attack_functions
        enemy_dialogue = ["Patch blocks the way!", "", "You will be judged for your every action...", "Patch is annoyed", "Patch is taken aback, surprised.", "Patch smiles at you", "Patch laughs and his arrogant vibe dissolves into a friendly aura."]
        self.enemy_attributes = ["Patch", 1, 50, False, -88]
        self.act_path = ["Taunt", "Compliment", "Critcize", "Encourage", "131", ""]
        attack_functions = [enemy.patch_attack1, enemy.patch_attack2, enemy.patch_attack3]
        
        
    def rosalind(self):
        global enemy_dialogue
        enemy_dialogue = ["Rosalind stumbles in the way.", "", "Rosalind apologizes.", "Rosalind cries pitifully", "Rosalind cries out, beggin for your sympathy", "Rosalind sniffs and wipes away her tears.", "Rosaline finally cracks a smile, she no longer wants to fight."]
        self.enemy_attributes = ["Rosalind", 30, 40, False, -360]  # Still need to change stats and location
        self.act_path = ["Threaten", "Play", "Smile", "Hug", "231", ""]
        attack_functions = [enemy.patch_attack1, enemy.patch_attack2, enemy.patch_attack3]
        
        
    def quack(self):
        global enemy_dialogue
        enemy_dialogue = ["Quack blocks the way!", "", "Quack brings a friend", "Woodward growls at you", "Quack watches you pet his little friend", "Both Quack and Woordward find you very amusing", "Quack and Woodward no longer want to fight."]
        self.enemy_attributes = ["Quack", 30, 40, False, -582]
        self.act_path = ["Taunt", "Ignore", "Joke", "Pet", "1323", ""]
        attack_functions = [enemy.patch_attack1, enemy.patch_attack2, enemy.patch_attack3]

        
    def desdemona(self):
        global enemy_dialogue
        enemy_dialogue = ["Desdemona blocks the way!", "", "Desmonda files her nails", "You are ignored", "She glares at you, the insult hits a sore spot", "Desdemona's confidence goes down", "Desdemona is getting scared", "Desdemona cowers in fright."]
        self.enemy_attributes = ["Desdemona", 30, 40, False, -759]
        self.act_path = ["Threaten", "Cheer", "Insult", "Scare", "2023", ""]
        attack_functions = [enemy.patch_attack1, enemy.patch_attack2, enemy.patch_attack3]
 
 
    def gallo(self):
        global enemy_dialogue
        enemy_dialogue = ["Gallo blocks the way!", "", "Gallo takes your phone", "Gallo transcends this realm of mortals. Your actions are meaningless."]
        self.enemy_attributes = ["Gallo", 300, 300, False, -881]
        self.act_path = ["Plead", "Reason", "Talk", "Compliment", "0", ""]
        attack_functions = [enemy.patch_attack1, enemy.patch_attack2, enemy.patch_attack3]
                                                               
    
    def act(self, act_index):
        index = 0
        number_correct_choices = 0

        if self.act_path[5] == "":
            self.act_path[5] = str(act_index)
        else:
            self.act_path[5] += str(act_index)
            
        for i in range(0, len(self.act_path[4])):
            if self.act_path[5][index + 1: ].count(self.act_path[4][i]) > 0:
                index = self.act_path[5][index: ].find(self.act_path[4][i])
                number_correct_choices += 1
            else:
                text(enemy_dialogue[number_correct_choices + 3], 60, 320)
                break
        else:
            print(len(enemy_dialogue))
            text("{}".format(enemy_dialogue[len(enemy_dialogue) - 1]), 60, 320)
            self.enemy_attributes[3] = True
    
    
    def damage_calc(self):
        global player_pos, keys_pressed, user_color
        
        if self.collision_immune == True:
            if frameCount - self.immune_time_elapsed >= self.IMMUNE_TIME:
                user_color = "#FF0000"
                self.collision_immune = False
                self.immune_time_elapsed = 0
        
        for i in range(0, len(self.obstacle_pos), 4):
            if player_pos[0] >= self.obstacle_pos[i] and player_pos[0] <= self.obstacle_pos[i + 2] and player_pos[1] >= self.obstacle_pos[i + 1] and player_pos[1] <= self.obstacle_pos[i + 3] and self.collision_immune == False:
                user_color = "#A52323"
                self.collision_immune = True
                self.immune_time_elapsed = frameCount
                return 4
        else:
            return 0
    
            
    def patch_attack1(self):
        global offset, enemy
        
        if offset < 220:
            offset += 0.5
            
        self.obstacle_pos = [width/2  - 107, height/2 + 67.5, width/2 - 110 + offset, height/2 + 137]
        
        fill(0, 0, 255)
        noStroke()
        rect(self.obstacle_pos[0], self.obstacle_pos[1], self.obstacle_pos[2], self.obstacle_pos[3])
        
        
    def patch_attack2(self):
        global offset, enemy
        
        if offset < 220:
            offset += 2
            
        self.obstacle_pos = [width/2  - 107, height/2 + 67.5, width/2 - 110 + offset, height/2 + 137]
        
        fill(255, 0, 0)
        noStroke()
        rect(self.obstacle_pos[0], self.obstacle_pos[1], self.obstacle_pos[2], self.obstacle_pos[3])
        
        
    def patch_attack3(self):
        global offset, enemy
        
        if offset < 220:
            offset += 2
            
        self.obstacle_pos = [width/2  - 107, height/2 + 67.5, width/2 - 110 + offset, height/2 + 137]
        
        fill(0, 255, 0)
        noStroke()
        rect(self.obstacle_pos[0], self.obstacle_pos[1], self.obstacle_pos[2], self.obstacle_pos[3])
        
            
    def end_attack(self):
        global offset, user, keys_pressed, player_pos, slide, user_color
        if offset >= 220:
            self.obstacle_pos = []  # Consider moving player pos reset to damage function
            offset = 0
            keys_pressed = [False for key_code in range(256)]
            player_pos = [320, 308]
            user_color = "#FF0000"
            time.sleep(0.25)
            slide = 2
        elif user.user_attributes[0] <= 0:
            time.sleep(0.2)
            slide = 6
        

class User:
    user_attributes = [400, 20]
    items = ["Burger", "Ice Cream", "Noodles", "Cake"]
    item_values = [12, 6, 2, 8]  # Do I need to use dictionaries?
    
    def use_item(self, item_index):
        value = self.item_values[item_index]
        self.item_values.pop(item_index)
        self.items.pop(item_index)
    
        self.user_attributes[0] += value
        
        if self.user_attributes[0] > self.user_attributes[1]:
            self.user_attributes[0] = self.user_attributes[1]
            
    
    def spare(self, enemy_attributes):
        if enemy_attributes[3] == True:
            return 7
        else:
            text("You tried to spare the enemy but it missed", 60, 320)

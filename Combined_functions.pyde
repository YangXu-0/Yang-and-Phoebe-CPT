import random
import time

user_option_selection_counter = 0
option_selection = 0
slide = 0
player_pos = [320, 308] # Might need to change later cause "doesn't make sense"
offset = 0 # For some reason it doesn't repeatedly add to this when it's a class variable so gotta fix later

enemy = Enemy()
user = User()

enemy.patch()

def setup():
    size(640, 480)
    rectMode(CORNERS)
    text_font = loadFont("CharterBT-Bold-48.vlw")
    textFont(text_font)


def draw():
    global slide, user_option_selection_counter, option_selection
    
    background(0)
        
    if slide == 1 or slide == 2 or slide == 3 or slide == 4:
        battle_screen_display(user, enemy)
      
    if slide == 0:
        title_screen()      
    elif slide == 1:
        user_selection()
        fill(255)
        textSize(20)
        text("Enemy dialogue", 60, 320)    
    elif slide == 2:
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
    elif slide == 3:
        if user_option_selection_counter == 0:
            enemy.enemy_attributes[2] -= user_attack_damage_calc()
            print(user_attack_damage_calc())
            print(enemy.enemy_attributes[2])
        elif user_option_selection_counter == 1:
            enemy.act(option_selection)
            print(enemy.act_path[option_selection + 6])
            slide += 1
        elif user_option_selection_counter == 2:
            user.use_item(option_selection)
            slide += 1
    elif slide == 4:
        user_movement()
        enemy.patch_attack1()
        user.user_attributes[0] -= enemy.damage_calc()
        if user.user_attributes <= 0:
            slide == 6
    elif slide == 5:
        text("You win. Normally, the win screen would go here", 60, 320)
        

def title_screen():
    fill(255)
    textSize(80)
    text("Blundertale", width/2 - 205, height/2 + 40)
    textSize(20)
    text("Press 'z' to start", width/2 - 70, height/2 + 70)

        
def battle_screen_display(user_info, enemy_info):   
    if slide == 4:
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
        rect(12, 236, 628, 379)
    
    # Selection boxes
    stroke("#FF8503")
    rect(12, 417, 157, 467)
    rect(169, 417, 314, 467)
    rect(326, 417, 471, 467)
    rect(483, 417, 628, 467)
    
    # Health fractions
    fill(255)
    textSize(16)
    text("Player Health {}/{}".format(user_info.user_attributes[0], user_info.user_attributes[1]), 12, 405)
    text("Enemy Health {}/{}".format(enemy_info.enemy_attributes[2], enemy_info.enemy_attributes[3]), 150, 405)
    
    
def user_selection():
    global user_option_selection_counter, option_selection
    player_pos = [32, 442]
        
    if slide == 1:
        # Player location changer (Could refactor)
        if user_option_selection_counter == 0:
            player_pos = [32, 442]
        elif user_option_selection_counter == 1:
            player_pos = [189, 442]
        elif user_option_selection_counter == 2:
            player_pos = [346, 442]
        else:
            player_pos = [503, 442]
    elif slide == 2:
        # Player location changer (Could refactor)
        if option_selection == 0:
            player_pos = [56, 320]
        elif option_selection == 1:
            player_pos = [207, 320]
        elif option_selection == 2:
            player_pos = [358, 320]
        else:
            player_pos = [509, 320]
        
    # Player
    draw_user(player_pos[0], player_pos[1])


def fight():
    global offset, slide
    
    # Box
    fill(0)
    stroke(255)
    strokeWeight(5)
    rect(70, 276, 570, 360)
    
    # Red line
    stroke(255, 59, 59)
    rect(320, 276, 320, 360)
    
    stroke(255)
    strokeWeight(10)
    rect(70 + offset, 276, 73 + offset, 360)
    
    if offset >= 490:
        slide += 1

    offset += 2
    
    
def user_attack_damage_calc():
    global offset
    # Need to abstract midpoint and endpoints somehow
    damage = int(24.5 - (abs(245 - offset) / 10))

    return damage
    

def user_movement():
    global player_pos 
    
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
    

def print_options(min_range, max_range, options_list):
    slice_list = options_list[min_range: max_range]
    
    for option in range(0, len(slice_list)):
        text(slice_list[option], 60 + (option * 151), 320)


def keyReleased():
    global user_option_selection_counter, slide, option_selection
    
    if key == "z":
        slide += 1
        print(slide)
    
    if key == "x":
        slide -= 1
        print(slide)
    
    if slide == 1:
        # Changes option selection counter
        if keyCode == RIGHT and user_option_selection_counter < 3:
            user_option_selection_counter += 1
        elif keyCode == LEFT and user_option_selection_counter > 0:
            user_option_selection_counter -= 1
    if slide == 2:
        # Changes option selection counter
        if keyCode == RIGHT and option_selection < 3:
            option_selection += 1
        elif keyCode == LEFT and option_selection > 0:
            option_selection -= 1


def mousePressed():
    print(str(mouseX) + ", " + str(mouseY))
    
    
# Should put in seperate tab?
# Why does it force me to make an argument?
class Enemy:
    enemy_attributes = []
    act_path = []
    obstacle_pos = []
    collision_immune = False
    immune_time_elapsed = 0
    IMMUNE_TIME = 3

    def patch(self):
        self.enemy_attributes = ["Patch", "Hi I'm Patch", 20, 50, False]
        self.act_path = ["Spray", "Heat", "Cut", "Sew", "0123", "", "u did 1", "u did 2", "u did 3", "u did 4"]
        
    
    def act(self, act_index):
        index = 0

        if self.act_path[5] == "":
            self.act_path[5] = str(act_index)
        else:
            self.act_path[5] += str(act_index)
            
        for i in range(len(self.act_path[4])):
            if self.act_path[5][index: ].find(self.act_path[4][i]) > 0:
                index = self.act_path[5][index: ].find(self.act_path[4][i])
            else:
                break
        else:
            self.act_path[4] = True
    
    
    def damage_calc(self):
        global player_pos
        
        if self.collision_immune == True:
            if second() - self.immune_time_elapsed >= self.IMMUNE_TIME:
                self.collision_immune = False
                self.immune_time_elapsed = 0
        
        for i in range(0, len(self.obstacle_pos), 4):
            if player_pos[0] >= self.obstacle_pos[i] and player_pos[0] <= self.obstacle_pos[i + 2] and player_pos[1] >= self.obstacle_pos[i + 1] and player_pos[1] <= self.obstacle_pos[i + 3] and self.collision_immune == False:
                self.collision_immune = True
                self.immune_time_elapsed = second()
                return 4
        else:
            return 0
    
            
    def patch_attack1(self):
        global slide, offset
        
        if offset < 220:
            offset += 2
            
        self.obstacle_pos = [width/2  - 110, height/2 + 67.5, width/2 - 110 + offset, height/2 + 139]
        
        rect(self.obstacle_pos[0], self.obstacle_pos[1], self.obstacle_pos[2], self.obstacle_pos[3])
        
        if offset >= 220:
            time.sleep(1)
            slide += 1

class User:
    user_attributes = [0, 20]
    items = ["Food", "Food", "Food", "Food", 10, 4, 6, 2]
    
    def use_item(self, item_index):
        value = self.items[item_index + 4]
        self.items.pop(item_index + 4)
        self.items.pop(item_index)
    
        self.user_attributes[0] += value
        
        if self.user_attributes[0] > self.user_attributes[1]:
            self.user_attributes[0] = self.user_attributes[1]
            
    
    def spare(self, enemy_attributes):
        if enemy_attributes[4] == True:
            return 5
        else:
            text("You tried to spare the enemy but it missed", 60, 320)

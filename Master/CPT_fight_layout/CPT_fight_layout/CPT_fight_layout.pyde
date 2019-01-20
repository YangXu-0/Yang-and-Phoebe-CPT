import random
import time

user_option_selection_counter = 0
option_selection = 0
slide = 0
player_pos = [320, 308]
offset = 0
keys_pressed = [False for key_code in range(256)]
enemy_dialogue = []
movement = True
text_list_index = 0 # Maybe fix
ENEMY_ATTACK_BOUNDARIES = [430, 379, 210, 236]
WORLD_BOUNDARIES = [0, 150, -891, -72]
map_offset = [-10, 0]
counter = 0
attack_functions = 0
enemy_attack = None
user_color = "#FF0000"
USER_HEALTH = [400, 20]
items = ["Burger", "Ice Cream", "Noodles", "Cake"]
item_values = [12, 6, 2, 8]
ENEMY_DAMAGE = 4


def setup():
    global user, enemy, landscape, PLAYER_POS_WORLD, user_items, heart, keys_pressed
    size(640, 480)
    rectMode(CORNERS)
    frameRate(100)

    heart = loadImage("heart.png")
    landscape = loadImage("map.png")

    PLAYER_POS_WORLD = [width/2, height/2]

    enemy = Enemy()
    user_items = Item(items, item_values)
    user = User(USER_HEALTH)
    tests = Tests()

    print(movement_boundaries([100, 200], [430, 379, 210, 236], 10))

    tests.test_user_attack_damage_calc()
    tests.test_user_movement()
    tests.test_movement_boundaries()
    tests.test_enemy_patch()

    enemy.patch()  # Defined at beginning just to get program running
    
    keys_pressed = [False for key_code in range(256)]  # Reseting because tests change variables


def draw():
    global slide, user_option_selection_counter, option_selection, user, enemy
    global offset, player_pos, movement, map_offset
    global counter, keys_pressed, enemy_attack, user_health, user_items
    background(0)

    if slide == 2 or slide == 3 or slide == 4 or slide == 5:
        battle_screen_display(user.user_health, enemy.enemy_attributes[1:3])

    if slide == 0:
        title_screen()

    elif slide == 1:
        landscape.resize(0, 800)
        image(landscape, map_offset[0], map_offset[1])
        draw_world_user(PLAYER_POS_WORLD[0], PLAYER_POS_WORLD[1], 13)
        if movement:
            map_offset = user_movement(-1.5, map_offset, [38, 40, 37, 39], keys_pressed)
            map_offset = movement_boundaries(map_offset, WORLD_BOUNDARIES, 10)

        if map_offset[0] <= enemy.enemy_attributes[4]:
            movement = False
            draw_textbox([11, 324], [629, 468])
            if text_list_index <= 0:
                fill(255)
                text(enemy_dialogue[text_list_index], 25, 405)
            else:
                slide += 1

    elif slide == 2:
        draw_textbox([width/2 - 308, height/2 - 4], [width/2 + 308, height/2 + 139])
        
        # Needs to be defined at the beginning of turn
        enemy_attack = random.choice(attack_functions)

        user_choice_pos = [37 + (157 * user_option_selection_counter), 442]
        draw_user(user_choice_pos[0], user_choice_pos[1])
        fill(255)
        textSize(20)
        text(enemy_dialogue[1], 60, 320)

    elif slide == 3:
        draw_textbox([width/2 - 308, height/2 - 4], [width/2 + 308, height/2 + 139])
        
        fill(255)

        if user_option_selection_counter == 0:
            fight()
        elif user_option_selection_counter == 1:
            print_options(0, 4, enemy.act_path)
            user_choice_pos = [56 + (151 * option_selection), 320]  #problem
            draw_user(user_choice_pos[0], user_choice_pos[1])
        elif user_option_selection_counter == 2:
            print_options(0, 4, user_items.items)
            
            if option_selection > len(user_items.items) - 1:
                option_selection = len(user_items.items) - 1
            
            user_choice_pos = [56 + (151 * option_selection), 320]
            draw_user(user_choice_pos[0], user_choice_pos[1])
        else:   
            if enemy.enemy_attributes[3]:
                time.sleep(0.15)
                slide = 7
            else:
                text("You tried to spare the enemy but it missed", 60, 320)

    elif slide == 4:
        draw_textbox([width/2 - 308, height/2 - 4], [width/2 + 308, height/2 + 139])

        if user_option_selection_counter == 0:
            if enemy.enemy_attributes[1] - user_attack_damage_calc(24.5, 245, offset) < 0:
                enemy.enemy_attributes[1] = 0
            else:
                enemy.enemy_attributes[1] -= user_attack_damage_calc(24.5, 245, offset)
            if enemy.enemy_attributes[1] <= 0:
                time.sleep(1)
                slide = 7
            else:
                offset = 0
                slide += 1
        elif user_option_selection_counter == 1:
            text_index = enemy.act(option_selection)
            
            if text_index == len(enemy_dialogue) - 1:
                text("{}".format(enemy_dialogue[text_index]), 60, 320)
                enemy.enemy_attributes[3] = True
            else:
                text(enemy_dialogue[text_index + 2], 60, 320)

        elif user_option_selection_counter == 2:
            user.use_item(option_selection, user_items.items, user_items.item_values)
            slide += 1
        else:
            slide += 1

    elif slide == 5:
        draw_fight_box([width/2 - 110, height/2 - 4], [width/2 + 110, height/2 + 139])

        enemy_attack()
        if user.user_health[0] <= 0:
            time.sleep(0.15)
            slide = 6
        
        player_pos = user_movement(1.5, player_pos, [38, 40, 37, 39], keys_pressed)
        player_pos = movement_boundaries(player_pos, ENEMY_ATTACK_BOUNDARIES, 10)
        draw_user(player_pos[0], player_pos[1])
        
        if enemy.collision_immune == True:
            tint(165, 35, 35)
        else:
            noTint()
        
        if enemy.collision_detection(player_pos):
            enemy.collision_immune = True
            enemy.immune_time_elapsed = frameCount
            user.user_health[0] -= ENEMY_DAMAGE
        
        enemy.immunity()
        
        if offset >= 220:  #This needs to be changed to work for all attacks
            enemy.reset()
            slide = 2

    elif slide == 6:
        lose_screen()

    elif slide == 7:
        if counter == 4:
            final_win_screen()
        else:
            movement = True
            win_screen()

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

        offset = 0
        keys_pressed = [False for key_code in range(256)]
        user.user_health[0] = user.user_health[1]
        slide = 1


def title_screen():
    fill(255)
    textSize(80)
    text("Blundertale", width/2 - 205, height/2 + 40)
    textSize(20)
    text("Press 'z' to start", width/2 - 70, height/2 + 70)


def battle_screen_display(user_health, enemy_health):
    # Selection boxes
    stroke("#FF8503")
    fill(0)
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

    try:
        text("Player Health {}/{}".format(user_health[0], user_health[1]), width/2 - 308, height/2 + 165)
    except:
        raise Exception("User's health should contain 2 integers in a list. The list contained '{}'".format(user_health))

    try:
        text("Enemy Health {}/{}".format(enemy_health[0], enemy_health[1]), width/2 - 120, height/2 + 165)
    except:
        raise Exception("Enemy's health should contain 2 integers in a list. The list contained '{}'".format(enemy_health))


def draw_fight_box(corner1, corner2):
    fill(0)
    stroke(255)
    strokeWeight(5)
    try:
        rect(corner1[0], corner1[1], corner2[0], corner2[1])
    except:
        raise Exception("corner1 and corner2 should be lists, each containing a set of coordinates (ints or floats). corner1 contained '{}'. corner2 contained '{}'.".format(corner1, corner2))


def draw_textbox(corner1, corner2):
    fill(0)
    stroke(255)
    strokeWeight(5)
    try:
        rect(corner1[0], corner1[1], corner2[0], corner2[1])
    except:
        raise Exception("corner1 and corner2 should be lists, each containing a set of coordinates (ints or floats). corner1 contained '{}'. corner2 contained '{}'.".format(corner1, corner2))


def win_screen():
    fill(255)
    textSize(80)
    text("You Win!", width/2 - 175, height/2 + 40)
    textSize(10)
    text("...we'll get you next time", width/2 + 50, height/2 + 75)


def final_win_screen():
    dialogue = ["You won.", "You've finally escaped.", "The Gallo has been defeated."]
    draw_textbox([11, 324], [629, 468])
    if text_list_index <= 2:
        fill(255)
        text(dialogue[text_list_index], 25, 405)
    else:
        exit()


def lose_screen():
    fill(255)
    textSize(80)
    text("You Lose.", width/2 - 175, height/2 + 40)
    textSize(10)
    text("how unfortunate :)", width/2+85, height/2+75)


def fight():  #problem
    global offset, slide

    # Box
    fill(0)
    stroke(255)
    strokeWeight(5)
    rect(width/2 - 250, height/2 + 15, width/2 + 250, height/2 + 120)

    # Red line
    stroke(255, 59, 59)
    rect(width/2, height/2 + 15, width/2, height/2 + 120)

    # Moving white bar
    stroke(255)
    strokeWeight(10)
    rect((width/2 - 246) + offset, height/2 + 15, (width/2 - 245) + offset, height/2 + 120)

    if offset >= 490:
        offset = 0
        slide += 1

    offset += 2


def user_attack_damage_calc(start, end, hit_location):
    try:
        damage = int(abs(start - (abs(end - hit_location) / 10)))
    except:
        raise Exception("All three arguments should be ints or floats and the start argument can't be 0.")
        
    return damage


def user_movement(speed, position, keys_used, keys_pressed):  #problem
    if keys_pressed[keys_used[0]]:
        position[1] -= speed
    if keys_pressed[keys_used[1]]:
        position[1] += speed
    if keys_pressed[keys_used[2]]:
        position[0] -= speed
    if keys_pressed[keys_used[3]]:
        position[0] += speed

    return position


def movement_boundaries(position, boundary_values, radius):  #problem
    if not(position[0] >= (boundary_values[2] + radius)):
        position[0] = (boundary_values[2] + radius)
    if not(position[0] <= (boundary_values[0] - radius)):
        position[0] = (boundary_values[0] - radius)
    if not(position[1] >= (boundary_values[3] + radius)):
        position[1] = (boundary_values[3] + radius)
    if not(position[1] <= (boundary_values[1] - radius)):
        position[1] = (boundary_values[1] - radius)
    
    return position


def draw_user(x_pos, y_pos):
    heart.resize(0, 15)
    
    try:
        image(heart, x_pos, y_pos)
    except:
        raise Exception("x_pos and y_pos should be ints or floats. Respectively, they were '{}' and '{}'.".format(x_pos, y_pos))
    

def draw_world_user(x_pos, y_pos, length):
    if keyCode == RIGHT:
        color = "#333FB4"
    elif keyCode == LEFT:
        color = "#07F509"
    elif keyCode == UP:
        color = "#F5072B"
    else:
        color = "#F5E907"

    fill(color)
    ellipse(x_pos, y_pos, length, length)


def print_options(min_range, max_range, options_list):
    try:
        slice_list = options_list[min_range: max_range]
    except:
        raise Exception("min_range, max_range should be ints within the length of options_list (needs to be a list).")

    for option in range(0, len(slice_list)):
        text(slice_list[option], 60 + (option * 151), 320)


def keyPressed():
    global keys_pressed

    if slide == 5 or slide == 1:
        keys_pressed[keyCode] = True


def keyReleased():  #problem
    global user_option_selection_counter, slide, option_selection, keys_pressed, text_list_index

    if key == "z":
        if slide in [1, 7] and movement is False:
            text_list_index += 1
            
        elif slide in [0, 2, 3, 4, 7]:
            time.sleep(0.15)
            slide += 1
    elif key == "x" and slide in [3] and user_option_selection_counter not in [0, 3]:
        slide -= 1


    if slide == 2:
        # Changes option selection counter
        if keyCode == RIGHT and user_option_selection_counter < 3:
            user_option_selection_counter += 1
        elif keyCode == LEFT and user_option_selection_counter > 0:
            user_option_selection_counter -= 1
    elif slide == 3:
        # Changes option selection counter
        if keyCode == RIGHT:
            if user_option_selection_counter == 2 and option_selection < len(user_items.items) - 1:
                option_selection += 1
            elif user_option_selection_counter == 1 and option_selection < 3:
                option_selection += 1
        elif keyCode == LEFT and option_selection > 0:
            option_selection -= 1

    keys_pressed[keyCode] = False


def mousePressed():
    print(str(mouseX) + ", " + str(mouseY))


class Enemy:
    enemy_attributes = []
    act_path = []
    obstacle_pos = []
    collision_immune = False
    immune_time_elapsed = 0
    IMMUNE_TIME = 70  # Frames

    def patch(self):
        global enemy_dialogue, attack_functions
        enemy_dialogue = ["Patch blocks the way!", "You will be judged for your every action...", "Patch is annoyed", "Patch is taken aback, surprised.", "Patch smiles at you", "Patch laughs and his arrogant vibe dissolves into a friendly aura."]
        self.enemy_attributes = ["Patch", 1, 50, False, -88]
        self.act_path = ["Taunt", "Compliment", "Critcize", "Encourage", "131", ""]
        attack_functions = [enemy.patch_attack1, enemy.patch_attack1]

    def rosalind(self):
        global enemy_dialogue
        enemy_dialogue = ["Rosalind stumbles in the way.", "Rosalind apologizes.", "Rosalind cries pitifully", "Rosalind cries out, beggin for your sympathy", "Rosalind sniffs and wipes away her tears.", "Rosaline finally cracks a smile, she no longer wants to fight."]
        self.enemy_attributes = ["Rosalind", 30, 40, False, -360]  # Still need to change stats and location
        self.act_path = ["Threaten", "Play", "Smile", "Hug", "231", ""]
        attack_functions = [enemy.rosalind_attack, enemy.rosalind_attack]

    def quack(self):
        global enemy_dialogue
        enemy_dialogue = ["Quack blocks the way!", "Quack brings a friend", "Woodward growls at you", "Quack watches you pet his little friend", "Both Quack and Woordward find you very amusing", "Quack and Woodward no longer want to fight."]
        self.enemy_attributes = ["Quack", 30, 40, False, -582]
        self.act_path = ["Taunt", "Ignore", "Joke", "Pet", "1323", ""]
        attack_functions = [enemy.patch_attack1, enemy.patch_attack2, enemy.patch_attack3]

    def desdemona(self):
        global enemy_dialogue
        enemy_dialogue = ["Desdemona blocks the way!", "Desmonda files her nails", "You are ignored", "She glares at you, the insult hits a sore spot", "Desdemona's confidence goes down", "Desdemona is getting scared", "Desdemona cowers in fright."]
        self.enemy_attributes = ["Desdemona", 30, 40, False, -759]
        self.act_path = ["Threaten", "Cheer", "Insult", "Scare", "2023", ""]
        attack_functions = [enemy.patch_attack1, enemy.patch_attack2, enemy.patch_attack3]

    def gallo(self):
        global enemy_dialogue
        enemy_dialogue = ["Gallo blocks the way!", "Gallo takes your phone", "Gallo transcends this realm of mortals. Your actions are meaningless."]
        self.enemy_attributes = ["Gallo", 300, 300, False, -881]
        self.act_path = ["Plead", "Reason", "Talk", "Compliment", "0", ""]
        attack_functions = [enemy.patch_attack1, enemy.patch_attack2, enemy.patch_attack3]

    def patch_attack1(self):
        global offset

        if offset < 220:
            offset += 1

        self.obstacle_pos = [width/2  - 107, height/2 + 67.5, width/2 - 110 + offset, height/2 + 137]

        fill(0, 0, 255)
        noStroke()
        rect(self.obstacle_pos[0], self.obstacle_pos[1], self.obstacle_pos[2], self.obstacle_pos[3])

    def patch_attack(self):
        global offset, obstacle_pos, ratio
        
        if offset < 220:
            offset += 1

        fill(255)
        stroke(255)
        strokeWeight(5)
        
        try:
            self.obstacle_pos = [width/2  - 110 + offset, (height/2) + 8.3 * ratio, width/2 - 50 + offset, (height/2 + 50) + 8.3 * ratio]
        except:
            raise Exception("offset and ratio need to be ints or floats.")
            
        try:
            rect(self.obstacle_pos[0], self.obstacle_pos[1], self.obstacle_pos[2], self.obstacle_pos[3])
        except:
            raise Exception("obstacle_pos needs to be a list containing ints or floats of at least 2 corners of an obstacle.")
        
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
            
    def act(self, act_index):  #problem
        index = 0
        number_correct_choices = 0

        if self.act_path[5] == "":
            self.act_path[5] = str(act_index)
        else:
            self.act_path[5] += str(act_index)

        fill(255)
        for action in range(0, len(self.act_path[4])):
            if self.act_path[5][index + 1:].count(self.act_path[4][action]) > 0:
                index = self.act_path[5][index:].find(self.act_path[4][action])
                number_correct_choices += 1
            else:
                return number_correct_choices
        else:
            return len(enemy_dialogue) - 1

    def collision_detection(self, player_pos):
        for coordinate in range(0, len(self.obstacle_pos), 4):
            try:
                player_pos[0] >= self.obstacle_pos[coordinate] and player_pos[0] <= self.obstacle_pos[coordinate + 2] \
                and player_pos[1] >= self.obstacle_pos[coordinate + 1] and player_pos[1] <= self.obstacle_pos[coordinate + 3] \
                    and self.collision_immune is False
            except:
                raise Exception("player_pos should contain the x and y pos (ints) of player in a list as separate elements. obstacle_pos should contain the location (x1, y1, x2, y2) of every obstacle as separate elements in a list.")
            else:
                if player_pos[0] >= self.obstacle_pos[coordinate] and player_pos[0] <= self.obstacle_pos[coordinate + 2] \
                    and player_pos[1] >= self.obstacle_pos[coordinate + 1] and player_pos[1] <= self.obstacle_pos[coordinate + 3] \
                        and self.collision_immune is False:
                    return True
        else:
            return False

    def immunity(self):
        if self.collision_immune:
            try:
                frameCount - self.immune_time_elapsed >= self.IMMUNE_TIME
            except:
                raise Exception("immune_time_elapsed and IMMUNE_TIME should be ints or floats.")
            else:
                if frameCount - self.immune_time_elapsed >= self.IMMUNE_TIME:
                    self.collision_immune = False
                    self.immune_time_elapsed = 0
            
    def reset(self):
        global offset, user, keys_pressed, player_pos, slide, user_color

        self.obstacle_pos = []
        offset = 0
        player_pos = [320, 308]
        user_color = "#FF0000"
        time.sleep(0.25)
        noTint()
        self.collision_immune = False


class User:
    user_health = []
    
    def __init__(self, health):
        self.user_health = health

    def use_item(self, item_index, list_items, list_item_values):
        try:
            value = list_item_values[item_index]
        except:
            raise Exception("item_index needs to be an int smaller than the length of list_item_values (needs to be list)")
        (list_item_values).pop(item_index)

        try:
            (list_items).pop(item_index)
        except:
            raise Exception("item_index needs to be an int smaller than the length of list_items (needs to be list)")

        try:
            self.user_health[0] += value
        except:
            raise Exception("user_health needs to be a list that contains only ints or floats.")

        try:
            self.user_health[0] > self.user_health[1]
        except:
            raise Exception("user_health needs 2 int or float elements.")
        else:
            if self.user_health[0] > self.user_health[1]:
                self.user_health[0] = self.user_health[1]


class Item:
    items = []
    item_values = []

    def __init__(self, item_list, health_values):
        self.items = item_list
        self.item_values = health_values


class Tests():
    def test_user_attack_damage_calc(self):
        assert user_attack_damage_calc(1, 10, 5) == 1,  "Should return 1"
        assert user_attack_damage_calc(3, 56, 5) == 2,  "Should return 2"
        assert user_attack_damage_calc(34, 200, 123) == 27,  "Should return 27"
        
    def test_user_movement(self):
        test_keys_pressed = keys_pressed
        assert user_movement(1, [230, 480], [38, 40, 37, 39], test_keys_pressed) == [230, 480], "There should be no change"
        test_keys_pressed[38] = True
        assert user_movement(1, [230, 480], [38, 40, 37, 39], test_keys_pressed) == [230, 479], "y position should decrease by 1"
        test_keys_pressed[38] = False
        test_keys_pressed[40] = True
        assert user_movement(3, [230, 480], [38, 40, 37, 39], test_keys_pressed) == [230, 483], "y position should increase by 3"
        test_keys_pressed[40] = False
        test_keys_pressed[37] = True
        assert user_movement(2, [230, 480], [38, 40, 37, 39], test_keys_pressed) == [228, 480], "x position should decrease by 2"
        test_keys_pressed[37] = False
        test_keys_pressed[39] = True
        assert user_movement(10, [230, 480], [38, 40, 37, 39], test_keys_pressed) == [240, 480], "x position should increase by 1"
        
    def test_movement_boundaries(self):
        assert movement_boundaries([230, 480], [430, 379, 210, 236], 10) == [230, 369], "y position should change to 369"
        assert movement_boundaries([230, 200], [430, 379, 210, 236], 10) == [230, 246], "y position should change to 24"
        assert movement_boundaries([500, 480], [430, 379, 210, 236], 10) == [420, 369], "x position should change to 420"
        assert movement_boundaries([100, 480], [430, 379, 210, 236], 10) == [220, 369], "x position should change to 220"

    def test_enemy_patch(self):
        test_class = Enemy()
        test_class.patch()
        assert enemy_dialogue == ["Patch blocks the way!", "You will be judged for your every action...", "Patch is annoyed", "Patch is taken aback, surprised.", "Patch smiles at you", "Patch laughs and his arrogant vibe dissolves into a friendly aura."], "Should be given patch's dialogue"
        assert test_class.enemy_attributes == ["Patch", 1, 50, False, -88], "Should be given Patch stats and location"
        assert test_class.act_path == ["Taunt", "Compliment", "Critcize", "Encourage", "131", ""], "Should be given actions user can do against Patch and solution to problem"
        assert attack_functions == [enemy.patch_attack1, enemy.patch_attack1], "Should be set to patch_attack"

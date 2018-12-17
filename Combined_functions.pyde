user_option_selection_counter = 0
slide = 0

def setup():
    size(640, 480)
    rectMode(CORNERS)
    text_font = loadFont("CharterBT-Bold-48.vlw")
    textFont(text_font)


def draw():
    global slide
    
    background(0)
    
    if slide == 0:
        title_screen()
        
    elif slide == 1:
        battle_screen()
        
    elif slide == 2:
        enemy = Enemy()
        fill(255)
        
        if user_option_selection_counter == 0:
            fight()
            
        elif user_option_selection_counter == 1:
            print_options(1, 5, enemy.patch())
                    
        elif user_option_selection_counter == 2:
            print_options(0, 4, enemy.display_items())
            
        else:
            mercy()
        
        
def title_screen():
    fill(255)
    textSize(80)
    text("Blundertale", width/2 - 205, height/2 + 40)
    textSize(20)
    text("Press 'z' to start", width/2 - 70, height/2 + 70)

        
def battle_screen():
    global user_option_selection_counter
    player_pos = [32, 442]
    
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
        
    # Player location changer (Could refactor)
    if user_option_selection_counter == 0:
        player_pos = [32, 442]
    elif user_option_selection_counter == 1:
        player_pos = [189, 442]
    elif user_option_selection_counter == 2:
        player_pos = [346, 442]
    else:
        player_pos = [503, 442]
        
    # Player
    ellipse(player_pos[0], player_pos[1], 10, 10)


def keyPressed():
    global user_option_selection_counter, slide
    
    if key == "z":
        slide += 1
    
    if key == "x":
        slide -= 1
    
    if slide == 1:
        # Changes option selection counter
        if keyCode == RIGHT and user_option_selection_counter < 3:
            user_option_selection_counter += 1
        elif keyCode == LEFT and user_option_selection_counter > 0:
            user_option_selection_counter -= 1
            

def fight():
    text("Hit enemy", 40, 259)
    

def print_options(min_range, max_range, options_list):
    # Will need to abstract text locations
    for option in range(min_range, max_range):
        if option < 3: # Need fix
            text(options_list[option], 40 + (100 * (option - 1)), 259)
        else:
            text(options_list[option], 40 + (100 * (option - 3)), 300)


def mousePressed():
    print(str(mouseX) + ", " + str(mouseY))
    
    
# Should put in seperate tab?
# Why does it force me to make an argument?
class Enemy:
    global enemy_attributes, items, mercy_options # Need fix
    enemy_attributes = []
    items = ["Food", "Food", "Food", "Food"]
    mercy_options = ["Spare", "Flee"]


    def patch(self):
        enemy_attributes = ["Patch", "Spray", "Heat", "Cut", "Sew", "Hi I'm Patch"]
        return enemy_attributes
    
    
    def display_items(self):
        return items
    
    
    def display_mercy_options(self):
        return mercy_options
    
    # Gotta make new functions for items, mercy, and act. One is for displaying and one is for changing/excecuting
        

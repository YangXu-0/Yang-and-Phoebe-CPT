user_option_selection_counter = 0
slide = 0

def setup():
    size(640, 480)
    rectMode(CORNERS)
    text_font = loadFont("CharterBT-Bold-48.vlw")
    textFont(text_font)


def draw():
    global slide, user_option_selection_counter
    
    background(0)
    
    if slide == 0:
        title_screen()
        
    if slide == 1 or slide == 2:
        battle_screen_display()
        
    if slide == 1:
        battle_screen_function()
        fill(255)
        text("Enemy dialogue", 60, 320)    
    elif slide == 2:
        enemy = Enemy()
        locked_option_selection = user_option_selection_counter
        user_option_selection_counter = 0 # Currently this breaks the program since it cycles rapidly (always changes to the first option). However, the plan is to build another function that takes care of all the user choosing stuff and use while loops which means this won't break the program
        fill(255)
        
        if locked_option_selection == 0:
            fight()
        elif locked_option_selection == 1:
            print_options(1, 5, enemy.patch())        
        elif locked_option_selection == 2:
            print_options(0, 4, enemy.items)
        else:
            print_options(0, 2, enemy.mercy_options)
        

def title_screen():
    fill(255)
    textSize(80)
    text("Blundertale", width/2 - 205, height/2 + 40)
    textSize(20)
    text("Press 'z' to start", width/2 - 70, height/2 + 70)

        
def battle_screen_display():    
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
    
    
def battle_screen_function():
    global user_option_selection_counter
    player_pos = [32, 442]
        
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
    slice_list = options_list[min_range: max_range]
    
    for option in range(0, len(slice_list)):
        text(slice_list[option], 60 + (option * 151), 320)


def mousePressed():
    print(str(mouseX) + ", " + str(mouseY))
    
    
# Should put in seperate tab?
# Why does it force me to make an argument?
class Enemy:
    enemy_attributes = []
    items = ["Food", "Food", "Food", "Food"]
    mercy_options = ["Spare", "Flee"]


    def patch(self):
        enemy_attributes = ["Patch", "Spray", "Heat", "Cut", "Sew", "Hi I'm Patch"]
        return enemy_attributes
    
    # Gotta make new functions for items, mercy, and act. One is for displaying and one is for changing/excecuting

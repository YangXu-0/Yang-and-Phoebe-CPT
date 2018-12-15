user_option_selection_counter = 0
select = False
slide = 0

def setup():
    size(640, 480)
    rectMode(CORNERS)
    text_font = loadFont("CharterBT-Bold-48.vlw")
    textFont(text_font)


def draw():
    global select, slide
    
    background(0)
    
    if slide == 0:
        title_screen()
    else:
        battle_screen()
     
        
def title_screen():
    global select, slide
    
    fill(255)
    textSize(80)
    text("Blundertale", width/2 - 205, height/2 + 40)
    textSize(20)
    text("Press 'z' to start", width/2 - 70, height/2 + 70)
    
    # Moves to next scene
    if select == True:
        slide += 1
        select = False

        
def battle_screen():
    global user_option_selection_counter, select
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
    
    # Chooses option
    if select == True:
        print(user_option_selection_counter)
        select = False


def keyPressed():
    global user_option_selection_counter, select, slide
    
    if key == "z":
        select = True
    
    if slide == 1:
        # Changes option selection counter
        if keyCode == RIGHT and user_option_selection_counter < 3:
            user_option_selection_counter += 1
        elif keyCode == LEFT and user_option_selection_counter > 0:
            user_option_selection_counter -= 1
            

def mousePressed():
    print(str(mouseX) + ", " + str(mouseY))

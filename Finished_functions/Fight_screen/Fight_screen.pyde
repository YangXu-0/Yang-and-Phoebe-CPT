def setup():
    size(640, 480)
    rectMode(CORNERS)
    text_font = loadFont("CharterBT-Bold-48.vlw")
    textFont(text_font)


def draw():
    background(0)
    battle_screen()
        
def battle_screen():
    player_pos = [32, 442]
    user_option_selection_counter = 0
    
    fill(0)
    stroke(255)
    strokeWeight(5)
    rect(12, 236, 628, 379)
    
    stroke("#FF8503")
    rect(12, 417, 157, 467)
    rect(169, 417, 314, 467)
    rect(326, 417, 471, 467)
    rect(483, 417, 628, 467)
    
    if key == "d" and user_option_selection_counter < 3:
        user_option_selection_counter += 1
    if key == "a" and user_option_slection_counter > 0:
        user_option_slection_counter -=1
    print(user_option_selection_counter)
        
    if user_option_selection_counter == 0:
        player_pos = [32, 442]
    elif user_option_selection_counter == 1:
        player_pos = [189, 442]
    elif user_option_selection_counter == 2:
        player_pos = [346, 442]
    else:
        player_pos = [503, 442]
        
        
    ellipse(player_pos[0], player_pos[1], 10, 10)


def mousePressed():
    print(str(mouseX) + ", " + str(mouseY))

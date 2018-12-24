offset = 0
slide = 0

def setup():
    size(640, 480)
    rectMode(CORNERS)
    

def draw():
    background(0)
    
    if slide == 0:
        fight_option()
    elif slide == 1:
        print(user_attack_damage_calc())
    
    
def fight_option():
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
        
        
def keyReleased():
    global slide
    
    if key == "z":
        slide += 1

OFFSET = 0
MOVING = False 

def setup():
    size(640, 480)
    rectMode(CORNERS)
    text_font = loadFont("CharterBT-Bold-48.vlw")
    textFont(text_font)


def draw():
    background(0)
    fight_option()        
    
def fight_option():
    global OFFSET, MOVING
    fill(0)
    stroke(255)
    strokeWeight(5)
    rect(70, 276, 570, 360)
    stroke(255, 59, 59)
    rect(320, 276, 320, 360)
    stroke(255)
    strokeWeight(10)
    rect(OFFSET + 70, 276, OFFSET + 80, 360)
    if OFFSET >= 490:
        MOVING = False 
    if MOVING == True:
        OFFSET += 8
        
def keyReleased(): 
    global MOVING
    if key.lower() == "z":
        if OFFSET == 0:
            MOVING = True
        else:
            MOVING = False
        

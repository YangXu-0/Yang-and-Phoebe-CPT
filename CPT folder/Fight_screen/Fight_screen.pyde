def setup():
    size(640, 480)
    rectMode(CORNERS)
    text_font = loadFont("CharterBT-Bold-48.vlw")
    textFont(text_font)


def draw():
    background(0)
    battle_screen()
        
def battle_screen():
    fill(0)
    stroke(255)
    strokeWeight(5)
    rect(12, 236, 628, 379)
    
    rect(12, 417, 157, 467)
    rect(169, 417, 314, 467)
    rect(326, 417, 471, 467)
    rect(483, 417, 628, 467)


def keyPressed():
    return key


def mousePressed():
    print(str(mouseX) + ", " + str(mouseY))

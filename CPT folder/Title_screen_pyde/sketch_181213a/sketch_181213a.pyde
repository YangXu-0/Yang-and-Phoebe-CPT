def setup():
    size(640, 480)
    rectMode(CORNERS)
    text_font = loadFont("CharterBT-Bold-48.vlw")
    textFont(text_font)


def draw():
    background(0)
    title_screen()


def title_screen():
    fill(255)
    textSize(80)
    text("Blundertale", width/2 - 205, height/2 + 40)
    textSize(20)
    text("Press 'z' to start", width/2 - 70, height/2 + 70)
    
    if key.lower() == "z":
        rect(0, 0, 640, 480)
        

def mousePressed():
    print(str(mouseX) + ", " + str(mouseY))

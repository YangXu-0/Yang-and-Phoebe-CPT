def setup():
    size(640, 480)
    rectMode(CORNERS)
    text_font = loadFont("CharterBT-Bold-48.vlw")
    textFont(text_font)


def draw():
    background(0)
    lose_screen()

def win_screen():
    fill(255)
    textSize(80)
    text("You Win!", width/2 - 175, height/2 + 40)
    textSize(10)
    text("...we'll get you next time", width/2+50, height/2+75)

    
    if key.lower() == "z":
        rect(0, 0, 640, 480)

        
def lose_screen():
    fill(255)
    textSize(80)
    text("You Lose.", width/2 - 175, height/2 + 40)
    textSize(10)
    text("how unfortunate :)", width/2+85, height/2+75)

    
    if key.lower() == "z":
        rect(0, 0, 640, 480)
        

def mousePressed():
    print(str(mouseX) + ", " + str(mouseY))

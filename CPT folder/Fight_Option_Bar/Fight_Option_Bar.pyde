def setup():
    size(640, 480)
    rectMode(CORNERS)
    text_font = loadFont("CharterBT-Bold-48.vlw")
    textFont(text_font)


def draw():
    background(0)
    fight_option()

def fight_option():
    fill(0)
    stroke(255)
    strokeWeight(5)
    rect(70, 276, 570, 360)
    strokeWeight(10)
    rect(70, 276, 80, 360)

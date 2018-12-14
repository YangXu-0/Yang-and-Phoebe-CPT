def setup():
    global img
    rectMode(CORNERS)
    size(640, 480)
    img = loadImage("https://upload.wikimedia.org/wikipedia/en/thumb/d/db/Undertale_Combat_Example.png/220px-Undertale_Combat_Example.png")
    

def draw():
    global img
    
    background(0)
    
    img.resize(640, 480)
    image(img, 0, 0)
    
    
def mousePressed():
    print(str(mouseX) + ", " + str(mouseY))

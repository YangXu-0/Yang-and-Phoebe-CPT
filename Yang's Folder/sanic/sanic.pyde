x = 0
x_increments = 1
temp = 0
animate = False

def setup():
    global gallo_img
    size(640, 480)
    gallo_img = loadImage("data/1385136139955.png")
    
def draw():
    global x, x_increments, animate
    
    if animate:
        x += x_increments
        if x >= 590:
            x_increments *= -1.25
        elif x <= 0:
            x_increments *= -1.25
    
    background(255, 255, 255)
    image(gallo_img, x, height/2, 100, 100)

def mousePressed():
    global animate
    animate = not animate
    
    

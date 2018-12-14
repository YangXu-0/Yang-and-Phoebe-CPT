x = 0
increments = 0
def setup():
    size(640, 580)

def draw():
    global x
    global increments
    if x == 0:
        increments = 3
    elif x >= 640:
        increments = -3
    x += increments
    
    background(28, 251, 255)
    noStroke()
    
    fill(255, 115, 0)
    rect(0, 480, 640, 20)
    fill(255, 51, 0)
    rect(0, 500, 640, 20)
    fill(255, 0, 106)
    rect(0, 520, 640, 20)
    fill(28, 3, 255)
    rect(0, 540, 640, 20)
    fill(72, 255, 6)
    rect(0, 560, 640, 20)
    
    translate(width/2, height/2)
    fill(255, 255, 255)
    rotate(radians(0 + x), )
    ellipse(x, height/2, 100, 50)
    ellipse(x + 30, height/2 + 30, 96, 60)
    ellipse(x - 30, height/2 + 30, 96, 60)
    ellipse(x - 50, height/2 - 10, 96, 60)
    stroke(0, 0, 0)
    fill(255, 255, 255)
    ellipse(x - 40, height/2, 30, 30)
    ellipse(x , height/2, 30, 30)
    fill(0, 0, 0)
    noStroke()
    ellipse(x-40, height/2, 10, 10)
    ellipse(x, height/2, 10, 10)

    #fill(0, 0, 70)
    #ellipse(x, height/2, 50, 50)
    #ellipse(x + 15, height/2 - 25, 35, 35)

import random

x = 0
timer = 0
random_x = 50
random_y = 50
zoom = 1
scale_inc = 0.05
start_scale = False

def setup():
    #global gallo_pic
    size(640, 580)
    #gallo_pic = loadImage("https://www.clipartmax.com/png/middle/8-86302_free-to-use-public-domain-zombie-clip-art-zombie-clipart-transparent-background.png")
    #imageMode(CENTER)
    
def draw():
    global x, timer, random_x, random_y, start_scale, zoom, scale_inc
    timer += 1
    
    if timer == random.randint(timer, 450):
        x = 240
        timer = 0
    
    if mousePressed:
        start_scale = True
    
    if start_scale:
        zoom += scale_inc
        translate(-width*zoom/2, -width*zoom/2)
        scale(zoom)
    
    if x >= 0:
        x -= 1.5
        
    background(87, 82, 100)
    noStroke()
    
    cloud(583, 108)
    cloud(469, 148)
    cloud(393, 90)
    
    #Land at back
    fill(58, 72, 63)
    ellipse(523, 431, 500, 200)
    
    #Land at middle
    fill(72, 90, 78)
    ellipse(120, 458, 550, 200)
    
    #Gravestones
    pushMatrix()
    rotate(PI/100)
    rectMode(CENTER)
    fill(30, 30, 30)
    rect(450, 330, 6, 60)
    rect(450, 320, 25, 5)
    rect(540, 330, 5, 60)
    rect(540, 320, 25, 5)
    rotate(PI/200)
    rect(480, 350, 5, 60)
    rect(480, 340, 25, 5)
    rect(500, 310, 5, 60)
    rect(500, 295, 25, 5)
    popMatrix()
    rect(500, 380, 8, 120)
    rect(500, 350, 40, 10)
    rect(565, 390, 7, 120)
    rect(565, 355, 30, 10)
    
    #House
    rect(200, 345, 150, 110)
    rect(200, 250, 50, 100)
    rect(165, 250, 20, 20)
    rect(130, 250, 20, 20)
    rect(95, 250, 10, 20)
    rect(140, 270, 100, 30)
    rect(135, 290, 40, 30)
    rect(235, 130, 6, 40)
    rect(218, 150, 40, 5)
    fill(255, 255, 0)
    rect(157, 336, 20, 20)
    fill(90, 48, 48)
    triangle(110, 304, 200, 224, 290, 304)
    triangle(225, 130, 235, 100, 245, 130)
    triangle(150, 200, 200, 100, 250, 200)
    fill(0)
    arc(200, 400, 50, 100, -PI, 0)
    
    #Moon
    fill(200, 255, 255, 80)
    ellipse(100, 100, 50, 50)
    
    #Land in front
    fill(81, 100, 87)
    ellipse(140, 571, 600, 300)
    ellipse(509, 488, 700, 200)
    
    #Test zombie
    #gallo_pic.resize(150, 0)
    #image(gallo_pic, 435, 459)
    
    rectMode(CORNERS)
    fill(255, x)
    rect(0, 0, width, height)
    
    fill(255, 255, 255)
    textSize(10)
    text(str(mouseX) + ", " + str(mouseY), mouseX, mouseY)
    
def cloud(x_location, y_location):
    fill(100, 99, 99, 150)
    ellipse(x_location, y_location, 100, 70)
    ellipse(x_location + 65, y_location - 18, 103, 73)
    ellipse(x_location + 126, y_location - 3, 100, 70)
    ellipse(x_location + 40, y_location + 34, 100, 50)
    ellipse(x_location + 120, y_location + 30, 97, 57)

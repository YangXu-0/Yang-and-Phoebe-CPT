import random

x = 0
timer = 0
random_x = 50
random_y = 50
zoom = 1
scale_inc = 0.05
start_scale = False
zoom_timer = 0

width = 720
height = 540
x_one = random.randint(10, width - 10)
y_one = random.randint(10, height - 10)
x_two = random.randint(10, width - 10)
y_two = random.randint(10, height - 10)
x_three = random.randint(10, width - 10)
y_three = random.randint(10, height - 10)

score = 0

def setup():
    global img
    size(640, 580)
    img = loadImage("background.JPG")
    
def draw():
    global x, timer, random_x, random_y, start_scale, zoom, zoom_timer, img, x_one, y_one, x_two, y_two, x_three, y_three
    timer += 1
    
    if zoom_timer <= 200:
        if timer == random.randint(timer, 450):
            x = 240
            timer = 0
    
        if x >= 0:
            x -= 1.5
        
        if key == ENTER:
            start_scale = True
        
        if start_scale:
            zoom += scale_inc
            translate(-324*zoom/2, -690*zoom/2)
            scale(zoom)
            if zoom_timer <= 210:
                zoom_timer += 1
            
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
        
        #Land in front
        fill(81, 100, 87)
        ellipse(140, 571, 600, 300)
        ellipse(509, 488, 700, 200)
        
        #Moon
        fill(200, 255, 255, 80)
        ellipse(540, 70, 50, 50)
        
        #Text
        textAlign(CENTER, CENTER)
        fill(255)
        textSize(25)
        text('Press enter bar to start game!', 320, 480)
        
        if zoom_timer >= 150:
            fill(0)
            rectMode(CORNERS)
            rect(0, 0, width, height)
            
    else:
        game()
    
    
def cloud(x_location, y_location):
    fill(100, 99, 99, 150)
    ellipse(x_location, y_location, 100, 70)
    ellipse(x_location + 65, y_location - 18, 103, 73)
    ellipse(x_location + 100, y_location - 3, 100, 70)
    ellipse(x_location + 40, y_location + 34, 100, 50)

    #Ghost
    fill(255, 255, 255, 70)
    arc(400, 200, 90, 200, -PI, 0)
    arc(370, 200, 30, 40, radians(0), radians(180))
    arc(400, 200, 30, 40, radians(0), radians(180))
    arc(430, 200, 30, 40, radians(0), radians(180))
    fill(0, 0, 0, 90)
    ellipse(385, 140, 10, 20)
    ellipse(415, 140, 10, 20)
    
def game():
    global img, x_one, y_one, x_two, y_two, x_three, y_three
    rectMode(CENTER)
    background(0)
    image(img, 0, 0)
    
    #Ghost one
    noStroke()
    fill(220)
    arc(x_one, y_one, 90, 200, -PI, 0)
    arc(x_one - 30, y_one, 30, 40, radians(0), radians(180))
    arc(x_one, y_one, 30, 40, radians(0), radians(180))
    arc(x_one + 30, y_one, 30, 40, radians(0), radians(180))
    fill(0)
    ellipse(x_one - 15, y_one - 70, 10, 20)
    ellipse(x_one + 15, y_one - 70, 10, 20)
    #Ghost coming down
    if y_one < 720:
        y_one += 10
    else:
        y_one = 0
        x_one = random.randint(10, width - 10)

    #Ghost two
    noStroke()
    fill(220)
    arc(x_two + 100, y_two + 100, 90, 200, -PI, 0)
    arc(x_two + 70, y_two + 100, 30, 40, radians(0), radians(180))
    arc(x_two + 100, y_two + 100, 30, 40, radians(0), radians(180))
    arc(x_two + 130, y_two + 100, 30, 40, radians(0), radians(180))
    fill(0)
    ellipse(x_two + 85, y_two + 30, 10, 20)
    ellipse(x_two + 115, y_two + 30, 10, 20)
    #Ghost coming down
    if y_two < 720:
        y_two += 10
    else:
        y_two = 0
        x_two = random.randint(10, width - 10)
        
    #Ghost three
    noStroke()
    fill(220)
    arc(x_three + 100, y_three + 100, 90, 200, -PI, 0)
    arc(x_three + 70, y_three + 100, 30, 40, radians(0), radians(180))
    arc(x_three + 100, y_three + 100, 30, 40, radians(0), radians(180))
    arc(x_three + 130, y_three + 100, 30, 40, radians(0), radians(180))
    fill(0)
    ellipse(x_three + 85, y_three + 30, 10, 20)
    ellipse(x_three + 115, y_three + 30, 10, 20)
    #Ghost coming down
    if y_three < 720:
        y_three += 10
    else:
        y_three = 0
        x_three = random.randint(10, width - 10)

    #PERSON
    fill(255)
    rect(mouseX, mouseY, 50, 50)
    
    #SCORE
    fill(255)
    rect(10, 10, 100, 50)
    textAlign(CENTER, CENTER)
    fill(0)
    textSize(25)
    text("Score:", 50, 25)
    textSize(15)
    text(second() + minute(), 45, 45)

    if (mouseX > x_one - 50 and mouseX < x_one + 50 and mouseY > y_one - 150 and mouseY < y_one + 20) or (mouseX > x_two and mouseX < x_two + 100 and mouseY > y_two - 50 and mouseY < y_two + 100) or (mouseX > x_three and mouseX < x_three + 150 and mouseY > y_three - 50 and mouseY < y_three + 100):
        textAlign(CENTER, CENTER)
        background(0)
        fill(255)
        textSize(150)
        text('YOU LOSE', width/2, height/2)

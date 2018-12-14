x_animated = 0
y = 0
y_animated = 1
x_increments = 0.1

def setup():
    size(640, 580)

def draw():
    #x_animated, x_increments, and y_increments are used to change location
    #y is used to shift objects if needed
    global x_animated, y, y_animated, x_increments
    
    movement_changes()
    
    background(114, 170, 255)
    noStroke()
    
    draw_sun()
    draw_land()
    draw_clouds()
    draw_bushes()
    draw_overlay()

def movement_changes():
    global x_animated, y, y_animated, x_increments
    x_animated += x_increments
    
    #controls sun and yellow overlay
    if y_animated >= -200:
        y_animated -= 0.07
        
    #controls movement of clouds
    if x_animated >= 400:
        x_increments = -0.1
    elif x_animated <= 0:
        x_increments = 0.1

def draw_sun():
    fill(255, 170, 0)
    #sun
    ellipse(width/2, 410 + y_animated, 150, 150)
    
def draw_land():
    fill(49, 126, 24)
    #land
    rect(0, 420 + y, 640, 580)
    ellipse(120, 450 + y, 300, 100)
    ellipse(292, 440 + y, 150, 50)
    ellipse(480, 440 + y, 300, 100)
    ellipse(640, 450 + y, 300, 100)
    
def draw_clouds():
    fill(255, 255, 255, 220)
    #big cloud
    ellipse(x_animated + 139, 230 + y, 100, 50)
    ellipse(x_animated + 169, 260 + y, 96, 60)
    ellipse(x_animated + 109, 260 + y, 96, 60)
    ellipse(x_animated + 89, 220 + y, 96, 60)
    
    #smaller cloud
    ellipse((x_animated * -1) + 500, 120 + y, 100, 50)
    ellipse((x_animated * -1) + 450, 90 + y, 96, 60)
    
    #smallest cloud
    ellipse((x_animated * -1) + 500, 350 + y, 100, 50)
    
def draw_bushes():
    fill(38, 93, 8)
    # bush #1 (far left)
    ellipse(78, 451, 30, 30)
    ellipse(100, 432, 50, 50)
    ellipse(121, 438, 40, 40)
    ellipse(140, 436, 40, 40)
    ellipse(147, 448, 30, 30)
    ellipse(99, 459, 30, 10)
    ellipse(85, 463, 30, 10)
    ellipse(117, 460, 40, 20)
    ellipse(140, 459, 30, 10)
    
    #bush #2 (top right)
    ellipse(552, 390, 50, 40)
    ellipse(576, 376, 50, 40)
    ellipse(598, 384, 50, 40)
    ellipse(577, 390, 50, 40)
    ellipse(601, 394, 40, 30)
    
    #bush #3 (middle)
    ellipse(450, 484, 50, 40)
    ellipse(464, 505, 50, 40)
    ellipse(432, 506, 50, 40)
    ellipse(400, 506, 50, 40)
    ellipse(416, 490, 50, 40)
    
def draw_overlay():
    fill(255, 225, 0 + ((y_animated + 15) * -3.25), 90)
    #overlay
    rect(0, 0, 640, 580)

value = 0

def draw():
    global value
    fill(value)
    rect(25, 25, 50, 50)
    
def keyPressed():
    global value
    if value == 0:
        value = 255
    else:
        value  = 0

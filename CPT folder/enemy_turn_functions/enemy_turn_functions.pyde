player_pos = [320, 308]

def setup():
    size(640, 480)
    rectMode(CORNERS)


def draw():
    background(0)
    battle_screen_display()
    user_movement()
    

def battle_screen_display():    
    # Textbox
    fill(0)
    stroke(255)
    strokeWeight(5)
    rect(width/2 - 110, height/2 - 4, width/2 + 110, height/2 + 139)
    
    # Selection boxes
    stroke("#FF8503")
    rect(12, 417, 157, 467)
    rect(169, 417, 314, 467)
    rect(326, 417, 471, 467)
    rect(483, 417, 628, 467)


def user_movement():
    global player_pos
    
    if keyPressed:
        if keyCode == UP:
            player_pos[1] -= 1.5
        elif keyCode == DOWN:
            player_pos[1] += 1.5
        elif keyCode == LEFT:
            player_pos[0] -= 1.5
        elif keyCode == RIGHT:
            player_pos[0] += 1.5
            
    if not(player_pos[0] >= (210 + 10)):
        player_pos[0] = (210 + 10)
    if not(player_pos[0] <= (430 - 10)):
        player_pos[0] = (430 - 10)
    if not(player_pos[1] >= (236 + 10)):
        player_pos[1] = (236 + 10)
    if not(player_pos[1] <= (379 - 10)):
        player_pos[1] = (379 - 10)
            
    draw_user(player_pos[0], player_pos[1])
        
    
def draw_user(x_pos, y_pos):
    fill(255, 0, 0)
    ellipse(x_pos, y_pos, 10, 10)

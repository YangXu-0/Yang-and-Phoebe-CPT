grid = []

def setup():
    size(640, 580)

def start():
    global grid
    vertical = [1, 2, 3, 4, 5, 6, 7]

    for horizontal in range(1, 8):
        grid.append(vertical)
    
    return grid

#for i in range(1, 8):
#    for j in range(0, 7):
    rect(grid[i], grid[i][j], 1, 1)

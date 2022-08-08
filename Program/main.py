import pygame as pg
from xo import XO
from checkWin import checkWin

pg.init()
WIDTH, HEIGHT = 360, 360
CELL_SIZE = 110,110
CELL_SEPERATION = 15
BOARD_IMAGE = pg.image.load("Program/Assets/board.png")
GAME_RUNNING = True

screen = pg.display.set_mode((WIDTH, HEIGHT))

def placeXO(cellSize, cellSeperation):
    x, y = pg.mouse.get_pos()
    xIndex = abs( -cellSeperation // 2 - x) // (cellSize[0] + cellSeperation)
    yIndex = abs( -cellSeperation // 2 - y) // (cellSize[1] + cellSeperation)

    #The "+13" is a padding value that you have to experiment with to place them right
    xPos = xIndex*(CELL_SIZE[0] + cellSeperation) + 5
    yPos = yIndex*(CELL_SIZE[1] + cellSeperation) + 5
    return xPos, yPos, xIndex, yIndex

# Update what images are drawn to the screen    
xoImages = []
isX = True
def updateXO(position: tuple, indeces: tuple):
    global xoImages
    global isX

    # Return if an image is already in the cell
    for i in xoImages:
        if position == i.position:
            return
    
    # Place an image in the cell
    isX = not isX
    img = XO("x" if isX else "o", position, indeces)

    xoImages.append(img)



while GAME_RUNNING:
    # Setup Screen
    screen.fill((255,255,255))
    screen.blit(BOARD_IMAGE, (0,0))

    # Make sure game closes when you press 'X'
    pygameEvents = pg.event.get()
    for event in pygameEvents:
        if event.type == pg.QUIT:
            GAME_RUNNING = False
        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                xPos, yPos, xInd, yInd = placeXO(CELL_SIZE, CELL_SEPERATION)
                updateXO((xPos, yPos), (xInd, yInd))

    # Check for wins
    if checkWin(xoImages):
        if isX:
            print("Yay! X Wins!")
            break
        else:
            print("Yes! O Wins!")
            break

    # Draw Other Imgaes
    for i in xoImages:
        screen.blit(i.image, i.position)
    

    # Update Screen
    pg.display.update()



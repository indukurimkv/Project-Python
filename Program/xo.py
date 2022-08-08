import pygame as pg
class XO:
    def __init__(self, value, position, indeces):
        # value must be x or o
        self.value = value
        self.position = position
        self.indeces = indeces

        self.loadImage()

    def loadImage(self):
        self.image = pg.image.load(f"Program/Assets/{self.value}.png")

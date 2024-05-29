import pygame
import sys
class Police:
    color=None
    row=None
    col=None
    width=None
    heigth=None
    def getColor(self):
        return self.color
    def getRow(self):
        return self.row
    def getCol(self):
        return self.col
    def __init__(self,color,col,row,width,height):
        self.color=color
        self.row=row
        self.col=col
        self.width=width
        self.heigth=height
        
    def drawMe(self,screen,cellSize):
        pygame.draw.rect(screen, self.color, (self.col * cellSize, self.row * cellSize, self.width, self.heigth))
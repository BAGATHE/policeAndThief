import numpy as np
import pygame
import sys
from voleur import Voleur
class Terrain:
    matrice = []
    voleur=None
    police=[]
    def getMatrice(self):
        return self.matrice
    def setMatrice(self,matrice):
        self.matrice = matrice
        
    def __init__(self,matrice,voleur,police):
        self.setMatrice(matrice)
        self.voleur=voleur
        self.police=police
        
    def initialize(self):
        self.matrice=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                      [1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1],
                      [1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1],
                      [1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,1],
                      [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
                      [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
                      [1,1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1],
                      [1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1],
                      [1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1],
                      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                      [1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1],
                      [1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1],
                      [1,1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1],
                      [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
                      [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
                      [1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,1],
                      [1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1],
                      [1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1],
                      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],]
            

    def drawMe(self):
        # Définition des constantes
        CELL_SIZE = 20
        ROWS = 19
        COLS = 19
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        GREEN = (0, 255, 0)
        # Matrice représentant le terrain de jeu
        # Initialisation de pygame
        pygame.init()
        WINDOW_SIZE = (COLS * CELL_SIZE, ROWS * CELL_SIZE)
        screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Terrain de jeu")

        # Fonction pour dessiner le terrain
        def draw_terrain():
            for y in range(ROWS):
                for x in range(COLS):
                    color = WHITE if self.getMatrice()[y][x] == 1 else BLACK
                    pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            self.voleur.drawMe(screen,CELL_SIZE)
            for i in range(len(self.police)):
                self.police[i].drawMe(screen,CELL_SIZE)
            pygame.display.flip()

        # Boucle principale
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    clicked_cell_x = mouse_x // CELL_SIZE
                    clicked_cell_y = mouse_y // CELL_SIZE
            
            # Dessiner le terrain
            draw_terrain()

        # Quitter pygame
        pygame.quit()
        sys.exit()
from Terrain import Terrain
from voleur import Voleur
from police import Police
if __name__ == "__main__":
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    police1 = Police(RED,6,9,20,20)
    police2 = Police(RED,9,6,20,20)
    police3 = Police(RED,12,9,20,20)
    police=[]
    police.append(police1)
    police.append(police2)
    police.append(police3)
    voleur = Voleur(GREEN,9,9,20,20)
    terrain = Terrain(None,voleur,police)
    terrain.initialize()
    terrain.drawMe()
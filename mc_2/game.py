#write here a code for main window of the game
from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Load the map
        self.land = Mapmanager()
        x,y = self.land.loadLand("land3.txt")
        self.hero = Hero((x//2,y//2,2),self.land)
        
        # Set field of view
        base.camLens.setFov(120)
        
        # Move camera and set it to look down
        base.camera.setPos(6, -2, 10)  # Back y units, up z units
        base.camera.setHpr(0, -45, 0)   # Heading, Pitch (look down), Roll

game = Game()
game.run()
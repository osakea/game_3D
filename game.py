#write here code for app's main window
from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager

# class
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        base.camLens.setFov(100)
        
game = Game()
game.run()
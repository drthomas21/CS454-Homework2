from direct.showbase.DirectObject       import DirectObject      
from direct.gui.OnscreenText            import OnscreenText 
from direct.gui.DirectGui               import *
from panda3d.core                       import *

class CharacterSelectScreen:
    def __init__(self,World,render,base):
        self.World = World;
        
        boxloc = Vec3(0.0, 0.0, 0.0)
        p = boxloc
        World.LoginFrame = DirectFrame(pos=p) 

    def unloadScreen(self):
        self.World.LoginFrame.destroy()
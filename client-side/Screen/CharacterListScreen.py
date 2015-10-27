from direct.showbase.DirectObject           import DirectObject      
from direct.gui.OnscreenText                import OnscreenText 
from direct.gui.DirectGui                   import *
from direct.gui.DirectScrolledList          import DirectScrolledList
from panda3d.core                           import *

class CharacterListScreen:
    def __init__(self,World,render,base):
        self.World = World;
        self.World.accept("tab",self.toggleScreen)
        
        boxloc = Vec3(0.65, 0.0, 0.7)
        frameSize = Vec4(0.0, 0.7, -0.05, 0.59)
        p = boxloc
        self.CharListFrame = DirectFrame(frameColor=(0,0,0,0.4),frameSize=frameSize,pos=p)       

        #size = frameSize + Vec4(0.0,0.0,-0.5,0.0)
        size = frameSize
        self.CharListFrame.scrolledList = DirectScrolledList(
            parent=self.CharListFrame,
            
            decButton_pos= (0.2, 0, 0.53),
            decButton_text = "Up",
            decButton_text_scale = 0.04,
            decButton_borderWidth = (0.1, 0.005),
         
            incButton_pos= (0.5, 0, 0.53),
            incButton_text = "Down",
            incButton_text_scale = 0.04,
            incButton_borderWidth = (0.1, 0.005),
            
            frameSize=size,
            frameColor = (0,0,0,0.0),
            #pos=p,
            numItemsVisible = 6,
            #forceHeight = 0.11,
            itemFrame_frameSize = (-0.35, 0.35, -0.37, 0.11),
            itemFrame_pos = (0.35, 0, 0.4),
            itemFrame_frameColor=(0,0,0,0) 
        )
        
    def toggleScreen(self):
        if self.hidden:
            self.showScreen()
        else:
            self.hideScreen()
            
    def updateStatus(self, statustext):
        self.CharListFrame.statusText.setText(statustext)
        
    def unloadScreen(self):
        self.CharListFrame.destroy()
        
    def hideScreen(self):
        self.CharListFrame.hide()
        self.hidden = True
        
    def showScreen(self):
        self.CharListFrame.show()        
        self.hidden = False          
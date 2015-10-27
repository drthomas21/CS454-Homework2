from direct.showbase.DirectObject           import DirectObject      
from direct.gui.OnscreenText                import OnscreenText 
from direct.gui.DirectGui                   import *
from direct.gui.DirectScrolledList          import DirectScrolledList
from panda3d.core                           import *

class NotificationScreen:
    def __init__(self,World,model):
        self.World = World;
        self.World.accept("tab",self.toggleScreen)
        
        boxloc = Vec3(0,0,0)
        p = boxloc
        self.NotifyMessage = OnscreenText(text = "", pos = p, scale = 0.07,fg=(1, 1, 1, 1),align=TextNode.ACenter)
        taskMgr.doMethodLater(3,self.hideScreen,"autoHideNotify")    

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
        self.NotifyMessage.statusText.setText(statustext)
        
    def unloadScreen(self):
        if self.NotifyMessage != None:
            self.NotifyMessage.destroy()
            self.NotifyMessage = None;
        
    def hideScreen(self):
        self.NotifyMessage.destroy()
        self.hidden = True
        
    def showScreen(self):
        if self.NotifyMessage == None:
            self.NotifyMessage = self.NotifyMessage
        self.hidden = False          
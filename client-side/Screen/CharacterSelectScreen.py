from direct.showbase.DirectObject       import DirectObject      
from direct.gui.OnscreenText            import OnscreenText 
from direct.gui.DirectGui               import *
from panda3d.core                       import *
from pandac.PandaModules                import * 
import sys

class CharacterSelectScreen:
    def __init__(self,World,render,base,camera):
        characterModels = World.characterModels
        self.availableModels = []
        
        for model in characterModels:
            print model[1]
            model[1].actor.name = model[0]
            
        if len(characterModels) >= 1:
            Character = characterModels[0][1]
            Character.actor.setPos(0,0,0)
            camera.setPos(Character.actor.getX(),Character.actor.getY()+10,2)
            camera.lookAt(Character.actor)
            Character.lookAt(camera)
            self.availableModels.append(Character)
            
        if len(characterModels) >= 2:
            Character = characterModels[1][1]
            Character.actor.setPos(2,0,0)
            Character.lookAt(base.camera)
            self.availableModels.append(Character)
            
        if len(characterModels) >= 3:
            Character = characterModels[2][1]
            Character.actor.setPos(-2,0,0)
            Character.lookAt(base.camera)
            self.availableModels.append(Character)
            
        boxloc = Vec3(0.0, 0.0, 0.0)
        p = boxloc + Vec3(0.0, 0.0, -0.5)
        World.SelectionFrame = DirectFrame(frameColor=(0,0,0,0.4),frameSize=(-1,1,-0.1,0.2),pos=p)       

        p = boxloc + Vec3(0.0, 0.0, 0.0)                                 
        World.SelectionFrame.textObject = OnscreenText(parent=World.SelectionFrame, text = "Select Your Character", pos = p, scale = 0.2,fg=(1, 1, 1, 1),align=TextNode.ACenter)
        
        self.makePickable()
        self.picker= CollisionTraverser() 
        self.queue=CollisionHandlerQueue() 
        
        self.pickerNode=CollisionNode('mouseRay') 
        self.pickerNP=camera.attachNewNode(self.pickerNode) 
        
        self.pickerNode.setFromCollideMask(GeomNode.getDefaultCollideMask()) 
        
        self.pickerRay=CollisionRay() 
        
        self.pickerNode.addSolid(self.pickerRay) 
        
        self.picker.addCollider(self.pickerNP, self.queue)
        
        #this holds the object that has been picked 
        self.pickedObj=None 
        
        World.accept('mouse1', self.getSelectedObject)
        
        self.base = base
        self.render = render
        self.World = World
    
    def makePickable(self):
        for model in self.availableModels:
            model.actor.setPythonTag('pickable','true')
        
    def getSelectedObject(self): 
        self.getObjectHit( self.base.mouseWatcherNode.getMouse())
        if self.pickedObj != None: 
            #self.World.selectedCharacter(self.pickedObj)
            self.unloadScreen()
        
    def getObjectHit(self, mpos): #mpos is the position of the mouse on the screen 
        self.pickedObj=None #be sure to reset this 
        self.pickerRay.setFromLens(self.base.camNode, mpos.getX(),mpos.getY()) 
        self.picker.traverse(self.render) 
        if self.queue.getNumEntries() > 0: 
            self.queue.sortEntries() 
            self.pickedObj=self.queue.getEntry(0).getIntoNodePath() 
            
            parent=self.pickedObj.getParent() 
            self.pickedObj=None
            
            while parent != self.render:
                if parent.getPythonTag('pickable')=='true': 
                    self.pickedObj=parent
                    return parent
                else:
                    parent=parent.getParent()
        return None  

    def unloadScreen(self):
        self.World.SelectionFrame.destroy()
        print self.pickedObj
        #for model in self.availableModels:
        #    if model.actor.name != self.pickedObj.name:
        #        model.actor.delete()
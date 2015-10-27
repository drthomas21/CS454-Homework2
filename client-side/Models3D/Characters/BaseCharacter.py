import sys
from panda3d.core               import PandaNode,NodePath,Camera,TextNode
from Models3D.BaseModel3D       import BaseModel3D

class BaseCharacter(BaseModel3D):
    floater = None
    def __init__(self, World, render, base,loader):
        BaseModel3D.__init__(self, World, render, base,loader)

    def setControls(self):
        if self.floater == None:
            self.floater = NodePath(PandaNode("floater"))
            self.floater.reparentTo(self.render)
            self.isMoving = False
        
        self.World.keyMap = {"left":0, "right":0, "forward":0, "cam-left":0, "cam-right":0}
        self.World.accept("escape", self.World.endSession)
        self.World.accept("a", self.setKey, ["left",1])
        self.World.accept("d", self.setKey, ["right",1])
        self.World.accept("w", self.setKey, ["forward",1])
        self.World.accept("q", self.setKey, ["cam-left",1])
        self.World.accept("e", self.setKey, ["cam-right",1])
        self.World.accept("a-up", self.setKey, ["left",0])
        self.World.accept("d-up", self.setKey, ["right",0])
        self.World.accept("w-up", self.setKey, ["forward",0])
        self.World.accept("q-up", self.setKey, ["cam-left",0])
        self.World.accept("e-up", self.setKey, ["cam-right",0])
        self.World.accept("shift-w",self.setKey, ["forward",5])
        
    def blockControls(self):
        self.World.ignore("escape")
        self.World.ignore("a")
        self.World.ignore("d")
        self.World.ignore("w")
        self.World.ignore("q")
        self.World.ignore("e")
        self.World.ignore("a-up")
        self.World.ignore("d-up")
        self.World.ignore("w-up")
        self.World.ignore("q-up")
        self.World.ignore("e-up")
        self.World.ignore("shift-w")
    
    def setCharacter(self, _Actor):
        self.actor = _Actor
    
    #Records the state of the arrow keys
    def setKey(self, key, value):
        self.World.keyMap[key] = value
        
    # Accepts arrow keys to move either the player or the menu cursor,
    # Also deals with grid checking and collision detection
    def move(self, task):

        self.base.camera.lookAt(self.actor)
        if (self.World.keyMap["cam-left"]!=0):
            self.base.camera.setX(self.base.camera, -20 * globalClock.getDt())
        if (self.World.keyMap["cam-right"]!=0):
            self.base.camera.setX(self.base.camera, +20 * globalClock.getDt())

        startpos = self.actor.getPos()

        #print self.actor.name
        #print self.World.keyMap
        if (self.World.keyMap["left"]!=0):
            self.actor.setH(self.actor.getH() + 300 * globalClock.getDt())
        if (self.World.keyMap["right"]!=0):
            self.actor.setH(self.actor.getH() - 300 * globalClock.getDt())
        if (self.World.keyMap["forward"]!=0 and self.World.keyMap["forward"]!=5 and self.actor.name =='Ralph'):
            self.actor.setY(self.actor, -25 * globalClock.getDt())
        if (self.World.keyMap["forward"]!=0 and self.World.keyMap["forward"]!=1 and self.actor.name == 'Ralph'):
            self.actor.setY(self.actor, -100 * globalClock.getDt())
        if (self.World.keyMap["forward"]!=0 and self.World.keyMap["forward"]!=5 and self.actor.name != 'Ralph'):
            self.actor.play("walk")
            self.actor.loop("walk")
            self.actor.setY(self.actor, -1000 * globalClock.getDt())
        if (self.World.keyMap["forward"]!=0 and self.World.keyMap["forward"]!=1 and self.actor.name != 'Ralph'):
            self.actor.play("walk")
            self.actor.loop("walk")
            self.actor.setY(self.actor, -2000 * globalClock.getDt())

        self.World.MoveManager.appendAction(left = self.World.keyMap["left"], right = self.World.keyMap["right"], forward = self.World.keyMap["forward"], pos = self.actor.getPos())
        #self.actor.stop()

        #if (self.World.keyMap["backward"]!=0):
        #    self.actor.setY(self.actor, 25 * globalClock.getDt())

        if (self.World.keyMap["forward"]!=0) or (self.World.keyMap["left"]!=0) or (self.World.keyMap["right"]!=0):
            if self.isMoving is False:
                self.actor.loop("run")
                self.isMoving = True
        else:
            if self.isMoving:
                self.actor.stop()
                self.actor.pose("walk",5)
                self.isMoving = False

        camvec = self.actor.getPos() - self.base.camera.getPos()
        camvec.setZ(0)
        camdist = camvec.length()
        camvec.normalize()
        if (camdist > 10.0):
            self.base.camera.setPos(self.base.camera.getPos() + camvec*(camdist-10))
            camdist = 10.0
        if (camdist < 5.0):
            self.base.camera.setPos(self.base.camera.getPos() - camvec*(5-camdist))
            camdist = 5.0

        self.floater.setPos(self.actor.getPos())
        self.floater.setZ(self.actor.getZ() + 2.0)
        self.base.camera.lookAt(self.floater)

        return task.cont
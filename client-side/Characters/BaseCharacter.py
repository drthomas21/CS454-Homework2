import sys
from panda3d.core import PandaNode,NodePath,Camera,TextNode

class BaseCharacter:
    def __init__(self, World, render):
        self.floater = NodePath(PandaNode("floater"))
        self.floater.reparentTo(render)
        self.isMoving = False
        
        World.keyMap = {"left":0, "right":0, "forward":0, "cam-left":0, "cam-right":0}
        World.accept("escape", sys.exit)
        World.accept("arrow_left", self.setKey, ["left",1])
        World.accept("arrow_right", self.setKey, ["right",1])
        World.accept("arrow_up", self.setKey, ["forward",1])
        World.accept("a", self.setKey, ["cam-left",1])
        World.accept("s", self.setKey, ["cam-right",1])
        World.accept("arrow_left-up", self.setKey, ["left",0])
        World.accept("arrow_right-up", self.setKey, ["right",0])
        World.accept("arrow_up-up", self.setKey, ["forward",0])
        World.accept("a-up", self.setKey, ["cam-left",0])
        World.accept("s-up", self.setKey, ["cam-right",0])
        self.World = World
    
    def setCharacter(self, _Actor):
        self.Character = _Actor
    
    #Records the state of the arrow keys
    def setKey(self, key, value):
        self.World.keyMap[key] = value
        
    # Accepts arrow keys to move either the player or the menu cursor,
    # Also deals with grid checking and collision detection
    def move(self, task):
        # If the camera-left key is pressed, move camera left.
        # If the camera-right key is pressed, move camera right.

        base.camera.lookAt(self.Character)
        if (self.World.keyMap["cam-left"]!=0):
            base.camera.setX(base.camera, -20 * globalClock.getDt())
        if (self.World.keyMap["cam-right"]!=0):
            base.camera.setX(base.camera, +20 * globalClock.getDt())

        # save ralph's initial position so that we can restore it,
        # in case he falls off the map or runs into something.

        startpos = self.Character.getPos()

        # If a move-key is pressed, move ralph in the specified direction.

        if (self.World.keyMap["left"]!=0):
            self.Character.setH(self.Character.getH() + 300 * globalClock.getDt())
        if (self.World.keyMap["right"]!=0):
            self.Character.setH(self.Character.getH() - 300 * globalClock.getDt())
        if (self.World.keyMap["forward"]!=0):
            self.Character.setY(self.Character, -25 * globalClock.getDt())

        # If ralph is moving, loop the run animation.
        # If he is standing still, stop the animation.

        if (self.World.keyMap["forward"]!=0) or (self.World.keyMap["left"]!=0) or (self.World.keyMap["right"]!=0):
            if self.isMoving is False:
                self.Character.loop("run")
                self.isMoving = True
        else:
            if self.isMoving:
                self.Character.stop()
                self.Character.pose("walk",5)
                self.isMoving = False

        # If the camera is too far from ralph, move it closer.
        # If the camera is too close to ralph, move it farther.

        camvec = self.Character.getPos() - base.camera.getPos()
        camvec.setZ(0)
        camdist = camvec.length()
        camvec.normalize()
        if (camdist > 10.0):
            base.camera.setPos(base.camera.getPos() + camvec*(camdist-10))
            camdist = 10.0
        if (camdist < 5.0):
            base.camera.setPos(base.camera.getPos() - camvec*(5-camdist))
            camdist = 5.0

         
        # The camera should look in ralph's direction,
        # but it should also try to stay horizontal, so look at
        # a floater which hovers above ralph's head.
        
        self.floater.setPos(self.Character.getPos())
        self.floater.setZ(self.Character.getZ() + 2.0)
        base.camera.lookAt(self.floater)

        return task.cont
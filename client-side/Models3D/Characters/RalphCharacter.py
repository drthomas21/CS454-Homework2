from Models3D.Characters.BaseCharacter  import BaseCharacter
from panda3d.core                       import *
from pandac.PandaModules                import *
from direct.actor.Actor                 import Actor

class RalphCharacter(BaseCharacter):
    count = 0    
    def __init__(self,World, render,base,loader):
        BaseCharacter.__init__(self,World, render,base,loader)
        RalphCharacter.count += 1
        self.id = RalphCharacter.count

        self.actor = Actor("models/ralph/ralph",
                         {"run":"models/ralph/ralph-run",
                          "walk":"models/ralph/ralph-walk"})
        self.actor.reparentTo(render)
        self.actor.setScale(.2)
        self.actor.setPos(int(self.id)*20, 0, 0)

        # Create a collsion node for this object.
        self.cNode = CollisionNode('ralph')
        # Attach a collision sphere solid to the collision node.
        self.cNode.addSolid(CollisionSphere(0, 0, 3, 3))
        # Attach the collision node to the object's model.
        self.smileyC = self.actor.attachNewNode(self.cNode)
        base.cTrav.addCollider(self.smileyC, World.pusher)
        World.pusher.addCollider(self.smileyC, self.actor, base.drive.node())
        
    def getActor(self):
        return self.actor

    def getRalphCount(self):
        return MyRalph.count

    def getMyRalphId(self):
        return self.id
    
    def lookAt(self,model):
        self.actor.lookAt(model)
        hpr = self.actor.getHpr()
        self.actor.setHpr(hpr[0]+180,hpr[1],hpr[2])
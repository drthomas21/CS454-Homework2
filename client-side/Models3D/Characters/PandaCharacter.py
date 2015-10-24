from Models3D.Characters.BaseCharacter  import BaseCharacter
from panda3d.core                       import *
from pandac.PandaModules                import *
from direct.actor.Actor                 import Actor

class PandaCharacter(BaseCharacter):
    count=0
    def __init__(self,World, render,base,loader):
        BaseCharacter.__init__(self,World, render,base,loader)
        PandaCharacter.count += 1
        self.id = PandaCharacter.count

        self.pandaNode=render.attachNewNode('pandaNode')
        self.actor=Actor("models/panda-model",
                     {"walk": "models/panda-walk4"})
        self.actor.reparentTo(self.pandaNode)
        self.actor.setPos(int(self.id) * 30,0,0)
        self.actor.setScale(0.002, 0.002, 0.002)

        self.cNode = CollisionNode('panda')
        self.cNode.addSolid(CollisionSphere(2, 0, 400, 500))
        self.frowneyC = self.actor.attachNewNode(self.cNode)
        base.cTrav.addCollider(self.frowneyC, World.pusher)
        World.pusher.addCollider(self.frowneyC, self.actor, base.drive.node())

    def getActor(self):
        return self.actor

    def getPandaCount(self):
        return MyRalph.count

    def getMyPandaId(self):
        return self.id  
    
    def lookAt(self,model):
        self.actor.lookAt(model)
        hpr = self.actor.getHpr()
        self.actor.setHpr(hpr[0]+180,hpr[1],hpr[2])
from Models3D.Characters.BaseCharacter  import BaseCharacter
from panda3d.core                       import *
from pandac.PandaModules                import *
from direct.actor.Actor                 import Actor

class VechileCharacter(BaseCharacter):
    count=0
    def __init__(self,World, render,base,loader):
        BaseCharacter.__init__(self,World, render,base,loader)
        VechileCharacter.count += 1
        self.carNode = render.attachNewNode('dummy_car')
        self.car = loader.loadModel("models/knucklehead")
        self.car_tex = loader.loadTexture("models/knucklehead.jpg")
        self.car.setTexture(self.car_tex, 1)
        self.car.reparentTo(self.carNode)
        self.car.setPos(20,20,0)
        self.car.setScale(.08)
        self.car.setP(-90)
        self.car.setColor(0.6, 0.6, 1.0, 1.0)
        self.car.setColorScale(0.6, 0.6, 1.0, 1.0)

        self.carCNode = CollisionNode('car')
        self.carCNode.addSolid(CollisionSphere(0, 0, 3, 3))
        self.carC = self.car.attachNewNode(self.carCNode)
        base.cTrav.addCollider(self.carC, self.world.pusher)
        self.world.pusher.addCollider(self.carC, self.car, base.drive.node())

        #self.actor = self.car

    def getMyCar(self):
        return self.car  
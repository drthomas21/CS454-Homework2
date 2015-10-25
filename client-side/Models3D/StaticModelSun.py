from panda3d.core                       import *
from pandac.PandaModules                import *
from direct.actor.Actor                 import Actor
from Models3D.BaseModel3D               import BaseModel3D

class StaticModelSun(BaseModel3D):
    def __init__(self,World, render,base,loader):
        BaseModel3D.__init__(self,World, render,base,loader)
        self.isSunRotate = False

        #Load the Sun
        self.orbit_root_sun = render.attachNewNode('orbit_root_sun')
        self.sun = loader.loadModel("models/planet_sphere")
        self.sun_tex = loader.loadTexture("models/sun_1k_tex.jpg")
        self.sun.setTexture(self.sun_tex, 1)
        self.sun.reparentTo(self.orbit_root_sun)
        self.sun.reparentTo(render)
        self.sun.setPos(-30,20,1)
        self.sun.setScale(2 * 0.4)

        self.sunCNode = CollisionNode('sun')
        self.sunCNode.addSolid(CollisionSphere(0, 0, 5, 5))
        self.sunC = self.sun.attachNewNode(self.sunCNode)
        base.cTrav.addCollider(self.sunC, self.World.pusher)
        self.World.pusher.addCollider(self.sunC, self.sun, base.drive.node())

        self.day_period_sun = self.sun.hprInterval((60/365.0)*5, Vec3(360, 0, 0))

    def getSun(self):
        return self.sun

    def rotateSun(self, task):
        if self.getDistance()<10 and not self.isSunRotate:
            self.isSunRotate = True
            self.day_period_sun.loop()
        return Task.cont

    def stopRotateSun(self, task):
        if self.getDistance() > 10 and self.isSunRotate:
            self.isSunRotate = False
            self.day_period_sun.pause()
        return Task.cont

    def getDistance(self):
        distanceVector = self.World.ralph.getPos()-self.sun.getPos()
        return distanceVector.length()
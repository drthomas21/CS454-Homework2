# Roaming-Ralph was modified to remove collision part.

import direct.directbase.DirectStart
from direct.showbase.DirectObject               import DirectObject      
from direct.gui.OnscreenText                    import OnscreenText 
from direct.gui.DirectGui                       import *
from panda3d.core                               import *
from direct.actor.Actor                         import Actor
from direct.showbase.DirectObject               import DirectObject
from Models3D.Characters.PandaCharacter         import PandaCharacter
from Models3D.Characters.RalphCharacter         import RalphCharacter
from Models3D.Characters.VechileCharacter       import VechileCharacter
from Models3D.StaticModelEarth                  import StaticModelEarth
from Models3D.StaticModelSun                    import StaticModelSun
from Models3D.StaticModelVenus                  import StaticModelVenus
from Screen.AuthScreen                          import AuthScreen
from Screen.CharacterSelectScreen               import CharacterSelectScreen
from Network.ServerConnection                   import ServerConnection
import random, sys, os, math

SPEED = 0.5
# Function to put instructions on the screen.
def addInstructions(pos, msg):
    return OnscreenText(text=msg, style=1, fg=(1,1,1,1),
                        pos=(-1.3, pos), align=TextNode.ALeft, scale = .05)

# Function to put title on the screen.
def addTitle(text):
    return OnscreenText(text=text, style=1, fg=(1,1,1,1),
                        pos=(1.3,-0.95), align=TextNode.ARight, scale = .07)

class World(DirectObject):

    def __init__(self):
        base.disableMouse()
        base.setBackgroundColor(0,0,0)
        self.backgroundImage = OnscreenImage(parent=render2dp,image="assets/screens/renderpipeline03-full.jpg",scale=(4,1,1),pos=(0,-20,0))
        base.cam2dp.node().getDisplayRegion(0).setSort(-20)
        self.backgroundImage.posInterval(70,Point3(2, 0, 0),startPos=Point3(-2,0,0)).start()
        base.cTrav = CollisionTraverser()
        self.pusher = CollisionHandlerPusher()
        self.bypassServer = True
        self.ServerConnection = ServerConnection()
        
        if not self.bypassServer:            
            self.ServerConnection.connect("localhost",9252)
       
        
        self.doLoginScreen()
        
    def setPlayerCharacter(self,Character):
        self.Character = Character
        
    def doLoginScreen(self):
        self.login = AuthScreen(self,render,base)
        
    def doSelectionScreen(self):
        self.characterModels = []
        self.characterModels.append(["Ralph",RalphCharacter(self,render,base,loader)])
        self.characterModels.append(["Panda 1",PandaCharacter(self,render,base,loader)])
        self.characterModels.append(["Panda 2",PandaCharacter(self,render,base,loader)])
        
        self.select = CharacterSelectScreen(self,render,base,camera)
        
    def doGameScreen(self):
        self.backgroundImage.destroy()
        self.Character.setControls()
        
        self.title = addTitle("Panda3D Tutorial: Multiplayer (Walking on the Moon)")
        self.inst1 = addInstructions(0.95, "[ESC]: Quit")
        self.inst2 = addInstructions(0.90, "[a]: Rotate Player Left")
        self.inst3 = addInstructions(0.85, "[d]: Rotate Player Right")
        self.inst4 = addInstructions(0.80, "[w]: Move Player Forward")
        self.inst5 = addInstructions(0.75, "[s]: Move Player Backward")
        self.inst6 = addInstructions(0.70, "[shift+w]: Move Player Fast")
        self.inst7 = addInstructions(0.65, "[q]: Rotate Camera Left")
        self.inst8 = addInstructions(0.60, "[e]: Rotate Camera Right")
        
        # Set up the environment
        self.environ = loader.loadModel("models/square")
        self.environ.reparentTo(render)
        self.environ.setPos(0,0,0)
        self.environ.setScale(100,100,1)
        self.moon_tex = loader.loadTexture("models/moon_1k_tex.jpg")
        self.environ.setTexture(self.moon_tex, 1)
        
        self.staticRefSun = StaticModelSun(self)
        self.staticRefVenus = StaticModelVenus(self)
        self.staticRefEarth = StaticModelEarth(self)

        self.sun = self.staticRefSun.getSun()
        self.venus = self.staticRefVenus.getVenus()
        self.earth = self.staticRefEarth.getEarth()
        
        taskMgr.add(self.staticRefSun.rotateSun,"rotateSun")
        taskMgr.add(self.staticRefVenus.rotateVenus,"rotateVenus")
        taskMgr.add(self.staticRefEarth.rotateEarth,"rotateEarth")
        taskMgr.add(self.staticRefEarth.stopRotateEarth,"stopRotateEarth")
        taskMgr.add(self.staticRefSun.stopRotateSun,"stopRotateSun")
        taskMgr.add(self.staticRefVenus.stopRotateVenus,"stopRotateVenus")
        
        #Change Camera Position Later
        base.camera.setPos(self.Character.actor.getX(),self.Character.actor.getY()+10,2)

        # Create some lighting
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor(Vec4(.3, .3, .3, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(Vec3(-5, -5, -5))
        directionalLight.setColor(Vec4(1, 1, 1, 1))
        directionalLight.setSpecularColor(Vec4(1, 1, 1, 1))
        render.setLight(render.attachNewNode(ambientLight))
        render.setLight(render.attachNewNode(directionalLight))
        
w = World()
run()
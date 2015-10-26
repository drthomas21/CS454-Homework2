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
from Screen.ChatScreen                          import ChatScreen
from Network.ServerConnection                   import ServerConnection
from Network.models.EndSessionConnectionModel   import EndSessionConnectionModel
from Network.models.HeartbeatConnectionModel import HeartbeatConnectionModel
import random, sys, os, math, json

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
        floorNode = render.attachNewNode("Floor NodePath")
        # Create a collision plane solid.
        collPlane = CollisionPlane(Plane(Vec3(0, 0, 1), Point3(0, 0, 0)))
        # Call our function that creates a nodepath with a collision node

        floorCollisionNP = self.makeCollisionNodePath(floorNode, collPlane)
        
        self.bypassServer = True
        self.jumpTo = 1
        self.ServerConnection = ServerConnection()
        if not self.bypassServer:
            with open('config.json') as data_file:    
                config = json.load(data_file)
            print config
            self.ServerConnection.connect(config['host'],config['port'])
       
        
        if self.jumpTo == 1:
            self.doAuthScreen()
        elif self.jumpTo == 2:
            self.doSelectionScreen()
        elif self.jumpTo == 3:
            self.setPlayerCharacter(RalphCharacter(self,render,base,loader))
            self.doGameScreen()
        else:
            self.doAuthScreen()
        
    def setPlayerCharacter(self,Character):
        self.Character = Character
        
    def doAuthScreen(self):
        self.authScreen = AuthScreen(self,render,base)
        
    def doSelectionScreen(self):
        self.characterModels = []
        self.characterModels.append(["Ralph",RalphCharacter(self,render,base,loader)])
        self.characterModels.append(["Panda",PandaCharacter(self,render,base,loader)])
        self.characterModels.append(["Motocycle",PandaCharacter(self,render,base,loader)])
        
        self.selectScreen = CharacterSelectScreen(self,render,base,camera)
    
    def doGameScreen(self):
        self.heartbeatConnection = HeartbeatConnectionModel()
        self.ServerConnection.setupConnectionModel(self.heartbeatConnection)
        
        self.backgroundImage.destroy()
        self.Character.setControls()
        self.Character.actor.setHpr(0,0,0)
        taskMgr.add(self.Character.move,"moveTask")
        
        self.title = addTitle("Panda3D Tutorial: Multiplayer (Walking on the Moon)")
        self.inst = []
        self.inst.append(addInstructions(0.95, "[ESC]: Quit/Close Chat Window"))
        self.inst.append(addInstructions(0.90, "[a]: Rotate Player Left"))
        self.inst.append(addInstructions(0.85, "[d]: Rotate Player Right"))
        self.inst.append(addInstructions(0.80, "[w]: Move Player Forward"))
        self.inst.append(addInstructions(0.75, "[s]: Move Player Backward"))
        self.inst.append(addInstructions(0.70, "[shift+w]: Move Player Fast"))
        self.inst.append(addInstructions(0.65, "[q]: Rotate Camera Left"))
        self.inst.append(addInstructions(0.60, "[e]: Rotate Camera Right"))
        self.inst.append(addInstructions(0.55, "[t]: Display Chat Window"))   
        
        # Set up the environment
        self.environ = loader.loadModel("models/square")
        self.environ.reparentTo(render)
        self.environ.setPos(0,0,0)
        self.environ.setScale(100,100,1)
        self.moon_tex = loader.loadTexture("models/moon_1k_tex.jpg")
        self.environ.setTexture(self.moon_tex, 1)
        
        self.staticRefSun = StaticModelSun(self,render,base,loader)
        self.staticRefVenus = StaticModelVenus(self,render,base,loader)
        self.staticRefEarth = StaticModelEarth(self,render,base,loader)

        self.sun = self.staticRefSun.getSun()
        self.venus = self.staticRefVenus.getVenus()
        self.earth = self.staticRefEarth.getEarth()
        
        taskMgr.add(self.staticRefSun.rotateSun,"rotateSun")
        taskMgr.add(self.staticRefVenus.rotateVenus,"rotateVenus")
        taskMgr.add(self.staticRefEarth.rotateEarth,"rotateEarth")
        taskMgr.add(self.staticRefEarth.stopRotateEarth,"stopRotateEarth")
        taskMgr.add(self.staticRefSun.stopRotateSun,"stopRotateSun")
        taskMgr.add(self.staticRefVenus.stopRotateVenus,"stopRotateVenus")
        taskMgr.doMethodLater(1,self.doHeartbeat,"heartbeat")
        
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
        
        self.chatScreen = ChatScreen(self,render,base)
        self.chatScreen.hideScreen()
        
    def doHeartbeat(self,task):
        self.heartbeatConnection.sendHeartbeat()
        return task.again
    
    def makeCollisionNodePath(self, nodepath, solid):
        '''
        Creates a collision node and attaches the collision solid to the
        supplied NodePath. Returns the nodepath of the collision node.
        '''
        # Creates a collision node named after the name of the NodePath.
        collNode = CollisionNode("%s c_node" % nodepath.getName())
        collNode.addSolid(solid)
        collisionNodepath = nodepath.attachNewNode(collNode)
        return collisionNodepath
    
    def endSession(self):
        self.endSession = EndSessionConnectionModel(self.exit)
        self.ServerConnection.setupConnectionModel(self.endSession)
        self.endSession.sendMessage(self.Character.actor.getPos())
        
        #Forces an exit
        taskMgr.doMethodLater(3,self.exit,"forceExit")
        
    def exit(self,data):
        if data != 1:
            print "Houston, we got a problem"
        sys.exit()
        
w = World()
run()
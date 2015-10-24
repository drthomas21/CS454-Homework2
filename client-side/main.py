# Roaming-Ralph was modified to remove collision part.

import direct.directbase.DirectStart
from direct.showbase.DirectObject import DirectObject      
from direct.gui.OnscreenText import OnscreenText 
from direct.gui.DirectGui import *
from panda3d.core import *
from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject
from Models3D.Characters.PandaCharacter import PandaCharacter
from Models3D.Characters.RalphCharacter import RalphCharacter
from Models3D.Characters.VechileCharacter import VechileCharacter
from Models3D.StaticModelEarth import StaticModelEarth
from Models3D.StaticModelSun import StaticModelSun
from Models3D.StaticModelVenus import StaticModelVenus
from Screen.AuthScreen import AuthScreen
from Screen.CharacterSelectScreen import CharacterSelectScreen
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
        base.setBackgroundColor(1,1,1)
        World.backgroundImage = OnscreenImage(image="assets/screens/renderpipeline03-full.jpg",scale=(4,1,1))
        World.backgroundImage.posInterval(70,Point3(2, 0, 0),startPos=Point3(-2,0,0)).start()
        self.login = AuthScreen(self,render,base)
        
    def selectCharacter(self):
        self.select = CharacterSelectScreen(self,render,base)
        
    def loadGame(self):
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
        
w = World()
run()
# Roaming-Ralph was modified to remove collision part.

import direct.directbase.DirectStart
from direct.showbase.DirectObject   import DirectObject      
from direct.gui.OnscreenText        import OnscreenText 
from direct.gui.DirectGui           import *
from panda3d.core                   import *
from direct.actor.Actor             import Actor
from direct.showbase.DirectObject   import DirectObject
from Characters.RalphCharacter      import RalphCharacter
from Characters.PandaCharacter      import PandaCharacter
from Screen.AuthScreen              import AuthScreen
from Screen.CharacterSelectScreen   import CharacterSelectScreen
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
        self.login = AuthScreen(self,render,base)
        self.selectCharacter()
        
    def selectCharacter(self):
        self.characterModels = []
        self.characterModels.append(["Ralph",RalphCharacter(self,render)])
        self.characterModels.append(["Panda 1",PandaCharacter(self,render)])
        self.characterModels.append(["Panda 2",PandaCharacter(self,render)])
        
        self.select = CharacterSelectScreen(self,render,base,camera)
        
w = World()
run()
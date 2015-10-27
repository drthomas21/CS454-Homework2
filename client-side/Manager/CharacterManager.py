from Models3D.Characters.PandaCharacter import PandaCharacter
from Models3D.Characters.RalphCharacter import RalphCharacter
from Models3D.Characters.VechileCharacter import VechileCharacter

class CharacterManager:
    characters = []
    
    def __init__(self, World, render, base,loader):
        self.World = World
        self.render = render
        self.base = base
        self.loader = loader
    
    def createCharacter(self,username="", modelName="", pos=(0.0,0.0,0.0), hpr=(0.0,0.0,0.0)):
        model = None
        if modelName == "panda1":
            model = PandaCharacter(World=self.World,render=self.render,base=self.base,loader=self.loader)
        elif modelName == "ralph1":
            model = RalphCharacter(World=self.World,render=self.render,base=self.base,loader=self.loader)
        elif model == "vehicle1":
            model = VechileCharacter(World=self.World,render=self.render,base=self.base,loader=self.loader)
        else:
            model = RalphCharacter(World=self.World,render=self.render,base=self.base,loader=self.loader)
        model.actor.setPos(float(pos[0]),float(pos[1]),float(pos[2]))
        model.actor.setHpr(float(hpr[0]),float(hpr[1]),float(hpr[2]))
        model.username = username
        
        self.characters.append(model)
        #self.World.
        return model
    
    def moveCharacter(self, username, time, pos):
        print "Move:",username,pos
        pos = pos.split(',')
        model = self.getModel(username)
        if model == None:
            #model = self.createCharacter(username,"",pos)
            return False
        
        model.moveCharacterTo(pos)
    
    def getModel(self,username):
        for model in self.characters:
            print model.username,username
            if(model.username == username):
                return model
        return None
            
    def getCharacters(self):
        list = []
        for model in self.characters:
            list.append(model)
            
        return list
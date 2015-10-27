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
    
    def createCharacter(self,username="", modelName="", pos=(0,0,0), hpr=(0,0,0)):
        model = None
        if modelName == "PandaCharacter":
            model = PandaCharacter(World=self.World,render=self.render,base=self.base,loader=self.loader)
        elif modelName == "RalphCharacter":
            model = RalphCharacter(World=self.World,render=self.render,base=self.base,loader=self.loader)
        elif model == "VechileCharacter":
            model = VechileCharacter(World=self.World,render=self.render,base=self.base,loader=self.loader)
        else:
            model = RalphCharacter(World=self.World,render=self.render,base=self.base,loader=self.loader)
        model.actor.setPos(pos[0],pos[1],pos[2])
        model.actor.setHpr(hpr[0],hpr[1],hpr[2])
        model.username = username
        
        self.characters.append(model)
    
    def moveCharacter(self, username, time, pos):
        pos = pos.split(',')
        if not self.characters[username]:
            self.createCharacter(username,"",pos)
        model = self.getMode(username)
        if model != None:
            self.characters[username].setPos(pos[0],pos[1],pos[2])
    
    def getModel(self,username):
        for model in self.characters:
            if(model.username == username):
                return model
        return None
            
    def getCharacters(self):
        list = []
        for model in self.characters:
            list.append(model)
            
        return list
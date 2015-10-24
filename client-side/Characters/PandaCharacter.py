from BaseCharacter import BaseCharacter
from direct.actor.Actor import Actor

class PandaCharacter(BaseCharacter):
    def __init__(self,World, render):
        BaseCharacter.__init__(self,World, render)
        self.Character = Actor("models/panda-model", {"walk": "models/panda-walk4"})
        self.Character.reparentTo(render)
        self.Character.setScale(.003)
        self.Character.setPos(0,0,0)
        
    def lookAt(self,model):
        self.Character.lookAt(model)
        self.Character.setHpr(180,0,0)  
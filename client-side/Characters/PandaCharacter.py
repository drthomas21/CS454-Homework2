from BaseCharacter import BaseCharacter
from direct.actor.Actor import Actor

class PandaCharacter(BaseCharacter):
    def __init__(self,World, render):
        BaseCharacter.__init__(self,World, render)
        self.Character = Actor("models/panda-model", {"walk": "models/panda-walk4"})
        self.Character.reparentTo(render)
        self.Character.setScale(.2)
        self.Character.setPos(0,0,0)        
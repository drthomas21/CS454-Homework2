from BaseCharacter import BaseCharacter
from direct.actor.Actor import Actor

class RalphCharacter(BaseCharacter):
    def __init__(self,World, render):
        BaseCharacter.__init__(self,World, render)
        self.Character = Actor("models/ralph/ralph", {"run":"models/ralph/ralph-run","walk":"models/ralph/ralph-walk"})
        self.Character.reparentTo(render)
        self.Character.setScale(.2)
        self.Character.setPos(0,0,0)        
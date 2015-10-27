from Models3D.Characters.PandaCharacter import PandaCharacter
from Models3D.Characters.RalphCharacter import RalphCharacter
from Models3D.Characters.VechileCharacter import VechileCharacter
from Network.models.PositionConnectionModel import PositionConnectionModel

class MoveManager:
    def __init__(self, World):
        self.Player = World.Character
        self.World = World
        self.PositionConnectionModel = PositionConnectionModel(World.CharacterManager.moveCharacter)
        World.ServerConnection.setupConnectionModel(self.PositionConnectionModel)
        self.actions = []
    
    def appendAction(self,left,right,forward,pos):
        if len(self.actions) == 0 or (len(self.actions) > 0 and self.actions[len(self.actions)-1][3] != pos):
            self.actions.append([left,right,forward,pos])
        
    def flushActions(self):
        actions = self.actions
        self.actions = []
        return actions
    
    def sendMoves(self,task):
        if self.World.stopSendingMovement:
            return None
        
        if not self.World.bypassServer:
            for moves in self.flushActions():
                pos = moves[3]
                self.PositionConnectionModel.sendPos(str(pos[0])+","+str(pos[1])+","+str(pos[2]))
        else:
            self.flushActions()
        return task.again
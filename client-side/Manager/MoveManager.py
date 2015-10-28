from Models3D.Characters.PandaCharacter     import PandaCharacter
from Models3D.Characters.RalphCharacter     import RalphCharacter
from Models3D.Characters.VehicleCharacter   import VehicleCharacter
from Network.models.PositionConnectionModel import PositionConnectionModel

class MoveManager:
    def __init__(self, World):
        self.Player = World.Character
        self.World = World
        self.PositionConnectionModel = PositionConnectionModel(World.CharacterManager.moveCharacter)
        World.ServerConnection.setupConnectionModel(self.PositionConnectionModel)
        self.actions = []
        self.lastAction = []
    
    def appendAction(self,left,right,forward,pos):
        if len(self.lastAction) == 0 or (len(self.lastAction) > 0 and self.lastAction[3] != pos):
            self.actions.append([left,right,forward,pos])
            self.lastAction = [left,right,forward,pos]
        
    def flushActions(self):
        actions = self.actions
        self.actions = []
        return actions
    
    def sendMoves(self,task):
        if self.World.stopSendingMovement:
            return None
        
        if not self.World.bypassServer:
            if len(self.actions) > 0:
                for moves in self.flushActions():
                    pos = moves[3]
                    self.PositionConnectionModel.sendPos(str(pos[0])+","+str(pos[1])+","+str(pos[2]))
        else:
            self.flushActions()
        return task.again
    
    def sendUpdatePosition(self):
        pos = self.Player.actor.getPos()
        self.PositionConnectionModel.sendPos(str(pos[0])+","+str(pos[1])+","+str(pos[2]))
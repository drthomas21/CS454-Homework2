from Network.ServerConnection import ServerConnection
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator
from panda3d.core import NetDatagram

class PositionConnectionModel(ServerConnection):
    CODE_SEND_POS = 105
    CODE_RECV_POS = 205
    
    def __init__(self,screenModel):
        self.screenModel = screenModel
        
    def getConnectionActions(self):
        return [[self.CODE_RECV_POS, self.getPosMessage]];
    
    def sendPos(self,message):
        request = self.buildRequestPackage(self.CODE_SEND_POS)
        ServerConnection.sendMessage(self,request)
        
    def getPosMessage(self,data):
        self.screenModel.parseResponse()
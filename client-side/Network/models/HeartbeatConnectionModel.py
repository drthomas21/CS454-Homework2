from Network.ServerConnection import ServerConnection
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator
from panda3d.core import NetDatagram

class HeartbeatConnectionModel(ServerConnection):
    CODE_SEND_MSG = 113
    CODE_RECV_MSG = 213
    
    def __init__(self,screenModel):
        self.screenModel = screenModel
        
    def getConnectionActions(self):
        return [[self.CODE_RECV_MSG, self.getHeartbeat]];
    
    def sendHeartbeat(self,message):
        request = self.buildRequestPackage(self.CODE_SEND_MSG)
        self.sendMessage(request)
        
    def getHeartbeat(self,data):
        self.screenModel.parseResponse()
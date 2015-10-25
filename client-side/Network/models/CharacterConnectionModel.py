from Network.ServerConnection import ServerConnection
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator
from panda3d.core import NetDatagram

class CharacterConnectionModel(ServerConnection):
    CODE_SEND_MSG = 104
    #CODE_RECV_MSG = 104
    
    def __init__(self,screenModel):
        self.screenModel = screenModel
        
    def getConnectionActions(self):
        return [];
    
    def sendCharacter(self,message):
        request = self.buildRequestPackage(self.CODE_SEND_MSG)
        request.addString(message)
        self.sendMessage(request)
        
    def getMessage(self,data):
        self.screenModel.parseResponse(data.getString())
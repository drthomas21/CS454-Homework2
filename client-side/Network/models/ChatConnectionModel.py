from Network.ServerConnection import ServerConnection
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator
from panda3d.core import NetDatagram

class ChatConnectionModel(ServerConnection):
    CODE_SEND_MSG = 112
    CODE_RECV_MSG = 212
    
    def __init__(self,screenModel):
        self.screenModel = screenModel
        
    def getConnectionActions(self):
        return [[self.CODE_RECV_MSG, self.getChatMessage]];
    
    def sendChatMessage(self,message):
        request = self.buildRequestPackage(self.CODE_SEND_MSG)
        request.addString(message)
        ServerConnection.sendMessage(self,request)
        
    def getChatMessage(self,data):
        self.screenModel.parseResponse(data.getString())
from Network.ServerConnection import ServerConnection
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator
from panda3d.core import NetDatagram

class AuthConnectionModel(ServerConnection):
    CODE_SEND_MSG = 112
    CODE_RECV_MSG = 212
    
    def __init(self):
        self.registerResponseAction(self.CODE_RECV_MSG, self.getChatMessage)
    
    def sendChatMessage(self,message):
        request = self.buildRequestPackage(self.CODE_SEND_MSG)
        request.addString(message)
        self.sendMessage(request)
        
    def getChatMessage(self,data):
        msg = data.getString()
from Network.ServerConnection import ServerConnection
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator
from panda3d.core import NetDatagram

class HeartbeatConnectionModel(ServerConnection):
    CODE_RECV_MSG = 207
    
    def __init__(self,callback):
        self.callback = callback
        
    def getConnectionActions(self):
        return [[self.CODE_RECV_MSG, self.getMessage]];
    
    def sendHeartbeat(self):
        request = self.buildRequestPackage(self.CODE_SEND_MSG)
        ServerConnection.sendMessage(self,request)
        
    def getMessage(self,data):
        print data
        self.callback(data.getString())
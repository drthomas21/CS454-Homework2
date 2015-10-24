from Network.ServerConnection import ServerConnection
from direct.distributed.PyDatagram import PyDatagram

class AuthConnectionModel(ServerConnection):
    CODE_AUTH=101
    CODE_REG = 102
    
    def __init__(self):
        self.registerResponseAction(self.CODE_REG, self.getReg)
        self.registerResponseAction(self.CODE_AUTH, self.getAuth)
    
    def sendLoginRequest(self,username,password):
        request = self.buildRequestPackage(self.CODE_AUTH)
        request.addString(username)
        request.addString(password)
        self.sendMessage(request)
        
    def sendRegisterRequest(self,username,password):
        request = self.buildRequestPackage(self.CODE_REG)
        request.addString(username)
        request.addString(password)
        self.sendMessage(request)
    
    def getAuth(self, data):
        msg = data.getString()

    def getReg(self, data):
        msg = data.getString()
        
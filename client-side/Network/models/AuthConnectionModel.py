from Network.ServerConnection import ServerConnection
from direct.distributed.PyDatagram import PyDatagram

class AuthConnectionModel(ServerConnection):
    CODE_SEND_AUTH=101
    CODE_SUCCESS_AUTH=201
    CODE_FAILED_AUTH=301
    
    CODE_SEND_REG =103
    CODE_SUCCESS_REG=203
    CODE_FAILED_REG=303
    
    def __init__(self):
        self.registerResponseAction(self.CODE_SEND_AUTH, self.getReg)
        self.registerResponseAction(self.CODE_SEND_REG, self.getAuth)
    
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
        
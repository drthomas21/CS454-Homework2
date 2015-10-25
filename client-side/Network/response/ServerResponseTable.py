from common.Constants import Constants

from Network.response.ResponseLogin import ResponseLogin
from Network.response.ResponseDisconnect import ResponseDisconnect
from Network.response.ResponseRegister import ResponseRegister
from Network.response.ResponseCreateCharacter import ResponseCreateCharacter
from Network.response.ResponseChat import ResponseChat
from Network.response.ResponseMove import ResponseMove
from Network.response.ResponseHeartBeat import ResponseHeartBeat


class ServerResponseTable:

    responseTable = {}

    def __init__(self):
        """Initialize the response table."""
        self.add(Constants.SMSG_AUTH, 'ResponseLogin')
        self.add(Constants.SMSG_DISCONNECT, 'ResponseDisconnect')
        self.add(Constants.SMSG_REGISTER, 'ResponseRegister')
        self.add(Constants.SMSG_CREATE_CHARACTER, 'ResponseCreateCharacter')
        self.add(Constants.CMSG_CHAT, 'ResponseChat')
        self.add(Constants.SMSG_MOVE,'ResponseMove')
        #self.add(Constants.RES_HEARTBEAT,'ResponseHeartBeat')

    def add(self, constant, name):
        """Map a numeric response code with the name of an existing response module."""
        if name in globals():
            self.responseTable[constant] = name
        else:
            print 'Add Response Error: No module named ' + str(name)

    def get(self, responseCode):
        """Retrieve an instance of the corresponding response."""
        serverResponse = None

        if responseCode in self.responseTable:
            serverResponse = globals()[self.responseTable[responseCode]]()
        else:
            print 'Bad Response Code: ' + str(responseCode)

        return serverResponse

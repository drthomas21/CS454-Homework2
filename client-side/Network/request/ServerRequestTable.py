from common.Constants import Constants

from Network.request.RequestLogin import RequestLogin
from Network.request.RequestDisconnect import RequestDisconnect
from Network.request.RequestRegister import RequestRegister
from Network.request.RequestCreateCharacter import RequestCreateCharacter
from Network.request.RequestChat import RequestChat
from Network.request.RequestMove import RequestMove
from Network.request.RequestHeartBeat import RequestHeartBeat

class ServerRequestTable:
    """
    The ServerRequestTable contains a mapping of all requests for use
    with the networking component.
    """
    requestTable = {}

    def __init__(self):
        """Initialize the request table."""
        self.add(Constants.CMSG_AUTH, 'RequestLogin')
        self.add(Constants.CMSG_DISCONNECT, 'RequestDisconnect')
        self.add(Constants.CMSG_REGISTER, 'RequestRegister')
        self.add(Constants.CMSG_CREATE_CHARACTER, 'RequestCreateCharacter')
        self.add(Constants.CMSG_CHAT, 'RequestChat')
        self.add(Constants.CMSG_MOVE,'RequestMove')
        self.add(Constants.REQ_HEARTBEAT,'RequestHeartBeat')

    def add(self, constant, name):
        """Map a numeric request code with the name of an existing request module."""
        if name in globals():
            self.requestTable[constant] = name
        else:
            print 'Add Request Error: No module named ' + str(name)

    def get(self, requestCode):
        """Retrieve an instance of the corresponding request."""
        serverRequest = None

        if requestCode in self.requestTable:
            serverRequest = globals()[self.requestTable[requestCode]]()
        else:
            print 'Bad Request Code: ' + str(requestCode)

        return serverRequest

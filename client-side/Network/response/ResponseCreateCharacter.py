from traceback import print_exc

from common.Constants import Constants
from Network.response.ServerResponse import ServerResponse

class ResponseCreateCharacter(ServerResponse):

    def execute(self, data):

        try:
            self.msg = data.getString()
            print "ResponseCreateCharacter - ", self.msg

        except:
            self.log('Bad [' + str(Constants.SMSG_CREATE_CHARACTER) + '] String Response')
            print_exc()

from traceback import print_exc

from common.Constants import Constants
from Network.response.ServerResponse import ServerResponse

class ResponseDisconnect(ServerResponse):

    def execute(self, data):

        try:
            self.msg = data.getString()
            print "ResponseDisconnect - ", self.msg

        except:
            self.log('Bad [' + str(Constants.SMSG_DISCONNECT) + '] String Response')
            print_exc()

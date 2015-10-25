from traceback import print_exc

from common.Constants import Constants
from Network.response.ServerResponse import ServerResponse

class ResponseRegister(ServerResponse):

    def execute(self, data):
        try:
            self.msg = data.getString()
            print "ResponseRegister - ", self.msg

        except:
            self.log('Bad [' + str(Constants.SMSG_REGISTER) + '] String Response')
            print_exc()

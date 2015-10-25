from traceback import print_exc

from common.Constants import Constants
from Network.response.ServerResponse import ServerResponse

class ResponseMove(ServerResponse):

    def execute(self, data):

        try:
            self.msg = data.getString()
            print "ResponseMove - ", self.msg

        except:
            self.log('Bad [' + str(Constants.SMSG_MOVE) + '] String Response')
            print_exc()

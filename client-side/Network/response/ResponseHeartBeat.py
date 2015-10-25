from traceback import print_exc

from common.Constants import Constants
from Network.response.ServerResponse import ServerResponse

class ResponseHeartBeat(ServerResponse):

    def execute(self, data):

        try:
            self.msg = data.getString()

            print "ResponseHeartBeat - ", self.msg

            #self.log('Received [' + str(Constants.RAND_STRING) + '] String Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_AUTH) + '] String Response')
            print_exc()

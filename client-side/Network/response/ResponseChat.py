from traceback import print_exc

from common.Constants import Constants
from Network.response.ServerResponse import ServerResponse

class ResponseChat(ServerResponse):

    def execute(self, data):

        try:
            self.msg = data.getString()
            print "ResponseChat - ", self.msg

        except:
            self.log('Bad [' + str(Constants.SMSG_CHAT) + '] String Response')
            print_exc()

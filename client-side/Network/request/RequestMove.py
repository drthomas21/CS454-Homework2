from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from Network.request.ServerRequest import ServerRequest

class RequestMove(ServerRequest):


    def send(self, username = None):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_MOVE)
            pkg.addString(username)
            pkg.addString(userLocation)
            self.cWriter.send(pkg, self.connection)

        except:
            self.log('Bad [' + str(Constants.CMSG_MOVE) + '] Request')
            print_exc()

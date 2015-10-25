from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from Network.request.ServerRequest import ServerRequest

class RequestDisconnect(ServerRequest):

    def send(self, username = None):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_DISCONNECT)
            pkg.addString(username)
            pkg.addString(charactername)
            pkg.addString(lastPos)

            self.cWriter.send(pkg, self.connection)
        except:
            self.log('Bad [' + str(Constants.CMSG_DISCONNECT) + '] Request')
            print_exc()

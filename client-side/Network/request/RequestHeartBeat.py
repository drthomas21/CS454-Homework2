from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestHeartBeat(ServerRequest):

    def send(self, username = None):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.REQ_HEARTBEAT)
            pkg.addString(username)
            self.cWriter.send(pkg, self.connection)

        except:
            self.log('Bad [' + str(Constants.REQ_HEARTBEAT) + '] Request')
            print_exc()
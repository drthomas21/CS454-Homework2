from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from Network.request.ServerRequest import ServerRequest

class RequestCreateCharacter(ServerRequest):


    def send(self, username = None):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_CREATE_CHARACTER)
            pkg.addString(username)
            pkg.addString(faction)
            pkg.addString(charactername)
            

            self.cWriter.send(pkg, self.connection)

            #self.log('Sent [' + str(Constants.RAND_STRING) + '] Int Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_CREATE_CHARACTER) + '] Int Request')
            print_exc()

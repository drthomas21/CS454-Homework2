from direct.showbase.DirectObject       import DirectObject      
from direct.gui.OnscreenText            import OnscreenText 
from direct.gui.DirectGui               import *
from panda3d.core                       import *
from Network.models.AuthConnectionModel  import AuthConnectionModel

class NotificationScreen:
    def __init__(self,World,render,base):
        self.World = World;
        self.authConnection = AuthConnectionModel(self)
        self.World.ServerConnection.setupConnectionModel(self.authConnection)
        
        boxloc = Vec3(0.0, 0.0, 0.0)
        p = boxloc
        self.LoginFrame = DirectFrame(frameColor=(0,0,0,0.4),frameSize=(-0.5,0.41,-0.25,0.1),pos=p)
        
    def updateStatus(self, statustext):
        self.LoginFrame.statusText.setText(statustext)
        
    def unloadScreen(self):
        self.LoginFrame.destroy()
        
    def attemptRegister(self):
        self.whichAction = 1      
        if(self.LoginFrame.usernameBox.get() == ""):
            if(self.LoginFrame.passwordBox.get() == ""):
                self.updateStatus("ERROR: You must enter a username and password before logging in.")
            else:
                self.updateStatus("ERROR: You must specify a username")
            self.LoginFrame.passwordBox['focus'] = 0
            self.LoginFrame.usernameBox['focus'] = 1
                
        elif(self.LoginFrame.passwordBox.get() == ""):
            self.updateStatus("ERROR: You must enter a password")
            self.LoginFrame.usernameBox['focus'] = 0
            self.LoginFrame.passwordBox['focus'] = 1
            
        else:
            self.updateStatus("Attempting to Signup...")
            self.LoginFrame.registerButton = DGG.DISABLED
            self.LoginFrame.loginButton = DGG.DISABLED
            if not self.World.bypassServer:
                self.authConnection.sendRegisterRequest(self.LoginFrame.usernameBox.get(),self.LoginFrame.passwordBox.get())
            else:
                self.parseResponse(0)
            
        
    def attemptLogin(self):  
        self.whichAction = 2     
        if(self.LoginFrame.usernameBox.get() == ""):
            if(self.LoginFrame.passwordBox.get() == ""):
                self.updateStatus("ERROR: You must enter a username and password before logging in.")
            else:
                self.updateStatus("ERROR: You must specify a username")
            self.LoginFrame.passwordBox['focus'] = 0
            self.LoginFrame.usernameBox['focus'] = 1
                
        elif(self.LoginFrame.passwordBox.get() == ""):
            self.updateStatus("ERROR: You must enter a password")
            self.LoginFrame.usernameBox['focus'] = 0
            self.LoginFrame.passwordBox['focus'] = 1
            
        else:
            self.updateStatus("Attempting to login...")
            self.LoginFrame.registerButton = DGG.DISABLED
            self.LoginFrame.loginButton = DGG.DISABLED
            if self.LoginFrame.usernameBox.get() == "test" and self.LoginFrame.passwordBox.get() == "test":
                self.parseResponse(1)
            elif not self.World.bypassServer:
                self.authConnection.sendLoginRequest(self.LoginFrame.usernameBox.get(),self.LoginFrame.passwordBox.get())
            else:
                self.parseResponse(1)
            
    def parseResponse(self,data):
        print data
        if data != 0:
            self.unloadScreen()
            self.World.doSelectionScreen()
        else: 
            if self.whichAction == 1:
                self.updateStatus("Unable to register with that username")
            else:
                self.updateStatus("Invalid username/password")
            self.whichAction = 0
from direct.showbase.DirectObject       import DirectObject      
from direct.gui.OnscreenText            import OnscreenText 
from direct.gui.DirectGui               import *
from panda3d.core                       import *
from Network.models.AuthConnectionModel  import AuthConnectionModel

class AuthScreen:
    def __init__(self,World,render,base):
        self.World = World;
        self.authConnection = AuthConnectionModel(self)
        self.World.ServerConnection.setupConnectionModel(self.authConnection)
        
        boxloc = Vec3(0.0, 0.0, 0.0)
        p = boxloc
        World.LoginFrame = DirectFrame(frameColor=(0,0,0,0.4),frameSize=(-0.5,0.41,-0.25,0.1),pos=p)       

        p = boxloc + Vec3(-0.5, 0, 0.0)                                 
        World.LoginFrame.textObject = OnscreenText(parent=World.LoginFrame, text = "Username:", pos = p, scale = 0.07,fg=(1, 1, 1, 1),align=TextNode.ALeft)
        
        p = boxloc + Vec3(-0.1, 0.0, 0.0)
        World.LoginFrame.usernameBox = DirectEntry(parent=World.LoginFrame, text = "" , pos = p, scale=.05, initialText="", numLines = 1)
        
        p = boxloc + Vec3(-0.5, -0.1, 0.0)        
        World.LoginFrame.textObject = OnscreenText(parent=World.LoginFrame, text = "Password:", pos = p, scale = 0.07,fg=(1, 1, 1, 1),align=TextNode.ALeft)
        
        p = boxloc + Vec3(-0.1, 0, -0.1)
        World.LoginFrame.passwordBox = DirectEntry(parent=World.LoginFrame, text = "" , pos = p, scale=.05, initialText="", numLines = 1, obscured = 1)
        
        p = boxloc + Vec3(-0.2, 0, -0.2)
        World.LoginFrame.loginButton = DirectButton(parent=World.LoginFrame, text = ("Login", "Login", "Login", "Login"), pos = p, scale = 0.075, command=self.attemptLogin)
        
        p = boxloc + Vec3(0.2, 0, -0.2)
        World.LoginFrame.registerButton = DirectButton(parent=World.LoginFrame, text = ("Signup", "Signup", "Signup", "Signup"), pos = p, scale = 0.075, command=self.attemptRegister)
        
        p = boxloc + Vec3(0, -0.4, 0)
        World.LoginFrame.statusText = OnscreenText(parent=World.LoginFrame, text = "", pos = p, scale = 0.075, fg = (1, 0, 0, 1), align=TextNode.ACenter)

        
    def updateStatus(self, statustext):
        self.World.LoginFrame.statusText.setText(statustext)
        
    def unloadScreen(self):
        self.World.LoginFrame.destroy()
        
    def attemptRegister(self):
        self.whichAction = 1      
        if(self.World.LoginFrame.usernameBox.get() == ""):
            if(self.World.LoginFrame.passwordBox.get() == ""):
                self.updateStatus("ERROR: You must enter a username and password before logging in.")
            else:
                self.updateStatus("ERROR: You must specify a username")
            self.World.LoginFrame.passwordBox['focus'] = 0
            self.World.LoginFrame.usernameBox['focus'] = 1
                
        elif(self.World.LoginFrame.passwordBox.get() == ""):
            self.updateStatus("ERROR: You must enter a password")
            self.World.LoginFrame.usernameBox['focus'] = 0
            self.World.LoginFrame.passwordBox['focus'] = 1
            
        else:
            self.updateStatus("Attempting to Signup...")
            self.World.LoginFrame.registerButton = DGG.DISABLED
            self.World.LoginFrame.loginButton = DGG.DISABLED
            if not self.World.bypassServer:
                self.authConnection.sendRegisterRequest(self.World.LoginFrame.usernameBox.get(),self.World.LoginFrame.passwordBox.get())
            else:
                self.parseResponse(0)
            
        
    def attemptLogin(self):  
        self.whichAction = 2     
        if(self.World.LoginFrame.usernameBox.get() == ""):
            if(self.World.LoginFrame.passwordBox.get() == ""):
                self.updateStatus("ERROR: You must enter a username and password before logging in.")
            else:
                self.updateStatus("ERROR: You must specify a username")
            self.World.LoginFrame.passwordBox['focus'] = 0
            self.World.LoginFrame.usernameBox['focus'] = 1
                
        elif(self.World.LoginFrame.passwordBox.get() == ""):
            self.updateStatus("ERROR: You must enter a password")
            self.World.LoginFrame.usernameBox['focus'] = 0
            self.World.LoginFrame.passwordBox['focus'] = 1
            
        else:
            self.updateStatus("Attempting to login...")
            self.World.LoginFrame.registerButton = DGG.DISABLED
            self.World.LoginFrame.loginButton = DGG.DISABLED            
            if not self.World.bypassServer:
                self.authConnection.sendLoginRequest(self.World.LoginFrame.usernameBox.get(),self.World.LoginFrame.passwordBox.get())
            else:
                self.parseResponse(0)
            
    def parseResponse(self,data):
        if data == 0:
            self.unloadScreen()
            self.World.doSelectionScreen()
        else: 
            if self.whichAction == 1:
                self.updateStatus("Unable to register with that username")
            else:
                self.updateStatus("Invalid username/password")
            self.updateStatus = 0
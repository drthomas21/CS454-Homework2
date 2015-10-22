from direct.showbase.DirectObject       import DirectObject      
from direct.gui.OnscreenText            import OnscreenText 
from direct.gui.DirectGui               import *
from panda3d.core                       import *

class MainScreen:
    def __init__(self,World,render,base):
        self.World = World;
        base.setBackgroundColor(0,0,0)
        GameTitleFrame = DirectFrame(frameColor=(0,0,0,1),frameSize=(-1,1,-1,1),pos=(-0.5,0,0.5))
        
        # creates a basic login screen that asks for a username/password
        
        boxloc = Vec3(0.0, 0.0, 0.0)
        # all items in the login form will have a position relative to this
        # this makes it easier to shift the entire form around once we have 
        # some graphics to display with it without having to change the 
        # positioning of every form element
        
        # p is the position of the form element relative to the boxloc 
        # coordinates set above it is changed for every form element
        p = boxloc + Vec3(-0.5, 0, 0.0)                                 
        World.textObject = OnscreenText(text = "Username:", pos = p, scale = 0.07,fg=(1, 1, 1, 1),align=TextNode.ALeft)
        # "Username: " text that appears beside the username box
        
        p = boxloc + Vec3(-0.1, 0.0, 0.0)
        World.usernameBox = DirectEntry(text = "" , pos = p, scale=.05, initialText="", numLines = 1)
        # Username textbox where you type in your username
        
        p = boxloc + Vec3(-0.5, -0.1, 0.0)        
        World.textObject = OnscreenText(text = "Password:", pos = p, scale = 0.07,fg=(1, 1, 1, 1),align=TextNode.ALeft)
        # "Password: " text that appears beside the password box
        
        p = boxloc + Vec3(-0.1, 0, -0.1)
        World.passwordBox = DirectEntry(text = "" , pos = p, scale=.05, initialText="", numLines = 1, obscured = 1)
        # Password textbox where you type in your password
        # Note - obscured = 1 denotes that all text entered will be replaced 
        # with a * like a standard password box
        
        p = boxloc + Vec3(0, 0, -0.2)
        World.loginButton = DirectButton(text = ("Login", "Login", "Login", "Login"), pos = p, scale = 0.075, command=self.attemptLogin)
        # The 'Login' button that will trigger the attemptLogin function 
        # when clicked
        
        p = boxloc + Vec3(-0.5, -0.4, 0)
        World.statusText = OnscreenText(text = "", pos = p, scale = 0.05, fg = (1, 0, 0, 1), align=TextNode.ALeft)
        # A simple text object that you can display an error/status messages 
        # to the user
        
    def updateStatus(self, statustext):
        self.World.statusText.setText(statustext)
        # all this does is change the status text.
        
    def attemptLogin(self):
        # checks to make sure the user inputed a username and password:
        #       if they didn't it will spit out an error message
        #       if they did, it will try to connect to the login server 
        #               (under construction)
        
        if(self.World.usernameBox.get() == ""):
            if(self.World.passwordBox.get() == ""):
                self.updateStatus("ERROR: You must enter a username and password before logging in.")
            else:
                self.updateStatus("ERROR: You must specify a username")
            self.World.passwordBox['focus'] = 0
            self.World.usernameBox['focus'] = 1
                
        elif(self.World.passwordBox.get() == ""):
            self.updateStatus("ERROR: You must enter a password")
            self.World.usernameBox['focus'] = 0
            self.World.passwordBox['focus'] = 1
            
        else:
            self.updateStatus("Attempting to login...")
            print "Attempting to connect to Server with credentials: (" + self.World.usernameBox.get() + ", " + self.World.passwordBox.get() + ")"
            #
            # this is where the networking code will get put in
            #
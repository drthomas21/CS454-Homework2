from direct.showbase.ShowBase import ShowBase
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator

from panda3d.core import ConnectionWriter
from panda3d.core import NetDatagram
from panda3d.core import QueuedConnectionListener
from panda3d.core import QueuedConnectionManager
from panda3d.core import QueuedConnectionReader

import random

class MyApp(ShowBase):
	def __init__(self):
		ShowBase.__init__(self)
		
		self.cManager = QueuedConnectionManager()
		self.cListener = QueuedConnectionListener(self.cManager, 0)
		self.cReader = QueuedConnectionReader(self.cManager, 0)
		self.cWriter = ConnectionWriter(self.cManager, 0)
		
		host = "10."
    	port = 9252
		self.connection = self.cManager.openTCPClientConnection(host, port, 10000)
		
		self.received = 1
		
		if self.connection:
                	self.cReader.addConnection(self.connection)                	
			#taskMgr.add(self.updateRoutine, 'updateRoutine')
			taskMgr.doMethodLater(3, self.updateRoutine, 'updateRoutine')
			
	def composeStringMessage(self, msg):
		myPyDatagram = PyDatagram()
		myPyDatagram.addString(msg)
		return myPyDatagram
				
	def retrieveStringMessage(self,datagram):
		myIterator = PyDatagramIterator(datagram)
		msg = myIterator.getString()
		print msg, " received"
    	
    	def sendRequest(self):
    		if(self.received):
    			print "->Client request:"
    			# Send a request to the server
			mylist = ["apple", "ball", "cat", "dog"] 
			
			msg = random.choice(mylist)
			request = self.composeStringMessage(msg)
			ack = self.cWriter.send(request,self.connection)				
			print msg, " sent"
			self.received = 0
		
	def receiveResponse(self):
		print "<-Server response:"
		while self.cReader.dataAvailable():
			datagram = NetDatagram()
			# Retrieve the contents of the datagram.
			if self.cReader.getData(datagram):
				self.retrieveStringMessage(datagram)
				self.received = 1
			
			
    	
    	def communicate(self):
    		#print "communicate"
		self.sendRequest()
		self.receiveResponse()		
    
	def updateRoutine(self,task):
		self.communicate()
		return task.again;

app = MyApp()
app.run() #enters the panda3D main loop
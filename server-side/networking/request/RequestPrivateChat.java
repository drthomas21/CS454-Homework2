package networking.request;

// Java Imports
import java.io.IOException;

import core.GameClient;
import networking.response.ResponsePrivateChat;
// Custom Imports
//import core.GameServer;
import utility.DataReader;

public class RequestPrivateChat extends GameRequest {

    // Data
    private String message;
    private String username;
    // Responses
    private ResponsePrivateChat responsePrivateChat;

    public RequestPrivateChat() {
    	 
      //  responses.add(responseString = new ResponseString());
    	responsePrivateChat = new ResponsePrivateChat();
      
    }

    @Override
    public void parse() throws IOException {
    	username = DataReader.readString(dataInput);
        message = DataReader.readString(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
        System.out.println(message);
        responsePrivateChat.setMessage(message);
        client.getServer().addResponseForUser(username, responsePrivateChat);
         
        
    }
}

package networking.request;

// Java Imports
import java.io.IOException;

import networking.response.GameResponse;
import networking.response.ResponseChat;
// Custom Imports
//import core.GameServer;
import utility.DataReader;

public class RequestChat extends GameRequest {

    // Data
    private String message;
    // Responses
    private ResponseChat responseString;

    public RequestChat() {
    	 
      //  responses.add(responseString = new ResponseString());
    	responseString = new ResponseChat();
      
    }

    @Override
    public void parse() throws IOException {
        message = DataReader.readString(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
        System.out.println(message);
        responseString.setMessage(message); 
        super.client.getServer().addResponseForAllOnlinePlayers(super.client.getId(), (GameResponse) responseString); 
    }
}

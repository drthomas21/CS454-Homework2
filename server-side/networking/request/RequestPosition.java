package networking.request;

// Java Imports
import java.io.IOException;

import networking.response.GameResponse;
import networking.response.ResponseChat;
import networking.response.ResponsePosition;
// Custom Imports
//import core.GameServer;
import utility.DataReader;

public class RequestPosition extends GameRequest {

    // Data
    private String position;
    private int x, y, z; 
    // Responses
    private ResponsePosition responsepos;

    public RequestPosition() {
    	 
      //  responses.add(responseString = new ResponseString());
    	responsepos = new ResponsePosition();
      
    }

    @Override
    public void parse() throws IOException {
       position = DataReader.readString(dataInput);
       String[] parts = position.split(",");
       x = Integer.parseInt(parts[0]);
       y = Integer.parseInt(parts[1]);
       z = Integer.parseInt(parts[2]);
    }

    @Override
    public void doBusiness() throws Exception {
        responsepos.setPosition(x, y, z); 
        super.client.getServer().addResponseForAllOnlinePlayers(super.client.getId(), (GameResponse) responsepos); 
    }
}

package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
//import core.GameServer;
import networking.response.ResponseString;
import utility.DataReader;

public class RequestChat extends GameRequest {

    // Data
    private String message;
    // Responses
    private ResponseString responseString;

    public RequestChat() {
        responses.add(responseString = new ResponseString());
    }

    @Override
    public void parse() throws IOException {
        message = DataReader.readString(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
        responseString.setMessage(message);
        System.out.println(responseString);
        super.client.getServer().addResponseForAllOnlinePlayers(super.client.getId(), responseString); 
        
    }
}

package networking.request;

// Java Imports
import java.io.IOException;

import dataAccessLayer.Connexion;
import networking.response.ResponseSaveexit;
// Custom Imports
//import core.GameServer;
import networking.response.ResponseString;
import utility.DataReader;

public class RequestSaveexit extends GameRequest {

    // Data
    private String position;
    //private double x, y, z;
    // Responses
    private ResponseSaveexit responseSE;

    public RequestSaveexit() {
        responses.add(responseSE = new ResponseSaveexit());
    }

    @Override
    public void parse() throws IOException {
    	 position = DataReader.readString(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
    	
    	//Need to handle the saving
    	Connexion db = client.getServer().getDAO();
    	db.saveAndExit(position, client.getPlayer().getID(), client.getPlayer().getCharacter());
        responseSE.setAnswer((short)1);
        client.stopClient();
        
    }
}

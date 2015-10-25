package networking.request;

// Java Imports
import java.io.IOException;

import database.Connexion;
import networking.response.ResponseSaveexit;
// Custom Imports
//import core.GameServer;
import networking.response.ResponseString;
import utility.DataReader;

public class RequestSaveexit extends GameRequest {

    // Data
    private String position;
    private int x, y, z;
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
    	Connexion db = new Connexion();
    	db.saveAndExit(position, client.getPlayerId(), client.getCharacter());
        responseSE.setAnswer((short)1);
        
    }
}

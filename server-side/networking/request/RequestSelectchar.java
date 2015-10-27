package networking.request;

// Java Imports
import java.io.IOException;

import networking.response.ResponseInt;
import networking.response.ResponseSelectchar;
// Custom Imports
//import core.GameServer;
import utility.DataReader;

public class RequestSelectchar extends GameRequest {
	private String character;
	private ResponseSelectchar response; 

	public RequestSelectchar() {
	    responses.add(response = new ResponseSelectchar());

	}

	@Override
	public void parse() throws IOException {

		character = DataReader.readString(dataInput);
	}

	@Override
	public void doBusiness() throws Exception {

		client.getPlayer().setCharacter(character);
		
		
		//Should return last position from the database
		response.setMessage("1, 2, 0");
		
		
		
	
		

	}
}

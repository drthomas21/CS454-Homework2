package networking.request;

// Java Imports
import java.io.IOException;

import dataAccessLayer.Connexion;
import networking.response.GameResponse;
import networking.response.ResponseInt;
import networking.response.ResponseOnline;
import networking.response.ResponseSelectchar;
// Custom Imports
//import core.GameServer;
import utility.DataReader;

public class RequestSelectchar extends GameRequest {
	private String character;
	private ResponseSelectchar responseSelect;
	private ResponseOnline responseOnline;
	private String x, y, z, position;

	public RequestSelectchar() {
		responses.add(responseSelect = new ResponseSelectchar());
		responseOnline = new ResponseOnline();

	}

	@Override
	public void parse() throws IOException {

		character = DataReader.readString(dataInput);
	}

	@Override
	public void doBusiness() throws Exception {

		client.getPlayer().setCharacter(character);

		// Should return last position from the database
		Connexion db = client.getServer().getDAO();
		position = db.lastPostion(client.getPlayer().getUsername(), client.getPlayer().getID());
		if(position != null)
		{
		String data[] = position.split(",");
		x = data[0];
		y = data[1];
		z = data[2];

		responseSelect.setPosition(Double.parseDouble("x"), Double.parseDouble("y"), Double.parseDouble("z"));
	
		}
		else {
			responseSelect.setPosition();
			
		}
		// Sending the new online player to every users
		responseOnline.setUser(client.getPlayer().getUsername());
		client.getServer().addResponseForAllOnlinePlayers(client.getId(), (GameResponse) responseOnline);

	}
}

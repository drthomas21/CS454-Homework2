package networking.request;

// Java Imports
import java.io.IOException;

import dataAccessLayer.Connexion;
// Custom Imports
//import core.GameServer;
import networking.response.ResponseInt;
import networking.response.ResponseRegister;
import utility.DataReader;
import utility.Player;

public class RequestRegister extends GameRequest {

	// Data
	private String username;
	private String password;
	// Responses
	private ResponseRegister responseRegister;
	private int player_id; 

	public RequestRegister() {
		responses.add(responseRegister = new ResponseRegister());
	}

	@Override
	public void parse() throws IOException {
		username = DataReader.readString(dataInput);
		password = DataReader.readString(dataInput);
	}

	@Override
	public void doBusiness() throws Exception {

		Connexion db = client.getServer().getDAO();
		player_id = db.create(username, password);
		if (player_id != 0) {
			responseRegister.setNumber(1);
			client.setPlayer(new Player(username, player_id));
		} else {
			responseRegister.setNumber(0);
		}

	}
}

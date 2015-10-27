package networking.request;

// Java Imports
import java.io.IOException;

import dataAccessLayer.Connexion;
import networking.response.GameResponse;
import networking.response.ResponseAuth;
import networking.response.ResponseOnline;
// Custom Imports
//import core.GameServer;
import utility.DataReader;
import utility.Player;

public class RequestAuth extends GameRequest {

	// Data
	private String username;
	private String password;
	// Responses
	private ResponseAuth responseAuth;
	private int player_id;
	private ResponseOnline responseOnline; 

	public RequestAuth() {
		responses.add(responseAuth = new ResponseAuth());
		responseOnline = new ResponseOnline(); 
	}

	@Override
	public void parse() throws IOException {
		username = DataReader.readString(dataInput);
		password = DataReader.readString(dataInput);
	}

	@Override
	public void doBusiness() throws Exception {

		Connexion db = client.getServer().getDAO();
		player_id = db.checkAuth(username, password);
		if (player_id != -1) {
			System.out.println("Connected !");
			responseAuth.setAnswer((short)1);
			client.setPlayer(new Player(username, player_id));
			//Sending the new online player to every users
			responseOnline.setCharacter(username);
			client.getServer().addResponseForAllOnlinePlayers(super.client.getId(), (GameResponse) responseOnline); 
		} else {
			System.out.println("Wrong credentials");
			responseAuth.setAnswer((short)0);
		}
	
		
		

	}
}

package networking.request;

// Java Imports
import java.io.IOException;

import core.GameClient;
import dataAccessLayer.Connexion;
import networking.response.GameResponse;
import networking.response.ResponseInt;
import networking.response.ResponseOnline;
import networking.response.ResponseSelectchar;
// Custom Imports
//import core.GameServer;
import utility.DataReader;
import utility.Player;

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
		position = db.lastPostion(character, client.getPlayer().getID());
		if (position != null) {
			String data[] = position.split(",");

			x = data[0];
			y = data[1];
			z = data[2];

			responseSelect.setPosition(Double.valueOf(x).longValue(), Double.valueOf(y).longValue(),
					Double.valueOf(z).longValue());

			// Sending the list of online clients
			for (Player player : client.getServer().getActivePlayers()) {
				ResponseOnline onlineclient = new ResponseOnline();
				onlineclient.setUsername(player.getUsername());
				onlineclient.setCharacter(player.getCharacter());
				responses.add(onlineclient);
			}
		} else { //If the character's player is new, empty array
			responseSelect.setPosition();
		}
		//The player is now active
		client.getServer().setActivePlayer(client.getPlayer());
		// Sending the new online player to every users
		responseOnline.setUsername(client.getPlayer().getUsername());
		responseOnline.setCharacter(client.getPlayer().getCharacter());
		client.getServer().addResponseForAllOnlinePlayers(client.getId(), (GameResponse) responseOnline);

	}
}

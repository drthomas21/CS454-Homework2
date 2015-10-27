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
	private double x, y, z;
	private Boolean skipbusiness;
	// Responses
	private ResponsePosition responsepos;

	public RequestPosition() {

		// responses.add(responseString = new ResponseString());
		responsepos = new ResponsePosition();
		skipbusiness = false;

	}

	@Override
	public void parse() throws IOException {
		position = DataReader.readString(dataInput);
		String[] parts = position.split(",");
		try {
			x = Double.parseDouble(parts[0]);
			y = Double.parseDouble(parts[1]);
			z = Double.parseDouble(parts[2]);
		} catch (Exception e) {
			this.skipbusiness = true;
			e.printStackTrace();
		}
	}

	@Override
	public void doBusiness() throws Exception {
		if (skipbusiness == false) {
			responsepos.setPosition(x, y, z);
			responsepos.setUsername(client.getPlayer().getUsername());
			client.getServer().addResponseForAllOnlinePlayers(client.getId(), responsepos);
		}
	}
}

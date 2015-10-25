package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
//import core.GameServer;
import utility.DataReader;

public class RequestSelectchar extends GameRequest {
	private String character;

	public RequestSelectchar() {

	}

	@Override
	public void parse() throws IOException {

		character = DataReader.readString(dataInput);
	}

	@Override
	public void doBusiness() throws Exception {

		client.setCharacter(character);

	}
}

package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
//import core.GameServer;
import networking.response.ResponseInt;
import utility.DataReader;
import database.Connexion;

public class RequestRegister extends GameRequest {

	// Data
	private String username;
	private String password;
	// Responses
	private ResponseInt responseInt;

	public RequestRegister() {
		responses.add(responseInt = new ResponseInt());
	}

	@Override
	public void parse() throws IOException {
		username = DataReader.readString(dataInput);
		password = DataReader.readString(dataInput);
	}

	@Override
	public void doBusiness() throws Exception {

		Connexion db = new Connexion();
		db.create(username, password);

	}
}

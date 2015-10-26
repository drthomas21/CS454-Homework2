package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
//import core.GameServer;
import networking.response.ResponseInt;
import networking.response.ResponseRegister;
import utility.DataReader;
import database.Connexion;

public class RequestRegister extends GameRequest {

	// Data
	private String username;
	private String password;
	// Responses
	private ResponseRegister responseRegister;

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
		System.out.println("Hey");

		Connexion db = new Connexion();
		if (db.create(username, password) == 1) {
			responseRegister.setNumber(1);
		} else {
			responseRegister.setNumber(0);
		}

	}
}

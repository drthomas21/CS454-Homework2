package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
//import core.GameServer;
import networking.response.ResponseInt;
import utility.DataReader;
import database.Connexion;

public class RequestAuth extends GameRequest {

	// Data
	private String username;
	private String password;
	// Responses
	private ResponseInt responseInt;

	public RequestAuth() {
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

		if (db.checkAuth(username, password)) {
			System.out.println("Connected !");
			responseInt.setNumber(1);
		} else {
			System.out.println("Wrong credentials");
			responseInt.setNumber(0);
		}

	}
}

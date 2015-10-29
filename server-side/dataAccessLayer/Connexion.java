package dataAccessLayer;

import java.sql.*;
import java.util.*;

public class Connexion {

	protected Connection conn;
	protected Statement stmt;
	protected ResultSet rset;
	protected ResultSetMetaData rsetMeta;
	protected PreparedStatement pstmt;

	public String userName = "panda";
	public String password = "panda";
	public String serverName = "localhost";
	public String portNumber = "8889";

	// Connection to Database
	public Connexion() throws SQLException, ClassNotFoundException {

		try {
			Properties connectionProps = new Properties();

			// setproperty only accept the string.
			connectionProps.setProperty("user", this.userName);
			connectionProps.setProperty("password", this.password);

			conn = DriverManager.getConnection("jdbc:mysql://" + this.serverName + ":" + this.portNumber + "/panda",
					connectionProps);

		} catch (Exception e) {
			System.out.println("Connexion failure with the database :" + e);
			e.printStackTrace();

		}
	}

	// close the connection
	public void close() {
		try {
			stmt.close();
			conn.close();
		} catch (Exception e) {
			System.out.println("exception in close :" + e);
		}
	}

	public Connection getInstance() {
		return conn;
	}

	// get character ID from a name
	public int characterIDFromName(String name) throws SQLException {
		try {
			String selectSQL = "SELECT * FROM CharacterList WHERE name = ?";
			PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
			System.out.println("Name : " + name);
			preparedStatement.setObject(1, name);
			ResultSet rs = preparedStatement.executeQuery();
			while (rs.next()) {
				System.out.println("id_character : "+ rs.getInt("idCharacter"));
				return rs.getInt("idCharacter");
			}

		} catch (Exception e) {
			System.out.println("Exception in connect :" + e);
			e.printStackTrace();
		}
		return -1;

	}

	//Saving last position of character on exit
	public void UpdateIsPlaying(int player_id, int characterID, String position) throws SQLException {
		//Boolean to know if it's the first time this player disconnect with this character
		boolean result = false; 
		System.out.println(position);
		try {
			//Finding the row to update
			String selectSQL = "SELECT * FROM isPlaying WHERE Character_idCharacter = ? AND Player_idPlayer = ?";
			PreparedStatement preparedStatement = conn.prepareStatement(selectSQL, rset.TYPE_SCROLL_INSENSITIVE,rset.CONCUR_UPDATABLE);
			preparedStatement.setObject(1, characterID);
			preparedStatement.setObject(2, player_id);
			rset = preparedStatement.executeQuery();
			while (rset.next()) {
				//Updating the row
				String selectSQL2 = "UPDATE isPlaying SET lastPosition  = ? WHERE Character_idCharacter = ? AND Player_idPlayer = ?";
				PreparedStatement preparedStatement2 = conn.prepareStatement(selectSQL2);
				preparedStatement2.setObject(1, position);
				preparedStatement2.setObject(2, characterID);
				preparedStatement2.setObject(3, player_id);
				preparedStatement2.executeUpdate();
				result = true; 
				System.out.println("Hey");
			}
			if (result == false) //If the row doesn't exixt (first time) creating it
			{
				String requete = "INSERT INTO isPlaying (Character_idCharacter, Player_idPlayer, lastPosition) VALUES (?, ?, ?)";
				pstmt = conn.prepareStatement(requete);

				pstmt.setObject(1, characterID);
				pstmt.setObject(2, player_id);
				pstmt.setObject(3, position);
			
				pstmt.executeUpdate();
			}
		} catch (Exception e) {
			System.out.println("Exception in connect :" + e);
			e.printStackTrace();
		}

	}

	//Getting the data and saving the last position
	public void saveAndExit(String position, int player_id, String character)
			throws SQLException, ClassNotFoundException {

		// Getting chracterID from charactername
		int characterID = characterIDFromName(character);

		UpdateIsPlaying(player_id, characterID, position);

	}

	//Creating a new player in the database
	public int create(String username, String password) throws SQLException {
		try {

			stmt = conn.createStatement();
			String requete = "INSERT INTO Player (username, password) VALUES (?, ?)";
			pstmt = conn.prepareStatement(requete);

			pstmt.setObject(1, username);
			pstmt.setObject(2, password);
			pstmt.executeUpdate();
			System.out.println("Created a new player");
			return getPlayerID(username);

		} catch (Exception e) {
			System.out.println("User is already created :" + e);
			e.printStackTrace();
			return 0;
		}

	}

	// Player authentication
	public int checkAuth(String username, String password) throws SQLException {
		String selectSQL = "SELECT * FROM Player WHERE username=? AND password =?";
		PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
		preparedStatement.setObject(1, username);
		preparedStatement.setObject(2, password);
		ResultSet rs = preparedStatement.executeQuery();
		while (rs.next()) {
			return rs.getInt("idPlayer");
		}
		return -1;

	}

	//Get player ID from username (on creating)
	public int getPlayerID(String username) {
		try {
			String selectSQL = "SELECT idPlayer FROM Player WHERE username = ?";
			PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
			preparedStatement.setObject(1, username);
			ResultSet rs = preparedStatement.executeQuery();
			while (rs.next()) {
				return rs.getInt("idPlayer");
			}
		} catch (Exception e) {
			System.out.println("Exception in connect :" + e);
			e.printStackTrace();
		}
		return 0;

	}

	//Get the last position for the character - on login
	public String lastPostion(String charactername, int player_idPlayer) {
		String lastPosition = null;
		try {		
			String selectSQL = "SELECT lastPosition FROM isPlaying WHERE Character_idCharacter = ? AND Player_idPlayer = ?";
			PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
			preparedStatement.setObject(1, characterIDFromName(charactername));
			preparedStatement.setObject(2, player_idPlayer);
			ResultSet rs = preparedStatement.executeQuery();
			while (rs.next()) {
				lastPosition = rs.getString("lastPosition");
			}
		} catch (Exception ae) {
			ae.printStackTrace();
		}

		return lastPosition;
	}
}
package dataAccessLayer;

import java.sql.*;
import java.util.*;
import networking.response.ResponseString;

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
			System.out.println("Exception in connect :" + e);
			e.printStackTrace();
			try {
				conn.close();
			} catch (Exception ee) {
			}
		}
	}

	// close the connection after every commit
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
			String selectSQL = "SELECT idCharacter FROM Character WHERE name = ?";
			PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
			preparedStatement.setObject(1, name);
			ResultSet rs = preparedStatement.executeQuery();
			while (rs.next()) {
				return rs.getInt("idCharacter");
			}

		} catch (Exception e) {
			System.out.println("Exception in connect :" + e);
			e.printStackTrace();
			try {
				conn.close();
			} catch (Exception ee) {
			}
		}
		return -1;

	}

	// last position of character
	public void UpdateIsPlaying(int player_id, int characterID, String position) throws SQLException {
		try {
			String selectSQL = "SELECT idIsPlaying FROM Users isPlaying WHERE Character_idCharacter = ? AND Player_idPlayer = ?";
			PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
			preparedStatement.setObject(1, characterID);
			preparedStatement.setObject(2, player_id);
			ResultSet rs = preparedStatement.executeQuery();
			while (rs.next()) {
				rs.updateString("lastPosition", position);
			}
		} catch (Exception e) {
			System.out.println("Exception in connect :" + e);
			e.printStackTrace();
		}

	}

	public void saveAndExit(String position, int player_id, String character)
			throws SQLException, ClassNotFoundException {

		// Getting chracterID from charactername
		int characterID = characterIDFromName(character);

		UpdateIsPlaying(player_id, characterID, position);

	}

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
}
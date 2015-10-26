package database;

import java.sql.*;
import java.util.*;
import networking.response.ResponseString;

public class Connexion {

	protected Connection conn;
	protected Statement stmt;
	protected ResultSet rset;
	protected ResultSetMetaData rsetMeta;
	protected PreparedStatement pstmt;

	// static public Connection conn;
	// static public Statement stmt;
	// static public ResultSet rset;
	// static public ResultSetMetaData rsetMeta;
	// static public PreparedStatement pstmt;

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

			// connectionProps.put("user", this.userName);
			// connectionProps.put("password", this.password);
			// connectionProps.put("password", this.password);

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

	// authentication of user
	public int checkAuth(String username, String password) throws SQLException {
		String selectSQL = "SELECT * FROM Credentials WHERE username=? AND password =?";
		PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
		preparedStatement.setObject(1, username);
		preparedStatement.setObject(2, password);
		ResultSet rs = preparedStatement.executeQuery();
		while (rs.next()) {
			return rs.getInt("Player_idPlayer");
		}
		return -1;

	}

	boolean UserIsNotExist;

	private ResponseString responseString;

	// store the username and password into db
	public int create(String username, String password) throws SQLException {
		try {

			stmt = conn.createStatement();
			String requete = "insert into Credentials values (?, ?)";

			pstmt = conn.prepareStatement(requete);

			pstmt.setObject(1, username);
			pstmt.setObject(2, password);
			pstmt.executeUpdate();
			close();
			return 1; 

		} catch (Exception e) {
			responseString.setMessage("User is already created");

			System.out.println("User is already created :" + e);
			e.printStackTrace();
			
		

			try {
				conn.close();
			} catch (Exception ee) {
			}
			return 0; 
		}

	}

	// character id of selected player
	public int characterIDFromName(String name) throws SQLException {
		try {
			String selectSQL = "SELECT idCharacter FROM Character WHERE name = ?";
			PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
			preparedStatement.setObject(1, name);
			ResultSet rs = preparedStatement.executeQuery();
			close();
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
			try {
				conn.close();
			} catch (Exception ee) {
			}
		}

	}

	public void saveAndExit(String position, int player_id, String character) throws SQLException {

		// Getting chracterID from charactername

		int characterID = characterIDFromName(character);
		UpdateIsPlaying(player_id, characterID, position);

	}

}
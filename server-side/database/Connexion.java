package database;

import java.sql.*;
import java.util.Date;
import java.util.*;

public class Connexion {

	static public Connection conn;
	static public Statement stmt;
	static public ResultSet rset;
	static public ResultSetMetaData rsetMeta;
	static public PreparedStatement pstmt;
	public String userName = "panda";
	public String password = "panda";
	public String serverName = "localhost";
	public String portNumber = "8889";

	public Connexion() throws SQLException, ClassNotFoundException {

		    Properties connectionProps = new Properties();
		    connectionProps.put("user", this.userName);
		    connectionProps.put("password", this.password);
		    connectionProps.put("password", this.password);

		
		    conn = DriverManager.getConnection(
		                   "jdbc:mysql://" +
		                   this.serverName +
		                   ":" + this.portNumber + "/panda",
		                   connectionProps);
		   


	}
	
	public int checkAuth(String username, String password) throws SQLException
	{
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
	
	public void create(String username, String password) throws SQLException
	{
		stmt = conn.createStatement();
		String requete = "insert into Credentials values (?, ?)";

		pstmt = conn.prepareStatement(requete);

		pstmt.setObject(1, username);
		pstmt.setObject(2, password);
		pstmt.executeUpdate();
	}
	
	public int characterIDFromName(String name) throws SQLException
	{
		
		String selectSQL = "SELECT idCharacter FROM Character WHERE name = ?";
		PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
		preparedStatement.setObject(1, name);
		ResultSet rs = preparedStatement.executeQuery();
		while (rs.next()) {
		return rs.getInt("idCharacter");
		}
		return -1;  
	}
	
	public void UpdateIsPlaying(int player_id, int characterID, String position) throws SQLException
	{
		
		String selectSQL = "SELECT idIsPlaying FROM Users isPlaying WHERE Character_idCharacter = ? AND Player_idPlayer = ?";
		PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
		preparedStatement.setObject(1, characterID);
		preparedStatement.setObject(2, player_id);
		ResultSet rs = preparedStatement.executeQuery();
		while (rs.next()) {
			 rs.updateString("lastPosition", position);
		}
		
	}
	
	public void saveAndExit(String position, int player_id, String character) throws SQLException
	{
		
		//Getting chracterID from charactername
		
		int characterID = characterIDFromName(character);
		UpdateIsPlaying(player_id, characterID, position);		
		
	}

}

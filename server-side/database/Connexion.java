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
	
	public boolean checkAuth(String username, String password) throws SQLException
	{
		String selectSQL = "SELECT username, password FROM Users WHERE username=? AND password =?";
		PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
		preparedStatement.setObject(1, username);
		preparedStatement.setObject(2, password);
		ResultSet rs = preparedStatement.executeQuery();
		while (rs.next()) {
		return true; 
		}
		return false; 
		
	}
	
	public void create(String username, String password) throws SQLException
	{
		
		stmt = conn.createStatement();
		String requete = "insert into users values (?, ?)";

		pstmt = conn.prepareStatement(requete);

		pstmt.setObject(1, username);
		pstmt.setObject(2, password);
		pstmt.executeUpdate();

		
	}

}

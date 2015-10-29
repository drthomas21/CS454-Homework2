package utility;

public class Player {

	private String username;
	private int player_id;
	private String character;

	public Player(String username, int player_id) {
		this.username = username;
		this.player_id = player_id;
	}

	public String getUsername() {
		return this.username;
	}

	public String getCharacter() {
		return this.character;
	}

	public void setCharacter(String character) {
		this.character = character;
	}
	
	public int getID()
	{
		return this.player_id;
	}
}

package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseOnline extends GameResponse {

    private String username;
    private String character;

    public ResponseOnline() {
        responseCode = Constants.SMSG_ONLINE;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);    
        packet.addString(username);
        packet.addString(character);
        return packet.getBytes();
    }
    
	public String getUsername() {
		return username;
	}

	public void setUsername(String username) {
		this.username = username;
	}
	public String getCharacter()
	{
		return character;
	}
	public void setCharacter(String character)
	{
		this.character = character;
	}
}
